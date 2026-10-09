---
schema: "library-summary/v1"
id: bsi-tr-03183-1
record: bsi-tr-03183-1
type: summary
updated: "2026-10-02"
---

# BSI TR-03183-1 — Cyber Resilience Requirements for Manufacturers and Products, Part 1: General requirements

|  |  |
|---|---|
| **Type** | spec (BSI Technical Guideline) |
| **Maturity** | best-practice — non-binding national guidance; "does NOT establish any obligations ... [or] provide presumption of conformity" (§2); "living document" |
| **Authors** | Bundesamt für Sicherheit in der Informationstechnik (BSI) |
| **Published** | v1.0.0, 2026-07-31 (cover "Date: 31.07.2026"; BSI press release of 05.08.2026 "Technische Richtlinie TR-03183-1 in Version 1.0.0 veröffentlicht" confirms the 2026 release; changelog misprints 2025-07-31) |
| **Identifier** | BSI TR-03183-1 v1.0.0 |
| **Source** | https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TR03183/BSI-TR-03183-1_v1_0_0.pdf?__blob=publicationFile&v=3 (landing: https://bsi.bund.de/dok/TR-03183-en) |
| **Digest** | `db5f5bfed4664faae75d13f3deb0c9140d13f8d10764f013b84e5ca912b969ef` (79 pages; re-downloaded 2026-10-02, identical hash) |

**Version check (2026-10-02, re-checked by the verifier 2026-10-03):** the TR-03183 landing page lists Part 1 as "a living document currently published in version 1.0.0"; its current download link is labelled "... Part 1: General requirements Version 1.0.0", and v0.9.0 and v0.10.0 are listed as archive versions. BSI press release 05.08.2026 (https://www.bsi.bund.de/DE/Service-Navi/Presse/Alle-Meldungen-News/Meldungen/2026/TR-03183_Einstiegshilfe_CRA_260805.html) announces v1.0 and the OSCAL measures. Sibling parts on the same page: Part 2 SBOM v2.1.0 (a v2.2.0 PDF is also linked), Part 3 Vulnerability Reports and Notifications v1.0.0, Part H Module H conformity v1.1.0 (30/05/2026).

## Overview

TR-03183-1 is BSI's reading of the EU Cyber Resilience Act for manufacturers "who have not yet established mature IT security processes". It summarises the CRA (scope, timeline, obligations, conformity routes, product categories, Annex I verbatim), then gives an assessment method (evaluator, scope, PASS/FAIL/N/A verdicts, report contents that double as Article 31 technical documentation) and an ISO 31000-based risk-handling method of eleven MUST activity controls (asset identification → threat modelling → analysis → evaluation → control selection → essential-requirement applicability → risk sharing → implementation/verification → documentation → update). Its distinctive contribution is "Adaptable Risk-based Controls": each control carries a risk scenario (minimum C/I/A impact × environment of access restriction, interface restriction and user capability) so that control selection is a match against a product's risk profile; the control catalogue itself is published separately in OSCAL (access on request). Annex C works the method through a home network camera; Annex D adds an experimental scoring scheme.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | CRA-oriented risk assessment + control selection + conformity self-assessment |
| Cryptography | adjacent | "state of the art cryptography" defined by reference (TR-02102, ECCG ACM) only |
| This project | core | R-040 (Activity/Mechanism/Documentation = process/technical/documentation), R-042 (PASS/FAIL/N/A, applicability statement), R-044 (CRA sub-ids ER/VH), DEC-003 (impact tables), DEC-009 (risk sharing, acceptance) |

## Relations

- Interprets `eu-cra-2024-2847` (Annex I quoted with BSI sub-ids; every control carries "Reference CRA").
- Sibling of `bsi-tr-03185` (BSI's SDL process TR) — TR-03183-1 has no SDL process requirements of its own.
- Other parts of the same series (not held as records): Part 2 SBOM (v2.1.0), Part 3 vulnerability reports and notifications (v1.0.0), Part H conformity based on full quality assurance / Module H (v1.1.0).
- Peers: `etsi-ts-104-219` (Annex A maps CRA → SSDIF), `enisa-sbd-playbook-2026` (Annex C maps principles → CRA).

## Implementations

Searched 2026-10-02: BSI's OSCAL control repository (github.com/tr-03183/tr-03183-1, access on request); BSI CycloneDX taxonomy namespace for Part 2 (BSI GitHub). No independent tool found.

| Name | Kind | License | URL |
|---|---|---|---|
| TR-03183-1 OSCAL controls | control catalogue | on request | https://github.com/tr-03183/tr-03183-1 |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, cites, distillation |
| `distilled/README.md` | artifact index with coverage |
| `distilled/normative.md` | §2, §4–§7, Appendix B, Annex D verbatim |
| `distilled/requirements.yaml` | 94 entries (12 RH MUST statements, 1 example control, 45 prose obligations, 36 CRA ER/VH) with `maps_to` CRA (target ids into `eu-cra-2024-2847`) |
| `distilled/messages.yaml`, `schema/` | 9 structures + derived JSON Schemas |
| `distilled/protocol.yaml`, `protocol.md` | risk handling, assessment, CRA reporting flows |
| `distilled/state-machine.yaml` | risk, control verdict, PwDE market lifecycle |
| `distilled/examples/` | Annex C camera, §6.5 ARC selection, D.2 matrix vectors |
| `distilled/object-model.yaml`, `.md` | 40 objects, 26 edges, 7 gaps |
| `distilled/design-notes.md` | adopt/adapt/reject; source defects |

## Limits

- Non-binding; no presumption of conformity; a PASS is not CRA compliance (§4.7).
- The actual control catalogue (Chapter 7, OSCAL) is not in the PDF and was not available, so the requirement set here is the method, not the controls.
- No secure-development process content (see TR-03185); Part I only, vulnerability-handling detail is in Part 3.
- Defects: §5.14.1/§5.14.2 truncated, Table 6 missing; Appendix B lacks ER.3/ER.8/VH.2 and truncates ER.14; Annex D formula and matrix orientation inconsistent; date conflict in changelog. Details in design-notes.md.
