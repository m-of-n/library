---
schema: "library-doc/v1"
id: etsi-en-304-223-distilled-index
record: etsi-en-304-223
type: index
audience: human   # orientation for people; the machine source is requirements.yaml
updated: "2026-10-01"
---

# Distilled artifacts — ETSI EN 304 223 V2.1.1

**Audience of each file:** `requirements.yaml` is the **machine/AI** source of truth (one entry
per provision, verbatim text). `requirements.md` is the **human** view, *generated* from the
YAML (do not hand-edit). `normative.md` is the compacted reading for people and agents.

Nothing here is reviewed line by line yet (`reviewed_by` is empty on each artifact).

| artifact | what it is | coverage |
|---|---|---|
| `requirements.yaml` | **machine source.** All 72 provisions of clause 5, keyed by ETSI's designator (`#5.1.2-3`), with normativity, every modal verb, actor, principle, phase, locator, verbatim text, nature, expected deliverables, verification | all 72 provisions: 49 requirements (*shall*), 23 recommendations (*should*) |
| `requirements.md` | **human view, generated.** One table per principle | all 72 |
| `normative.md` | stakeholder roles, the 13 principles by lifecycle phase, the AI-specific threats the standard names, scope, and how it relates to tmodel | overview; the provisions themselves are in the YAML |

## Checks run (docs/distillation.md §4), 2026-10-01

| check | result |
|---|---|
| **Verb baseline** — modal verbs in the clause-5 body vs. in the extracted `text` | shall 59 = 59 · should 28 = 28 · can 5 = 5 · shall not / should not / may 0 |
| **1. Verbatim** — every `text` appears in the source, whitespace normalised | pass, 72/72 |
| **2. Coverage** — every principle subsection (§5.1.1–§5.5.1) cited | pass, 13/13; provisions per principle 5, 9, 7, 5, 7, 6, 6, 6, 6, 5, 4, 4, 2 |
| **3. Verb** — no provision containing *shall* typed weaker than `requirement` | pass |

The baseline is a verb count, not a marker count: the standard numbers every provision
(`Provision 5.x.y-n`) but tags none as requirement or recommendation, so normativity is read
from the verb. Four provisions mix *shall* and *should* (5.1.2-7, 5.1.3-1, 5.1.3-2,
5.2.4-1); they take the strongest, and `verbs` keeps the full list.

## Derived fields — what to review

- `actor`: the stakeholders named before each modal verb. Four provisions name none
  (5.1.1-1.1, 5.1.1-2.1, 5.1.3-1.1, 5.2.4-2.1) and carry `(implied)` actors; two were set by
  hand where the first-named party is not the one obliged (5.1.2-1.1, 5.1.3-3).
- `short_title`, `nature`, `expects_deliverables`, `verification`: written for this
  distillation. EN 304 223 names no work products, so 22 provisions marked
  deliverable-producing carry plain-language descriptions, not designators.

## Not yet done

- Line-by-line human review (set `reviewed_by`).
- Conformance mapping to ETSI TS 104 216 once it is published (still a draft work item).
- Mapping each provision to the tmodel object model (#15/#17) and to automated compliance
  checks (#19).
