---
schema: "library-summary/v1"
id: schnorr-1991-jcryptology
record: schnorr-1991-jcryptology
type: summary
updated: "2026-11-05"
---

# Efficient Signature Generation by Smart Cards

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | C. P. Schnorr |
| **Published** | 1991, Journal of Cryptology 4(3), pp. 161-174 |
| **Identifier** | DOI 10.1007/BF00196725 |
| **Source** | https://web.archive.org/web/20240913105358id_/https://link.springer.com/content/pdf/10.1007/BF00196725.pdf |
| **Digest** | `sha256:57e8124d…` of an Internet Archive capture (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This is the journal version of the Schnorr scheme. It derives a signature from an interactive authentication protocol by replacing the verifier's challenge with a hash (§1, §2). Discrete logs are taken in a prime-order subgroup, which shortens signatures to 212 bits and improves on ElGamal in speed and size. Theorem 2.1 shows that anyone passing authentication with a success rate above 2^(-t+1) can be used to compute the discrete log of the public key: two answers on one commitment give the secret. §2 also sets out what the hash must satisfy, works through ElGamal's equation to reach the new one, says the scheme works in other groups such as elliptic curves, and warns that running the authentication and signature schemes side by side lets a verifier extract a signature. §4 replaces the 1989 preprocessing.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Hash requirements stated by attack; warning about the authentication and signature schemes coexisting |
| Cryptography | `core` | Standard citation for the scheme behind EdDSA |
| This project | `adjacent` | `rfc-8032` is the form we would use |

It bears on no open `DEC-*` or `R-*`, so `bears_on` is empty on purpose. §2 *Coexistence of the Authentication and the Signature Scheme* shows a verifier can choose a challenge equal to h(x, m) and so turn a proof of identity into a signature on m. That is a cousin of the confusion R-O-05's authenticated type indicator guards against, but R-O-05 is about payload encodings and verify-before-decode, and Schnorr's remedy is to send a hash of x, so we do not claim it as support.

## Implementations

Not applicable and not searched: this is a scheme paper, not software we would build on. See `rfc-8032` for the deployed variant.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **Contradicts `schnorr-1989-smartcards` on preprocessing.** Remark 4 of §4 reports de Rooij's attack on the earlier form, so the 1989 claim cannot stand with this one. The new algorithm requires a random permutation.
- **The new preprocessing is not proved.** §4 says *"If proven to be secure"* and Remark 5 says only that no attack under 2^72 is known.
- **Theorem 2.1 is about authentication.** Security of the signature against chosen messages is not proved here. §2 argues it through the properties asked of h. It says it *seems* unnecessary that h be collision-free, then strongly recommends one-wayness in m.
- **The Coexistence advice is about transmitting x.** It hashes x in the authentication protocol. Domain separation as a general rule is not stated.
- **Parameters are from 1991.** §2 itself warns that p > 2^512 may soon need raising.
- **A patent is named**: U.S. 4995082 of February 19, 1991. Current status was not checked.
- **Archive copy.** Read whole, all 14 pages, from an Internet Archive capture of Springer's PDF. Formulas read for structure; the proof of Theorem 2.1 was followed and not checked line by line.
