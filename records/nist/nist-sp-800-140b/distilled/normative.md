---
record: nist-sp-800-140b
kind: normative
title: "nist-sp-800-140b — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every requirement text in requirements.yaml that has source lines appears here verbatim under its section, as a marker that `bin/check-quotes --render` writes and `bin/check-quotes` verifies; split_of children are listed on their parent's line rather than quoted twice. Binding text that is not an entry (scope statements, normative references, definitions, abbreviations, sub-headings, captions and placeholder rows) is quoted the same way, with no id. Sections follow the source's own headings in source order; where requirements.yaml carries a skeleton locator that differs, the id line says so. requirements.yaml holds 181 entries: 13 skeleton, 40 split children, 24 from candidates (1 of them a table row), 53 hunted, 45 other table rows and 6 inferred.

## Status

The cover page (L1-38) is a withdrawal notice. What it means for every entry here is the inferred entry R-0176; the notice itself binds nothing (C-0001, rejected).

<!-- q L5 -->
> The attached publication has been withdrawn (archived), and is provided solely for historical purposes.

<!-- q L14-15 -->
> Withdrawal Note NIST SP 800-140B is withdrawn and superseded in its entirety by NIST SP 800-140Br1 (Revision 1)

## §1

<!-- q L227-229 "This" .. "conformance." -->
> This document specifies the Cryptographic Module Validation Program (CMVP) modifications of the methods to be used by a Cryptographic and Security Testing Laboratory (CSTL) to demonstrate conformance.

Scope statement (no entry).

<!-- q L229-230 "This" .. "conformity." -->
> This document also specifies the modification of documentation for providing evidence to demonstrate conformity.

Scope statement (no entry).

<!-- q L230-231 "Unless" .. "6.14." -->
> Unless otherwise specified in this document, the test requirements are specified in ISO/IEC 19790 Annex B and ISO/IEC 24759 section 6.14.

R-0025 · no candidate (hunted)

## §2

<!-- q L235 "This" .. "24759." -->
> This section identifies the normative references cited as ISO/IEC 19790 and ISO/IEC 24759.

<!-- q L235-236 "The" .. "24759:2017." -->
> The specific editions to be used are ISO/IEC 19790:2012 and ISO/IEC 24759:2017.

R-0026 · no candidate (hunted)

<!-- q L236-237 "Please" .. "2015." -->
> Please note that the version 19790:2012 referenced here includes the corrections made in 2015.

R-0027 · no candidate (hunted)

