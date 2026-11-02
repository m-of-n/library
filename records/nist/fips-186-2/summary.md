---
schema: "library-summary/v1"
id: fips-186-2
record: fips-186-2
type: summary
updated: "2026-11-01"
---

# FIPS 186-2: Digital Signature Standard (DSS), 2000

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `historic`: withdrawn or superseded (CSRC) |
| **Authors** | National Institute of Standards and Technology |
| **Published** | 2000-01-27, effective 2000-07-27. Change Notice 1, 2001-10-05. Superseded 2009-06-09 (archive cover of the change-notice edition) |
| **Identifier** | FIPS PUB 186-2 |
| **Source** | https://csrc.nist.gov/files/pubs/fips/186-2/upd1/final/docs/fips186-2-change1.pdf |
| **Digest** | `sha256:bad948fd…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

FIPS 186-2 admits a third algorithm: ECDSA, by reference to ANSI X9.62 (§8), alongside DSA and RSA under X9.31 (§7). Its new content is Appendix 6, the recommended elliptic curves for federal use: five prime-field and five binary-field sizes, keyed to symmetric strengths, with generation and verification procedures for pseudo-random curves. Change Notice 1 then narrows it: DSA's L should be 1024 only, and legacy RSA and Rabin-Williams moduli at least 1024 bits. It also reports an attack by Bleichenbacher on non-uniformity in the Appendix 3 generators, with a 2^64 work factor from 2^22 signatures, and either caps a key at 2 million signatures or modifies the generators.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The 2001 notice is a clean case of a nonce-bias attack on a deployed standard |
| Cryptography | `core` | Origin of the NIST curves |
| This project | `none` | Superseded. Current curves are in `sp-800-186` |

It bears on no open `DEC-*` or `R-*`, and `bears_on` is empty on purpose: a superseded standard. `fips-186-5` carries the live bearing.

## Implementations

Not searched: this standard is superseded. See `fips-186-5`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `spec` is inside FX-1's type scope, and extraction would owe the full artifact set, but this superseded version was not extracted and no issue owns it. The PDF stays in `.cache/` and is not committed.

## Limits

- **RSA and ECDSA are by reference.** §§7 and 8 are two sentences each. X9.31 and X9.62 are not held and were not read.
- **Its own text disagrees about the count.** §1 prescribes three algorithms, and §2 still says two: a leftover from `fips-186-1`, not a change of scope.
- **The attack is known here only as the notice reports it.** The notice spells the name Bliechenbacher and cites a press article. The attack itself was not read.
- **Dates need care.** CSRC gives 2001-10-05 for the first edition, when the change-notice edition replaced it. The change-notice edition's cover gives 2009-06-09. The first edition's cover says superseded on October 5, 2001 and points to 186-3, which skips a step.
- **Read by section.** Read: front matter, §§1 to 3, §§7 and 8, Appendix 6 opening, the whole of Change Notice 1. §§4 to 6 and Appendices 1 to 5 were checked only for carried-over DSA parameters. Appendices 6.1 to 6.9 were skimmed by heading. Curve values were not verified.
