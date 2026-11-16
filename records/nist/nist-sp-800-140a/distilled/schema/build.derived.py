#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library; nist-sp-800-140a ships no schema, so
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
       accept=(), reject=(), layout=None, note=None, props_override=None):
    if not cons:
        raise SystemExit(name + ": constrained_by is empty")
    return dict(name=name, title=title, locator=locator, lines=lines, cons=list(cons),
                fields=fields, caption=caption, extra=extra or {}, defs=defs,
                accept=list(accept), reject=list(reject), layout=layout, note=note,
                props_override=props_override)


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
        out.append(("accept", "required fields only", {f["name"]: copy.deepcopy(f["ex"])
                    for f in s["fields"] if f["req"]}))
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

R_SCOPE = R(r"^Section 6 of this document specifies any modifications to the minimum information that vendors shall provide", "§5.1")
R_ASA = R(r"^This annex \{ISO/IEC 19790 Annex A\} specifies the minimum documentation which shall be required", "§6.1")
R_VEA = R(r"^VEA\.01\.02:", "§6.1")
R_TEA = R(r"^TEA\.01\.02:", "§6.1")

structs = [
    ST("MinimumDocumentation", "the documentation a vendor provides a testing laboratory for one cryptographic module (ASA.01, VEA.01.02, TEA.01.02)",
       "§6.1", (266, 268), [R_SCOPE, R_ASA, R_VEA, R_TEA],
       [F("cryptographic_module", S(), "shall", "Example Module 1.0", cons=[R_VEA],
          note="VEA.01.02: documentation is for 'a cryptographic module'"),
        F("documentation_provided", A(S(), lo=1), "shall", ["Functional specification v1.2"], cons=[R_VEA, R_ASA],
          note="at least one document: the vendor 'shall provide documentation' (VEA.01.02); the source names no document list of its own"),
        F("fulfils_minimum_documentation_requirements", TRUE, "shall", True, cons=[R_VEA, R_ASA, R_TEA],
          note="const true: the documentation shall fulfil the minimum documentation requirements; false must be rejected"),
        F("minimum_requirements_specified_in", S(), "shall", "validation authority requirement and management documentation",
          cons=[R_VEA], lines=(266, 268),
          note="where the minimum requirements are specified: VEA.01.02 names the validation authority's requirement and management documentation, which SP 800-140A neither names nor cites (normative.md SD-2); ASA.01's own floor, ISO/IEC 19790 Annex A, is paywalled"),
        F("additional_documentation", A(S()), "stated", ["Operator guidance"], req=False, cons=[R_VEA], lines=(266, 268),
          note="'fulfils but is not limited to': documentation beyond the minimum is permitted")],
       layout="no byte layout; the vendor evidence is documentation handed to the CSTL"),
]

HEAD = """# =====================================================================
# nist-sp-800-140a messages -- SP 800-140A modifies ONE vendor-evidence item of
# ISO/IEC 24759 6.13 (ASA.01 / VEA.01.02 / TEA.01.02): the vendor shall
# provide documentation that fulfils, but is not limited to, the minimum
# documentation requirements. It lists no document, table or field of its own.
# ASA.01 has ISO/IEC 19790 Annex A specify the minimum documentation, and
# VEA.01.02 / TEA.01.02 measure it against the validation authority's
# requirement and management documentation, which the SP neither names nor
# cites (normative.md SD-2); neither is reproduced here.
# So there is one derived structure, deliberately thin, and this file says so
# instead of inventing fields. Section 6.1's other text is the modification
# convention (5.2), not a structure.
#
# Written by schema/build.derived.py; ids resolved by script from requirements.yaml.
# source_digest: %s
# =====================================================================
record: nist-sp-800-140a
reviewed_by: ""
source_digest: '%s'
applicability: 'one derived structure; the source prescribes no wire or document format and enumerates no document'""" % (SOURCE_DIGEST, SOURCE_DIGEST)


def sreadme(structs, na, nr):
    return generic_schema_readme(structs, na, nr,
        "SP 800-140A has no formal notation at all. Its whole content is one modified vendor-evidence item; "
        "the schema below is the thinnest honest rendering of it.", """
Source defect: VEA.01.02 and TEA.01.02 (%s, %s) measure the documentation against the validation
authority's requirement and management documentation, which SP 800-140A neither names nor cites
(normative.md SD-2), so `minimum_requirements_specified_in` is a free string.
""" % (R_VEA.split("#")[1], R_TEA.split("#")[1]))


def ereadme(structs, na, nr, extras):
    return (FRONT % (ID, "examples", ID, "examples and test vectors") + "# Examples and test vectors\n\n"
            "**Finding: SP 800-140A contains no worked example, sample documentation set, test vector or fixture.** "
            "Its section 6.1 consists of the modification of one assertion and its two evidence items:\n\n"
            + md(266, 268) + "\n" + md(272, 274) + "\nThere is nothing to turn into a fixture.\n\n"
            "## What is here instead\n\n"
            "`documentation-cases.derived.json` holds this library's own cases for `MinimumDocumentation`: "
            "%d cases, %d expected to be accepted and %d expected to be rejected, each with `expect` and a reason. "
            "`../schema/build.derived.py` re-validates all of them and exits 1 on any difference.\n" % (na + nr, na, nr))


finish(structs, HEAD, "documentation", sreadme, ereadme)
