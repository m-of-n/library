---
schema: "library-summary/v1"
id: rfc-9608
record: rfc-9608
type: summary
updated: "2026-11-04"
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
| **Digest** | `sha256:4952984e…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

Short-lived certificates have a validity period shorter than the time needed to detect, report and distribute revocation information, and some long-lived ones, such as factory IDevIDs, are never revoked (§1). RFC 9608 lets a CA say so with `noRevAvail`, non-critical and forbidden in CA certificates (§2, §3). §4 changes path validation: if the extension is present, or `ocsp-nocheck`, then "Step (a)(3) is skipped". §6 records the price. Misuse could leave a relying party trusting a revoked certificate, and "the only possible remediation is the revocation of the CA".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | removes a check, with the risk stated |
| Cryptography | `none` | no direct bearing |
| This project | `core` | R-O-02's trade-off in a standard |

- **R-O-02** (short-lived validity preferred over revocation-heavy design; revocation still representable) and **R-M-09** (validity intersection, time window ∩ optional online checks): this is the X.509 form of what R-O-02 asks for. §6.1 is the warning to copy: used with a validity period that is "not adequately short", the extension opens a window to exploit a compromised key. The RFC sets no bound, so only policy can check it; that inference is ours.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

- `see_also: cabforum-sc063`: the ballot lets short-lived TLS certificates carry no CRL or OCSP pointer and sets their maximum validity, the bound this RFC leaves to policy.
- `rfc-5280`, `rfc-6960`, `rfc-8555`, `itu-x509-1988` and `itu-x509` are references [RFC5280], [RFC6960], [RFC8555], [X.509-1988] and [X.509-2019], under `cites`. `cabforum-tls-br` authors its own edge here.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** §§1 to 6 and the reference list, by section. §§7 and 8 were not read. Quotes re-checked against the text 2026-11-04. The base X.509 2019 text was checked only so far as to see that `noRevAvail` there is an attribute-certificate extension; the public-key use comes from X.509 Cor. 2 [X.509-2019-TC2], which was not read and is not held.

- It sets no maximum for "short-lived"; `cabforum-tls-br` does that for its own scope.
- R-0001 §4.6 reads this as a surrender. The RFC itself is neutral: revocation remains the default.
- Errata exist per RFC metadata and were not read.
