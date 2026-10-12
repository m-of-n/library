---
schema: "library-distilled/v1"
id: uk-software-security-code-of-practice-normative
record: uk-software-security-code-of-practice
type: normative
updated: "2026-10-02"
---

# Software Security Code of Practice — normative text

Verbatim, in the source's structure. Three sources, each with its own locators:

- **Code** — DSIT *Software Security Code of Practice*, May 2025 (PDF, 9 pp.; gov.uk HTML identical in content). Locator `Code p.N`.
- **APC** — NCSC *Software Security Code of Practice – Assurance Principles and Claims (APCs)* v1.0. Locator `APC`.
- **IG** — NCSC *Software Security Code of Practice – Implementation Guidance* v1.0 (7-page web collection). Locator `IG page N`.

Requirement ids in brackets refer to `requirements.yaml` (`uk-software-security-code-of-practice#<id>`). Lower-case modals throughout; the Code's own definition (Code p.9, Table 3, "Shall"): *"In this Code of Practice, “shall” represents a requirement of the Code of Practice. This language reflects the language used in government standards, which will facilitate assurance against this Code of Practice."*

Rendering differences between the PDF and the gov.uk HTML of the Code (content otherwise identical): PDF "Divided into 4 themes" / HTML "Divided into four themes"; PDF "should be reasonably expected" / HTML "should reasonably be expected" (Audience and scope); PDF glossary "Vulnerability disclosure process" ends "(see implementation guidance for more detail)", the HTML omits the parenthesis. `requirements.yaml` quotes whichever rendering is linear (the PDF's two-column tables interleave lines under pdftotext).

## Part A — The Code (DSIT)

### Code p.6 — The Software Security Code of Practice

> The Software Security Code of Practice contains 14 principles split across 4 themes. A Senior Responsible Owner should be appointed at senior leadership level to hold accountability for the principles being followed within their organisations. [C-SRO]

#### 1. Secure design and development

> These principles ensure that the software is appropriately secure when provided.
>
> The Senior Responsible Owner in vendor organisations shall gain assurance that their organisation achieves the following in relation to any software or software services sold by their organisation:
>
> **1.1** Follow an established secure development framework. [1.1]
>
> **1.2** Understand the composition of the software and assess risks linked to the ingestion and maintenance of third-party components throughout the development lifecycle. [1.2]
>
> **1.3** Have a clear process for testing software and software updates before distribution. [1.3]
>
> **1.4** Follow secure by design and secure by default principles throughout the development lifecycle of the software. [1.4]

#### 2. Build environment security

> These principles ensure that the appropriate steps are taken to minimise the risk of build environments becoming compromised and protect the integrity and quality of the software.
>
> The Senior Responsible Owner in vendor organisations shall gain assurance that their organisation achieves the following in relation to any software or software services sold by their organisation:
>
> **2.1** Protect the build environment against unauthorised access. [2.1]
>
> **2.2** Control and log changes to the build environment. [2.2]

#### 3. Secure deployment and maintenance

> These principles ensure that the software remains secure throughout its lifetime, to minimise the likelihood and impact of vulnerabilities.
>
> The Senior Responsible Owner in vendor organisations shall gain assurance that their organisation achieves the following in relation to any software or software services sold by their organisation:
>
> **3.1** Distribute software securely to customers. [3.1]
>
> **3.2** Implement and publish an effective vulnerability disclosure process. [3.2]
>
> **3.3** Have processes and documentation in place for proactively detecting, prioritising and managing vulnerabilities in software components. [3.3]
>
> **3.4** Report vulnerabilities to relevant parties where appropriate. [3.4]
>
> **3.5** Provide timely security updates, patches and notifications to customers. [3.5]

#### 4. Communication with customers

> These principles ensure that vendor organisations provide sufficient information to customers to enable effective risk and incident management.
>
> The Senior Responsible Owner in vendor organisations shall gain assurance that their organisation achieves the following in relation to any software or software services sold by their organisation:
>
> **4.1** Provide information to the customer specifying the level of support and maintenance provided for the software being sold. [4.1]
>
> **4.2** Provides at least 1 year’s notice to customers of when the software will no longer be supported or maintained by the vendor. [4.2]
>
> **4.3** Make information available to customers about notable incidents that may cause significant impact to customer organisations. [4.3]

### Other normative statements in the Code

| id | locator | text |
|---|---|---|
| C-SRO | Code p.6, 'The Software Security Code of Practice' (intro); also Table 2 'Senior Leaders in Software Vendor organisations' | A Senior Responsible Owner should be appointed at senior leadership level to hold accountability for the principles being followed within their organisations. |
| C-SRO-T2 | Code p.4, Table 2, row 'Senior Leaders in Software Vendor organisations' | A Senior Responsible Owner (SRO) should be appointed at the top-tier leadership level of an organisation. |
| C-SKILLS | Code p.5, 'Skills' | Senior leaders should be accountable for ensuring that the organisation fulfils the requirements of this Code of Practice. |
| C-RESELLER | Code p.3, Table 1, row 'Software resellers' | However, where possible, resellers should encourage those developing the software they distribute to follow the principles of this Code. |
| C-OSS | Code p.3, Table 1, row 'Open-source developers and maintainers' | Any risks associated with open-source code must be managed by end-users or proprietary developers using open-source code in their software. |
| C-SCOPE-GOV | Code p.2, 'Background' | Organisations deemed in scope should also adhere to other relevant security measures, and particularly the Cyber Governance Code of Practice, which sets the baseline expectations for all organisations using digital technologies. |
| C-SCOPE-OTHER | Code p.2, 'Background' | Organisations deemed in scope should also consider whether they should adhere with further technology-specific codes of practice, such as those relating to A I and App Stores, depending on their business function. |
| C-GLOSS-BUILDENV | Code pp.7-9, Table 3 'Glossary of key terms', term 'Build Environment' | This should be logically or physically separate from areas where code is written and tested. |
| C-GLOSS-SBD | Code pp.7-9, Table 3 'Glossary of key terms', term 'Secure by Design' | Software vendors should perform a risk assessment to identify and enumerate prevalent cyber threats to critical systems and then include protections in the blueprints that account for the evolving cyber threat landscape. |
| C-GLOSS-SDF | Code pp.7-9, Table 3 'Glossary of key terms', term 'Secure development framework' | An established secure development framework should include the following topics as a minimum: threat modelling, secure coding practices, requirements capture, governance and roles, test strategy, data management, and configuration management (see implementation guidance for further detail). |
| C-GLOSS-VDP | Code pp.7-9, Table 3 'Glossary of key terms', term 'Vulnerability disclosure process' | This should be backed up by a vulnerability disclosure policy which details how reports should be handled internally. |

### Code p.3 — Applicability by stakeholder group (Table 1, Guidance column, verbatim excerpts)

- Software developers and distributors: "Software developers and distributors would be expected to follow all principles of this Code of Practice."
- Software resellers: "For software resellers, only principles 3 to 4 will fall within the scope of a reseller’s responsibility."
- Software developers only: "For software developers only, principles 1 and 2 will be relevant, as well as principle 3 where it is in the scope of responsibility of the organisation/ individual."
- Open-source developers and maintainers: "For the purpose of this Software Security Code of Practice, open-source developers and maintainers are not considered the primary audience."

### Code pp.4–5 — Assurance and self-assessment (verbatim)

> The UK Government is providing a self-assessment form to accompany this Code of Practice. This form can be used for internal compliance monitoring or can be shared with customers to provide software security assurance.
>
> The assurance approach for this Code of Practice has been developed to follow the NCSC’s Principles Based Assurance approach. This breaks the Code of Practice down into a set of Assurance Principles and Claims (APCs). Using the Code of Practice as the core principles, the APCs derive a set of ideal-scenario claims that, if met, mean the software vendor is achieving the principles of the Software Security Code of Practice. The kind of evidence provided may vary depending on the specific processes used by each organisation, which provides flexibility in how organisations can demonstrate compliance using the form provided.
>
> The UK Government is currently working to develop a certification scheme based on this compliance process. Further information about this certification process will be shared in due course.

## Part B — Per principle: Code text, APC claims (conformance criteria), Implementation Guidance

APC "About this document": *"This document considers each principle within the four themes in the Code, and breaks them down into a set of individual claims that describe a way to fully meet the associated principle. If all these claims are well-evidenced, then a vendor can claim in good faith that they are meeting the principle."* Evidence types: *"The type of evidence can vary but examples include document inspection, interviewing individuals, or auditing test plans and results."*

> Vendors requiring independent audit of compliance with the code should contact any NCSC-approved cyber resilience test facility. [APC-ABOUT-01]

— APC v1.0, About this document, "Note that:" item 2 (added in the verify pass). The APC Appendix claims trees (SVG on the NCSC page, not in the PDF) are transcribed in `apc-claim-trees.yaml`.

### Principle 1.1 — Follow an established secure development framework.

*Theme 1: Secure design and development. Code p.6.*

**APC claims** (APC, Theme 1, Principle 1.1):

- [APC-1.1-01] The development framework used is documented.
- [APC-1.1-02] Developers are trained in the use of the framework and tools.
- [APC-1.1-03] Tools are maintained and updated.
- [APC-1.1-04] Items requiring configuration control are identified and version control is used.
- [APC-1.1-05] Requirements are captured and recorded.
- [APC-1.1-06] Software is designed for user need.

**Implementation guidance** (IG page 3 'Theme 1: Secure design and development', Principle 1.1):

- [IG-1.1-01] You should be able to demonstrate conformance to a secure development framework across your development and deployment activities.
- [IG-1.1-02] A good secure development framework should include the following topics as a minimum:
- [IG-1.1-03] A proactive approach to building security into software should incorporate people, processes and technology aspects.
- [IG-1.1-04] You may wish to publish a description of which development framework you are using, and which claims have been implemented.

*A good secure development framework should include the following topics as a minimum:*

- [IG-1.1-05] Threat modelling: techniques used to understand how the software might be attacked or fail in some other way.
- [IG-1.1-06] Requirements capture: understanding and recording security and user needs.
- [IG-1.1-07] Governance & roles: the approach to managing and mitigating risks associated with the organisation’s ability to develop and maintain secure-by-design digital technologies.
- [IG-1.1-08] Secure coding practices: best practices to prevent common vulnerabilities such as SQL injection and cross-site scripting.
- [IG-1.1-09] Test strategy: consistent approaches to verification that have sufficient rigour and coverage, including all products, updates and patches.
- [IG-1.1-10] Data management: understanding what data exists and how it should be appropriately protected throughout its life cycle.
- [IG-1.1-11] Configuration management: consistent approaches to tracking changes, implementing version control, and enabling reproducibility.

### Principle 1.2 — Understand the composition of the software and assess risks linked to the ingestion and maintenance of third-party components throughout the development lifecycle.

*Theme 1: Secure design and development. Code p.6.*

**APC claims** (APC, Theme 1, Principle 1.2):

- [APC-1.2-01] All third-party components are identified and documented.
- [APC-1.2-02] Integrity of third-party components and updates is verified.
- [APC-1.2-03] Each third-party component is tested before being first deployed.
- [APC-1.2-04] Third-party component updates are tested.
- [APC-1.2-05] Processes are in place to manage and deploy updates to third- party components.

**Implementation guidance** (IG page 3 'Theme 1: Secure design and development', Principle 1.2):

- [IG-1.2-01] As a software vendor, your first step should be to identify all the components used across all your software.
- [IG-1.2-02] This inventory should be used to ensure that all components are regularly checked for known vulnerabilities, and used for any incident management events that may occur.

*You should ensure that:*

- [IG-1.2-03] You identify who is responsible for selection and security of third-party supplied goods, and consider the security attributes (such as provenance of the software, frequency of updates, how many maintainers, and geographic location of contributors).
- [IG-1.2-04] You capture all the third-party software components, including compilers and build systems. Components may come from a supplier with whom you have a contractual relationship, or they may be Free Open-Source Software (FOSS). An inventory can take any format that suits the processes and culture of the organisation, such as a software bill of materials (SBOM).
- [IG-1.2-05] You share security requirements with your suppliers. Your inventory should be validated and regularly updated as needed.
- [IG-1.2-06] You have the ability to share your inventory with your customers in the best format, so that, in the event that it is appropriate to do so, they have a validated and up-to-date list of all the third-party components in your software for their own supply chain security needs.
- [IG-1.2-07] Each third-party component of the software is up to date when first integrated into the product, and then regularly checked for vulnerabilities for the lifespan of the product. Not all your components will be provided through a contractual arrangement by a supplier who provides you with confidence that they have supply chain security measures in place. Therefore regular testing of all your third-party components and dependencies needs to be in place. You should be able to demonstrate that adequate testing has been carried out on each component.
- [IG-1.2-08] You can prioritise and test if a new vulnerability or attack is discovered outside of your regular testing cadence, to minimise the risk of the vulnerability being exploited.
- [IG-1.2-09] You can manage and deploy updates to third-party components and libraries provided by suppliers, and carry out any remediation required if vulnerabilities that can be exploited are discovered. Responding to these instances, and effectively communicating with customers is as important as discovery. You should carry out any remediation required (for example developing and issuing updates and patches) in a timely way and report these to your customers.

### Principle 1.3 — Have a clear process for testing software and software updates before distribution.

*Theme 1: Secure design and development. Code p.6.*

**APC claims** (APC, Theme 1, Principle 1.3):

- [APC-1.3-01] A test plan exists that covers all requirements and third-party components.
- [APC-1.3-02] Execution of the test plan is automated and repeatable wherever possible.
- [APC-1.3-03] Defects identified during testing are addressed.

**Implementation guidance** (IG page 3 'Theme 1: Secure design and development', Principle 1.3):

- [IG-1.3-01] As a minimum, your testing approach should include:

*You should ensure that:*

- [IG-1.3-02] Your tests include all individual components of your software, as well as the final software package. Your process includes testing defined security and functional requirements. Baseline levels of code coverage should be achieved on all code that is checked in, before new code is committed. Missing components and stages of your development process could mean that you miss important places where vulnerabilities exist.
- [IG-1.3-03] The results of testing are documented, and all discovered anomalies and vulnerabilities should be analysed and addressed. Your test plan is regularly reviewed against all these aspects to ensure that it continues to provide you with the confidence you need in your software. When a security issue is found, consider writing a new test for it. If you are experiencing a high number of false positives, consider correcting or removing failing tests. Consider testing your test regime on code which you know contains security flaws, so you can check it is functioning correctly.
- [IG-1.3-04] You test regularly; the more frequently you can test your code, the more confidence you can have in its security. Regular security testing does not have to get in the way of continuous delivery; it should take place throughout the life cycle of your software, not just in the development phase. Automating security testing where possible will provide you with easily repeatable, scalable security measures. Skilled testers can then concentrate on finding subtle and uncommon weaknesses.
- [IG-1.3-05] Your testing regime employs a range of different approaches that verify different aspects of the development life cycle. As a minimum, your testing approach should include:

*As a minimum, your testing approach should include:*

- [IG-1.3-06] Static & Dynamic Analysis: automated testing carried out on all code prior to check-in and for each release using a standard set of company-approved tools.
- [IG-1.3-07] Peer/code review: having two or more people review code to check its quality and security. This is a collaborative exercise that is general good practice as it promotes clean and maintainable code and encourages knowledge sharing.
- [IG-1.3-08] Unit testing: testing which focuses on individual units or components of software. This should be used to check that each unit is operating as it is intended before it is integrated into the whole system.
- [IG-1.3-09] Integration testing: testing which focuses on the whole system of the software once components have been brought together. It will look for unintended consequences and employ techniques such as ‘fuzzing’.
- [IG-1.3-10] Point-in-time assessments: Manual testing (such as ‘penetration testing’ or ‘software security assessment’) which is relatively slow and resource intensive. However it does allow security specialists to use their ingenuity in ways that aren’t possible for other types of testing.

### Principle 1.4 — Follow secure by design and secure by default principles throughout the development lifecycle of the software.

*Theme 1: Secure design and development. Code p.6.*

**APC claims** (APC, Theme 1, Principle 1.4):

- [APC-1.4-01] Techniques to understand how the software might be exploited (threat modelling) have been used in the design of the software.
- [APC-1.4-02] Multi-factor authentication for privileged users of the software is enforced.
- [APC-1.4-03] Default (and persistent) passwords are not used.
- [APC-1.4-04] Data input to the software is validated.
- [APC-1.4-05] Credentials and sensitive data are securely stored.

**Implementation guidance** (IG page 3 'Theme 1: Secure design and development', Principle 1.4):


*You should ensure that:*

- [IG-1.4-01] A structured process, such as threat modelling, should consider security threats from an adversarial perspective. By understanding what might go wrong, early in the development cycle, these aspects can be given focus and addressed.
- [IG-1.4-02] You mandate strong authentication such as multi-factor authentication (MFA) for privileged users. Your software should make phishing-resistant MFA opt-out (rather than opt-in) for privileged users. It should be easy for users of your software to set up MFA. Your choice of extra factor should be made based on the context and user experience of your software. We recommend choosing the strongest factor available as per the NCSC guidance.
- [IG-1.4-03] You change any default passwords in your toolset, following best practice. Administrators change or set up their own (strong) password during installation and configuration (or even better, other strong forms of authentication are established). You follow NCSC Password Guidance to enable users to set up a strong password for their accounts.
- [IG-1.4-04] You validate input data. All input data is verified, as early as possible, and any error handling output is clear and does not expose internal information that could be exploited. Use prepared statements with parameterised queries as standard practice. Character wildcards should not be permitted. Syntactic validation is in place that enforces correct syntax for structured fields, such as the set of characters that are permitted. Semantic validation is in place that enforces correctness of values in the context of the software, such as minimum and maximum inputs (like start dates and end dates) and ranges.
- [IG-1.4-05] You securely store credentials. You identify all credentials that would cause harm in the wrong hands (examples include passwords, certificates and API keys). You should avoid hard-coded credentials in your software.
- [IG-1.4-06] You protect sensitive data (such as personal, financial and medical information). If there is a significant risk of unauthorised access, either at rest or in transit, you should ensure that sensitive data is encrypted using well established standardised cryptography.

### Principle 2.1 — Protect the build environment against unauthorised access.

*Theme 2: Build environment security. Code p.6.*

**APC claims** (APC, Theme 2, Principle 2.1):

- [APC-2.1-01] Roles are defined that specify the data and functionality that each role is allowed to access.
- [APC-2.1-02] Users of the build environment are required to authenticate on a regular basis.
- [APC-2.1-03] Users of the build environment are issued with credentials bound to their role.
- [APC-2.1-04] Credentials are securely managed and stored.
- [APC-2.1-05] Credentials are multi factor.
- [APC-2.1-06] Users with access to the build environment are regularly reviewed to ensure they still have a legitimate need.

**Implementation guidance** (IG page 4 'Theme 2: Build environment security', Principle 2.1):


*You should ensure that:*

- [IG-2.1-01] You have a policy that defines who is allowed to access systems within the build environment.
- [IG-2.1-02] You have a policy for removing users from the build environment when they no longer need access.
- [IG-2.1-03] Monitoring of actions (such as accessing a system) is logged.
- [IG-2.1-04] Users have the appropriate level of privilege for their accounts (the least privilege necessary to perform their role).
- [IG-2.1-05] Your external-facing access management components are isolated from the rest of your systems.
- [IG-2.1-06] Credentials are securely stored, and no default credentials are issued.

### Principle 2.2 — Control and log changes to the build environment.

*Theme 2: Build environment security. Code p.6.*

**APC claims** (APC, Theme 2, Principle 2.2):

- [APC-2.2-01] Access and changes to the build environment are logged.
- [APC-2.2-02] Only authorised personnel can make changes to the build environment.
- [APC-2.2-03] Logs are auditable and retained for an agreed period.
- [APC-2.2-04] The confidentiality and integrity of logs is protected.

**Implementation guidance** (IG page 4 'Theme 2: Build environment security', Principle 2.2):

- [IG-2.2-01] To establish an effective logging capability, you will need to:

*To establish an effective logging capability, you will need to:*

- [IG-2.2-02] choose which logs to generate or retain
- [IG-2.2-03] decide how to retain logs
- [IG-2.2-04] implement protected log storage and tooling for analysis
- [IG-2.2-05] validate your logging capability is working as intended

*You should ensure that:*

- [IG-2.2-06] any changes made to the build environment are appropriately logged and retained
- [IG-2.2-07] a policy is in place on who is allowed to make changes to the build environment, what access they have and how long that access is required
- [IG-2.2-08] a policy is in place to remove those privileges when they are no longer needed

**Additional good practice for: build environment security — Mandate strong authentication for developers** (IG page 4):

- [IG-2.x-01] Access to the build environment must be controlled so that it is prohibitively difficult for attackers to gain access.
- [IG-2.x-02] Strong authentication (such as MFA) must be mandated for all developers who access the build environment.

*You should ensure that:*

- [IG-2.x-03] MFA is mandated for all accounts that have access to the build environment, and anything that resides within it.
- [IG-2.x-04] You follow NCSC password guidance to enable all build environment users to set up a strong password for their accounts. Users should be required to provide an extra factor when they log in using a device they have not used before.
- [IG-2.x-05] There is adequate support in place for MFA so that build environment users are able to report lost or forgotten credentials and reset them securely. You will need to ensure that an attacker cannot use these processes to bypass MFA.

### Principle 3.1 — Distribute software securely to customers.

*Theme 3: Secure deployment and maintenance. Code p.6.*

**APC claims** (APC, Theme 3, Principle 3.1):

- [APC-3.1-01] The integrity of software (including updates) can be verified in the customer environment.
- [APC-3.1-02] Software (including updates) is distributed overtrusted channels.

**Implementation guidance** (IG page 5 'Theme 3: Secure deployment and maintenance', Principle 3.1):

- [IG-3.1-01] To do this effectively, configuration management techniques should be used to manage change and version control, which allow a rollback to a specific state if necessary.

*You should ensure that:*

- [IG-3.1-02] A trusted location or tool is available (such as a support website with appropriate protective measures) for customers to download the software from. Code integrity/provenance must be verified to provide confidence in its integrity before installation.
- [IG-3.1-03] Automatic deployments of code are transmitted across a connection protected by standards such as TLS.
- [IG-3.1-04] For both regular and emergency deployments, clear documentation is provided to customers about version control and security fixes.
- [IG-3.1-05] Access control is in place for deployment and production environments.
- [IG-3.1-06] Software is tested thoroughly before deployment, with change claims in place to be able to roll back to the specific version if required.
- [IG-3.1-07] Code is digitally signed throughout the deployment pipeline. Code can only be pulled from an approved list of third parties.

### Principle 3.2 — Implement and publish an effective vulnerability disclosure process.

*Theme 3: Secure deployment and maintenance. Code p.6.*

**APC claims** (APC, Theme 3, Principle 3.2):

- [APC-3.2-01] A vulnerability disclosure policy and process is published.
- [APC-3.2-02] The vulnerability disclosure process describes how to confidentially report vulnerabilities.

**Implementation guidance** (IG page 5 'Theme 3: Secure deployment and maintenance', Principle 3.2):

- [IG-3.2-01] Internal practices should be in place to identify vulnerabilities, but this can be enhanced dramatically by putting in place a vulnerability disclosure policy which is communicated effectively to others.
- [IG-3.2-02] The vulnerability disclosure policy should include an openness to accept information from security researchers who may test software as part of a vulnerability disclosure process.

*IG 3.2 refers implementers to the NCSC Vulnerability Disclosure Toolkit: "The NCSC’s Vulnerability Disclosure Toolkit contains the essential components you need to set up your own vulnerability disclosure process and includes additional information on implementing the process, including validation and triage."*

### Principle 3.3 — Have processes and documentation in place for proactively detecting, prioritising and managing vulnerabilities in software components.

*Theme 3: Secure deployment and maintenance. Code p.6.*

**APC claims** (APC, Theme 3, Principle 3.3):

- [APC-3.3-01] Knowledge of public vulnerabilities is kept up to date.
- [APC-3.3-02] A vulnerability management plan exists that assesses and prioritises responses to vulnerabilities.

**Implementation guidance** (IG page 5 'Theme 3: Secure deployment and maintenance', Principle 3.3):

- [IG-3.3-01] In addition to a vulnerability disclosure policy, internal processes should be in place to detect and respond to vulnerabilities in a way that will support customers to implement their own vulnerability management process.

*You should ensure that:*

- [IG-3.3-02] you maintain a knowledge of public and third-party vulnerabilities
- [IG-3.3-03] a vulnerability management plan exists, which describes how vulnerabilities can be proactively detected
- [IG-3.3-04] you follow a documented process for the timely assessment of the severity of vulnerabilities and prioritise responses to vulnerabilities based on risk assessment
- [IG-3.3-05] you have a ‘security response playbook’ in place with roles assigned to handle the response, and test this periodically
- [IG-3.3-06] discovered vulnerabilities are reported to the CVE Website (which identifies, defines and catalogues publicly disclosed vulnerabilities so that they can be consistently described, aiding collaboration and communication)
- [IG-3.3-07] root cause analysis is carried out to prevent recurring vulnerabilities

*Informative (permissive, not extracted as requirements):* "Discovering new vulnerabilities in software, understanding how they can be exploited, and effective remediation can be achieved through a variety of approaches, including:" — regular vulnerability scanning and testing of your software, including third-party components; monitoring vulnerability databases, security mailing lists and other sources of vulnerability reports through manual or automated means; using threat intelligence sources to better understand how vulnerabilities in general are being exploited.

### Principle 3.4 — Report vulnerabilities to relevant parties where appropriate.

*Theme 3: Secure deployment and maintenance. Code p.6.*

**APC claims** (APC, Theme 3, Principle 3.4):

- [APC-3.4-01] Internal security teams are informed.
- [APC-3.4-02] Affected customers are informed.

**Implementation guidance** (IG page 5 'Theme 3: Secure deployment and maintenance', Principle 3.4):

- [IG-3.4-01] Software companies must manage the flow of information around a reported vulnerability by ensuring it gets sent to the appropriate team or organisation, such that a coordinated and effective response can be delivered.
- [IG-3.4-02] Several groups should be considered to notify, once a vulnerability has been reported or when a fix is available:

*Several groups should be considered to notify, once a vulnerability has been reported or when a fix is available:*

- [IG-3.4-03] internal security teams: usually will be the first people to contact, so that they can assess the implications of the vulnerability and work out how best to address the concerns raised
- [IG-3.4-04] customers and users: noting the communication with customers guidance below, the customers of the software should be informed promptly to take necessary precautions
- [IG-3.4-05] vulnerabilities systems: reporting to databases such as the National Vulnerability Database (NVD) or Common Vulnerabilities and Exposures (CVE) helps in tracking and managing vulnerabilities globally
- [IG-3.4-06] regulatory bodies: might need to be informed to comply with legal requirements
- [IG-3.4-07] third-party vendors: if the vulnerability affects third-party software or services, it should be reported to the respective vendors to ensure they can address the issue
- [IG-3.4-08] open source software: follow any vulnerability management process for the software

### Principle 3.5 — Provide timely security updates, patches and notifications to customers.

*Theme 3: Secure deployment and maintenance. Code p.6.*

**APC claims** (APC, Theme 3, Principle 3.5):

- [APC-3.5-01] Security updates are distributed as soon as is practicable.
- [APC-3.5-02] Security updates are tested and secure by default.

**Implementation guidance** (IG page 5 'Theme 3: Secure deployment and maintenance', Principle 3.5):

- [IG-3.5-01] When new vulnerabilities are discovered, particularly high impact ones, a timely and well tested patch should be issued by the vendor and installed by the customer to reduce the risk that it could be exploited to cause harm in a system.
- [IG-3.5-02] Updates and patches should not be a premium feature of software.
- [IG-3.5-03] Security fixes should be provided as standard for a reasonable support period, which has been clearly communicated to customers.

*You should ensure that:*

- [IG-3.5-04] Once identified, vulnerabilities should be validated and triaged. Prioritisation and classification criteria might include how easy to exploit they are and the potential impact if exploited. The outcome of this triage process will tell you whether to fix, acknowledge or investigate further.
- [IG-3.5-05] Vulnerabilities should be fixed within a reasonable timeframe, according to their priority. If they are critical, you will need to issue an ‘out-of-band’ update that sits outside any regular update cadence. You may need to issue a temporary fix or mitigation to begin with, followed by a more stable solution.
- [IG-3.5-06] Updates should be signed and thoroughly tested.
- [IG-3.5-07] The release of any updates and patches should ideally be communicated to customers in a clear manner, specifying aspects such as that it is a security update (or includes a security update), whether it is a temporary mitigation or a full fix.

### Principle 4.1 — Provide information to the customer specifying the level of support and maintenance provided for the software being sold.

*Theme 4: Communication with customers. Code p.6.*

**APC claims** (APC, Theme 4, Principle 4.1):

- [APC-4.1-01] ‘End of support’ dates are published for all software components.
- [APC-4.1-02] A policy on frequency of updates and the process for applying them is published.
- [APC-4.1-03] User documentation describes how to correctly and securely apply updates and use software.

**Implementation guidance** (IG page 6 'Theme 4: Communication with customers', Principle 4.1):

- [IG-4.1-01] To ensure that the customer is aware of the expected lifespan of the software, they should be given enough notice to adapt when the software reaches end of support, and understand how to secure the product.

*You should ensure that:*

- [IG-4.1-02] You provide information to the customer, in an accessible way, specifying the level of support and maintenance provided for the software being sold. You clarify what level of support will be provided, including frequency of patching against known vulnerabilities, how these are to be distributed and how the customer will be notified of these patches being available.
- [IG-4.1-03] You provide customers with documentation on how to securely use your software. This should emphasise the importance of applying the latest software updates, using strong authentication / MFA, how to regularly back up important data, controlling access to only those that require it and what ports may be exposed to the outside world along with firewall rules.

### Principle 4.2 — Provides at least 1 year’s notice to customers of when the software will no longer be supported or maintained by the vendor.

*Theme 4: Communication with customers. Code p.6.*

**APC claims** (APC, Theme 4, Principle 4.2):

- [APC-4.2-01] Customers are given at least 1 year's notice of when software will no longer be supported.

**Implementation guidance** (IG page 6 'Theme 4: Communication with customers', Principle 4.2):


*You should ensure that:*

- [IG-4.2-01] An end-of-support policy for the product is declared. This should include the length of time the software is supported for, and/or the notice period that will be given of the product containing the software reaching its end of life. This notification period should not be less than one year to allow the customer to take appropriate risk mitigation measures and should advise on the risks of not taking such measures.

### Principle 4.3 — Make information available to customers about notable incidents that may cause significant impact to customer organisations.

*Theme 4: Communication with customers. Code p.6.*

**APC claims** (APC, Theme 4, Principle 4.3):

- [APC-4.3-01] An incident support plan is published.
- [APC-4.3-02] Customers are informed of relevant incidents in a timely manner.

**Implementation guidance** (IG page 6 'Theme 4: Communication with customers', Principle 4.3):


*You should ensure:*

- [IG-4.3-01] A policy or plan is created in advance and shared with the customers of your software detailing how you will go about supporting them in the event of an incident occurring. This may contain roles and responsibilities, incident response procedures (including key points of contact), containment strategies, communication plans, eradication measures, recovery plans and post-incident reviews.
- [IG-4.3-02] When an incident occurs, you should prompt notification to users as soon as possible in a clear and concise way, communicating what happened, the expected impact and what is being done to resolve it. This will help minimise impact and maintain trust. Regular updates should be provided until the incident is resolved, and followed up with a post incident report, identifying the root cause and specifying measures being taken to prevent a future similar event.

## Part C — Implementation Guidance statements outside a principle

| id | locator | text |
|---|---|---|
| IG-ABOUT-01 | IG page 2 'About the Software Security Code of Practice' › 'Secure by design' | If this ‘secure by default’ approach is not possible, the user should be provided with guidance on how to securely configure the software . |
| IG-ABOUT-02 | IG page 2 'About the Software Security Code of Practice' › 'Note:' | The principles are objective measures that must be evidenced to provide confidence in the resilience of the software against an attacker that: |
| IG-T1-01 | IG page 3 'Theme 1: Secure design and development' (theme introduction) | The tools made available to developers should consider usability, ease of maintenance, functionality and cost. |

## Part D — Source-published mapping (IG page 7, Appendix 1: Secure development frameworks)

> There are many secure development frameworks available ‘off-the-shelf’. Examples include:

| Framework | IG description (verbatim) |
|---|---|
| NIST Secure Software Development Framework | A set of fundamental, sound and secure software development practices based on established secure software development practice documents from organizations such as BSA, OWASP, and SAFECode. |
| Microsoft Security Development Lifecycle | The approach Microsoft uses to integrate security into DevOps processes (sometimes called a DevSecOps approach). |
| OWASP Software Development Lifecycle | The OWASP® Foundation works to improve the security of software through its community-led open source software projects. |
| Cisco Secure Development Lifecycle | Designed to introduce security and privacy throughout the development process. |
| Supply-Chain Levels for Software Artifacts (SLSA) | Supply-chain Levels for Software Artifacts, or SLSA ('salsa') is a security framework, a checklist of standards and controls to prevent tampering, improve integrity, and secure packages and infrastructure. |
| S2C2F Simplified Requirements | The core concepts of the Secure Supply Chain Consumption Framework (S2C2F) to outline and define how to securely consume OSS dependencies (such as NuGet and NPM) into the developer's workflow. |

The Code itself (p.2, Background) states alignment without a clause-level mapping: "Where possible, the Code reflects internationally recognised best practices, which includes those outlined in the US Secure Software Development Framework (SSDF) and the EU’s Cyber Resilience Act, as well as existing guidance and formal standards in this space."

## Glossary (Code pp.7–9, Table 3) — terms the object model uses

Definitions are in `.cache/uk-software-security-code-of-practice.md`; the normative sentences inside them are C-GLOSS-* above. Terms: Assurance, Principles & Claims (APCs); Build Environment; Digital service; Enterprise customer; Implementation guidance; Incident; Lifecycle; Principles Based Assurance (PBA); Relevant parties (action 3.4); Secure by Default; Secure by Design; Secure development framework; Self-assessment form; Senior Leader; Senior Responsible Owner; Shall; Software; Software service (SaaS); Software Vendor; Third-party component; Vulnerability; Vulnerability disclosure process.
