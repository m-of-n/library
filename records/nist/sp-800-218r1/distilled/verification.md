---
record: sp-800-218r1
kind: verification
title: "sp-800-218r1 — independent verify (FX-1 pass 2) and cross-check (pass 3)"
verified: "2026-10-02"
verified_by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# Verification — SP 800-218r1 ipd (SSDF 1.2, Initial Public Draft)

Independent adversarial pass over the lane-A extraction, including an independent
re-derivation of `diff-vs-v1.1.md`. Everything was checked against the **source** PDF (and, for
the diff, against `sp-800-218`, which this same pass re-verified cell by cell against NIST's
xlsx and the 1.1 PDF). Scripts are in the session scratchpad (`v218/`): `rows.py` +
`rowcheck.py`, `normcheck.py`/`normcheck2.py`, `modals.py`, `ids.py`, `splitter.py`,
`editions.py`, `mydiff.py`, `omcheck.py`, `port.py`/`porte.py`. The extractor's own scripts
(`r1_*.py`) were **not** reused.

## 1. Source identity and currency

| check | result |
|---|---|
| `shasum -a 256 .cache/sp-800-218r1.ipd.pdf` | `0f40af24…a8d000` = `content.sha256` ✓ |
| pages (`pdfinfo`) | 57 ✓ |
| https://csrc.nist.gov/pubs/sp/800/218/r1/ipd | "NIST SP 800-218 Rev. 1 (Initial Public Draft)", published December 17, 2025, comments due January 30, 2026 (closed); supplemental material: SSDF project page only (no 1.2 xlsx) ✓ |
| authors | page lists Booth, Ogata, Kent, Souppaya, Dodson; the PDF title page orders Booth, Ogata, Souppaya, Kent, Dodson — the record follows the PDF ✓ |
| `/r1/final`, `/r1/2pd`, `/r1/fpd` | HTTP 404 |
| https://csrc.nist.gov/projects/ssdf | updated April 13, 2026; 1.1 still the posted final |

**Result:** still an Initial Public Draft on 2026-10-02; `maturity: draft`, `see_also` (not
`supersedes`) to `sp-800-218` is correct.

## 2. Verbatim

The IPD has margin line numbers, so plain `pdftotext` streams are unusable for substring checks
(26 false misses on a naive pass). Method: `pdftotext -bbox`, margin line-number words and
running heads dropped, Table 1 (PDF pp. 17–48) rebuilt as four columns at the measured
x-boundaries (190 / 320 / 508 pt), rows anchored on each task id's y, repeated header bands
removed; prose pages rebuilt in y/x order.

| item set | n | exact | marker-strip | miss |
|---|---|---|---|---|
| requirements.yaml task / example / reference texts vs their own table row | 796 | 792 | 4 (footnote markers 5, 8, 9) | 0 real (5 parser reports: footnote text interleaved at PS.2.1/E3 and RV.1.3; numbering check upset by markers) |
| framework R-0001..R-0008, groups, retired rows vs prose | 18 | 18 | — | 0 (R-0008 spans a page break; confirmed in layout text) |
| normative.md lines vs PDF | 788 | 774 | 5 | 0 real (9 reports: the conventions paragraph, the bullet list joined without bullet glyphs, and five footnote lines whose "Footnote n (…)" prefix the checker did not strip — each confirmed against the footnote text) |

Line-break hyphens: every hyphen kept at a PDF line end (`fault-`, `open-`, `third-`, `risk-`,
`organization-`, …) is a real compound; no false dehyphenation. **Spliced quotes:** none.

## 3. Locators

- Page locators on all 76 Table 1 practice/task entries (`p. N`) checked against the printed
  folio of the page holding the id: 76/76 (PS.4 and PW.5 begin at the foot of the cited page).
- Line locators on R-0001..R-0008 and the 4 groups re-read from the margin numbers: 12/12.
- Prose quotes placed in the right section (Executive Summary / §1 / §2): 23 checked; 0 wrong
  (5 reports are the group bullets that occur verbatim in both the Executive Summary and §2).
- Footnotes 5–9 anchors confirmed by the position of the superscript glyphs: PO.1.3/E4,
  PO.3.3 task, PO.5.1/E10, PS.1.1/E5, RV.1.1/E1 ✓.

## 4. Completeness

