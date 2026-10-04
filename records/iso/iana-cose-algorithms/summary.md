---
schema: "library-summary/v1"
id: iana-cose-algorithms
record: iana-cose-algorithms
type: summary
updated: "2026-10-03"
---

# IANA COSE Algorithms registry

|  |  |
|---|---|
| **Type** | dataset — a living registry |
| **Maturity** | _unset_ — a living allocation table has no RFC 2026 standing |
| **Publisher** | IANA |
| **Snapshot** | **2026-10-03** (96 entries) |
| **Identifier** | https://www.iana.org/assignments/cose/cose.xhtml |
| **Source** | https://www.iana.org/assignments/cose/algorithms.csv |
| **Digest** | `sha256:4dc4c64f84e6020a05403862219b66b0bfd9cc853245d87b82ed00f6d77600f3` |

## Overview

The authoritative list of **COSE `alg` values**. Each RFC registers a slice —
`rfc-9053` the initial set, `rfc-9964` the ML-DSA set, `rfc-9864` the
fully-specified ECDSA and EdDSA algorithms — but only the registry says what is
actually assigned at a given moment.

The snapshot taken 2026-10-03 holds **96 entries**:

| Recommended | Count |
|---|---|
| Yes | 59 |
| No | 16 |
| **Deprecated** | **11** |
| Filter Only | 2 |
| (blank / Unassigned / Reserved) | 8 |

The post-quantum neighbourhood as of this snapshot:

| Value | Name | Reference | Recommended |
|---|---|---|---|
| -48 | ML-DSA-44 | RFC 9964 | Yes |
| -49 | ML-DSA-65 | RFC 9964 | Yes |
| -50 | ML-DSA-87 | RFC 9964 | Yes |
| -51 | **ESP384** | RFC 9864 §2.1 | Yes |
| -52 | **ESP512** | RFC 9864 §2.1 | Yes |
| -53 | Ed448 | RFC 9864 §2.2 | Yes |

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | What a verifier may legitimately encounter in an `alg` header |
| Cryptography | `adjacent` | An allocation table, not a specification |
| This project | `adjacent` | Bears on R-M-12; the suite itself is deferred by NG3 |

Bears on **R-M-12**. This is the governed namespace an exported COSE statement
would draw its algorithm identifier from — relevant to D-3's "COSE as export
only" option, because what we export has to be a value in this table.

## Implementations

Not applicable — a registry, not software. Searched for tooling that consumes
it programmatically on **2026-10-03**: the CSV is the machine-readable form
IANA publishes, and COSE libraries generally hard-code the subset they support
rather than reading it.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, with the snapshot digest |
| `summary.md` | this document |

**No committed copy of the registry.** `library/CLAUDE.md` forbids committing
third-party documents, and the sibling records `iana-cbor-tags` and
`iana-cbor-simple-values` set the same pattern: digest and URL only. The CSV
is cached in `.cache/`, which is gitignored.

## Limits

- **It is a living document, so the digest dates rather than fixes it.**
  Unlike an RFC, this record's `sha256` identifies *a snapshot*, not a work.
  Any claim here is true as of 2026-10-03 and should be re-checked, not cited
  as settled. This is the one record in the lane where the digest means
  something weaker than usual.
- **Checking it caught a real error elsewhere.** `draft-ietf-cose-sphincs-plus-10`
  (July 2026) proposes `TBD1 (-51)` and `TBD2 (-52)` for SLH-DSA, but **both
  values are already assigned** to ESP384 and ESP512 by RFC 9864. The draft's
  suggested code points must move. This is exactly the kind of thing only the
  registry reveals, and the argument for holding it as a record rather than
  trusting the RFCs.
- **Eleven entries are Deprecated and still listed.** RS1, and the other
  SHA-1 and legacy constructions, remain in the table. Presence in the
  registry is not approval, and a verifier that accepts anything registered
  accepts deprecated algorithms.
- **"Recommended: Yes" is IETF consensus, not a cryptographic verdict**, and
  it is per-entry with no stated review cadence. It tells you what the WG
  thought at registration time.
- **There is no SLH-DSA entry at all.** Post-quantum COSE today means ML-DSA.
  The hash-based hedge has no code point, which is the registry's own
  confirmation of the gap recorded in `fips-205`.
