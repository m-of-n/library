---
schema: "library-doc/v1"
id: openssf-osps-baseline-design-notes
record: openssf-osps-baseline
type: design-notes
updated: "2026-10-02"
reviewed_by: ""
---

# Design notes — OSPS Baseline v2026.08.28 against the tmodel object model

Targets: ARCH-0001 v0.2.0 (proposal, iteration 6), DL-0009 (R-040…R-044), MAP-0001, DEC-009.
OSPS is the **most directly automatable conformance catalog** in the SDL set: 64 MUST-only
assessment requirements, each scoped to a maturity level, with machine-readable crosswalks to 14
frameworks. It is a better template for the tmodel `Requirement` object than any prose SDL.

## Adopt

| # | What | Where it lands | Why |
|---|---|---|---|
| A1 | **Two-grain requirement**: `Control` (objective; crosswalk grain) ⊃ `AssessmentRequirement` (testable MUST; evaluation grain), ids `OSPS-XX-NN` / `OSPS-XX-NN.MM` | R-042, R-044 `Requirement` | Crosswalks are coarse (control level — all 378 OSPS mappings), conformance checks are fine (AR level). One flat `Requirement` cannot hold both without losing one. |
| A2 | **Requirement lifecycle** `Active / Draft / Deprecated / Retired` + `replaced-by` + "Identifiers for retired controls MUST NOT be reused" | R-044 | Exactly the library's own id rule; conformance claims made against a retired requirement must stay resolvable (OSPS-BR-01.02 is kept as a tombstone). |
| A3 | **Gemara relationship vocabulary** for crosswalk edges: `implements`, `implemented-by`, `supports`, `supported-by`, `equivalent`, `subsumes`, `no-match`, `relates-to`; per-target `strength` 1–10 and `confidence-level` | R-044 `maps_to` edge attributes; MAP-0001 cells | MAP-0001 currently marks cells only "approx". Gemara gives a typed, graded edge. Use it even though OSPS itself only populates `relates-to`. |
| A4 | **Import the 14 OSPS mapping documents as `maps_to` edges** (already extracted per AR in `requirements.yaml`) | MAP-0001, R-044 | Gives ready, source-published crosswalk rows for SSDF (35 mappings), CRA (35), 800-161 (39), PSSCRM (34), SAMM (19), SLSA (9), Scorecard (13), UK CoP (31), BSI TR-03185-2 (28), etc. Flag them `relationship: relates-to, confidence: unset` — the source says they are "not guaranteed to be 100% matches". |
| A5 | **Version-pinned conformance claim**: "Downstream consumers … should specify their compliance against a specific version." | R-042 conformance check | A conformance result must name the requirement-set version (here `v2026.08.28`). |
| A6 | **Assessment requirements as verification procedures** — many are a single platform-API query (MFA enforced, branch protection, default token permissions, required approvals, status checks) | R-042 automatable check; DL-0009 "automate validation" | 31 of 64 ARs are rated `testable: yes`; ~20 are pure configuration assertions on the VCS/CI. These are the first checks a tmodel conformance runner could execute without human review. |

## Adapt

| # | What | Adaptation |
|---|---|---|
| B1 | **Maturity levels** (L1/L2/L3) | Model as a **conformance profile** (an ordered, named subset of requirements a `Product` targets), *not* as DL-0009 `Gate`s. OSPS levels are defined by project profile ("at least 2 maintainers and a small number of consistent users"), not by lifecycle phase, so they do not sit on the `LifecyclePhase` axis (R-037). A gate's exit criterion may *reference* a profile ("L2 met before release"). |
| B2 | **Event-condition triggers** in AR text ("When the project has made a release", "When a new collaborator is added", "When a commit is made to the primary branch") | Add an `applies_when` condition to `Requirement`, evaluated against model facts. 13 ARs switch on only after the first release — which is precisely a gate condition (R-041). |
| B3 | **R-040 mitigation kind** | OSPS splits cleanly: 38 of 64 ARs are deliverable-natured (a document, policy, release artefact) and 26 are process/configuration (`requirements.yaml` `nature`, our typing). This maps to R-040 `kind ∈ {documentation, process, technical}` — but OSPS shows a fourth practical class, **platform configuration** (branch protection, MFA, CI token defaults), which is neither a product feature nor a document. Recommend `kind` gain `configuration`, or define `technical` to include development-environment configuration. |
| B4 | **Documents as governed views (R-043)** | 24 ARs have "the project documentation" as subject (CVD policy, security contacts, support scope, dependency policy, test policy, roles list…). Each is a candidate governed document-view over KG facts (e.g. the roles list = Party role edges; the dependency list = `uses_component`). OSPS requires them to *exist*; tmodel could *generate* them. |
| B5 | **OSPS-SA-03.02 threat model** | "the project MUST perform a threat modeling and attack surface analysis" (L3) is the one AR whose evidence is a tmodel output. A tmodel threat-model instance on a Product, with approved `MitigationInstance`s (R-042 "threats-mitigated" check), is direct evidence for SA-03.01/03.02 and SA-01.01/SA-02.01 (actors/actions and external interfaces = the DFD layer). |
| B6 | **DEC-009 mitigation lifecycle** | OSPS objectives are generic mitigations ("Reduce the risk of account compromise or insider threats …"); the AR is the product-level instance check. That is the generic→product mapping DEC-009 describes: `Control` ≈ generic `Mitigation`, AR result on a Product ≈ `MitigationInstance` status. Threats are never linked formally (Gemara `threats` field unused) — the Control→Threat edge must be asserted by us, as an `Assertion` with `Review`. |
| B7 | **VEX (OSPS-VM-04.02)** | Matches ARCH-0001 §5 VEX override (`Assertion` + `Review` on the propagated edge, R-027b). OSPS requires the VEX *document*; tmodel's override is the source for it. |

