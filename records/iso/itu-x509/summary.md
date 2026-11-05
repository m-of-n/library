---
schema: "library-summary/v1"
id: itu-x509
record: itu-x509
type: summary
updated: "2026-11-04"
---

# ITU-T X.509: The Directory - Public-key and attribute certificate frameworks

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard`: ITU-T Recommendation, in force per the ITU page 2026-11-01 |
| **Authors** | ITU-T Study Group 17 |
| **Published** | 2019-10-14 |
| **Identifier** | ITU-T X.509 (10/2019) · ISO/IEC 9594-8:2020 |
| **Source** | ITU free PDF (base text only) |
| **Digest** | `sha256:1f4ea293…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

X.509 defines the public-key and attribute certificate frameworks, CRLs, extensions and path processing that PKIX profiles. It is broader than the Web uses: trust anchors (§7.5), three-cornered and four-cornered trust models (§8), authorization and validation lists (§11), and privilege management. On scope, §9.4.2.2 lets a CA constrain subject names, and says the extension may be critical or non-critical at the CA's option, with critical recommended. §7.11 requires CAs to be uniquely named but places how to ensure that outside its scope.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | the certificate model everything else profiles |
| Cryptography | `adjacent` | alternative algorithm extensions (§9.8) and signature handling |
| This project | `adjacent` | what R-M-01 declines |

- **R-M-01** (native encoding not X.509) and **R-I-05** (import only as foreign assertion): this is the format being declined and imported.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** front matter and summary, §7.11, §8, §9.4.2.2, the opening of Annex I.3. A 236-page standard, not read through: everything else was seen only in the contents list or by keyword.

- **Corrigenda and Amd. 1 are unread.** Do not assume this text is current for any clause. RFC 9608 says Cor. 2 extended `noRevAvail` to public-key certificates, which the base text here does not do.
- **Looser than PKIX on criticality:** §9.4.2.2 lets the CA mark name constraints non-critical, recommending critical; `rfc-5280` narrows that to critical. A profile narrowing an option is not a contradiction, so no `contradicts` edge. The Forum's exception (`cabforum-tls-br`) departs from RFC 5280, not from X.509.
- `see_also`: `itu-x509-1988` is the first edition of this line, kept as its own record for the naming premise in its §6.3; `rfc-5280` is the PKIX profile of this text. The `rfc-9608` edge is authored on that record.
