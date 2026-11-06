---
schema: "library-summary/v1"
id: rfc-4880
record: rfc-4880
type: summary
updated: "2026-11-04"
---

# OpenPGP Message Format

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, obsoleted by RFC 9580 |
| **Authors** | J. Callas, L. Donnerhacke, H. Finney, D. Shaw, R. Thayer |
| **Published** | 2007-11 |
| **Identifier** | RFC 4880 · DOI 10.17487/RFC4880 |
| **Source** | https://www.rfc-editor.org/rfc/rfc4880.txt |
| **Digest** | `sha256:575dc55f…` (full value in `record.yaml`), fetched 2026-11-01, unchanged 2026-11-04 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

RFC 4880 is the 2007 OpenPGP message format, since replaced by RFC 9580. For naming it holds two things. Trust Signature subpackets (§5.2.3.13) let a signer extend trust to a key with a level, so that level 1 makes a trusted introducer and level 2 a "meta introducer", and Regular Expression subpackets (§5.2.3.14), used with trust signatures of level above 0, limit that trust to User IDs that match. That is delegated, scoped introduction inside the format. §12.2 derives a V4 fingerprint as SHA-1 over the octet 0x99, a two-octet length and the Public-Key packet, and the Key ID as its low-order 64 bits, so identifiers are derived from the key itself but weak by today's standards; that judgement is ours.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | a scoped-trust mechanism, not a security analysis |
| Cryptography | `core` | a complete signature and key format |
| This project | `adjacent` | an import source |

- **R-I-04** (import OpenPGP identity signatures as `NameCert` and/or `Endorse`, never as `AuthzCert` unless an explicit profile says so): the subpackets above are what such an import has to carry or drop.
- **DEC-003** (accepted in ADR-0005: `kid` is SHA-256 of the suite's public-key encoding): a V4 fingerprint is a precedent for hash-of-key identifiers, and for what a hash choice costs later.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Relations

No `see_also` edges. `rfc-9580` carries `supersedes: rfc-4880`, and `gnupg-key-management` lists this RFC under its `cites`; neither is repeated here. No reference of this RFC (RFC 1991, RFC 2440 and others) is held by the library, so there is no `cites`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** §1, §5.2.3.13, §5.2.3.14, §12.2 by section, and the reference list. The rest was not read. Re-checked against the text 2026-11-04. Use `rfc-9580` for current rules: this record's value is what older keys contain.

- §5.2.3.14 defines the regular expression's effect on one signature. How scopes combine across a chain is not stated there; the `delegation-models` topic records R-0007's finding on this.
- Errata exist per RFC metadata and were not read.
- `superseded_by` is left empty because `rfc-9580` carries the edge.
