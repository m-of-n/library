---
schema: "library-distilled/v1"
id: iec-62443-4-1-2018-normative
record: iec-62443-4-1-2018
type: normative
updated: "2026-10-02"
---

# IEC 62443-4-1:2018 — normative text available from free official sources

**Read this first.** IEC 62443-4-1 is paywalled. Nothing here was read from the IEC normative body.
Three free sources were used, each hashed in `.cache/lane-d/iec/` (see `../summary.md`):

1. **IEC webstore preview** (`info_iec62443-4-1{ed1.0}en.pdf`, 11 pp; bilingual `{ed1.0}b`, 21 pp) — cover, ToC, Foreword, Introduction, Figures 1–2, Clause 1 Scope, Clause 2, the start of 3.1.
2. **iTeh Standards sample** (authorised-distributor preview, 15 pp) — same pages plus terms 3.1.1–3.1.17.
3. **ISASecure SDLA-312 v6.3** (ISCI, Dec 2022) — reproduces each IEC requirement (number, name, *Requirement Description*) beside ISCI's validation activities; and Table 3 (tester independence) as an image.

Requirement text below is quoted from SDLA-312's *Requirement Description* column. Requirement **titles and clause numbers** are from the IEC ToC. The *Rationale and supplemental guidance* subclauses, Clause 4 (concepts, maturity model, Table 1), Annexes A and B are **not available** and are not reproduced.

Text © IEC / ISA; SDLA-312 © 2014-2022 ASCI — reproduced for non-commercial reference (ASCI Terms of Use §C).

## Clause 1 — Scope (IEC preview p.11)

> This part of IEC 62443 specifies process requirements for the secure development of products used in industrial automation and control systems. It defines a secure development life-cycle (SDL) for the purpose of developing and maintaining secure products. This life-cycle includes security requirements definition, secure design, secure implementation (including coding guidelines), verification and validation, defect management, patch management and product end-of-life. These requirements can be applied to new or existing processes for developing, maintaining and retiring hardware, software or firmware for new or existing products. These requirements apply to the developer and maintainer of the product, but not to the integrator or user of the product. A summary list of the requirements in this document can be found in Annex B.

## Clause 2 — Normative references (IEC preview p.11)

> IEC 62443-2-4:2015, Security for industrial automation and control systems – Part 2-4: Security program requirements for IACS service providers  
> IEC 62443-2-4:2015/AMD1:2017

## Introduction (IEC preview pp.8–10) — provenance and scope boundary

> This document has been developed in large part from the Secure Development Life-cycle Assessment (SDLA) Certification Requirements [26] from the ISA Security Compliance Institute (ISCI). Note that the SDLA procedure was based on the following sources: – ISO/IEC 15408-3 (Common Criteria) [18]; – Open Web Application Security Project (OWASP) Comprehensive, Lightweight Application Security Process (CLASP) [36]; – The Security Development Life-cycle by Michael Howard and Steve Lipner [43]; – IEC 61508 Functional safety of electrical/electronic/ programmable electronic safety-related systems [24], and – RCTA DO-178B Software Considerations in Airborne Systems and Equipment Certification [28].

> The product supplier develops products using a process compliant with this document. [...] The products are then integrated together, usually by a system integrator, into an Automation Solution using a process compliant with IEC 62443-2-4. [...] This document only addresses the process used for the development of the product; it does not address design, installation or operation of the Automation Solution or IACS.

Figure 2 roles (preview p.10): **Asset Owner** *Operates (IEC 62443-2-1, IEC 62443-2-4)*; **System Integrator** *Integrates (IEC 62443-2-4, IEC 62443-3-2)* — "Configured for intended environment"; **Product Supplier** *Develops (IEC 62443-4-1)* a **Product (IEC 62443-4-2)** "system, subsystem, or component such as: Applications, Embedded devices, Network components, Host devices" — "Independent of the intended environment".

## Clause 3.1 — Terms available (iTeh sample pp.11–13)

| § | term | definition (verbatim; notes to entry omitted) |
|---|---|---|
| 3.1.1 | abuse case | test case used to perform negative operations of a use case |
| 3.1.2 | access control <protection> | protection of system resources against unauthorized access |
| 3.1.3 | access control <process> | process by which use of system resources is regulated according to a security policy and is permitted by only authorized users according to that policy |
| 3.1.4 | administrator | user who has been authorized to manage security policies/capabilities for a product or system |
| 3.1.5 | asset | physical or logical object owned by or under the custodial duties of an organization, having either a perceived or actual value to the organization |
| 3.1.6 | asset owner | individual or organization responsible for one or more IACSs |
| 3.1.7 | attack surface | physical and functional interfaces of a system that can be accessed and, therefore, potentially exploited by an attacker |
| 3.1.8 | audit log | event log that requires a higher level of integrity protection than provided by typical event logs |
| 3.1.9 | authentication | provision of assurance that a claimed characteristic of an identity is correct |
| 3.1.10 | automation solution | control system and any complementary hardware and software components that have been installed and configured to operate in an IACS |
| 3.1.11 | banned function | software method that is no longer recommended to be used in software because more secure versions exist with less propensity for misuse |
| 3.1.12 | best practices | guidelines for securely designing, developing, testing, maintaining or retiring products that the supplier has determined are commonly recommended by both the security and industrial automation communities |
| 3.1.13 | component | one of the parts that make up a product or system |
| 3.1.14 | configuration management | discipline of identifying the components of an evolving system for the purposes of controlling changes to those components and maintaining continuity and traceability throughout the life-cycle |
| 3.1.15 | defense in depth | approach to defend the system against any particular attack using several independent methods |
| 3.1.16 | dependent component | component external to the product on which the product depends |
| 3.1.17 | deprecated function | software method that is supported but whose use is no longer recommended |

