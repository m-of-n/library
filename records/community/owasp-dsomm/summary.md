---
schema: "library-summary/v1"
id: owasp-dsomm
record: owasp-dsomm
type: summary
updated: "2026-10-02"
---

# OWASP DevSecOps Maturity Model (DSOMM) — model data v5.1.0

|  |  |
|---|---|
| **Type** | spec (maturity model published as YAML data + JSON Schemas) |
| **Maturity** | _unset_ — OWASP Lab Project (owasp.org/www-project-devsecops-maturity-model) |
| **Authors** | OWASP DSOMM project; project leaders Timo Pagel, Aryan Prasad |
| **Published** | v5.1.0 GitHub release 2026-09-21 (Latest); the generated model.yaml inside the tag says `version: 5.0.2`, `released: "2026-09-17"` |
| **Identifier** | `github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel-data@v5.1.0` (a2c1b7e6c7cc22de0d478027d76fd8d02c41fd7a) |
| **Source** | https://github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel-data/blob/v5.1.0/generated/model.yaml |
| **Digest** | `319f86d788484f03ac70e39ad1dfb31c09b54a90c38c73abeb6dc945beb68e55` (generated/model.yaml at v5.1.0) |
| **Licence** | GPL-3.0 (repository LICENSE) |

**Version verified 2026-10-02.** `gh release list`: v5.1.0 Latest (2026-09-21),
v5.0.2/5.0.1 (2026-08-21); CHANGELOG: v5.0.0 (2026-08-18) "BREAKING CHANGE: add
agentic AI". The generated model's own `meta.version` (5.0.2) lags the tag —
recorded as found. README: "AI tools were used to assist in drafting and
refining texts in this model ... All AI-assisted content has been reviewed by
maintainers."

**Secondary reference.** Summarized with an object-model pass and the published
cross-references (crosswalk.yaml); not FX-1 extracted.

## Overview

DSOMM grades DevSecOps practice in 251 activities across 6 dimensions (Agentic
AI; Build and Deployment; Culture and Organization; Implementation;
Information Gathering; Test and Verification) and 24 sub-dimensions, each at a
level 1–5 ("Basic understanding" … "Advanced deployment of security practices
at scale"). Each activity states a risk and a measure, often an assessment
("Show …"), difficulty (knowledge/time/resources), usefulness, dependencies,
implementing tools, and references to OWASP SAMM v2, ISO 27001 (2017, 2022),
OpenCRE and (12) D3FEND. Its application tracks implementation and evidence per
team.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | pipeline-level SDL activities, incl. a new agentic-AI dimension |
| Cryptography | none | incidental only |
| This project | adjacent | risk→measure activities with per-team evidence (R-040/R-042) and SAMM/ISO/OpenCRE links (R-044); secondary to SAMM |

Bears on **R-041, R-044** (and R-042 via teamsEvidence).

## Implementations

Searched 2026-10-02.

| Name | Kind | License | URL |
|---|---|---|---|
| DSOMM application | web app (Angular) consuming model.yaml | see repository | https://github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel |
| dsomm.owasp.org | hosted instance | — | https://dsomm.owasp.org |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/README.md` | index |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass |
| `distilled/crosswalk.yaml` | per-activity SAMM / ISO 27001:2022 / OpenCRE references |

## Limits

- Lab project; texts partly AI-assisted (declared).
- SAMM references use `<practice>-<stream>-<level>` (e.g. D-SR-A-2), not SAMM's
  file ids; one is a literal placeholder string and one ('V-RT-AB-1') names two streams.
- No gates or dates; levels describe activities, not an organization state.
