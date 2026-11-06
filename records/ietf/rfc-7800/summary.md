---
schema: "library-summary/v1"
id: rfc-7800
record: rfc-7800
type: summary
updated: "2026-11-05"
---

# Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs)

|  |  |
|---|---|
| **Type** | rfc (IETF stream) |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc7800.json` 2026-11-01 |
| **Authors** | M. Jones, J. Bradley, H. Tschofenig |
| **Published** | 2016-04 |
| **Identifier** | RFC 7800 · DOI 10.17487/RFC7800 |
| **Source** | https://www.rfc-editor.org/rfc/rfc7800.txt |
| **Digest** | `sha256:051514a7…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-05 |

## Overview

The issuer of a JWT declares, with a `cnf` claim, that the presenter possesses a particular key, and that a recipient can cryptographically confirm it (§3). The key can be given as a public JWK, an encrypted symmetric key, a key ID or a URL (§3.2 to §3.5, registered as `jwk`, `jwe`, `kid` and `jku` in §6.2.2). The RFC only carries the declaration. How possession is actually demonstrated is left to the application (§3). So it moves a token from bearer use toward holder-of-key use, while leaving the proof to something like `rfc-9449`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The standard holder-of-key slot in a JWT |
| Cryptography | `adjacent` | Carries key material, defines no algorithm |
| This project | `adjacent` | A JWT projection of a key-named subject |

- **DEC-003**: `cnf` is one existing wire answer to naming a subject by key, in four forms.
- **Not R-M-02.** §3 identifies the presenter by `sub` or `iss`, one of which MUST be present, and `cnf` only declares the key that presenter holds. The key confirms a principal named some other way, so this RFC is not evidence for key-only principals.

## Implementations

**Not searched separately.** No library was checked for this RFC. `panva/jose` was checked and its README does not name it, which says nothing about support.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **No proof protocol.** §3 calls the means of confirming possession application specific.
- **Replay is flagged, not solved.** §4 says proof by encrypted symmetric secret is open to replay without a nonce or similar.
- **`cnf` does not tell you who the key belongs to.** It is an assertion by the issuer.
- **Errata: 1 verified** (checked 2026-11-05). 6187 (editorial) corrects the DOI of the [JWK] reference in §7.1.
- **Relations.** `rfc-9449` cites this RFC, so no `see_also` edge is needed.
- **Read scope.** Abstract, §3, §3.1, §3.2, §4 and §6 were read. §3.3 to §3.6 and §5 were not, apart from headings.