Terms 3.1.18 onward, 3.2 (abbreviations) and 3.3 (conventions) are beyond every free preview.

## Clause 4 — General principles (NOT available)

ToC only: 4.1 Concepts (p.17); 4.2 Maturity model (p.19); Table 1 – Maturity levels (p.20); Figure 3 – Defence in depth strategy is a key philosophy of the secure product life-cycle (p.18). For the ML1–ML4 labels used in `state-machine.yaml`, see the secondary sources cited there.

## Clause 5 — Practice 1 – Security management

Purpose (SDLA-312 p.4 wording; IEC §5.1 not read): *The purpose of the security management practice is to ensure that the security-related activities are adequately planned, documented and executed throughout the product’s lifecycle*

### 5.2 SM-1: Development process  (requirement §5.2.1)

> A general product development/maintenance/support process shall be documented and enforced that is consistent and integrated with commonly accepted product development processes (for example, ISO 9001 [13] certified processes) that include but are not limited to: a) configuration management with change permission controls and audit record logging, b) product description and requirements definition with requirements traceability, c) software or hardware design and implementation practices, such as modular design; d) repeatable testing verification and validation process; e) review and approval of all development process records; and f) life-cycle support.

— `iec-62443-4-1-2018#SM-1` · SDLA-312 v6.3 p.5 · validated by SDLA-SM-1A, SDLA-SM-1B-1, SDLA-SM-1B-2, SDLA-SM-1C, SDLA-SM-1D, SDLA-SM-1E, SDLA-SM-1F

### 5.4 SM-2: Identification of responsibilities  (requirement §5.4.1)

> A process shall be employed that identifies the organizational roles and personnel responsible for each of the processes required by this standard.

— `iec-62443-4-1-2018#SM-2` · SDLA-312 v6.3 p.5 · validated by SDLA-SM-2

### 5.5 SM-3: Identification of applicability  (requirement §5.5.1)

> A process shall be employed for identifying products (or parts of products) to which this standard applies.

— `iec-62443-4-1-2018#SM-3` · SDLA-312 v6.3 p.5 · validated by SDLA-SM-3

### 5.6 SM-4: Security expertise  (requirement §5.6.1)

> A process shall be employed for identifying and providing security training and assessment programs to ensure that personnel assigned to the organizational roles and duties specified in 5.3, SM-2 – Identification of responsibilities, have demonstrated security expertise appropriate for those processes.

— `iec-62443-4-1-2018#SM-4` · SDLA-312 v6.3 p.5 · validated by SDLA-SM-4

### 5.7 SM-5: Process scoping  (requirement §5.7.1)

> A process, that includes justification by documented security analysis, shall be employed to identify the parts of this standard that are applicable to a selected product development project.

— `iec-62443-4-1-2018#SM-5` · SDLA-312 v6.3 p.6 · validated by SDLA-SM-5

> Justification for scoping the level of compliance of a project to this standard shall be subject to review and approval by personnel with the appropriate security expertise (see SM-4).

— `iec-62443-4-1-2018#SM-5.2` · SDLA-312 v6.3 p.6 · validated by SDLA-SM-5

### 5.8 SM-6: File integrity  (requirement §5.8.1)

> A process shall be employed to provide an integrity verification mechanism for all scripts, executables and other important files included in a product.

— `iec-62443-4-1-2018#SM-6` · SDLA-312 v6.3 p.6 · validated by SDLA-SM-6

### 5.9 SM-7: Development environment security  (requirement §5.9.1)

> A process that includes procedural and technical controls shall be employed for protecting the product during development, production and delivery. This includes protecting the product or product update (patch) during design, implementation, testing and release.

— `iec-62443-4-1-2018#SM-7` · SDLA-312 v6.3 p.6 · validated by SDLA-SM-7

### 5.10 SM-8: Controls for private keys  (requirement §5.10.1)

> The supplier shall have procedural and technical controls in place to protect private keys used for code signing from unauthorized access or modification.

— `iec-62443-4-1-2018#SM-8` · SDLA-312 v6.3 p.6 · validated by SDLA-SM-8

### 5.11 SM-9: Security requirements for externally provided components  (requirement §5.11.1)

> A process shall be employed to identify and manage the security risks of all externally provided components used within the product.

— `iec-62443-4-1-2018#SM-9` · SDLA-312 v6.3 p.7 · validated by SDLA-SM-9

### 5.12 SM-10: Custom developed components from third-party suppliers  (requirement §5.12.1)

> A process shall be employed to ensure that product development life-cycle processes for components from a third-party supplier conform to the requirements used in this document when they meet the following criteria: a) the components are developed specifically for a single supplier for a specific purpose; and b) the components can have an impact on security.

— `iec-62443-4-1-2018#SM-10` · SDLA-312 v6.3 p.7 · validated by SDLA-SM-10

### 5.13 SM-11: Assessing and addressing security-related issues  (requirement §5.13.1)

> A process shall be employed for verifying that a product or a patch is not released until its security- related issues have been addressed and tracked to closure (See 10.5, DM-4:Addressing security-related issues). This includes issues associated with a) Requirements (see Clause 6, Practice 2 - Specification of Security requirements); b) secure by design (see Clause 7, Practice 3 - Secure by design); c) implementation (see Clause 8, Practice 4 - Secure implementation); d) verification/validation (see Clause 9, Practice 5 - Security verification and validation testing); and e) defect management (see Clause 10, Practice 6 - Management of security-related Issues).

