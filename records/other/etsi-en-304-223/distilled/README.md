---
schema: "library-doc/v1"
id: etsi-en-304-223-distilled-index
record: etsi-en-304-223
type: index
audience: human
updated: "2026-11-15"
---

# Distilled artifacts — ETSI EN 304 223 V2.1.1

FX-1 extraction (library#69). The source of record is the ETSI PDF
(`content.sha256` in `record.yaml`); every artifact cites the pinned
`pdftotext -layout` rendering named in `requirements.yaml` (`source_text`,
`source_text_digest`), by line number. Coverage figures live once, in
`record.yaml` `distillation.artifacts`, so they are not restated here.

| artifact | what it is |
|---|---|
| `requirements.yaml` | **machine source.** Each of the 72 provisions under its original id (`etsi-en-304-223#5.1.2-3`), split into one entry per sentence (`#R-NNNN`), with actor, object, field, testability; plus scope, stakeholder and applicability statements, and inferred obligations flagged `kind: inferred`. |
| `inferred-candidates.yaml` | every keyword-less sentence that might bind, and every verbal form in informative text, each with a verdict. |
| `normative.md` | the normative text by clause, quoted by line marker, and the source defects found. |
| `messages.yaml`, `schema/` | the work products the provisions require, and JSON Schemas derived from them. The EN defines no encoding or schema. |
| `protocol.yaml`, `protocol.md` | the process flows between stakeholder roles, with Mermaid diagrams. The EN defines no wire protocol. |
| `state-machine.yaml` | the lifecycles the provisions imply, stated vs inferred per state and transition. |
| `examples/` | the finding that the EN has no examples or test vectors; our own schema test cases (`*.derived.json`). |
| `design-notes.md` | adopt / adapt / reject against tmodel's and mofn's decisions, and open questions. |
| `skeleton-report.txt` | `bin/fx1-skeleton`'s counts, regenerable. |

**Id stability.** The provision ids predate this extraction and are cited by
tmodel; they are never renumbered. Cite a provision by its provision id, a
sentence by its `R-` id.

**Keywords.** `keyword_vocabulary: directives` — the ETSI Drafting Rules 3.2
verbal forms, which bind in lowercase. The reconciliation in
`requirements.yaml` accounts for every one.

Nothing here is reviewed by a person yet: `reviewed_by` is empty on every
artifact.
