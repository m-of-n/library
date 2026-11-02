---
schema: "library-summary/v1"
id: rfc-8812
record: rfc-8812
type: summary
updated: "2026-11-01"
---

# CBOR Object Signing and Encryption (COSE) and JSON Object Signing and Encryption (JOSE) Registrations for Web Authentication (WebAuthn) Algorithms

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc8812.json` 2026-11-01 |
| **Authors** | M. Jones |
| **Published** | 2020-08 |
| **Identifier** | RFC 8812 · DOI 10.17487/RFC8812 · COSE WG |
| **Source** | https://www.rfc-editor.org/rfc/rfc8812.txt |
| **Digest** | `sha256:7f49c0c7…` (full value in `record.yaml`), verified 2026-11-01 |
| **Errata** | none: errata search returned no matching errata, 2026-11-01 |

## Overview

RFC 8812 exists because deployed WebAuthn and CTAP implementations already used algorithms COSE had no number for, so it registers them after the fact: RS256, RS384, RS512 and RS1 in COSE (§2), and ES256K plus the secp256k1 curve in both COSE and JOSE (§3, §4). None is recommended. Every algorithm is registered `No` except RS1, which is `Deprecated`. RS1 is the telling case: §5.3 says a number is registered for SHA-1 signatures anyway, because deployed TPMs still use them and WebAuthn must represent those attestations, while new COSE applications and protocols are told not to use it (a MUST NOT, §5.3).

So a registry here records deployment as much as it endorses anything. A code point's existence says nothing about whether its algorithm should be used, and the `Recommended` column is what carries that judgement.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §5.4 states a key confusion with no general fix. §5.3 retains SHA-1 for a deployment reason |
| Cryptography | `adjacent` | Algorithm registrations only, with nothing new designed |
| This project | `adjacent` | Not native, per `ADR-0004`. A data point for two decisions |

- **DEC-003** (accepted, `ADR-0005`): §5.4 warns that a secp256k1 key can be mistaken for a P-256 key because *"their representations are the same except for the "crv" value"*, and says, citing RFC 8152 §8.1.1, that there is currently no way to deal with this attack except restricting the curves used. That is the class of collision `ADR-0005` item 4 assigns to the suite registry rule (`SPEC-0002` §12.3). Neither curve is a KSA suite, so no present `kid` is affected. It is evidence that the rule answers a real hazard.
- **DEC-005** (open): if COSE_Sign1 is the export envelope, these identifiers are values it could carry. §3.3 has to forbid secp256k1 under COSE `ES256` by rule, where JOSE's `ES256` is defined for P-256 only.

## Implementations

**Searched 2026-11-01** (web, then the source of two named libraries). Neither library below implements the whole RFC: no `ES256K` entry was found in either file read. No wider survey was done.

| Name | Kind | License | URL |
|---|---|---|---|
| py_webauthn | open source, Python, RS256/384/512 and RS1 identifiers | BSD-3-Clause | https://github.com/duo-labs/py_webauthn |
| go-cose | open source, Go, RS256 identifier | MPL-2.0 | https://github.com/veraison/go-cose |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **It does not make these algorithms safe.** §5.2 and §5.3 carry the weaknesses, and §5.4 notes theoretical weaknesses in secp256k1 as the reason for `Recommended: No`.
- **It leaves ECDH on secp256k1 open** (§3.3).
- **It defers RSA key size and exponent detail** to RFC 8230 §6.1 and RFC 7518 §8.3.
- **It cites RFC 8152**, since replaced by `rfc-9052` and `rfc-9053`. The RFC has not been updated. The registries themselves were not re-read, so current `Recommended` values are as this document states them.
- **Read scope.** The whole document, RFC Editor `.txt`.
