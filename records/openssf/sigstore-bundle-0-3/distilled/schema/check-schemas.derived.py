#!/usr/bin/env python3
# DERIVED - not verbatim. Written by this library. Checks bundle.derived.schema.json against
# ../examples/cases.derived.json, then runs a MUTATION pass: every asserting keyword (each
# required name, enum value, oneOf/allOf branch, property schema, $ref, ...) is removed in turn
# and at least one case must flip ("a schema that parses is not a schema that binds").
#
#   python3 -I check-schemas.derived.py [--cross]      --cross: also run python-jsonschema and
#                                                      python-protobuf if importable (scratch venv)
# Stdlib validator implementing exactly the keywords the schema uses; it RAISES on any other
# keyword. Patterns use ECMA-262 anchoring ($ matches only at the very end, not before a trailing
# newline as Python's does).
import copy, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EX = os.path.join(HERE, "..", "examples")
SCHEMA = json.load(open(os.path.join(HERE, "bundle.derived.schema.json")))
CASES = json.load(open(os.path.join(EX, "cases.derived.json")))
ANNOT = {"$schema", "$id", "$comment", "$defs", "title", "description"}
KNOWN = {"type", "required", "properties", "additionalProperties", "items", "minItems", "maxItems", "pattern",
         "enum", "const", "oneOf", "anyOf", "allOf", "not", "$ref"}


def jtype(v):
    if v is None: return "null"
    if isinstance(v, bool): return "boolean"
    if isinstance(v, int): return "integer"
    if isinstance(v, float): return "number"
    if isinstance(v, str): return "string"
    return "array" if isinstance(v, list) else "object"


def ecma(pat, s):
    if pat.endswith("$") and not pat.endswith("\\$"):
        pat = pat[:-1] + r"\Z"
    return re.search(pat, s) is not None


class V:
    def __init__(self, root): self.root = root

    def ref(self, r):
        n = self.root
        for p in r[2:].split("/"):
            n = n[p.replace("~1", "/").replace("~0", "~")]
        return n

    def errs(self, sch, inst, path="$"):
        e = []
        for k in sch:
            if k not in ANNOT and k not in KNOWN and not k.startswith("x-"):
                raise SystemExit(f"validator does not implement keyword {k!r}")
        if "$ref" in sch: e += self.errs(self.ref(sch["$ref"]), inst, path)
        t = jtype(inst)
        if "type" in sch and not (t == sch["type"] or (sch["type"] == "number" and t == "integer")):
            e.append(f"{path}: expected type {sch['type']}, got {t}")
        if "const" in sch and inst != sch["const"]: e.append(f"{path}: const mismatch {inst!r}")
        if "enum" in sch and inst not in sch["enum"]: e.append(f"{path}: {inst!r} not in enum")
        if t == "string" and "pattern" in sch and not ecma(sch["pattern"], inst): e.append(f"{path}: pattern mismatch {inst[:30]!r}")
        if t == "array":
            if "minItems" in sch and len(inst) < sch["minItems"]: e.append(f"{path}: minItems {sch['minItems']}, got {len(inst)}")
            if "maxItems" in sch and len(inst) > sch["maxItems"]: e.append(f"{path}: maxItems {sch['maxItems']}, got {len(inst)}")
            if "items" in sch:
                for i, x in enumerate(inst): e += self.errs(sch["items"], x, f"{path}[{i}]")
        if t == "object":
            for r in sch.get("required", []):
                if r not in inst: e.append(f"{path}: required property '{r}' missing")
            props = sch.get("properties", {})
            for k, v in inst.items():
                if k in props: e += self.errs(props[k], v, f"{path}.{k}")
                elif sch.get("additionalProperties") is False and "properties" in sch:
                    e.append(f"{path}: additional property '{k}'")
        for k, mode in (("allOf", "all"), ("anyOf", "any"), ("oneOf", "one")):
            if k in sch:
                res = [self.errs(b, inst, path) for b in sch[k]]
                ok = sum(1 for r in res if not r)
                if mode == "all": [e.extend(r) for r in res]
                elif mode == "any" and ok == 0: e.append(f"{path}: matches none of anyOf ({len(res)} branches); first: {res[0][0] if res[0] else ''}")
                elif mode == "one" and ok != 1: e.append(f"{path}: must match exactly one of {len(res)} branches, matched {ok}")
        if "not" in sch and not self.errs(sch["not"], inst, path): e.append(f"{path}: matches a 'not' schema")
        return e


