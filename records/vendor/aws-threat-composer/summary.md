---
schema: "library-summary/v1"
id: aws-threat-composer
record: aws-threat-composer
type: summary
updated: "2026-10-04"
---

# AWS Threat Composer

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | open-source implementation |
| **Authors** | Amazon Web Services |
| **Published** | not stated; reviewed 2026-09-26 |
| **Identifier** | git: https://github.com/awslabs/threat-composer |
| **Source** | https://github.com/awslabs/threat-composer |
| **Digest** | `not fetched` |

## Overview

AWS Threat Composer is an Apache-2.0 open-source application for composing structured threat statements. The reviewed repository documents assets or components, assumptions, threats, mitigations, diagrams, import/export surfaces, and AI, CLI, or MCP-assisted workflows.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Directly represents and reviews threat-model content. |
| Cryptography | none | Does not define cryptographic mechanisms. |
| This project | core | Relevant to DEC-001, DEC-002, DEC-003, DEC-006, R-018, and adjacent R-021 workflow evidence. |

Reviewed at commit `3d4ed92f96a29605a74795d8df103e068f11ed70`.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| AWS Threat Composer | open-source application | Apache-2.0 | https://github.com/awslabs/threat-composer |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

The project’s export structures are evidence of portability surfaces, not proof of lossless exchange with other products. AI-assisted capabilities were documented but not independently exercised. No acceptance test was performed.
