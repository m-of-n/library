---
schema: "library-summary/v1"
id: first-cvss-v4-0
record: first-cvss-v4-0
type: summary
updated: "2026-10-02"
---

# FIRST, Common Vulnerability Scoring System v4.0: Specification Document

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | not set |
| **Authors** | FIRST |
| **Published** | 2023-11-01 (version 1.0); this copy is version 1.2 of 2024-06-18 |
| **Identifier** | CVSS v4.0, document version 1.2 |
| **Source** | https://www.first.org/cvss/v4-0/cvss-v40-specification.pdf |
| **Digest** | `77afde9ea09f8a5c…` (full value in record.yaml) |

## Overview

FIRST's specification of CVSS version 4.0 (40 pages). Its exploitability metrics are attack vector, attack complexity, attack requirements, privileges required and user interaction. Scores come from MacroVector lookup tables with interpolation, and the document defines no exploitability subscore. ISO/SAE 21434's CVSS-based approach, written for v3.1, therefore does not take v4.0 vectors as they stand (tmodel RPT-0007 §3.2).

## Applicability

Bears on DEC-003 and R-011 (risk metric).

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Read only for the exploitability metrics and the scoring method.
