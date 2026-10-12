---
schema: "library-distilled/v1"
id: pci-secure-slc-2-object-model
record: pci-secure-slc-2
type: diagram
updated: "2026-10-02"
---

# PCI Secure SLC v2.0 — object model (public material only)

16 objects, 9 edges (2 inferred), 3 gaps — from PCI SSC public pages only; the standard text was not read (licence agreement).

```mermaid
classDiagram
  direction LR
  class SecureSLCStandard { v2.0 }
  class SecureSoftwareStandard { v2.0 }
  class SoftwareVendor
  class VendorSecureSLC
  class SecureSLCAssessor
  class ReportOnValidation
  class AttestationOfValidation
  class Listing
  class SecureSoftwareProduct
  class SAID
  class SensitiveAsset
  class DigitalTool { incl. AI }
  SecureSLCStandard --> SecureSoftwareStandard : aligns_with
  VendorSecureSLC --> SecureSLCStandard : assessed_against
  SecureSLCAssessor --> ReportOnValidation : performs
  SoftwareVendor --> AttestationOfValidation : attests
  SoftwareVendor --> Listing : listed_in
  SecureSoftwareProduct --> VendorSecureSLC : developed_under (programme benefits)
  SAID --> SensitiveAsset : identifies
  VendorSecureSLC --> DigitalTool : governs_use_of
```

Finding: the PCI programme is the only SDL source here with a **public registry of validated SDL processes** and an explicit **process-to-product benefit** (a validated Secure SLC eases product validation). If tmodel ever models third-party validation status, it needs a `validated_by` edge from SecurityProgram to an external assessment with a listing.
