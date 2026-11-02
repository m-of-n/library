---
schema: "library-summary/v1"
id: cisa-ed-21-01
record: cisa-ed-21-01
type: summary
updated: "2026-11-01"
---

# ED 21-01: Mitigate SolarWinds Orion Code Compromise (Closed)

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | historic |
| **Authors** | Cybersecurity and Infrastructure Security Agency |
| **Published** | 2020-12-13, Cybersecurity and Infrastructure Security Agency (CISA) |
| **Identifier** | `ED 21-01` |
| **Source** | https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise-closed |
| **Digest** | `sha256:be330c16…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

CISA's emergency directive to federal civilian agencies, dated December 13, 2020 and since closed. It orders them to disconnect or power down Orion versions 2019.4 through 2020.2.1 HF1, calling that the only known mitigation, and to treat monitored hosts as compromised. Supplemental Guidance v3 narrows the affected list to five named versions, and permits continued use at 2020.2.1 HF2 under hardening conditions, with a warning that the adversary's long access to the build process may have other unknown consequences.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Federal response to a signed-update compromise, with binding orders at the time |
| Cryptography | `none` | None directly |
| This project | `adjacent` | Trust in a vendor's signed output was withdrawn by administrative order |

- **R-O-02**: the remedy is operational: disconnect, rebuild, reset credentials. The directive and guidance as read never mention revoking a signature or certificate. That is one data point for why revocation needs to be representable. Bears on no `DEC-*`.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **Historic.** Closed, and archived by CISA. It states obligations no agency now has.
- **The first affected range was wider than the truth.** The opening text's range was narrowed by Supplemental Guidance v3. Read the guidance, not the opening, for affected versions.
- **It carries a naming error.** See `fireeye-sunburst` on TEARDROP.
- **The attribution on the page is an update of April 15, 2021**, not part of the original directive.
- **Read scope.** The directive and Supplemental Guidance v3 through to the third-party reporting section were read. Appendices A and B and the rest of the page were not read closely. Reporting templates were not fetched.
