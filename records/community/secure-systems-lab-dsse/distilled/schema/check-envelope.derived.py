#!/usr/bin/env python3
# DERIVED - not verbatim. Written by this library, not copied from the DSSE
# specification. Checks envelope.derived.schema.json against the instances in
# ../examples/cases.derived.json: every ACCEPT instance must validate, every
# REJECT instance must fail AND for the stated reason, and a mutation pass
# removes every asserting keyword in turn (equivalent mutants excepted, with
# the reason) and requires each removal to flip a case ("a schema that parses
# is not a schema that binds"). An insertion pass adds the constraints the
# source does NOT make (additionalProperties:false, a required keyid, minItems,
# minLength) and requires each to flip an accept case, so the permissive
# behaviour (consumers MUST ignore unknown fields, unset == empty) is bound too.
#
#   python3 -I check-envelope.derived.py
#
# Stdlib only (no jsonschema in this repo's toolchain). The validator below
# implements exactly the keywords the schema uses (plus those the insertion
# mutants add) and RAISES on any other keyword, so a schema edit that outgrows
# it fails loudly instead of being silently ignored. Patterns use ECMA-262
# anchoring: a final '$' matches only at the end of the string, never before a
# trailing newline as Python's does. contentEncoding is ASSERTED here; standard
# validators only annotate it.
import base64, binascii, copy, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA = os.path.join(HERE, "envelope.derived.schema.json")
CASES = os.path.join(HERE, "..", "examples", "cases.derived.json")

ANNOTATION = {"$schema", "$id", "$comment", "$defs", "title", "x-open"}
ASSERTING = {"type", "required", "properties", "items", "pattern", "$ref", "minItems",
             "contentEncoding", "additionalProperties", "minLength"}
# keywords the SCHEMA may use; the others exist only so insertion mutants can run
USED_BY_SCHEMA = ASSERTING - {"additionalProperties", "minLength"}


def jtype(v):
    if v is None: return "null"
    if isinstance(v, bool): return "boolean"
    if isinstance(v, int): return "integer"
    if isinstance(v, float): return "number"
    if isinstance(v, str): return "string"
    if isinstance(v, list): return "array"
    return "object"


def type_ok(v, t):
    return jtype(v) == t or (t == "number" and jtype(v) == "integer")


def ecma_search(pat, s):
    if pat.endswith("$") and not pat.endswith("\\$"):
        pat = pat[:-1] + r"\Z"
    return re.search(pat, s) is not None


def decode_b64(s):
    """The content check: what the pattern cannot say. Alphabet is the pattern's job."""
    std, url = set("+/"), set("-_")
    if any(c in std for c in s) and any(c in url for c in s):
        raise ValueError("mixes the standard and url-safe alphabets")
    t = s.rstrip("=")
    if len(t) % 4 == 1:
        raise ValueError("impossible base64 length")
    pad = len(s) - len(t)
    if pad and (len(s) % 4 != 0 or pad != -len(t) % 4):
        raise ValueError(f"{pad} padding character(s) do not complete a multiple of 4")
    t = t.replace("-", "+").replace("_", "/")
    return base64.b64decode(t + "=" * (-len(t) % 4), validate=True)


