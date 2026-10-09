---
schema: "library-distilled/v1"
id: cisa-secure-by-design-2023-verification
record: cisa-secure-by-design-2023
type: verification
updated: "2026-10-03"
reviewed_by: ""
---

# cisa-secure-by-design-2023 — verification (FX-1 passes 2 and 3)

Independent verifier (did not extract), 2026-10-02/03, effort max. Final requirement count: **152**.

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
| hash | match (774b82b1…83b6) |
| provenance | SHA-1 GDAMBS2U… = 102 of 105 Wayback captures of the official PDF URL (3 carry another digest, i.e. a different/older response) |
| currency | 2023-10-25 revision; co-sealer claims checked: CISA, NSA, FBI + 15 international partners listed on the cover (ACSC … NÚKIB), consistent with "8 new co-sealers" over April 2023 |
| verbatim | 335 spans; remaining checker hits are `[p. N]` page markers inside the capture and pdftotext ligature drops ("sofware", "afer") — the record's text restores the printed glyphs, which is correct; 0 real misses |
| locators | 152 checked; **3 wrong, fixed**: R-0056 p.14 → p.21 (Principle 2 "Demonstrating"), R-0059 p.14 → p.27 (Principle 3), P1-DEV-7 p.17 → p.18 |
| own forms | should 114 / must 8 / may 23 / recommend* 18 / urge* 5 / encourage* 11 — recount confirms; every unextracted occurrence matches the exclusions listed in the reconciliation |

## Typing

The guide is explicitly non-regulatory (Disclaimer); typing every entry `recommendation` even where
the sentence says "must" (R-0023, R-0054, R-0057, P3-3) is the documented choice and is accepted.

## Cross-check

maps_to holds only SSDF ids the source prints (SSDF v1.1 = sp-800-218); all resolve. Object model:
58 objects / 38 edges, endpoints valid, 2 inferred flagged; `tmodel_mapping` terms not in ARCH-0001
(Configuration, Incident, Metric, RiskAcceptanceDecision) are explicitly marked "new".

