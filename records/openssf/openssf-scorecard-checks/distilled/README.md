---
schema: "library-doc/v1"
id: openssf-scorecard-checks-distilled-index
record: openssf-scorecard-checks
type: index
updated: "2026-10-02"
---

# Distilled artifacts — OpenSSF Scorecard v5.5.0

Secondary reference (status `summarized`): requirements + object model only, per the lane brief.

| kind | file | coverage |
|---|---|---|
| requirements | `requirements.yaml` | all 20 checks + all 48 probes of v5.5.0, verbatim from `checks.yaml` / `probes/*/def.yml`; check→probe wiring from `probes/entries.go`; phase/nature/actor/deliverables are inferred typing |
| diagram | `object-model.yaml` | object-model pass: 32 objects, 29 edges, 5 gaps with locators |
| diagram | `object-model.md` | Mermaid class diagram + findings |
| verification | `verification.md` | FX-1 pass 2 (verify) — secondary reference, verify only, 2026-10-02: checks, scripts, counts, defects fixed, residual issues |

Not produced (secondary): normative.md, schema/, messages.yaml, protocol, state machine, examples, design notes.
Generator: `scorecard_req.py` (lane E scratchpad), re-runnable over the cached v5.5.0 files.
