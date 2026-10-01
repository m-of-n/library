---
record: rfc-8949
kind: schema
title: "rfc-8949 — schemas"
extracted: "2026-09-30"
reviewed_by: ""
---

# rfc-8949 — schemas

RFC 8949 (STD 94) **ships no CDDL and no ABNF of its own.** Its only formal
artifact is the well-formedness pseudocode of Appendix C; §8 declines a formal
definition even for the diagnostic notation ("no formal definition (as in ABNF)
is given in this document"), and the encoding itself is specified by prose plus
Table 1 (§3.1), Table 2 (§3.2.4), Tables 3 and 4 (§3.3), Table 5 (§3.4) and
Table 7 (Appendix B). So the two verbatim files below are the source's formal
material in full, and the two derived files are ours.

| file | covers | kind | source section |
|---|---|---|---|
| `well-formed.pseudocode.txt` | the normative decision procedure for well-formedness: `well_formed()` / `well_formed_indefinite()` (Figure 1), its prerequisites, and the signed-integer encoder (Figure 2) | **verbatim** | Appendix C, in full |
| `initial-byte-jump-table.txt` | Table 7, the whole encoding indexed by initial byte | **verbatim** | Appendix B, in full |
| `cbor-data-model.derived.cddl` | the basic generic data model as CDDL (RFC 8610): major types 0–7, integer ranges, strings, arrays, maps, generic tags, the three float widths, simple values; plus the tag-content restrictions for every tag number this RFC defines | **derived** | §2, §2.1, §3, §3.1, §3.2, §3.3, §3.4, §3.4.1–§3.4.6, §4.1, §5.3, Appendix B |
| `cbor-head.derived.abnf` | the *head* as ABNF (RFC 5234): exactly which of the 256 initial bytes are well-formed, and the 0/1/2/4/8-byte argument width each one selects | **derived** | §1.2, §3, §3.1, §3.2, §3.2.1, §3.3, Appendix B, Appendix F |

Verbatim files carry a header block and then `---- BEGIN VERBATIM ----`;
everything between that and `---- END VERBATIM ----` is byte-identical to the
cached source text and must stay that way. Derived files say `DERIVED` in their
first lines and name the sections they were built from. Nothing in a derived
file may be quoted as the source's own grammar.

## Using the CDDL

RFC 8610 takes the first rule as the root, so `cbor-data-item` is the default:
the basic generic data model of §2, admitting any tag number with any content,
which is what §5.4 requires of a decoder meeting a tag number it does not know.
Validate against `cbor-checked-item` instead when every tag in the fixture is
one this RFC defines — that rule enforces the tag-content restrictions of
§3.4.1–§3.4.6, i.e. the tag validity of §5.3.2, recursively. Individual
`cbor-tag-<n>` rules work as roots for single-tag fixtures.

Two roots are unavoidable: CDDL cannot say "any tag number *except* these", so
a single rule cannot both admit an unknown tag number and reject tag 0 wrapping
an integer — the unconstrained `#6(...)` alternative would match the latter too.

## What no schema here can express

CDDL describes instances of the data model and ABNF describes a regular byte
language. Several of CBOR's rules are neither: they are encoding-level,
value-dependent, or cross-item. These are **stated gaps, not omissions** — each
one lives in `../requirements.yaml` and `../normative.md`, and Figure 1 of
Appendix C decides the well-formedness ones.

- **Definite vs indefinite length (§3.2).** §2 makes serialization variants
  deliberately invisible at the generic data model level, so no CDDL rule can
  tell `[1,2]` encoded `0x820102` from the same item encoded `0x9f0102ff`. The
  ABNF distinguishes the four indefinite *heads*, but the chunk rule of §3.2.3
  (an indefinite-length string may enclose only definite-length strings of the
  same major type) is cross-item and lives only in the pseudocode.
- **Argument width for major types 0–6 (§3)**, and therefore the shortest-form
  requirement of preferred serialization (§4.1) and of core deterministic
  encoding (§4.2.1). The ABNF pins the width a given initial byte selects;
  requiring the *shortest* width that carries the value is a predicate over the
  value and is expressible in neither grammar. Same for the shortest
  float encoding that preserves the value, and for NaN-payload zero-padding
  (§4.1).
- **Map key ordering** — bytewise lexicographic (§4.2.1) or length-first
  (§4.2.3). CDDL maps are unordered.
- **Map key uniqueness.** A map with duplicate keys may be well-formed but is
  invalid (§3.1, §5.3.1); CDDL cannot require distinctness across a
  `* keytype => valuetype` entry.
- **UTF-8 validity of a major type 3 item.** An invalid UTF-8 sequence is
  well-formed but invalid (§3.1, §5.3.1); `tstr` constrains the major type only.
- **Every well-formedness error of Appendix F** except the head-level ones:
  bytes left over, bytes missing, a map with an odd number of items, a "break"
  outside an indefinite-length item or in a map value position. A fixture that
  is not well-formed cannot even be presented to a CDDL schema. The ABNF *does*
  decide the head-level ones by construction — it admits exactly 229 initial
  bytes, excluding reserved additional information 28–30 on every major type,
  additional information 31 on major types 0, 1 and 6, and a two-byte simple
  value whose following byte is below `0x20` (§3.3).
- **The lexical content of tags 0, 32, 33, 34 and 36.** §3.4.1 and §3.4.5.3
  delegate these to the RFC 3339 `date-time` production as refined by RFC 4287,
  to `URI-reference` of RFC 3986, to the RFC 4648 base64url/base64 alphabets and
  padding rules, and to RFC 2045. This record does not hold those productions,
  so the CDDL constrains each tag's content *type* and not its lexis; a
  well-typed but malformed string there is §5.3.2's "inadmissible value for tag
  content".
- **Tag 24 (§3.4.5.1)** requires only that the enclosed byte string encode a
  *well-formed* item; validity of the embedded item is explicitly not required,
  so `cbor-tag-24` is `#6.24(bstr)`. The stricter recursive variant is present
  but unreferenced as `cbor-tag-24-embedded-checked`.
- **Tag 55799 (§3.4.6)** imparts no semantics, and the 0xd9d9f7 self-description
  is a convention about where a tag appears in a stored item, not a shape.
- **Tag and simple-value registries grow (§2.1, §5.4)**, so an unknown tag
  number or simple value must not be treated as invalid. That is why the default
  root is permissive about tag numbers, and why simple values 0–19 and 32–255
  are admitted.

One portability note, written into the CDDL header too: `#7.n` is read here as
selecting on the additional-information value of Table 3, so
`cbor-simple-value-extended = #7.24` covers every simple value 32–255 as one
alternative and individual ones among them cannot be named. Check a tool against
Appendix F before relying on it — `f8 00`, `f8 01`, `f8 18` and `f8 1f` are not
well-formed, while `f8 20` is simple value 32. Likewise a tool that insists on a
tag number after `#6` cannot express `cbor-tag`'s "any tag"; validate such
fixtures against `cbor-checked-item` or a `cbor-tag-<n>` rule instead.

## Checks run on these files

- The verbatim regions were diffed against lines 3089–3193 and 2938–3087 of the
  cached source: byte-identical.
- The CDDL was checked mechanically for duplicate rule names, references to
  undefined rules, and redefinition of an RFC 8610 prelude name: none. 44 rules;
  the three unreferenced ones (`cbor-boolean`,
  `cbor-tag-24-embedded-checked`, `cbor-tag-not-for-interchange`) are deliberate
  and documented in place.
- The ABNF's admitted initial-byte set was rebuilt from its terminals and
  compared against the set derived independently from §3 and §3.3: 229 bytes,
  no extras, none missing; argument widths 0/1/2/4/8 and float widths 2/4/8 as
  §3 and Table 3 require.
- No CDDL or ABNF validator is installed in this workspace, so **neither derived
  file has been run through a real parser**, and that remains the first job for
  anyone who has one. What pass 3 did instead is weaker but not nothing: it
  transcribed `cbor-data-model.derived.cddl` rule for rule into a structural
  validator, paired it with a well-formedness checker written from Figure 1 of
  Appendix C, and ran both over all 232 vectors of `../examples/vectors.yaml`.
  All 131 well-formed vectors validate against both roots, all 101
  not-well-formed ones are refused, and every initial byte in the corpus is
  classified by the ABNF as the corpus expects. That exercises the *content* of
  the rules; it does not prove either file is syntactically acceptable to
  `cddl` or to an RFC 5234 tool. `../examples/README.md` records which rules no
  vector reaches.
- Pass 3 re-ran the mechanical rule audit above on the edited file: still 44
  rules, no duplicates, no reference to an undefined rule, no prelude name
  redefined, and the same three deliberately unreferenced rules.
- Pass 3 found and removed one unsupported assertion: `cbor-tag-35` had narrowed
  tag number 35's content to `tstr`, which no statement of RFC 8949 supports —
  §3.4.5.3 says only "string value" and Appendix G says the document does not
  define the tag. It now reads `tstr / bstr`. See "Open questions" item 14 in
  `../design-notes.md`.
