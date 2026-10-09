---
schema: "library-distilled/v1"
id: cis-safecode-sbd-assessment-1-1-verification
record: cis-safecode-sbd-assessment-1-1
type: verification
updated: "2026-10-03"
---

# Verification — CIS/SAFECode Secure by Design v1.1 (public material only)

By: claude (independent verifier, did not extract). Effort: max. Date: 2026-10-03. Verify-only. There are no
requirements, so no cross-check pass applies.

## Licence- or registration-walled content

**None was used.** `content.sha256` (`aa7bf245…16f36e`) matches `.cache/lane-f/cis-wp.html`, the public CIS landing
page. The other cached sources are public:
- the CIS press release, 15 Jul 2026;
- the SAFECode press release, dateline 14 Jul 2026, posted 16 Jul;
- the SAFECode blog, 13 Jul 2026.

The registration-walled zip (PDF + XLSX) is not in `.cache/`, and no guide content is quoted.

## Every claim checked against a public page

| claim | public source (cached) | result |
|---|---|---|
| landing page "Published on July 9, 2026"; zip of PDF + XLSX | CIS landing page | supported |
| guide "underlies a new ETSI standard"; v1.1 "is consistent in content with the new ETSI standard" | CIS landing page; SAFECode blog 2026-07-13 | supported |
| based on NIST SSDF; maps practices to CIS Controls, SAFECode DGs, organizational roles, development artifacts | CIS press release 2026-07-15; SAFECode press release | supported |
| six considerations (… "Vulnerability Remediation") | press releases | supported |
| AI topics; AI-generated code subject to the same testing, review and validation | press releases | supported |
| audiences (developers, acquirers, agencies, assessors, policymakers) | press releases | supported |

## Defect fixed

summary.md gave Type "paper" and Maturity "white-paper", but record.yaml has `type: spec` and
`maturity: best-practice`. The summary table now matches the record, and notes that the guide is published as a CIS
white paper.

## Object model

- 9 objects and 6 edges, each with a public-page locator, all `stated`. All are supported by the press releases and
  landing page.
- The `same_content_as` edge points at an object in another record ("ETSI TS 104 219 Essential"), which is not a local
  object. That is acceptable as a cross-record reference, and the target is defined in
  `etsi-ts-104-219/distilled/object-model.yaml` (Essential).
