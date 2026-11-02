---
schema: "library-summary/v1"
id: rfc-9459
record: rfc-9459
type: summary
updated: "2026-11-01"
---

# CBOR Object Signing and Encryption (COSE): AES-CTR and AES-CBC

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9459.json` 2026-11-01 |
| **Authors** | R. Housley, H. Tschofenig |
| **Published** | 2023-09 |
| **Identifier** | RFC 9459 · DOI 10.17487/RFC9459 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9459.txt |
| **Digest** | `sha256:d9a1cca5…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | none found, search 2026-11-01 |

## Overview

RFC 9459 adds AES-CTR and AES-CBC to COSE for cases where something else, such as a signature on a SUIT firmware manifest, provides integrity (§1). Neither mode is AEAD, so implementations must pair them with an integrity mechanism (§4, §5), and all six identifiers were registered as Deprecated to discourage accidental use. Because these modes cannot authenticate anything, the protected header must be empty and external AAD must be absent (§4, §5, §6). §8 explains the price of having these identifiers at all: an attacker can rewrite an AES-GCM or AES-CCM message's algorithm identifier to one of them and strip or probe the protection.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §8: downgrade by algorithm identifier, keystream reuse, CTR forgery, CBC padding oracles |
| Cryptography | `core` | Full mode definitions and misuse analysis for COSE |
| This project | `none` | Bears on no `DEC-*` or `R-*`. m-of-n does not encrypt |

- It bears on none. The general lesson, ours and not the RFC's, is that a verifier needs an allow-list of algorithms and must not take one from unauthenticated input. `rfc-9864` §7 cites this document for cross-protocol attacks.

## Implementations

**Searched 2026-11-01, none found.** GitHub code search for `A128CTR cose` returned nothing. A narrow query, so this is not evidence that none exists. We have no use for these algorithms.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **`Deprecated` here is a warning, not a ban.** The registry entries stay usable.
- **It does not stop substitution.** §8 describes the attack and `rfc-9864` §7 lists two defences, leaving the choice open.
- **The SUIT manifest it cites as motivation is not held here.**
- **Errata.** Search on 2026-11-01 found none.
- **Read scope.** Whole RFC from the cached `.txt`, except the references.
