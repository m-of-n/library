---
schema: "library-design-notes/v1"
id: sp-800-204d-design-notes
record: sp-800-204d
kind: design-notes
type: design-notes
title: "sp-800-204d — bearing on the tmodel design"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# SP 800-204D: how it bears on the tmodel design

**Conventions.** A bare `§x` refers to SP 800-204D. Requirement ids are `sp-800-204d#R-NNNN`,
shortened to `R-NNNN`; tmodel requirements are spelled out as tmodel R-040 to R-044. Our documents
are cited by id: ARCH-0001-PROPOSAL-v0.2.0 (shortened to ARCH), DL-0009, MAP-0001 and ADR-0001.
**[analysis]** marks reasoning from this extraction that neither the source nor our documents state.
Nothing here is accepted. DL-0009 puts SDL post-MVP, and only tmodel R-040 is MVP-adjacent.

## What the document is, for our purposes

SP 800-204D is the **pipeline-level operationalisation of SSDF v1.1** for cloud-native DevSecOps.
Appendix A (Table 2) maps its tasks onto 12 SSDF practices: PO.1–PO.5, PS.1–PS.3, PW.5, PW.6, PW.8
and PW.9. Appendix B leaves PW.1–PW.4, PW.7 and RV.1–RV.3 out of scope. The SDL report should read
it as **evidence that the SSDF practices about build, release and source protection can be checked
by machine**. It is not a full SDL: there is no design phase and no vulnerability response.

## Adopt

- **Policy-gated admission as the template for an automatable Gate (tmodel R-041, R-042).** In
  §5.1.1 and §5.2, a signed **Policy** says which attestations are required and which functionary
  keys may produce them. A **Verifier** evaluates the stored attestations against it, and the
  result is allow or block (R-0067–R-0070, R-0099–R-0101). This is the conformance-check shape
  DL-0009 asks for: a Requirement is satisfied by Evidence, and an approving decision is recorded.
  Adopt it as the reference pattern for a Gate exit criterion that can run without a person.
- **Typed evidence (tmodel R-042).** §5.1.1 names four evidence kinds: environment, process
  (explicitly "best effort"), materials and artifacts. DEPLOY_REQ-4 adds vulnerability-finding
  attestations, and the scan time matters. DL-0009 `Evidence` should carry a `kind` and a
  **timestamp that conformance can test for recency**. Both build horizon (R-0113) and scan recency
  (R-0100) are time-bounded validity: the `valid_from`/`valid_to` axis ARCH §3b already flags as
  missing.
- **Mitigation kind (tmodel R-040).** The 204D measures fall cleanly into technical (push
  protection, isolation, signing), process (code review, audit cadence, roles and authorizations)
  and documentation (build policy, trusted-OSS-source policy, security requirements per code type).
  This supports R-040's three-valued `kind` with no fourth value needed. **[analysis]**
- **Crosswalk edge with a basis (tmodel R-044).** Table 2 is a source-published mapping, so every
  `maps_to` in `requirements.yaml` carries `basis: stated` (from Table 2) or `basis: inferred` (ours,
  3 entries). MAP-0001 should keep the same distinction: SSDF row 13 (build/provenance) and row 16
  (protect the development environment) can now cite 204D statements instead of "approx".

## Adapt

- **Attestation is not the §4 Assertion.** ARCH §4 reserves `Assertion` for epistemic claims about
  the model (AI proposes, a human reviews). ADR-0001 defers SLSA/build provenance to the
  radar→tmodel contract. A tmodel R-042 conformance check that reads 204D-style attestations
  therefore needs an **external-evidence reference type**: a digest, a type and a verifier result.
  It does not need to model the attestation itself. **[analysis]** This keeps ADR-0001 intact and
  still lets a Gate cite the evidence.
- **Ordered trust.** ARCH `TrustBoundary` is a zone. 204D needs a *ranking* between zones: the
  driver/control plane outranks the steps (§5 prerequisite 4), and the attestor outranks the build
  (§5.1.1, R-0059). Model this as a `higher_trust_than` relation between zones rather than a new
  layer.
