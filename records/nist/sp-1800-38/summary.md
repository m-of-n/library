---
schema: "library-summary/v1"
id: sp-1800-38
record: sp-1800-38
type: summary
updated: "2026-11-01"
---

# SP 1800-38: Migration to Post-Quantum Cryptography

|  |  |
|---|---|
| **Type** | spec (NIST SP 1800-series practice guide, three volumes) |
| **Maturity** | `draft`: all volumes are marked PRELIMINARY DRAFT |
| **Authors** | W. Newhouse, M. Souppaya (NIST), W. Barker, C. Brown and consortium authors; full list in `record.yaml` |
| **Published** | Volume A April 2023; Volumes B and C December 2023 |
| **Identifier** | NIST SP 1800-38A, -38B, -38C |
| **Source** | https://csrc.nist.gov/pubs/sp/1800/38/iprd-(1) |
| **Digest** | `sha256:53474286…` for Volume C. A and B in `content.note`. Fetched 2026-11-01 |

## Overview

An NCCoE consortium project with two workstreams. Volume B demonstrates cryptographic discovery: a test plan, use case and architecture for tools that build the inventory a migration needs. Volume A notes that organizations are often unaware of how far their dependence on public-key cryptography reaches. Volume C tests interoperability and performance of pre-standard Kyber and Dilithium in SSH, TLS, QUIC, X.509 and HSMs. Its findings are operational: draft churn and codepoints break interop (C §6.4), and negotiation can land on plain classical key exchange (C §6.4). In its TLS tests, handshake impact was small (C §6.3). It also has a useful taxonomy of X.509 hybrid formats: concatenated, bound, composite, Catalyst, Chameleon (C §8.1.2).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Migration practice, not a security analysis |
| Cryptography | `adjacent` | Measures algorithms, specifies none |
| This project | `none` | About enterprise inventory and network protocols. We are not an enterprise migration |

It bears on no open `DEC-*` or `R-*`. Two lessons are worth carrying into any later identifier work: OIDs that reference a specification version are critical while specifications change (C §8.4), and ASN.1 encodings of keys differed between specifications (C §8.4). R-I-05 would need to account for the hybrid formats of C §8.1.2 if X.509 import ever meets one, but this record claims no bearing today.

## Implementations

Not searched. Volume C names consortium stacks (OQS-OpenSSL, s2n-tls, Samsung SDS PQC-TLS) tested in 2023 against pre-standard algorithms, and they should not be assumed current.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. As a preliminary draft of a practice guide it is a poor extraction target, and no issue owns that work. Extract only if a final appears.

## Limits

- **Pre-standard.** All results use Kyber and Dilithium drafts, not FIPS 203 or 204. Numbers do not carry over.
- **Preliminary and incomplete.** Volume B says outright that there are gaps and that the document is incomplete. This record may lag: we read only what the CSRC pages list.
- **No signed-artifact coverage.** Nothing here tests attestation or code signing formats.
- **The title-page URL did not work for us.** The NCCoE page returned 403, so project updates there are unseen.
- **Read scope.** Volume A in full. Volume B §1 only. Volume C §1, §2, the §6.4 and §8.4 lessons and §8.1.2's composite format. The rest of B, the SSH, QUIC and HSM sections, and the C §6.3 tables were sampled, not read.
