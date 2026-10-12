---
schema: "library-distilled/v1"
id: etsi-ts-104-219-distilled
record: etsi-ts-104-219
type: index
updated: "2026-10-02"
---

# etsi-ts-104-219 — distilled artifacts (FX-1)

Source: ETSI TS 104 219 V1.1.1 (2026-03), sha256 `17aee144482cfe85691b6d9e66c312fad3183391442a68ea741946795f607c15`, 78 pages. Local renderings (gitignored): `.cache/etsi-ts-104-219.txt` (pdftotext -layout) and `.cache/etsi-ts-104-219.md` (faithful Markdown capture; clause-5 tables and Annexes A/B rebuilt from parsed cells; figures not reproduced).

| Artifact | Coverage |
|---|---|
| `normative.md` | Modal-verbs clause; framing statements (5.0.1, 5.0.4 conformance definition, clause 3.1 terms used by actions); Tables 5.0-1/5.0-2/5.0-3; all 42 task tables of 5.1.1–5.6.1 verbatim (task statement, CSC Safeguard, SAFECode practices, DG Specific Actions by DG scope, DG Artifacts, Responsible Roles, informative Implementation Examples); Annex A (CRA), B.1 (CRT APC), B.2 (29 frameworks); Annex C differences noted. Introduction/clause 4 history and Annex D history are left to `.cache`. |
| `requirements.yaml` | 220 entries: 183 numbered DG actions (111 shall → requirement, 72 should → recommendation), 3 'same as' inheritance entries (PW.5.1, PW.6.2, PW.9.2), 34 prose 'should' recommendations (R-0001..R-0034). Plus `tasks` (42) with statement, CSC, SAFECode, DG artifacts, roles, examples and 768 `maps_to` (task-table rows: CSC 36, SAFECode 31; Annex A CRA 54; Annex B.1 CRT APC 128; Annex B.2 519). BCP 14 count 0, reconciled against the ETSI shall/should baseline. Verbatim check: every `text` is an in-order token subsequence of the source (0 failures). |
| `crosswalk.yaml` | Inverse index of the published mappings (framework → ref → SSDIF tasks) + the CRA and CRT tables row by row. Generated from requirements.yaml. |
| `messages.yaml` | 15 work-product structures whose content the TS prescribes (process document, threat model, threat, security bug, bug bar, shall-fix list, product spec, design review, tool config, TPC risk assessment, component inventory, reporting policy, handling policy, remediation record, setting doc), fields tied to action ids. |
| `schema/` | 15 derived JSON Schemas generated from messages.yaml (source has no schema). |
| `protocol.yaml`, `protocol.md` | 4 flows with roles, error paths and Mermaid: vulnerability disclosure/remediation (3 phases of 5.6.0), threat model → bugs → fix, bug-bar release gate, third-party component acceptance. |
| `state-machine.yaml` | 4 machines: vulnerability (SM1), security bug vs bug bar (SM2), third-party component (SM3), SDL process document (SM4). Only timer in source: triage "commonly ... one week". |
| `object-model.yaml`, `object-model.md` | Object-model pass: 60 objects, 36 edges (2 inferred), 7 gaps vs ARCH-0001/DL-0009; Mermaid class diagram. |
| `design-notes.md` | Adopt/adapt/reject vs R-040..R-044, DEC-009; 7 open questions incl. source defects (item 7: B.2 PW.1.1/PS.3.2 mislabel). |
| `verification.md` | FX-1 passes 2 (verify) and 3 (cross-check), independent verifier, 2026-10-02/03: methods, counts, defects fixed, residuals. |

Not applicable: `examples/` — see record.yaml.
