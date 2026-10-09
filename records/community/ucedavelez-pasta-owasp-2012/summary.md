---
schema: "library-summary/v1"
id: ucedavelez-pasta-owasp-2012
record: ucedavelez-pasta-owasp-2012
type: summary
updated: "2026-09-29"
---

# Real World Threat Modeling Using the PASTA Methodology

|  |  |
|---|---|
| **Type** | presentation slides (61 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Tony UcedaVélez (VerSprite) |
| **Published** | OWASP AppSec EU 2012 |
| **Identifier** | https://wiki.owasp.org/images/a/aa/AppSecEU2012_PASTA.pdf |
| **Source** | same (PDF, OWASP wiki archive) |
| **Digest** | `92f78b709f3a1b6335d17c09f11fad336192e515abb2638a2f38ae76c6ea81e4` (retrieved 2026-09-29) |

## Overview

The creator's own walkthrough of PASTA (Process for Attack Simulation and Threat
Analysis), the freely available primary source for the method (the full book,
`pasta-risk-centric-threat-modeling`, is paywalled). It argues that pen tests,
vulnerability scans and static analysis each give a partial view, and that a
**risk-centric** method should tie threats to business impact. It defines the
vocabulary first (asset, threat, vulnerability, attack, countermeasure, use and
abuse case, attack vector, attack surface, actor, impact) and then walks the
**seven stages** on an online-banking example: (1) define business and security
objectives, (2) define technical scope, (3) decompose the application (actors,
use cases, trust boundaries, data-flow diagrams), (4) threat analysis from threat
intelligence, (5) weakness and vulnerability analysis (mapped to MITRE CWE),
(6) attack enumeration and modeling with **attack trees** and use/abuse cases,
(7) risk and impact analysis, residual risk and countermeasures. It argues risk
should include a **probability** term informed by attack simulation, not only
threat × vulnerability × impact.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Primary description of a major risk-centric threat-modeling method. |
| Cryptography | none | Not about cryptography. |
| This project | core | PASTA links business impact, CWE weaknesses, attack trees and countermeasures in one process — close to tmodel's object model and risk goals (RPT-0002 §3). |

Bears on **DEC-001** (object model), **DEC-003** (risk metric — business impact
and probability) and **DEC-005** (MVP scope).

## Implementations

No open-source PASTA tool found. Commercial support is offered by VerSprite (the
author's firm) and by threat-modeling platforms that list PASTA among supported
methods; see tmodel RPT-0003. Searched 2026-09-29.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Slides, not a specification.** Stages are listed with activities but no
  precise inputs, outputs or scoring rules; the book is needed for detail.
- **Heavy process.** Seven stages across business, architecture, threat
  intelligence and testing; realistic only with several roles and a lot of time
  (SEI: "laborious").
- **Risk formula is informal.** The probability term is argued for, but how to
  compute it is not defined here.
- **Web-application focus.** The worked example is an online bank; applying it
  to hardware, embedded or AI systems is not shown.
- **Author-vendor source.** Written by the method's creator, whose firm sells
  PASTA services; independent evaluations are thin.
