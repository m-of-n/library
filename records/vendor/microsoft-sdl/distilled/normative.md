---
schema: "library-normative/v1"
id: microsoft-sdl-normative
record: microsoft-sdl
kind: normative
type: normative
title: "microsoft-sdl — the current SDL practice set, verbatim"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

Source: the Microsoft SDL web practice set (16 pages, fetched 2026-10-02; `.cache/microsoft-sdl.md`). Every statement below is verbatim page text in the source order; Markdown emphasis and link targets are removed, link text kept; resource-link lists are omitted (they are in `requirements.yaml` → `resources`). Ids in brackets are the requirement ids (`microsoft-sdl#…`).

## Lifecycle stages (practices index page)

"Security risks (and the need to mitigate them) can occur at any point in the development lifecycle:"

- [STAGE-design] Design – ensure that the design doesn’t naturally allow attackers to easily gain unauthorized access to the workload, its data, or other business assets in the organization.
- [STAGE-code] Code – ensure that writing (and re-use) of code doesn’t allow attackers to easily take control of the application to perform unauthorized actions that harm customers, employees, systems, data, or other business assets. Developers should also work in a secure environment that doesn’t allow attackers to do this without their knowledge.
- [STAGE-build-and-deploy] Build and Deploy – ensure that the continuous integration and continuous deployment (CI/CD) processes don’t allow unauthorized users to alter the code and allow attackers to compromise it.
- [STAGE-run] Run – ensure that environment running the code (cloud, servers, mobile devices, others) follows security best practices across people, process, and technology to avoid attackers compromising and abusing the workload. This includes the adoption of well-established best practices, security baseline configurations, and more.
- [STAGE-zero-trust-architecture-and-governance] Zero Trust architecture and governance – All of these stages should follow Zero Trust principles to assume breach (assume compromise), explicitly verify trust, and grant the least privilege required for each user account, machine/service identity, and application component.

"These are the 10 key security practices of the SDL that help you integrate security into each stage of your overall development process. These practices will be updated as the SDL, learnings, best practices, and tooling evolve." (practices index)

## Practice 1: Establish security standards, metrics, and governance [1]

