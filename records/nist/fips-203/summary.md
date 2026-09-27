---
schema: "library-summary/v1"
id: fips-203
record: fips-203
type: summary
updated: "2026-09-26"
---

# Module-Lattice-Based Key-Encapsulation Mechanism Standard

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — a US Federal Information Processing Standard, issued under 40 U.S.C. 11331 |
| **Authors** | NIST |
| **Published** | 2024-08-13 (effective immediately on publication) |
| **Identifier** | FIPS 203 · DOI 10.6028/NIST.FIPS.203 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf |
| **Digest** | `sha256:fe1f12f32a7e44ec9fdebbf400cda843a40b506dee676725234dc6f7923b6cac` |

## Overview

Specifies **ML-KEM**, a key-encapsulation mechanism derived from
CRYSTALS-KYBER, in three parameter sets — ML-KEM-512, ML-KEM-768 and
ML-KEM-1024, claimed at security categories 1, 3 and 5. Its security rests on
the hardness of the **Module Learning With Errors** problem, believed to hold
against a quantum adversary.

A KEM is not encryption and not a signature. The shape is: the holder generates
a decapsulation key (private) and an encapsulation key (public); a counterparty
uses the encapsulation key to produce a shared secret plus a ciphertext; the
holder recovers the same shared secret from that ciphertext. The output is a
**shared secret for symmetric use** — confidentiality, and at most implicit
authentication of the key holder.

Worth recording for the lane: ML-KEM is **built on FIPS 202**. §4.1 defines its
internal functions directly in terms of SHA3-256, SHA3-512, SHAKE128 and
SHAKE256 — `H(s) := SHA3-256(s)`, `J(s) := SHAKE256(s, 8·32)`,
`PRF_η(s,b) := SHAKE256(s‖b, 8·64·η)`. The post-quantum standard inherits the
SHA-3 permutation wholesale.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Real and important, but it is confidentiality machinery |
| Cryptography | `core` | Normative for the primitive, if we ever needed a KEM |
| This project | `none` | Nothing in a key-centric *statement* model turns on it |

**`bears_on` is empty, deliberately.** Our model is about who says what about
which artifact — naming, signing, delegation. ML-KEM establishes a shared
secret; it makes no assertion, carries no subject, and produces nothing a
verifier could later re-check. There is no requirement in ARCH-0001 it
discharges, and inventing one to justify the record would be worse than holding
it honestly as background.

It is held as the **post-quantum counterpart to the signature records** — so
that the lane's answer can say what NIST has standardised post-quantum and what
it has not — and because `docs/scope.md` §6 asks that a negative verdict be
recorded once rather than re-litigated each time someone notices the gap.

## Implementations

Searched **2026-09-26**. The standard is recent; treat conformance claims as
version-specific and unverified here.

| Name | Kind | License | URL |
|---|---|---|---|
| `pq-crystals/kyber` | open source | CC0 / Apache-2.0 | https://github.com/pq-crystals/kyber — reference from the submission team |
| liboqs (Open Quantum Safe) | open source | MIT | https://openquantumsafe.org |
| OpenSSL 3.5+ | open source | Apache-2.0 | https://openssl.org — ML-KEM in the default provider |
| AWS-LC / `aws-lc-rs` | open source | Apache-2.0 / ISC | https://github.com/aws/aws-lc |
| Go `crypto/mlkem` | open source | BSD-3-Clause | https://pkg.go.dev/crypto/mlkem |

**We use a vetted library. We do not implement these.** NIST's validation
programme for ML-KEM is newer than the classical CAVP suites; a claim of
FIPS 203 conformance should be checked against CMVP directly, not inferred.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`, and none is warranted — we extract requirements only where
we intend to conform or map, and we intend neither.

## Limits

- **It is not a signature scheme, and must never be cited as our post-quantum
  answer.** The post-quantum *signature* standards are **FIPS 204 (ML-DSA)** and
  **FIPS 205 (SLH-DSA)**, and the library **holds neither**. Combined with
  `fips-186-5`'s own Limits — that treating 186-5 as "the signature standard"
  in 2026 would be wrong — this is the open gap in the lane: we hold the
  post-quantum KEM and none of the post-quantum signatures. Named as out of
  scope in #21 and tracked for a later record.
- **Security is conditional and the conditions are elsewhere.** §13 states the
  guarantees "only hold under certain conditions (see SP 800-227)", including
  secrecy of the randomness, the decapsulation key and the shared secret
  itself. SP 800-227 is not held.
- **Category claims are claims.** §8 and the security analysis present
  categories 1/3/5 as *claimed*; lattice cryptanalysis is young relative to
  factoring, and the document does not pretend otherwise.
- **Patent position is a licence, not a grant.** NIST records two patent
  licence agreements intended to let anyone implement ML-KEM, and then says
  plainly that implementations "may be covered by U.S. and foreign patents of
  which NIST is not aware." That is weaker than it first reads.
- **It inherits FIPS 202's fate.** Because H, J and the PRFs are SHA-3/SHAKE,
  any future weakening of `KECCAK-p` is an ML-KEM problem too. The two records
  are not independent.
