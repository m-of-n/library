---
schema: "library-summary/v1"
id: cabforum-tls-br
record: cabforum-tls-br
type: summary
updated: "2026-11-04"
---

# Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard`: adopted CA/Browser Forum requirements, not an IETF or ISO standard |
| **Authors** | CA/Browser Forum |
| **Published** | 2026-10-04 (v2.3.1, SC104 effective date) |
| **Identifier** | TLS BR v2.3.1 |
| **Source** | https://github.com/cabforum/servercert/blob/main/docs/BR.md (raw) |
| **Licence** | CC BY 4.0 (front matter) |
| **Digest** | `sha256:ee4e4e95…` (full value in `record.yaml`), fetched 2026-11-01, re-checked 2026-11-04 |

## Overview

The Baseline Requirements bind publicly trusted TLS CAs. Two themes bear on this topic. Scope: §7.1.2.5.2 defines how a Technically Constrained TLS Subordinate CA encodes Name Constraints and, as "an explicit exception from RFC 5280", says the extension SHOULD be critical but MAY be non-critical for legacy applications; §7.1.2.10.8 says the same for CA certificates generally. Lifetime: §6.3.2 sets maximum Subscriber validity at 200 days from 2026-03-15, 100 from 2027-03-15 and 47 from 2029-03-15. Short-lived Subscriber Certificates (≤7 days when issued from 2026-03-15, §1.6.1) are carved out of the revocation duties: §4.9.1.1 says the CA MAY support their revocation.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | the operative rules of the Web PKI |
| Cryptography | `none` | no direct bearing |
| This project | `adjacent` | what an X.509 import can assume |

- **R-I-05**: a BR-conformant certificate is the most common X.509 object an importer will see, and its scope constraint may be legitimately non-critical, which is one reason to treat it only as a foreign assertion about a key.
- **R-O-02**: the validity schedule is that requirement arriving by policy, while §4.9.7 keeps CRL publication mandatory, so revocation stays representable.

## Relations

- `contradicts: rfc-5280`: the BR's own words call the non-critical Name Constraints allowance "an explicit exception from RFC 5280", which requires the extension be critical.
- `see_also: cabforum-smime-br`: the sibling Forum requirements, which make the same non-critical exception for S/MIME and state the condition for retiring it.
- `see_also: rfc-9608`: the IETF's `noRevAvail` marker is the profile-level way to say a certificate has no revocation information. The BR's Short-lived Subscriber Certificates are the case it fits: the CRL Distribution Points extension is OPTIONAL in them (§7.1.2.11.2) and the CA MAY support their revocation (§4.9.1.1). The BR does not reference RFC 9608 or `noRevAvail`.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** front matter, the effective-dates and revision tables, §4.9.1.1, the opening of §4.9.7, §6.3.2's validity lines, §7.1.2.5.2, §7.1.2.10.8, §7.1.2.11.2, and the definition of Short-lived Subscriber Certificate. Not read through: domain validation, audit and most of §7.

- It binds CAs, not relying parties, so it does not say what a client enforces.
- R-001 §4.4's "explicitly exclude the universe" is R-001's own phrase, not the BR's; the rule it describes is the Entire Namespace Exclusion column of the second table in §7.1.2.5.2 in this version.
- A moving document: cite the version.
