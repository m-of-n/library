---
schema: "library-summary/v1"
id: rfc-8943
record: rfc-8943
type: summary
updated: "2026-11-01"
---

# Concise Binary Object Representation (CBOR) Tags for Date

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc8943.json` 2026-11-01 |
| **Authors** | M. Jones, A. Nadalin, J. Richter |
| **Published** | 2020-11 |
| **Identifier** | RFC 8943 · DOI 10.17487/RFC8943 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8943.txt |
| **Digest** | `sha256:bb3a6283…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | none found, search 2026-11-01 |

## Overview

RFC 8943 adds two tags for a calendar date with no time of day: 1004 for an RFC 3339 full-date string, and 100 for a signed count of days since 1970-01-01 (§1, §2). It deliberately gives no time zone, so comparing a date with a date/time is out of scope (§1.3). Its §3 is the useful part: a date is a range of instants that differs by location, so a decision based on one depends on where it is made, and a date alone is the wrong trigger for certificate expiry.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §3: ambiguity when a date drives access control or expiry |
| Cryptography | `none` | No cryptography |
| This project | `adjacent` | Evidence for a decided point. The validity lesson is general |

- **DEC-002** and **R-M-12** (now `ARCH-0002` P1): two more registry numbers `ADR-0004` keeps out of the native model.
- It does not bear on R-M-09, which is about intersecting validity windows, but §3 is a reason to express those windows as instants.

## Implementations

**Searched 2026-11-01, none found.** GitHub code search for `RFC8943 cbor` returned nothing. A narrow query, so this is not evidence that none exists.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **Nothing on timescales or leap seconds.** They are stated not to apply (§1). `rfc-9581` covers time in that depth.
- **It cites RFC 7049,** not RFC 8949, as the base specification.
- **Errata.** Search on 2026-11-01 found none.
- **Read scope.** Whole RFC from the cached `.txt`, except the tail of the references.
