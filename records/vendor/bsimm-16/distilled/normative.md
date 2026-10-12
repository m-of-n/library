---
schema: "library-normative/v1"
id: bsimm-16-normative
record: bsimm-16
kind: normative
type: normative
title: "bsimm-16 — the BSIMM16 framework, verbatim"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

Source: BSIMM16 Report 2026 (sha256 `d34e341f9b5c01d43db0978a53a418b24ff56b2d0cc0371127bde9313fc14dc2`), Part 7 Table 7 (domains) and Part 8 (practices and all 128 activities). Texts are verbatim, rejoined across PDF line, column and page breaks. BSIMM is descriptive: nothing here is a mandate; each entry is an activity observed in some fraction of the 111 firms. `[id | level | firms/111 | %]` precedes each activity; % is Figure 18, and the Part 8 heading percentage is noted where it differs.

## Terminology the activities rely on (p.5, verbatim excerpt)

- "Activity. Actions or efforts carried out or facilitated by the SSG as part of a practice. Activities are divided into three levels in the BSIMM based on observation rates."

## Level semantics (p.45, verbatim)

"Level 1 activities (often straightforward and universally applicable) are those that are most observed across the data pool of 111 firms, level 2 activities (often more difficult to implement and requiring more coordination) are less frequently observed, and level 3 activities (usually more difficult to implement and not always applicable) are more rarely observed. Note that new activities are added at level 3 because we don’t yet know how common they are, so they start with zero observations."

## Domain: Governance (`bsimm-16#GOVERNANCE`)

(Part 7, Table 7 THE SOFTWARE SECURITY FRAMEWORK (p.45)) Practices that help organize, manage, and measure a software security initiative. Staff development is also a central governance practice.

### Practice SM: Strategy & Metrics (`bsimm-16#SM`)

(Part 8, GOVERNANCE: STRATEGY & METRICS (SM) (p.60)) The Strategy & Metrics practice encompasses planning, assigning roles and responsibilities, identifying software security goals, determining budgets, and identifying metrics and software release conditions.

#### [SM1.1] PUBLISH PROCESS AND EVOLVE AS NECESSARY.

`[SM1.1 | level 1 | 84/111 | 75.68%]` — Part 8, Strategy & Metrics (SM), p.60 (right column)

The process for addressing software security is defined, published internally, and broadcast to all stakeholders so that everyone knows the plan. Goals, roles, responsibilities, and activities are explicitly defined. Most organizations examine existing methodologies, such as the NIST SSDF, Microsoft SDL, or Black Duck Touchpoints, then tailor them to meet their needs. Security activities will be adapted to software lifecycle processes (e.g., waterfall, Agile, CI/CD, DevOps), so activities will evolve with both the organization and the security landscape. The process doesn’t need to be publicly promoted outside the firm to have the desired impact (see [SM3.2]). In addition to publishing the written process, some firms also automate parts (e.g., a testing strategy) as governance-as-code (see [SM3.4]).

#### [SM1.3] EDUCATE EXECUTIVES ON SOFTWARE SECURITY.

`[SM1.3 | level 1 | 66/111 | 59.46%]` — Part 8, Strategy & Metrics (SM), p.60 (right column)

Executives are regularly shown the ways malicious actors attack software and the negative business impacts those attacks can have on the organization. Go beyond reporting of open and closed defects to educate executives on the business risks, including risks of adopting emerging engineering technologies and methodologies without security oversight. Demonstrate a worst-case scenario in a controlled environment with the permission of all involved (e.g., by showing attacks and their business impact). Presentation to the board can help garner resources for new or ongoing SSI efforts. Demonstrating the need for new skill-building training in evolving areas, such as DevOps groups using cloud-native technologies, can help convince leadership to accept SSG recommendations when they might otherwise be ignored in favor of faster release dates or other priorities. Bring in an outside expert when necessary to bolster executive attention.

#### [SM1.4] IMPLEMENT SECURITY CHECKPOINTS AND ASSOCIATED GOVERNANCE.

`[SM1.4 | level 1 | 100/111 | 90.09%]` — Part 8, Strategy & Metrics (SM), p.60 (right column)

The software security process includes checkpoints (such as gates, release conditions, guardrails, milestones, etc.) at one or more points in a software lifecycle. The first two steps toward establishing security-specific checkpoint conditions are to identify process locations that are compatible with existing development practices and to then begin gathering the information necessary, such as risk-ranking thresholds or defect data, to make a go/no-go decision. Importantly, the conditions need not be enforced at this stage, e.g., the SSG can collect security testing results for each project prior to release, then provide an informed opinion on what constitutes sufficient testing or acceptable test results without trying to stop a project from moving forward (see [SM1.7]). Shorter release cycles might require creative approaches to collecting the right evidence and rely heavily on automation. Socializing the conditions and then enforcing them once most project teams already know how to succeed is a gradual approach that motivates good behavior without introducing unnecessary friction.

#### [SM1.7] ENFORCE SECURITY CHECKPOINTS AND TRACK EXCEPTIONS.

`[SM1.7 | level 1 | 71/111 | 63.96%]` — Part 8, Strategy & Metrics (SM), p.61 (left column)

Enforce security release conditions at each checkpoint (gate, guardrail, milestone, etc.) for every project, so that each project must either meet an established measure or follow a defined process for obtaining an exception to move forward. Use internal policies and standards, regulations, contractual agreements, and other obligations to define release conditions, then track all exceptions. Verifying conditions yields data that informs the KRIs and any other metrics used to govern the process. Automatically giving software a passing grade or granting exceptions without due consideration defeats the purpose of verifying conditions. Even seemingly innocuous software projects (e.g., small code changes, infrastructure access control changes, deployment blueprints) must successfully satisfy the prescribed security conditions as they progress through the software lifecycle. Similarly, APIs, frameworks, libraries, bespoke code, microservices, container configurations, etc., are all software that must satisfy security release conditions. It’s possible, and often very useful, to have verified the conditions both before and after the development process itself. In modern development environments, the verification process will increasingly become automated (see [SM3.4]).

#### [SM2.1] PUBLISH DATA ABOUT SOFTWARE SECURITY INTERNALLY AND USE IT TO DRIVE CHANGE.

`[SM2.1 | level 2 | 54/111 | 48.65%]` — Part 8, Strategy & Metrics (SM), p.61 (left column)

To facilitate improvement, data is published internally about the state of software security within the organization. Produce security or development dashboards with metrics for executives and software development management. Dashboards can be part of pipeline toolchains to enable developer self-improvement. Sometimes, this published data won’t be shared with everyone in the firm but only with the stakeholders who are tasked to drive change. In other cases, open book management and data published to all stakeholders helps everyone know what’s going on. If the organization’s culture promotes internal competition between groups, use this information to add a security dimension. Integrate automated security telemetry to gather measurements quickly and accurately to increase timeliness of security data in areas such as speed (e.g., time to fix) and quality (e.g., defect density). Publishing data about new technologies (e.g., security and risk in cloud-native architectures) is important for identifying needed improvements.

#### [SM2.3] CREATE OR GROW A SECURITY CHAMPIONS PROGRAM.

`[SM2.3 | level 2 | 55/111 | 49.55%]` — Part 8, Strategy & Metrics (SM), p.61 (left column)

Form a collection of people scattered across the organization—often called security champions—who show an above-average level of security interest or skill and who contribute software security expertise to development, QA, and operations teams. Forming this social network of advocates is a good step toward scaling security into software engineering. One way to build the initial group is to track the people who stand out during introductory training courses (see [T3.6]). Another way is to ask for volunteers. In a more top-down approach, initial champions membership is assigned to ensure good coverage of development groups, but ongoing membership is based on actual performance.

The champions can act as a sounding board for new projects and, in new or fast-moving technology areas, can help combine software security skills with domain knowledge that might be under-represented in the SSG or engineering teams. Agile coaches, scrum masters, and DevOps engineers can make particularly useful champions members, especially for detecting and removing process friction. In some environments, champions-led efforts are delivered via automation (e.g., as-code).

#### [SM2.6] REQUIRE SECURITY SIGN-OFF PRIOR TO SOFTWARE RELEASE.

`[SM2.6 | level 2 | 62/111 | 55.86%]` — Part 8, Strategy & Metrics (SM), p.61 (right column)

The organization has an initiative-wide process for documenting accountability and accepting security risk by having a risk owner use SSG-approved criteria to sign off on the state of all software prior to release. The sign-off policy might also require the accountable person to, e.g., acknowledge critical vulnerabilities that have not been mitigated or SSDL steps that have been skipped. Informal or uninformed risk acceptance alone isn’t a security sign-off because the act of accepting risk is more effective when it’s formalized (e.g., with a signature, a form submission, or something similar) and captured for future reference. Similarly, simply stating that certain projects don’t need sign-off at all won’t achieve the desired risk management results. In some cases, however, the risk owner can provide the sign-off on a particular set of software project acceptance criteria, which are then implemented in automation to provide governance-as-code (see [SM3.4]), but there must be an ongoing verification that the criteria remain accurate and the automation is working.

#### [SM2.7] CREATE EVANGELISM ROLE AND PERFORM INTERNAL MARKETING.

`[SM2.7 | level 2 | 49/111 | 44.14%]` — Part 8, Strategy & Metrics (SM), p.61 (right column)

Build support for software security throughout the organization via ongoing evangelism and ensure that everyone aligns on security objectives. This internal marketing function, often performed by a variety of stakeholder roles, keeps executives and others up to date on the magnitude of the software security problem and the elements of its solution. A champion or a scrum master familiar with security, for example, could help teams adopt better software security practices as they transform to Agile and DevOps methods. Similarly, a cloud expert could demonstrate the changes needed in security architecture and testing for serverless applications. Evangelists can increase understanding and build credibility by giving talks to internal groups (including executives), publishing roadmaps, authoring technical papers for internal consumption, or creating a collection of papers, books, and other resources on an internal website (see [SR1.2]) and promoting its use. In turn, organizational feedback becomes a useful source of improvement ideas.

#### [SM3.1] USE A SOFTWARE ASSET TRACKING APPLICATION WITH PORTFOLIO VIEW.

`[SM3.1 | level 3 | 31/111 | 27.93%]` — Part 8, Strategy & Metrics (SM), p.61 (right column)

The SSG uses centralized tracking automation to chart the progress of every piece of software and deployable artifact, from creation to decommissioning, regardless of development methodology. The automation records the security activities scheduled, in progress, and completed, incorporating results from SSDL activities even when they happen in a tight loop or during deployment. The combined inventory and security posture view enables timely decision-making. The SSG uses the automation to generate portfolio reports for multiple metrics and, in many cases, publishes this data at least among executives. As an initiative matures and activities become more distributed, the SSG uses the centralized reporting system to keep track of all the moving parts.

#### [SM3.2] MAKE SSI EFFORTS PART OF EXTERNAL MARKETING.

`[SM3.2 | level 3 | 25/111 | 22.52%]` — Part 8, Strategy & Metrics (SM), p.62 (left column)

To build external awareness, the SSG helps market the SSI beyond internal teams. The process of sharing details externally and inviting critique is used to bring new perspectives into the firm. Promoting the SSDL externally can turn security efforts into a market differentiator, and feedback from external marketing can grow an SSI’s risk reduction exercises into a competitive advantage. The SSG might provide details at external conferences or trade shows. In some cases, a complete SSDL methodology can be published and promoted outside the firm, and governance-as-code concepts can make interesting case studies.

#### [SM3.3] IDENTIFY METRICS AND USE THEM TO DRIVE RESOURCING.

`[SM3.3 | level 3 | 30/111 | 27.03%]` — Part 8, Strategy & Metrics (SM), p.62 (left column)

The SSG and its management identify metrics that define and measure SSI progress in quantitative terms. These metrics are reviewed on a regular basis and drive the initiative’s budgeting and resource allocations, so simple counts and out-of-context measurements won’t suffice here. On the technical side, one such metric could be defect density, a reduction of which could be used to show a decreasing cost of remediation over time, assuming, of course, that testing depth has kept pace with software changes. Data for metrics is best collected early and often using event-driven processes with telemetry rather than relying on calendar-driven data collection. The key is to tie security results to business objectives in a clear and obvious fashion to justify resourcing. Because the concept of security is already tenuous to many businesspeople, make the tie-in explicit.

#### [SM3.4] INTEGRATE SOFTWARE-DEFINED LIFECYCLE GOVERNANCE.

`[SM3.4 | level 3 | 9/111 | 8.11%]` — Part 8, Strategy & Metrics (SM), p.62 (left column)

Organizations begin replacing traditional document-, presentation-, and spreadsheet-based lifecycle management with software-based delivery platforms. For some software lifecycle phases, humans are no longer the primary drivers of progression from one phase to the next. Instead, organizations rely on automation to drive the management and delivery process with software such as Spinnaker or GitHub, and humans participate asynchronously (and often optionally). Automation often extends beyond the scope of CI/CD to include functional and nonfunctional aspects of delivery, such as health checks, cut-over on failure, rollback to known-good state, defect discovery and management, compliance verification, and a way to ensure adherence to policies and standards. Some organizations are also evolving their lifecycle management approach by integrating their compliance and defect discovery data, perhaps augmented by intelligence feeds and other external data, to begin moving from a series of point-in-time go/no-go decisions (e.g., release conditions) to a future state of continuous accumulation of assurance data (see [CMVM3.6]).

#### [SM3.5] INTEGRATE SOFTWARE SUPPLY CHAIN RISK MANAGEMENT.

`[SM3.5 | level 3 | 5/111 | 4.50%]` — Part 8, Strategy & Metrics (SM), p.62 (right column)

Organizational risk management processes ensure that important software created by and entering the organization is managed through policy-driven access and usage controls, maintenance standards (see [SE3.9]), and captured software provenance data (see [SE2.4]). Apply these processes to external (see [SR2.7]), bespoke, and internally developed software (see [SE3.9]) to help ensure that deployed code has the expected components (see [SE3.8]). The lifecycle management for all software, from creation or importation through secure deployment, ensures that all access, usage, and modifications are done in accordance with policy. This assurance is easier to implement at scale using automation in software lifecycle processes (see [SM3.4]).

### Practice CP: Compliance & Policy (`bsimm-16#CP`)

