---
schema: "library-summary/v1"
id: tcg-dice-hw-requirements
record: tcg-dice-hw-requirements
type: summary
updated: "2026-11-04"
---

# Hardware Requirements for a Device Identifier Composition Engine

|  |  |
|---|---|
| **Type** | spec (TCG) |
| **Maturity** | `standard`: cover marked PUBLISHED |
| **Authors** | Trusted Computing Group, individual contributors not recorded here |
| **Published** | 2024-08-08 |
| **Identifier** | TCG DICE hardware requirements, Version 1.0 Revision 0.91 |
| **Source** | https://www.trustedcomputinggroup.org/resources/documents/hardware-requirements-for-a-device-identifier-composition-engine |
| **Digest** | `sha256:20b1ceaa…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

DICE is a hardware root of trust aimed at designers of programmable components that do not have access to a TPM (§1). At reset it reads a Unique Device Secret, measures the First Measured Code, combines the two by a one-way function into a Compound Device Identifier, locks the secret until next reset, and hands over the CDI (§5.4). Code that changes gets a different CDI, so malware cannot inherit the previous one's secrets (§4). That is the design's central move: identity depends on what booted, without anything storing a key.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | It is the root the rest of the family rests on |
| Cryptography | `adjacent` | Requires a one-way function preserving the UDS's strength, and leaves the choice open (§5.4) |
| This project | `adjacent` | Shows a key can be derived from state, not generated and held |

- **R-M-02**: a key derived from the CDI identifies device and code together. What a hardware root adds to a bare key is this binding between the key and what booted.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**`cites`** lists the held records among §2's references: [2] DICE Layering Architecture and [3] NIST SP 800-57 Part 1 Rev. 5 (`sp-800-57pt1r5`). **No `see_also`.** All five earlier edges pointed at records that cite this one (`tcg-dice-implicit-identity`, `tcg-dice-symmetric`, `tcg-dice-cert-profiles`, `google-open-dice`) or that it cites (`tcg-dice-layering`).

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **The engine itself is believed, not measured.** §4.1 says updates to the engine are not measured in the CDI and must be inherently trusted, and §5.2.2 item 3 says a manufacturer-controlled update SHOULD NOT change the CDI.
- **Protecting the CDI is largely out of scope.** §4 puts how the CDI is protected outside the specification, and the §5.3 informative comment warns that a leaked CDI allows replay and impersonation.
- **Interoperable mixing is not specified.** §4 says the method of combining UDS and measurement is the manufacturer's choice "because it does not affect interoperability", so a verifier cannot recompute a CDI without knowing it.
- **Source defect.** The §5.3 informative comment cites "DICE Protection Environment (DPE) [3]", but [3] is NIST SP 800-57; DPE is [4].
- **No attestation protocol.** That is in the other DICE records.
- **Read scope.** r0.91 was read whole on 2026-11-04, and all locators above are r0.91's. Revision 78 was read whole earlier and was not re-compared.
