---
schema: "library-distilled/v1"
id: bsi-tr-03183-1-normative
record: bsi-tr-03183-1
type: normative
updated: "2026-10-02"
---


# BSI TR-03183-1 v1.0.0 — normative text

Verbatim from `.cache/bsi-tr-03183-1.txt` (pdftotext -layout of BSI-TR-03183-1_v1_0_0.pdf, sha256 `db5f5bfe…969ef`). Line breaks joined, page furniture removed. Structure follows the TR. Requirement ids and typed fields: `requirements.yaml`.

## 2 Important: State of this Document

As the technical and legal details of the CRA are still in development this document will be further developed in parallel with the European standardisation, legal clarification and further feedback on this guideline. For this purpose, this technical guideline will be handled as a “living document” and will be updated in regular intervals.

This document can be used as

- a collection of information and recommendations for manufacturers for the CRA;

- a platform for feedback for the CRA implementation and to support CRA standardisation;

- an entry into the CRA and a guideline to prepare for manufacturers without sufficiently structured security-by-design and vulnerability handling processes.

This document does NOT

- establish any obligations on manufacturers;

- provide presumption of conformity for essential cybersecurity requirements of the CRA when applied;

- always reflect the current state of standardisation contents;

- address cybersecurity requirements in other European legislations

- describe the only way to address the essential cybersecurity requirements laid out in the CRA.

## 4 Usage

This Technical Guideline is intended to be used for a self-assessment by the manufacturer or by a third party on behalf of the manufacturer. The following clarifications and assessment procedures have to be taken into account when performing the assessment.

### 4.1 Evaluator

The assessment is performed by an evaluator, which can be part of the manufacturer organisation or a third party. The following aspects have to be taken into account when selecting an evaluator:

- The evaluator needs sufficient technical knowledge as well as knowledge in assessment methods to perform the assessment in a qualified manner.

- The evaluator requires access to, or has to be provided with, all information required to perform the assessment

- The evaluator has to be impartial and should, if possible not be involved in the development of the PwDE, to facilitate an independent assessment.

It is always important to perform the assessment with an appropriately impartial and independent mindset and to stay objective, even if the evaluation is performed by the development team

### 4.2 Assessment Scope

The conformity assessment is performed on the design of the PwDE or an instance of the finished PwDE. The generic PwDE architecture in Figure 3 will be used.

The PwDE consists of the hardware and/or software components placed on the market according (Article 3(1) CRA). These "placed components" are distributed and placed under the control of a user.

- A PwDE might have multiple users, e.g. an integrator installing the PwDE, an NOTE administrator configuring and maintaining the PwDE or an end-user actually using the functionality of the PwDE. A distributor reselling the PwDE as is, is not regarded as a user, as the distributor neither changes the PwDE nor uses it for one of its functionalities.

Where the PwDE provides the possibility to be altered by hardware or software components, placed on the market by, or under control of the manufacturer or other parties, these components do not have to be considered in the assessment. The interfaces to accommodate these components on the other hand are part of the PwDE and part of the assessment. Furthermore, the effects of possible additional components have to be considered in the risk assessment.

The same is true for PwDE that are supposed to be used in conjunction with other PwDE, placed on the market by, or under control of the manufacturer or other parties.

Additional components integrated by the user are not part of the PwDE, e.g. additional apps or services. Although these components not integrated by the manufacturer are not part of the PwDE, the associated risks still have to be taken into account when performing the risk assessment if the integration of third-party components by the user is within the intended purpose or foreseeable use of the PwDE.

Besides the software and hardware components placed on the market, the PwDE also contains remote data processing solutions (RDPS) designed and developed by the manufacturer, or under the responsibility of the manufacturer, and the absence of which would prevent the product with digital elements from performing one of its functions (Article 3(2) CRA).

- Figure 3 Generic PwDE architecture

According to CRA Article 26 additional guidance on the RDPS will be provided by the Commission. For the meantime this technical guideline will assume that every software designed and developed by or on behalf of the manufacturer, which provides a function used by the "placed components" are "RDPS" of the PwDE. Development also includes the customization of third-party software and implementation of new features used by the PwDE. The act of configuring a third-party software is not regarded as development.

This includes RDPS designed and developed by the manufacturer required for essential functionalities of the PwDE as well as RDPS necessary for other PwDE functionalities without importance for the user, like telemetry or advertisement, as these non-essential functions might also pose a risk to the PwDE. Software with no impact on the functionality of the PwDE is not part of the PwDE even if developed by the manufacturer.

### 4.3 Time of assessment

As it cannot be avoided that the PwDE is modified to an insecure state by the user, only the state after the initial configuration following the recommendations in the user’s manual and (potential) update to the newest version is relevant for the assessment. This state can be achieved by executing the following steps:

- Obtaining a new PwDE or resetting the PwDE to its original state, e.g. factory reset or new installation.

- Start-up of the PwDE and initial setup following the recommendations in the user’s manual.

- Performing an update to the newest software version, if not already done during the initial setup.

### 4.4 Modal verbs

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED” and “OPTIONAL” in this document are to be interpreted as described in BCP 14 (RFC 2119, RFC 8174 ) when, and only when, they appear in all capitals, as shown here.

- 1. MUST This word, or the terms "REQUIRED" or "SHALL", means that the definition is an absolute requirement of the specification.

- 2. MUST NOT This phrase, or the phrase "SHALL NOT", means that the definition is an absolute prohibition of the specification.

- 3. SHOULD This word, or the adjective "RECOMMENDED", mean that there may exist valid reasons in particular circumstances to ignore a particular item, but the full implications must be understood and carefully weighed before choosing a different course.

- 4. SHOULD NOT This phrase, or the phrase "NOT RECOMMENDED" mean that there may exist valid reasons in particular circumstances when the particular behaviour is acceptable or even useful, but the full implications should be understood and the case carefully weighed before implementing any behaviour described with this label.

### 4.5 Control

The requirements of the CRA are dictated by the legislation itself. This technical guideline will set out controls with the goal to mitigate the cybersecurity risks of PwDE and fulfil the essential cybersecurity requirements of the CRA.

Each control consists of the following parts:

- Input (Activity only): Expected input for manufacturer activities

- Risk (Optional): Risk-based scenario under which the control is applicable

- Control: has to be met by the PwDE or part thereof where applicable.

- Output (Activity only): Expected output of manufacturer activities

- Target (Optional): Type of component or function secured by the control.

- Assessment Guidance (Optional): Additional guidance for the assessment of the control. Depending on the associated risks different levels of assessment guidance might be provided.

- Implementation Guidance (Optional): Implementation specific information for the control, e.g. a specific cryptographic algorithm or a specific configuration of the PwDE. This is not a mandatory requirement, but rather a recommendation to implement the control in a specific way in accordance with the associated risk.

- Compensation (Optional): Alternative control for compensation if the initial control can not be fulfilled.

- Reference CRA: Essential requirement or other requirement of the CRA supported by the control. This reference can be used to identify the essential requirements implemented by the PwDE.

### 4.6 Assessment Procedure

This section specifies an assessment procedure on how to assess that the security controls stated in this Technical Guideline are met. For reproducibility and consistency every assessment step should be documented by the evaluator and included in the assessment report as defined in section 4.8.

The assessment is performed by evaluating the applicability and fulfilment of every control in this document based on the following rules:

Controls: Controls consist of a normative statement with MUST, the control is fulfilled (PASS) if the statement can be assessed as true, otherwise the control is not fulfilled (FAIL). A control can be marked as not applicable (N/A), if

- a referenced compensation is fulfilled instead,

- the target mechanism of the control does not exist in the PwDE,

- an "if" condition in the control statement does not apply,

- or the control is in conflict with other regulations.

Generally controls are specific enough for evaluation, if not the control will be supplemented by additional guidance which has to be used for assessing the control. Controls have to be at least assessed on a conceptional level based on the documentation of the PwDE. A functional assessment based on the behaviour of the PwDE or the manufacturer is recommended for additional assurance if possible, but not required.

Risk-based Controls: Risk-based controls consists of one or more risk-scenarios, a requirement and optional assessment criteria. Risk-based controls can be not applicable (N/A) if the risk does not apply to the PwDE. Risk-based controls are fulfilled (PASS) if the underlying control is fulfilled by the PwDE or part thereof affected by the risk.

Generally the requirements of the CRA can be satisfied with any kind of control appropriate to sufficiently mitigate cybersecurity risks. This guideline uses the following types of controls for easier differentiation:

Activity: Activities are administrative controls consisting of an activity to be performed by the manufacturer as well as an expected input and output. Process controls are fulfilled (PASS) if the activity stated in the requirement is performed by the manufacturer and the required output is produced; otherwise, the control is not fulfilled (FAIL).

Mechanism: Mechanisms are active technical controls and are fulfilled (PASS) if the control is implemented as described by the PwDE, otherwise the control is not fulfilled (FAIL).

Documentation: Documentation is generated in the context of the PwDE but not direct part of the PwDE. Documentation controls are fulfilled (PASS) if the manufacturer provides the described documentation in the described manner for internal, external or public consumption. The assessment of documentation does not include the assessment of the underlying processes.

The assessment is preferably integrated into the development processes and continuous quality assurance processes, if possible in an automated manner.

The overall verdict "PASS" is given if all controls are marked as "PASS" or "N/A", otherwise "FAIL".

The assessment step might include one of the following terms, which have to be interpreted by the evaluator:

