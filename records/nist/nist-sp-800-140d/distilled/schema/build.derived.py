#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library; nist-sp-800-140d ships no schema, so
# every schema, message description and case below is this library's reading of its prose.
# Regenerates ../messages.yaml, *.derived.schema.json and ../examples/*.derived.json, then
# validates every case with jsonschema. Needs: python3 + jsonschema; run from anywhere.
import copy, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
DIST = HERE.parent
REC = DIST.parent
ID = REC.name
ROOT = REC.parent.parent.parent
sys.path.insert(0, str(ROOT / "bin"))
import _source_text as st            # noqa: E402
from _yaml import parse as yaml_a    # noqa: E402
import _record_yaml as yaml_b        # noqa: E402
import jsonschema                    # noqa: E402

WS = re.compile(r"\s+")
SRC = ROOT / ".cache" / (ID + ".txt")
RQ = yaml_a((DIST / "requirements.yaml").read_text())
cleaned = st.clean_for(st.read_lines(SRC), "pdf")
SOURCE_DIGEST = str(RQ.get("source_digest"))
TEXT_DIGEST = str(RQ.get("source_text_digest"))
DRAFT = "https://json-schema.org/draft/2020-12/schema"
LEVELS = {"shall", "should", "may", "must", "can", "will", "stated", "inferred"}


def span(a, b=None):
    return st.span(cleaned, a, b or a)


def Q(a, b=None):
    """{source_lines, quote} with the quote WRITTEN BY THIS FUNCTION from the
    cached source (never typed) and the range checked tight."""
    b = b or a
    t = span(a, b)
    if not t:
        raise SystemExit("Q(%s,%s): empty span" % (a, b))
    if a != b and (t in span(a + 1, b) or t in span(a, b - 1)):
        raise SystemExit("Q(%s,%s): range is wider than the text" % (a, b))
    return {"source_lines": ("%d-%d" % (a, b)) if a != b else str(a), "quote": t}


# ---- requirement ids: resolved by script, never typed -----------------------
REQS = [r for r in RQ["requirements"] if not r.get("split_of")]
USED = {}


def R(pattern, locator=None):
    """The id of the ONE requirement whose text matches `pattern` (re.search
    over whitespace-collapsed text). 0 or >1 matches raise."""
    hit = [r for r in REQS
           if re.search(pattern, WS.sub(" ", str(r["text"])).strip())
           and (locator is None or r["locator"] == locator)]
    if len(hit) != 1:
        raise SystemExit("R(%r, %r): %d matches %s" % (pattern, locator, len(hit),
                         [h["id"] for h in hit]))
    r = hit[0]
    USED[r["id"]] = (r["locator"], r.get("source_lines", "-"), WS.sub(" ", str(r["text"])).strip())
    return r["id"]


def RL(line, phrase=None):
    """The id of the ONE top-level requirement whose source_lines START on
    `line`, narrowed by a phrase of its text. 0 or >1 matches raise."""
    hit = [r for r in REQS if str(r.get("source_lines") or "").split("-")[0] == str(line)
           and (phrase is None or phrase in WS.sub(" ", str(r["text"])))]
    if len(hit) != 1:
        raise SystemExit("RL(%r, %r): %d matches %s" % (line, phrase, len(hit), [h["id"] for h in hit]))
    r = hit[0]
    USED[r["id"]] = (r["locator"], r.get("source_lines", "-"), WS.sub(" ", str(r["text"])).strip())
    return r["id"]


def EV(evid):
    """Requirement whose text opens with an evidence id (VE../TE../AS..)."""
    return R(r"^(?:(?:Additional )?Required [A-Za-z ]+? )?" + re.escape(evid) + r"\b")


# ---- JSON Schema fragments --------------------------------------------------
def S(**kw):
    d = {"type": "string", "minLength": 1}
    d.update(kw)
    return d


def I(lo=None, hi=None):
    d = {"type": "integer"}
    if lo is not None:
        d["minimum"] = lo
    if hi is not None:
        d["maximum"] = hi
    return d


def E(*vals):
    return {"enum": list(vals)}


def A(items, lo=0, uniq=False):
    d = {"type": "array", "items": items}
    if lo:
        d["minItems"] = lo
    if uniq:
        d["uniqueItems"] = True
    return d


BOOL = {"type": "boolean"}
TRUE = {"const": True}


