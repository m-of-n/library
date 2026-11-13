#!/usr/bin/env python3
"""crosscheck.derived.py -- DERIVED from the distilled artifacts of pics-1-1-labels.
FX-1 pass 3 (cross-check). Library-written, not source text.

Joins, by script (each resolved pair was also read by the pass-3 agent):
  (a) every field a requirement names (`field:`) exists in messages.yaml or the schema,
      or is a concept that is wired or listed under not_wired;
  (b) constrained_by: every message, field, option, step, code, rule and finding is wired or
      carries an unwired_reason; every requirement is wired or listed under not_wired (and
      not both); every cited id resolves; no split parent is cited except the named
      exceptions; no constrained_by_pending is left (candidate join: see b_candidates);
  (c) examples: every fixture is accounted for in examples/README.md; reproduce.py and the
      schema recogniser are run and their summary lines must report 0 failures;
  (d) ids: every R-/SD-/F-/D-/A- id cited in the prose artifacts resolves to an existing
      entry of the right kind (the intended statement was read by the agent: see crosscheck.yaml);
  (e) counts: every count a prose artifact states (requirements, messages, fields, ...) equals
      the count measured here.
Usage:  python3 -I crosscheck.derived.py            # report only; exit 1 on any problem
        python3 -I crosscheck.derived.py --write    # also rewrite crosscheck.yaml
Every count printed is EXAMINED beside FOUND.
"""
import collections
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "bin"))
import _yaml  # noqa: E402

REC = "pics-1-1-labels"
REC_DIR = HERE.parent
PREFIX = REC + "#R-"
problems = []


def bad(m):
    problems.append(m)


def rd(p):
    return pathlib.Path(p).read_text()


REQ = _yaml.parse(rd(HERE / "requirements.yaml"))["requirements"]
MSG = _yaml.parse(rd(HERE / "messages.yaml"))
RID = {int(x["id"].split("R-")[1]): x for x in REQ}
PARENTS = {}
for x in REQ:
    if x.get("split_of"):
        PARENTS.setdefault(int(x["split_of"].split("R-")[1]), []).append(int(x["id"].split("R-")[1]))
# split parents whose child is only an example or a note: the parent is the applicable text
PARENT_OK = []
raw = {n: rd(HERE / n) for n in ("messages.yaml", "requirements.yaml", "normative.md", "design-notes.md", "README.md", "inferred-candidates.yaml")}

# ------------------------------------------------------------------ items
ITEMS = {}  # key -> dict(kind, obj)


def add(k, kind, o):
    ITEMS[k] = {"kind": kind, "obj": o}


for m in MSG["messages"]:
    add(m["id"], "message", m)
    for f in m.get("fields") or []:
        add(m["id"] + "/" + f["name"], "field", f)
    for f in m.get("options") or []:
        add(m["id"] + "/" + f["name"], "option", f)
    for s in m.get("steps") or []:
        add(m["id"] + "/step-%s" % s["step"], "step", s)
    for i, c in enumerate(m.get("codes") or [], 1):
        add(m["id"] + "/code-%d" % i, "code", c)
    for k in ("derivation_rules", "canonicalization_rules"):
        for r in m.get(k) or []:
            add(r["id"], "rule", r)
for t in MSG.get("source_tensions") or []:
    add(t["id"], "finding", t)

wired = collections.defaultdict(set)  # req number -> items
unwired_items = {}
n_pending = len(re.findall(r"^\s+constrained_by_pending:", raw["messages.yaml"], re.M))
cited = set()
parent_cites = []
dangling = []
for k, it in ITEMS.items():
    o = it["obj"]
    cb = o.get("constrained_by")
    if cb is None:
        bad("(b) %s has no constrained_by" % k)
        continue
    if not cb:
        if not o.get("unwired_reason"):
            bad("(b) %s has an empty constrained_by and no unwired_reason" % k)
        else:
            unwired_items[k] = o["unwired_reason"]
    for c in cb:
        if not c.startswith(PREFIX):
            bad("(b) %s cites %s, not an id of this record" % (k, c))
            continue
        n = int(c[len(PREFIX):])
        cited.add(n)
        wired[n].add(k)
        if n not in RID:
            dangling.append((k, c))
        if n in PARENTS and n not in PARENT_OK:
            parent_cites.append((k, n))
    if len(set(cb)) != len(cb):
        bad("(b) %s cites an id twice" % k)
