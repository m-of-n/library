---
schema: "library-summary/v1"
id: nist-sp-800-140
record: nist-sp-800-140
type: summary
updated: "2026-09-26"
---

# NIST SP 800-140 — FIPS 140-3 Derived Test Requirements (DTR): CMVP updates to ISO/IEC 24759

|  |  |
|---|---|
| **Type** | spec (NIST SP) |
| **Maturity** | best-practice (CMVP validation authority document) |
| **Authors** | NIST |
| **Identifier** | SP 800-140 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-140.pdf (free) |
| **Digest** | `dfb6d1b9c829c3d8caad960a4d0e3bcc076852604061dd755718c259d79fc3f7` |

## Overview

The Derived Test Requirements (DTR): the Test Evidence (TE) / Vendor Evidence (VE) items a CMVP lab uses to test a module against FIPS 140-3. Contains the bulk of the testable ~shall statements (136). It is part of the **FIPS 140-3** modification stack: it modifies **ISO/IEC 24759 (test requirements)**. Testable requirements are expressed as TE/VE modifications keyed to ISO/IEC 24759 clauses; full sense requires ISO/IEC 24759 (paywalled).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | CMVP crypto-module validation requirement |
| Cryptography | core | SP 800-140 content is cryptographic-module specific |
| This project | adjacent | A compliance/validation input we reference & model (#15), not the core threat model |

Bears on `DEC-009` (compliance / conformance). See `fips-140-3` for the umbrella.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/normative.md` | role, what it modifies/replaces, structure |

## Limits

Part of the FIPS 140-3 / ISO stack — its items are **modifications keyed to ISO/IEC 19790/24759** (paywalled), so this record captures role + structure, not every restated clause.
