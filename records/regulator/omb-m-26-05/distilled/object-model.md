---
schema: "library-distilled/v1"
id: omb-m-26-05-object-model
record: omb-m-26-05
type: object-model
updated: "2026-10-02"
reviewed_by: ""
---

# OMB M-26-05 — object model

Machine form: `object-model.yaml` (13 objects, 8 edges, 2 gaps). The memo replaces one fixed
gate (attestation against SSDF) with an **agency-owned, risk-based assurance policy**; the
attestation form and SBOM become optional evidence sources.

```mermaid
classDiagram
    class AgencyHead
    class Agency
    class Producer
    class Product {
      kind: hardware|software
      cloud_platform
    }
    class RiskAssessment
    class AssurancePolicy
    class Inventory
    class AttestationForm
    class SBOM {
      current
      runtime_environment
    }
    class ContractTerm
    AgencyHead "1" --> "*" Product : accountable_for
    Agency --> Producer : validates
    AssurancePolicy --> RiskAssessment : based_on
    Inventory "1" --> "*" Product : lists
    AssurancePolicy ..> AttestationForm : may_use (optional)
    ContractTerm --> SBOM : requires_on_request
    class Memorandum
    class ReferenceDocument
    Memorandum --> Memorandum : rescinds (M-22-18, M-23-16)
    Memorandum --> ReferenceDocument : cites
```

Verifier note (2026-10-03): the `rescinds` edge runs memo -> memo (para 3). Pass 1 had drawn it
AssurancePolicy -> AttestationForm, which the source does not support (the form stays usable, R-0006).
