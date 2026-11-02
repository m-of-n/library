---
schema: "library-summary/v1"
id: tcg-pc-client-pfp
record: tcg-pc-client-pfp
type: summary
updated: "2026-11-01"
---

# TCG PC Client Platform Firmware Profile Specification

|  |  |
|---|---|
| **Type** | spec (TCG) |
| **Maturity** | `standard`: footer marked PUBLISHED |
| **Authors** | Trusted Computing Group, individual contributors not recorded here |
| **Published** | 2023-12-04 (footer) |
| **Identifier** | TCG PC Client Platform Firmware Profile, Level 00 Version 1.06 Revision 52 |
| **Source** | https://www.trustedcomputinggroup.org/resources/documents/pc-client-specific-platform-firmware-profile-specification |
| **Digest** | `sha256:9a308786…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This is the firmware side of PC measured boot. §1 says it fixes what is and is not measured, how it is logged, and which PCR or NV Extend index receives it. PCR[0-7] belong to pre-OS firmware (§3.3), and EV_SEPARATOR marks where firmware gives up control of measurement, which lets software seal to pre-separator values (§3.3). §10 defines the event log formats. New in 1.06 is event log integrity through NV indexes, because SPDM instance data now sits in the log (§10.5).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Defines the content of a PC's evidence |
| Cryptography | `none` | Hash-agile logs. No primitives of its own |
| This project | `none` | Bears on no requirement of ours yet |

- Bears on no `DEC-*` or `R-*` yet. It is kept so an appraisal rule has its source, and nothing in ARCH-0001 asks for boot-state evidence.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **It says what is measured, not what is good.** Reference values are elsewhere.
- **Event log integrity is optional.** §10.5 is framed as something a firmware vendor may provision.
- **Read scope.** §1, the section list, the PCR rule lines in §3.3, EV_SEPARATOR's note and the opening of §10.5 were read, from text search. The event tables and §12 predictive logs were not read. This is a sampled read of a 189-page specification.