class V:
    def __init__(self, schema):
        self.root = schema
        self.used = set()

    def ref(self, r):
        assert r.startswith("#/"), r
        n = self.root
        for p in r[2:].split("/"):
            n = n[p]
        return n

    def check(self, sch, inst, path, errs):
        for k in sch:
            if k not in ANNOTATION and k not in ASSERTING:
                raise SystemExit(f"validator does not implement keyword {k!r}")
        if "$ref" in sch:
            self.used.add("$ref")
            self.check(self.ref(sch["$ref"]), inst, path, errs)
        if "type" in sch:
            self.used.add("type")
            if not type_ok(inst, sch["type"]):
                errs.append(f"{path or '/'} type: want {sch['type']}, got {jtype(inst)}")
                return
        if "pattern" in sch and isinstance(inst, str):
            self.used.add("pattern")
            if not ecma_search(sch["pattern"], inst):
                errs.append(f"{path or '/'} pattern: {inst!r} does not match")
        if "minLength" in sch and isinstance(inst, str):
            self.used.add("minLength")
            if len(inst) < sch["minLength"]:
                errs.append(f"{path or '/'} minLength {sch['minLength']}")
        if isinstance(inst, dict):
            for r in sch.get("required", []):
                self.used.add("required")
                if r not in inst:
                    errs.append(f"{path or '/'} required {r}")
            for k, sub in sch.get("properties", {}).items():
                self.used.add("properties")
                if k in inst:
                    self.check(sub, inst[k], f"{path}/{k}", errs)
            if sch.get("additionalProperties") is False:
                self.used.add("additionalProperties")
                for k in inst:
                    if k not in sch.get("properties", {}):
                        errs.append(f"{path}/{k} additionalProperties")
        if isinstance(inst, list):
            if "items" in sch:
                self.used.add("items")
                for i, x in enumerate(inst):
                    self.check(sch["items"], x, f"{path}/{i}", errs)
            if "minItems" in sch:
                self.used.add("minItems")
                if len(inst) < sch["minItems"]:
                    errs.append(f"{path or '/'} minItems {sch['minItems']}")
        if "contentEncoding" in sch and isinstance(inst, str) and not errs_at(errs, path):
            self.used.add("contentEncoding")
            try:
                decode_b64(inst)
            except (ValueError, binascii.Error) as e:
                errs.append(f"{path or '/'} content: base64: {e}")


def errs_at(errs, path):
    return any(e.startswith((path or "/") + " ") for e in errs)


def validate(schema, d, inst):
    v = V(schema)
    errs = []
    v.check(schema["$defs"][d], inst, "", errs)
    return errs, v.used


def outcome_ok(case, errs):
    """accept: no errors. reject: some error contains the stated reason."""
    if case["expect"] == "accept":
        return not errs
    return any(case["error_contains"] in e for e in errs)


# Removing these changes no instance's verdict or reason by construction.
EQUIVALENT = {}


def sites(schema):
    """Every asserting keyword in $defs, as a path of keys (properties descended into)."""
    out = []

    def walk(node, path):
        for k, v in node.items():
            if k in ASSERTING:
                out.append(path + (k,))
            if k == "properties":
                for pk, pv in v.items():
                    walk(pv, path + (k, pk))
            elif k == "items" and isinstance(v, dict):
                walk(v, path + (k,))
    for d, node in schema["$defs"].items():
        walk(node, (d,))
    return out


def removals(schema):
    out = []
    for p in sites(schema):
        if p in EQUIVALENT:
            continue
        s = copy.deepcopy(schema)
        n = s["$defs"]
        for k in p[:-1]:
            n = n[k]
        n.pop(p[-1])
        out.append((".".join(p) + ": removed", s))
    return out


# Constraints the source does NOT make. Each, added, must make some accept case fail.
INSERTIONS = [
    ("Envelope", (), "additionalProperties", False, "unknown top-level members must be ignored (R-0014, R-0015)"),
    ("Signature", (), "additionalProperties", False, "unknown members of a signature must be ignored (R-0014, R-0015)"),
    ("Signature", (), "required+keyid", None, "keyid is OPTIONAL (R-0012)"),
    ("Signature", ("properties", "keyid"), "minLength", 1, "an unset keyid is the same as set-but-empty (R-0013)"),
    ("Signature", ("properties", "sig"), "minLength", 1, "sig is 'set, even if empty' (R-0011)"),
    ("Envelope", ("properties", "payload"), "minLength", 1, "payload is 'set, even if empty' (R-0011)"),
    ("Envelope", ("properties", "payloadType"), "minLength", 1, "payloadType is 'set, even if empty' (R-0011)"),
    ("Envelope", ("properties", "signatures"), "minItems", 1, "signatures is 'set, even if empty' (envelope.md 2.1.2), in tension with the proto comment"),
    ("Base64Text", (), "pattern", "^[A-Za-z0-9+/]*={0,2}$", "URL-safe base64 must be accepted (R-0007)"),
    ("Base64Text", (), "pattern", "^[A-Za-z0-9_-]*={0,2}$", "standard base64 must be accepted (R-0007)"),
    ("Base64Text", (), "pattern", "^[A-Za-z0-9+/_-]*$", "'=' padding must be accepted (the vector's own payload has it)"),
    ("Base64Text", (), "pattern", "^[A-Za-z0-9+/_-]+={0,2}$", "an empty payload/sig must be accepted (R-0011)"),
]


