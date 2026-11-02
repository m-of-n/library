---
schema: "library-summary/v1"
id: draft-asor-wimse-agent-delegation-chain
record: draft-asor-wimse-agent-delegation-chain
type: summary
updated: "2026-11-01"
---

# Verifiable Attenuated Delegation for AI Agent Chains

|  |  |
|---|---|
| **Type** | draft (individual) |
| **Maturity** | `draft`: individual Internet-Draft, Active, no working group, per datatracker 2026-11-01 |
| **Authors** | R. Asor |
| **Published** | 2026-10-27 |
| **Identifier** | draft-asor-wimse-agent-delegation-chain-03 |
| **Source** | https://www.ietf.org/archive/id/draft-asor-wimse-agent-delegation-chain-03.txt |
| **Digest** | `sha256:270e28cb…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The draft profiles `rfc-9068` tokens into a chain that any enforcement point can check offline. It starts from a gap: RFC 8693's `act` claim records actors but does not enforce anything across hops (§1.1). Each token carries authority as RAR, a `cnf` holder key and a `par_hash` over its parent's exact signing input (§3, §5). §6 then gives a deterministic verifier, in which step 4 checks that each hop's authority is subsumed by its parent's. §4.3 defines that relation per constraint type, and defines attenuation as a meet of parent and request, so intersection survives at derivation while the verifier checks only containment. §9.7 draws the honest line: verification shows that no hop exceeded the root, never that the root was right.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Complete offline chain verifier with named attacks |
| Cryptography | `adjacent` | JCS, fully specified JOSE algorithms, byte commitment to parent |
| This project | `core` | Nearest modern analogue of 5-tuple reduction |

- **DEC-004, R-M-08**: §4.3 is a closed constraint vocabulary with defined subset rules per type, which is what R-M-08 asks of a tag profile. The rule that an absent constraint means unbounded, and so cannot narrow, is directly reusable.
- **R-M-05**: §6 calls the algorithm deterministic and side-effect free, apart from cumulative constraints.
- **R-M-09**: step 5 enforces monotonic expiry along the chain, which is a containment form of validity intersection.
- **R-O-02**: §9.1 relies on short life plus a status list, and treats an unknown status as a denial (§6 step 7).
- **R-O-05** (proposed): §3 makes the verifier reject bytes that are not exactly JCS. That checks a canonical form and does not repair input, which is closer to R-O-05 than `ucan-1-0`, though a verifier must still re-serialize to compare.

## Implementations

**Checked 2026-11-01.** §11 names attenu-guard (0.22.0) and attenu-guard-ts (0.16.0). PyPI confirms 0.22.0 and links the GitHub organisation. §11 says neither performs holder binding (step 6) or the status list (step 7). No wider survey was done.

| Name | Kind | License | URL |
|---|---|---|---|
| attenu-guard | open source, Python; reference implementation, repository named by PyPI | Apache-2.0 per the draft; the PyPI record states none | https://github.com/attenu-io/attenu-guard |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `draft` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **Parents stay valid.** §9.1 says attenuation does not invalidate the parent, and offers mitigations only.
- **Subsumption is syntactic.** §4.5 says two deployments can verify the same chain and read different meanings. That is an open issue, not a solved one.
- **The implementations lag the text.** §11 reports that the latest independent run of the -02 vectors had 20 passes, 5 failures and 10 declared gaps, and that no run covers all thirty-six -03 vectors.
- **Claim names are shared with `draft-niyikiza-oauth-attenuating-agent-tokens` with different meaning.** That draft's §1.3 says so for `del_max_depth`. The two are stated to converge, and have not.
- **Read scope.** Abstract, §1, §3, §4.3, §4.5, §5, §6 (main steps), §9.1 to §9.3, §9.6, §9.7 and §11 were read. §4.1, §4.2, §4.4, §6.1 to §6.4, §7, §8, §9.4, §9.5 and the appendices were not.
