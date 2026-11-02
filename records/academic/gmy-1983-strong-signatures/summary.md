---
schema: "library-summary/v1"
id: gmy-1983-strong-signatures
record: gmy-1983-strong-signatures
type: summary
updated: "2026-11-01"
---

# Strong Signature Schemes

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | Shafi Goldwasser, Silvio Micali, Andy Yao |
| **Published** | 1983-04, STOC '83, pp. 431-439 |
| **Identifier** | DOI 10.1145/800061.808774 |
| **Source** | https://web.archive.org/web/20060907233801id_/http://theory.lcs.mit.edu/~cis/pubs/shafi/1983-stoc.pdf |
| **Digest** | `sha256:64f23798…` of an Internet Archive capture (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Goldwasser, Micali and Yao list why signing as f^-1(m) is not enough, even if f is hard to invert: some message spaces may be easy to sign, random messages can be forged, and past signatures may help forge new ones (Abstract, §1). They give the first two schemes with a proof that a forger breaks a number-theoretic assumption: one bit-by-bit on Blum integers, reducing to factoring (§3), and one that reveals s-th roots modulo N at consecutive primes, reducing to inverting RSA (§4). The claim holds for every message space and distribution, so the proof does not lean on what messages look like. §3.5's first form reveals all prior messages. Rivest's suggestion, a tree of starting locations, removes that at the cost of longer signatures (Comment 3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Moves signature security from argument to reduction |
| Cryptography | `core` | First proved schemes; the tree idea reappears in `gmr-1988-adaptive` |
| This project | `none` | Historical. We would not deploy either scheme |

It bears on no open `DEC-*` or `R-*`. `bears_on` is empty on purpose.

## Implementations

Not applicable and not searched: this is a historical scheme paper, not software we would build on.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **Weaker than its abstract reads.** The abstract speaks of an adversary who has seen all previously signed messages. §2's definition fixes the message sequence T in advance. `gmr-1984-paradoxical` §IV and `gmr-1988-adaptive` §3 read the results as covering a generic chosen-message attack and say adaptive attacks are not settled. That reading fits the text.
- **Informal definition.** §2 says it describes a strong signature scheme only informally.
- **Sketches.** Theorems 11 and 12 are proof sketches, and the Remarks promise a fuller paper. Internal references do not line up: for example the text cites "theorem 1" and "claim 7" for items numbered otherwise.
- **Stateful.** The first scheme signs the concatenation of all messages so far (§3.5), and the second consumes a tape of primes (§4.3).
- **Archive copy.** Read from a 2006 Internet Archive capture of the MIT-hosted scan. Not compared with the ACM Digital Library file, which was unreachable.
- **Read whole**, all nine pages, from an OCR text layer that garbles formulas. No sentence is quoted and the proofs were followed in outline only.
