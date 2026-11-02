---
schema: "library-summary/v1"
id: rfc-4880
record: rfc-4880
type: summary
updated: "2026-11-01"
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
| **Digest** | `sha256:575dc55f…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | RFC metadata carries an errata link; not read |

## Overview

RFC 4880 is the 2007 OpenPGP message format, since replaced by RFC 9580. For naming it holds two things. Trust Signature subpackets (§5.2.3.13) let a signer extend trust to a key with a depth, so that level 2 makes a meta introducer, and Regular Expression subpackets (§5.2.3.14) limit that trust to User IDs that match. That is delegated, scoped introduction inside the format. §12.2 derives a V4 fingerprint as SHA-1 over the key packet and the Key ID as its low 64 bits, so identifiers are self-certifying but weak by today's standards.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | a scoped-trust mechanism, not a security analysis |
| Cryptography | `core` | a complete signature and key format |
| This project | `adjacent` | an import source |

- **R-I-04** (import OpenPGP identity signatures as `NameCert` and/or `Endorse`): the subpackets above are what such an import has to carry or drop.
- **DEC-003**: a V4 fingerprint is a precedent for hash-of-key identifiers, and for what a hash choice costs later.

## Implementations

Not searched: this batch is the summary bar and ran no implementation survey.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

`distilled/` and a `distillation` block are absent on purpose: this is the summary bar. No open issue owns FX-1 extraction of this record yet; that would be triggered by a decision that builds on it.

## Limits

**Read:** §1, §5.2.3.13, §5.2.3.14, §12.2 by section. The rest was not read. Use `rfc-9580` for current rules: this record's value is what older keys contain.

- §5.2.3.14 defines the regular expression's effect on one signature. How scopes combine across a chain is not stated there; `delegation-models` records R-0007's finding on this.
- Errata exist per RFC metadata and were not read.
- `superseded_by` is left empty because `rfc-9580` carries the edge.
