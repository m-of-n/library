---
schema: "library-distilled/v1"
id: omb-m-23-16-normative
record: omb-m-23-16
type: normative
updated: "2026-10-02"
reviewed_by: ""
---

# OMB M-23-16 (2023-06-09) — normative statements

Source: OMB M-23-16, 5 pp, sha256 f9f920e4…cfa5b. Every statement verbatim in the memo's own outline. Controls over M-22-18 where they conflict (intro-2). **Rescinded 2026-01-23 by M-26-05.**

## Introduction and Authorities

- **intro-1** (Introduction and Authorities, p.1; *restatement*, verb "must", actor: federal agency) — "Pursuant to M-22-18, agencies must only use software that is provided by software producers who can attest to complying with Government-specified minimum secure software development practices."
- **intro-2** (Introduction and Authorities, p.1; *precedence*, verb "is controlling", actor: n/a (document precedence)) — "To the extent any provision of this memorandum may be read to conflict with any provision of M-22-18, this memorandum is controlling."

## §A Extending Timeline for Collection of Attestations for Critical Software and Non-Critical Software

- **A-1** (§A, p.2; *restatement*, verb "requires", actor: federal agency) — "Consistent with EO 14028, M-22-18 requires each Federal agency to collect attestations from producers of software used by the agency if that software was developed after September 14, 2022, the effective date of M-22-18."
- **A-1b** (§A, p.2; *scope*, verb "are also required", actor: federal agency) — "Agencies are also required to collect attestations from producers of software developed prior to September 14, 2022, if that software is used by a Federal agency and either: (1) is modified by one or more major version changes after September 14, 2022, or (2) is a hosted service that deploys continuous updates."
- **A-def** (§A, p.2; *definition*, verb "includes", actor: n/a) — "For the purposes of M-22-18 and this memorandum, "software" includes firmware, operating systems, applications, and application services (e.g., cloud-based software), as well as products containing software."
- **A-2** (§A, p.2; Appendix A row 1; *requirement*, verb "must", actor: federal agency) — "Agencies must collect attestations for critical software subject to the requirements of M-22-18 and this memorandum no later than three months after the M-22-18 attestation common form released by the Cybersecurity and Infrastructure Security Agency (CISA) (hereinafter "common form") is approved by OMB under the Paperwork Reduction Act (PRA)."
- **A-3** (§A, p.2; Appendix A row 2; *requirement*, verb "must", actor: federal agency) — "Six months after the common form's PRA approval by OMB, agencies must collect attestations for all software subject to the requirements delineated in M-22-18, as amended by this memorandum."

## §B.1 Third Party Components

- **B.1-1** (§B.1, p.2; *requirement*, verb "must", actor: federal agency) — "Attestations must be collected from the producer of the software end product used by an agency because the producer of that end product is best positioned to ensure its security."
- **B.1-2** (§B.1, p.2; *definition*, verb "serves as", actor: software producer (end product)) — "An attestation provided by that producer to an agency serves as an affirmative statement that the producer follows the secure software development minimum requirements, as articulated in the common form."
- **B.1-3** (§B.1, p.2; *informative*, verb "should", actor: software producer) — "These minimum requirements include several best practices regarding how software producers should address and maintain the security of code."
- **B.1-4** (§B.1, p.2; *informative*, verb "(best practices)", actor: software producer) — "Best practices include: regularly logging, monitoring, and auditing trust relationships used for authorization and access among components within the develop and build environments; taking consistent and reasonable steps to document and minimize use of software products that create undue risk; maintaining provenance data for internal and third-party code; and maintaining trusted source code supply chains."
- **B.1-5** (§B.1, p.3; *exemption*, verb "are not required", actor: federal agency) — "Accordingly, agencies are not required to collect attestations from producers of third-party software components that are incorporated into the software end product used by the agency."
- **B.1-6** (§B.1, p.3; *definition*, verb "only qualifies", actor: n/a) — "A component, whether open-source or proprietary, only qualifies as a "third-party" component if it was developed by an entity other than the producer of the software end product into which it is incorporated."

## §B.2 Freely Obtained and Publicly Available Proprietary Software

- **B.2-1** (§B.2, p.3; *exemption*, verb "are not required", actor: federal agency) — "Agencies are not required to collect attestations from software producers for products that are proprietary but freely obtained and publicly available."
- **B.2-2** (§B.2, p.3; *exemption*, verb "is outside the scope", actor: federal agency) — "Open-source software freely and directly obtained by Federal agencies is outside the scope of NIST's guidance for agencies on software supply chain security."
- **B.2-3** (§B.2, p.3; *exemption*, verb "is also out of scope", actor: federal agency) — "This memorandum further clarifies that no-cost, publicly available proprietary software is also out of scope for M-22-18 attestation collection."
- **B.2-4** (§B.2, p.3; *requirement*, verb "are required", actor: federal agency) — "Agencies are, nevertheless, required to assess the risk in utilizing such software and take appropriate steps to minimize or eliminate identified risks."
- **B.2-5** (§B.2, p.3; *scope*, verb "remain subject", actor: federal agency) — "Though freely obtained, demonstrations or pilots of software products that are otherwise unavailable on a no-cost basis remain subject to M-22-18 attestation requirements, as amended."

## §B.3 Federal Contractor Developed Software

