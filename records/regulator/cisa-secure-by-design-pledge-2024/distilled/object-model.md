---
schema: "library-distilled/v1"
id: cisa-secure-by-design-pledge-2024-object-model
record: cisa-secure-by-design-pledge-2024
type: object-model
updated: "2026-10-02"
reviewed_by: ""
---

# Secure by Design Pledge — object model

Machine form: `object-model.yaml` (14 objects, 11 edges, 3 gaps; all stated).

```mermaid
classDiagram
    class Manufacturer
    class Pledge {
      signed_date
      voluntary
    }
    class Goal {
      id G1..G7
      due: signed+1y
    }
    class ExampleApproach
    class ProgressEvidence
    class Metric
    class Roadmap
    class Product
    class VulnerabilityClass
    class CVERecord {
      cwe
      cpe
    }
    class VDP
    class Customer
    class CISA
    Manufacturer --> Pledge : signs
    Pledge "1" --> "7" Goal : comprises
    Goal --> ExampleApproach : achieved_by (optional)
    Goal --> ProgressEvidence : evidenced_by
    ProgressEvidence --> Metric : measures
    Goal --> Product : applies_to
    Goal --> VulnerabilityClass : targets (G3)
    CVERecord --> VulnerabilityClass : annotated_with CWE
    Roadmap --> Product : plans
    Manufacturer --> CISA : reports_to (no progress)
    Metric --> Customer : behaviour_of
```

Key difference from the SbD whitepaper: the pledge turns principles into **seven time-boxed
goals with measurable, public outcome evidence**, but leaves the method entirely to the signer.
