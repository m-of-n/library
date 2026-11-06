---
schema: "library-summary/v1"
id: rfc-9090
record: rfc-9090
type: summary
updated: "2026-11-01"
---

# Concise Binary Object Representation (CBOR) Tags for Object Identifiers

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9090.json` 2026-11-01 |
| **Authors** | C. Bormann |
| **Published** | 2021-07 |
| **Identifier** | RFC 9090 · DOI 10.17487/RFC9090 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9090.txt |
| **Digest** | `sha256:16e606aa…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | none found, search 2026-11-01 |

## Overview

RFC 9090 carries object identifiers in CBOR by tagging the value part of their BER encoding, with tag 111 for absolute OIDs, 110 for relative OIDs and 112 for OIDs under the IANA enterprise arc (§2). §2.1 closes the BER malleability that matters, leading 0x80 bytes and truncated final arcs, with validity rules and regular expressions. §2.2 then makes the 112 form preferred, which means the RFC 8949 core deterministic requirements force 112 over 111 wherever it applies. §4 lets a tag on an array or map apply to the items within, and §8 warns that an attacker may steer a byte string into such a position.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §8: alternative representations can get past a checker, and tag factoring can give data unintended semantics |
| Cryptography | `none` | No cryptography. OIDs name algorithms elsewhere |
| This project | `adjacent` | Evidence for two decided points |

- **R-M-12** (now `ARCH-0002` P1): the OID tree is a hierarchically managed global namespace (§2), which is what a key-relative model refuses. These tags sit at the interchange boundary, if anywhere.
- **DEC-002**: our reading of §2.2 is that determinism here requires tag knowledge. A generic encoder following RFC 8949 §4.2.1 cannot turn 111 into 112 unless it understands OIDs, and §4.1 leaves tag factoring to the protocol. KSA-CBOR avoids both by forbidding tags (`ADR-0004`).

## Implementations

**Searched 2026-11-01, none found.** GitHub code search for `RFC9090 cbor oid` returned nothing. A narrow query, so this is not evidence that none exists.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **A count is wrong in the source.** §5 says it introduces two new control operators, then lists three, and §7.2 registers three.
- **It does not make OIDs safe to interpret.** §8 advises treating them as opaque, and warns that integer values are unlimited in range if converted.
- **Who assigns an OID is out of scope.** §2.3 only points at lookup services.
- **Errata.** Search on 2026-11-01 found none.
- **Read scope.** Whole RFC from the cached `.txt`, except the references.
