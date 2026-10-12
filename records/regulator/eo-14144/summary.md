---
schema: "library-summary/v1"
id: eo-14144
record: eo-14144
type: summary
updated: "2026-10-02"
---

# Executive Order 14144: Strengthening and Promoting Innovation in the Nation's Cybersecurity

|  |  |
|---|---|
| **Type** | spec (presidential executive order) |
| **Maturity** | _unset_ — in force **as amended by EO 14306** |
| **Authors** | President Joseph R. Biden Jr. |
| **Published** | signed 2025-01-16; 90 FR 6755 (2025-01-17), FR Doc. 2025-01470 |
| **Identifier** | EO 14144 |
| **Source** | https://www.govinfo.gov/content/pkg/FR-2025-01-17/pdf/2025-01470.pdf |
| **Digest** | `006cddd54c6f3aeb42eb0ca48b36a692c13ad47d01c91ad47e7e07a99c82691d` (17 pp, retrieved 2026-10-02) |

**Record status:** `summarized` (lane B adds a verified summary of the SDL-relevant parts only;
no FX-1). Topic kept as `supply-chain-attestation`.

## Overview

Builds on EO 14028. The SDL-relevant part is **§2 "Operationalizing Transparency and Security in
Third-Party Software Supply Chains"** (read from the cached text):

- **§2(b) as issued** — OMB to recommend FAR language requiring software providers to submit to
  CISA's **RSAA** (A) machine-readable secure software development attestations, (B) high-level
  artifacts validating them, (C) a list of their FCEB agency customers (30 days); FAR Council to
  amend the FAR (120 days after); CISA to evaluate methods for machine-readable attestations and,
  as appropriate, give providers RSAA submission guidance "including a common data schema and
  format" (60 days after the recommendations); CISA to centrally verify completeness of all attestation forms and
  continuously validate a sample against artifacts; notify provider and agency of failures with a
  response process; the National Cyber Director to publicly post validation results by provider
  and software version, and "is encouraged to refer" failed attestations to the Attorney General.
- **§2(c) as issued** — NIST NCCoE consortium demonstrating SSDF-based practices (60 days); update
  SP 800-53 for secure patch deployment (90 days); preliminary SSDF update (180 days) and final
  version 120 days later; OMB to fold select updated-SSDF practices into M-22-18 (120 days after);
  CISA to revise the common attestation form accordingly (30 days after).
- **§2(d)** — OMB to require agencies to comply with NIST SP 800-161r1 C-SCRM across the
  acquisition lifecycle; **§2(e)** — CISA/OMB recommendations on open-source software assessment,
  patching and contribution.

**What survives (verified against eo-14306):** EO 14306 §1(a) **struck §2(a)–(b)** (the whole
RSAA machine-readable attestation / CISA validation / public posting / FAR package) and
redesignated §2(c)–(e) as §2(a)–(c); EO 14306 §2(b) replaced the SSDF subsection with dated
directives (NCCoE consortium by 2025-08-01; SP 800-53 patch guidance by 2025-09-02; preliminary
SSDF update by 2025-12-01, final within 120 days) and **dropped** the M-22-18 incorporation and
form-revision steps. Later, OMB M-26-05 (2026-01-23) rescinded M-22-18/M-23-16 altogether.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | federal software-assurance policy, SSDF update driver |
| Cryptography | adjacent | §4 (PQC, TLS) outside SDL scope |
| This project | adjacent | the struck §2(b) is the most complete design for machine-readable, validated, publicly reported attestations (R-042, R-044) — useful as a design reference even though withdrawn |

## Implementations

Searched 2026-10-02: CISA RSAA exists (softwaresecurity.cisa.gov); no machine-readable attestation
schema from CISA found (the directive was struck). SSDF update: sp-800-218r1 record (other lane).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; `updated_by` eo-14306 |
| `summary.md` | this summary |

Local only: `.cache/eo-14144.{pdf,txt,raw.txt,clean.txt,md}`.

## Limits

Summary only (no requirement extraction). Resolved by the verifier (2026-10-03): EO 14306 consistently cites EO 14144 by its ORIGINAL numbering — §1(d) strikes a phrase that is in original 3(c) (not redesignated 3(c) = original 3(e)), §1(e) the word "novel" in original 3(c)(i)(A), §2(f) "section 7" = original §7 Aligning Policy to Practice, §2(g) "subsection 8(a)" = original NSS §8(a). So §1(b) strikes the first sentence of ORIGINAL 2(e), "Open source software plays a critical role in Federal information systems.", and §2(b) "striking subsection 2(c)" replaces the ORIGINAL SSDF subsection 2(c). The open-source subsection therefore survives (as redesignated 2(c)) minus its first sentence.
