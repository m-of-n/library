---
record: draft-ietf-cbor-serialization
kind: examples
title: "draft-ietf-cbor-serialization — examples and test vectors"
extracted: "2026-10-18"
pass: 1
reviewed_by: ""
---

# CBOR Serialization and Determinism — examples and test vectors

`vectors.yaml` holds **105 vectors**: every encoded byte string printed anywhere
in draft-ietf-cbor-serialization-08, in source order, with no gaps.

| where | vectors | what |
|---|---|---|
| §1, Table 1 | 2 | `[1, 2]` definite vs indefinite — the document's opening illustration |
| §3 | 6 | the bullet list of what general serialization permits |
| §4.1 item 4 | 3 | the float rule's own worked examples: `0.0`, `0.1`, the canonical NaN |
| §9.1 | 5 | the covert-channel enumeration: the value `1` in all five argument widths |
| Appendix L.2 | 89 | the 25 `.edn` example files, every encoding in each |
| **total** | **105** | |

Of the 89 from Appendix L.2, each is one row of one file's
`general-serializations` list — which in all 25 files is a superset of that
file's `preferred-plus-serializations` and `deterministic-serialization`
lists, so iterating the general list reaches every encoding the document
prints.

## `expect` needs a denominator, and this is it

This document defines no format that bytes can be well-formed or ill-formed
against. It defines **three nested serializations** — general (§3),
preferred-plus (§4), deterministic (§5) — and *every* byte string it prints is
well-formed, valid CBOR and valid general serialization. The source says so
itself: "All examples are well-formed and valid" (Appendix L.1).

So a bare valid/invalid verdict would be meaningless. Each vector carries:

| field | meaning |
|---|---|
| `expect` | the verdict under **preferred-plus**, which §4.3 calls "the recommended default" |
| `conformance.general` | always `valid` — see above |
| `conformance.preferred_plus` | same as `expect` |
| `conformance.deterministic` | preferred-plus **plus** map key ordering |
| `violates` | why `expect` is `invalid`, cited by section. Present on every `invalid` |
| `violates_deterministic` | present only where deterministic rejects what preferred-plus accepts — which can be for exactly one reason, §5.1 item 2 |

The split:

| serialization | valid | invalid |
|---|---|---|
| general | 105 | 0 |
| preferred-plus | 41 | 64 |
| deterministic | 31 | 74 |

The 10 vectors that are valid preferred-plus and invalid deterministic are the
unsorted maps, and they are the **only** difference between the two modes in
the entire corpus. That is not an artefact of the vector set; it is the
document's claim: "The only difference between preferred-plus and deterministic
serialization is that in deterministic serialization, maps are required to be
sorted by their keys" (§5.3.2). The vectors confirm it exhaustively.

### `invalid` means "a checking decoder must reject this"

Not "no decoder will read it". Appendix H defines the optional conformance
pass, and Appendix L.1.3 defines the test these negative vectors drive: "for
each example, supply the decoder with every representation permitted under
general serialization except those allowed for the target serialization type.
Decoding each such input must result in a conformance-checking error."

A **non**-checking preferred-plus decoder may well accept them, and Appendix
L.1.4 expects it to: "It is common for preferred-plus and deterministic
decoders to accept non-shortest-length arguments." Nothing in §4.2 requires a
decoder to reject anything. The negative vectors therefore test the *checking*
mode, and that is why there are more of them than positive ones.

## Provenance: every byte is the document's

**All 105 hex strings are printed in the source. None is computed by this
library.** The document gives bytes for every example it states, including the
ones buried in prose, so no vector had to be reconstructed from a diagnostic
form — the honesty rule that forces a `notes` disclosure never fired.

Checked mechanically: 103 of the 105 appear in the cached text as a contiguous
hex string — as an `h''` literal in Appendix L.2, or after `0x` in the prose
sections — and were matched against it by script. Two normalisations, neither
touching a byte:

- **Letter case.** §9.1 writes two of its five encodings with uppercase hex
  digits (`0x1A00000001`, `0x1B0000000000000001`). Everything here is lower
  case.
