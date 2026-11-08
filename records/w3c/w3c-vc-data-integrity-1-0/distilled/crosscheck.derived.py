#!/usr/bin/env python3
"""crosscheck.derived.py -- DERIVED from the distilled artifacts of w3c-vc-data-integrity-1-0.
FX-1 pass 3 (cross-check). Library-written, not source text.

Joins, by script (each resolved pair was also read by the pass-3 agent):
  (a) every field a requirement's `field` names exists in messages.yaml or the schema;
  (b) every message / returns / error_code / calls / role in protocol.yaml resolves
      to messages.yaml (the join table: protocol <-> messages);
  (c) every state-machine trigger is a step, a defined message/operation, or a named event;
  (h) hygiene: states, flows, defect ids, error codes, transition ids.
Usage:  python3 -I crosscheck.derived.py [--lib DIR]           # report only
        python3 -I crosscheck.derived.py [--lib DIR] --write   # also rewrite crosscheck.yaml
Every count printed is EXAMINED beside FOUND.
"""
import json
import pathlib
import re
import sys
import collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "bin"))
if "--lib" in sys.argv:  # python3 -I ignores PYTHONPATH; --lib DIR adds jsonschema/referencing for (d)
    sys.path.insert(0, sys.argv[sys.argv.index("--lib") + 1])
import _yaml  # noqa: E402

REC = "w3c-vc-data-integrity-1-0"


def load(n):
    return _yaml.parse((HERE / n).read_text())


REQ = load("requirements.yaml")["requirements"]
MSG = load("messages.yaml")
PRO = load("protocol.yaml")
SM = load("state-machine.yaml")
M = {m["id"]: m for m in MSG["messages"]}
FIELDS = {mid: {f["name"] for f in (m.get("fields") or [])} for mid, m in M.items()}
FLOWS = {f["id"]: f for f in PRO["flows"]}
ROLES = {r["name"] for r in PRO["roles"]}
CODES = set(FIELDS["MSG-20"])
rid = {x["id"].split("#")[1]: x for x in REQ}
problems = []
report = {}


def bad(msg):
    problems.append(msg)


# ---------------------------------------------------------------- (a) fields
props = collections.defaultdict(set)


def walk(o, src):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "properties" and isinstance(v, dict):
                for p in v:
                    props[p].add(src)
            walk(v, src)
    elif isinstance(o, list):
        for v in o:
            walk(v, src)


for f in sorted((HERE / "schema").glob("*.schema.json")):
    walk(json.loads(f.read_text()), f.name)
allfields = collections.defaultdict(list)
for mid, fs in FIELDS.items():
    for n in fs:
        allfields[n].append(mid)
wired = set()
owner = collections.defaultdict(set)


def cb(o, top):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "constrained_by":
                for x in v:
                    wired.add(x.split("#")[1])
                    owner[x.split("#")[1]].add(top)
            else:
                cb(v, top)
    elif isinstance(o, list):
        for v in o:
            cb(v, top)


for sec in ("encoding_rules", "source_tensions"):
    for e in MSG[sec]:
        cb(e, e["id"])
for m in MSG["messages"]:
    cb(m, m["id"])
notwired = {x["id"].split("#")[1]: x["reason"] for x in MSG["not_wired"]}
PREFIX = ("proof.", "options.", "combinedVerificationResult.", "securedDataDocument.",
          "securedDocument.", "inputDocument.", "output.")
atoms = collections.defaultdict(list)
for x in REQ:
    f = re.sub(r"\([^)]*\)", "", x["field"])
    for a in re.split(r";|,| -> ", f):
        a = a.strip()
        if a and a != "none":
            atoms[a].append(x["id"].split("#")[1])
direct, indirect = [], []
for a, ids in sorted(atoms.items()):
    cands = [a.lstrip(".")]
    for p in PREFIX:
        if a.startswith(p):
            cands.append(a[len(p):])
    hit = [(c, sorted(allfields[c]), sorted(props.get(c, ()))) for c in cands if c in allfields or c in props]
    if hit:
        direct.append((a, ids, hit))
    else:
        indirect.append((a, ids))
for a, ids, hit in direct:
    if a.startswith("proof.") and not (hit[-1][1] and hit[-1][2]):
        bad(f"(a) {a}: proof member missing from messages or schema: {hit}")
