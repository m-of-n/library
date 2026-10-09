---
schema: "library-verification/v1"
id: sp-800-218a-verification
record: sp-800-218a
type: verification
kind: verification
title: "sp-800-218a — FX-1 verify and cross-check passes"
verified: "2026-10-02"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# Verification of sp-800-218a (FX-1 passes 2 and 3)

Everything below was checked against the **source PDF**. The summary, normative.md and the pass-1
scratch scripts were not used as evidence. The method was independent of pass 1: pass 1 parsed
Table 1 with pdfplumber, and this pass used poppler `pdftotext` column crops (`-x/-y/-W/-H`, read
column by column across pages 16–27) and `pdftotext -tsv` word coordinates.

## Pass 2 — verify

| check | method | result |
|---|---|---|
| Hash | `shasum -a 256 .cache/sp-800-218a.pdf` | `e088c8bc…10d8` = `content.sha256` ✔ |
| Currency | https://csrc.nist.gov/pubs/sp/800/218/a/final, opened 2026-10-02 | Final 2024-07-26 (draft 2024-04-29). No withdrawal and no revision. SP 800-218r1 (SSDF 1.2) is still an IPD (2025-12-17; comments closed 2026-01-30) ✔ |
| Verbatim | Every `text` in requirements.yaml and every quoted statement in normative.md (374 source quotes; 2 front-matter strings excluded) was normalised to alphanumerics (NFKC; whitespace, hyphenation and ligatures ignored) and checked as a contiguous substring of the plain and column-major renderings, with running heads and column headers dropped | 374/374 pass (after the R-0014 addition, 376/376). A second, punctuation-preserving check failed on 21 items. All 21 are real compound hyphens at line ends (e.g. "risk-based", "fact-checking") that `pdftotext` silently dehyphenates; `-layout` keeps them. The record is right |
| Splices | Contiguity is enforced by the substring test. Texts were also searched for embedded `R\d:`/`C\d:` labels | 0 spliced quotes |
| Addition ↔ task assignment | The sequence of R/C/N labels and "No additions" markers in the column, compared with the yaml. Every ambiguous boundary (a task whose first addition is not R1) was resolved by `-tsv` y-coordinates | 96/96 positions match. All 9 ambiguous boundaries are correct, as are the C1-before-R1 order in PO.5.1 and the R2, N1, R3 order in RV.1.1 |
| Counts | Recounted from the column crops | 20 practices, 48 tasks, 59 R / 16 C / 11 N, 10 "No additions", Priority 21 H / 22 M / 5 L, task order and Priority sequence identical ✔. Tags: 2 practices + 3 tasks "Modified", 1 practice + 6 tasks "Not part of SSDF 1.1" ✔. `bin/bcp14-count` = 0 ✔. Lowercase should 36 / shall 1 / must 1 / may 24 ✔ |
| Informative References | Each ref-column cell assigned to its task by y-coordinate, then compared with `maps_to.source_text`; `ids` re-parsed from `source_text` | 48/48 tasks match, including the 6 empty ones. 61/61 `source_text` verbatim. Parsed ids are consistent (e.g. `LLM05-8`, which pdftotext renders "LLM058") ✔ |
| Locators | Tasks and practices: all 68 checked against the `-tsv` page of their id. R/C/N additions: all 86 checked against the page of their label. Prose: all checked | **19 defects fixed** (see below). 0 remaining |
| SSDF 1.1 deltas | `ssdf_1_1_text` checked against `.cache/sp-800-218.txt` | 5/5 quoted texts verbatim. PO.5.2 untagged change confirmed. PO.1 "SDLC" expansion confirmed |
| Typing | Distribution of normativity, level, kind and testable | No weakening: R→recommendation, C→consideration, N→informative; prose is typed by its own verb. All entries are `kind: stated` (correct; nothing implied was added) |
| Object model | Every locator id resolves to a requirements id. Quoted definitions were checked verbatim. Edge endpoints are defined objects. `tmodel_mapping` was spot-checked against ARCH-0001 §0–§5, §2b, §3b and DL-0009 | 62 objects / 52 edges / 9 gaps. All locators resolve and every endpoint is defined. 3 inferred items are flagged. One false note was fixed (below) |
| Completeness sweep | Front matter, §1–§3, footnotes and Appendix A were swept for should/must/shall/expected/encouraged/recommend | **1 dropped statement** (below). Footnotes on table pages: none |

