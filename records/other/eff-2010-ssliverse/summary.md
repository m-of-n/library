---
schema: "library-summary/v1"
id: eff-2010-ssliverse
record: eff-2010-ssliverse
type: summary
updated: "2026-11-01"
---

# An Observatory for the SSLiverse

|  |  |
|---|---|
| **Type** | paper (in fact a 47-slide conference deck, see Limits) |
| **Maturity** | `informational`: talk slides, not peer reviewed |
| **Authors** | Peter Eckersley, Jesse Burns |
| **Published** | 2010-07 |
| **Identifier** | DEF CON 18 talk |
| **Source** | https://www.eff.org/files/defconssliverse.pdf |
| **Digest** | `sha256:f88c056a…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

The EFF scanned IPv4 for port 443 and collected the certificate chains, finding 16.2M listening IPs, 10.8M starting a handshake, and 1.3+M distinct valid leaves. Its question was the deck's phrase "Trust model: 1 of N CAs (N is large)": it counted 1,482 CA certificates trustable by Windows or Firefox, from 651 organisations. The point follows on the same slide: "If a CA can sign for one domain, it can sign for any domain". It asks, without answering, whether the CA model is fundamentally broken.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | sizes the population that holds global signing power |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | historic baseline for R-M-03 |

- **R-M-03**: the "any domain" slide states the condition R-M-03 exists to remove.

## Implementations

The deck used NMap, a custom Python client and OpenSSL. Not evaluated.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** all 47 slides as extracted text; figures on image-only slides were not read.

- **`type: paper` is wrong for what this is.** It is a slide deck, so it has no prose argument, and it is not peer reviewed. The type was left alone for a reviewer to decide.
- **A quotation in R-001 is not here.** §4.8 attributes to this source "the security of HTTPS is only as strong as the practices of the least trustworthy/competent CA". That sentence does not occur in the text of this PDF. It may come from EFF's project pages, but we did not find it, so it should be re-sourced or dropped.
- 2010 counts. 651 organisations is the deck's own number and it warns that ownerships and jurisdictions overlap.
- Counts of CA certificates include subordinates, so it is not comparable with the 50 owners of `survey-2026-nameconstraints-measurement`.
