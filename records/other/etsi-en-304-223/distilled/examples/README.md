---
record: etsi-en-304-223
kind: examples
title: "etsi-en-304-223 — examples and test vectors"
extracted: "2026-11-15"
reviewed_by: ""
---

# Examples and test vectors

**Finding: the EN contains no worked example, sample artefact, fixture or test vector.** Its only `EXAMPLE` block is one informative sentence about data protection roles in clause 4. It is prose, not a test vector. Nothing in the source can be turned into a fixture with an expected result. Verified by grepping the pinned text (`EXAMPLE`, `for example`, `e.g.`, `such as`) and reading every hit.

The one `EXAMPLE` block (clause 4):

<!-- q L438-440 -->
> EXAMPLE: Under data protection law, when processing personal data, organizations can have a role of controller and/or joint controller and/or processor, depending on their role in creating and setting up AI systems.

Inline illustrations introduced by "for example" inside provisions are informative too. Each is the provision's own aside, not a fixture:

<!-- q L598-599 "For example" .. "system function." -->
> For example, where a multi-modal model is being used but only single modality is used for system function.

<!-- q L684-685 "For example" .. "poison a model." -->
> For example, placing limits on model access rate to limit an attacker's ability to reverse engineer or overwhelm defences to rapidly poison a model.

<!-- q L718-718 "for example" .. "component)." -->
> for example if there was no other supplier for said component).

<!-- q L798-799 "for example" .. "partners)." -->
> for example, if it is used for model retraining, or reviewed by employees or partners).

<!-- q L832-833 "for example" .. "APIs)." -->
> for example by providing preview access via beta-testing and versioned APIs).

## Our instances (derived, not the source's)

`<Name>.cases.derived.json` beside this file, one per schema in `../schema/`, holds instances **we** wrote to test the derived schemas. They are not source test vectors.

Each file has `accept` (instances the schema must accept: the unconditional `shall` fields only, plus the first case of a multi-case structure, and every field populated) and `reject` (instances it must reject, each with `why`): a missing required field, a wrong type or value per field, an additional property, an empty required array, a nested item missing its required field, a `shall` boolean set to `false`, a field missing beside the field it is required with, and a multi-case structure with no case populated. Expected result: every `accept` validates and every `reject` fails against `../schema/<Name>.derived.schema.json`. `python -I ../schema/selftest.derived.py` (with `jsonschema` available) checks all of them.
