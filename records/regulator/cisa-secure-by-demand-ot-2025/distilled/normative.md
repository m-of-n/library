---
record: cisa-secure-by-demand-ot-2025
kind: normative
title: "cisa-secure-by-demand-ot-2025 — normative text"
generated_by: bin/fx1-skeleton, rewritten by pass 1 (requirements lane) as markers emitted by script
reviewed_by: ""
---

# Normative text

Every quotation below is a marker whose words `bin/check-quotes --render` wrote from the
pinned `pdftotext -layout` rendering (`requirements.yaml` `source_text_digest`); no quotation
was typed. The line after each quotation names its `requirements.yaml` entry, emitted by script
from that file: role (criterion, question, threat model question, goal, element, seek-out), the
lead-in an item belongs to, the skeleton sentence a child was split from, the candidate it
promotes, the footnote it quotes. A skeleton sentence that welds several statements is shown
through its children, a unit with children (a criterion or a Summary sentence) as the unit; so
every verbal form of the source appears once, in the statement that carries it. A line in
parentheses with no id marks informative text: rationale, an example, a reference, a footnote
or a cell, quoted for structure and context, binding nothing.

This is joint guidance (CISA and eleven partner agencies), not a standard. It states that it
binds no one (see *How the guide binds*); its should is a recommendation to buyers or
manufacturers and its few musts are the authors’ strongest wording. `requirements.yaml`’s
header note gives the judgement conventions; the defects found in the source are at the end.

## Coverage

Counted by script from `requirements.yaml`.

| consideration | criteria | questions to ask | threat model questions | goal | entries naming it |
|---|---|---|---|---|---|
| Configuration Management | 1 | 3 | 0 | 1 | 17 |
| Logging in the Baseline Product | 1 | 3 | 0 | 1 | 24 |
| Open Standards | 1 | 2 | 0 | 1 | 13 |
| Ownership | 1 | 3 | 0 | 1 | 18 |
| Protection of Data | 1 | 3 | 0 | 1 | 11 |
| Secure by Default | 1 | 3 | 0 | 1 | 34 |
| Secure Communications | 1 | 2 | 0 | 1 | 18 |
| Secure Controls | 1 | 5 | 0 | 1 | 27 |
| Strong Authentication | 1 | 2 | 0 | 1 | 21 |
| Threat Modeling | 1 | 3 | 6 | 1 | 20 |
| Vulnerability Management | 3 | 5 | 0 | 1 | 39 |
| Upgrade and Patch Tooling | 2 | 6 | 0 | 1 | 37 |
| **all twelve** | **15** | **40** | **6** | **12** | **279** |

## How the guide binds

The status sentences, quoted where they sit (Summary footnote 4, Disclaimer); read together in
R-0311 (inferred).

## Summary

### Preamble

<!-- q L35-36 "Cyber threat actors" .. "to control systems." -->
> Cyber threat actors can easily exploit these weaknesses across multiple victims to gain access to control systems.

R-0001

<!-- q L38-41 "This Secure by" .. "other OT products." -->
> This Secure by Demand guide, authored by CISA with contributions from the following partners, describes how OT owners and operators should integrate security into their procurement process when purchasing industrial automation and control systems as well as other OT products.

R-0102 (split from R-0002)

The partner list (L42-53) names the co-authoring agencies; footnote numbers 3 and 4 print in it.

### The twelve security elements

<!-- q L84-85 -->
> When procuring products, OT owners and operators should select products from manufacturers who prioritize the following security elements:

R-0003

#### 1. Configuration Management

<!-- q L86-87 "The product supports" .. "and engineering logic." -->
> The product supports controlling and tracking modifications to configuration settings and engineering logic.

R-0168 (element; item of R-0003; candidate C-0007)

<!-- q L87-88 "Seek out manufacturers" .. "and simple manner." -->
> Seek out manufacturers whose products backup and deploy system configurations in a secure and simple manner.

R-0169 (seek-out; item of R-0003; candidate C-0008)

#### 2. Logging in the Baseline Product

<!-- q L89-91 "The product supports" .. "standard logging formats." -->
> The product supports logging of all actions—including changes to configuration, security events, and safety events—in the baseline versions using open standard logging formats.

R-0170 (element; item of R-0003; candidate C-0009)

<!-- q L91-92 "Seek out products" .. "incident response capabilities." -->
> Seek out products that come with standardized access and change logs for building incident response capabilities.

R-0171 (seek-out; item of R-0003; candidate C-0010)

#### 3. Open Standards

<!-- q L93-94 "The product uses" .. "and engineering logic." -->
> The product uses open standards to support secure functions and services and for migrating configuration settings and engineering logic.

R-0172 (element; item of R-0003; candidate C-0011)

<!-- q L94-95 "Seek out products" .. "or adding products." -->
> Seek out products that support open, interoperable standards to facilitate replacing or adding products.

R-0173 (seek-out; item of R-0003; candidate C-0012)

#### 4. Ownership

<!-- q L96-97 "The product gives" .. "maintenance and changes." -->
> The product gives owners and operators full autonomy over said product, including maintenance and changes.

R-0174 (element; item of R-0003; candidate C-0013)

<!-- q L97-98 "Seek out products" .. "on the vendor." -->
> Seek out products that enable operator autonomy while minimizing dependency on the vendor.

R-0175 (seek-out; item of R-0003; candidate C-0014)

#### 5. Protection of Data

<!-- q L99-100 "The product protects" .. "and engineering logic." -->
> The product protects the integrity and confidentiality of data, services, and functions, including a product’s configuration settings and engineering logic.

R-0176 (element; item of R-0003; candidate C-0015)

<!-- q L100-102 "Seek out products" .. "vendors and manufacturers." -->
> Seek out products that treat operational data as valuable and protect it at rest and during transit to and from vendors and manufacturers.

R-0177 (seek-out; item of R-0003; candidate C-0016)

#### 6. Secure by Default

<!-- q L103-104 "The product is" .. "owners and operators." -->
> The product is delivered secure out of the box, reducing the attack surface and removing the burden on owners and operators.

R-0178 (element; item of R-0003; candidate C-0017)

<!-- q L104-109 "Seek out products" .. "its original state." -->
> Seek out products that include all security features in all versions; eliminate default passwords; allow for appropriate length and complexity for passwords; use secure up-to-date versions of protocols with older insecure protocols (e.g., SNMPv1/2, Telnet, SSL, TLS 1.0/1.1) disabled by default; do not unnecessarily expose external interfaces; and provide authorized users the ability to reset product configuration to its original state.

R-0179 (seek-out; item of R-0003; split into R-0180 to R-0185; candidate C-0018)

#### 7. Secure Communications

<!-- q L110-112 "The product supports" .. "processes to continue." -->
> The product supports secure authenticated communication with digital certificates deployed that fail loudly (e.g., when a certificate expires) but allows critical processes to continue.

R-0186 (element; item of R-0003; candidate C-0019)

<!-- q L112-113 "Seek out products" .. "secure authenticated communications." -->
> Seek out products that simplify digital certificate deployment and renewal such that operators do not need to be cyber experts to achieve secure authenticated communications.

R-0187 (seek-out; item of R-0003; candidate C-0020)

#### 8. Secure Controls

<!-- q L114-116 "The product is" .. "the overall system." -->
> The product is resilient to threat actors sending malicious emergency, safety, or diagnostic commands; protects the availability of essential functions; withstands active security scanning; and minimizes the impact of an incident on the overall system.

R-0188 (element; item of R-0003; split into R-0189 to R-0192; candidate C-0021)

<!-- q L116-118 "Seek out manufacturers" .. "regain that trust." -->
> Seek out manufacturers who can demonstrate trusted safety-critical controls and explain how operators can continuously verify and regain that trust.

R-0004 (seek-out; item of R-0003)

#### 9. Strong Authentication

<!-- q L119-121 "The baseline version" .. "phishing-resistant multifactor authentication." -->
> The baseline version of the product, especially safety-critical equipment, protects against unauthorized access through appropriate control measures, including role-based access control and phishing-resistant multifactor authentication.

R-0193 (element; item of R-0003; candidate C-0022)

<!-- q L121-122 "Seek out manufacturers" .. "in their products." -->
> Seek out manufacturers that have eliminated the use of shared role-based passwords in their products.

R-0194 (seek-out; item of R-0003; candidate C-0023)

#### 10. Threat Modeling

<!-- q L132-132 "The product has" .. "detailed threat model." -->
> The product has a full and detailed threat model.

R-0195 (element; item of R-0003; candidate C-0024)

<!-- q L132-134 "Seek out products" .. "these threat scenarios." -->
> Seek out products that have an up-to-date threat model that articulates the ways in which it might be compromised, along with security measures implemented to reduce these threat scenarios.

R-0196 (seek-out; item of R-0003; candidate C-0025)

#### 11. Vulnerability Management

<!-- q L135-137 "The manufacturer has" .. "known exploitable vulnerabilities." -->
> The manufacturer has a comprehensive vulnerability management regime in which products are rigorously tested to help ensure they contain no known exploitable vulnerabilities.

R-0197 (element; item of R-0003; candidate C-0026)

<!-- q L137-138 "Each product has" .. "free of charge." -->
> Each product has a clearly defined support period during which vulnerabilities are managed and patches are supplied free of charge.

R-0198 (element; item of R-0003; candidate C-0027)

<!-- q L138-140 "Seek out manufacturers" .. "vulnerability disclosure program." -->
> Seek out manufacturers who include hardware and software bill of materials with product delivery and who commit to timely remediation of vulnerabilities through a vulnerability disclosure program.

R-0199 (seek-out; item of R-0003; split into R-0200, R-0201; candidate C-0028)

#### 12. Upgrade and Patch Tooling

<!-- q L141-143 "The product has" .. "no longer supported." -->
> The product has a well-documented and easy to follow patch and upgrade process and supports moving to a supported operating system version at no extra cost if the original operation system is soon to be no longer supported.

