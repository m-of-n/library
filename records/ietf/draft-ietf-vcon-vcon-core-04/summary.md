---
schema: "library-summary/v1"
id: draft-ietf-vcon-vcon-core-04
record: draft-ietf-vcon-vcon-core-04
type: summary
updated: "2026-09-22"
---

# The JSON format for vCon — Conversation Data Container

|  |  |
|---|---|
| **Type** | draft (IETF, Standards Track intent) |
| **Maturity** | `draft` — **not a standard**; `-04`, expires 2027-03-11 |
| **Authors** | D. Petrie |
| **Published** | 2026-09 |
| **Identifier** | draft-ietf-vcon-vcon-core-04 |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-vcon-vcon-core-04.txt |
| **Digest** | `sha256:cc2a2cb5…` — full value in `record.yaml` |

## Overview

Defines a JSON container for a conversation: who took part (**parties**), what
was said (**dialog** — recording, text, transfer, incomplete, recording-set),
supporting material (**attachments**), and derived insight (**analysis**).
Integrity and confidentiality are delegated to **JWS** and **JWE** rather than
invented.

Two mechanisms carry more weight than the container itself. **`extensions` and
`critical`** declare which extensions a consumer must be able to process, and
`critical` means *reject if you cannot*. **`redacted` and `amended`** point at a
prior vCon rather than replacing it, so a conversation accumulates a chain of
versions each of which remains addressable.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Delegates signing and encryption; defines no new crypto |
| Cryptography | `adjacent` | Cites JWS, JWE, SHA-512, the IANA COSE algorithms registry |
| This project | **`core`** | An attestation-shaped object **we did not design** |

That last rating is the point. Everything else in this library is either a
document we intend to conform to or prior art we are reacting against. vCon is
neither: an independently-designed signed container binding parties to content.
If *A says B has C* (ARCH-0002 P2) cannot express it, that is a finding about
our model, not about vCon.

`bears_on: DEC-005` — it picked JWS/JWE where we are still choosing an envelope.
`R-M-11` — its subjects are conversations, which are not bytes you can hash.

## Three things worth reading closely

**1. `critical` is must-understand, implemented.** ARCH-0002 **P5** argues
unknown fields must be rejected rather than skipped, and inverts the default so
forgetting is safe. vCon scopes the same idea to *extensions* and makes the
rejection list explicit. Their scoping is narrower than ours; whether that is a
weakness or a lesson is §8 of library#9.

**2. `redacted` / `amended` is a supersession model.** A prior version is
referenced, not replaced. Compare `docs/scope.md` §5, where we fold versions
into one record. vCon keeps them as distinct addressable objects — the opposite
choice, and worth understanding before ours hardens.

**3. It cites the IANA COSE Algorithms registry.** A live, current draft
reaching for registry-allocated identifiers is precisely the pattern **R-M-12 /
ARCH-0002 P1** argues against. Not a criticism of vCon — it is the normal thing
to do — but it is evidence that the alternative has to be made easy or nobody
will take it.

## Implementations

**Not yet searched.** Recorded as a gap rather than an absence — library#9 step 2.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |
| `distilled.md` | compacted normative form, for requirements extraction |
| `requirements/fields.yaml` | extracted field definitions **— unreviewed** |

## Limits

- **It is a draft, not a standard.** `-04` expires 2027-03-11 and the field set
  has changed across revisions. This record pins `-04`; a later revision is a
  **new record**, not an edit.
- **`vcon` (the version field) is marked deprecated in the draft itself**, which
  is a signal the versioning approach is unsettled.
- **We conform to none of it.** Extraction here is to *understand a format*, not
  to implement one — no clause obliges us.
- **The distillation and field extraction in this record are `reviewed_by:
  ""`** — readable, but **nothing may be built on them** until step 6 of
  library#9 is done.