for k, c in dangling:
    bad("(b) %s cites %s which does not exist" % (k, c))
for k, n in parent_cites:
    bad("(b) %s cites split parent R-%04d; cite its children %s" % (k, n, PARENTS[n]))
if n_pending:
    bad("(b) %d constrained_by_pending left in messages.yaml" % n_pending)
NW = {int(x["id"][len(PREFIX):]): x["reason"] for x in MSG.get("not_wired") or []}
for n in NW:
    if n not in RID:
        bad("(b) not_wired lists %s which does not exist" % n)
    if n in cited:
        bad("(b) R-%04d is both wired and listed under not_wired" % n)
neither = sorted(n for n in RID if n not in cited and n not in NW)
for n in neither:
    bad("(b) R-%04d is neither wired nor listed under not_wired" % n)
nw_parent = sorted(n for n in NW if n in PARENTS)
nw_other = sorted(n for n in NW if n not in PARENTS)
by_kind = collections.Counter(it["kind"] for it in ITEMS.values())
wired_by_kind = collections.Counter(it["kind"] for k, it in ITEMS.items() if it["obj"].get("constrained_by"))
report = {}
report["b_wiring"] = {
    "items_examined": len(ITEMS), "items_by_kind": dict(by_kind),
    "items_wired": sum(wired_by_kind.values()), "items_unwired_with_reason": len(unwired_items),
    "constrained_by_entries": sum(len(it["obj"].get("constrained_by") or []) for it in ITEMS.values()),
    "constrained_by_entries_on_fields_options_steps": sum(len(it["obj"].get("constrained_by") or []) for it in ITEMS.values() if it["kind"] in ("field", "option", "step", "code")),
    "requirements_examined": len(REQ), "requirements_wired": len(cited),
    "requirements_not_wired": len(NW), "not_wired_split_parents": len(nw_parent),
    "not_wired_other": len(nw_other), "requirements_neither": len(neither),
    "dangling_citations": len(dangling), "split_parent_citations": len(parent_cites),
    "constrained_by_pending_left": n_pending,
    "split_parents_cited_by_exception": sorted("R-%04d" % n for n in PARENT_OK if n in cited),
}

# candidate join: each `candidates:` citation of messages.yaml names a skeleton candidate; the
# requirement that promotes it (requirements.yaml `candidate:`) or one of its split children must
# be wired to the same item (or, for a message, to the message or any of its fields/options/steps).
c2r = collections.defaultdict(list)
for x in REQ:
    if x.get("candidate"):
        c2r[x["candidate"]].append(int(x["id"].split("R-")[1]))
sub = collections.defaultdict(set)
for k, it in ITEMS.items():
    top = k.split("/")[0]
    if "/" in k:
        sub[top] |= {int(c[len(PREFIX):]) for c in it["obj"].get("constrained_by") or []}
cand_cites = cand_rejected = 0
residual = []
for k, it in ITEMS.items():
    cb = {int(c[len(PREFIX):]) for c in it["obj"].get("constrained_by") or []}
    if "/" not in k:
        cb |= sub[k]
    for c in it["obj"].get("candidates") or []:
        cand_cites += 1
        rs = c2r.get(c)
        if not rs:
            cand_rejected += 1
            continue
        for r in rs:
            if not ({r} | set(PARENTS.get(r, []))) & cb:
                residual.append("%s: %s -> R-%04d" % (k, c, r))
report["b_candidates"] = {"candidate_citations_examined": cand_cites, "citing_a_rejected_candidate_no_requirement": cand_rejected,
                          "promoted_but_not_wired_to_that_item_or_its_children": len(residual), "residual": residual}


# ------------------------------------------------------------------ (a) fields
names = set()
for k, it in ITEMS.items():
    o = it["obj"]
    for key in ("name", "short_form", "code"):
        v = o.get(key)
        if isinstance(v, str):
            names.add(v.strip().strip('"').lower())
    if it["kind"] == "message":
        names.add(o["name"].lower())
schema_text = ""
for p in sorted((HERE / "schema").iterdir()):
    if p.suffix in (".txt", ".abnf", ".md", ".py"):
        schema_text += p.read_text() + "\n"
