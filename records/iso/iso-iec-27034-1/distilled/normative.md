---
schema: "library-distilled/v1"
id: iso-iec-27034-1-normative
record: iso-iec-27034-1
type: normative
updated: "2026-10-02"
---

# ISO/IEC 27034-1:2011 — readable normative and framing text (free preview only)

**Coverage, stated plainly.** ISO/IEC 27034-1:2011 is paywalled. This file holds **only** the
text that is legitimately free: the distributor-sample (iTeh/SIST) preview pages (front matter pp. i–xiv,
Clause 1, Clause 2 and Clause 3 up to and including 3.2, on p. 1). Everything from 3.3 onward —
the rest of the vocabulary, Clauses 4–8 (abbreviations, structure of the series, application
security concepts, the overall processes, the ONF / ASC / ASLC Reference Model / ANF / audit
concepts) and Annexes A–C — was **not read** and is not represented here. Clause *titles* for
that material come from the Table of Contents (p. iii–vi), which is in the preview.

Sources (hashes in `record.yaml` and `summary.md`):

- **P1a** — iTeh Standards preview of ISO/IEC 27034-1:2011, 15 pp, pp. i–xiv + p. 1.
  Watermark overlays drop a few words; gaps marked `[…]`.
- **P1b** — normsplash preview of the same document, 10 pp, pp. i–x. Used **only** to fill words the
  P1a watermark dropped on pp. i–x; where it filled a gap that is noted.

Every passage below is verbatim from the source. Clause 0 (Introduction) of an ISO document is
informative; its "should" sentences are recommendations, not requirements. The only
normative clauses in the preview are 1, 2 and 3.1–3.2, and none of them contains a "shall".

## Foreword (p. vii)

> ISO/IEC 27034-1 was prepared by Joint Technical Committee ISO/IEC JTC 1, Information technology,
> Subcommittee SC 27, IT Security techniques.
>
> ISO/IEC 27034 consists of the following parts, under the general title Information technology — Security
> techniques ― Application security:
>
> ― Part 1: Overview and concepts
>
> The following parts are under preparation:
>
> ― Part 2: Organization normative framework
> ― Part 3: Application security management process
> ― Part 4: Application security validation
> ― Part 5: Protocols and application security control data structure

(Part 2 line filled from P1b; P1a watermark obscured it.)

## 0.1 General (p. viii)

> Organizations should protect their information and technological infrastructures in order to stay in business.
> Traditionally this has been addressed at the IT level by protecting the perimeter and such technological
> infrastructure components as computers and networks, which is generally insufficient.

> In addition, organizations are increasingly protecting themselves at the governance level by operating
> formalized, tested and verified information security management systems (ISMS). A systematic approach
> contributes to an effective information security management system as described in ISO/IEC 27001.

> However, organizations face an ever-growing need to protect their information at the application level.

> Applications should be protected against vulnerabilities which might be inherent to the application itself (e.g.
> software defects), appear in the course of the application's life cycle (e.g. through changes to the application),
> or arise due to the use of the application in a context for which it was not intended.

> A systematic approach to increased application security provides evidence that information being used or
> stored by an organization's applications is adequately protected.

> Applications can be acquired through internal development, outsourcing or purchasing a commercial product.
> Applications can also be acquired through a combination of these approaches which might introduce new
> security implications that should be considered and managed.

> Throughout its life cycle, a secure application exhibits prerequisite characteristics of software quality, such as
> predictable execution and conformance, as well as meeting security requirements from a development,
> management, technological infrastructure, and audit perspective. Security-enhanced processes and
> practices—and the skilled people to perform them—are required to build trusted applications that do not
> increase risk exposure beyond an acceptable or tolerable level of residual risk and support an effective ISMS.

("predictable execution and conformance" filled from P1b.)

> Additionally, a secure application takes into account the security requirements stemming from the type of data,
> the targeted environment (business, regulatory and technological contexts), the actors and the application
> specifications. It should be possible to obtain evidence that is shown to demonstrate that an acceptable (or
> tolerable) level of residual risk has been attained and is being maintained.

## 0.2 Purpose (pp. viii–ix)

