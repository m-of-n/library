---
schema: "library-summary/v1"
id: owasp-threat-model-library
record: owasp-threat-model-library
type: summary
updated: "2026-10-04"
---

# OWASP Threat Model Library and TM-BOM

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | emerging specification project |
| **Authors** | OWASP Threat Model Library project |
| **Published** | not stated; reviewed 2026-09-26 |
| **Identifier** | git: https://github.com/OWASP/www-project-threat-model-library |
| **Source** | https://github.com/OWASP/www-project-threat-model-library |
| **Digest** | `not fetched` |

## Overview

The OWASP Threat Model Library project hosts work toward a reusable threat-model library and the TM-BOM JSON interchange direction. RPT-0003 uses it as evidence of an emerging attempt to move threat models between tools without treating an individual tool’s internal file as the neutral standard.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Concerns reusable threat-model content. |
| Cryptography | none | Does not define cryptographic mechanisms. |
| This project | core | Directly relevant to DEC-002 interchange. |

Reviewed at commit `68640e1447294232f7ab24ceb9527979587f1849`.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| OWASP Threat Model Library / TM-BOM | open-source specification project | unclear from reviewed evidence | https://github.com/OWASP/www-project-threat-model-library |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

TM-BOM is an emerging direction rather than evidence of broad adoption or complete cross-tool round trips. The repository license was not established from the reviewed evidence and is therefore recorded as unclear rather than inferred.
