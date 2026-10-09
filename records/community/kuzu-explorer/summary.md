---
schema: "library-summary/v1"
id: kuzu-explorer
record: kuzu-explorer
type: summary
updated: "2026-10-05"
---

# Kùzu Explorer

## Overview

Kùzu Explorer is an MIT-licensed browser interface for the Kùzu graph database, built with
Vue, Monaco, and G6 and distributed through Docker with a WebAssembly mode. Its repository
documents read-write and read-only database access, Cypher queries, and graph-result
visualization. The repository was archived on 2025-10-10.

## Evidence used by RPT-0006

- Repository, documentation, license, and archive state: https://github.com/kuzudb/explorer
- Pinned repository HEAD: `1ceb6e2884768d7a089632b5688f401371ca44b4`

## Applicability

Local graph-query UI precedent for Issue #10. It bears on no accepted decision in this
record.

## Limits

Primary evidence is incomplete for editing gestures, layouts, focus controls, scale,
coordinated views, and human review. G6 features are not treated as Explorer features
without direct evidence. Archive status limits maintenance confidence.
