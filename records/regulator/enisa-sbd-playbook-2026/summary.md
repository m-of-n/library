---
schema: "library-summary/v1"
id: enisa-sbd-playbook-2026
record: enisa-sbd-playbook-2026
type: summary
updated: "2026-10-02"
---

# ENISA Secure by Design and Default Playbook — A Practical Guide to Secure by Design and Default Principles for SMEs

|  |  |
|---|---|
| **Type** | spec (agency guidance / playbook) |
| **Maturity** | best-practice — EU agency guidance, non-binding ("does not endorse a regulatory obligation", Legal notice); "introductory guidance rather than a comprehensive compliance manual" (§1.2) |
| **Authors** | European Union Agency for Cybersecurity (ENISA); public consultation April–May 2026 (28 contributions, named contributors listed) |
| **Published** | Version 1.0, July 2026 (PDF created 2026-07-30) |
| **Identifier** | ISBN 978-92-9204-802-0; doi:10.2824/4422633; TP-01-26-016-EN-N |
| **Source** | https://www.enisa.europa.eu/sites/default/files/2026-07/ENISA_Secure_By_Design_and_Default_Playbook_v1.pdf |
| **Digest** | `c0dc5132d162f1a06f0adab350226070a176d24b9b826a85b5874961633d357d` (80 pages; CC BY 4.0) |

**Version check (2026-10-02):** the PDF states "Version: 1.0", "JULY 2026", and "prepared following a public consultation held by ENISA during April 2026 and May 2026" — this is the final v1.0 after the consultation draft; no later version found. Licence: CC BY 4.0 (reuse with attribution and indication of changes).

## Overview

The playbook turns secure by design and secure by default into repeatable engineering actions for small and medium-sized manufacturers of products with digital elements. It frames security across six life-cycle processes (requirements → maintenance and disposal) driven by lightweight risk management and Shostack-style threat modelling (Tables 1–3, each activity with a concrete one-page deliverable), then states 22 principles in four groups — architectural foundations (trust boundaries/threat modelling, least privilege, strong identity, attack-surface minimisation, defence in depth, open design), operational integrity (life-cycle, user-centric design, secure coding, logging, configuration/change, incident response, vulnerability/patch, supply chain), default hardening (minimised services, restrictive initial access, secure communication, unique device identity/secrets) and guided protection (mandatory onboarding, automated updates, transparent posture, secure recovery/ownership). Each principle becomes a one-page playbook with a checklist, the *minimum evidence* that proves it, and a copy-and-paste *release gate* of pass/fail criteria (125 in total). Section 5 argues for manufacturer-issued, machine-processable attestations (control → implementation → verification layers; OSCAL, CycloneDX CDXA, SPDX 3, SLSA/in-toto, TEA) with a worked SafeGate-X1 example; Annex C maps each principle to CRA Annex I essential requirements (indicative).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | complete secure by design/default practice set with evidence and gates |
| Cryptography | adjacent | crypto agility, PQC readiness, per-device keys, signed updates/artefacts (4.17, 4.18, 4.14) |
| This project | core | R-041 (125 release-gate criteria, go/no-go gate), R-042 (evidence + attestation cascade), R-043 (refresh triggers), R-044 (Annex C → CRA), R-040 (secure defaults), DEC-009 (dispositions with expiry) |

## Relations

- Maps to `eu-cra-2024-2847` (Annex B reproduces Annex I with ENISA ids; Annex C maps principles).
- Peers: `etsi-ts-104-219`, `bsi-tr-03183-1`, `bsi-tr-03185`, `cisa-secure-by-design-2023`; cites `owasp-samm-2`, `owasp-asvs-5`, `nist-sp-800-160`, `slsa-1-2`, `spdx-3-0-1`, `cyclonedx-1-7`, `openssf-scorecard-checks`, `openssf-osps-baseline`.

## Implementations

Searched 2026-10-02: none implements the playbook as such; Section 5.3 lists building blocks (OSCAL, CycloneDX CDXA and Assessors Studio, SPDX 3.0 Security Profile, OpenSSF Security Insights/Scorecard/Best Practices/Baseline, SLSA, in-toto + Sigstore Cosign, Transparency Exchange API, Device Security Passport).

| Name | Kind | License | URL |
|---|---|---|---|
| CycloneDX Assessors Studio | attestation assessment tool | OSS (Apache-2.0 per project) | https://github.com/CycloneDX/cyclonedx-assessors-studio |
| NIST OSCAL | compliance-as-code format | public domain | https://pages.nist.gov/OSCAL/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, cites, distillation |
| `distilled/README.md` | artifact index |
| `distilled/normative.md` | §2–§5 normative content, all 22 playbooks, Annex C |
| `distilled/requirements.yaml` | 550 entries (incl. 67 prose recommendations, 39 added by the verify pass) + 22 principles with CRA `maps_to` |
| `distilled/messages.yaml`, `schema/` | 11 structures, 11 JSON Schemas (one validated against the Fig. 5 fixture) |
| `distilled/protocol.yaml`, `protocol.md` | release gate, vulnerability, attestation flows |
| `distilled/state-machine.yaml` | 5 lifecycles |
| `distilled/examples/` | SafeGate-X1 example + Figure 5 JSON |
| `distilled/object-model.yaml`, `.md` | 39 objects, 19 edges, 7 gaps |
| `distilled/design-notes.md` | adopt/adapt/reject; defects |

## Limits

- Non-binding and explicitly not a compliance route; Annex C is indicative.
- SME-oriented "minimum viable" depth — higher-risk products need "a more comprehensive analysis" (§2.3).
- No assessment scheme beyond self-run release gates; attestation is illustrative, no schema.
- Defects: undefined "MRSM", 443-only vs 443/22 contradiction, elided evidence hash, duplicated gate criteria across design/default playbooks (design-notes.md).
