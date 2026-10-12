---
record: cncf-supply-chain-best-practices-v2
kind: verification
title: "cncf-supply-chain-best-practices-v2 — verify pass (secondary reference)"
date: "2026-10-02"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# CNCF Software Supply Chain Best Practices v2: verification report

This is a lighter, verify-only pass. The record is `status: summarized`, so no cross-check pass is
recorded.

Sources:

- `.cache/cncf-supply-chain-best-practices-v2.md` (= `SSCBPv2.md`);
- `.cache/lane-e/sec/sscbp-v2.pdf`;
- `.cache/lane-e/sec/sscp-v1.pdf`.

## Checks

1. **Hash and currency.**
   - `SSCBPv2.md` was re-fetched live and hashes `e2087a3f…3f33` = `content.sha256`. ✔
   - The PDF hashes `0af09b1f…250b`, which matches the `record.yaml` comment.
   - The `cncf/tag-security` repository is `archived: true`, last pushed 2025-12-08.
   - The last commit in the v2 folder is #1461, "Add sscs best practices v2 pdf", 2025-03-20.
   - The PDF metadata gives a creation date of 2025-03-11 and 37 pages. The "Published" field still
     reads `xxxxxxxxx`.
   - v1 (`sscp-v1.pdf`) is 45 pages, created 2021-05-14.
   - **v2 is current.** ✔
2. **Verbatim.** All 59 extract-pass texts are verbatim against the Markdown.
3. **Locators.** Every `SSCBPv2.md line N` locator was checked against the heading lines, for
   example 601, 652, 894, 906, 908, 1081, 1176 and 1206. All point at the named heading.
4. **Completeness.** Stage counts were recomputed from the headings:
   - Source Code 11;
   - Materials 9;
   - Build Pipelines 24;
   - Artifacts 9;
   - Deployments and Distribution 6.

   **Defect V-1 (dropped), fixed:**
   - The level-3 subsection "Second and Third-Party Risk Management" (Materials, line 716) is a
     practice section, not stage-intro prose. It carries several "should" practices:
     risk-management processes, operational-health metrics such as Scorecard, monitoring changes,
     and vendors listing changes.
   - Pass 1 itemized only level-4 and level-5 headings, so this section was dropped.
   - It was added as `P-060`, with its body verbatim from lines 718–742. The header counts are now
     practices 60 and Materials 10, and the `record.yaml` coverage was updated.
5. **Typing.** Every entry is `recommendation`, with no levels, which is faithful because the paper
   states none. `modal_words_in_text` holds for the spot-checked entries.
   - `P-025` ("Recommendations For Reproducible Builds") has empty text. That is faithful: the
     heading has no body. A note now says so, and names its children `P-026`..`P-030`.
6. **Object model.**
   - Locators are section paths, and the spot checks hold (Attestations, Root of Trust, 2-party
     review).
   - `ThirdPartySupplier` was located in the subsection that is now `P-060`.
7. **Claims in `summary.md`.** Confirmed:
   - the authors and reviewers on the PDF title page;
   - the archived repository;
   - the dates;
   - the SLSA A–I stage mapping (Markdown lines 551–570).

   **Defect V-2, fixed.** Two digests were mistyped.
   - `summary.md` gave the v1 PDF digest as `be96fbd8…3f33`. The actual value is `be96fbd8…fa4b`;
     the `…3f33` tail belongs to the v2 Markdown digest.
   - `requirements.yaml` `note` gave the v2 PDF digest as `0af09b1f…a489`. The actual value is
     `…250b`.

   Both were corrected.

## Residual (not fixed in a verify-only pass)

- 8 objects have no edge: `ContainerRegistry`, `SoftwareConsumer`, `SoftwareDistributor`,
  `Credential`, `Verifier`, `BuildTool`, `Metadata` and `BuildEnvironmentRecord`.
- Stage-introduction prose with lowercase must/should, for example Materials: "Producers must take
  care to verify the quality of these materials.", is still not itemized. The record states this
  scope limit.
- `reviewed_by` is empty.
