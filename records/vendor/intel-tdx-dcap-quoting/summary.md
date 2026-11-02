---
schema: "library-summary/v1"
id: intel-tdx-dcap-quoting
record: intel-tdx-dcap-quoting
type: summary
updated: "2026-11-01"
---

# Intel TDX DCAP: Quote Generation Library and Quote Verification Library

|  |  |
|---|---|
| **Type** | spec (vendor API reference) |
| **Maturity** | `implementation`: an API reference for Intel libraries |
| **Authors** | Intel Corporation, no individuals named |
| **Published** | 2026-09 |
| **Identifier** | Intel TDX DCAP Quote Library API, Rev 0.91 |
| **Source** | https://download.01.org/intel-sgx/latest/dcap-latest/linux/docs/Intel_TDX_DCAP_Quoting_Library_API.pdf |
| **Digest** | `sha256:01c7e01d…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This documents Intel's libraries for generating and verifying TD Quotes, across setup, generation and verification phases (§2). Generation runs through a Quote Generation Service in an SGX-capable component, operated by the platform owner (§2.1, §2.2). Verification can be done by any party, either in an unprotected application or inside an SGX enclave. The enclave variant gives a cryptographically verified result (§2.3). Either way it needs verification collateral, which includes at least the root Intel CA certificate.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | What a verifier must obtain and decide |
| Cryptography | `adjacent` | No cryptographic design here |
| This project | `none` | A foreign evidence format only |

- **R-I-02**: verification depends on Intel-signed collateral at every step, so a verifier has a live dependency on the vendor.

## Implementations

**Not surveyed.** Licenses were read from each repository on 2026-11-01. No wider search was run.

| Name | Kind | License | URL |
|---|---|---|---|
| SGXDataCenterAttestationPrimitives | open source, Intel | see repository; GitHub reports NOASSERTION | https://github.com/intel/SGXDataCenterAttestationPrimitives |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Verifying a Quote is not the same as trusting it.** §2.3 allows additional validation checks around the library, and §2.3.2 is headed Extended TD Checks.
- **Platform owner controls the service path.** §2.2 makes the owner responsible for the QGS and the channel to it.
- **A moving document** at a `latest` URL.
- **Read scope.** §2 up to the variants of quote verification, and the opening of §2.3.1, were read. API definitions in §3, §4 and the appendices were not.
