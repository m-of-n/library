---
schema: "library-summary/v1"
id: did-key-method
record: did-key-method
type: summary
updated: "2026-11-01"
---

# The did:key Method v0.9

|  |  |
|---|---|
| **Type** | spec (W3C CCG draft) |
| **Maturity** | `unofficial`: CG-DRAFT, not on the W3C standards track |
| **Authors** | W3C Credentials Community Group |
| **Published** | 2026 |
| **Identifier** | did:key v0.9 |
| **Source** | https://w3c-ccg.github.io/did-key-spec/ |
| **Digest** | `sha256:e014a146…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

`did:key` turns a public key into a DID with no registry: multibase over a multicodec key type and the raw key bytes, expanded deterministically into a DID document. The method is "purely generative", and its values "cannot be updated or deactivated". The spec positions it for short-lived and offline uses, and says use for long-lived cases "is only recommended when accompanied with high confidence in hardware isolation". It is the clean self-authenticating case, and it pays Zooko's price and a rotation price as well.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | identifier binding, with key compromise unaddressed by design |
| Cryptography | `adjacent` | encoding of keys |
| This project | `core` | an option under DEC-003 |

- **DEC-003** (issuer and subject identifiers on the wire): the listed option. Note that the spec defines the bytes, but canonical key bytes per key type are what DEC-003 must pin.
- **R-M-02**: a principal identified solely by key, with no way to rotate it.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** introduction, syntax, and Create, then the security sections and per-key-type parts by keyword only, from the ReSpec source of the editor's draft. The rendered page was not read.

- The version label says 0.9, but it is a moving Community Group draft with no W3C endorsement.
- The multicodec and multibase registries it relies on are global allocations, so it is not free of central registries in the R-M-12 sense.
- It leaves key rotation to the application layer.
