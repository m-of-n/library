---
schema: "library-summary/v1"
id: threagile
record: threagile
type: summary
updated: "2026-10-04"
---

# Threagile

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | maintained open-source implementation |
| **Authors** | Threagile project |
| **Published** | not stated; reviewed 2026-09-26 |
| **Identifier** | git: https://github.com/Threagile/threagile |
| **Source** | https://github.com/Threagile/threagile |
| **Digest** | `not fetched` |

## Overview

Threagile is an MIT-licensed threat-modeling toolkit centered on a YAML architecture model. The reviewed repository documents built-in and custom risk rules, explicit risk tracking, generated diagrams and risk reports, JSON/PDF/XLSX output, container execution, and a REST server mode.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Implements structured architecture and risk analysis. |
| Cryptography | none | Cryptographic design is not the source’s focus. |
| This project | core | Evidence for DEC-001, DEC-002, DEC-003, DEC-006, and R-021. |

Reviewed at commit `74e323ed635f026ca85bd61b5082f0da053ba1b2`.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| Threagile | open-source CLI/container/server | MIT | https://github.com/Threagile/threagile |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

Structured YAML and generated JSON improve inspectability but do not by themselves establish lossless neutral interchange. The source documents a limited UI and does not establish a full human approval workflow. No acceptance test was performed.
