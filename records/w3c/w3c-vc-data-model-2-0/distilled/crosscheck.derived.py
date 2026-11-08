#!/usr/bin/env python3
"""crosscheck.derived.py -- DERIVED from the distilled artifacts of w3c-vc-data-model-2-0.
FX-1 pass 3 (cross-check). Library-written, not source text. Adapted from the finished sibling's
w3c-vc-data-integrity-1-0/distilled/crosscheck.derived.py.

Joins, by script (each resolved pair was also read by the pass-3 agent):
  (a) every field a requirement's `field` names exists in messages.yaml and the schema;
  (b) protocol <-> messages: every step's message_ref and every messages_used entry of protocol.yaml
      (the vocabulary of 26) resolves to a messages.yaml structure, or is recorded as a gap of the
      source (design-notes.md open question 12);
  (c) every state-machine trigger is a defined message (resolving through (b)) or a named event;
  (d) every example agrees with the schema as recorded (vectors.yaml expectation against the checks of
      results.derived.json; the schema is re-run in addition by schema/run_checks.derived.py);
  (e) the credentialSubject id-only decision is pinned to a schema test;
  (f) schema and cross-field-rule line citations carry requirement ids (cite-requirements.derived.py),
      and the defect-id inventory behind the README crosswalk is complete;
  (g) the numbers the README states, recomputed.
Usage:  python3 -I crosscheck.derived.py [--lib DIR]           # report only
        python3 -I crosscheck.derived.py [--lib DIR] --write   # also rewrite crosscheck.yaml
(--lib DIR adds a directory holding jsonschema and referencing to sys.path: python3 -I ignores PYTHONPATH.)
Every count printed is EXAMINED beside FOUND.
"""
import collections
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "bin"))
if "--lib" in sys.argv:
    sys.path.insert(0, sys.argv[sys.argv.index("--lib") + 1])
import _yaml  # noqa: E402

REC = "w3c-vc-data-model-2-0"


def load(n):
    return _yaml.parse((HERE / n).read_text())


REQ = load("requirements.yaml")["requirements"]
MSG = load("messages.yaml")
PRO = load("protocol.yaml")
SM = load("state-machine.yaml")
VEC = load("examples/vectors.yaml")
rid = {x["id"].split("#")[1]: x for x in REQ}
problems = []
report = {}


def bad(msg):
    problems.append(msg)


def short(i):
    return i.split("#")[1]


# ------------------------------------------------------------ indexes
M = {m["name"]: m for m in MSG["messages"]}
FIELDS = {n: {re.sub(r"^\(|\)$", "", f["name"]) for f in (m.get("fields") or [])} for n, m in M.items()}
allfields = collections.defaultdict(list)
for n, fs in FIELDS.items():
    for f in fs:
        allfields[f].append(n)
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


def cited_ids(o, into, where):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "constrained_by" and isinstance(v, list):
                for x in v:
                    into[short(x)].add(where)
            else:
                cited_ids(v, into, where)
    elif isinstance(o, list):
        for v in o:
            cited_ids(v, into, where)


cited = collections.defaultdict(set)
cited_ids(MSG, cited, "messages")
cited_ids(PRO, cited, "protocol")
cited_ids(SM, cited, "state-machine")
cited_ids(VEC, cited, "vectors")

# ---------------------------------------------------------------- (a) fields
OWNER = {  # first segment of a dotted field path -> the messages.yaml structure that holds its members
    "credentialSubject": "CredentialSubject", "credentialStatus": "CredentialStatus",
    "credentialSchema": "CredentialSchema", "refreshService": "RefreshService", "termsOfUse": "TermsOfUse",
    "evidence": "Evidence", "relatedResource": "RelatedResource", "confidenceMethod": "ReservedExtensionEntry",
    "renderMethod": "ReservedExtensionEntry", "verifiableCredential": "VerifiablePresentation",
    "issuer": "Issuer",
}
SHAPE = re.compile(r"@?[A-Za-z][A-Za-z0-9]*(\[\*\])?(\.@?[A-Za-z][A-Za-z0-9]*(\[\*\])?)*")
atoms = collections.defaultdict(list)
for x in REQ:
    f = re.sub(r"\([^)]*\)", "", x["field"])
    for a in re.split(r";|,| or ", f):
        a = a.split(":")[0].strip().lstrip(".")
        if a:
            atoms[a].append(short(x["id"]))
