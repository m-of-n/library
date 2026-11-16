---
record: etsi-en-304-223
kind: normative
title: "etsi-en-304-223 — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every quotation below is a `<!-- q Lx-y -->` marker whose words `bin/check-quotes --render`
wrote from the pinned pdftotext rendering, and `bin/check-quotes` verifies. `bin/fx1-skeleton`
wrote the sentences that carry a verbal form of the directives, each followed by its
requirement id. Pass 1 (requirements lane) added the keyword-less text that decides how they
apply: the Clause 1 scope, the empty normative-references clause, the §3.1 definitions the
provisions use, the definition cells of Table 4-1, each principle's title and applicability
line (the line that opens it, naming the stakeholders primarily responsible, e.g. L517), and
the keyword-less sentences inside provisions, each with a note on its status. The References
line under each principle is an informative signpost (Introduction, L195-198) and is not carried.

Under a quotation: the requirement id, `split into` the ids of its split_of children, the
normativity where it is not a requirement or recommendation, or `no entry` with the reason.
SD-n is a defect in the Source defects section at the end. Each Provision paragraph is also an
entry of its own, id `etsi-en-304-223#<designator>` (e.g. `etsi-en-304-223#5.1.1-1`), whose
sentences are the R-ids shown under its quotations.

## §1

<!-- q L226-226 "The present document" .. "models and systems." -->
> The present document defines baseline security requirements for AI models and systems.

R-0093 · applicability · verb none, C-0021

<!-- q L226-227 "The present document includes" .. "as generative AI." -->
> The present document includes in its scope systems that incorporate deep neural networks, such as generative AI.

R-0094 · applicability · verb none

<!-- q L227-230 "For consistency, the" .. "of the provisions." -->
> For consistency, the term "AI systems" is used throughout the present document when framing the scope of provisions and the term "AI security", which is considered a subset of cybersecurity, is used when addressing any cybersecurity issues in the scope of the provisions.

R-0095 · convention · verb none, C-0022

<!-- q L230-231 "The present document" .. "to be deployed)." -->
> The present document is not designed for academics who are creating and testing AI systems only for research purposes (AI systems which are not going to be deployed).

R-0096 · applicability · verb none, C-0023

## §2.1

<!-- q L248-250 -->
> The following referenced documents are necessary for the application of the present document. Not applicable.

no entry: §2.1 lists no normative references, so conformance needs no other document; every [i.n] in §2.2 is informative (C-0026, rejected).

## §3.1

<!-- q L341-342 -->
> adversarial attack: attempt to manipulate an AI model by introducing specially crafted inputs to cause the model to produce errors or unintended outcomes

used by R-0014.

<!-- q L344-345 -->
> AI system: engineered system that generates outputs such as content, forecasts, recommendations or decisions for a given set of human-defined objectives

used by 21 leaf entries.

<!-- q L347-348 -->
> Application Programming Interface (API): set of tools and protocols that allow different software systems to communicate and interact

used by R-0045, R-0046, R-0085.

<!-- q L350-351 -->
> data poisoning: type of adversarial attack where malicious data is introduced into training datasets to compromise the AI system's performance or behaviour

used by R-0023, R-0063, R-0087.

<!-- q L353-354 -->
> guardrails: predefined constraints or rules implemented to control and limit an AI system's outputs and behaviours, ensuring safety, reliability, and alignment with ethical or operational guidelines

used by R-0061.

<!-- q L377-378 -->
> model inversion: privacy attack where an adversary infers sensitive information about the training data by analysing the AI model's outputs

used by R-0023.

<!-- q L392-392 -->
> prompt: input provided to an AI model, often in the form of text, that directs or guides its response

used by R-0016, R-0065.

<!-- q L396-397 -->
> risk assessment: process of identifying, analysing and mitigating potential threats to the security or functionality of an AI system

used by R-0017, R-0020, R-0055.

<!-- q L399-400 -->
> sanitisation: process of cleaning and validating data or inputs to remove errors, inconsistencies and malicious content, ensuring data integrity and security

used by R-0042.

<!-- q L402-403 -->
> system prompt: predefined input or set of instructions provided to guide the behaviour of an AI model, often used to define its tone, rules, or operational context

used by R-0065.

<!-- q L405-406 -->
> threat modelling: process to identify and address potential security threats to a system during its design and development phases

used by R-0023, R-0024, R-0112.

<!-- q L408-409 -->
> training: process of teaching an AI model to recognize patterns, make decisions, or generate outputs by exposing it to labelled data and adjusting its parameters to minimize errors

Every leaf in §5.1.1 using the word means staff training: R-0007, R-0008, R-0011, R-0104 (SD-5).

<!-- q L411-411 -->
> training data: data used to train a machine learning model