unjoined = []
for a, ids in indirect:
    for i in ids:
        if i not in wired and i not in notwired:
            unjoined.append((a, i))
            bad(f"(a) {a} ({i}) is neither wired to a message nor listed under not_wired")
text_tokens = collections.defaultdict(set)
alltext = " ".join(p.read_text() for p in [HERE / "messages.yaml", HERE / "protocol.yaml", HERE / "state-machine.yaml",
                                           HERE / "schema/rules.derived.yaml"] + list((HERE / "schema").glob("*.json")))
for x in REQ:
    for t in re.findall(r"(?<![\w#@/.])@?[a-z]+[A-Z][A-Za-z]*(?![\w])|@[a-z]+", x["text"]):
        text_tokens[t].add(x["id"].split("#")[1])
tok_absent = {t: sorted(v) for t, v in text_tokens.items() if t not in alltext}
report["a_fields"] = {
    "requirements_examined": len(REQ), "field_atoms_examined": len(atoms),
    "resolved_to_a_member": len(direct), "not_a_member_concept_or_local": len(indirect),
    "ids_behind_non_member_atoms": sum(len(i) for _, i in indirect),
    "ids_neither_wired_nor_listed": len(unjoined),
    "text_tokens_examined": len(text_tokens), "text_tokens_absent_from_artifacts": tok_absent,
}

# ---------------------------------------------------------------- (b) join
J = {  # (flow, seq, key) -> [(message id, [fields that must exist in it]), ...]
    ("F01", "5", "message"): [("MSG-01", [])],
    ("F02", "2", "message"): [("MSG-09", ["instantiation algorithm"]), ("MSG-23", [])],
    ("F02", "2", "returns"): [("MSG-09", [])],
    ("F02", "5", "message"): [("MSG-09", ["createProof"]), ("MSG-11", ["inputDocument", "options"])],
    ("F02", "5", "returns"): [("MSG-02", []), ("MSG-20", [])],
    ("F02", "6", "message"): [("MSG-09", ["verifyProof"]), ("MSG-15", ["securedDocument"])],
    ("F02", "6", "returns"): [("MSG-10", []), ("MSG-20", [])],
    ("F04", "0", "message"): [("MSG-11", ["inputDocument", "cryptosuite", "options"])],
    ("F04", "1", "message"): [("MSG-09", ["createProof"]), ("MSG-11", ["inputDocument", "options"])],
    ("F04", "1", "returns"): [("MSG-02", [])],
    ("F04", "7", "message"): [("MSG-11", ["(output) securedDataDocument"]), ("MSG-01", ["proof"])],
    ("F05", "0", "message"): [("MSG-12", ["securedDocument", "suite", "options.previousProof"]), ("MSG-23", ["previousProof"])],
    ("F05", "9", "message"): [("MSG-12", ["(output) output"]), ("MSG-01", ["proof"])],
    ("F08", "0", "message"): [("MSG-13", ["mediaType", "documentBytes", "cryptosuite", "expectedProofPurpose", "domain", "challenge"])],
    ("F08", "8", "message"): [("MSG-09", ["verifyProof"])],
    ("F08", "8", "returns"): [("MSG-10", ["verified", "verifiedDocument"]), ("MSG-20", [])],
    ("F08", "10", "message"): [("MSG-14", ["verified", "verifiedDocument", "mediaType", "warnings", "errors"])],
    ("F09", "0", "message"): [("MSG-15", ["securedDocument"])],
    ("F09", "13", "message"): [("MSG-16", ["successfulVerificationResults", "status", "verified", "document", "mediaType"])],
    ("F10", "0", "message"): [("MSG-17", ["inputDocument", "knownContext", "recompact"])],
    ("F10", "7", "message"): [("MSG-18", ["validated", "validatedDocument", "warnings", "errors"])],
    ("F11", "3", "message"): [],
    ("F11", "3", "returns"): [("MSG-07", ["vocabulary[]"])],
    ("F12", "2", "message"): [("MSG-02", ["verificationMethod"])],
    ("F12", "2", "returns"): [("MSG-22", [])],
    ("F14", "1", "message"): [("MSG-23", ["challenge", "domain"])],
    ("F14", "3", "message"): [("MSG-01", ["proof"])],
    ("F15", "2", "message"): [("MSG-01", ["proof"]), ("MSG-05", [])],
    ("F16", "2", "message"): [("MSG-01", ["proof"]), ("MSG-04", [])],
    ("F16", "3", "message"): [("MSG-01", ["proof"]), ("MSG-04", [])],
    ("F17", "1", "message"): [],
    ("F17", "3", "message"): [("MSG-01", ["@context", "proof"])],
    ("F19", "2", "message"): [("MSG-19", ["type", "title", "detail"])],
}
GAP = {
    ("F11", "3", "message"): "The HTTP GET request is not a structure of the source; it is described by the curl command at L414 only. Response side: MSG-07.vocabulary[] and ENC-05 (digest of the response body). Open question 12 in design-notes.md.",
    ("F17", "1", "message"): "Inferred step; the source names such a protocol only as an example (section 2.4.1) and defines no request. Open question 12 in design-notes.md.",
}
seen = set()
rows = []
nmsg = 0
for fid, f in FLOWS.items():
    for s in f["steps"]:
        for key in ("message", "returns"):
            if key not in s:
                continue
            nmsg += 1
            k = (fid, str(s["seq"]), key)
            seen.add(k)
            if k not in J:
                bad(f"(b) {k} has no entry in the join table")
                continue
            tg = []
            for mid, fl in J[k]:
                if mid not in M:
                    bad(f"(b) {k} -> {mid} is not a message")
                    continue
                miss = [x for x in fl if x not in FIELDS[mid]]
                if miss:
                    bad(f"(b) {k} -> {mid} lacks fields {miss}")
                tg.append({"message": mid, "name": M[mid]["name"], "fields_checked": fl})
            rows.append({"flow": fid, "step_seq": str(s["seq"]), "key": key, "text": s[key], "kind": s["kind"],
                         "targets": tg, "gap": GAP.get(k, "")})
