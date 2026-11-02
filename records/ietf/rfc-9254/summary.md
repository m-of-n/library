---
schema: "library-summary/v1"
id: rfc-9254
record: rfc-9254
type: summary
updated: "2026-11-01"
---

# Encoding of Data Modeled with YANG in the Concise Binary Object Representation (CBOR)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9254.json` 2026-11-01 |
| **Authors** | M. Veillette (Ed.), I. Petrov (Ed.), A. Pelov, C. Bormann, M. Richardson |
| **Published** | 2022-07 |
| **Identifier** | RFC 9254 · DOI 10.17487/RFC9254 · CoRE WG |
| **Source** | https://www.rfc-editor.org/rfc/rfc9254.txt |
| **Digest** | `sha256:ff6cab52…` (full value in `record.yaml`), verified 2026-11-01 |
| **Errata** | none: errata search returned no matching errata, 2026-11-01 |

## Overview

RFC 9254 maps YANG data trees to CBOR, and its argument is a trade between size and coordination. A node can be keyed by a text name, or by a YANG SID, a 63-bit integer delta-encoded against the enclosing map's reference SID (§3.2). Names avoid *"the management overhead associated with SID allocation"* at a significant cost in size (§3.3). SIDs are compact, but only if someone has assigned them, and §3.2 puts assignment and uniqueness outside the specification. §8 draws the consequence: reading SID-keyed data depends on having the right mapping as well as the right modules, and that mapping needs the same care as the modules.

As a CBOR profile it faces the other way from ours. §3 requires decoders to support indefinite lengths unless a protocol says otherwise, and the examples show map keys unsorted (§4.2.1, §4.4.1). The document never mentions deterministic encoding. Its one strictness rule, in §8, is that receivers SHOULD reject non-compliant messages.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `none` | §8 adds little beyond its dependencies: a SHOULD reject and the mapping warning |
| Cryptography | `none` | No cryptography |
| This project | `adjacent` | Prior art for R-M-12, and a contrast with `ADR-0004` |

- **R-M-12** (relocated to `ARCH-0002` P1 by `ADR-0001`): a worked example of the design P1 rejects, and of its real benefit. Integer identifiers from a managed global space give the compactness, and a stateless decoder still cannot read them without the mapping (§8). P1's `(key, local label)` pair pays with key material in size and needs no such coordination. This RFC gives no measurement that would price that trade for us.

Kept off **DEC-002** deliberately: `ADR-0004` is decided and this RFC offers no input to it. The tag use (§9.3, tags 43 to 47) is what a registry-native profile looks like, and KSA-CBOR forbids it.

## Implementations

**Searched 2026-11-01** (web and GitHub). The projects below describe themselves as CORECONF, which uses this mapping. `pycoreconf`'s README was read. The other two are listed from their repository metadata. None was tested against the RFC.

| Name | Kind | License | URL |
|---|---|---|---|
| pycoreconf | open source, Python, CORECONF | GPL-3.0 | https://github.com/alex-fddz/pycoreconf |
| ccoreconf | open source, C, CORECONF | not stated by GitHub | https://github.com/manojgudi/ccoreconf |
| rustconf | open source, Rust, CORECONF | Apache-2.0 | https://github.com/samsirohi11/rustconf |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **It does not say how SIDs are assigned.** That is RFC 9595, which the library does not hold (a gap), and `rfc-9997` for one range.
- **It is an encoding, not a protocol.** CORECONF is referenced as [CORE-COMI], a draft at the time.
- **The reference SID of an outermost map can come from the environment** (§3.2), so a value is not always self-describing. §3 only says payloads SHOULD identify nodes statelessly.
- **Read scope.** §1 to §9 in full, from the `.txt` with page furniture stripped. References read only for the entries cited in `record.yaml`.
