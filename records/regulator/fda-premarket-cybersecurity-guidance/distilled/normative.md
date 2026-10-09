---
schema: "library-distilled/v1"
id: fda-premarket-cybersecurity-guidance-normative
record: fda-premarket-cybersecurity-guidance
type: normative
updated: "2026-10-02"
---

# Normative text — FDA, Cybersecurity in Medical Devices: QMS Considerations and Content of Premarket Submissions (Feb 3 2026)

Every paragraph or list item of the guidance that yields at least one entry in
`requirements.yaml`, **verbatim**, in source order and source structure, followed by the ids it
yields. Footnote call numbers are rendered `[^n]`; the footnotes that carry statements are quoted
under the section that calls them. Paragraphs with no normative form (background, examples) are
omitted — they are in the full capture `.cache/fda-premarket-cybersecurity-guidance.md`. Section
I states the force of every 'should' below:

> In general, FDA’s guidance documents do not establish legally enforceable responsibilities. Instead, guidances describe the Agency’s current thinking on a topic and should be viewed only as recommendations, unless specific regulatory or statutory requirements are cited. The use of the word should in Agency guidances means that something is suggested or recommended, but not required. — §I

## III Background

Additionally, section 3305 of the Food and Drug Omnibus Reform Act of 2022 (“FDORA”), enacted on December 29, 2022, added section 524B “Ensuring Cybersecurity of Medical Devices” to the FD&C Act. Effective March 29, 2023, with respect to premarket submissions for “cyber devices,” section 524B(a) provides that sponsors must include information to ensure the device meets the cybersecurity requirements under section 524B(b).[^14] Under section 524B(a) of the FD&C Act, a person who submits a 510(k), PMA, PDP, De Novo, or HDE for a device that meets the definition of a cyber device, as defined under section 524B(c), is required to submit information to ensure that cyber devices meet the cybersecurity requirements under section 524B(b).[^15] Section 524B(c) of the FD&C Act defines “cyber device” as a device that “(1) includes software validated, installed, or authorized by the sponsor as a device or in a device; (2) has the ability to connect to the internet; and (3) contains any such technological characteristics validated, installed, or authorized by the sponsor that could be vulnerable to cybersecurity threats” (see Section VII.B for more information on the term “cyber device”). The recommendations in this guidance are intended to help manufacturers meet their obligations under section 524B of the FD&C Act.

`III-01 III-02`


> [^15]: In addition to the cybersecurity requirements set forth in section 524B(b) of the FD&C Act, section 524B(b)(4) of the FD&C Act requires cyber device manufacturers to comply with any other such requirements FDA sets forth in regulations “to demonstrate reasonable assurance that the device and related systems are cybersecure.”  `fn15-01`

## IV General Principles

### IV.A Cybersecurity is Part of Device Safety and the Quality Management System Regulation (QMSR)

Device manufacturers must establish and follow quality management systems to help ensure that their products consistently meet applicable requirements and specifications. The quality management systems requirements are found in the QMSR in 21 CFR Part 820, which incorporates by reference ISO 13485. Depending on the device, QMS requirements may be relevant at the premarket stage, postmarket stage,[^16] or both.

`IV.A-01`


> [^16]: In the postmarket context, design and development may also be important to ensure medical device cybersecurity and maintain medical device safety and effectiveness. FDA recommends that device manufacturers implement comprehensive cybersecurity risk management programs and documentation consistent with the QMSR, including but not limited to complaint handling (ISO 13485 Subclause 8.2.2 and 21 CFR 820.35(a)), quality audit (Subclause 8.2.4), analysis of data and improvement (Subclauses 8.4 and 8.5), software validation (Subclause 7.3.7), risk management (Subclause 7.1), and servicing (Subclause 7.5.4 and 21 CFR 820.35(b)).  `fn16-01`

In the premarket context, in order to demonstrate a reasonable assurance of safety and effectiveness for certain devices with cybersecurity risks, documentation outputs related to the ongoing requirements of the QMSR may be one source of documentation to include as part of the premarket submission.[^17] This guidance is intended to explain how such documentation that may be relevant for QMSR compliance can also be used to show how a sponsor or manufacturer is addressing cybersecurity considerations relevant to a device. For example, 21 CFR 820.10(c) requires that for all classes of devices automated with software, a manufacturer must comply with the requirements in Design and Development, Clause 7.3 and its subclauses of ISO 13485.[^18] As part of design and development, “[d]esign and development validation shall be performed in accordance with planned and documented arrangements to ensure that the resulting product is capable of meeting the requirements for the specified application or intended use” (Subclause 7.3.7). Design and development validation includes validation of device software. In addition, Subclause 7.1 of ISO 13485 specifies that the “organization shall document one or more processes for risk management in product realization.” As part of the software validation required by Subclause 7.3.7, and risk management, including the requirements of Subclause 7.1, software device manufacturers may need to establish cybersecurity risk management and validation processes, where appropriate. See also FDA’s guidance titled “Content of Premarket Submissions for Device Software Functions.”

`IV.A-02 IV.A-03 IV.A-04`

Software validation and risk management are key elements of cybersecurity analyses and demonstrating whether a device has a reasonable assurance of safety and effectiveness. FDA requires manufacturers to implement development processes that account for and address software risks throughout the design and development process, as discussed in ISO 13485 regarding design and development, which may include cybersecurity considerations.[^19] For example, these processes should address the identification of security risks, the design requirements for how the risks will be controlled, and the evidence that the controls function as designed and are effective in their environment of use for ensuring adequate security.

`IV.A-05 IV.A-06`

#### IV.A.1 A Secure Product Development Framework (SPDF) may be one way to satisfy the QMSR

Using an SPDF is one approach to help ensure that the QMSR is met. Because of its benefits in helping comply with the QMSR and cybersecurity, FDA encourages manufacturers to use an SPDF, but other approaches might also satisfy the QMSR.

`IV.A.1-01`

### IV.B Designing for Security

Premarket submissions should include information that describes how the above security objectives are addressed by and integrated into the device design. The extent to which security requirements, architecture, supply chain, and implementation are needed to meet these objectives will depend on but may not be limited to:

`IV.B-01`

SPDF processes aim to reduce the number and severity of vulnerabilities and thereby reduce the exploitability of a medical device system and the associated risk of patient harm. Because exploitation of known vulnerabilities or weak cybersecurity controls should be considered reasonably foreseeable failure modes for medical device systems, these factors should be addressed in the device design.[^21] One of the key benefits of using an SPDF is that a medical device system is more likely to be secure by design, such that the device is designed from the outset to be secure within its system and/or network of use throughout the device lifecycle.

`IV.B-02`

### IV.C Transparency

FDA believes that the cybersecurity information discussed in this guidance is important for the safe and effective use of devices and should be included in device labeling, as discussed below in Section VI.

`IV.C-01`

### IV.D Submission Documentation

Device cybersecurity design and documentation are expected to scale with the cybersecurity risk of that device. Manufacturers should take into account the larger system in which the device may be used. For example, a cybersecurity risk assessment performed on a simple, non-connected thermometer may conclude that the risks are limited, and therefore such a device needs only a limited security architecture (i.e., addressing only device hardware and software) and few security controls based on the technical characteristics and design of the device. However, if a thermometer is used in a safety-critical control loop, or is connected to networks or other devices, then the cybersecurity risks for the device are considered to be greater and more substantial design and development activities should result. Submitters should consider including in premarket submissions to FDA documentation generated from those design and development activities used during the development of a device with cybersecurity risks as a way to demonstrate reasonable assurance of safety and effectiveness. This guidance identifies the cybersecurity information FDA recommends to help support a premarket submission for devices within the scope of this guidance, including but not limited to cyber devices.[^22]

`IV.D-01 IV.D-02 IV.D-03`

As cybersecurity is part of device safety and effectiveness, cybersecurity controls established during premarket development should also take into consideration the intended and actual use environment (see Section IV.B). Cybersecurity risks evolve over time and as a result, the effectiveness of cybersecurity controls may degrade as new risks, threats, and attack methods emerge. In the 510(k) context, FDA evaluates the cybersecurity information submitted and the protections the cybersecurity controls provide in demonstrating substantial equivalence (see section 513(i) of the FD&C Act and 21 CFR 807.100(b)(2)(ii)(B)).[^23]

`IV.D-04`

This guidance recommends cybersecurity information be included in submissions based on cybersecurity risks, not on any other criteria or level of risk/concern established in a separate FDA guidance (e.g., the risk-based approach in the Premarket Software Guidance to help determine a device’s Documentation Level). For example, a device that is determined to have a greater software risk may only have a small cybersecurity risk due to how the device is designed. Likewise, a device with a smaller software risk may have a significant cybersecurity risk. Therefore, the recommendations in this guidance regarding information to be submitted to FDA are intended to address the cybersecurity risk, as assessed by the cybersecurity risk assessment during development of a device, and are expected to scale based on the cybersecurity risk. The premarket submission documentation recommendations throughout this guidance apply to all premarket submissions and are intended to be used to support FDA’s assessment of a device’s safety and effectiveness.

`IV.D-05`

## V Using an SPDF to Manage Cybersecurity Risks

The documentation recommended in this guidance is based on FDA’s experience evaluating the safety and effectiveness of devices with cybersecurity vulnerabilities. However, sponsors may use alternative approaches and provide different documentation so long as their approach and documentation satisfy premarket submission requirements in applicable statutory provisions and regulations. The increasingly interconnected nature of medical devices has demonstrated the importance of addressing cybersecurity risks associated with device connectivity in device design because of the effects on safety and effectiveness.[^24] Cybersecurity risks to the medical device or to the larger medical device system can be reasonably controlled through using an SPDF.

`V-01`

FDA recommends that manufacturers use device design processes such as those described in the QMSR, including ISO 13485, to support secure product development and maintenance. To preserve flexibility for manufacturers, manufacturers may use other existing frameworks that satisfy the QMSR and align with FDA’s recommendations for using an SPDF. Possible frameworks to consider include, but are not limited to, the medical device-specific framework that can be found in the Medical Device and Health IT Joint Security Plan (JSP2) [^26] and IEC 81001-5-1. Frameworks from other sectors may also comply with the QMSR, like the framework provided in ANSI/ISA 62443-4-1 Security for industrial automation and control systems Part 4-1: Product security development life-cycle requirements.[^27]

`V-02 V-03`

The following subsections provide recommendations for using SPDF processes that FDA believes provide important considerations for the development of devices that are safe and effective, how these processes can complement the QMSR, and the documentation FDA recommends manufacturers provide for review as part of premarket submissions. These recommendations may be helpful for manufacturers of cyber devices that must “design, develop, and maintain processes and procedures to provide a reasonable assurance that the device and related systems are cybersecure . . .” pursuant to section 524B(b)(2) of the FD&C Act (see Section VII.C.2). The information in these sections does not represent a complete SPDF. For more information on SPDFs, see earlier in Section V. In addition, FDA does not recommend that manufacturers discontinue existing, effective processes.

`V-04`

### V.A Security Risk Management

To fully account for cybersecurity risks in medical device systems, the safety and security risks of each device should be assessed within the context of the larger system in which the device operates. In the context of cybersecurity, security risk management processes are critical because, given the evolving nature of cybersecurity threats and risks, no device is, or can be, completely secure. Security risk management should be an integrated part of a manufacturer’s entire quality management system, addressed throughout the TPLC.[^28] The quality management system processes entail the technical, personnel, and management practices, among others, that manufacturers use to manage potential risks to their devices and ensure that their devices are, and once on the market, remain, safe and effective, which includes security.

`V.A-01 V.A-02`

The scope and objective of a security risk management process, in conjunction with other SPDF processes (e.g., security testing), is to expose how threats, through vulnerabilities, can manifest patient harm and other potential risks. These processes should also ensure that risk control measures for one type of risk assessment do not inadvertently introduce new risks in the other. For example, AAMI TIR57 and ANSI/AAMI SW96 detail how the security and safety risk management processes should interface to ensure all risks are adequately assessed.[^29] FDA recommends that security risk management processes, as detailed in the QMSR and ISO 13485,[^30] be established or incorporated into those that already exist, and should address the manufacturer’s design, manufacturing, and distribution processes, as well as updates across the TPLC. The processes in ISO 13485, as incorporated by reference in the QMSR, that may be relevant in this context include, but are not limited to design and development (Subclause 7.3 of ISO 13485), production processes (Subclause 7.5), and improvement (including corrective actions and preventive actions) (Subclause 8.5) to ensure both safety and security risks are adequately addressed. For completeness in performing risk management under Subclause 7.1, FDA recommends that device manufacturers conduct both a safety risk assessment and a separate, accompanying security risk assessment to ensure a more comprehensive identification and management of patient safety risks.