R-0202 (element; item of R-0003; split into R-0203, R-0204; candidate C-0029)

<!-- q L143-144 "Seek out products" .. "owner-controlled patch management." -->
> Seek out products that can be verified and that support owner-controlled patch management.

R-0005 (seek-out; item of R-0003)

### After the list

<!-- q L145-147 "By rigorously enforcing" .. "from legacy environments." -->
> By rigorously enforcing purchasing decisions that require and prioritize the purchase of products that enforce these elements, critical infrastructure organizations can help mitigate current and emerging cyber threats to critical infrastructure and create a path away from legacy environments.

R-0006

<!-- q L149-150 -->
> Manufacturers that implement these considerations can establish a resilient and flexible cybersecurity foundation in their products that OT owners and operators can build on over the coming decades.

R-0007

<!-- q L151-152 "Additionally, owners and" .. "digital systems acquisition." -->
> Additionally, owners and operators may need to consider regulatory requirements, such as the European Union’s (EU’s) NIS2 Directive, during digital systems acquisition.

R-0103 (split from R-0008)

<!-- q L152-154 "Where applicable, owners" .. "of regulatory compliance." -->
> Where applicable, owners and operators should ensure that the products they buy are compliant with applicable legal obligations and carry required marks of regulatory compliance.

R-0104 (split from R-0008)

### Footnotes 1 to 6

<!-- q L56-61 "CISA’s Secure by" .. "by Design Software." -->
> CISA’s Secure by Design campaign urges technology providers to take ownership of their customers’ security outcomes by building cybersecurity into design and development. As part of CISA’s campaign, CISA and partners developed three core principles to guide software manufacturers in building software security into their design process. For more information, see joint guide Secure-by-Design - Shifting the Balance of Cybersecurity Risk: Principles and Approaches for Secure by Design Software.

(footnote 1, informative: the Secure by Design campaign and its three principles, which R-0010 names)

<!-- q L62-64 "European Union (EU)" .. "the manufacturing sector." -->
> European Union (EU) legislation refers to essential and important entities, such as critical infrastructures as well as entities in the manufacturing sector.

R-0163 (footnote 2)

<!-- q L65-69 "NSA manages the" .. "the product evaluations." -->
> NSA manages the National Information Assurance Partnership (NIAP) program and is piloting the Operational Technology Assurance Partnership (OTAP) program. These oversee evaluation of Commercial Off-the-Shelf (COTS) IT and OT products for use in National Security Systems (NSS) and develop security functional requirements and assurance activities for the product evaluations.

(footnote 3, informative: NSA’s NIAP and OTAP evaluation programs; C-0003’s reason explains its weld with footnote 4)

<!-- q L70-72 "This document does" .. "of Union law." -->
> This document does not interpret European Union law nor is it meant to be a guidance for implementation of Union law.

R-0164 (candidate C-0003; footnote 4)

<!-- q L72-72 "The document does" .. "the European Commission." -->
> The document does not bind the European Commission.

R-0165 (candidate C-0004; footnote 4)

<!-- q L73-74 "However, as this" .. "reflect Union law." -->
> However, as this document is a multilateral effort, not all of its elements reflect Union law.

R-0166 (footnote 4)

<!-- q L74-75 "Entities falling within" .. "information purposes only." -->
> Entities falling within the scope of Union law might use this document for information purposes only.

R-0167 (candidate C-0006; footnote 4)

<!-- q L159-161 "The NIS2 directive" .. "networks are secure." -->
> The NIS2 directive requires critical infrastructures and certain other entities providing services in the Union to take measures to ensure that the products deployed on their networks are secure.

R-0205 (candidate C-0031 and C-0032; footnote 5)

<!-- q L161-164 "In addition, several" .. "December 10, 2024." -->
> In addition, several countries and regions have started laying down security-by-design in law, such as the EU’s Delegated Regulation on the Radio Equipment Directive, which will apply from 1 August 2025, and the Cyber Resilience Act, entered into force on December 10, 2024.

(footnote 5, informative: security by design in law, with dates)

<!-- q L165-168 "The CE marking" .. "of the product." -->
> The CE marking is required by the EU’s Cyber Resilience Act for products with digital elements placed on the Union market and that products have been subjected to legally required conformity assessment procedures that are in line with the intended purpose and the risk profile of the product.

R-0206 (candidate C-0033 and C-0034; footnote 6)

## Introduction

Binding here without a verbal form: the scope and the definition of buyers. The six
Introduction forms (C-0036, C-0037, C-0038, C-0040 twice, C-0041) are context, threat and benefit,
and are rejected with reasons in `inferred-candidates.yaml`, as are C-0035 and C-0039.

<!-- q L228-229 "This document is" .. "by design elements." -->
> This document is intended to help owners and operators purchase OT products, particularly industrial automation and control system products, with priority secure by design elements.

R-0207

<!-- q L229-230 "Owners and operators" .. "as “buyers” hereafter." -->
> Owners and operators purchasing products are referred to as “buyers” hereafter.

R-0208

## Considerations for OT Product Selection

<!-- q L252-252 -->
> Buyers should look for the following key security elements when selecting OT products:

R-0009

The two-column list of L253-258, cell by cell (a `-layout` row welds two cells, C-0042 to C-0047):

<!-- q L253-253 "1. Configuration Management" .. "1. Configuration Management" -->
> 1. Configuration Management

(cell of the title list, informative)

<!-- q L253-253 "7. Secure Communications" .. "7. Secure Communications" -->
> 7. Secure Communications

(cell of the title list, informative)

<!-- q L254-254 "2. Logging in" .. "the Baseline Product" -->
> 2. Logging in the Baseline Product

(cell of the title list, informative)

<!-- q L254-254 "8. Secure Controls" .. "8. Secure Controls" -->
> 8. Secure Controls

(cell of the title list, informative)

<!-- q L255-255 "3. Open Standards" .. "3. Open Standards" -->
> 3. Open Standards

(cell of the title list, informative)

<!-- q L255-255 "9. Strong Authentication" .. "9. Strong Authentication" -->
> 9. Strong Authentication

(cell of the title list, informative)

<!-- q L256-256 "4. Ownership" .. "4. Ownership" -->
> 4. Ownership

(cell of the title list, informative)

<!-- q L256-256 "10. Threat Modeling" .. "10. Threat Modeling" -->
> 10. Threat Modeling

(cell of the title list, informative)

<!-- q L257-257 "5. Protection of" .. "Protection of Data" -->
> 5. Protection of Data

(cell of the title list, informative)

<!-- q L257-257 "11. Vulnerability Management" .. "11. Vulnerability Management" -->
> 11. Vulnerability Management

(cell of the title list, informative)

<!-- q L258-258 "6. Secure by" .. "Secure by Default" -->
> 6. Secure by Default

(cell of the title list, informative)

<!-- q L258-258 "12. Upgrade and" .. "and Patch Tooling" -->
> 12. Upgrade and Patch Tooling

(cell of the title list, informative)

<!-- q L259-260 "The key elements" .. "of their products." -->
> The key elements above collectively enable buyers to consider how manufacturers are including security in the design and development of their products.

(informative: what the elements enable; welded to the last row in C-0047)

<!-- q L260-260 "These elements are" .. "in priority order." -->
> These elements are not in priority order.

R-0209 (candidate C-0048)

<!-- q L260-264 "As buyers are" .. "of design decisions." -->
> As buyers are checking for these elements, they should ensure their manufacturers are familiar with the Secure by Design principles of taking ownership of their customers’ security outcomes, embracing transparency and accountability with their own security progress, and business leadership for integrating cybersecurity from the start of design decisions.

R-0010

<!-- q L264-265 "(For more information," .. "by Design Software.)" -->
> (For more information, see the joint guide Shifting the Balance of Cybersecurity Risk: Principles and Approaches for Secure by Design Software.)

(reference, informative; C-0049)

<!-- q L265-267 "Buyers should look" .. "(ISA) 62443 standards." -->
> Buyers should look for manufacturers that demonstrate their adoption of Secure by Design and International Society of Automation (ISA) 62443 standards.

R-0105 (split from R-0011)

<!-- q L267-268 "Manufacturers can demonstrate" .. "adopting these practices." -->
> Manufacturers can demonstrate their adoption of Secure by Design by publishing roadmaps that detail how they are adopting these practices.

R-0106 (split from R-0011)

<!-- q L269-270 "The following sections" .. "these considerations matter." -->
> The following sections provide buyers with guidance on questions to ask manufacturers, considerations for the OT context, and why these considerations matter.

(informative: the structure of the twelve sections, carried by role: and question_set:; C-0050)

<!-- q L270-273 "This guidance aligns" .. "and control systems." -->
> This guidance aligns with established cybersecurity standards, including National Institute of Standards and Technology (NIST) 800-213a for industrial internet of things or NIST 800-82 for OT and Security Level 3 of ISA/IEC 62443-4-2 and 62443-3-3 for cybersecurity features in industrial automation and control systems.

R-0210 (candidate C-0051)

<!-- q L273-274 "This guidance aligns" .. "Resilience Act (CRA)." -->
> This guidance aligns to technology-neutral and objective-oriented approaches contemplated by the Cyber Resilience Act (CRA).

R-0211 (candidate C-0051)

<!-- q L279-282 "ISA writes standards" .. "and development lifecycles." -->
> ISA writes standards for automation professionals to improve safety, security, and efficiency. The ISA/IEC 62443 multi-part standard is internationally recognized as defining requirements and processes for implementing and maintaining electronically secure OT products, systems, and development lifecycles.

(footnote 7, informative: ISA and the ISA/IEC 62443 series)

<!-- q L283-283 "NSA recommends maintainers" .. "profile in ISA." -->
> NSA recommends maintainers of National Security Systems (NSS) use the forthcoming OT NSS profile in ISA.

R-0212 (footnote 8)

<!-- q L285-287 "The EU’s CRA" .. "of their products." -->
> The EU’s CRA lays down technology-neutral and objective-oriented essential requirements, which manufacturers are required to implement through concrete technical measures in light of the nature of their products.

