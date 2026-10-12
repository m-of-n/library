---
schema: "library-summary/v1"
id: pasta-risk-centric-threat-modeling
record: pasta-risk-centric-threat-modeling
type: summary
updated: "2026-09-29"
---

# Risk Centric Threat Modeling: Process for Attack Simulation and Threat Analysis

|  |  |
|---|---|
| **Type** | book |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Tony UcedaVélez, Marco M. Morana |
| **Published** | John Wiley & Sons, May 2015 |
| **Identifier** | ISBN 978-0-470-50096-5; DOI 10.1002/9781118988374 |
| **Source** | https://onlinelibrary.wiley.com/doi/book/10.1002/9781118988374 |
| **Digest** | `not fetched` (paywalled book) |

## Overview

The full reference for **PASTA**, a seven-stage, risk-centric threat-modeling
method created by UcedaVélez (SEI dates it to 2012). **This book has not been
read for this record** — the summary is based on the publisher's description,
the SEI survey (`sei-threat-modeling-methods-2018`) and the author's own slides
(`ucedavelez-pasta-owasp-2012`). Per those sources, the book presents PASTA as a
way to apply countermeasures in proportion to the business impact of threats,
combining business objectives, application decomposition, threat intelligence,
vulnerability analysis and attack modeling in one process, aimed at developers,
architects, security professionals and managers.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The main reference for a major threat-modeling method. |
| Cryptography | none | Not about cryptography. |
| This project | core | Source for RPT-0002 §3; relevant to risk ("how bad") and to linking threats, weaknesses and attacks. |

Bears on **DEC-001**, **DEC-003** and **DEC-005**.

## Implementations

See `ucedavelez-pasta-owasp-2012` — no open-source PASTA tool found; searched
2026-09-29.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Not read.** Paywalled; this record summarises secondary and author-slide
  sources only. Anything the report needs from the book (exact stage outputs,
  scoring) must be checked in a copy (e.g. through the university library).
- Everything in `ucedavelez-pasta-owasp-2012`'s limits likely applies: heavy
  process, informal risk formula, web-application focus.
