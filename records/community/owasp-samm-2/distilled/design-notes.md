---
schema: "library-design-notes/v1"
id: owasp-samm-2-design-notes
record: owasp-samm-2
kind: design-notes
type: design-notes
title: "owasp-samm-2 — bearing on the tmodel design"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

Ids cited: `ARCH-0001-PROPOSAL-v0.2.0` (§1 layers, §2b Party, §3b LifecyclePhase,
§4 Assertion/Review, §5 MitigationInstance), `DL-0009` (R-040…R-044),
`MAP-0001`, `RPT-0013`. **[analysis]** marks reasoning of this extraction that
neither SAMM nor our documents state. Nothing here is a decision; SDL is post-MVP
(DL-0009, ADR-0002 scope guard).

## Adopt

1. **SAMM's GUID-linked, typed file model as a precedent for R-044 Requirement
   ingestion.** SAMM is data, not prose: 302 files, 8 types, referential links by
   id (`schema/samm-core-model.derived.schema.json` validates all 302). A
   `Requirement` importer for tmodel can load SAMM losslessly: Stream and
   Activity become `Requirement` nodes (kind `practice`), QualityCriterion becomes
   a child criterion, and the hierarchy edges are already explicit
   (`object-model.yaml`). **Adopt** the import as the reference case for R-044.
2. **Typed `maps_to` (R-044).** OWASP publishes SAMM↔SSDF, BSIMM14, IEC 62443-4-1,
   NIST CSF 2.0, Microsoft SDL and Threat-Modeling-Capability mappings
   (`crosswalk.yaml`, 428 stream/activity pairs + 77 OLIR stream rows + 81 OLIR
   activity rows), and the SSDF and Microsoft SDL tabs carry a **relationship
   type** from the NIST OLIR vocabulary (whole-part, general-specific /
   generic-specific, equivalence, supports, precedes…). MAP-0001 cells are
   untyped. **Adopt** a `relationship` property on `maps_to` using the OLIR
   vocabulary; it is the only published typing among our SDL sources.
3. **SAMM's official crosswalk replaces several MAP-0001 `approx` cells.** E.g.
   row 3 (threat modeling): SAMM D-TA-B → SSDF PW.1.1/PW.1.2, BSIMM AA2.2/AA3.1/
   AM1.3/AM2.6, IEC 62443-4-1 SR-2/SD-2, MS SDL 3.1/3.3/3.5. MAP-0001 lists SAMM
   only as "Design › TA" and BSIMM as "AA+AM approx". **[analysis]** MAP-0001
   should cite `owasp-samm-2#D-TA-B` and these targets, keeping in mind the
   publisher's caveat that the mappings are "our interpretation".

## Adapt

4. **Maturity is a score, not a state (R-041/R-042).** The release toolbox
   computes `practice = Σ_level mean(stream A, stream B)` (cell formulas cited
   in `state-machine.yaml`), so level-2 credit counts with level 1 at zero
   (`examples/non-cumulative.yaml`). A tmodel `Gate` exit criterion of the form
   "SAMM practice ≥ 2" must therefore be phrased as a **score threshold**, and
   must not be modelled as a LifecyclePhase-like state with guards (ARCH §3b
   critic M3 warned against over-claiming state machines; SAMM confirms it).
5. **QualityCriterion → conformance check, but evidence is ours (R-042).**
   SAMM's 295 quality criteria are the most testable statements in the model
   ("The organization has an inventory for the applications in scope"), yet
   SAMM assesses them by interview with free-text notes, and its `results`/
   `metrics` fields are placeholders. **Adapt:** a criterion becomes a
   `ConformanceCheck` whose satisfaction requires an `Evidence` node + approving
   `Review` (ARCH §4/§5) — tmodel adds the evidence edge SAMM lacks.
6. **Roadmap phases → Milestones (R-041).** SAMM's Roadmap (target score per
   practice per phase; G-SM-2-A "covers 1 to 3 years and includes milestones")
   is the nearest SAMM object to dated gates. **Adapt** into a `Milestone` with
   target scores as exit criteria, adding owner, approval and planned/actual
   dates, which SAMM does not have.
