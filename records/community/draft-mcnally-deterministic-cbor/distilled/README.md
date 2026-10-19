---
record: draft-mcnally-deterministic-cbor
kind: index
title: "draft-mcnally-deterministic-cbor — distilled artifacts"
extracted: "2026-10-16"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

**State: complete — all three passes, `profile: full`.** The extract pass ran
at effort max, one agent per artifact kind, each reading only
`.cache/draft-mcnally-deterministic-cbor.txt`. The verify pass then ran at
effort max as a single adversarial agent that did not extract: it recounted the
BCP 14 keywords independently (18, unchanged), re-tested all 38 requirement
quotes and all 74 `normative.md` bullets and 14 fences as contiguous substrings
of the source (0 failures, 0 splices), decoded all 72 vectors with its own CBOR
decoder and recomputed the 5 that are ours (all 5 reproduce), and fixed six
small errors. All six were in our own commentary — a wrong length claim, a
self-contradicting initial-byte census stated twice, a mistyped example head, a
quotation that had silently lowercased its first letter, and a miscount of the
reconciliation's own items. **No quoted source text, no locator, no requirement
and no vector changed.** See `record.yaml` `distillation.passes`.

The cross-check pass then ran at effort max as a third agent that had neither
extracted nor verified, and worked **artifact against artifact** — the source
was opened only to adjudicate. It did the check nothing earlier had done: it
transcribed `schema/dcbor-validate.derived.pseudocode.txt`,
`schema/numeric-reduction.derived.pseudocode.txt`, the ABNF's admitted-byte set
and the data-model half of the profile CDDL into a runnable checker and ran
**every vector that carries bytes — 67 of the 72 — through all three layers.
52 valid accepted, 15 invalid rejected, 0 failures, and every invalid one
rejected under a rule its own `violates` cites.** (The other 5 carry no bytes
because the source names no instance; they are scope markers.) It then showed
the checker discriminates on 28 cases the source never prints, and ran the
encoder direction on all 43 values Table 3 names, byte-exact. It walked all 38
requirements for the structure each names and **completed `messages.yaml`'s
`constrained_by`: 33 fields, 148 links, 33 of 38 requirements**; it reconciled
the rule counts, the Appendix A coverage claim and the ABNF census across the
artifacts; it fixed one place where our own files contradicted each other about
whether `constrained_by` had been populated; and it found one new source
ambiguity (defect 7 below). **No quoted source text, no locator, no requirement
and no vector changed.** Nothing is left for a later pass but a human
`reviewed_by`, and the two tool runs `schema/README.md` asks for — a real RFC
8610 parser and a real RFC 5234 parser, neither installed here.

Source: *dCBOR: Deterministic CBOR*, `draft-mcnally-deterministic-cbor-18`,
10 August 2026, Standards Track, **expires 11 February 2027**.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 74 located statements and 14 verbatim fenced blocks across §1, §1.1, §2, §2.1–§2.7, §3, §5, §6, §7/§7.1/§7.2 and a restricted §8. Excludes §1's motivation, §4 Implementation Status (marked for removal before publication), §8.1–§8.6 rationale prose, references, acknowledgements and boilerplate. Mechanically verified: 74/74 bullets are contiguous substrings of the whitespace-normalised source, 14/14 fences are byte-exact source line runs |
| requirements | `requirements.yaml` | 38 entries, `R-0001`–`R-0038`, source order, no gaps: 18 `stated` carrying all 18 BCP 14 occurrences (16 MUST, 2 MUST NOT — the document uses no SHOULD, MAY, REQUIRED or OPTIONAL), 20 `inferred` carrying none and each declaring so. `source_keyword_count` and `extracted_keyword_count` both 18; `reconciliation` is written anyway because five of the count's details are invisible to a reader of the file alone. Pass 2 recounted from the source independently: 18 again, same 16/2 split |
| schema | `schema/` | 1 verbatim (`cddl-prelude-number.cddl`, the §3 prelude line) and 4 derived — a profile CDDL, a head-layer ABNF, and pseudocode for numeric reduction and for validation. The source ships almost no formal grammar of its own, so nearly every formal artifact here is ours and is named `.derived.` accordingly. The cross-check pass ran the whole vector set through them and re-derived their own claims: the ABNF census (229 well-formed initial bytes, 202 admitted, the same 27 excluded — 5 by §2.1, 22 by §2.6) and the CDDL audit (14 rules, no duplicates, no undefined references, the same 4 deliberately unreferenced). Their stated division of labour holds exactly: of the 15 runnable invalid vectors the CDDL catches 3 and the ABNF 1 — the "one and a half plus one" rules they claim — and the procedure catches all 15. See `schema/README.md` |
| messages | `messages.yaml` | 17 structures: the data item head and each major type's encoded layout as this profile narrows it, the numeric-reduction forms, and map key ordering. **33 fields, 148 `constrained_by` links, 33 of the 38 requirements** — every field carries at least one. The 5 unlinked requirements constrain no structure and that is the result, not a hole: `R-0002` and `R-0004` are §2's scoping sentences, `R-0031` and `R-0032` §5's security sentences, and `R-0037` is the non-normative RFC 8949 §3.4.2 quotation, whose subject is tag 1's content and belongs to the `rfc-8949` record. The per-structure `constrained_by_note` (section and rule number) is kept beside the links: it is what they were resolved against, and it survives a renumbering |
| examples | `examples/` | 72 vectors, `V-0001`–`V-0072`: 56 `valid`, 16 `invalid`, every invalid one carrying a `violates`. 62 hex strings are the source's own and were each confirmed to occur verbatim in it; 5 are our computation and say so in `notes`; 5 vectors state a case the source names without giving bytes. All 52 hex values in Tables 3 and 4 were decoded by hand against their stated values and agree. **All 67 that carry bytes were then run against this record's own `schema/`: 52 accepted, 15 rejected, 0 failures, each rejection under a rule its `violates` cites.** See `examples/README.md` for the source's own coverage holes |
| design-notes | `design-notes.md` | a 23-rule comparison of dCBOR against option 5 as drafted (same 3, stricter 3, looser 1, direct conflict 1, conditional conflict 1, **silent 14**), the R-O-03 question of whether option 5 can cite dCBOR rather than invent, and six places this document cuts against MD-3 with the favoured DEC-002 option named in each |

