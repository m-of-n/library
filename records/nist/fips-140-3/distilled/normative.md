---
record: fips-140-3
kind: normative
title: "fips-140-3 — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every stated requirement in requirements.yaml with source lines appears here verbatim under its section, as a marker that `bin/check-quotes --render` writes and `bin/check-quotes` verifies; split_of children are named on their parent's line rather than quoted twice. The keyword-less binding text pass 1 added (candidate-stated and hunted) is interleaved in source order, and binding text that is not an entry (¶3's sentence on who runs the CMVP, Figure 1, the §3.2 document titles, Table 1) is quoted where it falls with a line saying why. requirements.yaml holds 88 entries: 14 skeleton, 17 split children (13 of them main's AREA and RQ ids), 14 from candidates, 37 hunted, 6 inferred.

The announcement paragraphs ¶1 to ¶14 bind where they say who must do what: ¶3, ¶6, ¶7, ¶9, ¶10, ¶11, ¶12 and ¶13 carry entries; ¶1, ¶2, ¶4, ¶5, ¶8 and ¶14 only name the standard, its category, approver, maintainer, the affixed text and where to get copies. The eleven security areas are listed in ¶3 (and the Abstract), not in the body: the body's §3 lists the documents that modify ISO/IEC 19790 and ISO/IEC 24759.

## ¶3

<!-- q L98-100 "This" .. "information)." -->
> This standard specifies the security requirements that will be satisfied by a cryptographic module utilized within a security system protecting sensitive but unclassified information (hereafter referred to as sensitive information).

R-0015 · candidate C-0008

<!-- q L100-103 "The" .. "employed." -->
> The standard provides four increasing, qualitative levels of security: Level 1, Level 2, Level 3, and Level 4. These levels are intended to cover the wide range of potential applications and environments in which cryptographic modules may be employed.

R-0001 · split: R-0016 (none), R-0017 (may)

<!-- q L104-108 "These" .. "attacks." -->
> These areas include cryptographic module specification; cryptographic module interfaces; roles, services, and authentication; software/firmware security; operating environment; physical security; non-invasive security; sensitive security parameter management; self-tests; life-cycle assurance; and mitigation of other attacks.

R-0018 · candidate C-0010 · split: AREA-01 (none), AREA-02 (none), AREA-03 (none), AREA-04 (none), AREA-05 (none), AREA-06 (none), AREA-07 (none), AREA-08 (none), AREA-09 (none), AREA-10 (none), AREA-11 (none)

<!-- q L108-109 "This" .. "entirety." -->
> This standard supersedes FIPS 140-2, Security Requirements for Cryptographic Modules, in its entirety.

R-0019 · candidate C-0011

<!-- q L111-112 -->
> The Cryptographic Module Validation Program (CMVP) validates cryptographic modules to Federal Information Processing Standard (FIPS) 140-3 and other cryptography-based standards.

R-0020 · no candidate (hunted)

<!-- q L113-114 "The CMVP is" .. "Cyber Security." -->
> The CMVP is a joint effort between the National Institute of Standards and Technology and the Canadian Centre for Cyber Security.

Not an entry: names the two countries whose Federal agencies R-0021 says accept a validated module.

<!-- q L114-116 "Modules" .. "(Canada)." -->
> Modules validated as conforming to FIPS 140-3 are accepted by the Federal agencies of both countries for the protection of sensitive information (United States) or Designated Information (Canada).

R-0021 · no candidate (hunted)

<!-- q L120-121 "In" .. "tested." -->
> In the CMVP, vendors of cryptographic modules use independent, accredited Cryptographic and Security Testing (CST) laboratories to have their modules tested.

R-0022 · no candidate (hunted)

<!-- q L121-123 "National" .. "testing." -->
> National Voluntary Laboratory Accreditation Program (NVLAP) accredited laboratories perform cryptographic module compliance/conformance testing.

R-0023 · no candidate (hunted)

## ¶6

<!-- q L134-137 "This" .. "104-106." -->
> This standard is applicable to all Federal agencies that use cryptography-based security systems to protect sensitive information in computer and telecommunication systems (including voice systems) as defined in Section 5131 of the Information Technology Management Reform Act of 1996, Public Law 104-106.

R-0024 · candidate C-0015

<!-- q L137-139 "This" .. "contract." -->
> This standard shall be used in designing and implementing cryptographic modules that Federal departments and agencies operate or are operated for them under contract.

R-0002