| unit | source (re-counted) | extracted |
|---|---|---|
| groups | 4 | 4 |
| practice rows | 22 (21 + PW.3 retired) | 22 |
| task rows | 54 (49 + 5 retired) | 54 |
| notional examples | 225 | 225 |
| reference lines | 497 | 497 |
| reference ids | 1,548 with the `sp-800-218` split rules (was recorded as 1,504) | 1,548 |
| framework statements | 8 | 8 |
| BCP 14 (`bin/bcp14-count`) | 0 | 0 |
| lowercase `should` in PDF | 39 | 35 in normative.md body; not extracted: FISMA authority (2), abstract "should help" (1), patent call "should be addressed to" (1) |

**Defect fixed:** the four Executive Summary recommendation bullets ("Organizations should
ensure … / protect … / produce … / identify …", lines 155–163) and the "does not prescribe"
statement (164–165) were missing from `normative.md` (present in the 1.1 record). Added with
line locators. (They restate the §2 group statements, which are requirements entries, so no
requirements entry was added.)

## 5. Typing

`normativity: recommendation`, `verb` "should (group-level, §2); task text imperative" — never
weakened; no shall/must in Table 1. `testable` on active tasks: 12 yes / 37 partial.
`change_vs_v1_1` re-checked against the independent diff (§8): **fixed** four practices
(PO.1, PO.3, PS.1, PW.1) whose explanation was reworded but had an empty `change_vs_v1_1`, and
RV.1.1, which wrongly said "Example 1 reworded".

`maps_to.ids` **fixed**: 23 cells of prose-titled schemes (CNCFSSCP 9, SCAGILE 5, SCFPSSD 4,
SCSIC 4, SCTPC 1) kept comma-joined items as one id (e.g. `MAINTAIN, ASSESS`,
`Securing Build Pipelines—Verification, Automation, Controlled Environments`), unlike
`sp-800-218`, so 1.1↔1.2 id comparison and the crosswalk were inconsistent. Re-split with the
exact `sp-800-218` rules (the splitter reproduces all 528 1.1 splits); 1,504 → 1,548 ids;
header, record.yaml, design-notes updated.

## 6. Object model

- Mechanical: endpoints defined, every id in a locator exists, every item mapped — 0 issues.
- `tmodel_mapping` **fixed**: PracticeGroup said "maps loosely to LifecyclePhase (§3b)",
  contradicting the 1.1 model, MAP-0001 and this record's own design notes (§2 denies
  sequence). Now "NOT a LifecyclePhase", aligned with `sp-800-218`.
- **Missed objects/edges added:** the IPD retains every 1.1 task and example (additions are
  appended; no renumbering), yet the 1.2 model had 54 objects against 82 for 1.1. 32 objects
  (TrainingProgram, PSIRT, SecurityResearcher, CodeOwner, SecurityCheck, Metric, AuditTrail,
  TrustRelationship, HostingInfrastructure, CodeChange, ComponentRepository,
  ApprovedComponentList, StandardizedSecurityService, CodeSigningCertificate, ReleaseArchive,
  SoftwareDesign, DesignReview, DataClassification, SecureCodingPractice, CodeAnalysis,
  IssueTrackingSystem, ConfigurationSetting, VulnerabilityInformationSource,
  SecurityResponsePlaybook, RiskCalculation, Remediation, LessonsLearned, Attestation,
  ApprovedConfiguration, ReferenceDocument, Term, ConformanceRecord) and 48 edges were ported
  from the 1.1 model **after** checking each cited id in the 1.2 text (unchanged, or reworded
  with the concept intact); prose locators were rewritten to 1.2 line numbers; the 1.1-only
  Appendix A clause object/edge was not ported; four inverse duplicates were skipped. Now 86
  objects / 104 edges; 2 objects + 3 edges inferred. Counts updated in record.yaml, README,
  summary and object-model.md.
- Inferred items honest: CommunityProfile (the draft never says "profile" — confirmed by grep),
  SoftwareUpdate `updates` SoftwareRelease, and the two ported ones.

## 7. Claims in summary.md / design-notes.md / diff-vs-v1.1.md

