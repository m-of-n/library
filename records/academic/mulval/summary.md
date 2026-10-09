---
schema: "library-summary/v1"
id: mulval
record: mulval
type: summary
updated: "2026-09-26"
---

# MulVAL: A Logic-based Network Security Analyzer (Ou et al., USENIX Security 2005)

|  |  |
|---|---|
| **Type** | paper (white-paper) |
| **Source** | https://www.usenix.org/legacy/event/sec05/tech/full_papers/ou/ou.pdf |

## Overview

Canonical logic-based engine: vulns/config/privileges as Datalog facts, exploitation as rules; derives reachable attack paths at scale (code: github.com/risksense/mulval).

## Applicability to tmodel

Reference model for rule-based attack-path derivation; facts=nodes, rules=logic, derivation graph = the reviewable attack-path artifact.

- Ratings — security: core · cryptography: adjacent · this project: core
- Bears on: DEC-005
- Gathered for RPT-0011 (Knowledge Graphs and NSF OKN), tmodel #25.
