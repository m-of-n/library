---
schema: "library-summary/v1"
id: fips-180-4
record: fips-180-4
type: summary
updated: "2026-09-26"
---

# Secure Hash Standard (SHS)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — a US Federal Information Processing Standard, approved by the Secretary of Commerce |
| **Authors** | NIST |
| **Published** | 2015-08 (supersedes FIPS 180-3; erratum 2014-05-09 folded in) |
| **Identifier** | FIPS 180-4 · DOI 10.6028/NIST.FIPS.180-4 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf |
| **Digest** | `sha256:0455b406d89648d20cbde375561e19c245b9815e894164c2670772e3d54deb82` |

## Overview

Specifies the SHA-1 and SHA-2 hash functions: **SHA-1, SHA-224, SHA-256,
SHA-384, SHA-512, SHA-512/224 and SHA-512/256**. Each is an iterative one-way
function built on the Merkle–Damgård construction, described in two stages —
preprocessing (pad, parse into blocks, set the initial hash value) and hash
computation.

The document is a **specification, not an argument**. It defines the functions
bit-exactly and then delegates every security question elsewhere: Appendix A.1
says the security of these algorithms "is discussed in [SP 800-107]" and offers
nothing further. The one substantive policy statement is in the announcement,
§6 — *either* this Standard *or* FIPS 202 "must be implemented wherever a
secure hash algorithm is required for Federal applications." Approval does not
choose between SHA-2 and SHA-3.

Changes from 180-3 are minor (Appendix C): padding may now be inserted at any
point before the block containing it is processed, and SHA-512/224 and
SHA-512/256 were added along with the method for deriving an initial value for
SHA-512/t.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines the hash functions integrity and signing actually run on |
| Cryptography | `core` | Normative for the primitives; we implement none of them ourselves |
| This project | `adjacent` | Bears on `R-M-02` but settles no open `DEC-*` |

`bears_on: R-M-02` — a principal may be identified solely by key or **key
digest**. That makes the choice of digest function a naming decision, not an
implementation detail: two principals named under different functions are not
comparable, and a name is only as stable as the function that produced it.

**§7 is the clause that matters to us.** Truncation of a digest is permitted —
apply a longer function and take the leftmost bits — with the guidance deferred
entirely to SP 800-107. Any key-digest naming scheme that truncates is
operating under a rule this document declines to state.

## Implementations

Searched **2026-09-26**. Ubiquitous; the list below is representative, not
exhaustive.

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL | open source | Apache-2.0 | https://openssl.org |
| libsodium | open source | ISC | https://libsodium.org — SHA-256/512 |
| python-cryptography | open source | Apache-2.0 / BSD | https://cryptography.io |
| Go `crypto/sha256`, `crypto/sha512` | open source | BSD-3-Clause | https://pkg.go.dev/crypto/sha256 |
| RustCrypto `sha2` | open source | MIT / Apache-2.0 | https://github.com/RustCrypto/hashes |
| CAVP-validated HSMs | commercial | — | Thales, Entrust, AWS CloudHSM |

**We use a vetted library. We do not implement these.** Per `CLAUDE.md`, no
generated cryptographic primitives. Note that CAVP validation is per
implementation and per version — none of the above is validated by virtue of
appearing here.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. We extract no requirements from it — we conform to no clause
here, we call a library. See `docs/requirements.md` §5.1.

## Limits

- **It still specifies SHA-1, and says nothing against it.** SHA-1 appears
  throughout as a first-class algorithm of the Standard. The withdrawal is
  elsewhere — SP 800-131A and SP 800-107 — so **reading FIPS 180-4 alone would
  leave you believing SHA-1 is approved.** This is the sharpest trap in the
  document and the reason it cannot be cited as "the list of hash functions we
  may use."
- **No security analysis whatsoever.** Appendix A.1 is two lines of deferral.
  Digest lengths are in Figure 1; *strengths* are not in this document. For
  collision and preimage figures you need FIPS 202 Table 4 or SP 800-107.
- **It does not choose.** §6 approves this Standard or FIPS 202
  interchangeably. A system naming principals by key digest must pick a
  function itself; NIST approval does not narrow the field to one, and two
  conforming systems can be mutually unintelligible.
- **Second-preimage strength is message-length dependent** for the
  Merkle–Damgård functions — `256 − L(M)` for SHA-256, per FIPS 202 Table 4.
  The SHA-512/t and SHA-3 functions do not have this property. A flat "256-bit
  hash, 256-bit security" reading is wrong.
- **Approval is jurisdictional.** "FIPS-approved" describes US federal
  procurement scope, not a claim that these are the best available functions.
