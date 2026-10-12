---
schema: "library-distilled/v1"
id: cisa-secure-by-demand-guide-2024-design-notes
record: cisa-secure-by-demand-guide-2024
type: design-notes
updated: "2026-10-02"
reviewed_by: ""
---

# Secure by Demand Guide — design notes for tmodel

## Adopt

- **Questions as consumer-side requirements (R-042, R-044).** Each question is a check an acquirer
  runs against a supplier; most map one-to-one to a Pledge goal (recorded as `related_inferred`,
  lane judgement). A tmodel conformance view can be rendered *for the customer*: the same KG
  Requirement nodes, answered by supplier Assertions and checked with Evidence.
- **Two evidence provenances.** "Artifacts you can collect from a software manufacturer" vs
  "Artifacts you can collect yourself" is exactly the PROV distinction tmodel's §4 Assertion
  spine supports (who generated the evidence). Make it explicit on `Evidence`.
- **Concrete, checkable thresholds:** SSO and MFA at no additional cost / by default; logs ≥ 6
  months for cloud/SaaS; SBOM machine-readable and complete; CWE+CPE in every CVE. Good
  automatable conformance checks (R-042).

## Adapt

- **Procurement stages** (before / during / following) are an acquirer lifecycle; DL-0009's gates
  are producer-side. Model acquisition as a separate program with its own gates rather than
  stretching `LifecyclePhase`.

## Reject

- Nothing; the guide is short and consistent with the pledge.

## Bears on

R-040 (technical vs documentation vs process items), R-042, R-043 (a customer-facing governed
view), R-044, DEC-009 (post-procurement continual assessment).

## Open questions

1. Ingest the companion references it names: ICT SCRM Task Force *Software Acquisition Guide for
   Government Enterprise Consumers* and *Minimum Viable Secure Product* (MVSP).
