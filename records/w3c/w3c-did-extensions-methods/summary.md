---
schema: "library-summary/v1"
id: w3c-did-extensions-methods
record: w3c-did-extensions-methods
type: summary
updated: "2026-11-01"
---

# DID Extensions: Methods registry

|  |  |
|---|---|
| **Type** | spec (W3C Group Note) |
| **Maturity** | `informational`: W3C Group Note, which the Note says is not endorsed by W3C itself |
| **Authors** | Manu Sporny, Markus Sabadello |
| **Published** | 2026-10-01 |
| **Identifier** | W3C NOTE-did-extensions-methods-20261001 |
| **Source** | https://www.w3.org/TR/did-extensions-methods/ |
| **Digest** | `sha256:300cb710…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This W3C Group Note lists known DID methods, with 274 rows in the 2026-10-01 version, each naming a method, its registry and a contact. Its existence answers part of this topic's question. DIDs were designed to avoid central registries, yet method names are short global strings that someone must keep from colliding. So allocation moved from identifiers to method names, and to whoever accepts entries.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | no direct bearing |
| Cryptography | `none` | no direct bearing |
| This project | `core` | direct evidence on who allocates identifiers |

- **R-M-12** (proposed in ARCH-0001-PROPOSAL v0.2.0; extension points are key-relative): the registry shows the global-name pattern re-forming one level up, which is the argument of ARCH-0002 P1.

## Implementations

274 methods are listed; none was evaluated.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** header, status section, the description of the registration process, and a row count of the table (274, from the HTML). The entries themselves were not read, and the process it points to was not followed.

- Whether method names are enforced as unique was not established. A registry is social; the URI scheme does not stop two parties using one name. That reading is ours.
- Listing is not review, so the count says nothing about quality or use.
