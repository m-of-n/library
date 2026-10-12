---
schema: "library-summary/v1"
id: threat-dragon-tmf-format
record: threat-dragon-tmf-format
type: summary
updated: "2026-10-04"
---

# Threat Dragon Threat Model File format and TM-BOM direction

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | project format note and successor direction |
| **Authors** | OWASP Threat Dragon project |
| **Published** | not stated; retrieved 2026-10-04 |
| **Identifier** | https://github.com/OWASP/threat-dragon/wiki/Threat-Model-File-%28TMF%29-format |
| **Source** | https://github.com/OWASP/threat-dragon/wiki/Threat-Model-File-%28TMF%29-format |
| **Digest** | `da03fb446bee9aed61af4006c5c0c939325917b3edc7eadd8b47209db1f68e8f` |

## Overview

This Threat Dragon project note describes the Threat Model File format as a tool-oriented JSON representation and discusses TM-BOM as its successor direction. It is direct project evidence that the existing format is not presented as a complete neutral interchange solution.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Concerns representation of threat-model content. |
| Cryptography | none | Does not define cryptographic mechanisms. |
| This project | core | Directly relevant to DEC-002 portability. |

The source helps distinguish existing tool-specific persistence from proposed cross-tool interchange.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| Threat Dragon TMF | project-specific format | project documentation | https://github.com/OWASP/threat-dragon/wiki/Threat-Model-File-%28TMF%29-format |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

The note describes a direction, not evidence of completed TM-BOM adoption or verified lossless interchange across products.