def describe(s):
    if "$ref" in s:
        return "object (" + s["$ref"].split("/")[-1] + ")"
    if "const" in s:
        return "const " + json.dumps(s["const"])
    if "enum" in s:
        return "enum " + json.dumps(s["enum"], ensure_ascii=False)
    t = s.get("type")
    if t == "array":
        return "array of " + describe(s.get("items", {})) + (
            " (min %d)" % s["minItems"] if s.get("minItems") else "") + (
            ", unique" if s.get("uniqueItems") else "")
    if t == "integer":
        return "integer" + (" >= %s" % s["minimum"] if "minimum" in s else "") + (
            " <= %s" % s["maximum"] if "maximum" in s else "")
    if t == "string" and "pattern" in s:
        return "string, pattern " + s["pattern"]
    if "oneOf" in s or "anyOf" in s:
        return " or ".join(describe(x) for x in s.get("oneOf", s.get("anyOf")))
    return t or "any"


def F(name, sch, lvl, ex, req=True, cons=None, reason=None, note=None, lines=None):
    if lvl not in LEVELS:
        raise SystemExit("field %s: level %r" % (name, lvl))
    if lvl == "inferred" and not reason:
        raise SystemExit("field %s: inferred needs a reason" % name)
    if lvl == "stated" and not lines:
        raise SystemExit("field %s: stated needs source lines" % name)
    return dict(name=name, sch=sch, lvl=lvl, ex=ex, req=req, cons=cons, reason=reason,
                note=note, lines=lines)


def ST(name, title, locator, lines, cons, fields, caption=None, extra=None, defs=None,
       accept=(), reject=(), layout=None, note=None, props_override=None, minimal=None, also=None):
    if not cons:
        raise SystemExit(name + ": constrained_by is empty")
    return dict(name=name, title=title, locator=locator, lines=lines, cons=list(cons),
                fields=fields, caption=caption, extra=extra or {}, defs=defs,
                accept=list(accept), reject=list(reject), layout=layout, note=note,
                props_override=props_override, minimal=minimal, also=also or {})


# ---- schema, cases ----------------------------------------------------------
def build_schema(s):
    props = {f["name"]: f["sch"] for f in s["fields"]}
    sch = {"$schema": DRAFT, "$id": "urn:library:%s:%s" % (ID, s["name"]),
           "$comment": "DERIVED, not verbatim. Written by this library from the prose and tables of %s "
                       "(source digest %s); it is not the standard's own grammar. Generated by "
                       "schema/build.derived.py. Describes: %s." % (ID, SOURCE_DIGEST, s["title"]),
           "title": s["name"], "type": "object", "properties": props,
           "required": [f["name"] for f in s["fields"] if f["req"]],
           "additionalProperties": False}
    if s["defs"]:
        sch["$defs"] = s["defs"]
    sch.update(s["extra"])
    return sch


def bad_value(sc):
    """A value that violates `sc`, or None when none can be built."""
    if "const" in sc:
        return (not sc["const"]) if isinstance(sc["const"], bool) else "__wrong_const__"
    if "enum" in sc:
        return "__not_a_member__"
    t = sc.get("type")
    if t == "string":
        return 12345
    if t == "integer":
        return "1"
    if t == "boolean":
        return "true"
    if t == "array":
        return "not-an-array"
    if t == "object":
        return "not-an-object"
    return None


def cases_for(s):
    full = {f["name"]: copy.deepcopy(f["ex"]) for f in s["fields"]}
    out = [("accept", "every field present, example values", full)]
    optional = [f for f in s["fields"] if not f["req"]]
    if optional:
        out.append(("accept", "required fields only", copy.deepcopy(s["minimal"]) if s["minimal"] is not None else
                    {f["name"]: copy.deepcopy(f["ex"]) for f in s["fields"] if f["req"]}))
    for why, inst in s["accept"]:
        out.append(("accept", why, inst))
    if any(f["req"] for f in s["fields"]):
        out.append(("reject", "empty object (mandatory fields absent)", {}))
    for f in s["fields"]:
        if f["req"]:
            inst = copy.deepcopy(full)
            del inst[f["name"]]
            out.append(("reject", "mandatory field '%s' omitted" % f["name"], inst))
        bv = bad_value(f["sch"])
        if bv is not None:
            inst = copy.deepcopy(full)
            inst[f["name"]] = bv
            out.append(("reject", "field '%s' given a value its schema forbids" % f["name"], inst))
        if f["sch"].get("pattern"):
            inst = copy.deepcopy(full)
            inst[f["name"]] = "not matching"
            out.append(("reject", "field '%s' breaks its pattern" % f["name"], inst))
        if "minimum" in f["sch"] and "enum" not in f["sch"]:
            inst = copy.deepcopy(full)
            inst[f["name"]] = f["sch"]["minimum"] - 1
            out.append(("reject", "field '%s' below its minimum" % f["name"], inst))
        if "maximum" in f["sch"] and "enum" not in f["sch"]:
            inst = copy.deepcopy(full)
            inst[f["name"]] = f["sch"]["maximum"] + 1
            out.append(("reject", "field '%s' above its maximum" % f["name"], inst))
        if f["sch"].get("minItems"):
            inst = copy.deepcopy(full)
            inst[f["name"]] = []
            out.append(("reject", "field '%s' an empty array" % f["name"], inst))
        if f["sch"].get("type") == "string" and f["sch"].get("minLength"):
            inst = copy.deepcopy(full)
            inst[f["name"]] = ""
            out.append(("reject", "field '%s' an empty string" % f["name"], inst))
    inst = copy.deepcopy(full)
    inst["unlisted_field"] = 1
    out.append(("reject", "a field the structure does not define (additionalProperties false)", inst))
    for why, inst in s["reject"]:
        out.append(("reject", why, inst))
    return out


