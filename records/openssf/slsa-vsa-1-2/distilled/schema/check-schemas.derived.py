#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library; SLSA VSA v1.2 ships no checker.
# Runs the derived JSON Schemas in this directory against
#   - schema-tests.derived.json            instances each schema MUST accept / MUST REJECT
#   - ../examples/example-vsa.derived.json the section 4 example (must be accepted)
#   - ../examples/consumer-verification.derived.json  every VSA in it (schema verdict as recorded)
# plus one SEMANTIC rule JSON Schema cannot state (SEM-01, one level per track),
# and a KEYWORD-MUTATION test: every keyword (and every element of required, enum
# and anyOf) is removed in turn and the whole test set re-run; a keyword whose
# removal changes no verdict binds nothing and fails the run.
# Stdlib only (no jsonschema in the library).
#
#   python3 -I check-schemas.derived.py
#
# The validator implements only the keywords the schemas use and RAISES on any
# other, so an unsupported keyword cannot silently constrain nothing
# (hazards.md: a schema that parses is not a schema that binds).
import copy, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EX = os.path.join(HERE, "..", "examples")
PREFIX = "urn:library:slsa-vsa-1-2:"
ANNOTATION = {"$schema", "$id", "$comment", "title", "description"}
KNOWN = ANNOTATION | {"type", "required", "properties", "additionalProperties", "items",
                      "enum", "const", "pattern", "minimum", "minItems", "propertyNames",
                      "if", "then", "$ref"}
FAILS = []
CHECKS = [0]


def check(cond, what):
    CHECKS[0] += 1
    if not cond:
        FAILS.append(what)


def is_type(inst, t):
    if t == "object": return isinstance(inst, dict)
    if t == "array": return isinstance(inst, list)
    if t == "string": return isinstance(inst, str)
    if t == "boolean": return isinstance(inst, bool)
    if t == "null": return inst is None
    # 2020-12: an integer is any number with a zero fractional part, so 5.0 is one
    # (pass 1 required a Python int, which rejected what the schema accepts).
    if t == "integer": return (isinstance(inst, int) and not isinstance(inst, bool)) or (isinstance(inst, float) and inst.is_integer())
    if t == "number": return isinstance(inst, (int, float)) and not isinstance(inst, bool)
    raise ValueError("unknown type " + t)


def ecma(p):
    """JSON Schema patterns are ECMA 262: $ is end of input only (Python's $ also
    matches before a trailing newline), and the classes used here are ASCII."""
    return re.sub(r"(?<!\\)\$", r"\\Z", p)


def validate(inst, sch, reg, path="$"):
    """Errors for inst against sch (empty = valid). reg maps $id -> schema."""
    bad = set(sch) - KNOWN
    if bad:
        raise ValueError("unsupported keyword(s) %s at %s" % (sorted(bad), path))
    errs = []
    if "$ref" in sch:
        if sch["$ref"] not in reg:
            raise ValueError("unresolved $ref " + sch["$ref"])
        errs += validate(inst, reg[sch["$ref"]], reg, path)
    if "type" in sch:
        ts = sch["type"] if isinstance(sch["type"], list) else [sch["type"]]
        if not any(is_type(inst, t) for t in ts):
            return errs + ["%s: not of type %s" % (path, ts)]
    if "enum" in sch and inst not in sch["enum"]:
        errs.append("%s: not in enum" % path)
    if "const" in sch and inst != sch["const"]:
        errs.append("%s: not const" % path)
    if "if" in sch and "then" in sch and not validate(inst, sch["if"], reg, path):
        errs += validate(inst, sch["then"], reg, path)
    if isinstance(inst, str) and "pattern" in sch and not re.search(ecma(sch["pattern"]), inst):
        errs.append("%s: pattern %s" % (path, sch["pattern"]))
    if is_type(inst, "number") and "minimum" in sch and inst < sch["minimum"]:
        errs.append("%s: below minimum" % path)
    if isinstance(inst, list):
        if "minItems" in sch and len(inst) < sch["minItems"]:
            errs.append("%s: fewer than %d items" % (path, sch["minItems"]))
        if "items" in sch:
            for i, v in enumerate(inst):
                errs += validate(v, sch["items"], reg, "%s[%d]" % (path, i))
    if isinstance(inst, dict):
        for r in sch.get("required", []):
            if r not in inst:
                errs.append("%s: missing required %s" % (path, r))
        props = sch.get("properties", {})
        for k, v in inst.items():
            if "propertyNames" in sch:
                errs += validate(k, sch["propertyNames"], reg, "%s{name %s}" % (path, k))
            if k in props:
                errs += validate(v, props[k], reg, path + "." + k)
            elif isinstance(sch.get("additionalProperties"), dict):
                errs += validate(v, sch["additionalProperties"], reg, path + "." + k)
    return errs


