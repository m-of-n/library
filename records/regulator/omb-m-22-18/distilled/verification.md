---
schema: "library-distilled/v1"
id: omb-m-22-18-verification
record: omb-m-22-18
type: verification
updated: "2026-10-03"
reviewed_by: ""
---

# omb-m-22-18 — verification (FX-1 passes 2 and 3)

Independent verifier (did not extract), 2026-10-02/03, effort max. Final requirement count: **58**.

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
| hash | match; re-fetched from bidenwhitehouse.archives.gov 2026-10-03 — identical; original whitehouse.gov URL returns 404 (claim confirmed) |
| currency | rescinded by M-26-05 (2026-01-23), verified from M-26-05 text and the OMB index |
| verbatim | 125 spans; 5 checker hits are footnote markers inside quotes (record notes say markers were omitted); 0 real misses |
| locators | 58/58 correct |
| completeness | uncovered modal sentences are the background paragraph, the descriptive EO sentence and the Appendix A table rows (documented as restatements) — no drops |
| typing | no shall/must weakened; II.1.d "shall be acceptable" typed permission is an acceptance rule — accepted |

## Defects found and fixed

- III.A.1 notes cited `omb-m-26-05#R-0003` for the inventory obligation → R-0005.
- summary.md attributed "weak conformance signal" to M-26-05 as "its own criticism"; M-26-05 does not
  say that. Re-worded as our assessment plus the verbatim M-26-05 rationale.

## Cross-check

All constrained_by / state-machine locators / maps_to resolve (0 dangling). State-machine triggers
are named events or messages; the terminal `rescinded` transition is supported by omb-m-26-05#R-0004.
messages.yaml fields for the attestation point to cisa-ssdf-attestation-form-2024 (field schema there).

