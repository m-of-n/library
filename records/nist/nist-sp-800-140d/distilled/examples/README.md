---
record: nist-sp-800-140d
kind: examples
title: "nist-sp-800-140d — examples and test vectors"
extracted: "2026-11-15"
reviewed_by: ""
---

# Examples and test vectors

**Finding: SP 800-140D contains no worked example, sample or test vector.** Its section 6.2 is the list itself, and 6.1 says what the list is:

<!-- q L303-305 -->
> This document identifies CMVP-approved sensitive security parameter generation and establishment methods. It precludes the use of all other sensitive security parameter generation and establishment methods.

## Fixtures

| file | what it is | expected result |
|---|---|---|
| `approved-methods.derived.json` | the 13 rows of section 6.2 (one per citation), each with `source_lines`, `quote`, and parsed fields | every row is accepted by `ApprovedSspMethodReference`; the 6.2.2 rows are numbered 1 to 12 in order |
| `approved-methods-cases.derived.json` | this library's cases for that schema: 37 cases, 2 `accept` and 35 `reject` | each case's `expect` |

`../schema/build.derived.py` regenerates both and exits 1 on any difference. A check that every `https://` token of lines 309-393 landed in exactly one row examined 13 tokens and 13 rows.
