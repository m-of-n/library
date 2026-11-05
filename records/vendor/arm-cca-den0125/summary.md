---
schema: "library-summary/v1"
id: arm-cca-den0125
record: arm-cca-den0125
type: summary
updated: "2026-11-04"
---

# Learn the architecture: Introducing Arm Confidential Compute Architecture

|  |  |
|---|---|
| **Type** | spec (vendor learning guide, Non-Confidential) |
| **Maturity** | _unset_: a vendor guide whose content it calls informational only, so no maturity level applies |
| **Authors** | Arm Limited, no individuals named |
| **Published** | 2025-03-19 (issue 400) |
| **Identifier** | DEN0125, issue 400 (den0125_400_en), version 4.0 |
| **Source** | https://documentation-service.arm.com/static/6812468479c4c17ad8037525 |
| **Digest** | `sha256:799d3c93…` (full value in `record.yaml`), fetched 2026-11-01, re-checked 2026-11-04 |

## Overview

This guide introduces CCA: Realms are protected VM environments, allocated by the Normal world Host, which can schedule them and manage their memory but cannot observe or modify what runs in them (§3). The RME hardware extension adds Root and Realm worlds to TrustZone's Secure and Normal worlds, and the RMM firmware manages Realms (§2, §3). Attestation has two parts, the platform and the initial state of the Realm (§2), and it is how a Realm owner establishes trust in a Realm before provisioning secrets to it (§3). Issue 400 adds Realm Planes (document history), and §3's example runs a vTPM in one Plane beside the guest OS in another, inside one Realm.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Context for the CCA attestation model |
| Cryptography | `none` | None |
| This project | `none` | Bears on no requirement |

- Bears on no `DEC-*` or `R-*` yet. It is held as context for `draft-ffm-rats-cca-token`, which cites this issue as [CCA-ARCH] and is where the attestation detail sits.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites`, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**`cites: rfc-9334`**: §2 refers readers to RATS for the roles of the actors in Realm attestation. It names it only as "the Remote Attestation Specification (RATS)", with no reference entry or link; the RATS architecture the library holds is `rfc-9334`. **No `see_also`.** The link to `draft-ffm-rats-cca-token` is carried by that draft's `cites`, so it is not repeated as a `see_also`.

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **An introduction.** Attestation gets a short treatment in §2, and it defers the model to RATS.
- **Attestation of initial state**, as §2 frames it, and §5 describes the RSI attestation report the same way. Runtime claims are in the draft.
- **No availability.** §3 says CCA gives Realms confidentiality and integrity but not availability, and that a compromised hypervisor might prevent a Realm VM from executing.
- **Read scope.** §1 to §3 in full, the RMM and interface parts of §5, the §7.2 opening and a keyword search for attestation were read, as a text extraction of the PDF. §4, §6 and the rest of §5 and §7 were not.
