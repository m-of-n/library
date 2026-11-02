---
schema: "library-summary/v1"
id: rfc-1422
record: rfc-1422
type: summary
updated: "2026-11-01"
---

# PEM Part II: Certificate-Based Key Management

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `historic`: rfc1422.json gives status Historic (published as Proposed Standard) |
| **Authors** | S. Kent |
| **Published** | 1993-02 |
| **Identifier** | RFC 1422 · DOI 10.17487/RFC1422 |
| **Source** | https://www.rfc-editor.org/rfc/rfc1422.txt |
| **Digest** | `sha256:89985ada…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | no errata link in RFC metadata, 2026-11-01 |

## Overview

RFC 1422 builds a key management infrastructure on the 1988 X.509 framework for Privacy Enhanced Mail, because X.509 alone leaves out policy and procedure. It sets a single root, the Internet Policy Registration Authority, with Policy Certification Authorities beneath it and CAs beneath them. Its naming rule is the part still worth reading: §3.4.2.2 levies a DN subordination requirement, so certificates from a CA are "syntactically constrained" to entities below it in the directory tree. Scope is therefore a property of the name, with no extension to omit or ignore. The cost was one global root and a directory-shaped namespace.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | a structural defence against the any-CA-any-name problem |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | a prior design that R-M-03 improves on |

- **R-M-03** (names relative to an issuing principal): RFC 1422 ties a name to an issuer by subordination, but inside one global hierarchy. Ours keeps the binding and drops the hierarchy.
- **R-M-01**: background for how PKIX moved scope into an optional extension.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** §1 and §3.4.2.2's closing rule and §3.4.2.4 by section. The rest of §3.4 and §3.5 onward were not read.

- The subordination rule has exceptions: cross-certificates and reverse certificates for applications other than PEM (§3.4.2.2).
- It does not explain why the design failed in deployment; nothing here is evidence of that.
- The IPRA root is exactly the global authority this project rejects, so this is a counterpoint and not a model.
