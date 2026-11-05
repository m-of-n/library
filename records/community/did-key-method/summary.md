---
schema: "library-summary/v1"
id: did-key-method
record: did-key-method
type: summary
updated: "2026-11-04"
---

# The did:key Method v0.9

|  |  |
|---|---|
| **Type** | spec (W3C CCG draft) |
| **Maturity** | `unofficial`: the ReSpec config sets `specStatus: "CG-DRAFT"`, not the W3C standards track |
| **Authors** | Dave Longley, Dmitri Zagidulin, Manu Sporny (editors "TBD"), W3C Credentials Community Group |
| **Published** | 2026 |
| **Identifier** | did:key v0.9 |
| **Source** | https://w3c-ccg.github.io/did-key-spec/ |
| **Digest** | `sha256:e014a146…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |

## Overview

`did:key` turns a public key into a DID with no registry: multibase over a multicodec key-type code and the raw key bytes (Identifier Syntax), expanded deterministically into a DID document (Create). The Operations section calls the method "purely generative", and says its values "cannot be updated or deactivated". The introduction positions it for short-lived and offline uses, and says use for long-lived cases "is only recommended when accompanied with high confidence in hardware isolation". It is the clean self-authenticating case, and by our reading it pays Zooko's price and a rotation price as well.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | identifier binding, with key compromise unaddressed by design |
| Cryptography | `adjacent` | encoding of keys |
| This project | `adjacent` | an option DEC-003 weighed and rejected |

- **DEC-003** (issuer and subject identifiers on the wire): `did:key` was one of the listed options. DEC-003 was accepted on 2026-10-25 by ADR-0005 (`kid` = SHA-256 of the suite's public-key encoding), which rejects `did:key` because its key type is a multicodec code from a registry maintained outside the project, a registry in the identifier.
- **R-M-02** (a principal MAY be identified solely by key or key digest): a principal identified solely by key, with no way to rotate it.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

- `see_also` `w3c-did-1-1`: the DID data model this method's identifiers and documents conform to (Identifier Syntax cites the DID specification). Which DID version the ReSpec `[[DID]]` reference resolves to was not checked, so this is not a `cites` entry.
- `see_also` `w3c-did-extensions-methods`: the W3C registry of DID methods, which lists `key` with this specification as its link (checked in the 2026-10-01 Note, 2026-11-04).
- `see_also` `zooko-2001-names`: `did:key` is a decentralised, secure name that is not human-meaningful: it picks two of the three properties the essay says a name cannot all have.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** introduction, Identifier Syntax, Operations and Create, then the Privacy and Security Considerations sections and per-key-type parts by keyword only, from the ReSpec source of the editor's draft. The rendered page was not read. Quotes re-checked against the source 2026-11-04.

- The version label says 0.9, but it is a moving Community Group draft with no W3C endorsement.
- The multicodec and multibase registries it relies on are global allocations, so it is not free of registries in the sense of ARCH-0002 P1 (R-M-12, accepted by ADR-0001). ADR-0005 rejects it on that ground.
- It leaves key rotation to the application layer.
