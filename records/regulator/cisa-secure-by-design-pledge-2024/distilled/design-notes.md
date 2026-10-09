---
schema: "library-distilled/v1"
id: cisa-secure-by-design-pledge-2024-design-notes
record: cisa-secure-by-design-pledge-2024
type: design-notes
updated: "2026-10-02"
reviewed_by: ""
---

# Secure by Design Pledge — design notes for tmodel

## Adopt

- **Time-boxed, outcome-evidenced goals (R-041, R-042).** Each goal is due "within one year of
  signing" and is satisfied by *public evidence of measurable progress*, not by a practice
  checklist. A tmodel SDL program can carry such goals as `Requirement`s with a due
  `Milestone` and evidence kinds (statistics, roadmap, policy, blog) — a second conformance mode
  beside practice attestation.
- **Goal 5 is a precise, testable requirement** (four VDP elements) and Goal 6 is testable over
  CVE records (CWE + CPE in every record). These are good candidates for automated checks over
  the KG's Vulnerability/Finding nodes (CWE link present, CPE present) — a cheap R-042 demo.
- **CWE root-cause trend as SDL metric (Goal 3).** tmodel already links Vulnerability ↔ Weakness
  (CWE); a "vulnerability classes reduced over time" view is a derived, governed view (R-043).
- **Mitigation kinds (R-040).** Example approaches split cleanly into technical (MFA by default,
  instance-unique passwords, parameterized queries, logs), documentation (VDP, CVE policy, EOL
  statement) and process (patch campaigns, standards participation).

## Adapt

- **Commitment vs attestation.** The pledge is a *forward-looking* claim; the attestation form is a
  *present-tense* claim. Model both as `Assertion` with a `modality` (commitment | attestation)
  and a time horizon, so conformance views don't treat a pledge as evidence of practice.
- **Metric interpretation rules** (G3-M1-note, G6-C1: rising CVE counts can mean success) need to
  be recorded with any outcome metric used as an exit criterion.

## Reject

- Treating pledge membership as conformance: "CISA does not enforce nor verify adherence" (WEB-3).

## Bears on

R-040, R-041, R-042, R-043, R-044 (goals relate to SbD tactics — lane judgement, recorded as
`related_inferred`, not `maps_to`), DEC-009 (patch/EOL obligations are post-release mitigation
lifecycle).

## Open questions

1. Should tmodel model customer-behaviour metrics (MFA adoption, patch levels) at all? They are
   about the installed base (ProductInstance population), which tmodel models only per instance.
2. Ingest CISA's Secure by Design Alerts and "Product Security Bad Practices" (v2, Jan 2025) —
   referenced by Goal 3 context and closely related.