— `iec-62443-4-1-2018#SM-11` · SDLA-312 v6.3 p.7 · validated by SDLA-SM-11

### 5.14 SM-12: Process verification  (requirement §5.14.1)

> A process shall be employed for verifying that, prior to product release, all applicable security-related processes required by this specification (See SM-5: Process Scoping) have been completed with records documenting the completion of each process.

— `iec-62443-4-1-2018#SM-12` · SDLA-312 v6.3 p.7 · validated by SDLA-SM-12

### 5.15 SM-13: Continuous improvement  (requirement §5.15.1)

> A process shall be employed for continuously improving the SDL.

— `iec-62443-4-1-2018#SM-13` · SDLA-312 v6.3 p.8 · validated by SDLA-SM-13

> This process shall include the analysis of security defects in component/subsystem/system technologies that escape to the field.

— `iec-62443-4-1-2018#SM-13.2` · SDLA-312 v6.3 p.8 · validated by SDLA-SM-13

## Clause 6 — Practice 2 – Specification of security requirements

Purpose (SDLA-312 p.4 wording; IEC §6.1 not read): *The processes specified by this practice are used to document the security capabilities that are required for a product along with the expected product security context*

### 6.2 SR-1: Product security context  (requirement §6.2.1)

> A process shall be employed to ensure that the intended product security context is documented.

— `iec-62443-4-1-2018#SR-1` · SDLA-312 v6.3 p.9 · validated by SDLA-SR-1

### 6.3 SR-2: Threat model  (requirement §6.3.1)

> A process shall be employed to ensure that all products shall have a threat model specific to the current development scope of the product with the following characteristics (where applicable):

— `iec-62443-4-1-2018#SR-2` · SDLA-312 v6.3 p.9 · validated by SDLA-SR-2

> a) correct flow of categorized information throughout the system; b) trust boundaries; c) processes; d) data stores; e) interacting external entities;

— `iec-62443-4-1-2018#SR-2.a-e` · SDLA-312 v6.3 p.9 · validated by SDLA-SR-2A

> f) internal and external communication protocols implemented in the product g) externally accessible physical ports including debug ports h) circuit board connections such as Joint Test Action Group (JTAG) connections or debug headers which might be used to attack the hardware

— `iec-62443-4-1-2018#SR-2.f-h` · SDLA-312 v6.3 p.9 · validated by SDLA-SR-2F

> i) potential attack vectors including attacks on the hardware if applicable j) potential threats and their severity as defined by a vulnerability scoring system (for example, CVSS) l) security-related issues identified

— `iec-62443-4-1-2018#SR-2.i-l` · SDLA-312 v6.3 p.9 · validated by SDLA-SR-2i

> j) potential threats and their severity as defined by a vulnerability scoring system (for example, CVSS)

— `iec-62443-4-1-2018#SR-2.j` · SDLA-312 v6.3 p.10 · validated by SDLA-SR-2J

> k) mitigations and/or dispositions for each threat

— `iec-62443-4-1-2018#SR-2.k` · SDLA-312 v6.3 p.10 · validated by SDLA-SR-2K

> All products shall have an up-to-date threat model with the following characteristics: m) external dependencies in the form of drivers or third party applications (code that is not developed by the supplier) that are linked into the application.

— `iec-62443-4-1-2018#SR-2.m` · SDLA-312 v6.3 p.10 · validated by SDLA-SR-2M

> The threat model shall be reviewed periodically (at least once a year) for released products and updated if required in response to the emergence of new threats to the product even if the design does not change

— `iec-62443-4-1-2018#SR-2.periodic` · SDLA-312 v6.3 p.10 · validated by SDLA-SR-2N

> The threat model shall be reviewed and verified by the development team to ensure that it is correct and understood.

— `iec-62443-4-1-2018#SR-2.review` · SDLA-312 v6.3 p.10 · validated by SDLA-SR-2O

> Any issues identified in the threat model shall be addressed as defined in 10.4, DM-3 – Assessing security-related issues, and 10.5, DM-4 – Addressing security- related issues.

— `iec-62443-4-1-2018#SR-2.issues` · SDLA-312 v6.3 p.10 · validated by SDLA-SR-2O

### 6.4 SR-3: Product security requirements  (requirement §6.4.1)

> A process shall be employed for ensuring that security requirements are documented for the product/feature under development including requirements for security capabilities related to installation, operation, maintenance, and decommissioning

— `iec-62443-4-1-2018#SR-3` · SDLA-312 v6.3 p.10 · validated by SDLA-SR-3

### 6.5 SR-4: Product security requirements content  (requirement §6.5.1)

> A process shall be employed for ensuring that security requirements include the following information: a) the scope and boundaries of the component or system, in general terms in both a physical and a logical way; and b) the required capability security level (SL-C) of the product.

— `iec-62443-4-1-2018#SR-4` · SDLA-312 v6.3 p.11 · validated by SDLA-SR-4

### 6.6 SR-5: Security requirements review  (requirement §6.6.1)

> A process shall be employed to ensure that security requirements are reviewed, updated as necessary and approved to ensure clarity, validity, alignment with the Threat Model (discussed in 6.3 SR-2 –Threat model), and their ability to be verified.

— `iec-62443-4-1-2018#SR-5` · SDLA-312 v6.3 p.11 · validated by SDLA-SR-5

> Each of the following representative disciplines shall participate in this process. Personnel may be assigned to more than one discipline except for testers, who shall remain independent. a) Architects/developers (those who will implement the requirements); b) testers (those who will validate that the requirements have been met); c) customer advocate (such as sales, marketing, product management or customer support); and d) Security Advisor