`V.A-03 V.A-04 V.A-05`

A device should be designed to eliminate or mitigate known vulnerabilities. For marketed devices, if comprehensive design mitigations are not possible, compensating controls should be considered. For all devices, when any known vulnerabilities are only partially mitigated or unmitigated by the device design, they should be assessed as reasonably foreseeable risks in the risk assessment and be assessed for additional control measures or risk transfer[^31] to the user/operator, or, if necessary, the patient. Risk transfer, if appropriate, should only occur when all relevant risk information is known, assessed, and appropriately communicated to users and includes risks inherited from the supply chain as well as how risk transfer will be handled when the device or manufacturer-controlled assets of the medical device system reach end of support and end of life and whether or how the user is able to take on that role (e.g., if the user may be a patient).

`V.A-06 V.A-07 V.A-08 V.A-09`

To document the security risk management activities for a medical device system, FDA recommends that manufacturers generate a security risk management plan and report such as that described in AAMI TIR57 and ANSI/AAMI SW96.[^32] Manufacturers should include their security risk management reports—including the outputs of their security risk management processes—in their premarket submissions to help demonstrate the safety and effectiveness of the device. A security risk management report, such as that described in AAMI TIR57 and ANSI/AAMI SW96, should be sufficient to support the security risk management process aspect of demonstrating a reasonable assurance of safety and effectiveness. Such report should include the documentation elements for the system threat modeling, cybersecurity risk assessment, Software Bill of Materials (SBOM), component support information, vulnerability assessments, and unresolved anomaly assessment(s) described in the sections below.[^33] In the subsections below, we discuss FDA’s recommendations regarding the scope and/or content of specific security risk management documentation elements.

`V.A-10 V.A-11 V.A-12`

In addition to containing the documentation elements listed above, the security risk management report should:

`V.A-13`

- Summarize the risk evaluation methods and processes;  `V.A-14`
- Detail the residual risk conclusion from the security risk assessment;  `V.A-15`
- Detail the risk mitigation activities undertaken as part of a manufacturer’s risk management processes; and  `V.A-16`
- Provide traceability between the threat model, cybersecurity risk assessment, SBOM, and testing documentation as discussed later in this guidance as well as other relevant cybersecurity risk management documentation.  `V.A-17`

#### V.A.1 Threat Modeling

With respect to security risk management, and in order to identify appropriate security risks and controls for the medical device system, FDA recommends that threat modeling be performed to inform and support the risk analysis activities. As part of the risk assessment, FDA recommends threat modeling be performed throughout the design process and be inclusive of all medical device system elements.

`V.A.1-01 V.A.1-02`

The threat model should:

`V.A.1-03`

- Identify medical device system risks and mitigations as well as inform the pre- and post-mitigation risks considered as part of the cybersecurity risk assessment;  `V.A.1-04`
- State any assumptions about the medical device system or environment of use (e.g., hospital networks are inherently hostile, therefore manufacturers are recommended to assume that an adversary controls the network with the ability to alter, drop, and replay packets); and  `V.A.1-05`
- Capture cybersecurity risks introduced through the supply chain, manufacturing, deployment, interoperation with other devices, maintenance/update activities, and decommission activities that might otherwise be overlooked in a traditional safety risk assessment process.  `V.A.1-06`

FDA recommends that premarket submissions include threat modeling documentation to demonstrate how the medical device system has been analyzed to identify potential security risks that could impact safety and effectiveness. There are a number of methodologies and/or combinations of methods for threat modeling that manufacturers may choose to use.[^34] Rationale for the methodology(ies) selected should be provided with the threat modeling documentation. Additional recommendations on how threat modeling documentation should be submitted to FDA are discussed in Section V.B below.

`V.A.1-07 V.A.1-08 V.A.1-09`

Threat modeling activities can be performed and/or reviewed during design reviews. FDA recommends that threat modeling documentation include sufficient information on threat modeling activities performed by the manufacturer to assess and review the security features built into the device such that they holistically evaluate the device and the system in which the device operates, for the safety and effectiveness of the device.

`V.A.1-10`

#### V.A.2 Cybersecurity Risk Assessment

As a part of security risk management, security risks and controls should be assessed for residual risks as part of a cybersecurity risk assessment. Effective security risk assessments address the fact that cybersecurity-related failures can occur either intentionally or unintentionally. Accordingly, cybersecurity risks are difficult to predict, meaning that it is not possible to assess and quantify the likelihood of an incident occurring based on historical data or modeling (also known as a “probabilistic manner”). This non-probabilistic approach is not the fundamental approach performed in safety risk management under ISO 14971 and further underscores why safety and security risk management are distinct but connected processes. Instead, security risk assessment processes focus on exploitability, or the ability to exploit vulnerabilities present within a device and/or system. FDA recommends that manufacturers assess identified risks according to the level of risk posed from the device and the system in which it operates. Additional discussion on exploitability assessments for the security risk assessment can be found in FDA’s Postmarket Cybersecurity Guidance.

`V.A.2-01 V.A.2-02`

Acceptance criteria for cybersecurity risks should carefully consider the TPLC of the medical device system, as it might be more difficult to mitigate cybersecurity issues once the device is marketed. As discussed above in Sections IV.B and V.A, known vulnerabilities should be assessed as reasonably foreseeable risks. The cybersecurity risk assessment for vulnerabilities identified during cybersecurity testing should also consider the TPLC of the device as the exploitability of the vulnerability is likely to increase over the device lifecycle. If a penetration tester, for example, was able to exploit a vulnerability, the ability of a threat actor to exploit that vulnerability is likely to increase over the device lifecycle. Furthermore, vulnerabilities identified in CISA’s Known Exploited Vulnerabilities Catalog should be designed out of the device, as they are already being exploited and expose the medical device system and users to the risk.

`V.A.2-03 V.A.2-04 V.A.2-05 V.A.2-06`

FDA recommends that the cybersecurity risk assessment provided in premarket submissions capture the risks and controls identified from the threat model. The methods used for scoring the risk pre- and post-mitigation and the associated acceptance criteria as well as the method for transferring security risks into the safety risk assessment process should also be provided as part of the premarket submission.

`V.A.2-07 V.A.2-08`

#### V.A.3 Interoperability Considerations

While cybersecurity controls may increase the complexity of interfaces to allow for interoperability, when properly implemented, the cybersecurity controls can help ensure that these capabilities remain safe and effective. Cybersecurity controls should be used as a means to allow for the safe and effective exchange and use of information. Additionally, cybersecurity controls should not be intended to prohibit a user from accessing their device data.

`V.A.3-01 V.A.3-02`

When common technology and communication protocols are used to enable interoperability (e.g., Bluetooth, Bluetooth Low Energy, network protocols), device manufacturers should assess whether added security controls beneath such communication are needed to ensure the safety and effectiveness of the device (e.g., added security controls beneath Bluetooth Low Energy to protect against risks if vulnerabilities in the Bluetooth Low Energy protocol or supporting technology are discovered).

`V.A.3-03`

In addition to the recommendations in the Interoperability Guidance, manufacturers should consider the appropriate cybersecurity risks and controls associated with the interoperability capabilities and document these considerations as recommended throughout this guidance.

`V.A.3-04`

#### V.A.4 Third-Party Software Components

As discussed in FDA’s guidance “Off-The-Shelf (OTS) Software Use in Medical Devices,” medical devices commonly include third-party software components,[^35] including off-the-shelf and open source software. When these components are incorporated, security risks of the software components should become factors of the overall medical device system risk management processes and documentation.

`V.A.4-01`

As part of demonstrating compliance with design and development under Subclause 7.3 of ISO 13485, and to support supply chain risk management processes, all software, including those developed by the device manufacturer (“proprietary software”) or obtained from third parties, should be assessed for cybersecurity risk. Device manufacturers should document all software components of a device and address or otherwise mitigate risks associated with these software components.

`V.A.4-02 V.A.4-03`

In addition, under Subclause 7.4 of ISO 13485, a manufacturer must put in place processes and controls to ensure that its suppliers conform to the manufacturer’s requirements. Such information is documented in the Design and Development Files, required by Subclause 7.3.10, and Medical Device File, required by Subclause 4.2.3. This documentation demonstrates the device’s overall compliance with the QMSR, as well as that the third-party components meet specifications established for the device. Security risk assessments that include analyses and considerations of cybersecurity risks that may exist in or be introduced by third-party software and the software supply chain may help demonstrate that manufacturers have adequately ensured such compliance and documented such history.

`V.A.4-04`

Software is updated over time to provide additional features, address security concerns, and otherwise be maintained. These changes may introduce new considerations or risks that must be accounted for as part of risk management. As a result, device manufacturers should establish and maintain custodial control of device source code (the original “copy” of the software) throughout the lifecycle of a device as part of configuration management.[^36] This may be accomplished through different methods, such as source code escrow or source code backups, among others.[^37]

`V.A.4-05 V.A.4-06`


> [^36]: While some suppliers may not grant access to source code, manufacturers may consider adding to their purchasing controls acquisition of the source code should the purchased software reach end of support or end of life from the supplier earlier than the intended end of support or end of life of the medical device.  `fn36-01`

Manufacturers may not have control of source code due to licensing restrictions, terms of supplier agreements, or other challenges. While source code is not required to be provided in premarket submissions, manufacturers should include plans for how third-party software components could be updated or replaced if support ends or other software issues arise in premarket submissions. The device manufacturer should also provide users with whatever information they may need in the device labeling to allow them to manage risks associated with the software components, including known vulnerabilities, configuration specifications, and other relevant security and risk management considerations.

`V.A.4-07 V.A.4-08`

##### V.A.4(a) Software Bill of Materials (SBOM)

Because vulnerability management is a critical part of a device’s security risk management processes, an SBOM or an equivalent capability should be maintained as part of the device’s configuration management, be regularly updated to reflect any changes to the software in marketed devices, and should support documentation, such as the types detailed in Subclause 7.3.10 (Design and Development Files) and Subclause 4.2.3 (Medical Device File) of ISO 13485.

`V.A.4.a-01`

To assist FDA’s assessment of the device risks and associated impacts on safety and effectiveness related to cybersecurity, FDA recommends that premarket submissions include SBOM documentation as outlined below. For cyber devices, an SBOM is required (see section 524B(b)(3) of the FD&C Act and Section VII.C.3 of this guidance). SBOMs can also be an important tool for transparency with users of potential risks as part of labeling as addressed later in Section VI.

`V.A.4.a-02 V.A.4.a-03`

##### V.A.4(b) Documentation Supporting Software Bill of Materials

FDA’s guidance document “Off-The-Shelf (OTS) Software Use in Medical Devices” describes information that should be provided in premarket submissions for software components for which a manufacturer cannot claim complete software lifecycle control. In addition to the information recommended in that guidance, manufacturers should provide machine-readable SBOMs consistent with the minimum elements (also referred to as “baseline attributes”) identified in the October 2021 National Telecommunications and Information Administration (NTIA) Multistakeholder Process on Software Component Transparency document “Framing Software Component Transparency: Establishing a Common Software Bill of Materials (SBOM).”

`V.A.4.b-01`

In addition to the minimum elements identified by NTIA, for each software component contained within the SBOM, manufacturers should include in the premarket submission:

`V.A.4.b-02`

- The software level of support provided through monitoring and maintenance from the software component manufacturer (e.g., the software is actively maintained, no longer maintained, abandoned); and  `V.A.4.b-03`
- The software component’s end-of-support date.  `V.A.4.b-04`

When provided, manufacturers may choose to provide these additional elements as part of the SBOM, or they may provide it separately, such as in an addendum. Industry-accepted formats of SBOMs are encouraged.