- **Rejoining, for V-0001 and V-0002 only.** Table 1 prints their bytes spaced
  *and* wrapped across two lines of a table cell — `0x82 0x01` on source line
  186 and `0x02` on line 187; `0x9f 0x01` on 189 and `0x02 0xff` on 190. Both
  vectors say so in their own `notes`.

**And every one was decoded.** An independent CBOR decoder re-derived each
value and each per-serialization verdict from the bytes, and the generator
aborts if a verdict stated in the file is not the one the decoder computes. The
`decoded` text is therefore checked against the source's EDN rather than copied
from it.

### The verdicts reproduce the author's own classification exactly

The strongest check available, and it passes: for all **25** Appendix L.2
files, the set of encodings this file marks `preferred_plus: valid` is
**identical** to that file's own `preferred-plus-serializations` list, and the
set marked `deterministic: valid` is identical to its
`deterministic-serialization` list. Zero mismatches, 34 and 24 encodings
respectively. The verdicts were *computed* from §4.1 and §5.1 by a decoder that
had never seen those lists, so this is an independent agreement rather than a
transcription. Counted mechanically, the appendix prints 148 `h''` literals, 90
of them distinct: the 89 encodings here, plus `h'010203'`, which is
byte_string.edn's unencoded EDN *value* and is recorded as the `diagnostic` of
V-0037 … V-0039 rather than as a vector. Nothing in Appendix L.2 is unaccounted
for.

In each of the 25 files the `general-serializations` list is a superset of the
`preferred-plus-serializations` list, which is in turn a superset of the
`deterministic-serialization` list — also checked, in all 25. Three byte strings the source prints only as a diagnostic *value* —
`0x1ff` as a NaN significand at three widths — were confirmed arithmetically:
`0x1ff << 13 = 0x3fe000` and `0x1ff << 42 = 0x7fc0000000000`, matching
`fa7fbfe000` and `fb7ff7fc0000000000`.

## Six hex strings appear twice, on purpose

`00`, `1800`, `190000`, `f90000`, `fa00000000` and `f97e00` each appear as both
a prose example and an Appendix L.2 vector, and `f90000` appears three times
(§3, §4.1, float_zero.edn). They are separate vectors because they are separate
examples in the source with different locators and different force — §4.1's
`f90000` is the one place the document states the reduction as a **MUST**,
while float_zero.edn's is a fixture. Each says so in its notes.

## What the vectors do *not* cover

The 25 files are a deliberate subset, and the source says which: "They cover
only what is defined in this document and therefore do not provide complete or
general CBOR test coverage" (Appendix L.1). Specifically absent:

- **No vector for the 8-byte argument as a *shortest* form** except
  `3bffffffffffffffff` (65_bit_neg.edn). Since §4.1 item 1 never states the
  8-byte case at all (see below), nothing tests the boundary at 2^32.
- **No vector for `0.1`** in Appendix L.2 — the document's only
  precision-irreducible float lives in §4.1 prose and is V-0010 here. The
  Appendix L.2 double vector (`1.7976931348623157e+308`) is irreducible for
  *range* instead, which exercises a different branch of Appendix D's code.
