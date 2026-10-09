---
schema: "library-distilled/v1"
id: iec-81001-5-1-2021-verification
record: iec-81001-5-1-2021
type: verification
updated: "2026-10-02"
---

# Verification — IEC 81001-5-1:2021 (+ ISH1:2025) (verify-only scope: paywalled, `status: summarized`)

By: claude (independent verifier, did not extract). Effort: max. Date: 2026-10-02.
**Scope set by the coordinator.** This pass checked three things:
- every extracted statement is truly from the free material cited;
- the coverage notes are honest;
- nothing was taken from unofficial or pirated copies.

A full FX-1 verify (locators, completeness against the paywalled body) is impossible without the standard.
**Method.** Scripted substring checks with normalised whitespace, hyphenation and punctuation, using the
session scratchpad scripts `vcheck.py` and `ncheck.py`. They ran against `pdftotext -raw` of each cached
preview, and each preview was re-hashed against the recorded sha256.

## Findings

**Source.** The IEC webstore bilingual preview (30 pp) matches `content.sha256` (`b4d73b51…a96a58`).

**Verbatim.** 64 `text` fields were checked.
- **1 defect, fixed:** the Annex F entry's `text` was a composed string, "TRANSITIONAL HEALTH SOFTWARE (Annex
  F, normative: F.2 …; F.4 …)". It is now reduced to the verbatim ToC title "TRANSITIONAL HEALTH SOFTWARE",
  with a note. 64/64 now match.
- All 7 ISH1 statements are verbatim from the ISH1 text included in the preview.
- `normative.md`: 16 quote segments. One quote joins Foreword sentences with an explicit `[...]`, which is
  acceptable.

**Provenance.** IEC webstore preview only. No unofficial copy was used.

**Coverage notes.** Honest: 57 activities title-only with `normativity: unknown`, and the counterpart
mapping to 62443-4-1 is flagged `inferred`.

**Currency (claims). 1 defect, fixed.** The summary said "No amendment or second edition was found". ISO
open data (deliverables metadata, Last-Modified 2026-09-30) shows:
- IEC 81001-5-1:2021 at stage 90.92 (to be revised);
- **IEC/AWI 81001-5-1 Edition 2** (project 92904) at stage 10.99.

summary.md is corrected.

**Not checked.**
- The FDA recognition number 13-122 and the M/575 harmonisation date, both secondary sources as the summary
  already says.
- Object-model edges whose endpoints are external standards ("IEC 62443-4-1 requirement", "IEC 62304
  process") rather than objects. Cosmetic.