prop_rows, concept_atoms, unresolved = [], [], []
for a, ids in sorted(atoms.items()):
    segs = re.sub(r"\[\*\]", "", a).split(".")
    shaped = bool(SHAPE.fullmatch(a)) and (len(segs) > 1 or "[*]" in a or a.startswith("@")
                                           or re.search(r"[a-z][A-Z]", a) or a in allfields)
    if not shaped:
        concept_atoms.append((a, ids))
        continue
    if len(segs) == 1:
        ok = segs[0] in allfields and (segs[0] in props or all(not M[n].get("schema") for n in allfields[segs[0]]))
        prop_rows.append({"atom": a, "requirements": ids, "messages": sorted(allfields.get(segs[0], [])),
                          "schema_files": sorted(props.get(segs[0], [])), "resolved": ok})
    else:
        own = OWNER.get(segs[0])
        ok = bool(own) and own in M and segs[-1] in FIELDS[own] and segs[-1] in props
        prop_rows.append({"atom": a, "requirements": ids, "messages": [own] if ok else [],
                          "schema_files": sorted(props.get(segs[-1], [])), "resolved": ok})
    if not ok:
        unresolved.append(a)
        bad(f"(a) field atom {a} ({','.join(ids)}) is not a member of messages.yaml and the schema")
# a requirement whose atoms are property-shaped must be cited by a message
parent_ids = {short(x["split_of"]) for x in REQ if x.get("split_of")}
active = [x for x in REQ if x["status"] == "active"]
leaf_active = {short(x["id"]) for x in active if short(x["id"]) not in parent_ids}  # a split parent is never cited (pass 2)
prop_ids = {i for r in prop_rows for i in r["requirements"]} & leaf_active
cited_by_msg = {k for k, v in cited.items() if "messages" in v}
unwired_prop = sorted(i for i in prop_ids if i not in cited_by_msg)
nowhere = sorted(i for i in leaf_active if i not in cited)
tok_pat = r"(?<![\w#@/.])@?[a-z]+[A-Z][A-Za-z]*(?![\w])|@[a-z]+"
alltext = " ".join(p.read_text() for p in [HERE / "messages.yaml", HERE / "protocol.yaml", HERE / "state-machine.yaml",
                                           HERE / "schema/cross-field-rules.derived.yaml", HERE / "examples/vectors.yaml",
                                           HERE / "schema/README.md", HERE / "design-notes.md"]
                   + list((HERE / "schema").glob("*.schema.json")))
text_tokens = collections.defaultdict(set)
for x in REQ:
    for t in re.findall(tok_pat, x["text"]):
        text_tokens[t].add(short(x["id"]))
tok_absent = {t: sorted(v) for t, v in sorted(text_tokens.items()) if t not in alltext}
for t, v in tok_absent.items():
    bad(f"(a) camelCase/@ token {t} of {','.join(v)} appears in no artifact")
report["a_fields"] = {
    "requirements_examined": len(REQ), "active_requirements": len(active), "field_atoms_examined": len(atoms),
    "property_atoms": len(prop_rows), "property_atoms_resolved_to_messages_and_schema": sum(1 for r in prop_rows if r["resolved"]),
    "concept_atoms_not_a_member": len(concept_atoms),
    "requirements_behind_property_atoms": len(prop_ids),
    "property_requirements_cited_by_no_message": len(unwired_prop), "property_requirements_cited_by_no_message_ids": unwired_prop,
    "active_requirements_cited_by_no_artifact": len(nowhere),
    "text_tokens_examined": len(text_tokens), "text_tokens_absent_from_artifacts": tok_absent,
}
for i in unwired_prop:
    bad(f"(a) {i} names a member ({rid[i]['field']}) and no node of messages.yaml cites it")

