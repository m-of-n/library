---
record: microsoft-sdl-5-2
kind: verification
title: "microsoft-sdl-5-2 — verify and cross-check passes (FX-1 passes 2 and 3)"
date: "2026-10-03"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# Microsoft SDL Process Guidance 5.2: verification report

## Source and method

The source is `.cache/microsoft-sdl-5-2.docx`:

- sha256 `108cd2ee…75f2` = `content.sha256`;
- 2,372,954 bytes;
- `docProps/app.xml` gives 168 pages.

I wrote my own walk of `word/document.xml` (`docx_paras.py`). It yields 2,410 paragraphs and table rows, each with its paragraph style, and each row's cells are joined with ` | `. I did not use the extractor's `.md` capture.

The scripts are in the scratchpad:

- `sdl52_rows.py`: verbatim check, row-aware;
- `sdl52_modal.py`: lowercase-modal completeness walk;
- `sdl52_add.py` and `sdl52_write_add.py`: build the added entries;
- inline locator checkers.

## Pass 2: verify

1. **Hash and currency.**
   - The hash matches. ✔
   - Download Center page id 29884, fetched 2026-10-03, still serves the same file at the same size, with "Date Published: 7/15/2024" and file version 1.
   - The SDL Resources page lists the document under "Legacy archive" (see `microsoft-sdl` verification).
   - The title page reads "SDL Process Guidance Version 5.2 / May 23, 2012".
   - Licence: front matter reads "© 2012 Microsoft Corporation. All rights reserved. Licensed under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported". **CC BY-NC-SA 3.0 is confirmed.** ✔ The front matter also says "You may copy and use this document for your internal, reference purposes."
2. **Verbatim (510/510).**
   - All 268 `item`/`paragraph` texts from the extract pass are strict contiguous substrings of the XML text once list markers are stripped. So there are no splices, and the nested items really are adjacent to their parents.
   - For all 140 table rows (tool, agile, firewall, table), every cell value was found in a single source table row.
   - The 102 entries I added come straight from the XML and also pass.
3. **Locators (510/510).**
   - Every entry's heading path was checked against the docx heading stack at the paragraph that holds its text.
   - 11 tool rows looked wrong at first, because identical tool names recur in the Win32, Win64 and CE tables. A table-aware recheck confirmed all 32 tool-row locators.
4. **Completeness: the main finding.** This is the lowercase-modal failure the brief warned about.
   - The extract pass's baseline was "statements under the headed Security/Privacy Requirements/Recommendations sections + appendix tables + Agile tables".
   - Every docx paragraph carrying must/should/required/requires/need to/mandatory was walked. **102 normative statements outside those headings** were in neither `requirements.yaml` nor `normative.md`. The scoped-out Appendices A, C, K, L, M, N, O, U and V were excluded from this count, along with disclaimers, history, the worked Agile example narrative and a resources title.
   - Examples:
     - *"However, you must complete a Final Security Review before final release."* (Phase Five > Public Release Privacy Review)
     - *"The security advisor assigned to the release must certify that your team has satisfied security requirements. … your privacy advisor must certify …"* (Release to Manufacturing/Release to Web). This is the RTM gate itself.
     - *"You must complete threat modeling during project design."* (Phase Two > Risk Analysis)
     - *"Your team must be prepared for a zero-day exploit …"* (Release > Planning)
     - *"There must be well-defined criteria to determine when the push is complete."* (Security Push)
     - *"One-year cap. At a minimum, a product must meet SDL requirements that are older than one year at the time of release …"* (applicability)
     - *"Each member of a project team must complete at least one security training course every year. If more than 20 percent … the requirement is failed"* (SDL-Agile)
     - *"SDL-Agile requires the following tools to be run at least once per sprint …"*
     - Appendix D *Application Quality* ("… that wish to receive unsolicited traffic must:" plus 2 items) and *Least Privilege* ("Firewall rules must adhere to the principle of least privilege by:" plus 4 items)
     - SDL-LOB checklist items: input validation "must be applied at all identified entry points", HBI data at rest "needs to be encrypted", and others.
   - The extract pass's stated rule, that context paragraphs "with no modal word" are descriptive, was also broken: Appendix F, I and J and the Agile section paragraphs that **do** carry modal words had been left out.
   - Other counts:
     - `bin/bcp14-count` = 5. All five are caps-styled lowercase text, as the reconciliation says. ✔
     - The lowercase counts in the header (must 187, should 204, required 62, may 61) are case-sensitive counts on `.cache/microsoft-sdl-5-2.md`. Case-insensitive, they are 189/206/78/64.
