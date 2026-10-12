---
schema: "library-summary/v1"
id: owasp-pytm
record: owasp-pytm
type: summary
updated: "2026-10-04"
---

# OWASP pytm

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | established OWASP implementation |
| **Authors** | OWASP pytm project |
| **Published** | not stated; reviewed 2026-09-26 |
| **Identifier** | git: https://github.com/OWASP/pytm |
| **Source** | https://github.com/OWASP/pytm |
| **Digest** | `not fetched` |

## Overview

OWASP pytm is a GPL-3.0 Python library and command-line approach for defining a threat model as code. The reviewed repository documents Python model objects, rule-based threat generation, and generated data-flow diagrams, sequence diagrams, and reports.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Implements threat generation from a structured system model. |
| Cryptography | none | Does not define a cryptographic protocol. |
| This project | adjacent | Useful model-as-code evidence for DEC-001, DEC-003, and DEC-006. |

Reviewed at commit `78895796f6c6f6ec3131c28b624c296810fa9797`.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| OWASP pytm | open-source library/CLI | GPL-3.0 | https://github.com/OWASP/pytm |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

Python source is the native model representation. The reviewed source does not establish a neutral interchange round trip, built-in issue-tracker integration, or a native collaborative review lifecycle. No acceptance test was performed.
