---
schema: "library-design-notes/v1"
id: sp-800-53r5-design-notes
record: sp-800-53r5
type: design-notes
kind: design-notes
title: "sp-800-53r5 (SA/SR subset): bearing on the tmodel design"
updated: "2026-10-02"
extracted: "2026-10-02"
reviewed_by: ""
---

**Scope.** These notes cover only the in-scope controls (see `README.md`). Our own ids come from
`tmodel/spec/ARCH-0001-PROPOSAL-v0.2.0.md` and `design-log/0009-sdl-conformance-object`. None of
those decisions is accepted. Text marked **[analysis]** is this extraction's own reasoning.

## 1. Inbound crosswalk: SSDF 1.1 → SP 800-53 (in-scope controls)

The SSDF 1.1 References column (`sp-800-218`, official xlsx table) cites `SP80053:` ids per task.
The table below inverts that column for the in-scope controls. It is the SSDF's own mapping, not
ours. 800-53 publishes no reverse mapping to SSDF.

| 800-53 | SSDF 1.1 tasks citing it |
|---|---|
| SA-3 | PO.2.1 |
| SA-3(1) | PO.5.1 |
| SA-4 | PO.1.3, PW.4.1 |
| SA-8 | PO.1.1, PO.1.2, PO.2.2, PO.5.1, PS.2.1, PS.3.2, PW.1.1, PW.1.2 |
| SA-8(3) | PO.1.2, PW.4.1, PW.4.2 |
| SA-8(23) | PW.9.2 |
| SA-10 | PO.1.3, PS.1.1, PS.3.1, PW.1.2, RV.1.1, RV.2.1, RV.2.2 |
| SA-10(1) | PO.1.3 |
| SA-10(6) | PW.4.1 |
| SA-11 | PW.7.1, PW.7.2, PW.8.1, PW.8.2, RV.1.2, RV.2.2, RV.3.3 |
| SA-11(1) | PW.7.2 |
| SA-11(2) | PW.1.1 |
| SA-11(4) | PW.7.2 |
| SA-11(5) | PW.8.2 |
| SA-11(6) | PW.1.1 |
| SA-11(8) | PW.8.2 |
| SA-15 | PO.1.1, PO.1.2, PO.1.3, PO.3.1, PO.3.2, PO.3.3, PO.4.1, PO.4.2, PO.5.1, PO.5.2, PS.3.1, PW.6.1, PW.6.2, RV.3.4 |
| SA-15(1) | PO.4.1, PO.4.2 |
| SA-15(5) | PW.1.1 |
| SA-15(7) | PW.7.2, PW.8.2, RV.2.1, RV.2.2 |
| SA-15(10) | RV.1.3 |
| SA-15(11) | PO.4.2, PS.3.1 |
| SA-17 | PW.1.2 |
| SR-3 | PO.1.1, PO.1.2, PO.1.3, PS.3.2, PW.4.1, PW.4.4, RV.1.1 |
| SR-4 | PO.1.3, PS.3.1, PS.3.2, PW.4.1, PW.4.4, RV.1.1 |
| SR-4(3), SR-4(4) | PW.4.4 |
| SR-5 | PO.1.3 |
| SR-9 | PW.6.2 |

**[analysis]** SA-15 is the hub: 14 SSDF tasks cite it, and SSDF practice PO.4 ("security checks")
maps to SA-15(1) quality metrics at milestones. The traffic also runs the other way. Release 5.2.0
added **SI-2(7) Root Cause Analysis**, which its change log describes as "Identified as a gap from
analysis of the NIST SSDF" (SSDF RV.3). So 800-53 now absorbs SSDF content, and the crosswalk
(R-044) is bidirectional and versioned.

## 2. Bearing on our ids

| id | adopt / adapt / reject | why |
|---|---|---|
| **R-040** mitigation kind | **adopt (evidence)** | The SA controls cover all three kinds. Process: SA-3, SA-15. Documentation: SA-4(1) functional properties, SA-4(2) design and implementation information, SA-17 architecture. Technical: SA-8 principles, SA-11(1) static analysis. This supports `kind ∈ {technical, documentation, process}`. |
| **R-041** SDL / Gate | **adapt** | SA-3 requires an organization-defined SDLC with roles, which matches the SDL object. SA-15(1)'s "program review milestones" and "upon delivery" are the only milestone construct, and they have no ordering, so the DL-0009 Gate is richer than anything 800-53 states. SA-10.a's phase selection (design; development; implementation; operation; disposal) is coarser than the ARCH-0001 §3b LifecyclePhase enum. The mapping is many-to-one. |
| **R-042** conformance | **adopt the shape** | SA-11(2) has (a) contextual information, (b) tools and methods, (c) rigor and (d) evidence that meets acceptance criteria. That is a ready template for a threat-model acceptance check. Requirement: a tmodel `Requirement` must carry **organization-defined parameter values**, or the check is undecidable. |
| **R-043** governed views | **adopt** | SA-15(11) archives the release "together with the corresponding evidence supporting the final security and privacy review". That is a versioned, signed-off snapshot, which is our governed document-view. |
| **R-044** crosswalk | **adopt** | Two sources of `maps_to` data: the control's own Related Controls (intra-catalog, in `requirements.yaml`) and inbound citations from SSDF and SP 800-161 (§1). Use the stable 800-53 ids as join keys, and keep withdrawn ids with `incorporated_into` so that old citations resolve. For example, SA-15(4) → SA-11(2). |
| **DEC-009** mitigation lifecycle | **adapt** | SA-10.e (track flaws and resolution, then report) together with SA-11.d/e (verifiable flaw remediation, correct the flaws) and SI-2(7) (root cause, actions, then monitor effectiveness) form a lifecycle: found → tracked → remediated → verified, with root-cause feedback. This matches DEC-009's mitigation lifecycle. |

## 3. Open questions

1. **Source defect.** The OSCAL 5.2.0 catalog (last-modified 2026-05-11) carries SA-15(12)'s
   statement under SA-15(13) (usnistgov/oscal-content#304, #343). NIST's fix (PR #345,
   2026-09-24) was unmerged on 2026-10-02. We used the fix text. Re-check after the merge, and
   decide whether the library should pin OSCAL by commit hash rather than by "main".
2. Should Lane A extract SP 800-53B baselines or SP 800-53A assessment objectives as separate
   records? The objectives are the "verification" column that R-042 would actually run.
3. `obligated_party` (developer vs organization) is derived from statement wording. Should
   requirements.yaml v2 make it a standard field across the library?
