---
schema: "library-summary/v1"
id: tcg-pc-client-pfp
record: tcg-pc-client-pfp
type: summary
updated: "2026-11-04"
---

# TCG PC Client Platform Firmware Profile Specification

|  |  |
|---|---|
| **Type** | spec (TCG) |
| **Maturity** | `standard`: cover and footer marked PUBLISHED; the TCG page lists it as a Specification |
| **Authors** | Trusted Computing Group, PC Client Work Group; individual contributors not recorded here |
| **Published** | 2023-12-04 (footer) |
| **Identifier** | TCG PC Client Platform Firmware Profile, Level 00 Version 1.06 Revision 52 |
| **Source** | https://www.trustedcomputinggroup.org/resources/documents/pc-client-specific-platform-firmware-profile-specification |
| **Digest** | `sha256:9a308786…` (full value in `record.yaml`), fetched 2026-11-01, re-checked 2026-11-04 |

## Overview

This is the firmware side of PC measured boot. §1 says it describes what is and is not measured, how the measurement is captured in a log of events, and into which PCR or NV Extend index it is extended. PCR[0-7] belong to the pre-OS firmware (§3.3, §3.3.1 item 6). EV_SEPARATOR marks where platform firmware relinquishes control of measurement, so firmware can seal a secret to the pre-separator PCR value that OS-resident agents cannot then unseal (note to §3.3.1 item 10). §10 defines the event log formats. 1.06 adds event log integrity through NV indexes, because SPDM instance information now sits in the log (§3.3.6.1, §10.5.1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Defines the content of a PC's evidence |
| Cryptography | `none` | Hash-agile logs. No primitives of its own; §2.5.2 puts mechanism strength out of scope |
| This project | `none` | Bears on no requirement of ours yet |

- Bears on no `DEC-*` or `R-*` yet. It is kept so an appraisal rule has its source, and nothing in ARCH-0001 asks for boot-state evidence.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Relations

- **`cites`** holds the TCG and external specifications of §2.5 and §2.6. The PTP is held as `tcg-pc-client-ptp`; §2.5.3 names it as "Version 2.0, Revision 1.00", and §3.3.6 and §10.5.1 point at PTP 1.06 for the NV index attributes, while the record tracks PTP 1.07. PTP 1.07 dropped the section defining those attributes by mistake; its Errata v1.1 (Errata 6) says the 1.06 requirements still apply. The TPM Library is cited "as released" with no version (§2.5.4), so it is a title gap and not pinned to `tcg-tpm-2-0-library-184` or `-185`.
- **No `see_also`.** `tcg-integrity-event-log` cites this document, and the PTP is under `cites`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, cites, relations, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **It says what is measured, not what is good.** Reference values are elsewhere.
- **Source defects in r52.** §3.3.6.1 still carries an editorial placeholder, "TCG PC Client Platform TPM Profile for TPM 2.0 (insert revision and reference)". §1 names PTP "1.05, or later" while §2.5.3 names PTP "Version 2.0, Revision 1.00".
- **Event log integrity is optional.** §3.3.6.1 says a platform OEM may provision the index, and its normative steps apply "If the Event Log Integrity Feature is supported".
- **Read scope.** §1, §2.5 to §2.6, the §3.3 informative comment and §3.3.1, §3.3.6 to the start of §3.3.6.1's normative steps, and §10.5.1 were read on 2026-11-04. The event tables, §3.3.4 PCR usage, §8 state transitions and §12 predictive logs were not read. This is a sampled read of a 189-page specification.
