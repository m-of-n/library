---
record: nist-sp-800-140
kind: normative
title: "nist-sp-800-140 — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every stated requirement in requirements.yaml with source lines appears here verbatim under its section, as a marker that `bin/check-quotes --render` writes and `bin/check-quotes` verifies; split_of children are named on their parent's line rather than quoted twice. The keyword-less binding text pass 1 added (candidate-stated and hunted) is interleaved in source order, and binding text that is not an entry (§2's opening sentence and its reference to FIPS 140-3, §3, §4, and the or between AS07.77's two items) is quoted where it falls with a line saying why. requirements.yaml holds 242 entries: 139 skeleton, 24 split children, 33 from candidates, 41 hunted, 5 inferred.

The document modifies ISO/IEC 24759 assertion by assertion. Every one of the 22 assertions it touches appears below as an entry that quotes its heading line: 13 headings stand alone and 9 are joined to the assertion's text in the same entry (no blank line between them). The index at the end lists them with their levels and the entries under each.

## §1

<!-- q L198-200 "This" .. "conformance." -->
> This document specifies the Cryptographic Module Validation Program (CMVP) modifications of the methods to be used by a Cryptographic and Security Testing Laboratory (CSTL) to demonstrate conformance.

R-0140 · no candidate (hunted)

<!-- q L200-202 "It" .. "conformity." -->
> It also specifies the modification to the required documentation vendors are to provide to the testing laboratories as supporting evidence to demonstrate conformity.

R-0141 · candidate C-0011

<!-- q L202-203 "Unless" .. "24759." -->
> Unless otherwise specified in this document, the test requirements are specified in ISO/IEC 24759.

R-0142 · no candidate (hunted)

## §2

<!-- q L207-207 "This section" .. "ISO/IEC 24759." -->
> This section identifies the normative references cited as ISO/IEC 19790 and ISO/IEC 24759.

Not an entry: names the two references whose editions R-0143 then pins.

<!-- q L207-213 "The" .. "24759:2017." -->
> The specific editions to be used are ISO/IEC 19790:2012 and ISO/IEC 24759:2017.

R-0143 · no candidate (hunted)

<!-- q L213-214 "Please" .. "2015." -->
> Please note that the version 19790:2012 referenced here includes the corrections made in 2015.

R-0144 · no candidate (hunted)

<!-- q L216-217 -->
> Federal Information Processing Standard Publication (FIPS) 140-3, Security Requirements for Cryptographic Modules

Not an entry: the third normative reference, FIPS 140-3 itself.

## §3

<!-- q L221-222 -->
> The following terms and definitions supersede or are in addition to those defined in ISO/IEC 19790 and ISO/IEC 24759:

Not an entry: §3's lead-in; the next line says there is nothing under it.

<!-- q L224-224 -->
> None at this time

Not an entry: §3 adds or supersedes no term, so ISO/IEC 19790's and ISO/IEC 24759's definitions stand.

## §4

<!-- q L228-229 -->
> The following symbols and abbreviated terms supersede or are in addition to ISO/IEC 19790 and ISO/IEC 24759 symbols and abbreviated terms:

Not an entry: §4's lead-in.

<!-- q L231-247 -->
> CMVP Cryptographic Module Validation Program CSD Computer Security Division CCCS Canadian Centre for Cyber Security CSTL Cryptographic and Security Testing Laboratory CVE Common Vulnerabilities and Exposures FIPS Federal Information Processing Standard FISMA Federal Information Security Management/Modernization Act NIST National Institute of Standards and Technology SP 800-XXX NIST Special Publication 800 series document

Not an entry: §4's abbreviations, which add to or supersede ISO/IEC 19790's and ISO/IEC 24759's.

## §5.1

<!-- q L258-260 "Section" .. "laboratories." -->
> Section 6 of this document specifies any modifications to the requirements for information that vendors shall provide to testing laboratories and the requirements for testing that shall be used by testing laboratories.

R-0001 · split: R-0145 (shall), R-0146 (shall)

<!-- q L260-261 "Following" .. "security." -->
> Following the format of ISO/IEC 24759, Section 6 includes a general area of security, followed by eleven specific areas of security.

Not an entry: describes §6's layout.

<!-- q L263-271 -->
> Each Annex is addressed in a similarly labeled SP 800-140X, such that Annex A – Documentation requirements is addressed in SP 800-140A.

R-0147 · no candidate (hunted)

<!-- q L273-274 -->
> Annex B – Cryptographic module security policy is addressed in SP 800-140B.

R-0148 · no candidate (hunted)

<!-- q L276-277 -->
> Annex C - Approved security functions is addressed in SP 800-140C.

R-0149 · no candidate (hunted)

<!-- q L279-280 -->
> Annex D – Approved sensitive parameter generation and establishment methods is addressed in SP 800-140D.

R-0150 · no candidate (hunted)

<!-- q L282-283 -->
> Annex E – Approved authentication mechanisms is addressed in SP 800-140E.

R-0151 · no candidate (hunted)

<!-- q L285-286 -->
> Annex F – Approved non-invasive attack mitigation test metrics is addressed in SP 800-140F.

R-0152 · no candidate (hunted)

## §5.2

<!-- q L290-293 "Modifications" .. "strikethrough." -->
> Modifications will follow a similar format as in ISO/IEC 24759. For additions to test requirements, new Test Evidence (TEs) or Vendor Evidence (VEs) will be listed by increasing the “sequence_number.” Modifications can include a combination of additions using underline and deletions using strikethrough.

R-0002 · split: R-0153 (none), R-0154 (none), R-0155 (can)

<!-- q L293-294 "If" .. "change.”" -->
> If no changes are required, the paragraph will indicate “No change.”

R-0156 · candidate C-0012

## §6

<!-- q L298-298 -->
> In responding to test evidence (TE), a yes/no answer does not provide sufficient assurance.

R-0157 · candidate C-0013

<!-- q L299-300 -->
> CMVP requires the following information when responding to a documentation, operational testing, or verify/verify by inspection requirement.

R-0158 · candidate C-0014

<!-- q L302-305 -->
> Documentation: Reference/cite the applicable vendor documentation and summarize the contents per the TE.

R-0159 · no candidate (hunted)

<!-- q L312-314 -->
> Operational Testing: Describe the test method and tools, and summarize the results, per the TE.

R-0160 · no candidate (hunted)

<!-- q L316-319 -->
> Verify or Verify by Inspection: Describe the test or inspection method used to verify the requirement and provide detailed results of the test or inspection, per the TE.

R-0161 · no candidate (hunted)

## §6.1

<!-- q L323-323 -->
> No change.

R-0162 · no candidate (hunted)

## §6.2

<!-- q L331-331 -->
> AS02.15: (Specification – Levels 1, 2, 3, and 4)

R-0163 · no candidate (hunted)

<!-- q L333-334 -->
> The cryptographic boundary of a hardware cryptographic module shall delimit and identify:

