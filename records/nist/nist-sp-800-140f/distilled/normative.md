---
record: nist-sp-800-140f
kind: normative
title: "nist-sp-800-140f — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every requirement text in requirements.yaml that has source lines appears here verbatim under its section, as a marker that `bin/check-quotes --render` writes and `bin/check-quotes` verifies; split_of children are listed on their parent's line rather than quoted twice. Binding text that is not an entry (scope statements, normative references, definitions, abbreviations, sub-headings, captions and placeholder rows) is quoted the same way, with no id. Sections follow the source's own headings in source order; where requirements.yaml carries a skeleton locator that differs, the id line says so. requirements.yaml holds 14 entries: 1 skeleton, 1 split child, 1 from candidates, 10 hunted, 0 other table rows and 1 inferred.

## §1

<!-- q L185-187 "This" .. "conformance." -->
> This document specifies the Cryptographic Module Validation Program (CMVP) modifications of the methods to be used by a Cryptographic and Security Testing Laboratory (CSTL) to demonstrate conformance.

Scope statement (no entry).

<!-- q L187-188 "This" .. "conformity." -->
> This document also specifies the modification of methods for evidence that a vendor or testing laboratory provides to demonstrate conformity.

Scope statement (no entry).

<!-- q L188-190 "Unless" .. "6.18." -->
> Unless otherwise specified in this document, the test requirements are specified in ISO/IEC 24759 paragraph 6.18.

R-0003 · no candidate (hunted)

## §2

<!-- q L194 "This" .. "24759." -->
> This section identifies the normative references cited as ISO/IEC 19790 and ISO/IEC 24759.

<!-- q L194-195 "The" .. "24759:2017." -->
> The specific editions to be used are ISO/IEC 19790:2012 and ISO/IEC 24759:2017.

R-0004 · no candidate (hunted)

<!-- q L195-201 "Please" .. "2015." -->
> Please note that the version 19790:2012 referenced here includes the corrections made in 2015.

R-0005 · no candidate (hunted)

<!-- q L203-206 -->
> National Institute of Standards and Technology (2019) Security Requirements for Cryptographic Modules. (U.S. Department of Commerce, Washington, DC), Federal Information Processing Standards Publication (FIPS) 140-3. https://doi.org/10.6028/NIST.FIPS.140-3

The normative reference to FIPS 140-3.

## §3

<!-- q L210-211 -->
> The following terms and definitions supersede or are in addition to ISO/IEC 19790 and ISO/IEC 24759.

R-0006 · no candidate (hunted)

<!-- q L213 -->
> No additional terms at this time.

## §4

<!-- q L217-218 -->
> The following symbols and abbreviated terms supersede or are in addition to ISO/IEC 19790 and ISO/IEC 24759 throughout this document:

R-0007 · no candidate (hunted)

<!-- q L220 -->
> CCCS Canadian Centre for Cyber Security

<!-- q L222 -->
> CMVP Cryptographic Module Validation Program

<!-- q L224 -->
> CSD Computer Security Division

<!-- q L226 -->
> CSTL Cryptographic and Security Testing Laboratory

<!-- q L228 -->
> FIPS Federal Information Processing Standard

<!-- q L230 -->
> FISMA Federal Information Security Management/Modernization Act

<!-- q L232 -->
> NIST National Institute of Standards and Technology

<!-- q L237 -->
> SP 800-XXX NIST Special Publication 800 series document

## §5.1

<!-- q L243-244 -->
> Section 6 of this document replaces the approved non-invasive attack mitigation test metrics requirements of ISO/IEC 19790 Annex F and ISO/IEC 24759 paragraph 6.18.

R-0008 · no candidate (hunted)

## §5.2

<!-- q L248 "Modifications" .. "24759." -->
> Modifications will follow a similar format as in ISO/IEC 24759.

R-0009 · no candidate (hunted)

<!-- q L248-255 "For" .. "“sequence_number.”" -->
> For additions to test requirements, new Test Evidence (TEs) or Vendor Evidence (VEs) will be listed by increasing the “sequence_number.”

R-0010 · no candidate (hunted)

<!-- q L255-256 "the" .. "strikethrough." -->
> the “sequence_number.” Modifications can include a combination of additions using underline and deletions using strikethrough.

R-0001 · split into R-0002

<!-- q L256-257 "If" .. "change.”" -->
> If no changes are required, the paragraph will indicate “No change.”

R-0011 · C-0010

## §6.1

<!-- q L263 -->
> This document identifies CMVP-approved non-invasive attack mitigation test metrics.

R-0012 · no candidate (hunted)

## §6.2

<!-- q L267 -->
> No additional requirements at this time

R-0013 · no candidate (hunted)

## Document Revisions

L276-288 print a Document Revisions table: a header (Date, Change) and no rows. Not normative.

## Inferred

Kind inferred, in our words, in requirements.yaml with derived_from: R-0014.

## Source defects

**SD-1** — source, open question: §1 (R-0003) keeps ISO/IEC 24759 paragraph 6.18 as the test requirements unless this SP says otherwise; §5.1 (R-0008) has §6 replace Annex F and that paragraph; and §6.2 (R-0013) then specifies nothing. The Abstract (front matter) goes further:

<!-- q L135 -->
> This document supersedes ISO/IEC 19790 Annex F and ISO/IEC 24759 paragraph 6.18.

Read with §1, Annex F's metrics and paragraph 6.18 still apply and this SP adds none; read with §5.1 and the Abstract, they are replaced by an empty list and no approved metric exists. The text does not choose.

**SD-2** — source: §6.1 (R-0012) promises the approved metrics, and §6.2 identifies none.

**SD-3** — reader, fixed: NIST prints the rotated free-of-charge sidebar mid-page with blank lines around it, and the pass-1 PDF reading kept them as a paragraph break; the skeleton cut §5.2's second sentence there, so R-0001 opens on the last words of the sentence before it (whole: R-0010). 63d708e drops the sidebar's blank surround; a skeleton re-run now runs L248-256 together, because the skeleton does not end a sentence after a closing quotation mark (L255).

**SD-4** — rendering, not source: §5.2 marks additions by underline and deletions by strikethrough, which the pdftotext rendering cannot carry; §6 prints no marked-up text.
