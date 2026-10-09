---
schema: "library-distilled/v1"
id: esf-sscs-developers-2022-object-model
record: esf-sscs-developers-2022
type: object-model
updated: "2026-10-02"
reviewed_by: ""
---

# ESF developer guide — object model

Machine form: `object-model.yaml` (27 objects, 22 edges, 6 gaps; all stated with locators).
The guide's spine is **ThreatScenario → mitigated_by → RecommendedMitigation → applies_in →
LifecycleArea**, with mitigations aligned to **SSDF tasks** (Table 1, Appendix A) and evidenced by
**Artifacts** that a **ChecklistItem** asks for (Appendix D).

```mermaid
classDiagram
    class Role {
      developer|supplier|customer
    }
    class LifecycleArea {
      2.1 criteria & mgmt
      2.2 develop secure code
      2.3 verify third-party
      2.4 harden build
      2.5 deliver code
    }
    class ThreatScenario
    class InsiderThreatCase
    class AttackStep
    class InjectionPoint
    class RecommendedMitigation {
      advanced?
    }
    class SSDFTask
    class ThreatModel {
      reviewers >= 2
      refresh: change|major release|annual
    }
    class ReleaseCriteria
    class Product
    class ThirdPartyComponent
    class BuildEnvironment
    class SigningServer
    class Artifact
    class AvailabilityClass
    class ChecklistItem {
      Yes|No|NA|Inc
    }
    ThreatScenario --> LifecycleArea : occurs_in
    ThreatScenario "1" --> "*" RecommendedMitigation : mitigated_by
    RecommendedMitigation --> LifecycleArea : applies_in
    RecommendedMitigation --> SSDFTask : aligns_with (Table 1, App. A)
    InsiderThreatCase --|> ThreatScenario : specialises
    AttackStep --> AttackStep : precedes
    AttackStep --> InjectionPoint : targets
    RecommendedMitigation --> BuildEnvironment : protects
    ThreatModel --> Product : models
    Product --> ReleaseCriteria : evaluated_against
    Product --> ThirdPartyComponent : incorporates
    Product --> SigningServer : signed_by
    Artifact --> AvailabilityClass : has_availability
    ChecklistItem --> Artifact : evidenced_by
    ChecklistItem --> SSDFTask : maps_to
    Role --> Role : liaises
```

| ESF object | tmodel (ARCH-0001 / DL-0009) |
|---|---|
| ThreatScenario / InsiderThreatCase | `ThreatInstance` / `AttackPattern`, `applies_in_phase` (§1, §3b); insider = `ThreatActor` facet of a `Party` |
| AttackStep (4-step build-chain exploit) | `AttackStep` + `precedes` (§2a) |
| RecommendedMitigation | `Mitigation` → `MitigationInstance` with `kind` technical/documentation/process (R-040) |
| LifecycleArea | `LifecyclePhase` (§3b) — the guide adds a *build* phase |
| ReleaseCriteria | SDL release `Gate` exit criteria (R-041/R-042) |
| ThreatModel (governance rules) | governed view + `Review` quorum (R-043) |
| Artifact / AvailabilityClass / ChecklistItem | `Evidence` with visibility; conformance verdict (R-042) |
| SSDFTask | crosswalk target (R-044) |