R-0003

<!-- q L336-336 -->
> - The set of hardware components which may include:

R-0004

<!-- q L338-339 -->
> - physical structures, including circuit boards, substrates or other mounting surfaces that provide the interconnecting physical wiring between components,

R-0164 · candidate C-0015

<!-- q L340-342 -->
> - active electrical components such as semi-integrated, custom-integrated or common-integrated circuits, processors, memory, power supplies, converters, etc.

R-0165 · candidate C-0016

<!-- q L343-344 -->
> - physical structures, such as enclosures, potting or encapsulation materials, connectors, and interfaces,

R-0166 · candidate C-0017

<!-- q L345-345 -->
> - firmware, which may include an operating system,

R-0005

<!-- q L346-346 -->
> - other components types not listed above.

R-0167 · candidate C-0018

<!-- q L349-351 -->
> VE02.15.05 For each processor in the module, the vendor shall identify, by major services, the software or firmware that are executed by the processor, and the memory devices that contain the executable code and data.

R-0006

<!-- q L353-354 -->
> VE02.15.06 For each processor, the vendor shall identify any hardware with which the processor interfaces.

R-0007

<!-- q L358-367 -->
> TE02.15.10 The tester shall verify the documentation provided under assertion AS02.02, with a focus on the block diagram depicting all of the major hardware components of a cryptographic module and component interconnections, including any microprocessors, input/output buffers, plaintext/ciphertext buffers, control buffers, key storage, working memory, and program memory.

R-0008

<!-- q L369-371 "TE02.15.11" .. "equipment." -->
> TE02.15.11 The tester shall verify that the block diagram indicates all significant interconnections and data flow among major components of the module, and between the module and outside equipment.

R-0009

<!-- q L371-372 "In" .. "transmits." -->
> In particular, each line on the block diagram indicating an interconnection must be labeled with the type of information it transmits.

R-0010

<!-- q L374-375 -->
> TE02.15.12 The tester shall verify that the block diagram indicates the cryptographic boundary for the cryptographic module, as required under this assertion.

R-0011

<!-- q L377-384 -->
> TE02.15.13 The tester shall verify that, for each processor, the vendor has identified the software or firmware code modules executed by that processor, the services performed by that processor and associated code, and the memory devices containing the executable code and data.

R-0012 · split: R-0168 (none)

<!-- q L386-387 "TE02.15.14" .. "interfaces." -->
> TE02.15.14 The tester shall verify that, for each processor, the vendor has identified any hardware with which the processor interfaces.

R-0013

<!-- q L387-390 "This" .. "software/firmware." -->
> This must include, as applicable, any hardware components that provide input, control, or status data to the processor and associated software/firmware, and any hardware components that receive output, control, or status data from the processor and associated software/firmware.

R-0014

<!-- q L390-392 "Such" .. "devices." -->
> Such hardware components may be within the cryptographic module or may be user equipment outside the module such as input/output devices.

R-0015

<!-- q L394-394 -->
> AS02.17: (Specification – Levels 1, 2, 3, and 4)

R-0169 · no candidate (hunted)

<!-- q L396-397 -->
> The cryptographic boundary of a firmware cryptographic module shall delimit and identify:

R-0016

<!-- q L399-399 -->
> - The set of executable file or files that constitute the cryptographic module; and

R-0170 · candidate C-0021

<!-- q L400-401 -->
> - The instantiation of the cryptographic module saved in memory and executed by one or more processors.

R-0171 · candidate C-0022

<!-- q L405-407 -->
> VE02.17.04 For each processor in the computing platform of the operational environment bound to the firmware module, the vendor shall identify, by major services, the firmware that is executed by the processor, and the memory devices that contain the executable code and data.

R-0017

<!-- q L409-411 -->
> VE02.17.05 For each processor in the computing platform of the operational environment bound to the firmware module, the vendor shall identify any hardware with which the processor interfaces.

R-0018

<!-- q L415-425 -->
> TE02.17.06 The tester shall verify the documentation provided under assertion AS02.02, with a focus on the block diagram depicting all of the major hardware components of a cryptographic module and component interconnections, including any microprocessors, input/output buffers, plaintext/ciphertext buffers, control buffers, key storage, working memory, and program memory.

R-0019

<!-- q L427-429 "TE02.17.07" .. "equipment." -->
> TE02.17.07 The tester shall verify that the block diagram indicates all significant interconnections and data flows among major components of the module, and between the module and outside equipment.

R-0020

<!-- q L429-430 "In" .. "transmits." -->
> In particular, each line on the block diagram indicating an interconnection must be labeled with the type of information it transmits.

R-0021

<!-- q L432-433 -->
> TE02.17.08 The tester shall verify that the block diagram indicates the cryptographic boundary for the cryptographic module, as required under this assertion.

R-0022

<!-- q L435-443 -->
> TE02.17.09 The tester shall verify that, for each processor in the computing platform of the operational environment bound to the firmware module, the vendor has identified the firmware code modules executed by that processor, the services performed by that processor and associated code, and the memory devices containing the executable code and data.

R-0023 · split: R-0172 (none)

<!-- q L445-447 "TE02.17.10" .. "interfaces." -->
> TE02.17.10 The tester shall verify that, for each processor in the computing platform of the operational environment bound to the firmware module, the vendor has identified any hardware with which the processor interfaces.

R-0024

<!-- q L447-450 "This" .. "firmware." -->
> This must include, as applicable, any hardware components that provide input, control, or status data to the processor and associated firmware, and any hardware components that receive output, control, or status data from the processor and associated firmware.

R-0025

<!-- q L450-451 "Such" .. "devices." -->
> Such hardware components may be within the cryptographic module or may be user equipment outside the module such as input/output devices.

R-0026

<!-- q L453-453 -->
> AS02.18: (Specification – Levels 1, 2, 3, and 4)

R-0173 · no candidate (hunted)

<!-- q L455-455 -->
> The cryptographic boundary of a hybrid cryptographic module shall:

R-0027

<!-- q L457-458 -->
> - be the composite of the module’s hardware component boundary and the disjoint software or firmware component(s) boundary; and

R-0174 · candidate C-0025

<!-- q L459-459 -->
> - include the collection of all ports and interfaces from each component.

R-0175 · candidate C-0026

<!-- q L466-467 -->
> VE02.18.01: The cryptographic module shall be identified in the vendor documentation as either a Hybrid Software Module or a Hybrid Firmware Module.

R-0028

<!-- q L469-471 -->
> a) For Hybrid Software Module components, the vendor documentation shall provide information required under VE02.15.01 through VE02.15.04 VE02.15.06 and VE02.16.01 through VE02.16.03.

R-0029

<!-- q L472-474 -->
> b) For Hybrid Firmware Module components, the vendor documentation shall provide information required under VE02.15.01 through VE02.15.04 VE02.15.06 and VE02.17.01 through VE02.17.03 VE02.17.05.