`V.A.4.b-05 V.A.4.b-06`

If a manufacturer is unable to provide the SBOM information to FDA, the manufacturer should provide a justification for why the information cannot be included in the premarket submission.

`V.A.4.b-07`

As part of the premarket submission, manufacturers should also identify all known vulnerabilities associated with the device and the software components, including those identified in CISA’s Known Exploited Vulnerabilities Catalog. For each known vulnerability, manufacturers should describe how the vulnerabilities were discovered to demonstrate whether the assessment methods were sufficiently robust. For components with known vulnerabilities, device manufacturers should provide in premarket submissions:

`V.A.4.b-08 V.A.4.b-09 V.A.4.b-10`

- A safety and security risk assessment of each known vulnerability (including device and system impacts); and  `V.A.4.b-11`
- Details of applicable safety and security risk controls to address the vulnerability. If risk controls include compensating controls, those should be described in an appropriate level of detail.  `V.A.4.b-12 V.A.4.b-13`

#### V.A.5 Security Assessment of Unresolved Anomalies

FDA’s Premarket Software Guidance recommends that device manufacturers provide a list of software anomalies that exist in a product at the time of submission. For each anomaly, FDA recommends that device manufacturers conduct an evaluation of the anomaly’s impact on the device’s safety and effectiveness, and consult the Premarket Software Guidance to assess the associated documentation recommended for inclusion in such device’s premarket submission.

`V.A.5-01`

Some anomalies discovered during development or testing may have security implications and may also be considered vulnerabilities. As a part of ensuring a complete security risk assessment under Subclause 7.1 of ISO 13485, the assessment for impacts to safety and effectiveness may include an assessment for the potential security impacts of anomalies. The assessment should also include consideration of any present Common Weakness Enumeration (CWE) categories.[^39]

`V.A.5-02 V.A.5-03`

The criteria and rationales for addressing the resulting anomalies with security impacts should be provided as part of documentation in the premarket submission.

`V.A.5-04`

#### V.A.6 TPLC Security Risk Management

Cybersecurity risks may continue to be identified throughout the device’s TPLC. Manufacturers should ensure they have appropriate resources to identify, assess, and mitigate cybersecurity vulnerabilities as they are identified throughout the supported device lifecycle.

`V.A.6-01`

As part of using an SPDF, manufacturers should update their security risk management documentation as new information becomes available, such as when new threats, vulnerabilities, assets, or adverse impacts are discovered during development and after the device is released. When maintained throughout the device lifecycle, this documentation (e.g., threat modeling, cybersecurity risk assessment) can be used to quickly identify vulnerability impacts once a device is released and, when appropriate, to support timely improvement, through corrective actions and preventive actions, described in Subclause 8.5 of ISO 13485.

`V.A.6-02`

Over the service life of a device, FDA recommends that the risk management documentation account for any differences in the risk management for fielded devices (e.g., marketed devices or devices no longer marketed but still in use). For example, if an update is not applied automatically for all fielded devices, then there will likely be different risk profiles for differing software configurations of the device. FDA recommends that vulnerabilities be assessed for any differing impacts for all fielded versions to ensure patient risks are being accurately assessed. Additional information as to whether a new premarket submission (e.g., PMA, PMA supplement, or 510(k)) or 21 CFR Part 806 reporting is needed based on postmarket vulnerabilities and general postmarket cybersecurity risk management is discussed in the Postmarket Cybersecurity Guidance.

`V.A.6-03 V.A.6-04`

To demonstrate the effectiveness of a manufacturer’s processes, FDA recommends that a manufacturer track and record the measures and metrics below,[^40] and provide them in premarket submissions and PMA annual reports (21 CFR 814.84), when available.[^41] Selecting appropriate measures and metrics for the processes that define an SPDF is important to ensure that device design appropriately addresses cybersecurity in compliance with the QMSR. At a minimum, FDA recommends tracking the following measures and metrics, or those that provide equivalent information:

`V.A.6-05 V.A.6-06`


> [^40]: The measures and metrics provided are examples; alternative or additional measures and metrics may also be considered and reported.  `fn40-01`


> [^41]: If a manufacturer has not marketed prior versions or the premarket submission does not pertain to a marketed product (e.g., PMA supplement), FDA acknowledges that these measures and metrics might not be available, but recommends that manufacturers include these as part of their risk management plan and SPDF processes.  `fn41-01`

- Percentage of identified vulnerabilities that are updated or patched (defect density);  `V.A.6-07`
- Duration from vulnerability identification to when it is updated or patched; and  `V.A.6-08`
- Duration from when an update or patch is available to complete implementation in devices deployed in the field, to the extent known.  `V.A.6-09`

Averages of the above measures should be provided if multiple vulnerabilities are identified and addressed. These averages may be provided over multiple time frames based on volume or in response to process or procedure changes to increase efficiencies of these measures over time.

`V.A.6-10`

### V.B Security Architecture

Subclause 7.3.1 of ISO 13485 requires manufacturers to document procedures for design and development. Under Subclause 7.3.2, a manufacturer must establish and maintain plans that describe or reference the design and development activities and define responsibility for implementation. Such plans must be maintained and updated as design and development progresses (Subclause 7.3.2). Under Subclause 7.3.3, a manufacturer must determine and maintain inputs related to product requirements to ensure that the design requirements relating to a device are appropriate and address the intended use of the device. Under Subclause 7.3.4, design and development outputs must be in a form suitable for verification against the design and development inputs, and records must be maintained. Subclause 7.3.4 also states that design and development outputs shall contain or make reference to product acceptance criteria and shall ensure that those design outputs that are essential for its safe and proper use are identified.

`V.B-01 V.B-02 V.B-03 V.B-04 V.B-05 V.B-06`

FDA recommends that these plans and procedures include design processes, design requirements, and acceptance criteria for the security architecture of the device such that they holistically address the cybersecurity considerations for the device and the system in which the device operates. FDA recommends that all medical devices provide and enforce the security objectives in Section IV, above, but recognizes that implementations to address the security objectives may vary.

`V.B-07 V.B-08`

FDA recommends that premarket submissions include documentation on the security architecture. The objective in providing security architecture information in premarket submissions is to provide to FDA the security context and trust-boundaries of the medical device system in terms of the interfaces, interconnections, and interactions that the medical device system has with external entities. The details of these elements enable the identification of the parts of the medical device system in or through which incidents might occur. These details help to provide a sufficient understanding of the system such that FDA can evaluate adequacy of the architecture itself as it relates to safety and effectiveness.

`V.B-09`

Manufacturers should analyze the entire system to understand the full environment and context in which the device is expected to operate. The security architecture should include a consideration of system-level risks, including but not limited to risks related to the supply chain (e.g., to ensure the device remains free of malware, or vulnerabilities inherited from upstream dependencies such as third-party software, among others), design, production, and deployment (i.e., into a connected/networked environment).

`V.B-10 V.B-11`

FDA recommends that this architecture information take the form of “views,” and that these views be provided during premarket submissions to demonstrate safety and effectiveness.[^43] If the documentation identified in this section already exists in other risk management documentation, FDA does not expect manufacturers to separate out this information into new document(s); such documentation can be provided and the submission can reference the relevant sections.

`V.B-12 V.B-13`

#### V.B.1 Implementation of Security Controls

FDA considers the way in which a device addresses cybersecurity risks and the way in which the device responds when exposed to cybersecurity threats as functions of the device design. Effective cybersecurity relies upon security being “built in” to a device, and not “bolted on” after the device is designed. FDA recommends that device manufacturers’ design processes include design and development inputs for cybersecurity controls.[^44]

`V.B.1-01`

FDA recommends that these procedures include design requirements and acceptance criteria for the security features built into the device such that they holistically address the cybersecurity considerations for the device and the system in which the device operates.

`V.B.1-02`

Security controls allow manufacturers to achieve the security objectives outlined in Section IV and are an integral part of an SPDF. FDA recommends that an adequate set of security controls should include, but not necessarily be limited to, controls from the following categories:

`V.B.1-03`

- Authentication;  `V.B.1-04`
- Authorization;  `V.B.1-05`
- Cryptography;  `V.B.1-06`
- Code, Data, and Execution Integrity;  `V.B.1-07`
- Confidentiality;  `V.B.1-08`
- Event Detection and Logging;  `V.B.1-09`
- Resiliency and Recovery; and  `V.B.1-10`
- Updatability and Patchability.  `V.B.1-11`

Implementation of security controls should be applied across the system architecture using risk-based determinations associated with the subject connections and devices. Without adequate security controls across the medical device system—which include management, technical, and operational controls—there is no reasonable assurance of safety and effectiveness. Additionally, deficiencies in the design of selected security controls or the implementation of those controls can have dramatic impacts on a device’s ability to demonstrate or maintain its safety and effectiveness.

`V.B.1-12`

FDA recommends the requirements and acceptance criteria for each of the above categories be provided in premarket submissions to demonstrate safety and effectiveness. Manufacturers should submit documentation in their premarket submissions demonstrating that the security controls for the categories above, and further detailed in the recommendations in Appendix 1, have (1) been implemented, and (2) been tested in order to validate that they were effectively implemented. For more information on cybersecurity testing, see Section V.C, below.

`V.B.1-13 V.B.1-14`

Manufacturers may include the demonstration of security controls that are comparable or in addition to those described in Appendix 1 in their premarket submissions. If using alternate controls that are not described in this document, manufacturers should provide documentation and tracing of specific design features and security controls to the associated risks in order to demonstrate that they provide appropriate levels of safety and effectiveness. As cybersecurity design and development activities are established early in the development phase, FDA recommends that device manufacturers utilize the FDA Q-submission process to discuss design considerations for cybersecurity risk management throughout the device lifecycle with the agency.[^45] Additional information on premarket documentation recommendations for design and development are discussed in the Security Architecture Views section below.

`V.B.1-15 V.B.1-16 V.B.1-17`

#### V.B.2 Security Architecture Views

In addition to the design and development requirements,[^46] Subclause 8.5 of ISO 13485 requires that manufacturers establish and maintain procedures for implementing improvement, including corrective action and preventive action. The requirements under Subclause 8.4 for analyzing quality data to identify existing and potential causes of quality problems are used to determine the need for improvement under Subclause 8.5. FDA recommends that manufacturers develop and maintain security architecture view documentation as a part of the process for the design, development, and maintenance of the medical device system. If corrective and preventive actions are identified, these views can be used to help identify impacted functionality and solutions that address the risks.

`V.B.2-01 V.B.2-02`

FDA recommends that premarket submissions include the architecture views described in this section. These architecture views can contribute to the demonstration of safety and effectiveness in premarket submissions by illustrating how the controls to address cybersecurity risks have been applied to the medical device system.

`V.B.2-03`

FDA recommends providing, at minimum, the following types of views in premarket submissions:

`V.B.2-04`

- Global System View;  `V.B.2-05`
- Multi-Patient Harm View;  `V.B.2-06`
- Updateability/Patchability View; and  `V.B.2-07`
- Security Use Case View(s).  `V.B.2-08`

Documenting these views in premarket submissions should include both diagrams and explanatory text. These diagrams and explanatory text should contain sufficient details to permit an understanding of how the assets within the medical device system function holistically within the associated implementation details. For the security architecture views, manufacturers should follow the recommendations outlined in Appendix 2 when determining the level of detail to include in premarket submissions.

`V.B.2-09 V.B.2-10 V.B.2-11`

These security architecture views should:

`V.B.2-12`

- Identify security-relevant medical device system elements and their interfaces;  `V.B.2-13`
- Define security context, domains, boundaries, critical user roles, and external interfaces of the medical device system;  `V.B.2-14`
- Align the architecture with (a) the medical device system security objectives and requirements, (b) security design characteristics in order to address the identified threats; and  `V.B.2-15`
- Establish traceability of architecture elements to user and medical device system security requirements. Such traceability should exist throughout the cybersecurity risk management documentation.  `V.B.2-16 V.B.2-17`

If a particular view sufficiently captures the risks of another view identified above, we do not expect manufacturers to duplicate documentation. Similarly, if threat modeling documentation sufficiently captures the view, we do not expect manufacturers to duplicate documentation. Additionally, if one of the views listed above is not appropriate, manufacturers should instead provide an explanation for why the view is not included in the premarket submission.

