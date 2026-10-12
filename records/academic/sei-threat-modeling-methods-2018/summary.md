---
schema: "library-summary/v1"
id: sei-threat-modeling-methods-2018
record: sei-threat-modeling-methods-2018
type: summary
updated: "2026-09-28"
---

# Threat Modeling: A Summary of Available Methods

|  |  |
|---|---|
| **Type** | paper (SEI technical white paper, 26 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Nataliya Shevchenko, Timothy A. Chick, Paige O'Riordan, Thomas P. Scanlon, Carol Woody |
| **Published** | July 2018 (web posting 2018-08-09), Software Engineering Institute, Carnegie Mellon University |
| **Identifier** | https://www.sei.cmu.edu/library/threat-modeling-a-summary-of-available-methods/ |
| **Source** | https://www.sei.cmu.edu/documents/569/2018_019_001_524597.pdf |
| **Digest** | `92e2bd703fd347d11c43a6f75424cbcb7d114fe12184db632ba72f18e7d6e896` (PDF, retrieved 2026-09-28) |

## Overview

A short survey of twelve threat-modeling methods — STRIDE (and variants),
PASTA, LINDDUN, CVSS, attack trees, Persona non Grata, Security Cards, hTMM,
Quantitative TMM, Trike, VAST, and OCTAVE — each described in one to two pages
with its steps, origin, and known weaknesses. Its central claim is that no
method is best: the choice depends on the target (risk, security, or privacy),
the time available, the team's experience, and how involved stakeholders want
to be, and methods are often combined (hTMM and Quantitative TMM are themselves
combinations). It closes with a qualitative feature table (Table 3) comparing
the methods on traits such as built-in prioritisation, stakeholder
collaboration, consistency of results, automated components, and quality of
documentation. It also stresses modeling early in development and notes that
cyber-physical systems widen the range of threats to consider.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A survey of security (and privacy) threat-modeling methods. |
| Cryptography | none | Does not address cryptography. |
| This project | core | The backbone source for RPT-0002 (tmodel #6): it covers most of the frameworks in the comparison and gives a first cross-method feature table. |

Bears on **DEC-001** (object model — how existing methods represent threats and
attack steps) and **DEC-005** (MVP scope — which methods tmodel should support).

## Implementations

The paper surveys methods, not software. Tools that implement the methods it
covers include the Microsoft Threat Modeling Tool (STRIDE; named in the paper),
OWASP Threat Dragon, OWASP pytm, IriusRisk and ThreatModeler. Searched
2026-09-28; tools are compared in detail in tmodel RPT-0003 (#7).

| Name | Kind | License | URL |
|---|---|---|---|
| Microsoft Threat Modeling Tool | desktop tool (STRIDE) | free, proprietary | https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool |
| OWASP Threat Dragon | open-source tool | Apache-2.0 | https://github.com/OWASP/threat-dragon |
| OWASP pytm | open-source library | MIT (threat catalog includes CAPEC material under MITRE's terms) | https://github.com/OWASP/pytm |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Dated (2018).** It predates LLM-assisted and agentic-AI threat modeling
  (e.g. MAESTRO), and newer versions of the methods it covers (it describes CVSS v3.0).
- **Not every framework in scope.** MITRE ATT&CK and the Cyber Kill Chain are
  not covered; other sources are needed for those rows of RPT-0002.
- **CVSS is a scoring system, not a threat-modeling method**, although the paper
  lists it as one.
- **The feature table is qualitative.** It is a list of traits per method with no
  stated criteria or evidence, and methods do not all get the same traits
  assessed, so it cannot be read as a scored comparison.
- **Attack paths are not compared.** It does not compare how each method
  represents multi-step attacks — the key question for tmodel's `AttackStep` /
  `AttackPath` (ARCH-0001 §3); RPT-0002 has to derive that itself.
- **Tooling and interchange formats are barely covered**, apart from the
  Microsoft tool.
- **A factual slip:** it credits attack trees to "Bruce Schneider"; the author is
  Bruce Schneier (1999).
