---
schema: "library-distilled/v1"
id: cisa-ssdf-attestation-form-2024-normative
record: cisa-ssdf-attestation-form-2024
type: normative
updated: "2026-10-02"
reviewed_by: ""
---

# Secure Software Development Attestation Form (v1.0, OMB 1670-0052) — normative statements

Source: CISA 'Secure Software Development Attestation Form Instructions' PDF (10 pp, includes the form v1.0 on pp.5-7), sha256 a8d6b568…dacb. Every statement verbatim in source order by part. Since 2026-01-23 (OMB M-26-05) agency use of the form is optional.

## Instructions (pp.1–4)

- **INS-01** (Privacy Act Statement note, p.1; *recommendation*, verb "should", actor: agency using the common form) — "Each agency using this common form should provide Privacy Act Statements that conform to its applicable agency procedures and requirements."
- **INS-01b** (Privacy Act Statement note, p.1; *requirement*, verb "will need to", actor: agency using the common form) — "All agencies using this common form will need to provide an agency-unique Privacy Act Statement when they request to use this form."
- **INS-PA-1** (Privacy Act Statement — Background, p.1; *permission*, verb "may be disclosed", actor: collecting agency) — "This information may be disclosed as generally permitted under Executive Order 14028, Improving the Nation's Cybersecurity (E.O. 14028) and Memorandum M-22-18, "Enhancing the Security of the Software Supply Chain through Secure Software Development Practices" (M-22-18), as amended."
- **INS-PA-2** (Privacy Act Statement — Background, p.1; *permission*, verb "may be disclosed", actor: DHS) — "For DHS, information may be disclosed as necessary and authorized by the routine uses published in DHS/ALL-002 Department of Homeland Security (DHS) Mailing and Other List System, November 25, 2008, 73 FR 71659."
- **INS-02** (Privacy Act Statement, p.1; *consequence*, verb "may result", actor: software producer) — "Failure to provide any of the information requested may result in the agency no longer utilizing the software at issue."
- **INS-03** (Privacy Act Statement, p.1; *consequence*, verb "may constitute", actor: signatory (software producer)) — "Willfully providing false or misleading information may constitute a violation of 18 U.S.C. § 1001, a criminal statute."
- **INS-04** (What is the Purpose..., p.2; *restatement*, verb "may use ... only if", actor: federal agency) — "M-22-18, as amended by M-23-16, provides that a Federal agency may use software subject to M-22-18's requirements only if the producer of that software has first attested to compliance with Federal Government-specified secure software development practices drawn from the SSDF."
- **INS-05** (What is the Purpose..., p.2; *requirement*, verb "must meet, and attest to meeting", actor: software producer) — "This self-attestation form identifies the minimum secure software development requirements a software producer must meet, and attest to meeting, before software subject to the requirements of M-22-18 and M-23-16 may be used by Federal agencies."
- **INS-06** (What is the Purpose..., p.2-3; *scope*, verb "requires self-attestation", actor: software producer) — "Software requires self-attestation if any of the conditions is met:"
- **INS-06.1** (p.2, condition 1; *scope*, verb "(condition)", actor: software producer) — "The software was developed after September 14, 2022;"
- **INS-06.2** (p.2, condition 2; *scope*, verb "(condition)", actor: software producer) — "The software was developed prior to September 14, 2022, but was modified by major version changes (e.g., using a semantic versioning schema of Major.Minor.Patch, the software version number goes from 2.5 to 3.0) after September 14, 2022; or"
- **INS-06.3** (p.3, condition 3; *scope*, verb "(condition)", actor: software producer) — "The producer delivers continuous changes to the software code (as is the case for software-as-a-service products or other products using continuous delivery/continuous deployment)."
- **INS-07** (p.3; *exemption*, verb "are not in scope", actor: software producer / agency) — "Software products and components in the following categories are not in scope for M-22-18, as amended by M-23-16, and do not require a self-attestation:"
- **INS-08** (p.3; *requirement*, verb "are required to attest", actor: software producer) — "Software producers who utilize third party components in their software are required to attest that they have taken specific steps, detailed in "Section III – Attestation and Signature" of the common form, to minimize the risks of relying on such components in their products."
- **INS-09** (p.3; *permission*, verb "may", actor: agency) — "Agency-specific instructions may be provided to the software producer outside of this common form."
- **INS-10** (p.3; *permission+responsibility*, verb "may / are responsible", actor: agency; software producer) — "Conformance to agency-specific requirements may be included with this form as an addendum; agencies are responsible for fulfilling any Paperwork Reduction Act requirements applicable to agency-specific additions."
- **INS-11** (p.3; *permission*, verb "may", actor: software producer) — "If a software producer is unable to submit via the online form, they may email a pdf version of the form to the respective agency:"
- **INS-11b** (p.3; *commitment*, verb "will provide", actor: agency) — "Individual agencies will provide their respective email addresses."
- **INS-12** (Filling Out the Form, p.3; *requirement*, verb "are required", actor: software producer) — "All fields in the attestation form are required to be appropriately completed by the software producer."
- **INS-13** (Filling Out the Form, p.3; *requirement*, verb "will not be accepted", actor: agency (receiving)) — "Incomplete forms will not be accepted."
- **INS-14** (p.4; *requirement*, verb "must", actor: software producer (signatory)) — "The form must be signed by the Chief Executive Officer (CEO) of the software producer or their designee, who must be an employee of the software producer and have the authority to bind the corporation."
- **INS-15** (p.4; *definition*, verb "attests", actor: signatory) — "By signing, that individual attests that the software in question is developed in conformity with the secure software development practices delineated within this form."
- **INS-16** (p.4; *permission*, verb "may be used", actor: federal agency) — "The software may be used by a federal agency, consistent with the requirements of M-22-18, as amended by M-23-16, once the agency has received an appropriately signed copy of the attestation form."
- **INS-17** (p.4; *permission*, verb "may choose", actor: software producer) — "The software producer may choose to demonstrate conformance with the minimum requirements by submitting a third-party assessment documenting that conformance."
- **INS-18** (p.4; *requirement*, verb "must", actor: 3PAO) — "A third-party assessment must be performed by a Third Party Assessor Organization (3PAO) that has either been FedRAMP certified or approved in writing by an appropriate agency official."
- **INS-19** (p.4; *requirement*, verb "must", actor: 3PAO) — "The 3PAO must use relevant NIST Guidance that includes all elements outlined in this form as part of the assessment baseline."
- **INS-20** (p.4; *requirement*, verb "must", actor: software producer) — "To rely upon a third-party assessment, the software producer must check the appropriate box in Section III and attach the assessment to the form."
- **INS-21** (p.4; *permission*, verb "need not", actor: software producer) — "The producer need not sign the form in this instance."
- **INS-22** (p.4; *requirement*, verb "shall", actor: federal agency) — "The agency shall take appropriate steps to ensure that the assessment is not posted publicly, either by the vendor or by the agency itself."
- **INS-23** (Additional Information, p.4; *permission*, verb "may still decide", actor: federal agency) — "In the event that an agency cannot obtain a completed self-attestation from the software producer, an agency may still decide to use the producer's software if the producer identifies the practices to which they cannot attest, documents practices they have in place to mitigate associated risks, and submits a plan of actions and milestones (POA&M) to the agency."
- **INS-24** (Additional Information, p.4; *requirement*, verb "are responsible", actor: federal agency) — "When an attestation is not provided, per OMB guidance, agencies are responsible for requesting from OMB an extension or waiver for the continued use."
- **INS-25** (Additional Information, p.4; *statement*, verb "fulfills", actor: n/a) — "This common self-attestation form fulfills the minimum requirements set forth by OMB in M-22-18, as amended by M-23-16."
- **INS-26** (Additional Information, p.4; *statement*, verb "may be modified", actor: CISA) — "The attestation form, background, and instructions are subject to change and may be modified."

