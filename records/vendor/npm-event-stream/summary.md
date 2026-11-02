---
schema: "library-summary/v1"
id: npm-event-stream
record: npm-event-stream
type: summary
updated: "2026-11-01"
---

# Details about the event-stream incident

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | informational |
| **Authors** | npm, Inc. (adam-npm) |
| **Published** | 2018-11-27, npm, Inc. |
| **Identifier** | https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident |
| **Source** | https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident |
| **Digest** | `sha256:0385796b…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

npm's incident report, published the day after the response. The attacker posed as a maintainer, took over `event-stream`, and added `flatmap-stream` 0.1.1 as a dependency in 3.3.6. The malicious code decrypted a payload using the npm description of the importing package as the key, so it ran only for its target, the Copay wallet's release build, which it altered to harvest account data and private keys from large balances. npm says Copay confirmed the malicious code was deployed on versions 5.0.2 through 5.1.0. npm removed the packages and took ownership of `event-stream`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Social engineering of a maintainer, then a targeted build-time payload |
| Cryptography | `none` | The payload's use of AES keyed on a package description is a cheap and effective targeting trick |
| This project | `adjacent` | Publish authority was legitimately held, so every signature or token check would have passed |

- **R-M-10**: the attacker needed no break, only a transfer.
- **R-M-07**: the payload modified build output downstream of the dependency. A digest of the dependency would have matched exactly what was published.
- Bears on no `DEC-*`.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **Prevention is not covered.** The post advises `npm audit` and upgrades, and says nothing about what would have stopped the takeover.
- **Attribution is absent**, and it makes no statement about how many users were harmed.
- **Read scope.** The whole post was read. The Copay and BitPay sources it quotes were not.
