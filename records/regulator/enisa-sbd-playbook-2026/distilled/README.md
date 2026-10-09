---
schema: "library-distilled/v1"
id: enisa-sbd-playbook-2026-distilled
record: enisa-sbd-playbook-2026
type: index
updated: "2026-10-02"
---

# enisa-sbd-playbook-2026 — distilled artifacts (FX-1)

Source: ENISA Secure by Design and Default Playbook, Version 1.0, July 2026 (CC BY 4.0), ISBN 978-92-9204-802-0, doi:10.2824/4422633, sha256 `c0dc5132d162f1a06f0adab350226070a176d24b9b826a85b5874961633d357d`, 80 pages. Local: `.cache/enisa-sbd-playbook-2026.txt`, `.cache/enisa-sbd-playbook-2026.md`.

| Artifact | Coverage |
|---|---|
| `normative.md` | §2 (life cycle, Tables 1–3), §3 (22 principles), §4 all 22 playbooks (principle, objective, checklist by heading, minimum evidence, release gate, Annex C mapping), §4.23, §5 concepts, Annex C table. CC BY 4.0, changes = layout only. |
| `requirements.yaml` | 550 entries: 220 checklist actions, 119 minimum-evidence items, 125 release-gate criteria (PB-x-CL/EV/RG-nn), 6 + 8 + 5 Table 1–3 activities, 67 prose recommendations (inferred; R-0029..R-0067 added by the verify pass). `principles` (22) carry Annex C `maps_to` (62 rows → eu-cra-2024-2847). BCP 14 0/0, reconciled. |
| `messages.yaml` | 11 structures: attestation (4 information groups), attestation claim (Fig. 5), release review record, exception, risk register entry, threat-model scope note, top threat, vulnerability register entry, log event, access model row, life-cycle policy. |
| `schema/` | 10 derived schemas from messages.yaml + hand-derived `attestation-claim.derived.schema.json` (Fig. 5 fixture validates). |
| `protocol.yaml`, `protocol.md` | P1 release with gates, P2 vulnerability intake → fix, P3 attestation and third-party verification. |
| `state-machine.yaml` | SM1 support life-cycle states, SM2 security posture, SM3 onboarding, SM4 vulnerability disposition, SM5 update installation. |
| `examples/` | SafeGate-X1 (§5.4.2): scope, trust boundaries, T1–T5, controls, verification table, gate rules; Figure 5 JSON fixture. |
| `object-model.yaml`, `object-model.md` | 39 objects, 19 edges, 7 gaps; Mermaid. |
| `design-notes.md` | Adopt/adapt/reject vs R-040..R-044, DEC-009; 7 open questions/defects. |
| `verification.md` | FX-1 passes 2 (verify) and 3 (cross-check), independent verifier, 2026-10-02/03: methods, counts, defects fixed (39 dropped prose recommendations added; Figure 5 re-checked from the native image), residuals. |
