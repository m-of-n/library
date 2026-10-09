---
schema: "library-summary/v1"
id: openssf-scorecard-checks
record: openssf-scorecard-checks
type: summary
updated: "2026-10-02"
---

# OpenSSF Scorecard — Check Documentation (v5.5.0)

|  |  |
|---|---|
| **Type** | web (generated check documentation of a tool; secondary reference) |
| **Maturity** | implementation — the documented behaviour of a released tool, not a standard |
| **Authors** | OpenSSF Scorecard Authors |
| **Published** | v5.5.0, 2026-04-23 (GitHub release) |
| **Identifier** | `docs/checks.md` @ tag `v5.5.0` (generated from `docs/checks/internal/checks.yaml`) |
| **Source** | https://github.com/ossf/scorecard/blob/v5.5.0/docs/checks.md |
| **Digest** | `ccfc71f01d63507cce12fd604838ababd2c2923dba3bbcd90342ab39cbe817e2` (raw `docs/checks.md` @ v5.5.0) |

**Version verified 2026-10-02:** the GitHub releases API for `ossf/scorecard`
(https://api.github.com/repos/ossf/scorecard/releases) lists v5.5.0 (2026-04-23) as the newest
release, after v5.4.0 (2025-11-14) and v5.3.0 (2025-09-30). The docs are pinned to that tag, not
to `main`. Also read at the same tag: `README.md` (§Scoring, §Project Non-Goals),
`probes/*/def.yml` (48 probes), `probes/entries.go` (check → probe wiring), `finding/finding.go`
and `checker/check_result.go`.

## Overview

Scorecard runs 20 automated checks against a source repository. Each check returns a score from 0
to 10, or "?" (inconclusive, -1) when it has no reliable data. The README combines them into an
aggregate weighted by each check's risk: Critical 10, High 7.5, Medium 5, Low 2.5. Since v5, each
check is built from atomic **probes**. A probe asks one boolean question, for example "are releases
signed?" or "is the repo archived?". It emits findings with an outcome of True, False,
NotApplicable, NotSupported, NotAvailable or Error. The documentation is heuristic by design. Its
non-goals say Scorecard is not "a definitive report or requirement that all projects should
follow", and that an aggregate score "tells you nothing about what individual behaviors a
repository is or is not doing". For an SDL, Scorecard is the most widely deployed *automated
evidence collector* for repository-level practices: branch protection, code review, pinned
dependencies, token permissions, SAST, fuzzing, signed releases with provenance, SBOM and a
security policy.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | measures the supply-chain and repository-hygiene controls that SSDF PS/PW, the OSPS Baseline and SLSA require |
| Cryptography | adjacent | records only whether signatures and provenance are present; it explicitly does not verify signatures |
| This project | adjacent | its Check → Probe → Finding(outcome) pattern is a working model of automated conformance (R-042) and of a probe-level crosswalk to a baseline (R-044). It is not something tmodel must conform to |

Bears on **R-042**: an automated conformance check with a graded result, an inconclusive state and
evidence findings. Bears on **R-044**: probes are the unit the README says the OSPS Baseline
approach uses. Bears on **R-040**: Security-Policy and SBOM are documentation-kind mitigations, and
Branch-Protection is a technical one.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| scorecard (CLI, library, API) | open source tool | Apache-2.0 | https://github.com/ossf/scorecard |
| scorecard-action | GitHub Action | Apache-2.0 | https://github.com/ossf/scorecard-action |
| Allstar | policy-enforcement bot that uses Scorecard checks | Apache-2.0 | https://github.com/ossf/allstar |
| scorecard.dev | weekly public scan results and API | service | https://scorecard.dev |

Searched 2026-10-02.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/README.md` | index of the distilled artifacts |
| `distilled/requirements.yaml` | all 20 checks and all 48 probes, scripted from the v5.5.0 YAML. Each check has its verbatim short text, description, scoring-criteria lines and remediation, plus its risk, weight and probe list. Each probe has its verbatim short text, motivation, implementation, outcome rules, remediation and ecosystem |
| `distilled/object-model.yaml` | object-model pass: 32 objects, 29 edges and 5 gaps, each with a locator |
| `distilled/object-model.md` | Mermaid class diagram and the findings for tmodel |

This is a secondary reference, so its status is `summarized`. The FX-1 artifact set (normative,
schema, messages, protocol, state machine, examples, design notes) was not produced, because the
lane brief scopes Scorecard as summary + requirements + object model.

## Limits

- **Heuristics, not requirements.** A check measures what the forge API can see. Scorecard checks
  that artifacts are *present*. It does not check whether they *work*: Signed-Releases ignores
  whether a signature is valid, and Fuzzing detects that fuzzing is integrated, not how much it
  covers. A good score is weak evidence of conformance.
- **Forge-bound.** Most checks need GitHub. Some also support GitLab or Azure DevOps. Several
  Branch-Protection settings need an admin token. Without one, those settings "can be safely
  ignored", in the documentation's words, and are scored as if met.
- **Scores drift between releases.** The README says scores "change as we add new heuristics". A
  score must cite the Scorecard version that produced it.
- **No SDL phases or gates.** Checks have tags such as supply-chain, security and testing, not
  lifecycle phases. The `phase` values in requirements.yaml are our own assignment.
- **The scoring rubric is prose inside `description`.** `scoring_criteria_lines` lifts the matching
  lines verbatim, but it is a regex selection, so a reader should still consult `text`.
