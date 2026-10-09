---
schema: "library-summary/v1"
id: eu-cra-2024-2847
record: eu-cra-2024-2847
type: summary
updated: "2026-10-02"
---

# Regulation (EU) 2024/2847 — Cyber Resilience Act (CRA)

|  |  |
|---|---|
| **Type** | spec (EU regulation, directly applicable) |
| **Maturity** | standard — adopted legislation, in force since 10 December 2024 (Art 71(1)) |
| **Authors** | European Parliament and Council of the European Union |
| **Published** | OJ L, 2024/2847, 20.11.2024 (signed 23 October 2024) |
| **Identifier** | CELEX 32024R2847 · ELI http://data.europa.eu/eli/reg/2024/2847/oj |
| **Source** | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024R2847 (PDF, 81 pp.); extraction from the EUR-Lex English HTML |
| **Digest** | PDF `e3ecaabddf6e321fa04097d15dfcccc7309d0fe5896240ab7625a27d74ab1b0a`; HTML `628cb514474e218a7c3d3dd55cda45f8c0e17fc92afadbf982d83bed574a5589` (retrieved 2026-10-02) |

## Overview

The CRA makes a secure development lifecycle a condition of selling any "product with digital elements" in the EU.
A manufacturer has to carry out and document a cybersecurity risk assessment (in effect, a threat model) across the
product's whole life (Art 13(2)-(3)). The product has to be placed on the market "without known exploitable
vulnerabilities" and meet the Annex I Part I properties. For a support period of normally at least five years the
manufacturer has to run Annex I Part II vulnerability handling: an SBOM, coordinated vulnerability disclosure (CVD),
regular testing, and free security updates.

Since **11 September 2026** manufacturers have also had to report actively exploited vulnerabilities and severe
incidents through ENISA's single reporting platform on a fixed clock (Art 14):
- an early warning within 24 h;
- a notification within 72 h;
- a final report within 14 days of a corrective measure for a vulnerability, or within one month for a severe incident.

The evidence is a governed, versioned technical-documentation set (Annex VII) that must be kept for 10 years. The
manufacturer's EU declaration of conformity covers both the product and its processes.

## Version and currency (checked 2026-10-02)

- **Text.** OJ L 2024/2847 of 20.11.2024 is the current text. It is corrected by three English corrigenda:
  - OJ L 2024/90780 (5.12.2024, title);
  - OJ L 2025/90555 (2.7.2025, Art 64(10): "paragraphs 2 to 9"; applied in our extraction);
  - OJ L 2025/90828 (17.10.2025, Art 67).

  EUR-Lex lists only one consolidated version, 02024R2847-20241120.
- **Pending amendment.** Regulation (EU) 2025/327 (EHDS) Art 104 amends Art 13(4) and Art 31(3) and inserts Art 32(5a),
  applying from 26 March 2027. Source: https://eur-lex.europa.eu/eli/reg/2024/2847/oj (document information and
  corrigenda tabs).
- **Application dates (Art 71(2)).**

  | Date | What applies |
  |---|---|
  | 10 Dec 2024 | Entry into force |
  | 11 Jun 2026 | Chapter IV, notification of conformity assessment bodies (Arts 35-51) |
  | **11 Sep 2026** | Art 14 reporting obligations; Art 69(3) extends them to products already on the market |
  | **11 Dec 2027** | Everything else |

- **Secondary acts we found.**
  - Commission Delegated Regulation (EU) 2026/881 of 11 December 2025 (OJ L 20.4.2026). It sets the grounds on which a
    CSIRT may delay disseminating a notification (Art 14(9)) and is summarised in `normative.md`.
  - Commission Implementing Regulation (EU) 2025/2392, giving the technical descriptions of Annex III/IV important and
    critical product categories (Art 7(4)), noted from the EUR-Lex list of acts based on 32024R2847.
  - Commission Delegated Regulation (EU) 2025/1535 of 29 July 2025, excluding from the CRA certain products with
    digital elements that fall within Regulation (EU) No 168/2013 (two- and three-wheel vehicles) (title verified via
    the Publications Office SPARQL endpoint in the verify pass).
  - **Proposal COM(2026) 590** (CELEX 52026PC0590, 9 September 2026), the "Public Procurement Act", which among many
    acts *proposes to amend* Regulation (EU) 2024/2847. Found in the verify pass (Publications Office SPARQL,
    `resource_legal_proposes_to_amend_resource_legal`); not adopted; content of the CRA amendment not read.
  - Corrigenda R(03) (FR/HU, 3.10.2025), R(05) (SK, 23.2.2026), R(06) (FR, 25.3.2026) and R(07) (DE, 6.8.2026) exist
    only in other language versions; none touches the English text (languages verified in the verify pass).
  - **No** implementing act fixing the SBOM format (Art 13(24)) or the notification format (Art 14(10)) has been adopted.
- **Commission guidance C(2026) 5252** (27 July 2026). A non-binding Communication with an 84-page annex and 67 worked
  examples. It covers scope (remote data processing, free and open-source software), substantial modification, support
  periods, the reporting obligations and the interplay with other EU law.
  https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
  It is not extracted here. It is a candidate for its own record, and its examples could serve as fixtures.

## Harmonised standards status (checked 2026-10-02)

