---
schema: "library-summary/v1"
id: draft-ietf-cbor-cde
record: draft-ietf-cbor-cde
type: summary
updated: "2026-10-18"
---

# CBOR Common Deterministic Encoding (CDE)

|  |  |
|---|---|
| **Type** | draft |
| **Maturity** | draft — IETF CBOR WG, intended status **Best Current Practice**, "Updates: 8949 (if approved)" |
| **Authors** | C. Bormann (Universität Bremen TZI) |
| **Published** | 14 October 2025 (revision -13); **expired 17 April 2026** |
| **Identifier** | draft-ietf-cbor-cde-13 |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-cbor-cde-13.txt |
| **Digest** | `bc554e3d2d37…` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

RFC 8949 §4.2 defines deterministic encoding but leaves the choice of
*which* deterministic encoding to the application, and four mutually
incompatible profiles grew in that gap. CDE is the CBOR working group's attempt
to close it: a single named constraint set, composed of three parts —
**preferred serialization** (shortest head), **definite-length-only** (no
indefinite-length items), and **lexicographic map sorting** — plus two CDDL
control operators, `.cde` and `.cdeseq`, so a schema can assert it.

Its relationship to RFC 8949 is to make elective things mandatory. §3 selects
§4.2.1's core requirements and excludes the §4.2.3 legacy variant; §3.1.1
"turns this recommendation into a mandate" for the bignum/basic-integer
treatment that §4.2.2 only recommends; §3.2 forbids indefinite lengths
outright; and §3.3 strengthens map ordering to **strictly greater**,
deliberately folding RFC 8949's *validity* rule about duplicate keys into an
*encoding* constraint. In the other direction it declines to exercise §4.2.2's
float choices at all — no special handling of the two zeros, no integer/float
mixing, no NaN canonicalisation beyond a clarification, no subnormal handling,
no tag 4/5 equivalence — and it explicitly **does not require Unicode
normalisation**, which is the sharpest divergence from dCBOR.

Everything CDE does not constrain it pushes to an **ALDR ruleset**
(application-level deterministic representation, §1.1 and Appendix B), which it
declares out of scope and encourages protocols to publish separately.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Encoding | **core** | library#39 calls this "the IETF baseline option 5 must state its relation to". |
| Security | supporting | Determinism is the precondition for signing a structured object; CDE is the candidate for the cited algorithm R-O-03 demands. |
| Naming | supporting | §4's control operators are the only standard way to *assert* determinism in a schema, which bears on how a profile is declared. |

**What the extraction found, bearing on DEC-002 and the Oct 28 ADR.**
`distilled/design-notes.md` scores every CDE rule against option 5, and the
three results worth stating here are:

- **Option 5 as drafted names no canonicalisation algorithm at all.** §3.3 of
  the proposal says "deterministic encoding rules"; MD-3 says "CBOR data
  model". So #39's question — what is option 5's relation to the IETF
  baseline? — is **underdetermined by our own documents**, and `R-O-03`
  ("cited, not invented silently") is not yet discharged. Naming an algorithm
  is ADR work, and it is the cheapest R-O-03 fix available before Oct 28.
- **Option 5 is a subset of CDE's bytes and a superset of its duties.** Every
  option-5 encoding is CDE-conformant, because each restriction option 5 adds
  *removes* encodings; but our obligations go further, because we require
  decoder rejection normatively and forbid discharging the checks by
  re-encoding. It is neither a pure subset nor a superset.
- **It is expressible as "CDE plus eleven restrictions", and CDE supplies the
  vocabulary for the "plus".** Nine are subtractions; only two — a canonical
  order for set-valued arrays, and a Unicode normalisation rule — are
  additions that no candidate profile supplies. CDE's real contribution to us
  is that it gives those additions a declared place to live (an ALDR ruleset)
  so publishing them is *authored at a named layer* rather than a silent
  modification of a cited algorithm. That distinction is the whole of R-O-03.

## Implementations

The draft lists none, and has no Implementation Status section. Its one piece
of running code is Appendix F's `try_float16_encode`, a C function for the
binary32 → binary16 leg of shortest-head — held verbatim at
`distilled/schema/try-float16-encode.c` and cross-checked during the verify
pass against an independent implementation over 125,560 inputs, including all
65,536 binary16 bit patterns widened to binary64, with **zero disagreements**.
*Searched for a named CDE implementation on 2026-10-18; none found in the
document, and the `.cde`/`.cdeseq` control operators are registered but
unexercised here.*

## Limits

- **It expired on 17 April 2026 and is parked.** The -13 revision note says it
  "merges all active pull requests in preparation for the 2025-cbor-17
  interim", so it is a snapshot taken for a meeting. Citing it means citing an
  expired draft.
- **Our own documents disagree about its status, and this is not resolved.**
  `topics/deterministic-cbor-profiles.yaml` says "the CBOR WG is now writing
  CDE to close it", while this record's own `usefulness.reason` says CDE
  expired and parked and that the live work is `draft-ietf-cbor-serialization`.
  Both are ours, both are cited, and the topic is `status: open` with no owner.
  A reviewer reading only the topic will believe CDE is the WG's live
  determinism work. It is not.
- **§3's normative statements are agentless.** "Integers … MUST be encoded",
  never "a CDE encoder MUST emit". No sentence in §3 addresses an encoder or a
  decoder. Obligations are attached to roles only in Appendix C.3.1/C.3.2 — an
  appendix carrying **30 of the document's 40 BCP 14 keywords** that opens by
  disclaiming normative mandates. Appendix E (which does *not* declare itself
  informative) does state one decoder obligation, so the document is not
  silent; but what a *role* must do lives almost entirely in prose the document
  disclaims.
- **The constraint has two names.** §2 and Table 1 call it
  `definite-length-encoding` (4 occurrences, all inside §2); §1, §3, §3.2, the
  appendices and everywhere else call it `definite-length-only` (22). Table 1
  is the document's summary table, so it composes CDE out of a name that
  appears nowhere in §3 or the appendices.
- **C.1.2 versus §3.2 is reconciled only by implication.** C.1.2 says a decoder
  accepting Preferred Serialization MUST accept indefinite-length items; §3.2
  forbids them. C.1.2's preamble scopes itself to "Partial decoder
  implementations", which takes CDE decoders out of scope — but never in terms,
  and never anywhere a reader following C.3.2 item 1 would arrive.
- Smaller defects, recorded in `distilled/README.md`: an unbalanced parenthesis
  in C.3.2 item 3; C.1.1 item 2 presenting a both-stronger-and-weaker
  requirement as a restatement; and draft-state artefacts left in the body.
- The extraction is **complete — all three passes, `profile: full`**. The
  cross-check pass ran all 117 hex-bearing vectors against this record's own
  derived schemas (96 valid accepted, 21 invalid rejected, 0 failures, each
  rejection under a rule its own `violates` cites) and completed
  `messages.yaml`'s `constrained_by`. Nothing here carries a human sign-off
  yet: every `reviewed_by` is still empty, which is what pass 4 is for.
