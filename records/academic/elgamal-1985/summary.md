---
schema: "library-summary/v1"
id: elgamal-1985
record: elgamal-1985
type: summary
updated: "2026-11-01"
---

# A Public Key Cryptosystem and a Signature Scheme Based on Discrete Logarithms

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | Taher ElGamal |
| **Published** | 1985-07, IEEE Transactions on Information Theory IT-31(4), pp. 469-472. Read as a retyped transcription |
| **Identifier** | DOI 10.1109/TIT.1985.1057074 |
| **Source** | https://caislab.kaist.ac.kr/lecture/2010/spring/cs548/basic/B02.pdf |
| **Digest** | `sha256:b903d355…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

ElGamal builds a public key cryptosystem from the Diffie-Hellman exchange (§II) and proposes a new signature scheme (§III), both resting on discrete logarithms over a finite field. A signature on m is a pair (r, s) with alpha^m = y^r r^s mod p, where r comes from a fresh random k and s solves m = xr + ks mod (p-1) (equations 3 to 6). Encryption is randomized, so the same message does not repeat a ciphertext (§V.A). §IV lists attacks, none of which the author believes breaks the scheme, and asks readers to find better ones. Unlike RSA, the signature is not a decryption: there is no trap-door permutation.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Attack 6 (§IV.B) is an early published forgery of a new message from an old signature, or from none |
| Cryptography | `core` | Direct ancestor of DSA and Schnorr; §III's nonce rule is the DSA `k` rule |
| This project | `none` | We would not use this scheme itself |

It bears on no open `DEC-*` or `R-*`. `bears_on` is empty on purpose.

## Implementations

Not applicable and not searched: this is a scheme paper whose descendants are what is deployed, not software we would build on. See `fips-186-5` and `rfc-8032`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **Not the IEEE bytes.** We read a retyped copy on a KAIST course site. It presents itself as the IEEE text and matches its pagination, but it was keyed by someone else. Visible slips, such as *computer* for *compute* and a dropped letter in the Rivest-Shamir-Adleman name, show that it is not a facsimile. Nothing here depends on an exact word, so no sentence is quoted. Equations 3 and 6 were read from the rendered page. They agree in form with `schnorr-1991-jcryptology` §2, which restates them, allowing for its opposite sign convention on the public key.
- **Cannot tell where one error comes from.** Reference [3] gives pp. 472-492 for Diffie-Hellman. The true range is 644-654. This may be the transcriber's or the original's.
- **The CRYPTO '84 version is a different document.** We viewed only its first page, enough to see that the abstract and opening differ. It was not read. The IEEE text's acknowledgement credits a referee for Attack 6.
- **No security proof.** §IV says twice that breaking the scheme is not proved equivalent to discrete logs. `gmr-1984-paradoxical` §IV classes it as existentially forgeable with a generic chosen-message attack and selectively forgeable with a directed one.
- **Signs m directly.** Attack 6's remedy, a one-way function on the message, appears only as an aside. `schnorr-1991-jcryptology` builds the hash in.
- **Read whole**, all four pages. The size and speed figures in §V are 1985 estimates.
