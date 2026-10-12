---
schema: "library-normative/v1"
id: fips-140-3-normative
record: fips-140-3
type: normative
audience: human+ai
updated: "2026-09-26"
coverage: "Adoption model, security levels, 11 areas, CMVP, supersession. Detailed requirements are in ISO/IEC 19790 (paywalled) + SP 800-140x."
reviewed_by: ""
---

# FIPS 140-3 — distilled

## 1. What it is (and isn't)
FIPS 140-3, *Security Requirements for Cryptographic Modules* (NIST, 2019; effective 2019-09-22, testing began 2020-09-22). It **supersedes FIPS 140-2**. Crucially, FIPS 140-3 is an **adoption/umbrella** standard: it does **not** restate the requirements — it **adopts ISO/IEC 19790:2012(E)** (security requirements) and **ISO/IEC 24759:2017(E)** (test requirements), with U.S. modifications published in the **NIST SP 800-140x** series. So the detailed, auditable requirements live in ISO/IEC 19790 (**paywalled — logged, not held**) and SP 800-140/A–F (free).

## 2. Security levels (1–4)
Four increasing levels. A module gets a rating per area; the **overall level is the minimum across the 11 areas**. Higher levels add authentication strength, physical tamper evidence → detection/response, SSP protection, and environmental-attack resistance.

## 3. The 11 requirement areas
1 Cryptographic module specification · 2 Interfaces · 3 Roles, services & authentication · 4 Software/firmware security · 5 Operational environment · 6 Physical security · 7 Non-invasive security · 8 Sensitive security parameter (SSP) management · 9 Self-tests · 10 Life-cycle assurance · 11 Mitigation of other attacks.
Conformance is an **area × level matrix**; each cell's shall-statements are in ISO/IEC 19790.

## 4. Modifications (SP 800-140x, free)
- **800-140** general / validation authorities · **800-140A** documentation (mods to 24759) · **800-140B** security-policy requirements · **800-140C** approved security functions · **800-140D** approved SSP establishment methods · **800-140E** approved authentication mechanisms · **800-140F** non-invasive attack mitigation test metrics.

## 5. Validation & audit relevance
Conformance is established by the **CMVP** (Cryptographic Module Validation Program): a lab tests against ISO/IEC 24759 (as modified) and NIST/CCCS validate. The **auditable deliverable** most visible at this level is the **module security policy** (SP 800-140B). This is a *different* requirement/audit shape than ISO/SAE 21434: a program-validated **level × area matrix** whose detail is delegated to an adopted standard — a good stress test for the compliance model (tmodel #15) and for cross-document conformance (FIPS → ISO 19790 → SP 800-140x).

## 6. Granularity note (tmodel #5)
Distilling FIPS 140-3 yields **structure, not a large requirement set** — the opposite of ISO/SAE 21434's 118 tagged requirements. This is expected and honest: granularity is bounded by the source. To get the detailed cryptographic-module requirements we would ingest ISO/IEC 19790 (paywalled) and/or the SP 800-140x series (free) — a natural next step.
