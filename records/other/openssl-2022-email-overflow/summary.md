---
schema: "library-summary/v1"
id: openssl-2022-email-overflow
record: openssl-2022-email-overflow
type: summary
updated: "2026-11-01"
---

# CVE-2022-3786 and CVE-2022-3602: X.509 Email Address Buffer Overflows

|  |  |
|---|---|
| **Type** | web (project blog) |
| **Maturity** | `informational`: project advisory FAQ |
| **Authors** | OpenSSL Project |
| **Published** | 2022-11-01 |
| **Identifier** | CVE-2022-3786, CVE-2022-3602 |
| **Source** | https://openssl-library.org/post/2022-11-01-email-address-overflows/ |
| **Digest** | `sha256:0cb9a0d8…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

OpenSSL 3.0.7 fixed two buffer overflows in X.509 email address handling. CVE-2022-3602 is a 4-byte stack overflow first rated CRITICAL and lowered to HIGH during prenotification. CVE-2022-3786 is variable-length, with only the length under attacker control. They came from "punycode decoding functionality (currently only used for processing email address name constraints in X.509 certificates)", first added in 3.0.0. Any 3.0 application verifying certificates from untrusted sources was exposed, including TLS servers using client authentication.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | memory corruption in certificate verification |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | cost of the feature set R-M-01 declines |

- **R-M-01**: internationalised name constraints are complex enough that adding them to a mature C library opened an RCE-class bug. Not carrying that in a native format is a real benefit.

## Implementations

Fixed in OpenSSL 3.0.7. 1.1.1 and earlier are stated to be unaffected.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** the blog FAQ whole. The formal advisory it links to was not read.

- The post says no working RCE exploit was known at the time.
- The bug class is a C memory-safety problem as much as a name-constraint problem, so it does not show that constraints are inherently unsafe.
