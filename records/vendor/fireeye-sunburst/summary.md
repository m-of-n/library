---
schema: "library-summary/v1"
id: fireeye-sunburst
record: fireeye-sunburst
type: summary
updated: "2026-11-01"
---

# Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | informational |
| **Authors** | FireEye |
| **Published** | 2020-12-12, FireEye (now Mandiant, Google Cloud) |
| **Identifier** | https://cloud.google.com/blog/topics/threat-intelligence/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor |
| **Source** | https://cloud.google.com/blog/topics/threat-intelligence/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor |
| **Digest** | `sha256:617bb1da…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The first public analysis of the campaign. SolarWinds Orion updates carried a trojanized plugin, `SolarWinds.Orion.Core.BusinessLayer.dll`, which FireEye tracks as SUNBURST. The DLL was signed by SolarWinds with a valid certificate, on March 24, 2020 for the sample analysed. It sits dormant for up to two weeks, then contacts infrastructure through a DNS-based generation scheme, masquerading as the Orion Improvement Program. Post-compromise activity favoured legitimate credentials over malware. The piece is an operational detection guide, with the signature as a passing fact and not the headline.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The defining case of a signed supply chain compromise |
| Cryptography | `adjacent` | A valid vendor code signature was on the malicious component |
| This project | `adjacent` | A signature proved who built it, and that was exactly the wrong question |

- **R-M-07**: the digest and signature on the DLL were both right. A signature over a build output proves nothing about the build. `crowdstrike-sunspot` shows the mechanism. Bears on no `DEC-*`.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **Early and vendor-authored.** It was written as the campaign was active, and it promotes vendor products in places.
- **The build compromise itself is not explained.** That is `crowdstrike-sunspot`.
- **CISA conflates a name.** `cisa-ed-21-01` Supplemental Guidance v3 says "TEARDROP or SUNBURST" of the backdoor in Orion. FireEye separates them: SUNBURST is the backdoor, and TEARDROP a memory-only dropper seen post-compromise.
- **Attribution here is a later update**, not the original finding.
- **Read scope.** Executive summary through to the start of *DGA and Blocklists*, plus the closing mitigations, were read. The middle of the malware analysis and the indicator tables were not read closely.
