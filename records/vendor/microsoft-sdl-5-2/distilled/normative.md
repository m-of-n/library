---
schema: "library-normative/v1"
id: microsoft-sdl-5-2-normative
record: microsoft-sdl-5-2
kind: normative
type: normative
title: "microsoft-sdl-5-2 — normative content, verbatim"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

Source: *Microsoft Security Development Lifecycle (SDL) Process Guidance – Version 5.2* (May 23, 2012), sha256 `108cd2ee…75f2`. Text from the document XML with original case. Grouped by the source headings (Phase › activity › Requirements/Recommendations). Each statement carries its requirement id `[R-NNNN]`; statements marked `[context]` are prose inside requirement sections that carries no modal and is not in `requirements.yaml`. Part II reproduces the normative tables (Appendices B, M, N) verbatim from the capture.

# Part I — statements by section


## Pre-SDL Requirements: Security Training > Education and Awareness > Security Requirements

- [R-0001] (requirement) All developers, testers, and program managers must complete at least one security training class each year. Individuals who have not taken a class in the basics of security design, development, and testing must do so.
- [R-0002] (requirement) At least 80 percent of the project team staff who work on products or services must be in compliance with the standards listed earlier before their product or service is released. Relevant managers must also be in compliance with these standards. Project teams are strongly encouraged to plan security training early in the development process so that training can be completed as early as possible and have a maximum positive effect on the project’s security.

## Pre-SDL Requirements: Security Training > Education and Awareness > Security Recommendations

- [R-0003] (recommendation) Microsoft recommends that staff who work in all disciplines read the following publications:
  - Writing Secure Code, Second Edition (ISBN 9780735617223; ISBN: 0-7356-1722-8).
  - Uncover Security Design Flaws Using the STRIDE Approach (ISBN: 0-7356-1991-3).

## Pre-SDL Requirements: Security Training > Education and Awareness > Privacy Recommendations

- [R-0004] (recommendation) Microsoft recommends that staff who work in all disciplines read the following documents:
  - Appendix A: Privacy at a Glance (Sample)
  - Microsoft Privacy Guidelines for Developing Software Products and Services

## Phase One: Requirements > Project Inception > Security Requirements

- [R-0005] (requirement) Develop and answer a short questionnaire to verify whether your development team is subject to Security Development Lifecycle (SDL) policies. The questionnaire has two possible outcomes:
  1. If the project is subject to SDL policies, it must be assigned a security advisor who serves as the point of contact for its Final Security Review (FSR). It is in the project team’s interest to register promptly and establish the security requirements for which they will be held accountable. The team will also be asked some technical questions as part of a security risk assessment to help the security advisor identify potential security risks. (See Cost Analysis in this document.)
  2. If the project is not subject to SDL policies, it is not necessary to assign a security advisor and the release is classified as exempt from SDL security requirements.
  - Identify the team or individual that is responsible for tracking and managing security for the product. This team or individual does not have sole responsibility for ensuring that a software release is secure, but the team or individual is responsible for coordinating and communicating the status of any security issues. In smaller product groups, a single program manager might take on this role.
  - Ensure that bug reporting tools can track security issues and that a database can be queried dynamically for all security bugs at any time. The purpose of this query is to examine unfixed security issues in the FSR. The project’s bug tracking system must accommodate the bug bar ranking value recorded with each bug.
  - Define and document the project’s security bug bar. This set of criteria establishes a minimum level of quality. Defining it at the start of the project improves understanding of risks associated with security issues and enables teams to identify and fix security issues during development. The project team must negotiate a bug bar approved by the security advisor with project-specific clarifications and (as appropriate) more stringent security requirements specified by the security advisor. The bug bar must never be relaxed, though, even as the project’s release date nears. Bug bar examples can be found in Appendix M: SDL Privacy Bug Bar and Appendix N: SDL Security Bug Bar.
  - Include third-party code licensing security requirements in all new contracts. If your product contains licensed third-party code or hardware that is newly contracted in the current release, you should ensure that there is a provision in the licensing contract that requires the third party to provide proof of compliance with a predefined list of SDL requirements. Depending upon your company's relationship with the third party, this can include things such as the source code itself for verification, security tool output and logs, or independent verification performed by an outside agent.

## Phase One: Requirements > Project Inception > Privacy Requirements

- [R-0006] (requirement) Identify the privacy advisor who will serve as your team’s first point of contact for privacy support and additional resources.
- [R-0007] (requirement) Identify the team member responsible for privacy for the project. This person is typically called the privacy lead or, sometimes, the privacy champion.
- [R-0008] (requirement) Define and document the project’s privacy bug bar (see the preceding Security Requirements section).

## Phase One: Requirements > Project Inception > Security Recommendations

- [R-0009] (recommendation) It is useful to create a security plan document during the Design phase to outline the processes and work items your team will follow to integrate security into their development process. The security plan should identify the timing and resource requirements that the Security Development Lifecycle prescribes for individual activities. These requirements should include:
  - Team training.
  - Threat modeling.
  - Security push.
  - Final Security Review (FSR).
- [R-0010] (recommendation) The security plan should reflect a development team’s overall perspective on security goals, challenges, and plans. Security plans can change, but articulating one early helps ensure that no requirements are overlooked and avoids last-minute surprises. A sample security plan is included in Appendix O.
- [R-0011] (recommendation) Consider using a tool to track security issues by cause and effect. This information is very important to have later in a project. Ensure that the bug reporting tool used includes fields with the STRIDE values in the following lists (definitions for these values are available in Appendix B: Security Definitions for Vulnerability Work Item Tracking).
- [R-0012] (recommendation) The tool’s Security Bug Effect field should be set to one or more of the following STRIDE values:
  - Not a Security Bug
  - Spoofing
  - Tampering
  - Repudiation
  - Information Disclosure
  - Denial of Service
  - Elevation of Privilege
  - Attack Surface Reduction
- [R-0013] (recommendation) It is also important to use the Security Bug Cause field to log the cause of a vulnerability (this field should be mandatory if Security Bug Effect is anything other than Not a Security Bug).
- [R-0014] (recommendation) The Security Bug Cause field should be set to one of the following values:
  - Not a security bug
  - Buffer overflow/underflow
  - Arithmetic error (for example, integer overflow)
  - SQL/Script injection
  - Directory traversal
  - Race condition
  - Cross-site scripting
  - Cryptographic weakness
  - Weak authentication
  - Weak authorization/Inappropriate permission or access control list (ACL)
  - Ineffective secret hiding
  - Unlimited resource consumption (Denial of Service [DoS])
  - Incorrect/No error messages
  - Incorrect/No pathname canonicalization
  - Other
- [R-0015] (recommendation) Be sure to configure bug reporting tools correctly; limit access to bugs with security implications to the project team and security advisors only.

## Phase One: Requirements > Cost Analysis > Security Requirements

- [R-0016] (requirement) A security risk assessment (SRA) is a mandatory exercise to identify functional aspects of the software that might require deep security review. Given that program features and intended functionality might be different from project to project, it is wise to start with a simple SRA and expand it as necessary to meet the project scope.
- [R-0017] (requirement) Such assessments must include the following information:
  - What portions of the project will require threat models before release.
  - What portions of the project will require security design reviews before release.
  - What portions of the project will require penetration testing (pen testing) by a mutually agreed-upon group that is external to the project team. Any portion of the project that requires pen testing must resolve issues identified during pen testing before it is approved for release.
  - Any additional testing or analysis requirements the security advisor deems necessary to mitigate security risks.
  - Clarification of the specific scope of fuzz testing requirements. (Verification Phase: Security and Privacy Testing discusses fuzz testing.)
- [R-0018] (requirement) Note: SRA guidelines are discussed in Chapter 8 of The Security Development Lifecycle, along with a sample SRA on the DVD included with the book.

## Phase One: Requirements > Cost Analysis > Privacy Requirements

- [R-0019] (requirement) Complete the Initial Assessment of the Appendix C: SDL Privacy Questionnaire. An initial assessment is a quick way to determine a project’s Privacy Impact Rating and to estimate how much work is necessary to comply with Microsoft Privacy Guidelines for Developing Software Products and Services.
- [R-0020] (requirement) The Privacy Impact Rating (P1, P2, or P3) measures the sensitivity of the data your software will process from a privacy point of view. More information about Privacy Impact Ratings can be found in Chapter 8 of The Security Development Lifecycle. General definitions of privacy impact are defined as:
  - P1 High Privacy Risk. The feature, product, or service stores or transfers PII or error reports, monitors the user with an ongoing transfer of anonymous data, changes settings or file type associations, or installs software.
  - P2 Moderate Privacy Risk. The sole behavior that affects privacy in the feature, product, or service is a one-time, user-initiated, anonymous data transfer (for example, the user clicks a link and goes out to a website).
  - P3 Low Privacy Risk. No behaviors exist within the feature, product, or service that affect privacy. No anonymous or personal data is transferred, no PII is stored on the machine, no settings are changed on the user's behalf, and no software is installed.
- [R-0021] (requirement) Product teams must complete only the work that is relevant to their Privacy Impact Rating. Complete the initial assessment early in the product planning/requirements phase, before you write detailed specifications or code.

## Phase One: Requirements > Cost Analysis > Privacy Recommendations

- [R-0022] (recommendation) If your Privacy Impact Rating is P1 or P2, understand your obligations and try to reduce your risk. Early awareness of all the required steps for deploying a project with high privacy risk might help you decide whether the costs are worth the business value gained. Review the guidance in Understand Your Obligations and Try to Lower Your Risk of Appendix C: SDL Privacy Questionnaire. If your Privacy Impact Rating is P1, schedule a “sanity check” with your organization's privacy expert. This person should be able to guide you through implementation of a high-risk project and might have other ideas to help you reduce your risk.

## Phase Two: Design > Establish and Follow Best Practices for Design > Security Requirements

- [R-0023] (requirement) Complete a security design review with a security advisor for any project or portion of a project that requires one. Some low-risk components might not require a detailed security design review.
- [R-0024] (requirement) The AllowPartiallyTrustedCallersAttribute (APTCA) enables an assembly to be called by untrusted code. APTCA behavior is different depending on the version of the framework, but the general effect is the same: potentially dangerous functionality is now exposed to partially trusted code, and the effects of this additional attack surface exposure have to be mitigated by security checks, strong enforcement mechanisms, and review. In order to comply with this requirement, you should follow these steps:
  1. Determine whether or not your assembly has enabled the AllowPartiallyTrustedCallersAttribute. You may do this by either looking for the annotations in your source code or using tools like FxCop which will flag usage. If you determine that this attributes is not enabled, you are compliant with this requirement, no review is required, and you may skip the rest of these steps.
  2. If your assembly has enabled the AllowPartiallyTrustedCallers attribute, your assembly needs to be reviewed by project security experts.
  - For online services, all new releases must use the Relying Party Suite (RPS) v4.0 SDK. RPS provides significant security advantages over the current Passport Manager (PPM) SDK; most important being the elimination of the shared symmetric encryption keys, which mitigates security issues involving key distribution, deployment, and administration. This also provides a significantly reduced cost of key revision.
  - (Updated for SDL 5.2) User Account Control (UAC) is a security feature in Windows Vista, Windows 7, Windows Server® 2008, and Windows Server 2008 R2. It is intended to help the transition to regular use of non-administrative privilege by client applications.
  - (Updated for SDL 5.2) Comply with UAC best practices and ensure that your application runs with least privilege whenever possible. Exit criteria for this requirement is confirmation from the project team that it has analyzed and minimized the need for elevated privileges and followed best practices for operation in a UAC environment. Highly privileged features of the application (such as those that perform administrative functions) are separated out and placed behind an elevation prompt as appropriate. Following this requirement enables teams to design and develop their applications with a standard user in mind. This results in a reduced attack surface exposed by applications, which increases the security of the user and the system.
  - If a program’s users require an open port in the firewall, then the code that listens on the port must comply with certain quality requirements. Prohibited and permitted actions are covered in the bulleted list that follows. See Appendix D: Firewall Rules and Requirements for additional information. For a discussion of Windows Firewall integration and best practices, please visit http://msdn.microsoft.com/en-us/library/bb736286(VS.85).aspx.
  - The following actions are prohibited:
  - Except for security products, disabling of the firewall or changing the state of the firewall. The firewall must only be disabled by explicit user action.
  - Any service or feature that adds, changes, or removes firewall rules automatically at runtime. Except at setup time (that is, during the installation process), programs, features, and services that are not designed specifically as firewall management utilities must not change firewall settings unless the user has explicitly initiated some action.
  - Any service or feature that allows a port to be opened or a rule to be enabled by a user without administrative privileges. A user must be acting as an administrator in order to change the settings of the firewall, and no service or feature (both Windows and non-Windows) must bypass this restriction.
  - Silent activation or enabling of any feature that permits other programs to receive unsolicited traffic. For example, the RemoteAdmin feature permits other RPC-based programs to receive unsolicited traffic. In such cases, the system must obtain user consent before activating such functionality.
  - Programs, services, and features may not configure an external device (for example, a NAT gateway) without user consent.
  - Any interference with Post Setup Security Update or similar functionality designed to ensure that the system is up-to-date prior to accepting incoming traffic without user consent.
  - Creation of inbound firewall rules unless the feature or service will receive unsolicited inbound traffic.
  - The following actions are permitted:
  - Programs, services, and features may define a firewall rule and leave it disabled for the sake of making it convenient for the user to enable the rule later on.
  - All cryptography must comply with the Microsoft Cryptographic Standards for SDL-covered products. Adhere to the SDL crypto requirements, which at a high-level are:
  - Use AES for symmetric enc/dec.
  - Use 128-bit or better symmetric keys.
  - Use RSA for asymmetric enc/dec and signatures.
  - Use 2048-bit or better RSA keys.
  - Use SHA-256 or better for hashing and message-authentication codes.
  - Support certificate revocation.
  - Limit lifetimes for symmetric keys and asymmetric keys without associated certificates.
  - Support cryptographically secure versions of SSL (must not support SSL v2).
  - Use cryptographic certificates reasonably and choose reasonable certificate validity periods.
  - (New for SDL 5.2) Use Transport Layer encryption securely. Properly use Transport Layer Security (TLS) when communicating with another entity, and verify that your service checks the Common Name attribute to be sure it matches the host with which you intended to communicate. Verify that your service consults a certificate revocation list (CRL) for an updated list of revoked certificates at a frequent interval. If your service is accessible via a browser, confirm that no security warnings appear at any visited URL for any supported browser.
  - Mitigate against Cross-Site Scripting (XSS), which is a client-side code injection attack that allows arbitrary code execution in your customer’s browser. XSS has been used by attackers to capture credentials, financial data, and other sensitive information. It has also been used to map back-end server space and in cases of vulnerable browser plug-ins, completely compromise a customer’s machine. Perform all pre-approved tests that have been explicitly approved by your security advisor. If this is an ASP.NET application, this should include use of CAT.NET. All test results should be uploaded into your project tracking system to validate against project requirements. All issues found by approved tests must be triaged with the security advisor and fixed in accordance with the SDL bug bar. Suggested tools include: Web Protection (Anti-XSS) Library, CAT.NET, and Watcher (from Casaba Security for the MAC portion).

## Phase Two: Design > Establish and Follow Best Practices for Design > Privacy Requirements

- [R-0025] (requirement) If your project has a Privacy Impact Rating of P1, identify a compliant design based on the concepts, scenarios, and rules in the Microsoft Privacy Guidelines for Developing Software Products and Services. Definitions of privacy rankings (P1, P2, P3) can be found in Cost Analysis and Chapter 8 of The Security Development Lifecycle. You can find additional guidance in Appendix C: SDL Privacy Questionnaire.

## Phase Two: Design > Establish and Follow Best Practices for Design > Security Recommendations

- [R-0026] (recommendation) Include in all functional and design specifications a section that describes impacts on security.
- [R-0027] (recommendation) Write a security architecture document that provides a description of a software project that focuses on security. Such a document should complement and reference existing traditional development collateral without replacing it. A security architecture document should contain, at a minimum:
  - (Updated for SDL 5.2) Attack surface measurement. After all design specifications are complete, define and document what the program’s default and maximum attack surfaces are. The size of the attack surface indicates the likelihood of a successful attack. Therefore, your goal should be to minimize the attack surface. You can find additional background information in the papers Fending Off Future Attacks by Reducing Attack Surface and Measuring Relative Attack Surfaces. Use of tools like Attack Surface Analyzer (ASA) and Web Application Configuration Analyzer (WACA) should be required for existing products to identify the existing attack surface.
  - Product structure or layering. Highly structured software with well-defined dependencies among components is less likely to be vulnerable than software with less structure. Ideally, software should be structured in a layered hierarchy so that higher components (layers) depend on lower ones. Lower layers should never depend on higher ones. Developing this sort of layered design is difficult and might not be feasible with legacy or pre-existing software. However, teams that develop new software should consider layered and highly structured designs.
  - Minimize default attack surface/enable least privilege.
  - All feature specifications should consider whether the features should be enabled by default. If a feature is not used frequently, you should disable it. Consider carefully whether to enable by default those features that are used infrequently.
  - If the program needs to create new user accounts, ensure that they have as few permissions as possible for the required function and that they also have strong passwords.
  - Be very aware of access control issues. Always run code with the fewest possible permissions. When code fails, find out why it failed and fix the problem instead of increasing permissions. The more permissions any code has, the greater its exposure to abuse.
  - Default installation should be secure. Review functionality and exposed features that are enabled by default and constitute the attack surface carefully for vulnerabilities.
  - Consider a defense-in-depth approach. The most exposed entry points should have multiple protection mechanisms to reduce the likelihood of exploitation of any security vulnerabilities that might exist. If possible, review public sources of information for known vulnerabilities in competitive products, analyze them, and adjust your product’s design accordingly.
  - If the program is a new release of an existing product, examine past vulnerabilities in previous versions of the product and analyze their root causes. This analysis might uncover additional instances of the same classes of problems.
  - Deprecate outdated functionality. If the product is a new release of an existing product, evaluate support for older protocols, file formats, and standards, and strongly consider removing them in the new release. Older code written when security awareness was less prevalent almost always contains security vulnerabilities.
  - Conduct a security review of all sample source code released with the product and use the same level of scrutiny as for object code released with the product.
  - If the product is a new release of an existing product, consider migration of any possible legacy code from unmanaged code to managed code.
  - Implement any new code using managed code whenever possible.
  - When developing with managed code, take advantage of .NET security features:
  - Refuse unneeded permissions.
  - Request optional permissions.
  - Use CodeAccessPermission Assert and LinkDemand carefully. Use Assert in as small a window as possible.
  - Disable tracing and debugging before deploying ASP.NET applications.
  - Watch for ambiguous representation issues. Hackers will try to force code to follow a dangerous path or URL by hiding their intent in escape characters or obscure conventions. Always design code to deal with full canonical representations, rather than acting on externally provided data. The canonical representation of something is the standard, most direct, and least ambiguous way to represent it.
  - Remain informed about security issues in the industry. Attacks and threats evolve constantly, and staying current is important. Keep your team informed about new threats and vulnerabilities.
  - Ensure that everyone on your team knows about unsafe functions and coding patterns. Maintain a list of your code’s vulnerabilities. When you find new vulnerabilities, publish them. Make security everyone’s business.
  - Be careful with error messages. Sensitive information displayed in an error message can provide an attacker with privileged information, such as a file path on a server or the structure of a query. Such information makes it easier for an attacker to attack any defenses. In general, record detailed failure messages in a secure log, and give the user discreet failure messages.
  - For online services and/or LOB applications, ensure appropriate logging is enabled for forensics.
  - For online services and/or LOB applications, page flow integrity checking should be performed.
  - Hardware security design review. Conduct a high-level security design review for hardware products that are new or being updated in the current release. The goal of a high-level hardware security design review is to identify aspects of the design that could lead to security vulnerabilities. This might include checks such as:
  1. Methods of cryptographic key generation and storage.
  2. Methods of data storage, including encryption, For example, does the design meet Microsoft Cryptographic Standards?
  3. Methods of data manipulation.
  4. The "business or customer impact" of the data being manipulated and stored. For example, whether the data could be considered High Business Impact (HBI), Moderate Business Impact (MBI), or Low Business Impact (LBI) by the product's expected customers.
  5. Use of standard versus custom protocols.
  6. Presence of JTAG*/debugging back doors.
  - * Joint Test Action Group (JTAG) is the common name used for the IEEE 1149.1 standard entitled Standard Test Access Port and Boundary-Scan Architecture for testing/debugging access ports using a boundary scan.
  7. Firmware upgrade features and procedures (security, process, and scalability).
  8. Firmware development process – /analyze, fuzzing and/or other security tools may be applicable.
  - Integration-points security design review. Enterprise server application suites, software-as-a-service (SaaS) offerings, and security products interact with a variety of other products and platforms in order to provide robust, enterprise-focused services. It is not sufficient to threat model these products by themselves because the points of interaction with other products are the source of many nuanced security issues. Conduct an integration-points security design review with dependent product teams across your end-to-end scenarios. Examples of products that should do this are:
  - Products designed to handle high business impact (HBI) data.
  - Enterprise applications and services.
  - Security products.
  - SaaS offerings.
  - The exit criteria for this recommendation is that the product teams and security reviewers/owners have reviewed and are satisfied with the security threat mitigations and validations provided at each point of integration.
  - Strong log-out and session management. Proper session handling is one of the most important parts of web application security. At the most fundamental level, sessions must be initiated, managed, and terminated in a secure manner. If a product employs an authenticated session, it must begin as an encrypted authentication event to avoid session fixation.
  - A session identifier/token must never be transmitted via the URL to avoid side-jacking via the referrer header or browser history.
  - All session data must be maintained on the server, not the client, to avoid tampering.
  - Sessions must be completely terminated on the server side via logout and timeout mechanisms. When multiple sessions are tied to a single authentication event, all of the sessions tied to that event must be terminated by logout/time-out.
  - The following items must be met as part of the exit criteria for this recommendation:
  - When multiple sessions are tied to a single user identity, they must be collectively terminated on the server side at timeout or logout.
  - Authentication events must invalidate unauthenticated sessions and create a new session identifier.
  - Logout functionality is available on every page.
  - Session state, outside of a single identifier, is maintained on the server and not accepted from the user (including via cookie or header).
  - Session tokens are not present in the URI.
  - Timeout functionality is present and timeout thresholds are documented along with the rationale.
  - Apply no-open header to user-supplied downloadable files. Use the HTTP Header X-Download-Options: noopen for each HTTP file download response that may contain user-controllable content. Recommended tool: Casaba Passive Security Auditor.

## Phase Two: Design > Establish and Follow Best Practices for Design > Privacy Recommendations

- [R-0028] (recommendation) If your project has a privacy impact rating of P2, identify a compliant design based on the concepts, scenarios, and rules in the Microsoft Privacy Guidelines for Developing Software Products and Services. Additional guidance can be found in Appendix C: SDL Privacy Questionnaire.
- [R-0029] (recommendation) Use FxCop to enforce design guidelines in managed code. Many rules are built in by default.

## Phase Two: Design > Risk Analysis > Security Requirements

- [R-0030] (requirement) Complete threat models for all functionality identified during the cost analysis phase. Threat models typically must consider the following areas:
  - All projects. All code exposed on the attack surface and all code written by or licensed from a third party.
  - New projects. All features and functionality.
  - Updated versions of existing projects. New features or functionality added in the updated version.
  - Ensure that all threat models meet minimal threat model quality requirements. All threat models must contain data flow diagrams, assets, vulnerabilities, and mitigation. Threat modeling can be done in a variety of ways, using either tools or documentation/specifications to define the approach. For assistance in creating threat models, see “Chapter 9: Stage 4 – Risk Analysis” in The Security Development Lifecycle book or consult other guidance listed in Resources.
  - Have all threat models and referenced mitigations reviewed and approved by at least one developer, one tester, and one program manager. Ask architects, developers, testers, program managers, and others who understand the software to contribute to threat models and to review them. Solicit broad input and reviews to ensure the threat models are as comprehensive as possible.
  - Confirm that threat model data and associated documentation (functional/design specifications) has been stored using the document control system used by the product team.

## Phase Two: Design > Risk Analysis > Privacy Requirements

- [R-0031] (requirement) If a project has a privacy impact rating of P1:
  - Complete Detailed Privacy Analysis in Appendix C: SDL Privacy Questionnaire. The questions will be customized to the behaviors specified in the initial assessment.
  - Hold a design review with your privacy subject-matter expert.
- [R-0032] (requirement) If your project has a privacy impact rating of P2:
  - Complete the Detailed Privacy Analysis in Appendix C: SDL Privacy Questionnaire. The questions will be customized to the behaviors specified in the initial assessment.
  - Hold a design review with your privacy subject-matter expert only if one or more of these criteria apply:
  - The privacy subject-matter expert requests a design review.
  - You want confirmation that the design is compliant.
  - You wish to request an exception.
- [R-0033] (requirement) If your project has a privacy impact rating of P3, there are no privacy requirements during this phase.

## Phase Two: Design > Risk Analysis > Security Recommendations

