---
schema: "library-distilled-index/v1"
id: microsoft-sdl-simplified-2010-distilled
record: microsoft-sdl-simplified-2010
kind: index
type: index
title: "microsoft-sdl-simplified-2010 — distilled artifacts"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts — Simplified Implementation of the Microsoft SDL (2010)

Sources: the .doc (sha256 `ef676ae4…d413`, 17 pp.) and its companion
`Simplified SDL_Spreadsheet.xlsx` (sha256 `094b8e5f…49c9`). Passes: extract, then independent verify and cross-check (2026-10-03, `verification.md`).

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | the paper from the Optimization Model to the Verification Process verbatim with ids on headings; all 28 spreadsheet rows verbatim |
| requirements | `requirements.yaml` | 61 entries: 16 mandatory practices (SP-01…16), 3 optional, 8 process requirements/sections, 6 text-box callouts, 28 spreadsheet rows (XLS-…); 9 entries added by the verify pass |
| schema | `schema/simplified-sdl.derived.schema.json` | DERIVED enums (maturity level, capability area, P1-P3, FSR outcome, roles) and an inferred compliance-tracking record |
| state-machine | `state-machine.yaml` | Optimization Model levels; FSR outcomes and release certification guards |
| messages, protocol, examples | — | not applicable (record.yaml) |
| design-notes | `design-notes.md` | adopt / adapt / reject vs R-040…R-044 |
| verification | `verification.md` | pass 2 (verify) and pass 3 (cross-check) report |
| diagram | `object-model.yaml`, `object-model.md` | 24 objects, 9 edges, 3 gaps |
