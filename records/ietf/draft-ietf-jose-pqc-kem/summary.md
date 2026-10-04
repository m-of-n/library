---
schema: "library-summary/v1"
id: draft-ietf-jose-pqc-kem
record: draft-ietf-jose-pqc-kem
type: summary
updated: "2026-10-03"
---

# Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for COSE

|  |  |
|---|---|
| **Type** | draft |
| **Maturity** | `draft` — IETF COSE WG, intended status Standards Track; expires 2027-01-07 |
| **Authors** | T. Reddy, A. Banerjee (Nokia), H. Tschofenig (UniBw M.) |
| **Published** | 2026-07-06 (**revision -06**) |
| **Identifier** | draft-ietf-jose-pqc-kem-06 |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-jose-pqc-kem-06.txt |
| **Digest** | `sha256:a53eb780ae6bb38b71f38d1e500dd3c392f8c124553ec9802835add6deb0145f` |

## Overview

Conventions for using **post-quantum KEMs** — in practice **ML-KEM**, from
`fips-203` — with COSE. It registers the three ML-KEM parameter sets both
standalone and paired with AES key wrap:

| Name | COSE `alg` | Recommended |
|---|---|---|
| ML-KEM-512 / 768 / 1024 | TBD1 / TBD2 / TBD3 | **No** |
| ML-KEM-512+A128KW | TBD4 | **No** |
| ML-KEM-768+A192KW | TBD5 | **No** |
| ML-KEM-1024+A256KW | TBD6 | **No** |

The `+AxxxKW` composites pair each ML-KEM security level with a matched AES
key-wrap strength (128/192/256), which is why `fips-197` and the SP 800-38
series sit behind this draft as much as `fips-203` does.

**Mind the name.** The document is `draft-ietf-**jose**-pqc-kem` but its title,
abstract and content are **COSE** — the WG renamed the work and the draft name
did not follow. Its predecessor was the individual draft
`draft-reddy-cose-jose-pqc-kem`. #8 flagged this rename as a trap and it is a
real one: searching the library or datatracker for a *COSE* ML-KEM draft by
name will not find this.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Real and important, but confidentiality machinery |
| Cryptography | `adjacent` | A binding, not a primitive |
| This project | `none` | Nothing in a key-centric *statement* model turns on a KEM |

**`bears_on` is empty, deliberately** — the same negative verdict recorded on
`fips-203`, and for the same reason. A KEM establishes a shared secret; it
makes no assertion, carries no subject, and produces nothing a verifier could
later re-check. `docs/scope.md` §6 asks that such a verdict be recorded once
rather than re-litigated each time someone notices the gap, so it is recorded
here too rather than inherited silently.

Held so the post-quantum COSE picture is complete: signatures via `rfc-9964`
and `draft-ietf-cose-sphincs-plus`, key establishment via this draft.

## Implementations

Searched **2026-10-03**. **None found.** ML-KEM primitives are widely
available (OpenSSL 3.5+, liboqs, Go `crypto/mlkem`, AWS-LC); no COSE library
was found implementing this binding, which is expected while the code points
are unassigned. That is a result, not an omission.

| Name | Kind | License | URL |
|---|---|---|---|
| — | — | — | none found on 2026-10-03 |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. A draft with unassigned code points, bearing on nothing we
decide.

## Limits

- **Every code point is TBD and every one is marked `Recommended: No`.** Six
  registrations, none assigned, none recommended. This is early work, and the
  "No" is the WG's own signal about readiness — not something to read past.
- **The draft name lies about its scope.** `jose` in the name, COSE in the
  content. Any future citation should give the title alongside the name, or a
  reader will look in the wrong registry.
- **It inherits the whole AES key-wrap stack.** The `+AxxxKW` composites are
  half ML-KEM and half **AES Key Wrap**. #8 lists `sp-800-38f` as optional,
  "ingest if the JOSE/COSE key-wrap path needs it" — this draft is that path,
  so 38F is now held and related. Note that neither this draft nor `rfc-7518`
  states whether `AxxxKW` means KW or KWP.
- **A KEM is not a signature and must never be cited as our post-quantum
  answer.** The same warning `fips-203` carries. The post-quantum *signature*
  bindings are `rfc-9964` and `draft-ietf-cose-sphincs-plus`.
- **It is a draft and expires 2027-01-07.** Revision `-06` is recorded in
  `version` and `identifiers.draft`; a new revision is a re-ingest.
