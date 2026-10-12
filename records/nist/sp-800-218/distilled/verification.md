---
record: sp-800-218
kind: verification
title: "sp-800-218 — independent verify (FX-1 pass 2) and cross-check (pass 3)"
verified: "2026-10-02"
verified_by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# Verification — SP 800-218 (SSDF 1.1)

Independent adversarial pass over the lane-A extraction. Everything was checked against the
**source** (the PDF and NIST's official xlsx), never against `summary.md` or another artifact.
Scripts are in the session scratchpad (`v218/`): `xlsx_check.py`, `refpdf.py`, `reflayout.py`,
`rows.py` + `rowcheck.py`, `verbatim.py`, `normcheck.py`, `modals.py`, `t2.py`, `ids.py`,
`splitter.py`, `omcheck.py`, `omsupport.py`.

## 1. Source identity and currency

| check | result |
|---|---|
| `shasum -a 256 .cache/sp-800-218.pdf` | `617746e5…cde22` = `content.sha256` ✓ |
| official xlsx re-downloaded from CSRC 2026-10-02 | `f5729c4c…bd55` = cached copy ✓ |
| pages (`pdfinfo`) | 36 ✓ |
| https://csrc.nist.gov/pubs/sp/800/218/final | SP 800-218 SSDF 1.1, Feb 2022, final; supersedes CSWP 13 (04/23/2020); authors Souppaya, Scarfone, Dodson ✓ |
| https://csrc.nist.gov/pubs/sp/800/218/r1/ipd | SSDF 1.2 IPD, 2025-12-17, comments closed 2026-01-30 |
| `/r1/final`, `/r1/2pd`, `/r1/fpd` | HTTP 404 → no final or second draft |
| https://csrc.nist.gov/projects/ssdf | updated April 13, 2026; still presents 1.1 as final |

**Result:** the record tracks the current final edition (1.1) as of 2026-10-02. Note: the final
page also offers `sp800-218-potential-updates.xlsx` (sha256 `a01878f0…094d`), a NIST worksheet
of candidate changes, not a new edition; not ingested.

## 2. Verbatim

Method: three independent haystacks — (a) the official xlsx, (b) `pdftotext` of the PDF,
(c) a word-coordinate reconstruction of Table 1 from `pdftotext -bbox` (columns split at the
measured x-boundaries, rows anchored on the y of each task id, header bands and margin text
removed). Every `text`, every example and every `maps_to.source_text` was compared after
whitespace collapse; a match that needed hyphen removal or digit removal (footnote markers) is
counted separately.

| item set | n | exact | needed hyphen-strip | needed marker-strip | miss |
|---|---|---|---|---|---|
| groups/practices/tasks/examples vs xlsx | 4 + 19 + 42 + 198 cells | all | — | — | 0 (1 deliberate deviation, below) |
| References cells vs xlsx | 528 lines | 528 | — | — | 0 |
| References vs PDF, per task row (layout) | 42 rows | 42 | — | — | 0 |
| requirements.yaml texts vs PDF row reconstruction | 777 | 772 | 0 | 5 | 0 real (16 reported misses all traced to the bbox parser: right-edge practice words crossing the column boundary, interleaved footnote text, one y-sort swap in PW.7.1; each confirmed by eye in `pdftotext -layout`) |
| normative.md quoted statements vs PDF | 845 | 836 | 1 | 5 | 0 real (2 are front-matter labels, 1 is the PO.3.3/E4 footnote-interleave artifact) |

**Spliced quotes:** none. Every multi-sentence quote is a contiguous substring of the source.

**Defects found and fixed**
- RV.1.1/E1 carried "databases **,** security" with a stray space — inherited from the xlsx,
  which leaves a blank where footnote marker 9 sits. The PDF reads "databases⁹, security".
  Fixed in `requirements.yaml` and `normative.md`. This is now the only cell that deliberately
  differs from the xlsx (noted in the requirements header).
- `normative.md` §1: two quotes had the locator "(footnote 1)" / "(footnote 2)" **inside** the
  quotation marks. Moved outside, into the locator.

## 3. Locators

- All 42 task rows and 5 retired rows: each task text was found in its own row of the PDF table
  reconstruction, and each row's References lines in its own row (counts per row equal). This
  covers every `§2 Table 1, practice X, task X.n.n` locator.
- 31 prose quotes (Executive Summary, §1, §2): each falls between the matching section
  headings in the PDF. 0 out of section.
- Table 2 (Appendix A): the 15 rows re-parsed from the PDF; the inverse
  (task → 4e subsections) equals every `EO14028-Table2` maps_to entry. 0 mismatches.
- **Defect fixed:** footnote 5 ("Provenance is …") was located "on PS.3 practice text". The
  bbox scan shows the only superscript 5 sits after "provenance" in **PO.1.3 Example 4**
  (p. 6). Fixed in `normative.md`, `object-model.yaml` (ProvenanceData) and
  `design-notes.md`. Footnote 7 was located at "PO.5.1 Example 10 / PO.5.2 Example 7"; the
  marker is only at PO.5.1/E10 (PO.5.2/E7 uses the term without a marker). Fixed.

## 4. Completeness

Native baseline (re-counted from the PDF and xlsx, independently of the header):

| unit | source | extracted |
|---|---|---|
| groups | 4 | 4 |
| practices | 19 active + PW.3 retired | 20 |
| tasks | 42 active + 5 retired | 47 |
| notional examples | 198 ("Example n:" occurrences in the reconstructed column) | 198 |
| reference lines | 528 (scheme-prefixed lines in the column) | 528 |
| reference ids (split by the README rules; `splitter.py` reproduces all 528 splits) | 1,483 | 1,483 |
| Appendix A Table 2 rows | 15 | 15 |
| Table 1 footnotes | 5 (5–9) | 5 (now also in requirements.yaml) |
| framework-level "should"/"necessary" statements outside Table 1 | 8 | **0 → 8** |
| BCP 14 (`bin/bcp14-count`) | 0 | 0 |
| lowercase `should` in whole PDF | 36 | 33 in normative.md body; the 3 not extracted are FISMA authority boilerplate (2) and the abstract ("should help") |

**Defects found and fixed**
- **Dropped requirements:** the eight framework-level statements (Executive Summary: integrate
  the SSDF / consult the references / adopt a risk-based approach; §1: integrate practices
  throughout the SDLC / factors should be considered / tenant should establish an agreement; §2:
  adopters should define terms / enumerating environments is necessary) were in `normative.md`
  but absent from `requirements.yaml`, although the sibling record `sp-800-218r1` extracts them.
  Added as `sp-800-218#R-0001..R-0008` (numbering aligned with `sp-800-218r1`), verbatim from
  the 1.1 PDF, with page locators (p. vi, 1, 3, 4). Entries 71 → 79; header `counts`,
  `native_counts`, reconciliation, `record.yaml` coverage, README and summary updated.
- **Claimed but absent:** the requirements header said footnote markers were "listed in
  footnotes", but no entry carried them. Added `footnote {number, anchored_at, text}` to
  PO.1.3 (5), PO.3.3 (6), PO.5.1 (7), PS.1.1 (8), RV.1.1 (9), verbatim.

## 5. Typing

- `normativity: recommendation`, `verb: should` throughout. Nothing was weakened: the source
  has no shall/must in Table 1 (the one `shall` is FISMA boilerplate; the 4 `must` are inside
  task/example texts, e.g. PO.3.1 "must or should be included", kept verbatim).
- `testable`: 25 yes / 17 partial on active tasks (matches the design-notes claim). Unquoted
  `yes`/`no` follow the library exemplars.
- `kind: stated` everywhere; the 8 added framework entries are stated. `actor`/`phase` are
  marked DERIVED in the header — sane on the sample (PO → governance, PW.1 → design,
  RV → operations/response, PS.2/PS.3 → release).

## 6. Object model

- Mechanical: 82 objects / 82 edges; every edge endpoint is a defined object; every locator id
  (task, practice, `/En`) exists; every item has a `tmodel_mapping`. 1 object + 2 edges are
  `inferred` and honestly so (ConformanceRecord; `runs_in`, `conforms_to`).
- Semantic sample (25 items, the ones whose names did not lexically match their cited text):
  each re-read against the cited task/example. All supported. Borderline, left as stated:
  `signed_with` IntegrityVerificationInformation → CodeSigningCertificate (PS.2.1/E2 names CA
  code signing, signatures being the integrity information).
- `tmodel_mapping` checked against ARCH-0001-PROPOSAL v0.2.0 §2b (Party, relational roles as
  edges), §3b (LifecyclePhase; PracticeGroup correctly **not** mapped to it), §4 (Assertion /
  supply-chain provenance deferred to ADR-0001), §5 (MitigationInstance, Review) and DL-0009
  (Gate, Requirement, WorkProduct, Evidence). Consistent.
- Fixed: ProvenanceData locator (footnote 5 anchor, see §3).

## 7. Claims in summary.md / design-notes.md

Checked against the CSRC pages, the PDF and the referenced records: dates, authors, "supersedes
CSWP 13", 36 pp, 4/19/42, 29 schemes, "NISTCSF ids for 14 tasks", "gates appear once
(PO.1.2/E2)", "17 of 42 partially testable", quoted example texts (PS.1.1/E3, PW.6.2/E4,
RV.2.2/E1, PW.1.2/E3, PO.4.2/E4, PO.3.2/E7, PO.4.1/E3), MAP-0001 rows 3 and 15, PW.1.1's
BSIMM/IEC references — all correct.

