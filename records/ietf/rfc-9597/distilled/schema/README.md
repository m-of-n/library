---
record: rfc-9597
kind: schema
title: "rfc-9597 — schemas"
extracted: "2026-10-20"
reviewed_by: ""
---

# Schemas

**RFC 9597 ships exactly one grammar fragment — four lines of CDDL — and
declares it non-normative in the sentence immediately before it.** That
sentence is the most important fact in this directory, so the verbatim capture
reproduces **both together** and never the fragment alone:

> The following is a non-normative description for the value type of the CWT
> claim header parameter using CDDL [RFC8610].

Measured over all 265 lines: `CDDL` occurs **twice** (that sentence and the
reference entry); `ABNF`, `ASN.1` and `JSON Schema` occur **zero** times.

| file | kind | what it is |
|---|---|---|
| `source-renderings.txt` | **verbatim** | two regions: §2's Table 1 (the IANA registration of label 15) and the non-normative declaration together with the CDDL fragment it governs. Each with its line range and its own `sha256` |
| `cwt-claims-header.derived.cddl` | derived | what §1's and §2's **normative** sentences fix, which the source's CDDL does not contain: the label, the three conformant placements, and a named list of what CDDL cannot express |
| `cwt-claims-header.derived.schema.json` | derived | a JSON-projection schema for fixture validation. `$id: urn:library:rfc-9597:cwt-claims-header.derived` |

## Why a derived CDDL exists at all, when the source has one

Because the source's fragment constrains **nothing** and the document says so.
`CWT-Claims = { * Claim-Label => any }` with `Claim-Label = int / text` admits
the **empty map**, admits any label the union covers, and forbids nothing. Every
load-bearing rule in RFC 9597 is in prose that its own CDDL omits:

- **placement** — `RECOMMENDED` protected, `MUST` occur at most once across the
  two buckets (§2);
- **duplication** — header and payload claims `MUST` be identical, *unless*
  (§2);
- **use** — a recipient `MUST NOT` use the information beyond the protection
  afforded (§1).

The derived CDDL carries the first of those three as three enumerated shapes,
**including the conformant-but-unsigned one**, and names the other two as a
profile's job. The second and third are not expressible: one is a
cross-structure equality predicate scoped to a classification `rfc-8392` §6
declines to define, and the other is a constraint on *use* rather than on bytes.

**Those three shapes are complete only under reading 1 of the placement
`MUST`** — *at most once across the two buckets* — which is
`../design-notes.md`'s `D-6`: the sentence admits three readings and the
document disambiguates none. Under D-6's reading 2, *at most once per bucket*, a
fourth shape is conformant (label 15 in both buckets, once each) and the
enumeration is incomplete rather than wrong. The `.cddl` now states which
reading it encodes, at the top of its placement block. *[added 2026-10-21,
pass 3 — cross-check: pass 2 found D-6 and recorded it in three files, none of
them in this directory, so the two files the ambiguity is actually about did not
mention it.]*

## What the derived schemas deliberately do not constrain

- **Which claims must be present.** RFC 9597 requires none. `rfc-9943` §6 is
  the only ratified profile this library holds that does — label 15 in the
  **protected** header with `iss` (1) and `sub` (2).
- **The label space.** `int / text`, flat and global, with no key component.
  `ARCH-0002 P1` wants `(defining key, label)` and nothing here can express it.
- **"Identical".** §2's duplication rule turns on a word the document does not
  define. Byte equality of the encoded items, or equality of the CBOR data
  items? A preferred and a non-preferred encoding of the same integer are one
  value and two byte strings, and a verifier comparing bytes and one comparing
  values disagree on inputs neither would call malformed.

## Derived-vs-verbatim

`.derived.` is mandatory on anything this library wrote and an unmarked name
asserts the source's own bytes (`docs/extraction.md`).
`source-renderings.txt` is the only unmarked file here. `bin/validate` checks
the name against the header marker in each file's first 12 lines, and the `$id`
of every `*.derived.schema.json`.