R-0030

<!-- q L483-484 -->
> TE02.18.01: The tester shall verify that the documentation identifies the module as either a Hybrid Software Module or a Hybrid Firmware Module.

R-0031

<!-- q L486-487 -->
> a) For Hybrid Software Module components, the tester shall follow procedures required under TE02.15.01 through TE02.15.09 TE02.15.14 and TE02.16.01 through TE02.16.05.

R-0032

<!-- q L488-490 -->
> b) For Hybrid Firmware Module components, the tester shall follow procedures required under TE02.15.01 through TE02.15.09 TE02.15.14 and TE02.17.01 through TE02.17.05 TE02.17.10.

R-0033

<!-- q L492-492 -->
> AS02.20: (Specification – Levels 1, 2, 3, and 4)

R-0176 · no candidate (hunted)

<!-- q L498-501 -->
> An approved mode of operation shall be defined as the set of services which include at least one service that utilises an approved cryptographic algorithm, security function or process and those services or processes specified in {ISO/IEC 19790:2012/Cor.1:2015 subclause} 7.4.3.

R-0034

<!-- q L505-505 -->
> VE02.20.03 The vendor shall provide a list of all vendor affirmed security methods.

R-0035

<!-- q L507-508 -->
> VE02.20.04 The vendor provided non-proprietary security policy shall include a list of all vendor affirmed security methods.

R-0036

<!-- q L512-513 -->
> TE02.20.03 The tester shall verify that the vendor has provided the list of vendor affirmed security methods as described above.

R-0037

<!-- q L515-516 -->
> TE02.20.04 The tester shall verify that the vendor provided documentation specifies how the implemented vendor affirmed security methods conform to the relevant standards.

R-0038

## §6.3

<!-- q L520-523 -->
> AS03.07: (Data output interface – Levels 1, 2, 3, and 4) All data output via the “data output” interface shall be inhibited while performing manual entry, pre-operational self-tests, software/firmware loading and zeroisation; or when the cryptographic module is in an error state.

R-0039

<!-- q L524-528 -->
> Required Vendor Information VE03.07.03: The vendor documentation shall specify how the physical and logical paths used by all major categories of output data exiting the cryptographic module are logically or physically disconnected from the processes performing SSP generation, manual SSP entry, and zeroisation of SSPs.

R-0040

<!-- q L535-537 -->
> VE03.07.04: If the physical and logical paths followed by the output data and SSP information are physically shared, the vendor documentation shall specify how the cryptographic module enforces logical separation of the output data and SSP information.

R-0041

<!-- q L538-540 -->
> VE03.07.05: The vendor documentation shall specify how the cryptographic module does not allow the specified SSP processes to pass SSP information to the output data path, and does not allow output data exiting the module to interfere with the SSP processes.

R-0042

<!-- q L544-552 -->
> TE03.07.06: The tester shall verify that the vendor documentation specifies how the physical and logical paths used by all major categories of output data exiting the cryptographic module are logically or physically disconnected from the processes performing SSP generation, manual SSP entry, and zeroisation of SSPs.

R-0043 · split: R-0177 (none)

<!-- q L554-556 -->
> TE03.07.07: If the physical and logical paths followed by the output data and SSP information are physically shared, the tester shall verify that the vendor documentation specifies how the cryptographic module enforces logical separation of the output data and SSP information.

R-0044

<!-- q L558-560 -->
> TE03.07.08: The tester shall verify that the output data path is logically or physically disconnected from the processes performing SSP generation, manual SSP entry, and zeroisation of SSPs.

R-0045

## §6.4

<!-- q L565-567 -->
> AS04.44: (Operator authentication – Levels 1, 2, 3, and 4) Authentication data within a cryptographic module shall be protected against unauthorised use, disclosure, modification, and substitution.

R-0046

<!-- q L568-568 -->
> NOTE Approved security functions can be used as part of the authentication mechanism.

R-0047

<!-- q L569-571 "Required" .. "module." -->
> Required Vendor Information VE04.44.01: The vendor documentation shall describe the protection of all authentication data within the module.

R-0048

<!-- q L571-572 "Protection" .. "substitution." -->
> Protection shall include the implementation of mechanisms that protect against unauthorised use, disclosure, modification, and substitution.

R-0049

<!-- q L575-576 "TE04.44.01:" .. "data." -->
> TE04.44.01: The tester shall verify the vendor documentation that describes the protection of authentication data.

R-0050

<!-- q L576-577 "The" .. "substitution." -->
> The tester shall verify that the documentation describes how the data will be protected against unauthorised use, disclosure, modification, and substitution.

R-0051

<!-- q L578-578 -->
> AS04.45: (Operator authentication – Levels 2, 3, and 4)

R-0178 · no candidate (hunted)

<!-- q L580-588 -->
> If a cryptographic module does not contain the authentication data required to authenticate the operator for the first time the module is accessed, then other authorised methods (e.g. procedural controls or use of factory-set or default authentication data) shall be used to control access to the module and initialise the authentication mechanisms.

R-0052

<!-- q L592-593 -->
> TE04.45.02: If access to the module before initialisation is procedurally controlled, the tester shall initiate an error on an uninitialised module and shall verify that the module denies access.

R-0053

<!-- q L594-595 "The" .. "procedures." -->
> The tester shall assume the authorised role and verify that the required authentication complies with the documented procedures.

R-0054

<!-- q L595-596 "The" .. "roles." -->
> The tester shall attempt to assume other roles before the module has been initialised and verify that the module denies access to the roles.

R-0055

<!-- q L598-598 -->
> AS04.54: (Operator authentication — Levels 2, 3, and 4)

R-0179 · no candidate (hunted)

<!-- q L604-605 "Feedback" .. "operator." -->
> Feedback of authentication data to an operator shall be obscured during authentication to anyone other than the operator.

R-0056

<!-- q L605-606 "(e.g." .. "password)." -->
> (e.g. no visible display of characters when entering a password).

R-0180 · no candidate (hunted)

<!-- q L610-611 -->
> VE04.54.01: The vendor documentation shall specify the method used to obscure feedback of the authentication data to an operator during entry of the authentication data.

R-0057

<!-- q L613-615 -->
> VE04.54.02: The vendor documentation shall specify how, if implemented, the vendor allows an operator to confirm authentication data at the time of entry, while obscuring any useful information to all others.

R-0058

<!-- q L619-620 -->
> TE04.54.01: The tester shall verify from the vendor documentation that the authentication data is obscured during data entry.

R-0059

<!-- q L622-623 -->
> TE04.54.02: The tester shall enter authentication data and verify that there is no access of authentication data during data entry, except, as an option, to the operator.

R-0060

<!-- q L625-626 -->
> TE04.54.03: If the vendor allows an operator to confirm authentication data at the time of entry, the tester shall verify that this information is obscured from other entities.

R-0061

## §6.5

<!-- q L630-630 -->
> No change.

R-0181 · no candidate (hunted)

