---
schema: "library-distilled/v1"
id: omb-m-22-18-normative
record: omb-m-22-18
type: normative
updated: "2026-10-02"
reviewed_by: ""
---

# OMB M-22-18 (2022-09-14) — normative statements

Source: OMB M-22-18, 8 pp, sha256 85b119f5…c6c2. Every obligation, permission, scope rule and commitment, verbatim (whitespace re-flowed; footnote markers omitted where noted in requirements.yaml), in the memo's own outline. **Rescinded 2026-01-23 by M-26-05** — held for history and as the reference attestation regime.

## Introduction (p.1)

- **intro** (Introduction, p.1; *requirement*, verb "requires", actor: federal agency) — "This memorandum requires agencies to comply with the NIST Guidance and any subsequent updates."

## §I Scope

- **I-1** (§I Scope, p.2; *requirement*, verb "requires", actor: federal agency) — "this memorandum requires each Federal agency to comply with the NIST Guidance when using third-party software on the agency's information systems or otherwise affecting the agency's information."
- **I-2** (§I Scope, first bullet, p.2; *scope*, verb "apply", actor: federal agency) — "These requirements apply to agencies' use of software developed after the effective date of this memorandum, as well as agencies' use of existing software that is modified by major version changes (e.g., using a semantic versioning schema of Major.Minor.Patch, the software version number goes from 2.5 to 3.0) after the effective date of this memorandum."
- **I-3** (§I Scope, second bullet, p.2; *scope*, verb "do not apply", actor: federal agency) — "These requirements do not apply to agency-developed software, although agencies are expected to take appropriate steps to adopt and implement secure software development practices for agency-developed software."
- **I-4** (§I Scope, third bullet, p.2; *requirement*, verb "is responsible", actor: awarding agency) — "An agency awarding a contract that may be used by other agencies is responsible for implementing the requirements of this memorandum."

## §II Actions