<!-- q L239-247 -->
> National Institute of Standards and Technology (2019) Security Requirements for Cryptographic Modules. (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 140-3. https://doi.org/10.6028/NIST.FIPS.140-3

The normative reference to FIPS 140-3.

## §3

<!-- q L251-252 -->
> The following terms and definitions supersede or are in addition to those defined in ISO/IEC 19790 and ISO/IEC 24759:

R-0028 · no candidate (hunted)

<!-- q L254 -->
> None added at this time.

## §4

<!-- q L258-259 -->
> The following symbols and abbreviated terms supersede or are in addition to ISO/IEC 19790 throughout this document:

R-0029 · no candidate (hunted)

<!-- q L261 -->
> CAVP Cryptographic Algorithm Validation Program

<!-- q L263 -->
> CCCS Canadian Centre for Cyber Security

<!-- q L265 -->
> CMVP Cryptographic Module Validation Program

<!-- q L267 -->
> CSD Computer Security Division

<!-- q L269 -->
> CSTL Cryptographic and Security Testing Laboratory

<!-- q L271 -->
> EFP Environmental Failure Protection

<!-- q L273 -->
> EFT Environmental Failure Testing

<!-- q L275 -->
> FIPS Federal Information Processing Standard

<!-- q L281 -->
> FISMA Federal Information Security Management/Modernization Act

<!-- q L283 -->
> NIST National Institute of Standards and Technology

<!-- q L285 -->
> SP 800-XXX NIST Special Publication 800 series document

<!-- q L287 -->
> TE Test Evidence

<!-- q L289 -->
> VE Vendor Evidence

## §5.1

<!-- q L295-301 -->
> Section 6 of this document specifies any modifications to ISO/IEC 19790 Annex B and ISO/IEC 24759 section 6.14.

R-0030 · no candidate (hunted)

## §5.2

<!-- q L305-309 "Modifications" .. "strikethrough." -->
> Modifications to ISO/IEC 24759 section 6.14 - Cryptographic module security policy - will follow a similar format as in ISO/IEC 24759. For additions to test requirements, new Test Evidence (TEs) or Vendor Evidence (VEs) will be listed by increasing the “sequence_number.” Modifications can include a combination of additions using underline and deletions using strikethrough.

R-0001 · split into R-0014, R-0015

<!-- q L309 "If" .. "change.”" -->
> If no changes are required, the paragraph will indicate “No change.”

R-0031 · C-0011

<!-- q L312-314 "Modifications" .. "deletion." -->
> Modifications are addressed by adding formatting guidance (e.g., tables, images, etc.), adding underlined text, or using strikethrough for deletion.

R-0032 · no candidate (hunted)

<!-- q L314-316 "If" .. "800-140F." -->
> If no changes are required, the paragraph will indicate “No change.” Additional guidance may also be included to address requirements presented in SP 800-140, SP 800-140A, SP 800-140C, SP 800-140D, SP 800-140E, and SP 800-140F.

R-0002 · split into R-0016, R-0017

## §6.1

<!-- q L322-323 -->
> All requirements from ISO/IEC 24759 section 6.14 and ISO/IEC 19790 Annex B apply and are required in the security policy as applicable.

R-0033 · C-0013

<!-- q L325-328 "ISO/IEC" .. "respectively." -->
> ISO/IEC 19790 Annex B uses the same section naming convention as ISO/IEC 19790 section 7 - Security requirements. For example, Annex B section B.2.1 is named “General” and B.2.2 is named “Cryptographic module specification,” which is the same as ISO/IEC 19790 section 7.1 and section 7.2, respectively.

Explains the order rule that follows (no entry).

<!-- q L328-330 "Therefore," .. "policy." -->
> Therefore, the format of the security policy shall be presented in the same order as indicated in Annex B, starting with “General” and ending with “Mitigation of other attacks.” If sections are not applicable, they shall be marked as such in the security policy.

R-0003 · split into R-0018, R-0019

<!-- q L337-338 -->
> ISO/IEC 24759 section 6.14 – Cryptographic module security policy requirements are modified as indicated below:

R-0034 · no candidate (hunted)

<!-- q L340 -->
> ● No change.

R-0035 · no candidate (hunted)

<!-- q L342 -->
> ISO/IEC 19790 Annex B requirements are modified as indicated below:

R-0036 · no candidate (hunted)

<!-- q L344-345 "The" .. "B." -->
> The additions are intended to provide further guidance on what type of information is expected for a specific requirement or set of requirements from Annex B.

R-0037 · no candidate (hunted)

<!-- q L345-346 "They" .. "purposes." -->
> They are not intended to cover all the requirements from Annex B but rather a subset for clarification purposes.

R-0038 · no candidate (hunted)

<!-- q L346-347 "The" .. "reference." -->
> The applicable Annex B requirements are included here in bulleted form for reference.

R-0039 · no candidate (hunted)

## Annex B.2.1

<!-- q L351 -->
> ● A table indicating the individual clause levels and overall level.

R-0040 · no candidate (hunted)

<!-- q L352 -->
> ● Overall Security Rating of the module and the Security Levels of individual areas.

R-0041 · no candidate (hunted)

<!-- q L358-359 -->
> ISO/IEC 24759 Section 6. FIPS 140-3 Section Title Security Level [Number Below]

R-0042 · row: B.2.1 table 1 of 1 (caption L388): header row · split into R-0043, R-0044

<!-- q L361 -->
> 1 General

R-0045 · row: B.2.1 table 1 of 1 (caption L388): row 1 of 12

<!-- q L363-364 -->
> 2 Cryptographic module specification

R-0046 · row: B.2.1 table 1 of 1 (caption L388): row 2 of 12

<!-- q L366-367 -->
> 3 Cryptographic module interfaces

R-0047 · row: B.2.1 table 1 of 1 (caption L388): row 3 of 12

<!-- q L369-370 -->
> 4 Roles, services, and authentication

R-0048 · row: B.2.1 table 1 of 1 (caption L388): row 4 of 12

<!-- q L372 -->
> 5 Software/Firmware security

R-0049 · row: B.2.1 table 1 of 1 (caption L388): row 5 of 12

<!-- q L374 -->
> 6 Operational environment

R-0050 · row: B.2.1 table 1 of 1 (caption L388): row 6 of 12

<!-- q L376 -->
> 7 Physical security

R-0051 · row: B.2.1 table 1 of 1 (caption L388): row 7 of 12

<!-- q L378 -->
> 8 Non-invasive security

R-0052 · row: B.2.1 table 1 of 1 (caption L388): row 8 of 12

<!-- q L380-381 -->
> 9 Sensitive security parameter management

R-0053 · row: B.2.1 table 1 of 1 (caption L388): row 9 of 12

<!-- q L383 -->
> 10 Self-tests

R-0054 · row: B.2.1 table 1 of 1 (caption L388): row 10 of 12

<!-- q L385 -->
> 11 Life-cycle assurance

R-0055 · row: B.2.1 table 1 of 1 (caption L388): row 11 of 12

<!-- q L387 -->
> 12 Mitigation of other attacks

R-0056 · row: B.2.1 table 1 of 1 (caption L388): row 12 of 12

<!-- q L388 -->
> Table x – Security Levels

Caption of B.2.1 table 1.

## Annex B.2.2

<!-- q L399 -->
> ● Hardware, Software, Firmware, or Hybrid designation:

R-0057 · no candidate (hunted)

<!-- q L400-402 -->
> o For software, firmware, and hybrid cryptographic modules, list the operating system(s) the module was tested on and the operating system(s) that the vendor affirms can be used by the module.

R-0004

<!-- q L403 -->
> [For Software/Firmware/Hybrid Module]

R-0058 · C-0014

<!-- q L405-406 -->
> # Operating Hardware Platform Processor PAA/Acceleration System

R-0059 · row: B.2.2 table 1 of 7 (caption L417): header row · split into R-0060, R-0061

<!-- q L408-416 -->
> 1 2 …

Placeholder rows of B.2.2 table 1.

<!-- q L417 -->
> Table x - Tested Operational Environments

Caption of B.2.2 table 1.

<!-- q L420 -->
> # Operating System Hardware Platform

R-0062 · row: B.2.2 table 2 of 7 (caption L427): header row

<!-- q L422-426 -->
> 1 2 …

Placeholder rows of B.2.2 table 2.

<!-- q L427 -->
> Table x – Vendor Affirmed Operational Environments

Caption of B.2.2 table 2.

<!-- q L431 -->
> [For Hardware Module]

R-0063 · no candidate (hunted)

<!-- q L433-436 -->
> Model Hardware Firmware Version Distinguishing Features 1 [Part Number and Version]

R-0064 · row: B.2.2 table 3 of 7 (caption L441): header row · split into R-0065, R-0066, R-0067, R-0068

<!-- q L441 -->
> Table x - Cryptographic Module Tested Configuration

Caption of B.2.2 table 3.

<!-- q L445-447 -->
> 1 Examples may be ports and interfaces, memory storage devices and sizes, field replaceable and stationary accessories (power supplies, fans), etc.

R-0069 · no candidate (hunted)

<!-- q L454-456 -->
> ● Table of all security functions with specific key strengths employed for approved services, as well as the implemented modes of operation (e.g. CBC, CCM), if appropriate.

R-0070 · no candidate (hunted)

<!-- q L458-460 -->
> CAVP Algorithm Mode/Method Description / Key Size(s) / Key Use / Function and Standard Strength(s) Cert 23

R-0071 · row: B.2.2 table 4 of 7 (caption L465): header row · split into R-0072, R-0073, R-0074

<!-- q L465 -->
> Table x - Approved Algorithms

Caption of B.2.2 table 4.

<!-- q L471 -->
> Algorithm Caveat Use / Function

R-0075 · row: B.2.2 table 5 of 7 (caption L476): header row

<!-- q L476 -->
> Table x – Non-Approved Algorithms Allowed in the Approved Mode of Operation

Caption of B.2.2 table 5.

<!-- q L479 -->
> Algorithm 4 Caveat Use / Function

R-0076 · row: B.2.2 table 6 of 7 (caption L484): header row

<!-- q L484 -->
> Table x – Non-Approved Algorithms Allowed in the Approved Mode of Operation with No Security Claimed

Caption of B.2.2 table 6.

<!-- q L488-492 -->
> 2 If applicable, insert a footnote detailing any mode/key-size that is present on a listed CAVP certificate but is not used by any service, or state something to the effect of: There are algorithms, modes, and key/moduli sizes that have been CAVP-tested but are not used by any approved service of the module. Only the algorithms, modes/methods, and key lengths/curves/moduli shown in this table are used by an approved service of the module.

R-0077 · no candidate (hunted)

<!-- q L494 -->
> 3 This table includes vendor-affirmed algorithms that are approved but CAVP testing is not yet available.

R-0078 · no candidate (hunted)

<!-- q L497-499 -->
> 4 These algorithms do not claim any security and are not used to meet FIPS 140-3 requirements. Therefore, SSPs do not map to these algorithms.

R-0079 · no candidate (hunted)

<!-- q L507 -->
> Algorithm/Function Use/Function

R-0080 · row: B.2.2 table 7 of 7 (caption L512): header row

<!-- q L512 -->
> Table x – Non-Approved Algorithms Not Allowed in the Approved Mode of Operation

Caption of B.2.2 table 7.

<!-- q L514 "●" .. "module." -->
> ● Illustrative diagram, schematic or photograph of the module.

R-0081 · no candidate (hunted)

<!-- q L514-515 "A" .. "module." -->
> A photograph is included for a hardware module.

R-0082 · C-0015

<!-- q L515-517 "If" .. "versions." -->
> If the security policy encompasses multiple versions of the module, each version is represented separately or annotated that the representation is illustrated for all versions.

R-0083 · C-0016

<!-- q L517-518 "For" .. "illustrates:" -->
> For a software or firmware cryptographic module, the security policy includes a block diagram that illustrates:

R-0084 · no candidate (hunted)

<!-- q L519-527 -->
> o the location of the logical object of the software or firmware module with respect to the operating system, other supporting applications and the cryptographic boundary so that all the logical and physical layers between the logical object and the cryptographic boundary are clearly defined; and

R-0085 · C-0017

<!-- q L528-530 -->
> o the interactions of the logical object of the software or firmware module with the operating system and other supporting applications resident within the cryptographic boundary.

R-0086 · C-0018

<!-- q L531 -->
> ● Block Diagram, as applicable.

R-0087 · C-0018

<!-- q L532 -->
> [For Software/Firmware/Hybrid Module]

R-0088 · C-0019

<!-- q L537 -->
> Figure x – Logical [cryptographic] boundary [and physical boundary if combined]

R-0089 · row: B.2.2 figure 1 of 3: caption

<!-- q L542 -->
> Figure x – Physical boundary [if separated from logical boundary]

R-0090 · row: B.2.2 figure 2 of 3: caption

<!-- q L549 -->
> [For Hardware/Hybrid 5 Module]

R-0091 · no candidate (hunted)

<!-- q L554 -->
> Figure x – [Model 1]

R-0092 · row: B.2.2 figure 3 of 3: caption

<!-- q L556 -->
> ● Overall security design and the rules of operation 6

R-0093 · no candidate (hunted)

## Annex B.2.3

<!-- q L563 -->
> ● Table listing of all ports and interfaces (physical and logical).

R-0094 · C-0020

<!-- q L564 -->
> ● Define the information passing over the five logical interfaces.

R-0095 · C-0020

<!-- q L565 -->
> ● Specify physical ports and data that pass over them.

R-0096 · C-0020

<!-- q L567-568 -->
> Physical port 7 Logical interface Data that passes over port/interface

R-0097 · row: B.2.3 table 1 of 1 (caption L573): header row · split into R-0098, R-0099

<!-- q L573 -->
> Table x – Ports and Interfaces

Caption of B.2.3 table 1.

## Annex B.2.4

<!-- q L580 -->
> ● Specify all roles.

R-0100 · no candidate (hunted)

<!-- q L581 -->
> ● Table of Roles, with corresponding service with input and output.

R-0101 · no candidate (hunted)

<!-- q L585 -->
> 5 The image will show the disjoint hardware component of the hybrid module

R-0102 · no candidate (hunted)

<!-- q L588 -->
> 6 As part of this requirement, algorithm-specific guidance, rules, and security policy-specific requirements shall be included.

R-0005 · requirements.yaml locator reads §5

<!-- q L591 "7" .. "images/diagrams." -->
> 7 The physical ports here should map to the physical ports shown in the module images/diagrams.

R-0006 · requirements.yaml locator reads §5

<!-- q L591-593 "If" .. "differences." -->
> If the ports are different per module within the same submission, then this table should indicate the differences.

R-0103 · no candidate (hunted) · split into R-0007

<!-- q L601 -->
> Role Service Input Output

R-0104 · row: B.2.4 table 1 of 4 (caption L606): header row

<!-- q L606 -->
> Table x – Roles, Service Commands, Input and Output

Caption of B.2.4 table 1.

<!-- q L608-609 -->
> ● Specify each authentication method, whether the method is identity or role-based, and whether the method is required.

R-0105 · C-0021

<!-- q L610 -->
> ● How is the strength of authentication requirement met?

R-0106 · C-0021

<!-- q L616 -->
> Role Authentication Method Authentication Strength

R-0107 · row: B.2.4 table 2 of 4 (caption L621): header row

<!-- q L621 -->
> Table x – Roles and Authentication

Caption of B.2.4 table 2.

<!-- q L623-629 "●" .. "uses." -->
> ● Separately list the security and non-security services, both approved and non-approved. ● For each service, list the service name, a concise description of the service purpose and/or use (the service name alone may, in some instances, provide this information), a list of approved security functions (algorithm(s), key management technique(s), or authentication technique) used by or implemented through the invocation of the service, and a list of the SSPs associated with the service or with the approved security function(s) it uses.

R-0008 · split into R-0020, R-0021, R-0022 · requirements.yaml locator reads §5

<!-- q L629-631 "For" .. "role." -->
> For each operator role authorized to use the service, describe the individual access rights to all SSPs including information describing the method used to authenticate each role.

R-0108 · no candidate (hunted)

<!-- q L641-643 -->
> Service Description Approved Keys and/or SSPs Roles Access rights Indicator Security to Keys Functions 8 and/or SSPs 9

R-0109 · row: B.2.4 table 3 of 4 (caption L648): header row · split into R-0110, R-0111, R-0112

<!-- q L648 -->
> Table x – Approved Services

Caption of B.2.4 table 3.

<!-- q L650 -->
> G = Generate: The module generates or derives the SSP.

R-0113 · row: B.2.4 table 3 of 4 (caption L648): access-right legend, G

<!-- q L652 -->
> R = Read: The SSP is read from the module (e.g. the SSP is output).

R-0114 · row: B.2.4 table 3 of 4 (caption L648): access-right legend, R

<!-- q L658 -->
> W = Write: The SSP is updated, imported, or written to the module.

R-0115 · row: B.2.4 table 3 of 4 (caption L648): access-right legend, W

<!-- q L660 -->
> E = Execute: The module uses the SSP in performing a cryptographic operation.

R-0116 · row: B.2.4 table 3 of 4 (caption L648): access-right legend, E

<!-- q L662 -->
> Z = Zeroise: The module zeroises the SSP.

R-0117 · row: B.2.4 table 3 of 4 (caption L648): access-right legend, Z

<!-- q L666-667 -->
> Service Description Algorithms Role Indicator Accessed 10

R-0118 · row: B.2.4 table 4 of 4 (caption L672): header row · split into R-0119, R-0120

<!-- q L672 -->
> Table x – Non-Approved Services

Caption of B.2.4 table 4.

## Annex B.2.5

<!-- q L676 -->
> ● No change.

R-0121 · no candidate (hunted)

<!-- q L681-683 -->
> 8 Each algorithm shown in the Approved Algorithms and Non-Approved Algorithms Allowed in the Approved Mode of Operation tables should map to at least one service

R-0122 · no candidate (hunted) · split into R-0009

<!-- q L685 -->
> 9 Use the letters (G, R, W, E, Z) as defined under this table when listing the access rights of each SSP.

R-0123 · no candidate (hunted)

<!-- q L688-690 -->
> 10 Each algorithm shown in the Non-Approved Algorithms Not Allowed in the Approved Mode of Operation table should map to at least one service.

R-0124 · no candidate (hunted) · split into R-0010

## Annex B.2.6

<!-- q L698 -->
> ● No change.

R-0125 · no candidate (hunted)

## Annex B.2.7

<!-- q L702 -->
> [For physical Security Level 2 and above]

R-0126 · no candidate (hunted)

<!-- q L704-705 -->
> ● Specify the physical security mechanisms that are implemented in the module (e.g., tamper-evident seals, locks, tamper response and zeroisation switches, and alarms).

R-0127 · C-0022

<!-- q L706-708 -->
> ● Specify the actions required by the operator(s) to ensure that the physical security is maintained (e.g. periodic inspection of tamper-evident seals or testing of tamper response and zeroisation switches).

R-0128 · C-0022

<!-- q L710-716 -->
> Physical Security Recommended Frequency of Inspection/Test Guidance Details Mechanism Inspection/Test

R-0129 · C-0023 · row: B.2.7 table 1 of 3 (caption L721): header row · split into R-0130, R-0131

<!-- q L721 -->
> Table x – Physical Security Inspection Guidelines

Caption of B.2.7 table 1.

<!-- q L725-728 "o" .. "specified." -->
> o Specify the following information if the module requires operator applied tamper evident seals or security appliances that the operator will apply or modify over the lifecycle of the module: The reference photo or illustrations required in B 2.2 will reflect the module configured or constructed as specified.

R-0132 · C-0024

<!-- q L728-729 "Additional" .. "configurations." -->
> Additional photos/illustrations may be provided to reflect other configurations.

R-0011

<!-- q L730-732 "o" .. "needed." -->
> o If filler panels are needed to cover unpopulated slots or openings to meet the opacity requirements, they will be included in the photo or illustrations with tamper seals affixed as needed.

R-0133 · C-0025

<!-- q L732-733 "The" .. "parts." -->
> The filler panels will be included in the list of parts.

R-0134 · C-0026

<!-- q L734-735 -->
> o Photos or illustrations will indicate the precise placement of any tamper evident seal or security appliance needed to meet the physical security requirements.

R-0135 · C-0027

<!-- q L736-737 "o" .. "screens)." -->
> o The total number of tamper-evident seals or security appliances that are needed will be indicated (e.g., five tamper-evident seals and two opacity screens).

R-0136 · C-0028

<!-- q L737-741 "The" .. "illustrated)." -->
> The photos or illustrations which provide instruction on the precise placement will have each item numbered in the photo or illustration and will equal the total number indicated (the actual tamper-evident seals or security appliances are not required to be numbered as illustrated).

R-0137 · C-0029

<!-- q L752 -->
> Figure x – Module 1 Seal Application Locations

R-0138 · row: B.2.7 figure 1 of 2: caption

<!-- q L758 -->
> Figure x – Module 2 Seal Application Locations

R-0139 · row: B.2.7 figure 2 of 2: caption

<!-- q L762 -->
> [For physical Security Level 3 and above]

R-0140 · no candidate (hunted)

<!-- q L764-766 -->
> Temperature or voltage Specify EFP 11 or EFT Specify if this condition measurement results in a shutdown or zeroisation

R-0141 · row: B.2.7 table 2 of 3 (caption L775): header row · split into R-0142, R-0143, R-0144

<!-- q L768 -->
> Low Temperature

R-0145 · row: B.2.7 table 2 of 3 (caption L775): row 1 of 4

<!-- q L770 -->
> High Temperature

R-0146 · row: B.2.7 table 2 of 3 (caption L775): row 2 of 4

<!-- q L772 -->
> Low Voltage

R-0147 · row: B.2.7 table 2 of 3 (caption L775): row 3 of 4

<!-- q L774 -->
> High Voltage

R-0148 · row: B.2.7 table 2 of 3 (caption L775): row 4 of 4

<!-- q L775 -->
> Table x – EFP/EFT

Caption of B.2.7 table 2.

<!-- q L780 -->
> 11 EFP is required for modules with physical Security Level 4.

R-0149 · C-0030

<!-- q L789-790 -->
> [For modules covered by strong or hard conformal or non-conformal enclosures, coatings, or potting materials]

R-0150 · no candidate (hunted)

<!-- q L792 -->
> Hardness tested temperature measurement

R-0151 · row: B.2.7 table 3 of 3 (caption L797): header row

<!-- q L794 -->
> Low Temperature

R-0152 · row: B.2.7 table 3 of 3 (caption L797): row 1 of 2

<!-- q L796 -->
> High Temperature

R-0153 · row: B.2.7 table 3 of 3 (caption L797): row 2 of 2

<!-- q L797 -->
> Table x –Hardness testing temperature ranges 12

Caption of B.2.7 table 3; the 12 is the mark of footnote 12.

## Annex B.2.8

<!-- q L801 -->
> ● No change.

R-0154 · no candidate (hunted)

## Annex B.2.9

<!-- q L809-812 -->
> ● Provide a key table specifying the key type(s), strength(s) in bits, security function(s), security function certification number(s), where and how the key(s) is generated, whether the key(s) is imported or exported, any SSP generation and establishment method used, and indicate any related keys.

R-0155 · no candidate (hunted)

<!-- q L813 -->
> ● Present a table of other SSPs and how they are generated.

R-0156 · no candidate (hunted)

<!-- q L814 -->
> ● Specify the approved and non-approved random bit generators.

R-0157 · no candidate (hunted)

<!-- q L815 -->
> ● Describe the uses of RBG output(s).

R-0158 · no candidate (hunted)

<!-- q L816 -->
> ● Specify the electronic and manual key SSP I/O method(s) 13.

R-0159 · no candidate (hunted)

<!-- q L817 -->
> ● Specify the SSP storage technique(s).

R-0160 · no candidate (hunted)

<!-- q L818-819 -->
> ● Specify the unprotected SSP zeroisation method(s) and rationale and operator initiation capability.

R-0161 · no candidate (hunted)

<!-- q L820-823 -->
> Key/SSP Strength Security Gener- Import Establish- Storage Zero- Use & Name/ Function ation /Export ment isation related Type and Cert. keys Number

R-0162 · row: B.2.9 table 1 of 2 (caption L828): header row · split into R-0163, R-0164, R-0165, R-0166

<!-- q L828 -->
> Table x – SSPs 14

Caption of B.2.9 table 1; the 14 is the mark of footnote 14.

<!-- q L832-834 -->
> 12 The module is hardness tested at the lowest and highest temperatures within the module's intended temperature range of operation.

R-0167 · no candidate (hunted)

<!-- q L836 -->
> 13 This should be specified in the “Import/Export” column in the SSP table.

R-0012

<!-- q L839-847 -->
> 14 The SSPs should map to the Approved Algorithms and CAVP Certificates and Cryptographic Algorithms Allowed in the ● Specify the RBG entropy source(s).

R-0013 · split into R-0023, R-0024

<!-- q L849-850 -->
> Entropy sources Minimum number of Details bits of entropy 15

R-0168 · row: B.2.9 table 2 of 2 (caption L855): header row · split into R-0169, R-0170

<!-- q L855 -->
> Table x – Non-Deterministic Random Number Generation Specification

Caption of B.2.9 table 2.

## Annex B.2.10

<!-- q L859 -->
> ● No change.

R-0171 · no candidate (hunted)

## Annex B.2.11

<!-- q L866 -->
> ● No change.

R-0172 · no candidate (hunted)

## Annex B.2.12

<!-- q L869 -->
> ● No change.

R-0173 · no candidate (hunted)

<!-- q L874 -->
> Approved Mode of Operation tables in section B.2.2

R-0174 · no candidate (hunted)

<!-- q L875-877 -->
> 15 That is, the minimum number of bits of entropy generated, requested, and/or believed to have been loaded, with a justification of the stated amount.

R-0175 · no candidate (hunted)

## Document Revisions

L881-886 print a rotated Document Revisions table: a header (Date, Change) and no rows. Not normative; pdftotext interleaves it with the running header.

## Inferred

Kind inferred, in our words, in requirements.yaml with derived_from: R-0176, R-0177, R-0178, R-0179, R-0180, R-0181.

## Source defects

**SD-1** — reader, fixed: footnotes 1, 2, 4 and 5 (L445, L488, L497, L585) begin with a number the table of contents lists, so the pass-1 PDF reading keyed each as a heading (§1, §2, §4, §5). The skeleton therefore never cut those lines into sentences — footnote 1's may is the verbal form its reconciliation could not place — and filed R-0005 to R-0008 under §5 and 6 candidates (C-0015, C-0016, C-0017, C-0018, C-0019, C-0021) under §4 and §5. 63d708e fixed the reading (a numbered heading the table of contents lists must agree with the title it has there); those locators were then re-derived from the fixed reading, and bin/check-locators finds every entry in its clause. Of the skeleton's 13 sentences none changes under the fixed reading; a re-run adds footnote 1's, which R-0069 already holds.

**SD-2** — source: every table is numbered Table x and every figure Figure x; the placeholders were never numbered, so no table or figure can be cited by number. Entries name them by clause and position, with the caption's line.

**SD-3** — rendering: footnote 14 is split across a page in the rendering. Its head (L839) is welded by the skeleton to a B.2.9 bullet printed at the top of the next page (L847, R-0013), and its last words are printed after B.2.12 (L874, R-0174).

**SD-4** — source: a B.2.7 sub-item refers to the reference photo required in B 2.2 (L727), a misprint for B.2.2.

**SD-5** — source: the B.2.9 heading reads sensitive security parameters management, the B.2.1 table row 9 sensitive security parameter management.

**SD-6** — rendering, not source: §5.2 marks additions by underline and deletions by strikethrough, which the pdftotext rendering cannot carry. §6.1 says the bullets reproduce Annex B for reference, but which words of an item, or which sub-items, the CMVP added cannot be read from the rendering.

**SD-7** — reader: pdftotext prints a blank line inside footnotes 1 (L446), 2 (L489), 4 (L498), 7 (L592), 8 (L682), 10 (L689), 12 (L833), 15 (L876), and the PDF reading takes each as a paragraph break (until 63d708e it took the blank lines around the mid-page sidebar as one too); the skeleton cut R-0007, R-0009 and R-0010 out of their sentences, and the whole sentences are entries of which they are split_of parts.
