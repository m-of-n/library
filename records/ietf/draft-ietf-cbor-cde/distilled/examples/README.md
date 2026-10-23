---
record: draft-ietf-cbor-cde
kind: examples
title: "draft-ietf-cbor-cde — examples and test vectors"
extracted: "2026-10-16"
reviewed_by: ""
---

# Examples and test vectors

`vectors.yaml` holds **118 vectors**, `V-0001`–`V-0118`, in source order with
no gaps: **96 `valid`** and **22 `invalid`**. Every `invalid` vector carries a
`violates` naming the rule it breaks and the section that states it. 117 of
the 118 carry `hex`.

This is the artifact that drives our tests. A CDE conformance check is only as
good as its negative cases, so the 22 rejections matter more than the 96
acceptances: CDE's whole content is forbidding encodings that RFC 8949 permits.

## Where the vectors come from

| locator | count | what it is |
|---|---|---|
| Appendix D.2 (Table 5) | 63 | preferred serialization of floating point — the NaN and shortening cases |
| Appendix D.1 (Table 4) | 22 | the examples table |
| Appendix E (Table 7) | 9 | plus 3 more from Appendix E prose |
| Appendix D.3 (Table 6) | 8 | failing examples |
| Appendix B | 4 | the ALDR aside, including the hypothetical application protocol |
| §3.1.2, §3.3, §1.2 and other prose | 6 | examples stated inline rather than tabulated |

## Scope judgement worth knowing

Appendices A, B and C each say "This appendix is informative" in their own
words. **Appendices D, E and F do not.** The extraction therefore treated
Tables 4–7 and Figure 1 as in scope and reproduced them whole. That is a
deliberate reading, not an oversight, and it means this vector set overlaps
the content reproduced in `../normative.md`. A later pass should not prune the
overlap without deciding the scope question first.

## Honesty markers

Where the source gives a diagnostic form but not the encoded bytes, a computed
`hex` says so in its `notes`. No byte string derived by this extraction is
presented as something the document printed.

## Verified (pass 2, 2026-10-18)

Every vector was reproduced from the cached source with a CBOR decoder and
IEEE 754 arithmetic written for that pass — exact rationals, round-half-even,
no CBOR library and no `struct`-based float unpacking — by an agent that did
not write these fixtures.

- **Tables 4, 5 and 6 were re-parsed out of the source and diffed row for
  row**, not spot-checked: 22/22, 63/63 and 8/8 match the vectors in order and
  byte for byte, EDN and hex. All 9 distinct serializations Table 7 prints are
  covered by a vector.
- **All 117 hex-bearing vectors decode to their stated `diagnostic` and
  `decoded` value**, including all 20 `float'hex'` NaN rows, where the payload,
  quiet bit, sign and "shortens to fNN" claim were each recomputed from the
  Appendix C.1.1 trimming rule. The 8 EDN-form diagnostics were additionally
  re-encoded from scratch and matched byte for byte.
- **Every `expect` verdict follows from CDE's rules** as independently
  implemented, and each of the 22 `invalid` vectors has a computed violation
  backing its `violates`, and no vector breaks a rule its `violates` fails to
  name: `V-0114` and `V-0115` break two rules each and name both, `V-0116`
  breaks three and names all three.
- **Provenance holds.** `V-0117`'s bytes are the source's three-line annotated
  dump concatenated and lower-cased, as its note says; `V-0118`, `V-0006`–
  `V-0008`, `V-0010`–`V-0011` are correctly marked as our computation;
  `V-0013` is correctly marked as borrowed from RFC 8949; `V-0012` correctly
  carries no hex at all.
- **Appendix F's `try_float16_encode`** (`../schema/try-float16-encode.c`) was
  cross-checked against the same independent implementation over 125,560
  inputs, including all 65,536 binary16 patterns widened to binary64. No
  disagreement: the source's figure is correct.

## Validated against the schemas (pass 3, cross-check, 2026-10-18)

The two things pass 2 left open are now done.

**Every vector that carries bytes has been run against this record's own
`../schema/`.** The derived pseudocode and the data-model rules of the two
derived CDDL files were transcribed into one runnable layered checker, and all
**117 hex-bearing vectors went through it: 96 `valid` accepted, 21 `invalid`
rejected, 0 failures.** The 118th, `V-0012`, carries no bytes because the source
prints none; it was synthesised exactly as its own `notes` instruct — `0x9f`,
256 encoded items, `0xff` — and is rejected, with the definite-length
counterpart accepted as a control. All 96 valid vectors additionally survive the
re-encode check the source itself proposes in the Appendix C preamble
(`cde_encode(generic_decode(input)) == input`): **96 byte-identical, 0
mismatched.**

**Every `invalid` vector fails for a rule its own `violates` names.** Each of
the 22 now carries `violates_requirements`, the machine-resolvable ids for the
rules its prose cites — 55 links in all, every one resolving to an entry
`../requirements.yaml` defines. The prose `violates` strings are unchanged. The
checker's rejection reason was then matched against those ids rule by rule:
**0 vectors are rejected under a rule their `violates_requirements` fails to
name.** `V-0114` and `V-0115` are each rejected under both rules they cite, and
`V-0116` under all three. `V-0006` cites two ids the checker's own rejection
does not reach (`R-0066`, `R-0067`, basic validity) and that is correct: a map
with two identical integer keys breaks the ordering rule *and* the duplicate-key
validity rule, and the checker rejects it under the first.

**Which layer catches which.** Of the 21 runnable `invalid` vectors the CDDL
layer catches **none** — `../schema/README.md` says in terms that CDDL can
express neither shortest-head nor sibling map ordering, and this is that claim
measured. The head-level rules catch **9** (`V-0100`, `V-0101`, `V-0106`,
`V-0109`–`V-0112`, `V-0116`, `V-0118`), the value-level rules **12**
(`V-0006`, `V-0010`, `V-0013`, `V-0099`, `V-0102`–`V-0105`, `V-0113`–`V-0116`),
and the extra-code check of `../schema/cde-encode.derived.pseudocode.txt` §4.2
catches the **one** nothing else does: `V-0007`, the `-0.0`/`0.0` map, which is
correctly sorted and passes every byte-level CDE rule. `V-0116` is caught twice,
which is why 9 + 12 + 1 covers 21 vectors.

**The checker discriminates rather than merely accepting.** 54 cases the source
never prints were run through it — indefinite-length text, array and map heads
(the source exhibits only the byte-string one), non-preferred heads at every
argument width for integers, strings, arrays, maps and tags, non-preferred float
widths including subnormals and NaN payloads, misordered, duplicate and
byte-string-keyed maps, bignum range and leading-zero edges, reserved `ai`, a
sub-32 one-byte simple value, and trailing data. **54 correct, 0 wrong.**

Outstanding: a human `reviewed_by`, and nothing else.
