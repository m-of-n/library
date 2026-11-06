---
schema: "library-summary/v1"
id: biscuit-spec-3-3
record: biscuit-spec-3-3
type: summary
updated: "2026-11-05"
---

# Biscuit Specification v3.3

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_: no ratification statement on the page |
| **Authors** | none named on the page |
| **Published** | 2025-10-21 |
| **Identifier** | no number; `eclipse-biscuit/biscuit` @ `3bf6eb5` |
| **Source** | https://doc.biscuitsec.org/reference/specifications.html |
| **Digest** | `sha256:d7ec7840…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

A Biscuit is an append-only list of signed blocks. The authority block grants rights as Datalog facts, and later blocks add checks that restrict them. Any holder can append a block offline, and an authorizer needs only the root public key (Overview, Cryptography). Each block signs the next block's public key, and the token carries the last private key, or a signature of the last block if it has been sealed (Cryptography). As with macaroons, nothing computes a resulting authority. The authorizer runs Datalog and every check must succeed. Scopes do the work that intersection does elsewhere: by default a block's facts are invisible to checks and policies from the authorizer, so a later block that asserts a new right has no effect (Scopes).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Offline attenuation with a defined authorization procedure |
| Cryptography | `core` | Ed25519 or P-256 signature chain with ephemeral per-block keys |
| This project | `adjacent` | Studied, not adopted. Closest peer to `AuthzCert` chains in the token world |

- **DEC-004, R-M-08**: Datalog with expressions is a fourth kind of answer for DEC-004. It meets R-M-08 by avoiding it, since there is no tag intersection to define.
- **R-M-05**: the procedure is deterministic given facts, rules and an ordered policy list (Authorization process). Evaluation depends on ambient facts from the authorizer, unlike reduction over certificates alone.
- **R-M-10**: there is no delegation flag. Sealing is the only way to stop further attenuation (Overview).
- **R-O-05** (proposed, ARCH-0001-PROPOSAL v0.2.0): each signed payload includes the serialized block bytes, and those bytes are carried in the token, so no canonicalization runs at verification. Note the order: the outer protobuf is decoded before the signature check (Deserializing the token).

## Implementations

**Checked 2026-11-01.** Repositories confirmed through the GitHub API; `biscuit-auth/*` now redirects to `eclipse-biscuit/*`. Other language ports were not surveyed.

| Name | Kind | License | URL |
|---|---|---|---|
| biscuit-rust | open source, Rust | Apache-2.0, from `biscuit-auth/Cargo.toml`. The repo has no root LICENSE file, so the GitHub API reports none | https://github.com/eclipse-biscuit/biscuit-rust |
| biscuit spec and samples | specification repository with sample tokens | Apache-2.0 | https://github.com/eclipse-biscuit/biscuit |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **No identity, no transport, no revocation service.** The spec generates revocation identifiers (block signatures) and leaves the list to the authorizer (Revocation identifiers).
- **Bearer by default.** The token carries the private key needed to extend it, so possession is the authorization (Cryptography). Holder binding is left to checks.
- **Datalog needs an engine at every verifier.** `draft-asor-wimse-agent-delegation-chain` §1.1 sets Biscuit aside as a non-IETF wire format, "protocol buffers with an embedded Datalog engine". Resource limits on evaluation were not found in the sections read.
- **Version 0 signatures are deprecated, and the external form is unsupported.** Implementers need the version 1 payload (Signed payload generation).
- **Read scope.** Read: Introduction through Grammar, Scopes, Checks, Authorizer, Format, Cryptography through Optional external signature. Not read: expression semantics and opcodes, the symbol table and public key table rules, and the Appending procedure. The sample tokens were not run.
