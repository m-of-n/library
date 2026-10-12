---
record: openssf-scorecard-checks
kind: verification
title: "openssf-scorecard-checks — verify pass (secondary reference)"
date: "2026-10-02"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# OpenSSF Scorecard checks v5.5.0: verification report

This is a lighter, verify-only pass. The record is `status: summarized`, a secondary reference, so
no cross-check pass is recorded. Comparisons were made against the v5.5.0 sources in
`.cache/lane-e/sec/`: `scorecard-checks-v5.5.0.yaml` (= `docs/checks/internal/checks.yaml`), 48
`probes/*.yml`, `entries.go`, `finding.go`, `check_result.go` and `scorecard-README.md`.

## Checks

1. **Hash and currency.**
   - `docs/checks.md` at the v5.5.0 tag was re-fetched live and hashes `ccfc71f0…17e2` =
     `content.sha256`. ✔
   - The releases API shows v5.5.0 (2026-04-23) as the newest release, after v5.4.0 and v5.3.0.
     The record is current. ✔
2. **Verbatim.**
   - 20/20 checks: `short`, `text` (full description) and `risk` are identical to `checks.yaml`;
     `remediation` is identical.
   - 48/48 probes: `short`, `text` (= `motivation`), `implementation`, `outcome` and `remediation`
     are identical to each `probes/<id>.yml`.
3. **Locators and wiring.** Probe → check assignments equal `probes/entries.go`, for example
   Branch-Protection 11, Security-Policy 4, Maintained 4 and Token-Permissions 3, plus 4
   Uncategorized and 1 Independent. Risk weights equal README §Aggregate Score: Critical 10,
   High 7.5, Medium 5, Low 2.5.
4. **Completeness.** All 20 checks and all 48 probes are present. `bin/bcp14-count` gives 0, so 0
   = 0.
5. **Defect V-1, fixed: fragmentary `scoring_criteria_lines`.** Pass 1 had lifted wrapped physical
   lines of the description. Several started mid-sentence ("a low score on this test. …") or
   mid-link ("issue](https://github.com/…)"), and some were not about scoring at all ("Allowed by
   Scorecard:"). They were regenerated as the whole sentences and list items of the unwrapped
   description that mention score or points. All are verified as verbatim substrings, and the
   header `note` records the change.
6. **Typing.** Every `normativity` is `heuristic-check` or probe. `phase`, `nature` and `actor` are
   declared derived. Nothing claims BCP 14 force.
7. **Object model.** All 32 objects and 29 edges carry locators into the v5.5.0 tree.
8. **Claims in `summary.md`.** The following are confirmed against source:
   - the release order;
   - "?" means `InconclusiveResultScore = -1` (`check_result.go`);
   - the six finding outcomes (`finding.go`);
   - the README non-goal "a definitive report or requirement that all projects should follow" and
     "tells you nothing about what individual behaviors…".

## Residual (not fixed in a verify-only pass)

- 4 objects have no edge: `License`, `Webhook`, `Ecosystem` and `BinaryArtifact`.
- One edge, `maps_to_baseline → "OSPS Baseline AssessmentRequirement"`, is a cross-record endpoint
  marked inferred. It should point at `openssf-osps-baseline` ids. The OSPS → Scorecard mapping
  (`osps-to-scorecard.yaml`, 11 check names, all present in v5.5.0) is the authoritative direction.
- `reviewed_by` is empty.
