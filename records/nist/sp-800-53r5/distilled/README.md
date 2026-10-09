---
schema: "library-distilled-index/v1"
id: sp-800-53r5-distilled
record: sp-800-53r5
type: index
kind: index
updated: "2026-10-02"
extracted: "2026-10-02"
reviewed_by: ""
---

# sp-800-53r5: distilled artifacts (partial, status: summarized)

This is **not** an FX-1 record. The SDL lane extracts only the controls it needs. Other families,
the Discussion text, references and SP 800-53A objectives are not extracted.

| kind | file | coverage |
|---|---|---|
| requirements | requirements.yaml | 107 entries. SA-3, SA-4, SA-8, SA-10, SA-11, SA-15, SA-17 and SA-24, each with all of its enhancements (86, of which 3 are withdrawn). Also SI-2(7), and the SR-1..SR-12 base statements, with SR enhancements listed by id and title only. Verbatim text: 104 entries from the PDF, 3 from OSCAL 5.2.0 (`text_source`). Each entry carries baselines from the OSCAL 5.2.0 profiles and Related Controls as `maps_to`. |
| diagram | object-model.yaml | Object-model pass: 20 objects, 24 edges, 6 gaps |
| diagram | object-model.md | Mermaid class diagram and reading notes |
| design-notes | design-notes.md | Inbound SSDF→SP80053 map, bearing on R-040..R-044 and DEC-009, and open questions |
| verification | verification.md | Verify pass (2026-10-02). Confirms the stated coverage (8 SA controls, 86 enhancements, SI-2(7), SR-1..12 + 15 listed) and that the text is verbatim. Records 3 defects fixed and residual issues. |

Not produced, because the record is partial: `normative.md`, `schema/`, `messages.yaml`,
`protocol.*`, `state-machine.yaml` and `examples/`. The catalog's own machine-readable schema is
OSCAL (`usnistgov/oscal-content`), which we reference rather than copy.