## §6.6

<!-- q L634-636 -->
> AS06.11: (Operational environment – Level 2) The operating system shall be configured to protect against unauthorised execution, unauthorised modification, and unauthorised reading of SSPs, control and status data.

R-0062

<!-- q L637-646 -->
> Required Vendor Information VE06.11.01: The vendor shall provide operating system documentation which provides a description of the operating system control mechanisms which can be configured to protect against unauthorised execution, unauthorised modification, and unauthorised reading of SSPs, control and status data.

R-0063 · split: R-0182 (can)

<!-- q L647-651 -->
> Required Test Procedures TE06.11.01: The tester shall verify that the vendor documentation, and by inspection of operating system control mechanisms, that the operating system can be configured to protect against unauthorised execution, unauthorised modification, and unauthorised reading of SSPs, control and status data.

R-0064 · split: R-0183 (can)

<!-- q L652-658 -->
> TE06.11.02: The tester shall configure the operating system to protect against unauthorised execution, unauthorised modification, and unauthorised reading of SSPs, control and status data.

R-0065 · split: R-0184 (none)

<!-- q L659-660 -->
> During execution of a cryptographic process, the tester shall attempt to execute, modify or read SSPs, control or status data which the tester has authorised access.

R-0066

<!-- q L661-662 -->
> TE06.11.03: The tester shall configure the operating system to protect against unauthorised execution, unauthorised modification, and unauthorised reading of SSPs, control and status data.

R-0067

<!-- q L663-664 -->
> During execution of a cryptographic process, the tester shall attempt to execute, modify or read SSPs, control or status data which the tester has unauthorised access.

R-0068

## §6.7

<!-- q L668-671 -->
> AS07.26: (Physical security – Levels 3 and 4) Strong or hard conformal or non-conformal enclosures, coatings or potting materials shall maintain strength and hardness characteristics over the module's intended temperature range of operation, storage and distribution.

R-0069

<!-- q L672-675 -->
> Required Vendor Information VE07.26.01: The vendor documentation shall describe the strength or hardness of the, hard conformal or non-conformal enclosure, coatings or potting materials and the rationale that the strength or hardness is appropriate for the module design.

R-0070

<!-- q L676-677 -->
> VE07.26.02: The vendor provided security policy shall specify the nominal and high/low temperature range.

R-0071

<!-- q L678-681 "Required" .. "specified." -->
> Required Test Procedures TE07.26.01: The tester shall verify from the vendor documentation and inspection testing of the module that the strength or hardness of the, hard conformal or non-conformal enclosure, coatings or potting materials is the one designed implemented as specified.

R-0072

<!-- q L681-682 "The" .. "temperatures:" -->
> The tester shall verify the module hardness at the following temperatures:

R-0073

<!-- q L683-684 -->
> - the lowest temperature of the module’s intended temperature range of operation, storage and distribution;

R-0185 · candidate C-0037

<!-- q L692-693 -->
> - the highest temperature of the module’s intended temperature range of operation, storage and distribution.

R-0186 · candidate C-0038

<!-- q L694-695 -->
> TE07.26.02: The tester shall verify that the vendor provided security policy specifies the high/low temperature range.

R-0074

<!-- q L696-696 -->
> AS07.77: (Environmental failure protection features — Levels 3 and 4)

R-0187 · candidate C-0039

<!-- q L698-699 -->
> If the temperature or voltage falls outside of the cryptographic module’s normal operating range, the protection capability shall either

R-0075

<!-- q L701-701 -->
> — shutdown the module to prevent further operation,

R-0188 · no candidate (hunted)

<!-- q L707-707 -->
> or

Not an entry: the word joining AS07.77's two items (R-0188, R-0189), which R-0075's either opens.

<!-- q L708-708 -->
> — immediately zeroise all unprotected SSPs

R-0189 · no candidate (hunted)

<!-- q L712-714 "VE07.77.01:" .. "condition." -->
> VE07.77.01: If EFP is chosen for a particular condition, the module shall monitor and correctly respond to fluctuations in the operating temperature or voltage outside of the module’s normal operating range for that condition.

R-0076

<!-- q L714-715 "The" .. "conditions." -->
> The protection features shall continuously measure these environmental conditions.

R-0077

<!-- q L715-716 "If" .. "either" -->
> If a condition is determined to be outside of the module’s normal operating range, the protection circuitry shall either

R-0078

<!-- q L718-718 -->
> a) shutdown the module, or

R-0190 · candidate C-0041

<!-- q L720-720 -->
> b) zeroise all plaintext unprotected SSPs

R-0191 · candidate C-0042

<!-- q L722-723 -->
> Documentation shall state which of these approaches was chosen and provide a specification description of the EFP features implemented within the module.

R-0079

<!-- q L725-726 -->
> VE07.77.02: The security policy shall address whether the employed EFP feature forces module shutdown or zeroises all unprotected SSPs and shall specify the temperature range met.

R-0080

<!-- q L730-733 -->
> TE07.77.04 The tester shall verify that the security policy specifies the normal operating temperature and voltage range, and whether the module shuts down or zeroises all unprotected SSPs if the operating temperature or voltage falls outside the normal operating range of the module.

R-0081

<!-- q L735-735 -->
> AS07.81: (Environmental failure testing procedures — Level 3)

R-0192 · no candidate (hunted)

<!-- q L737-748 -->
> The temperature range to be tested shall be from a temperature within the normal operating temperature range to the lowest (i.e., coldest) temperature that either (1) shutdown the module to prevent further operation or (2) immediately zeroise all unprotected SSPs; and from a temperature within the normal operating temperature range to the highest (i.e., hottest) temperature that either (1) shuts down or goes into an error state or (2) zeroises all unprotected SSPs.

R-0082

<!-- q L752-753 -->
> VE07.81.01: If EFT is chosen for a particular condition, the module shall be tested within the temperature range specified in AS07.82 and voltage ranges specified in AS07.85 and AS07.86.

R-0083

<!-- q L754-754 -->
> The module shall either:

R-0084

<!-- q L756-756 -->
> a) continue to operate normally, or

R-0193 · candidate C-0045

<!-- q L757-757 -->
> b) shutdown, or

R-0194 · candidate C-0046

<!-- q L763-763 -->
> c) zeroise all plaintext unprotected SSPs.

R-0195 · candidate C-0047

<!-- q L765-766 -->
> Documentation shall state which of these approaches was chosen and provide a specification description of the EFT.

R-0085

<!-- q L768-769 -->
> VE07.81.02: The security policy shall address whether the employed EFT feature forces module shutdown or zeroises all unprotected SSPs and shall specify the temperature range met.

R-0086

<!-- q L773-776 -->
> TE07.81.03: The tester shall verify that the non-proprietary security policy specifies the normal operating temperature and voltage range, and whether the module forces shut down or zeroises all unprotected SSPs if the operating temperature or voltage falls outside the normal operating range of the module.

