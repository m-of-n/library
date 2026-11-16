---
record: nist-sp-800-140e
kind: normative
title: "nist-sp-800-140e — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every requirement text in requirements.yaml that has source lines appears here verbatim under its section, as a marker that `bin/check-quotes --render` writes and `bin/check-quotes` verifies; split_of children are listed on their parent's line rather than quoted twice. Binding text that is not an entry (scope statements, normative references, definitions, abbreviations, sub-headings, captions and placeholder rows) is quoted the same way, with no id. Sections follow the source's own headings in source order; where requirements.yaml carries a skeleton locator that differs, the id line says so. requirements.yaml holds 54 entries: 7 skeleton, 23 split children, 1 from candidates, 11 hunted, 8 other table rows and 4 inferred.

## §1

<!-- q L185-187 "This" .. "conformance." -->
> This document specifies the Cryptographic Module Validation Program (CMVP) modifications of the methods to be used by a Cryptographic and Security Testing Laboratory (CSTL) to demonstrate conformance.

Scope statement (no entry).

<!-- q L187-188 "This" .. "conformity." -->
> This document also specifies the modification of methods for evidence that a vendor or testing laboratory provides to demonstrate conformity.

Scope statement (no entry).

<!-- q L188-190 "The" .. "6.17." -->
> The approved sensitive security parameter generation and establishment methods specified in this document supersede those specified in ISO/IEC 19790 Annex E and ISO/IEC 24759 paragraph 6.17.

R-0016 · no candidate (hunted)

## §2

<!-- q L194 "This" .. "24759." -->
> This section identifies the normative references cited as ISO/IEC 19790 and ISO/IEC 24759.

<!-- q L194-195 "The" .. "24759:2017." -->
> The specific editions to be used are ISO/IEC 19790:2012 and ISO/IEC 24759:2017.

R-0017 · no candidate (hunted)

<!-- q L195-196 "Please" .. "2015." -->
> Please note that the version 19790:2012 referenced here includes the corrections made in 2015.

R-0018 · no candidate (hunted)

