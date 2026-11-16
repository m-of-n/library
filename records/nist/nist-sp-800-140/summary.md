---
schema: "library-summary/v1"
id: nist-sp-800-140
record: nist-sp-800-140
type: summary
updated: "2026-11-15"
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

The Derived Test Requirements (DTR): the Test Evidence (TE) / Vendor Evidence (VE) items a CMVP lab uses to test a module against FIPS 140-3. It modifies 22 assertions and their 29 VE and 47 TE items; `record.yaml` `distillation` has the keyword counts. It is part of the **FIPS 140-3** modification stack: it modifies **ISO/IEC 24759 (test requirements)**. Testable requirements are expressed as TE/VE modifications keyed to ISO/IEC 24759 clauses; full sense requires ISO/IEC 24759 (paywalled).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | CMVP crypto-module validation requirement |
| Cryptography | core | SP 800-140 content is cryptographic-module specific |
| This project | adjacent | A compliance/validation input we reference & model (#15), not the core threat model |

Bears on `tmodel:DEC-009` (compliance / conformance), tmodel's register, not mofn's. See `fips-140-3` for the umbrella.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; `distillation` holds the FX-1 coverage counts |
| `distilled/` | the FX-1 artifact set (library#69): every requirement and the normative text, the derived evidence structures and schemas, protocol flows and lifecycles, and design notes; `distilled/README.md` is the index |

## Limits

Part of the FIPS 140-3 / ISO stack — its items are **modifications keyed to ISO/IEC 24759** (paywalled, not held), so an assertion's unmodified TEs and VEs, and the base text each modification edits, are not here. The text rendering loses the underline and strikethrough that mark additions and deletions (`distilled/normative.md` SD-1): which words of a modified item are in force must be checked against the PDF.
