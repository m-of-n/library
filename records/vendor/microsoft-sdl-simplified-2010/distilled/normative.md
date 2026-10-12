---
schema: "library-normative/v1"
id: microsoft-sdl-simplified-2010-normative
record: microsoft-sdl-simplified-2010
kind: normative
type: normative
title: "microsoft-sdl-simplified-2010 — normative content, verbatim"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

Source: *Simplified Implementation of the Microsoft SDL* (updated November 4, 2010), sha256 `ef676ae4…d413`, and its companion spreadsheet (sha256 `094b8e5f…49c9`). Part I is the paper from "Microsoft SDL Optimization Model" to the end of "Application Security Verification Process", verbatim, with requirement ids in brackets on the headings. Part II lists every spreadsheet row verbatim with its own id.

# Part I — the paper

## Microsoft SDL Optimization Model

Integration of secure development concepts into an existing development process can be intimidating and costly if done improperly. Success or failure often hinges on variables such as organizational size, resources (time, talent, and budgets), and support from the executive suite. The impact of these intangibles can be controlled by understanding the elements of good security development practices and establishing implementation priorities based on the maturity level of the development team. Microsoft has created the SDL Optimization Model to help address these issues.

The SDL Optimization Model is structured around five capability areas that roughly correspond to the phases within the software development life cycle:

Training, policy, and organizational capabilities

Requirements and design

Implementation

Verification

Release and response

Additionally, the SDL Optimization Model defines four levels of maturity for the practices and capabilities in these areas—Basic, Standardized, Advanced, and Dynamic.

The SDL Optimization Model starts at the Basic level of maturity, with little or no process, training, and tooling in place, and progresses to the Dynamic level, which is characterized by complete SDL compliance across an entire organization. Complete SDL compliance includes efficient and effective processes, highly trained individuals, specialized tooling, and strong accountability to parties both internal and external to the organization.

This paper focuses on the tasks and processes necessary to achieve the “advanced” maturity level. That is, the point where an organization demonstrating competence in each of the five capability areas mentioned earlier can reasonably claim to follow the practices of the Microsoft SDL.

In contrast to other software maturity models, the Microsoft SDL Optimization Model focuses strictly on development process improvements. It provides prescriptive, actionable guidance on how to move from lower levels of process maturity to higher levels and avoids the “list of lists” approach, of other optimization models.

## SDL Applicability [PROC-sdl-applicability]

It is vitally important to set clear expectations for an organization about the types of projects that will be subject to the controls imposed by the Microsoft SDL. Practical experience suggests that applications exhibiting one or more of the following characteristics should be subject to the SDL:

Deployed in a business or enterprise environment

Processes personally identifiable information (PII) or other sensitive information

Communicates regularly over the Internet or other networks

Given the pervasiveness of computing technologies and the evolving threat environment, it may be easier to identify application development projects that aren’t subject to security controls like those present in the SDL.

## Roles, Responsibilities, and Qualifications of Security Personnel [PROC-roles-responsibilities-and-qualification]

The SDL includes general criteria and job descriptions for security and privacy roles. These roles are filled during the Requirements Phase of the SDL process. These roles are consultative in nature, and provide the organizational structure necessary to identify, catalog, and mitigate security and privacy issues present in a software development project. These roles include:

Reviewer/Advisory Roles. These roles are designed to provide project security and privacy oversight and have the authority to accept or reject security and privacy plans from a project team.

- Security Advisor/Privacy Advisor. These roles are filled by subject-matter experts (SMEs) from outside the project team. The role can either be filled by a qualified member of an independent, centralized group within the organization specifically chartered for reviews of this type, or by an expert external to the organization. The person chosen for this task must fill two sub-roles:
  - Auditor. This individual must monitor each phase of the software development process and attest to successful completion of each security requirement. The advisor must have the freedom to attest to compliance (or non-compliance) with security and privacy requirements without interference from the project team.
  - Expert. The person chosen for the advisor role must possess verifiable subject-matter expertise in security.
- Combination of Advisory Roles. The role of security advisor may be combined with the role of privacy advisor if an individual with the appropriate skills and experience can be identified.

Team Champions. The team champion roles should be filled by SMEs from the project team. These roles are responsible for the negotiation, acceptance, and tracking of minimum security and privacy requirements and maintaining clear lines of communication with advisors and decision makers during a software development project.

- Security Champion/Privacy Champion. This individual (or group of individuals) does not have sole responsibility for ensuring that a software release has addressed all security issues, but is responsible for coordinating and tracking security issues for the project. This role also is responsible for reporting status to the security advisor and to other relevant parties (for example, development and test leads) on the project team.
- Combination of Roles. As with the security and privacy advisor role, the responsibilities vested in the champion role may be combined if an individual with the appropriate skills and experience can be identified.

## Simplified SDL Security Activities

Simply put, the Microsoft SDL is a collection of mandatory security activities, presented in the order they should occur and grouped by the phases of the traditional software development life cycle (SDLC). Many of the activities discussed would provide some degree of security benefit if implemented on a standalone basis. However, practical experience at Microsoft has shown that security activities executed as part of a software development process lead to greater security gains than activities implemented piecemeal or in an ad-hoc fashion.

Optional security activities may be added at the discretion of the project team or the security advisor to achieve desired security and privacy objectives. In the interest of brevity, detailed discussion of each security activity is omitted.

Figure 2: The Microsoft Security Development Lifecycle - Simplified

