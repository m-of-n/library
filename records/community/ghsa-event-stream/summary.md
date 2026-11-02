---
schema: "library-summary/v1"
id: ghsa-event-stream
record: ghsa-event-stream
type: summary
updated: "2026-11-01"
---

# Critical severity vulnerability that affects event-stream and flatmap-stream

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | informational |
| **Authors** | GitHub Advisory Database |
| **Published** | 2018-11-26, GitHub |
| **Identifier** | `GHSA-mh6f-8j2x-4483` |
| **Source** | https://api.github.com/advisories/GHSA-mh6f-8j2x-4483 |
| **Digest** | `sha256:39b59057…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The advisory entry for the event-stream compromise. It says `flatmap-stream` is considered malicious, that it was added as a dependency of `event-stream` 3.3.6, and that users should go to 3.3.4 or a 4.x release. Affected versions are `event-stream` = 3.3.6 and every version of `flatmap-stream`. Severity is critical, CVSS 3.1 9.8, CWE-506.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | A machine-readable identifier for the incident |
| Cryptography | `none` | No cryptographic content |
| This project | `none` | Names an event. It informs no design beyond R-M-07 |

- **R-M-07**: as with `cve-2024-3094`, identification is by package name and version, with no digest. Bears on no `DEC-*`.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **It gives `first_patched_version` 4.0.0** for something that was never a defect to patch, and it recommends a downgrade in its own text. The structured field and the prose do not quite say the same thing.
- **The CVSS scoring is generic.** The payload targeted one build environment (`npm-event-stream`), which the 9.8 does not convey.
- **Read scope.** The whole advisory was read, in both API and HTML form.