for k in J:
    if k not in seen:
        bad(f"(b) join entry {k} matches no step")
# errors, calls, roles
codes_used = 0
for fid, f in FLOWS.items():
    for s in f["steps"]:
        if "error_code" in s:
            for c in re.split(r",\s*", s["error_code"]):
                codes_used += 1
                if c not in CODES:
                    bad(f"(b) {fid} step {s['seq']} error_code {c} not in MSG-20")
        for c in s.get("calls") or []:
            if c not in FLOWS:
                bad(f"(b) {fid} step {s['seq']} calls {c}: no such flow")
        for side in ("from", "to"):
            r0 = re.sub(r"\s*\(.*\)$", "", s[side])
            if r0 not in ROLES:
                bad(f"(b) {fid} step {s['seq']} {side} {s[side]} is not a role")
    for r0 in f["run_by"]:
        if r0 not in ROLES:
            bad(f"(b) {fid} run_by {r0} is not a role")
perr = {e["code"] for e in PRO["errors"]}
if perr != CODES:
    bad(f"(b) protocol errors {sorted(perr)} != MSG-20 {sorted(CODES)}")
for e in PRO["errors"]:
    for fl in e["flows"]:
        if fl not in FLOWS:
            bad(f"(b) error {e['code']} names flow {fl}")
pd = {d["id"] for d in PRO["source_defects"]}
for f in FLOWS.values():
    for s in f["steps"]:
        for d in s.get("defects") or []:
            if d not in pd:
                bad(f"(b) {f['id']} step {s['seq']} defect {d} undefined")
report["b_protocol_messages"] = {
    "flows": len(FLOWS), "steps": sum(len(f["steps"]) for f in FLOWS.values()),
    "message_or_returns_items_examined": nmsg, "joined": sum(1 for r in rows if r["targets"]),
    "no_structure_in_messages_yaml": sum(1 for r in rows if not r["targets"]),
    "error_codes_examined": codes_used, "protocol_error_codes": len(perr), "msg20_codes": len(CODES),
}

# ---------------------------------------------------------------- (c) triggers
def T(cls, *targets):
    return (cls, list(targets))