A fundamental concept to note is that an organization should focus on the quality and completeness of the output produced at each phase. A certain degree of security-process sophistication is expected of organizations operating at the Advanced and Dynamic levels of the SDL Optimization Model. That being said, it makes no difference if, for example, a threat model is produced as the result of a whiteboard session with the development team, is written out as a narrative in a Microsoft Word document, or is produced with the use of a specialized tool, such as the SDL Threat Modeling Tool. The SDL process does benefit from investments in effective tools and automation, but the real value lies in comprehensive and accurate results.

For ease of review, a detailed diagram that illustrates the SDL process flow can be found in Appendix A. This diagram is a visualization of the security activities used on a hypothetical project, ranging from training employees to application release. This example includes both mandatory and optional tasks.

### Mandatory Security Activities

If a software development project is determined to be subject to the SDL (see the SDL Applicability section), the development team must successfully complete sixteen mandatory security activities to comply with the Microsoft SDL process. These mandatory activities have been acknowledged as effective by security and privacy experts, and are constantly reviewed for effectiveness as part of a rigorous annual evaluation process. As mentioned previously, development teams should retain the flexibility to specify other security activities as necessary, but the list of “must-complete” practices should always include the sixteen included in this document.

#### Pre-SDL Requirements: Security Training

##### SDL Practice 1: Training Requirements [SP-01]

All members of a software development team must receive appropriate training to stay informed about security basics and recent trends in security and privacy. Individuals in technical roles (developers, testers, and program managers) that are directly involved with the development of software programs must attend at least one unique security training class each year.

Basic software security training should cover foundational concepts such as:

Secure design, including the following topics:

Attack surface reduction

Defense in depth

Principle of least privilege

Secure defaults

Threat modeling, including the following topics:

Overview of threat modeling

Design implications of a threat model

Coding constraints based on a threat model

Secure coding, including the following topics:

Buffer overruns (for applications using C and C++)

Integer arithmetic errors (for applications using C and C++)

Cross-site scripting (for managed code and Web applications)

SQL injection (for managed code and Web applications)

Weak cryptography

Security testing, including the following topics:

Differences between security testing and functional testing

Risk assessment

Security testing methods

Privacy, including the following topics:

Types of privacy-sensitive data

Privacy design best practices

Risk assessment

Privacy development best practices

Privacy testing best practices

The preceding training establishes an adequate knowledge baseline for technical personnel. As time and resources permit, training in advanced concepts may be necessary. Examples include, but are not limited to, the following:

Advanced security design and architecture

Trusted user interface design

Security vulnerabilities in detail

Implementing custom threat mitigations

#### Phase One: Requirements

##### SDL Practice 2: Security Requirements [SP-02]

The need to consider security and privacy “up front” is a fundamental aspect of secure system development. The optimal point to define trustworthiness requirements for a software project is during the initial planning stages. This early definition of requirements allows development teams to identify key milestones and deliverables, and permits the integration of security and privacy in a way that minimizes any disruption to plans and schedules. Security and privacy requirements analysis is performed at project inception and includes specification of minimum security requirements for the application as it is designed to run in its planned operational environment and specification and deployment of a security vulnerability/work item tracking system.

##### SDL Practice 3: Quality Gates/Bug Bars [SP-03]

Quality gates and bug bars are used to establish minimum acceptable levels of security and privacy quality. Defining these criteria at the start of a project improves the understanding of risks associated with security issues and enables teams to identify and fix security bugs during development. A project team must negotiate quality gates (for example, all compiler warnings must be triaged and fixed prior to code check-in) for each development phase, and then have them approved by the security advisor, who may add project-specific clarifications and more stringent security requirements as appropriate. The project team must also illustrate compliance with the negotiated quality gates in order to complete the Final Security Review (FSR).

A bug bar is a quality gate that applies to the entire software development project. It is used to define the severity thresholds of security vulnerabilities—for example, no known vulnerabilities in the application with a “critical” or “important” rating at time of release. The bug bar, once set, should never be relaxed. A dynamic bug bar is a moving target that is likely to be poorly understood within the development organization.

##### SDL Practice 4: Security and Privacy Risk Assessment [SP-04]

Security risk assessments (SRAs) and privacy risk assessments (PRAs) are mandatory processes that identify functional aspects of the software that require deep review. Such assessments must include the following information:

(Security) Which portions of the project will require threat models before release?

(Security) Which portions of the project will require security design reviews before release?

(Security) Which portions of the project (if any) will require penetration testing by a mutually agreed upon group that is external to the project team?

(Security) Are there any additional testing or analysis requirements the security advisor deems necessary to mitigate security risks?

(Security) What is the specific scope of the fuzz testing requirements?

(Privacy) What is the Privacy Impact Rating? The answer to this question is based on the following guidelines:

P1 High Privacy Risk. The feature, product, or service stores or transfers PII, changes settings or file type associations, or installs software.

P2 Moderate Privacy Risk. The sole behavior that affects privacy in the feature, product, or service is a one-time, user-initiated, anonymous data transfer (for example, the user clicks on a link and the software goes out to a Web site).

P3 Low Privacy Risk. No behaviors exist within the feature, product, or service that affect privacy. No anonymous or personal data is transferred, no PII is stored on the machine, no settings are changed on the user's behalf, and no software is installed.

#### Phase Two: Design

##### SDL Practice 5: Design Requirements [SP-05]

The optimal time to influence a project’s design trustworthiness is early in its life cycle. It is critically important to consider security and privacy concerns carefully during the design phase. Mitigation of security and privacy issues is much less expensive when performed during the opening stages of a project life cycle. Project teams should refrain from the practice of “bolting on” security and privacy features and mitigations near the end of a project’s development.

