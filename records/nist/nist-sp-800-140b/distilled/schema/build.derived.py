#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library; nist-sp-800-140b ships no schema, so
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


def b(i):
    """An id's bare R-NNNN, for prose."""
    return i.split("#")[1]


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
R3 = R(r"^Therefore, the format of the security policy shall be presented in the same order", "§6.1")
R4 = R(r"^o For software, firmware, and hybrid cryptographic modules, list the operating system", "Annex B.2.2")
R5 = R(r"^6 As part of this requirement, algorithm-specific guidance")
R6 = R(r"^7 The physical ports here should map")
R8 = R(r"^● Separately list the security and non-security services")
# Since pass 1 the skeleton fragments R-0007, R-0009 and R-0010 are split_of
# parts of the whole footnote sentences; cite the wholes.
FN7B = RL(591, "If the ports are different per module")
FN8 = RL(681, "8 Each algorithm shown in the Approved Algorithms")
FN10 = RL(688, "10 Each algorithm shown in the Non-Approved Algorithms Not Allowed")
R11 = R(r"^Additional photos/illustrations may be provided")
R12 = R(r"^13 This should be specified in the .Import/Export. column")
R13 = R(r"^14 The SSPs should map to the Approved Algorithms")
# §6.1 and the inferred readings of it
R_ALLREQ = R(r"^All requirements from ISO/IEC 24759 section 6.14 and ISO/IEC 19790 Annex B apply", "§6.1")
R_ORDER = R(r"^A conforming security policy has the twelve sections", "§6.1")
R_NOCHG = R(r"^Where a B\.2 clause of this SP reads No change", "§6.1")
# B.2.1
B21_TAB = RL(351, "A table indicating the individual clause levels")
B21_OSR = RL(352, "Overall Security Rating")
B21_HDR = RL(358)
B21_ROWS = [RL(n) for n in (361, 363, 366, 369, 372, 374, 376, 378, 380, 383, 385, 387)]
# B.2.2
B22_DESIG = RL(399, "Hardware, Software, Firmware, or Hybrid designation")
B22_SWLBL = RL(403, "[For Software/Firmware/Hybrid Module]")
B22_TOE = RL(405)
B22_VAOE = RL(420)
B22_HWLBL = RL(431, "[For Hardware Module]")
B22_HWCFG = RL(433)
FN1 = RL(445, "1 Examples may be ports")
B22_ALGB = RL(454, "Table of all security functions")
B22_ALG = RL(458)
B22_NAA = RL(471)
B22_NSC = RL(479)
FN2, FN3, FN4 = RL(488), RL(494), RL(497)
B22_NNA = RL(507)
B22_ILL = RL(514, "Illustrative diagram, schematic or photograph")
B22_PHOTO = RL(514, "A photograph is included for a hardware module")
B22_VERS = RL(515, "If the security policy encompasses multiple versions")
B22_BD = RL(517, "For a software or firmware cryptographic module")
B22_BD1, B22_BD2 = RL(519), RL(528)
B22_BDA = RL(531, "Block Diagram, as applicable")
B22_SWLBL2 = RL(532)
B22_FIG1, B22_FIG2 = RL(537), RL(542)
B22_HYLBL = RL(549)
B22_FIG3 = RL(554)
B22_RULES = RL(556, "Overall security design and the rules of operation")
FN5 = RL(585)
# B.2.3
B23_PORTS, B23_LOGI, B23_PHYS, B23_HDR = RL(563), RL(564), RL(565), RL(567)
# B.2.4
B24_ROLES, B24_RTAB, B24_RSHDR = RL(580), RL(581), RL(601)
B24_AUTHM, B24_AUTHS, B24_RAHDR = RL(608), RL(610), RL(616)
B24_ACC = RL(629, "For each operator role authorized to use the service")
B24_ASHDR = RL(641)
B24_LEG = [RL(n) for n in (650, 652, 658, 660, 662)]
B24_NSHDR = RL(666)
FN9 = RL(685)
# B.2.7
B27_L2, B27_MECH, B27_ACT, B27_INSP = RL(702), RL(704), RL(706), RL(710)
B27_SEAL, B27_FILL1 = RL(725), RL(730)
B27_FILL2 = RL(732, "The filler panels will be included in the list of parts")
B27_PLACE, B27_TOTAL = RL(734), RL(736)
B27_NUMB = RL(737, "The photos or illustrations which provide instruction")
B27_FIGS = [RL(752), RL(758)]
B27_L3, B27_EFP = RL(762), RL(764)
B27_EFPROWS = [RL(n) for n in (768, 770, 772, 774)]
FN11 = RL(780)
B27_HLBL, B27_HHDR = RL(789), RL(792)
B27_HROWS = [RL(794), RL(796)]
FN12 = RL(832)
# B.2.9
B29_KEYT, B29_OTHER, B29_RBG, B29_RBGU = RL(809), RL(813), RL(814), RL(815)
B29_IO, B29_STOR, B29_ZERO = RL(816), RL(817), RL(818)
B29_SSPHDR = RL(820)
FN13 = R12
FN14T = RL(874, "Approved Mode of Operation tables in section B.2.2")
B29_ENTHDR = RL(849)
FN15 = RL(875)

