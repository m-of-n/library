---
schema: "library-summary/v1"
id: ucan-1-0
record: ucan-1-0
type: summary
updated: "2026-11-05"
---

# User Controlled Authorization Network (UCAN) Specification v1.0.0

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_: working-group spec, no ratification |
| **Authors** | I. Gozalishvili, D. Holmgren, P. Krüger, B. Zelenka (editor B. Zelenka) |
| **Published** | 2026-10-22 |
| **Identifier** | `ucan-wg/spec` @ `8072f3f` |
| **Source** | https://raw.githubusercontent.com/ucan-wg/spec/8072f3f23f451eaa1271269fe763aebcf294f4db/README.md |
| **Digest** | `sha256:b349eece…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

UCAN is delegable authorization with principals named by DID and no authorization server. The spec places itself directly in SPKI's line: Related Work says the core idea and usage pattern are very close to SPKI/SDSI, and the Intuition section says UCAN approximates SPKI with some dynamic features. Its treatment of narrowing is not SPKI's. A capability is `subject x command x policy`. Commands narrow by path prefix, and a policy is a predicate over the arguments of an eventual invocation (core §Command, Delegation §Policy). The sub-spec validates by substituting `args` into the policy and evaluating it (Delegation §Validation), so a verifier tests a concrete call and does not compute an intersection. All UCANs are signed over DAG-CBOR, and other forms are converted to DAG-CBOR for signature validation (§Encoding).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Full delegation and invocation model with a stated threat discussion |
| Cryptography | `adjacent` | Mandates a cryptosuite and canonical signatures, defines no primitive |
| This project | `core` | Same principal model, same SPKI ancestry, different choices on DEC-002 and R-O-05 |

- **DEC-004, R-M-08**: path-prefix commands plus predicates, evaluated per invocation. No intersection operator is defined, and the core spec's only rule across a hop is that a delegated capability be equal or narrower (§Authority, §Attenuation).
- **DEC-002** (accepted, option 5, `ADR-0004`): DAG-CBOR is a restricted deterministic CBOR profile, so it is a neighbour of option 5, but not an endorsement of it. It requires tag 42 for CID links, which option 5's no-tag rule forbids, and it diverges from RFC 8949 §4.2.1 on floats and simple values (`ipld-dag-cbor`). This spec gives no deployment figures.
- **DEC-003**: `did:key` is the one required DID method (§Cryptosuite).
- **R-M-12**: Commands are interpreted by the Subject (§Command), which is close to key-relative meaning, though the `/ucan` namespace is globally reserved.
- **R-O-05** (proposed): **direct conflict.** §Encoding allows presentation in other IPLD forms and conversion for signature validation, so a verifier may canonicalize untrusted input. Our rule forbids exactly that.

## Implementations

**Checked 2026-11-01.** The working group's own repositories were confirmed through the GitHub API. No wider survey was done.

| Name | Kind | License | URL |
|---|---|---|---|
| rs-ucan | open source, Rust | Apache-2.0 | https://github.com/ucan-wg/rs-ucan |
| go-ucan | open source, Go | Apache-2.0 OR MIT (`LICENSE.md`, the Permissive License Stack; the GitHub API reports NOASSERTION) | https://github.com/ucan-wg/go-ucan |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **The version string does not pin the text.** The canonical-signature requirement arrived in October 2026 under the same 1.0.0. Cite the commit.
- **No confinement.** §Security Considerations says UCAN does not offer confinement and that a delegate can sub-delegate without alerting its delegator.
- **Revocation is a sub-spec and only RECOMMENDED** (§Lifecycle).
- **No PITM protection** beyond inspecting the chain (FAQ).
- **`sub: null` powerline is a wide door.** Delegation §Powerline delegates all future authority regardless of subject, which has no SPKI analogue we know of.
- **Read scope.** The core spec was read whole. In Delegation, the Abstract, Introduction, §Validation and §Token Validation were read, and the rest was scanned through its headings and MUST statements. Invocation, Promise and Revocation sub-specs were not read.
