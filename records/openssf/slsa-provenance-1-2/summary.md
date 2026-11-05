---
schema: "library-summary/v1"
id: slsa-provenance-1-2
record: slsa-provenance-1-2
type: summary
updated: "2026-11-04"
---

# SLSA Build Provenance (SLSA Specification v1.2)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | standard: the page's Status is Approved, the stable stage in SLSA's spec-stages definitions |
| **Authors** | SLSA project contributors (slsa-framework) |
| **Published** | 2025-11-24, Open Source Security Foundation (OpenSSF) |
| **Identifier** | `https://slsa.dev/provenance/v1` |
| **Source** | https://slsa.dev/spec/v1.2/build-provenance |
| **Digest** | `sha256:04a97c9b…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

Provenance is an in-toto predicate, `https://slsa.dev/provenance/v1`, stating that a build platform produced some artifacts by executing a `buildDefinition`. The model's central split is trust: `externalParameters` are untrusted and must be verified downstream, while `internalParameters` come from the platform and need not be. `builder.id` names the transitive closure of everything trusted to run the build and record it, and is meant to be the sole determiner of the Build level. Consumers must accept only specific signer and builder pairs, because the builder and the signer are distinct. Minor versions never change the predicate type, so the URI stays `v1`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Separates what is attested from what is merely reported, and says who is trusted for each |
| Cryptography | `adjacent` | No cryptography. Signing is left to the in-toto envelope |
| This project | `core` | The most likely `predicate_type` for an R-I-03 export, and a direct contrast with our own extension rule |

- **R-I-03**: the concrete predicate an export to in-toto Statement + DSSE would carry.
- **R-I-01**: the mapping table must say what is lost. `builder.id` has no key in it, and the signer and builder pair is out-of-band consumer configuration.
- **R-M-07**: `subject` and `resolvedDependencies` bind digests. *BuildDefinition* shows the limit: `resolvedDependencies` is best effort, even at Build L3.
- **R-M-12**: a direct contrast. Types here are URIs and extension fields are `<vendor>_<fieldname>`, resolved by naming convention and not relative to a key. *Extension fields* is still a useful statement of monotonicity: deleting an extension should not turn a DENY into an ALLOW.

## Implementations

**Searched 2026-11-01.** GitHub repository metadata checked. Covered at spec level by `slsa-1-2`, so only the direct tooling is listed.

| Name | Kind | License | URL |
|---|---|---|---|
| slsa-verifier | open source, verifier | Apache-2.0 | https://github.com/slsa-framework/slsa-verifier |
| slsa-github-generator | open source, generator | Apache-2.0 | https://github.com/slsa-framework/slsa-github-generator |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

**Relations.** No `see_also`. The page links in-toto's Statement, ResourceDescriptor and parsing rules (`in-toto-attestation-v1`) and other pages of SLSA v1.2 (`slsa-1-2`), so both sit under `cites`. `slsa-vsa-1-2` cites this record, and `in-toto-attestation-v1` and `slsa-2026-mini-shai-hulud` author their own edges to it. The page does not mention DSSE.

## Limits

- **Provenance is evidence, not a verdict.** The page defers verification to *Verifying Artifacts*, which this record does not hold separately (it is part of `slsa-1-2`, which this record cites).
- **Unknown fields are ignored.** *Parsing rules* carries the in-toto rule, the opposite of a must-understand design. `in-toto-attestation-v1` records why that matters.
- **Stale version reference.** *Purpose* still calls this predicate the RECOMMENDED way to satisfy the SLSA v1.0 provenance requirements, on the v1.2 page.
- **The field-level text wins over the schemas.** Both the cue summary and the protobuf are marked informative.
- **Mini Shai-Hulud shows the boundary.** `slsa-2026-mini-shai-hulud` records attestations that stayed accurate while the build was compromised.
- **Read scope.** The whole build provenance page was read as rendered HTML, plus the hub at the recorded URL. Source provenance, the sibling page, was not read and is not covered.
