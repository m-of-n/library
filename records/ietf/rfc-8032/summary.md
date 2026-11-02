---
schema: "library-summary/v1"
id: rfc-8032
record: rfc-8032
type: summary
updated: "2026-11-01"
---

# Edwards-Curve Digital Signature Algorithm (EdDSA)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `informational`: IRTF stream, Category Informational |
| **Authors** | S. Josefsson, I. Liusvaara |
| **Published** | 2017-01 |
| **Identifier** | RFC 8032 · DOI 10.17487/RFC8032 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8032.txt |
| **Digest** | `sha256:ed63657f…` of the .txt (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

RFC 8032 specifies EdDSA, a variant of Schnorr's system on Edwards curves, for edwards25519 and edwards448 (§1). It gives five parameter sets: Ed25519, Ed25519ctx, Ed25519ph, Ed448 and Ed448ph (§5). Signing derives the nonce by hashing a secret prefix with the message, so no per-signature random number is needed (§1, §3.3, §8.2). PureEdDSA signs the message itself and stays collision-resilient, at the cost of two passes over the input (§4). The document is implementation-oriented: encoding, decoding and point addition for each curve, Python code (§6, Appendix A) and test vectors (§7). §8 gives the operational advice: side channels, contexts, malleability and which variant to choose.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Deterministic nonces remove the failure ElGamal and DSA share; §8.4 and §8.8 address malleability and verifier agreement |
| Cryptography | `core` | Normative for EdDSA as used by COSE (`rfc-9053`) |
| This project | `adjacent` | A likely suite, not a decided one. NG3 keeps algorithms unfrozen |

`bears_on: R-M-02`: a public key is a fixed 32 or 57 octet string with a defined encoding (§1, §5), so it can stand as a principal's identifier. `bears_on: R-O-05`: §8.7 sets a conditional MUST on buffering the whole message and explains that it is unsafe to process unverified data, which supports verifying the signed bytes before using them. Neither is a decision for a suite.

## Implementations

Searched **2026-11-01** for implementations. This covers open source only and is not exhaustive. Commercial HSM support was not searched. OpenSSL and libsodium are listed in `fips-186-5` from its 2026-09-22 search and were not re-checked here.

| Name | Kind | License | URL |
|---|---|---|---|
| Go `x/crypto` ed25519 | open source | not confirmed in this search | https://go.googlesource.com/crypto |
| RustCrypto `ed25519` | open source | Apache-2.0 OR MIT (licenses.dev) | https://licenses.dev/cargo/ed25519/1.5.3 |
| `ed25519-dalek` | open source | Apache-2.0 OR MIT for 1.0.1 (licenses.dev dependency view) | https://licenses.dev/cargo/ed25519-dalek-bip32/0.1.1 |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `rfc` is inside FX-1's type scope, so extraction would owe the full artifact set. This record was not extracted, and no issue owns its extraction yet. The text stays in `.cache/` and is not committed.

## Limits

- **Informational, from the IRTF.** The Status of This Memo says it is not an Internet Standards Track specification and that it is a CFRG product. Standing comes from use, such as `rfc-9053` and `fips-186-5`, not from this RFC. It is filed under `body: ietf`, and `publisher` was corrected from IETF to IRTF.
- **The Python in §6 and Appendix A is not side-channel silent**, says §8.1. Do not ship it.
- **Deterministic means no fresh nonce, not no entropy.** §8.2 still needs randomness for key generation.
- **Verification agreement is not complete.** §8.8 explains why the formulas multiply by the cofactor. It describes the disagreement risk rather than ruling on it for all implementations, so byte-identical verdicts across libraries are not promised.
- **§8.5 carries a SHOULD NOT on the prehashed variants**, Ed25519ph and Ed448ph, and a RECOMMENDED on Ed25519 or Ed448.
- **A sufficiently large quantum computer breaks both curves** (§1, §8.5).
- **Read by section, not whole.** Read closely: §1, §3.3, §3.4, §4, §8. Read in part: §2, §3 opening, §5 section structure. §5's arithmetic, §6, §7 and the appendices were not read. Test vectors were not run. Errata were not checked: the errata page gave our client nothing usable.