> The purpose of ISO/IEC 27034 is to assist organizations in integrating security seamlessly throughout the life
> cycle of their applications by:
>
> a) providing concepts, principles, frameworks, components and processes;
> b) providing process-oriented mechanisms for establishing security requirements, assessing security
>    risks, assigning a Targeted Level of Trust and selecting corresponding security controls and
>    verification measures;
> c) providing guidelines for establishing acceptance criteria to organizations outsourcing the development
>    or operation of applications, and for organizations purchasing from third-party applications;
> d) providing process-oriented mechanisms for determining, generating and collecting the evidence
>    needed to demonstrate that their applications can be used securely under a defined environment;
> e) supporting the general concepts specified in ISO/IEC 27001 and assisting with the satisfactory
>    implementation of information security based on a risk management approach; and
> f) providing a framework that helps to implement the security controls specified in ISO/IEC 27002 and
>    other standards.

> ISO/IEC 27034:
>
> a) applies to the underlying software of an application and to contributing factors that impact its security,
>    such as data, technology, application development life cycle processes, supporting processes and
>    actors; and
> b) applies to all sizes and all types of organizations (e.g. commercial enterprises, government agencies,
>    non-profit organizations) exposed to risks associated with applications.

> ISO/IEC 27034 does not:
>
> a) provide guidelines for physical and network security;
> b) provide controls or measurements; or
> c) provide secure coding specifications for any programming language.

> ISO/IEC 27034 is not:
>
> a) a software application development standard;
> b) an application project management standard; or
> c) a software development life cycle standard.

> The requirements and processes specified in ISO/IEC 27034 are not intended to be implemented in isolation
> but rather integrated into an organization's existing processes. To this effect, organizations should map their
> existing processes and frameworks to those proposed by ISO/IEC 27034, thus reducing the impact of
> implementing ISO/IEC 27034.

> Annex A (informative) provides an example illustrating how an existing software development process can be
> mapped to some of the components and processes of ISO/IEC 27034. Generally speaking, an organization
> using any development life cycle should perform a mapping such as the one described in Annex A, and add
> whatever missing components or processes are needed for compliance with ISO/IEC 27034.

## 0.3 Targeted audiences (pp. ix–xi)

### 0.3.1 General

> The following audiences will benefit from ISO/IEC 27034 while carrying out their designated organizational
> roles:
>
> a) managers;
> b) provisioning and operation teams;
> c) acquisition personnel;
> d) suppliers; and
> e) auditors.

### 0.3.2 Managers

> Managers are persons involved in the management of the application during its complete life cycle. The
> applicable stages of the application life cycle include the provisioning stages and the production stages.
> Examples of managers are:
>
> a) information security managers;
> b) project managers;
> c) administrators;
> d) software acquirers;
> e) software development managers;
> f) application owners;
> g) line managers, who supervise employees.

> Typically managers need to:
>
> a) balance the cost of implementing and maintaining application security against the risks and value it
>    represents for the organization;
> b) review auditor's reports recommending acceptance or rejection based on whether an application has
>    attained and maintained its Targeted Level of Trust;
> c) ensure compliance with standards, laws and regulations according to an application's regulatory
>    context (see 8.1.2.2);
> d) oversee the implementation of a secure application;
> e) authorize the Targeted Level of Trust according to the organization's specific context;
> f) determine which security controls and corresponding verification measurements should be
>    implemented and tested;
> g) minimize application security verification costs;
> h) document security policies and procedures for an application;
> i) provide security awareness, training and oversight to all actors;
> j) put in place proper information security clearances required by applicable information security policies
>    and procedures; and
> k) stay abreast of all system-related security plans throughout the organization's network.

### 0.3.3 Provisioning and operation teams

> Members of provisioning and operation teams (known collectively as the project team) are persons involved in
> an application's design, development and maintenance throughout its whole life cycle. Members include:
>
> a) architects,
> b) analysts,
> c) programmers,
> d) testers,
> e) system administrators,
> f) database administrators,
> g) network administrators, and
> h) technical personnel.

(d) and e) filled from P1b.)

> Typically members need to:
>
> a) understand which controls should be applied at each stage of an application's life cycle and why;
> b) understand which controls should be implemented in the application itself;
> c) minimize the impact of introducing controls into the development, test and documentation activities
>    within the application life cycle;
> d) make sure that introduced controls meet the requirements of the associated measurements;
> e) obtain access to tools and best practices in order to streamline development, testing and
>    documentation;
> f) facilitate peer review;
> g) participate in acquisition planning and strategy;
> h) establish business relationships to obtain needed goods and services, (e.g. for the solicitation,
>    evaluation and awarding of contracts); and
> i) arrange disposal of residual items after work is completed, (e.g. property management/disposal).

