---
schema: "library-summary/v1"
id: larisch-2017-crlite
record: larisch-2017-crlite
type: summary
updated: "2026-11-01"
---

# CRLite: A Scalable System for Pushing All TLS Revocations to All Browsers

|  |  |
|---|---|
| **Type** | paper (peer-reviewed, IEEE S&P 2017) |
| **Maturity** | `informational`: research paper |
| **Authors** | James Larisch, David Choffnes, Dave Levin, Bruce M. Maggs, Alan Mislove, Christo Wilson |
| **Published** | 2017 |
| **Identifier** | DOI 10.1109/SP.2017.17 |
| **Source** | UMD-hosted PDF |
| **Digest** | `sha256:1630ad4e…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

No major browser fully checks revocation, because each deployed mechanism is incomplete, insecure, inefficient, slow to update or not private. CRLite has an aggregator collect the status of every known certificate from scans and CT, and pushes it to clients as a filter cascade: Bloom filters arranged to have neither false positives nor false negatives over that set. The paper reports 10 MB initially and about 580 KB a day for over 30M certificates. Because it holds all revocations, a client can adopt a fail-closed posture, and it reveals no browsing to third parties.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | removes the soft-fail failure mode |
| Cryptography | `adjacent` | a data-structure construction |
| This project | `adjacent` | an alternative to online status, evidence for R-O-02 |

- **R-O-02**: shows revocation can stay representable without an online check, at the cost of a global aggregator.

## Implementations

The paper describes a prototype with a Firefox extension. R-001 §4.6 says CRLite shipped in Firefox 142; this paper cannot and does not support that, and it was not verified here.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** abstract, introduction, conclusion, and the design-challenge list. §III's proofs and the evaluation were not read through.

- The paper's figures are from a January 2017 corpus and predate today's issuance volume and shorter lifetimes.
- Its coverage rests on knowing all certificates, so it depends on CT and scans. Clients are protected only for certificates the aggregator saw.
- It centralises aggregation. The paper offers signed logs for auditing, which is not the same as removing the role. That matters for a design whose premise avoids global parties.
