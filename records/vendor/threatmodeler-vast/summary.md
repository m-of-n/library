---
schema: "library-summary/v1"
id: threatmodeler-vast
record: threatmodeler-vast
type: summary
updated: "2026-09-29"
---

# VAST (Visual, Agile, and Simple Threat) modeling — ThreatModeler

|  |  |
|---|---|
| **Type** | web (vendor product page) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | ThreatModeler Software, Inc. (method attributed by SEI to Anurag Agarwal) |
| **Published** | living web page; read 2026-09-29 (formerly threatmodeler.com/innovation-lab/vast) |
| **Identifier** | https://www.threatmodeler.ai/innovation-lab/vast |
| **Source** | same |
| **Digest** | `not fetched` (living web page) |

## Overview

ThreatModeler's own description of **VAST**, the threat-modeling method behind
its commercial platform. The page presents VAST as built for enterprise scale
around four characteristics — **scalable**, **automated**, **integrated** (with
Agile/DevOps tooling) and **collaborative** — and describes it as "a core element
of the ThreatModeler platform". It does not describe the method's steps, model
types, diagrams or how threats are identified; those details come from secondary
sources (e.g. `sei-threat-modeling-methods-2018`: separate *application* threat
models using process-flow diagrams and *operational* threat models using
data-flow diagrams).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A named threat-modeling method used in a commercial product. |
| Cryptography | none | Not about cryptography. |
| This project | adjacent | A method defined mainly through a vendor tool; relevant to scaling and UI (DEC-006), little public substance for the object model. |

Bears on **DEC-005** (scope) and **DEC-006** (UI and interaction model).

## Implementations

ThreatModeler (commercial) — compared in tmodel RPT-0003 (#7). No open-source
VAST implementation found; searched 2026-09-29.

| Name | Kind | License | URL |
|---|---|---|---|
| ThreatModeler | commercial platform | commercial | https://www.threatmodeler.ai/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Marketing, not a specification.** No steps, notation, inputs or outputs;
  the method cannot be applied from this page alone.
- **Vendor-tied.** VAST is defined through, and promoted with, one commercial
  product; SEI also notes it has little publicly available documentation.
- **Unverifiable claims.** Statements such as reducing threat evaluation "from
  hours to minutes" come without evidence.
- **Living page.** It has already moved domain (threatmodeler.com → .ai); no digest.
