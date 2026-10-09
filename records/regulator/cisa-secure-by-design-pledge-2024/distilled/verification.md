---
schema: "library-distilled/v1"
id: cisa-secure-by-design-pledge-2024-verification
record: cisa-secure-by-design-pledge-2024
type: verification
updated: "2026-10-03"
reviewed_by: ""
---

# cisa-secure-by-design-pledge-2024 — verification (FX-1 passes 2 and 3)

Independent verifier (did not extract), 2026-10-02/03, effort max. Final requirement count: **72**.

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
| hash | match (3e9cd705…9bcb) |
| provenance | SHA-1 SS6PPK3G… = all 17 Wayback captures of the official PDF URL |
| currency | May 2024 PDF; web-page claims checked in the cached page text: "CISA does not enforce nor verify adherence to the pledge.", "hundreds of companies who have signed the pledge." — confirmed |
| verbatim | 148 spans; 1 checker hit is a mailto subject string; 0 real misses |
| locators | 18 paged locators correct; 54 locate by goal/section heading (7-page document) — acceptable |
| own forms | should 9 (PDF) / 11 (web), may 3, will 1, required 1, encouraged 4, recommend* 1 — recount confirms; the two unextracted "should" are descriptive (Goal 6 context) |

## Defects found and fixed

- **Cross-check:** state-machine transition reporting-due → reported used trigger `report-to-cisa`,
  which is not a defined message; renamed to the defined message `challenges-report`.

## Residual

- The progress-reports page claim ("60+ companies, latest July 2025") could not be re-fetched
  (archive returned an error page); left as pass 1 recorded it.

