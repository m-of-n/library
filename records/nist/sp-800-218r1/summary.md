---
schema: "library-summary/v1"
id: sp-800-218r1
record: sp-800-218r1
type: summary
updated: "2026-10-02"
---

# SP 800-218r1 ipd: Secure Software Development Framework (SSDF) Version 1.2 (Initial Public Draft)

|  |  |
|---|---|
| **Type** | spec (NIST Special Publication, **Initial Public Draft**) |
| **Maturity** | draft |
| **Authors** | Harold Booth, Michael Ogata, Murugiah Souppaya, Karen Kent, Donna Dodson (NIST; Kent: Trusted Cyber Annex) |
| **Published** | 2025-12-17 (dated December 2025); public comment 2025-12-17 to 2026-01-30 (closed) |
| **Identifier** | NIST SP 800-218r1 ipd · https://doi.org/10.6028/NIST.SP.800-218r1.ipd |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218r1.ipd.pdf (57 pp.) |
| **Digest** | `0f40af24b5d0175ced02dee971a89128f55ea9ac077963038b46cc9434a8d000` (sha256 of the PDF, retrieved 2026-10-02) |

## Currency check (2026-10-02)

- https://csrc.nist.gov/pubs/sp/800/218/r1/ipd (HTTP 200) lists "NIST SP 800-218 Rev. 1 (Initial Public Draft)", published December 17, 2025, with "Comments Due: January 30, 2026 (public comment period is CLOSED)".
- https://csrc.nist.gov/pubs/sp/800/218/r1/final returns **404**, and so does https://csrc.nist.gov/pubs/sp/800/218/r1/2pd. No final version and no second draft has been published.
- The SSDF project page https://csrc.nist.gov/projects/ssdf (last updated 2026-04-13) still presents **SSDF 1.1 (SP 800-218, Feb 2022)** as the current final version, and SP 800-218A as its only NIST community profile.
- **Result:** SSDF 1.2 is **still an Initial Public Draft**. This record is labelled `maturity: draft` throughout. **`sp-800-218` (SSDF 1.1) remains authoritative.** When NIST finalizes SP 800-218r1, the final document will supersede `sp-800-218`. That final will need a re-extraction, because draft and final text can differ. This record is linked to `sp-800-218` by `see_also` only, not by `supersedes`.

## Overview

The draft revises the SSDF, NIST's outcome-based set of secure software development practices grouped as Prepare the Organization (PO), Protect the Software (PS), Produce Well-Secured Software (PW) and Respond to Vulnerabilities (RV). The revision responds to EO 14306 (June 2025), which asked for updated "practices, procedures, controls, and implementation examples regarding the secure and reliable development and delivery of software". It keeps every SSDF 1.1 task id and adds two practices. **PO.6** is a continuous process improvement plan. **PS.4** makes software updates robust and reliable, covering tiered roll-out, rollback, anti-rollback and resilient update engines. It also adds ten notional examples to existing tasks, among them sharing threat models with customers under controlled disclosure, least-privilege design, input-format design, formal methods, a ban on default passwords and hard-coded secrets, and review of supplier ownership changes. It remaps the SP 800-53 references to Release 5.2.0 and the SP 800-161 references to r1-upd1, and **drops the EO 14028 mapping** (and its appendix). The result is 49 active tasks, 225 examples and 497 reference lines. The framework stays recommendation-grade guidance: "Organizations should …", and it is not a checklist.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The US federal baseline for secure software development, and the reference point for CISA self-attestation and procurement. |
| Cryptography | adjacent | Only through integrity verification (hashes, code signing: PS.2, PS.1 Ex 5) and FIPS-compliant encryption on development endpoints (PO.5.2 Ex 1). |
| This project | core | It is the backbone requirement set for the SDL object (R-041). Its tasks are the conformance units (R-042), its examples are typed mitigations (R-040), and its References column is a NIST-published crosswalk (R-044). PW.1.1 Ex 5 bears on governed threat-model views (R-043). Use it only as a *draft* delta over `sp-800-218`. |

Bears on R-040, R-041, R-042, R-043, R-044 and DEC-009. See `distilled/design-notes.md`.