# ---- YAML out (block style; both readers must agree on it) -------------------
def scalar(x):
    if isinstance(x, bool):
        return "true" if x else "false"
    if isinstance(x, int):
        return str(x)
    if isinstance(x, str):
        if "\n" in x:
            raise SystemExit("newline in scalar: " + x[:60])
        return "'" + x.replace("'", "''") + "'"
    raise SystemExit("scalar of type %s" % type(x))


def y(v, ind=0):
    pad = " " * ind
    out = []
    if isinstance(v, dict):
        for k, x in v.items():
            if isinstance(x, (dict, list)):
                if not x:
                    raise SystemExit("empty container under " + k)
                out.append("%s%s:" % (pad, k))
                out.append(y(x, ind + 2))
            else:
                out.append("%s%s: %s" % (pad, k, scalar(x)))
    else:
        for x in v:
            if isinstance(x, dict):
                ls = y(x, ind + 2).split("\n")
                ls[0] = pad + "- " + ls[0][ind + 2:]
                out.extend(ls)
            elif isinstance(x, list):
                raise SystemExit("nested list")
            else:
                out.append("%s- %s" % (pad, scalar(x)))
    return "\n".join(out)


def norm(v):
    if isinstance(v, dict):
        return {k: norm(x) for k, x in v.items()}
    if isinstance(v, list):
        return [norm(x) for x in v]
    if isinstance(v, bool):
        return "true" if v else "false"   # _yaml.py reads bare booleans as text, _record_yaml.py as bool
    return str(v)


def message_of(s):
    m = {"name": s["name"], "locator": s["locator"], "kind": "derived structure",
         "encoding": "JSON object; derived_schema validates it"}
    m["derived_schema"] = "schema/%s.derived.schema.json" % s["name"]
    m["title"] = s["title"]
    m.update(Q(*s["lines"]))
    if s["caption"]:
        m["caption"] = Q(*s["caption"])
    for k, ln in s["also"].items():
        m[k] = Q(*ln)
    m["constrained_by"] = list(s["cons"])
    flds = []
    for f in s["fields"]:
        d = {"name": f["name"], "type": describe(f["sch"]), "required": f["req"],
             "level": f["lvl"], "constrained_by": list(f["cons"] or s["cons"])}
        if f["lines"]:
            d.update(Q(*f["lines"]))
        if f["reason"]:
            d["inferred_reason"] = f["reason"]
        if f["note"]:
            d["note"] = f["note"]
        flds.append(d)
    m["fields"] = flds
    if s["layout"]:
        m["layout"] = s["layout"]
    if s["note"]:
        m["note"] = s["note"]
    return m


def md(a, b=None):
    b = b or a
    return "<!-- q L%d%s -->\n> %s\n" % (a, ("-%d" % b) if b != a else "", span(a, b))


def dump_json(path, obj):
    path.write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n")


