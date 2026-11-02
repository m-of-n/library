---
schema: "library-summary/v1"
id: merkle-1980-protocols
record: merkle-1980-protocols
type: summary
updated: "2026-11-01"
---

# Protocols for Public Key Cryptosystems

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | unset: the enum has no value for a peer-reviewed paper or a technical report |
| **Authors** | Ralph C. Merkle |
| **Published** | 1980-04, 1980 IEEE Symposium on Security and Privacy, pp. 122-134 |
| **Identifier** | DOI 10.1109/SP.1980.10006 |
| **Source** | https://www.ralphmerkle.com/papers/Protocols.pdf |
| **Digest** | `sha256:d568120b…` of the PDF (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Merkle compares protocols for key distribution and signatures, and his point is that the protocol, not the primitive, decides what a signature does. Key distribution moves from a central centre (§2) through plain public keys (§3) and Kohnfelder's certificates (§5) to tree authentication, where a hash root replaces the CA's secret key and every user can check a path (§6). For signatures he splits a protocol into signing, checking and dispute resolution, and says that two protocols differing only in dispute rules are different protocols (§7). That matters when a key is lost: the basic protocol leaves the signer responsible, an alternative leaves the recipient holding the risk, and a third adds time-stamps and validity-checks from a central authority (§§9 to 10). §12 proposes signed network software and an operating system that refuses unsigned privileged code.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Key loss, time and dispute are treated as protocol questions |
| Cryptography | `core` | Certificates and tree authentication compared |
| This project | `adjacent` | Early statement of two choices we still face |

`bears_on: R-O-02` through §10: a validity-check is the online status a short-lived design avoids. `bears_on: R-O-04` through §6: a public file authenticated by a hash root. §12's code signing is a precursor of our artifact statements, but it sets no requirement, so it is not claimed against R-M-07.

## Implementations

Not applicable and not searched: this is a protocol survey, not software we would build on. The tree is implemented by the logs in `rfc-9162`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** `paper` is outside FX-1's type scope, and nothing here calls for extraction. The PDF stays in `.cache/` and is not committed.

## Limits

- **§6 buys auditability with rigidity.** It says the file is unalterable, and its strong claim, that only a user's own key can compromise the protocol, rests on that. It cannot add users after publishing the root. `merkle-1989-certified` §6 states that cost directly; append-only logs (`rfc-9162`) came later.
- **§10 is not a design.** It assumes time-keepers and a status agent. Revocation is out of scope beyond that.
- **Brief by design.** An extended version is said to be with CACM; `merkle-1979-thesis` Chapter IX is the longer treatment we hold.
- **Its own §7 notation misleads**, and says so: D_A(m) stands for any signature method.
- **Read whole**, all 13 pages, from the author-hosted scan's OCR layer. No sentence is quoted.
