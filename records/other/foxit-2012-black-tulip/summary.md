---
schema: "library-summary/v1"
id: foxit-2012-black-tulip
record: foxit-2012-black-tulip
type: summary
updated: "2026-11-01"
---

# Black Tulip: Report of the investigation into the DigiNotar CA breach

|  |  |
|---|---|
| **Type** | article (forensic report, version 1.0, classification PUBLIC) |
| **Maturity** | `informational`: commissioned investigation, not a standard |
| **Authors** | Hans Hoogstraaten, Ronald Prins, Daniël Niggebrugge, Danny Heppener, Frank Groenewegen, Janna Wettinck, Kevin Strooy, Pascal Arends, Paul Pols, Robbert Kouprie, Steffen Moorrees, Xander van Pelt, Yun Zheng Hu |
| **Published** | 2012-08-13 |
| **Identifier** | Fox-IT project PR-110202 |
| **Source** | Internet Archive capture of the rijksoverheid.nl copy (see Limits) |
| **Digest** | `sha256:63af05c7…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Fox-IT's report for the Dutch state reconstructs the DigiNotar compromise. The perimeter was breached on June 17, 2011 through web servers in the external DMZ, the segment holding the CA servers on July 1, and the first rogue certificate issued on July 10. All eight servers that managed Certificate Authorities were compromised, and a "non-exhaustive list of 531 rogue certificates" was identified. A rogue `*.google.com` certificate then served a man-in-the-middle attack: OCSP logs show 298,140 unique IP addresses, 95% of them from Iran. Serial numbers that did not match DigiNotar's records mean further unknown rogue certificates cannot be excluded, because the logs sat on the compromised servers and had been tampered with.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | a single CA's compromise produced trusted certificates for names it had no relationship with |
| Cryptography | `adjacent` | the failure is operational and structural, not cryptographic |
| This project | `adjacent` | evidence for a design choice, not a constraint on an encoding |

- **R-M-03** (names interpreted only relative to an issuing principal): the attacker needed one CA to speak for `google.com`. Nothing in the certificate tied that name to that issuer, which is the condition R-M-03 removes.
- **R-I-02** (import must not make the foreign object a native trust anchor): the report's closing concern is erosion of trust in the PKI as a whole, which is what follows when one anchor speaks for every name.

## Implementations

Not applicable: an incident report, nothing to build on.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** the 101-page report from an Internet Archive capture of 2013-10-15, because the government URL now 404s. Management and investigative summaries read in full, plus the timeline note on Chrome. Chapters 4 to 10 were searched by keyword for the figures here, not read through.

- 531 is a floor. The report calls the list non-exhaustive, so it should not be cited as the total.
- The report says "approximately 300,000 users" in its summary, but the measured number is 298,140 unique IP addresses, and Internet Explorer 6 users are excluded because they make no OCSP request.
- Detection by Chrome rests on a user's forum post and footnote 4's description of certificate pinning. The report does not draw the lesson that R-001 §4.8 draws about what sits outside X.509; that reading is ours.
- It says nothing about how name constraints would have changed the outcome.
