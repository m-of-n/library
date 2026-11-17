#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library; the source ships no checker.
#
#   python3 -I check-schemas.derived.py            # every check below; exit 0 only if all hold
#   python3 -I check-schemas.derived.py --verbose  # also list every case and mutant
#
# What it does, each part printing how many things it EXAMINED beside what it found:
#   1. the derived schema   provenance-v1.derived.schema.json against schema-tests.derived.json:
#                           every ACCEPT instance must be accepted, every REJECT instance rejected.
#   2. keyword mutation     a schema that parses is not a schema that binds (hazards.md 7). Every
#                           constraint keyword, required member, property, type member and anyOf
#                           branch is deleted in turn, and every object is closed in turn
#                           (additionalProperties: false); a mutant that no case notices is a
#                           keyword that binds nothing, and is reported and fails the run.
#   3. cue and proto        provenance.verbatim.cue and provenance.verbatim.proto are parsed with the
#                           small readers below (no cue or protoc is installed) and their field sets,
#                           types and proto numbers are compared with the derived schema.
#   4. lints                the SHOULD-level rule R-0023 the schema cannot state.
# Stdlib only. The validator implements only the keywords the schema uses and RAISES on any other, so
# a keyword it does not implement cannot silently constrain nothing.
import copy, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_FILE = os.path.join(HERE, "provenance-v1.derived.schema.json")
TESTS_FILE = os.path.join(HERE, "schema-tests.derived.json")
CUE_FILE = os.path.join(HERE, "provenance.verbatim.cue")
PROTO_FILE = os.path.join(HERE, "provenance.verbatim.proto")

ANNOTATION = {"$schema", "$id", "$comment", "title", "description", "$defs"}
CONSTRAINT = {"type", "required", "properties", "additionalProperties", "items", "const", "enum",
              "pattern", "minLength", "minItems", "minProperties", "anyOf", "$ref"}


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
    if not ref.startswith("#/"):
        raise ValueError("only local refs are implemented: " + ref)
    node = root
    for part in ref[2:].split("/"):
        node = node[part]
    return node


def ecma_pattern(p):
    # JSON Schema patterns are ECMA 262: a trailing $ does not match before a final newline.
    return p[:-1] + r"\Z" if p.endswith("$") and not p.endswith("\\$") else p


def validate(inst, sch, root, path="$"):
    """Return a list of error strings (empty = valid)."""
    if sch is True: return []
    if sch is False: return [path + ": false schema"]
    bad = set(sch) - ANNOTATION - CONSTRAINT
    if bad:
        raise ValueError("unsupported keyword(s) %s at %s" % (sorted(bad), path))
    errs = []
    if "$ref" in sch:
        errs += validate(inst, resolve(sch["$ref"], root), root, path)
    if "type" in sch:
        ts = sch["type"] if isinstance(sch["type"], list) else [sch["type"]]
        if not any(is_type(inst, t) for t in ts):
            errs.append("%s: not of type %s" % (path, ts))
    if "const" in sch and not (type(inst) is type(sch["const"]) and inst == sch["const"]):
        errs.append("%s: not const" % path)
    if "enum" in sch and inst not in sch["enum"]:
        errs.append("%s: not in enum" % path)
    if "anyOf" in sch and not any(not validate(inst, s, root, path) for s in sch["anyOf"]):
        errs.append("%s: matches no anyOf branch" % path)
    if isinstance(inst, str):
        if "pattern" in sch and not re.search(ecma_pattern(sch["pattern"]), inst):
            errs.append("%s: pattern %s" % (path, sch["pattern"]))
        if "minLength" in sch and len(inst) < sch["minLength"]:
            errs.append("%s: shorter than %d" % (path, sch["minLength"]))
    if isinstance(inst, list):
        if "minItems" in sch and len(inst) < sch["minItems"]:
            errs.append("%s: fewer than %d items" % (path, sch["minItems"]))
        if "items" in sch:
            for i, v in enumerate(inst):
                errs += validate(v, sch["items"], root, "%s[%d]" % (path, i))
    if isinstance(inst, dict):
        if "minProperties" in sch and len(inst) < sch["minProperties"]:
            errs.append("%s: fewer than %d properties" % (path, sch["minProperties"]))
        for r in sch.get("required", []):
            if r not in inst:
                errs.append("%s: missing required %s" % (path, r))
        props = sch.get("properties", {})
        for k, v in inst.items():
            if k in props:
                errs += validate(v, props[k], root, "%s.%s" % (path, k))
            elif "additionalProperties" in sch:
                errs += validate(v, sch["additionalProperties"], root, "%s.%s" % (path, k))
    return errs


