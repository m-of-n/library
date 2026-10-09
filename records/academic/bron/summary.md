---
schema: "library-summary/v1"
id: bron
record: bron
type: summary
updated: "2026-09-26"
---

# BRON — Linking ATT&CK, CAPEC, CWE, CVE, CPE (Hemberg et al., 2020)

|  |  |
|---|---|
| **Type** | paper (white-paper) |
| **Source** | https://arxiv.org/abs/2010.00533 |

## Overview

A bidirectional graph linking ATT&CK↔CAPEC↔CWE↔CVE↔CPE for tracing tactics→platforms; code at github.com/ALFA-group/BRON.

## Applicability to tmodel

The most directly relevant prior art: a reusable reference implementation of tmodel's CVE→CWE→CAPEC→ATT&CK backbone.

- Ratings — security: core · cryptography: adjacent · this project: core
- Bears on: DEC-001
- Gathered for RPT-0011 (Knowledge Graphs and NSF OKN), tmodel #25.
