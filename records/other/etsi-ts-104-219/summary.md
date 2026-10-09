---
schema: "library-summary/v1"
id: etsi-ts-104-219
record: etsi-ts-104-219
type: summary
updated: "2026-10-02"
---

# ETSI TS 104 219 V1.1.1 — CYBER; Software Security Development and Implementation Framework (SSDIF)

|  |  |
|---|---|
| **Type** | spec (ETSI Technical Specification) |
| **Maturity** | standard (published ETSI TS, V1.1.1, History: "March 2026 Publication"; a TS, not an EN or harmonised standard) |
| **Authors** | ETSI Technical Committee Cyber Security (TC CYBER); content drafted with SAFECode and CIS (see Relations) |
| **Published** | 2026-03 (PDF created 2026-03-06, modified 2026-03-19) |
| **Identifier** | ETSI TS 104 219 V1.1.1 (2026-03); work item DTS/CYBER-00190 |
| **Source** | https://www.etsi.org/deliver/etsi_ts/104200_104299/104219/01.01.01_60/ts_104219v010101p.pdf |
| **Digest** | `17aee144482cfe85691b6d9e66c312fad3183391442a68ea741946795f607c15` (78 pages) |

**Version check (2026-10-02):** the ETSI deliver directory for 104219 carries only `01.01.01_60`; the document's History lists only V1.1.1; a web search on 2026-10-02 found no later version. A direct `curl` of the PDF URL from this host returned an HTML bot-challenge page, so the hashed bytes are the copy fetched earlier in this session to the lane scratchpad (`sdlscan/ts104219.pdf`, a valid 78-page PDF titled "TS 104 219 - V1.1.1"). SAFECode's blog "A New International Standard for Software Security" states ETSI adopted it in January 2026.

## Overview

SSDIF regroups the 42 NIST SSDF 1.1 tasks into six engineer-oriented **Essentials** (Secure Software Design, Secure Development, Secure Default Configuration, Supply Chain Security, Code Integrity, Vulnerability Disclosure and Remediation). For each task it writes numbered, testable "DG Specific Actions" in ETSI shall/should form (183 in total: 111 *shall*, 72 *should*), scopes each to one of three **Development Groups** (tiers chosen by how much custom software an organisation builds), names the **DG Artifacts** that evidence the task, and assigns **Responsible Roles** from 14 role types, with cross-references to the CIS Critical Security Controls (ETSI TS 103 305-1, the only normative reference) and SAFECode practices. Its argument is that secure by design can be *evaluated* without a separate compliance paper trail: the evidence is the development by-products (workflow items, tool configurations and outputs, threat models, design documents, signed code) bound to code versions and reproducible by an assessor (§5.0.4). "Secure-by-design means that the software development organization has sufficiently addressed the six SSDIF Essentials." Informative Annexes map CRA Annex I and the UK NCSC CRT APC claims to SSDIF actions, and every SSDF task to 29 other frameworks.

## Why it matters for an SDL

It is the only SDL source in the library that combines (1) SSDF-native ids, (2) normative testable actions, (3) a tiered applicability model (DG), (4) a per-task evidence list, (5) a per-task RACI-like role list and (6) a published SSDF-pivot crosswalk to BSIMM, SAMM, IEC 62443-4-1, MS SDL, PCI Secure SLC, ISO/IEC 27034-1/29147/30111, the CRA and UK CRT. That makes it the most direct input to MAP-0001 and the R-042 conformance check.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | normative SDL framework with testable actions, evidence and roles |
| Cryptography | adjacent | code signing (PS.2.1), integrity hashes, MFA only as actions/examples |
| This project | core | R-041 gate (bug bar), R-042 evidence/conformance, R-044 crosswalk (Annex B.2), R-043 artifact-as-by-product, R-040 mitigation kinds, DEC-009 vulnerability lifecycle |

## Relations

- Builds on `sp-800-218` (SSDF 1.1; task statements and examples copied verbatim).
- Same content line as the CIS/SAFECode "Secure by Design" guide (`cis-safecode-sbd-assessment-1-1`): per SAFECode, the guide "underlies a new ETSI standard" and v1.1 is "consistent in content with the new ETSI standard".
- Maps to `eu-cra-2024-2847` (Annex A), UK NCSC CRT APC (implementing `uk-software-security-code-of-practice`) (Annex B.1), and 29 frameworks (B.2).
- Peers: `bsi-tr-03185`, `bsi-tr-03183-1`, `enisa-sbd-playbook-2026`, `cisa-secure-by-design-2023`.

## Implementations

Searched 2026-10-02: no tool implements SSDIF as such; the CIS/SAFECode Secure by Design spreadsheet (registration-walled) is the companion machine-readable form.

| Name | Kind | License | URL |
|---|---|---|---|
| CIS/SAFECode Secure by Design v1.1 guide + spreadsheet | assessment workbook | registration | https://www.cisecurity.org/insights/white-papers/secure-by-design-v1-1-a-guide-to-assessing-software-security-practices |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, cites, distillation block |
| `distilled/README.md` | index of distilled artifacts with coverage |
| `distilled/normative.md` | every task table verbatim (statement, CSC, SAFECode, DG actions, DG artifacts, roles, examples), Tables 5.0-1..5.0-3, 5.1-x, Annexes A, B.1, B.2 |
| `distilled/requirements.yaml` | 220 entries (183 DG actions, 3 inheritance entries, 34 prose recommendations) + 42 `tasks` with 768 `maps_to` |
| `distilled/crosswalk.yaml` | inverse index framework → provision → SSDIF tasks; CRA and CRT tables |
| `distilled/messages.yaml`, `distilled/schema/` | 15 work-product structures the TS prescribes; derived JSON Schemas |
| `distilled/protocol.yaml`, `protocol.md` | 4 flows (vulnerability response, threat model → fix, release gate, TPC acceptance) with Mermaid |
| `distilled/state-machine.yaml` | 4 lifecycles (vulnerability, security bug vs bug bar, third-party component, SDL process document) |
| `distilled/object-model.yaml`, `object-model.md` | object-model pass: 60 objects, 36 edges, 7 gaps |
| `distilled/design-notes.md` | adopt/adapt/reject vs R-040..R-044, DEC-009; source defects |

## Limits

- No assessment scheme: no scoring or pass/fail rule beyond "sufficiently addressed"; evidence is described, not sampled.
- Annex mappings are informative and coarse (CRA I.I(2)(a) → "All"; (m) data removal not covered; B.1 claim 5.1.5 unmapped).
- DG1 coverage is thin for design (PW.1.1 threat modelling has *no* DG1/2 action), so a DG1/2 organisation is not required to threat-model at all.
- Source defects: wrong reference numbers in §5.6.0; [i.13] names "EO 14036" (EO 14306 is meant); DG/IG terminology mixed in §5.5; typos (PW.4.2 #8 "should should"); Annex C artifact cells differ from clause 5. Details in design-notes.md.
