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

## Not yet verified

**Passes 2 and 3 have not run.** In particular:

- No vector has been validated against the derived schemas in `../schema/`.
- The ~90 rows of Tables 5 and 6 were **spot-checked**, not exhaustively
  re-derived: `float'7fbfe000'`→`f97dff`, `float'7fffe000'`→`f97fff` and
  `[4, 5]`→`98020405` were confirmed correct. Reproducing every row
  byte-for-byte is a verify-pass job.
- `violates` strings have not been cross-checked against the requirement ids
  in `../requirements.yaml`.

Until then these vectors are readable; nothing may be built on them.
