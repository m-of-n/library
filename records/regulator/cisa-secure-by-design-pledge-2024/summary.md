---
schema: "library-summary/v1"
id: cisa-secure-by-design-pledge-2024
record: cisa-secure-by-design-pledge-2024
type: summary
updated: "2026-10-02"
---

# Secure by Design Pledge (CISA, May 2024)

|  |  |
|---|---|
| **Type** | spec (voluntary pledge) |
| **Maturity** | best-practice (voluntary, "not legally binding") |
| **Authors** | CISA |
| **Published** | May 2024 (PDF created 2024-05-06) |
| **Identifier** | https://www.cisa.gov/securebydesign/pledge |
| **Source** | https://www.cisa.gov/sites/default/files/2024-05/CISA%20Secure%20by%20Design%20Pledge_508c.pdf (bytes from the Internet Archive id_ copy; cisa.gov returns 403 to scripts) |
| **Digest** | `3e9cd7058314fe1407b6665fcd9a51f90c08a8fa08e4578e817cd99af5b79bcb` (7 pp, retrieved 2026-10-02) |

**Currency (checked 2026-10-02).** CISA resource page lists the May 2024 PDF (English; Spanish
version Aug 2024) and no revision. The live pledge page (snapshot 2026-09-20) matches the PDF
except: Goal 6's goal line is shortened (criteria moved to Context), an extra Overview paragraph,
and a disclaimer "CISA does not enforce nor verify adherence to the pledge". The progress-reports
page (https://www.cisa.gov/securebydesign/pledge/progress-reports, fetched 2026-10-02) lists
roughly 60+ companies' reports, latest seen July 2025; the signers page claims "hundreds of
companies".

## Overview

Enterprise software manufacturers pledge a good-faith effort, over one year, on **seven goals**:
(1) measurably increase MFA use; (2) reduce default passwords; (3) measurably reduce one or more
vulnerability classes; (4) increase customers' installation of security patches; (5) publish a
VDP that authorizes public testing, promises no legal action against good-faith research,
provides a reporting channel and allows coordinated public disclosure; (6) put accurate CWE and
CPE in every CVE record and issue CVEs timely for critical/high vulnerabilities needing customer
action or actively exploited; (7) increase customers' ability to gather evidence of intrusions
(logs). Each goal has context, example approaches and examples of evidence. Within a year the
signer should publicly document progress (or how it already meets a goal); if no progress, it is
encouraged to tell CISA and the public why. Method is at the signer's discretion.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | operationalises the SbD principles as measurable goals |
| Cryptography | none | — |
| This project | adjacent | time-boxed outcome goals as SDL Requirements + Milestones (R-041/R-042); Goals 5/6 automatable over Vulnerability/Weakness nodes; mitigation kinds (R-040); commitment-vs-attestation modality; DEC-009 for patch/EOL lifecycle |

## Implementations

Searched 2026-10-02: signer progress reports (AWS, Microsoft, Google, Cloudflare, Fortinet,
Sophos, …) on CISA's progress-reports page; no tooling. Related public tools: security.txt
(RFC 9116) for Goal 5's machine-readable VDP.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; see_also SbD whitepaper, Secure by Demand, attestation form |
| `distilled/README.md` | index |
| `distilled/normative.md` | 72 statements verbatim, PDF/web differences |
| `distilled/requirements.yaml` | 72 typed entries (`#G1`, `#G1-A1`, `#G1-M1`, `#PRE-4` …) |
| `distilled/messages.yaml`, `protocol.*`, `state-machine.yaml` | sign-up, reporting, lifecycle |
| `distilled/object-model.*` | object-model pass |
| `distilled/design-notes.md` | bearing on tmodel |

Local only: `.cache/cisa-secure-by-design-pledge-2024.{pdf,txt,html,html.txt}`.

## Limits

Voluntary and unverified ("CISA does not enforce nor verify adherence"); no thresholds for
"measurable"; enterprise software only (IoT/consumer out of scope); goals are outcomes, not SDL
practices, so it says little about *how* software is developed. Political status after 2025 not
stated by CISA (no update to the pledge found).
