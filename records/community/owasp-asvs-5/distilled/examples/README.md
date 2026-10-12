---
schema: "library-doc/v1"
id: owasp-asvs-5-examples-index
record: owasp-asvs-5
type: index
updated: "2026-10-02"
reviewed_by: ""
---

# Examples — ASVS 5.0.0

ASVS has **no test vectors** and gives no example verification report. What it does give, and what is held
here as fixtures:

| file | what | origin |
|---|---|---|
| `identifiers.yaml` | 7 identifier vectors: the standard's own examples (`v5.0.0-1.2.5`, `1.11.3`, `1.2.5`) with expected parse/resolution, plus 4 derived vectors exercising stated rules (lower-case `v`, export form, unresolvable id, v4.0.3 → v5.0.0 through the published mapping) | source + derived (marked per vector) |
| `export-v1.1.1.json` | requirement V1.1.1 as it appears verbatim in every 5.0.0 export (nested JSON, flat JSON, CSV, legacy JSON, CycloneDX), with expected results; the three JSON forms validate against `../schema/` (checked 2026-10-02) | source (verbatim excerpts) |

Not held, deliberately: the level-choice illustration (startup → L1, online bank → L3; What is the ASVS? ›
Which level to achieve) is prose guidance, not a testable vector; it is in `normative.md`.