## Form Section I (p.5)

- **I-type** (Form Section I, p.5; *requirement*, verb "(check one)", actor: software producer) — "[ ] New Attestation [ ] Attestation Following Extension or Waiver [ ] Revised Attestation"
- **I-scope** (Form Section I, p.5; *requirement*, verb "(check one)", actor: software producer) — "Type of Attestation: [ ] Company-wide [ ] Individual Product [ ] Multiple Products or Specific Product Version(s) (please provide complete list)"
- **I-products** (Form Section I, p.5; *requirement*, verb "provide", actor: software producer) — "If this attestation is for an individual product or multiple products, provide the software name, version number, and release/publish date to which this attestation applies."
- **I-fn4** (Form Section I, footnote 4, p.5; *rule*, verb "are binding", actor: software producer) — "Attestations are binding for future versions of the named software product unless and until the software producer notifies the agencies to which it previously submitted the form that its development practices no longer conform to the required elements specified in the attestation."
- **I-excl** (Form Section I, p.5; *exemption*, verb "does not cover", actor: software producer) — "For the above specified software, this form does not cover software or any components of that software that fall into the following categories:"
- **I-note** (Form Section I note, p.5; *definition*, verb "are attesting", actor: software producer) — "Note: In signing this attestation, software producers are attesting to adhering to the secure software development practices outlined in Section III for code developed by the producer."

