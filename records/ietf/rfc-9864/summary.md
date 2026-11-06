---
schema: "library-summary/v1"
id: rfc-9864
record: rfc-9864
type: summary
updated: "2026-11-05"
---

# Fully-Specified Algorithms for JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9864.json` 2026-11-01 |
| **Authors** | M.B. Jones, O. Steele |
| **Published** | 2025-10 |
| **Identifier** | RFC 9864 · DOI 10.17487/RFC9864 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9864.txt |
| **Digest** | `sha256:0f9b6dd2…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | none found, search 2026-11-01 |

## Overview

RFC 9864 separates algorithm identifiers that fully determine the operation from polymorphic ones that need the key to say what happens. Protocols negotiate on identifiers alone, so polymorphism breaks them, and WebAuthn had to redefine COSE -8 to mean Ed25519 only (§1). It therefore registers fully specified values for ECDSA and EdDSA (§2), marks ES256, ES384, ES512 and EdDSA Deprecated in COSE (§4.2.2), and tells experts to accept only fully specified registrations from now on (§4.3). It also defines Deprecated and Prohibited for the first time (§4.4). It updates RFC 7518, RFC 8037 and RFC 9053.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | §7: a key must serve one algorithm unless proven safe, and allow-lists can exclude polymorphic combinations (§3) |
| Cryptography | `core` | Changes which identifiers COSE signatures should use |
| This project | `adjacent` | Governs export values if COSE is chosen |

- **DEC-005** is undecided, and this does not decide it. If COSE_Sign1 is chosen, it fixes which identifiers appear.
- **R-I-03**: our inference is that `SPEC-0002` suite 1 (Ed25519) would export as -19, not -8. `R-I-01`'s mapping table should say so. The native model carries no COSE number (`ADR-0004` item 3).

## Implementations

**Searched 2026-11-01.** GitHub code search for `"ESP256" cose`, limited to Go, Rust and TypeScript and capped at five hits each. These two are examples and no survey was done. Libraries named in our other records, such as `veraison/go-cose` and `google/coset`, were not checked for the new values.

| Name | Kind | License | URL |
|---|---|---|---|
| go-webauthn/webauthn | open source, Go | BSD-3-Clause | https://github.com/go-webauthn/webauthn |
| transmute-industries/cose | open source, TypeScript | Apache-2.0 | https://github.com/transmute-industries/cose |

- **go-webauthn/webauthn**: Search hit for ESP256 only; support not assessed.
- **transmute-industries/cose**: Search hit for ESP256 only; support not assessed.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **Deprecated does not mean forbidden.** Under §4.4 the replacement SHOULD be used in new deployments, unless documented operational or regulatory requirements prevent migration. Existing -7 and -8 messages remain verifiable.
- **Polymorphism remains.** ECDH (§6.2) and HSS-LMS (§6.3) are not updated, the latter affecting `rfc-8778`. RSA is left unresolved (§6.1).
- **Encryption identifiers are not deprecated** (§3).
- **Adoption was not measured.** §1 shows that negotiation in WebAuthn relied on -8, and how far it has moved is not known here.
- **Errata.** Search on 2026-11-01 found none.
- **Read scope.** Whole RFC from the cached `.txt`, except the reference entries.