# ---------------------------------------------------------------- (b) join
ROLES = {r["name"] for r in PRO["roles"]}
FLOWS = {f["id"]: f for f in PRO["flows"]}
MU = {m["id"]: m for m in PRO["messages_used"]}
S, G, Fd = "structure", "gap", "field"  # structure resolves; field resolves to a member only; gap = the source defines none
J = {  # MU id -> (class, [(messages.yaml name, [fields that must exist])], note)
    "MU-01": (S, [("VerifiableCredential", ["@context", "type", "issuer", "credentialSubject"])], "the same structure without the proof"),
    "MU-02": (S, [("VerifiableCredential", ["@context", "type", "issuer", "credentialSubject", "proof"]), ("MediaType application/vc", ["Type name"])], ""),
    "MU-03": (S, [("VerifiablePresentation", ["@context", "type", "verifiableCredential", "holder", "proof"]), ("MediaType application/vp", ["Type name"])], ""),
    "MU-04": (S, [("EnvelopedVerifiableCredential", ["@context", "id", "type"])], ""),
    "MU-05": (S, [("EnvelopedVerifiablePresentation", ["@context", "id", "type"])], ""),
    "MU-06": (G, [("EnvelopedVerifiableCredential", ["id"]), ("MediaType application/vc", ["Encoding considerations"])],
              "the enveloping serialization (JOSE, COSE, SD-JWT) is defined by the securing specification, not by the source; only the carrier (the data: URL of an enveloped object) and the media type are here"),
    "MU-07": (Fd, [("VerifiableCredential", ["proof"]), ("EmbeddedProofRelation", ["relating property"])],
              "the members of a proof belong to VC Data Integrity (messages.yaml applicability)"),
    "MU-08": (S, [("VerificationInput", ["inputMediaType", "inputData"])], "added in pass 3: pass 1 had no structure for the input"),
    "MU-09": (S, [("VerificationAlgorithmResult", ["status", "document", "mediaType", "controller", "controlledIdentifierDocument", "warnings", "errors"])], ""),
    "MU-10": (S, [("SecuringMechanismVerificationResult", ["verified", "verifiedDocument", "mediaType"])], ""),
    "MU-11": (S, [("ProblemDetails", ["type", "title", "detail"])], ""),
    "MU-12": (S, [("CredentialStatus", ["id", "type"])], ""),
    "MU-13": (G, [], "the credentialStatus type defines it (L2277); the source defines no status information"),
    "MU-14": (S, [("RefreshService", ["type", "id"])], ""),
    "MU-15": (G, [("RefreshService", ["type"])], "no request structure: Example 27 POSTs the credential and §5.4 says no more"),
    "MU-16": (S, [("TermsOfUse", ["type", "id"])], ""),
    "MU-17": (S, [("Evidence", ["id", "type"])], ""),
    "MU-18": (S, [("CredentialSchema", ["id", "type"])], ""),
    "MU-19": (S, [("RelatedResource", ["id", "mediaType", "digestSRI", "digestMultibase"])], ""),
    "MU-20": (G, [("RelatedResource", ["mediaType", "digestSRI", "digestMultibase"])],
              "the HTTP response (bytes and Content-Type header) is HTTP's, not a structure of the source; the three members above are what it is checked against"),
    "MU-21": (G, [], "the source mentions a request (Appendix A.1, §9.5.2) and defines no structure or property for it"),
    "MU-22": (S, [("BaseContext", ["digest"]), ("VerifiableCredential", ["@context"])], ""),
    "MU-23": (Fd, [("VerificationAlgorithmResult", ["controlledIdentifierDocument"])],
              "the document's structure is defined by Controlled Identifiers v1.0, outside the source"),
    "MU-24": (G, [("VerifiableCredential", ["proof"])], "derivation of presentable data and its proof is delegated to the securing mechanism (§4.13, §5.7)"),
    "MU-25": (G, [], "§5.11 only requires a registered media type for the input document; no structure"),
    "MU-26": (G, [], "Appendix A.4 names a data registry and defines nothing (non-normative)"),
}
mu_rows = []
for mid, m in MU.items():
    if mid not in J:
        bad(f"(b) {mid} has no entry in the join table")
        continue
    cls, tg, note = J[mid]
    targets = []
    for name, fl in tg:
        if name not in M:
            bad(f"(b) {mid} -> {name} is not a messages.yaml structure")
            continue
        miss = [x for x in fl if x not in FIELDS[name]]
        if miss:
            bad(f"(b) {mid} -> {name} lacks fields {miss}")
        targets.append({"message": name, "kind": M[name]["kind"], "fields_checked": fl})
    if cls in (S, Fd) and not targets:
        bad(f"(b) {mid} is classed {cls} and has no target")
    mu_rows.append({"id": mid, "name": m["name"], "class": cls, "targets": targets, "note": note})
for k in J:
    if k not in MU:
        bad(f"(b) join entry {k} matches no messages_used entry")
step_rows = []
n_steps = n_msg = 0
used = collections.Counter()
mu_names = {k: v["name"] for k, v in MU.items()}
for fid, f in FLOWS.items():
    for r in f["participants"]:
        if r not in ROLES:
            bad(f"(b) {fid} participant {r} is not a role")
    for s in f["steps"]:
        n_steps += 1
        n_msg += 1
        ref = s["message_ref"]
        used[ref] += 1
        if ref not in MU:
            bad(f"(b) {fid} step {s['n']} message_ref {ref} is not in messages_used")
        elif s["message"] != mu_names[ref]:
            bad(f"(b) {fid} step {s['n']} message {s['message']!r} is not {ref}'s name")
        for side in ("from", "to"):
            if s[side] not in ROLES:
                bad(f"(b) {fid} step {s['n']} {side} {s[side]} is not a role")
        cls = J[ref][0] if ref in J else "UNJOINED"
        step_rows.append({"flow": fid, "step": str(s["n"]), "message_ref": ref, "class": cls, "basis": s["basis"]})
for mid, m in MU.items():
    if str(m["used_by_steps"]) != str(used[mid]):
        bad(f"(b) {mid} says used_by_steps {m['used_by_steps']}, the flows use it {used[mid]} times")
step_ids = {(fid, str(s["n"])) for fid, f in FLOWS.items() for s in f["steps"]}
tids = {t["id"] for m in SM["machines"] for t in m["transitions"]}
ep_ptr = 0
for e in PRO["error_paths"]:
    if e["detected_by"] not in ROLES:
        bad(f"(b) error path {e['id']} detected_by {e['detected_by']} is not a role")
    for p in e["in"]:
        ep_ptr += 1
        if re.fullmatch(r"M\d\d", p):
            if p not in {m["id"] for m in SM["machines"]}:
                bad(f"(b) error path {e['id']} names machine {p}: no such machine")
        elif re.fullmatch(r"M\d\d-T\d\d", p):
            if p not in tids:
                bad(f"(b) error path {e['id']} names transition {p}: no such transition")
        else:
            fl, _, st = p.partition(" ")
            if (fl, st) not in step_ids:
                bad(f"(b) error path {e['id']} names {p}: no such step")
