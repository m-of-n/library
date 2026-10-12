---
schema: "library-summary/v1"
id: iso-sae-21434-2021
record: iso-sae-21434-2021
type: summary
updated: "2026-10-03"
---

# Road vehicles — Cybersecurity engineering (ISO/SAE 21434:2021)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | standard (ratified ISO/SAE, first edition 2021-08) |
| **Authors** | ISO/TC 22/SC 32 · SAE |
| **Published** | 2021-08 |
| **Identifier** | ISO/SAE 21434:2021 |
| **Source** | https://www.iso.org/standard/70918.html (purchased; bytes held locally, never committed) |
| **Digest** | `73f990078d3a5b47dec91dd0d2b4e6c24cecd9e4160ae5b143c3b3fa80b7cdf4` |

## Overview

ISO/SAE 21434 is the reference standard for **cybersecurity engineering of road-vehicle
electrical/electronic systems** across the whole lifecycle (concept → development →
production → operations → maintenance → decommissioning). It cancels and supersedes
SAE J3061:2016. Its core method is **TARA — Threat Analysis and Risk Assessment**
(Clause 15): identify damage scenarios and assets, derive threat scenarios, rate
impact in four categories (Safety, Financial, Operational, Privacy), analyse attack
paths, rate **attack feasibility** (Table 1), determine a **risk value**, and decide a
risk treatment. It also defines a normative **object model** (Figure 3: item, function,
component, asset, cybersecurity goal/requirement, threat scenario, damage scenario) and
structures every obligation as a tagged **requirement** (`[RQ-CC-NN]` shall / `[RC-]`
should / `[PM-]` may) that produces auditable **work products** (`[WP-CC-NN]`).

## Why it matters here

Two things make this the core doc to iterate on:
1. **A ready object model + risk pipeline** we can adopt/adapt for tmodel (feeds ARCH-0001,
   the schema #17, and the metrics work #14).
2. **Its requirement/work-product structure is the template for automating conformance
   audits** — a work product is the unit of evidence, so an audit becomes a coverage +
   traceability query over the knowledge graph, with a human judging adequacy (tmodel #15).

## Requirements

**118 requirements** (101 shall / 13 should / 4 may) and **42 work products**, extracted with full text, clause locators, cross-references, and produced work products.

- Full structured catalog: [`distilled/requirements.yaml`](distilled/requirements.yaml) (cite as `iso-sae-21434-2021#RQ-CC-NN`)
- Viewable list (designator + short title, per clause): [`distilled/requirements.md`](distilled/requirements.md)

| clause | area | requirements | work products |
|---|---|---|---|
| 5 | Organizational mgmt | 17 | 5 |
| 6 | Project-dependent mgmt | 34 | 4 |
| 7 | Distributed activities | 8 | 1 |
| 8 | Continual activities | 8 | 6 |
| 9 | Concept | 11 | 7 |
| 10 | Product development | 13 | 7 |
| 11 | Validation | 2 | 1 |
| 12 | Production | 3 | 1 |
| 13 | Operations & maintenance | 3 | 1 |
| 14 | End of support | 2 | 1 |
| 15 | TARA methods | 17 | 8 |
| **all** | | **118** | **42** |

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The normative method for automotive threat modeling & risk |
| Cryptography | adjacent | Uses crypto controls; does not specify primitives |
| This project | core | Object model, TARA pipeline, and audit template all map directly |

Bears on `DEC-003` (risk metric), `DEC-005` (MVP scope), `DEC-009` (product/mitigation
mapping), `R-011`, `R-012` (ISO 21434 support), `R-021` (mitigation lifecycle).

## Implementations

Tooling exists (e.g. IriusRisk, medini analyze, itemis SECURE, Ansys medini) but not yet
surveyed as build-on-it options — see the products survey (tmodel #7). searched: 2026-09-25.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/requirements.yaml` | 118 requirements + 42 work products, full text/refs, `#RQ-CC-NN` referenceable |
| `distilled/requirements.md` | viewable per-clause table: designator + short title |
| `distilled/normative.md` | TARA pipeline, object model (Fig 3), Table 1 feasibility, terminology, audit mapping |
| `distilled/README.md` | index of distilled artifacts + coverage |

## Limits

- Distilled from the document body; **Annexes not distilled** — impact criteria (Annex F),
  attack-feasibility methods (attack-potential / CVSS / attack-vector, Annexes G/H), and the
  worked example are referenced but not extracted.
- Requirement statements are **verbatim** and **not yet reviewed line by line** (`reviewed_by`
  empty). A check against the source (tmodel RPT-0007 §7, 2026-10-02) found 16 of the 118 texts
  wrong: 5 hold annex text instead of the provision (RQ-07-04, RQ-09-03, RQ-09-04, RQ-10-08,
  RQ-11-01), and 11 lose the list items that follow an interrupting NOTE or EXAMPLE (RQ-05-11,
  RQ-06-02, RQ-06-15, RQ-06-16, RQ-06-30, RQ-09-01, RQ-10-01, RQ-10-04, RQ-12-02, RQ-13-01,
  RQ-15-17). Their text is left as it is until the sponsor decides whether this public
  repository may hold the standard's verbatim text; read the standard for those entries. A
  human pass is still required before any requirement is treated as authoritative.
- Work-product links (22 were missing), locators (5 provision, 14 work product) and three
  work-product titles were corrected against the source on 2026-10-02 (RPT-0007 §7). The
  derived `nature` and `verification` fields follow the links: 47 provisions are now
  deliverable-producing. The 10 work products that the standard ties to subclauses rather than
  provisions list those subclauses in `from_subclauses` (2026-10-03).
- 21434 defines a *method*, not machine-readable schemas; the object model is ours to encode.
