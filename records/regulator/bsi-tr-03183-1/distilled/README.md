---
schema: "library-distilled/v1"
id: bsi-tr-03183-1-distilled
record: bsi-tr-03183-1
type: index
updated: "2026-10-02"
---

# bsi-tr-03183-1 — distilled artifacts (FX-1)

Source: BSI TR-03183-1 v1.0.0 (cover date 31.07.2026), sha256 `db5f5bfed4664faae75d13f3deb0c9140d13f8d10764f013b84e5ca912b969ef`, 79 pages. Local renderings: `.cache/bsi-tr-03183-1.txt`, `.cache/bsi-tr-03183-1.md`.

| Artifact | Coverage |
|---|---|
| `normative.md` | §2 (scope of force), §4 (assessment method incl. modal verbs, control structure, verdict rules, report contents), §5 (risk-based approach, all RH_* controls with Input/Control/Output/Reference CRA, decision criteria Tables 1–5, 7, acceptance criteria), §6 (ARC), §7, Appendix B (all ER/VH rows), Annex D tables + matrix. §3 CRA overview and Annex C example left to `.cache` (Annex C is in `examples/`). |
| `requirements.yaml` | 94 entries: 12 RH control statements (11 controls, RH_RT.1.1.2 split), 1 example ARC control, 45 lower-case prose obligations (R-0001..R-0045, inferred; R-0031..R-0045 added by the verify pass), 36 CRA Annex I sub-requirements ER/VH quoted with BSI ids. BCP 14: source 23, extracted 13, reconciled (9 definitions + 1 descriptive). `maps_to` = TR's 'Reference CRA' → eu-cra-2024-2847. |
| `messages.yaml` | 9 structures: Control (§4.5), RiskScenario, AssessmentVerdict, AssessmentReport, RiskContext, Asset, Risk, Environment, ApplicabilityStatement. |
| `schema/` | 9 derived JSON Schemas from messages.yaml. |
| `protocol.yaml`, `protocol.md` | P1 risk handling, P2 assessment, P3 CRA Art. 14 reporting (quoted context, marked stated-by-CRA). |
| `state-machine.yaml` | SM1 risk, SM2 control verdict, SM3 PwDE market lifecycle (CRA context). |
| `examples/` | Annex C SNC X5 camera risk assessment; §6.5 ARC selection; D.2 risk matrix vectors + formula check. Source inconsistencies noted inline. |
| `object-model.yaml`, `object-model.md` | 40 objects, 26 edges, 7 gaps; Mermaid. |
| `design-notes.md` | Adopt/adapt/reject vs R-040..R-044, DEC-003/009; 7 open questions incl. source defects. |
| `verification.md` | FX-1 passes 2 (verify) and 3 (cross-check), independent verifier, 2026-10-02/03: methods, counts, defects fixed (15 dropped obligations added), residuals. |
