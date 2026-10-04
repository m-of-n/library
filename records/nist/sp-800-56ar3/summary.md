---
schema: "library-summary/v1"
id: sp-800-56ar3
record: sp-800-56ar3
type: summary
updated: "2026-10-03"
---

# Recommendation for Pair-Wise Key-Establishment Schemes Using Discrete Logarithm Cryptography

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice` — a NIST Special Publication, not a FIPS |
| **Authors** | Elaine Barker, Lily Chen, Allen Roginsky, Apostol Vassilev, Richard Davis |
| **Published** | 2018-04 (Revision 3) |
| **Identifier** | SP 800-56A Rev. 3 · DOI 10.6028/NIST.SP.800-56Ar3 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Ar3.pdf |
| **Digest** | `sha256:6b315e3a91012981f9a88ad62c97ea7d4b170a7746e713f34dd29538ee46f403` |

## Overview

Specifies the approved **pair-wise key-establishment schemes** built on the
discrete logarithm problem, over both finite fields and elliptic curves:
several variations of **Diffie-Hellman** and of **MQV**, together with the key
derivation and key confirmation machinery around them.

The library holds it for a specific reason. `sp-800-186` Table 2 grants
P-224/256/384/521 the usage *"ECDSA, EC key establishment (see SP 800-56A)"* —
so the curve record's own statement of what those curves are approved for
pointed at a document we did not have. That is now closed.

It is the classical counterpart to `draft-ietf-jose-pqc-kem`: SP 800-56A is
how two parties agree a key *today*, ML-KEM is the proposed post-quantum
replacement, and `fips-203` is the primitive behind it.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Key establishment is half of what a curve is approved for |
| Cryptography | `core` | Normative for the schemes |
| This project | `none` | Key agreement establishes a shared secret; it asserts nothing |

**`bears_on` is empty, deliberately.** A key-establishment scheme produces a
shared secret between two parties. It makes no statement, names no subject,
and leaves nothing a third party could later verify — the same reasoning
recorded on `fips-203` for ML-KEM, and for the same underlying reason:
confidentiality machinery is not attestation machinery.

Held to complete `sp-800-186`'s Table 2 citation, not because a decision turns
on it.

## Implementations

Searched **2026-10-03**. ECDH is universal; MQV is effectively absent from
mainstream libraries, which is itself the useful finding.

| Name | Kind | License | URL |
|---|---|---|---|
| OpenSSL | open source | Apache-2.0 | https://openssl.org — ECDH and FFDH |
| Go `crypto/ecdh` | open source | BSD-3-Clause | https://pkg.go.dev/crypto/ecdh |
| RustCrypto `elliptic-curves` | open source | MIT / Apache-2.0 | https://github.com/RustCrypto/elliptic-curves |
| CAVP/CMVP-validated HSMs | commercial | — | validated under the CVL/KAS programmes |

**We use a vetted library. We do not implement these.**

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. Held to resolve a citation; we neither conform nor map.

## Limits

- **MQV is specified and essentially unimplemented.** The document gives MQV
  equal standing with Diffie-Hellman, but no mainstream open-source library
  ships it. Reading approval as availability would be a mistake here — this is
  a case where the standard and the ecosystem have diverged and the standard
  does not say so.
- **It is entirely classical and that is now its defining limitation.** Every
  scheme here falls to a cryptographically relevant quantum computer. NIST's
  answer is ML-KEM (`fips-203`), which is a KEM and not a Diffie-Hellman
  variant — so the post-quantum replacement has a *different shape*, not just
  different parameters. Protocols assuming a DH-shaped interface do not port
  by swapping a primitive.
- **Revision 3 is from 2018 and predates the PQ standards entirely.** It has
  no hybrid or post-quantum guidance. For that, SP 800-227 and the KEM drafts
  are the current material, and SP 800-227 is **not held**.
- **Key confirmation is optional, and its absence is a real attack surface.**
  The document defines schemes both with and without it; without key
  confirmation, a party can complete the protocol believing it shares a key
  with someone it does not. Which variant an application uses is not visible
  from the scheme name alone.
- **It does not authenticate the parties.** Key establishment assumes static
  public keys are already trustworthy. Where that trust comes from — a
  certificate, a key digest under R-M-02, a trust-on-first-use decision — is
  entirely outside this document, and is precisely the part our project is
  about.
