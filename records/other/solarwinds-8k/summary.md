---
schema: "library-summary/v1"
id: solarwinds-8k
record: solarwinds-8k
type: summary
updated: "2026-11-01"
---

# SolarWinds Form 8-K, Item 8.01, 14 December 2020

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | informational |
| **Authors** | SolarWinds Corporation |
| **Published** | 2020-12-14, SolarWinds Corporation (filed with the U.S. Securities and Exchange Commission) |
| **Identifier** | `0001739942` |
| **Source** | https://www.sec.gov/Archives/edgar/data/1739942/000162828020017451/swi-20201214.htm |
| **Digest** | `sha256:9827bee5…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

SolarWinds' securities filing, made the day after its notice to customers. It says a vulnerability was inserted in Orion products in updates released between March and June 2020, introduced through a compromise of the build system, and not present in the source code repository. About 33,000 customers were notified, and fewer than 18,000 may have installed an affected version. It also reports a Microsoft 365 email compromise of unknown relationship.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | The victim's own statement of where the compromise sat |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Establishes that source was clean while build output was not |

- **R-M-07**: the filing is the accountable source for the split between repository and build. Bears on no `DEC-*`.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **Filed days into an investigation.** The filing calls its findings preliminary, and later records in this batch add detail.
- **Dates differ from `fireeye-sunburst`.** The filing says updates released between March and June 2020. FireEye says trojanized updates were signed from March to May 2020. The two describe different events and neither is shown to be wrong, so no `contradicts` edge is set.
- **"Vulnerability" is the filing's word.** The technical sources call it a backdoor.
- **Read scope.** The whole filing was read, except the end of the forward-looking statements boilerplate.
