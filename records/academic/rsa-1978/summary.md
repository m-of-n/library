---
schema: "library-summary/v1"
id: rsa-1978
record: rsa-1978
type: summary
updated: "2026-11-05"
---

# A Method for Obtaining Digital Signatures and Public-Key Cryptosystems

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | R. L. Rivest, A. Shamir, L. Adleman |
| **Published** | 1978-02, Communications of the ACM 21(2), pp. 120-126 |
| **Identifier** | DOI 10.1145/359340.359342 |
| **Source** | https://people.csail.mit.edu/rivest/pubs/RSA78.pdf |
| **Digest** | `sha256:8c007353…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

RSA gives a concrete trap-door one-way permutation, and with it a working form of the public-key cryptosystem and signature that Diffie and Hellman proposed (ref 1, §I). A message M becomes a number below n = pq and is encrypted as M^e mod n, and decrypted with d, where ed = 1 mod (p-1)(q-1) (§V, §VI). Signing applies the decryption operation to the message, and anyone can check the result with the public key (§IV). The authors separate signing from authentication: a signed message must convince a judge that the recipient did not forge it. Security rests in part on factoring: they show that finding d or phi(n) is as hard, and leave open whether another way exists (§IX). §VII gives the arithmetic, including Solovay-Strassen primality testing and a recommended 200-digit n.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Argues that a judge can be convinced, and invites attack on the method |
| Cryptography | `core` | The trap-door one-way permutation signatures need (§IV); basis of RSA signatures in `fips-186-5` |
| This project | `adjacent` | RSA remains an available suite, not a preferred one |

It bears on no open `DEC-*` or `R-*`. `bears_on` is empty on purpose.

## Implementations

Not applicable and not searched: this is a method paper, not software we would build on. Current RSA signature requirements are in `fips-186-5`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **The abstract overclaims.** It says *"Signatures cannot be forged, and a signer cannot later deny the validity of his signature."* There is no proof, and §IX says so. `gmr-1988-adaptive` §3 shows the scheme as given is selectively forgeable under a directed chosen-message attack, because it is multiplicative. Hence the `contradicts` edge on that record. The later fix is padding and hashing, not this paper's work.
- **Long messages are split into blocks** (§V), and §X blocks a signed message by the signature n. There is no hash, so nothing binds the blocks together. Do not copy this construction.
- **The equivalence with factoring is a conjecture** (§IX.D).
- **Key sizes and timings are 1978.** The 200-digit recommendation and Table I do not stand. `fips-186-5` and `sp-800-57pt1r5` hold current guidance.
- **Quantum.** Shor's algorithm (`shor-1997`) removes the factoring assumption on a quantum computer.
- **Identity is a public file.** §IV handles a forged file by having the file sign its replies. That is where certificates begin, not where they end.
- **Read whole**, all seven pages, from the author-hosted scan.
