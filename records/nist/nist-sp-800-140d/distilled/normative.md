---
record: nist-sp-800-140d
kind: normative
title: "nist-sp-800-140d — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every requirement text in requirements.yaml that has source lines appears here verbatim under its section, as a marker that `bin/check-quotes --render` writes and `bin/check-quotes` verifies; split_of children are listed on their parent's line rather than quoted twice. Binding text that is not an entry (scope statements, normative references, definitions, abbreviations, sub-headings, captions and placeholder rows) is quoted the same way, with no id. Sections follow the source's own headings in source order; where requirements.yaml carries a skeleton locator that differs, the id line says so. requirements.yaml holds 34 entries: 1 skeleton, 4 split children, 9 from candidates (8 of them table rows), 8 hunted, 8 other table rows and 4 inferred.

## Status

The cover page (L1-37) is a withdrawal notice. What it means for every entry here is the inferred entry R-0031; the notice itself binds nothing (C-0001 to C-0003, rejected).

<!-- q L5 -->
> The attached publication has been withdrawn (archived), and is provided solely for historical purposes.

<!-- q L14-15 -->
> Withdrawal Note NIST SP 800-140D is superseded in its entirety by the publication of NIST SP 800-140Dr1

## §1

<!-- q L226-228 -->
> This document specifies the Cryptographic Module Validation Program (CMVP) approved sensitive security parameter generation and establishment methods and supersedes those specified in ISO/IEC 19790 Annex D and ISO/IEC 24759 paragraph 6.16.

R-0004 · no candidate (hunted)

## §2

<!-- q L232 "This" .. "24759." -->
> This section identifies the normative references cited as ISO/IEC 19790 and ISO/IEC 24759.

<!-- q L232-233 "The" .. "24759:2017." -->
> The specific editions to be used are ISO/IEC 19790:2012 and ISO/IEC 24759:2017.

R-0005 · no candidate (hunted)

<!-- q L233-234 "Please" .. "2015." -->
> Please note that the version 19790:2012 referenced here includes the corrections made in 2015.

R-0006 · no candidate (hunted)

