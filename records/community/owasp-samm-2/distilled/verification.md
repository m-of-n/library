---
record: owasp-samm-2
kind: verification
title: "owasp-samm-2 — verify and cross-check passes (FX-1 passes 2 and 3)"
date: "2026-10-03"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# OWASP SAMM v2.2.0: verification report

The verifier did not do the extraction. Every check below ran against the
source files, never against the record's own rendering or summary. The source
files are:

- the release tarball `samm.tar.gz`, unpacked afresh into the scratchpad;
- the release toolbox `SAMM_spreadsheet.xlsx`;
- the OWASP mappings spreadsheet;
- the SAMM–SSDF OLIR workbook.

The scratchpad scripts are:

- `samm_verify.py`: entries against the model files;
- `samm_maps.py`: `maps_to` against the spreadsheets;
- `samm_norm.py`: `normative.md` in both directions.

## Pass 2: verify

1. **Hash and currency.**
   - `samm.tar.gz` hashes to `ec8dce3a…3b05`, which equals `content.sha256`. ✔
   - The three spreadsheets match the digests cited in `summary.md`.
   - `gh release list -R owaspsamm/core` on 2026-10-03 shows v2.2.0 as Latest (2026-07-06), with v2.1.0 before it.
   - The v2.2.0 tag resolves to commit `21352e0f…`, dated 2026-07-01.
   - `compare v2.1.0...v2.2.0` reports 115 `model/` files changed, +187/−186 lines. This matches `summary.md`. ✔
   - Licence: `gh api …/license` gives CC-BY-SA-4.0 (`license.txt` in the repository, not in the tarball).
   - The toolbox has three licence statements:
     - the heading says "Creative Commons Attribution-ShareAlike 4.0 License";
     - the next sentence says "Share Alike 3.0";
     - another sentence says "SAMM is licensed under … 4.0".
   - This inconsistency is recorded correctly in design-notes OQ 3. **CC BY-SA 4.0 is confirmed.** ✔
2. **Verbatim (415/415).** `samm_verify.py` loads every model file and compares exact strings, not substrings:
   - 30 stream `text` values = `description`;
   - 90 activity `text` values = `longDescription`, plus `title`, `benefit`, `shortDescription`, the practice-level objective and the stream link;
   - 295 quality-criterion `text` values = `quality[i]`, plus the `question` text and the parent.
   - **0 mismatches.**
   - A splice is impossible here because each `text` is one whole source field.
3. **Locators.**
   - Every file named in the 415 locators exists.
   - Each activity locator names its own file, and each stream locator names its own file.
   - Each quality-criterion locator `model/questions/<X>.yml quality[i]` was checked index by index (295 of 295).
4. **Completeness.**
   - Every string value of the 302 YAML files appears in `normative.md` (2,328 values). The only omissions are authoring metadata: `assignee` ×15, `model: SAMM20` ×5 and `logo` URLs ×5.
   - In the other direction, every substantive line of `normative.md` occurs in the source.
   - Unit counts recomputed from the files:
     - functions, practices, streams and levels: 5/15/30/3;
     - practice levels: 45;
     - activities: 90;
     - questions: 90;
     - quality criteria: 295, distributed 36×3, 27×4, 19×2, 7×5 and 1×6;
     - answer sets: 24.
   - **All counts match the header.**
   - `bin/bcp14-count .cache/owasp-samm-2.txt` = 0.
   - The lowercase forms (must 5, should 24, shall 0, may 32, ensure 60, required 13) are case-sensitive counts. "Ensure" in any case is 82.
   - SAMM is lowercase-modal. Because every activity's whole `longDescription` is carried, no `should`/`must` sentence can be dropped.
5. **Typing.** Everything is `kind: stated`.
   - The 18 activities that have a `personnel` field use it as the actor. The remaining 72 are flagged `actor_source: inferred`, which was checked against the files.
   - No normativity was weakened: SAMM has no mandatory form.
   - `phase` is declared to be OUR mapping.
6. **Object model.**
   - Object attributes were compared with the actual key sets of each document type. All match, except that Function's `model` field is carried as an edge, which is acceptable.
   - Edge cardinalities were checked: 15:1 at_level, 2:1 at_practice_level and 3:1 in_stream.
   - `related_to` (18 activities) was confirmed.
