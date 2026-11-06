---
schema: "library-summary/v1"
id: rfc-9618
record: rfc-9618
type: summary
updated: "2026-11-04"
---

# Updates to X.509 Policy Validation

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard |
| **Authors** | D. Benjamin |
| **Published** | 2024-08 |
| **Identifier** | RFC 9618 · DOI 10.17487/RFC9618 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9618.txt |
| **Digest** | `sha256:d36535f5…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | 1 reported, unverified: Errata ID 9260 (Technical, §3.1), checked 2026-11-04 |

## Overview

RFC 5280's certificate policy validation built a tree that could grow exponentially in path depth, so a small certificate chain could exhaust a verifier (CVE-2023-0464, CVE-2023-23524). RFC 9618 replaces the tree with a policy graph that scales linearly. §1.1 says it does not change the validity status of any path or which policies are valid. §6 lists other mitigations, including verifying signatures first and limiting depth.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | denial of service in a standard's algorithm |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | design lesson for R-M-05 and R-M-08 |

- **R-M-05** (deterministic composition) and **R-M-08** (defined tag intersection): deterministic and well-defined is not enough. An attacker-supplied chain must also not be able to make composition expensive, so a cost bound belongs with these requirements.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** abstract, §1 and §1.1, §3.3, §6, §7, and the section list; the errata page. §4's graph and §5's replacement text were not read, so §1.1's equivalence claim is taken from the RFC, not checked.

- Updates only policy processing. Name constraints have their own cost bugs (`go-nameconstraint-cves`, CVE-2025-58187); that is the reason for the `see_also` edge.
- Errata ID 9260 (Reported 2026-11-01, not yet verified by the RFC Editor) says §3.1 lists the RFC 5280 tree-building steps without §6.1.4 steps (a) and (b), where policy mappings act. It concerns §3's description of the old algorithm, not §5's replacement text. Not checked against RFC 5280 here.
