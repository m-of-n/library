---
schema: "library-summary/v1"
id: nist-sp-800-140b
record: nist-sp-800-140b
type: summary
updated: "2026-09-26"
---

# NIST SP 800-140B — CMVP Security Policy Requirements

|  |  |
|---|---|
| **Type** | spec (NIST SP) |
| **Maturity** | best-practice (CMVP validation authority document) |
| **Authors** | NIST |
| **Identifier** | SP 800-140B |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-140B.pdf (free) |
| **Digest** | `60bc7223fa81f21724d0d4cd74e5a7e5df52cba928c8187803290ccaa398424c` |

## Overview

Defines the content and tabular format of the cryptographic module security policy — the primary PUBLIC, auditable deliverable of a FIPS 140-3 validation. Directly realizes fips-140-3#security-policy. It is part of the **FIPS 140-3** modification stack: it modifies **ISO/IEC 19790 Annex B and ISO/IEC 24759 §6.14**. Specifies required sections/tables of the security policy; the deliverable an auditor/consumer reads to confirm conformance.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | CMVP crypto-module validation requirement |
| Cryptography | core | SP 800-140B content is cryptographic-module specific |
| This project | adjacent | A compliance/validation input we reference & model (#15), not the core threat model |

Bears on `DEC-009` (compliance / conformance). See `fips-140-3` for the umbrella.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/normative.md` | role, what it modifies/replaces, structure |

## Limits

Part of the FIPS 140-3 / ISO stack — its items are **modifications keyed to ISO/IEC 19790/24759** (paywalled), so this record captures role + structure, not every restated clause.