## Form Section II (pp.5–6)

- **II-contact** (Form Section II.2, p.6; *requirement*, verb "(provide)", actor: software producer) — "Primary Contact for this Document and Related Information (may be an individual, role, or group):"
- **II-email** (Form Section II.2, p.6; *permission*, verb "may be", actor: software producer) — "Email Address (may be an alias/distribution list):"

## Form Section III — Attestation and Signature (pp.6–7)

- **III-lead** (Form Section III, p.6; *attestation*, verb "attest", actor: signatory on behalf of software producer) — "On behalf of the above-specified company, I attest that, to the best of my knowledge, [software producer] presently makes consistent use of the following practices, derived from the secure software development framework (SSDF), in developing the software identified in Section I:"
- **III.1** (Form §III.1, p.6; Appendix row 1; *attestation*, verb "is developed and built", actor: software producer) — "The software is developed and built in secure environments. Those environments are secured by the following actions, at a minimum:"
- **III.1.a** (Form §III.1.a, p.6; Appendix; *attestation*, verb "separating and protecting", actor: software producer) — "Separating and protecting each environment involved in developing and building software;"
- **III.1.b** (Form §III.1.b, p.6; Appendix; *attestation*, verb "regularly logging, monitoring, and auditing", actor: software producer) — "Regularly logging, monitoring, and auditing trust relationships used for authorization and access:"
- **III.1.b.i** (Form §III.1.b.i, p.6; *attestation*, verb "(scope of 1.b)", actor: software producer) — "to any software development and build environments; and"
- **III.1.b.ii** (Form §III.1.b.ii, p.6; *attestation*, verb "(scope of 1.b)", actor: software producer) — "among components within each environment;"
- **III.1.c** (Form §III.1.c, p.6; Appendix; *attestation*, verb "enforcing", actor: software producer) — "Enforcing multi-factor authentication and conditional access across the environments relevant to developing and building software in a manner that minimizes security risk;"
- **III.1.d** (Form §III.1.d, p.6-7; Appendix; *attestation*, verb "taking consistent and reasonable steps", actor: software producer) — "Taking consistent and reasonable steps to document, as well as minimize use or inclusion of software products that create undue risk within the environments used to develop and build software;"
- **III.1.e** (Form §III.1.e, p.7; Appendix; *attestation*, verb "encrypting", actor: software producer) — "Encrypting sensitive data, such as credentials, to the extent practicable and based on risk;"
- **III.1.f** (Form §III.1.f, p.7; Appendix; *attestation*, verb "implementing", actor: software producer) — "Implementing defensive cybersecurity practices, including continuous monitoring of operations and alerts and, as necessary, responding to suspected and confirmed cyber incidents;"
- **III.2** (Form §III.2, p.7; Appendix; *attestation*, verb "makes a good-faith effort", actor: software producer) — "The software producer makes a good-faith effort to maintain trusted source code supply chains by employing automated tools or comparable processes to address the security of internal code and third-party components and manage related vulnerabilities;"
- **III.3** (Form §III.3, p.7; Appendix; *attestation*, verb "maintains provenance", actor: software producer) — "The software producer maintains provenance for internal code and third-party components incorporated into the software to the greatest extent feasible;"
- **III.4** (Form §III.4, p.7; Appendix; *attestation*, verb "employs", actor: software producer) — "The software producer employs automated tools or comparable processes that check for security vulnerabilities. In addition:"
- **III.4.a** (Form §III.4.a, p.7; *attestation*, verb "operates", actor: software producer) — "The software producer operates these processes on an ongoing basis and prior to product, version, or update releases;"
- **III.4.b** (Form §III.4.b, p.7; *attestation*, verb "has a policy or process", actor: software producer) — "The software producer has a policy or process to address discovered security vulnerabilities prior to product release; and"
- **III.4.c** (Form §III.4.c, p.7; *attestation*, verb "operates", actor: software producer) — "The software producer operates a vulnerability disclosure program and accepts, reviews, and addresses disclosed software vulnerabilities in a timely fashion and according to any timelines specified in the vulnerability disclosure program or applicable policies."
- **III-notify** (Form Section III, p.7; *attestation*, verb "will notify", actor: software producer) — "I further attest that the software producer will notify any agency to which it has submitted this form if and when the producer ceases to make consistent use of the practices identified above in developing the software."
- **III-sign** (Form Section III, p.7; *requirement*, verb "(signature)", actor: CEO or designee) — "Signature of CEO or Designee with authority to bind the corporation"
- **III-3PAO** (Form Section III, p.7; *attestation*, verb "has evaluated", actor: software producer (3PAO path)) — "A certified FedRAMP Third Party Assessor Organization (3PAO) or other 3PAO approved in writing by an appropriate agency official has evaluated our conformance to all elements in this form. The 3PAO used relevant NIST Guidance that includes all elements outlined in this form as the assessment baseline. The assessment is attached."
- **III-attach** (Form Section III, ATTACHMENT(S), p.7; *requirement*, verb "(attachments)", actor: software producer) — "[Artifact/Addendum Title]: [Artifact/Addendum Description]"