In addition, it is crucially important for project teams to understand the distinction between “secure features” and “security features.” It is quite possible to implement security features, which are in fact, insecure. Secure features are defined as features whose functionality is well engineered with respect to security, including rigorous validation of all data before processing or cryptographically robust implementation of libraries for cryptographic services. The term security features describes program functionality with security implications, such as Kerberos authentication or a firewall.

The design requirements activity contains a number of required actions. Examples include the creation of security and privacy design specifications, specification review, and specification of minimal cryptographic design requirements. Design specifications should describe security or privacy features that will be directly exposed to users, such as those that require user authentication to access specific data or user consent before use of a high-risk privacy feature. In addition, all design specifications should describe how to securely implement all functionality provided by a given feature or function. It’s a good practice to validate design specifications against the application’s functional specification. The functional specification should:

Accurately and completely describe the intended use of a feature or function.

Describe how to deploy the feature or function in a secure fashion.

##### SDL Practice 6: Attack Surface Reduction [SP-06]

Attack surface reduction is closely aligned with threat modeling, although it addresses security issues from a slightly different perspective. Attack surface reduction is a means of reducing risk by giving attackers less opportunity to exploit a potential weak spot or vulnerability. Attack surface reduction encompasses shutting off or restricting access to system services, applying the principle of least privilege, and employing layered defenses wherever possible.

##### SDL Practice 7: Threat Modeling [SP-07]

Threat modeling is used in environments where there is meaningful security risk. It is a practice that allows development teams to consider, document, and discuss the security implications of designs in the context of their planned operational environment and in a structured fashion. Threat modeling also allows consideration of security issues at the component or application level. Threat modeling is a team exercise, encompassing program/project managers, developers, and testers, and represents the primary security analysis task performed during the software design stage.

#### Phase Three: Implementation

##### SDL Practice 8: Use Approved Tools [SP-08]

All development teams should define and publish a list of approved tools and their associated security checks, such as compiler/linker options and warnings. This list should be approved by the security advisor for the project team. Generally speaking, development teams should strive to use the latest version of approved tools to take advantage of new security analysis functionality and protections.

##### SDL Practice 9: Deprecate Unsafe Functions [SP-09]

Many commonly used functions and APIs are not secure in the face of the current threat environment. Project teams should analyze all functions and APIs that will be used in conjunction with a software development project and prohibit those that are determined to be unsafe. Once the banned list is determined, project teams should use header files (such as banned.h and strsafe.h), newer compilers, or code scanning tools to check code (including legacy code where appropriate) for the existence of banned functions, and replace those banned functions with safer alternatives.

##### SDL Practice 10: Static Analysis [SP-10]

Project teams should perform static analysis of source code. Static analysis of source code provides a scalable capability for security code review and can help ensure that secure coding policies are being followed. Static code analysis by itself is generally insufficient to replace a manual code review. The security team and security advisors should be aware of the strengths and weaknesses of static analysis tools and be prepared to augment static analysis tools with other tools or human review as appropriate.

#### Phase Four: Verification

##### SDL Practice 11: Dynamic Program Analysis [SP-11]

Run-time verification of software programs is necessary to ensure that a program’s functionality works as designed. This verification task should specify tools that monitor application behavior for memory corruption, user privilege issues, and other critical security problems. The SDL process uses run-time tools like AppVerifier, along with other techniques such as fuzz testing, to achieve desired levels of security test coverage.

##### SDL Practice 12: Fuzz Testing [SP-12]

Fuzz testing is a specialized form of dynamic analysis used to induce program failure by deliberately introducing malformed or random data to an application. The fuzz testing strategy is derived from the intended use of the application and the functional and design specifications for the application. The security advisor may require additional fuzz tests or increases in the scope and duration of fuzz testing.

##### SDL Practice 13: Threat Model and Attack Surface Review [SP-13]

It is common for an application to deviate significantly from the functional and design specifications created during the requirements and design phases of a software development project. Therefore, it is critical to re-review threat models and attack surface measurement of a given application when it is code complete. This review ensures that any design or implementation changes to the system have been accounted for, and that any new attack vectors created as a result of the changes have been reviewed and mitigated.

#### Phase Five: Release

##### SDL Practice 14: Incident Response Plan [SP-14]

Every software release subject to the requirements of the SDL must include an incident response plan. Even programs with no known vulnerabilities at the time of release can be subject to new threats that emerge over time. The incident response plan should include:

An identified sustained engineering (SE) team, or if the team is too small to have SE resources, an emergency response plan (ERP) that identifies the appropriate engineering, marketing, communications, and management staff to act as points of first contact in a security emergency.

On-call contacts with decision-making authority that are available 24 hours a day, seven days a week.

Security servicing plans for code inherited from other groups within the organization.

Security servicing plans for licensed third-party code, including file names, versions, source code, third-party contact information, and contractual permission to make changes (if appropriate).

##### SDL Practice 15: Final Security Review [SP-15]

The Final Security Review (FSR) is a deliberate examination of all the security activities performed on a software application prior to release. The FSR is performed by the security advisor with assistance from the regular development staff and the security and privacy team leads. The FSR is not a “penetrate and patch” exercise, nor is it a chance to perform security activities that were previously ignored or forgotten. The FSR usually includes an examination of threat models, exception requests, tool output, and performance against the previously determined quality gates or bug bars. The FSR results in one of three different outcomes:

Passed FSR. All security and privacy issues identified by the FSR process are fixed or mitigated.

Passed FSR with exceptions. All security and privacy issues identified by the FSR process are fixed or mitigated and/or all exceptions are satisfactorily resolved. Those issues that cannot be addressed (for example, vulnerabilities posed by legacy “design level” issues) are logged and corrected in the next release.

