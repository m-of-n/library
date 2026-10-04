---
record: rfc-8785
kind: examples
title: "rfc-8785 - examples and test vectors"
extracted: "2026-10-03"
pass: 1
reviewed_by: ""
---

# Examples and test vectors

Every example and test vector in RFC 8785 (JSON Canonicalization Scheme),
transcribed verbatim into `vectors.yaml`. This is the artifact a later JCS
implementation is checked against, so it is exhaustive by intent: a vector
that is missing here is a conformance hole we will not notice.

Source: `.cache/rfc-8785.txt`, 984 lines, digest
`63d52294eb0e3f0014174288186d388b4ddbf2c67d1ce8af1d9726eb0c3ab240`.

## Count

**44 entries: 43 executable vectors plus 1 recorded absence (`JCS-E1-01`).**

| locator | vectors | ids |
|---|---:|---|
| Section 3.1 Creation of Input Data | 1 | `JCS-31-E1` |
| Section 3.2.2 Serialization of Primitive Data Types | 4 | `JCS-322-01` .. `JCS-322-04` |
| Section 3.2.2.2 Serialization of Strings | 1 | `JCS-3222-E1` |
| Section 3.2.2.3 Serialization of Numbers | 2 | `JCS-3223-E1`, `JCS-3223-E2` |
| Section 3.2.3 Sorting of Object Properties | 3 | `JCS-323-01` .. `JCS-323-03` |
| Section 3.2.4 UTF-8 Generation | 1 | `JCS-324-01` |
| Appendix B Number Serialization Samples | **26** | `JCS-B-01` .. `JCS-B-26` |
| Appendix C Canonicalized JSON as "Wire Format" | 1 | `JCS-C-01` |
| Appendix D Dealing with Big Numbers | 2 | `JCS-D-01`, `JCS-D-02` |
| Appendix E String Subtype Handling | 2 | `JCS-E-01`, `JCS-E-02` |
| Appendix E.1 Subtypes in Arrays | 1 | `JCS-E1-01` (absence, `input: null`) |

**Appendix B Table 1 has exactly 26 data rows** and all 26 are transcribed,
in source order, one vector per row. Both IEEE 754 columns are preserved
exactly: the input as the 16-digit big-endian hexadecimal bit pattern the
source prints, the expected output as the JSON Representation string
character-for-character. The Comment column is kept, and the four table
footnotes `(1)`-`(4)` are resolved inline under `source_note` on each row
that carries a marker.

By fidelity: 34 verbatim, 3 split out of a larger verbatim example,
2 reconstructed from a display-only line wrap, 5 constructed from prose that
states a rule but prints no literal example.

**7 error vectors**, each carrying `expected: error` and a `violates` key
naming the rule and its locator: `JCS-31-E1` (duplicate property names),
`JCS-3222-E1` (lone surrogate), `JCS-3223-E1` / `JCS-B-10` (NaN),
`JCS-3223-E2` / `JCS-B-11` (Infinity), `JCS-D-01` (number not expressible as
an IEEE 754 double).

## The ones that matter most

- **`JCS-323-02`** is the document's own conformance vector for sorting --
  the source introduces it as "JSON test data [that] can be used for
  verifying the correctness of the sorting scheme in a JCS implementation".
  Seven properties, UTF-16 code unit ordering, with the emoji as the
  discriminator: `😀` sorts *below* `דּ` because its first
  UTF-16 code unit is `d83d`, so sorting the same names as UTF-8 or UTF-32
  gives a different and non-conforming order.
- **`JCS-324-01`** is the only place the document commits to bytes. Its
  118-byte hex block is what ties the whole chain together, and it is what
  lets us confirm both line-wrap reconstructions independently.
- **Appendix B rows 15-17** (`444b1ae4d6e2ef4e`..`50`) straddle `1e+21`, the
  positional/exponential switch, and **row 26** (`43143ff3c1cb0959`) is the
  only round-half-to-even test. These are the rows a serializer fails.

## Reconstructions

The source wraps two long values for display and says so explicitly: "with a
line wrap added for display purposes only". Both have been rejoined to the
true single-line value, and each vector records where the wrap fell under a
`reconstruction` key.

| vector | wrap position |
|---|---|
| `JCS-322-01` (Section 3.2.2, ECMAScript output) | between `"string":` and the value |
| `JCS-323-01` (Section 3.2.3, canonical output) | between `333333333.3333333,` and `1e+30` |

Both reconstructions are confirmed independently rather than assumed: the
Section 3.2.4 hex block decodes to exactly 118 bytes / 116 characters, and
that decoding equals the rejoined `JCS-323-01` value byte-for-byte. The
`JCS-322-01` value differs from it only in property order, which is the point
of that example.

## Derived material

RFC 8785 stops short of printing a canonicalized document in three places.
Where that gap is worth filling, the derivation sits under a `derived:` key
with `in_source: false` and is never mixed into `input` or `expected`:

- `JCS-323-02` -- the canonical document for the sorting vector, given as
  text notation *and* as 180 bytes of hex, with the hex authoritative.
- `JCS-C-01` -- the canonical address record (the source gives only the
  resulting property order, in prose).
- `JCS-D-02` -- the canonical form of the string-wrapped big number.
- `JCS-322-02` -- a per-escape breakdown of the sample string.

All four are pass-1 derivations and want a second pair of eyes.

## Transcription hazards found while writing this

Two characters in this document do not survive an ordinary text pipeline, and
both were silently corrupted on first write before being caught by a
byte-level diff against the source:

1. **U+0080** in the `JCS-323-02` canonical output. It is *outside* the ASCII
   control range U+0000-U+001F, so Section 3.2.2.2 requires it to be emitted
   raw, as the two UTF-8 bytes `c2 80`. A raw C1 control byte does not
   round-trip through editors, clipboards or terminals.
