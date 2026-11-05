---
schema: "library-summary/v1"
id: rfc-9581
record: rfc-9581
type: summary
updated: "2026-11-05"
---

# Concise Binary Object Representation (CBOR) Tags for Time, Duration, and Period

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9581.json` 2026-11-01 |
| **Authors** | C. Bormann, B. Gamari, H. Birkholz |
| **Published** | 2024-08 |
| **Identifier** | RFC 9581 · DOI 10.17487/RFC9581 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9581.txt |
| **Digest** | `sha256:7c81cc73…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | none found, search 2026-11-01 |

## Overview

RFC 9581 extends CBOR time past tags 0 and 1 with tag 1001, a map holding a base time plus optional higher precision, timescale, clock quality and time-zone hints (§2, §3). Tags 1002 and 1003 add durations and periods (§4, §5). The map has a real extensibility rule: unknown negative or text keys are ignored as elective, and unknown unsigned keys are an error as critical (§3). New keys and timescales go to two new IANA registries (§7.2, §7.3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §8: ambiguity where time decides freshness or validity, and disclosure of clock details |
| Cryptography | `none` | No cryptography |
| This project | `adjacent` | Evidence for a decided point, and a design worth comparing |

- **DEC-002**: `ADR-0004`'s profile cannot carry this. It uses tags and allows floats as base time, decimal-fraction and bigfloat content (the unwrapped content of tags 4 and 5), and `null` in periods (§3.1, §3.2, §5). Tags, floats and `null` are all forbidden natively.
- **R-M-12** (now `ARCH-0002` P1): a CBOR tag plus two further registries for keys and timescales. The elective and critical split is still worth comparing if our own extension points need one.
- It does not bear on R-M-09: §5 defines a period but no intersection of periods.

## Implementations

**Searched 2026-11-01, none found.** GitHub code search for `RFC9581 cbor` returned nothing, as did `"tag 1001" cbor etime`. A narrow query, so this is not evidence that none exists.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **No deterministic encoding is defined.** The word does not occur in that sense. Figure 4 shows one uncertainty written three ways, and keys -1 and -13 have identical semantics (§3.4).
- **§8 is thin.** It defers to RFC 8949 and to RFC 9557 §7, which is not held here.
- **Clock-quality claims are unverified statements by the sender.** §3.5.5 itself calls the guarantee unattainable in theory.
- **Errata.** Search on 2026-11-01 found none.
- **Read scope.** §1 to §8 of the cached `.txt` in full. Appendix A (collected CDDL) was not read separately, and the references were skimmed.