FSR with escalation. If a team does not meet all SDL requirements and the security advisor and the product team cannot reach an acceptable compromise, the security advisor cannot approve the project, and the project cannot be released. Teams must either address whatever SDL requirements that they can prior to launch or escalate to executive management for a decision.

##### SDL Practice 16: Release/Archive [SP-16]

Software release to manufacturing (RTM) or release to Web (RTW) is conditional on completion of the SDL process. The security advisor assigned to the release must certify (using the FSR and other data) that the project team has satisfied security requirements. Similarly, for all products that have at least one component with a Privacy Impact Rating of P1, the project’s privacy advisor must certify that the project team has satisfied the privacy requirements before the software can be shipped.

In addition, all pertinent information and data must be archived to allow for post-release servicing of the software. This includes all specifications, source code, binaries, private symbols, threat models, documentation, emergency response plans, license and servicing terms for any third-party software and any other data necessary to perform post-release servicing tasks.

### Optional Security Activities

Optional security activities are generally performed when a software application is likely to be used in critical environments or scenarios. They are often specified by a security advisor as part of a negotiated set of additional requirements to ensure a greater level of security analysis for certain software components. The practices in this section provide examples of optional security tasks and should not be considered an exhaustive list.

##### Manual Code Review [OPT-manual-code-review]

Manual code review is an optional task in the SDL and is usually performed by highly skilled individuals on the application security team and/or the security advisor. While analysis tools can do much of the work of finding and flagging vulnerabilities, they are not perfect. As a result, manual code review is usually focused on the “critical” components of an application. Most often it is used where sensitive data, such as personally identifiable information (PII), is processed or stored. It is also used to examine other critical functionality such as cryptographic implementations.

##### Penetration Testing [OPT-penetration-testing]

Penetration testing is a white box security analysis of a software system performed by skilled security professionals simulating the actions of a hacker. The objective of a penetration test is to uncover potential vulnerabilities resulting from coding errors, system configuration faults, or other operational deployment weaknesses. Penetration tests are often performed in conjunction with automated and manual code reviews to provide a greater level of analysis than would ordinarily be possible.

##### Vulnerability Analysis of Similar Applications [OPT-vulnerability-analysis-of-similar-applications]

Many reputable sources of information about software vulnerabilities can be found on the Internet. In some cases, the analysis of vulnerabilities found in analogous software applications can shed light on potential design or implementation issues in software under development.

## Other Process Requirements

### Root Cause Analysis [PROC-root-cause-analysis]

While not traditionally a part of the software development process, root cause analysis plays an important part in ensuring software security. Upon discovery of a previously unknown vulnerability, an investigation should be performed to ascertain precisely where the security processes failed. These vulnerabilities can be attributed to a variety of causes, including human error, tool failure, and policy failure. The goal of root cause analysis is to understand the precise nature of the failure. This information helps to ensure that errors of the same type are accounted for in future revisions of the SDL.

### Periodic Process Updates [PROC-periodic-process-updates]

Software threats are not static. As a result, the process used to secure software cannot be static. Organizations should take the knowledge learned from practices such as root cause analysis, policy changes, and improvements in technology and automation, and apply them to the SDL on a predictable schedule. Generally speaking, a yearly update schedule should suffice. The exception to this rule is when new, previously unknown vulnerability types are identified. This phenomenon requires immediate, out-of-cycle revision of the SDL to ensure proper mitigations are in place going forward.

## Application Security Verification Process [PROC-application-security-verification-proces]

Organizations developing secure software will naturally want a means to verify that the processes outlined in the Microsoft SDL have been followed. Access to centralized development and test data helps decision-making in a number of important scenarios, such as the Final Security Review, SDL requirement exception handling, and security audits. The process of verifying application security involves a number of different processes and actors:

A specially designated application should be used to track compliance with the SDL. This application serves as the central repository for all SDL process artifacts, including (but not limited to) design and implementation notes, threat models, tool log uploads, and other process attestations. As with any critical application, it should use access controls to ensure:

- Only authorized personnel can use the application.
- Strong separation between roles. For example, a developer may be able to use the application and upload data, but should be prohibited from accessing functionality reserved for the security and privacy advisors, security team leads, and testers.
- The security and privacy team leads are responsible for ensuring that the data necessary for an objective judgment is properly categorized and entered into the tracking application.
- The information entered into the tracking application is used by the security and privacy advisors to provide the analysis framework for the Final Security Review.
- The security and privacy advisors are responsible for reviewing the data entered into the tracking application (including the FSR results and other additional security tasks assigned by the advisors) and certifying that all requirements are met and/or all exceptions are satisfactorily resolved.

This document focuses on the Advanced level of the SDL Optimization Model, where rudimentary tracking processes are (in most instances) insufficient to the task. However, organizations with less sophisticated processes or smaller resource pools—those who fit within the Basic or Standardized levels of the SDL Optimization Model—can likely make do with a simpler tracking process.

It is very important that the tracking and verification process accurately capture:

The security and privacy requirements of the organization (for example, no known critical vulnerabilities at release).

The functional and technical requirements of the application under development.

The application’s operational context.

For example, if a development team creates a process control application to run in a critical environment, the proper investment of time and resources must be allocated to the creation and maintenance of the tracking process to enable objective analyses by the organization’s security and privacy principals, executive leadership, and relevant third parties such as compliance auditors or evaluators. Put differently, skimping on the tracking process inevitably leads to problems later, usually during an emergency. Ensure that reliable systems are in place to answer critical questions at critical times.



# Part II — Simplified SDL spreadsheet (verbatim rows)

## Training 1.0 — Training Practices [XLS-Training-1.0]

