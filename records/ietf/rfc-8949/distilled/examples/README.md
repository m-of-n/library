---
record: rfc-8949
kind: examples
title: "rfc-8949 — examples and test vectors"
extracted: "2026-09-30"
reviewed_by: ""
---

<!-- Every example in the source as a fixture file (verbatim bytes or
text), with the expected verification result. These drive our tests. -->

# rfc-8949 — examples and test vectors

`vectors.yaml` holds **232 vectors** extracted from RFC 8949 (STD 94),
"Concise Binary Object Representation (CBOR)". 131 are well-formed encodings;
101 are not well-formed.

Every vector carries the encoded bytes (`hex`, lowercase, no spaces, no `0x`
prefix), the source's own diagnostic notation where the source gives one
(`diagnostic`), a prose description of what the bytes mean (`decoded`), the
expected well-formedness verdict (`expect`), and provenance plus caveats
(`notes`). `locator` names the section or appendix the vector came from, and
`id` is a stable `rfc-8949#V-NNNN` handle.

Every `not-well-formed` vector also carries **`violates`**: the rule the bytes
break, as a `rfc-8949#R-NNNN` requirement id where one applies, followed by the
`normative.md` locator and the substance of the statement. 97 of the 101 cite
`rfc-8949#R-0004` (a decoder MUST NOT return a decoded data item for input that
is not well-formed) plus the §3 / §3.2.x statement that makes those particular
bytes not well-formed; the four `f8`-prefixed ones cite `rfc-8949#R-0005`, the
only BCP 14 statement in the document that forbids a specific byte sequence
outright. Well-formed vectors have no `violates` key. The classification was
derived mechanically by running the Appendix C procedure over each vector's
bytes, not by reading the `notes`: for 100 of the 101 the error kind the
procedure reaches is the one `notes` already claimed, and the hundred-and-first
(V-0089, the bare `ff` of §3.2.1) has notes that give no Appendix F error kind
at all.

## Where the vectors came from

| `locator` | ids | count | content |
| --- | --- | --- | --- |
| Appendix A | V-0001 – V-0081 | 81 | Table 6, the full diagnostic-notation / encoding table |
| Section 3.1 | V-0082 – V-0088 | 7 | worked examples for major types 0, 1, 2, 4, 5 |
| Section 3.2.1 | V-0089 | 1 | the "break" stop code on its own |
| Section 3.2.2 | V-0090 – V-0095 | 6 | definite- and indefinite-length arrays, and the indefinite-length map |
| Section 3.2.3 | V-0096 | 1 | indefinite-length byte string with two chunks |
| Section 3.4 | V-0097 – V-0101 | 5 | tagging example, plus the four alternative encodings of the integer 1 |
| Section 3.4.3 | V-0102 – V-0103 | 2 | bignum for 2^64, and `0x1800` as a longer-than-needed encoding of 0 |
| Section 3.4.4 | V-0104 – V-0105 | 2 | decimal fraction 273.15 and bigfloat 1.5 |
| Section 3.4.6 | V-0106 | 1 | the self-described-CBOR tag head `0xd9d9f7` |
| Section 4.1 | V-0107 – V-0109 | 3 | preferred floating-point serializations (5.5, 5555.5, NaN) |
| Section 4.2.1 | V-0110 – V-0119 | 10 | shortest-form floats, plus the 8 correctly sorted map keys |
| Section 4.2.2 | V-0120 – V-0124 | 5 | the four candidate encodings of the value written "1.0", plus NaN |
| Section 4.2.3 | V-0125 – V-0132 | 8 | the same 8 map keys in length-first order |
| Section 5.2 | V-0133 | 1 | `0x62c0ae`, well-formed but not valid UTF-8 |
| Section 5.5 | V-0134 | 1 | `0x190000`, a longer-than-needed encoding of 0 |
| Section 8.1 | V-0135 – V-0136 | 2 | the no-chunk indefinite-length strings `''_` and `""_` |
| Appendix E.5 | V-0137 – V-0138 | 2 | the CBOR row of Table 8 |
| Appendix F.1 | V-0139 – V-0232 | 94 | every listed CBOR data item that is not well-formed |