- (Generally acknowledged) state of the art refers to the current and generally acknowledged best practices within a specific field for a specific use case. This does generally not require the usage of the latest technology, but rather the usage of well-known and established technologies, methods and processes appropriate for a specific use case. If necessary examples or criteria for state of the art will be given.

- (Generally acknowledged) State of the art cryptography follows common and well-known cryptographic recommendations e.g. BSI TR-02102, ECCG Agreed Cryptographic Mechanisms for EUCC or comparable standards meeting the requirements of ISO 18033-1 Annex A. A cryptographic mechanism can be considered state of the art if it is suitable for the corresponding use case and no feasible attack with current readily available technology is known.

- Provide and publish indicates the required distribution of information. By default the manufacturer is not required to make documentation or other records available for third- parties if not otherwise specified with provide or publish. Providing means granting access to a document for a specific third-party, e.g. the user of the PwDE. Publish means that something is documented and available for free, easy and public access.

- Support and implement indicates if a functionality has to be implemented into the PwDE directly or only be supported in the context of integration into another PwDE.

- By default and always indicates the validity of a configuration/policy of the PwDE. "by default" means the PwDE behaves in a described manner if not configured otherwise by the user. "Always" means the behaviour is enforced and cannot be changed by the user.

### 4.7 Interpretation of the overall verdict

The overall verdict is as an indicator if a PwDE is compliant with the requirements of this Technical Guideline, but is no direct statement of compliance with the CRA.

A "FAIL" does not necessarily mean the PwDE is not compliant with the CRA, as some requirements of this guideline might not be applicable for every PwDE. Neither does a "PASS" mean that the PwDE is compliant with the CRA, as the PwDE might impose risks which are not covered by this Technical Guideline.

### 4.8 Assessment Report

Pursuant to Article 31 CRA the manufacturer must draw up technical documentation before placing a PwDE on the market. This includes, among other things:

- A general description of the product with digital elements, including its intended purpose, versions of software affecting compliance with essential cybersecurity requirements, user information and instructions as set out in Annex II as well as photographs or illustrations showing external features, marking, and internal layout in case of hardware.

- A description of the design, development and production of the product with digital elements and vulnerability handling processes

- Necessary information and specifications of the production and monitoring processes of the product with digital elements and the validation of those processes;

- An assessment of the cybersecurity risks against which the product with digital elements is designed, developed, produced including how the essential cybersecurity requirements of Annex I Part I are applicable;

- Reports of the tests carried out to verify the conformity of the product with digital elements and of the vulnerability handling processes with the applicable essential cybersecurity requirements as set out in Parts I and II of Annex I;

Using this Technical Guideline a assessment report can be generated to document the assessment of the PwDE. Based on the requirements for technical documentation the assessment report has to include at least the following information:

- Date of the assessment

- Identification of the PwDE, including at least:

- Name and model of the PwDE

- Description of the PwDE and intended purpose and reasonable foreseeable use

- Version of hardware and software

- Software bill of materials (SBOM) where applicable

- For hardware PwDE: Photographs or illustrations showing external features, marking and internal layout as well as hardware components with digital elements

- Risk assessment

- Identified assets and threats

- Evaluated risks

- Accepted risks

- Design Documentation

- Architecture of the PwDE, including hardware and software components with digital elements as well as network and physical interfaces

- Selected controls including mitigated risk and corresponding applicable essential cybersecurity requirements

- Non-applicable essential cybersecurity requirements and justification

- Description of implementation of selected controls

- Verification processes for the selected controls

- Description of vulnerability handling activities

- Verification of vulnerability handling activities

- Provided user documentation

## 5 Risk-based Approach

### 5.1–5.7 Context (verbatim)

### 5.1 Relevance of (Cybersecurity) Risks

According to Article 13 and Annex I Part 1 manufacturers shall ensure that their PwDEs are designed, developed and produced according to the essential cybersecurity requirements set out in Part I of Annex I in such a way that they ensure an appropriate level of cybersecurity based on the risks.

For this manufacturers shall undertake an assessment of the (cybersecurity) risks associated with a PwDE and take the outcome of that assessment into account during the planning, design, development, production, delivery and maintenance phases of the product with digital elements with a view to minimising cybersecurity risks by preventing incidents and minimising their impact.

This approach is necessary to establish an appropriate level of cybersecurity for the broad spectrum of PwDEs covered by the CRA and to enable the manufacturer to exercise due diligence during the complete PwDE lifecycles with the actions and processes fitting for its specific use case.

Risk Assessment is widely used in different use cases as every decision has an inherent risk. For the scope of this document the term "risk" is always used in the context of cybersecurity with the goal to reduce the risk to the PwDE, the user, the environment and networks connected to the PwDE to an acceptable level. The term "minimising" as stated in the legislation will not be used, as it is generally not the goal to reduce the associated risk to a minimum as that is generally not feasible and not necessary to handle risks in an appropriate manner. The goal is to reduce the risk to an acceptable level.

### 5.2 Explanation on Risk-Terms

For the risk assessment the terms asset, (cybersecurity) threat, (cybersecurity) risk and (cybersecurity) incident will be used.

Asset: Assets are everything worth protecting which is created, processed, stored or otherwise influenced by the PwDE. This can be, among others, data, created, transmitted, stored or otherwise processed by the PwDE, network resources provided, used or otherwise influenced by the PwDE, physical or other assets as well as the integrity and proper function of the PwDE itself, privacy, safety and health of users of, and everybody affected by the PwDE.

(Cybersecurity) Incident: According to Article 3 an incident "is any event having an actual adverse effect on the security of network and information systems". Following this a (cybersecurity) incident is a single cybersecurity related event with an adverse effect on the security of assets of the PwDE.

(Cybersecurity) Threat: According to Article 3 a threat is "Any potential circumstance, event or action that could damage, disrupt or otherwise adversely impact network and information systems, the users of such systems and other persons". A threat does only conclude that there is a potential for an incident and does not include the likelihood and potential impact of the threat. This abstraction is necessary as an incident can only be handled after it occurred, in contrast a threat can be used for evaluating potential cybersecurity measures to prevent, detect and correct incidents.

(Cybersecurity) Risk: According to Article 3 a cybersecurity risk is the potential for loss or disruption caused by an incident and is to be expressed as a combination of the magnitude of such loss or disruption and the likelihood of occurrence of the incident. Adding the statements of likelihood and impact (magnitude of such loss or disruption) to a threat, makes it possible to plan appropriate security measures to prevent, detect and correct incidents and to prioritize their implementation.

As this technical guideline will only handle risks related to cybersecurity, the term cybersecurity will not be explicitly stated in conjunction with incident, threat and risk.

### 5.3 Tailoring of the risk-based approach

The appropriate handling of risks is highly specific to the type of PwDE and its intended purpose and foreseeable use. The risk handling in this technical guideline is based on the ISO 31000 and constitutes a general set of activities common to risk-based approaches, which can be used for every kind of PwDE. To simplify the risk handling for a specific use case and to ease the implementation into existing processes the activities as well as the input and output can generally be customized, as long as it meets the general aspects and requirements set out in this document. The practice of customization to a specific use case is called "tailoring" and will be indicated throughout this document if encouraged.

It is generally advisable to use well known standards and frameworks for the tailoring of the risk based approach to incorporate existing sectorial knowledge about existing PwDE specific risks and their appropriate treatment.

This guideline can be used standalone or in conjunction with other sector specific standards using the general activities laid out in this chapter.

### 5.4 Risk Handling

The minimal risk handling activities as shown in Figure 4 are risk assessment consisting of identification, analysis and evaluation of potential risks and the risk treatment to reduce risks to an acceptable level. Both activities are based on a risk context which describes the PwDE as well as criteria for the analysis and evaluation of risks.

The ISO 31000 uses the term risk management which also includes the activities "communication and consultation" for communicating and coordination risks with stakeholders, "review and monitoring" for reviewing the existing risks assessment and reacting to new risks as well as "recording and reporting" for the documentation of risks. Those activities are also partially included in the manufacturer’s obligations of updating the risk assessment and reporting risks and will be described separately, if needed.

- Figure 4 Risk Handling Overview

### 5.5 Risk handling as a process

Risk handling processes are individual based on the specific organisational needs. Generally there are some aspects to consider:

- Risk handling is iterative: It is not possible to handle all relevant risks in one go, as even with the most rigorous risk assessment there will very likely be risks not evaluated before as reality is complex and external factors can change often and risk mitigation measures will introduce new or affect existing interactions inside the PwDE, that have to be reassessed. Thus it is important to stay flexible by implementing usable and structured processes able to react to change and uncertainty. This applies to pre- as well as post-market.

- Risk handling is multi-layered: Risk handling is part of every part of a PwDE’s lifecycle with different layers of granularity, based on the relevant stakeholders from governance, design, development, production and operations. This multi-layered approach will ensure an appropriate stakeholder engagement as well as multiple viewpoints necessary to get a good result. This guideline will stay on a level of granularity fit for PwDE design as it is intended to help technical experts preparing for the CRA while simultaneously giving them the freedom for specific implementations.

- Risk handling is communication: The key to successful risk handling is communication as everyone involved in the PwDE is able to contribute with valuable insights and information necessary to handle risks appropriately. Thus it is important to be transparent on risks and communicate them with the relevant stakeholders.

### 5.6 Perspectives for risk handling

