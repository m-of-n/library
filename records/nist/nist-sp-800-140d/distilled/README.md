---
schema: "library-doc/v1"
id: nist-sp-800-140d-distilled-index
record: nist-sp-800-140d
type: index
audience: human
updated: "2026-11-15"
---

# Distilled artifacts — NIST SP 800-140D

FX-1 extraction (library#69, with the other FIPS 140-3 / SP 800-140 documents).
The source of record is the NIST PDF (`content.sha256` in `record.yaml`);
every artifact cites the pinned `pdftotext -layout` rendering named in
`requirements.yaml` (`source_text`, `source_text_digest`), by line number.
Coverage figures, and the reason for each artifact this document does not
need, live once in `record.yaml` `distillation`, so they are not restated here.

| artifact | what it is |
|---|---|
| `requirements.yaml` | **machine source.** Every keyword sentence, verbatim with source lines, plus the keyword-less binding text (table rows, list items) and inferred obligations flagged `kind: inferred`; actor, object, field, testability, normativity. |
| `inferred-candidates.yaml` | every keyword-less sentence that might bind, and every verbal form in front matter or notes, each with a verdict. |
| `normative.md` | the normative text by section, quoted by line marker, and the source defects found. |
| `messages.yaml` | the structures the document prescribes (documents, tables, evidence), field by field, each tied to the requirement that demands it. |
| `schema/` | JSON Schemas derived from `messages.yaml`, with the generator and accept/reject cases. |
| `examples/` | the finding on examples and test vectors, and our own derived fixtures (`*.derived.json`). |
| `design-notes.md` | adopt / adapt / reject against tmodel's and mofn's decisions, and open questions. |
| `skeleton-report.txt` | `bin/fx1-skeleton`'s counts from the run that wrote the verbatim layer (pass-1 reader, before 63d708e). A re-run under the fixed reader reports 12 verbal forms, 11 of them in front matter, and 37 candidates, not 14, 13 and 29: the withdrawal date's May is no longer counted and items 2 to 6 are no longer headings (normative.md SD-1, SD-3). |

**Keywords.** `keyword_vocabulary: directives` (lowercase shall / should /
may / can ...). The reconciliation in `requirements.yaml` accounts for every
one, including those in front matter.

Nothing here is reviewed by a person yet: `reviewed_by` is empty on every
artifact.
