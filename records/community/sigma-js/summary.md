---
schema: "library-summary/v1"
id: sigma-js
record: sigma-js
type: summary
updated: "2026-10-05"
---

# Sigma.js documentation and project

## Overview

Sigma.js 3.0.3 is an MIT-licensed WebGL graph renderer built around the Graphology data
model. Official documentation covers camera and pointer interaction, events, rendering,
custom layers, and reducers that can alter presentation without mutating graph data.
Layouts and editing/review application behavior require Graphology packages or surrounding
code.

## Evidence used by RPT-0006

- Documentation: https://www.sigmajs.org/docs/
- Graph data and reducers: https://www.sigmajs.org/docs/advanced/data/
- Layers: https://www.sigmajs.org/docs/advanced/layers/
- Repository, release state, and MIT license: https://github.com/jacomyal/sigma.js
- RPT-0006 assesses stable 3.0.3; visible v4 releases were alpha and were not treated as
  stable-v3 capabilities.

## Applicability

Core candidate evidence for Issue #10 rendering, focus, path styling, and separation of
view state from domain facts. It bears on no accepted decision in this record.

## Limits

The source does not provide a complete editor, coordinated review console, or AI proposal
workflow. The RPT-0006 adapter observation is internal hands-on evidence, not a claim from
these external sources.
