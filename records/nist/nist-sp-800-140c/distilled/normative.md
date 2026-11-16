---
record: nist-sp-800-140c
kind: normative
title: "nist-sp-800-140c — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every requirement text in requirements.yaml that has source lines appears here verbatim under its section, as a marker that `bin/check-quotes --render` writes and `bin/check-quotes` verifies; split_of children are listed on their parent's line rather than quoted twice. Binding text that is not an entry (scope statements, normative references, definitions, abbreviations, sub-headings, captions and placeholder rows) is quoted the same way, with no id. Sections follow the source's own headings in source order; where requirements.yaml carries a skeleton locator that differs, the id line says so. requirements.yaml holds 61 entries: 1 skeleton, 5 split children, 2 from candidates (1 of them a table row), 11 hunted, 38 other table rows and 4 inferred.

## Status

The cover page (L1-37) is a withdrawal notice. What it means for every entry here is the inferred entry R-0058; the notice itself binds nothing (C-0001 to C-0003, rejected).

<!-- q L5 -->
> The attached publication has been withdrawn (archived), and is provided solely for historical purposes.

<!-- q L14-15 -->
> Withdrawal Note NIST SP 800-140C is superseded in its entirety by the publication of NIST SP 800-140Cr1.

## §1

<!-- q L228-230 "This" .. "conformance." -->
> This document specifies the Cryptographic Module Validation Program (CMVP) modifications of the methods to be used by a Cryptographic and Security Testing Laboratory (CSTL) to demonstrate conformance.

Scope statement (no entry).

<!-- q L230-231 "This" .. "conformity." -->
> This document also specifies the modification of methods for evidence that a vendor or testing laboratory provides to demonstrate conformity.

Scope statement (no entry).

<!-- q L231-233 "The" .. "6.15." -->
> The approved security functions specified in this document supersede those specified in ISO/IEC 19790 Annex C and ISO/IEC 24759 paragraph 6.15.

R-0003 · no candidate (hunted)

## §2

<!-- q L237 "This" .. "24759." -->
> This section identifies the normative references cited as ISO/IEC 19790 and ISO/IEC 24759.

<!-- q L237-243 "The" .. "24759:2017." -->
> The specific editions to be used are ISO/IEC 19790:2012 and ISO/IEC 24759:2017.

R-0004 · no candidate (hunted)

<!-- q L243-244 "Please" .. "2015." -->
> Please note that the version 19790:2012 referenced here includes the corrections made in 2015.

R-0005 · no candidate (hunted)

