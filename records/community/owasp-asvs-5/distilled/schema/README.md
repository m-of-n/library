---
schema: "library-doc/v1"
id: owasp-asvs-5-schema-index
record: owasp-asvs-5
type: index
updated: "2026-10-02"
reviewed_by: ""
---

# Schemas — ASVS 5.0.0 exports

**OWASP publishes no schema of its own** for the ASVS exports (checked: the `5.0/` tree at tag
`v5.0.0_release` holds `templates/` and `tools/` export scripts, no `*.schema.json`). Everything here is
**derived** by the library from the release assets and **validated against them** (`jsonschema`, all pass,
2026-10-02).

| file | validates | status |
|---|---|---|
| `asvs-export.derived.schema.json` | `..._5.0.0_en.json` (Chapter → Section → Requirement tree; the XML export has the same element names under `<root>`) | derived, validates the release asset |
| `asvs-flat.derived.schema.json` | `..._5.0.0_en.flat.json`; its seven keys are also the CSV columns, in order | derived, validates the release asset |
| `asvs-legacy-requirement.derived.schema.json` | each requirement item of `..._5.0.0_en.legacy.json` (4.x shape: per-level tick flags, `CWE`, `NIST`) | derived; asserts the CWE/NIST arrays are empty in 5.0.0 — true for all 345 |

The **CycloneDX** export (`..._5.0.0_en.cdx.json`) conforms to the CycloneDX 1.6 `declarations.standards`
schema (record `cyclonedx-1-7` holds the line); it is not re-derived here. See `messages.yaml` for its
structure and a source defect (level membership lists are empty).

Level semantics are not encodable in the schema: `L` is the lowest level at which a requirement applies and
levels are cumulative (What is the ASVS? › Application Security Verification Levels) — see
`state-machine.yaml`.
