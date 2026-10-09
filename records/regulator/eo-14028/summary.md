---
schema: "library-summary/v1"
id: eo-14028
record: eo-14028
type: summary
updated: "2026-10-02"
---

# Executive Order 14028: Improving the Nation's Cybersecurity

|  |  |
|---|---|
| **Type** | spec (presidential executive order) |
| **Maturity** | _unset_ — binding on the executive branch; in force |
| **Authors** | President Joseph R. Biden Jr. |
| **Published** | signed 2021-05-12; 86 FR 26633 (2021-05-17), FR Doc. 2021-10460 |
| **Identifier** | EO 14028 |
| **Source** | https://www.govinfo.gov/content/pkg/FR-2021-05-17/pdf/2021-10460.pdf |
| **Digest** | `250578b7bdd468cb67e4f64d332f6648694302257670ae966d37b21aa138a282` (15 pp, retrieved 2026-10-02) |

**Topic note.** This record keeps its original `topic: supply-chain-attestation`; the SDL lane uses
it too (tag `sdl`).

**Status / currency (checked 2026-10-02 against the texts of EO 14144 and EO 14306).** EO 14028
is in force and is not amended (verifier 2026-10-03: the Federal Register document record for 2021-10460 lists only "See: EO 14141, EO 14144" — no "Amended by"; EO 14306's own disposition note lists "Amends: EO 13694; EO 14144"). **EO 14144** (2025-01-16) built on §4 with RSAA
machine-readable attestations, CISA validation of attestations with public results and AG
referral, FAR amendments and an SSDF update. **EO 14306** (2025-06-06) *struck* EO 14144 §2(a)–(b)
— the attestation-validation and FAR-attestation part — and re-dated the SSDF directives (NCCoE
consortium by 2025-08-01, SP 800-53 patch guidance by 2025-09-02, preliminary SSDF update by
2025-12-01, final within 120 days), dropping EO 14144's directions to fold SSDF updates into
M-22-18 and revise CISA's form. Separately, **OMB M-26-05** (2026-01-23) rescinded M-22-18 and
M-23-16, the §4(k) implementation, so collecting attestations is no longer mandatory for agencies.

## Overview

§4 ("Enhancing Software Supply Chain Security") sets up the US federal secure-software regime:
NIST guidance (→ SSDF) that must cover ten practice areas — secure development environments
(separate build environments, audited trust relationships, MFA/conditional access, minimised
dependencies, encryption, monitoring/IR), conformance artifacts, automated source-supply-chain
integrity, automated vulnerability checks "at a minimum prior to product, version, or update
release", tool-execution artifacts plus a **public summary of risks assessed and mitigated**,
provenance and component controls, an SBOM per product, a VDP, attestation of conformity, and
OSS integrity/provenance. It orders NTIA's SBOM minimum elements, a "critical software"
definition and measures, OMB requirements on agencies (with extensions/waivers), FAR contract
language for attestation, vendor testing standards, and consumer IoT/software labeling pilots.
Rest of the order (threat sharing, zero trust, CSRB, playbook, EDR, logging) is out of SDL scope.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | origin of SSDF, SBOM minimum elements, the attestation form and the CISA SbD wave |
| Cryptography | adjacent | §4(e)(i)(E) "employing encryption for data" only |
| This project | core | §4(e) ids are the crosswalk hub (R-044); release gate (R-041); public risk summary as governed threat-model view (R-043); attestation/conformance (R-042); DEC-009 |

## Implementations

Searched 2026-10-02: the order is implemented by documents, several held here — SP 800-218
(SSDF), ntia-2021-sbom-minimum, omb-m-22-18/omb-m-23-16 (rescinded), cisa-ssdf-attestation-form-2024;
not held: NIST §4e guidance (2022-02-04), NISTIR 8397 (§4(r)), OMB M-21-30 (§4(j)).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, distillation |
| `distilled/README.md` | index |
| `distilled/normative.md` | §4 verbatim + §10 definitions |
| `distilled/requirements.yaml` | 53 typed §4 statements (`eo-14028#§4(e)(i)(A)` …) |
| `distilled/state-machine.yaml` | §4 milestone dependency chain |
| `distilled/object-model.*` | object-model pass |
| `distilled/design-notes.md` | bearing on tmodel |

Local only: `.cache/eo-14028.{pdf,txt,raw.txt,clean.txt,s4.clean.txt,md}`.

## Limits

§4 obliges *officials*, not producers; producer obligations exist only via OMB/FAR, now largely
withdrawn (M-26-05). All deadlines are historical. Practice areas are topics, not testable
requirements.
