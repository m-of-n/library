#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library; RFC 9162 ships no checker.
# Runs every *.derived.schema.json in this directory against
#   - schema-tests.derived.json   (instances each schema MUST accept / MUST REJECT)
#   - ../examples/api-samples.derived.json   (every sample must be accepted)
# and checks that the TransItem-type prefix patterns bind exactly the intended
# VersionedTransType codes. Stdlib only (no jsonschema in the library).
#
#   python3 -I check-schemas.derived.py
#
# The validator below implements only the keywords the schemas here use and
# RAISES on any other keyword, so an unsupported keyword cannot silently
# constrain nothing (hazards.md Section 7).
import base64, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
KNOWN = {"$schema", "$id", "$comment", "title", "description", "$defs", "type",
         "required", "properties", "additionalProperties", "items", "enum",
         "const", "pattern", "minLength", "maxLength", "minimum", "maximum",
         "minItems", "maxItems", "allOf", "anyOf", "oneOf", "not", "$ref",
         "dependentRequired", "minProperties", "examples"}


def is_type(inst, t):
    if t == "object": return isinstance(inst, dict)
    if t == "array": return isinstance(inst, list)
    if t == "string": return isinstance(inst, str)
    if t == "boolean": return isinstance(inst, bool)
    if t == "null": return inst is None
    if t == "integer": return isinstance(inst, int) and not isinstance(inst, bool)
    if t == "number": return isinstance(inst, (int, float)) and not isinstance(inst, bool)
    raise ValueError("unknown type " + t)


def resolve(ref, root):
    assert ref.startswith("#/"), ref
    node = root
    for part in ref[2:].split("/"):
        node = node[part]
    return node


def validate(inst, sch, root, path="$"):
    """Return a list of error strings (empty = valid)."""
    if sch is True: return []
    if sch is False: return [path + ": false schema"]
    bad = set(sch) - KNOWN
    if bad:
        raise ValueError("unsupported keyword(s) %s at %s" % (sorted(bad), path))
    errs = []
    if "$ref" in sch:
        errs += validate(inst, resolve(sch["$ref"], root), root, path)
    if "type" in sch:
        ts = sch["type"] if isinstance(sch["type"], list) else [sch["type"]]
        if not any(is_type(inst, t) for t in ts):
            return errs + ["%s: not of type %s" % (path, ts)]
    if "enum" in sch and inst not in sch["enum"]:
        errs.append("%s: not in enum" % path)
    if "const" in sch and inst != sch["const"]:
        errs.append("%s: not const" % path)
    if isinstance(inst, str):
        if "pattern" in sch and not re.search(sch["pattern"], inst):
            errs.append("%s: pattern %s" % (path, sch["pattern"]))
        if "minLength" in sch and len(inst) < sch["minLength"]:
            errs.append("%s: shorter than %d" % (path, sch["minLength"]))
        if "maxLength" in sch and len(inst) > sch["maxLength"]:
            errs.append("%s: longer than %d" % (path, sch["maxLength"]))
    if isinstance(inst, (int, float)) and not isinstance(inst, bool):
        if "minimum" in sch and inst < sch["minimum"]:
            errs.append("%s: below minimum" % path)
        if "maximum" in sch and inst > sch["maximum"]:
            errs.append("%s: above maximum" % path)
    if isinstance(inst, list):
        if "minItems" in sch and len(inst) < sch["minItems"]:
            errs.append("%s: fewer than %d items" % (path, sch["minItems"]))
        if "maxItems" in sch and len(inst) > sch["maxItems"]:
            errs.append("%s: more than %d items" % (path, sch["maxItems"]))
        if "items" in sch:
            for i, v in enumerate(inst):
                errs += validate(v, sch["items"], root, "%s[%d]" % (path, i))
    if isinstance(inst, dict):
        for r in sch.get("required", []):
            if r not in inst:
                errs.append("%s: missing required %s" % (path, r))
        if "minProperties" in sch and len(inst) < sch["minProperties"]:
            errs.append("%s: fewer than %d properties" % (path, sch["minProperties"]))
        props = sch.get("properties", {})
        for k, v in inst.items():
            if k in props:
                errs += validate(v, props[k], root, path + "." + k)
            elif sch.get("additionalProperties", True) is False:
                errs.append("%s: additional property %s" % (path, k))
            elif isinstance(sch.get("additionalProperties"), dict):
                errs += validate(v, sch["additionalProperties"], root, path + "." + k)
        for k, deps in sch.get("dependentRequired", {}).items():
            if k in inst:
                for dname in deps:
                    if dname not in inst:
                        errs.append("%s: %s requires %s" % (path, k, dname))
    for sub in sch.get("allOf", []):
        errs += validate(inst, sub, root, path)
    if "anyOf" in sch and not any(not validate(inst, s, root, path) for s in sch["anyOf"]):
        errs.append("%s: matches none of anyOf" % path)
    if "oneOf" in sch:
        n = sum(1 for s in sch["oneOf"] if not validate(inst, s, root, path))
        if n != 1:
            errs.append("%s: matches %d of oneOf" % (path, n))
    if "not" in sch and not validate(inst, sch["not"], root, path):
        errs.append("%s: matches a 'not' schema" % path)
    return errs