- [R-0034] (recommendation) The person who manages the threat modeling process should complete threat modeling training before working on threat models.
- [R-0035] (recommendation) After all specifications and threat models have been completed and approved, the process for making changes to functional or design specifications—known as design change requests (DCRs—should include an assessment of whether the changes alter existing threats, vulnerabilities, or the effectiveness of mitigations.
- [R-0036] (recommendation) Create an individual work item for each vulnerability listed in the threat model so that your quality assurance team can verify that the mitigation is implemented and functions as designed.
- [R-0037] (recommendation) (New for SDL 5.2) Follow NEAT security user experience (UX) guidance to ensure that warnings are Necessary, Explained, Actionable, and Tested.
  - Microsoft has produced guidance to help engineers design better warnings. The guidance is summarized in the four-letter acronym NEAT—Necessary, Explained, Actionable, and Tested. The objective of NEAT is to improve security warnings in products by making sure they are:
  - Necessary. Does the user really need to be presented with the decision?
  - Explained. Does the UX present all the information the user needs to make this decision?
  - Actionable. Is there a set of steps users can take to make good decisions in both benign and malicious scenarios?
  - Tested. Has the warning been reviewed by multiple engineers to make sure users will understand how to respond to the warning?
  - Improve security-related prompts in your products to enable customers to make good security decisions that protect them from harm.
  - Users face a barrage of decisions about whom and what to trust, and when to be concerned about their security. These security decisions arise when users initiate activities like installing an executable from the web, using an application that needs to get through the firewall, and allowing a web application to access their sensitive data. These decisions also arise when a product prompts the user to take an action to improve their security, such as when Windows prompts the user to reboot or to turn the Windows Firewall on. With attacks moving “up the stack” from silent code exploits to social engineering, good security UX gives you a chance to help the user avoid running malicious software.

## Phase Three: Implementation > Creating Documentation and Tools for Users That Address Security and Privacy > Security Recommendations

- [R-0038] (recommendation) Development management, program management, and UX teams should meet to identify and discuss what information users will need to use the software program securely. Define realistic use and deployment scenarios in functional and design specifications. Consider user needs for documentation and tools.
- [R-0039] (recommendation) User experience teams should establish a plan to create user-facing security documentation. This plan should include appropriate schedules and staffing needs. Communicating the security aspects of a program to the user in a clear and concise fashion is as important as ensuring that the product code or functionality is free of vulnerabilities.
- [R-0040] (recommendation) For new versions of existing programs, solicit or gather comments about what problems and challenges users faced when securing prior versions.
- [R-0041] (recommendation) Make information about secure configurations available separately or as part of the default product documentation and/or help files. Consider the following issues:
  - The program will follow the best practice of reducing the default attack surface. However, what should users know if they need to activate additional functionality? What risks will they be exposed to?
  - Are there usage scenarios that allow users to lock down or harden the program more securely than the default configuration without losing functionality? Inform users about how to configure the program for these situations. Better yet, provide easy-to-use templates that implement such configurations.
  - Inform users about security best practices, such as removing guest accounts and default passwords. External security notes from threat modeling are good sources of information to consider.
  - For programs that use network or Internet communications, describe all communications channels and ports, protocols, and communications configuration options (and their associated security impacts).
  - To support earlier versions of the software and older protocols, it is often necessary to operate less securely. Do not enable insecure protocols in the default configuration. You might still need to deliver them with the release, so inform users about the security implications of older protocols and backward compatibility. Inform users about these trade-offs and how to disable older compatibility modes to achieve the best possible security.
  - Tell users how they can ensure safe use of the program or take advantage of built-in security and privacy features.

## Phase Three: Implementation > Creating Documentation and Tools for Users That Address Security and Privacy > Privacy Recommendations

- [R-0042] (recommendation) If the program contains privacy controls, create deployment guides for organizations to help them protect their users’ privacy (for example, Group Policy controls).
- [R-0043] (recommendation) Create content to help users protect their privacy when using the program (for example, secure your subnet).

## Phase Three: Implementation > Establish and Follow Best Practices for Development > Security Requirements

- [R-0044] (requirement) (Promoted for SDL 5.2) Components must have no hard dependencies on the NTLM protocol. All explicit uses of the NTLM package for network authentication must be replaced with the Negotiate package. All client authentication calls must provide a properly formatted target name—service principal name (SPN). The purpose of the requirement is to enable systems to use Kerberos in place of NTLM whenever possible.
- [R-0045] (requirement) (Promoted for SDL 5.2) HTTPOnly Cookies. To mitigate the risk of information disclosure with a cross-site scripting attack, a new attribute was introduced to cookies for Internet Explorer 6 Service Pack 1 (SP1) and is now in use in all current browsers. This attribute specifies that a cookie is not accessible through script. By using HTTP-only cookies, a web application reduces the possibility that sensitive information contained in the cookie can be stolen via script. Watcher, a web security testing tool, can help you meet this recommendation.
- [R-0046] (requirement) All HTTP-based applications that use cookies must specify HttpOnly in the cookie definition for all cookies not explicitly required by legitimate scripts in the web page. For example:
- [R-0047] (requirement) Set-Cookie: USER=123; expires=Wednesday, 10-Feb-2012 23:12:40 GMT; HttpOnly"
- [R-0048] (requirement) Use minimum code generation suite and libraries. For unmanaged, native C/C++ code, use Visual C++ 2010 as it offers all the SDL-mandated compiler and linker flags, including /GS, /DYNAMICBASE, /NXCOMPAT, and /SAFESEH. For managed code, use Visual Studio® 2008 SP1 or later. Use the currently required (or later) versions of compilers to compile options for the Win32®, Win64, WinCE, and Macintosh target platforms, as listed in Appendix E: SDL Required and Recommended Compilers, Tools, and Options for All Platforms. The biggest change in Visual Studio 2008 SP1 and later is Data Execution Prevention (DEP) support, enabled by default for all binaries, which can help protect against classes of buffer overrun.
- [R-0049] (requirement) For unmanaged C or C++ code, BinScope must indicate a "Pass" in the compiler version field for all binaries. For managed code, an attestation is required that the compiler version used to ship the product is the version outlined in this document or later.
- [R-0050] (requirement) Code analysis tools. Use the currently required (or later) versions of code analysis tools for either native C and C++ or managed (C#) code that are available for the target platforms, as listed in Appendix E: Required and Recommended Compilers, Tools, and Options for All Platforms. Run PREfast for Drivers on all kernel-mode driver source code. File bugs for each instance of each warning as required by the SDL and triage based on tool output. Ensure that all appropriate bugs are fixed.
- [R-0051] (requirement) Banned application programming interfaces (APIs). All native C and C++ code must not use banned versions of string buffer handling functions. Based on analysis of previous Microsoft Security Response Center (MSRC) cases, avoiding use of banned APIs is one actionable way to remove many vulnerabilities. For more information, see Security Development Lifecycle (SDL) Banned Function Calls and The Security Development Lifecycle (ISBN 9780735622142; ISBN-10 0-7356-2214-0), Chapter 19: SDL Banned Function Calls (pp. 241-49).
- [R-0052] (requirement) No writable shared PE sections. Sections marked as shared in shipping binaries represent a security threat. Use properly secured dynamically created shared memory objects instead. See Appendix G: SDL Requirement: No Shared Sections.
- [R-0053] (requirement) For online services and/or LOB applications, follow data input validation and output encoding requirements to address potential cross-site scripting vulnerabilities.
- [R-0054] (requirement) For online services and/or LOB applications that access a SQL database, do not use “ad-hoc” SQL queries in order to avoid SQL injection attacks.
- [R-0055] (requirement) For online services and/or LOB applications that implement web services, use an approved XML parser.
- [R-0056] (requirement) Fix issues identified by code analysis tools for managed code. Run the FxCop code analysis tool against all managed code, and fix all violations of the “Security” rules for the version of FXCop used. Note that there are slight differences in the security rules for FXCop 1.35 (from Visual Studio 2005) and FXCop 1.36 (from Visual Studio 2008). These differences are explained in the Code Analysis Team Blog. When using .NET Framework version 3.5, FXCop 1.36 must be used. Security rules for FXCop can be found at http://msdn.microsoft.com/en-us/library/ms182296(VS.80).aspx. Security rules for FXCop can be found at http://www.microsoft.com/en-us/download/details.aspx?id=6544.
- [R-0057] (requirement) Compile native code with /GS compiler. All unmanaged C and C++ code must be compiled with the /GS compiler option. /GS- (which turns off /GS) is not allowed. Verify all build files include the /GS compiler option so that all native code C and C++ binaries are compiled using this option. High-risk code (code facing the Internet, file parsers, and ActiveX controls) must have #pragma strict_gs_check(on) in an application-wide header file, such as stdafx.h. Ensure no buffers are marked as safebuffers. Verify there are no instances of compiler warning C4748.
- [R-0058] (requirement) Address Space Layout Randomization (ASLR) must be enabled on all native code (unmanaged) binaries to protect against return-to-libc class of attacks. Enabling this functionality requires the flag /DynamicBase in the PE header of all binaries. This flag can be inserted using  Visual Studio 2005 SP1 or later. Earlier versions do not contain a linker version that supports it. DumpBin can be used to manually verify if ASLR is enabled on a binary.
- [R-0059] (requirement) Do not use banned APIs. Problems arise when an attacker controls the incoming buffer and the code uses data from the buffer to determine the maximum buffer length to copy. Verify there are no banned APIs in shipping code, including sample code. Recommended tool: banned.h header or use of Visual C++ use of C4996 warnings.
- [R-0060] (requirement) Use secure methods to access databases. Creating dynamic queries using string concatenation potentially allows an attacker to execute an arbitrary query through the application. Verify that all database access is performed through a combination of parameterized inline queries, stored procedures (activated through parameterized queries or LINQ), or object names passed to Windows Azure Storage APIs that are not based on user-provided data.
- [R-0061] (requirement) Also verify:
  - If directly calling the Windows Azure Storage Blob REST APIs, all parameters should be URL-encoded with AntiXSS.Urlencode. When calling Windows Azure Table APIs, WCF Data Services should be used rather than writing REST queries directly.
  - The database is accessed via a least-privilege account with only the minimum level of access required to carry out the application's functions. This account must never have system administrator (SA), database owner (DBO), or other administrative privileges.
  - Avoid LINQ ExecuteQuery. LINQ queries are normally converted by the compiler/framework into parameterized queries to be passed to the database. However, the LINQ method ExecuteQuery allows the developer to pass arbitrary SQL commands that may have been created through string concatenation. Creating dynamic queries using string concatenation potentially allows an attacker to execute an arbitrary query through the application. This vulnerability allows for unauthorized, interactive logon to a SQL server that may result in the execution of malicious commands leading to the possible disclosure, modification, or deletion of the operating system or user data.
  - Calls to System.Data.Linq.DataContext.ExecuteQuery are prohibited. If you are using LINQ, use the standard LINQ object-relational mapping (ORM) syntax or stored procedure syntax.
  - Examples of correct code/procedures
  - Correct ORM:
  - from product in Products select product
  - Correct stored procedure:
  - SelectProducts()
  - Example of incorrect code:
  - ExecuteQuery<Products>("SELECT * FROM Products")
  - The exit criteria for this requirement is that your code contains no references to System.Data.Linq.DataContext.ExecuteQuery.
  - Avoid EXEC in stored procedures. Verify that the stored procedures contain no calls to EXEC, EXECUTE, or sp_executesql (except for calls to other stored procedures).
  - Do not use Microsoft Visual Basic® 6 to build products. Make sure that all Visual Basic code in the product, including sample code, is built with Visual Basic .NET and not Visual Basic 6. No product distributes or uses the runtime environment for Visual Basic 6. When running BinScope, confirm it reports no instances of binaries built with Visual Basic 6.
  - Harden or disable XML entity resolution. XML parsing code can be vulnerable to exponential entity expansion attacks and external entity resolution attacks causing denials of service and disclosure of sensitive data. If XML entity resolution is not required by your application, then disable it. Verify that all XML parsing code (including use of XmlReader and XmlDocument) do one of the following:
  - Completely disable entity resolution.
  - Limit the size of internal entity resolution and disable external entity resolution if it is not possible to disable entity resolution.
  - Limit the size of internal entity resolution and limit the time and size of external entity resolution if it is not possible to disable external entity resolution.
  - Use safe integer arithmetic for memory allocation for new code. All new code that uses arithmetic to determine the amount of dynamic memory to allocate must be safe from any form of overflow, underflow, or truncation.
  - Use secure cookie over HTTPS. HTTP cookies created over HTTPS should not be visible to the same site over clear text via HTTP. Ensure that all cookies set over HTTPS use the "secure" attribute. Suggested tools include: Watcher (from Casaba Security).
  - AllowPartiallyTrustedCallersAttribute (APTCA) review. Ensure that the AllowPartiallyTrustedCallersAttribute (APTCA) enables an assembly to be called by untrusted code. APTCA behavior is different depending on the version of the framework, but the general effect is the same: potentially dangerous functionality is now exposed to partially trusted code, and the effects of this additional attack surface exposure have to be mitigated by security checks, strong enforcement mechanisms, and review. Ensure there is no code using APTCA or that your project exception review process has approved a request to use APTCA.
  - Mitigate against cross-site request forgery (CSRF). Cross-site request forgery is a type of attack in which a malicious website exploits the user’s browser to send commands to another website. This attack exploits the victim site’s trust in the user’s browser, generally by using the user’s cookies or session.
  - For ASP.NET or ASP.NET MVC projects, verify that all pages in the application report no AlwaysSetViewStateUserKeyTokenValue or MarkVerbHandlersWithValidateAntiforgeryToken FxCop rule violations.
  - For non ASP.NET projects, verify that:
  - A secondary token is submitted with each request. Ideally, the token must be unique per user, though session-unique tokens will suffice.
  - Validation tokens are not automatically submitted (such as via cookie). Including a hidden input value in a POST is the preferred method.
  - The token is not predictable. If the attacker can predict the token, it negates the protection.
  - Load DLLs securely. Applications and dynamic-link libraries (DLLs) must load DLLs securely to prevent DLL preloading vulnerabilities.
  - Minimum ATL Version and Secure COM Coding Requirements. Developers using the Active Template Library (ATL) to build COM controls must make sure they use the most secure ATL versions and use appropriate secure ATL coding constructs. Verify that the latest version of the ATL library is used and all ATL code is implemented with the correct secure coding constructs. This can be verified by passing the ATLVersionCheck and ATLVulnCheck tests with BinScope.
  - Reflection and authentication relay defense. This new recommendation is designed to help combat sophisticated toolkits that are available to implement reflection and relay attacks. It is hoped that it will aid developers in utilizing available defenses against reflection and authentication relay attacks. For network authentication, the following tasks should be followed:
  1. Specify the target system name as part of the authentication mechanism.
  2. Ensure channel integrity through signing and/or encrypting underlying transport messages using the negotiated session key, or implement Extended Protection for Authentication when signing or encryption is not supported.
  - Sample code should be SDL compliant. All sample code (code snippets, small sample applications, or complete sample applications) should meet the same SDL development practices security bar as if it were in a shipping product. That means all the appropriate tools must be run, and there is no use of banned functionality or compiler switches.
  - Internet Explorer 8 MIME handling: Sniffing OPT-OUT. This recommendation addresses functionality new in Internet Explorer 8 that may have security implications in some cases. It is recommended that for each HTTP response that could contain user controllable content, you utilize the HTTP Header X-Content-Type-Options:nosniff. The Watcher tool may be of use in meeting this requirement.
  - Safe redirect, online only. Automatically redirecting the user (through Response.Redirect, for example) to any arbitrary location specified in the request (such as a query string parameter) could open the user to phishing attacks. Therefore, it is recommended that you not allow HTTP redirects to arbitrary user-defined domains.
  - Comply with minimal Standard Annotation Language (SAL) code annotation recommendations as described in Appendix H: SDL Standard Annotation Language (SAL) Recommendations for Native Win32 Code. Annotating code helps existing code analysis tools identify implementation issues better and also helps improve the tools. SAL annotated code has additional code analysis requirements, as described in SDL SAL Recommendations.

## Phase Three: Implementation > Establish and Follow Best Practices for Development > Privacy Requirements

- [R-0062] (requirement) Establish and document development best practices for the development team. Communicate any design changes that affect privacy to your team’s privacy lead so that they can document and review any changes.

## Phase Three: Implementation > Establish and Follow Best Practices for Development > Security Recommendations

- [R-0063] (recommendation) Use HeapSetInformation. Use Windows heap corruption detection to help reduce the likelihood of successful exploitation of residual heap-based vulnerabilities.
- [R-0064] (recommendation) Review available information resources to adopt appropriate coding techniques and methodologies. For a current and complete list of all development best practice information and resources, see Writing Secure Code, Second Edition (ISBN 9780735617223; ISBN-10 0-7356-1722-8).
- [R-0065] (recommendation) Review recommended development tools and adopt appropriate tools.
- [R-0066] (recommendation) Define, document, and communicate to your entire team all best practices and policies based on analysis of all the resources and tools listed in this document.
- [R-0067] (recommendation) Document all tools that are used, including compiler versions, compile options (for example, /GS), and additional tools used. Also, forecast any anticipated changes in tools. For more information about minimum tool requirements and related policy, review How Are New Recommendations and New Requirements Added to the Security Development Life Cycle Process?
- [R-0068] (recommendation) Create a coding checklist that describes the minimal requirements for any checked-in code. This checklist can include some of the items from Writing Secure Code, Second Edition “Appendix D: A Developer’s Security Checklist” (p. 731), clean compile warning level requirements (/W3 as minimal and /W4 clean as ideal), or other desired minimum standards.
- [R-0069] (recommendation) Establish and document how the team enforces these practices. Is the team running scripts to check for compliance when code is checked in? How often do you run analysis tools? The development manager is ultimately responsible for establishing, documenting, and validating compliance of development best practices.
- [R-0070] (recommendation) For online services and/or LOB applications that use JavaScript, avoid use of the eval() function.
- [R-0071] (recommendation) Additional development best practices for security can be divided into three general categories:
  1. Review available information resources to adopt coding techniques and methodologies that are appropriate for the product.
  2. Review recommended development tools to adopt, and use those that are appropriate for the product, in addition to the tools required by the SDL.
  3. Define, communicate, and document all best practices and policies for the product. Based on analysis of all of the resources and tools listed above, product teams should adopt and communicate best practices, policies, and tools. This information should be documented and widely communicated to the entire product team to ensure best practices are adopted and followed.
  - Document all tools used. This includes all compiler versions, compile options (for example, /GS), and additional tools used for static code analysis. This should also forecast any changes in tools anticipated. As updated versions of tools (both compilers and code analysis tools) are made available, products that have not yet released a final beta will likely be required to adopt the newest version of the tools. Products that have released their final beta prior to the availability of updated tools are not required to adopt the latest versions of tools. Please review How Are New Recommendations and New Requirements Added to the Security Development Lifecycle Process? For more information on how policy is established on minimum tool requirements.
  - Use the Windows Imaging Component (WIC). WIC provides an extensible framework for reading and manipulating images, image files, and image metadata. It represents a standard interface. All software products that process digital image data must perform any encoding or decoding of image data solely and exclusively using the Windows Imaging Component (WIC) and therefore must remove any potential custom (image) codecs from the product codebase. For more information, see http://msdn.microsoft.com/en-us/library/ee719654.aspx.
  - Ensure that regular expressions must not execute in exponential time (O(2^n)). Regular expressions that are evaluated against untrusted input must be examined for unsafe patterns that can lead to denial-of-service (DoS) vulnerabilities. Use RegexFuzzer to analyze all regular expressions to ensure that they are free of grouping expressions with repetition that are themselves repeated and containing alternation where the alternate sub-expressions overlap each other.
  - Use proper http.sys URL canonicalization. Web servers often make security decisions based on a requested URL from a user. For example, a web server may deny access to certain files, such as configuration files, directly through the web server; rather, such files can only be viewed and manipulated with text editing tools, such as Visual Studio, against the local file system.
- [R-0072] (recommendation) The weakness with this approach is that the authorization check is based on the name of the resource, rather than based on an access control mechanism, such as an ACL, enforced by the operating system. And this leads to canonicalization (C14N) vulnerabilities, because there is often more than one way to name a resource. All web servers have suffered from such issues, but http.sys does not offer much protection from C14N vulnerabilities. It is therefore important that developers using http.sys follow these recommendations to defend themselves. Any application that uses http.sys should follow these guidelines.
- [R-0073] (recommendation) Managed Code
  1. Limit the URL length to no more than 16,384 characters (ASCII or Unicode). This is the absolute maximum URL length, based on the default IIS 6 setting. websites should strive for a length shorter than this, if possible.
  2. Use the standard .NET Framework file I/O classes (such as FileStream), since these take advantage of the canonicalization rules in the .NET FX.
  3. Explicitly build an allow-list of known filenames.
  4. Explicitly reject known filetypes you will not serve; UrlScan rejects: exe, bat, cmd, com, htw, ida, idq, htr, idc, shtm[l], stm, printer, ini, pol, dat files.
  5. Catch the following exceptions: System.ArgumentException (for device names), System.NotSupportedException (for data streams), System.IO.FileNotFoundException (for invalid escaped filenames), and System.IO.DirectoryNotFoundException (for invalid escaped dirs).
  6. Do not call out to Win32 file I/O APIs.
  7. On an invalid URL, gracefully return a 400 error to the user, and log the real error.
- [R-0074] (recommendation) Unmanaged Code
  1. Limit the URL length to 16,384 characters (ASCII or Unicode).
  2. Prepend \\?\ to the filename prior to accessing the file system, since this forces the file system to bypass filename equivalency checks. This is not perfect, because it does not prevent data streams (::$DATA, for example).
  3. Normalize the URL by URL double-decoding the filename, and check that the first decode matches the second decode. If not, it's an error.
  4. Look for known “bad characters” in the filename.
  5. Look for known “bad strings” in the filename.
  6. On an invalid URL or filename, return a 400, and log the real error.
- [R-0075] (recommendation) Use Standard Annotation Language (SAL). Annotate all functions that read from or write to a buffer passed as an argument to the function.
- [R-0076] (recommendation) Do not use the JavaScript eval() function (or equivalents). The JavaScript eval() function is used to interpret a string as executable code. While eval() enables a web application to dynamically generate and execute JavaScript (including JSON), it also opens up potential security holes, such as injection attacks, where an attacker-fed string may also get executed. For this reason, the eval() function or functional equivalents, such as setTimeout() and setInterval(), should not be used.
- [R-0077] (recommendation) Enforced automated banned API replacement. Add the following to an often-used header file, such as stdafx.h:
- [R-0078] (recommendation) #define _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES (1)
- [R-0079] (recommendation) This informs the compiler that you want to upgrade various C runtime functions to safer versions. For example, some calls to strcpy will upgrade to strcpy_s. For more information on banned APIs, visit http://blogs.msdn.com/sdl/archive/2008/10/22/good-hygiene-and-banned-apis.aspx.
- [R-0080] (recommendation) Encode long-lived pointers. Long-lived pointers (for example, globally scoped function pointers or pointers to shared memory regions) are subject to corruption through a buffer overrun attack that can lead to code execution attacks. This recommended defense raises the bar substantially on the attackers.
- [R-0081] (recommendation) Identify any long-lived pointers in your code. Access to these functions should be through encoded pointers using code like this:
- [R-0082] (recommendation) // g_pFoo is a global point that points to foo
- [R-0083] (recommendation) void g_pFoo = EncodePointer(&foo);
- [R-0084] (recommendation) // Now get the encoded pointer
- [R-0085] (recommendation) void *pFoo = DecodePointer(g_pFoo);
- [R-0086] (recommendation) The global pointer (g_pFoo) is encoded during the initialization phase, and its true value remains encoded until the pointer is needed. Each time g_pFoo is to be accessed, the code must call DecodePointer.
- [R-0087] (recommendation) Fix code flagged by /W4 compiler warnings. Attackers are finding and exploiting more obscure classes of vulnerabilities as traditional stack and heap buffer overruns become harder to find. To this end, it is recommended that all W4 warning messages are fixed prior to release.
- [R-0088] (recommendation) No global exception handlers. Exceptions are a powerful way to handle run-time errors, but they can also be abused in a way that could mask errors or make it easier for attackers to compromise systems.
- [R-0089] (recommendation) Restrict database permissions. Only grant "execute" permission on all stored procedures, and grant that permission only for the application domain group. For example:
  - Run your online service as "Network Service," for example, phx\$machinename
  - Join that domain account to a domain group, for example, phx\mywebappgroup
  - Ensure that the application database is set for execute permission only (and no other permissions) on its stored procedures and those permissions are associated with a domain group of which that application or server is a member. The principle of least privilege should be used and the group associated with the online service should not be granted access to any other object and no other user or group should be used within the online service for communication with the SQL server.
  - NULL out freed memory pointers in new code. This helps reduce the severity of double-free bugs and bugs that overwrite "dangling" pointers. For example:
- [R-0090] (recommendation) char *p = new char[N];
- [R-0091] (recommendation) ...
- [R-0092] (recommendation) delete [] p;
- [R-0093] (recommendation) Add this statement after the delete operator:
- [R-0094] (recommendation) p = NULL;
- [R-0095] (recommendation) The same process applies to any dynamic allocation and freeing pattern (for example, using malloc/free, GlobalAlloc/GlobalFree, or VirtuaAlloc/VirtualFree).
- [R-0096] (recommendation) Lock ActiveX controls to a defined set of domains. Identify any ActiveX controls, new and existing, that can be locked to a preselected set of domains, and incorporate the SiteLock 1.15 Template for ActiveX Controls during implementation to lock each control to that set of domains. Note that each control can have its own set of domains.
- [R-0097] (recommendation) ClickJacking defense. For each page that could contain user controllable content, you should use a "frame-breaker" script and include the HTTP response header named X-FRAME-OPTIONS in each authenticated page. The Watcher tool may be of use in meeting this recommendation. The exit criteria for this recommendation is as follows:
  1. A "frame-breaker" script is included in each authenticated page to prevent unintentionally framing.
  2. The X-FRAME-OPTIONS header has been added to all authenticated page HTTP responses that should not be framed (for example, DENY) or is utilized to only allow trusted sites to frame site content (for example, the current site with the use of SAMEORIGIN).
  - COM best practices. Check for HRESULT misuse and uninitialized [PROP]VARIANTs. All HRESULTs should be set to valid COM values, (such as S_OK, S_FALSE, or E_FAILED) and all VARIANTs are initialized correctly.
  - Restrict database permissions. Only grant Execute permission on all stored procedures, and grant that permission only for the application domain group. For example, run your online service as Network Service (for example, phx\$machinename) or join that domain account to a domain group (for example, phx\mywebappgroup).
- [R-0098] (recommendation) Make sure that this group is granted execute permissions only on your stored procedures. The principle of least privilege should be used and the group associated with the online service should not be granted access to any other object (and no other user or group should be used within the online service for communication with the SQL server).
- [R-0099] (recommendation) Use Transport Layer encryption securely. Properly use Transport Layer Security (TLS) when communicating with another entity, and verify that your service checks the Common Name attribute to be sure it matches the host with which you intended to communicate. Verify that your service consults a CRL for an updated list of revoked certificates at a frequent interval. If your service is accessible via a browser, verify that no security warnings appear at any visited URL for any supported browser.

## Phase Four: Verification > Security and Privacy Testing > Security Requirements

- [R-0100] (requirement) Where input to file parsing code could have crossed a trust boundary, file fuzzing must be performed on that code. All issues must be fixed as described in the Security Development Lifecycle (SDL) Bug Bar. Each file parser is required to be fuzzed using a recommended tool.
- [R-0101] (requirement) Win32/64/Mac: An Optimized set of templates must be used. Template optimization is based on the maximum amount of code coverage of the parser with the minimum number of templates. Optimized templates have been shown to double fuzzing effectiveness in studies. A minimum of 500,000 iterations, and have fuzzed at least 250,000 iterations since the last bug found/fixed that meets the SDL Bug Bar.
- [R-0102] (requirement) WinCE and Xbox: 100,000 bug free iterations, since the last bug found/fixed that meets the SDL Bug Bar. All file fuzzing bugs must be filed and triaged according to the SDL Bug Bar’s guidance.
- [R-0103] (requirement) If the program exposes remote procedure call (RPC) interfaces, you must use an RPC fuzzing tool to test for problems. You can find RPC fuzzers on the Internet. This requirement applies only to programs that expose RPC interfaces. All fuzz testing must be conducted using “retail” (not debug) builds and must correct all issues as described in the SDL Bug Bar.
- [R-0104] (requirement) If the project uses ActiveX controls, use an ActiveX fuzzer to test for problems. ActiveX controls pose a significant security risk and require fuzz testing. You can find ActiveX fuzzers on the Internet. Conduct all fuzz testing using “retail” (not debug) builds, and correct all issues as described in the SDL Privacy Bug Bar (Sample) and SDL Security Bug Bar (Sample) appendices.
- [R-0105] (requirement) Satisfy Win32 testing requirements as described in Appendix J: SDL Requirement: Application Verifier. The Application Verifier is easy to use and identifies issues that are MSRC patch class issues in unmanaged code. AppVerifier requires a modest resource investment and should be used throughout the testing cycle. AppVerifier is not optimized for managed code.
- [R-0106] (requirement) Define and document the security bug bar for the product. Verify that a security bug bar has been established and approved. Vulnerabilities include:
  - Elevation of privilege (the ability either to execute arbitrary code or to obtain more privilege than intended).
  - Denial of service.
  - Targeted information disclosure (where the attacker can locate and read information from anywhere on the system, including system information, that was not intended or designed to be exposed).
  - Spoofing.
  - Tampering (permanent modification of any user data or data used to make trust decisions in a common or default scenario that persists after restarting the operating system or application).
  - For online services and/or LOB applications, use approved cross-site scripting scanning test tools with the bug tracking system, and enter all vulnerabilities found into your bug tracking system. All vulnerabilities must be addressed prior to the Final Security Review.
  - For online services and/or LOB applications that implement web services, use an approved scanner to check for XML parsing problems.
  - Complete testing for kernel-mode drivers. The product team must complete the following testing for every kernel-mode driver:
- [R-0107] (requirement) Driver Verifier
  1. Using Windows Vista or Windows Server 2008, complete a full functional test on the driver with Driver Verifier enabled using /standard mode.
  2. Execute all code paths in the driver with Driver Verifier enabled using /standard mode.
- [R-0108] (requirement) Device Path Exerciser
  1. Run Device Path Exerciser specifically against each driver in the product (using the /dr parameter).
  2. Run Device Path Exerciser with Driver Verifier enabled.
- [R-0109] (requirement) To meet the exit criteria, every kernel-mode driver in the product must pass the Driver Verifier and Device Path Exerciser tests. Driver Verifier is available in the Windows Driver Kit, see Driver Development Tools -> Tools for Verifying Drivers -> Driver Verifier or, on MSDN, see http://msdn.microsoft.com/en-gb/library/ff545448.aspx. Device Path Exerciser is available in the Windows Driver Kit, see Driver Development Tools -> Tools for Testing Drivers -> Device Path Exerciser or, on MSDN, see http://msdn.microsoft.com/en-gb/library/ff544851.aspx.
- [R-0110] (requirement) COM object testing. Any product that ships a registered COM object must meet the following minimum criteria:
  1. COM objects must be compiled and tested with the SDL required switches enabled (for example, a COM object must be tested with NX and ASLR flags applied to the control and on a machine with NX and ASLR enabled).
  2. All methods in a COM object's supported interfaces must execute without access violations when called with valid data.
  3. COM objects must follow all published rules on reference counting. See the MSDN documentation on Addref and Release.
  4. COM objects must be tested for reliable query, instantiation, and interrogation by any COM container without returning an invalid pointer, leaking memory, or causing access violations.
  5. COM objects must follow the published rules for QueryInterface.
  - (Web applications only) If a site provides any authenticated access, then the crossdomain.xml or clientaccesspolicy.xml files for the site must only allow specifically enumerated authorized sites (that is, no wildcards). When using JavaScript, do not set document.domain to a shared top-level domain (for example, microsoft.com). Use a more specific domain instead. Exit criteria is as follows:
- [R-0111] (requirement) Read-Only Unauthenticated Sites and Services
- [R-0112] (requirement) Sites and web services that do not require authentication and provide read-only information have no action items for this requirement. However, keep in mind that policy files are site-wide, so a policy meant for an unauthenticated site will also apply to any other sites on the same server. If the application is a public service that could be used in mashups, other web services, or Flash or Silverlight® applications and thus requires a permissive crossdomain.xml or accesspolicy.xml file (one allowing * or a broad top-level domain, like msn.com or live.com), then interactive websites or authenticated APIs may not be hosted on the same domain.
- [R-0113] (requirement) Authenticated Websites
- [R-0114] (requirement) If an application is a standard web UI (not a service) that hosts web services for its own use, or has Flash and Silverlight components on the site, any crossdomain.xml or clientaccesspolicy.xml file in the root directory must allow access only to the sites that contain the appropriate Flash and Silverlight components or web services.
- [R-0115] (requirement) Authenticated Web Services
- [R-0116] (requirement) If a site has functions available only to authenticated users but also needs to be accessed by a Flash or Silverlight application, ensure that any Flash or Silverlight applications that the site uses load the policy file only from the root directory of the site, and ensure that the value of does not set domain="*". In addition, if such a site must be accessed by Silverlight applications, ensure a clientaccesspolicy.xml that allows only the desired sites is present, since Silverlight does not honor Flash crossdomain.xml files with policies other than "*". Authenticated sites with Flash and Silverlight front-ends must always use crossdomain.xml or clientaccesspolicy.xml to restrict access, since an open policy (domain="*") will allow any Internet site the user visits to take action as the user.
- [R-0117] (requirement) JavaScript
- [R-0118] (requirement) Scripts setting document.domain to any value should be validated to ensure that:
  1. The site checks that the caller is on a list of allowed sites before setting document.domain.
  2. If the site deals with PII in any way, document.domain is not set to a top-level domain (for example, live.com) but only to an appropriate subdomain (for example, billing.live.com).
  - Perform Application Verifier tests. Test all discrete applications within a shipping product for heap corruption and Win32 resource issues that might lead to security and reliability issues. You can detect these issues using AppVerifier, available at http://technet.microsoft.com/en-us/library/bb457063.aspx. Exit Criteria: All tests in the application's functional test suite have been run under AppVerifier, and all issues have been fixed.
  - Network fuzzing. Fuzzing of network interfaces is one of the primary tools of security researchers and attackers, and network facing applications are arguably the most easily accessed target for a remote attacker. Each network parser must successfully handle 100,000 malformed packets without error.
  - Binary analysis. If obfuscated binaries are being shipped, BinScope must be run on the pre-obfuscated version of each binary instead of the obfuscated version to ensure that issues were identified correctly.

## Phase Four: Verification > Security and Privacy Testing > Security Recommendations

- [R-0119] (recommendation) Create and complete security testing plans that address these issues:
  - Security features and functionality work as specified. Ensure that all security features and functionality that are designed to mitigate threats perform as expected.
  - Security features and functionality cannot be circumvented. If a mitigation can be bypassed, an attacker can try to exploit software weaknesses, rendering security features and functionality useless.
  - Ensure general software quality in areas that can result in security vulnerabilities. Validating all data input and parsing code against malformed or unexpected data is a common way attackers try to exploit software. Data fuzzing is a general testing technique that can help prevent such attacks.
  - Penetration testing. Use the threat models to determine priorities, test, and attack the software as a hacker might. Use existing tools or design new tools, if needed.
  - Hire third-party security firms as appropriate. Depending on the business goals for your project and availability of resources, consider engaging an external security firm for a security review or penetration testing.
  - Develop and use vulnerability regression tests. If the code has ever had a security vulnerability reported, it is strongly suggested that you add regression tests to the test suite for that component to ensure that similar vulnerabilities are not inadvertently re-introduced to the code. Similarly, if there are other products with similar functionality in the market that have suffered publicly reported vulnerabilities, add tests to the test plan to prevent similar vulnerabilities.
  - For online services and/or LOB applications, conduct data flow testing. Any externally accessible pages and interfaces must have tests. This should include pages that automatically redirect.
  - Run through your test cases with WinHTTP, the debug version of wininet, or another application that captures all page transitions. Make sure that no part of the flow can be bypassed.
  - If the feature exposes SOAP or DCOM interfaces or any other services, these must also be tested. Ensure that no step can be skipped or bypassed.
  - If your feature requires authenticating a user before providing access, ensure that it is not possible to bypass this authentication step by directly connecting to the backend.
  - For online services and/or LOB applications, conduct replay testing. Replay all messages for any scenario you are responsible for to ensure that the expected outcome occurs. For example, try and change the password and then repeat, or attempt to reuse security tokens in other contexts (for example, try using a login token in a password reset flow).
  - For online services and/or LOB applications, cover input validation testing scenarios and variants. Do not do this through a web browser, since it will honor server-specified field lengths. Test cases must cover the following scenarios:
  - Random inputs. Ensure that a full range of ASCII and Unicode characters are used. All verification should be “allow” based instead of “block” based (deny everything that is not explicitly allowed).
  - Large inputs. Large strings should be attempted.
  - Script injection.
  - SQL injection.
  - Path traversal. Try and pass filenames, like ../../../../../../../boot.ini, to bypass directory access controls.
  - Malformed XML blobs. Attempt to submit XML that does not match the target schema, if your feature uses XSL attempt to pass XSL processing instructions within your input. Note that this is best done either using valid, but slightly incorrect, XML data to bypass the .NET validation code or disabling .NET validation checks before testing. All final release code to be used in production environments must not disable XML and other validation code in .NET.
  - Secure Code Review. Security code reviews are a critical component of the Security Development Lifecycle. Given the opportunity to review old code or work on a new cool feature, developers lean towards the latter. Unsurprisingly, attackers don't target only new functionality; they will attack all code, regardless of its age. Waiting to make the code more secure in the next version of the product is not a good solution for protecting customers, and therefore, high-risk items (Critical) that are considered the most sensitive and important for security should be reviewed in depth at the earliest opportunity.
- [R-0120] (recommendation) Determine the most at-risk components (Critical) and perform an in-depth security review of the code making up those components. For critical components or if time allows, also review Important items. Use the following guidelines to determine the most at-risk components.
  1. Define the code review priority based on these criteria:
  - Critical code is considered to be the most sensitive from a security standpoint. The following are examples of Critical code, but please note this is not necessarily a definitive list. Critical code is all Internet- or network-facing code, code in the Trusted Computing Base (TCB)—such as kernel or SYSTEM code, code running as administrator or Local System, code running as an elevated user (also includes LocalService and NetworkService), or features with a prior history of vulnerability, regardless of version. Any code that handles secret data, such as encryption keys and passwords, is considered Critical code. For managed code, Critical code is considered to be any unverifiable code (any code that the standard PEVerify.exe tool reports as not verified). All code supporting functionality exposed on the maximum attack surface is considered Critical code by definition.
  - Important code is optionally installed code that runs with user privilege, or code that is installed by default that doesn't meet the Critical criteria.
  - Moderate code is rarely used code and setup code. Setup code that handles secret data, such as encryption keys and passwords, is always considered Critical code.
  - Any code or component with high rates of security bug discovery is considered to be Critical code, even if it otherwise maps to Important or Moderate per the previous definitions. While the definition of high rates is subjective within the team, it is important to examine the portions of code that have experienced the highest rates of security issues with extra scrutiny.
  - Don't forget to include and prioritize all sample code shipped with the product. While generalized guidelines are difficult, consider how customers will be using the samples. Samples that are expected to be compiled and used with little changes in production environments should be considered Critical. "Hello World" applications are more likely to be considered Moderate code.
  2. Identify development and testing owners for everything in products. The following are required to meet this security recommendation:
  - All Critical source code should be thoroughly reviewed by inspection teams and code-scanning tools.
  - All Important code should be reviewed using code-scanning tools and some human analysis.
  - Development owners for all source code and testing owners for all binaries have been identified, documented, and archived.
  - All source code is assessed and assigned a severity—Critical, Important, Moderate, or Low. This information is recorded in a document or spreadsheet and is archived.
- [R-0121] (recommendation) Use a passive security auditor. Use Watcher and Fiddler to detect vulnerabilities. Browse through every page in your web application (or run a prerecorded web macro that hits every page) with the Watcher plug-in for Fiddler enabled. If Watcher finds any potential vulnerabilities, you must fix them. Repeat this process until the run is completed with no flagged issues.

## Phase Four: Verification > Security and Privacy Testing > Privacy Recommendations

- [R-0122] (recommendation) For P1 and P2 projects, include privacy testing in your master test plan. Privacy testing of platform components deployed in organizations should include verification of organizational policy controls that affect privacy (these controls are listed in Appendix C: SDL Privacy Questionnaire). Privacy testing for features that transfer data over the Internet should include monitoring network traffic for unexpected network calls.

## Phase Four: Verification > Security Push > Security Requirements

- [R-0123] (requirement) Review and update threat models. Examine the threat models that were created during the Design phase. If circumstances prevented creation of threat models during Design phase, you must develop them in the earliest phase of the security push.
- [R-0124] (requirement) Review all bugs that affect security against the security bug bar. Ensure that all security bugs contain the security bug bar rating.

## Phase Four: Verification > Security Push > Privacy Requirements

- [R-0125] (requirement) Review and update the SDL Privacy Questionnaire form (Appendix C to this document) for any material privacy changes that were made during the implementation and verification stages. Material changes include:
  - Changing the style of consent.
  - Substantively changing the language of a notice.
  - Collecting different data types.
  - Exhibiting new behavior.

## Phase Four: Verification > Security Push > Security Recommendations

- [R-0126] (recommendation) Conduct security code reviews for at-risk components. Use the following information to help determine which components are most at risk, and use this determination to set priorities for security code review. High-risk items (Critical) must be reviewed earliest and most in depth. For a minimal checklist for security issues to be aware of during code reviews, see “Appendix D: A Developer’s Security Checklist” in Writing Secure Code, Second Edition (p. 731).
- [R-0127] (recommendation) Identify development and testing owners for everything in the program. Identify a development owner for each source code file. Identify a quality assurance owner for each binary file. Record this information in a document or spreadsheet and use a document/source tracking system to store it.
- [R-0128] (recommendation) Prioritize all code before you start the push. Track severity ratings in a document or spreadsheet that lists the development and quality assurance owners. Subject all code to the same criteria for prioritization, including legacy code. Many security vulnerabilities have come from legacy code that was created before the introduction of security pushes, threat modeling, and the other processes that are included in the Security Development Lifecycle.
- [R-0129] (recommendation) Ensure that you include and prioritize all sample code shipped with the product. Consider how users will use the samples. Samples that are expected to be compiled and used with small changes in production environments should be considered Critical.
- [R-0130] (recommendation) Re-evaluate the attack surface of the software. It is important to re-evaluate your team’s definition of attack surface during the security push. You should be able to calculate the attack surface based on information described in the design specifications for the software. Measurement of the attack surface enables you to understand which components have direct exposure to attack and the highest risk of damage if a security breach occurs. Focus effort on areas of highest risk areas, and take appropriate corrective actions. These actions might include:
  - Prolonging the push for especially error-prone components.
  - Deciding not to ship a component until it is corrected.
  - Disabling a component by default.
  - Re-designating a component for future removal from the software (deprecating it).
  - Modifying development practices to make vulnerabilities less likely to be introduced by future modifications or new developments.
- [R-0131] (recommendation) After you evaluate the attack surface, update attack surface documentation as appropriate.
- [R-0132] (recommendation) As time permits, consider code reviews for all components tagged with a severity level of Important.
- [R-0133] (recommendation) Review the security documentation plan. Examine how any changes to the product design during development have affected security documentation. Ensure that the security documentation plan meets all user needs.
- [R-0134] (recommendation) Focus the entire team on the push. When team members finish reviewing and testing their own components, they should help others in the group.
- [R-0135] (recommendation) Code severity definitions are provided in the following list:
  - Critical code is considered the most sensitive from a security standpoint. The following examples of Critical code are not necessarily a definitive list:
  - All Internet-facing or network-facing code.
  - Code in the Trusted Computing Base (TCB) (for example, kernel or SYSTEM code).
  - Code running as administrator or Local System.
  - Code running as an elevated user (including LocalService and NetworkService).
  - Features with a history of vulnerability, regardless of version.
  - Any code that handles secret data, such as encryption keys and passwords.
  - Any unverifiable managed code (any code that the standard PEVerify.exe tool reports as not verified).
  - All code supporting functionality exposed on the maximum attack surface.
  - Important code is optionally installed code that runs with user privilege or code that is installed by default that does not meet the Critical criteria.
  - Moderate code is rarely used code and setup code. (Setup code that handles secret data, such as encryption keys and passwords, is always considered Critical code.)
  - Any code or component that has experienced large numbers of security issues is considered Critical code, even if it would otherwise be considered Important or Moderate. Although the definition of large numbers is subjective, it is important to scrutinize carefully the portions of code that contain the most security vulnerabilities.

## Phase Five: Release > Public Release Privacy Review > Privacy Requirements

- [R-0136] (requirement) Review and update the Privacy Companion form.
- [R-0137] (requirement) For a P1 project, your privacy advisor reviews your final SDL Privacy Questionnaire (Appendix C to this document), helps determine whether a privacy disclosure statement is required, and gives final privacy approval for public release.
- [R-0138] (requirement) For a P2 project, you need validation by a privacy advisor if any of the following is true:
  - A design review is requested by a privacy advisor.
  - You want confirmation that the design is compliant with privacy standards.
  - You wish to request an exception.
  - For a P3 project, there are no additional privacy requirements.
  - Complete the privacy disclosure.
  - Draft a privacy disclosure statement as advised by the privacy advisor. If your privacy advisor indicates that a privacy disclosure is waived or covered, you do not need to meet this requirement.
  - Work with your privacy advisor and legal representatives to create an approved privacy disclosure.
  - Post the privacy disclosure to the appropriate website before each public release.

## Phase Five: Release > Public Release Privacy Review > Privacy Recommendations

- [R-0139] (recommendation) Create talking points as suggested by the privacy advisor to use after release to respond to any potential privacy issues.
- [R-0140] (recommendation) Review deployment guidance for enterprise programs to verify that privacy controls that affect functionality are documented. Conduct a legal review of the deployment guide.
- [R-0141] (recommendation) Create “quick text” for your support team that addresses likely user questions, and generally foster strong and frequent communication between your development and support teams.

## Phase Five: Release > Planning > Security Requirements

- [R-0142] (requirement) The project team must provide contact information for people who respond to security incidents. Typically, such responses are handled differently for products and services.
- [R-0143] (requirement) Provide information about which existing sustained engineering (SE) team has agreed to be responsible for security incident response for the project. If the product does not have an identified SE team, they must provide an emergency response plan (ERP) and provide it to the incident response team. This plan must include contact information for three to five engineering resources, three to five marketing resources, and one or two management resources who are the first points of contact when you need to mobilize your team for a response effort. Someone must be available 24 hours a day, seven days a week, and contacts must understand their roles and responsibilities and be able to execute on them when necessary.
- [R-0144] (requirement) Identify someone who is responsible for security servicing. All code developed outside the project team (third-party components) must be listed by filename, version, and source (where it came from).
- [R-0145] (requirement) You must have an effective security response process for servicing code that has been inherited or reused from other teams. If that code has a vulnerability, the releasing team may have to release a security update even though it did not develop the code.
- [R-0146] (requirement) You must also have an effective security response process for servicing code that has been licensed from third parties in either object or source form. For licensed code, you also need to consider contractual requirements regarding which party has rights and obligations to make modifications, associated service level agreements (SLAs), and redistribution rights for any security modifications.
- [R-0147] (requirement) Create a documented sustaining model that addresses the need to release immediate patches in response to security vulnerabilities and does not depend entirely on infrequent service packs.
- [R-0148] (requirement) Develop a consistent and comprehensible policy for security response for components that are released outside of the regular product release schedule (out-of-band) but that can be used to update or enhance the software after release. For example, Windows must plan a response to security vulnerabilities in a component, such as DirectX, that ships as part of the operating system but that might also be updated independently of the operating system, either directly by the user or by the installation of other products or components.
- [R-0149] (requirement) Disable tracing and debugging in ASP.NET applications prior to deployment. This neutralizes the following possible security vulnerabilities:
  - When tracing is enabled for the page, every browser requesting it also obtains the trace information that contains sensitive data about internal server state and workflow. This information could be security-sensitive.
  - When debugging is enabled for the page, errors happening on the server result in a full set of stack trace data presented to the browser. This data may expose security-sensitive information about the server’s workflow.

## Phase Five: Release > Planning > Privacy Requirements

- [R-0150] (requirement) For P1 and P2 projects, identify the person who is responsible for responding to all privacy incidents that may occur. Add this person’s e-mail address to the Incident Response section of the SDL Privacy Questionnaire (Appendix C to this document). If this person changes positions or leaves the team, identify a new contact and update all SDL Privacy Questionnaire forms for which that person was listed as the privacy incident response lead.
- [R-0151] (requirement) Identify additional development and quality assurance resources on the project team to work on privacy incident response issues. The privacy incident response lead is responsible for defining these resources in the Incident Response section of the SDL Privacy Questionnaire.
- [R-0152] (requirement) After release, if a privacy incident occurs, you must be prepared to follow the SDL Privacy Escalation Response Framework (Appendix K to this document), which might include risk assessment, detailed diagnosis, short-term and long-term action planning, and implementation of action plans. Your response might include creating a patch, replying to media inquiries, and reaching out to influential external contacts.

## Phase Five: Release > Final Security Review and Privacy Review > The FSR Process

- [R-0153] (process) Define a due date for all project information that is required to start the FSR. To minimize the likelihood of unexpected delays, plan to conduct an FSR four to six weeks before release to manufacturing (RTM) or release to web (RTW). Your team might need to revalidate specific decisions or change code to fix security issues. The team must understand that additional security work needs to be performed during the FSR.
- [R-0154] (process) The FSR cannot begin until you have completed the reviews of the security milestones that were required during development. Milestones include in-depth bug reviews, threat model reviews, and running all SDL-mandated tools.
- [R-0155] (process) Reconvene the development and security leadership teams to review and respond to the questions posed during the FSR process.
- [R-0156] (process) Review threat models. The security advisor should review the threat models to ensure that all known threats and vulnerabilities are identified and mitigated. Have complete and up-to-date threat models at the time of the review.
- [R-0157] (process) Review security issues that were deferred or rejected for the current release. The review should ensure that a consistent, minimum security standard was adhered to throughout the development cycle. Teams should already have reviewed all security issues against the criteria that were established for release. If the release does not have a defined security bug bar, your team can use the standard SDL Security Bug Bar.
- [R-0158] (process) Validate results of all security tools. You should have run these tools before the FSR, but a security advisor might recommend that you also run other tools. If tool results are inaccurate or unacceptable, you might need to rerun some tools.
- [R-0159] (process) Ensure that you have done all you can to remove vulnerabilities that meet your organization’s severity criteria so that there are no known vulnerabilities. Ultimately, the goal of SDL is to remove security vulnerabilities from products and services. No software release can pass an FSR with known vulnerabilities that would be considered as Critical, Important, Moderate, or Low.
- [R-0160] (process) Submit exception requests to a security advisor for review. If your team cannot meet a specific SDL requirement, you must request an exception. Typically, such a request is made well in advance of the FSR. A security advisor reviews these requests and, if the overall security risk is tolerable, might choose to grant the exception. If the security risk is not acceptable, the security advisor will deny the exception request. It is best to address all exception requests as soon as possible in the development phase of the project.

## Phase Five: Release > Final Security Review and Privacy Review > Possible FSR Outcomes

- [R-0161] (process) Possible outcomes of an FSR include:
  - Passed FSR. If all issues identified during the FSR are corrected before RTM/RTW, the security advisor should certify that the project has successfully met all SDL requirements.
  - Passed FSR (with exceptions). If all issues identified during the FSR are corrected before RTM/RTW or the security advisor and team can reach an acceptable compromise about any SDL requirements that the project team was unable to resolve, the security advisor should identify the exceptions and certify that all other aspects of the project have successfully met all SDL requirements.
  - All exceptions and security issues not addressed in the current release should be logged and then addressed and corrected in the next release.
  - FSR escalation. If a team does not meet all SDL requirements, and the security advisor and the product team cannot reach an acceptable compromise, the security advisor cannot approve the project, and the project cannot be released. Teams must correct whatever SDL requirements that they can or escalate to higher management for a decision.
  - Escalations occur when the security advisor determines that a team cannot meet the defined requirements or is in violation of an SDL requirement. Typically, the team has a business justification that prevents them from being compliant with the requirement. In such instances, the security advisor and the team should work together to compose a consolidated escalation report that outlines the issue—including a description of the security or privacy risk and the rationale behind the escalation. This information is typically provided to the business unit executive and the executive with corporate responsibility for security and privacy, to aid decision-making.
  - If a team fails to follow proper FSR procedures—either by an error of omission or by willful neglect—the result is an immediate FSR failure. Examples include:
  - Errors of omission, such as failure to properly document all required information.
  - Specious claims and willful neglect, including:
  - Claims of “Not subject to SDL” contrary to evidence.
  - Claims of “FSR pass” contrary to evidence, and software RTM/RTW without the appropriate signoff.
  - Such an incident can result in very serious consequences and, as such, should always and immediately be escalated to the project team executive staff and the executive in charge of security and privacy.

## Phase Five: Release > Final Security Review and Privacy Review > Security Requirements

- [R-0162] (requirement) The project team must provide all required information before the scheduled FSR start date. Failure to do so may delay completion of the FSR. If the schedule slips significantly before the FSR begins, contact the assigned security advisor to reschedule.
- [R-0163] (requirement) After the FSR is finished, the security advisor either signs off on the project as is or provides a list of required changes.
- [R-0164] (requirement) For online services and/or LOB applications, projects releasing services are required to have a security score of B or above to successfully pass the FSR. Both Operations and Product groups are responsible for compliance. A product’s security is managed at many levels. Vulnerabilities, whether in code or at host level, put the entire product (and possibly the environment) at risk.

## Phase Five: Release > Final Security Review and Privacy Review > Privacy Requirements

- [R-0165] (requirement) Repeat the privacy review for any open issues that were identified in the pre-release privacy review or for material changes made to the product after the pre-release privacy review. Material changes include modifying the style of consent, substantively revising the language of a notice, collecting different data types, or exhibiting new behavior. If no material changes were made, no additional reviews or approvals are required.
- [R-0166] (requirement) After the privacy review is finished, your privacy advisor either signs off on the product as is or provides a list of required changes.

## Phase Five: Release > Final Security Review and Privacy Review > Security Recommendations

- [R-0167] (recommendation) Ensure the product team is constantly evaluating the severity of security vulnerabilities against the standard that is used during the security push and FSR. Otherwise, a large number of security bugs might be reactivated during the FSR.

## Phase Five: Release > Release to Manufacturing/Release to Web > Security Requirements

- [R-0168] (requirement) To facilitate the debugging of security vulnerability reports and to help tools teams research cases in which automated tools failed to identify security vulnerabilities, all product teams must submit symbols for all publicly released products as part of the release process. This requirement is needed only for RTM/RTW binaries and any post-release binaries that are publicly released to users (such as service packs or updates, among others).
- [R-0169] (requirement) Design and implement a sign-off process to ensure security and other policy compliance before you ship. This process should include explicit acknowledgement that the product successfully passed the FSR and was approved for release.

## Phase Five: Release > Release to Manufacturing/Release to Web > Privacy Requirements

- [R-0170] (requirement) Design and implement a sign-off process to ensure privacy and other policy compliance before you ship. This process should include explicit acknowledgement that the product successfully passed the FSR and was approved for release.

## Post-SDL Requirement: Response > Security Servicing and Response Execution

- [R-0171] (requirement) After a software program is released, the product development team must be available to respond to any possible security vulnerabilities or privacy issues that warrant a response. In addition, develop a response plan that includes preparations for potential post-release issues.

## SDL-Agile Requirements

- [context] A workhorse of Agile development is the sprint, which is a short period of time (usually 15 to 60 days) within which a set of features or stories are designed, developed, tested, and then potentially delivered to customers. The list of features to add to a product is called the product backlog, and prior to a sprint commencing, a list of features is selected from the product backlog and added to the sprint backlog. The SDL fits this metaphor perfectly—SDL requirements are represented as tasks and added to the product and sprint backlogs. These tasks are then selected by team members to complete. You can think of the bite-sized SDL tasks added to the backlog as non-functional stories.

## SDL-Agile Requirements > Every-Sprint Requirements

- [R-0172] (requirement) In order to fit the weighty SDL requirements into the svelte Agile framework, SDL-Agile places each SDL requirement and recommendation into one of three categories defined by frequency of completion. The first category consists of the SDL requirements that are so essential to security that no software should ever be released without these requirements being met. This category is called the every-sprint category. Whether a team’s sprint is two weeks or two months long, every SDL requirement in the every-sprint category must be completed in each and every sprint, or the sprint is deemed incomplete, and the software cannot be released. This includes any release of the software to an external audience, whether this is a box product release to manufacturing (RTM), online service release to web (RTW), or alpha/beta preview release.
- [context] Some examples of every-sprint requirements include:
  - Run analysis tools daily or per build (see Tooling and Automation later in this Agile-SDL section).
  - Threat model all new features (see Threat Modeling: The Cornerstone of the SDL).
  - Ensure that each project member has completed at least one security training course in the past year (see Security Education).
  - Use filtering and escaping libraries around all web output.
  - Use only strong crypto in new code (AES, RSA, and SHA-256 or better).
- [context] For a complete list of the every-sprint requirements as followed by Microsoft SDL-Agile teams, see Appendix P.

## SDL-Agile Requirements > Bucket Requirements

- [R-0173] (requirement) The second category of SDL requirement consists of tasks that must be performed on a regular basis over the lifetime of the project but that are not so critical as to be mandated for each sprint. This category is called the bucket category and is subdivided into three separate buckets of related tasks. Currently there are three buckets in the bucket category—verification tasks (mostly fuzzers and other analysis tools), design review tasks, and planning tasks. Instead of completing all bucket requirements each sprint, product teams must complete only one SDL requirement from each bucket of related tasks during each sprint. The table below contains only a sampling of the tasks for each bucket. To see a complete list of all tasks for all three buckets, consult Appendix Q: SDL-Agile Bucket Requirements.
- [context] Table 1. Example of bucket categories. For a complete list of bucket items, see Appendix Q: SDL-Agile Bucket Requirements.
- [R-0174] (requirement) In this example, a team would be required to complete one verification requirement, one design review requirement, and one planning requirement in every sprint (in addition to the every-sprint requirements discussed earlier). For sprint one, the team might choose to complete ActiveX fuzzing, Review crypto design, and Update security bug bar from the table. For sprint two, they might choose Binary analysis, Conduct a privacy review, and Update network down plan.
- [context] It is left to the product teams to determine which tasks from each bucket that they would like to address in any given sprint. The SDL-Agile does not mandate any type of round-robin or other task prioritization for these requirements. If your team determines that they are best served by completing file fuzzing requirements every other sprint but that SOAP fuzzing only needs to be performed every 10 sprints, that’s acceptable.
- [context] However, no requirement can be completely ignored. Every requirement in the SDL has been shown to identify or prevent some form of security or privacy issue, or both. Therefore, no SDL bucket requirement can go more than six months without being completed.

## SDL-Agile Requirements > One-Time Requirements

- [context] There are some SDL requirements that need to be met when you first start a new project with SDL-Agile or when you first start using SDL-Agile with an existing project. These are generally once-per-project tasks that won’t need to be repeated after they’re complete. This is the final category of SDL-Agile requirements, called the one-time requirements.
- [R-0175] (recommendation) The one-time requirements should generally be easy and quick to complete, with the exception of creating a baseline threat model, which is discussed later in this section. Even though these tasks are short, there are enough of them that it would not be feasible for a team just starting with SDL-Agile to complete all of them in one sprint, given that the team also needs to complete the every-sprint requirements and one requirement from each of the buckets.
- [context] To address this issue, the SDL-Agile allows a grace period to complete each one-time requirement. The period generally ranges from one month to one year after the start of the project, depending on the size and complexity of the requirement. For example, choosing a security advisor is considered an easy, straightforward task and has a one-month completion deadline, whereas updating your project to use the latest version of the compiler is considered a potentially long, difficult task and has a one-year completion deadline. The current list of one-time requirements and the corresponding grace periods can be found in Appendix R of this document. Figure 2 provides an illustration of this process in action.
- [context] Figure 2. SDL-Agile process

## SDL-Agile Requirements > Constraints

- [R-0176] (requirement) The main difficulty that SDL-Agile attempts to address is that of fitting the entire SDL into a short release cycle. It is entirely reasonable to mandate that every SDL requirement be completed over the course of a two- or three-year-long release cycle. It is not reasonable to mandate the same for a two- or three-week-long release cycle. The categorization of SDL requirements into every-sprint, one-time, and the three bucket groups is the SDL-Agile solution for dealing with this conundrum. However, an effect of this categorization is that teams can temporarily skip some SDL requirements for some releases. The Microsoft SDL team believes this is a necessary situation required to provide the best mix of security, feature development, and speed of release for teams with short release cycles.
- [context] Although SDL-Agile was designed for teams with short release cycles, teams with longer release cycles are still eligible to use the SDL-Agile process. However, they may find that they are actually performing more security work than if they had used the classic, waterfall-based SDL. Requirements that a team only needs to complete once in classic SDL may need to be met five or six (or more) times in SDL-Agile over the course of a long project. However, this is not necessarily a bad thing and may help the team to create a more secure product.

## Applying SDL Tasks to Sprints > Exceptions

- [context] The SDL requirement exception workflow is somewhat different in SDL-Agile than in the classic SDL. Exceptions in SDL-Classic are granted for the life of the release, but this won’t work for Agile projects. A “release” of an Agile project may only last for a few days until the next sprint is complete, and it would be a waste of time for project managers to keep renewing exceptions every week.
- [R-0177] (requirement) To address this issue, project teams following SDL-Agile can choose to either apply for an exception for the duration of the sprint (which works well for longer sprints) or for a specific amount of time, not to exceed six months (which works well for shorter sprints). When reviewing the requirement exception, the security advisor can choose to increase or decrease the severity of the exception by one level (and thus increase or decrease the seniority of the manager required to approve the exception) based on the requested exception duration.
- [context] For example, say a team requests an exception for a requirement normally classified as Moderate, which requires manager approval. If they request the exception only for a very short period of time, say two weeks, the security advisor may drop the severity to Low, which requires only approval from the team’s security champion. On the other hand, if the team requests the full six months, the security advisor may increase the severity to Important and require signoff from senior management due to the increased risk.
- [R-0178] (requirement) In addition to applying for exceptions for specific requirements, teams can also request an exception for an entire bucket. Normally teams must complete at least one requirement from each of the bucket categories during each sprint, but if a team cannot complete even one requirement from a bucket, the team requests an exception to cover that entire bucket. The team can request an exception for the duration of the sprint or for a specific time period, not to exceed six months, just like for single exceptions. However, due to the broad nature of the exception—basically stating that the team is going to skip an entire category of requirements—bucket exceptions are classified as Important and require the approval of at least a senior manager.

## Applying SDL Tasks to Sprints > Final Security Review

- [R-0179] (requirement) A Final Security Review (FSR) similar to the FSR performed in the classic waterfall SDL is required at the end of every agile sprint. However, the SDL-Agile FSR is limited in scope—the security advisor only needs to review the following:
  - All every-sprint requirements have been completed, or exceptions for those requirements have been granted.
  - At least one requirement from each bucket requirement category has been completed (or an exception has been granted for that bucket).
  - No bucket requirement has gone more than six months without being completed (or an exception has been granted).
  - No one-time requirements have exceeded their grace period deadline (or exceptions have been granted).
  - No security bugs are open that fall above the designated severity threshold (that is, the security bug bar).
- [R-0180] (recommendation) Some of these tasks may require manual effort from the security advisor to ensure that they have been completed satisfactorily (for example, threat models should be reviewed), but in general, the SDL-Agile FSR is considerably more lightweight than the SDL-Classic FSR.
- [context] Now that the basic methodology and foundation is in place, it's time for an example scenario.

## Phase One: Requirements for LOB > Risk Assessment > Security Requirements

- [R-0181] (requirement) Application portfolio
- [R-0182] (requirement) Application teams enter application details in an application portfolio system that is used to track the life cycle of LOB applications within the enterprise.
- [R-0183] (requirement) The portfolio system can track information, such as contacts, dependencies, version history, deployment considerations, milestones, testing information and history, locations of relevant documents, and tasks and security controls used during the applications life cycle. Ideally, the portfolio would feature support, such as automated notification if the application is not in compliance with required (and, as appropriate—optional) controls. If you have a dedicated security team, the portfolio would also track the security SME assigned to perform an assessment, assessment history, artifacts, and, if appropriate, actual bugs.
- [R-0184] (requirement) Development teams must enter a new entry for the application if a new version of the application is being released so that it can follow this process cycle again.
- [R-0185] (requirement) Application risk assessment
- [R-0186] (requirement) Application risk level is determined based on a questionnaire filled out by the application team. This determines the SDL-LOB tasks the application owner must complete and is used to determine if the application is in scope for a security and privacy assessment. Please see Appendix U: SDL-LOB Risk Assessment Questionnaire for more details.
- [R-0187] (requirement) Note: The risk posed by an application may increase or decrease between successive releases and should be evaluated accordingly.

## Phase One: Requirements for LOB > Risk Assessment > Security Recommendations

- [R-0188] (recommendation) Visual Studio .NET Team System (or equivalent) can be used for bug tracking and management purposes.
- [R-0189] (recommendation) Dedicated security and privacy subject matter experts assist the application team during application development. These SMEs serve as resources for conducting all of the SDL-LOB tasks but, in particular, help perform specific tasks, such as a code reviews and penetration tests, among others.

## Phase Two: Design for LOB > Threat Modeling and Design Review > Security Requirements

- [R-0190] (requirement) Threat models should be completed for all applications, regardless of risk level.
- [R-0191] (requirement) Ensure that all threat models meet minimal threat model quality requirements. That is, all threat models must contain digital assets or data, business objectives, components, and role information. It must have application use cases, data flow, call flows, generated threats, and mitigations. Threat model reports generated are consumed by the development team as actionable items. A threat model that is not actionable (in terms of selecting countermeasures and prioritizing by risk) is an incomplete threat model.
- [R-0192] (requirement) All threat models and referenced mitigations should be reviewed and approved by the security SME. Ask architects, developers, testers, program managers, and others who understand the software to contribute to threat models and to review them. Solicit broad input and reviews to ensure the threat models are as comprehensive as possible.
- [R-0193] (requirement) Threat model data and associated documentation (functional/design specifications) have been stored within the application portfolio system described previously or by using the document control system used by product team for archiving purposes.

## Phase Two: Design for LOB > Threat Modeling and Design Review > Security Recommendations

- [R-0194] (recommendation) In addition to the specific security recommendation in the SDL for threat modeling, perform the following:
  - Security issues identified during the design review task should be logged under projects bug tracking system.

## Phase Three: Implementation for LOB > Internal Review > Security Requirements

- [R-0195] (requirement) Microsoft Anti-Cross-Site Scripting Library V4.2. Incorporate Anti-XSS library to protect ASP.NET web-based applications from XSS attacks. This library offers a more rigorous “white-list” approach than the native encoding methods found in .NET. Also featured is new support for globalization also not present in the .NET library.
- [R-0196] (requirement) CAT.NET. Run CAT.NET on managed code (C#, Visual Basic .NET, J#) applications. CAT.NET is a snap-in to the Visual Studio IDE that helps you identify exploitable code paths for security vulnerabilities, such as Cross-Site Scripting - SQL Injection - Process Command Injection - File Canonicalization - Exception Information - LDAP Injection - XPATH Injection - Redirection to User Controlled Site.
- [R-0197] (requirement) FxCop. FxCop is an application that analyzes managed code assemblies (code that targets the .NET Framework common language runtime) and reports information about the assemblies, such as possible design, localization, performance, and security improvements.
- [R-0198] (requirement) Microsoft Source Code Analyzer for SQL Injection. Run this static code analysis tool that helps identify SQL injection vulnerabilities in Active Server Pages (ASP) code.

## Phase Three: Implementation for LOB > Internal Review > Security Recommendations

- [R-0199] (recommendation) Security vulnerabilities identified during self-review and through code analysis tools should be logged under the project's bug tracking system.
- [R-0200] (recommendation) Resources
- [R-0201] (recommendation) Index of Security Checklists. While focused on .NET and web application development, much of the guidance here is technology agnostic.
- [R-0202] (recommendation) Perform a Security Code Review for Managed Code (Baseline Activity).
- [R-0203] (recommendation) Anti-XSS 4.2 Library.
- [R-0204] (recommendation) CAT.NET, a code analysis tool for .NET.
- [R-0205] (recommendation) Microsoft Source Code Analyzer for SQL Injection.

## Phase Four: Verification for LOB > Pre-Production Assessment > Security Requirements

- [R-0206] (requirement) The service level assigned to the application at the Risk Assessment phase governs the type of assessment an application receives in this phase. An application that has been assigned a medium or higher rating automatically requires a white-box code review, while applications assigned with a low rating will not.
- [R-0207] (requirement) Code review (white box)
  - Security team is provided access to an application’s source code and documentation to aid them in their assessment activities.
  - Complete review using both manual code inspection and security tools, such as static analysis or penetration testing.
  - Review threat model. Code reviews are prioritized based on risk ratings identified through threat modeling activities. Components of an application with the highest severity ratings get the highest priority with respect to assigning code review resources, whereas components with low severity ratings are assigned lesser priority.
  - Validate tools results. The security expert also validates results from code analysis tools (if applicable), such as CAT.NET to verify that vulnerabilities have been addressed by the development team. In situations where this is not the case, the issue is filed in the bug tracking system.
  - If source code is not available or the application is a third-party application, then black box assessment is conducted for that application.
  - Code review duration. The duration of a security review is determined by the security SME and is directly related to the amount of code that needs to be reviewed.
  - Code review can be conducted manually or by using automated tools to identity categories of vulnerabilities in the code. However, it should be noted that automated tools should supplement a code review and not replace them entirely, due to their limitations.
- [R-0208] (requirement) SQL injection. Ensure that the SQL queries are parameterized (preferably within a stored procedure) and that any input used in a SQL query is validated.
- [R-0209] (requirement) Cross-site scripting. Ensure that user controlled data is encoded properly before rendering to the browser. .NET applications can leverage Anti-XSS library for encoding data that is more rigorous than the native .NET encoding.
- [R-0210] (requirement) Cross-site request forgery. Ensure that the Page.ViewStateUserKey property is set to a unique value that prevents one-click attacks on your application from malicious users.
- [R-0211] (requirement) Data access. Look for improper storage of database connection strings and proper use of authentication to the database.
- [R-0212] (requirement) Input/data validation. Look for client-side validation that is not backed by server-side validation, poor validation techniques, and reliance on file names or other insecure mechanisms to make security decisions.
- [R-0213] (requirement) Authentication. Look for weak passwords, clear-text credentials, overly long sessions, and other common authentication problems.
- [R-0214] (requirement) Authorization. Look for failure to limit database access, inadequate separation of privileges, and other common authorization problems.
- [R-0215] (requirement) Sensitive data. Look for mismanagement of sensitive data by disclosing secrets in error messages, code, memory, files, or the network.
- [R-0216] (requirement) Auditing and logging. Ensure the application is generating logs for sensitive actions and has a process in place for auditing logs file periodically.
- [R-0217] (requirement) Unsafe code. Pay particularly close attention to any code compiled with the /unsafe switch. This code does not have all of the protection that normal managed code has. Look for potential buffer overflows, array out of bound errors, integer underflow and overflow, and data truncation errors.
- [R-0218] (requirement) Unmanaged code. In addition to the checks performed for unsafe code, also scan unmanaged code for the use of potentially dangerous APIs, such as strcpy and strcat. For a list of potentially dangerous APIs, see the section “Potentially Dangerous Unmanaged APIs,” in Security Question List: Managed Code (.NET Framework 2.0). Be sure to review any interop calls and the unmanaged code itself to make sure that bad assumptions are not made as execution control passes from managed to unmanaged code.
- [R-0219] (requirement) Hard-coded secrets. Look for hard-coded secrets in code by looking for variable names, such as "key," "password," "pwd," "secret," "hash," and "salt."
- [R-0220] (requirement) Poor error handling. Look for functions with missing error handlers or empty catch blocks.
- [R-0221] (requirement) Web.config. Examine your configuration management settings in the web.config file to make sure that forms authentication tickets are protected adequately, tracking and debugging is turned off, and that the correct algorithms are specified in the machineKey element.
- [R-0222] (requirement) Code access security. Search for the use of asserts, link demands, and allowPartiallyTrustedCallersAttribute (APTCA).
- [R-0223] (requirement) Code that uses cryptography. Check for failure to clear secrets and improper use of the cryptography APIs themselves.
- [R-0224] (requirement) Threading problems. Check for race conditions and deadlocks, especially in static methods and constructors.
- [R-0225] (requirement) Penetration test (black box)
  - This is a flip of a white-box code where the assessment is carried out without access to the application’s source code. This testing is intended to simulate an attacker’s perspective and uses a combination of tools and penetration techniques to find vulnerabilities in the system.
  - While this best simulates most malicious hacker scenarios, this approach typically yields the least bugs, both in terms of quality and quantity, but it is the best approach when source code is not available for review.
  - Depending upon available resources, this testing can be done internally by your security team or by engaging a third-party security firm as appropriate. Third-party security tools can also help with this requirement. Following are some of the high-level areas to consider in web penetration testing:
  - Use HTTP(s) interrogators, such as Fiddler, to capture traffic and to investigate cookies, headers, and hidden fields. Use Request/Response tampering methods to detect error disclosure, cross-site scripting, SQL injection, and other injection attacks. All user- controlled data, such as cookies, headers, form fields, and query strings should be tested by sending in malformed data.
  - Check for forceful browsing to verify authorization controls in applications where there are more than two user groups with different access levels.
  - Use Network Monitor to identify if sensitive data is being transferred from client to server and to verify if the channel is encrypted or not. This would be more useful in the case of thick client LOB applications.
  - Experiment with the high risk portions of the application to ensure that controls described in the code review discussion have been implemented correctly and consistently.
- [R-0226] (requirement) Deployment review of servers
  - Review the deployment of the production servers to ensure adequate hardening. This review focuses on minimizing the attack surface of the server (in terms of running services and applications installed), hardening the operating system (ACLs, accounts, patching, registry hardening, minimal open ports, installing server functionality, such as IIS websites on a non-system drive), and hardening functionality, such as IIS and SQL Server.
  - Review, if possible, actual production servers or standard images used to build those servers. Failing that, reviewing test servers with the expectation that the issues found are used as a road map by operations to harden the actual production servers.
  - The test server environment and the production server should have similar security measures while the team is developing the application. This ensures that the application is not modified to execute on the production server. The security team runs security checks on the server. The application security team can complete this either manually or by using a tool.
- [R-0227] (requirement) Privacy review
  - Review the privacy statements, notification, privacy controls, user categories, data management, and PII management for the application.
- [R-0228] (requirement) Host security deployment review
  - Installing server software (IIS, SQL Server) introduces new attack surfaces that must be hardened as well. Each server deployed, whether Intranet- or extranet-facing, needs to be hardened to both reduce attack surfaces and provide defense in depth. Recommended tools: Attack Surface Analyzer

## Phase Four: Verification for LOB > Pre-Production Assessment > Security Recommendations

- [R-0229] (recommendation) Assessment results yielding Critical or Important bugs automatically result in the application being blocked from deploying into production environments until the issues have been addressed or an exception has been granted by the business owner accepting the risk.
- [R-0230] (recommendation) The security bug bar for LOB applications has additional considerations than what is described earlier in this document. Your business needs to establish guidelines for evaluating the risk posed by individual vulnerabilities. This includes a risk rating framework that applies across all applications. The risk rating framework is independent of the risk assigned to the entire application. The sample table below presents a bug bar that accounts for the unique environment of an LOB application, including the risk posed by individual bugs.
- [R-0231] (recommendation) Severity: Critical | Description: Impact across the enterprise and not just the local LOB application/resources <br> Exploitable vulnerability in deployed production application
- [R-0232] (recommendation) Severity: Important | Description: Exploitable security issue <br> Policy or standards violation <br> Affects local application or resources only <br> Risk rating = High risk
- [R-0233] (recommendation) Severity: Moderate | Description: Difficult to exploit <br> Non-exploitable due to other mitigation <br> Risk rating = Medium risk
- [R-0234] (recommendation) Severity: Low | Description: Bad practice <br> Non-exploitable <br> Should not lead to exploit but helpful to attacker exploiting another vulnerability <br> Risk rating = minimal risk
- [R-0235] (recommendation) There is a trade-off in proving that a vulnerability is actually exploitable against time constraints in finding bugs. It may not be worthwhile to actually craft explicit exploit/malicious payload. In this case, you can adjust the severity as appropriate, erring on the side of caution.

## Phase Five: Release for LOB > Post-Production Assessment > Security Requirements

- [R-0236] (requirement) The actual list of servers deployed in production will likely vary dramatically from what was initially recorded in the application portfolio at the beginning of the SDL-LOB process. Post-production, operations may own both the servers and routine scanning of those servers for vulnerabilities, patch management, and similar activities. It is a best practice to segregate the duties between the server owners and the compliance organization. The compliance organization owns scanning in a timely manner, and the application team follows the processes established by the compliance team for moving into production.
- [R-0237] (requirement) Host-level security. Providing security for the host computer involves the following items that are audited on a regular basis on production servers:
  - Patch management. The security SME verifies that servers have the latest applicable security updates, including updates from every software manufacturer that has software running on the server.
  - Appropriate configuration. The servers are reviewed for compliance with established baselines. For example, all unused services that are not required for the application are disabled and blocked instead of running with default settings.
  - Antivirus. Servers have antivirus software running and actively scanning all system file areas, in addition to all shared directories. All systems must have their antivirus application or signature files examined at logon to ensure that the latest antivirus application or current virus signature files are present.
  - Compliance. Verify compliance with internal business policies and external legal requirements, in addition to standards such as PCI.
  - Review access control/permissions. The access control list (ACL) permission settings on all file shares and other system, database, and COM+ objects are reviewed to help prevent unauthorized access. Regular review, for example, of administrator privileges on a given server should be performed.
  - Server auditing and logging. Ensuring that auditing with appropriate logging procedures for all system objects that contain business-sensitive information is enabled. Logging procedures include collecting log files and protecting access to log data to only appropriate users (members of security, internal audit, or systems management teams) with the appropriate ACLs. Even more critical is ensuring that the logs are reviewed on a regular basis and that there is some guidance for filtering critical logs from regular operational "noise."
  - Network level security. The network infrastructure should be scanned for compliance with baselines (just like servers). This evaluates configuration, vulnerabilities, patch management, and other similar concerns.
  - Application retirement. At some point the application will need to be retired gracefully. Are there adequate controls, contact information, and operational awareness to ensure that this can happen at the appropriate time?

## Phase Five: Release for LOB > Post-Production Assessment > Security Recommendations

- [R-0238] (recommendation) Vulnerabilities identified in production should be remediated per operational processes defined by the compliance team.
- [R-0239] (recommendation) Frequently, application teams have a variety of post-production changes to the application, ranging from a hotfix, service pack, or entirely new features. Depending on the scope, the application team either needs to start over by updating the application portfolio (which kicks off a new iteration of the SDL-LOB life cycle), or perform a subset of the SDL-LOB tasks. At a minimum, this subset should include a review/update of the threat model and selected tasks from the Internal Review conducting during the Implementation phase.

## Appendix D: Firewall Rules and Requirements > Firewall Rules and Requirements

- [R-0240] (requirement) : Port-specific rules <br> (permitted only when one or more of the following conditions are TRUE) | Conditions: Customer and User Behavior | Requirements: Empirical data is provided that shows that at least 80% of your users are or will be using a feature that requires the port within the next year.
- [R-0241] (requirement) Conditions: Informed Consent <br> The user has provided explicit informed consent (the user must be prompted for and grant informed consent for the port to be open). | Requirements: Data showing that 80% of customers will answer “Yes” to a dialog asking them whether they want to open the port.
- [R-0242] (requirement) : Program-specific rules <br> (permitted only when all of the following conditions are true) | Conditions: The program does not run as a service. <br> The program listens on the network only when the user is using the functionality that listens. This includes programs that start when the user logs in. <br> The program can be prevented from starting automatically through a GUI.
- [R-0243] (requirement) : Inbound firewall rules | Requirements: Applications must create rules during setup for traffic that is expected in more than 80% of installations of the application. Explicit user consent is required to enable the rules. <br> Rules must be scoped to all these parameters—Program, Port, and Profile(s). <br> For features that implement services, rules must also be scoped to that service. <br> Services must implement Windows Service Hardening firewall rules.

## Appendix E: Required and Recommended Compilers, Tools, and Options for All Platforms > Win32 Requirements: Unmanaged Code

- [R-0244] (requirement) Compiler/Tool: C/C++ Compiler | Minimum Required Version and Switches/Options: Microsoft Visual Studio .NET 2008
- [R-0245] (requirement) Compiler/Tool: cl.exe | Minimum Required Version and Switches/Options: Version 14.00.50727.42 <br> Use /GS | Optimal/Recommended Version  and Switches/Options: Use /GS
- [R-0246] (requirement) Compiler/Tool: Link.exe | Minimum Required Version and Switches/Options: Version 8.00.50727.762 <br> Use /SAFESEH <br> Use /NXCOMPAT and don’t use /NXCOMPAT:NO. <br> See Appendix F: SDL Requirement: No Executable Pages for more information. | Optimal/Recommended Version  and Switches/Options: Use /SAFESEH <br> Use /functionpadmin:5 <br> Use /DYNAMICBASE | Comments: Visual Studio 2008 SP1 is needed for /DYNAMICBASE
- [R-0247] (requirement) Compiler/Tool: MIDL.exe | Minimum Required Version and Switches/Options: Version 6.00.0366 <br> Use /robust | Optimal/Recommended Version  and Switches/Options: Use /robust
- [R-0248] (requirement) Compiler/Tool: Source code analysis | Minimum Required Version and Switches/Options: Visual Studio 2008 Code Analysis Options (“/analyze”) <br> For Visual Studio 2008 code analysis, all warning IDs from the following list must be fixed: 4532 6029 6053 6057 6059 6063 6067 6200 6201 6202 6203 6204 6248 6259 6260 6268 6276 6277 6281 6282 6287 6288 6289 6290 6291 6296 6298 6299 6305 6306 6308 6334 6383 | Optimal/Recommended Version  and Switches/Options: Visual Studio 2008 Code Analysis Options (“/analyze”). <br> For Visual Studio 2008 code analysis, all warning IDs from the following list must be fixed: 4532 6029 6053 6057 6059 6063 6067 6200 6201 6202 6203 6204 6248 6259 6260 6268 6276 6277 6281 6282 6287 6288 6289 6290 6291 6296 6298 6299 6305 6306 6308 6334 6383 <br> Standard Annotation Language (SAL): Code annotated with SAL should correct additional warnings, in addition to those listed above. See Appendix H: SDL Standard Annotation Language (SAL) Recommendations for Native Win32 Code for more information. The warnings are summarized as follows: <br> SAL Compliance <br> Visual Studio 2008: 26020–26023 <br> /analyze <br> Visual Studio 2008: 6029 6053 6057 6059 6063 6067 6201–6202 6248 6260 6276 6277 6305 | Comments: Visual Studio 2008 Team Edition contains a publicly available version that is branded as “C/C++ Code Analysis.”
- [R-0249] (requirement) Compiler/Tool: Protecting Against Heap Corruption | Minimum Required Version and Switches/Options: n/a | Optimal/Recommended Version  and Switches/Options: All executable programs written using unmanaged code (.EXE) must call the HeapSetInformation interface. See Appendix I: SDL Requirement: Heap Manager Fail Fast Setting for more information.
- [R-0250] (requirement) Compiler/Tool: C4700 and C4701 Compiler Warnings | Minimum Required Version and Switches/Options: n/a | Optimal/Recommended Version  and Switches/Options: Compile code with C4700 and C4701 compiler warnings enabled and fix all instances of these warnings.

## Appendix E: Required and Recommended Compilers, Tools, and Options for All Platforms > Win32 Requirements: Managed Code

- [R-0251] (requirement) Compiler/Tool: C# Compiler | Minimum Required Version  and Switches/Options: Visual Studio 2008 | Comments: If using C#, use C# v2.0 or later; if using Visual Basic.NET use Visual Basic.NET 8.0 or later
- [R-0252] (requirement) Compiler/Tool: csc.exe | Minimum Required Version  and Switches/Options: Version 8.0.50727.42
- [R-0253] (requirement) Compiler/Tool: .NET Framework | Minimum Required Version  and Switches/Options: Version 2.0.50727
- [R-0254] (requirement) Compiler/Tool: FxCop | Minimum Required Version  and Switches/Options: Version 1.32 | Optimal/Recommended Version  and Switches/Options: Most recent version

## Appendix E: Required and Recommended Compilers, Tools, and Options for All Platforms > Win32 Requirements: Testing Tools

- [R-0255] (requirement) Tool: AppVerifier | Minimum Required Version and Switches/Options: Most recent version <br> Run tests as described in Appendix J: SDL Requirement: Application Verifier. | Optimal/Recommended Version  and Switches/Options: Most recent version | Comments: Note: AppVerifier is targeted at unmanaged code and is not optimized for managed code.

## Appendix E: Required and Recommended Compilers, Tools, and Options for All Platforms > Win64 Requirements (IA64 and AMD64): Unmanaged Code

- [R-0256] (requirement) Compiler/Tool: C/C++ Compiler | Minimum Required Version  and Switches/Options: Visual Studio 2008
- [R-0257] (requirement) Compiler/Tool: cl.exe | Minimum Required Version  and Switches/Options: Version 14.00.50727.42
- [R-0258] (requirement) Compiler/Tool: Link.exe | Minimum Required Version  and Switches/Options: Version 8.00.50727.762 <br> Use of /SAFESEH does not apply to Win64 platforms. <br> Use /NXCOMPAT and do not use /NXCOMPAT:NO. See Appendix F: SDL Requirement: No Executable Pages for more information. | Optimal/Recommended Version  and Switches/Options: AMD64 only: Use /functionpadmin:6 <br> Use of /SAFESEH does not apply to Win64 platforms. <br> Use /DYNAMICBASE | Comments: Visual Studio 2008 SP1 is needed for /DYNAMICBASE.
- [R-0259] (requirement) Compiler/Tool: MIDL.exe | Minimum Required Version  and Switches/Options: Version 6.00.0366 <br> Use /robust | Optimal/Recommended Version  and Switches/Options: Use /robust
- [R-0260] (requirement) Compiler/Tool: Protecting Against Heap Corruption | Minimum Required Version  and Switches/Options: n/a | Optimal/Recommended Version  and Switches/Options: All executable programs written using unmanaged code (.EXE) must call the HeapSetInformation interface. See Appendix I: SDL Requirement: Heap Manager Fail Fast Setting for more information.
- [R-0261] (requirement) Compiler/Tool: C4700 and C4701 Compiler Warnings | Minimum Required Version  and Switches/Options: n/a | Optimal/Recommended Version  and Switches/Options: Compile code with C4700 and C4701 compiler warnings enabled and fix all instances of these warnings.

## Appendix E: Required and Recommended Compilers, Tools, and Options for All Platforms > Win64 Requirements (IA64 and AMD64): Managed Code

- [R-0262] (requirement) Compiler/Tool: C# Compiler | Minimum Required Version  and Switches/Options: Visual Studio 2008 | Comments: If using C#, use C# v2.0 or later; if using Visual Basic.NET use Visual Basic.NET 8.0 or later
- [R-0263] (requirement) Compiler/Tool: csc.exe | Minimum Required Version  and Switches/Options: Version 8.0.50727.42
- [R-0264] (requirement) Compiler/Tool: .NET Framework | Minimum Required Version  and Switches/Options: Version 2.0.50727
- [R-0265] (requirement) Compiler/Tool: FxCop | Minimum Required Version  and Switches/Options: Most recent version | Optimal/Recommended Version  and Switches/Options: Most recent version

## Appendix E: Required and Recommended Compilers, Tools, and Options for All Platforms > Win64 Requirements (IA64 and AMD64): Testing Tools

- [R-0266] (requirement) Tool: AppVerifier | Minimum Required Version and Switches/Options: Most recent version <br> Run tests as described in Appendix J: SDL Requirement: Application Verifier. | Optimal/Recommended Version  and Switches/Options: Most recent version | Comments: Note: AppVerifier is targeted at unmanaged code and is not optimized for managed code.

## Appendix E: Required and Recommended Compilers, Tools, and Options for All Platforms > Windows CE Requirements: Unmanaged Code

- [R-0267] (requirement) Compiler/Tool: C/C++ Compiler | Minimum Required Version and Switches/Options: Visual Studio 2008
- [R-0268] (requirement) Compiler/Tool: cl.exe | Minimum Required Version and Switches/Options: Version 14.0.50725.0 <br> Use –GS (see comments) | Optimal/Recommended Version  and Switches/Options: Use –GS (see comments) | Comments: The –GS flag has a modest impact on code size, which can be of interest on WinCE platforms. Minimally, –GS must be used on all Internet-facing code. Ideally,  –GS should be used on all code.
- [R-0269] (requirement) Compiler/Tool: Link.exe | Minimum Required Version and Switches/Options: Version 8.00.50727.762 <br> Use of /SAFESEH only applies to x86 on WinCE platforms. <br> Use of /NXCOMPAT does not apply to WinCE. | Optimal/Recommended Version  and Switches/Options: Use of /SAFESEH only applies to x86 on WinCE platforms. <br> Use of /NXCOMPAT:NO does not apply to WinCE.
- [R-0270] (requirement) Compiler/Tool: MIDL.exe | Minimum Required Version and Switches/Options: Version 6.00.0366 <br> Use /robust | Optimal/Recommended Version  and Switches/Options: Use /robust
- [R-0271] (requirement) Compiler/Tool: Source code analysis | Minimum Required Version and Switches/Options: Visual Studio 2008 Code Analysis Options (“/analyze) <br> For Visual Studio 2008 code analysis, all warning IDs from the following list must be fixed: 4532 6029 6053 6057 6059 6063 6067 6200 6201 6202 6203 6204 6248 6259 6260 6268 6276 6277 6281 6282 6287 6288 6289 6290 6291 6296 6298 6299 6305 6306 6308 6334 6383

## Appendix E: Required and Recommended Compilers, Tools, and Options for All Platforms > Windows CE Requirements: Compact Framework Managed Code

- [R-0272] (requirement) Compiler/Tool: C# Compiler | Minimum Required Version and Switches/Options: Visual Studio 2008 | Comments: If using C#, use C# v2.0 or later; if using Visual Basic.NET use Visual Basic.NET 8.0 or later
- [R-0273] (requirement) Compiler/Tool: csc.exe | Minimum Required Version and Switches/Options: Version 8.0.50727.42
- [R-0274] (requirement) Compiler/Tool: .NET Framework | Minimum Required Version and Switches/Options: Version 2.0.50727
- [R-0275] (requirement) Compiler/Tool: FxCop | Minimum Required Version and Switches/Options: Most recent version | Optimal/Recommended Version  and Switches/Options: Most recent version

## Appendix F: SDL Requirement: No Executable Pages

- [R-0276] (requirement) Executing code from data code pages is a very common attack vector. The use of this technique is needed only in very limited scenarios. As a result, all programs and services should avoid this technique unless explicitly required. Having even one page marked EXECUTABLE in a process (other than dynamic-link libraries or DLLs) usually renders other security measures (such as /GS and /SafeSEH) useless for that process.

## Appendix F: SDL Requirement: No Executable Pages > Goals and Justification

- [context] The Windows Exception Handling mechanism assumes that it is safe to dispatch exceptions to any address if they are not in a DLL but are still EXECUTABLE.
- [context] Given a stack buffer overflow, an attacker can overflow the nearest exception record on the stack (there is always at least one) and point it to an address in the page marked EXECUTABLE.
- [context] Because of the number of stack locations controlled by the overflow at the point the exception handler takes over, many possible op-code sequences would reliably deliver execution back to the attack-supplied buffer. One such sequence is {pop, pop, ret} (possibly interleaved with other instructions). It is also possible to leverage a sequence of op-codes that would produce an arbitrary memory-overwrite in a two-stage attack.
- [context] Because of the number of possibilities, it is very hard to prove that bytes on a page marked EXECUTABLE cannot be abused sufficiently to take control.

## Appendix F: SDL Requirement: No Executable Pages > Scope

- [context] The following subsections specify the scope of the No Executable Pages requirement proposal.

## Appendix F: SDL Requirement: No Executable Pages > Operating Systems

- [context] This requirement applies to Win32 and Win64 operating systems but not to Windows CE or Macintosh.

## Appendix F: SDL Requirement: No Executable Pages > Products/Services

- [context] This requirement applies to code that runs on users’ computers (products) and to code that runs only on Microsoft-owned computers and accessed by users (for example, Microsoft-owned and provisioned online services).

## Appendix F: SDL Requirement: No Executable Pages > Technologies

- [context] This requirement applies to unmanaged (native) code, such as C and C++.

## Appendix F: SDL Requirement: No Executable Pages > New Code and Legacy Code

- [context] This requirement applies to both new code and legacy code.

## Appendix F: SDL Requirement: No Executable Pages > Exceptions

- [context] Sometimes it simply might not be possible to mark all pages as non-executable. Examples include digital rights management technologies and just-in-time (JIT) technologies that dynamically create code. For such cases, the following techniques can help make the pages safe:
  - If your code uses VirtualAllocXXX APIs to allocate EXECUTABLE pages, load a dummy DLL and use one of its sections instead.
  - Register a Vectored Exception Handler in the process, and vet the chain of exception handlers to make sure none of them point to your EXECUTABLE pages.
  - Randomize the address of the EXECUTABLE pages and/or randomize the starting offset of content within those pages.

## Appendix F: SDL Requirement: No Executable Pages > Special Cases

- [context] Because marking a binary as “DEP compatible” (with /NXCOMPAT) changes how the operating system interacts with the executable, it is important to test all executables (.EXE) marked as /NXCOMPAT with a version of Windows that supports this functionality:
  - Client software: Windows XP SP2, Windows Vista
  - Server software: Windows Server 2003 Service Pack 1 (SP1) or Windows Server 2008
- [context] (Review the detailed description of the Data Execution Prevention [DEP] feature for specific details about how to use DEP on Windows Server 2003 SP1.)
- [context] All executables (.EXE) marked as /NXCOMPAT are able to take advantage of Data Execution Protection. Dynamic-link libraries (.DLL files) or other code called by executables (such as COM objects) do not gain direct security benefits with /NXCOMPAT but need to coordinate enabling /DEP support with any executable files that might call them. Any EXE with /NXCOMPAT enabled that loads other code without /NXCOMPAT enabled may have the process fail unexpectedly unless the EXE and all of the other code that it calls (such as DLLs or COM objects) have been thoroughly tested with DEP enabled (linked with /NXCOMPAT option).

## Appendix F: SDL Requirement: No Executable Pages > Requirements > Requirement: Do Not Use Certain VirtualAllocXXX Flags

- [R-0277] (requirement) If your code calls any of these APIs:
  - VirtualAlloc
  - VirtualAllocEx
  - VirtualProtect
  - VirtualProtectEx
  - NtAllocateVirtualMemory
  - NtProtectVirtualMemory
- [R-0278] (requirement) Do not use any of these flags:
  - PAGE_EXECUTE
  - PAGE_EXECUTE_READ
  - PAGE_EXECUTE_READWRITE
  - PAGE_EXECUTE_WRITECOPY

## Appendix F: SDL Requirement: No Executable Pages > Requirements > Requirement: Use /NXCOMPAT Linker Option

- [R-0279] (requirement) All binaries must link with /NXCOMPAT flag (and not link with /NXCOMPAT:NO) using the linker included with Visual Studio 2005 and later.

## Appendix F: SDL Requirement: No Executable Pages > Compliance Measurement > Requirement: Do Not Use Certain VirtualAllocXXX Flags

- [R-0280] (requirement) While no solutions exist to monitor the use of these APIs, project teams will be asked to examine project specifications for the use of these APIs and attest to their removal.

## Appendix F: SDL Requirement: No Executable Pages > Compliance Measurement > Requirement: Measurement by Product/Service Team

- [R-0281] (requirement) Project teams will be asked to attest to the use of this linker option.

## Appendix F: SDL Requirement: No Executable Pages > Compliance Measurement > Requirement: Measurement by Security Advisors

- [R-0282] (requirement) This requirement is required to complete the final security review, and use of this linker option should be confirmed before allowing the software to be released to manufacturing or the web (RTM/RTW).

## Appendix F: SDL Requirement: No Executable Pages > Support Considerations > Requirement: Impact on Existing SDL Requirements

- [R-0283] (requirement) This requirement currently has some overlap with the Banned API requirement in that it describes some function calls that are prohibited. With the release of Windows Vista, this requirement is an even more important part of the Microsoft defense-in-depth strategy (in conjunction with Address Space Layout Randomization [ASLR] support in Windows Vista).

## Appendix F: SDL Requirement: No Executable Pages > Support Considerations > Requirement: Education and Training

- [R-0284] (requirement) Education reference materials currently available include:
  - Data Execution Prevention
  - Detailed Description of the Data Execution Prevention (DEP) Feature

## Appendix G: SDL Requirement: No Shared Sections

- [R-0285] (requirement) Binaries that are shipped as part of the product must not contain sections marked as shared, which are a security threat and should not be used. Use properly secured, dynamically created shared memory objects instead.

## Appendix G: SDL Requirement: No Shared Sections > Rationale

- [context] The Portable Executable (PE) format allows binaries to define sections—named areas of code or data—that have distinct properties, such as size, virtual address, and flags, which define the behavior of the operating system as it maps the sections into memory when the binary image is loaded. An example of a section would be text, which is typically present in all executable images. This section is used to store the executing code and is marked as Code, Execute, Read, which means code can execute from it, but data cannot be written to it. It is possible to define custom sections with desired names and properties by using compiler/linker directives.
- [context] One such section flag is Shared. When it is used and the binary is loaded into multiple processes, the shared section maps to the same physical memory address range. This functionality makes it possible for multiple processes to write to and read from addresses that belong to the shared section.
- [context] Unfortunately, it is not possible to secure a shared section. Any malicious application that runs in the same session can load the binary with a shared section and eavesdrop or inject data into shared memory (depending on whether the section is read-only or read-write).
- [context] To avoid security vulnerabilities, use the CreateFileMapping function with proper security attributes to create shared memory objects.

## Appendix G: SDL Requirement: No Shared Sections > Detecting Existing Shared PE Sections

- [context] You can use the following linker directive to create a shared section:
- [context] /section:<name>, RWS
- [context] The following directives in C/C++ source code can be used:
- [context] // (this introduces a new PE section)
  #pragma data_seg(".shared")
- [context] int mySharedData = 1;
  #pragma data_seg()
- [context] Or:
  #pragma section(".shrd2", read, write, shared)
- [context] __declspec(allocate(".shrd2")) int mySharedData2 = 2;

## Appendix H: SDL SAL Recommendations for Native Win32 Code

- [context] The Standard Source Code Annotation Language (SAL), a technology from Microsoft Research that is actively embraced by the Windows and Office teams, is a powerful addition to C/C++ source code to help find bugs, especially security vulnerabilities. SAL can help find more vulnerabilities than the present set of static analysis tools can find. A major benefit of SAL is that developers need only annotate their headers to provide benefit for others. For example, most C runtime and Windows headers that ship with Visual Studio 2005 and later are annotated. Windows Development Kit headers are also annotated.
- [R-0286] (recommendation) All products developed using SDL should use a subset of SAL to help find deeper issues, such as buffer overrun issues. Microsoft teams, such as Office and Windows, are using SAL beyond the requirements of SDL.

## Appendix H: SDL SAL Recommendations for Native Win32 Code > SAL Details

- [context] SAL is primarily used as a method to help tools, such as the Visual C++ /analyze compiler option, to find vulnerabilities by knowing more about a function interface. For the purposes of this appendix, SAL can document three properties of a function:
  - Whether a pointer can be NULL
  - How much space can be written to a buffer
  - How much can be read from a buffer (potentially including NULL termination)
- [context] At a high level, things become more complicated because there are two implementations of SAL:
  - __declspec syntax (Visual Studio 2005 and Visual Studio 2008)
  - Attribute syntax (Visual Studio 2008)
- [R-0287] (recommendation) Each of these implementations maps onto lower-level primitives that are too verbose for typical use. Therefore, developers should use macros that define commonly used combinations in a more concise form. C or C++ should add the following to their precompiled headers:
  - #include “sal.h”

## Appendix H: SDL SAL Recommendations for Native Win32 Code > SAL Recommendations

- [R-0288] (recommendation) Start with new code only. Microsoft strongly recommends that you also plan to annotate old code.
- [R-0289] (recommendation) All function prototypes that accept buffers in internal header files you create should be SAL annotated.
- [R-0290] (recommendation) If you create public headers, you should annotate all function prototypes that read or write to buffers.

## Appendix H: SDL SAL Recommendations for Native Win32 Code > SAL in Practice

- [context] All examples use the __declspec form.
- [context] A classic example is that of a function that takes a buffer and a buffer size as arguments. You know that the two arguments are closely connected, but the compiler and the source code analysis tools do not know that. SAL helps bridge that gap.
- [context] A list of common SAL annotations, with examples, can be found on Michael Howard's blog.
- [context] The following code demonstrates this benefit by annotating a writeable buffer named buf:
- [context] void FillString(
- [context] TCHAR* buf,
- [context] int cchBuf,
- [context] TCHAR ch) {
- [context] for (int i = 0; i < cchBuf; i++)
- [context] buf[i] = ch;
- [context] }
- [context] cchBuf is the character count of buf. Adding SAL helps link the two arguments together:
- [context] void FillString(
- [context] __out_ecount(cchBuf) TCHAR* buf,
- [context] int cchBuf,
- [context] TCHAR ch) {
- [context] for (int i = 0; i < cchBuf; i++)
- [context] buf[i] = ch;
- [context] }
- [context] If you compile this code for Unicode, a potential buffer overrun exists when you call this code:
- [context] TCHAR buf[MAX_PATH];
- [context] FillString(buf, sizeof(buf), '\0');
- [R-0291] (recommendation) sizeof is a byte count, not a character count. The programmer should have used countof.
- [context] In the __out_ecount macro, __out means the buffer is an “out” buffer and is written to by the functions. The buffer size, in elements, is _ecount(cchBuf). Note that this function cannot handle a NULL buf, if it could, then the following macro could be used: __out_ecount_opt(cchBuf), where _opt means optional.
- [context] The following example shows a function that reads to a buffer and writes to another.
- [context] void CopyRange(__in_ecount(cchFrom) const char *from,
- [context] size_t cchFrom,
- [context] __out_ecount(cchTo) char *to,
- [context] size_t cchTo);

## Appendix H: SDL SAL Recommendations for Native Win32 Code > Tools Usage

- [context] To take advantage of SAL, make sure you compile your code with a version of Microsoft Visual C++® 2005 or Visual C++ 2008 that support the /analyze compile-time flag.

## Appendix H: SDL SAL Recommendations for Native Win32 Code > Top Severity Warnings to Triage for Fixing

- [context] 6029  Possible buffer overrun in call to <function>: use of unchecked value
- [context] 6053  Call to <function>: may not zero-terminate string <variable>
- [context] 6057  Buffer overrun due to number of characters/number of bytes mismatch in call to <function>
- [context] 6059  Incorrect length parameter in call to <function>: pass the number of remaining characters, not the buffer size of <variable>
- [context] 6200  Index <name> is out of valid index range <min> to <max> for non-stack buffer <variable>
- [context] 6201  Buffer overrun for <variable>, which is possibly stack allocated: index <name> is out of valid index range <min> to <max>
- [context] 6202  Buffer overrun for <variable>, which is possibly stack allocated, in call to <function>: length <size> exceeds buffer size <max>
- [context] 6203  Buffer overrun for buffer <variable> in call to <function>: length <size> exceeds buffer size
- [context] 6204  Possible buffer overrun in call to <function>: use of unchecked parameter <variable>
- [context] 6209  Using “sizeof<variable1>” as parameter <number> in call to <function> where <variable2> may be an array of wide characters; did you intend to use character count rather than byte count?
- [context] 6248  Setting a SECURITY_DESCRIPTOR’s DACL to NULL will result in an unprotected object
- [context] 6383  Buffer overrun due to conversion of an element count into a byte count

## Appendix H: SDL SAL Recommendations for Native Win32 Code > Benefits of SAL

- [context] Because SAL provides more function interface information to the compiler toolset, SAL finds more issues earlier and with less noise.

## Appendix H: SDL SAL Recommendations for Native Win32 Code > Summary

- [R-0292] (recommendation) Microsoft recommends that you start by annotating new code only. As time permits, existing code should be annotated also.
- [R-0293] (recommendation) You should use SAL for all functions that write to buffers.
- [R-0294] (recommendation) You should consider using SAL for all functions that read from buffers.
- [context] The SDL requirement does not mandate either SAL macro syntax. Use attribute or __declspec as you see fit.
- [context] Annotate the function prototypes in headers that you create.
- [R-0295] (requirement) If you consume public headers, you must use only annotated headers.

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting

- [context] During the past few years, Microsoft added core defenses at the operating system level to help protect against some types of attacks. None of them are perfect but, when used together, they can provide an effective defense. Examples include the firewall, the –GS flag, heap checking, and DEP (also known as NX). Generally, Microsoft introduces an initial version or subset of the defense and then augments it over time, as developers and end users become accustomed to it.
- [context] A good example is Data Execution Protection (DEP). This feature was never enabled in Microsoft Windows 2000 because it had no hardware support but became available in Windows Server 2003 as an unsupported boot.ini option. DEP was then supported for the first time in Windows XP SP2 but set only for the system and not for non-system applications.
- [context] Another example, and the focus of this requirement, is the ability to detect and respond to heap corruption. In the past, there was no protection in the heap from heap-based buffer overruns. Microsoft then added metadata checking, primarily in the form of forward and backward link-checking post block-free to determine whether a heap overrun had occurred. However, for application compatibility reasons, the mitigation was limited to preventing the arbitrary write controlled by a potential exploit from taking place, and the application was allowed to continue to run after the point the corruption was detected. Windows Vista includes a more robust mechanism—the application terminates when heap corruption is detected. This mechanism also helps developers find and fix heap-based overruns early in the development lifecycle.
- [context] This Heap Manager Fail Fast Setting requirement might cause reliability issues in applications that have poor heap memory management. However, the failing code is found immediately and can be fixed, which makes software both more secure and more reliable. Windows Vista has encountered only one such example in a third-party ActiveX control.
- [context] This capability is enabled for some core operating system components but not for non-system applications running on Windows Vista. This appendix outlines how to enable the option for non-system applications.

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting > Goals and Justification

- [R-0296] (requirement) Currently, even if corruption is detected in the heap manager, the process might continue to run successfully, depending on the corruption pattern, the data affected, and the usage. Some applications might hide memory-related vulnerabilities by handling exceptions, such as access violations, that are raised inside the heap manager. The goal is to find vulnerabilities early and to create robust code. Therefore, certain critical operating system components must hard fail when heap corruption is detected. Also, any new application developed and tested on Windows Vista should terminate on heap corruptions.
- [context] This requirement has two major benefits:
  - The first benefit applies to development. With this requirement in place, problematic code is more likely to be found because the failure is immediate. Think of it as an “assert” on heap overrun. However, the code that performs heap-based memory allocation and manipulation must be tested correctly. The best method to find this class of vulnerability is through fuzz testing.
  - The second benefit is in deployment. If a vulnerability is missed during development and a heap-based overrun exploit occurs, the exploit would become a denial-of-service issue rather than a potential code execution issue.
- [R-0297] (requirement) The requirement is a no-op on versions of the Windows operating system prior to Windows Vista because the required setting is ignored.

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting > Scope

- [context] The following subsections specify the scope of the Heap Manager Fail Fast Setting requirement proposal.

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting > Operating System

- [context] This requirement applies only to Win32.

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting > Products/Services

- [context] This proposal applies to code that runs on users’ computers (products) and to code that runs only on Microsoft-owned computers and accessed by users (services).

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting > Technologies

- [context] This proposal applies to unmanaged (native) code, such C and C++, but not to managed code, such as C#.

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting > New Code and Legacy Code

- [context] This proposal applies to new code but not to legacy code.

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting > External Applicability

- [context] This proposal applies to external third-party ISV code.

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting > Exceptions and Special Cases

- [context] There are no exceptions or special cases for new code.

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting > Requirement Definition

- [R-0298] (requirement) Before you use any heap–based memory, you must add the following code to your application startup:
  - (void)HeapSetInformation(NULL,
  - HeapEnableTerminationOnCorruption,
  - NULL,
  - 0);
- [R-0299] (recommendation) Microsoft also recommends that the code use the Low-Fragmentation Heap, which has been shown to be more resistant to attack than the “normal” heap in Windows. To use the Low-Fragmentation Heap, use the following code:
  - DWORD Frag = 2;
  - (void)HeapSetInformation(NULL,
  - HeapCompatibilityInformation,
  - &Frag,
  - sizeof(&Frag));
- [R-0300] (requirement) You must add these function calls as early as possible on application startup. This requirement applies to all unmanaged .EXE files, but not to dynamic-link libraries (DLLs), which do not need to call this function.

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting > Compliance Measurement

- [context] A product/service team can verify compliance in either of the two ways mentioned in the following requirement.

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting > Requirement: Measurement by Product/Service Team

- [R-0301] (requirement) Verify that the correct function is included in the main() function of the product, and attest to its use.
- [R-0302] (requirement) Or
- [R-0303] (requirement) Run the application under a kernel debugger, issue the !heap -s command, and verify that the following text appears: Termination on corruption : ENABLED.

## Appendix J: SDL Requirement: Application Verifier

- [context] Application Verifier is a runtime verification tool for unmanaged code. It helps developers quickly find subtle programming errors that can be extremely difficult to identify with typical application testing. Application Verifier makes it easier to create reliable applications by monitoring an application's interaction with the Windows operating system. It profiles the application’s use of kernel objects, the registry, the file system, and Win32 APIs (heap, handle, locks, and more).

## Appendix J: SDL Requirement: Application Verifier > Why Is Application Verifier Important?

- [context] Application Verifier can help quickly identify security issues related to heap buffer overruns by enabling it when test scenarios are covered. As a result of using it, your organization could avoid having to release security bulletins related to such problems and save you both money and credibility.

## Appendix J: SDL Requirement: Application Verifier > Code Required to Run Application Verifier

- [R-0304] (recommendation) Application Verifier should be run on all unmanaged code.
- [R-0305] (recommendation) Application Verifier is a tool that detects errors in a process (user-mode software) while the process is running. Typical findings include heap corruptions (including heap buffer overruns) and incorrect synchronizations and operations. Whenever Application Verifier finds an issue, it goes into debugger mode. Therefore, either the application being verified should run under a user-mode debugger or the system should run under a kernel debugger.

## Appendix J: SDL Requirement: Application Verifier > Application Verifier Usage Scenarios

- [context] Application Verifier (available in Visual Studio and as a download) cannot be enabled for a running process. You need to make settings as described in this appendix and then start the application. The settings are persistent until explicitly deleted. Therefore, an application always starts with AppVerifier enabled, regardless of how many times you launch it
- [R-0306] (recommendation) The scenarios in this appendix showcase the recommended command-line options for quality gates that you should run during all tests (BVTs, stress, unit, and regression) that exercise the code change.

## Appendix J: SDL Requirement: Application Verifier > Testing with Application Verifier

- [context] The expectation for this scenario is that the application does not break into debugger mode and that all tests pass with the same pass rate as when run without Application Verifier enabled.
- [context] Enable verifier for the application(s) you wish to test using:
  - appverif /verify <MyApp.exe>
  - Note: /verify enables the base checks: HANDLE_CHECKS, RPC_CHECKS, COM_CHECKS, LOCK_CHECKS, FIRST_CHANCE_EXCEPTION_CHECKS, and FULL_PAGE_HEAP.
  - If you are testing a dynamic-link library (DLL), you must enable the verifier for the test .exe that is exercising the DLL.
  - Run all your tests exercising the application.
  - Analyze any debugger break that you encounter. Debugger breaks signify bugs found by the verifier, and you need to understand and fix them.
  - When you are finished, delete all settings made with:
  - appverif /n <MyApp.exe>
- [context] You can debug any issues you find with Application Verifier by reviewing the Verifier Stop codes within the help contents.

## Appendix J: SDL Requirement: Application Verifier > Testing with Application Verifier and Fault Injection

- [context] The expectation for this scenario is that the application does not break into debugger mode. Not breaking into debugger mode means there are no errors that need to be addressed.
- [context] The pass rate for the tests may decrease significantly because random fault injections are introduced into the normal operation.
- [context] Enable verifier and fault injection for the application(s) you wish to test by using the following command-line syntax:
  - appverif /verify <MyApp.exe> /faults
  - Note: If you are testing a DLL, you can apply fault injection on a certain DLL instead of on the entire process. The command-line syntax would be:
  - appverif /verify TARGET [/faults [PROBABILITY [TIMEOUT [DLL …]]]]
  - For example, appverif /verify <mytest.exe> /faults 5 1000 d3d9.dll
  - Run all your tests exercising the application.
  - Analyze any debugger break that you encounter. Debugger breaks signify bugs found by the verifier, and you need to understand and fix them.
  - When you are finished, delete all settings made with:
  - appverif /n <MyApp.exe>
- [R-0307] (requirement) Note that running with and without fault injection exercises different code paths in an application. Therefore, you must run both scenarios to obtain the full benefit of Application Verifier.

## Appendix P: SDL-Agile Every-Sprint Requirements

- [R-0308] (requirement) Title: AllowPartiallyTrustedCallersAttribute (APTCA) review | Requirement/ Recommendation: Requirement | Applies to Managed Code: X
- [R-0309] (requirement) Title: Apply input validation (LOB) | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0310] (requirement) Title: Annotate pointers to non-const parameters using Standard Annotation Language (SAL) | Requirement/ Recommendation: Requirement | Applies to Native Code: X
- [R-0311] (requirement) Title: Avoid Exec in stored procedures | Requirement/ Recommendation: Requirement | Applies to Online Services: X
- [R-0312] (requirement) Title: Communicate privacy-impacting design changes to the team’s privacy advisor | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0313] (requirement) Title: Compile all code with the /GS compiler option | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Native Code: X
- [R-0314] (requirement) Title: Comply with SDL firewall requirements | Requirement/ Recommendation: Requirement | Applies to Managed Code: X | Applies to Native Code: X
- [R-0315] (requirement) Title: Conduct internal security design review (LOB) | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0316] (requirement) Title: Do not use banned APIs in new code | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Native Code: X
- [R-0317] (requirement) Title: Employ reflection and authentication relay defense | Requirement/ Recommendation: Requirement | Applies to Managed Code: X | Applies to Native Code: X
- [R-0318] (requirement) Title: Encrypt all secrets, such as credentials, keys, and passwords (LOB) | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0319] (requirement) Title: Ensure all ASP.NET applications use the ValidateRequest cross-site scripting input validation attribute | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X
- [R-0320] (requirement) Title: Ensure all database access is performed through parameterized queries to stored procedures | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0321] (requirement) Title: Ensure all team members have had security education within the past year | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0322] (requirement) Title: Ensure the application domain group is granted only execute permissions on the database stored procedures | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0323] (requirement) Title: Fix all issues identified by code analysis tools for unmanaged code | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Native Code: X
- [R-0324] (requirement) Title: Fix all security issues identified by CAT.NET and FxCop static analysis | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X
- [R-0325] (requirement) Title: Follow input validation and output encoding guidelines to defend against cross-site scripting attacks | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0326] (requirement) Title: Harden or disable XML entity resolution | Requirement/ Recommendation: Requirement | Applies to Managed Code: X | Applies to Native Code: X
- [R-0327] (requirement) Title: Host security deployment review (LOB) | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0328] (requirement) Title: Link all code with the /dynamicbase linker option (Address Space Layout Randomization) | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Native Code: X
- [R-0329] (requirement) Title: Link all code with the /nxcompat linker option (Data Execution Prevention) | Requirement/ Recommendation: Requirement | Applies to Native Code: X
- [R-0330] (requirement) Title: Link all code with the /safeseh linker option (safe exception handling) | Requirement/ Recommendation: Requirement | Applies to Native Code: X
- [R-0331] (requirement) Title: Mitigate against cross-site request forgery (CSRF) | Requirement/ Recommendation: Requirement | Applies to Managed Code: X
- [R-0332] (requirement) Title: Mitigate against cross-site scripting (XSS) | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0333] (requirement) Title: Secure sensitive data-at-rest (LOB) | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0334] (requirement) Title: Secure sensitive data-in-transit (LOB) | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0335] (requirement) Title: Update threat models for new features | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0336] (requirement) Title: Use HeapSetInformation | Requirement/ Recommendation: Requirement | Applies to Native Code: X
- [R-0337] (requirement) Title: Use safe integer arithmetic for memory allocation for new code | Requirement/ Recommendation: Requirement | Applies to Native Code: X
- [R-0338] (requirement) Title: Use safe redirect | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0339] (requirement) Title: Use secure cookie over HTTPS | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0340] (recommendation) Title: Use standard annotation language (SAL) to annotate all functions | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Native Code: X
- [R-0341] (requirement) Title: Use the most secure ATL version and secure COM coding requirements | Requirement/ Recommendation: Requirement | Applies to Native Code: X
- [R-0342] (requirement) Title: Use the /robust MIDL compiler switch | Requirement/ Recommendation: Requirement | Applies to Native Code: X
- [R-0343] (requirement) Title: Use the Relying Party Suite SDK | Requirement/ Recommendation: Requirement | Applies to Managed Code: X | Applies to Native Code: X
- [R-0344] (requirement) Title: Utilize LOB Secure Code Review (LOB) | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0345] (recommendation) Title: Avoid JavaScript eval function and equivalents | Requirement/ Recommendation: Recommendation | Applies to Online Services: X
- [R-0346] (recommendation) Title: Canonicalize URLs | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0347] (recommendation) Title: Employ COM best practices | Requirement/ Recommendation: Recommendation | Applies to Native Code: X
- [R-0348] (recommendation) Title: Encode long-lived pointers | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Native Code: X
- [R-0349] (recommendation) Title: Restrict database permissions | Requirement/ Recommendation: Recommendation | Applies to Online Services: X
- [R-0350] (recommendation) Title: Review error messages to ensure sensitive information is not disclosed | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0351] (recommendation) Title: Use strict /GS option | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Native Code: X
- [R-0352] (recommendation) Title: Use transport layer encryption securely | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0353] (recommendation) Title: Use whitelist of allowed domains to perform redirects | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X

