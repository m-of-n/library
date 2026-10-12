---
schema: "library-summary/v1"
id: open-threat-model
record: open-threat-model
type: summary
updated: "2026-10-04"
---

# Open Threat Model specification and JSON Schema

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | specification repository |
| **Authors** | IriusRisk |
| **Published** | not stated; reviewed 2026-09-26 |
| **Identifier** | git: https://github.com/iriusrisk/OpenThreatModel |
| **Source** | https://github.com/iriusrisk/OpenThreatModel |
| **Digest** | `not fetched` |

## Overview

Open Threat Model (OTM) defines a JSON representation for exchanging threat models. The reviewed repository includes `otm_schema.json`, which describes project, component, data-flow, threat, mitigation, and related model fields. The repository documentation is licensed CC-BY-SA-4.0, while the schema file separately declares Apache-2.0.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Defines security-model objects and relationships. |
| Cryptography | none | Does not define cryptographic mechanisms. |
| This project | core | Direct evidence for DEC-001 object modeling and DEC-002 interchange. |

Bears on DEC-001 and DEC-002. Reviewed at commit `c88c5a7b4115f0f025e28d5682a2b0d790b389e4`.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| IriusRisk CLI | open-source implementation/tooling | See repository | https://github.com/iriusrisk/iriusrisk-cli |
| IriusRisk | commercial implementation | commercial | https://www.iriusrisk.com/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

The source defines a format; it does not establish broad adoption, lossless round trips between products, or compatibility with every vendor extension. The CLI was recorded as an implementation of OTM rather than as a separate specification record.
