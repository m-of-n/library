---
schema: "library-distilled/v1"
id: etsi-ts-104-219-design-notes
record: etsi-ts-104-219
type: design-notes
updated: "2026-10-02"
---

# ETSI TS 104 219 (SSDIF): design notes for tmodel

This note covers how SSDIF V1.1.1 bears on ARCH-0001 v0.2.0 and DL-0009 (R-040 to R-044, DEC-009). The SDL work is post-MVP under ADR-0002. R-040 is the one MVP-adjacent item.

## Adopt

- **R-044 crosswalk: take the SSDIF Annex B.2 table as a ready-made SSDF-pivot crosswalk.**
  - It maps each of the 42 SSDF tasks to provisions in 29 frameworks: BSIMM, IEC 62443-4-1, OWASP SAMM and ASVS, the Microsoft SDL practice numbers, PCI Secure SLC 1.x, ISO/IEC 27034-1, 29147 and 30111, SP 800-53, -160, -161, -181 and -216, CNCF, EO 14028, and others. That is 519 published task-to-provision rows, carried verbatim in `requirements.yaml` and inverted in `crosswalk.yaml`.
  - It is a second published source for the MAP-0001 IEC 62443-4-1 column. For example, PW.1.1 maps to SM-4, SR-1, SR-2 and SD-1, and RV.1.3 maps to DM-1 to DM-5. Because MAP-0001 marks the IEC ids as unverified, these rows can be used to confirm or correct it.
  - Annex A (CRA Annex I to SSDIF) and Annex B.1 (UK NCSC CRT APC claims to SSDIF) link the SSDF to the two newest regulatory baselines. tmodel holds both as records: `eu-cra-2024-2847` and `uk-software-security-code-of-practice` (the CRT APC implements its principles).
- **R-042 evidence model: adopt "artifact = by-product, version-bound".**
  - §3.1 defines an artifact as evidence "not for the sole purpose of proving compliance".
  - §5.0.4 says artifacts are "locked or attached to a specific version of code", and an evaluator can re-run the tool to reproduce them.
  - This is the strongest statement in the SDL set for R-043's "KG is the SoT, documents are views". Evidence should be a KG node linked to a ProductInstance version and to the tool run that produced it (PROV `wasGeneratedBy`). It should not be an attachment to a report.