`V.B.2-18`

##### V.B.2(a) Global System View

A global system view should describe the overall medical device system, including the device itself and all internal and external connections. For interconnected and networked devices, this view should identify all interconnected elements, including any software update infrastructure(s), healthcare facility network impacts, intermediary connections or devices, cloud connections, and patient home network impact.

`V.B.2.a-01 V.B.2.a-02`

##### V.B.2(b) Multi-Patient Harm View

FDA recommends that manufacturers address how their device(s) and the system(s) in which they operate defend against and/or respond to attacks with the potential to harm multiple patients in a multi-patient harm view. This view should include the information recommended in Appendix 2. These risks, once identified, may also need to be assessed differently in the accompanying cybersecurity risk assessment due to the different nature of the risk.

`V.B.2.b-01 V.B.2.b-02`

##### V.B.2(c) Updatability and Patchability View

With the need to provide timely, reliable updates to devices in order to address emerging cybersecurity risks throughout the TPLC of the device, FDA recommends manufacturers provide an updateability and patchability view. This view should describe the end-to-end process that permits software updates and patches to be provided (i.e., deployed) to the device, and should include detailed information as recommended in Appendix 2.

`V.B.2.c-01 V.B.2.c-02`

For example, if a device manufacturer intends to push software from a software update server to an in-clinic cardiac implant programmer, “end-to-end” means the path from the update server to the in-clinic programmer that programs the implanted device. The software update path will likely include traversing technology that the device manufacturer does not control, and therefore the device design should provide for the protection of the end-to-end path and take into account any additional cybersecurity risk created or posed by those non-manufacturer-controlled technologies.

`V.B.2.c-03`

##### V.B.2(d) Security Use Case Views

In addition to the views identified above, security use case views should also be provided. Security use cases should be included for all medical device system functionality through which a security compromise could impact the safety or effectiveness of the device. These security use cases should cover various operational states of elements in the medical device system (e.g., power on, standby, transition states) and assess clinical functionality states of the medical device system (e.g., programming, alarming, delivering therapy, send/receive data, reporting diagnostic results).

`V.B.2.d-01 V.B.2.d-02 V.B.2.d-03`

The number of security use cases that should be assessed will scale with the cybersecurity complexity and risk of the device. Each view should include detailed information as recommended in Appendix 2. For use cases identified that share the same security assessment, the associated diagrams and explanatory text can describe the multiple use cases covered by the view in lieu of providing duplicative information in multiple places. For example, programming commands and sending/receiving device data may share the same communication protocol and therefore may not exhibit differences between the security views for both scenarios, despite having different clinical risk assessments.

`V.B.2.d-04 V.B.2.d-05`

### V.C Cybersecurity Testing

As with other areas of product development, testing is used to demonstrate the effectiveness of design and development activities. While software development and cybersecurity are closely related disciplines, cybersecurity controls require testing beyond standard software verification and validation activities to demonstrate the effectiveness of the controls in a proper security context to therefore demonstrate that the device has a reasonable assurance of safety and effectiveness.

`V.C-01`

Under Subclause 7.3.6 of ISO 13485, a manufacturer must establish and maintain procedures for verifying the device design. Such verification shall confirm that the design output meets the design input requirements. Under Subclause 7.3.7, a manufacturer must establish and maintain procedures for validating its device design. FDA recommends verification and validation include sufficient testing performed by the manufacturer on the cybersecurity of the medical device system through which the manufacturer verifies and validates their inputs and outputs, as appropriate.

`V.C-02 V.C-03 V.C-04 V.C-05`

Security testing documentation and any associated reports or assessments should be submitted in the premarket submission. FDA recommends that the following types of testing, among others, be considered for inclusion in the submission:

`V.C-06 V.C-07`

- Security requirements;  `V.C-08`
  - Manufacturers should provide evidence that each design input requirement was implemented successfully.  `V.C-09`
  - Manufacturers should provide evidence of their boundary analysis and rationale for their boundary assumptions.  `V.C-10`
- Threat mitigation;  `V.C-11`
  - Manufacturers should provide details and evidence of testing that demonstrates effective risk control measures according to the threat models provided in the global system, multi-patient harm, updatability and patchability, and security use case views.  `V.C-12`
  - Manufacturers should ensure the adequacy of each cybersecurity risk control (e.g., security effectiveness in enforcing the specified security policy, performance for maximum traffic conditions, stability, and reliability, as appropriate).  `V.C-13`
- Vulnerability Testing (described in ANSI/ISA 62443-4-1); and  `V.C-14`
  - Manufacturers should provide details and evidence[^47] of the following testing and analyses:  `V.C-15`

> [^47]: For any testing tools or software used, the details provided may include, but may not be limited to, the name of the tool, version information as applicable, and any settings or configuration options for the tools used.  `fn47-01`

    - Abuse or misuse cases, malformed and unexpected inputs;  `V.C-16`
      - Robustness.  `V.C-17`
      - Fuzz testing.  `V.C-18`
    - Attack surface analysis;  `V.C-19`
    - Vulnerability chaining;  `V.C-20`
    - Closed box testing of known vulnerability scanning;  `V.C-21`
    - Software composition analysis of binary executable files; and  `V.C-22`
    - Static and dynamic code analysis, including testing for credentials that are “hardcoded,” default, easily guessed, and easily compromised.  `V.C-23`
- Penetration testing.  `V.C-24`
  - The testing should identify and characterize security-related issues via tests that focus on discovering and exploiting security vulnerabilities in the product. Penetration test reports should be provided and include the following elements:  `V.C-25 V.C-26`
    - Independence and technical expertise of testers;  `V.C-27`
    - Scope of testing;  `V.C-28`
    - Duration of testing;  `V.C-29`
    - Testing methods employed; and  `V.C-30`
    - Test results, findings, and observations.  `V.C-31`

Device manufacturers should indicate in the test reports by whom the testing was performed (e.g., independent internal testers, external testers) and what level of independence those responsible for testing devices have from the developers responsible for designing devices. In some cases, it may be necessary to use third parties to ensure an appropriate level of independence between the two groups, such that vulnerabilities or other issues revealed during testing are appropriately addressed. For any third-party test reports, manufacturers should provide the original third-party report. For all testing, manufacturers should provide their assessment of any findings including rationales for not implementing or deferring any findings to future releases.

`V.C-32 V.C-33 V.C-34`

As discussed in Sections V.A.2 and V.A.3 above, vulnerabilities and anomalies identified during testing should be assessed for their security impacts as part of the security risk management process. In non-security software testing, a benefit analysis of a discovered defect may lead to the conclusion that an anomaly does not need to be fixed, as its impact on medical device system functionality may be small or unlikely. Conversely, in security testing, the exploitability of an anomaly may necessitate that it is mitigated because of the greater, and different type of, harm that it could facilitate.

`V.C-35`

For issues that will be addressed in future releases (i.e., remediation deferred for a future software release because current risk was assessed to be acceptable), the premarket submission should contain plans for those releases. Such plans should include the vulnerabilities that future software releases will address, anticipated timelines for release, whether devices released in the interim will receive those updates, and how long it will take the update to reach the devices.

`V.C-36 V.C-37`

FDA recommends that cybersecurity testing should occur throughout the SPDF. Security testing early in development can ensure that security issues are addressed prior to impacting release timelines and can prevent the need to redesign or re-engineer the device. After release, cybersecurity testing should be performed at regular intervals commensurate with the risk (e.g., annually) to ensure that potential vulnerabilities are identified and able to be addressed prior to their ability to be exploited.

`V.C-38 V.C-39`

## VI Cybersecurity Transparency

Cybersecurity transparency is critical to ensure safe and effective use and integration of devices and systems.[^49] This transparency can be conveyed through both device labeling and the establishment of manufacturer vulnerability management plans. However, different types of users (e.g., manufacturers, servicers, patients) will have different abilities to take on a mitigation role, and the need for actions to ensure continued cybersecurity should be appropriate for the type of user. Manufacturers of cyber devices should consider the recommendations in this section as they “design, develop, and maintain processes and procedures to provide a reasonable assurance that the device and related systems are cybersecure . . .” (section 524B(b)(2) of the FD&C Act; see Section VII.C.2).

`VI-01 VI-02`

### VI.A Labeling Recommendations for Devices with Cybersecurity Risks

FDA regulates device labeling in several ways. For example, section 502(f) of the FD&C Act requires that labeling include adequate directions for use. Under section 502(a)(1) of the FD&C Act, a medical device is deemed misbranded if its labeling is false or misleading in any particular.

`VI.A-01`

For devices with cybersecurity risks, informing users of relevant security information may be an effective way to comply with labeling requirements relating to such risks. FDA also believes that informing users of security information through labeling may be an important part of design and development activities to help mitigate cybersecurity risks and help ensure the continued safety and effectiveness of the device. Therefore, when drafting labeling for inclusion in a premarket submission, a manufacturer should consider all applicable labeling requirements and how informing users through labeling may be an effective way to manage cybersecurity risks and/or to ensure the safe and effective use of the device. Any risks transferred to the user should be detailed and considered for inclusion as tasks during usability testing (e.g., human factors testing)[^50] to ensure that the type of user has the capability to take appropriate actions to manage those risks.

`VI.A-02 VI.A-03`

The recommendations below aim to communicate to users the relevant device security information that may enable their own ongoing security posture, thereby helping ensure a device remains safe and effective throughout its lifecycle. The depth of detail, the exact location in the labeling for specific types of information (e.g., operator’s manual, security implementation guide), and the method to provide this information should account for the intended user of the information. Instructions to manage cybersecurity risks should be understandable to the intended audience, which might include patients or caregivers with limited technical knowledge. The manufacturer may wish to employ methods to ensure certain information is available only to the user, and if it does so through an online portal, should ensure that users have up-to-date links that contain accurate information.[^51]

`VI.A-04 VI.A-05 VI.A-06`

- Device instructions and product specifications related to recommended cybersecurity controls appropriate for the intended use environment (e.g., anti-malware software, use of a firewall, password requirements).  `VI.A-07`
- Sufficiently detailed diagrams for users that allow recommended cybersecurity controls to be implemented.  `VI.A-08`
- A list of network ports and other interfaces that are expected to receive and/or send data. This list should include a description of port functionality and indicate whether the ports are incoming, outgoing, or both, along with approved destination end-points.  `VI.A-09 VI.A-10`
- Specific guidance to users regarding supporting infrastructure requirements so that the device can operate as intended (e.g., minimum networking requirements, supported encryption interfaces). Where appropriate, such guidance should include technical instructions to permit secure network deployment and servicing, and instructions for users on how to respond upon detection of a cybersecurity vulnerability or incident.  `VI.A-11 VI.A-12`
- An SBOM as specified in Section V.A.4 or in accordance with an industry accepted format to effectively manage their assets, to understand the potential impact of identified vulnerabilities to the medical device system, and to deploy countermeasures to maintain the device’s safety and effectiveness. Manufacturers should provide or make available SBOM information to users on a continuous basis. If an online portal is used, manufacturers should ensure that users have up-to-date links that contain accurate information. The SBOM should be in a machine-readable format.  `VI.A-13 VI.A-14 VI.A-15 VI.A-16`
- A description of systematic procedures for users to download version-identifiable manufacturer-authorized software and firmware, including a description of how users will know when software is available.  `VI.A-17`
- A description of how the design enables the device to respond when anomalous conditions are detected (i.e., security events). This should include notification to the user and logging of relevant information. Security event types could be configuration changes, network anomalies, login attempts, or anomalous traffic (e.g., send requests to unknown entities).  `VI.A-18 VI.A-19`
- A high-level description of the device features that protect critical functionality (e.g., backup mode, disabling ports/communications).  `VI.A-20`
- A description of backup and restore features and procedures to restore authenticated configurations.  `VI.A-21`
- A description of methods for retention and recovery of device configuration by an authenticated authorized user.  `VI.A-22`
- A description of the secure configuration of shipped devices, instructions for user-configurable changes, and identification of user-configurable changes that could increase security risk for the medical device system. Secure configurations may include end point protections such as anti-malware, firewall/firewall rules, allow lists, deny lists, security event parameters, logging parameters, and physical security detection, and resetting of credentials, among others.  `VI.A-23`
- Where appropriate for the intended use environment, a description of how forensic evidence is captured, including but not limited to any log files kept for a security event. Log file descriptions should include how, where, and in what format the log file is located, stored, recycled, archived, and how it could be consumed by automated analysis software (e.g., Intrusion Detection System (IDS) or Security Information and Event Management (SIEM)).  `VI.A-24 VI.A-25`
- Information, if known or anticipated, concerning device cybersecurity (including components) end of support and end of life. At the end of support, a manufacturer may no longer be able to reasonably provide security patches or software updates. If the device remains in service following the end of support, the manufacturer should have a pre-established and pre-communicated process for transferring the risks highlighting that the cybersecurity risks for end-users can be expected to increase over time.  `VI.A-26 VI.A-27`
- Information on securely decommissioning devices by sanitizing the product of sensitive, confidential, and proprietary data and software.  `VI.A-28`

