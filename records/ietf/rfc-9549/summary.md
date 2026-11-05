---
schema: "library-summary/v1"
id: rfc-9549
record: rfc-9549
type: summary
updated: "2026-11-04"
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
| **Digest** | `sha256:28c50589…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

RFC 9549 updates RFC 5280 for IDNA2008 and internationalised email, and obsoletes RFC 8399. §1.2 explains why: RFC 8399 sometimes required converting A-labels to U-labels to process email name constraints, which led to implementation complexity and at least two security vulnerabilities; now all IDNs are carried and processed as A-labels. §2.2 removes the ability to constrain a particular mailbox, on the ground that it was not used, so that name constraints can apply alike to `rfc822Name` and `SmtpUTF8Mailbox`. Our reading: each new name form forces the constraint semantics to be revisited, decades after deployment.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | name-constraint semantics, rewritten after vulnerabilities (§1.2) |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | only for R-I-05 |

- **R-I-05** (import X.509 only as a foreign identity assertion about a key, marked `provenance: x509`): an importer that reads names or constraints out of X.509 must compare them under these rules.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

- `see_also: openssl-2022-email-overflow`: §1.2 cites a write-up of CVE-2022-3602 [DDHQ] as a summary of the vulnerabilities RFC 8399's conversion rule produced; the OpenSSL post is the vendor account of the same bugs.
- `rfc-5280` is reference [RFC5280], under `cites`; `updates: rfc-5280` is the RFC's own header claim. `rfc-9598` cites this RFC, so that edge sits under its `cites`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §1 to §2.4 and the reference list, by section. §2.5 and §3 onward were not read. Re-checked against the text 2026-11-04.

- Which verifiers implement this was not checked.
- §2.4's "OLD" text quotes RFC 5280's original §7.3 paragraph, not the version RFC 6818 §5 installed; the replacement makes the difference moot.
- Errata exist per RFC metadata and were not read.
