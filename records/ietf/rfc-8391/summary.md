---
schema: "library-summary/v1"
id: rfc-8391
record: rfc-8391
type: summary
updated: "2026-11-01"
---

# XMSS: eXtended Merkle Signature Scheme

|  |  |
|---|---|
| **Type** | rfc (IRTF CFRG) |
| **Maturity** | `informational`: Category Informational, confirmed in `rfc8391.json` 2026-11-01 |
| **Authors** | A. Huelsing, D. Butin, S. Gazdag, J. Rijneveld, A. Mohaisen |
| **Published** | 2018-05 |
| **Identifier** | RFC 8391 · DOI 10.17487/RFC8391 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8391.txt |
| **Digest** | `sha256:1c9af7d6…` (full value in `record.yaml`), fetched 2026-11-01 |
| **Errata** | not checked (see Limits) |

## Overview

RFC 8391 specifies XMSS, a many-time signature built from one-time WOTS+ keys under a Merkle tree, and XMSS^MT, a multi-tree variant that avoids slow key generation (§1, §3, §4). Its security rests on properties of hash functions and not on number-theoretic hardness (§9.2), which is why it is post-quantum (§9.3). The price is state. The secret key changes with every signature, and §1.1 carries the CFRG warning that if a state is used twice no cryptographic security guarantees remain. So the signing API itself must change: §1.1 requires it to return an updated secret key state. §6 explains the deviation from the literature: the public key and index go into the message hash to stop multi-target attacks.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Forgery follows from one state reuse, a failure mode classical signatures do not have (§1.1) |
| Cryptography | `core` | A complete hash-based signature specification |
| This project | `adjacent` | NG3 defers the suite. The state model still constrains what a key can be |

- **R-M-02**: a principal identified solely by key inherits that key's limits. An XMSS key has a fixed budget set by tree height h (§5), and it ends when the budget does. A key-as-principal design needs a story for that, whichever suite is picked.

For the suite question itself, `cnsa-2-0` allows single-tree XMSS for firmware and software signing, and bars XMSS^MT. `sp-800-208` approves a subset of these parameter sets, so implementing this RFC does not imply SP 800-208 conformance, as that record already notes.

## Implementations

**Searched 2026-11-01.** Only the reference code named by §7 was confirmed; no wider survey was done.

| Name | Kind | License | URL |
|---|---|---|---|
| XMSS reference code | open source, C | CC0-1.0 | https://github.com/XMSS/xmss-reference |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. An `rfc` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **It does not solve state.** §1.1 tells developers not to use these schemes except where reuse is prevented, and leaves how to the deployer.
- **It does not say which parameters are approved.** That is `sp-800-208` and `cnsa-2-0`, and they differ from each other and from this RFC.
- **Security is by reference.** §9.1 defers the proof to [HRS16], and notes that the proof covers classical randomized hashing, not the indexed form used here. Quantum cryptanalysis of hash functions is less well understood (§9.1).
- **The CFRG note is dated.** §1.1 says there was no significant deployment experience at the time of writing.
- **Errata not checked.** The errata lookup gave no usable result.
- **Read scope.** §1, §2.5 to §2.7, §5 (text), §6, §7 and §9 were read. §3, §4, §8 and the XDR appendices were sampled for MUST statements and not read line by line.