R-0087

## §6.8

<!-- q L780-780 -->
> No change.

R-0196 · no candidate (hunted)

## §6.9

<!-- q L784-788 -->
> AS09.23: (Sensitive security parameter entry and output – Level 3) {If the module employs split knowledge procedures, the module shall employ separate identity-based operator authentication for entering or outputting each key component,} and at least two key components shall be required to reconstruct the original cryptographic key.

R-0088

<!-- q L791-792 -->
> VE09.23.01: The vendor documentation shall specify the number of components that are required to construct the original CSP.

R-0089

<!-- q L793-802 -->
> VE09.23.02: If knowledge of the number of key components is required to reconstruct the original key, the vendor provided documentation shall include rationale stating how knowledge of any one less than the number of key components provides no information about the original key other than the length.

R-0090

<!-- q L803-805 -->
> Required Test Procedures TE09.23.01: The tester shall verify in the vendor provided documentation that the split knowledge procedure requires at least two components to construct the original CSP.

R-0091

<!-- q L806-809 -->
> TE09.23.02: The tester shall verify the vendor provided documentation provides a rationale that no information is gained without knowing all the necessary split keys. that the output of CSPs under split knowledge procedures does not result in the output of a single component that can be used to construct the original CSP.

R-0092 · split: R-0197 (can)

<!-- q L810-810 "TE09.23.04:" .. "vendor." -->
> TE09.23.04: The tester shall verify the accuracy of any rationale provided by the vendor.

R-0093

<!-- q L810-817 "The burden" .. "needed." -->
> The burden of proof is on the vendor; if there is any uncertainty or ambiguity, the tester shall require the vendor to produce additional information as needed.

R-0094

<!-- q L818-818 -->
> AS09.28: (Sensitive security parameter zeroisation – Levels 1, 2, 3, and 4)

R-0198 · no candidate (hunted)

<!-- q L820-821 -->
> A module shall provide methods to zeroise all unprotected SSPs and key components within the module.

R-0095

<!-- q L825-826 -->
> VE09.28.01: The vendor documentation shall specify the following zeroisation information for SSPs:

R-0096

<!-- q L828-828 -->
> a. Zeroisation techniques

R-0199 · no candidate (hunted)

<!-- q L829-830 "Restrictions" .. "c." -->
> Restrictions when unprotected SSPs can be zeroised c.

R-0097 · split: R-0200 (can)

<!-- q L830-830 -->
> c. Unprotected SSPs that are zeroised

R-0201 · no candidate (hunted)

<!-- q L831-831 -->
> d. Unprotected SSPs that are not zeroised and rationale

R-0202 · no candidate (hunted)

<!-- q L832-833 -->
> e. Rationale explaining how the zeroisation technique is performed in a time that is not sufficient to compromise unprotected SSPs

R-0203 · no candidate (hunted)

<!-- q L835-836 -->
> VE09.28.02 The vendor documentation shall specify how the zeroisation method(s) are employed such that unprotected SSPs within the module cannot be obtained by an attacker.

R-0098 · split: R-0204 (cannot)

<!-- q L838-841 -->
> VE09.28.03: If SSPs are zeroised procedurally while under the control of the operator (i.e., present to observe the method has completed successfully or controlled via a remote management session), vendor documentation and the module security policy must specify how the methods shall be performed.

R-0099 · split: R-0205 (shall)

<!-- q L845-846 "TE09.28.01:" .. "VE09.30.01." -->
> TE09.28.01: The tester shall verify the vendor documentation includes the information specified in VE09.30.01.

R-0100

<!-- q L846-846 "The" .. "vendor." -->
> The tester shall verify the accuracy of any rationale provided by the vendor.

R-0101

<!-- q L846-853 "The burden" .. "needed." -->
> The burden of proof is on the vendor; if there is any uncertainty or ambiguity, the tester shall require the vendor to produce additional information as needed.

R-0102

<!-- q L855-856 "TE09.28.02:" .. "command." -->
> TE09.28.02: The tester shall verify which SSPs are present in the module and initiate the zeroise command.

R-0103

<!-- q L856-857 "Following" .. "module." -->
> Following the completion of the zeroise command, the tester shall attempt to perform cryptographic operations using each of the unprotected SSPs that were stored in the module.

R-0104

<!-- q L857-858 "The" .. "accessed." -->
> The tester shall verify that each unprotected SSP cannot be accessed.

R-0105 · split: R-0206 (cannot)

<!-- q L860-861 -->
> TE09.28.03: The tester shall initiate zeroisation and verify the SSP destruction method is performed in a time that is not sufficient to compromise unprotected SSPs.

R-0106

<!-- q L863-871 -->
> TE09.28.04: The tester shall verify that all unprotected SSPs that are not zeroised by the zeroise command are either 1) encrypted using an approved algorithm, or 2) physically or logically protected within an embedded validated cryptographic module (validated as conforming to ISO/IEC 19790).

R-0107 · split: R-0207 (none)

<!-- q L873-875 -->
> TE09.28.05: If procedural zeroisation methods are used, the tester shall verify that the vendor provided documentation, including the security policy, specifies that the procedure must be performed under the control of the operator.

R-0108 · split: R-0208 (must)

<!-- q L877-879 "TE09.28.06" .. "attacker." -->
> TE09.28.06 If the procedural zeroisation method is not under the direct control of the operator, the tester shall verify the accuracy of any rationale provided by the vendor as to why unprotected SSPs within the module cannot be obtained by an attacker.

R-0109 · split: R-0209 (cannot)

<!-- q L879-881 "The" .. "needed." -->
> The burden of proof is on the vendor; if there is any uncertainty or ambiguity, the tester shall require the vendor to produce additional information as needed.

R-0110

<!-- q L883-883 -->
> NOTE 1 This assertion is tested AS09.30.

R-0210 · no candidate (hunted)

<!-- q L888-888 -->
> AS09.29: (Sensitive security parameter zeroisation – Levels 1, 2, 3, and 4)

R-0211 · no candidate (hunted)

<!-- q L890-890 -->
> A zeroised SSP shall not be retrievable or reusable.

R-0111

<!-- q L894-895 -->
> VE09.29.01: The vendor documentation shall specify how a zeroised SSP cannot be retrievable or reusable.

R-0112 · split: R-0212 (cannot)

<!-- q L899-900 -->
> TE09.29.01: The tester shall verify that the vendor provided documentation specifies how a zeroised SSP cannot be retrievable or reusable.

R-0113 · split: R-0213 (cannot)

<!-- q L909-909 "TE09.29.02:" .. "vendor." -->
> TE09.29.02: The tester shall verify the accuracy of any rationale provided by the vendor.

R-0114

<!-- q L909-911 "The burden" .. "needed." -->
> The burden of proof is on the vendor; if there is any uncertainty or ambiguity, the tester shall require the vendor to produce additional information as needed.

R-0115

