---
schema: "library-summary/v1"
id: intel-tdx-whitepaper
record: intel-tdx-whitepaper
type: summary
updated: "2026-11-01"
---

# Intel Trust Domain Extensions (white paper)

|  |  |
|---|---|
| **Type** | spec (vendor white paper) |
| **Maturity** | `white-paper` |
| **Authors** | Intel Corporation, no individuals named |
| **Published** | 2020-09 |
| **Identifier** | Intel 343961-002US |
| **Source** | https://www.intel.com/content/dam/develop/external/us/en/documents/tdx-whitepaper-final9-17.pdf |
| **Digest** | `sha256:575e4e71…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

TDX puts VMs in hardware-isolated trust domains and takes the hypervisor, firmware and cloud operators out of their trusted base (§2). An Intel-signed module in a new CPU mode enforces this. Remote attestation is built in steps: the CPU's SEAMREPORT produces a MAC'd report bound to the platform, a local SGX quoting enclave verifies it and signs a Quote, and a certificate chain runs from the attestation key through a platform PCK key to an Intel CA (§2.E).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Primary source on what a TEE quote contains and how it chains |
| Cryptography | `adjacent` | AES-XTS with a 28-bit MAC, ECDSA attestation |
| This project | `adjacent` | A vendor root reachable only through a vendor CA |

- **R-I-02**: every quote chains to an Intel-issued certificate (§2.E). Accepting one means accepting Intel for that claim, and must not make Intel a native anchor.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Replay of memory by physical attack is excluded.** The paper says TDX does not defend against it and that the current generation does not detect it (§2.A).
- **Denial of service by the VMM is not a goal** (§1).
- **Dated and preliminary.** The notices say dates and figures are preliminary. This 2020 description has not been compared with current Intel documentation.
- **TD identity in the Quote is what software declares**, plus measurements. The paper says some state, like MROWNER, is included unmeasured (§2.E).
- **Read scope.** Read whole, from the Archive capture.
