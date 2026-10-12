---
schema: "library-distilled/v1"
id: omb-m-26-05-verification
record: omb-m-26-05
type: verification
updated: "2026-10-03"
reviewed_by: ""
---

# omb-m-26-05 — verification (FX-1 passes 2 and 3)

Independent verifier (did not extract), 2026-10-02/03, effort max. Final requirement count: **9**.

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
| hash | match; re-fetched directly from whitehouse.gov 2026-10-03 — identical sha256 54d5132e…67ab |
| currency | OMB memoranda index (fetched 2026-10-03) lists M-26-05 (January 23, 2026); entries through M-26-19 (September 10, 2026) contain no later software/hardware-assurance memo — claim confirmed |
| verbatim | 25 spans, 0 real misses (PDF text layer is OCR: "0MB", "Dlfector"; quotes use the intended text, as the record says) |
| locators | 9/9 correct |
| counts | shall 1 / must 2 / should 2 / may 2 — recount confirms |

## Rescission claims (priority check, against the texts)

- M-26-05 para 3: "Accordingly, OMB Memoranda M-22-18 and M-23-16, a companion policy, are hereby
  rescinded." — **confirmed**. It does not rescind or withdraw the CISA form: para 4 says agencies
  "may choose to use the government-wide secure software development resources developed under
  M-22-18, such as the Secure Software Development Attestation Form" — so "the form remains available
  for optional use" (here and in the omb-m-22-18 / attestation-form records) is correct.
- Inventory: "Agencies shall continue to maintain a complete inventory of software and hardware" —
  the only shall; confirmed. omb-m-22-18#III.A.1 cited this as `omb-m-26-05#R-0003`; **wrong id**,
  fixed to R-0005.
- M-26-05 says nothing about EOs 14028/14144/14306; the EO relationship is recorded in those records
  (see eo-14306 summary, verified separately).

## Defects found and fixed

- **Typing:** R-0001 ("agencies must rely on hardware and software producers…") typed `requirement`;
  it states a dependency, not an obligation → `descriptive` (normative.md label updated).
- **Object model:** edge `rescinds` was drawn AssurancePolicy → AttestationForm (inferred). The source
  rescinds the two memoranda and keeps the form usable, so the edge misstated the source. Replaced by
  `rescinds` Memorandum → Memorandum (stated, para 3) and added `cites` Memorandum → ReferenceDocument;
  objects Memorandum and ReferenceDocument added (13 objects / 8 edges). Mermaid updated.
- Design notes' "Deployment/Environment (ARCH-0001 §3)" checked: both exist in ARCH-0001 v0.2.0 §3.

## Cross-check

maps_to: omb-m-22-18, omb-m-23-16, cisa-ssdf-attestation-form-2024, omb-m-22-18#III.A.1, sp-800-218
all resolve. N/A reasons (schema, messages, protocol, state-machine, examples) are true: the memo
defines no structure or exchange beyond an optional SBOM-on-request term.

## Residual

- The law-firm alerts in summary.md were not re-opened (marked there as search results only).
- cites "CISA 2025 Minimum Elements for an SBOM (draft 2025-08-22)": the library holds
  `cisa-2026-sbom-minimum` whose record has no date/version; whether it is that draft or a later final
  is unresolved (design-notes open question 2 stands).

