---
record: nist-sp-800-140a
kind: normative
title: "nist-sp-800-140a — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every requirement text in requirements.yaml that has source lines appears here verbatim under its section, as a marker that `bin/check-quotes --render` writes and `bin/check-quotes` verifies; split_of children are listed on their parent's line rather than quoted twice. Binding text that is not an entry (scope statements, normative references, definitions, abbreviations, sub-headings, captions and placeholder rows) is quoted the same way, with no id. Sections follow the source's own headings in source order; where requirements.yaml carries a skeleton locator that differs, the id line says so. requirements.yaml holds 22 entries: 5 skeleton, 4 split children, 1 from candidates, 10 hunted, 0 other table rows and 2 inferred.

## §1

<!-- q L177-178 "Federal" .. "19790." -->
> Federal Information Processing Standard (FIPS) 140-3 documentation requirements are specified in ISO/IEC 19790.

R-0010 · no candidate (hunted)

<!-- q L178-180 "This" .. "conformity." -->
> This document specifies any additional requirements specified by the Cryptographic Module Validation Program (CMVP) for evidence that vendors provide to a Cryptographic and Security Testing Laboratory (CSTL) to demonstrate conformity.

Scope statement: what this SP adds (no entry).

<!-- q L180-181 "Unless" .. "24759." -->
> Unless otherwise modified in this document, the test requirements are specified in ISO/IEC 24759.

R-0011 · no candidate (hunted)

## §2

<!-- q L185 "This" .. "24759." -->
> This section identifies the normative references cited as ISO/IEC 19790 and ISO/IEC 24759.

<!-- q L185-186 "The" .. "24759:2017." -->
> The specific editions to be used are ISO/IEC 19790:2012 and ISO/IEC 24759:2017.

R-0012 · no candidate (hunted)

<!-- q L186-187 "Please" .. "2015." -->
> Please note that the version 19790:2012 referenced here includes the corrections made in 2015.

R-0013 · no candidate (hunted)

<!-- q L189-197 -->
> National Institute of Standards and Technology (2019) Security Requirements for Cryptographic Modules. (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 140-3. https://doi.org/10.6028/NIST.FIPS.140-3

The normative reference to FIPS 140-3.

## §3

<!-- q L201-202 -->
> The following terms and definitions supersede or are in addition to ISO/IEC 19790 and ISO/IEC 24759.

R-0014 · no candidate (hunted)

<!-- q L204 -->
> No additional terms at this time.

## §4

<!-- q L208-209 -->
> The following symbols and abbreviated terms supersede or are in addition to ISO/IEC 19790 and ISO/IEC 24759 throughout this document:

R-0015 · no candidate (hunted)

<!-- q L211 -->
> CCCS Canadian Centre for Cyber Security

<!-- q L213 -->
> CMVP Cryptographic Module Validation Program

<!-- q L215 -->
> CSD Computer Security Division

<!-- q L217 -->
> CSTL Cryptographic and Security Testing Laboratory

<!-- q L219 -->
> FIPS Federal Information Processing Standard

<!-- q L221 -->
> FISMA Federal Information Security Management/Modernization Act

<!-- q L223 -->
> NIST National Institute of Standards and Technology

<!-- q L229 -->
> SP 800-XXX NIST Special Publication 800 series document

## §5.1

<!-- q L235-237 -->
> Section 6 of this document specifies any modifications to the minimum information that vendors shall provide to testing laboratories as specified in Annex A of ISO/IEC 19790. Section 6 also addresses any modifications to 6.13 A – Documentation requirements of ISO/IEC 24759.

R-0001 · split into R-0006, R-0007

## §5.2

<!-- q L241 "Modifications" .. "24759." -->
> Modifications will follow a similar format as in ISO/IEC 24759.

R-0016 · no candidate (hunted)

<!-- q L241-242 "For" .. "“sequence_number.”" -->
> For additions to vendor-supplied documentation, requirements will be listed by increasing the “sequence_number.”

R-0017 · no candidate (hunted)

<!-- q L248-249 "Modifications" .. "strikethrough." -->
> Modifications can include a combination of additions using underline and deletions using strikethrough.

R-0002

<!-- q L249 "If" .. "change.”" -->
> If no changes are required, the paragraph will indicate “No change.”

R-0018 · C-0010

## §6.1

<!-- q L255-256 -->
> ISO/IEC 24759 6.13 A- and ISO/IEC 24759 Documentation requirements are modified as indicated below:

R-0019 · no candidate (hunted)

<!-- q L258 -->
> ASA.01: (Documentation – Levels 1, 2, 3, and 4)

R-0020 · no candidate (hunted)

<!-- q L260-262 -->
> This annex {ISO/IEC 19790 Annex A} specifies the minimum documentation which shall be required for a cryptographic module that is to undergo an independent verification scheme {and the documentation shall meet those requirements}.

R-0003 · split into R-0008, R-0009

<!-- q L264 -->
> Required Vendor Information

Sub-heading (C-0011, rejected): introduces VEA.01.02.

<!-- q L266-268 -->
> VEA.01.02: The vendor shall provide documentation for a cryptographic module that fulfils but is not limited to the minimum documentation requirements as specified in the validation authority requirement and management documentation.

R-0004

<!-- q L270 -->
> Required Test Procedures

Sub-heading (C-0012, rejected): introduces TEA.01.02.

<!-- q L272-274 -->
> TEA.01.02: The tester shall verify that the vendor provides documentation for a cryptographic module that fulfils but is not limited to the minimum documentation requirements as specified in the validation authority requirement and management documentation.

R-0005

## Document Revisions

L280-285 print a rotated Document Revisions table: a header (Date, Change) and no rows. It is not normative and carries nothing to quote; pdftotext interleaves it with the running header.

## Inferred

Kind inferred, in our words, in requirements.yaml with derived_from: R-0021, R-0022.

## Source defects

**SD-1** — §6.1 L255-256: the lead-in to the modification names ISO/IEC 24759 twice and no ISO/IEC 19790 annex, while §5.1 (R-0001) says §6 modifies ISO/IEC 19790 Annex A and ISO/IEC 24759 6.13. The assertion it introduces, ASA.01, is the ISO/IEC 24759 6.13 one.

**SD-2** — VEA.01.02 and TEA.01.02 (R-0004, R-0005) set the minimum by the validation authority's requirement and management documentation, which this SP neither names nor cites: §2 lists only ISO/IEC 19790, ISO/IEC 24759 and FIPS 140-3. Both are testable only against whatever CMVP document a laboratory takes that to be.

**SD-3** — rendering, not source: §5.2 (R-0002) marks an addition by underline and a deletion by strikethrough, and the pdftotext -layout rendering every tool reads carries neither. Which words of ASA.01 are CMVP additions, and whether anything was struck, cannot be read from it; the two brace-enclosed passages are printed, but braces are not the notation §5.2 names.
