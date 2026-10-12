---
schema: "library-distilled/v1"
id: cisa-ssdf-attestation-form-2024-examples
record: cisa-ssdf-attestation-form-2024
type: examples
updated: "2026-10-02"
reviewed_by: ""
---

# Examples

The source contains exactly one example: the PDF file-naming convention (p.3), verbatim:

```
e.g. [Software Producer]_[Product]_[Version]_[Attestation Date]
→Acme_SecuritySuite_4.6.2.1_20230124
```

Expected result: producer `Acme`, product `SecuritySuite`, version `4.6.2.1`, attestation date
2023-01-24 (`examples/filename-vectors.yaml`).

The JSON instances are **ours** (constructed, not from the source), built from that example to
exercise `schema/attestation-form.schema.json`:

| file | expected |
|---|---|
| `attestation-acme.json` | valid |
| `attestation-3pao.json` | valid — 3PAO path: box checked + assessment attached, no signature (INS-20, INS-21); added by the verifier 2026-10-03 |
| `attestation-invalid-unsigned.json` | invalid — neither signature nor 3PAO assessment (violates the oneOf; INS-14 / INS-20) |
