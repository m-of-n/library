---
schema: "library-summary/v1"
id: rfc-9110
record: rfc-9110
type: summary
updated: "2026-11-01"
---

# HTTP Semantics

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Internet Standard, STD 97, confirmed in `rfc9110.json` 2026-11-01 |
| **Authors** | R. Fielding, Ed., M. Nottingham, Ed., J. Reschke, Ed. |
| **Published** | 2022-06 |
| **Identifier** | RFC 9110 · DOI 10.17487/RFC9110 · STD 97 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9110.txt |
| **Digest** | `sha256:21c1cdce…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

RFC 9110 defines the semantics shared by all versions of HTTP, separated from any one wire format: a uniform interface over self-descriptive messages, so that implementation and client purpose stay independent (§1.1). For https it requires a client to verify that the service's identity matches the URI's origin, against configured trust anchors (§4.3.4). It treats a response as a representation chosen for that request, and metadata such as validators describes that selected representation (§8.8). Our reading: a URL names a resource and does not guarantee fixed bytes.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §4.3.4 fixes how an https client verifies a server |
| Cryptography | `none` | Certificate checking is delegated to RFC 6125 (§4.3.4) |
| This project | `none` | Bears on no `DEC-*` or `R-*` |

**Bears on no `DEC-*` or `R-*`.** It is held because `draft-ietf-vcon-vcon-core-04` cites it as `[HTTPS]`: for `url` values (§2.4.1), `x5u` (§5.2.2) and Content-Type on external files.

One thought sits close to **R-M-11** without being a bearing: R-M-11 treats a locator as non-authoritative evidence, and §8.8's wording on selected representations fits that. vCon's own answer is `content_hash`, not anything in this RFC. §8.3 warns that clients may sniff and override the type, which matters where the draft takes the media type from that header.

## Implementations

**Searched 2026-11-01.** Only the one project below was checked. HTTP stacks are ubiquitous, so this is not a survey.

| Name | Kind | License | URL |
|---|---|---|---|
| curl | open source, C | see repo: GitHub reports no SPDX id | https://github.com/curl/curl |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `rfc` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **This record covers only what vCon touches.** A 194-page standard was read in small part, and nothing here should be read as a summary of HTTP.
- **It defines no content integrity.** Nothing read provides a digest of the content. Validators (§8.8) support conditional requests, and are not integrity checks.
- **Errata.** `errata.json` retrieved 2026-11-01 lists 6 verified, 2 reported and 6 rejected. Their text was not reviewed.
- **Read scope.** §1.1, the start of §4.3.4, part of §8.3 and the start of §8.8, from the RFC Editor `.txt`, and the §17 headings. Everything else, including §3, §9 to §16 and the §17 text, was not read.
