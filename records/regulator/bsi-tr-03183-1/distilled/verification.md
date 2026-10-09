---
schema: "library-distilled/v1"
id: bsi-tr-03183-1-verification
record: bsi-tr-03183-1
type: verification
updated: "2026-10-03"
---

# Verification — BSI TR-03183-1 v1.0.0: FX-1 passes 2 (verify) and 3 (cross-check)

By: claude (independent verifier, did not extract). Effort: max. Run 2026-10-02/03.
Every check below was scripted against `.cache/bsi-tr-03183-1.txt` and fresh `pdftotext -raw` and default renderings of
the PDF, never against the summary. The scripts are in the session scratchpad (`verify-f/`): `vb.py`/`vb2.py`,
`vnm2.py`, `modal.py`, `secloc.py`, `bsi_add.py`, `om.py`, `xc.py`.

## Pass 2 — verify

**Hash and currency.**
- The cached PDF and a fresh download on 2026-10-03 both hash to `db5f5bfe…969ef`, matching `content.sha256`. 79
  pages.
- The landing page (bsi.bund.de/dok/TR-03183-en) labels the current Part 1 download "… Part 1: General requirements
  Version 1.0.0" and lists v0.9.0 and v0.10.0 as archive versions.
- **The 2026-07-31 date is confirmed.** The cover says "Date: 31.07.2026", and BSI's press release of **05.08.2026**
  ("Technische Richtlinie TR-03183-1 in Version 1.0.0 veröffentlicht") announces the release. The changelog's
  "2025-07-31" and the copyright "2023 - 2025" are source typos.
- Two summary and design-note claims could not be reproduced and were removed: that the current download link was
  labelled "Version 0.10.0", and a server Last-Modified of 2026-07-31 (the server returned no Last-Modified).

**Verbatim.** Contiguous substring checks after normalisation, with page furniture (running heads, page numbers)
removed.
- `requirements[].text`: 94/94 pass (79 original and 15 added).
- `normative.md`: 470 lines checked. The remaining misses are editorial notes, the "Reference CRA" lists joined with
  commas, and the Annex D formula line whose second half is the D.1 bullet text (verbatim at source line 3779).
- No splices found.

**Locators.** All 94 entries were resolved to a source line and the nearest heading (`secloc.py`). Every RH control
sits in its "Control" sub-clause, and every R-NNNN in its stated section. Each ER/VH row sits in Appendix B Tables 8–10.
0 locator defects.

**Completeness. This is the main defect.** `bin/bcp14-count` = 23, and the reconciliation (9 §4.4 definitions, 1
descriptive, 13 extracted) is correct. But the TR's lower-case obligations ("has to", "should", "must") were only
partly extracted. A sentence-by-sentence modal walk of §4–§7 and Annexes C–D found **15 dropped prescriptive
sentences**, now added as R-0031…R-0045 (`kind: inferred`, `added_by` set):

| id | where | dropped sentence (start) |
|---|---|---|
| R-0031 | §4.6 | additional guidance "has to be used for assessing the control" |
| R-0032 | §5.6 | "Risk handling has to find an appropriate balance …" |
| R-0033 | §5.7.1 | reasonably foreseeable misuse "has to be documented according Annex II CRA …" |
| R-0034 | §5.7.2 | architecture "should include:" (with its 4-item list) |
| R-0035 | §5.7.2 | third-party components: "has to exercise due diligence according to CRA Article 13 (5)" |
| R-0036 | §5.9.1 NOTE | analysis effort "should be put into perspective …" |
| R-0037 | §5.11.2.1 | "The manufacturer also has to meet and document the applicable requirements of Annex I Part I (2) …" |
| R-0038 | §5.11.3.2.1 | "the manufacturer has to take into account the capabilities of the user …" |
| R-0039 | §5.11.3.2.1 | "the integrating manufacturer has to exercise due diligence …" |
| R-0040 | §5.12.1 | tools or templates "is advisable" |
| R-0041 | §5.14 | decision criteria "should be defined on a … sectorial, organisational or PwDE level" |
| R-0042 | §6.2 step 4 | "If more than one value is given for an environment parameter, at least one must match." |
| R-0043 | §6.4 | the risk profile "also has to be evaluated based on the PwDE in scope …" |
| R-0044 | Annex D.2 NOTE | moderate risks "have to be treated during the course of development, but can be accepted in post-market …" |
| R-0045 | Annex D.2 NOTE | "High and very high risks are generally not acceptable and have to be treated." |

