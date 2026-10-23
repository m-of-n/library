---
record: draft-ietf-cbor-cde
kind: index
title: "draft-ietf-cbor-cde — distilled artifacts"
extracted: "2026-10-16"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

**State: complete — all three passes, `profile: full`.** The extract pass ran,
at effort max, one agent per artifact kind, each reading only
`.cache/draft-ietf-cbor-cde.txt`. The **verify** pass then ran adversarially, at
effort max, against the same cached source and against nothing the extract pass
wrote: it re-derived the keyword count and mapped all 40 occurrences one-to-one
onto stated requirements; re-checked every quoted text in `requirements.yaml`
and `normative.md` for contiguity and locator; re-parsed Tables 4–7 out of the
source and diffed every row against `examples/vectors.yaml`; and re-decoded
every vector with a CBOR decoder and IEEE 754 arithmetic written for the
purpose rather than a library. What it moved is listed under *What the verify
pass changed* below.

The **cross-check** pass then ran at effort max as a third agent that had
neither extracted nor verified, working **artifact against artifact** — the
source was opened only to adjudicate. It did the check nothing earlier had done:
it transcribed the derived pseudocode and the data-model rules of the two
derived CDDL files into a runnable layered checker and ran **every vector that
carries bytes — 117 of the 118 — through it: 96 valid accepted, 21 invalid
rejected, 0 failures, every rejection under a rule the vector's own `violates`
cites.** The 118th carries no bytes and was synthesised as its own notes
instruct. It showed the checker discriminates on 54 cases the source never
prints, and ran the source's own re-encode check over all 96 valid vectors
byte-exact. It walked all 73 requirements for the structure each names and
**completed `messages.yaml`'s `constrained_by`: 81 fields, 240 links, 62 of the
73 requirements** — with 18 fields deliberately left at zero and each carrying
its reason. It wired `examples/vectors.yaml`'s `violates` prose to requirement
ids (55 links across the 22 invalid vectors), reconciled the counts pass 2
moved, traced all 28 rows of `design-notes.md`'s option-5 table to requirement
ids, and found two new source defects (D-5 and D-6) and one place where our own
files contradicted each other about where the §3.3 key comparison is held. **No
quoted source text, no locator, no requirement and no vector changed.** Nothing
is left but a human `reviewed_by` and the RFC 8610 parser run
`schema/README.md` asks for.

