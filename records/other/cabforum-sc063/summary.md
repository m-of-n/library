---
schema: "library-summary/v1"
id: cabforum-sc063
record: cabforum-sc063
type: summary
updated: "2026-11-01"
---

# Ballot SC-063v4: Make OCSP Optional, Require CRLs

|  |  |
|---|---|
| **Type** | web (adopted ballot) |
| **Maturity** | `standard`: adopted amendment to the TLS Baseline Requirements |
| **Authors** | Ryan Dickson, Chris Clements |
| **Published** | 2023-07-13 |
| **Identifier** | Ballot SC-063v4 |
| **Source** | https://cabforum.org/2023/07/14/ballot-sc063v4-make-ocsp-optional-require-crls-and-incentivize-automation/ |
| **Digest** | `sha256:985d14ab…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

SC-063 made OCSP optional, required CRLs, and introduced short-lived certificates. CAs must publish a full CRL or partitioned CRLs, on a set refresh schedule. Short-lived certificates need no CRL or OCSP pointer and need not be revoked, with an initial 10-day maximum falling to 7 days for those issued on or after 15 March 2026. The vote was 28 to 1 among issuers, with Certinomis against, and 3 to 0 among consumers.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | changed the revocation regime |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-O-02 |

- **R-O-02**: a voting body of CAs and browsers adopted the preference, and kept revocation representable through CRLs, which is what R-O-02 says.

## Implementations

Not applicable.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** the ballot page whole, with results. The redline and background document it links to were not read, so the text changed in the BRs is known from the ballot's summary.

- R-001 §4.6 summarises this as making CRLs mandatory: right, for subscriber certificates other than short-lived ones.
- The v2.0.1 line of the revision table in `cabforum-tls-br` gives an effective date of 2024-03-15. The current BR text may differ from this ballot's numbers.
