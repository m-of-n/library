---
schema: "library-summary/v1"
id: merkle-1979-thesis
record: merkle-1979-thesis
type: summary
updated: "2026-11-01"
---

# Secrecy, Authentication, and Public Key Systems

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | Ralph Charles Merkle |
| **Published** | 1979-06, Stanford University, SEL 79-017, Technical Report No. 1979-1 |
| **Identifier** | SEL 79-017 |
| **Source** | https://www.ralphmerkle.com/papers/Thesis1979.pdf |
| **Digest** | `sha256:af9c14df…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Merkle's thesis gathers his work from 1974 to 1979 (Chapter I). It defines a one-way hash function by the properties later called preimage and second-preimage resistance, and warns that a hash applied to many values makes a search for a match cheaper unless each use has its own function (Chapter II). Chapters III and IV give the puzzle method, the first public key distribution system. Chapter V builds a certified digital signature from a conventional cipher, using the Lamport-Diffie one-time signature and tree authentication. Chapters VI and VII give the trapdoor knapsack and argue for its security. Chapter IX lays out protocols for using public key systems, and Chapter X shows a weakness in a proposed multiple-encryption scheme.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Mostly historical; the knapsack result did not hold |
| Cryptography | `core` | One-way hash definitions, tree authentication, puzzles |
| This project | `adjacent` | Tree authentication is the origin of the transparency-log construction |

`bears_on: R-O-04`, through Chapters V and IX: tree authentication is what a SCITT-like log (`rfc-9162`, `rfc-9942`) is built from. It bears on nothing else open.

## Implementations

Not applicable and not searched: this is a thesis, not software we would build on. Descendants of its tree are in `rfc-9162`, `rfc-8391` and `rfc-8554`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **The knapsack did not survive.** Chapter VII argues that the trapdoor knapsack is secure, and Chapter I says the author is convinced. `gmr-1988-adaptive` §3 records Shamir's break of the basic Merkle-Hellman scheme. Do not rely on Chapters VI and VII.
- **Chapter V is an earlier text than `merkle-1989-certified`.** It has no Winternitz improvement (the name does not occur in the thesis) and no property 1 and 2 analysis, and it states a different signature size. Cite the published paper.
- **Chapter II's security argument is a plausibility argument**, in its own words.
- **Read by section, not whole.** Read closely: Chapter I, Chapter II. First pages of Chapters III to X and all of XI. The section list of Chapter IX, compared against `merkle-1980-protocols`. Chapter V read as far as the Lamport-Diffie section; the rest not compared line by line. The appendices of code and sample knapsacks were not read.
- **OCR text layer on a scan.** No sentence is quoted.
