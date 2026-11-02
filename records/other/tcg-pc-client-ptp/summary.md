---
schema: "library-summary/v1"
id: tcg-pc-client-ptp
record: tcg-pc-client-ptp
type: summary
updated: "2026-11-01"
---

# TCG PC Client Platform TPM Profile Specification for TPM 2.0

|  |  |
|---|---|
| **Type** | spec (TCG) |
| **Maturity** | `standard`: cover marked PUBLISHED |
| **Authors** | Trusted Computing Group, individual contributors not recorded here |
| **Published** | 2026-03-23 |
| **Identifier** | TCG PC Client Platform TPM Profile for TPM 2.0, Version 1.07 |
| **Source** | https://www.trustedcomputinggroup.org/resources/documents/pc-client-platform-tpm-profile-ptp-specification |
| **Digest** | `sha256:e6a031c5…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The PTP says which of the TPM library's options a PC TPM must have, and specifies its interfaces: registers, localities, SPI and I2C (§3 to §8). Version 1.07 changes the algorithm table in a way that matters here. ML-DSA and ML-KEM are mandatory as of this version, SHA-1 is Not Allowed, and an NV index must now hold 8500 bytes, sized for an ML-KEM-1024 EK certificate signed by ML-DSA-87 (§4.2, §4.3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Sets the floor for what a PC TPM can do |
| Cryptography | `adjacent` | Algorithm mandates, including FIPS 203 and 204 parameter sets |
| This project | `adjacent` | What a device principal's key can be on a compliant PC |

- **R-M-02**: §4.3 means a compliant PC TPM can hold an ML-DSA key. The 8500-byte index shows the certificate-size pressure a key-as-principal design would inherit. See `tcg-tpm-2-0-library-185`.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **A profile, not a product.** It says what a compliant TPM must support, not what has shipped. This does not close the availability gap in `tcg-tpm-2-0-library-185`.
- **Interfaces are not attestation.** Almost all of this document is hardware interface.
- **Errata not read.** Errata v1.1 for 1.07 exists and could change §4.
- **Read scope.** Section list, §4.2 minimums on ML-DSA and NV size, and §4.3's rules and PQC rows were read. §3 and §5 to §8 were not. v1.06 r32 was fetched and not read, and no diff was made.