### 0.3.4 Acquirers (p. xi)

> This includes all persons involved in acquiring a product or service.
>
> Typically acquirers need to:
>
> a) prepare requests for proposals that include requirements for security controls;
> b) select suppliers that comply with such requirements;
> c) verify evidence of security controls applied by outsourcing services; and
> d) evaluate products by verifying evidence of correctly implemented application security controls.

### 0.3.5 Suppliers

> This includes all persons involved in supplying a product or service.
>
> Typically suppliers need to:
>
> a) comply to application security requirements from requests for proposals;
> b) select appropriate application security controls for proposals, with respect to their impact on cost; and
> c) provide evidence that required security controls are implemented correctly in proposed products or
>    services.

### 0.3.6 Auditors

> Auditors are persons who need to:
>
> a) understand the scope and procedures involved in verification measurements for the corresponding […]
> b) ensure that audit results are repeatable;
> c) establish a list of verification measurements which generate evidence that an application has reached
>    the Targeted Level of Trust as required by management; and
> d) apply standardized audit processes based on the use of verifiable evidence.

(Item a) is truncated by the P1a watermark; P1b does not reach p. xi.)

### 0.3.7 Users

> […] Users are persons who need to:
>
> a) trust that it is deemed secure to use or deploy an application;
> b) trust that an application produces reliable results consistently and in a timely manner; and
> c) trust that the controls and their corresponding verification measurements are positioned and
>    functioning correctly as expected.

(The 0.3.7 heading line is obscured in P1a; the clause number is from the ToC.)

## 0.4 Principles (pp. xi–xii)

### 0.4.1 Security is a requirement

> Security requirements should be defined and analyzed for each and every stage of an application's life cycle,
> adequately addressed and managed on a continuous basis.

> Application security requirements (see 6.4) should be treated in the same manner as functionality, quality and
> usability requirements (see ISO/IEC 9126 for an example of a quality model). In addition, security-related
> requirements to conform to the established limitations on residual risk should be instituted.

> According to ISO/IEC/IEEE 29148 (under development), requirements should be necessary, abstract,
> unambiguous, consistent, complete, concise, feasible, traceable and verifiable. The same characteristics
> apply to security requirements. Vague security requirements such as "The developer should discover all
> important security risks for the application" are too often encountered in application projects' documentation.

### 0.4.2 Application security is context-dependent

> Application security is influenced by a defined target environment. The type and scope of application security
> requirements are determined by the risks to which the application is subjected, which in turn depend on three
> contexts:
>
> a) business context: specific risks arising from the organization's business domain (phone company,
>    transport company, government, etc.);
> b) regulatory context: specific risks arising from the geographical location where the organization is doing
>    business (intellectual property rights and licensing, restrictions on cryptography protection, copyright,
>    laws and regulations, privacy legislation, etc.);
> c) technological context: specific risks from the technologies used by the organization in the course of
>    business [reverse engineering, security of build tools, protection of source code, use of third-party pre-
>    compiled code, security testing, penetration testing, bounds checking, code checking, information and
>    communication technology (ICT) environment in which the application runs, configuration files and
>    uncompiled data, operating system privileges for installation and/or operation, maintenance, secure
>    distribution, etc.].
>    The technological context encompasses applications' technical specifications (security functionality,
>    secure components, online payments, secure log, cryptography, permissions management, etc.).

> An organization can affirm that an application is secure, but this affirmation is only valid for this particular
> organization in its specific business, regulatory and technological contexts. If, for example, the application's
> technological infrastructure changes, or the application is used for the same purposes in another country,
> these new contexts might impact the security requirements and the Targeted Level of Trust. The current
> Application Security Controls might no longer adequately address the new security requirements and the
> application might no longer be secure.

### 0.4.3 Appropriate investment for application security

> The costs of applying Application Security Controls and performing audit measurements should be
> commensurate with the Targeted Level of Trust (see 8.1.2.6.4) required by the application owner or by […]
> These costs can be considered as an investment because they reduce the costs, application owner
> responsibilities and legal consequences of security breaches.