- **B.3-1** (§B.3, p.3; *exemption*, verb "remains out of scope", actor: federal agency) — "Agency-developed software remains out of scope for M-22-18 and any attestation collection requirements."
- **B.3-2** (§B.3, p.3; *scope*, verb "depends on", actor: federal agency (contracting)) — "Whether software developed under a Federal contract may constitute "[a]gency-developed software" for the purposes of M-22-18, as amended, depends on whether the contracting agency is able to ensure that secure software development practices are followed throughout the entire software development lifecycle (i.e., requirements, design, development, testing, deployment, and maintenance)."
- **B.3-3** (§B.3, p.3; *expectation*, verb "are expected", actor: federal agency) — "Agencies, in their development of software, are expected to appropriately leverage the NIST SSDF (SP 800-218)."
- **B.3-4** (§B.3, p.3; *requirement*, verb "are required", actor: agency CIO) — "If there are questions regarding whether software developed by Federal contractors should be considered agency-developed, agency CIOs are required to make that determination on behalf of the agency."
- **B.3-5** (§B.3, p.3; *scope*, verb "will remain subject", actor: federal agency) — "If an agency must, under M-22-18 and this memorandum, obtain an attestation before using a given software application, then that application will remain subject to the attestation requirement even if it is deployed, configured, or modified by a Federal contractor on behalf of an agency."

## §C Guidance on the Use of Plans of Action and Milestones Submitted to Federal Agencies by Software Producers

- **C-0** (§C, p.4; *restatement*, verb "may", actor: federal agency) — "M-22-18 provides that, if a software producer cannot attest to one or more practices identified in the attestation form, an agency may still use the software if the producer identifies the practices to which they cannot attest, documents practices they have in place to mitigate associated risks, and submits a satisfactory Plan of Action and Milestones (POA&M)."
- **C-1** (§C, p.4; *requirement*, verb "must", actor: software producer) — "First, the producer of a given software application must identify the practices to which they cannot attest, document practices they have in place to mitigate associated risks, and submit a POA&M to an agency."
- **C-2** (§C, p.4; *permission+requirement*, verb "may / must", actor: federal agency) — "If the agency finds the documentation satisfactory, it may continue using the software, but must concurrently seek an extension of the deadline for attestation from OMB."
- **C-3** (§C, p.4; *requirement*, verb "must include", actor: federal agency) — "Extension requests submitted to OMB must include a copy of the software producer's POA&M."
- **C-4** (§C, p.4; *requirement*, verb "must", actor: federal agency) — "The agency must discontinue use of the software if the agency finds the software producer's documentation unsatisfactory or if the agency is unable to confirm that the producer has identified the practices to which it cannot attest; documented practices they have in place to mitigate associated risk; and submitted a POA&M to the agency."
- **C-5** (§C, p.4; *requirement*, verb "must", actor: federal agency) — "Additionally, if the agency fails to submit an extension request, the POA&M is not considered valid, and the agency must discontinue use of the software."
- **C-6** (§C, p.4; *commitment*, verb "will prioritize", actor: OMB) — "In instances where multiple agencies are affected by a software producer's inability to attest to minimum requirements for one or more software products, OMB will prioritize consideration of agencies' extension requests for software product(s) that share a common POA&M."
- **C-7** (§C, p.4; *permission*, verb "may", actor: OMB) — "OMB may designate a lead agency to work with the software producer and all affected agencies."
- **C-8** (§C, p.4; *commitment*, verb "will", actor: lead agency) — "The lead agency will coordinate common updates, communication, and oversight of progress with impacted agencies."
- **C-9** (§C, p.4; *permission*, verb "may", actor: non-lead federal agencies) — "Agencies other than the OMB-designated lead agency may continue working with the software producer to ensure progress towards attestation."
- **C-10** (§C, p.4; *commitment*, verb "will", actor: OMB) — "Additional instructions on the format and process for extension and waiver requests will be provided on MAX.gov."
- **C-11** (§C, p.4; Appendix A row 3; *commitment*, verb "will", actor: OMB) — "No later than one year following the publication of this memorandum, OMB will begin to collect metrics on the number of products in use at each agency that do not meet the secure software minimum requirements."

## §D Future Updates to Guidance

- **D-1** (§D, p.4; *commitment*, verb "will", actor: OMB) — "Additional clarifications and general updates on implementation of M-22-18 and this memorandum will be posted on the appropriate MAX.gov or successor site."
- **D-2** (§D, p.4; *recommendation*, verb "should", actor: any party with questions) — "All questions or inquiries concerning this memorandum should be addressed to the OMB Office of the Federal Chief Information Officer (OFCIO) via email: ofcio@omb.eop.gov."

## Appendix A (verbatim table, p.5) — updated key dates

| Requirement | Actions following publication | Responsible Body |
|---|---|---|
| Agencies shall collect attestation letters for "critical software" subject to the requirements of M-22-18, as amended by this memorandum. | 3 months after OMB PRA approval of common form | Agencies |
| Agencies shall collect attestation letters for all software subject to the requirements of M-22-18, as amended by this memorandum. | 6 months after OMB PRA approval of common form | Agencies |
| OMB will begin to collect metrics on agency approval of POA&Ms, as well as the number of extensions and waivers in place at each agency. | Within 1 year of issuance of this memorandum | OMB |

## Definitions carried by the memo (verbatim, footnotes 4–5)

- "Component" is defined as: A software object, meant to interact with other components, encapsulating certain functionality or a set of functionalities. A component has a clearly defined interface and conforms to a prescribed behavior common to all components within an architecture. See NIST SP 800-95, Guide to Secure Web Services.
- Open-source software is "software that can be accessed, used, modified, and shared by anyone." See NIST, Open Source Code (December 6, 2018).
- fn 6: "NIST SP 800-218: Secure Software Development Framework (SSDF) Version 1.1, February 2022. See, PO 1.3; PW 4.1; PW 4.4; PW 7.1, among others."