Source: *CBOR Common Deterministic Encoding (CDE)*, `draft-ietf-cbor-cde-13`,
"Updates: 8949 (if approved)". The draft **expired 2026-04-17**, and the -13
revision note says it merely merges open pull requests ahead of an interim.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 176 located statements and 50 verbatim fenced blocks (33 source ranges, once blocks split only by a page break are rejoined) across 32 headings, §1 through Appendix F. Excludes Status of This Memo, Copyright, ToC, About This Document, §7.2 informative references, List of Figures, List of Tables, Acknowledgments, Contributors and Author's Address, each omission named in the file's own preamble. Mechanically verified twice: 176/176 bullets contiguous substrings of the source and every locator names the section that actually contains the quote; 50/50 fences byte-exact source line runs with no page furniture leaked; all 7 tables and the one figure caption captured in full, row for row |
| requirements | `requirements.yaml` | 73 entries, `R-0001`–`R-0073`, source order, no gaps: 40 `stated` carrying all 40 BCP 14 occurrences (33 MUST, 3 MUST NOT, 1 RECOMMENDED, 1 NOT RECOMMENDED, 1 MAY, 1 SHOULD), 33 `inferred` carrying none. `source_keyword_count` and `extracted_keyword_count` both 40; `reconciliation` is filled anyway because five of the 40 occurrences are counted by the tool but impose nothing on a CDE implementation (two inside an invented example protocol in Appendix B, two inside a block quote of RFC 9679 §4.2, one a bare meta-mention). Verify pass: the 40 source occurrences were re-enumerated by line and matched one-to-one onto the 40 `stated` entries — none claimed twice, none unclaimed — and the five-occurrence argument was re-derived from the source and holds |
| schema | `schema/` | 2 verbatim — `cde-control-operator.cddl` (the `.cde`/`.cdeseq` definition) and `try-float16-encode.c` (Appendix F Figure 1, the source's own C function) — and 5 derived: a constraints CDDL, a shortest-head CDDL, and pseudocode for encoding, for checking, and for float shortest-head. Verify pass: both verbatim extracts re-checked byte for byte against the cached source (`leaf = #6.24(bytes .cde any)` at line 915; Figure 1 at lines 2195–2215), the C file now compiles, and the source's `try_float16_encode` was cross-checked against an independent implementation over 125,560 inputs including all 65,536 binary16 patterns — no disagreement. See `schema/README.md` |
| messages | `messages.yaml` | 24 structures, 81 fields: the data item head, each major type's encoded layout as CDE constrains it, the shortest-head argument forms, float shortening, and the bytewise map-key comparison. **Every field carries `constrained_by`: 63 of the 81 hold 240 links to 62 of the 73 requirements, and 18 hold an explicit empty list with a reason on the field.** Those 18 are a result, not a hole: six of the eight major-type assignments (CDE pins only major types 0 and 1), the [IEEE754] interchange widths in all three float layouts plus `nan-encoding.exponent` — R-0044 enumerates a NaN's preserved value as sign bit, quiet bit and payload, which are exactly the structure's other three fields — three of Appendix F's four fields, because **no requirement in `requirements.yaml` has an Appendix F locator at all**, and `major-type-2-byte-string.content`, the only major-type content field with no link, against text-string content's four. The linking rule is stated in the file header so a reviewer can argue with a specific link; the per-field source locators are kept beside the links, because they are what the links were resolved against |
| examples | `examples/` | 118 vectors, `V-0001`–`V-0118`: 96 `valid`, 22 `invalid`, every invalid one carrying a `violates`. Drawn from Tables 4–7 (examples, failing examples, preferred serialization) and from prose. Verify pass: Tables 4, 5 and 6 were re-parsed out of the source and diffed row for row — 22/22, 63/63 and 8/8 match in order, byte for byte — and all 117 vectors that carry hex were re-decoded with a CBOR decoder and IEEE 754 arithmetic written for the purpose, agreeing on every `diagnostic`, every `decoded` and every `expect`. See `examples/README.md` |
| design-notes | `design-notes.md` | what CDE requires; adopt / adapt / reject; a rule-by-rule table of every CDE rule against option 5 as drafted; the three-level answer to "what is option 5's relation to CDE"; the cost of citing an expired draft; four findings on where CDE cuts against MD-3, each naming an option; and the source's own defects |

## Not applicable

Recorded in `record.yaml` under `distillation.not_applicable`, with reasons.
Both are findings, not omissions:

- **protocol** — CDE defines an encoding constraint set that *other* protocols
  reference, not an exchange. §4: "It does not specify encoding; CBOR
  protocols can specify the use of CDE (or simply definite-length-only
  encoding) independent of the CDDL data model." The only role-shaped language
  in the document is an informative aside in Appendix B describing a
  hypothetical application protocol — informative by the appendix's own first
  line, hypothetical by its own framing ("an application protocol that needs
  to represent birthdate/times **could** specify"), and offered as a negative
  example the document immediately faults ("While this specification is
  interoperable, it lacks determinism"). Every failure path in the document is
  local; the verify pass counted four, not two: an encoder's serialization
  failure (§3.3), a decoder that advertises support rejecting non-conforming
  input (Appendix C preamble), the same preamble's duplicate-key error
  handling, and a CDE-checking decoder refusing to present data to the
  application (C.3.2). None of the four involves a peer, a response or an
  error code.
- **state-machine** — no states, no transitions, no lifecycle beyond a
  one-shot IANA registration. The two things that could be mistaken for
  machines are algorithms: the bytewise key comparison of §3.3 and Appendix F's
  `try_float16_encode`. Both are captured, but **not both verbatim** — the
  cross-check pass corrected that claim, which this file and `record.yaml` both
  carried. `try_float16_encode` is verbatim, in
  `schema/try-float16-encode.c`. The key comparison is **derived**: its
  sentences are quoted verbatim in `normative.md` (§3.3) and inside
  `schema/cde-encode.derived.pseudocode.txt` §3, but the step-by-step rendering
  there is ours, and the `.derived.` infix says so. `schema/README.md` names
  only two verbatim files and never listed it; saying "both verbatim" was our
  error, not the source's, and under FX-1's derived/verbatim convention it is
  exactly the error the convention exists to prevent.

## The structural finding

Issue #39 calls this record "the IETF baseline option 5 must state its
relation to". The extraction's first result is that the baseline is less
firm than that framing assumes:

**CDE's §3 states the constraints but never names a role.** §3 and its
subsections do carry normative force: five of the forty BCP 14 occurrences sit
there. Four of the five say what a CDE encoding must look like, and they form
the three rules CDE adds — §3.1.1's two MUSTs for integers (one sentence, one
rule), §3.2's "indefinite length encoding MUST NOT be used", and §3.3's
strictly-greater map-key MUST. The fifth is §3.1.2's NOT RECOMMENDED for
signalling NaNs, which binds the protocol designer rather than the encoding.
(The sixth and last body occurrence is outside §3 altogether: §1.2's
RECOMMENDED, the one that makes CDE itself elective.) But every one of the
four is agentless: *"Integers … MUST be encoded"*, not *"a CDE encoder MUST
emit"*. **No sentence in §3 addresses an encoder or a decoder at all.** The only place in the document that attaches
these obligations to a role — and the only place that states any decoder
obligation whatsoever — is Appendix C.3.1 and C.3.2, and Appendix C opens by
declaring "This appendix is informative" and "It does not contain any
normative mandates" while carrying **30 of the document's 40 BCP 14 keyword
occurrences** (29 if the meta-mention of the word MUST in its own preamble is
set aside).

Two places outside Appendix C do describe what a CDE-checking decoder does,
and the verify pass found both; neither is normative and neither rescues the
gap. §1.2 *defines* the term — "A decoder that checks that the encoding
constraints of CDE have been met" — and Appendix E *asserts* the behaviour in
the lowercase: "A CDE-checking decoder checks that no other serialization is
being used in the encoded data item being decoded" (`R-0073`, `kind:
inferred`). So the accurate statement of the finding is this: **what CDE
normatively requires is three agentless encoding rules; who has to do
anything about them, and what a decoder has to check, exists only in prose
the document itself disclaims.**

The matching finding on our side, from `design-notes.md`: **option 5 as
drafted names no canonicalisation algorithm**, so `R-O-03` ("cited, not
invented silently") is not yet discharged. Naming one is ADR work, and it is
the cheapest R-O-03 fix available to the Oct 28 package.

## Source defects found

Reported, never repaired. The first two are substantive:

1. **The constraint has two names.** §2 and **Table 1** — the document's own
   summary table, and so the most-cited place — call it
   `definite-length-encoding` (4 occurrences, **all four inside §2**: the
   defining sentence, the "Combining preferred-serialization with …" sentence,
   and two Table 1 cells). §3.2's defining heading and all **22** other
   occurrences — spread over the Abstract, the ToC, §1, §1.1, §3, §3.2, §3.3,
   §4, A.1, C.2, C.3.1, C.3.2 and E — call it `definite-length-only`. Table 1's
   `cde` row therefore composes CDE out of a name that appears nowhere in §3 or
   the appendices.
2. **Appendix C's disclaimer contradicts its content** (above).
3. "This appendix is informative." appears twice in the same paragraph.
4. Unbalanced parenthesis in C.3.2 item 3: `(see Section 5.3.1 of RFC 8949
   [STD94],` is never closed.
5. **C.1.1 item 2's "That is," is not a restatement**, in either direction.
   The sentence "That is, encoders MUST support half-precision and
   single-precision floating point" is offered as a consequence of the MUST
   before it ("If multiple of these encodings preserve the precision of the
   value to be encoded, only the shortest form of these MUST be emitted"), and
   is neither equivalent nor a subset. It is **stronger**, because that MUST
   bites only when more than one width preserves the value: an encoder handed
   only values exactly representable in binary16 never needs binary32 under it,
   yet this sentence requires binary32 anyway. And it is **weaker**, because it
   names only half and single although the same bullet enumerates binary64, and
   an encoder handed a binary64 value with no shorter exact form must emit
   binary64 to satisfy the preceding MUST. (Pass 1 called this simply "new and
   stronger"; the verify pass found it cuts both ways.)
6. C.1.1 item 1's shortest-head range list stops at four additional bytes;
   there is no bullet for the 8-byte range, left implied by exclusion.
7. **C.1.2 versus CDE, reconciled only by implication.** C.1.2 items 2 and 3
   say a decoder accepting Preferred Serialization MUST accept
   indefinite-length items; §3.2 forbids them outright, and C.3.2 item 1 makes
   a CDE-checking decoder check *both* preferred-serialization and
   definite-length-only. The document's only answer is C.1.2's own scoping
   sentence — "**Partial decoder implementations that want to accept at least
   Preferred Serialization** need to pay attention to at least the following
   requirements" — which takes CDE decoders out of C.1.2's scope by
   implication. It is never said in terms, and it is not said anywhere a reader
   following C.3.2 item 1 back through the words "preferred-serialization"
   would arrive. A CDE decoder must not accept what C.1.2 item 2 says it must
   accept. (Pass 1 called this flatly "unreconciled"; the scoping sentence is
   the part it missed.)
8. "Updates: 8949 (if approved)" and §1's "it does not make technical changes
   to RFC 8949" sit against §3.1.1's "CDE turns this recommendation into a
   mandate". Coherent only if CDE is read as a newly-named constraint set
   rather than an amendment, which the document never says.
9. Draft-state artefacts left in the body, all captured verbatim: the -13
   merge note, the `.dlo` note in §4, and "RFC Editor: please replace
   RFCXXXX". Any `XXX` a scanner finds in `normative.md` is the source's own
   placeholder, not one of ours.
10. **C.1.1 item 1 says "argument" and then enumerates integer values**
    (cross-check pass; `design-notes.md` D-5). The lead-in scopes the rule to
    "any argument that is not a floating point value", but all four bullets are
    written as signed integer ranges — "0 to 23 **and -1 to -24**" and so on.
    An argument is never negative. So the widths are stated only for integers,
    the lead-in states the rule without the widths, and a reader encoding a
    300-byte string or a 300-element array must generalise. Read with defect 6,
    the document never gives a width table for arguments as such.
11. **The C.1.2 scoping problem bites three times, not once** (cross-check
    pass; `design-notes.md` D-6). Defect 7 above is the indefinite-length case.
    C.1.2 item 5 is a third: "Leading zero bytes in the tag content of a tag 2
    or 3 MUST be ignored" against C.1.1 item 3's "Leading zeros MUST NOT be
    present" and C.3.2 item 1's checking duty — one checklist says ignore,
    the other says reject, and the same implicit "Partial decoder
    implementations" sentence is the only resolution.

## What the verify pass changed

Pass 2 (2026-10-18, effort max) re-derived everything pass 1 asserted, from the
cached source, without reading pass 1's reasoning. Corrections, in descending
order of how much rests on them:

1. **The structural finding was overstated and is now sharpened** (above). §3
   is not silent: it carries five of the forty keywords and three rules. What
   §3 never does is name a role. And "the only statement anywhere in the
   document" was false — §1.2 defines the CDE-checking decoder and Appendix E
   asserts what it does, both non-normatively.
2. **Appendix C carries 30 of the 40 keyword occurrences, not 29.** The
   breakdown is C preamble 1, C.1.1 13, C.1.2 9, C.3.1 3, C.3.2 4. 29 is the
   count after setting aside the preamble's meta-mention of the word MUST
   (`R-0032`). `design-notes.md` already said 30; this file and
   `requirements.yaml` said 29. Fixed in both.
3. **`definite-length-only` occurs 22 times, not 21** (defect 1).
4. **C.1.1 item 2's "That is," cuts both ways**, not just one (defect 5).
5. **C.1.2 is scoped, not merely unreconciled** (defect 7).
6. **`normative.md` had dropped six statements**, now added: §1.1's three
   sentences describing Appendix C.1, C.2 and C.3; §3's statement of what the
   Core Deterministic Encoding Requirements are designed for; and §4's
   `"float16"` sentence (its `"float32"` sibling was present) and "CDDL
   specifications may want to specify that the data items should be encoded in
   Common CBOR Deterministic Encoding." 170 bullets became 176.
7. **`schema/try-float16-encode.c` did not compile.** The figure caption sat
   bare inside the BEGIN/END VERBATIM region, so the file contradicted its own
   header claim that it "still compiles as-is". The caption now sits in a
   comment just outside the region; the verbatim region is exactly source lines
   2195–2215, byte for byte, and `cc -c` exits 0.
8. **Four counts in `record.yaml` and this file were stale or wrong**: 39
   source ranges for the fences (33), "exactly two failure paths" (four, all
   local), `constrained_by` "populated only where pass 1 was confident" (absent
   throughout, deliberately), and Tables 5 and 6 "spot-checked, not
   exhaustively re-derived" (now re-derived, row for row).

What it could not break, and tried to:

- **The keyword reconciliation.** 40 in the source, 40 in the extraction, one
  per `stated` entry, and each of the 40 source occurrences matched to exactly
  one entry whose quoted text spans the line it sits on. No occurrence claimed
  twice, none unclaimed. The argument that five of the 40 impose nothing on a
  CDE implementation was re-derived independently and holds: two are a
  hypothetical protocol the document itself faults for lacking determinism, two
  are RFC 9679's own obligations inside a block quote, one is a meta-mention.
- **Every quotation.** 73/73 requirement texts and 176/176 `normative.md`
  bullets are contiguous substrings of the source after collapsing hard line
  wraps, and every locator names the section that actually contains the quote.
  No spliced quotes. 12 bullets and 0 requirements depend on the
  hyphen/solidus rejoin; 0 bullets and 4 requirements depend on stripping a
  `|` margin. 50/50 fenced blocks are exact source line runs with no page
  header or footer leaked.
- **Every table.** All 7 tables and the one figure caption are captured in
  full. Tables 4, 5 and 6 were re-parsed out of the source and diffed against
  the vectors row for row: 22/22, 63/63, 8/8 in order and byte for byte. All
  9 distinct serializations Table 7 prints are covered by a vector.
- **Every fixture.** All 118 vectors reproduce. 117 carry hex and were decoded
  with a CBOR decoder and IEEE 754 arithmetic written for this pass — exact
  rationals, round-half-even, no library and no `struct` float unpacking — and
  every `diagnostic`, `decoded` and `expect` agreed. The 8 EDN-form
  diagnostics were additionally re-encoded from scratch and matched byte for
  byte. Every one of the 22 `invalid` vectors has an independently computed
  violation backing its `violates`. `V-0118` is correctly marked as our
  computation; `V-0117`'s bytes are the source's three-line annotated dump
  concatenated and lower-cased, as its note says.
- **Appendix F's C code.** Cross-checked against an independent implementation
  of the same rule over 125,560 inputs, including all 65,536 binary16 patterns
  widened to binary64 — no disagreement. The source's Figure 1 is correct.
- **Both `not_applicable` verdicts.** No exchange between roles, no lifecycle.
  The Appendix B sender/receiver aside is informative by the appendix's own
  first line, hypothetical by its own wording, and offered as a negative
  example.
- **The unbalanced parenthesis** in C.3.2 item 3 (defect 4) is real.

## What the cross-check pass did

Pass 3 (2026-10-18, effort max) worked **artifact against artifact**; the cached
source was opened only to adjudicate a disagreement between two of our own
files. Nothing pass 2 established was re-derived.

**The four checks `docs/extraction.md` asks for.**

1. **Every field a requirement names exists in `messages.yaml` or the schema.**
   All 73 requirements were walked for the structure each names. 62 resolve to
   at least one field; 11 name no structure, and each is named in
   `messages.yaml`'s header with its reason — two incorporations by reference
   (`R-0001`, `R-0025`), the document's own RECOMMENDED status (`R-0003`), the
   §4 invitation to *other* specifications (`R-0024`), §5's deployment hinge
   (`R-0026`), the five Appendix B/C occurrences the reconciliation already
   names as imposing nothing (`R-0028`–`R-0032`), and `R-0072`, the only one
   worth arguing about: the fail-closed rule governs what a decoder may hand to
   the application, and no structure here models API surface.
2. **Every message in a protocol flow is defined.** `protocol` is
   `not_applicable` and the artifacts are consistent with the reason. A scan of
   every artifact for exchange-shaped vocabulary — request, response, peer,
   client, server, session, handshake, retry, acknowledgement, error code —
   returns nothing that describes an exchange: the only hits are
   `design-notes.md`'s "on request" and "round-trip fixture package", a
   `messages.yaml` note about a decoder round trip, and this file's own sentence
   saying none of the four failure paths involves a peer. All four local
   failure paths pass 2 counted are present and attributable: the §3.3
   serialization failure (`R-0022`, and `V-0006`), the Appendix C preamble's
   advertise-then-check duty (`R-0033`), the same preamble's duplicate-key error
   handling (`schema/cde-encode.derived.pseudocode.txt` §4.3), and C.3.2's
   refusal to present (`R-0072`).
3. **Every state-machine trigger is a defined message or named event.**
   `state-machine` is `not_applicable` and no artifact posits a state or a
   transition. The reason itself was wrong in one respect and is corrected
   above: the §3.3 key comparison is held derived, not verbatim.
4. **Every example validates against the schema.** This had never been done and
   was the pass's main job; the result is under `examples/README.md` and
   `schema/README.md`. 117 of 118 vectors run (the 118th prints no bytes and was
   synthesised as its notes instruct): **96 valid accepted, 21 invalid
   rejected, 0 failures**, each rejection under a rule its own
   `violates_requirements` names. 96/96 valid vectors also satisfy the
   re-encode check the source itself proposes. The CDDL layer catches **0** of
   the 21 — the *Known under-constraint* in `schema/README.md`, measured — the
   head layer 9, the value layer 12, and the §4.2 extra-code check the 1 that
   nothing else does. 54 discrimination cases the source never prints: 54
   correct, 0 wrong.

**What it changed.** Only our own commentary and links; no quoted source text,
no locator, no requirement and no vector.

1. **`messages.yaml`'s `constrained_by` is populated** — 81 fields, 240 links,
   62 of 73 requirements — with the linking rule and its three corollaries
   written into the file header, and a reason on each of the 18 fields that
   carries none.
2. **`examples/vectors.yaml`'s 22 `invalid` vectors carry
   `violates_requirements`** — 55 links, every one resolving to a defined entry.
   The prose `violates` strings are untouched.
3. **"Both captured verbatim in `schema/`" was false** and is corrected in this
   file and in `record.yaml`. One of the two is derived, and `schema/README.md`
   had never claimed otherwise.
4. **`design-notes.md`'s 28-row option-5 table is traced to requirement ids.**
   20 rows resolve; 8 do not, and the reason is now stated per row — two score
   an absence, and six score informative statements that carry no BCP 14
   keyword. The practical finding is that five of the rows our profile most
   needs to cite are citable only as prose.
5. **Two new source defects**, 10 and 11 above (`design-notes.md` D-5, D-6),
   and `design-notes.md` D-4 now points at `V-0007` instead of asking for a
   fixture that already exists.
6. **`schema/README.md` and `examples/README.md` said pass 2 and pass 3 had not
   run.** Both are now written up against what the passes actually did.

**What it could not break.** Every count pass 2 moved is consistent across
`record.yaml`, this file, `requirements.yaml`, `design-notes.md` and
`summary.md`: Appendix C's 30 of 40 keyword occurrences (29 only ever as the
explained alternative), the 33 source ranges behind the 50 fences, the 22
occurrences of `definite-length-only`, and four local failure paths. Both
verbatim schema artifacts are still byte-identical to the cached source and
`try-float16-encode.c` still compiles. All three source defects this record
exists to report — the two names, Appendix C's disclaimer, and C.1.2 reconciled
only by implication — survive untouched, and D-6 strengthens the third.
