---
schema: "library-summary/v1"
id: nist-sp-800-140c
record: nist-sp-800-140c
type: summary
updated: "2026-09-26"
---

# NIST SP 800-140C — CMVP Approved Security Functions

|  |  |
|---|---|
| **Type** | spec (NIST SP) |
| **Maturity** | best-practice (CMVP validation authority document) |
| **Authors** | NIST |
| **Identifier** | SP 800-140C |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-140C.pdf (free) |
| **Digest** | `8edf4f1f64bbdf62660f7b1b19f10e95a2d9a5671533530b2eb1dfb9e10dd0f4` |

## Overview

The maintained LIST of CMVP-approved security functions (cryptographic algorithms), by reference to the NIST FIPS/SP crypto standards. It is part of the **FIPS 140-3** modification stack: it replaces **ISO/IEC 19790 Annex C (replaced)**. A reference list, not narrative requirements; kept current as algorithms are approved/withdrawn.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | CMVP crypto-module validation requirement |
| Cryptography | core | SP 800-140C content is cryptographic-module specific |
| This project | adjacent | A compliance/validation input we reference & model (#15), not the core threat model |

Bears on `DEC-009` (compliance / conformance). See `fips-140-3` for the umbrella.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/normative.md` | role, what it modifies/replaces, structure |

## Limits

Part of the FIPS 140-3 / ISO stack — its items are **modifications keyed to ISO/IEC 19790/24759** (paywalled), so this record captures role + structure, not every restated clause.
