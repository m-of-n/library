---
schema: "library-distilled/v1"
id: cisa-secure-by-demand-guide-2024-normative
record: cisa-secure-by-demand-guide-2024
type: normative
updated: "2026-10-02"
reviewed_by: ""
---

# Secure by Demand Guide (CISA/FBI, Aug 2024) — normative statements

Source: 4-page PDF 'As of August 2024', sha256 4efa7d2e…6d16. Every question, artifact item and modal statement verbatim, grouped by the guide's sections. p.2 is two-column; verbatim checked against both layout and reading-order text.

## Overview (p.1)

- **OV-1** (Overview, p.1; *recommendation*, verb "is crucial", actor: software customer (acquirer)) — "Software manufacturers strive to deliver the features customers request, so it is crucial that customers explicitly demand security as part of the procurement process."
- **OV-2** (Overview, p.1; *recommendation*, verb "need to focus", actor: software customer (acquirer)) — "Although enterprise security is important, customers also need to focus on how a manufacturer approaches product security."
- **OV-def** (Overview, p.1; *definition*, verb "refers to", actor: n/a) — "Enterprise security refers to practices to protect a company's own infrastructure and operations, while product security refers to actions the software manufacturer takes to ensure the products they deliver are secure against attackers."
- **OV-3** (Overview, p.1; *permission*, verb "can also use", actor: software customer (acquirer)) — "Customer organizations can also use this guidance in procurement discussions with third party resellers or service providers."

## Overview — procurement lifecycle (p.1)

- **PL-1** (Overview — procurement lifecycle, p.1; *recommendation*, verb "can integrate", actor: software customer (acquirer)) — "Before procurement, by posing questions to understand each candidate software manufacturer's approach to product security."
- **PL-2** (Overview — procurement lifecycle, p.1; *recommendation*, verb "can integrate", actor: software customer (acquirer)) — "During procurement, by integrating product security requirements into contract language, as appropriate."
- **PL-3** (Overview — procurement lifecycle, p.1; *recommendation*, verb "can integrate", actor: software customer (acquirer)) — "Following procurement, by continually assessing software manufacturers' product security and security outcomes."

## Software Manufacturer Questions (p.2)

- **Q-lead** (Software Manufacturer Questions, p.2; *recommendation*, verb "should ask", actor: software customer (acquirer)) — "Customers should ask the following questions of their software manufacturers to understand the extent to which the manufacturer has designed the product with security in mind and to ensure quality and positive customer security outcomes."

## General Questions (p.2)

- **GEN-Q1** (General Questions, p.2; *question*, verb "(question)", actor: software customer (acquirer)) — "Has the manufacturer taken CISA's Secure by Design Pledge? What progress reports has the manufacturer published in line with its commitments to the pledge?"
- **GEN-Q2** (General Questions, p.2; *question*, verb "(question)", actor: software customer (acquirer)) — "How does the manufacturer make it simple for customers to install security patches? Does it offer support for security patches on a widespread basis and enable functionality for automatic updates?"
- **GEN-why** (General Questions — Why this is important, p.2; *rationale*, verb "(why)", actor: n/a) — "Why this is important: a company that has made the Pledge has publicly committed to take and demonstrate steps towards producing software that is secure by design."

## Authentication (p.2)

- **AUTH** (Authentication, p.2; *recommendation*, verb "should", actor: product (manufacturer)) — "The product should support secure authentication."
- **AUTH-Q1** (Authentication, p.2; *question*, verb "(question)", actor: software customer (acquirer)) — "Does the manufacturer support integrating standards-based single sign-on (SSO) for customers at no additional cost?"
- **AUTH-Q2** (Authentication, p.2; *question*, verb "(question)", actor: software customer (acquirer)) — "If the software manufacturer manages authentication, does it enable multi-factor authentication (MFA) or other phishing-resistant forms of authentication like passkeys by default, and at no cost?"
- **AUTH-Q3** (Authentication, p.2; *question*, verb "(question)", actor: software customer (acquirer)) — "Has the software manufacturer eliminated default passwords in its products? If not, is it working to reduce the use of default passwords across its product lines?"
- **AUTH-why** (Authentication — Why this is important, p.2; *recommendation*, verb "should", actor: software manufacturer) — "Default passwords should be replaced with more secure authentication mechanisms, such as random, instance-unique passwords."

