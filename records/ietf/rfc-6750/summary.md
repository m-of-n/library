---
schema: "library-summary/v1"
id: rfc-6750
record: rfc-6750
type: summary
updated: "2026-11-01"
---

# The OAuth 2.0 Authorization Framework: Bearer Token Usage

|  |  |
|---|---|
| **Type** | rfc (IETF stream) |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc6750.json` 2026-11-01 |
| **Authors** | M. Jones, D. Hardt |
| **Published** | 2012-10 |
| **Identifier** | RFC 6750 · DOI 10.17487/RFC6750 |
| **Source** | https://www.rfc-editor.org/rfc/rfc6750.txt |
| **Digest** | `sha256:9dc385cf…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This RFC specifies use of bearer tokens with OAuth. Its definition is the point: any party in possession of a bearer token can use it the way any other possessor can, with no proof of possession of key material (§1.2). The security text follows from that. §5.3 makes safeguarding the token the primary consideration, and recommends TLS, short lifetimes of an hour or less, audience restriction, and keeping tokens out of URLs. Every recommendation limits the damage of a stolen token, because the token cannot limit it itself.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines the bearer threat model |
| Cryptography | `none` | No cryptography beyond TLS |
| This project | `adjacent` | The opposite of a key-named principal |

- **R-M-02**: the contrast case. A bearer token authorizes whoever holds it, so no key names the principal.
- **R-O-02**: §5.3 is an early standards statement of preferring short-lived tokens.

## Implementations

**Checked 2026-11-01.** Confirmed through the GitHub API, and the README names this RFC. No wider survey was done.

| Name | Kind | License | URL |
|---|---|---|---|
| Authlib | open source, Python; README lists RFC 6750 | BSD-3-Clause | https://github.com/authlib/authlib |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **It says nothing about delegation.** Whoever passes a bearer token passes all of it.
- **Audience restriction is only a SHOULD.** `rfc-9449` §2 reports that it has been cumbersome in practice.
- **Errata not read.** The search lists 4 entries.
- **Read scope.** §1.2, §5.1 and §5.3 were read. The token transmission methods in §2 and the error scheme in §3 were not.
