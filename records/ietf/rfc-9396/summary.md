---
schema: "library-summary/v1"
id: rfc-9396
record: rfc-9396
type: summary
updated: "2026-11-01"
---

# OAuth 2.0 Rich Authorization Requests

|  |  |
|---|---|
| **Type** | rfc (IETF stream) |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9396.json` 2026-11-01 |
| **Authors** | T. Lodderstedt, J. Richer, B. Campbell |
| **Published** | 2023-05 |
| **Identifier** | RFC 9396 · DOI 10.17487/RFC9396 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9396.txt |
| **Digest** | `sha256:d6a8f032…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Scope strings suit coarse requests but not requests such as a specific transfer to a specific merchant, so this RFC adds `authorization_details`, a JSON array of typed objects (§1). The important text is §6.1: the fields' meaning is API-specific, so the RFC says there is no standardized mechanism to compare two arbitrary requests, and warns against simple object comparison. Instead each type's designer defines comparison, and the examples show that a value may or may not subsume another depending on the API. It gives RAR expressiveness at the cost of any general narrowing rule, and both delegation drafts must add that rule back for their own type.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Fine-grained grants with a stated comparison problem |
| Cryptography | `none` | No cryptography |
| This project | `core` | Direct evidence on what a tag language must define |

- **DEC-004, R-M-08**: §6.1 shows what happens without a defined comparison: the semantics move to each API, and a general verifier cannot decide narrowing. It is an argument for R-M-08 as written.
- **R-M-12**: §2.1 lets the authorization server control the meaning of `type`, and recommends a collision-resistant namespace, such as a URI, for types used across servers. That is issuer-relative meaning, solved with DNS instead of keys.

## Implementations

**Not searched separately.** No library was checked for RAR support. `draft-niyikiza-oauth-attenuating-agent-tokens` and `draft-asor-wimse-agent-delegation-chain` profile the format.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **It does not address delegation between holders.** §6.1 is about an authorization server comparing requests, for example on refresh.
- **The AS and RS are expected to share semantics** (§1, §9). Nothing lets a third party evaluate an object it does not understand.
- **Tampering needs other specs.** §12 points to signed request objects when integrity matters.
- **No errata found** on 2026-11-01.
- **Read scope.** §1, §2.1, §6.1, §9 and §12 were read. The request and response flows, §7 enrichment, metadata and §11 were not.