<!-- q L139-140 "Cryptographic" .. "standard." -->
> Cryptographic modules that have been approved for classified use may be used in lieu of modules that have been validated against this standard.

R-0003

<!-- q L140-141 "The" .. "organizations." -->
> The adoption and use of this standard is available to private and commercial organizations.

R-0025 · candidate C-0016

## ¶7

<!-- q L143-146 "Cryptography-based" .. "environments)." -->
> Cryptography-based security systems may be utilized in various computer and telecommunication applications (e.g., data storage, access control and personal identification, network communications, radio, facsimile, and video) and in various environments (e.g., centralized computer facilities, office environments, and hostile environments).

R-0004

<!-- q L149-152 "The" .. "provide." -->
> The security level to which a cryptographic module is validated must be chosen to provide a level of security appropriate for the security requirements of the application and environment in which the module will be utilized and the security services that the module will provide.

R-0005 · same sentence: RQ-02 (id carried from main)

<!-- q L152-154 "The" .. "level." -->
> The security requirements for a particular security level include both the security requirements specific to that level and the security requirements that apply to all modules regardless of the level.

R-0026 · candidate C-0019

## ¶9

<!-- q L159-161 "This" .. "thereof." -->
> This standard covers implementations of cryptographic modules including, but not limited to, hardware components or modules, software/firmware programs or modules or any combination thereof.

R-0027 · candidate C-0023

<!-- q L161-162 "Cryptographic" .. "standard." -->
> Cryptographic modules that are validated under the CMVP will be considered as conforming to this standard.

R-0028 · candidate C-0024

<!-- q L162-162 "Information" .. "from the" -->
> Information about the CMVP can be obtained from the

R-0006

## ¶10

<!-- q L169-172 "Cryptographic" .. "information." -->
> Cryptographic modules that conform to this standard shall employ Approved security functions such as cryptographic algorithms, cryptographic key management techniques, and authentication techniques that have been approved for protecting Federal government sensitive information.

R-0007 · same sentence: RQ-01 (id carried from main)

<!-- q L172-173 "Approved" .. "either:" -->
> Approved security functions include those that are either:

R-0029 · candidate C-0026

<!-- q L175-175 -->
> a. specified in a Federal Information Processing Standard (FIPS),

R-0030 · no candidate (hunted)

<!-- q L181-182 -->
> b. adopted in a FIPS and specified either in an appendix to the FIPS or in a document referenced by the FIPS,

R-0073 · no candidate (hunted)

<!-- q L183-183 -->
> c. specified in NIST SP 800-140C as an Approved security function, or

R-0031 · no candidate (hunted)

<!-- q L184-185 -->
> d. specified in NIST SP 800-140D as an Approved sensitive security parameter establishment method.

R-0032 · no candidate (hunted)

## ¶11

<!-- q L187-190 "Questions" .. "20899-8900." -->
> Questions concerning the content and specifications of this standard should be addressed to: Director, Information Technology Laboratory, ATTN: FIPS 140-3 Interpretation, National Institute of Standards and Technology, 100 Bureau Drive, Stop 8900, Gaithersburg, MD 20899-8900.

R-0008

<!-- q L190-192 "Resolution" .. "Security." -->
> Resolution of questions regarding this standard will be provided by the validation authorities at the National Institute of Standards and Technology and the Canadian Centre for Cyber Security.

R-0033 · candidate C-0028

## ¶12

<!-- q L194-195 "This" .. "Commerce." -->
> This standard becomes effective six months after approval by the Secretary of Commerce.

R-0034 · candidate C-0030

<!-- q L195-196 "A" .. "testing." -->
> A minimum transition period of 6 months after approval is provided for testing labs to develop and implement FIPS 140-3 testing.

R-0035 · candidate C-0031

<!-- q L196-197 "A" .. "validation." -->
> A test report for modules demonstrating compliance will be submitted to the CMVP for review and validation.

R-0036 · candidate C-0032

<!-- q L198-200 "Agencies" .. "list." -->
> Agencies should develop plans for the acquisition of products that are compliant with FIPS 140-3; however, agencies may purchase any of the products on the CMVP validated modules list.

R-0009 · split: R-0037 (should), R-0038 (may)

