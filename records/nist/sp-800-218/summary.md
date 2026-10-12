---
schema: "library-summary/v1"
id: sp-800-218
record: sp-800-218
type: summary
updated: "2026-10-02"
---

# SP 800-218: Secure Software Development Framework (SSDF) Version 1.1

|  |  |
|---|---|
| **Type** | spec (NIST Special Publication, guidance) |
| **Maturity** | best-practice (final NIST SP; checked on CSRC 2026-10-02) |
| **Authors** | Murugiah Souppaya (NIST), Karen Scarfone (Scarfone Cybersecurity), Donna Dodson (NIST, former) |
| **Published** | February 2022 — supersedes CSWP 13 (SSDF 1.0, April 2020) |
| **Identifier** | NIST SP 800-218 · doi:10.6028/NIST.SP.800-218 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf (36 pp) + official table https://csrc.nist.gov/files/pubs/sp/800/218/final/docs/nist.sp.800-218.ssdf-table.xlsx |
| **Digest** | PDF `617746e553a9e2da49bfbd4eef0dfc3094758a39b869314e4173ac36605cde22` · xlsx `f5729c4c6c792cbf6cfbea74eee7cc84c579b2109006fe3cbfa8934eb460bd55` (retrieved 2026-10-02) |

## Currency check (2026-10-02)

- https://csrc.nist.gov/pubs/sp/800/218/final — SP 800-218 **SSDF Version 1.1**, final, February 2022.
- https://csrc.nist.gov/pubs/sp/800/218/r1/ipd — **SP 800-218 Rev. 1 (SSDF 1.2) Initial Public Draft**, published 2025-12-17, comments closed 2026-01-30.
- `https://csrc.nist.gov/pubs/sp/800/218/r1/final` and `…/r1/2pd` return 404; the SSDF project page (https://csrc.nist.gov/projects/ssdf, updated 2026-04-13) still describes v1.1 as the posted final.

**SSDF 1.1 is the current final version.** The 1.2 draft is held as record `sp-800-218r1` (`see_also`); on finalization it will supersede this record.

## Overview

The SSDF is a core set of high-level, outcome-based secure software development practices to be integrated into whatever SDLC an organization already uses, drawn from established documents (BSA, BSIMM, OWASP, SAFECode, IEC 62443-4-1, and others). Its argument: a common vocabulary lets producers reduce vulnerabilities in releases, limit the impact of the ones that escape, and fix root causes — and lets acquirers state requirements and compare suppliers. It is organized as four practice groups (PO Prepare the Organization, PS Protect the Software, PW Produce Well-Secured Software, RV Respond to Vulnerabilities), 19 practices and 42 tasks, each task with optional notional implementation examples and a References column that maps it to 29 other practice documents; Appendix A maps EO 14028 §4e to the tasks, which is why OMB M-22-18 and the CISA attestation form are built on it. It is explicitly not a checklist: practices are risk-based, unsequenced and adopter-tailored.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The US reference SDL practice set; federal attestation (EO 14028 → OMB M-22-18 → CISA form) rests on it |
| Cryptography | adjacent | Only code signing / hashes for release integrity (PS.1.1, PS.2.1) and FIPS-compliant encryption on endpoints (PO.5.2/E1) |
| This project | core | Hub of the R-044 crosswalk; task-level conformance (R-042); PW.1.1/PW.1.2/PW.2.1 make the threat model a reviewed SDL artifact (R-043); PO.4 criteria = Gate exit criteria (R-041); examples sort into R-040 mitigation kinds; RV.2.2/PW.1.2 give the DEC-009 lifecycle |

Topic: the record's pre-existing topic `supply-chain-attestation` is kept (brief rule); SDL membership is carried by the `sdl` tag.

## Implementations

Searched 2026-10-02 (web search; none recorded as build-on implementations in record.yaml). No open-source "SSDF engine" found. Building blocks:

| Name | Kind | License | URL |
|---|---|---|---|
| NIST SSDF 1.1 table (xlsx) | machine-readable source | public domain (US Gov) | https://csrc.nist.gov/files/pubs/sp/800/218/final/docs/nist.sp.800-218.ssdf-table.xlsx |
| NIST OLIR | informative-reference mapping program | US Gov | https://csrc.nist.gov/projects/olir |
| CISA Secure Software Development Attestation Form / RSAA | attestation built on SSDF | US Gov | record `cisa-ssdf-attestation-form-2024` |
| NIST OSCAL | machine-readable control catalogs (SP 800-53 side of the References) | public domain | https://pages.nist.gov/OSCAL/ |

Commercial "SSDF compliance" offerings (AppSec/ASPM vendor dashboards) exist; none assessed.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, cites (29 reference keys + footnote refs), FX-1 distillation block |
| `distilled/README.md` | artifact index, maps_to id-splitting rules, count table |
| `distilled/normative.md` | every normative statement verbatim with locator, incl. all of Table 1 |
| `distilled/requirements.yaml` | 79 typed entries (library-requirements/v2): 8 framework statements, 4 groups, 20 practices, 47 tasks, with examples, footnotes, maps_to crosswalk and reference_editions |
| `distilled/crosswalk.yaml` | maps_to pivoted per reference scheme + inverse index |
| `distilled/object-model.yaml` | object-model pass: 82 objects, 82 edges, 9 gaps |
| `distilled/object-model.md` | Mermaid diagrams + findings |
| `distilled/design-notes.md` | bearing on R-040..R-044, DEC-009 |

Local only (`.cache/`, gitignored): `sp-800-218.pdf`, `.txt` (pdftotext -layout), `.raw.txt`, `.ssdf-table.xlsx`, and `sp-800-218.md` (faithful Markdown capture of the whole document).

## Limits

- No conformance criteria, levels or assessment method; "well-secured", "qualified person", "sensitive data" and environment names are left to the adopter (§2), frequencies are "notional" (§1). 17 of 42 tasks are only partially testable without adopter bindings.
- No sequence and no gates: §2 says the table order "is not intended to imply the sequence of implementation"; gates appear once, in an example (PO.1.2/E2).
- The References column points at now-stale editions (BSIMM12, SAMM 1.5, ASVS 4.0.3, MASVS 1.4.2, SP 800-161r1 second draft, draft SP 800-216); crosswalk edges must carry the target edition.
- Source-internal tension: footnote 2 says SSDF practices "do not map to" NIST CSF Functions/Categories/Subcategories, yet the References column carries `NISTCSF` ids for 14 tasks — read the column as "related to"; recorded, not resolved.
- Provenance here is supply-chain provenance (PS.3.2, footnote 5); nothing on epistemic/review provenance (ARCH §4).
