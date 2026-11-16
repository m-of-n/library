#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library; nist-sp-800-140e ships no schema, so
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
       accept=(), reject=(), layout=None, note=None, props_override=None, minimal=None):
    if not cons:
        raise SystemExit(name + ": constrained_by is empty")
    return dict(name=name, title=title, locator=locator, lines=lines, cons=list(cons),
                fields=fields, caption=caption, extra=extra or {}, defs=defs,
                accept=list(accept), reject=list(reject), layout=layout, note=note,
                props_override=props_override, minimal=minimal)


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

R_COMM = R(r"^Some of these mechanisms may be employed to establish module provided protected communication services", "§6.1")
R_T1 = R(r"^While there are currently no approved authentication mechanisms", "§6.2")
R_L1 = R(r"^Level 1 None required", "§6.2")
R_L1S = R(r"^If authentication is used, it should meet the requirements of Level 2", "§6.2")
R_63B = R(r"^Vendors should use SP 800-63B as a framework", "§6.2")
R_TEST = R(r"^Testers should review and affirm the vendor documentation", "§6.2")
# Table 1's rows are their own stated entries (row:); the mechanisms are read from them.
R_ROW2 = RL(299, "Memorized secret Level 2")
R_ROW3 = RL(304, "Level 3")
R_ROW4 = RL(321, "Level 4")
R_63BSEC = RL(327, "Normative SP 800-63B sections include")

# Table 1, read by script: the mechanism names are the bullets of the Level 3 and Level 4 cells.
L3_NAMES = [x.strip(" ;") for x in span(304, 318).split("•")[1:]]
L4_NAMES = [x.strip(" ;") for x in span(321, 322).split("•")[1:]]
assert len(L3_NAMES) == 9 and len(L4_NAMES) == 2 and set(L4_NAMES) <= set(L3_NAMES), (L3_NAMES, L4_NAMES)
ROWS = [
    {"level": 1, "lines": (295, 297), "instance": {"level": 1, "authentication_required": False,
     "permitted_mechanisms": [], "if_used_minimum_level": 2}},
    {"level": 2, "lines": (299, 302), "instance": {"level": 2, "authentication_required": True,
     "permitted_mechanisms": L3_NAMES}},
    {"level": 3, "lines": (304, 318), "instance": {"level": 3, "authentication_required": True,
     "permitted_mechanisms": L3_NAMES}},
    {"level": 4, "lines": (321, 322), "instance": {"level": 4, "authentication_required": True,
     "permitted_mechanisms": L4_NAMES}},
]

