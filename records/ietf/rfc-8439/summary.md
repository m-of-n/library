---
schema: "library-summary/v1"
id: rfc-8439
record: rfc-8439
type: summary
updated: "2026-10-03"
---

# ChaCha20 and Poly1305 for IETF Protocols

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `informational` — **IRTF**, not IETF Standards Track |
| **Authors** | Y. Nir (Dell EMC), A. Langley (Google) |
| **Published** | 2018-06 · obsoletes RFC 7539 |
| **Identifier** | RFC 8439 · DOI 10.17487/RFC8439 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8439.txt |
| **Digest** | `sha256:25bef70fbf7a07ff45c2fe4cb7c6ce954eac687413d8610603268b4e4415324c` |

## Overview

Specifies the **ChaCha20** stream cipher, the **Poly1305** one-time
authenticator, and the **AEAD_CHACHA20_POLY1305** construction that composes
them. It is the non-AES AEAD of the modern internet: TLS 1.3's alternative
cipher suite, and **COSE algorithm 24** in `rfc-9053` §4.3.

Its reason for existing is performance without hardware support. AES is fast
when AES-NI is present and markedly slower when it is not; ChaCha20 is a pure
ARX design that runs at consistent speed in software on anything, and is
naturally constant-time. The whole point is a credible AEAD for platforms AES
does not serve well.

The library holds it so COSE alg 24 resolves to a specification, completing
the symmetric set alongside `sp-800-38c` and `sp-800-38d`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | One of the two AEADs the web actually runs on |
| Cryptography | `core` | Normative for the primitive and the composition |
| This project | `none` | We sign statements; we do not encrypt them |

**`bears_on` is empty, deliberately** — as for the rest of the symmetric set.
No ARCH-0001 requirement turns on an AEAD.

## Implementations

Searched **2026-10-03**. Excellent coverage, and notably better than AES-CCM's
in general-purpose language runtimes.

| Name | Kind | License | URL |
|---|---|---|---|
| libsodium | open source | ISC | https://libsodium.org |
| OpenSSL | open source | Apache-2.0 | https://openssl.org |
| Go `x/crypto/chacha20poly1305` | open source | BSD-3-Clause | https://pkg.go.dev/golang.org/x/crypto/chacha20poly1305 |
| RustCrypto `chacha20poly1305` | open source | MIT / Apache-2.0 | https://github.com/RustCrypto/AEADs |

**We use a vetted library. We do not implement these.**

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. Reference data we cite, not requirements we discharge.

## Limits

- **It is IRTF Informational, and it is load-bearing anyway.** This is the
  cleanest instance in the library of the trap `library/CLAUDE.md` names:
  *an RFC being an RFC does not make it a standard*. RFC 8439 is a product of
  the **IRTF CFRG**, published for information — yet TLS 1.3 and COSE both
  depend on it. `maturity: informational` here is the document's own
  classification, not a judgement about its quality, and the gap between its
  standing and its deployment is the thing worth remembering.
- **Nonce reuse is catastrophic, as with GCM, and for a sharper reason.**
  ChaCha20 is a stream cipher: reusing a nonce under one key XORs two
  plaintexts together *and* compromises the Poly1305 one-time key, enabling
  forgery. There is no partial failure mode.
- **The nonce is 96 bits with no built-in counter discipline.** The RFC gives a
  32-bit block counter and a 96-bit nonce but does not mandate how a sender
  derives nonces, so the same scaling problem as GCM applies — and again,
  nothing in COSE constrains it.
- **Poly1305 is a one-time authenticator, not a MAC.** Its key must never be
  reused across messages. The AEAD construction handles this by deriving a
  fresh Poly1305 key per message from ChaCha20; anyone using Poly1305 directly
  must replicate that, and the failure is silent.
- **It obsoletes RFC 7539, held here as a stub.** The change was editorial and
  clarifying rather than cryptographic, but citations to 7539 remain common in
  older material and should be retargeted.