def finish(structs, messages_head, tag, schema_readme, examples_readme, extra_examples=None,
           extra_check=None, messages_tail=None):
    """Write every artifact, then verify every accept/reject case. Exits 1 on
    any surprise. Reports how many cases it EXAMINED."""
    (DIST / "schema").mkdir(exist_ok=True)
    (DIST / "examples").mkdir(exist_ok=True)
    validators, allcases, bad = {}, [], []
    for s in structs:
        sch = build_schema(s)
        jsonschema.Draft202012Validator.check_schema(sch)
        dump_json(DIST / "schema" / ("%s.derived.schema.json" % s["name"]), sch)
        v = jsonschema.Draft202012Validator(sch)
        validators[s["name"]] = v
        for exp, why, inst in cases_for(s):
            ok = not list(v.iter_errors(inst))
            allcases.append({"schema": s["name"], "expect": exp, "why": why, "instance": inst})
            if (exp == "accept") != ok:
                bad.append("%s: %s expected %s, validator said %s" % (s["name"], why, exp,
                           "accept" if ok else "reject"))
    na = sum(1 for c in allcases if c["expect"] == "accept")
    nr = len(allcases) - na
    dump_json(DIST / "examples" / ("%s-cases.derived.json" % tag), {
        "_comment": "DERIVED, not verbatim. Instances each derived schema in ../schema MUST accept "
                    "(expect accept) or MUST REJECT (expect reject); written and re-checked by "
                    "../schema/build.derived.py with the jsonschema library. These are this library's "
                    "cases, not the standard's.", "cases": allcases})
    extras = extra_examples(validators) if extra_examples else {}
    if extra_check:
        bad.extend(extra_check(validators))
    # messages.yaml
    msgs = [message_of(s) for s in structs]
    body = messages_head + "\nmessages:\n" + y(msgs, 2)
    if messages_tail:
        body += "\n" + messages_tail
    body += "\n"
    (DIST / "messages.yaml").write_text(body)
    a = yaml_a(body)
    b = yaml_b.load_yaml(DIST / "messages.yaml")
    want = norm(json.loads(json.dumps({"messages": msgs})))["messages"]
    for nm, got in (("_yaml", a), ("_record_yaml", b)):
        if norm(got["messages"]) != want:
            bad.append("messages.yaml: %s reads different values than were written" % nm)
    (DIST / "schema" / "README.md").write_text(schema_readme(structs, na, nr))
    (DIST / "examples" / "README.md").write_text(examples_readme(structs, na, nr, extras))
    # requirement ids actually cited, read back
    cited = set()
    for m in msgs:
        cited.update(m["constrained_by"])
        for f in m["fields"]:
            cited.update(f["constrained_by"])
    unused = sorted(set(USED) - cited)
    if unused:
        bad.append("resolved but never cited: %s" % unused)
    print("cited constrained_by ids (%d distinct), read back from requirements.yaml:" % len(cited))
    for k in sorted(cited):
        loc, sl, tx = USED[k]
        print("  %s  %s L%s  %s" % (k, loc, sl, tx[:92]))
    cb = sum(len(m["constrained_by"]) + sum(len(f["constrained_by"]) for f in m["fields"]) for m in msgs)
    print("structures=%d fields=%d cite_sites=%d distinct_ids=%d cases=%d (accept %d, reject %d) "
          "unexpected=%d" % (len(structs), sum(len(s["fields"]) for s in structs), cb,
                             len(cited), len(allcases), na, nr, len(bad)))
    for b_ in bad:
        print("UNEXPECTED: " + b_)
    sys.exit(1 if bad else 0)


FRONT = ("---\nrecord: %s\nkind: %s\ntitle: \"%s — %s\"\nextracted: \"2026-11-15\"\n"
         "reviewed_by: \"\"\n---\n\n")


def schema_table(structs):
    rows = ["| file | locator | what it validates | source lines |", "|---|---|---|---|"]
    for s in structs:
        rows.append("| `%s.derived.schema.json` | %s | %s | L%s |" % (
            s["name"], s["locator"], s["title"], Q(*s["lines"])["source_lines"]))
    return "\n".join(rows)


