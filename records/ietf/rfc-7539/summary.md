---
schema: "library-summary/v1"
id: rfc-7539
record: rfc-7539
type: summary
updated: "2026-11-01"
---

# ChaCha20 and Poly1305 for IETF Protocols

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `informational` — **IRTF**, not IETF Standards Track. **Obsoleted by RFC 8439** |
| **Authors** | Y. Nir (Check Point), A. Langley (Google) |
| **Published** | 2015-05 |
| **Identifier** | RFC 7539 · DOI 10.17487/RFC7539 |
| **Source** | https://www.rfc-editor.org/rfc/rfc7539.txt |
| **Digest** | `sha256:546e12200dbbc7b08cf85c8f07ea8681be89954b7c7e0c56f0c51f775a0ba704` (the .txt, retrieved 2026-11-01). The 2026-10-03 digest `3200f936…` was of the .html, whose bytes still match |

## Overview

An IRTF reference for ChaCha20, Poly1305 and AEAD_CHACHA20_POLY1305. Its argument is about dependency, not novelty: AES has
no widely deployed fast alternative, it is slow without hardware support, and
many implementations are exposed to cache-collision timing attacks (§1), so
protocols need a stable reference for a standby cipher. It introduces no new
primitive. It fixes a 96-bit nonce and 32-bit block counter in place of the
original 64/64 split (§2.3), and composes the two primitives into an AEAD whose
Poly1305 key is derived per nonce from ChaCha20 block 0 (§2.6, §2.8).

**Do not cite this record for the algorithm: cite `rfc-8439`.** That RFC
obsoletes this one, and by its own abstract merges the errata and adds a little
text to the Security Considerations. This record exists so that a citation of
7539 resolves and its status is visible.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | The AEAD matters. This revision of it no longer does |
| Cryptography | `adjacent` | The primitives are real, but the current specification is `rfc-8439` |
| This project | `none` | We sign statements; we do not encrypt them |

**`bears_on` is empty, deliberately**, matching `rfc-8439`. It informs no
`DEC-*` or `R-*`. The topic's interest is that an algorithm identifier must
resolve to a specification, and that identifier resolves to the successor.

## Implementations

Current libraries are listed on `rfc-8439` and are not repeated here. The two
RFCs carry the same vectors: all 204 distinct offset-format hex-dump lines match.
A GitHub repository search on `rfc7539`, run 2026-11-01, returned small
single-purpose repositories, of which one is listed.

| Name | Kind | License | URL |
|---|---|---|---|
| levigross/ChaCha20 | open source | Apache-2.0 | https://github.com/levigross/ChaCha20 |

Commercial: not searched. The search above covered GitHub only.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata and typed relations |
| `summary.md` | this document |

No `distilled/`. Nothing here justifies extracting a superseded document: any
FX-1 work belongs on `rfc-8439`, and neither record has an owning issue yet.
Verbatim normative text lives under FX-1, so this summary cites sections only.

## Limits

- **The §2.8.1 pseudocode contradicts its own prose.** §2.8 specifies both
  lengths as 64-bit little-endian integers, and the worked buffer in §2.8.2
  shows them as 8 bytes. The pseudocode calls `num_to_4_le_bytes` for both. RFC
  8439 §2.8.1 has `num_to_8_le_bytes`. The prose and vectors are normative where
  the pseudocode conflicts (§2.3.1), so the algorithm is not ambiguous, but code
  written from the pseudocode is wrong.
- **Eight errata are filed**: four Verified, three Held for Document Update and
  one Rejected (rfc-editor.org, checked 2026-11-01). Sections touched include
  §2.3, §2.3.2, §2.5.1, §2.6 and §2.8.
- **Security rests on cited papers.** §4 states design goals and says proving
  them is out of scope. The composition's analysis is `[Procter]`, not held.
- **Nonce uniqueness is left to the protocol.** §4 calls it the most important
  consideration, and repetition exposes the XOR of plaintexts and reuses the
  Poly1305 key. §2.7 also declines to specify a PRF.
- **P_MAX is about 256 GB per invocation** (§2.8), with the 64-bit-nonce variant
  only sketched for file or disk encryption.
- **Read scope:** the complete .txt, plus the RFC Editor metadata and errata
  list. RFC 8439 was consulted only for its abstract, its §2.8.1 pseudocode and
  a mechanical comparison of hex-dump lines.
