---
schema: "library-summary/v1"
id: intel-tdx-whitepaper
record: intel-tdx-whitepaper
type: summary
updated: "2026-11-04"
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

TDX puts VMs in hardware-isolated trust domains, isolated from the hypervisor (§1), and lets a workload exclude the platform's firmware, software, devices and operators from its trusted base (§2). An Intel-signed module in a new CPU mode, SEAM, enforces this (§2). Remote attestation is built in steps: SEAMREPORT produces a MAC'd report bound to the platform, a TD-quoting enclave (an SGX enclave) verifies the MAC with EVERIFYREPORT and signs a Quote, and the Provisioning-Certification Enclave certifies the attestation key under a PCK, for which Intel publishes certificates and CRLs, giving a chain from the Quote to an Intel CA (§2.E).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Primary source on what a TEE quote contains and how it chains |
| Cryptography | `adjacent` | AES-XTS with a 28-bit MAC, ECDSA attestation |
| This project | `adjacent` | A vendor root reachable only through a vendor CA |

- **R-I-02**: §2.E says TD-quoting enclaves are certified "with a certificate chain rooted to an Intel-issued certificate". Importing a TDX Quote therefore means configuring Intel's CA for that one check, which R-I-02 requires to stay a scoped foreign root rather than a native anchor.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**`see_also`** (owned here, not repeated on the targets):

- `intel-tdx-dcap-quoting`: the current Intel API documentation of the generation and verification flow this paper sketches in §2.E.
- `intel-sgx-dcap-quotelib`: §2.E says the TDX certification infrastructure is "built upon" Intel SGX DCAP; that record is the SGX DCAP quote library.

`sev-snp-primer-2026` was a `see_also` here and was dropped on 2026-11-04: neither document refers to the other, and grouping two vendors' TEEs is what the shared `device-attestation` topic already does.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Replay of memory by physical attack is excluded.** The paper says TDX does not defend against it (§2, opening) and that the current generation does not detect it (§2.A).
- **Denial of service by the VMM is not a security objective** (§2, opening).
- **Dated and preliminary.** The notices say dates and figures are preliminary. This 2020 description has not been compared with current Intel documentation.
- **Not everything in the Quote is measured.** Besides TD-provided data and measurement registers, the paper says some state, such as the TD's attributes and the owner identity MROWNER, is included in the attestation without being measured (§2.E).
- **Read scope.** Read whole, from the Archive capture; re-read in full for the 2026-11-04 source check. The paper numbers its sections 01 to 03 with lettered subsections; §2.E here is "02. E. Remote Attestation".
