---
schema: "library-distilled/v1"
id: cisa-ssdf-attestation-form-2024-design-notes
record: cisa-ssdf-attestation-form-2024
type: design-notes
updated: "2026-10-02"
reviewed_by: ""
---

# Attestation form — design notes for tmodel

**Status:** form v1.0, OMB 1670-0052, expires 2027-03-31. Mandatory for agencies to collect under
M-22-18/M-23-16 until **2026-01-23**; since **OMB M-26-05** rescinded both memos it is an
**optional** tool agencies "may choose to use" (omb-m-26-05#R-0006). The form itself is unchanged.

## Adopt

- **Attestation as a governed, signed document-view (R-043).** The form is the canonical example
  of what DL-0009 calls a governed view: an owner (producer), an approver/signatory with authority
  (CEO or designee), a version (form 1.0; kinds new / revised / following waiver), a date, and a
  scope. Render an SDL conformance report as such a view over the KG: Section III's 12 items
  become `Requirement` rows whose status is computed from Evidence, and the signature is a
  `Review` by the signatory Party. This is also the export format test for R-043.
- **Crosswalk data (R-044).** The Appendix is a **source-published** three-way mapping
  form item → EO 14028 §4(e) subsection → SSDF tasks (`maps_to` in requirements.yaml, ids
  `eo-14028#§4(e)(i)(A)`, `sp-800-218#PO.5.1`). Load into MAP-0001 as stated (not inferred) edges.
  Note the mapping is coarse: row 4 (4, 4a–4c) maps as a block to 19 SSDF tasks and to §4(e)(iv)
  only; the form's VDP item (4c) is not mapped to EO §4(e)(viii).
- **Revocation and forward scope (R-042).** An attestation binds future versions "unless and until"
  the producer notifies non-conformance (fn 4, III-notify). tmodel conformance results must carry
  `valid_from`, a version range, and a revocation event — not only a point-in-time verdict.
- **Release gate (R-041).** 4a/4b put vulnerability checks and remediation policy *prior to
  product, version, or update releases* — the form's one explicit gate, matching SSDF PO.4.
- **Three outcomes + alternative assurance (R-042).** signed self-attestation / 3PAO assessment
  (no signature) / POA&M + OMB extension. Same three-valued conformance as omb-m-22-18.

## Adapt

- **All-or-nothing statements.** The form has no per-item "not met"; partial conformance leaves
  the form and becomes a POA&M. tmodel should keep per-Requirement status and *derive* the
  all-or-nothing form view.
- **Build environment as asset.** Items 1a–1f treat development and build environments, their
  components and trust relationships, as the protected asset. A threat model of the SDL itself
  needs these as `Component`s in a dev/build `Environment` — today ARCH-0001 §3 Environment is the
  runtime deployment. Raise for iteration 7.
- **Producer-developed code only.** "attesting ... for code developed by the producer" (Section I
  note) — conformance scope excludes third-party components except via items 2–3. Model as an
  applicability predicate.

## Reject

- Using the form's company-wide scope as product-level conformance evidence; keep it as an input
  Assertion with a wide subject set. (M-26-05 says M-22-18's processes "prioritized compliance over genuine security investments".)
- Treating attestation text as testable: most items are qualitative ("good-faith effort", "to the
  greatest extent feasible", "to the extent practicable") — `testable: partial` in requirements.

## Bears on

R-041 (release gate), R-042 (conformance states, revocation, assurance level), R-043 (signed
governed document), R-044 (form→EO→SSDF crosswalk), DEC-009 (POA&M as a mitigation with a plan).

## Open questions

1. Does the online RSAA form (login-gated, not inspected) carry fields beyond the PDF (e.g.
   product identifiers like CPE/purl)? If so, derive v2 of the schema.
2. Should tmodel's export of an SDL conformance view target this form's structure as one output
   profile (US federal), alongside EU CRA Annex I declarations?
3. Source defect: Appendix row 4 says "employed", the form says "employs"; SSDF ids printed
   inconsistently ("PO 1.1", "PW 7.1"). Recorded, normalised in maps_to.
