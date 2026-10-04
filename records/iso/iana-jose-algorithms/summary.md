---
schema: "library-summary/v1"
id: iana-jose-algorithms
record: iana-jose-algorithms
type: summary
updated: "2026-10-03"
---

# IANA JSON Web Signature and Encryption Algorithms registry

|  |  |
|---|---|
| **Type** | dataset — a living registry |
| **Maturity** | _unset_ — a living allocation table has no RFC 2026 standing |
| **Publisher** | IANA |
| **Snapshot** | **2026-10-03** (67 entries) |
| **Identifier** | https://www.iana.org/assignments/jose/jose.xhtml |
| **Source** | https://www.iana.org/assignments/jose/web-signature-encryption-algorithms.csv |
| **Digest** | `sha256:0e997b2cad5bb64c3fd383ac1e66db0af6095ea05b1228eb27dddfbb0c8654cd` |

## Overview

The JOSE counterpart to `iana-cose-algorithms`: the authoritative list of JWS
and JWE algorithm names, populated initially by `rfc-7518` and extended since —
including by `rfc-9964`, whose ML-DSA registrations land in **both** registries.

Its distinguishing column is **JOSE Implementation Requirements**, which COSE
has no equivalent of. The 2026-10-03 snapshot holds 67 entries:

| Requirement | Count |
|---|---|
| Optional | 43 |
| Recommended | 8 |
| **Prohibited** | **8** |
| Required | 3 |
| Recommended+ | 3 |
| Recommended− | 1 |
| Deprecated | 1 |

Post-quantum status: **ML-DSA-44/65/87 are registered**; **SLH-DSA is not**,
matching the COSE side and confirming that
`draft-ietf-cose-sphincs-plus` has landed in neither registry.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | What a JOSE verifier may encounter in an `alg` header |
| Cryptography | `adjacent` | An allocation table, not a specification |
| This project | `adjacent` | Bears on R-M-12; held mainly for the comparison with COSE |

Bears on **R-M-12**. Held chiefly so the governed-namespace question can be
asked of both ecosystems at once: two registries, two governance styles, one
set of underlying algorithms.

## Implementations

Not applicable — a registry, not software. Searched **2026-10-03**: as with
the COSE registry, libraries hard-code their supported subset rather than
consuming the published CSV.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, with the snapshot digest |
| `summary.md` | this document |

**No committed copy of the registry** — digest and URL only, following
`iana-cose-algorithms` and `iana-cbor-tags`.

## Limits

- **A living document; the digest dates rather than fixes it.** Everything
  here is true as of 2026-10-03.
- **JOSE marks algorithms `Prohibited`; COSE has no such state.** Eight
  entries are Prohibited — a stronger signal than COSE's `Recommended: No`,
  and a genuine governance difference between the two registries rather than a
  cosmetic one. A comparison of the ecosystems should start here.
- **Three different negative verdicts coexist** — Prohibited, Deprecated, and
  Optional-but-unwise — with no single column a verifier can filter on. The
  taxonomy is richer than COSE's and correspondingly harder to automate
  against.
- **`none` is in this registry.** The unsecured JWS algorithm from `rfc-7518`
  §3.6 is registered. Its presence, with whatever requirement level, is the
  structural difference from COSE noted in `rfc-7518`'s Limits.
- **Names, not integers**, so this registry can never collide the way the
  COSE one can — the flip side of the byte-cost noted in `rfc-7518`. It is
  also why the SLH-DSA draft's JOSE registrations are uncontroversial while
  its COSE code points conflict.
