---
schema: "library-summary/v1"
id: zoom-keybase-2020
record: zoom-keybase-2020
type: summary
updated: "2026-11-01"
---

# Zoom Acquires Keybase and Announces Goal of Developing the Most Broadly Used Enterprise End-to-End Encryption Offering

|  |  |
|---|---|
| **Type** | web (company blog post) |
| **Maturity** | `informational`: a corporate announcement |
| **Authors** | Eric S. Yuan |
| **Published** | 7 May 2020, editor's note 19 June 2020 |
| **Identifier** | https://blog.zoom.us/ (see Source) |
| **Source** | https://blog.zoom.us/zoom-acquires-keybase-and-announces-goal-of-developing-the-most-broadly-used-enterprise-end-to-end-encryption-offering/ |
| **Digest** | `sha256:e13f1dec…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Zoom announces it has acquired Keybase, describing the deal as a step in a 90-day plan to strengthen its security and calling the team's encryption skills the reason. The rest is about Zoom's own plan: an end-to-end encrypted meeting mode in which logged-in users hold public cryptographic identities, stored on Zoom's network. A draft cryptographic design is promised for 22 May. The post is about Zoom, not about Keybase.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | Corporate news; no technical argument about Keybase |
| Cryptography | `adjacent` | Outlines a host-generated meeting key design, as a plan |
| This project | `none` | Serves one date in a citation |

It bears on no open `DEC-*` or `R-*`. It is cited by mofn R-001 §5.6 for the May 2020 date.

## Implementations

None applicable: an announcement. Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, and a `web` record is outside FX-1 scope.

## Limits

Read whole, live page. It does not mention Keybase's identity proofs, the Keybase service's future, or any failure of the model. So it cannot support mofn R-001 §5.6's "ceased to be an independent identity layer", or any claim that Keybase failed to be adopted. Those need other sources. It is a forward-looking company statement with an explicit disclaimer. Whether the plan shipped is out of scope.
