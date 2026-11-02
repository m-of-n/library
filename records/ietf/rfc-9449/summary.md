---
schema: "library-summary/v1"
id: rfc-9449
record: rfc-9449
type: summary
updated: "2026-11-01"
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
| **Digest** | `sha256:3842c58e…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

DPoP sender-constrains OAuth tokens at the application layer: the client signs a JWT proof in a `DPoP` header, and the token is bound to that key (§1). It exists because TLS-layer binding is unavailable to many clients, notably browser apps (§1), and because audience restriction has proved cumbersome for many deployments (§2). The goal is to make a leaked token useless without the private key (§2). The RFC is careful about what it does not stop: XSS can use the key in place, and proofs can be pre-computed unless the server supplies a nonce (§2, §11.4). The proof covers method and URI only, not body or headers, by design (§11.7).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Sender-constraining with stated limits |
| Cryptography | `adjacent` | Uses JWT signatures and a key thumbprint, adds no primitive |
| This project | `adjacent` | Pattern for proving a key at invocation |

- **DEC-003**: §6 binds a token through a hash of the public key, which is a key-digest subject identifier on the wire.
- **R-M-02**: possession of the key, not of the token, becomes what authorizes use. The principal is still whoever the authorization server says it is.

## Implementations

**Checked 2026-11-01.** Confirmed through the GitHub API, and the README lists DPoP. No wider survey was done.

| Name | Kind | License | URL |
|---|---|---|---|
| oauth4webapi | open source, JavaScript; README lists DPoP | MIT | https://github.com/panva/oauth4webapi |

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
- **Errata not read.** The search lists 1 entry.
- **Read scope.** §1, §2, §6, §11.1, §11.4 and §11.7 were read. The proof syntax and checks in §4, nonces in §8 and §9 and the remaining §11 subsections were not.
