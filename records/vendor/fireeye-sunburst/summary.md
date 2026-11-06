---
schema: "library-summary/v1"
id: fireeye-sunburst
record: fireeye-sunburst
type: summary
updated: "2026-11-04"
---

# Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | unset: a vendor blog has no publisher-stated standing |
| **Authors** | FireEye |
| **Published** | 2020-12-12, FireEye (now Mandiant, Google Cloud) |
| **Identifier** | https://cloud.google.com/blog/topics/threat-intelligence/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor |
| **Source** | https://cloud.google.com/blog/topics/threat-intelligence/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor |
| **Digest** | `sha256:4387cb2a…` (full value in `record.yaml`), fetched 2026-11-04. The page changes per request; see `content.note` |

## Overview

FireEye's disclosure of the campaign. SolarWinds Orion updates carried a trojanized plugin, `SolarWinds.Orion.Core.BusinessLayer.dll`, which FireEye tracks as SUNBURST. The DLL is described as "a SolarWinds digitally-signed component", and the sample analysed was signed with a SolarWinds certificate on March 24, 2020. Trojanized updates were signed from March to May 2020. After a dormant period of up to two weeks it resolves C2 subdomains of `avsvmcloud[.]com` from a domain generation algorithm, and masquerades its traffic as the Orion Improvement Program protocol. Post-compromise activity favoured legitimate credentials and remote access over malware. The piece is an operational detection guide, with the signature as a passing fact and not the headline.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The defining case of a signed supply chain compromise |
| Cryptography | `adjacent` | A vendor code signature was on the malicious component |
| This project | `adjacent` | A signature proved who built it, and that was exactly the wrong question |

- **R-M-07**: the DLL was signed by its vendor and identified by hash. Our reading, not FireEye's: a signature or digest over a build output says which bytes the vendor shipped, nothing about whether the build was sound. Binding a digest is necessary and not sufficient. `crowdstrike-sunspot` shows the mechanism. Bears on no `DEC-*`.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Relations

No `see_also` is authored here. The edges to this record are authored, with reasons, on `crowdstrike-sunspot`, `solarwinds-8k` and `cisa-ed-21-01`.

## Limits

- **Early and vendor-authored.** It was written while the campaign was active ("is currently ongoing"), and it promotes FireEye products in places.
- **The build compromise itself is not explained.** That is `crowdstrike-sunspot`.
- **CISA conflates a name.** `cisa-ed-21-01` Supplemental Guidance v3 says "a malicious backdoor AKA TEARDROP or SUNBURST". FireEye separates them: SUNBURST is the backdoor, and TEARDROP "a previously unseen memory-only dropper" that the attackers deployed in at least one instance, among the payloads SUNBURST samples delivered.
- **Attribution here is a later update** (May 2022, merging UNC2452 into APT29), not the original finding.
- **Read scope.** Executive summary through to the start of *DGA and Blocklists*, plus the closing mitigations, were read. The middle of the malware analysis and the indicator tables were not read closely.