<!-- q L913-915 -->
> NOTE 1 Zeroisation of protected PSPs, encrypted CSPs, or CSPs otherwise physically or logically protected within an additional embedded validated module (meeting the requirements of this document International Standard) is not required.

R-0214 · candidate C-0055

<!-- q L917-919 -->
> NOTE 2 SSPs need not meet these zeroisation requirements if they are used exclusively to reveal plaintext data to processes that are authentication proxies (e.g. a CSP that is a module initialisation key).

R-0215 · candidate C-0056

<!-- q L925-925 -->
> AS09.30: (Sensitive security parameter zeroisation – Levels 2, 3, and 4)

R-0216 · no candidate (hunted)

<!-- q L927-928 -->
> The cryptographic module shall perform the zeroisation of unprotected SSPs (e.g. overwriting with all zeros or all ones or with random data).

R-0116

<!-- q L930-930 -->
> NOTE 1 This assertion is tested in AS09.28.

R-0217 · no candidate (hunted)

<!-- q L934-935 -->
> VE09.30.01: The vendor documentation shall specify the following SSPs zeroisation information:

R-0117

<!-- q L937-937 -->
> a) Zeroisation techniques

R-0218 · candidate C-0058

<!-- q L938-938 -->
> b) Restrictions when plaintext SSPs can be zeroised

R-0118

<!-- q L939-939 -->
> c) Plaintext SSPs that are zeroised

R-0219 · candidate C-0059

<!-- q L940-940 -->
> d) Plaintext SSPs that are not zeroised and rationale

R-0220 · candidate C-0060

<!-- q L941-942 -->
> e) Rationale explaining how the zeroisation technique is performed in a time that is not sufficient to compromise plaintext SSPs

R-0221 · candidate C-0061

<!-- q L946-947 "TE09.30.01:" .. "included." -->
> TE09.30.01: The tester shall verify the vendor documentation that the information specified in VE09.30.01 is included.

R-0119

<!-- q L947-948 "The" .. "vendor." -->
> The tester shall verify the accuracy of any rationale provided by the vendor.

R-0120

<!-- q L948-949 "The" .. "needed." -->
> The burden of proof is on the vendor; if there is any uncertainty or ambiguity, the tester shall require the vendor to produce additional information as needed.

R-0121

<!-- q L951-952 "TE09.30.02:" .. "command." -->
> TE09.30.02: The tester shall verify which keys are present in the module and initiate the zeroise command.

R-0122

<!-- q L952-953 "Following" .. "module." -->
> Following the completion of the zeroise command, the tester shall attempt to perform cryptographic operations using each of the plaintext SSPs that were stored in the module.

R-0123

<!-- q L953-954 "The" .. "accessed." -->
> The tester shall verify that each plaintext SSPs cannot be accessed.

R-0124 · split: R-0222 (cannot)

<!-- q L956-957 -->
> TE09.30.03: The tester shall initiate zeroisation and verify the key destruction method is performed in a time that is not sufficient to compromise plaintext SSPs.

R-0125

<!-- q L965-968 -->
> TE09.30.04: The tester shall verify that all plaintext SSPs that are not zeroised by the zeroise command are either 1) encrypted using an approved algorithm, or 2) physically or logically protected within an embedded validated cryptographic module (validated as conforming to ISO/IEC 19790:2012/Cor.1:2015).

R-0126

## §6.10

<!-- q L972-981 -->
> AS10.01: (Self-tests – Levels 1, 2, 3, and 4) All self-tests shall be performed, {and determination of pass or fail shall be made by the module, without external controls, externally provided input text test vectors, expected output results, or operator intervention or whether the module will operate in an approved or non-approved mode}.

R-0127 · split: R-0223 (none)

<!-- q L982-982 -->
> NOTE This assertion is not separately tested.

R-0224 · no candidate (hunted)

<!-- q L983-987 -->
> AS10.02: (Self-tests – Levels 1, 2, 3, and 4) {All self-tests shall be performed,} and determination of pass or fail shall be made by the module, without external controls, externally provided input text test vectors, expected output results, or operator intervention or whether the module will operate in an approved or non-approved mode.

R-0128

<!-- q L988-993 -->
> NOTE The intention of this assertion is that the determination of pass or fail will be made by the module, without external controls, primarily for pre-operational self-tests and (conditional) cryptographic algorithm self-test. It is known that a software/firmware load test into a validated module involves the software or firmware that is loaded from an external source, and that a manual entry test involves SSPs or key components manually entered by a human operator; however, the essence is the same.

R-0225 · no candidate (hunted)

<!-- q L994-994 -->
> AS10.07: (Self-tests – Levels 1, 2, 3, and 4)

R-0226 · no candidate (hunted)

<!-- q L996-997 -->
> If a cryptographic module fails a self-test, the module shall enter an error state {and shall output an error indicator as specified in {ISO/IEC 19790:2012/Cor.1:2015 subclause} 7.3.3}.

R-0129

<!-- q L998-1001 -->
> Required Test Procedures TE10.07.05: The tester shall verify by inspection and from the vendor documentation that determination of pass or fail of each self-test is made by the module, without external controls, externally provided input text test vectors, expected output results, or operator intervention.

R-0130

## §6.11

<!-- q L1005-1007 -->
> AS11.13: (Finite state model – Levels 1, 2, 3, and 4) Changing to the Crypto Officer state from any other role other than the Crypto Officer shall be prohibited.

R-0131

<!-- q L1008-1009 -->
> NOTE: The intention of this assertion is to remove/avoid privilege escalation to a Crypto Officer role.

R-0227 · no candidate (hunted)

<!-- q L1015-1015 -->
> AS11.29: (Vendor testing – Levels 1, 2, 3, and 4)

R-0228 · no candidate (hunted)

<!-- q L1017-1017 -->
> Documentation shall specify the functional testing performed on the cryptographic module.

R-0132

<!-- q L1021-1023 -->
> VE11.29.01: The vendor shall provide documentation that specifies the functional testing performed on the cryptographic module, providing assurance that the cryptographic module behaves in accordance with the module security policy and functional specifications.

R-0133

<!-- q L1027-1033 -->
> TE11.29.01: The tester shall verify that the vendor provided documentation that specifies the functional testing performed on the cryptographic module.

R-0134 · split: R-0229 (none)

<!-- q L1034-1036 -->
> TE11.29.02: The tester shall verify that the vendor provided documentation provides assurance that the cryptographic module behaves in accordance with the module security policy and functional specifications.

R-0135

<!-- q L1037-1038 -->
> AS11.38: (Guidance documents – Levels 1, 2, 3, and 4) Administrator guidance shall specify:

R-0136

<!-- q L1039-1041 -->
> - the administrative functions, security events, security parameters (and parameter values, as appropriate), physical ports, and logical interfaces of the cryptographic module available to the Crypto Officer and/or other administrative roles;

R-0230 · candidate C-0065

<!-- q L1042-1043 -->
> - procedures required to keep operator authentication data and mechanisms functionally independent;

