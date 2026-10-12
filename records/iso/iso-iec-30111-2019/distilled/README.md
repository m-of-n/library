---
schema: "library-doc/v1"
id: iso-iec-30111-2019-distilled-index
record: iso-iec-30111-2019
type: index
updated: "2026-10-02"
---

# Distilled artifacts — ISO/IEC 30111:2019 (free preview only)

**Not an FX-1 extraction.** ISO/IEC 30111:2019 is paywalled. Everything here is drawn from the
distributor-sample (iTeh/SIST) **11-page free preview** (Contents, Foreword, Introduction, Clauses 1–6.5.3.4
incl. Figure 1). Clauses 6.5.4–8 (incl. the phase-by-phase handling process, Clause 7), Annex A
(summary of normative provisions) and the Bibliography are not available. Nothing is reviewed.

| file | what it is | coverage |
|---|---|---|
| `normative.md` | every visible shall/should/may verbatim, in clause order, with locator | Clauses 5.1–6.5.3.4 complete; 6.5.4–8 absent |
| `requirements.yaml` | `library-requirements/v2`; 32 entries: 2 shall, 26 should, 2 may, 2 inferred ("is responsible for") | all normative statements in the preview; counts reconciled against the preview |
| `state-machine.yaml` | lifecycle of one potential vulnerability: 10 states, 10 transitions, 1 guard, 2 side paths; shared with ISO/IEC 29147 | stated from Figure 1; phase names from Clause 7 / 29147 §5.6 headings; no deadlines visible |
| `object-model.yaml` / `object-model.md` | object-model pass: 18 objects, 19 edges, 5 gaps; Mermaid class diagram | Clause 6 organisation stated; Clause 7–8 inferred from headings |
| `design-notes.md` | adopt / adapt / reject against ARCH-0001, R-040–R-044, DEC-009 | — |

**Not produced, with reason:** `protocol.yaml` — 30111 is the vendor-internal process; the external
exchange is 29147's and is held in `records/iso/iso-iec-29147-2018/distilled/protocol.yaml` (which
includes 30111's lane of Figure 1). `messages.yaml` / `schema/` — 30111 defines no message or data
structure in the visible text. `examples/` — none in the preview.

## Verification

`verification.md` — independent verify-only pass (paywalled source: provenance, coverage honesty, no unofficial copies), 2026-10-02: method, counts, every defect found and how it was fixed, residual issues.
