---
schema: "library-doc/v1"
id: iso-iec-29147-2018-design-notes
record: iso-iec-29147-2018
type: design-notes
updated: "2026-10-02"
---

# ISO/IEC 29147:2018 — design notes for tmodel

Read with `iso-iec-30111-2019/distilled/design-notes.md`; the two standards are one design (each
says it "shall be used in conjunction with" the other). Basis: the free preview only — Clause 3
terms, Figure 1 and the Contents. Anything resting on a heading is flagged.

## Adopt

- **Role vocabulary as Party edges (R-036, ARCH-0001 §2b).** `reporter`, `vendor`, `coordinator`,
  `user` are relational roles defined by activity (§3.4–§3.6, Notes to entry). Adopt the 29147 terms
  as the edge vocabulary for `Finding/Vulnerability` (`reported_by`, `remediated_by`,
  `coordinated_by`) — the same Party can hold several (Note 1 to 3.5).
- **Verification as the acceptance gate (ARCH-0001 §4, R-042).** Figure 1's "Vulnerability
  verified?" is the Assertion→Review pattern: a report is an unreviewed `Assertion`; verification is
  the `Review` verdict; only a verified vulnerability propagates (`affects`, `uses_component`).
- **Advisory field list (R-043).** The 16 advisory elements (§7.4.2–§7.4.17, headings only) are a
  ready-made schema for a *governed, versioned, published view*: it has identifiers, revision history
  and terms of use. Render via OASIS CSAF 2.x when we need a wire format (see `messages.yaml`).

## Adapt

- **Remediation vs mitigation (R-040, DEC-009).** 29147 §3.7 makes mitigation (workaround /
  countermeasure) a sub-case of remediation. tmodel's `MitigationInstance` is the superclass; add a
  `removes | mitigates` effect flag and treat a remediation as `kind: technical`, an advisory's
  workaround text as `kind: documentation`.
- **Handling phases ≠ product lifecycle (ARCH-0001 §3b).** Preparation → Receipt → Verification →
  Remediation development → Release → Post-release (+ Embargo) is the lifecycle of *one
  vulnerability*, not of the product. Do not overload `LifecyclePhase`; model it as the state machine
  of a Finding/MitigationInstance pair (DEC-009) — `iso-iec-30111-2019/distilled/state-machine.yaml`.
- **SDL gate hook (R-041).** §5.2's "develop policy before starting to receive reports" is an
  ordering constraint usable as an entry criterion on the release/response gate: no product ships
  without a published disclosure policy (EU CRA Annex I Part II makes this mandatory; 29147 itself is
  opt-in per its Scope).

## Reject / not applicable

- Nothing visible to reject. 29147 defines no wire format, so D-3 (encoding) is not engaged.

## Crosswalk (R-044)

MAP-0001 rows 17–18 (vulnerability management; disclosure & response) cite ISO/IEC 29147/30111
only indirectly. Candidate cells: SSDF RV.1.3 (policy for disclosure), IEC 62443-4-1 DM-1..DM-5,
ISO/SAE 21434 §8.3–8.6, EU CRA Annex I Part II (2)-(8), OWASP SAMM Operations › IM. These are
**our** proposals; 29147's own cross-references visible in the preview are only 30111, 27000, 27002
(12.6.1), and — by heading — 27034, 27036-3, 27017, 27035.

## Open questions

1. Is the 29147:2018 acknowledgement (§6.2.5) time-boxed? Not visible; the CRA's 24 h/72 h clocks are
   for *reporting to authorities*, not for acknowledging reporters — keep the two clocks distinct.
2. Both standards are being revised (AWI 29147 "Cybersecurity — Vulnerability disclosure processes";
   AWI 30111 "Cybersecurity — Vulnerability handling and disclosure processes", both registered
   2025-10-08 at stage 20.00). The 30111 title suggests the pair may merge; re-check before modelling
   against clause numbers.
3. Purchasing the two standards (or a CEN EN ISO/IEC 29147/30111:2020 national adoption) would let
   us finish FX-1; until then `requirements.yaml` is a 3-item stub of a standard whose Annex D lists
   many more provisions.
