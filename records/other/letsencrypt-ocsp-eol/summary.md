---
schema: "library-summary/v1"
id: letsencrypt-ocsp-eol
record: letsencrypt-ocsp-eol
type: summary
updated: "2026-11-01"
---

# OCSP Service Has Reached End of Life

|  |  |
|---|---|
| **Type** | web (blog post) |
| **Maturity** | `informational`: CA announcement |
| **Authors** | Josh Aas |
| **Published** | 2025-08-06 |
| **Identifier** | Let's Encrypt blog, 2025-08-06 |
| **Source** | https://letsencrypt.org/2025/08/06/ocsp-service-has-reached-end-of-life |
| **Digest** | `sha256:d1ffd905…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Let's Encrypt turned off OCSP on August 6, 2025, and will publish revocation only through CRLs. The main reason given is privacy: a CA running a responder learns which site is being visited from which IP address, and even a CA that keeps no logs could be compelled to. The second is simplicity. At peak the service handled about 340 billion requests a month, over 140,000 a second at the CDN.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | privacy and operations of revocation |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-O-02 |

- **R-O-02**: an online check leaks to the issuer who is relying on what. Any optional online check in R-M-09 inherits that leak.

## Implementations

Not applicable.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** whole.

- One CA's decision. No other CA's status was checked.
- The traffic figures are the post's own.