def generic_schema_readme(structs, na, nr, intro, notes):
    return (FRONT % (ID, "schema", ID, "schemas") + "# Schemas\n\n" + intro.strip() + "\n\n"
            "## Derived (written by this library)\n\n"
            "Every file here is **derived**: `%s` ships no CDDL, ASN.1 or JSON Schema of its own, so each "
            "is a JSON Schema (draft 2020-12, `additionalProperties: false`, `$id: urn:library:%s:<Name>`) "
            "written from the prose or tables the Source lines column names. Nothing here is verbatim.\n\n"
            % (ID, ID) + schema_table(structs) + "\n\n"
            "## Rebuild and self-check\n\n"
            "`build.derived.py` writes every `*.derived.schema.json` here, `../messages.yaml` and "
            "`../examples/*.derived.json`. It resolves every `constrained_by` id from "
            "`../requirements.yaml` by script (it raises on 0 or more than 1 match), writes every "
            "quotation from the cached source, then validates every case in "
            "`../examples/*-cases.derived.json` with the `jsonschema` package "
            "(`Draft202012Validator`) and exits 1 on any surprise. Run it with a Python that has "
            "`jsonschema` installed, from the repository root:\n\n"
            "```sh\npython3 records/%s/%s/distilled/schema/build.derived.py\n```\n\n"
            "Last run: %d structures, %d cases (%d accept, %d reject), 0 unexpected.\n\n"
            "Every structure with a mandatory field is tested with the empty object and with each "
            "mandatory field omitted in turn (each must be rejected), with a wrong-typed value for each "
            "field, and with an undefined extra field; a field the source makes a `shall` boolean is "
            "`const: true`, so `false` is rejected.\n\n" % (
                REC.parent.name, ID, len(structs), na + nr, na, nr) + notes.strip() + "\n")

# ---- registry reader: a list of citations printed in a PDF, cut into rows by script ----
URLTOK = re.compile(r"^https?://")


def tok_lines(a, b):
    """(token, line) over lines a..b of the cleaned source; a line made only of
    digits would be a page number the reader left in (the pass-1 reader did;
    none is left since 63d708e), so it is skipped."""
    out = []
    for ln, l in cleaned[a - 1:b]:
        if l is None or not l.strip() or re.fullmatch(r"\d+", l.strip()):
            continue
        out.extend((t, ln) for t in l.split())
    return out


def split_entries(a, b):
    """Rows of a citation list: each ends at its URL (a URL cut after a hyphen
    ends one token later)."""
    entries, cur, need = [], [], False
    for t, ln in tok_lines(a, b):
        cur.append((t, ln))
        if need:
            entries.append(cur)
            cur, need = [], False
        elif URLTOK.match(t):
            if t.endswith("-"):
                need = True
            else:
                entries.append(cur)
                cur = []
    if cur or need:
        raise SystemExit("citation list %d-%d ends inside an entry: %s" % (a, b, st.join(cur)[:80]))
    return entries


CITE = re.compile(
    r"^(?P<authors>.+?) \((?P<year>\d{4})\) (?P<title>.+?)\.? "
    r"\((?P<publisher>(?:U\.S\. Department of Commerce|National Institute of Standards and Technology|IEEE)[^)]*)\)"
    r"[.,]?\s*(?P<series>.*?)\s*(?:Available at )?(?P<url>https?://\S+)$")


def parse_cite(text):
    m = CITE.match(text)
    if not m:
        raise SystemExit("citation does not parse: " + text[:120])
    d = m.groupdict()
    ref = {"authors": d["authors"], "year": int(d["year"]), "title": d["title"],
           "publisher": d["publisher"], "url": d["url"]}
    series = d["series"].strip(" .,")
    if series:
        ref["series"] = series
    dm = re.search(r"\((SP|FIPS)\)\s+([0-9][0-9A-Za-z\-]*)", series)
    if dm:
        ref["designation"] = "%s %s" % (dm.group(1), dm.group(2))
    rv = re.search(r"Rev\. (\d+)", series)
    if rv:
        ref["revision"] = int(rv.group(1))
    return ref


def functions_of(heading):
    """Function names a sub-heading lists: the last parenthesised list, a lone
    abbreviation, the list after a colon, or the whole heading."""
    if heading is None:
        return None
    pars = re.findall(r"\(([^()]*)\)", heading)
    if pars and "," in pars[-1]:
        return [x.strip() for x in re.split(r",\s*(?:and\s+)?|\s+and\s+", pars[-1]) if x.strip()]
    if pars:
        return [pars[-1].strip()]
    if ":" in heading:
        return [x.strip() for x in re.split(r",\s*(?:and\s+)?", heading.split(":", 1)[1]) if x.strip()]
    return [heading.strip()]


