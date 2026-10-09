---
schema: "library-distilled/v1"
id: iso-iec-27034-1-design-notes
record: iso-iec-27034-1
type: design-notes
updated: "2026-10-02"
---

# ISO/IEC 27034 — design notes for tmodel

Targets: ARCH-0001 v0.2.0 (§1 layers, §2b Party, §3b LifecyclePhase, §4 Assertion/Review,
§5 mitigation/review) and DL-0009 (R-040 mitigation kind, R-041 SDL/Gate, R-042 conformance,
R-043 governed views, R-044 crosswalk), DEC-009 (generic→product mapping, mitigation lifecycle).
Evidence base: 27034-1 preview only, plus the previews of Parts 2, 3, 5, 7 and DIS 4, plus the free
TS 27034-5-1 XSD (see `object-model.yaml` for locators). **Nothing here rests on the unread body
of 27034-1.** Where a conclusion would need it, the conclusion is listed under open questions.

## Adopt

| # | 27034 concept | tmodel target | Why |
|---|---|---|---|
| A1 | **Verification measurement bound to every control** (27034-5 §5.1; 27034-7 §3.13) | R-042: `MitigationInstance` —`verified_by`→ `VerificationProcedure` —`produces`→ `Evidence` | Conformance can be automated only if each mitigation says how it is verified and what evidence counts. 27034 makes this mandatory (M) for every ASC. |
| A2 | **Actual vs Targeted Level of Trust** (27034-1 §3.2, §0.4.4) | R-041 gate exit criterion; R-042 verdict | A gate passes when every requirement selected by the target has verified evidence and a reviewer agrees. §0.4.4 is the rule written down: "cannot be declared secure unless the auditor agrees …". Record the verdict as a `Review` on an `Assertion` (ARCH-0001 §4), not as a boolean. |
| A3 | **Requirement provenance on the control**: `requirements-addressed/requirement {context, type, name, description, source}` (XSD) | R-044 `Requirement` with `source` → library record id + native id | The XSD already has a `source` slot per addressed requirement, which is exactly where a crosswalk id (`sp-800-218#PW.1.1`, `iso-sae-21434-2021#RQ-15-…`) belongs. |
| A4 | **Map the local lifecycle to a reference model** (27034-1 §0.2; XSD label "MAP APPLICATION LIFE CYCLES USED IN THE ORGANIZATION TO THE REFERENCE MODEL"; 27034-1 Annex A maps Microsoft SDL) | R-041 "canonical phase + local name" | Same pattern DL-0009 proposes, with a standard behind it. Annex A (ToC) shows the mapping can be published as data. |
| A5 | **RACI on activity roles** (27034-2 §5.4.2; 27034-3 §5.3.2; XSD `rasciLabel`, `responsibility-matrix-type` RACI/RASCI) | ARCH-0001 §2b relational role edges gain a `responsibility` qualifier | Gives R-043 governed views a defined owner/approver vocabulary instead of free text. |

## Adapt

| # | 27034 concept | Adaptation |
|---|---|---|
| D1 | **ASC as one fused object** | Do not fuse. Keep tmodel's split (`Requirement`, `MitigationInstance{kind}`, `VerificationProcedure`, `Evidence`) for graph queries and DEC-009 reuse, and provide an **ASC view**: a governed projection (R-043) that renders those four nodes as one 27034-shaped control and can be exported as an `asc:asc` instance. R-040's `kind ∈ {technical, documentation, process}` covers ASCs whose security activity is a process step (e.g. Annex A.9.1 "Training"). |
| D2 | **ONF / ANF** | ONF ≈ the org's SDL definition plus its approved catalogue of generic Requirements and Mitigations (DEC-009 generic layer), owned by a Party (the ONF Committee) and versioned and approved per iteration. ANF ≈ the per-Product SDL instance: the applicable requirements and chosen MitigationInstances with their evidence. Model ANF —`derived_from`→ ONF as a typed edge, so a change in the ONF can be flagged against every ANF built from it. |
| D3 | **ASLCRM 2-D grid vs `LifecyclePhase` enum** | Keep the 1-D enum as the threat-scoping axis (§3b). Add the 27034 *layer* (management / supply / infrastructure / audit) as an optional facet on SDL activities and gates, not on threats. Map the 27034 operation-stage areas Archival and Destruction to tmodel `end-of-support` and `decommission/disposal`. |
| D4 | **Execution moment** (BEFORE / DURING / AFTER an ASLC activity; ONCE / PERIODIC / ON_EVENT) | Express a control's schedule relative to a Gate (before or after the gate) and allow periodic or on-event re-verification, e.g. re-running the verification when a dependency changes. This refines `applies_in_phase` for mitigations only. |
| D5 | **ASC lifecycle + staged signed approvals** | Reuse the Assertion/Review spine. Each control-definition stage approval is a `Review` with stage, approver Party and signature reference. Do not import the 11-value enum verbatim; map it to draft → reviewed → approved → active → retired. |
| D6 | **Expected Level of Trust / PASR** (27034-7) | Later (post-MVP): a rule for carrying evidence from ProductInstance vN to vN+1. A PASR is an `Assertion` ("verification of control X is still valid for vN+1, because …") that the application owner approves. A "substantial change" (27034-7 §3.14) revokes it. This needs ARCH-0001 §3b's missing `valid_from`/`valid_to` axis. |