**Fixed**
- design-notes: "SP 800-53 Release 5.2.0 added SI-2(7) *because* of SSDF RV.3" overstated the
  attribution. 5.2.0 marks SI-02(07) "Identified as a gap from analysis of the NIST SSDF" (record
  `sp-800-53r5`); the RV.3 link is the 1.2 IPD's RV.3.3 → SI-02(07) mapping. Reworded.
- record.yaml `cites`: `microsoft-sdl` was cited for `[MSSDL]` (2021 web page, 12 numbered
  practices); the library record is the 2024 10-practice set, a different edition, so MSSDL ids
  do not resolve against it. `sp-800-161r1` was cited for `[SP800161]`, which SSDF 1.1 cites as
  the Rev. 1 **second draft**. Both changed to `{ref, title}` entries naming the edition gap.
- Counts in record.yaml / README / summary (71 → 79 entries).

## 8. Cross-check (pass 3)

- **schema / messages / protocol / state-machine / examples:** all N/A. Each reason was checked
  against the text: no data format or wire structure anywhere; PS.3.2/E1 "preferably using
  standards-based formats" is the only format mention; §2 "is not intended to imply the sequence
  of implementation" (no lifecycle); §2 "No examples or combination of examples are required"
  (examples are not test vectors). Reasons are true.
