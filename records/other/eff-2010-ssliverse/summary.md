---
schema: "library-summary/v1"
id: eff-2010-ssliverse
record: eff-2010-ssliverse
type: summary
updated: "2026-11-04"
---

# An Observatory for the SSLiverse

|  |  |
|---|---|
| **Type** | paper (in fact a 47-slide conference deck, see Limits) |
| **Maturity** | unset: talk slides, not peer reviewed; no body assigns them a standing |
| **Authors** | Peter Eckersley, Jesse Burns |
| **Published** | 2010-07 |
| **Identifier** | DEF CON 18 talk |
| **Source** | https://www.eff.org/files/defconssliverse.pdf |
| **Digest** | `sha256:f88c056a…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-03 and 2026-11-04 |

## Overview

The EFF scanned IPv4 for port 443 and collected the certificate chains, finding 16.2M listening IPs, 10.8M starting a handshake, and 1.3+M distinct valid leaves (slide 14). Slide 5 frames it as "Trust model: 1 of N CAs (N is large)" and asks how large N is. Slide 19 counts 1,482 CA certificates trustable by Windows or Firefox, from 651 organisations, and closes with "If a CA can sign for one domain, it can sign for any domain". Slide 45 asks, without answering, whether the CA model is fundamentally broken.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | sizes the population that holds global signing power |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | historic baseline for R-M-03 |

- **R-M-03** (names interpreted only relative to an issuing principal): slide 19's "any domain" line states the condition R-M-03 exists to remove.

## Implementations

The deck used NMap, a custom Python client and OpenSSL (slides 8 to 10). Not evaluated.

## Relations

- `see_also` `foxit-2012-black-tulip`: DigiNotar is the realised case of slide 19's condition: one CA among many issued a trusted `*.google.com` certificate.
- `see_also` `survey-2026-nameconstraints-measurement`: our 2026 count of the same trusted-CA population; the counts are not comparable (see Limits).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** all 47 slides as extracted text; figures on image-only slides (22, 23, 38 to 41) were not read. Quotes and slide numbers re-checked against the PDF 2026-11-04.

- **`type: paper` is wrong for what this is.** It is a slide deck, so it has no prose argument, and it is not peer reviewed. The type was left alone for a reviewer to decide.
- **A quotation R-001 attributes to this record is not in it.** R-001 §4.8 cites this record for "the security of HTTPS is only as strong as the practices of the least trustworthy/competent CA". That sentence is not in the deck. It is on EFF's SSL Observatory project page, https://www.eff.org/observatory, checked 2026-11-04. R-001 should cite that page, which the library does not yet hold.
- 2010 counts. 651 organisations is the deck's own number and it warns that ownerships and jurisdictions overlap.
- Counts of CA certificates include subordinates, so it is not comparable with the 50 owners of `survey-2026-nameconstraints-measurement`.