HEADS = [re.match(r"^B\.2\.(\d+) (.*)$", span(n)) for n in (349, 397, 557, 578, 674, 696, 700, 799, 803, 857, 860, 867)]
SECS = [("B.2." + m.group(1), m.group(2)) for m in HEADS]
assert [int(m.group(1)) for m in HEADS] == list(range(1, 13)), SECS
TAB_TITLES = [t for _, t in SECS]
TAB_TITLES[8] = "Sensitive security parameter management"       # the Table x - Security Levels spelling
for t in TAB_TITLES[:1] + TAB_TITLES[2:]:
    assert t in span(358, 387) or t.replace("Cryptographic module specification", "Cryptographic module specification") in span(358, 387), t

TR = ("a column of a table template in SP 800-140B; no sentence makes the cell mandatory, so the column's presence in "
      "the template is read as required (this library's reading)")


def col(name, ex, sch=None, lvl="inferred", cons=None, note=None, req=True, reason=None, lines=None):
    return F(name, sch or S(), lvl, ex, req=req, cons=cons, reason=(reason or TR) if lvl == "inferred" else None, note=note, lines=lines)


def sec_item(i, sid, title):
    return {"type": "object", "additionalProperties": False, "required": ["id", "title", "applicable"],
            "properties": {"id": {"const": sid}, "title": {"const": title}, "applicable": BOOL,
                           "marked_not_applicable": TRUE, "content": {"type": "object"}},
            "allOf": [{"if": {"properties": {"applicable": {"const": False}}, "required": ["applicable"]},
                       "then": {"required": ["marked_not_applicable"]}}]}


SEC_OK = [{"id": a, "title": b, "applicable": True} for a, b in SECS]
SEC_NA = [dict(x) for x in SEC_OK]
SEC_NA[4] = {"id": SECS[4][0], "title": SECS[4][1], "applicable": False}   # not marked
SEC_NA_OK = [dict(x) for x in SEC_OK]
SEC_NA_OK[4] = {"id": SECS[4][0], "title": SECS[4][1], "applicable": False, "marked_not_applicable": True}
LVL_ROWS = [{"section_number": i + 1, "section_title": t, "security_level": 1} for i, t in enumerate(TAB_TITLES)]
ENVS = {"type": "object"}
DIAG = {"type": "object", "additionalProperties": False, "required": ["shows_logical_object_location", "shows_interactions"],
        "properties": {"shows_logical_object_location": TRUE, "shows_interactions": TRUE}}
ACC = {"type": "object", "additionalProperties": False, "required": ["role", "ssp", "rights"],
       "properties": {"role": S(), "ssp": S(), "rights": A(E("G", "R", "W", "E", "Z"), lo=1, uniq=True)}}
PLACE = {"type": "object", "additionalProperties": False, "required": ["item_number", "placement"],
         "properties": {"item_number": I(1), "placement": S()}}
RTAB = "one JSON object per table row"

