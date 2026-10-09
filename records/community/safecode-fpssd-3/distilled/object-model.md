---
schema: "library-object-model-view/v1"
id: safecode-fpssd-3-object-model
record: safecode-fpssd-3
type: diagram
updated: "2026-10-02"
---

# SAFECode FPSSD 3rd ed. — object model

Source of truth `object-model.yaml` (25 objects, 14 edges).

```mermaid
classDiagram
  class ComplianceDriver
  class ApplicationSecurityControl { requirement; status }
  class ADLMSystem
  class Tool { SAST|DAST|fuzzer|scanner }
  class Artifact
  class SecurityFinding { severity; status }
  class SeverityScale
  class RiskAcceptance { T S R V; expiry; approver }
  class Approver
  class SecurityConfigurationGuide
  class ThirdPartyComponent
  class Vulnerability
  class PSIRT
  class Reporter
  class Workaround
  class SecurityAdvisory { affected; severity; CVE; fix; credit }
  ComplianceDriver --> ApplicationSecurityControl : drives
  ApplicationSecurityControl --> Artifact : validated_by
  ApplicationSecurityControl --> ADLMSystem : tracked_in
  Tool --> Artifact : produces
  Artifact --> SecurityFinding : contains
  SecurityFinding --> SeverityScale : rated_by
  SecurityFinding --> RiskAcceptance : accepted_via
  RiskAcceptance --> Approver : approved_by
  RiskAcceptance --> SecurityConfigurationGuide : may require
  ThirdPartyComponent --> Vulnerability : inherits
  Reporter --> PSIRT : reports
  Workaround --> Vulnerability : mitigates
  SecurityAdvisory --> Vulnerability : discloses
```

**Findings.** (1) "manage the controls as structured data in an ADLM system
rather than in an unstructured document" is the clearest industry statement of
R-043 (KG as SoT, documents as views). (2) TSRV (Technique, Specifics,
Remaining risk, Verification) is a ready-made field set for an accepted-risk
MitigationInstance. (3) No gate object — release is mentioned only as the
deadline for risk approval.