— `iec-62443-4-1-2018#SR-5.2` · SDLA-312 v6.3 p.11 · validated by SDLA-SR-5

## Clause 7 — Practice 3 – Secure by design

Purpose (SDLA-312 p.4 wording; IEC §7.1 not read): *The processes specified by this practice are used to ensure that the product is secure by design including defence in depth*

### 7.2 SD-1: Secure design principles  (requirement §7.2.1)

> A process shall be employed for developing and documenting a secure design that identifies and characterizes each interface of the product, including physical and logical interfaces, to include: a) an indication of whether the interface is externally accessible (by other products), or internally accessible (by other components of the product), or both; b) security implications of the product security context (see Clause 6, Practice 2 – Specification of security requirements) on the external interface; c) potential users of the interface and the assets that can be accessed through it (directly or indirectly); d) a determination of whether access to the interface crosses a trust boundary; e) security considerations, assumptions and/or constraints associated with the use of the interface within the product security context, including applicable threats; f) the security roles, privileges/rights and access control permissions needed to use the interface and to access the assets defined in c) above; g) the security capabilities and/or compensating mechanisms used to safeguard the interface and the assets defined in c) above, including input validation as well as output and error handling. h) the use of third-party products to implement the interface and their security capabilities; and i) documentation that describes how to use the interface if it is externally accessible. j) description of how the design mitigates the threats identified in the threat model

— `iec-62443-4-1-2018#SD-1` · SDLA-312 v6.3 p.12 · validated by SDLA-SD-1

### 7.3 SD-2: Defense in depth design  (requirement §7.3.1)

> A process shall be employed to implement multiple layers of defence using a risk based approach based on the threat model.

— `iec-62443-4-1-2018#SD-2` · SDLA-312 v6.3 p.12 · validated by SDLA-SD-2

> This process shall be employed for assigning responsibilities to each layer of defence. NOTE 1 Each layer provides additional defence mechanisms NOTE 2 Each layer may be compromised; therefore, secure design principles are applied to each layer. NOTE 3 The objective is to reduce the attack surface of the subsequent layers

— `iec-62443-4-1-2018#SD-2.2` · SDLA-312 v6.3 p.12 · validated by SDLA-SD-2

### 7.4 SD-3: Security design review  (requirement §7.4.1)

> A process shall be employed for conducting design reviews to identify, characterize, and track to closure security-related issues associated with each significant revision of the secure design including but not limited to: a) security requirements (Practice 2) that were not adequately addressed by the design, NOTE 1 Requirements allocation, including security requirements, is part of typical design processes. b) threats and their ability to exploit product interfaces, trust boundaries, and assets (SD-1 – Secure design principles), c) identification of design best practices (SD-4 – Secure design industry recommended practices) that were not followed (for example, failure to apply principle of least privilege) NOTE 2 Characterizing threats and their ability to exploit interfaces is often referred to as threat modeling.

— `iec-62443-4-1-2018#SD-3` · SDLA-312 v6.3 p.13 · validated by SDLA-SD-3

### 7.5 SD-4: Secure design best practices  (requirement §7.5.1)

> A process shall be employed to ensure that secure design best practices are documented and applied to the design process.

— `iec-62443-4-1-2018#SD-4` · SDLA-312 v6.3 p.13 · validated by SDLA-SD-4

> These practices shall be periodically reviewed and updated. Secure design practices include but are not be limited to: a) least privilege (granting only the privileges to users/software necessary to perform intended operations); b) using proven secure components/designs where possible; c) economy of mechanism (striving for simple designs); d) using secure design patterns; f) all trust boundaries are documented as part of the design; and g) removing debug ports, headers and traces from circuit boards used during development from production hardware or documenting their presence and the need to protect them from unauthorized access.

— `iec-62443-4-1-2018#SD-4.2` · SDLA-312 v6.3 p.13 · validated by SDLA-SD-4

> e) attack surface reduction;

— `iec-62443-4-1-2018#SD-4.e` · SDLA-312 v6.3 p.13 · validated by SDLA-SD-4E

## Clause 8 — Practice 4 – Secure implementation

Purpose (SDLA-312 p.4 wording; IEC §8.1 not read): *The processes specified by this practice are used to ensure that the product features are implemented securely*

### 8.2 Applicability

> The requirements of this phase that are applicable to system development, shall only apply to code written in a full variability language.

— `iec-62443-4-1-2018#SI-applicability` · SDLA-312 v6.3 p.15 · validated by SDLA-SI-3

### 8.3 SI-1: Security implementation review  (requirement §8.3.1)

> A process shall be employed to ensure that implementation reviews are performed for identifying, characterizing and tracking to closure security-related issues associated with the implementation of the secure design including: a) identification of security requirements (see Clause 6, Practice 2 – Specification of security requirements) that were not adequately addressed by the implementation; NOTE Requirements allocation, including security requirements, is part of typical design processes. b) identification of secure coding standards (see 8.4, SI-2 – Secure coding standards ) that were not followed (for example, use of banned functions or failure to apply principle of least privilege); c) Static Code Analysis (SCA) for source code to determine security coding errors such as buffer overflows, null pointer dereferencing, etc. using the secure coding standard for the supported programming language.

— `iec-62443-4-1-2018#SI-1` · SDLA-312 v6.3 p.14 · validated by SDLA-SI-1, SDLA-SI-1A, SDLA-SI-1C-1, SDLA-SI-1C-2, SDLA-SI-1C-3

> SCA shall be done using a tool if one is available for the language used.

— `iec-62443-4-1-2018#SI-1.sca-tool` · SDLA-312 v6.3 p.14 · validated by SDLA-SI-1C-1, SDLA-SI-1C-2, SDLA-SI-1C-3