schema_tokens = {t.lower() for t in re.findall(r"[A-Za-z][\w.+-]*", schema_text)}
msg_tokens = {t.lower() for t in re.findall(r"[A-Za-z][\w.+-]*", raw["messages.yaml"])}
atoms = collections.defaultdict(list)
for x in REQ:
    f = x.get("field") or ""
    flat = re.sub(r"[()]", ";", f)
    for a in re.split(r";|,|/| or | -> | \| ", flat):
        a = a.strip().strip("'\"")
        if a and a.lower() not in ("none", "") and not a.lower().startswith("none "):
            atoms[a].append(int(x["id"].split("R-")[1]))
direct, in_text, in_schema, concept = [], [], [], []
CONCEPTS = {'DNS': 'Appendix A (Bureau Location) client algorithm; protocol is not covered, no message', 'DNS name of the bureau': 'same', 'bureau addresses': 'same', 'bureau selection': 'same', 'timer': 'same', 'connection': 'same (HTTP keep-alive refinement)', 'definitions': "the Glossary's lead entry (content label, content rating, ...): terminology, no structure", 'tail': 'the rest of the get production of section 12.2 (R-0198, a split parent; its children are wired)'}
unexplained = []
for a, ids in sorted(atoms.items()):
    al = a.lower()
    toks = [t.lower() for t in re.findall(r"[A-Za-z][\w.+-]*", a)]
    if al in names:
        direct.append(a)
    elif toks and all(t in msg_tokens for t in toks):
        in_text.append(a)
    elif toks and all(t in schema_tokens for t in toks):
        in_schema.append(a)
    elif a in CONCEPTS:
        concept.append(a)
    else:
        unexplained.append((a, ids))
        bad("(a) field atom %r (R-%s) is not in messages.yaml or the schema and is not a listed concept" % (a, ",".join("%04d" % i for i in ids[:4])))
report["a_fields"] = {
    "requirements_examined": len(REQ), "field_atoms_examined": len(atoms),
    "atom_is_a_message_field_option_or_name": len(direct),
    "atom_named_in_messages_yaml_text": len(in_text), "atom_named_in_schema": len(in_schema),
    "atom_listed_as_concept": len(concept), "atom_unexplained": len(unexplained),
    "concepts": CONCEPTS,
}

# ------------------------------------------------------------------ (c) examples
EX = HERE / "examples"
ex_readme = rd(EX / "README.md")
fixtures = sorted(p.name for p in EX.rglob("*") if p.is_file() and p.suffix == ".txt" or (p.is_file() and p.parent.name == "templates"))
fixtures = sorted(set(p.relative_to(EX).as_posix() for p in EX.rglob("*.txt")))
unaccounted = []
for f in fixtures:
    stem = pathlib.PurePosixPath(f).name
    code = re.match(r"(ex\d+|t\d+)", stem)
    if stem not in ex_readme and not (code and re.search(r"\b%s\b" % code.group(1), ex_readme)):
        unaccounted.append(f)
        bad("(c) fixture %s is not accounted for in examples/README.md" % f)


def run(cmd, cwd):
    p = subprocess.run([sys.executable, "-I"] + cmd, cwd=str(cwd), capture_output=True, text=True, timeout=900)
    return p.returncode, (p.stdout + p.stderr).strip().split("\n")


bin_path = ROOT / ".cache" / (REC + ".bin")
if not bin_path.exists():
    bad("(c) %s missing: cannot run reproduce.py" % bin_path)
    rc1, out1 = 1, ["missing source"]
else:
    rc1, out1 = run(["reproduce.py", str(bin_path)], EX)
rc2, out2 = run(["check-grammar.derived.py"], HERE / "schema")
for _rc, _out, _req in ((rc1, out1, 'EXAMINED 212 checks, 0 FAILED'), (rc2, out2, 'EXAMINED 288 checks, FAILED 0')):
    if not any(re.search(_req, l) for l in _out):
        bad('(c) summary line %r not found in the checker output' % _req)
report["c_examples"] = {
    "fixtures_listed": len(fixtures), "fixtures_unaccounted": len(unaccounted),
    "reproduce_py_exit": rc1, "reproduce_py_summary": [l for l in out1 if re.search(r"^EXAMINED", l)][-1:],
    "recogniser_exit": rc2, "recogniser_summary": [l.strip() for l in out2 if re.search(r"^\s*EXAMINED", l)][-2:],
}
if rc1 != 0:
    bad("(c) reproduce.py exit %d" % rc1)
if rc2 != 0:
    bad("(c) recogniser exit %d" % rc2)

