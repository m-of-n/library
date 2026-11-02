---
schema: "library-summary/v1"
id: rfc-9549
record: rfc-9549
type: summary
updated: "2026-11-01"
---

# Internationalization Updates to RFC 5280

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard |
| **Authors** | R. Housley |
| **Published** | 2024-03 |
| **Identifier** | RFC 9549 · DOI 10.17487/RFC9549 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9549.txt |
| **Digest** | `sha256:28c50589…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

RFC 9549 updates RFC 5280 for IDNA2008 and internationalised email. §2.2 removes the ability to constrain a particular mailbox, on the ground that it was not used, so that name constraints can apply alike to `rfc822Name` and `SmtpUTF8Mailbox`. It shows the cost of a global name form: each new form of name needs the constraint semantics revisited, decades after deployment.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | no direct bearing |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | only for R-I-05 |

- **R-I-05**: an importer must compare names under these rules. Name-form growth is also an argument for R-M-03, since local names do not need a global internationalisation profile.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §1, §2.2, the opening of §2.3 by section. The remainder of §2 and §3 onward were not read.

- Which verifiers implement this was not checked. `openssl-2022-email-overflow` shows the punycode work behind it going wrong.
- Errata exist per RFC metadata and were not read.