pd = {d["id"] for d in PRO["source_defects_and_tensions"]}
used_defs = set(re.findall(r"\bT-\d\d\b", (HERE / "protocol.yaml").read_text())) | set(re.findall(r"\bT-\d\d\b", (HERE / "state-machine.yaml").read_text()))
if not used_defs <= pd:
    bad(f"(b) protocol.yaml or state-machine.yaml cites tensions that protocol.yaml does not define: {sorted(used_defs - pd)}")
cls_count = collections.Counter(r["class"] for r in mu_rows)
report["b_protocol_messages"] = {
    "flows": len(FLOWS), "steps_examined": n_steps, "step_message_refs_resolved_to_messages_used": sum(1 for r in step_rows if r["message_ref"] in MU),
    "messages_used_examined": len(MU), "by_class": dict(cls_count),
    "step_items_by_class": dict(collections.Counter(r["class"] for r in step_rows)),
    "messages_used_resolving_to_a_structure": cls_count[S] + cls_count[Fd],
    "messages_used_that_are_source_gaps": cls_count[G],
    "error_paths_examined": len(PRO["error_paths"]), "error_path_pointers_examined": ep_ptr,
    "tension_ids_cited_examined": len(used_defs),
}

# ---------------------------------------------------------------- (c) triggers
TU = {t["name"]: t for t in SM["triggers_used"]}
trig_rows = []
cls_t = collections.Counter()
n_tr = 0
tr_use = collections.Counter()
flow_ids = set(FLOWS)
for m in SM["machines"]:
    states = {s["name"] for s in m["states"]}
    for st in [m["initial"]] + list(m.get("terminal_states") or []) + list(m.get("error_states") or []):
        if st not in states:
            bad(f"(c) {m['id']} lists state {st} not in states")
    for fl in re.split(r",\s*", m["protocol_flow"]):
        if fl.split(" ")[0] not in flow_ids:
            bad(f"(c) {m['id']} protocol_flow {fl} names an unknown flow")
    ids = collections.Counter(t["id"] for t in m["transitions"])
    for k, v in ids.items():
        if v > 1:
            bad(f"(c) duplicate transition id {k}")
    incoming = collections.Counter(t["to"] for t in m["transitions"])
    for st in (m.get("terminal_states") or []) + (m.get("error_states") or []):
        if incoming[st] == 0:
            bad(f"(c) {m['id']} state {st} is terminal/error with no incoming transition")
    for t in m["transitions"]:
        n_tr += 1
        for e in (t["from"], t["to"]):
            if e not in states:
                bad(f"(c) {m['id']} {t['id']} state {e} undefined")
        for p in t.get("protocol_steps") or []:
            fl, _, st = p.partition(" ")
            if (fl, st) not in step_ids:
                bad(f"(c) {t['id']} protocol_steps {p}: no such step")
        tr = t["trigger"]
        tr_use[tr] += 1
        d = TU.get(tr)
        if d is None:
            bad(f"(c) {m['id']} {t['id']} trigger {tr!r} is neither a defined message nor a named event")
            cls_t["UNDEFINED"] += 1
            continue
        if d["kind"] == "message" or d.get("resolves_to"):
            if d["resolves_to"] not in MU:
                bad(f"(c) trigger {tr} resolves_to {d['resolves_to']}: not in messages_used")
                c2 = "UNRESOLVED"
            else:
                c2 = "message->" + J[d["resolves_to"]][0]
            tg = d["resolves_to"]
        else:
            if not (d.get("definition") and d.get("locator")):
                bad(f"(c) event {tr} has no definition or locator")
            c2, tg = "named-event", ""
        cls_t[c2] += 1
        trig_rows.append({"machine": m["id"], "transition": t["id"], "trigger": tr, "kind": d["kind"],
                          "class": c2, "resolves_to": tg})
for name, d in TU.items():
    if str(d["used_by_transitions"]) != str(tr_use.get(name, 0)):
        bad(f"(c) trigger {name} says used_by_transitions {d['used_by_transitions']}, found {tr_use.get(name, 0)}")
report["c_triggers"] = {
    "machines": len(SM["machines"]), "transitions_examined": n_tr, "triggers_defined": len(TU),
    "distinct_triggers_used": len(tr_use), "by_class": dict(cls_t),
    "undefined": cls_t.get("UNDEFINED", 0) + cls_t.get("UNRESOLVED", 0),
    "triggers_kind_message": sum(1 for d in TU.values() if d["kind"] == "message"),
    "triggers_kind_event": sum(1 for d in TU.values() if d["kind"] == "event"),
}