(Part 8, GOVERNANCE: COMPLIANCE & POLICY (CP) (p.62)) The Compliance & Policy practice is focused on identifying controls for compliance regimens such as PCI DSS and GDPR, developing contractual controls such as SLAs to help manage COTS risk, setting organizational software security policy, and auditing against that policy.

#### [CP1.1] UNIFY REGULATORY PRESSURES.

`[CP1.1 | level 1 | 88/111 | 79.28%]` — Part 8, Compliance & Policy (CP), p.62 (right column)

Have a cross-functional team that understands the constraints imposed on software security by regulatory or compliance drivers that are applicable to the organization and its customers. The team takes a common approach that removes redundancy and conflicts to unify compliance requirements, such as from PCI security standards; GLBA, SOX, and HIPAA in the US; or GDPR in the EU. A formal approach will map applicable portions of regulations to controls (see [CP2.3]) applied to software to explain how the organization complies. Existing business processes run by legal, product management, or other risk and compliance groups outside the SSG could serve as the regulatory focal point, with the SSG providing software security knowledge. A unified set of software security guidance for meeting regulatory pressures ensures that compliance work is completed as efficiently as possible.

#### [CP1.2] IDENTIFY PRIVACY OBLIGATIONS.

`[CP1.2 | level 1 | 94/111 | 84.68%]` — Part 8, Compliance & Policy (CP), p.62 (right column)

The SSG identifies privacy obligations stemming from regulation and customer expectations, then translates these obligations into both software requirements and privacy best practices. The way software handles PII might be explicitly regulated, but even if it isn’t, privacy is an important topic. For example, if the organization processes credit card transactions, the SSG will help in identifying the privacy constraints that the PCI DSS places on the handling of cardholder data and will inform all stakeholders (see [SR1.3]). Note that outsourcing to hosted environments (e.g., the cloud) doesn’t relax privacy obligations and can even increase the difficulty of recognizing and meeting all associated needs. Also, note that firms creating software products that process PII when deployed in customer environments might meet this need by providing privacy controls and guidance for their customers. Evolving consumer privacy expectations, the proliferation of “software is in everything,” and data scraping and correlation (e.g., social media) add additional expectations and complexities for PII protection.

#### [CP1.3] CREATE POLICY.

`[CP1.3 | level 1 | 92/111 | 82.88%]` — Part 8, Compliance & Policy (CP), p.63 (left column)

The SSG guides the organization by creating or contributing to software security policies that satisfy internal, regulatory, and customer-driven security requirements. This policy is what is permitted and denied at the initiative level—if it’s not mandatory and enforced, it’s not policy. The policies include a unified approach for satisfying the (potentially lengthy) list of security drivers at the governance level so that project teams can avoid keeping up with the details involved in complying with all applicable regulations or other mandates. Likewise, project teams won’t need to relearn customer security requirements on their own. Architecture standards and coding guidelines aren’t examples of policy, but policy that prescribes and mandates their use for certain software categories falls under this umbrella. In many cases, policy statements are translated into automation to provide governance-as-code. Even if not enforced by humans, policy that’s been automated must still be mandatory. In some cases, policy will be documented exclusively as governance as-code (see [SM3.4]), often as tool configuration, but it must still be readily readable, auditable, and editable by humans.

#### [CP2.1] BUILD A PII INVENTORY.

`[CP2.1 | level 2 | 46/111 | 41.44%]` — Part 8, Compliance & Policy (CP), p.63 (left column)

The organization identifies and tracks the kinds of PII processed or stored by each of its systems, along with their associated data repositories. In general, simply noting which applications process PII isn’t enough—the type of PII (e.g., PHI, PFI, PI) and where it’s stored are necessary so that the inventory can be easily referenced in critical situations. This usually includes making a list of databases that would require customer notification if breached or a list to use in crisis simulations (see [CMVM3.3]). Build the PII inventory by starting with each individual application and noting its PII use or by starting with PII types and noting the applications that touch each one. System architectures have evolved such that PII will often flow into cloud-based service and endpoint device ecosystems, then come to rest there (e.g., content delivery networks, workflow systems, mobile devices, IoT devices), making it tricky to keep an accurate PII inventory.

#### [CP2.2] REQUIRE SECURITY SIGN-OFF FOR COMPLIANCE-RELATED RISK.

`[CP2.2 | level 2 | 56/111 | 50.45%]` — Part 8, Compliance & Policy (CP), p.63 (left column)

The organization has a formal compliance risk acceptance sign-off and accountability process that addresses all software development projects. In this process, the SSG acts as an advisor while the risk owner signs off on the software’s compliance state prior to release based on its adherence to documented criteria. The sign-off policy might also require the head of the business unit to, e.g., acknowledge compliance issues that haven’t been mitigated or compliance-related SSDL steps that have been skipped, but sign-off is required even when no compliance-related risk is present. Sign-off is explicit and captured for future reference, with any exceptions tracked, even in automated application lifecycle methodologies. Note that an application without security defects might still be noncompliant, so clean security testing results are not a substitute for a compliance sign-off. Even in DevOps organizations where engineers have the technical ability to release software, there is still a need for a deliberate risk acceptance step even if the compliance criteria are embedded in automation (see [SM3.4]). In cases where the risk owner signs off on a particular set of compliance acceptance criteria that are then implemented in automation to provide governance as-code, there must be ongoing verification that the criteria remain accurate and the automation is actually working.

#### [CP2.3] IMPLEMENT AND TRACK CONTROLS FOR COMPLIANCE.

`[CP2.3 | level 2 | 63/111 | 56.76%]` — Part 8, Compliance & Policy (CP), p.63 (right column)

The organization can demonstrate compliance with applicable requirements because its SSDL is aligned with the control statements that were developed by the SSG in collaboration with compliance stakeholders (see [CP1.1]). The SSG collaborates with stakeholders to track controls, navigate problem areas, and ensure that auditors and regulators are satisfied. The SSG can then remain in the background when the act of following the SSDL automatically generates the desired compliance evidence predictably and reliably. Increasingly, the DevOps approach embeds compliance controls in automation, such as in software-defined infrastructure and networks, rather than in human process and manual intervention. A firm doing this properly can explicitly associate satisfying its compliance concerns with following its SSDL.

#### [CP2.4] INCLUDE SOFTWARE SECURITY SLAs IN ALL VENDOR CONTRACTS.

`[CP2.4 | level 2 | 61/111 | 54.95%]` — Part 8, Compliance & Policy (CP), p.63 (right column)

Software vendor contracts include an SLA to ensure that the vendor’s security efforts align with the organization’s security and compliance story. Each new or renewed contract contains provisions requiring the vendor to address software security and deliver a product or service compatible with the organization’s security policy. In some cases, open source licensing concerns initiate the vendor management process, which can open the door for additional software security language in the SLA (see [SR2.5]). Typical provisions set requirements for policy conformance, incident management, training, defect management, and response times for addressing software security issues. Traditional IT security requirements and a simple agreement to allow penetration testing or another defect discovery method aren’t sufficient here.

#### [CP2.5] ENSURE EXECUTIVE AWARENESS OF COMPLIANCE AND PRIVACY OBLIGATIONS.

`[CP2.5 | level 2 | 68/111 | 61.26%]` — Part 8, Compliance & Policy (CP), p.63 (right column)

Gain buy-in around compliance and privacy obligations by providing executives with plain-language explanations of both the organization’s compliance and privacy requirements and the potential consequences of failing to meet those requirements. For some organizations, explaining the direct cost and likely fallout from a compliance failure or data breach can be an effective way to broach the subject. For others, having an outside expert address the board works because some executives value an outside perspective more than an internal one. A sure sign of proper executive buy-in is an acknowledgment of the need along with adequate allocation of resources to meet those obligations. Use the sense of urgency that typically follows a compliance or privacy failure to build additional awareness and bootstrap new efforts.

#### [CP3.1] DOCUMENT A SOFTWARE COMPLIANCE STORY.

`[CP3.1 | level 3 | 40/111 | 36.04%]` — Part 8, Compliance & Policy (CP), p.63 (right column)

The SSG can demonstrate the organization’s up-to-date software security compliance story on demand. A compliance story is a collection of data, artifacts, policy controls, or other documentation that shows the compliance state of the organization’s software and processes. Often, senior management, auditors, and regulators—whether government or other—will be satisfied with the same kinds of reports that can be generated directly from various tools. In some cases, particularly where organizations leverage shared responsibility through cloud services, the organization will require additional information from vendors about how that vendor’s controls support organizational compliance needs. It will often be necessary to normalize information that comes from disparate sources.

#### [CP3.2] ENSURE COMPATIBLE VENDOR POLICIES.

`[CP3.2 | level 3 | 41/111 | 36.94%]` — Part 8, Compliance & Policy (CP), p.64 (left column)

Ensure that vendor software security policies and SSDL processes are compatible with internal policies. Vendors likely comprise a diverse group—cloud providers, middleware providers, virtualization providers, container and orchestration providers, bespoke software creators, contractors, and many more—and each might be held to different policy requirements. Policy adherence enforcement might be through a point-in-time review (such as ensuring acceptance criteria), automated checks (such as those applied to pull requests, committed artifacts like containers, or similar), or convention and protocol (such as preventing services connection unless security settings are correct and expected certificates are present). Evidence of vendor adherence could include results from SSDL activities, from manual tests or tests built directly into automation or infrastructure, or from other software lifecycle instrumentation. For some policies or SSDL processes, vendor questionnaire responses and attestation alone might be sufficient.

#### [CP3.3] DRIVE FEEDBACK FROM SOFTWARE LIFECYCLE DATA BACK TO POLICY.

`[CP3.3 | level 3 | 15/111 | 13.51%]` — Part 8, Compliance & Policy (CP), p.64 (left column)

Feed information from the software lifecycle into the policy creation and maintenance process to drive improvements, such as in defect prevention and strengthening governance-as-code practices (see [SM3.4]). With this feedback as a routine process, blind spots can be eliminated by mapping them to trends in SSDL failures. Events such as the regular appearance of inadequate architecture analysis, recurring vulnerabilities, ignored security release conditions, or the wrong vendor choice for carrying out a penetration test can expose policy weakness (see [CP1.3]). As an example, lifecycle data including KPIs, OKRs, KRIs, SLIs, SLOs, or other organizational metrics can indicate where policies impose too much bureaucracy by introducing friction that prevents engineering from meeting the expected delivery cadence. Rapid technology evolution might also create policy gaps that must be addressed. Over time, policies become more practical and easier to carry out (see [SM1.1]). Ultimately, policies are refined with SSDL data to enhance and improve effectiveness.

### Practice T: Training (`bsimm-16#T`)

(Part 8, GOVERNANCE: TRAINING (T) (p.64)) Training has always played a critical role in software security because organizational stakeholders across GRC, legal, engineering, operations, and other groups often start with little security knowledge.

#### [T1.1] CONDUCT SOFTWARE SECURITY AWARENESS TRAINING.

`[T1.1 | level 1 | 61/111 | 54.95%]` — Part 8, Training (T), p.64 (left column)

To promote a culture of software security throughout the organization, the SSG conducts periodic software security awareness training. This training might be delivered via SSG members, security champions, an outside firm, the internal training organization, or e-learning, but course content isn’t necessarily tailored for a specific audience—developers, QA engineers, and project managers could attend the same “Introduction to Software Security” course, for example. Augment this content with a tailored approach that addresses the firm’s culture explicitly, which might include the process for building security in, avoiding common mistakes, and technology topics such as CI/CD and DevSecOps. Generic introductory courses that only cover basic IT or high-level security concepts don’t generate satisfactory results. Likewise, awareness training aimed only at developers and not at other roles in the organization is insufficient.

#### [T1.7] DELIVER ON-DEMAND INDIVIDUAL TRAINING.

`[T1.7 | level 1 | 61/111 | 54.95%]` — Part 8, Training (T), p.64 (right column)

The organization lowers the burden on students and reduces the cost of delivering software security training by offering on-demand training for SSDL stakeholders. The most obvious choice, e-learning, can be kept up to date through a subscription model, but an online curriculum must be engaging and relevant to students in various roles (e.g., developer, QA, cloud, ops) to achieve its intended purpose. Ineffective (e.g., aged, off-topic) training or training that isn’t used won’t create any change. Hot engineering topics like containerization and security orchestration, and new training delivery styles such as gamification, will attract more interest than boring policy discussions. For developers, it’s possible to provide training directly through the IDE right when it’s needed, but in some cases, building a new skill (such as cloud security or threat modeling) might be better suited for instructor-led training, which can also be provided on demand.

#### [T1.8] INCLUDE SECURITY RESOURCES IN ONBOARDING.

`[T1.8 | level 1 | 52/111 | 46.85%]` — Part 8, Training (T), p.64 (right column)

The process for bringing new hires into a software engineering organization requires timely completion of a training module about software security. While the generic new hire process usually covers topics like picking a good password and avoiding phishing, this orientation period is enhanced to cover topics such as how to create, deploy, and operate secure code, the SSDL, security standards (see [SR1.1]), and internal security resources (see [SR1.2]). The objective is to ensure that new hires contribute to the security culture as soon as possible. Although a generic onboarding module is useful, it doesn’t take the place of a timely and more complete introductory software security course.

#### [T2.5] ENHANCE SECURITY CHAMPIONS THROUGH TRAINING AND EVENTS.

`[T2.5 | level 2 | 30/111 | 27.03%]` — Part 8, Training (T), p.64 (right column)

Strengthen the security champions network (see [SM2.3]) by inviting guest speakers or holding special events about advanced software security topics. This effort is about providing to the champions customized training (e.g., the latest software security techniques for DevOps or serverless technologies or on the implications of new policies and standards) so that it can fulfill its assigned responsibilities—it’s not about inviting champions members to routine brown bags or signing them up for standard computer-based training. Similarly, a standing conference call with voluntary attendance won’t get the desired results, which are as much about building camaraderie as they are about sharing knowledge and organizational efficiency. Regular events build community and facilitate collaboration and collective problem-solving. Face-to-face meetings are by far the most effective, even if they happen only once or twice a year and even if some participants must attend by videoconferencing. In teams with many geographically dispersed and work-from-home members, simply turning on cameras and ensuring that everyone gets a chance to speak makes a substantial difference.

#### [T2.8] CREATE AND USE MATERIAL SPECIFIC TO COMPANY HISTORY.

`[T2.8 | level 2 | 25/111 | 22.52%]` — Part 8, Training (T), p.65 (left column)

