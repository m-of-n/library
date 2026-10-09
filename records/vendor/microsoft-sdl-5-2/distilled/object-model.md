---
schema: "library-object-model-view/v1"
id: microsoft-sdl-5-2-object-model
record: microsoft-sdl-5-2
type: diagram
updated: "2026-10-02"
---

# Microsoft SDL 5.2 — object model

Source of truth `object-model.yaml` (29 objects, 17 edges). SDL 5.2 is the
richest Microsoft source for R-041: it has a named gate (FSR) with entry
milestones, an approver role, outcomes, exceptions and carry-over to the next
release.

```mermaid
classDiagram
  class Project { subject_to_sdl; variant }
  class Phase { Training..Response }
  class Requirement
  class Recommendation
  class SecurityAdvisor
  class PrivacyAdvisor
  class BugBar { Critical|Important|Moderate|Low }
  class SecurityWorkItem { effect STRIDE; cause; severity }
  class SecurityRiskAssessment
  class PrivacyImpactRating { P1|P2|P3 }
  class ThreatModel
  class SecurityMilestone
  class FinalSecurityReview { due; outcome; score }
  class FSROutcome { Passed; Passed with exceptions; Escalation }
  class Exception
  class Release { RTM|RTW }
  class AgileCategory { every-sprint|bucket|one-time }
  Project --> SecurityAdvisor : assigned
  Project --> PrivacyImpactRating
  Requirement --> Phase : in_phase
  Recommendation --> Phase
  SecurityAdvisor --> BugBar : approves
  SecurityWorkItem --> BugBar : ranked_by
  SecurityRiskAssessment --> ThreatModel : scopes
  ThreatModel --> SecurityWorkItem : one per vulnerability
  FinalSecurityReview --> SecurityMilestone : requires
  FinalSecurityReview --> ThreatModel : reviews
  FinalSecurityReview --> FSROutcome
  SecurityAdvisor --> Exception : grants
  Exception --> Release : carried to next
  FinalSecurityReview --> Release : gates
  Requirement --> AgileCategory
```

**Findings.** (1) The FSR is a complete Gate: entry guard (milestones done,
information delivered), reviewer (security advisor), checks (threat models
reviewed for mitigation of all known threats; deferred bugs against the bug bar;
tool results), outcomes, waiver path, and post-gate debt. (2) "Create an
individual work item for each vulnerability listed in the threat model" is the
threat→mitigation→verification link tmodel automates. (3) The undefined
"security score of B" is a gap.
