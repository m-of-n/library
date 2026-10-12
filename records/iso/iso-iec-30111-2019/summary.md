---
schema: "library-summary/v1"
id: iso-iec-30111-2019
record: iso-iec-30111-2019
type: summary
updated: "2026-10-02"
---

# ISO/IEC 30111:2019 — Information technology — Security techniques — Vulnerability handling processes

|  |  |
|---|---|
| **Type** | spec (International Standard) |
| **Maturity** | standard — published 2019-10, Edition 2; confirmed 2025; marked "to be revised" (90.92) |
| **Authors** | ISO/IEC JTC 1/SC 27 |
| **Published** | 2019-10 (EN ISO/IEC 30111:2020 adopted by CEN/CLC JTC 13 without modification, 2020-05) |
| **Identifier** | ISO/IEC 30111:2019 (replaces ISO/IEC 30111:2013) |
| **Source** | https://www.iso.org/standard/69725.html (catalogue; paywalled) — read via the free preview https://cdn.standards.iteh.ai/samples/69725/127b437f4f0c4b9196fd5b8d3fd294b1/ISO-IEC-30111-2019.pdf |
| **Digest** | `5a2f9235b70896ecece35a823aebbe3a3151a471888c232d776bbc2658ec08b8` (11-page preview PDF, not the standard) |

## Overview

The vendor-internal companion to ISO/IEC 29147: how a vendor organises (policy, leadership, PSIRT,
divisions, contacts) and runs (preparation, receipt, verification, remediation development, release,
post-release) the handling of potential vulnerabilities, whether reported externally or found
internally. Its single visible hard requirement is that a vendor **shall develop and maintain an
internal vulnerability handling policy** (§6.3), recommended to include responsibilities, responsible
roles, safeguards against premature disclosure and a **target schedule for remediation development**.
It normatively references 29147:2018 and says the two "shall be used in conjunction" (§5.1), sharing
one Figure 1 that splits the lifecycle at "Acknowledge receipt → Verify report".

## Version and access verified (2026-10-02)

- **Current edition:** 2019 (Edition 2). Per the iso.org catalogue page (https://www.iso.org/standard/69725.html,
  via search-engine snapshots — iso.org returned HTTP 403 to curl and WebFetch): last reviewed and confirmed
  in 2025, now stage **90.92 "to be revised"**. **Edition 3 is in preparation:** registered 2025-10-08 as ISO/IEC AWI 30111
  "Cybersecurity — Vulnerability handling and disclosure processes", https://www.iso.org/standard/92946.html;
  per ISO open data (deliverables metadata, Last-Modified 2026-09-30, read in the verify pass) it is now
  **ISO/IEC WD 30111.2, stage 20.60** (second working draft, comment period closed) — the new title suggests it may absorb disclosure (29147).
- **European adoption:** EN ISO/IEC 30111:2020, approved by CEN 2020-05-03 and taken over by
  CEN/CLC/JTC 13 "Cybersecurity and Data Protection" without modification (seen in the SIST EN ISO/IEC
  30111:2020 preview, https://cdn.standards.iteh.ai/samples/69311/c6a4832600f241eaa22d2d4d3f536a22/SIST-EN-ISO-IEC-30111-2020.pdf).
  JTC 13 is also the CRA standardisation committee.
- **Not free;** never on ISO's Publicly Available Standards list. Read: the free sample from
  iTeh Standards — the sales platform of SIST (Slovenian national body), not the ISO OBP preview the lane brief names (11 PDF pages, Clauses 1–6.5.3.4), captured to `.cache/iso-iec-30111-2019.md` and corrected
  against rendered page images where the preview watermark overlays text.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | the reference vendor-side vulnerability handling process; basis for PSIRT practice and for CRA Annex I Part II-style obligations |
| Cryptography | none | — |
| This project | adjacent | per-vulnerability lifecycle for Finding/MitigationInstance (DEC-009), policy as a governed and checkable document (R-042, R-043), process-kind mitigation (R-040), SDL coverage and root-cause feedback (R-041), crosswalk (R-044) |

## Implementations

Searched 2026-10-02 (ecosystem knowledge, not a survey). Process standards have no reference
implementation; practice frameworks and tooling:

| Name | Kind | License | URL |
|---|---|---|---|
| FIRST PSIRT Services Framework (cited as [4]) | practice framework | FIRST | https://www.first.org/standards/frameworks/psirts/ |
| OASIS CSAF 2.x + VEX profile | advisory / exploitability format for Release phase | OASIS IPR | https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html |
| DefectDojo, OWASP Dependency-Track | open source vulnerability tracking | BSD-3 / Apache-2.0 | https://github.com/DefectDojo/django-DefectDojo · https://github.com/DependencyTrack/dependency-track |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; `distillation` lists every artifact and its coverage |
| `distilled/README.md` | index of artifacts, coverage and what was not produced |
| `distilled/normative.md` | all 30 visible normative statements + 2 inferred, verbatim, clause order |
| `distilled/requirements.yaml` | the same 32 as `library-requirements/v2` with counts and reconciliation |
| `distilled/state-machine.yaml` | per-vulnerability handling lifecycle (shared with 29147) |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass (18 objects, 19 edges) |
| `distilled/design-notes.md` | bearing on ARCH-0001 / R-040–R-044 / DEC-009 |

## Limits

- **Coverage is the free preview only:** all of Clause 6 up to §6.5.3.4 is read; §6.5.4 (staff
  capabilities), §6.6–6.8, **Clause 7 (the handling phases, monitoring, confidentiality)**, Clause 8
  (supply chain) and Annex A (summary of normative provisions) are not. The phase states in
  `state-machine.yaml` come from Figure 1 and headings; their entry/exit criteria are unknown.
  Status is `summarized`, deliberately.
- The 6.2 leadership text is generic ISO management-system wording; it is extracted but carries little
  design signal.
- Edition 3 (WD 30111.2, stage 20.60 per ISO open data 2026-09-30) may merge with 29147; clause numbers will move.
