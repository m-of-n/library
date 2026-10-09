---
schema: "library-summary/v1"
id: d3-js
record: d3-js
type: summary
updated: "2026-10-05"
---

# D3.js documentation and project

## Overview

D3 7.9.0 is an ISC-licensed modular visualization toolkit. Its official modules provide
selection, drag, zoom, force simulation, and hierarchy primitives, but not a graph model,
graph editor, review workflow, or ready-made large-graph application.

## Evidence used by RPT-0006

- Force: https://d3js.org/d3-force
- Drag: https://d3js.org/d3-drag
- Zoom: https://d3js.org/d3-zoom
- Hierarchy: https://d3js.org/d3-hierarchy
- Release identity: https://github.com/d3/d3/releases
- ISC license: https://github.com/d3/d3/blob/main/LICENSE

## Applicability

Evidence for the low-level custom-visualization path in Issue #10, including possible
coordination of graph and non-graph views. It bears on no accepted decision in this record.

## Limits

The documentation does not establish a practical tmodel graph-size target or reduce the
application work needed for editing, accessibility, persistence, and human review.
