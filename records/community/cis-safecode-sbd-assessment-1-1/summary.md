---
schema: "library-summary/v1"
id: cis-safecode-sbd-assessment-1-1
record: cis-safecode-sbd-assessment-1-1
type: summary
updated: "2026-10-03"
---

# Secure by Design v1.1: A Guide to Assessing Software Security Practices (CIS / SAFECode)

|  |  |
|---|---|
| **Type** | spec (assessment guide + spreadsheet; record type `spec`) |
| **Maturity** | best-practice (published as a CIS white paper) |
| **Authors** | Center for Internet Security (CIS) and SAFECode |
| **Published** | 2026-07-09 (landing page); press releases 2026-07-14 (SAFECode) and 2026-07-15 (CIS) |
| **Source** | https://www.cisecurity.org/insights/white-papers/secure-by-design-v1-1-a-guide-to-assessing-software-security-practices |
| **Digest** | landing page only; the guide (zip with PDF + XLSX) is registration-walled and was not downloaded |

**Coverage warning.** Stub. Only the public landing page and press releases were read.

## Overview

An assessment guide for software security practices, built on the NIST SSDF and organised
as six considerations. It maps to the CIS Critical Security Controls, to development
groups, roles and artifacts, and v1.1 adds AI coverage. SAFECode describes it as
underlying a new ETSI standard and "consistent in content with" ETSI TS 104 219 — use the
`etsi-ts-104-219` record (full FX-1) for requirement content.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | SSDF-based assessment guide |
| Cryptography | none | |
| This project | adjacent | same content line as ETSI TS 104 219 (R-042, R-044) |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/object-model.yaml`, `object-model.md` | objects/edges from public material only (9 objects, 6 edges) |

## Limits

Content not read. Ingest the registered download if the assessment workbook (XLSX) is
needed as a fixture.
