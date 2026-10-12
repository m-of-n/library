---
schema: "library-distilled-index/v1"
id: microsoft-sdl-5-2-distilled
record: microsoft-sdl-5-2
kind: index
type: index
title: "microsoft-sdl-5-2 — distilled artifacts"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts — Microsoft SDL Process Guidance 5.2

Source `Microsoft SDL_Version 5.2.docx` (sha256 `108cd2ee…75f2`), captured by a
direct walk of the document XML. Passes: extract, then independent verify and cross-check (2026-10-03, `verification.md`).

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | Part I: every statement in every Security/Privacy Requirements and Recommendations section of all seven phases (waterfall, SDL-Agile, SDL-LOB), the FSR process and outcomes, Response, Appendices D-J and S, and the Agile requirement tables, each tagged with its R-id or `[context]`; Part II: Appendices B, M, N verbatim; Part III (verify pass): 102 modal-bearing statements outside the headed sections |
| requirements | `requirements.yaml` | 510 entries: R-0001…R-0408 (extract) + R-0409…R-0510 (102 modal-bearing statements outside the headed sections, added by the verify pass); 311 requirement, 188 recommendation, 9 FSR process, 2 descriptive; 100 SDL-Agile rows (P/Q/R), 32 compiler/tool rows (E), 4 firewall rows (D); BCP 14 5 (caps-styled text) vs 0, reconciled |
| schema | `schema/sdl-5-2.derived.schema.json` | DERIVED: SecurityWorkItem (Effect/Cause enums verbatim from Appendix B, conditional cause), Severity, PrivacyImpactRating, FSROutcome/FSRRecord, AgileRequirementRow (100 rows validate) |
| messages | — | not applicable (record.yaml) |
| protocol | `protocol.yaml`, `protocol.md` | FSR exchange (team ↔ security advisor ↔ management) and the privacy escalation response (Appendix K) |
| state-machine | `state-machine.yaml` | phase sequence, SDL applicability (subject/exempt), the FSR gate with its outcomes and guards, SDL-Agile cadences |
| examples | `examples/` | bug bars (N security server/client + DoS matrix; M privacy), LOB and Agile tables, all Agile requirement rows |
| design-notes | `design-notes.md` | adopt / adapt / reject vs R-040…R-044, ARCH §2/§3b/§4/§5, MAP-0001; 3 open questions |
| verification | `verification.md` | pass 2 (verify) and pass 3 (cross-check) report |
| diagram | `object-model.yaml`, `object-model.md` | object-model pass: 29 objects, 17 edges, 4 gaps |

Not extracted as requirements: Appendix A (privacy at a glance), C (privacy
questionnaire), K (sample PERF — in protocol), L (glossary), O (security plan
sample — a restatement of the phase requirements), T (Agile FAQ), U (LOB risk
questionnaire), V (LOB lessons learned). They remain in `.cache/microsoft-sdl-5-2.md`.
