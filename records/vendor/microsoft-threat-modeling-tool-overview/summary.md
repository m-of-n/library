---
schema: "library-summary/v1"
id: microsoft-threat-modeling-tool-overview
record: microsoft-threat-modeling-tool-overview
type: summary
updated: "2026-10-04"
---

# Microsoft Threat Modeling Tool overview

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | established product documentation |
| **Authors** | Microsoft |
| **Published** | 2017-02-16 |
| **Identifier** | https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool |
| **Source** | https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool |
| **Digest** | `c2fbae5eee5b0266f6df2b7378816d7bd8e714d9a2a5adcdf99139d560fdf255` |

## Overview

Microsoft’s overview describes the Threat Modeling Tool as a diagram-first application that analyzes elements and data flows using STRIDE. It presents generated threats with recommended mitigations and supports marking mitigation state during review.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Documents STRIDE analysis and mitigation workflow. |
| Cryptography | none | Does not specify cryptographic mechanisms. |
| This project | adjacent | Evidence for DEC-001, DEC-003, DEC-006, and R-018. |

The source provides an established diagram-and-analysis interaction precedent.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| Microsoft Threat Modeling Tool | desktop application | Microsoft product | https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

The overview does not establish neutral model interchange, broad tracker integration, or current acceptance-tested behavior. It is first-party product documentation.
