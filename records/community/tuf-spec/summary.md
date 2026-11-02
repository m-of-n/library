---
schema: "library-summary/v1"
id: tuf-spec
record: tuf-spec
type: summary
updated: "2026-11-01"
---

# The Update Framework Specification v1.0.37

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | unset: the source states no standing |
| **Authors** | Justin Cappos, Trishank Karthik Kuppusamy, Joshua Lock, Marina Moore, Lukas Pühringer |
| **Published** | 2026-10-08, The Update Framework project |
| **Identifier** | `https://github.com/theupdateframework/specification tag v1.0.37 @ d4cb70582ba507b9265672792c0fc8a5f390b851` |
| **Source** | https://theupdateframework.github.io/specification/v1.0.37/index.html |
| **Digest** | `sha256:f20fda0d…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

TUF secures software update systems on the assumption that keys will be compromised. Trust is split across roles: an offline root delegates to targets, snapshot and timestamp, each with its own keys and threshold, so a compromise short of a threshold does not reach clients (§1.5.2, §2.1). Targets can delegate full or partial trust further, and a delegation is revoked by signing new metadata without it (§2.1.2). The client workflow in §5 is the heart of the document: fixed start time, root chaining where each new root must meet a threshold of both old and new keys (§5.3), then explicit rollback, freeze and fast-forward checks per role.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A worked threat model of arbitrary installation, rollback, freeze, mix-and-match and key compromise (§1.5.2), enforced step by step in §5 |
| Cryptography | `adjacent` | Threshold counting by unique key (§4.2.1, §5.3). Key objects name a key type and a signature scheme (§4.2.2), so the framework is not tied to one algorithm |
| This project | `core` | Threshold principals, key-relative trust and canonicalisation at verification, all in deployed form |

- **R-M-06**: threshold roles without a CA hierarchy, and §1.5.3 says no authority derives from keys outside the framework.
- **R-O-02**: expiry per role, with the timestamp role as the short-lived one, and revocation by re-signing delegations.
- **R-O-03**: the canonicalisation is cited: *Canonical JSON* in §4.1. §4.1 also lets an implementation use any data format, documented in its POUF.
- **R-O-05**: a direct conflict with the proposed rule. §4.2.1 signs "the canonical form of the metadata", so a client works from the canonical form when it checks a signature, and §4 says unknown fields must be included in that calculation. R-O-05 appears only in ARCH-0001-PROPOSAL v0.2.0, so this is a contrast with a proposed rule.

## Implementations

**Searched 2026-11-01.** GitHub repository metadata checked for license and archive state.

| Name | Kind | License | URL |
|---|---|---|---|
| python-tuf | open source, Python | Apache-2.0 | https://github.com/theupdateframework/python-tuf |
| go-tuf | open source, Go | Apache-2.0 | https://github.com/theupdateframework/go-tuf |
| rust-tuf | open source, Rust | Apache-2.0 | https://github.com/theupdateframework/rust-tuf |
| tuf-conformance | open source, tests | MIT | https://github.com/theupdateframework/tuf-conformance |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Not a threat analysis.** §2.2 says a detailed threat analysis is outside the document's scope.
- **Trust on first use is assumed away.** §5.2 assumes a good root shipped out of band.
- **Entitlement stops at the repository.** Delegation here says which keys may sign which paths in one repository. Target files are opaque (§2), so nothing says the signed thing is good.
- **Equal versions are worded awkwardly.** §5.4's rollback step says the trusted version must be less than the new one, then says equal versions are normal and abort quietly. An implementer has to read the whole step.
- **Read scope.** §1, §2 to §2.2, §4.1 to §4.2.2 and §5.1 to §5.4 were read. §3, §4.3 onward, §5.5 onward and §6 were not read line by line, including `root.json` fields, consistent snapshots and key management. The Mercury paper §5.3 cites was not read.
