---
schema: "library-distilled-index/v1"
id: safecode-fpssd-3-distilled
record: safecode-fpssd-3
kind: index
type: index
title: "safecode-fpssd-3 — distilled artifacts"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts — SAFECode FPSSD, 3rd edition (2018)

Source PDF sha256 `9a9a07b5…33ae` (38 pp.). Passes: extract, then independent verify and cross-check (2026-10-03, `verification.md`).

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | all 52 sections of the eight practice chapters verbatim, each with its modal statements listed by id and its CWE references |
| requirements | `requirements.yaml` | 198 entries: 52 practice sections + 146 modal statements (34 requirement, 112 recommendation; 3 front-matter statements added by the verify pass); 13 CWE maps_to |
| schema | `schema/safecode-records.derived.schema.json` | DERIVED: SecurityFinding, Severity, RiskAcceptance (TSRV), SecurityAdvisory, ApplicationSecurityControl |
| messages | — | not applicable (record.yaml) |
| protocol | `protocol.yaml`, `protocol.md` | vulnerability report intake → acknowledgement → triage → fix → advisory |
| state-machine | `state-machine.yaml` | finding disposition, risk acceptance, reported-vulnerability lifecycle |
| examples | `examples/examples.yaml` | every worked example: CVSS→severity bands, approver by risk, TSRV, ASC workflow, design principles, canonicalization/sanitization, generic error messages |
| design-notes | `design-notes.md` | adopt / adapt / reject vs R-040…R-044; MAP-0001 corrections |
| verification | `verification.md` | pass 2 (verify) and pass 3 (cross-check) report |
| diagram | `object-model.yaml`, `object-model.md` | 25 objects, 14 edges, 2 gaps |