## Appendix Q: SDL-Agile Bucket Requirements

- [R-0354] (requirement) Title: Debug the application with the Application Verifier enabled | Requirement/ Recommendation: Requirement | Applies to Native Code: X
- [R-0355] (requirement) Title: Disable tracing and debugging in ASP.NET applications | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X
- [R-0356] (requirement) Title: Ensure regular expressions must not execute in exponential time (O(2^n)) | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0357] (requirement) Title: Ensure sample code complies with appropriate SDL development practices | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0358] (requirement) Title: Employ network fuzzing | Requirement/ Recommendation: Requirement | Applies to Managed Code: X | Applies to Native Code: X
- [R-0359] (requirement) Title: Investigate and service any reported /GS crashes | Requirement/ Recommendation: Requirement | Applies to Native Code: X
- [R-0360] (requirement) Title: Perform ActiveX control fuzzing | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Native Code: X
- [R-0361] (requirement) Title: Perform attack surface analysis | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0362] (requirement) Title: Perform binary analysis (BinScope) | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0363] (requirement) Title: Perform COM object testing | Requirement/ Recommendation: Requirement | Applies to Native Code: X
- [R-0364] (requirement) Title: Perform cross-domain scripting testing | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0365] (requirement) Title: Perform file fuzz testing | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Native Code: X
- [R-0366] (requirement) Title: Perform RPC fuzz testing | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Native Code: X
- [R-0367] (recommendation) Title: Conduct in-depth manual and automated code review for high-risk code | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0368] (recommendation) Title: Perform data flow testing | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0369] (recommendation) Title: Perform input validation testing | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0370] (recommendation) Title: Perform replay testing | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0371] (requirement) Title: Avoid cross-domain access to authenticated sites | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0372] (requirement) Title: Comply with User Account Control (UAC) best practices to ensure all code runs as a non-administrator | Requirement/ Recommendation: Requirement | Applies to Managed Code: X | Applies to Native Code: X
- [R-0373] (requirement) Title: Conduct a privacy review | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0374] (requirement) Title: Ensure all code is compliant with the SDL Cryptographic Standards | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0375] (requirement) Title: Ensure all code is compliant with the SDL Privacy Guidelines document | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0376] (requirement) Title: Incorporate third-party component licensing security requirements in all new contracts | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0377] (requirement) Title: Opt out of automatic MIME sniffing | Requirement/ Recommendation: Requirement | Applies to Managed Code: X | Applies to Native Code: X
- [R-0378] (requirement) Title: Use strongly named assemblies, and request minimal permissions | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X
- [R-0379] (recommendation) Title: Apply no-open header to user-supplied downloadable files | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0380] (recommendation) Title: Complete in-depth threat model training | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0381] (recommendation) Title: Disable rarely used features by default, to reduce attack surface | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0382] (recommendation) Title: Grant minimal privileges | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0383] (recommendation) Title: Review planning and design specifications for user interface elements | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0384] (recommendation) Title: Use Windows Imaging Component to process image data | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Native Code: X
- [R-0385] (requirement) Title: Add or update privacy scenarios in the test plan | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0386] (requirement) Title: Create or update the list of response contacts | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0387] (requirement) Title: Define or update the privacy bug bar | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0388] (requirement) Title: Define or update the security bug bar | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0389] (requirement) Title: Ensure symbols are available internally for all public releases | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0390] (recommendation) Title: Create or update a business continuity-disaster recovery plan | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0391] (recommendation) Title: Create or update a network down plan | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0392] (recommendation) Title: Create or update content publishing plan | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0393] (recommendation) Title: Create or update privacy support documents | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X