- **II-0** (§II Actions, p.2; *requirement*, verb "must", actor: federal agency) — "Federal agencies must only use software provided by software producers who can attest to complying with the Government-specified secure software development practices, as described in the NIST Guidance."
- **II-0b** (§II Actions, p.3; *requirement*, verb "must", actor: agency CIO (with requiring offices and CAOs)) — "Agency Chief Information Officers (CIOs), in coordination with requiring offices and Chief Acquisition Officers (CAOs), must take the following steps to ensure software producers have implemented and will attest to conformity with secure software development practices."
- **II.1** (§II.1, p.3; *requirement*, verb "are required", actor: federal agency) — "Consistent with the NIST Guidance and by the timelines identified below, agencies are required to obtain a self-attestation from the software producer before using the software."
- **II.1.a-1** (§II.1.a, p.3; *definition*, verb "serves as", actor: software producer) — "A software producer's self-attestation serves as a "conformance statement" described by the NIST Guidance."
- **II.1.a-2** (§II.1.a, p.3; *requirement*, verb "must", actor: federal agency) — "The agency must obtain a self-attestation for all third-party software subject to the requirements of this memorandum used by the agency, including software renewals and major version changes."
- **II.1.a.i** (§II.1.a.i, p.3; *recommendation*, verb "should", actor: federal agency) — "Agencies should encourage software producers to be product inclusive so that the same attestation may be readily provided to all purchasing agencies."
- **II.1.a.ii-1** (§II.1.a.ii, p.3; *requirement*, verb "shall", actor: requesting agency (obliging the software producer)) — "If the software producer cannot attest to one or more practices from the NIST Guidance identified in the standard self-attestation form, the requesting agency shall require the software producer to identify those practices to which they cannot attest, document practices they have in place to mitigate those risks, and require a Plan of Action & Milestones (POA&M) to be developed."
- **II.1.a.ii-2** (§II.1.a.ii, p.3; *requirement*, verb "shall", actor: federal agency) — "The agency shall take appropriate steps to ensure that such documentation is not posted publicly, either by the vendor or by the agency itself."
- **II.1.a.ii-3** (§II.1.a.ii, p.3; *permission*, verb "may", actor: federal agency) — "If the software producer supplies that documentation and the agency finds it satisfactory, the agency may use the software despite the producer's inability to provide a complete self-attestation."
- **II.1.a.ii-4** (§II.1.a.ii, p.3; *prohibition*, verb "shall not", actor: software producer and federal agency) — "Documentation provided in lieu of a complete self-attestation, as described in the preceding paragraph, shall not be posted publicly by the vendor or the agency."
- **II.1.b** (§II.1.b, p.3; *requirement*, verb "shall", actor: federal agency) — "The agency shall retain the self-attestation document, unless the software producer posts it publicly and provides a link to the posting as part of its proposal response."
- **II.1.c** (§II.1.c, p.3; *requirement*, verb "must include", actor: software producer (attestation content)) — "An acceptable self-attestation must include the following minimum requirements:"
- **II.1.c.i** (§II.1.c.i, p.3; *requirement*, verb "must include", actor: software producer (attestation content)) — "The software producer's name;"
- **II.1.c.ii** (§II.1.c.ii, p.4; *requirement*, verb "must include", actor: software producer (attestation content)) — "A description of which product or products the statement refers to (preferably focused at the company or product line level and inclusive of all unclassified products sold to Federal agencies);"
- **II.1.c.iii** (§II.1.c.iii, p.4; *requirement*, verb "must include", actor: software producer (attestation content)) — "A statement attesting that the software producer follows secure development practices and tasks that are itemized in the standard self-attestation form;"
- **II.1.c.iv** (§II.1.c.iv, p.4; *permission*, verb "may", actor: federal agency) — "Self-attestation is the minimum level required; however, agencies may make risk-based determinations that a third-party assessment is required due to the criticality of the service or product that is being acquired, as defined in M-21-30."
- **II.1.d** (§II.1.d, p.4; *permission*, verb "shall be acceptable", actor: federal agency) — "A third-party assessment provided by either a certified FedRAMP Third Party Assessor Organization (3PAO) or one approved by the agency shall be acceptable in lieu of a software producer's self-attestation, including in the case of open source software or products incorporating open source software, provided the 3PAO uses the NIST Guidance as the assessment baseline."
- **II.1.e-1** (§II.1.e, p.4; *recommendation*, verb "are encouraged", actor: federal agency) — "Agencies are encouraged to use a standard self-attestation form, which will be made available to agencies."
- **II.1.e-2** (§II.1.e, p.4; *statement-of-intent*, verb "plans to", actor: FAR Council) — "The Federal Acquisition Regulatory (FAR) Council plans to propose rulemaking on the use of a uniform standard self-attestation form."
- **II.2** (§II.2, p.4; *permission*, verb "may", actor: federal agency) — "Agencies may obtain from software producers artifacts that demonstrate conformance to secure software development practices, as needed."
- **II.2.a-1** (§II.2.a, p.4; *permission*, verb "may", actor: federal agency) — "A Software Bill of Materials (SBOMs) may be required by the agency in solicitation requirements, based on the criticality of the software as defined in M-21-30, or as determined by the agency."
- **II.2.a-2** (§II.2.a, p.4; *requirement*, verb "shall", actor: federal agency) — "If required, the SBOM shall be retained by the agency, unless the software producer posts it publicly and provides a link to that posting to the agency."
- **II.2.b** (§II.2.b, p.4; *requirement*, verb "must", actor: software producer (SBOM format)) — "SBOMs must be generated in one of the data formats defined in the National Telecommunications and Information Administration (NTIA) report "The Minimum Elements for a Software Bill of Materials (SBOM)," or successor guidance as published by the Cybersecurity and Infrastructure Security Agency (CISA)."
- **II.2.c** (§II.2.c, p.4; *requirement*, verb "shall", actor: federal agency) — "Agencies shall consider reciprocity of SBOM and other artifacts from software producers that are maintained by other Federal agencies, based on direct applicability and currency of the artifacts."
- **II.2.d** (§II.2.d, p.5; *permission*, verb "may", actor: federal agency) — "Artifacts other than the SBOM (e.g., from the use of automated tools and processes which validate the integrity of the source code and check for known or potential vulnerabilities) may be required if the agency determines them necessary."
- **II.2.e** (§II.2.e, p.5; *permission*, verb "may", actor: federal agency) — "Evidence that the software producer participates in a Vulnerability Disclosure Program may be required by the agency."
- **II.2.f** (§II.2.f, p.5; *recommendation*, verb "are encouraged", actor: federal agency) — "Agencies are encouraged to notify potential vendors of requirements as early in the acquisition process as feasible, including leveraging pre-solicitation activities."
- **II-3** (§II (closing), p.5; *requirement*, verb "must", actor: federal agency) — "In order to ensure compliance and reduce risk, agencies must integrate the NIST Guidance into their software evaluation process as outlined in this memorandum and consistent with the timelines below."
- **II-4** (§II (closing), p.5; *requirement*, verb "must", actor: federal agency) — "As agencies develop requirements that include the use of new software, they must request confirmation that the software producer utilizes secure software development practices."
- **II-5** (§II (closing), p.5; *requirement*, verb "must", actor: federal agency) — "regardless of how the agency ensures compliance, the agency must ensure that the company implements and attests to the use of secure software development practices consistent with NIST Guidance, throughout the software development lifecycle."

