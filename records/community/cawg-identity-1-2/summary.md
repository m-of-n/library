---
schema: "library-summary/v1"
id: cawg-identity-1-2
record: cawg-identity-1-2
type: summary
updated: "2026-11-01"
---

# CAWG Identity Assertion 1.2

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard`: DIF Ratified Specification |
| **Authors** | not extracted; Creator Assertions Working Group |
| **Published** | 2025-12-15 |
| **Identifier** | version 1.2 |
| **Source** | https://cawg.io/identity/1.2/ |
| **Digest** | `sha256:f29572c1…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

C2PA's claim signature identifies the tool that generated the claim, not the person or organisation responsible. The `cawg.identity` assertion adds a second, independent signature by a credential holder over a `signer_payload`, which hash-links chosen assertions, so a named actor can bind themselves to specific statements (§1.2, §5.1). Optional fields guard against unwanted association with other assertions or a claim generator (§5.1). Credentials are either identity claims aggregation or X.509 with COSE, and 1.2's stated change from 1.1 is an added trust model for X.509 (§8.2.4). §5.1.2 defines seven recommended role values, such as `cawg.creator`, and §5.3 allows entity-specific ones.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Separates the tool's signature from the actor's, with a stated trust model and threats (§9) |
| Cryptography | `adjacent` | Per-assertion holder signatures, over COSE or via credentials (§8) |
| This project | `adjacent` | A nearby design for binding a principal to statements, though with identity not key-relative names |

- **DEC-007**: §5.1.2 asks any UX to be prepared to describe roles in the surrounding language, and gives a one-line English meaning for each value in a table. That is a small vocabulary with renderings, specified in prose. The client ships the words, and §5.3 concedes that external labels may not be widely understood. **DEC-007** is proposed, not accepted: it exists only in ARCH-0001-PROPOSAL v0.2.0 §5, and mofn's DECISIONS-0001 item 5d asks whether it survives at all.
- **R-M-12** (proposed text; relocated to ARCH-0002 P1 and accepted by ADR-0001): §5.3 uses the same DNS-based labels as C2PA, so the same gap applies. The identity assertion itself is closer to the idea of a principal standing behind specific statements.

## Implementations

No search was run for this record. Whether the contentauth SDKs implement this version was not established.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **1.3 is current.** This is the previous ratified version. Differences from 1.3 were not examined.
- **Built against C2PA 2.2** (§1.1), not `c2pa-2-4`. The 2.4 text does not mention CAWG in a full-text search, so the relation is one-way at spec level, while `c2pa-ux-2-2` does name CAWG.
- **No UX in this version.** §10 says guidance is forthcoming. Whether it now exists was not checked.
- **Other CAWG specs not held.** The Metadata Assertion specification listed on the site is where vocabulary work would sit.
- **Read scope.** By section: header, §1.1, part of §1.2, §3.3.12 and §3.3.13, §5.1, §5.1.2, §5.3, the start of §9.1, and §10, plus the section headings. §1.3, §6, §7, §8 and most of §9 were not read, so nothing here covers validation or the threat analysis.
