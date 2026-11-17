#!/usr/bin/env python3
"""DERIVED by the library. Validates the pinned DSOMM source and our cases
against the derived schemas, and reports how many it EXAMINED.

    <venv>/bin/python -I distilled/schema/check.derived.py

Needs PyYAML, jsonschema, .cache/owasp-dsomm.txt and bin/ readers.
Exit 1 on any failure.
"""
import collections, copy, json, pathlib, sys
import yaml
import jsonschema

HERE = pathlib.Path(__file__).resolve().parent
DIST = HERE.parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "bin"))
fails = []


def V(name):
    s = json.loads((HERE / f"{name}.derived.schema.json").read_text())
    jsonschema.Draft202012Validator.check_schema(s)
    return jsonschema.Draft202012Validator(s)


class L(yaml.SafeLoader):
    pass


dups = []


def cm(loader, node, deep=False):
    seen = set()
    for k, _ in node.value:
        kk = loader.construct_object(k)
        if kk in seen:
            dups.append(kk)
        seen.add(kk)
    return yaml.SafeLoader.construct_mapping(loader, node, deep)


L.add_constructor("tag:yaml.org,2002:map", cm)
docs = list(yaml.load_all((REPO / ".cache/owasp-dsomm.txt").read_text(encoding="utf-8"), Loader=L))
env, model = docs
vact, vimp, venv_, vsub, vdim = (V(n) for n in ("activity", "implementation", "envelope", "sub-dimension", "dimension"))


def run(v, inst):
    return [e.message for e in v.iter_errors(inst)]


print(f"source: {len(docs)} documents, duplicate keys: {len(dups)}")
e = run(venv_, env)
print(f"envelope: 1 examined, {len(e)} rejected")
fails += e
acts = [(d, s, a, b) for d, ss in model.items() for s, al in ss.items() for a, b in al.items()]
ne = 0
for d, s, a, b in acts:
    r = run(vact, b)
    if r:
        ne += 1; fails.append(f"{d}/{s}/{a}: {r[0][:100]}")
print(f"activity: {len(acts)} examined, {ne} rejected")
impls = [i for *_, b in acts for i in (b.get("implementation") if isinstance(b.get("implementation"), list) else [])]
ni = sum(1 for i in impls if run(vimp, i))
fails += [f"implementation {i.get('uuid')}" for i in impls if run(vimp, i)]
print(f"implementation (standalone schema): {len(impls)} examined, {ni} rejected")
nd = sum(1 for d, ss in model.items() if run(vdim, ss))
ns = sum(1 for ss in model.values() for sv in ss.values() if run(vsub, sv))
fails += [f"dimension {d}" for d, ss in model.items() if run(vdim, ss)]
print(f"dimension: {len(model)} examined, {nd} rejected; sub-dimension: {sum(len(x) for x in model.values())} examined, {ns} rejected")

# cross-reference checks JSON Schema cannot express
uu = collections.Counter(b["uuid"] for *_, b in acts)
names = collections.Counter(a for _, _, a, _ in acts)
unres = [x for *_, b in acts for x in b.get("dependsOn", []) if x not in uu]
selfd = [1 for *_, b in acts for x in b.get("dependsOn", []) if x == b["uuid"]]
bykey = collections.defaultdict(set)
for i in impls:
    bykey[i["uuid"]].add(json.dumps(i, sort_keys=True))
incons = sum(1 for v in bykey.values() if len(v) > 1)
deps = {b["uuid"]: set(b.get("dependsOn", [])) for *_, b in acts}
state, cyc = {}, 0


def dfs(u):
    global cyc
    state[u] = 1
    for w in deps.get(u, ()):
        if state.get(w) == 1: cyc += 1
        elif w not in state: dfs(w)
    state[u] = 2


sys.setrecursionlimit(5000)
for u in deps:
    if u not in state: dfs(u)
print(f"cross-checks: activity uuid duplicates {sum(1 for c in uu.values() if c > 1)} of {len(uu)}; "
      f"activity-name duplicates {sum(1 for c in names.values() if c > 1)} of {len(names)}; "
      f"dependsOn entries {sum(len(v) for v in deps.values())} unresolved {len(unres)}, self-dependency {len(selfd)}, cycles {cyc}; "
      f"implementation uuids {len(bykey)} with differing content {incons}")
fails += [f"unresolved dependsOn {x}" for x in unres]
if any(c > 1 for c in uu.values()) or incons or cyc or selfd:
    fails.append("cross-check failure")

# our cases
n = bad = 0
for f in sorted((DIST / "examples").glob("*.derived.json")):
    c = json.loads(f.read_text())
    v = V(c["schema"].replace(".derived.schema.json", ""))
    got = "reject" if run(v, c["instance"]) else "accept"
    n += 1
    if got != c["expect"]:
        bad += 1; fails.append(f"case {f.name}: expected {c['expect']}, got {got}")
print(f"cases: {n} examined, {bad} wrong")

