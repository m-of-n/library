---
schema: "library-distilled/v1"
id: omb-m-23-16-verification
record: omb-m-23-16
type: verification
updated: "2026-10-03"
reviewed_by: ""
---

# omb-m-23-16 — verification (FX-1 passes 2 and 3)

Independent verifier (did not extract), 2026-10-02/03, effort max. Final requirement count: **37**.

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
| hash | match; re-fetched from bidenwhitehouse.archives.gov 2026-10-03 — identical |
| currency | rescinded by M-26-05 (2026-01-23) — confirmed from the M-26-05 text |
| verbatim | 80 spans, 0 misses |
| locators | 37/37 correct |
| completeness | uncovered modal sentences: background, "agencies must have access" (descriptive, documented), "modifies the deadlines by which agencies must collect" (descriptive), Appendix A rows (documented) — no drops |
| claims | "controls over M-22-18 where they conflict" — source: "…may be read to conflict with any provision of M-22-18, this memorandum is controlling" (p.1) — confirmed |

## Defects

None found requiring change.

## Cross-check

maps_to into omb-m-22-18 and sp-800-218 resolve; state-machine triggers are named events; messages
consistent with requirements (extension request, POA&M package).

