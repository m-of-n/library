---
schema: "library-summary/v1"
id: tcg-tpm2-keys-device-identity
record: tcg-tpm2-keys-device-identity
type: summary
updated: "2026-11-01"
---

# TPM 2.0 Keys for Device Identity and Attestation

|  |  |
|---|---|
| **Type** | spec (TCG) |
| **Maturity** | `standard`: cover marked PUBLISHED |
| **Authors** | Trusted Computing Group, individual contributors not recorded here |
| **Published** | 2025-04-23 |
| **Identifier** | TCG TPM 2.0 Keys for Device Identity and Attestation, Version 1.1 |
| **Source** | https://www.trustedcomputinggroup.org/resources/documents/tpm-2-0-keys-for-device-identity-and-attestation |
| **Digest** | `sha256:220a7322…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This maps IEEE 802.1AR device identity onto TPM 2.0 keys. An OEM CA verifies TPM residency before certifying an IDevID or IAK, and the owner later enrols local LDevID and LAK keys under them (§4 to §6). It rejects using the Endorsement Key as the identity: an EK is a storage key and identifies a TPM, while a DevID identifies a device (§3.11). A CA's certificate is the point where the key becomes bound to a device, and the TPM's job is to make that key non-transferable (§3.3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Residency proof is the operational meaning of hardware-bound |
| Cryptography | `adjacent` | Templates for RSA, NIST P-256 to P-521 and SM2. No post-quantum template found |
| This project | `adjacent` | Models key, device, and owner as separate certified relations |

- **R-M-02**: §3.3 says the point of a TPM for identity is that the private key cannot move. A bare key cannot show that, and only a CA's check under §4 can.
- **R-I-05**: everything is X.509 and rests on an OEM CA.
- **R-O-02**: §11 recommends using the long-term IDevID/IAK only to enrol an LDevID/LAK, and using one local key per application.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Assurance sits in the OEM.** §4 calls the OEM CA's diligence essential, and §10.1 treats factory monitoring as a countermeasure.
- **Key attributes are not state.** Residency says where a key lives, not what the platform is running. §6.1.4 recommends device validation at enrolment, and it stays a recommendation.
- **Zeroisation.** §9 requires IDevID/IAK to survive return to factory state, so it is deliberately not owner-erasable.
- **Read scope.** §2.1, §2.2, §3.3, §3.11, §4 opening, §5.8, §9, §10.1 opening and §11 were read in Version 1.00 r12, and §9, §10.1 and §11 again in v1.1. The diff to v1.1 was not reviewed. §6 to §8 and the annexes were sampled only.
