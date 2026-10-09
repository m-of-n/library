---
record: slsa-1-2
kind: design-notes
title: "slsa-1-2 — bearing on our design"
extracted: "2026-10-02"
reviewed_by: ""
---

# SLSA v1.2 — design notes for tmodel

Context. ARCH-0001 v0.2.0 §4 keeps AI-generation provenance in the model but sends
"Compile/SLSA build provenance" to the radar→tmodel contract (ADR-0001), outside the MVP (F7).
DL-0009 proposes R-040 (mitigation kind), R-041 (SDL/Gate), R-042 (conformance check), R-043
(governed views) and R-044 (crosswalk), all post-MVP except R-040. Requirement ids below are
`slsa-1-2#R-NNNN` from `requirements.yaml`.

## What we adopt

1. **The verification result as the shape of a conformance result (R-042).** The VSA predicate is
   `verifier.id`, `timeVerified`, `resourceUri`, `policy{uri,digest}`, `inputAttestations[]`,
   `verificationResult` (PASSED|FAILED), `verifiedLevels[]`, `dependencyLevels{}` and `slsaVersion`
   (see `messages.yaml` verification-summary-v1, `schema/vsa-v1.derived.schema.json`). It is the
   most complete published shape for "an automated check of X against policy P, using evidence E,
   by verifier V, at time T, with outcome O". A tmodel `ConformanceResult` node should carry the
   same fields. In our model it is an `Assertion` (§4) whose evidence edges point at the input
   attestations.
2. **Expectations keyed to a policy subject.** The verifier compares provenance with
   *expectations* set per package name (R-0214, R-0229 for trusted signer/builder pairs, and the
   `verify-build-provenance` flow in `protocol.yaml`). This is the R-042 input that DL-0009 leaves
   implicit: a Requirement's acceptance criterion is evaluated against expectations bound to a
   Product, not stored on the evidence itself.
3. **Levels are cumulative, per track, and separate from gates.** Each SLSA track has its own
   ladder: Build L0–L3 and Source L1–L4 (`state-machine.yaml` build-track-level and
   source-track-level). "Note that each SLSA level implies the levels below it in the same track." In tmodel, a Level is *how strongly*
   a property holds; it is not the R-041 Gate, which is *when* a check runs. Both are needed. A gate
   exit criterion can be "Build L3 verified for every release artifact".
4. **The supply-chain threat taxonomy A–I** (`normative.md` threats.md; 54 scenarios in
   `examples/threat-scenarios.yaml`) becomes a `ThreatCategory` facet for phase-scoped threats
   (R-037 `applies_in_phase`). It maps source threats A–C to implementation, build threats D–F to
   production/distribution, and usage threats G–I to deployment/operation.
5. **Party roles on edges, not nodes.** SLSA states that "a person or organization may act as more
   than one role". This is consistent with ARCH-0001 §2b (critic M1). We add *verifier*, *tenant*
   and *infrastructure provider* as relational roles.

## What we adapt, and how

- **Provenance as custody evidence, not epistemic Assertion.** A SLSA provenance is a signed
  in-toto Statement in a DSSE envelope. Its authenticity is cryptographic (R-0016–R-0021, R-0028–
  R-0032). tmodel's `Assertion` has provenance plus a review status and no signature. When radar
  hands evidence over (ADR-0001), we keep the attestation as an external `Entity` with a digest
  and a `verified_by` edge to the conformance result. We do not re-model DSSE inside tmodel.
- **Source track → mitigation kinds (R-040).** The Source L2–L4 requirements split cleanly:
  technical controls on protected refs (R-0110–R-0112) are `technical`; change history and
  continuity (R-0099–R-0102) are `process` with attested evidence; and the Source VSA (R-0096) is a
  `documentation`/attestation deliverable. Continuity needs the `valid_from`/`valid_to` time axis
  that ARCH-0001 §3b already flags as missing.
- **Platform assessment → Review with a method.** Assessing build platforms and source control
  systems allows self-attestation or third-party certification, done on a recurring cadence. In
  tmodel this is a `Review` with `method` and `assessor` attributes and a validity period.

## What we reject, and why

- **Modelling DSSE, signatures and roots of trust inside the tmodel KG at MVP.** ADR-0001 and
  ARCH-0001 §4 defer build provenance to the radar contract, so we reference attestations by digest
  and URI only. SLSA's own `rootsOfTrust` configuration stays the verifier's concern.
- **SLSA level as a risk metric.** A level is an assurance property of how an artifact was
  produced. It is not likelihood or impact, so it must not feed DEC-003's risk score directly. It
  may lower attack feasibility for supply-chain threat categories, but only through an explicit,
  reviewed mapping.

## Mapping to our decisions

| tmodel id | SLSA content | relation |
|---|---|---|
| R-040 mitigation kind | source controls (technical), history/continuity (process), Source VSA / provenance (documentation) | adopt |
| R-041 SDL / Gate | levels are not gates; the VSA is the evidence a release gate consumes; the deployment-time check is the `verify-vsa` flow | adapt |
| R-042 conformance | VSA fields; expectations; signer–builder pairs; PASSED/FAILED; `dependencyLevels` | adopt |
| R-043 governed views | VSA `policy{uri,digest}` pins the exact policy version a result was computed against: a governed, versioned view of a requirement set | adopt the pin |
| R-044 crosswalk | SLSA cites SSDF ("measure your efforts toward compliance with the SSDF"); the OSPS Baseline maps controls to SLSA | edges to `sp-800-218`, `openssf-osps-baseline` |
| R-037 lifecycle phase | threat categories A–I by stage | adopt as facet |
| R-036 parties | producer/consumer/verifier/tenant/admin roles | adopt as edge roles |
| DEC-009 mitigation lifecycle | control continuity (start revision, lapse, re-established) is a mitigation lifecycle with evidence | adapt |
| ADR-0001 radar contract | provenance + VSA are what radar hands over | confirms the boundary |

## Open questions

1. Should a tmodel `ConformanceResult` reuse the VSA field names verbatim, so that a VSA imports
   lossless, or should it stay neutral and map at the edge?
2. `dependencyLevels` reports levels of dependencies without making them part of `verifiedLevels`.
   How should conformance of a product roll up over `composed_of`? SLSA deliberately does not
   define transitive levels (the dependency track is still in the working draft).
3. The working draft adds a **Build Environment track** and a **Dependency track**
   (https://slsa.dev/spec/draft/, checked 2026-10-02). Do we wait for them before modelling
   Track as an open enum?
4. Source L1/L2 VSAs "MAY" be issued from the SCS's understanding of itself (R-0098). Should such
   self-attested evidence carry a lower confidence on the Assertion? Note the source overlaps at
   Level 2: the same sentence says "At Source Levels 1 and 2 the SCS MAY issue these attestations
   based on its understanding of the underlying system" and "at Level 2+ the SCS MUST use the
   SCS-issued source provenance". We read the MUST as governing L2 (found by the verify pass,
   2026-10-02).
5. Source defects recorded during extraction:
   - the single-page renderer rewrites "This page describes" to "This section describes";
   - pseudocode comments are split across lines in the rendered page (see the `requirements.yaml`
     note);
   - the v0.2→v1 migration example is JavaScript, not a schema.
   None changes meaning.
