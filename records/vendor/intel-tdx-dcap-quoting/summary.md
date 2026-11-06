---
schema: "library-summary/v1"
id: intel-tdx-dcap-quoting
record: intel-tdx-dcap-quoting
type: summary
updated: "2026-11-04"
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

This documents Intel's libraries for generating and verifying TD Quotes, across setup, generation and verification phases (§2). Generation runs through a Quote Generation Service in an SGX-capable component, operated by the platform owner (§2.1, §2.2). Verification can be done by any party, either in an unprotected application or inside an SGX enclave. The enclave variant gives a cryptographically verified result (§2.3). The verification library needs collateral that includes at least the root Intel CA certificate, the CRLs and reference values for the platform TCB (§2.3). It checks the chain, the TDQE and the Quote signature, and evaluates the TCB, but does not check the TD Quote Body: whether the TD's measurements and identity are the expected ones is the verifier's job (§2.3, §2.3.2).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | What a verifier must obtain and decide |
| Cryptography | `adjacent` | No cryptographic design here |
| This project | `none` | A foreign evidence format only |

- **R-I-02**: the PCK Cert is "an X.509 certificate chain rooted in an Intel® CA" (§2.1), and the root Intel CA certificate is part of the verification collateral (§2.3), so importing a TD Quote means configuring Intel's root for that check. Table 1-1 also says the TDQE and QvE can instead be "provided and signed by any authority trusted by the attestation infrastructure owner", and then "the trust is not rooted in Intel". The vendor's own document thus treats the enclave signer as the infrastructure owner's choice, though the PCK Cert's trust stays "rooted in an Intel® CA" (§2.1).

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

**`see_also: intel-sgx-dcap-quotelib`**, owned here: TD Quote generation depends on SGX enclaves (the PCE and the TDQE, §2.1), and the TDX verification library uses the same QvE and verification result codes as the SGX quote library. `intel-tdx-whitepaper` authors its own `see_also` to this record, so that edge is not repeated here.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Verifying a Quote is not the same as trusting it.** §2.3.2 says the library "does not verify the data contained in the TD Quote Body" and lists the Quote Body data that "potentially needs to be checked", leaving the choice to the verifier: MROWNER and MROWNERCONFIG, MRCONFIGID, MRTD, the RTMRs, the debug and security attributes, XFAM, and the report data, for example a nonce for freshness.
- **Source defects.** Table 1-1 defines the TDQE Report as containing "a hash of the private key–part of the Attestation Key"; the AK entry in the same table and §2.1 say it is the public key part. And in the text extraction, the §2.3.1 sentence about `tee_verify_quote` is broken by a pasted copy of the §4.1.1 Set Enclave Load Policy text, a cross-reference that appears to have been expanded in place.
- **Platform owner controls the service path.** §2.2 makes the owner responsible for the QGS and the channel to it.
- **A moving document** at a `latest` URL.
- **Read scope.** §1, Table 1-1 and all of §2 were read by text extraction, on 2026-11-04. API definitions in §3, §4 and the appendices were not.