R-0213 (candidate C-0052; footnote 9)

<!-- q L287-290 "The European Commission" .. "specific product categories." -->
> The European Commission intends to request the development of vertical (product-specific) standards by the European Standardisation Organisations. These standards aim to facilitate the compliance of manufacturers by proposing concrete technical solutions for specific product categories.

(footnote 9, informative: product-specific standards to come)

## Configuration Management

### Selection criteria

<!-- q L300-301 "Products support controlling" .. "and engineering logic." -->
> Products support controlling and tracking modifications to configuration settings and engineering logic.

R-0214 (criterion)

### Questions to ask

<!-- q L302-303 "Does the product" .. "and engineering logic?" -->
> Does the product enable authenticated backup recording and deployment for configuration settings and engineering logic?

R-0215 (question)

<!-- q L303-303 "Does the product" .. "prevention or detection?" -->
> Does the product have tamper prevention or detection?

R-0216 (question)

<!-- q L303-305 "Does the manufacturer" .. "products or services?" -->
> Does the manufacturer provide custom processes and response plans for interruptions involving their products or services?

R-0217 (question)

### Why this matters

<!-- q L306-309 "Without strong configuration" .. "a product failure." -->
> Without strong configuration management, it is difficult to validate changes to infrastructure. Asset owners and operators need this validation to detect and prevent a threat actor from establishing persistence on OT devices. Recording and protecting backups of OT products is necessary for an operator to recover quickly and independently after a product failure.

(rationale, informative)

### Goal

<!-- q L311-313 -->
> The goal of this consideration is to help ensure OT owners and operators can swiftly identify unauthorized configuration changes and recover critical infrastructure after an incident occurs to minimize societal impact and downtime.

R-0012 (goal)

### Provisions

<!-- q L314-315 "Owners and operators" .. "the OT network." -->
> Owners and operators must be able to recover from incidents in which a threat actor establishes a foothold or wipes a component on the OT network.

R-0013

<!-- q L315-316 "Buyers should look" .. "offer the following:" -->
> Buyers should look for manufacturers who can offer the following:

R-0107 (split from R-0014)

<!-- q L317-317 "Alerts for known" .. "less secure configurations" -->
> Alerts for known insecure configurations or attempts to change to less secure configurations

R-0108 (item of R-0107; split from R-0014)

<!-- q L318-318 "The ability to" .. "restrict configuration changes" -->
> The ability to authorize or restrict configuration changes

R-0109 (item of R-0107; split from R-0014)

<!-- q L319-319 "The ability to" .. "support asset management" -->
> The ability to uniquely identify an OT device to support asset management

R-0110 (item of R-0107; split from R-0014)

<!-- q L320-320 "Open standards for" .. "for backup files" -->
> Open standards for backup files

R-0111 (item of R-0107; split from R-0014)

<!-- q L321-322 "Documented interfaces for" .. "over the network." -->
> Documented interfaces for creating backups and restoring from backups in person or over the network.

R-0112 (item of R-0107; split from R-0014)

<!-- q L323-324 "As OT software" .. "very little downtime." -->
> As OT software manufacturers adopt best practices, buyers should seek out resilient products that can rapidly recover and update themselves with very little downtime.

R-0015

<!-- q L325-327 "For more on" .. "the “Ownership” consideration." -->
> For more on how manufacturers can support resilience with their business practices, see the “Ownership” consideration.

R-0016

### Informative

<!-- q L324-325 "For example, immutable" .. "by hot-swapping containers." -->
> For example, immutable containers would allow operators to make configuration changes with minimal downtime by hot-swapping containers.

(example, informative)

## Logging in the Baseline Product

### Selection criteria

<!-- q L338-339 "The baseline product" .. "standard logging formats." -->
> The baseline product version supports security and safety logging of all actions using open standard logging formats.

R-0218 (criterion)

### Questions to ask

<!-- q L340-340 "Does the product" .. "to the product?" -->
> Does the product log, restarts, logins, or changes to the product?

R-0219 (question)

<!-- q L340-341 "Does the product provide" .. "prevent process failure?" -->
> Does the product provide telemetry and logs that help predict and prevent process failure?

R-0220 (question)

<!-- q L341-342 "Does the product" .. "events by default?" -->
> Does the product log security events and safety events by default?

R-0221 (question)

### Why this matters

<!-- q L343-343 "Logging will help" .. "into OT networks." -->
> Logging will help OT network defenders gather evidence of intrusions into OT networks.

(rationale, informative)

### Goal

<!-- q L345-346 "The goal of" .. "throughout product lines." -->
> The goal of this consideration is to include logging in baseline OT products to preserve evidence of an intrusion throughout product lines.

R-0222 (goal)

### Provisions

<!-- q L346-346 "Logging should not" .. "or paid feature." -->
> Logging should not be an add-on or paid feature.

R-0017

<!-- q L351-352 -->
> Even in scenarios where the logs cannot safely be aggregated over the network into a security tool, OT products with local logging already enabled through their default function will support incident responders.

R-0018

<!-- q L353-353 "Buyers should seek" .. "enabled by default" -->
> Buyers should seek products with a minimum set of logs enabled by default

R-0113 (split from R-0019)

<!-- q L353-354 "which should be" .. "products and manufacturers" -->
> which should be standardized across products and manufacturers

R-0114 (split from R-0019)

<!-- q L354-354 "Log types that" .. "look for include:" -->
> Log types that buyers should look for include:

R-0115 (split from R-0020)

<!-- q L355-355 "Open standard formats." .. "Open standard formats." -->
> Open standard formats.

R-0116 (item of R-0115; split from R-0020)

<!-- q L356-356 "Authentication events, both" .. "successful and unsuccessful." -->
> Authentication events, both successful and unsuccessful.

R-0117 (item of R-0115; split from R-0020)

<!-- q L357-357 "Deletion or modification" .. "modification of logs." -->
> Deletion or modification of logs.

R-0118 (item of R-0115; split from R-0020)

<!-- q L358-359 "Changes to the" .. "change in configurations." -->
> Changes to the device, such as updated engineering logic, firmware updates, or a change in configurations.

R-0119 (item of R-0115; split from R-0020)

<!-- q L360-360 "Data events including" .. "update, and delete." -->
> Data events including create, read, update, and delete.

R-0120 (item of R-0115; split from R-0020)

<!-- q L361-361 "Error or exception" .. "or exception events." -->
> Error or exception events.

R-0121 (item of R-0115; split from R-0020)

<!-- q L362-363 "All event records" .. "and event description." -->
> All event records should include a timestamp, source address and port, affected account details, correlation identifier, and event description.

R-0021

<!-- q L363-365 "Buyers should then" .. "Threat Model section)." -->
> Buyers should then seek manufacturers that supplement minimum log types with information from the manufacturer’s written threat model (see the Threat Model section).

R-0022

<!-- q L366-368 "Without logs, cyber" .. "or incident responders." -->
> Without logs, cyber threat actors can establish persistence through configuration or logic changes, or degrade operational efficiency, without leaving a record of the action for the operator or incident responders.

R-0023

### Informative

<!-- q L368-369 "For further guidance" .. "and threat detection." -->
> For further guidance on OT logging, see the joint guide Best practices for event logging and threat detection.

(reference, informative)

## Open Standards

### Selection criteria

<!-- q L380-381 "The product uses" .. "configurations and logic." -->
> The product uses open standards to support secure functions, services, and migrating configurations and logic.

R-0223 (criterion)

### Questions to ask

<!-- q L382-383 "Does the product" .. "or adding products?" -->
> Does the product support open, interoperable standards to simplify replacing or adding products?

R-0224 (question)

<!-- q L383-384 "Is the manufacturer" .. "(e.g., ISA/IEC 62443)?" -->
> Is the manufacturer demonstrating their alignment to industry regulations or international standards (e.g., ISA/IEC 62443)?

R-0225 (question)

### Why this matters

<!-- q L385-386 "Open standards enable" .. "best product available." -->
> Open standards enable interoperability that allows buyers to pick the best product available.

(rationale, informative)

### Goal

<!-- q L388-389 "The goal of" .. "in OT environments." -->
> The goal of this consideration is to confirm buyers can switch between vendors and manufacturers as well as leverage advances in general security standards in OT environments.

R-0024 (goal)

### Provisions

<!-- q L396-396 "The lack interoperability" .. "lack interoperability may:" -->
> The lack interoperability may:

R-0122 (split from R-0025)

<!-- q L397-397 "Complicate asset management" .. "asset management governance" -->
> Complicate asset management governance

R-0123 (item of R-0122; split from R-0025)

<!-- q L398-398 "Require owners to" .. "adding new manufacturers" -->
> Require owners to buy additional hardware when adding new manufacturers

R-0124 (item of R-0122; split from R-0025)

<!-- q L399-399 "Impede safety by" .. "and security capabilities." -->
> Impede safety by introducing friction for acquiring the newest safety and security capabilities.

R-0125 (item of R-0122; split from R-0025)

<!-- q L405-405 -->
> Buyers should prioritize open standards when evaluating new features to avoid any risks of vendor lock-in.

R-0026

<!-- q L407-409 "When this occurs," .. "interoperability working groups." -->
> When this occurs, buyers should seek out manufacturers that actively support interoperability, such as those who publish parsers or participate in interoperability working groups.

R-0027

### Informative

<!-- q L402-404 "These standards might" .. "from cross-vendor communication." -->
> These standards might apply to logging formats (sysmon), networking protocols (OPC-UA), programming languages (IEEE 61131-3), encryption protocols (TLS), or any element of a device that would benefit from cross-vendor communication.

(examples, informative; two are wrong (SD-4, SD-5))

## Ownership

### Selection criteria

<!-- q L420-421 "The product gives" .. "maintenance and changes." -->
> The product gives owners and operators full autonomy over the product, including maintenance and changes.

R-0226 (criterion)

### Questions to ask

