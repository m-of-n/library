---
record: draft-ietf-cbor-serialization
kind: index
title: "draft-ietf-cbor-serialization — distilled artifacts"
extracted: "2026-10-18"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

**State: passes 1, 2 and 3 of 3 complete — `profile: full`.** Human review
(pass 4) is outstanding; every `reviewed_by` is empty. The **extract** pass ran
at effort max, agents in parallel, each reading only
`.cache/draft-ietf-cbor-serialization.txt`. The **verify** pass (2026-10-19,
effort max) re-derived the keyword reconciliation, every quotation and locator,
every fenced and verbatim block, and all 105 vectors from the cached source
alone, and corrected four pass-1 claims. The **cross-check** pass (2026-10-19,
effort max) worked artifact against artifact rather than against the source: it
transcribed the derived ABNF and both pseudocode procedures into a runnable
layered checker and ran every vector through it, completed `constrained_by`
across all 48 fields, wired `violates_requirements` onto every invalid vector,
and found three defects — two in the source (Appendix D's float narrowing, §8's
recursion clause) and one in this library's own check procedure. See
`record.yaml`'s `distillation.passes`.

Source: *CBOR Serialization and Determinism*, `draft-ietf-cbor-serialization-08`.
This record's `usefulness.reason` calls it "the live WG determinism work and
the document a signing profile must target" — see *A contradiction in our own
repo* below.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | statements and verbatim blocks across the source's own section structure. Re-derived by the verify pass: 294 inline quotations all contiguous and correctly located, 36 fenced blocks each byte-exact and uniquely placed, no quotation crossing a page boundary and none spliced |
| requirements | `requirements.yaml` | 100 entries, `R-0001`–`R-0100`, source order: 65 `stated` carrying all 65 BCP 14 occurrences (41 MUST, 8 MAY, 7 RECOMMENDED, 4 SHOULD, 4 MUST NOT, 1 NOT RECOMMENDED), 35 `inferred` carrying none. Counts reconcile 65 = 65, and the verify pass matched each of the 65 source occurrences, by line, to exactly one `stated` entry — none unclaimed, none claimed twice. Two sentences carry two occurrences each for two different actors and are quoted as two non-overlapping clauses rather than twice in full, which would have double-counted |
| schema | `schema/` | 3 verbatim, 3 derived — see below |
| messages | `messages.yaml` | 19 structures, **48 fields, all carrying `constrained_by`**: 40 hold 203 links to 68 of the 100 requirements, 8 hold an explicit `[]` with a note saying why. The two-part linking rule and the five groups of unlinked requirements are in the file header, so a reviewer can argue with a specific link. The map key comparison is spelled out byte by byte |
| examples | `examples/` | 105 vectors, **every hex string the source's own, none computed by us**. 41 valid / 64 invalid under preferred-plus, 31 / 74 under deterministic, 105 / 0 under general; `conformance` carries all three serializations, and every invalid vector now carries `violates_requirements` (64 vectors, 109 links) or `violates_deterministic_requirements` (12, 12) beside its prose reason. All 420 verdicts were re-derived by a checker built from `schema/`. See `examples/README.md` |
| design-notes | `design-notes.md` | this document against RFC 8949 §4.2, CDE and dCBOR; the convergence question its topic owns; the R-O-03 citation target; and where the source cuts against MD-3 |

## Not applicable

Both with quoted evidence in `record.yaml` — findings, not omissions.
**protocol**: the document defines serializations, not an exchange, and says so
in its own Abstract; `handshake`, `session`, `retry`, `exchange` and
`transition` occur **zero** times in 2968 lines, and where a sender and
receiver appear it is to require that the *bytes* match, not that anything is
exchanged. **state-machine**: every occurrence of "state" is the verb *to
state*, checked line by line; the three serializations form a subset lattice,
not a set of states.

## The schema directory is unusual, and the gap it leaves matters

This source **does** ship formal grammar, which is rare in this reference set —
three verbatim artifacts, all small: Appendix F's 12 lines of CDDL for big
numbers, §8's 5-line control-operator definition, and Appendix D's 133-line C
function. Each fence was byte-compared against the cached source by script.

But it ships **no ABNF, no JSON Schema and no CDDL profile of either
serialization it defines.** §8 adds a *control operator* rather than a grammar,
which is in effect the admission that CDDL cannot express the thing. And CDDL
cannot express a shortest-head predicate, definite-versus-indefinite length, or
a sibling-ordering constraint — so **the one difference between this document's
two serializations is invisible in every file here except the two derived
pseudocode procedures.** `schema/README.md` says so per file.

## Source defects and gaps found

Reported, never repaired. Two are substantive:

1. **§3 states the wrong value.** It says `0xc34100` encodes 0; it encodes
   **−1**. `0xc3` is tag 3, the *negative* big number (value −1−n), so with
   content `0x00` the value is −1 — verified by decoding, and `zero.edn` lists
   `0xc24100`/`0xc240` as the encodings of 0. The bullet's point survives (−1
   is also major-type-representable) but the value as printed is wrong.
