---
schema: "library-doc/v1"
id: owasp-asvs-5-design-notes
record: owasp-asvs-5
type: design-notes
updated: "2026-10-02"
reviewed_by: ""
---

# Design notes — OWASP ASVS 5.0.0 against the tmodel object model

Targets are ARCH-0001 v0.2.0 (proposal, iteration 6), DL-0009 (R-040..R-044), MAP-0001 and DEC-009. ASVS is
**post-MVP SDL content** (DL-0009 guardrail). The exception is R-040, which ASVS supports directly.

## What ASVS is, for us

ASVS is a catalogue of **345 verifiable outcome requirements on an application**: L1 70, L2 183, L3 92, in
17 chapters and 80 sections. Each requirement must yield a pass/fail decision (F-03). It is **not** an SDL
process framework. It "does not prescribe development lifecycle activities" (What is the ASVS? › Scope ›
Application). In 5.0 the old SDL process items were moved out of the requirement set into the non-mandatory
Appendix D (AppD-10..16): secure SDLC, threat modeling, security user stories, secure-coding checklist,
backdoor review, configuration drift and third-party hardening. For the SDL model, ASVS therefore fills
the **verification gate's exit criteria**. It does not supply the gate structure.

## Adopt

| ASVS concept | tmodel target | note |
|---|---|---|
| Requirement (`v5.0.0-<ch>.<sec>.<req>`) | `Requirement` node (R-042/R-044) | Use the standard's own versioned id as the stable external key. F-14/F-15 make the version part mandatory in practice. A bare id "refers to the latest", which is unsafe for a KG (F-16). |
| Documentation requirement vs implementation requirement | **R-040** `MitigationInstance.kind ∈ {documentation, technical}` | The strongest external warrant for R-040 in the library. The standard makes documentation requirements first-class (31 requirements, the first section of 11 chapters) and verifies them *separately* from the implementation (F-06). A documented decision may be "a literal document" or "a common code library that all developers are mandated to use". So a documentation mitigation's artifact can be code. |
| Per-requirement pass / fail / not-applicable, with evidence | ARCH-0001 §4 reified `Assertion` + §5 `Review`; R-042 | `VerificationResult` = Assertion("application satisfies v5.0.0-x.y.z") with a Review verdict. The N/A outcome *must be noted in the report* (F-21). R-042's "every in-scope ThreatInstance has an approved MitigationInstance" needs the same explicit, justified N/A. |
| Verification report: scope, all requirements checked, exceptions, N/A, remediation, methods | **R-043** governed document-view | The report is the governed, versioned, signed-off projection of conformance Assertions. `messages.yaml: verification-report` lists its fields. |
| Level (cumulative L1 ⊂ L2 ⊂ L3) | **R-041** Gate exit criterion = "all in-scope requirements with L ≤ n pass" | `state-machine.yaml`. A gate at release can name an ASVS level as its criterion. Procurement uses the same construct ("developed at ASVS level X"). |
| v4.0.3 ↔ v5.0.0 mapping files | **R-044** `maps_to` edges | 5.0.0 ids that link back to a 4.0.3 id: 190 of 345, each carried with its relation verb. These are source-published, so `kind: stated`. |
| Requirement phase | R-037 `LifecyclePhase` | Our classification: documentation → design, V13 → release, V15 supply-chain items → supply-chain, the rest → implementation. ASVS gives no phase. These values are derived and marked so. |

## Adapt

