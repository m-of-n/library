---
schema: "library-distilled/v1"
id: enisa-sbd-playbook-2026-normative
record: enisa-sbd-playbook-2026
type: normative
updated: "2026-10-02"
---


# ENISA Secure by Design and Default Playbook v1.0 (July 2026) — normative content

Verbatim from `.cache/enisa-sbd-playbook-2026.txt` (pdftotext -layout; sha256 `c0dc5132…7c15`). CC BY 4.0, © ENISA 2026 — reproduced with attribution; changes: layout only (line breaks joined, two-column tables linearised). Non-binding guidance (Legal notice). Ids in `requirements.yaml`.

## 2 Secure by design and default across a product's life cycle (prescriptive parts)

2. Secure by design and default across a product’s life cycle

Secure by design and secure by default require more than applying principles during development. They must be operationalised end to end across the entire product life cycle, from the initial concept to the product’s eventual decommissioning. This life-cycle view is especially important for connected products; where evolving threats, supply-chain dependencies and long-lived deployments can erode security despite otherwise sound design if governance and assurance do not persist over time.

ENISA’s report Guidelines for Securing the Internet of Things highlights a common failure node: ‘Security goals can often fail – even in the presence of good design – if there is a lack of tools that enable stakeholders to understand and assess security issues’ (8). In practice, secure by design and default depends on both good engineering decisions and the organisational mechanisms (methods, artefacts, metrics and review gates) that make risk visible, decisions repeatable and trade-offs explicit.

### 2.1 Product life cycle

As highlighted in the ENISA report Baseline security recommendations for IoT in the context of critical information infrastructures (9), security must be considered throughout the entire product life cycle. Regardless of the production model used (V-model or agile), the following life-cycle processes require explicit security consideration to support product security.

- Requirements. As part of this process, user, business, functional and security requirements are determined. These requirements reflect the intended use of the product and will be translated into specifications that will guide design, development and maintenance/deployment decisions at later stages.

- Design. As part of the design process, the architecture and the design of the product are created. This process involves the creation of a set of documents that describe how the product requirements, including security requirements, will be translated into system specifications and essentially how the product will work.

- Implementation. As part of the implementation process, specifications and software design artefacts are implemented in the product.

- Verification: This process involves all necessary steps to verify that the developed product actually meets the identified requirements and design principles of the previous processes.

- Deployment. This process follows the acceptance of the product subject to successful testing as part of the previous processes – that is, it takes place after it has been approved for release. It involves integrating all necessary elements of the solution into the production environment and its deployment.

(8) ENISA, Guidelines for Securing the Internet of Things – Secure supply chain for IoT, 2020, https://www.enisa.europa.eu/sites/default/files/publications/ENISA%20Report%20- %20Guidelines%20for%20Securing%20the%20Internet%20of%20Things.pdf.

(9) ENISA, Baseline security recommendations for IoT in the context of critical information infrastructures, 2017, https://www.enisa.europa.eu/publications/baseline-security-recommendations-for-iot; see also ENISA, Good Practices for Security of IoT – Secure software development lifecycle, 2019, https://www.enisa.europa.eu/sites/default/files/publications/WP2019%20- %20O.1.1.1%20Good%20practices%20for%20security%20of%20IoT.pdf.

- Maintenance and disposal. Solutions deployed in production need to be constantly maintained to ensure the availability and integrity of the functionality provided. When the solution becomes obsolete, it is important to provide data erasure mechanisms that ensure secure disposal and preserve privacy management.

These processes are presented as groupings, not a mandatory sequential model. They may overlap, occur iteratively and be revisited throughout a product’s life cycle. For example, in agile environments, security requirements may be captured and progressively refined through backlog items, user stories, acceptance criteria and the definition of done.

Figure 1: Secure by design and default across a product’s life cycle

Figure 1 shows the relationships between the product life cycle, secure by design and default principles and risk management activities.

Risk management activities establish the security context by clarifying important considerations, including what needs to be protected, the threats of concern and the acceptable level of residual risk given the product’s intended purpose and security impact. Secure by design and default principles translate this context into practical security decisions that are applied throughout the processes of the product life cycle, from requirements through to end of life.

Risk management activities should be revisited in response to changes or events arising during the product life cycle. Similarly, while the product life-cycle processes are presented sequentially, both the life cycle and the application of secure by design and default principles across the processes are inherently iterative. Events or findings in later processes, such as testing results, deployment in new environments, incidents, discovered vulnerabilities or the implementation of new features, often require re-entry into earlier life-cycle processes.

Table 1: Cybersecurity activities during the product life cycle for SMEs

| Life-cycle process | Actions | Deliverables |
|---|---|---|
| Deciding on requirements | Define the product context (users, environments, data), non-negotiable security defaults, and top risks and threat scenarios; establish clear criteria for addressing risks, based on the product's intended purpose, expected use and security impact. | One-page security context and assumptions, short security requirements checklist (including secure defaults) |
| Design | Maintain one architecture diagram with trust boundaries; run a lightweight threat model to identify a manageable number of threat scenarios (e.g. the top 5 to 10); decide on the critical design controls (authentication/authorisation (a), update mechanism, secrets, logging). | Architecture and trust-boundary diagram, top threats and mitigations (bulleted list) |
| Implementation | Build secure defaults into code/config; enforce dependency hygiene; protect secrets; require review for security-sensitive changes; configure automated static application security testing (SAST) / dependency scanning as part of CI environments (agile /DevOps/DevSecOps). | CI evidence (pipeline logs), lightweight secure coding / checklist (often a repo file) |
| Verification | Run automated security checks (SAST / dependency scanning, basic dynamic application security testing (DAST) where relevant); ensure default configuration is validated; run targeted penetration testing when potential risk triggers are hit (e.g. in the case of a substantial modification). Run automated tests with high coverage that include security-relevant negative tests (verifying that what shouldn't happen doesn't happen). Note that security verification should be integrated into developer workflows and CI pipelines as early as possible (following the 'shift left' principle). | Release security checklist (pass/fail and exceptions) and documented known issues / residual risk |
| Deployment | Ensure secure provisioning/enrolment, least-privilege runtime config and monitoring of key health/security indicators; treat updates as controlled change management. | Deployment hardening checklist, rollback plan, minimal monitoring/alert list |
| Maintenance and disposal | Define a patch intake process and service-level agreements (SLAs), decide on vulnerability monitoring and incident handling processes and draw up an end-of-support/end-of-life plan; ensure secure disposal (data erasure, credential revocation). | Vulnerability and patch process guide (one page), end-of-life/disposal note, maintained risk register updates |

### 2.2 Risk management activities

Risk management activities provide the foundation for implementing secure by design and default across the product life cycle. They ensure that security decisions are based on an informed and shared understanding of what needs to be protected, from whom and under what constraints.

In this report, ‘risk management’ concerns cybersecurity risks affecting the product and the users, operators, customers, data, services and systems that depend on it, taking into account the product’s intended purpose and reasonably foreseeable use. It does not refer to the manufacturer’s commercial or reputational risk.

These activities establish the context within which secure by design and default principles are applied. Their outputs directly informs:

- security requirements and architecture decisions;

- default configuration and ‘out of the box’ hardening;

- prioritisation of controls and assurance activities (e.g. testing depth, review gates);

- acceptable trade-offs inherent to the product’s intended use and deployment context;

- the ongoing operational security posture, including patching and end-of-life handling.

Risk management is typically initiated early, but it must be iterative: revisited at defined life-cycle gates (e.g. major release, supplier change, new deployment context) and triggered by significant events (e.g. newly disclosed vulnerabilities, threat shifts, incident learnings). Examples of risk management activities directly supporting secure by design and default decisions include:

- product context definition, including intended purpose, operating environment, users, data processed, and constraints

- establishing risk acceptance criteria, expressed as simple and practical guidelines to support consistent decision-making;

- high-level risk assessment focused on threat modelling, key assets, trust boundaries and risk treatment decisions.

Risk assessments should also be informed by evidence from deployed products, including customer and researcher reports, incident investigations, observed exploitation patterns and proportionate telemetry, where available and appropriate.

This report does not aim to define or replace a formal risk management framework. Rather, it aims to highlight common risk management activities and outputs that feed security decision-making.

To support SMEs, the following list is a sample set of activities that can drive secure by design and default decisions without creating heavy processes. The purpose of these activities is to translate product context and credible threats into testable security requirements, prioritise the relevant playbooks and determine the appropriate depth of controls and assurance activities, rather than applying every practice uniformly.

Table 2: Risk management activities for SMEs

| Activity | Actions | Deliverables |
|---|---|---|
| Product context and scope | Define intended use, deployment environments, user/admin roles, data types/sensitivity and key external dependencies (cloud, mobile app, third parties). | One- or two-page 'product security context' note (scope, assumptions, dependencies) |
| Asset and adverse effect identification | List top data, hardware or function assets (e.g. credentials, customer data, essential functions) and key adverse effect outcomes (privacy breach, takeover, outage, fraud, safety impact). | Asset list and top adverse effects list (one page) |
| Lightweight threat modelling | See Section 2.3 | See Section 2.3 |
| Risk register | Record 10 to 30 risks using a simple, documented prioritisation method, with owner, treatment and status; link priority risks to backlog items/controls. The prioritisation method could take into account aspects like impact, likelihood, plausibility, exploitability or exposure, as appropriate. | Living risk register (spreadsheet or ticket board) |
| Risk acceptance criteria | Define a set of non-negotiable risk conditions (e.g. misuse of software updates, unauthorised administrative access and exploitation of default credentials are not acceptable) and establish criteria for accepting residual risk. For example, the accepted level of residual risk should not undermine the essential cybersecurity requirements, given the product's intended purpose and reasonably foreseeable use. | One-page risk acceptance and exceptions policy |
| Security requirements baseline | Translate top risks into testable 'must' requirements (authn/authz, secure defaults, secrets, encryption, logging, updates). | security requirements checklist (testable controls) |
| Release risk review gate | As part of the secure development life cycle, include a formal pre-release gate to verify compliance with the requirements defined during the above activities. This review should confirm checklist met, defaults verified, known vulnerabilities triaged, high risks treated / accepted with rationale; decide go/no-go. | Release security review record (ticket/comment) and documented exceptions |
| Change-triggered reassessment | Rerun context/threat/risk steps when major changes occur (architecture, auth model, data, critical dependencies/suppliers, deployment environment), including changes that could be considered substantial modifications, or after incidents. | Updated context note, threat shortlist and risk register entries (with date) |

Risk assessments can also support product-specific implementation of applicable cybersecurity requirements, assessment and treatment of identified vulnerabilities and evaluation of the security impact of significant changes to a product.

### 2.3 Threat modelling

Threat modelling is a structured activity that supports security decision-making and may inform risk assessment by helping teams identify credible threats and attack paths. Combined with the product context and an appropriate prioritisation method, the outputs can help in selecting appropriate security requirements and controls, including secure by default settings.

One commonly used approach to identifying and categorising security threats is STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service and Elevation of Privilege) (11). STRIDE is presented in this report as an illustrative example, but other suitable threat-modelling approaches may also be used(12).

Threat modelling should align with widely accepted threat-modelling principles (13), recognising that it is a collaborative and iterative activity focused on understanding and reducing real security risks, rather than simply producing documentation artefacts. Common anti-patterns to avoid include treating threat modelling as a one-off compliance exercise, over-engineering models that do not influence design or secure by default decisions and failing to review the model following substantial product modifications or changes in the threat landscape. For products incorporating artificial intelligence (AI) / machine learning (ML) components, threat identification should also consider relevant AI-specific attack patterns, such as prompt injection, model poisoning and adversarial inputs (14).

For SMEs, particularly those developing products intended for non-critical or lower-risk environments, the objective is not exhaustive analysis; it is a minimum viable model that is fast to produce, easy to refresh and tightly coupled to delivery (architecture decisions, default configuration and release gates).

A lightweight threat-modelling exercise can be organised around four questions (Shostack’s four- question framework) (15).

- What are we working on?

- What can go wrong?

- What are we going to do about it?

- Did we do a good enough job?

Table 3: Threat modelling for SMEs

| Activity | Actions | Deliverable |
|---|---|---|
| Define scope, assumptions and security objectives | Time-box a short scoping stage to make the exercise decision focused. Capture what is in and out of scope (e.g. devices, apps, cloud services, admin tools), the deployment context(s) and the assumptions and constraints you are working under (e.g. 'device may be physically accessible', 'customer network is untrusted', 'cloud APIs are internet-exposed', 'advanced user capabilities'). Then state the security objectives that matter for this product (e.g. confidentiality, integrity, availability, plus privacy/safety if applicable). | One-page (or equivalent ticket/wiki) 'Threat model scope and objectives' note, covering: purpose (what decisions this will drive); scope boundaries (components and environments); assumptions/constraints; security objectives and 'crown jewels' (what must not fail). |
| Model the system at a useful level of abstraction | Produce a simple representation of the system that answers Shostack's core question, 'What are we working on?' This may be an architecture diagram, a data-flow diagram or another suitable representation. It should show the main components, data stores, external entities, key data flows, entry points and trust boundaries in sufficient detail to assess exposure. Complementary techniques, such as misuse cases or attack trees, may also be used where helpful. Consider reusing the architecture and trust-boundary diagram developed during the design phase described in Table 1. | System representation, covering: main components (devices, apps, cloud services, APIs); external entities (users, admins, third-party services); data stores (device storage, cloud database, logs); entry points (APIs, admin UI, update channel, local ports); trust boundaries (where trust assumptions, privileges or security properties change). |
| Mark trust boundaries and privilege paths; identify key assets | Annotate the diagram with (a) trust boundaries (a) (boundaries between environments with different security properties) and (b) the highest-privilege operations (e.g. firmware / OTA updates, remote admin, key provisioning, identity issuance). This is the step that turns architecture into security-relevant architecture. | Diagram showing: trust boundaries (internet–back end, device–cloud, user–admin, tenant–tenant); privileged paths (updates, auth, key management, admin actions); top assets (credentials/keys, sensitive data, device control functions, availability). |
| Identify and prioritise the top threats | Generate a short list/representation of the answers to the question 'What can go wrong?', mapped to entry/exit points, data flows and trust boundaries (e.g. 'credential stuffing → account takeover → remote control', 'malicious update', 'API authorisation bypass', 'man-in-the-middle attacks during onboarding'). Prioritise them using a lightweight, documented method appropriate to the product. This might take into account impact, likelihood, plausibility, exploitability and exposure or use predefined severity criteria. OWASP (b) describes this as threat identification and ranking as a core step in most threat-modelling approaches. | Top threats table, showing: a manageable number of threat scenarios (e.g. the top 5 to 10) tied to specific entry/exit points and trust boundaries; priority or severity rating with a short rationale. Prioritised threat scenarios that drive design and default choices |
| Define mitigations and secure defaults, verify their effectiveness and set refresh triggers | Next, focus on 'What are we going to do about it?' For each top threat, specify the mitigation strategy, the required control(s) and the secure by default settings that the product should ship with (e.g. 'admin interface disabled by default', 'no default passwords', 'signed updates enforced', 'least-privilege roles', 'authentication attempts rate-limited'). Then map each control to how it will be verified (e.g. CI checks, tests, configuration validation, release gates), which will help to answer the question 'Did we do a good enough job?' Finally, define the triggers that require rerunning the model (e.g. a new internet-exposed interface, a new auth model, new sensitive data, a new critical dependency, a major architecture change). | Controls, defaults and verification checklist, including: Control/default decision for each top threat; test/verification mapping (automation first); explicit refresh triggers (so that the model stays current). |