Checked: dates, comment period, 57 pp, 404s, project-page date, EO 14306 quote (lines 58–61),
"keeps every 1.1 task id", 49 / 225 / 497, "NISTCSF20 only on PO.6", "PS.4 only SP 800-53 /
800-161", "Protect Software (PS)" (Table 1 group row, line 1121 of the layout text) vs "Protect
the Software (PS)" (§2), "Appendix C" in the Acknowledgments (line 121) vs Appendix B, the change
log text (lines 537–596), BSIMM/CNCF "Latest version available at".

**Fixed**
- summary: "26 reworded" examples → 25 (RV.1.1 Ex 1 is unchanged).
- design-notes: "stable from 1.0 through 1.2" was imprecise (ids were moved and retired in
  1.1); reworded to "every 1.1 id carries over; ids are never renumbered or reused".
- `target_record: microsoft-sdl` on all 18 MSSDL lines was wrong by the record's own rule:
  the draft cites "Microsoft (2021) Security Development Lifecycle" (12 numbered practices),
  the library record is the 2024 10-practice set. Removed; `cites` entry rewritten as
  `{ref, title}` stating the edition gap.
- `target_record` was missing on all 38 IEC62443 lines although the library holds the cited
  edition (`iec-62443-4-1-2018`); added, and `cites` now uses the record id.

## 8. diff-vs-v1.1.md — independent re-derivation

Recomputed from the two verified `requirements.yaml` files (`mydiff.py`), not from the
extractor's output:

| item | independent result | file said |
|---|---|---|
| new practices / tasks | PO.6, PS.4 / PO.6.1–6.3, PS.4.1–4.4 | same ✓ |
| practice explanations reworded | PO.1, PO.3, PS.1, PW.1 | same ✓ |
| task texts reworded | PO.4.1, PO.4.2, PO.5.2, PS.1.1, PW.1.1, RV.1.2, RV.2.1, RV.3.3 | same ✓ |
| examples added to existing tasks | 10 | same ✓ |
| examples reworded | 25 | 26 ✗ (RV.1.1 Ex 1: xlsx stray-space artifact, not a change) |
| examples removed | 0 | — ✓ |
| EO14028 lines removed | 42 | 42 ✓ |
| SP80053 | 35 changed + 7 added | "rewritten for all 42" ✗ |
| SP800161 | 25 changed + 10 removed + 1 added (PW.1.3) | "rewritten for 36" ✗ |
| 26 other schemes on pre-existing tasks | byte-identical | same ✓ |
| per-task SP 800-53 / 800-161 table (42 rows × 4 cells) | 168/168 cells match | ✓ |
| every verbatim old/new cell in the reworded tables | found in the respective record | ✓ |
| change-log claims (§6) | match Appendix B text | ✓ (RV.1.1 dropped from the "diff also finds" list) |

All three errors fixed in the file, and a re-derivation note added under **Method**.

## 9. Cross-check (pass 3)

- **schema / messages / protocol / state-machine / examples:** N/A; each reason re-checked:
  no format or table file (CSRC page offers none), no exchange or sequence (§2 lines 311–313),
  PS.4/RV.2 name lifecycles without states, examples are "not required" (§2 lines 302–303).
- **maps_to ids are the target's own ids** (NIST's verbatim tokens) ✓.
- **Edition named:** added `reference_editions` (29 keys: cited edition, `target_record` only
  where held, `library_holds_other_edition` otherwise). Every per-line `target_record` now
  agrees with it (0 disagreements).
- **Source inconsistencies recorded, not fixed:** "Protect Software" vs "Protect the Software";
  "Appendix C" vs B; change log lists 2 of 8 task-text changes; `[CNCFSSCP]` dated 2021 but
  linked to the v2 paper at a pinned commit (mapped to v2 per the URL; flagged in
  `reference_editions`).

## 10. Residual open issues

1. Resolution of `maps_to` into held records needs normalization: 1.2 uses zero-padded SP 800-53
   ids (`SA-08`) and only 105/287 resolve into `sp-800-53r5` even after un-padding (that record
   holds an SA/SI/SR subset); ISO clause numbers do not match the ISO records' `<clause>-Rnn`
   keys; `sp-800-161r1` has no requirements file.
2. Ported object-model items carry 1.1 definitions; a human should confirm none should be
   reworded for 1.2.
3. Derived fields (actor, nature, phase, deliverables, verification, testable) unreviewed.
4. Re-extract when NIST publishes the final.