### VI.B Cybersecurity Management Plans

Recognizing that cybersecurity risks evolve as technology evolves throughout a device’s TPLC, FDA recommends that manufacturers establish a plan for how they will identify and communicate to the relevant parties the vulnerabilities that are identified after releasing the device in accordance with Subclause 8.4 and Subclause 8.5 of ISO 13485, and 21 CFR Part 806, as appropriate. This plan can also support security risk management processes that are described throughout the QMSR and ISO 13485, as incorporated by reference in the QMSR.

`VI.B-01`

FDA recommends that manufacturers submit their cybersecurity management plans as part of their premarket submissions so that FDA can assess whether the manufacturer has sufficiently addressed how to maintain the safety and effectiveness of the device after marketing authorization is achieved. For cyber devices, “a plan to monitor, identify, and address, as appropriate, in a reasonable time, postmarket cybersecurity vulnerabilities and exploits, including coordinated vulnerability disclosure and related procedures” is required (see section 524B(b)(1) of the FD&C Act and Section VII.C.1 of this guidance).

`VI.B-02 VI.B-03`

Cybersecurity management plans should include the following elements:

`VI.B-04`

- Personnel responsible;  `VI.B-05`
- Sources, methods, and frequency for monitoring and identifying vulnerabilities (e.g., researchers, NIST national vulnerability database (NIST NVD), third-party software manufacturers);  `VI.B-06`
- Identify and address vulnerabilities identified in CISA’s Known Exploited Vulnerabilities Catalog;  `VI.B-07`
- Periodic security testing;  `VI.B-08`
- Timeline to develop and release patches;  `VI.B-09`
- Update processes;  `VI.B-10`
- Patching capability (i.e., rate at which update can be delivered to devices);  `VI.B-11`
- Description of their coordinated vulnerability disclosure process; and  `VI.B-12`
- Description of how the manufacturer intends to communicate forthcoming remediations, patches, and updates to customers.  `VI.B-13`

## VII Cyber Devices

This section identifies the cybersecurity information FDA considers to generally be necessary to support obligations under section 524B of the FD&C Act for cyber devices. This section provides recommendations specifically for cyber devices. Manufacturers of cyber devices should also consider the recommendations throughout this guidance to help meet their obligations under section 524B.

`VII-01`

### VII.A Who is Required to Comply with Section 524B of the FD&C Act

Under section 524B(a) of the FD&C Act, a person, including a manufacturer,[^53] who submits a premarket application or submission under any of the following pathways—510(k),[^54] PMA,[^55] PDP, De Novo, or HDE[^56]—for a device that meets the definition of a “cyber device,” as defined in section 524B(c), is required to include such information as FDA may require to ensure that the cyber device meets the cybersecurity requirements under section 524B(b).

`VII.A-01`


> [^53]: Section 524B(a) of the FD&C Act places obligations on the “person” who submits a specific type of device marketing application. Section 524B(b) of the FD&C Act places obligations on a “sponsor.” For the purposes of this guidance, we assume that the manufacturer is the entity submitting the application and use the term accordingly throughout the guidance in lieu of the term “person” or “sponsor.” However, if another person submits the application or submission enumerated under section 524B(a) of the FD&C Act to the Agency, that person should follow the guidance for manufacturers herein. Whatever person submits the application for a cyber device is subject to the requirements of section 524B.  `fn53-01`

### VII.C Documentation Recommendations to Comply with Section 524B of the FD&C Act

For applicable premarket submission types, manufacturers must provide documentation to comply with the requirements under section 524B of the FD&C Act. Recommendations regarding the documentation to support each of the requirements are discussed in the sections below.

`VII.C-01`

#### VII.C.1 Plans and Procedures (Section 524B(b)(1))

Section 524B(b)(1) of the FD&C Act requires manufacturers of cyber devices to submit to FDA “a plan to monitor, identify, and address, as appropriate, in a reasonable time, postmarket cybersecurity vulnerabilities and exploits, including coordinated vulnerability disclosure and related procedures” in their premarket submissions. We recommend that the plan contain the information recommended for the Cybersecurity Management Plan described in Section VI.B. In particular, such a plan should address the items discussed below.

`VII.C.1-01 VII.C.1-02 VII.C.1-03`

First, FDA considers that coordinated vulnerability disclosure (CVD) and related procedures, as required in section 524B(b)(1) of the FD&C Act, could include:

`VII.C.1-04`

- Coordinated disclosure of vulnerabilities and exploits identified by external entities (including third-party software suppliers and researchers);  `VII.C.1-05`
- Disclosure of vulnerabilities and exploits identified by the manufacturer of cyber devices; and  `VII.C.1-06`
- Manufacturer procedures to carry out disclosures of the vulnerabilities and exploits, as identified above.[^62]  `VII.C.1-07`

> [^62]: For the purposes of this guidance, manufacturer procedures to carry out disclosures of the vulnerabilities and exploits may include procedures to inform device users, customers, patients, and other relevant healthcare parties.  `fn62-01`

Second, plans required by section 524B(b)(1) of the FD&C Act should also describe the timeline, with associated justifications, to develop and release required updates and patches:

`VII.C.1-08`

- Section 524B(b)(2)(A) of the FD&C Act requires manufacturers of cyber devices to make available updates and patches[^63] to the device and related systems[^64] for known unacceptable vulnerabilities, with these updates and patches made available on a reasonably justified regular cycle.[^65]  `VII.C.1-09`

> [^65]: The justification for the regular cycle should typically be included in the cybersecurity management plan. The length of the regular cycle may vary depending on numerous factors for the particular device. One of the primary factors that may influence the length of the cycle is risk. For example, an interconnected thermometer whose functionality is limited to taking and reporting patient temperature may have lower risk of harm if exploited than an interconnected surgery robot, whose risk of harm may be significantly higher. At the same time, exploitation of a seemingly lower-risk device may provide opportunities to affect other devices within the environment of use, leading to significantly greater risk of harm if these other devices or the larger environment are exploited or disrupted. Manufacturers should fully consider the risks to and from their devices, within the larger context(s) of the environment(s) in which they will be intended to operate, and design and deploy regular update cycles that provide a reasonable assurance of cybersecurity.  `fn65-01 fn65-02`

  - A “known unacceptable vulnerability” in section 524B(b)(2)(A) contrasts with a “critical vulnerability that could cause uncontrolled risks” in section 524B(b)(2)(B). A known unacceptable vulnerability could include a vulnerability that could not cause uncontrolled risks; a vulnerability that is not currently known to cause uncontrolled risks; or a vulnerability that could present controlled risk, as described in FDA’s Postmarket Cybersecurity Guidance. Updates and/or patches to address these vulnerabilities may be intended to maintain the supportability of software. Generally, software should be regularly updated to maintain the supportability of the software. For examples of vulnerabilities associated with controlled risk, see the Postmarket Cybersecurity Guidance. Updates and patches to address these types of vulnerabilities are not to reduce uncontrolled risk, and therefore not to reduce a risk to health or to correct a violation of the FD&C Act. See below for more information on section 524B(b)(2)(B) of the FD&C Act.  `VII.C.1-10`
- Section 524B(b)(2)(B) of the FD&C Act requires manufacturers of cyber devices to make available updates and patches to the device and related systems to address as soon as possible out of cycle,[^66] critical vulnerabilities that could cause uncontrolled risks.  `VII.C.1-11`

> [^66]: For example, a manufacturer may make updates outside of the planned reasonably justified regular cycle to remediate an uncontrolled risk.  `fn66-01`

Third, we recommend that manufacturers of cyber devices anticipate and make appropriate updates to these plans,[^67] as well as to the processes and procedures discussed in Section VII.C.2 below,[^68] as new information becomes available, such as when new risks, threats, vulnerabilities, assets, or adverse impacts are discovered throughout the total product lifecycle. To support such efforts, manufacturers should also create or update appropriate documentation (e.g., threat modeling, cybersecurity risk assessment) and maintain it throughout the device lifecycle. Doing so will allow manufacturers to quickly identify vulnerability impacts once a device is released and could also help satisfy the patching requirements of section 524B(b)(2)(A)-(B) of the FD&C Act.

`VII.C.1-12 VII.C.1-13`

The required plans,[^69] as well as the processes and procedures discussed in Section VII.C.2 below,[^70] also should, as appropriate, account for any differences in the risk management for fielded devices (e.g., differences between marketed devices and devices no longer marketed but still in use). For example, if an update is not applied automatically for all fielded devices, then there will likely be different risk profiles for the differing software configurations of the device. Vulnerabilities should be assessed for any differing impacts for all fielded versions to ensure patient risks are being accurately assessed.

`VII.C.1-14 VII.C.1-15`

#### VII.C.2 Design, Develop, and Maintain Processes and Procedures to Provide a Reasonable Assurance of Cybersecurity (Section 524B(b)(2))

Manufacturers of cyber devices must “design, develop, and maintain processes and procedures to provide a reasonable assurance that the device and related systems are cybersecure . . .” (section 524B(b)(2) of the FD&C Act). FDA considers related systems to include, among other things, manufacturer-controlled elements, such as other devices, software that performs “other functions” as described in FDA’s Guidance “Multiple Function Device Products: Policy and Considerations,” software/firmware update servers, and connections to healthcare facility networks. In the design, development and maintenance of a cyber device, manufacturers should consider the cybersecurity risks of related systems to the cyber device and implement appropriate security controls to mitigate those risks. The documentation recommendations identified in this guidance and summarized in Appendix 4 should be considered and used to demonstrate reasonable assurance that the device and related systems are cybersecure as required by section 524B(b)(2).

`VII.C.2-01 VII.C.2-02 VII.C.2-03`

#### VII.C.3 Software Bill of Materials (SBOM) (Section 524B(b)(3))

Section 524B(b)(3) of the FD&C Act requires manufacturers of cyber devices to provide an SBOM, including commercial, open-source, and off-the-shelf software components. To assist with complying with this requirement, we recommend that a cyber device provide SBOMs that contain the information recommended in Section V.A.4.b.

`VII.C.3-01 VII.C.3-02`

### VII.D Modifications

As previously stated, the requirements under section 524B of the FD&C Act apply to a manufacturer who submits an application or submission under any of the following pathways— 510(k), PMA, PDP, De Novo or HDE—for a device that meets the definition of a cyber device. Therefore, a manufacturer required to submit an application or submission under one of the enumerated pathways for a device modification would also need to comply with the requirements in section 524B of the FD&C Act.[^71] In keeping with least burdensome principles,[^72] the information we recommend that manufacturers of cyber devices provide will generally differ based on the type of change and whether such change impacts the cybersecurity of the device. Overall, we recommend that manufacturers use the recommendations below to determine the information FDA recommends manufacturers of cyber devices provide to demonstrate they have met the new requirements under section 524B when submitting a premarket submission for a device modification.

`VII.D-01`

#### VII.D.2 Changes Unlikely to Impact Cybersecurity

For these types of changes, FDA recommends that manufacturers of cyber devices provide the following information to meet their premarket submission requirements in section 524B of the FD&C Act:

