---
schema: "library-distilled/v1"
id: esf-sscs-developers-2022-distilled
record: esf-sscs-developers-2022
type: index
updated: "2026-10-02"
---

# esf-sscs-developers-2022 — distilled artifacts

| file | kind | coverage |
|---|---|---|
| `normative.md` | normative | all 490 extracted statements (27 added by pass 2) verbatim by section (§2 intro … §2.5.3, Exec Summary, §1.1, App. C, App. D) + 40 threat-scenario items + App. D artifact table summary |
| `requirements.yaml` | requirements | 490 entries `#R-0001..R-0490` (R-0464..R-0490 added by pass 2): 380 Section-2 statements/mitigations, 2 front-matter, 18 App. C SLSA statements (all 18 normative BCP 14 keywords), 3 App. D statements, 60 App. D checklist questions; maps_to = Appendix A section-level SSDF crosswalk + SSDF tasks printed in checklist rows. Derived fields heuristic |
| `crosswalk.yaml` | requirements | source-published crosswalks transcribed: Table 1 (14 rows), Appendix A (10 SSDF practices × developer/supplier/customer), Appendix B (20 dependencies) |
| `object-model.yaml`, `object-model.md` | diagram | object-model pass: 27 objects, 22 edges, 6 gaps; Mermaid |
| `design-notes.md` | design-notes | R-040..R-044, DEC-009, R-037; 3 open questions |
| `verification.md` | verification | FX-1 passes 2 (verify) and 3 (cross-check), independent verifier 2026-10-03: method, counts, defects found and fixed, residual issues |

Not applicable (reasons in record.yaml): schema, messages, protocol, state-machine, examples.
Extraction scripts (lane B scratchpad) are not committed; the parse is reproducible from
`.cache/esf-sscs-developers-2022.txt`.
