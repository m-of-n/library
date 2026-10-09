---
schema: "library-summary/v1"
id: uk-software-security-code-of-practice
record: uk-software-security-code-of-practice
type: summary
updated: "2026-10-02"
---

# Software Security Code of Practice (UK, DSIT / NCSC)

|  |  |
|---|---|
| **Type** | spec (voluntary government code of practice) |
| **Maturity** | best-practice (voluntary code; government guidance, not legislation, and no certification scheme yet) |
| **Authors** | Department for Science, Innovation and Technology (DSIT), co-designed with the National Cyber Security Centre (NCSC) |
| **Published** | 2025-05-07. gov.uk page last updated 2026-01-15; the content is unchanged since first publication |
| **Identifier** | gov.uk publication "Software Security Code of Practice" (May 2025) |
| **Source** | https://assets.publishing.service.gov.uk/media/69a8060a2e1f4fbda4252270/Software_Security_Code_of_Practice_Web_Accessible.pdf (9 pp.) |
| **Digest** | `b0861856bfbc3ed469d885e57fd0edc0071f0700e3224c3ce020e8fadbed811f` (PDF, retrieved 2026-10-02) |

## Overview

The Code is a voluntary baseline for any organisation that develops or sells software to
businesses. It has 14 principles under 4 themes: secure design and development, build environment
security, secure deployment and maintenance, and communication with customers. The normative
construction is a single accountability: "The Senior Responsible Owner in vendor organisations
shall gain assurance that their organisation achieves the following…". The Code defines "shall" as
"a requirement of the Code". It deliberately does not define a lifecycle. Principle 1.1 requires the
vendor to follow an established secure development framework (SSDF, MS SDL, SLSA and others, in the
implementation guidance's Appendix 1). The Code's own additions are the customer-facing duties: a
published VDP, a support statement, **at least one year's end-of-support notice**, and incident
notification. Conformance is made testable by the NCSC **Assurance Principles and Claims (APCs)**,
which split each principle into 45 objectively evidenced outcome claims in total, and is shown by
self-assessment or by an NCSC-approved test facility.

## Version check (2026-10-02)

| What | Where checked | Result |
|---|---|---|
| Code | https://www.gov.uk/government/publications/software-security-code-of-practice | First published 7 May 2025. Updates: 28 Nov 2025 (link to evaluation survey), 15 Jan 2026 (Ambassadors Scheme added). No content revision. The PDF asset was re-issued (ModDate 2026-03-04, title "Software Security Code of Practice - May 2025"). The HTML matches the PDF apart from 3 trivial rendering differences (normative.md). |
| Implementation guidance | https://www.ncsc.gov.uk/collection/software-security-code-of-practice-implementation-guidance | Version 1.0, published and reviewed 7 May 2025. 7 web pages. |
| APCs | https://www.ncsc.gov.uk/guidance/software-security-code-of-practice-assurance-principles-claims | Version 1.0, published 7 May 2025. Page `dateModified` 3 July 2026; PDF rendering `/sites/default/files/2026-07/…APCs.pdf` (4 pp.), sha256 `5064391a…09fd`. |
| Ambassadors Scheme | https://www.gov.uk/government/publications/software-security-ambassadors-scheme | Published 15 Jan 2026, last updated 1 Oct 2026 (disclaimer added). An adoption campaign with 15 signatories (DSIT, NCSC, Accenture, Cisco, ISC2, NCC Group and others). It is **not** a certification scheme. |
| Certification | Code p.5 | "currently working to develop a certification scheme … will be shared in due course". None published as of 2026-10-02. |
| Co-sealing | https://www.cyber.gc.ca/en/news-events/joint-guidance-software-security-code-practice | The Canadian Centre for Cyber Security joined the release (page dated 2025-04-30). It is the same document, not a new version. |

Per-page HTML digests of the implementation guidance (retrieved 2026-10-02): about `0e8e9742…`,
theme-1 `13909672…`, theme-2 `7635be6c…`, theme-3 (secure-deployment-maintenance) `d863facf…`,
theme-4 `378e130b…`, appendix-1 `47b4af8b…`, collection index `a669fe4b…`. Local Markdown capture
`13e28f4d…`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A government baseline for vendor SDL plus vulnerability and customer communication, aligned to SSDF and the EU CRA. |
| Cryptography | adjacent | Only "well established standardised cryptography" for sensitive data (IG 1.4) and signed code and updates (IG 3.1, 3.5). |
| This project | core | It gives a three-level Requirement → Claim → Evidence conformance chain (R-042). One claim, APC 1.4 #1, can be evidenced directly by a threat model. All three R-040 mitigation kinds appear, and a source-published framework mapping exists for R-044. |

Bears on **R-040** (mitigation kinds), **R-041** (SDL program, SRO accountability, end-of-support
transition), **R-042** (conformance through the APC claims), **R-043** (published VDP, support
statement and self-assessment as governed views) and **R-044** (Appendix 1 mapping).

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| NCSC Principles Based Assurance self-assessment template | official form (.docx), generic PBA | Crown copyright / OGL | https://www.ncsc.gov.uk/sites/default/files/documents/pba-self-assessment-template.docx |
| NCSC Cyber Resilience Test Facilities | independent assessment services | commercial | https://www.ncsc.gov.uk/schemes/cyber-resilience-test-facilities |
| NCSC Vulnerability Disclosure Toolkit | VDP setup guidance (referenced by IG 3.2) | Crown copyright | https://www.ncsc.gov.uk/information/vulnerability-reporting |

Searched 2026-10-02 for open-source conformance tooling or a machine-readable APC: none found.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, distillation block |
| `distilled/README.md` | index of the distilled artifacts with coverage |
| `distilled/normative.md` | Code, APC and IG normative text, verbatim, per principle |
| `distilled/requirements.yaml` | 166 typed requirements (library-requirements/v2) |
| `distilled/apc-claim-trees.yaml` | the APC appendix claims trees (68 nodes), transcribed from the NCSC SVGs in the verify pass |
| `distilled/verification.md` | verify and cross-check passes: method, counts, defects, residual issues |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass (46 objects, 42 edges) |
| `distilled/protocol.yaml`, `protocol.md` | information-exchange flows (vulnerability, incident, end of support) |
| `distilled/state-machine.yaml` | vulnerability, product-support and incident lifecycles |
| `distilled/design-notes.md` | adopt, adapt and reject against R-040..R-044 |

## Limits

- It is voluntary, and its scope is B2B proprietary software. Open-source maintainers are "not
  the primary audience".
- There is no lifecycle, no gates and no maturity levels. The lifecycle is delegated to an external
  framework (1.1).
- Timeliness is unquantified except end-of-support notice ≥ 1 year. Compare the EU CRA's 24h/72h/14-day
  reporting clock (`eu-cra-2024-2847`).
- The APC claims trees are not in the APC PDF; they are SVG images on the NCSC page, whose node text was
  transcribed in the verify pass (`distilled/apc-claim-trees.yaml`, 68 claims; connectors not parsed). The
  self-assessment form is a generic PBA template. No machine-readable conformance artefact is published.
- No certification scheme exists yet. Assurance is self-assessment or an independent test facility.
