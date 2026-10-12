---
schema: "library-distilled/v1"
id: sp-800-218r1-design-notes
record: sp-800-218r1
kind: design-notes
type: design-notes
title: "sp-800-218r1 — bearing on the tmodel design"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# SSDF 1.2 (Initial Public Draft): how it bears on tmodel

**Source status.** This document is an **IPD**. Nothing below should be built on until NIST finalizes SP 800-218r1. Until then, `sp-800-218` (SSDF 1.1) is the authoritative SSDF, and these notes say only where 1.2 would *change* what we take from 1.1. Section references with no document name refer to the draft. tmodel ids come from `ARCH-0001-PROPOSAL-v0.2.0` (§§1–5) and `DL-0009` (R-040…R-044). The model is still a proposal and is not accepted. **[analysis]** marks reasoning that belongs to this extraction and is stated by neither the source nor our documents.

## Adopt

- **The task as the atomic conformance unit (R-042).** Every SSDF 1.1 task id (PO.1.1 … RV.3.4) carries over to 1.2 unchanged, and since 1.0 ids are never renumbered or reused: moved or merged ids persist as retired "Moved to …" rows. That is exactly the citation discipline `docs/requirements.md` §3b asks for. Adopt `sp-800-218r1#<task>` as a `Requirement` id, with a 1:1 `same_task_as` link to `sp-800-218#<task>`. The link carries a `text_changed` flag for the 8 reworded tasks (see `diff-vs-v1.1.md`).
- **The References column as published crosswalk data (R-044).** The table has 497 reference lines, 1,548 identifiers and 29 schemes. Every line is published *by NIST* as a task→framework mapping, so it is not our own curatorial judgement. These are first-class `maps_to` edges with provenance `asserted_by: NIST (SP 800-218r1 ipd)`. They seed MAP-0001: SSDF ↔ BSIMM ↔ SAMM ↔ IEC 62443-4-1 ↔ SP 800-53 ↔ MS SDL ↔ SAFECode are mapped *by the source*. MAP-0001's cells are hand-built and marked *approx*. Where an SSDF reference exists, it should replace them.
- **PO.4 "criteria for software security checks" as the Gate exit criterion (R-041).** Together with PO.1.2 Ex 2 ("verify compliance at key points in the SDLC (e.g., classes of software flaws verified by gates …)"), this is the SSDF's only explicit gate concept. MAP-0001 row 15 already treats it as the hook for `Gate` exit criteria, and 1.2 keeps it unchanged except for wording.
- **PW.1.1 risk modeling is the anchor that links SSDF and tmodel.** "Use forms of risk modeling (e.g., threat modeling, attack modeling, attack surface mapping)". A tmodel threat model *is* the deliverable for PW.1.1. **[analysis]** A conformance check can therefore treat "a threat model exists for the product version, reviewed and current" as the evidence for PW.1.1. Pair it with PW.1.2 (requirements, risks and design decisions recorded) and PW.2.1 (independent design review): together they are exactly the automated "threats mitigated" check that DL-0009 R-042 describes.
- **Mitigation kinds (R-040).** The notional examples fall cleanly into the three kinds R-040 proposes. *Technical*: PS.4.3 rollback, PW.9.1 secure defaults, PW.6.2 compiler hardening. *Documentation*: PW.9.2 setting documentation, RV.2.2 Ex 3 security advisories, PS.2.1 integrity information. *Process*: PO.2.2 training, RV.1.3 PSIRT, PO.6 improvement plan. This is supporting evidence for R-040's three-way enum.

## Adapt

- **Two kinds of requirement.** SSDF tasks constrain the *producer's process*. The producer's own SecurityRequirements (PO.1.2) constrain the *software*. DL-0009 calls both `Requirement`. Adapt with `Requirement.level ∈ {process, product}` or something equivalent. A Gate's exit criteria cite process requirements, while a threat model's MitigationInstances discharge product requirements. Without the distinction, the conformance check counts the wrong things.
- **Gate order (R-041).** §2 (lines 311–313) says the order of practices, tasks and examples "is not intended to imply the sequence of implementation or the relative importance". R-041 wants ordered, named, dated gates, so the mapping of SSDF tasks onto gates is **ours**. Record it as our `Assertion`, not as a fact about the SSDF. MAP-0001's canonical phase line is the right place for it. The `phase` value in `requirements.yaml` is derived and is marked as such.
- **Notional examples become MitigationInstance templates, never obligations.** "No examples or combination of examples are required" (§2, lines 302–303). They belong in a catalog of candidate mitigations, as a sibling of D3FEND in ARCH-0001 §1.3, and must be excluded from conformance counts.
- **Shared responsibility (ARCH-0001 §2b).** §1 (lines 273–280) has the tenant agree with each provider "which party is responsible for each practice and task and how each provider will attest to their conformance". Adapt §2b's relational roles by adding a `responsible_for` edge (Party → Requirement) and an attestation `Assertion` (§4) per party, so the platform's share and the tenant's share are checked separately.
- **The update lifecycle is new in 1.2 (PS.4) and touches ARCH-0001 §3b.** PS.4.1–PS.4.4 cover testing all releases, tiered or canary roll-out, rollback to the last known good version, anti-rollback protection and resilient update engines. §3b has a `maintenance/update` phase but no update *event*. Adapt by modelling a `SoftwareUpdate` transition on `ProductInstance`, from version N to N+1, with `rollback_to`. The same machinery R-038's future state machine needs. Threats scoped `applies_in_phase=maintenance/update` include malicious or faulty updates and rollback to a vulnerable version (PS.4.3 Ex 3).
- **Governed, disclosure-controlled threat-model views (R-043).** New PW.1.1 Ex 5: "Consider processes for creating and sharing under controlled disclosure the risk and threat models used during software development to inform customer risk management decisions." This is a direct use case for R-043. The threat-model report is a governed view whose *audience* (internal or customer) and *disclosure level* are governance metadata.