To make a strong and lasting change in behavior, training includes material specific to the company’s history of software security challenges. When participants can see themselves in a problem, they’re more likely to understand how the material is relevant to their work as well as when and how to apply what they’ve learned. One way to do this is to use noteworthy attacks on the company’s software as examples in the training curriculum. Both successful and unsuccessful attacks, as well as notable results from penetration tests, design review, and red team exercises, can make good teachable moments. Stories from company history can help steer training in the right direction but only if those stories are still relevant and not overly censored. This training should cover platforms used by developers (developers orchestrating containers probably won’t care about old virtualization problems) and problems relevant to languages in common use.

#### [T2.9] DELIVER ROLE-SPECIFIC ADVANCED CURRICULUM.

`[T2.9 | level 2 | 30/111 | 27.03%]` — Part 8, Training (T), p.65 (left column)

Software security training goes beyond building awareness (see [T1.1]) to enabling students to incorporate security practices into their work. This training is tailored to cover the tools, technology stacks, development methodologies, and issues that are most relevant to the students. An organization could offer tracks for its engineers, for example, supplying one each for architects, developers, operations, DevOps, site reliability engineers, and testers. Tool-specific training is also commonly needed in such a curriculum. While it might be more concise than engineering training, role-specific training is also necessary for many other stakeholders within an organization, including product management, executives, and others. In any case, the training must be taken by a broad enough audience to build the collective skillsets required.

#### [T2.10] HOST SOFTWARE SECURITY EVENTS.

`[T2.10 | level 2 | 21/111 | 18.92%]` — Part 8, Training (T), p.65 (left column)

The organization hosts security events featuring external speakers and content in order to strengthen its security culture. Good examples of such events are Intel iSecCon and AWS re:Inforce, which invite all employees, feature external presenters, and focus on helping engineering create, deploy, and operate better code. Employees benefit from hearing outside perspectives, especially those related to fast-moving technology areas with software security ramifications, and the organization benefits from putting its security credentials on display (see [SM3.2]). Events open only to small, select groups or simply putting recordings on an internal portal won’t result in the desired culture change across the organization.

#### [T2.11] REQUIRE AN ANNUAL REFRESHER.

`[T2.11 | level 2 | 30/111 | 27.03%]` — Part 8, Training (T), p.65 (left column)

Everyone involved in the SSDL is required to take an annual software security refresher course. This course keeps the staff up to date on the organization’s security approach and ensures that the organization doesn’t lose focus due to turnover, evolving methodologies, or changing deployment models. The SSG might give an update on the security landscape and explain changes to policies and standards. A refresher could also be rolled out as part of a firmwide security day or in concert with an internal security conference. While one refresher module can be used for multiple roles (see [T2.9]), coverage of new topics and changes to the previous year’s content should result in a significant amount of fresh content.

#### [T2.12] PROVIDE EXPERTISE VIA OPEN COLLABORATION CHANNELS.

`[T2.12 | level 2 | 45/111 | 40.54%]` — Part 8, Training (T), p.65 (right column)

Software security experts offer help to anyone in an open manner during regularly scheduled office hours or openly accessible channels on Slack, Jira, or similar. By acting as an informal resource for people who want to solve security problems, the SSG leverages teachable moments and emphasizes the carrot over the stick approach to security best practices. Office hours might be hosted one afternoon per week by a senior SSG member, perhaps inviting briefings from product or application groups working on hard security problems. Slack and other messaging applications can capture questions 24x7, functioning as an office hours platform when appropriate subject matter experts are consistently part of the conversation and are ensuring that the answers generated align with SSG expectations. An online approach has the added benefit of discussions being recorded and searchable.

#### [T3.1] REWARD PROGRESSION THROUGH CURRICULUM.

`[T3.1 | level 3 | 8/111 | 7.21%]` — Part 8, Training (T), p.65 (right column)

Progression through the security curriculum brings personal benefits, such as public acknowledgement or career advancement. The reward system can be formal and lead to a certification or an official mark in the human resources system, or it can be less formal and include motivators such as documented praise at annual review time. Involving a corporate training department and human resources team can make the impact of improving security skills on career progression more obvious, but the SSG should continue to monitor security knowledge in the firm and not cede complete control or oversight. Coffee mugs and t-shirts can build morale, but it usually takes the possibility of real career progression to change behavior.

#### [T3.2] PROVIDE TRAINING FOR VENDORS AND OUTSOURCED WORKERS.

`[T3.2 | level 3 | 21/111 | 18.92%]` — Part 8, Training (T), p.65 (right column)

Vendors and outsourced workers receive appropriate software security training, comparable to the level of training given to employees. Spending time and effort helping suppliers get security right at the outset is much easier than trying to determine what went wrong later, especially if the development team has moved on to other projects. Training individual contractors is much more natural than training entire outsourced firms and is a reasonable place to start. It’s important that everyone who works on the firm’s software has an appropriate level of training that increases their capability of meeting the software security expectations for their role, regardless of their employment status. Of course, some vendors and outsourced workers might have received adequate training from their own firms, but that should always be verified.

#### [T3.6] IDENTIFY NEW SECURITY CHAMPIONS THROUGH OBSERVATION.

`[T3.6 | level 3 | 8/111 | 7.21%]` — Part 8, Training (T), p.66 (left column)

Future security champions are recruited by noting people who stand out during opportunities that show skill and enthusiasm, such as training courses, office hours, capture-the-flag exercises, hack-a-thons, etc., and then encouraging them to join the champions. Pay particular attention to practitioners who are contributing things such as code, security configurations, or defect discovery rules. The champions program often begins as an assigned collection of people scattered across the organization who show an above-average level of security interest or advanced knowledge of new technology stacks and development methodologies (see [SM2.3]). Identifying future members proactively is a step toward creating a social network that speeds the adoption of security into software development and operations. A group of enthusiastic and skilled volunteers will be easier to lead than a group that is drafted.

## Domain: Intelligence (`bsimm-16#INTELLIGENCE`)

(Part 7, Table 7 THE SOFTWARE SECURITY FRAMEWORK (p.45)) Practices that result in collections of corporate knowledge used in carrying out software security activities throughout the organization. Collections include both proactive security guidance and organizational threat modeling.

### Practice AM: Attack Models (`bsimm-16#AM`)

(Part 8, INTELLIGENCE: ATTACK MODELS (AM) (p.66)) Attack Models capture information used to think like an attacker, including threat modeling inputs, abuse cases, data classification, and technology-specific attack patterns.

#### [AM1.2] USE A DATA CLASSIFICATION SCHEME FOR SOFTWARE INVENTORY.

`[AM1.2 | level 1 | 57/111 | 51.35%]` — Part 8, Attack Models (AM), p.66 (left column)

Security stakeholders in an organization agree on a data classification scheme and use it to inventory software, delivery artifacts (e.g., containers), and associated persistent data stores according to the kinds of data processed or services called, regardless of deployment model (e.g., on- or off-premises). Many classification schemes are possible—one approach is to focus on PII, for example. Depending on the scheme and the software involved, it could be easiest to first classify data repositories (see [CP2.1]), then derive classifications for applications according to the repositories they use. Other approaches include data classification according to protection of intellectual property, impact of disclosure, exposure to attack, relevance to GDPR, and geographic boundaries.

#### [AM1.3] IDENTIFY POTENTIAL ATTACKERS.

`[AM1.3 | level 1 | 44/111 | 39.64%]` — Part 8, Attack Models (AM), p.66 (left column)

The SSG identifies potential attackers in order to understand and begin documenting their motivations and abilities. The outcome of this periodic exercise could be a set of attacker profiles that includes outlines for categories of attackers and more detailed descriptions for noteworthy individuals that are used in end-to-end design review (see [AA1.2]). In some cases, a third-party vendor might be contracted to provide this information. Specific and contextual attacker information is almost always more useful than generic information copied from someone else’s list. Moreover, a list that simply divides the world into insiders and outsiders won’t drive useful results. Identification of attackers should also consider the organization’s evolving software supply chain, attack surface, theoretical internal attackers, and contract staff.

#### [AM1.5] GATHER AND USE ATTACK INTELLIGENCE.

`[AM1.5 | level 1 | 78/111 | 70.27%]` — Part 8, Attack Models (AM), p.66 (right column)

The SSG ensures the organization stays ahead of the curve by learning about new types of attacks and vulnerabilities, then adapts that information to the organization’s needs. Attack intelligence must be made actionable and useful for a variety of consumers, which might include developers, testers, DevOps, security operations, and reliability engineers, among others. In many cases, a subscription to a commercial service can provide a reasonable way of gathering basic attack intelligence related to applications, APIs, containerization, orchestration, cloud environments, etc. Attending technical conferences and monitoring attacker forums, then correlating that information with what’s happening in the organization (perhaps by leveraging automation to mine operational logs and telemetry) helps everyone learn more about emerging vulnerability exploitation.

#### [AM2.1] BUILD ATTACK PATTERNS AND ABUSE CASES TIED TO POTENTIAL ATTACKERS.

`[AM2.1 | level 2 | 20/111 | 18.02%]` — Part 8, Attack Models (AM), p.66 (right column)

The SSG works with stakeholders to build attack patterns and abuse cases tied to potential attackers (see [AM1.3]). Attack patterns frequently contain details of the targeted asset, attackers, goals, and the techniques used. These resources can be built from scratch or from standard sets, such as the MITRE ATT&CK framework, with the SSG adding to the pile based on its own attack stories to prepare the organization for SSDL activities such as design review and penetration testing. For example, a story about an attack against a poorly designed cloud-native application could lead to a containerization attack pattern that drives a new type of testing (see [ST3.5]). If a firm tracks the fraud and monetary costs associated with specific attacks, this information can in turn be used to prioritize the process of building attack patterns and abuse cases. Organizations will likely need to evolve both their attack pattern and abuse case creation prioritization and their content over time due to changing software architectures (e.g., zero trust, cloud native, serverless), attackers, and technologies.

#### [AM2.6] COLLECT AND PUBLISH ATTACK STORIES.

`[AM2.6 | level 2 | 16/111 | 14.41%]` — Part 8, Attack Models (AM), p.66 (right column)

To maximize the benefit from lessons that don’t always come cheap, the SSG collects and publishes stories about attacks against the organization’s software. Both successful and unsuccessful attacks can be noteworthy, and discussing historical information about software attacks has the added effect of grounding software security in a firm’s reality. This is particularly useful in training classes (see [T2.8]) to help counter a generic approach that might be overly focused on other organizations’ most common bug lists or outdated platform attacks. Hiding or overly sanitizing information about attacks from people building new systems fails to garner any positive benefits from a negative event.

#### [AM2.7] BUILD AN INTERNAL FORUM TO DISCUSS ATTACKS.

`[AM2.7 | level 2 | 18/111 | 16.22%]` — Part 8, Attack Models (AM), p.66 (right column)

The organization has an internal, interactive forum where the SSG, champions, incident response, and others discuss attacks and attack methods. The discussion serves to communicate the attacker perspective to everyone, so it’s useful to include all successful attacks here, regardless of attack source, such as supply chain, internal, consultants, or bug bounty contributors.

The SSG augments the forum with an internal communication channel (see [T2.12]) that encourages subscribers to discuss the latest information on publicly known incidents. Dissection of attacks and exploits that are relevant to a firm are particularly helpful when they spur discussion of software, infrastructure, and other mitigations. Simply republishing items from public mailing lists doesn’t achieve the same benefits as active and ongoing discussions, nor does a closed discussion hidden from those creating code and configurations. Everyone should feel free to ask questions and learn about vulnerabilities and exploits.

#### [AM2.8] HAVE A RESEARCH GROUP THAT DEVELOPS NEW ATTACK METHODS.

`[AM2.8 | level 2 | 26/111 | 23.42%]` — Part 8, Attack Models (AM), p.67 (left column)

A research group works to identify and mitigate the impact of new classes of attacks and shares their knowledge with stakeholders. Identification does not always require original research—the group might expand on an idea discovered by others. Doing this research in-house is especially important for early adopters of new technologies and configurations so that they can discover potential weaknesses before attackers do. One approach is to create new attack methods that simulate persistent attackers during goal-oriented red team exercises (see [PT3.1]). This isn’t a penetration testing team finding new instances of known types of weaknesses, it’s a research group that innovates attack methods and mitigation approaches. Example mitigation approaches include test cases, static analysis rules, attack patterns, standards, and policy changes. Some firms provide researchers time to follow through on their discoveries by using bug bounty programs or other means of coordinated disclosure (see [CMVM2.4]). Others allow researchers to publish their findings at conferences like DEF CON to benefit everyone.

#### [AM2.9] MONITOR AUTOMATED ASSET CREATION.

`[AM2.9 | level 2 | 22/111 | 19.82%]` — Part 8, Attack Models (AM), p.67 (left column)

Implement technology controls that provide a continuously updated view of the various network, machine, software, and related infrastructure assets being instantiated by engineering teams. To help ensure proper coverage, the SSG works with engineering teams (including potential shadow IT teams) to understand orchestration, cloud configuration, and other self-service means of software delivery to ensure proper monitoring. This monitoring requires a specialized effort—normal system, network, and application logging and analysis won’t suffice. Success might require a multi-pronged approach, including consuming orchestration and virtualization metadata, querying cloud service provider APIs, and outside-in crawling and scraping.

#### [AM3.2] CREATE AND USE AUTOMATION TO MIMIC ATTACKERS.

`[AM3.2 | level 3 | 5/111 | 4.50%]` — Part 8, Attack Models (AM), p.67 (left column)

The SSG arms engineers, testers, and incident response with automation to mimic what attackers are going to do. For example, a new attack method identified by an internal research group (see [AM2.8]) or a disclosing third party could require a new tool, so the SSG, perhaps through the security champions, could package the tool and distribute it to testers. The idea here is to push attack capability past what typical commercial tools and offerings encompass, then make that knowledge and technology easy for others to use. Mimicking attackers, especially attack chains, almost always requires tailoring tools to a firm’s particular technology stacks, infrastructure, and configurations. When technology stacks and coding languages evolve faster than vendors can innovate, creating tools and automation in-house might be the best way forward. In the DevOps world, these tools might be created by engineering and embedded directly into toolchains and automation (see [ST3.6]).

#### [AM3.4] CREATE TECHNOLOGY- SPECIFIC ATTACK PATTERNS.

