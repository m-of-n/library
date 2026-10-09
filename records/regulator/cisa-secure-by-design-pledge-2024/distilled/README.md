---
schema: "library-distilled/v1"
id: cisa-secure-by-design-pledge-2024-distilled
record: cisa-secure-by-design-pledge-2024
type: index
updated: "2026-10-02"
---

# cisa-secure-by-design-pledge-2024 — distilled artifacts

| file | kind | coverage |
|---|---|---|
| `normative.md` | normative | all 72 statements verbatim by goal + Goal 7 sub-bullets + sign-up template; PDF vs web-page differences listed |
| `requirements.yaml` | requirements | 72 entries: 8 goal statements (7 goals + G6-2), 12 recommendations, 19 example approaches, 17 example-evidence items, 7 notes, plus scope/status/permission/commitment/definition items (incl. 3 web-only); own-form counts reconciled; `related_inferred` (lane judgement) instead of maps_to |
| `messages.yaml` | messages | sign-up email (from the web page), progress publication per goal, challenges report, VDP elements, CVE record fields |
| `protocol.yaml`, `protocol.md` | protocol | sign / report progress / report challenges; Mermaid |
| `state-machine.yaml` | state-machine | pledge lifecycle (5 states) + per-goal status (4 states) |
| `object-model.yaml`, `object-model.md` | diagram | object-model pass: 14 objects, 11 edges, 3 gaps |
| `design-notes.md` | design-notes | R-040..R-044, DEC-009 |
| `verification.md` | verification | FX-1 passes 2 (verify) and 3 (cross-check), independent verifier 2026-10-03: method, counts, defects found and fixed, residual issues |

Not applicable: schema (no data structure defined; the sign-up email has 3 fields, held in
messages.yaml), examples (the source's "examples" are example approaches/evidence, extracted as
requirements; there are no fixtures or vectors).
