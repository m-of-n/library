---
record: nist-sp-800-140b
kind: examples
title: "nist-sp-800-140b — examples and test vectors"
extracted: "2026-11-15"
reviewed_by: ""
---

# Examples and test vectors

**Finding: SP 800-140B contains no worked example, sample security policy or test vector.** Every table is an empty template whose caption reads 'Table x', for instance:

<!-- q L416-417 -->
> … Table x - Tested Operational Environments

and the only illustrative figure of a value is an aside about counting seals:

<!-- q L736-737 -->
> o The total number of tamper-evident seals or security appliances that are needed will be indicated (e.g., five tamper-evident seals and two opacity screens). The

## What is here instead

`security-policy-cases.derived.json` holds this library's own cases for the 22 schemas in `../schema/`: 323 cases, 27 expected to be accepted and 296 to be rejected, each with `expect` and a reason. The cases include the empty object and each mandatory field omitted in turn. `../schema/build.derived.py` re-validates every case with jsonschema and exits 1 on any difference.
