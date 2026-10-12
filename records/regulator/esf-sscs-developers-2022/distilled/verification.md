---
schema: "library-distilled/v1"
id: esf-sscs-developers-2022-verification
record: esf-sscs-developers-2022
type: verification
updated: "2026-10-03"
reviewed_by: ""
---

# esf-sscs-developers-2022 — verification (FX-1 passes 2 and 3)

Independent verifier (did not extract), 2026-10-02/03, effort max. Final requirement count: **490**.

## Method (scripts in the verifier's scratchpad; sources in `.cache/`, never committed)

- **Hash**: `shasum -a 256` of the cached bytes vs `content.sha256`.
- **Verbatim**: every `text` in requirements.yaml and every quoted span in normative.md (quote pairs
  split per line, ellipses split) normalised to lowercase alphanumerics (NFKC, so ligatures and
  hyphenation/whitespace drop out) and tested as a substring of the union of the cached `.txt`/`.md`
  captures. Misses re-tested with digits removed (footnote markers / page heads) and inspected by hand.
- **Locators**: every requirement whose locator carries a page was checked mechanically against
  per-page `pdftotext` output (printed-page offset determined per document); misses inspected by hand.
- **Completeness**: the source capture was split into sentences; every sentence not covered by an
  extracted text and carrying a modal/normative form (should/must/shall/required/recommend*/
  encourage*/urge*/need to/may) — plus, for ESF, imperative sentences — was reviewed by hand.
  Source normative-form baselines were recounted with `grep -o -w -i` and `bin/bcp14-count`.
- **Typing**: scan for shall/must texts typed below `requirement`; review of verb/actor/normativity.
- **Cross-check**: every `<record>#<id>` reference in the record (maps_to, constrained_by,
  state-machine locators, notes) resolved against the target requirements.yaml; state-machine
  triggers compared with messages.yaml names; examples validated against the schema (jsonschema,
  Draft 2020-12) where present; object-model edge endpoints and locators checked; `tmodel_mapping`
  names checked against ARCH-0001 v0.2.0 and design-log 0009.

## Results

| check | result |
|---|---|
| hash | match (72f5bb1f…34bf); media.defense.gov 403s scripts; SHA-1 matches 78 Wayback captures 2022-09-01 (publication day) … 2026-09-22 |
| currency | Part 1 (Developers), Aug 2022 is the current edition (no revision listed) |
| verbatim | 1015 spans checked; 0 real misses (3 residual checker hits are page breaks inside table rows / across p.34-35) |
| locators | 489 paged locators checked (printed = PDF − 4); pass-1 locators correct; R-0415 widened to p.46-47 |
| BCP 14 | bin/bcp14-count 19 = 18 extracted (App. C) + cover-title RECOMMENDED; confirmed |
| own forms | shall 2 / must 48 / should 173 / may 89 / will 23 / required 27 / encouraged 2 / recommend* 117 — recount confirms header |

## Defects found and fixed

**Dropped (27 added, R-0464..R-0490).**
- 19 §2 statements pass 1 missed because they carry no should/must marker or are permissions /
  list lead-ins: R-0464 (release-readiness tests may include…), R-0465 (training ideally by a central
  team), R-0466 (may reuse vetted modules, PW.4), R-0467 (check-in audit trail), R-0468 ("consider the
  following" lead-in), R-0469/R-0470 (production-branch access and builds), R-0471 (temporary SSH key),
  R-0472 ("At minimum, log the MFA ID…"), R-0473 ("avoid putting secrets in plain text… rotate
  secrets"), R-0474/R-0475 (hermetic "best effort is sufficient", container suffices), R-0476
  ("Advanced techniques may include:"), R-0477/R-0478 (customer may run binary SCA / keep monitoring),
  R-0479 (developer can include SBOMs in the package), R-0480 (**§2.5.3 activities "may be optional"
  if §2.5.2 measures are taken** — an exemption that changes the force of R-0377..R-0380), R-0481
  ("apply continuous monitoring" of the repository), R-0482 (lead-in).
- **Appendix C**: pass 1 extracted only the 18 uppercase sub-bullets and dropped the 7 SLSA row
  requirements and their **level applicability** (Scripted build L1-4, Build service L2-4, Ephemeral
  and Isolated L3-4, Parameterless, Hermetic L4, Reproducible L4 best effort): R-0483..R-0489; plus
  the Parameterless permission "(Default substitutions … are acceptable.)" R-0490.
- Initial page numbers on the additions were off by one (the verifier's own script read the next
  page header); corrected and re-checked mechanically.

**Typing.**
- **Weakened (fixed):** R-0306..R-0309 ("Must fetch… / Must not allow mutable references / Must verify
  the integrity / Must prevent network access") were typed recommendation / "(recommended mitigation)";
  R-0190 ("…must be preapproved, validated, and scanned…") typed recommendation/"ensure". All five
  restored to `requirement`.
- **Over-typed (fixed):** 33 descriptive sentences were typed requirement/recommendation because the
  heuristic fired on a keyword ("are required to compare and merge", "may require", "Most secure
  development processes recommend this practice", "It should also be noted…", "This ensures…") →
  `descriptive` (R-0001, 0002, 0004, 0031, 0044, 0092, 0095, 0096, 0098, 0117, 0124, 0127, 0129, 0136,
  0141, 0150-0152, 0191-0193, 0195-0197, 0216, 0217, 0233, 0283, 0312, 0313, 0323, 0357, 0372). Kept,
  not deleted, so keyword reconciliation still holds. R-0366/0370 → heading; R-0085 → informative;
  R-0232 → permission; R-0053/0070/0071 (list items under a "should include/address" lead-in) →
  recommendation; R-0225..R-0231 (SSDF alignment list) → crosswalk.
- **Phase (heuristic, improved):** pass 1 typed all of §2.1 `governance` and had only 1 `verification`
  entry. Re-assigned by subsection: requirements (3), design (17), verification (58), release (72),
  operations/response (25), training (30); checklist questions by keyword. Still derived — human review.

**Claims.** The header reconciliation said the unextracted 27th "required" was the §2-intro sentence;
that sentence is R-0001. The real residue is Appendix B row 2 "Provide given hashes as required"
(crosswalk.yaml). Fixed.

**Object model.** 27 objects / 21 edges checked (endpoints, locators). Added edge `meets_level`
(BuildEnvironment → SLSALevel, inferred, App. C). tmodel mappings consistent with ARCH-0001 v0.2.0.

**Cross-check.** maps_to → sp-800-218 (SSDF **v1.1**, the edition the guide cites in §2.1 "Alignment
with SSDF") ids all resolve. No schema/messages/state machine (N/A reasons true).

## Accident during verification (disclosed)

A header-rewrite regex in the verifier's script (DOTALL) truncated `requirements.yaml` to its header
on 2026-10-03. The file was rebuilt byte-for-byte from the extractor's own build script and data
(`laneb/esfbuild.py` + `esf-reqs.json` → 372 092 bytes, identical to the pass-1 size; every entry's
id/normativity/verb/phase/locator/text prefix compared equal to a dump taken before the edit), and
all pass-2 edits were re-applied by script.

## Residual / open

- actor/nature/phase/expects_deliverables remain heuristic (flagged in `note`).
- Appendix B colour coding (which role provides which dependency) is lost in text extraction;
  crosswalk.yaml lists the items without the role.
- normative.md italic type labels for pass-1 entries are not rewritten; requirements.yaml typing wins
  (stated at the head of the pass-2 section of normative.md).

