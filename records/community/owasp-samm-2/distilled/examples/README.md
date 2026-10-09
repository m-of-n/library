---
schema: "library-examples/v1"
id: owasp-samm-2-examples
record: owasp-samm-2
type: examples
updated: "2026-10-02"
---

# Examples — SAMM scoring fixtures

SAMM v2.2.0 ships **no worked examples** in its core model. These fixtures are
**constructed by this library** to pin the scoring rule that the release's
official toolbox spreadsheet implements (`state-machine.yaml` → `scoring`, with
the cell formulas cited). Each fixture gives answers as answer values
(0 / 0.25 / 0.5 / 1) per stream (A, B) per level (1, 2, 3) and the expected
practice score. They are tests of *our reading* of the formulas, not quotations.

| file | what it pins |
|---|---|
| `full-level-1.yaml` | all level-1 answers "most or all" → practice score 1.0 |
| `non-cumulative.yaml` | level 1 = 0 and level 2 = 1 still scores 1.0 — levels are not gated |
| `mixed.yaml` | partial answers across levels and streams |
| `answer-sets.yaml` | every one of the 24 answer sets, verbatim option texts and values |
| `score.py` | the checker for the three scoring fixtures |

Expected results reproduce with `score.py` in this directory
(`python3 score.py *.yaml` except `answer-sets.yaml`): `practice = Σ_level mean(A_level, B_level)`.
