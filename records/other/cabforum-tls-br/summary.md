---
schema: "library-summary/v1"
id: cabforum-tls-br
record: cabforum-tls-br
type: summary
updated: "2026-11-01"
---

# CA/Browser Forum Baseline Requirements for TLS Server Certificates

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard`: adopted CA/Browser Forum requirements, not an IETF or ISO standard |
| **Authors** | CA/Browser Forum |
| **Published** | 2026-10-04 |
| **Identifier** | TLS BR v2.3.1 |
| **Source** | https://github.com/cabforum/servercert/blob/main/docs/BR.md (raw) |
| **Digest** | `sha256:ee4e4e95…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The Baseline Requirements bind publicly trusted TLS CAs. Two themes bear on this topic. Scope: §7.1.2.5.2 defines a Technically Constrained TLS Subordinate CA and, as "an explicit exception" from RFC 5280, allows the constraint to be non-critical for legacy clients. Lifetime: §6.3.2 sets maximum Subscriber validity at 200 days from 2026-03-15, 100 from 2027-03-15 and 47 from 2029-03-15. Short-lived certificates may also go unrevoked, per the revocation clauses of §4.9.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | the operative rules of the Web PKI |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | what an X.509 import can assume |

- **R-I-05**: a BR-conformant certificate is the most common thing an importer sees.
- **R-O-02**: the validity schedule is that requirement arriving by policy.

The `contradicts: rfc-5280` edge records the deliberate exception on criticality.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** front matter, the effective-dates and revision tables, the opening of §4.9.7, §6.3.2's validity lines, §7.1.2.5.2, §7.1.2.10.8, and the definition of Short-lived Subscriber Certificate. Not read through: domain validation, audit and most of §7.

- It binds CAs, not relying parties, so it does not say what a client enforces.
- R-001 §4.4's "explicitly exclude the universe" rule lives in the table of §7.1.2.5.2, column Entire Namespace Exclusion, in this version.
- A moving document: cite the version.