`[AM3.4 | level 3 | 9/111 | 8.11%]` — Part 8, Attack Models (AM), p.67 (right column)

The SSG facilitates technology-specific attack pattern creation by collecting and providing knowledge about attacks relevant to the organization’s technologies. For example, if the organization’s cloud software relies on a cloud vendor’s security apparatus (e.g., key and secrets management), the SSG or appropriate SMEs can help catalog the quirks of the crypto package and how it might be exploited. Attack patterns directly related to the security frontier (e.g., AI, serverless) can be useful here as well. It’s often easiest to start with existing generalized attack patterns to create the needed technology-specific ones, but simply adding “for microservices” at the end of a generalized pattern name, for example, won’t suffice.

#### [AM3.5] MAINTAIN AND USE A TOP N POSSIBLE ATTACKS LIST.

`[AM3.5 | level 3 | 12/111 | 10.81%]` — Part 8, Attack Models (AM), p.67 (right column)

The SSG periodically digests the ever-growing list of applicable attack types, creates a prioritized short list—the top N—and then uses the list to drive change. This initial list almost always combines input from multiple sources, both inside and outside the organization. Some organizations prioritize their list according to a perception of potential business loss while others might prioritize according to preventing successful attacks against their software. The top N list doesn’t need to be updated with great frequency, and attacks can be coarsely sorted. For example, the SSG might brainstorm twice a year to create lists of attacks the organization should be prepared to counter “now,” “soon,” and “someday.”

### Practice SFD: Security Features & Design (`bsimm-16#SFD`)

(Part 8, INTELLIGENCE: SECURITY FEATURES & DESIGN (SFD) (p.67)) The Security Features & Design practice is charged with creating usable security patterns for major security controls (meeting the standards defined in the Standards & Requirements practice), building components and services for those controls, and establishing collaboration during security design efforts.

#### [SFD1.1] INTEGRATE AND DELIVER SECURITY FEATURES.

`[SFD1.1 | level 1 | 85/111 | 76.58%]` — Part 8, Security Features & Design (SFD), p.67 (right column)

Provide proactive guidance on preapproved security features for engineering groups to use rather than each group implementing its own security features. Engineering groups benefit from implementations that come preapproved, and the SSG benefits by not having to repeatedly track down the kinds of subtle errors that often creep into security features (e.g., authentication, role management, key management, logging, cryptography, protocols). These security features might be discovered during SSDL activities, created by the SSG or specialized development teams, or defined in configuration templates (e.g., cloud blueprints) and delivered via mechanisms such as SDKs, containers, microservices, and APIs. Generic security features often must be tailored for specific platforms—for example, each mobile and cloud platform might need its own means by which users are authenticated and authorized, secrets are managed, and user actions are centrally logged and monitored. It’s implementing and disseminating these defined security features that generates real progress, not simply making a list of them.

#### [SFD1.2] APPLICATION ARCHITECTURE TEAMS ENGAGE WITH THE SSG.

`[SFD1.2 | level 1 | 77/111 | 69.37%]` — Part 8, Security Features & Design (SFD), p.68 (left column)

Application architecture teams take responsibility for security in the same way they take responsibility for performance, availability, scalability, and resiliency. One way to keep security from falling out of these architecture discussions is to have secure design experts (from the SSG, a vendor, etc.) participate. Increasingly, architecture discussions include developers and site reliability engineers who are governing all types of software components, such as open source, APIs, containers, and cloud services. In other cases, enterprise architecture teams have the knowledge to help the experts create secure designs that integrate properly into corporate design standards. Proactive engagement with experts is key to success here. In addition, it’s never safe for one team to assume another team has addressed security requirements—even moving a well-known system to the cloud means reengaging the experts.

#### [SFD2.1] LEVERAGE SECURE-BY-DESIGN COMPONENTS AND SERVICES.

`[SFD2.1 | level 2 | 44/111 | 39.64%]` — Part 8, Security Features & Design (SFD), p.68 (left column)

Build or provide approved secure-by-design software components and services for use by engineering teams. Prior to approving and publishing secure-by-design software components and services, including open source and cloud services, the SSG must carefully assess them for security. This assessment process to declare a component secure-by-design is usually more rigorous and in-depth than that for typical projects. In addition to teaching by example, these resilient and reusable building blocks aid important efforts such as architecture analysis and code review by making it easier to avoid mistakes. These components and services also often have features (e.g., application identity, RBAC) that enable uniform usage across disparate environments. Similarly, the SSG might further take advantage of this defined list by tailoring static analysis rules specifically for the components it offers (see [CR2.6]).

#### [SFD2.2] CREATE CAPABILITY TO SOLVE DIFFICULT DESIGN PROBLEMS.

`[SFD2.2 | level 2 | 62/111 | 55.86%]` — Part 8, Security Features & Design (SFD), p.68 (left column)

Contribute to building resilient architectures by solving design problems unaddressed by organizational security components or services, or by cloud service providers, thus minimizing the negative impact that security has on other constraints, such as feature velocity. Involving the SSG and secure design experts in application refactoring or in the design of a new protocol, microservice, or architecture feature (e.g., containerization) enables timely analysis of the security implications of existing defenses and identifies elements to be improved. Designing for security early in the new project process is more efficient than analyzing an existing design for security and then refactoring when flaws are uncovered (see [AA1.1], [AA1.2], [AA2.1]). The SSG could also get involved in what would have historically been purely engineering discussions, as even rudimentary use of cloud-native technologies (e.g., “Hello, world!”) requires proper use of configurations and other capabilities that have direct implications on security posture.

#### [SFD3.1] FORM A REVIEW BOARD TO APPROVE AND MAINTAIN SECURE DESIGN PATTERNS.

`[SFD3.1 | level 3 | 16/111 | 14.41%]` — Part 8, Security Features & Design (SFD), p.68 (right column)

A review board formalizes the process of reaching and maintaining consensus on security tradeoffs in design needs. Unlike a typical architecture committee focused on functions, this group focuses on providing security guidance, preferably in the form of patterns, standards, features, or frameworks. It also periodically reviews already published design guidance (especially around authentication, authorization, and cryptography) to ensure that design decisions don’t become stale or out of date. This review board helps control the chaos associated with adoption of new technologies when development groups might otherwise make decisions on their own without engaging the SSG or champions. Review board security guidance can also serve to inform outsourced software providers about security expectations (see [CP3.2]).

#### [SFD3.2] REQUIRE USE OF APPROVED SECURITY FEATURES AND FRAMEWORKS.

`[SFD3.2 | level 3 | 22/111 | 19.82%]` — Part 8, Security Features & Design (SFD), p.68 (right column)

Implementers must take their security features and frameworks from an approved list or repository (see [SFD1.1], [SFD2.1], [SFD3.1]). There are two benefits to this activity—developers don’t spend time reinventing existing capabilities, and review teams don’t have to contend with finding the same old defects in new projects or when new platforms are adopted. Reusing proven components eases testing, code review, and threat modeling (see [AA1.1]). Reuse is a major advantage of consistent software architecture and is particularly helpful for Agile development and velocity maintenance in CI/CD pipelines. Packaging and applying required components, such as via containerization (see [SE2.5]), makes it especially easy to reuse approved features and frameworks.

#### [SFD3.3] FIND AND PUBLISH SECURE DESIGN PATTERNS FROM THE ORGANIZATION.

`[SFD3.3 | level 3 | 11/111 | 9.91%]` — Part 8, Security Features & Design (SFD), p.68 (right column)

Foster centralized design reuse by collecting secure design patterns (sometimes referred to as security blueprints) from across the organization and publishing them for everyone to use. A section of the SSG website (see [SR1.2]) could promote positive elements identified during threat modeling or architecture analysis so that good ideas spread widely. This process is formalized—an ad hoc, accidental noticing isn’t sufficient. Common design patterns accelerate development, so it’s important to use secure design patterns, and not just for applications but for all software assets (e.g., microservices, APIs, containers, infrastructure, and automation).

### Practice SR: Standards & Requirements (`bsimm-16#SR`)

(Part 8, INTELLIGENCE: STANDARDS & REQUIREMENTS (SR) (p.68)) The Standards & Requirements practice involves eliciting explicit software security requirements from the organization, determining which COTS tools to recommend, building standards for major security controls (such as authentication and input validation), creating security standards for technologies in use, and creating a standards review process.

#### [SR1.1] CREATE SECURITY STANDARDS.

`[SR1.1 | level 1 | 82/111 | 73.87%]` — Part 8, Standards & Requirements (SR), p.68 (right column)

The organization meets the demand for security guidance by creating standards that explain the required way to adhere to policy and carry out security-centric design, development, and operations. A standard might mandate how to perform identity-based application authentication or how to implement transport-level security, perhaps with the SSG ensuring the availability of a reference implementation. Standards often apply to software beyond the scope of an application’s code, including container construction, orchestration, infrastructure as-code, and cloud security configuration. Standards can be deployed in a variety of ways to keep them actionable and relevant. For example, they can be automated into development environments (such as an IDE or toolchain) or explicitly linked to code examples and deployment artifacts (e.g., containers). In any case, to be considered standards, they must be adopted and enforced. Standards for technology stacks [SR3.4] and standards for incorporating new technologies [SR3.5] can be expected to aid in the creation of these standards but are not required.

#### [SR1.2] CREATE A SECURITY PORTAL.

`[SR1.2 | level 1 | 88/111 | 79.28%]` — Part 8, Standards & Requirements (SR), p.69 (left column)

The organization has a well-known central location for information about software security. Typically, this is an internal website maintained by the SSG and security champions that people refer to for current information on security policies, standards, and requirements, as well as for other resources (such as training). An interactive portal is better than a static portal with guideline documents that rarely change. Organizations often supplement these materials with mailing lists, chat channels (see [T2.12]), and face-to-face meetings. Development teams are increasingly putting software security knowledge directly into toolchains and automation that are outside the organization (e.g., GitHub), but that does not remove the need for SSG-led knowledge management.

#### [SR1.3] TRANSLATE COMPLIANCE CONSTRAINTS TO REQUIREMENTS.

`[SR1.3 | level 1 | 77/111 | 69.37%]` — Part 8, Standards & Requirements (SR), p.69 (left column)

Compliance constraints are translated into security requirements for individual projects and communicated to the engineering teams. This is a linchpin in the organization’s compliance strategy—by representing compliance constraints explicitly with requirements and informing stakeholders, the organization demonstrates that compliance is a manageable task. For example, if the organization builds software that processes credit card transactions, PCI DSS compliance plays a role during the security requirements phase. In other cases, technology standards built for international interoperability can include security guidance on compliance needs. Representing these standards as requirements also helps with traceability and visibility in the event of an audit. It’s particularly useful to codify the requirements into reusable code (see [SFD2.1]) or artifact deployment specifications (see [SE1.4]).

#### [SR1.5] IDENTIFY OPEN SOURCE.

`[SR1.5 | level 1 | 88/111 | 79.28%]` — Part 8, Standards & Requirements (SR), p.69 (left column)

Identify open source components and dependencies included in the organization’s code repositories and built software, then review them to understand their security posture. Organizations use a variety of tools and metadata provided by delivery pipelines to discover old versions of open source components with known vulnerabilities or that their software relies on multiple versions of the same component. Scale efforts by using automated tools to find open source, whether whole components or perhaps large chunks of borrowed code. Some software development pipeline platforms, container registries, and middleware platforms have begun to provide this visibility as metadata (e.g., SBOMs [SE3.6]) resulting from behind the-scenes artifact scanning. Some organizations combine composition analysis results from multiple phases of the software lifecycle to get a more complete and accurate list of the open source being included in production software.

#### [SR2.2] CREATE A STANDARDS REVIEW PROCESS.

`[SR2.2 | level 2 | 65/111 | 58.56% — heading prints 56.6% (source inconsistency)]` — Part 8, Standards & Requirements (SR), p.69 (right column)

Create a process to develop software security standards and ensure that all stakeholders have a chance to weigh in. This review process could operate by appointing a spokesperson for any proposed security standard, putting the onus on the person to demonstrate that the standard meets its goals and to get buy-in and approval from stakeholders. Enterprise architecture or enterprise risk groups sometimes take on the responsibility of creating and managing standards review processes. When the standards are implemented directly as software, the responsible person might be a DevOps manager, release engineer, or whoever owns the associated deployment artifact (e.g., the orchestration code). Common triggers for standards review processes include periodic updates, security incidents, major vulnerabilities discovered, adoption of new technologies, acquisition, etc.

#### [SR2.5] CREATE SLA BOILERPLATE.

`[SR2.5 | level 2 | 62/111 | 55.86%]` — Part 8, Standards & Requirements (SR), p.69 (right column)

