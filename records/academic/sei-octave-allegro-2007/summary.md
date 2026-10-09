---
schema: "library-summary/v1"
id: sei-octave-allegro-2007
record: sei-octave-allegro-2007
type: summary
updated: "2026-09-29"
---

# Introducing OCTAVE Allegro: Improving the Information Security Risk Assessment Process

|  |  |
|---|---|
| **Type** | paper (SEI technical report, 154 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Richard A. Caralli, James F. Stevens, Lisa R. Young, William R. Wilson (CERT, SEI) |
| **Published** | May 2007, Software Engineering Institute, Carnegie Mellon University |
| **Identifier** | CMU/SEI-2007-TR-012 |
| **Source** | https://www.sei.cmu.edu/documents/786/2007_005_001_14885.pdf |
| **Digest** | `7fc97ad76b0fc438599eb2732b9cc78d26027ca2004c18fc04439887c58cb946` (retrieved 2026-09-29) |

## Overview

Introduces **OCTAVE Allegro**, the third and most streamlined member of SEI's
OCTAVE family (Operationally Critical Threat, Asset, and Vulnerability
Evaluation) of organisational information-security **risk assessments**. It
recounts the family's history — the OCTAVE framework (1999, developed with the
US DoD for HIPAA compliance), the workshop-based OCTAVE method, OCTAVE-S for
small organisations (2003–2005) — and argues those were too resource-heavy.
Allegro focuses on **information assets** and where they live ("containers":
technical, physical, people), in **eight steps**: establish risk measurement
criteria; develop an information-asset profile; identify containers; identify
areas of concern; identify threat scenarios (using four **threat trees** —
human actors using technical means, human actors using physical access,
technical problems, other problems); identify risks; analyse risks with a
**relative risk score** from impact criteria; select a mitigation approach. It
can be done by a small team or even one person, using the supplied worksheets
and questionnaires.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A widely known organisational security-risk method from SEI/CERT. |
| Cryptography | none | Not about cryptography. |
| This project | adjacent | Organisational and asset-level risk rather than system design; relevant to tmodel's risk scoring (DEC-003) and asset modeling, less to attack paths. |

Bears on **DEC-001** (assets, containers, threat scenarios), **DEC-003**
(impact-based relative risk score) and **DEC-005** (scope).

## Implementations

The method ships as worksheets, questionnaires and guidance in the report's
appendices; no open-source tool found. Searched 2026-09-29.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Organisational, not system design.** It assesses risk to an organisation's
  information assets; it does not analyse a software design or its data flows.
- **No attack paths.** Threat trees classify *sources* of threat (actor, means,
  outcome), not multi-step attacks.
- **Qualitative scoring.** The relative risk score comes from organisation-set
  qualitative criteria; probability is optional because it is hard to quantify.
- **Dated (2007)** and paper-worksheet based.
- **Disagreement with `sei-threat-modeling-methods-2018`:** that survey says
  OCTAVE was "created … in 2003 and refined in 2005"; this report's own timeline
  (Table 1) gives the OCTAVE Framework v1.0 in **September 1999**, with 2003–2005
  being OCTAVE-S.
