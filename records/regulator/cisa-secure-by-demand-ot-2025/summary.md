---
schema: "library-summary/v1"
id: cisa-secure-by-demand-ot-2025
record: cisa-secure-by-demand-ot-2025
type: summary
updated: "2026-11-16"
---

# Secure by Demand: Priority Considerations for OT Owners and Operators when Selecting Digital Products

|  |  |
|---|---|
| **Type** | spec (joint guidance, TLP:CLEAR) |
| **Maturity** | best-practice (voluntary guidance) |
| **Authors** | CISA with NSA, FBI, EPA, TSA, ASD's ACSC, CCCS, EC DG CONNECT, BSI, NCSC-NL, NCSC-NZ, NCSC-UK |
| **Published** | 2025-01-13 |
| **Identifier** | https://www.cisa.gov/resources-tools/resources/secure-demand-priority-considerations-operational-technology-owners-and-operators-when-selecting |
| **Source** | https://www.cisa.gov/sites/default/files/2025-01/joint-guide-secure-by-demand-priority-considerations-for-ot-owners-and-operators-508c_0.pdf (Internet Archive id_ copy; cisa.gov 403s scripts) |
| **Digest** | `172daac421ad9d3c535cba962f9aa4a3b894065c4c2522bcdbb0f064c6696d16` (22 pp, retrieved 2026-10-02) |

**FX-1 extraction (library#69, family 4), claiming `profile: full`.** The source of record is
the PDF; every artifact reads it through the pinned `pdftotext -layout` rendering named in
`distilled/requirements.yaml` (`source_text`, `source_text_digest`) and cites it by line. The
passes run so far are in `record.yaml` `distillation.passes`; no artifact is reviewed by a person
yet. **Currency:** CISA's page lists this January 2025 guide and a shorter 2025-04 PDF
(`identifiers.pdf_2025_04`, not fetched). This is the only 2025 "Secure by Demand" priorities
document found; it is OT-specific.

## Overview

Threat actors target *OT products* (not organizations) because weaknesses — weak authentication,
known vulnerabilities, limited logging, insecure defaults, legacy protocols — replicate across
victims. OT owners/operators ("buyers") should select products from manufacturers that
prioritize **12 security elements** (not in priority order): configuration management, logging
in the baseline product, open standards, ownership, protection of data, secure by default,
secure communications, secure controls, strong authentication, **threat modeling**,
vulnerability management, and upgrade and patch tooling. Each consideration has selection
criteria, questions to ask the manufacturer, a paragraph on why it matters, a goal and guidance
for the OT context; a Summary list restates all twelve. It aligns with ISA/IEC 62443 (4-2 SL3,
3-3), NIST SP 800-82/800-213A and the EU CRA, and points to NIS2/RED/CE marking.

Most relevant to tmodel: element 10 asks for "a full and detailed threat model" that is kept
up to date, tracks public threat sources such as MITRE EMB3D, states the assumed external
controls, communication paths and intended environment, and has a roadmap for gaps; buyers
should partner with the manufacturer's threat-modeling capability. Element 11 asks for a software
bill of materials (the Summary asks for a hardware one too), CVE-based handling per ISO/IEC
29147/30111, CSAF advisories, VEX following CSAF, a CVD policy and an RFC 9116 security.txt.

The guide binds no one: its disclaimer says it does not bind CISA and its co-sealers, and a
footnote says it does not bind the European Commission. Its should is a recommendation and its
three musts are the authors' strongest wording. It sets no acceptance threshold and ranks none of
the twelve, so whether a product is acceptable is the buyer's decision.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | buyer-side OT product security criteria |
| Cryptography | adjacent | certificates that fail loudly; disabling SSL/TLS 1.0/1.1, SNMPv1/2, Telnet |
| This project | adjacent | demand-side case for an exportable, governed product threat model (`tmodel:R-043`); per-requirement conformance over a manufacturer's evidence, the threats-mitigated check run by a buyer (`tmodel:R-042`); criteria and questions as a requirement source with only document-level alignment to 62443 and the CRA (`tmodel:R-044`); VEX and CSAF as interchange formats (`tmodel:ARCH-0001` §5) |

## Implementations

Searched 2026-10-02: none specific. Related tooling: CSAF (OASIS) producers/validators,
security.txt generators, MITRE EMB3D.

## Artifacts in this record

Per-artifact coverage is in `record.yaml` `distillation.artifacts`.

| File | What it is |
|---|---|
| `record.yaml` | metadata, cites (62443, NIST, EMB3D, CSAF, 29147/30111, NIS2, CRA), distillation block |
| `distilled/README.md` | index |
| `distilled/requirements.yaml` | every sentence with a verbal form outside the front matter and the Introduction, split per form; every selection-criteria sentence, question to ask and threat-model question, goal, and Summary element and seek-out sentence (`role`, `question_set`, `favourable_answer`); keyword-less binding statements; inferred entries flagged `kind: inferred` |
| `distilled/inferred-candidates.yaml` | the skeleton's keyword-less candidates and the verbal forms of the front matter and Introduction, each with a verdict |
| `distilled/normative.md` | the text by section, quoted by line marker, with the source defects (SD-1 to SD-19) |
| `distilled/messages.yaml`, `distilled/schema/` | four structures the guide prescribes in prose and two derived so its questions and criteria can be tested; derived JSON Schemas, their generator and checker |
| `distilled/protocol.yaml`, `distilled/protocol.md` | the procurement exchange and the operational exchanges the elements describe, with Mermaid diagrams; no wire protocol exists |
| `distilled/state-machine.yaml` | the lifecycles the guide states or implies |
| `distilled/examples/` | the finding that the guide has no worked example or test vector; our derived schema cases |
| `distilled/design-notes.md` | adopt / adapt / reject against tmodel and mofn decisions; open questions |
| `distilled/object-model.yaml` + `.md` | the earlier object-model pass (2026-10-02), kept unchanged |

Local only: `.cache/cisa-secure-by-demand-ot-2025.bin` (the PDF) and
`.cache/cisa-secure-by-demand-ot-2025.txt` (the pinned rendering).

## Limits

- Joint guidance, not a standard, and it follows no drafting rules: each verbal form is read
  per sentence (`normativity` in `requirements.yaml`), not by convention.
- No acceptance threshold, weighting or ranking of the twelve; the questions carry no stated
  answer, so the favourable answer recorded for each is our reading.
- OT-specific; no thresholds beyond named protocol versions. The 62443, NIST and CRA alignment
  is asserted for the document as a whole, without an item-level mapping.
- The Summary and the sections disagree in places (insecure protocols, bills of materials,
  phishing-resistant MFA, when the move to a supported operating system is owed); inferred
  entries reconcile them and `normative.md` lists each defect.
- The shorter 2025-04 PDF was not fetched or compared.
