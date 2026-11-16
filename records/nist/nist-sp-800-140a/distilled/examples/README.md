---
record: nist-sp-800-140a
kind: examples
title: "nist-sp-800-140a — examples and test vectors"
extracted: "2026-11-15"
reviewed_by: ""
---

# Examples and test vectors

**Finding: SP 800-140A contains no worked example, sample documentation set, test vector or fixture.** Its section 6.1 consists of the modification of one assertion and its two evidence items:

<!-- q L266-268 -->
> VEA.01.02: The vendor shall provide documentation for a cryptographic module that fulfils but is not limited to the minimum documentation requirements as specified in the validation authority requirement and management documentation.

<!-- q L272-274 -->
> TEA.01.02: The tester shall verify that the vendor provides documentation for a cryptographic module that fulfils but is not limited to the minimum documentation requirements as specified in the validation authority requirement and management documentation.

There is nothing to turn into a fixture.

## What is here instead

`documentation-cases.derived.json` holds this library's own cases for `MinimumDocumentation`: 16 cases, 2 expected to be accepted and 14 expected to be rejected, each with `expect` and a reason. `../schema/build.derived.py` re-validates all of them and exits 1 on any difference.
