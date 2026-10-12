---
record: sp-800-218
kind: diagram
title: "sp-800-218 — object model (SSDF 1.1)"
extracted: "2026-10-02"
reviewed_by: ""
---

# SSDF 1.1 — object model

Object-model pass: the source was re-read for one question — *what entity types and edges does
the SSDF assume or define?* The machine form is `object-model.yaml` (82 objects, 82 edges, 9 gaps;
1 inferred object and 2 inferred edges). Each object and edge has a locator. This page shows the
backbone in three diagrams.

## 1. Framework layer: how the SSDF is built

```mermaid
classDiagram
  class Framework {
    version = 1.1
  }
  class PracticeGroup {
    id PO/PS/PW/RV
    outcome_statement
  }
  class Practice {
    id e.g. PO.1
    name
    explanation
    status
  }
  class Task {
    id e.g. PO.1.1
    text
    formerly
    status
  }
  class NotionalImplementationExample {
    task_id
    n
    text - optional
  }
  class InformativeReference {
    scheme_key
    identifiers
  }
  class ReferenceDocument {
    key
    title
    version
  }
  class ExternalClause {
    EO 14028 4e subsection
  }
  class Term {
    adopter-defined
  }
  Framework "1" --> "4" PracticeGroup : contains
  PracticeGroup "1" --> "*" Practice : groups
  Practice "1" --> "*" Task : has_task
  Task "1" --> "*" NotionalImplementationExample : illustrated_by
  Task "*" --> "*" InformativeReference : maps_to
  InformativeReference "*" --> "1" ReferenceDocument : cites
  Task "*" --> "*" ExternalClause : helps_address
  Task "*" --> "*" Task : retired_into
  Framework ..> Term : leaves undefined (§2)
```

## 2. Producer side: governance, toolchain, environment, evidence, gates

```mermaid
classDiagram
  class Organization
  class Role
  class Personnel
  class SecurityLeadership
  class SecurityRequirement {
    scope infra/software
    source internal/external
  }
  class Policy
  class RequirementException
  class Toolchain
  class Tool
  class Artifact {
    a piece of evidence
  }
  class SecurityCheckCriteria {
    KPI KRI severity DoD
  }
  class SecurityCheck {
    approved/rejected/exception
  }
  class Gate {
    key point in SDLC
  }
  class DevelopmentEnvironment
  class SDLC
  class ConformanceRecord {
    inferred
  }
  Organization --> Role
  Personnel --> Role : plays
  SecurityLeadership --> SoftwareRelease : accountable_for_release
  SecurityRequirement --> Policy : derived_from_source
  RequirementException --> SecurityRequirement : excepts
  Toolchain --> Tool : includes_tool
  Toolchain --> DevelopmentEnvironment : runs_in (inferred)
  Tool --> Artifact : generates
  Artifact --> Task : evidences
  SecurityCheck --> SecurityCheckCriteria : evaluated_against
  SecurityCheck --> Artifact : inspects
  Gate --> SDLC : placed_at
  Gate --> SecurityRequirement : verifies_flaw_class
  DevelopmentEnvironment --> DevelopmentEnvironment : separated_from / trusts
  ConformanceRecord --> Task : conforms_to
  RootCause --> SDLC : improves
```

## 3. Product side: software, design, verification, release, response

```mermaid
classDiagram
  class Software
  class SoftwareComponent
  class ThirdPartySupplier
  class SoftwareDesign
  class RiskModel {
    threat_model/attack_model/attack_surface_map
  }
  class Risk
  class RiskResponse {
    mitigate/accept/transfer/temporary
  }
  class DesignReview {
    qualified, independent, or automated
  }
  class Code
  class Issue
  class SoftwareRelease
  class IntegrityVerificationInformation
  class ProvenanceData
  class SBOM
  class Vulnerability
  class RootCause
  class Remediation
  class SecurityAdvisory
  Software "*" --> "*" SoftwareComponent : composed_of
  SoftwareComponent --> ThirdPartySupplier : supplied_by
  RiskModel --> Software : assesses
  RiskModel --> Risk : identifies
  SoftwareDesign --> Risk : mitigates
  RiskResponse --> Risk : responds_to
  RiskResponse --> SecurityRequirement : becomes_requirement
  DesignReview --> SoftwareDesign : reviews
  DesignReview --> RiskModel : reviews_model
  CodeReview --> Issue : produces_issue
  SecurityTest --> Issue : produces_issue
  SoftwareRelease --> Software : release_of
  SoftwareRelease --> IntegrityVerificationInformation : accompanied_by
  SoftwareRelease --> ProvenanceData : has_provenance
  ProvenanceData ..> SBOM : e.g.
  Vulnerability --> SoftwareRelease : affects
  Vulnerability --> RootCause : caused_by
  RootCause --> Task : traced_to_practice
  Remediation "*" --> "*" Vulnerability : remediates
  SecurityAdvisory --> Vulnerability : announces
```

## Findings

1. **The SSDF has two requirement tiers.** The first is the framework *Task* (what the SDL must
   do). The second is the product *SecurityRequirement* (PO.1.2, PW.1.2: what the software must
   meet). A conformance engine (R-042) needs both. A Task such as PW.2.1 is satisfied by a
   DesignReview, made by an independent reviewer, which shows that every product
   SecurityRequirement and identified Risk was addressed.
2. **The threat model enters at PW.1.1 and is approved at PW.2.1.** The independent reviewer
   reviews both the design and the risk model (PW.2.1/E2). This is the R-043 "governed view with
   approval" pattern, stated by the source.
3. **There is a feedback loop that tmodel does not have.** A Vulnerability has a RootCause
   (RV.3.1). That RootCause can be a Task not followed (RV.3.2), and it leads to an SDLC update
   (RV.3.4). Separately, a RiskResponse becomes a SecurityRequirement (PW.1.2/E1).
4. **The SSDF names gates but does not order them.** PO.1.2/E2 is the only place gates appear,
   and §2 denies any implied sequence. The criteria (PO.4.1) and recorded check outcomes
   (PO.4.1/E5) are rich, so they map well onto Gate exit criteria. The gate order has to come
   from somewhere else.
5. **Responsibility can be split across Parties per Task.** Under the §1 shared-responsibility
   agreement, providers attest to their part. This needs a Party→Requirement edge that tmodel
   lacks.