def load(name):
    with open(os.path.join(HERE, name + ".derived.schema.json"), encoding="utf-8") as fh:
        return json.load(fh)


def main():
    fails = []
    counts = {"files": 0, "accept": 0, "reject": 0, "samples": 0, "prefix": 0}
    files = sorted(f for f in os.listdir(HERE) if f.endswith(".derived.schema.json"))
    schemas = {}
    for f in files:
        name = f[: -len(".derived.schema.json")]
        sch = load(name)
        want = "urn:library:rfc-9162:%s.derived" % name
        if sch.get("$id") != want:
            fails.append("%s: $id %r != %r" % (f, sch.get("$id"), want))
        head = "".join(open(os.path.join(HERE, f), encoding="utf-8").readlines()[:12]).lower()
        if "derived" not in head:
            fails.append(f + ": no derived marker in first 12 lines")
        schemas[name] = sch
        counts["files"] += 1
    with open(os.path.join(HERE, "schema-tests.derived.json"), encoding="utf-8") as fh:
        tests = json.load(fh)["tests"]
    per = {}
    for t in tests:
        sch = schemas[t["schema"]]
        errs = validate(t["instance"], sch, sch)
        ok = not errs
        kind = "accept" if t["valid"] else "reject"
        counts[kind] += 1
        per.setdefault(t["schema"], {"accept": 0, "reject": 0})[kind] += 1
        if ok != t["valid"]:
            fails.append("%s: %r expected %s but got %s %s" % (
                t["schema"], t["why"], kind, "accept" if ok else "reject", errs[:2]))
    for name in schemas:
        if per.get(name, {}).get("reject", 0) < 3:
            fails.append("%s: fewer than 3 MUST-REJECT instances" % name)
        if per.get(name, {}).get("accept", 0) < 1:
            fails.append("%s: no MUST-ACCEPT instance" % name)
    with open(os.path.join(HERE, "..", "examples", "api-samples.derived.json"), encoding="utf-8") as fh:
        samples = json.load(fh)["samples"]
    for s in samples:
        name = s["endpoint"] + ("-request" if s["direction"] == "request" else "-response")
        sch = schemas[name]
        errs = validate(s["instance"], sch, sch)
        counts["samples"] += 1
        if errs:
            fails.append("sample %s: %s" % (name, errs[:2]))
    # the one verbatim JSON fixture (the source's own error body) is accepted by its schema
    with open(os.path.join(HERE, "..", "examples", "ex-10.verbatim.json"), encoding="utf-8") as fh:
        ex10 = json.load(fh)
    errs = validate(ex10, schemas["error-response"], schemas["error-response"])
    counts["samples"] += 1
    if errs:
        fails.append("ex-10.verbatim.json: %s" % errs[:2])
    # the TransItem-type prefix patterns bind exactly the intended codes
    want = {"entry": {0x0100, 0x0101}, "sct": {0x0102, 0x0103}, "sth": {0x0104},
            "consistency": {0x0105}, "inclusion": {0x0106}}
    seen_defs = 0
    for sname, sch in schemas.items():
        for dname, dsch in sch.get("$defs", {}).items():
            if not dname.startswith("transItem_"):
                continue
            kind = dname[len("transItem_"):]
            seen_defs += 1
            rx = [p["pattern"] for p in dsch["allOf"] if "pattern" in p][-1]
            codes = want[kind]
            for code in range(0x10000):
                for third in (0x00, 0x7F, 0xFF):
                    raw = code.to_bytes(2, "big") + bytes([third])
                    hit = re.search(rx, base64.b64encode(raw).decode()) is not None
                    counts["prefix"] += 1
                    if hit != (code in codes):
                        fails.append("prefix %s/%s: code 0x%04x third 0x%02x hit=%s" % (sname, kind, code, third, hit))
                        break
                else:
                    continue
                break
    if seen_defs == 0:
        fails.append("no transItem_ definitions examined")
    print("schema files: %d; per schema (accept, reject): %s" % (
        counts["files"], {k: (v["accept"], v["reject"]) for k, v in sorted(per.items())}))
    print("tests: %d MUST-ACCEPT, %d MUST-REJECT; samples checked: %d; prefix probes: %d over %d definitions" % (
        counts["accept"], counts["reject"], counts["samples"], counts["prefix"], seen_defs))
    for f in fails:
        print("FAIL:", f)
    print("failures: %d" % len(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