- **Separation of duties on Review (DEC-009 mitigation lifecycle).** "Developers with 'merge
  approval' permissions cannot approve their own merges" (R-0071), and reviewers must be another
  developer (R-0032). DEC-009's review step should carry an author ≠ approver constraint. It is the
  same rule our governed views need for sign-off (tmodel R-043).
- **LifecyclePhase.** The 204D stages (build, test, package, deploy, plus GitOps operation) belong
  to ARCH §3b `implementation → distribution → deployment → operation`. Put the deployment
  admission decision at the `distribution → deployment` boundary as a Gate.

## Reject or do not carry

- **Wire formats.** 204D defines none; it says SBOM and attestation formats are out of scope
  (§1.2, §6). Take formats from `in-toto-attestation-v1`, `slsa-1-2`, `spdx-3-0-1` or
  `cyclonedx-1-7`, never from 204D.
- **The §3 generic mitigation list** (patch management … adherence to standards) is control-family
  vocabulary with no testable content. Do not import it as Requirements. At most, use it as tags on
  Mitigation.

## Source defects and inconsistencies (recorded, not fixed)

1. **Strength escalation between §5 and Appendix A.** On online keys, §5.1.3 says they "should not
   be used" for client-trusted roles (R-0081); Appendix A says "must not" (R-0117). On SAST/DAST,
   §5.1.4 says tools "should be run" (R-0086); Appendix A says they "must provide coverage" (R-0121).
   On SCA, §5.1.4 says "potentially using appropriate SCA tools" (R-0087); Appendix A says "must be
   detected using appropriate SCA tools" (R-0122). Automation is an imperative in §5 (R-0049) and a
   "must" in Appendix A (R-0115). **Open question:** which strength does a conformance check apply?
   Our default **[analysis]** is the weaker body text, with the Appendix A wording noted. Raise it
   with NIST (sp800-204d-comments@nist.gov) if we depend on it.
2. **Option dropped in Appendix A.** PULL-PUSH-REQ-3 in §5.1.2 offers (a) sandboxed CI *or* (b) an
   approval delay. Appendix A lists only (b) (R-0120).
3. **Scope drift.** PULL-PUSH_REQ-1 covers "the change being pushed" in §5.1.2 but "the pull
   request" in Appendix A. PULL-PUSH-REQ-2 is about tools' "source-code origin" in §5.1.2 but
   "external tools (e.g., Jenkins)" in Appendix A.
4. **Identifier hygiene.** The source writes `PULL-PUSH_REQ-1`, `PULL-PUSH-REQ-2`,
   `PULL-PUSH_REQ-4` and `DEPLOY_REQ-4` with mixed `_`/`-`. Designators are kept exactly as
   printed; a citing document must not normalise them silently.
5. **COMMIT-REQ-1** opens with a misplaced parenthetical "(e.g., personal access token)", before the
   verb.
6. **Unexpanded acronym.** Table 1 note b mentions "VSA" without expanding it. It is the SLSA
   Verification Summary Attestation; `slsa-1-2` is the record to read.
7. **Unmapped requirements.** The attestation requirements other than environment attestation
   (R-0055, R-0062–R-0066; R-0061 environment attestation *is* mapped to PO.5 and PW.6 — corrected
   by the verify pass 2026-10-02), push protection
   (R-0090–R-0094) and GitOps-REQ-1/3/4 have **no SSDF mapping** in Table 2, although PS.2/PS.3 and
   PO.5 obviously apply. **[analysis]** A crosswalk built from Table 2 alone will undercount 204D's
   SSDF coverage.

## Open questions for iteration 7 or 8

- Does a tmodel Gate store the *Policy* (criteria document) as a governed view (tmodel R-043) with a
  signature, or only reference an external policy by digest?
- Evidence recency: should a tmodel R-042 check fail a gate when the evidence is older than a
  policy-defined horizon (204D build horizon and scan recency)? That needs the time axis first.
- Should the 204D threat taxonomy in §3.1 (actors, vectors, targets, exploit types) and the
  three-stage SSC attack in §2.4.2 seed supply-chain `AttackPattern`/`AttackPath` entries, or is
  that work for `slsa-1-2` threats or `sigstore-threat-model`?
