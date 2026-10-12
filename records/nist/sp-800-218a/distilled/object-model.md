---
schema: "library-object-model-view/v1"
id: sp-800-218a-object-model
record: sp-800-218a
type: diagram
kind: diagram
title: "sp-800-218a — object model (entities and edges)"
extracted: "2026-10-02"
updated: "2026-10-02"
generated_from: distilled/object-model.yaml
reviewed_by: ""
---

# SP 800-218A object model

The authoritative version is `object-model.yaml`: 62 objects (61 stated, 1 inferred) and
52 edges (50 stated, 2 inferred), each with a locator. This page is a reading aid. The
diagram shows the main structure, not every edge.

The source assumes three layers.

1. **The framework layer.** CommunityProfile → PracticeGroup → Practice → Task → R/C/N
   ProfileAddition, plus InformativeReference. Priority and ProfileStatus hang on the
   (Profile, Task) membership, not on the task.
2. **The AI artifact layer.** These are new compared with SSDF 1.1: AIModel and its
   separately protected parts (ModelWeights, ConfigurationParameters, RewardModel,
   AdaptationLayer), Dataset by purpose, AdversarialSample, ModelInputOutput,
   TrainingPipeline and ModelRegistry inside a DevelopmentEnvironment.
3. **The party layer.** AI model producer, AI system producer, AI system acquirer and
   user, joined by a SharedResponsibilityAgreement that assigns tasks and attestation.

```mermaid
classDiagram
  direction LR
  class CommunityProfile { use_case; base = SSDF 1.1 }
  class PracticeGroup { PO PS PW RV }
  class Practice { id; title; profile_status }
  class Task { id; text; priority; profile_status }
  class ProfileAddition { id = task.R|C|N n; kind; text }
  class InformativeReference { scheme AI RMF|OWASP|Adv ML; ids }
  CommunityProfile --> Practice : augments
  Practice --> PracticeGroup : part_of
  Task --> Practice : part_of
  ProfileAddition --> Task : annotates
  Task --> InformativeReference : maps_to
  Task --> Task : modifies (SSDF 1.1)

  class Organization
  class AIModelProducer
  class AISystemProducer
  class AISystemAcquirer
  class SharedResponsibilityAgreement { task assignments; attestation method }
  class Attestation
  Organization --> AIModelProducer : plays_role
  Organization --> Task : responsible_for
  SharedResponsibilityAgreement --> Task : specifies
  Attestation --> SharedResponsibilityAgreement : attests_conformance

  class AIModel { version; closed/open; trained_on_sensitive_data }
  class ModelWeights { hash; signature }
  class ConfigurationParameters
  class RewardModel
  class Dataset { purpose train|test|fine-tune|align; provenance_known }
  class ProvenanceData { known; SBOM|SLSA }
  class AISystem
  AIModelProducer --> AIModel : produces
  AISystemProducer --> AIModel : integrates
  AISystem --> AIModel : composed_of
  AISystemAcquirer --> AISystem : acquires
  AIModel --> ModelWeights : parameterized_by
  AIModel --> ConfigurationParameters : configured_by
  AIModel --> Dataset : trained_on
  AIModel --> AIModel : derived_from
  Dataset --> ProvenanceData : has_provenance 0..1
  AIModel --> ProvenanceData : has_provenance

  class DevelopmentEnvironment { dev|AI training|build|test|distribution }
  class TrainingPipeline
  class ModelRegistry
  TrainingPipeline --> DevelopmentEnvironment : hosted_in
  AIModel --> ModelRegistry : stored_in
  ModelWeights --> TrainingPipeline : generated_by (inferred)

  class RiskModel
  class AIThreatType
  class DesignReview { human AND automated }
  class HumanInTheLoop
  class SecurityCheckCriteria
  RiskModel --> AIThreatType : considers_threat
  DesignReview --> RiskModel : reviews
  HumanInTheLoop --> SecurityCheckCriteria : approves

  class Vulnerability
  class RiskResponse { remediate|stop-use|roll-back }
  class RootCause
  Vulnerability --> AIModel : affects
  RiskResponse --> Vulnerability : responds_to
  Vulnerability --> RootCause : caused_by
```

## What the pass found

- **A threat model is SSDF work product PW.1.1.** 218A requires AI threat types in it
  (PW.1.1.R1 names seven) and asks for re-modelling for future versions and derivatives
  (PW.1.1.C1). This is the direct conformance hook for tmodel (R-042).
- **Responsibility is distributed.** The SharedResponsibilityAgreement (§2) is the only
  structure in the SSDF family that assigns tasks to *different* organizations. tmodel
  has no Party→Requirement responsibility edge.
- **Profile membership carries attributes.** Priority and ProfileStatus belong to the
  pair (Profile, Task). A Requirement node alone cannot hold them; an overlay edge can.
- **Provenance can be explicitly unknown.** PW.3.2 asks the organization to document
  which data do *not* have known provenance. The absence of an edge has to be
  representable, which is a gap in an open-world graph.
- **The model is both code and data.** AIModel, ModelWeights and Dataset get code-style
  protection (PS.1), and the provenance runs back through TrainingPipeline. The
  boundary that tmodel's §0 one-artifact rule assumes is blurred here (§1 says so
  explicitly).

The full gap list is in `object-model.yaml`.
