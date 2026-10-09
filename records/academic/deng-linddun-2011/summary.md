---
schema: "library-summary/v1"
id: deng-linddun-2011
record: deng-linddun-2011
type: summary
updated: "2026-09-29"
---

# A privacy threat analysis framework: supporting the elicitation and fulfillment of privacy requirements

|  |  |
|---|---|
| **Type** | paper (journal article, 27 pp. author manuscript) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Mina Deng, Kim Wuyts, Riccardo Scandariato, Bart Preneel, Wouter Joosen (KU Leuven) |
| **Published** | *Requirements Engineering* 16(1):3–32, Springer, 2011 |
| **Identifier** | DOI 10.1007/s00766-010-0115-7 |
| **Source** | author manuscript: https://cosicdatabase.esat.kuleuven.be/backend/publications/files/journal/1412 |
| **Digest** | `e2b0187290cb90f6f16a9e9fbb33d17482af322a24578f5195ac82eef542b1ea` (author manuscript PDF, retrieved 2026-09-29) |

## Overview

The paper that introduced **LINDDUN**, a privacy counterpart to STRIDE. It argues
that few systematic methods exist for privacy threats and adapts Microsoft's
STRIDE process: the system is modelled as a data-flow diagram, and seven privacy
threat categories — Linkability, Identifiability, Non-repudiation, Detectability,
information Disclosure, content Unawareness, policy and consent Non-compliance —
are mapped to the DFD element types where they can occur. It separates **hard
privacy** (data minimisation: the user shares as little as possible) from **soft
privacy** (the user trusts the controller, who must protect the data), and lists
the privacy properties each threat violates (e.g. unlinkability, anonymity,
undetectability). Its three contributions are the threat-to-DFD **mapping table**,
a catalogue of **privacy threat tree patterns** that detail each threat, and a
mapping from threats to **privacy-enhancing technologies** (PETs); threats are
documented as misuse cases.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Privacy threat modeling; also relevant to data security. |
| Cryptography | adjacent | Several privacy-enhancing technologies it maps to are cryptographic. |
| This project | core | The original LINDDUN method for RPT-0002 §5; its threat-tree patterns and threat→element mapping are reusable knowledge for tmodel. |

Bears on **DEC-001** (object model) and **DEC-005** (MVP scope — whether privacy
threats are in scope).

## Implementations

The method is maintained at linddun.org (`linddun-org`), which offers the LINDDUN
GO card deck and LINDDUN PRO. OWASP Threat Dragon lists LINDDUN among its
supported threat categories. Searched 2026-09-29.

| Name | Kind | License | URL |
|---|---|---|---|
| OWASP Threat Dragon | open-source threat-modeling tool (LINDDUN threats) | Apache-2.0 | https://github.com/OWASP/threat-dragon |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Superseded names.** The 2011 categories have since been renamed on
  linddun.org (e.g. *Linking*, *Identifying*, *Data disclosure*, *Unawareness &
  unintervenability*); cite the current names for current practice.
- **Inherits STRIDE's scaling problem.** Threats multiply with every DFD element;
  SEI notes it is labour-intensive and that generic threats hurt efficiency.
- **Privacy only.** Security threats need STRIDE or another method alongside.
- **Digest is of the author manuscript**, not the Springer version of record.
