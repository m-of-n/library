---
schema: "library-summary/v1"
id: rfc-6818
record: rfc-6818
type: summary
updated: "2026-11-01"
---

# Updates to the Internet X.509 PKI Certificate and CRL Profile

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard |
| **Authors** | P. Yee |
| **Published** | 2013-01 |
| **Identifier** | RFC 6818 · DOI 10.17487/RFC6818 |
| **Source** | https://www.rfc-editor.org/rfc/rfc6818.txt |
| **Digest** | `sha256:e6bb52bd…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | no errata link in RFC metadata, 2026-11-01 |

## Overview

RFC 6818 is a set of corrections to RFC 5280. It changes the acceptable `explicitText` encodings to match practice, aligns the IDN rules for distinguished names with those for GeneralNames, and places self-signed certificates issued by non-CAs outside the profile's scope. §4 replaces RFC 5280 §6.2's text so that it points to `rfc-5914` and `rfc-5937` for trust anchor information. Its introduction also says the Security Considerations gain depth on CA key compromise in light of observed attacks, citing Prins.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | no direct bearing |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | reading aid for R-I-05 |

- **R-I-05**: anyone importing X.509 reads RFC 5280 through this update. §2's scope carve-out matters most: what a self-signed end-entity certificate means is outside RFC 5280.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** §§1 to 4 and the opening of §5 by section. The rest of §5, the Security Considerations update and the references were not read, so the CA-compromise text is known only from §1's description.

- RFC 9549 has since changed the IDN rules this RFC touched, so §5 of this RFC should not be read as current.
- Whether `rfc-5280`'s extraction takes these updates into account was not checked. `updated_by` is derived from this record's `updates` edge.
