#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library; nist-sp-800-140 ships no schema, so
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
SPLIT = [r for r in RQ["requirements"] if r.get("split_of")]
USED = {}


def R(pattern, locator=None, split=False):
    """The id of the ONE requirement whose text matches `pattern` (re.search
    over whitespace-collapsed text). 0 or >1 matches raise. split=True
    searches the split_of children instead of the top-level entries."""
    hit = [r for r in (SPLIT if split else REQS)
           if re.search(pattern, WS.sub(" ", str(r["text"])).strip())
           and (locator is None or r["locator"] == locator)]
    if len(hit) != 1:
        raise SystemExit("R(%r, %r): %d matches %s" % (pattern, locator, len(hit),
                         [h["id"] for h in hit]))
    r = hit[0]
    USED[r["id"]] = (r["locator"], r.get("source_lines", "(inferred)"), WS.sub(" ", str(r["text"])).strip())
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
    if isinstance(s, bool):
        return "nothing further" if not s else "any"
    if "prefixItems" in s:
        return "array of exactly %d positional objects (prefixItems), in fixed order" % len(s["prefixItems"])
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


# ===== record-specific spec =====
R1 = R(r"^Section 6 of this document specifies any modifications to the requirements for information", "§5.1")
R2 = R(r"^Modifications will follow a similar format as in ISO/IEC 24759", "§5.2")
AS_HW = R(r"^The cryptographic boundary of a hardware cryptographic module shall delimit")
AS_FW = R(r"^The cryptographic boundary of a firmware cryptographic module shall delimit")
AS_HY = R(r"^The cryptographic boundary of a hybrid cryptographic module shall:")
AS_MODE = R(r"^An approved mode of operation shall be defined")
AS_OUT = EV("AS03.07"); AS_AUTH = EV("AS04.44"); AS_OS = EV("AS06.11"); AS_HARD = EV("AS07.26")
AS_EFP = R(r"^If the temperature or voltage falls outside of the cryptographic module")
AS_SPLIT = EV("AS09.23"); AS_Z28 = R(r"^A module shall provide methods to zeroise all unprotected SSPs")
AS_Z29 = R(r"^A zeroised SSP shall not be retrievable or reusable"); AS_Z30 = R(r"^The cryptographic module shall perform the zeroisation of unprotected SSPs")
AS_FN = R(r"^Documentation shall specify the functional testing performed"); AS_GUIDE = EV("AS11.38")
AS_FBK = R(r"^Feedback of authentication data to an operator shall be obscured")
VE = {k: EV(k) for k in ("VE02.15.05", "VE02.15.06", "VE02.17.04", "VE02.17.05", "VE02.18.01", "VE02.20.03", "VE02.20.04",
                         "VE03.07.03", "VE03.07.04", "VE03.07.05", "VE04.44.01", "VE04.54.01", "VE04.54.02", "VE06.11.01",
                         "VE07.26.01", "VE07.26.02", "VE07.77.01", "VE07.77.02", "VE07.81.01", "VE07.81.02", "VE09.23.01",
                         "VE09.23.02", "VE09.28.01", "VE09.28.03", "VE09.29.01", "VE09.30.01", "VE11.29.01", "VE11.38.03")}
TE = {k: EV(k) for k in ("TE02.18.01", "TE02.20.04", "TE09.23.01")}
R_PROT = R(r"^Protection shall include the implementation of mechanisms")
R_EFP_DOC = R(r"^Documentation shall state which of these approaches was chosen.*of the EFP")
R_EFT_DOC = R(r"^Documentation shall state which of these approaches was chosen.*of the EFT")
R_Z30B = R(r"^b\) Restrictions when plaintext SSPs can be zeroised")
R_CVE2 = R(r"^- or, for any CVE")
# pass 2 (verify): the section 6 response format, the heading entries, list
# items, split children and the TEs a field quotes are entries now; cite them
# rather than the nearest keyword sentence
R_TE_YN = R(r"^In responding to test evidence \(TE\), a yes/no answer", "§6")
R_TE_INFO = R(r"^CMVP requires the following information when responding", "§6")
R_TE_DOC = R(r"^Documentation: Reference/cite", "§6")
R_TE_OPS = R(r"^Operational Testing: Describe the test method", "§6")
R_TE_VER = R(r"^Verify or Verify by Inspection: Describe", "§6")
R_AS15H = EV("AS02.15")
R_LEVELS_RULE = R(r"^An assertion applies to a module only at the security levels", "§6")
R_SEQ = R(r"^For additions to test requirements, new Test Evidence", "§5.2", split=True)
R_VEND = R(r"^the requirements for information that vendors shall provide", "§5.1", split=True)
R_TEST = R(r"^the requirements for testing that shall be used by testing laboratories", "§5.1", split=True)
R_Z28I = [R(r"^a\. Zeroisation techniques$", "§6.9"),
          R(r"^Restrictions when unprotected SSPs can be zeroised$", "§6.9", split=True),
          R(r"^c\. Unprotected SSPs that are zeroised$", "§6.9"),
          R(r"^d\. Unprotected SSPs that are not zeroised", "§6.9"),
          R(r"^e\. Rationale explaining how the zeroisation technique", "§6.9")]
