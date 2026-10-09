---
schema: "library-doc/v1"
id: iso-iec-30111-2019-normative
record: iso-iec-30111-2019
type: normative
updated: "2026-10-02"
---

# ISO/IEC 30111:2019 — normative statements (free preview only)

**Coverage.** Every normative statement (shall / should / may) in the **free preview** of
ISO/IEC 30111:2019, verbatim, in source order, with locator. The preview ends at §6.5.3.4 (printed
page 5). **Not covered — not available to us:** §6.5.4 Staff capabilities, §6.6 product business
division, §6.7 customer support and public relations, §6.8 legal consultation, **all of Clause 7**
(the vulnerability handling phases: preparation, receipt, verification, remediation development,
release, post-release; process monitoring; confidentiality), Clause 8 (supply chain
considerations), Annex A (summary of normative provisions — referenced in the Foreword) and the
Bibliography. The standard is paywalled; we did not and will not use an unofficial copy.

Source: distributor-sample (iTeh/SIST) preview PDF (sha256 `5a2f9235…08b8`), captured as
`.cache/iso-iec-30111-2019.md`. Verbal forms per ISO/IEC Directives Part 2: **shall** =
requirement, **should** = recommendation, **may** = permission. Ids refer to
`requirements.yaml`.

## Clause 1 — Scope (informative framing of the requirement scope)

> This document provides requirements and recommendations for how to process and remediate
> reported potential vulnerabilities in a product or service.
>
> This document is applicable to vendors involved in handling vulnerabilities.

## Clause 2 — Normative references

ISO/IEC 27000 (vocabulary) and **ISO/IEC 29147:2018** (dated — only the 2018 edition applies).

## Clause 3 — Terms

> For the purposes of this document, terms and definitions given in ISO/IEC 27000 and ISO/IEC 29147 apply.

(30111 defines no terms of its own; see `iso-iec-29147-2018` normative.md for vulnerability,
disclosure, coordination, vendor, reporter, coordinator, remediation, advisory.)

## Clause 5 — Relationships to other International Standards

| id | locator | form | text |
|---|---|---|---|
| 5.1-R01 | §5.1 | shall | ISO/IEC 29147 shall be used in conjunction with this document. |

Figure 1 (relationship between ISO/IEC 29147 and ISO/IEC 30111) is transcribed in
`object-model.md` and drives `state-machine.yaml`. §5.2–§5.4 (27034, 27036-3, 15408-3) are
informative pointers with no normative verb.

## Clause 6 — Policy and organizational framework

### 6.1 General

| id | form | text |
|---|---|---|
| 6.1-R01 | should | Vendors should create a vulnerability handling process in accordance with this document in order to prepare for investigating and remediating potential vulnerabilities. |
| 6.1-R02 | should | The creation of a vulnerability handling process is a task that is performed by a vendor and should be periodically assessed to ensure that the process performs as expected and to support process improvements. |
| 6.1-R03 | should | Vendors should document their vulnerability handling processes in order to ensure that they are repeatable. |
| 6.1-R04 | should | The documentation should describe the procedures and methods used to track all reported vulnerabilities. |

Not extracted (descriptive): "Clause 6 describes the organizational elements that vendors should consider in their vulnerability handling processes."

### 6.2 Leadership

**6.2.1-R01 (should)** — Top management should demonstrate leadership and commitment with respect to vulnerability handling by:

a) ensuring the policy and the objectives of vulnerability handling are established and are compatible with the strategic direction of the organization;
b) ensuring the integration of the vulnerability handling into the organization’s processes;
c) ensuring that the resources needed for the vulnerability handling are available;
d) communicating the importance of effective vulnerability handling;
e) ensuring that the vulnerability handling process achieves its intended outcome(s);
f) directing and supporting persons to contribute to the effectiveness of the vulnerability handling process;
g) promoting continual improvement; and
h) supporting other relevant management roles to demonstrate their leadership as it applies to their areas of responsibility.

**6.2.2-R01 (should)** — Top management should establish vulnerability handling policy that:

a) is appropriate to the purpose of the organization;
b) includes a best-effort commitment to satisfy user’s requirements related to its product or online service security; and
c) includes a commitment to continual improvement of the vulnerability handling process.

**6.2.3-R01 (should)** — Top management should ensure that the responsibilities and authorities for roles relevant to vulnerability handling are assigned and communicated.

**6.2.3-R02 (should)** — Top management should assign the responsibility and authority for:

a) ensuring that the vulnerability handling process conforms to the requirements of this document; and
b) reporting on the performance of the vulnerability handling to top management.

### 6.3 Vulnerability handling policy development

**6.3-R01 (shall)** — A vendor shall develop and maintain an internal vulnerability handling policy to define and clarify its intentions for investigating and remediating vulnerabilities as part of a vulnerability handling process.

**6.3-R02 (should)** — This policy should be compatible with the external vulnerability disclosure policy required by ISO/IEC 29147.

**6.3-R03 (should)** — It should include the following items:

a) basic guidance, principles, and responsibilities for handling potential vulnerabilities in products or services;
b) a list of departments and roles responsible for handling potential vulnerabilities;
c) safeguards to prevent premature disclosure of information about potential vulnerabilities before they are fixed; and
d) a target schedule for remediation development.

Context (descriptive, not extracted): the internal policy "is intended for the vendor’s staff and
defines who is responsible in each stage of the vulnerability handling process and how they should
handle reports about potential vulnerabilities"; the external disclosure policy's audience is
internal and external stakeholders (see ISO/IEC 29147:2018, Clause 9 and Annex A).

### 6.4 Organizational framework development

| id | form | text |
|---|---|---|
| 6.4-R01 | should | An organizational framework should be designed, recognized, and supported by the stakeholder divisions of the vendor responsible for each area. |
| 6.4-R02 | should | An organization should have a role or capability that is responsible for and has authority to make decisions on vulnerability handling, preferably at a management level. |
| 6.4-R03 | should | This role or capability should understand the responsibility toward the vendor’s users, the internal processes, and the organizational framework for vulnerability handling. |
| 6.4-R04 | should | An organization should have a role or capability that is a point of contact for handling potential vulnerabilities. |
| 6.4-R05 | should | This point of contact should be identified for each division or department within a vendor that provides products or services to customers. |
| 6.4-R06 | should | An organization should establish a point of contact for external parties to reach and communicate with about vulnerabilities. |
| 6.4-R07 | should | Since customers and members of the media can contact the vendor with questions or requests for additional information after a vulnerability is disclosed, divisions responsible for customer and public relations should be prepared so that they can respond. |

### 6.5 Vendor CSIRT or PSIRT

| id | locator | form | text |
|---|---|---|---|
| 6.5.1-I01 | §6.5.1 | *(inferred — "is responsible for")* | A PSIRT is responsible for coordinating external vulnerability reports. |
| 6.5.2-R01 | §6.5.2 | should | Vendors should include all of their products and services in their vulnerability disclosure and vulnerability handling processes. |
| 6.5.2-R02 | §6.5.2 | should | A PSIRT should be implemented centrally within a vendor. |
| 6.5.2-P01 | §6.5.2 | may | However, a PSIRT may be implemented within a business unit, as long as all products and services are covered by the vendor’s vulnerability handling processes. |
| 6.5.3.2-R01 | §6.5.3.2 | should | A PSIRT should monitor known public sources of vulnerability information for disclosures or discussion that affect the vendor’s products or services. |
| 6.5.3.3-R01 | §6.5.3.3 | should | A PSIRT should develop a single entry-point for receiving potential vulnerability reports from reporters or coordinators, typically either an e-mail address or a form on a web page. |
| 6.5.3.3-I01 | §6.5.3.3 | *(inferred — "is responsible for")* | A PSIRT is responsible for maintaining communication with reporters. |
| 6.5.3.3-P01 | §6.5.3.3 | may | A PSIRT may choose to handle security vulnerabilities from customers with a valid support contract through their customer support division rather than receiving them directly. |
| 6.5.3.3-R02 | §6.5.3.3 | should | In that case, appropriate processes and training should be provided to the customer support division. |
| 6.5.3.3-R03 | §6.5.3.3 | should | The customer support division should partner closely with the PSIRT to ensure that the vulnerability is appropriately handled and responded to. |
| 6.5.3.4-R01 | §6.5.3.4 | should | A PSIRT should work with product and services divisions to build a database of contacts for each product. |
| 6.5.3.4-R02 | §6.5.3.4 | should | When a potential vulnerability is reported, the PSIRT should identify the responsible product business division to dispatch the report to them through the contact person. |
| 6.5.3.4-R03 | §6.5.3.4 | should | The information should be shared confidentially on a need-to-know basis. |

§6.5.3.1 notes that the responsibilities in 6.5.3 are "an unordered list" and points to the FIRST
PSIRT Services Framework [4] for example services.

*— end of free preview —*
