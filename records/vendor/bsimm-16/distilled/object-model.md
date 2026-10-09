---
schema: "library-object-model-view/v1"
id: bsimm-16-object-model
record: bsimm-16
type: diagram
updated: "2026-10-02"
---

# BSIMM16 — object model

Source of truth: `object-model.yaml` (29 objects, 20 edges, each with locator;
`Score` and the absent `Evidence` edge are inferred).

```mermaid
classDiagram
  class SoftwareSecurityFramework
  class Domain { Governance; Intelligence; SSDL Touchpoints; Deployment }
  class Practice { code; name }
  class Activity { label e.g. SM1.4; title; level 1..3 }
  class Capability
  class Edition { BSIMMn; activity_count; pool }
  class Participant { firm; verticals }
  class SSI { state emerging|maturing|enabling }
  class SSG
  class Champion
  class SSDL
  class Checkpoint { gate|guardrail|milestone }
  class ReleaseCondition
  class Exception
  class SignOff { risk_owner; criteria }
  class Scorecard
  class Observation { firms/111; % }
  class Mapping { ssdf_task; bsimm12; bsimm16 }
  SoftwareSecurityFramework o-- "4" Domain
  Domain o-- "3" Practice
  Practice o-- "*" Activity
  Activity --> Activity : relabelled_as (Table 9)
  Activity --> Activity : see [XX]
  Capability o-- "*" Activity
  Edition o-- "*" Activity
  Participant --> SSI : runs
  SSI --> SSG : staffed_by
  SSG --> Champion : leverages
  SSG --> Activity : carries_out
  SSI --> SSDL
  SSDL o-- "*" Checkpoint
  Checkpoint o-- "*" ReleaseCondition
  ReleaseCondition --> Exception : excepted_by
  SignOff ..> Checkpoint : release sign-off
  Participant o-- Scorecard
  Scorecard o-- "128" Observation
  Observation --> Activity
  Activity --> Mapping : maps_to SSDF
```

**Findings for tmodel.** (1) BSIMM's `Checkpoint` (explicitly "gates, release
conditions, guardrails, milestones") + `ReleaseCondition` + tracked `Exception`
+ `SignOff` by a risk owner is the most concrete published description of the
R-041 Gate among the maturity models — but it lives in prose of three activities
(SM1.4, SM1.7, SM2.6), not as data. (2) Activity labels are edition-scoped and
relabelled when levels change, so crosswalk ids need edition qualification.
(3) The SSI state (emerging → maturing → enabling) is the program-level state;
activity levels are not states.
