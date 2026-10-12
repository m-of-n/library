---
record: slsa-1-2
kind: examples
title: "slsa-1-2 — examples and test vectors"
extracted: "2026-10-02"
reviewed_by: ""
---

# SLSA v1.2 examples and vectors

`vectors.yaml` is the index: 21 fixtures, each with its source and expected result.

| dir / file | what |
|---|---|
| `verbatim/` | every example code block of the spec, byte-for-byte (dedented): predicateType strings, the external-parameters/resolved-dependencies fragment, the VSA and Source VSA examples, the build/source roots-of-trust maps, the v0.2→v1 migration snippet |
| `normalized/` | mechanical JSON renderings of verbatim fragments, so they can be schema-checked (comments and trailing commas removed). The VSA and Source VSA examples validate against the derived schemas; the parameters fragment is illustrative only |
| `external/` | the GitHub Actions workflow buildType's complete example predicate, linked from the spec's buildType index. It is not spec text |
| `derived/` | 10 library-made negative vectors, each a single mutation named for the requirement it breaks. 9 are rejected by the derived schemas; 1 (R-0236) is invalid but cannot be detected by a schema |
| `threat-scenarios.yaml` | the 54 example attacks from threats.md (A–I and the dependency, availability and verification threats). 16 of them carry the spec's stated verifier outcome (REJECT …) |
| `vsa-verification-cases.yaml` | the two verification cases the spec states for the VSA example (case 1 FAIL, case 2 PASS) |