<!-- q L202-205 -->
> National Institute of Standards and Technology (2019) Security Requirements for Cryptographic Modules. (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 140-3. https://doi.org/10.6028/NIST.FIPS.140-3

The normative reference to FIPS 140-3.

## §3

<!-- q L209-210 -->
> The following terms and definitions supersede or are in addition to ISO/IEC 19790 and ISO/IEC 24759:

R-0019 · no candidate (hunted)

<!-- q L212-213 -->
> Rate Limiting: Used to control the rate of requests sent or received by a network interface and is used to prevent automated attacks.

Definition (C-0010, rejected as a provision).

<!-- q L215-218 -->
> Authenticator: The means used to confirm the identity of a user, processor, or device (e.g., user password or token). Sometimes defined as something you know, something you have or something you are. Referred to as a token in earlier versions of SP 800-63 and in ISO/IEC 19790 and ISO/IEC 24759.

Definition.

## §4

<!-- q L222-223 -->
> The following symbols and abbreviated terms supersede or are in addition to ISO/IEC 19790 and ISO/IEC 24759 throughout this document:

R-0020 · no candidate (hunted)

<!-- q L225 -->
> CCCS Canadian Centre for Cyber Security

<!-- q L227 -->
> CMVP Cryptographic Module Validation Program

<!-- q L229 -->
> CSD Computer Security Division

<!-- q L231 -->
> CSTL Cryptographic and Security Testing Laboratory

<!-- q L237 -->
> FIPS Federal Information Processing Standard

<!-- q L239 -->
> FISMA Federal Information Security Management/Modernization Act

<!-- q L241-242 -->
> FMR False Match Rate. The proportion of zero-effort impostor attempt samples falsely declared to match the compared non-self template

<!-- q L244 -->
> NIST National Institute of Standards and Technology

<!-- q L246-247 -->
> PAD Presentation Attack Detection. An automated determination of a presentation attack

<!-- q L249 -->
> SP 800-XXX NIST Special Publication 800 series document

## §5.1

<!-- q L259-260 "Section" .. "6.17." -->
> Section 6 of this document replaces the approved authentication mechanisms requirements of ISO/IEC 19790 Annex E and ISO/IEC 24759 paragraph 6.17.

R-0021 · no candidate (hunted)

<!-- q L260-262 "While" .. "authentication." -->
> While this document serves a different purpose, much of the authentication is purposely meant to align with SP 800-63B, which is an informative reference for module authentication.

R-0022 · no candidate (hunted)

## §5.2

<!-- q L266-267 "Modifications" .. "strikethrough." -->
> Modifications will follow a similar format as in ISO/IEC 24579. Modifications can include a combination of additions using underline and deletions using strikethrough.

R-0001 · split into R-0008, R-0009

<!-- q L267-268 "If" .. "change.”" -->
> If no changes are required, the paragraph will indicate “No change.”

R-0023 · C-0011

## §6.1

<!-- q L274-275 "This" .. "operators." -->
> This document includes all requirements for CMVP-approved authentication mechanisms for operators.

R-0024 · no candidate (hunted)

<!-- q L275-277 "Some" .. "800-140D." -->
> Some of these mechanisms may be employed to establish module provided protected communication services; however, these must meet the cryptographic strength requirements of SP 800-140C and SP 800-140D.

R-0002 · split into R-0010, R-0011

<!-- q L277-278 "These" .. "19790." -->
> These requirements supplement the authentication requirements specified in ISO/IEC 19790.

R-0025 · no candidate (hunted)

## §6.2

<!-- q L282-290 -->
> While there are currently no approved authentication mechanisms, allowed authentication mechanisms may be used as indicated in Table 1. Except at level 1, operator authentication acceptance is required to be performed by the module or by the Operating Environment as defined in ISO/IEC 19790. Table 1 - Authentication mechanism permitted at FIPS 140-3 security levels

R-0003 · split into R-0012, R-0013

<!-- q L290 -->
> Table 1 - Authentication mechanism permitted at FIPS 140-3 security levels

Table 1 caption, welded into R-0003 by the skeleton under the pass-1 reader (SD-7).

<!-- q L292 -->
> FIPS 140-3 Level Authentication

Table 1 header row.

<!-- q L295 "Level" .. "implicit." -->
> Level 1 None required—may be implicit.

R-0004 · row: Table 1 (caption L290), Level 1: sentence 1 of 2

<!-- q L295-297 "If" .. "minimum." -->
> If authentication is used, it should meet the requirements of Level 2 as a minimum.

R-0005 · row: Table 1 (caption L290), Level 1: sentence 2 of 2

<!-- q L299-302 -->
> Memorized secret Level 2 or Level 3 authentication mechanism

R-0026 · row: Table 1 (caption L290), Level 2 · split into R-0027, R-0028, R-0029, R-0030

<!-- q L304-318 -->
> Level 3 • Memorized Secret; • Look-Up Secret; • Out-of-Band; • Single-Factor One Time Password (OTP) Device; • Multi-Factor OTP Device; • Single-Factor Crypto Software; • Single-Factor Crypto Device; • Multi-Factor Crypto Software; • Multi-Factor Crypto Device

R-0031 · row: Table 1 (caption L290), Level 3 · split into R-0032, R-0033, R-0034, R-0035, R-0036, R-0037, R-0038, R-0039, R-0040

<!-- q L321-322 -->
> Level 4 • Multi-Factor Crypto Software; • Multi-Factor Crypto Device

R-0041 · row: Table 1 (caption L290), Level 4 · split into R-0042, R-0043

<!-- q L324-325 "Vendors" .. "met." -->
> Vendors should use SP 800-63B as a framework for authentication requirements and should provide justification whenever SP 800-63B requirements cannot be met.

R-0006 · split into R-0014, R-0015

<!-- q L325-326 "Testers" .. "documentation." -->
> Testers should review and affirm the vendor documentation.

R-0007

<!-- q L327 -->
> Normative SP 800-63B sections include

R-0044 · no candidate (hunted)

<!-- q L328 -->
> ● Section 5, Detailed requirements specific to each type of authenticator;

R-0045 · row: SP 800-63B sections list: normative 1 of 3

<!-- q L329 -->
> ● Section 6, Lifecycle management;

R-0046 · row: SP 800-63B sections list: normative 2 of 3

<!-- q L330 -->
> ● Section 7, Session Management;

R-0047 · row: SP 800-63B sections list: normative 3 of 3

<!-- q L331 -->
> Informative information to be assessed for each authenticator includes:

R-0048 · no candidate (hunted)

<!-- q L332 -->
> ● Section 8, Threats and Security Considerations; and

R-0049 · row: SP 800-63B sections list: assessed 1 of 2

<!-- q L333 -->
> ● Section 10, Usability Considerations.

R-0050 · row: SP 800-63B sections list: assessed 2 of 2

## Document Revisions

L339-346 print a rotated Document Revisions table: a header (Date, Change) and no rows. Not normative; pdftotext interleaves it with the running header.

## Inferred

Kind inferred, in our words, in requirements.yaml with derived_from: R-0051, R-0052, R-0053, R-0054.

## Source defects

**SD-1** — source: §1's last sentence (R-0016) has this SP's SSP generation and establishment methods supersede ISO/IEC 19790 Annex E. Such methods are SP 800-140D's subject; this SP's are authentication mechanisms, as §5.1 says.

**SD-2** — source: ISO/IEC 24579 is printed for ISO/IEC 24759 on the title page (L29) and in §5.2 (R-0001).

**SD-3** — source: §5.1 calls SP 800-63B an informative reference, while §6.2 tells vendors to use it as the framework and lists its normative sections; §2 does not cite it at all.

**SD-4** — source: §6.1 (R-0054 reads it) holds a mechanism that establishes a protected communication service to strength requirements it attributes to SP 800-140C and SP 800-140D, which list approved functions and methods and state no strength requirement of their own.

**SD-5** — source: the title promises approved authentication mechanisms, and §6.2 says there are none; Table 1 lists allowed, permitted ones.

**SD-6** — source: §4 defines FMR and PAD, biometric terms, which the body never uses; Table 1 lists no biometric mechanism.

**SD-7** — reader, fixed: the pass-1 reading kept page numbers as text, so the page before Table 1 ended on its page number (L286) rather than a finished sentence, no paragraph break was kept, and the skeleton's R-0003 ran from §6.2's two sentences through the page number into the table caption (L290). 63d708e drops the page number, and a skeleton re-run now ends R-0003 at L285. The entry keeps the skeleton's cut, re-cut without the page number; its children quote the two sentences.

**SD-8** — rendering: in Table 1's Level 2 row pdftotext prints the row label between the first and second lines of its cell (L299-302); the row entry records the weld and its children quote each line.

**SD-9** — rendering, not source: §5.2 marks additions by underline and deletions by strikethrough, which the pdftotext rendering cannot carry; §6 prints no marked-up text.
