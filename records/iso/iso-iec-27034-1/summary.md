---
schema: "library-summary/v1"
id: iso-iec-27034-1
record: iso-iec-27034-1
type: summary
updated: "2026-10-02"
---

# ISO/IEC 27034-1:2011 — Information technology — Security techniques — Application security — Part 1: Overview and concepts

|  |  |
|---|---|
| **Type** | spec (International Standard, ed. 1) |
| **Maturity** | standard. Published 2011-11-21, confirmed at systematic review (ISO stage 90.93). Corrigendum: ISO/IEC 27034-1:2011/Cor 1:2014 (2014-01-08, 2 pp.) |
| **Authors** | ISO/IEC JTC 1/SC 27 (IT Security techniques) |
| **Published** | 2011-11-21 (ISO catalogue); title page says "First edition 2011-11-15"; 67 pp. |
| **Identifier** | ISO/IEC 27034-1:2011 (ISO catalogue id 44378) |
| **Source** | <https://www.iso.org/standard/44378.html> (paywalled) |
| **Digest** | `8e3d0f99777061524aba23818e4ecedf773e7e5202a747cbb734474de23f0768`. This is the free 15-page **preview** (pp. i–xiv, p. 1), not the standard. |

## Overview

ISO/IEC 27034 says application security is demonstrated, not asserted. Each organization keeps an
approved, governed library, the **Organization Normative Framework (ONF)**, which holds
**Application Security Controls (ASCs)** and processes. Each application is assigned a **Targeted
Level of Trust**, which selects the ASCs it must implement. Every ASC pairs a security activity
with a **verification measurement**, and the measurement produces evidence. An application "cannot
be declared secure unless the auditor agrees" that this evidence shows the target was reached
(§0.4.4). The result of that audit is the **Actual Level of Trust** (§3.2). The standard is
deliberately *not* an SDLC (§0.2): an organization maps its existing life cycle (Annex A uses the
Microsoft SDL) onto the 27034 **Application Security Life Cycle Reference Model**. Of all the SDL
standards it is the most object-model-like, because it names its objects and, through TS
27034-5-1, gives the control a machine-readable schema.

## What was read, and how (honest coverage)

