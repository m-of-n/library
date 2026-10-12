---
schema: "library-summary/v1"
id: iso-iec-29147-2018
record: iso-iec-29147-2018
type: summary
updated: "2026-10-02"
---

# ISO/IEC 29147:2018 — Information technology — Security techniques — Vulnerability disclosure

|  |  |
|---|---|
| **Type** | spec (International Standard) |
| **Maturity** | standard — published 2018-10, Edition 2; confirmed 2024; marked "to be revised" (90.92) 2025-09-26 |
| **Authors** | ISO/IEC JTC 1/SC 27 |
| **Published** | 2018-10 |
| **Identifier** | ISO/IEC 29147:2018 (replaces ISO/IEC 29147:2014) |
| **Source** | https://www.iso.org/standard/72311.html (catalogue; paywalled) — read via the free preview https://cdn.standards.iteh.ai/samples/72311/06fe3b1905aa4f3f8d9c5824ebc3c396/ISO-IEC-29147-2018.pdf |
| **Digest** | `e433e9e17bf3aafd52542d58c0ddbe51e115455030aff72fd148e22c7d42a8c1` (13-page preview PDF, not the standard) |

## Overview

The international standard for **coordinated vulnerability disclosure**: how a vendor receives
reports of potential vulnerabilities from outside (reporters, coordinators) and publishes
advisories and remediations to users. It defines the role vocabulary used everywhere since —
vulnerability, disclosure, coordination, vendor, reporter, coordinator, remediation, advisory — and
it is one half of a pair: it "shall be used in conjunction with" ISO/IEC 30111 (§5.3.1), which owns
the vendor-internal triage, verification and remediation. Its own Scope makes it opt-in ("vendors who
choose to practice vulnerability disclosure"); regulation such as the EU CRA (Annex I Part II) is what
turns a disclosure policy into an obligation, and CRA-related standardisation builds on this pair.

## Version and access verified (2026-10-02)

- **Current edition:** 2018 (Edition 2). Per the iso.org catalogue page (https://www.iso.org/standard/72311.html,
  read through search-engine snapshots because iso.org returned HTTP 403 / a Cloudflare challenge to both
  curl and WebFetch): confirmed at stage 90.93 on 2024-05-03, then stage **90.92 "to be revised"** on
  2025-09-26. **Edition 3 is an Approved Work Item:** ISO/IEC AWI 29147 "Cybersecurity — Vulnerability
  disclosure processes", https://www.iso.org/standard/92945.html, stage 20.00, registered 2025-10-08.
- **Not free.** The ISO/ITTF Publicly Available Standards site
  (https://standards.iso.org/ittf/PubliclyAvailableStandards/index.html) is closed ("now available at no
  charge on the ISO and IEC webstores"). Wayback CDX shows only the **2014** edition
  (`c045170_ISO_IEC_29147_2014.zip`) was ever on that list; there is no entry for the 2018 edition
  (`c072311`). ISO OBP is a JavaScript app behind the same Cloudflare block.
- **What we read:** the free sample distributed by iTeh Standards (the sales platform of SIST, the Slovenian national standards body; not the ISO OBP preview) (13 PDF pages:
  Contents, Foreword, Introduction, Clauses 1–5.3.2 with Figure 1), captured to `.cache/iso-iec-29147-2018.md`
  and corrected against rendered page images. The ANSI webstore preview URL returned 403.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | the reference vocabulary and process for vulnerability disclosure; cited by NIST SSDF RV.1, IEC 62443-4-1 DM, ISO/SAE 21434 bibliography [14], EU CRA practice |
| Cryptography | none | only mentions OpenPGP / S/MIME / TLS for secure communications |
| This project | adjacent | the response phase of an SDL (R-041), the verified/unverified acceptance gate (ARCH-0001 §4, R-042), mitigation-as-remediation (R-040, DEC-009), advisories as governed views (R-043), crosswalk rows 17–18 of MAP-0001 (R-044), Party roles (R-036) |

## Implementations

Searched 2026-10-02 (from knowledge of the ecosystem, not a product survey).

| Name | Kind | License | URL |
|---|---|---|---|
| OASIS CSAF 2.0 / 2.1 (successor of CVRF, cited in §4) | advisory format standard | OASIS IPR (open) | https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html |
| Secvisogram (CSAF editor) | open source tool | see repo | https://github.com/secvisogram/secvisogram |
| csaf_distribution (BSI) | open source CSAF provider/aggregator | see repo | https://github.com/gocsaf/csaf |
| RFC 9116 security.txt | machine-readable disclosure-policy contact | IETF | https://www.rfc-editor.org/rfc/rfc9116 |
| FIRST PSIRT Services Framework | practice framework (cited by 30111 [4]) | FIRST | https://www.first.org/standards/frameworks/psirts/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; `distillation` lists every artifact and its coverage |
| `distilled/README.md` | index of artifacts, coverage and what was not produced |
| `distilled/normative.md` | terms, scope, the 3 visible normative statements, Figure 1 context |
| `distilled/requirements.yaml` | 3 requirements (preview only) with counts and reconciliation |
| `distilled/protocol.yaml`, `protocol.md` | reporter / vendor / coordinator / user protocol from Figure 1 + headings; Mermaid |
| `distilled/messages.yaml` | advisory (16 elements), report, policy (9 elements) — names from headings |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass (20 objects, 19 edges) |
| `distilled/design-notes.md` | bearing on ARCH-0001 / R-036 / R-040–R-044 / DEC-009 |

## Limits

- **Coverage is the free preview only.** Clauses 6 (receiving reports), 7 (advisories), 8
  (coordination), 9 (policy) and Annexes A–D — where nearly every provision on vendors lives — were
  not read. The requirement set has 3 entries; the standard's Annex D summarises far more. The status
  is `summarized`, not `distilled`, on purpose.
- Advisory and policy "fields" are clause headings; their obligation level is known only at the
  §9.2/§9.3/§9.4 tier (required / recommended / optional).
- No timings: 29147 itself may or may not set acknowledgement or embargo deadlines — not visible. Do
  not confuse with the CRA's 24 h / 72 h / 14-day reporting clocks to CSIRTs/ENISA.
- Revision in progress (AWI, stage 20.00): clause numbers may change in Edition 3.
- Scope says "communications (Annex B)" while Annex B is titled "Information to request in a report"
  and example advisories are Annex C — a minor source inconsistency, noted not corrected.
