---
schema: "library-distilled/v1"
id: esf-sscs-developers-2022-design-notes
record: esf-sscs-developers-2022
type: design-notes
updated: "2026-10-02"
reviewed_by: ""
---

# ESF developer guide — design notes for tmodel

The richest object-model source in lane B: it is literally organised as *threat scenario →
recommended mitigation → lifecycle phase*, which is tmodel's own spine applied to the SDL itself.

## Adopt

- **Threat-model governance rules (R-043).** §2.1 "Threat models": created by impartial senior
  architects; cover all critical software components *and all critical systems in the build
  pipeline*; reviewed against code and build systems on an ongoing basis; **updated as
  functionality changes, for major releases, or minimally at least annually**; shared with
  internal teams that pick up the components; **reviewed and approved by at least two independent
  engineers**. These are directly implementable as constraints on tmodel's governed threat-model
  view: approval quorum (≥2 `Review`s by independent `Party`s), refresh triggers, and a staleness
  check (> 1 year since last approved version).
- **Release criteria as gate exit criteria (R-041, R-042).** §2.1 "Release criteria" lists what a
  release gate checks: no unacceptable vulnerabilities pending after required threat modeling and
  testing, environment hygiene maintained with artifacts stored, practices followed with artifacts
  stored (design docs, threat model, test results, open issues), SBOM produced and validated,
  binaries signed, crypto standards met, OSS standards met. The "no unacceptable vulnerabilities
  after threat modeling" criterion is exactly DL-0009's automatable "every in-scope threat has an
  approved mitigation" check.
- **Checklist as conformance template (R-042, R-044).** Appendix D's 60 measurable-outcome
  questions with Yes/No/NA/Inc + description + SSDF tasks + artifact examples is a ready-made
  conformance record shape: `Requirement` × verdict × evidence × crosswalk. Adopt the four-valued
  verdict (incl. *Incomplete*) and the "brief description / alternative practice" field.
- **Mitigation kinds (R-040).** Recommended mitigations split naturally into technical (MFA,
  hermetic builds, ASLR/DEP flags, signing), documentation (threat models, test plans, release
  criteria, SBOM) and process (code review, nightly builds, training, OSRB approval).
- **Phase-scoped threats (ARCH-0001 §3b, R-037).** The guide's phases (criteria/management,
  develop, verify third-party, harden build, deliver) give `applies_in_phase` values for SDL threats.

## Adapt

- **Build environment as an asset.** §2.4 treats repositories, build systems, signing servers and
  the engineering network as the attack surface (4-step build-chain exploit; 5 injection points).
  ARCH-0001's `Environment` is the runtime deployment. A threat model *of the SDL* needs the
  dev/build environment as `Component`s; propose a `dev-build` Environment kind in iteration 7.
- **Evidence visibility (R-043).** Appendix D's availability classes (public / NDA / government-
  mandated / confidential) → a visibility attribute on Evidence and on governed views; §2.1 also
  asks for security procedures to be "made publicly available ... without divulging sensitive
  security information".
- **SSDF version drift (R-044).** Table 1 cites PW.3.x, which SSDF 1.1 final moved into PW.4; the
  guide was written against the SSDF 1.1 draft. Crosswalk edges must carry the target version.

## Reject

- The guide's SLSA table (Appendix C) as a normative source: it quotes SLSA *alpha* (2022); use
  slsa-1-2 for build-provenance requirements.

## Bears on

R-040, R-041, R-042, R-043, R-044, DEC-009 (vulnerability tracking with CWE/CVSS, PSIRT, secure
update delivery as the post-release mitigation lifecycle), R-037 (phase scoping).

## Open questions

1. Ingest Parts 2 (Suppliers, Oct 2022) and 3 (Customers, Nov 2022) of the series — Appendix A
   already cites their sections.
2. Should the 40 threat-scenario items become a generic SDL threat catalogue in tmodel (an
   `AttackPattern` library for the development process itself)?
3. Source defects: Appendix A cites "2.2.1.4 Code Reviews" where the body's item 4 is "Map
   features to requirements"; "24.1"/"23.2" typos; checklist prints "P0.4.2". Recorded in
   crosswalk.yaml / requirements notes.