# ---- semantic rules JSON Schema cannot state --------------------------------
TRACKED = re.compile(r"^SLSA_([A-Z][A-Z0-9_]*)_LEVEL_(?:UNEVALUATED|[0-9]+)\Z")


def track_of(level):
    m = TRACKED.match(level) if isinstance(level, str) else None
    return m.group(1) if m else None


def semantic(inst, kind, rules):
    """kind: predicate | statement | slsa-result. Returns violated rule ids."""
    pred = inst.get("predicate") if kind == "statement" and isinstance(inst, dict) else inst
    out = []
    if kind in ("predicate", "statement") and isinstance(pred, dict):
        lv = pred.get("verifiedLevels")
        if "SEM-01" in rules and isinstance(lv, list):
            seen = [track_of(x) for x in lv]
            seen = [t for t in seen if t]
            if len(seen) != len(set(seen)):
                out.append("SEM-01")  # L199: MUST NOT include more than one level per SLSA track
    return out


ALL_RULES = {"SEM-01"}


def load_registry():
    reg, names = {}, {}
    for f in sorted(os.listdir(HERE)):
        if not f.endswith(".derived.schema.json"):
            continue
        with open(os.path.join(HERE, f), encoding="utf-8") as fh:
            sch = json.load(fh)
        name = f[: -len(".derived.schema.json")]
        check(sch.get("$id") == PREFIX + name + ".derived", "%s: $id %r" % (f, sch.get("$id")))
        head = "".join(open(os.path.join(HERE, f), encoding="utf-8").readlines()[:12]).lower()
        check("derived" in head, f + ": no derived marker in first 12 lines")
        reg[sch["$id"]] = sch
        names[name] = names[re.sub(r"^vsa-", "", name)] = sch["$id"]
    return reg, names


def verdict(inst, kind, reg, names, rules=ALL_RULES):
    errs = validate(inst, reg[names[kind]], reg)
    sem = semantic(inst, kind, rules)
    return (not errs and not sem), errs, sem


# ---- mutation ---------------------------------------------------------------
def mutants(sch, path=()):
    """Yield (description, mutated-copy-builder) pairs: every non-annotation keyword
    removed, and every element of required / enum removed."""
    if not isinstance(sch, dict):
        return
    for k, v in sch.items():
        if k in ANNOTATION:
            continue
        yield (path + (k,), None)
        if k in ("required", "enum") and isinstance(v, list):
            for i in range(len(v)):
                yield (path + (k, i), "elem")
        if k in ("properties",):
            for pk, pv in v.items():
                yield from mutants(pv, path + (k, pk))
        elif k in ("items", "additionalProperties", "propertyNames", "if", "then"):
            if isinstance(v, dict):
                yield from mutants(v, path + (k,))


def apply(sch, p, mode):
    s = copy.deepcopy(sch)
    node = s
    for part in p[:-1]:
        node = node[part]
    if mode == "elem":
        del node[p[-1]]
    else:
        del node[p[-1]]
    return s


def mutation_test(reg, names, tests, counts):
    base = [verdict(t["instance"], t["schema"], reg, names)[0] for t in tests]
    total = survived = 0
    for sid, sch in sorted(reg.items()):
        for p, mode in mutants(sch):
            if mode == "elem":
                # remove one element; the parent list is p[:-1]
                node = sch
                for part in p[:-1]:
                    node = node[part]
                mut = copy.deepcopy(sch)
                m = mut
                for part in p[:-2]:
                    m = m[part]
                del m[p[-2]][p[-1]]
            else:
                mut = apply(sch, p, mode)
            reg2 = dict(reg)
            reg2[sid] = mut
            flipped = False
            for t, b in zip(tests, base):
                try:
                    v = verdict(t["instance"], t["schema"], reg2, names)[0]
                except Exception:
                    v = None
                if v != b:
                    flipped = True
                    break
            total += 1
            if not flipped:
                survived += 1
                check(False, "keyword binds nothing: %s %s" % (sid.rsplit(":", 1)[1], "/".join(str(x) for x in p)))
    # semantic rules
    for r in sorted(ALL_RULES):
        total += 1
        flipped = any(verdict(t["instance"], t["schema"], reg, names, ALL_RULES - {r})[0] !=
                      verdict(t["instance"], t["schema"], reg, names)[0] for t in tests)
        if not flipped:
            survived += 1
            check(False, "semantic rule binds nothing: " + r)
    counts["mutants"] = total
    counts["survived"] = survived


