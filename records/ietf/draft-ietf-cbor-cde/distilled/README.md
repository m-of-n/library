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

**State: pass 1 of 3 complete.** The extract pass ran, at effort max, one
agent per artifact kind, each reading only `.cache/draft-ietf-cbor-cde.txt`.
**The verify and cross-check passes have NOT run**, so this record carries no
`profile` — an unfinished extraction is neither `full` nor `partial`. It is
readable; nothing may be built on it. library#39 owns finishing it.

Source: *CBOR Common Deterministic Encoding (CDE)*, `draft-ietf-cbor-cde-13`,
"Updates: 8949 (if approved)". The draft **expired 2026-04-17**, and the -13
revision note says it merely merges open pull requests ahead of an interim.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 170 located statements and 50 verbatim fenced blocks (from 39 source ranges) across 32 headings, §1 through Appendix F. Excludes Status of This Memo, Copyright, ToC, About This Document, §7.2 informative references, Acknowledgments, Contributors and Author's Address, each omission named in the file's own preamble. Mechanically verified: 170/170 bullets contiguous substrings, 50/50 fences byte-exact source line runs with no page furniture leaked |
| requirements | `requirements.yaml` | 73 entries, `R-0001`–`R-0073`, source order, no gaps: 40 `stated` carrying all 40 BCP 14 occurrences (33 MUST, 3 MUST NOT, 1 RECOMMENDED, 1 NOT RECOMMENDED, 1 MAY, 1 SHOULD), 33 `inferred` carrying none. `source_keyword_count` and `extracted_keyword_count` both 40; `reconciliation` is filled anyway because five of the 40 occurrences are counted by the tool but impose nothing on a CDE implementation (two inside an invented example protocol in Appendix B, two inside a block quote of RFC 9679 §4.2, one a bare meta-mention) |
| schema | `schema/` | 2 verbatim — `cde-control-operator.cddl` (the `.cde`/`.cdeseq` definition) and `try-float16-encode.c` (Appendix F Figure 1, the source's own C function) — and 5 derived: a constraints CDDL, a shortest-head CDDL, and pseudocode for encoding, for checking, and for float shortest-head. See `schema/README.md` |
| messages | `messages.yaml` | 24 structures, 81 fields: the data item head, each major type's encoded layout as CDE constrains it, the shortest-head argument forms, float shortening, and the bytewise map-key comparison. `constrained_by` is populated only where pass 1 was confident from the source's own section numbering; completing it is a cross-check-pass job that has not run |
| examples | `examples/` | 118 vectors, `V-0001`–`V-0118`: 96 `valid`, 22 `invalid`, every invalid one carrying a `violates`. Drawn from Tables 4–7 (examples, failing examples, preferred serialization) and from prose. See `examples/README.md` |
| design-notes | `design-notes.md` | what CDE requires; adopt / adapt / reject; a rule-by-rule table of every CDE rule against option 5 as drafted; the three-level answer to "what is option 5's relation to CDE"; the cost of citing an expired draft; four findings on where CDE cuts against MD-3, each naming an option; and the source's own defects |

## Not applicable

Recorded in `record.yaml` under `distillation.not_applicable`, with reasons.
Both are findings, not omissions:

- **protocol** — CDE defines an encoding constraint set that *other* protocols
  reference, not an exchange. §4: "It does not specify encoding; CBOR
  protocols can specify the use of CDE (or simply definite-length-only
  encoding) independent of the CDDL data model." The only role-shaped language
  in the document is an informative aside in Appendix B describing a
  hypothetical application protocol. There are exactly two failure paths and
  both are local: an encoder's serialization failure (§3.3) and a
  CDE-checking decoder refusing to present data to the application (C.3.2).
- **state-machine** — no states, no transitions, no lifecycle beyond a
  one-shot IANA registration. The two things that could be mistaken for
  machines are algorithms (the bytewise key comparison of §3.3 and Appendix
  F's `try_float16_encode`), and both are captured verbatim in `schema/`.

## The structural finding

Issue #39 calls this record "the IETF baseline option 5 must state its
relation to". The extraction's first result is that the baseline is less
firm than that framing assumes:

**CDE's §3 defines the constraints but never states encoder or decoder
conformance.** The only statement anywhere in the document of what a CDE
encoder emits and what a CDE-checking decoder must check is Appendix C.3.1
and C.3.2 — and Appendix C opens by declaring "This appendix is informative"
and "It does not contain any normative mandates", while carrying **29 of the
document's 40 BCP 14 keyword occurrences**. A reader cannot tell whether CDE
conformance is normatively specified at all.

The matching finding on our side, from `design-notes.md`: **option 5 as
drafted names no canonicalisation algorithm**, so `R-O-03` ("cited, not
invented silently") is not yet discharged. Naming one is ADR work, and it is
the cheapest R-O-03 fix available to the Oct 28 package.

## Source defects found

Reported, never repaired. The first two are substantive:

1. **The constraint has two names.** §2 and **Table 1** — the document's own
   summary table, and so the most-cited place — call it
   `definite-length-encoding` (4 occurrences). §3.2's defining heading and all
   21 other occurrences call it `definite-length-only`. Table 1's `cde` row
   therefore composes CDE out of a name that appears nowhere in §3 or the
   appendices.
2. **Appendix C's disclaimer contradicts its content** (above).
3. "This appendix is informative." appears twice in the same paragraph.
4. Unbalanced parenthesis in C.3.2 item 3: `(see Section 5.3.1 of RFC 8949
   [STD94],` is never closed.
5. C.1.1 item 2 presents a **new and stronger** requirement as a restatement —
   "That is, encoders MUST support half-precision and single-precision
   floating point" — and omits binary64 although the same bullet enumerates it.
6. C.1.1 item 1's shortest-head range list stops at four additional bytes;
   there is no bullet for the 8-byte range, left implied by exclusion.
7. **C.1.2 versus CDE, unreconciled.** C.1.2 says a decoder accepting
   Preferred Serialization MUST accept indefinite-length items; §3.2 forbids
   them outright. C.3.2 item 1 makes a CDE-checking decoder check both, and
   nothing says C.1.2's MUSTs are superseded for CDE decoders.
8. "Updates: 8949 (if approved)" and §1's "it does not make technical changes
   to RFC 8949" sit against §3.1.1's "CDE turns this recommendation into a
   mandate". Coherent only if CDE is read as a newly-named constraint set
   rather than an amendment, which the document never says.
9. Draft-state artefacts left in the body, all captured verbatim: the -13
   merge note, the `.dlo` note in §4, and "RFC Editor: please replace
   RFCXXXX". Any `XXX` a scanner finds in `normative.md` is the source's own
   placeholder, not one of ours.