A practical starting point could be to identify a small number of the highest-impact adverse-effect scenarios for users, operators or other affected parties and a manageable number of credible threat scenarios (e.g. the top 5 to 10) that could lead to them. These scenarios should be prioritised based on impact and likelihood. As part of their release review, teams should determine whether product changes affect the scenarios, assumptions or controls. Where products are intended for higher-risk or critical use cases, depending on the product’s intended use and associated risks, a more comprehensive analysis will be required.

Lightweight threat modelling does not necessarily require special threat-modelling expertise. Product expertise, on the other hand, is essential, because an accurate understanding of the product, its intended use and its deployment context is the foundation of a useful threat model. However, specialist security expertise is likely to be needed for higher-risk products or more complex threats.

Threat-modelling outputs can vary depending on aspects like the product’s scope, the assumptions, the methodology selected and analyst judgement. These inputs should be documented and applied consistently, to increase repeatability and support review.

Threat modelling and risk assessment should be revisited throughout the product lifecycle. For example, reviews could be performed at initial product design, implementation of the technical architecture, and verification, validation, maintenance and operation, where discovered vulnerabilities and field evidence can inform subsequent assessments.

## 3 Secure by design and default principles

3. Secure by design and default principles

Secure by design and secure by default provide a framework for building systems that are resilient and security hardened from the start and that remain so once released into real-world environments. ENISA’s report Good Practices for Security of IoT (SDLC) (16) describes secure by design as a ‘holistic approach’ that must be applied throughout the entire life cycle of a product or service.

Security is not a static state but a continuous process involving specific development guidelines, threat modelling and the integration of security controls during the earliest stages of design to minimise the impact of cyberattacks.

- Secure by design embeds protective measures into products during development, rather than adding them retrospectively. This includes threat modelling, secure architecture patterns, validated cryptography and systematic vulnerability management integrated into development processes.

- Secure by default ensures that products ship with the most secure configuration reasonably possible. Users should not need technical expertise to achieve baseline security; protective measures must be active upon installation, with any reduction requiring deliberate user action.

### 3.1 Secure by design principles

Secure by design focuses on incorporating security principles from the earliest stages of development. It requires organisations to embed security into the structure, logic and behaviour of a system rather than treating it as an afterthought. For the purposes of this playbook, secure by design is treated as a life-cycle approach. The principles are grouped into architectural foundations (how a system is built) and operational integrity (how it is managed and maintained) (Figure 2). These categories are practical organising lenses rather than mutually exclusive classifications, and some aspects of the principles contribute to both categories (17).

(16) ENISA, Good Practices for Security of IoT – Secure software development lifecycle, 2019, https://www.enisa.europa.eu/sites/default/files/publications/WP2019%20- %20O.1.1.1%20Good%20practices%20for%20security%20of%20IoT.pdf.

