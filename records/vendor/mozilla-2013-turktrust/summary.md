---
schema: "library-summary/v1"
id: mozilla-2013-turktrust
record: mozilla-2013-turktrust
type: summary
updated: "2026-11-04"
---

# Revoking Trust in Two TurkTrust Certificates

|  |  |
|---|---|
| **Type** | web (blog post) |
| **Maturity** | unset: a vendor announcement; no body assigns it a standing |
| **Authors** | Michael Coates (signs the post; the byline reads "mozilla") |
| **Published** | 2013-01-03 |
| **Identifier** | Mozilla Security Blog, 2013-01-03 |
| **Source** | https://blog.mozilla.org/security/2013/01/03/revoking-trust-in-two-turktrust-certficates/ |
| **Digest** | `sha256:d9780cf1…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

TURKTRUST mis-issued two intermediate certificates to customers, and at least one was used for man-in-the-middle traffic management of domains the customer did not own. Mozilla revoked trust in both, in an update due on January 8, and suspended inclusion of TURKTRUST's newer root pending review. A mistake at a single CA gave a customer the ability to sign for any domain.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | a mis-issued CA certificate is a global capability |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-M-03 |

- **R-M-03**: a certificate's power came from who issued it, not from any relation to the names it signed.

## Relations

- `see_also: mozilla-2013-anssi`: the same mechanism eleven months later: an intermediate chaining to an included root, placed in a MITM traffic-management device for names its holder did not own, reported by Google, and handled by Mozilla revoking trust in a certificate store update.
- The earlier `see_also` to `foxit-2012-black-tulip` was removed on 2026-11-04: it had no stated reason, and DigiNotar was a compromise, not a mis-issuance; both already meet through `bears_on: R-M-03`.

## Implementations

Not applicable.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** post and update whole, comments skimmed.

- **R-001 §4.8 says TURKTRUST was "again caught by Chrome pinning". This post does not say that.** It says only that the issue was reported by Google. The claim needs another source.
- Further action on the CA was referred to the mozilla.dev.security.policy forum; that discussion was not read.
- The count of two rests on TURKTRUST's own review of its records.
