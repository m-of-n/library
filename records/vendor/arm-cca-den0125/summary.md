---
schema: "library-summary/v1"
id: arm-cca-den0125
record: arm-cca-den0125
type: summary
updated: "2026-11-01"
---

# Learn the architecture: Introducing Arm Confidential Compute Architecture

|  |  |
|---|---|
| **Type** | spec (vendor learning guide, Non-Confidential) |
| **Maturity** | `recommendation`: vendor guidance, not a specification |
| **Authors** | Arm Limited, no individuals named |
| **Published** | 2025-03-19 (issue 400) |
| **Identifier** | DEN0125, issue 400 |
| **Source** | https://documentation-service.arm.com/static/6812468479c4c17ad8037525 |
| **Digest** | `sha256:799d3c93…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This guide introduces CCA: Realms are protected VM environments, allocated by the normal-world host, which can schedule them and manage their memory, but cannot read them (§3). The RME hardware extension adds Root and Realm worlds to TrustZone's two, and the RMM firmware manages Realms (§2, §3). Attestation has two parts, platform and initial Realm state, and the guide frames it as how a Realm owner establishes trust before giving it secrets (§2, §3). Issue 400 adds Planes, which can run a vTPM beside a guest OS inside one Realm (§3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Context for the CCA attestation model |
| Cryptography | `none` | None |
| This project | `none` | Bears on no requirement |

- Bears on no `DEC-*` or `R-*` yet. It is held as context for `draft-ffm-rats-cca-token`, which is where the attestation detail sits.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **An introduction.** Attestation gets a short treatment in §2, and it defers the model to RATS.
- **Attestation of initial state only**, as §2 and §3 frame it. Runtime claims are in the draft.
- **Read scope.** §1 to §3 were read in full up to the TrustZone comparison, plus the §7.2 opening and a keyword search for attestation. §4 to §6 were not read. Read as a text extraction of the PDF.