A well thought-out training program allows software development teams to learn about security and privacy basics, specific technical issues and stay informed about recent trends in security and privacy.

## Training 1.1 — Complete Core Security Training [XLS-Training-1.1]

All members of software development teams must receive appropriate training to stay informed about security basics and recent trends in security and privacy. 

Basic software security training should cover foundational concepts such as: 
-  Secure design, including the following topics: Attack surface reduction, Defense in depth, rinciple of least privilege, Secure defaults
- Threat modeling, including the following topics: Overview of threat modeling, Design implications of a threat model, Coding constraints based on a threat model
- Secure coding, including the following topics: Buffer overruns (for applications using C and C++), Integer arithmetic errors (for applications using C and C++), Cross-site scripting (for managed code and Web applications), SQL injection (for managed code and Web applications), Weak cryptography
- Security testing, including the following topics: Differences between security testing and functional testing, Risk assessment, Security testing methods
- Privacy, including the following topics: Types of privacy-sensitive data, Privacy design best practices, Risk assessment, Privacy development best practices, Privacy testing best practices

*Additional notes:* More training resources available at:http://www.microsoft.com/security/sdl/discover/training.aspx

## Requirements 2.0 — Requirements Practices [XLS-Requirements-2.0]

Setting a designated time for defining project requirements allows development teams to consider how to best integrate security and privacy into the development process and identify key security objectives while minimizing disruption to applicaion usability, plans, and schedules.

## Requirements 2.1 — Establish Security Requirements [XLS-Requirements-2.1]

The need to consider security and privacy “up front” is a fundamental aspect of secure system development. The optimal point to define trustworthiness requirements for a software project is during the initial planning stages. This early definition of requirements allows development teams to identify key milestones and deliverables, and permits the integration of security and privacy in a way that minimizes any disruption to plans and schedules.

Create a basic questionnaire to verify whether your product should be subject to the SDL. If you determine is should be based on the results of your questionairre, begin building your baseline security requirements from the content of the questionnaire.

*Additional notes:* At a minimum, products that meet the following criteria should follow a SDL process:
1. Any product that is commonly used or deployed within a business (e.g. Email or database servers)
2. Any product that regularly stores, processes, or communicates personally identifiable information (PII) such as financial, medical, or sensitive customer information.
3. Any online products or services that target or are attractive to children .
4. Any product that regularly touches or listens on the internet.
5. Any product that automatically downloads updates.

## Requirements 2.1.1 — Assign Security Experts [XLS-Requirements-2.1.1]

Identify the security advisor who will serve as your team's first point of contact for security support and additional resources. This person will serve as the security advisor for the project.

Identify the team or individual that is responsible for tracking and managing security for the product. This team or individual does not have sole responsibility for ensuring that a software release is secure, but this team or individual is responsible for coordinating and communicating the status of any security issues in the product. 

In smaller product groups, a single person may fill these roles.

## Requirements 2.1.2 — Define Minimum Security Criteria [XLS-Requirements-2.1.2]

Establish the minimum security requirements for the application as it is designed to run in its planned operational environment.

## Requirements 2.1.3 — Specify Bug/Work Tracking Tool [XLS-Requirements-2.1.3]

Specify and deploy a security vulnerability/work item tracking system that will allow you to assign, sort, filter, and track completion of security related bugs, work items or tasks.

*Additional notes:* Recommendation: Be sure to configure bug reporting tools correctly; limit access to bugs with security implications to the project team and security advisors only.

## Requirements 2.2 — Create Quality Gates/Bug Bars [XLS-Requirements-2.2]

Quality gates and bug bars are used to establish minimum acceptable levels of security and privacy quality. Defining these criteria at the start of a project improves the understanding of risks associated with security issues and enables teams to identify and fix security bugs during development. A project team must negotiate quality gates (for example, all compiler warnings must be triaged and fixed prior to code check-in) for each development phase, and then have them approved by the security advisor, who may add project-specific clarifications and more stringent security requirements as appropriate. The project team must also illustrate compliance with the negotiated quality gates in order to complete the Final Security Review (FSR). 

A process should be defined to regulate the approval of exceptions to the Quality Gate/Bug Bar throughout the lifecycle of your project. This exception process should require approval from both product team management and security experts who understand any potential risks associated with a security exception and can make plans for mitigation in both Incident Response Planning and future product cycles.

*Additional notes:* A sample security bug bar document is available at http://msdn.microsoft.com/en-us/library/cc307404.aspx.

## Requirements 2.3 — Perform Security & Privacy Risk Assessment [XLS-Requirements-2.3]

Security risk assessments (SRAs) and privacy risk assessments (PRAs) are mandatory processes that identify functional aspects of the software that require deep review. Such assessments must include the following information:

• (Security) Which portions of the project will require threat models before release?
• (Security) Which portions of the project will require security design reviews before release?
• (Security) Which portions of the project (if any) will require penetration testing by a mutually agreed upon group that is external to the project team? 
• (Security) Are there any additional testing or analysis requirements the security advisor deems necessary to mitigate security risks?
• (Security) What is the specific scope of the fuzz testing requirements?
• (Privacy) What is the Privacy Impact Rating? The answer to this question is based on the following guidelines:
 
P1 High Privacy Risk: The feature, product, or service stores or transfers PII, changes settings or file type associations, or installs software.
P2 Moderate Privacy Risk: The sole behavior that affects privacy in the feature, product, or service is a one-time, user-initiated, anonymous data transfer (for example, the user clicks on a link and the software goes out to a Web site).
P3 Low Privacy Risk: No behaviors exist within the feature, product, or service that affect privacy. No anonymous or personal data is transferred, no PII is stored on the machine, no settings are changed on the user's behalf, and no software is installed.