Risk handling is based on the expertise of the people involved as well as their perspective. Risk handling has to find an appropriate balance between the different perspectives. Common perspectives for risk handling are:

- Cyber Security perspective: The PwDE has to protect the user or other stakeholders. Cybersecurity tries to assess what aspects of the PwDE are valuable and how to protect them. This perspective tries to represent the cybersecurity needs of the user or other entities affected by the PwDE and to reduce cybersecurity risks as much as possible.

- Developer perspective: The PwDE has to provide a function for the user. A developer has primarily the function in mind and thus risks have to be assessed and treated in harmony with the intended purpose of the PwDE. This perspective is needed to ensure that the PwDE stays usable and functional for the user.

- Attacker perspective: The PwDE is subject to potential attackers. An attacker tries to assess if a PwDE is worth attacking and how to do so. This perspective is important for the balance as it actively works against the interests of the user. Normally there is no real attacker involved in PwDE development, consequently this can be emulated by internal expertise in offensive security, e.g. penetration testers or other cybersecurity experts.

### 5.7 Risk Context

The risk context contains all information necessary to perform the risk assessment. The risk context is highly individual for the specific product with digital elements and consists of the following components.

#### 5.7.1 Intended purpose and reasonable foreseeable use

Risks which only impact the manufacturer, i.e. costs of necessary cybersecurity measures or the impact of cybersecurity measures on potential business opportunities, are generally not considered and are up to the manufacturer.

To assess the scope of the risk assessment it is necessary to define the context of the PwDE in regards to cybersecurity. Based on Article 13(1) products with digital elements shall be made available on the market only where they meet the essential cybersecurity requirements set out in Annex I Part I, provided that they are properly installed, maintained, used for their intended purpose or under conditions which can reasonably be foreseen, and, where applicable, the necessary security updates have been installed; and the processes put in place by the manufacturer comply with the essential cybersecurity requirements set out in Annex I Part I.

This means that the manufacturer can assume that their PwDEs are used for their intended purpose or other use cases that can be reasonably foreseen. 'reasonably foreseeable use' means use that is not necessarily the intended purpose supplied by the manufacturer, but which is likely to result from reasonably foreseeable human behaviour or technical operations or interactions.

The CRA also addresses reasonably foreseeable misuse, which is in general not part of the risk assessment but has to be documented according Annex II CRA when posing a significant security risk. 'reasonably foreseeable misuse' means the use of a product with digital elements in a way that is not in accordance with its intended purpose, but which may result from reasonably foreseeable human behaviour or interaction with other systems. Intentionally malicious or detrimental actions by the users, which deliberately endanger the security of the PwDE or other systems, e.g. jailbreaking of a device or intentionally configuring a PwDE to be insecure are generally not part of intended purpose or foreseeable use.

Based on this assumption the manufacturer can establish his risk assessment based on the intended purpose of the product as well as the reasonably foreseeable use. Following article 13 (3) this includes among other things:

- The functionality of the PwDE required to serve the intended purpose

- The potential degrees of freedom which will enable the use for a reasonably foreseeable use not included in the intended purpose

- The (operational) environment in which the PwDE will be used (indoor or outside, private or office environment or other)

- The intended target user and usage scenarios (layman or professional users, single or multi user or other)

- Length of time the PwDE is expected to be in use

#### 5.7.2 PwDE architecture

Besides the intended purpose and foreseeable use a PwDE architecture is also necessary to perform an effective risk assessment. The architecture is a high level technical description of the PwDE and should include:

- The connective capabilities of the PwDE (WAN, Bluetooth, WLAN or other )

- The (potential) relation and communication of the PwDE’s components with its remote data processing solutions

- The (potential) relation and communication to other PwDE or PwDE components

- The boundaries of the PwDE

Generally the risk context also includes the boundaries of the assessed PwDE as the risk assessment and especially the risk treatment can often only be sufficiently performed for PwDEs or components under the responsibility of the manufacturer. Risks associated with components outside of the PwDE might have to be handled by other entities. This is generally no problem for components in scope of the CRA as they are required to be designed, developed and produced in such a way that they ensure an appropriate level of cybersecurity based on the risks for the intended purpose.

The manufacturer is generally responsible for third-party components integrated by the manufacturer itself and has to exercise due diligence according to CRA Article 13 (5). How to handle risks relating third-party components integrated by the manufacturer will be discussed in section 5.11.

#### 5.7.3 Decision Criteria

The risk assessment aims to identify risks which have to be treated. The decision if a risk has to be treated depends on the potential impact of the risk and other factors. To establish a comprehensible and consistent assessment the factors and criteria used for decision making have to be established as part of the risk context.

It is generally advisable to use existing specific standards based on existing sectorial knowledge and best practices.

For the risk assessment described in this document three types of criteria will be used:

- Impact criteria contain information on types of assets and the expected base impact of an incident, based on the type of affected asset and the loss of confidentiality, integrity and availability. The base impact can be raised depending on the duration of the incident, the affected number of assets or on other factors.

- Likelihood criteria contain information on the estimated likelihood of an incident, based on existing compensation provided by the context of the PwDE.

- Acceptance criteria define which risks are acceptable, based on the potential impact and likelihood of the risk.

A strategy on using these decision criteria as well as an initial set of criteria will be provided at the end of this chapter and can be tailored by the manufacturer for his specific use case based on its specific processes.

### Risk-handling activity controls (§5.8–§5.13)

#### RH_RA.1.1.1 — Asset Identification (Activity) (§5.8.1.1.3 Control (RH_RA.1.1.1))

- **Input:** Functionality of the PwDE with digital elements based on the intended purpose and reasonably foreseeable use; Recommended: Catalogue of common assets and asset categories
- **Control:** The manufacturer MUST identify all assets of the PwDE.
- **Output:** (Categorized) List of Assets of the PwDE
- **Reference CRA:** CRA Annex I Part I (1)

#### RH_RA.1.1.2 — Threat Modelling (Activity) (§5.8.1.2.3 Control (RH_RA.1.1.2))

- **Input:** Intended purpose and reasonably foreseeable use; PwDE architecture; List of assets (Optional: Threat catalogue)
- **Control:** The manufacturer MUST identify the threats to the assets and the potentially affected components of the PwDE.
- **Output:** List of identified risks resulting from threats and potentially affected assets and components of the PwDE
- **Reference CRA:** CRA Annex I Part I (1)

#### RH_RA.1.2 — Risk Analysis (Activity) (§5.9.3 Control (RH_RA.1.2))

- **Input:** List of identified risks; Likelihood of an incident based on Likelihood criteria; Impact of a potential incident based on impact criteria
- **Control:** The manufacturer MUST analyse the risks of the PwDE in regard to their likelihood and potential impact.
- **Output:** List of (analysed) risks including impact and likelihood
- **Reference CRA:** CRA Annex I Part I (1)

#### RH_RA.1.3 — Risk Evaluation (Activity) (§5.10.3 Control (RH_RA.1.3))

- **Input:** List of analysed risks; Acceptance criteria
- **Control:** The manufacturer MUST evaluate whether the analysed risks of the PwDE can be accepted or not.
- **Output:** List of (evaluated risks), which have to be treated or have been accepted
- **Reference CRA:** CRA Annex I Part I (1)

#### RH_RT.1.1.1 — Select appropriate controls (Activity) (§5.11.1.3 Control (RH_RT.1.1.1))

- **Input:** List of evaluated risk, which have to be treated
- **Control:** The manufacturer MUST select appropriate controls to treat the evaluated risks and to reduce them to an acceptable level and include the selected controls in the design of the PwDE.
- **Output:** List of selected controls and associated risks to be included in the design of the PwDE
- **Reference CRA:** CRA Annex I Part I (1)

#### RH_RT.1.1.2.1 — Select Applicable Essential Cybersecurity Requirements (Activity) (§5.11.2.3 Control (RH_RT.1.1.2))

- **Input:** List of selected controls and associated risks to be included in the design of the PwDE
- **Control:** The manufacturer MUST select and document applicable essential cybersecurity requirements from Annex I Part I (2) based on the selected controls.
- **Output:** List of applicable and non-applicable essential cybersecurity requirements from Annex I Part I (2)
- **Reference CRA:** CRA Annex I Part I (2) point (a), CRA Annex I Part I (2) point (b), CRA Annex I Part I (2) point (c), CRA Annex I Part I (2) point (d), CRA Annex I Part I (2) point (e), CRA Annex I Part I (2) point (f), CRA Annex I Part I (2) point (g), CRA Annex I Part I (2) point (h), CRA Annex I Part I (2) point (i), CRA Annex I Part I (2) point (j), CRA Annex I Part I (2) point (k), CRA Annex I Part I (2) point (l), CRA Annex I Part I (2) point (m)

#### RH_RT.1.1.2.2 — Select Applicable Essential Cybersecurity Requirements (Activity) (§5.11.2.3 Control (RH_RT.1.1.2))

- **Input:** List of selected controls and associated risks to be included in the design of the PwDE
- **Control:** The manufacturer MUST document and justify any non-applicable essential cybersecurity requirements from Annex I Part I (2) based on the associated risks.
- **Output:** List of applicable and non-applicable essential cybersecurity requirements from Annex I Part I (2)
- **Reference CRA:** CRA Annex I Part I (2) point (a), CRA Annex I Part I (2) point (b), CRA Annex I Part I (2) point (c), CRA Annex I Part I (2) point (d), CRA Annex I Part I (2) point (e), CRA Annex I Part I (2) point (f), CRA Annex I Part I (2) point (g), CRA Annex I Part I (2) point (h), CRA Annex I Part I (2) point (i), CRA Annex I Part I (2) point (j), CRA Annex I Part I (2) point (k), CRA Annex I Part I (2) point (l), CRA Annex I Part I (2) point (m)