> In addition, static code analysis shall be done on all source code changes including new source code. d) review of the implementation and its traceability to the security capabilities defined to support the security design (see Clause 7, Practice 3 – Secure by design); and e) examination of threats and their ability to exploit implementation interfaces, trust boundaries and assets (see 7.2, SD-1 – Secure design principles, and 7.3, SD-2 – defence in depth design).

— `iec-62443-4-1-2018#SI-1.sca-changes` · SDLA-312 v6.3 p.14 · validated by SDLA-SI-1C-1, SDLA-SI-1C-2, SDLA-SI-1C-3

### 8.4 SI-2: Secure coding standards  (requirement §8.4.1)

> The implementation processes shall incorporate security coding standards that are periodically reviewed and updated and include at a minimum: a) avoidance of potentially exploitable implementation constructs – implementation design patterns that are known to have security weaknesses; b) avoidance of banned functions and coding constructs/design patterns – software functions and design patterns that should not be used because they have known security weaknesses; c) automated tool use and settings (for example, for static analysis tools); d) secure coding practices; e) validation of all inputs that cross trust boundary. f) error handling

— `iec-62443-4-1-2018#SI-2` · SDLA-312 v6.3 p.15 · validated by SDLA-SI-2, SDLA-SI-2A, SDLA-SI-2B, SDLA-SI-2D, SDLA-SI-2E, SDLA-SI-2F, SDLA-SI-2G

## Clause 9 — Practice 5 – Security verification and validation testing

Purpose (SDLA-312 p.4 wording; IEC §9.1 not read): *The processes specified by this practice are used to document the security testing required to ensure that all of the security requirements have been met for the product and that the security of the product is maintained when it is used in its product security context*

### 9.2 SVV-1: Security requirements testing  (requirement §9.2.1)

> A process shall be employed for verifying the product security functions meet the security requirements and that the product handles error scenarios and invalid input correctly.

— `iec-62443-4-1-2018#SVV-1` · SDLA-312 v6.3 p.16 · validated by SDLA-SVV-1A1, SDLA-SVV-1A2, SDLA-SVV-1A3, SDLA-SVV-1B, SDLA-SVV-1C

> Types of testing shall include: a) functional testing of security requirements; b) performance and scalability testing c) boundary/edge condition, stress and malformed or unexpected input tests not specifically targeted at security; and d) trust boundary requirements testing

— `iec-62443-4-1-2018#SVV-1.types` · SDLA-312 v6.3 p.16 · validated by SDLA-SVV-1A1, SDLA-SVV-1A2, SDLA-SVV-1A3, SDLA-SVV-1B, SDLA-SVV-1C

### 9.3 SVV-2: Threat mitigation testing  (requirement §9.3.1)

> A process shall be employed for testing the effectiveness of the mitigation for the threats identified and validated in the threat model.

— `iec-62443-4-1-2018#SVV-2` · SDLA-312 v6.3 p.16 · validated by SDLA-SVV-2-1, SDLA-SVV-2-2

> Activities shall include: a) creating and executing plans to ensure that each mitigation implemented to address a specific threat has been adequately tested to ensure the mitigation works as designed and b) creating and executing plans for attempting to thwart each mitigation.

— `iec-62443-4-1-2018#SVV-2.activities` · SDLA-312 v6.3 p.16 · validated by SDLA-SVV-2-1, SDLA-SVV-2-2

### 9.4 SVV-3: Vulnerability testing  (requirement §9.4.1)

> A process shall be employed for performing tests that focus on identifying and characterizing potential security vulnerabilities in the product.

— `iec-62443-4-1-2018#SVV-3` · SDLA-312 v6.3 p.17 · validated by SDLA-SVV-3A1, SDLA-SVV-3A2, SDLA-SVV-3A3, SDLA-SVV-3A4, SDLA-SVV-3A5, SDLA-SVV-3B, SDLA-SVV-3C1, SDLA-SVV-3C2, SDLA-SVV-3D, SDLA-SVV-3E, SDLA-SVV-3

> Known vulnerability testing shall be based upon, at a minimum, recent contents of an established, industry-recognized, public source for known vulnerabilities.

— `iec-62443-4-1-2018#SVV-3.known` · SDLA-312 v6.3 p.17 · validated by SDLA-SVV-3C1, SDLA-SVV-3C2

> Testing shall include: a) abuse case or malformed or unexpected input testing focused on uncovering security issues. This shall include manual or automated abuse case testing and specialized types of abuse case testing on all external interfaces and protocols for which tools exist. Examples include fuzz testing and network traffic load testing and capacity testing.

— `iec-62443-4-1-2018#SVV-3.a` · SDLA-312 v6.3 p.17 · validated by SDLA-SVV-3A1, SDLA-SVV-3A2, SDLA-SVV-3A3, SDLA-SVV-3A4, SDLA-SVV-3A5

> b) attack surface analysis to determine all avenues of ingress and egress to and from the system, common vulnerabilities including but not limited to week ACLs, exposed ports and services running with elevated privileges.

— `iec-62443-4-1-2018#SVV-3.b` · SDLA-312 v6.3 p.17 · validated by SDLA-SVV-3B

> c) black box known vulnerability scanning focused on detecting known vulnerabilities in the product hardware, host or software components. For example, this could be a network based known vulnerability scan.

— `iec-62443-4-1-2018#SVV-3.c` · SDLA-312 v6.3 p.17 · validated by SDLA-SVV-3C1, SDLA-SVV-3C2