### Defects found and fixed

1. **Dropped (completeness).** §2 footnote 2: "Organizations using this document are encouraged to
   adapt it to any machine learning-specific life cycle they are using." It is now
   `sp-800-218a#R-0014` (recommendation), and normative.md has the matching line. Counts went from
   167 to 168 entries and from 13 to 14 prose statements in requirements.yaml, record.yaml,
   README and summary.
2. **Locators (19).** These R/C/N additions continue onto the page after their task, but their
   `p.` was the task's page. Corrected: PO.5.1.R4–R6 → p. 11; PS.1.1.R4/C1/C2 → p. 12;
   PS.3.1.R2/R3/N1 → p. 13; PW.1.1.C1/C2 → p. 14; PW.3.1.R2/C1 → p. 15; PW.4.4.R2 → p. 16;
   RV.1.1.R2/N1/R3 → p. 18; RV.2.2.R2/C1 → p. 19.
3. **Verbatim / structure (normative.md glossary).** Three Appendix A terms were mis-split, with the
   term's last word leaking into the definition (e.g. term "artificial intelligence", definition
   "model A component of …"). The terms are now "artificial intelligence model", "artificial
   intelligence red-teaming" and "artificial intelligence system", each with its exact definition.
   The character-level check passed these, which is why the column check was not enough on its own.
4. **Claim (false source defect).** design-notes, summary, record.yaml coverage and object-model
   said 218A *renamed* the PS group ("Protect Software" vs SSDF 1.1 "Protect the Software"). SP
   800-218 Table 1's group row also reads "Protect Software (PS)"; only its §2 prose says "Protect
   the Software". The claim is withdrawn in all four places, and the defect count is now 4.
5. **Claim (PW.3.3).** `ssdf_1_1_text` said "SSDF 1.1 retired this identifier" for PW.3.3. The
   SP 800-218 change log retires PW.3, PW.3.1, PW.3.2, PW.4.3 and PW.5.2 only, so PW.3.3 is a fresh
   id. Corrected.
6. **Claim (reconciliation).** The reconciliation said "4 should are boilerplate" and "bin/validate
   errors on source_keyword_count 0". The real residue is 3 boilerplate, 1 predictive (§2 "should
   help"), 2 R/C definitions, 1 §1 example duplicating PS.1.1.R1, and 29 in texts (= 36). The
   current validator accepts 0 when a reconciliation is given. Rewritten.

### Claims checked and found correct

The ERB approval date of 2024-07-25 is on p. ii. Its authors and affiliations, and its 30 pages
(pdfinfo), are correct. EO 14110 was revoked by EO 14148 on 2025-01-20. SSDF 1.2 IPD (2025-12-17)
does not mention 218A (CSRC). SSDF 1.1 has 19 practices and 42 tasks. PW.1.1.R1 names seven
threat types. PS.3.2 adds SLSA. PW.2.1 changed "and/or" to "and". The PO.5.2 untagged change is
real, and so is the §3 "considering adding a column for Implementation Examples" sentence (cited
by the examples N/A reason).

## Pass 3 — cross-check

- No schema, messages, protocol, state machine or examples exist. Each N/A reason was re-read
  against the source and is true. The examples N/A quote is verbatim (§3, p. 7).
- `maps_to`: every target names its edition (`[2] NIST AI 100-1 (AI RMF 1.0)`, `[15] OWASP Top 10
  for LLM Applications v1.1`, `[3] NIST AI 100-2e2023`) and uses the target's own id spelling.
  "Adv ML" carries no ids because the source gives none.
- Every requirement id cited in object-model.yaml and design-notes.md exists in
  requirements.yaml.

## Residual / open

- Derived fields (phase, nature, expects_deliverables, verification, testable) are unreviewed
  judgement. `phase: supply-chain` is used for 44 entries, which is generous.
- "Cost models may need to be updated to effectively consider the costs inherent to AI model
  development." (§2) is not extracted. It is a possibility statement, not a recommendation.
  Flagged for the human reviewer.
- Human review (pass 4) is outstanding for every artifact.

Scripts: session scratchpad `verify/vcheck.py`, `omcheck.py` and the inline checks. They are not
committed.
