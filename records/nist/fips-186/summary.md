---
schema: "library-summary/v1"
id: fips-186
record: fips-186
type: summary
updated: "2026-11-01"
---

# FIPS 186: Digital Signature Standard (DSS), 1994

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `historic`: withdrawn or superseded (CSRC) |
| **Authors** | National Institute of Standards and Technology |
| **Published** | 1994-05-19, effective 1994-12-01. Change Notice 1, 1996-12-30. Withdrawn 1998-12-15 (CSRC) |
| **Identifier** | FIPS PUB 186 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub186.pdf |
| **Digest** | `sha256:1ee5bf0d…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

FIPS 186 is the first Digital Signature Standard, and prescribes one algorithm: the Digital Signature Algorithm, with SHA as its hash (§1, §3). DSA works in a 160-bit subgroup of a prime field of 512 to 1024 bits (§4). A signature is the pair r = (g^k mod p) mod q and s = k^-1(SHA(M) + xr) mod q (§5), a form descended from ElGamal's with a shorter result (our reading; the standard does not say so). That descent is the reason for the `see_also` edge to `elgamal-1985`. The per-message k must be secret and regenerated for each signature (§4). The appendices give prime generation (2), random number generation (3) and a worked example (5). Change Notice 1 replaces the example for SHA-1 and adds a patent note to the precomputation method.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | First U.S. federal signature standard |
| Cryptography | `core` | Defines DSA |
| This project | `none` | Withdrawn. Current requirements are in `fips-186-5` |

It bears on no open `DEC-*` or `R-*`, and `bears_on` is empty on purpose: a withdrawn standard. `fips-186-5` carries the live bearing.

## Implementations

Not searched: this standard is withdrawn. See `fips-186-5`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `spec` is inside FX-1's type scope, and extraction would owe the full artifact set, but this withdrawn version was not extracted and no issue owns it. The PDF stays in `.cache/` and is not committed.

## Limits

- **Overclaims in its own text.** §3 says *"In other words, signatures cannot be forged."* That is a design goal, not a result. `fips-186-3` §3 later says signatures are *designed* so that they cannot be.
- **Identity is out of scope.** §3 requires a binding between a user and a key, then says: *"Systems for certifying credentials and distributing certificates are beyond the scope of this standard."*
- **Non-repudiation is asserted in the Abstract, not defined.** A later version softens it (`fips-186-3`).
- **The patent statement did not last.** It says Commerce is not aware of patents that would be infringed. Change Notice 1 adds that precomputation may be covered, and `fips-186-1` widens that to the algorithms.
- **Hash is named by a separate standard.** SHA (FIPS 180) is not held in this version, and a SHA change forced Appendix 5's replacement.
- **Read whole**, all pages of the scan's OCR layer, plus Change Notice 1. The example values in Appendix 5 were not run.
