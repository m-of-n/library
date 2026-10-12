---
schema: "library-doc/v1"
id: iso-iec-29147-2018-distilled-index
record: iso-iec-29147-2018
type: index
updated: "2026-10-02"
---

# Distilled artifacts — ISO/IEC 29147:2018 (free preview only)

**Not an FX-1 extraction.** ISO/IEC 29147:2018 is paywalled (only the superseded 2014 edition was
ever on ISO's free list). Everything here is drawn from the distributor-sample (iTeh/SIST) **13-page free
preview** (Contents, Foreword, Introduction, Clauses 1–5.3.2 incl. Figure 1). The requirement-bearing
Clauses 6–9 and Annexes A–D are not available. Nothing is reviewed (`reviewed_by` empty).

| file | what it is | coverage |
|---|---|---|
| `normative.md` | scope, normative references, all 8 Clause 3 terms verbatim, the 3 visible shall/should statements, the 29147/30111 division of labour | complete for the preview; Clauses 5.3.3–9 absent |
| `requirements.yaml` | `library-requirements/v2`; 3 entries (1 shall, 2 should) with counts + reconciliation | preview only — NOT the standard's requirement set (Annex D lists it) |
| `protocol.yaml` / `protocol.md` | roles, 9 messages, 5 flows (3 stated from Figure 1, 2 inferred from headings), 3 error paths; Mermaid flowchart of Figure 1 and sequence diagrams | flows F0–F2 stated; timing rules not visible |
| `messages.yaml` | advisory (16 elements, §7.4.2–7.4.17), report, acknowledgement, remediation, disclosure policy (9 elements with required/recommended/optional tier) | **field names from headings only** — no types, cardinality or wording; CSAF 2.x correspondences noted |
| `object-model.yaml` / `object-model.md` | object-model pass: 20 objects, 19 edges, 6 gaps; Mermaid class diagram | stated = Clause 3 / Figure 1; inferred = headings |
| `design-notes.md` | adopt / adapt / reject against ARCH-0001, R-036, R-040–R-044, DEC-009; open questions | — |

**Not produced, with reason:** `state-machine.yaml` — the vulnerability lifecycle is shared with
ISO/IEC 30111 and is held once, in `records/iso/iso-iec-30111-2019/distilled/state-machine.yaml`
(`also_covers: iso-iec-29147-2018`). `schema/` — no schema can be derived without inventing field
types; the 16 advisory elements are listed in `messages.yaml`, and OASIS CSAF 2.x is the existing
JSON Schema to adopt. `examples/` — Annex C (example advisories) and Annex A (example policies) are
not in the preview.

## Verification

`verification.md` — independent verify-only pass (paywalled source: provenance, coverage honesty, no unofficial copies), 2026-10-02: method, counts, every defect found and how it was fixed, residual issues.
