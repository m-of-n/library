---
schema: "library-object-model-view/v1"
id: owasp-dsomm-object-model
record: owasp-dsomm
type: diagram
updated: "2026-10-02"
---

# OWASP DSOMM (data v5.1.0) — object model

Source of truth `object-model.yaml` (11 objects, 8 edges).

```mermaid
classDiagram
  class Dimension
  class SubDimension
  class Activity { uuid; risk; measure; assessment; level 1..5; usefulness }
  class Difficulty { knowledge; time; resources }
  class Implementation { tool/method; url }
  class Reference { samm2; iso27001; openCRE; d3f }
  class Team
  class TeamImplementation
  class TeamEvidence
  Dimension o-- SubDimension
  SubDimension o-- Activity
  Activity --> Activity : dependsOn
  Activity --> Difficulty
  Activity --> Implementation : implemented_by
  Activity --> Reference : maps_to
  Activity --> Team : teamsImplemented
  TeamImplementation --> TeamEvidence : teamsEvidence
```

**Findings.** Each DSOMM activity pairs a *risk* with a *measure* (a
threat→mitigation statement), carries an *assessment* ("Show …") and has
per-team implementation and evidence slots — the closest data model among the
maturity models to tmodel's MitigationInstance + Evidence + Review (R-040,
R-042). Every activity cites SAMM (278 of 280 references resolve to SAMM v2.2
ids; `crosswalk.yaml`).
