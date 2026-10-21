---
record: rfc-9054
kind: schema-index
title: "rfc-9054 — schema artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# `distilled/schema/` — RFC 9054

**RFC 9054 never uses the word "CDDL", and prints two CDDL fragments.**
Measured over all 498 lines: `CDDL`, `ABNF`, `JSON Schema`, `schema` and
`grammar` occur **zero** times; `ASN.1` occurs once, at line 77, in the sentence
saying COSE has no `DigestedData` equivalent. RFC 8610 appears in **neither**
the normative nor the informative references. So the grammar the fragments are
written in is nowhere identified by the document, and the erratum that corrects
one of them has to appeal to a specification the RFC does not cite.

| file | kind | what it is |
|---|---|---|
| `cose-hash-structures.cddl` | **verbatim** | source lines 211–216 and 224–227, byte for byte, **with erratum 7335 intact** |
| `source-renderings.txt` | **verbatim** | Tables 1–3, the four-field prose bullets, and the SHA-256/64 NOTE — 5 regions with line ranges and sha256 |
| `cose-hash.derived.cddl` | derived | the two fragments with erratum 7335 applied, the map wrapper the document never supplies, and this library's own structure |
| `hash-algorithms.derived.yaml` | derived | the eight registry rows as data, each with its CBOR encoding computed |
| `cose-hash.derived.schema.json` | derived | `$id: urn:library:rfc-9054:cose-hash.derived`; a JSON projection for fixtures only |
| `cddl-parse.derived.txt` | derived | the output of running RFC 8610 Appendix B's grammar against both fragments |

## The headline, and it corrects this record's own summary

`summary.md` says of `COSE_Hash_V` that *"the fragment does not parse"*. **It
parses.** `#` is CDDL's tag operator (`type2 = … / "#" DIGIT ["." uint] / "#"`),
not a comment marker — RFC 8610 Appendix B gives `COMMENT = ";" *PCHAR CRLF` —
so each `#` is read as the "any" type and each comment word after it as a bare
type reference. **The grammar sees 24 group entries where four were written**,
with 15 distinct undefined names: `Algorithm`, `identifier`, `Hash`, `value`,
`Location`, `of`, `object`, `that`, `was`, `hashed`, `containing`, `other`,
`details`, `and`, `things`. None begins with `$`, so RFC 8610 §3.9's socket
convention does not silence them and a tool rejects the file **at name
resolution**. With erratum 7335 applied the count is zero.

**And the defect no erratum covers is the worse one.** Even repaired,
`COSE_Hash_V` is a parenthesised **group**: forced as a type rule it fails
after 14 characters, because a parenthesised `type` cannot contain member keys.
RFC 8610 §2.2.4 — *"there is no way to use a group as a root -- it must be a
type"*, as `records/ietf/rfc-8610/distilled/schema/grammar-gaps.derived.txt`
quotes it at G-04 — therefore forbids it as a root, and the member keys mean the
only legal wrapper is a map (G-03). **RFC 9054 never supplies one.**
`cose-hash.derived.cddl` does, with the round-trip to the verbatim bytes
asserted by its generator.

`COSE_Hash_Find`, by contrast, parses **as printed** and as a **type** rule.
Of the two structures the document offers, one works.

## And it is already `rfc-9360`'s type

`COSE_Hash_Find = [ hashAlg : int / tstr, hashValue : bstr ]` against
`rfc-9360` §2's `COSE_CertHash = [ hashAlg: (int / tstr), hashValue: bstr ]`:
same member key names, same types, same order, differing by one pair of
parentheses around a single `/` expression. `../examples/vectors.yaml` V-0006
encodes the same *(algorithm, digest)* pair under both for all eight algorithms
and they are **byte-identical every time**. Same working group, same author, six
months apart, and **neither cites the other's structure**.

## What the derived files are for

`hash-algorithms.derived.yaml` exists because the document's eight rows are
spread over three tables in three subsections with three different column
layouts, and because the measurement §4.1 invites is not in the document: the
CBOR cost of each identifier, which contradicts §4.1's own rationale for five
of eight.

`cose-hash.derived.cddl`'s second half is this library's own digest structure,
and it is there to make the `R-O-03` position explicit: the **algorithm** is
citable (`-16`), and the **carrier** is an invention with nothing to cite,
because §1 says COSE defines none and that the omission was intentional.
