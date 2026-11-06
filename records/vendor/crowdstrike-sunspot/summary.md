---
schema: "library-summary/v1"
id: crowdstrike-sunspot
record: crowdstrike-sunspot
type: summary
updated: "2026-11-04"
---

# SUNSPOT: An Implant in the Build Process

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | unset: a vendor blog has no publisher-stated standing |
| **Authors** | CrowdStrike Intelligence Team |
| **Published** | 2021-01-11, CrowdStrike |
| **Identifier** | https://www.crowdstrike.com/en-us/blog/sunspot-malware-technical-analysis/ |
| **Source** | https://www.crowdstrike.com/en-us/blog/sunspot-malware-technical-analysis/ |
| **Digest** | `sha256:e19341f5…` (full value in `record.yaml`), fetched 2026-11-04. The page changes per request; see `content.note` |

## Overview

CrowdStrike's analysis of the implant that put SUNBURST into Orion. SUNSPOT ran on the build server, watched for `MsBuild.exe`, read each such process's command line to find the Orion solution, and replaced one source file, `InventoryManager.cs`, during compilation. It restored the original after `MsBuild.exe` exited. Safeguards kept the build from failing or drawing attention: MD5 checks on the original and replacement source before the swap, and the injected code wrapped in `#pragma warning disable` and `restore`. CrowdStrike does not discuss the source repository, but a swap made on the build server and undone afterwards is consistent with `solarwinds-8k`'s statement that the vulnerability was not in the repository. That link is ours.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Shows a trusted build as the point of compromise, in operational detail |
| Cryptography | `adjacent` | Hash checks were used by the attacker for build safety, not by the defender |
| This project | `adjacent` | It is why attested provenance needs a build platform it can trust, and why provenance alone would not have helped here |

- **R-M-07**: a statement binding the output digest would have bound the backdoored build. Provenance from this builder would, on this account, have recorded a clean source, since the swap happened beneath the build definition. That is our inference, not CrowdStrike's claim. On that reading, binding a digest is not sufficient on its own. `slsa-2026-mini-shai-hulud` records a similar outcome in 2026, with valid provenance from a compromised build. Bears on no `DEC-*`.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Relations

- **`see_also` `fireeye-sunburst`**: SUNSPOT is the mechanism that inserted the backdoor FireEye analysed.
- **`see_also` `solarwinds-8k`**: the vendor's statement that the build, not the repository, was compromised, which this mechanism fits.
- Edges from `cisa-ed-21-01`, `freund-2024-xz` and `slsa-2026-mini-shai-hulud` are authored on those records.

## Limits

- **It does not say how the build server was reached.** Initial access is not covered.
- **A single sample.** The post says SUNSPOT supports replacing multiple files, but the identified copy only replaces `InventoryManager.cs`.
- **No attribution.** CrowdStrike says it "does not attribute the SUNSPOT implant, SUNBURST backdoor or TEARDROP post-exploitation tool to any known adversary" and tracks the activity as StellarParticle. `cisa-ed-21-01` and `fireeye-sunburst` carry later attribution.
- **Read scope.** The whole post was read from the article text fetched 2026-11-04, with YARA rules and indicator tables skimmed. Nothing from the post was executed.
