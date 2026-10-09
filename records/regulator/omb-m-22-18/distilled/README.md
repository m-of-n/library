---
schema: "library-distilled/v1"
id: omb-m-22-18-distilled
record: omb-m-22-18
type: index
updated: "2026-10-02"
---

# omb-m-22-18 — distilled artifacts

| file | kind | coverage |
|---|---|---|
| `normative.md` | normative | all 58 extracted statements verbatim in the memo's outline (Intro, §I–§IV) + Appendix A table verbatim + definitions |
| `requirements.yaml` | requirements | 58 entries (`omb-m-22-18#<outline id>`), library-requirements/v2; every lowercase shall/must/required/should/may/will statement of the body; Appendix A rows are restatements (cited, not duplicated); counts reconciled in header; all `status: rescinded` |
| `messages.yaml` | messages | 14 documents the memo names (self-attestation with its minimum fields, 3PAO assessment, POA&M package, SBOM, artifacts, VDP evidence, extension/waiver requests, inventory, common form ...) with `constrained_by` |
| `protocol.yaml`, `protocol.md` | protocol | 6 flows (solicitation/attestation, 3PAO, POA&M, artifacts, extension/waiver, repository) + Mermaid sequence diagram |
| `state-machine.yaml` | state-machine | software-item lifecycle (10 states, 14 transitions) + program milestones M1–M11 with offsets and computed dates |
| `object-model.yaml`, `object-model.md` | diagram | object-model pass: 21 objects, 18 edges, 5 gaps; Mermaid class diagram; tmodel mapping |
| `design-notes.md` | design-notes | adopt/adapt/reject vs R-041..R-044, DEC-009; 3 open questions |
| `verification.md` | verification | FX-1 passes 2 (verify) and 3 (cross-check), independent verifier 2026-10-03: method, counts, defects found and fixed, residual issues |

Not applicable: `schema/` (the memo defines the attestation's minimum content in prose, held as a
message; the field-level schema of the actual form is in cisa-ssdf-attestation-form-2024),
`examples/` (the memo contains no examples).
