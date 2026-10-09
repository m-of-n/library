---
record: bsimm-16
kind: verification
title: "bsimm-16 — verify and cross-check passes (FX-1 passes 2 and 3)"
date: "2026-10-03"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# BSIMM16: verification report

**Source.** I made new renderings of `.cache/bsimm-16.pdf`, which hashes to
`d34e341f…dc2` = `content.sha256` and has 96 pp. I did not use the extractor's
`.md`. The renderings are:

- `pdftotext -raw`;
- `pdftotext -layout`;
- my own column crops: each page split at x=306 into left and right halves (`bsimm_cols.txt`).

**Comparison method.** All text comparisons normalise ligatures, soft and
end-of-line hyphens, quotes and whitespace. The scratchpad scripts are:

- `gen_verify.py`: substring check;
- `sent_check.py` and `split_check.py`: sentence-level check that tolerates page and column breaks;
- `splice_check.py` and `gap_check.py`: adjacency and gap content;
- `norm_check.py`: `normative.md`;
- an inline locator checker.

## Pass 2: verify

1. **Hash and currency.**
   - Hash ✔. `pdfinfo` gives CreationDate 2026-01-27 and 96 pages ✔.
   - The release was announced on 2026-02-04 in Black Duck's press release (news.blackduck.com). ✔
   - A web search on 2026-10-03 found no BSIMM17. The landing page still offers the BSIMM16 Report, so **BSIMM16 is current**. ✔
   - Licence: p.33 reads "THIS WORK IS LICENSED UNDER THE CREATIVE COMMONS Attribution-Share Alike 3.0 License … licenses/by-sa/3.0". **CC BY-SA 3.0 is confirmed.** ✔
2. **Verbatim (144/144).**
   - 105 texts are strict substrings. 19 more match once hyphenation and quotes are normalised. The other 20 cross a page or column boundary.
   - For those 20, `gap_check.py` shows that every gap between consecutive matched pieces is page furniture only: a page number ("60", "61", …) or the running head "BSIMM16".
   - **No sentence dropped, no paraphrase, no splice.** `splice_check.py` found 0 non-adjacent sentence pairs.
3. **Locators: all 144 checked.** Each activity label `[XXn.n:` was found on the stated page and column, and each domain or practice text on the stated page. 0 wrong.
4. **Completeness.**
   - Part 8 has 128 `[label: pct%]` headings, which is 128 unique labels. The 128 activities in the record match them exactly. Levels are 40/41/47 ✔.
   - Figure 18, parsed from p.56, has 128 rows. Every `observation.firms` and `percentage` in the record matches it. Every `header_percentage` matches its Part 8 heading.
   - `normative.md`: 148 text segments, all found in the source (0 unmatched).
   - `bin/bcp14-count` = 1, the pull-quote "MUST" on p.41. The reconciliation is correct.
   - Lowercase modals in the activity texts were recounted: must 29, should 23, required 11 ✔. They all sit inside whole activity descriptions, so none was dropped.
5. **Typing.** `descriptive-practice` throughout is honest. The report says it "descriptively observes, quantifies, and documents" (p.60) and that "the only goal of the BSIMM is to observe and report" (p.47). `actor` is flagged as inferred, with the p.5 terminology box as its locator. `level` equals the digit in the label for all 128.
6. **Object model.**
   - Stated edges were checked against their locators: p.5 terminology, p.45 levels and the dropped CR1.3, the relabelling quote on p.60, and the SM1.4/SM1.7/SM2.6 texts.
   - The claim that SM1.4 lists gates, guardrails and milestones as checkpoint kinds is verbatim.
   - Score and Evidence are correctly marked inferred.
7. **Claims.**
   - p.50 "For the first time, there have been no changes to the BSIMM framework this year" ✔.
   - "we added 16 firms and removed 26, resulting in a data pool of 111" ✔.
   - Table 3: 22 rows covering 16 distinct tasks. Table 4: 6 rows. Total 28 = `maps_to` ✔.
   - Figure 3: BSIMM is referenced by 39 of 42 SSDF tasks ✔.
   - Figure 8's example firm has 41 observed activities ✔.
   - CMVM1.1 = 106/111 and SM1.4 = 100/111 ✔.
   - **Claimed source defects, each checked:**
     - [SR2.2] heading 56.6% vs Figure 18 65/111 = 58.56%: TRUE.
     - [SE1.4] heading 62.1% vs 62.16%: TRUE. This is the only heading that truncates instead of rounding; SE2.5's 53.2% from 53.15% is ordinary half-up rounding.
     - Table 1 uses a denominator of 121 (CMVM1.1 87.6% = 106/121, SM1.4 82.6% = 100/121, SE1.2 79.3% = 96/121): TRUE.
     - Table 4 prints "PO5.2": TRUE.
     - "SDLC TOUCHPOINTS" vs "SSDL Touchpoints", and "SDLC toolchains" in Table 9: TRUE.
     - "Top 10 Activity in BSIMM15" legend on p.60: TRUE.

### Defects found and fixed

| # | cat. | defect | fix |
|---|---|---|---|
| 1 | claims | design-notes said the 121 denominator was "apparently the BSIMM15 pool size". The report's own arithmetic proves it (111 + 26 − 16 = 121, p.50). | design-notes defect bullet strengthened with the p.50 quote |

No verbatim, dropped, locator or typing defects were found.

## Pass 3: cross-check

- **Requirements ↔ schema.** All 128 activities validate against `$defs/Activity` (label pattern, practice, level, title, description). The Figure 8 example-firm scorecard (128 rows) validates against `$defs/FirmScorecard`, and its inferred score is 41.
- **Examples.**
  - `figure18-scorecard.csv` equals my parse of Figure 18 for all 128 rows (firms and percentage).
  - The Table 3 and Table 4 fixture rows equal the printed tables, with "PO5.2" kept verbatim.
  - `table9` parses 86 changes across 16 editions.
- **`maps_to`.** These target SSDF 1.1 task ids and name the edition. Table 4 is labelled unofficial.
- **Lineage, checked against `owasp-samm-2`.** SAMM's BSIMM14 targets SM2.2, SE2.2, CMVM2.1 and CMVM3.7 resolve through this record's `former_ids`. Table 9 lists them as BSIMM15 relabels to SM1.7, SE1.4, CMVM1.4 and CMVM2.4.
- **State machine.** The emerging→maturing trigger and text are a verbatim Figure 6 caption. The guard text is quoted from p.19. Activity-lifecycle guard: "intra-level standard deviation analysis and the trend in observation counts" (p.60) ✔.
- **not_applicable.** Messages and protocol are N/A; the reasons are true, since assessments are interview-based (p.45) with no defined exchange.

## Residual open issues

- Chart-only figures (9–13, 16–17, 19–38) are not extractable as data. This is accepted and documented.
- The `PO5.2` target is kept verbatim. A consumer must normalise it to PO.5.2.
