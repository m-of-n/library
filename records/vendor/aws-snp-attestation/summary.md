---
schema: "library-summary/v1"
id: aws-snp-attestation
record: aws-snp-attestation
type: summary
updated: "2026-11-04"
---

# Attest an Amazon EC2 instance with AMD SEV-SNP

|  |  |
|---|---|
| **Type** | web (vendor user guide) |
| **Maturity** | `implementation`: vendor user guide |
| **Authors** | Amazon Web Services, no individuals named |
| **Published** | undated |
| **Identifier** | AWS EC2 User Guide, snp-attestation |
| **Source** | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snp-attestation.html |
| **Digest** | `sha256:07b51a1e…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This is AWS's procedure for getting and verifying a SEV-SNP report from an EC2 instance, using `snpguest`. The report holds the launch measurement of initial guest memory and vCPU state. On Dedicated Hosts it is signed by a per-chip VCEK. On shared tenancy it is signed by a VLEK, issued by AMD for AWS. Both chain to an AMD root, and the page has the user validate that chain from AMD's key distribution service.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | A worked verification, not new security content |
| Cryptography | `none` | None of its own |
| This project | `adjacent` | A real instance of a cloud TEE's evidence |

- **Bears on no `DEC-*` or `R-*`.** It is a how-to for one vendor's evidence and says nothing about how a verifier should hold the AMD root beyond fetching it from AMD's KDS at verification time (Step 3, both flows). R-I-02, which an earlier pass cited, needs a statement about trust anchors that this page does not make.

## Implementations

**Not surveyed.** Licenses were read from each repository on 2026-11-01. No wider search was run.

| Name | Kind | License | URL |
|---|---|---|---|
| snpguest | open source, used by the page | Apache-2.0 | https://github.com/virtee/snpguest |

## Relations

- **`see_also: sev-snp-primer-2026`**: the primer explains what this page leaves implicit, VCEK versus VLEK (§6.3.2), and the verifier duties the page omits: pinning the ARK, checking the CRL, enforcing a minimum TCB and checking REPORT_DATA (§6.8).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A `web` record is not an FX-1 type, and nothing here needs extraction yet.

## Limits

- **Proves initial state.** The page's claim is limited to a genuine AMD environment and the initial boot code. `sev-snp-primer-2026` §6.7 gives the wider limits.
- **A VLEK does not name the chip.** The page says only that it is "issued by AMD for AWS". That VLEK certificates carry no CHIP_ID is from `sev-snp-primer-2026` §6.3.2, not from this page.
- **Milan only** is stated as the supported processor model in the Dedicated Hosts note, which may date. Both flows' KDS URLs are also Milan-specific.
- **The root is fetched, not pinned.** Step 3 downloads `cert_chain` from `kdsintf.amd.com` and verifies the VCEK or VLEK against it. `sev-snp-primer-2026` §6.8 says the ARK should be pinned because a network adversary could otherwise substitute it. The page also does not check the CRL, a minimum TCB, the measurement value or REPORT_DATA; its Step 4 only checks the signature and that the TCB fields match the certificate.
- **Read scope.** The whole page was read as extracted text, both flows.
