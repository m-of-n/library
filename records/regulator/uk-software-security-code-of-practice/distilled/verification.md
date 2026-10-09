---
schema: "library-distilled/v1"
id: uk-software-security-code-of-practice-verification
record: uk-software-security-code-of-practice
type: verification
updated: "2026-10-02"
---

# Verification — UK Software Security Code of Practice (+ NCSC APC, Implementation Guidance): passes 2 and 3

By: claude (independent verifier, did not extract). Effort: max. Date: 2026-10-02.
The checks were scripted against `pdftotext -raw` of the Code and APC PDFs and the IG capture. The scripts
are in the session scratchpad: `vcheck.py`, `ncheck.py`, `loccheck.py`, `omcheck.py`, `xcheck.py`.

## Pass 2 — verify

**Hash and currency.**
- The Code PDF matches `content.sha256` (`b0861856…811f`). It was re-fetched on 2026-10-02 and is
  identical.
- APC PDF: `5064391a…09fd`.
- The gov.uk content API confirms the dates and changes: first published 2025-05-07; last updated
  2026-01-15 (Ambassadors scheme note); 2025-11-28 (survey link). No new edition.
- The APC prints "Version 1.0, published 7 May 2025".

**Verbatim.**
- 165 `text` fields were checked: 0 real misses. Two IG gaps are link anchors in the HTML capture. No
  splices.
- `normative.md` blockquotes: all verbatim. The "off-the-shelf" lead-in is from IG page 7.

**Locators.** 32 were sampled (Code principles, glossary, APC claims, IG statements): 32/32 correct. The
APC two-column layout puts the principle label after the first claim line; the sample was checked by hand.

**Completeness.** Defects found:
1. **Dropped statement.** An APC "About this document" note was not extracted: "Vendors requiring
   independent audit of compliance with the code should contact any NCSC-approved cyber resilience test
   facility." It is **added** as `APC-ABOUT-01`, a recommendation, in `requirements.yaml` and
   `normative.md`. Entries: 165 → 166.
2. **Wrong baseline count.** The IG "will need to" count was recorded as 1; it is 4. Three are inside
   extracted texts and one is descriptive.
   - The APC modals were also never reconciled: should 4, may 5.
   - Both are now reconciled in the header.
3. **Figures not read.** The extraction said the APC claims trees are "images only". The APC PDF in fact
   prints only the theme headings. The NCSC web page serves four **SVG** trees whose node text is
   machine-readable.
   - **Fixed:** they are transcribed into the new artifact `apc-claim-trees.yaml`, with 68 claim nodes and
     21 strategy boxes. `parent` is inferred from the numbering; connector geometry is not parsed. SVG
     sha256 values are recorded per tree.
   - 43 nodes are identical to body claims and 2 are wording variants (2.1.1, 4.1.3).
   - **Source inconsistency found:** tree leaf 1.2.3, "Security requirements are shared with third party
     suppliers", has no body claim. Recorded in design-notes Q1.
   - design-notes, summary.md, object-model.yaml and the record.yaml not_applicable reason were corrected.

**Typing.**
- No weakening.
- APC claims are typed `conformance-claim` (indicative mood), which is honest.
- Theme-stem "shall" is carried in `governing_clause`.

**Object model.**
- 46 objects and 42 edges; all have locators.
- 2 inferred, flagged.
- The `refines` edge (claim tree) is now backed by data.

**Claims in summary.md.** The dates were checked against the gov.uk API. The other statements were checked
against the PDFs.

## Pass 3 — cross-check

- Requirement ids referenced by `protocol.yaml` and `state-machine.yaml` exist.
- Every protocol flow message is defined in `protocol.yaml` `messages`.
- State-machine triggers are free-text events, now catalogued in `state-machine.yaml` `events:` (15 events).
- `maps_to` (IG Appendix 1) targets `sp-800-218` and `slsa-1-2`, but the IG names those frameworks without a
  version. An `edition_note` now says the edition is our choice.
- The not_applicable reasons were checked; the examples reason was reworded for the claim trees.

## Residual open issues

- The claim-tree connectors ("Supports" / "Comments on") and the strategy-box attachment points are not
  parsed. A geometry pass over the SVGs would populate them.
- The SVGs are kept only in the verifier's scratchpad (hashes in `apc-claim-trees.yaml`). They should be
  re-fetched to `.cache/` by whoever re-runs the record.
