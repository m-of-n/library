---
schema: "library-summary/v1"
id: rfc-3339
record: rfc-3339
type: summary
updated: "2026-11-01"
---

# Date and Time on the Internet: Timestamps

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc3339.json` 2026-11-01 |
| **Authors** | G. Klyne, C. Newman |
| **Published** | 2002-07 |
| **Identifier** | RFC 3339 · DOI 10.17487/RFC3339 |
| **Source** | https://www.rfc-editor.org/rfc/rfc3339.txt |
| **Digest** | `sha256:9ab2b886…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

RFC 3339 profiles ISO 8601 into one timestamp form for Internet protocols, on the view that the full ISO grammar is too complex and that most fields should be mandatory (§5.5). A timestamp names an instant, and every time has a stated relationship to UTC: intervals are out of scope (§1). The design values sortability (§5.1), no redundant fields (§5.4) and at most one rarely used option, fractional seconds (§5.3). It separates an offset of `-00:00`, meaning UTC is known but the local offset is not, from `Z` and `+00:00` (§4.3).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | §7 notes only that a local offset can reveal when a site is less monitored |
| Cryptography | `none` | No cryptographic content |
| This project | `none` | Bears on no `DEC-*` or `R-*`. Reachable from vCon only |

**Bears on no `DEC-*` or `R-*`.** R-M-09 asks for validity intersection over time windows, but a search of mofn `origin/main` `spec/` and `project/DECISIONS-0001.md` found no adoption of this format for it. The one mention is in the withdrawn YAML notes, `ARCH-0001-PROPOSAL-v0.2.0` Appendix A.

It is held because `draft-ietf-vcon-vcon-core-04` §2.2 defines its Date type by it. That draft reaches it through `rfc-8620` §1.4, which is stricter: no zero fractional part and uppercase letters. So vCon's Date is a narrower form than RFC 3339 alone, and a reader should check `rfc-8620`.

## Implementations

**Searched 2026-11-01.** Only the one project below was checked. This was not a survey.

| Name | Kind | License | URL |
|---|---|---|---|
| chrono | open source, Rust | see repo: GitHub reports no SPDX id | https://github.com/chronotope/chrono |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `rfc` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **It does not give one byte form per instant.** Offsets, optional fractions and lowercase `t` and `z` (§5.6) all give different strings for one instant, and §5.1 says string sorting needs the same zone and the same fraction width. It is no canonical form.
- **It is not current on its own.** RFC 9557 updates it and is not held here, so its effect on §4.3 was not assessed.
- **Its leap-second table stops at 1998** (Appendix D). The live source must be consulted.
- **§5.6 allows a space for `T` only in a note.** The ABNF does not allow it, so parsers may reasonably differ.
- **Errata.** `errata.json` retrieved 2026-11-01 lists 4 verified and 3 held. Their text was not reviewed.
- **Read scope.** Whole document, from the RFC Editor `.txt`.
