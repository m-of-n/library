---
schema: "library-summary/v1"
id: merkle-1989-certified
record: merkle-1989-certified
type: summary
updated: "2026-11-01"
---

# A Certified Digital Signature

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | Ralph C. Merkle |
| **Published** | 1990, Advances in Cryptology - CRYPTO '89, LNCS 435, pp. 218-238. Text dates from 1979 |
| **Identifier** | DOI 10.1007/0-387-34805-0_21 |
| **Source** | https://web.archive.org/web/20251011190157id_/https://link.springer.com/content/pdf/10.1007/0-387-34805-0_21.pdf |
| **Digest** | `sha256:a5d71a10…` of an Internet Archive capture (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Merkle gives a practical signature system whose security rests only on a conventional encryption function, so a cipher that is already trusted gives a signature that is "pre-certified" with no new certification effort (§1). It starts from the Lamport-Diffie one-time signature (§3), halves its size by appending a count of zero bits (§4), and reports Winternitz's trade of time for space (§5). The large-public-file problem is solved by tree authentication: hash one-time public keys pairwise up to a single root, and authenticate any leaf with log n values, the authentication path (§6). §7 regenerates those paths in sequence with modest time and memory, and derives the one-time keys from one seed. §2 constructs a one-way hash from the cipher and proves it under two stated properties.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Signature security reduced to a one-way function |
| Cryptography | `core` | Introduces tree authentication and authentication paths for signatures |
| This project | `adjacent` | Tree authentication underlies transparency logs and `rfc-8391` / `rfc-8554` |

`bears_on: R-O-04`: §6's root and authentication path are the structure a SCITT-like transparency service commits to (`rfc-9162`). It does not bear on signature suite choice, which NG3 leaves open.

## Implementations

Not applicable and not searched: this is a method paper, not software we would build on. Standardised descendants are `rfc-8391` and `rfc-8554`; the author's 2012 note names his own later code, which was not examined.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **Stateful.** Each leaf is used once, in order (§7). Nothing here treats what happens if a signer loses its place and reuses a leaf. `rfc-8391` and `rfc-8554` carry that burden.
- **The signature size claim is for 100-bit outputs and a 300-bit-key cipher.** Those are 1979 parameters. Do not reuse the 1 to 3 kilobyte figure.
- **The tree cannot grow.** §6 says no new leaves can be added once computed, and treats this as the reason the clearinghouse need not be trusted. Append-only logs relax it.
- **A 1979 text, printed in 1990 almost unchanged.** The Addendum says: *"The only change (besides formatting) is the author's affiliation."* Its concerns, such as certifying a cipher, are of that date.
- **Differs from `merkle-1979-thesis` Chapter V**, which has no Winternitz section and gives another size.
- **Archive copy.** Read from an Internet Archive capture of Springer's PDF, whole, all 21 pages. The OCR layer garbles some formulas, so the pseudocode in §7 was read for structure and not checked. The author-hosted copy was not compared beyond its 2012 cover note.
