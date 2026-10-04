---
schema: "library-summary/v1"
id: sp-800-38d
record: sp-800-38d
type: summary
updated: "2026-10-03"
---

# Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice` — a NIST Special Publication, not a FIPS |
| **Authors** | Morris Dworkin |
| **Published** | 2007-11 |
| **Identifier** | SP 800-38D · DOI 10.6028/NIST.SP.800-38D |
| **Source** | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf |
| **Digest** | `sha256:d99f3921ccebca049e7522426553aba071dae14ec3d5b6041e8c111a6cb57bba` |

## Overview

Defines **GCM**, authenticated encryption with associated data, and its
MAC-only specialisation **GMAC**. GCM composes CTR-mode encryption with a
GF(2¹²⁸) universal hash (GHASH) over the ciphertext and associated data,
producing a tag. It is parallelisable and streamable, which is why it became
the default AEAD of TLS 1.2/1.3 and why hardware acceleration for it is
ubiquitous.

In the formats this project cares about it appears as `A128GCM`, `A192GCM` and
`A256GCM` — COSE code points **1, 2, 3** (`rfc-9053` §4.1) and the identically
named JOSE algorithms (`rfc-7518` §5.3).

The document's centre of gravity is not the algorithm but **§8, the uniqueness
requirement on IVs**, which it states as a formal bound:

> The probability that the authenticated encryption function ever will be
> invoked with the same IV and the same key on two (or more) distinct sets of
> input data shall be no greater than 2⁻³².

and then, unusually bluntly for a NIST document:

> Across all instances of the authenticated encryption function with a given
> key, **if even one IV is ever repeated**, then the implementation may be
> vulnerable to the forgery attacks … **In practice, this requirement is almost
> as important as the secrecy of the key.**

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The default AEAD of the modern web, and the one with the sharpest misuse cliff |
| Cryptography | `core` | Normative for the mode |
| This project | `none` | We sign statements; we do not encrypt them |

**`bears_on` is empty, deliberately** — as for the rest of the symmetric set.
No ARCH-0001 requirement turns on an encryption mode.

Held so that `A128GCM` in both `rfc-9053` and `rfc-7518` resolves to a
specification, and so that the nonce constraint is on record in the library
rather than in someone's memory.

## Implementations

Searched **2026-10-03**. The best-supported AEAD in existence; hardware
acceleration (AES-NI + PCLMULQDQ, ARMv8 PMULL) is near-universal.

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL | open source | Apache-2.0 | https://openssl.org |
| BoringSSL | open source | ISC / OpenSSL | https://boringssl.googlesource.com |
| Go `crypto/cipher` `NewGCM` | open source | BSD-3-Clause | https://pkg.go.dev/crypto/cipher |
| RustCrypto `aes-gcm` | open source | MIT / Apache-2.0 | https://github.com/RustCrypto/AEADs |
| CAVP-validated HSMs | commercial | — | Thales, Entrust, AWS CloudHSM |

**We use a vetted library. We do not implement these** — and for GCM
specifically, we do not manage nonces by hand either.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. Reference data we cite, not requirements we discharge.

## Limits

- **A single repeated IV is catastrophic, not degraded.** This is the fact to
  carry away. Nonce reuse under GCM does not merely leak a plaintext
  relationship: it leaks the GHASH authentication subkey, which lets an
  attacker **forge arbitrary messages** under that key thereafter. Confidentiality
  loss is recoverable by rotating keys; forgery capability is not. NIST's own
  framing — "almost as important as the secrecy of the key" — is not
  rhetorical.
- **The 96-bit IV is the only safe default, and random IVs do not scale.** With
  a random 96-bit IV the 2⁻³² bound is reached around 2³² messages per key, so
  a long-lived key with randomly generated nonces will eventually violate the
  requirement. §8.2 gives a deterministic construction for this reason. An
  application that picks "random nonce" without a key-rotation policy has
  deferred a failure, not avoided one.
- **Neither COSE nor JOSE enforces any of this.** `A128GCM` is a code point.
  Nothing in `rfc-9053` or `rfc-7518` constrains how the sender derives its
  IV, so the entire security of the mode rests on a property the wire format
  cannot check and a verifier cannot detect.
- **Short tags are permitted and change the threat model.** Appendix C allows
  tags as short as 32 bits for specific applications, with conditions on the
  number of permitted failed verifications. The conditions are easy to adopt
  the tag length from and ignore.
- **GMAC is GCM with no plaintext, and is a MAC, not a signature.** It proves
  possession of a shared key. It cannot identify a principal, so nothing in a
  key-centric statement model can use it for attribution.