R-0044 and R-0045 are the classic lower-case drop. The extract pass took the NOTE's first obligation (R-0030) and
skipped the next two sentences. The full NOTE is now also in `normative.md`.

Not extracted, by decision: §3 restates CRA obligations (Art. 13/14/31) as an overview, and those are held in
`eu-cra-2024-2847`. Annex C sentences are illustrative restatements inside the worked example. Descriptive and
definitional uses were also left out.

Counts updated: entries 79 → 94, prose_obligations 30 → 45, requirement 74 → 85, recommendation 5 → 9, inferred
30 → 45. Updated in requirements.yaml, record.yaml, README.md and summary.md.

**Appendix B (CRA ER/VH mapping).**
- All 36 rows were re-read against the source tables. The ids, the CRA references as printed, and the verbatim text all
  match: ER.0–ER.14 (24 rows) and VH.1–VH.8a (12 rows).
- Source defects (no ER.3, ER.8 or VH.2; ER.14 truncated; VH.6a printed "Part II 4" for point 6) are recorded
  correctly.

**Typing.**
- RH controls: MUST ⇒ requirement, `stated`.
- R-NNNN: `inferred`, with the reason recorded.
- R-0002 had verb "is given" for "The evaluator needs …". Fixed to "needs".
- No normativity was weakened.

**Object model.** 40 objects and 26 edges, all with locators, and every edge endpoint is a defined object. Sampled
edges were confirmed against the source:
- evaluated_by (RH_RA.1.3 input "Acceptance criteria");
- maintained_by → OpenSourceSteward (§5.11.3.1.1, line 1923);
- provides_environment (§6.6);
- justified_non_applicable (RH_RT.1.1.2).

All are kind `stated`. Nothing invented was found.

**Claims (summary.md, design-notes.md).** The following were confirmed:
- §2 "does NOT establish any obligations"; 11 MUST activity controls.
- Control types Activity, Mechanism and Documentation with their PASS rules (§4.6).
- The N/A reasons.
- The OSCAL repository and access on request (Chapter 7).
- Table 1's repeated PII.Important row.
- §6.5 "amplifier of 1", the RDPS environment mislabel, and PII.Generic 3/2/3 in Table 1.
- Annex D "highly experimental" and the formula defect (round(1+x)·4 ∈ {4, 8}).
- The dangling [USER_DOCUMENTATION] and "REQ_RA 1.1.2".

The date claim was corrected as described above.

## Pass 3 — cross-check

- Every `constrained_by` id in messages.yaml, protocol.yaml and state-machine.yaml resolves (0 dangling). The 9
  messages and 9 derived schemas correspond 1:1.
- protocol.yaml flow P3 uses four CRA Art. 14 notifications that were not in messages.yaml. They were added as `events`
  (`content_prescribed: false`, with a note that the normative source is `eu-cra-2024-2847` Art. 14).
- **maps_to targets now use the target record's own ids.** All 73 CRA maps_to entries carry `target_id`
  (`eu-cra-2024-2847#AnnexI-PartI(1)`, `…AnnexI-PartI(2)(c)`, `…AnnexI-PartII(6)`, `…Art13(3)-1`), and all resolve.
  - VH.6a targets PartII(6), with a `target_note` that BSI prints "Part II 4".
  - RH_UPD.1's bare "Article 13(3)" targets Art13(3)-1, with a note.
- Examples: the D.2 matrix and the four vectors reproduce the source matrix exactly. The §6.5 ARC fixture values match
  the source. Some labels in the Annex C fixture are condensed (e.g. "might be accepted; not advisable"), but the values
  are traceable to C.6.
- `not_applicable: []` is correct, since every artifact is present.

## Residual open issues

- The OSCAL control catalogue (the TR's real control set) was not obtained, because access is on request. Until it is
  imported, the requirement set is the method, not the controls.
- State-machine triggers are prose, not event ids.
- Derived fields still need human review.
