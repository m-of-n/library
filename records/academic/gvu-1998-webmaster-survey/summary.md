---
schema: "library-summary/v1"
id: gvu-1998-webmaster-survey
record: gvu-1998-webmaster-survey
type: summary
updated: "2026-11-04"
---

# GVU 9th WWW User Survey: webmaster PICS labelling rates

|  |  |
|---|---|
| **Type** | dataset (survey result tables, webmaster section) |
| **Maturity** | `informational`: a survey result, not a standard |
| **Authors** | None named on the result pages; published by GVU. The survey home page names Colleen Kehoe, James Pitkow and Juan Rogers as authors of the separate 9th survey report, not of these tables |
| **Published** | 1998. Fielded 10 April to 15 May 1998 |
| **Identifier** | https://sites.cc.gatech.edu/gvu/user_surveys/survey-1998-04/graphs/webmaster/q69.htm |
| **Source** | https://sites.cc.gatech.edu/gvu/user_surveys/survey-1998-04/graphs/webmaster/q69.htm |
| **Digest** | `sha256:7092a1a1…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

Of 784 webmasters answering the 1998 GVU survey, 636 (81.1%) said none of their site's content carried a PICS rating (q69). The rest split thinly: 4.6% all rated, 0.9% most, 3.2% some, 5.0% little, 5.2% a single site-wide rating. Intent was only slightly better: 553 (70.5%) planned to rate nothing (q70). This is the measured supply-side failure of PICS self-labelling, about eighteen months after the label format reached Recommendation.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | Measures adoption, not a security property |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Primary evidence for the claim that unpaid self-labelling yields no statements |

It bears on no open `DEC-*` or `R-*`. It is evidence for mofn R-0004 §6 and for condition C1 (near-zero supply cost) of the model in R-0004 §7. It sets no requirement.

## Relations

- `see_also: pics-1-1-labels`: the label format whose uptake q69 and q70 measure.
- The `pics-censorship-faq` and `aclu-fahrenheit-451-2` edges are authored on those records, with their reasons. The `w3-org-pics` edge was dropped: it adds nothing the label specification does not.

## Implementations

None applicable: this is survey data. Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this file |

No `distilled/`: this is a summary-bar fill, and a `dataset` record is outside FX-1 scope.

## Limits

Read: q69 and q70 whole, including the location and gender breakdowns, plus the question text of q68 and q71 and the survey home page. The home page says the survey was endorsed by W3C, which published PICS; nothing here shows that affected the webmaster answers. The methodology pages were not read, so this record makes no claim about sampling; 784 is the respondent count, not a population. Self-reported, and 1998 only, so it shows no trend. It does not say why webmasters did not rate.

**Disagreement with mofn.** R-001 §6.2 and R-0004 §6 cite this record as the "10th" survey with "roughly 82%" rating nothing, and R-001 §6.4 repeats "82% declined". The pages say Ninth and 81.1%. The 70.5% figure is correct. The sources must be corrected in mofn, not here.