- **Level-conditional clauses.** Some requirements tighten *within one id* by level. V13.3.1 says: "For an L3
  application, this must involve a hardware-backed solution such as an HSM". The standard says this is
  deliberate ("some requirements apply to a particular level but have more stringent conditions for higher
  levels"). The tmodel `Requirement` needs a per-level parameter or derived sub-requirements. Otherwise an
  L2 pass and an L3 fail on the same id cannot both be recorded.
- **Documentation ↔ implementation pairing.** ASVS asserts each documentation requirement "always" has a
  related implementation requirement, but never enumerates the pairs. We inferred
  `related_documentation_section` for 26 implementation requirements whose text references documentation (count corrected from 27 by the verify pass, 2026-10-02)
  (kind: inferred). A Requirement→Requirement `depends_on` edge is needed (gap in R-042).
- **Forks and tailoring.** ASVS encourages organization-specific forks that keep traceability (F-13,
  F-17). The R-044 crosswalk must key on the base id and treat a fork as a profile with omissions and
  added guidance, never as new ids.
- **Supply-chain items (V15.1.1, V15.1.2, V15.1.4, V15.2.1, V15.2.4).** These are application-level
  checks: SBOM maintained, components from expected repositories, no dependency confusion, remediation time
  frames not breached. They map onto ARCH-0001 `Component` + `supplied_by` Party. They also need a new
  `RemediationTimeFrame` SLA object, which is checkable mechanically against Vulnerability age. They overlap
  SSDF PW.4/PS.3 and SLSA source/build provenance (Lane E siblings `slsa-1-2`, `openssf-osps-baseline`).
- **Crypto registry.** Appendix C's A/L/D tables (`crypto-registry.yaml`, 14 tables, 120 rows) are a
  catalog in the same sense as CWE. A detected use of a `D` mechanism is a finding against V11.

## Reject / do not rely on

- **CWE linkage from ASVS.** 5.0 discontinued CWE and NIST SP 800-63 mappings ("category-only CWEs,
  difficulties in mapping requirements to a single CWE ... imprecise mappings"). The legacy exports keep
  empty `CWE`/`NIST` arrays. The CWE links in `requirements.yaml` (204 requirements) are **composed by us**
  from the v5.0.be "just-in-case" export through the be→5.0.0 id map, and are marked `kind: inferred`. Do
  not use them as authoritative ThreatInstance→Requirement edges. Prefer our own reviewed mapping, or
  OWASP CRE when ASVS publishes it.
- **The CycloneDX export as a level source.** In the 5.0.0 asset every `levels[].requirements` array is
  empty (source defect, `messages.yaml`). Take the level from JSON/CSV `L`.
- **Testability as a level criterion.** ASVS 5 explicitly rejects black-box testability as the L1
  criterion ("The Fallacy of Testability"). Do not equate "automatable check" with "L1".

## Bearing on DEC-009 (mitigation lifecycle)

The documentation → implementation → verification sequence is a mitigation lifecycle with two checkpoints
per control: the decision is documented (verifiable), then the decision is implemented (verifiable). In
DEC-009 terms a `MitigationInstance` derived from an ASVS pair has two evidence obligations, and a
documentation-kind mitigation can be `verified` while its technical twin is still `open`.

## Bearing on threat modeling

ASVS 5 *consumes* a threat model at only one point: V13.1.4 ("based on the organization's threat model and
business requirements"). Elsewhere it consumes "risk analysis" (V7.3.1/V7.3.2, level choice). The tmodel →
ASVS direction is therefore **parameterisation**: a ThreatInstance/RiskScore justifies a documented
decision (a timeout, a rotation schedule, a target level). The direction is not coverage. The
ASVS → tmodel direction is a **conformance check**: an ASVS Requirement that fails at verification is a
Finding on the Product.

## Open questions

1. Should the `Requirement` id in the KG be the versioned ASVS form (`v5.0.0-1.2.5`) or our record form
   (`owasp-asvs-5#v5.0.0-1.2.5`)? The library uses the latter. The ASVS citation inside it is preserved.
2. How should a not-applicable verdict propagate into R-042's threat-model conformance check? ASVS
   requires the N/A to be noted, and the verifier gives an opinion on the exclusions.
3. Should Appendix D's removed SDL process items (AppD-10..16) seed MAP-0001 rows? They are the ASVS
   project's own statement of what an SDL needs, outside its scope.
4. Source defects to report upstream. The CycloneDX levels are empty. "execptions" and "onyly" are typos
   kept verbatim. "1.11.3" in the referencing example does not resolve in 5.0.0.