`VII.D.2-01`

  - If not previously provided, manufacturers must provide a plan as described in section 524B(b)(1) of the FD&C Act; we recommend that it contain the information as described in Section VII.C.1, above.  `VII.D.2-02 VII.D.2-03`
  - If a plan described in Section VII.C.1, above, was previously provided, the manufacturer should provide a reference to the prior submission and a summary of any changes to the plan.  `VII.D.2-04`
  - Instead of the full documentation described as required or recommended in Section VII.C.2, above, manufacturers may provide the following information:  `VII.D.2-05`
    - Description of whether there are currently any “critical vulnerabilities that could cause uncontrolled risks.”[^73]  `VII.D.2-06`

> [^73]: Section 524B(b)(2)(B) of the FD&C Act requires manufacturers to make available postmarket updates and patches to the cyber device and related systems to address, as soon as possible out of cycle, critical vulnerabilities that could cause uncontrolled risks, among other requirements. See Section VII.C.1 for more information on “critical vulnerabilities that could cause uncontrolled risks.”  `fn73-01`

    - Description of whether any vulnerabilities with uncontrolled risk were remediated in the device since the last authorization. If so, manufacturers should describe how remediation was performed following the recommendations in FDA’s Postmarket Cybersecurity Guidance.  `VII.D.2-07 VII.D.2-08`
  - Section 524B(b)(3) of the FD&C Act requires manufacturers of cyber devices to provide an SBOM, including commercial, open-source, and off-the-shelf software components. To assist with complying with this requirement, we recommend that a manufacturer of a cyber device provide an SBOM that contains the information recommended in Section V.A.4.b above.  `VII.D.2-09 VII.D.2-10`

## Appendix 1. Security Control Categories and Associated Recommendations

### Authentication

As part of normal operations within a secure system, devices should verify the authenticity of information from external entities, as well as prove the authenticity of information that they generate. A medical device system that appropriately accounts for authenticity can evaluate and ensure authenticity for:

`App1.A-01`

When choosing an authentication scheme, manufacturers should keep in mind the following generally applicable characteristics of different types of schemes:

`App1.A-02`

- Implicit authentication schemes, based solely on non-cryptographic interfaces, handshakes, and/or protocols, are inherently weak because, once they are reverse-engineered, an unauthorized user can easily emulate the correct behavior and appear to be authorized.  `App1.A-03`
- Cryptographic authentication protocols are generally superior, but they need careful design choices and implementation practices to achieve their full strength.  `App1.A-04`

In addition, these schemes are still limited by the confidentiality of the cryptographic keys needed to interact with the scheme, and by the integrity of the devices that hold or otherwise leverage those keys. For more information on cryptography, see Appendix 1 subsection C., below. Therefore, for device operations where non-authenticated behavior could lead to harm, devices should implement additional, non-routine signals of intent based on physical actions, such as a momentary switch, to authorize the command/session.

`App1.A-05`

- Use cryptographically strong[^76] authentication, where the authentication functionality resides on the device, to authenticate personnel, messages, commands updates, and as applicable, all other communication pathways. Hardware-based security solutions should be considered and employed when possible;  `App1.A-06 App1.A-07`
- Authenticate external connections at a frequency commensurate with the associated risks. For example, if a device connects to an offsite server, then the device and the server should mutually authenticate each session and limit the duration of the session, even if the connection is initiated over one or more existing trusted channels;  `App1.A-08 App1.A-09`
- Use appropriate user authentication (e.g., multi-factor authentication to permit privileged device access to system administrators, service technicians, or maintenance personnel, among others, as needed);  `App1.A-10`
- Require authentication, and authorization in certain instances, before permitting software or firmware updates, including those updates affecting the operating system, applications, and anti-malware functionality;  `App1.A-11`
- Strengthen password protections. Do not use passwords that are hardcoded, default, easily guessed, or easily compromised (e.g., passwords that are the same for each device; unchangeable; can persist as default; difficult to change; and/or vulnerable to public disclosure);  `App1.A-12 App1.A-13`
- Implement anti-replay measures in critical communications such as potentially harmful commands. This can be accomplished with the use of several methods including the use of cryptographic nonces (an arbitrary number used only once in a cryptographic communication);  `App1.A-14`
- Provide mechanisms for verifying the authenticity of information originating from the device, such as telemetry. This is especially important for data that, if spoofed or otherwise modified, could result in patient harm, such as the link between a clinician programmer or monitoring device and an implanted device like a pacemaker, defibrillator, or neurostimulator; or the link between a continuous glucose monitor system and an automated insulin pump;  `App1.A-15`
- Do not rely on cyclic redundancy checks (CRCs) as security controls. CRCs do not provide integrity or authentication protections in a security environment. While CRCs are an error detecting code and provide integrity protection against environmental factors (e.g., noise or EMC), they do not provide protections against an intentional or malicious actor; and  `App1.A-16`
- Consider how the device and/or system should respond in event of authentication failure(s).  `App1.A-17`

### Authorization

Within an adequately designed authorization scheme, the principle of least privileges[^77] should be applied to users, system functions, and others, to only allow those entities the levels of system access necessary to perform a specific function.

`App1.B-01`

For example, in a situation in which a malicious actor has gained access to a credential associated with patient privileges, that malicious actor should not be able to access device resources or functionality reserved for the manufacturer or for the healthcare provider, such as device maintenance routines or the ability to change medication dosage amounts.

`App1.B-02`

- Limit authorized access to devices through the authentication of users (e.g., user ID and password, smartcard, biometric, certificates, or other appropriate authentication method);  `App1.B-03`
- Use automatic timed methods to terminate sessions within the medical device system where appropriate for the use environment;  `App1.B-04`
- Employ an authorization model that incorporates the principle of least privileges by differentiating privileges based on the user role (e.g., caregiver, patient, healthcare provider, system administrator) or device functions; and  `App1.B-05`
- Design devices to “deny by default” (i.e., that which is not expressly permitted by a device is denied by default). For example, the device should generally reject all unauthorized connections (e.g., incoming TCP, USB, Bluetooth, serial connections). Ignoring requests is one form of denying authorization.  `App1.B-06 App1.B-07`

### Cryptography

Cryptographic algorithms and protocols are recommended to be implemented to achieve the secure by design objectives outlined in Section IV. While high-quality, standardized cryptographic algorithms and protocols are readily available, several commercial products that include cryptographic protections have been shown to have exploitable vulnerabilities due to improper configurations and/or implementations.

`App1.C-01`

- Select industry-standard cryptographic algorithms and protocols, and select appropriate key generation, distribution, management and protection, as well as robust nonce mechanisms.  `App1.C-02`
- Use current NIST recommended standards for cryptography (e.g., FIPS 140-3[^79]) or equivalent-strength cryptographic protection that are expected to be considered cryptographically strong throughout the service life of the device.  `App1.C-03`
  - Manufacturers should not implement cryptographic algorithms that have been deprecated or disallowed in applicable standards or best practices (e.g., NIST SP 800-131A, Transitioning the Use of Cryptographic Algorithms and Key Lengths). Implementation of algorithms with a status of “legacy use” should be discussed with FDA during a pre-submission meeting.  `App1.C-04 App1.C-05`
- Design a system architecture and implement security controls to prevent a situation where the full compromise of any single device can result in the ability to reveal keys for other devices.  `App1.C-06`
  - For example, avoid using master-keys stored on device, or key derivation algorithms based solely on device identifiers or other readily discoverable information.  `App1.C-07`
  - For example, avoid using device serial numbers as keys or as part of keys. Device serial numbers may be disclosed by patients seeking additional information on their device or might be disclosed during a device recall to identify affected products and should be avoided as part of the key generation process (e.g., public-key cryptography can be employed to help meet this objective).  `App1.C-08 App1.C-09`
- Implement cryptographic protocols that permit negotiated parameters/versions such that the most recent, secure configurations are used, unless otherwise necessary.  `App1.C-10`
- Do not allow downgrades, or version rollbacks, unless absolutely necessary for safety reasons, and log and document the event. Downgrades can allow attackers to exploit prior, less protected versions and should be avoided.  `App1.C-11 App1.C-12`

### Code, Data, and Execution Integrity

  - Hardware-based security solutions should be considered and employed when possible;  `App1.D-01`
  - Authenticate firmware and software. Verify authentication tags (e.g., signatures, message authentication codes (MACs)) of software/firmware content, version numbers, and other metadata. The version numbers intended to be installed should themselves be signed or have MACs. Devices should be electronically and visibly identifiable (e.g., Unique device identifier (UDI),[^80] model number, serial number);  `App1.D-02 App1.D-03 App1.D-04 App1.D-05`
  - Allow installation of cryptographically authenticated firmware and software updates, and do not allow installation where such cryptographic authentication either is absent or fails. Use cryptographically signed updates to help prevent any unauthorized reductions in the level of protection (downgrade or rollback attacks) by ensuring that the new update represents an authorized version change;  `App1.D-06 App1.D-07`
    - One possible approach for authorized downgrades would be to sign new metadata for downgrade requests which, by definition, only happen in exceptional circumstances.  `App1.D-08`
  - Ensure that the authenticity of software, firmware, and configuration are validated prior to execution, e.g., “allow-listing”[^81] based on digital signatures;  `App1.D-09`
  - Disable or otherwise restrict unauthorized access to all test and debug ports (e.g., JTAG, UART) prior to delivering products; and  `App1.D-10`
  - Employ tamper evident seals on device enclosures and their sensitive communication ports to help verify physical integrity.  `App1.D-11`
  - Verify the integrity of all incoming data, ensuring that it is not modified in transit or at rest. Cryptographic authentication schemes verify data integrity, but do not verify data validity. Therefore, the integrity of all incoming data should be verified to ensure that it is not modified in transit or at rest;  `App1.D-12 App1.D-13`
  - Validate that all data originating from external sources is well-formed and compliant with the expected protocol or specification. Additionally, as appropriate, validate data ranges to ensure they fall within safe limits; and  `App1.D-14`
  - Protect the integrity of data necessary to ensure the safety and effectiveness of the device, e.g., critical configuration settings such as energy output.  `App1.D-15`
  - Use industry-accepted best practices to maintain and verify integrity of code while it is being executed on the device. For example, Host-based Intrusion Detection/Prevention Systems (HIDS/HIPS) can be used to accomplish this goal; and  `App1.D-16`
  - Carefully design and review all code that handles the parsing of external data using automated (e.g., static and dynamic analyses) and manual (i.e., code review) methods.  `App1.D-17`

### Confidentiality

Manufacturers should ensure support for the confidentiality[^82] of any/all data whose disclosure could lead to patient harm (e.g., through the unauthorized use of otherwise valid credentials, lack of encryption). Loss of confidentiality of credentials could be used by a threat-actor to effect multi-patient harm. Lack of encryption to protect sensitive information and or data at rest and in transit can expose this information to misuse that can lead to patient harm. For example, confidentiality is required in the handling and storage of cryptographic keys used for authentication because disclosure could lead to unauthorized use/abuse of device functionality.

`App1.E-01 App1.E-02`

The proper implementation of authorization and authentication schemes as described in Sections A and B of this appendix will generally ensure confidentiality. However, manufacturers should evaluate and assess whether this is the case during their threat modeling and other risk management activities and make any appropriate changes to their medical device systems to ensure appropriate confidentiality controls are in place.

`App1.E-03`

### Event Detection and Logging

Event detection and logging are critical capabilities that should be present in a device and the larger system in which it operates in order to ensure that suspected and successful attempts to compromise a medical device may be identified and tracked. These event detection capabilities and logs should include storage capabilities, if possible, so that forensic discovery may later be performed.

`App1.F-01 App1.F-02`

While many of the following recommendations are tailored for workstations, the concepts presented below also apply to embedded computing devices. Manufacturers should consider the following for all devices:

`App1.F-03`

