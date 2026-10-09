---
schema: "library-doc/v1"
id: cncf-supply-chain-best-practices-v2-object-model
record: cncf-supply-chain-best-practices-v2
type: object-model
updated: "2026-10-02"
reviewed_by: ""
---

# CNCF Software Supply Chain Best Practices v2 — object model

Machine source: `object-model.yaml` (39 objects, 29 edges, 5 gaps; locators are SSCBPv2.md headings).

```mermaid
graph LR
  Persona -- plays_role --> SoftwareProducer
  Persona -. plays_role .-> SoftwareDistributor
  Persona -. plays_role .-> SoftwareConsumer
  Stage -- has_category --> PracticeCategory -- contains --> Practice
  SupplyChainThreat -- threatens --> Stage
  Practice -. mitigates .-> SupplyChainThreat
  SourceRepository -- has_namespace --> ProtectedNamespace
  SourceRepository -- logs --> AuditLog
  ChangeRequest -- reviewed_by --> Persona
  Dependency -- supplied_by --> ThirdPartySupplier
  Dependency -- retrieved_from --> TrustedRepository
  PipelineOrchestrator -- orchestrates --> BuildStep
  BuildWorker -- executes --> BuildStep
  BuildStep -- produces --> Attestation
  BuildStep -- outputs --> Artifact
  Signature -- signs --> Artifact
  SBOM -- describes --> Artifact
  VEX -- qualifies --> SBOM
  Attestation -- attests_to --> Artifact
  Attestation -- signed_by --> Identity
  Attestation -- evaluated_against --> SupplyChainPolicy
  SupplyChainPolicy -- authorizes --> Identity
  SupplyChainPolicy -- requires_test --> TestResult
  Attestation -- stored_in --> MetadataStore
  RootOfTrust -- anchors --> SigningKey
  TUFRepository -- distributes --> Artifact
  Client -- verifies --> Attestation
  DeploymentGate -- gates --> Artifact
```

Attestation lifecycle (Part 2 › Attestations), stated as four phases:

```mermaid
stateDiagram-v2
  [*] --> Created : step executes, actor signs
  Created --> Distributed : associated with artifact (TUF, Archivista, OCI)
  Distributed --> Verified : checked against supply-chain policy
  Verified --> Stored : kept as audit trail
```

## Findings for tmodel

1. **Policy evaluated against attestations is the gate check.** The paper defines supply-chain
   policy as "requirements for the software supply chain, defined in software, including authorized
   actors and expected actions", evaluated against signed attestations. That is the automatable
   Gate exit criterion R-041/R-042 need. tmodel has no `Policy` object.
2. **A deployment gate is a real, automated gate.** The admission controller "can supplement, but
   not replace" verification at the end of the pipeline and by the end user. Gates are layered, not
   single.
3. **Distributor is a missing Party role** in ARCH-0001 §2b.
4. **VEX statuses** (AFFECTED / NOT AFFECTED / UNDER INVESTIGATION / FIXED) are the values the R-027b
   VEX-override Assertion should carry.
5. **Stages ≈ lifecycle phases.** The five stages and the SLSA threat mapping A–I give a
   supply-chain slice of the `LifecyclePhase` axis (R-037).
