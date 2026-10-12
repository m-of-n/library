---
schema: "library-distilled/v1"
id: cisa-secure-by-demand-guide-2024-object-model
record: cisa-secure-by-demand-guide-2024
type: object-model
updated: "2026-10-02"
reviewed_by: ""
---

# Secure by Demand Guide — object model

Machine form: `object-model.yaml` (16 objects, 12 edges — 3 inferred — 2 gaps).
The customer-side mirror of Secure by Design: a **SoftwareCustomer** asks **Questions** (in six
**Categories**) of a **SoftwareManufacturer** at a **ProcurementStage**, and checks answers against
**artifacts** either supplied by the manufacturer (SBOM, roadmaps) or **collected by the customer**
from public sources (baseline features, VDP page, CVE records, pledge status).

```mermaid
classDiagram
    class SoftwareCustomer
    class SoftwareManufacturer
    class Question
    class Category
    class ProcurementStage {
      before|during|following
    }
    class ManufacturerArtifact
    class SelfCollectedArtifact
    class SBOM
    class CVERecord
    class VDP
    class Pledge
    class VulnerabilityClass
    SoftwareCustomer --> Question : asks
    Question --> SoftwareManufacturer : answered_by
    Question --> Category : grouped_in
    Question --> ProcurementStage : asked_during
    Question ..> ManufacturerArtifact : evidenced_by (inferred)
    Question ..> SelfCollectedArtifact : checked_via (inferred)
    SoftwareManufacturer --> Pledge : signed
    SBOM --|> ManufacturerArtifact
    CVERecord --|> SelfCollectedArtifact
    VDP --|> SelfCollectedArtifact
    SoftwareManufacturer --> VulnerabilityClass : addresses
    CVERecord --> VulnerabilityClass : annotated_with (CWE)
```
