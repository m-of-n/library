---
schema: "library-distilled/v1"
id: cisa-ssdf-attestation-form-2024-verification
record: cisa-ssdf-attestation-form-2024
type: verification
updated: "2026-10-03"
reviewed_by: ""
---

# cisa-ssdf-attestation-form-2024 — verification (FX-1 passes 2 and 3)

Independent verifier (did not extract), 2026-10-02/03, effort max. Final requirement count: **67**.

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
| hash | match (a8d6b568…dacb) |
| provenance | SHA-1 SPUES7JA… = all 25 Wayback 200/revisit captures of the official PDF URL (other entries are 301/403) |
| currency | CISA landing page (Wayback 2026-08-09): "CISA released the Secure Software Development Attestation Form on March 11, 2024"; the page is now flagged **"Archived Content"** (added to summary). Form v1.0; OMB 1670-0052 expires 03/31/2027 (p.1-8 headers and Burden Statement) |
| verbatim | 145 spans; checker hits are footnote markers and one verb label; 0 real misses |
| locators | 67/67 page locators correct |
| own forms | shall 1 / must 6 / should 1 / may 16 / will 4 / required 5 — recount confirms header |

## Defects found and fixed

- **Dropped (4 added):** INS-00 "Read all instructions before completing this form" (p.1); INS-11a
  online path "Selecting the provided URL: https://softwaresecurity.cisa.gov" (p.3); **INS-11c the PDF
  naming-convention instruction** (p.3 — previously only in a note, although the examples are built on
  it); I-products-2 "Additional pages can be attached…" (p.5).
- **Schema vs PDF (priority check):** every field of Sections I-III was compared with pp.5-7. The
  derived schema *required* `assessor` and `assessor_basis` on the 3PAO path; **the form has no such
  fields** — only the checkbox paragraph and the attachment. Now required: `box_checked`,
  `assessment_attachment`; the other two are optional, flagged library extensions. messages.yaml
  updated to match (assessor credential is a condition on the 3PAO, INS-18, not a form field).
  All other fields match the PDF (Section I three attestation kinds, three scopes, product table with
  "(if applicable)" version/date; Section II.1 seven producer fields; II.2 five contact fields;
  Section III items 1a-f incl. 1b i/ii, 2, 3, 4a-c, the notify-on-lapse attestation, signature block
  with Date (YYYY-MM-DD), Name, Title; the OR 3PAO paragraph; ATTACHMENT(S) title/description).
- **Examples:** the two fixtures still validate as expected; added `attestation-3pao.json` (valid —
  3PAO path, no signature) to exercise the oneOf branch.
- **Source defects recorded:** Section I exclusion item 2 (p.5) reads "freely and directly obtained
  directly" and differs from p.3; Appendix row 4 says "employed" where the form says "employs";
  Appendix SSDF ids "PO 1.1", "PW 7.1", "PW 8.1", "RV 1.1" undotted (already noted; normalised in
  maps_to).
- **Claims:** "weak conformance signal — the criticism M-26-05 makes" and the design-notes paraphrase
  were not M-26-05's words; replaced with the verbatim M-26-05 rationale.

## Cross-check

maps_to: EO ids `eo-14028#§4(e)(…)` and SSDF `sp-800-218#…` (SSDF **v1.1**, the edition the form's
footnote 5 names as SP 800-218) all resolve — 0 dangling across requirements, messages,
state-machine, protocol. State-machine triggers are named events or the defined message
`lapse-notification`. Every field a requirement names (Section I-III) exists in the schema;
every schema property carries x-locator.

## Residual

- RSAA online form (login-gated) not inspected; its field names may differ from the PDF.

