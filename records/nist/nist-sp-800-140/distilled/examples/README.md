---
record: nist-sp-800-140
kind: examples
title: "nist-sp-800-140 — examples and test vectors"
extracted: "2026-11-15"
reviewed_by: ""
---

# Examples and test vectors

**Finding: SP 800-140 contains no worked example, sample evidence package or test vector.** The words 'test vectors' occur only in the self-test assertions, as inputs a module must not need:

<!-- q L984-987 -->
> {All self-tests shall be performed,} and determination of pass or fail shall be made by the module, without external controls, externally provided input text test vectors, expected output results, or operator intervention or whether the module will operate in an approved or non-approved mode.

## Fixtures

| file | what it is | expected result |
|---|---|---|
| `assertion-index.derived.json` | the 22 assertions with their VE and TE ids and start lines | every row accepted by `Assertion` |
| `evidence-index.derived.json` | the 76 evidence items with the assertion above each | every row accepted by `EvidenceItem` |
| `evidence-cases.derived.json` | this library's cases for all 19 schemas: 286 cases, 29 `accept`, 257 `reject` | each case's `expect` |

`../schema/build.derived.py` regenerates all three and exits 1 on any difference.