- **R-041 Gate: adopt the bug bar as a typed exit criterion.**
  - PO.4.1 #4 to #6 make the release gate a severity threshold over open security bugs.
  - DG3 adds a "shall fix" static-analysis list that must be clean before release (PW.8.2 #4).
  - Both are mechanically checkable, which is exactly the R-042 "automatable conformance check".
- **R-040 mitigation kind:**
  - SSDIF threats become bugs that are fixed by code changes, which are technical mitigations (PW.1.1 #5).
  - Secure-default documentation for administrators is a documentation mitigation (PW.9.2).
  - Training, review and root-cause processes are process mitigations (PO.2.2, RV.3.x).
  - This confirms the three-valued enum.

## Adapt

- **Development Group gives an applicability filter that R-041 and R-042 currently lack.**
  - Each SSDIF action is scoped DG 1/2/3, DG 2/3 or DG 3, and an organisation picks its DG by what it builds (Table 5.0-2).
  - Proposal: give `SecurityProgram` an `applicability_profile` (here DG1, DG2 or DG3).
  - Requirement applicability is then evaluated before conformance, so a DG1 program does not "fail" a DG3-only action.
  - This should be generalised, because the CRA product classes, the SAMM levels and the BSIMM activity levels are different axes of the same idea.
- **DEC-009 mitigation lifecycle.** The threat-to-bug-to-fixed path (PW.1.1) and the vulnerability path (RV.1.1 to RV.3.4, state machine SM1) are compatible with DEC-009 if:
  - "approved exception" (PO.1.2 example 7, PW.1.2 example 3) maps to the accepted-risk state;
  - its periodic re-evaluation becomes a review timer.

  Those two are informative examples only. SSDIF's DG actions never require an exception register.
- **Root cause becomes a program change.** RV.3.4 and §5.0.4 make the SDL itself a product with work items.
  - Proposal: add an edge `Finding --drives_change--> SecurityProgram`, versioned through §4 provenance.
  - This is how a governed SDL view (R-043) gets its change history from the KG rather than from document edits.
- **Responsible Roles become a RACI.** The 14 roles across 42 tasks give a responsibility matrix. Model it as a Party-role edge `responsible_for` to Requirement, not as a free-text owner.

## Reject or hold

- **No maturity scoring.** SSDIF deliberately defines no levels or scores. "Secure-by-design means ... sufficiently addressed the six SSDIF Essentials" (§5.0.4). tmodel should not invent a numeric SSDIF score.
- **The CRA and CRT mappings are informative.** The TS says they "do not imply authoritative compliance". tmodel must carry their strength as `informative`; they must never become an equivalence used in a conformance verdict.

## Open questions and source defects

1. **"42 actions" is ambiguous.**
   - The executive summary says "6 Essential Practices that group 42 SSDIF specific actions".
   - The tables have 42 tasks, which is also the 42 SSDF 1.1 tasks, but 183 numbered DG actions.
   - We treat "action" at task level as `SSDIF <task>` (§5.0.1) and the numbered items as atomic requirements.
2. **Wrong reference numbers in §5.6.0.** The text cites [i.100] for CVE/NVD and [i.101] for GCVE/EUVD. In §2.2, [i.100] is SP 800-128 and [i.101] is a Microsoft fuzzing blog; CVE and GCVE are [i.98] and [i.99].
3. **Two tier systems in one table.** PO.5.1 lists the same CIS safeguards under "DG 1/2/3 ... for CSC IG2" and "DG 2/3 ... for CSC IG3". §5.5.0 speaks of IG2/IG3 organisations instead of DGs. The DG-to-IG relation is never stated.
4. **Typos and inconsistencies.**
   - PW.4.2 DG1/2/3 #8 reads "should should support ... applications\"" (doubled verb, stray quote).
   - The executive summary calls CRT APC "(APT)".
   - The §3.1 definition reads "echanisms" for "mechanisms".
   - Annex C and clause 5 differ for PW.1.3, PW.4.2, PW.5.1, RV.2.2 and PO.5.1 (listed in normative.md).
5. **Truncations and gaps in the Annexes.**
   - Annex A row I.II(8) is truncated ("including on potential").
   - Annex B.1 claim 5.1.5 (accessibility testing) has no mapping.
   - Annex A maps CRA I.I(1) and I.I(2)(a) to "All" without action ids.
   - CRA I.I(2)(m), secure data removal, is "Not covered in SSDIF". This is a real coverage gap against the CRA, which BSI TR-03183-1 and the ENISA playbook (4.22) do cover.
6. **Lineage.** SSDIF is the ETSI publication of the CIS/SAFECode "Secure by Design" guide. The SAFECode/CIS v1.1 announcement says the guide "underlies a new ETSI standard" and v1.1 is "consistent in content with the new ETSI standard". `cis-safecode-sbd-assessment-1-1` should be treated as the same content line. Its spreadsheet would be the machine-readable source, but it is registration-walled.
7. **Annex B.2 mislabels PS.3.2 as PW.1.1 (found by the verify pass, 2026-10-02).**
   - In ten framework rows (BSAFSS, BSIMM, CNCF, EO 14028, NTIA SBOM, OWASP SCVS, SAFECode SCSIC and SCTPC, SP 800-53, SP 800-161) B.2 prints "PW.1.1" twice. The first of the two sits between PS.3.1 and the real PW.1.1, and its provisions are exactly the SP 800-218 v1.1 References for **PS.3.2** (provenance / SBOM). Example: NTIA SBOM "All" appears against PW.1.1 (threat modelling).
   - `requirements.yaml` keeps these rows under PW.1.1 as printed and flags each with `ssdf_1_1_task: "PS.3.2"` and `source_defect`; `crosswalk.yaml` carries a note on each affected entry. **The consolidated SDL crosswalk must key these ten rows to PS.3.2.**
   - Other B.2 differences from SP 800-218 v1.1: OWASP MASVS for PO.1.1 is printed "1.1" (SSDF: "1.10"); B.2 omits the SSDF BSIMM rows for PO.1.1, PO.1.2 and PO.1.3 and the SP 800-181 rows for PO.1.1 to PO.2.3. These are source omissions, not extraction drops: the extracted 519 rows match an independent re-parse of B.2 exactly.
