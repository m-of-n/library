---
schema: "library-summary/v1"
id: tuf-tap-21
record: tuf-tap-21
type: summary
updated: "2026-11-01"
---

# TAP 21: ML-DSA signing scheme for TUF metadata

|  |  |
|---|---|
| **Type** | spec (TUF Augmentation Proposal, Type Standardization) |
| **Maturity** | unset: status is `Accepted`, which has no enum equivalent |
| **Authors** | Fredrik Skogman |
| **Published** | Created 2026-04-29, last modified 2026-09-30, accepted by commit of 2026-10-06 |
| **Identifier** | TAP 21, Version 1 · `tap21.md` @ `21efd976` |
| **Source** | https://raw.githubusercontent.com/theupdateframework/taps/21efd9762c6bae5c6f61199d1fce7756c9dd18d2/tap21.md |
| **Digest** | `sha256:0e62f9af…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

TAP 21 adds an `ml-dsa` keytype to TUF, and solves one problem: pure ML-DSA needs the whole message at the signing device, and TUF metadata can be large while keys sit in HSMs. So the metadata is never signed directly. The client hashes the canonical metadata and signs `0x74 || 0x75 || 0x66 || version || H(MSG)` (the bytes for `tuf`) with pure ML-DSA and an empty context. The one-byte version fixes the hash and canonicalization together, and v1 is SHA-512 over TUF canonical JSON. Schemes are `ml-dsa-44/1`, `ml-dsa-65/1` and `ml-dsa-87/1`, all three MUST be supported, and §*Verification steps* forbids inference from signature bytes, fallback or multiple interpretations. HashML-DSA is rejected on ecosystem grounds, and external mu because not every provider exposes it (*Rationale*).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Domain separation, version pinning and a no-fallback rule, stated as a verifier procedure |
| Cryptography | `core` | A concrete application-level pre-hash over FIPS 204 |
| This project | `core` | A real answer to how a signed-metadata format moves to PQ, in the design space we are choosing in |

- **R-O-05**: a direct contrast. R-O-05 requires signing the canonical encoding verbatim and forbids canonicalizing during verification. TAP 21 signs a digest of canonical JSON, and step 1 of its verification computes the canonical form. Reasoning from HSM limits, the TAP argues against signing whole messages. Our rule would have to answer this at PQ sizes, and it has not been tested against the case. The authenticated type indicator has a counterpart in the domain and version bytes.
- **R-O-03**: the canonicalization is cited and bound to the version byte, which is a clean instance of "cited, not invented silently".
- **R-M-02**: the *Appendix* gives measured growth: 1.0x ECDSA to 33.6x, 46.0x and 64.3x for signatures alone. On a sigstore example with whole files, root grows 7.0x to 12.8x. Identification by raw key would add 1890 to 3652 bytes each as TUF encodes them.

## Implementations

**Searched 2026-11-01.** The TAP's own list, checked against GitHub.

| Name | Kind | License | URL |
|---|---|---|---|
| go-tuf (PR #780, merged) | open source, Go | Apache-2.0 | https://github.com/theupdateframework/go-tuf |
| securesystemslib 1.5.0 | open source, Python | MIT | https://github.com/secure-systems-lab/securesystemslib |
| tuf-conformance | open source, tests | not checked | https://github.com/theupdateframework/tuf-conformance |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **Single-algorithm only.** There is no hybrid or composite here, and no transition guidance beyond backwards compatibility for repositories that do not use `ml-dsa`. How a repository rotates from ECDSA to ML-DSA is not discussed.
- **v1 has no margin at ML-DSA-87.** *Security Analysis* says SHA-512 has zero margin, but is valid. The FIPS 204 §5.4 passage the Appendix quotes is the basis.
- **The "no pre-hash" argument is an opinion.** *Rationale* cites a blog post and an expectation about ecosystem support. It does not claim a security break in HashML-DSA.
- **CNSA is not mentioned.** `cnsa-2-0` does not approve HashML-DSA either, but whether this application-level construction satisfies NSS rules is not addressed. Its SHA-512 is permitted there, and its ML-DSA-44 and ML-DSA-65 sets are not.
- **Read scope.** The whole TAP was read. The implementations were confirmed to exist, not tested.