## Reject / do not carry

| # | What | Why |
|---|---|---|
| C1 | OSPS's flat lexicon file as a model artefact | It is not Gemara `#Lexicon`-shaped and has no ids; we lift the terms into object types (object-model.yaml) instead. |
| C2 | Treating `relates-to` mappings as equivalence | The source explicitly disclaims functional equivalence; carry them as weak edges only. |
| C3 | Source-control objects in the MVP | `Repository`, `PrimaryBranch`, `Change`, `StatusCheck`, `CICDPipeline` are needed to evaluate ~20 ARs but are post-MVP (DL-0009 guardrail: SDL is post-MVP; custody/build provenance is the ADR-0001 radar contract). Record as a gap, do not model now. |

## Open questions

1. **Non-cumulative applicability (source defect?).** OSPS-BR-07.01 (no unencrypted secrets in the
   VCS) and OSPS-VM-02.01 (security contacts) list `maturity-1` only, while every other L1 AR also
   lists L2 and L3. Read literally, an L3 assessment filtered by level does not require them. The
   checklist shows them only under "Level 1", which is consistent with levels being cumulative by
   convention — but the data says otherwise. Likely an omission; worth an upstream issue.
2. **Level semantics.** Is a level *achieved* (meet the ARs) or *assigned* (profile says you should
   meet them)? The source defines levels by profile and gives no assessment procedure.
3. **Lowercase "should" inside MUST requirements.** OSPS-BR-07.02 ("The policy should include
   guidelines …") and OSPS-QA-06.03 ("… should add or update tests …") embed non-binding content in
   a MUST statement; a conformance checker cannot tell which part is required.
4. **Stale rendered page at the tag.** `docs/versions/2026-08-28.md` as committed at tag
   `v2026.08.28` still carried the "While active," qualifier and the older OSPS-GV-03.01 text that
   the tag's YAML had already changed (#544); the live page was regenerated on main afterwards. A
   conformance claim citing "the published page" vs "the tagged YAML" could differ for that window.
   We extracted from the YAML and checked it against the live page (all 65 AR texts identical).
5. **Mapping grain mismatch.** Mappings are control-level; when a control's ARs differ by level
   (e.g. OSPS-BR-01.01 at L1 vs OSPS-BR-01.04 at L3), the inherited `maps_to` over-claims for the
   L1 AR. Our `requirements.yaml` copies control mappings to every AR and says so (`maps_to_note`).
6. **SLSA mapping targets prose, not ids, and SLSA 1.0** (`osps-to-slsa.yaml`), while the library
   tracks SLSA 1.2. The file has 9 mappings carrying 14 target entries over 6 distinct SLSA 1.0
   requirement names. Cross-check (2026-10-02): all 6 still resolve in SLSA 1.2
   `build-requirements.md` — "Choose an appropriate build platform" → `slsa-1-2#R-0003`..`R-0004`;
   "Follow a consistent build process" → `R-0005`..`R-0007`; "Distribute provenance" →
   `R-0008`..`R-0009`; "Provenance generation - Exists" → `#provenance-exists` `R-0010`..`R-0015`;
   "Provenance generation - Authentic" → `#provenance-authentic` `R-0016`..`R-0027`;
   "Isolation strength - Isolated" → `#isolated` `R-0035`..`R-0043`. Every `maps_to` entry in
   `requirements.yaml` now carries `target_edition` (the mapping-reference `version`), and the three
   edition mismatches with the linked library record (SLSA 1.0 vs `slsa-1-2`, Scorecard 5.0 vs
   v5.5.0, BSI TR-03185-2 v1.1.0 vs `bsi-tr-03185` v1.1.1) carry an `edition_note`.
7. **Gemara EvaluationLog** (Layer 5) is the natural result format for an OSPS assessment and for
   tmodel's R-042 conformance result; worth its own library record before the conformance object is
   designed.
