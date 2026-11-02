---
schema: "library-summary/v1"
id: zooko-2001-names
record: zooko-2001-names
type: summary
updated: "2026-11-01"
---

# Names: Decentralized, Secure, Human-Meaningful: Choose Two

|  |  |
|---|---|
| **Type** | article (web essay) |
| **Maturity** | `informational`: self-published essay |
| **Authors** | Zooko Wilcox-O'Hearn |
| **Published** | 2001-10-12 |
| **Identifier** | version 0.9.1 as captured |
| **Source** | Internet Archive capture of zooko.com |
| **Digest** | `sha256:0b871cb2…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The essay divides name-value pairs into self-authenticating ones, which anyone can verify alone, and the rest, which it doubts can be secure across a trust boundary. Since self-authenticating names cannot be memorised, it argues that a namespace cannot be distributed, secure and human-usable all at once. It lists four ways out, and the fourth keeps a secure distributed namespace while a local, loyal agent translates self-authenticating names into readable ones. The claim is a challenge rather than a proof: "I didn't prove that it is impossible to have all three features".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | frames name security, defines no mechanism |
| Cryptography | `none` | relies on hash and signature properties, adds nothing to them |
| This project | `core` | the question of `topics/namespace-governance.yaml` in one page |

- **R-M-02** (a principal may be identified solely by key): this is the essay's self-authenticating case, and it names the cost, that such names are not memorable.
- **R-M-03** and **DEC-003**: the essay's option 4 is a local translation layer, which is the shape of a relative name bound by a key. DEC-003's candidates, a key thumbprint or `did:key`, are all self-authenticating in the essay's sense.

## Implementations

Not applicable. The essay points to Freenet, Mojo Nation, SFS and the Pet Names Markup Language as examples of 2001; none was evaluated.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** whole, version 0.9.1 from a 2001-10-20 capture, plus the summary section of version 0.9.9.0 from a 2013 capture.

- **The title we cite is not the one on the page we hash.** v0.9.1 says "Distributed, Secure, Human-Readable". "Decentralized, Secure, Human-Meaningful" is the 2003 revision, which also lists five alternatives and not four, and recommends strategy #3 with #4 as an optional addition. Later wording should not be attributed to 2001.
- The essay defines security through "some universal policy of name ownership". A key-relative system denies there is one, so it steps around the triangle and does not refute it. R-001 §5.6 makes the same point about SDSI.
- It predates consensus-ledger naming entirely, and it says nothing about what a local agent costs in practice.