def ptr_parts(p): return [x.replace("~1", "/").replace("~0", "~") for x in p.split("/")[1:]]


def walk(doc, p, create=False):
    n = doc
    for k in ptr_parts(p):
        n = n[int(k)] if isinstance(n, list) else n[k]
    return n


def setp(doc, p, v):
    parts = ptr_parts(p)
    if not parts: return v
    par = walk(doc, "/" + "/".join(x.replace("~", "~0").replace("/", "~1") for x in parts[:-1])) if len(parts) > 1 else doc
    k = parts[-1]
    if isinstance(par, list):
        i = int(k)
        if i == len(par): par.append(v)
        else: par[i] = v
    else: par[k] = v
    return doc


def delp(doc, p):
    parts = ptr_parts(p)
    par = walk(doc, "/" + "/".join(parts[:-1])) if len(parts) > 1 else doc
    if isinstance(par, list): del par[int(parts[-1])]
    else: del par[parts[-1]]


def load_fixture(name): return json.load(open(os.path.join(EX, name)))


def instance(case):
    b = case.get("base")
    if b is None: return copy.deepcopy(case["instance"])
    spec = CASES["bases"][b]
    doc = copy.deepcopy(spec["instance"] if "instance" in spec else load_fixture(spec["fixture"]))
    for op in case["ops"]:
        if "set" in op: doc = setp(doc, op["set"], copy.deepcopy(op["value"]))
        elif "remove" in op: delp(doc, op["remove"]) if ptr_parts(op["remove"]) and exists(doc, op["remove"]) else None
        elif "copy" in op: setp(doc, op["to"], copy.deepcopy(walk(doc, op["copy"])))
        elif "move" in op:
            v = walk(doc, op["move"]); delp(doc, op["move"]); setp(doc, op["to"], v)
    if "instance_at" in case: doc = walk(doc, case["instance_at"])
    return doc


def exists(doc, p):
    try: walk(doc, p); return True
    except (KeyError, IndexError, ValueError): return False


def run(schema, cases, verbose=False):
    v = V(schema); out = []
    for c in cases:
        errs = v.errs({"$ref": "#/$defs/" + c["def"]}, instance(c))
        ok = not errs
        good = ok if c["expect"] == "accept" else (not ok and (not c.get("error_contains") or any(c["error_contains"] in x for x in errs)))
        out.append((c, errs, good, ok))
    return out


def mutants(schema):
    """(label, mutated schema) for every asserting keyword occurrence."""
    def sites(node, path):
        if isinstance(node, dict):
            yield path, node
            for k, x in node.items():
                if k in ("properties", "$defs"):
                    for pk, pv in x.items(): yield from sites(pv, path + [k, pk])
                elif k in ("allOf", "anyOf", "oneOf"):
                    for i, b in enumerate(x): yield from sites(b, path + [k, i])
                elif k in ("items", "not"): yield from sites(x, path + [k])
    for path, node in list(sites(schema, [])):
        where = "/".join(map(str, path)) or "<root>"

        def sub(fn):
            m = copy.deepcopy(schema); n = m
            for p in path: n = n[p]
            fn(n); return m
        for k in list(node):
            if k in ("type", "pattern", "const", "minItems", "maxItems", "additionalProperties", "items", "not"):
                yield f"{where}: drop {k}", sub(lambda n, k=k: n.pop(k))
            elif k == "required":
                for r in node[k]: yield f"{where}: drop required {r}", sub(lambda n, r=r: n["required"].remove(r))
            elif k == "enum":
                for r in node[k]: yield f"{where}: drop enum {r}", sub(lambda n, r=r: n["enum"].remove(r))
            elif k == "$ref" and where != "<root>":
                yield f"{where}: drop $ref", sub(lambda n: n.pop("$ref"))
            elif k in ("allOf", "anyOf", "oneOf"):
                for i in range(len(node[k])):
                    yield f"{where}: drop {k}[{i}]", sub(lambda n, k=k, i=i: n[k].pop(i))
            elif k == "properties":
                for pk in node[k]:
                    yield f"{where}: relax property {pk}", sub(lambda n, pk=pk: n["properties"].__setitem__(pk, {}))


