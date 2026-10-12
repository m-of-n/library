---
schema: "library-distilled/v1"
id: enisa-sbd-playbook-2026-object-model
record: enisa-sbd-playbook-2026
type: diagram
updated: "2026-10-02"
---

# ENISA SbD&D Playbook: object model

This is the object-model pass. `object-model.yaml` holds 39 objects and 19 edges, all of them stated, and 7 gaps.

```mermaid
classDiagram
  direction LR
  class Principle { id; group }
  class Playbook
  class ChecklistAction
  class MinimumEvidence
  class ReleaseGateCriterion { pass|fail|not affected }
  class ReleaseGate { go|no-go }
  class Exception { rationale; owner; expiry }
  class ThreatModel
  class ThreatScenario { priority H/M/L; owner }
  class TrustBoundary
  class Control { where_enforced; verification }
  class SecureDefault
  class Attestation { layers; signature }
  class Assessor
  Principle --> Playbook : realised_by
  Playbook --> ChecklistAction
  ChecklistAction --> MinimumEvidence : evidenced_by (N:M, reusable)
  Playbook --> ReleaseGateCriterion : gated_by
  ReleaseGateCriterion --> ReleaseGate : part_of
  ReleaseGateCriterion --> Exception : excepted_by
  ThreatModel --> ThreatScenario
  ThreatScenario --> TrustBoundary : crosses
  ThreatScenario --> Control : mitigated_by
  Control --> SecureDefault : sets_default
  Attestation --> Control : attests
  Attestation --> MinimumEvidence : links_evidence
  Assessor --> Attestation : verifies
```

## Findings

1. **Each playbook bundles Requirement, Evidence and Gate.** Every one of the 22 playbooks packages checklist actions (requirements), minimum evidence and pass/fail release-gate criteria. That bundle is a natural unit for an R-041 SecurityProgram module. Its 125 gate criteria are the largest explicit set of automatable gate checks among the SDL sources.
2. **Evidence is reusable across requirements.** "A single item of evidence may support several playbooks." So R-042 needs Evidence to relate many-to-many with Requirement.
3. **The attestation cascade is the R-042 chain made portable.** The control layer (objective) leads to the implementation layer (claim and settings), then to verification (gate result and evidence hash). That cascade is exactly the Requirement → MitigationInstance → Evidence → Review chain. It suggests the shape for exporting tmodel conformance as a signed attestation, with CycloneDX CDXA or OSCAL as candidate formats.
4. **Exceptions expire.** Exceptions and accepted residual risk carry an owner and an expiry date throughout. The DEC-009 "accepted" disposition should require an expiry.
5. **Refresh triggers invalidate the threat model.** Some events must re-run the threat model, such as a new interface, a new auth model or an OTA change. A governed threat-model view (R-043) therefore needs invalidation by event, not only versioning.
