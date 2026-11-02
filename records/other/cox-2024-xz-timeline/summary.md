---
schema: "library-summary/v1"
id: cox-2024-xz-timeline
record: cox-2024-xz-timeline
type: summary
updated: "2026-11-01"
---

# Timeline of the xz open source attack

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | unofficial |
| **Authors** | Russ Cox |
| **Published** | 2024-04-01, research!rsc |
| **Identifier** | https://research.swtch.com/xz-timeline |
| **Source** | https://research.swtch.com/xz-timeline |
| **Digest** | `sha256:2fa9c2a7…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

A dated reconstruction of the social engineering. From late 2021 a contributor named Jia Tan sent innocuous patches while accounts Cox judges likely fake pressured the maintainer, who had said publicly that their resources were limited. By late 2022 Jia Tan had commit access, and by March 2023 was tagging and building releases. The backdoor arrived in February 2024. The post argues this is a watershed, and its evidence shows every step was permitted: each grant of access was real.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The best public account of how authority was obtained |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Authority moved by repeated informal grants, with no object recording any of them |

- **R-M-10**: delegation here was a series of unrecorded acts. R-M-10 asks for delegation to be explicit, though an explicit grant given to a patient attacker is still a grant.
- **R-M-06**: one maintainer could release alone. Threshold release would have needed a second, independently compromised or deceived party. The timeline shows pressure aimed at exactly that scarcity.
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

- **Attribution is unresolved.** Who is behind the accounts is not settled by this post, which treats them as fakes on circumstantial grounds.
- **One superlative is disputed here.** The post calls this apparently the first serious known supply chain attack on widely used open source software. `ohm-2020-backstabbers` and the event-stream records describe earlier attacks on popular open source packages. Whether those count as serious is arguable, so no `contradicts` edge is set.
- **It stops at 2024-03-30.** It records no later analysis, and marks some intent as speculation.
- **Read scope.** The whole post was read, except the external sources it links.
