---
schema: "library-distilled/v1"
id: sp-800-218r1-object-model
record: sp-800-218r1
kind: diagram
type: object-model
title: "sp-800-218r1 — object model (SSDF 1.2 IPD)"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# SSDF 1.2 (IPD) — object model

The source of truth is `object-model.yaml`: 86 objects and 104 edges, each with a locator. Three are inferred: two objects (CommunityProfile; ConformanceRecord, ported) and three edges (SoftwareUpdate `updates` SoftwareRelease; Toolchain `runs_in` DevelopmentEnvironment and ConformanceRecord `conforms_to` Task, both ported). The other objects and edges are stated. Objects new in 1.2 are flagged `new_in_1_2`. 32 objects and 48 edges were ported from the `sp-800-218` model by the verify pass (2026-10-02) after checking that every cited id carries the same concept in the 1.2 IPD. The diagram below shows the backbone of the lane-A model and leaves out the leaf objects and the ported ones.

```mermaid
classDiagram
  direction LR
  class Framework { version; status draft|final }
  class PracticeGroup { PO|PS|PW|RV }
  class Practice { id; name; description; status }
  class Task { id; text; formerly; moved_to }
  class NotionalImplementationExample { id; text (non-binding) }
  class InformativeReference { scheme; edition; ids }
  Framework "1" o-- "4" PracticeGroup
  PracticeGroup "1" o-- "*" Practice
  Practice "1" o-- "*" Task
  Task "1" o-- "*" NotionalImplementationExample : illustrates
  Task "*" --> "*" InformativeReference : maps_to
  Task --> Task : moved_to / formerly / cross_references

  class Organization
  class SoftwareProducer
  class SoftwareAcquirer
  class ThirdPartySupplier
  class PlatformServiceProvider
  class ResponsibilityAgreement
  Organization <|-- SoftwareProducer
  Organization <|-- SoftwareAcquirer
  Organization <|-- ThirdPartySupplier
  Organization <|-- PlatformServiceProvider
  Organization --> Framework : adopts
  Organization --> Task : performs / responsible_for
  PlatformServiceProvider --> ResponsibilityAgreement : attests_conformance

  class SecurityRequirement
  class Exception
  class SecurityCheckCriteria
  class Gate
  SecurityRequirement --> ThirdPartySupplier : communicated_to
  ThirdPartySupplier --> SecurityRequirement : attests
  Exception --> SecurityRequirement : excepts
  SecurityCheckCriteria --> Gate : enforced_at

  class Toolchain
  class Tool
  class Artifact
  class DevelopmentEnvironment
  class ImprovementPlan { NEW 1.2 PO.6 }
  Toolchain o-- Tool
  Tool --> Artifact : generates
  Artifact --> Task : evidences
  ImprovementPlan --> SDLCProcess : improves

  class Software
  class SoftwareComponent
  class SoftwareRelease
  class ProvenanceData
  class IntegrityVerificationInformation
  class SoftwareUpdate { NEW 1.2 PS.4 }
  class RollbackMechanism { NEW 1.2 PS.4.3 }
  class UpdateEngine { NEW 1.2 PS.4.4 }
  Software --> SoftwareComponent : uses_component
  SoftwareComponent --> ThirdPartySupplier : supplied_by
  SoftwareRelease --> ProvenanceData : has_provenance
  SoftwareRelease --> IntegrityVerificationInformation : verified_by
  SoftwareUpdate --> SoftwareRelease : updates (inferred)
  SoftwareUpdate --> UpdateEngine : delivered_by
  RollbackMechanism --> SoftwareRelease : reverts_to

  class RiskModel
  class DesignDecision
  RiskModel --> Software : assesses
  RiskModel --> SoftwareAcquirer : shared_with (NEW PW.1.1 Ex5)

  class Vulnerability
  class RootCause
  class RiskResponse
  class SDLCProcess
  Vulnerability --> SoftwareRelease : affects
  Vulnerability --> RiskResponse : responded_by
  Vulnerability --> RootCause : caused_by
  RootCause --> SDLCProcess : feeds_back_to
```

## Findings

1. **There are two kinds of requirement.** An SSDF *Task* is a process requirement on the producer, and this is what conformance is checked against. A producer's own *SecurityRequirement* (PO.1.1 and PO.1.2) is a product requirement on its software. In DL-0009 R-042 both are a single `Requirement`, so tmodel needs a `level` or `kind` field that separates them.
2. **Examples are not obligations.** §2 says "No examples or combination of examples are required". A NotionalImplementationExample is therefore a template for a MitigationInstance (R-040), not a conformance item.
3. **The table has no gate order.** §2, lines 311–313, says the order "is not intended to imply the sequence of implementation". The only gates are the ones PO.1.2 Ex 2 and PO.4 name. Ordered R-041 gates have to be laid over the SSDF by our own phase mapping.
4. **The new PS.4 practice adds an update lifecycle**: test, then staged or canary roll-out, then rollback to the last known good version, with anti-rollback protection. ARCH-0001 §3b has a maintenance/update phase but has no SoftwareUpdate event or rollback transition.
5. **Responsibility is split per task.** In shared-responsibility platforms, the agreement in §1 (lines 277–280) assigns each practice and task to a party, and each party attests to its share. That needs a `responsible_for` edge from Party to Requirement and an attestation Assertion.