R_Z30I = [R(r"^a\) Zeroisation techniques$", "§6.9"), R_Z30B,
          R(r"^c\) Plaintext SSPs that are zeroised$", "§6.9"),
          R(r"^d\) Plaintext SSPs that are not zeroised", "§6.9"),
          R(r"^e\) Rationale explaining how the zeroisation technique", "§6.9")]
R_EFP_TE = EV("TE07.77.04")
R_EFT_TE = EV("TE07.81.03")
R_EFP_EITHER = R(r"^If a condition is determined to be outside of the module.s normal operating range, the protection circuitry shall either", "§6.7")
R_EFT_EITHER = R(r"^The module shall either:$", "§6.7")
R_EFP_AB = [R(r"^a\) shutdown the module, or$", "§6.7"), R(r"^b\) zeroise all plaintext unprotected SSPs$", "§6.7")]
R_EFT_ABC = [R(r"^a\) continue to operate normally, or$", "§6.7"), R(r"^b\) shutdown, or$", "§6.7"),
             R(r"^c\) zeroise all plaintext unprotected SSPs\.$", "§6.7")]
R_CVE1 = R(r"^- provide assurance that they are not security relevant;", "§6.11")


def short(i):
    return i.split("#")[1]


def cut(a, b, start, end):
    """A verbatim sub-span of lines a..b, cut by script, never typed."""
    t = span(a, b)
    i = t.index(start)
    return t[i:t.index(end, i) + len(end)]

# ---- the assertion / evidence index, read from the source by script ----
IDRE = re.compile(r"^(AS|VE|TE)(\d\d\.\d\d)(\.\d\d)?(?=:|\s+(?:The|For|If|Documentation)\b)")
ASRE = re.compile(r"^AS\d\d\.\d\d:\s*\((.*?)\s+[\u2013\u2014-]+\s+Levels?\s+([^)]*)\)")
ASSERT, EVID, area, cur = [], [], None, None
for ln, l in cleaned[321 - 1:1064]:
    if l is None:
        continue
    t = l.strip()
    h = re.match(r"^6\.(\d+)\s+([A-Z][^.]{2,60})$", t)
    if h:
        area = h.group(2)
        continue
    m = IDRE.match(t)
    if not m:
        continue
    q = Q(ln)
    if m.group(1) == "AS":
        am = ASRE.match(t)
        assert am, t
        cur = "AS" + m.group(2)
        ASSERT.append({"assertion_id": cur, "security_area": area, "title": am.group(1),
                       "levels": [int(x) for x in re.findall(r"\d", am.group(2))], "vendor_evidence": [], "test_evidence": [],
                       "source_lines": q["source_lines"]})
    else:
        eid = m.group(1) + m.group(2) + m.group(3)
        EVID.append({"evidence_id": eid, "kind": m.group(1), "assertion_id": cur,
                     "responsible": "vendor" if m.group(1) == "VE" else "tester", "source_lines": q["source_lines"]})
        ASSERT[-1]["vendor_evidence" if m.group(1) == "VE" else "test_evidence"].append(eid)
MISPLACED = [e["evidence_id"] for e in EVID if e["evidence_id"][2:7] != e["assertion_id"][2:]]
assert len(ASSERT) == 22 and len(EVID) == 76, (len(ASSERT), len(EVID))

IDS = S(pattern=r"^AS\d{2}\.\d{2}$")
VEID = S(pattern=r"^VE\d{2}\.\d{2}\.\d{2}$")
TEID = S(pattern=r"^TE\d{2}\.\d{2}\.\d{2}$")
LIM = {"type": "object", "additionalProperties": False, "required": ["a"], "properties": {"a": S()}}
TXT = "text"
NOTE_RESP = ("a response to a Test Evidence item; section 6 prescribes it in keyword-less sentences ('%s'; '%s'), entries %s and %s"
             % (cut(298, 298, "a yes/no", "assurance"), cut(299, 300, "CMVP requires", "information"), short(R_TE_YN), short(R_TE_INFO)))


def vef(name, ex, ve, note, sch=None, req=True, lvl="shall", cons=None):
    return F(name, sch or S(), lvl, ex, req=req, cons=cons or [VE[ve]], note=note)