## Appendix R: SDL-Agile One-Time Requirements

- [R-0394] (requirement) Title: Avoid writable PE segments | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Native Code: X
- [R-0395] (requirement) Title: Create a baseline threat model | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0396] (requirement) Title: Determine security response standards | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0397] (requirement) Title: Do not use Visual Basic 6 to build products | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0398] (requirement) Title: Establish a security response plan | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0399] (requirement) Title: Identify primary security and privacy contacts | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0400] (requirement) Title: Identify your team’s privacy expert | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0401] (requirement) Title: Identify your team’s security expert | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0402] (requirement) Title: Threat model your product, its attack surface, and its new features | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0403] (requirement) Title: Use approved XML parsers | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Native Code: X
- [R-0404] (requirement) Title: Use latest compiler versions | Requirement/ Recommendation: Requirement | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0405] (requirement) Title: Use minimum code generation suite and libraries | Requirement/ Recommendation: Requirement | Applies to Managed Code: X | Applies to Native Code: X
- [R-0406] (recommendation) Title: Configure bug tracking to track the cause and effect of security bugs | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X
- [R-0407] (recommendation) Title: Remove dependencies on NTLM authentication | Requirement/ Recommendation: Recommendation | Applies to Online Services: X | Applies to Managed Code: X | Applies to Native Code: X

