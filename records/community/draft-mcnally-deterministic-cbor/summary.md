---
schema: "library-summary/v1"
id: draft-mcnally-deterministic-cbor
record: draft-mcnally-deterministic-cbor
type: summary
updated: "2026-10-16"
---

# dCBOR: Deterministic CBOR

|  |  |
|---|---|
| **Type** | draft |
| **Maturity** | draft — an **individual** Internet-Draft, Standards Track intent, no IETF stream and no WG adoption |
| **Authors** | W. McNally, L. Lundblade |
| **Published** | 10 August 2026 (revision -18); **expires 11 February 2027** |
| **Identifier** | draft-mcnally-deterministic-cbor-18 |
| **Source** | https://www.ietf.org/archive/id/draft-mcnally-deterministic-cbor-18.txt |
| **Digest** | `bce4874da41f…` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

dCBOR is an application profile that narrows RFC 8949 until a given value has
exactly one encoding. It takes §4.2.1 core deterministic encoding and adds four
things RFC 8949 leaves to the application: **numeric reduction** (a float whose
value is an integer in `[-2^63, 2^64-1]` must be encoded as that integer, so
`10` and `10.0` are the same data item), **a single NaN** (`f97e00`, every
other NaN spelling rejected), **rejection of `undefined` and of all simple
values but `false`/`true`/`null`**, and **NFC normalisation of text strings**.
Rules bind decoders as well as encoders: a dCBOR decoder must *reject*
non-conforming input, not merely avoid producing it.

Its defining move is to quotient the data model rather than the encoding. §2.5
makes semantically equal numbers the same value, which is why the document
concedes that "some maps that are valid CBOR cannot be reduced to valid dCBOR
maps" — the CBOR→dCBOR mapping is not total. It also registers **tag 201**
("enclosed dCBOR") and two CDDL control operators, `.dcbor` and `.dcborseq`.

It is widely cited as "the" deterministic CBOR profile. It is not: it is an
individual draft, it does not mention CDE anywhere, and the IETF's own
convergence work is happening in `draft-ietf-cbor-cde` and
`draft-ietf-cbor-serialization`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Encoding | **core** | library#39 names it the existing profile closest to DEC-002 option 5, and the extraction compares it rule by rule. |
| Security | supporting | §5 states the threat plainly: the risk is an attacker producing semantically equivalent documents that serialise to different bytes. That is exactly the signing hazard DEC-002 exists to close. |
| Naming | supporting | §2.7's NFC rule is the only answer in our whole reference set to the text-identity question (`canonical-encoding` condition 6), and it answers it with a Unicode dependency. |

**Why we hold it, and what the extraction found.** It bears on **DEC-002**.
MD-3 (2026-09-28) narrowed DEC-002 to option 5 — reduced CBOR, no IANA tags,
COSE export only — and `distilled/design-notes.md` scores dCBOR against that
narrowing rule by rule. Three results are worth stating here:

- **Option 5's three sentences decide 1 of 23 rule-shaped questions; 14 are
  silent.** A reduced profile that has not said where it diverges from the
  nearest existing profile is the "fourth-and-a-half profile by accident" that
  `topics/deterministic-cbor-profiles.yaml` names as the live risk.
- **Option 5 can largely cite dCBOR rather than invent** — which is what
  `R-O-03` requires — with three carve-outs, none of them a modification of
  dCBOR's algorithm: exclude tag 201 and the §8.5 escape hatch by name, add an
  array-order rule (nothing in the document closes condition 5), and restate
  the integer range normatively (see Limits).
- **It cuts against MD-3 in six places**, each naming a DEC-002 option. Tag
  201 and §8.5 favour option 2; the §2.7 NFC rule prices option 5's answer to
  condition 6 and favours option 1; citing an expiring individual draft is the
  third ground against option 3 applied to option 5. Running the other way,
  dCBOR is the only source we hold that states the decoder's obligation
  normatively, which is a gain for option 5 alone.

## Implementations

§4 lists four, all "Coverage: Complete", and the pattern matters more than the
count:

| Language | Organization | Primary maintainer | Note |
|---|---|---|---|
| Swift | Blockchain Commons | Wolf McNally | BSD-2-Clause-Patent |
| Rust | Blockchain Commons | Wolf McNally | BSD-2-Clause-Patent |
| TypeScript | Blockchain Commons | Wolf McNally | BSD-2-Clause-Patent |
| Ruby | — | Carsten Bormann | Apache-2.0; also at cbor.me |

**Three of the four share one maintainer and one organisation**, and the
fourth contradicts itself: its Coverage reads "Complete specification" and then
"Checking of dCBOR - exclusions not yet implemented" — the exclusions being
§2.6 and §2.7, the two rules we most need. **There is no Python
implementation**, and our prototype is Python. *Searched the §4 list and for a
Python dCBOR implementation on 2026-10-16; none found.*

This matters because proposal §3.3 defends option 5 partly on "keeps modern
library support". That is true of CBOR, not of dCBOR: at the profile layer the
support is three-under-one-maintainer plus one incomplete port — the same
weakness the `canonical-encoding` topic held against RFC 8785.

## Limits

- **A normative gap in the document itself.** §7.2 Table 4 requires rejecting
  the 65-bit negative integers `-2^63-1` and `-2^64`, but **no rule in the
  normative §2 forbids them**: `DCBOR_INT` appears only in §2.5 and only as the
  range within which *floating point* values reduce to integers. Nine of
  eleven Table 4 rows trace to a §2 rule; these two do not. §3 cuts the same
  way — it recommends the CDDL prelude's `number = int / float`, whose `nint`
  is the whole of major type 1 and reaches `-2^64`, so a §2 that narrowed the
  integer range would make §3's own sentence false. **The integer range cannot
  be inherited by citing §2**; anyone adopting dCBOR must restate it.
- **Standing.** The draft disclaims its own citability — "It is inappropriate
  to use Internet-Drafts as reference material" — and expires 11 February 2027.
- **§2.7 does not say whether a conforming encoder rejects or rewrites non-NFC
  input**, and that ambiguity is the whole of the identity risk it creates.
- **The source's own test vectors are numeric only.** Nothing in Appendix A
  exercises §2.1 (definite length), §2.3 (map ordering), §2.4, §2.6 or §2.7 at
  all, and tag 201 is defined, registered and never shown. The NFC rule — the
  one most consequential for ARCH-0002 P1 identity — has no fixture, and we
  must build one.
- Smaller defects, all recorded in `distilled/README.md`: §6 names Table 1
  where it means Table 2; §2.7 numbers its decoder rule "1." where every other
  subsection uses "2."; and two of Table 3's parentheticals are arithmetically
  wrong while their hex is correct.
- The extraction is **complete — all three passes at effort max, `profile:
  full`.** Cross-check ran every vector that carries bytes through this
  record's own derived schemas (67 of 72; 0 failures, each rejection under a
  rule its `violates` cites) and finished `messages.yaml`'s requirement links.
  **Nothing here has been signed off by a human** — every `reviewed_by` is
  still empty — so build on it with that in mind.