<!-- q L246-249 -->
> National Institute of Standards and Technology (2019) Security Requirements for Cryptographic Modules. (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 140-3. https://doi.org/10.6028/NIST.FIPS.140-3

The normative reference to FIPS 140-3.

## §3

<!-- q L253 -->
> The following terms and definitions supersede or are in addition to ISO/IEC 19790

R-0006 · no candidate (hunted)

<!-- q L255 -->
> None at this time

## §4

<!-- q L259-260 -->
> The following symbols and abbreviated terms supersede or are in addition to ISO/IEC 19790 throughout this document:

R-0007 · no candidate (hunted)

<!-- q L262 -->
> CCCS Canadian Centre for Cyber Security

<!-- q L264 -->
> CMVP Cryptographic Module Validation Program

<!-- q L266 -->
> CSD Computer Security Division

<!-- q L268 -->
> CSTL Cryptographic and Security Testing Laboratory

<!-- q L270 -->
> FIPS Federal Information Processing Standard

<!-- q L272 -->
> FISMA Federal Information Security Management/Modernization Act

<!-- q L274 -->
> NIST National Institute of Standards and Technology

<!-- q L280 -->
> SP 800-XXX NIST Special Publication 800 series document

## §5.1

<!-- q L286-287 -->
> Section 6 of this document replaces the approved security functions of ISO/IEC 19790 Annex C and ISO/IEC 24759 paragraph 6.15.

R-0008 · no candidate (hunted)

## §5.2

<!-- q L291 "Modifications" .. "24759." -->
> Modifications will follow a similar format to that used in ISO/IEC 24759.

R-0009 · no candidate (hunted)

<!-- q L291-298 "For" .. "“sequence_number.”" -->
> For additions to test requirements, new Test Evidence (TEs) or Vendor Evidence (VEs) will be listed by increasing the “sequence_number.”

R-0010 · no candidate (hunted)

<!-- q L298-299 "the" .. "strikethrough." -->
> the “sequence_number.” Modifications can include a combination of additions using underline and deletions using strikethrough.

R-0001 · split into R-0002

<!-- q L299-300 "If" .. "change.”" -->
> If no changes are required, the paragraph will indicate “No change.”

R-0011 · C-0013

## §6.1

<!-- q L306 "This" .. "functions." -->
> This document identifies CMVP-approved security functions.

R-0012 · no candidate (hunted)

<!-- q L306-307 "It" .. "24759." -->
> It supersedes security functions identified in ISO/IEC 19790 and ISO/IEC 24759.

R-0013 · no candidate (hunted)

## §6.2

<!-- q L311-312 -->
> The categories include transitions, symmetric key encryption and decryption, digital signatures, hashing and message authentication.

R-0014 · no candidate (hunted)

## §6.2.1

<!-- q L316-318 -->
> Barker EB, Roginsky AL (2019) Transitioning the Use of Cryptographic Algorithms and Key Lengths. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-131A, Rev. 2. https://doi.org/10.6028/NIST.SP.800-131Ar2

R-0015 · row: §6.2.1 Transitions: reference

<!-- q L320 -->
> ● Relevant Sections: 1, 2, 3, 9 and 10.

R-0016 · row: §6.2.1 Transitions: relevant sections

## §6.2.2

<!-- q L324 -->
> Advanced Encryption Standard (AES)

R-0017 · row: §6.2.2 AES: function

<!-- q L326-328 -->
> National Institute of Standards and Technology (2001) Advanced Encryption Standard (AES). (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 197. https://doi.org/10.6028/NIST.FIPS.197

R-0018 · row: §6.2.2 AES: reference 1 of 9

<!-- q L333-335 -->
> Dworkin MJ (2001) Recommendation for Block Cipher Modes of Operation: Methods and Techniques. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38A. https://doi.org/10.6028/NIST.SP.800-38A

R-0019 · row: §6.2.2 AES: reference 2 of 9

<!-- q L337-340 -->
> Dworkin MJ (2010) Recommendation for Block Cipher Modes of Operation: Three Variants of Ciphertext Stealing for CBC Mode. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38A, Addendum. https://doi.org/10.6028/NIST.SP.800-38A-Add

R-0020 · row: §6.2.2 AES: reference 3 of 9

<!-- q L342-345 -->
> Dworkin MJ (2004) Recommendation for Block Cipher Modes of Operation: the CCM Mode for Authentication and Confidentiality. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38C, Includes updates as of July 20, 2007. https://doi.org/10.6028/NIST.SP.800-38C

R-0021 · row: §6.2.2 AES: reference 4 of 9

<!-- q L351-354 -->
> Dworkin MJ (2007) Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38D. https://doi.org/10.6028/NIST.SP.800-38D

R-0022 · row: §6.2.2 AES: reference 5 of 9

<!-- q L356-359 -->
> Dworkin MJ (2010) Recommendation for Block Cipher Modes of Operation: The XTS-AES Mode for Confidentiality on Storage Devices. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38E. https://doi.org/10.6028/NIST.SP.800-38E

R-0023 · row: §6.2.2 AES: reference 6 of 9

<!-- q L361-363 -->
> Dworkin MJ (2012) Recommendation for Block Cipher Modes of Operation: Methods for Key Wrapping. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38F. https://doi.org/10.6028/NIST.SP.800-38F

R-0024 · row: §6.2.2 AES: reference 7 of 9

<!-- q L365-368 -->
> IEEE Standards Association (2013) IEEE 802.1AEbw-2013 – IEEE Standard for Local and metropolitan area networks—Media Access Control (MAC) Security Amendment 2: Extended Packet Numbering (IEEE, Piscataway, NJ). Available at https://standards.ieee.org/standard/802_1AEbw-2013.html

R-0025 · row: §6.2.2 AES: reference 8 of 9

<!-- q L370-373 -->
> Dworkin MJ (2016) Recommendation for Block Cipher Modes of Operation: Methods for Format-Preserving Encryption. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38G. https://doi.org/10.6028/NIST.SP.800-38G

R-0026 · row: §6.2.2 AES: reference 9 of 9

<!-- q L375 -->
> Triple-DES Encryption Algorithm (TDEA)

R-0027 · row: §6.2.2 TDEA: function

<!-- q L377-380 -->
> Barker EB, Mouha N (2017) Recommendation for the Triple Data Encryption Algorithm (TDEA) Block Cipher. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-67, Rev. 2. https://doi.org/10.6028/NIST.SP.800-67r2

R-0028 · row: §6.2.2 TDEA: reference 1 of 3

<!-- q L382-388 -->
> Dworkin MJ (2001) Recommendation for Block Cipher Modes of Operation: Methods and Techniques. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38A. https://doi.org/10.6028/NIST.SP.800-38A

R-0029 · row: §6.2.2 TDEA: reference 2 of 3 · split into R-0030, R-0031

<!-- q L390 -->
> ● Appendix E references modes of the Triple-DES algorithm.

R-0032 · row: §6.2.2 TDEA: note on reference 2

<!-- q L392-394 -->
> Dworkin MJ (2012) Recommendation for Block Cipher Modes of Operation: Methods for Key Wrapping. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38F. https://doi.org/10.6028/NIST.SP.800-38F

R-0033 · row: §6.2.2 TDEA: reference 3 of 3

<!-- q L396 -->
> SKIPJACK

R-0034 · row: §6.2.2 SKIPJACK: function

<!-- q L398 "NOTE" .. "only." -->
> NOTE The use of SKIPJACK is approved for decryption only.

R-0035 · C-0014 · row: §6.2.2 SKIPJACK: NOTE, sentence 1

<!-- q L398-400 "The SKIPJACK" .. "withdrawn." -->
> The SKIPJACK algorithm has been documented in Federal Information Processing Standards Publication (FIPS) 185. This publication is obsolete and has been withdrawn.

R-0036 · row: §6.2.2 SKIPJACK: NOTE, sentences 2 and 3

## §6.2.3

<!-- q L408 -->
> Digital Signature Standard (DSS)

R-0037 · row: §6.2.3 DSS: function

<!-- q L410-412 -->
> National Institute of Standards and Technology (2013) Digital Signature Standard (DSS). (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 186-4. https://doi.org/10.6028/NIST.FIPS.186-4

R-0038 · row: §6.2.3 DSS: reference 1 of 1

## §6.2.4

<!-- q L416-417 -->
> Secure Hash Standard (SHS) (SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256)

R-0039 · row: §6.2.4 SHS: function

<!-- q L419-421 -->
> National Institute of Standards and Technology (2015) Secure Hash Standard (SHS). (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 180-4. https://doi.org/10.6028/NIST.FIPS.180-4

R-0040 · row: §6.2.4 SHS: reference 1 of 1

## §6.2.5

<!-- q L425 -->
> SHA-3 Hash Algorithms (SHA3-224, SHA3-256, SHA3-384, SHA3-512)

R-0041 · row: §6.2.5 SHA-3 hash: function

<!-- q L427-430 -->
> National Institute of Standards and Technology (2015) SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions. (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 202. https://doi.org/10.6028/NIST.FIPS.202

R-0042 · row: §6.2.5 SHA-3 hash: reference 1 of 1

<!-- q L432 -->
> SHA-3 Extendable-Output Functions (XOF) (SHAKE128, SHAKE256)

R-0043 · row: §6.2.5 SHA-3 XOF: function

<!-- q L434-443 -->
> National Institute of Standards and Technology (2015) SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions. (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 202. https://doi.org/10.6028/NIST.FIPS.202

R-0044 · row: §6.2.5 SHA-3 XOF: reference 1 of 1 · split into R-0045, R-0046

<!-- q L445 -->
> SHA-3 Derived Functions: cSHAKE, KMAC, TupleHash, and ParallelHash

R-0047 · row: §6.2.5 SHA-3 derived: function

<!-- q L447-450 -->
> Kelsey JM, Chang S-jH, Perlner RA (2016) SHA-3 Derived Functions: cSHAKE, KMAC, TupleHash, and ParallelHash. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-185. https://doi.org/10.6028/NIST.SP.800-185

R-0048 · row: §6.2.5 SHA-3 derived: reference 1 of 1

## §6.2.6

<!-- q L454 -->
> Triple-DES

R-0049 · row: §6.2.6 Triple-DES MAC: function

<!-- q L460-463 -->
> Dworkin MJ (2005) Recommendation for Block Cipher Modes of Operation: The CMAC Mode for Authentication. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38B, Includes updates as of October 6, 2016. https://doi.org/10.6028/NIST.SP.800-38B

R-0050 · row: §6.2.6 Triple-DES MAC: reference 1 of 1

<!-- q L465 -->
> AES

R-0051 · row: §6.2.6 AES MAC: function

<!-- q L467-470 -->
> Dworkin MJ (2005) Recommendation for Block Cipher Modes of Operation: The CMAC Mode for Authentication. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38B, Includes updates as of October 6, 2016. https://doi.org/10.6028/NIST.SP.800-38B

R-0052 · row: §6.2.6 AES MAC: reference 1 of 3

<!-- q L472-475 -->
> Dworkin MJ (2004) Recommendation for Block Cipher Modes of Operation: The CCM Mode for Authentication and Confidentiality. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38C, Includes updates as of July 20, 2007. https://doi.org/10.6028/NIST.SP.800-38C

R-0053 · row: §6.2.6 AES MAC: reference 2 of 3

<!-- q L477-480 -->
> Dworkin MJ (2007) Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38D. https://doi.org/10.6028/NIST.SP.800-38D

R-0054 · row: §6.2.6 AES MAC: reference 3 of 3

<!-- q L482 -->
> HMAC

R-0055 · row: §6.2.6 HMAC: function

<!-- q L484-487 -->
> National Institute of Standards and Technology (2008) The Keyed-Hash Message Authentication Code (HMAC). (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 198-1. https://doi.org/10.6028/NIST.FIPS.198-1

R-0056 · row: §6.2.6 HMAC: reference 1 of 2

<!-- q L489-491 -->
> Dang QH (2012) Recommendation for Applications Using Approved Hash Algorithms. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-107, Rev. 1. https://doi.org/10.6028/NIST.SP.800-107r1

R-0057 · row: §6.2.6 HMAC: reference 2 of 2

## Document Revisions

L493-498 print a rotated Document Revisions table: a header (Date, Change) and no rows. Not normative.

## Inferred

Kind inferred, in our words, in requirements.yaml with derived_from: R-0058, R-0059, R-0060, R-0061.

## Source defects

**SD-1** — reader, fixed: NIST prints the rotated free-of-charge sidebar mid-page with blank lines around it, and the pass-1 PDF reading kept those blank lines as a paragraph break. The skeleton therefore cut §5.2's second sentence at L293-297, and R-0001 opens on the last words of the sentence before it; the whole sentence is R-0010. 63d708e drops the sidebar's blank surround, and a skeleton re-run now runs L291-299 together as one sentence, because the skeleton does not end a sentence after a closing quotation mark (L298); R-0001 stays as cut, its ids stable.

**SD-2** — reader, fixed: the pass-1 reading kept page numbers as text, because they recur on fewer than half the pages and furniture was found by recurrence. Two reference rows were welded across one (L384, L438), so pass 1 split each into split_of children quoting the citation either side. 63d708e makes a lone page number at a page edge furniture; the two rows (R-0029, R-0044) were re-cut without it, and each notes why its children exist.

**SD-3** — counter, fixed: pass 1's bin/_bcp14 skipped May only when a year followed it, so the month of the withdrawal date, printed with a day at L13 and L37, was counted twice as the verbal form may (C-0002, C-0003) and the source count read 14. Since 63d708e it also skips May before a day and a year: the source carries 12 verbal forms. skeleton-report.txt is the pass-1 run and still reads 14.

**SD-4** — rendering, not source: §5.2 marks additions by underline and deletions by strikethrough, which the pdftotext rendering cannot carry. §6 is a replacement list rather than marked-up ISO text, so nothing in it depends on the marks.

**SD-5** — source: SKIPJACK decryption stays approved while the NOTE says its only cited specification, FIPS 185, is obsolete and withdrawn; §6.2.2 gives no current specification to test it against (R-0060).