## Eliminating Classes of Vulnerability (p.2)

- **VC** (Eliminating Classes of Vulnerability, p.2; *recommendation*, verb "should", actor: software manufacturer) — "The software manufacturer should systematically address entire classes of software defects across its products."
- **VC-Q1** (Eliminating Classes of Vulnerability, p.2; *question*, verb "(question)", actor: software customer (acquirer)) — "What classes of vulnerability has the software manufacturer systematically addressed in their products?"
- **VC-Q2** (Eliminating Classes of Vulnerability, p.2; *question*, verb "(question)", actor: software customer (acquirer)) — "For those that they haven't yet addressed, do they have a roadmap showing how they plan to eliminate those classes of vulnerability?"
- **VC-T** (Eliminating Classes of Vulnerability, p.2; *informative*, verb "(tactics)", actor: n/a) — "The following tactics are in line with a healthy secure development process:"
- **VC-T1** (Eliminating Classes of Vulnerability, p.2; *tactic*, verb "(tactic)", actor: software manufacturer) — "Consistently enforcing the use of parametrized queries to prevent SQL injection attacks."
- **VC-T2** (Eliminating Classes of Vulnerability, p.2; *tactic*, verb "(tactic)", actor: software manufacturer) — "Adopting web template frameworks with built-in protection against cross-site scripting vulnerabilities."
- **VC-T3** (Eliminating Classes of Vulnerability, p.2; *tactic*, verb "(tactic)", actor: software manufacturer) — "Transitioning code to memory safe languages in a prioritized approach and writing new products in memory safe languages."
- **VC-T4** (Eliminating Classes of Vulnerability, p.2; *tactic*, verb "(tactic)", actor: software manufacturer) — "Providing secure defaults for developers, such as by providing "building blocks" of secure functions and libraries that make it impossible (or significantly more difficult) to introduce a certain class of vulnerability."

## Evidence of Intrusions (p.3)

- **EI-1** (Evidence of Intrusions, p.3; *recommendation*, verb "should", actor: software manufacturer) — "Software manufacturers should make available security logs to customers in the baseline version of the product."
- **EI-2** (Evidence of Intrusions, p.3; *recommendation*, verb "should", actor: software manufacturer) — "For cloud service providers and software as a service (SaaS) providers, the software manufacturer should retain and make available to customers security logs for at least six months at no additional charge."
- **EI-3** (Evidence of Intrusions, p.3; *recommendation*, verb "should cover", actor: software manufacturer) — "Logs should cover areas such as:"

## Software Supply Chain Security (p.3)

- **SC** (Software Supply Chain Security, p.3; *recommendation*, verb "should", actor: software manufacturer) — "The software manufacturer should maintain and share provenance data of third-party dependencies and have processes to govern its use of, and contributions to, open source software components."
- **SC-Q1** (Software Supply Chain Security, p.3; *question*, verb "(question)", actor: software customer (acquirer)) — "Does the manufacturer generate a software bill of materials (SBOM) in a standard, machine-readable format and make this available to customers? Does the SBOM enumerate all third-party dependencies, including open source software components?"
- **SC-Q2** (Software Supply Chain Security, p.3; *question*, verb "(question)", actor: software customer (acquirer)) — "How does the software manufacturer vet the security of open source software components it incorporates and facilitate contributions back to help sustain those open source projects? Does the software manufacturer have an established process to do so, such as through an open source program office (OSPO)?"
- **SC-why-1** (Software Supply Chain Security — Why this is important, p.3; *recommendation*, verb "should", actor: software manufacturer) — "Software manufacturers should treat the security of their third-party dependencies as an extension of their own security."
- **SC-why-2** (Software Supply Chain Security — Why this is important, p.3; *recommendation*, verb "should", actor: software manufacturer) — "To that end, software manufacturers should continually maintain provenance data of their dependencies, share this with their customers, and establish processes (such as through an OSPO) to govern their use of, and contributions to, open source software components."