def check_case(schema, case):
    target = schema if case["def"] == "root" else {"$ref": "#/$defs/" + case["def"]}
    return validate(case["instance"], target, schema)


# ------------------------------------------------------------------ mutation
def nodes(sch, path=()):
    """Every schema node with its path, descending through the keywords that hold subschemas."""
    if not isinstance(sch, dict):
        return
    yield path, sch
    for k in ("properties",):
        for name, sub in sch.get(k, {}).items():
            yield from nodes(sub, path + (k, name))
    if isinstance(sch.get("items"), dict):
        yield from nodes(sch["items"], path + ("items",))
    if isinstance(sch.get("additionalProperties"), dict):
        yield from nodes(sch["additionalProperties"], path + ("additionalProperties",))
    for i, sub in enumerate(sch.get("anyOf", [])):
        yield from nodes(sub, path + ("anyOf", i))


def all_nodes(root):
    yield from nodes(root, ())
    for name, d in root.get("$defs", {}).items():
        yield from nodes(d, ("$defs", name))


def get(root, path):
    n = root
    for p in path:
        n = n[p]
    return n


def mutants(root):
    """(label, mutated schema) for every way to remove or tighten one thing."""
    out = []
    for path, node in all_nodes(root):
        where = "/".join(map(str, path)) or "(root)"
        for k in sorted(set(node) & CONSTRAINT):
            m = copy.deepcopy(root); del get(m, path)[k]
            out.append(("delete %s at %s" % (k, where), m))
            if k == "type" and isinstance(node[k], list) and len(node[k]) > 1:
                for t in node[k]:
                    m = copy.deepcopy(root); get(m, path)[k] = [x for x in node[k] if x != t]
                    out.append(("drop type member %s at %s" % (t, where), m))
            if k == "required":
                for r in node[k]:
                    m = copy.deepcopy(root); get(m, path)[k] = [x for x in node[k] if x != r]
                    out.append(("drop required member %s at %s" % (r, where), m))
            if k == "properties":
                for pname in node[k]:
                    m = copy.deepcopy(root); get(m, path)[k][pname] = {}
                    out.append(("empty property %s at %s" % (pname, where), m))
            if k == "anyOf" and len(node[k]) > 1:
                for i in range(len(node[k])):
                    m = copy.deepcopy(root); del get(m, path)[k][i]
                    out.append(("drop anyOf branch %d at %s" % (i, where), m))
        if "properties" in node and "additionalProperties" not in node:
            m = copy.deepcopy(root); get(m, path)["additionalProperties"] = False
            out.append(("close object (additionalProperties false) at %s" % where, m))
    return out


def run_mutation(schema, cases, verbose):
    survivors, n = [], 0
    for label, m in mutants(schema):
        n += 1
        killed = False
        for c in cases:
            try:
                ok = not check_case(m, c)
            except Exception:  # a mutant the validator cannot evaluate is noticed
                killed = True
                break
            if ok != (c["expect"] == "accept"):
                killed = True
                break
        if verbose:
            print("   %s  %s" % ("killed  " if killed else "SURVIVOR", label))
        if not killed:
            survivors.append(label)
    return n, survivors


