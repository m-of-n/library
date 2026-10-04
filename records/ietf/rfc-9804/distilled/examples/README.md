---
record: rfc-9804
kind: examples
title: "rfc-9804 — examples and test vectors"
extracted: "2026-10-04"
reviewed_by: ""
---

# RFC 9804 — examples and test vectors

`vectors.yaml` holds **78 vectors**, every example RFC 9804 prints, in source
order. Each carries its locator, what the source says it denotes, and a
`fidelity` marker saying how close the `input` is to the printed characters.
Anything this extraction worked out rather than read sits under `derived:` with
`in_source: false`, never mixed into `input` or `expected`.

The file's own header documents the conventions: the `input_lines` sequence for
multi-line examples (`bin/_yaml.py` has no block scalars — library#43), the
quoting rules, the margin-stripping rule, and the `equiv_group` / `same_sexp_as`
/ `linkage` cross-form links.

## Coverage

| source section | vectors | ids |
|---|---|---|
| §1 Introduction | 1 | `SEXP-1-01` |
| §2 Informal introduction | 6 | `SEXP-2-01` … `-06` |
| §4.1 Verbatim | 6 | `SEXP-41-01` … `-06` |
| §4.2 escape-convention table | 17 | `SEXP-42-E01` … `-E17` |
| §4.2 examples | 8 | `SEXP-42-01` … `-08` |
| §4.3 Token | 6 | `SEXP-43-01` … `-06` |
| §4.4 Hexadecimal | 4 | `SEXP-44-01` … `-04` |
| §4.5 Base-64 of an octet-string | 6 | `SEXP-45-01` … `-06` |
| §4.6 Display-hints | 9 | `SEXP-46-01` … `-09` |
| §5 Lists | 5 | `SEXP-5-01` … `-05` |
| §6.2 Canonical | 5 | `SEXP-62-01` … `-05` |
| §6.3 Basic transport | 2 | `SEXP-63-01`, `-02` |
| §9.2 Array-layout memory | 3 | `SEXP-921-01`, `SEXP-922-01`, `SEXP-923-01` |
| **total** | **78** | |

**The three sections with no vectors, and why.** §3 enumerates character
classes rather than examples; §7 is the ABNF, held verbatim in
`../schema/`; §9.1 describes the list-structure memory representation in prose
and prints no layout at all. Every other section of the body is represented.

**Count correction.** This file's header claimed `vector_count: 99` until pass
3. Pass 1 was interrupted after writing seven vectors — the file stopped at
`SEXP-2-06` while its own conventions section already referred forward to
`SEXP-42-E09`, `SEXP-44-03`, `SEXP-45-02`, `SEXP-42-07` and `SEXP-63-02`, and
five vectors carried `same_sexp_as` links to ids that did not yet exist. Pass 3
completed the set and recounted from the source; 78 is the enumerated total and
`count_reconciliation` in the file records the arithmetic. 99 matches no
enumeration of this document and is treated as an estimate, not as evidence of
21 vectors still missing.

## Source defect found — §4.6

**`SEXP-46-01` does not decode to what its prose says, and this is a defect in
RFC 9804, not in the extraction.**

§4.6 introduces its display-hint example by saying the octet-string represents
*"böb☺"*, that is *"bob" with an umlaut over the "o"*, followed by U+263A WHITE
SMILING FACE. It then prints:

```
["text/plain; charset=utf-8"]"b\xC3\xB7b\xE2\x98\xBA"
```

`\xC3\xB7` is the octets `0xC3 0xB7`, which in UTF-8 is **U+00F7 DIVISION
SIGN**. The example therefore decodes to `b÷b☺`. The letter *o with umlaut* is
U+00F6, encoded `0xC3 0xB6` — the example has `B7` where it needs `B6`, a
single-digit error. The second escape is correct: `\xE2\x98\xBA` is U+263A,
exactly as the prose states.

Verified by decoding the octets, not by reading them. The vector records both
the printed bytes (verbatim, as `input`) and the mismatch (under `derived:`),
and repairs nothing.

This is the same class of defect as the U+FB33 corruption recorded in the
`rfc-8785` record, and carries the same lesson: a test vector inside a
canonicalisation document that does not decode to what its own prose claims
propagates silently into every implementation that copies it. It is not
mentioned in RFC 9804's errata as of the retrieval date; see `design-notes.md`
open question 5 for the companion §10 grammatical slip, which is cosmetic where
this one is not.

## The vectors that earn their place

Eight, for a test harness built on this record.

1. **`SEXP-41-03`** — `4:::":`  Four payload octets, every one of them
   punctuation that another representation would have to escape. Catches a
   parser that stops at the first colon or treats `"` as a delimiter.
2. **`SEXP-62-04`** — `10:foo)]}>bar`  Payload contains `)`, `]`, `}` and `>`.
   Catches a parser scanning for a matching delimiter instead of counting
   octets. The vector `design-notes.md` cites for escape-free framing.
3. **`SEXP-42-04`** — `"\xFE is the same octet as \376"`  The source writes one
   octet two ways inside a single literal. The clearest demonstration in the
   document of why a canonical form is needed.
4. **`SEXP-42-05`** — `3"\n\n\n"`  Length 3 against six printed characters.
   Catches a parser counting raw characters rather than decoded octets.
5. **`SEXP-44-03`** — whitespace split **inside an octet pair**, `6` ending one
   line and `2` beginning the next. Catches a parser that strips whitespace
   only between pairs.
6. **`SEXP-45-05`** — `|YWJjZA|`  Unpadded. Emitting it is non-conforming
   (`R-0028`); accepting it is merely permitted (`R-0029`). Two conforming
   parsers may legitimately disagree, and the source prints it as valid.
7. **`SEXP-46-09`** — the default display-hint. The condition-1 vector: an
   explicit `[24:application/octet-stream]` and no hint at all are the same
   value to an application applying the default, and have **different canonical
   forms**. See `design-notes.md` condition 1.
8. **`SEXP-63-02`** — the brace-wrapped base-64 of `(1:a1:b1:c)`. The
   condition-2 vector: one S-expression, two octet sequences, and `R-0045`
   obliges a conforming implementation to accept both.

## What was checked, and how

Pass 3, mechanically:

- **Every `same_sexp_as` target resolves** to an id defined in the file. Zero
  dangling references across all 78 vectors.
- **Ids are unique**, and every vector has both an `input` (or `input_lines`)
  and an `expected`.
- **Base-64 round-trips.** `SEXP-63-02` decodes to exactly `(1:a1:b1:c)`:
  base64 of those eleven octets is `KDE6YTE6YjE6Yyk=`, matching the source once
  the ignorable whitespace is removed, with one equals sign as `R-0027`
  requires for remainder two.
- **Every §9.2 length field verified by addition.** `SEXP-922-01`: declared
  `0x000d` = 13 = (1+2+3) + (1+2+4). `SEXP-923-01`: inner `0x0005` = 5 =
  (1+2+1) + 1; outer `0x001b` = 27 = 6 + 12 + 8 + 1. All consistent — **no
  defect in the §9.2 examples.**
- **The §4.6 UTF-8 example decoded**, which is how the defect above was found.
- **Quoting linted** for un-doubled apostrophes in single-quoted scalars and
  un-escaped interior double quotes. Zero problems. `SEXP-42-E09` remains the
  one value containing both a backslash and an apostrophe, and its `yaml_note`
  records that `bin/_yaml.py` returns one extra apostrophe for that value alone.

Not checked, because the document supports no such check: there is no
reference implementation here, so no vector has been round-tripped through a
parser. The canonical forms under `derived:` were produced by applying §6.2 by
hand and are marked `in_source: false` throughout.
