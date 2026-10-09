---
schema: "library-doc/v1"
id: openssf-osps-baseline-object-model
record: openssf-osps-baseline
type: diagram
updated: "2026-10-02"
reviewed_by: ""
---

# Object model — OSPS Baseline v2026.08.28

Machine source: `object-model.yaml` (45 objects, 48 edges; 2 objects and 7 edges are `inferred`; the verify pass of 2026-10-02 added VulnerabilityAdvisory and 9 edges that are not yet drawn in the diagrams below).
OSPS has two halves: a **catalog model** it states formally (Gemara Layer 2 CUE schema), and a
**domain model** it assumes through its lexicon and control text — source-control, CI/CD and
release objects that tmodel does not yet have.

## Catalog half (stated in schema)

```mermaid
classDiagram
  class ControlCatalog { id; version YYYY-MM-DD; gemara-version; draft }
  class ControlFamily { id AC|BR|DO|GV|LE|QA|SA|VM }
  class Control { id OSPS-XX-NN; title; objective; state }
  class AssessmentRequirement { id OSPS-XX-NN.MM; text MUST; recommendation; state }
  class MaturityLevel { maturity-1; maturity-2; maturity-3 }
  class MappingDocument { source osps-baseline; target framework }
  class Mapping { relationship relates-to; strength?; confidence? }
  class Guideline { entry-id }
  class ExternalFramework { CRA; SSDF; SLSA; SAMM; ... 14 }
  ControlCatalog "1" --> "*" Control : contains
  Control "*" --> "1" ControlFamily : member_of
  Control "1" --> "1..*" AssessmentRequirement : has_requirement
  AssessmentRequirement "*" --> "1..*" MaturityLevel : applies_at
  MappingDocument "1" --> "*" Mapping
  Mapping "*" --> "1" Control : source
  Mapping "*" --> "1..*" Guideline : targets
  Guideline "*" --> "1" ExternalFramework : part_of
  Control ..> Control : replaced_by
```

## Domain half (assumed by the controls)

```mermaid
graph LR
  Project -->|owns| Repository
  Project -->|has_subproject| Subproject
  Repository -->|hosted_on| VCS[VersionControlSystem]
  Repository -->|has_primary_branch| PrimaryBranch
  Change -->|applied_to| PrimaryBranch
  Change -->|authored_by / approved_by| Collaborator
  Change -->|gated_by| StatusCheck
  Change -->|asserts_right_to_commit| ContributorAssertion
  Collaborator -->|has_permission_on| SensitiveResource
  CICD[CICDPipeline] -->|accesses| SensitiveResource
  CICD -->|produces| Release
  Project -->|makes| Release
  Release -->|contains_asset| Asset[ReleasedSoftwareAsset]
  Asset -->|described_by_sbom| SBOM
  Release -->|distributed_via| DistributionChannel
  Project -->|depends_on| Dependency
  PolicyDocument -->|documents| Project
  SecurityAssessment -->|assesses| Project
  VulnerabilityReport -->|reported_to| SecurityContact
  Vulnerability -->|declared_not_affected_in| VEX[VEXDocument]
  Finding[SCA / SAST Finding] -->|blocks| Change
  Assessment -.->|evaluates| AR[AssessmentRequirement]
  Assessment -.->|claims_level| MaturityLevel
```

## Findings

1. **Two grains of requirement.** `Control` (objective, mapping grain) and `AssessmentRequirement`
   (testable MUST, evaluation grain). tmodel's `Requirement` (R-042/R-044) needs both levels and a
   `part_of` between them; crosswalks attach at the coarse grain, conformance checks at the fine one.
2. **Maturity level is a profile, not a gate.** Levels are defined by *who the project is*
   (maintainers, users), not by lifecycle phase. They should not be modelled as DL-0009 `Gate`s;
   they are a conformance *target* a `Product` claims.
3. **Requirements are event-condition rules.** Most ARs start "When …" or (in earlier releases)
   "While active, …": the condition is a model fact (`has_released`, `new collaborator added`)
   that decides applicability. tmodel needs an applicability condition on `Requirement`.
4. **The domain half is the development environment.** ~20 ARs are configuration facts about the
   VCS, the primary branch and the CI pipeline. tmodel has no source-control objects; SLSA's Source
   track assumes the same ones — a shared gap.
5. **Gemara supplies the crosswalk vocabulary R-044 lacks:** typed relationship
   (`implements`/`supports`/`equivalent`/`subsumes`/`relates-to`/`no-match`), strength 1–10,
   confidence-level. OSPS itself only uses `relates-to` with everything else unset.
