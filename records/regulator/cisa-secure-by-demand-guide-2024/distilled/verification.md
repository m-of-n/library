---
schema: "library-distilled/v1"
id: cisa-secure-by-demand-guide-2024-verification
record: cisa-secure-by-demand-guide-2024
type: verification
updated: "2026-10-03"
reviewed_by: ""
---

# cisa-secure-by-demand-guide-2024 — verification (FX-1 passes 2 and 3)

Independent verifier (did not extract), 2026-10-02/03, effort max. Final requirement count: **44**.

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
| hash | match (4efa7d2e…9edca) |
| provenance | SHA-1 PKCEW5XD… = all 20 Wayback captures of the official PDF URL |
| currency | Aug 2024 (PDF 2024-08-06); no revision found by pass 1; not contradicted |
| verbatim | 89 spans, 0 misses |
| locators | 44/44 correct |

## Defects found and fixed

- **Dropped:** "For further guidance, CISA encourages organizations to read … the Minimum Viable Secure
  Product, and CISA's Secure by Design Pledge." (p.1) → OV-4. Cause: the own-form baseline had no
  `encourage*` row (only exact "encouraged", 0), so both encourage* uses went uncounted; FI-1 was
  extracted, this one not. Added `encourage*: 2` to source and extracted forms; reconciliation updated.

## Cross-check

No maps_to (guide prints no item-level mapping; related_inferred flagged as lane judgement). N/A
reasons checked. Object model: 16 objects / 12 edges, endpoints and locators valid, 3 inferred flagged.

