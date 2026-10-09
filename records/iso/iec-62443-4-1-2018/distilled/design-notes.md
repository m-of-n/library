---
schema: "library-distilled/v1"
id: iec-62443-4-1-2018-design-notes
record: iec-62443-4-1-2018
type: design-notes
updated: "2026-10-02"
---

# IEC 62443-4-1:2018 — design notes for tmodel

Basis: requirement text reproduced in ISASecure SDLA-312 v6.3 + IEC preview (ToC, Scope, Fig 2) + terms
3.1.1–3.1.17. The IEC rationale/guidance, Clause 4 and Annexes were not read; conclusions resting on them
are marked.

## Adopt

- **R-042 conformance check = SR-2 k) + SVV-2.** "All products shall have a threat model … with … k)
  mitigations and/or dispositions for each threat" and SVV-2 "testing the effectiveness of the mitigation
  for the threats identified and validated in the threat model" together are the automatable check
  DL-0009 describes: every in-scope ThreatInstance has a MitigationInstance (or disposition) *and* the
  mitigation has test evidence. Adopt as the reference definition of the check.
- **SR-2 a)–m) as the minimum threat-model schema.** The characteristic list maps one-to-one onto ARCH-0001
  §1 layers 2–3 (DataFlow with classification, TrustBoundary, Process, DataStore, ExternalEntity, protocol,
  attack vector, threat + CVSS severity, mitigation). Gaps: physical/debug ports and JTAG headers (g, h) and
  "external dependencies … linked into the application" (m) → Component with `uses_component`. Adopt as a
  conformance profile: "tmodel instance satisfies 62443-4-1 SR-2".
- **R-041 Gate exit criteria = SM-11 + SM-12.** Release is gated on (a) all security-related issues from
  requirements, design, implementation, V&V and DM "addressed and tracked to closure" and (b) "records
  documenting the completion of each process". Both are queryable predicates over the KG.
- **R-040 documentation kind ⇐ Practice 8 (SG-1..SG-7).** 62443-4-1 treats user documentation
  (defense-in-depth strategy, expected environment measures, hardening, disposal, secure operation,
  accounts) as required security outputs, i.e. mitigations of kind `documentation`. SG-2 is the
  standard's explicit *risk-transfer* mechanism to the integrator/asset owner.
- **Review discipline (SR-5).** Required reviewer disciplines (architects/developers, testers, customer
  advocate, Security Advisor) with tester independence — a template for `Review` participants.

## Adapt

- **DEC-009 mitigation lifecycle → issue lifecycle.** DM-1..DM-5 give a disposition set {fix, remediation
  plan, defer with reason+risk, accept below residual-risk threshold}, plus side effects (inform other
  products' processes, inform third parties). Adapt MitigationInstance/Finding status to this enum; the
  `ResidualRiskThreshold` must be a stated, supplier-level value (DM-4) — bears on DEC-003.
- **Conformance is graded (ML1–ML4).** Clause 4.2/Table 1 not read; secondary sources say ML is assessed
  per practice and ISASecure CSA/SSA product certification expects ML3+ (claim not verified in a free
  primary source). Adapt R-042: a conformance result needs `level` and per-practice granularity.
- **Two Requirement types (R-044).** Keep `SDLRequirement` (process: SM-1…) distinct from
  `ProductSecurityRequirement` (SR-3/SR-4 with SL-C, traced to 62443-4-2/3-3). MAP-0001 conflates them.
- **Severity via CVSS** (SR-2 j, DM-3 b, DM-5 a) — keep tmodel's DEC-003 metric but carry a CVSS vector as
  an interoperable projection.

## Reject / out of scope

- Integrator/asset-owner process (62443-2-4, 2-1) — explicitly outside 4-1 Scope; tmodel models the
  product side only for SDL conformance.
- ISASecure SDLA certification mechanics (12/36-month validity) — recorded in `state-machine.yaml` as
  external attestation context, not modelled as tmodel behaviour.

## MAP-0001 verification item 1 — confirmed titles (IEC preview ToC)

| id | exact IEC title | IEC clause |
|---|---|---|
| SR-2 | Threat model | 6.3 |
| SVV-4 | Penetration testing | 9.5 |
| SG-3 | Security hardening guidelines | 12.4 |
| DM-5 | Disclosing security-related issues | 10.6 |

Corrections to MAP-0001 cells suggested by the text: row 6 (crypto) — SM-8 is *code-signing key
protection*, not crypto standards; SD-4 has no crypto item → mark 62443-4-1 *none dedicated*. Row 13
(build/provenance) — SM-6 "integrity verification mechanism for all scripts, executables and other
important files" + SM-7 + SM-8 + SUM-4 authenticity is stronger than *approx*. Row 15 (release gate) —
SM-11 and SM-12 are explicit release gates, so 62443-4-1 is not *approx*. Row 18 — disclosure is DM-5;
SUM-1..5 are update management, not disclosure. Row 1 training — SM-4 is exact, not *approx*.

## Open questions

1. SR-2 sentence structure: SDLA-312 splits it into rows, puts l) before k), and gives m) its own lead-in
   ("All products shall have an up-to-date threat model"). Is that the IEC text or ISCI restructuring?
   Needs the purchased standard.
2. ML3 label: exida says "Defined", TÜV/ISASecure says "Process practiced". IEC Table 1 needed.
3. SUM-1 second sentence ("The Process should include a verification that update is not contradicting
   other operational, safety or legal constraints") — capital "Process" and lower-case "should" suggest an
   ISCI/ANSI addition; unverifiable without the IEC text.
4. Edition 2 (TC 65/WG 10) and EN IEC 62443-4-1:2018/A11 (CRA harmonisation, CEN-CLC/JTC 13 WG 9) will add
   "intended use"/"security context" documentation and expected development artefacts — re-extract then.

## Licensing (read before publishing this record)

The requirement texts are © IEC/ISA, read from SDLA-312 (© ASCI), whose Terms of Use §C allow
non-commercial use with notices intact but otherwise forbid republication. ISASecure now lists SDLA-312
as "Available for purchase at ISA Store" although v6.3 remains publicly hosted on ISA's own CDN.
If this library is published under a public remote, the coordinator should decide whether to keep the
verbatim `text` fields or reduce them to titles (the ids/titles/clauses come from the free IEC preview
and are unproblematic).
