---
schema: "library-distilled/v1"
id: pci-secure-slc-2-verification
record: pci-secure-slc-2
type: verification
updated: "2026-10-03"
---

# Verification — PCI Secure SLC v2.0 (public material only)

By: claude (independent verifier, did not extract). Effort: max. Date: 2026-10-03. Verify-only. There are no
requirements, so no cross-check pass applies.

## Licence-walled content

**None was used.** The record's `content.sha256` (`a13e1aaa…c7a363`) matches `.cache/lane-f/pci-blog-v2.html`, which is
the public PCI SSC blog post of 28 Sep 2026. The only other cached sources are:
- the public RFC blog of 15 May 2026 (`pci-rfc.*`);
- the public Secure SLC standard page (`pci-slc-page.*`).

No PCI Document Library file (standard, ROV, AOV, Program Guide) is in `.cache/`. Nothing in the record quotes
requirement, control-objective or test-procedure text. The v1.x numbers that appear in `etsi-ts-104-219` Annex B.2 are
explicitly marked as not evidence for v2.0.

## Every claim checked against a public page

| claim | public source (cached) | result |
|---|---|---|
| v2.0 released 2026-09-28; first major revision; one of two SSF standards | blog 2026-09-28 | supported |
| "refocused solely on a software vendor's Secure SLC"; requirements "objective"; "varying levels of maturity" | blog 2026-09-28; RFC 2026-05-15 | supported |
| sensitive assets; SAID; "digital tools" incl. AI | blog 2026-09-28 | supported |
| neither standard requires assessment to the other; programme benefits for listed products | blog 2026-09-28 | supported |
| document list (standard, Summary of Changes, Program Guide, ROV v2.0, AOV, AQR 2026) | blog 2026-09-28 | supported |
| CBT and ILT in Q4 2026; 12-month transition from v1.1 once training is available | blog 2026-09-28 | supported |
| intended audience; assessors qualified and trained by PCI SSC; Secure SLC-Qualified Software Vendors listing; payment brands manage compliance | standard page | supported |
| companion Secure Software Standard v2.0 "(January 2026)" | blog says only "earlier this year"; PCI SSC blog "PCI SSC Releases Version 2.0 of the PCI Secure Software Standard" (15 Jan 2026, public) | supported (date from a second public page) |

## Object model

- 16 objects and 9 edges, each with a public-page locator.
- 3 edges are `inferred` (performs, attests, identifies), and that is honest: the pages list the documents and name
  SAID, but do not state these relations.
- `tmodel_mapping` values are consistent with ARCH-0001 and DL-0009 (SecurityProgram is a DL-0009 term).
- No defects.

## Defects

None. The record status `summarized` and `confidence: low` are appropriate.
