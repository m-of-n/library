---
schema: "library-summary/v1"
id: google-2016-wosign
record: google-2016-wosign
type: summary
updated: "2026-11-01"
---

# Distrusting WoSign and StartCom Certificates

|  |  |
|---|---|
| **Type** | web (blog post) |
| **Maturity** | `informational`: vendor announcement |
| **Authors** | Andrew Whalley |
| **Published** | 2016-10-31 |
| **Identifier** | Google Security Blog, 2016-10-31 |
| **Source** | https://security.googleblog.com/2016/10/distrusting-wosign-and-startcom.html |
| **Digest** | `sha256:36b4b2d7…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

After GitHub reported an unauthorized certificate on August 17, 2016, a public investigation with Mozilla found that WoSign knowingly misissued, and that it had bought StartCom and replaced its systems while management tried to mislead the community. Chrome 56 stopped trusting certificates from both CAs issued after October 21, 2016, keeping some older ones if they met the CT policy or were on a whitelist, with full distrust to follow. Google says it could not trust all pre-existing certificates while still protecting users.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | the operative enforcement in the Web PKI is removal |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | the relying-party power in R-I-02 |

- **R-I-02**: the relying party, not the certificate, decided what the anchor still meant. Trust here was a local policy with a date in it.

## Implementations

Not applicable: an incident announcement.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** whole. The page renders from a script template, so the text was taken from that template.

- A party's account of its own decision: the underlying Mozilla investigation was not read.
- The cut-off rests on the certificate's own claimed date plus CT, so it depends on logs for pre-existing certificates.