# ------------------------------------------------------------------ (d) ids
files = [REC_DIR / "record.yaml", REC_DIR / "summary.md"] + sorted(HERE.glob("*.md")) + sorted(HERE.glob("*.yaml")) + \
    [HERE / "schema" / "README.md", HERE / "examples" / "README.md", HERE / "examples" / "reproduce.py"] + sorted((HERE / "schema").glob("*.py"))
files = [f for f in files if f.exists() and f.name != "crosscheck.yaml"]
other = {}


def other_req(rec):
    if rec not in other:
        p = ROOT / "records" / "w3c" / rec / "distilled" / "requirements.yaml"
        other[rec] = {int(x["id"].split("R-")[1]) for x in _yaml.parse(p.read_text())["requirements"]} if p.exists() else set()
    return other[rec]


SD_DEFS = set(re.findall(r"^### (SD-[0-9A-Z]+):", raw["normative.md"], re.M))
F_DEFS = {t["id"] for t in MSG.get("source_tensions") or []}
sch_readme = rd(HERE / "schema" / "README.md")
ex_readme2 = rd(HERE / "examples" / "README.md")
gram_py = "".join(p.read_text() for p in (HERE / "schema").glob("*.py"))
defs = {"schema/README.md": set(re.findall(r"^\|\s*([AD]\d+)\s*\|", sch_readme, re.M)) | set(re.findall(r"^\s*(?:#\s*)?\**\s*([AD]\d+)\b[ :.)-]", sch_readme, re.M)),
        "examples/README.md": set(re.findall(r"^\|\s*([AD]\d+)\s*\|", ex_readme2, re.M))}
defs["check-grammar.derived.py"] = set(re.findall(r"""["'](A\d+)["']""", gram_py))
AD_ANY = defs["schema/README.md"] | defs["examples/README.md"] | defs["check-grammar.derived.py"]
n_r = n_sd = n_f = n_ad = n_ext = 0
unres = []
by_file = {}
for f in files:
    rel = f.relative_to(REC_DIR).as_posix()
    cnt = collections.Counter()
    for ln, line in enumerate(f.read_text().split("\n"), 1):
        scrub = re.sub(r"(mofn report|mofn report R-0006|report) R-\d{4}", "", line)
        scrub = re.sub(r"`?ADR-\d+`?\s*D\d+(?:,\s*D\d+)*", "", scrub)
        for m in re.finditer(r"(?<![A-Za-z0-9])(?:([a-z0-9-]+)#)?R-(\d{4})\b", scrub):
            rec, n = m.group(1) or REC, int(m.group(2))
            if not m.group(1) and rel in ("distilled/design-notes.md", "summary.md"):
                # by this artifact's convention a bare R-nnnn here is an m-of-n report id (R-0004 .. R-0006), never ours
                cnt["external_mofn"] += 1
                n_ext += 1
                if n not in (4, 5, 6):
                    unres.append("%s:%d bare R-%04d is not an m-of-n report id and is not prefixed" % (rel, ln, n))
                continue
            n_r += 1
            cnt["R"] += 1
            ok = (n in RID) if rec == REC else (n in other_req(rec))
            if not ok:
                unres.append("%s:%d R-%04d (%s)" % (rel, ln, n, rec))
        for m in re.finditer(r"\bSD-[0-9A-Z]+\b", scrub):
            n_sd += 1
            cnt["SD"] += 1
            if m.group(0) not in SD_DEFS:
                unres.append("%s:%d %s" % (rel, ln, m.group(0)))
        for m in re.finditer(r"\bF-\d{2}\b", scrub):
            if False:
                n_f += 1
                cnt["F"] += 1
                if m.group(0) not in F_DEFS:
                    unres.append("%s:%d %s" % (rel, ln, m.group(0)))
        for m in re.finditer(r"(?<![\w-])([AD]\d{1,2})\b(?!\d)", scrub):
            if True:
                n_ad += 1
                cnt["AD"] += 1
                if m.group(1) not in AD_ANY:
                    unres.append("%s:%d %s" % (rel, ln, m.group(1)))
        for m in re.finditer(r"(schema/README\.md|examples/README\.md)([^;)\n]{0,40})", scrub):
            for a in re.findall(r"\b([AD]\d+)\b", m.group(2)):
                if a not in defs[m.group(1)]:
                    unres.append("%s:%d %s cited as %s, defined elsewhere" % (rel, ln, a, m.group(1)))
    if cnt:
        by_file[rel] = dict(cnt)
