---
record: sp-800-218
kind: design-notes
title: "sp-800-218 — bearing on the tmodel design (SSDF 1.1)"
extracted: "2026-10-02"
reviewed_by: ""
---

**Scope and voice.** SSDF identifiers (`PO.1.2`, `PW.2.1/E2`) refer to SP 800-218 Table 1, and
"/En" is notional implementation example n. Our own decisions are cited by id: ARCH-0001-PROPOSAL
v0.2.0 §n, DL-0009, R-040..R-044, DEC-009 and MAP-0001. Text marked **[analysis]** is reasoning
from this extraction, not something the source or our documents say. Nothing here is accepted.
DL-0009 says SDL is post-MVP and ADR-gated, and only R-040 (mitigation kind) is MVP-adjacent.

## What SSDF 1.1 is for us

The SSDF is the **backbone requirement set** for the SDL object. It provides:

- 42 atomic, stably identified, outcome-based tasks;
- a published crosswalk to 29 other practice documents: 528 task→scheme lines and 1,483
  identifiers;
- an explicit mapping from a regulation (EO 14028 §4e, Appendix A).

It is the only SDL source in our set that is free, machine-readable (NIST's xlsx), and
identifier-stable with retired ids kept (Appendix C). That makes it the natural **hub** of the
R-044 crosswalk: other frameworks map *to* SSDF tasks, and the SSDF's References column provides
many of those edges already.

## R-044 — requirements crosswalk (adopt)

- **Adopt** SSDF task ids as hub Requirement ids: `sp-800-218#PW.1.1` and so on. The
  `maps_to` entries in `requirements.yaml` are the source's own edges, so they enter the graph as
  *stated* crosswalk edges with provenance "NIST SP 800-218 Table 1". MAP-0001's cells are
  *authored* (ours) and many are marked *approx*. The two must stay distinguishable:
  `Assertion.source = sp-800-218` versus `Assertion.source = MAP-0001`, per ARCH §4.
- **Check MAP-0001 against the source.** **[analysis]** A cell-by-cell comparison is left to
  the cross-check pass, but several MAP-0001 cells can already be tested against the SSDF's own
  References. Examples:
  - MAP row 3 (threat modeling) puts BSIMM "AA+AM approx" against PW.1.1. SSDF PW.1.1 cites
    `BSIMM: AM1.2, AM1.3, AM1.5, AM2.1, AM2.2, AM2.5, AM2.6, AM2.7, SFD2.2, AA1.1, AA1.2, AA1.3,
    AA2.1`, so "approx" can be dropped for BSIMM.
  - MAP row 3, IEC 62443-4-1 "SR-2": SSDF PW.1.1 cites `IEC62443: SM-4, SR-1, SR-2, SD-1`.
  - MAP row 15 (release gate) assigns PO.4.1/PO.4.2. That fits, because PO.1.2/E2 is the SSDF's
    only use of the word "gates".

  The cross-check pass should diff each MAP-0001 SSDF/BSIMM/SAMM/62443 cell against
  `crosswalk.yaml`.
- **Edition skew is a crosswalk hazard.** SSDF 1.1 maps to BSIMM12 (2021), OWASP SAMM **1.5**,
  ASVS 4.0.3, MASVS 1.4.2, SP 800-161r1 *second draft*, and SP 800-216 *draft*. SAMM 2.x
  renamed streams, and BSIMM has moved on (BSIMM15 or later). A `maps_to` edge must therefore
  carry the **target edition**: the scheme key alone is not enough. **Adapt:** R-044 edges get
  `target_version`, taken from the References entry. (`requirements.yaml` now carries a
  `reference_editions` map, scheme key → cited edition + `target_record` where the library holds
  that edition; verify pass 2026-10-02.)
- The SSDF's own identifier rules (retired ids kept, `[Formerly PW.3.1]`) are a precedent for
  R-044 versioning. Requirements are never renumbered, and a `retired_into` edge lets 1.0
  citations resolve.

## R-042 — conformance check (adopt, with a two-tier Requirement)

- **[analysis]** The SSDF has **two requirement tiers**. Framework tasks say what the SDL must
  do. Product SecurityRequirements (PO.1.2, PW.1.2) say what the software must meet. DL-0009
  defines one `Requirement`. **Adapt:** use `Requirement.tier ∈ {framework, product}`, linked by
  `satisfied_via`. For example, PW.1.2 is satisfied when product SecurityRequirements, risks and
  design decisions are tracked.
- DL-0009's conformance rule is "every in-scope ThreatInstance has an approved
  MitigationInstance". That rule is exactly the evidence for **PW.1.2 + PW.2.1**:
  - PW.1.2/E1: "Record the response to each risk, including how mitigations are to be achieved
    and what the rationales are for any approved exceptions".
  - PW.2.1: an independent or automated review confirms that the design "satisfactorily
    addresses the identified risk information".

  So the automatable threats-mitigated check *is* an SSDF conformance check. It is the strongest
  single justification for R-042.
- The **testable** values in `requirements.yaml` come out as 25 yes, 17 partial, 0 no. The
  partials mostly turn on adopter-defined terms (§2: "well-secured", "qualified person") or on
  unstated frequencies ("periodically", and §1 says "Any stated frequency for performing
  practices is notional"). **Adapt:** the SDL object carries a **term binding and frequency
  binding** per adopter. Without it, partial tasks cannot be evaluated.
- **Responsibility per task.** The §1 shared-responsibility agreement and its attestation call
  for `ConformanceRecord.responsible_party`. A conformance result is (Task, Party, evidence,
  verdict), not (Task, verdict).

## R-041 — SDL / Gate (adapt)

- The SSDF **denies sequence**: "the order of the practices, tasks, and notional implementation
  examples in the table is not intended to imply the sequence of implementation" (§2). It names
  gates only in PO.1.2/E2. **Consequence:** Gate order and names come from the adopter's SDLC
  (DL-0009's ordered, named, dated gates) or from a phase-ordered framework (MS SDL, IEC
  62443-4-1). The SSDF supplies **exit criteria**, not gates:
  - PO.4.1 criteria: KPIs, KRIs, severity scores, Definition of Done.
  - PO.4.1/E5 recorded outcomes: "approvals, rejections, and exception requests".
  - PO.4.2/E3 automated decision-making.
- The `phase` values in `requirements.yaml` are **derived** (ours), so that tasks can be placed
  on the DL-0009 canonical phase line. They are reviewable, not source facts.
- PO.2.3/E1, "accountable for releasing software to production", is the release-gate approver
  role. Map it to the Gate approver `Party` role, following the ARCH §2b one-identity rule.

## R-040 — mitigation kind (adopt)

The 198 notional examples sort naturally into the three R-040 kinds:

- **technical**: PS.1.1/E3 "Use commit signing", PW.6.2/E4 compiler hardening, PW.9 secure
  defaults;
- **documentation**: PW.9.2 administrator documentation, PO.1.2 policies, RV.2.2/E3 advisories;
- **process**: PO.2.2 training, PW.7.2 peer review, RV.1.3/E4 PSIRT exercises.

**Adopt:** a notional example is a candidate **MitigationInstance template** that carries a
`kind`. The SSDF says outright that examples are not requirements ("No examples or combination
of examples are required", §2), so a template never becomes a conformance obligation on its own.

## R-043 — governed views (adopt)

- PW.2.1/E6 records "the findings of design reviews to serve as artifacts (e.g., in the software
  specification, in the issue tracking system, in the threat model)". PW.2.1/E2 reviews "the risk
  models created during software design". The threat model is therefore an **approvable
  artifact** with review findings. That matches DL-0009's "documents are governed views; the KG
  is the SoT".
- PO.3.3/E1 asks for an audit trail of secure-development actions, and PO.4.2/E4 for "prevent
  any alteration or deletion of the information". Both support the change-tracking and
  immutability half of R-043. The SSDF defines **Artifact** = "a piece of evidence" (footnote 6),
  which matches DL-0009 `Evidence`.

## DEC-009 — mitigation lifecycle (adapt)

The SSDF supplies the lifecycle transitions DEC-009 needs:

- risk → response (PW.1.2/E1);
- response ∈ {remediate, accept, transfer} (RV.2.2/E1), plus temporary mitigation (RV.2.2/E2);
- approved exception → periodic re-evaluation (PW.1.2/E3);
- **mitigation → added to the security requirements** (PW.1.2/E1).

The last transition is missing from our model. A mitigation that is decided becomes a
requirement that later gates verify. **Adapt:** add a `MitigationInstance —becomes→
Requirement(tier=product)` edge and a time-bounded `accepted-risk` state with `next_review`.

## Root-cause feedback (new; no R-id yet)

RV.3.1–RV.3.4 close the loop:

1. vulnerability → root cause;
2. root cause pattern → "a particular secure coding practice not being followed consistently";
3. the SDLC is updated.

tmodel can say *which weakness* (CWE) but not *which SDL task failed*. **Open question:** do we
add `RootCause —traced_to→ Requirement(tier=framework)`? If we do, the SDL object becomes
self-correcting. SP 800-53 Release 5.2.0 added SI-2(7) Root Cause Analysis, which it marks "Identified as a gap
from analysis of the NIST SSDF" (record `sp-800-53r5`; SSDF 1.2 IPD maps RV.3.3 to SI-02(07)),
which is evidence that the edge matters.

## Provenance — keep the two kinds separate (ARCH §4)

SSDF "provenance" is **supply-chain/custody** provenance: "the chronology of the origin,
development, ownership, location, and changes to a system or system component" (footnote 5,
anchored at PO.1.3/E4, quoting SP 800-53). It applies to release components, in an SBOM (PS.3.2), and to tools
(PO.3.2/E7). ARCH §4 deliberately keeps that class out of the epistemic `Assertion` spine and
defers it to the radar→tmodel contract (ADR-0001). **Keep it out**, but give the SDL view a
**reference** to the release provenance artifact. PS.3.2 makes it a release deliverable, so a
release Gate exit criterion must be able to say "provenance data exists and is integrity
protected" without the model ingesting it.

## Reject / not adopted

- **Not adopted:** using SSDF groups (PO/PS/PW/RV) as lifecycle phases. They are
  organizational and domain groupings, as MAP-0001 notes. Phase placement belongs on the task
  (`phase`), not on the group.
- **Not adopted:** treating notional examples as requirements, for the reason given under R-040.

## Open questions

1. Hub choice: should R-044 use SSDF **1.1** task ids or **1.2** (SP 800-218r1, still an IPD
   at 2026-10-02) as the hub? Recommendation: stay on 1.1 until 1.2 is final, and record the
   1.1→1.2 identifier changes (see `sp-800-218r1` diff note) as `retired_into`/`updates` edges.
2. Should the conformance engine evaluate *practices* at all? The SSDF defines no
   practice-level conformance. We treat a practice as satisfied when all its applicable tasks
   are satisfied, which is our rule and not the source's.
3. 4e(ix) maps to "All practices and tasks consistent with a risk-based approach". That is a
   non-enumerable mapping. Should it be stored as a wildcard edge or left out?