structs = [
    ST("Assertion", "one assertion of ISO/IEC 24759 6.x as SP 800-140 modifies it: its id, area, levels and the evidence items under it",
       "§6", (333, 334), [R1, R2], [
        F("assertion_id", IDS, "stated", "AS02.15", lines=(331, 331), cons=[R2, R_AS15H]),
        F("security_area", S(), "stated", "Cryptographic module specification", lines=(329, 329), cons=[R1]),
        F("title", S(), "stated", "Specification", lines=(331, 331), cons=[R_AS15H]),
        F("levels", A(I(1, 4), lo=1, uniq=True), "stated", [1, 2, 3, 4], lines=(331, 331), cons=[R_AS15H, R_LEVELS_RULE], note="the 'Levels' list printed beside the assertion id"),
        F("vendor_evidence", A(VEID, uniq=True), "inferred", ["VE02.15.05", "VE02.15.06"], reason="items are grouped under their assertion by the Required Vendor Information heading; no sentence states the grouping", cons=[R2], note="VE items listed by increasing sequence number; may be empty (an assertion with no VE)"),
        F("test_evidence", A(TEID, uniq=True), "inferred", ["TE02.15.10"], reason="items are grouped under their assertion by the Required Test Procedures heading; no sentence states the grouping", cons=[R2], note="TE items; may be empty ('This assertion is not separately tested')"),
        F("source_lines", S(pattern=r"^\d+(-\d+)?$"), "inferred", "331", reason="provenance, added by this library", cons=[R2])],
       layout="one JSON object per assertion; the index of all %d assertions is examples/assertion-index.derived.json" % len(ASSERT)),
    ST("EvidenceItem", "one Vendor Evidence or Test Evidence item",
       "§5.2", (290, 293), [R2, R_SEQ, R1], [
        F("evidence_id", S(pattern=r"^(VE|TE)\d{2}\.\d{2}\.\d{2}$"), "stated", "VE02.15.05", lines=(290, 293), cons=[R_SEQ], note="new items are '%s' (the last two digits); strict increase is not checked by the schema" % cut(291, 292, "listed by", "number.\u201d")),
        F("kind", E("VE", "TE"), "stated", "VE", lines=(290, 293), cons=[R_SEQ]),
        F("assertion_id", IDS, "inferred", "AS02.15", reason="the id prefix ties an item to its assertion in every item of the source; the source states no rule", cons=[R2]),
        F("responsible", E("vendor", "tester"), "inferred", "vendor", reason="VE items say 'the vendor shall', TE items 'the tester shall' throughout; no sentence states the mapping", cons=[R_VEND, R_TEST]),
        F("source_lines", S(pattern=r"^\d+(-\d+)?$"), "inferred", "349", req=False, reason="provenance, added by this library", cons=[R2])],
       extra={"allOf": [
           {"if": {"properties": {"kind": {"const": "VE"}}, "required": ["kind"]},
            "then": {"properties": {"evidence_id": {"pattern": "^VE"}, "responsible": {"const": "vendor"}}}},
           {"if": {"properties": {"kind": {"const": "TE"}}, "required": ["kind"]},
            "then": {"properties": {"evidence_id": {"pattern": "^TE"}, "responsible": {"const": "tester"}}}}]},
       reject=[("kind VE with a TE id", {"evidence_id": "TE02.15.10", "kind": "VE", "assertion_id": "AS02.15", "responsible": "vendor"}),
               ("a TE item assigned to the vendor", {"evidence_id": "TE02.15.10", "kind": "TE", "assertion_id": "AS02.15", "responsible": "vendor"})],
       layout="one JSON object per item; examples/evidence-index.derived.json"),
    ST("TestEvidenceResponse", "a CSTL's response to one Test Evidence item (documentation, operational testing, verify / verify by inspection)",
       "§6", (298, 319), [R1, R_TE_YN, R_TE_INFO], [
        F("te_id", S(pattern=r"^TE\d{2}\.\d{2}\.\d{2}$"), "stated", "TE02.15.10", lines=(298, 300), cons=[R_TE_YN, R_TE_INFO], note=NOTE_RESP),
        F("response_type", E("documentation", "operational_testing", "verify", "verify_by_inspection"), "stated", "documentation", lines=(299, 300), cons=[R_TE_INFO]),
        F("vendor_documentation_cited", A(S(), lo=1), "stated", ["Functional specification s3.2"], req=False, lines=(304, 305), cons=[R_TE_DOC], note="documentation: 'Reference/cite the applicable vendor documentation'"),
        F("documentation_summary", S(), "stated", "summary per the TE", req=False, lines=(304, 305), cons=[R_TE_DOC], note="documentation: 'summarize the contents per the TE'"),
        F("test_method_and_tools", S(), "stated", "tool X", req=False, lines=(312, 314), cons=[R_TE_OPS], note="operational testing: 'Describe the test method and tools'"),
        F("results_summary", S(), "stated", "passed", req=False, lines=(312, 314), cons=[R_TE_OPS], note="operational testing: 'summarize the results, per the TE'"),
        F("test_or_inspection_method", S(), "stated", "inspection of block diagram", req=False, lines=(316, 319), cons=[R_TE_VER], note="verify / verify by inspection: 'Describe the test or inspection method used'"),
        F("detailed_results", S(), "stated", "all interconnections labelled", req=False, lines=(316, 319), cons=[R_TE_VER], note="verify / verify by inspection: 'provide detailed results of the test or inspection'")],
       extra={"allOf": [
           {"if": {"properties": {"response_type": {"const": "documentation"}}, "required": ["response_type"]}, "then": {"required": ["vendor_documentation_cited", "documentation_summary"]}},
           {"if": {"properties": {"response_type": {"const": "operational_testing"}}, "required": ["response_type"]}, "then": {"required": ["test_method_and_tools", "results_summary"]}},
           {"if": {"properties": {"response_type": {"enum": ["verify", "verify_by_inspection"]}}, "required": ["response_type"]}, "then": {"required": ["test_or_inspection_method", "detailed_results"]}}]},
       minimal={"te_id": "TE02.15.10", "response_type": "documentation", "vendor_documentation_cited": ["doc"], "documentation_summary": "s"},
       accept=[("operational testing", {"te_id": "TE09.28.02", "response_type": "operational_testing", "test_method_and_tools": "m", "results_summary": "r"}),
               ("verify by inspection", {"te_id": "TE02.15.12", "response_type": "verify_by_inspection", "test_or_inspection_method": "m", "detailed_results": "d"})],
       reject=[("a bare yes/no answer", {"te_id": "TE02.15.10", "response_type": "documentation", "answer": "yes"}),
               ("documentation response without a summary", {"te_id": "TE02.15.10", "response_type": "documentation", "vendor_documentation_cited": ["doc"]}),
               ("operational testing without the results", {"te_id": "TE09.28.02", "response_type": "operational_testing", "test_method_and_tools": "m"}),
               ("verify without detailed results", {"te_id": "TE02.15.12", "response_type": "verify", "test_or_inspection_method": "m"})],
       also={"required_information": (299, 300)}, layout="one JSON object per response"),
    ST("ProcessorEvidence", "VE02.15.05/06 and VE02.17.04/05: what the vendor identifies for each processor of a hardware or firmware module",
       "§6.2", (349, 354), [AS_HW, AS_FW, VE["VE02.15.05"], VE["VE02.15.06"], VE["VE02.17.04"], VE["VE02.17.05"]], [
        F("module_kind", E("hardware", "firmware"), "stated", "hardware", lines=(349, 351), cons=[VE["VE02.15.05"], VE["VE02.17.04"]], note="firmware: the processors are those 'in the computing platform of the operational environment bound to the firmware module'"),
        F("processor", S(), "shall", "CPU0", cons=[VE["VE02.15.05"]]),
        F("software_or_firmware_by_major_service", A(S(), lo=1), "shall", ["boot loader: self-tests"], cons=[VE["VE02.15.05"], VE["VE02.17.04"]]),
        F("memory_devices_with_executable_code_and_data", A(S(), lo=1), "shall", ["flash 0"], cons=[VE["VE02.15.05"], VE["VE02.17.04"]]),
        F("interfaced_hardware", A(S(), lo=1), "shall", ["UART"], cons=[VE["VE02.15.06"], VE["VE02.17.05"]], note="'any hardware with which the processor interfaces'; an empty list is rejected, so a vendor with none must say so in the text")],
       layout="one JSON object per processor"),
    ST("HybridModuleDesignation", "VE02.18.01: the module is identified as a Hybrid Software Module or a Hybrid Firmware Module",
       "§6.2", (466, 467), [AS_HY, VE["VE02.18.01"], TE["TE02.18.01"]], [
        F("designation", E("Hybrid Software Module", "Hybrid Firmware Module"), "shall", "Hybrid Software Module", cons=[VE["VE02.18.01"]], note="'identified in the vendor documentation as either a Hybrid Software Module or a Hybrid Firmware Module'"),
        F("identified_in_vendor_documentation", TRUE, "shall", True, cons=[VE["VE02.18.01"], TE["TE02.18.01"]])],
       layout="one JSON object"),
    ST("VendorAffirmedSecurityMethod", "VE02.20.03/04: one vendor-affirmed security method, listed in the non-proprietary security policy",
       "§6.2", (505, 508), [AS_MODE, VE["VE02.20.03"], VE["VE02.20.04"], TE["TE02.20.04"]], [
        F("method", S(), "shall", "vendor-affirmed CKG", cons=[VE["VE02.20.03"]]),
        F("conforms_to", S(), "inferred", "SP 800-133 Rev. 2", cons=[TE["TE02.20.04"]], reason="no VE asks the vendor for it; TE02.20.04 has the tester verify that the vendor documentation specifies how each method conforms to the relevant standards", note="TE02.20.04: the documentation specifies how the method conforms to the relevant standards"),
        F("listed_in_non_proprietary_security_policy", TRUE, "shall", True, cons=[VE["VE02.20.04"]], note="const true: the vendor-provided non-proprietary security policy 'shall include a list of all vendor affirmed security methods'")],
       layout="one JSON object per method"),
    ST("DataOutputPathSeparation", "VE03.07.03-05: how output data paths are separated from SSP processes",
       "§6.3", (524, 540), [AS_OUT, VE["VE03.07.03"], VE["VE03.07.04"], VE["VE03.07.05"]], [
        F("paths_disconnected_from_ssp_processes", S(), "shall", "output path gated off during zeroisation", cons=[VE["VE03.07.03"]]),
        F("paths_physically_shared", BOOL, "stated", False, lines=(535, 537), cons=[VE["VE03.07.04"]]),
        F("logical_separation_enforcement", S(), "shall", "arbiter blocks output", req=False, cons=[VE["VE03.07.04"]], note="required when the physical and logical paths are physically shared"),
        F("ssp_to_output_and_output_to_ssp_interference_prevented", S(), "shall", "no shared buffer", cons=[VE["VE03.07.05"]])],
       extra={"allOf": [{"if": {"properties": {"paths_physically_shared": {"const": True}}, "required": ["paths_physically_shared"]}, "then": {"required": ["logical_separation_enforcement"]}}]},
       minimal={"paths_disconnected_from_ssp_processes": "x", "paths_physically_shared": False, "ssp_to_output_and_output_to_ssp_interference_prevented": "y"},
       reject=[("shared paths with no logical separation described", {"paths_disconnected_from_ssp_processes": "x", "paths_physically_shared": True, "ssp_to_output_and_output_to_ssp_interference_prevented": "y"})],
       layout="one JSON object"),
    ST("AuthenticationDataProtection", "VE04.44.01: protection of authentication data against four named threats",
       "§6.4", (569, 572), [AS_AUTH, VE["VE04.44.01"], R_PROT], [
        F("against_unauthorised_use", S(), "shall", "x", cons=[VE["VE04.44.01"], R_PROT]),
        F("against_disclosure", S(), "shall", "x", cons=[VE["VE04.44.01"], R_PROT]),
        F("against_modification", S(), "shall", "x", cons=[VE["VE04.44.01"], R_PROT]),
        F("against_substitution", S(), "shall", "x", cons=[VE["VE04.44.01"], R_PROT])],
       layout="one JSON object"),
    ST("AuthenticationFeedbackObscuring", "VE04.54.01/02: how feedback of authentication data is obscured",
       "§6.4", (610, 615), [AS_FBK, VE["VE04.54.01"], VE["VE04.54.02"]], [
        F("obscuring_method", S(), "shall", "no echo", cons=[VE["VE04.54.01"]]),
        F("operator_confirmation_at_entry", S(), "shall", "show last character briefly", req=False, cons=[VE["VE04.54.02"]], note="'how, if implemented': present only when the vendor lets the operator confirm the data, and then must say how others see nothing useful")],
       layout="one JSON object"),
    ST("OperatingSystemControls", "VE06.11.01: operating system control mechanisms that protect SSPs, control and status data",
       "§6.6", (643, 646), [AS_OS, VE["VE06.11.01"]], [
        F("operating_system_documentation", S(), "shall", "OS hardening guide", cons=[VE["VE06.11.01"]]),
        F("against_unauthorised_execution", S(), "shall", "noexec mounts", cons=[VE["VE06.11.01"]]),
        F("against_unauthorised_modification", S(), "shall", "file permissions", cons=[VE["VE06.11.01"]]),
        F("against_unauthorised_reading", S(), "shall", "process isolation", cons=[VE["VE06.11.01"]])],
       layout="one JSON object"),
    ST("EnclosureHardness", "VE07.26.01/02: strength or hardness of the enclosure, coating or potting and the temperature range the security policy states",
       "§6.7", (673, 677), [AS_HARD, VE["VE07.26.01"], VE["VE07.26.02"]], [
        F("strength_or_hardness", S(), "shall", "Shore D 80", cons=[VE["VE07.26.01"]]),
        F("rationale_appropriate_for_design", S(), "shall", "x", cons=[VE["VE07.26.01"]]),
        F("nominal_temperature", S(), "shall", "20 C", cons=[VE["VE07.26.02"]]),
        F("high_temperature", S(), "shall", "70 C", cons=[VE["VE07.26.02"]]),
        F("low_temperature", S(), "shall", "-20 C", cons=[VE["VE07.26.02"]])],
       layout="one JSON object; the temperature fields belong in the security policy"),
    ST("EnvironmentalProtectionStatement", "VE07.77.01/02 and VE07.81.01/02: which EFP or EFT approach was chosen and the ranges met",
       "§6.7", (712, 726), [AS_EFP, VE["VE07.77.01"], VE["VE07.77.02"], VE["VE07.81.01"], VE["VE07.81.02"], R_EFP_DOC, R_EFT_DOC, R_EFP_TE, R_EFT_TE], [
        F("feature", E("EFP", "EFT"), "shall", "EFP", cons=[VE["VE07.77.01"], VE["VE07.81.01"]]),
        F("response", E("shutdown", "zeroise_plaintext_unprotected_ssps", "continue_to_operate_normally"), "shall", "shutdown", cons=[VE["VE07.77.01"], R_EFP_EITHER] + R_EFP_AB + [VE["VE07.81.01"], R_EFT_EITHER] + R_EFT_ABC,
          note="EFP: shutdown or zeroise (a, b); EFT adds 'continue to operate normally' (a, b, c); the schema rejects continue for EFP"),
        F("approach_chosen_and_feature_described", S(), "shall", "x", cons=[R_EFP_DOC, R_EFT_DOC], note="'Documentation shall state which of these approaches was chosen and provide a specification description'"),
        F("temperature_range_met", S(), "shall", "-20 C to 70 C", cons=[VE["VE07.77.02"], VE["VE07.81.02"]]),
        F("normal_operating_temperature_range", S(), "stated", "0 C to 50 C", lines=(730, 733), cons=[R_EFP_TE, R_EFT_TE]),
        F("normal_operating_voltage_range", S(), "stated", "3.0 V to 3.6 V", lines=(730, 733), cons=[R_EFP_TE, R_EFT_TE])],
       extra={"allOf": [{"if": {"properties": {"feature": {"const": "EFP"}}, "required": ["feature"]}, "then": {"properties": {"response": {"enum": ["shutdown", "zeroise_plaintext_unprotected_ssps"]}}}}]},
       reject=[("EFP described as continuing to operate", {"feature": "EFP", "response": "continue_to_operate_normally", "approach_chosen_and_feature_described": "x", "temperature_range_met": "t", "normal_operating_temperature_range": "t", "normal_operating_voltage_range": "v"})],
       accept=[("EFT that continues to operate", {"feature": "EFT", "response": "continue_to_operate_normally", "approach_chosen_and_feature_described": "x", "temperature_range_met": "t", "normal_operating_temperature_range": "t", "normal_operating_voltage_range": "v"})],
       layout="one JSON object"),
    ST("SplitKnowledgeEvidence", "VE09.23.01/02: split knowledge procedure documentation",
       "§6.9", (791, 802), [AS_SPLIT, VE["VE09.23.01"], VE["VE09.23.02"], TE["TE09.23.01"]], [
        F("components_required", I(2), "shall", 2, cons=[AS_SPLIT, VE["VE09.23.01"], TE["TE09.23.01"]], note="'%s' (AS09.23): minimum 2" % cut(787, 788, "at least two", "cryptographic key")),
        F("rationale_fewer_components_reveal_nothing_but_length", S(), "shall", "x", req=False, cons=[VE["VE09.23.02"]], note="required when knowledge of the number of components is required to reconstruct the key")],
       layout="one JSON object"),
    ST("SspZeroisationInformation", "VE09.28.01: zeroisation information for unprotected SSPs (items a to e)",
       "§6.9", (825, 833), [AS_Z28, VE["VE09.28.01"]] + R_Z28I, [
        F("zeroisation_techniques", A(S(), lo=1), "shall", ["overwrite with zeros"], cons=[VE["VE09.28.01"], R_Z28I[0]]),
        F("restrictions_when_unprotected_ssps_can_be_zeroised", S(), "shall", "none", cons=[VE["VE09.28.01"], R_Z28I[1]]),
        F("unprotected_ssps_zeroised", A(S(), lo=1), "shall", ["AES key"], cons=[VE["VE09.28.01"], R_Z28I[2]]),
        F("unprotected_ssps_not_zeroised_and_rationale", A(S()), "shall", [], cons=[VE["VE09.28.01"], R_Z28I[3]], note="may be empty: items 'not zeroised' with rationale, when there are any"),
        F("rationale_time_not_sufficient_to_compromise", S(), "shall", "x", cons=[VE["VE09.28.01"], R_Z28I[4]])],
       layout="one JSON object"),
    ST("PlaintextSspZeroisationInformation", "VE09.30.01: zeroisation information for plaintext SSPs (items a to e)",
       "§6.9", (934, 942), [AS_Z30, VE["VE09.30.01"]] + R_Z30I, [
        F("zeroisation_techniques", A(S(), lo=1), "shall", ["overwrite with random data"], cons=[VE["VE09.30.01"], R_Z30I[0]]),
        F("restrictions_when_plaintext_ssps_can_be_zeroised", S(), "shall", "none", cons=[VE["VE09.30.01"], R_Z30I[1]]),
        F("plaintext_ssps_zeroised", A(S(), lo=1), "shall", ["AES key"], cons=[VE["VE09.30.01"], R_Z30I[2]]),
        F("plaintext_ssps_not_zeroised_and_rationale", A(S()), "shall", [], cons=[VE["VE09.30.01"], R_Z30I[3]]),
        F("rationale_time_not_sufficient_to_compromise", S(), "shall", "x", cons=[VE["VE09.30.01"], R_Z30I[4]])],
       layout="one JSON object"),
    ST("ProceduralZeroisation", "VE09.28.03: zeroisation performed procedurally under operator control",
       "§6.9", (838, 841), [AS_Z28, VE["VE09.28.03"]], [
        F("procedure", S(), "shall", "power-cycle and erase", cons=[VE["VE09.28.03"]]),
        F("specified_in_vendor_documentation", TRUE, "must", True, cons=[VE["VE09.28.03"]], note="'vendor documentation and the module security policy must specify how the methods shall be performed'"),
        F("specified_in_security_policy", TRUE, "must", True, cons=[VE["VE09.28.03"]])],
       layout="one JSON object"),
    ST("ZeroisedSspNonRetrievability", "VE09.29.01: how a zeroised SSP cannot be retrieved or reused",
       "§6.9", (894, 895), [AS_Z29, VE["VE09.29.01"]], [
        F("how_not_retrievable_or_reusable", S(), "shall", "x", cons=[VE["VE09.29.01"]])], layout="one JSON object"),
    ST("FunctionalTestingDocumentation", "VE11.29.01: functional testing performed on the module",
       "§6.11", (1021, 1023), [AS_FN, VE["VE11.29.01"]], [
        F("functional_testing_performed", S(), "shall", "x", cons=[VE["VE11.29.01"]]),
        F("assurance_behaves_per_security_policy_and_functional_specification", S(), "shall", "x", cons=[VE["VE11.29.01"]])], layout="one JSON object"),
    ST("CveDisclosure", "VE11.38.03: one CVE associated with the module and its disposition",
       "§6.11", (1050, 1054), [AS_GUIDE, VE["VE11.38.03"], R_CVE1, R_CVE2], [
        F("cve_id", S(pattern=r"^CVE-\d{4}-\d{4,}$"), "shall", "CVE-2024-12345", cons=[VE["VE11.38.03"]]),
        F("security_relevant", BOOL, "shall", False, cons=[VE["VE11.38.03"]]),
        F("assurance_not_security_relevant", S(), "shall", "x", req=False, cons=[VE["VE11.38.03"], R_CVE1], note="required when security_relevant is false"),
        F("mitigation", S(), "shall", "x", req=False, cons=[R_CVE2], note="required when security_relevant is true")],
       extra={"allOf": [{"if": {"properties": {"security_relevant": {"const": False}}, "required": ["security_relevant"]}, "then": {"required": ["assurance_not_security_relevant"]}},
                        {"if": {"properties": {"security_relevant": {"const": True}}, "required": ["security_relevant"]}, "then": {"required": ["mitigation"]}}]},
       minimal={"cve_id": "CVE-2024-12345", "security_relevant": False, "assurance_not_security_relevant": "x"},
       accept=[("relevant CVE with mitigation", {"cve_id": "CVE-2024-12345", "security_relevant": True, "mitigation": "patched"})],
       reject=[("relevant CVE with no mitigation", {"cve_id": "CVE-2024-12345", "security_relevant": True}),
               ("not-relevant CVE with no assurance", {"cve_id": "CVE-2024-12345", "security_relevant": False})],
       layout="one JSON object per CVE"),
]

