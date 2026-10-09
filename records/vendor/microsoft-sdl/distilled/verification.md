---
record: microsoft-sdl
kind: verification
title: "microsoft-sdl — verify and cross-check passes (FX-1 passes 2 and 3)"
date: "2026-10-03"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# Microsoft SDL (web practice set): verification report

## Sources and method

- **Pages checked.** The 16 cached pages in `.cache/lane-c/microsoft-sdl/*.html`.
- **Live re-fetch.** All 16 pages were fetched again on 2026-10-03 with a browser User-Agent. A plain curl request gets Akamai "Access Denied".
- **Text extraction.** The scratchpad parser `h2t.py` (stdlib `html.parser`, with script and style dropped) turned each page into text.
- **Requirement texts.** `mssdl_verify.py` normalised whitespace and NBSP/ZWSP, and removed the `- ` and `N. ` list markers that the extractor added when it rendered `<ul>`/`<ol>`. It then checked that each requirement text is a substring of a single page.
- **Coverage.** `mssdl_cover.py` checked the other direction: every line of more than 40 characters on each page was looked for in `normative.md`.

## Pass 2: verify

1. **Hash and currency.**
   - All 16 cached pages hash to the per-page digests in `summary.md`. ✔
   - The live 2026-10-03 fetch gives text identical to the cache on all 16 pages (0 differing lines), so the practice set is unchanged.
   - The SDL-for-AI blog post (2026-02-03) was checked. Its author is Yonatan Zunger, and it names six focus areas and promises guidance "in the coming months". It does not change the 10-practice web set. ✔
2. **Verbatim (73/73).**
   - 70 texts are exact substrings of one page, after list markers are stripped.
   - The other 3 (2.1, 3.3, 6.3) were checked line by line, and every segment is verbatim. They fail as whole strings for two reasons:
     - resource-link lines that sit between paragraphs were moved to `resources`, which is documented in the header note;
     - 3.3 contains the STRIDE table rendered in Markdown.
   - No splices.
3. **Locators.** All 73 were checked. Each text was found only on the page that its practice number or locator names: stages on the practices index, `n.x` on page p0n.
4. **Completeness.**
   - Every page line missing from `normative.md` falls into one of these groups:
     - resource-link titles (e.g. "Microsoft Learn: …");
     - tool-table blurbs;
     - navigation ("See Practice …", "Back to …");
     - index-page practice titles, which appear in `normative.md` under the practice-page title variant;
     - FAQ marketing prose.
   - No practice or sub-practice prose is missing.
   - Recounted from the pages: 10 practices; 48 sub-practices (4+5+6+4+4+6+7+10+2, practice 10 has none); 5 stage statements; 7 exception steps; 3 tracking reasons. All match.
   - `bin/bcp14-count` = 0.
   - Lowercase counts in the capture: must 33, should 45, never 7, required 10, recommend 2, ensure 26. All match the header.
5. **Typing.** This is where the lowercase-modal failure was found.
   - The header rule says normativity is `requirement` where the text contains "must", with `verb` set to the strongest modal.
   - The extract pass applied that rule to 9 entries, but **16 entries contain "must"**.
   - Six practice introductions (1, 3, 4, 6, 7, 10) were typed `recommendation` / `imperative (practice title)`. Examples: "Security requirements must be continually updated…" (1), "You must establish and apply sound cryptographic practices…" (4), "You must test applications…" (7), and five must-statements in practice 10.
   - Step 1.4-S2 ("which level of management must review the risk") was typed `should`.
   - Practice 10 has no sub-practices. Its must-statements were therefore visible only as a "recommendation".
6. **Object model.**
   - Stated edges were checked against their locators: the 3.4/3.5 work-item and testing text, the 3.3 threat fields and the 1.4 approver.
   - **Defect:** the `crosses` edge ran from DataFlowDiagram to TrustBoundary with an empty definition. The page says "Data that crosses a trust boundary…" and that the diagram depicts "subsystems, trust boundaries, and data flows".
7. **Claims.** All claims in `summary.md` and `design-notes.md` were checked against the pages and confirmed:
   - "not complete until you create work items";
   - the bug-bar quote;
   - 3.4's last paragraph repeated as 3.5;
   - the garbled practice-10 lead-in ("In particular, developers and the Since engineers…");
   - the FAQ's 12-practice list pointing to the Simplified Implementation;
   - Resources "Legacy archive" listing 5.2 and the Simplified paper;
   - the index "secure" vs "security" title variant;
   - the [link when available] placeholders.

### Defects found and fixed

| # | cat. | defect | fix |
|---|---|---|---|
| 1 | typing | 7 entries contain "must" but were typed `recommendation`, which weakens them | practices 1, 3, 4, 6, 7, 10 and step 1.4-S2 retyped `normativity: requirement`, `verb: must`, each with a `verification_note`; `counts.by_normativity` changed to 55/2/16; reconciliation and record coverage text updated |
| 2 | verbatim | STRIDE table rows read "S poofing", "T ampering", … in `normative.md` and the 3.3 text. This was a pandoc artefact: the HTML is `<strong>S</strong>poofing`, with no space. | 6 rows corrected in both files; the examples note corrected (it had claimed the page renders the split) |
| 3 | object-model | `crosses` was drawn from the wrong source object and had no definition | split into `depicts` (DataFlowDiagram→TrustBoundary) and `crosses` (data flow→TrustBoundary), both with verbatim definitions; Mermaid updated; edge count 17→18 in record, README and object-model.md |

## Pass 3: cross-check

- **Protocol ↔ state machine.** Every protocol message (ExceptionRequest, ExceptionDecision, ExceptionReview, ExceptionRenewalRequest) corresponds to a state-machine transition:
  - step 3 → requested;
  - step 4 → approved/denied;
  - step 6 → active→triaged;
  - step 7 → expired→requested.
- **State-machine and protocol text.** All 14 quoted texts are verbatim. Invariants are quoted from the 1.4 benefits and from tracking reason 3.
- **Examples.** All 57 strings in `examples/threat-modeling-examples.yaml` are verbatim lines of the practice-3 page.
- **Incoming `maps_to`.** `owasp-samm-2` maps 47 rows onto these ids. 46 resolve. `10.1` does not, because practice 10 has no sub-practice; this is annotated in `owasp-samm-2`.
- **not_applicable.** Schema and messages are N/A, which is true: the pages define no data format. The inferred exchange fields are in `protocol.yaml`.

## Residual open issues

- The pages are undated and silently editable. They were identical between 2026-10-02 and 2026-10-03.
- The `phase` values are our own mapping, not Microsoft's.
- Nested sub-lists, such as "Invite people of varied backgrounds, including:" in 3.3, are flattened in the Markdown rendering. The wording is verbatim, but the nesting is lost.
