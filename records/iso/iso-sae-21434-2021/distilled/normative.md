---
schema: "library-normative/v1"
id: iso-sae-21434-2021-normative
record: iso-sae-21434-2021
type: normative
updated: "2026-10-02"
coverage: "Clause 15 TARA, the Fig 3 object model, Table 1 feasibility, key Clause 3 terms, audit mapping. Annexes NOT distilled."
reviewed_by: ""
---

# ISO/SAE 21434 — distilled normative content

> Compacted so an implementer can build the model without re-reading the source.
> Requirement ids resolve in `requirements.yaml`. **Coverage baseline:** the standard
> tags every obligation, so the baseline is marker count, not a verb grep —
> **118 requirements (101 RQ shall / 13 RC should / 4 PM may) + 42 work products.**
> A distillation missing any marker has failed; all 118+42 are catalogued.

## 1. Object model (Figure 3 — item, function, component and related terms)

Typed edges (a ready candidate object model for ARCH-0001 / #17), read from Figure 3 tail to head
(checked on a page image on 2026-10-02; an earlier
version had the item and function edge reversed and the wrong source for `contains` and
`allocated to`):

- `item` **implements** `function(s)`; `item` **contains** `asset`; `item` **consists of** `component`
- `cybersecurity property` **attribute of** `asset`
- `cybersecurity goal` **protects** `asset`; **associated with** `item`; **associated with**
  `threat scenario`; **realized by** `cybersecurity requirement`
- `cybersecurity requirement` **allocated to** `item`; **allocated to** `component`
- `threat scenario` **compromises** `cybersecurity property`; **realizes** `damage scenario`
- `damage scenario` **affects** `road user`

## 2. TARA pipeline (Clause 15) — the risk method

Ordered, each step a requirement + a work product:

| step | clause | requirement(s) | work product |
|---|---|---|---|
| Damage scenarios | 15.3 | RQ-15-01 | WP-15-01 |
| Asset identification | 15.3 | RQ-15-02 | WP-15-02 |
| Threat scenario identification | 15.4 | RQ-15-03 (targeted asset + compromised property + cause) | WP-15-03 |
| Impact rating | 15.5 | RQ-15-04 (categories **S,F,O,P**), RQ-15-05 (**severe/major/moderate/negligible**), RQ-15-06 (safety ← ISO 26262) | WP-15-04 |
| Attack path analysis | 15.6 | RQ-15-08, RQ-15-09 | WP-15-05 |
| Attack feasibility rating | 15.7 | RQ-15-10 (per **Table 1**), RC-15-11 (method) | WP-15-06 |
| Risk value determination | 15.8 | RQ-15-15, RQ-15-16 | WP-15-07 |
| Risk treatment decision | 15.9 | RQ-15-17 | WP-15-08 |

### Table 1 — Attack feasibility ratings
| rating | the attack path can be accomplished utilising… |
|---|---|
| High | low effort |
| Medium | medium effort |
| Low | high effort |
| Very low | very high effort |

**RC-15-11** — feasibility method is one of: (a) attack-potential-based; (b) CVSS-based;
(c) attack-vector-based. (Detailed criteria are in the Annexes, not distilled here.)

## 3. Key terminology (Clause 3, selected)

- **asset** — object with cybersecurity property whose compromise leads to a damage scenario.
- **cybersecurity property** — attribute of an asset (e.g. confidentiality, integrity, availability).
- **damage scenario** — adverse consequence for a road user, involving a vehicle.
- **threat scenario** — potential cause of compromise of a cybersecurity property of ≥1 asset.
- **attack path** — set of deliberate actions to realise a threat scenario.
- **attack feasibility** — attribute of an attack path describing ease of successful execution.
- **item** — component or set of components implementing a function at vehicle level.
- **component** — part logically/technically separable.
- **weakness** — defect/characteristic that can lead to undesirable behaviour (cf. CWE).
- **vulnerability** — weakness that can be exploited (cf. CVE).
- **work product** — result of activities that fulfil requirements (the auditable evidence).

## 4. Requirement / work-product structure → audit automation (tmodel #15)

Every `[RQ]` produces one or more `[WP]` (e.g. `WP-15-05 = Attack paths, from RQ-15-08/09`).
Because **conformance is itself audited** (§6.4.8 cybersecurity assessment; §5.4.7 audit),
this structure is the template for automating the mechanical parts of an audit:

- model **Requirement → produces → WorkProduct → evidenced_by → Evidence → for_product → Product@version**;
- **audit = query**: for a scope, enumerate applicable requirements → required work products →
  check evidence exists and is human-reviewed-adequate → emit a coverage/gap report;
- **tailoring** (Clause 6) is recorded with rationale and is itself auditable;
- the KG automates coverage/traceability/gaps; a **human judges adequacy**.

`requirements.yaml` (RQ/RC/PM + work_products with `resulting_from`) is the seed dataset.