- **maps_to targets use the target's own ids:** yes — ids are NIST's verbatim References tokens,
  which are the target documents' native identifiers (BSIMM activity ids, SAMM stream ids,
  62443-4-1 practice ids, SP 800-53 control ids, ISO clause numbers, NICE TKSA ids).
- **Target edition named:** previously only implicit in `cites`. **Fixed:** added a
  `reference_editions` map to `requirements.yaml` (30 keys incl. EO14028-Table2: cited edition +
  `target_record` only where the library holds that edition + `library_holds_other_edition`
  where it holds a different one), and `edition`/`target_record` on every scheme in
  `crosswalk.yaml`.
- **crosswalk.yaml** rebuilt independently from `requirements.yaml`: all 30 scheme pivots and
  every `by_id` inverse index identical; `tasks_citing` counts correct.
- **Source inconsistency recorded (not papered over):** RV.2.2's References cell gives
  `EO14028: 4e(iv), 4e(vi), 4e(viii), 4e(ix)` (PDF = xlsx) but Appendix A Table 2 lists RV.2.2
  under 4e(iv), **4e(v)**, 4e(viii). The only task where the two EO 14028 mappings disagree.
  Both kept verbatim; noted on the RV.2.2 entry.

## 9. Residual open issues

1. `maps_to` resolution into held library records needs normalization: SP 800-53 ids resolve
   78/86 into `sp-800-53r5` (that record holds an SA/SI/SR subset); ISO 27034/29147/30111 clause
   numbers resolve 0/27 because those records key requirements as `<clause>-Rnn`. This is a
   cross-record convention gap, not an extraction defect.
2. `actor`, `nature`, `phase`, `expects_deliverables`, `verification`, `testable` remain derived
   and need human review (`reviewed_by` empty on every artifact).
3. The NIST "potential updates" xlsx on the final page was not ingested.
