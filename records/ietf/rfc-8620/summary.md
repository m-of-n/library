---
schema: "library-summary/v1"
id: rfc-8620
record: rfc-8620
type: summary
updated: "2026-11-04"
---

# The JSON Meta Application Protocol (JMAP)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc8620.json` 2026-11-01 |
| **Authors** | N. Jenkins, C. Newman |
| **Published** | 2019-07 |
| **Identifier** | RFC 8620 · DOI 10.17487/RFC8620 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8620.txt |
| **Digest** | `sha256:2faef529…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

RFC 8620 is a generic client-server protocol for synchronising data such as mail, calendars and contacts, with the data models left to further specifications (§1). Its argument is about efficiency on mobile and web: batched calls, push in place of polling, and delta updates (§1). Before the protocol it sets strict type conventions: ids restricted to URL-safe base64 characters (§1.2), integers restricted to the range safe in a double (§1.3), and a Date profile of RFC 3339 with one normal form (§1.4).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §8 covers TLS, autodiscovery and JSON parsing for a sync protocol |
| Cryptography | `none` | No cryptographic design in what was read |
| This project | `none` | Bears on no `DEC-*` or `R-*` |

**Bears on no `DEC-*` or `R-*`.** The protocol is unrelated to us. It is held because `draft-ietf-vcon-vcon-core-04` §2.2 copies its notation from §1.1 to §1.5, so §1.3 and §1.4 are effectively normative for vCon's field types.

Two checks against that draft, on -04:

- **Date.** vCon's Date cites §1.4, so a zero fractional second must be omitted and letters must be uppercase. That is stricter than `rfc-3339`, and a reader of the vCon JSON schema descriptions, which cite only RFC 3339, would miss it.
- **UnsignedInt.** vCon calls it a positive integer as defined in §1.3, but §1.3's range starts at 0. So the draft's word and its citation differ on whether 0 is allowed.

## Relations

- `see_also: rfc-3339`: §1.4 defines Date as RFC 3339 `date-time` with two further MUSTs. Authored here; `rfc-3339` does not repeat it.
- `see_also: rfc-8259`: §1.5 makes JSON per RFC 8259 the data encoding, and requires all protocol data to be valid I-JSON, a stricter subset. vCon takes its notation from both. Authored only here.
- `see_also: draft-ietf-vcon-vcon-core-04`: that draft copies its notation from §1.1 to §1.5, cited as `[JMAP]` (its §2.2). Authored only here.

## Implementations

**Searched 2026-11-01.** Only these two projects were checked, for existence and a JMAP mention. This was not a survey, and conformance was not tested.

| Name | Kind | License | URL |
|---|---|---|---|
| Cyrus IMAP | open source, C | BSD-style CMU licence (per `COPYING`; GitHub reports `NOASSERTION`) | https://github.com/cyrusimap/cyrus-imapd |
| Stalwart | open source, Rust | AGPL-3.0-only or the proprietary Stalwart Enterprise License v2 (dual, per README) | https://github.com/stalwartlabs/stalwart |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `rfc` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **Read for its conventions only.** Nothing here assesses JMAP as a protocol.
- **Later RFCs update it.** RFC 9404 (blob management) and RFC 9670 (sharing) are not held. Titles and dates were checked, not their text.
- **Errata.** `errata.json` retrieved 2026-11-01, recounted 2026-11-04, lists 1 verified and 5 reported. Their text was not reviewed, so a defect in §1.3 or §1.4 cannot be excluded.
- **Read scope.** §1, §1.2 to §1.5 (§1.5 added 2026-11-04) and §8.1 to the start of §8.4, from the RFC Editor `.txt`. §1.1 and everything from §1.6 to §7 were not read, nor the rest of §8.
