---
schema: "library-distilled/v1"
id: bsi-tr-03183-1-design-notes
record: bsi-tr-03183-1
type: design-notes
updated: "2026-10-02"
---

# BSI TR-03183-1: design notes for tmodel

This note covers how TR-03183-1 v1.0.0 bears on ARCH-0001 v0.2.0 and DL-0009. The TR is BSI's interpretation of the CRA (`eu-cra-2024-2847`). It is the risk-assessment and conformity-assessment front end, where its sibling `bsi-tr-03185` is the SDL process. The TR states plainly that it imposes no obligations and gives no presumption of conformity (§2).

## Adopt

- **R-040.** Take the TR's control types, Activity, Mechanism and Documentation (§4.6), as the warrant for `MitigationInstance.kind ∈ {process, technical, documentation}`.
  - The PASS rule per type should become the verification rule per kind:
    - Activity: performed, with its output produced.
    - Mechanism: implemented as described.
    - Documentation: provided in the described manner.
- **R-042.** Adopt a three-valued verdict, PASS / FAIL / N/A, with the closed N/A reason list from §4.6: compensation fulfilled, target absent, if-condition not met, conflict with another regulation, risk not applicable.
  - The overall verdict is PASS iff every control is PASS or N/A. That is exactly an automatable gate exit criterion.
  - Keep the TR's caveat that the verdict is *not* a statement of CRA compliance (§4.7). tmodel conformance should carry the same disclaimer.
- **R-044.** Use Appendix B's sub-ids as the atomic CRA requirement keys when tmodel maps to the CRA. The sub-ids are ER.0 to ER.14 and VH.1 to VH.8a; for example ER.4a to ER.4d split CRA I(2)(c) into automatic updates, opt-out, notification and postponement. They are finer than the CRA's own lettering and suit conformance checks. They are recorded as `maps_to` → `eu-cra-2024-2847`.
- **DEC-003 / R-011.** The impact criteria (Tables 1 to 3), with C/I/A defaults per asset category and inheritance by security assets (X'), are a ready-made, tailorable default impact table. Keep them separate from ISO 21434 S/F/O/P, per the iteration-6 critic H3. They are a different axis: CIA of PwDE assets.

## Adapt

- **ARC selection is a predicate.** A risk scenario has a minimum C/I/A impact and an environment (access, interface, user capability), with "*" as wildcard and OR within a parameter. Selecting controls means matching that against a product's risk profile.
  - Model a generic Mitigation with an `applies_when` predicate over Asset impact and Environment attributes. The "generic → product" step of DEC-009 then becomes computable.
  - This needs Environment attributes that ARCH-0001 lacks: user capability and access restriction.
- **Applicability statements.** RH_RT.1.1.2 requires a list of applicable and non-applicable essential requirements, each with a justification.
  - Model this as a Requirement-scoped `Assertion` (§4) with value applicable/non-applicable and a justification that points at a Risk.
- **Risk sharing.** Add `shared(with: Party, basis: law|contract|guidance)` to the DEC-009 dispositions alongside mitigated and accepted. Due-diligence evidence is attached to it.
- **Lifecycle-dependent acceptance.** The Annex D.2 NOTE allows moderate risks to be accepted post-market but not during development. Acceptance rules need the LifecyclePhase (§3b) as an input.
- **Environment composition.** §6.6 lets an integrated component expect an environment from its integrator, who provides it or delegates it downstream with a description. Model this as an assume/guarantee edge between Components and Parties. It is the supply-chain counterpart of a trust boundary.

## Reject or hold

- **Annex D numeric scoring.** BSI marks it "highly experimental", and the formula as printed is inconsistent (see below). Do not implement it as a metric. Keep the D.2 matrix only as an example fixture.
- **The OSCAL control catalogue (Chapter 7).** It is outside the PDF, and access is on request. Hold any import until it is obtained; the request goes to tr-03183@bsi.bund.de.

## Open questions and source defects

1. **Date.** The cover says "Date: 31.07.2026". The changelog says "2025-07-31 Publication of version 1.0.0" and the copyright reads "2023 - 2025". BSI's press release of 05.08.2026 announces the v1.0 publication, so we record 2026-07-31 and treat the changelog year as a typo. (Verifier 2026-10-03: the landing page labels the current Part 1 download "Version 1.0.0"; v0.9.0 and v0.10.0 are archive entries. An earlier note that the current link was labelled 0.10.0, and a server Last-Modified of 2026-07-31, could not be reproduced and were removed.)
2. **Missing material in §5.14.**
   - §5.14.1 is truncated at a page break, ending mid-sentence in the Security.Mechanism row.
   - The §5.14.2 "Likelihood criteria" heading is missing.
   - Table 6 (Access Restriction) is missing; table numbering jumps from 5 to 7. Annex D Table 12 supplies the values.
3. **Appendix B.**
   - There is no ER.3 and no ER.8; CRA I(2)(g), data minimisation, is absent.
   - ER.14 is truncated and has no 14a.
   - There is no VH.2.
   - VH.6a is labelled "Part II 4" but belongs to Part II point 6.
   - Table 1 repeats the PII.Important row.
4. **Annex D formula.** `round(1 + i*a*u) * 4` yields 4 or 8, which does not match the 1–5 environment rows of the D.2 matrix. The matrix also puts the highest risk at "Environment 1", which reverses the intuitive direction of the formula, where a higher value means more exposure.
5. **Example inconsistencies.**
   - §6.5 uses "amplifier of 1" additively, although the definition is Impact = Base × Amplifier.
   - §6.5 mislabels the RDPS environment.
   - Annex C uses asset sub-categories (Security.PrivateConfiguration, Security.Secrets.NetworkCredentials) that Table 3 does not define.
6. **Dangling references.** "[USER_DOCUMENTATION]" (RH_RT.1.2.2) and "REQ_RA 1.1.2" (§5.9.1) do not resolve inside the PDF. The first is probably an OSCAL control id; the second means RH_RA.1.1.2.
7. **SDL coverage gap.** Part 1 covers risk assessment and the CRA overview but contains no secure-development process requirements. For those, BSI points to TR-03185. Part 2 covers SBOM (current v2.1.0, and the landing page also links a v2.2.0 PDF). Part 3 covers vulnerability reports and notifications (v1.0.0). Part H covers Module H conformity through an ISO 27001 ISMS (v1.1.0, 30/05/2026).
