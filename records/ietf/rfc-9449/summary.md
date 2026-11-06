---
schema: "library-summary/v1"
id: rfc-9449
record: rfc-9449
type: summary
updated: "2026-11-05"
---

# OAuth 2.0 Demonstrating Proof of Possession (DPoP)

|  |  |
|---|---|
| **Type** | rfc (IETF stream) |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9449.json` 2026-11-01 |
| **Authors** | D. Fett, B. Campbell, J. Bradley, T. Lodderstedt, M. Jones, D. Waite |
| **Published** | 2023-09 |
| **Identifier** | RFC 9449 · DOI 10.17487/RFC9449 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9449.txt |
| **Digest** | `sha256:3842c58e…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-05 |

## Overview

DPoP sender-constrains OAuth tokens at the application layer: the client signs a JWT proof in a `DPoP` header, and the token is bound to that key (§1). It exists because TLS-layer binding is unavailable or undesirable for some clients, notably browser apps (§1), and because audience restriction has proved cumbersome for many deployments (§2). The goal is to make a leaked token useless without the private key (§2). The RFC is careful about what it does not stop: XSS can use the key in place, and proofs can be pre-computed unless the server supplies a nonce (§2, §11.2, §11.4). The proof covers method and URI only, not body or headers, by design (§11.7).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Sender-constraining with stated limits |
| Cryptography | `adjacent` | Uses JWT signatures and a key thumbprint, adds no primitive |
| This project | `adjacent` | Pattern for proving a key at invocation |

- **DEC-003**: §6.1 binds a token through `cnf.jkt`, the base64url JWK SHA-256 Thumbprint (RFC 7638) of the public key. That is a key-digest identifier on the wire whose hash input is delegated to RFC 7638, which is not held and was not read.
- **Not R-M-02.** The key constrains who may present the token; it does not identify the principal, which is still whoever the authorization server says it is, so this RFC is not evidence for key-only principals.

## Implementations

**Checked 2026-11-01.** Confirmed through the GitHub API, and the README lists DPoP. No wider survey was done.

| Name | Kind | License | URL |
|---|---|---|---|
| oauth4webapi | open source, TypeScript; README lists DPoP | MIT | https://github.com/panva/oauth4webapi |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **Replay is limited, not prevented.** §11.1 uses short acceptance windows, with `jti` tracking that may not be feasible behind several servers.
- **No request integrity.** §11.7 states that this is an intentional design decision.
- **No client authentication** (§1).
- **It binds to one holder.** Nothing here covers a chain of holders. `draft-asor-wimse-agent-delegation-chain` applies it to the leaf only.
- **Relations.** This RFC cites `rfc-6750` and `rfc-7800`, so the earlier `see_also` edges to them are carried by `cites`.
- **Errata: 1 verified** (checked 2026-11-05). 7646 (editorial) corrects "authentication server" to "authorization server" in §4.2.
- **Read scope.** §1, §2, §6, §6.1 and all of §11 were read, plus the §4.2 sentence the erratum corrects. The proof syntax and checks in §4, nonces in §8 and §9 were not.
