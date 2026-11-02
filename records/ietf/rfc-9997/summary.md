---
schema: "library-summary/v1"
id: rfc-9997
record: rfc-9997
type: summary
updated: "2026-11-01"
---

# YANG-CBOR: Allocating SID Ranges for Private Enterprise Number (PEN) Holders

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9997.json` 2026-11-01 |
| **Authors** | C. Bormann |
| **Published** | 2026-07 |
| **Identifier** | RFC 9997 · DOI 10.17487/RFC9997 · CoRE WG |
| **Source** | https://www.rfc-editor.org/rfc/rfc9997.txt |
| **Digest** | `sha256:2ce14ff5…` (full value in `record.yaml`), verified 2026-11-01 |
| **Errata** | none: errata search returned no matching errata, 2026-11-01 |

## Overview

RFC 9997 gives every Private Enterprise Number holder a block of YANG SIDs with no further request. It reserves two mega-ranges and defines the block arithmetically: PEN ppp ppp controls 3pp ppp p00 000 to 3pp ppp p99 999, and PENs below 100 000 also get a 32-bit-sized block (§1, §4). It works because it reuses a registry that exists. §3 calls the result extremely-low-threshold, with zero interaction, on top of a PEN registry that already has a low-threshold process.

§3 is frank about what that buys. There is no way to discover the module behind a SID, and the obscurity may be what a holder wants. §5 is the sentence for us: a PEN inside a SID *"is not an indicator of provenance"*. The number says who may allocate, and nothing on the wire proves who did.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §5 limits what the identifier proves |
| Cryptography | `none` | No cryptography. The range is not bound to a key |
| This project | `adjacent` | The closest prior art to R-M-12 in this batch, and the contrast with it |

- **R-M-12** (relocated to `ARCH-0002` P1 by `ADR-0001`): this is a namespace by delegation without a per-entry registry, which is P1's goal reached by a different route, and it stops exactly where P1 says such routes stop. P1 says private ranges give *escape from a registry, not a namespace*. RFC 9997 goes further than a private range, since a block has an owner, and the collision P1 names is prevented for parties who follow the rule. But the owner is a registry entry and not a cryptographic root, so §5 has to disclaim provenance. P1's `(defining key, local label)` needs no such disclaimer, because the key is in the name and the statement is signed. It is the same shape `ARCH-0002` P1.1 records for a COSE `kid`: an owner with no cryptographic root.

The arithmetic checks: PEN 32473 gives 303 247 300 000 and 3 324 730 000, matching the ranges §4 reserves for documentation.

## Implementations

**Searched 2026-11-01.** A web search found the RFC and its mirrors, and no tool or deployment using PEN ranges. A GitHub repository search found the draft and RFC source repositories (`core-wg/sid-pen`, `rfc-editor-drafts/rfc9997`) and no code. GitHub code search for `rfc9997`, first 10 hits, was all mirrors and bibliographic data. `pyang` generates SID files, per the `pycoreconf` README, and whether it knows these ranges was not checked.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **It proves nothing about origin** (§5), and it defines no discovery (§3).
- **It depends on IANA twice:** the PEN registry for ownership and the mega-range registry for the space. §4 rests the 10-year capacity requirement on IANA's PEN operation.
- **The 32-bit space runs out.** §3 expects PENs below 100 000 to be exhausted by or around 2040.
- **It is young.** Published 2026-07, so §3's dismissal of a land grab is an argument from PEN history, not observation of this mechanism.
- **RFC 9595 is not held.** The mega-range policy (§6.3 of that document) was read only as this RFC reports it.
- **Read scope.** The whole document, RFC Editor `.txt`.
