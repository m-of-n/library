---
schema: "library-distilled/v1"
id: eo-14028-verification
record: eo-14028
type: verification
updated: "2026-10-03"
reviewed_by: ""
---

# eo-14028 — verification (FX-1 passes 2 and 3)

Independent verifier (did not extract), 2026-10-02/03, effort max. Final requirement count: **53**.

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
| hash | match; re-fetched from govinfo.gov 2026-10-03 — identical |
| currency / amendment | Federal Register document API (2021-10460): disposition "See: EO 14141, January 14, 2025; EO 14144, January 16, 2025" — **no "Amended by"**; EO 14306's own disposition is "Amends: EO 13694; EO 14144". EO 14028 is in force and unamended. |
| verbatim | 106 spans; 2 checker hits = FR running head inside §4(u)-3 across a page break; 0 real misses |
| locators | 53/53 FR-page ranges correct |
| counts | §4 slice: shall 41 / must 1 / may 9 (2 = running head "May 17") — recount confirms |

## EO 14028 / 14144 / 14306 relationship (priority check, against the texts)

- EO 14144 builds on EO 14028 ("Building on the foundational steps I directed in Executive Order
  14028"); it does not amend it.
- EO 14306 amends only EO 14144 and EO 13694 (title, §1-§3, FR disposition). §1(a) strikes EO 14144
  §2(a)-(b) — §2(a) is the policy preamble, §2(b) the RSAA machine-readable attestation / CISA
  validation / public posting / FAR package. §2(b) replaces original §2(c) with re-dated SSDF
  directives (NCCoE consortium by 2025-08-01; SP 800-53 patch guidance by 2025-09-02; preliminary SSDF
  update by 2025-12-01, final within 120 days), dropping the M-22-18 incorporation and form-revision
  steps. EO 14306 cites EO 14144 by original numbering throughout (verified on §1(d), §1(e), §2(f),
  §2(g)), so these readings hold.
- The record's statements match; the requirements.yaml `source_version` said "amended in force" —
  corrected to "in force, not amended and not revoked".

## Cross-check

state-machine milestones reference eo-14028 ids that all resolve; realised_by chain to omb-m-22-18 /
omb-m-23-16 / omb-m-26-05 correct. N/A reasons (schema, messages, protocol, examples) are true.

