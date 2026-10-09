---
schema: "library-summary/v1"
id: nist-sp-800-140e
record: nist-sp-800-140e
type: summary
updated: "2026-09-26"
---

# NIST SP 800-140E — CMVP Approved Authentication Mechanisms

|  |  |
|---|---|
| **Type** | spec (NIST SP) |
| **Maturity** | best-practice (CMVP validation authority document) |
| **Authors** | NIST |
| **Identifier** | SP 800-140E |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-140E.pdf (free) |
| **Digest** | `26616caa396fc292dd1d726309e34287683c8089ea401f3dc7f55ccb671aa28e` |

## Overview

Approved authentication mechanisms and their strength requirements for module roles. It is part of the **FIPS 140-3** modification stack: it replaces **ISO/IEC 19790 Annex E and ISO/IEC 24759 §6.17 (replaced)**. Requirements + list for operator authentication strength.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | CMVP crypto-module validation requirement |
| Cryptography | core | SP 800-140E content is cryptographic-module specific |
| This project | adjacent | A compliance/validation input we reference & model (#15), not the core threat model |

Bears on `DEC-009` (compliance / conformance). See `fips-140-3` for the umbrella.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/normative.md` | role, what it modifies/replaces, structure |

## Limits

Part of the FIPS 140-3 / ISO stack — its items are **modifications keyed to ISO/IEC 19790/24759** (paywalled), so this record captures role + structure, not every restated clause.