## Burden Statement (p.8)

- **BURDEN-1** (Burden Statement, p.8; *statement*, verb "may not conduct ... is not required to respond", actor: agency; respondent) — "An agency may not conduct or sponsor, and a person is not required to respond to, a collection of information unless it displays a currently valid OMB control number and expiration date."

## Appendix (p.9)

- **APX-lead** (Appendix — References, p.9; *statement*, verb "address", actor: n/a) — "The minimum requirements within the Secure Software Attestation Form address requirements put forth in E.O. 14028 subsection (4)(e). A mapping to specific SSDF practices and tasks is provided for reference purposes."

## Appendix — References (verbatim table, pp.9-10)

"The minimum requirements within the Secure Software Attestation Form address requirements put forth in E.O. 14028 subsection (4)(e). A mapping to specific SSDF practices and tasks is provided for reference purposes."

| Attestation Requirements | Related E.O. 14028 Subsection | Related SSDF Practices and Tasks |
|---|---|---|
| 1) The software is developed and built in secure environments. Those environments are secured by the following actions, at a minimum: | 4e(i) | [See rows below] |
| a) Separating and protecting each environment involved in developing and building software; | 4e(i)(A) | PO.5.1 |
| b) Regularly logging, monitoring, and auditing trust relationships used for authorization and access: i) to any software development and build environments; and ii) among components within each environment; | 4e(i)(B) | PO.5.1 |
| c) Enforcing multi-factor authentication and conditional access across the environments relevant to developing and building software in a manner that minimizes security risk; | 4e(i)(C) | PO.5.1, PO.5.2 |
| d) Taking consistent and reasonable steps to document, as well as minimize use or inclusion of software products that create undue risk within the environments used to develop and build software; | 4e(i)(D) | PO.5.1 |
| e) Encrypting sensitive data, such as credentials, to the extent practicable and based on risk; | 4e(i)(E) | PO.5.2 |
| f) Implementing defensive cybersecurity practices, including continuous monitoring of operations and alerts and, as necessary, responding to suspected and confirmed cyber incidents; | 4e(i)(F) | PO.3.2, PO.3.3, PO.5.1, PO.5.2 |
| 2) The software producer makes a good-faith effort to maintain trusted source code supply chains by employing automated tools or comparable processes to address the security of internal code and third-party components and manage related vulnerabilities; | 4e(iii) | PO 1.1, PO.3.1, PO.3.2, PO.5.1, PO.5.2, PS.1.1, PS.2.1, PS.3.1, PW.4.1, PW.4.4, PW 7.1, PW 8.1, RV 1.1 |
| 3) The software producer maintains provenance for internal code and third-party components incorporated into the software to the greatest extent feasible; | 4e(vi) | PO.1.3, PO.3.2, PO.5.1, PO.5.2, PS.3.1, PS.3.2, PW.4.1, PW.4.4, RV.1.1, RV.1.2 |
| 4) The software producer employed automated tools or comparable processes that check for security vulnerabilities. In addition: a) The software producer operates these processes on an ongoing basis and prior to product, version, or update releases; b) The software producer has a policy or process to address discovered security vulnerabilities prior to product release; and c) The software producer operates a vulnerability disclosure program and accepts, reviews, and addresses disclosed software vulnerabilities in a timely fashion and according to any timelines specified in the vulnerability disclosure program or applicable policies. | 4e(iv) | PO.4.1, PO.4.2, PS.1.1, PW.2.1, PW.4.4, PW.5.1, PW.6.1, PW.6.2, PW.7.1, PW.7.2, PW.8.2, PW.9.1, PW.9.2, RV.1.1, RV.1.2, RV.1.3, RV.2.1, RV.2.2, RV.3.3 |