RULES = [
    (r"steps? \d[\d.\-]*( test| skipped| shape test| \(\u00a74\.2 steps 1-6\))?", "step"),
    (r"call cryptosuite\.verifyProof", ("message", ["MSG-09.verifyProof"])),
    (r"call createProof", ("message", ["MSG-09.createProof"])),
    (r"cryptosuite verification result", ("message", ["MSG-10"])),
    (r"cryptosuite error", ("message", ["MSG-09", "MSG-20"])),
    (r"parse JSON bytes to an Infra value", ("message", ["MSG-13.documentBytes"])),
    (r"Add Proof \(§4\.2\)( again)?", ("message", ["MSG-11"])),
    (r"Add Proof Set/Chain \(§4\.3\)", ("message", ["MSG-12"])),
    (r"Add Proof with options\.challenge", ("message", ["MSG-23.challenge"])),
    (r"Verify Proof with challenge", ("message", ["MSG-13.challenge"])),
    (r"run §4\.4 steps 4-8 on inputDocument", ("message", ["MSG-13", "MSG-15.securedDocument"])),
    (r"steps 4-8 (complete|raise)", ("event", ["MSG-14", "MSG-20"])),
    (r"(next proof in allProofs|loop over allProofs ends|continue loop|results exhausted|next cryptosuiteVerificationResult|start)",
     ("event", ["MSG-15.securedDocument", "MSG-16.successfulVerificationResults"])),
    (r"previousProof test", ("event", ["MSG-02.previousProof"])),
    (r"options test", ("event", ["MSG-12.options.previousProof"])),
    (r"compaction result", ("event", ["MSG-17.recompact"])),
    (r"implementation rule", ("event", ["MSG-17"])),
    (r"an intermediary removes a (member|named proof)", ("event", ["MSG-04", "MSG-05"])),
    (r"read verificationMethod", ("event", ["MSG-02.verificationMethod"])),
    (r"dereference the URL", ("event", ["MSG-02.verificationMethod", "MSG-22"])),
    (r"cryptosuite-specific means", ("event", ["MSG-02.verificationMethod", "MSG-22"])),
    (r"binding check", ("event", ["MSG-22"])),
    (r"verification relationship validation", ("event", ["MSG-21", "MSG-02.proofPurpose"])),
    (r"controller check.*", ("event", ["MSG-22.controller"])),
    (r"validity check", ("event", ["MSG-02.created", "MSG-02.expires"])),
    (r"verifier retires the value", ("event", ["MSG-02.challenge"])),
    (r"the same challenge presented again", ("event", ["MSG-02.challenge"])),
    (r"resolve", ("event", ["MSG-07"])),
    (r"hash check", ("event", ["MSG-06.digestMultibase", "MSG-07"])),
]


def ptr_ok(p):
    mid, _, fld = p.partition(".")
    if mid not in M:
        return False
    return (not fld) or fld in FIELDS[mid]


trig_rows = []
cls_count = collections.Counter()
n_tr = 0
tid_dups = []
for m in SM["machines"]:
    fl = [FLOWS[x] for x in m["flows"] if x in FLOWS]
    if len(fl) != len(m["flows"]):
        bad(f"(c) {m['id']} names an unknown flow")
    states = {s["name"] for s in m["states"]}
    for st in [m["initial"]] + list(m.get("final_states") or []) + list(m.get("error_states") or []):
        if st not in states:
            bad(f"(c) {m['id']} lists state {st} not in states")
    tids = collections.Counter(t["id"] for t in m["transitions"])
    tid_dups += [(m["id"], k) for k, v in tids.items() if v > 1]
    incoming = collections.Counter(t["to"] for t in m["transitions"])
    for st in (m.get("final_states") or []) + (m.get("error_states") or []):
        if incoming[st] == 0:
            bad(f"(c) {m['id']} state {st} is final/error with no incoming transition")
    for t in m["transitions"]:
        n_tr += 1
        for e in (t["from"], t["to"]):
            if e not in states:
                bad(f"(c) {m['id']} {t['id']} state {e} undefined")
        for c in re.split(r",\s*", t.get("error_code") or ""):
            if c and c not in CODES:
                bad(f"(c) {m['id']} {t['id']} error_code {c} not in MSG-20")
        for d in t.get("defects") or []:
            if d not in pd:
                bad(f"(c) {m['id']} {t['id']} defect {d} undefined")
        tr = t["trigger"]
        cls, tg, note = None, [], ""
        for pat, res in RULES:
            if re.fullmatch(pat, tr):
                if res == "step":
                    mm = re.match(r"steps? (\d+(?:\.\d+)?)", tr)
                    n = mm.group(1)
                    nxt = "test" in tr and str(t.get("step")) == str(int(n.split(".")[0]) + 1)
                    ok = nxt or (t.get("step") == n) or re.search(r"step[s]? " + re.escape(n) + r"\b", t["locator"]) \
                        or n.split(".")[0] == str(t.get("step")).split(".")[0]
                    if not ok:
                        bad(f"(c) {m['id']} {t['id']} trigger {tr!r} vs step {t.get('step')} {t['locator']}")
                    cls = "step"
                    note = "outcome branch of step %s; continues at step %s" % (n, t.get("step")) \
                        if str(t.get("step")) != n and "test" in tr else ""
                else:
                    cls, tg = res
                break
        if cls is None:
            bad(f"(c) {m['id']} {t['id']} trigger {tr!r} is not a step, message or named event")
            cls = "UNCLASSIFIED"
        for p in tg:
            if not ptr_ok(p):
                bad(f"(c) {m['id']} {t['id']} trigger {tr!r} points at {p}, not in messages.yaml")
        cls_count[cls] += 1
        trig_rows.append({"machine": m["id"], "transition": t["id"], "trigger": tr, "class": cls,
                          "targets": tg, "step": str(t.get("step") or ""), "note": note})
