---
schema: "library-summary/v1"
id: rfc-8152
record: rfc-8152
type: summary
updated: "2026-11-01"
---

# CBOR Object Signing and Encryption (COSE)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, **obsoleted by RFC 9052 and RFC 9053**, confirmed in `rfc8152.json` 2026-11-01 |
| **Authors** | J. Schaad |
| **Published** | 2017-07 |
| **Identifier** | RFC 8152 · DOI 10.17487/RFC8152 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8152.txt |
| **Digest** | `sha256:bd44c8c3…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | 6 verified, 2 reported, 1 held (see Limits) |

## Overview

The first COSE specification, redoing JOSE for CBOR while revisiting its choices (§1, §1.1). Every message is an array of a protected header in a byte string, an unprotected header map and the content, followed by type-specific elements, with six message types identified by context or CBOR tag (§2). A signature covers a Sig_structure, not the message as sent (§4.4). Canonical encoding is required only for that to-be-signed structure and its peers, by reference to RFC 7049 §3.9 (§14). Which algorithms and services apply is left to an application profile (§15). This single document also defined the algorithms, including ES256 (-7) and EdDSA (-8), which RFC 9864 later deprecated.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §17 sets out key-to-algorithm binding and the trust decision before acting on a key |
| Cryptography | `core` | Defines the structures and algorithms, in their original form |
| This project | `adjacent` | History for DEC-005. The current rule is `rfc-9052` |

- **DEC-005**: read only to see what changed. RFC 9052 §1.2 lists the split into two documents and the removal of countersignatures to RFC 9338, and RFC 9052 §9 replaces the RFC 7049 reference with alignment to RFC 8949 §4.2.1. Anything that still cites this RFC for encoding inherits the older rule described in `rfc-7049`.

## Implementations

**Not searched for this record.** It is obsolete, so what to build on belongs to `rfc-9052` and `rfc-9053`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **Obsolete.** Cite `rfc-9052` and `rfc-9053`.
- **Errata matter here.** 6 verified: EID 5066 adds COSE_KDF_Context to §14's list, EID 6209 fixes a missing "not" in §9 on MACs and third parties, and EIDs 5545, 5650 and 5669 fix registry references. 2 reported, including EID 6597 on which KDF §12.5.1 means. 1 held.
- **§14 scopes encoding to what is signed, not to messages.** It does not make a COSE message deterministic, so a byte-identical message cannot be assumed.
- **Whether deployed stacks still follow this text was not measured.**
- **Read scope.** §1, §1.1, §2, §4.4, the openings of §8 and §8.2, §14, §15 and §17 of the cached `.txt`, plus RFC 9052 §1.2 and §9 for the comparison. §3, §5 to §7, §9 to §13, §16 and the appendices were not read.
