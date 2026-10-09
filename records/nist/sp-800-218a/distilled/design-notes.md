---
schema: "library-design-notes/v1"
id: sp-800-218a-design-notes
record: sp-800-218a
type: design-notes
kind: design-notes
title: "sp-800-218a — bearing on our design"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

**Conventions.** Ids such as `PO.1.2.R1` belong to SP 800-218A (namespace
`sp-800-218a#`). Our documents are cited by id: ARCH-0001-PROPOSAL-v0.2.0 (§n),
DL-0009, MAP-0001, and R-040…R-044 and DEC-009. **[analysis]** marks this
extraction's reasoning; the source and our documents do not state it.
**[source-defect]** marks an inconsistency inside 218A itself. Nothing here is
accepted: R-040…R-044 are DL-0009 proposals, and the SDL work is post-MVP under
ADR-0002.

## 1. What 218A is to our model

218A is an **overlay** on SSDF 1.1. It adds 6 tasks and 1 practice, changes 3 tasks and
2 practices, and attaches 86 R/C/N items and a Priority to all 48 tasks. It is not a
standalone set of requirements ("should not be used without SP 800-218", §1). For
MAP-0001 / R-044, this means a profile is a **typed, versioned edge set over a base
requirement set**, not a parallel framework.

## 2. Adopt / adapt / reject

| # | 218A element | Disposition | Our id | Notes |
|---|---|---|---|---|
| 1 | Profile = base requirement set + per-task Priority + R/C/N additions + status (unchanged / modified / new) | **Adopt** as the shape of a tailored Requirement set | R-042, R-044 | **[analysis]** DL-0009 already says corporate SDLs rename gates. A profile is the requirements-side equivalent: the same base, tailored. Model `ProfileMembership(profile, requirement, priority, status)` as an edge with attributes. Keep the base requirement node unchanged. |
| 2 | Native addition ids `PO.1.2.R1` (§3) | **Adopt** verbatim as Requirement ids | R-044 | Stable, source-defined, and citable. We use them as `sp-800-218a#PO.1.2.R1`. |
| 3 | Normativity levels R (should do), C (should consider), N (informative) | **Adopt**, adding a `normativity` attribute on Requirement with at least `recommendation / consideration / informative` | R-042 | A gate exit criterion (R-041) should be able to require all R items and ignore C/N. Without the level, C items would turn into hard checks. |
| 4 | PW.1.1 + PW.1.1.R1 (AI threat types in risk modelling), PW.1.1.C1 (re-model future versions/derivatives) | **Adopt**: a tmodel threat model is the evidence for PW.1.1; the seven named AI threat types seed the AttackPattern catalog | R-042, DEC-009 | The R-042 check "every in-scope ThreatInstance has an approved MitigationInstance" is how PW.1.1 + PW.2.1 conformance gets automated. PW.1.1.C1 requires a re-verification trigger on a new model version (gap 8). For agentic systems, the MAESTRO method facet (ARCH §2) is the natural carrier. |
| 5 | PW.1.1.C2: "consider checking that the AI model is not in a critical path to make significant security decisions without a human in the loop" | **Adopt** as a design-review check on the DFD: a Process realized_by an AIModel Component, on a security-decision path, with no Review/HITL node | R-042 | **[analysis]** This can be checked mechanically as a graph query over §0 projections. It is a good candidate for a demonstration conformance rule. |
| 6 | PW.2.1 modified: an independent qualified human **and** automated toolchain review (SSDF 1.1 had "and/or") | **Adopt** for the Review model: a design Gate needs both a human Review and an automated Assertion | R-041, §4 | Matches the ARCH §4 "AI proposes → human accepts" rule. In 218A the human is mandatory, not optional. |
| 7 | PO.4.1.C1: human-in-the-loop approval for security checks "beyond risk-based thresholds" | **Adapt**: a Gate criterion carries a threshold; when it is exceeded, an approving Review is required | R-041 | 218A makes this a C item. We would make it configurable per gate. |
| 8 | §2 shared-responsibility agreement (task → responsible party → how conformance is attested) | **Adopt** as a new edge `responsible_for(Party, Requirement)` plus an agreement node | R-041, R-042, ARCH §2b | Lets the R-042 conformance check run across a producer / integrator / acquirer chain. It fits the §2b rule that relational roles are edges. |
| 9 | Mitigations that are documents (data/model/system cards PO.1.2.N1, training process documentation PS.3.1.R3, policies) | **Adopt** as evidence that R-040 `kind: documentation` is needed | R-040 | 218A mixes technical (PS.1.3.R4 encryption/signatures), documentation (PS.3.1.R2/R3) and process (PO.2.2 training) mitigations for one risk family. This is exactly R-040's three kinds. |
| 10 | Dataset purpose (training / testing / fine-tuning / aligning) and "document which data do not have known provenance" (PW.3.2) | **Adapt**: add `purpose` to the DataStore/Asset classification (R-029). Represent provenance as `known / unknown-documented / untracked` | ARCH §4, R-025 | **[analysis]** An open-world graph cannot distinguish "no provenance edge yet" from "provenance known to be unknown". PW.3.2 needs the second state to be stated explicitly, which takes an Assertion with value `unknown`. |
| 11 | AIModel parts that are protected separately (weights, config parameters, reward model, adaptation layers) | **Adapt**: add Component subtypes. Express the separation rules (PS.1.1.R3, PS.1.3.R1) as `stored_in` constraints | ARCH §0/§1 | Post-MVP. |
| 12 | Development environments, including the "AI model training" environment (PO.5 modified), protected and monitored (PO.5.1, PO.5.3) | **Adapt**: a DevelopmentEnvironment node distinct from the deployment `Environment` (§3), scoped by LifecyclePhase `implementation` / `production` | ARCH §3b, R-037 | The dev/training environment is an attack surface in its own right (supply-chain tamper in *production* — §3b). |
| 13 | RV.2.2.R2: criteria for when to stop using a model and roll back to a previous version | **Defer** to the §3b state machine (post-MVP). Record it as a requirement on the future ProductInstance operational state machine | DEC-009, R-038 | 218A implies the states in-use → stopped → rolled-back but defines no transitions. We do not invent them (see `not_applicable: state-machine`). |
| 14 | Provenance via SBOM / SLSA (PS.3.2 modified), tool versions in provenance (PW.6.2.C1) | **Defer** to the radar contract (ADR-0001); build/supply-chain provenance is out of MVP (ARCH §4) | ADR-0001 | Do not pull SLSA provenance into the epistemic Assertion spine (DL-0009 critic M5). |
| 15 | Informative References to AI RMF / OWASP LLM Top 10 v1.1 / NIST AI 100-2 | **Adopt** as R-044 `maps_to`, keeping the source spellings | R-044 | Both targets have since been revised (OWASP Top 10 for LLM 2025; AI 100-2 E2025). The mapping is pinned to the versions 218A cites, so do not silently retarget it. |
| 16 | The priority ordering itself | **Reject** as a model attribute of the base Requirement | — | The Profile says priorities are "a starting point for organizations to assign their own". Priority is profile- and organization-local. |

