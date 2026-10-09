---
schema: "library-distilled/v1"
id: eo-14028-object-model
record: eo-14028
type: object-model
updated: "2026-10-02"
reviewed_by: ""
---

# EO 14028 §4 — object model

Machine form: `object-model.yaml` (22 objects, 13 edges — 1 inferred — 4 gaps).

§4 is a *program*: dated **Directives** to named officials produce **Guidance** covering ten
**PracticeAreas** (§4(e)(i)–(x)); OMB then requires **Agencies** to comply, and producers
**attest**, deliver **SBOMs** and **Artifacts**, and publish a summary of risks assessed and
mitigated.

```mermaid
classDiagram
    class Directive {
      owner
      offset
      deliverable
    }
    class Guidance
    class PracticeArea {
      id (i)..(x)
    }
    class SoftwareProducer
    class Purchaser
    class Software
    class CriticalSoftware
    class BuildEnvironment
    class Artifact
    class PublicSummary
    class Tool
    class Release
    class SBOM
    class Attestation
    class Agency
    class Waiver
    Directive --> Agency : tasks
    Directive --> Directive : depends_on (+offset)
    Guidance "1" --> "10" PracticeArea : covers
    PracticeArea ..> SoftwareProducer : performed_by (inferred)
    PracticeArea --> BuildEnvironment : secures (i)(A-F)
    Artifact --> PracticeArea : demonstrates
    Artifact --> Purchaser : provided_to (on request)
    SBOM --> Software : describes
    Tool --> Release : runs_before (iv)
    Attestation --> PracticeArea : attests_to (ix)
    Software --> CriticalSoftware : classified_as
    Agency --> Guidance : requires_compliance (k)
    Waiver --> Guidance : overrides (m)
```

The ten practice-area ids (`eo-14028#§4(e)(i)(A)` … `#§4(e)(x)`) are the hub the CISA attestation
form's Appendix maps onto (cisa-ssdf-attestation-form-2024 `maps_to`).