## Appendix S: SDL-Agile High-Risk Code

- [R-0408] (recommendation) The following defines the highest risk code (at the time of writing) that should receive greater scrutiny if the code is legacy code and should be written with the greatest care if the code is new code.
- [context] Windows services and *nix daemons listening on network connections
- [context] Windows services running as SYSTEM or *nix daemons running as root
- [context] Code listening on unauthenticated network ports connections
- [context] ActiveX controls
- [context] Browser protocol handlers (for example, about: or mms:)
- [context] setuid root applications on *nix
- [context] Code that parses data from untrusted (non-admin or remote) files
- [context] File parsers or MIME handlers

# Part II — normative tables and enumerations (verbatim)

## Appendix B: Security Definitions for Vulnerability Work Item Tracking

It is critical for project teams to specify and maintain a work item tracking system that allows for creation, triage, assignment, tracking, remediation, and reporting of software vulnerabilities. Optimally, work item tracking should also include the ability to track security and privacy issues by cause and effect of the security bugs. The work item tracking system should have access controls in place to ensure that changes to information in the system (whether malicious or accidental) can be tracked appropriately.

Ensure that the vulnerability/work item tracking system used includes fields with the following values (at a minimum):

### Security Bug Cause

The following fields describe causes of vulnerabilities:

- Not a Security Bug. This field is self-explanatory.
- Buffer Overflow/Underflow. A failure to check or to limit input data buffer sizes before data is manipulated or processed.
- Arithmetic Error. A failure to check bounds conditions for integer math, in which results of calculations might overflow or underflow data type. An example is integer overflow.
- SQL/Script Injection. Allows attackers to alter intended behavior by altering script.
- Directory Traversal. Allows attackers access to navigate host directory structure.
- Race Condition. A security vulnerability caused by code timing or synchronization issues.
- Cross-Site Scripting. This cause involves website weaknesses that allow attackers to have inappropriate access to information or resources. Although a subset of script injection, it is listed separately.
- Cryptographic Weakness. Insufficient or incorrect use of cryptography to protect data.
- Weak Authentication. Insufficient checks or tests to validate that the user or process is who or what it claims to be.
- Weak Authorization/Inappropriate Permission or ACL. Access to resources or data for an authenticated user that are not appropriate for users of that type. For example, allowing anonymous or guest users access to sensitive information.
- Ineffective Secret Hiding. Insufficient or incorrect protection of cryptographic keys or passwords. For example, storing passwords in plain text in registry or not zeroing out password buffers.
- Unlimited Resource Consumption (DoS). A failure to check or limit resource allocations that might allow an attacker to deny service by depleting available resources.
- Incorrect/No Error Messages. Insufficient or incorrect reporting of error checking.
- Incorrect/No Pathname Canonicalization. An incorrect trust decision based on a resource name, or allowing access to a resource because an attacker bypassed location or name restrictions.
- Other. None of the above.

