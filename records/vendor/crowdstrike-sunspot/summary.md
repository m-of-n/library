---
schema: "library-summary/v1"
id: crowdstrike-sunspot
record: crowdstrike-sunspot
type: summary
updated: "2026-11-01"
---

# SUNSPOT: An Implant in the Build Process

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | informational |
| **Authors** | CrowdStrike Intelligence Team |
| **Published** | 2021-01-11, CrowdStrike |
| **Identifier** | https://www.crowdstrike.com/en-us/blog/sunspot-malware-technical-analysis/ |
| **Source** | https://www.crowdstrike.com/en-us/blog/sunspot-malware-technical-analysis/ |
| **Digest** | `sha256:08e91791…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

CrowdStrike's analysis of the implant that put SUNBURST into Orion. SUNSPOT ran on the build server, watched for `MsBuild.exe`, read the process's command line to find the Orion solution, and replaced one source file, `InventoryManager.cs`, during compilation. It restored the original afterwards. MD5 checks on the original and replacement files, and `#pragma warning` wrapping, ensured nothing failed or warned, so the developers saw a normal build. The repository therefore stayed clean, which matches `solarwinds-8k`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Shows a trusted build as the point of compromise, in operational detail |
| Cryptography | `adjacent` | Hash checks were used by the attacker for build safety, not by the defender |
| This project | `adjacent` | It is why attested provenance needs a build platform it can trust, and why provenance alone would not have helped here |

- **R-M-07**: a statement binding the output digest would have bound the backdoored build. Provenance from this builder would, on this account, have recorded a clean source, since the swap happened beneath the build definition. That is our inference, not CrowdStrike's claim. `slsa-2026-mini-shai-hulud` makes the same point five years later. Bears on no `DEC-*`.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **It does not say how the build server was reached.** Initial access is not covered.
- **A single sample.** The text says the identified copy replaces only one file, though the tool supports more.
- **No attribution.** The post explicitly tracks the activity as StellarParticle, without naming an adversary. `cisa-ed-21-01` and `fireeye-sunburst` carry later attribution.
- **Read scope.** The whole post was read from the article text, with YARA rules and indicator tables skimmed. Nothing from the post was executed.
