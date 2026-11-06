---
schema: "library-summary/v1"
id: rfc-7539
record: rfc-7539
type: summary
updated: "2026-11-03"
---

# ChaCha20 and Poly1305 for IETF Protocols

|  |  |
|---|---|
| **Type** | rfc (IRTF stream, CFRG; from `draft-irtf-cfrg-chacha20-poly1305-10`) |
| **Maturity** | `informational`: "Category: Informational" on the title page, and `pub_status` INFORMATIONAL in the RFC Editor metadata, checked 2026-11-03. IRTF documents are *"not a candidate for any level of Internet Standard"* (Status of This Memo) |
| **Authors** | Y. Nir (Check Point), A. Langley (Google) |
| **Published** | 2015-05 |
| **Identifier** | RFC 7539 · DOI 10.17487/RFC7539 · **Obsoleted by RFC 8439** |
| **Source** | https://www.rfc-editor.org/rfc/rfc7539.txt |
| **Digest** | `sha256:546e1220…` (full value in `record.yaml`), fetched 2026-11-03 |
| **Errata** | 4 Verified, 3 Held for Document Update, 1 Rejected, checked 2026-11-03. All merged into RFC 8439 |

## Overview

RFC 7539 is a stable reference and implementation guide for three of D. J. Bernstein's designs, and it says it *"does not introduce any new crypto"* (Abstract). The three are the ChaCha20 stream cipher (§2.1–§2.4), the Poly1305 one-time authenticator (§2.5), and their AEAD composition **AEAD_CHACHA20_POLY1305** (§2.8). The AEAD derives a one-time Poly1305 key from the first ChaCha20 block (§2.6) and encrypts from counter 1. It MACs AAD ‖ pad ‖ ciphertext ‖ pad ‖ two 64-bit little-endian lengths. It takes a 256-bit key and a 96-bit nonce, and yields a 128-bit tag. The case made for it (§1) is a standby cipher in case AES falls, plus speed and timing-attack resistance on hardware without AES instructions. The security section rests everything on **nonce uniqueness** (§4): a repeated nonce reveals the XOR of the plaintexts. Tag comparison must be constant-time. §2.7 declines to define a PRF, because Poly1305 is unsuitable for one. IANA assigned AEAD registry id 29 (§5). Test vectors fill §2 and Appendix A.

`rfc-8439` (June 2018) obsoletes it. 8439's abstract says it *"merges the errata filed against RFC 7539 and adds a little text to the Security Considerations section"*. **Cite `rfc-8439`, not this.**

## What it contributes to "which attestation systems have a stated post-quantum path?"

**Little, and nothing it says itself.** The word "quantum" does not occur. This is a symmetric construction, so `shor-1997` does not apply to it. The generic quantum speed-up against symmetric keys (Grover) is not held in this library, and the RFC does not discuss it. §4 claims only that ChaCha20 *"is designed to provide 256-bit security"*. The post-quantum exposure of a system using this AEAD sits in its **key establishment**, not here. In the parent project's prototype, that is the X25519 KEM of `HPKE_Curve25519_ChaCha20Poly1305` (`research/0003-cipher-suite` §7). For the topic answer, ChaCha20-Poly1305 belongs in the "no migration needed for the primitive" column. Any gap is in whatever delivers its key.

## Source defects: the errata, and one internal contradiction

Recorded because an implementer working from 7539 instead of 8439 would hit them:

- **§2.8 prose and §2.8.1 pseudocode disagree.** The prose says the MAC input ends with the lengths *"as a 64-bit little-endian integer"*. The pseudocode writes `num_to_4_le_bytes(aad.length)` and `num_to_4_le_bytes(ciphertext.length)`. Erratum 4371 (Verified) corrects the pseudocode to 8 bytes. The test vectors follow the prose. An implementation built from the pseudocode fails interop.
- **§2.8 arithmetic.** It gives *"247,877,906,880 bytes"* for 2^32−1 blocks of 64 bytes, and the same figure for P_MAX. The correct value is 274,877,906,880, digits transposed (erratum 4858, Verified). The C_MAX figure is off the same way (erratum 4861, Verified). `rfc-8439` §2.8 has the corrected figures.
- Erratum 4700 (Verified) on §2.8's description of the AEAD output. 4372, 4373 and 4434, all Held, are pseudocode naming and wording in §2.5.1 and §2.6.

No `contradicts` edge: the correction is in `rfc-8439`, which supersedes this record.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §4's nonce-uniqueness and constant-time requirements are the operational security content |
| Cryptography | `core` | Defines the AEAD behind COSE algorithm 24 and an HPKE AEAD, as specified at the time |
| This project | `none` | Obsoleted, and ARCH-0001 defines statement *signatures*, not encryption. NG3 defers the algorithm suite |

**Bears on none.** No R-* in ARCH-0001 §5 concerns confidentiality. `research/0003-cipher-suite` mentions ChaCha20Poly1305 only as the AEAD of an existing prototype HPKE suite. §8 there says the wallet, attestation and delegation schemas *"will not embed a KEM"*, and nothing in it selects an AEAD. If one is ever needed, the citation is `rfc-8439`.

## Implementations

**Searched 2026-11-03.** Same set as `rfc-8439`. Implementations follow the corrected (8439) behaviour, which matches 7539's test vectors.

| Name | Kind | License | URL |
|---|---|---|---|
| libsodium (`crypto_aead_chacha20poly1305_ietf_*`) | open source | ISC | https://libsodium.org |
| OpenSSL | open source | Apache-2.0 | https://openssl.org |
| Go `golang.org/x/crypto/chacha20poly1305` | open source | BSD-3-Clause | https://pkg.go.dev/golang.org/x/crypto/chacha20poly1305 |
| RustCrypto `chacha20poly1305` | open source | MIT / Apache-2.0 | https://github.com/RustCrypto/AEADs |

Commercial: none listed separately. Every TLS 1.3 and WireGuard stack ships this AEAD.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, RFC Editor and errata evidence in `content.note`, implementations, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed.** This `rfc` record is at the summary bar for m-of-n/library#45. No issue owns an FX-1 extraction, and none should be opened for an obsoleted RFC. If the AEAD ever bears on a decision, the extraction belongs on `rfc-8439`. The `superseded_by` edge to `rfc-8439` is not authored here: `rfc-8439` holds `supersedes: rfc-7539`, and `bin/reindex` derives the inverse (`docs/references.md` §2). The `.txt` is in `.cache/` and is not committed.

## Limits

- **Obsoleted.** Everything here is superseded by `rfc-8439`. This record exists so citations to 7539 resolve.
- **No security proofs.** §4 defers to the academic papers ([ChaCha], [Poly1305], [Procter] for the composition), none of which is held.
- **96-bit nonce, no misuse resistance.** §2.8 note 1 caps a single invocation at about 256 GB. Random nonces at scale are not addressed. XChaCha20 is not in this RFC.
- **Read scope.** §1–§5 were read in full, including all §2.8 text and pseudocode. The test vectors in §2.x.x and Appendix A were not recomputed. The §2.8 contradiction above was found by reading, and confirmed against erratum 4371 and `rfc-8439` §2.8.1. The text has 7 uses of BCP 14 keywords outside the §1.1 boilerplate (§2.4, §2.5, §2.6, §4), not reconciled as an extraction would be.