# ------------------------------------------------------------------ shapes
def schema_shape(prop, defs):
    """Reduce a property schema to a token comparable with the cue and proto readings."""
    ts = prop.get("type")
    ts = ts if isinstance(ts, list) else ([ts] if ts else [])
    if "$ref" in prop:
        name = prop["$ref"].split("/")[-1]
        return "timestamp" if name in ("Timestamp", "OptionalTimestamp") else ("string" if name == "TypeURI" else "ref:" + name)
    if "anyOf" in prop:
        refs = [s for s in prop["anyOf"] if "$ref" in s]
        return schema_shape(refs[0], defs)
    if "string" in ts:
        return "bytes" if "pattern" in prop else "string"
    if "array" in ts:
        return "array:" + prop["items"]["$ref"].split("/")[-1]
    if "object" in ts:
        ap = prop.get("additionalProperties")
        return "map:string" if isinstance(ap, dict) and ap.get("type") == "string" else "object"
    raise ValueError("no shape for %s" % prop)


def schema_defs_shapes(schema):
    d = schema["$defs"]
    return {n: {k: schema_shape(v, d) for k, v in d[n]["properties"].items()}
            for n in ("Provenance", "BuildDefinition", "RunDetails", "Builder", "BuildMetadata", "ResourceDescriptor")}


# ------------------------------------------------------------------ proto reader
SCALARS = {"string": "string", "bytes": "bytes"}
WKT = {"google.protobuf.Struct": "object", "google.protobuf.Timestamp": "timestamp"}


def camel(s):
    h, *t = s.split("_")
    return h + "".join(x.capitalize() for x in t)


def read_proto(text):
    """{message: {jsonName: (shape, number)}} for the proto3 subset in the file; raises on anything else."""
    text = re.sub(r"//[^\n]*", "", text)
    msgs = {}
    for m in re.finditer(r"message\s+(\w+)\s*\{([^}]*)\}", text):
        fields = {}
        for stmt in [s.strip() for s in m.group(2).split(";") if s.strip()]:
            f = re.fullmatch(r"(repeated\s+)?(map\s*<\s*(\w+)\s*,\s*([\w.]+)\s*>|[\w.]+)\s+(\w+)\s*=\s*(\d+)", stmt)
            if not f:
                raise ValueError("unreadable proto field: " + stmt)
            rep, typ, kt, vt, name, num = f.groups()
            if kt:
                shape = "map:string" if (kt, vt) == ("string", "string") else "object"
            elif rep:
                shape = "array:" + typ
            else:
                shape = SCALARS.get(typ) or WKT.get(typ) or "ref:" + typ
            fields[camel(name)] = (shape, int(num))
        msgs[m.group(1)] = fields
    return msgs


# ------------------------------------------------------------------ cue reader
def cue_tokens(text):
    toks, i, n = [], 0, len(text)
    while i < n:
        c = text[i]
        if c.isspace():
            i += 1
        elif text.startswith("//", i):
            while i < n and text[i] != "\n":
                i += 1
        elif c == '"':
            j = i + 1
            while text[j] != '"':
                j += 2 if text[j] == "\\" else 1
            toks.append(("str", text[i + 1:j])); i = j + 1
        elif text.startswith("...", i):
            toks.append(("sym", "...")); i += 3
        elif c in "{}[]:,":
            toks.append(("sym", c)); i += 1
        else:
            m = re.match(r"[#\w]+", text[i:])
            if not m:
                raise ValueError("unreadable cue at %r" % text[i:i + 20])
            toks.append(("id", m.group(0))); i += len(m.group(0))
    return toks


