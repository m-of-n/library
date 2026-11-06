---
schema: "library-summary/v1"
id: cabforum-sc063
record: cabforum-sc063
type: summary
updated: "2026-11-04"
---

# Ballot SC063v4: Make OCSP Optional, Require CRLs, and Incentivize Automation

|  |  |
|---|---|
| **Type** | web (adopted ballot) |
| **Maturity** | `standard`: adopted amendment to the TLS Baseline Requirements (all bylaw requirements shown as MET on the ballot page) |
| **Authors** | Ryan Dickson, Chris Clements (Google, Chrome Root Program) |
| **Published** | 2023-07-13 (close of voting; post dated 2023-07-14) |
| **Identifier** | Ballot SC063v4 |
| **Source** | https://cabforum.org/2023/07/14/ballot-sc063v4-make-ocsp-optional-require-crls-and-incentivize-automation/ |
| **Digest** | `sha256:985d14ab…` (full value in `record.yaml`), fetched 2026-11-01, re-checked 2026-11-04 |

## Overview

SC-063 made OCSP optional for CAs, required CRLs, and revisited the "short-lived" certificate first introduced in Ballot 153. CAs must publish a full CRL or partitioned CRLs, on a set refresh schedule. Short-lived certificates are optional for CAs, need no CRL or OCSP pointer and need not be revoked, with an initial 10-day maximum falling to 7 days for those issued on or after 15 March 2026. The vote was 28 to 1 among issuers, with Certinomis against, and 3 to 0 among consumers.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | changed the revocation regime |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-O-02 |

- **R-O-02**: a voting body of CAs and browsers made expiry, not revocation, the invalidation mechanism for short-lived certificates, while making CRL publication mandatory, so revocation stays representable. That is the shape R-O-02 asks for. The ballot makes short-lived certificates an option, not a preference.

## Relations

- `see_also: cabforum-tls-br`: the document this ballot amends (effective in BR v2.0.1).
- `see_also: letsencrypt-ocsp-eol`: making OCSP optional is what allowed a CA to switch its responder off within the BRs; Let's Encrypt did so in 2025. The post itself does not cite the ballot.

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

- R-001 §4.6 summarises this as making OCSP optional and CRLs mandatory. Right: CRL publication is a duty of every CA (current BR §4.9.7); short-lived certificates need carry no CRL pointer and need not be revoked, so they need never appear on one.
- The v2.0.1 line of the revision table in `cabforum-tls-br` gives an effective date of 2024-03-15. The current BR text may differ from this ballot's numbers.
