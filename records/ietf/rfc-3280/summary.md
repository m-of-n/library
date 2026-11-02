---
schema: "library-summary/v1"
id: rfc-3280
record: rfc-3280
type: summary
updated: "2026-11-01"
---

# Internet X.509 PKI Certificate and CRL Profile (2002)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, obsoleted by RFC 5280 |
| **Authors** | R. Housley, W. Polk, W. Ford, D. Solo |
| **Published** | 2002-04 |
| **Identifier** | RFC 3280 · DOI 10.17487/RFC3280 |
| **Source** | https://www.rfc-editor.org/rfc/rfc3280.txt |
| **Digest** | `sha256:65a813a3…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

RFC 3280 is the second PKIX certificate and CRL profile, replacing RFC 2459 and itself replaced by RFC 5280. It carries the shape of today's profile: §4.2.1.11 name constraints as a critical extension in CA certificates, §6 path validation, and §6.3.3 CRL processing ending in an UNDETERMINED status. It matters to this library as the state of the profile before RFC 5280, not as anything to implement.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | superseded |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | history for R-I-05 |

- **R-I-05** (import X.509 only as a foreign identity assertion): anything imported today follows `rfc-5280`. This record only helps with older certificates and history.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** §1, the opening of §4.2.1.11, and the opening of §6.3.3, by section. The rest was not read. `rfc-5280` is the record to use; it is extracted to FX-1. Differences between the two were not listed here.

- An errata link exists; errata were not read.
- `superseded_by` is left empty on purpose: `rfc-5280` carries `supersedes: rfc-3280`, and docs/references.md derives inverses.