2. **The conformance corpus cannot distinguish the required sort order from the
   rejected one.** Measured, not guessed: the document prints **16** map
   encodings in all, and on the sort key §5.1 item 2 actually names — "their
   deterministic encodings of the map keys" — bytewise order and RFC 7049 §3.9
   length-first order agree on **all 16, zero disagreements**. Every key in the
   document encodes to 1 byte (the integers 1, 2, 3 in `map.edn`) or 4 bytes
   (the strings "abc", "def", "ghi" in `map_strings.edn`), and equal-length
   keys collapse length-first sorting onto its bytewise tiebreak. **A library
   implementing the rejected length-first sort passes the entire suite.** This
   is the single most useful thing in the extraction for anyone relying on the
   corpus to prove an implementation correct. (Pass 1 reported one
   disagreement; the verify pass could reproduce that only by sorting key bytes
   *as printed* instead of their deterministic encodings — see
   `examples/README.md`, which keeps that encoding as the one place a naive
   encoder would diverge. The correction strengthens the finding.)
3. Appendix F's `bnbstr = bstr .size (8..bnmax)` is one byte too loose: no
   8-byte big-number content can occur in preferred-plus, so the floor is 9 —
   as the document's own `h'c349010000000000000000'` demonstrates.
4. §4.1 item 1 never states the 8-byte argument case, stopping at `ai = 0x1a`,
   although §9.1 enumerates all five widths and Appendix L.2 treats
   `1b`-headed arguments as general-only throughout. Both derived procedures
   supply the step and label it as ours.
5. §4.1 item 1 read literally ("for all major types") admits `0xf8 0x18`–`0xf8
   0x1f`, the simple values 24–31 that RFC 8949 declares not well-formed. The
   exception is never mentioned; the derived files follow RFC 8949.
6. Two scope claims in tension: §4.4 lists **three** differences from RFC 8949
   preferred serialization, while Appendix C.5 calls the NaN restriction "the
   sole difference" from §4.2.1. They reconcile, but the document never does
   it, and anyone comparing this draft against CDE or dCBOR on C.5 alone
   misses the big-number half.
7. **No duplicate-key rule anywhere.** §4.1, §4.2, §5.1 and §5.2 are silent and
   RFC 8949 §4.2.1's prohibition is not restated; C.4 says *when* two float
   keys are duplicates without saying what to do about it.
8. `float_nan_payload.edn` cannot drive the encode test: its
   `edn-representations` is empty ("there is no EDN representation for that")
   while L.1.1's encode test takes the EDN as input.
9. Referenced but never defined: `COSE_Sign1` and `Sig_structure`; and
   C.5's escape hatch — "A new CBOR tag can be defined in the future to
   explicitly support them" — with no tag number and no content model.
10. **Appendix D's example code loses precision on ±2^-25.** Found by the
    cross-check pass. `S2H_MIN_SUBNORM_EXP` is 102 where the biased single
    exponent of the smallest half subnormal (2^-24) is 103, so
    `pref_plus_single_to_half(0x33000000)` returns half `0x0000` — the code
    the document ships as its implementation of "the shortest … **that
    preserves precision**" does not preserve it. Exactly 2 of the 63,493
    inputs it narrows change value, established by exhaustive exact
    enumeration; the parallel `D2S_MIN_SUBNORM_EXP 874` is correct, so it is an
    off-by-one in one constant. No vector exercises it — a corpus gap two
    vectors would close. `design-notes.md` item 17.
11. **§8's recursion clause never mentions tags.** It extends `.serial`
    "recursively through nested arrays and maps" and excludes byte strings; a
    tag's content is neither, so the sentence decides nothing about it — while
    `date_epoch_tag.edn` plainly treats tag content as profile-dependent.
    Recursion through a tag is what the document does, not what it says.
    `design-notes.md` item 18.

## One finding for the COSE export lane

**The structure most often cited as the reason to implement deterministic
serialization does not need it.** Appendix K.2, of COSE's own
deterministic-encoding requirement (RFC 9052 §9) as it bears on the
`Sig_structure`: "This COSE requirement is effectively equivalent to the
deterministic serialization defined in Section 5, since no floating-point NaNs
are involved. It is also effectively equivalent to preferred-plus serialization
as defined in Section 4, because the Sig_structure contains no maps." A
preferred-plus encoder suffices there, and the deterministic mode buys nothing
for it. The verify pass confirmed the quotation and the reasoning: RFC 9052
§4.4's `Sig_structure` is an array of a text string and byte strings — the
protected headers enter it as `empty_or_serialized_map`, a **byte string**
holding an encoded map, not a map — so the one rule deterministic adds over
preferred-plus has nothing in it to bite on, and the document says as much two
paragraphs later ("determinism requirements do not extend into CBOR inside of
byte strings"). Note the subject of the quoted sentence is the COSE
*requirement*, not the structure; a gloss that says "the `Sig_structure` is
equivalent to preferred-plus serialization" compares a structure to a
serialization and should not be repeated downstream.

## A contradiction in our own repo

This record's `usefulness.reason` and `draft-ietf-cbor-cde`'s disagree with
`topics/deterministic-cbor-profiles.yaml`. The topic says "the CBOR WG is now
writing CDE to close it"; both records say CDE expired and parked and that the
live work is *this* document. Both are ours, both are cited, and the topic is
`status: open` with no owner. A reviewer reading only the topic will believe
CDE is the working group's live determinism effort. Recorded here because an
extraction can report it but cannot fix it.
