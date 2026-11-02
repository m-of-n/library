---
schema: "library-summary/v1"
id: langley-2014-revchecking
record: langley-2014-revchecking
type: summary
updated: "2026-11-01"
---

# No, don't enable revocation checking

|  |  |
|---|---|
| **Type** | web (blog post) |
| **Maturity** | `informational`: personal blog by a Chrome engineer |
| **Authors** | Adam Langley |
| **Published** | 2014-04-19 |
| **Identifier** | ImperialViolet, 2014-04-19 |
| **Source** | https://www.imperialviolet.org/2014/04/19/revchecking.html |
| **Digest** | `sha256:564bc67b…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Everyone soft-fails, because hard-fail makes OCSP a single point of failure. So an attacker who can intercept traffic can block the check, and in the DNS-hijack case they can use stored responses or get new certificates. Langley calls this security theatre, and explains CRLSets as pushed lists of some high-value revocations. He names short-lived certificates or OCSP Must-Staple as the scalable path. His one exception matters: for code signing, soft-fail still adds cost, because the attacker does not otherwise need to be on the network path.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | threat analysis of soft-fail |
| Cryptography | `none` | no direct bearing |
| This project | `core` | its code-signing exception is close to our case |

- **R-O-02**: the argument applies to interactive TLS. Signed artifacts are checked offline and later, which is the exception's case, so R-O-02's preference needs its own reasoning for artifact statements and should not simply cite TLS.

## Implementations

Chrome's CRLSet is described. Not evaluated.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** whole.

- An argument, not a measurement.
- It is a browser engineer's view from 2014, before CT enforcement and before CRLite. The claim that a much larger list would be too much data was later tested by `larisch-2017-crlite`.