Vectors from Sections 3.2.2, 3.4, 3.4.3, 4.1, 4.2.1, 4.2.2 and 4.2.3 sometimes
repeat bytes that also appear in Appendix A. They are kept as separate vectors
because they are separate examples in the source, each making its own point;
the `notes` field says when a vector shares bytes with an Appendix A row.

## What `expect` means

- **`well-formed`** — the bytes are a complete, well-formed encoded CBOR data
  item, with nothing left over. A decoder must accept them.
- **`not-well-formed`** — a decoder must refuse to return a decoded data item.
  `notes` names the failure using the source's own taxonomy from Appendix F:
  error kind 2 (too little data) or error kind 3 (syntax error) with its
  subkind 1–5.

Two distinctions the field deliberately does not carry:

- **Well-formed is not the same as valid.** V-0133 (`62c0ae`) is well-formed
  and must pass a well-formedness check, but its content is not valid UTF-8,
  so a validity check must reject it. Its `notes` says so.
- **Well-formed is not the same as preferred or deterministic.** V-0100
  (`1801`), V-0101 (`190001`), V-0103 (`1800`), V-0122 (`fa3f800000`),
  V-0123 (`fb3ff0000000000000`) and V-0134 (`190000`) are all well-formed but
  are not preferred serializations; `notes` flags each one.

Six vectors are **head-only fragments** — V-0085 (`45`), V-0086 (`5901f4`),
V-0087 (`8a`), V-0088 (`a9`), V-0097 (`c24c`) and V-0106 (`d9d9f7`). The
source shows only the head of these items and describes the content bytes in
prose rather than giving them, so the bytes recorded here stop mid-item and
are marked `not-well-formed` (Appendix F error kind 2). Their `notes` says
this explicitly. A harness that only wants complete items should skip them.

## How a harness should consume the file

`vectors.yaml` is written for a minimal YAML reader: block mappings and
sequences only, no flow collections, every scalar on a single line, and
every scalar quoted. Scalars that contain a double quote or a backslash are
single-quoted with `''` escaping the single quote; all others are
double-quoted with no escapes inside.

Read `vectors` as a list and, for each entry:

1. `bytes.fromhex(hex)` gives the encoded item. Every `hex` value has even
   length, and the empty string never occurs.
2. Run the decoder over exactly those bytes and require that it consumes all
   of them. Assert success when `expect` is `well-formed` and failure when it
   is `not-well-formed`.
3. When `diagnostic` is non-empty, it is the source's diagnostic notation
   verbatim and can drive an encoder round-trip: parse it, encode it, and
   compare against `hex`. Note that Appendix A's diagnostic notation does not
   record encoding indicators (Section 8.1), so several distinct `hex` values
   legitimately share one `diagnostic` — `1.0` appears as `f93c00`,
   `fa3f800000` and `fb3ff0000000000000`, and `1` appears as `01`, `1801` and
   `190001`. Match on `id`, not on `diagnostic`.
4. When `diagnostic` is empty the source gave no diagnostic form for that
   example (it gave an annotated byte listing, binary notation, or prose
   instead). Use `decoded` for the human-readable expectation and do not
   attempt an encoder round-trip.
5. `decoded` is prose, not a machine format. It is empty for every
   `not-well-formed` vector and for the head-only fragments.

Diagnostic notation frequently contains `"`, `:`, `#`, `[`, `{` and
backslashes. After unquoting, treat it as an opaque string: `'"\"\\"'`
unquotes to the six characters `"\"\\"` (V-0058), and `'"𐅑"'`
unquotes to the escaped form the source uses for U+10151 (V-0061), not to the
character itself.

Every vector in this file was cross-checked against an independently written
CBOR well-formedness checker, and the numeric vectors were cross-checked by
decoding their IEEE 754 half-, single- and double-precision bit patterns and
their major type 0 and 1 arguments.

## What this corpus does not cover — for whoever writes the test suite

