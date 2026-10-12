---
schema: "library-distilled/v1"
id: iec-81001-5-1-2021-normative
record: iec-81001-5-1-2021
type: normative
updated: "2026-10-02"
---

# IEC 81001-5-1:2021 (+ ISH1:2025) — normative text available from the free IEC preview

**Read this first.** Paywalled. Source: IEC webstore bilingual preview of the *corrected version 2025-12*
(30 pp, sha256 `b4d73b51…a58`), which carries the full 3-page Interpretation Sheet 1, the Foreword,
Introduction 0.1–0.3, Clause 1 Scope, Clause 2, the ToC, Figure 2 and the Bibliography. **Clause 3
(terms) and the normative Clauses 4–9 and Annexes A–G were not available**; the activity list in
`requirements.yaml` is title-only. Small-caps terms are written in UPPER CASE as in the source.
Text © IEC 2021/2025.

## Interpretation Sheet 1 (IEC 81001-5-1:2021/ISH1:2025, 62A/1692/DISH, RVDISH 62A/1706/RVDISH) — complete

> This interpretation sheet is intended to clarify the following:
> a) Requirements which are needed to provide essential ACCOMPANYING DOCUMENTATION to the operators of the HEALTH SOFTWARE product regarding the transfer of risk related to software items from the MANUFACTURER to the responsible organization or operator.
> b) Requirements which are needed to maintain SECURITY of the HEALTH SOFTWARE product

**Interpretation of 0.2**

> The HEALTH SOFTWARE is part of a connected and complex healthcare ecosystem, which is integrated into a surrounding HEALTH IT SYSTEM and HEALTH IT INFRASTRUCTURE. ISO 81001-1 provides a definition of the sociotechnical ecosystem in which the HEALTH SOFTWARE operates in, and how to reference the security aspect of the HEALTH SOFTWARE within an IT-system inside a broader HEALTHCARE SYSTEM.

**Interpretation of 4.1**

> 4.1.7 Disclosing SECURITY-related issues — NOTE 1 This activity is related to 9.3 through 9.5 where additional supporting details are provided. NOTE 2 On a) "CVSS" and "ranking" address the rating of the severity and characteristics of security vulnerabilities.
>
> 4.1.9 ACCOMPANYING DOCUMENTATION review — NOTE For clarification, the documents mentioned with "SECURITY guidelines" are detailed in 5.8.2 and 5.8.7.

**Interpretation of 4.3 — SOFTWARE ITEM classification relating to risk transfer.** NOTE 1 (foundations, intentions):

Table 1 – SOFTWARE ITEM classification mapped to affected clauses (read from the image in the preview)

| Activity category | Clause | MAINTAINED | SUPPORTED (includes MAINTAINED) | REQUIRED (includes SUPPORTED) |
|---|---|---|---|---|
| Quality Management | 4.3 Software Item classification related to risk transfer (Note: clarifying roles and responsibilities in support) | X | X | X |
| Software development | 5.2.3 Security Risks for REQUIRED SOFTWARE | X* | X* | X |
| Software maintenance | 6.3.1 SUPPORTED SOFTWARE update documentation | X* | X | |
| Software maintenance | 6.3.2 MAINTAINED SOFTWARE security update delivery | X | | |
| Software maintenance | 6.3.3 MAINTAINED SOFTWARE security update INTEGRITY | X | | |

> \* Implied inclusion in clause since IEC 81001-5-1:2021, Clause 3 explicitly defines SUPPORTED SOFTWARE "includes MAINTAINED SOFTWARE" and REQUIRED SOFTWARE "includes SUPPORTED SOFTWARE".

> SOFTWARE ITEM classification related to risk transfer from 4.3 is clarified as follows:
> a) The SOFTWARE ITEM classification categories are nested, but only to ensure clauses that explicitly mention a category are also understood to include the nested categories. Table 1 above notes all clauses that detail requirements specific to a SOFTWARE ITEM classification and notes the implicit inclusion of nested categories. Further requirements of SOFTWARE ITEM classification that are not explicit in an associated clause are not part of this document.
> b) The manufacturer shall apply risk transfer activities for all SOFTWARE ITEMS according to their associated category. An organization's policy and procedures may choose different terms for these classifications if clauses citing requirements for these SOFTWARE ITEM classifications are satisfied. Risks for all SOFTWARE ITEMS should be identified and managed (5.2.3), updates for SOFTWARE ITEMS controlled by the manufacturer or PRODUCT user should be communicated (6.3.1) and updates to manufacturer provided SOFTWARE ITEMS should be made available (6.3.2) and have verifiable integrity (6.3.3). For 4.3, any declaration of conformance, or internal policy/procedure, should state the alternative terminology leveraged and how it maps to the specific SOFTWARE ITEM categories when alternative approaches to MAINTAINED, SUPPORTED and REQUIRED SOFTWARE are utilized.
>
> The following clarifying statements help illustrate how the implicit software category nesting [...]:
> 1) 5.2.3 applies for all 3 categories of software. SECURITY Risks from REQUIRED, SUPPORTED and MAINTAINED software should be identified and managed.
> 2) 6.3.1 applies to MAINTAINED software in addition to SUPPORTED software. PRODUCT users also should be notified about updates to MAINTAINED software and SUPPORTED SOFTWARE.
> 3) 6.3.2 & 6.3.3 applies only to MAINTAINED software.

