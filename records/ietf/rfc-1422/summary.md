---
schema: "library-summary/v1"
id: rfc-1422
record: rfc-1422
type: summary
updated: "2026-11-04"
---

# Privacy Enhancement for Internet Electronic Mail: Part II: Certificate-Based Key Management

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `historic`: rfc1422.json gives status Historic (published as Proposed Standard) |
| **Authors** | S. Kent |
| **Published** | 1993-02 |
| **Identifier** | RFC 1422 · DOI 10.17487/RFC1422 |
| **Source** | https://www.rfc-editor.org/rfc/rfc1422.txt |
| **Digest** | `sha256:89985ada…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |
| **Errata** | none: `errata_url` is null in rfc1422.json, checked 2026-11-04 |

## Overview

RFC 1422 builds a key management infrastructure on the 1988 X.509 framework for Privacy Enhanced Mail, because X.509 alone leaves out policy and procedure (§1). It sets a single root, the Internet Policy Registration Authority, with Policy Certification Authorities beneath it and CAs beneath them. Its naming rule is the part still worth reading: §3.4.2.2 levies a DN subordination requirement, so certificates from a CA are "syntactically constrained" to entities below it in the directory tree, and §3.4.2.4 says the subjects of PEM certificates "must have DNs subordinate to that of the issuing CA". Scope is therefore a property of the name, with no extension to omit or ignore; that framing is ours. The cost was one global root and a directory-shaped namespace.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | a structural defence against the any-CA-any-name problem |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | a prior design that R-M-03 improves on |

- **R-M-03** (names SHALL be interpreted only relative to an issuing principal): RFC 1422 ties a name to an issuer by subordination, but inside one global hierarchy. Ours keeps the binding and drops the hierarchy.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

No `see_also` edges. X.509 (1988) is reference [2], under `cites` as `itu-x509-1988`. `rfc-3280` cites this RFC, and `rfc-5280` authors its own edge here; neither is repeated.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** §1, §3.4.2.2's closing rule and §3.4.2.4, by section, and the reference list. The rest of §3.4 and §3.5 onward were not read. Quotes re-checked against the text 2026-11-04.

- §3.4.2.2 states the rule softly: CAs "are expected to" sign only subordinate DNs, with exceptions for cross-certificates and reverse certificates used with applications other than PEM.
- It does not explain why the design failed in deployment; nothing here is evidence of that.
- The IPRA root is exactly the global authority this project rejects, so this is a counterpoint and not a model.