#### RH_RT.1.2.1 — Risk Sharing with Suppliers (Activity) (§5.11.3.1.3 Control (RH_RT.1.2.1))

- **Input:** List of selected risks to share
- **Control:** If sharing risks with a third-party supplier, the manufacturer MUST exercise due diligence by ensuring that the manufacturer of the integrated component is legally obliged, contractually required or otherwise able and willing to treat the risk accordingly.
- **Output:** List of shared risks including the actions taken by the manufacturer to exercise due diligence
- **Reference CRA:** CRA Annex I Part I (1)

#### RH_RT.1.2.2 — Risk Sharing with Users (Activity) (§5.11.3.2.3 Control (RH_RT.1.2.2))

- **Input:** List of selected risks to share
- **Control:** If sharing the risk with the user, the manufacturer MUST ensure that the shared risks are within the foreseeable expectations of the user and that sufficient guidance documenting the risks and the expected mitigation by the user according to [USER_DOCUMENTATION] is provided.
- **Output:** List of shared risks including the actions taken by the manufacturer to document shared risks
- **Reference CRA:** CRA Annex I Part I (1)

#### RH_RT.1.3 — Implementation and Verification (Activity) (§5.11.4.3 Control (RH_RT.1.3))

- **Input:** List of selected controls and associated risks to be included in the design of the PwDE
- **Control:** The manufacturer MUST implement the selected controls and verify their effectiveness and correctness, in accordance with the associated risk.
- **Output:** List of implemented controls and performed verification
- **Reference CRA:** CRA Annex I Part I (1)

#### RH_DOC.1 — Documentation of the risk assessment (Activity) (§5.12.3 Control (RH_DOC.1))

- **Input:** Risk context * Evaluated risks * Shared risks * Implemented controls * Applicable essential cybersecurity requirements
- **Control:** The manufacturer MUST document the results of the risk assessment in a comprehensive manner. This includes the risk context, the evaluated risks including the corresponding implemented controls and shared risks as well as the applicable essential cybersecurity requirements.
- **Output:** Documentation of the risk assessment
- **Reference CRA:** CRA Annex I Part I (1)

#### RH_UPD.1 — Update Risk Assessment (Activity) (§5.13.3 Control (RH_UPD.1))

- **Input:** Risk Assessment- Optional: Event influencing the risk context
- **Control:** The manufacturer MUST update the risk assessment when the risk context of the PwDE changes and treat new unaccepted risks accordingly.
- **Output:** Updated risk assessment
- **Reference CRA:** Article 13(3)

### General text of §5.8–§5.13 (verbatim, includes the lower-case obligations R-NNNN)

5.8 RH_RA.1 - Risk Assessment Based on the context of the PwDE it is possible to identify and analyse potential cybersecurity risks to the PwDE. The following requirements are a general approach based on the ISO 31000 scoped for the purpose of assessing the cybersecurity risk of a PwDE in general manner. Risk assessment consists of risk identification, risk analysis and risk evaluation.

5.8.1 RH_RA.1.1 - Risk Identification

5.8.1.1 RH_RA.1.1.1 -Asset Identification (Activity)

###### 5.8.1.1.1 General

To identify potential risks to a PwDE it is necessary to identify the assets of the PwDE potentially affected by the realization of a risk. Assets are everything of the PwDE worth protecting.

This includes among others:

- The PwDE, its components and its functions

- Data assets collected, stored or otherwise processed by the PwDE

The list of assets should not include objects outside of the PwDE, as those can not be directly protected by the PwDE and will be unnecessarily redundant, as everything outside of the PwDE which can be affected by the PwDE has a corresponding asset in the PwDE.

To keep the list of identified assets manageable it is advisable to group assets into categories based on the use case and general type of asset based on an asset catalogue. The list of assets in the impact criteria may be used as a base for the asset management.

###### 5.8.1.1.2 Input

- Functionality of the PwDE with digital elements based on the intended purpose and reasonably foreseeable use

- Recommended: Catalogue of common assets and asset categories

###### 5.8.1.1.3 Control

- The manufacturer MUST identify all assets of the PwDE.

###### 5.8.1.1.4 Output

- (Categorized) List of Assets of the PwDE

###### 5.8.1.1.5 Reference CRA

- CRA Annex I Part I (1)

5.8.1.2 RH_RA.1.1.2 -Threat Modelling (Activity)

###### 5.8.1.2.1 General

It is possible to identify the potential risks to the PwDE resulting from cyber threats to the previously identified assets. This includes all threats with potential adverse impact to the assets of the PwDE. This is independent of the likelihood or impact of an incident resulting from the cyber threat as this will be considered when the to be identified cyber risks are analysed and evaluated.

Generally cyber threats are dependent on the intended purpose and reasonably foreseeable use of the PwDE without regards to a specific threat actor. It is generally advisable to use a structured approach for threat identification based on an existing threat catalogue. As threats can affect different components of PwDE and their relations the threat identification can be supplemented by a data flow model for easier location of the affected components of the PwDE.

If components or RDPS of the PwDE are reused for other PwDEs, e.g. a companion app used for multiple IoT devices or a RDPS of the manufacturer used for multiple PwDEs, it is generally advisable to split threat modelling and the consequent risk assessment into components for easier reuse. This way the risk handling for a common component can be done in one place and only has to be updated for each new related PwDE if necessary.

###### 5.8.1.2.2 Input

- Intended purpose and reasonably foreseeable use

- PwDE architecture

- List of assets (Optional: Threat catalogue)

###### 5.8.1.2.3 Control

- The manufacturer MUST identify the threats to the assets and the potentially affected components of the PwDE.

###### 5.8.1.2.4 Output

- List of identified risks resulting from threats and potentially affected assets and components of the PwDE

###### 5.8.1.2.5 Reference CRA

- CRA Annex I Part I (1)

5.9 RH_RA.1.2 -Risk Analysis (Activity)

#### 5.9.1 General

The Analysis of an identified risk is necessary for the evaluation of the risk and includes the magnitude of the loss or disruption caused by an incident (impact) and the likelihood of occurrence of the incident. The impact is primarily defined through the value of the affected assets as an incident with a negative influence on an important asset has a higher impact than an incident affecting assets of lower importance.

The impact can be determined based on impact criteria for the affected assets and additional amplifying factors, which can include the amount of affected assets and the duration of the adverse effect. Generally the value and consequently the potential impact on an asset is dependent on the usage of the PwDE and the interests of the involved stakeholders, as businesses might have other priorities than a consumer.

The likelihood of an incident is influenced by several factors, which can include

- Attacker Motivation (Valuable assets raise the likelihood of an incident as there is a higher motivation for more qualified attackers)

- Communicative capabilities and communicative relations of the PwDE ( Depending on the communicative capabilities and functionality communication which can be accessed by external actors, the PwDE might be more likely to experience an incident)

- Potential exposure of the PwDE through existing vulnerabilities

- Potential exposure of the PwDE through the operational environment

- Implemented or designed security controls

Generally, determining the likelihood of risks requires existing specific experience as well as applicable statistics and threat intelligence. To keep the estimation of likelihood comprehensible appropriate likelihood criteria have to be established.

If the impact or likelihood of an identified risk can not be assessed, because it depends on additional parameters, e.g. attacker potential, duration of the incident, number of affected PwDEs, the identified risk should be split into multiple risks depending on the parameters. This will result in additional identified risks extending the list generated in REQ_RA 1.1.2.

NOTE Rationale on impact and likelihood

- The assessment of likelihood and impact can be performed using quantitative or qualitative methods or a mix of both. It is generally advisable to use sectorial appropriate methods for the risk analysis, fitting for the specific use case. Generally, the analysis of risks is subjective and based on the experience of the person performing the risk analysis. Additional information to qualify or quantify the impact or likelihood of a risk enhances the reliability of the risk analysis, but raises the complexity and effort required for the risk analysis.

- As it’s generally not possible to completely, precisely and objectively assess the likelihood and impact of risks, the effort used for the risk analysis should be put into perspective to the effort of treating a potential risk. The result of the risk analysis is the decision, if a risk has to be treated - Yes or No.

- Consequently it might be more reliable and easier to handle a potential risk, instead of taking the effort to precisely assess the impact and likelihood. To support this statement and not give a false sense of numerical accuracy, this Technical Guideline does not use a quantitative approach. Instead, a qualitative approach using parametrized risk scenarios will be used based on asset categories and operational environments.

#### 5.9.2 Input

List of identified risks

- Likelihood of an incident based on Likelihood criteria

- Impact of a potential incident based on impact criteria

#### 5.9.3 Control

The manufacturer MUST analyse the risks of the PwDE in regard to their likelihood and potential impact.

#### 5.9.4 Output

List of (analysed) risks including impact and likelihood

#### 5.9.5 Reference CRA

CRA Annex I Part I (1)

5.10 RH_RA.1.3 -Risk Evaluation (Activity)

#### 5.10.1 General

After the risks have been analysed, the manufacturer needs to evaluate if the analysed risks have to be treated or can be accepted. This activity relies on acceptance criteria containing rules for the acceptance of a risk. As with other decision criteria these can be general, sector, organisation or PwDE specific.