Established by the pass-3 cross-check, which ran a purpose-written
well-formedness checker and a structural validator for
`../schema/cbor-data-model.derived.cddl` over all 232 vectors. All 131
well-formed vectors validate against **both** CDDL roots (`cbor-data-item` and
`cbor-checked-item`) and every one of their initial bytes is admitted by
`../schema/cbor-head.derived.abnf`; all 101 not-well-formed vectors are refused.
The 27 initial bytes the ABNF excludes all appear in the corpus as
not-well-formed vectors, so the head layer is fully exercised. What is missing
is below; none of it is a transcription defect, because the source gives no
example in any of these cases.

**Requirements marked `testable: yes` that no vector exercises** — four of the
twenty:

| requirement | what a fixture would need |
| --- | --- |
| `rfc-8949#R-0002` | §2.2's rule that an encoder MUST NOT encode "0.0" as a major type 0 integer. Needs an encoder-side assertion, or a map carrying both `0` and `0.0` as keys; the source gives neither as bytes. |
| `rfc-8949#R-0009` | a bignum whose byte string carries leading zeroes, which decoders MUST accept — e.g. tag 2 over `0x0001`. Every bignum in the source is already minimal. |
| `rfc-8949#R-0026` | a layering test: a forwarding layer must pass data it does not process through unchanged. Testable against an implementation, not against bytes. |
| `rfc-8949#R-0027` | the same: the first layer that processes an invalid item must either substitute an error marker or stop. An API-level test. |

`rfc-8949#R-0023` (encoders for CBOR-based protocols MUST produce only valid
items) is half-exercised: V-0133 covers the invalid-UTF-8 case, but nothing
covers an inadmissible tag content type (§5.3.2) or a duplicate-key map
(§5.3.1). `rfc-8949#R-0008` and `rfc-8949#R-0010` are exercised positively only
— V-0048, V-0049, V-0104 and V-0105 show admissible tag content, and the source
offers no negative fixture such as tag 1 over a text string.

**CDDL rules no well-formed vector exercises:** `cbor-tag-21`, `cbor-tag-22`,
`cbor-tag-33`, `cbor-tag-34`, `cbor-tag-35`, `cbor-tag-36` and
`cbor-tag-55799`. Of the 16 tag numbers in `../messages.yaml`, only 0, 1, 2, 3,
4, 5, 23, 24 and 32 appear in a complete vector; 55799 appears only as the
truncated head V-0106. Every other rule in the file is exercised, including all
three float widths, all four indefinite-length forms, both definite and
indefinite variants of each of the four container types, and simple values from
the unassigned-low range, the four named ones and the one-byte extension.

## Material in the source that is not a vector here

- **Appendix B** (jump table for the initial byte) and Tables 1, 2, 3, 4
  and 5 give byte ranges and semantics, not example data items.
- **Appendix C** (pseudocode) and **Appendix D** (half-precision decoders in
  C and Python) contain code, not encoded examples. Section 3.3 and
  Appendix D give no encoded float examples of their own; the float vectors
  come from Appendix A, Section 4.1, Section 4.2.1 and Section 4.2.2.
- **Section 8**: the byte string `0x12345678` written `h'12345678'`,
  `b32'CI2FM6A'` and `b64'EjRWeA'` is byte-string *content* shown in three
  base encodings, not an encoded CBOR data item, so the source gives no
  encoding for it.
- **Section 1.2**: `0b00100001` (`0x21`) illustrates the binary notation used
  throughout the document; it is not offered as a CBOR example.
- **Section 3.1**: the newline discussion contrasts the content byte `0x0a`
  with `0x5c6e` and `0x5c7530303061`. These are bytes inside a text string,
  and no complete data item is given.
- **Section 8.1**: `[_ 1, 2]`, and the encoding indicators `1.5_1` and
  `1.5_3`, are shown without any encoding.
- **Appendix E.5**: the RFC 713, ASN.1 BER, MessagePack and BSON rows of
  Table 8 are other formats, not CBOR.
- **Appendix G** records that errata corrected two earlier encoding examples
  (`29` to `49` in Section 3.4.3, `0b000_11101` to `0b000_11001` in
  Section 5.5). The corrected values are what V-0102 and V-0134 carry.
