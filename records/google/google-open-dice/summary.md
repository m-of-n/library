---
schema: "library-summary/v1"
id: google-open-dice
record: google-open-dice
type: summary
updated: "2026-11-04"
---

# Open Profile for DICE

|  |  |
|---|---|
| **Type** | spec (project specification, explicitly not a formal standard) |
| **Maturity** | `implementation`: Non-Goals says it is not intended to be a formal standard |
| **Authors** | Google / Pigweed open-dice project, no individuals named |
| **Published** | v2.6, read at HEAD 2026-11-01 |
| **Identifier** | Open Profile for DICE v2.6 |
| **Source** | https://pigweed.googlesource.com/open-dice/+/HEAD/docs/specification.md |
| **Digest** | `sha256:db93a541…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Open DICE fills what the TCG hardware specification leaves open: cryptography, UDS size and provisioning, input values, and key derivation and certification. It splits the single CDI in two. The Attestation CDI changes with any input, and the Sealing CDI uses only stable inputs, so sealed data survives updates (CDI Values). Five fixed inputs cover code, configuration, verified-boot authority, a one-byte mode and hidden values (Input Values). Each layer derives a key pair and certificate, chaining to a UDS-derived key certified at manufacture (CDI Certificates, Layering Details). It allows X.509 or CBOR certificates, mixed in one chain (Certificate Details).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A worked root of trust: what is measured, what is sealed, what is certified |
| Cryptography | `core` | Names hashes, KDFs and signatures, including ML-DSA-65 and ML-DSA-87 |
| This project | `adjacent` | A shipped non-X.509 certificate path in CWT and COSE |

- **R-M-01 and DEC-002**: the CBOR option shows an identity chain need not be X.509, and §Certificate Details lets a chain mix the two. It uses CWT and COSE, so it is prior art for a CBOR native encoding.
- **R-M-02**: the CDI key changes with software. A principal named by that key is named by key and state together, so the name changes on every update. That is a real cost if the key is meant to be stable.

## Implementations

**Not surveyed.** Licenses were read from each repository on 2026-11-01 and re-checked 2026-11-04. No wider search was run.

| Name | Kind | License | URL |
|---|---|---|---|
| open-dice | open source, the profile's repository | Apache-2.0 | https://pigweed.googlesource.com/open-dice/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**Relations.** `cites` holds what the text links or names: the TCG DICE hardware requirements (Background), RFC 5280, RFC 8392 and RFC 8152 for the two certificate forms (Certificate Details), RFC 8032 and RFC 9881 for Ed25519 and ML-DSA key info, and CNSA 2.0 (ML-DSA: "CNSA2.0 requirements accept ML-DSA-87 only"). ML-DSA itself is linked to Wikipedia, not FIPS 204, so `fips-204` was dropped from `see_also`; `tcg-dice-hw-requirements` was dropped from `see_also` as a duplicate of `cites`. Two `see_also` edges remain, both ours: `tcg-dice-layering` is TCG's own layering architecture, the counterpart to Layering Details here, which this profile does not cite; `tcg-dice-cert-profiles` is TCG's X.509 profile for DICE-derived keys; it defers attestation extensions to a future specification, while Open DICE's X.509 CDI certificates fill that gap with a Google-assigned custom extension (1.3.6.1.4.1.11129.2.1.24, X.509 CDI Certificates).

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Not a formal standard**, by its own Non-Goals.
- **Sealing needs verified boot.** Use Cases says sealing only works well in combination with it.
- **Layer isolation is assumed.** Layering Details forbids a layer offering CDI-based services upward and requires previous-layer CDIs be "destroyed, locked, or otherwise protected", without saying how.
- **A floating source.** The URL tracks HEAD, so the digest pins only what was read.
- **Android specialisation not held.** `android.md` is named as a specialisation and was not read.
- **Read scope.** Background to CDI Certificates, High-level DICE Flow, ML-DSA, Layering Details, UDS Requirements, the Certificate Details opening and Appendix B were read. Other cryptography sections, the provisioning schemes, certificate field tables and Appendices A and C were not read.
