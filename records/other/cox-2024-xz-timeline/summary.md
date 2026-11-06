---
schema: "library-summary/v1"
id: cox-2024-xz-timeline
record: cox-2024-xz-timeline
type: summary
updated: "2026-11-04"
---

# Timeline of the xz open source attack

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | unset: a personal blog states no standing |
| **Authors** | Russ Cox |
| **Published** | 2024-04-01, updated 2024-04-03, research!rsc |
| **Identifier** | https://research.swtch.com/xz-timeline |
| **Source** | https://research.swtch.com/xz-timeline |
| **Digest** | `sha256:2fa9c2a7…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-04 |

## Overview

A dated reconstruction of the social engineering. From late 2021 a contributor named Jia Tan sent innocuous patches. From April 2022 accounts that Cox judges likely fake pressured the maintainer, who had said publicly that his resources were too limited. By late 2022 Jia Tan had commit access, and by March 2023 was tagging and building releases. The backdoor arrived in February 2024. Cox calls the attack a watershed, and his timeline shows each grant of access was real: GitHub organisation membership, a shared bug-report address, commit access, release tagging, and control of the project web page.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A dated public account of how authority was obtained |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Authority moved by a series of separate grants, each in a different system, with no single object recording them all |

- **R-M-10**: delegation here was a series of informal grants spread across GitHub, a README, a mail alias and the web host. R-M-10 asks for delegation to be explicit, though an explicit grant given to a patient attacker is still a grant.
- **R-M-06**: by 2023 Jia Tan was tagging and building releases, and the timeline shows no second party in that step. Threshold release would have needed a second, independently compromised or deceived party. The pressure campaign was aimed at the maintainer's stated lack of capacity.
- Bears on no `DEC-*`.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

**Relations.** `cites`: the post links Freund's oss-security message, which is `freund-2024-xz`. Its other links are not held. One `see_also`: `tukaani-xz-backdoor`, the maintainer's first-party statement of who held which keys and hosts, which this outside reconstruction does not have. The edge to `cve-2024-3094` was dropped because that record already cites this one.

## Limits

- **Attribution is unresolved.** Who is behind the accounts is not settled by this post, which treats them as fakes on circumstantial grounds.
- **One superlative is disputed here.** The post says the attack "appears to be the first serious known supply chain attack on widely used open source software". `ohm-2020-backstabbers` and the event-stream records describe earlier attacks on popular open source packages. Whether those count as serious is arguable, so no `contradicts` edge is set.
- **It stops at 2024-03-30.** It records no later analysis, and marks some intent as speculation.
- **Read scope.** The whole post was read, except the external sources it links.
