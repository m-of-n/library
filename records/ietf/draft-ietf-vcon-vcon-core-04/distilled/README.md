---
schema: "library-distilled-index/v1"
record: draft-ietf-vcon-vcon-core-04
type: distilled-index
updated: "2026-09-22"
---

# Distilled artifacts — vCon core `-04`

**Distillation is progressive.** This record accumulates artifacts as
understanding deepens; each has its own coverage and its own review state.
`status: distilled` on the record means *at least one artifact exists* — it
never means *finished*.

| artifact | kind | covers | generated from | reviewed |
|---|---|---|---|---|
| `normative.md` | normative | §4.1–4.5 data model, §2 conventions, §5 delegation. **Not** §6 IANA, §7 examples, §5 in full | — (hand) | ✗ |
| `fields.yaml` | fields | **54 fields**, all five objects | `normative.md` + `bin/extract-fields` | ✗ |
| `requirements.yaml` | requirements | **33 requirements**, externally referenceable | `fields.yaml` | ✗ |
| `schema/types.cddl` | schema | structural shape only | `fields.yaml` | ✗ |
| `code/types.py` | code | Python dataclasses | `fields.yaml` | ✗ |
| `code/types.rs` | code | Rust serde structs | `fields.yaml` | ✗ |
| `examples/` | examples | **empty** — §7 examples not yet lifted | — | — |

## Reading order
`normative.md` → `fields.yaml` → everything else is derived from the field
table and regenerable with `bin/derive`.

## Generated artifacts are never hand-edited
A defect in `fields.yaml` propagates into requirements, schema and both
languages. **Fix the field table and regenerate.** That is the point of
recording `generated from`: a defect can be traced forward, and a fix reaches
everything.

## What the derived artifacts deliberately do not express

- **Per-type applicability (§4.3.1.6).** A `Dialog` that satisfies the CDDL or
  the Rust struct may still be invalid, because which parameters apply depends
  on `Dialog.type`. **Structural validity is not conformance.**
- **A MUST on a field's *value* is not a MUST on its *presence*.** `vcon`
  carries a MUST constraining its value yet is optional. The generator cannot
  distinguish these; required-ness comes from the field table, where a human
  put it.
- **Cross-field and cross-object constraints.** Index references from
  `Dialog.parties` into the vCon `parties` array are not range-checked anywhere
  in these artifacts.

## Still to distil

| | |
|---|---|
| `Party_History` (§4.3.13.1) | sub-object of `Dialog.party_history` |
| Content carriage (§4.3.10, §4.4.7, §4.5.9) | inline vs. URL vs. encoding rules |
| Dialog Transfer (§4.3.14) | transfer-specific structure |
| §7 examples | → `examples/`, as test vectors |
| A state machine | `Dialog.type` transitions, `redacted`/`amended` chains |

## Review state
**Every artifact is `reviewed_by: ""`.** All are readable; **nothing may be
built on them** until a human other than the author checks them
(`docs/requirements.md` §3). The three mechanical checks pass — 33/33 verbatim
quotes, 58/58 sections cited — but mechanical checks are not review.
