---
schema: "library-summary/v1"
id: fips-186-1
record: fips-186-1
type: summary
updated: "2026-11-01"
---

# FIPS 186-1: Digital Signature Standard (DSS), 1998

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `historic`: withdrawn or superseded (CSRC) |
| **Authors** | National Institute of Standards and Technology |
| **Published** | 1998-12-15. Withdrawn 2000-01-27 (CSRC) |
| **Identifier** | FIPS PUB 186-1 |
| **Source** | https://csrc.nist.gov/files/pubs/fips/186-1/final/docs/fips186-1.pdf |
| **Digest** | `sha256:b2701fb6…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

FIPS 186-1 widens the standard from one algorithm to two: DSA stays as specified, and the RSA digital signature algorithm is admitted by reference to ANSI X9.31 (§1). The hash moves to SHA-1 under FIPS 180-1. The Applicability changes from unclassified to sensitive unclassified information. It adds advice that X9.31 users keep separate keys for signing and confidentiality, because RSA can do both. The patent statement changes from unaware of infringement to saying the algorithms may be covered. Conformance tests for X9.31 are said not to exist yet.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | First federal approval of RSA signatures |
| Cryptography | `adjacent` | DSA unchanged; RSA specified elsewhere |
| This project | `none` | Withdrawn. Current requirements are in `fips-186-5` |

It bears on no open `DEC-*` or `R-*`, and `bears_on` is empty on purpose: a withdrawn standard. `fips-186-5` carries the live bearing.

## Implementations

Not searched: this standard is withdrawn. See `fips-186-5`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `spec` is inside FX-1's type scope, and extraction would owe the full artifact set, but this withdrawn version was not extracted and no issue owns it. The PDF stays in `.cache/` and is not committed.

## Limits

- **RSA is not specified here.** The specification is ANSI X9.31, which the library does not hold and this record did not read.
- **Most of the text is `fips-186`.** The `supersedes` edge means this replaced that version, not that the DSA changed.
- **Read by comparison.** We read the front matter and §§1 to 3, and sentence-diffed the extracted text against `fips-186`. Changes in §4 onward and the appendices were reviewed from that diff, skipping hexadecimal example lines. Appendix 5 values were not run.
