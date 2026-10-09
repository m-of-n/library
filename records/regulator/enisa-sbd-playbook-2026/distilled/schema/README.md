---
schema: "library-distilled/v1"
id: enisa-sbd-playbook-2026-schema
record: enisa-sbd-playbook-2026
type: schema
updated: "2026-10-02"
---

# Derived schemas

The source has no schema of its own. These JSON Schemas (draft 2020-12) were generated from `../messages.yaml` by `msg2schema.py` in the lane-F scratchpad. A field is in `required` only when the source governs it with a mandatory verb, and every property carries `x-constrained-by` pointing at its requirement ids.

- `MachineProcessableAttestation.derived.schema.json`
- `attestation-claim.derived.schema.json` — hand-derived from Figure 5's field names (ENISA: illustrative, not a schema); `../examples/safegate-x1-figure5.json` validates against it (python-jsonschema, 2026-10-02)
- `ReleaseSecurityReviewRecord.derived.schema.json`
- `ExceptionRecord.derived.schema.json`
- `RiskRegisterEntry.derived.schema.json`
- `ThreatModelScopeNote.derived.schema.json`
- `TopThreat.derived.schema.json`
- `VulnerabilityRegisterEntry.derived.schema.json`
- `SecurityLogEvent.derived.schema.json`
- `AccessModelRow.derived.schema.json`
- `LifecyclePolicy.derived.schema.json`