5. **Typing.**
   - Normativity follows the source's own headings, which is acceptable.
   - Four entries from "Applying SDL Tasks to Sprints" (R-0177..R-0180) were labelled `variant: SDL (waterfall/spiral)`. That section belongs to "Security Development Lifecycle for Agile Development".
   - R-0161 (the FSR outcomes) is typed `process`, although it contains "must"/"should". It is kept whole, because it is a list of outcomes that the state machine models.
6. **Object model, state machine and protocol.**
   - All 18 quoted state-machine texts, 9 protocol texts and 13 object-model texts are verbatim.
   - The FSR outcomes (Passed / Passed with exceptions / FSR escalation / immediate failure) were checked word for word against the "Possible FSR Outcomes" list. ✔
   - **Defect:** the guard "No software release can pass an FSR with known vulnerabilities … Critical, Important, Moderate, or Low" sat on `passed → released`. It conditions *passing the FSR*. The real RTM guard is the advisor-certification sentence, which had been dropped entirely (item 4).
7. **Claims.**
   - "Changes in This Version" matches: the Design, Implementation and LOB counts, plus Appendix N "Updated guidance".
   - Appendix B enums: 15 causes and 8 effects. ✔
   - "security score of B or above" ✔. The A–F scale in the schema is marked inferred. ✔
   - The source inconsistency in design-notes OQ1 is real. The same R-0159 paragraph says "remove vulnerabilities that meet your organization's severity criteria" and then "No software release can pass an FSR with known vulnerabilities that would be considered as Critical, Important, Moderate, or Low."

### Defects found and fixed

| # | cat. | defect | fix |
|---|---|---|---|
| 1 | dropped | 102 modal-bearing normative statements outside the headed sections were missing, including the RTM certification gate, "must complete a Final Security Review before final release" and "must complete threat modeling during project design" | appended as R-0409..R-0510 (verbatim whole paragraphs; a lead-in ending ":" carries its list items; typed by strongest modal; `added_by` gives the docx paragraph index); `normative.md` Part III added; header counts (510 = 408 + 102; 311/188/9/2; 291/132/87), reconciliation, README, record coverage and summary updated |
| 2 | typing | R-0177..R-0180 had the wrong `variant` | set to `SDL-Agile`, with `variant_note` |
| 3 | object-model / state machine | FSR guard was on the wrong transition, and the RTM guard was missing | guard moved to `fsr-in-progress → passed`; `passed → released` now carries the verbatim advisor-certification guard and the "must complete a Final Security Review before final release" sentence |
| 4 | claims | summary said the download page date is "2012-05-23"; the page shows 7/15/2024 | corrected: the title-page date is 2012-05-23 and the page re-publication date is 2024-07-15 |
| 5 | claims | summary quoted "one work item per vulnerability", which is not in the source | replaced with the verbatim "Create an individual work item for each vulnerability listed in the threat model" |

## Pass 3: cross-check

- **Requirements ↔ schema.**
  - All 100 Appendix P–R rows in `examples/agile-requirement-tables.yaml` validate against `$defs/AgileRequirementRow`. The example's 100 rows equal the 100 `agile-row` entries.
  - `SecurityBugCause` and `SecurityBugEffect` enums equal Appendix B, and `Severity` equals the four FSR severities.
  - FSR fields named by requirements (security score, exceptions, sign-off) exist in `FSRRecord`.
- **State-machine triggers.** These are named events (sign-off, list of required changes, compromise, escalation, omission or neglect), each quoting source text. Protocol messages (information package, exception request/decision, sign-off/required changes, escalation, privacy sign-off) correspond to those transitions.
- **`maps_to`.** None; SDL 5.2 publishes no crosswalk. ✔
- **not_applicable.** Messages are N/A; the reason is true.

## Residual open issues

- **Not done:** design-notes OQ2 asks for each Appendix P–R Agile row to be linked to its main-body R-id. This needs a per-row judgement on the short titles, so it is left open.
- R-0409+ are appended out of document order. Their ids are stable, and each entry records its docx paragraph index.
- `expects_deliverables` on the added entries is empty. The extract pass derived deliverables by keyword, which is our own reading, and that was not repeated.
- Appendices C, K, U and V still contain modal statements. They are scoped out by the record's stated coverage: questionnaires and samples.