<!-- q L422-423 "Does the product" .. "on the vendor?" -->
> Does the product enable OT operators to do what is needed without an onward dependency on the vendor?

R-0227 (question)

<!-- q L423-424 "Does the manufacturer" .. "local engineering firms?" -->
> Does the manufacturer allow for support contracts with local engineering firms?

R-0228 (question)

<!-- q L424-425 "Does the warranty" .. "to the environment?" -->
> Does the warranty policy for the product allow for adding security software or products (e.g., firewalls, gateways, continuous monitoring, diodes) to the environment?

R-0229 (question)

### Why this matters

<!-- q L426-427 "Asset owners and" .. "for everyone involved." -->
> Asset owners and operators need to be in control of their dependencies to respond and recover quickly with clear roles and responsibilities for everyone involved.

(rationale, informative)

### Goal

<!-- q L429-430 -->
> The goal of this consideration is to enable operators to control and recover their systems without unintended or unnecessary dependencies.

R-0230 (goal)

### Provisions

<!-- q L431-432 "Buyers should seek" .. "services or products." -->
> Buyers should seek out vendors and manufacturers with explicit roles, responsibilities, and onward dependencies for their services or products.

R-0028

<!-- q L433-435 "This is only" .. "product but unnecessary." -->
> This is only an issue if the responsible party for a given system is unclear, the buyer’s dependency on the manufacturer is unintentional, or the buyer’s dependency on the manufacturer is required by the product but unnecessary.

R-0231 (candidate C-0054)

<!-- q L436-437 "Products that discourage" .. "and security issues." -->
> Products that discourage third-party or on-premises configuration and management may interfere in the timely remediation of safety and security issues.

R-0029

<!-- q L437-437 "These barriers may" .. "may manifest as:" -->
> These barriers may manifest as:

R-0126 (split from R-0030)

<!-- q L438-439 "Restriction of data" .. "the asset owner" -->
> Restriction of data to an ecosystem or partition owned by the manufacturer and inaccessible to the asset owner

R-0127 (item of R-0126; split from R-0030)

<!-- q L440-441 "A warranty policy" .. "for safety compliance" -->
> A warranty policy that limits an asset owner’s ability to perform an upgrade, a security examination, or vulnerability testing beyond the limitations necessary for safety compliance

R-0128 (item of R-0126; split from R-0030)

<!-- q L442-442 "A manufacturer selling" .. "an additional service." -->
> A manufacturer selling device security functionality as an additional service.

R-0129 (item of R-0126; split from R-0030)

<!-- q L443-445 "Given that modern" .. "barriers listed above." -->
> Given that modern process automation involves technically complex components and architectures integrated with third-party vendors or contractors for maintenance and monitoring, buyers should seek out products unrestricted by the barriers listed above.

R-0031

<!-- q L445-448 "To improve security" .. "back online safely." -->
> To improve security across critical infrastructure, buyers should seek manufacturers that equip end users with the tools and skills necessary to engage in a business continuity plan that involves maintaining system functionality, operating through a degraded state, and bringing critical components back online safely.

R-0032

<!-- q L448-450 "For guidance on" .. "risk management agency." -->
> For guidance on the recommended minimum system functionality to aim for, U.S. organizations should consult their appropriate sector risk management agency.

R-0033

## Protection of Data

### Selection criteria

<!-- q L461-462 "The product protects" .. "configurations and logic." -->
> The product protects the integrity and confidentiality of data, services, and functions, including configurations and logic.

R-0232 (criterion)

### Questions to ask

<!-- q L463-463 "Does the product" .. "data at rest?" -->
> Does the product encrypt data at rest?

R-0233 (question)

<!-- q L463-464 "Does the product have" .. "of its data?" -->
> Does the product have a way to verify the integrity of its data?

R-0234 (question)

<!-- q L464-464 "Does the product" .. "data to anyone?" -->
> Does the product share or sell its data to anyone?

R-0235 (question)

### Why this matters

<!-- q L465-466 "OT data rarely" .. "cause sustained harm." -->
> OT data rarely changes and is valuable for threat actors trying to understand a system. An understanding of operational data is often needed to bypass safety checks and cause sustained harm.

(rationale, informative)

### Goal

<!-- q L468-468 -->
> The goal of this consideration is to protect customer data and limit harm to operational environments.

R-0236 (goal)

### Provisions

<!-- q L469-469 "Buyers should seek" .. "of OT data." -->
> Buyers should seek out products that minimize access and sharing of OT data.

R-0034

<!-- q L471-472 "Look for manufacturers" .. "of this data." -->
> Look for manufacturers and vendors that can explain how they protect copies of this data.

R-0035

<!-- q L473-474 "Buyers should seek" .. "the OT network." -->
> Buyers should seek out manufacturers that rely on data pushed out of the OT network as necessary, rather than pulling data out of the OT network.

R-0036

<!-- q L476-477 "If two-way connections" .. "establish a connection." -->
> If two-way connections are required, buyers should seek out products that require an operator’s approval to establish a connection.

R-0037

### Informative

<!-- q L477-478 "Including this check" .. "of segmentation misconfigurations." -->
> Including this check in the product helps mitigate the impact of segmentation misconfigurations.

(informative: places the approval check of R-0037 in the product)

<!-- q L479-480 -->
> For more information on OT data protection see the joint guide Principles of operational technology cyber security.

(reference, informative)

## Secure by Default

### Selection criteria

<!-- q L483-484 "The product is" .. "users or administrators." -->
> The product is delivered secure out of the box, resilient against the most prevalent threats and vulnerabilities, without requiring additional configuration from users or administrators.

R-0237 (criterion)

### Questions to ask

<!-- q L485-485 "Has the manufacturer" .. "eliminate default passwords?" -->
> Has the manufacturer eliminated or is working to eliminate default passwords?

R-0238 (question)

<!-- q L485-487 "Does the product" .. "File Transfer Protocol])?" -->
> Does the product enable by default and use the secure, up-to-date, versions of protocols (e.g., Secure Shell [SSH], SFTP [SSH File Transfer Protocol])?

R-0239 (question)

<!-- q L487-488 "Are older insecure" .. "Transfer Protocol [TFTP])?" -->
> Are older insecure protocols disabled by default (i.e., SNMPv1/2, Telnet, Trivial File Transfer Protocol [TFTP])?

R-0240 (question)

### Why this matters

<!-- q L489-489 "Insecure default settings" .. "increase security costs." -->
> Insecure default settings expose asset owners to more risk and increase security costs.

(rationale, informative)

### Goal

<!-- q L491-492 "The goal of" .. "to the buyer." -->
> The goal of this consideration is to configure security into OT products such that protection against the most prevalent threats is included by default at no additional cost to the buyer.

R-0241 (goal; candidate C-0055)

### Provisions

<!-- q L495-495 -->
> The key aims to achieve a Secure by Design product are:

R-0242

<!-- q L496-496 "Making customer security" .. "a technical feature." -->
> Making customer security a core business requirement, not just a technical feature.

R-0243 (item of R-0242)

<!-- q L497-497 "Including default configurations" .. "against prevalent threats." -->
> Including default configurations that protect against prevalent threats.

R-0244 (item of R-0242)

<!-- q L506-506 "Eliminating default passwords." .. "Eliminating default passwords." -->
> Eliminating default passwords.

R-0130 (item of R-0242; split from R-0038)

<!-- q L507-507 "Introducing continuous friction" .. "the public-facing internet." -->
> Introducing continuous friction for connecting internal OT devices to the public-facing internet.

R-0131 (item of R-0242; split from R-0038)

<!-- q L508-508 "Ensuring security functionality" .. "no additional cost." -->
> Ensuring security functionality is available on the device at no additional cost.

R-0132 (item of R-0242; split from R-0038)

<!-- q L509-509 "Embedding secure deployment" .. "product by default" -->
> Embedding secure deployment guidance or hardening guides into the product by default

R-0133 (item of R-0242; split from R-0038)

<!-- q L509-510 "the guide should" .. "default configuration options." -->
> the guide should clearly state security risks introduced by operators changing default configuration options.

R-0134 (item of R-0242; split from R-0038)

<!-- q L511-512 "Eliminating default passwords" .. "leveraging default passwords." -->
> Eliminating default passwords is especially important because nation-state affiliated groups and hacktivists have recently exploited devices by leveraging default passwords.

R-0245

<!-- q L515-517 "To remove this" .. "default password mistake." -->
> To remove this risk, buyers should seek products without default passwords for user login or embedded into the product’s firmware, removing the possibility of an operator or integrator making a default password mistake.

R-0039

<!-- q L517-518 "This is vital" .. "for remote access." -->
> This is vital for passwords for remote access.

R-0246

<!-- q L518-519 "For further guidance" .. "Eliminating Default Passwords." -->
> For further guidance on eliminating default passwords, see CISA’s Secure by Design Alert: How Manufacturers Can Protect Customers by Eliminating Default Passwords.

R-0040

<!-- q L520-522 -->
> Additionally, buyers should seek manufacturers that document the level of security included in their products, with the most secure default configuration preset removing the burden of hardening from operators.

R-0041

<!-- q L523-524 "Buyers should also" .. "gradual security improvements." -->
> Buyers should also ask for security implementations that work with their existing operator workflows and allow for gradual security improvements.

R-0042

<!-- q L525-527 "However, this compatibility" .. "can communicate seamlessly." -->
> However, this compatibility often requires that security features in new devices are not enabled by default to help ensure the legacy components can communicate seamlessly.

R-0043

<!-- q L527-528 "This can be" .. "old insecure services." -->
> This can be seen in lengthy secure deployment guidance that details how to turn off old insecure services.

R-0044

<!-- q L529-531 "Buyers should seek" .. "downgrades when necessary." -->
> Buyers should seek manufacturers that develop backwards compatibility operating models that prioritize security features with negotiated downgrades when necessary.

R-0045

<!-- q L536-538 "Buyers should look" .. "enabled by default." -->
> Buyers should look for manufacturers that are performing voice of customer research to embed cybersecurity within existing workflows and deploy functional products with security enabled by default.

