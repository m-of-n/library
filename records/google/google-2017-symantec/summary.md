---
schema: "library-summary/v1"
id: google-2017-symantec
record: google-2017-symantec
type: summary
updated: "2026-11-01"
---

# Chrome's Plan to Distrust Symantec Certificates

|  |  |
|---|---|
| **Type** | web (blog post) |
| **Maturity** | `informational`: vendor announcement |
| **Authors** | Devon O'Brien, Ryan Sleevi, Andrew Whalley |
| **Published** | 2017-09-11 |
| **Identifier** | Google Security Blog, 2017-09-11, updated 2018-01-31 |
| **Source** | https://security.googleblog.com/2017/09/chromes-plan-to-distrust-symantec.html |
| **Digest** | `sha256:9a700cdd…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

A January 19, 2017 posting to mozilla.dev.security.policy exposed questionable Symantec certificates, and the investigation found Symantec had let organisations issue without proper oversight. Chrome set out a phased end: Chrome 66 removed trust in certificates issued before June 1, 2016, DigiCert-run infrastructure took over on December 1, 2017, and Chrome 70 removed the old infrastructure entirely, around October 23, 2018. The staging exists so that site operators have time to replace certificates.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | the cost of revoking a global anchor |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | same point as `google-2016-wosign`, at scale |

- **R-I-02**: a single global anchor cannot be withdrawn quickly. Per-issuer local scope bounds that cost.

## Implementations

Not applicable: an incident announcement.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** whole, from the page's script template, including the reference timeline.

- **R-001 §4.8 says Symantec was "caught by CT". This post does not say that.** It attributes the discovery to the newsgroup posting and does not mention Certificate Transparency. The claim needs another source.
- Dates marked with `~` are the post's estimates; actual Chrome releases were not checked.
