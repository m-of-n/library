---
schema: "library-summary/v1"
id: langley-2014-revchecking
record: langley-2014-revchecking
type: summary
updated: "2026-11-04"
---

# No, don't enable revocation checking

|  |  |
|---|---|
| **Type** | web (blog post) |
| **Maturity** | unset: personal blog by a Chrome engineer, no standing to verify |
| **Authors** | Adam Langley |
| **Published** | 2014-04-19 |
| **Identifier** | ImperialViolet, 2014-04-19 |
| **Source** | https://www.imperialviolet.org/2014/04/19/revchecking.html |
| **Digest** | `sha256:564bc67b…` (full value in `record.yaml`), fetched 2026-11-01, re-checked 2026-11-04 |

## Overview

Everyone soft-fails: networks are noisy, captive portals block OCSP, and hard-fail would make OCSP services a single point of failure and a DDoS target. So an attacker who can intercept traffic can block the check, and in the DNS-hijack case they can staple a stored pre-revocation response or get new certificates issued. Langley calls online checking useless and points to the marks of security theater, and explains CRLSets as pushed daily lists of some high-value revocations. He names short-lived certificates or something like OCSP Must Staple as the scalable path. His one exception matters: for code signing, soft-fail still adds cost, because the attacker otherwise needs only to be able to email you, not to intercept OCSP checks.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | threat analysis of soft-fail |
| Cryptography | `none` | no direct bearing |
| This project | `core` | its code-signing exception is close to our case |

- **R-O-02**: the argument is made for interactive TLS. A signed artifact delivered by a channel the attacker does not control is the exception's case, where an online check does raise attacker cost, so R-O-02's preference needs its own reasoning for artifact statements and should not simply cite TLS.

## Relations

- `see_also: langley-2011-revocation`: the same author's earlier post, which tested browsers and first proposed days-long certificates; this one adds the threat cases and the code-signing exception.
- `see_also: rfc-7633`: the TLS Feature extension behind OCSP Must-Staple, which the post names as one scalable path.

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
- It is a browser engineer's view from 2014, before CT enforcement and before CRLite. Its remark that a system for far more revocations would mean about two orders of magnitude more data was later addressed by `larisch-2017-crlite` (that record carries the edge).
