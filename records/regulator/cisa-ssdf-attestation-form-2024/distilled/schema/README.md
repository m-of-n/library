---
schema: "library-distilled/v1"
id: cisa-ssdf-attestation-form-2024-schema
record: cisa-ssdf-attestation-form-2024
type: schema
updated: "2026-10-02"
reviewed_by: ""
---

# Schema — derived

`attestation-form.schema.json` (JSON Schema 2020-12) is **derived** by the library: the source
is a PDF form with no machine-readable schema. Every property has `x-locator` (page/section of the
form) and, where one exists, `x-requirement` (the requirement id it renders).

Design choices, all flagged in the schema:
- Section III items are `const: true` — the form is all-or-nothing; a producer that cannot attest
  sends a POA&M package instead (instructions p.4), which is a different message (`messages.yaml`).
- The signature and the 3PAO path are a `oneOf` (instructions p.4: "The producer need not sign the
  form in this instance").
- `products` is required unless scope is company-wide (Section I).
- The online RSAA form (https://softwaresecurity.cisa.gov) was not inspected (login-gated); its
  field names may differ.

Validated: `examples/attestation-acme.json` passes; `examples/attestation-invalid-unsigned.json`
fails (no signature and no 3PAO).
