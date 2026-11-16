---
record: nist-sp-800-140e
kind: examples
title: "nist-sp-800-140e — examples and test vectors"
extracted: "2026-11-15"
reviewed_by: ""
---

# Examples and test vectors

**Finding: SP 800-140E contains no worked example, sample or test vector.** Its one table is Table 1 and its caption reads:

<!-- q L290 -->
> Table 1 - Authentication mechanism permitted at FIPS 140-3 security levels

## Fixtures

| file | what it is | expected result |
|---|---|---|
| `table-1.derived.json` | the 4 rows of Table 1, each with `source_lines`, `quote` and a derived `instance` | every `instance` is accepted by `AuthenticationLevelRow` |
| `authentication-cases.derived.json` | this library's cases for both schemas: 49 cases, 8 `accept` and 41 `reject` | each case's `expect` |

`../schema/build.derived.py` regenerates both files and exits 1 when any case's result differs from `expect`. The cases are this library's, not the standard's.