def read_cue(text):
    toks = cue_tokens(text)
    pos = [0]

    def peek(): return toks[pos[0]] if pos[0] < len(toks) else (None, None)
    def take(): pos[0] += 1; return toks[pos[0] - 1]
    def expect(v):
        t = take()
        if t[1] != v:
            raise ValueError("cue: expected %s got %s" % (v, t))

    def value():
        k, v = peek()
        if v == "{":
            take(); obj = {"keys": {}, "patterns": [], "spread": None}
            while peek()[1] != "}":
                if peek()[1] == "...":
                    take(); obj["spread"] = take()[1]
                else:
                    if peek()[1] == "[":
                        take(); kt = take()[1]; expect("]"); expect(":")
                        obj["patterns"].append((kt, value()))
                    else:
                        key = take()[1]; expect(":"); obj["keys"][key] = value()
                if peek()[1] == ",":
                    take()
            take()
            return obj
        if v == "[":
            take(); item = None
            if peek()[1] == "...":
                take()
                if peek()[1] != "]":
                    item = take()[1]
            expect("]")
            return {"list": item}
        return take()[1]

    top = {}
    while pos[0] < len(toks):
        if peek()[1] == "{":
            top["_"] = value()
        else:
            name = take()[1]; expect(":"); top[name] = value()
    return top


def cue_shape(v, names):
    if isinstance(v, dict) and "list" in v:
        return "array:" + (v["list"] or "").lstrip("#")
    if isinstance(v, dict):
        if v["spread"] == "string" or any(k == "string" and val == "string" for k, val in v["patterns"]):
            return "map:string"
        if v["patterns"] and not v["keys"] or (v["patterns"] and v["patterns"][0][1] == "_"):
            return "object"
        return "ref:" + names
    return {"string": "string", "object": "object", "bytes": "bytes", "#Timestamp": "timestamp"}[v]


CUE_NAME = {"buildDefinition": "BuildDefinition", "runDetails": "RunDetails", "builder": "Builder", "metadata": "BuildMetadata"}


def cue_defs(cue):
    pred = cue["_"]["keys"]["predicate"]
    out = {"Provenance": {}}

    def walk(defname, obj):
        shapes = out.setdefault(defname, {})
        for k, v in obj["keys"].items():
            if isinstance(v, dict) and "keys" in v and k in CUE_NAME:
                shapes[k] = "ref:" + CUE_NAME[k]
                walk(CUE_NAME[k], v)
            else:
                shapes[k] = cue_shape(v, CUE_NAME.get(k, k))
    walk("Provenance", pred)
    rd = cue["#ResourceDescriptor"]
    out["ResourceDescriptor"] = {k: cue_shape(v, k) for k, v in rd["keys"].items()}
    return out


# ------------------------------------------------------------------ lints
def lint_provenance(inst):
    """R-0023: the same field name SHOULD NOT be used for both externalParameters and internalParameters."""
    bd = (inst or {}).get("buildDefinition") or {}
    e, i = bd.get("externalParameters") or {}, bd.get("internalParameters") or {}
    return ["name %r in both externalParameters and internalParameters" % k for k in sorted(set(e) & set(i))]


