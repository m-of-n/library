---
schema: "library-summary/v1"
id: survey-2026-nameconstraints-measurement
record: survey-2026-nameconstraints-measurement
type: summary
updated: "2026-11-04"
---

# Name-constraint prevalence among CCADB-disclosed intermediate CA certificates (original measurement, 2026-09-26)

|  |  |
|---|---|
| **Type** | dataset (original measurement, re-run) |
| **Maturity** | unset: an unreviewed measurement of ours; no body assigns it a standing |
| **Authors** | m-of-n research survey R-001, area B |
| **Published** | 2026-09-26 |
| **Identifier** | mofn R-001 §4.5 |
| **Source** | CCADB public report (see Limits) |
| **Digest** | `sha256:d7de84aa…` (full value in `record.yaml`), fetched 2026-11-04; the report changes as certificates are disclosed, so earlier digests do not match (see `content.note`) |

## Overview

R-001 §4.5 reported that 31 of 1,769 CCADB-disclosed intermediate CA certificates in Mozilla's program carried `nameConstraints` on 2026-09-26, and 2 of those marked it critical. We re-ran the count with `openssl x509 -noout -text` over every PEM in the report on 2026-11-01, **31 of 1,758 (1.8%), 2 critical**, and again on 2026-11-04, **31 of 1,755, 2 critical**. The result is stable. 29 of the 31 are issued under Hellenic Academic and Research Institutions (HARICA), 1 under Actalis and 1 under TunTrust, and the 2 critical ones are the two non-HARICA certificates (AgID CA SSL SERVER, TunTrust Services CA). Of 169 included roots from 50 owners, 3 have a "Mozilla Applied Constraints" value, and only one is a positive scope (`*.tr`); the other two say no constraints apply.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | says how much of the Web PKI is actually scoped |
| Cryptography | `none` | counts an extension |
| This project | `core` | the deployed baseline any argument for structural scoping is measured against |

- **R-M-03** (names interpreted only relative to an issuing principal): under 2% of disclosed intermediates carry the mechanism PKIX offers in place of RFC 1422's structural rule.
- **R-M-01** (native encoding SHALL NOT be X.509 / PKIX): R-001 §4.9 gives this count as one of five reasons X.509 does not, in practice, supply scoped delegation. It is evidence for the rationale, not a test of the requirement.

## Implementations

Not applicable. The method is `openssl x509 -noout -text` over the report's PEM column, OpenSSL 3.6.4.

## Relations

- `see_also` `ccadb`: the record for the CCADB public reports this measurement is computed from.
- `see_also` `rfc-5280`: defines the `nameConstraints` extension counted here and requires it be marked critical, which is the test behind the "2 critical" figure.
- `see_also` `cabforum-tls-br`: the Baseline Requirements let a CA mark Name Constraints non-critical, so the 29 non-critical certificates need not break the Forum's rules.
- `see_also` `golang-61963`: the one positive root-store scope found here, `*.tr`, is the constraint Go's root bundle failed to carry.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. This is not a specification, so FX-1 does not apply to it.

## Limits

**Read:** the whole CSV, every certificate parsed, none failed, on both re-runs. The script was not committed and is described in R-001 §4.5.

| | R-001, 2026-09-26 | re-run, 2026-11-01 | re-run, 2026-11-04 |
|---|---|---|---|
| Intermediates | 1,769 | 1,758 | 1,755 |
| With `nameConstraints` | 31 | 31 | 31 |
| Marked critical | 2 | 2 | 2 |
| Included roots | 172 | 169 | 169 |
| Websites / Email trust bits | 121 / 91 | 118 / 88 | 118 / 88 |
| CA owners | 50 | 50 | 50 |

- **R-001's count of 1,613 `serverAuth`-capable intermediates is not reproduced as such.** On 2026-11-04, 1,616 certificates name `serverAuth` in EKU (1,619 on 2026-11-01) and the other 139 have no EKU extension at all, and no EKU does not limit a CA. So every certificate in the set is capable by that reading, and the 1.9% figure depends on a definition R-001 does not state. All 31 constrained certificates do name `serverAuth`.
- It covers Mozilla's disclosed set only: no other root program and no private PKI. That the report excludes expired and revoked certificates is R-001's statement; the CSV has no column that shows it.
- It counts presence, not correctness or relying-party enforcement. A constraint can be present and still be useless.