if tid_dups:
    bad(f"(c) duplicate transition ids {tid_dups}")
report["c_triggers"] = {"machines": len(SM["machines"]), "transitions_examined": n_tr,
                        "distinct_triggers": len({r["trigger"] for r in trig_rows}),
                        "by_class": dict(cls_count), "unclassified": cls_count.get("UNCLASSIFIED", 0)}


# ---------------------------------------------------------------- (d) examples vs schema
T = json.loads((HERE / "schema/schema-tests.derived.json").read_text())["cases"]
covered = collections.defaultdict(lambda: collections.Counter())
for c in T:
    e = c.get("example")
    if isinstance(e, dict):
        covered[e["file"]][c["expect"]] += 1
fixtures = sorted(p.name for p in (HERE / "examples").glob("ex[0-9][0-9]-*.derived.json"))
fixtures += sorted(p.name for p in (HERE / "examples").glob("ex[0-9][0-9]-*.json") if ".derived" not in p.name
                   and p.name.replace(".json", ".derived.json") not in fixtures)
ex_rows = []
for fx in fixtures:
    cov = covered.get(fx)
    if not cov:
        # verbatim twin covered under its derived name?
        ex_rows.append({"fixture": fx, "schema_cases": 0, "note": "no schema-tests case"})
    else:
        ex_rows.append({"fixture": fx, "schema_cases": sum(cov.values()), "accept": cov.get("accept", 0), "reject": cov.get("reject", 0)})
unsecured = {}
try:
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012
    S = {p.name: json.loads(p.read_text()) for p in (HERE / "schema").glob("*.derived.schema.json")}
    reg = Registry().with_resources([(x["$id"], Resource.from_contents(x, default_specification=DRAFT202012)) for x in S.values()])
    v = Draft202012Validator(S["secured-document.derived.schema.json"], registry=reg)
    for n in ("ex01-simple-json-document.derived.json", "ex03-simple-json-ld-document.derived.json"):
        errs = [e.message for e in v.iter_errors(json.loads((HERE / "examples" / n).read_text()))]
        unsecured[n] = "reject: " + errs[0] if errs else "accept"
        if not errs:
            bad(f"(d) {n} is an unsecured document and secured-document.derived accepts it")
except ImportError:
    unsecured = {"not run": "jsonschema not importable; run with PYTHONPATH to a directory that has jsonschema and referencing"}
report["d_examples"] = {"fixtures_listed": len(ex_rows), "with_schema_cases": sum(1 for r in ex_rows if r["schema_cases"]),
                        "without_schema_cases": [r["fixture"] for r in ex_rows if not r["schema_cases"]],
                        "unsecured_documents_against_secured_document_schema": unsecured}