# ---------------------------------------------------------------- (d) examples vs the recorded checks
RES = json.loads((HERE / "examples/results.derived.json").read_text())["results"]
ex_rows = []
agree = 0
for v in VEC["vectors"]:
    pf = mf = mp = sf = 0
    for fx in v["fixtures"]:
        if fx["file"] not in RES:
            bad(f"(d) {v['id']} fixture {fx['file']} has no recorded checks")
        for c in RES.get(fx["file"], []):
            if c["check"] == "parse" and c["result"] == "fail":
                pf += 1
            if "must:" in c["check"] and c["result"] == "fail":
                mf += 1
            if "must:" in c["check"] and c["result"] == "pass":
                mp += 1
            if c["check"] in ("shape", "wrap", "kind") and c["result"] == "fail":
                sf += 1
    e = v["expect"]
    if e == "accept":
        ok = mf == 0 and sf == 0
    elif e == "not-parseable":
        ok = pf >= 1 and mp == 0
    elif e == "accept-after-comment-removal":
        ok = pf >= 1 and mf == 0
    elif e in ("reject", "reject-reading-A"):
        ok = mf >= 1 or sf >= 1 or pf >= 1
    else:
        ok = False
    agree += ok
    if not ok:
        bad(f"(d) {v['id']} expects {e}; recorded checks: parse fail {pf}, must fail {mf}, shape fail {sf}")
    ex_rows.append({"vector": v["id"], "expect": e, "fixtures": len(v["fixtures"]), "parse_fail": pf,
                    "must_fail": mf, "must_pass": mp, "shape_fail": sf, "agrees": ok})
sch_tests = json.loads((HERE / "schema/schema-tests.derived.json").read_text())["cases"]
unsecured_ok = None
try:
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    SCH = {p.name: json.loads(p.read_text()) for p in (HERE / "schema").glob("*.derived.schema.json")}
    reg = Registry().with_resources([(x["$id"], Resource.from_contents(x)) for x in SCH.values()])
    base = "urn:library:" + REC + ":"
    n_run = n_off = 0
    for c in sch_tests:
        tgt = c["schema"]
        val = Draft202012Validator({"$ref": base + tgt}, registry=reg)
        inst = c["instance"] if "instance" in c else json.loads((HERE / "examples" / c["fixture"]).read_text().replace("\u00a0", " "))
        got = "accept" if not list(val.iter_errors(inst)) else "reject"
        n_run += 1
        if got != c["expect"]:
            n_off += 1
            bad(f"(d) schema case {c['id']} expects {c['expect']}, the schema says {got}")
    unsecured_ok = {"schema_cases_rerun": n_run, "unexpected": n_off}
except ImportError:
    unsecured_ok = {"not run": "jsonschema not importable; pass --lib DIR (or run schema/run_checks.derived.py)"}
report["d_examples"] = {"vectors_examined": len(ex_rows), "vectors_agreeing_with_recorded_checks": agree,
                        "fixtures_examined": sum(r["fixtures"] for r in ex_rows),
                        "recorded_checks_examined": sum(len(RES[f["file"]]) for v in VEC["vectors"] for f in v["fixtures"] if f["file"] in RES),
                        "schema_cases_rerun": unsecured_ok}

# ---------------------------------------------------------------- (e) credentialSubject holding only id
e_case = [c for c in sch_tests if c["id"] == "vc-subject-id-only"]
if len(e_case) != 1 or e_case[0]["expect"] != "reject":
    bad("(e) schema-tests has no 'vc-subject-id-only' reject case")
n_subj = n_id_only = 0
for fx in sorted((HERE / "examples").glob("ex*.json")):
    try:
        doc = json.loads(fx.read_text().replace("\u00a0", " "))
    except ValueError:
        continue

    def subjects(o):
        global n_subj, n_id_only
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "credentialSubject":
                    for s in (v if isinstance(v, list) else [v]):
                        if isinstance(s, dict):
                            n_subj += 1
                            n_id_only += set(s) <= {"id"}
                subjects(v)
        elif isinstance(o, list):
            for v in o:
                subjects(v)
    subjects(doc)
if n_id_only:
    bad(f"(e) {n_id_only} fixture credentialSubject objects hold only id; the schema rejects them")
subj = json.loads((HERE / "schema/vcdm.derived.schema.json").read_text())["$defs"]["subjectObject"]
e_ok = subj.get("anyOf") is not None and "R-0173" in subj["$comment"] and "R-0174" in subj["$comment"]
if not e_ok:
    bad("(e) the subjectObject comment does not ground the id-only rejection in R-0173 and R-0174")
report["e_subject_id_only"] = {"test_cases_for_it": len(e_case), "fixture_subject_objects_examined": n_subj, "fixture_subject_objects_holding_only_id": n_id_only, "schema_comment_cites_R_0173_R_0174": e_ok,
                               "decision": "rejected: R-0173 and R-0174 (stated MUSTs) require a claim serialized inside the object; R-0175's note reads an id-only object as no claim"}