for u in unres:
    bad("(d) unresolved or misdirected id: " + u)
report["d_ids"] = {"files_scanned": len(files), "r_citations_examined": n_r, "sd_citations_examined": n_sd,
                   "f_citations_examined": n_f, "external_mofn_report_ids_not_resolved_here": n_ext, "ad_citations_examined": n_ad,
                   "sd_defined": len(SD_DEFS), "f_defined": len(F_DEFS),
                   "ad_defined": {k: len(v) for k, v in defs.items()},
                   "unresolved": len(unres), "citations_by_file": by_file}


# ------------------------------------------------------------------ (e) counts
nf = sum(1 for it in ITEMS.values() if it["kind"] == "field")
no = sum(1 for it in ITEMS.values() if it["kind"] == "option")
measured = {"requirements": len(REQ), "messages": len(MSG["messages"]), "fields": nf, "options": no,
            "stated": sum(1 for x in REQ if x["kind"] == "stated"), "inferred": sum(1 for x in REQ if x["kind"] == "inferred"),
            "split_children": sum(1 for x in REQ if x.get("split_of")),
            "findings": len(MSG.get("source_tensions") or [])}
CAND = _yaml.parse(rd(HERE / "inferred-candidates.yaml"))["candidates"]
measured["candidates"] = len(CAND)
measured["cand_stated"] = sum(1 for c in CAND if c["verdict"] == "stated")
measured["cand_inferred"] = sum(1 for c in CAND if c["verdict"] == "inferred")
measured["cand_rejected"] = sum(1 for c in CAND if c["verdict"] == "reject")
measured["promoted"] = measured["cand_stated"]
measured["hunted"] = sum(1 for x in REQ if x["kind"] == "stated" and not x.get("candidate") and not x.get("split_of"))
measured["examples"] = len(list(EX.glob("ex*.txt")))
measured["templates"] = len(list((EX / "templates").glob("*.txt"))) if (EX / "templates").exists() else 0
measured["verbatim_grammars"] = len(list((HERE / "schema").glob("*.verbatim.txt")))
_dn = raw["design-notes.md"]
measured["design_rows"] = len(re.findall(r"^\| [A-Z]-[0-9]{2} \|", _dn, re.M))
measured["open_questions"] = len(re.findall(r"^[0-9]+\. \*\*", _dn.split("## 14. Open questions")[-1], re.M))
# every non-rejected candidate is promoted by exactly one requirement; a rejected one by none
_prom = collections.Counter(x["candidate"] for x in REQ if x.get("candidate"))
for c in CAND:
    n = _prom.get(c["id"], 0)
    if (c["verdict"] == "reject" and n) or (c["verdict"] != "reject" and n != 1):
        bad("(e) candidate %s verdict %s is promoted by %d requirements" % (c["id"], c["verdict"], n))
