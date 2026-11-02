---
schema: "library-summary/v1"
id: intel-sgx-dcap-quotelib
record: intel-sgx-dcap-quotelib
type: summary
updated: "2026-11-01"
---

# Intel SGX DCAP: ECDSA Quote Library API

|  |  |
|---|---|
| **Type** | spec (vendor API reference) |
| **Maturity** | `implementation`: an API reference for Intel libraries |
| **Authors** | Intel Corporation, no individuals named |
| **Published** | 2026-09 |
| **Identifier** | Intel SGX ECDSA Quote Library API, Rev Production |
| **Source** | https://download.01.org/intel-sgx/latest/dcap-latest/linux/docs/Intel_SGX_ECDSA_QuoteLibReference_DCAP_API.pdf |
| **Digest** | `sha256:1450e4b7…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

An enclave's REPORT is MAC'd for local attestation, and a Quoting Enclave converts it to a Quote under a P-256 attestation key certified by a key rooted in platform fuses (§2, §2.1). Verification returns graded results, not a boolean. Some are terminal, such as invalid signature or revoked. Others are non-terminal, such as out of date or configuration needed, and need more analysis by the relying party (Verify Quote API result list). §3.8 notes the verify API establishes an enclave ran with SGX protections, without identifying whose enclave it was.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Shows how a verdict is graded and what the caller must still check |
| Cryptography | `adjacent` | ECDSA P-256 under fuse-rooted certification |
| This project | `none` | Foreign evidence only |

- **R-I-02**: the root is Intel's. The verdicts depend on Intel-published collateral, so a stale policy can change the answer.

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

- **Whose enclave is the caller's job** (§3.8).
- **Scalable SGX has different properties.** §3.7 says multi-package platforms have different security properties from standard ones.
- **A moving document** at a `latest` URL.
- **Read scope.** §2 opening, §2.1 opening, the verification-result list, the §3.7 opening and the §3.8 opening were read. API reference sections were not. 
