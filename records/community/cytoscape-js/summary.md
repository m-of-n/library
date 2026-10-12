---
schema: "library-summary/v1"
id: cytoscape-js
record: cytoscape-js
type: summary
updated: "2026-10-05"
---

# Cytoscape.js documentation and project

## Overview

Cytoscape.js 3.34.0 is an MIT-licensed browser graph library with a graph model,
Canvas rendering, events, data-driven styling, algorithms, layouts, and viewport APIs.
Its documentation covers graph mutation and interaction primitives; a complete review
console, coordinated non-graph views, and proposal verdict workflow remain application work.

## Evidence used by RPT-0006

- Documentation and API: https://js.cytoscape.org/
- Repository and MIT license: https://github.com/cytoscape/cytoscape.js
- Version identity: https://zenodo.org/records/20511608
- Documented performance guidance is qualitative; RPT-0006 records its own bounded
  hands-on sanity check separately and does not treat it as a benchmark.

## Applicability

Core candidate evidence for Issue #10 visualization, interaction, layout, styling,
filtering, and domain/presentation separation. It bears on no accepted decision in this
record.

## Limits

The source set does not supply tmodel's review workflow, accessibility validation,
production-scale benchmark, or coordinated graph/table/matrix/timeline application.
