---
schema: "library-summary/v1"
id: rfc-9421
record: rfc-9421
type: summary
updated: "2026-11-05"
---

# HTTP Message Signatures

|  |  |
|---|---|
| **Type** | rfc (IETF stream) |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9421.json` 2026-11-01 |
| **Authors** | A. Backman, Ed., J. Richer, Ed., M. Sporny |
| **Published** | 2024-02 |
| **Identifier** | RFC 9421 · DOI 10.17487/RFC9421 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9421.txt |
| **Digest** | `sha256:61265578…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-05 |

## Overview

TLS protects only one connection, libraries and intermediaries alter or hide parts of a message, and object-based signatures such as JWS need the exact signed bytes, so HTTP elements must be duplicated into the payload and checked for consistency (§1, §1.3). This RFC signs selected components of a message: signer and verifier each derive a signature base from the message they hold, under canonicalization rules strict enough that many transformations HTTP permits do not break verification (§1, §1.3); others, such as reserializing a covered field, still do (§1.3). It is therefore a detached signature that **rebuilds what was signed at verification time**. The cost is stated plainly: unsigned parts can be altered (§7.2.1), content is not covered unless a digest field is signed and then separately checked (§7.2.8), and an implementation must get field processing exactly right to avoid canonicalization attacks (§7.5.5). §1.4 makes each application responsible for choosing what is covered.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Request-level authenticity across intermediaries |
| Cryptography | `core` | Defines a signature base and registers algorithms |
| This project | `adjacent` | A counter-example to R-O-05, and a dependency of a neighbouring draft |

- **R-O-05** (proposed, ARCH-0001-PROPOSAL v0.2.0): the verifier reconstructs signed input from an untrusted message, which is what R-O-05 forbids. HTTP forces this because the message is transformed in transit, a constraint our objects do not have. It shows when the opposite design is justified.
- **R-O-03**: the canonicalization rules are defined once in the specification (§1 points to §2) rather than per application, and §7.5.2 recommends that applications avoid additional application-specific rules.

## Implementations

**Checked 2026-11-01.** Confirmed through the GitHub API, and the README states conformance to this RFC. No wider survey was done.

| Name | Kind | License | URL |
|---|---|---|---|
| dadrus/httpsig | open source, Go; README states RFC 9421 | MIT | https://github.com/dadrus/httpsig |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **It says who signed, not what they may do.** `draft-hamr-oauth-agent-delegation` builds a delegation chain on top of it.
- **It is not a complete protocol.** §1.4 lists what every application must decide, including keys, algorithms and required components.
- **Replay is mitigated, not prevented.** §7.2.2: a signature over no components can be attached to any message, and even one with sufficient coverage can validate on two similar messages; the defences are wider coverage, the `nonce` parameter, `created`/`expires`, and a fresh nonce requested via `Accept-Signature`.
- **Relations.** `draft-hamr-oauth-agent-delegation` cites this RFC, so the earlier `see_also` edge to it is carried by that record's `cites`.
- **Errata: 2 verified** (checked 2026-11-05). 8102 (editorial) and 8103 (technical) both replace `@signature-input` with `@signature-params`, in the §7.2.8 example and in §7.5.3.
- **Read scope.** §1, §1.3, §1.4, §7.2.1, §7.2.2, §7.2.8, §7.5.2, §7.5.3 and §7.5.5 were read, and the section list was reviewed. The derivation rules in §2, including the signature base in §2.5, were **not** read, so the statements here about how a base is built rest on §1 and §7.