def read_registry(layout, region, ordinal):
    """Rows of the whole list. `layout` is the document's own order of
    headings, citation runs, bullets and notes (line numbers into the cleaned
    source); `region` = (first, last) lines for the coverage count."""
    rows, sec, sec_title, group = [], None, None, None
    for item in layout:
        kind, a = item[0], item[1]
        b = item[2] if len(item) > 2 else a
        if kind == "sec":
            m = re.match(r"^(\d+(?:\.\d+)+)\s+(.*)$", span(a, b))
            sec, sec_title, group = m.group(1), m.group(2), None
        elif kind == "sub":
            group = span(a, b)
        elif kind == "refs":
            for toks in split_entries(a, b):
                text = st.join(toks)
                o = None
                q = Q(toks[0][1], toks[-1][1])
                if ordinal:
                    om = re.match(r"^(\d+)\.\s+(.*)$", text)
                    if om:   # 6.2.1 has one unnumbered row
                        o, text = int(om.group(1)), om.group(2)
                row = {"section": sec, "section_title": sec_title}
                if group:
                    row["group"] = group
                    row["functions"] = functions_of(group)
                if o is not None:
                    row["ordinal"] = o
                row["reference"] = parse_cite(text)
                row["source_lines"], row["quote"] = q["source_lines"], q["quote"]
                rows.append(row)
        elif kind in ("bullet", "note"):
            if kind == "note" and not rows:
                raise SystemExit("note with no entry")
            q = Q(a, b)
            if not rows or (rows[-1]["section"] != sec) or (kind == "note" and group and rows[-1].get("group") != group):
                # a sub-heading that has no citation of its own (SKIPJACK): the note makes its row
                rows.append({"section": sec, "section_title": sec_title, "group": group,
                             "functions": functions_of(group), "notes": [q],
                             "source_lines": q["source_lines"], "quote": q["quote"]})
                last = rows[-1]
            else:
                last = rows[-1]
                last.setdefault("notes", []).append(q)
            rs = re.match(r"^[●•]\s*(?:Relevant Sections|Sections relevant to this Annex):\s*(.*?)\.$", q["quote"])
            if rs:
                last["relevant_sections"] = rs.group(1)
            ur = re.search(r"is approved for (\w+ only)", q["quote"])
            if ur:
                last["usage_restriction"] = ur.group(1)
    nurl = sum(1 for t, _ in tok_lines(*region) if URLTOK.match(t))
    nref = sum(1 for r in rows if "reference" in r)
    if nurl != nref:
        raise SystemExit("coverage: %d URLs in lines %d-%d but %d reference rows" % (nurl, region[0], region[1], nref))
    for i, r in enumerate(rows, 1):
        r["id"] = "%s-entry-%02d" % (ID, i)
    return rows, nurl


def registry_schema_fields(ordinal):
    ref = {"type": "object", "additionalProperties": False,
           "required": ["authors", "year", "title", "publisher", "url"],
           "properties": {"authors": S(), "year": I(1990, 2100), "title": S(), "publisher": S(),
                          "series": S(), "designation": S(pattern=r"^(SP|FIPS) [0-9]"),
                          "revision": I(1), "url": S(pattern=r"^https?://\S+$")}}
    return ref


# ===== record-specific spec =====
# uses: registry
# The list binds through the scope statements (§1, §5.1, §6.1) and the
# closed-list reading; every row of §6.2 is its own stated, keyword-less entry.
R_SCOPE = [R(r"^This document specifies the Cryptographic Module Validation Program \(CMVP\) approved sensitive", "§1"),
           R(r"^Section 6 of this document replaces the approved sensitive security parameter", "§5.1"),
           R(r"^This document identifies CMVP-approved sensitive security parameter generation", "§6.1"),
           R(r"^It precludes the use of all other sensitive security parameter", "§6.1"),
           R(r"^A module that generates or establishes an SSP by a method outside items 1 to 12", "§6.1")]
R_RELSEC = RL(315, "Sections relevant to this Annex")
R_DSA = RL(323, "DSA, RSA, and ECDSA")
R_DSSNOTE = RL(331, "only used to define the domain parameters")

LAYOUT = [("sec", 309), ("refs", 311, 313), ("bullet", 315),
          ("sec", 317), ("refs", 319, 321), ("bullet", 323), ("note", 331, 333), ("refs", 335, 393)]
ROWS, NURL = read_registry(LAYOUT, (309, 393), True)
REF_IDS, ROWREQ = [], []
for r in ROWS:
    a = int(r["source_lines"].split("-")[0])
    ids = [RL(a)]
    REF_IDS.append(ids[0])
    for n in r.get("notes", []):
        ids.append(RL(int(n["source_lines"].split("-")[0])))
    r["requirements"] = ids
    ROWREQ.extend(ids)
ROW_ENTRIES = [x["id"] for x in REQS if x.get("row")]
_missing = sorted(set(ROW_ENTRIES) - set(ROWREQ))
_dups = sorted({i for i in ROWREQ if ROWREQ.count(i) > 1})
if _missing or _dups:
    raise SystemExit("registry/requirements join: missing %s, carried twice %s" % (_missing, _dups))