claim_ok = {"level": 3, "mechanism": L3_NAMES[0], "acceptance_performed_by": "module"}
structs = [
    ST("AuthenticationLevelRow", "one row of Table 1: the authentication mechanisms permitted at one FIPS 140-3 security level",
       "§6.2", (292, 292), [R_T1, R_L1, R_L1S, R_ROW2, R_ROW3, R_ROW4], [
        F("level", I(1, 4), "stated", 1, lines=(292, 292), cons=[R_T1, R_L1, R_ROW2, R_ROW3, R_ROW4],
          note="the first column of Table 1: FIPS 140-3 Level 1 to 4"),
        F("authentication_required", BOOL, "stated", False, lines=(295, 297), cons=[R_L1],
          note="false only at Level 1 ('None required'); true at Levels 2 to 4 (schema enforces both)"),
        F("permitted_mechanisms", A(E(*L3_NAMES), uniq=True), "stated", [], lines=(304, 318), cons=[R_ROW2, R_ROW3, R_ROW4],
          note="names are the bullets of the Level 3 cell, taken by script. The Level 2 cell is printed on three lines with the row label "
               "between them (L299, L301, L302): a memorized secret, or a Level 3 mechanism, so its row carries the whole Level 3 list "
               "(derived expansion). The schema pins each level's list to Table 1's exactly; Level 1 lists none"),
        F("if_used_minimum_level", I(2, 2), "should", 2, req=False, cons=[R_L1S],
          note="Level 1 row only (the schema refuses it on any other row): 'If authentication is used, it should meet the requirements of Level 2 as a minimum'; a should, so optional and not enforced on claims")],
       caption=(290, 290),
       extra={"allOf": [
           {"if": {"properties": {"level": {"const": 1}}, "required": ["level"]},
            "then": {"properties": {"authentication_required": {"const": False}}}},
           {"if": {"properties": {"level": {"enum": [2, 3, 4]}}, "required": ["level"]},
            "then": {"properties": {"authentication_required": {"const": True},
                                    "permitted_mechanisms": {"minItems": 1}}}},
           {"if": {"properties": {"level": {"const": 4}}, "required": ["level"]},
            "then": {"properties": {"permitted_mechanisms": {"items": {"enum": L4_NAMES}}}}},
           # Table 1 is a fixed table: each level's row lists exactly what the table lists
           {"if": {"properties": {"level": {"const": 1}}, "required": ["level"]},
            "then": {"properties": {"permitted_mechanisms": {"const": []}}}},
           {"if": {"properties": {"level": {"enum": [2, 3]}}, "required": ["level"]},
            "then": {"properties": {"permitted_mechanisms": {"const": L3_NAMES}, "if_used_minimum_level": False}}},
           {"if": {"properties": {"level": {"const": 4}}, "required": ["level"]},
            "then": {"properties": {"permitted_mechanisms": {"const": L4_NAMES}, "if_used_minimum_level": False}}}]},
       accept=[("Level 1: none required", ROWS[0]["instance"]), ("Level 4: the two multi-factor crypto mechanisms", ROWS[3]["instance"]),
               ("Level 2 row as derived", ROWS[1]["instance"])],
       reject=[("Level 1 requiring authentication", {"level": 1, "authentication_required": True, "permitted_mechanisms": []}),
               ("Level 2 with authentication not required", {"level": 2, "authentication_required": False, "permitted_mechanisms": L3_NAMES}),
               ("Level 3 permitting nothing", {"level": 3, "authentication_required": True, "permitted_mechanisms": []}),
               ("Level 4 permitting Memorized Secret", {"level": 4, "authentication_required": True, "permitted_mechanisms": ["Memorized Secret"]}),
               ("a mechanism Table 1 never lists", {"level": 3, "authentication_required": True, "permitted_mechanisms": ["Biometric"]}),
               ("Level 4 row listing one of its two", {"level": 4, "authentication_required": True, "permitted_mechanisms": L4_NAMES[1:]}),
               ("Level 3 row listing one of its nine", {"level": 3, "authentication_required": True, "permitted_mechanisms": L3_NAMES[:1]}),
               ("Level 1 row listing a mechanism", {"level": 1, "authentication_required": False, "permitted_mechanisms": L3_NAMES[:1]}),
               ("if_used_minimum_level on the Level 3 row", {"level": 3, "authentication_required": True, "permitted_mechanisms": L3_NAMES, "if_used_minimum_level": 2})],
       layout="one JSON object per table row; Table 1 is a two-column table (FIPS 140-3 Level, Authentication)"),
    ST("AuthenticationMechanismClaim", "a vendor's claim that a module authenticates operators with one mechanism at one level",
       "§6.2", (282, 285), [R_COMM, R_T1, R_63B, R_TEST], [
        F("level", I(1, 4), "stated", 3, lines=(282, 285), cons=[R_T1]),
        F("mechanism", S(), "may", L3_NAMES[0], req=False, cons=[R_T1, R_ROW2, R_ROW3, R_ROW4],
          note="required from Level 2 up, and then one of the Table 1 names for that level (schema enforces it); at Level 1 none is required"),
        F("acceptance_performed_by", E("module", "operating_environment"), "stated", "module", req=False,
          lines=(282, 285), cons=[R_T1],
          note="'Except at level 1, operator authentication acceptance is required to be performed by the module or by the Operating Environment'; required from Level 2 up"),
        F("protected_communication_service", BOOL, "may", True, req=False, cons=[R_COMM],
          note="true when the mechanism is employed to establish a module-provided protected communication service"),
        F("meets_sp_800_140c_and_140d_strength", TRUE, "must", True, req=False, cons=[R_COMM],
          note="'these must meet the cryptographic strength requirements of SP 800-140C and SP 800-140D': const true, and required whenever protected_communication_service is true"),
        F("sp_800_63b_requirements_met", BOOL, "should", True, req=False, cons=[R_63B, R_63BSEC],
          note="the first should of %s, with the SP 800-63B sections %s names normative; recommended, not enforced" % (R_63B.split("#")[1], R_63BSEC.split("#")[1])),
        F("justification", S(), "should", "Lockout differs from SP 800-63B 5.2.2 because ...", req=False, cons=[R_63B],
          note="the second should of %s (a justification where an SP 800-63B requirement is not met); a should, so not required by the schema" % R_63B.split("#")[1])],
       extra={"allOf": [
           {"if": {"properties": {"level": {"enum": [2, 3, 4]}}, "required": ["level"]},
            "then": {"required": ["mechanism", "acceptance_performed_by"]}},
           {"if": {"properties": {"level": {"enum": [2, 3]}}, "required": ["level"]},
            "then": {"properties": {"mechanism": {"enum": L3_NAMES}}}},
           {"if": {"properties": {"level": {"const": 4}}, "required": ["level"]},
            "then": {"properties": {"mechanism": {"enum": L4_NAMES}}}},
           {"if": {"properties": {"protected_communication_service": {"const": True}}, "required": ["protected_communication_service"]},
            "then": {"required": ["meets_sp_800_140c_and_140d_strength"]}}]},
       minimal={"level": 1},
       accept=[("Level 4 multi-factor crypto device", {"level": 4, "mechanism": L4_NAMES[1], "acceptance_performed_by": "operating_environment"})],
       reject=[("Level 2 with no mechanism", {"level": 2, "acceptance_performed_by": "module"}),
               ("Level 3 with no acceptance performer", {"level": 3, "mechanism": L3_NAMES[0]}),
               ("Level 4 with Memorized Secret", {"level": 4, "mechanism": "Memorized Secret", "acceptance_performed_by": "module"}),
               ("protected communication without the strength statement", dict(claim_ok, protected_communication_service=True)),
               ("protected communication whose strength is not met", dict(claim_ok, protected_communication_service=True, meets_sp_800_140c_and_140d_strength=False))],
       layout="one JSON object per claim"),
]

