---
schema: "library-summary/v1"
id: aws-snp-attestation
record: aws-snp-attestation
type: summary
updated: "2026-11-01"
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

- **R-I-02**: the root is AMD's, and the VLEK path adds AWS as a named party. The page shows a verifier choosing to check it, not inheriting it.

## Implementations

**Not surveyed.** Licenses were read from each repository on 2026-11-01. No wider search was run.

| Name | Kind | License | URL |
|---|---|---|---|
| snpguest | open source, used by the page | Apache-2.0 | https://github.com/virtee/snpguest |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`.** This is the summary bar. A `web` record is not an FX-1 type, and nothing here needs extraction yet.

## Limits

- **Proves initial state.** The page's claim is limited to a genuine AMD environment and the initial boot code. `sev-snp-primer-2026` §6.7 gives the wider limits.
- **A VLEK does not name the chip.** The page calls it issued by AMD for AWS, so the signer is not per chip.
- **Milan only** is stated as the supported processor model in the note read, which may date.
- **Read scope.** The page was read as extracted text for the VCEK flow, and by keyword for the VLEK flow.
