---
schema: "library-summary/v1"
id: google-2016-wosign
record: google-2016-wosign
type: summary
updated: "2026-11-04"
---

# Distrusting WoSign and StartCom Certificates

|  |  |
|---|---|
| **Type** | web (blog post) |
| **Maturity** | unset: a vendor blog post has no published standing to check |
| **Authors** | Andrew Whalley |
| **Published** | 2016-10-31 |
| **Identifier** | Google Security Blog, 2016-10-31 |
| **Source** | https://security.googleblog.com/2016/10/distrusting-wosign-and-startcom.html |
| **Digest** | `sha256:b65e8723…` (full value in `record.yaml`), fetched 2026-11-04. The page embeds a per-render token, so its digest changes between fetches; the post's template block is the stable check (see `content.note`) |

## Overview

Google says GitHub's security team notified it on August 17, 2016 that WoSign had issued a certificate for one of GitHub's domains without authorization. A public investigation, run with Mozilla and the security community, concluded that WoSign knowingly and intentionally misissued, that it had bought StartCom and replaced StartCom's infrastructure, staff, policies and issuance systems with its own, and that the two companies' management tried to mislead the browser community about the acquisition. The post announces that, beginning with Chrome 56, certificates from both CAs issued after October 21, 2016 00:00:00 UTC will not be trusted. Older ones may stay trusted for a time if they comply with Chrome's Certificate Transparency policy or belong to a limited whitelist of known customer domains, and these exceptions are to shrink release by release until full distrust. Google says it cannot trust all pre-existing certificates while protecting users from further misissuance.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | a root program withdrawing trust from whole CAs |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | evidence for R-I-02 |

- **R-I-02** (import SHALL NOT require the foreign object to become a native trust anchor): this is what it costs a relying party when a foreign CA *is* an anchor. The conduct of two commonly owned CAs changed every Chrome user's trust decision, and the remedy had to be a local policy keyed to issuance date, CT compliance and a domain whitelist. That reading is ours; the post argues nothing about trust architecture.

## Implementations

Not applicable: an incident announcement.

## Relations

- `see_also` `mozilla-2013-turktrust`: both are root-program responses to CA misissuance, and they differ in what was removed. Mozilla revoked trust in two mis-issued intermediates, while Chrome distrusted two entire CAs by issuance date.
- The edge to `google-2017-symantec` is authored on that record.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** the whole post, re-read 2026-11-04. The page renders the post from a script template, so the text was taken from that template.

- A party's account of its own decision: the underlying Mozilla investigation was not read. The post gives no certificate counts and does not describe the backdating.
- The post does not say how a certificate's issuance date is established. The date comes from the certificate itself, so a misissuing CA could backdate; that is our inference. The post itself gives only "a number of technical limitations and concerns" as the reason it cannot trust all pre-existing certificates.
- The post states a plan in the future tense. Whether the later Chrome releases followed it was not checked.
