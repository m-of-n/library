---
schema: "library-summary/v1"
id: rfc-7518
record: rfc-7518
type: summary
updated: "2026-10-03"
---

# JSON Web Algorithms (JWA)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard` — IETF Standards Track |
| **Authors** | M. Jones (Microsoft) |
| **Published** | 2015-05 |
| **Identifier** | RFC 7518 · DOI 10.17487/RFC7518 |
| **Source** | https://www.rfc-editor.org/rfc/rfc7518.txt |
| **Digest** | `sha256:9a9ae524b09ea700ad3f189bac115df95ba69af84b26ffdbe3cdfb8d2152b1fc` |

## Overview

The **algorithm half of JOSE** — the JSON counterpart to `rfc-9053`. It
registers the `alg` and `enc` values used by JWS (`rfc-7515`) and JWE
(`rfc-7516`), and defines the JWK key representations they consume.

Signature algorithms are named strings rather than integers: `HS256`
(Required), `RS256` (Recommended), `ES256` (Recommended+), and `EdDSA` added
later by RFC 8037. Content encryption covers `A128CBC-HS256` — the
encrypt-then-MAC composition of CBC (`sp-800-38a`) with HMAC, marked Required —
and `A128GCM`/`A192GCM`/`A256GCM` from `sp-800-38d`, marked Recommended.

Each registration carries an **implementation requirement** column
(Required / Recommended / Recommended+ / Optional). That column is the most
useful thing in the document and has no counterpart in COSE, where
`rfc-9053` leaves the equivalent judgement to a separate "Recommended" field
in the IANA registry.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The algorithm identifiers a JOSE verifier dispatches on |
| Cryptography | `adjacent` | Bindings and names, not primitives |
| This project | `adjacent` | JOSE is not our export target, but it is the design COSE reacted to |

Bears on no `DEC-*` directly. **DEC-005** is about the COSE side; this record
is held because the COSE decisions are only legible as *departures* from JOSE —
integer code points instead of strings, no pre-hash variants, a different key
model. Holding only `rfc-9053` would leave those departures looking arbitrary.

## Implementations

Searched **2026-10-03**. Mature and plural; JOSE is the better-deployed of the
two ecosystems by a wide margin.

| Name | Kind | License | URL |
|---|---|---|---|
| `jose` (panva) | open source | MIT | https://github.com/panva/jose |
| Authlib / python-jose | open source | BSD / MIT | https://authlib.org |
| `go-jose` | open source | Apache-2.0 | https://github.com/go-jose/go-jose |
| `nimbus-jose-jwt` | open source | Apache-2.0 | https://connect2id.com/products/nimbus-jose-jwt |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. Held for comparison with the COSE set; we do not intend to
conform to JOSE.

## Limits

- **`alg: "none"` is in this document.** §3.6 registers an unsecured JWS with
  no signature. It is the origin of a well-known class of verifier
  vulnerability — accepting a token whose `alg` the attacker chose. COSE has no
  equivalent, and that absence is a deliberate improvement worth recording
  explicitly rather than leaving as folklore.
- **Algorithm agility is attacker-controlled by default.** Because `alg` is
  carried in the header and names both the algorithm *and* its key type, a
  verifier that trusts the header rather than the key's own metadata can be
  steered — the RSA-public-key-as-HMAC-secret confusion. The document does not
  prohibit the pattern that enables it.
- **RSA PKCS#1 v1.5 (`RS256`) is Recommended and is the weakest construction
  here.** It is retained for compatibility; `PS256` (RSASSA-PSS) is the better
  choice and is merely Optional. Standing in the registry does not track
  cryptographic preference.
- **Names, not code points — and that costs bytes.** `"A128CBC-HS256"` is 13
  bytes of header on every message where COSE spends one. For a statement
  model that may carry many small signed objects, this is one of the concrete
  reasons the COSE side of the comparison wins.
- **It predates post-quantum entirely** (2015). The PQ extensions are
  `rfc-9964` for ML-DSA, `draft-ietf-cose-sphincs-plus` for SLH-DSA, and
  `draft-ietf-jose-pqc-kem` for ML-KEM — and all three are, despite the JOSE
  heritage of their names, now primarily COSE documents.
