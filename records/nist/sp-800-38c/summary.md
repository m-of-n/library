---
schema: "library-summary/v1"
id: sp-800-38c
record: sp-800-38c
type: summary
updated: "2026-10-03"
---

# Recommendation for Block Cipher Modes of Operation: The CCM Mode for Authentication and Confidentiality

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice` — a NIST Special Publication, not a FIPS |
| **Authors** | Morris Dworkin |
| **Published** | 2004-05 |
| **Identifier** | SP 800-38C · DOI 10.6028/NIST.SP.800-38C |
| **Source** | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38c.pdf |
| **Digest** | `sha256:16ec6f99424192757b5b9928a7dcf41817be3aaf85d48366740dfdf7c16db250` |

## Overview

Defines **CCM** — Counter with CBC-MAC — an authenticated-encryption mode that
provides *both* confidentiality and authenticity by composing two mechanisms
from `sp-800-38a`: **CTR** mode for encryption and **CBC-MAC** for
authentication. It is a generic composition, standardised.

CCM is the quietly dominant algorithm family in COSE. `rfc-9053` §4.2
registers **eight** AES-CCM code points (values 10–13 and 30–33), varying the
nonce length (13 or 7 bytes), the tag length (64 or 128 bits) and the key size
(128 or 256). That is more code points than any other algorithm in the COSE
initial set — a consequence of CCM's parameterisation being exposed directly in
the registry rather than fixed.

Its constituency is constrained environments: CCM needs no additional
primitive beyond the block cipher itself, which is why it is standard in
IEEE 802.11 and Bluetooth and why COSE — a format designed for small messages
— carries so many variants.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | An AEAD mode; authenticity as well as confidentiality |
| Cryptography | `core` | Normative for the mode |
| This project | `none` | We sign statements; we do not encrypt them |

**`bears_on` is empty, deliberately** — as for the rest of the symmetric set.

Held so the eight `AES-CCM-*` entries in `rfc-9053` resolve to a
specification.

## Implementations

Searched **2026-10-03**. Present wherever constrained-device protocols are, and
notably thinner in general-purpose web stacks than GCM.

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL | open source | Apache-2.0 | https://openssl.org |
| mbedTLS | open source | Apache-2.0 | https://github.com/Mbed-TLS/mbedtls |
| RustCrypto `ccm` | open source | MIT / Apache-2.0 | https://github.com/RustCrypto/AEADs |

Notably **absent**: Go's standard library has no CCM. **We use a vetted
library. We do not implement these.**

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. Reference data we cite, not requirements we discharge.

## Limits

- **The nonce must never repeat under a given key**, and CCM's failure on
  repeat is as bad as GCM's. The constraint is the same class of operational
  hazard documented at length in `sp-800-38d` §8 — but SP 800-38C treats it far
  more briefly, which makes the danger *less* visible here, not smaller.
- **Short nonces force short message lifetimes.** CCM trades nonce length
  against maximum payload length: the 7-byte-nonce COSE variants
  (`AES-CCM-64-*`) buy a longer permitted message at the cost of a much smaller
  nonce space, and a 7-byte nonce is well inside birthday range for a
  high-volume sender. The COSE registry exposes this trade as a code-point
  choice with no guidance attached.
- **64-bit tags are approved and are weak for most uses.** Four of the eight
  COSE variants use a 64-bit tag, giving an attacker a 2⁻⁶⁴ forgery probability
  per attempt. Approved is not the same as advisable; the choice belongs to the
  application and COSE does not make it.
- **It is two-pass and cannot stream.** CCM must know the message length before
  it starts, because the length is encoded into the first block. For a signing
  or attestation pipeline that would prefer to process incrementally, this is a
  structural limitation GCM does not share.
- **It is a generic composition, with that composition's caveats.** CCM is
  CTR + CBC-MAC, and its security proof depends on the exact encoding of the
  formatting function. Implementers who "simplify" the formatting break it;
  the document's Appendix A exists for that reason.