structs = [
    ST("SecurityPolicy", "the non-proprietary security policy as an ordered list of the twelve Annex B sections, each marked applicable or not",
       "§6.1", (328, 330), [R3, R_ALLREQ, R_ORDER, R_NOCHG], [
        F("sections", {"type": "array", "minItems": 12, "maxItems": 12,
                       "prefixItems": [sec_item(i, a, b) for i, (a, b) in enumerate(SECS)], "items": False},
          "shall", SEC_OK, lines=(328, 330), cons=[R3, R_ORDER],
          note="exactly the twelve Annex B sections in Annex B order, from General to Mitigation of other attacks (%s, %s); a section that is not applicable 'shall be marked as such' (marked_not_applicable const true); section content is an open object whose tables have their own schemas" % (b(R3), b(R_ORDER)))],
       caption=None, accept=[("one section marked not applicable", {"sections": SEC_NA_OK})],
       reject=[("a not-applicable section left unmarked", {"sections": SEC_NA}),
               ("sections out of Annex B order", {"sections": [SEC_OK[1], SEC_OK[0]] + SEC_OK[2:]}),
               ("only eleven sections", {"sections": SEC_OK[:11]}),
               ("a section marked not applicable with marked_not_applicable false", {"sections": SEC_OK[:4] + [{"id": SECS[4][0], "title": SECS[4][1], "applicable": False, "marked_not_applicable": False}] + SEC_OK[5:]})],
       layout="a document, not a byte format: twelve sections B.2.1 to B.2.12 in order",
       note="Source defect: the heading of B.2.9 reads 'Sensitive security parameters management' (plural) while the B.2.1 Security Levels table prints 'Sensitive security parameter management'; the section list uses the headings and SecurityLevelsTable the table's spelling."),
    ST("SecurityLevelsTable", "B.2.1: the overall security rating and the security level of each of the twelve areas (Table x - Security Levels)",
       "Annex B.2.1", (358, 359), [B21_TAB, B21_OSR, B21_HDR], [
        F("overall_security_rating", I(1, 4), "stated", 1, lines=(351, 352), cons=[B21_OSR],
          note="'Overall Security Rating of the module'; the 1 to 4 range is FIPS 140-3's four levels, outside this document"),
        F("area_levels", {"type": "array", "minItems": 12, "maxItems": 12, "items": False,
                           "prefixItems": [{"allOf": [{"$ref": "#/$defs/Row"},
                                                      {"properties": {"section_number": {"const": i + 1}, "section_title": {"const": tt}}}]}
                                           for i, tt in enumerate(TAB_TITLES)]}, "stated", LVL_ROWS,
          lines=(351, 352), cons=[B21_TAB, B21_HDR] + B21_ROWS, note="one row per area, numbered 1 to 12 as the ISO/IEC 24759 section number below 6, each position pinned to the number and title the table prints")],
       caption=(388, 388),
       defs={"Row": {"type": "object", "additionalProperties": False, "required": ["section_number", "section_title", "security_level"],
                     "properties": {"section_number": I(1, 12), "section_title": E(*TAB_TITLES), "security_level": I(1, 4)}}},
       reject=[("eleven areas only", {"overall_security_rating": 1, "area_levels": LVL_ROWS[:11]}),
               ("an area level of 5", {"overall_security_rating": 1, "area_levels": LVL_ROWS[:11] + [dict(LVL_ROWS[11], security_level=5)]}),
               ("twelve copies of the first area", {"overall_security_rating": 1, "area_levels": [LVL_ROWS[0]] * 12}),
               ("the areas in reverse order", {"overall_security_rating": 1, "area_levels": LVL_ROWS[::-1]}),
               ("area 1 titled with area 10's title", {"overall_security_rating": 1, "area_levels": [dict(LVL_ROWS[0], section_title=TAB_TITLES[9])] + LVL_ROWS[1:]})],
       layout=RTAB),
    ST("TestedOperationalEnvironment", "B.2.2: one tested operational environment of a software, firmware or hybrid module",
       "Annex B.2.2", (405, 406), [R4, B22_DESIG, B22_SWLBL, B22_TOE], [
        col("number", 1, I(1)), col("operating_system", "Linux 5.4", lvl="shall", cons=[R4], note="'list the operating system(s) the module was tested on'"),
        col("hardware_platform", "x86-64 server"), col("processor", "Intel Xeon"), col("paa_acceleration", "AES-NI", note="header 'PAA/Acceleration'; the source does not expand the abbreviation")],
       caption=(417, 417), layout=RTAB),
    ST("VendorAffirmedOperationalEnvironment", "B.2.2: one operational environment the vendor affirms the module can be used on",
       "Annex B.2.2", (420, 420), [R4, B22_SWLBL, B22_VAOE], [
        col("number", 1, I(1)), col("operating_system", "Linux 5.10", lvl="shall", cons=[R4], note="'the operating system(s) that the vendor affirms can be used by the module'"),
        col("hardware_platform", "x86-64 server")], caption=(427, 427), layout=RTAB),
    ST("HardwareModuleTestedConfiguration", "B.2.2: one tested configuration of a hardware module",
       "Annex B.2.2", (433, 436), [B22_DESIG, B22_HWLBL, B22_HWCFG], [
        col("model", "Model 1"), col("hardware_part_number_and_version", "HW-100 v2"), col("firmware_version", "1.4.2"),
        col("distinguishing_features", "ports, memory, field-replaceable accessories", note="footnote 1 (%s) gives examples of distinguishing features: ports and interfaces, memory, field replaceable and stationary accessories" % b(FN1), cons=[B22_HWCFG, FN1])],
       caption=(441, 441), layout=RTAB),
    ST("ApprovedAlgorithmRow", "B.2.2: one row of Table x - Approved Algorithms (security functions employed for approved services)",
       "Annex B.2.2", (458, 460), [B22_ALGB, B22_ALG, FN2, FN3, FN8], [
        col("cavp_cert", "A1234", note="footnote 3 (%s): the table also holds vendor-affirmed approved algorithms not yet CAVP-testable, and the source gives no marker for them; footnote 2 (%s) asks for a footnote on certificate entries no service uses" % (b(FN3), b(FN2)), cons=[B22_ALG, FN2, FN3]),
        col("algorithm_and_standard", "AES-CBC, FIPS 197"), col("mode_or_method", "CBC", cons=[B22_ALGB, B22_ALG]),
        col("description_key_sizes_key_strengths", "128, 256 bits", cons=[B22_ALGB, B22_ALG]), col("use_or_function", "encryption and decryption")],
       caption=(465, 465), layout=RTAB),
    ST("NonApprovedAlgorithmAllowedRow", "B.2.2: one row of Table x - Non-Approved Algorithms Allowed in the Approved Mode of Operation",
       "Annex B.2.2", (471, 471), [B22_NAA, FN8], [
        col("algorithm", "MD5", cons=[B22_NAA, FN8], note="footnote 8 (%s): each algorithm in this table and in the Approved Algorithms table should map to at least one service (a should; not enforceable in a row)" % b(FN8)),
        col("caveat", "allowed in the approved mode only as part of TLS"), col("use_or_function", "key derivation")],
       caption=(476, 476), layout=RTAB),
    ST("NonApprovedAlgorithmNoSecurityClaimedRow", "B.2.2: one row of Table x - Non-Approved Algorithms Allowed in the Approved Mode of Operation with No Security Claimed",
       "Annex B.2.2", (479, 479), [B22_NSC, FN4], [
        col("algorithm", "Blowfish", note="footnote 4 (%s): these algorithms claim no security and meet no FIPS 140-3 requirement, so no SSP maps to them" % b(FN4), cons=[B22_NSC, FN4]),
        col("caveat", "no security claimed"), col("use_or_function", "obfuscation")],
       caption=(484, 484), layout=RTAB),
    ST("NonApprovedAlgorithmNotAllowedRow", "B.2.2: one row of Table x - Non-Approved Algorithms Not Allowed in the Approved Mode of Operation",
       "Annex B.2.2", (507, 507), [B22_NNA, FN10], [
        col("algorithm_or_function", "DES", cons=[B22_NNA, FN10], note="footnote 10 (%s): each algorithm in this table should map to at least one (non-approved) service" % b(FN10)),
        col("use_or_function", "encryption")],
       caption=(512, 512), layout=RTAB),
    ST("ModuleRepresentation", "B.2.2: the illustrations of the module (photograph, block diagram, per-version handling)",
       "Annex B.2.2", (514, 518), [B22_ILL, B22_DESIG, B22_FIG1, B22_FIG2, B22_FIG3], [
        F("module_type", E("hardware", "software", "firmware", "hybrid"), "stated", "software", lines=(514, 518), cons=[B22_DESIG, B22_ILL]),
        F("photograph", S(), "stated", "photo-model1.png", req=False, lines=(514, 515), cons=[B22_PHOTO, B22_HYLBL, FN5, B22_FIG3],
          note="'A photograph is included for a hardware module'; required for hardware and hybrid (the hybrid hardware component) by the schema"),
        F("block_diagram", DIAG, "stated", {"shows_logical_object_location": True, "shows_interactions": True}, req=False, lines=(517, 530), cons=[B22_BD, B22_BD1, B22_BD2, B22_BDA, B22_SWLBL2, B22_FIG1, B22_FIG2],
          note="for software or firmware (and the hybrid's software or firmware component): a block diagram showing where the logical object sits relative to the operating system, the supporting applications and the boundary, and how it interacts with them (%s, %s); both const true" % (b(B22_BD1), b(B22_BD2))),
        F("encompasses_multiple_versions", BOOL, "stated", True, req=False, lines=(515, 517), cons=[B22_VERS]),
        F("multiple_versions_representation", E("each_version_separately", "annotated_as_illustrated_for_all_versions"), "stated", "each_version_separately", req=False, lines=(515, 517), cons=[B22_VERS],
          note="required when the policy encompasses multiple versions: 'each version is represented separately or annotated that the representation is illustrated for all versions'")],
       extra={"allOf": [
           {"if": {"properties": {"module_type": {"enum": ["hardware", "hybrid"]}}, "required": ["module_type"]}, "then": {"required": ["photograph"]}},
           {"if": {"properties": {"module_type": {"enum": ["software", "firmware", "hybrid"]}}, "required": ["module_type"]}, "then": {"required": ["block_diagram"]}},
           {"if": {"properties": {"encompasses_multiple_versions": {"const": True}}, "required": ["encompasses_multiple_versions"]}, "then": {"required": ["multiple_versions_representation"]}}]},
       minimal={"module_type": "software", "block_diagram": {"shows_logical_object_location": True, "shows_interactions": True}},
       accept=[("hardware module with a photograph", {"module_type": "hardware", "photograph": "p.png"})],
       reject=[("hardware module with no photograph", {"module_type": "hardware"}),
               ("firmware module with no block diagram", {"module_type": "firmware"}),
               ("hybrid module with only a photograph", {"module_type": "hybrid", "photograph": "p.png"}),
               ("block diagram that does not show interactions", {"module_type": "software", "block_diagram": {"shows_logical_object_location": True, "shows_interactions": False}}),
               ("multiple versions with no representation rule", {"module_type": "software", "block_diagram": {"shows_logical_object_location": True, "shows_interactions": True}, "encompasses_multiple_versions": True})],
       layout="figures: Figure x - Logical boundary, Physical boundary, [Model 1]"),
    ST("RulesOfOperation", "B.2.2: overall security design and rules of operation, with the guidance footnote 6 requires",
       "Annex B.2.2", (556, 556), [B22_RULES, R5], [
        F("overall_security_design", S(), "stated", "text", lines=(556, 556), cons=[B22_RULES]),
        F("rules_of_operation", S(), "stated", "text", lines=(556, 556), cons=[B22_RULES]),
        F("algorithm_specific_guidance", S(), "shall", "text", cons=[R5], note="footnote 6: 'shall be included'"),
        F("security_policy_specific_requirements", S(), "shall", "text", cons=[R5], note="footnote 6: 'shall be included'")],
       layout="prose section"),
    ST("PortInterfaceRow", "B.2.3: one row of Table x - Ports and Interfaces",
       "Annex B.2.3", (567, 568), [B23_PORTS, B23_LOGI, B23_PHYS, B23_HDR, R6, FN7B], [
        col("physical_port_interface", "USB-A", cons=[B23_PHYS, B23_HDR, R6], note="footnote 7 (%s): the physical ports should map to those shown in the module images (a should)" % b(R6)),
        col("logical_interface", "data input", note="the source says 'five logical interfaces' without naming them", cons=[B23_LOGI, B23_HDR]),
        col("data_that_passes_over_port", "plaintext user data", cons=[B23_PHYS, B23_HDR]),
        F("differences_per_module", S(), "should", "Model 2 omits the serial port", req=False, cons=[FN7B], note="footnote 7 (%s): if the ports differ per module within one submission, this table should indicate the differences" % b(FN7B))],
       caption=(573, 573), layout=RTAB),
    ST("RoleServiceRow", "B.2.4: one row of Table x - Roles, Service Commands, Input and Output",
       "Annex B.2.4", (601, 601), [B24_ROLES, B24_RTAB, B24_RSHDR], [col("role", "Crypto Officer"), col("service", "Show status"), col("input", "command"), col("output", "status")],
       caption=(606, 606), layout=RTAB),
    ST("RoleAuthenticationRow", "B.2.4: one row of Table x - Roles and Authentication",
       "Annex B.2.4", (616, 616), [B24_AUTHM, B24_AUTHS, B24_RAHDR], [
        col("role", "Crypto Officer"), col("authentication_method", "password", cons=[B24_AUTHM, B24_RAHDR]), col("authentication_strength", "1 in 10^6", cons=[B24_AUTHS, B24_RAHDR]),
        F("identity_or_role_based", E("identity", "role"), "stated", "role", lines=(608, 609), cons=[B24_AUTHM], note="'whether the method is identity or role-based'; no column in the table template"),
        F("method_required", BOOL, "stated", True, lines=(608, 609), cons=[B24_AUTHM], note="'and whether the method is required'; no column in the table template")],
       caption=(621, 621), layout=RTAB),
    ST("ApprovedServiceRow", "B.2.4: one row of Table x - Approved Services",
       "Annex B.2.4", (641, 643), [R8, B24_ASHDR, FN8, FN9], [
        F("service", S(), "may", "Encrypt", cons=[R8, B24_ASHDR], note="'list the service name'"),
        F("description", S(), "may", "Encrypts data", cons=[R8, B24_ASHDR], note="'a concise description of the service purpose and/or use (the service name alone may, in some instances, provide this information)'"),
        F("approved_security_functions", A(S(), lo=1), "stated", ["AES-CBC"], lines=(624, 629), cons=[R8, B24_ASHDR, FN8], note="algorithm(s), key management technique(s) or authentication technique used by the service; footnote 8: each approved algorithm should map to a service"),
        F("keys_and_or_ssps", A(S(), lo=1), "stated", ["AES key"], lines=(624, 629), cons=[R8, B24_ASHDR]),
        F("access_rights", A(ACC, lo=1), "stated", [{"role": "Crypto Officer", "ssp": "AES key", "rights": ["E"]}], lines=(629, 631), cons=[B24_ACC, B24_ASHDR, FN9] + B24_LEG,
          note="'For each operator role authorized to use the service, describe the individual access rights to all SSPs'; rights are G, R, W, E, Z (Generate, Read, Write, Execute, Zeroise, L650-662)"),
        F("indicator", S(), "inferred", "returns 1", reason=TR, cons=[B24_ASHDR])],
       caption=(648, 648), also={"access_right_letters": (650, 662)}, layout=RTAB),
    ST("NonApprovedServiceRow", "B.2.4: one row of Table x - Non-Approved Services",
       "Annex B.2.4", (666, 667), [R8, B24_NSHDR, FN10], [
        col("service", "Hash with MD5", cons=[R8, B24_NSHDR]), col("description", "computes MD5"), col("algorithms_accessed", "MD5", cons=[B24_NSHDR, FN10], note="footnote 10 (%s): each algorithm in the Not Allowed table should map to at least one service" % b(FN10)),
        col("role", "User"), col("indicator", "none")],
       caption=(672, 672), layout=RTAB),
    ST("PhysicalSecurityInspectionRow", "B.2.7: one row of Table x - Physical Security Inspection Guidelines (physical Security Level 2 and above)",
       "Annex B.2.7", (710, 716), [B27_L2, B27_MECH, B27_ACT, B27_INSP], [
        col("physical_security_mechanism", "tamper-evident seal", lvl="stated", lines=(704, 705), cons=[B27_MECH, B27_INSP]),
        col("recommended_frequency_of_inspection_test", "every 90 days", lvl="stated", lines=(706, 708), cons=[B27_ACT, B27_INSP]),
        col("inspection_test_guidance_details", "inspect seal for tear or residue", lvl="stated", lines=(706, 708), cons=[B27_ACT, B27_INSP])],
       caption=(721, 721), layout=RTAB),
    ST("TamperSealApplication", "B.2.7: the photos or illustrations of operator-applied tamper-evident seals or security appliances",
       "Annex B.2.7", (725, 741), [B27_SEAL, R11] + B27_FIGS, [
        F("total_items", I(1), "stated", 2, lines=(736, 741), cons=[B27_TOTAL, B27_NUMB], note="'The total number of tamper-evident seals or security appliances that are needed will be indicated'"),
        F("placements", A(PLACE, lo=1), "stated", [{"item_number": 1, "placement": "over the left screw"}, {"item_number": 2, "placement": "over the right screw"}], lines=(734, 741), cons=[B27_PLACE, B27_NUMB],
          note="each item is numbered in the photo or illustration and the numbers equal the total; equality of placements count and total_items is NOT enforced by the schema"),
        F("filler_panels_needed", BOOL, "stated", False, req=False, lines=(730, 733), cons=[B27_FILL1]),
        F("filler_panels_shown_with_seals_in_photos", TRUE, "stated", True, req=False, lines=(730, 733), cons=[B27_FILL1], note="required, and true, when filler panels are needed"),
        F("filler_panels_in_parts_list", TRUE, "stated", True, req=False, lines=(730, 733), cons=[B27_FILL2], note="required, and true, when filler panels are needed"),
        F("additional_configuration_photos", A(S()), "may", ["rack-mounted configuration"], req=False, cons=[R11], note="'Additional photos/illustrations may be provided to reflect other configurations'")],
       extra={"allOf": [{"if": {"properties": {"filler_panels_needed": {"const": True}}, "required": ["filler_panels_needed"]},
                         "then": {"required": ["filler_panels_shown_with_seals_in_photos", "filler_panels_in_parts_list"]}}]},
       minimal={"total_items": 1, "placements": [{"item_number": 1, "placement": "over the screw"}]},
       reject=[("filler panels needed but not listed", {"total_items": 1, "placements": [{"item_number": 1, "placement": "p"}], "filler_panels_needed": True})],
       layout="photos or illustrations; Figure x - Module 1 Seal Application Locations"),
    ST("EfpEftRow", "B.2.7: one row of Table x - EFP/EFT (physical Security Level 3 and above)",
       "Annex B.2.7", (764, 766), [B27_L3, B27_EFP, FN11], [
        col("condition", "Low Temperature", E("Low Temperature", "High Temperature", "Low Voltage", "High Voltage"), lvl="stated", lines=(764, 774), cons=[B27_EFP] + B27_EFPROWS),
        col("protection_or_testing", "EFP", E("EFP", "EFT"), lvl="stated", lines=(764, 766), cons=[B27_EFP, FN11], note="the second column header asks for EFP or EFT (L764, with footnote 11's mark between the two); footnote 11 (%s) requires EFP at physical Security Level 4" % b(FN11)),
        col("result", "shutdown", E("shutdown", "zeroisation"), lvl="stated", lines=(764, 766), cons=[B27_EFP], note="the third column header, printed across L764-766, asks whether the condition results in a shutdown or a zeroisation")],
       caption=(775, 775), layout=RTAB),
    ST("HardnessTemperatureRow", "B.2.7: one row of Table x - Hardness testing temperature ranges (strong or hard enclosures, coatings or potting)",
       "Annex B.2.7", (792, 792), [B27_HLBL, B27_HHDR, FN12] + B27_HROWS, [
        col("condition", "Low Temperature", E("Low Temperature", "High Temperature"), cons=[B27_HHDR] + B27_HROWS), col("hardness_tested_temperature_measurement", "-20 C", note="footnote 12 (%s): hardness testing is at the lowest and highest temperatures of the module's intended range" % b(FN12), cons=[B27_HHDR, FN12])],
       caption=(797, 797), layout=RTAB),
    ST("SspTableRow", "B.2.9: one row of Table x - SSPs (the key and SSP table)",
       "Annex B.2.9", (820, 823), [B29_KEYT, B29_OTHER, B29_SSPHDR, FN13, R13, FN14T], [
        col("key_ssp_name_type", "AES key", lvl="stated", lines=(809, 812), cons=[B29_KEYT, B29_SSPHDR]),
        F("strength_bits", {"oneOf": [I(1), A(I(1), lo=1)]}, "stated", 256, lines=(809, 810), cons=[B29_KEYT, B29_SSPHDR], note="'strength(s) in bits': one number or a list"),
        col("security_function_and_cert_number", "AES-CBC, A1234", lvl="stated", lines=(810, 811), cons=[B29_KEYT, B29_SSPHDR, R13, FN14T], note="footnote 14 (%s; its last words are %s): each SSP should map to an approved or allowed algorithm and its CAVP certificate (a should)" % (b(R13), b(FN14T))),
        col("generation", "DRBG", lvl="stated", lines=(810, 811), cons=[B29_KEYT, B29_OTHER, B29_SSPHDR]),
        col("import_export", "electronic, encrypted", lvl="stated", lines=(811, 811), cons=[B29_KEYT, B29_IO, B29_SSPHDR, FN13], note="footnote 13 (%s): the electronic and manual SSP I/O methods go in the Import/Export column of the SSP table (a should)" % b(FN13)),
        col("establishment", "SP 800-56A", lvl="stated", lines=(811, 812), cons=[B29_KEYT, B29_SSPHDR]),
        col("storage", "RAM", lvl="stated", lines=(817, 817), cons=[B29_STOR, B29_SSPHDR]),
        col("zeroisation", "zeroise service", lvl="stated", lines=(818, 819), cons=[B29_ZERO, B29_SSPHDR]),
        col("use_and_related_keys", "encrypts user data; wrapped by KEK", lvl="stated", lines=(811, 812), cons=[B29_KEYT, B29_SSPHDR])],
       caption=(828, 828), layout=RTAB),
    ST("EntropySourceRow", "B.2.9: one row of Table x - Non-Deterministic Random Number Generation Specification",
       "Annex B.2.9", (849, 850), [R13, B29_RBG, B29_RBGU, B29_ENTHDR, FN15], [
        col("entropy_source", "ring oscillator", lvl="stated", lines=(847, 847), cons=[R13, B29_ENTHDR]),
        col("minimum_bits_of_entropy", 128, I(1), note="footnote 15 (%s): the minimum bits of entropy generated, requested or believed loaded, with a justification of the amount" % b(FN15), cons=[B29_ENTHDR, FN15]),
        col("details", "256 raw bits per 128 output; justification: min-entropy 0.5/bit", cons=[B29_ENTHDR, FN15])],
       caption=(855, 855), layout=RTAB),
]


