---
schema: "library-summary/v1"
id: ptacek-2024-macaroons
record: ptacek-2024-macaroons
type: summary
updated: "2026-11-05"
---

# Macaroons Escalated Quickly

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | `implementation`: a vendor account of its own system |
| **Authors** | Thomas Ptacek |
| **Published** | 2024-01-31 |
| **Identifier** | none |
| **Source** | https://fly.io/blog/macaroons-escalated-quickly/ |
| **Digest** | `sha256:73b14eaf…` (full value in `record.yaml`), fetched 2026-11-01. A re-fetch on 2026-11-05 hashes differently; see `content.note` |

## Overview

Fly.io replaced its OAuth2 tokens with macaroons, and this post says what that took. The stated win is not theft resistance but permissions: users derive their own restricted tokens, and the platform never has to design the roles in advance (§3). Caveat evaluation keeps the rule that every caveat must pass in isolation, so adding one can only narrow (§1). The hard part is HMAC itself. Since "If you can verify a Macaroon, you can generate one", verification moved to an isolated service reached over HTTP, and clearing of caveats can happen anywhere (§6). Third-party caveats, nearly dropped, became the login and SSO mechanism and a plugin interface (§5).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Field evidence on token design and operations |
| Cryptography | `adjacent` | Uses HMAC-SHA256 and Chapoly, and describes no new construction |
| This project | `adjacent` | Evidence for what a caveat model costs to run |

- **DEC-004**: the author reports that purely restrictive caveats are awkward for some roles (§8). This is one of the few statements from practice about the expressive limit of a narrowing-only language, and it applies to tag intersection too. §6 also rejects untyped opaque caveat blobs, which bears on DEC-004's opaque-tag starting profile.
- **R-O-02**: revocation is by nonce, with a list and cache invalidation, and is described as rare enough for that to be fine (§7). That is one data point for preferring short life and keeping revocation available.

## Implementations

**Checked 2026-11-01.** The post says the code is public, and the repository was confirmed through the GitHub API.

| Name | Kind | License | URL |
|---|---|---|---|
| superfly/macaroon | open source, Go; Fly.io implementation | Apache-2.0 | https://github.com/superfly/macaroon |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**Relation.** The post links the NDSS paper, so `macaroons-2014` is under `cites`, not `see_also`.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `web` record owes FX-1 only if someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **One vendor, on its own work, in a casual register.** Nothing is measured, and the author says the downsides are mostly left out (§8).
- **The narrowing rule has an escape hatch.** The verifier service turns a user token into a service token with the authentication caveat and expiry stripped off (§6). That is sound only because the service holds the key. It shows that monotonic narrowing in practice applies to holders, not to the issuer.
- **It says little on who can verify.** The central verifier fits one platform. It is not an answer for parties that do not share an operator.
- **Read scope.** The whole post was read. The post's section numbers are used as locators. The linked technical documentation and code were not read.
