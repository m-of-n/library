---
schema: "library-summary/v1"
id: bsimm-16
record: bsimm-16
type: summary
updated: "2026-10-02"
---

# BSIMM16 — Building Security In Maturity Model (Report 2026)

|  |  |
|---|---|
| **Type** | spec (descriptive maturity model + annual observational report) |
| **Maturity** | informational — the report describes itself as "a descriptive model" whose "only goal ... is to observe and report" (p.47) |
| **Authors** | not named; Black Duck Software, Inc. (©2026); acknowledgements list ~170 data gatherers (p.33) |
| **Published** | report PDF created 2026-01-27; release announced 2026-02-04 |
| **Identifier** | BSIMM16 |
| **Source** | https://www.blackduck.com/content/dam/black-duck/en-us/reports/bsimm-report.pdf |
| **Digest** | `d34e341f9b5c01d43db0978a53a418b24ff56b2d0cc0371127bde9313fc14dc2` (96 pp.) |
| **Licence** | "THIS WORK IS LICENSED UNDER THE CREATIVE COMMONS Attribution-Share Alike 3.0 License" (p.33) — CC BY-SA **3.0**, not 4.0 |

**Version verified 2026-10-02.** Black Duck press release "Black Duck Releases
BSIMM16 ..." (news.blackduck.com, 2026-02-04) and the BSIMM landing page
(blackduck.com/resources/analyst-reports/bsimm.html) name BSIMM16 as current; no
BSIMM17 found by web search. The PDF was obtained from the direct, un-gated URL
above (no registration). BSIMM16 itself states "For the first time, there have
been no changes to the BSIMM framework this year" (p.50), so the 128 activities
equal BSIMM15's.

## Overview

BSIMM records which software-security activities real organizations perform,
from in-person assessments of 111 firms (BSIMM16 data pool). Its framework has
4 domains, 12 practices and 128 activities; each activity's level (1-3) says how
commonly it is observed, not how advanced it is. Organizations use it to build a
scorecard of their own software security initiative (SSI) and compare it with
the pool. It frames activities as controls and publishes yearly trends (2026:
AI/ML and regulation, SBOM growth driven by US self-attestation).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The largest observational dataset of SDL practice; activity catalogue widely cited (SSDF references BSIMM in 39 of 42 tasks per Figure 3) |
| Cryptography | none | No cryptographic content |
| This project | core | Gate vocabulary for R-041 ([SM1.4]/[SM1.7]/[SM2.6]), crosswalk ids for R-044 (with edition lineage), observation-as-assertion for R-042 |

Bears on **R-041, R-042, R-044**, and R-040 (control kinds).

## Structure

- Governance (SM 13, CP 11, T 12), Intelligence (AM 11, SFD 7, SR 11), SSDL
  Touchpoints (AA 9, CR 11, ST 10), Deployment (PT 7, SE 13, CMVM 13) = 128.
- Level 1/2/3 = 40/41/47 activities. Most observed: CMVM1.1 (106/111), SM1.4 (100/111).
- Part 3 maps SSDF tasks to BSIMM16 labels (Tables 3-4); names six AI/ML key
  activities (SR3.5, AM1.5, AM3.4, SFD3.1, SM3.5, CR1.5); describes SSI states
  emerging / maturing / enabling.

## How it relates to the others

- **NIST SSDF (`sp-800-218`)**: SSDF cites BSIMM12 labels; BSIMM16 Table 3
  translates 22 references (16 tasks) to BSIMM16 labels.
- **OWASP SAMM (`owasp-samm-2`)**: OWASP maps SAMM streams to BSIMM**14**
  activities; BSIMM is descriptive and pool-relative, SAMM a self-assessment ladder.
- **Microsoft SDL (`microsoft-sdl`)**: [SM1.1] names "the NIST SSDF, Microsoft
  SDL, or Black Duck Touchpoints" as methodologies firms tailor.
- **SAFECode (`safecode-fpssd-3`)**: no published mapping.

## Implementations

Searched 2026-10-02. BSIMM assessments are performed by Black Duck (the report's in-person
assessments, p.45); no open-source BSIMM assessment tool found. OWASP SAMM's
mapping spreadsheet provides a free SAMM↔BSIMM14 crosswalk.

| Name | Kind | License | URL |
|---|---|---|---|
| BSIMM assessment | commercial service | proprietary | https://www.blackduck.com/resources/analyst-reports/bsimm.html |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, distillation block |
| `distilled/README.md` | artifact index |
| `distilled/normative.md` | domains, practices, 128 activities verbatim |
| `distilled/requirements.yaml` | 144 entries with observations, lineage, maps_to |
| `distilled/schema/` | derived JSON Schema |
| `distilled/state-machine.yaml` | SSI states; activity lifecycle in the model |
| `distilled/examples/` | scorecards and report tables as data |
| `distilled/design-notes.md` | bearing on R-040…R-044; source defects |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass |

## Limits

- Descriptive only: no requirement, no pass criterion, no evidence standard.
- Organization-level, interview-based; nothing about a product's threats.
- Percentages are inconsistent in places (Table 1 uses 121 as denominator;
  SR2.2 and SE1.4 headings disagree with Figure 18) — use counts.
- Chart data (verticals, longitudinal) is image-only and not extracted.
- Activity labels change across editions; any crosswalk must be edition-qualified.