R-0231 · candidate C-0066

<!-- q L1044-1045 -->
> - procedures on how to administer the cryptographic module in an approved mode of operation; and

R-0232 · candidate C-0067

<!-- q L1046-1047 -->
> - assumptions regarding User behavior that are relevant to the secure operation of the cryptographic module.

R-0233 · candidate C-0068

<!-- q L1050-1050 -->
> VE11.38.03: The vendor shall list any CVEs associated with the module, and either

R-0137

<!-- q L1052-1052 -->
> - provide assurance that they are not security relevant;

R-0234 · candidate C-0070

<!-- q L1053-1054 -->
> - or, for any CVE’s that are considered security relevant, the vendor shall describe how they have been mitigated.

R-0138

<!-- q L1058-1058 -->
> TE11.38.03: The tester shall verify that any CVEs associated with the module:

R-0139

<!-- q L1060-1060 -->
> - are not security relevant, or,

R-0235 · candidate C-0072

<!-- q L1061-1061 -->
> - if they are security relevant, mitigations provided by the vendor are appropriate.

R-0236 · candidate C-0073

## §6.12

<!-- q L1070-1070 -->
> No change.

R-0237 · no candidate (hunted)

## Assertion index

By script from each entry's assertion field. Assertions named in this document but not modified by it: AS02.02 (TE02.15.10, TE02.17.06), AS07.82, AS07.85 and AS07.86 (VE07.81.01); the VE and TE ranges of VE02.18.01 and TE02.18.01 name designators of AS02.15, AS02.16 and AS02.17 that it does not list (SD-1).

| assertion | levels | heading entry | entries under it |
|---|---|---|---|
| AS02.15 | 1, 2, 3, 4 | R-0163 | R-0003, R-0004, R-0005, R-0006, R-0007, R-0008, R-0009, R-0010, R-0011, R-0012, R-0013, R-0014, R-0015, R-0164, R-0165, R-0166, R-0167, R-0168 |
| AS02.17 | 1, 2, 3, 4 | R-0169 | R-0016, R-0017, R-0018, R-0019, R-0020, R-0021, R-0022, R-0023, R-0024, R-0025, R-0026, R-0170, R-0171, R-0172 |
| AS02.18 | 1, 2, 3, 4 | R-0173 | R-0027, R-0028, R-0029, R-0030, R-0031, R-0032, R-0033, R-0174, R-0175 |
| AS02.20 | 1, 2, 3, 4 | R-0176 | R-0034, R-0035, R-0036, R-0037, R-0038 |
| AS03.07 | 1, 2, 3, 4 | R-0039 | R-0040, R-0041, R-0042, R-0043, R-0044, R-0045, R-0177 |
| AS04.44 | 1, 2, 3, 4 | R-0046 | R-0047, R-0048, R-0049, R-0050, R-0051 |
| AS04.45 | 2, 3, 4 | R-0178 | R-0052, R-0053, R-0054, R-0055 |
| AS04.54 | 2, 3, 4 | R-0179 | R-0056, R-0057, R-0058, R-0059, R-0060, R-0061, R-0180 |
| AS06.11 | 2 | R-0062 | R-0063, R-0064, R-0065, R-0066, R-0067, R-0068, R-0182, R-0183, R-0184, R-0241 |
| AS07.26 | 3, 4 | R-0069 | R-0070, R-0071, R-0072, R-0073, R-0074, R-0185, R-0186 |
| AS07.77 | 3, 4 | R-0187 | R-0075, R-0076, R-0077, R-0078, R-0079, R-0080, R-0081, R-0188, R-0189, R-0190, R-0191 |
| AS07.81 | 3 | R-0192 | R-0082, R-0083, R-0084, R-0085, R-0086, R-0087, R-0193, R-0194, R-0195 |
| AS09.23 | 3 | R-0088 | R-0089, R-0090, R-0091, R-0092, R-0093, R-0094, R-0197 |
| AS09.28 | 1, 2, 3, 4 | R-0198 | R-0095, R-0096, R-0097, R-0098, R-0099, R-0100, R-0101, R-0102, R-0103, R-0104, R-0105, R-0106, R-0107, R-0108, R-0109, R-0110, R-0199, R-0200, R-0201, R-0202, R-0203, R-0204, R-0205, R-0206, R-0207, R-0208, R-0209, R-0210 |
| AS09.29 | 1, 2, 3, 4 | R-0211 | R-0111, R-0112, R-0113, R-0114, R-0115, R-0212, R-0213, R-0214, R-0215 |
| AS09.30 | 2, 3, 4 | R-0216 | R-0116, R-0117, R-0118, R-0119, R-0120, R-0121, R-0122, R-0123, R-0124, R-0125, R-0126, R-0217, R-0218, R-0219, R-0220, R-0221, R-0222 |
| AS10.01 | 1, 2, 3, 4 | R-0127 | R-0223, R-0224 |
| AS10.02 | 1, 2, 3, 4 | R-0128 | R-0225 |
| AS10.07 | 1, 2, 3, 4 | R-0226 | R-0129, R-0130 |
| AS11.13 | 1, 2, 3, 4 | R-0131 | R-0227 |
| AS11.29 | 1, 2, 3, 4 | R-0228 | R-0132, R-0133, R-0134, R-0135, R-0229 |
| AS11.38 | 1, 2, 3, 4 | R-0136 | R-0137, R-0138, R-0139, R-0230, R-0231, R-0232, R-0233, R-0234, R-0235, R-0236 |

## Inferred requirements (not verbatim)

These entries are in our words and quote nothing; each names what it is derived from in `derived_from`. R-0238 (§5.2), R-0239 (§6), R-0240 (§6.10), R-0241 (§6.6), R-0242 (§5.1).

## Source defects and open questions

Found reading the source for this pass. Each quotes the lines it rests on; the prose is ours.

### SD-1 — the underline and strikethrough are lost, and where they met the words weld

§5.2 marks additions by underline and deletions by strikethrough. The pdftotext rendering every tool reads keeps the words of both and neither mark, so wherever a deletion sits beside its replacement the text reads as one garbled phrase, and which words are deleted cannot be recovered from the .txt. The sites found:

<!-- q L470-471 "VE02.15.01" .. "VE02.16.03." -->
> VE02.15.01 through VE02.15.04 VE02.15.06 and VE02.16.01 through VE02.16.03.

<!-- q L487-487 "TE02.15.01" .. "TE02.16.05." -->
> TE02.15.01 through TE02.15.09 TE02.15.14 and TE02.16.01 through TE02.16.05.