# ---------------------------------------------------------------- (f) defect ids
README = (HERE / "README.md").read_text()
dn = (HERE / "design-notes.md").read_text()
dn = dn[dn.index("## 9. Source defects"):dn.index("## 10. bears_on")]
norm = (HERE / "normative.md").read_text()
defined = {
    "protocol.yaml (and state-machine.yaml, which cites them)": [d["id"] for d in PRO["source_defects"]],
    "normative.md": re.findall(r"^### (SD-[\dE]+)", norm, flags=re.M),
    "messages.yaml and schema/README.md": [t["id"] for t in MSG["source_tensions"]],
    "design-notes.md": re.findall(r"^- \*\*(D\d+)\.", dn, flags=re.M),
    "examples/README.md": re.findall(r"^- \*\*(EXD-\d\d)\*\*", (HERE / "examples/README.md").read_text(), flags=re.M),
}
flat = collections.Counter(i for v in defined.values() for i in v)
clash = [i for i, n in flat.items() if n > 1]
if clash:
    bad(f"(f) the same defect id is defined in two schemes: {clash}")
missing = [i for v in defined.values() for i in v if not re.search(r"(?<![\w-])" + re.escape(i) + r"(?![\w])", README.split("## Defect crosswalk")[-1] if "## Defect crosswalk" in README else "")]
if missing:
    bad(f"(f) defect ids missing from the README crosswalk: {missing}")
sm_ids = set(re.findall(r"\bD-\d\d\b", (HERE / "state-machine.yaml").read_text()))
if not sm_ids <= {d["id"] for d in PRO["source_defects"]}:
    bad(f"(f) state-machine.yaml cites defect ids not in protocol.yaml: {sorted(sm_ids - {d['id'] for d in PRO['source_defects']})}")
report["f_defect_ids"] = {"schemes": {k: len(v) for k, v in defined.items()}, "ids_defined": sum(len(v) for v in defined.values()),
                          "ids_defined_twice": len(clash), "ids_missing_from_readme_crosswalk": len(missing),
                          "state_machine_defect_citations_examined": len(sm_ids)}

# ---------------------------------------------------------------- output
report["problems_found"] = len(problems)
print(json.dumps(report, indent=1, ensure_ascii=False))
for p in problems:
    print("PROBLEM", p)


def key(k):
    return k if re.fullmatch(r"[A-Za-z_][\w.\-]*", k) else json.dumps(k)


def y(o, ind=0):
    pad = "  " * ind
    if isinstance(o, dict):
        out = []
        for k, v in o.items():
            if isinstance(v, (dict, list)) and v:
                out.append(f"{pad}{key(k)}:")
                out.append(y(v, ind + 1))
            else:
                out.append(f"{pad}{key(k)}: {json.dumps(v, ensure_ascii=False) if not isinstance(v, (dict, list)) else ('[]' if isinstance(v, list) else '{}')}")
        return "\n".join(out)
    out = []
    for v in o:
        if isinstance(v, dict):
            first = True
            for k, w in v.items():
                lead = f"{pad}- " if first else f"{pad}  "
                first = False
                k = key(k)
                if isinstance(w, (dict, list)) and w:
                    out.append(f"{lead}{k}:")
                    out.append(y(w, ind + 2))
                else:
                    out.append(f"{lead}{k}: {json.dumps(w, ensure_ascii=False) if not isinstance(w, (dict, list)) else ('[]' if isinstance(w, list) else '{}')}")
        else:
            out.append(f"{pad}- {json.dumps(v, ensure_ascii=False)}")
    return "\n".join(out)


if "--write" in sys.argv:
    head = ("# w3c-vc-data-integrity-1-0 cross-check joins, FX-1 pass 3. DERIVED by crosscheck.derived.py from the\n"
            "# distilled artifacts; not source text. Re-run the script, do not edit by hand.\n")
    doc = {
        "record": REC, "kind": "crosscheck", "derived_by": "crosscheck.derived.py", "extracted": "2026-11-07",
        "reviewed_by": "",
        "counts": report,
        "examples_against_schema": ex_rows,
        "field_atoms_not_a_member": [{"atom": a, "requirements": ids,
                                      "wired_by": sorted({o for i in ids for o in owner.get(i, ())}),
                                      "listed_under_not_wired": [i for i in ids if i in notwired]} for a, ids in indirect],
        "protocol_message_join": rows,
        "trigger_join": trig_rows,
    }
    (HERE / "crosscheck.yaml").write_text(head + y(doc) + "\n")
sys.exit(1 if problems else 0)
