---
schema: "library-doc/v1"
id: iso-iec-29147-2018-object-model
record: iso-iec-29147-2018
type: diagram
updated: "2026-10-02"
---

# ISO/IEC 29147:2018 — object model (free preview)

Machine form: `object-model.yaml` (20 objects, 19 edges, 6 gaps). Solid boxes are **stated**
(Clause 3 definitions, Figure 1, visible text); objects known only from a clause heading are
**inferred** and marked `«inferred»`.

```mermaid
classDiagram
  class Vulnerability {
    <<stated 3.1>>
    identifier (CVE)
    severity (CVSS)
  }
  class PotentialVulnerability { <<inferred>> verification_status }
  class Reporter { <<stated 3.5>> }
  class Vendor { <<stated 3.4>> }
  class Coordinator { <<stated 3.6>> }
  class User { <<inferred 5.5.2>> }
  class Disclosure { <<stated 3.2 event>> }
  class Coordination { <<stated 3.3 activities>> }
  class Remediation { <<stated 3.7>> form; authenticity; deployment }
  class Mitigation { <<stated 3.7 Note 1>> workaround / countermeasure }
  class Advisory { <<stated 3.8>> 16 elements 7.4.2-7.4.17 }
  class VulnerabilityReport { <<inferred>> tracking_id; acknowledged }
  class VulnerabilityDisclosurePolicy { <<stated Fig1 / Cl.9>> }
  class Product { <<inferred 5.4.3>> }
  class Service { <<inferred 5.4.4>> }
  class Component { <<inferred 5.4.2>> }
  class Embargo { <<inferred 5.6.8>> }

  Reporter --> Vendor : notifies
  Reporter --> Coordinator : notifies
  VulnerabilityReport --> PotentialVulnerability : concerns
  Vendor --> PotentialVulnerability : verifies
  PotentialVulnerability <|-- Vulnerability : verified
  Vendor --> Vulnerability : responsible_for_remediating
  Coordinator --> Coordination : performs
  Coordination --> Disclosure : supports
  Vulnerability --> Product : present_in
  Vulnerability --> Service : present_in
  Vulnerability --> Component : present_in
  Product --> Component : depends_on «inferred»
  Remediation --> Vulnerability : removes_or_mitigates
  Remediation <|-- Mitigation
  Remediation --> Product : changes
  Advisory --> Vulnerability : provides_information_about
  Advisory --> Remediation : references «inferred»
  Advisory --> User : intended_for
  Vendor --> Advisory : publishes
  Vendor --> VulnerabilityDisclosurePolicy : publishes
  Embargo ..> Disclosure : delays «inferred»
```

## Findings

1. **Roles, not organisations.** Vendor, reporter and coordinator are defined by what a party
   *does* (remediates / notifies / coordinates), and Note 1 to 3.5 says anyone — including a vendor or
   a coordinator — can be a reporter. This confirms ARCH-0001 §2b's choice: relational roles are
   edges on one `Party`, never node types.
2. **Potential → verified is an acceptance gate.** The whole standard pair pivots on "Vulnerability
   verified?" (Figure 1). In tmodel this is the reified `Assertion` (a report) receiving a `Review`
   (verification verdict) — the same AI-proposes/human-accepts spine of ARCH-0001 §4.
3. **Remediation ⊃ mitigation.** 29147 defines remediation as a change that removes *or mitigates*,
   with workarounds/countermeasures as mitigations. tmodel's `MitigationInstance` is the general
   class; a remediation is `kind: technical`, an advisory telling users a workaround is
   `kind: documentation` (R-040).
4. **The advisory is a governed, versioned document** with a revision history (§7.4.16) and terms of
   use — exactly R-043's governed view, and its 16 elements are a ready-made field list (see
   `messages.yaml`) that OASIS CSAF renders as JSON.
