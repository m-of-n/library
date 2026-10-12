---
record: fda-premarket-cybersecurity-guidance
kind: schema-index
title: "fda-premarket-cybersecurity-guidance — schemas"
extracted: "2026-10-02"
reviewed_by: ""
---

# Schemas — all DERIVED

FDA publishes **no** schema, data format or CDDL for any of this documentation; the only
format statement is that the SBOM "should be in a machine-readable format" (VI.A-16) in an
"industry-accepted" format (V.A.4.b-06). Every file here is therefore `derived` from prose, with
each property's `description` citing the requirement id that asks for it.

| file | from | what it models |
|---|---|---|
| `sbom-supplement.derived.schema.json` | §V.A.4(b) | FDA's per-component supplement (level of support, end-of-support date) and known-vulnerability entries, as the addendum FDA permits beside an SPDX/CycloneDX SBOM |
| `cybersecurity-management-plan.derived.schema.json` | §VI.B, §VII.C.1 | the nine plan elements + the 524B(b)(1)/(b)(2) additions; conditional `required` for cyber devices |
| `architecture-view.derived.schema.json` | §V.B.2, App. 2 | a security architecture view: four view types, five asset categories, per-communication-path details |
| `premarket-cybersecurity-documentation.derived.schema.json` | App. 4 Table 1 | completeness index over the Table 1 elements, referencing the three schemas above; 524B elements required for cyber devices |

Validated: each schema is valid draft 2020-12 (checked with `jsonschema` `Draft202012Validator.check_schema`),
and `../examples/sbom-supplement.constructed.json` validates against the SBOM supplement schema.
