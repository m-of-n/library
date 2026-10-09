---
schema: "library-distilled/v1"
id: cis-safecode-sbd-assessment-1-1-object-model
record: cis-safecode-sbd-assessment-1-1
type: diagram
updated: "2026-10-02"
---

# CIS/SAFECode Secure by Design v1.1 — object model (public material only)

9 objects, 6 edges, all stated, from the CIS landing page, CIS/SAFECode press releases and the SAFECode blog (2026-07-13). The guide and spreadsheet were not read (registration wall). CIS/SAFECode state v1.1 "is consistent in content with the new ETSI standard", so the full model is `etsi-ts-104-219/distilled/object-model.yaml`.

```mermaid
classDiagram
  direction LR
  class SecureByDesignConsideration { 6 }
  class SSDFPractice
  class DevelopmentGroup
  class Role
  class DevelopmentArtifact
  class CISControl
  SecureByDesignConsideration --> SSDFPractice : based_on
  SSDFPractice --> CISControl : maps_to
  SSDFPractice --> DevelopmentGroup : applies_to
  Role --> SSDFPractice : responsible
  SSDFPractice --> DevelopmentArtifact : evidenced_by
```
