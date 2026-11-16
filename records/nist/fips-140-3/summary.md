---
schema: "library-summary/v1"
id: fips-140-3
record: fips-140-3
type: summary
updated: "2026-11-15"
---

# FIPS 140-3 — Security Requirements for Cryptographic Modules

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | standard (NIST FIPS, 2019; supersedes FIPS 140-2) |
| **Authors** | NIST |
| **Published** | 2019-03 (effective 2019-09-22) |
| **Identifier** | FIPS 140-3 · doi:10.6028/NIST.FIPS.140-3 |
| **Source** | https://csrc.nist.gov/pubs/fips/140-3/final (free) |
| **Digest** | `942a4f929dfbd2b4af2e4e03df7f6e6377054346afd9bee346ed0ebac5db384b` |

## Overview

FIPS 140-3 is the U.S. federal standard for validating **cryptographic modules**. It is an **umbrella/adoption** standard: rather than restating requirements, it **adopts ISO/IEC 19790:2012** (security requirements) and **ISO/IEC 24759:2017** (test requirements), with U.S. modifications in the **NIST SP 800-140x** series. Conformance is a **4-level × 11-area matrix** established through the **CMVP** validation program. It supersedes FIPS 140-2.

## Why it matters here

A deliberately **contrasting** requirement framework to ISO/SAE 21434:
- It **adopts another standard** rather than restating it → a real test of **cross-document conformance** (FIPS → ISO 19790, modified by SP 800-140x) for the compliance model (#15).
- Its requirements are a **level × area matrix** validated by a program — a different audit shape than 21434's tagged RQ/WP.
- Distilling it yields **structure, not a big requirement set** — a concrete demonstration that requirement granularity is bounded by the source (#5). The detail is in ISO/IEC 19790 (paywalled) + SP 800-140x (free).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The federal crypto-module security/validation standard |
| Cryptography | core | Defines crypto-module security requirements & approved functions |
| This project | adjacent | A compliance/validation regime we may reference & model, not the core threat-model |

Bears on `tmodel:DEC-005` (scope) and `tmodel:DEC-009` (compliance / product conformance), tmodel's register, not mofn's.

## Implementations

Validated via the **CMVP** (NIST/CCCS); a large public list of validated modules exists. Not surveyed as build-on-it tooling. searched: 2026-09-26.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata (adopts ISO 19790/24759; cites SP 800-140x; supersedes FIPS 140-2); `distillation` holds the FX-1 coverage counts |
| `distilled/` | the FX-1 artifact set (library#69): every requirement and the normative text, the derived message structures and schemas, protocol flows and lifecycles, and design notes; `distilled/README.md` is the index |

## Limits

- **Umbrella standard** — the detailed, auditable requirements are in **ISO/IEC 19790:2012** (paywalled, held only as a stub) and the **SP 800-140x** modifications (held as `nist-sp-800-140` to `nist-sp-800-140f`). The FX-1 extraction holds all of FIPS 140-3's own text; it cannot hold a per-area or per-level requirement, because the document states none.
- Native normative statements are few: the source's verbal forms include four shall and two must. No artifact is human-reviewed yet.
