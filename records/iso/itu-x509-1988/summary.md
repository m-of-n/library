---
schema: "library-summary/v1"
id: itu-x509-1988
record: itu-x509-1988
type: summary
updated: "2026-11-01"
---

# ITU-T X.509 (1988): The Directory - Authentication framework

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `historic`: Superseded per ITU, 1988 edition |
| **Authors** | CCITT |
| **Published** | 1988-11-25 |
| **Identifier** | CCITT Rec. X.509 (11/1988) |
| **Source** | ITU free PDF (2008 reedition) |
| **Digest** | `sha256:13e7ced4…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The first X.509 is an authentication framework for the X.500 Directory, not an Internet PKI. Certificates carry directory distinguished names, and users rely on "an unbroken chain of trusted points in the Directory". §6.3 states the naming premise plainly: authentication relies on each user having a unique distinguished name, allocation is the Naming Authorities' job, and each user must trust them not to issue duplicates. Global naming is therefore a stated trust assumption from the start.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | historic |
| Cryptography | `adjacent` | Annex C uses RSA as its example |
| This project | `adjacent` | names the assumption R-M-03 removes |

- **R-M-03** (names relative to an issuing principal): §6.3 is the position R-M-03 reverses.

## Implementations

Not applicable: superseded.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** contents, definitions in part, §6 opening clauses by section, from ITU's 2008 reedition. §§7 to 10 and the annexes were not read.

- It says nothing about how Naming Authorities would be organised, and it assumes a directory that was never deployed globally, as `rfc-1422` §1 expected.
- The reedition's front matter is from 2008; the body was treated as the 1988 text without comparing originals.
