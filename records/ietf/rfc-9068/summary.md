---
schema: "library-summary/v1"
id: rfc-9068
record: rfc-9068
type: summary
updated: "2026-11-05"
---

# JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens

|  |  |
|---|---|
| **Type** | rfc (IETF stream) |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9068.json` 2026-11-01 |
| **Authors** | V. Bertocci |
| **Published** | 2021-10 |
| **Identifier** | RFC 9068 · DOI 10.17487/RFC9068 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9068.txt |
| **Digest** | `sha256:68d3ff39…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-05 |

## Overview

Many OAuth deployments already used JWT access tokens with similar layouts, and this profile standardizes them (§1). Tokens must be signed, `none` is forbidden, and `typ` must carry the `application/at+jwt` media type, which should be written `at+jwt` (§2.1). The reason is confusion: without explicit typing, an OpenID Connect ID Token could pass as an access token (§2.1, §5). §4 gives the resource server a validation list covering `typ`, `iss`, `aud`, signature and `exp`. Authorization content stays issuer-asserted: §4 says authorization claims should be used with other context, and leaves how to the implementation.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Validation rules and cross-JWT confusion handling |
| Cryptography | `adjacent` | Signature requirements, RS256 mandatory to implement |
| This project | `adjacent` | Precedent, not a building block |

- **R-O-05** (proposed, ARCH-0001-PROPOSAL v0.2.0): the `typ` check in §4 is a working instance of an authenticated type indicator, carried in the protected header.

## Implementations

**Checked 2026-11-01.** Confirmed through the GitHub API, and the README names this RFC. No wider survey was done.

| Name | Kind | License | URL |
|---|---|---|---|
| Authlib | open source, Python; README lists RFC 9068 | BSD-3-Clause | https://github.com/authlib/authlib |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **No delegation.** A single issuer signs each token. There is no chain and no holder derivation, which is why `draft-asor-wimse-agent-delegation-chain` adds both.
- **Any published key can sign.** §5 warns that a resource server has to accept signatures from any key in the issuer's metadata, so compromise of any one is enough.
- **Authorization checks are out of scope** (§4).
- **Errata: none verified** (checked 2026-11-05). The one entry, 8802, asked to make `iss` optional in §2.2 and was rejected.
- **Relations.** No `see_also`. The earlier edge to `rfc-9396` had no stated reason, and neither RFC cites the other; `draft-asor-wimse-agent-delegation-chain` cites both.
- **Read scope.** §1 (in part), §2.1, §4 and §5 were read. The claim definitions in §2.2, §3 and §6 were not, apart from headings.
