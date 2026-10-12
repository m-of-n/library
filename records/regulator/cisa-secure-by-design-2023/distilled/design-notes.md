---
schema: "library-distilled/v1"
id: cisa-secure-by-design-2023-design-notes
record: cisa-secure-by-design-2023
type: design-notes
updated: "2026-10-02"
reviewed_by: ""
---

# Design notes: *Secure by Design* (CISA et al., 2023-10-25) and the tmodel object model

This record bears on **R-040** (mitigation kind), **R-041** (SDL/Gate), **R-042** (conformance check),
**R-043** (governed views) and **R-044** (crosswalk). It touches **DEC-009** (mitigation lifecycle) and
**R-036** (Party). The proposal ids come from ARCH-0001 v0.2.0 §1–§5 and §10, and from DL-0009. Requirement
ids are from `requirements.yaml`; object names are from `object-model.yaml`.

## What the document is, for design purposes

The guide has no gates, phases, work products or pass/fail criteria. Its conformance model is
**voluntary public evidence**. A manufacturer demonstrates each of three principles by publishing
artifacts (roadmaps, SBOMs, VDPs, threat models, self-attestations, statistics), and customers use
them in procurement (R-0007, R-0009, P1 Demonstrating p. 14). That makes it the **acquirer-facing
counterpart** of the process standards. SSDF, 62443-4-1 and 21434 tell a producer what to do; this
guide tells a producer what to *show*, and tells a buyer what to *ask for*.

## Adopt

1. **The three mitigation kinds of R-040 are all present, and the guide ranks them.** Technical
   mitigations (secure defaults, MFA, SSO, logging, memory safety; TAC-DEF-*, TAC-SBD-01..05) are
   preferred. Documentation mitigations (hardening guides) are actively deprecated: "Relying on
   hardening guides simply does not scale" (p. 13); P1-DEF-3; TAC-DEF-07; R-0068..R-0070. Process
   mitigations (field tests, RCA, code review) back them up. **Adopt R-040 as proposed, and add an
   optional `preference` or `polarity` note**, because a documentation mitigation that shifts work to the customer is
   a weaker treatment than a technical default. Practically, the threat×mitigation matrix (§10) should
   be able to flag a threat whose only mitigation is `kind=documentation` and `owner=customer`.
2. **Treat the SSDF task ids printed in the tactics as crosswalk edges (R-044).** TAC-SBD-01 → PW.6.1;
   -03 → PW.4.1; -04/-05 → PW.5.1; -06 → PW.7.2, PW.8.2; -07 → PW.7.1, PW.7.2; -08 → PS.3.2, PW.4.1;
   -09 → RV.1.3. Footnote 3 → PO.1.2. These are the source's own mappings, carried in `maps_to`. MAP-0001
   should import them as `source-asserted` edges. Mappings that we infer belong in a separate,
   reviewed set, the same split ARCH-0001 §2 uses for STRIDE↔CWE.
3. **A published, high-level threat model is an explicit demonstration item (P2-DEV-2).** It "should
   cover both the enterprise and development environments, as well as the way the software
   manufacturers intend for it to be used in customer environments." This bears directly on **R-043**. A tmodel
   threat model must be able to emit a **public, redacted, high-level governed view** of itself.
   It also bears on **§3b**: the scope list (enterprise, development, customer) is an environment ×
   lifecycle-phase selection that the `applies_in_phase` + `Environment` axes can express.
4. **Class-level root cause is how this guide frames mitigation.** "a large set of vulnerabilities
   are due to a relatively small subset of root causes" (p. 8). The same idea appears in P1-DEV-3,
   P2-DEV-4, P2-DEV-6, TAC-SBD-09 and TAC-SBD-10 (CVE with CWE). This confirms that tmodel's
   `Weakness(CWE)` layer is the right anchor for mitigation reporting. See gap G2 below.
5. **Party roles (R-036).** The guide names a single accountable person, the publicly named secure by
   design executive (P2-BIZ-1, P3-3). It also names the board as recipient of product-security
   reports (P3-2) and, on the customer side, of risk acceptances (CUST-06). These are relational
   roles on `Party`, which is what §2b proposes, so adopt as is. They also give DL-0009's
   "document owner / approver" a concrete instance: the SbD executive owns the roadmap view.

## Adapt

