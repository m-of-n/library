---
schema: "library-design-notes/v1"
id: microsoft-sdl-5-2-design-notes
record: microsoft-sdl-5-2
kind: design-notes
type: design-notes
title: "microsoft-sdl-5-2 — bearing on the tmodel design"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

Ids cited: `ARCH-0001-PROPOSAL-v0.2.0` §2, §3b, §4, §5; `DL-0009` R-040…R-044;
`MAP-0001`. **[analysis]** marks our reasoning. SDL is post-MVP. SDL 5.2 is
legacy (Microsoft files it under "Legacy archive" and its FAQ says not to use it
as an implementation resource), but it is the most complete public statement of
an SDL with a gate, so it is the reference model for R-041.

## Adopt

1. **The FSR as the template for the R-041 `Gate`.** Entry guard: "The FSR
   cannot begin until you have completed the reviews of the security milestones
   that were required during development" and "The project team must provide all
   required information before the scheduled FSR start date". Reviewer: the
   assigned security advisor. Checks: threat models reviewed "to ensure that all
   known threats and vulnerabilities are identified and mitigated"; deferred or
   rejected security issues against the bug bar; results of all security tools.
   Outcomes: Passed / Passed (with exceptions) / FSR escalation, plus immediate
   failure for omission or specious claims. Debt: "All exceptions and security
   issues not addressed in the current release should be logged and then
   addressed and corrected in the next release." **Adopt** these as Gate
   attributes and the outcome enum (`state-machine.yaml`, `schema/`).
2. **The threats-mitigated check (R-042) has a Microsoft precedent.** The FSR
   item "Review threat models ... ensure that all known threats and
   vulnerabilities are identified and mitigated" plus Risk Analysis's "Create an
   individual work item for each vulnerability listed in the threat model so that
   your quality assurance team can verify that the mitigation is implemented and
   functions as designed" is exactly DL-0009's automatable check (every in-scope
   ThreatInstance has an approved, verified MitigationInstance). The in-scope set
   is defined by the security risk assessment (Cost Analysis).
3. **Seven-phase line.** Training → Requirements → Design → Implementation →
   Verification → Release → Response is MAP-0001's canonical phase line; keep it
   as the R-041 phase skeleton with local names mapped onto it.
4. **Security work item fields.** Security Bug Effect (STRIDE + "Attack Surface
   Reduction") and Security Bug Cause (15 values) — adopt as the minimum
   classification on Finding (ARCH §2 already makes STRIDE a facet; the cause list
   is a coarse CWE-like axis).

## Adapt

5. **Bug bar → severity policy with versioning.** The bug bar is per project,
   approved by the security advisor and "must never be relaxed". Adapt into a
   versioned `SeverityPolicy` referenced by the Gate's exit criterion ("no known
   vulnerabilities that would be considered as Critical, Important, Moderate, or
   Low" — note the FSR text excludes *all four* levels, which is stricter than
   the Phase One wording; record both).
6. **SDL-Agile cadence.** Every-sprint / bucket (≤ six months) / one-time (grace
   period one month to one year): adapt as a `cadence` attribute on Requirement
   so R-041 Milestones can be sprint-shaped rather than phase-shaped.
7. **Risk-tiered applicability (SDL-LOB).** High/Medium/Low application risk →
   required service level (threat model, design review, code review, pen test,
   privacy review, deployment review). Adapt: Requirement applicability can
   depend on a risk tier of the Product — the same idea as SRA scoping.
8. **Mitigation kind (R-040).** 5.2 requirements produce documents (security
   plan, privacy disclosure, response plan, threat models), process steps
   (training, push, FSR) and technical controls (compiler switches, banned APIs,
   /NXCOMPAT, heap fail-fast) — all three R-040 kinds, with Appendix E making the
   technical ones mechanically checkable.

## Reject

9. **Platform-specific requirements as generic Requirements.** Appendices E–J
   (Win32/Win64/CE compilers, VirtualAlloc flags, shared PE sections, SAL,
   Application Verifier) are Windows/2012-specific; keep them in the record, do
   not lift them into a generic SDL catalogue.
10. **The undefined "security score of B".** It cannot be modelled from this
    source; do not invent a scale (our schema's A–F is marked inferred).

## Open questions

1. Two release criteria disagree: FSR text — no known vulnerabilities rated
   "Critical, Important, Moderate, or Low"; elsewhere teams fix issues meeting
   their bug-bar severity criteria. Which is the gate? (Source inconsistency.)
2. Appendices P–R restate main-body requirements under short titles; a
   cross-check pass should link each Agile row to its main-body R-id.
3. Privacy review is a parallel gate with its own advisor — model as a second
   Gate on the same transition, or one Gate with two reviewers?