# ---------------------------------------------------------------- (f) line citations carry requirement ids
cit = re.compile(r"\u00bb\s*\(([^()]*\bL(\d+)(?:-L?(\d+))?[^()]*)\)")
NO_REQ = {  # citations and rules whose lines no requirement carries, each with the ground
    "\u00a7B.3.1 L4146": "a pointer to SRI's ABNF in an appendix about a datatype: no keyword and no candidate",
    "X-20": "candidate C-0197 (L3345-3346) is rejected: section 6.3 is marked non-normative",
}
req_lines = collections.defaultdict(set)
for x in REQ:
    if "source_lines" in x and short(x["id"]) not in {short(y["split_of"]) for y in REQ if y.get("split_of")}:
        for part in str(x["source_lines"]).split(","):
            mm = re.fullmatch(r"\s*(\d+)(?:\s*-\s*(\d+))?\s*", part)
            if mm:
                for ln in range(int(mm.group(1)), int(mm.group(2) or mm.group(1)) + 1):
                    req_lines[ln].add(short(x["id"]))
n_cit = n_with = n_allowed = 0
for f in sorted((HERE / "schema").glob("*.schema.json")):
    t = f.read_text()
    for m in cit.finditer(t):
        n_cit += 1
        if re.search(r"R-\d{4}", m.group(1)):
            n_with += 1
        else:
            key = m.group(1).strip()
            if key in NO_REQ and not req_lines.get(int(m.group(2))):
                n_allowed += 1
            else:
                bad(f"(f) schema citation ({key}) carries no requirement id and is not a recorded exception (run cite-requirements.derived.py)")
rules = load("schema/cross-field-rules.derived.yaml")["rules"]
n_rule_with = n_rule_allowed = 0
for r in rules:
    if r.get("requirements"):
        n_rule_with += 1
        for i in r["requirements"]:
            if short(i) not in rid:
                bad(f"(f) rule {r['id']} cites {i}, which is not a requirement")
    elif r["id"] in NO_REQ and not req_lines.get(int(str(r["source_lines"]).split("-")[0])):
        n_rule_allowed += 1
    else:
        bad(f"(f) rule {r['id']} carries no requirements list and is not a recorded exception")
report["f_requirement_ids_beside_lines"] = {
    "schema_quote_citations_examined": n_cit, "with_requirement_ids": n_with, "carried_by_no_requirement": n_allowed,
    "cross_field_rules_examined": len(rules), "rules_with_requirement_ids": n_rule_with, "rules_carried_by_no_requirement": n_rule_allowed,
    "exceptions": NO_REQ}

# defect-id inventory behind the README crosswalk
README = (HERE / "README.md").read_text()
cw = README[README.index("## Defect crosswalk"):]
cw = cw[:cw.index("\n## ", 5)] if "\n## " in cw[5:] else cw
defined = {
    "P": [d["id"] for d in PRO["source_defects_and_tensions"]],
    "N": re.findall(r"^### (SD-\d+)", (HERE / "normative.md").read_text(), flags=re.M),
    "S": re.findall(r"^\| ((?:F|T)-\d\d[a-z]?) \|", (HERE / "schema/README.md").read_text(), flags=re.M),
    "DN": re.findall(r"^- \*\*(D\d+)\.", (HERE / "design-notes.md").read_text(), flags=re.M),
    "X": [d["id"] for d in VEC["defects"]],
}
for t in SM["source_tensions"]:
    if not any(short_t in (t.get("see") or "") for short_t in [t["id"]]) or t["id"] not in defined["P"]:
        bad(f"(f) state-machine tension {t['id']} does not point at protocol.yaml")
sch_cites = set(re.findall(r"\b(?:F|T)-\d\d[a-z]?\b", (HERE / "messages.yaml").read_text())) - set()
if not sch_cites <= set(defined["S"]) | set(defined["P"]):
    bad(f"(f) messages.yaml cites ids defined nowhere: {sorted(sch_cites - set(defined['S']) - set(defined['P']))}")
vec_cites = set(re.findall(r"\bD-\d\d\b", (HERE / "examples/vectors.yaml").read_text()))
if not vec_cites <= set(defined["X"]):
    bad(f"(f) vectors.yaml cites {sorted(vec_cites - set(defined['X']))}")
rows = [r for r in cw.splitlines() if r.startswith("|") and not r.startswith("|---") and not r.startswith("| source defect")]
cols = {k: set() for k in defined}
order = ["P", "N", "S", "DN", "X"]


def expand(cell, rx):
    out = set()
    for a, b in re.findall(rf"({rx}\d+[a-z]?) to ({rx}\d+[a-z]?)", cell):
        pre = re.match(rf"({rx})", a).group(1)
        for n in range(int(re.search(r"\d+", a).group()), int(re.search(r"\d+", b).group()) + 1):
            out.add(f"{pre}{n:02d}" if "-" in pre else f"{pre}{n}")
    out |= set(re.findall(rf"{rx}\d+[a-z]?", cell))
    return out


