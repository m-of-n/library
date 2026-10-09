---
schema: "library-object-model/v1"
id: eu-cra-2024-2847-object-model
record: eu-cra-2024-2847
type: diagram
updated: "2026-10-02"
---

# CRA object model

Machine form: `object-model.yaml` (51 objects, 37 edges incl. 3 added in the verify pass; 2 objects and 2 edges inferred, the rest defined or named by
the Regulation, mostly Art 3). Only the core is drawn here. Parties and the reporting infrastructure are in the YAML.

```mermaid
classDiagram
    direction LR
    class Manufacturer { name_or_trademark; main_establishment_MS; enterprise_size }
    class ProductWithDigitalElements { identifier; intended_purpose; software_versions; product_class }
    class Component { maintainer; is_foss }
    class SupportPeriod { end_month_year >= 5y; rationale }
    class CybersecurityRiskAssessment { version; applicability_per_requirement; justification }
    class EssentialCybersecurityRequirement { part I|II; point; applicable }
    class TechnicalDocumentation { version; Annex VII elements }
    class EUDeclarationOfConformity
    class ConformityAssessment { module; notified_body }
    class SoftwareBillOfMaterials { format; top_level_deps }
    class Vulnerability { severity; impact }
    class ActivelyExploitedVulnerability { aware_at; evidence }
    class Incident { aware_at; root_cause }
    class SevereIncident { ground 14(5)(a)|(b) }
    class SecurityUpdate { issued_at; separate; free; advisory }
    class SecurityAdvisory
    class CVDPolicy
    class Notification { subject; stage; submitted_at; sensitivity }
    class CSIRTCoordinator { member_state }
    class ENISA
    class MarketSurveillanceAuthority

    ProductWithDigitalElements --> Manufacturer : manufactured_by
    ProductWithDigitalElements "N" --> "M" Component : integrates
    ProductWithDigitalElements --> SupportPeriod : has_support_period
    ProductWithDigitalElements --> CybersecurityRiskAssessment : assessed_by (versions)
    CybersecurityRiskAssessment --> EssentialCybersecurityRequirement : determines_applicability_of
    EssentialCybersecurityRequirement ..> SecurityUpdate : implemented_by (inferred)
    CybersecurityRiskAssessment --> TechnicalDocumentation : part_of
    TechnicalDocumentation --> ProductWithDigitalElements : documents
    SoftwareBillOfMaterials --> ProductWithDigitalElements : describes
    ConformityAssessment --> TechnicalDocumentation : evidenced_by test reports
    EUDeclarationOfConformity --> ProductWithDigitalElements : declares_conformity_of
    Vulnerability --> ProductWithDigitalElements : affects
    Vulnerability --> Component : located_in
    Vulnerability <|-- ActivelyExploitedVulnerability : state
    Vulnerability --> SecurityUpdate : remedied_by
    Vulnerability --> SecurityAdvisory : disclosed_in
    Manufacturer --> CVDPolicy : has_policy
    Incident <|-- SevereIncident : classified (14(5))
    Incident --> ProductWithDigitalElements : impacts
    Notification --> ActivelyExploitedVulnerability : reports
    Notification --> SevereIncident : reports
    Notification --> CSIRTCoordinator : submitted_to
    Notification --> ENISA : accessible_to
    Notification --> CSIRTCoordinator : disseminated_to
    Notification --> MarketSurveillanceAuthority : forwarded_to
```

## Findings

1. **The cybersecurity risk assessment is the hinge object.** Art 13(3) requires it to state, for *each* Annex I Part I(2)
   requirement, whether it applies, how it is implemented, and (Art 13(4)) a justification where it does not. That is a
   per-product `Requirement` applicability table with `MitigationInstance` pointers. It is exactly the R-042 conformity
   object, and a tmodel threat model is a natural way to produce it.
2. **Conformity covers product and process together.** CE marking (Art 3(31)) and the DoC attest to the product (Annex I
   Part I) *and* the manufacturer's vulnerability-handling processes (Part II). An SDL object (R-041) therefore has to be
   linkable to a product's conformity claim. It cannot stand alone.
3. **The lifecycle has dated legal anchors.** These are the support period (at least 5 years, end month and year
   published), update availability (`max(10y, remainder)`), and documentation retention (`max(10y after placing,
   support period)`). They give ARCH §3b's `LifecyclePhase` the `valid_from`/`valid_to` window it still lacks.
4. **"Actively exploited" and "known exploitable" are evidence-bearing states of a Vulnerability, not types.** The 24 h
   clock starts on awareness of reliable evidence, so the state change needs provenance: an Assertion plus a Review.
5. **Reporting needs objects tmodel does not have:** Incident/SevereIncident, a staged deadline-bound `Notification`,
   and the jurisdiction set (`made_available_in` Member States), which drives where the report is disseminated.
