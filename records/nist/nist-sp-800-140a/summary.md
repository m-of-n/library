---
schema: "library-summary/v1"
id: nist-sp-800-140a
record: nist-sp-800-140a
type: summary
updated: "2026-09-26"
---

# NIST SP 800-140A — CMVP Documentation Requirements

|  |  |
|---|---|
| **Type** | spec (NIST SP) |
| **Maturity** | best-practice (CMVP validation authority document) |
| **Authors** | NIST |
| **Identifier** | SP 800-140A |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-140A.pdf (free) |
| **Digest** | `0fc31c5fdb7bd4a33a2490897d509da1fdedba59e10c46729ce11831fb611fd1` |

## Overview

Additional vendor documentation requirements (VE additions) a module submission must provide. It is part of the **FIPS 140-3** modification stack: it modifies **ISO/IEC 24759 (vendor documentation)**. Small set of documentation modifications, formatted as additions to ISO/IEC 24759 vendor evidence.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | CMVP crypto-module validation requirement |
| Cryptography | core | SP 800-140A content is cryptographic-module specific |
| This project | adjacent | A compliance/validation input we reference & model (#15), not the core threat model |

Bears on `DEC-009` (compliance / conformance). See `fips-140-3` for the umbrella.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/normative.md` | role, what it modifies/replaces, structure |

## Limits

Part of the FIPS 140-3 / ISO stack — its items are **modifications keyed to ISO/IEC 19790/24759** (paywalled), so this record captures role + structure, not every restated clause.
