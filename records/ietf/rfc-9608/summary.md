---
schema: "library-summary/v1"
id: rfc-9608
record: rfc-9608
type: summary
updated: "2026-11-01"
---

# No Revocation Available for X.509 Public Key Certificates

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard |
| **Authors** | R. Housley, T. Okubo, J. Mandel |
| **Published** | 2024-06 |
| **Identifier** | RFC 9608 · DOI 10.17487/RFC9608 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9608.txt |
| **Digest** | `sha256:4952984e…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

Short-lived certificates expire before a compromise could be detected, reported and distributed, and some long-lived ones, such as factory IDevIDs, are never revoked. RFC 9608 lets a CA say so with `noRevAvail`, non-critical and forbidden in CA certificates (§2, §3). §4 changes path validation: if the extension is present, or `ocsp-nocheck`, then "Step (a)(3) is skipped". §6 records the price. Misuse leaves a relying party trusting a revoked certificate, and "the only possible remediation is the revocation of the CA".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | removes a check, with the risk stated |
| Cryptography | `none` | no direct bearing |
| This project | `core` | R-O-02's trade-off in a standard |

- **R-O-02** and **R-M-09**: this is the X.509 form of what R-O-02 asks for. §6.1 is the warning to copy: the validity period has to be adequately short, and nobody can check that it is except by policy.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** §§1 to 6, by section. §§7 and 8 were not read, and the base X.509 2019 text was checked only so far as to see that `noRevAvail` there is an attribute-certificate extension; the public-key use comes from X.509 Cor. 2, which was not read.

- It sets no maximum for "short-lived"; `cabforum-tls-br` does that for its own scope.
- R-001 §4.6 reads this as a surrender. The RFC itself is neutral: revocation remains the default.
- Errata exist per RFC metadata and were not read.
