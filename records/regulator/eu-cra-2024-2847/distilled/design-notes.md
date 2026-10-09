---
schema: "library-design-notes/v1"
id: eu-cra-2024-2847-design-notes
record: eu-cra-2024-2847
type: design-notes
updated: "2026-10-02"
---

# Design notes — how the CRA bears on tmodel

Decision ids are from tmodel `spec/ARCH-0001-PROPOSAL-v0.2.0.md` and `design-log/0009-sdl-conformance-object` (R-040..R-044,
DEC-009). Requirement ids are `eu-cra-2024-2847#…` from `requirements.yaml`.

## Why this source matters more than the voluntary SDLs

The CRA is the first binding, horizontal, product-law SDL in a major market. Art 14 reporting has applied since
**11 September 2026**, so it is in force today. Everything else applies from **11 December 2027**. It turns three things
that were voluntary into legal obligations: a threat model ("cybersecurity risk assessment", Art 13(2)-(3)), a release
gate ("without known exploitable vulnerabilities", Annex I Part I(2)(a)), and vulnerability handling (Annex I Part II).
Each is evidenced in a governed, versioned, retained document set (Art 31 and Annex VII). Fines reach EUR 15 M or 2.5 %
of turnover (Art 64(2)). For tmodel this is the strongest external justification for R-041..R-043.

## Adopt

| # | What | tmodel target | Source |
|---|---|---|---|
| A1 | **The threat model is the Art 13 cybersecurity risk assessment.** Model a product's threat model so it can be emitted as the Annex VII point 3 risk assessment. It is based on intended purpose, reasonably foreseeable use and misuse, conditions of use, operational environment, assets to protect and expected use time. | R-043 governed view; ARCH §3 Environment; §3b LifecyclePhase | `#Art13(2)`, `#Art13(3)-2`, `#AnnexVII(3)` |
| A2 | **Per-requirement applicability table.** For each Annex I Part I(2)(a)-(m) item record `applicable`, `implementation` (pointer to MitigationInstance(s)) and `justification` when not applicable. This is the R-042 conformity object in its legal form. | R-042, R-044 (`Requirement` + `maps_to`) | `#Art13(3)-3`, `#Art13(4)-3` |
| A3 | **Mitigation kinds.** The CRA needs all three kinds. Technical: security update, secure-by-default configuration, exploit mitigations. Documentation: user information, secure-use instructions, advisories. Process: CVD policy, regular testing, due diligence. Adopt `MitigationInstance.kind ∈ {technical, documentation, process}` exactly as R-040 proposes. | R-040, DEC-009 | `#AnnexI-PartI(2)(b)`, `#AnnexII(8(a))`, `#AnnexI-PartII(5)` |
| A4 | **Release gate.** "Placing on the market" is a gate with explicit exit criteria. Technical documentation must exist (Art 13(12)), the conformity assessment must be done, the DoC drawn up and the CE marking affixed, there must be no known exploitable vulnerabilities, the support period must be set and published, and the SBOM must exist. Model it as a `Gate` with these as exit criteria, each a `Requirement`. | R-041 Gate; R-042 | `#Art13(12)-1..3`, `#AnnexI-PartI(2)(a)`, `#Art13(19)-1`, `#AnnexI-PartII(1)` |
| A5 | **Dated support window.** `SupportPeriod {start, end_month_year, rationale}` on the product, with the invariants `end - start >= 5y` (or expected use time), update availability `max(10y, remainder)` and documentation retention `max(10y, support period)`. This supplies the `valid_from/valid_to` that ARCH §3b says is still missing. | ARCH §3b; R-041 | `#Art13(8)-5`, `#Art13(9)`, `#Art13(13)` |
| A6 | **Vulnerability states with provenance.** Add `known_exploitable` and `actively_exploited` as states of `Vulnerability`. Each needs an Assertion (evidence) and a Review, because the state change starts legal clocks. | ARCH §4 Assertion/Review; §5 VEX | `#Art14(1)-1`; Art 3(41)-(42) |
| A7 | **SBOM ⇄ composed_of.** The Annex I Part II(1) SBOM, with top-level dependencies at minimum, is a materialisation of `composed_of`/`uses_component`. Export it as SPDX or CycloneDX (library records `spdx-3-0-1`, `cyclonedx-1-7`). | ARCH §1.1, §5 propagation | `#AnnexI-PartII(1)` |

## Adapt

| # | What | Why adapt |
|---|---|---|
| D1 | **Art 14 reporting as an automatable conformity check.** Given `aware_at`, `measure_available_at` and submission timestamps, SM1 and SM2 in `state-machine.yaml` decide "on time / breached" mechanically. tmodel should *store* these events (with provenance) but not *be* the reporting tool. The ENISA SRP is the channel. | Post-MVP (ADR-0002 scope guard). Keep `Notification` as a governed view over Vulnerability/Incident state, with no SRP client. |
| D2 | **Incident object.** CRA reporting needs `Incident` → `SevereIncident` (Art 14(5) guard). tmodel has `ThreatInstance` (designed threat) and `Finding` (discovered weakness) but nothing for an operational occurrence. Add it as a thin object linked to ThreatInstance via `realizes` and keep it out of the epistemic Assertion spine. | Avoids overloading ThreatInstance (critic M6 Environment-vs-phase discipline). |
| D3 | **Party roles.** The CRA's actors are relational, as ARCH §2b already prefers: manufacturer, importer, distributor, authorised representative, steward, component maintainer. Arts 21-22 turn an importer or distributor into a "manufacturer" by conduct. Adopt edge roles, and add `CSIRT` and `market-surveillance-authority` as intrinsic Party classifications, beside `cna`. | Matches critic M2; no new node types. |
| D4 | **Jurisdiction.** `made_available_in` Member States drives dissemination (Art 16(2)), and main establishment drives which CSIRT receives the report (Art 14(7)). Add a minimal `Jurisdiction` value set. Do not add a market model. | Only needed if reporting views are built. |
| D5 | **DoC as a Review.** The EU declaration of conformity is a signed approval over a governed view (the technical documentation). Represent it as a `Review` with `verdict=conforms` and a signer Party. It is not a separate document type. | Keeps R-043 "documents are governed views" consistent. |

