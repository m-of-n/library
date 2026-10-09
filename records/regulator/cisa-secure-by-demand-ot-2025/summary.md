---
schema: "library-summary/v1"
id: cisa-secure-by-demand-ot-2025
record: cisa-secure-by-demand-ot-2025
type: summary
updated: "2026-10-02"
---

# Secure by Demand: Priority Considerations for OT Owners and Operators when Selecting Digital Products

|  |  |
|---|---|
| **Type** | spec (joint guidance, TLP:CLEAR) |
| **Maturity** | best-practice (voluntary guidance) |
| **Authors** | CISA with NSA, FBI, EPA, TSA, ASD's ACSC, CCCS, EC DG CONNECT, BSI, NCSC-NL, NCSC-NZ, NCSC-UK |
| **Published** | 2025-01-13 |
| **Identifier** | https://www.cisa.gov/resources-tools/resources/secure-demand-priority-considerations-operational-technology-owners-and-operators-when-selecting |
| **Source** | https://www.cisa.gov/sites/default/files/2025-01/joint-guide-secure-by-demand-priority-considerations-for-ot-owners-and-operators-508c_0.pdf (Internet Archive id_ copy; cisa.gov 403s scripts) |
| **Digest** | `172daac421ad9d3c535cba962f9aa4a3b894065c4c2522bcdbb0f064c6696d16` (22 pp, retrieved 2026-10-02) |

**Secondary record — `status: summarized`.** Summary and object-model pass only, as allowed for
lane context-setters. Read in full (pdftotext). **Currency:** CISA's page lists this Jan 2025
guide plus a 2025-04 PDF (likely a re-issue/short version; not fetched). This is the only 2025
"Secure by Demand" priorities document found; it is OT-specific.

## Overview

Threat actors target *OT products* (not organizations) because weaknesses — weak authentication,
known vulnerabilities, limited logging, insecure defaults, legacy protocols — replicate across
victims. OT owners/operators ("buyers") should select products from manufacturers that
prioritize **12 security elements** (not in priority order): configuration management, logging
in the baseline product, open standards, ownership, protection of data, secure by default,
secure communications, secure controls, strong authentication, **threat modeling**,
vulnerability management, and upgrade and patch tooling. Each has a selection criterion,
questions to ask and "why this matters". It aligns with ISA/IEC 62443 (4-2 SL3, 3-3), NIST SP
800-82/800-213A and the EU CRA, and points to NIS2/RED/CE marking.

Most relevant to tmodel: element 10 asks for "a full and detailed threat model" that is kept
up to date, tracks public threat sources such as MITRE EMB3D, states the assumed external
controls, communication paths and intended environment, and has a roadmap for gaps; buyers
should partner with the manufacturer's threat-modeling capability. Element 11 asks for SBOM *and
HBOM*, CVE-based handling per ISO/IEC 29147/30111, CSAF advisories, VEX via CSAF, a CVD policy and
RFC 9116 security.txt.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | buyer-side OT product security criteria |
| Cryptography | adjacent | certificates that fail loudly; disabling SSL/TLS 1.0/1.1, SNMPv1/2, Telnet |
| This project | adjacent | demand-side case for an exportable product threat model (R-043), consumer-selected requirement profile (R-042), document-level alignment to 62443/CRA (R-044); VEX/CSAF ties to ARCH-0001 §5 |

## Implementations

Searched 2026-10-02: none specific. Related tooling: CSAF (OASIS) producers/validators,
security.txt generators, MITRE EMB3D.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, cites (62443, NIST, EMB3D, CSAF, 29147/30111, NIS2, CRA) |
| `distilled/README.md` | index |
| `distilled/object-model.yaml` + `.md` | object-model pass |

Local only: `.cache/cisa-secure-by-demand-ot-2025.{pdf,txt,raw.txt}`.

## Limits

Not extracted to FX-1 (secondary). OT-specific; no thresholds beyond named protocol versions; the
62443 alignment is asserted at document level, without an item-level mapping.
