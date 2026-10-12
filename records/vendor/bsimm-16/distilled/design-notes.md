---
schema: "library-design-notes/v1"
id: bsimm-16-design-notes
record: bsimm-16
kind: design-notes
type: design-notes
title: "bsimm-16 — bearing on the tmodel design"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

Ids cited: `ARCH-0001-PROPOSAL-v0.2.0` (§2b Party, §3b LifecyclePhase, §4
Assertion/Review, §5 MitigationInstance), `DL-0009` (R-040…R-044), `MAP-0001`,
`RPT-0013`. **[analysis]** marks our reasoning. SDL is post-MVP.

## Adopt

1. **BSIMM's checkpoint vocabulary for the R-041 `Gate`.** [SM1.4] defines
   checkpoints "(such as gates, release conditions, guardrails, milestones,
   etc.) at one or more points in a software lifecycle", gathered first and
   enforced later; [SM1.7] enforces "security release conditions at each
   checkpoint ... so that each project must either meet an established measure
   or follow a defined process for obtaining an exception to move forward";
   [SM2.6] requires "a risk owner use SSG-approved criteria to sign off on the
   state of all software prior to release", formalized and "captured for future
   reference". **Adopt** as Gate attributes: `exit_criteria` (release
   conditions, sourced from policy/standards/regulation/contract), `enforced`
   (bool — BSIMM distinguishes observe-only SM1.4 from enforced SM1.7),
   `exceptions[]` (tracked), and an approving `Review` by a risk-owner `Party`.
   MAP-0001 row 15 lists BSIMM "CP/SM approx"; the precise cells are SM1.4,
   SM1.7, SM2.6 (and SM3.4 governance-as-code).
2. **Edition-qualified ids + `supersedes` for R-044.** BSIMM relabels an
   activity whenever its level changes (p.60); NIST's SSDF still cites BSIMM12
   labels, which BSIMM16 Table 3 had to translate (22 rows, 16 tasks).
   **Adopt:** a `Requirement` id always carries its source edition
   (`bsimm-16#SM1.7`), and Table 9 lineage becomes `supersedes` edges
   (`examples/table9-activity-changes.yaml`, 86 parsed changes).
3. **Observation as an `Assertion` (ARCH §4).** An observation is an
   assessor's claim that a firm does an activity; it fits the reified
   Assertion + Review spine with provenance = assessment.

## Adapt

4. **Threat modeling cells (MAP-0001 row 3).** BSIMM has no single TM activity:
   it is spread over AA (AA1.1 security feature review, AA1.2 design review for
   high-risk apps, AA2.1 defined AA process, AA2.2 standardized architectural
   descriptions) and AM (AM1.2 data classification, AM1.3 identify potential
   attackers, AM1.5 attack intelligence, AM2.1 attack patterns/abuse cases,
   AM3.4 technology-specific attack patterns). The Part 8 AA intro names
   "Microsoft Threat Modeling [STRIDE] or Architecture Risk Analysis [ARA]".
   **[analysis]** Map MAP-0001 row 3 to AA1.2/AA2.1 (process) + AM1.3/AM2.1
   (inputs) rather than "AA+AM approx"; SAMM's own BSIMM14 mapping of D-TA-B is
   AA2.2, AA3.1, AM1.3, AM2.6 (`owasp-samm-2` crosswalk) — the two disagree in
   detail, which is itself a finding for R-044 (mappings are opinions with
   provenance).
5. **Levels → not a gate threshold.** BSIMM levels are observation-frequency
   bands, not maturity steps; a Gate criterion "BSIMM level 2" is meaningless.
   Adapt to "activity X observed" per activity.
6. **SSI states (emerging/maturing/enabling) → SDL program state (R-041).**
   Stated, with no guards; usable as a descriptive status on the SDL object,
   not as an automatable state.
7. **Mitigation kind (R-040).** BSIMM calls its activities controls that "might
   function as preventive, detective, corrective, or compensating controls"
   (p.45). Most are process; some are technical (SE2.4 protect code integrity,
   SE1.1 input monitoring, SE2.5 containers); some documentary (SR1.1
   standards, CP1.3 policy, SE3.6 BOMs). **[analysis]** supports R-040's three
   kinds, and suggests a fourth orthogonal axis (control function:
   preventive/detective/corrective/compensating) — open question 3.

## Reject

8. **BSIMM as product conformance evidence (R-042).** BSIMM scores an
   organization's SSI; it never touches a product's ThreatInstances. Reject
   using a BSIMM score or observation to discharge a product's threat mitigation.
9. **Percentages as data.** Use counts out of the pool (Figure 18), not printed
   percentages — see defects below.

## Source defects found (record, do not paper over)

- [SR2.2] heading prints 56.6% but Figure 18 gives 65/111 = 58.56%.
- [SE1.4] heading prints 62.1%; Figure 18 gives 69/111 = 62.16% (62.2% rounded;
  every other heading rounds).
- Table 1 (p.6) top-activity percentages use a denominator of 121, not 111
  (e.g. CMVM1.1 87.6% = 106/121; Figure 18: 95.50%) — the BSIMM15 pool size:
  p.50 says "we added 16 firms and removed 26, resulting in a data pool of 111
  firms", so the previous pool was 111 + 26 − 16 = 121 (confirmed in
  verification, 2026-10-03).
- Table 4 prints "PO5.2" (missing dot).
- Domain naming: "SSDL Touchpoints" (p.5, Table 7) vs "SDLC TOUCHPOINTS" (Part
  8 headings); [SE3.9] is "Protect integrity of development toolchains" in Part
  8 and on p.6 but "Protect integrity of SDLC toolchains" in Table 9.
- The Part 8 intro still refers to a "Top 10 Activity in BSIMM15" icon legend.

## Open questions

1. BSIMM16 Table 4's "Could Add" SSDF links are explicitly unofficial — carry
   them as `maps_to` with `relationship: proposed`? (We did, labelled.)
2. Should tmodel import the 128 activities as `Requirement`s at all, given they
   are descriptive? Proposal: yes, kind `observed-practice`, never used as
   mandatory gate criteria unless an SDL owner adopts them.
3. Add `control_function` (preventive/detective/corrective/compensating) to
   MitigationInstance alongside R-040 `kind`?
4. Licence: CC BY-SA 3.0 (p.33) permits reuse of the activity text with
   attribution and share-alike; confirm this is compatible with the library's
   intended licence before committing verbatim activity text at scale.
