---
record: rfc-9942
kind: index
title: "rfc-9942 — distilled artifacts"
extracted: "2026-09-30"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

Source: RFC 9942 "COSE Receipts", 1033 lines, `sha256:da8ed24e…`, cached and
digest-verified. `bin/bcp14-count` gives **16** BCP 14 keywords — REQUIRED 8,
MUST 6, SHOULD 1, MAY 1 — and the extraction reconciles to 16 exactly. The
profile is unusual: **half the keywords are `REQUIRED` used as field
designators** in the §5.2.1 and §5.3.1 receipt tables, four each, not as
sentence-level obligations. Only 8 are prose obligations.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | Every normative statement verbatim with locator, all 16 keywords, plus all 7 CDDL blocks, the 3 IANA tables, both registration templates and §8.2.1's five expert-review criteria. Records separately the non-BCP-14 obligations — §7.1's deliberate "ought to be performed" and "It is recommended", §4.2's "should not expect interoperability", §4.4.1's lowercase "must" — excluded from the count. §3 Terminology retained as definitional-normative. |
| requirements | `requirements.yaml` | 27 entries, R-0001…R-0027: 16 `stated` carrying all 16 keywords, 11 `inferred` carrying none. `source_keyword_count` 16, `extracted_keyword_count` 16, `reconciliation` empty because they agree. The 8 `REQUIRED` field designators each become one requirement quoted as the whole table entry it heads — which lands exactly 8 keywords rather than 0 or 16. |
| schema | `schema/` | All 7 CDDL blocks verbatim, each byte-identical to its source range by md5 — Figures 1, 3, 4, 5, 7, 8 and the uncaptioned §5.3.1 block at lines 616–625 — 33 rule heads over 30 distinct names, ~160 of 1033 lines. Plus `receipts-merged.derived.cddl`, a **derived** compilable rendering with 35 heads, zero duplicates and zero unresolved references. Three defect families recorded, not repaired. |
| messages | `messages.yaml` | 13 structures field by field with labels, types, protection and requirement levels; 37 field entries — 24 carrying real requirement ids (7 of those also carrying a clarifying note), 11 carrying only an honest note for CDDL-only facts, and 2 carrying neither, both being the deliberate "(no fourth element)" entries that record an absence rather than a member; the three header parameters 394/395/396, both proof contents, the one verifiable data structure, the `leaf_index >= tree_size` bound, the §4.3-versus-§5 naming duality, and the two IANA subregistries. |
| protocol | `protocol.yaml`, `protocol.md` | **Not applicable** — the files hold the evidence: 25 search terms, the word "protocol" occurring zero times, all 14 §9 references being format/crypto/IANA documents, and no sentence anywhere with one actor as subject and another as object. `protocol.md` carries a flowchart of the *gap* rather than a sequence diagram. |
| state-machine | `state-machine.yaml` | 3 derived machines — receipt admission (§4.3), inclusion verification (§5.2.1), consistency verification (§5.3.1) — with states, transitions, guards and error states, the `leaf_index >= tree_size` guard, and the detached-payload binding. The **verification-order inversion** is made mechanically visible five independent ways, enumerated as data in `verification_order_inversion.enumerated_ways` — the two order vectors, the per-machine `order` tag and its warning, the transition topology, the four `absent_transitions` entries stating which transitions must *not* exist, and the named `hazard`. |
| examples | `examples/` | **Not applicable** — all 21 `h'…'` literals elided, zero non-elided literals, zero complete 32-hex runs. The file inventories the 3 EDN figures and names where fixtures would have to come from. |
| design-notes | `design-notes.md` | The D-3 header-by-header mapping and export mapping; adopt A1–A7, adapt B1–B7, reject C1–C8; DEC-005 and R-M-12 assessed; open questions O1–O7. Carries the finding that **the COSE dependency runs inbound** for receipts, which D-3's "export only" gloss does not cover, and the four-row table holding both poles of R-M-12 with their asymmetry stated. |

## The three defect families in the source

Recorded across `schema/README.md`, `messages.yaml` and `design-notes.md`, and
deliberately **not** repaired in the verbatim files:

1. **Rule redefinition.** `verifiable-proofs` is defined twice with *different*
   bodies (`{-1 => inclusion-proofs}` at 506 against `{-2 => consistency-proofs}`
   at 618); `protected-header-map` and `unprotected-header-map` are each defined
   twice with identical bodies that nonetheless *mean* different things, because
   each resolves to its own `verifiable-proofs`. RFC 8610 permits no
   redefinition, so the blocks cannot be concatenated.
2. **`cose-value` undefined.** Used at 490, 512, 602 and 624; the document
   defines `cose-values` plural, at 239 only.
3. **`inclusion-proof` and `consistency-proof` undefined.** Referenced as types
   at 504 and 616; the `bstr .cbor` wrapper rules §4.3 spells out at 292–293 and
   331–332 are simply omitted from §5, while `inclusion-proof-content` and
   `consistency-proof-content` are defined and never referenced.

Consequence: **the §5 CDDL cannot be mechanically validated as written**, so the
RFC's own schema cannot serve as a conformance artifact. The derived file is our
reconciliation, not the RFC's.

## Status

Passes 1 (extract), 2 (verify) and 3 (cross-check) are complete and are
recorded in `record.yaml` under `distillation.passes`. **`reviewed_by` is
empty on every artifact** — no human has signed any of them, so these are
readable but not buildable-on.

### Settled in pass 3: which advisory statements earn an inferred requirement

§8.2.1 lists **five** expert-review criteria. Two became inferred requirements
— R-0026 (lowercase "required") and R-0027 ("not permissible"). Pass 1
declined the other three on the ground that they carry no BCP 14 keyword, and
pass 2 was right that this is not the rule applied elsewhere: R-0022 and
R-0025 stand on a lowercase "should" and R-0005 on "encouraged".

Pass 3 settles it by adopting the sibling record's threshold —
`records/ietf/rfc-9943/distilled/requirements.yaml` — so that one rule governs
both records. A keyword-free sentence is promoted when all three hold: a
contiguous verbatim quote; an actor named or unambiguously fixed; and an
obligation, prohibition or ordering **a conforming implementation could
violate**. The threshold is now stated in `requirements.yaml`'s `note:`, and
the outcome is recorded at the point of use in `messages.yaml` under
`iana_subregistries.expert_review.promotion_outcome`.

**Outcome: the three stay declined, on the third limb** — not on the keyword
ground, which was wrong. R-0026 and R-0027 state absolute conditions on what
may exist in the two registries; both are violable by a VDS specification
author, an actor §4.4.1 already binds with two uppercase MUSTs, and both
violations are detectable by inspecting the registries. Criteria 1, 2 and 5
are hortatory advice to the IANA expert reviewer, an actor this document binds
nowhere else, and their violation is exhibited by no artifact: a point
assigned out of sequence is still valid, a squatted point is
indistinguishable from a used one, and two differing change controllers leave
both registrations valid and every label resolving. Criteria 2 and 5 also fail
the second limb, naming no actor. **Neither resolution could move either
keyword count** — all five bullets are lowercase — and the count was re-run
after the edit: still **16** keywords over **27** entries.