> d) for compiled software, software composition analysis on all binary executable files, including embedded firmware, delivered by the supplier to be installed for a product. This analysis shall detect the following types of problems at a minimum: 1) known vulnerabilities in the product software components; 2) linking to vulnerable libraries; 3) security rule violations; and 4) compiler settings that can lead to vulnerabilities.

— `iec-62443-4-1-2018#SVV-3.d` · SDLA-312 v6.3 p.17 · validated by SDLA-SVV-3D

> e) dynamic runtime resource management testing that detects flaws not visible under static code analysis, including but not limited to denial of service conditions due to failing to release runtime handles, memory leaks and accesses made to shared memory without authentication. This testing shall be applied if such tools are available.

— `iec-62443-4-1-2018#SVV-3.e` · SDLA-312 v6.3 p.17 · validated by SDLA-SVV-3E

### 9.5 SVV-4: Penetration testing  (requirement §9.5.1)

> A process shall be employed to identify and characterize security-related issues via tests that focus on discovering and exploiting security vulnerabilities in the product.

— `iec-62443-4-1-2018#SVV-4` · SDLA-312 v6.3 p.18 · validated by SDLA-SVV-4

### 9.6 SVV-5: Independence of testers  (requirement §9.6.1)

> A process shall be employed to ensure that individuals performing testing are independent from the developers who designed and implemented the product according to the following table (see next row).

— `iec-62443-4-1-2018#SVV-5` · SDLA-312 v6.3 p.18 · validated by SDLA-SVV-5

> The levels of independence are defined as follows: • None – no independence required. Developer can perform the testing. • Independent person – the person who performs the testing cannot be one of the developers of the product. • Independent department – the person who performs the testing cannot report to the same first line manager as any developers of the product. Alternatively, they could be a member of a quality assurance (QA) department.

— `iec-62443-4-1-2018#SVV-5.levels` · SDLA-312 v6.3 p.18 · validated by SDLA-SVV-5

**Table 3 – Required level of independence of testers from developers** (IEC ToC p.37; read as an image on SDLA-312 v6.3 pp.18–19):

| Test type | Reference | Level of independence |
|---|---|---|
| Security requirements testing | SVV-1 – Security requirements testing | Independent department |
| Threat mitigation testing | SVV-2 – Threat mitigation testing | Independent department |
| Abuse case testing | SVV-3 – Vulnerability testing | Independent person |
| Static code analysis | SI-1 – Security implementation review | None |
| Attack surface analysis | SVV-3 – Vulnerability testing | Independent person |
| Known vulnerability scanning | SVV-3 – Vulnerability testing | Independent person |
| Software composition analysis | SVV-3 – Vulnerability testing | None |
| Penetration testing | SVV-4 – Penetration testing | Independent department or organization |

## Clause 10 — Practice 6 – Management of security-related issues

Purpose (SDLA-312 p.4 wording; IEC §10.1 not read): *The processes specified by this practice are used for handling security-related issues of a product that has been configured to employ its defence in depth strategy (Practice 3) within the product security context (Practice 2)*

### 10.2 DM-1: Receiving notifications of security-related issues  (requirement §10.2.1)

> A process shall exist for receiving and tracking to closure security-related issues in the product reported by internal and external sources including at a minimum: a) security verification and validation testers, b) suppliers of third-party components used in the product, c) product developers and testers, and d) product users including integrators, asset owners, end users and maintenance personnel NOTE External security verification and validation testers include researchers

— `iec-62443-4-1-2018#DM-1` · SDLA-312 v6.3 p.20 · validated by SDLA-DM-1A, SDLA-DM-1B

### 10.3 DM-2: Reviewing security-related issues  (requirement §10.3.1)

> A process shall exist for ensuring that reported security-related issues are investigated in a timely manner to determine their: a) applicability to the product, b) verifiability, and c) threats that trigger the issue. NOTE Timeliness is driven by market forces.

— `iec-62443-4-1-2018#DM-2` · SDLA-312 v6.3 p.20 · validated by SDLA-DM-2

### 10.4 DM-3: Assessing security-related issues  (requirement §10.4.1)

> A process shall be employed for analyzing valid security-related issues in the product to include: a) assessing their impact with respect to: 1) the actual security context in which they were discovered, 2) the product’s security context (Practice 2), and 3) the product’s defence in depth strategy (Practice 3), b) severity as defined by a vulnerability scoring system (for example, CVSS) c) identifying all other products/product versions containing the security-related issue (if any), d) identifying the root cause of the issue, and e) identifying related security issues.

— `iec-62443-4-1-2018#DM-3` · SDLA-312 v6.3 p.20 · validated by SDLA-DM-3, SDLA-DM-3A, SDLA-DM-3C, SDLA-DM-3D

> For root cause analysis, a methodical approach such as that described in IEC 62740 [25] may be employed

— `iec-62443-4-1-2018#DM-3.rca` · SDLA-312 v6.3 p.20 · validated by SDLA-DM-3D

### 10.5 DM-4: Addressing security-related issues  (requirement §10.5.1)

> A process shall be employed for addressing security-related issues and determining whether to report them based on the results of the impact assessment (DM-3 – Assessing security-related issues).

— `iec-62443-4-1-2018#DM-4` · SDLA-312 v6.3 p.20 · validated by SDLA-DM-4

> The supplier shall establish an acceptable level of residual risk that shall be applied when determining appropriate way to address each issue. Options include one or more of the following: a) fixing the issue through one or more of the following: 1) defence in depth strategy or design change; 2) addition of one or more security requirements and/or capabilities; 3) use of compensating mechanisms; and/or 4) disabling or removing features b) creating a remediation plan to fix the problem, c) deferring the problem for future resolution (reapply this requirement at some time in the future) and specifying the reason(s) and associated risk(s), d) not fixing the problem if the residual risk is below the established acceptable level of residual risk