<!-- q L200-201 "(Note:" .. "decisions." -->
> (Note: the CMVP Historical list should not be used for procurement decisions.

R-0010

<!-- q L202-203 "Figure" .. "begin." -->
> Figure 1 summarizes the CMVP implementation schedule when FIPS 140-3 testing may begin.

R-0011

<!-- q L206-229 -->
> FIPS 140-2 FIPS 140-3 APPROVAL DATE OF FIPS 140-3 EFFECTIVE DATE OF FIPS 140-3 (6 months after approval date) FIPS 140-3 TESTING BEGINS (18 months after approval date) FIPS 140-2 TESTING ENDS FUTURE Figure 1. FIPS 140-3 Implementation Schedule

Figure 1, whole. Not an entry: its schedule lines are R-0039, R-0040, R-0041, and its other labels (the two column heads, APPROVAL DATE, FUTURE, the caption) state nothing on their own.

<!-- q L211-212 -->
> EFFECTIVE DATE OF FIPS 140-3 (6 months after approval date)

R-0039 · no candidate (hunted)

<!-- q L217-218 -->
> FIPS 140-3 TESTING BEGINS (18 months after approval date)

R-0040 · no candidate (hunted)

<!-- q L223-223 -->
> FIPS 140-2 TESTING ENDS

R-0041 · no candidate (hunted)

## ¶13

<!-- q L243-245 "The" .. "accepted." -->
> The operator of a cryptographic module is responsible for ensuring that the security provided by a module is sufficient and acceptable to the owner of the information that is being protected and that any residual risk is acknowledged and accepted.

R-0042 · no candidate (hunted)

<!-- q L245-246 "The" .. "acceptable." -->
> The responsible authority in each agency shall ensure that the security of the system is sufficient and acceptable.

R-0012

<!-- q L248-249 "A" .. "technology." -->
> A standard of this nature must be flexible enough to adapt to advancements and innovations in science and technology.

R-0013

<!-- q L249-250 "New" .. "changes." -->
> New or revised requirements may be needed to meet technological and economic changes.

R-0014

## §1

<!-- q L280-284 -->
> This standard specifies the security requirements for a cryptographic module utilized within a security system protecting sensitive information in computer and telecommunication systems (including voice systems) as defined in Section 5131 of the Information Technology Management Reform Act of 1996, (Public Law 104-106) and the Federal Information Security Management Act of 2002 (Public Law 107-347).

R-0043 · no candidate (hunted)

<!-- q L303-303 "FIPS" .. "FIPS140-2." -->
> FIPS 140-3 supersedes FIPS140-2.

R-0044 · no candidate (hunted)

<!-- q L303-304 "FIPS 140-3 aligns" .. "authority)." -->
> FIPS 140-3 aligns with ISO/IEC 19790:2012(E) and includes modifications of the Annexes that are allowed to CMVP (as a validation authority).

R-0045 · no candidate (hunted)

<!-- q L304-307 "The" .. "5.2." -->
> The testing for these requirements will be in accordance with ISO/IEC 24759:2017(E), with the modifications, additions or deletions of vendor evidence and testing allowed as a validation authority under paragraph 5.2.

R-0046 · no candidate (hunted)

## §2

<!-- q L317-318 "It" .. "permitted." -->
> It is currently in the best interest to use these standards, superseding those sections where national standards are permitted.

R-0047 · no candidate (hunted)

<!-- q L318-319 "Therefore," .. "24759:2017(E)." -->
> Therefore, FIPS 140-3 is based on ISO/IEC 19790:2012/Cor.1:2015(E) and ISO/IEC 24759:2017(E).

R-0048 · candidate C-0046

<!-- q L319-320 "The" .. "modified." -->
> The following documents identify those elements that are superseded or modified.

R-0049 · no candidate (hunted)

## §3.1

<!-- q L332-333 "When" .. "applies." -->
> When referring to ISO/IEC 19790:2012(E) and ISO/IEC 24759:2017(E), the latest edition of the referenced document (including any amendments) applies.

R-0050 · no candidate (hunted)

<!-- q L333-334 "“NIST" .. "document." -->
> “NIST SP” denotes a NIST Special Publication series document.

R-0051 · no candidate (hunted)

<!-- q L334-335 "For" .. "applies." -->
> For those NIST SP documents that are not referenced by a specific version or date, the latest edition of the referenced document (including any amendments) applies.

R-0052 · no candidate (hunted)

## §3.2

<!-- q L339-340 -->
> These documents form the technical requirements and the basis for the testing methods of this FIPS.

R-0053 · no candidate (hunted)

<!-- q L342-343 -->
> ISO/IEC 19790:2012(E), Information technology — Security techniques — Security requirements for cryptographic modules

Not an entry: the first of the two documents R-0053 names.

<!-- q L345-346 -->
> ISO/IEC 24759:2017(E), Information technology — Security techniques — Test requirements for cryptographic modules

Not an entry: the second of the two documents R-0053 names.

## §3.3

<!-- q L350-351 "These" .. "authority." -->
> These documents modify the annex requirements of the technical requirements document ISO/IEC 19790:2012(E) as specified by the CMVP validation authority.

R-0054 · no candidate (hunted)

<!-- q L354-355 -->
> NIST SP 800-140A modifies: ISO/IEC 19790:2012(E) CMVP Documentation Requirements Annex A

R-0055 · no candidate (hunted)

<!-- q L356-357 -->
> NIST SP 800-140B modifies: ISO/IEC 19790:2012(E) CMVP Security Policy Requirements Annex B

R-0056 · no candidate (hunted)

<!-- q L358-359 -->
> NIST SP 800-140C modifies: ISO/IEC 19790:2012(E) CMVP Approved Security Functions Annex C

R-0057 · no candidate (hunted)

<!-- q L360-363 -->
> NIST SP 800-140D modifies: ISO/IEC 19790:2012(E) CMVP Approved Sensitive Security Annex D Parameter Generation and Establishment Methods

R-0058 · no candidate (hunted)

<!-- q L364-366 -->
> NIST SP 800-140E modifies: ISO/IEC 19790:2012(E) CMVP Approved Authentication Annex E Mechanisms

R-0059 · no candidate (hunted)

<!-- q L367-369 -->
> NIST SP 800-140F modifies: ISO/IEC 19790:2012(E) CMVP Approved Non-Invasive Attack Annex F Mitigation Test Metrics

R-0060 · no candidate (hunted)

## §3.4

<!-- q L380-381 "These" .. "authority." -->
> These documents modify the vendor documentation and testing requirements of ISO/IEC 24759:2017(E) as specified by the CMVP validation authority.

R-0061 · no candidate (hunted)

<!-- q L383-385 -->
> NIST SP 800-140 modifies: ISO/IEC 24759:2017(E) FIPS 140-3 Derived Test Requirements (6.1 through 6.12) (DTR)

R-0062 · no candidate (hunted)

<!-- q L386-387 -->
> NIST SP 800-140A modifies: ISO/IEC 24759:2017(E) CMVP Documentation Requirements (6.13)

R-0063 · no candidate (hunted)

<!-- q L388-389 -->
> NIST SP 800-140B modifies: ISO/IEC 24759:2017(E) CMVP Security Policy Requirements (6.14)

R-0064 · no candidate (hunted)

<!-- q L390-391 -->
> NIST SP 800-140C modifies: ISO/IEC 24759:2017(E) CMVP Approved Security Functions (6.15)

R-0065 · no candidate (hunted)

<!-- q L392-395 -->
> NIST SP 800-140D modifies: ISO/IEC 24759:2017(E) CMVP Approved Sensitive Security (6.16) Parameter Generation and Establishment Methods

R-0066 · no candidate (hunted)

<!-- q L396-397 -->
> NIST SP 800-140E modifies: ISO/IEC 24759:2017(E) CMVP Approved Authentication Mechanisms (6.17)

R-0067 · no candidate (hunted)

<!-- q L398-400 -->
> NIST SP 800-140F modifies: ISO/IEC 24759:2017(E) CMVP Approved Non-Invasive Attack (6.18) Mitigation Test Metrics

R-0068 · no candidate (hunted)

<!-- q L401-420 -->
> Table 1: NIST SPs that Modify ISO/IEC Standards NIST ISO/IEC ISO/IEC Special Publication 19790:2012(E) 24759:2017(E) SP 800-140 -- §6.1 through §6.12 SP 800-140A Annex A §6.13 SP 800-140B Annex B §6.14 modifies SP 800-140C Annex C §6.15 SP 800-140D Annex D §6.16 SP 800-140E Annex E §6.17 SP 800-140F Annex F §6.18

Table 1, whole. Not an entry: it restates the §3.3 and §3.4 rows (R-0055 to R-0060 and R-0062 to R-0068), as the next sentence says.

<!-- q L423-424 -->
> This table is provided to simplify locating where the changes to the ISO/IEC document sections are addressed in the CMVP documentation.

Not an entry: says Table 1 is a finding aid.

## Inferred requirements (not verbatim)

These entries are in our words and quote nothing; each names what it is derived from in `derived_from`. R-0069 (¶6), R-0070 (¶12), R-0071 (¶12), R-0072 (§2), RQ-03 (§3.3), security-policy (§3.3).

## Source defects and open questions

Found reading the source for this pass. Each quotes the lines it rests on; the prose is ours.

### SD-1 — ¶12: the text gives a minimum, the figure a different start

The text provides a transition of at least six months for laboratories; Figure 1 starts FIPS 140-3 testing at eighteen. Not a contradiction (six is a floor), but the start of testing is stated only in the figure, which a reader of the text alone would miss. Entries: R-0035, R-0040.

<!-- q L195-196 "A" .. "testing." -->
> A minimum transition period of 6 months after approval is provided for testing labs to develop and implement FIPS 140-3 testing.

<!-- q L217-218 -->
> FIPS 140-3 TESTING BEGINS (18 months after approval date)

### SD-2 — ¶12: no approval date, and no end for FIPS 140-2 testing

Every Figure 1 date is an offset from an approval date the document never prints as such; the only date in the announcement is its own (L85). The end of FIPS 140-2 testing has neither a date nor an offset. R-0070 computes the dates on the stated assumption. Entries: R-0039, R-0040, R-0041.

<!-- q L223-223 -->
> FIPS 140-2 TESTING ENDS

### SD-3 — §2 against §3.1: dated editions or the latest edition

§2 bases FIPS 140-3 on dated editions; §3.1 says that when referring to them the latest edition, including amendments, applies. ISO/IEC has since published later editions: the library's `iso-iec-19790` and `iso-iec-24759` records note that both were withdrawn on 2025-02-26 and revised by 2025 editions. So an implementer cannot tell from this text whether the 2012 basis still holds. nist-sp-800-140 §2 pins the editions instead, the opposite reading. Entries: R-0048, R-0050.

<!-- q L318-319 "Therefore," .. "24759:2017(E)." -->
> Therefore, FIPS 140-3 is based on ISO/IEC 19790:2012/Cor.1:2015(E) and ISO/IEC 24759:2017(E).

<!-- q L332-333 "When" .. "applies." -->
> When referring to ISO/IEC 19790:2012(E) and ISO/IEC 24759:2017(E), the latest edition of the referenced document (including any amendments) applies.

### SD-4 — §3.1 omits the corrigendum §2 names

§2 names ISO/IEC 19790:2012/Cor.1:2015(E); §3.1, §3.2 and §3.3 name ISO/IEC 19790:2012(E) without it. Editorial, unless §3.1's latest-edition rule is read as what brings Cor.1 in.

### SD-5 — ¶10: is the list of sources closed?

The word include leaves open whether a function from a source other than a to d can be Approved. Entry: R-0029.

<!-- q L172-173 "Approved" .. "either:" -->
> Approved security functions include those that are either:

### SD-6 — area names differ across the family

FIPS 140-3 lists operating environment (¶3, Abstract) where nist-sp-800-140 heads its §6.6 Operational environment; main's AREA-05 used the latter. ¶3 also says the areas relate to secure design and implementation, the Abstract to secure design, implementation and operation. Editorial. Entries: AREA-05, R-0018.

### SD-7 — §1: whose paragraph 5.2

The testing sentence allows modifications under paragraph 5.2 without saying it is ISO/IEC 24759's. Entry: R-0046.

## Tooling defects (bin/, not the source)

### TD-1 — fixed in library#137 (63d708e): `bin/_source_text.clean_pdf` dropped the first line of every page after the first

A line that opens a page carries the form feed, and the reader filed it in both pages; the earlier page's edge trim blanked it, so bin/fx1-skeleton and bin/check-quotes lost L37, L56, L82, L131, L181, L237 and L261 (four titles, the first line of ¶5, the first line of ¶10 item b, the end of a ¶13 sentence). After the fix pass 1 added ¶10 item b as R-0073, re-cut C-0037 (its sentence now runs to L237) and appended C-0047 to C-0049, the sentences the fixed reader newly offers (¶5's two and the last of ¶13's first paragraph). A dry rebuild under the fixed reader re-cut every other requirement text and marker of this record unchanged.

### TD-2 — fixed in library#137: page furniture the filter kept

The page numbers (L55, L81, L130, L180, L236, L260, L325, L374, L427) and the second running-header line CRYPTOGRAPHIC MODULES (L275, L327, L376) survived cleaning as text. They are furniture now. C-0045's text carried L275 and was re-cut to L269-273; no requirement spans those lines.