def main():
    reg, names = load_registry()
    counts = {"schemas": len(reg), "accept": 0, "reject": 0, "silent": 0, "mutants": 0, "survived": 0}
    with open(os.path.join(HERE, "schema-tests.derived.json"), encoding="utf-8") as fh:
        tests = json.load(fh)["tests"]
    ids = [t["id"] for t in tests]
    check(len(ids) == len(set(ids)), "duplicate test ids")
    for t in tests:
        ok, errs, sem = verdict(t["instance"], t["schema"], reg, names)
        want = t["valid"]
        if want:
            counts["accept"] += 1
            if t["why"].startswith("SILENT"):
                counts["silent"] += 1
        else:
            counts["reject"] += 1
        check(ok == want, "%s [%s] %s: expected valid=%s, got %s %s" % (t["id"], t["schema"], t["why"], want, errs[:2], sem))
        if not want:
            # the rejection must come from the channel the case names
            check((t["via"] == "semantic") == bool(sem) or (t["via"] == "schema" and bool(errs)),
                  "%s: rejected via the wrong channel (%s): schema %s semantic %s" % (t["id"], t["via"], errs[:1], sem))
            if t["via"] == "schema":
                check(bool(errs), "%s: reject case rejected by nothing in the schema" % t["id"])
    # fixtures from the examples directory
    for fn, kind, want in [("example-vsa.derived.json", "statement", True)]:
        p = os.path.join(EX, fn)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as fh:
                inst = json.load(fh)
            ok, errs, sem = verdict(inst, kind, reg, names)
            check(ok == want, "%s: expected %s, got %s %s" % (fn, want, errs[:2], sem))
            counts["accept"] += 1
        else:
            check(False, "missing " + p)
    p = os.path.join(EX, "consumer-verification.derived.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as fh:
            cases = json.load(fh)["cases"]
        for c in cases:
            ok = verdict(c["vsa"], "statement", reg, names)[0]
            check(ok == c["schema_valid"], "consumer case %s: schema verdict %s != recorded %s" % (c["id"], ok, c["schema_valid"]))
            counts["accept" if ok else "reject"] += 1
    else:
        check(False, "missing " + p)
    mutation_test(reg, names, tests, counts)
    # the jsonc schema block's own field names are all properties of the derived schema
    names_in_block = set()
    vp = os.path.join(HERE, "vsa-schema.verbatim.jsonc")
    if os.path.exists(vp):
        with open(vp, encoding="utf-8") as fh:
            in_pred = False
            for line in fh:
                m = re.match(r'^(\s*)"(\w+)":', line)
                if m and in_pred:
                    names_in_block.add((len(m.group(1)), m.group(2)))
                if line.startswith('"predicate": {'):
                    in_pred = True  # the members of `predicate` only, not subject's name and digest
        pred = reg[PREFIX + "vsa-predicate.derived"]
        tops = {n for i, n in names_in_block if i == 2}
        check(tops == set(pred["properties"]), "jsonc predicate members %s != schema properties %s" % (sorted(tops), sorted(pred["properties"])))
        # nested members against the schema, not a typed list (pass 1 compared indent 4
        # with a literal set and never read the inputAttestations entry, at indent 6)
        props = pred["properties"]
        nested = {n for i, n in names_in_block if i == 4}
        want4 = set(props["verifier"]["properties"]) | set(props["policy"]["properties"])
        check(nested == want4, "jsonc verifier/policy members %s != schema %s" % (sorted(nested), sorted(want4)))
        entry = {n for i, n in names_in_block if i == 6}
        want6 = set(props["inputAttestations"]["items"]["properties"])
        check(entry == want6, "jsonc inputAttestations entry members %s != schema %s" % (sorted(entry), sorted(want6)))
        counts["jsonc_members"] = len(tops) + len(nested) + len(entry)
    else:
        check(False, "missing " + vp)
    print("schemas %(schemas)d  accept %(accept)d (silent %(silent)d)  reject %(reject)d  "
          "mutants %(mutants)d (surviving %(survived)d)  jsonc members %(jsonc_members)d" % counts)
    print("checks run: %d, failed: %d" % (CHECKS[0], len(FAILS)))
    for f in FAILS:
        print("FAIL:", f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