VE02.18.01 a) and TE02.18.01 a), and their b) items, each print two numbers side by side. Two readings fit the numbering, and the rendering cannot choose: (i) the first is struck and the second added, extending each range to the designators this document lists after the old end (VE02.15.05 to VE02.15.06, TE02.15.10 to TE02.15.14, VE02.17.04 to VE02.17.05, TE02.17.06 to TE02.17.10), so a hybrid module takes them all; or (ii) the second is an added single item, so a hybrid module takes the old range plus the hardware-interface designator alone (VE02.15.06, TE02.15.14, VE02.17.05, TE02.17.10) and not the per-processor code identification or the new block-diagram TEs. Entries: R-0029, R-0030, R-0032, R-0033.

<!-- q L680-681 "the" .. "specified." -->
> the strength or hardness of the, hard conformal or non-conformal enclosure, coatings or potting materials is the one designed implemented as specified.

<!-- q L722-723 -->
> Documentation shall state which of these approaches was chosen and provide a specification description of the EFP features implemented within the module.

<!-- q L720-720 -->
> b) zeroise all plaintext unprotected SSPs

<!-- q L806-809 "provides" .. "CSP." -->
> provides a rationale that no information is gained without knowing all the necessary split keys. that the output of CSPs under split knowledge procedures does not result in the output of a single component that can be used to construct the original CSP.

<!-- q L913-915 -->
> NOTE 1 Zeroisation of protected PSPs, encrypted CSPs, or CSPs otherwise physically or logically protected within an additional embedded validated module (meeting the requirements of this document International Standard) is not required.

Also: VE07.26.01 (of the, hard, L673), VE07.81.01 (a specification description, L765-766; plaintext unprotected, L763) and AS07.81's two differently worded end points (L737-748). Entries carry the site in their note.

### SD-2 — AS09.28 and AS09.30 each say the other tests them

Each NOTE 1 routes the assertion's test to the other assertion, while both list TEs of their own. One of the two NOTEs may be a struck deletion (SD-1); the rendering cannot say. Entries: R-0210, R-0217.

<!-- q L883-883 -->
> NOTE 1 This assertion is tested AS09.30.

<!-- q L930-930 -->
> NOTE 1 This assertion is tested in AS09.28.

### SD-3 — TE09.28.01 checks AS09.30's vendor information

Under AS09.28, TE09.28.01 verifies the information of VE09.30.01, AS09.30's item list, although AS09.28 has its own VE09.28.01 with the same five items for unprotected rather than plaintext SSPs. Entry: R-0100.

<!-- q L845-846 "TE09.28.01:" .. "VE09.30.01." -->
> TE09.28.01: The tester shall verify the vendor documentation includes the information specified in VE09.30.01.

### SD-4 — the test of AS10.02's clause sits under AS10.07

AS10.02 lists no TE. TE10.07.05, filed under AS10.07 (error state on a failed self-test), verifies that the module decides pass or fail without external controls, which is AS10.02's clause, and nothing here tests AS10.07's error state. Entries: R-0128, R-0130.

<!-- q L999-1001 -->
> TE10.07.05: The tester shall verify by inspection and from the vendor documentation that determination of pass or fail of each self-test is made by the module, without external controls, externally provided input text test vectors, expected output results, or operator intervention.

### SD-5 — AS11.13 mixes state and role

The assertion speaks of changing to a state from a role, and a state of the finite state model is not a role. Its NOTE gives the aim as keeping any other role from gaining Crypto Officer privileges. Entries: R-0131, R-0227.

<!-- q L1006-1007 -->
> Changing to the Crypto Officer state from any other role other than the Crypto Officer shall be prohibited.

### SD-6 — TE06.11.02 states no result

TE06.11.02 and TE06.11.03 state the attempts and not the outcome that passes. For TE06.11.03 the outcome follows from AS06.11 (R-0241); for TE06.11.02, attempts on data the tester is authorised for, nothing settles whether success is what passes. Entries: R-0066, R-0068.

### SD-7 — terms used and not defined

Vendor affirmed security methods (VE02.20.03, VE02.20.04, TE02.20.03, TE02.20.04) is defined neither here nor, by §3, added; EFP and EFT, CSP and PSP are ISO/IEC 19790's and not in §4. Entries: R-0035, R-0036.

### SD-8 — NOTE 1 of AS09.28 drops a word

It reads tested AS09.30 where AS09.30's NOTE reads tested in AS09.28. Editorial; see SD-2.

### SD-9 — §2 pins the editions that FIPS 140-3 says float

§2 names ISO/IEC 19790:2012 (with its 2015 corrections) and ISO/IEC 24759:2017 as the editions to use; FIPS 140-3 §3.1 says the latest edition of each applies when they are referred to (fips-140-3 SD-3). Both editions were withdrawn on 2025-02-26 and revised by 2025 editions (the notes of the library's `iso-iec-19790` and `iso-iec-24759` records), so the two documents now disagree. Entries: R-0143, R-0144.

### SD-10 — Annex D's title

§5.1 gives ISO/IEC 19790 Annex D as approved sensitive parameter generation and establishment methods; FIPS 140-3 §3.3 titles SP 800-140D with sensitive security parameter. SP 800-140D's own withdrawal notice titles it as §5.1 does (`nist-sp-800-140d`). Editorial. Entry: R-0150.

## Tooling defects (bin/, not the source)

### TD-1 — fixed in library#137 (63d708e): the mid-page sidebar split sentences

NIST prints its free-of-charge sidebar rotated, and pdftotext places it mid-page with blank lines around it. The old reader removed the sidebar line as furniture but kept the blank lines, so the skeleton's block splitter saw a paragraph break inside a sentence: seven skeleton entries stopped at the sidebar (R-0012, R-0023, R-0043, R-0065, R-0107, R-0127, R-0134) and one began after it (R-0094). Pass 1 first cut each lost tail from the source as a hunted entry. Since the fix the reader drops the blank surround too; the eight skeleton texts are re-cut, by script from a re-run of bin/fx1-skeleton, to the whole sentence under the same ids, and the seven tails (R-0168, R-0172, R-0177, R-0184, R-0207, R-0223, R-0229) are their split_of children under their own ids. No keyword moved: the tails carry none. The sidebar also split a sentence of the Authority section (L65-L73), so the skeleton offered two front-matter candidates, C-0003 (L65-L66) and C-0004 (L72-L73). A re-run under the fixed reader offers one, C-0003's text followed by the whole of C-0004's, and numbers every later candidate one lower (72 in all, as skeleton-report.txt now says). This file keeps its 73 ids and both texts, which are still verbatim within their lines.

### TD-2 — sentence and NOTE boundaries the skeleton misreads

A number followed by a full stop (24759.) is read as a list number, so C-0010's Abstract text welds three sentences; list letters attach to the neighbouring item (R-0097); and a NOTE that follows an assertion's text with no blank line is filed as a requirement (R-0047). None changes a verbatim text; the verdicts and notes carry the corrections.

### TD-3 — fixed in library#137: `clean_pdf` dropped each page's first line

As in fips-140-3 (its TD-1): a page-opening line was blanked. Here every such line is a running header except L22 (the second title page) and L1081 (the closing page), neither binding, so this record lost nothing.
