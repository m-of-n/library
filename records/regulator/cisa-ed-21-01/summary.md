---
schema: "library-summary/v1"
id: cisa-ed-21-01
record: cisa-ed-21-01
type: summary
updated: "2026-11-04"
---

# ED 21-01: Mitigate SolarWinds Orion Code Compromise (Closed)

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | historic: the page says CISA "has therefore sunset this ED", under an Archived Content banner |
| **Authors** | Cybersecurity and Infrastructure Security Agency |
| **Published** | 2020-12-13, Cybersecurity and Infrastructure Security Agency (CISA) |
| **Identifier** | `ED 21-01` |
| **Source** | https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise-closed |
| **Digest** | `sha256:1ba9a144…` (full value in `record.yaml`), fetched 2026-11-04 by a sibling session; cisa.gov refused this one. Earlier digests did not reproduce; see `content.note` |

## Overview

CISA's emergency directive to federal civilian agencies, dated December 13, 2020 and since sunset; the page marking it closed is dated January 08, 2026. It ordered them to disconnect or power down Orion versions 2019.4 through 2020.2.1 HF1, calling that the only known mitigation then available. Its Required Action 4, to treat monitored hosts as compromised and rebuild them, was later superseded by Supplemental Guidance v3 (January 6, 2021). Supplemental Guidance v1 (December 18, 2020) had already narrowed the affected list, and v3 names five affected versions. v3 permits continued use at 2020.2.1 HF2 or later under hardening conditions (Appendix B), and warns that the adversary's "longstanding, covert access to the build process" may have other unknown consequences. Supplemental Direction v4 (April 22, 2021) adds pre-eviction and eviction actions for networks with follow-on activity.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Federal response to a signed-update compromise, with binding orders at the time |
| Cryptography | `none` | None directly |
| This project | `adjacent` | Trust in a vendor's signed output was withdrawn by administrative order |

- **Bears on no `R-*` or `DEC-*`.** The remedy is operational: disconnect, forensics, rebuild, reset credentials. The directive and its guidance never mention revoking a signature or certificate. That is an observation about this response, not evidence for or against R-O-02's "revocation still representable", so no `bears_on` is claimed.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Relations

- **`see_also` `fireeye-sunburst`**: v3 names the backdoor "TEARDROP or SUNBURST", which FireEye's analysis separates (see Limits).
- **`see_also` `crowdstrike-sunspot`**: v3's warning about the adversary's access to the build process is what SUNSPOT documents in mechanism.
- **`see_also` `solarwinds-8k`**: the vendor's own account, filed the next day, states the affected scope as updates released between March and June 2020, where this directive first gave a version range, 2019.4 through 2020.2.1 HF1, later narrowed.

## Limits

- **Historic.** Closed, and archived by CISA. It states obligations no agency now has.
- **The first affected range was wider than the truth.** The original directive's range was narrowed by Supplemental Guidance v1 and restated in v3. Read the guidance, not the opening, for affected versions.
- **It carries a naming error.** v3's Background says the affected versions contain "a malicious backdoor AKA TEARDROP or SUNBURST". FireEye (`fireeye-sunburst`) calls the backdoor SUNBURST and TEARDROP a memory-only dropper seen post-compromise.
- **The attribution on the page is an update of April 15, 2021**, not part of the original directive.
- **Read scope.** The whole page, from the copy whose digest is recorded: the directive, FAQ, Supplemental Guidance v3 with Appendices A and B and footnotes, and Supplemental Direction v4. Reporting templates and the archived v1 and v2 guidance were not fetched.
