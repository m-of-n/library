---
schema: "library-summary/v1"
id: liu-2015-revocation
record: liu-2015-revocation
type: summary
updated: "2026-11-01"
---

# An End-to-End Measurement of Certificate Revocation in the Web's PKI

|  |  |
|---|---|
| **Type** | paper (peer-reviewed, IMC '15) |
| **Maturity** | `informational`: research paper |
| **Authors** | Yabing Liu, Will Tome, Liang Zhang, David Choffnes, Dave Levin, Bruce Maggs, Alan Mislove, Aaron Schulman, Christo Wilson |
| **Published** | 2015-10 |
| **Identifier** | DOI 10.1145/2815675.2815685 |
| **Source** | author-hosted PDF |
| **Digest** | `sha256:6c676ed7…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Using 74 full IPv4 HTTPS scans, the paper measures who does their part in revocation. Over 8% of fresh certificates are revoked, and fetching revocation information is often expensive. Across 30 browser and OS combinations, it finds that "no browser in its default configuration correctly checks all revocations and rejects certificates if revocation information is unavailable", and mobile browsers never check. Chrome's CRLSet covers 0.35% of all revocations.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | measures the failure of a security control |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-O-02 |

- **R-O-02**: the measured result is inaction at every party, which is the case for preferring short validity.

## Implementations

None: a measurement study. The improvements it proposes are smaller CRLs, OCSP stapling and a modified CRLSet.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** abstract, introduction, the browser summary, and the concluding discussion. The scan methodology and per-CA tables were not read through.

- 2015 snapshot of browsers. Later records supersede the behaviour measured here.
- Most of the 8% of *fresh* certificates comes from Heartbleed, per the paper, with over 1% revoked before it. The paper's figure for alive certificates is almost 1%. The three should not be interchanged.
- It does not settle whether strict checking would be deployable.