- **Standardisation request.** M/606 was adopted by Commission Implementing Decision C(2025) 618 of 3 February 2025 and
  accepted by CEN, CENELEC and ETSI on 3 April 2025. It asks for 41 standards: horizontal Type A and B standards from
  CEN/CENELEC JTC 13, and product-specific Type C standards mostly from ETSI and JTC 13.
  - Source: https://ec.europa.eu/transparency/documents-register/api/files/C(2025)618_0/de00000001069725
  - Source: https://www.cencenelec.eu/news-events/news/2025/newsletter/ots-62-cra/
- **Proposed deadline change.** A draft amendment (July 2026) would move the deadlines from 30 Aug 2026 to 31 Oct 2026
  for Types A and B, and from 30 Oct 2026 to 31 Dec 2026 for Type C. It had not been published in the OJ as of 8 Sep
  2026 (secondary source: cyberresilienceact.eu).
- **FprEN 40000-1-2**, *Principles, product risk management, and lifecycle activities* (JT013089). Status "Under
  Approval", Date of Ratification **2026-11-02**. The CEN record says "No citation expected" under 2024/2847, so it is a
  framework standard and does not itself confer presumption of conformity.
  - Source: the CEN/CLC JTC 13 project page, standards.cencenelec.eu, FSP_ORG_ID 2307986.
- **prEN 40000-1-3**, *Vulnerability handling*. Status "Under Approval", no ratification date published yet. The CEN
  record says "Citation expected" under 2024/2847. Once cited, this will be the presumption-of-conformity standard for
  Annex I Part II.
- **EN 40000-1-1** (vocabulary). Approved in formal vote, ratification also scheduled for 2026-11-02, per a secondary
  tracker (craevidence.com, dated 2026-10-02).
- **EN 40000-1-4** (generic security requirements, Annex I Part I). In development, deadline 30 Oct 2027, per the same
  tracker.
- **ETSI EN 304 6xx** (17 Type C product drafts: firewalls, IDS/IPS, VPN, routers and others). Public enquiry launched
  13 Aug 2026; the approval procedures end between mid-September and mid-November 2026.
- **OJ citations.** **No CRA harmonised standard is cited in the Official Journal.** The Art 27(1) presumption of
  conformity from standards is therefore not yet available. EN 18031-x (RED delegated act) and ETSI EN 303 645 do not
  confer CRA presumption.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The binding EU baseline for product security engineering and vulnerability handling. |
| Cryptography | adjacent | It requires "state of the art mechanisms" for confidentiality and integrity (Annex I Part I(2)(e)-(f)) and secure distribution of updates, but names no algorithms. |
| This project | core | It bears on **R-040** (all three mitigation kinds appear), **R-041** (placing on the market is a release gate; the support period is a dated window), **R-042** (the Annex I applicability-and-justification table and the Art 14 clocks are mechanically checkable), **R-043** (Annex VII documentation and the DoC are governed, retained views), **R-044** (Annex I is the legal anchor row set for the crosswalk) and **DEC-009** (the Annex I Part II handling lifecycle). |

Topic: the record keeps its existing topic `supply-chain-attestation`; it also belongs to the `sdl` lane (tag `sdl`).

## Implementations

The Regulation is law, not software. Things that implement parts of it:

| Name | Kind | License | URL |
|---|---|---|---|
| ENISA CRA Single Reporting Platform | Operational service (Art 16) | public authority | https://portal.cra-srp.enisa.europa.eu |
| OASIS CSAF 2.x | Advisory format usable for Annex I Part II(4) and Art 14(8) | OASIS open standard | https://docs.oasis-open.org/csaf/ |
| SPDX / CycloneDX | SBOM formats for Annex I Part II(1) | open | records `spdx-3-0-1`, `cyclonedx-1-7` |
| ORC WG CRA FAQ (Eclipse Foundation) | Community interpretation | CC-BY | https://cra.orcwg.org/ |

Commercial CRA compliance tooling exists in quantity; none was evaluated (searched 2026-10-02).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, FX-1 distillation block |
| `distilled/README.md` | artifact index with coverage |
| `distilled/normative.md` | verbatim in-scope text (Arts 3, 13-17, 24, 31, 64, 69, 71; Annexes I, II, VII) plus a title-only ToC of the rest |
| `distilled/requirements.yaml` | 191 atomic provisions, library-requirements/v2, with reconciled counts |
| `distilled/protocol.yaml`, `protocol.md` | reporting and CVD protocol: roles, timers, flows, error paths, Mermaid |
| `distilled/state-machine.yaml` | reporting clocks (AEV, severe incident), vulnerability handling, support lifecycle |
| `distilled/messages.yaml` | notification contents and documentation structures |
| `distilled/schema/` | derived JSON Schema for Art 14 notifications |
| `distilled/design-notes.md` | adopt / adapt / reject against tmodel, open questions |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass (51 objects, 37 edges; 3 edges added in verify) |

## Limits

- Conformity assessment procedures, notified bodies, market surveillance, penalties beyond Art 64(2)-(4) and (10),
  and all recitals are **not** extracted. Recitals carry the "should" interpretation (283 occurrences) and are
  non-binding.
- The Regulation is outcome-based. It names no SDL practices, methods or tools. The operational detail will come from
  EN 40000-1-2/-1-3/-1-4 and the ETSI verticals, which are not yet citable.
- There are textual defects: the Art 16(2) cross-reference, and Art 16 applying later than the Art 14 obligations that
  depend on it. See design-notes open questions 1-2. "Known exploitable" has no knowledge-state cut-off.
- Verify and cross-check passes done 2026-10-02 by an independent verifier; defects and residual issues in `distilled/verification.md`.
