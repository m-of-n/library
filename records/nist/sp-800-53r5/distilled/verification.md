---
schema: "library-verification/v1"
id: sp-800-53r5-verification
record: sp-800-53r5
type: verification
kind: verification
title: "sp-800-53r5 — verify pass over the partial extraction"
verified: "2026-10-02"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# Verification of sp-800-53r5 (verify pass only)

This record is `status: summarized`. It is partial and declares no FX-1 profile, so only the
**verify** pass is recorded. The question was whether its stated coverage, which is SA-3/4/8/10/11/15/17/24
with all enhancements, SI-2(7), and the SR-1..SR-12 base statements with enhancements listed by
id and title, is accurate and verbatim. A cross-check pass was not run, because no
schema/messages/protocol/state-machine artifacts exist to cross-check.

## Checks

| check | method | result |
|---|---|---|
| Hashes | `shasum -a 256` on the cached PDF, the OSCAL catalog and the 5.2.0 change-log PDF; `git hash-object` on the catalog compared with the GitHub `main` blob sha | PDF `fc63bcd6…c11ec6` ✔. Catalog `01f37cf9…c9bc062` ✔, identical to the current `main` blob (8ebe3c91). Change log `bc4e6267…a89a86` ✔ |
| Currency | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final (2026-10-02). OSCAL catalog metadata. `gh release list usnistgov/oscal-content` | Rev. 5 upd1 (2020-12-10) plus Release 5.2.0 (2025-08-27). No Rev. 6 draft. Catalog version 5.2.0, last-modified 2026-05-11. OSCAL Content v1.5.0 (2026-05-13) ✔ |
| Coverage | Enhancement counts read from the OSCAL catalog | SA-3 3, SA-4 12, SA-8 33, SA-10 7, SA-11 9, SA-15 13, SA-17 9, SA-24 0, giving **86** enhancements, 3 withdrawn (SA-4(4)→CM-8(9), SA-15(4)→SA-11(2), SA-15(9)→SA-3(2)). SR has 12 base controls and 15 enhancements. Entries: 8 + 86 + 1 + 12 = 107 ✔. Every SR `enhancements_listed_only` list matches OSCAL ids and titles ✔ |
| 5.2.0 additions | Read the change-log PDF | SA-15(13), SA-24 and SI-2(7) are new. SI-2(7) is "Identified as a gap from analysis of the NIST SSDF" ✔. SI-7(12) was revised, but it is out of scope and correctly not claimed |
| Verbatim (PDF) | 104 `text_source: pdf` texts, normalised to alphanumerics, checked as substrings of `pdftotext` and `-layout` renderings of the PDF | 104/104 ✔ |
| Verbatim (OSCAL) | 3 OSCAL-sourced texts compared with the OSCAL statement, rendered with `[Assignment: organization-defined <label>]` | SA-24 and SI-2(7) match. SA-15(13) deliberately differs: the OSCAL 5.2.0 statement is SA-15(12)'s text, a source defect. The record uses the statement from usnistgov/oscal-content PR #345 (opened 2026-09-24 by selenaxiao-nist, still open and unmerged, fixes #343; issue #304 is open). I read the PR diff and the text matches exactly ✔ |
| PDF vs OSCAL | difflib ratio over the 104 PDF texts, with parameter text stripped | 101 ≥ 0.97. SA-4(3) 0.94, SA-15(1) 0.965 and SR-10 0.968 fall below, because OSCAL restructures an assignment as a nested selection. The PDF wording was confirmed for all three |
| Titles / status / withdrawn targets | Compared with OSCAL for all 107 | 0 mismatches |
| `maps_to` (Related Controls) | Compared with OSCAL `rel: related` links, in order, for all 107 | 0 mismatches. The lists include the 5.2.0 related-control additions (e.g. SI-2(7) on SA-15 and SR-8) |
| Baselines | Compared with the LOW/MODERATE/HIGH/PRIVACY 5.2.0 profiles | 0 mismatches. The three new controls are in no baseline ✔ |
| Locators | All 107: family section number (§3.17 SA / §3.19 SI / §3.20 SR, confirmed in the PDF TOC and body) plus the control id. Statement position under its control heading was spot-checked for 19 base controls | ✔ |
| Object model | Locators and quoted fragments | 20 objects / 24 edges / 6 gaps. Locators are control ids or §2.x. 2 inferred edges are flagged |

## Defects found and fixed

1. **Count.** The requirements.yaml header said `native_counts.sa_enhancements: 87`, but OSCAL and
   the record's own coverage text both give 86. Fixed to 86.
2. **Typing (false testable reason, 34 entries).** The note "testable partial: organization-defined
   parameters must be assigned before the control is checkable" sat on 34 entries whose statement
   has no `[Assignment…]` or `[Selection…]`. Examples are SA-3(1), SA-4(1), SA-10(1)–(6),
   SA-11(1), SA-17 and SI-2(7). The reason was replaced with an accurate one, and `testable: partial`
   is kept pending review.
3. **Claim.** The header note said every PDF statement matches OSCAL at ≥ 0.97. Three fall below
   (above). The note now names them.

## Residual / open

- The record is partial by design. The Discussion, References and SP 800-53A objectives are not
  extracted, and neither are the SR enhancement statements. FX-1 does not apply while
  `status: summarized`.
- SA-15(13) depends on an unmerged upstream PR. Re-check it when #345 merges, or if NIST publishes
  a 5.2.0 PDF.
- object-model `ThreatModel` cites SA-15(5) (Attack Surface Reduction) alongside SA-11(2). That
  is related, but it is not a threat-model statement. Left for the human reviewer.
- Derived fields (phase, nature, obligated_party, expects_deliverables) are unreviewed.

Scripts: session scratchpad `verify/`. They are not committed.