HEAD = """# =====================================================================
# nist-sp-800-140b messages -- SP 800-140B (WITHDRAWN 2023-11-17 per its own
# cover page; kept because FIPS 140-3 modules were validated against it)
# prescribes the structure of the NON-PROPRIETARY SECURITY POLICY: twelve
# sections B.2.1 to B.2.12 in Annex B order, an N/A mark for a section that
# does not apply, and, inside them, table templates and figure rules. Six
# sections say 'No change' (B.2.5, B.2.6, B.2.8, B.2.10, B.2.11, B.2.12) and
# add nothing here. Each table template is one derived structure (a ROW);
# SecurityPolicy is the document spine. 22 structures in all.
#
# The table captions all read 'Table x': they are templates, not data. The
# sentences that fill them mostly carry no directive keyword (bulleted
# 'Specify ...', 'Provide ...'), and each is a stated entry of
# requirements.yaml, as is every table's header row, pre-filled row, figure
# caption, applicability label and footnote. constrained_by names those
# entries: per structure the bullet that asks for it, its header row and the
# footnotes on it; per field the bullet, column or footnote it is read from.
# Fields whose only support is the column's presence in a template say so in
# inferred_reason.
#
# Written by schema/build.derived.py; ids resolved by script from requirements.yaml.
# source_digest: %s
# =====================================================================
record: nist-sp-800-140b
reviewed_by: ""
source_digest: '%s'
applicability: 'derived structures: the security policy spine and its table and figure templates; no wire format'""" % (SOURCE_DIGEST, SOURCE_DIGEST)