R-0046

### Informative

<!-- q L533-535 "For example, instead" .. "securely by default." -->
> For example, instead of replacing all the devices in a portion of the system at once, an owner/operator could deploy a newer secure device with an embedded protocol gateway that translates it to observed legacy devices while still communicating securely by default.

(example, informative)

<!-- q L539-541 -->
> For more information on Secure by Design, see the joint guide Shifting the Balance of Cybersecurity Risk: Principles and Approaches for Secure by Design Software. This guide urges manufacturers to make it harder, or even impossible, for the operator or integrator to make a cybersecurity mistake.

(reference, informative)

## Secure Communications

### Selection criteria

<!-- q L552-553 "Products should support" .. "processes to continue." -->
> Products should support authenticated communication with device certificates deployed that fails loudly but that allows critical processes to continue.

R-0135 (criterion; split from R-0047)

### Questions to ask (printed as Key considerations, SD-1)

<!-- q L554-554 "Does the product" .. "certificates for devices?" -->
> Does the product simplify the deployment and renewal of certificates for devices?

R-0247 (question)

<!-- q L555-556 -->
> Does the manufacturer need asset owners and operators to be cyber experts to sustain secure communication?

R-0248 (question)

### Why this matters

<!-- q L557-558 "Secure communication is" .. "controlling critical infrastructure." -->
> Secure communication is necessary to validate the integrity and authenticity of the messages controlling critical infrastructure.

(rationale, informative)

### Goal

<!-- q L560-561 -->
> The goal of this consideration is to improve the usability and uptake of secure machine-to-machine communications in OT networks.

R-0249 (goal)

### Provisions

<!-- q L562-564 "Without authentication, cyber" .. "across the network" -->
> Without authentication, cyber threat actors can impersonate any device and send safety-impacting commands across the network

R-0136 (split from R-0048)

<!-- q L564-564 "without encryption, cyber" .. "sensitive network traffic." -->
> without encryption, cyber threat actors can read sensitive network traffic.

R-0137 (split from R-0048)

<!-- q L571-572 "That is not" .. "can make mistakes." -->
> That is not a risk many critical infrastructure owners and operators are willing to take when even mature IT organizations can make mistakes.

R-0049

<!-- q L572-574 "However, critical infrastructure" .. "which requires authentication." -->
> However, critical infrastructure owners and operators must be able to verify the integrity of their system, which requires authentication.

R-0050

<!-- q L574-575 "Much like the" .. "data in transit." -->
> Much like the needed progression to open standards, as critical infrastructure sectors mature, there should be a move towards more ubiquitous authentication and integrity for data in transit.

R-0051

<!-- q L576-577 -->
> Moreover, as secure communication capabilities mature, buyers should ask for products that support cryptographic agility to allow system upgrades if a product’s cryptography becomes vulnerable.

R-0052

<!-- q L579-580 "Buyers should mandate" .. "be cyber experts." -->
> Buyers should mandate that secure communication solutions are easy for operators or integrators to deploy securely, resistant to operator error, and do not require operators to be cyber experts.

R-0053

<!-- q L580-583 "As certificate management" .. "not prevent communication." -->
> As certificate management is not common in OT environments, operators may consider the equivalent of a TLS sign-only (unencrypted but still signed with a private key) or opportunistic TLS mode as an interim safety solution, where an expired certificate will generate logs but not prevent communication.

R-0054

<!-- q L586-587 -->
> Buyers should seek manufacturers that understand common operator workflows and embed secure communications into those workflows.

R-0055

## Secure Controls

### Selection criteria

<!-- q L598-599 "The product assumes" .. "or diagnostic commands." -->
> The product assumes a threat actor is operating on the network and protects itself against malicious emergency, safety, or diagnostic commands.

R-0250 (criterion; candidate C-0059)

### Questions to ask

<!-- q L600-601 "Does the product" .. "to/from critical components?" -->
> Does the product have a method to establish trust for commands to/from critical components?

R-0251 (question)

<!-- q L601-601 "Does the product" .. "known safety concerns?" -->
> Does the product prevent or ignore commands if they create known safety concerns?

R-0252 (question; candidate C-0060)

<!-- q L601-603 "Does the product behave" .. "during active operations?" -->
> Does the product behave differently if commands meant for maintenance periods are sent during active operations?

R-0253 (question)

<!-- q L603-603 "Can the product" .. "standard or specification?" -->
> Can the product alert on breaks from a standard or specification?

R-0056 (question)

<!-- q L603-604 "Can the product remain" .. "asset inventory tools?" -->
> Can the product remain stable during security scans, such as vulnerability assessments or asset inventory tools?

R-0057 (question)

### Why this matters

<!-- q L605-606 "OT environments need" .. "and valuable targets." -->
> OT environments need safety systems and processes to keep people safe. Without security checks, safety systems are easy and valuable targets.

(rationale, informative)

### Goal

<!-- q L608-610 "The goal of" .. "standard or specification." -->
> The goal of this consideration is to improve the resilience of OT systems by encouraging components that do not inherently trust the entire network or trust that all components are acting according to the rules of a standard or specification.

R-0254 (goal; candidate C-0061)

### Provisions

<!-- q L610-610 "Components should assume" .. "on the network." -->
> Components should assume threat actors are on the network.

R-0058

<!-- q L615-616 "A threat actor" .. "against the system." -->
> A threat actor can recreate those conditions or send a command to weaponize safety features against the system.

R-0059

<!-- q L616-618 "Products must mitigate" .. "to do harm." -->
> Products must mitigate the risks from a threat actor compromising a trusted device or intentionally violating a standard to do harm.

R-0060

<!-- q L619-619 "Buyers should ask" .. "use of commands." -->
> Buyers should ask for products that are designed to withstand the malicious use of commands.

R-0061

<!-- q L624-625 "For average components," .. "safety or security." -->
> For average components, this could mean documenting how the component responds to conditions impacting safety or security.

R-0255

<!-- q L628-629 "Identifying illegitimate behavior" .. "a primary controller." -->
> Identifying illegitimate behavior is particularly important for roots of trust, such as a primary controller.

R-0256

<!-- q L629-630 "Components do not" .. "log anomalous behavior." -->
> Components do not need to merely log anomalous behavior.

R-0257 (candidate C-0064)

<!-- q L630-632 "If the intended" .. "the anomalous behavior." -->
> If the intended system architecture or specification is broken or does not follow the operational context, then a component may be able to ignore or respond to the anomalous behavior.

R-0062

<!-- q L645-645 "Buyers should look" .. "through security scans." -->
> Buyers should look for products that are designed to operate through security scans.

R-0063

<!-- q L648-649 "Moreover, buyers should" .. "the design process." -->
> Moreover, buyers should seek out manufacturers that considered the security of unauthorized commands throughout the design process.

R-0064

<!-- q L649-651 "Asset owners and" .. "and design process." -->
> Asset owners and operators should consider consulting the Department of Energy’s Cyber-Informed Engineering Implementation Guidance to incorporate cybersecurity decisions into their engineering and design process.

R-0065

### Informative

<!-- q L632-635 "Examples of system" .. "updates mid process." -->
> Examples of system specifications being broken include: a singular Modbus client or bus controller being impersonated, network arbitration designed to disable an existing system such as a new engine appearing while a vehicle is in operation, or maintenance commands and updates mid process.

(examples, informative: the test conditions of R-0324 (inferred))

## Strong Authentication

### Selection criteria

<!-- q L654-655 "The baseline version" .. "to safety-critical equipment." -->
> The baseline version of the product supports role-based access control (RBAC) and multifactor authentication (MFA), particularly for changes to safety-critical equipment.

R-0258 (criterion)

### Questions to ask

<!-- q L656-657 "Has the manufacturer" .. "in their products?" -->
> Has the manufacturer eliminated or is working to eliminate the use of shared role-based passwords in their products?

R-0259 (question)

<!-- q L657-657 "Is MFA included" .. "the baseline version?" -->
> Is MFA included in the baseline version?

R-0260 (question)

### Why this matters

<!-- q L658-659 "Strong authentication allows" .. "management best practices." -->
> Strong authentication allows for defense-in-depth and enables identity and access management best practices.

(rationale, informative)

### Goal

<!-- q L661-662 "The goal of" .. "management best practices." -->
> The goal of this consideration is to use human-to-machine authentication mechanisms that are sufficient to support modern identity and access management best practices.

R-0261 (goal)

### Provisions

<!-- q L662-663 "This consideration is" .. "of strong authentication:" -->
> This consideration is focused on two elements of strong authentication:

R-0262

<!-- q L664-664 "RBAC and/or attribute-based" .. "access control (ABAC)" -->
> RBAC and/or attribute-based access control (ABAC)

R-0263 (item of R-0262; candidate C-0065)

<!-- q L665-665 "Phishing-resistant MFA" .. "Phishing-resistant MFA" -->
> Phishing-resistant MFA

R-0138 (item of R-0262; split from R-0066)

<!-- q L666-666 "Buyers should seek" .. "on common accounts." -->
> Buyers should seek products with RBAC and ABAC rather than relying on common accounts.

R-0139 (split from R-0066)

<!-- q L666-668 "RBAC and ABAC," .. "to authorized individuals." -->
> RBAC and ABAC, or a control that can restrict users to viewing information versus the ability to change information, is key for limiting the ability to make network changes to authorized individuals.

R-0067

<!-- q L671-671 "Buyers should look" .. "the baseline version." -->
> Buyers should look for products with phishing-resistant MFA included in the baseline version.

R-0068

<!-- q L673-674 "Phishing-resistant MFA is" .. "an OT environment." -->
> Phishing-resistant MFA is a key security control for limiting the damage a threat actor can do in an OT environment.

R-0069

<!-- q L683-692 "However, segmentation is" .. "layer of protection." -->
> However, segmentation is difficult to maintain, and critical components warrant that additional layer of protection.

R-0264 (candidate C-0074)