NOTE Rationale on Acceptance

- It is generally possible to include additional parameters in the acceptance criteria and to define risk acceptance levels for different use cases. It might be useful to establish risk acceptance levels for separate usage scenarios, e.g. consumer, business, government to handle multiple scenarios with one set of identified risks and for easier communication of the intended use of the PwDE. This approach is not used in this guideline in order to keep the risk assessment flexible and generally applicable. Conceptually there is no difference as every additional parameter used to evaluate the risk acceptance can be reduced to impact and likelihood.

#### 5.10.2 Input

List of analysed risks

- Acceptance criteria

#### 5.10.3 Control

The manufacturer MUST evaluate whether the analysed risks of the PwDE can be accepted or not.

#### 5.10.4 Output

List of (evaluated risks), which have to be treated or have been accepted

#### 5.10.5 Reference CRA

CRA Annex I Part I (1)

5.11 RH_RT.1 - Risk Treatment Risks which a not accepted have to be treated. Treatment does not entail the complete eradication of a risk, as that is generally not possible. The goal of the treatment is to reduce the impact or likelihood of a risk to an acceptable level by implementing appropriate security measures based on the essential cybersecurity requirements of Annex I Part I.

The first essential cybersecurity requirement Part I (1) of Annex I states that "products with digital elements shall be designed, developed and produced in such a way that they ensure an appropriate level of cybersecurity based on the risks". This entails that an appropriate risk treatment based on the risk is a required part of the PwDE design. If the PwDE design is properly implemented it will result in a secure development and production.

The treatment of risks is in the responsibility of the manufacturer and up to the process and used standard of the manufacturer. This document will define a strategy for selecting requirements and appropriate controls later on, which can be combined with existing standards and processes.

5.11.1 RH_RT.1.1.1 -Select appropriate controls (Activity)

##### 5.11.1.1 General

The manufacturer has to meet the requirement Annex I Part I (1) by designing, developing and producing PwDEs in such a way that they ensure an appropriate level of cybersecurity based on the risks.

This requires an initial selection of appropriate controls based on the risks to be treated. If a risk can not be effectively treated by the manufacturer on his own, risk sharing can be used. Generally, the risk treatment can initially be performed independent of the essential cybersecurity requirements set out in Annex I Part I (2).

A possible way to select an initial set of controls used in this guideline will be discussed in 7

##### 5.11.1.2 Input

- List of evaluated risk, which have to be treated

##### 5.11.1.3 Control

- The manufacturer MUST select appropriate controls to treat the evaluated risks and to reduce them to an acceptable level and include the selected controls in the design of the PwDE.

##### 5.11.1.4 Output

- List of selected controls and associated risks to be included in the design of the PwDE

##### 5.11.1.5 Reference CRA

- CRA Annex I Part I (1)

5.11.2 RH_RT.1.1.2 -Select Applicable Essential Cybersecurity Requirements (Activity)

##### 5.11.2.1 General

The manufacturer also has to meet and document the applicable requirements of Annex I Part I (2) on the basis of the cybersecurity risk assessment.

This can be achieved by mapping the selected controls to the essential cybersecurity requirements of Annex I Part I (2). If a selected control addresses an essential cybersecurity requirement, this requirement is applicable.

If it is not addressed by any selected control, the manufacturer has to document and justify why the essential cybersecurity requirement is not applicable based on the associated risks.

This guideline will not contain explicit criteria when an essential cybersecurity requirement can not be applied. Nevertheless the controls set out in 7 are mapped to associated risks as well as to the corresponding essential cybersecurity requirements of Annex I Part I (2). Consequently not implemented controls from this set can be used to extrapolate a justification for non-applicable essential cybersecurity requirements.

Appendix B contains the list of essential cybersecurity requirements and subrequirements from Annex I Part I (2) for reference and can be used to generate an applicability statement.

##### 5.11.2.2 Input

- List of selected controls and associated risks to be included in the design of the PwDE

##### 5.11.2.3 Control

- The manufacturer MUST select and document applicable essential cybersecurity requirements from Annex I Part I (2) based on the selected controls.

- The manufacturer MUST document and justify any non-applicable essential cybersecurity requirements from Annex I Part I (2) based on the associated risks.

##### 5.11.2.4 Output

- List of applicable and non-applicable essential cybersecurity requirements from Annex I Part I (2)

##### 5.11.2.5 Reference CRA

- CRA Annex I Part I (2) point (a)

- CRA Annex I Part I (2) point (b)

- CRA Annex I Part I (2) point (c)

- CRA Annex I Part I (2) point (d)

- CRA Annex I Part I (2) point (e)

- CRA Annex I Part I (2) point (f)

- CRA Annex I Part I (2) point (g)

- CRA Annex I Part I (2) point (h)

- CRA Annex I Part I (2) point (i)

- CRA Annex I Part I (2) point (j)

- CRA Annex I Part I (2) point (k)

- CRA Annex I Part I (2) point (l)

- CRA Annex I Part I (2) point (m)

5.11.3 RH_RT.1.2 - Risk Sharing

5.11.3.1 RH_RT.1.2.1 -Risk Sharing with Suppliers (Activity)

###### 5.11.3.1.1 General

If the manufacturer is not able to effectively lower the risk on his own, he can use risk sharing to reduce the risk to an acceptable level. The term risk transfer can be used synonymously, but will be avoided as it is generally not possible to transfer a risk completely to a third-party as the manufacturer is still responsible for addressing the risks of the PwDE and has to exercise due diligence according to CRA Article 13 (5) when integrating components. Generally there are several ways to share risk with suppliers:

- Sharing through compliance (with CRA): If the third-party component is subject to the CRA, the manufacturer can share risks if the intended purpose and foreseeable use as well as the associated handled risks of the component are sufficient for the integration in the PwDE. Other legislation with regard to cyber security may also be suitable for risk sharing.

- Sharing through contract: If no regulation ensures that the shared risks are handled by the other party, the manufacturer can enforce the appropriate handling of risks by establishing a contract with the third-party manufacturer of the component or provider of the RDPS to meet the requirements of the CRA. This approach can be combined with existing contractual frameworks like service level agreements, underpinning contracts or data processing agreements.

Financial risk sharing in the context of an insurance for cyber security related incident can also be additionally applied, but is generally not a valid approach to meet cyber security requirements.

Note: The sharing of risks when integrating free open source software (FOSS) is uncommon, as these software projects often neither have the capacity, resources, nor the legal obligations to meet the requirements of the CRA. If the manufacturer is not able to treat the risk in relation to a FOSS component appropriately, he may rely on a third party acting as an open-source software steward providing support for the component. This will benefit the development of FOSS and can be a way to make FOSS viable for commercial usage.

###### 5.11.3.1.2 Input

- List of selected risks to share

###### 5.11.3.1.3 Control

- If sharing risks with a third-party supplier, the manufacturer MUST exercise due diligence by ensuring that the manufacturer of the integrated component is legally obliged, contractually required or otherwise able and willing to treat the risk accordingly.

###### 5.11.3.1.4 Output

- List of shared risks including the actions taken by the manufacturer to exercise due diligence

###### 5.11.3.1.5 Reference CRA

- CRA Annex I Part I (1)

5.11.3.2 RH_RT.1.2.2 -Risk Sharing with Users (Activity)

###### 5.11.3.2.1 General

Risks can also be shared with the user by providing sufficient guidance for setting up and maintaining the PwDE. In this case the manufacturer has to take into account the capabilities of the user and the infrastructure of the user. This can only be done if the shared risk meets the foreseeable expectations of the user, as the user is neither legally nor contractually obliged to share the risk.

A common expectation for the end consumer context is that the PwDE is secure by default and the secure configuration and operation of the PwDE needs minimal user interaction. For other cases assuming a professional integrator or administrator more risks might be transferred if within the expectation of the user. This also includes providing PwDEs for integration in other PwDEs.

It is also possible to extend risk sharing through several steps of the supply chain, e.g. if the PwDE integrates a third-party software using a third party RDPS which has to be explicitly enabled and agreed upon by the user in the third-party software, the manufacturer of the third-party application is able to perform risk-sharing directly with the user independent of the integrating manufacturer. This way the integrating manufacturer has to exercise due diligence when integrating the third-party software, but the usage of the third-party RDPS is purely between the user and the provider of the third-party application.

###### 5.11.3.2.2 Input

- List of selected risks to share

###### 5.11.3.2.3 Control

- If sharing the risk with the user, the manufacturer MUST ensure that the shared risks are within the foreseeable expectations of the user and that sufficient guidance documenting the risks and the expected mitigation by the user according to [USER_DOCUMENTATION] is provided.

###### 5.11.3.2.4 Output

- List of shared risks including the actions taken by the manufacturer to document shared risks

###### 5.11.3.2.5 Reference CRA

- CRA Annex I Part I (1)

5.11.4 RH_RT.1.3 -Implementation and Verification (Activity)

##### 5.11.4.1 General

The selected controls which were incorporated into the PwDE design have to be implemented accordingly to be effective. This includes all measures necessary to perform the development and production according to the design of the PwDE as well as the verification that the design is effective against the assessed risks and the implementation is correct according to specification. The verification is part of the conformity assessment required for the CRA and depends on the used module and the associated risk of the implemented control. The verification of effectiveness should at least be done on a conceptual level supported by a development process showing that the manufacturer develops and produces the PwDE correctly following the design. Generally higher risks might require additional or in depth verification.

