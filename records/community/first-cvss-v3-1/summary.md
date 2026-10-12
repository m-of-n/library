---
schema: "library-summary/v1"
id: first-cvss-v3-1
record: first-cvss-v3-1
type: summary
updated: "2026-10-02"
---

# FIRST, Common Vulnerability Scoring System v3.1: Specification Document

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | not set |
| **Authors** | FIRST |
| **Published** | not stated in the document (Revision 1) |
| **Identifier** | CVSS v3.1, Revision 1 |
| **Source** | https://www.first.org/cvss/v3-1/cvss-v31-specification_r1.pdf |
| **Digest** | `6321d986c680205a…` (full value in record.yaml) |

## Overview

FIRST's specification of CVSS version 3.1 (Revision 1, 24 pages). It defines the Base, Temporal and Environmental metric groups and their equations; the Base equations include the exploitability subscore, 8.22 × AttackVector × AttackComplexity × PrivilegesRequired × UserInteraction (section 7.1), with the metric weights in section 7.4. ISO/SAE 21434 cites this version (its Bibliography [24]) and builds its CVSS-based attack feasibility approach on these four metrics (Annex G, G.3 and Table G.8). Added for tmodel RPT-0007 (#11), §3.2.

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

Read only for sections 7.1 and 7.4 and the exploitability metrics. The version-less record `first-cvss` remains as it is.
