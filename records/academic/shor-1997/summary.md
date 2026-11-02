---
schema: "library-summary/v1"
id: shor-1997
record: shor-1997
type: summary
updated: "2026-11-01"
---

# Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed journal paper |
| **Authors** | Peter W. Shor |
| **Published** | 1997-10, SIAM Journal on Computing 26(5), pp. 1484-1509 (Crossref). Read as arXiv v2, 1996-01-25 |
| **Identifier** | DOI 10.1137/S0097539795293172 · arXiv quant-ph/9508027 |
| **Source** | https://arxiv.org/pdf/quant-ph/9508027 |
| **Digest** | `sha256:96ba03bb…` of the arXiv PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Shor gives efficient randomized algorithms for factoring integers and for discrete logarithms modulo a prime on a hypothetical quantum computer, which removes the hardness that RSA-style and Diffie-Hellman-style public-key cryptography rest on (§1). Factoring is reduced to finding the order of an element mod n (§5), using a quantum Fourier transform (§4) and reversible modular exponentiation (§3). Factoring takes O((log n)^2 (log log n)(log log log n)) quantum steps plus polynomial classical post-processing, against the number field sieve's superpolynomial time (§5). The discrete-log algorithm uses two modular exponentiations and two Fourier transforms (§6). The argument is also about computation itself: the result is evidence against the quantitative Church's thesis (§1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The break that every quantum-vulnerable label in `nistir-8547` and `cnsa-2-0` assumes |
| Cryptography | `core` | The algorithms behind the threat |
| This project | `adjacent` | Background for the signature suite, which NG3 defers |

It bears on no open `DEC-*` or `R-*`: it says why classical signatures have a sunset, not what we should sign with. `bears_on` is empty on purpose. It is summarized anyway because the `post-quantum-migration` topic rests on it.

## Implementations

Not applicable and not searched: this is an algorithm paper, and we would not build on a factoring implementation.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **Preprint, not the journal text.** We read arXiv v2. The SIAM version is behind the publisher and was not compared.
- **No resource estimates.** It gives asymptotics only. Qubit counts and timelines for a cryptographically relevant machine are not here, and nothing in this record should be read as a date.
- **Elliptic curves are not treated.** §6 covers discrete logs mod p. Applying this to ECDSA or EdDSA comes from later work that NIST assumes (`nistir-8547` §2.1.1), not from this paper.
- **A forward note on lattices.** §7 suggests that finding a short vector in a lattice *"seems as if it might potentially be amenable to solution by a quantum computer"*. ML-DSA rests on structured lattices, and no such algorithm is claimed here. It is a 1996 remark and we record it only as context for why NIST wants a non-lattice hedge (`nistir-8610`).
- **The practicality discussion is dated.** §7's view of decoherence and error correction is from 1996.
- **Read scope.** §1, the definitions of §5 and §6, and §7 were read closely. The proofs in §3 to §6 were not checked.
