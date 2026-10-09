---
schema: "library-distilled/v1"
id: iso-iec-27034-1-distilled
record: iso-iec-27034-1
type: index
updated: "2026-10-02"
---

# distilled/ — ISO/IEC 27034-1 (preview-based; NOT a full FX-1 extraction)

ISO/IEC 27034-1:2011 is paywalled and was **not** read in full. Every artifact here is built from
free official material only:

- the distributor-sample (iTeh/SIST) preview of 27034-1 (pp. i–xiv and p. 1; stops after definition 3.2);
- the previews of 27034-2:2015, 27034-3:2018, 27034-5:2017, TS 27034-5-1:2018, 27034-7:2018 and
  DIS 27034-4 (2020), used for the series object model and labelled by part in every locator;
- the XSD that ISO publishes free of charge as the electronic insert of TS 27034-5-1.

The record is therefore `status: summarized` without `profile: full`.

| Artifact | Kind | Coverage |
|---|---|---|
| `normative.md` | normative | Verbatim text of the 27034-1 preview: Foreword parts list, Introduction 0.1–0.5, Clause 1 Scope, Clause 2, Clause 3.1–3.2. ToC titles of the unread body are given as locators. **Not covered:** 3.3 onward, Clauses 4–8, Annexes A–C. |
| `requirements.yaml` | requirements | 15 entries (14 "should" recommendations and 1 "cannot … unless" prohibition), all from the informative Introduction. BCP 14 count is 0 in source and extraction. The normative-body baseline is **unknown** (not read); see `reconciliation`. |
| `object-model.yaml` / `object-model.md` | diagram | Object-model pass: 45 objects and 37 edges (1 edge inferred), each with a locator naming the series part. Mermaid class diagram plus the five key findings. |
| `state-machine.yaml` | state-machine | (1) ASC lifecycle: 11 states from the XSD `life-cycle-stage` enum, with inferred transitions. (2) Application-assurance lifecycle: ASMP steps → Targeted LoT → verification → audit → Actual LoT (inferred states and transitions, all located). |
| `schema/` | schema | README with the official XSD URL, sha256, licence note and observed source defects, plus a **derived** structural outline of the XSD. The XSD itself is not copied. |
| `design-notes.md` | design-notes | Adopt / adapt / reject against R-040..R-044, DEC-009 and ARCH-0001, plus 6 open questions. |

Not produced, with reasons (also in `record.yaml` `distillation.not_applicable`):

- **messages:** the only exchange structures are the ASC package and the ASC element, which are data
  formats. They are held in `schema/`. No message exchange between parties is defined in the text read.
- **protocol:** 27034-5's title says "Protocols", but its preview and the XSD define a data
  structure and a reference model, not an exchange protocol. 27034-1 defines processes
  (ONF management, ASMP), which are captured in `state-machine.yaml`.
- **examples:** the only worked examples (Annex A, Microsoft SDL mapping; Annex B, SP 800-53 AU-14 in
  ASC format) are beyond the preview.

All artifacts: `reviewed_by` empty; readable, not buildable-on.

## Verification

`verification.md` — independent verify-only pass (paywalled source: provenance, coverage honesty, no unofficial copies), 2026-10-02: method, counts, every defect found and how it was fixed, residual issues.
