---
schema: "library-summary/v1"
id: solarwinds-8k
record: solarwinds-8k
type: summary
updated: "2026-11-04"
---

# SolarWinds Form 8-K, Item 8.01, 14 December 2020

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | unset: an SEC filing has no standing level to verify |
| **Authors** | SolarWinds Corporation |
| **Published** | 2020-12-14, SolarWinds Corporation (filed with the U.S. Securities and Exchange Commission) |
| **Identifier** | `0001739942` |
| **Source** | https://www.sec.gov/Archives/edgar/data/1739942/000162828020017451/swi-20201214.htm |
| **Digest** | `sha256:2bc6cea3…` (full value in `record.yaml`), fetched 2026-11-04. The served bytes vary between fetches and earlier digests did not reproduce; see `content.note` |

## Overview

SolarWinds' securities filing, made the day after its December 13 communication to customers. It says a vulnerability was inserted in Orion products in updates released between March and June 2020, introduced through a compromise of the Orion software build system, and not present in the source code repository. About 33,000 active-maintenance Orion customers were notified, and SolarWinds believed fewer than 18,000 may have installed an affected version. It also reports a compromise of its Microsoft Office 365 email, whose relationship to the build compromise was still under investigation.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | The victim's own statement of where the compromise sat |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Establishes that source was clean while build output was not |

- **Bears on no `R-*` or `DEC-*`.** The filing says nothing about digests, signatures or statements, so it supports no requirement on its own. Its value is as the accountable source for the repository-versus-build split that `crowdstrike-sunspot` explains, and that record carries the R-M-07 reasoning.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Relations

- **`see_also` `fireeye-sunburst`**: the two date the malicious updates differently (see Limits). The edges to `crowdstrike-sunspot` and `cisa-ed-21-01` are authored on those records, with their reasons.

## Limits

- **Filed days into an investigation.** The filing calls its investigations "preliminary and on-going", and later records in this topic add detail.
- **Dates differ from `fireeye-sunburst`.** The filing says updates released between March and June 2020. FireEye says trojanized updates were digitally signed from March to May 2020. One is about release and the other about signing, and neither is shown to be wrong, so no `contradicts` edge is set.
- **"Vulnerability" is the filing's word.** The technical sources call it a backdoor.
- **Read scope.** The whole filing, including the forward-looking statements, was read on 2026-11-04 from the copy whose digest is recorded.
