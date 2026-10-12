---
schema: "library-summary/v1"
id: microsoft-threat-modeling-tool-features
record: microsoft-threat-modeling-tool-features
type: summary
updated: "2026-10-04"
---

# Microsoft Threat Modeling Tool feature overview

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | established product documentation |
| **Authors** | Microsoft |
| **Published** | 2017-08-17 |
| **Identifier** | https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-feature-overview |
| **Source** | https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-feature-overview |
| **Digest** | `97daad1c18910d3a8a951ab4a334fc0ce572dc60bc06f6cd8bb66f811789bfc3` |

## Overview

Microsoft’s feature overview separates threat modeling into design and analysis views. It documents templates, generated threats, threat properties and status, mitigation information, and report generation as parts of the review workflow.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Documents threat review and mitigation-state features. |
| Cryptography | none | Does not specify cryptographic mechanisms. |
| This project | adjacent | Evidence for DEC-001, DEC-003, DEC-006, and R-018. |

The design/analysis separation is useful interaction-model evidence for later product design review.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| Microsoft Threat Modeling Tool | desktop application | Microsoft product | https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-feature-overview |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

The page documents features but does not independently test usability, model portability, or lifecycle integration. Product behavior may vary by tool version.
