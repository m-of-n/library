---
schema: "library-summary/v1"
id: rfc-8769
record: rfc-8769
type: summary
updated: "2026-11-01"
---

# Cryptographic Message Syntax (CMS) Content Types for Concise Binary Object Representation (CBOR)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `informational`: Category Informational, confirmed in `rfc8769.json` 2026-11-01 |
| **Authors** | J. Schaad |
| **Published** | 2020-03 |
| **Identifier** | RFC 8769 · DOI 10.17487/RFC8769 · individual submission, not a WG product |
| **Source** | https://www.rfc-editor.org/rfc/rfc8769.txt |
| **Digest** | `sha256:ab2c0a62…` (full value in `record.yaml`), verified 2026-11-01 |
| **Errata** | none: errata search returned no matching errata, 2026-11-01 |

## Overview

RFC 8769 is a labelling document. It gives CMS two content type OIDs, `id-ct-cbor` for one CBOR item (§2) and `id-ct-cborSequence` for a CBOR Sequence (§3), so that CBOR inside CMS need not be called `id-data`. Both say nothing about what the CBOR means: *"Nothing is stated about the specific CBOR object that is included."* §6 claims no new security issues, and the only stated benefit is reduced confusion.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | §6 introduces nothing new |
| Cryptography | `none` | It only assigns OIDs |
| This project | `none` | Bears on nothing |

Bears on no `DEC-*` or `R-*`. The usefulness verdict is the point of this record: it closes the question. R-M-01 excludes X.509 and PKIX as native encoding, which is a different thing from CMS, and no requirement names CMS.

## Implementations

**Searched 2026-11-01** (web and GitHub code search for `id-ct-cbor` and its OID). No library was found that does more than carry the OID in a table or module. `pyasn1-modules` ships the §4 ASN.1 module. Generic OID tables also list it, and those were not catalogued.

| Name | Kind | License | URL |
|---|---|---|---|
| pyasn1-modules, rfc8769.py | open source, Python, ASN.1 module only | BSD-2-Clause | https://github.com/etingof/pyasn1-modules |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **It does not bind a CBOR profile.** A content type does not require deterministic encoding or any schema (§2, §3).
- **It cites RFC 7049 and RFC 8152**, since replaced by `rfc-8949`, and by `rfc-9052` with `rfc-9053`. The RFC has not been updated.
- **It carries no usage evidence.** §1 asserts that CBOR is going to be transported using CMS and gives no example, and the search above found none.
- **Read scope.** The whole document, RFC Editor `.txt`.
