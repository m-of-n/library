---
schema: "library-summary/v1"
id: gmr-1984-paradoxical
record: gmr-1984-paradoxical
type: summary
updated: "2026-11-05"
---

# A Paradoxical Solution to The Signature Problem

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | Shafi Goldwasser, Silvio Micali, Ronald L. Rivest |
| **Published** | 1984-10, 25th Annual Symposium on Foundations of Computer Science, pp. 441-448 |
| **Identifier** | DOI 10.1109/SFCS.1984.715946 |
| **Source** | https://people.csail.mit.edu/rivest/pubs/GMR84b.pdf |
| **Digest** | `sha256:69370c7a…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This extended abstract defines what it means to attack and to break a signature scheme, then builds one that meets the strongest definition available. Attacks run from a direct attack, with only the public key, to adaptive chosen-message, and breaks from total break to existential forgery (§II). The folklore held that a scheme cannot be both provably as hard as factoring and safe against chosen-message attack, because the reduction could be run against the real signer (§III). The authors defeat this with a random root in the public key: the reduction needs to choose that root, and an attacker cannot (§III.B). The scheme itself uses claw-free pairs of trap-door permutations, randomization, and a tree of authentications (§V), and §VI proves it not existentially forgeable under adaptive chosen-message attack.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Source of the vocabulary for stating what a signature resists |
| Cryptography | `core` | First signature scheme proved secure against adaptive chosen-message attack |
| This project | `adjacent` | Vocabulary only; the scheme is not one we would deploy |

It bears on no open `DEC-*` or `R-*`. `bears_on` is empty on purpose.

## Implementations

Not applicable and not searched: this is a scheme paper, not software we would build on. We know of no reason to deploy this scheme and did not look for one.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **Superseded for most purposes.** `gmr-1988-adaptive` is the journal treatment. It reworks the definitions, adds the machinery of §§5 to 7 and improves the construction. Cite that one.
- **Stateful.** The signer keeps a counter and tree state (§II.A says the scheme is not memoryless), and §VII leaves a memoryless scheme open.
- **The proof here is a sketch.** The lemma in §VI is given as a proof sketch.
- **Only the signature is proved.** Nothing here concerns binding a key to a person.
- **Read whole**, all eight pages, from the author-hosted scan. The text layer is heavily garbled OCR, so the wording here is ours and we quote nothing. The `cites` list was transcribed from that OCR and the reference entries cross-checked against the cleaner list in `gmr-1988-adaptive`; [GMY83] is cited there and in §§I and IV, so it is a `cites` entry, not a `see_also` edge.