## Reject

| # | What | Why |
|---|---|---|
| X1 | Modelling the CRA's conformity-assessment procedures (modules A, B+C, H, EUCC), notified bodies and market surveillance (Arts 32-60). | Not extracted. These belong to the assessor, not the product's threat model. Out of tmodel scope. |
| X2 | Treating draft harmonised standards (prEN 40000-x, ETSI EN 304 6xx) as conferring a presumption of conformity. | Art 27: the presumption exists only once the reference is cited in the OJ. None is cited as of 2026-10-02. Map to them in R-044 as `draft`. |
| X3 | Encoding the ENISA SRP form as our schema. | The form is not in the Regulation, and Art 14(10) leaves format to an implementing act that has not been adopted. Our derived JSON Schema is for internal checks only. |

## Crosswalk hooks (R-044)

The CRA publishes no mapping to other frameworks. Natural `maps_to` targets for the SDL lane:
- Annex I Part II ↔ ISO/IEC 30111 (handling) and 29147 (disclosure); IEC 62443-4-1 DM-1..DM-6 and SUM-1..SUM-5; NIST SSDF RV.1-RV.3.
- Art 13(2)-(3) risk assessment ↔ SSDF PW.1.1, 62443-4-1 SR-2, ISO/SAE 21434 cl.15.
- Annex I Part I(2)(a) release gate ↔ SSDF PW.8 / PO.4, 62443-4-1 SVV-1..SVV-4.
- Annex I Part II(1) SBOM ↔ SSDF PS.3.2, NTIA/CISA minimum elements (`ntia-2021-sbom-minimum`, `cisa-2026-sbom-minimum`).
- Art 13(5) due diligence ↔ SSDF PW.4, 62443-4-1 SM-9/SM-10.
These are *our* mappings (kind: inferred). They belong in MAP-0001 and not in this record's `requirements.yaml`.

## Open questions (including defects in the source)

1. **Art 16 application date vs Art 14.** Art 71(2) applies Art 14 from 2026-09-11, but Art 16 (the single reporting platform that Art 14(1), (3) and (7) require) falls under the general date of 2027-12-11. In practice ENISA opened the SRP on 2026-09-11 ("The CRA Single Reporting Platform is launched", ENISA press release 11 September 2026, linked from https://www.enisa.europa.eu/topics/product-security-and-certification/single-reporting-platform-srp, checked 2026-10-02: "initial operating capability"). Formally, the CSIRT-side duties in Arts 15-17 (dissemination, MSA forwarding, EUVD) look like they apply only from 2027-12-11. **Source inconsistency; record, do not resolve.**
2. **Wrong cross-reference in Art 16(2).** The second subparagraph says the sensitivity indication is made "under Article 14(2), point (a)", but sensitivity is in Art 14(2)(b) and 14(4)(b). **Source defect.**
3. **Clock origin for severe incidents.** The 24 h runs from awareness "of it" (the severe incident). The text does not say whether the clock starts when the manufacturer becomes aware of the incident or of its severity under Art 14(5). The recitals are silent (checked).
4. **No upper bound on the vulnerability final report.** T14d starts only when a corrective or mitigating measure is available, so an unfixed AEV has no final-report deadline. Does tmodel flag "AEV with no measure after N days" as a conformity risk anyway?
5. **Art 64(10) corrigendum.** The OJ text exempted micro and small enterprises "from paragraphs 3 to 9", which made the exemption for missing the Art 14 24 h deadline meaningless, because Art 14 fines are in paragraph 2. Corrigendum OJ L 2025/90555 (2.7.2025) changes this to "2 to 9". Our requirement uses the corrected text. Anyone citing the OJ PDF alone gets it wrong.
6. **EHDS amendment pending.** Regulation (EU) 2025/327 Art 104 rewrites Art 13(4) and Art 31(3) and inserts Art 32(5a) for EHR systems, from 26 March 2027. No consolidated CRA text after 2024-11-20 exists yet. When one is published, re-capture and diff.
7. **"Without known exploitable vulnerabilities" needs a knowledge-state cut-off.** Known *to whom*, and as of when? The release gate in A4 needs `as_of` and `source` (VEX-style) to be checkable.
8. **Harmonised standards.** When prEN 40000-1-2 (principles and risk management) and prEN 40000-1-3 (vulnerability handling) are cited in the OJ, they will be the operational definition of Annex I. They should get their own library records and replace the inferred crosswalk above. They are paywalled at CEN/CENELEC; public-enquiry drafts circulated through national bodies.
9. **Art 64 applies later than Art 14** *(verify pass)*. Art 71(2) brings forward only Art 14 and Chapter IV; Art 64 (penalties) applies from 2027-12-11. Read literally, the Regulation sets no fine for an Art 14 breach between 2026-09-11 and 2027-12-11. The state machines keep `deadline-breached` as a compliance flag regardless; whether national penalty rules fill the gap is a legal question, not answerable from this text.
