---
schema: "library-summary/v1"
id: rfc-9598
record: rfc-9598
type: summary
updated: "2026-11-04"
---

# Internationalized Email Addresses in X.509 Certificates

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard |
| **Authors** | A. Melnikov, W. Chuang, C. Bonnell |
| **Published** | 2024-05 |
| **Identifier** | RFC 9598 · DOI 10.17487/RFC9598 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9598.txt |
| **Digest** | `sha256:df8f7adc…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |
| **Errata** | none: `errata_url` is null in rfc9598.json, checked 2026-11-04 |

## Overview

RFC 9598 defines `SmtpUTF8Mailbox`, an `otherName` form for internationalised email addresses in X.509, and obsoletes RFC 8398. §6 explains how old constraints keep working: both name forms "represent the same underlying email address namespace", and since legacy constrained CAs would lack UTF-8 constraints, `rfc822Name` constraints are extended (by RFC 9549) to cover the new form. Comparison strips the local part and works on the domain. So existing scoped CAs gain coverage of a name form that did not exist when they were issued.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | keeps legacy name constraints binding on a new name form |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | only for R-I-05 |

- **R-I-05** (import X.509 only as a foreign identity assertion about a key, marked `provenance: x509`): an importer must treat both forms as one namespace, as §6 says.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

- `see_also: cabforum-smime-br`: the S/MIME Baseline Requirements admit `id-on-SmtpUTF8Mailbox` subject alternative names "encoded in accordance with" RFC 9598 (§7.1.4.2.1) and list mailbox constraints in Subordinate CA certificates via `rfc822Name` in `permittedSubtrees` (note in §3.2.2), consistent with §6 here, which requires `rfc822Name` for email constraints. The edge is ours; `cabforum-smime-br` says it is authored here.
- `rfc-5280`, `rfc-5321` and `rfc-9549` are references [RFC5280], [RFC5321] and [RFC9549], under `cites`. `updates: rfc-5280` is the RFC's own header claim.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §6 and the reference list, by section. §§1 to 5 were not read. Quotes re-checked against the text 2026-11-04.

- It says local-part constraints are "rarely, if at all, used in practice"; that claim comes from the RFC, not from us.
- Deployment was not checked.