##### 5.11.4.2 Input

- List of selected controls and associated risks to be included in the design of the PwDE

##### 5.11.4.3 Control

- The manufacturer MUST implement the selected controls and verify their effectiveness and correctness, in accordance with the associated risk.

##### 5.11.4.4 Output

- List of implemented controls and performed verification

##### 5.11.4.5 Reference CRA

- CRA Annex I Part I (1)

5.12 RH_DOC.1 -Documentation of the risk assessment (Activity)

#### 5.12.1 General

Following Article 13 (3) and (4) the cybersecurity risk assessment shall be documented and included in the technical documentation required pursuant to Article 31 and Annex VII.

Besides that, the documentation of the risk assessment is in the interest of the manufacturer as a well structured and comprehensive documentation can be reused as a basis for an update of the risk assessment. The usage of tools or templates for the documentation of the risk assessment is advisable.

#### 5.12.2 Input

Risk context * Evaluated risks * Shared risks * Implemented controls * Applicable essential cybersecurity requirements

#### 5.12.3 Control

The manufacturer MUST document the results of the risk assessment in a comprehensive manner. This includes the risk context, the evaluated risks including the corresponding implemented controls and shared risks as well as the applicable essential cybersecurity requirements.

#### 5.12.4 Output

Documentation of the risk assessment

#### 5.12.5 Reference CRA

CRA Annex I Part I (1)

5.13 RH_UPD.1 -Update Risk Assessment (Activity)

#### 5.13.1 General

The cybersecurity risk assessment has to be updated as appropriate during a defined support period according to Article 13 (3). An update is appropriate every time the existing risk assessment gets deprecated by an external or internal change in the threat context.

This is at least the case in the following events:

- Update to the PwDE with security implications

- New vulnerability becomes known

- New threats become known, e.g. new attack methods with potential impact on the PwDE.

Additionally, as not all relevant events can be monitored in all cases it is generally advisable to update the risk assessment in regular intervals.

#### 5.13.2 Input

Risk Assessment- Optional: Event influencing the risk context

#### 5.13.3 Control

The manufacturer MUST update the risk assessment when the risk context of the PwDE changes and treat new unaccepted risks accordingly.

#### 5.13.4 Output

Updated risk assessment

### 5.14 Decision Criteria

This guideline will work with decision criteria based on classification of the assets and the operational environment of the PwDE.

Decision criteria are a tool to simplify the analysis and evaluation of risks and should be defined on a on a sectorial, organisational or PwDE level. Decision criteria condense existing knowledge in risk analysis and enable a reproducible and consistent risk assessment.

The risk assessment can be performed without detailed decision criteria as this will give additional freedom in performing the risk assessment, but might result in a higher effort necessary to perform a comprehensible and consistent risk assessment.

#### 5.14.1 Impact Criteria

The impact of an incident is primarily dependent on the adversely affected assets. To estimate the potential impact of an incident the following scale will be used:

Impact:

- 1 - Negligible impact

- 2 - Small impact

- 3 - Moderate impact

- 4 - High impact

- 5 - Very high impact

The impact is estimated by selecting the base impact from the impact criteria in the following tables based on the affected assets and the type of loss in confidentiality ©, integrity (I) and availability (A). The criteria can be tailored if needed.

The base impact might not be representative based on the amount of affected Assets, in case of long time impact or other additional factors. In case an amplifier will be used in the context of this guideline a scenario/use case specific justification will be given.

Impact = BaseImpact * Amplifier

This guideline differentiates between assets to be protected and security assets required to protect the assets.

The impact of security assets is equal to impact the assets they protect, this will be implied by the impact X' with X equals C,I,A of the protected asset.

Table 1: Data Assets

| Asset | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| PII.TechnicalNecessary | 2 | 1 | 1 | Technical necessary PII is data necessary for network communication and authentication related to a person with minor impact on confidentiality, which can not be protected without loss of function. This includes IP addresses and other technical identifiers |
| PII.Generic | 3 | 2 | 3 | Generic PII with moderate impact in confidentiality, e.g. names, addresses, pictures or other |
| PII.Important | 4 | 3 | 3 | PII with a major impact on the associated person in case of information disclosure. This includes financial and health data. Note: This does not entail data, which is mixed with generic PII and can not be identified as important. |
| BusinessData.Generic | 3 | 2 | 3 | Business data with moderate impact in if business relevant data get disclosed or corrupted , e.g. metrics for controlling, internal reports or other |
| BusinessData.Important | 4 | 4 | 3 | Business data with high impact in if business relevant data get disclosed or corrupted , e.g. intellectual property, financial data, production relevant data or other |
| PII.Important (repeated row in source) | 4 | 3 | 3 | (identical to the PII.Important row above) |
| Other.Telemetric | 1 | 1 | 1 | Telemetric data containing no PII and no business relevant data have no relevant impact |
| Other.Configuration | 1 | 3 | 1 | Configuration containing no PII and no security relevant data might disturb the function of the PwDE if integrity is lost |

Table 2: Functional Assets

| Asset | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Functions.Essential | - | - | 3 | Functions of the PwDE which are required for its intended purpose and foreseeable use and whose availability has a moderate impact for the user |
| Functions.NonEssential | - | - | 1 | Functions of the PwDE which might be part of the intended purpose and foreseeable use but whose availability have a negligible impact for the user, |
| Functions.Safety | - | - | 5 | Functions of the PwDE in relation to safety whose availability have a major impact on the user |
| Functions.CommunicationNetwork | - | 3 | - | Functions of the PwDE in relation to the network might be tampered with and used to affect adjacent networks with generally more than two network peers. The base impact is estimated as moderate but can be amplified if needed. |
| Functions.CommunicationLocal | - | 2 | - | Functions of the PwDE in relation to connections with a peer in close proximity, generally this includes only one peer. The base impact is estimated as low. |

Table 3: Security Assets

| Asset | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Security.Secrets | C' / I' | C' / I' | A' | Secrets (api-keys, passwords or other) used for ensuring confidentiality or integrity of a protected asset. The confidentiality and integrity impact of a secret is equal to the impact on either the confidentiality or integrity of the protected asset depending on the security mechanism. This also applies to availability as without secrets functionalities or access to assets can not be performed. [continued on next page:] the disclosed secret. For secrets affecting the authentication to a complete network the impact 4 is assumed and for single network resources the impact 3 is taken as baseline, which can be changed based on the specific use case. |
| Security.PublicConfiguration | 1 | I' / C' | A' | Security relevant configuration, whose loss of confidentiality has no impact on the protected assets still needs to be protected in regard to integrity and availability depending on the confidentiality or integrity of the protected asset. This includes e.g. server certificates or cypher suites for cryptographic negotiation. |
| Security.Logs | C' | I' | 2 | Security relevant logs contain information which might disclose security relevant data in case of an incident or might be manipulated to hide an incident. A short term loss of availability is of minor concern. If the long term loss of availability of security relevant log data is a major concern, an amplifier can be used. |
| Security.Mechanism | - | I' / C' | A' | Security relevant functions which needs to be protected in regard to integrity and availability depending on the [text breaks off at page end; page 50 resumes mid-sentence:] consideration of attack chains or granular defence in depth strategies, as this would require assumptions of potentially broken environments or environment sensitive changes to asset impacts. |

_Source defect: Table 3's last row and the following text (presumably the end of §5.14.1 and the start of §5.14.2 "Likelihood criteria") are cut at the page break; Table 6 (Access Restriction values) is missing from §5.14.2 — numbering jumps from Table 5 to Table 7. Annex D Table 12 gives the access-restriction values (Restricted, Public Restricted, Movable, Non Restricted)._

Table 4: Indicators

| Indicator | Rationale |
|---|---|
| Interface Restriction | Restriction on interfaces decrease the likelihood for an attack. This indicator shows the maximal assumed accessibility of the PwDE. |
| Access Restriction | Access restrictions have an impact on the number of potential attackers and the possible attack windows, lessening the likelihood of a successful attack. |
| User capabilities | Unskilled users have a higher likelihood to handle the PwDE incorrectly or are more vulnerable to social engineering attacks. This indicator is only used, if the treatment of a risk depends on a user. |

Table 5: Interface Restriction

| Value | Rationale |
|---|---|
| Physical | The PwDE communicates internally and can be accessed by physical manipulation. In case of software PwDEs this entails a manipulation of the internal communication/processing of the software. Attackers need direct access to the PwDE and manipulate it internally |
| Local | The PwDE communicates a short distance via a local interface, e.g. embedded user interface, nfc or short distance wired connection. In the case of software this also includes interprocess communication with other software PwDEs on the same device. Attackers need direct local access to the PwDE. |
| Dedicated known Network | The PwDE communicates with an adjacent network known and trusted by the user without intended connection to an external network. The network is dedicated to a use case and is as such expected to consist of a limited number of PwDE only using the network for the dedicated use case, e.g. local home bus system, peer-to-peer WLAN or bluetooth connection. Attackers have to be in proximity to the PwDE to access it via the network, access from an external network is not intended |
| Known network | The PwDE communicates with an adjacent multi-purpose network known and trusted by the user which is shared with other PwDEs for multiple use cases, e.g. home or office network. Attackers have to be in proximity to the PwDE to access it via the network, access from an external network is not intended |
| External Network | The PwDE communicates with a network not under the control of the user or the organisation of the user, e.g. mobile network, WAN or unknown WLANs. Attacker can potentially access the PwDE from anywhere as the topology of the external network is not known. |

