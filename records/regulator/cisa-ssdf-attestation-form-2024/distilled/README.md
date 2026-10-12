---
schema: "library-distilled/v1"
id: cisa-ssdf-attestation-form-2024-distilled
record: cisa-ssdf-attestation-form-2024
type: index
updated: "2026-10-02"
---

# cisa-ssdf-attestation-form-2024 — distilled artifacts

| file | kind | coverage |
|---|---|---|
| `normative.md` | normative | all 67 extracted statements verbatim by part (instructions, Section I, II, III, burden, appendix) + the Appendix crosswalk table verbatim |
| `requirements.yaml` | requirements | 67 entries: instruction obligations (INS-*), form controls (I-*, II-*), the 12+ Section III attestation items with the form's own `maps_to` EO 14028 §4(e) + SSDF tasks; counts reconciled |
| `schema/attestation-form.schema.json` | schema | DERIVED JSON Schema 2020-12 of the PDF form (Sections I–III, signature vs 3PAO oneOf), x-locator on every field |
| `messages.yaml` | messages | the form as a message (sections, fields, encodings online/PDF) + 3PAO assessment, POA&M package, extension/waiver request, lapse notification, addendum, Privacy Act statement |
| `protocol.yaml`, `protocol.md` | protocol | 6 flows (online, PDF, 3PAO, cannot-attest, revise/lapse, addendum) with error paths; Mermaid |
| `state-machine.yaml` | state-machine | attestation lifecycle: 10 states, 15 transitions (incl. forward-binding across versions, lapse, PRA expiry) |
| `examples/` | examples | the source's one example (PDF filename convention) as vectors + 2 constructed JSON instances (valid / invalid) validated against the schema |
| `object-model.yaml`, `object-model.md` | diagram | object-model pass: 25 objects, 24 edges, 5 gaps; Mermaid |
| `design-notes.md` | design-notes | adopt/adapt/reject vs R-041..R-044, DEC-009; 3 open questions |
| `verification.md` | verification | FX-1 passes 2 (verify) and 3 (cross-check), independent verifier 2026-10-03: method, counts, defects found and fixed, residual issues |