used by R-0041, R-0044, R-0049, R-0061, R-0063, R-0064, R-0071, R-0090.

## §4

<!-- q L433-433 "The present clause defines" .. "AI supply chain." -->
> The present clause defines the stakeholder groups that form the AI supply chain.

no entry: describes the clause (C-0032, rejected).

<!-- q L433-434 "An indication is" .. "for its implementation." -->
> An indication is given for each principle on which stakeholders are primarily responsible for its implementation.

R-0097 · applicability · verb none

<!-- q L434-436 "A single entity" .. "different regulatory regimes." -->
> A single entity can hold multiple stakeholder roles, as defined in the present document, in addition to any responsibilities arising from different regulatory regimes.

R-0001 · possibility (can): no provision

<!-- q L438-440 -->
> EXAMPLE: Under data protection law, when processing personal data, organizations can have a role of controller and/or joint controller and/or processor, depending on their role in creating and setting up AI systems.

no entry: EXAMPLE, informative (C-0033, rejected).

<!-- q L442-442 "All stakeholders included" .. "data protection obligations." -->
> All stakeholders included in Table 4-1 should note that they can have data protection obligations.

R-0002 · split into R-0098 (should), R-0099 (can)

<!-- q L442-443 "Additionally, senior leaders" .. "infrastructure." -->
> Additionally, senior leaders in an organization also have responsibilities to help protect their staff and infrastructure.

no entry: senior leaders are not a Table 4-1 role and no verbal form binds them.

<!-- q L443-444 "Some provisions for" .. "involving open-source models." -->
> Some provisions for Developers in the present document are less applicable to AI systems involving open-source models.

R-0100 · applicability · verb none

<!-- q L444-445 "Further information and" .. "104 128 [i.1]." -->
> Further information and guidance about different types of AI systems can be found in ETSI TR 104 128 [i.1].

R-0003 · possibility (can): no provision

<!-- q L447-447 -->
> Table 4-1: Stakeholder definition

Definition cells only below: each marker is anchored past the stakeholder-name cell, so no quotation welds the two columns (the -layout rendering puts both on one line).

<!-- q L449-458 "This encompasses" .. "System Operator." -->
> This encompasses any type of business or organization across any sector as well as individuals that are responsible for creating or adapting an AI model and/or system. This applies to all AI technologies, including proprietary and open-source models. For context, a business or organization that creates an AI model and who is also responsible for embedding/deploying that model/system in their organization are defined in the present document to be both a Developer and a System Operator.

Developers row. Its last sentence classes the create-and-deploy organization as both roles (R-0128).

<!-- q L459-461 -->
> Developers can be AI providers under the EU AI Act [i.2], when putting a system into service or placing it on the market.

R-0004 · possibility (can): no provision

<!-- q L462-470 "This includes" .. "business purposes." -->
> This includes any type of business or organization across any sector that has responsibility for embedding/deploying an AI model and system within their infrastructure and/or its ongoing maintenance. This applies to all AI technologies, including proprietary and open-source models. This term also includes those businesses that provide a contractual service to organizations to embed/deploy an AI model and system for business purposes.

System Operators row.

<!-- q L471-473 -->
> System operators can be deployers under the EU AI Act [i.2] and can also be AI providers if they make changes to the system.

R-0005 · split into R-0101 (can), R-0102 (can) · possibility (can): no provision

<!-- q L474-485 "This includes" .. "other sources." -->
> This includes any type of business, organization or individual that controls data permissions and the integrity of data that is used for any AI model or system to function. This stakeholder group also includes those entities that set the policies for how data is used and managed for an AI model and/or system. In the context of an AI system, there could be multiple data custodians involved because some data used to create a model could come from the organization that is deploying/embedding the system in their infrastructure and other data could be from public databases and other sources.

