---
schema: "library-summary/v1"
id: fips-202
record: fips-202
type: summary
updated: "2026-09-26"
---

# SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — a US Federal Information Processing Standard, approved by the Secretary of Commerce |
| **Authors** | NIST |
| **Published** | 2015-08 |
| **Identifier** | FIPS 202 · DOI 10.6028/NIST.FIPS.202 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf |
| **Digest** | `sha256:1592607831ff0908cc590632ce371c6c95e94025bb1a0c8ae90a4d0ec1ed025e` |

## Overview

Specifies the SHA-3 family — four hash functions (**SHA3-224, SHA3-256,
SHA3-384, SHA3-512**) and two extendable-output functions (**SHAKE128,
SHAKE256**) — all defined as modes of the `KECCAK-p[1600, 24]` permutation via
the sponge construction. It also specifies the `KECCAK-p` permutation family
itself, explicitly so that future permutation-based functions can be built on
it.

The argument is **design diversity, not replacement**. SHA-3 does not supersede
FIPS 180-4; the announcement says the two standards together "provide
resilience against future advances in hash function analysis, because they rely
on fundamentally different design principles." Sponge rather than
Merkle–Damgård also buys length-extension resistance for free, which SHA-2 does
not have.

The subtler contribution is the **XOF as a distinct primitive**. SHAKE128 and
SHAKE256 produce output of any requested length, and §7 is careful that they
are *approved XOFs* but "**not approved as hash functions**," for the reason
given in A.2 — see Limits, because it is the finding that matters most here.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines the second approved hash family and the XOF primitive |
| Cryptography | `core` | Normative for the primitives; we implement none of them ourselves |
| This project | `adjacent` | Bears on `R-M-02` but settles no open `DEC-*` |

`bears_on: R-M-02` — naming a principal by key digest makes the digest function
part of the name. FIPS 202 widens rather than narrows that choice: after it,
**two fully conforming systems can name the same key differently and neither is
wrong**, because §6 of FIPS 180-4 and §6 here approve both families
interchangeably. That is the finding a key-digest naming scheme has to resolve
for itself, and it is why this record is held alongside FIPS 180-4 rather than
instead of it.

Security strengths are in **Table 4** — the only place in either hash standard
where collision, preimage and second-preimage figures are tabulated for SHA-1,
SHA-2 and SHA-3 side by side. It is the reference table for the lane.

## Implementations

Searched **2026-09-26**.

| Name | Kind | License | URL |
|---|---|---|---|
| XKCP (eXtended Keccak Code Package) | open source | CC0 / public domain | https://github.com/XKCP/XKCP — the designers' reference |
| OpenSSL | open source | Apache-2.0 | https://openssl.org — SHA-3 and SHAKE |
| python-cryptography / `hashlib` | open source | Apache-2.0 / BSD / PSF | `hashlib.sha3_256`, `hashlib.shake_128` |
| Go `golang.org/x/crypto/sha3` | open source | BSD-3-Clause | https://pkg.go.dev/golang.org/x/crypto/sha3 |
| RustCrypto `sha3` | open source | MIT / Apache-2.0 | https://github.com/RustCrypto/hashes |
| CAVP-validated HSMs | commercial | — | Thales, Entrust, AWS CloudHSM |

**We use a vetted library. We do not implement these.** CAVP validation is per
implementation and per version; nothing above is validated by appearing here.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. We conform to no clause here. See `docs/requirements.md` §5.1.

## Limits

- **SHAKE output is prefix-related, and this breaks digest naming.** A.2 states
  it outright: for any `d`, `e` and message `M`,
  `Trunc_d(SHAKE128(M, d+e)) == SHAKE128(M, d)`. The output length is not an
  input to the function — conceptually the output is an infinite string and you
  take a prefix. **So a 128-bit SHAKE name of a key is a literal prefix of the
  256-bit SHAKE name of the same key**, and any scheme that treats digest
  length as a security parameter, or that compares names of differing length,
  is relying on a property SHAKE does not have. This is precisely why §7
  withholds approval of the XOFs *as hash functions*. A key-centric naming
  scheme should use SHA3-*n* or SHA-2, not a truncated SHAKE, unless it can
  state why the prefix relation is harmless.
- **SHAKE strength is capped by output length, not by the 128/256 in the name.**
  Table 4: collision resistance is `min(d/2, 128)` for SHAKE128 and
  `min(d/2, 256)` for SHAKE256. At `d = 224` both give 112-bit collision
  resistance and they differ only in preimage resistance. The suffix names the
  *ceiling*, not the delivered strength.
- **Approved XOF uses are deferred.** §6 of the announcement and §7 both say
  approved uses of the XOFs "will be specified in NIST Special Publications" —
  SP 800-185 (cSHAKE, KMAC, TupleHash, ParallelHash) is the follow-on, and **we
  do not hold it.** Reading FIPS 202 alone does not tell you what you are
  allowed to do with SHAKE.
- **It settles nothing in our architecture.** It tells us a second approved
  family exists, not which to use. ARCH-0001 NG3 defers the suite.
- **Conforming implementations may restrict input and output lengths** (§7),
  which is an interoperability hazard the Standard names and then declines to
  constrain.
