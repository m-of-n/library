---
schema: "library-summary/v1"
id: sp-800-208
record: sp-800-208
type: summary
updated: "2026-09-26"
---

# Recommendation for Stateful Hash-Based Signature Schemes

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice` — a NIST Special Publication, mandatory guidance for federal systems but not a FIPS |
| **Authors** | David Cooper, Daniel Apon, Quynh Dang, Michael Davidson, Morris Dworkin, Carl Miller |
| **Published** | 2020-10 |
| **Identifier** | SP 800-208 · DOI 10.6028/NIST.SP.800-208 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-208.pdf |
| **Digest** | `sha256:9ac6bee3da878e883874847b40f80d2265d6268385d8201f866581437533465f` |

## Overview

Supplements FIPS 186 with two **stateful hash-based signature** schemes —
**LMS** (RFC 8554) and **XMSS** (RFC 8391), with their multi-tree variants
**HSS** and **XMSS^MT**. It approves a *subset* of the parameter sets in those
RFCs and defines some new ones, all using 192- or 256-bit output with SHA-256
or SHAKE256.

The argument is a narrow one, and the document makes it honestly. Every
signature scheme in FIPS 186 "will be broken if large-scale quantum computers
are ever built"; the security of these schemes "depends only on the security of
the underlying hash functions," which is believed to survive. But statefulness
makes them **unsuitable for general use** (§1.1), so they are aimed at a
specific case: you must deploy now, the deployment will live for decades, and
you will not be able to change the verifier afterwards. Firmware signing for
constrained devices is the worked example.

A stateful HBS private key is a large set of **one-time** signature keys.
Sign twice under one OTS key and forgery becomes computationally feasible. The
document therefore spends most of its normative weight not on the mathematics
but on preventing that: §8.1 conformance requirements, and the hard constraint
that **key generation and signature generation must occur in hardware
cryptographic modules that do not allow secret keying material to be exported,
even in encrypted form** (§1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | An approved signature scheme, and the only quantum-resistant one we hold |
| Cryptography | `core` | Normative for the schemes; we implement none of them ourselves |
| This project | `adjacent` | Bears on `R-O-05`; settles no open `DEC-*` |

`bears_on: R-O-05` — sign the canonical encoding verbatim. LMS and XMSS both
apply **randomized hashing**: a random value is generated at signing time and
prepended to the message before the digest is taken (§9.2). So what is hashed
is not the canonical bytes alone, and the randomizer travels in the signature.
R-O-05 says the signed payload is the canonical encoding verbatim with an
authenticated type indicator; under these schemes the *scheme* inserts a prefix
beneath that layer. That is compatible — the randomizer is part of the
signature format, not the payload — but it is exactly the kind of detail that
a naive "we sign the canonical bytes" reading gets wrong.

## Implementations

Searched **2026-09-26**. Thin by comparison with the classical schemes, which
is itself the finding — the hardware-module requirement excludes most of them
from conformance regardless of correctness.

| Name | Kind | License | URL |
|---|---|---|---|
| `cisco/hash-sigs` | open source | custom permissive | https://github.com/cisco/hash-sigs — LMS/HSS reference |
| XMSS reference code | open source | CC0 | https://github.com/XMSS/xmss-reference |
| Bouncy Castle | open source | MIT | https://bouncycastle.org — LMS and XMSS in the Java/C# providers |
| liboqs | open source | MIT | https://openquantumsafe.org — includes stateful HBS |
| HSMs with stateful HBS firmware | commercial | — | Thales, Utimaco — availability varies by model and firmware |

**We use a vetted library. We do not implement these.** And note that a
software library alone **cannot** produce a conforming signature under this
recommendation: §1 requires a hardware module that will not export the private
key.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. If we ever adopted an HBS scheme, §8.1 would be the first
requirement set worth extracting — it is unusually testable for a NIST SP.

## Limits

- **The state is a correctness requirement, not a hardening measure.** Reuse of
  one OTS key is not a weakening; it makes forgery feasible. §9.1 is blunt
  about how easily this happens in practice: writing the state update to a file
  is *not* sufficient, because the write is cached and a crash before it
  reaches non-volatile memory can resurrect a used key. The state must be
  committed **before the signature is exported**. Monotonic counters are
  suggested where hardware provides them.
- **The hardware requirement rules this out for us as specified.** A project
  whose principals are keys held by ordinary software has no conforming path
  here. Holding this record is about knowing what approval costs, not about a
  scheme we can adopt.
- **The 192-bit parameter sets weaken the verifier, not the signer.** §9.2: a
  collision in SHA-256/192 or SHAKE256/192 may be found near 2⁹⁶, which "may be
  possible for a signer with access to an extremely large amount of computing
  resources." The formal security properties are untouched because only the
  signer can sign — but **the verifier loses assurance that the signer cannot
  change the message after revealing the signature.** For a statement model
  that is the wrong failure to accept: it makes a signed "A says B has C"
  equivocable by A. The 256-bit sets do not have this problem, and we should
  not use the 192-bit ones.
- **Not all RFC parameter sets are approved.** The sets in RFC 8391 using
  SHAKE128, SHAKE256 (as defined there) and SHA-512 are explicitly *not*
  approved (§6). "We implement RFC 8391" and "we conform to SP 800-208" are
  different claims.
- **Stateless post-quantum signing is elsewhere.** SLH-DSA (FIPS 205) is the
  stateless hash-based alternative and is **not held**. Anyone reaching for
  this record because they want post-quantum signatures probably wants that one.
