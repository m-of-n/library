---
schema: "library-summary/v1"
id: cisa-ssdf-attestation-form-2024
record: cisa-ssdf-attestation-form-2024
type: summary
updated: "2026-10-02"
---

# Secure Software Development Attestation Form (CISA, v1.0)

|  |  |
|---|---|
| **Type** | spec (federal information-collection form + instructions) |
| **Maturity** | _unset_ — PRA-approved federal form; agency use optional since 2026-01-23 |
| **Authors** | CISA (DHS), with OMB |
| **Published** | final form released 2024-03-11; instructions PDF dated 2024-04 |
| **Identifier** | OMB Control No. 1670-0052, expires 03/31/2027; form Version 1.0 |
| **Source** | https://www.cisa.gov/sites/default/files/2024-04/Self_Attestation_Common_Form_FINAL_508c.pdf |
| **Digest** | `a8d6b568f1c96a18c711e656ebc66fa06e757d53f444ae45d8d23d1414a7dacb` (10 pp; bytes from the Internet Archive copy because cisa.gov returns 403 to scripts) |

**Currency (checked 2026-10-02).** No revision of the form after v1.0 found (CISA page and
search). Verifier (2026-10-03): the CISA landing page https://www.cisa.gov/secure-software-attestation-form (Internet Archive capture 2026-08-09) confirms "CISA released the Secure Software Development Attestation Form on March 11, 2024" and is now flagged by CISA as **"Archived Content"**; the PDF bytes match all 25 Internet Archive 200/revisit captures of the official URL (SHA-1 SPUES7JA…). The OMB control number is current to 2027-03-31. **Regime change:** OMB **M-26-05**
(2026-01-23) rescinded M-22-18 and M-23-16, so agencies are **no longer required** to collect
this form; they "may choose to use" it (omb-m-26-05#R-0006). EO 14306 (2025-06-06) had earlier
struck EO 14144's plan to have CISA validate attestations and to put them in the FAR (eo-14306).

## Overview

The "common form" M-22-18 asked CISA to build. A software producer's CEO (or a designee who can
bind the company) attests that the company "presently makes consistent use" of practices derived
from the SSDF in developing the named software: secure, separated and monitored build
environments with MFA and encrypted secrets (1a–1f), trusted source-code supply chains (2),
provenance for internal and third-party code (3), and automated vulnerability checking before
release with a remediation policy and a vulnerability disclosure program (4a–4c). Alternatives:
attach a FedRAMP/agency-approved 3PAO assessment (no signature), or give the agency a POA&M while
it seeks an OMB extension. Attestations bind future versions until the producer notifies that
its practices lapsed; false statements risk 18 U.S.C. § 1001. Submitted via CISA's RSAA
(softwaresecurity.cisa.gov) or by PDF to the agency. An Appendix maps each item to EO 14028
§4(e) and SSDF tasks.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | the US federal secure-development conformance instrument |
| Cryptography | adjacent | only "encrypting sensitive data, such as credentials" (1e) |
| This project | core | concrete governed, signed conformance document (R-043), conformance states incl. 3PAO and POA&M (R-042), release gate (R-041), and a source-published crosswalk (R-044); POA&M as mitigation lifecycle (DEC-009) |

## Implementations

Searched 2026-10-02. CISA operates the Repository for Software Attestations and Artifacts (RSAA)
at https://softwaresecurity.cisa.gov (login-gated; not inspected). Many vendors publish their
signed forms or attestation letters (e.g. Oracle's "Secure Software Development Attestation
Form" statement of direction surfaced in search). No open-source tool generating/validating the
form found; `distilled/schema` is ours.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, identifiers (OMB control number, RSAA URL, archived copy), distillation |
| `distilled/README.md` | index |
| `distilled/normative.md` | every statement verbatim + the Appendix crosswalk table |
| `distilled/requirements.yaml` | 67 typed entries with `maps_to` EO 14028 §4(e) and SSDF |
| `distilled/schema/` | derived JSON Schema of the form |
| `distilled/messages.yaml` | the form and related documents as messages |
| `distilled/protocol.*` | submission flows + Mermaid |
| `distilled/state-machine.yaml` | attestation lifecycle |
| `distilled/examples/` | filename vector + two schema test instances |
| `distilled/object-model.*` | object-model pass |
| `distilled/design-notes.md` | bearing on tmodel |

Local only: `.cache/cisa-ssdf-attestation-form-2024.{pdf,txt,md}`.

## Limits

Company-level self-attestation of qualitative practices ("good-faith effort", "to the greatest
extent feasible"): no evidence is required with the form, so it is a weak conformance signal (our assessment; M-26-05's stated criticism is of M-22-18's "unproven and burdensome software accounting processes that prioritized compliance over genuine security investments"). Covers only producer-developed code. The Appendix mapping is coarse
(item 4 mapped as a block; VDP not mapped to EO §4(e)(viii)). The online RSAA form may differ
from the PDF.