The SSG works with the legal department to create standard SLA boilerplate for use in contracts with vendors and outsource providers, including cloud providers, to require software security efforts on their part. The legal department might also leverage the boilerplate to help prevent compliance and privacy problems. Under the agreement, vendors and outsource providers must meet company-mandated software security SLAs (see [CP2.4]). Boilerplate language might call for objective third-party insight into software security efforts, such as SSDF gap analysis (https://csrc.nist.gov/Projects/ssdf), BSIMMsc measurements, or BSIMM scores.

#### [SR2.7] CONTROL OPEN SOURCE RISK.

`[SR2.7 | level 2 | 53/111 | 47.75%]` — Part 8, Standards & Requirements (SR), p.69 (right column)

The organization has control over its exposure to the risks that come along with using open source components and all the involved dependencies, including dependencies integrated at runtime. Controlling exposure usually includes multiple efforts, with one example being responding to known vulnerabilities in identified open source (see [SR1.5]). The use of open source could also be restricted to predefined projects or to a short list of versions that have been through an approved security screening process, have had unacceptable vulnerabilities remediated, and are made available only through approved internal repositories and containers. For some use cases, policy might preclude any use of open source. The legal department often spearheads additional open source controls due to license compliance objectives and the viral license problem associated with GPL code. SSGs that partner with and educate the legal department can help move an organization to improve its open source risk management practices, which must be applied across the software portfolio to be effective.

#### [SR3.2] COMMUNICATE STANDARDS TO VENDORS.

`[SR3.2 | level 3 | 17/111 | 15.32%]` — Part 8, Standards & Requirements (SR), p.70 (left column)

Work with vendors to educate them and promote the organization’s security standards. A healthy relationship with a vendor often starts with contract language (see [CP2.4]), but the SSG should engage with vendors, discuss vendor security practices, and explain in simple terms (rather than legalese) what the organization expects. Any time a vendor adopts the organization’s security standards, it’s a clear sign of progress. Note that standards implemented as security features or infrastructure configuration could be a requirement to services integration with a vendor (see [SFD1.1], [SE1.4]). When the firm’s SSDL is publicly available, communication regarding software security expectations is easier. Likewise, sharing internal practices and measures can make expectations clear.

#### [SR3.3] USE SECURE CODING STANDARDS.

`[SR3.3 | level 3 | 19/111 | 17.12%]` — Part 8, Standards & Requirements (SR), p.70 (left column)

Developers use secure coding standards to avoid the most obvious bugs and as ground rules for code review. These standards are necessarily specific to a programming language, and they can address the use of popular frameworks, APIs, libraries, and infrastructure automation. Secure coding standards can also be for low- or no-code platforms (e.g., Microsoft Power Apps, Salesforce Lightning). While enforcement isn’t the point at this stage (see [CR3.5]), violation of standards is a teachable moment for all stakeholders. Other useful coding standards topics include proper use of cloud APIs, use of approved cryptography, memory sanitization, banned functions, open source use, and many others. If the organization already has coding standards for other purposes (e.g., style), its secure coding standards should build upon them. A clear set of secure coding standards is a good way to guide both manual and automated code review, as well as to provide relevant examples for security training. Some groups might choose to integrate their secure coding standards directly into automation. Socializing the benefits of following standards is also a good first step to gaining widespread acceptance (see [SM2.7]).

#### [SR3.4] CREATE STANDARDS FOR TECHNOLOGY STACKS.

`[SR3.4 | level 3 | 26/111 | 23.42%]` — Part 8, Standards & Requirements (SR), p.70 (left column)

The organization standardizes on the use of specific technology stacks, which translates into a reduced workload because teams don’t have to explore new technology risks for every new project. The organization might create a secure base configuration (commonly in the form of golden images, Terraform definitions, etc.) for each technology stack, further reducing the amount of work required to use the stack safely. In cloud environments, hardened configurations likely include up-to-date security patches, configurations, and services, such as logging and monitoring. In traditional on-premises IT deployments, a stack might include an operating system, a database, an application server, and a runtime environment (e.g., a MEAN stack). Standards for secure use of reusable technologies, such as containers, microservices, or orchestration code, means that getting security right in one place positively impacts the security posture of all downstream efforts (see [SE2.5]).

#### [SR3.5] CREATE STANDARDS CONTROLLING AND GUIDING THE ADOPTION OF NEW TECHNOLOGIES.

`[SR3.5 | level 3 | 2/111 | 1.80%]` — Part 8, Standards & Requirements (SR), p.70 (right column)

The SSG is involved in efforts to provide internal practices for technologies so new that industry best practices have not yet been codified. Involving the SSG in exploration efforts to understand and plan for new technology minimizes the negative impacts that insecure implementations will have by proactively accounting for potential security pitfalls. The SSG’s involvement can result in updates to policies and standards [SR1.1], new security requirements for technology stacks [SR3.4], secure-by-design components and services [SFD2.1, SFD3.2], or coding guidelines [SR3.3]. The SSG must be involved in proactive efforts surrounding the adoption of new technologies rather than merely retroactively securing existing integrations [SFD2.2] or updating policy and standards in response to changing regulations [CP1.1] or emerging threat intelligence [AM1.5]. This effort helps control the chaos associated with adoption of new technologies (such as the rise of AI and LLMs) when development groups might otherwise make decisions on their own without engaging the SSG or champions. It is all about ensuring that security is considered from the beginning instead of having to be bolted on after the fact.

## Domain: SSDL Touchpoints (`bsimm-16#SSDL-TOUCHPOINTS`)

(Part 7, Table 7 THE SOFTWARE SECURITY FRAMEWORK (p.45)) Practices associated with analysis and assurance of particular software development artifacts and processes. All software security methodologies include these practices.

### Practice AA: Architecture Analysis (`bsimm-16#AA`)

(Part 8, SDLC TOUCHPOINTS: ARCHITECTURE ANALYSIS (AA) (p.70)) Architecture analysis encompasses capturing software architecture in concise diagrams, applying lists of risks and threats, adopting a process for review (such as Microsoft Threat Modeling [STRIDE] or Architecture Risk Analysis [ARA]), building an assessment and remediation plan for the organization, and using a risk methodology to rank applications.

#### [AA1.1] PERFORM SECURITY FEATURE REVIEW.

`[AA1.1 | level 1 | 89/111 | 80.18%]` — Part 8, Architecture Analysis (AA), p.70 (right column)

Security-aware reviewers identify application security features, review these features against application security requirements and runtime parameters, and determine if each feature can adequately perform its intended function—usually collectively referred to as threat modeling. The goal is to quickly identify missing security features and requirements, or bad deployment configuration (authentication, access control, use of cryptography, etc.), and address them. For example, threat modeling would identify both a system that was subject to escalation of privilege attacks because of broken access control as well as a mobile application that incorrectly puts PII in local storage. Use of the firm’s secure-by-design components often streamlines this process (see [SFD2.1]). Many modern applications are no longer simply “3-tier” but instead involve components architected to interact across a variety of tiers—browser/endpoint, embedded, web, microservices, orchestration engines, deployment pipelines, third-party SaaS, etc. Some of these environments might provide robust security feature sets, whereas others might have key capability gaps that require careful analysis, so organizations should consider the applicability and correct use of security features across all tiers that constitute the architecture and operational environment.

#### [AA1.2] PERFORM DESIGN REVIEW FOR HIGH-RISK APPLICATIONS.

`[AA1.2 | level 1 | 51/111 | 45.95%]` — Part 8, Architecture Analysis (AA), p.71 (left column)

Perform a design review to determine whether the security features and deployment configurations are resistant to attack in an attempt to break the design. The goal is to extend the more formulaic approach of a security feature review (see [AA1.1]) to model application behavior in the context of real-world attackers and attacks. Reviewers must have some experience beyond simple threat modeling to include performing detailed design reviews and breaking the design under consideration. Rather than security feature guidance, a design review should produce a set of flaws and a plan to mitigate them. An organization can use consultants to do this work, but it should participate actively. A review focused only on whether a software project has performed the right process steps won’t generate useful results about flaws. Note that a sufficiently robust design review process can’t be executed at CI/CD speed, so organizations should focus on a few high-risk applications to start (see [AA1.4]).

#### [AA1.4] USE A RISK METHODOLOGY TO RANK APPLICATIONS.

`[AA1.4 | level 1 | 57/111 | 51.35%]` — Part 8, Architecture Analysis (AA), p.71 (left column)

Use a defined risk methodology to collect information about each application in order to assign a risk classification and associated prioritization. It is important to use this information in prioritizing what applications or projects are in scope for testing, including security feature and design reviews. Information collection can be implemented via questionnaire or similar method, whether manual or automated. Information needed for classification might include, “Which programming languages is the application written in?” or “Who uses the application?” or “Is the application’s deployment software orchestrated?” Typically, a qualified member of the application team provides the information, but the process should be short enough to take only a few minutes. The SSG can then use the answers to categorize the application as, e.g., high, medium, or low risk. Because a risk questionnaire can be easy to game, it’s important to put into place some spot-checking for validity and accuracy—an overreliance on self-reporting can render this activity useless.

#### [AA2.1] PERFORM ARCHITECTURE ANALYSIS USING A DEFINED PROCESS.

`[AA2.1 | level 2 | 35/111 | 31.53%]` — Part 8, Architecture Analysis (AA), p.71 (left column)

Define and use a process for AA that extends the design review (see [AA1.2]) to also document business risk in addition to technical flaws. The goal is to identify application design flaws as well as the associated risk (e.g., impact of exploitation), such as through frequency or probability analysis, to more completely inform stakeholder risk management efforts. The AA process includes a standardized approach for thinking about attacks, vulnerabilities, and various security properties. The process is defined well enough that people outside the SSG can carry it out. It’s important to document both the architecture under review and any security flaws uncovered, as well as risk information that people can understand and use. Microsoft Threat Modeling, Versprite PASTA, and Black Duck ARA are examples of such a process, although these will likely need to be tailored to a given environment. In some cases, performing AA and documenting business risk is done by different teams working together in a single process. Uncalibrated or ad hoc AA approaches don’t count as a defined process.

#### [AA2.2] STANDARDIZE ARCHITECTURAL DESCRIPTIONS.

`[AA2.2 | level 2 | 38/111 | 34.23%]` — Part 8, Architecture Analysis (AA), p.71 (right column)

Threat modeling, design review, or AA processes use an agreed upon format (e.g., diagramming language and icons, not simply a text description) to describe architecture, including a means for representing data flow. Standardizing architecture descriptions between those who generate the models and those who analyze and annotate them makes analysis more tractable and scalable. High-level network diagrams, data flow, and authorization flows are always useful, but the model should also go into detail about how the software itself is structured. A standard architecture description can be enhanced to provide an explicit picture of information assets that require protection, including useful metadata. Standardized icons that are consistently used in diagrams, templates, and dry-erase board squiggles are especially useful, too.

#### [AA2.4] HAVE SSG LEAD DESIGN REVIEW EFFORTS.

`[AA2.4 | level 2 | 36/111 | 32.43%]` — Part 8, Architecture Analysis (AA), p.71 (right column)

The SSG takes a lead role in performing design review (see [AA1.2]) to uncover flaws. Breaking down an architecture is enough of an art that the SSG, or other reviewers outside the application team, must be proficient, and proficiency requires practice. This practice might then enable, e.g., champions to take the day-to-day lead while the SSG maintains leadership around knowledge and process. The SSG can’t be successful on its own either—it will likely need help from architects or implementers to understand the design. With a clear design in hand, the SSG might be able to carry out a detailed review with a minimum of interaction with the project team. Approaches to design review evolve over time, so don’t expect to set a process and use it forever. Outsourcing design review might be necessary, but it’s also an opportunity to participate and learn.

#### [AA3.1] HAVE ENGINEERING TEAMS LEAD AA PROCESS.

`[AA3.1 | level 3 | 17/111 | 15.32%]` — Part 8, Architecture Analysis (AA), p.71 (right column)

Engineering teams lead AA to uncover technical flaws and document business risk. This effort requires a well-understood and well-documented process (see [AA2.1]). But even with a good process, consistency is difficult to attain because breaking architecture requires experience, so provide architects with SSG or outside expertise in an advisory capacity. Engineering teams performing AA might normally have responsibilities such as development, DevOps, cloud security, operations security, security architecture, or a variety of similar roles. The process is more useful if the AA team is different from the design team.

#### [AA3.2] DRIVE ANALYSIS RESULTS INTO STANDARD DESIGN PATTERNS.

`[AA3.2 | level 3 | 7/111 | 6.31%]` — Part 8, Architecture Analysis (AA), p.71 (right column)

Failures identified during threat modeling, design review, or AA are fed back to security and engineering teams so that similar mistakes can be prevented in the future through improved design patterns, whether local to a team or formally approved for everyone (see [SFD3.1]). This typically requires a root-cause analysis process that determines the origin of security flaws, searches for what should have prevented the flaw, and makes the necessary improvements in documented security design patterns. Note that security design patterns can interact in surprising ways that break security, so apply analysis processes even when vetted design patterns are in standard use. For cloud services, providers have learned a lot about how their platforms and services fail to resist attack and have codified this experience into patterns for secure use. Organizations that heavily rely on these services might base their application layer patterns on those building blocks provided by the cloud service provider (for example, AWS CloudFormation and Azure Blueprints) when making their own.

#### [AA3.3] MAKE THE SSG AVAILABLE AS AN AA RESOURCE OR MENTOR.

`[AA3.3 | level 3 | 14/111 | 12.61%]` — Part 8, Architecture Analysis (AA), p.72 (left column)

To build organizational AA capability, the SSG advertises experts as resources or mentors for teams using the AA process (see [AA2.1]). This effort might enable, e.g., security champions, site reliability engineers, DevSecOps engineers, and others to take the lead while the SSG offers advice. As one example, mentors help tailor AA process inputs (such as design or attack patterns) to make them more actionable for specific technology stacks. This reusable guidance helps protect the team’s time so they can focus on the problems that require creative solutions rather than enumerating known bad habits. While the SSG might answer AA questions during office hours (see [T2.12]), they will often assign a mentor to work with a team, perhaps comprising both security-aware engineers and risk analysts, for the duration of the analysis. In the case of high-risk software, the SSG should play a more active mentorship role in applying the AA process.

### Practice CR: Code Review (`bsimm-16#CR`)

(Part 8, SDLC TOUCHPOINTS: CODE REVIEW (CR) (p.72)) The Code Review practice includes use of code review tools (e.g., static analysis), development of tailored rules, customized profiles for tool use by different roles (e.g., developers vs. auditors), manual analysis, and tracking and measuring results.

#### [CR1.2] PERFORM OPPORTUNISTIC CODE REVIEW.

`[CR1.2 | level 1 | 75/111 | 67.57%]` — Part 8, Code Review (CR), p.72 (left column)

Perform code review for high-risk applications in an opportunistic fashion. For example, organizations can follow up a design review with a code review looking for security issues in source code and dependencies and perhaps also in deployment artifact configuration (e.g., containers) and automation metadata (e.g., infrastructure-as-code). This informal targeting often evolves into a systematic approach (see [CR1.4]). Manual code review could be augmented with the use of specific tools and services, but it has to be part of a proactive process. When new technologies pop up, new approaches to code review might become necessary.

#### [CR1.4] USE AUTOMATED CODE REVIEW TOOLS.

`[CR1.4 | level 1 | 95/111 | 85.59%]` — Part 8, Code Review (CR), p.72 (left column)

Incorporate static analysis into the code review process to make the review more efficient and consistent. Automation won’t replace human judgment, but it does bring definition to the review process and security expertise to reviewers who typically aren’t security experts. Note that a specific tool might not cover an entire portfolio, especially when new languages are involved, so additional local effort might be useful. Some organizations might progress to automating tool use by instrumenting static analysis into source code management workflows (e.g., pull requests) and delivery pipeline workflows (build, package, and deploy) to make the review more efficient, consistent, and aligned with release cadence. Whether use of automated tools is to review a portion of the source code incrementally, such as a developer committing new code or small changes, or to conduct full analysis by scanning the entire codebase, this service should be explicitly connected to a larger SSDL defect management process applied during software development. This effort is not useful when done just to “check the security box” on the path to deployment.

#### [CR1.5] MAKE CODE REVIEW MANDATORY FOR ALL PROJECTS.

`[CR1.5 | level 1 | 74/111 | 66.67%]` — Part 8, Code Review (CR), p.72 (right column)

A security-focused code review is mandatory for all software projects, with a lack of code review or unacceptable results stopping a release, slowing it down, or causing it to be recalled. While all projects must undergo code review, the process might be different for different kinds of projects. The review for low-risk projects might rely more heavily on automation (see [CR1.4]), for example, whereas high-risk projects might have no upper bound on the amount of time spent by reviewers. Having a minimum acceptable standard forces projects that don’t pass to be fixed and reevaluated. A code review tool with nearly all the rules turned off (so it can run at CI/CD automation speeds, for example) won’t provide sufficient defect coverage. Similarly, peer code review or tools focused on quality and style won’t provide useful security results.

#### [CR1.7] ASSIGN CODE REVIEW TOOL MENTORS.

`[CR1.7 | level 1 | 47/111 | 42.34%]` — Part 8, Code Review (CR), p.72 (right column)

Mentors show developers how to get the most out of code review tools, including configuration, triage, and remediation. Security champions, DevOps and site reliability engineers, and SSG members often make good mentors. Mentors could use office hours or other outreach to help developers establish the right configuration and get started on interpreting and remediating results. Alternatively, mentors might work with a development team for the duration of the first review they perform. Centralized use of a tool can be distributed into the development organization or toolchains over time through the use of tool mentors, but providing installation instructions and URLs to centralized tool downloads isn’t the same as mentoring. Increasingly, mentorship extends to code review tools associated with deployment artifacts (e.g., container security) and infrastructure (e.g., cloud configuration). While AI is becoming useful to augment human code review guidance, it likely doesn’t have the context necessary to replace it.

#### [CR2.6] USE CUSTOM RULES WITH AUTOMATED CODE REVIEW TOOLS.

`[CR2.6 | level 2 | 29/111 | 26.13%]` — Part 8, Code Review (CR), p.72 (right column)

Create and use custom rules in code review tools to help uncover security defects specific to the organization’s coding standards or to the framework-based or cloud-provided middleware the organization uses. The same group that provides tool mentoring (see [CR1.7]) will likely spearhead this customization. Custom rules are often explicitly tied to proper usage of technology stacks in a positive sense and avoidance of errors commonly encountered in a firm’s codebase in a negative sense. Custom rules are also an easy way to check for adherence to coding standards (see [CR3.5]). To reduce the workload for everyone, many organizations also create rules to remove repeated false positives and to turn off checks that aren’t relevant.

#### [CR2.7] USE A TOP N BUGS LIST (REAL DATA PREFERRED).

`[CR2.7 | level 2 | 19/111 | 17.12%]` — Part 8, Code Review (CR), p.73 (left column)

Maintain a living list of the most important kinds of bugs the organization wants to eliminate from its code and use it to drive change. Many organizations start with a generic list pulled from public sources, but broad-based lists such as the OWASP Top 10 rarely reflect an organization’s bug priorities. Build a valuable list by using real data gathered from code review (see [CR2.8]), testing (see [PT1.2]), software composition analysis (see [SE3.8]), and actual incidents (see [CMVM1.1]), then prioritize it for prevention efforts. Simply sorting the day’s bug data by number of occurrences won’t produce a satisfactory list because the data changes so often. To increase interest, the SSG can periodically publish a “most wanted” report after updating the list. One potential pitfall with a top N list is that it tends to include only known problems. Of course, just building the list won’t accomplish anything—everyone has to use it to find and fix bugs.

#### [CR2.8] USE CENTRALIZED DEFECT REPORTING TO CLOSE THE KNOWLEDGE LOOP.

`[CR2.8 | level 2 | 28/111 | 25.23%]` — Part 8, Code Review (CR), p.73 (left column)

The defects found during code review are tracked in a centralized repository that makes it possible to do both summary and trend reporting for the organization. Reported defects drive engineering improvements such as enhancing processes, updating standards, adopting reusable frameworks, etc. For example, code review information is usually incorporated into a CISO-level dashboard that can include feeds from other security testing efforts (e.g., penetration testing, composition analysis, threat modeling). Given the historical code review data, the SSG can also use the reports to demonstrate progress (see [SM3.3]) or drive the training curriculum. Individual bugs make excellent training examples (see [T2.8]). Some organizations have moved toward analyzing this data and using the results to drive automation (see [ST3.6]).

#### [CR3.2] BUILD A CAPABILITY TO COMBINE AST RESULTS.

`[CR3.2 | level 3 | 18/111 | 16.22%]` — Part 8, Code Review (CR), p.73 (left column)

Combine application security testing (AST) results so that multiple testing techniques feed into one reporting and remediation process. In addition to code review, testing techniques often include dynamic analysis, software composition analysis, container scanning, cloud services configuration review, etc. The SSG might write scripts or acquire software to gather data automatically and combine the results into a format that can be consumed by a single downstream review and reporting solution. The tricky part of this activity is normalizing vulnerability information from disparate sources that might use conflicting terminology or scoring. In some cases, using a standardized taxonomy (e.g., a CWE-like approach) can help with normalization. Combining multiple sources helps drive better-informed risk mitigation decisions and identify engineering improvements.

#### [CR3.3] CREATE CAPABILITY TO ERADICATE BUGS.

`[CR3.3 | level 3 | 8/111 | 7.21%]` — Part 8, Code Review (CR), p.73 (left column)

When a security bug is found during code review (see [CR1.2], [CR1.4]), the organization searches for and then fixes all occurrences of the bug, not just the instance originally discovered. Searching with custom rules (see [CR2.6]) makes it possible to eradicate the specific bug entirely without waiting for every project to reach the code review portion of its lifecycle. This doesn’t mean finding every instance of every kind of cross-site scripting bug when a specific example is found—it means going after that specific example everywhere. A firm with only a handful of software applications built on a single technology stack will have an easier time with this activity than firms with many large applications built on a diverse set of technology stacks. A new development framework or library, rules in RASP or a next-generation firewall, or cloud configuration tools that provide guardrails can often help in (but not replace) eradication efforts.

#### [CR3.4] AUTOMATE MALICIOUS CODE DETECTION.

`[CR3.4 | level 3 | 3/111 | 2.70%]` — Part 8, Code Review (CR), p.73 (right column)

Use automated code review to identify malicious code written by in-house developers or outsource providers. Examples of malicious code include backdoors, logic bombs, time bombs, nefarious communication channels, obfuscated program logic, and dynamic code injection. Although out-of-the-box automation might identify some generic malicious-looking constructs, custom rules for the static analysis tools used to codify acceptable and unacceptable patterns in the organization’s codebase will likely become a necessity. Manual review for malicious code is a good start but insufficient to complete this activity at scale. While not all backdoors or similar code were meant to be malicious when they were written (e.g., a developer’s feature to bypass authentication during testing), such things tend to stay in deployed code and should be treated as malicious until proven otherwise. Discovering some types of malicious code will require dynamic testing techniques.

#### [CR3.5] ENFORCE SECURE CODING STANDARDS.

`[CR3.5 | level 3 | 4/111 | 3.60%]` — Part 8, Code Review (CR), p.73 (right column)

A violation of secure coding standards is sufficient grounds for rejecting a piece of code. This rejection can take one or more forms, such as denying a pull request, breaking a build, failing quality assurance, removing from production, or moving the code into a different development workstream where repairs or exceptions can be worked out. The enforced portions of an organization’s secure coding standards (see [SR3.3]) often start out as a simple list of banned functions or required frameworks. Code review against standards must be objective—it shouldn’t become a debate about whether the noncompliant code is exploitable. In some cases, coding standards are specific to language constructs and enforced with tools (e.g., codified into SAST rules). In other cases, published coding standards are specific to technology stacks and enforced during the code review process or by using automation. Standards can be positive (“do it this way”) or negative (“do not use this API”), but they must be enforced.

### Practice ST: Security Testing (`bsimm-16#ST`)

(Part 8, SDLC TOUCHPOINTS: SECURITY TESTING (ST) (p.73)) The Security Testing practice is concerned with prerelease defect discovery as well as integrating security into standard QA processes. The practice includes the use of opaque-box AST tools (including fuzz testing) as a smoke test in QA, risk-driven crystal-box test suites, application of the attack model, and code coverage analysis. Security testing focuses on vulnerabilities in construction.

#### [ST1.1] PERFORM EDGE/ BOUNDARY VALUE CONDITION TESTING DURING QA.

`[ST1.1 | level 1 | 93/111 | 83.78%]` — Part 8, Security Testing (ST), p.74 (left column)

QA efforts go beyond functional testing to perform basic adversarial tests and probe simple edge cases and boundary conditions, with no particular attacker skills required. When QA pushes past standard functional testing that uses expected input, it begins to move toward thinking like an adversary. Boundary value testing, whether automated or manual, can lead naturally to the notion of an attacker probing the edges on purpose (e.g., determining what happens when someone enters the wrong password over and over).

#### [ST1.3] DRIVE TESTS WITH SECURITY REQUIREMENTS AND SECURITY FEATURES.

`[ST1.3 | level 1 | 66/111 | 59.46%]` — Part 8, Security Testing (ST), p.74 (left column)

QA targets declarative security mechanisms with tests derived from security requirements and features. A test could try to access administrative functionality as an unprivileged user, for example, or verify that a user account becomes locked after some number of failed authentication attempts. For the most part, security features can be tested in a fashion similar to other software features—security mechanisms such as account lockout, transaction limitations, entitlements, etc., are tested with both expected and unexpected input as derived from security requirements. Software security isn’t security software, but testing security features is an easy way to get started. New software architectures and deployment automation, such as with container and cloud infrastructure orchestration, might require novel test approaches.

#### [ST1.4] INTEGRATE OPAQUE-BOX SECURITY TOOLS INTO THE QA PROCESS.

`[ST1.4 | level 1 | 47/111 | 42.34%]` — Part 8, Security Testing (ST), p.74 (left column)

The organization uses one or more opaque-box security testing tools as part of the QA process. Such tools are valuable because they encapsulate an attacker’s perspective, albeit generically. Traditional dynamic analysis scanners are relevant for web applications, while similar tools exist for cloud environments, containers, mobile applications, embedded systems, APIs, etc. In some situations, other groups might collaborate with the SSG to apply the tools, e.g., a testing team could run the tool but come to the SSG for help with interpreting the results. When testing is integrated into Agile development approaches, opaque-box tools might be hooked into internal toolchains, provided by cloud-based toolchains, or used directly by engineering. Regardless of who runs the opaque-box tool, the testing should be properly integrated into a QA cycle of the SSDL and will often include both authenticated and unauthenticated reviews.

#### [ST2.4] DRIVE QA TESTS WITH AST RESULTS.

`[ST2.4 | level 2 | 20/111 | 18.02%]` — Part 8, Security Testing (ST), p.74 (left column)

Share results from application security testing, such as penetration testing, threat modeling, composition analysis, code reviews, etc., with QA teams to evangelize the security mindset. Using security defects as the basis for a conversation about common attack patterns or the underlying causes for them allows QA teams to generalize this information into new test approaches. Organizations that leverage software pipeline platforms such as GitHub, or CI/CD platforms such as the Atlassian stack, can benefit from teams receiving various testing results automatically, which should then facilitate timely stakeholder conversations—emailing security reports to QA teams will not generate the desired results. Over time, QA teams learn the security mindset, and the organization benefits from an improved ability to create security tests tailored to the organization’s code.

#### [ST2.5] INCLUDE SECURITY TESTS IN QA AUTOMATION.

`[ST2.5 | level 2 | 30/111 | 27.03%]` — Part 8, Security Testing (ST), p.74 (right column)

Security tests are included in an automation framework and run alongside functional, performance, and other QA test suites. Executing this automation framework can be triggered manually or through additional automation (e.g., as part of pipeline tooling). When test creators who understand the software create security tests, they can uncover more specialized or more relevant defects than commercial tools might (see [ST1.4]). Security tests might be derived from typical failures of security features (see [SFD1.1]), from creative tweaks of functional and developer tests, or even from guidance provided by penetration testers on how to reproduce an issue. Tests that are performed manually or out-of-band likely will not provide timely feedback.

#### [ST2.6] PERFORM FUZZ TESTING CUSTOMIZED TO APPLICATION APIS.

`[ST2.6 | level 2 | 28/111 | 25.23%]` — Part 8, Security Testing (ST), p.74 (right column)

QA efforts include running a customized fuzzing framework against APIs critical to the organization. An API might be software that allows two applications to communicate or even software that allows a human to interact with an application (e.g., a webform). Testers could begin from scratch or use an existing fuzzing toolkit, but the necessary customization often goes beyond creating custom protocol descriptions or file format templates to giving the fuzzing framework a built-in understanding of application interfaces and business logic. Test harnesses developed explicitly for specific applications make good places to integrate fuzz testing.

#### [ST3.3] DRIVE TESTS WITH DESIGN REVIEW RESULTS.

`[ST3.3 | level 3 | 15/111 | 13.51%]` — Part 8, Security Testing (ST), p.74 (right column)

Use design review or architecture analysis results to direct QA test creation. For example, if the results of attempting to break a design determine that “the security of the system hinges on the transactions being atomic and not being interrupted partway through,” then torn transactions will become a primary target in adversarial testing. Adversarial tests like these can be developed according to a risk profile, with high-risk flaws at the top of the list. Security defect data shared with QA (see [ST2.4]) can help focus test creation on areas of potential vulnerability that can, in turn, help prove the existence of identified high-risk flaws.

#### [ST3.4] LEVERAGE CODE COVERAGE ANALYSIS.

`[ST3.4 | level 3 | 6/111 | 5.41%]` — Part 8, Security Testing (ST), p.74 (right column)

Testers measure the code coverage of their application security testing to identify code that isn’t being exercised and then adjust test cases to incrementally improve coverage. AST can include automated testing (see [ST2.5], [ST2.6]) and manual testing (see [ST1.1], [ST1.3]). In turn, code coverage analysis drives increased security testing depth. Coverage analysis is easier when using standard measurements, such as function coverage, line coverage, or multiple condition coverage. The point is to measure how broadly the test cases cover the security requirements, which is not the same as measuring how broadly the test cases exercise the code.

#### [ST3.5] BEGIN TO BUILD AND APPLY ADVERSARIAL SECURITY TESTS (ABUSE CASES).

`[ST3.5 | level 3 | 9/111 | 8.11%]` — Part 8, Security Testing (ST), p.75 (left column)

QA teams incorporate test cases based on abuse cases (see [AM2.1]) as testers move beyond verifying functionality and take on the attacker’s perspective. One way to do this is to systematically attempt to replicate incidents from the organization’s history. Abuse and misuse cases based on the attacker’s perspective can also be derived from security policies, attack intelligence, standards, and the organization’s top N attacks list (see [AM3.5]). This effort turns the corner in QA from testing features to attempting to break the software under test.

#### [ST3.6] IMPLEMENT EVENT-DRIVEN SECURITY TESTING IN AUTOMATION.

`[ST3.6 | level 3 | 10/111 | 9.01%]` — Part 8, Security Testing (ST), p.75 (left column)

The SSG guides implementation of automation for continuous, event-driven application security testing. An event here is simply a noteworthy occurrence, such as dropping new code in a repository, a pull request, a build request, or a push to deployment. Event-driven testing implemented in pipeline automation (rather than testing only in production) typically moves the testing closer to the conditions driving the testing requirement (whether shift left toward design or shift right toward operations), repeats the testing as often as the event is triggered, and helps ensure that the right testing is executed for a given set of conditions. Success with this approach depends on the broad use of sensors (e.g., agents, bots) that monitor engineering processes, execute contextual rules, and provide telemetry to automation that initiates the specified testing whenever event conditions are met. More mature configurations typically include risk-driven conditions (e.g., size of change, provenance, function, team).

## Domain: Deployment (`bsimm-16#DEPLOYMENT`)

(Part 7, Table 7 THE SOFTWARE SECURITY FRAMEWORK (p.45)) Practices that interface with traditional network security and software maintenance organizations. Software configuration, maintenance, and other environment issues have direct impact on software security.

### Practice PT: Penetration Testing (`bsimm-16#PT`)

(Part 8, DEPLOYMENT: PENETRATION TESTING (PT) (p.75)) The Penetration Testing practice involves standard outside-in testing of the sort carried out by security specialists. Penetration testing focuses on vulnerabilities in preproduction and production code, providing direct feeds to defect management and mitigation.

#### [PT1.1] USE EXTERNAL PENETRATION TESTERS TO FIND PROBLEMS.

`[PT1.1 | level 1 | 95/111 | 85.59%]` — Part 8, Penetration Testing (PT), p.75 (left column)

External penetration testers are used to demonstrate that the organization’s software needs help. Finding critical vulnerabilities in high-profile applications provides the evidence that executives often require. Over time, the focus of penetration testing moves from trying to determine if the code is broken in some areas to a sanity check done before shipping or on a periodic basis. In addition to breaking code, this sanity check can also be an effective way to ensure that vulnerability prevention techniques are both used and effective. External penetration testers who bring a new set of experiences and skills to the problem are the most useful.

#### [PT1.2] FEED RESULTS TO THE DEFECT MANAGEMENT AND MITIGATION SYSTEM.

`[PT1.2 | level 1 | 87/111 | 78.38%]` — Part 8, Penetration Testing (PT), p.75 (left column)

All penetration testing results are fed back to engineering through established defect management or mitigation channels, with development and operations responding via a defect management and release process. In addition to application vulnerabilities, also track results from testing other software such as containers and infrastructure configuration. Properly done, this exercise demonstrates the organization’s ability to improve the state of security and emphasizes the importance of not just identifying but actually fixing security problems. One way to ensure attention is to add a security flag to the bug-tracking and defect management system. The organization might leverage developer workflow or social tooling (e.g., JIRA or Slack) to communicate change requests, but these requests are still tracked explicitly as part of a vulnerability management process.

#### [PT1.3] USE PENETRATION TESTING TOOLS INTERNALLY.

`[PT1.3 | level 1 | 67/111 | 60.36%]` — Part 8, Penetration Testing (PT), p.75 (right column)

The organization creates an internal penetration testing capability that uses tools as part of an established process. Execution can rest with the SSG or be part of a specialized team elsewhere in the organization, with the tools complementing manual efforts to improve the efficiency and repeatability of the testing process. The tools used will usually include off-the-shelf products built specifically for application penetration testing, network penetration tools that specifically understand the application layer, container and cloud configuration testing tools, and custom scripts. Free-time or crisis-driven efforts aren’t the same as an internal capability.

#### [PT2.2] PENETRATION TESTERS USE ALL AVAILABLE INFORMATION.

`[PT2.2 | level 2 | 40/111 | 36.04%]` — Part 8, Penetration Testing (PT), p.75 (right column)

Penetration testers, whether internal or external, routinely make use of artifacts created throughout the SSDL to do more comprehensive analysis and find more problems. Example artifacts include design documents, architecture analysis results, misuse and abuse cases, code review results, cloud environment and other deployment configurations, and source code if applicable. Focusing on high-risk applications is a good way to start. Note that having access to SSDL artifacts is not the same as using them.

#### [PT2.3] SCHEDULE PERIODIC PENETRATION TESTS FOR APPLICATION COVERAGE.

`[PT2.3 | level 2 | 56/111 | 50.45%]` — Part 8, Penetration Testing (PT), p.75 (right column)

All applications are tested periodically, which could be tied to a calendar or a release cycle. High-risk applications could get a penetration test at least once per year, for example, even if there have not been substantive code changes, while other applications might receive different kinds of security testing on a similar schedule. Any security testing performed must focus on discovering vulnerabilities, not just checking a process or compliance box. This testing serves as a sanity check and helps ensure that yesterday’s software isn’t vulnerable to today’s attacks. The testing can also help maintain the security of software configurations and environments, especially for containers and components in the cloud. One important aspect of periodic security testing across the portfolio is to make sure that the problems identified are actually fixed. Software that isn’t an application, such as automation created for CI/CD, infrastructure-as-code, etc., deserves some security testing as well.

#### [PT3.1] USE EXTERNAL PENETRATION TESTERS TO PERFORM DEEP-DIVE ANALYSIS.

`[PT3.1 | level 3 | 25/111 | 22.52%]` — Part 8, Penetration Testing (PT), p.76 (left column)

The SSG uses external penetration testers to do a deep-dive analysis on critical software systems or technologies and to introduce fresh thinking. One way to do this is to simulate persistent attackers using goal-oriented red team exercises. These testers are domain experts and specialists who keep the organization up to speed with the latest version of the attacker’s perspective and have a track record for breaking the type of software being tested. When attacking the organization’s software, these testers also demonstrate a creative approach that provides useful knowledge to the people designing, implementing, and hardening new systems. Creating new types of attacks from threat intelligence and abuse cases typically requires extended timelines, which is essential when it comes to new technologies, and prevents checklist-driven approaches that look only for known types of problems.

#### [PT3.2] CUSTOMIZE PENETRATION TESTING TOOLS.

`[PT3.2 | level 3 | 25/111 | 22.52%]` — Part 8, Penetration Testing (PT), p.76 (left column)

Build a capability to create penetration testing tools, or to adapt publicly available ones, to attack the organization’s software more efficiently and comprehensively. Creating penetration testing tools requires a deep understanding of attacks (see [AM2.1], [AM2.8]) and technology stacks (see [AM3.4]). Customizing existing tools goes beyond configuration changes and extends tool functionality to find new issues. Tools will improve the efficiency of the penetration testing process without sacrificing the depth of problems that the SSG can identify. Automation can be particularly valuable in organizations using Agile methodologies because it helps teams go faster. Tools that can be tailored are always preferable to generic tools. Success here is often dependent on both the depth and scope of tests enabled through customized tools.

### Practice SE: Software Environment (`bsimm-16#SE`)

(Part 8, DEPLOYMENT: SOFTWARE ENVIRONMENT (SE) (p.76)) The Software Environment practice deals with OS and platform patching (including in the cloud), WAFs (web application firewalls), installation and configuration documentation, containerization, orchestration, application monitoring, change management, and code signing.

#### [SE1.1] USE APPLICATION INPUT MONITORING FOR SECURITY PURPOSES.

`[SE1.1 | level 1 | 73/111 | 65.77%]` — Part 8, Software Environment (SE), p.76 (left column)

The organization monitors input to the software that it runs in order to spot attacks. Monitoring systems that write log files are useful only if humans or bots periodically review the logs and take action. For web applications, RASP or a WAF can do this monitoring, while other kinds of software likely require other approaches, such as custom runtime instrumentation. Software and technology stacks, such as mobile and IoT, likely require their own input monitoring solutions. Serverless and containerized software can require interaction with vendor software to get the appropriate logs and monitoring data. Cloud deployments and platform-as-a-service usage can add another level of difficulty to the monitoring, collection, and aggregation approach.

#### [SE1.2] ENSURE HOST AND NETWORK SECURITY BASICS ARE IN PLACE.

`[SE1.2 | level 1 | 96/111 | 86.49%]` — Part 8, Software Environment (SE), p.76 (right column)

The organization provides a solid foundation for its software in operation by ensuring that host (whether bare metal or virtual machine) and network security basics are in place across its data centers and networks and that these basics remain in place during new releases. Host and network security basics must account for evolving network perimeters, increased connectivity and data sharing, software-defined networking, and increasing dependence on vendors (e.g., content delivery, load balancing, and content inspection services). In addition to securing your production environment, the organization should consider securing their development endpoints [SE3.10] and tool chains [SE3.9]. Doing software security before getting host and network security in place is like putting on shoes before putting on socks.

#### [SE1.3] IMPLEMENT CLOUD SECURITY CONTROLS.

`[SE1.3 | level 1 | 79/111 | 71.17%]` — Part 8, Software Environment (SE), p.76 (right column)

Organizations ensure that cloud security controls are in place and working for both public and private clouds. Industry best practices are a good starting point for local policy and standards to drive controls and configurations. Of course, cloud-based assets often have public-facing services that create an attack surface (e.g., cloud-based storage) that is different from the one in a private data center, so these assets require customized security configuration and administration. In the increasingly software-defined world, the SSG has to help everyone explicitly configure cloud-specific security features and controls (e.g., through cloud provider administration consoles) comparable to those built with cables and physical hardware in private data centers. Detailed knowledge about cloud provider shared responsibility security models is always necessary to ensure that the right cloud security controls remain in place.

#### [SE1.4] DEFINE SECURE DEPLOYMENT PARAMETERS AND CONFIGURATIONS.

`[SE1.4 | level 1 | 69/111 | 62.16% — heading prints 62.1% (source inconsistency)]` — Part 8, Software Environment (SE), p.76 (right column)

Create deployment automation or installation guides (e.g., standard operating procedures) to help teams and customers install and configure software securely. Software here includes applications, products, scripts, images, firmware, and other forms of code. Deployment automation usually includes a clearly described configuration for software artifacts and the infrastructure-as-code (e.g., Terraform, CloudFormation, ARM templates, Helm Charts) necessary to deploy them, including details on COTS, open source, vendor, and cloud services components. All deployment automation should be understandable by humans, not just by machines, especially when distributed to customers. Where deployment automation is not applicable, customers or deployment teams need installation guides that include hardening guidance and secure configurations.

#### [SE2.4] PROTECT CODE INTEGRITY.

`[SE2.4 | level 2 | 52/111 | 46.85%]` — Part 8, Software Environment (SE), p.76 (right column)

Use code protection mechanisms (e.g., code signing) that allow the organization to attest to the provenance, integrity, and authorization of important code. While legacy and mobile platforms accomplished this with point-in-time code signing and permissions activity, protecting modern containerized software demands actions in various lifecycle phases. Organizations can use build systems to verify sources and manifests of dependencies, creating their own cryptographic attestation of both. Packaging and deployment systems can sign and verify binary packages, including code, configuration, metadata, code identity, and authorization to release material. In some cases, organizations allow only code from their own registries to execute in certain environments. Protecting code integrity can also include securing development infrastructure, using permissions and peer review to govern code contributions, and limiting code access to help protect integrity (see [SE3.9]).

#### [SE2.5] USE APPLICATION CONTAINERS TO SUPPORT SECURITY GOALS.

`[SE2.5 | level 2 | 59/111 | 53.15%]` — Part 8, Software Environment (SE), p.77 (left column)

The organization uses application containers to support its software security goals. Simply deploying containers isn’t sufficient to gain security benefits, but their planned use can support a tighter coupling of applications with their dependencies, immutability, integrity (see [SE2.4]), and some isolation benefits without the overhead of deploying a full operating system on a virtual machine. Containers are a convenient place for security controls to be applied and updated consistently (see [SFD3.2]), and while they are useful in development and test environments, their use in production provides the needed security benefits.

#### [SE2.7] USE ORCHESTRATION FOR CONTAINERS AND VIRTUALIZED ENVIRONMENTS.

`[SE2.7 | level 2 | 40/111 | 36.04%]` — Part 8, Software Environment (SE), p.77 (left column)

The organization uses automation to scale service, container, and virtualized environments in a disciplined way. Orchestration processes take advantage of built-in and add-on security features (see [SFD2.1]), such as hardening against drift, secrets management, RBAC, and rollbacks, to ensure that each deployed workload meets predetermined security requirements. Setting security behaviors in aggregate allows for rapid change when the need arises. Orchestration platforms are themselves software that becomes part of your production environment, which in turn requires hardening and security patching and configuration—in other words, if you use Kubernetes, make sure you patch Kubernetes.

#### [SE3.2] USE CODE PROTECTION.

`[SE3.2 | level 3 | 25/111 | 22.52%]` — Part 8, Software Environment (SE), p.77 (left column)

To protect intellectual property and make exploit development harder, the organization erects barriers to reverse engineering its software (e.g., anti-tamper, debug protection, anti-piracy features, runtime integrity). For some software, obfuscation techniques could be applied as part of the production build and release process. In other cases, these protections could be applied at the software-defined network or software orchestration layer when applications are being dynamically regenerated post-deployment. Code protection is particularly important for widely distributed code, such as mobile applications and JavaScript distributed to browsers. On some platforms, employing Data Execution Prevention (DEP), Safe Structured Exception Handling (SafeSEH), and Address Space Layout Randomization (ASLR) can be a good start at making exploit development more difficult, but be aware that yesterday’s protection mechanisms might not hold up to today’s attacks.

#### [SE3.3] USE APPLICATION BEHAVIOR MONITORING AND DIAGNOSTICS.

`[SE3.3 | level 3 | 22/111 | 19.82%]` — Part 8, Software Environment (SE), p.77 (right column)

The organization monitors production software to look for misbehavior or signs of attack. Go beyond host and network monitoring to look for software-specific problems, such as indications of malicious behavior, fraud, and related issues. Application-level intrusion detection and anomaly detection systems might focus on an application’s interaction with the operating system (through system calls) or with the kinds of data that an application consumes, originates, and manipulates. Signs that an application isn’t behaving as expected will be specific to the software business logic and its environment, so one-size-fits-all solutions probably won’t generate satisfactory results. In some types of environments (e.g., platform-as a-service), some of this data and the associated predictive analytics might come from a vendor.

#### [SE3.6] CREATE BILLS OF MATERIALS FOR DEPLOYED SOFTWARE.

`[SE3.6 | level 3 | 31/111 | 27.93%]` — Part 8, Software Environment (SE), p.77 (right column)

Create a BOM detailing the components, dependencies, and other metadata for important production software. Use this BOM to help the organization tighten its security posture, i.e., to react with agility as attackers and attacks evolve, compliance requirements change, and the number of items to patch grows quite large. Knowing where all the components live in running software—and whether they’re in private data centers, in clouds, or sold as box products (see [CMVM2.3])—allows for timely response when unfortunate events occur.

#### [SE3.8] PERFORM APPLICATION COMPOSITION ANALYSIS ON CODE REPOSITORIES.

`[SE3.8 | level 3 | 8/111 | 7.21%]` — Part 8, Software Environment (SE), p.77 (right column)

Use composition analysis results to augment software asset inventory information with data on all components comprising important applications. Beyond open source (see [SR1.5]), inventory information (see [SM3.1]) includes component and dependency information for internally developed (first-party), commissioned code (second-party), and external (third-party) software, whether that software exists as source code or binary. One common way of documenting this information is to build SBOMs. Doing this manually is probably not an option—keeping up with software changes likely requires toolchain integration rather than carrying this out as a point-in-time activity. This information is extremely useful in supply chain security efforts (see [SM3.5]).

#### [SE3.9] PROTECT INTEGRITY OF DEVELOPMENT TOOLCHAINS.

`[SE3.9 | level 3 | 13/111 | 11.71%]` — Part 8, Software Environment (SE), p.77 (right column)

The organization ensures the integrity of software it builds and integrates by maintaining and securing all development infrastructure and preventing unauthorized changes to source code and other software lifecycle artifacts. Development infrastructure includes code and artifact repositories, build pipelines, and deployment automation. Secure the development infrastructure by safely handling and storing secrets, following pipeline configuration requirements, patching tools and build environments, limiting access to pipeline settings, and auditing changes to configurations. Preventing unauthorized changes typically includes enforcing least privilege access to code repositories and requiring approval for code commits. Automatically granting access for all project team members isn’t sufficient to adequately protect software integrity.

#### [SE3.10] PROTECT THE INTEGRITY OF DEVELOPMENT ENDPOINTS.

`[SE3.10 | level 3 | 6/111 | 5.41%]` — Part 8, Software Environment (SE), p.78 (left column)

The organization maintains the integrity of the software it builds by applying security basics to the workstations used by development stakeholders who interact with the development toolchain. Development endpoints are the workstations used for writing source code, configuring the development toolchain, testing the software’s functionality, or modifying data in the code or artifact repositories. Organizations can protect development endpoints by limiting or monitoring privileged actions, ensuring that the operating system and antivirus definitions are up to date, vetting installed software, or by providing a separate, secured workstation for development that is not used for administrative tasks. Establishing and applying a development endpoint security baseline allows for stakeholders to perform the technical tasks required by software development, but also provides another layer of defense to the development toolchain [SE3.9].

### Practice CMVM: Configuration Management & Vulnerability Management (`bsimm-16#CMVM`)

(Part 8, DEPLOYMENT: CONFIGURATION MANAGEMENT & VULNERABILITY MANAGEMENT (CMVM) (p.78)) The Configuration Management & Vulnerability Management practice concerns itself with operations processes, patching and updating applications, version control, defect tracking and remediation, and incident handling.

#### [CMVM1.1] CREATE OR INTERFACE WITH INCIDENT RESPONSE.

`[CMVM1.1 | level 1 | 106/111 | 95.50%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.78 (left column)

The SSG is prepared to respond to an event or alert and is regularly included in the incident response process, either by creating its own incident response capability or by regularly interfacing with the organization’s existing team. A standing meeting between the SSG and the incident response team keeps information flowing in both directions. Having prebuilt communication channels with critical vendors (e.g., ISP, monitoring, IaaS, SaaS, PaaS) is also very important.

#### [CMVM1.2] IDENTIFY SOFTWARE DEFECTS FOUND IN OPERATIONS MONITORING AND FEED THEM BACK TO ENGINEERING.

`[CMVM1.2 | level 1 | 76/111 | 68.47%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.78 (left column)

Defects identified in production through operations monitoring are fed back to development and used to change engineering behavior. Useful sources of production defects include incidents, bug bounty (see [CMVM3.4]), responsible disclosure (see [CMVM2.4]), SIEMs, production logs, customer feedback, and telemetry from cloud security posture monitoring, container configuration monitoring, RASP, and similar technologies. Entering production defect data into an existing bug-tracking system (perhaps by making use of a special security flag) can close the information loop and make sure that security issues get fixed. In addition, it’s important to capture lessons learned from production defects and use these lessons to change the organization’s behavior. In the best of cases, processes in the SSDL can be improved based on operations data (see [CMVM3.2]).

#### [CMVM1.3] TRACK SOFTWARE DEFECTS FOUND IN OPERATIONS THROUGH THE FIX PROCESS.

`[CMVM1.3 | level 1 | 82/111 | 73.87%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.78 (right column)

Defects found in operations (see [CMVM1.2]) are entered into established defect management systems and tracked through the fix process. This tracking ability could come in the form of a two-way bridge between defect finders and defect fixers or possibly through intermediaries (e.g., the vulnerability management team), but make sure the loop is closed completely. Defects can appear in all types of deployable artifacts, deployment automation, and infrastructure configuration. Setting a security flag in the defect tracking system can help facilitate tracking.

#### [CMVM1.4] HAVE EMERGENCY RESPONSE.

`[CMVM1.4 | level 1 | 86/111 | 77.48%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.78 (right column)

The organization can make quick code and configuration changes when software (e.g., application, API, microservice, infrastructure) is under attack. An emergency response team works in conjunction with stakeholders such as application owners, engineering, operations, and the SSG to study the code and the attack, find a resolution, and fix the production code (e.g., push a patch into production, rollback to a known-good state, deploy a new container). Often, the emergency response team is the engineering team itself. A well-defined process is a must here, a process that has never been used might not actually work.

#### [CMVM2.3] DEVELOP AN OPERATIONS SOFTWARE INVENTORY.

`[CMVM2.3 | level 2 | 38/111 | 34.23%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.78 (right column)

The organization has a map of its software deployments and related containerization, orchestration, and deployment automation code, along with the respective owners. If a software asset needs to be changed or decommissioned, operations or DevOps teams can reliably identify both the stakeholders and all the places where the change needs to occur. Common components can be noted so that when an error occurs in one application, other applications sharing the same components can be fixed as well. Building an accurate representation of an inventory will likely involve enumerating at least the source code, the open source incorporated both during the build and during dynamic production updates, the orchestration software incorporated into production images, and any service discovery or invocation that occurs in production.

#### [CMVM2.4] STREAMLINE INCOMING RESPONSIBLE VULNERABILITY DISCLOSURE.

`[CMVM2.4 | level 2 | 53/111 | 47.75%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.78 (right column)

Provide external bug reporters with a line of communication to internal security experts through a low-friction, public entry point. These experts work with bug reporters to invoke any necessary organizational responses and to coordinate with external entities throughout the defect management lifecycle. Successful disclosure processes require insight from internal stakeholders, such as legal, marketing, and public relations roles, to simplify and expedite decision-making during software security crises (see [CMVM3.3]). Although bug bounties might be important to motivate some researchers (see [CMVM3.4]), proper public attribution and a low-friction reporting process is often sufficient motivation for researchers to participate in a coordinated disclosure. Most organizations will use a combination of easy-to-find landing pages, common email addresses (security@), and embedded product documentation when appropriate (security.txt) as an entry point for external reporters to invoke this process.

#### [CMVM3.1] FIX ALL OCCURRENCES OF SOFTWARE DEFECTS FOUND IN OPERATIONS.

`[CMVM3.1 | level 3 | 16/111 | 14.41%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.79 (left column)

When a security defect is found in operations (see [CMVM1.2]), the organization searches for and fixes all occurrences of the defect in operations, not just the one originally reported. Doing this proactively requires the ability to reexamine the entire operations software inventory (see [CMVM2.3]) when new kinds of defects come to light. One way to approach reexamination is to create a ruleset that generalizes deployed defects into something that can be scanned for via automated code review. In some environments, addressing a defect might involve removing it from production immediately and making the actual fix in some priority order before redeployment. Use of orchestration can greatly simplify deploying the fix for all occurrences of a software defect (see [SE2.7]).

#### [CMVM3.2] ENHANCE THE SSDL TO PREVENT SOFTWARE DEFECTS FOUND IN OPERATIONS.

`[CMVM3.2 | level 3 | 27/111 | 24.32%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.79 (left column)

Experience from operations leads to changes in the SSDL (see [SM1.1]), which can in turn be strengthened to prevent the reintroduction of defects. To make this process systematic, the incident response postmortem includes a feedback-to-SSDL step. The outcomes of the postmortem might result in changes such as to tool-based policy rulesets in a CI/CD pipeline and adjustments to automated deployment configuration (see [SE1.4]). This works best when root-cause analysis pinpoints where in the software lifecycle an error could have been introduced or slipped by uncaught (e.g., a defect escape). DevOps engineers might have an easier time with this because all the players are likely involved in the discussion and the solution. An ad hoc approach to SSDL improvement isn’t sufficient for prevention.

#### [CMVM3.3] SIMULATE SOFTWARE CRISES.

`[CMVM3.3 | level 3 | 29/111 | 26.13%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.79 (left column)

The SSG simulates high-impact software security crises to ensure that software incident detection and response capabilities minimize damage. Simulations could test for the ability to identify and mitigate specific threats or could begin with the assumption that a critical system or service is already compromised and evaluate the organization’s ability to respond. Planned chaos engineering can be effective at triggering unexpected conditions during simulations. The exercises must include attacks or other software security crises at the appropriate software layer to generate useful results (e.g., at the application layer for web applications and at lower layers for IoT devices). When simulations model successful attacks, an important question to consider is the time required for cleanup. Regardless, simulations must focus on security-relevant software failure, not on natural disasters or other types of emergency response drills. Organizations that are highly dependent on vendor infrastructure (e.g., cloud service providers, SaaS, PaaS) and security features will naturally include those things in crisis simulations.

#### [CMVM3.4] OPERATE A BUG BOUNTY PROGRAM.

`[CMVM3.4 | level 3 | 34/111 | 30.63%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.79 (left column)

The organization solicits vulnerability reports from external researchers and pays a bounty for each verified and accepted vulnerability received. Payouts typically follow a sliding scale linked to multiple factors, such as vulnerability type (e.g., remote code execution is worth $10,000 vs. CSRF is worth $750), exploitability (demonstrable exploits command much higher payouts), or specific service and software versions (widely deployed or critical services warrant higher payouts). Ad hoc or short-duration activities, such as capture-the-flag contests or informal crowdsourced efforts, don’t constitute a bug bounty program.

#### [CMVM3.5] AUTOMATE VERIFICATION OF OPERATIONAL INFRASTRUCTURE SECURITY.

`[CMVM3.5 | level 3 | 24/111 | 21.62%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.79 (right column)

The SSG works with engineering teams to verify with automation the security properties (e.g., adherence to agreed upon security hardening) of infrastructure generated from controlled self-service processes. Engineers use self-service processes to create networks, storage, containers, and machine instances, to orchestrate deployments, and to perform other tasks that were once IT’s sole responsibility. In facilitating verification, the organization uses machine-readable policies and configuration standards (see [SE1.4]) to automatically detect issues and report on infrastructure that does not meet expectations. In some cases, the automation makes changes to running environments to bring them into compliance, but in many cases, organizations use a single policy to manage automation in different environments, such as in multi- and hybrid-cloud environments.

#### [CMVM3.6] PUBLISH RISK DATA FOR DEPLOYABLE ARTIFACTS.

`[CMVM3.6 | level 3 | 5/111 | 4.50%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.79 (right column)

The organization collects and publishes risk information about the applications, services, APIs, containers, and other software it deploys. Whether captured through manual processes or telemetry automation, published information extends beyond basic software security (see [SM2.1]) and inventory data (see [CMVM2.3]) to include risk information. This information usually includes constituency of the software (e.g., BOMs [SE3.6]), provenance data about what group created it and how, and the risks associated with known vulnerabilities, deployment models, security controls, or other security characteristics intrinsic to each artifact. This approach stimulates cross-functional coordination and helps stakeholders take informed risk management action. Making a list of risks that aren’t used for decision support won’t achieve useful results.

#### [CMVM3.8] DO ATTACK SURFACE MANAGEMENT FOR DEPLOYED APPLICATIONS.

`[CMVM3.8 | level 3 | 3/111 | 2.70%]` — Part 8, Configuration Management & Vulnerability Management (CMVM), p.79 (right column)

Operations standards and procedures proactively minimize application attack surfaces by using attack intelligence and application weakness data to limit vulnerable conditions. Finding and fixing software defects in operations is important (see [CMVM1.2]) but so is finding and fixing errors in cloud security models, VPNs, segmentation, security configurations for networks, hosts, and applications, etc., to limit the ability to successfully attack deployed applications. Combining attack intelligence (see [AM1.5]) with information about software assets (see [AM2.9]) and a continuous view of application weaknesses helps ensure that attack surface management keeps pace with attacker methods. SBOMs (see [SE3.6]) are also an important information source when doing attack surface management in a crisis.