> NOTE 2 (explain practical consequences) It is generally understood that along with purchasing, installing, and using HEALTH SOFTWARE, the risk related to its use over time (often constrained by legal provisions) transitions to the operator. For the purposes of information security, MANUFACTURERS depend on information from suppliers of SOFTWARE ITEMS (being a logical part of the HEALTH SOFTWARE) for certain post-market activities, such as 9.3, to maintain a secure state.
>
> Similarly, operators depend on information from MANUFACTURERS regarding which SOFTWARE ITEMS are intended to be used with HEALTH SOFTWARE product, which kind of support the MANUFACTURER declares for these SOFTWARE ITEMS and which are not supported. Therefore, aspects of risk transfer of the HEALTH SOFTWARE from the MANUFACTURER to the operator is addressed by the categories introduced in 4.3 and the associated clauses citing the SOFTWARE ITEM classifications.
>
> For technical or organizational reasons, it is possible that operators wish to be in control of when or whether a new security update is being installed on related systems where the MANUFACTURER does not provide the security updates. [...] This is a reason for introducing the category of SUPPORTED SOFTWARE.
>
> For technical or organizational reasons, MANUFACTURERS in some cases are not in a position to obtain security notifications or security updates for certain SOFTWARE ITEMS. This is a reason for introducing the category of REQUIRED SOFTWARE. When vulnerabilities for such ("end-of-support" or otherwise unsupported) software become known, MANUFACTURERS can still select other means of maintaining the overall security of the HEALTH SOFTWARE product.
>
> Over the HEALTH SOFTWARE LIFE CYCLE, the MANUFACTURER can update the SOFTWARE ITEM categorization, which is typically done by downgrading SOFTWARE ITEMS from MAINTAINED to SUPPORTED, from MAINTAINED to REQUIRED or SUPPORTED to REQUIRED. When this happens, the requirements from associated clauses shall be evaluated to ensure appropriate risk transfer from MANUFACTURERS to operators.

> NOTE 3 (distinguish from transitional software) For clarification, Transitional (Annex F) is an attribute applied to the whole HEALTH SOFTWARE product – independent of the above categories for SOFTWARE ITEMS. The term "transitional" does not specify a fourth category for SOFTWARE ITEMS – rather it is a circumstance in which the MANUFACTURER developed the HEALTH SOFTWARE product before IEC 81001-5-1 existed. Therefore, Transitional HEALTH SOFTWARE (Annex F) is an alternative approach for evaluating HEALTH SOFTWARE that was "developed without following all of the ACTIVITIES defined in of IEC 81001-5-1:2021, Clause 4 to Clause 9.

**Interpretation of 6.1**

> 6.2.1 Monitoring public incident reports — NOTE For clarification, this activity specifies "review of the information" rather than review of the source.

## Foreword (preview p.5–6) — provenance

> International Standard IEC 81001-5-1 has been prepared by a Joint Working Group of IEC subcommittee 62A: Common aspects of electrical equipment used in medical practice, of IEC technical committee 62: Electrical equipment in medical practice, and ISO technical committee 215: Health informatics. It is published as a double logo standard. [FDIS 62A/1458/FDIS, RVD 62A/1466/RVD] [...] The contents of the Interpretation sheet 1 (2025-12) have been included in this copy.

## Introduction (preview pp.7–9)

**0.1 Structure**

> PROCESS standards for HEALTH SOFTWARE provide a specification of ACTIVITIES that will be performed by the MANUFACTURER – including software incorporated in medical devices –as a part of a development LIFE CYCLE. The normative clauses of this document are intended to provide minimum best practices for a secure software LIFE CYCLE. Local legislation and regulation are considered.
>
> PROCESS requirements (Clause 4 through Clause 9) have been derived from the IEC 62443-4-1[11] PRODUCT LIFE CYCLE management. Implementations of these specifications can extend existing PROCESSES at the MANUFACTURER's organization – notably existing PROCESSES conforming to IEC 62304[8]. This document can therefore support conformance to IEC 62443-4-1[11].
>
> Normative clauses of this document specify ACTIVITIES that are the responsibility of the MANUFACTURER. The HEALTH SOFTWARE LIFE CYCLE can be part of an incorporating PRODUCT project. Some ACTIVITIES specified in this document depend on input and support from the PRODUCT LIFE CYCLE (for example to define specific criteria). Examples include: RISK MANAGEMENT; requirements; testing; post-release (after first placing HEALTH SOFTWARE on the market).
>
> [...] Clause 4 specifies that MANUFACTURERS develop and maintain HEALTH SOFTWARE within a quality management system (see 4.1) and a RISK MANAGEMENT SYSTEM (4.2). Clause 5 through Clause 8 specify ACTIVITIES and resulting output as part of the software LIFE CYCLE PROCESS implemented by the MANUFACTURER. These specifications are arranged in the ordering of IEC 62304[8]. Clause 9 specifies ACTIVITIES and resulting output as part of the problem resolution PROCESS implemented by the MANUFACTURER.
>
> For expression of provisions in this document, – "can" is used to describe a possibility or capability; and – "must" is used to express an external constraint.