# mutation sweep: every real activity, three breakages, all must be rejected
mut_n = mut_bad = 0
for *_, b in acts:
    for name, fn in (("drop uuid", lambda x: x.pop("uuid")),
                     ("level 6", lambda x: x.update(level=6)),
                     ("unknown key", lambda x: x.update(zz=1)),
                     ("dependsOn name", lambda x: x.update(dependsOn=["An activity name"]))):
        x = copy.deepcopy(b); fn(x); mut_n += 1
        if not run(vact, x):
            mut_bad += 1; fails.append(f"mutation {name} accepted for {b['uuid']}")
print(f"mutations of real activities: {mut_n} examined, {mut_bad} wrongly accepted")

# verbatim examples (verify pass, 2026-11-16): re-cut every fenced code block from the decoded source
# scalars, compare byte for byte with examples/ex-NN.verbatim.*, check the block-scalar ones line by line
# against the raw source lines, and run the hook example where bash and jq exist
import re, shutil, subprocess, tempfile
FENCE = re.compile(r"^([ \t]*)```([\w-]*)[ \t]*\n(.*?)^\1```[ \t]*$", re.S | re.M)
src_text = (REPO / ".cache/owasp-dsomm.txt").read_text(encoding="utf-8")
src_lines = src_text.split("\n")
cut = []


def walk(n):
    if isinstance(n, yaml.MappingNode):
        for _, v in n.value:
            walk(v)
    elif isinstance(n, yaml.SequenceNode):
        for v in n.value:
            walk(v)
    elif isinstance(n, yaml.ScalarNode) and "```" in n.value:
        fl = [i for i in range(n.start_mark.line, n.end_mark.line + 1) if "```" in src_lines[i]]
        for j, m in enumerate(FENCE.finditer(n.value)):
            ind = m.group(1)
            rows = m.group(3).split("\n")[:-1]
            cut.append((n, ind, fl[2 * j], fl[2 * j + 1], "\n".join(r[len(ind):] for r in rows) + "\n"))


for d in yaml.compose_all(src_text):
    walk(d)
files = sorted((DIST / "examples").glob("ex-*.verbatim.*"))
nb = 0
for (n, ind, a, b, content), f in zip(cut, files):
    if f.read_text(encoding="utf-8") != content:
        fails.append(f"{f.name} differs from the source block")
    if n.style in ("|", ">"):
        blk = len(src_lines[a]) - len(src_lines[a].lstrip(" ")) - len(ind)
        raw = "\n".join(l[blk + len(ind):] for l in src_lines[a + 1:b]) + "\n"
        nb += 1
        if raw != f.read_text(encoding="utf-8"):
            fails.append(f"{f.name} differs from source lines {a + 2}-{b}")
if len(cut) != len(files):
    fails.append(f"{len(cut)} fenced blocks in the source, {len(files)} fixtures")
hook = DIST / "examples" / "ex-02.verbatim.sh"
ran = 0
if shutil.which("bash") and shutil.which("jq") and hook.exists():
    with tempfile.TemporaryDirectory() as tmp:
        tp = pathlib.Path(tmp)
        for rel, body in (("specs/threat-model.md", "TM"), ("docs/secure-coding-rules.md", "SCR"),
                          ("docs/security-review-checklist.md", "SRC")):
            (tp / rel).parent.mkdir(parents=True, exist_ok=True)
            (tp / rel).write_text(body)
        for prompt, want in (("/speckit.plan x", "TM"), ("/speckit.implement", "SCR"), ("/speckit.review", "SRC"), ("hello", None)):
            r = subprocess.run(["bash", str(hook)], input=json.dumps({"prompt": prompt}), capture_output=True, text=True, cwd=tmp)
            ran += 1
            got = json.loads(r.stdout)["hookSpecificOutput"] if r.stdout.strip() else None
            ok = r.returncode == 0 and (got == {"hookEventName": "UserPromptSubmit", "additionalContext": want} if want else got is None)
            if not ok:
                fails.append(f"hook example: prompt {prompt!r} gave {r.returncode} {r.stdout[:80]!r}")
print(f"verbatim examples: {len(files)} examined against {len(cut)} source blocks, {nb} also line by line; hook cases run: {ran}")

# messages.yaml readable by both repo readers, equal by value
import _yaml, _record_yaml
txt = (DIST / "messages.yaml").read_text()
a = _yaml.parse(txt)
b = _record_yaml.Parser(txt, "messages.yaml").parse() if hasattr(_record_yaml, "Parser") else None
if b is None:
    cls = [getattr(_record_yaml, n) for n in dir(_record_yaml) if n.endswith("Parser") or n == "P"]
    b = cls[0](txt, "messages.yaml").parse() if cls else None


def flat(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items(): yield from flat(v, f"{p}.{k}")
    elif isinstance(x, list):
        if not x: yield (p, "[]")
        for i, v in enumerate(x): yield from flat(v, f"{p}[{i}]")
    else:
        yield (p, str(x).lower())


fa, fb = dict(flat(a)), dict(flat(b)) if b is not None else {}
diff = [k for k in set(fa) | set(fb) if fa.get(k) != fb.get(k)]
print(f"messages.yaml: both readers, {len(fa)} leaves vs {len(fb)}, {len(diff)} differ {diff[:3]}")
if diff or not b:
    fails.append("readers disagree")
print("FAIL" if fails else "OK", len(fails))
for f in fails[:20]:
    print("  ", f)
sys.exit(1 if fails else 0)