def equivalent(label, schema):
    """Named equivalence rules (each argued in README.md, section Mutation). Returns a reason or None."""
    m = re.match(r"^(\$defs/\w+): drop type$", label)
    if not m: return None
    node = schema["$defs"][m.group(1).split("/")[1]]
    allof = node.get("allOf", [])
    vals = node.get("enum", []) + ([node["const"]] if "const" in node else [])
    if node.get("type") == "string" and vals and all(isinstance(v, str) for v in vals):
        return "enum/const values are all strings: the type test is implied"
    # a oneOf needs two or more branches: with one, a non-object matches it and passes
    if node.get("type") == "object" and any(("oneOf" in a and len(a["oneOf"]) >= 2 and all(set(b) == {"required"} for b in a["oneOf"]))
                                            or ("not" in a and set(a["not"]) == {"required"}) for a in allof):
        return ("a non-object satisfies every `required` vacuously: an exactly-one oneOf over required-branches fails "
                "(all branches match) and a `not` over a required-pair fails, so a non-object is already rejected without `type`")
    return None


EQUIV = {}


def main():
    cross = "--cross" in sys.argv
    cases = CASES["cases"]
    res = run(SCHEMA, cases)
    bad = [(c, e) for c, e, g, _ in res if not g]
    na = sum(1 for c in cases if c["expect"] == "accept"); nr = len(cases) - na
    for c, e in bad: print("CASE FAIL", c["id"], c["expect"], c["why"], e[:2])
    print(f"cases: {len(cases)} ({na} accept, {nr} reject); failures {len(bad)}")
    # every def reachable must be exercised by a reject case: crude check by case 'def' count
    surv, total = [], 0
    base = [ok for _, _, _, ok in res]
    for label, m in mutants(SCHEMA):
        total += 1
        r = run(m, cases)
        if [ok for _, _, _, ok in r] == base:   # a kill is a flipped accept/reject verdict
            surv.append(label)
    print(f"mutation: {total} mutants, {total-len(surv)} killed, {len(surv)} survived")
    eq = [(s, equivalent(s, SCHEMA)) for s in surv]
    real = [s for s, r in eq if r is None]
    print(f"  of the survivors, {len(surv)-len(real)} are equivalent mutants by a named rule, {len(real)} are unexplained")
    for s, r in eq:
        if r: print("  EQUIVALENT", s, "|", r)
        else: print("  SURVIVOR", s)
    surv = real
    rc = 1 if bad or surv else 0
    if cross:
        rc |= cross_run(cases, res)
    return rc


def cross_run(cases, res):
    rc = 0
    try:
        import jsonschema
        cls = jsonschema.Draft202012Validator
        cls.check_schema(SCHEMA)
        val = cls(SCHEMA, format_checker=None)
        diff = []
        for c, e, g, ok in res:
            sch = {"$ref": "#/$defs/" + c["def"], "$defs": SCHEMA["$defs"]}
            jok = cls(sch).is_valid(instance(c))
            if jok != ok: diff.append((c["id"], ok, jok, c["why"]))
        print(f"jsonschema {__import__("importlib.metadata").metadata.version("jsonschema")}: {len(cases)-len(diff)} of {len(cases)} agree with the stdlib validator")
        for d in diff: print("  DISAGREE", d)
        if diff: rc = 1
    except ImportError as ex:
        print("cross-run jsonschema: SKIPPED", ex)
    try:
        gen = os.environ.get("PB_GEN")
        if not gen: raise ImportError("set PB_GEN to a dir with the protoc python output (sigstore_bundle_pb2.py ...)")
        sys.path.insert(0, gen)
        from google.protobuf import json_format
        import sigstore_bundle_pb2 as pb
        dis = []
        for c, e, g, ok in res:
            if c["def"] not in ("Bundle", "BundleV03"): continue
            try:
                json_format.Parse(json.dumps(instance(c)), pb.Bundle()); pok = True
            except Exception as ex:
                pok = False
            if pok != ok: dis.append((c["id"], "schema", "accept" if ok else "reject", "protobuf", "accept" if pok else "reject", c["why"][:70]))
        print(f"protobuf json_format: {len(dis)} disagreements with the schema (schema is stricter where listed):")
        for d in dis: print("  ", d)
        n = sum(1 for c, *_ in res if c["def"] in ("Bundle", "BundleV03"))
        print(f"  over {n} Bundle-level cases: schema rejects/protobuf accepts {sum(1 for d in dis if d[2]=='reject')}, "
              f"schema accepts/protobuf rejects {sum(1 for d in dis if d[2]=='accept')}")
    except ImportError as ex:
        print("cross-run protobuf: SKIPPED", ex)
    return rc


if __name__ == "__main__":
    sys.exit(main())
