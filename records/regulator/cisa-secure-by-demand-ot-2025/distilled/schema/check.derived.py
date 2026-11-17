#!/usr/bin/env python3
"""DERIVED by the library. Validates the twelve consideration sections parsed
from the pinned source, and our accept/reject cases, against the derived
schemas; cross-checks question counts against requirements.yaml; re-resolves
every constrained_by id in messages.yaml. Reports how many it EXAMINED.

    <venv>/bin/python -I distilled/schema/check.derived.py
"""
import collections, importlib.util, json, pathlib, sys
sys.dont_write_bytecode = True  # a __pycache__ of build.derived.py in distilled/ fails bin/validate (pass 2)
import yaml, jsonschema

HERE = pathlib.Path(__file__).resolve().parent
DIST = HERE.parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "bin"))
spec = importlib.util.spec_from_file_location("b", HERE / "build.derived.py")
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
fails = []


def V(n):
    s = json.loads((HERE / f"{n}.derived.schema.json").read_text())
    jsonschema.Draft202012Validator.check_schema(s)
    return jsonschema.Draft202012Validator(s)


run = lambda v, i: [e.message for e in v.iter_errors(i)]
vs = {n: V(n) for n in b.STRUCT}
secs = b.SECTION_INSTANCES
bad = 0
for s in secs:
    r = run(vs["consideration-section"], s)
    if r: bad += 1; fails.append(f"{s['name']}: {r[0][:90]}")
print(f"real sections: {len(secs)} examined, {bad} rejected")
# pass 2: the parsed goal is the goal sentence its role: goal entry quotes, and the guidance after it is kept
gtext = {r["consideration"]: " ".join(str(r["text"]).split()) for r in b.REQ if r.get("role") == "goal"}
gbad = [s["name"] for s in secs if s["goal"] != gtext.get(s["name"]) or not s.get("buyer_guidance")]
print(f"goal sentence equals its goal entry, and guidance follows: {len(secs)} examined, {len(gbad)} differ {gbad}")
fails += [f"goal {g}" for g in gbad]
tmq = [" ".join(str(r["text"]).split()) for r in sorted((r for r in b.REQ if r.get("question_set") == "threat model questions"),
                                                         key=lambda r: int(str(r["source_lines"]).split("-")[0]))]
got = [s.get("threat_model_questions") for s in secs if s["name"] == "Threat Modeling"][0]
same = sorted(got or []) == sorted(tmq)  # two entries start on L729, so compare as a multiset
print(f"threat model questions parsed from source vs requirements.yaml: {len(got or [])} vs {len(tmq)}, same texts: {same}")
if not same: fails.append("threat model questions")
qc = collections.Counter(r["consideration"] for r in b.REQ if r.get("role") == "question" and r.get("question_set") == "questions to ask")
mism = [(s["name"], len(s["questions"]), qc[s["name"]]) for s in secs if len(s["questions"]) != qc[s["name"]]]
print(f"question count, parsed from source vs requirements.yaml: {len(secs)} examined, {len(mism)} differ {mism}")
fails += [f"question count {m}" for m in mism]
print("sections with label Key considerations:", [s["name"] for s in secs if s["question_label"] != "Questions to ask"])
n = w = 0
for f in sorted((DIST / "examples").glob("*.derived.json")):
    c = json.loads(f.read_text()); n += 1
    got = "reject" if run(vs[c["schema"].replace(".derived.schema.json", "")], c["instance"]) else "accept"
    if got != c["expect"]: w += 1; fails.append(f"case {f.name}: expected {c['expect']} got {got}")
print(f"cases: {n} examined, {w} wrong")
# every cited id exists exactly once, and is read back
ids = collections.Counter(r["id"] for r in b.REQ)
m = yaml.safe_load((DIST / "messages.yaml").read_text())
cited = [i for ms in m["messages"] for f in ms["fields"] for i in f["constrained_by"]]
miss = [i for i in cited if ids[i] != 1]
empty = [(ms["name"], f["name"]) for ms in m["messages"] for f in ms["fields"] if not f["constrained_by"] and not f.get("inferred_reason")]
print(f"constrained_by: {len(cited)} citations, {len(set(cited))} distinct ids, {len(miss)} not exactly-one in requirements.yaml; fields with none and no reason: {len(empty)}")
fails += [f"id {i}" for i in miss] + [f"no ids no reason {e}" for e in empty]
for ms in m["messages"]:
    print("  ", ms["name"], [(f["name"], len(f["constrained_by"])) for f in ms["fields"]])
import _yaml, _record_yaml
t = (DIST / "messages.yaml").read_text()
fl = lambda x, p="": [kv for k, v in (x.items() if isinstance(x, dict) else enumerate(x) if isinstance(x, list) else []) for kv in fl(v, f"{p}.{k}")] if isinstance(x, (dict, list)) and x else [(p, "[]" if isinstance(x, list) else str(x).lower())]
fa, fb = dict(fl(_yaml.parse(t))), dict(fl(_record_yaml.YamlParser(t, "m").parse()))
diff = [k for k in set(fa) | set(fb) if fa.get(k) != fb.get(k)]
print(f"messages.yaml: both readers, {len(fa)} leaves vs {len(fb)}, {len(diff)} differ {diff[:3]}")
if diff: fails.append("readers")
print("FAIL" if fails else "OK", len(fails))
for f in fails[:20]: print("  ", f)
sys.exit(1 if fails else 0)
