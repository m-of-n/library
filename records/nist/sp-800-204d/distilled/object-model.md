---
schema: "library-object-model-doc/v1"
id: sp-800-204d-object-model
record: sp-800-204d
kind: diagram
type: object-model
title: "sp-800-204d — object model"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# SP 800-204D — object model

`object-model.yaml` is the machine form: 62 objects and 45 edges, each with a locator. One edge
(`maps_to_ssdf`) is inferred; the rest are stated. The document's own model is **Figure 1**: an SSC
is a chain of **Steps**. An **Actor**, human or not, *carries out* a Step. A Step *uses*
**Artifacts** and **Resources** and *produces* Artifacts. Everything else adds to that core.

```mermaid
classDiagram
    direction LR
    class Actor { identity; human_or_nonhuman; role }
    class SSCStep { activity_type; trust_level }
    class Artifact { digest; owner; kind; version }
    class Resource
    class Repository { kind: SCM|artifact mgr|build|package|registry }
    class CICDPipeline { CI|CD; automated }
    class Workflow
    class Stage
    class DriverTool { trust_level }
    class Tool { source_origin; trusted }
    class ExecutionEnvironment { isolated; hardened }
    class Role { authorizations }
    class Attestation { type; subject_digest; signature }
    class EnvironmentAttestation
    class ProcessAttestation
    class MaterialsAttestation
    class ArtifactsAttestation
    class VulnerabilityAttestation { scan_time }
    class AttestationStore { tamper_proof }
    class SigningKey { online; HSM }
    class Policy { signed; required_attestations; functionary_keys; build_horizon }
    class Verifier
    class Assurance
    class SBOM
    class Dependency { transitive_depth }
    class Release { module_versions; config }
    class Cluster { actual; specified; drift }
    class SSCAttack { compromise→propagation→exploitation }
    class SSDFPractice

    Actor --> SSCStep : carries_out
    SSCStep --> Artifact : uses
    SSCStep --> Artifact : produces
    Resource --> SSCStep : used_for
    Artifact --> Actor : owned_by
    Artifact --> Repository : stored_in / travels_through
    CICDPipeline --> Stage : has_stage
    CICDPipeline --> Workflow : uses_workflow
    Workflow --> Artifact : transforms
    DriverTool --> Tool : invokes
    DriverTool ..> SSCStep : higher_trust_than
    SSCStep --> ExecutionEnvironment : runs_in
    Actor --> Role : holds_role
    Role --> SSCStep : authorizes
    Attestation <|-- EnvironmentAttestation
    Attestation <|-- ProcessAttestation
    Attestation <|-- MaterialsAttestation
    Attestation <|-- ArtifactsAttestation
    Attestation <|-- VulnerabilityAttestation
    Attestation --> Artifact : attests
    Attestation --> SSCStep : describes_step
    Attestation --> SigningKey : signed_with
    Attestation --> AttestationStore : stored_in
    Policy --> Attestation : requires_attestation
    Policy --> SigningKey : authorizes_functionary_key
    Verifier --> Policy : evaluates
    Verifier --> Assurance : yields
    Policy --> Artifact : admits_or_blocks
    SigningKey ..> Policy : signing_gated_by
    SBOM --> Dependency : lists
    Dependency --> Dependency : depends_on
    Release --> Artifact : preserves
    Cluster --> Repository : reconciles
    SSCAttack --> SSCStep : compromises
    Policy ..> SSDFPractice : maps_to_ssdf (App. A)
```

## Findings for the tmodel object model

1. **Fig. 1 *is* PROV-O.** Step = `prov:Activity`, Actor = `prov:Agent` (including software agents,
   fn 1), uses/produces = `used`/`wasGeneratedBy`. ARCH-0001 §4 already uses PROV-O as its node
   model, so the 204D supply-chain model fits the same spine. The only open question is ADR-0001's
   split: is this custody provenance (deferred to radar) or something a conformance check reads?
2. **The signed Policy is the Gate's exit criterion.** 204D's Policy is "a signed document that
   encodes the requirements for an artifact to be validated". A Verifier evaluates it against stored
   attestations and gets an allow/block answer. That is the automatable check DL-0009 R-041/R-042
   describes. What 204D adds is that the criteria document is *signed*, names *which keys* may
   produce evidence, and depends on *time* (scan recency, build horizon).
3. **Attestation needs a type the model does not yet have.** It has four stated subtypes
   (environment, process, materials, artifacts) plus vulnerability-finding attestations and VSAs.
   It is not the §4 epistemic `Assertion`. See `gaps` in the YAML.
4. **Trust is ordered, not only zoned.** Driver tools run at higher trust than the steps they
   invoke, and the attestor at higher trust than the build. ARCH-0001 `TrustBoundary` models
   membership of a zone, not a ranking between zones.
5. **Separation of duties is a constraint on Review:** merge approvers cannot approve their own
   merges, and reviewers must be other developers.
