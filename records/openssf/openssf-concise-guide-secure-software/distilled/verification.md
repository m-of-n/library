---
record: openssf-concise-guide-secure-software
kind: verification
title: "openssf-concise-guide-secure-software — verify pass (secondary reference)"
date: "2026-10-02"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# Concise Guide for Developing More Secure Software: verification report

This is a lighter, verify-only pass. The record is `status: summarized`, so no cross-check pass is
recorded. The source is `.cache/openssf-concise-guide-secure-software.md`, the raw `main` Markdown.

## Checks

1. **Hash and currency.**
   - The raw Markdown on `main` was re-fetched live on 2026-10-02 and hashes `adb2925c…572c` =
     `content.sha256`. The page is unchanged since extraction. ✔
   - The latest commit to the file is `99c65a8522`, 2026-09-19, "Add cooldowns to an existing point
     (#1136)". Earlier commits fall in 2025-03, 2025-04 and 2025-01. The byline still reads
     2023-06-14. All of this matches `summary.md`. ✔
2. **Verbatim.** 29/29 item texts are verbatim: each equals the full source item, including the
   continuation lines of item 11 (three sub-bullets) and item 29 (link list). There is no
   truncation.
3. **Locators.** Each `numbered item N` points at the Nth numbered item: 29/29.
4. **Completeness.** The source has 29 numbered items and all are extracted. The preamble and the
   closing "We welcome suggestions" line are not practices. `bin/bcp14-count` gives 0, so 0 = 0.
5. **Typing.** Every item is `recommendation` / imperative, and `kind` is stated. Item 27 holds a
   lowercase "should" and is still typed recommendation. That is consistent with the guide's
   advisory status.
6. **Object model.** Objects and edges carry item locators. Spot checks hold: items 3, 7 and 9 for
   SecurityTool, item 10 for ChangeReview, item 23 for SecurityAudit and item 28 for WebAsset.
7. **Claims.** Confirmed: the byline, the commit history and the "for all software developers …"
   quote. In `record.yaml`, the `cites` entry for item 20 correctly says the guide links the CNCF
   **v1** PDF (`CNCF_SSCP_v1.pdf`) while the library holds v2. That edition mismatch is stated
   honestly.

## Defects

None found that needed fixing.

## Residual

- 4 objects have no edge: `DeprecationProcess`, `AutomatedTestSuite`, `VendoredDependency` and
  `TrainingCourse`.
- `reviewed_by` is empty.