7. **Personnel → Party roles (R-036).** The 18 Implementation activities name
   roles (Developer, Security Engineer, Administrator, Architect, Security
   Officer, Security Champion, Product Owner, Manager). These are relational
   (who performs), so they are `Party` role **edges** per ARCH §2b critic M2.
8. **Phase mapping (§3b, R-037).** SAMM functions are not phases (Governance
   spans everything). Our requirements.yaml assigns a best-fit canonical phase per
   practice; it is labelled OUR mapping. Threat Assessment (D-TA) sits in
   *design*, matching MAP-0001 row 3.

## Reject

9. **Answer-set weights.** Every option carries `weight: 1` and the toolbox never
   reads it; do not model a weight.
10. **SAMM as a product-level conformance target.** SAMM assesses an
    organization, team or application portfolio ("for most or all of the
    applications"); it never touches threats or mitigations. The R-042
    "every in-scope ThreatInstance has an approved MitigationInstance" check is
    outside SAMM; SAMM only tells us whether D-TA-B (threat modeling) is
    *practised*. Reject using a SAMM score as evidence that a specific product's
    threats are mitigated.

## Mitigation kind (R-040) and DEC-009

SAMM activities are almost all **process** mitigations in R-040's sense
(policies, training, reviews, testing programmes); a few yield documents
(D-SA-3-A reference architectures, G-PC-1-A policies and standards) —
**documentation**; none is a technical feature. **[analysis]** This supports
R-040's three-valued `kind`: an SDL practice instantiated for a product is a
process- or documentation-kind `MitigationInstance` whose lifecycle (DEC-009)
is planned → implemented → verified by a Review, like any other mitigation.

## Open questions

1. Source defect: the TMC tab maps three capabilities to ids that are not SAMM
   ids: `P-SM-1-B` and `P-SM-2-B` (remarks say "Measure and Improve", i.e. G-SM-B
   levels 1 and 2) and `D-TM-3-B` ("Program Management / Simple Changes"; remark
   says "Level 3 Threat Modeling Stream", i.e. presumably D-TA-3-B). Kept verbatim
   in `crosswalk.yaml`; not attached to any entry, which is why 33 of the 36 TMC
   rows appear as `maps_to` in requirements.yaml.
2. Source inconsistency: the template comment on `relatedActivities` differs by
   file — "References to other activities that are prerequisites to implement
   this one." in 54 activity files, "...that are related to this one" in 18 and
   "...that may be related to this one" in 18. Of the 18 activities that populate
   the field, 13 carry the "prerequisites" comment (e.g. D-TA-2-A, V-AA-2-A,
   I-SB-3-A), 3 "are related" (O-EM-1-A, O-EM-3-A, O-EM-3-B) and 2 "may be
   related" (G-EG-3-A, G-SM-3-B). The comment looks like template drift rather
   than intent, so we cannot tell which edges are prerequisites. Ask the SAMM
   project?
3. Licence inconsistency: `license.txt` is CC BY-SA 4.0 and the spreadsheet says
   "Creative Commons Attribution-ShareAlike 4.0 License" in its header but "Share
   Alike 3.0" in the following sentence. We record 4.0 (the repository licence).
4. Should tmodel import SAMM at stream granularity (where OWASP maps) or at
   activity granularity (where assessment happens)? Proposal: both, with
   `part_of` from activity to stream, and `maps_to` attached where published.
5. Cross-check (2026-10-03): four BSIMM14 labels in the BSIMM tab no longer
   exist in BSIMM16 — SM2.2, SE2.2, CMVM2.1 and CMVM3.7 were relabelled in
   BSIMM15 to SM1.7, SE1.4, CMVM1.4 and CMVM2.4 (BSIMM16 Table 9; held in
   `bsimm-16` `former_ids`). A consumer resolving SAMM→BSIMM must go through
   that lineage; the targets are kept verbatim as BSIMM14 ids. Likewise the
   Microsoft SDL tab's `10.1` is not a Microsoft id (practice 10 has no
   sub-practices; it resolves to `microsoft-sdl#10`).
6. The SSDF mapping is to SSDF **1.1** task ids; if SSDF 1.2 (SP 800-218r1)
   finalises with renumbered tasks, these links need a version qualifier.
