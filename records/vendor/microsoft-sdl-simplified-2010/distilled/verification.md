---
record: microsoft-sdl-simplified-2010
kind: verification
title: "microsoft-sdl-simplified-2010 — verify and cross-check passes (FX-1 passes 2 and 3)"
date: "2026-10-03"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# Simplified Implementation of the Microsoft SDL: verification report

## Sources and method

- **Source files.**
  - `.cache/microsoft-sdl-simplified-2010.doc` (sha256 `ef676ae4…d413` = `content.sha256`, 1,169,408 bytes);
  - the companion `.xlsx` (`094b8e5f…49c9`, 23,544 bytes).
- **My own renderings.**
  - `textutil -convert txt` of the `.doc`. Its `HYPERLINK \l "…"` field codes are stripped; these are what made 3 texts look broken at first.
  - An openpyxl dump of every spreadsheet row.
- **Scripts.** `gen_verify.py`, `split_check.py`, `norm_check.py` and `quote_check.py`, plus a sentence-level modal walk.

## Pass 2: verify

1. **Hash and currency.**
   - Both hashes match. ✔
   - Download Center id 12379, fetched 2026-10-03, still serves both files at the same sizes. The page's date is 7/15/2024, a re-publication.
   - The title page reads "Updated November 4, 2010". The `.doc` was created 2010-10-29.
   - The TOC's last page reference is 17, consistent with 17 pp.
   - Licence: front matter reads "Licensed under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported", alongside "© 2010 Microsoft Corporation. All rights reserved." **Confirmed.** ✔
2. **Verbatim (61/61).**
   - Every paper text is a substring of the cleaned `.doc` text.
   - Every spreadsheet text is a substring of the xlsx dump. That includes the `additional_notes` cells.
   - No splices: one sentence crosses a break, and its pieces are adjacent.
3. **Locators.** All 61 were checked. Each paper locator names the heading that holds the text, and each spreadsheet locator names the "SDL PRACTICE" number of its row.
4. **Completeness.**
   - A sentence-level walk of the whole `.doc` for must/should/required/requires/mandatory/need to found **9 statements missing** from both `requirements.yaml` and `normative.md`:
     - the Introduction: "development teams should apply the SDL in a way that is suitable to the human talent and resources available…";
     - About: "the SDL … requires regular evaluation of SDL processes … requires the archival of all data necessary to service an application in a crisis";
     - the Conclusion: "Development teams should use this document as a guide…";
     - **six text-box callouts** printed beside the body. One of them is the requirement *"Any issues identified during penetration testing must be addressed and resolved before the project is approved for release."* The extract pass had put the callouts in the cache Markdown only.
   - What remains is front matter (legal boilerplate) and TOC entries.
   - The sixteen mandatory practices, the three optional activities and the 28 spreadsheet rows (6 headers and 22 practices) all recount correctly.
   - `bin/bcp14-count` = 1 ("OPTIONAL", a caps-styled heading). The reconciliation is correct.
5. **Typing.**
   - All 16 practices are `requirement`. This follows the paper's "must successfully complete sixteen mandatory security activities", and is correct.
   - Spreadsheet rows Design 3.2, Implementation 4.2 and 4.3 were typed `recommendation`, although their ADDITIONAL NOTES cell states must-requirements:
     - "must adhere to the requirements … Policy for Managing Firewall Configurations";
     - "must not use banned versions of string buffer handling functions";
     - "must set the System.Web.UI.Page.ViewStateUserKey property";
     - "you must fix all violations that fall within the 'Security rules'".
6. **Object model and state machine.**
   - All 13 state-machine quotes and 11 object-model quotes are verbatim. The one apparent miss is our own tmodel-mapping phrase.
   - The FSR outcomes (Passed / Passed with exceptions / FSR with escalation) and the certification guards are verbatim.
   - Basic→Standardized and Advanced→Dynamic are honestly marked inferred.
7. **Claims.**
   - The SDL FAQ recommends the paper and the Resources page lists it under "Legacy archive" (verified in `microsoft-sdl`).
   - "There is a strong correlation between this paper and the published process" ✔.

### Defects found and fixed

| # | cat. | defect | fix |
|---|---|---|---|
| 1 | dropped | 9 modal-bearing statements (introduction, About, conclusion and 6 text-box callouts) were missing, including a must-requirement on penetration-test findings before release | appended as PROC-intro-minimum-threshold, PROC-core-concepts, PROC-conclusion-guide and CALLOUT-1..6 (verbatim, with an `added_by` note); new section in `normative.md`; header counts (61 = 52 + 9; 32/22/7), reconciliation, README, summary and record coverage updated |
| 2 | typing | 3 spreadsheet rows whose ADDITIONAL NOTES state must-requirements were typed recommendation | retyped `requirement`, verb "must (in the ADDITIONAL NOTES column)", each with a `verification_note` |

## Pass 3: cross-check

- **Requirements ↔ schema.** The derived enums agree with the paper:
  - FSR outcomes, the three values;
  - privacy impact ratings P1–P3;
  - the four Optimization Model levels and five capability areas;
  - roles (security advisor, privacy advisor, …).
- **State machine.** Every guard is a verbatim stated sentence, and the triggers are named events.
- **not_applicable.** All three reasons are true:
  - messages: no data formats;
  - protocol: only "escalate to executive management";
  - examples: the paper has none, and Appendix A is an embedded Visio image.
- **maps_to.** None published. The spreadsheet↔SP correspondence is a `see` note in `normative.md`.

## Residual open issues

- The `.doc` conversion cannot give a page or anchor position for the callouts, so their locator is "text-box callout n of 7".
- The spreadsheet rows Requirements 2.1, 2.1.1 and others restate mandatory practices, yet keep their own modal-word typing. They can be weaker than the SP-NN entry they restate, and a consumer should take SP-NN as authoritative.
