---
schema: "library-doc/v1"
id: cisa-secure-by-demand-ot-2025-distilled-index
record: cisa-secure-by-demand-ot-2025
type: index
audience: human
updated: "2026-11-16"
---

# Distilled artifacts — CISA Secure by Demand: Priority Considerations for OT Owners and Operators

FX-1 extraction (library#69, family 4). The source of record is the CISA PDF
(`content.sha256` in `record.yaml`); every artifact cites the pinned
`pdftotext -layout` rendering named in `requirements.yaml` (`source_text`,
`source_text_digest`), by line number. Coverage figures live once, in
`record.yaml` `distillation.artifacts`, so they are not restated here.

| artifact | what it is |
|---|---|
| `requirements.yaml` | **machine source.** Every sentence with a verbal form outside the front matter and the Introduction (`#R-NNNN`), split per form; the 12 considerations' selection criteria and questions to ask manufacturers (with `consideration:` and `role:`); scope and keyword-less binding statements; inferred entries flagged `kind: inferred`. |
| `inferred-candidates.yaml` | the keyword-less sentences `bin/fx1-skeleton` cued as possibly binding, and the 8 verbal forms of the front matter and the Introduction, each with a verdict; binding text no cue caught was hunted into `requirements.yaml` with no candidate. |
| `normative.md` | the normative text by section, quoted by line marker, and the source defects found. |
| `messages.yaml`, `schema/` | four structures the guide prescribes in prose (consideration section, security event record, advisory content, VEX statement), two derived so its questions and criteria can be tested (manufacturer response, product-selection evaluation), and JSON Schemas generated with them by `schema/build.derived.py`. The guide defines no encoding or schema. |
| `protocol.yaml`, `protocol.md` | the selection and procurement flows between owner/operator and manufacturer, with Mermaid diagrams. No wire protocol exists. |
| `state-machine.yaml` | the lifecycles the guide implies, stated vs inferred per state and transition. |
| `examples/` | the finding that the guide has no worked examples or test vectors; our own schema test cases (`*.derived.json`). |
| `design-notes.md` | adopt / adapt / reject against tmodel's and mofn's decisions, and open questions. |
| `skeleton-report.txt` | `bin/fx1-skeleton`'s counts, regenerable. |
| `object-model.yaml`, `object-model.md` | the earlier object-model pass (2026-10-02), kept unchanged. |

**Keywords.** `keyword_vocabulary: directives` (lowercase verbal forms). CISA
does not follow the ETSI Drafting Rules; the reconciliation in
`requirements.yaml` accounts for every form.

Nothing here is reviewed by a person yet: `reviewed_by` is empty on every
artifact.
