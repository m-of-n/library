---
schema: "library-summary/v1"
id: lamport-1979-one-way
record: lamport-1979-one-way
type: summary
updated: "2026-11-05"
---

# Constructing Digital Signatures from a One Way Function

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | Leslie Lamport |
| **Published** | 1979-10-18, SRI International Technical Report CSL-98 |
| **Identifier** | CSL-98 |
| **Source** | https://lamport.azurewebsites.net/pubs/dig-sig.pdf |
| **Digest** | `sha256:15f8c99c…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Lamport signs with nothing but a one-way function. The signer publishes the images under F of 40 secret keys in a trusted repository, then signs one document by revealing the 20 keys that G(m) selects (§2). Anyone can verify, with no further action by the signer, and the signer can then destroy the unused keys (§1). That removes two defects of the Rabin scheme it improves on: the need for a single recipient, and the signer's later involvement before a court. The security argument is short: forging needs an inverse of F or a second document with the same G (§2). §3 builds G from an ordinary one-way function, retrying documents until exactly 20 bits are set.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Shows signatures need no trap door, only a one-way function |
| Cryptography | `core` | Founding one-time signature |
| This project | `adjacent` | Ancestor of the hash-based schemes in `rfc-8391` and `rfc-8554` |

It bears on no open `DEC-*` or `R-*`. `bears_on` is empty on purpose.

`see_also: rfc-8554` because LMS is a deployed descendant of the one-way-function signature this report starts. RFC 8554 does not cite the report; its abstract names Lamport only as lineage, so the edge is our judgement rather than a `cites`. The links to `diffie-hellman-1976`, which reference [1] cites, and to `merkle-1989-certified`, which cites this report, are carried by `cites` and not repeated as `see_also`.

## Implementations

Not applicable and not searched: this is a method paper, not software we would build on. Deployed descendants are in `rfc-8391` and `rfc-8554`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **One key set signs one document.** §2 says many documents need a sequence of published 40-tuples and omits the details as simple. Making that practical is the work of `merkle-1989-certified`.
- **Depends on a trusted public repository**, which must also prove in court that the signer created each entry (§1). The paper does not build one.
- **The Rabin scheme compared is not `rabin-1979-tr212`.** Lamport's reference [2] is Rabin's 1978 chapter, *Digitalized Signatures*, a one-time scheme that the library does not hold. Do not read §1's criticism as being about the TR's scheme.
- **G is left open.** §3 says the author cannot prove the many-to-one construction safe, and hopes for a better one than the retry method.
- **Lamport-Diffie versus Lamport.** `diffie-hellman-1976` §IV already gives Lamport's bit-by-bit scheme with 2N vectors. This report's 40-choose-20 subset is a different encoding.
- **Read whole**, all eight pages, from the scanned report's OCR layer. No sentence is quoted.
