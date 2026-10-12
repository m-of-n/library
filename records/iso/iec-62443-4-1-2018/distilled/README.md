---
schema: "library-distilled/v1"
id: iec-62443-4-1-2018-distilled
record: iec-62443-4-1-2018
type: index
updated: "2026-10-02"
---

# IEC 62443-4-1:2018 — distilled artifacts

Paywalled standard. **Not** an FX-1 full extraction: nothing was read from the IEC normative body.
Sources: IEC webstore preview (ToC, Scope, Intro, Fig 1–2), iTeh authorised-distributor sample (terms
3.1.1–3.1.17), ISASecure SDLA-312 v6.3 (reproduces each requirement's description), SDLA-300 v1.9.

| File | Coverage |
|---|---|
| `normative.md` | Scope, normative refs, Intro provenance, Fig 2 roles, 17 terms, all 47 requirements (84 statements) with IEC clause + SDLA-312 page, Table 3. Missing: Clause 4 (concepts, maturity model, Table 1, Fig 3), every "Rationale and supplemental guidance" subclause, purpose subclauses (SDLA-312 wording used instead), Table 2, Annexes A/B. |
| `requirements.yaml` | `library-requirements/v2`: 8 practices + 84 statements covering all 47 native ids (SM-1..13, SR-1..5, SD-1..4, SI-1..2 + 8.2 Applicability, SVV-1..5, DM-1..6, SUM-1..5, SG-1..7); verbatim text via SDLA-312 (83/84 mechanically verified); derived actor/nature/phase/deliverables; verification = SDLA-312 validation ids. Counts reconciled against SDLA-312 (91 shall). |
| `state-machine.yaml` | security-related-issue lifecycle (stated, DM-1..5/SM-11), ML1–ML4 progression (inferred, secondary sources), ISASecure SDLA certification lifecycle (SDLA-300). |
| `object-model.yaml` / `object-model.md` | 54 objects, 38 edges, 10 gaps; Mermaid class diagram. |
| `design-notes.md` | adopt/adapt/reject vs R-040..R-044, DEC-003, DEC-009; MAP-0001 corrections; open questions; licensing caveat. |

Not produced: `schema/`, `messages.yaml`, `protocol.yaml`, `examples/` — the standard defines process
requirements only (no data formats, messages or test vectors); the DM/SUM user-notification flow is held
in `state-machine.yaml`.

## Verification

`verification.md` — independent verify-only pass (paywalled source: provenance, coverage honesty, no unofficial copies), 2026-10-02: method, counts, every defect found and how it was fixed, residual issues.