**0.2 Field of application** — applies to development and maintenance of HEALTH SOFTWARE by a MANUFACTURER; recognises bi-lateral communication with HDOs; future parts of the 81001-5 series to address implementation, operations and use. Applies to:

> – software as part of a medical device; – software as part of hardware specifically intended for health use; – software as a medical device (SaMD); and – software-only PRODUCT for other health use.

**0.3 Conformance**

> Conformance with this document focuses on the implementation of requirements regarding PROCESSES, ACTIVITIES, and TASKS – and can be claimed in one of two alternative ways: • for HEALTH SOFTWARE by implementing requirements in Clause 4 through Clause 9 of this document, • for TRANSITIONAL HEALTH SOFTWARE by only implementing the PROCESSES, ACTIVITIES, and TASKS identified in Annex F.
>
> This document is designed to assist in the implementation of the PROCESSES required by IEC 62443-4-1, however, conformance to this document is not necessarily a sufficient condition for conformance to IEC 62443-4-1[11]. More guidance on coverage can be found in Annex D. MANUFACTURERS can implement the specifications for Annex E in order to achieve conformance of documentation to IEC 62443-4-1[11].
>
> Clause 4 through Clause 9 of this document require establishing one or more PROCESSES that include identified ACTIVITIES. [...] None of the requirements in this document requires to implement these ACTIVITIES as one single PROCESS or as separate PROCESSES. The ACTIVITIES specified in this document will typically be part of an existing LIFE CYCLE PROCESS.

## Clause 1 Scope (preview p.10)

> This document defines the LIFE CYCLE requirements for development and maintenance of HEALTH SOFTWARE needed to support conformance to IEC 62443-4-1[11] – taking the specific needs for HEALTH SOFTWARE into account. The set of PROCESSES, ACTIVITIES, and TASKS described in this document establishes a common framework for secure HEALTH SOFTWARE LIFE CYCLE PROCESSES. [...]
>
> The purpose is to increase the CYBERSECURITY of HEALTH SOFTWARE by establishing certain ACTIVITIES and TASKS in the HEALTH SOFTWARE LIFE CYCLE PROCESSES and also by increasing the SECURITY of SOFTWARE LIFE CYCLE PROCESSES themselves. It is important to maintain an appropriate balance of the key properties SAFETY, effectiveness and SECURITY as discussed in ISO 81001-1[17]. This document excludes specification of ACCOMPANYING DOCUMENTATION contents.

Figure 2 – HEALTH SOFTWARE LIFE CYCLE PROCESSES [derived from IEC 62304:2006, Figure 2] (read from image):
customer needs → *System development ACTIVITIES (including RISK MANAGEMENT)* (outside scope) ⇄
**7 Software RISK MANAGEMENT PROCESS**; **5.1** Software development planning → **5.2** Software
requirements analysis → **5.3** Software architectural design → **5.4** Software detailed design → **5.5**
SOFTWARE UNIT implementation → **5.6** Software integration and integration testing → **5.7** SOFTWARE SYSTEM
testing → **5.8** Software release; **8** Software configuration management PROCESS; **9** Software problem
resolution PROCESS — each band annotated "Security - Activities in the product lifecycle" → customer needs satisfied.

## Clause 2 Normative references

> There are no normative references in this document.

## Activities (ToC only) — see `requirements.yaml`

Clause 4 General requirements (4.1.1–4.1.9, 4.2, 4.3); Clause 5 Software development PROCESS (5.1.1–5.8.7);
Clause 6 SOFTWARE MAINTENANCE PROCESS (6.1.1–6.3.3); Clause 7 SECURITY RISK MANAGEMENT PROCESS (7.1.1–7.5);
Clause 8 Software CONFIGURATION MANAGEMENT PROCESS; Clause 9 Software problem resolution PROCESS (9.2–9.5);
Annex F (normative) TRANSITIONAL HEALTH SOFTWARE; Annex G (normative) Object identifiers (Table G.1 –
Object identifiers for conformance concepts). Informative: A Rationale (A.1 Relationship to IEC 62443,
A.2 to IEC 62304, A.3 Risk transfer, Table A.1 tester independence), B Guidance, C THREAT MODELLING
(attack-defense trees, CAPEC/OWASP/SANS, CWSS, DREAD, OCTAVE, STRIDE, Trike, VAST), D Relation to
IEC 62443-4-1 (D.1, D.2), E Documents specified in IEC 62443-4-1.
