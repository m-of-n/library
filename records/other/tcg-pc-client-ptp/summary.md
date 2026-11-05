---
schema: "library-summary/v1"
id: tcg-pc-client-ptp
record: tcg-pc-client-ptp
type: summary
updated: "2026-11-04"
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

The PTP says which of the TPM library's options a PC TPM must have, and specifies its interfaces: registers, localities, SPI and I2C (§3 to §9). Version 1.07 changes the algorithm table in a way that matters here. ML-DSA and ML-KEM are mandatory as of this version, SHA-1 is Not Allowed, and an NV index must now hold 8500 bytes, sized for an ML-KEM-1024 EK certificate signed by ML-DSA-87 (§4.2, §4.3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Sets the floor for what a PC TPM can do |
| Cryptography | `adjacent` | Algorithm mandates, including FIPS 203 and 204 parameter sets |
| This project | `adjacent` | What a device principal's key can be on a compliant PC |

- **R-M-02**: §4.3 means a compliant PC TPM can hold an ML-DSA key, so a device principal named by its TPM key can be post-quantum. The 8500-byte index (§4.2, Table 2) shows the size of what such a key brings with it, which is an argument for naming it by key digest rather than by key. See `tcg-tpm-2-0-library-185`.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**`cites`** holds the TPM Library Specification, which §1 to §2 require at "Version 185 [5] or later" (`tcg-tpm-2-0-library-185`), and the PC Client PFP (§11 ref 2). **No `see_also`.** `tcg-pc-client-pfp` was a duplicate of `cites` both ways, the TPM library is now under `cites`, and `fips-204` and `cnsa-2-0` had no stated reason; the profile names ML-DSA and ML-KEM parameter sets but cites neither FIPS 204 nor CNSA 2.0.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **A profile, not a product.** It says what a compliant TPM must support, not what has shipped. This does not close the availability gap in `tcg-tpm-2-0-library-185`.
- **Interfaces are not attestation.** Almost all of this document is hardware interface.
- **Errata v1.1 (2026-08-27) changes §4 and more, non-normatively.** It corrects the ML-DSA SHOULD in Table 3 from "ML-DSA-44, ML-DSA-65, or ML-DSA-87" to "and" (Errata 1), treats algorithms not in Table 3 as Optional (Errata 2), drops ECC as a requirement for TPM2_Encapsulate/Decapsulate (Errata 3), rewrites CRB Seize behaviour (Errata 4), and restores §10.2 NV Index Provisioning for Platform Firmware Supported Features, which 1.07 "inadvertently removed" (Errata 6). That last one matters to `tcg-pc-client-pfp`, whose event-log integrity indexes point at PTP 1.06 for their attributes.
- **Read scope.** Section list, §1 to §2 on the library version, §4.2 Table 2 on ML-DSA and NV size, §4.3 whole, §11 references and the whole errata were read on 2026-11-04. §3 and §5 to §9 were not. v1.06 r32 was fetched and not read, and no diff was made.
