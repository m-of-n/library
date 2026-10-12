---
schema: "library-distilled-index/v1"
id: bsimm-16-distilled
record: bsimm-16
kind: index
type: index
title: "bsimm-16 — distilled artifacts"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts — BSIMM16

Source: `bsimm-report.pdf` (sha256 `d34e341f…dc2`, 96 pp.). Passes: extract, then independent verify and cross-check (2026-10-03, `verification.md`).

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 4 domains (Table 7), 12 practice intros and all 128 activity descriptions verbatim (Part 8), with level, firms/111 and % per activity; terminology and level semantics quoted |
| requirements | `requirements.yaml` | 144 entries (4 domains + 12 practices + 128 activities); level 1/2/3 = 40/41/47; observation counts from Figure 18; Table 9 lineage as `former_ids`; Top-10-by-vertical and AI/ML key-activity flags; 28 `maps_to` links (Tables 3-4, SSDF) |
| schema | `schema/bsimm-activity.derived.schema.json` | DERIVED JSON Schema: activity label grammar, activity, scorecard row, firm scorecard; the Figure 8 EXAMPLEFIRM scorecard validates (41 activities observed) |
| messages | — | not applicable (record.yaml) |
| protocol | — | not applicable (record.yaml) |
| state-machine | `state-machine.yaml` | (A) SSI states emerging/maturing/enabling, stated, with the one stated transition; (B) activity-in-model lifecycle (added at L3, moved/relabelled, dropped) |
| examples | `examples/` | Figure 18 scorecard (128 rows, counts + %), Figure 8 example-firm scorecard, Table 16 Top-10 by 9 verticals, Table 8 new-activity observations BSIMM7-16, Table 9 activity changes (86 parsed), Tables 3-4 SSDF mapping (22 + 6 rows) |
| design-notes | `design-notes.md` | adopt / adapt / reject vs R-040…R-044, ARCH §2b/§4/§5, MAP-0001; 6 source defects; 4 open questions |
| verification | `verification.md` | pass 2 (verify) and pass 3 (cross-check) report |
| diagram | `object-model.yaml`, `object-model.md` | object-model pass: 29 objects, 20 edges, Mermaid, 4 gaps |

Charts (box plots, spider charts, verticals' score distributions, Figures 9-13,
16-17, 19-38) are images; only captions were captured — their underlying data is
not in the PDF text and was not extracted.
