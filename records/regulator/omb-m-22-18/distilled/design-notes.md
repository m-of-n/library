---
schema: "library-distilled/v1"
id: omb-m-22-18-design-notes
record: omb-m-22-18
type: design-notes
updated: "2026-10-02"
reviewed_by: ""
---

# OMB M-22-18 — design notes for tmodel

**Status of the source:** rescinded 2026-01-23 by M-26-05 (omb-m-26-05#R-0004); amended
2023-06-09 by M-23-16. It is no longer binding, but it is the clearest worked example of a
**conformance gate run by an acquirer**: *no acceptable attestation → no use*. That is exactly
the shape DL-0009 wants for an SDL `Gate` exit criterion, seen from the customer side.

## Adopt

- **Conformance as a scoped, signed claim (R-042).** The memo's `SelfAttestation` is a
  producer-issued *conformance statement* over a named requirement baseline (NIST Guidance) at a
  declared scope (company / product line / product). Model it as an `Assertion` whose subject is a
  `Requirement` set and whose object is a `Product` scope, attributed to a `Party` (§4 PROV
  `wasAttributedTo`) and accepted by a `Review` from the consuming Party. Adopt the three minimum
  fields (II.1.c.i–iii) as the floor of any `Attestation` view.
- **Three-valued conformance (R-042).** M-22-18 has *attested*, *third-party-assessed* and
  *partial + POA&M accepted* as usable outcomes, and *not usable* as the failure. tmodel's
  "every in-scope threat has an approved mitigation" check needs the same third state: a
  Requirement **not met but with an accepted, dated plan** (POA&M). Adopt: `Requirement`
  satisfaction ∈ {satisfied, satisfied-by-assessment, gap-with-accepted-plan, unsatisfied, waived}.
- **Dated milestones with owners (R-041).** §III / Appendix A is a program plan: owner, deliverable,
  offset from an epoch (memo date or a dependent event R). `state-machine.yaml#program-milestones`
  shows that a `Milestone` needs `offset_from` (another milestone/event), not only an absolute
  date — M7/M8 were later re-anchored by M-23-16 to "PRA approval + 3/6 months".
- **Evidence kinds (R-040, R-042).** SBOM, automated integrity/vulnerability-check outputs, and VDP
  evidence are the evidence classes the memo recognises; all are `Evidence` attached to the
  attestation, consistent with mitigation `kind ∈ {technical, documentation, process}` — the POA&M
  is a *documentation/process* mitigation of a practice gap.

## Adapt

- **Applicability rules.** Scope depends on development date, major-version change, renewal,
  third-party vs agency-developed and criticality (M-21-30). tmodel's `Requirement` → `Product`
  applicability needs predicates over Product attributes; record them as `applies_if` on the
  Requirement mapping rather than duplicating Requirements.
- **Confidential evidence.** POA&M documentation "shall not be posted publicly". Governed views
  (R-043) need an access/visibility attribute on evidence, separate from approval.
- **Waiver / extension** are approvals by a named authority (OMB Director + APNSA) that override
  a Requirement or a Milestone for a bounded time. Model as a `Review` with verdict `waived` /
  `extended` and `valid_to`, so DEC-009's mitigation lifecycle and the gate share one mechanism.

## Reject

- The memo's **company-level self-attestation** as a substitute for per-product evidence. tmodel's
  conformance is per `ProductInstance` and per threat; a product-line claim is an *input* Assertion,
  not a satisfied Requirement. (M-26-05's rationale — "prioritized compliance over genuine security
  investments" — is the same criticism.)

## Bears on

- **R-041** — Milestone/Gate: offsets, owners, deliverables, extension override.
- **R-042** — conformance states incl. gap-with-plan and waiver; attestation as Assertion+Review.
- **R-043** — the attestation and inventory are governed documents (retained, central system,
  confidentiality).
- **R-044** — maps_to edges to SSDF / NTIA SBOM / EO 14028 §4(e) (requirements.yaml).
- **DEC-009** — POA&M is a mitigation with its own lifecycle (planned → in progress → done), owned
  by the producer and approved by the consumer.

## Open questions

1. Should rescinded source requirements stay in the crosswalk with `status: rescinded` (our choice
   here) or be dropped? Keeping them preserves history and the M-23-16 → M-22-18 precedence chain.
2. Is "third-party assessment in lieu of self-attestation" one `Review` with a stronger assurance
   level, or a different `Evidence` kind? (Assurance level as an attribute seems simpler.)
3. The memo never defines what happens at the deadline if nothing is filed; `not-usable` is
   inferred from "must only use". Flagged `kind: inferred` in the state machine.
