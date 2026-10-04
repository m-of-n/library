---
schema: "library-summary/v1"
id: sp-800-38a
record: sp-800-38a
type: summary
updated: "2026-10-03"
---

# Recommendation for Block Cipher Modes of Operation: Methods and Techniques

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice` — a NIST Special Publication, not a FIPS |
| **Authors** | Morris Dworkin |
| **Published** | 2001-12 |
| **Identifier** | SP 800-38A · DOI 10.6028/NIST.SP.800-38A |
| **Source** | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf |
| **Digest** | `sha256:66821162de1e7130c5fb5eedb22140d8d6d013ec51af4550bb095c2a9481a00e` |

## Overview

Defines the five classical **confidentiality** modes for a block cipher:
**ECB, CBC, CFB, OFB and CTR**. The word in the abstract that governs the whole
document is *confidentiality* — these modes hide content and do **not**
authenticate it.

This is the document that turns `fips-197` from a 128-bit permutation into
something that can process a message. It is held for one mode in particular:
**CBC**, which JOSE composes with HMAC in the `A128CBC-HS256` family
(`rfc-7518` §5.2). The other four are background.

CTR matters indirectly: it is the counter construction that `sp-800-38c` (CCM)
and `sp-800-38d` (GCM) both build their AEAD on.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Mode choice is where symmetric encryption is usually got wrong |
| Cryptography | `core` | Normative for the modes |
| This project | `none` | We sign statements; we do not encrypt them |

**`bears_on` is empty, deliberately** — the same judgement as `fips-197`. No
requirement in ARCH-0001 turns on a confidentiality mode.

Held so that JOSE's `A128CBC-HS256` resolves to a specification rather than a
name.

## Implementations

Searched **2026-10-03**. Universal, and in several libraries the raw modes are
now deliberately awkward to reach — a deprecation signal in itself.

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL | open source | Apache-2.0 | https://openssl.org |
| RustCrypto `block-modes` | open source | MIT / Apache-2.0 | https://github.com/RustCrypto/block-modes |
| Go `crypto/cipher` | open source | BSD-3-Clause | https://pkg.go.dev/crypto/cipher |

**We use a vetted library. We do not implement these.**

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. Reference data we cite, not requirements we discharge.

## Limits

- **Not one of these modes authenticates anything.** All five provide
  confidentiality only. A ciphertext under CBC can be modified by an attacker
  in structured, predictable ways. This is why JOSE pairs CBC with HMAC and why
  the AEAD modes exist at all — and it is the single most common
  misunderstanding about this document.
- **ECB is specified and should essentially never be used.** NIST includes it
  for completeness; identical plaintext blocks produce identical ciphertext
  blocks, so it leaks structure directly. Its presence in an approved NIST
  document is not an endorsement of its use.
- **CBC's IV must be unpredictable, not merely unique** — a stronger and more
  easily violated condition than GCM's uniqueness requirement, and a different
  one. A predictable IV with CBC is exploitable. The document states the
  requirement; it does not say how to meet it.
- **The document predates authenticated encryption as standard practice** and
  reflects a 2001 view. It has never been revised. Read it with `sp-800-38c`
  and `sp-800-38d`, which exist precisely because confidentiality alone turned
  out not to be what applications needed.
- **CBC + HMAC composition is not specified here.** JOSE's `A128CBC-HS256` is
  an encrypt-then-MAC composition defined in `rfc-7518` §5.2, not in this
  document. SP 800-38A tells you nothing about whether that composition is
  sound; it only defines the CBC half.
