---
schema: "library-summary/v1"
id: tcg-dice-hw-requirements
record: tcg-dice-hw-requirements
type: summary
updated: "2026-11-01"
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

DICE is a hardware root of trust for devices with no TPM (§1). At reset it reads a Unique Device Secret, measures the First Measured Code, combines the two by a one-way function into a Compound Device Identifier, locks the secret until next reset, and hands over the CDI (§5.4). Code that changes gets a different CDI, so malware cannot inherit the previous one's secrets. That is the design's central move: identity depends on what booted, without anything storing a key.

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

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **The engine itself is believed, not measured.** Revision 78 §1 says updates to the engine are not measured in the CDI and must be inherently trusted. An updatable DICE leaves the CDI unchanged after a manufacturer update (§5.2.2 SHOULD NOT).
- **Protecting the CDI is largely out of scope.** Revision 78 §6.3 and its notes leave this to the device, and warn that a leaked CDI allows impersonation.
- **Interoperable mixing is not specified.** Revision 78 §5 says the choice of method is the manufacturer's, so a verifier cannot recompute a CDI without knowing it.
- **No attestation protocol.** That is in the other DICE records.
- **Read scope.** Revision 78 was read whole. In r0.91 §1, the section list and the normative lines of §5 were read, and the rest was not compared. Where a statement above cites revision 78 its presence in r0.91 was not checked line by line.
