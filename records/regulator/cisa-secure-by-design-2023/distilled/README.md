---
schema: "library-distilled/v1"
id: cisa-secure-by-design-2023-distilled-index
record: cisa-secure-by-design-2023
type: index
updated: "2026-10-02"
---

# Distilled artifacts: cisa-secure-by-design-2023

Source: *Shifting the Balance of Cybersecurity Risk: Principles and Approaches for Secure by Design
Software*, CISA + 17 partner agencies, revision of 2023-10-25, 36 pp., sha256 `774b82b1…583b6`.
All artifacts come from the restored capture `.cache/cisa-secure-by-design-2023.md`, which is gitignored
and documents its normalisation of ligatures and full stops. Pass 1 (extract) only; the verify and
cross-check passes are pending.

| Artifact | Kind | Coverage |
|---|---|---|
| `normative.md` | normative | Every normative statement, verbatim, in source order with section and page: 10 definitional/scope statements plus all 152 requirement texts, grouped by source section. Ends with a list of the deliberately excluded statements and why. |
| `requirements.yaml` | requirements | 152 entries, `library-requirements/v2`: the 3 principles, 3 operational tactics, 37 Demonstrating-This-Principle practices (P1 18, P2 13, P3 6), 12 secure-by-design tactics, 8 secure-by-default tactics, 2 secure-by-default definition bullets, 16 customer recommendations and 71 narrative recommendation sentences. BCP 14 count 0/0. Own-form reconciliation: should 114→111, must 8→4, recommend* 18→10, may 23→12, urge* 5→5, encourage* 11→9, need to 7(9)→6, each exclusion itemised. `maps_to` carries only mappings the source prints: 14 links (11 SSDF task ids in tactic titles, PO.1.2 from footnote 3, and the SSDF as a whole for P1-DEV-1 and P2-DEV-3). |
| `design-notes.md` | design-notes | Adopt / adapt / reject against R-040..R-044, DEC-009 and R-036; five model gaps (G1–G5) with open questions; three source-level observations (S1–S3). |
| `object-model.yaml` | diagram | Object-model pass: 58 objects, 38 edges, 9 gaps, each with a locator and a tmodel mapping; 1 inferred object and 1 inferred edge, both flagged. |
| `object-model.md` | diagram | Mermaid class diagram of the core model and the mapping table to ARCH-0001/DL-0009. |
| `verification.md` | verification | FX-1 passes 2 (verify) and 3 (cross-check), independent verifier 2026-10-03: method, counts, defects found and fixed, residual issues |

Not applicable (reasons are in `record.yaml` `distillation.not_applicable`): schema, messages, protocol,
state-machine, examples.