*Practice 1 page (https://www.microsoft.com/en-us/securityengineering/sdl/practices/security-program-management), introduction*

This practice focuses on continually updating and communicating security requirements to reflect changes in functionality and to the regulatory and threat landscape.

Clear guidance and rules are required to guide team members (product line leaders, product owners, developers, operations, and other roles) through what they need to do for security, how success is measured, and what resources are available to help them.

The need to consider security and privacy is a fundamental aspect of developing highly secure applications and systems and regardless of development methodology being used. Security requirements must be continually updated to reflect changes in required functionality and changes to the threat landscape. Obviously, the optimal time to define the security requirements is during the initial design and planning stages as this allows development teams to integrate security in ways that minimize disruption. Factors that influence security requirements include (but are not limited to) the legal and regulatory requirements, internal standards and coding practices, review of previous incidents, and known threats. These requirements should be tracked through either a work-tracking system or through telemetry derived from the engineering pipeline.

It is essential to define the minimum acceptable levels of security quality and to hold engineering teams accountable to meeting that criteria. Defining these early helps a team understand risks associated with security issues, identify and fix security defects during development, and apply the standards throughout the entire project. Setting a meaningful bug bar involves clearly defining the severity thresholds of security vulnerabilities (for example, all known vulnerabilities discovered with a “critical” or “important” severity rating must be fixed with a specified time frame) and never relaxing it once it's been set. In order to track key performance indicators (KPIs) and ensure security tasks are completed, the bug tracking and/or work tracking mechanisms used by an organization (such as Azure DevOps) should allow for security defects and security work items to be clearly labeled as security and marked with their appropriate security severity. This allows for accurate tracking and reporting of security work.

A formal mechanism for tracking exceptions to the standards is needed to effectively manage risk. Eventually, every organization encounters circumstances that require security risks to be accepted temporarily due to business priorities and resource constraints. The hallmark of a mature governance process is that such risk acceptance is handled by well-defined processes to triage, justify, approve, and track temporary exceptions to security standards. Primary reasons for formally tracking exceptions to security requirements include:

1. Exceptions are approved at the appropriate management level based on their security risk.
2. Formal tracking lets management know the nature of the security risks they are accepting and what the remediation plan is so that appropriate resources can be allocated to fix security issues in a timely fashion.
3. Exceptions are timebound and must be renewed and re-approved if they expire before they are remediated.

### 1.1 Identify Required Standards [1.1]

1.1 Identify Required Standards – Every organization will have their own definition of requirements for appropriate security standards. You can begin by reviewing the information provided in the following guides:

- The NIST Secure Software Development Framework
- Industry-specific regulations e.g. where payment account data is stored, processed or transmitted, PCI Data Security Standard (PCI DSS) should be met. Health Insurance Portability and Accountability Act (HIPAA) regulations for U.S. companies that work with protected health information (PHI).

### 1.2 Define Security Requirements [1.2]

1.2 Define Security Requirements – Establish a minimum-security baseline that takes account of both security and compliance controls. Ensure these are baked into the DevOps process and pipeline. At the very minimum, ensure the baseline takes into account real-world threats such as the OWASP Top 10 or SANS Top 25, and industry or regulatory requirements and issues known to exist or that could be introduced by human error in the technology stack you select. Use Azure DevOps to help record security requirements once defined:

### 1.3 Define metrics and compliance reporting [1.3]

1.3 Define metrics and compliance reporting – It is essential to define the minimum acceptable levels of security quality and to hold engineering teams accountable to meeting that criteria. Defining these early helps a team understand risks associated with security issues, identify and fix security defects during development, and apply the standards throughout the entire project. Setting a meaningful bug bar involves clearly defining the severity thresholds of security vulnerabilities (for example, all known vulnerabilities discovered with a “critical” or “important” severity rating must be fixed with a specified time frame) and never relaxing it once it's been set. The bug bar should be maintained to reflect the changing threat landscape, both the type of issue and their severity. The bug bar is a great way to ensure that everyone involved in triaging issues understands why a security issue has a certain severity and what action is required.

In order to track key performance indicators (KPIs) and ensure security tasks are completed, the bug tracking and/or work tracking mechanisms used by an organization (such as Azure DevOps) should allow for security defects and security work items to be clearly labeled as security and marked with their appropriate security severity. This allows for accurate tracking and reporting of security work.

### 1.4 Create a Security Exception Process [1.4]

1.4 Create a Security Exception Process – Key aspects of managing security risk for an organization include making risks visible and holding the organization accountable for accepting such risks and remediating them in a timely fashion. It is not reasonable to expect that organizations can or should achieve 100% compliance with their security policies all of the time. For example, when new policies are added or existing ones are changed to raise the bar for security, it takes time for engineering teams to reach this new level of compliance. So, the very act of raising security standards can cause non-compliance.

When an engineering team cannot achieve compliance with a security policy within the timeframe of defined SLAs, they must request a temporary exception to the policy. A security program should provide a clear process for requesting and managing such security exceptions. This should include steps such as:

1. Triaging the security risk of non-compliance with the policy and documenting:
- The reason why an exception is needed.
- Any short-term actions that can reduce the risk.
- A remediation plan to achieve compliance.
- An expiration date for the exception.
2. Determining which level of management must review the risk, based on its severity.
3. Requesting an exception to the policy via an approval workflow.
4. Formal review and approval/denial of the exception request by the proper level of management.
5. Tracking of the exception to its resolution or expiration.
6. Reviewing the exception again when the security risk changes.
7. Restarting the exception approval workflow if the exception expires before being remediated.

The benefits of such a risk management process include:

- Management is aware of the risks and can allocate resources to address them.
- Deviations from policy must be justified and only exist temporarily.
- Security risks are discussed openly, fostering a culture of honesty.

## Practice 2: Require use of proven security features, languages, & frameworks [2]

*Practice 2 page (https://www.microsoft.com/en-us/securityengineering/sdl/practices/secure-platforms), introduction*

This practice focuses on ensuring development teams use well established and proven security solutions. This is important because secure solutions require a solid foundation, and experience has taught us that attempting to invent new solutions is challenging and almost always results in increased security risk and wasted time and effort.

Additionally, some aspects of software design and development are too important to leave undefined and areas such as authentication and authorization and the associated and necessary logging for auditing are foundational controls, that many other security controls are built upon, and organizations should standardize on an approach, that provides clear consistent guidance with guardrails and means to verify their implementation to the required standard.

Additionally, you should define and publish a list of approved tools and their associated security checks, such as compiler/linker options and warnings. Engineers should strive to use the latest version of approved tools, such as compiler versions, and to take advantage of new security analysis functionality and protections.

### 2.1 Identity [2.1]

2.1 Identity - Ensure users are using strong authentication and only have the level of permissions suitable to their needs (least privilege). See Practice 6.1 Take a Zero Trust Approach for more information.

Managed Identities (instead of SAS tokens) - Managed Identities for Azure.

Secure Credential Storage (KeyVault / HSM)- Implement a mechanism to inventory, monitor, maintain, and update all stored secrets. Encrypt and store application secrets and eliminate the need to include secrets and other sensitive configuration information in code or configuration files of the code. Never store passwords or other sensitive data in source code or configuration files or in plaintext files (documents, spreadsheets) stored in unprotected locations. Production secrets should not be used for development or testing.

Use Standard Identity Libraries (MSAL): The Microsoft Authentication Library (MSAL) enables developers to acquire security tokens from the Microsoft identity platform to authenticate users and access secured web APIs. It can be used to provide secure access to Microsoft Graph, other Microsoft APIs, third-party web APIs, or your own web API.

Enforce Least Privilege: For the workload, each account type and component of the system should have only the minimum necessary privileges to perform the required operations. Provide control and management of sensitive accounts and grant access only as needed. It’s important to restrict and minimize the number of people in privileged roles who have access to secured information or resources. This reduces the chance of a malicious user getting that access, or an authorized user inadvertently compromising a sensitive resource. However, users still need to carry out privileged operations on a service and there is a need to understand what those operations are and to separate those roles such that there’s no easy opportunity for privilege escalation. The principle of “just enough administration” should be adopted to constrain the elevated privilege only to those functions the administrator requires to complete the task at hand and only on a "just-in-time" (JIT) basis and only for the minimum practical period.

### 2.2 AI safety and security [2.2]

2.2 AI safety and security - Review the specific guidance for anyone building or integrating AI solutions:

### 2.3 Data protection [2.3]

2.3 Data protection: Securing content used in apps - Secure implementation and connection to databases, storage accounts, unstructured documents, and more.

### 2.4 Logging and telemetry [2.4]

2.4 Logging and telemetry - Provides valuable insights into the behavior and performance of systems and applications. Security logging must be enabled and retained to assist with any post-incident investigations. Telemetry helps guide developer feedback on user interaction, feature popularity, and performance metrics.

### 2.5 Use approved tools [2.5]

2.5 Use approved tools - Define and publish a list of approved tools and their associated security checks, such as compiler/linker options and warnings. Engineers should strive to use the latest version of approved tools, such as compiler versions, and to take advantage of new security analysis functionality and protections.

## Practice 3: Perform secure design review and threat modeling [3]

*Practice 3 page (https://www.microsoft.com/en-us/securityengineering/sdl/practices/secure-by-design), introduction*

Our computer systems operate in a hostile threat landscape with well-funded, technically capable adversaries continually probing for and exploiting vulnerabilities. Security design flaws can result in vulnerabilities that can be exploited by attackers. Threat modeling and security design reviews of threat models identify potential security threats so that designers can mitigate them early in the development process, resulting in systems that are Secure by Design. Adding security during the design process is much cheaper and less risky than adding it after the fact. To design secure systems, one must shift the focus from:

how products should work to how products might be abused.

Threat modeling lets you pause and consider the system from a security and privacy standpoint, answering questions like:

- “What if this feature were abused by an attacker instead of being used as intended?”
- “What happens to assets and users if attackers compromise the system?”
- “What happens to the system if individual components I rely on become unavailable?”

Threat modeling is a structured approach to analyze the security design of the system, while “thinking like an attacker”. The threats that are identified can then be mitigated before the new product or feature ships.

### 3.1 Identify use cases, scenarios, and assets [3.1]

3.1 Identify use cases, scenarios, and assets - An essential part of threat modeling and reviewing threat models is understanding what business functions or “use cases” the system has. Scenarios describing the sequence of steps for typical interactions with the system illustrate its intended purposes and workflows. They also describe the different roles of users and external systems that connect to it. The first step in threat modeling is to document the business functions the system performs and how users or other systems interact with it. Supplement textual descriptions of use cases and scenarios with flowcharts and UML sequence diagrams as needed. Whether you use formal documentation such as use cases and scenarios, or take a more informal approach, ensure you provide context that answers these questions:

- What are the business functions of the system?
- What are the roles of the actors that interact with it?
- What kind of data does the system process and store?
- Are there special business or legal requirements that impact security?
- How many users and how much data is the system expected to handle?
- What are the real-world consequences if the system fails to provide confidentiality, integrity, or availability of the data and services it handles?

An asset is something of value in a system that needs to be protected. Some assets are obvious such as money in financial transactions or secrets such as passwords and crypto keys. Others are more intangible like privacy, reputation, or system availability. Once you properly identify the system’s assets, it is easier to identify threats against them. Document the list of system assets.

Examples of tangible assets:

- Personal photos and contacts stored on a smartphone
- Compute resources in a cloud environment
- Software supply chain integrity in a development environment
- Medical imaging and diagnostic data
- Financial accounting data
- Biometric authentication data
- Proprietary formulae and manufacturing processes
- Military and government secrets
- Machine learning models and training data
- Credit card data

Examples of intangible assets:

- Customer trust
- User privacy
- System availability

### 3.2 Create an architecture overview [3.2]

3.2 Create an architecture overview - In addition to documenting business functionality and assets, create diagrams and tables to depict the architecture of your application, including subsystems, trust boundaries, and data flows between actors and components. At minimum, a Data Flow Diagram (DFD) is recommended, and other supplementary diagrams such as UML Sequence Diagrams to illustrate complex flows may also be helpful. A DFD is a high-level way to visualize data flows between the major components of a system. It is a simplified view that does not include every detail—just enough to understand the security properties and attack surface of the system. It is a recommended practice to label the following in your DFD arrows:

- Data types (business function)
- Data transfer protocols

A trust boundary is a logical construct used to demarcate areas of the system with different levels of trust such as:

- Public Internet vs. private network
- Service APIs
- Separate operating system processes
- Virtual machines
- User vs. kernel memory space
- Containers

Trust boundaries are important to consider when threat modeling because calls that cross them often need to be authenticated and authorized. Data that crosses a trust boundary may need to be treated as untrusted and validated or blocked from flowing altogether. There may be business/regulatory rules related to trust boundaries. For example, sovereign clouds must ensure that data is stored only within their trust boundaries, and in some cases, HIPAA Protected Health Information (PHI) shouldn’t cross trust boundaries. Trust boundaries are often illustrated in DFDs with dashed red lines.

### 3.3 Identify the threats [3.3]

3.3  Identify the threats – Threat modeling is most effective when performed by a group of people familiar with the system architecture and business functions who are prepared to think like attackers. Here are some tips for scheduling an effective threat modeling session:

- Prepare the list of use cases/scenarios and, if possible, a first draft of DFDs in advance.
- Limit the scope of your threat modeling activity primarily to the system or features that you are developing or directly interface with.
- Designate an official notetaker to capture and record threats, mitigations and action items during the meeting.
- Reserve at least 2 hours for the meeting. The first hour will usually be spent on getting a common understanding of system architecture and what scenarios you are modeling so you can spend the second hour identifying threats and mitigations.
- If you can’t cover it all in two hours, decompose the system into smaller chunks and threat model them separately.
- Invite people of varied backgrounds, including:
- Engineers who are developing and testing the system
- Product owners who can weigh security risk against business goals
- Security analysts/engineers
- People who are proficient at software testing (violating system assumptions, testing boundary conditions, generating invalid input, etc.)

STRIDE is a common methodology for enumerating potential security threats that fall into these categories:

| Spoofing | Making false identity claims |
|---|---|
| Tampering | Unauthorized data modification |
| Repudiation | Performing actions and then denying that you did |
| Information Disclosure | Leaking sensitive data to unauthorized parties |
| Denial of Service | Crashing or overloading a system to impact its availability |
| Elevation of Privilege | Manipulating a system to gain unauthorized privileges |

People and threat modeling tools apply this methodology by considering all the elements in a dataflow diagram and asking if threats in any of the STRIDE categories apply to them. STRIDE is useful for novice threat modelers who have not been exposed to all these threat categories and so might miss some important threats. However, STRIDE is not a substitute for thinking like an attacker. STRIDE may miss important design flaws that only thinking like an attacker will catch.

Thinking like an attacker is the most important and difficult part of threat modeling. Once you and your team understand the system architecture, use scenarios, and assets you need to protect, you must imagine what could go wrong with your system if a motivated, capable attacker attempts to compromise it. Thinking like an attacker is not as simple as applying a methodology like STRIDE to enumerate threats. You must also challenge the security assumptions in your design and contemplate what-if scenarios in which some or all your security controls fail as attackers actively try to compromise your assets. Examples of security assumptions:

- We assume our open-source dependencies don’t have malicious code.
- We assume that cloud computing services are inherently trustworthy.
- We assume that app users will not root their mobile devices.
- We assume that all authenticated users have benign intent.

Validate that your security assumptions are correct and consider what happens if they are not. Determine if any assumptions are invalid based on the threat landscape and the value of the assets you need to protect. It helps to study historical incidents to gain insight into the attacker mindset.

Many threats and mitigations are highly technical, and you are unlikely to think of them all on your own. Educate yourself on threats and associated mitigation techniques that apply to the domain you are working in. For instance, every web developer should be aware of attacks like cross-site scripting (XSS), cross-site request forgery (CSRF), and command injection. Study resources like the CWE Top 25 Most Dangerous Software Weaknesses and the OWASP Top Ten to learn more.

Record the threats you identify in your engineering team's work tracking system and rate their security severity so they can be prioritized accordingly. Document the threats you identify with sufficient detail that those reading them later can understand them. Well-written threats clearly describe:

- The threat actor who exploits the vulnerability
- Any preconditions required for exploitation
- What the threat actor does
- The consequences for affected assets and users

### 3.4 Identify and track mitigations [3.4]

3.4 Identify and track mitigations - Secure Design Philosophy: When identifying mitigations, keep in mind that security is not “all or nothing”. A partial mitigation that raises the cost for an attacker, slows them down to give defenders time to detect them, or limits the scope of damage is much better than no mitigation at all. Think in terms of layered defenses. Attackers don’t just exploit a single vulnerability and stop there. They chain multiple vulnerabilities together, pivoting from one target system to the next until they achieve their objective (or get caught.) Each layered defense increases the likelihood that attackers will be blocked or detected. Also, assume that other layers’ security controls will be bypassed or disabled. This is the essence of the Assume Breach philosophy which results in a resilient set of layered defenses rather than relying solely on external defenses that, if bypassed, result in a major breach.

Recommended Secure Design Practices:

- Design and Threat Model as a Team
- Prefer Platform Security to Custom Code
- Secure Configuration is the Default
- Never Trust Data from the Client
- Assume Breach
- Enforce Least Privilege
- Minimize Blast Radius
- Minimize Attack Surface
- Consider Abuse Cases
- Monitor and Alert on Security Events

Threat modeling is not complete until you create work items to track your threat findings and the related development and testing tasks to mitigate them. Consider tagging the work items and writing queries so they are easy to find. A threat model provides the seeds for a good security test plan. Be sure to test that your mitigations work as intended and use automated testing when possible.

### 3.5 Communicate threat models to key stakeholders [3.5]

3.5 Communicate threat models to key stakeholders - Threat modeling is not complete until you create work items to track your threat findings and the related development and testing tasks to mitigate them. Consider tagging the work items and writing queries so they are easy to find. A threat model provides the seeds for a good security test plan. Be sure to test that your mitigations work as intended and use automated testing when possible.

### 3.6 Threat Modeling resources [3.6]

3.6 Threat Modeling resources

## Practice 4: Define and use cryptography standards [4]

*Practice 4 page (https://www.microsoft.com/en-us/securityengineering/sdl/practices/cryptography), introduction*

You must establish and apply sound cryptographic practices to have any strong and sustainable security assurances. Almost all technical security assurances ultimately depend on cryptography including authentication and authorization mechanisms, communication security (such as TLS/SSL), data security, and more. If attackers can find a weakness in the underlying cryptographic implementation, all of the other security assurances will quickly unravel.

It is critically important to use the correct cryptographic solution to protect data from unintended disclosure or alteration while data is being stored (at rest) or transmitted (in transit). To achieve this, it’s necessary to know what data you need to protect via encryption, what mechanisms should be used to encrypt that data and how encryption keys and certificates will be managed.

Threat modeling, described in practice 3, is a great way to help identify scenarios where data that needs to be protected by encryption exists.

Because this is a complex topic where many developers are not cryptography experts, it is critical to have clear standards and guidance (documentation, examples, etc.) for how to use cryptography properly and to prevent the implementation of bespoke algorithms.

Providing specifics on every element (algorithms, key lengths, cipher modes, key and initial vector generation techniques and usages, and cryptographic libraries) of the encryption implementation is also necessary and requires expert input, which may not be available.  However, a good general rule is to only use industry-vetted encryption libraries as it is intended to ensure a correct and secure implementation of the cryptographic algorithms as well as appropriate security patching as needed.

### 4.1 Encrypt data in transit and at rest [4.1]

4.1 Encrypt data in transit and at rest - Ensure data is encrypted at rest and in transit, this includes security-sensitive information and management and control data. For encryption in transit, use only strong versions of TLS (see recommendation) for all internet traffic and ideally, traffic within private networks. For encryption at rest, be sure you understand the protections an encryption solution provides. While many easily deployable encryption solutions exist to protect data on a device or disk from theft (offline attack), they do not protect against online compromise through application logic, and additional solutions are required in these situations to encrypt data before it's written to storage (encrypt in transit).

### 4.2 Post-Quantum Cryptography (PQC) [4.2]

4.2 Post-Quantum Cryptography (PQC) - We recommend prioritizing symmetric encryption where applicable and subsequently adopting post-quantum cryptography (PQC) for asymmetric encryption once standardized and approved by relevant setting bodies and governments, as recommended by cybersecurity agencies globally.

### 4.3 Cryptographic agility [4.3]

4.3 Cryptographic agility - The practice of implementing cryptographic solutions to enable changes to new cryptographic mechanisms, algorithms and libraries when the need arises, such as in the case of vulnerabilities discovered in libraries that compromise sound algorithms, or when an encryption algorithm might be considered broken at any time. Cryptographic agility is critical to any successful plan to efficiently apply new cryptographic updates, including the adoption of quantum-safe algorithms.

### 4.4 Encryption key and certificate management and rotation [4.4]

4.4 Encryption key and certificate management and rotation - Encrypting data is only a portion of a successful cryptography standard and it's also essential to define how to manage, protect and rotate encryption keys and certificates. Keys and certificates have a limited lifespan, and it is necessary to define mechanisms to manage the lifecycle of keys and certificates, including mechanisms to both create new keys and certificates once the previous ones are near expiration and to rapidly rotate in the event of a security incident, such as unintended access. Anyone who can access an encryption key or private key can access the encrypted data, and therefore it's necessary to control who (whether a person or a service) has access (see Practice 2.1 Identity) and provide a clear audit log of that access (see Practice 2.5 Use approved tools).

## Practice 5: Secure the software supply chain [5]

*Practice 5 page (https://www.microsoft.com/en-us/securityengineering/sdl/practices/sscs), introduction*

The security of a workload depends on the security of all the components in that workload. An attacker who compromises one vulnerable component of a workload can often take over the whole workload (and often many others in the organization using lateral traversal techniques).

Today, the vast majority of software projects are built using third-party components (both commercial and open source). When selecting third-party components to use, it’s important to understand the impact that a security vulnerability in them could have to the security of the larger system into which they are integrated and you should always be more selective when using high-risk components, and consider a thorough analysis before using them. There are a myriad of ways that developers consume OSS today: git clone, wget, copy & pasted source, checking-in the binary into the repo, direct from public package managers, repackaging the OSS into a .zip, curl, apt-get, git submodule, and more. Securing the OSS supply chain in any organization is going to be near impossible if developer teams don’t follow a uniform process for consuming OSS. Enforcing an effective secure OSS supply chain strategy necessitates standardizing your OSS consumption process across the various developer teams throughout your organization, so all developers consume OSS using governed workflows.

### 5.1 Establish a secure open source software ingestion process [5.1]

5.1 Establish a secure open source software ingestion process - The Secure Supply Chain Consumption Framework (S2C2F) is a security assurance and risk reduction process that is focused on securing how developers consume open source software.

### 5.2 Understand dependencies in your environment [5.2]

5.2 Understand dependencies in your environment - Many software projects depend on open-source software projects, and many of these have dependencies on other open source projects. It’s essential to inventory use of open source, including dependencies to be able to update these if a vulnerability is discovered.

### 5.3 Produce software bill of materials (SBOM) [5.3]

5.3 Produce software bill of materials (SBOM) - SBOMs contribute software transparency and integrity. An SBOM is a machine-readable document that lists all of the components, including open source components used to create a product and helps better inventory software and therefore helps organizations to understand license and vulnerability risk. SBOMs also contain package and file checksums to help validate hashes, which is useful when signatures aren’t provided by other means.

### 5.4 Signing and attesting artifacts [5.4]

5.4 Signing and attesting artifacts – A Core aspect of software integrity is signing and validating its components. This applies to SBOMs just as much as artifacts created by tools integrated into your lifecycle, Artifact attestations establish a verifiable trail, enabling you to trace the integrity and prove the provenance of the artifact throughout the lifecycle.

## Practice 6: Secure the engineering environment [6]

*Practice 6 page (https://www.microsoft.com/en-us/securityengineering/sdl/practices/secure-dev-infra), introduction*

The security of a workload relies on the security of the operational environments where it is developed. An attacker that compromises the development environment infrastructure can take over the workload and find vulnerabilities in it, add vulnerabilities to it, add backdoors to it, access the data in it, launch lateral attacks on other internal systems, and more. Effectively, development security depends on the overall security of the environment including the security of identities, networks, servers, containers, email, user endpoints, and other systems.

Attackers have now expanded their focus to include targeting user accounts, development environments and build processes, and so those systems must be defended in addition to ensuring that source code and configuration files do not contain security errors or have been tampered with. Access to source code and engineering systems should be managed, operated and secured through Zero Trust and least privilege access policies. Source code should be stored in a version controls systems such as a Git with access gated through conditional access policies and multifactor authentication. Engineering systems should be segmented, managed from privileged access workstations, by individuals (who’s privileged access is regularly reviewed) using separate authorized identities. All privileges access should be provided following Just-In-Time and Just-Enough-Access (JIT/JEA) principles and security logging should be enabled and provided to the security monitoring team.

### 6.1 Take a Zero Trust approach [6.1]

6.1 Take a Zero Trust approach - At its core the Zero Trust model requires that each access request (user, service, or device) is verified as though it originated from an untrusted network, regardless of where the request originates or what resource it accesses. Base this always authenticate and authorize policy on all available data points, limit user access, especially privilede users, through Just-In-Time and Just-Enough-Access (JIT/JEA) policies and segment access to minimize the possible damage in the event of a breach.

### 6.2 Disallow direct commits to production branches [6.2]

6.2 Disallow direct commits to production branches - Configure your source control repositories to prevent developer accounts from making direct commits to production branches and to require code review and approval for all pull requests. This ensures that a single compromised/rogue developer account cannot make arbitrary changes to code for production systems.

### 6.3 Implement privileged access workstations [6.3]

6.3 Implement privileged access workstations - The use of hardened security workstations helps protect privileged users from internet attacks and threat vectors by providing a dedicated machine for sensitive tasks and separating these sensitive tasks and accounts from the daily use workstations.

- See Practice 8.8 Implement operational terminals: Device security

### 6.4 Provide Secure virtual workstations [6.4]

6.4 Provide Secure virtual workstations - Microsoft Dev Box gives developers self-service access to ready-to-code cloud workstations called dev boxes. Dev boxes can be configured with tools, source code, and prebuilt binaries that are specific to a project, so developers can immediately start working - securely. Dev boxes are managed like all devices on the network and can be more easily kept up to date and secured through security settings, network configuration and organizational policies.

### 6.5 Implement GitHub Codespaces [6.5]

6.5 Implement GitHub Codespaces - Created with security in mind, Codespaces provides a secure development environment through its built-in capabilities and native integration with the GitHub platform. Developers can quickly spin up a Codespace with only an IDE or browser and a GitHub account and work in a shared and secure development environment.

### 6.6 Secure deployment environments [6.6]

6.6 Secure deployment environments - Azure Deployment Environments empower development teams to quickly and easily spin up app infrastructure with project-based templates that establish consistency and best practices while maximizing security. This on-demand access to secure environments accelerates the stages of the software development lifecycle and compliments Microsoft Dev Box.

## Practice 7: Perform security testing [7]

*Practice 7 page (https://www.microsoft.com/en-us/securityengineering/sdl/practices/security-testing), introduction*

You must test applications to gain insight into the potential risk of any application and to validate the security results from the development process. Without this visibility, you cannot make decisions about the security of the workload like planning, prioritizing, and implementing fixes for this workload (and for the systemic issues in the development program and processes for all workloads).

Security testing is essential to secure software and is often amongst the first activities integrated into the development lifecycle that aim to have an immediate impact on security. Security testing includes both automated (e.g. Static and Dynamic Security Testing) and manual (Penetration testing) approaches, and each can be further categorized, and typically multiple approaches will be used.

### 7.1 Implement Static Analysis Security testing (SAST) [7.1]

7.1 Implement Static Analysis Security testing (SAST) - Analyzing the source code prior to compilation provides a highly scalable method of security code review and helps ensure that secure coding policies are being followed. It looks for known issues based on the application's logic and adherence to coding standards, rather than when the application is running. SAST is typically integrated into the developer workflow identifying simple to detect issues before code is committed and into build automation to identify vulnerabilities each time the software is built or packaged. There is no one- size-fits-all solution and development teams should decide the optimal frequency for performing SAST and will often deploy multiple tactics—to balance productivity with adequate security coverage.

### 7.2 Implement dynamic analysis security testing (DAST) [7.2]

7.2 Implement dynamic analysis security testing (DAST) - Refers to testing a fully compiled, packaged an executing version of a program or service checks functionality that is only exercisable when all the components are integrated and running.  This is typically achieved using a tool or suite of prebuilt attacks or tools, often replicating in a limited form what an attacker might try, that specifically test application behavior for memory corruption, user privilege issues, and other critical security problems. Similar to SAST, there is no one-size-fits-all solution and while some tools, such as web app scanning tools, can be more readily integrated into the continuous integration / continuous delivery pipeline, other DAST testing such as fuzzing requires a different approach.

### 7.3 Red/blue team exercises [7.3]

7.3 Red/blue team exercises - A dedicated “red team” of security experts simulate real-world attacks at the network, platform, and application layers - challenging the ability of cloud services “blue team”, a dedicated team of security responders, to detect, protect against, and recover from security breaches. Every exercise is followed by full disclosure between the Red Team and Blue Team to identify gaps, address findings, and significantly improve breach response.

### 7.4 Application penetration testing [7.4]

7.4 Application penetration testing - Simulate real-world attacks and challenge teams to detect, protect, and recover. Penetration testing is a security analysis of a software system performed by skilled security professionals simulating the actions of a hacker. The objective of a penetration test is to uncover potential vulnerabilities resulting from coding errors, system configuration faults, or other operational deployment weaknesses, and as such the test typically finds the broadest variety of vulnerabilities. Penetration tests are often performed in conjunction with automated and manual code reviews to provide a greater level of analysis than would ordinarily be possible.

### 7.5 Perform continuous security testing and measurement [7.5]

7.5 Perform continuous security testing and measurement - Continuous security testing (CST) checks for security issues and unsafe implementations in third-party libraries on an ongoing basis. CST includes software composition analysis (SCA) checks and static application security testing (SAST).

### 7.6 Perform triggered/cadence-based security testing [7.6]

7.6 Perform triggered/cadence-based security testing - Routine security tests should be conducted at a regular cadence to meet compliance requirements. These tests should be conducted periodically and on schedule.

### 7.7 Run a bug bounty program [7.7]

7.7 Run a bug bounty program - A bug bounty program offers monetary rewards to ethical hackers to uncover significant vulnerabilities that have a direct and demonstrable impact on the systems.

## Practice 8: Ensure operational platform security [8]

*Practice 8 page (https://www.microsoft.com/en-us/securityengineering/sdl/practices/operational-security), introduction*

The security of a workload relies on the security of the operational infrastructure and platform that is hosting it (cloud, on premises, hybrid, etc.). An attacker that compromises the production infrastructure can take over the workload, the data in it, and also launch lateral attacks on other internal systems. The security of the workload depends on the overall security of the environment including the security of identities, networks, servers, containers, email, user endpoints, and other systems.

It’s critical to ensure that security practices are being implemented consistently on each workload in production as well as on the production infrastructure itself. These are a few key controls that have an outsized impact.

### 8.1 Enforce multifactor authentication [8.1]

8.1 Enforce multifactor authentication - It's often said, attackers don’t break-in, they sign-in and it’s therefore necessary to enforce additional controls to help protect all users, especially administrators.  Multifactor Authentication adds a critical second layer of security to sign-ins to help protect access to data and applications while still providing a simple and efficient sign-in experience.

### 8.2 Protect administrative accounts [8.2]

8.2 Protect administrative accounts - At Microsoft, a combination of layered defenses are used to protect administrative access to production systems, including Secure Admin Workstations (SAWs), alternate credentials with MFA for administration, and Just in Time privilege elevation (JIT) with role-based access control (RBAC). For more on how to do this see:

### 8.3 Implement security baselines [8.3]

8.3 Implement security baselines - All operational environments need to have security baselines defined and enforced. These can be created as policies that detect drift from configuration standards and implement automated remediation

### 8.4 Create isolation layers [8.4]

8.4 Create isolation layers - Isolation layers refers to the various levels at which security controls are applied to ensure that systems are kept separate and secure, across process, compute, and network.

### 8.5 Use confidential compute [8.5]

8.5 Use confidential compute -  Isolate sensitive data while it's being processed in the cloud. Since the dawn of cloud computing in Azure, we’ve recognized the crucial role of HBV in running customer workloads on VMs. However, VMs only protect the host machine from malicious activity within the VM. In many cases, a vulnerability in the VM interface could allow a bad actor to escape to the host, and from there they could fully access other customers’ VM. Confidential Compute presents a new layer of defense against these attacks by preventing bad actors with hosting environment access from accessing the content running in a VM. Our goal is to leverage Confidential VMs and Confidential Containers broadly across Azure Services, adding this extra layer of defense to VMs and containers utilized by our services. This has the potential to reduce the blast radius of a compromise at any level in Azure. While ambitious, one day using Confidential Compute should be as ubiquitous as other best practices have become such as encryption in transit or encryption at rest.

### 8.6 Reduce the attack surface [8.6]

8.6 Reduce the attack surface - Attack surfaces are all the places where your organization is vulnerable to cyberthreats and attacks.

### 8.7 Perform platform penetration testing [8.7]

8.7 Perform platform penetration testing - Production running platform penetration testing, from physical data centers to cloud platforms.

### 8.8 Implement operational terminals [8.8]

8.8 Implement operational terminals: device security - Microsoft has a privileged access strategy that guides on implementing secure accounts, workstations and devices and interface security. Device control is extremely important because an attacker with access to a device can impersonate users on it or steal credentials for future impersonation. For strongest security for highest impact assets and accounts, we recommend using privileged access workstation (PAW). This is the highest security configuration designed for extremely sensitive roles that would have a significant or material impact on the organization if their account was compromised. The PAW configuration includes security controls and policies that restrict local administrative access and productivity tools to minimize the attack surface to only what is absolutely required for performing sensitive job tasks. This makes the PAW device difficult for attackers to compromise because it blocks the most common vector for phishing attacks: email and web browsing. To provide productivity to these users, separate accounts and workstations must be provided for productivity applications and web browsing. While inconvenient, this is a necessary control to protect users whose account could inflict damage to most or all resources in the organization.

### 8.9 Scheduled maintenance and automated patching cycles [8.9]

8.9 Scheduled maintenance and automated patching cycles - All systems must be continuously monitored and updated with the latest security updates.

### 8.10 Protect against DDoS attacks [8.10]

8.10 Protect against DDoS attacks - Provide real-time mitigation to common network-level attacks. Distributed denial of service (DDoS) attacks are some of the largest availability and security concerns facing cloud applications, because any endpoint that's publicly reachable over the internet can be targeted. To address this, at a minimum traffic must be continually monitored and real-time mitigations must be provided for common network-level attacks. However, as DDoS attacks become more sophisticated and targeted, it may also be necessary to provide DDoS mitigations to protocol and application layer attacks.

## Practice 9: Implement security monitoring and response [9]

*Practice 9 page (https://www.microsoft.com/en-us/securityengineering/sdl/practices/monitoring-and-response), introduction*

This practice focuses on maintaining continuous visibility into both the vulnerabilities attackers can exploit and anomalies that may be signs of an active attack. This is critically important to guide your risk mitigation efforts and to ensure you can detect, respond to, and recover from attacks.

This is often referred to as posture management or vulnerability management (for ‘left of bang' preventive measures) and security operations (SecOps/SOC) for ‘right of bang’ management of active incidents.

### 9.1 Proactively detect and address threats [9.1]

9.1 Proactively detect and address threats - Use a security analytics and threat intelligence platform to enable attack detection, threat visibility, proactive hunting, and threat response. This is often composed of extended detection and response (XDR) tools for well-known attacks, a security information and event management (SIEM) for building custom detections based on log files, and a Security Data Lake for long-term efficient storage of archival log files. A well-designed system for application, system, and security log files and other data sources is key to enable effective threat detection, investigation and forensic analysis, threat hunting, threat intelligence, and similar activities.

### 9.2 Establish a standard incident response process [9.2]

9.2 Establish a standard incident response process – Preparing an Incident Response Plan is crucial for helping to address new threats that can emerge over time. It should be created in coordination with your organization’s dedicated Product Security Incident Response Team (PSIRT). The plan should include who to contact in case of a security emergency, and establish the protocol for security servicing, including plans for code inherited from other groups within the organization and for third-party code. The incident response plan should be tested before it is needed!

## Practice 10: Provide security training [10]

*Practice 10 page (https://www.microsoft.com/en-us/securityengineering/sdl/practices/security-training), introduction*

You must ensure that anyone in the organization who makes decisions that impact security of applications understands the implications of that those decisions. This makes security part of almost everyone’s job in the development life cycle including users, developers, product line managers, testers, and more. Each of these roles must have education on security risks and their role in keeping the applications safe via formal training, on-demand training, simulation exercises, threat modeling, mentoring/advisors, security champions, purple team activities, podcasts, videos, or any other learning methods.

Since engineers building systems are not usually security experts, training in both the technical and conceptual aspects of threat modeling is necessary for them to become effective at it so they can build systems that are Secure by Design. This is also vital for the threat modeling process to work at-scale in organizations where developers far outnumber security professionals. Threat modeling must be thought of as a fundamental engineering skill in which all engineers must have at least basic proficiency. Therefore, engineering teams must be trained to be competent at threat modeling as part of onboarding and with periodic refreshers.

Ultimately, each role needs to understand why it’s important to address security risks, what they need to do for security in their role, and how to do those things. We have learned that people who understand the attacker’s perspective, their goals, and how that shows up in real world security incidents will quickly become security allies instead of trying to avoid security.

Security is an infinite game where the threats, technology, and business assets to protect are always changing and the attackers never give up so the security training approach should also be ongoing and continuously evolve. Effective training complements and re-enforce security policies, SDL practices, standards, and requirements of software security, and be guided by insights derived through data or newly available technical capabilities.

Although security is everyone’s job, it’s important to remember that not everyone needs to be a security expert nor strive to become a proficient penetration tester. However, ensuring everyone understands security basics and how to apply them to their role of building security into software and services is essential (including in the safe use of their computers and their identities and logon accounts).

In particular, developers and the Since engineers building systems are not usually security experts, so training in both the technical and conceptual aspects of threat modeling is necessary for them to become effective at it so they can build systems that are Secure by Design. This is also vital for the threat modeling process to work at-scale in organizations where developers far outnumber security professionals. Threat modeling must be thought of as a fundamental engineering skill in which all developers and engineers must have at least basic proficiency. Therefore, development and engineering teams must be trained to be competent at threat modeling as part of onboarding and with periodic refreshers.

## Legacy twelve-practice list (FAQ page, "Getting started")

The FAQ still answers "Which security activities should my organization perform in order to follow the Microsoft SDL process?" by pointing to the *Simplified Implementation of the Microsoft SDL* and listing:

- Provide Training
- Define Security Requirements
- Define Security Quality Bars and KPIs
- Use Threat Modeling
- Establish Design Requirements
- Encrypt Data Everywhere
- Use Secure Third-Party Components
- Use Approved Tools
- Perform Static Analysis Security Testing (SAST)
- Perform Dynamic Analysis Security Testing (DAST)
- Perform Penetration Testing
- Establish a Standard Incident Response Process for Your Organization

and answers "Should I use the Microsoft SDL Process Guidance as a resource to implement the SDL at my organization?" with "No. The Microsoft SDL Process Guidance illustrates the way Microsoft applies the SDL to its own technologies and software." (FAQ page). The Resources page files both documents under "Legacy archive".