### Security Bug Effect

The following definitions are from Writing Secure Code, Second Edition.

- Not a Security Bug. This field is self-explanatory.
- Spoofing. Spoofing threats allow an attacker to pose as another user, allow a rogue server to pose as a valid server, or rogue code to pose as valid code.
- Tampering. Data tampering means malicious modification of data.
- Repudiation. Repudiation threats are associated with users who deny having performed an action without other parties having any way to prove otherwise. For example, a user with malicious intent performs an illegal operation on a computer that is unable to trace the prohibited operation.
- Information Disclosure. Information disclosure threats involve the exposure of information to individuals who are not supposed to have access to it. For example, such a threat might be a user’s ability to read a file to which they did not have access, or an intruder’s ability to read data in transit between two computers.
- Denial of Service. Denial of Service (DoS) attacks deny or restrict services to valid users.
- Elevation of Privilege. In this type of threat, a user increases their permissions level and therefore can perform actions they should not be allowed to perform. Any unprivileged user who gains unauthorized access might have sufficient access to compromise or even destroy the system.
- Attack Surface Reduction. This type of threat is not a security bug in the same sense as the other items listed. However, when you attempt to reduce the attack surface, it is valuable to track bugs that describe services and functionality that affect the attack surface. It is important to identify attack surface, even though interfaces that are exposed on the attack surface are technically not vulnerabilities. Such bugs are assigned the Attack Surface Reduction designation.

## Appendix M: SDL Privacy Bug Bar (Sample)

Note: This sample document is for illustration purposes only. The content presented below outlines basic criteria to consider when creating privacy processes. It is not an exhaustive list of activities or criteria and should not be treated as such.

Please refer to the definitions of terms in this section.

| End-User Scenarios <br> Usage notes: These scenarios apply to consumers, enterprise clients, and enterprise administrators acting as end users. For enterprise administrators acting in their administrative role, see the Enterprise Administrators Scenarios. |  |
|---|---|
| Critical | Lack of notice and consent <br> Example: Transfer of sensitive personally identifiable information (PII) from the user's system without prominent notice and explicit opt-in consent in the UI prior to transfer. <br> Lack of user controls <br> Example: Ongoing collection and transfer of non-essential PII without the ability within the UI for the user to stop subsequent collection and transfer. <br> Lack of data protection <br> Example: PII is collected and stored in a persistent general database without an authentication mechanism for users to access and correct stored PII. <br> Lack of child protection <br> Example: Age is not collected for a site or service that is attractive to or directed at children and the site collects, uses, or discloses the user’s PII. <br> Improper use of cookies <br> Example: Sensitive PII stored in a cookie is not encrypted. <br> Lack of internal data management and control <br> Example: Access to PII stored at organization is not restricted only to those who have a valid business need or there is no policy to revoke access after it is no longer required. <br> Insufficient legal controls <br> Example: Product or feature transmits data to an agent or independent third party that has not signed a legally approved contract. |
| Important | Lack of notice and consent <br> Example: Transfer of non-sensitive PII from the user's computer without prominent notice and explicit opt-in consent in the UI prior to transfer. <br> Lack of user controls <br> Example: Ongoing collection and transfer of non-essential anonymous data without the ability in the UI for the user to stop subsequent collection and transfer. <br> Lack of data protection <br> Example: Persistently stored non-sensitive PII lacks a mechanism to prevent unauthorized access. A mechanism is not required where the user is notified in the UI that data will be shared (for example, folder labeled “Shared”). <br> Data minimization <br> Example: Sensitive PII transmitted to an independent third party is not necessary to achieve the disclosed business purpose. <br> Improper use of cookies <br> Example: Non-sensitive PII stored in a persistent cookie is not encrypted. |
| Moderate | Lack of user controls <br> Example: PII is collected and stored locally as hidden metadata without any means for a user to remove the metadata. PII is accessible by others or may be transmitted if files or folders are shared. <br> Lack of data protection <br> Example: Temporarily stored non-sensitive PII lacks a mechanism to prevent unauthorized access during transfer or storage. A mechanism is not required where the sharing of information is obvious (for example, user name) or there is prominent notice. <br> Data minimization <br> Example: Non-sensitive PII or anonymous data transmitted to an independent third party is not necessary to achieve disclosed business purpose. <br> Improper use of cookies <br> Example: Use of persistent cookie where a session cookie would satisfy the purpose. Or, persisting a cookie for a period that is longer than necessary to satisfy the purpose. <br> Lack of internal data management and control <br> Example: Data stored at organization does not have a retention policy. |
| Low | Lack of notice and consent <br> Example: PII is collected and stored locally as hidden metadata without discoverable notice. PII is not accessible by others and is not transmitted if files or folders are shared. |

| Enterprise Administration Scenarios <br> Usage notes: These scenarios apply to enterprise administrators acting in their administrative role. For Enterprise administrators in an end-user role, see the End User Scenarios. |  |
|---|---|
| Critical | Lack of enterprise controls <br> Example: Automated data transfer of sensitive PII from the user's system without prominent notice and explicit opt-in consent in the UI from the enterprise administrator prior to transfer. <br> Insufficient privacy disclosure <br> Example: Deployment or development guide for enterprise administrators provides legal advice. |
| Important | Lack of enterprise controls <br> Example: Automated data transfer of non-sensitive PII or anonymous data from the user's system without prominent notice and explicit opt-in consent in the UI from the enterprise administrators prior to transfer. Notice and consent must appear in the UI—not through the End-User License Agreement (EULA) or Terms of Service. <br> Insufficient privacy disclosure <br> Example: Disclosure to enterprise administrators, such as deployment guide or UX, does not disclose storage or transfer of PII. |
| Moderate | Lack of enterprise controls <br> Example: No mechanism is provided or identified to help the enterprise administrators prevent accidental disclosure of user data (for example, set site permissions). |

### Definition of Terms

anonymous data

Non-personal data that has no connection to an individual. By itself, it has no intrinsic link to an individual user. For example, hair color or height (in the absence of other correlating information) does not identify a user.

child or children

Under 14 years of age in Korea and under 13 years of age in the United States.

discoverable notice

A discoverable notice is one the user has to find (for example, by locating and reading a privacy statement of a website or by selecting a privacy statement link from a Help menu).

discrete transfer

Data transfer is discrete when it is an isolated data capture event that is not ongoing.

essential metadata

Metadata that is necessary to the application for supporting the file (for example, file extension).

explicit consent

Explicit consent requires that the user take—or have the ability to take—an explicit action before data is collected or transferred.

hidden metadata

Hidden metadata is information that is stored with a file but is not visible to the user in all views. Hidden data may include personal information or information that the user would likely not want to distribute publicly. If such information is included, the user must be made aware that this information exists and must be given appropriate control over sharing it.

implicit consent

Implicit consent does not require an explicit action indicating consent from the user; the consent is implicit in the operation the user initiates.

non-essential metadata

Metadata that is not necessary to the application for supporting the file (for example, key words).

persistent storage

Persistent storage of data means that the data continues to be available after the user exits the application.

personally identifiable information (PII)

Personally identifiable information is any information (i) that identifies or can be used to identify, contact, or locate the person to whom such information pertains, or (ii) from which identification or contact information of an individual person can be derived. Personally Identifiable Information includes, but is not limited to, name, address, phone number, fax number, e-mail address, financial profiles, medical profile, social security number, and credit card information. Additionally, to the extent that unique information (which by itself is not PII, such as a unique identifier or IP address) is associated with PII, such unique information will also be considered PII.

