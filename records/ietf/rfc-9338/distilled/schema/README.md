---
record: rfc-9338
kind: schema
title: "rfc-9338 — schemas"
extracted: "2026-10-20"
reviewed_by: ""
---

# `schema/` — RFC 9338's CDDL, and what this library had to add

**Five files: two verbatim, three derived.** The naming convention is
`docs/extraction.md`'s — `.derived.` is mandatory in the filename, an unmarked
name asserts the source's own bytes, and every file repeats the claim in its
header.

| file | kind | what it is |
|---|---|---|
| `rfc9338.cddl` | **verbatim** | All 5 CDDL fragments RFC 9338 prints — 8 rules — cut from `.cache/rfc-9338.txt` by line range by script, in the document's own order, each with its line range and its own sha256. **Erratum 7338 is present and is not repaired**, so this file does not parse |
| `source-renderings.txt` | **verbatim** | The same 5 regions as exact runs of source lines with the RFC's own indentation, plus erratum 7338's Original and Corrected Text as the RFC Editor's errata page prints them |
| `countersign-structure.derived.cddl` | **derived** | The repaired, self-contained grammar: erratum 7338 applied, the RFC 9052 imports supplied and marked, dedented. Nothing renamed, reordered or tightened |
| `countersign-structure.derived.schema.json` | **derived** | A machine-checkable rendering of §3.3's `Countersign_structure` as a 4-branch `oneOf`. `$id: urn:library:rfc-9338:countersign-structure.derived` |
| `bstr-slot-census.derived.txt` | **derived** | **The file the whole record turns on.** The `bstr`-slot count of all eight permitted target structures, derived by script from RFC 9052's verbatim CDDL |

## Two defects in the source's grammar, one of them with no erratum

**1. It does not parse — erratum 7338.** *Reported*, Technical, §3.3, Carsten
Bormann, 2023-02-06; errata searched 2026-10-20 and this is the **only** erratum
on RFC 9338. The `context` choice ends `"CounterSignature0V2" /,` — a choice
operator with no right operand. RFC 8610 Appendix B, held verbatim in this
library at `records/ietf/rfc-8610/distilled/schema/cddl.abnf` line 141, gives
`type = type1 *(S "/" S type1)`, so a trailing `/` requires a following `type1`
and the fragment is a syntax error, not a warning.

**2. It does not stand alone, and no erratum covers that.** §1.2 promises that
*"The collected CDDL can be extracted from the XML version of this document via
the XPath expression below"* and prints the expression. Run it and the result
references **two names it does not define**:

| dangling name | defined in | reached from |
|---|---|---|
| `COSE_Signature` | RFC 9052 §4.1 | `COSE_Countersignature = COSE_Signature` (§3.1) |
| `empty_or_serialized_map` | RFC 9052 §3 | `body_protected` and `sign_protected` in `Countersign_structure` (§3.3) |

So even with erratum 7338 applied the extracted file fails **name resolution**,
and a tool that only checks syntax would report one defect and a tool that
resolves names reports both. The document says the grammar exists for *"the
automated validation tools used during the writing of this document"*.
`countersign-structure.derived.cddl` supplies both imports from this library's
verbatim capture of RFC 9052's CDDL and marks them `IMPORTED`.

## A third defect, between the CDDL and the prose

§3.3's four prose bullets pair each `context` string with the presence or
absence of `other_fields`. **The CDDL states neither half of that pairing**: it
makes `context` a free choice of all four strings and `? other_fields`
independent, so the source's own grammar admits `"CounterSignature"` *with*
`other_fields` and `"CounterSignatureV2"` *without* — both of which the prose
forbids. The pairing exists only in
`countersign-structure.derived.schema.json`'s `oneOf`, which is therefore
**stricter than the source's grammar and exactly as strict as its prose**, and
the file says so in `x-derived-notes`.

And `payload : bstr` is **mandatory** in the CDDL while four of the eight
permitted target structures have no payload field. That is left alone: it is an
under-specification to record, not a defect to patch. `../design-notes.md` §3.4.

## Why the census is a file and not a table in prose

RFC 9338 states the `other_fields` outcome for **one** structure, `COSE_Sign1`,
as an example. For the other seven it is arithmetic nobody performs in the
document, and getting it wrong changes which bytes are signed. So the count is
done by script, from the member lists and type expressions of
`records/ietf/rfc-9052/distilled/schema/cose.cddl` — including the
classification of `protected`, which is read off that file's own
`empty_or_serialized_map = bstr .cbor header_map / bstr .size 0` rather than
asserted.

The census prints **two** columns, `slot-bstr` and `wire-bstr`, and **they
disagree for five of the eight structures**. §3.3's own COSE_Sign1 example
forces the `slot` reading; the `wire` column is printed because the gap between
them *is* the detached-payload hazard.
