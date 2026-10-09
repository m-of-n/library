---
schema: "library-distilled-index/v1"
id: microsoft-sdl-distilled
record: microsoft-sdl
kind: index
type: index
title: "microsoft-sdl — distilled artifacts"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts — Microsoft SDL (current web practice set)

Source: 16 pages fetched 2026-10-02 (`.cache/microsoft-sdl.md`). Passes: extract, then independent verify and cross-check (2026-10-03, `verification.md`).

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 5 lifecycle-stage statements, all 10 practice introductions and all 48 sub-practices verbatim (link lists omitted), plus the FAQ's legacy twelve-practice list and its "Legacy archive" statements |
| requirements | `requirements.yaml` | 73 entries: 10 practices, 48 sub-practices (Microsoft's own n.m ids), 5 stages, 7 exception-process steps, 3 exception properties; resource links per sub-practice; no maps_to (Microsoft publishes none) |
| schema | — | not applicable (record.yaml) |
| messages | — | not applicable (record.yaml) |
| protocol | `protocol.yaml`, `protocol.md` | the exception request/approval exchange of 1.4 (roles, 4 messages, 3 flows) — inferred names, stated steps |
| state-machine | `state-machine.yaml` | security exception lifecycle (9 states, 10 transitions each quoting its step) |
| examples | `examples/threat-modeling-examples.yaml` | every example list on the practice 3 page: STRIDE table, context questions, tangible/intangible assets, trust boundaries, assumptions, threat fields, secure design practices |
| design-notes | `design-notes.md` | adopt / adapt / reject vs R-040…R-044, ARCH §1/§2/§3b/§5, MAP-0001; source observations |
| verification | `verification.md` | pass 2 (verify) and pass 3 (cross-check) report |
| diagram | `object-model.yaml`, `object-model.md` | object-model pass: 33 objects, 18 edges, 4 gaps |