for r in rows:
    cells = [c.strip() for c in r.strip("|").split("|")]
    if len(cells) != 6:
        bad(f"(f) crosswalk row has {len(cells)} cells: {r[:60]}")
        continue
    for k, c in zip(order, cells[1:]):
        rx = {"P": r"T-", "N": r"SD-", "S": r"(?:F|T)-", "DN": r"D", "X": r"D-"}[k]
        cols[k] |= expand(c, rx)
tail = cw.split("Protocol gaps and tensions with no counterpart")[-1] if "Protocol gaps and tensions with no counterpart" in cw else ""
cols["P"] |= expand(tail.replace("P:", ""), r"T-")
missing = {k: sorted(set(defined[k]) - cols[k]) for k in defined}
extra = {k: sorted(cols[k] - set(defined[k])) for k in defined}
for k in defined:
    if missing[k]:
        bad(f"(f) crosswalk lacks {k}: {missing[k]}")
    if extra[k]:
        bad(f"(f) crosswalk names {k} ids that are not defined: {extra[k]}")
report["f_defect_ids"] = {"schemes": {k: len(v) for k, v in defined.items()}, "ids_defined": sum(len(v) for v in defined.values()),
                          "ids_in_crosswalk": sum(len(v) for v in cols.values()),
                          "ids_missing_from_crosswalk": sum(len(v) for v in missing.values()),
                          "ids_in_crosswalk_but_undefined": sum(len(v) for v in extra.values()),
                          "colliding_bare_ids_across_schemes": sorted(set(defined["P"]) & set(defined["S"]))}

# ---------------------------------------------------------------- (g) the numbers README states, recomputed
nm = (HERE / "normative.md").read_text()
kinds = collections.Counter(m["kind"] for m in MSG["messages"])
nfields = sum(len(m.get("fields") or []) for m in MSG["messages"])
nodes = list(MSG["messages"]) + [f for m in MSG["messages"] for f in (m.get("fields") or [])]
cites_total = sum(len(n.get("constrained_by") or []) for n in nodes)
cites_ids = {short(x) for n in nodes for x in (n.get("constrained_by") or [])}
empty_nodes = sum(1 for n in nodes if not n.get("constrained_by"))
quotes_p = len(re.findall(r"^\s*(?:- )?(?:\"?quote\"?): ", (HERE / "protocol.yaml").read_text(), flags=re.M))
quotes_s = len(re.findall(r"^\s*(?:- )?(?:\"?quote\"?): ", (HERE / "state-machine.yaml").read_text(), flags=re.M))
flat = collections.Counter(c["result"] for r in RES.values() for c in r)
infer_steps = sum(1 for f in PRO["flows"] for s in f["steps"] if s["basis"] == "inferred")
CAND = load("inferred-candidates.yaml")["candidates"]
rec = {
    "requirements_entries": len(REQ), "requirements_active": len(active), "requirements_withdrawn": len(REQ) - len(active),
    "requirements_kind_inferred": sum(1 for x in REQ if x["kind"] == "inferred"),
    "requirements_split_parents": len(parent_ids), "requirements_split_children": sum(1 for x in REQ if x.get("split_of")),
    "normative_markers": len(re.findall(r"^<!-- q L", nm, flags=re.M)),
    "normative_definition_scope_recital_blocks": len(re.findall(r"^_\[(?:definition|scope|recital)\]_", nm, flags=re.M)),
    "normative_markers_in_sd_section": len(re.findall(r"^<!-- q L", nm[nm.index("### SD-1 "):], flags=re.M)),
    "requirements_stated_non_parent": sum(1 for x in REQ if x["kind"] == "stated") - len(parent_ids),
    "requirements_skeleton_entries": sum(1 for x in REQ if int(short(x["id"])[2:]) <= 127),
    "requirements_promoted_candidates": sum(1 for x in REQ if re.search(r"C-\d{4}", " ".join(str(v) for v in x.values()))),
    "candidates": len(CAND), "candidates_stated": sum(1 for c in CAND if c["verdict"] == "stated"),
    "candidates_rejected": sum(1 for c in CAND if c["verdict"] == "reject"),
    "messages_nodes_structures": len(MSG["messages"]), "messages_by_kind": dict(kinds), "messages_fields": nfields,
    "messages_citations": cites_total, "messages_distinct_ids": len(cites_ids),
    "messages_nodes_total": len(nodes), "messages_nodes_empty": empty_nodes,
    "protocol_roles": len(PRO["roles"]), "protocol_flows": len(PRO["flows"]), "protocol_steps": n_steps,
    "protocol_steps_inferred": infer_steps, "protocol_error_paths": len(PRO["error_paths"]),
    "protocol_tensions": len(PRO["source_defects_and_tensions"]), "protocol_messages_used": len(MU),
    "protocol_quotations": quotes_p,
    "sm_machines": len(SM["machines"]), "sm_states": sum(len(m["states"]) for m in SM["machines"]),
    "sm_transitions": n_tr, "sm_quotations": quotes_s,
    "examples_vectors": len(VEC["vectors"]), "examples_fixtures": len(RES), "examples_checks": sum(flat.values()),
    "examples_by_result": dict(flat),
    "examples_vector_citations": sum(len(v["constrained_by"]) for v in VEC["vectors"]),
    "examples_vector_distinct_ids": len({short(x) for v in VEC["vectors"] for x in v["constrained_by"]}),
    "schema_cases": len(sch_tests), "schema_rules": len(rules),
}
report["g_recount"] = rec
README_CLAIMS = [  # (computed key, README pattern that must contain the computed value)
    ("requirements_entries", r"{v} entries"), ("sm_machines", r"{v} machines"), ("sm_states", r"{v} states"),
    ("sm_transitions", r"{v} transitions"), ("protocol_flows", r"{v} flows"), ("protocol_steps", r"{v} steps"),
    ("protocol_roles", r"{v} roles"), ("protocol_error_paths", r"{v} error paths"),
    ("messages_fields", r"{v} fields"), ("examples_vectors", r"{v} vectors"), ("examples_checks", r"{v} checks"),
    ("schema_cases", r"{v} test cases"), ("schema_rules", r"{v} cross-field rules"),
    ("messages_citations", r"{v} citations of"), ("messages_distinct_ids", r"citations of {v} requirement ids"),
    ("protocol_quotations", r"{v} quotations"), ("sm_quotations", r"{v} quotations"),
    ("messages_nodes_total", r"of the {v} nodes"),
    ("normative_markers", r"{v} markers in all"), ("normative_definition_scope_recital_blocks", r"{v} definition, scope and recital"),
    ("normative_markers_in_sd_section", r"\({v} quotations\)"), ("requirements_stated_non_parent", r"\({v}\)"),
    ("requirements_skeleton_entries", r"{v} from the skeleton"), ("requirements_split_children", r"{v} split children"),
    ("requirements_promoted_candidates", r"{v} promoted candidates"), ("requirements_kind_inferred", r"{v} inferred"),
    ("candidates", r"All {v} candidates"), ("candidates_stated", r"{v} stated"), ("candidates_rejected", r"{v} rejected"),
]
claims_checked = claims_bad = 0
for key, pat in README_CLAIMS:
    claims_checked += 1
    if not re.search(pat.format(v=rec[key]), README):
        claims_bad += 1
        bad(f"(g) README does not state {pat.format(v=rec[key])!r} ({key}={rec[key]})")
