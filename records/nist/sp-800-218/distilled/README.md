---
record: sp-800-218
kind: index
title: "sp-800-218 — distilled artifacts"
extracted: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts — SP 800-218 (SSDF 1.1)

FX-1 (`docs/extraction.md`). Sources: the PDF (sha256 `617746e5…cde22`) and NIST's official
machine-readable SSDF 1.1 table, `nist.sp.800-218.ssdf-table.xlsx` (sha256 `f5729c4c…bd55`,
https://csrc.nist.gov/files/pubs/sp/800/218/final/docs/nist.sp.800-218.ssdf-table.xlsx). Both are
held only in `.cache/`. All 282 practice, task and example cells in the xlsx were checked against
the PDF text, ignoring whitespace. They match except for PDF line-break hyphenation and footnote
markers.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | Every normative statement, verbatim, with a locator. Executive Summary, §1 and §2 *should* statements; all of Table 1 (practices, tasks, examples, references); retired rows; footnotes 5–9; Appendix A Table 2; Appendix C identifier rules |
| requirements | requirements.yaml | 79 entries: 8 framework-level statements (R-0001..R-0008), 4 groups, 19 practices and 42 tasks (73 active), plus 6 retired ids. Table 1 footnotes 5–9 are attached to their tasks; `reference_editions` names the edition behind every scheme key. Examples are verbatim. `maps_to` holds the full References column and EO 14028 Table 2. Header counts are reconciled |
| requirements (derived) | crosswalk.yaml | `maps_to` pivoted by scheme, with the inverse index (reference id → SSDF tasks) |
| diagram | object-model.yaml | Object-model pass: 82 objects, 82 edges and 9 gaps, each with a locator and a tmodel mapping |
| diagram | object-model.md | Mermaid diagrams and findings |
| schema | — | N/A: the SSDF defines no data format (reason in record.yaml) |
| messages | — | N/A: no messages or structures defined |
| protocol | — | N/A: no exchange sequence defined |
| state-machine | — | N/A: §2 denies sequence; no lifecycle defined |
| examples | — | N/A: the notional examples are informative, not test vectors. They are held verbatim in requirements.yaml |
| design-notes | design-notes.md | Adopt, adapt or reject against R-040..R-044 and DEC-009 |
| verification | verification.md | Independent verify (pass 2) and cross-check (pass 3), 2026-10-02: method, counts, every defect found and how it was fixed, residual issues |

## How `maps_to.ids` were split from the References cell

`source_text` is always the verbatim line from the References cell. `ids` is a convenience split
of that line:

- **Code-like schemes** (BSIMM, SAMM, ASVS, IEC 62443, SP 800-53 and others) are split on `,`
  and `;`.
- **SP800181** is split on `,` and `;`. Its semicolons separate the NICE Tasks, Knowledge,
  Skills and Abilities groups.
- **CNCFSSCP** entries like `Area—Aspect1, Aspect2; Area2—…` are expanded to `Area—Aspect` pairs.
- **SCAGILE** entries like `Operational Security Tasks 14, 15` are expanded to
  `Operational Security Tasks 14` and `… 15`.
- **SAFECode section titles** (SCFPSSD, SCSIC, SCTPC) are split on `,` and `;`. None of the
  titles contains a comma.
- **SCTTM and NTIASBOM** are kept whole (`Entire guide`, `All`).

## Counts (native baseline)

| unit | source | extracted |
|---|---|---|
| groups | 4 | 4 |
| practices | 19 active + 1 retired | 20 |
| tasks | 42 active + 5 retired | 47 |
| notional implementation examples | 198 | 198 |
| reference lines (task × scheme) | 528 | 528 |
| reference identifiers | 1,483 | 1,483 |
| reference schemes | 29 | 29 |
| EO 14028 Table 2 rows | 15 | 15 |
| BCP 14 keywords | 0 | 0 |
