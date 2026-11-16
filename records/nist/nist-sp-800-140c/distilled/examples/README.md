---
record: nist-sp-800-140c
kind: examples
title: "nist-sp-800-140c — examples and test vectors"
extracted: "2026-11-15"
reviewed_by: ""
---

# Examples and test vectors

**Finding: SP 800-140C contains no worked example, sample or test vector.** Its section 6.2 is the list itself, introduced by:

<!-- q L311-312 -->
> The categories include transitions, symmetric key encryption and decryption, digital signatures, hashing and message authentication.

## Fixtures

| file | what it is | expected result |
|---|---|---|
| `approved-functions.derived.json` | the 25 rows of section 6.2, one per citation plus the SKIPJACK note, each with `source_lines`, `quote`, and parsed fields | every row is accepted by `ApprovedSecurityFunctionReference` |
| `approved-functions-cases.derived.json` | this library's cases for that schema: 39 cases, 3 `accept` and 36 `reject` | each case's `expect` |

`../schema/build.derived.py` regenerates both and exits 1 on any difference. A check that every `https://` token of lines 309-491 landed in exactly one row examined 24 tokens and 24 rows with a citation.