## Not applicable

Recorded in `record.yaml` under `distillation.not_applicable`, with reasons.
Both are findings, not omissions:

- **protocol** — dCBOR defines an encoding profile, not an exchange. Its only
  roles are codec roles ("dCBOR encoders:", "dCBOR decoders:"), §2 fixes its
  scope as processing rather than conversation, every failure is a local
  decoder verdict with no error code and no peer, and §8.6 expressly declines
  to specify even an API.
- **state-machine** — no lifecycle. dCBOR conformance is a per-data-item
  predicate defined recursively in §2. The only registration-like content is
  §6's one-time IANA action, which has no states or transitions.

## Source defects found

Reported in the artifacts, never repaired. The first is decision-relevant:

1. **A normative gap.** §7.2 Table 4 requires rejecting the 65-bit negative
   integers `3b8000000000000000` (−2^63−1) and `3bffffffffffffffff` (−2^64)
   as "65-bit negative integer value", but **no rule in the normative §2
   forbids them**. `DCBOR_INT` is introduced only inside §2.5, as the range
   within which *floating point* values are reduced to integers; these two
   encodings are the preferred serialization of their values, so §2.2 does not
   reach them either. Nine of eleven Table 4 rows trace to a §2 rule; these two
   do not. **The integer range cannot be inherited by citing §2.** Found
   independently by three agents in pass 1; pass 2 re-derived it by reading every
   rule in §2.1–§2.7 for an integer-range narrowing and found none, and added
   §3 as corroboration — §3 recommends the CDDL `number` type for numeric fields
   and says it "encompasses the full space of CBOR numeric values representable
   by CBOR major types 0, 1, and 7", a space that reaches −2^64 and so includes
   both values Table 4 rejects.
2. §6 asks IANA to register "Table 1" into the CDDL Control Operators
   registry, but the operators are Table 2; Table 1 is the tag 201
   registration. The same section says Table 1 "has registered" while Table 2
   is still a request, and Table 1's Reference is the placeholder `[RFCXXXX]`.
3. §2.7 numbers its decoder rule "1." where §2.1–§2.6 all number it "2.", so
   §2.7 has two items numbered 1.
4. Two arithmetically wrong parentheticals in Table 3: `-127 (-2^8 - 1)`
   (−2^8−1 is −257; −127 is −(2^7−1)) and `-32768 (-2^16)` (−2^16 is −65536;
   −32768 is −2^15). Both hex encodings are correct; only the labels are wrong.
5. §2.7 does not say whether a conforming encoder rejects or rewrites non-NFC
   input, which is the whole of the identity risk it creates.
6. A tension the source itself acknowledges, and which a later pass must not
   "fix": §2 claims "The rules specified here do not "fork" CBOR" while the
   §2.5 aside concedes Numeric Reduction can turn a valid CBOR map into an
   invalid dCBOR map. The CBOR→dCBOR mapping is not total; the document puts
   the burden on applications rather than on the rules.
7. **Figure 1 is not rejected for the reason §2.5 gives for it** (cross-check
   pass; `design-notes.md` defect 14). §2.5 presents Figure 1 as a valid CBOR
   map dCBOR cannot represent *because reduction collides its keys*. That is
   true of the **encoder**. A **decoder** rejects Figure 1's bytes strictly
   earlier and under a different rule — the key `f94900` is an integral float
   inside `DCBOR_INT`, which §2.5 (1) required to have been reduced and §2.5 (3)
   makes a decoder reject on sight, before any two keys are compared. No input
   makes a dCBOR decoder report "duplicate key" *because of* Numeric Reduction.
   Nothing in the source is false; but in a document that states every other
   rule twice, once per role, the figures invite a decoder test that can never
   fire. `V-0006` records both rules, encoder rule first.
