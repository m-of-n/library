---
schema: "library-distilled/v1"
id: uk-software-security-code-of-practice-design-notes
record: uk-software-security-code-of-practice
type: design-notes
updated: "2026-10-02"
---

# Design notes — UK Software Security Code of Practice → tmodel

Mapped against ARCH-0001 v0.2.0 (proposed), DL-0009 (R-040..R-044) and MAP-0001. Nothing here is
accepted. SDL is post-MVP, and only R-040 is MVP-adjacent.

## Adopt

- **R-042: a three-level conformance chain, Requirement → Claim → Evidence.** The Code's principle
  (`#1.1`..`#4.3`) is the Requirement. The NCSC APC claim (`#APC-<p>-NN`) is an objectively
  evidenceable conformance criterion. Evidence is typed as document inspection, interview, or audit
  of test plans and results. Adopt a `ConformanceCriterion` (claim) node between `Requirement` and
  `Evidence`, with a `refines` edge so it can form a claims tree (APC Appendix). A principle is met
  when all of its claims are well-evidenced. This is the source's own rule (APC "About this
  document"), and it is exactly R-042's "satisfied by Evidence + approving Review".
- **R-042: the threat-model hook.** `#APC-1.4-01`, "Techniques to understand how the software might
  be exploited (threat modelling) have been used in the design of the software", together with
  `C-GLOSS-SBD` (risk assessment of prevalent threats in the blueprints) means a tmodel threat-model
  instance is direct evidence for a named conformance claim. Use this as the worked example for "a
  threat model evidences an SDL requirement".
- **R-040: mitigation kinds.** The Code needs all three kinds. Technical: signed updates,
  MFA (`IG-1.4-*`). Documentation: user secure-use documentation (`IG-4.1-02`), the support statement
  (4.1), the published VDP (3.2). Process: the vulnerability management plan, the response playbook
  (3.3), build-environment access policy (2.1). This is good external evidence that R-040's
  `{technical, documentation, process}` enum is complete enough. No fourth kind appears.
- **R-044: crosswalk.** Carry the source-published mapping only. IG Appendix 1 lists SSDF, MS SDL,
  OWASP SDLC, Cisco SDL, SLSA and S2C2F as frameworks that satisfy `#1.1` (`maps_to` in
  requirements.yaml). The Code (p.2) claims alignment with SSDF and the EU CRA but publishes **no
  clause-level mapping**. Any principle-to-SSDF-task cell in MAP-0001 is therefore *our* assertion
  (an `Assertion` + `Review`, ARCH-0001 §4), not extracted fact.

## Adapt

- **Applicability profiles.** Table 1 scopes the themes by the organisation's role in the supply
  relationship: developers and distributors get all four themes, resellers get 3–4, developers only
  get 1–2 (and 3 where in scope). ARCH-0001 §2b already makes supplier, consumer and vendor-of
  *relational* edges. Adapt by deriving conformance applicability from those edges. Do not tag the
  Party: the same Party can be a developer of A and a reseller of B.
- **The SRO is an accountability role.** The verb is "shall gain assurance that their organisation
  achieves". This role is neither the owner nor the approver of a work product (DL-0009). Model it as a
  `Party` role (`accountable_for`) on the SDL program (R-041), separate from per-gate approvers.
  This answers the critic-M1 constraint: it is a role of a Party, not a new node type.
- **Phase mapping (R-041 Gate).** The themes map coarsely onto the canonical phase line, and design
  and testing sit inside theme 1:
  theme 1 → requirements/design/implementation/verification; theme 2 → implementation (build) and
  supply-chain; theme 3 → release and operations/response; theme 4 → cross-cutting customer
  communication from release through end of support. The `phase` field in requirements.yaml is
  per principle. The Code has no gates. Its only time-bound checkpoint is the end-of-support notice
  (≥ 1 year), which is a dated lifecycle transition in state-machine.yaml.
- **§3b lifecycle.** The Code's SDLC definition has 7 stages (requirements gathering, analysis,
  design, implementation/coding, testing, deployment, maintenance/support). Add an explicit
  `end-of-support-notified` state with a notice-period guard to the `ProductInstance` lifecycle when
  §3b gains `valid_from`/`valid_to`.

## Reject

- **No maturity levels or scoring.** The Code and the APC are binary per claim: evidenced or not.
  Do not invent levels for the UK code in a crosswalk that uses SAMM/62443 maturity.
- **The Code as a lifecycle definition.** The Code deliberately delegates the lifecycle to "an
  established secure development framework" (1.1). Do not model it as an SDL in its own right. It
  is a *conformance profile* applied over whichever SDL a vendor follows.
- **Treating IG statements as Code requirements.** The implementation guidance "should" statements
  (`IG-*`) are advice on *how*. Only the 14 principles carry the Code's defined "shall". Keep
  `normativity` and `source` distinct in any conformance rule: a vendor is non-conformant for a
  failed APC claim, not for skipping an IG bullet.

## Open questions

1. **Claims trees: transcribed, connectors not.** *(Corrected in the verify pass, 2026-10-02.)* The
   APC appendix trees are not in the PDF (it prints only the theme headings), but the NCSC web page
   serves them as four SVGs whose node text is machine-readable. `apc-claim-trees.yaml` now holds all
   68 claim nodes (ids 1.1 ... 4.3.2) and 21 strategy boxes; `parent` is inferred from the numbering, so
   the `refines` edge is populated, but the connector geometry ("Is a subclaim of" / "Supports" /
   "Comments on") and the strategy-box attachment points are not parsed. Source inconsistency found:
   tree leaf 1.2.3 "Security requirements are shared with third party suppliers" has no counterpart
   among the 45 APC body claims, and 2.1.1 / 4.1.3 are worded differently from body claims APC-2.1-01 /
   APC-4.1-03. Which list is authoritative for conformance is an open question for NCSC.
2. **The self-assessment "form" is a generic template.** The Code links
   `pba-self-assessment-template.docx`, which is the NCSC PBA template and not an SSCoP-specific
   form. The evidence record format is undefined, so R-042's Evidence shape cannot be aligned to it.
3. **The certification scheme does not exist yet.** The Code p.5 says "will be shared in due
   course". As of 2026-10-02 no scheme is published. The Ambassadors Scheme (Jan 2026) promotes
   adoption and does not certify. Revisit when DSIT publishes it, since it would define an
   assessor role and outcome states.
4. **The sources disagree on internal teams.** The Code's glossary defines "relevant parties" as
   "external to the organisation", but IG 3.4 lists internal security teams first and APC 3.4 claim
   1 is "Internal security teams are informed." This is a minor inconsistency in the source;
   requirements.yaml keeps both.
5. **Source typo.** APC 3.1 reads "distributed overtrusted channels". It is preserved verbatim.
6. **PDF and HTML renderings differ** in three places (normative.md header). Neither is marked
   authoritative. The PDF is the hashed source of record.