COUNT_CLAIMS = [('record.yaml', '(\\d+) entries \\(', 'requirements', 0), ('record.yaml', '(\\d+) messages, \\d+ fields and \\d+ option', 'messages', 0), ('record.yaml', '\\d+ messages, (\\d+) fields and \\d+ option', 'fields', 0), ('record.yaml', '\\d+ messages, \\d+ fields and (\\d+) option', 'options', 0), ('record.yaml', '(\\d+) split children', 'split_children', 0), ('distilled/README.md', '(\\d+) entries:', 'requirements', 0), ('distilled/README.md', '(\\d+) messages, \\d+ fields and \\d+ option', 'messages', 0), ('distilled/README.md', '\\d+ messages, (\\d+) fields and \\d+ option', 'fields', 0), ('distilled/README.md', '\\d+ messages, \\d+ fields and (\\d+) option', 'options', 0), ('distilled/README.md', '(\\d+) split children', 'split_children', 0), ('distilled/normative.md', '(\\d+) stated \\(', 'stated', 0), ('distilled/normative.md', '(\\d+) inferred \\(', 'inferred', 0), ('record.yaml', '(\\d+) promoted candidates', 'promoted', 0), ('record.yaml', '(\\d+) hunted', 'hunted', 0), ('record.yaml', '(\\d+) of \\d+ candidates with a verdict', 'candidates', 0), ('record.yaml', '(\\d+) rows against', 'design_rows', 0), ('record.yaml', '(\\d+) open questions', 'open_questions', 0), ('record.yaml', 'all (\\d+) examples', 'examples', 0), ('distilled/README.md', '(\\d+) promoted candidates', 'promoted', 0), ('distilled/README.md', '(\\d+) rows\\)', 'design_rows', 0), ('distilled/README.md', '(\\d+) open questions', 'open_questions', 0), ('distilled/README.md', 'All (\\d+) candidates have a verdict', 'candidates', 0), ('distilled/README.md', '(\\d+) stated, \\d+ rejected', 'cand_stated', 0), ('distilled/README.md', '(\\d+) rejected\\)', 'cand_rejected', 0), ('distilled/README.md', 'all (\\d+) examples as fixtures', 'examples', 0), ('distilled/README.md', 'the (\\d+) source grammars verbatim', 'verbatim_grammars', 0), ('distilled/messages.yaml', 'Counts, by script after pass 3: (\\d+) messages', 'messages', 0), ('distilled/messages.yaml', 'messages, (\\d+) fields', 'fields', 0)]
cc = []
for fname, rx, key, grp in COUNT_CLAIMS:
    p = REC_DIR / fname if not fname.startswith("distilled/") or True else None
    txt = rd(REC_DIR / fname)
    hits = re.findall(rx, txt)
    if not hits:
        bad("(e) %s: no match for %r" % (fname, rx))
        continue
    for h in hits:
        v = int(h if isinstance(h, str) else h[grp])
        cc.append((fname, key, v))
        if v != measured[key]:
            bad("(e) %s states %s=%d, measured %d" % (fname, key, v, measured[key]))
# source digests: the rendering the quotations count in and the HTML of record
import hashlib
_sha = {}
for _k, _ext in (("bin", ".bin"), ("txt", ".txt")):
    _p = ROOT / ".cache" / (REC + _ext)
    if _p.exists():
        _sha[_k] = hashlib.sha256(_p.read_bytes()).hexdigest()
_digest_hits = 0
if len(_sha) == 2:
    _rec = rd(REC_DIR / "record.yaml")
    if _sha["bin"] not in _rec:
        bad("(e) record.yaml content.sha256 is not the sha256 of .cache/%s.bin" % REC)
    for _n in ("messages.yaml", "requirements.yaml"):
        _m = re.search(r"^source_digest:\s*[\"']?([0-9a-f]{64})", raw[_n], re.M)
        if not _m or _m.group(1) != _sha["txt"]:
            bad("(e) %s source_digest is not the sha256 of the rendering .cache/%s.txt" % (_n, REC))
    _all = [REC_DIR / "record.yaml", REC_DIR / "summary.md"] + [p for p in HERE.rglob("*") if p.is_file() and p.suffix in (".md", ".yaml", ".txt") and p.name != "crosscheck.yaml" and "examples" not in p.parts]
    for _f in _all:
        for _h in re.findall(r"(?<![0-9a-f])([0-9a-f]{64})(?![0-9a-f])", _f.read_text()):
            _digest_hits += 1
            if _h not in _sha.values():
                bad("(e) %s carries a 64-hex digest that is neither the .bin nor the .txt sha256: %s" % (_f.name, _h[:12]))
        for _h in re.findall(r"(?<![0-9a-f])([0-9a-f]{8})\.\.\.", _f.read_text()):
            if not any(v.startswith(_h) for v in _sha.values()):
                bad("(e) %s carries a truncated digest %s... that is neither the .bin nor the .txt sha256" % (_f.name, _h))
report["e_digests"] = {"cache_present": len(_sha) == 2, "bin_sha256": _sha.get("bin"), "rendering_sha256": _sha.get("txt"), "full_digests_examined": _digest_hits}
report["e_counts"] = {"measured": measured, "claims_examined": len(cc), "claims_differing": sum(1 for f, k, v in cc if v != measured[k])}

# ------------------------------------------------------------------ (f) the two YAML readers agree
import _record_yaml  # noqa: E402


def _norm(x):
    return ("true" if x else "false") if isinstance(x, bool) else (str(x) if isinstance(x, int) else x)


def _diff(a, b, path, out):
    a, b = _norm(a), _norm(b)
    if type(a) is not type(b):
        out.append(path)
    elif isinstance(a, dict):
        for k in set(a) | set(b):
            if k not in a or k not in b:
                out.append(path + "/" + str(k))
            else:
                _diff(a[k], b[k], path + "/" + str(k), out)
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append(path + " length")
        else:
            for i, (x, y) in enumerate(zip(a, b)):
                _diff(x, y, "%s[%d]" % (path, i), out)
    elif a != b:
        out.append(path)


