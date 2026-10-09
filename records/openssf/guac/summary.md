---
schema: "library-summary/v1"
id: guac
record: guac
type: summary
updated: "2026-09-26"
---

# GUAC — Graph for Understanding Artifact Composition (OpenSSF)

|  |  |
|---|---|
| **Type** | repo (implementation) |
| **Source** | https://github.com/guacsec/guac |

## Overview

Aggregates software-security metadata into a graph DB; ingests CycloneDX/SPDX SBOMs, SLSA/in-toto attestations, OSV/OpenVEX/CSAF; three trees: Evidence, Actor, Software (pURL).

## Applicability to tmodel

Closest working analog to tmodel's supply-chain portion; its 3-tree split maps to assets/components vs threats/mitigations vs review provenance.

- Ratings — security: core · cryptography: adjacent · this project: core
- Bears on: DEC-001,DEC-004
- Gathered for RPT-0011 (Knowledge Graphs and NSF OKN), tmodel #25.
