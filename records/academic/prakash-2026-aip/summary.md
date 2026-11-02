---
schema: "library-summary/v1"
id: prakash-2026-aip
record: prakash-2026-aip
type: summary
updated: "2026-11-01"
---

# AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A

|  |  |
|---|---|
| **Type** | paper (preprint) |
| **Maturity** | _unset_: the enum has no value for a preprint |
| **Authors** | Sunil Prakash |
| **Published** | 2026-03-25 |
| **Identifier** | arXiv:2603.24775v1 |
| **Source** | https://arxiv.org/pdf/2603.24775 |
| **Digest** | `sha256:d9b9b610…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

AIP proposes Invocation-Bound Capability Tokens, one append-only chain that combines identity, attenuated authority and provenance (§3.2). It has two wire forms: a signed JWT for one hop and a Biscuit for several (§3.2.1). What it adds to Biscuit is identity resolution through `aip:web` or self-certifying `aip:key` identifiers, MCP and A2A bindings, completion blocks, and restricted policy profiles (§2.13, §3). Its claim is a seven-property gap that no surveyed system fills (§2.12). The attenuation itself is inherited, so narrowing is Biscuit's conjunction of checks.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Applies attenuation to agent protocols; self-reported evaluation |
| Cryptography | `none` | No new cryptography |
| This project | `adjacent` | A user of Biscuit, not a source of new semantics |

- **DEC-004**: §3.5's Simple profile, four fixed Datalog templates that implementations must generate exactly, is one way to keep a rich language interoperable.
- **R-O-05** (proposed): identity documents are signed over the RFC 8785 canonical form (§3.1), so a verifier has to canonicalize to check them, which R-O-05 forbids.

**Disagreement, recorded as `contradicts`.** The §2 survey misdescribes sources we hold. §2.3 calls macaroon caveats simple key-value predicates, while `macaroons-2014` defines caveats as predicates plus third-party caveats. §2.4 calls UCAN nested JWTs with flat URIs lacking conditional policy, while `ucan-1-0` is a DAG-CBOR envelope with a policy language and time bounds. The paper cites a 2024 UCAN reference, so part of this may be age, but the summary of macaroons has no such excuse. The gap claim in §2.12 depends on both.

## Implementations

**Checked 2026-11-01.** §4 gives this repository, which was confirmed through the GitHub API. A search for other implementations found a separate third-party project, MolTrust, that was not assessed.

| Name | Kind | License | URL |
|---|---|---|---|
| aip | open source; reference implementations named in §4 | Apache-2.0 | https://github.com/sunilp/aip |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `paper` record owes FX-1 only if someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **Single-machine evaluation.** §7 says it ran over localhost and has not been in production. The figures in the abstract are from that setting.
- **The 100% rejection result is against the author's own attack set**, in six categories (§1). It says nothing about attacks not tried.
- **Replay and within-scope misuse are not addressed** (§6).
- **Budgets are ceilings, not balances.** §3.4 says the verifier does not track cumulative spend.
- **§6 calls scope narrowing a cryptographic guarantee**, which overstates it: the guarantee comes from Datalog evaluation by the authorizer, as Table 9 says.
- **Read scope.** Abstract, §1, §2.1 to §2.5, §2.12, §2.13, §3.1 to §3.5 and §6 were read, along with the start of §7. §2.6 to §2.11, §3.6 to §3.8, §4 (bar the repository footnote) and §5 were not.