Table 7: User Capability

| Value | Rationale |
|---|---|
| Non-user-related | User Capabilities have no impact on the likelihood of an incident |
| Skilled | A skilled user, e.g. an IT professional, is not likely to expose the PwDE unnecessarily through insufficient handling and configuration and is able to enhance the security of the PwDE using his own expertise |
| Instructed | An instructed user, e.g. a craftsman or IT security savvy user who read the manual, is not likely to expose the PwDE unnecessarily through insufficient handling and configuration |
| Layman | A not particular skilled user is likely to expose the PwDE unnecessarily through insufficient handling and configuration |

#### 5.14.3 Acceptance Criteria

A risk can be classified and evaluated based on its likelihood and potential impact.

This guideline will use the following criteria for acceptance of risks:

- The risk for a moderate or higher impact of a local attack is not acceptable, if the access restrictions do not prevent the local access to potentially malicious actors with the capability to perform low complexity attacks.

- The risk for a high or higher impact of a local attack is not acceptable, if the access restrictions do not prevent local access to a known but potentially malicious group of actors with the capability to perform high complexity attacks.

- The risk for a moderate or higher impact of a network attack is not acceptable, if the network restrictions do not prevent the access to a unknown group of potentially malicious actors with the capability to perform low complexity attacks.

- The risk for a high or higher impact of a network attack is not acceptable, if the network restrictions do not prevent network access to a known limited group potentially malicious actors with the capability to perform high complexity attacks.

- The risk for a moderate or higher impact based on an initial misconfiguration of the PwDE is not acceptable, if the user is a layman.

- The risk for a high or very high impact based on an initial misconfiguration of the PwDE is not acceptable, if the user is an instructed tradesmen but not a skilled expert.

These acceptance criteria are understood as an initial baseline and have to tailored based on the product specific use case and sectorial best practices.

### 5.15 Risk handling in practice

Risk handling requires experience and is dependent on the PwDE and the persons involved as such it is not really feasible to describe risk handling in a way that detailed enough to be helpful but generic enough to be applicable to all PwDEs.

This guideline contains a simple example in Annex D which can be used as an initial guidance for manufacturers without existing risk handling.

## 6 Working with Adaptable Risk-based Controls (ARC)

This technical guideline will use an approach called "Adaptable Risk-based Controls" (ARC) for selecting appropriate controls based on the associated risks. For this reason ARCs are always accompanied by one or more risk scenarios.

### 6.1 Risk Scenarios

A risk scenario contains the following information:

- Risk Scenario: Prose describing the risk scenario

- Assets: Affected Assets and Impact

- Environment: Environment parameters (Access Restriction, Interface Restriction, User Capabilities)

### 6.2 Matching a Risk Scenario

Whether a risk applies to the PwDE can be evaluated following these steps:

- 1. Perform the risk assessment as described in risk handling.

- 2. Categorize the assets identified according to the impact criteria and the environment the component of the PwDE handling the asset is in. This will result in a mapping from asset to base impact in confidentiality, integrity and availability and corresponding environment.

- 3. Separate the PwDE into different environments. Following the likelihood criteria the environment is a tuple of access restriction, user capability and interface restriction. Note the tuple describing the environment. This can be started on a component basis and refined on an interface and functions basis later on. For RDPS under its responsibility the manufacturer is able to choose the environment it is willing to provide for the operation of the RDPS.

- 4. Select the controls based on the assets, impact and environment parameters given in the risk scenario of the control. A risk applies to the PwDE or part thereof if

- the PwDE or part thereof handles or otherwise influences one or more asset with at least the impact listed in the risk scenario, and

- the PwDE or part thereof expects one of the access and communicative restriction as well as the user capability listed in the environment. If more than one value is given for an environment parameter, at least one must match. "*" matches any value.

### 6.3 Recommended Workflow

To keep the approach simple this guideline recommends a rough top-down-approach with refinement if needed, as it is neither feasible nor reliable to start with a detailed selection of controls. Follow this process

- 1. Identify high-level assets and environments of the PwDE or components of the PwDE and generate a combined risk profile consisting of

- Highest Impact in C/I/A of all identified assets

- Combination of all environments, e.g. interface restriction: local, remote network. This will match all controls with an interface restriction of local, remote network or *.

- 2. Select all controls based on combined risk profile

- 3. Try to implement selected control

- 4. If a control can not be feasibly implemented everywhere, revaluate and refine the risk profile in scope of the part of the PwDE where the control can not be implemented. e.g. a control for remote network interface might not be able to implement on a local interface, consequently split up the risk profile in the environment for the local interface and an environment for the rest of the PwDE

- 5. Reevaluate the asset list for new assets after implementing all controls

This approach will lead to more implemented controls than minimally necessary, but is more straight forward and more resilient to yet unknown risks.

### 6.4 Working with predefined risk profiles

To simplify the risk assessment predefined risk profiles may be used. These risk profiles contain a predefined list of assets and environment based on an intended purpose or foreseeable use as well as preselected controls.

Generally it is not possible to completely skip the risk assessment as the risk profile also has to be evaluated based on the PwDE in scope and potentially extended with PwDE specific risks, but the risk profile sets an initial baseline which can be customized as needed.

Predefined risk profiles come with a list of preselected controls and can be used as follows:

- 1. Choose appropriate profile closely resembling the intended purpose and foreseeable use of the PwDE

- 2. Apply profile and controls following the workflow described in 6.3

- 3. Reevaluate assets and environments set out in the predefined risk profile and add missing risk, based on assets and environments

- 4. Enhance predefined profile with appropriate controls for added risks

### 6.5 Example

Example: A PwDE handling generic PIIs for the consumer market and indoor use with a RDPS operated by the manufacturer. The RDPS stores a huge amount of PII data sets.

Environment

A placed component with a layman consumer, restricted indoor access and connected to a remote network, resulting in (Layman, Restricted, External network) environment.

A RDPS component with a professional it operation, in a restricted data center and connected to a remote network, resulting in (Skilled, Restricted, External network) environment.

Impact categorisation

The placed component in the (Layman, Restricted, Network) environment handles PII.Generic with an impact of Confidentiality:3/Integrity:2/Availability:2.

The RDPS component in the (Layman, Restricted, Network) environment handles PII.Generic with an impact of Confidentiality:3/Integrity:2/Availability:2. As many data sets might be affected, an amplifier of 1 will be used resulting in Confidentiality:4/Integrity:3/Availability:3.

Selection of controls

Assume the following control:

Automatic Update Mechanism (Mechanism)

Risk Scenario: The PwDE handles assets with moderate or higher impact which can not be protected if PwDE integrity is lost. The user is a layman not installing updates in regular intervals leaving the PwDE vulnerable to attack via external networks.

Assets:

- C(3)

- I(3)

- A(3)

Environment:

- Access Restriction: *

- Interface Restriction: External network

- User Capabilities: Layman

Control:

The update mechanism of the PwDE MUST include an automatic update mechanism able to check for new updates automatically.

Based on the parameters the control can be selected for different environments:

"Automatic Update Mechanism" does apply to PwDE handling assets with an impact of at least 3 over an external network without a skilled user. Consequently it applies in general to the exemplary PwDE handling generic PII and using a remote network access.

As the control also expects a layman user it only applies to the components of the PwDE administered by the Layman and not the RDPS component as it is operated in a skilled environment. This applies to many security by default controls.

6.6 Rationale on ARCs ARCs are an approach to select controls applicable to cybersecurity appropriate to the use case of the PwDE. There are two aspects affecting the appropriateness of cybersecurity:

- What must be protected?

- This is defined by the assets identified in asset identification and their potential impact. Following the impact categorization described step 2, an indicator for the amount of protection for confidentiality, integrity and availability can be derived.

- What must be protected against?

- This is defined by the threats identified in threat analysis and the likelihood of their occurrence. The categorization of assets into different impact classes also generates three generic threats, i.e. loss of confidentiality, loss of integrity and loss of availability. This also includes the likelihood of occurrence of these threats as the impact has a direct relation to the motivation and consequently the potential capability of a malicious actors.

- If nothing else is known about the PwDE the worst case can be assumed, i.e. that all three threats apply and are likely relative to their potential impact. Generally this is not the case as based on the environment the PwDE already has some level of protection and thus a reduced likelihood of an incident based on existing access restrictions, communicative restrictions or other security controls already realized and expected by the environment. A special environmental factor is the user capability, as a high user capability indicates an environment with mature administrative controls in place and the expected capability to set up certain restrictions or other technical/physical controls. Although not malicious an unskilled user will require additional support for the secure operation of the PwDE.

Environments can be used for composition of components of the PwDE. A component of the PwDE can expect an environment the manufacturer has provided when integrating the component. The manufacturer has to provide the expected environment in full or can delegate the expectation to the next user in the supply chain. If this is done, the manufacturer has to enable the next user to meet the expectations. This does at least include a transparent description of the delegated expectations as well as the means to meet the expectations, e.g. a configuration interface if some additional configuration is expected.

- Figure 5: Composition of environments

In regards to the assessment of this technical guideline the composite property can be used for a top- down-approach, if the evaluator assumes that a control is not necessary or even detrimental for a part of the PwDE, e.g. an interface, an application or a function of the PwDE the evaluator can scope the used environment and assets specifically to that part of the PwDE and reevaluate the control.

