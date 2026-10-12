---
schema: "library-summary/v1"
id: eo-14306
record: eo-14306
type: summary
updated: "2026-10-02"
---

# Executive Order 14306: Sustaining Select Efforts To Strengthen the Nation's Cybersecurity and Amending EO 13694 and EO 14144

|  |  |
|---|---|
| **Type** | spec (presidential executive order, amending) |
| **Maturity** | _unset_ — in force |
| **Authors** | President Donald J. Trump |
| **Published** | signed 2025-06-06; 90 FR 24723 (2025-06-11), FR Doc. 2025-10804 |
| **Identifier** | EO 14306 |
| **Source** | https://www.govinfo.gov/content/pkg/FR-2025-06-11/pdf/2025-10804.pdf |
| **Digest** | `74da9b4afc40c012e51f596c00fa42c42565b89c518228ce361c77728143987d` (4 pp, retrieved 2026-10-02) |

**Record status:** `summarized` (verified summary of SDL-relevant changes only). Topic kept as
`supply-chain-attestation`.

## Overview

An amending order. It does **not** amend EO 14028 (its title and text amend only EO 13694 and
EO 14144). SDL-relevant changes to EO 14144, verbatim locators:

- **§1(a)** "striking subsections 2(a)–(b) and redesignating subsections 2(c), 2(d), and 2(e) as
  subsections 2(a), 2(b), and 2(c)" — removes EO 14144's RSAA machine-readable attestation,
  artifact submission, CISA completeness/validation program, public posting of validation results
  and AG referral, and the related FAR amendment.
- **§1(b)** "striking the first sentence of subsection 2(e)" — i.e. original 2(e)'s first sentence, "Open source software plays a critical role in Federal information systems." (see Limits for how the numbering is resolved).
- **§2(b)** replaces the SSDF subsection with: NIST NCCoE consortium on SSDF-based practices **by
  August 1, 2025**; update SP 800-53 on securely deploying patches and updates **by September 2,
  2025**; preliminary SSDF update (secure and reliable development and delivery of software and the
  security of the software itself) **by December 1, 2025**, final within 120 days. EO 14144's
  steps to fold the updated SSDF into M-22-18 and revise CISA's attestation form are not carried
  over.
- Other changes outside SDL scope: new §1 policy text; PQC product-category list and TLS 1.3 by
  2030-01-02 (§2(d)); AI vulnerability management (§2(e)); rules-as-code pilot and FAR Cyber Trust
  Mark requirement for consumer IoT by 2027-01-04 (§2(f)); NSS carve-out (§2(g)); EO 13694
  sanctions limited to foreign persons (§3).

**Effect on attestation:** after EO 14306 no executive order directs CISA validation or FAR-based
submission of attestations; the remaining attestation mandate was OMB's M-22-18/M-23-16, which
**OMB M-26-05 rescinded on 2026-01-23** (agencies may still use the form voluntarily). The SSDF
update directive survives (see sp-800-218r1, other lane).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | sets the current direction of US federal software assurance |
| Cryptography | adjacent | PQC/TLS 1.3 directives |
| This project | adjacent | explains the regime change behind R-042 design (no single mandated attestation baseline); SSDF update feeds R-044 |

## Implementations

Searched 2026-10-02: n/a (amending order).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; `updates` eo-14144 |
| `summary.md` | this summary |

Local only: `.cache/eo-14306.{pdf,txt,raw.txt,clean.txt,md}`.

## Limits

Summary only. Whether NIST met the dated SSDF directives is out of scope here (see the SSDF
records). Resolved by the verifier (2026-10-03): EO 14306 consistently cites EO 14144 by its ORIGINAL numbering — §1(d) strikes a phrase that is in original 3(c) (not redesignated 3(c) = original 3(e)), §1(e) the word "novel" in original 3(c)(i)(A), §2(f) "section 7" = original §7 Aligning Policy to Practice, §2(g) "subsection 8(a)" = original NSS §8(a). So §1(b) strikes the first sentence of ORIGINAL 2(e), "Open source software plays a critical role in Federal information systems.", and §2(b) "striking subsection 2(c)" replaces the ORIGINAL SSDF subsection 2(c).
