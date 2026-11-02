---
schema: "library-summary/v1"
id: tcg-dice-symmetric
record: tcg-dice-symmetric
type: summary
updated: "2026-11-01"
---

# Symmetric Identity Based Device Attestation

|  |  |
|---|---|
| **Type** | spec (TCG) |
| **Maturity** | `standard`: cover marked PUBLISHED |
| **Authors** | Trusted Computing Group, individual contributors not recorded here |
| **Published** | 2020-01-07 |
| **Identifier** | TCG Symmetric Identity Based Device Attestation, Version 1.0 Revision 0.95 |
| **Source** | https://www.trustedcomputinggroup.org/resources/documents/symmetric-identity-based-device-attestation |
| **Digest** | `sha256:4531a813…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

For microcontrollers that can run DICE but not asymmetric cryptography, this replaces signatures with MACs (§4.1). First Mutable Code derives a Symmetric Alias Key from the CDI, and the device answers a verifier's challenge with a MAC under it (§5.1). A TLS-PSK variant makes the handshake itself the implicit attestation (§5.2). The verifier must therefore hold the device's key, and to follow firmware updates it must know the device's UDS (§5.3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Shows what attestation costs when the verifier must share the secret |
| Cryptography | `adjacent` | MAC and KDF choices, with HMAC preferred on security grounds (§5.1 comment) |
| This project | `adjacent` | Instructive negative: there is no key a third party can verify |

- **R-M-02 and R-O-01**: a MAC has no public issuer key. A verifier who can check the attestation can also forge it (§5.3), so this design cannot satisfy R-O-01 and could only ever enter as a verifier-issued claim.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Disagrees in posture with the asymmetric family.** `tcg-dice-implicit-identity` §4 and §7.1.1.2 advise against manufacturers retaining UDS or CDI values, and this document requires the verifier to know the UDS. These are different schemes, so no `contradicts` edge is set, but a deployment cannot have both properties.
- **Revocation is not addressed** (§5.4 comment).
- **Single-infrastructure assumption** (§4).
- **Delegating verification hands over key material**, up to the UDS for firmware-update rights (§5.4 table).
- **Read scope.** r0.94 was read whole. r0.95 was checked for the statements above by text search and was not compared line by line.