report["g_readme_claims"] = {"claims_examined": claims_checked, "stale": claims_bad}

# ---------------------------------------------------------------- output
report["problems_found"] = len(problems)
print(json.dumps(report, indent=1, ensure_ascii=False))
for p in problems:
    print("PROBLEM", p)


def key(k):
    return k if re.fullmatch(r"[A-Za-z_][\w.\-]*", k) else json.dumps(k)


def scalar(w):
    if isinstance(w, list):
        return "[]"
    if isinstance(w, dict):
        return "{}"
    return json.dumps(w, ensure_ascii=False)


def y(o, ind=0):
    pad = "  " * ind
    if isinstance(o, dict):
        out = []
        for k, v in o.items():
            if isinstance(v, (dict, list)) and v:
                out.append(f"{pad}{key(k)}:")
                out.append(y(v, ind + 1))
            else:
                out.append(f"{pad}{key(k)}: {scalar(v)}")
        return "\n".join(out)
    out = []
    for v in o:
        if isinstance(v, dict):
            first = True
            for k, w in v.items():
                lead = f"{pad}- " if first else f"{pad}  "
                first = False
                if isinstance(w, (dict, list)) and w:
                    out.append(f"{lead}{key(k)}:")
                    out.append(y(w, ind + 2))
                else:
                    out.append(f"{lead}{key(k)}: {scalar(w)}")
        else:
            out.append(f"{pad}- {json.dumps(v, ensure_ascii=False)}")
    return "\n".join(out)


if "--write" in sys.argv:
    head = ("# w3c-vc-data-model-2-0 cross-check joins, FX-1 pass 3. DERIVED by crosscheck.derived.py from the\n"
            "# distilled artifacts; not source text. Re-run the script, do not edit by hand.\n")
    doc = {
        "record": REC, "kind": "crosscheck", "derived_by": "crosscheck.derived.py", "extracted": "2026-11-07",
        "reviewed_by": "",
        "counts": report,
        "messages_used_join": mu_rows,
        "step_join": step_rows,
        "trigger_join": trig_rows,
        "property_atoms": prop_rows,
        "concept_atoms_not_a_member": [{"atom": a, "requirements": ids} for a, ids in concept_atoms],
        "active_requirements_cited_by_no_artifact": nowhere,
        "examples_against_recorded_checks": ex_rows,
    }
    (HERE / "crosscheck.yaml").write_text(head + y(doc) + "\n")
sys.exit(1 if problems else 0)
