---
schema: "library-design-notes/v1"
id: fda-premarket-cybersecurity-guidance-design-notes
record: fda-premarket-cybersecurity-guidance
type: design-notes
updated: "2026-10-02"
---

# Design notes: how the FDA premarket cybersecurity guidance bears on tmodel

Decision ids come from tmodel `spec/ARCH-0001-PROPOSAL-v0.2.0.md` and `design-log/0009-sdl-conformance-object`.
Requirement ids are `fda-premarket-cybersecurity-guidance#…` from `requirements.yaml`.

## Why it matters

This is the most **threat-model-centric** SDL source in the library. FDA does not just ask for a threat model. It asks
for four things:
- the threat model, with the methodology rationale and assumptions (V.A.1-*);
- architecture views that "can therefore be an effective way to provide threat modeling information to FDA" (§V.B.2);
- a risk assessment that captures "the risks and controls identified from the threat model" (V.A.2-*);
- **traceability** across threat model, risk assessment, SBOM and testing (V.A-17).

That chain is the R-042 conformance check, stated as a regulator's review expectation. For cyber devices (FD&C 524B,
since 29 March 2023) the plan, the processes and the SBOM are **statutory**. The Feb 2026 revision re-anchors the
whole guidance on the QMSR / ISO 13485:2016 (21 CFR 820 as amended, effective 2 Feb 2026).

## Adopt

| # | What | tmodel target | Source |
|---|---|---|---|
| A1 | **Traceability as a checkable graph.** Typed edges from ThreatInstance to RiskScore to MitigationInstance to Requirement to Evidence(test), plus Asset to Component(SBOM). A conformance query reports every threat without a traced, tested control. | R-042, ARCH §4 (Assertion edges) | V.A-17, V.B.2-12..16, App2.B-* |
| A2 | **Mitigation kinds.** All three R-040 kinds appear: technical (App. 1 controls), documentation (labeling §VI.A; risk transfer), process (management plan §VI.B; CVD). | R-040 | §V.B.1, §VI |
| A3 | **Architecture views as governed views.** Four named view types (global system, multi-patient harm, updatability/patchability, security use case), each with diagrams and text. A view may be omitted only with an explanation. That is a view-spec with an "omission justification" field. | R-043, ARCH §10 | V.B.2-* |
| A4 | **Premarket submission as a gate.** Appendix 4 Table 1 is an exit-criteria list for the regulatory release gate. Each row is a documentation element, its guidance sections, and its IDE status. | R-041 Gate | App4.T1-*, `messages.yaml` premarket-cybersecurity-documentation |
| A5 | **Vulnerability disposition states.** KEV entries designed out; compensating controls; reasonably foreseeable risk; risk transfer with an information guard; deferred remediation with a plan; controlled vs uncontrolled; regular-cycle vs out-of-cycle patch. See `state-machine.yaml`. | DEC-009 mitigation lifecycle | V.A-07..09, V.A.2-06, V.C-36/37, VII.C.1-09/11 |
| A6 | **Methodology-agnostic threat modeling with a recorded rationale.** "Rationale for the methodology(ies) selected should be provided". This matches tmodel's "STRIDE is a method facet" (ARCH §2). | ARCH §2 | V.A.1-* |

## Adapt

| # | What | Why adapt |
|---|---|---|
| D1 | **Mitigation locus.** Add `locus ∈ {designed-in, user-deployed (compensating), transferred}` alongside R-040 `kind`. FDA's App. 5 *compensating control* is "external to the device design, configurable in the field, employed by a user". | R-040's kind alone cannot tell a firewall the hospital runs from a control in the firmware. |
| D2 | **Security risk vs safety risk.** Keep the exploitability-based security assessment as its own axis, with a documented transfer into the ISO 14971 safety assessment (V.A.2-*). | Matches critic H3. Do not overload S/F/O/P. |
| D3 | **Regime facet.** A `RegulatoryRegime` applicability facet on Product, e.g. `fda-cyber-device` evaluated from the three 524B(c) criteria, or `eu-cra-pde`. It switches which Requirement rows are mandatory. | The same pattern serves the CRA (scope, Art 2) and the UK Code (stakeholder groups). |
| D4 | **Component support attributes.** Add `level_of_support` and `end_of_support_date` to Component, as the SBOM supplement (V.A.4.b-*) requires. Exported as an addendum beside SPDX/CycloneDX (`schema/sbom-supplement.derived.schema.json`). | Not in NTIA minimum elements, so not in the export profiles yet. |
| D5 | **Metrics on the SDL program.** Three SPDF effectiveness metrics (V.A.6-*): % patched, identification-to-patch time, patch-to-field time. Put them on the R-041 program object as derived KPIs. | They are computed from vulnerability state timestamps, so the A5 state machine must keep timestamps. |

## Reject

| # | What | Why |
|---|---|---|
| X1 | Modelling FDA's review procedure (510(k) substantial equivalence, NSE, Q-Sub logistics) as tmodel states. | It belongs to the regulator's process, not the product's threat model. Only the gate outcome is recorded. |
| X2 | Treating Appendix 4 Table 1 as a checklist-only conformance test. | FDA itself says "This table is not intended to serve as merely a deliverable checklist" (App. 4). Conformance must check content and traceability (A1), not file presence. |
| X3 | Importing the App. 1 control recommendations as tmodel `Requirement` rows without context. | They are device-design recommendations scaled by risk ("expected to scale"). As crosswalk rows they need applicability conditions. |

## Crosswalk hooks (R-044)

The guidance publishes **no** mapping table. It names candidate SPDFs (JSP2, IEC 81001-5-1, ANSI/ISA 62443-4-1; §V and
fn 27). It names standards that "may partially meet the security testing recommendations" (fn 48: ANSI/UL 2900,
62443-4-1, IEC 81001-5-1, and others). And it cites AAMI TIR57 / ANSI/AAMI SW96 for security risk management plans and
reports (fn 29, 32). These are references, not mappings. They are recorded in `record.yaml` `cites`, and any mapping we
derive is ours (kind: inferred) and belongs in MAP-0001.

## Open questions

1. **Normativity.** FDA "should" is non-binding (§I), yet for cyber devices failure to comply with 524B(b)(2) "is
   considered a prohibited act under section 301(q)" (§IV.D). A conformance engine needs a per-row
   `normativity` × `regime` matrix, not a single verb.
2. **"Known unacceptable vulnerability"** (524B(b)(2)(A)) is defined only by contrast with "critical vulnerabilities
   that could cause uncontrolled risks". It is not a crisp predicate. The state machine models it as a guard on
   `controlled-risk`, which is our reading (kind: inferred on that transition).
3. **Timelines.** Unlike the CRA's 24 h / 72 h / 14 d, FDA sets no reporting clock here. Postmarket timelines live in
   the 2016 Postmarket Cybersecurity Guidance (a separate record is needed), and 21 CFR 806.
4. **Postmarket guidance not held.** The controlled/uncontrolled-risk examples and CVD timelines it relies on are in
   "Postmarket Management of Cybersecurity in Medical Devices" (2016). It should be ingested.
5. **Version churn.** Final Sept 2023; Level 1 draft reissued March 2024; Level 1 final June 2025;
   Level 2 revisions Feb 2026 (QMSR alignment) — per the guidance's own Guidance History table. Ids in `requirements.yaml` are section-based and so tied to this text.
   When the next revision lands, diff it against this record rather than renumbering.