— `iec-62443-4-1-2018#DM-4.residual` · SDLA-312 v6.3 p.20 · validated by SDLA-DM-4

> In all cases the following shall be done as well: e) informing other processes of the issue or related issue(s), including processes for other products/product revisions, and f) inform third parties if problems found in included third-party source code

— `iec-62443-4-1-2018#DM-4.all-cases` · SDLA-312 v6.3 p.20 · validated by SDLA-DM-4

> When security related issues are resolved recommendations to prevent similar errors from occurring in the future shall be evaluated.

— `iec-62443-4-1-2018#DM-4.prevent` · SDLA-312 v6.3 p.20 · validated by SDLA-DM-4

> This process shall include a periodic review of open security-related issues to ensure that issues are being addressed appropriately. This periodic review shall at a minimum occur during each release or iteration cycle. NOTE When the resolution decision is to fix the security-related issue in the product implementation, the timing of the release of the fix can result in a patch (see Practice 8) or the fix may be deferred until the next release.

— `iec-62443-4-1-2018#DM-4.periodic` · SDLA-312 v6.3 p.20 · validated by SDLA-DM-4

### 10.6 DM-5: Disclosing security-related issues  (requirement §10.6.1)

> A process shall be employed for informing product users about reportable security- related issues (see 10.5, DM-4 – Addressing security-related issues) in supported products in a timely manner with content that includes but is not limited to the following information: a) issue description, vulnerability score as per CVSS or a similar system for ranking vulnerabilities, and affected product version(s); and b) description of the resolution.

— `iec-62443-4-1-2018#DM-5` · SDLA-312 v6.3 p.20 · validated by SDLA-DM-5

### 10.7 DM-6: Periodic review of security defect management practice  (requirement §10.7.1)

> A process shall be employed for conducting periodic reviews of the security- related issue management process. Periodic reviews of the process shall, at a minimum, examine security-related issues managed through the process since the last periodic review to determine if the management process was complete, efficient, and led to the resolution of each security-related issue.

— `iec-62443-4-1-2018#DM-6` · SDLA-312 v6.3 p.21 · validated by SDLA-DM-6

> Periodic reviews of the security-related issue management process shall be conducted at least annually.

— `iec-62443-4-1-2018#DM-6.annual` · SDLA-312 v6.3 p.21 · validated by SDLA-DM-6

## Clause 11 — Practice 7 – Security update management

Purpose (SDLA-312 p.4 wording; IEC §11.1 not read): *The processes specified by this practice are used to ensure security updates associated with the product are tested for regressions and made available to product users in a timely manner*

### 11.2 SUM-1: Security update qualification  (requirement §11.2.1)

> A process shall be employed for verifying (1) security updates created by the product developer address the intended security vulnerabilities (2) security updates do not introduce regressions, including but not limited to patches created by: a) the product developer; b) suppliers of components used in the product; and c) suppliers of components or platforms on which the product depends.

— `iec-62443-4-1-2018#SUM-1` · SDLA-312 v6.3 p.22 · validated by SDLA-SUM-1

> The Process should include a verification that update is not contradicting other operational, safety or legal constraints

— `iec-62443-4-1-2018#SUM-1.constraints` · SDLA-312 v6.3 p.22 · validated by SDLA-SUM-1

### 11.3 SUM-2: Security update documentation  (requirement §11.3.1)

> A process shall be employed to ensure that documentation about product security updates is made available to product users that includes but is not limited to: a) the product version number(s) to which the security patch applies; b) instructions on how to apply approved patches manually and via an automated process; c) description of any impacts that applying the patch to the product, including reboot; d) instructions on how to verify that an approved patch has been applied; and e) risks of not applying the patch and mediations that can be used for patches that are not approved or deployed by the asset owner.

— `iec-62443-4-1-2018#SUM-2` · SDLA-312 v6.3 p.22 · validated by SDLA-SUM-2

### 11.4 SUM-3: Dependent component or operating system security update documentation  (requirement §11.4.1)

> A process shall be employed to ensure that documentation about dependent component or operating system security updates is made available to product users that includes but is not limited to: a) stating whether the product is compatible with the dependent component or operating system security update b) for security updates that are unapproved by the product vendor, the mitigations that can be used to in lieu of not applying the update.

— `iec-62443-4-1-2018#SUM-3` · SDLA-312 v6.3 p.22 · validated by SDLA-SUM-3

### 11.5 SUM-4: Security update delivery  (requirement §11.5.1)

> A process shall be employed to ensure that security updates for all supported products and product versions are made available to product users in a manner that facilitates verification that the security patch is authentic.

— `iec-62443-4-1-2018#SUM-4` · SDLA-312 v6.3 p.22 · validated by SDLA-SUM-4

### 11.6 SUM-5: Timely delivery of security patches  (requirement §11.6.1)

> A process shall be employed to define a policy that specifies the timeframes for delivering and qualifying (See SUM-1 – Security update qualification) security updates to product users and to ensure that this policy is followed.

— `iec-62443-4-1-2018#SUM-5` · SDLA-312 v6.3 p.22 · validated by SDLA-SUM-5

> At a minimum, this policy shall consider the following factors: a) The potential impact of the vulnerability; b) Public knowledge of the vulnerability; c) Whether published exploits exist for the vulnerability; d) The volume of deployed products that are affected; and e) The availability of an effective mitigation in lieu of the patch.