<!-- q L693-694 "An organization of" .. "prevent safety impacts." -->
> An organization of any size may want assurance that even if a single control (segmentation) fails, that there is a backup security control to prevent safety impacts.

R-0070

<!-- q L695-696 "Not every tiny" .. "the near term" -->
> Not every tiny sensor or cheap component necessarily needs to support MFA in the near term

R-0140 (split from R-0071)

<!-- q L696-698 "baseline versions of" .. "workstations, SCADA, HMI)." -->
> baseline versions of industrial automation control systems should support MFA from supervisory control (e.g., engineering workstations, SCADA, HMI).

R-0141 (split from R-0071)

## Threat Modeling

### Selection criteria

<!-- q L701-701 "The product has" .. "detailed threat model." -->
> The product has a full and detailed threat model.

R-0265 (criterion)

### Questions to ask

<!-- q L702-703 "Can the manufacturer" .. "designing their product?" -->
> Can the manufacturer articulate the attack vectors they have considered when designing their product?

R-0142 (question; split from R-0072)

<!-- q L703-703 "What security measures" .. "these threat scenarios?" -->
> What security measures does the product implement to reduce these threat scenarios?

R-0266 (question)

<!-- q L704-704 -->
> Does the manufacturer have a roadmap to address gaps in their threat model?

R-0267 (question)

### Why this matters

<!-- q L705-706 "Threat models are" .. "their security controls." -->
> Threat models are necessary for asset owners to understand the risk from a product and prioritize their security controls.

(rationale, informative)

### Goal

<!-- q L708-709 "The goal of" .. "in a product." -->
> The goal of this consideration is to give buyers the opportunity to make informed choices when evaluating the security mitigations in a product.

R-0268 (goal)

### Provisions

<!-- q L713-714 "Buyers should seek" .. "threat actor capabilities." -->
> Buyers should seek out threat models that track and incorporate threat sources, such as MITRE EMB3D, so that threats are aligned with modern threat actor capabilities.

R-0073

<!-- q L717-718 "Buyers should avoid" .. "the OT network." -->
> Buyers should avoid products that rely entirely on a threat actor never accessing the OT network.

R-0074

<!-- q L720-722 "Buyers should search" .. "from malicious actors." -->
> Buyers should search for manufacturers that use threat modeling throughout the software development lifecycle to understand where and how security measures should be prioritized and implemented to protect their product from malicious actors.

R-0075

<!-- q L724-725 "Asset owners and" .. "their OT system." -->
> Asset owners and operators should partner with a manufacturer’s threat modelling capability to prioritize upgrades and patches that impact their OT system.

R-0076

<!-- q L725-726 "Additionally, threat models" .. "the following questions:" -->
> Additionally, threat models enable manufacturers and buyers to answer the following questions:

R-0269 (candidate C-0078)

<!-- q L727-728 "What security products" .. "protecting the product?" -->
> What security products (e.g., EDR, network monitoring, firewalls) or security controls and policies (segmentation, password policies) does the manufacturer assume are protecting the product?

R-0270 (threat model question; item of R-0269; candidate C-0078)

<!-- q L729-729 "What communication capabilities" .. "the product have?" -->
> What communication capabilities does the product have?

R-0271 (threat model question; item of R-0269; candidate C-0078)

<!-- q L729-730 "Does the product" .. "to the manufacturer?" -->
> Does the product ever communicate back to the manufacturer?

R-0143 (threat model question; item of R-0269; split from R-0077)

<!-- q L731-731 "What environment is" .. "be used securely?" -->
> What environment is the product intended for and how can it be used securely?

R-0144 (threat model question; item of R-0269; split from R-0077)

<!-- q L740-741 "How have they" .. "product is vulnerable?" -->
> How have they designed to protect against common classes of coding error and how might adversaries take advantage of common coding errors if the product is vulnerable?

R-0272 (threat model question; item of R-0269; candidate C-0079)

<!-- q L742-742 "How does the" .. "supply chain attacks?" -->
> How does the manufacturer protect against supply chain attacks?

R-0273 (threat model question; item of R-0269; candidate C-0079)

### Informative

<!-- q L709-710 "Threat modeling is" .. "and analyze risks." -->
> Threat modeling is a structured process designed to identify and analyze risks.

(definition, informative)

## Vulnerability Management

### Selection criteria

<!-- q L745-746 "Product manufacturers should" .. "the CVE Program." -->
> Product manufacturers should have mature vulnerability management processes based on the CVE Program.

R-0145 (criterion; split from R-0078)

<!-- q L746-747 "The processes help" .. "entire life cycle." -->
> The processes help ensure that vulnerabilities in their products are identified and remediated across the entire life cycle.

R-0274 (criterion; candidate C-0080)

<!-- q L747-750 "In addition, manufacturers" .. "in their products." -->
> In addition, manufacturers need effective communication channels with users and the wider public, enabling them not only to share and publicly disclose information about vulnerabilities and mitigations, but also to receive information about newly discovered security flaws in their products.

R-0275 (criterion; candidate C-0081)

### Questions to ask

<!-- q L751-751 "Has the manufacturer" .. "bill of materials?" -->
> Has the manufacturer drawn up a software bill of materials?

R-0276 (question)

<!-- q L751-753 "Does the manufacturer" .. "and the public?" -->
> Does the manufacturer have a track record of remediating vulnerabilities in a complete, accurate, and timely manner and is relevant information about vulnerabilities and remediation shared with users and the public?

R-0277 (question)

<!-- q L753-755 "Will security advisories" .. "Framework (CSAF) standard?" -->
> Will security advisories be automatically retrievable according to the Common Security Advisory Framework (CSAF) standard?

R-0278 (question)

<!-- q L755-755 "Does the manufacturer" .. "vulnerability disclosure policy?" -->
> Does the manufacturer have a coordinated vulnerability disclosure policy?

R-0279 (question)

<!-- q L755-757 "Does the manufacturer make" .. "9116 compliant security.txt?" -->
> Does the manufacturer make it easy to report security vulnerabilities by providing an RFC 9116 compliant security.txt?

R-0280 (question)

### Why this matters

<!-- q L758-761 "It is difficult" .. "secure development practices." -->
> It is difficult to design and develop products without any vulnerabilities given the complexity of modern operational technology, the possibility of human error, and supply chain risks. Transparency of vulnerability handling is necessary for buyers to make informed decisions and manufacturers to continuously improve their secure development practices.

(rationale, informative)

### Goal

<!-- q L763-763 "The goal of" .. "entire life cycle." -->
> The goal of this consideration is to keep OT secure across its entire life cycle.

R-0281 (goal)

### Provisions

<!-- q L764-765 "It is essential" .. "of such products." -->
> It is essential that operators can rely on mature vulnerability handling processes put in place by the manufacturers of such products.

R-0079

<!-- q L766-768 -->
> A mature vulnerability handling process is based on the CVE Program and established international standards, mainly ISO/IEC 29147 and ISO/IEC 30111, complies with all application legislation (such as the EU’s Cyber Resilience Act), and should contain at least the following elements:

R-0146 (split from R-0080)

<!-- q L769-771 "Complete, accurate, and" .. "and machine-readable format." -->
> Complete, accurate, and timely identification and documentation of vulnerabilities and components contained in operational technology, including a software bill of materials in a commonly used and machine-readable format.

R-0147 (item of R-0146; split from R-0080)

<!-- q L772-772 "Vulnerabilities should be" .. "to CVE Program." -->
> Vulnerabilities should be assigned an identifier (CVE number) and published to CVE Program.

R-0148 (item of R-0147; split from R-0081)

<!-- q L773-773 "Risk-based remediation of" .. "including security updates." -->
> Risk-based remediation of vulnerabilities without delay, including security updates.

R-0149 (item of R-0146; split from R-0081)

<!-- q L774-778 "Public disclosure of" .. "as security advisories." -->
> Public disclosure of information about available security updates, including an accurate description of the vulnerabilities, the root cause, the common weakness enumeration (CWE), information allowing users to identify the products affected, the impacts of the vulnerabilities, the severity, and clear and accessible information to help users to remediate the vulnerabilities as security advisories.

R-0150 (item of R-0146; split from R-0081)

<!-- q L788-788 "Security advisories provided" .. "retrievable, machine-processable format." -->
> Security advisories provided in an automatically retrievable, machine-processable format.

R-0282 (item of R-0146)

<!-- q L790-791 "Vendors can use" .. "security advisory information." -->
> Vendors can use CSAF standard to automate retrieval of security advisory information.

R-0082

<!-- q L792-792 -->
> o Note: Information in BSI TR-03191 may provide the basis for procurement requirements.

R-0083 (item of R-0282)

<!-- q L793-793 -->
> Please consult your legal advisor.

R-0283 (item of R-0282; candidate C-0083)

<!-- q L794-796 "Vulnerability Exploitability eXchange" .. "the CSAF standard." -->
> Vulnerability Exploitability eXchange (VEX) statements indicating the “not affected” or “under investigation” status for “celebrity vulnerabilities” (i.e., Log4Shell-type vulnerabilities) should follow the CSAF standard.

R-0151 (item of R-0282; split from R-0084)

<!-- q L797-799 "A policy on" .. "and the public." -->
> A policy on coordinated vulnerability disclosure setting out how the manufacturer intends to responsibly share information about discovered security vulnerabilities with affected parties and the public.

R-0152 (item of R-0146; split from R-0084)

<!-- q L800-801 "o Note: Entities" .. "(CVD) best practices." -->
> o Note: Entities should follow well known and established coordinated vulnerability disclosure (CVD) best practices.

R-0085 (item of R-0152)

<!-- q L802-804 "Measures to facilitate" .. "of discovered vulnerabilities." -->
> Measures to facilitate the sharing of information about potential vulnerabilities in operational technology as well as in third party components contained in such products, including by providing a contact address for the reporting of discovered vulnerabilities.

R-0284 (item of R-0146; candidate C-0084)

<!-- q L804-805 "This should also" .. "the manufacturer’s website." -->
> This should also be supplied according to RFC 9116 as a security.txt on the manufacturer’s website.