*Additional notes:* A sample Privacy Questionairre to guide your risk assessment can be found here: http://msdn.microsoft.com/en-us/library/cc307393.aspx

## Design 3.0 — Design Practices [XLS-Design-3.0]

A design practices identifies the overall requirements and structure for the software and establishes design best practices.

## Design 3.1 — Establish Security Design Requirements [XLS-Design-3.1]

The design requirements activity contains a number of required actions. Examples include the creation of security and privacy design specifications, specification review, and specification of minimal cryptographic design requirements. Design specifications should describe security or privacy features that will be directly exposed to users, such as those that require user authentication to access specific data or user consent before use of a high-risk privacy feature. In addition, all design specifications should describe how to securely implement all functionality provided by a given feature or function. It’s a good practice to validate design specifications against the application’s functional specification. The functional specification should:
• Accurately and completely describe the intended use of a feature or function.
• Describe how to deploy the feature or function in a secure fashion.

## Design 3.1.1 — Perform Security Design Review [XLS-Design-3.1.1]

Complete a security design review with a security advisor for any project or portion of a project that requires one. Some low-risk components might not require a detailed security design review.

## Design 3.1.2 — Perform Privacy Design Review [XLS-Design-3.1.2]

To avoid costly mistakes, projects with a high privacy impact based on the Privacy Risk Assessment must hold a privacy design review.

*Additional notes:* A sample Privacy Questionairre to guide your review can be found here: http://msdn.microsoft.com/en-us/library/cc307393.aspx

## Design 3.1.3 — Satisfy Minimum Cryptographic Design Requirements [XLS-Design-3.1.3]

Satisfy the minimal cryptographic design requirements established for your product when you established Security Requirements.

*Additional notes:* The SDL crypto requirements, at a high-level, are:

Use AES for symmetric encryption/decryption
Use 128-bit or better symmetric keys
Use RSA for asymmetric encryption/decryption and signatures
Use 1024-bit or better RSA keys
Use SHA-256 or better for hashing and message authentication codes

For additional details on this requirement, please read through the online SDL Process Guidance available at: http://msdn.microsoft.com/en-us/security/cc420639.aspx

## Design 3.2 — Analyze Attack Surface [XLS-Design-3.2]

1. Use Code Access Secuirty (CAS) correctly
2. Manage firewall exceptions carefully
3. Ensure your application runs correctly as a non-administrator

*Additional notes:* 1. Use Code Access Secuirty (CAS) correctly: When developing with managed code, use strong-named assemblies and request minimal permission. When using strong-named assemblies, do not use APTCA (Allow Partially Trusted Caller Attribute) unless the assembly was approved by a security review.
2. Manage firewall exceptions carefully: Be logical and consistent when you make firewall exceptions. Any product or component that requires changes to the host firewall settings must adhere to the requirements that are outlined in the "Policy for Managing Firewall Configurations." document, available at http://msdn.microsoft.com/en-us/library/cc307394.aspx.
3. Ensure your application runs correctly as a non-administrator: following the requirement will enable teams to design and develop their applications with a standard user in mind. This will result in reducing attack surface exposed by applications, increasing the security of the user and system.

## Design 3.3 — Complete Threat Models [XLS-Design-3.3]

1. Complete threat models for all functionality identified during the cost analysis phase. Threat models typically must consider the following areas:
- All projects. All code exposed on the attack surface and all code written by or licensed from a third party.
- New projects. All features and functionality.
- Updated versions of existing projects. New features or functionality added in the updated version.

2. Ensure that all threat models meet minimal threat model quality requirements. All threat models must contain data flow diagrams, assets, vulnerabilities, and mitigation. Threat modeling can be done in a variety of ways using either tools or documentation/specifications to define the approach. 

3. Have all threat models and referenced mitigations reviewed and approved by at least one developer, one tester, and one program manager. Ask architects, developers, testers, program managers, and others who understand the software to contribute to threat models and to review them. Solicit broad input and reviews to ensure the threat models are as comprehensive as possible.

4. Threat model data and associated documentation (functional/design specs) should be stored using the document control system used by the product team.

*Additional notes:* For more information on Threat Modeling: http://www.microsoft.com/security/sdl/discover/design.aspx

## Implementation 4.0 — Implementation Practices [XLS-Implementation-4.0]

During the Implementation practice, the development team mandates and enforces best practices to be followed for the duration of the project.

## Implementation 4.1 — Specify/Approve Secure Compilers, Tools, Flags & Options [XLS-Implementation-4.1]

All development teams should define and publish a list of approved tools and their associated security checks, such as compiler/linker options and warnings. This list should be approved by the security advisor for the project team. Generally speaking, development teams should strive to use the latest version of approved tools to take advantage of new security analysis functionality and protections.

*Additional notes:* A list of Microsoft's SDL-related Implementation tools can be found at: http://www.microsoft.com/security/sdl/adopt/tools.aspx

The SDL Pro Network Tools members can be accessed at: http://www.microsoft.com/security/sdl/adopt/pronetwork.aspx

Use the currently required (or later) versions of compilers to compile options for the Win32, Win64, WinCE and Macintosh target platforms.
- Compile C/C++ code with /GS or approved alternative on other platforms. The "SDL Buffer Security Check" check-in policy provided with this template helps you enforce this in your project.
- Link C/C++ code with /SAFESEH or approved alternative on other platforms. The "SDL Safe Exception Handlers" check-in policy provided with this template helps you enforce this in your project.
- Link C/C++ code with /NXCOMPAT or approved alternative on other platforms. The "SDL DEP and ASLR" check-in policy provided with this template helps you enforce this in your project.
- Use MIDL with /robust or approved alternative on other platforms.