- Implement design features that allow for security compromises and suspected compromise attempts to be detected, recognized, logged, timed, and acted upon during normal use. Acting upon security events should consider the benefit/risk assessment in accordance with AAMI TIR57 or ANSI/AAMI SW96 in determining whether it is appropriate to affect standard device functionality during a security event.  `App1.F-04 App1.F-05`
- Ensure the design enables forensic evidence capture.[^83] The design should include mechanisms to securely create and store log files off the device to track security events. Documentation should include how and where log files are located, stored, recycled, archived, and how they could be consumed by automated analysis software (e.g., IDS). Examples of security events include, but are not limited to, configuration changes, network anomalies, login attempts, and anomalous traffic (e.g., sending requests to unknown entities).  `App1.F-06 App1.F-07 App1.F-08`
- Design devices such that the potential impact of vulnerabilities is limited by specifying a secure configuration. Secure configurations may include endpoint protections, such as anti-malware, firewall/firewall rules, allow-listing, defining security event parameters, logging parameters, physical security detection, and/or HIDS/HIPS.  `App1.F-09`
- Design devices such that they may integrate and/or leverage antivirus/anti-malware protection capabilities. These capabilities may vary depending on the type of device and the software and hardware components it contains:  `App1.F-10`
    - Antivirus/anti-malware is recommended on the device. Manufacturers are recommended to qualify multiple options to support user preferences for different options, especially if the device is used in healthcare facility environments.  `App1.F-11 App1.F-12`
    - Antivirus/anti-malware may be recommended based on the environment and associated risks of the device. Different operating systems will likely follow a case-by-case determination based on network exposure and risk.  `App1.F-13`
    - Antivirus/malware detection/protection software is generally not needed unless a particular risk or threat is identified that would not be addressed by other expected security controls.  `App1.F-14`
- Design devices to enable software configuration management and permit tracking and control of software changes to be electronically obtainable (i.e., machine readable) by authorized users.  `App1.F-15`
- Design devices to facilitate the performance of variant analyses such that the same vulnerabilities can be identified across device models and product lines.  `App1.F-16`
- Design devices to notify users when malfunctions or anomalous device behavior, including those potentially related to a cybersecurity breach, are detected.  `App1.F-17`
- Consider designing devices such that they are able to produce an SBOM in a machine readable format.  `App1.F-18`

### Resiliency and Recovery

Devices should be designed to be resilient to possible cyber incident scenarios (also known as “cyber-resiliency”) and maintain availability. Cyber-resiliency capabilities are important for medical devices because they provide a safety margin against unknown future vulnerabilities.

`App1.G-01`

- Implement features that protect critical functionality and data, even when the device has been partially compromised. For example, process isolation, virtualization techniques, and hardware-backed trusted execution environments all provide mechanisms to potentially contain the impact of a successful exploitation of a device.  `App1.G-02`
- Design devices to provide methods for retention and recovery of trusted default device configuration by an authenticated, authorized user.  `App1.G-03`
- Design devices to specify the level of resilience, or independent ability to function, that any component of the medical device system possesses when its communication capabilities with the rest of the medical device system are disrupted, including disruption of significant duration.  `App1.G-04`
- Design devices to be resilient to possible cyber incident scenarios such as network outages, Denial of Service, excessive bandwidth usage by other products, disrupted quality of service (QoS), and/or excessive jitter (i.e., a variation in the delay of received packets).  `App1.G-05`
- Design devices to be resilient to possible noise items (e.g., scanning).  `App1.G-06`

### Firmware and Software Updates

Devices should be capable of being updated in a secure and timely manner to maintain safety and effectiveness throughout the product’s lifecycle. Despite best efforts, undiscovered, exploitable vulnerabilities may exist in devices after they are marketed. This is especially true over the device’s service life, as threats evolve over time and exploit methods change, and become more sophisticated.

`App1.H-01`

FDA recommends that manufacturers should not only build in the ability for devices to be updated, but that manufacturers also plan for the rapid testing, evaluation, and patching of devices deployed in the field. The following recommendations can help to achieve this:

`App1.H-02`

- Design devices to anticipate the need for software and firmware patches and updates to address future cybersecurity vulnerabilities. This will likely necessitate the need for additional storage space and processing resources.  `App1.H-03`
- Consider update process reliability and how update process works in event of communication interruption or failure. This should include both considerations for hardware impacts (timing specifics of interruptions) and which phase of the update process the interruption or failure occurs.  `App1.H-04 App1.H-05`
- Consider cybersecurity patches and updates that are independent of regular feature update cycles.  `App1.H-06`
- Implement processes, technologies, security architectures, and exercises to facilitate the rapid verification, validation, and distribution of patches and updates.  `App1.H-07`
- Preserve and maintain full build environments and virtual machines, regression test suites, engineering development kits, emulators, debuggers, and other related tools that were used to develop and test the original product to ensure updates and patches may be applied safely and in a timely manner.  `App1.H-08`
- Maintain necessary third-party licenses throughout the supported lifespan of the device. Develop contingency plans for the possibility that a third-party company goes out of business or stops supporting a licensed product. Modular designs should be considered such that third-party solutions could be readily replaced.  `App1.H-09 App1.H-10 App1.H-11`
- Implement a secure process and mechanism for providing validated software updates and patches for users.  `App1.H-12`

## Appendix 2. Submission Documentation for Security Architecture Flows

In premarket submissions, FDA recommends that manufacturers provide detailed information for the views identified in Section V.B.2. Methods for providing the views and the recommendations for the level of detail to provide are discussed in the sections below. In addition to diagrams and explanatory text, call-flow views can be provided to convey some of the information details expected to be addressed in the architecture views.

`App2-01`

### Diagrams

FDA recommends that manufacturers provide diagrams to help describe the medical device system architecture, interfaces, communication protocols, threats, and cybersecurity controls used throughout the system. Different diagramming methods can be used to describe the architecture, including data flow diagrams, state diagrams, swim-lane diagrams, and call-flow diagrams, among others. Architecture views should include diagram(s) with explanatory text that describes the sequence of process or protocol steps in explicit detail for an associated use case.

`App2.A-01 App2.A-02`

Architecture views should provide specific protocol details of the communication pathways between parts of the medical device system, to include authentication or authorization procedures and session management techniques. These views should be sufficiently detailed such that engineers and reviewers should be able to logically and easily follow data, code, and commands from any asset (e.g., a manufacturer server) to any other associated asset (e.g., a medical device), while possibly crossing intermediate assets (e.g., application). The diagrams may also include items from the information details identified below for the architecture views identified in Section V.B.2 if the information is better represented or conveyed through a diagram than explanatory text alone.

`App2.A-03 App2.A-04`

### Information Details for an Architecture View

For each view described in Section V.B.2, manufacturers should provide a system-level description and analysis inclusive of end-to-end security analyses of all the communications in the medical device system regardless of intended use. This should include detailed diagrams and traces for all communication paths as described below. Security-relevant analysis requires the ability to construct and follow a detailed trace for important communication paths, which describes how data, code, and commands are protected between any two assets in the medical device system. This analysis can also help identify the software that should be included in the SBOM for each device.

`App2.B-01 App2.B-02`

FDA recommends that security architecture views should consider the following examples of information for inclusion:

`App2.B-03`

- Detailed diagrams and supporting explanatory text that identify all medical device system assets, including but not limited to:  `App2.B-04`
  - Device hardware itself (including assessments for any commercial platforms);  `App2.B-05`
  - Applications, hardware, and/or other supporting assets that directly interact with the targeted device, such as configuration, installation/upgrade, and data transfer applications;  `App2.B-06`
  - Healthcare facility-operated assets;  `App2.B-07`
  - Communications/networking assets; and  `App2.B-08`
  - Manufacturer-controlled assets, including any servers that interact with external entities (e.g., a server that collects and redistributes device data, or a firmware update server).  `App2.B-09`
- For every communication path that exists between any two assets in the security use case view (and/or explanatory text), including indirect connections when there is at least one intermediate asset (e.g., an app), the following details should be provided:  `App2.B-10`
  - A list of the communication interfaces and paths, including communication paths (e.g., between two assets through an intermediary), and any unused interfaces;  `App2.B-11`
  - An indication of whether the path is used for data, code, and/or commands, and type of data/information/code being transferred;  `App2.B-12`
  - Protocol name(s), version number(s), and ports/channels/frequencies;  `App2.B-13`
  - Detailed descriptions of the primary and all available functionality for each medical device system asset, including assessment of any functionality that is built in but not currently used or enabled (e.g., dormant application functionality or ports), including assurance that this functionality cannot be activated and/or misused;  `App2.B-14`
  - Access control models or features (if any) for every asset (such as privileges, user accounts/groups, passwords);  `App2.B-15`
  - Users’ roles and levels of responsibility if they interact with the assets and communication channels;  `App2.B-16`
  - Any “handoff” sequences from one communication path to another (e.g., from asset to asset, network to network, or Bluetooth to Wi-Fi), and how the data, code, and/or commands are secured/protected during handoff (i.e., how is their integrity/authenticity ensured);  `App2.B-17`
  - Explanations of intended behavior in unusual/erroneous/unexpected circumstances (e.g., termination of a connection in the middle of a data transfer);  `App2.B-18`
  - Authentication mechanism (if any), including the algorithm name/version (if available), “strength” indicators (e.g., key bit length, number of computational rounds) and mode of operation (if applicable);  `App2.B-19`
  - Descriptions of the cryptographic method used and the type and level of cryptographic key usage and their style of use throughout the medical device system (e.g., one-time use, key length, the standard employed, symmetric or otherwise). Descriptions should also include details of cryptographic protection for firmware and software updates;  `App2.B-20 App2.B-21`
  - Detailed analyses by cryptography experts if a cryptography algorithm is proprietary, or a proprietary modification of a standard algorithm;  `App2.B-22`
  - For each authenticator created, a list of where it is verified, and how verification credentials (e.g., certificates, asymmetric keys, or shared keys) are distributed to both endpoints;  `App2.B-23`
  - A precise, detailed list of how each type of credential (e.g., password, key) is generated, stored, configured, transferred, and maintained, including both manufacturer- and healthcare facility-controlled assets (e.g., key management and public key infrastructure (PKI));  `App2.B-24`
  - Identity management[^84] (if any), including how identities are managed/transferred and configured (e.g., from manufacturer to programmer and from programmer to device);  `App2.B-25`
  - If communication sessions are used or supported, a detailed explanation of how sessions are established, maintained, and broken down, including but not limited to assurances of security properties such as uniqueness, unpredictability, time-stamping, and verification of session identifiers;  `App2.B-26`
  - Include any security configuration settings and their default values;  `App2.B-27`
  - Precise links between diagram elements (or explanatory text), associated hazards and controls, and testing;  `App2.B-28`
  - Explanations or links to the evidence that may be used to justify security claims and any assumptions; and  `App2.B-29`
  - Traceability of the asset to the SBOM component described in Section V.B.2, above, for proprietary and third-party code, when appropriate.  `App2.B-30`

## Appendix 3. Submission Documentation for Investigational Device Exemptions

Under 21 CFR 812.25, manufacturers must provide an investigational plan as a part of their IDE application. For investigational devices within the scope of this guidance, FDA recommends that this investigational plan include information on the cybersecurity of the subject device.

`App3-01 App3-02`

Specifically, FDA recommends the following documentation be included as part of IDE applications:

`App3-03`

- Inclusion of cybersecurity risks as part of informed consent form (21 CFR 50.25(a)(2) and 21 CFR 812.25(g));  `App3-04`
- Global, multi-patient and updateability/patchability views (21 CFR 812.25(c), (d));  `App3-05`
- Security use case views for functionality with safety risks (e.g., implant programming) (21 CFR 812.25(c), (d));  `App3-06`
- Software Bill of Materials (21 CFR 812.25(c), (d)); and  `App3-07`
- General labeling – connectivity and associated general cybersecurity risks, updateability/process (21 CFR 812.25(f)).  `App3-08`

## Appendix 4. General Premarket Submission Documentation Elements and Scaling with Risk

As stated in Section IV.D and throughout the guidance, device cybersecurity design and documentation are expected to scale with the cybersecurity risk of that device. While documentation breadth is expected to scale, each type of documentation identified throughout the guidance is recommended for all premarket submissions for devices with potential cybersecurity risks. As mentioned previously, the submission documentation recommendations in this guidance are intended to help manufacturers meet their obligations for cyber devices under section 524B of the FD&C Act.

`App4-01`

Table 1 below summarizes the specific documentation elements identified throughout the guidance for premarket submissions, the associated sections of the guidance for the document, and whether the documentation is recommended for IDE submissions. While documentation elements are identified for the security risk management report, manufacturers can provide the documentation elements in a way that is consistent with their existing documentation processes.

