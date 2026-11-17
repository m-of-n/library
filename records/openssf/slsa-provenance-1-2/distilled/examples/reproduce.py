#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library, not copied from the SLSA specification.
# Re-extracts every verbatim fixture from the rendering of the source, checks the bytes, and runs the
# schema checks the manifest names. Stdlib only.
#
#   python3 -I reproduce.py            # check: fixtures on disk == re-extracted; every expectation holds
#   python3 -I reproduce.py --write    # rewrite the verbatim fixtures and migration-v1-output, then check
#
# Sources, all under the repository's .cache/ (never committed):
#   slsa-provenance-1-2.bin       slsa-framework/slsa releases/v1.2 @ ae7fc76, spec/build-provenance.md
#   slsa-provenance-1-2.include/  provenance.cue and provenance.proto, spliced in by Jekyll include_relative
#   slsa-provenance-1-2.txt       the rendering of the two, built by ../render-source.py (a pure function)
# Fixture bytes are the rendering's lines joined with a newline plus one final newline. Nothing is retyped.
import hashlib, importlib.util, json, os, re, subprocess, sys, tempfile

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
CACHE = os.path.join(ROOT, ".cache")
TXT = os.path.join(CACHE, "slsa-provenance-1-2.txt")
BIN = os.path.join(CACHE, "slsa-provenance-1-2.bin")
INC = os.path.join(CACHE, "slsa-provenance-1-2.include")
WRITE = "--write" in sys.argv
FAILS, CHECKS = [], [0]


def check(cond, what):
    CHECKS[0] += 1
    if not cond:
        FAILS.append(what)
        print("FAIL:", what)