HEAD = """# =====================================================================
# nist-sp-800-140e messages -- SP 800-140E defines no message or document
# format. Its one structured artefact is Table 1 (which authentication
# mechanisms are permitted at which FIPS 140-3 level, L290-322), plus prose on
# where acceptance is performed and on the use of SP 800-63B. Two DERIVED
# structures: the Table 1 row, and a vendor's claim checked against it. The
# claim encodes the musts and the shall-like requirement as schema rules and
# leaves the shoulds (SP 800-63B framework, justification) optional.
#
# There are no 'approved' mechanisms: the source says so (L282). Table 1
# lists ALLOWED ones.
#
# Written by schema/build.derived.py; ids resolved by script from requirements.yaml.
# source_digest: %s
# =====================================================================
record: nist-sp-800-140e
reviewed_by: ""
source_digest: '%s'
applicability: 'two derived structures (Table 1 row, mechanism claim); no wire or document format'""" % (SOURCE_DIGEST, SOURCE_DIGEST)


def sreadme(structs, na, nr):
    return generic_schema_readme(structs, na, nr,
        "SP 800-140E has no formal notation. Its one table is Table 1; the rows are in "
        "`../examples/table-1.derived.json`, produced by `build.derived.py` from the source lines and validated "
        "against `AuthenticationLevelRow`.", """
Source defects found while reading: (1) section 5.2 says the modifications follow the format of ISO/IEC
**24579**; every sibling document says 24759. (2) Table 1's Level 2 cell prints 'Memorized secret' before the
row label in the cleaned rendering (lines 299-302), and its mechanism names are capitalised differently from
the Level 3 bullets ('Memorized secret' against 'Memorized Secret'); the schema uses the Level 3 bullet
spelling. (3) 'Level 3 authentication mechanism' in the Level 2 cell is a reference, expanded here to the
nine Level 3 bullets; that expansion is this library's reading.
""")


def extra_examples(validators):
    rows = []
    for r in ROWS:
        q = Q(*r["lines"])
        errs = list(validators["AuthenticationLevelRow"].iter_errors(r["instance"]))
        assert not errs, errs
        rows.append({"level": r["level"], "source_lines": q["source_lines"], "quote": q["quote"],
                     "instance": r["instance"]})
    dump_json(DIST / "examples" / "table-1.derived.json", {
        "_comment": "DERIVED, not verbatim. Table 1 of SP 800-140E as one instance per row; each row names its "
                    "source_lines and the quote written from them, and its instance validates against "
                    "../schema/AuthenticationLevelRow.derived.schema.json (checked by ../schema/build.derived.py). "
                    "The Level 2 mechanism list is this library's expansion of 'Level 3 authentication mechanism'.",
        "rows": rows})
    return {"rows": len(rows)}


def ereadme(structs, na, nr, extras):
    return (FRONT % (ID, "examples", ID, "examples and test vectors") + "# Examples and test vectors\n\n"
            "**Finding: SP 800-140E contains no worked example, sample or test vector.** "
            "Its one table is Table 1 and its caption reads:\n\n" + md(290) + "\n"
            "## Fixtures\n\n"
            "| file | what it is | expected result |\n|---|---|---|\n"
            "| `table-1.derived.json` | the %d rows of Table 1, each with `source_lines`, `quote` and a derived `instance` | every `instance` is accepted by `AuthenticationLevelRow` |\n"
            "| `authentication-cases.derived.json` | this library's cases for both schemas: %d cases, %d `accept` and %d `reject` | each case's `expect` |\n\n"
            "`../schema/build.derived.py` regenerates both files and exits 1 when any case's result differs from "
            "`expect`. The cases are this library's, not the standard's.\n" % (extras["rows"], na + nr, na, nr))


finish(structs, HEAD, "authentication", sreadme, ereadme, extra_examples=extra_examples)