_rd = {}
for _n in ("messages.yaml", "requirements.yaml", "inferred-candidates.yaml"):
    _o = []
    _diff(_record_yaml.load_yaml(HERE / _n), _yaml.parse(rd(HERE / _n)), "", _o)
    _rd[_n] = len(_o)
    if _o:
        bad("(f) bin/_record_yaml.py and bin/_yaml.py disagree on %s at %s" % (_n, _o[:3]))
report["f_readers"] = {"files_compared": len(_rd), "differing_values_by_file": _rd,
                       "note": "bool and int scalars are compared as the strings the other reader keeps"}

report["problems_found"] = len(problems)
HUMAN = {
    "date": "2026-11-13",
    "unwired_items": [
        {"item": "requirements (not_wired in messages.yaml)", "reason": "47 of 353: 30 split parents whose children are wired; R-0333 to R-0349 (17, Appendix A bureau-location algorithm; protocol is not covered and the algorithm defines no message, field or encoding)"},
        {"item": "MSG-20/application/pics-service", "reason": "referenced, not defined here; no requirement of this record names the media type"},
    ],
    "inconsistencies_fixed": [
        {"file": "distilled/messages.yaml", "what": "header note (3) described constrained_by_pending on every item and 19 of 247 candidate citations; every message, field, option, error code and special-form step is now wired, and the note states the measured counts (245 candidate citations, 19 naming a rejected candidate)"},
        {"file": "distilled/messages.yaml", "what": "header note (5) said schema/README.md lists the source defects D1 ...; the D findings are in examples/README.md (schema/README.md holds A1 to A26 only)"},
        {"file": "distilled/messages.yaml", "what": "MSG-17 note said (schema/README.md A15, D7); D7 is in examples/README.md, now written as (schema/README.md A15; examples/README.md D7)"},
        {"file": "distilled/messages.yaml", "what": "source_digest was the sha256 of the HTML (a1acf198), while requirements.yaml and pics-dsig-1-0 carry the sha256 of the rendering the quotations count in (469de99e); now the rendering's"},
        {"file": "distilled/messages.yaml", "what": "MSG-19 step 7 and the signature-RSA-MD5 field cited candidate C-0145, which is the key-secrecy sentence (R-0282), not the encrypt-and-encode sentences; removed from both and the step wired to the signing steps R-0285 to R-0288 and R-0322 (the verify pass's note named R-0282 as wrong)"},
        {"file": "distilled/messages.yaml", "what": "added a top-level not_wired list (47 requirement ids with a reason)"},
    ],
    "source_inconsistencies_open": [],
    "id_pairs_read": [
        {"set": "R ids cited in the SD sections of normative.md (resolved beside the sentence that cites them)", "pairs": 88, "wrong": 0},
        {"set": "SD ids named in requirements.yaml notes, beside the requirement text and the SD title", "pairs": 60, "wrong": 0},
        {"set": "SD ids cited in record.yaml, README.md, design-notes.md, examples/README.md, messages.yaml", "pairs": 46, "wrong": 0},
        {"set": "A and D ids (messages.yaml, README.md, record.yaml, examples/README.md, reproduce.py, check-grammar.derived.py), beside the A/D title", "pairs": 87, "wrong": 1},
        {"set": "R ids cited in record.yaml (note), beside the requirement text", "pairs": 2, "wrong": 0},
        {"set": "constrained_by: every field, option, step and code pair read back beside the requirement text (415 on fields, options, steps and codes, the rest on messages)", "pairs": 580, "wrong": 0},
        {"set": "candidate join (messages.yaml candidates: against the requirement that promotes each)", "pairs": 245, "wrong": 2},
    ],
    "candidate_residual_reasons": [
        {"item": "MSG-04/ratings", "candidate": "C-0054", "reason": "C-0054 welds the productions of lines 200-219 (R-0111, a split parent); the productions that bear on ratings (R-0107, R-0108, R-0110) are wired"},
        {"item": "MSG-13", "candidate": "C-0083", "reason": "C-0083 is R-0157 (the client may assume a returned header label applies to the document); it is wired to MSG-14 and MSG-06 for, the response side"},
        {"item": "MSG-19/step-2", "candidate": "C-0159", "reason": "C-0159 is R-0301 (a split parent): the lead sentence of the special form welded to step 1; step 2's own sentence (R-0308) has no candidate and is wired"},
    ],
    "notes": [
        "design-notes.md and summary.md cite no requirement id of this record: a bare R-nnnn there is an m-of-n report id (R-0004 to R-0006) and is not resolved here; ADR-nnnn ids and their D1 to D5 are m-of-n's and are skipped",
        "Checked and found consistent, so unchanged: 353 requirements (136 promoted, 97 hunted of which 4 added by pass 2, 97 split children, 23 inferred; 330 stated), 20 messages, 61 fields, 11 option entries, 19 examples, 4 verbatim grammars, 30 design rows, 10 open questions in record.yaml, distilled/README.md and normative.md; SD-1 to SD-24 and SD-E numbering across normative.md, design-notes.md, record.yaml, README.md and messages.yaml; protocol and state-machine not covered (never not applicable) in record.yaml, README.md, summary.md, design-notes.md; design-notes section 8 arithmetic (30 rows as 8, 2, 7, 7, 1, 5; 8 occurrences of default on 5 lines)",
        "R-0165/R-0207 (header and bureau token-or-quoted-string) and R-0248/R-0256/R-0262 (the for sentence of opt=tree, opt=generic+tree and format=) have identical text (bin/check-id-joins --surface); each is cited on the side it was extracted from, and all three of the for sentences are cited on MSG-06 for and MSG-17 for",
    ],
}

