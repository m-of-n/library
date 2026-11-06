---
schema: "library-summary/v1"
id: google-2017-symantec
record: google-2017-symantec
type: summary
updated: "2026-11-04"
---

# Chrome's Plan to Distrust Symantec Certificates

|  |  |
|---|---|
| **Type** | web (blog post) |
| **Maturity** | unset: a vendor blog post has no published standing to check |
| **Authors** | Devon O'Brien, Ryan Sleevi, Andrew Whalley |
| **Published** | 2017-09-11 |
| **Identifier** | Google Security Blog, 2017-09-11, updated 2018-01-31 |
| **Source** | https://security.googleblog.com/2017/09/chromes-plan-to-distrust-symantec.html |
| **Digest** | `sha256:428d479c…` (full value in `record.yaml`), fetched 2026-11-04. The page embeds a per-render token, so its digest changes between fetches; the post's template block is the stable check (see `content.note`) |

## Overview

A January 19, 2017 posting to mozilla.dev.security.policy drew attention to questionable certificates from Symantec's PKI, and the investigation found Symantec had entrusted several organisations with issuance without appropriate oversight. The post announces a phased plan, already settled on blink-dev: Chrome 66 to remove trust in Symantec-issued certificates issued before June 1, 2016; issuance to move to DigiCert-operated Managed Partner Infrastructure by December 1, 2017, with later certificates from the old infrastructure not trusted; and Chrome 70, due around October 23, 2018, to remove trust in the old infrastructure and all its certificates, except a small number from independently operated, audited subordinate CAs previously disclosed to Google. The staging exists to give site operators time to replace certificates.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | the cost of withdrawing a widely trusted anchor |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-I-02 |

- **R-I-02** (import SHALL NOT require the foreign object to become a native trust anchor): withdrawing one large CA took a plan spanning more than a year, because every site chaining to it had to move first. By our reading that is the exposure R-I-02 avoids, and per-issuer local scope would bound the cost; the post argues nothing about trust architecture.

## Implementations

Not applicable: an incident announcement.

## Relations

- `see_also` `google-2016-wosign`: the same root program acting against CAs a year earlier. That post distrusted two CAs from one issuance cut-off, with exceptions to be reduced over later releases; this one staged the distrust of a larger CA across several releases and a change of operator.
- No edge to `rfc-6962`: this post does not mention Certificate Transparency (see Limits), so there is no stated reason for one.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** the whole post, re-read 2026-11-04 from the page's script template, including the reference timeline.

- **mofn R-0001 §4.8 says Symantec was "caught by CT" and cites this post for it. This post does not say that.** It attributes the discovery to the newsgroup posting and does not mention Certificate Transparency anywhere. The claim needs another source; R-0001's own mini-report B attaches "caught by CT" to Symantec's 2015 test certificates, a separate incident this post mentions only as "a previous incident in 2015".
- Dates marked with `~` in the post are its estimates. Actual Chrome release dates, and whether the plan was carried out as written, were not checked.
- The post gives no certificate counts.