6. **R-041 SDL / SecurityProgram.** The guide's "program" has Juran's three quality phases, planning,
   control and improvement (P2-BIZ-2, p. 25). It has **no lifecycle gates**. The only
   release-gate-like statement is R-0005 ("only permit the shipping of products secure by design and
   default"), and R-0066 says products should conform "as they are refreshed". **Adapt:**
   `SecurityProgram` should allow a *program-improvement cycle*, a roadmap with dated milestones per
   product, alongside the gate sequence. A SbD roadmap item (e.g. "migrate component X to a
   memory-safe language by date D") maps to a `Milestone` with no exit criterion beyond its own
   evidence. R-0062 makes **threat-model-driven prioritisation of the roadmap** a stated
   recommendation, which gives the edge `SecurityProgram.prioritized_by ThreatModel`.
7. **R-042 conformance check.** No item has a test procedure. Still, 79 of the 152 extracted entries
   are `testable: yes` as an artifact-existence or product-behaviour check, 35 are `partial` and 38
   are `no`. Examples: "is the VDP published and does it contain the three elements"
   (P2-DEV-6), "does each product have an SBOM" (P2-DEV-5), "is admin MFA nagged until enabled"
   (TAC-DEF-02, R-0038). The `verification` column in `requirements.yaml` is written as those checks.
   **Adapt:** `Requirement` needs a `verification_mode` ∈ {artifact-exists, artifact-content,
   product-behaviour-test, interview}, so that R-042 can compute partial automated conformance.
   Product-behaviour tests (R-0038, R-0039, TAC-DEF-01/02) are exactly the kind a threat-model
   instance could carry as mitigation verification evidence (§5).
8. **R-043 governed views.** The guide's artifacts are *public* governed views: roadmaps,
   transparency reports, statistics, self-attestations and the threat model. DL-0009 models governed
   views as internal sign-off snapshots. **Adapt:** add `audience` ∈ {internal, customer, public} and
   a `published` state with URL and date to the governed-view object. Redaction rules (public
   *high-level* threat model vs the internal one) become a view-spec property, not a second model.
9. **DEC-009 mitigation lifecycle.** The guide adds two lifecycle facts. (a) After a compromise
   the manufacturer re-evaluates whether a mitigation should become a **free default** (R-0042).
   That is a transition *documentation/optional → technical/default*, which the DEC-009 state
   machine should allow as a kind change with provenance. (b) Settings are **continuously
   re-evaluated** against the current threat landscape (R-0035). A mitigation's adequacy therefore
   decays as the threat model changes, and DEC-009 should support re-review triggered by
   threat-model change, not only by product change.

## Reject (for tmodel; record, do not model)

10. **Business-practice items** (P1-BIZ-2 "hidden taxes", P3-1 annual-report sections, P3-4
    incentives, councils, customer councils, CUST-* procurement behaviour) are organisational
    policy, not product threat-model content. Keep them as `Requirement`s in the crosswalk (R-044)
    so conformance *reports* can list them. Do **not** add pricing, compensation or council objects
    to ARCH-0001 (scope guard, ADR-0002).
11. **Customer-side RiskAcceptanceDecision** (CUST-06). The guide wants risk acceptances documented,
    approved by a senior executive and presented to the board. tmodel already has `Review` with an
    accept-risk verdict. Reject a separate customer object for now. Note only that the
    approver must be a `Party` with an executive role.

## Gaps this source exposes (from `object-model.yaml`)

- **G1 Configuration layer.** Secure-by-default conformance is about *settings*: `Setting{is_default,
  safe}`, a `SecureDefaultBaseline`, *deviation from* it, and an indicator per unsafe state.
  ARCH-0001 has no configuration object. Without one, "product ships secure by default" (SDEF-1,
  TAC-DEF-*) cannot be checked against a model. **Open question Q1:** a `ConfigurationProfile` on
  `ProductInstance` (§3b already makes ProductInstance the state-bearing entity), or properties on
  `Component`?
- **G2 Class-level mitigation.** "Eliminate entire classes of vulnerability" across a product line
  needs a `MitigationInstance` that targets a `Weakness` at `ProductFamily` scope, not a
  `ThreatInstance` on a `Component`. **Q2:** extend the mitigation target to {ThreatInstance,
  Weakness@ProductFamily}?
- **G3 Public artifact / commitment.** See item 8. A `PublicCommitment` ("never charge for security
  features", "publish complete CVEs") is a forward-looking assertion. **Q3:** does §4 `Assertion`
  carry a temporal scope (`valid_from`, open-ended), or is this a different node?
- **G4 Metrics.** SecurityStatistics (MFA adoption %, patch currency %, unused privileges) and the
  measurement → SDLC feedback loop (R-0045). **Q4:** is an SDL metric a `View` over KG telemetry, or a
  stored observation with provenance?
- **G5 Guide polarity.** Hardening guide vs loosening guide (p. 32): a documentation mitigation is
  either a list of steps the customer must take, or a list of risky deviations from a secure
  default. Only the second is endorsed.

## Relation to other lane-B records

- `cisa-secure-by-design-pledge-2024` turns a subset of these practices into seven measurable goals.
  The overlaps are MFA (TAC-DEF-02), default passwords (P1-DEF-1), class reduction (P1-DEV-3), patching
  (P2-DEF-2), VDP (P2-DEV-6), CVE with CWE (P2-DEV-4/TAC-SBD-10) and evidence of intrusions (logging,
  P1-BIZ-1). The pledge adds one-year measurement, which this guide lacks.
- `cisa-secure-by-demand-guide-2024` is the customer-question side of R-0008..R-0010 and CUST-*.
- `cisa-ssdf-attestation-form-2024` is the **signed, government-required** version of P2-DEV-3
  ("Publish detailed secure SDLC self-attestations"). This guide asks only for a voluntary published one.
- `sp-800-218` is the framework named in P1-DEV-1, P2-DEV-3 and the TAC-SBD bullets.
- `eu-cra-2024-2847` is cited on p. 4 as reinforcing life-cycle security. The CRA makes binding
  (Annex I) several items that are voluntary here: no known exploitable vulnerabilities, secure by
  default configuration, a VDP and an SBOM.

## Open questions about the source itself

- **S1.** The Principle 3 statement differs between p. 10 ("Build organizational structure and
  leadership to achieve these goals.") and its section title on p. 26 ("Lead from the Top"). They are
  the same principle under two names; we use "Lead from the Top" as its short name.
- **S2.** "Secure by default" appears both as a practice category under Principles 1 and 2 and as
  the separate "Secure by Default Tactics" list (pp. 30–31). The lists overlap: default passwords
  appear as P1-DEF-1 and TAC-DEF-01, and hardening-guide size as P1-DEF-3 and TAC-DEF-07, with
  different wording. A crosswalk should treat each pair as one requirement with two locators.
- **S3.** Footnote 4 (p. 29) says some authoring organisations "are exploring alternate approaches"
  to SBOM. The co-sealing agencies are not unanimous on SBOM.