## §III.A Agency Responsibility

- **III.A-0** (§III.A, p.5; *requirement*, verb "must", actor: federal agency) — "Agencies must incorporate the requirements of this memorandum, in accordance with the following:"
- **III.A.1** (§III.A.1, p.5; Appendix A; *requirement*, verb "shall", actor: federal agency) — "Within 90 days of the date of this memorandum, agencies shall inventory all software subject to the requirements of this memorandum, with a separate inventory for "critical software.""
- **III.A.2** (§III.A.2, p.5; Appendix A; *requirement*, verb "shall", actor: federal agency) — "Within 120 days of the date of this memorandum, agencies shall develop a consistent process to communicate relevant requirements in this memorandum to vendors, and ensure attestation letters not posted publicly by software providers are collected in one central agency system."
- **III.A.3** (§III.A.3, p.5; Appendix A; *requirement*, verb "shall", actor: federal agency) — "Agencies shall collect attestation letters not posted publicly by software providers for "critical software" subject to the requirements of this memorandum within 270 days after publication of this memorandum."
- **III.A.4** (§III.A.4, p.6; Appendix A; *requirement*, verb "shall", actor: federal agency) — "Agencies shall collect attestation letters not posted publicly by software providers for all software subject to the requirements of this memorandum within 365 days after publication of this memorandum."
- **III.A.5** (§III.A.5, p.6; Appendix A; *requirement*, verb "shall", actor: agency CIO (with requiring activities and CAOs)) — "Within 180 days of the date of this memorandum, agency CIOs, in coordination with agency requiring activities and agency CAOs, shall assess organizational training needs and develop training plans for the review and validation of full attestation documents and artifacts."
- **III.A.6-1** (§III.A.6, p.6; *permission*, verb "may", actor: federal agency) — "Agencies may request an extension for complying with the requirements of this memorandum."
- **III.A.6-2** (§III.A.6, p.6; *requirement*, verb "shall / must", actor: federal agency) — "The extension request shall be submitted to the Director of OMB and must be transmitted 30 days before any relevant deadline in this memorandum and accompanied by a plan for meeting the underlying requirements."
- **III.A.6-3** (§III.A.6, p.6; *commitment*, verb "will", actor: OMB) — "Specific instructions for submitting requests for extensions will be posted in MAX.gov at this URL: https://community.max.gov/x/LhtGJw."
- **III.A.7-1** (§III.A.7, p.6; *permission*, verb "may", actor: federal agency) — "Agencies may request a waiver—only in the case of exceptional circumstances and for a limited duration—for any specific requirement(s) of this memorandum."
- **III.A.7-2** (§III.A.7, p.6; *requirement*, verb "must", actor: federal agency) — "The waiver request must be submitted to the Director of OMB and must be transmitted 30 days before any relevant deadline in this memorandum and accompanied by a plan for mitigating any potential risks."
- **III.A.7-3** (§III.A.7, p.6; *statement-of-intent*, verb "will consider", actor: Director of OMB (with APNSA)) — "The Director of OMB, in consultation with the Assistant to the President and National Security Advisor (APNSA), will consider granting the request on a case-by-case basis."
- **III.A.7-4** (§III.A.7, p.6; *commitment*, verb "will", actor: OMB) — "Specific instructions for submitting requests for waivers will be posted in MAX at this URL: https://community.max.gov/x/LhtGJw."
- **III.A.8** (§III.A.8, p.6; *requirement*, verb "shall", actor: federal agency) — "In executing the activities required by this memorandum, agencies shall comply with laws governing the collection, use, and dissemination of information."

## §III.B OMB Responsibility

- **III.B.1** (§III.B.1, p.6; Appendix A; *commitment*, verb "will", actor: OMB) — "Within 90 days from the date of this memorandum, OMB will post specific instructions for submitting requests for waivers or extensions to the MAX.gov links identified above."
- **III.B.2** (§III.B.2, p.6; Appendix A; *commitment*, verb "will", actor: OMB (with CISA and GSA)) — "Within 180 days from the date of this memorandum, OMB, in consultation with CISA and the General Services Administration (GSA), will establish requirements for a centralized repository for software attestations and artifacts, with appropriate mechanisms for protection and sharing among Federal agencies."