## Reject (for now)

| # | What | Why |
|---|---|---|
| X1 | Importing the XSD's activity-label enumerations (221 non-CUSTOM labels, much of them PMBOK-style project management and records-management text) | Too fine and too project-management-specific for a threat model. Keep the `CUSTOM` escape hatch and the layer and stage structure only. |
| X2 | ASC package e-signature format (`e-signature-param` / `e-signature-data` strings) | Under-specified (opaque strings, no algorithm or profile). tmodel signing goes through its own provenance and export decisions, not through this. |
| X3 | Using Part 4 vocabulary as normative | ISO/IEC 27034-4 never published. ISO open data lists NP 27034-4 at 10.98, DIS 27034-4 at 40.98 and PWI 27034-4 at 00.98: all cancelled. Its DIS terms are design input only. |

## Bearing on decisions

- **R-041 (SDL / Gate):** A2, A4, D3, D4. A gate's exit criterion is "Actual LoT ≥ Targeted LoT
  for this application", evaluated over the controls selected by the target.
- **R-042 (conformance):** A1, A2, D1. 27034 is the clearest standard statement that conformance is
  *evidence produced by a declared verification, accepted by a named reviewer*.
- **R-043 (governed views):** D1, D2, D5, A5. The ONF is itself a governed artefact with an owner
  (the ONF Committee), PDCA iterations and an audit (27034-2 §5.4).
- **R-044 (crosswalk):** A3. Annex B (ToC) of 27034-1 renders a NIST SP 800-53 control (AU-14) in
  ASC format. The ASC is offered as a lingua franca for controls from other catalogues.
- **R-040 (mitigation kind):** D1. Annex A.9 (ToC) groups example ASCs by Training, Requirements,
  Design, Implementation, Verification and Release, so ASCs include process and documentation
  kinds, not only technical ones.
- **DEC-009:** D2. ONF→ANF is generic→product at the SDL level.

## Open questions

1. The 27034-1 definitions of ASC, ONF, ANF, ASLC Reference Model, level of trust and Targeted
   Level of Trust (Clause 3 after 3.2, and §8.1.2.6) were **not read**. The definitions used here
   come from Parts 2, 3, 5 and 7. Do they match Part 1 word for word? A purchased copy, or ISO OBP
   access from a browser (iso.org returned HTTP 403 to every automated request on 2026-10-02),
   would settle it.
2. Is the 27034-1 ASLCRM (Fig. 8) the same grid as the TS 27034-5-1 XSD? 27034-5 "further details"
   it, so Part 1 may be coarser.
3. Are the ASC lifecycle transitions ordered as the enumeration suggests? Is PUBLISHED_FOR_TRAINING
   mandatory before ACTIVE?
4. How do levels of trust compose? The XSD gives `level` as an integer, which suggests an order. Is
   a control mandatory at level N also mandatory at every level above N? That cannot be
   established from what was read.
5. Is the series being redesigned? A secondary source (iso27001security.com) says a revision
   restarted in 2025 as a PWI. ISO open data (2026-09-30) shows "ISO/IEC PWI 27034" at stage 00.98,
   i.e. abandoned. No successor is active, so the 2011–2018 texts stand. Watch SC 27 for a new
   item.
6. Source defects to track: the XSD namespace differs from the TS 5-1 §5.3 text, and the file
   declares `version="1.81"` in its XML declaration (`schema/README.md`).
