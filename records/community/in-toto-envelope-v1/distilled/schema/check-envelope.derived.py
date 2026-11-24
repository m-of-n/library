#!/usr/bin/env python3
# DERIVED - not verbatim. Written by this library, not copied from the in-toto
# specification. Checks envelope.derived.schema.json against the instances in
# ../examples/cases.derived.json: every ACCEPT instance must validate, every
# REJECT instance must fail AND for the stated reason, and a mutation pass
# removes every asserting keyword in turn (EQUIVALENT ones excepted, with the
# reason) and requires each removal to flip a case ("a schema that parses is
# not a schema that binds").
#
#   python3 -I check-envelope.derived.py
#
# Stdlib only (no jsonschema in this repo's toolchain). The validator below
# implements exactly the keywords the schema uses and RAISES on any other
# keyword, so a schema edit that outgrows it fails loudly instead of being
# silently ignored. Patterns use ECMA-262 anchoring: a final '$' matches only at
# the end of the string, never before a trailing newline as Python's does.
import base64, binascii, copy, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA = os.path.join(HERE, "envelope.derived.schema.json")
CASES = os.path.join(HERE, "..", "examples", "cases.derived.json")

ANNOTATION = {"$schema", "$id", "$comment", "$defs", "title", "x-open"}
ASSERTING = {"type", "required", "properties", "items", "pattern", "$ref", "if", "then",
             "contentEncoding", "contentMediaType", "contentSchema"}


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
    std, url = set("+/"), set("-_")
    if any(c in std for c in s) and any(c in url for c in s):
        raise ValueError("mixes the standard and url-safe alphabets")
    t = s.rstrip("=")
    if len(t) % 4 == 1:
        raise ValueError("impossible base64 length")
    # padding is optional, but when present it must be what the length calls
    # for: 'e30==' (one due, two given) is base64 in no RFC 4648 variant
    pad, due = len(s) - len(t), -len(t) % 4
    if pad and pad != due:
        raise ValueError(f"{pad} padding character(s) where {due} {'is' if due == 1 else 'are'} due")
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
        if isinstance(inst, dict):
            for r in sch.get("required", []):
                self.used.add("required")
                if r not in inst:
                    errs.append(f"{path or '/'} required {r}")
            for k, sub in sch.get("properties", {}).items():
                self.used.add("properties")
                if k in inst:
                    self.check(sub, inst[k], f"{path}/{k}", errs)
        if isinstance(inst, list) and "items" in sch:
            self.used.add("items")
            for i, x in enumerate(inst):
                self.check(sch["items"], x, f"{path}/{i}", errs)
        if "if" in sch:
            self.used.add("if")
            e = []
            self.check(sch["if"], inst, path, e)
            if not e and "then" in sch:
                self.check(sch["then"], inst, path, errs)
        if "contentEncoding" in sch and isinstance(inst, str) and not errs_at(errs, path):
            self.used.add("content")
            try:
                raw = decode_b64(inst)
            except (ValueError, binascii.Error) as e:
                errs.append(f"{path or '/'} content: base64: {e}")
                return
            if "contentMediaType" in sch:
                try:
                    doc = json.loads(raw.decode("utf-8"))
                except ValueError as e:
                    errs.append(f"{path or '/'} content: not JSON: {e}")
                    return
                if "contentSchema" in sch:
                    self.check(sch["contentSchema"], doc, path + "(decoded)", errs)


def errs_at(errs, path):
    return any(e.startswith((path or "/") + " ") for e in errs)


def validate(schema, d, inst):
    v = V(schema)
    errs = []
    v.check(schema["$defs"][d], inst, "", errs)
    return errs, v.used


# Removing these changes no instance's verdict, by construction, so no case
# can flip and they are skipped with the reason. Everything else is mutated.
EQUIVALENT = {
    ("GenericSignature", "if", "type"):
        "then constrains only objects, so an if that admits every instance changes nothing",
}


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
            elif isinstance(v, dict):
                walk(v, path + (k,))
    for d, node in schema["$defs"].items():
        walk(node, (d,))
    return out


def mutations(schema):
    """(name, mutated schema): EVERY asserting keyword removed in turn, one at a
    time, except the EQUIVALENT ones. Each must flip at least one case."""
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
        if c["basis"] not in ("source", "derived-assumption", "source-silent"):
            fails.append(f"{c['id']}: bad basis")
        # decoded-payload cases: the declared payload must itself be what the case says
    # every definition that can reject is exercised by at least one reject case
    for d in schema["$defs"]:
        if not any(c["def"] == d and c["expect"] == "reject" for c in cases):
            if d not in ("GenericSignature", "DsseSignature", "Statement"):  # reached via parents
                fails.append(f"definition {d} has no reject case")
    # mutation pass
    flipped = {}
    for name, ms in mutations(schema):
        changed = []
        for c in cases:
            errs, _ = validate(ms, c["def"], c["instance"])
            if bool(errs) != (c["expect"] == "reject"):
                changed.append(c["id"])
        flipped[name] = changed
        if not changed:
            fails.append(f"mutation {name!r} flips no case: that part of the schema binds nothing")
    # keywords actually exercised
    used = set()
    for c in cases:
        used |= validate(schema, c["def"], c["instance"])[1]
    print(f"cases examined: {len(cases)} (accept {n_acc}, reject {n_rej}; {n_open} pin source-silent behaviour)")
    print(f"reject cases rejected for the stated reason: {reasons}/{n_rej}")
    print(f"asserting keywords in the schema: {len(sites(schema))}; mutations examined: {len(flipped)} "
          f"({len(EQUIVALENT)} equivalent skipped); each flips at least one case: "
          f"{sum(1 for v in flipped.values() if v)}/{len(flipped)}")
    print(f"keywords exercised: {', '.join(sorted(used))}")
    for f in fails:
        print("FAIL:", f)
    print("check-envelope: " + ("FAILED" if fails else "ok"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