def load_checker():
    p = os.path.join(DIST, "schema", "check-schemas.derived.py")
    spec = importlib.util.spec_from_file_location("check_schemas_derived", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


CS = load_checker()
SCHEMA = json.load(open(CS.SCHEMA_FILE, encoding="utf-8"))


def verr(inst, d="root"):
    return CS.check_case(SCHEMA, {"def": d, "instance": inst})


def rng(s):
    a, _, b = s.partition("-")
    return int(a), int(b or a)


def cut(lines, s):
    a, b = rng(s)
    return ("\n".join(lines[a - 1:b]) + "\n").encode("utf-8")


def sha(b):
    return hashlib.sha256(b).hexdigest()


# --------------------------------------------------------------------------- the rendering itself
src_bytes = open(TXT, "rb").read()
lines = src_bytes.decode("utf-8").split("\n")      # split("\n"), never splitlines()
bin_lines = open(BIN, "rb").read().decode("utf-8").split("\n")

# 1. the rendering is a pure function of the .bin, the includes and ../render-source.py
with tempfile.TemporaryDirectory() as d:
    out = os.path.join(d, "out.txt")
    r = subprocess.run([sys.executable, "-I", os.path.join(DIST, "render-source.py"), BIN, INC, out],
                       capture_output=True, text=True)
    check(r.returncode == 0, "render-source.py runs: " + (r.stderr or r.stdout)[:200])
    if r.returncode == 0:
        check(open(out, "rb").read() == src_bytes, "render-source.py output is byte-identical to .cache/slsa-provenance-1-2.txt")

# 2. every fence of the rendering is accounted for, and nothing else is a fence
fence_lines = [i for i, l in enumerate(lines, 1) if l.startswith("```")]
man = json.load(open(os.path.join(HERE, "manifest.derived.json"), encoding="utf-8"))
want = []
for f in man["fences_accounted_for"]:
    a, b = rng(f["lines"])
    want += [a, b]
check(sorted(want) == fence_lines, "fence lines in the rendering %s == the fences the manifest accounts for %s" % (fence_lines, sorted(want)))

# 3. cue and proto: .bin directive -> include file -> rendering lines -> schema/*.verbatim.* (all byte-equal)
render_src = open(os.path.join(DIST, "render-source.py"), encoding="utf-8").read()
pinned = dict(re.findall(r'"([\w.\-]+)":\s*"([0-9a-f]{64})"', render_src))
for s in man["schema_verbatim"]:
    inc_bytes = open(os.path.join(INC, s["include"]), "rb").read()
    check(sha(inc_bytes) == pinned[s["include"]], "%s: include sha256 equals the digest render-source.py pins" % s["include"])
    check(bin_lines[s["bin_directive_line"] - 1] == "{% include_relative schema/" + s["include"] + " %}",
          "%s: the .bin has the include directive at line %d" % (s["include"], s["bin_directive_line"]))
    check(cut(lines, s["rendering_lines"]) == inc_bytes, "%s: rendering lines %s are byte-equal to the include file" % (s["include"], s["rendering_lines"]))
    on_disk = open(os.path.join(HERE, s["file"]), "rb").read()
    check(on_disk == inc_bytes, "%s: byte-equal to the include file (sha256 %s)" % (s["file"], sha(on_disk)[:12]))

# 4. verbatim fixtures
VERB = {}
for fx in man["verbatim"]:
    data = cut(lines, fx["source_lines"])
    path = os.path.join(HERE, fx["file"])
    if WRITE:
        open(path, "wb").write(data)
    check(os.path.exists(path) and open(path, "rb").read() == data, "%s: byte-equal to rendering lines %s" % (fx["file"], fx["source_lines"]))
    if fx["fence"]:
        a, b = rng(fx["source_lines"])
        check(lines[fx["fence"]["open"] - 1] == "```" + fx["fence"]["info"] and lines[fx["fence"]["close"] - 1] == "```"
              and fx["fence"]["open"] + 1 == a and fx["fence"]["close"] - 1 == b,
              "%s: lines are exactly the interior of the %s fence at %d-%d" % (fx["file"], fx["fence"]["info"], fx["fence"]["open"], fx["fence"]["close"]))
    VERB[fx["file"]] = data.decode("utf-8")

# 5. expectations
for fx in man["verbatim"]:
    text, k = VERB[fx["file"]], fx["check"]
    if k == "member-of-wrapped-object":
        obj = json.loads("{" + text + "}")
        for m in fx["members"]:
            check(m in obj and not verr(obj[m], fx["def"]), "%s: member %s is accepted by %s" % (fx["file"], m, fx["def"]))
    elif k == "members-of-build-definition":
        obj = json.loads("{" + text + "}")
        props = SCHEMA["$defs"]["BuildDefinition"]["properties"]
        for m in fx["members"]:
            check(m in obj and not CS.validate(obj[m], props[m], SCHEMA), "%s: member %s is accepted by BuildDefinition.%s" % (fx["file"], m, m))
        check(bool(verr(obj, "BuildDefinition")), "%s: the fragment alone is rejected as a BuildDefinition (no buildType)" % fx["file"])
        full = {"buildDefinition": dict(obj, buildType="https://example.com/build/v1"),
                "runDetails": {"builder": {"id": "https://example.com/builder/v1"}}}
        check(not verr(full), "%s: with buildType and a builder added it is a valid predicate" % fx["file"])
        check(json.dumps(obj["resolvedDependencies"][0]["digest"]) == '{"gitCommit": "7fd1a60b01f91b314f59955a4e4d4e80d8edf11d"}', "%s: the dependency digest is the gitCommit" % fx["file"])
    elif k == "migration-pseudocode":
        try:
            json.loads(text)
            check(False, "%s: must NOT parse as JSON" % fx["file"])
        except ValueError:
            check(True, "")
        check("old." in text and "//" in text and "/*" in text, "%s: carries old.* references and comments" % fx["file"])
    elif k == "buildtype-uri":
        check(not CS.validate(text.strip(), SCHEMA["$defs"]["TypeURI"], SCHEMA), "%s: accepted as TypeURI" % fx["file"])
        base = json.load(open(os.path.join(HERE, "provenance-minimal.derived.json")))
        base["buildDefinition"]["buildType"] = text.strip()
        check(not verr(base), "%s: accepted as buildType" % fx["file"])
    elif k == "extension-name":
        names = re.findall(r"`([A-Za-z0-9]+_[A-Za-z0-9]+)`", text)
        check(names == ["examplebuilder_isCodeReviewed"], "%s: exactly one code-quoted vendor_fieldname example %s" % (fx["file"], names))
        base = json.load(open(os.path.join(HERE, "provenance-minimal.derived.json")))
        probes = [base["buildDefinition"], base["runDetails"], base["runDetails"]["builder"], base]
        for p in probes:
            p[names[0]] = True
        check(not verr(base), "%s: %s as an extra member at four object levels is accepted" % (fx["file"], names[0]))
        check("<vendor>_<fieldname>" in text, "%s: states the form <vendor>_<fieldname>" % fx["file"])

# 6. derived instances
for d in man["derived"]:
    if d["file"] == "migration-v1-output.derived.json":
        continue                                          # produced and checked in step 7
    path = os.path.join(HERE, d["file"])
    obj = json.load(open(path, encoding="utf-8"))
    if d["check"] == "accept":
        check(not verr(obj, d["def"]), "%s: accepted by %s" % (d["file"], d["def"]))
    if d["file"] == "statement-full.derived.json":
        check(obj["predicate"] == json.load(open(os.path.join(HERE, "provenance-full.derived.json"))), "%s: the predicate is provenance-full" % d["file"])
    lint = CS.lint_provenance(obj if "buildDefinition" in obj else obj.get("predicate"))
    if "buildDefinition" in obj or "predicate" in obj:
        check(not lint, "%s: R-0023 lint clean %s" % (d["file"], lint))

# 7. the migration pseudocode, as the code the fixture describes
MISSING = object()


def g(o, *path):
    for p in path:
        if not isinstance(o, dict) or p not in o:
            return MISSING
        o = o[p]
    return o


def put(**kw):
    return {k: v for k, v in kw.items() if v is not MISSING}


def plus(a, b):
    # the pseudocode's + : object union (right wins; the source says nothing about a collision) or array concatenation
    if a is MISSING:
        a = [] if isinstance(b, list) else {}
    return a + b if isinstance(a, list) else dict(a, **b)


def migrate_v02(old):
    cs = lambda k: g(old, "invocation", "configSource", k)
    return {
        "buildDefinition": put(
            buildType=g(old, "buildType"),                        # the comment: MUST be updated for v1.0 (the caller does it)
            externalParameters=plus(g(old, "invocation", "parameters"), put(entryPoint=cs("entryPoint"), source=cs("uri"))),
            internalParameters=g(old, "invocation", "environment"),
            resolvedDependencies=plus(g(old, "materials"), [put(uri=cs("uri"), digest=cs("digest"))])),
        "runDetails": {
            "builder": put(id=g(old, "builder", "id"), builderDependencies=None, version=None),
            "metadata": put(invocationId=g(old, "metadata", "buildInvocationId"), startedOn=g(old, "metadata", "buildStartedOn"),
                            finishedOn=g(old, "metadata", "buildFinishedOn")),
            "byproducts": None},
    }


def keys_of(o, acc):
    if isinstance(o, dict):
        for k, v in o.items():
            acc.add(k)
            keys_of(v, acc)
    elif isinstance(o, list):
        for v in o:
            keys_of(v, acc)
    return acc


old = json.load(open(os.path.join(HERE, "migration-v02-input.derived.json"), encoding="utf-8"))
new = migrate_v02(old)
new["buildDefinition"]["buildType"] = "https://example.com/build/v1"    # chosen here: the updated buildType
out_path = os.path.join(HERE, "migration-v1-output.derived.json")
if WRITE:
    open(out_path, "w").write(json.dumps(new, indent=2) + "\n")
check(json.load(open(out_path, encoding="utf-8")) == new, "migration-v1-output.derived.json == migrate_v02(migration-v02-input.derived.json)")
check(not verr(new), "the migrated provenance is accepted by the schema: %s" % verr(new)[:2])
fixture_keys = set(re.findall(r'"(\w+)"\s*:', VERB["ex-03.verbatim.txt"]))
DATA_KEYS = {"arch", "sha1", "sha256", "target"}           # keys that come from the v0.2 input's own values, not from the mapping
check(keys_of(new, set()) - DATA_KEYS == fixture_keys, "key set of the migrated object, less the input's data keys %s, == quoted keys of ex-03: %s vs %s"
      % (sorted(DATA_KEYS), sorted(keys_of(new, set()) - DATA_KEYS), sorted(fixture_keys)))
ep = new["buildDefinition"]["externalParameters"]
check(ep == {"target": "all", "entryPoint": "build.yaml", "source": old["invocation"]["configSource"]["uri"]}, "externalParameters = parameters + entryPoint + source")
check(new["buildDefinition"]["resolvedDependencies"] == old["materials"] + [{"uri": old["invocation"]["configSource"]["uri"], "digest": old["invocation"]["configSource"]["digest"]}],
      "resolvedDependencies = materials + the configSource descriptor")
check(new["buildDefinition"]["internalParameters"] == old["invocation"]["environment"], "internalParameters = invocation.environment")
check(all(new["runDetails"][k] is None for k in ("byproducts",)) and new["runDetails"]["builder"]["version"] is None
      and new["runDetails"]["builder"]["builderDependencies"] is None, "byproducts, builder.version and builder.builderDependencies are null")
check(not any(k in keys_of(new, set()) for k in ("completeness", "reproducible", "buildConfig")), "completeness, reproducible and buildConfig are dropped")
# the pseudocode on a sparser v0.2 object (a missing field is omitted, as JavaScript undefined is) still migrates to a valid predicate
sparse = {"buildType": "https://example.com/old-build/v0.2", "builder": {"id": "https://example.com/builder/v0.2"}, "invocation": {"parameters": {"a": "b"}}}
sp = migrate_v02(sparse)
sp["buildDefinition"]["buildType"] = "https://example.com/build/v1"
check(not verr(sp), "a v0.2 object with no configSource, environment, materials or metadata migrates to a predicate the schema accepts, an empty descriptor appended (SD-12): %s" % verr(sp)[:2])
# and one with no parameters at all cannot: externalParameters would be empty
bare = migrate_v02({"buildType": "x", "builder": {"id": "https://b"}})
bare["buildDefinition"]["buildType"] = "https://example.com/build/v1"
check(bool(verr(bare)), "a v0.2 object with no parameters and no configSource migrates to an EMPTY externalParameters, which the schema rejects (source defect SD-7)")

print("checks run: %d, failed: %d" % (CHECKS[0], len(FAILS)))
sys.exit(1 if FAILS else 0)
