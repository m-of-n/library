---
schema: "library-object-model-view/v1"
id: owasp-samm-2-object-model
record: owasp-samm-2
type: diagram
updated: "2026-10-02"
---

# OWASP SAMM v2.2.0 — object model

`object-model.yaml` is the source of truth (19 objects, 22 edges, every one with
a locator). SAMM is the one SDL source here whose object model is **explicit in
its data**: each YAML file declares `type:` and links others by GUID. Solid
classes are stated in the core model; the assessment classes come from the
release's toolbox spreadsheet; `Evidence` is the gap.

```mermaid
classDiagram
  class BusinessFunction { id; name; order }
  class SecurityPractice { id; shortName; name }
  class Stream { id; letter A|B; name }
  class MaturityLevel { number 1..3 }
  class PracticeLevel { objective }
  class Activity { id; title; benefit; longDescription; personnel }
  class Question { text }
  class QualityCriterion { text }
  class AnswerSet
  class AnswerOption { text; value 0|.25|.5|1 }
  class Assessment { scope; date; team }
  class Answer { option; notes }
  class Score { level; practice 0..3; function; overall }
  class Roadmap { phases; targets }
  class Mapping { framework; target; relationship }
  class Evidence { <<absent in SAMM>> }
  BusinessFunction "1" o-- "3" SecurityPractice
  SecurityPractice "1" o-- "2" Stream
  SecurityPractice "1" o-- "3" PracticeLevel
  PracticeLevel "*" --> "1" MaturityLevel
  Stream "1" o-- "3" Activity
  Activity "*" --> "1" PracticeLevel : level
  Activity "*" --> "*" Activity : relatedActivities
  Question "1" --> "1" Activity : measures
  Question "1" o-- "*" QualityCriterion
  Question "*" --> "1" AnswerSet
  AnswerSet "1" o-- "4" AnswerOption
  Assessment "1" o-- "*" Answer
  Answer "*" --> "1" Question
  Answer "*" --> "1" AnswerOption
  Score ..> Answer : computed_from
  Roadmap "*" --> "*" SecurityPractice : target score
  Stream "*" --> "*" Mapping : maps_to
  Evidence ..> QualityCriterion : (tmodel needs; SAMM lacks)
```

**Findings for tmodel.** (1) The `Stream` is the unit SAMM's own crosswalk maps
at, so it is the right anchor for R-044 `maps_to`. (2) `QualityCriterion` is the
nearest thing to an evidence rule, but nothing links it to an artifact.
(3) Levels are scored by **sum**, not gated (see `state-machine.yaml`), so a
SAMM level is a score band, not a lifecycle state. (4) `Roadmap` phases with
target scores are the closest SAMM object to a dated gate; they carry no owner,
approval or dates.