HEAD = """# =====================================================================
# nist-sp-800-140 messages -- SP 800-140 (the DTR) defines no wire format. It
# MODIFIES the assertions (ASnn.nn), Vendor Evidence (VE) and Test Evidence
# (TE) of ISO/IEC 24759 6.1 to 6.12. Its structures are therefore (1) the
# assertion / evidence framework itself (Assertion, EvidenceItem, and the
# TestEvidenceResponse format of section 6) and (2) the content each VE item
# prescribes where it lists specific things (ProcessorEvidence, zeroisation
# items a to e, the four authentication-data threats, CVE disposition ...).
# %d structures. The full index of the %d assertions and %d evidence items the
# document modifies is generated by script into examples/.
#
# Not modelled: VE items that are a single free-text description with no
# listed parts, and every TE item (a tester's procedure, not a structure; its
# response format is TestEvidenceResponse). Sections 6.1, 6.5, 6.8, 6.12 say
# 'No change'.
#
# Written by schema/build.derived.py; ids resolved by script from requirements.yaml.
# source_digest: %s
# =====================================================================
record: nist-sp-800-140
reviewed_by: ""
source_digest: '%s'
applicability: 'derived structures for the evidence framework and the VE items that list parts; no wire format'""" % (len(structs), len(ASSERT), len(EVID), SOURCE_DIGEST, SOURCE_DIGEST)


