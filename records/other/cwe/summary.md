---
schema: "library-summary/v1"
id: cwe
record: cwe
type: summary
updated: "2026-09-26"
---

# MITRE CWE — Common Weakness Enumeration

|  |  |
|---|---|
| **Type** | dataset (best-practice) |
| **Source** | https://cwe.mitre.org/ |

## Overview

Weakness catalog as a graph: typed relations (ChildOf/ParentOf/PeerOf/CanPrecede), Views/Categories/Pillars; XML (with XSD) + CSV.

## Applicability to tmodel

Source for tmodel's Weakness nodes and their hierarchy; XSD validates ingestion. Ties to ARCH-0001 §3.

- Ratings — security: core · cryptography: adjacent · this project: core
- Bears on: DEC-001
- Gathered for RPT-0011 (Knowledge Graphs and NSF OKN), tmodel #25.
