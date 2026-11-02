---
schema: "library-summary/v1"
id: pics-censorship-faq
record: pics-censorship-faq
type: summary
updated: "2026-11-01"
---

# PICS, Censorship, and Intellectual Freedom FAQ

|  |  |
|---|---|
| **Type** | web (W3C white paper) |
| **Maturity** | `informational`: "no techincal standing" and no official policy standing, by its own status section (sic) |
| **Authors** | Paul Resnick, University of Michigan (editor) |
| **Published** | Last revised 4 August 1999 |
| **Identifier** | https://www.w3.org/PICS/PICS-FAQ-980126.html |
| **Source** | https://www.w3.org/PICS/PICS-FAQ-980126.html |
| **Digest** | `sha256:a46df860…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

W3C's reply to civil-liberties critics. Its core move is to separate labelling from filtering, and six roles any of which an independent party can fill: PICS itself fills none. It concedes much: PICS makes some controls easier, so more controls should be expected, and anyone can label anyone's site without approval. It nevertheless argues the net effect favours individual over central control, because a national blocklist gains little from interoperability while mixing labels and filters from different sources gains a lot. W3C takes no position on which content should be illegal, and offers only technical feedback to governments.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Abuse of labelling power is addressed, by market diversity |
| Cryptography | `none` | Mentions DSig only in passing |
| This project | `adjacent` | The closest thing to a defence of third-party assertions |

It bears on no open `DEC-*` or `R-*`. The role split maps well onto issuer, verifier and policy in mofn, and its answer to abusive labellers (monitor them, keep the market diverse) is the only answer on file.

`contradicts: aclu-fahrenheit-451-2`: see that record for the reason. The two disagree on the direction of the net effect.

## Implementations

None applicable: a FAQ. It names RSACi, SafeSurf, CyberPatrol and Net Shepherd as contemporaries. Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: a summary-bar fill, and a `web` record is outside FX-1 scope.

## Limits

Read: status, abstract, background, the government and labelling questions, and W3C's roles section. The filtering questions after "Other Social Concerns" were read only in part. Its own status section says it is not W3C policy beyond describing positions taken.

The substitution effect is argued, not measured, and the FAQ admits it is unclear how strong it would be. It predates the outcome: nothing here explains why PICS was not used. Its condition for self-labelling to work, a high share of materials labelled, is exactly what `gvu-1998-webmaster-survey` shows was not met.
