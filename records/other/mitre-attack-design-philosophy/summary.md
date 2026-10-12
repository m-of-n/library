---
schema: "library-summary/v1"
id: mitre-attack-design-philosophy
record: mitre-attack-design-philosophy
type: summary
updated: "2026-09-29"
---

# MITRE ATT&CK: Design and Philosophy

|  |  |
|---|---|
| **Type** | paper (MITRE product MP180360R1, 46 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Blake E. Strom, Andy Applebaum, Doug P. Miller, Kathryn C. Nickels, Adam G. Pennington, Cody B. Thomas |
| **Published** | July 2018, revised March 2020, The MITRE Corporation |
| **Identifier** | MP180360R1 |
| **Source** | https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf |
| **Digest** | `15eced1bbf6d3ba9aa57e4a6e6efa14620e9398d096471d64fd95df8a01d18bd` (retrieved 2026-09-29) |

## Overview

MITRE's own explanation of what ATT&CK is and how it is built. ATT&CK is a
knowledge base of adversary behaviour drawn from real-world observation, organised
as **tactics** (the adversary's "why" — a tactical objective such as persistence
or exfiltration), **techniques** and **sub-techniques** (the "how"), and
**procedures** (a specific group's implementation), linked to groups, software and
mitigations, across Enterprise, Mobile and ICS domains. Its core argument
(§4.1.3) is about **abstraction**: high-level models such as the Lockheed Martin
Kill Chain and Microsoft STRIDE explain adversary goals but not the individual
actions or how one action relates to another, while exploit and malware
databases are too specific; ATT&CK is the **mid-level** model that ties them
together and can be mapped to defences. Stated use cases are adversary
emulation, red teaming, behavioural-analytics development, defensive gap
assessment, SOC maturity assessment and threat-intelligence enrichment.
Tactics are treated as **tags** — a technique can belong to more than one tactic.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The design rationale for the most widely used adversary-behaviour catalog. |
| Cryptography | none | Not about cryptography. |
| This project | core | Defines the vocabulary tmodel would use for attack steps; explains how ATT&CK relates to STRIDE and the Kill Chain (RPT-0002 §9). |

Bears on **DEC-001** (object model — attack steps as techniques) and **DEC-005**
(MVP scope). The dataset itself is `mitre-attack`.

## Implementations

- **ATT&CK data** — STIX 2.1 JSON, see `mitre-attack`.
- **ATT&CK Navigator** — MITRE's web tool for annotating the matrix.
- **Attack Flow** — MITRE Center for Threat-Informed Defense format for
  *sequences* of ATT&CK techniques.

Searched 2026-09-29.

| Name | Kind | License | URL |
|---|---|---|---|
| ATT&CK Navigator | open-source web tool | Apache-2.0 | https://github.com/mitre-attack/attack-navigator |
| Attack Flow | open-source format + tools | Apache-2.0 | https://github.com/center-for-threat-informed-defense/attack-flow |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Not a threat-modeling method on its own.** It catalogs *observed* adversary
  behaviour; it has no process for analysing a system under design, and only
  covers attacks someone has already seen and reported.
- **No ordering.** Tactics are tags, not stages; ATT&CK does not describe the
  *sequence* of techniques in an attack. Sequences need something else (Attack
  Flow, or the Kill Chain's phases).
- **Enterprise-IT bias.** Strongest for Windows/Linux/cloud enterprise
  environments; other domains need their own matrices (Mobile, ICS) or new
  tactic categories, which the paper allows for.
- **Moving target.** The matrix changes with each ATT&CK release; this paper is
  the March 2020 revision and its counts and examples may be outdated.
