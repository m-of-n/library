---
schema: "library-summary/v1"
id: tcg-tpm-1-2-main
record: tcg-tpm-1-2-main
type: summary
updated: "2026-11-04"
---

# TPM Main Specification Version 1.2, Level 2, Revision 116

|  |  |
|---|---|
| **Type** | spec (TCG) |
| **Maturity** | `standard`: marked TCG Published. No retirement notice was found; PTP 1.07 lists SHA-1 as Not Allowed for PC TPMs |
| **Authors** | Trusted Computing Group, individual contributors not recorded here |
| **Published** | 2011-03-01 |
| **Identifier** | TPM Main Level 2, Version 1.2, Revision 116, Parts 1 to 3 |
| **Source** | https://www.trustedcomputinggroup.org/resources/documents/tpm-main-specification |
| **Digest** | `sha256:cc207a7a…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

This is the design that set the pattern for hardware attestation: an Endorsement Key, Attestation Identity Keys, PCRs and an owner secret. Part 1 defines DAA as an optional function with two commands, TPM_DAA_Join and TPM_DAA_Sign, which §33's informative comment calls highly resource intensive; §39 item 6 lists DAA as optional in v1.2. It defines the TPM's mandatory and optional blocks, with cost given as the reason for several options (§39).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Foundational history. Still the reference for what DAA looks like in hardware |
| Cryptography | `adjacent` | Fixed algorithms, with no agility |
| This project | `none` | Bears on no requirement |

- Bears on no `DEC-*` or `R-*` yet. Kept as the lineage behind `brickell-2004-daa`, `tcg-tpm-2-0-library-184` and `iso-iec-11889-2015`.

**Relations.** `see_also: tcg-tpm-2-0-library-184`: TPM 2.0 is the successor family TCG built after this one; TCG does not call it a replacement, so it is not `supersedes`. No `see_also` to `brickell-2004-daa`, because that paper already `cites` this record (its [34]), and none to `iso-iec-11889-2015`, because that record already authors the symmetric `see_also` here.

## Implementations

**Not searched.** The batch did not survey implementations for this record, and none is named in the parts read.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **SHA-1 only.** §4.2.6 requires SHA-1 (FIPS 180-1) and 160-bit hash values everywhere a hash is expected. That is the key difference to Family 2.0's agility.
- **Read scope.** Part 1's cover, section list, §4.2.6, §7 opening, §33 opening and the §39 list were read; re-checked 2026-11-04 against the same bytes. §6 is only a pointer to §11.4, which was not read. Parts 2 and 3 were fetched, digested and not read.
