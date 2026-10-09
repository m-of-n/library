---
schema: "library-distilled/v1"
id: cisa-ssdf-attestation-form-2024-object-model
record: cisa-ssdf-attestation-form-2024
type: object-model
updated: "2026-10-02"
reviewed_by: ""
---

# Attestation form — object model

Machine form: `object-model.yaml` (25 objects, 24 edges, 5 gaps; all `kind: stated`).

The form is a **signed, scoped, revocable conformance claim**: a `SoftwareProducer`, through a
`Signatory` who can bind it, affirms all 12 `AttestedPractice`s for a `SoftwareProduct` scope;
the Appendix maps each practice to `SSDFTask`s and `EOProvision`s. Alternatives are a
`ThirdPartyAssessment` (no signature) or a `POAM`. A `LapseNotification` ends it.

```mermaid
classDiagram
    class SoftwareProducer
    class Signatory
    class PrimaryContact
    class Attestation {
      form_version
      attestation_kind: new|following-waiver|revised
      attestation_scope
      date
    }
    class SoftwareProduct {
      name
      version
      release_date
    }
    class AttestedPractice {
      number 1a..4c
    }
    class SSDFTask
    class EOProvision
    class Environment
    class ThirdPartyComponent
    class Provenance
    class Release
    class Vulnerability
    class VulnerabilityDisclosureProgram
    class ThirdPartyAssessment
    class ThirdPartyAssessorOrganization
    class POAM
    class LapseNotification
    class Agency
    class Repository
    Attestation --> SoftwareProducer : issued_by
    Attestation --> Signatory : signed_by
    Signatory --> SoftwareProducer : acts_for
    PrimaryContact --> Attestation : contact_for
    Attestation "1" --> "*" SoftwareProduct : covers (+ future versions)
    Attestation "1" --> "12" AttestedPractice : affirms
    AttestedPractice --> SSDFTask : derived_from
    AttestedPractice --> EOProvision : addresses
    AttestedPractice --> Environment : secures (1a-1f)
    SoftwareProduct --> ThirdPartyComponent : incorporates
    ThirdPartyComponent --> Provenance : has_provenance
    Vulnerability --> Release : addressed before
    Vulnerability --> VulnerabilityDisclosureProgram : received_via
    ThirdPartyAssessment --> Attestation : in_lieu_of_signature
    ThirdPartyAssessment --> ThirdPartyAssessorOrganization : performed_by
    POAM --> Attestation : substitutes
    Attestation --> Repository : submitted_to
    Attestation --> Agency : received_by
    LapseNotification --> Attestation : revokes
```

| form object | tmodel (ARCH-0001 / DL-0009) |
|---|---|
| Attestation | `Assertion` (§4) specialised: signatory, scope, kind, revocation — **new** |
| AttestedPractice / SSDFTask / EOProvision | `Requirement` + `maps_to` crosswalk (R-044) |
| SoftwareProducer / Signatory / 3PAO / Agency | `Party` facets and roles (§2b) |
| ThirdPartyAssessment | `Review` with assurance level |
| POAM | `MitigationInstance` kind process/documentation (R-040) + milestones |
| Environment (dev/build) | needs Component/Environment for build infrastructure — gap |
| Release | SDL release `Gate` (R-041) |
