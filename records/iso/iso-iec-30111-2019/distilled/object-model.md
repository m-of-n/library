---
schema: "library-doc/v1"
id: iso-iec-30111-2019-object-model
record: iso-iec-30111-2019
type: diagram
updated: "2026-10-02"
---

# ISO/IEC 30111:2019 — object model (free preview)

Machine form: `object-model.yaml` (18 objects, 19 edges, 5 gaps). 30111 imports 29147's terms
(Clause 3), so the vulnerability/reporter/advisory objects live in
`iso-iec-29147-2018/distilled/object-model.yaml`; this model adds the organisation (Clause 6, fully
visible) and the handling phases (Clause 7, headings only — see `state-machine.yaml`).

```mermaid
classDiagram
  class TopManagement { <<stated 6.2>> }
  class VulnerabilityHandlingPolicy {
    <<stated 6.3 shall>>
    guidance_principles_responsibilities
    responsible_departments_and_roles
    premature_disclosure_safeguards
    target_remediation_schedule
  }
  class VulnerabilityDisclosurePolicy { <<29147 Cl.9>> }
  class VulnerabilityHandlingProcess { <<stated 6.1>> documented; repeatable }
  class ProcessAssessment { <<stated 6.1 / 7.2>> }
  class OrganizationalFramework { <<stated 6.4>> }
  class DecisionRole { <<stated 6.4>> }
  class PointOfContact { <<stated 6.4 / 6.5.3.3>> internal | external }
  class PSIRT { <<stated 6.5>> central | business-unit }
  class ProductBusinessDivision { <<stated 6.5.3.4>> }
  class CustomerSupportDivision { <<stated 6.5.3.3>> }
  class PublicVulnerabilitySource { <<stated 6.5.3.2>> }
  class HandlingPhase { <<7.1 headings>> Preparation..Post-release }
  class Product

  TopManagement --> VulnerabilityHandlingPolicy : establishes
  TopManagement --> DecisionRole : assigns_responsibility
  DecisionRole --> TopManagement : reports_performance_to
  VulnerabilityHandlingPolicy --> VulnerabilityDisclosurePolicy : compatible_with
  VulnerabilityHandlingPolicy --> VulnerabilityHandlingProcess : governs
  ProcessAssessment --> VulnerabilityHandlingProcess : assesses
  VulnerabilityHandlingProcess --> Product : covers (all)
  OrganizationalFramework o-- DecisionRole
  OrganizationalFramework o-- PSIRT
  PSIRT --> PointOfContact : receives_reports_via (single)
  PSIRT --> PublicVulnerabilitySource : monitors
  PSIRT --> ProductBusinessDivision : dispatches_report_to
  PointOfContact --> ProductBusinessDivision : contact_for
  PSIRT ..> CustomerSupportDivision : routes_reports_via (may)
  CustomerSupportDivision --> PSIRT : partners_with
  VulnerabilityHandlingProcess --> HandlingPhase : phases
```

## Findings

1. **One hard requirement is a document.** The single visible `shall` on the vendor (§6.3) is to
   develop and maintain an internal vulnerability handling policy — a governed, maintained document
   (R-043) whose presence and contents (a)–d)) a conformance check (R-042) can test mechanically.
2. **The policy carries a remediation SLA.** §6.3 d) "a target schedule for remediation
   development" gives a mitigation planned-date that ARCH-0001 §5's `MitigationInstance` lacks.
3. **Organisation is a graph, not a role list.** PSIRT ⊂ vendor, per-product divisions with contacts,
   support routing — Parties with `part_of` and `contact_for` edges that ARCH-0001 §2b does not yet have.
4. **Handling feeds the SDL back.** §6.1 points root-cause analysis back into secure development
   (ISO/IEC 27034): a loop from the response phase to design/implementation, which an ordered gate line
   (R-041) alone does not express.
