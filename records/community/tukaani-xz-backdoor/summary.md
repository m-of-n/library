---
schema: "library-summary/v1"
id: tukaani-xz-backdoor
record: tukaani-xz-backdoor
type: summary
updated: "2026-11-01"
---

# XZ Utils backdoor

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | informational |
| **Authors** | Lasse Collin |
| **Published** | 2025-01-17, Tukaani Project |
| **Identifier** | https://tukaani.org/xz-backdoor/ |
| **Source** | https://tukaani.org/xz-backdoor/ |
| **Digest** | `sha256:778df86b…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The upstream maintainer's dated statement. It separates authority by key and host: tarballs created by Jia Tan were signed by that account, tarballs signed by Collin were created by Collin, and Jia Tan had access only to things hosted on GitHub, including the `xz.tukaani.org` subdomain. It records the move back to `tukaani.org`, the decision not to rebase away the malicious files, and clean releases on 2024-05-29. The promised article on what can be learned is still unwritten as of the page's last update.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | A first-party account of the trust boundaries, though brief |
| Cryptography | `none` | Mentions signed tarballs only |
| This project | `adjacent` | Shows a project stating after the fact what a signed entitlement should have said in advance |

- **R-M-10**: every statement in *Facts* is an informal delegation scope, written after the incident. Nothing machine-checkable said any of it beforehand.
- **R-M-07**: signed tarballs were signed by a maintainer whose key was legitimately trusted. Verification passes and tells you nothing.

## Implementations

None applicable: this source describes an incident, not something to build on. No search was run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A web source has no FX-1 obligation, and nothing here needed a further artifact.

## Limits

- **A short statement, not an analysis.** It defers to Freund, and to review notes this record does not hold.
- **The harmlessness claim is narrow.** The page says the malicious repository files are harmless without trigger code never included in Git. That is about the repository, and `freund-2024-xz` is about the tarballs.
- **The XZ Utils review notes are not read here.** They would be the better source for what the maintainer found.
- **Read scope.** The whole page was read. Linked pages were not followed.
