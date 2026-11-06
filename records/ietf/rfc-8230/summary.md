---
schema: "library-summary/v1"
id: rfc-8230
record: rfc-8230
type: summary
updated: "2026-11-01"
---

# Using RSA Algorithms with CBOR Object Signing and Encryption (COSE) Messages

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc8230.json` 2026-11-01 |
| **Authors** | M. Jones |
| **Published** | 2017-09 |
| **Identifier** | RFC 8230 · DOI 10.17487/RFC8230 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8230.txt |
| **Digest** | `sha256:d59c3f07…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | none found, search 2026-11-01 |

## Overview

RFC 8230 registers RSASSA-PSS (PS256, PS384, PS512), RSAES-OAEP and the RSA key type for COSE (§2 to §4). Parameters are narrowed so that each identifier fixes the hash, MGF1 and salt length (§2) or the hash and empty encoding parameters (§3). §4 encodes numeric key parameters as big-endian byte strings of minimum length and allows multi-prime keys. §6.1 sets a 2048-bit floor and treats oversized keys as a denial-of-service risk, proposing a trust decision before any cryptography or a maximum length.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §6.1 on key-size denial of service. §6.2 on hash substitution |
| Cryptography | `core` | A complete RSA binding for COSE, though with no test vectors |
| This project | `adjacent` | Bears only on a closed input to DEC-003. Otherwise none |

- **DEC-003**: `ARCH-0001` §7 names §4 in its finding that RFC 9679 thumbprints need one pinned representation per key type. `ADR-0005` then chose `kid` as SHA-256 of the suite's encoding, so this is evidence for a closed decision. See `rfc-9679`, which authors the edge to this record.
- NG3 defers the algorithm suite. This RFC bears on no other `DEC-*` or `R-*` yet.

## Implementations

**Not searched for this record.** RSA is outside every suite `SPEC-0002` defines, so there is nothing we would build on yet.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **It cites obsoleted documents.** RFC 8152 and RFC 7049, and the IANA entries now also reference RFC 9053.
- **SHA-1 survives.** -40 is RSAES-OAEP with SHA-1 (§3, §6.3), and the IANA CSV still showed it as Recommended Yes on 2026-11-01.
- **RS256 is not here.** Only PSS and OAEP are defined. RFC 9864 §6.1 records disagreement on whether these key-size-flexible identifiers count as fully specified.
- **Errata.** Search on 2026-11-01 found none.
- **Read scope.** Whole RFC from the cached `.txt`, skimming the IANA list items against the §2 to §4 tables.
