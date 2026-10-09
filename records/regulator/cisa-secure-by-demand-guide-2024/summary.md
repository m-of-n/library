---
schema: "library-summary/v1"
id: cisa-secure-by-demand-guide-2024
record: cisa-secure-by-demand-guide-2024
type: summary
updated: "2026-10-02"
---

# Secure by Demand Guide: How Software Customers Can Drive a Secure Technology Ecosystem

|  |  |
|---|---|
| **Type** | spec (joint guidance) |
| **Maturity** | best-practice (voluntary guidance) |
| **Authors** | CISA and FBI |
| **Published** | 2024-08-06 ("As of August 2024") |
| **Identifier** | https://www.cisa.gov/resources-tools/resources/secure-demand-guide |
| **Source** | https://www.cisa.gov/sites/default/files/2024-08/SecureByDemandGuide_080624_508c.pdf (bytes from the Internet Archive id_ copy; cisa.gov returns 403 to scripts) |
| **Digest** | `4efa7d2e082dcb7f6d53f2812c9eeb4bb420b3e8d811df6df664021b13d9edca` (4 pp, retrieved 2026-10-02) |

**Currency (checked 2026-10-02).** CISA resource page: published 2024-08-06, no revision. The 2025
follow-on is a separate document, *Secure by Demand: Priority Considerations for OT Owners and
Operators when Selecting Digital Products* (2025-01-13; record cisa-secure-by-demand-ot-2025).
No general "2025 Secure by Demand priorities" for enterprise software was found.

## Overview

The customer-side counterpart of Secure by Design: buyers should explicitly demand product
security (not just the supplier's enterprise security) before, during and after procurement.
It gives questions in six areas — general (pledge status, patching), authentication (SSO and
MFA by default at no cost, no default passwords), eliminating vulnerability classes (with a
roadmap), evidence of intrusions (baseline logs; cloud/SaaS ≥ 6 months at no charge), supply
chain (machine-readable complete SBOM, OSS vetting/OSPO), vulnerability disclosure (CWE+CPE in
every CVE, public VDP authorizing testing) — and lists artifacts to collect from the manufacturer
(SBOM, roadmaps) or yourself (baseline features, VDP page, CVE record quality, pledge reports).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | acquisition-side SbD checklist |
| Cryptography | none | — |
| This project | adjacent | consumer-side conformance view over the same Requirements (R-042/R-043), supplier vs customer-collected evidence provenance, concrete automatable checks; R-044 via pledge goals |

## Implementations

Searched 2026-10-02: none (questionnaire guidance). Related: MVSP (mvsp.dev) checklist.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/README.md` | index |
| `distilled/normative.md` | all items verbatim |
| `distilled/requirements.yaml` | 44 typed items (`#AUTH-Q2`, `#EI-2`, `#ART-S3` …) |
| `distilled/object-model.*` | object-model pass |
| `distilled/design-notes.md` | bearing on tmodel |

Local only: `.cache/cisa-secure-by-demand-guide-2024.{pdf,txt,raw.txt,md}`.

## Limits

Four pages; questions with no scoring, thresholds (except 6-month logs) or verification method.
Enterprise software focus; OT is covered by the 2025 companion.
