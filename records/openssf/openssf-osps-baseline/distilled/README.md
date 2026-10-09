---
schema: "library-doc/v1"
id: openssf-osps-baseline-distilled-index
record: openssf-osps-baseline
type: index
updated: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts — OSPS Baseline v2026.08.28

FX-1 (`docs/extraction.md`). The source is the Gemara YAML at tag `v2026.08.28`. The extraction
is scripted (`.cache/lane-e/osps/extract.py`, local only), so `normative.md` and
`requirements.yaml` can be regenerated from the cached tarball.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | all 8 families, 41 controls and 65 ARs (64 active + 1 retired), verbatim with locators; recommendations; applicability; control-level mappings; applicability groups; the 14 mapping references; the 40-term lexicon; maintenance rules on identifiers |
| requirements | `requirements.yaml` | 67 entries: 64 active ARs, the OSPS-BR-01.02 tombstone, and 2 recommendation MAYs. BCP 14 count is 66 source = 66 extracted. Per-AR `maps_to` is inherited from 378 control-level mappings (1177 target entries). Audit typing (phase, nature, actor_role, deliverables, verification, testable) is ours and needs review. |
| schema | `schema/` | `osps.cue` + module pin, and the 7 Gemara v1.2.0 CUE files it imports, all verbatim; `cue vet` was not run in this pass |
| messages | `messages.yaml` | 12 structures: ControlCatalog, Metadata, Group, Control, AssessmentRequirement, MappingDocument, Mapping, MappingTarget, MappingReference, LexiconEntry, Checklist (plus `constrained_by`) |
| state machine | `state-machine.yaml` | project-maturity (L1→L2→L3, guards = all ARs at that level; transitions inferred), entry-lifecycle (Gemara #Lifecycle, stated), baseline-release (devel/current/previous) |
| examples | `examples/` | 5 verbatim YAML excerpts (a control, a control with a retired AR, metadata groups, the whole SLSA mapping document, lexicon entries) with expected validation results |
| design notes | `design-notes.md` | adopt 6 / adapt 7 / reject 3 against R-040…R-044 and DEC-009, plus 7 open questions (including a source applicability anomaly) |
| diagram | `object-model.yaml`, `object-model.md` | object-model pass: 45 objects and 48 edges with locators and tmodel mappings, 8 gaps, Mermaid class/graph diagrams |
| verification | `verification.md` | FX-1 pass 2 (verify) and pass 3 (cross-check), 2026-10-02: checks, scripts, counts, defects fixed, residual issues |

Not applicable: **protocol**. OSPS defines no exchange between parties. See `record.yaml`.
