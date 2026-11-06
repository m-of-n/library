---
schema: "library-summary/v1"
id: slsa-vsa-1-2
record: slsa-vsa-1-2
type: summary
updated: "2026-11-04"
---

# SLSA Verification Summary Attestation (VSA), SLSA Specification v1.2

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | standard: the page's Status is Approved, the stable stage in SLSA's spec-stages definitions |
| **Authors** | SLSA project contributors (slsa-framework) |
| **Published** | 2025-11-24, Open Source Security Foundation (OpenSSF) |
| **Identifier** | `https://slsa.dev/verification_summary/v1` |
| **Source** | https://slsa.dev/spec/v1.2/verification_summary |
| **Digest** | `sha256:f6234a9f…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

A VSA is an in-toto predicate in which a verifier states that it checked artifacts against a policy, so a consumer can accept the result without seeing the underlying attestations or the transitive dependencies. It serves two purposes: delegating a complex policy decision to a trusted party, and keeping a producer's pipeline confidential. *How to verify* gives seven mandatory consumer steps, covering the envelope signature, `subject`, `predicateType`, `verifier`, `resourceUri`, `verificationResult` and `verifiedLevels`. The first *Examples* entry says outright that a VSA with an arbitrary agreed level is analogous to traditional code signing.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A verifier is a single trusted party. The page says a VSA does not protect against compromise of the verifier |
| Cryptography | `none` | No cryptography of its own |
| This project | `adjacent` | A real delegation of judgement, but it is expressed only as which verifier keys a consumer configures |

- **R-I-03** and **R-I-01**: a second predicate to map if we export to in-toto.
- **Not R-M-10.** The VSA's *Purpose* speaks of delegating complex policy decisions to a trusted party, but that is a consumer choosing to trust a verifier's verdict, configured as a key in its preconfigured roots of trust. Nothing in the predicate grants or re-delegates authority, so it says nothing about R-M-10's delegation flag on `AuthzCert`.
- *Fields* has a useful rule: consumers must accept only specific (signer, verifier) pairs.

## Implementations

**Searched 2026-11-04.** GitHub repository metadata checked. The `slsa-verifier` README documents a `verify-vsa` command and links the v1.1 VSA spec; conformance to v1.2 was not tested.

| Name | Kind | License | URL |
|---|---|---|---|
| slsa-verifier | open source, verifier | Apache-2.0 | https://github.com/slsa-framework/slsa-verifier |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

**Relations.** No `see_also`. The page links in-toto's Statement, ResourceDescriptor and parsing rules (`in-toto-attestation-v1`), Build Provenance's `resolvedDependencies` (`slsa-provenance-1-2`) and Verified properties (`slsa-1-2`), so all three sit under `cites`.

## Limits

- **The spec's own examples are stale.** The change history says 1.2 fixed a typo where `verificationResult` was wrongly called `slsaResult`, but both worked cases under *Examples* still use `slsaResult`. Read *How to verify* and *Schema* as authoritative.
- **`resourceUri` can be anything agreed.** *Fields* allows another value if the producer communicates it out of band.
- **The result is only as good as the verifier.** The page says so, and offers no mitigation beyond choosing verifiers carefully.
- **A cross-version link.** The second worked example sends the reader to *Verifying artifacts* at `/spec/v1.0/`, not the v1.2 page.
- **Read scope.** The whole page was read as rendered HTML. The Verifying Artifacts page is not covered.
