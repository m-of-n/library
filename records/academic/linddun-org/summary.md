---
schema: "library-summary/v1"
id: linddun-org
record: linddun-org
type: summary
updated: "2026-09-29"
---

# LINDDUN privacy threat modeling framework (linddun.org)

|  |  |
|---|---|
| **Type** | web (official framework site) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | DistriNet Research Unit, KU Leuven |
| **Published** | living website; read 2026-09-29 |
| **Identifier** | https://linddun.org/ |
| **Source** | https://linddun.org/ (threat types: /threat-types/, methods: /methods/) |
| **Digest** | `not fetched` (living web page) |

## Overview

The maintained home of LINDDUN, the privacy threat-modeling framework introduced
in `deng-linddun-2011`. The current seven threat types are **Linking**,
**Identifying**, **Non-repudiation**, **Detecting**, **Data disclosure**,
**Unawareness & unintervenability** and **Non-compliance**. It offers three
methods of increasing rigour: **LINDDUN GO**, a card deck for lean team
brainstorming from informal sketches; **LINDDUN PRO**, a systematic analysis of
interactions between DFD elements using threat trees and mapping tables (and
described as STRIDE-compatible and tool-supportable); and **LINDDUN MAESTRO**, a
model-driven variant using enriched system descriptions, still marked "more info
coming soon".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Current reference for privacy threat modeling. |
| Cryptography | none | Not about cryptography. |
| This project | core | Current names and variants for RPT-0002 §5. |

Bears on **DEC-001** and **DEC-005**.

## Implementations

LINDDUN GO card deck (printable and physical); OWASP Threat Dragon supports
LINDDUN threats. Searched 2026-09-29.

| Name | Kind | License | URL |
|---|---|---|---|
| LINDDUN GO cards | card deck | none stated on the site | https://linddun.org/methods/ |
| OWASP Threat Dragon | open-source tool | Apache-2.0 | https://github.com/OWASP/threat-dragon |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Living site.** Content can change without versioning; no digest recorded.
- **No license stated** for the LINDDUN materials on the pages read.
- **LINDDUN MAESTRO is not documented yet** ("more info coming soon"). It is
  unrelated to the Cloud Security Alliance's *MAESTRO* framework for agentic-AI
  threat modeling, which shares the name.
