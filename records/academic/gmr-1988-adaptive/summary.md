---
schema: "library-summary/v1"
id: gmr-1988-adaptive
record: gmr-1988-adaptive
type: summary
updated: "2026-11-01"
---

# A Digital Signature Scheme Secure Against Adaptive Chosen-Message Attacks

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | Shafi Goldwasser, Silvio Micali, Ronald L. Rivest |
| **Published** | 1988-04, SIAM Journal on Computing 17(2), pp. 281-308 |
| **Identifier** | DOI 10.1137/0217017 |
| **Source** | https://people.csail.mit.edu/rivest/pubs/GMR88.pdf |
| **Digest** | `sha256:7ea5eaad…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This paper fixes the vocabulary for signature security. §2.2 orders attacks by what the enemy may ask of the signer, from key-only to adaptive chosen-message, and §2.3 orders breaks from total break down to existential forgery. Most of the earlier schemes in §3, RSA and Rabin among them, fall to some attack in that order. It then gives a scheme from claw-free permutation pairs, or from factoring in particular, and proves that an adaptive chosen-message attacker cannot forge a signature on even one new message (§§6 to 9). A signature is a chain of authentications through a tree, with a random message-independent bridge between tree and message (§8). §4 explains how a proof of equivalence to factoring and resistance to chosen messages can coexist, which folklore had thought impossible.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | It is the standard statement of what a signature must resist. Calls the adaptive attack *"the most severe natural attack an enemy can mount"* (§2.2) |
| Cryptography | `core` | The definition, and a scheme meeting it from a claw-free assumption |
| This project | `adjacent` | Tells us what to demand of a signature suite, without choosing one |

It bears on no open `DEC-*` or `R-*`, so `bears_on` is empty on purpose. It would supply the wording if a requirement ever states the unforgeability a suite must meet. No such requirement exists yet.

## Implementations

Not applicable and not searched: this is a scheme paper, not software we would build on. The result that matters is the definition.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **Forgery means a signature on a message not signed before.** A new signature on an already signed message is outside the §2.3 definition. So non-malleability is not covered; see `rfc-8032` §8.4 for why some systems need it.
- **It says nothing about who holds the key.** The result is about the key, not a person.
- **Disagreement recorded, two `contradicts` edges.** `rsa-1978` says signatures cannot be forged. §3 here shows the unpadded scheme selectively forgeable under a directed chosen-message attack. `rabin-1979-tr212` says forging is as hard as factoring. §§3 to 4 here limit that to a known-message attack, and say padding breaks the proof. Note that §3 and §4 describe a simplified form; the TR already hashes and adds a random suffix, so their total break applies to that simpler form, not to the TR's scheme as written.
- **The basic scheme keeps state**: a counter and the last signature (§8.4). §10 gives Levin's and Goldreich's ways of removing the memory. Not checked in detail.
- **Read scope.** §§1 to 4 and §8 read closely, §10 and §11 read, §§5 to 7 and the proofs of §9 skimmed and not checked. We cite the 1988 text; a claim about later schemes is not in this paper.
- **Assumes factoring or claw-free pairs.** Shor's algorithm (`shor-1997`) removes the factoring instantiation; the paper could not address this.
