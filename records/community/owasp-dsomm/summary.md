---
schema: "library-summary/v1"
id: owasp-dsomm
record: owasp-dsomm
type: summary
updated: "2026-11-16"
---

# OWASP DevSecOps Maturity Model (DSOMM) — model data v5.1.0

|  |  |
|---|---|
| **Type** | spec (maturity model published as YAML data + JSON Schemas) |
| **Maturity** | _unset_ — OWASP Lab Project (owasp.org/www-project-devsecops-maturity-model) |
| **Authors** | OWASP DSOMM project; project leaders Timo Pagel, Aryan Prasad |
| **Published** | v5.1.0 GitHub release 2026-09-21 (Latest); the generated model.yaml inside the tag says `version: 5.0.2`, `released: "2026-09-17"` |
| **Identifier** | `github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel-data@v5.1.0` (a2c1b7e6c7cc22de0d478027d76fd8d02c41fd7a) |
| **Source** | https://raw.githubusercontent.com/devsecopsmaturitymodel/DevSecOps-MaturityModel-data/v5.1.0/generated/model.yaml |
| **Digest** | `319f86d788484f03ac70e39ad1dfb31c09b54a90c38c73abeb6dc945beb68e55` (generated/model.yaml at v5.1.0) |
| **Licence** | GPL-3.0 (repository LICENSE) |

**Version verified 2026-10-02.** `gh release list`: v5.1.0 Latest (2026-09-21),
v5.0.2/5.0.1 (2026-08-21); CHANGELOG: v5.0.0 (2026-08-18) "BREAKING CHANGE: add
agentic AI". The generated model's own `meta.version` (5.0.2) lags the tag —
recorded as found. README: "AI tools were used to assist in drafting and
refining texts in this model ... All AI-assisted content has been reviewed by
maintainers." (Both quotations re-read against the README and CHANGELOG at the
tag on 2026-11-16.)

**FX-1 extraction (library#69, family 4).** The record is extracted against
FX-1 and claims `profile: full`: passes extract and verify are done, the
cross-check is pending, and no artifact is reviewed by a person yet. The source
of record is `generated/model.yaml` alone, read through the FX-1 YAML profile;
coverage figures are in `record.yaml` `distillation.artifacts`. The earlier
secondary-reference pass (object model, crosswalk, its verification) is kept
unchanged beside it.

## Overview

DSOMM grades DevSecOps practice in 251 activities across 6 dimensions (Agentic
AI; Build and Deployment; Culture and Organization; Implementation;
Information Gathering; Test and Verification) and 24 sub-dimensions, each at a
level 1–5. The level names ("Basic understanding" … "Advanced deployment of
security practices at scale") are in the project's `src/assets/YAML/meta.yaml`,
not in model.yaml, which defines no level. Each activity states a risk and a
measure, and carries difficulty (knowledge/time/resources), usefulness,
dependencies (`dependsOn`), implementing tools, and references to OWASP SAMM v2,
ISO 27001 (2017, 2022), OpenCRE and, for 12 activities, D3FEND; 78 activities
add an assessment (evidence to show). The DSOMM application, not this file,
tracks implementation and evidence per team.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | pipeline-level SDL activities, incl. a new agentic-AI dimension |
| Cryptography | none | incidental only |
| This project | adjacent | risk→measure activities with assessment evidence items (tmodel:R-042), dependsOn prerequisites (tmodel:R-041) and SAMM/ISO/OpenCRE links (tmodel:R-044); secondary to SAMM |

Bears on **tmodel:R-041, tmodel:R-042, tmodel:R-044** (`bears_on`). The design
notes also take up tmodel:R-018 (human review of AI-drafted output) and mofn's
supply-chain approvals; see `distilled/design-notes.md`.

## Implementations

Searched 2026-10-02.

| Name | Kind | License | URL |
|---|---|---|---|
| DSOMM application | web app (Angular) consuming model.yaml | see repository | https://github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel |
| dsomm.owasp.org | hosted instance | — | https://dsomm.owasp.org |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; `distillation` holds every artifact's coverage |
| `distilled/README.md` | index |
| `distilled/requirements.yaml` | one entry per activity keyed by its uuid (text: the measure), the sentences and hunted texts within activities, and inferred field-reading rules |
| `distilled/inferred-candidates.yaml` | keyword-less sentences that might bind, each with a verdict |
| `distilled/normative.md` | the normative text per activity, quoted by line marker; source defects SD-1 to SD-16 |
| `distilled/messages.yaml`, `distilled/schema/` | the model's structures and JSON Schemas derived from the file |
| `distilled/protocol.yaml`, `protocol.md` | 14 exchanges that activity texts state, with sequence diagrams; DSOMM defines no wire protocol |
| `distilled/state-machine.yaml` | lifecycles the model and its activities imply, stated vs inferred |
| `distilled/examples/` | the source's 3 fenced code examples verbatim; our schema test cases |
| `distilled/design-notes.md` | adopt / adapt / reject against tmodel and mofn decisions; open questions |
| `distilled/object-model.yaml`, `object-model.md`, `crosswalk.yaml`, `verification.md` | the earlier secondary-reference pass (2026-10-02/03), kept unchanged |

## Limits

- Lab project; texts partly AI-assisted (declared).
- DSOMM states no requirement level: a measure is a recommended practice, adopted level by level.
- The file has defects of its own (`distilled/normative.md`, Source defects): its `meta`
  names 5.0.2, not the tag's 5.1.0; four fields hold a placeholder instead of content; one
  dependency points to a higher level; two activity ids are not UUIDs.
- SAMM references use `<practice>-<stream>-<level>` (e.g. D-SR-A-2), not SAMM's
  file ids; one is a literal placeholder string and one ('V-RT-AB-1') names two streams.
- No published schema binds model.yaml: the project's JSON Schemas describe its
  per-dimension source files, so the schemas here are derived from the data.
- Quoted texts keep YAML's quote marks and backslash escapes as the bytes have
  them (the FX-1 YAML profile).
- No gates or dates; levels describe activities, not an organization state.
