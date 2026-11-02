---
schema: "library-summary/v1"
id: rfc-5321
record: rfc-5321
type: summary
updated: "2026-11-01"
---

# Simple Mail Transfer Protocol

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Draft Standard, confirmed in `rfc5321.json` 2026-11-01 |
| **Authors** | J. Klensin |
| **Published** | 2008-10 |
| **Identifier** | RFC 5321 · DOI 10.17487/RFC5321 |
| **Source** | https://www.rfc-editor.org/rfc/rfc5321.txt |
| **Digest** | `sha256:7d560edd…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

RFC 5321 consolidates the mail transport protocol, and says it adds no new function (§1.2). Its central distinction is that a mail object is an envelope and content: the envelope holds the originator and recipient addresses, and the content is a header section and body carried in DATA (§2.3.1). It argues against trusting the transport: SMTP mail cannot be authenticated or integrity-protected at the transport level, and real security lies in end-to-end methods over message bodies (§7.1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §7.1: SMTP cannot authenticate or integrity-protect mail at transport level |
| Cryptography | `none` | No cryptographic content in what was read |
| This project | `none` | Bears on no `DEC-*` or `R-*` |

**Bears on no `DEC-*` or `R-*`.**

**vCon cites the wrong layer.** `draft-ietf-vcon-vcon-core-04` §4.3.4 says `[SMTP]` messages have From, To, Cc and Bcc headers, and §4.3.16 that they have a message-id in the SMTP header. By §2.3.1 of this RFC those are header fields of the content, structured per RFC 5322, and the envelope recipients are a separate thing. So for a mail dialog, vCon's parties are taken from what the sender wrote and not from what SMTP carried, and §7.1 says neither is authenticated. RFC 5322 is not held in this library.

## Implementations

**No search run.** Mail transfer agents are not something this project would build on, so none was looked for.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `rfc` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **It does not define header fields.** That is RFC 5322, and `rfc-6068` depends on it too.
- **§7.1 predates current mail authentication.** Nothing read here covers SPF, DKIM or DMARC.
- **A successor may exist.** Metadata shows no obsoleted_by as of 2026-11-01. Work on a revision was not checked.
- **Errata.** `errata.json` retrieved 2026-11-01 lists 3 verified, 6 held and 6 rejected. Their text was not reviewed.
- **Read scope.** §1.1, the start of §1.2, §2.3.1 and §7.1, from the RFC Editor `.txt`, and the §7 headings. This is a 95-page protocol specification read only for what vCon uses. Commands, replies, retry and relay behaviour (§3, §4, §5) and §6 were not read.
