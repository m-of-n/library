---
schema: "library-summary/v1"
id: rfc-9528
record: rfc-9528
type: summary
updated: "2026-11-01"
---

# Ephemeral Diffie-Hellman Over COSE (EDHOC)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Proposed Standard, confirmed in `rfc9528.json` 2026-11-01 |
| **Authors** | G. Selander, J. Preuß Mattsson, F. Palombini |
| **Published** | 2024-03 |
| **Identifier** | RFC 9528 · DOI 10.17487/RFC9528 · LAKE WG |
| **Source** | https://www.rfc-editor.org/rfc/rfc9528.txt |
| **Digest** | `sha256:16b0959e…` (full value in `record.yaml`), verified 2026-11-01 |
| **Errata** | 2 reported, none verified: 8258 (Appendix C.2 CDDL), 8272 (§5.4.2 storage). Read 2026-11-01 |

## Overview

EDHOC is an authenticated ephemeral Diffie-Hellman exchange built to be small: 101 bytes in total in its smallest example (§1.2, Table 1). Its argument is reuse. A device that already has CBOR, COSE and CoAP for OSCORE gets a key exchange for little additional code. The design is SIGMA-I in MAC-then-Sign form for signature authentication, plus static Diffie-Hellman methods (§2, §3.2), with forward secrecy, mutual authentication and identity protection (§9.1). It leaves trust to the application: authentication beyond proof of possession is out of scope (§3.5).

Two things make it worth reading here. §1.4 says all CBOR in the document means deterministically encoded CBOR, yet §9.8 grades enforcement below rejection: a CDDL failure aborts (MUST), while non-deterministic input only MAY abort, with abort RECOMMENDED. And §3.8 builds must-understand into the wire form: the sign of an EAD label says whether the item is critical.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A full AKE with a stated property set (§9.1) |
| Cryptography | `core` | New protocol over COSE primitives, formally analysed in earlier versions (§9.1) |
| This project | `adjacent` | We do no key agreement. The encoding and credential choices are the evidence |

- **DEC-002** (accepted, `ADR-0004`): the closest shipped comparison for a rejecting decoder. `ADR-0004` item 2 and `ARCH-0002` P5.1 reject all non-canonical input. EDHOC, on the same RFC 8949 §4.2.1 base, stops at RECOMMENDED (§9.8). §3.5.2 says credentials SHOULD be used as is, without re-encoding, which is the same instinct as `SPEC-0002` §5. Our reading: the softer rule is tolerable in EDHOC because a session protocol has no long-lived signed objects, so it is no precedent against rejection.
- **Determinism has a stated hole.** §3.5.3 lets labels in an ID_CRED map go unsorted, and context_2 is computed over ID_CRED_R (§5.3.2). That is a carve-out inside a document whose §1.4 claims determinism throughout.
- **R-M-02**: Appendix D.2 and D.3 describe the case with no PKI, where identity is directly associated with the authentication key and the trust anchor is the peer's key. §3.5.2 dresses a naked COSE_Key as a CCS. That is key-as-principal in a deployed protocol, for a pairwise session.

Not on DEC-005, though §3.8 is relevant to the `crit` analysis `ARCH-0002` P5.2 still owes. Sign-of-label criticality is a design note for that work. EDHOC uses COSE internally and offers no envelope choice.

## Implementations

**Searched 2026-11-01** (web and GitHub), with each README or source file checked. All four names RFC 9528 or uses a library that does. None was run, and cipher suite and method coverage were not compared. Older repositories built against drafts (`py-edhoc`, `EDHOC-C`) are left out.

| Name | Kind | License | URL |
|---|---|---|---|
| lakers | open source, Rust, bindings for C and Python | BSD-3-Clause | https://github.com/lake-rs/lakers |
| uOSCORE / uEDHOC | open source, C | Apache-2.0 and MIT license files present | https://github.com/eriptic/uoscore-uedhoc |
| libedhoc | open source, C | MIT | https://github.com/kamil-kielbasa/libedhoc |
| aiocoap | open source, Python, CoAP stack using lakers | MIT in edhoc.py SPDX header; LICENSES directory not read | https://github.com/chrysn/aiocoap |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **It does not authenticate anyone by itself.** Credential validation, identity policy and trust anchors are the application's (§3.5, Appendix D).
- **It carries no version field.** Breaking changes arrive as new methods (§3.2).
- **Post-quantum is partial.** Method 0 can take a KEM, and static DH methods would need new methods (§9.4).
- **The security analyses are of earlier versions** (§9.1), and were not read.
- **Errata.** 8258 says the Appendix C.2 CDDL has defects, including an undefined `map` type. 8272 asks that C_I and C_R join §5.4.2's storage rule. Both are Reported, not verified, so the published text stands and the CDDL should not be lifted without checking.
- **Read scope.** §1 to §4, §5.1 to the opening of §5.4.2, the opening of §6 and §6.1, §8, §9.1 to §9.4, §9.8, §10.5, Appendix C, D and E, from the `.txt` with page furniture stripped. Not read: the rest of §5 and §6, §7, §9.5 to §9.7, the rest of §10, Appendix A, B, F, G, H, and Appendix I beyond its opening. References read only for the entries cited in `record.yaml`.
