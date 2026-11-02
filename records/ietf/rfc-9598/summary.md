---
schema: "library-summary/v1"
id: rfc-9598
record: rfc-9598
type: summary
updated: "2026-11-01"
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
| **Digest** | `sha256:df8f7adc…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | no errata link in RFC metadata, 2026-11-01 |

## Overview

RFC 9598 defines `SmtpUTF8Mailbox`, an `otherName` form for internationalised email addresses in X.509. §6 explains how old constraints keep working: `rfc822Name` constraints are extended to cover the new form, since legacy constrained CAs would lack UTF-8 constraints and the new form must not escape them. Comparison strips the local part and works on the domain. So existing scoped CAs gain coverage of a name form that did not exist when they were issued.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | no direct bearing |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | only for R-I-05 |

- **R-I-05**: an importer must treat both forms as one namespace, as §6 says.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract and §6's opening and comparison set-up by section. §§1 to 5 and the rest of §6 were not read.

- It says local-part constraints are rarely used, and that claim comes from the RFC, not from us.
- Deployment was not checked.