prominent notice

A prominent notice is one that is designed to catch the user’s attention. Prominent notices should contain a high-level, substantive summary of the privacy-impacting aspects of the feature, such as what data is being collected and how that data will be used. The summary should be fully visible to a user without additional action on the part of the user, such as having to scroll down the page. Prominent notices should also include clear instructions for where the user can get additional information (such as in a privacy statement).

sensitive PII

Sensitive personally identifiable information includes any data that could (i) be used to discriminate (ethnic heritage, religious preference, physical or mental health, for example), (ii) facilitate identity theft (like mother’s maiden name), or (iii) permit access to a user’s account (like passwords or PINs). Note that if the data described in this paragraph is not commingled with PII during storage or transfer, and it is not correlated with PII, then the data can be treated as Anonymous Data. If there is any doubt, however, the data should be treated as Sensitive PII. While not technically Sensitive PII, user data that makes users nervous (such as real-time location) should be handled in accordance with the rules for Sensitive PII.

Critical. Release may create legal or regulatory liability for the organization.

Important. Release may create high risk of negative reaction by privacy advocates or damage the organization’s image.

Moderate. Some user concerns may be raised, some privacy advocates may question, but repercussion will be limited.

Low. May cause some user queries. Scrutiny by privacy advocates unlikely.

temporary storage

Temporary storage of data means that the data is only available while the application is running.

## Appendix N: SDL Security Bug Bar (Sample)

Note: This sample document is for illustration purposes only. The content presented below outlines basic criteria to consider when creating security processes. It is not an exhaustive list of activities or criteria and should not be treated as such.

Please refer to the definitions of terms in this section.

| Server <br> Please refer to the Denial of Service Matrix for a complete matrix of server DoS scenarios. <br> The server bar is usually not appropriate when user interaction is part of the exploitation process. If a Critical vulnerability exists only on server products, and is exploited in a way that requires user interaction and results in the compromise of the server, the severity may be reduced from Critical to Important in accordance with the NEAT/data definition of extensive user interaction presented at the start of the client severity pivot. |  |
|---|---|
| Critical | Server summary: Network worms or unavoidable cases where the server is “owned.” <br> Elevation of privilege: The ability to either execute arbitrary code or obtain more privilege than authorized. <br> Remote anonymous user <br> Examples: <br> Unauthorized file system access: arbitrary writing to the file system <br> Execution of arbitrary code <br> SQL injection (that allows code execution) <br> All write access violations (AV), exploitable read AVs, or integer overflows in remote anonymously callable code |
| Important | Server summary: Non-default critical scenarios or cases where mitigations exist that can help prevent critical scenarios. <br> Denial of service: Must be “easy to exploit” by sending a small amount of data or be otherwise quickly induced. <br> Anonymous <br> Persistent DoS <br> Examples: <br> Sending a single malicious TCP packet results in a Blue Screen of Death (BSoD) <br> Sending a small number of packets that causes a service failure <br> Temporary DoS with amplification <br> Examples: <br> Sending a small number of packets that causes the system to be unusable for a period of time <br> A web server (like IIS) being down for a minute or longer <br> A single remote client consuming all available resources (sessions, memory) on a server by establishing sessions and keeping them open <br> Authenticated <br> Persistent DoS against a high value asset <br> Example: <br> Sending a small number of packets that causes a service failure for a high value asset in server roles (certificate server, Kerberos server, domain controller), such as when a domain-authenticated user can perform a DoS on a domain controller <br> Elevation of privilege: The ability to either execute arbitrary code or to obtain more privilege than intended. <br> Remote authenticated user <br> Local authenticated user (Terminal Server) <br> Examples: <br> Unauthorized file system access: arbitrary writing to the file system <br> Execution of arbitrary code <br> All write AVs, exploitable read AVs, or integer overflows in code that can be accessed by remote or local authenticated users that are not administrators (Administrator scenarios do not have security concerns by definition, but are still reliability issues.) <br> Information disclosure (targeted) <br> Cases where the attacker can locate and read information from anywhere on the system, including system information that was not intended or designed to be exposed <br> Examples: <br> Personally identifiable information (PII) disclosure—see the Microsoft Privacy Standard for Development (MPSD) for detailed definitions and examples of PII <br> Disclosure of PII (email addresses, phone numbers, credit card information) <br> Attacker can collect PII without user consent or in a covert fashion <br> Spoofing <br> An entity (computer, server, user, process) is able to masquerade as a specific entity (user or computer) of his/her choice. <br> Examples: <br> Web server uses client certificate authentication (SSL) improperly to allow an attacker to be identified as any user of his/her choice <br> New protocol is designed to provide remote client authentication, but flaw exists in the protocol that allows a malicious remote user to be seen as a different user of his or her choice <br> Tampering <br> Modification of any “high value asset” data in a common or default scenario where the modification persists after restarting the affected software <br> Permanent or persistent modification of any user or system data used in a common or default scenario <br> Examples: <br> Modification of application data files or databases in a common or default scenario, such as authenticated SQL injection <br> Proxy cache poisoning in a common or default scenario <br> Modification of OS or application settings without user consent in a common or default scenario <br> Security features: Breaking or bypassing any security feature provided. <br> Note that a vulnerability in a security feature is rated “Important” by default, but the rating may be adjusted based on other considerations as documented in the SDL bug bar. <br> Examples: <br> Disabling or bypassing a firewall without informing users or gaining consent <br> Reconfiguring a firewall and allowing connections to other processes |
| Moderate | Denial of service <br> Anonymous <br> Temporary DoS without amplification in a default/common install <br> Example: <br> Multiple remote clients consuming all available resources (sessions, memory) on a server by establishing sessions and keeping them open <br> Authenticated <br> Persistent DoS <br> Example: <br> Logged in Exchange user can send a specific mail message and crash the Exchange Server, and the crash is not due to a write AV, exploitable read AV, or integer overflow <br> Temporary DoS with amplification in a default/common install <br> Example: <br> Ordinary SQL Server user executes a stored procedure installed by some product and consumes 100% of the CPU for a few minutes <br> Information disclosure (targeted) <br> Cases where the attacker can easily read information on the system from specific locations, including system information, which was not intended/designed to be exposed. <br> Examples: <br> Targeted disclosure of anonymous data—see the Microsoft Privacy Standard for Development (MPSD) for detailed definitions of anonymous data <br> Targeted disclosure of the existence of a file <br> Targeted disclosure of a file version number <br> Spoofing <br> An entity (computer, server, user, process) is able to masquerade as a different, random entity that cannot be specifically selected. <br> Example: <br> Client properly authenticates to server, but server hands back a session from another random user who happens to be connected to the server at the same time <br> Tampering <br> Permanent or persistent modification of any user or system data in a specific scenario <br> Examples: <br> Modification of application data files or databases in a specific scenario <br> Proxy cache poisoning in a specific scenario <br> Modification of OS/application settings without user consent in a specific scenario <br> Temporary modification of data in a common or default scenario that does not persist after restarting the OS/application/session <br> Security assurances: <br> A security assurance is either a security feature or another product feature/function that customers expect to offer security protection. Communications have messaged (explicitly or implicitly) that customers can rely on the integrity of the feature, and that’s what makes it a security assurance. Security bulletins will be released for a shortcoming in a security assurance that undermines the customer’s reliance or trust. <br> Examples: <br> Processes running with normal “user” privileges cannot gain “admin” privileges unless admin password/credentials have been provided via intentionally authorized methods. <br> Internet-based JavaScript running in Internet Explorer cannot control anything the host operating system unless the user has explicitly changed the default security settings. |
| Low | Information disclosure (untargeted) <br> Runtime information <br> Example: <br> Leak of random heap memory <br> Tampering <br> Temporary modification of data in a specific scenario that does not persist after restarting the OS/application |

| Client <br> Extensive user action is defined as: <br> “User interaction” can only happen in client-driven scenario. <br> Normal, simple user actions, like previewing mail, viewing local folders, or file shares, are not extensive user interaction. <br> “Extensive” includes users manually navigating to a particular website (for example, typing in a URL) or by clicking through a yes/no decision. <br> “Not extensive” includes users clicking through e-mail links. <br> NEAT qualifier (applies to warnings only). Demonstrably, the UX is: <br> Necessary (Does the user really need to be presented with the decision?) <br> Explained (Does the UX present all the information the user needs to make this decision?) <br> Actionable (Is there a set of steps users can take to make good decisions in both benign and malicious scenarios?) <br> Tested (Has the warning been reviewed by multiple people, to make sure people understand how to respond to the warning?) <br> Clarification: Note that the effect of extensive user interaction is not one level reduction in severity, but is and has been a reduction in severity in certain circumstances where the phrase extensive user interaction appears in the bug bar. The intent is to help customers differentiate fast-spreading and wormable attacks from those, where because the user interacts, the attack is slowed down. This bug bar does not allow you to reduce the Elevation of Privilege below Important because of user interaction. |  |
|---|---|
| Critical | Client summary: <br> Network Worms or unavoidable common browsing/use scenarios where the client is “owned” without warnings or prompts. <br> Elevation of privilege (remote): The ability to either execute arbitrary code or to obtain more privilege than intended. <br> Examples: <br> Unauthorized file system access: writing to the file system <br> Execution of arbitrary code without extensive user action <br> All write AVs, exploitable read AVs, stack overflows, or integer overflows in remotely callable code (without extensive user action) |
| Important | Client summary: <br> Common browsing/use scenarios where client is “owned” with warnings or prompts, or via extensive actions without prompts. Note that this does not discriminate over the quality/usability of a prompt and likelihood a user might click through the prompt, but just that a prompt of some form exists. <br> Elevation of privilege (remote) <br> Execution of arbitrary code with extensive user action <br> All write AVs, exploitable read AVs, or integer overflows in remote callable code (with extensive user action) <br> Elevation of privilege (local) <br> Local low privilege user can elevate themselves to another user, administrator, or local system. <br> All write AVs, exploitable read AVs, or integer overflows in local callable code <br> Information disclosure (targeted) <br> Cases where the attacker can locate and read information on the system, including system information that was not intended or designed to be exposed. <br> Examples: <br> Unauthorized file system access: reading from the file system <br> Disclosure of PII—see the Microsoft Privacy Standard for Development (MPSD) for detailed definitions and examples of PII <br> Disclosure of PII (email addresses, phone numbers) <br> Phone home scenarios <br> Denial of service <br> System corruption DoS requires re-installation of system and/or components. <br> Example: <br> Visiting a web page causes registry corruption that makes the machine unbootable <br> Drive-by DoS <br> Criteria: <br> Un-authenticated System DoS <br> Default exposure <br> No default security features or boundary mitigations (firewalls) <br> No user interaction <br> No audit and punish trail <br> Example: <br> Drive-by Bluetooth system DoS or SMS in a mobile phone <br> Spoofing <br> Ability for attacker to present a UI that is different from but visually identical to the UI that users must rely on to make valid trust decisions in a default/common scenario. A trust decision is defined as any time the user takes an action believing some information is being presented by a particular entity—either the system or some specific local or remote source. <br> Examples: <br> Displaying a different URL in the browser’s address bar from the URL of the site that the browser is actually displaying in a default/common scenario <br> Displaying a window over the browser’s address bar that looks identical to an address bar but displays bogus data in a default/common scenario <br> Displaying a different file name in a “Do you want to run this program?” dialog box than that of the file that will actually be loaded in a default/common scenario <br> Display a “fake” login prompt to gather user or account credentials <br> Tampering <br> Permanent modification of any user data or data used to make trust decisions in a common or default scenario that persists after restarting the OS/application <br> Examples: <br> Web browser cache poisoning <br> Modification of significant OS/application settings without user consent <br> Modification of user data <br> Security features: Breaking or bypassing any security feature provided <br> Examples: <br> Disabling or bypassing a firewall with informing user or gaining consent <br> Reconfiguring a firewall and allowing connection to other processes <br> Using weak encryption or keeping the keys stored in plain text <br> AccessCheck bypass <br> Bitlocker bypass; for example not encrypting part of the drive <br> Syskey bypass, a way to decode the syskey without the password |
| Moderate | Denial of service <br> Permanent DoS requires cold reboot or causes Blue Screen/Bug Check <br> Example: <br> Opening a Word document causes the machine to Blue Screen/Bug Check <br> Information disclosure (targeted) <br> Cases where the attacker can read information on the system from known locations, including system information that was not intended or designed to be exposed <br> Examples: <br> Targeted existence of file <br> Targeted file version number <br> Spoofing <br> Ability for attacker to present a UI that is different from but visually identical to the UI that users are accustomed to trust in a specific scenario. “Accustomed to trust” is defined as anything a user is commonly familiar with based on normal interaction with the operating system or application but does not typically think of as a “trust decision.” <br> Examples: <br> Web browser cache poisoning <br> Modification of significant OS/application settings without user consent <br> Modification of user data |
| Low | Denial of service <br> Temporary DoS requires restart of application <br> Example: <br> Opening a HTML document causes Internet Explorer to crash <br> Spoofing <br> Ability for attacker to present a UI that is different from but visually identical to the UI that is a single part of a bigger attack scenario <br> Examples: <br> User has to go a “malicious” web site, click on a button in spoofed dialog box, and is then susceptible to a vulnerability based on a different browser bug <br> Tampering <br> Temporary modification of any data that does not persist after restarting the OS/application.Information disclosure (untargeted) <br> Example: <br> Leak of random heap memory |

### Definition of Terms

authenticated

Any attack which has to include authenticating by the network. This implies that logging of some type must be able to occur so that the attacker can be identified.

anonymous

Any attack which does not need to authenticate to complete.

client

Either software that runs locally on a single computer or software that accesses shared resources provided by a server over a network.

default/common

Any features that are active out of the box or that reach more than 10 percent of users.

scenario

Any features that require special customization or use cases to enable, reaching less than 10 percent of users.

server

Computer that is configured to run software that awaits and fulfills requests from client processes that run on other computers.

Critical. A security vulnerability that would be rated as having the highest potential for damage.

Important. A security vulnerability that would be rated as having significant potential for damage, but less than Critical.

Moderate. A security vulnerability that would be rated as having moderate potential for damage, but less than Important.

Low. A security vulnerability that would be rated as having low potential for damage.

targeted information disclosure

Ability to intentionally select (target) desired information.

temporary DoS

A temporary DoS is a situation where the following criteria are met:

- The target cannot perform normal operations due to an attack.
- The response to an attack is roughly the same magnitude as the size of the attack.
- The target returns to the normal level of functionality shortly after the attack is finished. The exact definition of “shortly” should be evaluated for each product.

For example, a server is unresponsive while an attacker is constantly sending a stream of packets across a network, and the server returns to normal a few seconds after the packet stream stops.

temporary DoS with amplification

A temporary DoS with amplification is a situation where the following criteria are met:

- The target cannot perform normal operations due to an attack.
- The response to an attack is magnitudes beyond the size of the attack.
- The target returns to the normal level of functionality after the attack is finished, but it takes some time (perhaps a few minutes).

For example, if you can send a malicious 10-byte packet and cause a 2048k response on the network, you are DoSing the bandwidth by amplifying our attack effort.

permanent DoS

A permanent DoS is one that requires an administrator to start, restart, or reinstall all or parts of the system. Any vulnerability that automatically restarts the system is also a permanent DoS.

### Denial of Service (Server) Matrix

| Authenticated vs. Anonymous attack | Default/Common vs. Scenario | Temporary DoS vs. Permanent | Rating |
|---|---|---|---|
| Authenticated | Default/Common | Permanent | Moderate |
| Authenticated | Default/Common | Temporary DoS with amplification | Moderate |
| Authenticated | Default/Common | Temporary DoS | Low |
| Authenticated | Scenario | Permanent | Moderate |
| Authenticated | Scenario | Temporary DoS with amplification | Low |
| Authenticated | Scenario | Temporary DoS | Low |
| Anonymous | Default/Common | Permanent | Important |
| Anonymous | Default/Common | Temporary DoS with amplification | Important |
| Anonymous | Default/Common | Temporary DoS | Moderate |
| Anonymous | Scenario | Permanent | Important |
| Anonymous | Scenario | Temporary DoS with amplification | Important |
| Anonymous | Scenario | Temporary DoS | Low |

# Part III — normative statements outside the headed Requirements/Recommendations sections (added by the verify pass, 2026-10-03)

The extract pass took only statements under the "Security/Privacy Requirements/Recommendations" headings, the appendix requirement tables and the Agile tables. These paragraphs carry *must / should / required / requires / need to / mandatory* elsewhere in the document and were missing from both Part I and `requirements.yaml`. Verbatim from `word/document.xml`, in document order, grouped by heading path; a lead-in ending ":" is followed by its list items.

## 

- **[R-0409]** (recommendation) Organizations that wish to implement the SDL should read the Simplified Implementation of the Microsoft SDL whitepaper. This whitepaper illustrates the core concepts of the Microsoft SDL and discusses the individual security activities that should be performed in order to follow the SDL process. Visit www.microsoft.com/sdl for resources and tools.

## Introduction

- **[R-0410]** (requirement) All software developers must address security threats. Computer users now require trustworthy and secure software, and developers who address security threats more effectively than others can gain a competitive advantage in the marketplace. Also, an increased sense of social responsibility now compels developers to create secure software that requires fewer patches and less security management.

- **[R-0411]** (requirement) Secure software development is mandatory for software that is developed for the following uses:
  - In a business environment
  - To process personally identifiable information (PII) or other sensitive information
  - To communicate regularly over the Internet or other networks

- **[R-0412]** (requirement) This document describes both required and recommended changes to software development tools and processes. These changes should be integrated into existing software development processes to facilitate best practices and achieve measurably improved security and privacy.

## Introduction > Secure by Default

- **[R-0413]** (recommendation) Less commonly used services off by default. If fewer than 80 percent of a program’s users use a feature, that feature should not be activated by default. Measuring 80 percent usage in a product is often difficult because programs are designed for many different personas. It can be useful to consider whether a feature addresses a core/primary use scenario for all personas. If it does, the feature is sometimes referred to as a P1 feature.

## Introduction > Privacy by Design

- **[R-0414]** (requirement) Minimize data collection and sensitivity. Collect the minimum amount of data that is required for a particular purpose, and use the least sensitive form of that data.

## Security Development Lifecycle (SDL) > What Products and Services Are Required to Adopt the SDL Process?

- **[R-0415]** (recommendation) Functionality that parses any unprotected file types that should be limited to system administrators.

## Security Development Lifecycle (SDL) > Are Service Releases Required to Adopt the SDL Process?

- **[R-0416]** (requirement) Any external release of software that can be installed on a user’s computer, regardless of operating system or platform, must comply with security and privacy policies as described in the Security Development Lifecycle. The SDL applies to new products, service releases such as product service packs, feature packs, development kits, and resource kits. The terms service pack and feature pack might not always be used in the descriptive title of a release to users, but the following definitions differentiate what constitutes a new product from a service release or feature pack.

- **[R-0417]** (requirement) New product releases are either completely new products (version 1.0) or significant updates of existing products (for example, Microsoft Office 2003). A new product release always requires a user to agree to a new software license and typically involves new packaging.

- **[R-0418]** (requirement) Service packs are the means by which product updates are distributed. Service packs might contain updates for system reliability, program compatibility, security, or privacy. A service pack requires a previous version of a product before it can be installed and used. A service pack might not always be named as such; some products may refer to a service pack as a service release, update, or refresh.

- **[R-0419]** (requirement) Resource kits are collections of resources to help administrators streamline management tasks. A resource kit must be targeted at a single product release to be treated as a service release. If a resource kit is targeted at multiple products or at multiple versions of a product, SDL requirements apply to it as described earlier for a product release.

- **[R-0420]** (requirement) Development kits provide information, specific architecture details, and tools to developers. A development kit must be targeted at a single product release to be treated as a service release. If a development kit is targeted at multiple products or at multiple versions of a product, SDL requirements from the corresponding product release apply.

- **[R-0421]** (requirement) All software releases referenced in What Products and Services Are Required to Adopt the SDL Process? must adopt the SDL. However, current SDL requirements are applied only to the new features in the service release and not retroactively to the entire product. Also, product teams are not required to change compiler versions or compile options in a service release.

## Security Development Lifecycle (SDL) > How Are New Recommendations and Requirements Added to the SDL Process?

- **[R-0422]** (requirement) The Security Development Lifecycle consists of the proven best practices and tools that were successfully used to develop recent products. However, the area of security and privacy changes frequently, and the Security Development Lifecycle must continue to evolve and to use new knowledge and tools to help build even more trusted products. But because product development teams must also have some visibility and predictability of security requirements in order to plan schedules, it is necessary to define how new recommendations and requirements are introduced, as well as when new requirements are added to the SDL.

- **[R-0423]** (requirement) New SDL recommendations may be added at any time, and they do not require immediate implementation by product teams. New SDL requirements should be released and published at six-month intervals. New requirements will be finalized and published three months before the beginning of the next six-month interval for which they are required. For more information about how to hold teams accountable for requirements, see How Are SDL Requirements Determined for a Specific Product Release?

## Security Development Lifecycle (SDL) > How Are SDL Requirements Determined for a Specific Product Release?

- **[R-0424]** (requirement) One-year cap. At a minimum, a product must meet SDL requirements that are older than one year at the time of release to manufacture (RTM) or release to web (RTW).

- **[R-0425]** (requirement) If a product registered with the SDL team in the first half of calendar year 2012 (H1CY12) but does not ship until H2CY13, it must meet all H2CY12 requirements.

## Pre-SDL Requirements: Security Training > Education and Awareness

- **[R-0426]** (recommendation) All members of software development teams should receive appropriate training to stay informed about security basics and recent trends in security and privacy. Individuals who develop software programs should attend at least one security training class each year. Security training can help ensure software is created with security and privacy in mind and can also help development teams stay current on security issues. Project team members are strongly encouraged to seek additional security and privacy education that is appropriate to their needs or products.

- **[R-0427]** (recommendation) A number of key knowledge concepts are important to successful software security. These concepts can be broadly categorized as either basic or advanced security knowledge. Each technical member of a project team (developer, tester, program manager) should be exposed to the knowledge concepts in the following subsections.

## Phase One: Requirements > Project Inception

- **[R-0428]** (recommendation) The need to consider security and privacy at a foundational level is a fundamental tenet of system development. The best opportunity to build trusted software is during the initial planning stages of a new release or a new version because development teams can identify key objects and integrate security and privacy, which minimizes disruption to plans and schedules.

## Phase Two: Design > Establish and Follow Best Practices for Design

- **[R-0429]** (recommendation) The best time to influence a project’s trustworthy design is early in its life cycle. Functional specifications may need to describe security features or privacy features that are directly exposed to users, such as requiring user authentication to access specific data or user consent before use of a high-risk privacy feature. Design specifications should describe how to implement these features and how to implement all functionality as secure features. Secure features are defined as features with functionality that is well engineered with respect to security, such as rigorously validating all data before processing it or cryptographically robust use of cryptographic APIs. It is important to consider security and privacy concerns carefully and early when you design features and to avoid attempts to add security and privacy near the end of a project’s development.

- **[R-0430]** (requirement) Threat modeling (described in Design Phase: Risk Analysis) is the other critical security activity that must be completed during the design phase.

## Phase Two: Design > Risk Analysis

- **[R-0431]** (requirement) For security concerns, threat modeling is a systematic process that is used to identify threats and vulnerabilities in software. You must complete threat modeling during project design. A team cannot build secure software unless it understands the assets the project is trying to protect, the threats and vulnerabilities introduced by the project, and details of how the project mitigates those threats. Threat modeling applies to all products and services, all code types, and all platforms. Verify that threat models exist for all attack surfaces and new features and each threat model includes: diagrams showing the software and all trust boundaries, STRIDE threats enumerated for each element that crosses a trust boundary or that connects to a data flow that crosses a trust boundary, mitigations for all threats, a list of assumptions made while threat modeling, all non-platform external dependencies that the elements in the threat model rely on.

## Phase Three: Implementation > Creating Documentation and Tools for Users That Address Security and Privacy

- **[R-0432]** (recommendation) Every release of a software program should be secure by design, in its default configuration, and in deployment. However, people use programs differently, and not everyone uses a program in its default configuration. You need to provide users with enough security information so they can make informed decisions about how to deploy a program securely. Because security and usability might conflict, you also need to educate users about the threats that exist and the balance between risk and functionality when deciding how to deploy and operate software programs.

## Phase Four: Verification > Security and Privacy Testing

- **[R-0433]** (requirement) Begin security testing very soon after the code is written. This testing stage requires one full test pass after the verification stage because potential issues and vulnerabilities might change during development.

## Phase Four: Verification > Security Push

- **[R-0434]** (recommendation) A security push is a team-wide focus on threat model updates, code review, testing, and thorough documentation review and edit. A security push is not a substitute for a lack of security discipline. Rather, it is an organized effort to uncover changes that might have occurred during development, improve security in any legacy code, and identify and remediate any remaining vulnerabilities. However, it should be noted that it is not possible to build security into software with only a security push.

- **[R-0435]** (requirement) A security push occurs after a product has entered the verification stage (reached code/feature complete). It usually begins at about the time beta testing starts. Because the results of the security push might alter the default configuration and behavior of a product, you should perform a final beta test review after the security push is complete and after all issues and required changes are resolved.

## Phase Four: Verification > Security Push > Push Preparation

- **[R-0436]** (requirement) A successful push requires planning:
  - You should allocate time and resources for the push in your project’s schedule, before you begin development. Rushing the security push will cause problems or delays during the Final Security Review.
  - Your team’s security coordinator should determine what resources are required, organize a security push leadership team, and create the needed supporting materials and resources.
  - The security representative should determine how to communicate security push information to the rest of the team. It is helpful to establish a central intranet location for all information related to the push, including news, schedules, plans, forms and documents, white papers, training schedules, and links. The intranet site should link to internal resources that help the group execute the security push. This site should serve as the primary source of information, answers, and news for employees during the push.
  - There must be well-defined criteria to determine when the push is complete.

- **[R-0437]** (requirement) Your team will need training before the push. At a minimum, this training should help team members understand the intent and logistics of the push itself. Some members might also require updated security training and training in security or analysis techniques that are specific to the software that is undergoing the push. The training should have two components—the push logistics, delivered by a senior member of the team conducting the push, and technical and role-specific security training.

## Phase Four: Verification > Security Push > Push Duration