<!-- q L236-244 -->
> National Institute of Standards and Technology (2019) Security Requirements for Cryptographic Modules. (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 140-3. https://doi.org/10.6028/NIST.FIPS.140-3

The normative reference to FIPS 140-3.

## §3

<!-- q L248-249 -->
> The following terms and definitions supersede or are in addition to ISO/IEC 19790 and ISO/IEC 24759.

R-0007 · no candidate (hunted)

<!-- q L251 -->
> None at this time

## §4

<!-- q L255-256 -->
> The following symbols and abbreviated terms supersede or are in addition to ISO/IEC 19790 and ISO/IEC 24759 throughout this document:

R-0008 · no candidate (hunted)

<!-- q L258 -->
> CCCS Canadian Centre for Cyber Security

<!-- q L260 -->
> CMVP Cryptographic Module Validation Program

<!-- q L262 -->
> CSD Computer Security Division

<!-- q L264 -->
> CSTL Cryptographic and Security Testing Laboratory

<!-- q L266 -->
> FIPS Federal Information Processing Standard

<!-- q L268 -->
> FISMA Federal Information Security Management/Modernization Act

<!-- q L270 -->
> NIST National Institute of Standards and Technology

<!-- q L272 -->
> SP 800-XXX NIST Special Publication 800 series document

## §5.1

<!-- q L282-283 -->
> Section 6 of this document replaces the approved sensitive security parameter generation and establishment methods of ISO/IEC 19790 Annex D and ISO/IEC 24759 paragraph 6.16.

R-0009 · no candidate (hunted)

## §5.2

<!-- q L287-290 "Modifications" .. "strikethrough." -->
> Modifications will follow a similar format to that used in ISO/IEC 24759. For additions to test requirements, new Test Evidence (TEs) or Vendor Evidence (VEs) will be listed by increasing the “sequence_number.” Modifications can include a combination of additions using underline and deletions using strikethrough.

R-0001 · split into R-0002, R-0003

<!-- q L290-296 "If" .. "change.”" -->
> If no changes are required, the paragraph will indicate “No change.”

R-0010 · C-0013

## §6.1

<!-- q L303-304 "This" .. "methods." -->
> This document identifies CMVP-approved sensitive security parameter generation and establishment methods.

R-0011 · no candidate (hunted)

<!-- q L304-305 "It" .. "methods." -->
> It precludes the use of all other sensitive security parameter generation and establishment methods.

R-0012 · no candidate (hunted)

## §6.2.1

<!-- q L311-313 -->
> Barker EB, Roginsky AL (2019) Transitioning the Use of Cryptographic Algorithms and Key Lengths. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-131A, Rev. 2. https://doi.org/10.6028/NIST.SP.800-131Ar2

R-0013 · row: §6.2.1 Transitions: reference

<!-- q L315 -->
> ● Sections relevant to this Annex: 1, 5, 6, 7, and 8.

R-0014 · row: §6.2.1 Transitions: relevant sections

## §6.2.2

<!-- q L319-321 -->
> 1. National Institute of Standards and Technology (2013) Digital Signature Standard (DSS). (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 186-4. https://doi.org/10.6028/NIST.FIPS.186-4

R-0015 · C-0014, C-0015, C-0016 · row: §6.2.2 item 1

<!-- q L323 -->
> • DSA, RSA, and ECDSA.

R-0016 · row: §6.2.2 item 1: algorithms

<!-- q L331-333 -->
> Note. For the purposes of the key establishment techniques, the Digital Signature Standard is only used to define the domain parameters and the (private, public) key-pair generation.

R-0017 · C-0017 · row: §6.2.2 item 1: note

<!-- q L335-338 -->
> 2. Barker EB, Chen L, Roginsky AL, Vassilev A, Davis R (2018) Recommendation for Pair-Wise Key-Establishment Schemes Using Discrete Logarithm Cryptography. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-56A, Rev. 3. https://doi.org/10.6028/NIST.SP.800-56Ar3

R-0018 · row: §6.2.2 item 2

<!-- q L340-349 -->
> 3. Barker EB, Chen L, Roginsky AL, Vassilev A, Davis R, Simon S (2019) Recommendation for Pair-Wise Key-Establishment Using Integer Factorization Cryptography. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-56B, Rev. 2. https://doi.org/10.6028/NIST.SP.800-56Br2

R-0019 · row: §6.2.2 item 3

<!-- q L351-353 -->
> 4. Chen L (2009) Recommendation for Key Derivation Using Pseudorandom Functions (Revised). (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-108, Revised. https://doi.org/10.6028/NIST.SP.800-108

R-0020 · row: §6.2.2 item 4

<!-- q L355-358 -->
> 5. Sönmez Turan M, Barker EB, Burr WE, Chen L (2010) Recommendation for Password-Based Key Derivation: Part 1: Storage Applications. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-132. https://doi.org/10.6028/NIST.SP.800-132

R-0021 · row: §6.2.2 item 5

<!-- q L360-362 -->
> 6. Dang QH (2011) Recommendation for Existing Application-Specific Key Derivation Functions. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-135, Rev. 1. https://doi.org/10.6028/NIST.SP.800-135r1

R-0022 · row: §6.2.2 item 6

<!-- q L364-367 -->
> 7. Barker EB, Chen L, Davis R (2018) Recommendation for Key-Derivation Methods in Key-Establishment Schemes. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-56C, Rev. 1. https://doi.org/10.6028/NIST.SP.800-56Cr1

R-0023 · C-0018, C-0019 · row: §6.2.2 item 7

<!-- q L369-371 -->
> 8. Chen L (2011) Recommendation for Key-Derivation through Extraction-then-Expansion. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-56C. https://doi.org/10.6028/NIST.SP.800-56C

R-0024 · C-0020, C-0021 · row: §6.2.2 item 8

<!-- q L373-375 -->
> 9. Dworkin MJ (2012) Recommendation for Block Cipher Modes of Operation: Methods for Key Wrapping. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-38F. https://doi.org/10.6028/NIST.SP.800-38F

R-0025 · C-0022, C-0023 · row: §6.2.2 item 9

<!-- q L377-379 -->
> 10. Barker EB, Roginsky AL (2019) Recommendation for Cryptographic Key Generation. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-133, Rev. 1. https://doi.org/10.6028/NIST.SP.800-133r1

R-0026 · C-0024, C-0025 · row: §6.2.2 item 10

<!-- q L381-388 -->
> 11. Barker EB, Kelsey J (2015) Recommendation for Random Number Generation Using Deterministic Random Bit Generators. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-90A, Rev. 1. https://doi.org/10.6028/NIST.SP.800-90Ar1

R-0027 · C-0026, C-0027 · row: §6.2.2 item 11 · split into R-0028, R-0029

<!-- q L390-393 -->
> 12. Sonmez Turan M, Barker EB, Kelsey J, McKay KA, Baish, ML, Boyle M (2018) Recommendation for Entropy Sources Used for Random Number Generation. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Special Publication (SP) 800-90B. https://doi.org/10.6028/NIST.SP.800-90B

R-0030 · C-0028, C-0029 · row: §6.2.2 item 12

## Document Revisions

L407-409 print a Document Revisions table: a header (Date, Change) and no rows. Not normative.

## Inferred

Kind inferred, in our words, in requirements.yaml with derived_from: R-0031, R-0032, R-0033, R-0034.

## Source defects

**SD-1** — reader, fixed in part: reference items 2 to 6 of §6.2.2 (L335-362) begin with a number the table of contents also lists (2 to 6), so the pass-1 PDF reading keyed each as a heading, §2 to §6, with its continuation lines. The skeleton therefore never saw items 2 to 6 (they are entries here, cut from their lines) and filed the item 7 to 12 candidates under §6. 63d708e fixed this (a numbered heading the table of contents lists must agree with the title it has there); the candidate locators were re-derived (§6.2.2), and bin/check-locators finds every entry in its clause. Still open in bin/_source_text: the wrapped table-of-contents line at L204, whose page number is printed six lines down after the sidebar, is keyed as heading §6, so L204-L223 read as §6. No entry or candidate lies in those lines.

**SD-2** — reader, fixed: the pass-1 reading kept page numbers as text (they recur on fewer than half the pages), so item 11 was welded across the page number at L383 and pass 1 gave the entry split_of children for the citation either side. 63d708e makes a lone page number at a page edge furniture; R-0027 was re-cut without it and notes why its children exist.

**SD-3** — counter, fixed: pass 1's bin/_bcp14 skipped May only when a year followed it, so the month of the withdrawal date, printed with a day at L13 and L37, was counted twice as the verbal form may (C-0002, C-0003) and the source count read 14. Since 63d708e it also skips May before a day and a year: the source carries 12 verbal forms. skeleton-report.txt is the pass-1 run and still reads 14.

**SD-4** — rendering, not source: §5.2 marks additions by underline and deletions by strikethrough, which the pdftotext rendering cannot carry; §6 is a replacement list, so nothing in it depends on the marks.

**SD-5** — source: §6.2 covers generation and establishment, but its only list, §6.2.2, is titled for key establishment and also holds key generation (item 10), deterministic random bit generators (item 11) and entropy sources (item 12); no clause lists generation methods as such.

**SD-6** — source: two editions of SP 800-56C are listed, the 2018 Rev. 1 (item 7) and the 2011 original (item 8), with nothing on whether the older one is approved only during a transition.