7. **Claims.** These were verified against the source:
   - the scoring formulas, cell by cell for all 15 practices: `Interview!J = SUM(H level1, H level2, H level3)`, `H = IFERROR(AVERAGE(stream A, stream B),0)`, `Scorecard!J14:J18 = AVERAGE` over 3 practices, and `J19 = AVERAGE(J14:J18)`;
   - **the claim that the practice score is summed across levels, not gated, is TRUE**;
   - the 3 scoring fixtures pass under `score.py`;
   - the attribution "created by Pravir Chandra";
   - the roadmap quote at Getting Started step 5.

### Defects found and fixed

| # | cat. | defect | fix |
|---|---|---|---|
| 1 | claims | design-notes OQ1 and summary.md said "two" TMC rows cite non-existent ids. There are **three**: `P-SM-1-B`, `P-SM-2-B` and `D-TM-3-B` (a typo for D-TA-3-B). Because of these, only 33 of the 36 TMC rows can attach as `maps_to`. | design-notes OQ1 and summary.md corrected |
| 2 | claims | The claim that `relatedActivities` says "may be related" in most files and "prerequisites" only in D-TA-2-A/B is wrong. The template comment reads "prerequisites to implement this one." in **54** files, "are related" in 18 and "may be related" in 18. Of the 18 populated activities, 13 carry "prerequisites". | design-notes OQ2, object-model `related_to` edge and summary.md Limits corrected |
| 3 | claims | `state-machine.yaml` said numeric scores "fall through to 0" in the Translated Value column. The formula `IF(C14=1,1,0)…` passes exact integers 1, 2 and 3; only non-integer scores give 0. | corrected |
| 4 | claims | The roadmap locator "Getting Started row 5" is really step 5 at cells B9:C9. | locator clarified |
| 5 | schema / source defect | "validates all 302 files" holds only under a YAML 1.2 loader. All 24 `answer_sets/*.yml` write the first option unquoted (`text: No`). PyYAML (YAML 1.1) reads it as boolean `false`, so jsonschema fails 24 of 302. With "No" restored, 302/302 validate. | noted in the schema `description` and in AnswerSet `values[].text`; README and record coverage qualified |

## Pass 3: cross-check

- **`maps_to` against the spreadsheets.** `samm_maps.py` rebuilt every link from the xlsx:
  - SSDF tab: 77;
  - BSIMM14: 125;
  - IEC 62443-4-1: 60;
  - CSF 2.0: 83;
  - Microsoft SDL: 47, with relationship text;
  - TMC: 36;
  - OLIR SSDF→SAMM activity rows, with the SSDF id forward-filled down merged cells: 81, with relationship text.
  - Expected total 509; the record has 506. The difference is exactly the 3 TMC rows whose SAMM id does not exist. Those rows are kept in `crosswalk.yaml` and are not attached.
  - **All 506 links match source, target and relationship.**
  - One OLIR row (V-ST-1-A → PO.4.2) has a blank relationship cell, which the record carries as `""`. This is faithful.
- **Target ids against the target records.**
  - **Microsoft SDL `10.1` does not exist** in `microsoft-sdl`. Practice 10 has no sub-practices, so OWASP's sheet invented "10.1 Provide security training". Notes were added on that `maps_to` entry and on the crosswalk row, and design-notes OQ5 was added.
  - Four BSIMM14 targets (SM2.2, SE2.2, CMVM2.1, CMVM3.7) are not BSIMM16 labels. BSIMM15 relabelled them to SM1.7, SE1.4, CMVM1.4 and CMVM2.4, and `bsimm-16` records this as `former_ids` from Table 9. They are kept verbatim because the framework is named "BSIMM14", and this is documented in design-notes OQ5.
- **Target editions.**
  - Named: SSDF 1.1, BSIMM14, NIST CSF 2.0.
  - "IEC 62443-4-1" carries no edition year. The mapping sheet itself gives none; it is presumably :2018.
  - "Microsoft SDL (current practice set)" is undated, as is the target.
  - These are recorded as residual issues.
- **Schema against examples.** The fixtures carry no schema-typed data. The answer-set fixture values equal the source (0/0.25/0.5/1).
- **State-machine triggers** are assessment events that the toolbox defines, not messages. No protocol or messages exist; they are N/A, and the reasons are true.
- **not_applicable reasons** were checked: SAMM defines no wire messages or inter-party exchange. ✔

## Residual open issues

- IEC 62443-4-1 targets are not edition-qualified in OWASP's source.
- Verb `imperative` on activities is approximate. Many `longDescription`s are indicative prose, which is harmless because normativity is `descriptive-practice`.
- `relatedActivities` semantics cannot be resolved from the source. Ask the SAMM project.
