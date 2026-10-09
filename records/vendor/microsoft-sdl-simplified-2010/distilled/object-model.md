---
schema: "library-object-model-view/v1"
id: microsoft-sdl-simplified-2010-object-model
record: microsoft-sdl-simplified-2010
type: diagram
updated: "2026-10-02"
---

# Simplified SDL (2010) — object model

Source of truth `object-model.yaml` (24 objects, 9 edges).

```mermaid
classDiagram
  class Organization
  class MaturityLevel { Basic; Standardized; Advanced; Dynamic }
  class CapabilityArea { 5 areas }
  class Project { subject_to_sdl }
  class Phase
  class Practice { 1..16 mandatory; optional }
  class SecurityAdvisor { Auditor; Expert }
  class Champion
  class QualityGate { per phase }
  class BugBar
  class RiskAssessment { SRA; PRA; P1-P3 }
  class ThreatModel
  class FinalSecurityReview { Passed; with exceptions; escalation }
  class ReleaseArchive
  class ComplianceTrackingApplication
  class ProcessAttestation
  Organization --> MaturityLevel : per CapabilityArea
  Practice --> Phase
  SecurityAdvisor --> QualityGate : approves
  SecurityAdvisor --> Practice : attests completion
  RiskAssessment --> ThreatModel : scopes
  FinalSecurityReview --> ThreatModel : examines
  SecurityAdvisor --> ReleaseArchive : certifies release
  ComplianceTrackingApplication o-- ProcessAttestation
  Champion --> ComplianceTrackingApplication : enters data
```

**Findings.** Per-phase quality gates approved by an independent advisor
(Practice 3), an advisor who "attest[s] to successful completion of each
security requirement", and a central compliance-tracking application holding
process attestations are the 2010 precursors of R-041 Gates, R-042
conformance and R-043 "KG as source of truth".
