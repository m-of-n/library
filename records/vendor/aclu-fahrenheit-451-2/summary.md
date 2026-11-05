---
schema: "library-summary/v1"
id: aclu-fahrenheit-451-2
record: aclu-fahrenheit-451-2
type: summary
updated: "2026-11-04"
---

# Fahrenheit 451.2: Is Cyberspace Burning?

|  |  |
|---|---|
| **Type** | web (white paper) |
| **Maturity** | `white-paper`: so described in its credits |
| **Authors** | Ann Beeson, Chris Hansen, Barry Steinhardt (principal authors) |
| **Published** | Page dated 17 March 2002; the text is from after 26 June 1997 |
| **Identifier** | https://www.aclu.org/documents/fahrenheit-4512-cyberspace-burning |
| **Source** | https://www.aclu.org/documents/fahrenheit-4512-cyberspace-burning |
| **Digest** | `sha256:6b0cd495…` (full value in `record.yaml`), fetched 2026-11-04; the 2026-11-01 bytes differed, see `record.yaml` note |

## Overview

After *Reno v. ACLU*, the ACLU warns that voluntary rating and blocking could do what the Communications Decency Act could not. Its projected path: PICS becomes universal, one or two rating systems dominate, they ship as browser defaults, unrated speech is blocked, search engines drop it, and governments make self-rating mandatory. Six reasons oppose self-rating, including that it will censor controversial speech, that it is burdensome and costly (one site has more than 26,000 pages to rate), and that it will favour large commercial speakers. Third-party rating does not rescue it: unrated sites may still be blocked, and speakers are not told. Home blocking software is the lesser evil, if lists are disclosed and users stay in control.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | A threat model from the subject's side, not the attacker's |
| Cryptography | `none` | Never mentions signatures or cryptography |
| This project | `core` | The political objection any third-party statement system must meet |

It bears on no open `DEC-*` or `R-*`, which is itself a gap: no requirement addresses it. Its burden argument is the supply-side finding of `gvu-1998-webmaster-survey`, stated before the data.

## Relations

- `contradicts: pics-censorship-faq`. The FAQ's abstract argues the net impact of PICS will be to shift government policies away from centralized controls and toward individual controls. This paper projects the opposite path and calls it "theoretical but inevitable". Both cannot be right as predictions. The edge is authored here only; it also covers the relation a `see_also` would have named.
- `see_also: pics-1-1-labels`: the label format whose universal use is the first step of this paper's projected path.
- `see_also: gvu-1998-webmaster-survey`: the survey measures the supply-side burden Reason #2 predicts.

## Implementations

None applicable: an advocacy paper. Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, and a `web` record is outside FX-1 scope.

## Limits

Read: executive summary, the six reasons, the third-party and home-blocking sections, most of the library section, and the appendix's end, from the ACLU's page. Date: the 2002 page date is a posting date, and the original date was not established from what we read.

It is advocacy, and it gives no measurements. Its target is rating for blocking; it says nothing about provenance or statements that name their issuer.

**Caution for mofn.** R-0004 §6 paraphrases the argument as a "general-purpose, cryptographically enforceable mechanism". The paper never mentions cryptography, and its main target is self-rating. The extension to signed assertions is R-0004's argument, not the ACLU's. R-0004 also cites `R-M-07` for the label-bureau pattern, but on mofn main `R-M-07` only requires a content digest.