`App4-02`


## Footnotes carrying statements whose calling paragraph is not otherwise normative

- [^20] Manufacturers may not be able to account for all potential environments of use, but should consider the range of use environments and ensure the risks are identified and controlled for the worst-case environments of use (e.g., least secure expected network configuration(s)).  `fn20-01`

## Appendix 4, Table 1 — Recommended Premarket Submission Documentation (verbatim)

| Type of Premarket Submission Documentation | Guidance Section(s) | IDE Submission* |
|---|---|---|
| Cybersecurity Risk Management Report | Sections V, VI.B | Could be helpful to submit, but not specifically recommended |
| - Threat Model (may include Architecture Views) | Sections V.A.1, V.A.3, V.A.4, V.A.5, V.B.2, Appendix 1, Appendix 2 | Could be helpful to submit, but not specifically recommended (see Architecture View recommendations) |
| - Cybersecurity Risk Assessment | Sections V.A.2, V.A.3, V.A.4, V.A.5, V.A.6 | Could be helpful to submit, but not specifically recommended |
| - SBOM | Sections V.A.4, VI.A | Recommended |
| - Vulnerability Assessment and Software Support | Section V.A.4 | Could be helpful to submit, but not specifically recommended |
| - Unresolved Anomalies Assessment | Section V.A.5 | Could be helpful to submit, but not specifically recommended |
| - Traceability | Sections V.A, V.A.1, V.A.2, V.A.3, V.A.4. V.A.5, V.A.6, V.B.1, V.B.2, V.C, VI.A | Could be helpful to submit, but not specifically recommended |
| Measures and Metrics | Section V.A.6 | Could be helpful to submit, but not specifically recommended |
| Architecture Views | Section V.B | Recommended · Global, Multi-patient and Updateability/Patchability views · Security Use Case views for functionality with safety risks |
| - Requirements | Sections V.B.1, Appendix 1 | Recommended · Global, Multi-patient and Updateability/Patchability views · Security Use Case views for functionality with safety risks |
| - Architecture Views (may be included in Threat Model) | Sections V.A.1, V.B.2, Appendix 1, Appendix 2 | Recommended · Global, Multi-patient and Updateability/Patchability views · Security Use Case views for functionality with safety risks |
| Testing | Section V.C | Could be helpful to submit, but not specifically recommended |
| Labeling | Section VI.A | Recommended · Informed Consent Form to include cybersecurity risks · General Cybersecurity Labeling - Connectivity and associated general cybersecurity risks, updateability/process |
| Cybersecurity Management Plans | Section VI.B | Could be helpful to submit, but not specifically recommended |

*For the purposes of this table, “recommended” refers to the elements of an IDE submission FDA discusses in Appendix 3 of this document; “could be helpful to submit, but not specifically recommended” refers to additional elements that could be helpful to FDA if submitted, but are not specifically recommended in Appendix 3. If a device-specific guidance contains additional or different recommendations to those in this table, the device-specific recommendations should be followed. If a manufacturer is unsure, they should utilize the FDA Q-submission process.  `App4.T1-01 App4.T1-02`

## Appendix 5 — Terminology (verbatim; definitions the statements above depend on)

> The terminology listed here are for the purposes of this guidance and are intended for use in the context of assessing medical device cybersecurity. These terms are not intended to be applied in any context beyond this guidance.

- **Anomaly** – any condition that deviates from the expected behavior based on user needs, requirements, specifications, design documents, or standards.
- **Asset** – anything that has value to an individual or an organization.[^85]
- **Attack Surface Analysis** – evaluation of attack surface to determine all avenues of ingress and egress to and from a system including common vulnerabilities and exposed ports and services.[^86]
- **Authentication** – the act of verifying the identity of a user, process, or device as a prerequisite to allowing access to the device, its data, information, or systems, or provision of assurance that a claimed characteristic of an entity is correct.[^87]
- **Authenticity** – information, hardware, or software having the property of being genuine and being able to be verified and trusted; confidence that the contents of a message originate from the expected party and has not been modified during transmission or storage.[^88]
- **Authorization** – the right or a permission that is granted to a system entity to access a system resource.[^89]
- **Availability** – the property of data, information, and information systems to be accessible and usable on a timely basis in the expected manner (i.e., the assurance that information will be available when needed).[^90]
- **Boundary Analysis** – the process of uniquely assigning information resources to an information system, which defines the security boundary for that system.[^91]
- **Closed Box Testing** – a method of software testing that examines the functionality of an application without peering into its internal structures of workings.[^92]
- **Compensating Controls** – a safeguard or countermeasure deployed, in lieu of, or in the absence of controls designed in by a device manufacturer. These controls are external to the device design, configurable in the field, employed by a user, and provide supplementary or comparable cyber protection for a medical device.[^93]
- **Confidentiality** – the property of data, information, or system structures to be accessible only to authorized persons and entities and are processed at authorized times and in the authorized manner, thereby helping ensure data and system security. Confidentiality provides the assurance that no unauthorized users (i.e., only trusted users) have access to the data, information, or system structures.[^94]
- **Configuration** – the possible conditions, parameters, and specifications with which a device or system component can be described or arranged.[^95]
- **Configuration Management** – a collection of activities focused on establishing and maintaining the integrity of information technology products and information systems, through control of processes for initializing, changing, and monitoring the configurations of those products and systems throughout the system development lifecycle.[^96]
- **Controlled Risk** – when there is sufficiently low (acceptable) residual risk of patient harm due to a device’s particular cybersecurity vulnerability.
- **Cryptography** – the discipline that embodies the principles, means, and methods for providing information security; including confidentiality, data integrity, non-repudiation, and authenticity.[^97]
- **Cybersecurity** – the process of preventing unauthorized access, modification, misuse or denial of use, or the unauthorized use of information that is stored, accessed, or transferred from a medical device to an external recipient.[^98]
- **Decommission** – a process in the disposition process that includes proper identification, authorization for disposition, and sanitization of the equipment, as well as removal of Patient Health Information (PHI) or software, or both.[^99]
- **Denial of Service** – prevention or impairment to the authorized use of the information system, resources, or services.[^100]
- **Disposal** – a process to end the existence of a system asset or system for a specified intended use, appropriately handle replaced or retired assets, and to properly attend to identified critical disposal needs (e.g., per an agreement, per organizational policy, or for environmental, legal, safety, or security aspects).[^101]
- **Encryption** – is the cryptographic transformation of data (called “plaintext”) into a form (called “ciphertext”) that conceals the data’s original meaning to prevent it from being known or used.[^102]
- **End of support** – a point beyond which the product manufacturer ceases to provide support, which may include cybersecurity support, for a product or service.
- **Exploitability** – the feasibility or ease and technical means by which the vulnerability can be exploited by a threat.[^103]
- **Firmware** – software program or set of instructions programmed on the flash read-only memory (ROM) of a hardware device. It provides the necessary instructions for how the device communicates with the other computer hardware.[^104]
- **Fuzz Testing** – process of creating malformed or unexpected data or call sequences to be consumed by the entity under test to verify that they are handled appropriately.[^105]
- **Hardware** – the material physical components of an information system.
- **Integrity** – the property of data, information and software to be accurate and complete and have not been improperly or maliciously modified.[^106]
- **Least Privilege** – a security principle that a system should restrict the access privileges of users (or processes acting on behalf of users) to the minimum necessary to accomplish assigned tasks.[^107]
- **Lifecycle** – all phases in the life of a medical device, from initial conception to final decommissioning and disposal.
- **Malware** – software or firmware intended to perform an unauthorized process that will have adverse impact on the confidentiality, integrity, or availability of an information system.[^108]
- **Patch** – a “repair job” for a piece of programming; also known as a “fix.” A patch is the immediate solution to an identified problem that is provided to users. The patch is not necessarily the best solution for the problem, and the product developers often find a better solution to provide when they package the product for its next release. A patch is usually developed and distributed as a replacement for or an insertion in compiled code (that is, in a binary file or object module). In many operating systems, a special program is provided to manage and track the installation of patches.[^109]
- **Patient harm** – injury or damage to the health of patients, including death.[^110]
- **Programmable logic** – hardware that has undefined function at the time of manufacture and must be programmed with software to function (e.g., Field-programmable gate array).
- **Quality of Service** – necessary level of measurable performance in a data communications system or other service which may include throughput (bandwidth), transit delay (latency), error rates, priority, security, packet loss, packet jitter, etc.[^111]
- **Reasonably foreseeable misuse** – use of a product or system in a way not intended by the manufacturer, but which can result from readily predictable human behavior.[^112]
- **Resilience** – the ability of an information system to continue to: (i) operate under adverse conditions or stress, even if in a degraded or debilitated state, while maintaining essential operational capabilities; and (ii) recover to an effective operational posture in a time frame consistent with mission needs.[^113]
- **Secure Product Development Framework (SPDF)** – a set of processes that reduce the number and severity of vulnerabilities in products. Additional information about an SPDF and its implementation is discussed in Sections IV and V, and throughout the guidance.[^114]
- **Security Architecture** – a set of physical and logical security-relevant representations (i.e., views) of system architecture that conveys information about how the system is partitioned into security domains and makes use of security-relevant elements to enforce security policies within and between security domains based on how data and information must be protected. The security architecture reflects security domains, the placement of security-relevant elements within the security domains, the interconnections and trust relationships between the security-relevant elements, and the behavior and interactions between the security-relevant elements.[^115]
- **Security Strength** – a measure of the computational complexity associated with recovering certain secret and/or security-critical information concerning a given cryptographic algorithm from known data (e.g., plaintext/ciphertext pairs for a given encryption algorithm).[^116] Throughout this guidance “strong” and other iterations of this term may be used that apply to this definition.
- **Security Risk Management** – a process (or processes) that evaluates and controls threat-based risks. For security risk management, this includes an evaluation of the impact of exploitation on the device’s safety and effectiveness, the exploitability, and the severity of patient harm if exploited.
- **Software Bill of Materials (SBOM)** – a formal inventory of software components and dependencies, information about those components, and their hierarchical relationships.[^117] The software components in an SBOM include, but are not limited to, commercial, open source, off-the-shelf, and custom software components. See Section V.A.4 for a more complete description of an SBOM.
- **System** – the combination of interacting elements or assets organized to achieve one or more function.[^118]
- **Threat** – any circumstance or event with the potential to adversely impact the device, organizational operations (including mission, functions, image, or reputation), organizational assets, individuals, or other organizations through an information system via unauthorized access, destruction, disclosure, modification of information, and/or denial of service. Threats exercise vulnerabilities, which may impact the safety or effectiveness of the device.[^119]
- **Threat modeling** – a methodology for optimizing system, product, network, application, and connection security by identifying objectives and vulnerabilities, and then defining countermeasures to prevent, or mitigate the effects of, threats to the system.[^120]
- **Threat surface** – the set of points on the boundary of a system, a system element, or an environment where a cyber threat can try to enter, cause an effect on, or extract data from, that system, system element, or environment.[^121]
- **Trustworthy Device** – a medical device that: (1) is reasonably secure from cybersecurity intrusion and misuse; (2) provides a reasonable level of availability and reliability; (3) is reasonably suited to performing its intended functions; and (4) adheres to generally accepted security procedures to support correct operation.[^122]
- **Uncontrolled risk** – when there is unacceptable residual risk of patient harm due to inadequate compensating controls and risk mitigations.
- **Unresolved anomaly** – a defect that still resides in the software because a sponsor deemed it appropriate not to correct or fix the anomaly, according to a risk-based rationale about its impact to the device’s safety and effectiveness.[^123]
- **Updatability and Patchability** – the ease and timeliness with which a device and related assets can be changed for any reason (e.g., feature update, security patch, hardware replacement).
- **Update** – corrective, preventative, adaptive, or perfective modifications made to software of a medical device.[^124]
- **Vulnerability** – a weakness in an information system, system security procedure(s), internal control(s), human behavior, or implementation that could be exploited.
- **Vulnerability Chaining** – the sequential exploit of multiple vulnerabilities in order to attack to attack a system, where one or more exploits at the end of the chain require the successful completion of prior exploits in order to be exploited.[^125]
