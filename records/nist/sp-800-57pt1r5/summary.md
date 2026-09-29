---
schema: "library-summary/v1"
id: sp-800-57pt1r5
record: sp-800-57pt1r5
type: summary
updated: "2026-09-26"
---

# Recommendation for Key Management: Part 1 — General

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice` — a NIST Special Publication; guidance and best practice, not a FIPS |
| **Authors** | Elaine Barker |
| **Published** | 2020-05 (170 pages) |
| **Identifier** | SP 800-57 Part 1 Rev. 5 · DOI 10.6028/NIST.SP.800-57pt1r5 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf |
| **Digest** | `sha256:cc32391022c1382ac7c91490f6bcc8838e0f889925270da23ef4e800e2ecb7ad` |

## Overview

The general part of NIST's three-part key-management recommendation. It
defines the security services cryptography provides, enumerates the key types
and the protection each requires, and works through the key lifecycle —
generation, distribution, storage, use, and destruction — as a sequence of
states with transitions between them.

Two contributions earn the record. The first is **cryptoperiod**, split into an
**originator-usage period** and a **recipient-usage period** (§5.3): the window
in which a key may be used to *apply* protection ends before the window in
which the resulting protection may still be *processed*, and the second may
extend well past the first. The second is **Table 4**, which puts dates on
approval: security strength below 112 bits is already disallowed for applying
protection, 112-bit is acceptable **through 2030 and disallowed from 2031**,
and 128-bit and above remain acceptable. Table 2 maps those strengths onto
concrete key sizes per algorithm family.

This is process guidance addressed to an agency with a PKI, not a mechanism
specification. **We conform to no clause in it.** What it supplies is
vocabulary precise enough to say what happens to a name when its key stops
being usable.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The reference for key lifecycle and algorithm-strength transition |
| Cryptography | `adjacent` | It specifies no primitive; it governs the use of primitives specified elsewhere |
| This project | `adjacent` | Bears on `R-M-02`; settles no open `DEC-*` |

`bears_on: R-M-02` — a principal may be identified solely by key or key digest.
That design has an unanswered question attached to it: **what becomes of the
principal when the key reaches the end of its cryptoperiod?** An X.509 name
outlives its key; a key-as-name does not, unless the model says otherwise. The
originator/recipient split is the right shape for the answer — statements
*made* under a key stop at one boundary, statements *verified* under it
continue past it — and it is the most directly reusable idea in the document.

Table 4's 2031 date is the concrete form of the topic question's second half.
What NIST approval settles for a principal named by its key is, in part, an
expiry date.

## Implementations

Searched **2026-09-26**. **No implementations, and none possible** — this is
policy guidance, not an interface. The nearest things are key-management
systems that *claim alignment* with it, which is a different relation from
conformance and not one we can verify:

| Name | Kind | License | URL |
|---|---|---|---|
| — | — | — | Not an implementable specification. Claims of "SP 800-57 compliance" by KMS vendors (HashiCorp Vault, AWS KMS, Thales CipherTrust) describe alignment with its recommendations, not conformance to a testable clause. |

Recording the absence as a result, per the summarisation procedure.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

No `distilled.md`. It uses "shall" extensively, so requirements *could* be
extracted — but per `docs/requirements.md` §5.1 we extract only where we intend
to conform or map, and we intend neither. Extraction here would produce a large
set of obligations addressed to a federal agency that we are not.

## Limits

- **Its trust model is PKI, and ours is not.** The glossary defines a trust
  anchor as "an authoritative entity for which trust is assumed. In a PKI, a
  trust anchor is a certification authority…" and, second sense, "the
  self-signed public key certificate of a trusted CA." ARCH-0001's R-M-01
  rejects exactly that — a central identity authority — so the document's
  vocabulary for *who vouches* is unusable to us even though its vocabulary for
  *key lifetime* is excellent. **Take the cryptoperiod model; leave the trust
  anchor.** Cite this record for lifecycle, never for trust structure.
- **It assumes an organisation, not a protocol.** Roles, policies, agency
  responsibilities, key-recovery obligations. Much of the document has no
  counterpart in a system where a principal is a keypair and there is no
  administrator.
- **Dated by its own table.** Published 2020 with a horizon of 2031; we are
  reading it in 2026. The transition it describes is now near-term, and
  SP 800-131A — which carries the actual approval status, including the
  `deprecated` category this document defines but does not apply — is **not
  held**. Table 4 alone does not tell you the current status of a given
  algorithm.
- **Pre-quantum in its bones.** Table 2 carries only the note that estimates
  "will be significantly affected when quantum computing becomes a practical
  consideration." Rev. 5 predates FIPS 203/204/205 and offers no guidance on
  cryptoperiods for post-quantum keys.
- **Part 1 of three.** Part 2 (policy) and Part 3 (application-specific
  guidance) are separate documents and are not held. Nothing here should be
  cited as "SP 800-57 says" without that qualification.
