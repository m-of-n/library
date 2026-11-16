---
record: fips-140-3
kind: examples
title: "fips-140-3 — examples and test vectors"
extracted: "2026-11-15"
reviewed_by: ""
---

# Examples and test vectors

**Finding: FIPS 140-3 contains no worked example, sample, test vector or fixture.** The only figure is the implementation schedule, which the source introduces thus:

<!-- q L202-203 "Figure 1" .. "may begin." -->
> Figure 1 summarizes the CMVP implementation schedule when FIPS 140-3 testing may begin.

It is a schedule diagram (dates in months after approval), not an example of any structure, and the `e.g.` lists in paragraphs 7 and 13 are illustrations of kinds of application and adversary, not inputs and expected outputs.

## What is here instead

`security-vocabulary-cases.derived.json` holds this library's own cases for the two derived schemas in `../schema/`: 23 cases, 3 expected to be accepted and 20 expected to be rejected. Each case names its schema, `expect` (`accept` or `reject`) and why; `../schema/build.derived.py` re-validates all of them and exits 1 if any result differs from `expect`.
