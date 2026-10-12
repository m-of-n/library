---
schema: "library-artifact-readme/v1"
id: eu-cra-2024-2847-schema
record: eu-cra-2024-2847
type: readme
updated: "2026-10-02"
---

# Schemas — Regulation (EU) 2024/2847

The Regulation ships **no schema** of its own (no ASN.1, CDDL or JSON Schema; no field names). Everything here is
**derived** from prose and marked so.

| File | Status | What |
|---|---|---|
| `cra-art14-notification.derived.schema.json` | derived | JSON Schema 2020-12 for the Art 14 notification family (early warning, notification, intermediate report, final report; vulnerability and severe-incident subjects), with Art 16(2) dissemination-delay inputs. Every property quotes its source phrase and locator. Clock fields are inferred deadline origins. |

Not modelled: ENISA single reporting platform form fields (not in the Regulation), SBOM format (Art 13(24) implementing
act not adopted as of 2026-10-02), Annex II / Annex VII document structures (see `../messages.yaml` `structures`).
