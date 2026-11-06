---
schema: "library-summary/v1"
id: npm-event-stream
record: npm-event-stream
type: summary
updated: "2026-11-04"
---

# Details about the event-stream incident

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | unset: a vendor blog post has no publisher-stated standing |
| **Authors** | npm, Inc. (adam-npm) |
| **Published** | 2018-11-27, npm, Inc. |
| **Identifier** | https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident |
| **Source** | https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident |
| **Digest** | `sha256:0385796b…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-04 |

## Overview

npm's incident report, posted 2018-11-27. npm's security team was notified on the morning of 26 November and responded that day. The attacker posed as a maintainer, took over `event-stream`, and added `flatmap-stream` 0.1.1 as a dependency in 3.3.6. The malicious code decrypted a payload using the npm description of the importing package as the key, so it ran only for its target, the Copay wallet's release build, which it altered to harvest account data and private keys from accounts holding more than 100 BTC or 1000 BCH. npm says Copay confirmed the malicious code was deployed on versions 5.0.2 through 5.1.0. npm removed `flatmap-stream` and `event-stream@3.3.6` from the registry and took ownership of `event-stream`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Social engineering of a maintainer, then a targeted build-time payload |
| Cryptography | `none` | AES appears only as the payload's targeting trick, keyed on a package description |
| This project | `adjacent` | Publish rights were obtained by social engineering, not by a break, so any check of who published would have passed |

- **R-M-10**: the post says only that the attacker "took over maintainership". It does not say how. `ohm-2020-backstabbers` says ownership was granted on request. An explicit delegation flag would have recorded that grant, not refused it.
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

**Relations.** No `cites`: the post links only a Copay GitHub comment and a press article, and the library holds neither. Three `see_also` edges, each to another account of the same incident:

- `event-stream-issue-116`: the public thread where the compromise was first reported, with early analysis that this post settles.
- `ghsa-event-stream`: the advisory that fixes the affected version ranges. It gives no account of the attack.
- `ohm-2020-backstabbers`: it supplies what this post omits, that the attacker got ownership by asking the original developer for it, and it counts `event-stream` 3.3.6 in its dataset of malicious packages.

## Limits

- **Prevention is not covered.** The post advises `npm audit` and upgrades, and says nothing about what would have stopped the takeover.
- **Attribution is absent**, and it makes no statement about how many users were harmed.
- **Read scope.** The whole post was read. The Copay and BitPay sources it quotes were not.
