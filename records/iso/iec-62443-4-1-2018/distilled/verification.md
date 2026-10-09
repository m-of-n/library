---
schema: "library-distilled/v1"
id: iec-62443-4-1-2018-verification
record: iec-62443-4-1-2018
type: verification
updated: "2026-10-02"
---

# Verification — IEC 62443-4-1:2018 (verify-only scope: paywalled, `status: summarized`)

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

**Sources.** All five hashed sources match their recorded sha256:
- IEC webstore preview, EN (11 pp) and bilingual (21 pp);
- iTeh sample (15 pp);
- ISASecure SDLA-312 v6.3;
- ISASecure SDLA-300 v1.9;
- ISASecure SDLA-102 v4.3.

**Verbatim.**
- `requirements.yaml`: **84/84** texts were found verbatim in ISASecure SDLA-312 v6.3, a public ISASecure
  document. The coverage note claimed 83/84 mechanically verified; the 84th is a page-break join and is also
  found. No text is attributable to the paywalled IEC body.
- `normative.md`: 88 quote segments, all found. The one miss is the Figure 2 role labels, transcribed from
  the preview image on p.10, which is labelled as such.

**Provenance.** Requirement texts come from ISASecure (public). The Clause 1-2 and Introduction quotes come
from the IEC webstore preview. Terms 3.1.1-3.1.17 come from the **iTeh Standards sample**.
- iTeh is the sales platform of SIST, the Slovenian national standards body. It is an authorised-distributor
  preview, not pirated, but it is **not** one of the sources the lane brief named (ISO OBP / IEC webstore /
  ISASecure).
- Paul should decide whether iTeh samples are acceptable. If not, the 17 terms must be dropped or re-sourced.

**Coverage notes.** Honest. Clause 4 (maturity model, Table 1), the rationale subclauses and Annexes A-B are
declared unread. The ML1-ML4 state machine is flagged as inferred from secondary sources.

**Not checked.**
- The CENELEC EN IEC 62443-4-1/prAA status claims in summary.md: a secondary webinar PDF, not re-opened.
- Object-model edge endpoints: three edges use composite or qualified endpoint labels (`reviews`,
  `gated_by`, `certifies`). This is cosmetic, left for the extraction owner.

**Defects fixed:** none needed beyond the record.yaml YAML-style conversion (inline `{…}` items and trailing
comments → block style, because `bin/_yaml.py` misparses both).
