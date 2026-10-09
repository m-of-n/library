---
schema: "library-summary/v1"
id: neo4j-bloom
record: neo4j-bloom
type: summary
updated: "2026-10-05"
---

# Neo4j Bloom user guide

## Overview

Neo4j Bloom 2.37 is a Neo4j-backed graph exploration product. Its official guide documents
search, expansion, inspection, editing, Scenes, Perspectives, rule-based visual styling,
and a Card list. It also distinguishes temporary Scene results from properties written to
the database in its GDS workflow.

## Evidence used by RPT-0006

- User guide: https://neo4j.com/docs/bloom-user-guide/current/
- Product capabilities: https://neo4j.com/docs/bloom-user-guide/current/about-bloom/
- Perspectives, styling, and scan warning: https://neo4j.com/docs/bloom-user-guide/current/bloom-perspectives/perspective-creation/
- Temporary versus persisted GDS results: https://neo4j.com/docs/bloom-user-guide/current/bloom-tutorial/gds-integration/
- Installation, activation, and tier boundaries: https://neo4j.com/docs/bloom-user-guide/current/bloom-installation/installation-activation/

## Applicability

Product precedent for Issue #10 exploration, inspection, filtering, saved presentation
state, and direct graph editing. It bears on no accepted decision in this record.

## Limits

Bloom is coupled to Neo4j and is not documented here as an embeddable review-console SDK.
The 10-million-element statement concerns Perspective scanning, not interactive display
capacity. No AI graph-change proposal and verdict workflow was found.
