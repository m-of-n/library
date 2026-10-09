---
schema: "library-object-model-view/v1"
id: microsoft-sdl-object-model
record: microsoft-sdl
type: diagram
updated: "2026-10-02"
---

# Microsoft SDL (web practice set) — object model

Source of truth `object-model.yaml` (33 objects, 18 edges). The threat-modeling
core (practice 3) lines up almost one-to-one with tmodel's §1 layers; the
governance objects (bug bar, exception) feed R-041/R-042; there is **no gate**.

```mermaid
classDiagram
  class Practice { 1..10 }
  class SubPractice { n.m }
  class LifecycleStage { Design; Code; Build and Deploy; Run; Zero Trust }
  class BugBar { severity thresholds; fix time frame }
  class WorkItem { security label; severity }
  class SecurityException { reason; remediation plan; expiry; status }
  class ManagementApprover
  class ThreatModel
  class UseCase
  class Asset { tangible|intangible }
  class DataFlowDiagram
  class TrustBoundary
  class Threat { actor; preconditions; action; consequences; STRIDE }
  class SecurityAssumption
  class Mitigation
  class SecurityTest { SAST|DAST|pentest|red team|bug bounty }
  class SBOM
  class Attestation
  class Gate { <<absent>> }
  Practice o-- SubPractice
  SubPractice ..> SubPractice : see Practice x.y
  WorkItem --> BugBar : classified_by
  SecurityException --> ManagementApprover : approved_by
  ThreatModel o-- UseCase
  ThreatModel o-- Asset
  ThreatModel o-- DataFlowDiagram
  DataFlowDiagram --> TrustBoundary : depicts
  ThreatModel o-- Threat
  ThreatModel o-- SecurityAssumption
  Threat --> Asset : threatens
  Threat --> Mitigation : mitigated_by
  Threat --> WorkItem : tracked_as
  Mitigation --> WorkItem : tracked_as
  Mitigation --> SecurityTest : verified_by
  SBOM --> Attestation : signed
```