## 7 PwDE Controls

This guideline defines an initial set of controls for PwDE security and vulnerability handling that are commonly used in order to ensure the cybersecurity of a PwDE.

These controls are generic and designed to be applicable for a wide range of PwDEs and are consequently rather high-level with the intent for further specification by the manufacturer depending on the use case and the specific type of PwDE.

The cybersecurity controls of this technical guideline are defined in the machine-readable format OSCAL in order to

- provide the capability for filtering the appropriate controls depending on the use case

- simplify the reuse of existing controls and definition of custom control catalogs

- establish a structured format for documentation and assessment of the implemented controls

The OSCAL controls are provided via the Github-Repository: https://github.com/tr-03183/tr-03183-1

Access in conjunction with additional information on the usage of the repository and OSCAL will be provided upon request to tr-03183@bsi.bund.de.

_The control catalogue itself is published only as OSCAL in a GitHub repository with access on request (tr-03183@bsi.bund.de); it is not part of the PDF and was not available to this extraction._

## Appendix B — Essential Cybersecurity Requirements (CRA Annex I quoted, BSI sub-ids)

| Requirement ID | CRA Reference | Requirement |
|---|---|---|
| ER.0 | Annex I Part I 1 | products with digital elements shall be designed, developed and produced in such a way that they ensure an appropriate level of cybersecurity based on the risks. |
| ER.1 | Annex I Part I 2 Point a | be made available on the market without known exploitable vulnerabilities; |
| ER.2 | Annex I Part I 2 Point b | be made available on the market with a secure by default configuration, unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements |
| ER.3a | Annex I Part I 2 Point b | including the possibility to reset the PwDE to its original state; |
| ER.4 | Annex I Part I 2 Point c | ensure that vulnerabilities can be addressed through security updates, |
| ER.4a | Annex I Part I 2 Point c | including, where applicable, through automatic security updates that are installed within an appropriate timeframe enabled as a default setting, |
| ER.4b | Annex I Part I 2 Point c | with a clear and easy-to-use opt-out mechanism, |
| ER.4c | Annex I Part I 2 Point c | through the notification of available updates to users, |
| ER.4d | Annex I Part I 2 Point c | and the option to temporarily postpone them; |
| ER.5 | Annex I Part I 2 Point d | ensure protection from unauthorised access by appropriate control mechanisms, |
| ER.5a | Annex I Part I 2 Point d | including but not limited to authentication, identity or access management systems, |
| ER.5b | Annex I Part I 2 Point d | and report on possible unauthorised access; |
| ER.6 | Annex I Part I 2 Point e | protect the confidentiality of stored, transmitted or otherwise processed data, personal or other, such as by encrypting relevant data at rest or in transit by state of the art mechanisms, and by using other technical means; |
| ER.7 | Annex I Part I 2 Point f | protect the integrity of stored, transmitted or otherwise processed data, personal or other, commands, programs and configuration against any manipulation or modification not authorised by the user, and report on corruptions; |
| ER.9 | Annex I Part I 2 Point h | protect the availability of essential and basic functions, also after an incident, |
| ER.9a | Annex I Part I 2 Point h | including through resilience and mitigation measures against denial-of-service attacks; |
| ER.10 | Annex I Part I 2 Point i | minimise the negative impact by the PwDEs themselves or connected devices on the availability of services provided by other devices or networks; |
| ER.11 | Annex I Part I 2 Point j | be designed, developed and produced to limit attack surfaces, |
| ER.11a | Annex I Part I 2 Point j | including external interfaces; |
| ER.12 | Annex I Part I 2 Point k | be designed, developed and produced to reduce the impact of an incident using appropriate exploitation mitigation mechanisms and techniques; |
| ER.13 | Annex I Part I 2 Point l | provide security related information by recording and monitoring relevant internal activity, |
| ER.13a | Annex I Part I 2 Point l | including the access to or modification of data, services or functions, |
| ER.13b | Annex I Part I 2 Point l | with an opt-out mechanism for the user; |
| ER.14 | Annex I Part I 2 Point m | provide the possibility for users to securely and easily remove on a permanent basis all data and settings and, |
| VH.1 | Annex I Part II 1 | identify and document vulnerabilities and components contained in products with digital elements, |
| VH.1a | Annex I Part II 1 | including by drawing up a software bill of materials in a commonly used and machine-readable format covering at the very least the top-level dependencies of the PwDEs; |
| VH.2a | Annex I Part II 2 | in relation to the risks posed to products with digital elements, address and remediate vulnerabilities without delay, including by providing security updates; where technically feasible, new security updates shall be provided separately from functionality updates; |
| VH.3 | Annex I Part II 3 | apply effective and regular tests and reviews of the security of the product with digital elements; |
| VH.4 | Annex I Part II 4 | once a security update has been made available, share and publicly disclose information about fixed vulnerabilities, including a description of the vulnerabilities, information allowing users to identify the product with digital elements affected, the impacts of the vulnerabilities, their severity and clear and accessible information helping users to remediate the vulnerabilities; in duly justified cases, where manufacturers consider the security risks of publication to outweigh the security benefits, they may delay making public information regarding a fixed vulnerability until after users have been given the possibility to apply the relevant patch; |
| VH.5 | Annex I Part II 5 | put in place and enforce a policy on coordinated vulnerability disclosure; |
| VH.6 | Annex I Part II 6 | take measures to facilitate the sharing of information about potential vulnerabilities in their product with digital elements as well as in third-party components contained in that PwDE, |
| VH.6a | Annex I Part II 4 | including by providing a contact address for the reporting of the vulnerabilities discovered in the product with digital elements; |
| VH.7 | Annex I Part II 7 | provide for mechanisms to securely distribute updates for products with digital elements to ensure that vulnerabilities are fixed or mitigated in a timely manner and, |
| VH.7a | Annex I Part II 7 | where applicable for security updates, in an automatic manner; |
| VH.8 | Annex I Part II 8 | ensure that, where security updates are available to address identified security issues, they are disseminated without delay and, |
| VH.8a | Annex I Part II 8 | unless otherwise agreed between a manufacturer and a business user in relation to a tailor-made product with digital elements, free of charge, accompanied by advisory messages providing users with the relevant information, including on potential action to be taken. |

_Source defects in Appendix B: no ER.3 (only ER.3a); no ER.8 (CRA Annex I Part I 2 point g, data minimisation, is missing); ER.14 ends at 'and,' with no ER.14a; no VH.2 (only VH.2a); VH.6a is referenced 'Annex I Part II 4' but is Part II point 6; heading 'B.1 A.1 Essential Cybersecurity Requirements Part I' while Part II is also in B.1; table captions carry a stray apostrophe._

## Annex D — Risk Scoring (experimental)

Table 11: Values for interface restriction (Base / Factor)

| Value | Base | Factor |
|---|---|---|
| Physical | 10% | 38% |
| Local | 20% | 55% |
| Dedicated known Network | 40% | 70% |
| Known network | 50% | 80% |
| External Network | 100% | 100% |

Table 12: Values for access restriction

| Value | Rationale | Base | Factor |
|---|---|---|---|
| Restricted | The access to the PwDE is restricted, only a group of known people have access to the PwDE. | 10% | 42% |
| Public Restricted | Public access is intended or unavoidable, but the PwDE is normally supervised by an authorized person. The window for an attack is generally limited. | 20% | 58% |
| Movable | Public access is intended or unavoidable, but the PwDE is normally supervised by an authorized person. The PwDE is movable and can be removed by an attacker. The window for an attack is generally limited, but can be extended by moving the object. | 50% | 81% |
| Non Restricted | No particular access restriction, there is no limitation on potential attacker and attack window. This also applies if the local access is restricted, but the attack can be executed without local access. | 100% | 100% |

Table 13: Values for user capabilities

| Value | Base | Factor |
|---|---|---|
| Non-user-related | 100% | 100% |
| Skilled | 20% | 58% |
| Instructed | 50% | 81% |
| Layman | 100% | 100% |

Formula (D.1): `environment = round(1 + interface restrictions * access restriction * user capability) * 4`; factor derivation `factor = Log_f( (b*(f-1))+1)` with f =(number of factors)^2.

_Source defect: as printed, round(1 + x) * 4 for factors in (0,1] yields 4 or 8, not the 1–5 "Environment" scale of the D.2 matrix; the intended form is presumably round(1 + x * 4). Recorded, not corrected._

D.2 risk matrix (Risk Classification 1 Very Low … 5 Very high; "Every Low and Very Low Risk can be accepted, every other risk has to be treated.")

NOTE (Annex D.2, verbatim; added by the verify pass — R-0030, R-0044, R-0045):

> The acceptance criteria are a tool for quick decision making, but not a substitute for a rationalized decision-making process. Generally when accepting a risk the decision must be comprehensibly justified and documented. Generally risks classified as moderate have to be treated during the course of development, but can be accepted in post-market if the effort of treatment is not in relation with the potential risk and the remaining PwDE lifetime. High and very high risks are generally not acceptable and have to be treated.

| Environment | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
|---|---|---|---|---|---|
| Environment 5 | 1 | 1 | 1 | 2 | 3 |
| Environment 4 | 1 | 1 | 2 | 3 | 3 |
| Environment 3 | 2 | 2 | 3 | 4 | 4 |
| Environment 2 | 2 | 3 | 4 | 4 | 5 |
| Environment 1 | 2 | 3 | 4 | 5 | 5 |

