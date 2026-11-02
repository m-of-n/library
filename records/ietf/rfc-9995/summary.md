---
schema: "library-summary/v1"
id: rfc-9995
record: rfc-9995
type: summary
updated: "2026-11-01"
---

# CBOR Object Signing and Encryption (COSE) Hash Envelope

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9995.json` 2026-11-01 |
| **Authors** | O. Steele, S. Lasker, H. Birkholz |
| **Published** | 2026-07 |
| **Identifier** | RFC 9995 · DOI 10.17487/RFC9995 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9995.txt |
| **Digest** | `sha256:bdc665c4…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | none found, search 2026-11-01 |

## Overview

RFC 9995 makes a digest the payload of a COSE signature, so the signature can be checked without the original data (abstract, §1). Three protected header parameters describe it: 258 for the hash algorithm, 259 for the preimage's content type and 260 for a location hint (§3). Label 3 is banned, so `content_type` cannot be confused with the preimage's type (§4). The signature covers these headers and the digest, not the artifact, and §5.3 leaves checking the preimage as something a verifier can choose to do.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Sound for what it signs. The artifact binding holds only for verifiers that hash the preimage (§5.3) |
| Cryptography | `adjacent` | Uses COSE signing unchanged. §5.1 only asks for algorithm strength to match |
| This project | `adjacent` | Direct prior art for R-M-07 under a COSE export |

- **R-M-07**: this meets "bind at least one content digest" under a COSE export, with the algorithm protected. It carries one digest per envelope, so several digests would need several envelopes or a structured payload.
- **DEC-005**: an input to the COSE_Sign1 option, not a decision. `ADR-0004` keeps COSE an export envelope, and the required tag 18 in §4's CDDL stays at that boundary.
- **R-I-03**: a candidate export form, subject to the R-I-01 mapping table.

## Implementations

**Searched 2026-11-01.** GitHub code search for `payload_preimage_content_type` and `payload-hash-alg`, capped at six hits each. These are the libraries among the hits, and no survey was done. `Azure/corim` and `microsoft/scitt-verifier` also matched.

| Name | Kind | License | URL |
|---|---|---|---|
| veraison/go-cose | open source, Go | MPL-2.0 | https://github.com/veraison/go-cose |
| microsoft/CoseSignTool | open source, .NET | MIT | https://github.com/microsoft/CoseSignTool |
| web-auth/cose-lib | open source, PHP | MIT | https://github.com/web-auth/cose-lib |

- **veraison/go-cose**: `hash_envelope.go` matched the search; conformance not assessed.
- **microsoft/CoseSignTool**: Hash-envelope code in CoseIndirectSignature; conformance not assessed.
- **web-auth/cose-lib**: `src/Structure/HashEnvelope.php`; conformance not assessed.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **It is not a detached payload.** The digest is usually inline (§4), and verification needs no preimage. `mofn` `research/0001-cbor/report.md` calls this detached-payload digest signing, and this record's old usefulness note did too. It can still be detached like any COSE payload (§4), but what is then detached is the digest.
- **Its own example uses a deprecated algorithm.** §4.1 signs with ES384 (-35), which `rfc-9864` §4.2.2 deprecated in 2025. The example is informative, so no `contradicts` edge is set. Do not copy it.
- **The names differ.** §4's CDDL uses `payload_hash_alg`, `payload_preimage_content_type` and `payload_location`. §6 and the IANA registry use `payload-hash-alg`, `preimage-content-type` and `payload-location`.
- **Loose ends.** §4's example sets the preimage type to `bstr`, which is neither form its CDDL allows. §5.2 scopes in COSE_Sign and COSE_Mac, but the CDDL and the §6 entries describe COSE_Sign1 only. The CDDL also marks `alg` optional.
- **No hash-agility or collision guidance beyond §5.1.**
- **Errata.** Search on 2026-11-01 found none.
- **Read scope.** Whole RFC from the cached `.txt`.
