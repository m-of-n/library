---
schema: "library-summary/v1"
id: schnorr-1989-smartcards
record: schnorr-1989-smartcards
type: summary
updated: "2026-11-01"
---

# Efficient Identification and Signatures for Smart Cards

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | C. P. Schnorr |
| **Published** | 1990, Advances in Cryptology - CRYPTO '89, LNCS 435, pp. 239-252 |
| **Identifier** | DOI 10.1007/0-387-34805-0_22 |
| **Source** | https://web.archive.org/web/20260606143933id_/https://link.springer.com/content/pdf/10.1007/0-387-34805-0_22.pdf |
| **Digest** | `sha256:0adf1be2…` of an Internet Archive capture (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Schnorr announces an identification protocol and a signature scheme based on discrete logarithms in a subgroup of prime order q, about 140 bits, modulo a prime p of about 512 bits (§1, §2). Signing picks random r, computes x = alpha^r mod p, sets e = h(x, m) and y = r + se mod q, and outputs (e, y), about 212 bits. The message-dependent work is one short multiplication. To make the exponentiation cheap on a smart card, §3 adds preprocessing: combine a stored set of random pairs (r_i, x_i) in place of a fresh exponentiation. §4 analyses that preprocessing, and §2 compares the scheme with ElGamal's equation.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The hash of the commitment replaces the verifier's challenge |
| Cryptography | `core` | Conference publication of the Schnorr signature |
| This project | `adjacent` | Ancestor of EdDSA (`rfc-8032` §1 calls it a variant of Schnorr's system) |

It bears on no open `DEC-*` or `R-*`. `bears_on` is empty on purpose; `rfc-8032` carries the bearing for the form we would use.

## Implementations

Not applicable and not searched: this is a scheme paper, not software we would build on. See `rfc-8032`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **§3's preprocessing does not stand as written.** It is claimed sufficient at k = 8, d = 6 (§4). `schnorr-1991-jcryptology` Remark 4 reports de Rooij's result that this form is vulnerable, and changes the algorithm. Hence the `contradicts` edge on that record.
- **Security of the signature is not proved here.** Proposition 2.1 covers the identification test, and §2 says the argument that nothing leaks is informal and the scheme is not zero-knowledge.
- **Parameters are from 1989.** p of 512 bits and t = 72 do not stand.
- **A patent is named** in the title footnote: European application 89103290.6. Patent status was not checked.
- **Archive copy.** Read whole, all 14 pages, from an Internet Archive capture of Springer's PDF. The OCR layer garbles exponents; formulas were read for structure and the proofs of §4 followed in outline only.