(SSDF ids reproduced as printed, including the undotted "PO 1.1", "PW 7.1", "PW 8.1", "RV 1.1".)

## Form exclusion categories (verbatim, p.3)

1. Software developed by Federal agencies;
2. Open-source software that is freely and directly obtained by a Federal agency;
3. Third-party open source and proprietary components that are incorporated into the software end product used by the agency; or
4. Software that is freely obtained and publicly available.


## Added by pass 2 (independent verifier, 2026-10-03)

Instructions dropped by pass 1, verbatim. Also noted: the Section I exclusion list (p.5) reads item 2 as 'Open source software that is freely and directly obtained directly by a Federal agency;' (differs from the p.3 list above); the Appendix row 4 reads 'employed' where the form reads 'employs'.

- **INS-00** (Instructions cover, p.1; *instruction*, verb "read (imperative)", actor: software producer) — "Read all instructions before completing this form"
- **INS-11a** (Online Form Instructions, p.3; *instruction*, verb "selecting (online path)", actor: software producer) — "Selecting the provided URL: https://softwaresecurity.cisa.gov"
- **INS-11c** (Local PDF Instructions, p.3; *instruction*, verb "saving ... using the naming convention", actor: software producer) — "Saving the completed form as a PDF using the following naming convention:"
- **I-products-2** (Form Section I, p.5; *permission*, verb "can be attached", actor: software producer) — "Additional pages can be attached to this attestation if more lines are needed:"
