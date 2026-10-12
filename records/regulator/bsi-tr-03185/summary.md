---
schema: "library-summary/v1"
id: bsi-tr-03185
record: bsi-tr-03185
type: summary
updated: "2026-10-02"
---

# BSI TR-03185 Secure Software Lifecycle

|  |  |
|---|---|
| **Type** | spec (German federal Technical Guideline, *Technische Richtlinie*) |
| **Maturity** | best-practice. It is a BSI Technical Guideline, voluntary unless referenced, and offered for certification of Part 1. |
| **Authors** | Bundesamt für Sicherheit in der Informationstechnik (BSI). Editors per the history tables: Mg, fvs, fd (v1.1.1); jdl, fvs (Part 2). |
| **Published** | v1.1.1 dated 2026-07-02 (PDF created 2026-08-20). It merges TR-03185(-1) v1.0 (2024) and TR-03185-2 v1.1.0 (2025-08-18). |
| **Identifier** | BSI TR-03185, short URL https://www.bsi.bund.de/dok/TR-03185-en |
| **Source** | https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TR03185/BSI-TR-03185.pdf?__blob=publicationFile&v=5 |
| **Digest** | `199c87754dec3eab884c18da6c3f6030e6fa7ced282f06e87fed7fe7841e8329` (51 pp., retrieved 2026-10-02) |

## Overview

TR-03185 is Germany's federal secure-software-lifecycle requirement set. Part 1 covers proprietary software:
169 requirements with native ids. BSI compiled them from IT-Grundschutz (CON.8, APP.6, OPS.1.1.3, OPS.1.1.6,
ORP), GSMA NESAS FS.16, IEC 62443-4-1 and NIST SSDF, and wrote them with capitalised MUST/SHOULD/MAY.

The distinctive move is to split every requirement by the manufacturer's **perspective**:

- **Software user** (`USER.*`): the manufacturer as a user of its own development tools. This covers
  selection, trusted acquisition, environment hardening, testing, installation, patching and decommissioning
  of the toolchain.
- **Software producer** (`PROD.*`): the manufacturer as producer of the product. This covers project
  management, documentation, development (design, threat modelling, architecture, design review, development
  testing, third-party components, code management, build tools, inventory), testing and release, delivery,
  vulnerability management and decommissioning.

Part 2 adds 20 deliberately minimal requirements for open-source projects (GV/LE/QA/BR/VM/DE). It is aligned
with the CRA and OpenSSF OSPS Baseline, and it assigns no single responsible party. v1.1.1 also brings AI
code assistants, LLMs and AI vulnerability scanners into scope as "resources and tools used". BSI strongly
recommends AI-based vulnerability scanners.

**Version verified (2026-10-02):**

- The German landing page states: "Im Jahr 2026 wurden die beiden Teile in einem englischsprachigen Dokument
  TR-03185 zusammengeführt" (in 2026 the two parts were merged into one English-language document). The
  English download is v1.1.1, and the separate TR-03185-2 PDF URL no longer serves a PDF.
- Pages checked:
  - https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03185/tr-03185.html
  - https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03185/tr-03185.html
  - https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TR03185/BSI-TR-03185.html
- The German *TR-03185-1 Sicherer Software-Lebenszyklus* v1.0 (06.08.2024) is still published. It remains the
  **certification basis**: BSI certifies Part 1 only, and audits are performed by IT-Grundschutz audit team
  leaders. That PDF (sha256 `5f507a35…72ddb0`) was used only to cross-check ids and dates.
- BSI's *Anforderungen und Prüfspezifikation v1.0* (xlsx, 2026-01-09) maps every Part 1 requirement to its
  sources and carries the audit columns.

**Record decision.** We hold one record per document line, and BSI itself merged the two parts into a single
document. So this record tracks the merged TR-03185, and no separate `-1`/`-2` records were created.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | It is a complete SDL requirement set from a national authority, with a certification scheme. |
| Cryptography | adjacent | Crypto appears only as integrity mechanisms (checksums, signatures, PROD.REL.1, USER.PM.C.8), protection of code-signing keys (USER.PM.C.6) and certificate handling in tools. |
| This project | core | Threat modelling is a mandatory, content-specified work product (PROD.DEV.C.1–C.5). The release gate's exit criteria are stated. BSI publishes a requirement-level crosswalk to IEC 62443-4-1 and SSDF. |

Bears on:

- **R-042** (conformance): the threat-model and release-gate checks.
- **R-041** (SDL/Gate): Release is the one explicit gate.
- **R-044** (crosswalk): BSI's mapping to 62443-4-1, SSDF, NESAS and IT-Grundschutz.
- **R-040** (mitigation kinds): all three kinds are used.
- **R-043** (governed documents): project and user documentation, change tracking.
- **DEC-009**: remedy options and accepted residual risk.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| BSI TR-03185 Anforderungen und Prüfspezifikation v1.0 | Official audit and mapping spreadsheet | BSI publication | https://www.bsi.bund.de/dok/TR-03185 (zip download) |
| BSI certification programme for TR-03185-1 | Certification by BSI-certified IT-Grundschutz auditors | — | same landing page |
| OpenSSF OSPS Baseline | Control catalogue that Part 2 is "induced by" | Community Specification | https://baseline.openssf.org/versions/2025-02-25 |

Searched on 2026-10-02 for open-source tooling that checks TR-03185 conformance; none was found on BSI's pages
or in the search results. The Prüfspezifikation spreadsheet is the only machine-readable artefact.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, cites, distillation block |
| `distilled/README.md` | index and per-artifact coverage |
| `distilled/normative.md` | every requirement verbatim, in source structure, with the framing prose |
| `distilled/requirements.yaml` | 191 typed requirements (library-requirements/v2) with BSI-published `maps_to` |
| `distilled/crosswalk.yaml` | inverse mapping index: target standard id → TR ids |
| `distilled/messages.yaml` | 17 prescribed work-product and communication structures |
| `distilled/schema/` | 7 derived JSON Schemas |
| `distilled/protocol.yaml`, `protocol.md` | 6 process flows with Mermaid sequence diagrams |
| `distilled/state-machine.yaml` | 5 lifecycle machines (issue, release, tool patch, threat model, support) |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass (67 objects, 45 edges, 8 gaps) |
| `distilled/design-notes.md` | adopt / adapt / reject against R-040 to R-044 and DEC-009, and open questions |

## Limits

- **No numbers.** There are no deadlines ("timely" is left to "market conditions"), no severity scheme (CVSS
  appears only as "e.g."), and no maturity levels. Compare with the CRA's 24 h / 72 h / 14-day clock and
  the IEC 62443-4-1 ML1–ML4 scheme.
- **Requirements definition is out of scope** (§1.2.1, §1.3.2 NOTE), yet PROD.PM.A.2 requires the security
  requirements to be identified and documented. The TR assumes they are supplied.
- **Granularity is uneven.** Part 1 cells bundle several MUST/SHOULD sentences under one id. BSI writes that
  the requirements "may therefore exhibit different language styles and levels of detail" (§1.3). Part 2 is
  minimal by design.
- **Source defects** (design-notes Q1 to Q4):
  - there is no PROD.DEV.E.2;
  - Table 3's v1.0 date (2024-09-06) conflicts with the German "06.08.2024";
  - §2.1.1 points to a section 3 that does not exist;
  - the Prüfspezifikation still follows the German v1.0 numbering.
- **Certification lags the current text.** Certification is against the German v1.0. The English v1.1.1 is
  not yet the audited text.
- **Mappings are not equivalences.** Part 2's mappings are explicitly not equivalences, and Part 1's
  "Additional information" mappings are chapter-level only.
