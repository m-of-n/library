---
schema: "library-summary/v1"
id: iec-81001-5-1-2021
record: iec-81001-5-1-2021
type: summary
updated: "2026-10-02"
---

# IEC 81001-5-1:2021: Health software and health IT systems safety, effectiveness and security. Part 5-1: Security, activities in the product life cycle

|  |  |
|---|---|
| **Type** | spec (International Standard, double logo IEC/ISO) |
| **Maturity** | standard |
| **Authors** | Joint Working Group of IEC SC 62A (TC 62) and ISO/TC 215 |
| **Published** | Edition 1.0, 2021-12; **corrected version 2025-12** incorporating Interpretation Sheet 1 (IEC 81001-5-1:2021/ISH1:2025, 62A/1692/DISH, voting report 62A/1706/RVDISH) |
| **Identifier** | IEC 81001-5-1:2021; EN IEC 81001-5-1:2022; ISO page https://www.iso.org/standard/76097.html |
| **Source** | https://webstore.iec.ch/en/publication/63293 (paywalled, 56 pp). Read: the free bilingual preview, 30 pp |
| **Digest** | preview `b4d73b515d0eb927b771f03b8f45acf5e2aba2332e18b84c50358cab7bc96a58` (retrieved 2026-10-02) |

## Overview

IEC 81001-5-1 is the health-software adaptation of IEC 62443-4-1. Its process requirements (Clauses 4-9) "have been
derived from the IEC 62443-4-1 PRODUCT LIFE CYCLE management". They are arranged in the ordering of IEC 62304 so that a
medical-software manufacturer can extend its existing 62304 processes rather than build a second lifecycle (0.1).

Conformance can be claimed two ways:
- full conformance, by implementing Clauses 4-9;
- for legacy (transitional) health software, by implementing Annex F only (0.3).

Interpretation Sheet 1 (2025) clarifies the **risk transfer** from manufacturer to operator through a nested
classification of software items (MAINTAINED ⊂ SUPPORTED ⊂ REQUIRED). Only maintained items carry the manufacturer's
security-update delivery and integrity duties.

## Version and currency (checked 2026-10-02)

- **IEC.** Edition 1.0 remains current. The webstore offers a **corrected version 2025-12** containing ISH1:2025, and
  that version is what we read. No amendment has been published. *(Corrected in the verify pass.)* A second
  edition is under way: ISO open data (deliverables metadata, Last-Modified 2026-09-30) lists IEC 81001-5-1:2021
  at stage 90.92 (to be revised) and **IEC/AWI 81001-5-1, Edition 2** (project 92904) at stage 10.99 (new project
  approved).
- **FDA.** Recognized consensus standard **13-122**, recognised 2022-12-19. This rests on a secondary source (MD101
  Consulting blog); the FDA database page was not opened. FDA's premarket guidance (Feb 2026) names it as a candidate
  SPDF (record `fda-premarket-cybersecurity-guidance`, §V, fn 48).
- **EU.**
  - EN IEC 81001-5-1:2022 is the European adoption.
  - Commission Implementing Decision (EU) 2026/1231 of 11 June 2026, the latest amendment to the MDR harmonised-standards
    Decision 2021/1182, does **not** cite it (EUR-Lex, checked).
  - A secondary source gives a planned harmonisation date of 27 May 2028 under standardisation request M/575. This was
    not verified.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Secure-lifecycle process standard for all health software (SiMD, SaMD, health IT). |
| Cryptography | none | Nothing cryptographic is readable in the free material. |
| This project | adjacent | It bears on **R-041** (a 62304-ordered process-area line as the phase/gate sequence), **R-042** (two conformance routes), **R-044** (a partial-strength mapping to 62443-4-1) and **DEC-009** (software-item support classes and risk transfer). It is adjacent rather than core because the normative text is unread. |

## Implementations

Searched 2026-10-02. There are no open-source implementations; it is a process standard. Certification and
assessment services exist (e.g. IECEE CB scheme, notified-body and test-house services). None was evaluated.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; distillation block (not FX-1, paywalled) |
| `distilled/README.md` | artifact index with honest coverage |
| `distilled/normative.md` | ISH1 complete, Introduction, Scope, Figure 2, title-only ToC |
| `distilled/requirements.yaml` | 57 title-only activities + 7 ISH1 statements |
| `distilled/state-machine.yaml` | software-item category downgrade; conformance route |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass (24 objects, 20 edges) |
| `distilled/design-notes.md` | adopt / adapt / reject, open questions |

## Limits

- **Paywalled. Clause 3 (terms), Clauses 4-9 (all normative activities) and Annexes A-G were not read.** No
  requirement text exists in this record beyond ToC titles and ISH1, and the true count of "shall" statements is
  unknown.
- The mapping to 62443-4-1 in `requirements.yaml` is our inference from titles. The standard's own Annex D mapping was
  not available.
- Finishing this record needs the purchased standard, or a licensed copy of EN IEC 81001-5-1.
