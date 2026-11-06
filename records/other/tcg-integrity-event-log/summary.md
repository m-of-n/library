---
schema: "library-summary/v1"
id: tcg-integrity-event-log
record: tcg-integrity-event-log
type: summary
updated: "2026-11-04"
---

# TCG Guidance on Integrity Measurements and Event Log Processing

|  |  |
|---|---|
| **Type** | spec (TCG guidance) |
| **Maturity** | `best-practice`: the TCG page files it as a Guide; footer says Published, cover banner REFERENCE |
| **Authors** | Trusted Computing Group, Infrastructure Work Group; individual contributors not recorded here |
| **Published** | 2025-09-10 |
| **Identifier** | TCG Guidance on Integrity Measurements and Event Log Processing, Version 1.0 Revision 131 |
| **Source** | https://www.trustedcomputinggroup.org/resources/guides-and-white-papers/tcg-guidance-integrity-measurements-event-log-processing-v1-0-r131 |
| **Digest** | `sha256:c485ae05…` (full value in `record.yaml`), fetched 2026-11-01, re-checked 2026-11-04 |

## Overview

This explains how a verifier appraises TPM measurements. Signed update and anti-rollback do not show which version is running, so integrity measurements provide that evidence (§2.1). A PCR's value depends on the order of extends, so a composite alone can fail on a harmless reordering, and an event log is what makes appraisal practical (§4.1.3, §4.3.1). The log is stored and transported without protection of its own (§4.3.2); what is signed is the quote over PCR values (§5.1), and the guidance tells the verifier to treat the log as untrusted and possibly malicious (§5.4.1). The verifier therefore replays the log to recompute the PCRs and compares them to the quote (§5.4.1, §5.4.2, worked through for a Linux endpoint in §7.2).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The clearest account of what a quote does and does not cover |
| Cryptography | `none` | Uses a signature over PCR digests and hash-agile banks; defines no primitive |
| This project | `adjacent` | Measured-boot appraisal, a foreign evidence format |

- Bears on no `DEC-*` or `R-*` yet. An earlier version of this record set `R-M-07`, on the analogy that a measurement is a content digest as an artifact statement's subject is. That is our analogy and the document does not speak to artifact statements, so the edge was removed. Nothing in ARCH-0001 asks for boot-state evidence.

## Implementations

**Not searched.** The reference list names HIRS ([8]) and the IBM TPM Attestation Client Server ([9]) as examples, and sbsigntools ([10]) for computing normalised EFI hashes (§7.2.5). None was evaluated here, and their licences were not checked.

## Relations

- **`cites`** holds the reference list (§8). The TPM 2.0 Library it cites is Revision 01.84 of March 2025, held as `tcg-tpm-2-0-library-184`; the PFP it cites is 1.06 r52, held as `tcg-pc-client-pfp`.
- **No `see_also`.** The PFP and TPM library are under `cites`. An earlier `see_also` from `draft-ietf-rats-corim` to this record was removed in that record's own check, since CoRIM does not mention event logs.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, cites, relations, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Unverified fields stay unverified.** Only digests contribute to the PCRs, so `eventType` and event data may be completely unverified (§7.1). §7.2.5 says `eventType` may have been altered by an attacker and can be used only as a hint, that path "hints" can be freely modified, and that the first EV_NO_ACTION event can be changed arbitrarily and must be ignored.
- **Quote and PCR read can desynchronise.** §5.1 warns that sending TPM2_PCR_Read values with a TPM2_Quote can cause problems, and offers the audit-session method, with its costs, for the hibernation case.
- **A newer integrity mechanism is pointed to, not described.** §5.4.1 notes the NV-index event log integrity introduced in PFP 1.06 and describes only the traditional PCR-replay method.
- **Source defect.** Footnote 6, on §4.3.2, says the Integrity Measurement Record "is not introduced until Section 3.3.4"; r131 has no §3.3.4 (its §3 is a one-page Overview), a cross-reference left over from r0.118's numbering.
- **Scope is firmware.** DRTM and OS boot loaders and OS measurements such as IMA are out of scope, and so is anything after the verifier's appraisal step, such as remediation (§1.1).
- **Read scope.** r131 was read in §1 to §5.4.2, §6.1, §7.1, §7.2.5 and §8, on 2026-11-04. §5.3.1 to §5.3.3, §6.2 to §6.3, the rest of §7 and Appendix A were skimmed or not read. An earlier read of r0.118 is superseded by this one; r0.118's remark in its §4.1 that TPM 1.2's SHA-1-only quote may be too weak does not appear in r131.