R-0153 (item of R-0284; split from R-0086)

<!-- q L806-806 "Mechanisms to securely" .. "promptly mitigate vulnerabilities." -->
> Mechanisms to securely distribute updates for products to fix or promptly mitigate vulnerabilities.

R-0154 (item of R-0146; split from R-0086)

<!-- q L807-807 "Dissemination of security" .. "updates without delay." -->
> Dissemination of security updates without delay.

R-0155 (item of R-0146; split from R-0086)

<!-- q L807-808 "Updates are accompanied" .. "to be taken." -->
> Updates are accompanied by advisory messages providing users with relevant information, including on potential action to be taken.

R-0285 (item of R-0146; candidate C-0085)

<!-- q L809-810 "Note: Entities that" .. "the CVE Program." -->
> Note: Entities that have mature vulnerability handling processes should consider becoming a CVE numbering authority (CNA) within the CVE Program.

R-0087

### Informative

<!-- q L801-801 "See CERT Coordination" .. "for more information." -->
> See CERT Coordination Center (CERT/CC)’s for more information.

(reference, informative; dangling possessive, SD-11)

<!-- q L810-811 "For more information," .. "CISA at cvd@cisa.dhs.gov." -->
> For more information, contact CISA at cvd@cisa.dhs.gov.

(pointer, informative; C-0086)

<!-- q L816-816 "https://vuls.cert.org/confluence/display/CVD" .. "https://vuls.cert.org/confluence/display/CVD" -->
> https://vuls.cert.org/confluence/display/CVD

(footnote 10, informative: the CERT/CC CVD page)

## Upgrade and Patch Tooling

### Selection criteria

<!-- q L827-828 "The product has" .. "no extra cost." -->
> The product has a well-documented and easy to follow process for patches and upgrades, and the manufacturer provides security patches at no extra cost.

R-0286 (criterion; split into R-0287, R-0288)

<!-- q L828-829 "This includes porting" .. "no longer supported." -->
> This includes porting supported software to new operating systems free of charge if the original operating system is no longer supported.

R-0289 (criterion)

### Questions to ask

<!-- q L830-831 "Does the product" .. "(e.g., golden images)?" -->
> Does the product employ resilient patching features to reduce the risk of downtime from a bad patch (e.g., golden images)?

R-0290 (question)

<!-- q L831-833 "Does the manufacturer" .. "overwrite existing configurations?" -->
> Does the manufacturer test patches and report the results to check for compatibility issues with software/firmware/binaries and help ensure the patches do not overwrite existing configurations?

R-0291 (question; candidate C-0087)

<!-- q L833-834 "Does the manufacturer" .. "system is end-of-life?" -->
> Does the manufacturer update software to modern operating systems if the operating system is end-of-life?

R-0292 (question)

<!-- q L834-834 "Does the manufacturer" .. "for their products?" -->
> Does the manufacturer publish end-of-life dates for their products?

R-0293 (question)

<!-- q L834-835 "Does the manufacturer allow" .. "update is authentic?" -->
> Does the manufacturer allow the buyer to verify an update is authentic?

R-0294 (question)

<!-- q L835-836 "Are patches made" .. "via secure channels?" -->
> Are patches made available free of charge and disseminated via secure channels?

R-0295 (question)

### Why this matters

<!-- q L837-838 "Patches are an" .. "a critical process." -->
> Patches are an excellent way to protect against known threats. Greater patch adoption in OT requires transparency, verifiability, and a confidence that patches will not break a critical process.

(rationale, informative)

### Goal

<!-- q L840-841 "The goal of" .. "confidence, and transparency." -->
> The goal of this consideration is to increase patch rates and reduce use of end-of-life software through increased patch availability, customer confidence, and transparency.

R-0296 (goal)

### Provisions

<!-- q L843-844 "For increased confidence," .. "techniques, and transparency." -->
> For increased confidence, buyers should seek manufacturers with resilient patching technologies, verification techniques, and transparency.

R-0088

<!-- q L844-845 "For resilience, find" .. "a faulty patch." -->
> For resilience, find manufacturers that develop and test patches in representative configurations to help address the risk of a faulty patch.

R-0297

<!-- q L845-846 "For example, a" .. "piece of software" -->
> For example, a patch may be incompatible with another piece of software

R-0156 (split from R-0089)

<!-- q L846-847 "a patch may" .. "or engineering logic." -->
> a patch may overwrite the asset owner’s configurations or engineering logic.

R-0157 (split from R-0089)

<!-- q L847-848 "Manufacturers can avoid" .. "replicates client environments." -->
> Manufacturers can avoid incompatibility by using a developer preview program for the software used by the operator or their own testing environment that replicates client environments.

R-0090

<!-- q L849-850 "Responsible manufacturers will" .. "considerations into account." -->
> Responsible manufacturers will test against common configurations and take environmental considerations into account.

R-0298

<!-- q L850-851 "Buyers should also" .. "or safe modes." -->
> Buyers should also ask about automatic recovery features to protect them from any patching issues, such as golden images or safe modes.

R-0091

<!-- q L852-852 "For verification, buyers" .. "of an update." -->
> For verification, buyers should be able to reliably determine the authenticity of an update.

R-0092

<!-- q L852-853 "The delivery mechanism" .. "help guarantee integrity." -->
> The delivery mechanism for that update needs to be over a secure channel to help guarantee integrity.

R-0299 (candidate C-0089)

<!-- q L853-855 "Buyers should ask" .. "updates are legitimate." -->
> Buyers should ask for the security controls the manufacturer uses to protect the update development, build, and delivery pipeline to help ensure their updates are legitimate.

R-0093

<!-- q L856-858 "For transparency, buyers" .. "for a product." -->
> For transparency, buyers should seek out manufacturers that release updates that provide users with relevant information (see Vulnerability Handling section), provide security updates free of charge, and are transparent about the length of the support period for a product.

R-0094

<!-- q L858-859 "This support period" .. "of the product" -->
> This support period should reflect the intended lifecycle of the product

R-0158 (split from R-0095)

<!-- q L859-860 "a pump intended" .. "centralized manufacturing use-case" -->
> a pump intended for remote areas may expect a greater period of support than a centralized manufacturing use-case

R-0159 (split from R-0095)

<!-- q L860-861 "During the support" .. "be made available." -->
> During the support period, a buyer can expect that security vulnerabilities in their products will be handled and security updates will be made available.

R-0096

<!-- q L861-862 "An organization may" .. "in the field." -->
> An organization may have hundreds or thousands of retired devices in the field.

R-0097

<!-- q L874-875 "Operators should verify" .. "the support agreement." -->
> Operators should verify that running software on modern operating systems does not needlessly invalidate the support agreement.

R-0098

<!-- q L875-876 "Without the planning" .. "product for years." -->
> Without the planning that transparency allows, an operator may have to maintain a high-risk product for years.

R-0099

## Resources

<!-- q L880-881 "Individual elements of" .. "sector or subsector." -->
> Individual elements of secure by design may be difficult to apply perfectly to the current processes of a sector or subsector.

R-0100

<!-- q L881-882 "For further guidance," .. "Agency or SecureByDesignOT@cisa.dhs.gov." -->
> For further guidance, reach out to the appropriate Sector Risk Management Agency or SecureByDesignOT@cisa.dhs.gov.

(pointer, informative)

<!-- q L882-884 "Additionally, CISA offers" .. "regional cybersecurity advisor." -->
> Additionally, CISA offers free products and services to help critical infrastructure owners and operators secure their current infrastructure. See our website for a full listing or contact a regional cybersecurity advisor.

(pointer, informative)

## Contact Information

Administrative reporting channels, outside product selection; each directive is an entry,
testable no.

<!-- q L887-888 -->
> U.S. organizations are encouraged to report suspicious or criminal activity related to information in this guide to:

R-0300

<!-- q L889-890 "CISA via CISA’s" .. "FBI field office." -->
> CISA via CISA’s 24/7 Operations Center (report@cisa.gov or 888-282-0870) or your local FBI field office.

R-0301 (item of R-0300)

<!-- q L890-893 "When available, please" .. "point of contact." -->
> When available, please include the following information regarding the incident: date, time, and location of the incident; type of activity; number of people affected; type of equipment used for the activity; the name of the submitting company or organization; and a designated point of contact.

R-0160 (item of R-0301; split from R-0101)

<!-- q L894-894 "For NSA cybersecurity" .. "inquiries, contact CybersecurityReports@nsa.gov." -->
> For NSA cybersecurity guidance inquiries, contact CybersecurityReports@nsa.gov.

R-0161 (item of R-0300; split from R-0101)

<!-- q L895-896 "State, local, tribal," .. "(SOC@cisecurity.org or 866-787-4722)." -->
> State, local, tribal, and territorial governments should report incidents to the MS-ISAC (SOC@cisecurity.org or 866-787-4722).

R-0162 (item of R-0300; split from R-0101)

<!-- q L897-898 -->
> Australian organizations visit cyber.gov.au or call 1300 292 371 (1300 CYBER 1) to report cybersecurity incidents and access alerts and advisories.

R-0302

<!-- q L899-899 -->
> Canadian organizations report incidents by emailing CCCS at contact@cyber.gc.ca.

R-0303

<!-- q L900-901 -->
> German organizations visit bsi.bund.de/EN/IT-Sicherheitsvorfall/it-sicherheitsvorfall_node.html to report cyber security incidents.

R-0304

<!-- q L902-903 -->
> Netherlands’ organizations visit ncsc.nl for advisories, and report incidents by emailing NCSC-NL at cert@ncsc.nl.

R-0305

<!-- q L904-904 -->
> New Zealand organizations report cyber security incidents to incidents@ncsc.govt.nz or call 04 498 7654.

R-0306

<!-- q L905-906 -->
> United Kingdom organizations report a significant cyber security incident: ncsc.gov.uk/report-an-incident (monitored 24 hours) or, for urgent assistance, call 03000 200 973.

