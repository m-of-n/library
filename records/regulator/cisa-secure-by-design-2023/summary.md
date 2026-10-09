---
schema: "library-summary/v1"
id: cisa-secure-by-design-2023
record: cisa-secure-by-design-2023
type: summary
updated: "2026-10-02"
---

# Shifting the Balance of Cybersecurity Risk: Principles and Approaches for Secure by Design Software

|  |  |
|---|---|
| **Type** | spec (joint government guidance, TLP:CLEAR) |
| **Maturity** | best-practice (voluntary guidance; not regulation) |
| **Authors** | CISA, NSA, FBI and 15 international partners (ACSC, CCCS, NCSC-UK, BSI, NCSC-NL, NCSC-NO, CERT NZ, NCSC-NZ, KISA, INCD, NISC, JPCERT/CC, CSIRT Americas, CSA Singapore, NÚKIB) |
| **Published** | April 2023; this record tracks the **2023-10-25 revision** |
| **Identifier** | https://www.cisa.gov/resources-tools/resources/secure-by-design |
| **Source** | https://www.cisa.gov/sites/default/files/2023-10/SecureByDesign_1025_508c.pdf (bytes from the Internet Archive id_ copy; cisa.gov returns 403 to scripts) |
| **Digest** | `774b82b17e5cf7776d21389a95f7db4a61e0363840c1c1554d3428dabce583b6` (36 pp, retrieved 2026-10-02) |

**Currency (checked 2026-10-02).** The CISA resource page lists the initial April 2023 edition and
the revision of 2023-10-25 (8 new international co-sealers; expands the three principles and how
manufacturers *demonstrate* them). No later revision found. The follow-on documents are separate
lines: the Secure by Design Pledge (May 2024, cisa-secure-by-design-pledge-2024), the Secure by
Demand Guide (Aug 2024, cisa-secure-by-demand-guide-2024), the OT Secure by Demand priorities
(Jan 2025, cisa-secure-by-demand-ot-2025), plus Secure by Design Alerts and "Product Security Bad
Practices" (not held).

## Overview

Argues that the burden of security must shift from customers to software manufacturers. Three
principles: **(1) take ownership of customer security outcomes**, **(2) embrace radical
transparency and accountability**, **(3) lead from the top** (build organizational structure and
leadership). For each principle the guide lists practices to *demonstrate* it, grouped as
secure-by-default, secure product development, and pro-security business practices — most of
them as things to **publish** (memory-safety roadmap, secure-by-design roadmap, SBOMs, a
vulnerability disclosure policy, complete CVE records with CWE root cause, high-level threat
models, SDLC self-attestations, a named executive sponsor, board reporting). It adds 12
secure-by-design tactics (many tagged with SSDF tasks: memory-safe languages PW.6.1, components
PW.4.1, parameterized queries PW.5.1, SAST/DAST PW.7.2/PW.8.2, SBOM PS.3.2, VDP RV.1.3 …),
8 secure-by-default tactics (no default passwords, MFA for privileged users, SSO, free logging,
authorization profiles, forward-looking security over backwards compatibility, …) and
recommendations for customers.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | the US-led international baseline for manufacturer secure-by-design accountability |
| Cryptography | none | no cryptographic content beyond naming MFA/SSO standards |
| This project | core | "publish high-level threat models" (P2-DEV-2) makes the threat model itself a governed public artifact (R-043); practices typed technical/documentation/process (R-040); public-evidence conformance (R-042); SSDF tags are crosswalk edges (R-044); executive sponsor/roadmap as SDL governance (R-041); DEC-009 |

## Implementations

Searched 2026-10-02. Not a technical spec. CISA tracks adoption through the Pledge and its progress
reports; CISA's VDP template and the CPGs are companion resources. No open-source tool that
checks conformance to these principles found.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, 18 authoring agencies, cites (SSDF, CRA, IEC 62443-4-1, numbered and in-text refs), distillation |
| `distilled/README.md` | index with coverage |
| `distilled/normative.md` | every normative statement verbatim in source order, with excluded statements listed |
| `distilled/requirements.yaml` | 152 entries (3 principles, 37 demonstrating practices P1/P2/P3, 12 SbD + 8 SbDef tactics, customer recommendations, narrative recommendations); own-form counts reconciled; `maps_to` only where the source prints SSDF ids |
| `distilled/object-model.yaml` + `.md` | object-model pass, 58 objects / 38 edges / 9 gaps, Mermaid |
| `distilled/design-notes.md` | adopt/adapt/reject vs R-040..R-044, DEC-009, R-036 |

Local only: `.cache/cisa-secure-by-design-2023.{pdf,txt,md}`.

## Limits

Voluntary and evidence-light: it asks manufacturers to *publish* and *commit*, but defines no
pass/fail criteria, gates, metrics thresholds or verification method; most items are
`testable: partial`. It is software-manufacturer centric (enterprise IT), with OT/ICS only by
reference. No schema for any of the artifacts it asks to be published (those live in SBOM, CVE,
VDP and attestation records).
