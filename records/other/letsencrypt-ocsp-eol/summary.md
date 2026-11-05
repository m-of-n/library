---
schema: "library-summary/v1"
id: letsencrypt-ocsp-eol
record: letsencrypt-ocsp-eol
type: summary
updated: "2026-11-04"
---

# OCSP Service Has Reached End of Life

|  |  |
|---|---|
| **Type** | web (blog post) |
| **Maturity** | unset: CA announcement, no standing to verify |
| **Authors** | Josh Aas |
| **Published** | 2025-08-06 |
| **Identifier** | Let's Encrypt blog, 2025-08-06 |
| **Source** | https://letsencrypt.org/2025/08/06/ocsp-service-has-reached-end-of-life |
| **Digest** | `sha256:d1ffd905…` (full value in `record.yaml`), fetched 2026-11-01, re-checked 2026-11-04 |

## Overview

Let's Encrypt turned off OCSP on August 6, 2025, having stopped putting OCSP URLs in certificates more than 90 days earlier, and will publish revocation only through CRLs. The main reason given is privacy: a CA running a responder learns which website is being visited from which IP address, and even a CA that does not retain this could retain it by accident or be legally compelled to collect it. The second is keeping the CA simple. At peak, earlier in 2025, the service handled about 340 billion requests a month, more than 140,000 a second at the CDN and 15,000 at origin.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | privacy and operations of revocation |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-O-02 and R-M-09 |

- **R-O-02**: a large CA moved off online status checking while keeping revocation representable through CRLs.
- **R-M-09**: an online check leaks to the issuer who is relying on what. Any optional online check in the validity intersection inherits that leak.

## Relations

None authored. `cabforum-sc063` and `rfc-6960` carry their edges to this record.

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
