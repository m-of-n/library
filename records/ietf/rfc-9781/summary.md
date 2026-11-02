---
schema: "library-summary/v1"
id: rfc-9781
record: rfc-9781
type: summary
updated: "2026-11-01"
---

# A Concise Binary Object Representation (CBOR) Tag for Unprotected CBOR Web Token Claims Sets (UCCS)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9781.json` 2026-11-01 |
| **Authors** | H. Birkholz, J. O'Donoghue, N. Cam-Winget, C. Bormann |
| **Published** | 2025-05 |
| **Identifier** | RFC 9781 · DOI 10.17487/RFC9781 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9781.txt |
| **Digest** | `sha256:d8c927ce…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | none found, search 2026-11-01 |

## Overview

RFC 9781 assigns tag 601 to a CWT Claims Set carried without COSE, on the argument that a secure channel can supply what the signature otherwise would (§1, §3). It is scoped hard to RATS: use elsewhere needs its own vetted security discussion, and the secure channel or protocol must define the endpoint roles (§4, §7). Trust ends with the channel, so once a UCCS is out it is ordinary unprotected data, and a forwarder is treated as its origin (§4). Appendix A gives CWT claims the formal CDDL that RFC 8392 lacked.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §4 and §7.1: trust ends at the channel, and evidence in a UCCS cannot support the credentials of the channel that carried it |
| Cryptography | `none` | No cryptography of its own. §7.2 points to RFC 9053 |
| This project | `adjacent` | An analogy for `AclEntry`, not a model |

- **R-M-12** (now `ARCH-0002` P1): tag 601 and its claim keys are registry numbers.
- **R-I-03**: Appendix A's CDDL defines the claims a COSE_Sign1 and CWT export would carry.
- **`AclEntry`** (`ARCH-0001`: unsigned, issuer `Self`, local policy root) has the same shape, and that is all. UCCS gets authority from a channel between two parties. `AclEntry` gets it from being local. Under §4 and §7 this tag could not be reused for it anyway.

## Implementations

**Searched 2026-11-01, none found.** GitHub code search for `uccs cbor 601` returned nothing. A narrow query, so this is not evidence that none exists.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **Channel setup and policy are out of scope** (§4). It defines a tag and conditions, not a protocol.
- **The secure channel is demanding.** §1.1 takes a definition including mutual authentication, integrity and confidentiality. Replay protection is added separately through a nonce claim.
- **Not usable outside RATS without new security work** (§4, §7).
- **Errata.** Search on 2026-11-01 found none.
- **Read scope.** Whole RFC from the cached `.txt`, including Appendices A to C. References only skimmed.