- **Paywalled; not pirated.** ISO's Publicly Available Standards site
  (<https://standards.iso.org/ittf/PubliclyAvailableStandards/>) was checked on 2026-10-02. It
  is closed: "The ISO/IEC Information Technology Task Force (ITTF) web site is now closed. The
  deliverables previously available on this site are now available at no charge on the ISO and IEC
  webstores". ISO/IEC 27034-1 is not among the free deliverables: every catalogue listing and
  reseller offers it for purchase only.
- **iso.org was unreachable from this environment.** The ISO Online Browsing Platform and the
  catalogue page both returned HTTP 403 to curl and to the fetch tool, so the OBP preview of
  Clause 3 could not be read. The preview used instead is the free sample distributed
  by iTeh Standards (watermarked "STANDARD PREVIEW"). Its scope is the same as ISO's own preview:
  front matter, Clauses 1–2, and Clause 3 up to 3.2. Watermark overlays drop a few words. They were
  filled from a second distributor preview (normsplash; publisher status not verified, pp. i–x, sha256 `647b27f2…6c906`), and each
  fill is noted in `distilled/normative.md`.
- **Read:** Foreword, Introduction 0.1–0.5, Scope, Normative references, definitions 3.1 *actor*
  and 3.2 *Actual Level of Trust*, and the full ToC with figure and table titles.
- **Not read:** definitions 3.3 onward, Clauses 4–8 (including §8.1.2.6, the ASC concept, and
  Fig. 8, the ASLC Reference Model) and Annexes A–C. No requirement or object from those clauses
  is claimed here.
- **Object model from the series.** Free previews of 27034-2, -3, -5, TS 5-1, -7 and DIS 27034-4,
  plus ISO's free XSD for TS 27034-5-1 (an official electronic insert), supply the ONF, ANF, ASC
  structure, ASLCRM grid and LoT data model. Every locator names its part.

## Series status

Verified 2026-10-02 against ISO's official open-data catalogue
(`iso_deliverables_metadata.jsonl` from isopublicstorageprod.blob.core.windows.net/opendata,
Last-Modified 2026-09-30, sha256 `ba910b39…8177`).

| Part | Edition / date | ISO stage | Notes |
|---|---|---|---|
| 27034-1:2011 Overview and concepts | ed. 1, 2011-11-21, 67 pp. | **90.93** confirmed | + **Cor 1:2014** (2014-01-08, stage 60.60). Secondary source (iso27001security.com): Cor 1 makes "three minor corrections plus a revised figure"; standard confirmed in 2022. |
| 27034-2:2015 Organization normative framework | ed. 1, 2015-07-28, 52 pp. | **90.60** | Under systematic review (close of review). The outcome was not public on 2026-10-02. |
| 27034-3:2018 Application security management process | ed. 1, 2018-05-22, 47 pp. | 90.93 confirmed | The ASMP's 5 steps. |
| 27034-4 Validation and verification | **never published** | NP 27034-4 at **10.98**; DIS 27034-4 at **40.98**; PWI 27034-4 at **00.98** (all cancelled) | A DIS circulated in 2020 (vote 2020-01-07 to 2020-03-31) and was then abandoned. Its preview is used here for audit vocabulary only. |
| 27034-5:2017 Protocols and ASC data structure | ed. 1, 2017-10-09, 33 pp. | 90.93 confirmed | ASC information requirements (M/O) and ASLCRM detail. |
| TS 27034-5-1:2018 XML schemas | ed. 1, 2018-05-07, 77 pp. | **90.60** | Under review. **XSD free** at <https://standards.iso.org/iso-iec/ts/27034/5-1/ed-1/en/ISO27034-ASC_Structure_v1.0.0.xsd> (sha256 `c9068e6d…2093`). |
| 27034-6:2016 Case studies | ed. 1, 2016-10-05, 70 pp. | 90.93 confirmed | Usage examples of ASCs. |
| 27034-7:2018 Assurance prediction framework | ed. 1, 2018-05-22, 29 pp. | 90.93 confirmed | Expected Level of Trust; PASR. |

**Revision:** iso27001security.com (secondary, not ISO) reports a project to revise the 27034 set
that began in 2024, was stopped, and was restarted in 2025 at Preliminary Work Item stage, as a
"major redesign of the scope". ISO's open-data catalogue (snapshot of 2026-09-30) lists an
**ISO/IEC PWI 27034** (id 86925) at stage **00.98**, which means the preliminary work item was
abandoned, and no other active 27034 project. **As of 2026-10-02 the current text of every part is
the edition above, and no successor is in active development in the ISO catalogue.**

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | International standard for application-security governance; the source of the control-with-verification and level-of-trust concepts. |
| Cryptography | none | Cryptography appears only as an example of technological context (§0.4.2). |
| This project | core | It is the closest existing standard to the SDL object model DL-0009 asks for (R-041 Gate exit = Targeted LoT; R-042 conformance = Actual LoT by audit of ASC evidence; R-043 the ONF as a governed, owned, iterated artefact; R-044 ASC `requirements-addressed/source`). Bears on DEC-009 through ONF→ANF, generic→product. |

## How it relates to the other SDL references

- **Microsoft SDL** (`microsoft-sdl-5-2`, `microsoft-sdl`): 27034-1 Annex A maps the SDL onto the
  ONF and the ASLCRM, and its example ASC library is grouped by SDL phase: Training, Requirements,
  Design, Implementation, Verification, Release (ToC A.9). 27034 is the framework and the SDL is one
  instantiation.
- **NIST SP 800-53** (`sp-800-53r5`): Annex B (ToC) renders an SP 800-53 Rev. 3 control (AU-14) in
  ASC format, which positions the ASC as an exchange shape for controls from other catalogues.
- **ISO/IEC 27001/27002/27005**: normative references. 27034 implements, for applications, the
  27001 PDCA approach and 27005 risk management (Annex C maps 27005 onto the ASMP).
- **ISO/IEC 15026-2** (assurance case): the 27034 risk analysis supplies claims, and ASC
  verification measurements supply evidence (§0.5.8).
- **ISO/IEC 15408-3** (`iso-iec-15408`): its assurance components can be implemented as ASCs (§0.5.6).
- **NIST SSDF** (`sp-800-218`), **OWASP SAMM** (`owasp-samm-2`), **IEC 62443-4-1**: these define
  practices and activities. 27034 defines the container (ONF / ASC / LoT) in which such practices
  become verifiable controls. Unlike 62443-4-1 it has no maturity levels; levels of trust are
  per-application assurance targets, not organizational maturity.
- **ISO/IEC 29147 / 30111** (`iso-iec-29147-2018`, `iso-iec-30111-2019`): post-release
  vulnerability handling. 27034 covers it only as operation-stage activities ("MANAGE INCIDENTS",
  "MANAGE PROBLEMS" in the XSD).

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| ISO27034-ASC_Structure_v1.0.0.xsd | official XML Schema (TS 27034-5-1 electronic insert) | ISO Customer Licence (use unmodified) | https://standards.iso.org/iso-iec/ts/27034/5-1/ed-1/en/ISO27034-ASC_Structure_v1.0.0.xsd |

Searched 2026-10-02 for open-source ONF/ASC tooling and ASC libraries: none found that implement
the XSD. Several commercial GRC and AppSec platforms claim to "map to ISO 27034", but none was
verified to exchange `asc:asc-package` documents.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; distillation block with per-artifact coverage |
| `distilled/README.md` | index of the artifacts and their coverage |
| `distilled/normative.md` | verbatim readable text of the 27034-1 preview plus ToC locators for the unread body |
| `distilled/requirements.yaml` | 15 recommendation and prohibition entries from the Introduction, with counts and reconciliation |
| `distilled/object-model.yaml` | object-model pass: 45 objects, 37 edges, 9 gaps |
| `distilled/object-model.md` | Mermaid class diagram and key findings |
| `distilled/state-machine.yaml` | ASC lifecycle (XSD) and application-assurance lifecycle (inferred) |
| `distilled/schema/` | official XSD pointer (URL, sha256, licence, source defects) and a derived outline |
| `distilled/design-notes.md` | adopt / adapt / reject for R-040..R-044, DEC-009; open questions |

## Limits

- The normative body of 27034-1 was not read. The definitions of ASC, ONF, ANF, ASLCRM, level of
  trust and Targeted Level of Trust *in Part 1* are unknown here. The object model uses Parts 2, 3,
  5 and 7 instead, and they may differ in wording.
- 27034 is guidance ("provides guidance", §1). Its "should" sentences are recommendations. The one
  hard rule read (§0.4.4) sits in the informative Introduction.
- No maturity model. Levels of trust are defined per organization in the ONF, and the series gives
  no standard set of levels. That makes cross-organization comparison impossible without an agreed
  ONF.
- The 2011 text predates SBOM, supply-chain provenance and CI/CD-native verification. Supply chain
  appears only as acquisition and outsourcing.
- A redesign was reported (secondary source), but its PWI is abandoned in ISO open data. The texts stand, and names may still change if SC 27 restarts the work.
- The only status check that worked was ISO's open-data catalogue. iso.org pages, including the OBP
  and the life-cycle page, returned 403. The 2022 confirmation date comes from a secondary source.