REF = registry_schema_fields(True)
NOTE = {"type": "object", "additionalProperties": False, "required": ["source_lines", "quote"],
        "properties": {"source_lines": S(pattern=r"^\d+(-\d+)?$"), "quote": S()}}
REASON = ("SP 800-140D lists approved SSP generation and establishment methods as keyword-less rows (citations, two "
          "bullets and a note), each a stated entry in requirements.yaml; the row fields name the parts of a printed "
          "row and are this library's reading of it")
BASE = {"id": "nist-sp-800-140d-entry-02", "section": "6.2.2", "section_title": "Key Establishment Techniques",
        "source_lines": "335-338", "quote": "q"}
REFOK = {"authors": "Barker EB", "year": 2018, "title": "t", "publisher": "p", "url": "https://doi.org/10.6028/NIST.SP.800-56Ar3"}
structs = [
    ST("ApprovedSspMethodReference", "one row of the CMVP approved sensitive security parameter generation and establishment methods list: the document that specifies a method",
       "§6.2", (303, 305), R_SCOPE, [
        F("id", S(pattern=r"^nist-sp-800-140d-entry-\d{2}$"), "inferred", "nist-sp-800-140d-entry-02", reason=REASON,
          note="this library's row key; the source numbers only the 6.2.2 rows"),
        F("section", S(pattern=r"^6\.2\.[12]$"), "inferred", "6.2.2", reason=REASON, note="the sub-section heading the row sits under (6.2.1 Transitions or 6.2.2 Key Establishment Techniques)"),
        F("section_title", S(), "inferred", "Key Establishment Techniques", reason=REASON),
        F("ordinal", I(1, 12), "stated", 2, req=False, lines=(335, 335), cons=REF_IDS[1:],
          note="the source's own number of a 6.2.2 row (1 to 12); 6.2.1 has one unnumbered row"),
        F("reference", {"$ref": "#/$defs/Reference"}, "inferred", REFOK, reason=REASON,
          cons=REF_IDS, note="the citation as printed, parsed by script"),
        F("relevant_sections", S(), "stated", "1, 5, 6, 7, and 8", req=False, lines=(315, 315), cons=[R_RELSEC],
          note="the 'Sections relevant to this Annex' bullet under the 6.2.1 citation"),
        F("notes", A({"$ref": "#/$defs/Note"}, lo=1), "inferred", [{"source_lines": "323", "quote": "x"}], req=False, reason=REASON, cons=[R_RELSEC, R_DSA, R_DSSNOTE],
          note="bullets and NOTEs that follow a row, each with its source lines and the words, written by script (row 1 has the 'DSA, RSA, and ECDSA' bullet and the note that the Digital Signature Standard is used only for domain parameters and key-pair generation)"),
        F("source_lines", S(pattern=r"^\d+(-\d+)?$"), "inferred", "335-338", reason=REASON, note="lines of the cached rendering the row occupies"),
        F("quote", S(), "inferred", "x", reason=REASON, note="the row's words, written by script from those lines"),
        F("requirements", A(S(pattern=r"^nist-sp-800-140d#R-\d{4}$"), lo=1, uniq=True), "inferred", list(ROWS[1]["requirements"]), req=False, reason=REASON,
          note="the requirements.yaml entries this row is the machine form of (its citation, and its bullets or note), resolved by script from the row's lines")],
       also={"scope": (226, 228), "exclusivity": (303, 305)},
       defs={"Reference": REF, "Note": NOTE},
       minimal=dict(BASE, reference=REFOK),
       reject=[("a citation without its url", dict(BASE, reference={"authors": "a", "year": 2019, "title": "t", "publisher": "p"})),
               ("a citation whose url is not a url", dict(BASE, reference=dict(REFOK, url="doi:10.1"))),
               ("a row with no citation (every D row has one)", dict(BASE)),
               ("section 6.2.3, which the document does not have", dict(BASE, section="6.2.3", reference=REFOK)),
               ("ordinal 13: the source numbers 1 to 12", dict(BASE, ordinal=13, reference=REFOK))],
       layout="a JSON object per row of the list; rows are in ../examples/approved-methods.derived.json"),
]