— `iec-62443-4-1-2018#SUM-5.factors` · SDLA-312 v6.3 p.22 · validated by SDLA-SUM-5

## Clause 12 — Practice 8 – Security guidelines

Purpose (SDLA-312 p.4 wording; IEC §12.1 not read): *The processes specified by this practice are used to provide documentation that describes how to integrate, configure, and maintain the defence in depth strategy of the product in accordance with its product security context*

### 12.2 SG-1: Product defense in depth  (requirement §12.2.1)

> A process shall exist to create product user documentation that describes the security defence in depth strategy for the product to support installation, operation and maintenance that includes: a) security capabilities implemented by the product and their role in the defence in depth strategy; b) threats addressed by the defence in depth strategy; and c) product user mitigation strategies for known security risks associated with the product, including risks associated with legacy code.

— `iec-62443-4-1-2018#SG-1` · SDLA-312 v6.3 p.23 · validated by SDLA-SG-1A, SDLA-SG-1B, SDLA-SG-1C

### 12.3 SG-2: Defense in depth measures expected in the environment  (requirement §12.3.1)

> A process shall be employed to create product user documentation that describes the security defence in depth measures expected to be provided by the external environment in which the product is to be used (see Clause 6, Practice 2 – Specification of security requirements). NOTE These measures can also come from DM-4 – Addressing security-related issues

— `iec-62443-4-1-2018#SG-2` · SDLA-312 v6.3 p.23 · validated by SDLA-SG-2

### 12.4 SG-3: Security hardening guidelines  (requirement §12.4.1)

> A process shall be employed to create product user documentation that includes guidelines for hardening the product when installing and maintaining the product.

— `iec-62443-4-1-2018#SG-3` · SDLA-312 v6.3 p.23 · validated by SDLA-SG-3A, SDLA-SG-3B, SDLA-SG-3C, SDLA-SG-3D, SDLA-SG-3E, SDLA-SG-3G, SDLA-SG-3H

> The guidelines shall include, but are not limited to, instructions, rationale and recommendations for the following: a) integration of the product, including third-party components, with its product security context (see Clause 6, Practice 2 – Specification of security requirements); b) integration of the product’s application programming interfaces/protocols with user applications; c) applying and maintaining the product’s defence in depth strategy (see Clause 7, Practice 3 – Secure by design); d) configuration and use of security options/capabilities in support of local security policies, and for each security option/capability: 1) its contribution to the product’s defence in depth strategy (see Clause 7, Practice 3 – Secure by design); 2) descriptions of configurable and default values that includes how each affects security along with any potential impact each has on work practices; and 3) setting/changing/deleting its value; e) instructions and recommendations for the use of all security-related tools and utilities that support administration, monitoring, incident handling and evaluation of the security of the product; f) instructions and recommendations for periodic security maintenance activities; g) instructions for reporting security incidents for the product to the product supplier; and h) description of the security best practices for maintenance and administration of the product.

— `iec-62443-4-1-2018#SG-3.content` · SDLA-312 v6.3 p.23 · validated by SDLA-SG-3A, SDLA-SG-3B, SDLA-SG-3C, SDLA-SG-3D, SDLA-SG-3E, SDLA-SG-3G, SDLA-SG-3H

### 12.5 SG-4: Secure disposal guidelines  (requirement §12.5.1)

> A process shall be employed to create product user documentation that includes guidelines for removing the product from use.

— `iec-62443-4-1-2018#SG-4` · SDLA-312 v6.3 p.24 · validated by SDLA-SG-4

> The guidelines shall include, but is not limited to instructions and recommendations for the following: a) removing the product from its intended environment (Practice 2), b) including recommendations for removing references and configuration data stored within the environment, c) secure removal of data stored in the product, d) secure disposal of the product to prevent potential disclosure of data contained in the product that could not be removed as described in c) above

— `iec-62443-4-1-2018#SG-4.content` · SDLA-312 v6.3 p.24 · validated by SDLA-SG-4

### 12.6 SG-5: Secure operation guidelines  (requirement §12.6.1)

> A process shall be employed to create product user documentation that describes: a) responsibilities and actions necessary for users, including administrators, to securely operate the product; and b) assumptions regarding the behavior of the user/administrator and their relationship to the secure operation of the product.

— `iec-62443-4-1-2018#SG-5` · SDLA-312 v6.3 p.24 · validated by SDLA-SG-5

### 12.7 SG-6: Account management guidelines  (requirement §12.7.1)

> A process shall be employed to create product user documentation that defines user account requirements and recommendations associated with the use of the product that includes, but is not limited to: a) user account permissions (access control) and privileges (user rights) needed to use the product, including, but not limited to operating system accounts, control system accounts and data base accounts; and b) default accounts used by the product (for example, service accounts) and instructions for changing default account names and passwords.

— `iec-62443-4-1-2018#SG-6` · SDLA-312 v6.3 p.24 · validated by SDLA-SG-6

### 12.8 SG-7: Documentation review  (requirement §12.8.1)

> A process shall be employed to identify, characterize, and track to closure errors and omissions in all user manuals including the security guidelines to include: a) coverage of the product’s security capabilities, b) integration of the product with its intended environment (Practice 2), and c) assurance that all documented practices are secure

— `iec-62443-4-1-2018#SG-7` · SDLA-312 v6.3 p.25 · validated by SDLA-SG-7A, SDLA-SG-7B, SDLA-SG-7C

## Annexes (NOT available)

ToC only: Annex A (informative) Possible metrics (p.48); Annex B (informative) Table of requirements — Table B.1 Summary of all requirements (p.50); Bibliography (p.52). Table 2 – Example SDL continuous improvement activities (p.26) is also not available.