Use the currently required (or later) versions of code analysis tools for either native C and C++ or managed (C#) code that are available for the target platforms. The "Code Analysis" check-in policy provided out-of-the-box with Visual Studio Team Suite or Visual Studio Team System Development Edition helps you enforce this in your project.

## Implementation 4.2 — Identify/Deprecate Unsafe Functions [XLS-Implementation-4.2]

Project teams should analyze all functions and APIs that will be used in conjunction with a software development project and prohibit those that are determined to be unsafe. Once the banned list is determined, project teams should use header files (such as banned.h and strsafe.h), newer compilers, or code scanning tools to check code (including legacy code where appropriate) for the existence of banned functions, and replace those banned functions with safer alternatives.

*Additional notes:* New native C and C++ code must not use banned versions of string buffer handling functions. Based on analysis of previous Microsoft Security Response Center (MSRC) cases, avoiding use of banned APIs is one actionable way to remove many vulnerabilities. The "SDL Banned APIs" check-in policy provided with this template helps you enforce this in your project. Check the "Setup check-in policies" task for information on how to ensure this.

Sections marked as shared in shipping binaries represent a security threat. Use properly secured dynamically created shared memory objects instead.

All ASP.NET pages that require authentication must set the System.Web.UI.Page.ViewStateUserKey property to a unique value per user (such as the user's session ID) to help protect the application against Cross-Site Request Forgery attacks.

Ensure that the application domain group is granted only execute permissions only on your stored procedures. Do not grant any other permission on your database to any other user or group.

All web applications accessing databases should always use stored procedures.

Do not use "exec @sql" construct in your stored procedures.

## Implementation 4.3 — Perform Periodic Static Code Analysis [XLS-Implementation-4.3]

Project teams should perform static analysis of source code. Static analysis of source code provides a scalable capability for security code review and can help ensure that secure coding policies are being followed. Static code analysis by itself is generally insufficient to replace a manual code review. The security team and security advisors should be aware of the strengths and weaknesses of static analysis tools and be prepared to augment static analysis tools with other tools or human review as appropriate.

*Additional notes:* A list of Microsoft's SDL-related Implementation tools can be found at: http://www.microsoft.com/security/sdl/adopt/tools.aspx

The SDL Pro Network Tools members can be accessed at:http://www.microsoft.com/security/sdl/adopt/pronetwork.aspx
Run a static code analysis tool against all managed code and fix all security sensitive issues discovered.

If you are writing code in Visual Studio or .NET Framework, the FxCop code analysis tool can be used in this situation. If using FxCop, you must fix all violations that fall within the "Security rules" for the version used. 

Note that there are slight differences in the security rules for FXCop 1.35 (from Visual Studio 2005) and FXCop 1.36 (from Visual Studio 2008). These are explained in this code analysis blog entry: http://blogs.msdn.com/fxcop/archive/2008/01/07/faq-which-rules-shipped-in-which-version.aspx

.Net Framework version 3.5 requires FXCop 1.36 

Security rules for FXCop 1.35 can be found here: http://msdn.microsoft.com/en-us/library/ms182296(VS.80).aspx
Security rules for FXCop 1.36 can be found here: http://msdn.microsoft.com/en-us/library/ms182296.aspx

## Verification 5.0 — Verification Practices [XLS-Verification-5.0]

Verification is the point at which the software is functionally complete and is tested against security and privacy goals outlined in the requirements and design phase.

## Verification 5.1 — Perform Dynamic Code Analysis [XLS-Verification-5.1]

Run-time verification of software programs is necessary to ensure that a program’s functionality works as designed. This verification task should specify tools that monitor application behavior for memory corruption, user privilege issues, and other critical security problems. The SDL process uses run-time tools, along with other techniques such as fuzz testing, to achieve desired levels of security test coverage.

*Additional notes:* A list of Microsoft's SDL-related Implementation tools can be found at: http://www.microsoft.com/security/sdl/adopt/tools.aspx

The SDL Pro Network Tools members can be accessed at:http://www.microsoft.com/security/sdl/adopt/pronetwork.aspx

## Verification 5.2 — Perform Fuzz Testing [XLS-Verification-5.2]

Fuzz testing is a specialized form of dynamic analysis used to induce program failure by deliberately introducing malformed or random data to an application. The fuzz testing strategy is derived from the intended use of the application and the functional and design specifications for the application. The security advisor may require additional fuzz tests or increases in the scope and duration of fuzz testing.

*Additional notes:* A list of Microsoft's SDL-related Implementation tools can be found at: http://www.microsoft.com/security/sdl/adopt/tools.aspx

The SDL Pro Network Tools members can be accessed at:http://www.microsoft.com/security/sdl/adopt/pronetwork.aspx

## Verification 5.3 — Conduct Attack Surface Review [XLS-Verification-5.3]

It is common for an application to deviate significantly from the functional and design specifications created during the requirements and design phases of a software development project. Therefore, it is critical to re-review threat models and attack surface measurement of a given application when it is code complete. This review ensures that any design or implementation changes to the system have been accounted for, and that any new attack vectors created as a result of the changes have been reviewed and mitigated. 

In addition, all security bugs identified in your project should be reviewed against the security bug bar/quality criteria established for your project to ensure you have met the criteria or understand the potential attack surface associated with any bugs granted exceptions.

## Release 6.0 — Release Practices [XLS-Release-6.0]

In preparation for releasing a product, the team must create the incident response plan, perform the Final Security Review and archive all pertinent data for post-release servicing of the software.

## Release 6.1 — Create an Incident Response Plan [XLS-Release-6.1]

Every software release subject to the requirements of the SDL must include an incident response plan. Even programs with no known vulnerabilities at the time of release can be subject to new threats that emerge over time. The incident response plan should include:
• An identified sustained engineering (SE) team, or if the team is too small to have SE resources, an emergency response plan (ERP) that identifies the appropriate engineering, marketing, communications, and management staff to act as points of first contact in a security emergency.
• On-call contacts with decision-making authority that are available 24 hours a day, seven days a week.
• Security servicing plans for code inherited from other groups within the organization.
• Security servicing plans for licensed third-party code, including file names, versions, source code, third-party contact information, and contractual permission to make changes (if appropriate).

## Release 6.2 — Perform a Final Security Review [XLS-Release-6.2]

The Final Security Review (FSR) is a deliberate examination of all the security activities performed on a software application prior to release. The FSR is performed by the security advisor with assistance from the regular development staff and the security and privacy team leads. The FSR is not a “penetrate and patch” exercise, nor is it a chance to perform security activities that were previously ignored or forgotten. The FSR usually includes an examination of threat models, exception requests, tool output, and performance against the previously determined quality gates or bug bars. The FSR results in one of three different outcomes:

• Passed FSR. All security and privacy issues identified by the FSR process are fixed or mitigated.
• Passed FSR with exceptions. All security and privacy issues identified by the FSR process are fixed or mitigated and/or all exceptions are satisfactorily resolved. Those issues that cannot be addressed (for example, vulnerabilities posed by legacy “design level” issues) are logged and corrected in the next release.
• FSR with escalation. If a team does not meet all SDL requirements and the security advisor and the product team cannot reach an acceptable compromise, the security advisor cannot approve the project, and the project cannot be released. Teams must either address whatever SDL requirements that they can prior to launch or escalate to executive management for a decision.

## Release 6.3 — Archive all Release Data [XLS-Release-6.3]

Software release to manufacturing (RTM) or release to Web (RTW) is conditional on completion of the SDL process. The security advisor assigned to the release must certify (using the FSR and other data) that the project team has satisfied security requirements. Similarly, for all products that have at least one component with a Privacy Impact Rating of P1, the project’s privacy advisor must certify that the project team has satisfied the privacy requirements before the software can be shipped.

In addition, all pertinent information and data must be archived to allow for post-release servicing of the software. This includes all specifications, source code, binaries, private symbols, threat models, documentation, emergency response plans, license and servicing terms for any third-party software and any other data necessary to perform post-release servicing tasks.

## Statements outside the extracted sections (added by the verify pass, 2026-10-03)

The extract pass excluded the introduction, the "About" section, the conclusion and the document's text-box callouts. These carry the following modal-bearing statements, verbatim from the .doc.

- **[PROC-intro-minimum-threshold]** (recommendation; Simplified Implementation of the Microsoft SDL > Introduction) The process outlined in this paper sets a minimum threshold for SDL compliance. That said, organizations aren’t uniform – development teams should apply the SDL in a way that is suitable to the human talent and resources available, but doesn’t compromise organizational security goals.
- **[PROC-core-concepts]** (requirement; Simplified Implementation of the Microsoft SDL > About the Microsoft Security Development Lifecycle) The Microsoft SDL is based on three core concepts—education, continuous process improvement, and accountability. The ongoing education and training of technical job roles within a software development group is critical. The appropriate investment in knowledge transfer helps organizations to react appropriately to changes in technology and the threat landscape. Because security risk is not static, the SDL places heavy emphasis on understanding the cause and effect of security vulnerabilities and requires regular evaluation of SDL processes and introduction of changes in response to new technology advancements or new threats. Data is collected to assess training effectiveness, in-process metrics are used to confirm process compliance and post-release metrics help guide future changes. Finally, the SDL requires the archival of all data necessary to service an application in a crisis. When paired with detailed security response and communication plans, an organization can provide concise and cogent guidance to all affected parties.
- **[PROC-conclusion-guide]** (recommendation; Simplified Implementation of the Microsoft SDL > Conclusion) While the process outlined above sets a minimum threshold for SDL compliance, the SDL is not “one size fits all.”  Development teams should use this document as a guide for implementing the SDL in a fashion appropriate to the time, resources and business practices of the organization.
- **[CALLOUT-1]** (descriptive; text-box callout 1 of 7 (document text-box story; anchored beside the body text, page not recoverable from the .doc conversion)) A centralized, internal advisory group is preferable; it provides organizational context and process knowledge beyond the capability of external experts.
- **[CALLOUT-2]** (recommendation; text-box callout 2 of 7 (document text-box story)) Focus should be placed on the accuracy of the output at each stage. Fancy reports with incomplete or incorrect information are a waste of time and resources.
- **[CALLOUT-3]** (recommendation; text-box callout 3 of 7 (document text-box story)) A formal exception or bug deferral method should be considered as part of any software development process. Many applications are based on legacy designs and code, so it may be necessary to defer certain security or privacy measures as a result of technical constraints.
- **[CALLOUT-4]** (descriptive; text-box callout 4 of 7 (document text-box story)) The preferred method for threat modeling is to use the SDL Threat Modeling Tool. The SDL Threat Modeling Tool is based on the STRIDE threat classification taxonomy.
- **[CALLOUT-5]** (recommendation; text-box callout 5 of 7 (document text-box story)) Generally speaking, development teams should decide the optimal frequency for performing static analysis – to balance productivity with adequate security coverage.
- **[CALLOUT-6]** (requirement; text-box callout 6 of 7 (document text-box story)) Any issues identified during penetration testing must be addressed and resolved before the project is approved for release.