(17) For other frameworks and models, see NIST SP 800-160, Vol. 1, Rev. 1 (https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), and OWASP SAMM (https://owaspsamm.org/model/).

Figure 2: Secure by design principles

#### 3.1.1 Architectural foundations

Architectural foundations are the blueprints for a system’s security; they focus on the structural design choices that make a product inherently difficult to compromise or exploit. This category establishes the fundamental rules for how data flows, how components interact, and how the system contains a potential breach before it can spread.

The following principles fall under this category.

- Trust boundaries and threat modelling. These concepts reflect two related security principles: trust should be made explicit rather than assumed, and threats should be identified before and throughout development. Trust boundaries define where data, identities and execution contexts cross from a more trusted domain to a less trusted one (or vice versa), such as between a device and a cloud service, a user and an admin interface or one microservice and another. Boundaries clearly identify which components must authenticate each other, where input must be treated as untrusted and where additional controls (e.g. validation, rate limiting, encryption or isolation) are required. Threat modelling also provides a structured way to identify what could go wrong at these boundaries by mapping key assets (e.g. credentials, firmware images, customer data), likely threat actors and realistic attacker capabilities and assumptions.

- Least privilege. Systems and users should be granted only the feasible minimum level of access required to perform their functions. Restricting permissions reduces the impact and limits the scope of compromise. Least privilege should be applied consistently across user accounts, service accounts, APIs and administrative roles, and privileges should be elevated only when needed and for the shortest feasible duration.

- Strong identity and authentication architecture. A secure product architecture requires a clear and consistent approach for how identities are created, verified, and managed for users, devices, services, and administrators. This includes defining authoritative identity sources, establishing how authentication occurs across interfaces (e.g. web portals, APIs, local

management consoles and device-to-cloud communication) and ensuring that authentication is resistant to common attacks such as credential stuffing, replay attacks and session hijacking.

- Attack surface minimisation. Unnecessary features, services and interfaces increase the number of potential attack vectors. Therefore, reducing system complexity and disabling unused or unnecessary components reduces the likelihood of vulnerabilities being introduced or exploited. This includes removing default accounts, uninstalling unused packages, closing non- essential ports, removing unused code and limiting exposed management interfaces to trusted networks only. Standardised secure baselines and hardened configuration templates make it easier to keep systems consistently minimal as they scale. Ongoing vulnerability scanning and asset inventory are also important, because you cannot minimise what you do not know exists.

- Defence in depth. Applying layered security controls ensures that the failure of a single mechanism does not result in complete compromise. Layers can include preventive controls (e.g. multi-factor authentication (MFA), network segmentation), detective controls (e.g. monitoring, logging, anomaly detection) and corrective controls (e.g. automated isolation, backup/restore). Effective defence in depth also assumes that some controls will be bypassed, so systems should be designed to degrade gracefully and still protect critical assets. This approach reduces reliance on any single silver bullet and increases the attacker’s cost and time to achieve their objectives. It is strongest when controls are diverse (not all dependent on the same technology or trust assumption).

- Open design (avoiding obscurity). Systems should not depend on secrecy of design or hidden behaviour for protection. Security controls should remain effective even if an adversary understands how the system operates. This principle encourages the use of well-studied algorithms and protocols, clear documentation and designs that can withstand scrutiny through review and testing. Open design does not mean making secrets public; rather, it means that the security of the product should rest on protected keys, strong authentication and robust implementation, not on keeping the mechanism itself hidden. In practice, it also supports maintainability, because transparent designs are easier to audit, validate and improve over time.

#### 3.1.2 Operational integrity

Operational integrity addresses the human and procedural practices that maintain product security throughout development, deployment, operation and retirement. It ensures that security is treated as a continuous, lived experience, for developers and users alike, rather than a one-time checklist completed during the design phase.

This category includes the following principles.

- Life-cycle management. Security responsibilities extend beyond initial development. Components must be maintained, updated and eventually retired in a controlled manner, taking the expected duration of use into account. The practical application of life-cycle management, including how secure by design and secure by default principles are applied from design and development through to decommissioning, is explored in Section 2.

- User-centric design. Security mechanisms must be usable and understandable even for everyday users. Poor usability often leads to insecure workarounds or misconfigurations. For example, if a system requires the user to perform complex manual configuration to enable encryption, they may skip the step or apply it incorrectly. On the other hand, providing a simple, guided set-up that enables encryption automatically reduces the chance of misconfiguration and encourages the use of the security feature.

- Secure coding and verification practices. Developers should follow established secure coding standards to prevent common vulnerabilities. Early identification and mitigation of

insecure code ensure that weaknesses are not built into the system. For example, developers can use SAST tools (18) while coding to identify vulnerabilities and software composition analysis to detect vulnerable third-party libraries. They can then apply dynamic testing tools (19) (DAST) before deployment to uncover runtime issues. These practices ensure that code-related vulnerabilities are identified early and not after the product is released.

- Logging, monitoring and alerting. Security depends on visibility. Systems should generate appropriate security-relevant logs, retain them for a defined period and protect them from tampering, so that they can support investigation and compliance needs. Rather than simply collecting data, monitoring should be designed to detect suspicious behaviours such as repeated failed authentication attempts, privilege escalation, unexpected configuration changes and unusual outbound connections.

- Configuration and change management. Secure operation requires configurations to be controlled, consistent and auditable. Baseline hardening standards should be defined (e.g. secure defaults, disabled unused services and enforced encryption settings) and applied through repeatable mechanisms such as templates and infrastructure as code to reduce drift. Changes to systems should follow a governed process that includes review, testing, approval and rollback plans, particularly for security-sensitive components.

- Incident response and recovery. Developers must be prepared to respond quickly and effectively to security incidents that affect their products in the field, including vulnerabilities, compromised code, malicious updates and misuse of product functionality. This requires defined internal roles, escalation paths and decision-making authority for security events, as well as documented playbooks for containment and customer communication.

- Vulnerability and patch management. Vulnerability and patch management should be practical, repeatable and prioritised by risk. Manufacturers need a simple way for customers and researchers to report issues (e.g. a dedicated security email address and a basic disclosure process) and an internal process to triage findings quickly and decide what needs urgent action.

- Supply-chain controls. Developers and manufacturers should protect product integrity without excessive process overhead, focusing on the points where a compromise would have the largest impact: code repositories, build systems, signing keys and the channels used to distribute updates. At a minimum, source code and CI/CD modification rights should be limited to named individuals, protected with MFA and reviewed through lightweight peer approval for changes to security-critical areas. Software bills of materials (SBOMs) should be generated and maintained to support dependency transparency, vulnerability management and product life- cycle security.

### 3.2 Secure by default principles

Secure by default complements secure by design by focusing on the product’s security configuration presented to the user. Even well-designed systems can become vulnerable if they are released with insecure or overly permissive default settings.

The goal of secure by default is to minimise the attack surface after deployment by ensuring that the most secure configuration is applied automatically (20). This includes disabling unnecessary services, applying restrictive access controls and providing clear information to users about the default security

(18) https://owasp.org/www-community/Source_Code_Analysis_Tools.

(19) https://owasp.org/www-community/Vulnerability_Scanning_Tools.

(20) Other useful references that cover the topic include ETSI EN 303 645 (https://www.etsi.org/deliver/etsi_en/303600_303699/303645/03.01.03_60/en_303645v030103p.pdf) and NIST SP 800- 213 (https://csrc.nist.gov/pubs/sp/800/213/final).

posture. Secure defaults reduce reliance on user expertise and limit the potential for misconfigurations, which are a common source of security incidents.

To summarise, secure by design focuses on how the system is engineered, while secure by default focuses on how the system arrives and behaves when the user first turns it on. We can organise secure by default into two distinct categories: default hardening and guided protection (Figure 3). These categories are practical organising lenses. Some principles contribute both to the product’s initial secure state and to maintaining that state during use.

Figure 3: Secure by default principles

#### 3.2.1 Default hardening

Default hardening focuses on the factory-shipped state of the software, ensuring that the initial configuration is as restrictive as possible. It aims to eliminate low-hanging fruit for attackers by removing unnecessary features and ensuring that all active components are operating at their highest security level without requiring any user input.

- Minimisation of default services. Any feature or service that is not essential for the core functionality of the product should be disabled by default. If a web server includes an optional file-sharing module that most users will not need, that module should be off until the user explicitly opts in, thereby reducing the immediate attack surface.

- Restrictive initial access. Systems should ship with the most restrictive permissions possible. This includes the elimination of universal ‘admin/admin’ credentials and the enforcement of unique passwords and mandatory password changes upon first boot.

- Secure communication by default. All external communications should be encrypted and authenticated from the first connection. Rather than allowing an unencrypted HTTP or Telnet connection for convenience, the system should strictly enforce protocols like TLS 1.3 or SSH, ensuring that data is protected the moment it leaves the device.

- Unique device identity and secrets by default. The product should ship with unique, per- device credentials and cryptographic identity (keys/certificates) rather than shared defaults. Any secrets used for authentication, update verification or encrypted communications must be generated uniquely and protected against extraction. This reduces the risk that compromise of a single device or a leaked credential could be used to attack other customers or the wider installed base.

#### 3.2.2 Guided protection

Guided protection addresses the interaction between the user and the system’s security features. It acknowledges that human error is a primary cause of breaches and uses automated prompts,

mandatory set-up steps and clear feedback to ensure that the user cannot easily or accidentally leave the system in an insecure state.

- Mandatory security onboarding. Critical security features should not be hidden in a settings menu; they should be part of the initial set-up wizard. For instance, requiring a user to configure MFA or an encryption key during the first-run experience ensures that the system enters a secure state before it is exposed to the internet.

- Automated maintenance and updates. A secure default posture must be sustainable. By enabling automatic security updates by default, the manufacturer ensures that the product remains protected against newly discovered vulnerabilities without requiring the SME to have a dedicated IT team to manually manage patching cycles.

- Transparent security posture. The system should clearly communicate its security status to the user. If a user chooses to disable a security feature or if a specific configuration increases risk, the system must provide a clear, understandable warning and offer a one-click path to return to the secure baseline.

- Secure recovery and ownership life cycle. The product should provide guided, low-friction recovery and transfer processes (credential reset, account recovery, secure factory reset and ownership transfer) that are simple for users to follow but resistant to account takeover and social engineering.

## 4 Playbooks

4. Playbooks

These playbooks provide a practical, lightweight way for small and medium-sized manufacturers and product teams to implement secure by design and secure by default principles without creating a heavy governance burden. Each playbook distils a single security principle into a one-page, execution-focused guide that teams can apply repeatedly across releases and product lines.

The intention is to translate security principles from abstract aspirations into concrete engineering and operational actions, with clear expectations, verifiable outcomes and a consistent definition of done for security. Each playbook follows the same format to make adoption fast and repeatable.

- Principle. The security concept being implemented.

- Objective. What the principle is trying to achieve and what failure modes it reduces.

- Checklist. The highest-impact actions to implement (designed to be achievable in lean teams).

- Minimum evidence. The smallest set of artefacts/logs/configurations that demonstrate that the checklist has been implemented.

- Release gate. A copy and paste set of pass or fail criteria that can be used in a release review (or CI/CD). Teams should apply the criteria relevant to the release and confirm that the controls continue to operate as intended where the release could affect them.

This structure is deliberately aligned with how SMEs operate: short cycles, shared responsibilities, limited specialist capacity and a need for guidance with a high signal-to-noise ratio. Unless stated otherwise, the actions in the playbooks are directed at manufacturers and teams acting on their behalf. References to users and operators describe product capabilities, information or actions that manufacturers should enable or support.

Developers and manufacturers should consider the following guidance when using the playbooks.

- Treat each playbook’s release gate as a standard agenda item in release readiness

- Implement the minimum evidence as repository artefacts and CI outputs wherever possible.

- Use the product changes, threat model and risk assessment to determine which release-gate criteria require verification. Unchanged controls may be recorded as not affected.

- Reuse the same evidence across playbooks where appropriate. For example, a single SBOM, scan result or release record may satisfy related evidence requirements and release-gate criteria for more than one playbook.

- Allow exceptions only with a documented rationale, owner and review date.

- Refresh playbooks periodically based on incident learnings, vulnerability trends and product changes.

It is important to note that the items listed under ‘Minimum evidence’ do not necessarily require separate documents or artefacts. A single item of evidence may support several playbooks. Organisations should reuse existing engineering records wherever possible, including architecture diagrams, repository files, configuration records, issue-tracking tickets, test results, SBOMs, CI/CD outputs and release records.

The contents of this section should be treated as a baseline rather than a final state. As products evolve, risks change and new features are introduced, the content should be reviewed and updated to ensure that secure by design and secure by default remain effective over time.

The playbooks can be adopted progressively, prioritising those most relevant to the product’s risks, intended use and development context. Progressive adoption does not imply delaying any applicable requirements or controls, including those arising from legal obligations under the CRA. A suggested approach is provided at the end of this section.

### 4.1 Trust boundaries and threat modelling

**Principle** (secure by design): Secure architectures make trust explicit rather than assumed. Trust boundaries define where data, identities and execution contexts cross from a more trusted domain to a less trusted one (or vice versa).

**Objective:** Ensure that the system’s architecture and data flows are understood, trust assumptions are explicit and the highest-risk attack paths are identified early, so that security controls and secure defaults are designed in, not retrofitted.

**Checklist**

- *Draw the system (one diagram)*
  - Include users/admins, device/app, back-end services, APIs, data stores, third parties.
  - Show key data flows and entry points (APIs, admin UI, OTA/update channel, local ports).
- *Mark trust boundaries and privileged paths*
  - Identify where trust changes (internet–back end, tenant–tenant, device–cloud, user– admin).
  - Highlight high-privilege flows (auth, key management, updates, admin actions).
- *List critical assets*
  - For instance, list credentials/keys, customer / personally identifiable information, payment tokens, device control functions, availability, audit logs, data, source code and the IDE.
- *Identify and prioritise top threats*
  - Map threats to the relevant entry/exit points, data flows, assets and trust boundaries, for example account takeover, malicious updates, API authorisation bypass, man-in-the-middle attacks and the tampering with, replay of or injection of fabricated or stale data and commands.
  - Assign a high, medium or low priority using a documented method appropriate to the product, such as assessing impact, likelihood, plausibility, exploitability and exposure.
- *Define mitigations, secure defaults and verification*
  - For each top threat: required controls and default configuration (deny by default, authn/authz, segmentation, signed updates, rate limits).
  - Map each control to a verification method (tests, CI checks, config validation).
  - Define refresh triggers (new interface, auth change, new sensitive data, new critical dependency, major architecture change).

**Minimum evidence**

- One architecture/data-flow diagram with trust boundaries and entry points (stored in repo/wiki)
- Top threats list (e.g. the top 5 to 10 threat scenarios) with H/M/L priority and owners
- Control/default mapping for each top threat (what control, where enforced, how verified)
- Verification evidence: CI outputs or test results for key negative tests (unauthorised calls fail)

**Release gate**

- [ ] Diagram updated for this release (components, flows, dependencies reflect reality)
- [ ] Trust boundaries and privileged paths clearly marked
- [ ] Top threat scenarios reviewed; high risks have mitigations or documented exceptions
- [ ] Secure defaults confirmed for new/exposed interfaces (deny by default, least privilege)
- [ ] Verification in place: at least one negative test per critical boundary / privileged path (unauthorised access is denied)
- [ ] Threat model refresh triggered if any of the following are relevant: new API/interface, auth model change, new sensitive data, major dependency/supplier change, OTA/update changes, major architecture change.

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.1: Supports identification and assessment of cybersecurity risks by making trust assumptions, assets and attack paths explicit during design
- ANNEX-1.PT1.2.d: Supports protection from unauthorised access by clarifying where authentication and access controls are required between trust boundaries
- ANNEX-1.PT1.2.e: Supports confidentiality protections by identifying where data crosses trust boundaries and requires protection
- ANNEX-1.PT1.2.f: Supports integrity protection by identifying where data, commands or configuration cross boundaries and may require integrity controls
- ANNEX-1.PT1.2.j: Supports attack surface limitation by identifying exposed interfaces and unnecessary trust relationships

### 4.2 Least privilege

**Principle** (secure by design): Every user, service and process operates with the feasible minimum permissions needed to do its job – no more and for no longer than necessary.

**Objective:** Reduces unauthorised access, limits blast radius, blocks lateral movement and prevents permission creep.

**Checklist**

- *Define minimum viable permissions for each role/service*
  - List key roles (user, support, admin) and key services (API, provisioning, updates).
  - For each, define allowed actions (read/write/admin) and resources (APIs, tables, buckets).
- *Use unique identities (no shared admin)*
  - One identity per service (service account/workload identity) , applicable to both web services and services running on a device.
  - No shared admin users/keys; separate dev/test/prod identities.
- *Default-deny and explicit allow lists*
  - Deny by default; allow only required API methods, data access and network paths.
  - Restrict service-to-service access to specific interfaces.
- *Time-bound admin access (JIT) + attribution*
  - Named accounts + MFA for admins (all human users if possible).
  - Temporary elevation for privileged actions; break-glass is separate and monitored.
- *Automate privilege hygiene*
  - Monthly (or at each release), flag broad privileges and unused permissions/tokens; remove or time-limit exceptions.

**Minimum evidence**

- Access model exists: for example, a short table “Role/Service, allowed actions, resources” stored in repo/wiki and kept current.
- No shared admin: IAM inventory shows unique service identities; no reused production admin keys.
- Deny works: automated negative tests prove unauthorised API/data access is blocked for each critical service.
- Admins are accountable: logs show who performed privileged actions; elevation expires automatically.
- Creep is controlled: recurring report flags unused/broad permissions; removals/exceptions are tracked, with owner and expiry.

**Release gate**

- [ ] Unique service identities; no shared production admin keys
- [ ] Default-deny posture; only required paths enabled
- [ ] Admin access uses MFA and is time bound and logged
- [ ] Automated authorisation tests run verifying correct access restrictions for critical privileged functions
- [ ] Privilege review run; exceptions owned and time limited

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.d: Supports protection from unauthorised access by limiting what authenticated users, services and processes are permitted to access or perform
- ANNEX-1.PT1.2.f: Supports integrity protection by limiting which identities are authorised to modify data, programs or configuration
- ANNEX-1.PT1.2.g: Supports data minimisation by limiting access to data to what is necessary for the intended purpose

### 4.3 Strong identity and authentication architecture

**Principle** (secure by design): Design identity and authentication as a core part of the architecture. Use authoritative identity mechanisms for users, devices, services and administrators across interfaces.

**Objective:** Prevent impersonation and unauthorised access.

**Checklist**

- *Define authoritative identity sources*
  - Identify and document the authoritative identity source (i.e. a system that acts as the single source of truth for creating, authentication/authorisation, and revoking identities) for users, devices, services and administrators.
- *Use unique identities for all actors*
  - Assign a unique identity to each user, device, service and administrator, prohibiting shared accounts/credentials, especially for administrative and service access.
- *Apply authentication across all interfaces*
  - Enforce authentication/authorisation on all access paths, including user interfaces, APIs, device-to-cloud communication and management interfaces.
- *Strengthen authentication for high-risk access*
  - Require stronger authentication for privileged actions and sensitive operations (e.g. MFA, device binding, or cryptographic credentials).
- *Manage sessions and credentials securely*
  - Ensure that sessions are time limited, bound to identity and invalidated on logout or credential change.
  - Rotate, revoke and expire credentials automatically when no longer needed or when compromise is suspected.

**Minimum evidence**

- Authoritative identity sources defined: a diagram or table exists showing the identity source for users, devices, services and administrators.
- No shared identities: identity inventory shows unique identities, no shared production accounts or credentials.
- Authentication enforced: configuration or test evidence shows that all interfaces enforce authentication or are explicitly defined as public with appropriate protections applied. Network location or reachability alone is not treated as authentication, unless explicitly justified by the product context and risk assessment and supported by appropriate compensating controls.
- Strong auth for privileged access: policy or configuration shows that MFA or equivalent is enforced for administrative or sensitive actions.
- Sessions and credentials controlled: configuration or logs show session expiry, revocation on logout or credential change, and credential rotation or expiry in place.

**Release gate**

- [ ] Authoritative identity sources defined and documented
- [ ] Unique identities enforced; no shared production accounts or credentials
- [ ] Authentication required on all access paths (UI, APIs, device-to-cloud, management interfaces)
- [ ] Strong authentication enforced for privileged or sensitive actions
- [ ] Sessions and credentials are time limited, revocable and expire automatically

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.d: Supports access protection by defining how identities are authenticated and managed across interfaces
- ANNEX-1.PT1.2.l: Supports logging and monitoring of authentication and access-related activity

### 4.4 Attack surface minimisation

**Principle** (secure by design): Expose only what is strictly necessary. Remove or disable all unnecessary code, services, interfaces, protocols and dependencies by default.

**Objective:** Reduce the likelihood and impact of compromise by eliminating unnecessary entry points and limiting attacker options.

**Checklist**

- *List exposed interfaces*
  - Identify all externally reachable APIs, ports, local interfaces (HMI), protocols, admin endpoints and update channels.
  - Remove or disable anything without a clear, current justification.
- *Enforce default deny*
  - Close all ports, APIs and interfaces by default.
  - Explicitly allow only what is required for production.
- *Remove development and diagnostic functionality*
  - Remove debuggers, test endpoints and debug modes from production builds.
  - Remove development features.
- *Minimise dependencies*
  - Remove unused libraries, SDKs and optional components from final builds. Remaining libraries should be verified for authenticity and integrity.
  - Use the smallest possible operating system, runtime or firmware configuration that supports the product’s intended function.
- *Continuously monitor for legacy exposure*
  - Continuously review exposed interfaces and dependencies.
  - Update/remove deprecated APIs, old protocols and unused resources.
- *Minimise data collection, processing and retention*
  - Collect, retain and store only the personal or sensitive data necessary for the product’s intended purpose and securely delete it when no longer required.

**Minimum evidence**

- Exposure inventory exists: a maintained list of externally reachable interfaces (APIs, ports, protocols, admin interfaces, update channels) is stored in the repo or product documentation.
- Default deny enforced: network rules, gateway configuration or device settings show that only explicitly required interfaces are enabled in production.
- Minimal build verified: build configuration, manifest, package list or firmware contents show that only required components are included.
- No dev or diagnostic tooling shipped that might enable exploitation: inspection of production artefacts confirms absence (or verification that they cannot impact security) of shells, debuggers, compilers, test interfaces and diagnostic utilities.
- No legacy exposure: release notes, ticket or checklist entry confirms that exposed interfaces and dependencies were reviewed and any unused or legacy elements removed.
- Data inventory and retention record: data inventory with purposes, retention periods and deletion methods is kept.

**Release gate**

- [ ] Exposed interfaces reviewed; only required APIs, ports, protocols and management interfaces enabled
- [ ] Default-deny posture confirmed; no unintended network paths or interfaces exposed
- [ ] Production build is minimal; unused libraries, services and optional components removed
- [ ] No development or diagnostic tools present in production unless there is evidence that it cannot impact security
- [ ] Attack surface review completed for this release; deprecated or legacy interfaces updates/removed
- [ ] Unnecessary data processing has been removed and required deletion mechanisms verified

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.b: Supports secure by default configuration by reducing enabled features and services at initial deployment
- ANNEX-1.PT1.2.j: Supports attack surface limitation by reducing unnecessary interfaces, services and exposed functionality

### 4.5 Defence in depth

**Principle** (secure by design): Apply multiple layers of security so that the failure or bypass of a single control does not result in full compromise.

**Objective:** Reduce the impact of security failures by layering independent controls that slow attackers, increase detection and prevent single points of compromise.

**Checklist**

- *Layer controls around critical assets*
  - Identify the most sensitive assets (e.g. credentials, control functions, customer data).
  - Ensure that more than one independent control protects each asset.
  - Where critical data or commands cross trust boundaries, consider integrity and freshness controls that remain effective if another protection layer, such as transport security, is bypassed.
- *Assume control failure and design for containment*
  - Design systems so that bypass of one control does not grant unrestricted access.
- *Enable detection at multiple layers*
  - Generate security-relevant logs at key layers (identity, network, application, data).
  - Ensure that failed and suspicious actions raise alerts and are not silently blocked.
- *Use diverse and independent controls*
  - Avoid relying on multiple controls that share the same technology, identity source or trust assumption.
- *Slow attackers and enable response*
  - Apply controls that increase attacker effort and time (rate limits, step-up authentication, staged access).
  - Ensure that response mechanisms exist to contain or isolate compromised components when alerts are triggered.

**Minimum evidence**

- Layered protection mapped: a simple table or diagram showing critical assets and the multiple security controls protecting each (stored in repo/wiki).
- Independent controls confirmed: configuration or design notes showing that layered controls do not rely on the same identity source or enforcement point.
- Multilayer logging enabled: log configuration or sample logs showing security events recorded across controls.
- Alerts and response defined: alert rules or playbook reference showing how suspicious activity is detected and the associated containment or response action.

**Release gate**

- [ ] Critical assets have more than one security control applied and the layering is documented.
- [ ] Layered controls are independent; no single identity source or enforcement point is a single point of failure.
- [ ] Security-relevant events are logged at multiple layers
- [ ] Alerts are in place for suspicious activity and a response action exists

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.h: Supports availability and resilience by relying on multiple layers of protection rather than a single control
- ANNEX-1.PT1.2.k: Supports impact reduction by applying multiple mitigation mechanisms that limit the effect of exploitation

### 4.6 Open design

**Principle** (secure by design): Systems should not depend on secrecy of design or hidden behaviour for protection. Security controls should remain effective even if an adversary understands how the system operates.

**Objective:** Ensure that the product’s security does not depend on the secrecy of its design or implementation details (‘security through obscurity’). Open design makes security properties reviewable, testable and maintainable.

**Checklist**

- *Document security-relevant design decisions*
  - Keep a short security design note covering trust boundaries, auth model, cryptographic usage, update mechanism, logging/audit approach and secure defaults.
  - Record the rationale for ‘why this control/protocol/library’.
- *Prefer open standards and proven building blocks*
  - Use standard, widely reviewed protocols and libraries (e.g. TLS, OAuth/OIDC, JWT with clear constraints, signed updates).
  - Avoid proprietary crypto, “home-grown” protocols, and undocumented encodings for security-critical flows.
- *Make interfaces and security expectations explicit*
  - Document APIs, authentication/authorisation requirements, error handling, rate limits and supported configurations.
  - Provide a secure configuration guide (outlining what must be enabled and disabled in production).
- *Enable review and disclosure*
  - Establish a vulnerability disclosure channel (security contact, intake process, basic triage/response targets).
  - Encourage internal peer review for security-sensitive changes (to auth, updates, crypto, boundary-crossing interfaces).
- *Maintain transparency of components and changes*
  - Maintain, publish and sign an SBOM (at least for customer-facing builds) and track third-party components.
  - Keep a security changelog / release notes for security-impacting fixes and default-setting changes.

**Minimum evidence**

- Security design note (1–3 pages), covering boundaries, auth, crypto choices, update path, logging, secure defaults
- API + security requirements documentation (authn/authz, rate limits, data-handling expectations)
- Secure configuration guide (production hardening defaults, required settings)
- Vulnerability disclosure process (public email / web page or customer-facing channel; triage ownership defined)
- SBOM (exported file or tool output) + dependency -tracking approach
- Security-sensitive PR review rule (CODEOWNERS file, repo policy or checklist evidence)

**Release gate**

- [ ] Security design note updated for any architectural/security-relevant change (auth, crypto, update path, trust boundaries)
- [ ] No custom/proprietary crypto or undocumented security-critical protocols introduced
- [ ] API/security documentation updated (auth requirements, scopes/roles, rate limits, secure defaults)
- [ ] Secure configuration guide updated; defaults validated for new/exposed interfaces
- [ ] SBOM generated for the release and stored/published per policy
- [ ] Vulnerability disclosure channel tested (contact works) and ownership/triage defined

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT2.3: Supports effective testing and review by using designs that can be examined and assessed
- ANNEX-1.PT2.4: Supports vulnerability disclosure by aligning with transparent communication of security issues and fixes

### 4.7 Life-cycle management

**Principle** (secure by design): Security responsibilities extend beyond initial development. Components must be maintained, updated and eventually retired in a controlled manner.

**Objective:** Ensure that security is maintained throughout the product’s full life cycle, from requirements and design through to deployment, maintenance and end of life, so that security does not degrade over time.

**Checklist**

- *Define support commitments and life-cycle states*
  - Publish (internally or externally) life-cycle states: active, maintenance, end of sale, end of support, end of life.
  - Define minimum support windows and internal guidelines for vulnerability triage and patch release timelines (e.g. critical vulnerabilities triaged in 48 hours; fixes released within X days where feasible).
- *Make the product updatable and recoverable*
  - Implement a secure and transactional update mechanism (authenticated updates, integrity protected, rollback/recovery plan).
  - Ensure safe failure modes (do not brick devices; provide fallback/rollback where practical).
  - During maintenance or recovery modes, restrict functionality and privileges to the minimum necessary to support update and recovery operations.
- *Operate vulnerability and patch management*
  - Track vulnerabilities from third-party components, internal findings and customer reports.
  - Maintain an SBOM (at least for each release) and a dependency update cadence.
  - Triage, prioritise and document risk decisions (fix, mitigate, accept with expiry date).
- *Monitor, log and handle incidents*
  - Enable security-relevant logging (auth events, admin actions, update events, boundary-crossing requests).
  - Define minimum incident response steps, for instance detection, triage, containment, remediation, customer communication
- *Learn from deployed products*
  - Collect evidence on how products are deployed and used, such as customer feedback, support cases, vulnerability reports, incident findings and privacy-preserving telemetry where appropriate.
  - Review findings, including the results of root-cause analyses where applicable, and update the product context, risk assessment, threat model and secure defaults as necessary.
- *Plan secure decommissioning and disposal*
  - Provide data erasure mechanisms and guidance (factory reset, key revocation, account deprovisioning).
  - Revoke credentials/keys when devices/users/services are deactivated.
  - Ensure that end-of-life guidance includes what security updates cease and what customers must do.

**Minimum evidence**

- Life-cycle policy: lifecycle states + support window + patch SLAs (1 page).
- Update/release process: secure update approach and rollback/recovery notes
- Vulnerability management log: intake, triage, prioritisation, disposition, owner, dates (ticket board or spreadsheet)
- SBOM: SBOM generated in a machine-readable, widely adopted standard format (e.g. SPDX or CycloneDX) and stored with the release
- Monitoring and logging: security logging baseline + sample logs showing admin/auth/update events
- Field feedback record: summary of relevant operational evidence reviewed, deviations from deployment assumptions identified and resulting actions
- Decommissioning checklist: data wipe/reset, credential/key revocation and customer guidance

**Release gate**

- [ ] Support status and life-cycle state for this release are clear (active, maintenance, etc.)
- [ ] Secure update path validated (integrity/authentication checks, rollback/recovery documented)
- [ ] Vulnerability triage completed for known issues (including third-party dependencies); decisions recorded (fix/mitigate/accept with expiry)
- [ ] SBOM generated (or dependency inventory updated) and stored for the release
- [ ] Security logging verified for critical events (authentication, admin actions, updates)
- [ ] Decommissioning actions defined for components introduced/changed (e.g. reset, wipe, key revocation)
- [ ] Any accepted residual security risk has an owner and review/expiry date

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.c: Supports the ability to address vulnerabilities over the product lifetime through updates
- ANNEX-1.PT1.2.m: Supports secure decommissioning by providing mechanisms to remove data and settings at end of use
- ANNEX-1.PT2.2: Supports timely remediation of vulnerabilities throughout the supported life cycle
- ANNEX-1.PT2.7: Supports controlled and secure distribution of updates over time

### 4.8 User-centric design

**Principle** (secure by design): Security mechanisms must be usable and understandable even for everyday users.

**Objective:** Ensure that security controls and secure defaults are usable, understandable and aligned with real user workflows, so that security outcomes do not depend on expert behaviour.

**Checklist**

- *Design secure defaults that require minimal user action*
  - Ship with the safest practical settings enabled (e.g. least exposure, secure communications, logging enabled).
  - Avoid optional security for critical protections; make insecure modes explicit and gated.
- *Make set-up and onboarding safe and simple*
  - Provide a guided first-run experience with clear security steps (e.g. change initial credentials, pair securely, enable updates).
  - Minimise manual configuration for sensitive settings; prefer automated secure provisioning.
- *Use clear, actionable security messaging*
  - Write user-facing warnings and error messages that explain what happened, the impact and what to do next.
  - Avoid vague messages (‘failed’) or blame-the-user language; include remediation steps.
- *Provide least-friction access management*
  - Prefer role-based access and simple permission models that match user roles (e.g. admin, operator, viewer).
  - Support safer auth options where feasible (e.g. MFA for admins, device identity, short-lived tokens).
  - Remove/limit insecure recovery paths; make account recovery robust.
- *Validate usability to prevent insecure workarounds*
  - Run quick usability checks on key security flows (onboarding, password reset, admin tasks, updates).
  - Use support tickets and pseudonymised telemetry (where appropriate) to detect confusion and misconfiguration trends.

**Minimum evidence**

- Secure defaults list (what ships enabled and disabled, with rationale)
- Onboarding / security set-up guide (short, step-by-step, including credentials and update steps)
- Roles/permissions model (roles defined + what each can do)
- User-facing security message catalogue (examples of warnings / error messages and text outlining required remediation measures)
- Usability validation notes (at least three to five users or internal proxies) covering the top security flows, plus resulting fixes

**Release gate**

- [ ] Secure defaults reviewed and validated (no critical protections disabled by default)
- [ ] No default admin credentials active; onboarding enforces safe initial set-up
- [ ] Admin/security-critical actions have clear UX (confirmations, guidance and safe recovery paths)
- [ ] Roles and permissions match real user workflows; privilege escalation is explicit and auditable
- [ ] Security warnings / error messages are actionable (what, why, how to fix) and documented
- [ ] Basic usability check completed for key security flows (onboarding, admin tasks, recovery, updates); issues tracked/fixed or accepted with owner + date

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.b: Supports secure by default configuration that users can reasonably adopt and maintain

### 4.9 Secure coding and verification practices

**Principle** (secure by design): Developers should follow established secure coding standards to prevent common vulnerabilities.

**Objective:** Reduce common, high-impact vulnerabilities by eliminating relevant weakness classes through architectural and technology choices, where feasible, and by standardising how remaining risks are addressed in code, review and testing.

**Checklist**

- *Eliminate vulnerability classes by construction*
  - Prefer architectural and technology choices that prevent relevant vulnerability classes from arising, such as memory-safe languages for buffer overflows, parameterised data-access APIs for SQL injection and frameworks with context-aware output encoding for cross-site scripting.
  - Where elimination is not feasible, identify the remaining vulnerability classes and apply appropriate coding, review, testing and containment controls.
- *Adopt a secure coding baseline (language/framework specific)*
  - Define must-follow rules for your stack (e.g. on input handling, auth checks, error handling, crypto usage, logging).
  - Ban unsafe patterns (e.g. string-built SQL, eval-like functions, disabling TLS verification).
- *Validate inputs and encode outputs*
  - Centralise validation (schemas, allow lists, length/range checks).
  - Encode output by context (HTML/JSON/SQL); avoid mixing data and commands.
- *Use safe dependency and secrets practices*
  - Pin and regularly update dependencies; remove unused packages.
  - Secrets (e.g. API keys, tokens, credentials) must never be stored in source code or committed to source repositories. Secure secret management solutions should be used instead.
  - Generate and store an SBOM for each release (or a dependency inventory at minimum).
- *Make security-sensitive changes reviewable*
  - Clearly define and document roles for each stakeholder involved in the CI/CD pipeline (e.g. developer, support, administrator, integrator, CI runner).
  - Protect critical branches to prevent direct commits and history rewriting.
  - Prohibit force push on protected branches to prevent history rewriting and preserve auditability.
  - Require peer review for changes touching authn/authz, boundary-crossing APIs, crypto, update mechanisms or deserialisation and for any new external exposure.
  - Use PR checklists and CODEOWNERS files for sensitive areas.
  - Apply the same review requirements to AI-generated or AI-modified code as to human-written code.
- *Automate detection in CI/CD*
  - Run SAST and dependency scanning on each PR; fail builds on critical findings.
  - Add targeted unit/integration negative tests (unauthorised access denied; injection attempts fail).
  - Add basic fuzzing or property-based testing for high-risk parsers/inputs if feasible.
  - AI-generated or AI-modified code should go through the same SAST, dependency and secrets checks as human-written code.

**Minimum evidence**

- Design evidence: record of relevant vulnerability classes considered and the architectural or technology choices used to eliminate them by construction
- Secure coding standards (one or two pages or a repo file) for your stack and a banned patterns list
- PR checklist / CODEOWNERS file for security-sensitive modules
- CI pipeline evidence: SAST and dependency scan results for the release
- Secrets controls: proof that secrets are not in repo (pre-commit secret scanning results) and secrets manager usage
- Test evidence: at least a small suite of negative tests for critical endpoints/inputs

**Release gate**

- [ ] Relevant vulnerability classes have been eliminated by construction where feasible; where not feasible, appropriate preventive and verification controls are in place.
- [ ] A secure coding baseline exists for the stack and is referenced in the repo
- [ ] SAST and dependency scanning run in CI; critical issues fixed or covered by a documented exception (with owner and expiry)
- [ ] Secret scanning enabled; no secrets committed; rotation performed if exposure occurred
- [ ] Security-sensitive changes were peer reviewed (auth/authz, crypto, parsers, external interfaces)
- [ ] Negative tests run on critical endpoints (unauthorised access denied; injection attempts fail)
- [ ] Dependencies reviewed for high/ critical vulns; patch/mitigation plan recorded for any accepted risk

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.a: Supports release without known exploitable vulnerabilities by identifying and addressing issues during development
- ANNEX-1.PT2.1: Supports identification and documentation of vulnerable components during development
- ANNEX-1.PT2.3: Supports regular testing and review of product security during development and before release

### 4.10 Logging, monitoring and alerting

**Principle** (secure by design): Systems should generate appropriate security-relevant logs, retain them for a defined period and protect them from tampering, so that they can support investigation and compliance needs.

**Objective:** Provide sufficient visibility to detect misuse, investigate incidents and maintain system integrity over time. The focus is on a small set of high-signal security events, reliable log retention and actionable alerts that do not overwhelm teams.

**Checklist**

- *Define the “must-log” security events*
  - Authentication: login success/failure; MFA events; token issuance/refresh/revocation.
  - Authorisation: access denied, privilege or role changes, admin actions.
  - Boundary events: external API calls, device onboarding or pairing, OTA/update events.
  - Data or security changes: configuration changes, key or secret changes, user or service enabled or disabled.
  - Do not log personal or secret data by default. In general, log only the bare minimum required to understand events in default log level
- *Standardise access and audit log structure and attribution*
  - For access and authorisation logging, use consistent fields capturing who (actor), what (action or event type) and when (timestamp), with additional contextual fields as appropriate.
  - Ensure that admin actions are attributable to a named identity (no shared accounts).
- *Centralise collection and protect log integrity*
  - Central log store (SIEM/log platform or managed logging).
  - Separate logs based on type and/or service.
  - Restrict access to logs; separate duties and apply write-only permissions where feasible.
  - Set retention targets (e.g. 30 days or 90 days, longer for archival material if required). Plan storage accordingly.
  - Ensure time sync (NTP) across systems.
- *Implement actionable monitoring and alerts*
  - Start with a small alert set (high confidence, high impact): repeated auth failures, new admin creation, privilege escalation, unusual API error spikes, updates failing, disabled logging, access to sensitive endpoints from new locations.
  - Tune alerts to reduce noise (rate thresholds, suppression windows, environment filters).
- *Practice incident triage and response*
  - Define on-call duties / ownership for security alerts.
  - Document a minimal triage playbook covering: validate, scope, contain, remediate and communicate.
  - Carry out a quarterly tabletop exercise or dry run for one common scenario (account takeover or API key leak).

**Minimum evidence**

- Logging baseline: list of must-log events and required fields (one page)
- Central logging proof: screenshot/export/config showing logs from key components arriving centrally
- Retention setting: configured retention is in place and there is an access-control policy for logs
- Alert catalogue: list of enabled alerts with thresholds and owners (initial set can consist of around 5 to 10 alerts)
- Triage runbook: one-page steps and escalation contacts, plus one recent test (tabletop note)

**Release gate**

- [ ] Must-log security events implemented for new/changed components (auth, admin, updates, boundary events)
- [ ] Logs include attribution fields (actor, request/session ID, source) and are centralised
- [ ] Log access restricted, retention configured, time sync verified
- [ ] High-signal alerts enabled and assigned an owner (at least brute force events, new admin / role change, key/secret change, update failures)
- [ ] Triage runbook exists and has been tested recently (tabletop exercise or test alert)
- [ ] Logging/alerting exceptions are documented, with owner and review/expiry date

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.d: Supports detection and reporting of unauthorised access attempts
- ANNEX-1.PT1.2.l: Supports recording and monitoring of security-relevant internal activity

### 4.11 Configuration and change management

**Principle** (secure by design): Secure operation requires configurations to be controlled, consistent and auditable. Baseline hardening standards should be defined and applied through repeatable mechanisms such as templates and infrastructure as code to reduce drift.

**Objective:** Prevent security regressions and outages by ensuring that system configuration is controlled, reviewable and reproducible and that changes are assessed for risk before reaching production. The priority is to eliminate ‘silent drift’, tighten defaults and make rollbacks reliable.

**Checklist**

- *Version and review configuration (treat it as code)*
  - Store environment config, infrastructure templates and policies in version control.
  - Require peer review for changes affecting exposure, identity/access, secrets, networking, logging and updates.
- *Harden defaults and prevent drift*
  - Establish secure baseline configurations (deny by default where possible).
  - Use automated checks to detect drift between desired and actual config (at least for critical settings).
- *Separate environments and limit privilege*
  - Strict separation for dev/test/prod (accounts, projects, networks, credentials).
  - Restrict who can deploy to prod; remove direct manual changes where feasible.
- *Implement change gating and rollback*
  - Use CI/CD gates for config and infra changes (linting, policy checks, approval).
  - Require a rollback plan for each production change (including config-only changes).
  - Keep break-glass changes rare, logged and post-reviewed.
- *Track and assess security-impacting changes*
  - Tag changes that affect external exposure, authentication/authorisation, crypto, update mechanisms, data classification or third-party integrations.
  - Ensure that a lightweight threat/risk review is triggered when these tags apply.

**Minimum evidence**

- Config versioned: repo location(s) for IaC, config, policies; PR review history
- Baseline config: documented secure defaults and key settings (one page)
- Drift detection: a scheduled job/report or tool output for critical config items
- Deployment controls: proof that prod changes go through CI/CD (or change tickets) and are attributable
- Rollback proof: last rollback test result or documented rollback procedure
- Change log: record of security-impacting changes and associated approvals

**Release gate**

- [ ] Production config/IaC changes are versioned and peer-reviewed (no untracked manual edits)
- [ ] Secure baseline defaults applied; new components inherit baseline (network, IAM, logging)
- [ ] Dev/test/prod separated (accounts, projects, credentials); least privilege enforced for deployers
- [ ] CI/CD gates applied to config changes (policy checks, linting); approvals recorded
- [ ] Rollback plan exists for this release; rollback procedure tested recently or validated
- [ ] Security-impacting changes tagged and reviewed (exposure, IAM, secrets, crypto, updates, integrations)
- [ ] Exceptions (emergency changes) logged and post-reviewed, with owner and expiry date

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.f: Supports protection of configuration integrity by controlling, reviewing, and rolling back configuration changes.
- ANNEX-1.PT1.2.d: Supports protection from unauthorised access by restricting who can deploy or modify configurations, particularly in production environments

### 4.12 Incident response and recovery

**Principle** (secure by design): Developers must be prepared to respond quickly and effectively to security incidents that affect their products in the field, including vulnerabilities, compromised code, malicious updates and misuse of product functionality.

**Objective:** Detect, contain and recover from security incidents quickly while limiting customer impact and preventing recurrence. The priority is a clear playbook, defined ownership, fast triage and reliable restore/rollback, supported by the minimum logging and backup evidence needed to act decisively.

**Checklist**

- *Define roles, escalation and decision authority*
  - Name an incident lead and backups. Define escalation thresholds, when senior management should be informed and who can approve customer communications, access elevation and emergency changes.
  - Maintain an on-call/escalation contact list (internal + key suppliers).
- *Create a minimal incident runbook*
  - Steps: detect, triage, contain, eradicate, recover, lessons learned.
  - Include checklists for common scenarios (account takeover, leaked API key, ransomware/supply-chain alert, compromised device fleet).
- *Prepare containment controls*
  - Make sure that it is possible to revoke/rotate credentials and keys quickly.
  - Make sure that it is possible to disable accounts, block IPs, quarantine services/devices and roll back releases / config changes.
  - Ensure that break-glass access exists, is logged and is time bound.
- *Ensure recovery capability*
  - Backups are automated, tested and protected (immutability where feasible).
  - Restore procedures are documented for critical systems (data, configs, secrets, device firmware if applicable).
  - Define RTO/RPO targets appropriate to the business.
- *Exercise and improve*
  - Run a lightweight tabletop exercise (30–60 minutes) quarterly on one realistic scenario.
  - Record and review incidents, near misses and exercise findings. Track actions to closure and update risk assessments, threat models, runbooks, detections and controls as appropriate.

**Minimum evidence**

- Defined roles: incident-response contact list + roles (owner, backups and escalation paths established).
- Runbooks: one-page incident runbook and at least one scenario checklist.
- Containment proof: documented steps and permissions to revoke keys, disable accounts and roll back deployments.
- Backup/restore proof: backup configuration and one recent restore test result (or evidence of a successful restore).
- Post-incident, near-miss or tabletop notes showing findings, actions and resulting improvements.

**Release gate**

- [ ] IR roles and escalation contacts are current
- [ ] Incident runbook exists and covers detect/triage/contain/recover with at least one common scenario
- [ ] Containment actions are ready
- [ ] Backups enabled for critical data/config; restore procedure documented and tested recently
- [ ] Post-incident, near-miss or tabletop notes exist and are updated

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.h: Supports recovery and continued availability of essential functions after incidents
- ANNEX-1.PT1.2.k: Supports reduction of incident impact through prepared response and mitigation actions

### 4.13 Vulnerability and patch management

**Principle** (secure by design): Manufacturers should establish practical, repeatable vulnerability and patch management processes and prioritise remediation according to risk. Manufacturers need a simple way for customers and researchers to report issues and an internal process to triage findings quickly and decide what needs urgent action.

**Objective:** Identify, prioritise and remediate vulnerabilities fast enough to reduce real-world exposure, across your code, dependencies, infrastructure and (if applicable) devices/firmware. The focus is a simple intake-to-fix workflow, clear SLAs and an update mechanism that makes patching reliable.

**Checklist**

- *Establish intake channels (do not miss issues)*
  - Sources: dependency scanning, SAST/DAST results, advisories, customer reports, security emails, etc.
  - Assign a single owner for triage and tracking.
- *Triage and prioritise consistently*
  - Use a lightweight severity approach (e.g. critical, high, medium or low) plus ‘internet-exposed’ and ‘known exploited’ flags.
  - Ensure awareness of applicable incident and vulnerability reporting timelines.
  - Decide quickly: fix now, mitigate, accept (time bound) or defer (with rationale).
- *Patch dependencies and third parties proactively*
  - Maintain a regular cadence (e.g. weekly or monthly) for dependency updates.
  - Pin versions, remove unused dependencies and track transitive dependencies.
- *Fix, test and release with a secure process*
  - Ensure that fixes are reviewed and tested; verify no regressions in authn/authz, input validation or critical workflows.
  - For devices/IoT: ensure secure OTA/update path and safe rollback where feasible.
- *Communicate, learn and close the loop*
  - Track affected versions, customers/environments and mitigation guidance.
  - Publish security release notes or advisories as appropriate.
  - Verify rollout completion and update the risk register.
  - Establish an escalation process to assess applicable regulatory reporting obligations.
  - Where proportionate, publish machine-readable advisories (e.g. CSAF), including structured information on whether specific products or versions are affected, such as through VEX.
  - Analyse significant or recurring vulnerabilities, field reports, incidents and exploitation patterns to identify root causes. Feed the findings back into the risk assessment, security requirements and development practices.

**Minimum evidence**

- Vulnerability tracking board / register: issue, severity, affected components/versions, owner, status, target date
- Defined SLAs: for example, critical triage ≤ XX hours; remediation/release target ≤ X days (specify numbers that are realistic for you)
- Scanning evidence: CI outputs for dependency scanning and SAST (and DAST if applicable)
- Proactive dependency patches: SBOM or dependency inventory for each release (at minimum for shipped artefacts)
- Patch release record: link from vulnerability ticket → PR(s) → tests → release version → rollout confirmation
- Exception log: accepted risks, with owner and expiry/review date, and compensating controls (if any)
- Field feedback and improvement record: recurring security issues or attack patterns, root causes identified where applicable, and the resulting risk, design or backlog actions.

**Release gate**

- [ ] Dependency and SAST scans executed for the release; critical and high findings addressed or documented exception (with owner and expiry date)
- [ ] SBOM (or dependency inventory) generated/updated and stored for the release
- [ ] Known vulnerabilities affecting shipped components are triaged with severity information, owner and target date
- [ ] Patch process validated: fix reviewed, tests passed, and release notes updated as needed
- [ ] For internet-exposed components: mitigations or patches for critical- and high-severity issues are in place before release
- [ ] OTA/update (if applicable) validated for secure delivery; rollback/recovery documented
- [ ] Accepted residual risk is time bound and tracked to closure or review date

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT2.1: Supports identification and tracking of vulnerable components and dependencies throughout the product life cycle
- ANNEX-1.PT2.2: Supports timely triage and remediation of identified vulnerabilities based on risk
- ANNEX-1.PT2.4: Supports public disclosure of fixed vulnerabilities
- ANNEX-1.PT2.5: Supports coordinated handling and disclosure of vulnerabilities
- ANNEX-1.PT2.6: Supports mechanisms for receiving vulnerability reports from external parties
- ANNEX-1.PT2.7: Supports secure distribution of patches and updates
- ANNEX-1.PT2.8: Supports timely dissemination of security updates and related user guidance

### 4.14 Supply-chain controls

**Principle** (secure by design): Developers should protect product integrity without excessive process overhead, focusing on the points where a compromise would have the largest impact: code repositories, build systems, signing keys and the channels used to distribute updates.

**Objective:** Reduce the risk of compromise through third parties (software components, libraries, build tools, CI/CD, contractors, hosting providers and hardware/firmware suppliers) by establishing minimum, repeatable controls that improve visibility, integrity and accountability across what you buy, build and ship.

**Checklist**

- *Know what you depend on (inventory + SBOM)*
  - Maintain an inventory of critical suppliers and third-party components, including externally sourced AI/ML models where relevant.
  - Generate an SBOM per release (or minimum: dependency manifest snapshot) to improve visibility and response speed.
- *Control what enters your codebase*
  - Pin dependency versions; require review for new dependencies and major upgrades. Pinning and lock files improve build repeatability but do not establish that the pinned component is trustworthy. New and updated dependencies still require appropriate review and security checks.
  - Run dependency scanning in CI; block builds on critical- or high where feasible (or require explicit exception).
  - Where proportionate, obtain dependencies through approved repositories or controlled registries and apply integrity, malware and policy checks before use.
  - For externally sourced AI/ML models, record their source and version, verify their integrity and provenance, and assess relevant security risks before integration.
- *Harden the build and release pipeline (integrity of artefacts)*
  - Restrict CI/CD permissions (least privilege), protect secrets and separate build and deploy roles.
  - Sign release artefacts and, where proportionate, generate verifiable provenance describing how and from which inputs they were built.
  - For higher-risk products, use isolated and ephemeral build environments, consider restricting build-time network access to approved sources and consider hermetic builds where feasible.
- *Set minimum supplier expectations (lightweight due diligence)*
  - For critical suppliers, require a security contact / VDP, patch timelines and confirmation of secure development practices.
  - Use a short questionnaire aligned with a recognised baseline (e.g. OWASP SCVS) rather than bespoke questions.
- *Plan for supplier failure*
  - Identify single points of failure (key providers/components) and define fallbacks (alternate package source, vendor substitution plan, rapid disable/mitigation).
  - Ensure that contracts and SLAs cover vulnerability notification and support windows (where possible).

**Minimum evidence**

- Supplier + component inventory (top vendors, critical libraries/tools, hosting/build services), including externally sourced AI/ML models where relevant
- SBOM (or dependency inventory) per release, stored with the release artefacts
- CI results showing dependency scanning (and ideally secret scanning) executed on PRs/releases
- Release integrity evidence: artefact signing and restricted CI/CD access (configs/screenshots/logs)
- Supplier baseline checks for critical suppliers (a completed questionnaire or SCVS-aligned checklist)
- Exception log for accepted supply-chain risks (with owners and expiry dates)

**Release gate**

- [ ] SBOM (or dependency inventory) generated and stored for this release
- [ ] Dependency scanning executed; critical- or high-severity issues fixed or covered by a documented exception (with owner and expiry date)
- [ ] New dependencies/suppliers reviewed and approved (recorded in PR/ticket)
- [ ] CI/CD and build secrets are protected; build/deploy permissions are least privilege and attributable
- [ ] Release artefacts signed (and provenance captured where feasible / per chosen SLSA target)
- [ ] Critical suppliers meet baseline expectations (security contact, vulnerability notification, support/patch commitments)
- [ ] Supply-chain risk exceptions recorded, with owner and review/expiry date

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.a: Supports reduction of exploitable vulnerabilities introduced through compromised components
- ANNEX-1.PT2.1: Supports transparency of components and dependencies through SBOM generation
- ANNEX-1.PT2.7: Supports secure distribution of updates through protected build and release channels

### 4.15 Minimisation of default services

**Principle** (secure by default): Disable non-essential features and services by default. Only the functionality required for the core operation of the product should be enabled by default.

**Objective:** Reduce the attack surface and ensure that products start in a hardened state, without relying on users to disable specific functionality.

**Checklist**

- *Define core functionality*
  - Identify the minimum set of features and services required for the product to operate.
- *Disable non-essential features and services by default*
  - Ensure that optional features and services are disabled by default.
- *Require explicit opt-in for additional functionality*
  - Ensure that non-essential features and services can be enabled only through deliberate user action.
- *Explain security implications on enablement*
  - Inform users of security risks when enabling optional features and services.
  - Avoid enabling additional features and services without clear acknowledgement.
- *Review defaults on change*
  - Reassess default-enabled features and services when new features are introduced.

**Minimum evidence**

- Core features and services defined: documentation or configuration identifying which features and services are required by default.
- Non-essential features and services disabled: default configuration or build artefacts show optional features and services and modules are off.
- Explicit opt-in required: configuration or documentation shows how additional features and services must be manually enabled.
- Security implications disclosed: documentation, UI text or configuration prompts show that users are informed of security implications when enabling non-essential features and services.
- Defaults reviewed for this release: release notes, checklist or ticket confirms that default settings have been reviewed after changes.

**Release gate**

- [ ] Only core functionality is enabled by default
- [ ] Optional features and services are disabled unless explicitly enabled by the user
- [ ] Users are informed of security implications when enabling non-essential features and services
- [ ] No new features or services are enabled by default without review
- [ ] Default configuration has been reviewed and confirmed for this release

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.b: Supports secure by default configuration by disabling non-essential features and services at initial deployment
- ANNEX-1.PT1.2.i: Supports minimising negative impact on other services by disabling non-essential functionality that could otherwise be abused or misused
- ANNEX-1.PT1.2.j: Supports limitation of attack surfaces by reducing exposed services and interfaces by default

### 4.16 Restrictive initial access

**Principle** (secure by default): Ship systems in the most restrictive access state possible. Eliminate shared or default credentials and require a secure access set-up before any privileged or sensitive operations are allowed.

**Objective:** To prevent immediate compromise after deployment by ensuring that attackers cannot gain access through default or weak initial access.

**Checklist**

- *Eliminate shared default credentials*
  - Do not ship products with universal usernames or passwords (e.g. ‘admin/admin’ or ‘root/root’).
- *Require unique credentials for each device or instance*
  - Ensure that each device or instance has unique credentials generated at manufacture, provisioning or first boot.
- *Enforce a secure initial set-up*
  - Require a credential change, key provisioning or account creation before allowing privileged or sensitive access.
- *Restrict initial permissions*
  - Grant the minimum permissions required for initial operation.
  - Avoid granting full administrative access by default.
- *Protect initial access paths*
  - Ensure that first-boot, onboarding and recovery interfaces are authenticated and not unnecessarily exposed.

**Minimum evidence**

- No default credentials shipped: build configuration or documentation confirms that no shared or hard-coded credentials exist.
- Unique credentials enforced: provisioning records, configuration or device inventory shows per-device or per-instance credentials.
- Secure set-up required: configuration or test evidence shows credential change or secure set-up is mandatory before privileged or sensitive access.
- Initial permissions restricted: access model or configuration shows limited permissions at first use.
- Initial access paths controlled: configuration or test evidence shows that onboarding and recovery interfaces are protected.

**Release gate**

- [ ] No shared or default credentials present in production builds
- [ ] Unique credentials generated for each device or instance
- [ ] Secure set-up enforced before privileged or sensitive access
- [ ] Initial permissions are restrictive by default
- [ ] Initial access and onboarding paths are protected and reviewed

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.b: Supports secure by default access settings by avoiding permissive initial credentials and permissions
- ANNEX-1.PT1.2.d: Supports protection from unauthorised access by enforcing restrictive authentication and access-control settings at first use

### 4.17 Secure communication by default

**Principle** (secure by default): Enforce secure communication from the start. All external communications must be encrypted and authenticated by default, with no support for insecure or plain-text protocols for convenience.

**Objective:** Protect data in transit and prevent interception, tampering or impersonation by ensuring that communications are always secure, without relying on user configuration or later hardening.

**Checklist**

- *Protect external communications by default*
  - Require encrypted communication for all external interfaces from first use.
  - Where data or commands pass through intermediaries, assess whether transport protection alone is sufficient or whether additional end-to-end authenticity, integrity and freshness controls are required.
- *Disable insecure and plain-text protocols*
  - Do not allow unencrypted or weak protocols (e.g. HTTP or Telnet) to be used by default or even as fallbacks.
- *Authenticate communicating endpoints*
  - Ensure that external endpoints authenticate each other where appropriate, for example for device-to-cloud, service-to-service and administrative access.
- *Enforce secure protocol versions and configurations*
  - Use modern, secure protocol versions and configurations by default.
  - Explicitly disable weak ciphers, legacy versions and insecure negotiation modes.
- *Fail securely on connection errors*
  - Ensure that communication failures result in denied connections rather than downgrading to insecure protocols or configurations.
- *Plan for cryptographic change*
  - Design cryptographic mechanisms so that algorithms, keys, certificates and trust anchors can be replaced or migrated without substantially redesigning the product, where feasible.
  - Assess whether the product’s support lifetime, data confidentiality requirements and deployment constraints require preparation for migration to post-quantum cryptography.

**Minimum evidence**

- Secure protocols enforced by default: configuration or test evidence shows that encrypted and authenticated communication is required from first connection.
- Insecure protocols disabled: configuration confirms that plain-text or legacy protocols are not enabled or available.
- Endpoint authentication in place: configuration or test evidence shows that mutual or appropriate endpoint authentication takes place for external communications.
- Strong protocol configuration applied: configuration shows that only approved protocol versions and cryptographic settings are enabled.
- No insecure fallback: test evidence shows that connection attempts fail securely rather than downgrading security.
- Cryptographic migration note: identification of critical cryptographic mechanisms and how algorithms, keys, certificates and trust anchors are to be updated or replaced.

**Release gate**

- [ ] External communications are encrypted and authenticated from first connection
- [ ] Insecure or plain-text protocols are disabled and unavailable
- [ ] Only approved secure protocol versions and configurations are enabled
- [ ] Endpoint authentication enforced where required
- [ ] Connection failures do not result in insecure fallback
- [ ] Cryptographic mechanisms can be replaced or migrated where required by the product’s risk assessment and support lifetime.

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.b: Supports secure by default configuration by enforcing encrypted and authenticated communications from initial connection
- ANNEX-1.PT1.2.e: Supports confidentiality of transmitted data by applying encryption to communications from first use
- ANNEX-1.PT1.2.f: Supports integrity protection of transmitted data by preventing unauthorised modification of data in transit

### 4.18 Unique device identity and secrets by default

**Principle** (secure by default): Ship each product instance with a unique cryptographic identity and secrets by default if it uses any private/secret value. Do not use shared credentials, keys or certificates across devices or installations.

**Objective:** Prevent large-scale compromise by ensuring that a breach of one device or a leaked secret cannot be reused to attack other devices, customers or the wider installed base.

**Checklist**

- *Generate unique identities per device or instance*
  - Assign a unique device identity (e.g. key pair or certificate) to every device or installation.
- *Eliminate shared or hard-coded secrets*
  - Do not use shared credentials, default keys or embedded secrets across products.
- *Protect secrets against extraction*
  - Store device identities and per-device secrets using platform-appropriate controls that protect against extraction, tampering or unauthorised replacement (e.g. secure storage, hardware-backed protection or restricted access).
- *Use unique secrets for security-critical functions*
  - Ensure that security-critical functions like authentication, secure communications and update verification rely on per-device secrets, not shared material.
- *Support revocation and replacement*
  - Ensure that device identities and secrets can be revoked and rotated if compromise is suspected.

**Minimum evidence**

- Unique device identities issued: device inventory or provisioning records show a unique identity (e.g. key pair or certificate) for each device or instance.
- No shared secrets present: build artefacts or configuration confirms that no shared credentials or hard-coded secrets exist.
- Secrets protected at rest: documentation or configuration shows that secrets are stored using appropriate protection mechanisms.
- Security functions use unique secrets: configuration or design notes show that authentication, communication and update processes rely on per-device secrets.
- Revocation supported: documentation or configuration shows that device identities or secrets can be revoked or replaced.

**Release gate**

- [ ] Unique cryptographic identity generated for each device or instance
- [ ] No shared or default secrets present in production builds
- [ ] Secrets are protected against extraction
- [ ] Security-critical functions use per-device secrets
- [ ] Identity and secret revocation or replacement is supported

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.b: Supports secure by default configuration by avoiding shared credentials and shared cryptographic material
- ANNEX-1.PT1.2.d: Supports protection from unauthorised access by avoiding shared credentials and enforcing unique device authentication
- ANNEX-1.PT1.2.e: Supports confidentiality by preventing reuse or leakage of shared secrets across devices

### 4.19 Mandatory security onboarding

**Principle** (secure by default): Require critical security controls to be configured during initial set-up. Do not allow products to enter an operational state until essential security steps are completed.

**Objective:** Ensure that systems start in a secure state by preventing or limiting use before baseline security controls, such as strong authentication or encryption, are configured.

**Checklist**

- *Identify mandatory security steps*
  - Define the minimum security controls required before the product can be used (e.g. MFA, encryption keys, admin account set-up).
- *Enforce security set-up during first use*
  - Integrate mandatory security steps into the initial set-up or onboarding flow.
  - Do not allow users to skip or defer required security configuration.
- *Block operation until onboarding is complete*
  - Prevent normal operation, privileged actions and external connectivity until mandatory security steps are completed.
- *Provide clear, guided configuration*
  - Guide users through security set-up with clear instructions and sensible defaults.
  - Avoid requiring expert knowledge to complete onboarding securely.
- *Re-trigger onboarding when security is incomplete*
  - Re-enforce onboarding if critical security settings are removed, reset or left unconfigured.

**Minimum evidence**

- Mandatory security steps defined: documentation identifies which security controls must be completed during onboarding.
- Onboarding enforces a security set-up: configuration, screenshots or test evidence shows that critical security steps cannot be skipped.
- Operation blocked pre-onboarding: configuration, screenshots or test evidence shows that the product cannot enter normal operation before onboarding is complete.
- Guided set-up is provided: screenshots, configuration flows or documentation shows that clear user guidance is provided on security set-up.
- Onboarding is re-enforced on incomplete security configuration: configuration, screenshots or test evidence shows that onboarding is re-triggered if required security settings are missing.

**Release gate**

- [ ] Mandatory security steps are defined and enforced during initial set-up
- [ ] Users cannot bypass or skip critical security configuration
- [ ] Product cannot enter normal operation before onboarding completion
- [ ] Security onboarding provides clear guidance and secure defaults
- [ ] Onboarding is re-enforced if critical security settings are removed

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.b: Supports secure by default configuration by requiring critical security features to be configured before initial exposure
- ANNEX-1.PT1.2.d: Supports protection from unauthorised access by ensuring that authentication and access controls are configured at first use

### 4.20 Automated maintenance and updates

**Principle** (secure by default): Manufacturers should provide secure update mechanisms that minimise user and operational effort. Security updates should be enabled by default, while allowing authorised users or operators to approve or schedule installation where the deployment requires controlled updates.

**Objective:** Ensure that vulnerabilities are addressed quickly and the device is left vulnerable for as little time as possible.

**Checklist**

- *Enable managed security updates by default*
  - Enable security updates by default, ensuring that the product automatically checks for updates, informs the user and supports timely installation, with escalation where updates are repeatedly deferred.
  - Where unattended installation could affect safety, availability or operational continuity, support staged rollout, maintenance windows and authorised operator approval.
- *Separate security updates from feature changes*
  - Ensure that critical security updates can be delivered independently of optional feature/functional updates.
- *Verify the authenticity and integrity of updates*
  - Ensure that updates are cryptographically verified before installation.
- *Apply updates safely*
  - Design updates to minimise disruption and avoid leaving the system in an insecure or unusable state if the update fails.
  - Support staged rollout, maintenance windows, operator approval and rollback where required by safety, availability or operational-continuity considerations.
- *Inform users of update activity*
  - Notify users when security updates are applied or when action is required, without requiring them to manage the update process manually.

**Minimum evidence**

- Automatic updates enabled: default configuration shows that security updates are enabled out of the box.
- Security updates decoupled: configuration or release notes show that security fixes can be delivered independently of optional feature/functional updates.
- Update verification enforced: configuration or design notes show that updates are authenticated and integrity-checked.
- Safe update mechanism in place: documentation or test evidence shows that updates can be applied without significantly disrupting basic operation.
- Update strategy: documentation or test evidence shows that the update process supports controlled approval, staging and rollback where required by the deployment context.
- User notification supported: logs, UI messages or documentation shows that users are informed of update activity or status.

**Release gate**

- [ ] Security update functionality is enabled by default, with an installation approach appropriate to the product’s deployment context
- [ ] Security updates can be delivered independently of features
- [ ] Updates are cryptographically verified before installation
- [ ] Failed updates do not leave the system insecure or unusable
- [ ] Users are informed of update status without manual intervention

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.b: Supports a secure by default posture by enabling automatic security updates
- ANNEX-1.PT1.2.c: Supports the ability to address vulnerabilities through automatic security updates enabled by default
- ANNEX-1.PT2.2: Supports timely remediation of vulnerabilities by reducing reliance on manual patch deployment
- ANNEX-1.PT2.7: Supports secure and timely distribution of security updates by enabling automated update mechanisms

### 4.21 Transparent security posture

**Principle** (secure by default): Make the system’s security posture visible and understandable. Clearly inform users when security protections are weakened and provide a simple path to return to a secure baseline.

**Objective:** Reduce risk arising from accidental or uninformed misconfiguration by ensuring that users understand the security state of the system and can easily correct insecure settings.

**Checklist**

- *Define security states and baseline*
  - Define the secure baseline and any degraded or unsupported security states.
  - Document which configurations cause a transition between states.
- *Expose current security status*
  - Indicate clearly whether the system is operating in a secure or degraded security state.
- *Warn on changes that reduce security*
  - Show clear warnings when users disable security features or apply configurations that increase risk.
- *Explain impact in plain language*
  - Explain to the user the security implications of a change in non-technical terms.
- *Provide a simple path to recovery*
  - Offer the user a simple interaction path to return to the secure baseline.

**Minimum evidence**

- Security states defined: documentation identifies the secure baseline and degraded or insecure states, including the configuration changes that trigger such states.
- Security status visible: screenshot, CLI output or documentation clearly shows the current security state.
- Warnings triggered on risk increase: screenshots, prompts or test evidence shows warnings when users apply security-reducing changes.
- Impact explained clearly: warning messages, screenshots or documentation demonstrates that security implications are described in plain, non-technical language.
- Baseline restore available: screenshots, commands or configuration shows a simple action exists to return to the secure baseline.

**Release gate**

- [ ] Secure baseline and degraded security states are defined and documented
- [ ] Current security state is clearly visible to the user
- [ ] Users are warned when security protections are reduced
- [ ] Security impact is explained in clear, non-technical language
- [ ] A simple action can be taken to restore the secure baseline

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.b: Supports secure by default configuration by guiding users back to a secure baseline when insecure choices are made
- ANNEX-1.PT1.2.l: Supports security-related information by informing users of security-relevant state changes and risks

### 4.22 Secure recovery and ownership life cycle

**Principle** (secure by default): Provide secure, guided recovery and ownership transfer mechanisms by default. Recovery, reset and transfer processes must be easy for users, operators and administrators to follow, while remaining resistant to abuse, account takeover and social engineering.

**Objective:** To enable users and administrators to recover access, reset systems or transfer ownership safely.

**Checklist**

- *Define supported recovery and transfer actions*
  - Identify supported recovery actions such as credential reset, account recovery, secure factory reset and ownership transfer, clearly defining who is allowed to initiate each action and under what conditions
- *Verify identity before recovery or transfer*
  - Require strong identity verification before allowing recovery, reset or ownership transfer actions.
- *Protect recovery paths from abuse*
  - Ensure that recovery mechanisms cannot be used to bypass normal authentication or authorisation controls.
  - Apply monitoring and rate limiting to recovery and reset workflows.
- *Ensure secure reset and ownership transfer*
  - Ensure that factory reset and ownership transfer fully remove previous user access, credentials and secrets.
- *Provide guided, secure workflows*
  - Offer clear recovery and transfer processes that reduce user error

**Minimum evidence**

- Recovery and transfer actions are defined: documentation identifies supported recovery, reset and ownership transfer processes.
- Strong verification is enforced: configuration or test evidence shows that recovery and transfer actions require a verified identity.
- Abuse protections are applied: configuration, logs or test evidence shows that rate limiting and monitoring of recovery workflows are in place.
- Secure reset and transfer is verified: test evidence confirms that factory reset and ownership transfer remove prior credentials and access.
- Guided workflows are available: screenshots, CLI commands or documentation demonstrates that recovery and transfer processes are guided.

**Release gate**

- [ ] Supported recovery and ownership transfer actions are defined
- [ ] Recovery and transfer actions require strong identity verification
- [ ] Recovery mechanisms cannot bypass normal access controls
- [ ] Factory reset and ownership transfer fully remove prior access
- [ ] Clear guidance is provided on recovery and transfer workflows

**Annex C (indicative CRA mapping)**

- ANNEX-1.PT1.2.b: Supports secure by default configuration by providing safe recovery and reset paths that restore a secure baseline
- ANNEX-1.PT1.2.d: Supports protection from unauthorised access during recovery, reset and ownership transfer processes
- ANNEX-1.PT1.2.m: Supports secure removal of data and settings during factory reset, decommissioning or ownership transfer

### 4.23 Progressive adoption of the playbooks

This section provides an illustrative progressive adoption sequence, showing how the playbooks can be adopted and applied over time. The example begins with activities that provide context and prioritisation, followed by a foundational engineering baseline and then a broader and more mature implementation of the principles. Progressive adoption here refers to how organisations build and strengthen their security practices over time. It does not suggest delaying applicable requirements or controls, particularly those arising from legal obligations, including under the CRA. This guidance is without prejudice to such obligations, which take precedence.

4.23.1 Establish context and priorities

The product context, risk management and threat-modelling activities described in Section 2 can be used, together with Playbook 4.1, to identify the most relevant threats, trust boundaries and security objectives. This step can guide prioritisation and scoping as regards the implementation of the playbooks.

4.23.2 Establish a foundational engineering baseline

Based on the product context, security objectives, and identified risks threats, organisations should establish an appropriate engineering baseline. For most products, an initial baseline should include:

- secure coding and verification practices (Playbook 4.9);

- logging, monitoring and alerting (Playbook 4.10);

- vulnerability and patch management (Playbook 4.13);

- supply-chain controls (Playbook 4.14).

This baseline should be supplemented by the secure by default playbooks relevant to the product. For example:

- restrictive initial access (Playbook 4.16), where the product provides user, administrative or maintenance access;

- secure communication by default (Playbook 4.17), where the product communicates over a network or exchanges data with external components;

- unique device identity and secrets by default (Playbook 4.18), where devices, product instances or services require identities or credentials;

- automated maintenance and updates (Playbook 4.20), where the product can be updated after deployment.

Other playbooks should be prioritised at this stage where they are necessary to address the identified risks, threats and security objectives or product context. For example, availability-sensitive products may require early implementation of the incident response and recovery playbook (Playbook 4.12), while products supporting reset, ownership transfer or decommissioning may require the implementation of the secure recovery and ownership life-cycle playbook (Playbook 4.22).

Progressive adoption could also determine the extent to which an individual playbook is implemented. An organisation could begin with the checklist items that address its priority risks and applicable requirements, and then strengthen coverage, evidence and automation over time.

4.23.3 Broaden and strengthen implementation

The remaining applicable playbooks can be implemented and prioritised according to the product context, intended use, deployment context and identified risks and threats. Over time, teams should increase the coverage, consistency and automation. Moreover, progress should be assessed using relevant measures.

This illustrative sequencing is intended to help organisations manage implementation effort. It does not mean that playbooks addressed in a later phase are inherently less important or that applicable security or regulatory requirements may be deferred.

## 5 Machine-processable attestation (concepts)

5. Machine-processable attestation

### 5.1 Demonstrability, verifiability and assurance

In modern software engineering, the transition from manual, document-heavy compliance to machine- processable attestations marks a critical evolution in how trust can be verified. At its core, a machine- processable attestation is a digital claim, encoded in formats like JSON or YAML, asserting that a specific security control, process or property has been met. Unlike static PDF reports that sit in a folder, these digital artefacts are ‘generatable’ and ‘consumable’ by automated systems, enabling frequent or event-driven updates and automated validation of security claims across the product supply chain.

Machine-processable means that automated systems should be able to validate, interpret and act on it without human interpretation. This requires elements such as defined field types and semantics, controlled values, structured representation of decision-relevant information and schema versioning. Structured fields should be preferred for information used in automated processing, with free text used where additional explanation is helpful.

By embedding these attestations directly into the development pipeline, security becomes an intrinsic part of the product’s DNA, rather than a post-development checkbox.

- During a product’s design and development, machine-processable formats allow architects to define security requirements as code, which can then be automatically mapped to implementation evidence.

- For verification, these attestations enable automated gatekeeping; for instance, a deployment system can be configured to block any container that lacks a valid, machine-signed attestation of a successful vulnerability scan by default.

Furthermore, machine-processable attestations solve the ‘transparency gap’ inherent in complex ecosystems. They provide a verifiable, tamper-evident trail of a product’s security posture from the source code to the final runtime environment. This level of transparency ensures that every stakeholder, from the developer to the end customer, has access to an objective, current view of the risk profile, effectively automating the trust relationship between producers and consumers.

Technical documentation can also benefit from machine-processable attestations. Instead of being created as a static snapshot at a particular point in time, the artefacts can help ensure that documentation stays accurate and current by displaying the security requirements, implementation evidence, and verification results.

This is a significant advantage, particularly in view of the CRA’s requirement that manufacturers maintain technical documentation. Such documentation can be kept up to date and supported by verifiable implementation and test evidence.

A manufacturer-issued attestation by itself is not proof that a product is secure. Attestation, verification and independent assessment are distinct activities. An attestation provides claims and links it to supporting evidence; verification checks the integrity, scope, currency and consistency of those claims and that evidence; and independent assessment can evaluate whether the controls and evidence are sufficient for the product and its risks.

For SME engineering teams, machine-processable attestation can support automation by employing these concepts:

- Demonstrability: The proactive capacity of a system and its development process to provide objective, machine-processable evidence that specific security requirements have been implemented. It represents the shift from “claiming” security in a static document to “showing” security through generated artefacts, such as signed build logs, automated test results, and standardised metadata.

- Verifiability: The ability for an independent party, whether an automated tool, a customer, or a regulator, to programmatically authenticate and validate the integrity of security claims. A verifiable system ensures that attestations are transparent, tamper-evident, and mapped to a recognised root of trust, allowing for the continuous, low-friction audit of a product’s security posture.

- Reusability: The ability to use existing attestations for further build on existing developments directly integrating cybersecurity in the development cycle and enabling an continuous cybersecurity improvement with minimal effort.

- Reliability: The ability to rely on existing attestations also for third party components, simplifying due diligence based on a structured attestation demonstrating security properties of a component with additional option for third party verification

### 5.2 Incentives

When security requirements are demonstrable, engineering teams move away from security as an afterthought and instead treat security as a primary functional requirement, because it means that every design decision, from the choice of a library to the architecture of a database, should be accompanied by the creation of a machine-processable artefact. This active generation of evidence allows teams to catch architectural flaws during the design phase, long before code is committed or products are shipped.

Furthermore, while secure by default focuses on delivering products that are secure out of the box, verifiability provides the mechanism to ensure those defaults remain intact and effective. In a verifiable ecosystem, the default state is not just a configuration choice but a protected claim that can be automatically checked at every stage of the life cycle.

Using reusable attestation enables the manufacturer to directly include cybersecurity into the development process and enabling the integration of cybersecurity controls in small use case specific packages leveraging existing agile methods and can also be included in quality gates in agile project management and tooling, e.g. cybersecurity as part of Definition of Ready and Done in Scrum

Relying on machine-processable attestation enables manufacturer to reduce effort for due diligence and supply chain management. A structured attestation enables integrators to simply pinpoint necessary security properties for due diligence and enhances trust with evidences and additional verification.

This creates a fail-safe environment in which a system can refuse to operate if its attestations, such as signed proof that MFA is enforced or that the latest vulnerability scan was passed, are missing or invalid.

For SMEs, this automation eliminates the need for constant manual checks. It ensures that the product’s security baseline is both self-verifying and consistently visible to stakeholders.

Machine-processable attestations can also support procurement and supplier assessment. Customers, integrators and procurers can use such structured claims and evidence to compare products, verify security-relevant properties and identify areas that may require further assessment.

### 5.3 Existing frameworks and initiatives

The ecosystem of machine-processable security has been rapidly evolving. Some of the key initiatives include foundational frameworks like NIST’s Open Security Controls Assessment Language (OSCAL) (compliance as code), OWASP’s CycloneDX Attestations (CDXA) (native security attestation) and SPDX 3.0 Security Profile, which provide the structural grammar for automating compliance and supply-chain transparency. Presented below are some of these initiatives in this area.

- OSCAL (21). Developed by NIST, OSCAL is the premier model for compliance as code. It provides a standardised way to express security control catalogues, system security plans and assessment results. By using OSCAL, organisations can automate the generation of compliance documentation, allowing for continuous authorisation, whereby the status of security controls is updated in real-time as evidence is collected.

- CycloneDX (OWASP ECMA-424) (22). While originally an SBOM format, CycloneDX has expanded into a full-stack transparency standard. Its attestation capabilities (CDXA) allow organisations to document claims about security requirements alongside generating a bill of materials. It also includes specialised modules like VEX to communicate whether a vulnerability actually affects a product, and it can produce a cryptographic bill of materials (CBOM) to inventory cryptographic assets for quantum readiness. CycloneDX Assessors Studio (23) provides an emerging open-source implementation for conducting structured assessments, collecting evidence, documenting claims and generating CycloneDX attestations.

- SDPX 3.0 Security Profile (24). The security profile captures security-related information in a SPDX Security Document. Specifically, the properties and relationships specified in the security profile are in support of exchanging information about system vulnerabilities that may exist, the severity of those vulnerabilities, and a mechanism to express how a vulnerability may affect a specific element including if a fix is available.

- The Open Source Security Foundation (OpenSSF). OpenSSF leads several projects, including Security Insights (25), a specification that project teams can use to report security facts (like bug bounty information or security contacts) in a machine-processable YAML format. They also champion the OpenSSF Scorecard (26), which automatically assesses open-source projects against security best practices. OpenSSF Best Practices badge (27) provides machine-readable security criteria status for many OSS projects, including against the OpenSSF Baseline (28). Supply-chain Levels for Software Artifacts, or SLSA (29) (“salsa”) provides recommended machine-readable schemas for SLSA attestations.

- OWASP (Open Web Application Security Project). Beyond CycloneDX, OWASP projects like the ASVS (30) (Application Security Verification Standard) provide the underlying requirements that these machine-readable formats aim to verify. Newer initiatives like the MLSVS (Machine Learning Security Verification Standard) are extending these principles into the AI/ML domain.

(21) https://pages.nist.gov/OSCAL/.

(22) https://cyclonedx.org/capabilities/attestations/.

(23) https://github.com/CycloneDX/cyclonedx-assessors-studio.

(24) https://spdx.dev/learn/areas-of-interest/security/.

(25) https://openssf.org/projects/security-insights/.

(26) https://openssf.org/projects/scorecard/.

(27) https://www.bestpractices.dev/.

(28) https://baseline.openssf.org/.

(29) https://slsa.dev/spec/v1.2/attestation-model.

(30) https://owasp.org/www-project-application-security-verification-standard/.

- TC54 (Ecma International) (31): This technical committee is the formal standardisation body for CycloneDX. It focuses on the Transparency Exchange API, which aims to standardise how software transparency information (like SBOMs and attestations) is discovered and shared across the global supply chain.

- in-toto (32). in-toto provides an open framework for expressing verifiable claims about software supply-chain activities. SLSA Provenance uses in-toto to describe where, when and how software artefacts were built and tools such as Sigstore Cosign (33) can sign and verify in-toto attestations.

- Device Security Passport (34). The Device Security Passport (DSP) is intended to provide a structured, machine-readable record that consolidates relevant security information about an IoT component and makes it accessible to stakeholders across the supply chain.

### 5.4 Illustrative example

This section describes an illustrative example of how security claims, supporting evidence and assessment results can be expressed in a structured, machine-processable format to describe aspects of a product’s security posture.

The example does not propose a new schema or prescribe a specific format; rather, it is intended to show the relationship between a security objective, its implementation and the evidence used to assess it. Existing standards and specifications may be used, separately or together, to represent this information.

The example follows a simple cascade pattern, in which each high-level security objective is linked to its implementation actions and the results used to verify it.

- Control layer (security objectives to be addressed)

- Defines structured security objectives (e.g. ‘protection against unauthorised access’ or ‘secure update delivery’), which may be derived from secure by design and default principles and/or aligned with regulatory or recognised cybersecurity frameworks.

- Implementation layer (how controls are implemented)

- Provides claims describing the technical controls implemented to satisfy each objective, together with references to supporting evidence (e.g. ‘Implementation of TLS 1.3 with AES-256 encryption’).

- Details the specific tools (e.g. OpenSSL version, specific compiler flags), versions, configurations (e.g. ‘Strict-Transport-Security’ headers) and parameters used to instantiate the control.

- Assessment and verification layer (how claims and evidence are validated)

- Links to verifiable outputs of automated validation processes, such as timestamped test results, static analysis (SAST) summaries and cryptographic hashes of build artefacts.

These layers do not need to be contained in a single document. Claims, SBOMs, vulnerability information, build provenance, test results and other evidence may be maintained as separate but linked machine-processable artefacts.

_The SafeGate-X1 worked example (§5.4.2) is in `examples/`._

## Annex C — Mapping security principles to CRA essential requirements (indicative)

| Principle | CRA essential requirement | Implementation support |
|---|---|---|
| 4.1 Trust boundaries and threat modelling | ANNEX-1.PT1.1 | Supports identification and assessment of cybersecurity risks by making trust assumptions, assets and attack paths explicit during design |
| 4.1 Trust boundaries and threat modelling | ANNEX-1.PT1.2.d | Supports protection from unauthorised access by clarifying where authentication and access controls are required between trust boundaries |
| 4.1 Trust boundaries and threat modelling | ANNEX-1.PT1.2.e | Supports confidentiality protections by identifying where data crosses trust boundaries and requires protection |
| 4.1 Trust boundaries and threat modelling | ANNEX-1.PT1.2.f | Supports integrity protection by identifying where data, commands or configuration cross boundaries and may require integrity controls |
| 4.1 Trust boundaries and threat modelling | ANNEX-1.PT1.2.j | Supports attack surface limitation by identifying exposed interfaces and unnecessary trust relationships |
| 4.2 Least privilege | ANNEX-1.PT1.2.d | Supports protection from unauthorised access by limiting what authenticated users, services and processes are permitted to access or perform |
| 4.2 Least privilege | ANNEX-1.PT1.2.f | Supports integrity protection by limiting which identities are authorised to modify data, programs or configuration |
| 4.2 Least privilege | ANNEX-1.PT1.2.g | Supports data minimisation by limiting access to data to what is necessary for the intended purpose |
| 4.3 Strong identity and authentication architecture | ANNEX-1.PT1.2.d | Supports access protection by defining how identities are authenticated and managed across interfaces |
| 4.3 Strong identity and authentication architecture | ANNEX-1.PT1.2.l | Supports logging and monitoring of authentication and access-related activity |
| 4.4 Attack surface minimisation | ANNEX-1.PT1.2.b | Supports secure by default configuration by reducing enabled features and services at initial deployment |
| 4.4 Attack surface minimisation | ANNEX-1.PT1.2.j | Supports attack surface limitation by reducing unnecessary interfaces, services and exposed functionality |
| 4.5 Defence in depth | ANNEX-1.PT1.2.h | Supports availability and resilience by relying on multiple layers of protection rather than a single control |
| 4.5 Defence in depth | ANNEX-1.PT1.2.k | Supports impact reduction by applying multiple mitigation mechanisms that limit the effect of exploitation |
| 4.6 Open design | ANNEX-1.PT2.3 | Supports effective testing and review by using designs that can be examined and assessed |
| 4.6 Open design | ANNEX-1.PT2.4 | Supports vulnerability disclosure by aligning with transparent communication of security issues and fixes |
| 4.7 Life-cycle management | ANNEX-1.PT1.2.c | Supports the ability to address vulnerabilities over the product lifetime through updates |
| 4.7 Life-cycle management | ANNEX-1.PT1.2.m | Supports secure decommissioning by providing mechanisms to remove data and settings at end of use |
| 4.7 Life-cycle management | ANNEX-1.PT2.2 | Supports timely remediation of vulnerabilities throughout the supported life cycle |
| 4.7 Life-cycle management | ANNEX-1.PT2.7 | Supports controlled and secure distribution of updates over time |
| 4.8 User-centric design | ANNEX-1.PT1.2.b | Supports secure by default configuration that users can reasonably adopt and maintain |
| 4.9 Secure coding and verification practices | ANNEX-1.PT1.2.a | Supports release without known exploitable vulnerabilities by identifying and addressing issues during development |
| 4.9 Secure coding and verification practices | ANNEX-1.PT2.1 | Supports identification and documentation of vulnerable components during development |
| 4.9 Secure coding and verification practices | ANNEX-1.PT2.3 | Supports regular testing and review of product security during development and before release |
| 4.10 Logging, monitoring and alerting | ANNEX-1.PT1.2.d | Supports detection and reporting of unauthorised access attempts |
| 4.10 Logging, monitoring and alerting | ANNEX-1.PT1.2.l | Supports recording and monitoring of security-relevant internal activity |
| 4.11 Configuration and change management | ANNEX-1.PT1.2.f | Supports protection of configuration integrity by controlling, reviewing, and rolling back configuration changes. |
| 4.11 Configuration and change management | ANNEX-1.PT1.2.d | Supports protection from unauthorised access by restricting who can deploy or modify configurations, particularly in production environments |
| 4.12 Incident response and recovery | ANNEX-1.PT1.2.h | Supports recovery and continued availability of essential functions after incidents |
| 4.12 Incident response and recovery | ANNEX-1.PT1.2.k | Supports reduction of incident impact through prepared response and mitigation actions |
| 4.13 Vulnerability and patch management | ANNEX-1.PT2.1 | Supports identification and tracking of vulnerable components and dependencies throughout the product life cycle |
| 4.13 Vulnerability and patch management | ANNEX-1.PT2.2 | Supports timely triage and remediation of identified vulnerabilities based on risk |
| 4.13 Vulnerability and patch management | ANNEX-1.PT2.4 | Supports public disclosure of fixed vulnerabilities |
| 4.13 Vulnerability and patch management | ANNEX-1.PT2.5 | Supports coordinated handling and disclosure of vulnerabilities |
| 4.13 Vulnerability and patch management | ANNEX-1.PT2.6 | Supports mechanisms for receiving vulnerability reports from external parties |
| 4.13 Vulnerability and patch management | ANNEX-1.PT2.7 | Supports secure distribution of patches and updates |
| 4.13 Vulnerability and patch management | ANNEX-1.PT2.8 | Supports timely dissemination of security updates and related user guidance |
| 4.14 Supply-chain controls | ANNEX-1.PT1.2.a | Supports reduction of exploitable vulnerabilities introduced through compromised components |
| 4.14 Supply-chain controls | ANNEX-1.PT2.1 | Supports transparency of components and dependencies through SBOM generation |
| 4.14 Supply-chain controls | ANNEX-1.PT2.7 | Supports secure distribution of updates through protected build and release channels |
| 4.15 Minimisation of default services | ANNEX-1.PT1.2.b | Supports secure by default configuration by disabling non-essential features and services at initial deployment |
| 4.15 Minimisation of default services | ANNEX-1.PT1.2.i | Supports minimising negative impact on other services by disabling non-essential functionality that could otherwise be abused or misused |
| 4.15 Minimisation of default services | ANNEX-1.PT1.2.j | Supports limitation of attack surfaces by reducing exposed services and interfaces by default |
| 4.16 Restrictive initial access | ANNEX-1.PT1.2.b | Supports secure by default access settings by avoiding permissive initial credentials and permissions |
| 4.16 Restrictive initial access | ANNEX-1.PT1.2.d | Supports protection from unauthorised access by enforcing restrictive authentication and access-control settings at first use |
| 4.17 Secure communication by default | ANNEX-1.PT1.2.b | Supports secure by default configuration by enforcing encrypted and authenticated communications from initial connection |
| 4.17 Secure communication by default | ANNEX-1.PT1.2.e | Supports confidentiality of transmitted data by applying encryption to communications from first use |
| 4.17 Secure communication by default | ANNEX-1.PT1.2.f | Supports integrity protection of transmitted data by preventing unauthorised modification of data in transit |
| 4.18 Unique device identity and secrets by default | ANNEX-1.PT1.2.b | Supports secure by default configuration by avoiding shared credentials and shared cryptographic material |
| 4.18 Unique device identity and secrets by default | ANNEX-1.PT1.2.d | Supports protection from unauthorised access by avoiding shared credentials and enforcing unique device authentication |
| 4.18 Unique device identity and secrets by default | ANNEX-1.PT1.2.e | Supports confidentiality by preventing reuse or leakage of shared secrets across devices |
| 4.19 Mandatory security onboarding | ANNEX-1.PT1.2.b | Supports secure by default configuration by requiring critical security features to be configured before initial exposure |
| 4.19 Mandatory security onboarding | ANNEX-1.PT1.2.d | Supports protection from unauthorised access by ensuring that authentication and access controls are configured at first use |
| 4.20 Automated maintenance and updates | ANNEX-1.PT1.2.b | Supports a secure by default posture by enabling automatic security updates |
| 4.20 Automated maintenance and updates | ANNEX-1.PT1.2.c | Supports the ability to address vulnerabilities through automatic security updates enabled by default |
| 4.20 Automated maintenance and updates | ANNEX-1.PT2.2 | Supports timely remediation of vulnerabilities by reducing reliance on manual patch deployment |
| 4.20 Automated maintenance and updates | ANNEX-1.PT2.7 | Supports secure and timely distribution of security updates by enabling automated update mechanisms |
| 4.21 Transparent security posture | ANNEX-1.PT1.2.b | Supports secure by default configuration by guiding users back to a secure baseline when insecure choices are made |
| 4.21 Transparent security posture | ANNEX-1.PT1.2.l | Supports security-related information by informing users of security-relevant state changes and risks |
| 4.22 Secure recovery and ownership life cycle | ANNEX-1.PT1.2.b | Supports secure by default configuration by providing safe recovery and reset paths that restore a secure baseline |
| 4.22 Secure recovery and ownership life cycle | ANNEX-1.PT1.2.d | Supports protection from unauthorised access during recovery, reset and ownership transfer processes |
| 4.22 Secure recovery and ownership life cycle | ANNEX-1.PT1.2.m | Supports secure removal of data and settings during factory reset, decommissioning or ownership transfer |

