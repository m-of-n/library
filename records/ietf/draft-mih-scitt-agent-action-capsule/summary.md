---
schema: "library-summary/v1"
id: draft-mih-scitt-agent-action-capsule
record: draft-mih-scitt-agent-action-capsule
type: summary
updated: "2026-09-30"
---

# An Agent Action Capsule Profile for SCITT

|  |  |
|---|---|
| **Type** | draft (IETF, **individual submission** — not a WG document) |
| **Maturity** | `draft` — `-05`, individual submission; no WG adoption |
| **Authors** | S. Mih (Action State Group) |
| **Published** | 2026-09-26 |
| **Identifier** | draft: draft-mih-scitt-agent-action-capsule-05 |
| **Source** | https://www.ietf.org/archive/id/draft-mih-scitt-agent-action-capsule-05.txt |
| **Digest** | `sha256:c2a498fa…` — full value in `record.yaml`, retrieved and verified 2026-09-27 |

## Overview

A Capsule is a **JSON** object recording one agent action — who acted, under
what authority, with what effect, and how that effect was attested. Its
identity is content-derived: remove `capsule_id`, canonicalise with JCS
([RFC 8785]), and take lowercase-hex SHA-256 over the result (§5.1, §6 check 2).
`canonicalization_id` MUST be exactly `"jcs"`, `format_version` exactly `"4"`,
and JSON floats are forbidden in digest-bearing material.

Despite the title, this is a SCITT **consumer**, not a SCITT document. In 3416
lines the only CBOR is the Producer Envelope (§3.1): a `COSE_Sign1` at tag 18
whose attached payload is the raw 32 bytes of the Capsule ID, with the
protected map fixed to exactly three entries — `alg` (1) = **−8** (EdDSA/
Ed25519), content type (3) = `application/agent-action-capsule-id`, and `kid`
(4) = the **raw 32-byte Ed25519 public key** itself. The unprotected map MUST
be empty; the signature MUST be 64 bytes over `Sig_structure` with context
`Signature1` and empty external AAD. One fixed suite, no agility. Envelopes sit
outside the Capsule-ID preimage, so adding or removing one never changes
`capsule_id`, and each MUST verify independently.

Everything else — seven registry-governed vocabularies, effect records,
assurance rungs, provenance modes, retention declarations — is prose and
eleven tables. There is **no CDDL, no ABNF, no JSON Schema, no figures, and
no examples.**

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | **`adjacent`** | §6's fail-closed verification discipline is a good model, but the document secures a JSON record shape we are not building |
| Cryptography | **`adjacent`** | One fixed suite (Ed25519, `alg` −8) and SHA-256-over-JCS; no agility, no proof mechanics of its own |
| This project | **`adjacent`** | Held as prior art and as the counter-position on R-M-12 — not as evidence about SCITT |

- **DEC-007** — the existing edge, and §3.3 earns it. This is the clearest
  statement anywhere in the library of what RFC 9943 *minimally* requires of a
  Signed Statement, arrived at negatively: *"A bare Producer Envelope is not an
  [RFC9943] Signed Statement. Its protected map intentionally contains only the
  three entries in Section 3.1, whereas an RFC 9943 Signed Statement
  additionally requires protected CWT [RFC8392] iss and sub claims. A
  conforming Transparency Service therefore MUST NOT treat a bare Producer
  Envelope as an RFC 9943 Signed Statement."* Transparency requires a
  **separate** 9943 Signed Statement over the same raw 32 bytes, and its
  Receipt *"does not replace or modify any Producer Envelope and does not by
  itself authorize a Producer Envelope key."* A signature over an identifier
  and a transparency claim about that identifier are two objects here, kept
  deliberately apart.
- **R-M-12** — added by this summary, and it is the reason to keep the record.
  The draft states a **binding invariant**, twice (§4, §12.1): *"verifiers MUST
  treat unregistered values as informational and MUST NOT reject a Capsule for
  carrying one. Registration governs shared meaning, never acceptance."* Set
  against [`rfc-9942`] §4.3 — where a verifier **MUST** confirm that the VDS
  and VDP identifiers match registry entries — the library now holds **both
  poles of R-M-12 in the same topic**: one document that makes registry
  membership load-bearing for verification, and one that forbids exactly that.
  That contrast is worth more to us than anything the Capsule schema contains.

## Why this stays a stub

`docs/extraction.md` (FX-1) requires every `rfc`/`draft`/`spec`/`ietf` record a
PR moves past stub to reach `distillation.profile: full`. This record stays at
`status: stub` deliberately, on four grounds read off the bytes:

1. **Wrong encoding for our decisions.** The Capsule is JSON + JCS. DEC-002
   option 2 is CBOR + CDDL and D-3 is a reduced CBOR profile. With zero CDDL in
   the document, `distilled/schema/` would be empty and the D-3 header mapping
   FX-1 mandates would be a single row — the §3.1 envelope.
2. **209 BCP 14 keyword occurrences with nothing to check them against.** FX-1
   requires *every* one in `requirements.yaml` with `testable` set and the
   counts reconciled. The document ships no example Capsule, no CBOR hex, and
   not one worked digest — a specification for a SHA-256-over-JCS content
   identity that never demonstrates that identity being computed. Nothing
   extracted could be validated against anything.
3. **Most of the bulk is off-axis.** §5.4.3 (provenance and backfill) and
   §5.5.6 (retention declarations) carry ~40 keywords between them and bear on
   none of DEC-002, DEC-005, DEC-007 or D-3.
4. **The surface is still moving.** Individual submission at `-05`, published
   four days before this summary, with `-02` already folded into `versions/`.

Three things are worth citing without extracting, and are recorded above and
below rather than in a `distilled/` tree: §3.3 (DEC-007), the binding invariant
(R-M-12), and §6's nine Class 1 checks — whose closing rule is a good model for
a conformance statement that stays decidable: *"A verifier MUST NOT consult a
model, a clock-dependent heuristic, or network state to decide ok."*

## Implementations

**Not searched for this record.** [`rfc-9942`] records `scitt-cose` (Action
State Group, searched 2026-09-28) — the same organisation as this draft's
author, and the interim change controller §12.1 and §12.3 name for all seven
registries and both media types. Treat SCITT implementation counts in this
library as reflecting one small organisation, not independent uptake.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |
| `versions/-02/` | the superseded `-02` revision, folded per scope §5 |

No `quotes.md`, no `distilled/` — see "Why this stays a stub".

## Limits

- **No test vectors, so no interoperability claim is possible.** Nobody can
  independently confirm interop against this document. The one passage labelled
  a test vector (§6, the check-5 note) is an expected *result* with no input
  bytes.
- **It is evidence about itself, not about SCITT.** `topics/scitt.yaml` reaches
  the same verdict independently: the draft *"contributed nothing to the
  answer — it is a profile consuming the model, not evidence about it."*
- **Seven registries under interim vendor change control** (§12.1: Action State
  Group, Inc., passing to IETF on publication), plus two provisional media
  types (§12.3). None is held by this library.
- **Receipt mechanics are entirely by reference** to [`rfc-9942`] and a receipt
  profile — `I-D.ietf-scitt-receipts-ccf-profile`, which the library does not
  hold.
- **`status: stub`, `confidence: low`** — bytes held and digest-verified, read
  for the three findings above and not further. No human has reviewed this
  summary.
