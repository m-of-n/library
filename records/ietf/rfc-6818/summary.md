---
schema: "library-summary/v1"
id: rfc-6818
record: rfc-6818
type: summary
updated: "2026-11-04"
---

# Updates to the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard |
| **Authors** | P. Yee |
| **Published** | 2013-01 |
| **Identifier** | RFC 6818 · DOI 10.17487/RFC6818 |
| **Source** | https://www.rfc-editor.org/rfc/rfc6818.txt |
| **Digest** | `sha256:e6bb52bd…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |
| **Errata** | RFC metadata carries an errata link (corrected 2026-11-04; earlier recorded as none); not read |

## Overview

RFC 6818 is a set of corrections to RFC 5280. §3 changes the acceptable `explicitText` encodings to match practice, §5 aligns the IDN rules for distinguished names with those for GeneralNames, and §2 places self-issued certificates and self-signed certificates issued by non-CAs outside the profile's scope. §4 replaces RFC 5280 §6.2's third paragraph so that it points to `rfc-5914` and `rfc-5937` for trust anchor information, while leaving implementations free to use or ignore it. Its introduction also says the Security Considerations gain depth on CA key compromise in light of observed attacks, citing Prins.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | clarifies trust-anchor use and, per §1, CA-compromise consequences |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | reading aid for R-I-05 |

- **R-I-05** (import X.509 only as a foreign identity assertion about a key, marked `provenance: x509`): anyone importing X.509 reads RFC 5280 through this update. §2's scope carve-out matters most: what a self-signed end-entity certificate means is outside RFC 5280.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

No `see_also` edges. `rfc-5280`, `rfc-5914` and `rfc-5937` are references [RFC5280], [RFC5914] and [RFC5937], under `cites`. `updates: rfc-5280` is the RFC's own header claim.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** §§1 to 5 and the reference list, by section. The Security Considerations (§6) were not read, so the CA-compromise text is known only from §1's description. Re-checked against the text 2026-11-04.

- RFC 9549 §2.4 has since replaced the RFC 5280 §7.3 paragraph that §5 here rewrote, so §5 of this RFC should not be read as current. RFC 9549's "OLD" text quotes RFC 5280's original paragraph, not the version this RFC installed.
- Errata exist per RFC metadata and were not read.
- Whether `rfc-5280`'s extraction takes these updates into account was not checked. `updated_by` on that record is derived from this record's `updates` edge.
