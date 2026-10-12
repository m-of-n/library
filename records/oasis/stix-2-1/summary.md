---
schema: "library-summary/v1"
id: stix-2-1
record: stix-2-1
type: summary
updated: "2026-09-26"
---

# STIX Version 2.1 (OASIS Standard)

|  |  |
|---|---|
| **Type** | spec (standard) |
| **Source** | https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html |

## Overview

OASIS Standard: threat intel as a connected graph — 17 SDO node types (Attack Pattern, Vulnerability, Course of Action, Threat Actor…), SRO edges, plus Opinion/Note objects.

## Applicability to tmodel

Proven graph schema to align tmodel to (Vulnerability↔CVE, Attack Pattern↔threat, Course of Action↔mitigation); Opinion/Note map onto the human-review layer.

- Ratings — security: core · cryptography: adjacent · this project: core
- Bears on: DEC-001,DEC-002
- Gathered for RPT-0011 (Knowledge Graphs and NSF OKN), tmodel #25.