## How it relates to the others

- **`sp-800-218`** (SSDF 1.1, final, Feb 2022) is the version this draft would replace. `distilled/diff-vs-v1.1.md` gives the complete diff: 2 new practices, 7 new tasks, 8 reworded tasks, 10 examples added to existing tasks and 25 reworded (corrected from 26 by the verify pass: RV.1.1 Ex 1 is unchanged), EO14028 removed, and SP 800-53 and SP 800-161 remapped. The draft's own change log under-reports these changes.
- **`sp-800-218a`** (SSDF Community Profile for generative AI) is built on SSDF 1.1 task ids, all of which survive in 1.2.
- **`sp-800-53r5`**: 1.2 maps tasks to SP 800-53 Release 5.2.0 controls, with zero-padded ids (`SA-08`).
- **`sp-800-161r1`**: the SP 800-161r1-upd1 mappings were rewritten, and dropped from 10 tasks (including PO.1.3).
- **`eo-14306`** is the driver. **`eo-14028`** is no longer mapped.
- Industry references are unchanged from 1.1 and pinned to old editions: BSIMM12, SAMM 1.5, ASVS 4.0.3, MASVS 1.4.2, SCVS 1.0, PCI Secure SLC 1.1, IEC 62443-4-1:2018, ISO/IEC 27034-1, 29147:2018, 30111:2019, the SAFECode papers, CNCF SSCP, MS SDL and NTIA SBOM minimum elements.

## Implementations

The SSDF is a practice framework, not software. Implementations and tooling (the CISA Secure Software Development Attestation Form, NIST OLIR mappings, vendor SSDF mappings) target SSDF 1.1 and are tracked on `sp-800-218`. Searched: NIST CSRC SSDF pages only, 2026-10-02. No implementation targets the 1.2 draft, and NIST has published no machine-readable 1.2 table (1.1 has one).

| Name | Kind | License | URL |
|---|---|---|---|
| NIST SSDF 1.1 table (xlsx); no 1.2 equivalent yet | official machine-readable table | US Gov public domain | https://csrc.nist.gov/files/pubs/sp/800/218/final/docs/nist.sp.800-218.ssdf-table.xlsx |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, cites and the FX-1 distillation block |
| `distilled/README.md` | index of the distilled artifacts, with coverage |
| `distilled/normative.md` | every practice, task, example and reference, and the framework "should" statements, verbatim with locators |
| `distilled/requirements.yaml` | 88 entries (framework, group, practice and task levels) with examples, `maps_to` crosswalk, derived audit fields and v1.1 change annotations |
| `distilled/design-notes.md` | adopt, adapt and reject decisions against R-040…R-044, DEC-009 and ARCH-0001 §2b and §3b |
| `distilled/object-model.yaml`, `distilled/object-model.md` | object-model pass: 86 objects, 104 edges and 8 gaps (32 objects / 48 edges ported from the sp-800-218 model by the verify pass), with a Mermaid diagram of the backbone |
| `distilled/diff-vs-v1.1.md` | full verbatim diff against SSDF 1.1 |

A local faithful Markdown capture of the whole draft is at `.cache/sp-800-218r1.md` (gitignored).

## Limits

- **It is a draft.** The comment period closed in January 2026, and the final text may add tasks to PO.6 and PS.4 (the draft asks for them), change examples, or alter mappings. Nothing here is citable as SSDF 1.2 final.
- Like 1.1, it is outcome-based and non-prescriptive. It sets no thresholds, no evidence requirements and no conformance levels, and §1 says it is "not to create a checklist". Any conformance scoring is our construct.
- It defines no gate sequence (§2 lines 311–313), no roles beyond examples, and no attestation format. The only attestation hook is the shared-responsibility agreement in §1.
- The references are pinned to stale editions (BSIMM12, SAMM 1.5, ASVS 4.0.3, CSF 1.1 for all pre-existing tasks), so the crosswalk needs edition translation.
- The draft contains small internal inconsistencies: "Protect Software (PS)" vs "Protect the Software (PS)", "Appendix C" vs Appendix B, and a change log that misses 6 of the 8 task-text changes.