- **No conforming map with keys of differing encoded length — so the corpus
  cannot tell the right sort order from the wrong one.** This is the sharpest
  gap in the set, and it was measured rather than guessed. §5.1 item 2 goes out
  of its way to say which sort it is *not* ("not the same as Section 3.9 of
  [RFC7049] / Section 4.2.3 of [STD94]", the length-first order), yet of the 16
  map encodings in the document the two orders disagree on exactly **one** —
  `bf7f6161626263ff017f6264656166ff027f63676869ff03ff` (map_strings.edn), whose
  keys are indefinite-length text strings of 7, 7 and 6 bytes. And that
  encoding is rejected by both preferred-plus and deterministic serialization
  anyway, for its indefinite framing (§4.1 items 2 and 3), so no conformance
  test built from these fixtures ever reaches the distinction. All 12
  preferred-plus-valid map encodings have keys of equal length (1 byte in
  map.edn, 4 in map_strings.edn). **A library that implements the RFC 7049
  length-first sort passes this entire test suite.**
- **No duplicate-key vector**, because the document states no duplicate-key
  rule (see the schema README).
- **No Unicode vector.** §9.1 lists "Varying the Unicode representation of text
  strings" as a surviving covert channel and Appendix B raises normalization as
  protocol-design advice, but no rule and no fixture address it.
- **No negative-zero vector** at any width, although `-0.0` is exactly the kind
  of value the shortening rule has to get right.
- **No tag-2 boundary vector.** negative_bignum.edn pins the tag 3 floor at
  nine content bytes; there is no tag 2 equivalent (the smallest positive big
  number, 2^64, as `c249010000000000000000`).

## Three examples in the source are not data items, and so are not vectors here

Held elsewhere rather than dropped:

| source | what | where it lives |
|---|---|---|
| §6 | the worked special-serialization specification text ("Deterministic serialization MUST be used, except that maps and arrays MUST be encoded with indefinite lengths…") | `../requirements.yaml` R-0060 … R-0062, and `../messages.yaml` under `indefinite-length-head` |
| §8 | the two CDDL examples of `.serial` | `../schema/serial-control-operator.cddl`, verbatim |
| App. B | the two hypothetical application-layer specifications (the birth date; the fluid level measurement) | `../requirements.yaml` R-0072 … R-0075 |

Appendix D's C code is likewise an example — "Figure 1: Example C Code" — and
is held verbatim as `../schema/pref-plus-float.c`.

## Source issues these vectors expose (recorded, not repaired)

1. **§3 says `0xc34100` encodes 0; it encodes −1.** (V-0008) The bullet
   reads "Big number representation of values that are also representable using
   major types 0 and 1 (for example, 0 can be encoded as the big number
   0xc34100)". `0xc3` is tag **3**, the *negative* big number, whose value is
   −1−*n*; with a content of `0x00` these bytes are −1. The positive big number
   0 is `0xc2 0x41 0x00` or `0xc2 0x40`, and zero.edn lists exactly those two
   (`h'c2420000'`, `h'c240'`) — never `0xc34100`. The bullet's *point* survives,
   since −1 is also representable with a major type, but the stated value is
   wrong. Verified by decoding.
2. **§4.1 item 1 never states the 8-byte case.** Its enumeration stops at "65536
   to 4294967295 … (ai = 0x1a)", yet zero.edn, three.edn, minus_twenty_five.edn
   and map.edn all treat `1b`-headed arguments as general-only. §9.1 counts five
   argument widths; §4.1 rules out three explicitly and the fourth only by
   implication from its opening sentence.
3. **float_nan_payload.edn cannot drive the encode test.** Its
   `edn-representations` list is empty — "there is no EDN representation for
   that" — but Appendix L.1.1's encode test takes the EDN as its input. The
   fixture is decode-side and check-side only. Not a contradiction, but a hole
   in the test matrix the document describes.
4. **`deterministic-serialization` is singular where its four siblings are
   plural**, in Table 3 and in every file's key name, yet it holds an array
   everywhere. Cosmetic.
5. **The `.edn` files are EDN, not JSON**, despite JSON-shaped bodies — they
   carry `h''` byte-string literals. The extension says so; the appendix never
   does.
6. **Table 1's bytes are split across table-cell lines**, which is a rendering
   artefact of the text version rather than a defect, but it is the only place
   in the document where a byte string cannot be lifted contiguously.

## Using the file

Each vector is self-contained: `hex` is the input, `decoded` says what it
means, `conformance` says what each of the three serializations does with it.
For the four test procedures the document defines — encode (L.1.1), decode
(L.1.2), checking decoder (L.1.3), non-checking decoder (L.1.4) — see
`../schema/serialization-check.derived.pseudocode.txt`, Part 3, which renders
them as procedure.

One caution carried from Appendix L.1.1: for the **encode** test the pass
condition is "produces **any** of the encoded representations given in the
example for that serialization type". For preferred-plus with maps that is
genuinely plural — map.edn admits six outputs — so an encode test must compare
against the set of vectors whose `conformance.preferred_plus` is `valid` for
that example, not against a single expected string. Under deterministic
serialization the set is a singleton, which is the whole point of the mode.

The upstream fixtures are also published as individual files at
`https://github.com/cbor-wg/draft-ietf-cbor-serialization/tree/main/examples`
(`[Examples-Repo]` in the source). Those were **not** fetched; every vector here
comes from the draft text itself.
