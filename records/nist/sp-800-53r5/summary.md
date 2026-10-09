---
schema: "library-summary/v1"
id: sp-800-53r5
record: sp-800-53r5
type: summary
updated: "2026-10-02"
---

# SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations

|  |  |
|---|---|
| **Type** | spec (control catalog) |
| **Maturity** | best-practice (NIST SP; mandatory for US federal systems via FISMA/OMB A-130, voluntary otherwise) |
| **Authors** | Joint Task Force (NIST) |
| **Published** | September 2020; includes updates as of 2020-12-10 (upd1); Release 5.2.0 on 2025-08-27 |
| **Identifier** | SP 800-53 Rev. 5, doi:10.6028/NIST.SP.800-53r5 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf (492 pp) |
| **Digest** | PDF `fc63bcd61715d0181dd8e85998b1e6201ae3515fc6626102101cab1841e11ec6`; OSCAL catalog 5.2.0 `01f37cf90ea99d92242c936cbfbdebcc338eef1f71454e2acac36cc56e9bc062`; 5.2.0 change log PDF `bc4e626745fa4cf48a1bb6d09f552aa4f7a4b945b459119407d08f2e97a89a86` |

## Currency check (2026-10-02)

- CSRC landing page https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final still shows Rev. 5 upd1
  (Sept 2020, updated 2020-12-10) as current. Its planning note (2025-08-27) announces **Release
  5.2.0**, a minor release. It adds SA-15(13), SA-24 and SI-02(07), revises SI-07(12), updates the
  discussion of SA-04, SA-05, SA-08, SA-08(14), SI-02 and SI-02(05), and updates related controls.
  The change log is
  https://csrc.nist.gov/files/projects/Risk-Management/800-53%20Comment%20Site/SP800-53-r5.2.0-changes.pdf.
  It marks SI-02(07) as "Identified as a gap from analysis of the NIST SSDF".
- The landing page links **no consolidated 5.2.0 PDF**. The PDF link is still the upd1 PDF. The
  5.2.0 text is published as OSCAL: usnistgov/oscal-content `main`,
  `nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json`, metadata version **5.2.0**,
  last-modified 2026-05-11. The latest repo release is OSCAL Content v1.5.0 (2026-05-13).
  Baselines come from the LOW, MODERATE, HIGH and PRIVACY baseline profiles, all version 5.2.0.
  None of the three new controls is in any baseline.
- **Defect found:** in OSCAL 5.2.0, SA-15(13) "Logging Syntax" carries SA-15(12)'s statement
  (issues usnistgov/oscal-content#304 and #343). NIST's correction is in PR #345, which was open
  and unmerged on 2026-10-02. We used the PR #345 text and flagged it in `requirements.yaml`.
- No Rev. 6 or public draft was found.

## Overview

SP 800-53 is the US federal catalog of security and privacy controls. It has 20 families, each
control with an imperative statement, organization-defined parameters for tailoring, discussion,
related controls and references. Baselines (now in SP 800-53B) select controls by impact level. For
an SDL, the relevant families are **SA (System and Services Acquisition)** and **SR (Supply Chain
Risk Management)**. SA-3 requires an organization-defined SDLC. SA-4 flows security requirements
into contracts. SA-8 lists 33 security and privacy engineering principles. SA-10 requires developer
configuration management. SA-11 requires developer testing, including SA-11(2) threat modeling and
vulnerability analysis. SA-15 requires a documented development process with tools, metrics and
criticality analysis. SA-17 requires a developer security architecture. SA-24 (new) requires design
for cyber resiliency. Most other SDL frameworks cite these ids. SSDF's References column lists
`SP80053:` controls for nearly every task.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | It is the reference control catalog that every federal SDL and supply-chain framework maps to. |
| Cryptography | adjacent | Not in the in-scope controls. Cryptography is in SC, and SA-4(7)/SR-11 touch validated products. |
| This project | adjacent | The SA/SR ids are join keys for the R-044 crosswalk. SA-11(2) gives a conformance shape for R-042. SA-3/SA-15 inform the R-041 SDL object. SA-15(11) informs R-043 governed views. |

Bears on R-040, R-041, R-042, R-043, R-044 and DEC-009. See `distilled/design-notes.md`.

## Coverage of this record (explicit)

**Partial, `status: summarized`. This is not FX-1.** `distilled/requirements.yaml` holds 107
entries:

- SA-3, SA-4, SA-8, SA-10, SA-11, SA-15, SA-17 and SA-24: the 8 base controls and all of their 86
  enhancements, verbatim. 3 enhancements are withdrawn and kept with their target: SA-4(4) →
  CM-8(9), SA-15(4) → SA-11(2) and SA-15(9) → SA-3(2).
- SI-2(7) Root Cause Analysis, added because 5.2.0 derived it from the SSDF.
- SR-1..SR-12 base statements, verbatim. Their 15 enhancements are listed by id and title only.

**Not covered:** all other families and SA controls, the Discussion and References text of every
control, and SP 800-53A assessment objectives. The text comes from the PDF (104 entries) or from
OSCAL 5.2.0 (3 entries: SA-15(13), SA-24 and SI-2(7), marked `text_source`). Every PDF statement
was compared with OSCAL. They match apart from parameter wording: OSCAL uses short 800-53A ODP
labels, not the PDF's assignment text.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| usnistgov/oscal-content | Machine-readable catalog and baselines (OSCAL) | public domain (NIST) | https://github.com/usnistgov/oscal-content |
| NIST CPRT | Online catalog browser and export | public | https://csrc.nist.gov/projects/cprt |
| compliance-trestle | OSCAL tooling (catalog, profile, SSP) | Apache-2.0 | https://github.com/oscal-compass/compliance-trestle |

Searched on 2026-10-02.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata, coverage statement and relations |
| `distilled/README.md` | Index of the distilled artifacts and their coverage |
| `distilled/requirements.yaml` | 107 in-scope controls and enhancements (library-requirements/v2), with baselines and related controls as `maps_to` |
| `distilled/object-model.yaml` | Object-model pass: 20 objects, 24 edges, 6 gaps |
| `distilled/object-model.md` | Mermaid diagram and reading notes |
| `distilled/design-notes.md` | Inbound SSDF→800-53 map, bearing on R-040..R-044 and DEC-009, and open questions |

## Limits

- 800-53 controls are **organizational and system controls, not developer practices**. The SDL
  content is phrased as acquirer requirements on a developer ("Require the developer ..."), so
  using them as an SDL means inverting the point of view.
- A control cannot be checked until its organization-defined parameters are assigned. Out of the
  box, 800-53 does not say how deep, how often or to what acceptance level.
- No ordering of phases or gates exists. SA-15(1) milestones are the only construct.
- The Release 5.2.0 text exists only as OSCAL and contains at least one known defect (SA-15(13)).
  Pin the commit and re-check it.
- Baselines and assessment procedures live in SP 800-53B and SP 800-53A, which are not ingested.