Data Custodians row (C-0034 and C-0035, rejected as definitions; the first welds this row's name cell to its first sentence).

<!-- q L486-494 "This encompasses" .. "end-users." -->
> This encompasses any employee within an organization or business and consumers who use an AI model and system for any purpose, including to support their work and day-to-day activities. This applies to all AI technologies and both proprietary and open-source models. This stakeholder group has been created because the voluntary Code has placed expectations on Developers, System Operators and Data custodians to help inform and protect end-users.

End-users row (SD-9).

<!-- q L504-508 "Encompasses" .. "application." -->
> Encompasses all individuals and technologies, such as apps and autonomous systems, that are not directly affected by AI systems or decisions based on the output of AI systems. These individuals do not necessarily interact with the deployed system or application.

Affected entities row (SD-10; C-0036, rejected as a definition).

## §5.1

<!-- q L515-515 -->
> 5.1 Secure Design

## §5.1.1

<!-- q L516-516 -->
> 5.1.1 Principle 1: Raise awareness of AI security threats and risks

<!-- q L517-517 -->
> Primarily applies to: System Operators, Developers, and Data Custodians

R-0103 · applicability · verb none

<!-- q L521-522 -->
> Provision 5.1.1-1 Organizations' cyber security training programme shall include AI security content which shall be regularly reviewed and updated, such as if new substantial AI-related security threats emerge.

R-0006 · split into R-0104 (shall), R-0105 (shall)

<!-- q L524-524 -->
> Provision 5.1.1-1.1 AI security training shall be tailored to the specific roles and responsibilities of staff members.

R-0007

<!-- q L526-527 "Provision 5.1.1-2 As" .. "that are AI-related." -->
> Provision 5.1.1-2 As part of an Organization's wider staff training programme, they shall require all staff to maintain awareness of the latest security threats and vulnerabilities that are AI-related.

R-0008

<!-- q L527-528 "Where available, this" .. "include proposed mitigations." -->
> Where available, this awareness shall include proposed mitigations.

R-0009

<!-- q L530-531 "Provision 5.1.1-2.1 These" .. "internal knowledge-sharing platforms." -->
> Provision 5.1.1-2.1 These updates should be communicated through multiple channels, such as security bulletins, newsletters, or internal knowledge-sharing platforms.

R-0010

<!-- q L531-532 "This will ensure" .. "the staff." -->
> This will ensure broad dissemination and understanding among the staff.

no entry: rationale for R-0010 (C-0037, rejected).

<!-- q L534-536 -->
> Provision 5.1.1-2.2 Organizations shall provide developers with training in secure coding and system design techniques specific to AI development, with a focus on preventing and mitigating security vulnerabilities in AI algorithms, models, and associated software.

R-0011

## §5.1.2

<!-- q L539-540 -->
> 5.1.2 Principle 2: Design the AI system for security as well as functionality and performance

<!-- q L541-541 -->
> Primarily applies to: System Operators and Developers

R-0106 · applicability · verb none

<!-- q L545-547 -->
> Provision 5.1.2-1 As part of deciding whether to create an AI system, a System Operator and/or Developer shall conduct a thorough assessment that includes determining and documenting the business requirements and/or problem they are seeking to address, along with associated AI security risks and mitigation strategies.

R-0012

<!-- q L549-550 -->
> Provision 5.1.2-1.1 Where the Data Custodian is part of a Developer's organization, they shall be included in internal discussions when determining the requirements and data needs of an AI system.

R-0013

<!-- q L552-553 -->
> Provision 5.1.2-2 Developers and System Operators shall ensure that AI systems are designed and implemented to withstand adversarial AI attacks, unexpected inputs and AI system failure.

R-0014

<!-- q L555-556 "Provision 5.1.2-3 To" .. "the AI system." -->
> Provision 5.1.2-3 To support the process of preparing data, security auditing and incident response for an AI system, Developers shall document and create an audit trail in relation to the AI system.

R-0015

<!-- q L556-557 "This shall include" .. "into the system." -->
> This shall include the operation, and lifecycle management of models, datasets and prompts incorporated into the system.

R-0016

<!-- q L559-561 -->
> Provision 5.1.2-4 If a Developer or System Operator uses an external component, they shall conduct an AI security risk assessment and due diligence process in line with their existing software development processes, that assesses AI specific risks.

R-0017

<!-- q L570-571 -->
> Provision 5.1.2-5 Data Custodians shall ensure that the intended usage of the system is appropriate to the sensitivity of the data it was trained on as well as the controls intended to ensure the security of the data.

R-0018

<!-- q L573-574 -->
> Provision 5.1.2-5.1 Organizations should ensure that employees are encouraged to proactively report and identify any potential security risks in AI systems and ensure appropriate safeguards are in place.

R-0019

<!-- q L576-578 -->
> Provision 5.1.2-6 Where the AI system will be interacting with other systems or data sources, (be they internal or external), Developers and System Operators shall ensure that the permissions granted to the AI system on other systems are only provided as required for functionality and are risk assessed.

R-0020

<!-- q L580-581 -->
> Provision 5.1.2-7 If a Developer or System Operator chooses to work with an external provider, they shall undertake a due diligence assessment and should ensure that the provider is adhering to the present document.

R-0021 · split into R-0107 (shall), R-0108 (should)

## §5.1.3

<!-- q L584-585 -->
> 5.1.3 Principle 3: Evaluate the threats and manage the risks to the AI system

<!-- q L586-586 -->
> Primarily applies to: Developers and System Operators

R-0109 · applicability · verb none

<!-- q L590-590 -->
> Provision 5.1.3-1 Developers and System Operators shall analyse threats and manage security risks to their systems.

R-0022

<!-- q L591-592 -->
> Threat modelling should include regular reviews and updates and address AI-specific attacks, such as data poisoning, model inversion, and membership inference.

R-0023

<!-- q L594-595 -->
> Provision 5.1.3-1.1 The threat modelling and risk management process shall be conducted to address any security risks that arise when a new setting or configuration option is implemented or updated at any stage of the AI lifecycle.

R-0024

<!-- q L597-598 "Provision 5.1.3-1.2 Developers" .. "to increased risk." -->
> Provision 5.1.3-1.2 Developers shall manage the security risks associated with AI models that provide superfluous functionalities, where increased functionality leads to increased risk.

R-0025

<!-- q L598-599 "For example, where" .. "system function." -->
> For example, where a multi-modal model is being used but only single modality is used for system function.

no entry: example for R-0025 (C-0038, rejected).

<!-- q L601-602 -->
> Provision 5.1.3-1.3 System Operators shall apply controls to risks identified through the analysis based on a range of considerations, including the cost of implementation in line with their corporate risk tolerance.

R-0026

<!-- q L604-605 "Provision 5.1.3-2 Where" .. "model their systems." -->
> Provision 5.1.3-2 Where AI security threats are identified that cannot be resolved by Developers, this shall be communicated to System Operators so they can threat model their systems.

R-0027 · split into R-0110 (cannot), R-0111 (shall), R-0112 (can)

<!-- q L605-606 "System Operators shall" .. "of these threats." -->
> System Operators shall communicate this information to End-users, so they are made aware of these threats.

R-0028

<!-- q L606-607 "This communication should" .. "monitor these threats." -->
> This communication should include detailed descriptions of the risks, potential impacts, and recommended actions to address or monitor these threats.

R-0029

<!-- q L609-610 -->
> Provision 5.1.3-3 Where an external entity has responsibility for AI security risks identified within an organizations infrastructure, System Operators should attain assurance that these parties are able to address such risks.

R-0030

<!-- q L612-613 "Provision 5.1.3-4 Developers" .. "to risk appetite." -->
> Provision 5.1.3-4 Developers and System Operators should continuously monitor and review their system infrastructure according to risk appetite.

R-0031

<!-- q L613-614 "It is important" .. "against them." -->
> It is important to recognize that a higher level of risk will remain in AI systems despite the application of controls to mitigate against them.

no entry: statement on residual risk closing Provision 5.1.3-4 (R-0031); no verbal form of the directives.

## §5.1.4

<!-- q L617-617 -->
> 5.1.4 Principle 4: Enable human responsibility for AI systems

<!-- q L618-618 -->
> Primarily applies to: Developers and System Operators

R-0113 · applicability · verb none

<!-- q L622-623 -->
> Provision 5.1.4-1 When designing an AI system, Developers and/or System Operators should incorporate and maintain capabilities to enable human oversight.

R-0032

<!-- q L625-626 -->
> Provision 5.1.4-2 Developers should design systems to make it easy for humans to assess outputs that they are responsible for in said system (such as by ensuring that models outputs are explainable or interpretable).

R-0033

<!-- q L628-629 -->
> Provision 5.1.4-3 Where human oversight is a risk control, Developers and/or System Operators shall design, develop, verify and maintain technical measures to reduce the risk through such oversight.

R-0034

<!-- q L631-632 -->
> Provision 5.1.4-4 Developers should verify that the security controls specified by the Data Custodian have been built into the system.

R-0035

<!-- q L641-642 -->
> Provision 5.1.4-5 Developers and System Operators should make End-users aware of prohibited use cases of the AI system.

R-0036

## §5.2

<!-- q L645-645 -->
> 5.2 Secure Development

## §5.2.1

<!-- q L646-646 -->
> 5.2.1 Principle 5: Identify, track and protect the assets

<!-- q L647-647 -->
> Primarily applies to: Developers, System Operators and Data Custodians

R-0114 · applicability · verb none

<!-- q L651-652 -->
> Provision 5.2.1-1 Developers, Data Custodians and System Operators shall maintain a comprehensive inventory of their assets (including their interdependencies/connectivity).

R-0037

<!-- q L654-656 -->
> Provision 5.2.1-2 As part of broader software security practices, Developers, Data Custodians and System Operators shall have processes and tools to track, authenticate, manage version control and secure their assets due to the increased complexities of AI specific assets.

R-0038

<!-- q L658-659 -->
> Provision 5.2.1-3 System Operators shall develop and tailor their disaster recovery plans to account for specific attacks aimed at AI systems.

R-0039

<!-- q L661-661 -->
> Provision 5.2.1-3.1 System Operators should ensure that a known good state can be restored.

R-0040 · split into R-0115 (should), R-0116 (can)

<!-- q L663-664 -->
> Provision 5.2.1-4 Developers, System Operators, Data Custodians and End-users shall protect sensitive data, such as training or test data, against unauthorized access (see clause 5.2.3 for details on securing data).

R-0041

<!-- q L666-668 "Provision 5.2.1-4.1 Developers," .. "inputs are stored." -->
> Provision 5.2.1-4.1 Developers, Data Custodians and System Operators shall apply checks and sanitisation to data and inputs when designing the model based on their access to said data and inputs and where those data and inputs are stored.

R-0042

<!-- q L668-668 "This shall be" .. "or continuous learning." -->
> This shall be repeated when model revisions are made in response to user feedback or continuous learning.

R-0043

<!-- q L668-669 "See clause 5.2.2" .. "open source." -->
> See clause 5.2.2 for relevant provisions for open source.

no entry: cross-reference closing Provision 5.2.1-4.1 that finds nothing (SD-8).

<!-- q L671-672 -->
> Provision 5.2.1-4.2 Where training data or model weights could be confidential, Developers shall put proportionate protections in place.

R-0044

## §5.2.2

<!-- q L675-675 -->
> 5.2.2 Principle 6: Secure the infrastructure

<!-- q L676-676 -->
> Primarily applies to: Developers and System Operators

R-0117 · applicability · verb none

<!-- q L680-681 -->
> Provision 5.2.2-1 Developers and System Operators shall evaluate their organization's access control frameworks and identify appropriate measures to secure APIs, models, data, and training and processing pipelines.

R-0045

<!-- q L683-684 "Provision 5.2.2-2 If" .. "via the API." -->
> Provision 5.2.2-2 If a Developer offers an API to external customers or collaborators, they shall apply controls that mitigate attacks on the AI system via the API.

R-0046

<!-- q L684-685 "For example, placing" .. "a model." -->
> For example, placing limits on model access rate to limit an attacker's ability to reverse engineer or overwhelm defences to rapidly poison a model.

no entry: example for R-0046.

<!-- q L687-687 -->
> Provision 5.2.2-3 Developers shall also create dedicated environments for development and model tuning activities.

R-0047

<!-- q L688-688 -->
> The dedicated environments shall be backed by technical controls to ensure separation and principle of least privilege.

R-0048

<!-- q L689-690 -->
> In the context of AI, this is particularly necessary because training data shall only be present in the training and development environments where this training data is not based on publicly available data.

R-0049

<!-- q L692-693 -->
> Provision 5.2.2-4 Developers and System Operators shall implement and publish a clear and accessible vulnerability disclosure policy.

R-0050

<!-- q L695-696 -->
> Provision 5.2.2-5 Developers and System Operators shall create, test and maintain an AI system incident management plan and an AI system recovery plan.

R-0051

<!-- q L698-699 -->
> Provision 5.2.2-6 Developers and System Operators should ensure that, where they are using cloud service operators to help to deliver the capability, their contractual agreements support compliance with the above requirements.

R-0052

## §5.2.3

<!-- q L708-708 -->
> 5.2.3 Principle 7: Secure the supply chain

<!-- q L709-709 -->
> Primarily applies to: Developers, System Operators and Data Custodians

R-0118 · applicability · verb none

<!-- q L713-714 -->
> Provision 5.2.3-1 Developers and System Operators shall follow secure software supply chain processes for their AI model and system development.

R-0053

<!-- q L716-718 -->
> Provision 5.2.3-2 System Operators that choose to use or adapt any models, or components, which are not well-documented or secured shall be able to justify their decision to use such models or components through documentation (for example if there was no other supplier for said component).

R-0054

<!-- q L720-721 -->
> Provision 5.2.3-2.1 In this case, Developers and System Operators shall have mitigating controls and undertake a risk assessment linked to such models or components.

R-0055

<!-- q L723-723 -->
> Provision 5.2.3-2.2 System Operators shall share this documentation with End-users in an accessible way.

R-0056

<!-- q L725-726 -->
> Provision 5.2.3-3 Developers and System Operators shall re-run evaluations on released models that they intend on using.

R-0057

<!-- q L728-729 -->
> Provision 5.2.3-4 System Operators shall communicate their intention to update models to End-users in an accessible way prior to models being updated.

R-0058

## §5.2.4

<!-- q L732-732 -->
> 5.2.4 Principle 8: Document data, models and prompts

<!-- q L733-733 -->
> Primarily applies to: Developers

R-0119 · applicability · verb none

<!-- q L737-738 "Provision 5.2.4-1 Developers" .. "post-deployment maintenance plans." -->
> Provision 5.2.4-1 Developers shall document and maintain a clear audit trail of their system design and post-deployment maintenance plans.

R-0059

<!-- q L738-739 "Developers should make" .. "and Data Custodians." -->
> Developers should make the documentation available to the downstream System Operators and Data Custodians.

R-0060

<!-- q L741-743 -->
> Provision 5.2.4-1.1 Developers should ensure that the document includes security-relevant information, such as the sources of training data (including fine-tuning data and human or other operational feedback), intended scope and limitations, guardrails, retention time, suggested review frequency and potential failure modes.

R-0061

<!-- q L745-746 -->
> Provision 5.2.4-1.2 Developers shall release cryptographic hashes for model components that are made available to other stakeholders to allow them to verify the authenticity of the components.

R-0062

<!-- q L748-749 "Provision 5.2.4-2 Where" .. "been poisoned." -->
> Provision 5.2.4-2 Where training data has been sourced from publicly available sources, there is a risk that this data might have been poisoned.

no entry: opening sentence of Provision 5.2.4-2, the risk its shall answers (R-0063); no verbal form of the directives.

<!-- q L749-750 "As discovery of" .. "in the model." -->
> As discovery of poisoned data is likely to occur after training (if at all), Developers shall document how they obtained the public training data, where it came from and how that data is used in the model.

R-0063

<!-- q L752-753 "Provision 5.2.4-2.1 The" .. "data was obtained." -->
> Provision 5.2.4-2.1 The documentation of training data should include at a minimum the source of the data, such as the URL of the scraped page, and the date/time the data was obtained.

R-0064

<!-- q L753-754 "This will allow" .. "data sets." -->
> This will allow Developers to identify whether a reported data poisoning attack was in their data sets.

no entry: rationale for R-0064; will states a consequence.

<!-- q L756-757 "Provision 5.2.4-3 Developers" .. "of the systems." -->
> Provision 5.2.4-3 Developers should ensure that they have an audit log of changes to system prompts or other model configuration (including prompts) that affect the underlying working of the systems.

R-0065

<!-- q L757-758 "Developers can make" .. "to the model." -->
> Developers can make this available to any System Operators and End-Users that have access to the model.

R-0066 · possibility (can): no provision

## §5.2.5

<!-- q L761-761 -->
> 5.2.5 Principle 9: Conduct appropriate testing and evaluation

<!-- q L762-762 -->
> Primarily applies to: Developers and System Operators

R-0120 · applicability · verb none

<!-- q L766-767 -->
> Provision 5.2.5-1 Developers shall ensure that all models, applications and systems that are released to System Operators and/or End-users have been tested as part of a security assessment process.

R-0067

<!-- q L769-770 -->
> Provision 5.2.5-2 System Operators shall conduct testing prior to the system being deployed with support from Developers.

R-0068

<!-- q L778-779 -->
> Provision 5.2.5-2.1 For security testing, System Operators and Developers should use independent security testers with technical skills relevant to their AI systems.

R-0069

<!-- q L781-782 -->
> Provision 5.2.5-3 Developers should ensure that the findings from the testing and evaluation are shared with System Operators, to inform their own testing and evaluation.

R-0070

<!-- q L784-785 -->
> Provision 5.2.5-4 Developers should evaluate model outputs to ensure they do not allow System Operators or End-users to reverse engineer non-public aspects of the model or the training data.

R-0071

<!-- q L787-788 -->
> Provision 5.2.5-4.1 Additionally, Developers should evaluate model outputs to ensure they do not provide System Operators or End-users with unintended influence over the system.

R-0072

## §5.3

<!-- q L791-791 -->
> 5.3 Secure Deployment

## §5.3.1

<!-- q L792-793 -->
> 5.3.1 Principle 10: Communication and processes associated with End-users and Affected Entities

<!-- q L794-795 -->
> NOTE: As part of an organization's wider deployment practices, pre-deployment testing of AI systems is to be considered alongside the requirements below.

no entry: NOTE, informative (SD-13). It stands where the other principles have their applicability line (SD-1).

<!-- q L797-798 "Provision 5.3.1-1 System" .. "employees or partners)." -->
> Provision 5.3.1-1 System Operators shall convey to End-users in an accessible way where and how their data will be used, accessed and stored (for example, if it is used for model retraining, or reviewed by employees or partners).

R-0073

<!-- q L798-799 "If the Developer" .. "to System Operators." -->
> If the Developer is an external entity, they shall provide this information to System Operators.

R-0074

<!-- q L801-802 "Provision 5.3.1-2 System" .. "of AI systems." -->
> Provision 5.3.1-2 System Operators shall provide End-users with accessible guidance to support their use, management, integration, and configuration of AI systems.

R-0075

<!-- q L802-803 "If the Developer" .. "help System Operators." -->
> If the Developer is an external entity, they shall provide all necessary information to help System Operators.

R-0076

<!-- q L805-806 -->
> Provision 5.3.1-2.1 System Operators shall include guidance on the appropriate use of the model or system, which includes highlighting limitations and potential failure modes.

R-0077

<!-- q L808-809 -->
> Provision 5.3.1-2.2 System Operators shall proactively inform End-users of any security relevant updates and provide clear explanations in an accessible way.

R-0078

<!-- q L811-812 "Provision 5.3.1-3 Developers" .. "of an incident." -->
> Provision 5.3.1-3 Developers and System Operators should support End-users and Affected Entities during and following a cyber security incident to contain and mitigate the impacts of an incident.

R-0079

<!-- q L812-813 "The process for" .. "contracts with End-users." -->
> The process for undertaking this should be documented and agreed in contracts with End-users.

R-0080

## §5.4

<!-- q L816-816 -->
> 5.4 Secure Maintenance

## §5.4.1

<!-- q L817-818 -->
> 5.4.1 Principle 11: Maintain regular security updates, patches and mitigations

<!-- q L819-819 -->
> Primarily applies to: Developers and System Operators

R-0121 · applicability · verb none

<!-- q L823-824 "Provision 5.4.1-1 Developers" .. "the security updates." -->
> Provision 5.4.1-1 Developers shall provide security updates and patches, where possible, and notify System Operators of the security updates.

R-0081

<!-- q L824-824 "System Operators shall" .. "patches to End-users." -->
> System Operators shall deliver these updates and patches to End-users.

R-0082

<!-- q L826-827 -->
> Provision 5.4.1-1.1 Developers shall have mechanisms and contingency plans to mitigate security risks, particularly in instances where updates cannot be provided for AI systems.

R-0083 · split into R-0122 (shall), R-0123 (cannot)

<!-- q L829-830 -->
> Provision 5.4.1-2 Developers should treat major AI system updates as though a new version of a model has been developed and therefore undertake a new security testing and evaluation process to help protect users.

R-0084

<!-- q L832-833 -->
> Provision 5.4.1-3 Developers should support System Operators to evaluate and respond to model changes, (for example by providing preview access via beta-testing and versioned APIs).

R-0085

## §5.4.2

<!-- q L842-842 -->
> 5.4.2 Principle 12: Monitor the system's behaviour

<!-- q L843-843 -->
> Primarily applies to: Developers and System Operators

R-0124 · applicability · verb none

<!-- q L847-848 -->
> Provision 5.4.2-1 System Operators shall log system and user actions to support security compliance, incident investigations, and vulnerability remediation.

R-0086

<!-- q L850-852 -->
> Provision 5.4.2-2 System Operators should analyse their logs to ensure that AI models continue to produce desired outputs and to detect anomalies, security breaches, or unexpected behaviour over time (such as due to data drift or data poisoning).

R-0087

<!-- q L854-855 -->
> Provision 5.4.2-3 System Operators and Developers should monitor internal states of their AI systems where this could better enable them to address security threats, or to enable future security analytics.

R-0088

<!-- q L857-858 -->
> Provision 5.4.2-4 System Operators and Developers should monitor the performance of their models and system over time so that they can detect sudden or gradual changes in behaviour that could affect security.

R-0089 · split into R-0125 (should), R-0126 (can)

## §5.5

<!-- q L861-861 -->
> 5.5 Secure End of Life

## §5.5.1

<!-- q L862-862 -->
> 5.5.1 Principle 13: Ensure proper data and model disposal

<!-- q L863-863 -->
> Primarily applies to: Developers and System Operators

R-0127 · applicability · verb none

<!-- q L865-866 "Provision 5.5.1-1 If" .. "of these assets." -->
> Provision 5.5.1-1 If a Developer or System Operator decides to transfer or share ownership of training data and/or a model to another entity they shall involve Data Custodians and securely dispose of these assets.

R-0090

<!-- q L866-867 "This will protect" .. "instantiation to another." -->
> This will protect AI against security issues that can transfer from one AI system instantiation to another.

R-0091 · possibility (can): no provision

<!-- q L869-870 -->
> Provision 5.5.1-2 If a Developer or System Operators decides to decommission a model and/or system, they shall involve Data Custodians and securely delete applicable data and configuration details.

R-0092

## Source defects and open questions

Found by pass 1 (requirements lane) reading the source; lines are the pinned rendering's.

**SD-1.** Principle 10 (§5.3.1, L792-813) has no applicability line and no References line; a NOTE (L794-795) stands where the other principles put them, so who holds primary responsibility for it is not indicated. Its provisions name System Operators, external Developers, and Developers with System Operators (R-0129). §5.5.1 also lacks a References line.

**SD-2.** Applicability lines and provision actors disagree, measured by script over the actor fields of the leaf entries: §5.1.1: Organization is bound here (R-0007, R-0008, R-0009, R-0010, R-0011, R-0104, R-0105) but not listed; System Operator, Developer, Data Custodian are listed but no provision here names them as actor · §5.1.2: Data Custodian is bound here (R-0018) but not listed; Organization is bound here (R-0019) but not listed · §5.2.1: End-user is bound here (R-0041) but not listed · §5.2.3: Data Custodian is listed but no provision here names it as actor. See R-0129 and R-0130.

**SD-3.** 5.2.1-4 (R-0041) is the one provision whose actors include End-users, a role that takes in consumers (Table 4-1, L486-489). Principle 5's applicability line does not list them, and nothing tells an End-user which data counts as sensitive.

**SD-4.** Organization, the actor of 5.1.1-1, 5.1.1-2, 5.1.1-2.2 and 5.1.2-5.1, is neither a Table 4-1 role nor a §3.1 term (R-0130). 5.1.1-2.2 also writes developers in lowercase, for staff who develop, where every other provision capitalises the role.

**SD-5.** §3.1 defines training as teaching an AI model (L408-409), but Principle 1 uses the word for staff security training (R-0007, R-0008, R-0011, R-0104). Read with the definition, 5.1.1-1.1 would tailor model training to staff roles; the entries read it as staff training.

**SD-6.** §3.1 confines threat modelling to a system's design and development phases (L405-406); 5.1.3-1.1 (R-0024) runs it at any lifecycle stage, and 5.1.3-2 has System Operators threat model their systems (R-0112).

**SD-7.** 5.2.1-4 (R-0041) sends the reader to clause 5.2.3 for data-securing details; clause 5.2.3 is Principle 7, the supply chain (L708-729), and holds none. The nearest data-securing provisions sit in clauses 5.2.1 (5.2.1-4.2) and 5.2.2 (5.2.2-1, 5.2.2-3).

**SD-8.** 5.2.1-4.1 ends by referring to clause 5.2.2 for provisions on open source (L668-669); clause 5.2.2, Principle 6 (L675-699), never mentions open source. With L443-444 the EN signals that some Developer provisions are relaxed for open-source models without identifying any (R-0140).

**SD-9.** The End-users row of Table 4-1 (L491-494) explains the role by expectations a voluntary Code places on the other roles. The EN identifies no such Code: the only code in §2.2 is [i.21], a code of conduct the row does not cite.

**SD-10.** The Affected entities row of Table 4-1 (L504-506) describes them as entities that AI systems, and decisions based on AI output, do not affect directly, which reads against the role's name; whether indirectly affected is meant is not said. 5.3.1-3 (R-0079) is the only provision naming them.

**SD-11.** 5.1.1-2.1 (R-0010) refers back to updates, but 5.1.1-2 before it speaks of awareness, not updates; the nearest antecedent is the review and update of AI security content in 5.1.1-1.

**SD-12.** The second sentence of 5.2.4-3 (R-0066) uses can where a permission seems meant. Under ETSI DR 3.2 can states possibility, so as written the sentence neither permits nor requires anything; it is recorded with normativity possibility.

**SD-13.** The NOTE opening §5.3.1 (L794-795) words a requirement (is to be considered) inside a NOTE, which states no provision under the drafting rules; the pre-deployment testing it points to is required anyway by 5.2.5-2 (R-0068).

**SD-14.** The third sentence of 5.2.2-3 (R-0049) states its shall inside a because-clause offered as the reason for the separate environments. It still binds under ETSI DR 3.2 and is recorded as a requirement, scoped to non-public training data.

**SD-15.** These entries take their actor from context, because the sentence is passive or its subject is the previous sentence's work product: R-0007 (5.1.1-1.1), R-0009 (5.1.1-2), R-0010 (5.1.1-2.1), R-0013 (5.1.2-1.1), R-0016 (5.1.2-3), R-0023 (5.1.3-1), R-0024 (5.1.3-1.1), R-0029 (5.1.3-2), R-0043 (5.2.1-4.1), R-0048 (5.2.2-3), R-0049 (5.2.2-3), R-0064 (5.2.4-2.1), R-0080 (5.3.1-3), R-0111 (5.1.3-2). Their actor fields mark the actor (implied).

**SD-16.** 5.1.2-1, 5.1.4-1 and 5.1.4-3 address a System Operator and/or Developer; where the two roles are separate entities, the EN does not say whether one of them meeting the provision is enough.

**SD-17.** 5.2.3-2.1 (R-0055) binds Developers and System Operators in this case, but the case (5.2.3-2) is a System Operator's choice of a poorly documented model or component; how a Developer falls under it is unstated.

**SD-18.** 5.2.2-6 (R-0052) asks that contracts with cloud service operators support compliance with the above requirements, without saying whether that is 5.2.2-1 to 5.2.2-5 or every provision before it.

**SD-19.** 5.5.1-1 (R-0090) attaches secure disposal of these assets to a transfer and to a sharing of ownership alike; disposing of an asset whose ownership is shared ends the sharing, so what the sharing party disposes of (its own copies?) is unclear.
