---
schema: "library-summary/v1"
id: omb-m-23-16
record: omb-m-23-16
type: summary
updated: "2026-10-02"
---

# M-23-16: Update to Memorandum M-22-18

|  |  |
|---|---|
| **Type** | spec (OMB memorandum) |
| **Maturity** | _unset_ — binding 2023-06-09 → **rescinded 2026-01-23** |
| **Authors** | Shalanda D. Young, Director, OMB |
| **Published** | 2023-06-09 |
| **Identifier** | OMB M-23-16 |
| **Source** | https://bidenwhitehouse.archives.gov/wp-content/uploads/2023/06/M-23-16-Update-to-M-22-18-Enhancing-Software-Security.pdf |
| **Digest** | `f9f920e49032707f9a58a4ef32fdf44ef5253ed5c66f1bc8de3824fcedbcfa5b` (5 pp, retrieved 2026-10-02) |

**Status / currency (checked 2026-10-02).** Supersession chain: M-22-18 (2022-09-14) → updated by
**M-23-16** (2023-06-09; controls over M-22-18 where they conflict) → **both rescinded by M-26-05**
(2026-01-23). Verified from M-26-05's text and the OMB memoranda index (no later software-security
memo through M-26-19).

## Overview

Reaffirms M-22-18, **re-anchors the attestation deadlines** to the PRA approval of CISA's common
form (critical software +3 months, all software +6 months), and **clarifies scope**: attestations
come from the producer of the *end product*, which carries the burden for its third-party
components; free/publicly available proprietary software and freely obtained OSS are out of scope
(but still risk-assessed); agency-developed software is out, with contractor-developed software
decided by the CIO against an explicit six-phase SDL test. It tightens the **POA&M path**: an
agency may keep using software under a satisfactory POA&M only if it concurrently files an OMB
extension request carrying the POA&M; otherwise use must stop.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | defines who is accountable for third-party code in federal acquisition (2023-2026) |
| Cryptography | none | — |
| This project | adjacent | end-product accountability rule and compound approval guard inform R-042/DEC-009; relative milestones inform R-041; bears on R-041, R-042, R-044, DEC-009 |

## Implementations

Searched 2026-10-02: none specific; implemented through CISA's common form and RSAA (see
cisa-ssdf-attestation-form-2024).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; `updates` omb-m-22-18, `superseded_by` omb-m-26-05 |
| `distilled/README.md` | index |
| `distilled/normative.md` | 37 statements verbatim + Appendix A + definitions |
| `distilled/requirements.yaml` | 37 typed requirements, `status: rescinded`, `maps_to` the M-22-18 provisions they restate or override |
| `distilled/messages.yaml`, `protocol.*`, `state-machine.yaml` | changed documents, flows, lifecycle and milestones |
| `distilled/object-model.*` | object-model pass |
| `distilled/design-notes.md` | bearing on tmodel |

Local only: `.cache/omb-m-23-16.{pdf,txt,md}`.

## Limits

Rescinded. A delta document: unreadable without M-22-18. Leaves "satisfactory" undefined and
does not say how long a POA&M extension lasts.
