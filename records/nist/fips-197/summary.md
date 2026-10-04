---
schema: "library-summary/v1"
id: fips-197
record: fips-197
type: summary
updated: "2026-10-03"
---

# Advanced Encryption Standard (AES)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — a US Federal Information Processing Standard |
| **Authors** | NIST |
| **Published** | 2001-11-26; **updated 2023-05-09** (FIPS 197-upd1) |
| **Identifier** | FIPS 197 · DOI 10.6028/NIST.FIPS.197-upd1 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf |
| **Digest** | `sha256:62c86eb567f13edb8f71826e985da870b04ef6381634f303cdb16e84d47becd1` |

## Overview

Specifies **AES**, three members of the Rijndael block cipher family selected
in the 2000 AES competition: **AES-128, AES-192 and AES-256**. All three
transform data in **128-bit blocks**; the suffix is the key length, not the
block length — a distinction the document is careful about and most summaries
blur.

It is a block cipher and nothing more. It encrypts one 128-bit block under one
key. Everything that makes AES usable on a real message — chaining, nonces,
authentication, associated data — lives in the SP 800-38 series, not here.

The record exists because `rfc-9053` assigns COSE code points for AES-GCM and
eight AES-CCM variants, and `rfc-7518` does the same for JOSE, while the
library held nothing that said what AES actually is.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The symmetric primitive essentially all of COSE/JOSE encryption rests on |
| Cryptography | `core` | Normative for the primitive |
| This project | `none` | A key-centric *statement* model signs; it does not encrypt |

**`bears_on` is empty, deliberately.** Our model is about who says what about
which artifact. AES provides confidentiality; it makes no assertion, carries no
subject, and produces nothing a verifier re-checks. There is no requirement in
ARCH-0001 it discharges, and inventing one to justify the record would be worse
than holding it honestly as background — the same judgement recorded for
`fips-203`.

It is held so the COSE/JOSE algorithm tables resolve to something.

## Implementations

Searched **2026-10-03**. Universal; AES is hardware-accelerated on every
current server and mobile CPU (AES-NI, ARMv8 Crypto Extensions).

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL | open source | Apache-2.0 | https://openssl.org |
| BoringSSL | open source | ISC / OpenSSL | https://boringssl.googlesource.com |
| RustCrypto `aes` | open source | MIT / Apache-2.0 | https://github.com/RustCrypto/block-ciphers |
| Go `crypto/aes` | open source | BSD-3-Clause | https://pkg.go.dev/crypto/aes |
| CAVP-validated HSMs | commercial | — | Thales, Entrust, AWS CloudHSM |

**We use a vetted library. We do not implement these.** A software AES without
constant-time discipline is a cache-timing oracle.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. We cite AES; we do not conform to it directly.

## Limits

- **A block cipher is not encryption.** AES alone encrypts exactly 128 bits.
  Using it without a mode is ECB by another name, and ECB does not hide
  structure. Every security property anyone actually wants comes from
  `sp-800-38a`, `sp-800-38c` or `sp-800-38d` — the mode, not the cipher.
- **It provides no authentication whatsoever.** Authenticity in COSE's
  `A128GCM` and `AES-CCM-*` comes from GCM and CCM, not from AES.
- **"Updated 2023" is editorial, not cryptographic.** FIPS 197-upd1 reorganised
  and corrected the presentation; the algorithm is byte-for-byte the one
  standardised in 2001. A conformance claim against "FIPS 197" is not
  version-sensitive the way one against FIPS 186 would be.
- **Key length is not the weak point, and treating it as the dial is a
  mistake.** AES-128 remains unbroken; the realistic failure modes are mode
  misuse, nonce reuse and side channels. Choosing AES-256 does not address any
  of them.
- **Quantum relevance is modest and often overstated.** Grover's algorithm
  gives at most a square-root speedup, so AES-256 retains a large margin and
  AES-128 a reduced one. Unlike the signature standards in this lane, AES is
  not the part of the stack that post-quantum migration is about.
