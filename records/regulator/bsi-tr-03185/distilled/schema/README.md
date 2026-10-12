---
schema: "library-distilled/v1"
id: bsi-tr-03185-schema
record: bsi-tr-03185
type: schema
updated: "2026-10-02"
---

# Derived schemas

BSI TR-03185 ships no schema of its own. It defines **content** for work products, not formats. Every file
here is therefore `*.derived.schema.json` (JSON Schema 2020-12), generated from the matching structure in
`../messages.yaml`. A field is `required` only when a MUST governs it in the TR. Fields governed by SHOULD,
or listed "where applicable", are optional, and each field's description carries its source requiredness
and its `constrained_by` requirement ids. `additionalProperties` is true throughout, because several TR
lists are open ("including, but not limited to").

| File | Source |
|---|---|
| `requirement-row.derived.schema.json` | §1.3 Table 4, the System of Requirements |
| `pruefspezifikation-row.derived.schema.json` | BSI Prüfspezifikation v1.0 sheet columns |
| `threat-model.derived.schema.json` | PROD.DEV.C.1–C.5 |
| `issue-analysis-record.derived.schema.json` | PROD.FIX.A.6, A.7 |
| `issue-resolution-decision.derived.schema.json` | PROD.FIX.A.8 |
| `security-update-documentation.derived.schema.json` | PROD.FIX.A.10 |
| `release-record.derived.schema.json` | PROD.TEST.A.17, PROD.PM.A.14, PROD.REL.1–2, PROD.DEV.I.3, L.1–2 |
