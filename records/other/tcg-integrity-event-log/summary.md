---
schema: "library-summary/v1"
id: tcg-integrity-event-log
record: tcg-integrity-event-log
type: summary
updated: "2026-11-01"
---

# TCG Guidance on Integrity Measurements and Event Log Processing

|  |  |
|---|---|
| **Type** | spec (TCG reference guidance) |
| **Maturity** | `best-practice`: guidance, cover typed REFERENCE |
| **Authors** | Trusted Computing Group, individual contributors not recorded here |
| **Published** | 2025-09-10 |
| **Identifier** | TCG Guidance on Integrity Measurements and Event Log Processing, Version 1.0 Revision 131 |
| **Source** | https://www.trustedcomputinggroup.org/resources/guides-and-white-papers/tcg-guidance-integrity-measurements-event-log-processing-v1-0-r131 |
| **Digest** | `sha256:c485ae05…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This explains how a verifier appraises TPM measurements. Signed update and anti-rollback do not show which version is running, so integrity measurements provide that evidence (§2.1). A PCR's value depends on the order of extends, so a composite alone can fail on a harmless reordering, and an event log is what makes appraisal practical (§3.1.3, §3.3.1). The log itself is unprotected: only a quote is signed (§4.1). The verifier therefore replays the log to recompute the PCRs and compares them to the quote.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The clearest account of what a quote does and does not cover |
| Cryptography | `none` | Signature over PCRs only. Notes TPM 1.2's SHA-1 weakness (§4.1) |
| This project | `adjacent` | Measured-boot appraisal, a foreign evidence format |

- **R-M-07**: measurements are content digests of what ran, and an appraisal is a comparison against asserted digests. That parallels how an artifact statement binds content.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Unverified fields stay unverified.** The later sections warn that a log's `eventType` is not verified and may have been altered, and that hint content can be changed arbitrarily.
- **Quote and PCR read can desynchronise.** §4.1 warns against sending PCR reads with a TPM2_Quote, and offers the audit-session method with its costs.
- **Scope is firmware.** DRTM and OS boot loaders are out of scope (§1.1), and r0.118 also excluded anything after appraisal, such as remediation.
- **Read scope.** §2 to §2.3, §3.1.1, §3.1.3, §3.3.1, §4 to §4.1 and §4.3.2 were read in r0.118, with the later warnings found by text search. r131 was compared only by a noisy text diff, which did not cleanly separate edits from extraction differences, and was not read line by line.