R-0307

## Disclaimer

<!-- q L917-917 "The information in" .. "informational purposes only." -->
> The information in this report is being provided “as is” for informational purposes only.

R-0308 (candidate C-0090)

<!-- q L917-919 "CISA and its" .. "within this document." -->
> CISA and its co-sealers do not endorse any commercial entity, product, company, or service, including any entities, products, or services linked within this document.

(non-endorsement, informative; C-0091)

<!-- q L919-921 "Any reference to" .. "CISA and co-sealers." -->
> Any reference to specific commercial entities, products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply endorsement, recommendation, or favoring by CISA and co-sealers.

(non-endorsement, informative; C-0092)

<!-- q L922-923 "This document is" .. "and its co-sealers." -->
> This document is without prejudice to any type of legislation that is applicable in the jurisdictions of CISA and its co-sealers.

R-0309

<!-- q L923-924 "This document does" .. "of such legislation." -->
> This document does not bind CISA and its co-sealers and is not intended to provide guidance on the implementation of such legislation.

R-0310 (candidate C-0093)

The Acknowledgements (L926-929) name contributors and bind nothing.

## Inferred entries

In our words, not quotations; each `derived_from` lists its grounds by id.

- R-0311 — Disclaimer: every entry of this record
- R-0312 — Considerations for OT Product Selection: the decision on a product
- R-0313 — Considerations for OT Product Selection: the twelve elements
- R-0314 — Considerations for OT Product Selection: the order of assessment within a consideration
- R-0315 — Considerations for OT Product Selection: evidence of Secure by Design adoption
- R-0316 — Considerations for OT Product Selection: the edition under test
- R-0317 — Secure by Default: the state a Secure by Default test starts from
- R-0318 — Secure Communications: behaviour on certificate failure
- R-0319 — Secure by Default: protocols in the default configuration
- R-0320 — Logging in the Baseline Product: the log set beyond the minimum
- R-0321 — Upgrade and Patch Tooling: the support period
- R-0322 — Considerations for OT Product Selection: answers to the questions
- R-0323 — Secure Controls: the Secure Controls test premise
- R-0324 — Secure Controls: anomaly detection and response
- R-0325 — Secure Controls: documentation of component responses
- R-0326 — Upgrade and Patch Tooling: information accompanying an update
- R-0327 — Vulnerability Management: bills of materials
- R-0328 — Upgrade and Patch Tooling: the move to a supported operating system
- R-0329 — Strong Authentication: MFA
- R-0330 — Strong Authentication: access control

## Source defects

Found by this lane in the source itself (not in the rendering). Each quotation is the defective
span; the entry notes that rest on it name the SD.

### SD-1

<!-- q L554-554 "Key considerations:" .. "Key considerations:" -->
> Key considerations:

(SD-1)

Secure Communications prints its questions under a different run-in label from the other eleven considerations; they are the same kind of list and are entries with question_set questions to ask.

### SD-2

<!-- q L340-340 "Does the product" .. "to the product?" -->
> Does the product log, restarts, logins, or changes to the product?

(SD-2)

A stray comma after log turns the verb into the first item of the list; the question asks whether the product logs restarts, logins or changes.

### SD-3

<!-- q L396-396 "The lack interoperability" .. "lack interoperability may:" -->
> The lack interoperability may:

(SD-3)

The lead-in omits of.

### SD-4

<!-- q L403-403 "programming languages (IEEE" .. "languages (IEEE 61131-3)" -->
> programming languages (IEEE 61131-3)

(SD-4)

IEC 61131-3 is an IEC standard (programmable controller languages), not an IEEE one.

### SD-5

<!-- q L402-402 "logging formats (sysmon)" .. "logging formats (sysmon)" -->
> logging formats (sysmon)

(SD-5)

Sysmon is a Microsoft Sysinternals logging tool, a product rather than an open standard for logging formats; the example does not illustrate what it is offered for.

### SD-6

<!-- q L364-365 "(see the Threat" .. "Threat Model section)." -->
> (see the Threat Model section).

(SD-6)

The cross-reference names a Threat Model section; the section is titled Threat Modeling.

### SD-7

<!-- q L857-857 "(see Vulnerability Handling" .. "Vulnerability Handling section)" -->
> (see Vulnerability Handling section)

(SD-7)

The cross-reference names a Vulnerability Handling section; no section has that title, and Vulnerability Management is meant (its body speaks of a vulnerability handling process).

### SD-8

<!-- q L110-111 "digital certificates deployed" .. "that fail loudly" -->
> digital certificates deployed that fail loudly

(SD-8)

<!-- q L552-553 "device certificates deployed" .. "that fails loudly" -->
> device certificates deployed that fails loudly

(SD-8)

The two statements of the Secure Communications criterion disagree in grammar, so what fails loudly is ambiguous: the Summary’s verb agrees with the certificates, the criterion’s with the communication; both keep critical processes running. R-0318 (inferred) reads both as the failure of certificate-based communication.

### SD-9

<!-- q L569-569 "Another consideration risk" .. "risk for operators" -->
> Another consideration risk for operators

(SD-9)

The opening words are garbled: either another consideration or another risk is meant.

### SD-10

<!-- q L767-767 "complies with all" .. "all application legislation" -->
> complies with all application legislation

(SD-10)

Application legislation: applicable legislation is meant.

### SD-11

<!-- q L801-801 "See CERT Coordination" .. "for more information." -->
> See CERT Coordination Center (CERT/CC)’s for more information.

(SD-11)

A dangling possessive: the CERT/CC document referred to is not named; footnote 10 gives only a URL.

### SD-12

<!-- q L143-143 "the original operation" .. "original operation system" -->
> the original operation system

(SD-12)

Operation system: operating system is meant.

### SD-13

<!-- q L143-143 "is soon to" .. "no longer supported" -->
> is soon to be no longer supported

(SD-13)

<!-- q L829-829 "if the original" .. "no longer supported" -->
> if the original operating system is no longer supported

(SD-13)

The two statements of the operating-system trigger differ: the Summary moves before end of support, the criterion once support has ended. R-0328 (inferred) shows that meeting the Summary meets both.

### SD-14

<!-- q L106-107 "(e.g., SNMPv1/2, Telnet," .. "SSL, TLS 1.0/1.1)" -->
> (e.g., SNMPv1/2, Telnet, SSL, TLS 1.0/1.1)

(SD-14)

<!-- q L487-488 "(i.e., SNMPv1/2, Telnet," .. "Transfer Protocol [TFTP])" -->
> (i.e., SNMPv1/2, Telnet, Trivial File Transfer Protocol [TFTP])

(SD-14)

The two lists of insecure protocols differ, and the question introduces its list with i.e., as if complete, though the Summary names SSL and TLS 1.0/1.1, which it omits. R-0319 (inferred) takes the union as the smallest test set.

### SD-15

<!-- q L859-859 "(i.e., a pump" .. "for remote areas" -->
> (i.e., a pump intended for remote areas

(SD-15)

i.e. introduces an example; e.g. is meant.

### SD-16

<!-- q L654-655 "role-based access control" .. "multifactor authentication (MFA)" -->
> role-based access control (RBAC) and multifactor authentication (MFA)

(SD-16)

<!-- q L664-664 "RBAC and/or attribute-based" .. "access control (ABAC)" -->
> RBAC and/or attribute-based access control (ABAC)

(SD-16)

<!-- q L666-666 "products with RBAC" .. "ABAC rather than" -->
> products with RBAC and ABAC rather than

(SD-16)

Strong Authentication states its access-control and MFA asks three ways: the criterion names RBAC and MFA without phishing-resistant; the focus list names RBAC and/or ABAC and phishing-resistant MFA; the body asks for RBAC and ABAC. R-0329 and R-0330 (inferred) resolve them.

### SD-17

<!-- q L138-139 "hardware and software" .. "bill of materials" -->
> hardware and software bill of materials

(SD-17)

<!-- q L751-751 "Has the manufacturer" .. "bill of materials?" -->
> Has the manufacturer drawn up a software bill of materials?

(SD-17)

The Summary asks for hardware and software bills of materials; the Vulnerability Management consideration names only the software one, in its question and in its element list. R-0327 (inferred).

### SD-18

<!-- q L165-167 "placed on the" .. "conformity assessment procedures" -->
> placed on the Union market and that products have been subjected to legally required conformity assessment procedures

(SD-18)

Footnote 6 lacks a verb before its second that-clause: read as intended, the CE marking is required for such products and attests that they passed the conformity assessment the law requires.

### SD-19

<!-- q L137-138 "Each product has" .. "defined support period" -->
> Each product has a clearly defined support period

(SD-19)

The Summary places the support period under Vulnerability Management, whose own section never mentions it; the consideration that sets it out is Upgrade and Patch Tooling (L856-861).

## Rendering notes

Properties of the pinned `pdftotext -layout` rendering, not of the source:

- **RN-1** A footnote prints a blank line after its first line (L57, L63, L66, L71, L160, L166, L280, L286). The
  skeleton’s sentence reader breaks there: C-0003 welds footnote 3 to the start of footnote 4,
  C-0031 and C-0032, C-0033 and C-0034, and C-0052 are pieces of footnotes 5, 6 and 9. The
  entries cut each footnote sentence whole, across the blank line.
- **RN-2** Two-column layouts weld in a sentence read: the cover’s agency list (L12-19) and the
  list of the twelve titles (L253-258); the latter is quoted above cell by cell.
- **RN-3** A page break that falls after a full stop ends a list for the skeleton: the Secure by
  Default aims (L495-497 before the break, L506-510 after), the Vulnerability Management elements
  (L788 after the break, no cue, hunted), the threat model questions (L740-742 after the break).
- **RN-4** List bullets print as the private-use glyph U+F0A7 and sub-items as a letter o; list
  entries quote each item without them.
- **RN-5** Footnote numbers print inline in the sentence they mark (L34, L38, L42, L49, L152, L154,
  L267, L273, L274, L801); entries that end at such a number leave it out.
