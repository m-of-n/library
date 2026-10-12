---
schema: "library-distilled/v1"
id: sp-800-218r1-distilled-index
record: sp-800-218r1
kind: index
type: index
title: "sp-800-218r1 — distilled artifacts"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# Distilled artifacts: SP 800-218r1 ipd (SSDF 1.2, INITIAL PUBLIC DRAFT)

FX-1 (`docs/extraction.md`): extract, independent verify and cross-check passes recorded (see `verification.md`). The source is the draft PDF, sha256 `0f40af24b5d0175ced02dee971a89128f55ea9ac077963038b46cc9434a8d000`.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | The framework "should" statements (Executive Summary, §1, §2), the four group statements, the element definitions, and all of Table 1 verbatim: 22 practice rows (incl. retired PW.3), 54 task rows (incl. 5 retired), 225 notional implementation examples, 497 reference lines and Table 1 footnotes 5–9. Front matter, acknowledgments, reference bibliography and acronyms are left out (they are captured in `.cache/sp-800-218r1.md`). |
| requirements | `requirements.yaml` | 88 entries (`library-requirements/v2`): 8 framework statements (R-0001…R-0008), 4 groups, 22 practices, 54 tasks. Each active task carries its examples verbatim and its References column as `maps_to` (ids split with the `sp-800-218` rules; `reference_editions` names each cited edition). Retired ids are kept with `status: withdrawn`. Each entry has a `change_vs_v1_1` annotation. BCP 14 count 0/0, with the native baseline in `reconciliation`. |
| design notes | `design-notes.md` | Adopt, adapt and reject decisions mapped to R-040…R-044, DEC-009 and ARCH-0001 §2b and §3b; open questions. |
| diagram | `object-model.yaml` | Object-model pass: 86 objects, 104 edges and 8 gaps (32 objects and 48 edges ported from the sp-800-218 model by the verify pass, locators re-checked against the 1.2 IPD). Every item has a locator; 2 objects and 3 edges are inferred. |
| diagram | `object-model.md` | Mermaid class diagram of the backbone, plus 5 findings. |
| diff | `diff-vs-v1.1.md` | Full diff against SSDF 1.1 (official xlsx). New practices and tasks, reworded practices, tasks and examples (verbatim old and new), reference changes (EO14028 removed; SP 800-53 and 800-161 remapped), and defects in the change log. |
| verification | `verification.md` | Independent verify (pass 2) and cross-check (pass 3), 2026-10-02: method, counts, every defect found and how it was fixed, residual issues. Includes an independent re-derivation of the 1.1 → 1.2 diff. |

Not applicable (see `record.yaml`): schema, messages, protocol, state-machine and examples. The SSDF defines no data format, message, protocol or lifecycle. The notional implementation examples are informative illustrations, not test vectors, and are carried verbatim in `requirements.yaml`.

**Generation.** Table 1 was extracted from the PDF by word x-coordinates with pdfplumber, using column bands at x = 75 / 193.5 / 322.5 / 511.5 pt on the landscape pages 17–48. Text below 9 pt was separated out as footnotes. Rows were anchored at each task id, and lines and hyphenation were rejoined. Every unchanged task, example and reference was checked word for word against NIST's SSDF 1.1 xlsx. The new and changed content was hand-checked against `pdftotext -layout`. The scripts are in the session scratchpad (`r1_cols.py`, `r1_parse.py`, `r1_gen*.py`) and are not committed.
