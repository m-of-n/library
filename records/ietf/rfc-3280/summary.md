---
schema: "library-summary/v1"
id: rfc-3280
record: rfc-3280
type: summary
updated: "2026-11-04"
---

# Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: rfc3280.json gives Proposed Standard; obsoleted by RFC 5280 |
| **Authors** | R. Housley, W. Polk, W. Ford, D. Solo |
| **Published** | 2002-04 |
| **Identifier** | RFC 3280 · DOI 10.17487/RFC3280 |
| **Source** | https://www.rfc-editor.org/rfc/rfc3280.txt |
| **Digest** | `sha256:65a813a3…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

RFC 3280 is the second PKIX certificate and CRL profile, replacing RFC 2459 and itself replaced by RFC 5280. It carries the shape of today's profile: §4.2.1.11 name constraints, which "MUST be used only in a CA certificate" and "MUST be critical", §6 path validation, and §6.3.3 CRL processing ending in an UNDETERMINED status. §3.2 describes RFC 1422's rigid CA hierarchy and name subordination rule, and §6.2 sketches an extended path validation that reproduces PEM's rules. It matters to this library as the state of the profile before RFC 5280, not as anything to implement.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | superseded |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | history for R-I-05 |

- **R-I-05** (import X.509 only as a foreign identity assertion about a key): anything imported today follows `rfc-5280`. This record only helps with older certificates and history.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

No `see_also` edges. `rfc-5280` carries `supersedes: rfc-3280`, the precise relation, and docs/references.md derives the inverse, so `superseded_by` is left empty here. RFC 1422 is a reference of this RFC (§3.1, §3.2, §6.2), under `cites`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** §1, §3.1 and §3.2 where they discuss RFC 1422, the opening of §4.2.1.11, the opening and close of §6.3.3, and the RFC 1422 sentence in §6.2, by section. The rest was not read. Re-checked against the text 2026-11-04. `rfc-5280` is the record to use; it is extracted to FX-1. Differences between the two were not listed here.

- An errata link exists; errata were not read.
