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

## Still not verified

**Pass 3 (cross-check) has not run.** In particular:

- No vector has been validated against the derived schemas in `../schema/`.
- `violates` strings name sections and quote the source, but have not been
  wired to the `R-NNNN` ids in `../requirements.yaml`.

Until then these vectors are readable; nothing may be built on them.
