---
schema: "library-summary/v1"
id: omb-m-22-18
record: omb-m-22-18
type: summary
updated: "2026-10-02"
---

# M-22-18: Enhancing the Security of the Software Supply Chain through Secure Software Development Practices

|  |  |
|---|---|
| **Type** | spec (OMB memorandum to heads of executive departments and agencies) |
| **Maturity** | _unset_ — binding federal policy 2022-09-14 → **rescinded 2026-01-23** |
| **Authors** | Shalanda D. Young, Director, OMB |
| **Published** | 2022-09-14 |
| **Identifier** | OMB M-22-18 |
| **Source** | https://bidenwhitehouse.archives.gov/wp-content/uploads/2022/09/M-22-18.pdf (original whitehouse.gov URL now 404) |
| **Digest** | `85b119f5b1e50a2a9bfb2ae19a9c0f52472e94a8e08fe474141849a1a4f6c6c2` (8 pp, retrieved 2026-10-02) |

**Status / currency (checked 2026-10-02).** Updated by **M-23-16** (2023-06-09: new deadlines
anchored to PRA approval of the common form, scope clarifications, POA&M + mandatory extension
request). **Both rescinded by M-26-05** (2026-01-23, "Adopting a Risk-based Approach to Software
and Hardware Security"), verified from the memo itself and from the OMB memoranda index
https://www.whitehouse.gov/omb/information-resources/guidance/memoranda/ — no later OMB
software-security memo through M-26-19 (Sept 2026). EO 14306 (June 2025) had already removed
EO 14144's attestation-validation directives (see eo-14306). The CISA common form produced under
this memo remains available for optional use.

## Overview

Implements EO 14028 §4(k): agencies **must only use third-party software whose producer attests
to the NIST secure-development practices** (SP 800-218 SSDF + NIST's §4e supply-chain guidance).
The attestation is a *conformance statement* with three minimum elements; a FedRAMP 3PAO (or
agency-approved) assessment may replace it; a producer that cannot attest to some practices must
list them, document mitigations and develop a POA&M, which the agency may accept. Agencies *may*
additionally require SBOMs (NTIA formats), other artifacts and VDP evidence. It runs on a dated
program (inventory 90 d, process 120 d, critical-software attestations 270 d, all 365 d) and
directs CISA to build the common form and a government-wide attestation/artifact repository.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | the US federal acquisition gate for secure development 2022-2026 |
| Cryptography | none | no cryptographic content |
| This project | adjacent | not something tmodel conforms to, but its gate (attest / assess / POA&M / waive) and milestone chain are direct templates for R-041/R-042; bears on R-041, R-042, R-043, R-044, DEC-009 |

Topic: `sdl` (lane B, US policy).

## Implementations

Searched 2026-10-02. The memo's process was implemented by CISA's **Repository for Software
Attestations and Artifacts (RSAA)** and the common form (see cisa-ssdf-attestation-form-2024).
No open-source tooling implements the memo itself; vendors (e.g. GRC platforms) offered
attestation-tracking modules — none recorded here.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations (updated_by M-23-16, superseded_by M-26-05), distillation block |
| `distilled/README.md` | artifact index with coverage |
| `distilled/normative.md` | every statement verbatim + Appendix A + definitions |
| `distilled/requirements.yaml` | 58 typed requirements (`omb-m-22-18#II.1.a.ii-1` ...), all `status: rescinded` |
| `distilled/messages.yaml` | the documents exchanged (attestation, POA&M, SBOM, waiver ...) |
| `distilled/protocol.yaml` + `protocol.md` | agency/producer/OMB/CISA exchanges, Mermaid |
| `distilled/state-machine.yaml` | software-item lifecycle + milestone chain |
| `distilled/object-model.yaml` + `object-model.md` | object-model pass |
| `distilled/design-notes.md` | bearing on tmodel |

Local only (gitignored): `.cache/omb-m-22-18.pdf`, `.txt`, `.md` (full capture).

## Limits

- Rescinded: nothing here binds anyone after 2026-01-23; requirements are kept with
  `status: rescinded` for history and crosswalk.
- Points to "NIST Guidance" by reference; the practices themselves are in SP 800-218 and the
  common form, not here. Company-level self-attestation is a weak conformance signal (our assessment; M-26-05
  criticises M-22-18's "unproven and burdensome software accounting processes that prioritized
  compliance over genuine security investments").
- Undefined: what an agency does at a missed deadline with no extension (inferred `not-usable`),
  what "satisfactory" POA&M documentation means, and repository access rules.
