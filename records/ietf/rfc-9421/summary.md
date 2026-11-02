---
schema: "library-summary/v1"
id: rfc-9421
record: rfc-9421
type: summary
updated: "2026-11-01"
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
| **Digest** | `sha256:61265578…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

HTTP lets intermediaries transform messages, so a signature over exact bytes would often break, while TLS covers only one connection (§1). This RFC signs selected components of a message: signer and verifier each derive a signature base from the message they hold, under rules strict enough that allowed transformations do not change the result (§1, §1.3). It is therefore a detached signature that **rebuilds what was signed at verification time**. The cost is stated plainly: unsigned parts can be altered (§7.2.1), content is not covered unless a digest field is signed and then separately checked (§7.2.8), and an implementation must get field processing exactly right to avoid canonicalization attacks (§7.5.5). §1.4 makes each application responsible for choosing what is covered.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Request-level authenticity across intermediaries |
| Cryptography | `core` | Defines a signature base and registers algorithms |
| This project | `adjacent` | A counter-example to R-O-05, and a dependency of a neighbouring draft |

- **R-O-05** (proposed, ARCH-0001-PROPOSAL v0.2.0): the verifier reconstructs signed input from an untrusted message, which is what R-O-05 forbids. HTTP forces this because the message is transformed in transit, a constraint our objects do not have. It shows when the opposite design is justified.
- **R-O-03**: the derivation rules are cited in the specification and not invented per application, and §7.5.2 recommends avoiding application-specific canonicalization.

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

- **It says who signed, not what they may do.** `draft-hamr-oauth-agent-delegation` starts from that gap.
- **It is not a complete protocol.** §1.4 lists what every application must decide, including keys, algorithms and required components.
- **Signature replay is covered in §7.2.2**, which was not read, so no claim is made here.
- **Errata not read.** The search lists 2 entries.
- **Read scope.** §1, §1.3, §1.4, §7.2.1, §7.2.8, §7.5.2 and §7.5.5 were read, and the section list was reviewed. The derivation rules in §2, including the signature base in §2.5, were **not** read, so the statements here about how a base is built rest on §1 and §7.
