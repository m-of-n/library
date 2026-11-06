---
schema: "library-summary/v1"
id: veski-2026-capmas
record: veski-2026-capmas
type: summary
updated: "2026-11-05"
---

# CAPMAS: Capability-Based Delegation of Privileges in Multi-Agent Systems

|  |  |
|---|---|
| **Type** | paper (preprint) |
| **Maturity** | _unset_: the enum has no value for a preprint |
| **Authors** | R. M. Veski, R. Guerraoui, D. Froelicher |
| **Published** | 2026-09-06 |
| **Identifier** | arXiv:2609.06500v1 |
| **Source** | https://arxiv.org/pdf/2609.06500 |
| **Digest** | `sha256:fb807f76…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

CAPMAS gives each user query a bounded privilege set, chosen by a contrastive retrieval model, then carries it in macaroons through a chain of agents (Abstract, §6). Each agent can append restrictions, and the IAM verifies the HMAC chain before a call reaches a service (§7). §7 calls the result privilege intersection: the final action must be allowed for every agent on the path. Unlike SPKI, this is not an operation on tags. It arises from caveats that each must hold. The headline gain is removing a call to the IAM at each hop, measured against RFC 8693 (Abstract, §10). A signed nested baseline fares badly on size, because repeated Base64 grows geometrically (§10).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Containment of model failures, under an honest-but-curious assumption |
| Cryptography | `adjacent` | Standard HMAC chain |
| This project | `adjacent` | Performance evidence only; the IAM-centred design does not fit us |

- **DEC-004, R-M-08**: shows the word "intersection" still being used for the property, with the mechanism now conjunction of caveats.

## Implementations

**Checked 2026-11-01.** §9 describes a Python prototype and gives no repository. The library it uses was confirmed through the GitHub API. Paper code was not otherwise searched for.

| Name | Kind | License | URL |
|---|---|---|---|
| pymacaroons | open source, Python; the token library used by §9 | MIT | https://github.com/ecordell/pymacaroons |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `paper` record owes FX-1 only if someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **"Offline" applies to attenuation only.** Verification and final execution go through the IAM (§7), which §11 calls a single point of failure for trust and operation.
- **The threat model excludes malicious agents.** §5 assumes non-malicious agent code, and §8 sketches extensions. In open settings it says asymmetric designs are needed.
- **The signed baseline is a construction chosen by the authors.** Its geometric growth comes from nesting with Base64 (§10), so it does not generalise to flat chains such as `biscuit-spec-3-3`.
- **Plaintext reasoning in caveats leaks** (§11).
- **The scoping model is not an authorization control.** It picks privileges probabilistically, with a tuned top-k (§11). The hard bound is the user's privileges (§7).
- **Read scope.** Abstract, §1 (in part), §5, the start of §6.1, §7, §8, §9, part of §10 and §11 were read. §2 to §4, the rest of §6 and §10, and the appendices were not, and the headline figures are taken from the abstract, not recomputed.
