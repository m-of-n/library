---
schema: "library-distilled/v1"
id: omb-m-23-16-object-model
record: omb-m-23-16
type: object-model
updated: "2026-10-02"
reviewed_by: ""
---

# OMB M-23-16 — object model (delta over M-22-18)

Machine form: `object-model.yaml` (12 objects, 9 edges, 3 gaps). Builds on
`omb-m-22-18/distilled/object-model.yaml`. The main new idea: the **end product** is the unit of
accountability, and its producer carries the assurance burden for **third-party components**.

```mermaid
classDiagram
    class SoftwareEndProduct
    class ThirdPartyComponent
    class Producer
    class Attestation
    class MinimumRequirement
    class POAM
    class ExtensionRequest
    class LeadAgency
    class CIODetermination
    class SDLPhase
    SoftwareEndProduct "1" --> "*" ThirdPartyComponent : incorporates
    SoftwareEndProduct --> Producer : produced_by
    Producer --> ThirdPartyComponent : accountable_for_components
    Attestation "1" --> "*" MinimumRequirement : affirms
    POAM --> ExtensionRequest : attached_to
    POAM "1" --> "*" SoftwareEndProduct : shared_by
    LeadAgency --> POAM : coordinates
    CIODetermination "1" --> "6" SDLPhase : ensures_across
    MinimumRequirement --> MinimumRequirement : maps_to (fn 6 SSDF)
```

`SDLPhase` (requirements, design, development, testing, deployment, maintenance — §B.3) is a
six-phase SDL list stated by OMB; it maps onto ARCH-0001 §3b `LifecyclePhase`
(architecture/design … maintenance/update).
