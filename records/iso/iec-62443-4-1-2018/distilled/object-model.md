---
schema: "library-distilled/v1"
id: iec-62443-4-1-2018-object-model
record: iec-62443-4-1-2018
type: diagram
updated: "2026-10-02"
---

# IEC 62443-4-1:2018 — object model (what the standard assumes)

Object-model pass over the free material only (IEC preview + iTeh sample terms + the requirement text
reproduced in ISASecure SDLA-312 v6.3; SDLA-300 for certification). 54 objects, 38 edges, 10 gaps — full
list with locators in `object-model.yaml`. Anything resting on the unread Clause 4 (maturity model) is
`kind: inferred`.

The single most useful finding: **SR-2's threat-model characteristics a)–m) are a DFD schema**
(information flow with classification, trust boundaries, processes, data stores, external entities,
protocols, physical/debug ports, attack vectors, threats with CVSS severity, mitigations/dispositions,
external dependencies). A 62443-4-1 conformant threat model is therefore a tmodel instance, and SR-2 k)
("mitigations and/or dispositions for each threat") is the R-042 "every threat has an approved
mitigation" check — with a *disposition* escape hatch tmodel does not yet model.

```mermaid
classDiagram
  direction LR
  class ProductSupplier
  class DevelopmentOrganization
  class SDLProcess{version; scope}
  class Practice{SM|SR|SD|SI|SVV|DM|SUM|SG}
  class Requirement{SM-1..SG-7}
  class MaturityLevel{ML1..ML4 (inferred)}
  class Product{version; SL-C}
  class Component
  class ExternallyProvidedComponent
  class ThreatModel{scope; last_reviewed}
  class Threat{severity CVSS}
  class MitigationOrDisposition
  class SecurityRequirement{SL-C}
  class SecureDesign
  class Interface{ext_accessible; crosses_TB}
  class TrustBoundary
  class DefenseInDepthLayer
  class Review
  class SecurityTest{type; independence}
  class SecurityRelatedIssue{severity; disposition}
  class ResidualRiskThreshold
  class SecurityAdvisory
  class SecurityUpdate
  class UserDocumentation{SG-1..SG-6}
  class Release
  class SDLACertification{12m|36m}

  ProductSupplier --> Product : develops
  DevelopmentOrganization --> SDLProcess : employs
  SDLProcess --> Product : applies_to (SM-3)
  Practice "1" --> "*" Requirement : groups
  Practice --> MaturityLevel : rated_at
  Product --> Component : composed_of
  Product --> ExternallyProvidedComponent : uses (SM-9)
  Product --> ThreatModel : has (SR-2)
  ThreatModel --> TrustBoundary : contains
  ThreatModel --> Threat : contains
  Threat --> MitigationOrDisposition : mitigated_or_disposed_by (SR-2 k)
  SecurityRequirement --> ThreatModel : aligned_with (SR-5)
  SecureDesign --> Interface : characterises (SD-1)
  Interface --> TrustBoundary : crosses
  SecureDesign --> Threat : mitigates (SD-1 j)
  DefenseInDepthLayer --> ThreatModel : based_on (SD-2)
  Review --> SecurityRelatedIssue : raises
  SecurityTest --> SecurityRequirement : verifies (SVV-1)
  SecurityTest --> MitigationOrDisposition : verifies (SVV-2)
  SecurityRelatedIssue --> Product : affects (DM-3 c)
  SecurityRelatedIssue --> ResidualRiskThreshold : judged_against (DM-4)
  SecurityRelatedIssue --> SecurityAdvisory : disclosed_in (DM-5)
  SecurityRelatedIssue --> SecurityUpdate : resolved_by
  UserDocumentation --> DefenseInDepthLayer : documents
  Release --> SecurityRelatedIssue : gated_by closed (SM-11)
  SDLACertification --> DevelopmentOrganization : certifies
```

## Gaps against tmodel (summary — see `object-model.yaml` `gaps`)

1. Graded conformance (ML1–ML4 per practice) — R-042 is pass/fail today.
2. Two requirement kinds: SDL process requirement vs product security requirement (SR-3/SR-4, SL-C).
3. Threat *disposition* (defer with reason/risk; accept below residual-risk threshold) beside mitigation.
4. Interface object with SD-1's attribute set; hardware/debug-port attack surface.
5. Tester-independence level on evidence; SM-5 tailoring justification; issue lifecycle; update objects;
   external certification as an attestation distinct from an internal Review.
