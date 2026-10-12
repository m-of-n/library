---
schema: "library-summary/v1"
id: nist-sp-800-140d
record: nist-sp-800-140d
type: summary
updated: "2026-09-26"
---

# NIST SP 800-140D — CMVP Approved Sensitive Security Parameter Generation and Establishment Methods

|  |  |
|---|---|
| **Type** | spec (NIST SP) |
| **Maturity** | best-practice (CMVP validation authority document) |
| **Authors** | NIST |
| **Identifier** | SP 800-140D |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-140D.pdf (free) |
| **Digest** | `23a9f6798c641653ca999b5a19838204f6e61ea58b42b21303bdfc00d2c20f0b` |

## Overview

The maintained LIST of approved SSP (key) generation and establishment methods. It is part of the **FIPS 140-3** modification stack: it replaces **ISO/IEC 19790 Annex D (replaced)**. A reference list of approved key-management methods; kept current.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | CMVP crypto-module validation requirement |
| Cryptography | core | SP 800-140D content is cryptographic-module specific |
| This project | adjacent | A compliance/validation input we reference & model (#15), not the core threat model |

Bears on `DEC-009` (compliance / conformance). See `fips-140-3` for the umbrella.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/normative.md` | role, what it modifies/replaces, structure |

## Limits

Part of the FIPS 140-3 / ISO stack — its items are **modifications keyed to ISO/IEC 19790/24759** (paywalled), so this record captures role + structure, not every restated clause.
