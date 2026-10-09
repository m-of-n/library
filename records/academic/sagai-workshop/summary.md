---
schema: "library-summary/v1"
id: sagai-workshop
record: sagai-workshop
type: summary
updated: "2026-10-01"
---

# SAGAI — IEEE Security and Privacy workshop series on securing generative AI

|  |  |
|---|---|
| **Type** | hierarchy (workshop series) |
| **Maturity** | _unset_ — a venue, not a document |
| **Organizers** | Mihai Christodorescu, John Mitchell, Somesh Jha, Khawaja Shams; Earlence Fernandes from 2025 |
| **Editions** | 2024, 2025, 2026 — co-located with IEEE S&P, San Francisco |
| **Identifier** | sites.google.com/view/sagai2024 · sites.google.com/ucsd.edu/sagai25-ieee-sp · sites.google.com/view/sagai-2026 |
| **Source** | https://sites.google.com/view/sagai2024/home |
| **Digest** | none — web pages |

## Overview

A workshop series at the IEEE Symposium on Security and Privacy on the security of
systems built on generative AI. **SAGAI'24** (*Security Architectures for GenAI Systems*,
May 23 2024) accepted peer-reviewed papers, published in the IEEE SPW 2024 proceedings.
**SAGAI'25** (*Secure Generative AI Agents Workshop*, May 15 2025) ran as invited talks and
panels with no papers; its stated output is a joint research-challenges document.
**SAGAI'26** (*Secure Agents for Generative Artificial Intelligence*, May 21 2026) is listed
by IEEE S&P; its program page was not available (404) on 2026-09-29.

The series' through-line is that GenAI security is a property of the **whole system**, not
only the model: its 2024 topics include input sanitization, prompt-injection defenses,
output validation and secure composition of GenAI components.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Security of GenAI-based systems is the whole subject |
| Cryptography | `none` | Not a topic of the series |
| This project | `adjacent` | Confirmed target of tmodel #13; its papers bear on DEC-001 (AI threat types) |

This record is a **container**: it bears on nothing itself. Members point here with
`part_of`; see `has_part` in `index/crosswalk.md`.

## Implementations

Not applicable to a workshop series; see the member papers.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Membership is partly unconfirmed.** `systems-security-agentic-computing` is probably
  the SAGAI'25 research-challenges document but never names the workshop, so it is linked
  with `see_also`, not `part_of`.
- **SAGAI'26 content is missing** from this library until its program is published.
- **Name clash.** Fraunhofer IESE runs an unrelated "SAGAI" workshop (*Software
  Architecture and Generative AI*, at ICSA); it is out of scope here.
