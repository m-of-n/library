---
schema: "library-design-notes/v1"
id: iec-81001-5-1-2021-design-notes
record: iec-81001-5-1-2021
type: design-notes
updated: "2026-10-02"
---

# Design notes: IEC 81001-5-1 and tmodel

**Basis: the free IEC preview only.** That is Interpretation Sheet 1 (full text), the Introduction, the Scope, the ToC,
Figure 2 and the Bibliography. The normative activities (Clauses 4-9) were read as titles only, so every note below is
limited to that.

## Why it matters

- In medical devices this is the 62443-4-1 derivative that matters. FDA names it as a candidate SPDF and as partially
  meeting its testing recommendations (record `fda-premarket-cybersecurity-guidance`, §V and fn 48). FDA recognised
  it as consensus standard 13-122 (2022-12-19), per a secondary source.
- EN IEC 81001-5-1:2022 is the European adoption and is widely treated as MDR/IVDR state of the art. However, it was
  **not** among the standards added by Commission Implementing Decision (EU) 2026/1231 (11 June 2026), which amends the
  MDR harmonised-standards list (Decision 2021/1182).
- It structures security activities along the IEC 62304 software life-cycle: development 5.1-5.8, maintenance 6,
  security risk management 7, configuration management 8, problem resolution 9.

## Adopt

| # | What | tmodel target | Source |
|---|---|---|---|
| A1 | **Component support class** (MAINTAINED / SUPPORTED / REQUIRED). Add it as an attribute of Component, with nested clause applicability and downgrade transitions that re-trigger risk-transfer evaluation. | ARCH §1.1 Component, §3b lifecycle; DEC-009 | ISH1 4.3 Table 1, b), NOTE 2 |
| A2 | **62304-ordered process areas as the medical-software phase line.** Map Figure 2's 5.1→5.8 onto the canonical phase line (requirements = 5.2, design = 5.3/5.4, implementation = 5.5, verification = 5.6/5.7, release = 5.8), plus 6/9 for response. | R-041 Gate ordering; MAP-0001 phase table | 0.1, Figure 2 |
| A3 | **Two conformance routes.** A product claims either full conformance (Clauses 4-9) or *transitional* conformance (Annex F) for legacy software. Model the route as a facet of the conformance claim. | R-042 | 0.3; ISH1 NOTE 3 |

## Adapt

| # | What | Why |
|---|---|---|
| D1 | **Partial-strength crosswalk.** "derived from IEC 62443-4-1", yet "not necessarily a sufficient condition for conformance to IEC 62443-4-1" (0.3). The `counterpart_62443_4_1` values in `requirements.yaml` are our title-similarity inference. The real mapping is Annex D (D.1/D.2), which we could not read. | R-044 needs `maps_to {strength: equivalent \| partial \| derived}`, and our inferred pairs must stay `kind: inferred` until Annex D is read. |
| D2 | **Alternative terminology in a declaration of conformance.** ISH1 4.3 b) allows an organisation's own terms if the declaration maps them to the standard's categories. This is the same "canonical + local name" mechanism DL-0009 wants for gates. | Generalise it: every Requirement, Gate and category gets `canonical_id` plus `local_name`. |

## Reject

| # | What | Why |
|---|---|---|
| X1 | Inventing activity text or normativity for Clauses 4-9 from secondary sources. | Paywalled; title-only rows are marked `text_kind: title-only`, `normativity: unknown`. |

## Open questions

1. Annex D's published mapping to 62443-4-1 and Annex G's object identifiers (Table G.1) are the two pieces that would
   make this standard machine-joinable with `iec-62443-4-1-2018`. Both need the purchased text.
2. Table A.1 sets a *required level of tester independence*. FDA §V.C also asks for tester independence. Where does
   independence live in tmodel's Review/Evidence model?
3. Harmonisation: EN IEC 81001-5-1 is not cited in the OJ under the MDR as checked. Re-check at each amending decision.