(In P1a the watermark text is interleaved with "(see 8.1.2.6.4)" and covers the end of the first
sentence. The words quoted are the legible ones, in reading order.)

### 0.4.4 Application security should be demonstrated

> The application auditing process in ISO/IEC 27034 (see 8.5) makes use of the verifiable evidence provided by
> Application Security Controls (see 8.1.2.6.5).

> An application cannot be declared secure unless the auditor agrees that the supporting evidence generated
> by the corresponding verification measurements of the applicable Application Security Controls demonstrates
> that it has reached management's Targeted Level of Trust.

## 0.5 Relationship to other International Standards (pp. xiii–xiv)

**0.5.1 General**

> Figure 1 shows relationships between ISO/IEC 27034 and other International Standards.

(Figure 1 is an image; not captured.)

> **0.5.2 ISO/IEC 27001** — ISO/IEC 27034 helps to implement, with a scope limited to application security, recommendations from
> ISO/IEC 27001. In particular, the following approaches are used:
> a) systematic approach to security management;
> b) "Plan, Do, Check, Act" process approach; and
> c) implementation of information security based on risk management.

> **0.5.3 ISO/IEC 27002** — ISO/IEC 27002 provides practices that an organization can implement as Application Security Controls as
> proposed by ISO/IEC 27034. Of utmost interest are controls from the following clauses in
> ISO/IEC 27002:2005:
> a) clause 10: Communications and Operations Management;
> b) clause 11: Access Control; and most importantly
> c) clause 12: Information Systems Acquisition, Development and Maintenance.

> **0.5.4 ISO/IEC 27005** — ISO/IEC 27034 helps to implement, with a scope limited to application security, the risk management process
> proposed by ISO/IEC 27005. See Annex C (informative) for a more detailed discussion.

> **0.5.5 ISO/IEC 21827 (SSE-CMM)** — ISO/IEC 21827 provides security engineering base practices that an organization can implement as
> Application Security Controls as proposed by ISO/IEC 27034. In addition, processes from ISO/IEC 27034 help
> to attain several of the capabilities that define the capability levels in ISO/IEC 21827.

> **0.5.6 ISO/IEC 15408-3** — ISO/IEC 15408-3 provides requirements and action elements that an organization can implement as
> Application Security Controls as proposed by ISO/IEC 27034.

> **0.5.7 ISO/IEC TR 15443-1 and TR 15443-3** — ISO/IEC 27034 helps to enforce and reflect the principles of security assurance from ISO/IEC TR 15443-1 and
> to contribute to the assurance cases of ISO/IEC TR 15443-3.

> **0.5.8 ISO/IEC 15026-2** — Use of processes and Application Security Controls from ISO/IEC 27034 in application projects directly
> provides assurance cases about the security of the application. In particular,
> a) claims and their justifications are provided by the application security risk analysis process,
> b) evidence is provided by Application Security Controls' built-in verification measurements, and
> c) compliance to ISO/IEC 27034 can be used as argument in many such assurance cases.
> See also 8.1.2.6.5.1.

> **0.5.9 ISO/IEC 15288 and ISO/IEC 12207** — ISO/IEC 27034 provides additional processes for the organization, as well as Application Security Controls
> that an organization can insert as additional activities into its existing systems and software engineering life
> cycle processes as provided by ISO/IEC 15288 and ISO/IEC 12207.

> **0.5.10 ISO/IEC TR 29193** — ISO/IEC TR 29193 provides guidance for secure system engineering of ICT systems or products that an
> organization can implement as Application Security Controls as proposed by ISO/IEC 27034.

## 1 Scope (p. 1) — normative

> ISO/IEC 27034 provides guidance to assist organizations in integrating security into the processes used for
> managing their applications.
>
> This part of ISO/IEC 27034 presents an overview of application security. It introduces definitions, concepts,
> principles and processes involved in application security.
>
> ISO/IEC 27034 is applicable to in-house developed applications, applications acquired from third parties, and
> where the development or the operation of the application is outsourced.

## 2 Normative references (p. 1)

> ISO/IEC 27000:2009, Information technology — Security techniques — Information security management
> systems — Overview and vocabulary
>
> ISO/IEC 27001:2005, Information technology — Security techniques — Information security management
> systems — Requirements
>
> ISO/IEC 27002:2005, Information technology — Security techniques — Code of practice for information
> security management
>
> ISO/IEC 27005:2011, Information technology — Security techniques — Information security risk management

