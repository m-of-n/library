---
schema: "library-summary/v1"
id: w3c-did-core
record: w3c-did-core
type: summary
updated: "2026-11-01"
---

# Decentralized Identifiers (DIDs) v1.0

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `recommendation`: W3C Recommendation 19 July 2022, as the document states |
| **Authors** | Manu Sporny, Dave Longley, Markus Sabadello, Drummond Reed, Orie Steele, Christopher Allen (editors: Manu Sporny, Amy Guy, Markus Sabadello, Drummond Reed) |
| **Published** | 2022-07-19 |
| **Identifier** | REC-did-core-20220719 |
| **Source** | https://www.w3.org/TR/2022/REC-did-core-20220719/ |
| **Digest** | `sha256:5e443457…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

DID Core defines an identifier that resolves to a document of verification methods and services, designed so that a controller can prove control without permission from any other party (Abstract, §9.16). The core specifies the syntax, data model and representations. Everything that makes a DID work, such as how it is created, resolved, updated and deactivated, is delegated to separate DID method specifications (§8). Purposes of a key are explicit verification relationships, such as `authentication` and `assertionMethod`, and a verifier must check the method used is in the right one (§5.3). The price is plain in §9.10: uniqueness without central authority costs memorability, which §9.10 sets out as Zooko's Triangle.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | §9 covers control, rotation, recovery and non-repudiation, mostly as advice that methods must fill in |
| Cryptography | `adjacent` | Defines verification relationships, not algorithms (§5.3) |
| This project | `adjacent` | DEC-003, closed: `did:key` was rejected. R-M-12: a contrast, since extension names go to a registry |

- **DEC-003** (accepted 2026-10-25, ADR-0005): `did:key` was rejected because its key type is named by a multicodec code from an outside registry. Note that the objection is to that method, not to DID Core, and `did:key` is not defined here.
- **R-M-12** (proposed): §4.1 routes extensions to the DID Specification Registries. That is registry-mediated extension, which R-M-12's native model excludes. It is a contrast and a mapping concern at the boundary, not a model to copy.
- **R-M-02 is not listed.** A DID is an indirection that resolves to keys, so it is not a principal identified solely by key.

It is held in this topic because `draft-ietf-vcon-vcon-core-04` §4.2.6 lets a party carry a `did`, so the same party can be named by DID, tel and mailto. Of these only a DID is designed for proof of control, and in §4.2.6 as read here that draft does not require anyone to perform that proof.

## Implementations

**Searched 2026-11-01.** Only these two projects were checked, for existence and stated scope. This was not a survey.

| Name | Kind | License | URL |
|---|---|---|---|
| Universal Resolver | open source, resolver | Apache-2.0 | https://github.com/decentralized-identity/universal-resolver |
| DID Test Suite | open source, conformance | see repo: GitHub reports no SPDX id | https://github.com/w3c/did-test-suite |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **Most security lives in the methods.** §8.3 and §8.4 require methods to address security and privacy, and §9 is largely advice. Claims about a DID's strength need the specific method, and none is assessed here.
- **Non-repudiation is conditional** (§9.4), on a registry with verifiable timestamps and a subject that monitors for changes.
- **Persistence is an ideal.** §9.16 speaks of an ideal case. It depends on the method's registry.
- **Version.** DID v1.1 (`w3c-did-1-1`, a stub) was a Candidate Recommendation Snapshot when checked, so it does not yet replace this document and no `superseded_by` is set.
- **The registry text cited.** §4.1 mentions were found by search, and the DID Specification Registries document itself was not read.
- **Read scope.** The status block, §1 outline, the openings of §5.3, §5.3.2, §8.1, §9.2, §9.4, §9.10, §9.15 and §9.16, and registry mentions found by search, from the HTML of the dated REC with code blocks stripped. §3, §4, §6, §7 and §10 were not read in full. This is the thinnest read in the batch for its size.
