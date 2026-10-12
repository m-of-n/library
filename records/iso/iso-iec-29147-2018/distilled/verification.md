---
schema: "library-distilled/v1"
id: iso-iec-29147-2018-verification
record: iso-iec-29147-2018
type: verification
updated: "2026-10-02"
---

# Verification — ISO/IEC 29147:2018 (verify-only scope: paywalled, `status: summarized`)

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

**Source.** The iTeh sample (13 pp) matches `content.sha256` (`e433e9e1…a8c1`).

**Verbatim.** 3/3 requirement texts and 4/4 `normative.md` quote segments were found in the preview.

**Coverage claim recounted.** The preview body holds exactly three modal statements:
- "Vendors should adapt…" (Introduction);
- "a vendor should ideally develop policy…" (§5.2);
- "ISO/IEC 30111 shall be used in conjunction…" (§5.3.1).

The header is right. The other modals are Foreword boilerplate.

**Field names.** The `messages.yaml` field names were checked against the preview Contents: §7.4.2-7.4.17
(16 advisory elements) and §9.2-9.4 (policy elements) are all present. Every field is honestly marked
`inferred-from-heading`, and no paywalled content (types, required/optional) is asserted.

**Provenance.**
- iTeh sample only. "publisher-authorised" is reworded (see 27034-1): iTeh is SIST's sales platform, not the
  ISO OBP preview.
- The claim that the 2018 edition was never on the ISO PAS list was not re-checked.

**Currency.** ISO open data confirms stage 90.92 and ISO/IEC AWI 29147 Edition 3 (92945) at stage 20.00, as
the summary says.

**Not checked.** Object-model edges use list-valued or descriptive endpoints. These are inferred, flagged,
and cosmetic.