## 3 Terms and definitions (p. 1) — readable only to 3.2

> For the purposes of this document, the terms and definitions given in ISO/IEC 27000, ISO/IEC 27001,
> ISO/IEC 27002, ISO/IEC 27005 and the following apply.

> **3.1 actor** — person or process that performs an activity during an application's life cycle or initiates interaction with any
> process provided by or impacted on by an application

> **3.2 Actual Level of Trust** — result of an audit process that provides supporting evidence that all Application Security Controls required by
> the application's Targeted Level of Trust were correctly implemented and verified, and produced the expected
> results

**Not read:** 3.3 onward. From the ToC and the rest of the series, the vocabulary goes on to define
(at least) application, application owner, Application Normative Framework, application
security audit, Application Security Control, Application Security Life Cycle Reference Model,
application security verification, level of trust, Organization Normative Framework, Targeted
Level of Trust, and verification measurement. None of those 27034-1 definitions is quoted here,
because none was read.

## Clause structure of the unread body (from the ToC, pp. iii–vi)

The titles below are verbatim ToC entries. They show where 27034-1 defines the objects that
`object-model.yaml` reconstructs from other sources. They are **locators, not content**.

| Clause | Title (ToC) |
|---|---|
| 5 | Structure of ISO/IEC 27034 |
| 6.3.2–6.3.10 | Business context · Regulatory context · Application life cycle processes · Processes involved with the application · Technological context · Application specifications · Application data · Organization and user data · Roles and permissions |
| 6.4 | Application security requirements (6.4.1 sources, 6.4.2 engineering, 6.4.3 ISMS) |
| 6.5 | Risk (6.5.1 application security risk, 6.5.2 vulnerabilities, 6.5.3 threats, 6.5.4 impact, 6.5.5 risk management) |
| 6.8 | Controls and their objectives |
| 7.1 | Components, processes and frameworks |
| 7.2 | ONF management process |
| 7.3 | Application security management process: 7.3.2 Specifying the application requirements and environment · 7.3.3 Assessing application security risks · 7.3.4 Creating and maintaining the Application Normative Framework · 7.3.5 Provisioning and operating the application · 7.3.6 Auditing the security of the application |
| 8.1 | Organization Normative Framework (8.1.2 Components; 8.1.3 Processes related to the ONF). Body cross-references in the Introduction locate the regulatory context at 8.1.2.2, the Targeted Level of Trust at 8.1.2.6.4 and ASC verifiable evidence at 8.1.2.6.5 / 8.1.2.6.5.1 |
| 8.2 | Application security risk assessment (8.2.4 Application's Targeted Level of Trust; 8.2.5 Application owner acceptation) |
| 8.3 | Application Normative Framework (8.3.4 Application's life cycle) |
| 8.4 | Provisioning and operating the application (8.4.2 Impact of ISO/IEC 27034 on an application project) |
| 8.5 | Application security audit |
| Annex A | Mapping an existing development process to ISO/IEC 27034 case study (Microsoft SDL: A.3 SDL mapped to the ONF; A.9 Organization ASC library — Training, Requirements, Design, Implementation, Verification, Release; A.12 SDL mapped to the ASLC Reference Model) |
| Annex B | Mapping ASC with an existing standard (NIST SP 800-53 Rev. 3; B.5 AU-14 rendered in ASC format) |
| Annex C | ISO/IEC 27005 risk management process mapped with the ASMP |

Figure titles in the ToC: Fig. 2 Application Security Scope; Fig. 3 Organization Management
Processes; Fig. 4 Organization Normative Framework (simplified); Fig. 5 example Organization ASC
Library; **Fig. 6 Components of an ASC**; **Fig. 7 Graph of ASCs**; **Fig. 8 Top-level view of the
Application Security Life Cycle Reference Model**; Fig. 9 ONF Management Process; Fig. 10
Application Normative Framework; Fig. 12 ASC used as a security activity; Fig. 13 ASC used as a
measurement; Fig. 14 Overview of the application security verification process. Table 1
Application Scope vs Application Security Scope; Table 2 Mapping of ISMS and application
security-related ONF management subprocesses.
