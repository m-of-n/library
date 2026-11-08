#!/usr/bin/env python3
"""cite-requirements.derived.py -- DERIVED, library-written (FX-1 pass 3, w3c-vc-data-model-2-0).

The derived schemas cite the source by line only ("«...» (§4.4 L425)"), and the cross-field rules by
`source_lines:`. This script puts the ids of the requirements that carry those lines beside the citations,
so the field-to-requirement join no longer goes through a line number:

  * schema/*.derived.schema.json  "$comment":  «quotation» (§4.4 L425)  ->  «quotation» (§4.4 L425; R-0146, R-0147)
  * schema/cross-field-rules.derived.yaml: a `requirements:` list beside `source_lines:`.

A requirement is chosen when (1) it carries one of the cited lines (its `source_lines`), (2) it is not a split
parent (a parent is never cited; its children are), and (3) its text and the quotation contain one another,
whitespace folded (a child may open with up to two connective words the quotation lacks, or lack its last word). Inferred entries have no line and are never chosen. A citation no requirement carries is
left as it is and reported. Ids the citation already names after the line are not repeated. Idempotent: it removes
what it inserted before it inserts again.

Usage:  python3 -I cite-requirements.derived.py            # report the pairs, change nothing
        python3 -I cite-requirements.derived.py --write    # edit the schema files and the rules file
Every count printed is EXAMINED beside FOUND.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
DIST = HERE.parent
sys.path.insert(0, str(DIST.parents[3] / "bin"))
import _yaml  # noqa: E402

REC = "w3c-vc-data-model-2-0"
REQ = _yaml.parse((DIST / "requirements.yaml").read_text())["requirements"]
PARENTS = {x["split_of"].split("#")[1] for x in REQ if x.get("split_of")}


def lines(s):
    out = set()
    for part in str(s).split(","):
        m = re.fullmatch(r"\s*(\d+)(?:\s*-\s*L?(\d+))?\s*", part)
        if m:
            out |= set(range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1))
    return out


BYLINE = {}
for x in REQ:
    if "source_lines" not in x or x["id"].split("#")[1] in PARENTS:
        continue
    for ln in lines(x["source_lines"]):
        BYLINE.setdefault(ln, []).append(x)


def fold(s):
    return re.sub(r"\s+", " ", s.replace("…", "")).strip()


def pick(quote, ls):
    q = fold(quote)
    got = {}
    for ln in ls:
        for x in BYLINE.get(ln, []):
            t = fold(x["text"])
            w = t.split(" ")
            # a child may begin with a connective its parent sentence supplied ("where each object MUST ...")
            variants = {t, " ".join(w[1:]), " ".join(w[2:]), " ".join(w[:-1])} if len(w) > 6 else {t}
            if any(v in q for v in variants if v) or q in t:
                got[x["id"].split("#")[1]] = x
    return sorted(got)


ADDED = re.compile(r"(?<=\d)(; R-\d{4}(?:, R-\d{4})*)(?=[,)]|$)")
CIT = re.compile(r"«([^«»]*)»\s*\(([^()]*)\)")
SPEC = re.compile(r"L(\d+)(?:-L?(\d+))?")
write = "--write" in sys.argv
examined = annotated = ids_added = 0
unmatched = []
pairs = []


def edit_comment(m):
    global examined, annotated, ids_added
    quote, cite = m.group(1), m.group(2)
    cite = ADDED.sub("", cite)
    spec = SPEC.search(cite)
    if not spec:
        return m.group(0)
    examined += 1
    ls = set()
    for a, b in SPEC.findall(cite):
        ls |= set(range(int(a), int(b or a) + 1))
    ids = [i for i in pick(quote, ls) if i not in cite]
    if not ids:
        if not [i for i in pick(quote, ls)]:
            unmatched.append(cite)
        return "«" + quote + "» (" + cite + ")"
    annotated += 1
    ids_added += len(ids)
    pairs.append((cite, ids, fold(quote)[:70]))
    new = cite[:spec.end()] + "; " + ", ".join(ids) + cite[spec.end():]
    return "«" + quote + "» (" + new + ")"


for f in sorted((DIST / "schema").glob("*.derived.schema.json")):
    t = f.read_text()
    t2 = CIT.sub(edit_comment, t)
    if write and t2 != t:
        f.write_text(t2)

# ---- the cross-field rules
rf = DIST / "schema/cross-field-rules.derived.yaml"
rules = _yaml.parse(rf.read_text())["rules"]
text = rf.read_text().split("\n")
out = []
i = 0
n_rules = n_rules_with = 0
sel = {}
for r in rules:
    n_rules += 1
    ids = pick(r["quote"], lines(r["source_lines"]))
    sel[r["id"]] = ids
    if ids:
        n_rules_with += 1
    else:
        unmatched.append("rule " + r["id"] + " L" + str(r["source_lines"]))
cur = None
skip = False
for ln in text:
    m = re.match(r"  - id: (X-\d+)", ln)
    if m:
        cur = m.group(1)
    if re.match(r"    requirements:\s*$", ln):
        skip = True
        continue
    if skip and re.match(r"      - ", ln):
        continue
    skip = False
    out.append(ln)
    if cur and re.match(r"    source_lines: ", ln) and sel.get(cur):
        out.append("    requirements:")
        out.extend('      - "%s#%s"' % (REC, i) for i in sel[cur])
        ids_added += len(sel[cur])
if write:
    rf.write_text("\n".join(out))
for cite, ids, q in pairs:
    print("PAIR", cite, "->", ",".join(ids), "|", q)
for r in rules:
    print("RULE", r["id"], r["source_lines"], "->", ",".join(sel[r["id"]]) or "-", "|", fold(r["quote"])[:60])
print("cite-requirements: EXAMINED %d schema quotation citations and %d rules; FOUND %d citations and %d rules with ids "
      "(%d ids placed), %d carried by no requirement: %s%s"
      % (examined, n_rules, annotated, n_rules_with, ids_added, len(unmatched), unmatched, "" if write else "  [dry run]"))