## 3. Source defects and traps

- **[source-defect] PW.3 reuses retired identifiers.** SSDF 1.1 retired PW.3, PW.3.1
  and PW.3.2 ("Retired identifiers for deleted/moved practices and tasks", SP 800-218
  change log; PW.3.1 → PO.1.3, PW.3.2 → PW.4.4). 218A gives PW.3 / PW.3.1 / PW.3.2 a new
  meaning (data integrity before use) and adds PW.3.3. The SSDF 1.2 IPD (Dec 2025)
  still lists "Verify Third-Party Software Complies with Security Requirements (PW.3):
  Moved to PW.4". A bare `PW.3.1` is therefore ambiguous across the SSDF family. **Our
  crosswalk must always key on (record, native id).**
- **[source-defect] PO.5.2 was changed silently.** The 218A text drops "i.e.," and
  shortens "development-related tasks" to "development tasks". It is not tagged
  "Modified from SSDF 1.1", even though §3 says untagged practices and tasks are
  unchanged. The change is editorial and does not alter meaning, but a strict
  text-equality crosswalk would flag it.
- **~~The PS group is renamed.~~ Withdrawn by the verify pass (2026-10-02).** The 218A
  group row reads "Protect Software (PS)", and so does the SSDF 1.1 Table 1 group row
  (SP 800-218 §3, Table 1). Only SSDF 1.1 §2 prose says "Protect the Software (PS)". The
  Profile copies the base table; there is no rename.
- **PO.1 expands an abbreviation.** "SDLC" becomes "software development life cycle
  (SDLC)". The change is editorial, untagged, and correct.
- **EO 14110 is gone.** The Profile exists to satisfy EO 14110 §4.1.a. EO 14110 was
  revoked on 2025-01-20 by EO 14148. NIST still lists 218A as final and the SSDF
  project page still links it, so the document stands. Its *mandate* has lapsed,
  though, and the "dual-use foundation model" definition in the glossary comes from
  the revoked order.

## 4. Open questions

1. Should a profile be a library record of its own (as here) **and** a first-class
   object in tmodel (a `RequirementSet` with `profiles` → base)? 218A and the SSDF 1.2
   IPD will both need the same overlay mechanism. **[analysis]** Yes. Otherwise every
   sector profile duplicates SSDF.
2. Where should Priority live when two profiles disagree, for example an
   organization adopting both 218A and a future sector profile?
3. Can the R-042 "threats mitigated" check consume OWASP LLM Top 10 ids (e.g. `LLM03-7d`)
   directly as AttackPattern ids? A small catalog record would be needed. No OWASP LLM
   Top 10 record exists in the library yet (gap).
4. 218A puts "performance issues" in the same reporting channel as security
   (RV.1.1.R2). Is performance degradation a Finding class in tmodel, or out of scope?
