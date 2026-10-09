---
schema: "library-summary/v1"
id: owasp-samm-2
record: owasp-samm-2
type: summary
updated: "2026-10-02"
---

# OWASP Software Assurance Maturity Model (SAMM) v2.2.0

|  |  |
|---|---|
| **Type** | spec (maturity model published as structured YAML data) |
| **Maturity** | _unset_ — an OWASP Flagship project's community model; not a ratified standard, and we did not find a standing we could cite |
| **Authors** | OWASP SAMM project; project leaders Seba Deleersnyder and Bart De Win (owasp.org/www-project-samm); SAMM "was created by Pravir Chandra" (toolbox spreadsheet, Attribution sheet) |
| **Published** | v2.2.0 release, tag commit 2026-07-01, published 2026-07-06 (GitHub release, marked Latest) |
| **Identifier** | `github.com/owaspsamm/core@v2.2.0` (commit 21352e0fc79a6764abcd83a008690e32d2d5a3fe) |
| **Source** | https://github.com/owaspsamm/core/releases/download/v2.2.0/samm.tar.gz |
| **Digest** | `ec8dce3a5d8ed972b595e306287336f1318d4ea318477e723921b41bf9223b05` (samm.tar.gz) |
| **Licence** | CC BY-SA 4.0 (`license.txt`) |

**Version verified 2026-10-02.** `gh release list -R owaspsamm/core`: v2.2.0
(2026-07-06, Latest), v2.1.0 (2024-09-18), v2.0.x pre-releases.
https://owasp.org/www-project-samm/ states 2.2.0. The release tarball's `model/`
differs from the tag only in four trailing-whitespace lines. v2.1.0 → v2.2.0
touched 115 model files (+187/−186 lines) — wording/terminology alignment
(PRs #190 "grammar-style", #191 "align terminology"); the structure (5 / 15 /
30 / 90) is unchanged. Also fetched: the release toolbox `SAMM_spreadsheet.xlsx`
(sha256 `87d95c85…e409`) for the scoring formulas, and OWASP's two mapping
spreadsheets linked from https://owaspsamm.org/docs/reference/mappings/ (xlsx
exports, sha256 `7ff751a4…4976` and `44f7f1d3…dfc9`).

## Overview

SAMM is a prescriptive-by-measurement maturity model: an organization rates
itself, by interview, against 90 activities arranged as 5 business functions ×
3 security practices × 2 streams × 3 maturity levels, then plans a roadmap to
raise chosen practices. Each activity has exactly one assessment question,
answered on a four-point coverage scale (0, 0.25, 0.5, 1), and the answer is
credited only if the question's quality criteria hold. Unlike every other SDL
source in this topic, the model is published as typed, GUID-linked YAML, so it
can be loaded as data. It is phase-agnostic: Governance spans the lifecycle, and
the other four functions roughly follow design → implementation → verification
→ operations.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The open maturity model for software assurance; D-TA-B (threat modeling) is a first-class stream |
| Cryptography | none | No cryptographic content beyond secret management (I-SD-B) and data protection (O-OM-A) |
| This project | core | Typed data model + OWASP's own typed crosswalk to SSDF/BSIMM/62443/CSF/MS SDL: the reference case for the R-044 Requirement/`maps_to` model and an input to R-041 (roadmap → milestones) and R-042 (quality criteria → conformance checks) |

Bears on **R-041, R-042, R-044** (and R-040/DEC-009 via process-kind
mitigations — `distilled/design-notes.md`).

## Structure

- 5 business functions: Governance, Design, Implementation, Verification, Operations.
- 15 practices: G-SM, G-PC, G-EG; D-TA, D-SR, D-SA; I-SB, I-SD, I-DM; V-AA, V-RT, V-ST; O-IM, O-EM, O-OM.
- 30 streams (A/B per practice), 45 practice-level objectives, 90 activities,
  90 questions, 295 quality criteria, 24 answer sets.
- Scoring (toolbox): practice score = Σ over levels of the mean of the two
  streams' answer values; function = mean of 3 practices; overall = mean of 5
  functions. Levels are **summed, not gated**.

## How it relates to the others

- **NIST SSDF (`sp-800-218`)**: OWASP and NIST built an OLIR mapping; 77 stream
  rows and 81 activity rows with OLIR relationship types (`crosswalk.yaml`).
- **BSIMM (`bsimm-16`)**: SAMM publishes a BSIMM**14** activity mapping (125
  pairs). BSIMM is descriptive (what firms are observed doing); SAMM is a
  self-assessment against a fixed ladder.
- **Microsoft SDL (`microsoft-sdl`)**: 47 pairs to the current practice-set
  sub-practice ids (1.1 … 10.x) with OLIR-style relationship types.
- **IEC 62443-4-1**: 60 pairs to SM/SR/SD/SI/SVV/DM/SUM/SG requirement ids.
- **OWASP DSOMM (`owasp-dsomm`)**: DSOMM activities reference SAMM streams.
- **SAFECode (`safecode-fpssd-3`)**: no published mapping.

## Implementations

Searched 2026-10-02.

| Name | Kind | License | URL |
|---|---|---|---|
| SAMM Toolbox spreadsheet (release asset) | assessment tool | CC BY-SA 4.0 | https://github.com/owaspsamm/core/releases/tag/v2.2.0 |
| SAMMwise | open-source assessment web app | Apache-2.0 (per repo) | https://github.com/owaspsamm/sammwise |
| SAMM website model pages (generated from this repo) | reference | CC BY-SA 4.0 | https://owaspsamm.org/model/ |
| Codific SAMMY | commercial SAMM management tool | proprietary | https://sammy.codific.com/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, distillation block |
| `distilled/README.md` | artifact index with coverage |
| `distilled/normative.md` | the whole model verbatim, with ids and file locators |
| `distilled/requirements.yaml` | 415 entries (streams, activities, quality criteria), `maps_to` from OWASP's mappings |
| `distilled/crosswalk.yaml` | every published SAMM mapping row, verbatim ids and relationship types |
| `distilled/schema/samm-core-model.derived.schema.json` | derived JSON Schema for the 8 file types |
| `distilled/state-machine.yaml` | maturity levels + toolbox scoring formulas |
| `distilled/examples/` | scoring fixtures, checker, answer sets |
| `distilled/design-notes.md` | bearing on R-040…R-044, DEC-009 |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass |

## Limits

- SAMM names **no work products or evidence**: `results` and `metrics` are
  placeholders ("result1", "result2") in 18 activities and empty in the rest.
  An assessment is an interview with free-text notes.
- The scoring rule lives only in the toolbox spreadsheet, not in the model data;
  the model alone does not say how answers become a level.
- Organization/portfolio scope: nothing in SAMM is about a specific product's
  threats or mitigations.
- OWASP's mappings carry its own caveat ("our interpretation… provided as-is");
  three TMC rows cite non-existent ids (`P-SM-1-B`, `P-SM-2-B`, `D-TM-3-B`), and the BSIMM
  mapping is to BSIMM14, two editions behind BSIMM16.
- `relatedActivities` mixes "related" and "prerequisite" semantics: the field's
  template comment reads "prerequisites to implement this one" in 54 activity
  files, "related to this one" in 18 and "may be related to this one" in 18; of
  the 18 activities that populate it, 13 carry the "prerequisites" comment.
