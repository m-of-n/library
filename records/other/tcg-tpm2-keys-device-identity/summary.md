---
schema: "library-summary/v1"
id: tcg-tpm2-keys-device-identity
record: tcg-tpm2-keys-device-identity
type: summary
updated: "2026-11-04"
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

This maps IEEE 802.1AR device identity onto TPM 2.0 keys. An OEM CA verifies TPM residency before certifying an IDevID or IAK, and the owner later enrols local LDevID and LAK keys under them (§4 to §6). It rejects using the Endorsement Key as the identity: an EK is a storage key and identifies a TPM, while a DevID identifies a device (§3.11). A CA's signature is what binds a fixedTPM key to device information (§4), and the TPM's job is to make that key non-transferable (§3.3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Residency proof is the operational meaning of hardware-bound |
| Cryptography | `adjacent` | Templates for RSA, NIST P-256 to P-521 and SM2. No post-quantum template found |
| This project | `adjacent` | Models key, device, and owner as separate certified relations |

- **R-M-02**: §3.3 says the point of a TPM for identity is that the private key cannot move. A bare key cannot show that, and only a CA's check under §4 can.
- **R-I-05**: everything is X.509 and rests on an OEM CA.
- Not `R-O-02`: §11's advice to use the long-term IDevID/IAK only to enrol an LDevID/LAK, one per application, is about correlation and privacy, not validity periods or revocation.

**Relations.** `see_also: tcg-tpm-2-0-library-184`: this profile is built on the TPM 2.0 Library (§2.2 assumes Rev 1.38 or later; its reference [2] is Rev 1.38, which we do not hold), and v184 is the library text held. `see_also: tcg-dice-cert-profiles`: the DICE profiles define IDevID, LDevID and attestation certificates for DICE-derived keys, the same 802.1AR roles for a different hardware root.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Assurance sits in the OEM.** §4 says the OEM CA MUST be diligent in verifying TPM binding to the device, and §10.1 (informative) treats monitoring the manufacturing infrastructure as a countermeasure.
- **Key attributes are not state.** Residency says where a key lives, not what the platform is running. §6.1.4 makes device attestation during OEM enrolment RECOMMENDED, not required.
- **Zeroisation.** §9 requires that zeroisation or return to factory defaults enable IDevID/IAK access and use, while LDevID/LAK configuration MUST be removed. The OEM identity is regenerable from the Endorsement Hierarchy (§11), so a factory reset does not shed it; §9 does require that the user can disable it.
- **Read scope.** §2.1, §2.2, §3.3, §3.11, §4 opening, §5.8, §9, §10.1 opening and §11 were read in Version 1.00 r12. In v1.1, §2.2, §3.3, §3.11, §4 to §4.2, §6.1.4, §9, §10.1, §11 and §12 were read on 2026-11-04 against the recorded digest. The diff to v1.1 was not reviewed. §6 to §8 and the annexes were sampled only.
