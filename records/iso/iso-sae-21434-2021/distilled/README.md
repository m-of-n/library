---
schema: "library-doc/v1"
id: iso-sae-21434-2021-distilled-index
record: iso-sae-21434-2021
type: index
audience: human   # orientation for people; the machine source is requirements.yaml
updated: "2026-10-03"
---

# Distilled artifacts — ISO/SAE 21434:2021

**Audience of each file:** `requirements.yaml` is the **machine/AI** source of truth (canonical, queryable, audit-typed). `requirements.md` is the **human** view, *generated* from the YAML (do not hand-edit). `normative.md` is human + AI reading. This `README` orients people.

Progressive distillation. Nothing here is reviewed line-by-line yet (`reviewed_by`
empty on each artifact); a human pass is required before treating any requirement
as authoritative.

| artifact | what it is | coverage |
|---|---|---|
| `requirements.yaml` | **machine source.** 118 requirements + 42 required deliverables, audit-typed: normativity, actor, nature (process vs deliverable-producing), expects_deliverables, verification, tailorable, refs, external_refs | all normative statements, full text; derived fields need review |
| `requirements.md` | **human view, generated.** Per-clause table: designator, normativity, nature, actor, short title, deliverables | all 118 + 42 |
| `normative.md` | TARA pipeline (Clause 15), Fig 3 object model, Table 1 feasibility, key Clause 3 terms, audit-automation mapping | overview; **Annexes not distilled** (impact tables F, feasibility methods) |

## Not yet done (next passes)
- Line-by-line human review of `requirements.yaml` (set `reviewed_by`, fix any truncation/verb drift).
- Fix the 16 wrong texts listed in `summary.md` (Limits), once the sponsor decides whether this public repository may hold the standard's verbatim text.
- Done 2026-10-02: every provision and work-product locator points to the subclause that holds it, and every provision-to-work-product link the standard names is recorded (RPT-0007 §7).
- Done 2026-10-03: the 10 work products that the standard ties to subclauses rather than provisions list them in `from_subclauses`, so every work product now records what it results from. The provisions in those subclauses do not list these work products; find them by locator.
- Annex distillation: impact-rating criteria (Annex F) and attack-feasibility methods (attack-potential / CVSS / attack-vector). tmodel RPT-0007 §3 and §4 summarize Annexes E to H in its own words.
- `fields.yaml` + a `schema/` encoding of the object model, once the model is chosen (#17).