2. **U+FB33** HEBREW LETTER DALET WITH DAGESH. It has a canonical
   decomposition to U+05D3 U+05BC, and a normalizing pipeline will silently
   apply it -- which is precisely the hazard Section 3.1 warns about when it
   says components "MUST preserve Unicode string data 'as is'" and that JCS
   "does not take [Unicode Normalization] into consideration".

Consequently **every non-ASCII character in `vectors.yaml` is held either in
the source's own `\uXXXX` escape form or as hex**, with one deliberate
exception: U+20AC EURO SIGN (`e2 82 ac`) is carried raw, because there it *is*
the expected output. The RFC prints the raw euro sign in **two** places --
§3.2.2's `JSON.stringify()` output and §3.2.3's canonical output -- and
`vectors.yaml` carries it raw in **six**: the four `input`/`expected` values
that hold that same string (`JCS-322-01`, `JCS-322-02`, `JCS-323-01`,
`JCS-324-01`), the derived per-escape `output` cell in `JCS-322-02`, and one
prose mention in `JCS-322-01.reconstruction`. Raw U+20AC occurs nowhere else
in the file. Keep that property if you edit it.

This is a finding about the specification, not only about our tooling: any
JCS deployment that moves canonical bytes through a normalizing layer breaks
signatures on exactly these inputs.

## Deliberately not transcribed

Nothing that constitutes an input/expected pair was left out. The following
material in the source is not a test vector and is not in `vectors.yaml`:

| source | why not |
|---|---|
| **Appendix A**, ECMAScript sample canonicalizer (~60 lines) | Reference implementation code, not a vector -- no input/expected pair. Its own header disclaims error handling and UTF-8 generation, so it is explicitly not a conformance target. It is nevertheless the thing that *produces* the expected outputs of `JCS-E-01` and `JCS-E-02`, and both are captured. Belongs in `protocol.md` / `design-notes.md`. |
| **Appendix E**, C#/Json.NET `[JsonProperty]`/`[JsonIgnore]` snippet | Remedial code showing the prescribed pure-string pattern. No input/expected pair; summarised in the `JCS-E-02` notes. |
| **Appendix E**, the three extraction statements (`new Date(object.time)`, `BigInt(object.big)`, `object.val`) | Post-canonicalization application code. Captured as context on `JCS-E-01`, not as vectors. |
| **Appendix F**, Implementation Guidelines | **Contains no worked example of the signature scheme.** It gives a 6-step creation procedure and a 6-step verification procedure in prose, with no keys, no payload, no signature value, no named algorithm and no designated signature property name. There is nothing to transcribe byte-for-byte. The procedures are protocol content and belong in `protocol.yaml` / `state-machine.yaml`. |
| **Section 5**, Security Considerations 3-step check | Normative requirements on a verifier, not a vector. Belongs in `requirements.yaml`; referenced from `JCS-31-E1`. |
| **Appendix E.1**, Subtypes in Arrays | Two lines of prose, no example. Recorded as `JCS-E1-01` with `input: null` / `expected: null` so a later pass does not hunt for a vector that was never written. Nothing invented to fill it. |
| **Appendices G, H, I** | Lists of URLs (open-source implementations, other canonicalization efforts, the development portal). No examples. |
| External test corpora the RFC points to -- Appendix B's "a file (currently) available in the development portal" and Appendix I's `github.com/cyberphone/json-canonicalization` | Not in the document, so out of scope for a transcription. Also: the library never commits third-party bytes (`library/CLAUDE.md`). If that corpus is wanted it is a separate record with its own `content.sha256` and `content.url`. |
| Appendix B's suggestion to run V8 live against randomly generated IEEE 754 values | A testing method, not a vector. |
| Negative infinity, `fff0000000000000` | **Not in Table 1.** The source tabulates positive infinity only. Noted on `JCS-B-11` as the symmetric case; deliberately not invented, since an invented row in a verbatim artifact is worse than a missing one. |
| Canonical strings for `JCS-323-02`, `JCS-C-01`, `JCS-D-02` | The source never prints them. Supplied under `derived:` only, clearly flagged, never as `expected`. |

One deliberate overlap: `JCS-B-10` / `JCS-B-11` and `JCS-3223-E1` /
`JCS-3223-E2` are the same two error conditions in two different notations
(IEEE 754 bit pattern vs. JSON token). Both are kept, because an
implementation can reject one form and accept the other.

One deliberate judgement call: **`JCS-D-01` is marked `expected: error`
although the source does not say so.** RFC 8785 presents that object as
conforming JSON used to motivate string-wrapping; the error reading follows
from Section 3.1 plus Section 3.2.2.3, since `1.4e+9999` overflows to
Infinity on parse. The vector carries `source_states_error: false` so pass 2
can confirm or overturn it.

## Self-consistency invariants

Re-checkable claims a later pass can assert against `vectors.yaml` and the
source, all of which hold as written:

- 44 vectors, ids unique, `vector_count` in the header agrees.
- Every vector has `id`, `locator`, `kind`, `fidelity`, `input`, `expected`.
- Every `expected: error` vector has `violates.rule` and `violates.locator`.
- Every line of every `verbatim` field occurs literally in
  `.cache/rfc-8785.txt`.
- `JCS-324-01.expected` is 118 bytes of hex and decodes to
  `JCS-324-01.input`, which equals `JCS-323-01.expected`.
- `JCS-323-02.derived.canonical_output_utf8_hex` is 180 bytes and its
  ASCII `<U+XXXX>` notation form matches it exactly; the derived key order
  agrees with the source's expected value list.
- All 26 Appendix B inputs match `/^[0-9a-f]{16}$/`.
