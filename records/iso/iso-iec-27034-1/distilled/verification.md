---
schema: "library-distilled/v1"
id: iso-iec-27034-1-verification
record: iso-iec-27034-1
type: verification
updated: "2026-10-02"
---

# Verification — ISO/IEC 27034-1:2011 (verify-only scope: paywalled, `status: summarized`)

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

**Sources.**
- The iTeh sample (15 pp) matches `content.sha256` (`8e3d0f99…0768`).
- The normsplash preview (10 pp) matches the recorded `647b27f2…6c906`.

**Verbatim.**
- `requirements.yaml`: 15/15 texts are verbatim from the preview.
- `normative.md`: 49 segments. The 11 flagged misses are benign:
  - nine §0.5.x blockquotes render "heading — first sentence", joining the subclause title to its text;
  - two are editorial framing.

**Provenance.**
- iso.org and the ISO OBP were blocked (403) during extraction, so the **iTeh sample** and a **normsplash**
  preview were used.
- iTeh is SIST's sales platform. normsplash's publisher status was **not verified**.
- record.yaml, summary.md, README.md and normative.md called these "publisher-licensed". That overclaims,
  and the wording is **corrected** to "free sample distributed by iTeh Standards (SIST sales platform; not
  the ISO OBP preview)" and "publisher status not verified" for normsplash.
- No pirated copy was found.
- The TS 27034-5-1 XSD is ISO's own free electronic insert (standards.iso.org).

**Currency.** ISO open data confirms 27034-1:2011 at stage 90.93, and Cor 1:2014 exists.

**Coverage notes.** Honest. The preview stops after 3.2; Clauses 4-8 and the Annexes are declared unread.

**Defects fixed.**
- The provenance wording above.
- The record.yaml `content.note` was a folded (`>`) scalar, which `bin/_yaml.py` cannot read. It is
  flattened to one quoted line.
- Inline `{…}` items and trailing comments are converted to block style.
