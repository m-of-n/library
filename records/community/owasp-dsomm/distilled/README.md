---
schema: "library-distilled-index/v1"
id: owasp-dsomm-distilled
record: owasp-dsomm
kind: index
type: index
title: "owasp-dsomm — distilled artifacts"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts — OWASP DSOMM (secondary reference)

Secondary record (status summarized): summary + object-model pass, plus the
published cross-references because they are crosswalk data for R-044. Not FX-1.

| file | coverage |
|---|---|
| `object-model.yaml`, `object-model.md` | 11 objects, 8 edges, 3 gaps |
| `crosswalk.yaml` | all 251 activities with dimension, sub-dimension, level, uuid and their samm2 / ISO 27001:2022 / OpenCRE references verbatim; 278 SAMM refs normalised to SAMM v2.2 activity ids, 2 unresolved (a literal placeholder and 'V-RT-AB-1') |
| `verification.md` | verify pass (2026-10-03): hash, currency, counts, crosswalk 251/251, no defects |