- **[R-0438]** (requirement) The amount of time, energy, and team-wide focus that a security push requires differs depending on the status of the code base and the amount of attention the team has given to security earlier in development. A security push requires less time if your team has:
  - Rigorously kept all threat models up to date.
  - Actively and completely subjected those threat models to penetrations testing.
  - Accurately tracked and documented attack surfaces and any changes made to them.
  - Completed security code reviews for all high-severity code (see discussion later in this section for details about how severity is assessed).
  - Identified and documented development and testing contacts for all code released with the product.
  - Rigorously brought all legacy code up to current security standards.
  - Validated the security documentation plan.

- **[R-0439]** (recommendation) The duration of a security push is determined by the amount of code that needs to be reviewed for security. Try to conduct security code reviews throughout development, after the code is fairly stable. If you try to condense too many code reviews into too brief a time period, the quality of code reviews suffers. In general, a security push is measured in weeks, not days. You should aim to complete the push in three weeks and extend the time as necessary.

## Phase Five: Release

- **[R-0440]** (requirement) The Release phase is when you ready your software for public consumption and, perhaps more importantly, you ready yourself and your team for what happens once your software is in the hands of the user. One of the core concepts in the Release phase is planning—mapping out a plan of action, should any security or privacy vulnerabilities be discovered in your release—and this carries over to post-release, as well, in terms of response execution. To this end, a Final Security Review and privacy review is required prior to release.

## Phase Five: Release > Public Release Privacy Review

- **[R-0441]** (requirement) Although privacy requirements must be addressed before any public release of code, security requirements need not be addressed before public release. However, you must complete a Final Security Review before final release.

## Phase Five: Release > Planning

- **[R-0442]** (requirement) Any software can be released with unknown security issues or privacy issues, despite best efforts and intentions. Even programs with no known vulnerabilities at the time of release can be subject to new threats that emerge and might require action. Similarly, privacy advocates might raise privacy concerns after release. You must prepare before release to respond to potential security and privacy incidents. With proper planning, you should be able to address many of the incidents that could occur in the course of normal business operations.

- **[R-0443]** (requirement) Your team must be prepared for a zero-day exploit of a vulnerability—one for which a security update does not exist. Your team must also be prepared to respond to a software security emergency. If you create an emergency response plan before release, you will save time, money, and frustration when an emergency response is required for either security or privacy reasons.

## Phase Five: Release > Final Security Review and Privacy Review

- **[R-0444]** (recommendation) As the end of your software development project approaches, you need to be sure that the software is secure enough to ship. The Final Security Review (FSR) helps determine this. The security team assigned to the project should perform the FSR with help from the product team to ensure that the software complies with all SDL requirements and any additional security requirements identified by the security team (such as penetration testing or additional fuzz testing).

- **[R-0445]** (recommendation) It is important to schedule the FSR carefully—that is, you need to allow enough time to address any serious issues that might be found during the review. You also need to allow enough time for a thorough analysis; insufficient time could cause you to make significant changes after the FSR is completed.

## Phase Five: Release > Release to Manufacturing/Release to Web

- **[R-0446]** (requirement) Software release to manufacturing (RTM) or release to web (RTW) is conditional to completion of the Security Development Lifecycle process as defined in this document. The security advisor assigned to the release must certify that your team has satisfied security requirements. Similarly, for all products that have at least one component with a privacy impact rating of P1, your privacy advisor must certify that your team has satisfied the privacy requirements before the software can be shipped.

## Introduction

- **[R-0447]** (requirement) If Agile practitioners are to adopt the SDL, two changes must be made. First, SDL additions to Agile processes must be lean. This means that for each feature, the team does just enough SDL work for that feature before working on the next one. Second, the development phases (design, implementation, verification, and release) associated with the classic waterfall-style SDL do not apply to Agile and must be reorganized into a more Agile-friendly format. To this end, the SDL team at Microsoft developed and put into practice a streamlined approach that melds agile methods and security—the Security Development Lifecycle for Agile Development (SDL-Agile).

## SDL-Agile Requirements > Bucket Requirements

- **[R-0448]** (recommendation) It is left to the product teams to determine which tasks from each bucket that they would like to address in any given sprint. The SDL-Agile does not mandate any type of round-robin or other task prioritization for these requirements. If your team determines that they are best served by completing file fuzzing requirements every other sprint but that SOAP fuzzing only needs to be performed every 10 sprints, that’s acceptable.

## SDL-Agile Requirements > One-Time Requirements

- **[R-0449]** (recommendation) There are some SDL requirements that need to be met when you first start a new project with SDL-Agile or when you first start using SDL-Agile with an existing project. These are generally once-per-project tasks that won’t need to be repeated after they’re complete. This is the final category of SDL-Agile requirements, called the one-time requirements.

## SDL-Agile Requirements > Constraints

- **[R-0450]** (recommendation) Although SDL-Agile was designed for teams with short release cycles, teams with longer release cycles are still eligible to use the SDL-Agile process. However, they may find that they are actually performing more security work than if they had used the classic, waterfall-based SDL. Requirements that a team only needs to complete once in classic SDL may need to be met five or six (or more) times in SDL-Agile over the course of a long project. However, this is not necessarily a bad thing and may help the team to create a more secure product.

## Applying SDL Tasks to Sprints > Security Education

- **[R-0451]** (requirement) Each member of a project team must complete at least one security training course every year. If more than 20 percent of the project members are out of compliance with this non-negotiable requirement, the requirement is failed (and consequently so is the sprint, and the product is not allowed to release). Consult your sprint leader for a list of courses that satisfy SDL training requirements. You can also consult the SDL Pro Network for training courses and recommendations.

- **[R-0452]** (recommendation) Additionally, in the interests of staying lean, engineers and testers performing security-related tasks or SDL-related tasks should acquire relevant security knowledge prior to performing the tasks on the sprint. In this case, relevant is defined as security concepts that are pertinent to the features developed or tested during the sprint. Examples include:

- **[R-0453]** (recommendation) Acquiring security knowledge could be as simple as reading appropriate chapters in a book or watching an online training class. If someone on the team wants to adopt the role of “security champion” or security expert for their team, they should attend broader and deeper security education as part of their normal ongoing education. Having a security expert close by is advantageous to the team and, more importantly, to the customer.

## Applying SDL Tasks to Sprints > Tooling and Automation

- **[R-0454]** (requirement) Tools that automate security-related tasks are critical to a successful security process because the more you can automate the work necessary to meet requirements, the easier security becomes. Also, tools help reduce some of the development effort required of the developers by shifting it onto the tools. When security is involved, tools are not a replacement for humans, but tools do offer scalability—a tool can scan lots of code or check binaries without getting tired. Keep in mind, however, that simply running tools does not make a software product secure.

- **[R-0455]** (requirement) SDL-Agile requires the following tools to be run at least once per sprint and recommends that they be run daily or as part of the build and check-in process:

- **[R-0456]** (requirement) Fix issues identified by static code analysis tools for unmanaged code. Use the currently required (or later) version of /analyze compiler option in Microsoft Visual Studio with the C and C++ compiler for native code for the target platforms and fix all required minimum (Min SDL) warnings. (Note: Also called /analyze in Microsoft Visual Studio.)

## Applying SDL Tasks to Sprints > Threat Modeling: The Cornerstone of the SDL

- **[R-0457]** (requirement) At some point, the major SDL artifact—the threat model—must be used as a baseline for the product. Whether this is a new product or a product already under development, a threat model must be built as part of the sprint design work. Like many good Agile practices, the threat model process should be time-boxed and limited to only the parts of the product that currently exist or are in development.

- **[R-0458]** (recommendation) During each sprint, the threat model should be updated to represent any new features or functionality added during that sprint. The threat model should also be updated to represent any significant design changes, even if the functionality stays the same.

## Applying SDL Tasks to Sprints > Threat Modeling: The Cornerstone of the SDL > SDL Threat Modeling Tool

- **[R-0459]** (descriptive) While not officially required as part of the SDL (either SDL-Agile or SDL-Classic), many internal Microsoft teams use the SDL Threat Modeling Tool with great success. The SDL Threat Modeling Tool is specifically designed to be used by developers and architects who may not necessarily have security expertise. A full review of the SDL Threat Modeling Tool is beyond the scope of this paper, but you can read more about it (and download it for free) at the Microsoft SDL Threat Modeling Tool website.

## Applying SDL Tasks to Sprints > Threat Modeling: The Cornerstone of the SDL > Starting a Threat Model for an Existing Project

- **[R-0460]** (recommendation) If an Agile team adopts the SDL-Agile as outlined in this document while a product is already in development, a threat model needs to be built for the current product, but it is imperative that the team remains lean. A minimal, but useful, threat model can be built by analyzing high-risk entry points and data in the system. At a minimum, the following should be identified and threat models built around the entry points and data:

## Applying SDL Tasks to Sprints > Threat Modeling: The Cornerstone of the SDL > Continuing Threat Modeling

- **[R-0461]** (requirement) Threat modeling is one of the every-sprint SDL requirements for SDL-Agile. Unlike most of the other every-sprint requirements, threat modeling is not easily automated and can require significant team effort. However, in keeping with the spirit of agile development, only new features or changes being implemented in the current sprint need to be threat modeled in the current sprint. This helps to minimize the amount of developer time required while still providing all the benefits of threat modeling.

## Applying SDL Tasks to Sprints > Fuzz Testing

- **[R-0462]** (recommendation) Fuzz testing is a brutally effective security testing technique, especially if the team has never used fuzz testing on the product. The threat model should determine what portions of the application to fuzz test. If no threat model exists, the initial list should include high-risk items, such as those defined in Appendix S: SDL-Agile High-Risk Code.

- **[R-0463]** (recommendation) After this list is complete, the relative exposure of each entry point should be determined, and this drives the order in which entry points are fuzzed. For example, remotely accessible or unauthenticated endpoints are higher risk than local-only or authenticated endpoints.

- **[R-0464]** (recommendation) The beauty of fuzz testing is that once a computer or group of computers is configured to fuzz the application, it can be left running, and only crashes need to be analyzed. If there are no crashes from the outset of fuzz testing, the fuzz test is probably inadequate, and a new task should be created to analyze why the fuzz tests are failing and make the necessary adjustments.

## Applying SDL Tasks to Sprints > Using a Spike to Analyze and Measure Unsecure Code in Bug Dense and “At-Risk” Code

- **[R-0465]** (recommendation) A critical indicator of potential security bug density is the age of the code. Based on the experiences of Microsoft developers and testers, the older the code, the higher the number of security bugs found in the code. If your project has a large amount of legacy code or risky code (see Appendix S: SDL-Agile High-Risk Code), you should locate as many vulnerabilities in this code as possible. This is achieved through a spike. A spike is a time-boxed “side project” with a well-defined goal (in this case, to find security bugs). You can think of this spike as a mini security push. The goal of the security push at Microsoft is to bring risky code up to date in a short amount of time relative to the project duration.

- **[R-0466]** (recommendation) Note that the security push doesn't propose fixing the bugs yet but rather analyzing them to determine how bad they are. If a lot of security bugs are found in code with network connections or in code that handles sensitive data, these bugs should not only be fixed soon, but also another spike should be set up to comb the code more thoroughly for more security bugs.

- **[R-0467]** (recommendation) All appropriate analysis tools available to the team should be run during the spike, and all bugs triaged and logged. Critical security bugs, such as a buffer overrun in a networked component or a SQL injection vulnerability, should be treated as high-priority unplanned items.

## Applying SDL Tasks to Sprints > Exceptions

- **[R-0468]** (descriptive) For example, say a team requests an exception for a requirement normally classified as Moderate, which requires manager approval. If they request the exception only for a very short period of time, say two weeks, the security advisor may drop the severity to Low, which requires only approval from the team’s security champion. On the other hand, if the team requests the full six months, the security advisor may increase the severity to Important and require signoff from senior management due to the increased risk.

## Security Development Lifecycle for Line-of-Business Applications

- **[R-0469]** (requirement) The following table highlights LOB-specific tasks for each phase of the SDL. These tasks are in addition to those outlined in the main SDL portion of this document. Each task in the table is discussed by phase in the remainder of the LOB section. Note that the Response phase is not included in the table because there are no additional tasks required for that phase beyond what is discussed in the main SDL.

- **[R-0470]** (recommendation) It is important to note that organizations should adapt rather than adopt the Microsoft SDL-LOB process. Organizations are unique and should expect and plan for differences in resources, executive support, and security expertise.

## Pre-SDL Requirements: Security Training for LOB

- **[R-0471]** (recommendation) In this section and in the remainder of the SDL-LOB, only supplements to the original SDL are highlighted. To create a complete security plan for LOB applications, you should consult each section of the main SDL and the supplemental information contained in each phase of the SDL-LOB.

- **[R-0472]** (recommendation) In addition to the basic concepts outlined in the main SDL, LOB training should include the following additional topics:

## Phase One: Requirements for LOB > Risk Assessment

- **[R-0473]** (requirement) When an application team proposes a new application or updates to an existing application, a risk assessment is completed. Application teams understand they must complete this step as a prerequisite for installing the application in a supported production environment. This risk assessment produces repeatable guidance on the type of oversight the project will receive in the SDL-LOB process.

## Phase One: Requirements for LOB > Risk Assessment > Mapping Risk to Security SME Service Levels

- **[R-0474]** (recommendation) The output of the risk assessment dictates the degree of oversight from a security SME. Questions in the assessment are weighted together into an overall “score,” while questions may dictate a review regardless of the overall “score.” The sample questionnaire provided gives some guidance in this respect, but you will need to tailor it for your specific business and customer needs. This approach ensures consistency and reputability combined with flexibility. Experience has shown that a “one-size-fits-all” approach is not effective.

- **[R-0475]** (requirement) For example, based on application risk (High/Medium/Low), applications are serviced accordingly during various phases of the development. Note that all applications require oversight; however, application teams are still responsible for compliance with your implementation of the SDL-LOB (including appropriate requirements and recommendations from main SDL described earlier in this document).

- **[R-0476]** (recommendation) Threat model. The application team needs to create (or update) a threat model for the application. Threat modeling is, in some sense, a discovery process wherein you look at your application through a lens of security and/or privacy. The application team should own the creation of the threat model in consultation with a security/privacy SME.
  Note: Threat models are recommended, but compliance is not typically enforced for low and sometimes medium risk applications.

- **[R-0477]** (recommendation) Code review (white box). Conducted to determine how many code vulnerabilities exist. Severity of findings is based on deviation from policy, standards, and best practices. The review should balance a line-by-line code inspection against prioritizing sensitive parts of the application, such as authentication, authorization, handling of sensitive data, and avoiding common security vulnerabilities, such as poor input validation, SQL injection, and failure to properly encode web output.

- **[R-0478]** (requirement) In addition, the code review should verify compliance with security/privacy standards and policies. Violations of standards and policies are viewed as must-fix, Critical vulnerabilities.

## Phase Two: Design for LOB > Threat Modeling and Design Review

- **[R-0479]** (requirement) Threat modeling and conducting design reviews is a systematic process that is used to identify threats and vulnerabilities in the application. You must complete threat modeling during project design. A team cannot build a secure application unless it understands the assets the project is trying to protect, the threats and vulnerabilities introduced by the project, and details of how the project will mitigate those threats.

## Phase Two: Design for LOB > Threat Modeling and Design Review > Choosing the Right Threat Modeling Tool for LOB Applications

- **[R-0480]** (recommendation) Provide a consistent methodology for objectively identifying and evaluating threats to software applications. In order for a threat modeling methodology to be practical, it needs to be consistently reproducible. Given the same input to the methodology, the output should remain unchanged.

- **[R-0481]** (recommendation) Empower the business to manage risk. Security is all about risk management, and risk management essentially entails identification of risks and how those risks are managed. The most common forms of risk management are acceptance, avoidance, transference, and reduction. However, before business groups can make decisions on their risk management approach, they need to be empowered with the right information to make the most justifiable decision in terms of business needs.

- **[R-0482]** (recommendation) Create awareness between teams of security dependencies and security assumptions. The creation of a LOB application goes through many phases of a development life cycle. Some examples are requirements, design, development, verification, and deployment. Just as the business requirements need to be maintained during the entire development life cycle, so do the identified countermeasures. By having a standard documentation of a security strategy, it enables the application groups to create and maintain awareness between various teams (for example, the design team or the test team) of the security dependencies and security assumptions made during various phases of the development life cycle that will lead to the realization of the identified countermeasures.

## Phase Two: Design for LOB > Threat Modeling and Design Review > Design Reviews

- **[R-0483]** (requirement) An architecture and design review helps you validate the security-related design features of your application before you start the development phase. This allows you to identify and fix potential vulnerabilities before they can be exploited and before the fix requires a substantial reengineering effort. Essentially this results in a reduced attack surface exposed by applications, thus increasing the security of the user and the system.

## Phase Three: Implementation for LOB > Internal Review > Incorporate Security Checklist and Review Policies

- **[R-0484]** (requirement) Tools. A mix of freeware, third-party tools to perform code analysis, or penetration testing can be employed during this phase. The challenge tools present is that they often require security expertise to filter false positives or to maximize the results from the tool. This is especially true for more sophisticated toolsets.

- **[R-0485]** (requirement) Security checklist. Development teams must review available information resources to adopt appropriate coding techniques and methodologies. A coding checklist that describes the minimal requirements for any checked-in code for ASP.NET version 2.0 applications. See checklist items from the Security Checklist Index from Microsoft Patterns and Practices.

- **[R-0486]** (recommendation) Review and develop deployment guidelines. The application team needs to answer this question: How will the application be securely deployed removing artifacts, test code, and settings that are needed during development and testing? For example, web.config files in ASP.NET often contain the following statement to facilitate debugging during this phase.

- **[R-0487]** (recommendation) However, it needs to be explicitly turned off in production, otherwise a malicious user may be able to take advantage of these settings to profile the application that could lead to an actual exploit. Whether there is a manual or automated process, the development team needs to work with the owners of the production servers to ensure that inappropriate code, artifacts, and settings are not actually used in production.

- **[R-0488]** (requirement) Encrypt all secrets in text format whether in source code, web.config, machine.config, or any file. Unencrypted, these secrets are prone to discovery and can easily allow a partially compromised application or system to be further exploited, thus increasing the impact of the exploit. All passwords, connection strings with passwords, encryption keys, credentials, and other secrets are stored encrypted when stored in configuration files. Secrets must never be in source code encrypted or plaintext.

- **[R-0489]** (requirement) Input validation. Input validation must be applied at all identified entry points (including form fields, QueryStrings, cookies, HTTP headers, and web service parameters). It is a security practice never to trust user input data without first confirming its authenticity. Verify that all inputs to the application are validated on the server side before consuming. String data is validated for length and format. Where possible use regular expressions to validate format. Make sure numeric data is validated for range (upper and lower bound) and type (signed vs. unsigned). String data should preferably use inclusion list (known, valid, and safe input) rather than exclusion list (rejecting known malicious or dangerous input).

- **[R-0490]** (recommendation) Line of Business Secure Code Review. High-risk items (Pri 1) that are considered the most sensitive or important for security should be reviewed in depth at the earliest opportunity. Resolve any Severity 1 bugs or bugs that are, per the Code Review Checklist, a standards violation. If the bug cannot be fixed, document the underlying infrastructure or framework limitation. Resolve all bugs that are moderate or higher based on the SDL Bug Bar. Development owners for all source code and testing owners for all binaries have been identified, documented, and archived—for example, in the source tracking system used by the product. All source code is assessed and assigned a priority—Pri 1, Pri 2, and Pri 3. This information is recorded in a document or spreadsheet and is archived in a tracking bug for ease-of-discovery.

- **[R-0491]** (requirement) Secure sensitive data-at-rest. High business impact (HBI) data needs to be encrypted "at-rest," that is, when located in your database server or other data stores. Ensuring that HBI data is encrypted with appropriate encryption algorithms and key strength when at-rest in a data-store, and that this encryption takes place within the data store. Where possible, leveraging existing operating system or server functionality to manage encryption rather than building such functionality from scratch. Be sure that that this encryption actually secures sensitive data. For SQL Server, use SQL Server Transparent Data Encryption to encrypt the entire database. Note that this approach still requires good management of any keys used for encryption. Use T-SQL functions and SQL Server infrastructure to encrypt specific data elements.

- **[R-0492]** (recommendation) Secure sensitive data-in-transit. Encryption should be used for any HBI data that is transmitted over wired or wireless connections on the corporate network (corpnet) or is extranet/Internet-facing. Encryption should be used for any medium business impact (MBI) information in transit via wireless or wired connections when in-transit across the Internet.

## Phase Four: Verification for LOB > Pre-Production Assessment

- **[R-0493]** (recommendation) Further, this phase should be conducted with a mix of manual process and automated tools. Manual reviews may need to be time constrained and focus on high-risk features. Automated tools can reduce overhead, but should not be relied upon exclusively.

## Phase Four: Verification for LOB > Pre-Production Assessment > Compliance

- **[R-0494]** (requirement) In response to exception requests, security teams gather all pertinent data points, such as technical details, business impact description, interim mitigation, and other exception information, and provide a development team’s upper management with these details in the form of an exception form. Upper management can then approve the exception request and accept identified risks for a small period of time, or they reject the exception request and require the business group to mitigate the identified risks. It is important that a specific business owner explicitly assume the risk posed by unmitigated Critical and Important bugs.

- **[R-0495]** (recommendation) Note: Critical and Important bugs may exist due to a technological or infrastructure limitation that cannot be mitigated in the current release. An exception should be created in to track the issue until such time as the limitation no longer exists.

## Phase Five: Release for LOB

- **[R-0496]** (recommendation) After deployment, several activities need to occur, including regular verification of patch management, compliance, network and host scanning, and responding to any incremental releases for hotfixes and service packs. For the SDL-LOB, these tasks are associated with the post-production assessment.

## Appendix B: Security Definitions for Vulnerability Work Item Tracking

- **[R-0497]** (recommendation) It is critical for project teams to specify and maintain a work item tracking system that allows for creation, triage, assignment, tracking, remediation, and reporting of software vulnerabilities. Optimally, work item tracking should also include the ability to track security and privacy issues by cause and effect of the security bugs. The work item tracking system should have access controls in place to ensure that changes to information in the system (whether malicious or accidental) can be tracked appropriately.

## Appendix D: Firewall Rules and Requirements

- **[R-0498]** (recommendation) A firewall is a key part of any organization’s protection strategy. You should have a consistent policy to manage the settings of your organization’s firewall to ensure that users are not exposed to unknown or unnecessary risk from programs that receive unsolicited data over the network. Use the information in this appendix to help draft your organization's firewall policy.

## Appendix D: Firewall Rules and Requirements > Firewall Rules and Requirements

- **[R-0499]** (requirement) In addition to the port- and program-specific requirements for Windows XP SP2 listed earlier, the following requirements must be met for Windows Vista and Windows Server 2008.

## Appendix D: Firewall Rules and Requirements > Application Quality

- **[R-0500]** (requirement) Programs, applications, services, or other components that wish to receive unsolicited traffic must:
  - Produce an independent threat model for the service which identifies each entry point explicitly, including services that are “multiplexed” behind a common port.
  - Meet the network fuzzing requirements.

## Appendix D: Firewall Rules and Requirements > Least Privilege

- **[R-0501]** (requirement) Firewall rules must adhere to the principle of least privilege by:
  - Scoping the rule to “local subnet” or tighter when practical.
  - Scoping the rule to only the network profile(s) where the feature is likely to be used. For example, if it is an enterprise feature, then you should scope the rule to domain, private profiles. Unless you expect your feature to be used in a public place like a WiFi hotspot, you should not scope the rule to the public profile.
  - Unless your feature requires NAT traversal using transition tunnel technologies, do not set the “Edge” traversal flag.
  - Limiting the privileges of the service that use the port to Network Service or more restrictive when practical. When not practical, the threat model should explicitly call out the reasons why.

- **[R-0502]** (requirement) If services must run with privileges greater than Network Service, it is recommended that the services be split into “privileged” and “non-privileged” components such that only the code that requires higher privileges receives them, and other code is addressed through some IPC mechanism. The end result being that the non-privileged service is the one that receives the traffic.

## Appendix D: Firewall Rules and Requirements > Informed Consent UI

- **[R-0503]** (requirement) This policy addresses user interface issues, but nothing in the policy should be interpreted to specify a particular user interface. For example, when it says “The user is informed and acknowledges the open port,” it does not imply that there must be a dialog that tells the user port 123 has been opened. The requirement is that the user is informed of the change in some explicit fashion via the UI (not an entry in a log file), and that the details are available for users who want to know.

## Appendix F: SDL Requirement: No Executable Pages > Special Cases

- **[R-0504]** (recommendation) All executables (.EXE) marked as /NXCOMPAT are able to take advantage of Data Execution Protection. Dynamic-link libraries (.DLL files) or other code called by executables (such as COM objects) do not gain direct security benefits with /NXCOMPAT but need to coordinate enabling /DEP support with any executable files that might call them. Any EXE with /NXCOMPAT enabled that loads other code without /NXCOMPAT enabled may have the process fail unexpectedly unless the EXE and all of the other code that it calls (such as DLLs or COM objects) have been thoroughly tested with DEP enabled (linked with /NXCOMPAT option).

## Appendix I: SDL Requirement: Heap Manager Fail Fast Setting > Goals and Justification

- **[R-0505]** (requirement) The first benefit applies to development. With this requirement in place, problematic code is more likely to be found because the failure is immediate. Think of it as an “assert” on heap overrun. However, the code that performs heap-based memory allocation and manipulation must be tested correctly. The best method to find this class of vulnerability is through fuzz testing.

## Appendix J: SDL Requirement: Application Verifier > Application Verifier Usage Scenarios

- **[R-0506]** (recommendation) Application Verifier (available in Visual Studio and as a download) cannot be enabled for a running process. You need to make settings as described in this appendix and then start the application. The settings are persistent until explicitly deleted. Therefore, an application always starts with AppVerifier enabled, regardless of how many times you launch it

## Appendix J: SDL Requirement: Application Verifier > Testing with Application Verifier

- **[R-0507]** (requirement) If you are testing a dynamic-link library (DLL), you must enable the verifier for the test .exe that is exercising the DLL.

- **[R-0508]** (recommendation) Analyze any debugger break that you encounter. Debugger breaks signify bugs found by the verifier, and you need to understand and fix them.

## Appendix J: SDL Requirement: Application Verifier > Testing with Application Verifier and Fault Injection

- **[R-0509]** (recommendation) The expectation for this scenario is that the application does not break into debugger mode. Not breaking into debugger mode means there are no errors that need to be addressed.

- **[R-0510]** (recommendation) Analyze any debugger break that you encounter. Debugger breaks signify bugs found by the verifier, and you need to understand and fix them.
