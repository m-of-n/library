---
schema: "library-summary/v1"
id: diffie-hellman-1976
record: diffie-hellman-1976
type: summary
updated: "2026-11-01"
---

# New Directions in Cryptography

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | Whitfield Diffie, Martin E. Hellman |
| **Published** | 1976-11, IEEE Transactions on Information Theory IT-22(6), pp. 644-654 |
| **Identifier** | DOI 10.1109/TIT.1976.1055638 |
| **Source** | https://www-ee.stanford.edu/~hellman/publications/24.pdf |
| **Digest** | `sha256:03fa2f49…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Diffie and Hellman argue that two problems block the move to teleprocessing: key distribution needs a secure channel, and conventional authentication cannot settle a dispute between sender and receiver (§I, §II). They propose public key cryptosystems, in which computing the deciphering key from the enciphering key is infeasible, and a public key distribution system based on exponentiation modulo a prime (§III). They then state the requirement that all later signature work inherits: a message anyone can check and nobody else, including the recipient, could have produced (§I, §IV). §IV shows that any public key cryptosystem yields signatures by "deciphering" the message, and gives Lamport's one-time scheme as a partial solution that needs only a one-way function. §V orders the problems by difficulty and introduces trap doors, and §VI asks whether complexity theory can replace certification by cryptanalytic attack.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Defines dispute as a threat, alongside eavesdropping and injection (§II) |
| Cryptography | `core` | Origin of public key cryptosystems and of the discrete-exponentiation key exchange |
| This project | `adjacent` | Background to every signature suite we might choose |

It bears on no open `DEC-*` or `R-*`, so `bears_on` is empty on purpose. §III's warning that the public file must be protected, *"It is crucial that the public file of enciphering keys be protected from unauthorized modification."*, is the problem R-M-02 sidesteps by naming a principal by its key, but this paper does not reach that design and we do not claim it as support.

## Implementations

Not applicable and not searched: this is a theory paper, not software we would build on. Concrete signature schemes are in `rfc-8032` and `fips-186-5`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **Read whole**, from the author-hosted scan of the IEEE print. The text layer is OCR, so equations were read for sense and are not quoted here.
- **No public key cryptosystem is given.** §III says the problem is still largely open, and its matrix example is called useless. RSA came later (`rsa-1978`).
- **The signature is not defined against an attacker.** The paper states a goal, not a security model. Signing by inverting a trap-door function directly is the construction `gmr-1988-adaptive` §3 shows is existentially forgeable with a key-only attack.
- **Security of the key exchange is conjectural.** §III has no proof that the system is secure when logs are hard. The q^(1/2) estimate for logs is the 1976 best known, and `elgamal-1985` §V already reports subexponential algorithms.
- **Identity is assumed.** The public file is presumed to authenticate users. How it does so is not settled here; see `merkle-1980-protocols` for certificates and tree authentication.
