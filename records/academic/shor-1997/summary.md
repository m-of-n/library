---
schema: "library-summary/v1"
id: shor-1997
record: shor-1997
type: summary
updated: "2026-11-03"
---

# Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer

|  |  |
|---|---|
| **Type** | paper (journal article) |
| **Maturity** | _unset_: a peer-reviewed journal article, so no standards-track level applies |
| **Authors** | Peter W. Shor (AT&T Research) |
| **Published** | 1997-10, *SIAM Journal on Computing* 26(5):1484–1509 (Crossref). Read as arXiv v2, 25 Jan 1996 |
| **Identifier** | DOI 10.1137/S0097539795293172 · arXiv:quant-ph/9508027 |
| **Source** | https://arxiv.org/pdf/quant-ph/9508027v2 (open preprint; the SIAM page returned 403) |
| **Digest** | `sha256:96ba03bb…` of the arXiv v2 PDF (full value in `record.yaml`), fetched 2026-11-03 |

## Overview

Shor's argument is that the quantitative ("strong") Church's thesis may fail for physically realisable machines. A quantum gate array can solve two problems believed classically hard in a number of steps polynomial in the input length (§1, Abstract). **Factoring** reduces, by Miller's randomised reduction, to finding the order *r* of a random *x* mod *n*. The quantum part finds *r* using reversible modular exponentiation (§3) and a quantum Fourier transform (§4), followed by continued-fraction post-processing on a classical machine. It takes O((log n)² (log log n)(log log log n)) quantum steps, against the number field sieve's sub-exponential time (§5). **Discrete logarithms** mod a prime *p* use two modular exponentiations and two Fourier transforms (§6). The paper notes the same algorithm works in any field with a cyclic multiplicative group (§6, closing paragraph).

§1 names the cryptographic consequence directly. These problems underpin *"several cryptosystems … including the widely used RSA public key cryptosystem"*. §7 says that if factoring and discrete logs remain the only uses of quantum computation, it *"will likely become a special-purpose technique whose only raison d'être is to thwart public key cryptosystems"*.

## What it contributes to "which attestation systems have a stated post-quantum path?"

It is the threat model, and it does not answer the question itself. It defines what "quantum-vulnerable" means for every signature scheme in this library. Three points from a close reading matter for how the topic answer is worded:

1. **Elliptic curves are not in this paper.** The words "elliptic" and "curve" do not occur in the v2 text. §6 covers discrete logs mod *p* and in fields with cyclic multiplicative groups, and cites Boneh and Lipton [1995] for the generalisation to abelian groups that are not cyclic. The break of ECDSA, EdDSA and ECDH, and so of `fips-186-4`'s ECDSA and `fips-186-5`'s EdDSA, follows from that generalisation and from later resource estimates for elliptic-curve groups. None of those works is held in this library. The parent project's `research/0001-signatures-and-attestation/mini-reports/H-post-quantum.md` §1 says *"Every deployed public-key signature scheme — RSA, ECDSA, EdDSA — falls to it"*, citing this paper. That is correct as a consequence and over-attributed as a citation. Not set as `contradicts`: the claim is true, just sourced one step short.
2. **It says nothing about when.** §1 says *"Currently, nobody knows how to build a quantum computer"*. §7 names imprecision and decoherence as the obstacles, and points to early error-correction work. No timeline appears, and none should be read into the paper. Deadlines come from `nistir-8547` and `cnsa-2-0`, not from here.
3. **It does not touch symmetric primitives or hashes.** Grover's search, which is the reason hash-based signatures (`fips-205`, `rfc-8554`, `rfc-8391`, `sp-800-208`) survive, is a different paper and is not held. §7 also speculates that finding a short lattice vector *"seems as if it might potentially be amenable to solution by a quantum computer"*. That is the hardness family behind ML-DSA (`fips-204`). Read in 2026, it is the author's own early note of the risk a lattice-only migration carries. It is a speculation, not a result.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The origin of the "harvest now, forge later" threat to long-lived signatures |
| Cryptography | `core` | The algorithms (§5, §6) that break RSA and finite-field discrete-log schemes, the basis of the generalisations that break elliptic-curve schemes |
| This project | `adjacent` | Motivates any post-quantum requirement on statement signatures. ARCH-0001 has none |

**Bears on none yet.** ARCH-0001 §5 has no requirement on algorithm choice, agility or post-quantum migration, and NG3 explicitly declines to *"Freeze encoding, algorithms"*. `research/0003-cipher-suite` §9 leaves the signature algorithm undecided. DEC-002 (encoding), DEC-003 (identifiers) and DEC-005 (envelope) do not choose an algorithm. When a requirement on suite agility or a post-quantum signature is written, this record is its threat-model citation.

## Implementations

**Searched 2026-11-03.** Implementations exist only as demonstrations on toy moduli.

| Name | Kind | License | URL |
|---|---|---|---|
| Cirq `examples/shor.py` | open source, simulator example | Apache-2.0 | https://github.com/quantumlib/Cirq/blob/main/examples/shor.py |
| Qiskit tutorial, "Shor's algorithm" (factors 15) | open source tutorial | Apache-2.0 code, CC BY-SA 4.0 text (Qiskit/documentation dual licence) | https://quantum.cloud.ibm.com/docs/en/tutorials/shors-algorithm |
| IBM Quantum Platform | commercial, hardware access | — | https://quantum.cloud.ibm.com/ |

Nothing here is something we would build on. The project needs to defend against the algorithm, not run it.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, the `supersedes: shor-1994` edge, implementations, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** A `paper` record owes no FX-1 extraction, and the algorithms are not something this project implements. A distillation would be warranted only if a design note needed the §5/§6 resource counts in detail. The arXiv PDF is in `.cache/` (gitignored) and is not committed.

## Limits

- **Read as the preprint, not the journal text.** SIAM returned 403. arXiv v2 (January 1996) predates the October 1997 publication, and any copy-edits or corrections between them are unknown. Locators are to v2.
- **Not a cryptanalysis of deployed systems.** It gives asymptotic step counts and no qubit or gate estimates for, say, RSA-2048 or P-256. Those are later literature, not held.
- **Elliptic-curve coverage is indirect.** See point 1 above. A library claim that "Shor breaks ECDSA" should cite this paper together with the elliptic-curve generalisation, which is a gap worth ingesting.
- **Read scope.** §1, §5, §6 and §7 were read in full. §2–§4 (gate model, reversible arithmetic, QFT) were read for structure, not checked line by line.
