---
schema: "library-summary/v1"
id: rfc-4119
record: rfc-4119
type: summary
updated: "2026-11-04"
---

# A Presence-based GEOPRIV Location Object Format

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc4119.json` 2026-11-01 |
| **Authors** | J. Peterson |
| **Published** | 2005-12 |
| **Identifier** | RFC 4119 · DOI 10.17487/RFC4119 |
| **Source** | https://www.rfc-editor.org/rfc/rfc4119.txt |
| **Digest** | `sha256:7d31fc52…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

RFC 4119 extends PIDF so a presence document can carry location, and invents no location format of its own (§1). Its claim is that location and the rules for handling it must travel as one object, so each `geopriv` element must hold both a `location-info` and a `usage-rules` element (§2.2). Those rules state retransmission and retention limits with privacy-preserving defaults: retransmission defaults to no, and retention to 24 hours (§2.2.2). It secures the document as a whole through S/MIME, and rejects element-level protection on the ground that nearly any partial configuration risks privacy leakage (§4).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Carries usage rules with location (§2.2.2), and requires implementations to support S/MIME, applied to the document as a whole (§4) |
| Cryptography | `none` | Delegates all cryptography to S/MIME and CMS (§4) |
| This project | `none` | Bears on no `DEC-*` or `R-*` |

**Bears on no `DEC-*` or `R-*`.** It is held because `draft-ietf-vcon-vcon-core-04` §4.2.9 takes its Civicaddress element names from §2.2.1 (cited as `[GEOPRIV]`).

Two ideas are of interest without being requirements for us. §2.2 binds policy to data inside the signed object, instead of leaving it to the channel. §4 rejects partial protection, which is the opposite pull from vCon's charter aim of disclosing parts of a vCon to different parties (`ietf-vcon-wg`).

## Relations

- `see_also: draft-ietf-vcon-vcon-core-04`: that draft takes its Civicaddress parameter names from §2.2.1 of this RFC, cited as `[GEOPRIV]` (§4.2.9). The edge is authored only here.

## Implementations

**Searched 2026-11-01.** One GitHub repository search for `pidf-lo` (5 results read), which found one implementation. This was not a survey.

| Name | Kind | License | URL |
|---|---|---|---|
| pidf-lo-javascript | open source, JavaScript | MIT | https://github.com/dec112/pidf-lo-javascript |

Its README points to RFC 5491 for PIDF-LO, not to this RFC, and says it "only covers a small portion of the PIDF-LO specification documents" (checked 2026-11-04). Conformance to this RFC was not checked.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `rfc` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **It is not the current civic format.** RFC 5139 revises it, and RFC 5491 and RFC 7459 update the document. vCon cites this RFC for civic labels and RFC 5491 separately for `gml:pos`. Whether vCon's list matches RFC 5139 was not checked.
- **The rules are promises, not enforcement.** §2.2.2 sets what a Recipient may do. Nothing technical stops a Recipient, and `note-well` is for humans only.
- **Policy was unfinished.** §2.2.2 says the GEOPRIV policy requirements were not complete at the time, and full rulesets are left to another document (§1).
- **Errata.** `errata.json` retrieved 2026-11-01, recounted 2026-11-04, lists 3 verified and 1 rejected. Their text was not reviewed.
- **Read scope.** §1, §2.1, §2.2 to the start of §2.2.4, the opening of §4, and §5, from the RFC Editor `.txt`. The remainder of §2.2.1's table, §2.2.4 onward, §3, the rest of §4 and §6 were not read.
