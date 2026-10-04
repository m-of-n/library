---
schema: "library-summary/v1"
id: sp-800-38f
record: sp-800-38f
type: summary
updated: "2026-10-03"
---

# Recommendation for Block Cipher Modes of Operation: Methods for Key Wrapping

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice` — a NIST Special Publication, not a FIPS |
| **Authors** | Morris Dworkin |
| **Published** | 2012-12 |
| **Identifier** | SP 800-38F · DOI 10.6028/NIST.SP.800-38F |
| **Source** | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38f.pdf |
| **Digest** | `sha256:b8b1052755448e5ff3913ea09dc9b5ae47a97886752525a0cccfa024fb072fa8` |

## Overview

Specifies the approved methods for **key wrapping** — protecting the
confidentiality *and integrity* of cryptographic keys, as distinct from
protecting ordinary data. It defines two AES modes, **KW** (AES Key Wrap) and
**KWP** (Key Wrap With Padding), plus **TKW**, the Triple-DES analogue retained
for legacy use.

The document's own framing is the point: KW and KWP are **deterministic
authenticated-encryption modes**. Deterministic, because a key-wrapping
operation has no safe place to put a nonce and no reliable source of one —
which is exactly the constraint that makes GCM unsuitable for the job and this
document necessary.

#8 lists SP 800-38F as optional, to be ingested "if the JOSE/COSE key-wrap
path needs it". It does: `rfc-7518` registers `A128KW`/`A192KW`/`A256KW`, and
every composite algorithm in `draft-ietf-jose-pqc-kem` —
`ML-KEM-512+A128KW`, `ML-KEM-768+A192KW`, `ML-KEM-1024+A256KW` — wraps the
encapsulated secret with exactly this mode.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Key wrapping is its own problem with its own failure modes |
| Cryptography | `core` | Normative for KW/KWP |
| This project | `none` | We sign statements; we do not distribute keys |

**`bears_on` is empty, deliberately** — as for the rest of the symmetric set.
No ARCH-0001 requirement turns on key wrapping.

Held to complete the post-quantum COSE picture: `draft-ietf-jose-pqc-kem`'s
composites are half ML-KEM (`fips-203`) and half this document, and the
library previously held only the first half.

## Implementations

Searched **2026-10-03**. Well supported where JOSE/COSE key management is, and
absent from Go's standard library.

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL | open source | Apache-2.0 | https://openssl.org |
| BouncyCastle | open source | MIT | https://bouncycastle.org |
| RustCrypto `aes-kw` | open source | MIT / Apache-2.0 | https://github.com/RustCrypto/key-wraps |

**We use a vetted library. We do not implement these.**

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. Reference data we cite, not requirements we discharge.

## Limits

- **Deterministic means no nonce, and therefore no nonce-reuse cliff** — the
  opposite trade from `sp-800-38d`. Wrapping the same key twice under the same
  KEK yields identical ciphertext, which leaks *that fact* and nothing more.
  For key wrapping that is an acceptable leak; for messages it would not be,
  and KW must not be repurposed as a general AEAD.
- **It is slow by construction.** KW makes six passes over the data. That is
  deliberate — it buys security without a nonce — but it makes the mode a poor
  choice for anything but short key material.
- **TKW is Triple-DES and should be treated as dead.** It is specified here for
  legacy support; Triple-DES is disallowed for new use under current NIST
  transition guidance. Its presence in an approved document is not approval
  for new designs — the same trap as ECB in `sp-800-38a`.
- **KW's input must be a multiple of 8 bytes; KWP exists only to lift that.**
  Choosing between them is an encoding decision, not a security one, and
  neither `rfc-7518` nor the PQ KEM draft is explicit that `AxxxKW` means KW
  rather than KWP.
- **Key wrapping assumes the key-encryption key arrived safely.** This
  document protects a key in transit under another key; where *that* key comes
  from is `sp-800-56ar3`, `fips-203`, or something outside the standards
  entirely. It is one link, not a chain.
