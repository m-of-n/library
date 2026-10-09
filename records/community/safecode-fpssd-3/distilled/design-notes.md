---
schema: "library-design-notes/v1"
id: safecode-fpssd-3-design-notes
record: safecode-fpssd-3
kind: design-notes
type: design-notes
title: "safecode-fpssd-3 — bearing on the tmodel design"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

Ids cited: ARCH-0001-PROPOSAL §1, §4, §5; DL-0009 R-040…R-044; MAP-0001.
**[analysis]** marks our reasoning. SDL is post-MVP.

## Adopt

1. **Controls as structured data (R-043).** "A best practice is to manage the
   controls as structured data in an Application Development Lifecycle
   Management (ADLM) system rather than in an unstructured document." Adopt as
   industry support for "the KG is the SoT; documents are governed views".
2. **Finding dispositions (R-042, DEC-009).** "The findings from these artifacts
   must be tracked and action taken to remediate, mitigate or accept the
   respective risk", with remediated = risk "completely eliminated" and
   mitigated = "reduced but not completely eliminated", and a residual-risk
   assessment when not remediated. Adopt the three dispositions on
   ThreatInstance/Finding (matching ISO/SAE 21434 treatment options and RPT-0013
   §4's mitigate/accept/transfer/avoid).
3. **Risk acceptance record (TSRV) and severity-tiered approver.** Technique,
   Specifics, Remaining risk, Verification; severity; remediation plan or
   expiration/re-review period; approver level by residual risk ("Critical Risk
   to VP of Business Unit, Medium Risk to Engineering Manager"); "Acceptance of
   risk must be tracked and archived." Adopt as the field set of an accepted-risk
   `Review` (schema `RiskAcceptance`).
4. **CWE references per practice.** SAFECode attaches CWE ids to five practice
   sections; keep them as `maps_to` CWE on the Requirement — a bridge from SDL
   practices to the Weakness catalogue (ARCH §1.3).

## Adapt

5. **ASC workflow → Requirement lifecycle.** Identify drivers → identify
   requirements → communicate → validate implementation → audit. Adapt as states
   of a product-instantiated Requirement (schema `ApplicationSecurityControl`,
   status INFERRED).
6. **Mitigation kind (R-040).** SAFECode itself names a documentation
   mitigation: "it may be necessary to produce documentation, such as a Security
   Configuration Guide" to ensure mitigating controls outside the application.
   Strong support for R-040 `documentation`.
7. **Third-party inheritance.** "development organizations inherit the security
   vulnerabilities of the components they incorporate" = R-027a propagation along
   `uses_component`.

## Reject

8. **SAFECode as a gate model.** No gates, phases or sign-offs are defined; it is
   a practice catalogue (MAP-0001 correctly calls SAFECode non-phased). Do not
   derive R-041 Gate structure from it.

## MAP-0001 corrections

- Row 6 (crypto): SAFECode's "Develop an Encryption Strategy" is a full section
  (in transit/at rest, standards, vetted libraries, key/certificate lifecycle,
  crypto agility) — confirmed first-class.
- Row 15 (release gate): SAFECode has risk acceptance "approved before the
  product is released", not a release gate — "Risk Acceptance approx" is right.
- Row 17/18: "Manage Security Findings" and "Vulnerability Response and
  Disclosure" (which defers to ISO/IEC 29147 and 30111) are confirmed.

## Open questions

1. SAFECode's two example severity scales (4-level and 6-level) and CVSS bands
   are illustrative; which scale does tmodel's policy object default to?
2. Should tmodel import SAFECode at section granularity (52 practices) or at
   statement granularity (143)?