def sreadme(structs, na, nr):
    return generic_schema_readme(structs, na, nr,
        "SP 800-140 has no formal notation. Each schema describes one evidence framework object or the parts a "
        "Vendor Evidence item lists.", """
Findings from reading the evidence ids by script (%d assertions, %d evidence items, all with source lines in
`../examples/`): %s
Other source anomalies: TE09.28.01 cites VE09.30.01 (the plaintext assertion's item) from assertion AS09.28, and
NOTE 1 of AS09.28 says the assertion 'is tested AS09.30'; TE02.15.10 and TE02.17.06 verify documentation 'provided
under assertion AS02.02', an assertion this document does not modify.
""" % (len(ASSERT), len(EVID), ("every evidence id carries its assertion's number prefix." if not MISPLACED else
        "evidence ids whose prefix differs from the assertion above them: %s." % ", ".join(MISPLACED))))


def extra_examples(validators):
    for kind, rows, sc in (("assertion", ASSERT, "Assertion"), ("evidence", EVID, "EvidenceItem")):
        for r in rows:
            row = {k: v for k, v in r.items()}
            errs = list(validators[sc].iter_errors(row))
            assert not errs, (row, errs[0].message)
            a = row["source_lines"]
            assert Q(int(a))["source_lines"] == a
    dump_json(DIST / "examples" / "assertion-index.derived.json", {
        "_comment": "DERIVED, not verbatim. Every assertion SP 800-140 modifies, read from the source by ../schema/build.derived.py: id, security area, title, levels, the VE and TE ids under it, and the line the assertion starts on. Each row validates against ../schema/Assertion.derived.schema.json.",
        "count": len(ASSERT), "rows": ASSERT})
    dump_json(DIST / "examples" / "evidence-index.derived.json", {
        "_comment": "DERIVED, not verbatim. Every VE and TE item id SP 800-140 lists, with the assertion above it and the line it starts on. Each row validates against ../schema/EvidenceItem.derived.schema.json.",
        "count": len(EVID), "rows": EVID})
    return {"assertions": len(ASSERT), "evidence": len(EVID)}


def ereadme(structs, na, nr, extras):
    return (FRONT % (ID, "examples", ID, "examples and test vectors") + "# Examples and test vectors\n\n"
            "**Finding: SP 800-140 contains no worked example, sample evidence package or test vector.** The words "
            "'test vectors' occur only in the self-test assertions, as inputs a module must not need:\n\n" + md(984, 987) + "\n"
            "## Fixtures\n\n| file | what it is | expected result |\n|---|---|---|\n"
            "| `assertion-index.derived.json` | the %d assertions with their VE and TE ids and start lines | every row accepted by `Assertion` |\n"
            "| `evidence-index.derived.json` | the %d evidence items with the assertion above each | every row accepted by `EvidenceItem` |\n"
            "| `evidence-cases.derived.json` | this library's cases for all %d schemas: %d cases, %d `accept`, %d `reject` | each case's `expect` |\n\n"
            "`../schema/build.derived.py` regenerates all three and exits 1 on any difference.\n"
            % (extras["assertions"], extras["evidence"], len(structs), na + nr, na, nr))


finish(structs, HEAD, "evidence", sreadme, ereadme, extra_examples=extra_examples)