def sreadme(structs, na, nr):
    return generic_schema_readme(structs, na, nr,
        "SP 800-140B has no formal notation: its Annex B content is bulleted requirements, blank table templates "
        "and figure placeholders. Each schema describes one table row, one figure rule or the document spine.", """
Source defects and decisions:

- B.2.9 is headed 'Sensitive security parameters management' but the Security Levels table prints 'Sensitive
  security parameter management'; both spellings are used where the source uses them.
- The six 'No change' sections (B.2.5, B.2.6, B.2.8, B.2.10, B.2.11, B.2.12) have no schema; their content is
  the open `content` object of their section.
- Footnote requirements that are `should` (ports map to images, algorithms map to services, SSPs map to
  certificates, I/O method in the Import/Export column) cannot be checked inside one row, so they are fields'
  notes, not schema rules. Footnote 6 (`shall`) is required fields of `RulesOfOperation`.
- One cross-row rule is not enforced: the placements count equal to `total_items` (TamperSealApplication).
  SecurityLevelsTable pins each of its twelve positions to the number and title the table prints.
""")


def ereadme(structs, na, nr, extras):
    return (FRONT % (ID, "examples", ID, "examples and test vectors") + "# Examples and test vectors\n\n"
            "**Finding: SP 800-140B contains no worked example, sample security policy or test vector.** Every "
            "table is an empty template whose caption reads 'Table x', for instance:\n\n" + md(416, 417) + "\n"
            "and the only illustrative figure of a value is an aside about counting seals:\n\n" + md(736, 737) + "\n"
            "## What is here instead\n\n"
            "`security-policy-cases.derived.json` holds this library's own cases for the %d schemas in `../schema/`: "
            "%d cases, %d expected to be accepted and %d to be rejected, each with `expect` and a reason. The cases "
            "include the empty object and each mandatory field omitted in turn. `../schema/build.derived.py` "
            "re-validates every case with jsonschema and exits 1 on any difference.\n" % (len(structs), na + nr, na, nr))


finish(structs, HEAD, "security-policy", sreadme, ereadme)
