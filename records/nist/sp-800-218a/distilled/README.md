---
record: sp-800-218a
kind: index
title: "sp-800-218a — distilled artifacts"
extracted: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`), plus the Lane A object-model pass. Each row says what the
artifact covers and what it leaves out. The source is NIST SP 800-218A, July 2024
(final), sha256 `e088c8bc75716824dae7c36a987f408364638561d381ed001b5c12254a7b10d8`.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | Covers all of Table 1 verbatim: 20 practices, 48 tasks with Priority, 86 R/C/N additions, the 10 "No additions" markers and every Informative References cell. Also covers 14 governing prose statements, the §3 column semantics and 9 glossary definitions. Leaves out FISMA boilerplate, the acknowledgements and the reference list. |
| requirements | requirements.yaml | 168 entries under native ids (`PO.1.2.R1`, …), with prose entries as `R-NNNN`. Each carries Priority, profile status, the SSDF 1.1 text where an item changed, and `maps_to` (AI RMF / OWASP LLM / Adv ML). Fields marked derived need review. |
| schema | — | Not applicable. No data format is defined (see record.yaml). |
| messages | — | Not applicable. No messages are defined. |
| protocol | — | Not applicable. The agreement and attestation are named but not specified. |
| state-machine | — | Not applicable. RV.2.2.R2 implies model stop/rollback states but defines none. |
| examples | — | Not applicable. The Profile has no Implementation Examples column yet. |
| design-notes | design-notes.md | Adopt/adapt/defer/reject decisions mapped to R-040..R-044, DEC-009 and ARCH-0001; source defects; open questions. |
| diagram | object-model.yaml | Object-model pass: 62 objects, 52 edges and 9 gaps, each with a locator and a tmodel mapping. |
| diagram | object-model.md | Mermaid class diagram and the headline findings, generated from object-model.yaml. |
| verification | verification.md | Verify and cross-check passes (2026-10-02). Covers methods, counts, 6 defect classes found and fixed, and residual issues. |

## How the extraction was done

1. The Table 1 rows were parsed by word position with pdfplumber, using the column x
   ranges 0–240 / 240–425 / 425–470 / 470–680 / 680+ (pt).
2. Every practice, task and addition text was checked against `pdftotext` output in
   4-word windows. 12 windows straddle a page break and were checked by hand.
3. The 48 Priority values were cross-checked against the `pdftotext -layout` rendering:
   0 mismatches.
4. The Profile text was diffed against the official SSDF 1.1 machine-readable table
   (`nist.sp.800-218.ssdf-table.xlsx`). This confirmed the 3 tagged task modifications
   and the 6 new tasks, and found one untagged change (PO.5.2).

The parse scripts were kept in the session scratchpad and are not committed. The local
capture is in `.cache/sp-800-218a.md` (gitignored).
