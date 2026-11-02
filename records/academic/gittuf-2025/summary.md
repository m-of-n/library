---
schema: "library-summary/v1"
id: gittuf-2025
record: gittuf-2025
type: summary
updated: "2026-11-01"
---

# Rethinking Trust in Forge-Based Git Security

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | white-paper (peer-reviewed; the library has no closer value) |
| **Authors** | Aditya Sirish A Yelgundhalli, Patrick Zielinski, Reza Curtmola, Justin Cappos |
| **Published** | 2025-02-24, Network and Distributed System Security (NDSS) Symposium |
| **Identifier** | `10.14722/ndss.2025.241008` |
| **Source** | https://www.ndss-symposium.org/wp-content/uploads/2025-1008-paper.pdf |
| **Digest** | `sha256:b86ce3bf…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Forges enforce repository policy, but no one can verify that they did, so a forge is a non-verifiable trusted third party. gittuf moves policy into the repository as signed metadata: a threshold-signed root of trust and rule files saying which keys may write to which branches, tags and files, with namespaced delegations. A Reference State Log, an append-only signed log kept in a Git ref, records every push. Any client can then verify every change against the policy in force at that point, so one honest verifier is enough to catch a violation. The cost is reported as under 4% storage and under 0.59 seconds per push on Git and Kubernetes.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Removes the forge as sole arbiter. Threats T1 to T3 cover policy weakening, log tampering and enforcement subversion (§III) |
| Cryptography | `adjacent` | Uses existing Git signing keys, or Gitsign identities. No new primitive |
| This project | `core` | An object saying who may write what, verified by every client, with thresholds and delegation |

- **R-M-06**: root and rule files carry thresholds, so no single owner changes policy.
- **R-M-10**: delegations are explicit and scoped by namespace.
- **R-M-05**: verification replays an ordered log against the policy in force, which is deterministic composition over an ordered set, in another domain.
- **Topic**: this is the most direct answer to the entitlement gap in the batch. Against takeovers like event-stream or xz it would help only where a threshold was configured, and the paper's text names neither incident.

## Implementations

**Searched 2026-11-01.** GitHub repository metadata checked.

| Name | Kind | License | URL |
|---|---|---|---|
| gittuf | open source, Git security | Apache-2.0 | https://github.com/gittuf/gittuf |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A paper has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **Authorised insiders still win.** §V says a threshold of privileged developers can weaken policy, with visibility and recovery as the answer. A patient maintainer takeover in the style of `cox-2024-xz-timeline` is not stopped by a policy that person legitimately holds.
- **Freeze attacks are out of scope** (§III). The paper relies on out-of-band communication to notice stale state.
- **Partial adoption loses the log.** §VII says gittuf needs all developers to adopt it to meet all of its goals.
- **Hash agility is future work.** §VII lists moving Git off SHA-1 as planned, so policy here still sits on Git's object identity.
- **One repository.** Cross-repository policy is listed as future work in §VII.
- **Read scope.** Abstract, §I (opening), §III, §IV.A and the opening of §IV.B, the opening of §V, the table heading of §VI, §VII and §IX were read through text extraction. Most of §IV, the attack evaluation in §V.B, the runtime numbers in §VI and §VIII were not read closely. The storage and latency figures above are the abstract's.
