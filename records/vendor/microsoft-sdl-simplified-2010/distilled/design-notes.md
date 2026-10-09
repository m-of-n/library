---
schema: "library-design-notes/v1"
id: microsoft-sdl-simplified-2010-design-notes
record: microsoft-sdl-simplified-2010
kind: design-notes
type: design-notes
title: "microsoft-sdl-simplified-2010 — bearing on the tmodel design"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

**[analysis]** marks our reasoning. Ids: ARCH-0001-PROPOSAL, DL-0009 R-040…R-044.

## Adopt

1. **Per-phase quality gates with an approver (R-041).** Practice 3: "A project
   team must negotiate quality gates ... for each development phase, and then
   have them approved by the security advisor ... The project team must also
   illustrate compliance with the negotiated quality gates in order to complete
   the Final Security Review." This is the most direct Microsoft statement of
   *phase gates*, not just a release gate. Adopt: each `Gate` has negotiated exit
   criteria, an approving advisor (`Party` role), and its compliance is an input
   to the release gate.
2. **The auditor role (R-042).** The security advisor's Auditor sub-role "must
   monitor each phase ... and attest to successful completion of each security
   requirement ... without interference from the project team" — adopt
   independence of the approving `Review` from the proposing party (ARCH §4
   already keeps proposal and verdict separate).
3. **Compliance-tracking application = KG as SoT (R-043).** "A specially
   designated application should be used to track compliance with the SDL. This
   application serves as the central repository for all SDL process artifacts
   ... threat models, tool log uploads, and other process attestations", with
   role separation. **[analysis]** This is DL-0009's "documents are governed views;
   the KG is the SoT" in 2010 vocabulary — adopt as supporting precedent.
4. **Sixteen mandatory practices as a crosswalk anchor (R-044).** Numbered and
   phase-ordered. Microsoft's FAQ still points to this paper, but lists twelve
   practices (a later regrouping), not these sixteen; MAP-0001's
   "legacy 12-practice list" note should cite this paper (16 practices) and the
   FAQ's 12-item list as two different legacy sets.

## Adapt

5. **Optimization-model levels.** Basic/Standardized/Advanced/Dynamic per
   capability area; only "Advanced" is defined (= the sixteen practices). Keep as
   a descriptive `MaturityLevel` on an organization, not a gate.
6. **Root cause analysis → requirement revision.** "Upon discovery of a previously
   unknown vulnerability, an investigation should be performed to ascertain
   precisely where the security processes failed" — adapt as a feedback edge
   from a post-release Finding to the Requirement/Gate that should have caught it.

## Reject

7. **Optional activities as gate criteria.** Manual code review, penetration
   testing and vulnerability analysis of similar applications are at the
   advisor's discretion; do not encode as mandatory.

## Mitigation kind (R-040)

Documentation (design specs, incident response plan, release archive), process
(training, threat modeling, FSR) and technical (banned functions, approved
tools/flags) all appear — consistent with R-040.

## Open questions

1. The paper says "sixteen mandatory security activities"; the current FAQ lists
   twelve under the same paper's name. Which list does MAP-0001 mean by "legacy"?
2. The spreadsheet's numbering (Requirements 2.1.1 …) differs from the paper's
   SDL Practice 1–16; both are recorded — which should a crosswalk cite?
