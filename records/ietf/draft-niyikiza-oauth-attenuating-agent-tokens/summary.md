---
schema: "library-summary/v1"
id: draft-niyikiza-oauth-attenuating-agent-tokens
record: draft-niyikiza-oauth-attenuating-agent-tokens
type: summary
updated: "2026-11-05"
---

# Attenuating Authorization Tokens for Agentic Delegation Chains

|  |  |
|---|---|
| **Type** | draft (individual) |
| **Maturity** | `draft`: individual Internet-Draft, Active, no working group, per datatracker 2026-11-01, re-checked 2026-11-05 |
| **Authors** | N. A. Niyikiza |
| **Published** | 2026-10-26 |
| **Identifier** | draft-niyikiza-oauth-attenuating-agent-tokens-02 |
| **Source** | https://www.ietf.org/archive/id/draft-niyikiza-oauth-attenuating-agent-tokens-02.txt |
| **Digest** | `sha256:a7e23c35…` (full value in `record.yaml`), fetched 2026-11-01, re-verified 2026-11-05 |

## Overview

AATs are holder-derived, offline-verifiable tokens that carry tools and typed argument constraints, built on a RAR profile (§1). §1.3 is the passage this topic needs. It describes SPKI's authority as the intersection of a chain's tags, and then says AATs carry the same ideas with narrowing by a subsumption relation, so that each hop is checked and the leaf states the authority exercised. It draws the same contrast with UCAN, whose arguments must satisfy every delegation's policy, while an AAT enforcement point evaluates only the leaf's constraints. The cost is stated in §4.1: argument spaces are typically infinite, so subsumption is structural and conservative, and some valid narrowings are rejected. §9.2 calls this I4 rule the draft's main contribution.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Explicit invariants and a threat model that names what it misses |
| Cryptography | `adjacent` | JWS with holder-bound PoP; adds no primitive |
| This project | `core` | Direct evidence on reduction versus containment |

- **DEC-004, R-M-08**: §4.5 is a closed table of valid (parent, derived) constraint pairs, and every other pair is rejected unless a registered extension type declares it (§5.1). It is a useful model for a tag profile under R-M-08, and it shows the choice between intersecting and checking subsumption.
- **R-M-10**: there is no boolean delegation flag. The equivalent is depth: §4.3 makes a token terminal when `del_depth` equals `del_max_depth`, so a root with `del_max_depth: 0` cannot be delegated.
- **R-O-02**: §9.8 defines no revocation and says short life bounds exposure. §9.4 notes that a stolen holder key exposes every token bound to it.
- **R-O-05** (proposed): §3.5 requires verification over the signing input exactly as presented, with no re-serialization or canonicalization, which matches R-O-05. JCS is only a SHOULD for producers, for reproducibility of `par_hash`.

## Implementations

**Checked 2026-11-01.** All three repositories are named in Appendix E and were confirmed through the GitHub API. The Mission-Bound reference architecture in Appendix E.3 was not checked. The Appendix states that its entries were supplied by contributors and not verified.

| Name | Kind | License | URL |
|---|---|---|---|
| Tenuo | open source, Rust; encodes in CBOR, JWS of -02 in progress | Apache-2.0 | https://github.com/tenuo-ai/tenuo |
| Warden | open source, Go; independent, implements -01 | Apache-2.0 | https://github.com/IgorKammerGrahl/Warden |
| ARCP | open source, Go; experimental profile | MIT | https://github.com/udaykishore-resu/arcp |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `draft` record owes FX-1 when someone extracts it. No issue owns that extraction yet. No keyword count is given because none has been reconciled.

## Limits

- **Within-scope misuse is out of scope.** §9.1.2 lists actions within constraints, exfiltration through permitted arguments and a malicious root.
- **No re-keying.** §9.4 concedes the property HMAC chains have, and approximates it by destroying a key.
- **No revocation** (§9.8).
- **The leading implementation is not this wire format.** Tenuo encodes in CBOR with its own envelope (Appendix E.1).
- **The comparison in §1.3 is the author's own.** §1.3 states no reason for moving from intersection to per-hop subsumption, beyond the leaf then stating the authority exercised, and reports no evidence that SPKI's approach failed.
- **Relations.** This draft cites `biscuit-spec-3-3` and `draft-asor-wimse-agent-delegation-chain`, and the second cites it back, so no `see_also` is needed.
- **Read scope.** Abstract, §1, §1.3, §3.5, §4.1, §4.2, §4.3, §4.5 (in part: the rules and the top of the table), §9.1.2, §9.2, §9.3, §9.4, §9.8 and Appendix E were read. Issuance, derivation, PoP, §8's algorithm and the other appendices were listed by heading only.
