---
schema: "library-doc/v1"
id: owasp-asvs-5-distilled-index
record: owasp-asvs-5
type: index
updated: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts — OWASP ASVS 5.0.0

FX-1 extraction pass (claude, lane E, 2026-10-02). Verify and cross-check passes are pending, to be run
by other agents. Nothing here is human-reviewed yet.

The source is the 5.0.0 release (tag `v5.0.0_release`, 2025-05-30). The requirement set was taken from
the JSON export and checked to be identical to the CSV export and the markdown tables for all 345
requirements: id, chapter, section, text and level. The CycloneDX export texts are also identical.
Generator: `.cache/lane-e/asvs/gen.py` (local, gitignored).

| kind | file | coverage |
|---|---|---|
| requirements | `requirements.yaml` | **All 345 requirements**, ids `owasp-asvs-5#v5.0.0-<ch>.<sec>.<req>`, verbatim. Each carries level, levels, chapter, section, documentation/implementation type, actor, nature, phase, deliverables, verification, v4.0.3 mapping (stated) and legacy CWE (inferred). Also: 27 framing statements (F-*), 25 Appendix C statements (AppC-*, holding all 11 BCP 14 keywords), 48 prescriptive chapter-prose statements (P-*; lowercase must/shall/should in Control Objectives and section introductions) and 16 non-mandatory Appendix D items (AppD-*). AppC-24/25 and P-01..P-48 were added by the verify pass (2026-10-02). |
| normative | `normative.md` | All 345 requirements in chapter/section order, with each Control Objective and section text. Also: What is the ASVS?, Assessment and Certification, Changes compared to v4.x, Appendix C and Appendix D, verbatim. Omitted: front matter, the per-chapter References lists, and Appendices A, B and E. |
| fields | `crypto-registry.yaml` | Appendix C approval tables: 14 tables, 120 rows, A/L/D status, cells verbatim. |
| schema | `schema/` | 3 derived JSON Schemas (nested JSON, flat JSON/CSV, legacy item), each validated against the release assets. OWASP publishes no schema of its own. |
| messages | `messages.yaml` | The requirement identifier and all 5 export structures (JSON/XML, flat/CSV, legacy, CycloneDX, the last with a source defect). Also the verification report (inferred structure). |
| protocol | `protocol.yaml`, `protocol.md` | The verification engagement and the procurement flow, with error paths and a Mermaid sequence diagram. |
| state-machine | `state-machine.yaml` | Level attainment (cumulative L1/L2/L3, staleness on major or minor release, carry-over on patch release) and the per-requirement outcome (pass/fail/N/A). |
| examples | `examples/` | 7 identifier vectors (source and derived), and V1.1.1 verbatim in every export format with expected results. |
| design-notes | `design-notes.md` | Adopt, adapt or reject against R-040..R-044, DEC-009, R-037 and ARCH-0001 §4/§5. Includes open questions and source defects. |
| diagram | `object-model.yaml`, `object-model.md` | Object-model pass: 43 objects, 45 edges and 9 gaps, with a Mermaid class diagram. |
| verification | `verification.md` | FX-1 pass 2 (verify) and pass 3 (cross-check), 2026-10-02: checks, scripts, counts, defects fixed, residual issues |
