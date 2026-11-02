---
schema: "library-summary/v1"
id: rabin-1979-tr212
record: rabin-1979-tr212
type: summary
updated: "2026-11-01"
---

# Digitalized Signatures and Public-Key Functions as Intractable as Factorization

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | Michael O. Rabin |
| **Published** | 1979-01, MIT/LCS/TR-212 |
| **Identifier** | MIT/LCS/TR-212 |
| **Source** | https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-212.pdf |
| **Digest** | `sha256:e8b37a44…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Rabin gives a public-key function E(x) = x(x+b) mod n, with n = pq, and proves that inverting it for even a small fraction of values lets one factor n (Theorems 1 and 2, §4). His claim is that this makes forgery hard almost everywhere, not just in the worst case, which he calls the first proved result of its kind (Abstract). RSA, by contrast, is at most as hard as factoring (Introduction). To sign, the signer hashes the message with a random suffix U and retries until the result is invertible, expecting four tries (§3). Verifying needs only one multiplication, so it is several hundred times faster than RSA. §5 generalises to cubes and rejects them for signatures.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Founds the hard-problem reduction for signatures |
| Cryptography | `core` | First signature scheme tied to factoring by proof |
| This project | `none` | Historical. Not a scheme we would deploy |

It bears on no open `DEC-*` or `R-*`. `bears_on` is empty on purpose.

## Implementations

Not applicable and not searched: this is a scheme report, not software we would build on.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **The theorem is about inversion, the claim is about forgery.** Theorems 1 and 2 reduce inverting E to factoring. The step to forging signatures goes through a hash C and a random suffix, and no theorem covers that step. The text treats C as harmless.
- **Disagreement recorded.** The Introduction says the ability to forge is equivalent to the ability to factor. `gmr-1988-adaptive` §§3 to 4 say this holds only under a known-message attack, and that padding breaks the proof. On chosen messages Rabin writes *"Actually, this does not seem a serious threat"* because of the hashing (§3). GMR's total break is of an unhashed form, so the two are not arguing about the same algorithm, but the claim of equivalence for the scheme as signed does not stand as proved.
- **This is the TR, not the 1978 chapter.** `lamport-1979-one-way` improves on Rabin's earlier one-time scheme, a different construction we do not hold.
- **C is not specified.** §3 refers to Rabin's 1978 chapter for the hash.
- **Performance figures are 1979 comparisons** with RSA.
- **Read whole**, all 20 PDF pages, through local OCR, which misses some formulas. Only the abstract and the §3 passage quoted above were checked against page images.