## Vulnerability Disclosure and Reporting (p.3)

- **VD** (Vulnerability Disclosure and Reporting, p.3; *recommendation*, verb "should", actor: software manufacturer) — "The software manufacturer should demonstrate transparency and timeliness in vulnerability reporting for both on-premises and cloud products."
- **VD-Q1** (Vulnerability Disclosure and Reporting, p.3; *question*, verb "(question)", actor: software customer (acquirer)) — "Does the software manufacturer include accurate Common Weakness Enumeration (CWE) and Common Platform Enumeration (CPE) fields in every CVE record for the software manufacturer's products?"
- **VD-Q2** (Vulnerability Disclosure and Reporting, p.3; *question*, verb "(question)", actor: software customer (acquirer)) — "Has the software manufacturer published a vulnerability disclosure policy that authorizes testing by members of the public on products offered by the software manufacturer?"
- **VD-why** (Vulnerability Disclosure and Reporting — Why this is important, p.3; *informative*, verb "(note)", actor: n/a) — "We note that issuing of CVEs is valuable even for SaaS products, while acknowledging that this is only now starting to become more standard practice."

## Artifacts you can collect (p.2, right column)

- **ART-M1** (Artifacts you can collect from a software manufacturer, p.2; *artifact*, verb "(collect)", actor: software customer (acquirer)) — "A Software Bill of Materials (SBOM) that lists third-party software components used by the product."
- **ART-M2** (Artifacts you can collect from a software manufacturer, p.2; *artifact*, verb "(collect)", actor: software customer (acquirer)) — "Roadmaps that highlight how the manufacturer plans to eliminate classes of vulnerability, such as a memory safe roadmap."
- **ART-S1** (Artifacts you can collect yourself, p.2; *artifact*, verb "(collect yourself)", actor: software customer (acquirer)) — "Whether the software manufacturer includes basic security features, like logging and single sign-on (SSO), in the baseline version of the product."
- **ART-S2** (Artifacts you can collect yourself, p.2; *artifact*, verb "(collect yourself)", actor: software customer (acquirer)) — "Whether the software manufacturer operates a vulnerability disclosure policy (which should be a public webpage)."
- **ART-S3** (Artifacts you can collect yourself, p.2; *artifact*, verb "(collect yourself)", actor: software customer (acquirer)) — "Whether the software manufacturer files timely and correct Common Vulnerabilities and Exposures (CVE) records."
- **ART-S4** (Artifacts you can collect yourself, p.2; *artifact*, verb "(collect yourself)", actor: software customer (acquirer)) — "Whether the software manufacturer has taken CISA's Secure by Design Pledge, and any progress reports published by the software manufacturer showing actions taken."

## Where to go for Further Information (p.4)

- **FI-1** (Where to go for Further Information, p.4; *recommendation*, verb "encourage", actor: software customer (acquirer)) — "We also encourage you to engage with your regional Cybersecurity Advisor and us at SecureByDesign@cisa.dhs.gov."

## Evidence of Intrusions — log areas (verbatim sub-bullets, p.3)

- Configuration changes or reading configuration settings;
- Identity (e.g., sign-in and token creation) and network flows, if applicable; and
- Data access or creation of business-relevant data.

## Resources named (p.1, p.4)

ICT SCRM Task Force, *Software Acquisition Guide for Government Enterprise Consumers: Software Assurance in the C-SCRM Lifecycle*; *Minimum Viable Secure Product*; CISA's Secure by Design Pledge; NIST's Secure Software Development Framework; CISA's Secure by Design white paper, blogs and alerts.


## Added by pass 2 (independent verifier, 2026-10-03)

Dropped by pass 1; verbatim with locator.

- **OV-4** (Overview, p.1; *recommendation*, verb "encourages", actor: software customer (acquirer)) — "For further guidance, CISA encourages organizations to read CISA’s Information and Communications Technology (ICT) Supply Chain Risk Management (SCRM) Task Force’s Software Acquisition Guide for Government Enterprise Consumers: Software Assurance in the Cyber-Supply Chain Risk Management (C-SCRM) Lifecycle, the Minimum Viable Secure Product, and CISA’s Secure by Design Pledge."
