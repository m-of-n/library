---
schema: "library-summary/v1"
id: openssl-2022-email-overflow
record: openssl-2022-email-overflow
type: summary
updated: "2026-11-04"
---

# CVE-2022-3786 and CVE-2022-3602: X.509 Email address buffer overflows

|  |  |
|---|---|
| **Type** | web (project blog) |
| **Maturity** | unset: a project blog FAQ accompanying the advisory; no body assigns it a standing |
| **Authors** | OpenSSL Project |
| **Published** | 2022-11-01 |
| **Identifier** | CVE-2022-3786, CVE-2022-3602 |
| **Source** | https://openssl-library.org/post/2022-11-01-email-address-overflows/ |
| **Digest** | `sha256:12ef0a3e…` (full value in `record.yaml`), fetched 2026-11-03, matched 2026-11-04; the 2026-11-01 digest no longer matches after a site rebuild (see `content.note`) |

## Overview

OpenSSL 3.0.7 fixed two buffer overflows in X.509 email address handling. CVE-2022-3602 is an arbitrary 4-byte stack overflow, first assessed CRITICAL because it might lead to remote code execution; after feedback from prenotified organisations it was downgraded to HIGH on 1 November 2022, before release. CVE-2022-3786 was never rated CRITICAL, since only the length of the overwrite, not its content, is attacker-controlled; both are HIGH as released. Both were "introduced as part of punycode decoding functionality (currently only used for processing email address name constraints in X.509 certificates)", code first added in 3.0.0. The post says any 3.0 application verifying certificates from untrusted sources should be considered vulnerable, including TLS clients and TLS servers that use client authentication.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | memory corruption in certificate verification |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | a cost of X.509 machinery that R-M-01 keeps out of the native encoding |

- **R-M-01** (native encoding SHALL NOT be X.509 / PKIX): the bugs sat in code that exists only to process internationalised email name constraints, a feature of the X.509 profile. A native format that does not carry that machinery does not carry this class of bug. This is supporting evidence for R-M-01, not the reason for it.

## Implementations

Fixed in OpenSSL 3.0.7. The post states OpenSSL 1.0.2, 1.1.1 and earlier are not affected, and that the FIPS provider is not affected.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** the blog FAQ whole. The formal advisory it links to was not read.

- The post says the project knew of no working exploit leading to RCE at the time of release.
- The bug class is a C memory-safety problem as much as a name-constraint problem, so it does not show that constraints are inherently unsafe.
- Related records link here, not from here: `go-nameconstraint-cves` and `rfc-9549` already carry `see_also` edges to this record.
