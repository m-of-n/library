---
schema: "library-distilled/v1"
id: iso-iec-30111-2019-verification
record: iso-iec-30111-2019
type: verification
updated: "2026-10-02"
---

# Verification — ISO/IEC 30111:2019 (verify-only scope: paywalled, `status: summarized`)

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

**Source.** The iTeh sample (11 pp) matches `content.sha256` (`5a2f9235…08b8`).

**Verbatim.**
- 32/32 requirement texts were found in the preview.
- `normative.md`: 5 segments. The two flags are benign:
  - a Clause 3 sentence quoted with an extra "the" ("the terms and definitions"; the source omits "the") — **fixed** in normative.md;
  - a markdown table whose cells are individually verbatim.

**Coverage claim recounted** from line-level grep of the preview body (from Clause 4 on):
- shall 2: "ISO/IEC 29147 shall be used…" and "A vendor shall develop and maintain…";
- may 2;
- about 28 should.

This is consistent with the header (should 26 of 28 extracted, with 2 descriptive uses excluded).

**Provenance.** iTeh sample only. The "publisher-authorised" wording is corrected.

**Currency. 1 defect, fixed.** summary.md, record.yaml and design-notes said Edition 3 was "AWI, stage
20.00". ISO open data (Last-Modified 2026-09-30) shows **ISO/IEC WD 30111.2, stage 20.60**. Corrected in all
three files.

**Not checked.** Object-model edges with descriptive endpoints. Inferred and cosmetic.