HEAD = """# =====================================================================
# nist-sp-800-140d messages -- SP 800-140D replaces ISO/IEC 19790 Annex D and
# ISO/IEC 24759 6.16 with a LIST of approved SSP generation and establishment
# methods. The list is prose: 6.2.1 has one citation (SP 800-131A) and 6.2.2
# has twelve numbered citations. There is no message, wire format or state. So
# ONE derived structure: a row of the list. The rows are generated by script
# into examples/approved-methods.derived.json (%d rows, each with
# source_lines and the quote); they are NOT re-extracted by hand, and the
# requirements lane owns the rows as requirements.
#
# The list is CLOSED: the source says the document 'precludes the use of all
# other sensitive security parameter generation and establishment methods'
# (carried as the `exclusivity` quotation on the structure).
#
# Every row of section 6.2 is a stated, keyword-less entry of requirements.yaml
# (row:), and each registry row lists the entries it carries in `requirements`.
# constrained_by names the scope statements that make the list binding (1,
# 5.1, 6.1 and the closed-list reading) and, per field, the rows the field is
# read from.
#
# Written by schema/build.derived.py; ids resolved by script from requirements.yaml.
# source_digest: %s
# =====================================================================
record: nist-sp-800-140d
reviewed_by: ""
source_digest: '%s'
applicability: 'one derived structure (a row of the approved-methods list); no wire or document format'""" % (len(ROWS), SOURCE_DIGEST, SOURCE_DIGEST)


def sreadme(structs, na, nr):
    return generic_schema_readme(structs, na, nr,
        "SP 800-140D has no formal notation: its section 6.2 is a numbered list of citations. "
        "The one schema describes a row of that list.", """
Row cut: `build.derived.py` cuts section 6.2 into rows by script. A row ends at its URL (a URL split after a
hyphen across a page ends one token later, as for SP 800-56B Rev. 2, lines 343-349); the bullets and the note
under row 1 are attached by the document's own order (the layout table at the top of the spec). Coverage is
checked: the number of `https://` tokens in lines 309-393 equals the number of rows (%d each).

Rendering: row 3 prints its URL across a page break (lines 343-349); the reader joins it at the line-end
hyphen. Source: row 12's first author is printed %s (line 390) and row 5's %s (line 355); both are kept as printed.

Join: each row's `requirements` lists the requirements.yaml entries it is the machine form of (its citation, and
its bullets or note), resolved by script from the row's lines; the build refuses a row entry of section 6.2 that
no row carries, or one that two rows carry.
""" % (NURL, span(390).split()[1], span(355).split()[1]))


def extra_examples(validators):
    rows = []
    for r in ROWS:
        errs = list(validators["ApprovedSspMethodReference"].iter_errors(r))
        assert not errs, (r["id"], errs[0].message)
        a, _, b = r["source_lines"].partition("-")
        assert r["quote"] == span(int(a), int(b or a)), r["id"]
        rows.append(r)
    ords = [r.get("ordinal") for r in rows if "ordinal" in r]
    assert ords == list(range(1, 13)), ords
    dump_json(DIST / "examples" / "approved-methods.derived.json", {
        "_comment": "DERIVED, not verbatim. Section 6.2 of SP 800-140D cut into rows by ../schema/build.derived.py: "
                    "one object per citation, each with source_lines and the quote written from them. Every row "
                    "validates against ../schema/ApprovedSspMethodReference.derived.schema.json and the 6.2.2 rows "
                    "are numbered 1 to 12 in order. The requirements lane owns these rows as requirements; this "
                    "file is their machine form.",
        "count": len(rows), "rows": rows})
    return {"rows": len(rows)}


def ereadme(structs, na, nr, extras):
    return (FRONT % (ID, "examples", ID, "examples and test vectors") + "# Examples and test vectors\n\n"
            "**Finding: SP 800-140D contains no worked example, sample or test vector.** Its section 6.2 is the "
            "list itself, and 6.1 says what the list is:\n\n" + md(303, 305) + "\n## Fixtures\n\n"
            "| file | what it is | expected result |\n|---|---|---|\n"
            "| `approved-methods.derived.json` | the %d rows of section 6.2 (one per citation), each with `source_lines`, `quote`, and parsed fields | every row is accepted by `ApprovedSspMethodReference`; the 6.2.2 rows are numbered 1 to 12 in order |\n"
            "| `approved-methods-cases.derived.json` | this library's cases for that schema: %d cases, %d `accept` and %d `reject` | each case's `expect` |\n\n"
            "`../schema/build.derived.py` regenerates both and exits 1 on any difference. A check that every "
            "`https://` token of lines 309-393 landed in exactly one row examined %d tokens and %d rows.\n"
            % (extras["rows"], na + nr, na, nr, NURL, extras["rows"]))


finish(structs, HEAD, "approved-methods", sreadme, ereadme, extra_examples=extra_examples)
