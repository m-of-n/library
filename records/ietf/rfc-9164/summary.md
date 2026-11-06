---
schema: "library-summary/v1"
id: rfc-9164
record: rfc-9164
type: summary
updated: "2026-11-01"
---

# Concise Binary Object Representation (CBOR) Tags for IPv4 and IPv6 Addresses and Prefixes

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9164.json` 2026-11-01 |
| **Authors** | M. Richardson, C. Bormann |
| **Published** | 2021-12 |
| **Identifier** | RFC 9164 · DOI 10.17487/RFC9164 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9164.txt |
| **Digest** | `sha256:bc18d7ca…` (full value in `record.yaml`), verified on fetch 2026-11-01 |
| **Errata** | none found, search 2026-11-01 |

## Overview

RFC 9164 defines tags 54 and 52 for IPv6 and IPv4, replacing tags 260 and 261, which distinguished families only by length or were under-documented (§1). A tag covers an address, a prefix or an interface form, told apart by array order (§3). A prefix drops trailing zero bytes, and §4.2 and §4.3 make this canonical: encoders zero unused bits and strip trailing zeros, and decoders must check both. §6 gives the reason: otherwise unused bits are a covert channel.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §4.3 and §6: unchecked prefix bits carry covert data. Validity must be checked before conversion to a platform type |
| Cryptography | `none` | No cryptography |
| This project | `adjacent` | Marginal. The pattern is relevant, the tags are not |

- **DEC-002**: a small instance of the principle in `ADR-0004` item 2, that canonicality is enforced by rejecting. §4.1 argues that its tag validity rules plus RFC 8949 §4.2.1 are enough for determinism here. §4 leaves open whether a generic library or the application does the check.
- **R-M-12** (now `ARCH-0002` P1): §1 is a registry story, with two tags replaced by two more because the first pair were underspecified.

## Implementations

**Searched 2026-11-01, none found.** GitHub code search for `RFC9164 cbor` returned nothing. A narrow query, so this is not evidence that none exists.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no open issue owns that. No keyword count is given because none has been reconciled.

## Limits

- **The sample decoder is weaker than the text.** §4.2 calls `54([44, h'20010db8123012'])` invalid. Following §4.3.1 as written, our trace copies only the covered bytes and checks only the last one, so it accepts that value. §4.3's prose does reject it. Implement the prose.
- **An example does not match the CDDL.** §3.2 writes the zone as `'eth0'`, a byte string in diagnostic notation, while Figure 1 allows only `uint / text`.
- **Scope.** No MAC addresses (§1). Zone identifiers are local to a node (§3.1.3), so they mean nothing to a remote verifier.
- **Errata.** Search on 2026-11-01 found none, so neither point above is a known erratum. Both are ours, and a reviewer should check them against the source.
- **Read scope.** Whole RFC from the cached `.txt`, from the table of contents through §7's opening. §7's detail and the references were not read.