def main():
    verbose = "--verbose" in sys.argv
    schema = json.load(open(SCHEMA_FILE, encoding="utf-8"))
    tests = json.load(open(TESTS_FILE, encoding="utf-8"))
    cases = tests["cases"]
    fails = []

    # 1. cases
    ex = {"accept": 0, "reject": 0}
    for c in cases:
        errs = check_case(schema, c)
        ok = (not errs) if c["expect"] == "accept" else bool(errs)
        ex[c["expect"]] += 1
        if verbose:
            print("   %-7s %s %s: %s" % ("ok" if ok else "FAIL", c["id"], c["def"], c["why"]))
        if not ok:
            fails.append("case %s (%s) expected %s: %s" % (c["id"], c["why"], c["expect"], errs[:2]))
    by_basis = {}
    for c in cases:
        by_basis[c["basis"]] = by_basis.get(c["basis"], 0) + 1
    print("cases: examined %d (%d accept, %d reject); basis %s; mismatched %d"
          % (len(cases), ex["accept"], ex["reject"], by_basis, sum(f.startswith("case") for f in fails)))

    # 2. mutation
    n, surv = run_mutation(schema, cases, verbose)
    print("mutation: examined %d mutants; survivors %d" % (n, len(surv)))
    for s in surv:
        print("   SURVIVOR: " + s)
        fails.append("mutant survived: " + s)

    # 3. cue and proto
    sh = schema_defs_shapes(schema)
    proto = read_proto(open(PROTO_FILE, encoding="utf-8").read())
    cue = cue_defs(read_cue(open(CUE_FILE, encoding="utf-8").read()))
    cmp_n = diffs = 0
    for name, want in sh.items():
        got_p = {k: v[0] for k, v in proto[name].items()}
        for label, got in (("proto", got_p), ("cue", cue[name])):
            cmp_n += 1
            if got != want:
                diffs += 1
                fails.append("%s %s differs from schema: %s vs %s" % (label, name, got, want))
    nums = {m: [v[1] for v in f.values()] for m, f in proto.items()}
    dup = [m for m, v in nums.items() if len(set(v)) != len(v)]
    if dup:
        fails.append("duplicate proto field numbers in %s" % dup)
    ctop = read_cue(open(CUE_FILE, encoding="utf-8").read())["_"]["keys"]
    stmt = schema["$defs"]["Statement"]
    cmp_n += 3
    if set(ctop) != set(stmt["properties"]) or set(ctop) != set(stmt["required"]):
        fails.append("cue top-level fields %s differ from Statement" % sorted(ctop))
    if ctop["_type"] != stmt["properties"]["_type"]["const"] or ctop["predicateType"] != schema["$defs"]["PredicateType"]["const"]:
        fails.append("cue constants differ from the schema consts")
    missing = set(proto) - set(sh)
    if missing:
        fails.append("proto messages not in schema: %s" % sorted(missing))
    print("cue/proto: compared %d structures (%d proto messages, %d fields; cue %d fields); differences %d"
          % (cmp_n, len(proto), sum(len(f) for f in proto.values()), sum(len(f) for f in cue.values()), diffs))

    # 3b. a real protoc, when one is importable (pip install grpcio-tools); otherwise skipped, said so
    try:
        import grpc_tools
        from grpc_tools import protoc
        import tempfile, shutil
        wkt = os.path.join(os.path.dirname(grpc_tools.__file__), "_proto")
        with tempfile.TemporaryDirectory() as d:
            shutil.copy(PROTO_FILE, os.path.join(d, "prov.proto"))
            rc = protoc.main(["protoc", "-I" + d, "-I" + wkt, "--descriptor_set_out=" + os.path.join(d, "p.desc"), os.path.join(d, "prov.proto")])
        print("protoc: grpc_tools.protoc compiled provenance.verbatim.proto, exit %d" % rc)
        if rc != 0:
            fails.append("protoc failed on the verbatim proto")
    except ImportError:
        print("protoc: SKIPPED, grpc_tools is not importable here (the field comparison above still ran)")

    # 4. lints
    l_bad = lint_provenance({"buildDefinition": {"externalParameters": {"a": 1, "b": 2}, "internalParameters": {"b": 3}}})
    l_ok = lint_provenance({"buildDefinition": {"externalParameters": {"a": 1}, "internalParameters": {"b": 3}}})
    l_none = lint_provenance({"buildDefinition": {"externalParameters": {"a": 1}}})
    print("lints: examined 3 instances; R-0023 flags %d, %d, %d (expected 1, 0, 0)" % (len(l_bad), len(l_ok), len(l_none)))
    if (len(l_bad), len(l_ok), len(l_none)) != (1, 0, 0):
        fails.append("lint R-0023 misbehaves")

    for f in fails:
        print("FAIL: " + f)
    print("RESULT: %s" % ("FAIL (%d)" % len(fails) if fails else "ok"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