def insertions(schema):
    out = []
    for d, path, kw, val, why in INSERTIONS:
        s = copy.deepcopy(schema)
        n = s["$defs"][d]
        for k in path:
            n = n[k]
        if kw == "required+keyid":
            n["required"] = list(n["required"]) + ["keyid"]
        else:
            n[kw] = val
        out.append((f"{d}{'.' + '.'.join(path) if path else ''}: add {kw}={val!r}" if kw != "required+keyid"
                    else f"{d}: require keyid", s, why))
    return out


def main():
    schema = json.load(open(SCHEMA))
    doc = json.load(open(CASES))
    cases = doc["cases"]
    fails = []
    n_acc = n_rej = n_open = 0
    reasons = 0
    ids = set()
    for c in cases:
        if c["id"] in ids:
            fails.append(f"duplicate case id {c['id']}")
        ids.add(c["id"])
        if not c.get("cites"):
            fails.append(f"{c['id']}: no cites")
        errs, _ = validate(schema, c["def"], c["instance"])
        if c["expect"] == "accept":
            n_acc += 1
            if errs:
                fails.append(f"{c['id']}: expected accept, got {errs}")
        elif c["expect"] == "reject":
            n_rej += 1
            if not errs:
                fails.append(f"{c['id']}: expected reject, accepted")
            else:
                want = c.get("error_contains")
                if not want:
                    fails.append(f"{c['id']}: reject case without error_contains")
                elif not any(want in e for e in errs):
                    fails.append(f"{c['id']}: rejected for the wrong reason: want {want!r}, got {errs}")
                else:
                    reasons += 1
        else:
            fails.append(f"{c['id']}: expect must be accept or reject")
        if c["basis"] == "source-silent":
            n_open += 1
        if c["basis"] not in ("source", "derived-assumption", "source-silent", "source-conflict"):
            fails.append(f"{c['id']}: bad basis")
    # every definition is exercised by at least one reject case, and at least one accept case
    for d in schema["$defs"]:
        for want in ("accept", "reject"):
            if not any(c["def"] == d and c["expect"] == want for c in cases):
                fails.append(f"definition {d} has no {want} case")
    # removal mutation pass: each removal must make some case miss its stated outcome
    flipped = {}
    for name, ms in removals(schema):
        changed = [c["id"] for c in cases if not outcome_ok(c, validate(ms, c["def"], c["instance"])[0])]
        flipped[name] = changed
        if not changed:
            fails.append(f"mutation {name!r} flips no case: that part of the schema binds nothing")
    # insertion mutation pass: each source-silent permission is bound by an accept case
    ins = {}
    for name, ms, why in insertions(schema):
        changed = [c["id"] for c in cases
                   if c["expect"] == "accept" and not outcome_ok(c, validate(ms, c["def"], c["instance"])[0])]
        ins[name] = changed
        if not changed:
            fails.append(f"insertion {name!r} flips no accept case: no case binds '{why}'")
    # keywords the schema uses are all exercised
    used = set()
    for c in cases:
        used |= validate(schema, c["def"], c["instance"])[1]
    in_schema = {p[-1] for p in sites(schema)}
    for k in sorted(in_schema - used):
        fails.append(f"keyword {k} appears in the schema but no case exercises it")
    print(f"cases examined: {len(cases)} (accept {n_acc}, reject {n_rej}; {n_open} pin source-silent behaviour)")
    print(f"reject cases rejected for the stated reason: {reasons}/{n_rej}")
    print(f"asserting keyword sites in the schema: {len(sites(schema))}; removal mutants examined: {len(flipped)} "
          f"({len(EQUIVALENT)} equivalent skipped); each flips at least one case: "
          f"{sum(1 for v in flipped.values() if v)}/{len(flipped)}")
    print(f"insertion mutants examined: {len(ins)}; each flips at least one accept case: "
          f"{sum(1 for v in ins.values() if v)}/{len(ins)}")
    print(f"keywords exercised: {', '.join(sorted(used))}")
    for f in fails:
        print("FAIL:", f)
    print("check-envelope: " + ("FAILED" if fails else "ok"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
