---
schema: "library-summary/v1"
id: intel-sgx-dcap-quotelib
record: intel-sgx-dcap-quotelib
type: summary
updated: "2026-11-04"
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

An enclave's REPORT is MAC'd for local attestation, and a Quoting Enclave converts it to a Quote under a P-256 attestation key certified by a key rooted in platform fuses (§2, §2.1). Verification returns graded results, not a boolean. Three are terminal: invalid signature, revoked and unspecified. Six are non-terminal, OK among them; a caller wanting Intel's strict policy accepts only OK, and the others "will need more analysis before establishing trust in the attesting enclave" (§3.6.2). §3.8 notes the verify API establishes an enclave ran with SGX protections, without identifying whose enclave it was.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Shows how a verdict is graded and what the caller must still check |
| Cryptography | `adjacent` | ECDSA P-256 under fuse-rooted certification |
| This project | `none` | Foreign evidence only |

- **R-I-02**: the attestation key is "certified by an Intel® SGX rooted key whose certificate is distributed by Intel®" (§1), and the PCK Cert is an X.509 chain Intel signs and distributes (Table 1-1). Importing an SGX Quote means configuring Intel's root for that check, which R-I-02 requires to stay a scoped foreign root rather than a native anchor.

## Implementations

**Not surveyed.** Licenses were read from each repository on 2026-11-01 and re-read 2026-11-04. No wider search was run.

| Name | Kind | License | URL |
|---|---|---|---|
| confidential-computing.tee.dcap (formerly SGXDataCenterAttestationPrimitives) | open source, Intel | BSD-3-Clause, per `License.txt`; GitHub's detector reports NOASSERTION | https://github.com/intel/confidential-computing.tee.dcap |

The old URL, github.com/intel/SGXDataCenterAttestationPrimitives, redirects to the renamed repository.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `see_also` authored here.** `intel-tdx-dcap-quoting` and `intel-tdx-whitepaper` each author a `see_also` to this record, with their reasons; the edge is symmetric, so it is not repeated.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Whose enclave is the caller's job** (§3.8).
- **Freshness is the caller's job.** Expired collateral only sets `p_collateral_expiration_status`; "this check alone will not cause the Verify Quote API to return an error" (§3.6.2).
- **Scalable SGX has different properties.** §3.7 says that when `sgx_type` is 1 (scalable, multi-package platforms) the security properties are different from `sgx_type` 0 (standard). It says "may be different" and "are different" in consecutive paragraphs.
- **A moving document** at a `latest` URL.
- **Read scope.** §1, §2 and §2.1, §2.2, the §3.6.2 result list and its surrounding text, §3.6.9's description, §3.7 and the §3.8 opening were read, by text extraction. The rest of the API reference was not.