## Reject / do not carry

- **EO 14028 mappings from 1.2.** The draft removes EO14028 from every task and drops the §4e mapping appendix. For EO 14028 / OMB M-22-18 / CISA attestation-form traceability, use `sp-800-218` (1.1) or the CISA form itself. Do not infer that 1.2 dropped the obligations, because it only dropped the mapping.
- **Edition-free crosswalk keys.** The references are stale editions: BSIMM12 (2021), SAMM 1.5 (2017), ASVS 4.0.3 and CSF 1.1 for all pre-existing tasks. Our library holds `bsimm-16`, `owasp-samm-2` and `owasp-asvs-5`. **Do not** treat an SSDF `BSIMM: SM1.1` edge as pointing at BSIMM16's SM1.1 without a version-translation step. Every `maps_to` edge must carry the edition. In `requirements.yaml`, `target_record` is set only where the edition matches.
- **SSDF as a checklist.** The draft repeats that "The intention of the SSDF is not to create a checklist to follow" (§1, lines 270–272). Any tmodel conformance score must be framed as *coverage of selected tasks*, with risk-based scoping (R-0003, R-0005), and never as pass/fail against all 49 tasks.

## Decisions touched

| id | how |
|---|---|
| R-040 (mitigation kind) | Examples split into technical, documentation and process (above). This supports the enum. |
| R-041 (SDL / Gate) | PO.4 criteria and PO.1.2 Ex 2 gates give the exit criteria. Gate order is ours, not the SSDF's. PO.6 (new) supplies the program's improvement loop. PS.4 (new) supplies release and update gates. |
| R-042 (conformance) | The task is the atomic unit. PO.3.3 "artifacts" and fn 6 (artifact = "a piece of evidence", evidence = "grounds for belief or disbelief …") supply the Evidence object directly. |
| R-043 (governed views) | PW.1.1 Ex 5 calls for controlled-disclosure sharing of threat models with customers. |
| R-044 (crosswalk) | 497 NIST-published reference lines. They need edition-aware edges. 1.2 re-maps SP 800-53 to Release 5.2.0 and SP 800-161 to r1-upd1. |
| DEC-009 (mitigation lifecycle) | RV.2.2 risk responses (remediate, or mitigate temporarily until permanent), approved exceptions with periodic review (PO.1.2 Ex 7, RV.2.2 Ex 5), and PO.6.3 "periodically review prior decisions" together give the lifecycle states *planned → temporary-mitigation → remediated*, plus *accepted (exception) → re-reviewed*. |
| ARCH-0001 §2b (Party) | Producer, acquirer, supplier and platform-provider roles; per-task responsibility. |
| ARCH-0001 §3b (LifecyclePhase) | PS.4 adds the update and rollback transitions. |

## Open questions

1. Will the final SP 800-218r1 keep PO.6 and PS.4 as drafted? The draft asks reviewers whether more tasks are needed. Re-extract on finalization and diff it against this record.
2. Should our crosswalk link `sp-800-218#X` ↔ `sp-800-218r1#X` with an explicit edge, or treat the two as one requirement line with versions? `docs/requirements.md` §3b requires the citation to resolve to a version. The proposal is separate ids plus a `same_task_as` edge.
3. The draft maps PO.1.3 (supplier requirements) to SP 800-53 CA-03, SA-04 and SA-21 only, and no longer to SP 800-161 at all. In 1.1 it mapped to SA-4, SA-9, SA-10, SA-10(1), SA-15 and SR-3/4/5. Is that intended or a drafting defect? It matters for the supply-chain row of MAP-0001.
4. The draft is internally inconsistent in three places: "Protect Software (PS)" vs "Protect the Software (PS)"; "Appendix C" vs Appendix B for the change log; and a change log that under-reports changes (2 task-text changes listed, 8 found). These are recorded and not fixed. Worth a public comment if NIST reopens one.