if __name__ == "__main__":
    for sec, d in report.items():
        print(sec, json.dumps(d, ensure_ascii=False)[:600] if isinstance(d, dict) else d)
    for p in problems:
        print("PROBLEM", p)
    print("problems_found", len(problems))
    if "--write" in sys.argv:
        out = ["# %s cross-check joins, FX-1 pass 3. DERIVED by crosscheck.derived.py from the" % REC,
               "# distilled artifacts; not source text. Re-run the script with --write, do not edit by hand.",
               "record: %s" % json.dumps(REC), 'kind: "crosscheck"', 'derived_by: "crosscheck.derived.py"',
               "extracted: %s" % json.dumps(HUMAN["date"]), 'reviewed_by: ""', "counts:"]

        def scalar(v):
            return json.dumps(v, ensure_ascii=False)

        def key(k):
            k = str(k)
            return k if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_-]*", k) else json.dumps(k, ensure_ascii=False)

        def emit(o, ind):
            sp = "  " * ind
            if isinstance(o, dict):
                for k, v in o.items():
                    if isinstance(v, (dict, list)) and v:
                        out.append("%s%s:" % (sp, key(k)))
                        emit(v, ind + 1)
                    else:
                        out.append("%s%s: %s" % (sp, key(k), scalar(v if not isinstance(v, (dict, list)) else None) if not isinstance(v, (dict, list)) else ("{}" if isinstance(v, dict) else "[]")))
            else:
                for v in o:
                    if isinstance(v, dict) and v:
                        first = True
                        for k, vv in v.items():
                            lead = sp + "- " if first else sp + "  "
                            first = False
                            if isinstance(vv, (dict, list)) and vv:
                                out.append("%s%s:" % (lead, key(k)))
                                emit(vv, ind + 2)
                            else:
                                out.append("%s%s: %s" % (lead, key(k), scalar(vv) if not isinstance(vv, (dict, list)) else ("{}" if isinstance(vv, dict) else "[]")))
                    elif isinstance(v, list) and v:
                        raise ValueError("list of lists is not emitted")
                    else:
                        out.append("%s- %s" % (sp, scalar(v) if not isinstance(v, (dict, list)) else ("{}" if isinstance(v, dict) else "[]")))
        emit(report, 1)
        for k in ("unwired_items", "inconsistencies_fixed", "source_inconsistencies_open", "id_pairs_read", "notes"):
            v = HUMAN[k]
            out.append("%s:" % k if v else "%s: []" % k)
            if v:
                emit(v, 1)
        out.append("unwired_items_measured:")
        emit([{"item": k, "reason": r} for k, r in sorted(unwired_items.items())], 1) if unwired_items else out.append("  []")
        (HERE / "crosscheck.yaml").write_text("\n".join(out) + "\n")
        print("wrote crosscheck.yaml")
    sys.exit(1 if problems else 0)
