---
schema: "library-summary/v1"
id: omb-m-26-05
record: omb-m-26-05
type: summary
updated: "2026-10-02"
---

# M-26-05: Adopting a Risk-based Approach to Software and Hardware Security

|  |  |
|---|---|
| **Type** | spec (OMB memorandum to heads of executive departments and agencies) |
| **Maturity** | _unset_ — current binding federal policy |
| **Authors** | Russell T. Vought, Director, OMB |
| **Published** | 2026-01-23 |
| **Identifier** | OMB M-26-05 |
| **Source** | https://www.whitehouse.gov/wp-content/uploads/2026/01/M-26-05-Adopting-a-Risk-based-Approach-to-Software-and-Hardware-Security.pdf |
| **Digest** | `54d5132e19ab394b20fad0fbec57a945320a7cda1918f499fb594ad9af2167ab` (2 pp, retrieved 2026-10-02) |

**Currency (checked 2026-10-02).** Listed on the OMB memoranda index
https://www.whitehouse.gov/omb/information-resources/guidance/memoranda/; the index shows no later
memo on software/hardware assurance through M-26-19 (2026-09). Secondary confirmation: law-firm
alerts of Feb 2026 (Covington "OMB Rescinds the 'Common Form' Secure Software Attestation
Requirement"; Mayer Brown; Crowell) seen as web-search results only; this record is extracted from the
memo itself.

## Overview

Rescinds M-22-18 and M-23-16: the uniform requirement that agencies obtain a secure-development
self-attestation (CISA common form) before using software ends. Accountability is placed on each
**agency head**; agencies **should** validate provider security using secure development
principles on a comprehensive risk assessment, and **shall** keep a complete software *and
hardware* inventory and develop assurance policies matched to their risk and mission. The
attestation form and SBOM-on-request contract terms remain **optional** tools (for cloud
platforms, an SBOM of the runtime production environment); SSDF, CISA's 2025 SBOM minimum
elements draft and CISA's HBOM framework are listed as references.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | current US federal software/hardware assurance policy |
| Cryptography | none | — |
| This project | adjacent | conformance must be a selectable profile, not one mandated baseline (R-042, R-044); inventory as governed view (R-043) |

## Implementations

Searched 2026-10-02: none (policy memo). Agencies may still use CISA's RSAA/common form.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; `supersedes` omb-m-22-18 and omb-m-23-16 (rescission) |
| `distilled/README.md` | index |
| `distilled/normative.md` | every statement verbatim + references + rationale |
| `distilled/requirements.yaml` | 9 typed statements `omb-m-26-05#R-0001..0009` |
| `distilled/object-model.*` | object-model pass |
| `distilled/design-notes.md` | bearing on tmodel |

Local only: `.cache/omb-m-26-05.{pdf,txt,md}`. The PDF text layer has OCR-like errors ("0MB",
"Dlfector"); quotes use the intended characters and say so.

## Limits

Two pages, mostly permissive; defines no process, timeline or evidence format. Does not say
what "secure development principles" are (no named baseline), nor how agencies evidence a
"comprehensive risk assessment".