## §III.C CISA Responsibility

- **III.C.1** (§III.C.1, p.7; Appendix A; *commitment*, verb "will", actor: CISA (with OMB)) — "Within 120 days from the date of this memorandum, CISA, in consultation with OMB, will establish a standard self-attestation "common form" for Paperwork Reduction Act (PRA) clearance that is suitable for use by multiple agencies."
- **III.C.2** (§III.C.2, p.7; Appendix A; *commitment*, verb "will", actor: CISA (with GSA and OMB)) — "Within 1 year from OMB's establishment of requirements, CISA, in consultation with GSA and OMB, will establish a program plan for a government-wide repository for software attestations and artifacts with appropriate mechanisms for information protection and sharing among Federal agencies."
- **III.C.3** (§III.C.3, p.7; Appendix A; *commitment*, verb "will", actor: CISA) — "Within 18 months from OMB's establishment of requirements, CISA will demonstrate an Initial Operating Capability (IOC) of the repository."
- **III.C.4** (§III.C.4, p.7; Appendix A; *commitment*, verb "will", actor: CISA) — "Within 24 months from OMB's establishment of requirements, CISA will evaluate requirements for the Full Operating Capability (FOC) of a Federal interagency software artifact repository through traditional OMB processes."
- **III.C.5** (§III.C.5, p.7; Appendix A; *commitment*, verb "will", actor: CISA) — "CISA will publish updated guidance on Software Bill of Materials (SBOM) for Federal agencies, as appropriate."

## §III.D NIST Responsibility

- **III.D** (§III.D, p.7; Appendix A; *commitment*, verb "(imperative)", actor: NIST) — "Update SSDF guidance as appropriate."

## §IV Policy Assistance

- **IV** (§IV Policy Assistance, p.7; *recommendation*, verb "should", actor: any party with questions) — "All questions or inquiries should be addressed to the OMB Office of the Federal Chief Information Officer (OFCIO) via email: ofcio@omb.eop.gov"

## Appendix A (verbatim table, p.8) — summary of all actions

| Requirement | Actions following publication | Responsible Body |
|---|---|---|
| Agencies shall inventory all software subject to the requirements of this memorandum. | Within 90 days | Agencies |
| Agency CIOs shall develop a consistent process to communicate relevant requirements in this memorandum to vendors, and ensure attestation letters are collected in one central agency system | Within 120 days | Agencies |
| Agencies shall collect attestation letters for "critical software" subject to the requirements of this memorandum | Within 270 days | Agencies |
| Agencies shall collect attestation letters for all software subject to the requirements of this memorandum | Within 365 days | Agencies |
| Agency CIOs shall assess training needs and develop training plans for the review and validation of software attestations and artifacts | Within 180 days | Agencies |
| OMB will post specific instructions for requesting waivers and extensions to identified MAX.gov sites. | Within 90 days | OMB |
| OMB will establish the requirements for a centralized repository for agency secure software attestations and artifacts | Within 180 Days | OMB |
| In consultation with GSA and OMB, CISA will establish a program plan for a Government-wide repository for software attestations and artifacts with appropriate mechanisms for information protection and sharing among Federal agencies | One year from the establishment of requirements | CISA |
| CISA will demonstrate IOC of the attestation and artifact repository | 18 months after establishment of requirements | CISA |
| CISA will evaluate requirements for the Full Operating Capability (FOC) of a Federal interagency software acquisition artifact repository through traditional OMB processes | 24 months after establishment of requirements | CISA |
| CISA will publish updated SBOM guidance | As appropriate | CISA |
| CISA will establish a self-attestation common form for PRA clearance, incorporating the minimum elements of NIST 800-218 as identified by OMB. | Within 120 days | CISA |
| NIST will update SSDF guidance. | As appropriate | NIST |

## Definitions carried by the memo (verbatim)

- (Intro, p.1) "The NIST Secure Software Development Framework (SSDF), SP 800-218, and the NIST Software Supply Chain Security Guidance (these two documents, taken together, are hereinafter referred to as "NIST Guidance") include a set of practices that create the foundation for developing secure software."
- (§I, p.2) "The term "software" for purposes of this memorandum includes firmware, operating systems, applications, and application services (e.g., cloud-based software), as well as products containing software."
- (fn 9) "The term "Federal agency" refers to an "agency" under the definition provided under 44 U.S.C. § 3502(1)."
- (fn 10) "Federal information systems carry the definition provided under 44 U.S.C. § 3502(8)."
- "critical software": defined by reference to OMB M-21-30 (fn 14).

