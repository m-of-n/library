---
schema: "library-doc/v1"
id: iso-iec-30111-2019-design-notes
record: iso-iec-30111-2019
type: design-notes
updated: "2026-10-02"
---

# ISO/IEC 30111:2019 — design notes for tmodel

Basis: free preview, Clauses 1–6.5.3.4 (all of the organisational Clause 6 up to PSIRT
responsibilities). Clause 7 (the phases) is known from headings and Figure 1 only.

## Adopt

- **The handling state machine (DEC-009).** `state-machine.yaml` — Receipt → Verification →
  Remediation development → (Embargo) → Release → Post-release, with the verified/not-verified fork —
  is the lifecycle a tmodel `Finding` and its `MitigationInstance` should move through. It is
  vendor-internal and per-vulnerability; it is not the product `LifecyclePhase` axis (ARCH-0001 §3b).
- **Policy as a conformance object (R-042, R-043).** 6.3-R01 (shall) plus 6.3-R03 a)–d) make the
  internal vulnerability handling policy a governed document with a checkable content list:
  responsibilities, responsible roles, premature-disclosure safeguards, target remediation schedule.
  A conformance check can test presence + contents mechanically; "compatible with the external
  disclosure policy" (6.3-R02) needs a Review.
- **Coverage = all products (R-041).** 6.5.2-R01 "include all of their products and services" is
  the scoping rule for attaching an SDL/SecurityProgram to a ProductFamily: an SDL gate check can
  assert that every Product in scope has a dispatch contact (6.5.3.4-R01) and is in the process.

## Adapt

- **Organisation graph (ARCH-0001 §2b).** PSIRT within vendor, per-division and per-product contacts,
  support-desk routing (6.4, 6.5.3.3–6.5.3.4) need `part_of` / `contact_for` edges between Parties.
  Today Party carries only intrinsic classification + relational edges to products.
- **Remediation schedule (ARCH-0001 §5).** 6.3 d) target schedule → add planned/actual dates to
  `MitigationInstance`, mirroring the planned/actual dates DL-0009 gives Gates (R-041).
- **Root-cause feedback (R-041).** §6.1 (with 27034) sends handling results back into secure
  development. A gate *line* cannot hold a loop; model it as an edge from a Finding to the
  design/implementation Requirement(s) whose failure caused it.

## Reject

- Nothing visible. The leadership list 6.2.1 a)–h) is ISO management-system boilerplate (HLS style);
  record it as requirements but do not model "leadership" as an object.

## Crosswalk (R-044)

Own references (visible): ISO/IEC 29147:2018 (normative, dated), 27000, 27034-1:2011 6.5.2,
27036-3:2013 (5.4 a), 5.8 i), 6.1.1 a) 2), 6.3.4), 15408-3:2008 13.5, FIRST PSIRT Services
Framework. Proposed mappings (ours): 6.3-R01 ↔ SSDF RV.1.3 / IEC 62443-4-1 DM-1 / CRA Annex I
Part II (5); 6.5.3.2-R01 ↔ SSDF RV.1.1 / 62443-4-1 DM-? (monitoring) / CRA Annex I Part II (1)-(2);
6.5.3.3-R01 ↔ the CRA Art. 13 single point of contact for users (paragraph to confirm against eu-cra-2024-2847) / 29147 §9.2.2.

## Open questions

1. Clause 7 entry/exit criteria per phase (and whether any carries a deadline) — not visible.
2. Annex A summarises all normative provisions; with it, `requirements.yaml` could be completed and
   verified mechanically. Requires a purchased copy.
3. AWI 30111 (Edition 3, "Cybersecurity — Vulnerability handling and disclosure processes",
   registered 2025-10-08; WD 30111.2 at stage 20.60 per ISO open data 2026-09-30) may absorb 29147 — watch for a merged document line.
