---
schema: "library-distilled/v1"
id: enisa-sbd-playbook-2026-design-notes
record: enisa-sbd-playbook-2026
type: design-notes
updated: "2026-10-02"
---

# ENISA Secure by Design and Default Playbook: design notes for tmodel

## Adopt

- **R-041 Gate: adopt the playbook release gates as a library of gate criteria.**
  - There are 125 pass/fail criteria with ids `PB-x-RG-nn`.
  - The model needs three per-criterion outcomes: `pass`, `fail` and `not affected`. ENISA allows "Unchanged controls may be recorded as not affected".
  - A "documented exception with owner and expiry date" needs to be a first-class result.
  - The gate is Table 2's "Release risk review gate", with a go/no-go decision.
- **R-042 conformance and export: the SafeGate-X1 cascade is a worked conformance record.**
  - The cascade runs threat → control → secure-default setting → verification gate → evidence hash. See `examples/`.
  - `examples/safegate-x1-figure5.json` is a fixture, and it validates against the derived schema.
  - Use it as the target shape for exporting a conformance result as an attestation. ENISA names OSCAL, CycloneDX CDXA, SPDX 3 Security, SLSA/in-toto and the Transparency Exchange API (TEA) as existing carriers. Do not invent a new schema; ENISA explicitly declines to.
- **R-040 mitigation kinds: secure defaults are technical mitigations with a "ships enabled" flag.**
  - The playbook distinguishes design (how built) from default (how it arrives).
  - tmodel should carry `default: true|false` on technical MitigationInstances. A security feature that exists but is off by default is a different conformance state from one that is on.
- **R-044 crosswalk: carry Annex C as `maps_to` to `eu-cra-2024-2847` with strength `indicative`.** There are 62 rows of principle → CRA Annex I point. Annex B ids (ANNEX-1.PT1.2.x) are an alternative atomic key to BSI's ER/VH ids, and the two can be cross-mapped mechanically.

## Adapt

- **DEC-009 lifecycle: make expiry mandatory.** Use ENISA's vulnerability dispositions, fix now / mitigate / accept (time-bound) / defer (with rationale), as the mitigation-lifecycle decision set. The expiry on "accept" should be mandatory.
- **R-043 governed views: invalidate by event, not only by version.**
  - Threat-model refresh triggers (Table 3, §4.1) should be events that mark the governed threat-model view stale.
  - Change-triggered reassessment (Table 2) should do the same for the risk register.
- **Runtime posture: model it separately.**
  - §4.21 describes "secure baseline" and "degraded" states, and §4.19 onboarding blocks operation.
  - These are runtime properties of a ProductInstance. They are out of scope for the MVP but should be distinguished from design-time conformance.
- **Proportionality.**
  - The playbook targets SMEs and allows progressive adoption (§4.23) "without prejudice" to CRA obligations.
  - Like ETSI's DG tiers, this argues for an applicability or adoption profile on SecurityProgram rather than one fixed requirement set.

## Reject or hold

- **Annex C is not a compliance route.** It says the mapping is "indicative" and that the playbook "does not inherently ensure ... compliance with regulatory mandates". It must never be used as an equivalence.
- **Hold numeric SLAs.** The SLA examples (48 h triage, "≤ XX hours") are placeholders for each manufacturer and should not become defaults in tmodel.

## Open questions and source defects

1. **§5.4.2.2 refers to "the MRSM exposed_ports list".** MRSM is never defined, and the Figure 5 JSON field is `ports_allowed`.
2. **§5.4.2.3 contradicts the controls table.** It says to close all ports except 443, but the controls table and the JSON allow 443 and 22.
3. **Figure 5's `evidence_hash` is elided** ("sha256:7f8d...a11b"). The fixture is checkable structurally only.
4. **Figure 4 (trust-boundary diagram) is a raster image of a Mermaid diagram** and is too small to transcribe; its source is not published.
5. **Annex A defines "CI" as "configuration item"**, while the body uses CI to mean continuous integration.
6. **The acknowledgements list Sebastien Deleersnyder twice.**
7. **"secure by default" principles 4.15 to 4.22 overlap with design principles 4.4 and 4.8.** The overlap is acknowledged ("practical organising lenses"), but it leads to duplicate gate criteria across playbooks. One example is "no default credentials", which appears in 4.8 RG-02 and 4.16 RG-01. A tmodel crosswalk should deduplicate these.
