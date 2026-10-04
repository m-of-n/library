---
record: rfc-8785
kind: index
title: "rfc-8785 — distilled artifact set"
extracted: "2026-10-03"
reviewed_by: ""
---

# rfc-8785 — distilled artifact set

FX-1 full extraction of **RFC 8785, JSON Canonicalization Scheme (JCS)**.
Source `.cache/rfc-8785.txt`, sha256 `63d52294eb0e…b240`, 984 lines, read in
full including Appendices A–I.

**Status: passes 1 and 2 complete; pass 3 (cross-check) has now run to the end
of its checklist, across two sessions.** The record still does **not** declare
`distillation.profile: full`, and pass 3 has deliberately not written its own
entry into `record.yaml`'s pass list: a pass does not get to certify itself, so
the human sets both after reading the report. What pass 3 landed is recorded
below in two parts — before and after the session limit that cut the first
attempt short — and what remains open is in *Known gaps*.

## Artifacts

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 91 verbatim statements and blocks, §2–§6.1 and Appendices A–I, in source order. 36 flagged `_[lowercase/implied]_` — pass 3 added statements 35–37, the three §3.2.3 "measures", to match their extraction as `R-0026/27/28` with `verb: none`. Includes Appendix A in full, Appendix B Table 1 with all 26 rows and footnotes (1)–(4), both Appendix F six-step procedures, and the §5 three-step procedure. Excludes §1, §6.2 informative references, Acknowledgements and Authors' Addresses, none of which carry a normative or testable statement. |
| requirements | `requirements.yaml` | 41 entries `R-0001`–`R-0041` in source order. 32 carry a BCP 14 verb, matching the source count exactly (25 MUST, 4 MUST NOT, 2 RECOMMENDED, 1 SHOULD); 9 are lowercase obligations with `verb: none`. One entry, `R-0036`, is `kind: inferred` and declared non-verbatim. `reconciliation` is no longer empty: the counts agree, but it now records the `R-0006` ↔ `R-0039` cross-reference, which a reader of the file alone cannot see. |
| schema | `schema/` | One verbatim file and three derived. RFC 8785 ships **no** CDDL, ABNF, JSON Schema or grammar of any kind — that absence is structural and is argued in `schema/README.md`. |
| messages | `messages.yaml` | 16 structures, 61 fields. Applicability is **partial** and the file says so: RFC 8785 defines no wire messages, headers or envelopes. What is captured is the output form, the input constraints, the per-type serializations, the complete §3.2.2.2 escaping table, the sort key, and the four appendix structures. |
| protocol | `protocol.md`, `protocol.yaml` | Partial, and the partiality is the finding. No exchange protocol exists, but §5 (normative) and Appendix F (carrying **no** BCP 14 keyword) both specify processing order, and that order is what R-O-05 contradicts. Three flows, five error paths. |
| examples | `examples/vectors.yaml` | 44 entries — 43 executable vectors and 1 recorded absence. All 26 Appendix B rows, the §3.2.3 seven-key sorting vector, the §3.2.4 byte dump, and the Appendix D and E cases. 7 error vectors each carry `violates.rule` verbatim plus `violates.locator`. 4 derived outputs carry `in_source: false`. |
| design-notes | `design-notes.md` | 6 adopt / 6 adapt / 8 reject against ARCH-0001, ARCH-0002 P1/P4/P5, ADR-0001 and DEC-002 option 5. 12 open questions, then 8 source defects numbered 13–20. Concludes that **DEC-002 option 3 should be withdrawn rather than out-scored**, while recording that option 3 wins namespace governance outright. |

**Not applicable:** `state-machine` — RFC 8785 defines no lifecycle, no
persistent state and no transitions. The two Appendix F procedures and the §5
procedure are straight-line sequences and are held in `protocol.md`. The
scaffold stub was removed rather than left as a file of TODOs.

## A counting trap, stated once

Appendix B Table 1 has **26 data rows**, of which **24 carry a serialization**;
the rows for `7fffffffffffffff` (NaN) and `7ff0000000000000` (Infinity) have an
empty JSON Representation cell. Both numbers are correct about different
things, and pass 1 produced one artifact saying 24 and another saying 26. Where
a figure appears in this record, it names which it means.

## What passes 2 and 3 changed

Pass 2 was adversarial and re-derived everything from the source rather than
reading the artifacts as truth. It found **10 defects and fixed 10**. The one
that mattered: `schema/sorting.md` carried the Hebrew property name
**decomposed** as `U+05D3 U+05BC` instead of the precomposed `U+FB33` the
§3.2.3 test vector specifies — wrong bytes, wrong UTF-16 length, and a wrong
sort position. That is precisely the hazard `examples/README.md` warns about,
committed inside the record that warns about it, and it is signature-breaking.
It is also the best available evidence for this topic's condition (6).

Others: a false "re-checkable" invariant about where U+20AC appears raw; a
dropped `[IEEE754]` inside quotation marks; a byte-offset off by one; a wrong
fixture byte count; three wrong token cells in a derived breakdown; and three
cases of extractor prose altered into or spliced inside a `violates.rule` field
that is verbatim everywhere else.

## What pass 3 landed before it was interrupted

1. **`constrained_by` is wired** across all 61 fields of `messages.yaml` — 104
   links to requirement ids, none left empty, none unresolved. This was the largest integration
   gap and it is closed.
2. **The ABNF was not valid RFC 5234 and now is.** Rules named `char` and
   `DIGIT` **are** the core rules, because §2.1 makes rule names
   case-insensitive, so a conforming tool rejected the grammar outright.
   Renamed to `jcs-char` and `digit0-9`; the language defined is unchanged.
   Only a real parser check surfaces this, which is why pass 1 recorded the
   check as not run rather than claiming it.
3. **`normative.md` flags reconciled from 33 to 36** — statements 35–37 added.
4. **`requirements.yaml` `reconciliation`** now records the `R-0006` ↔ `R-0039`
   cross-reference.

## What pass 3 landed on resumption

5. **`i-json-input.schema.json` passes the JSON Schema 2020-12 metaschema.**
   `jsonschema` 4.26.0, `Draft202012Validator`: `check_schema` raises nothing
   and a full `iter_errors` run against the metaschema returns **0 errors**.
   Nothing was changed. Detail in `schema/README.md`.
6. **All 44 vectors validated as a set — 0 mismatches.** Detail below.
7. **`protocol.yaml` cross-checked against `messages.yaml`.** Nothing
   referenced is undefined; four structures are unreachable from any flow, and
   correctly so. Detail below.
8. **The 36-vs-9 reconciliation is written down**, as the table below.
9. **The 13 gap items in `schema/README.md` now name their requirement ids.**
   Twelve name at least one `rfc-8785#R-NNNN`; item 7 (byte order mark) names
   none, because none exists — which is the item's whole point and is now said
   in those words.

## Vector validation — 44 of 44

Pass 3 validated the vectors as a set rather than one at a time, with a real
YAML parser (`pyyaml`; **not** `bin/_yaml.py`, which reads 36 of the 44 values
as the literal string `"|-"` — `library#43`). The declared `vector_count: 44`
matches the actual count. **No mismatch was found and no vector was changed.**

The set is not homogeneous, and reading it as though it were is the trap. Of
the 44, 15 have an `input` that is a JSON document, 26 have an `input` that is
a 16-hex-digit IEEE 754 bit pattern, and 3 have an `input` that is neither
(a list of quoted names, an ECMAScript snippet, and the recorded absence).
Each vector was therefore checked against what it claims to be, in its own
`fidelity` / `expected_form` terms:

| check | population | result |
|---|---|---|
| `input` admitted by `i-json-input.schema.json` | 15 JSON-document inputs | all admitted except `JCS-D-01`, which the schema correctly rejects |
| `expected` admitted by `canonical-output.abnf` | 10 whole-document expecteds | all admitted |
| `expected` admitted by the `number` production | 24 serializing Appendix B rows | all admitted |
| `expected` lines admitted by the `string` production | `JCS-323-02` (7), `JCS-323-03` (4) | all admitted |
| octet layer `jcs-octets` + decode round trip | `JCS-324-01` | 118 bytes, matches, decodes to exactly the `input` |
| error vectors rejected by something nameable | 7 | all 7 — by what, below |
| declared byte/char counts | `JCS-323-01`, `JCS-324-01` | 118 / 116 and 118 / 116, both correct |

Three results are worth keeping:

- **`JCS-D-02`'s `expected` is correctly *rejected* by the ABNF**, and that is
  not a defect. `{"giantNumber": "1.4e+9999"}` carries a space after the
  name-separator, so it is not canonical output — and the vector already says
  so: *"The source prints no canonicalized form of it."* It is the Appendix D
  remedy as the RFC prints it, not a canonicalization result. A harness that
  runs every `expected` through the grammar will flag this one; it should not.
- **`JCS-322-01`'s `expected` is admitted by the ABNF although it is not
  canonical.** Its properties are unsorted. The grammar admits it because the
  grammar cannot express member order — `canonical-output.abnf` gap item 1.
  The vector is therefore a live demonstration of that gap, which is a better
  argument for the gap than the prose about it.
- **The 24 serializing Appendix B rows were re-derived by a real ECMAScript
  engine**, decoding each bit pattern and taking `String(d)` under Node:
  **24 of 24 reproduce `expected` exactly.**

### The 7 error vectors — what rejects each

The point of this column is that three of the seven are **not** rejected by
either derived schema, and a harness that believes otherwise is green for the
wrong reason.

| vector | rejected by | the input schema? |
|---|---|---|
| `JCS-31-E1` duplicate names | a raw-token duplicate-name scan (confirmed: it finds `a`) — `rfc-8785#R-0003` | **no** — admits it; `NOT-EXPRESSIBLE` 1 |
| `JCS-3222-E1` lone surrogate | `canonical-output.abnf` (`unescaped` skips U+D800–DFFF; `UTF8-3` excludes the block) — `rfc-8785#R-0017` | **no** — admits it; `NOT-EXPRESSIBLE` 2 |
| `JCS-3223-E1` NaN | the JSON parser: RFC 8259 has no `NaN` token — `rfc-8785#R-0019` | n/a — not representable |
| `JCS-3223-E2` Infinity | the JSON parser: RFC 8259 has no `Infinity` token — `rfc-8785#R-0019` | n/a — not representable |
| `JCS-B-10` NaN bit pattern | `7fffffffffffffff` denotes NaN; no JSON token exists for it — `rfc-8785#R-0019` | n/a — not representable |
| `JCS-B-11` Infinity bit pattern | `7ff0000000000000` denotes +Infinity; likewise — `rfc-8785#R-0019` | n/a — not representable |
| `JCS-D-01` giant number | the schema's `maximum`: `1.4e+9999` overflows to Infinity on parse — `rfc-8785#R-0005` | **yes**, but only for `giantNumber`; the same object's `int64Max: 9223372036854775807` validates cleanly and still violates `rfc-8785#R-0005`. `NOT-EXPRESSIBLE` 3 |

## `protocol.yaml` ↔ `messages.yaml`

**Nothing referenced by a flow step or an error path is undefined in
`messages.yaml`.** 3 flows (13 steps) and 5 error paths were walked.

The first finding is about the link itself: **`protocol.yaml` carries no
machine-readable reference to `messages.yaml` at all** — no `structure:` key,
no `rfc-8785#R-NNNN` id, and not one structure name appearing verbatim. The
cross-check is therefore a reading, not a lookup, and it cannot be re-run by a
tool. That is a wiring gap of the same kind `constrained_by` closed for
`messages.yaml`, and it is the obvious next piece of work.

Two error paths do map onto named fields exactly, which is the standard the
rest could meet: *"Lone surrogate in string data"* →
`string-code-point-escaping.invalid Unicode (lone surrogates)`, and *"NaN or
Infinity in number data"* → `json-number-serialization.nan_and_infinity`.

**Defined but not reachable from any flow — 4 structures, all correctly so:**
`big-number-as-json-string` (Appendix D), `string-subtype-property` (Appendix
E), `string-subtype-in-array` (Appendix E.1) and
`canonicalized-json-as-wire-format` (Appendix C). None of those four appendices
defines a procedure, so there is no flow for them to hang from. Their absence
from `protocol.yaml` is the document's shape, not an extraction gap.

Six further structures — `json-object-serialization`, `json-object-member`,
`property-name-sort-key`, `json-array-serialization`,
`json-string-serialization`, `json-literal-serialization` — are reachable only
*through* `canonical-json-output`, which flows reach at signature-creation step
3 and signature-verification step 5. That is containment, not unreachability.

Three step texts name things RFC 8785 deliberately does not define —
*"Serialize the data using existing JSON tools"* (creation step 2,
verification step 4) and *"the conventions defined by the ecosystem"* (§5 step
2, and error path 2). Each is already listed under `protocol.yaml`'s `absent:`
key. No structure is missing for them.

**Incidental count correction.** `messages.yaml` carries **104**
`constrained_by` links, not 105; the file's own `note` says 104 and 104 is what
is there. Verified mechanically: 16 structures, 61 fields, 0 fields with an
empty `constrained_by`, 0 ids that do not resolve against `requirements.yaml`,
36 of the 41 requirements wired. The 5 unwired — `R-0031`, `R-0032`, `R-0033`,
`R-0036`, `R-0037` — are exactly the five the `note` names, and all five are §5
obligations on the verifier's procedure rather than constraints on any field.

## The 36 lowercase/implied flags against the 9 `verb: none` requirements

This is the enumeration the interrupted pass derived and lost. It is redone
here from scratch.

The two numbers count different things and were never meant to be equal.
`normative.md` flags **36** statements `_[lowercase/implied]_`;
`requirements.yaml` carries **9** entries with `verb: none`. The overlap is
five. Going the other way, four of the nine come from a statement that is *not*
flagged.

**Where the 9 come from:**

| requirement | from | flagged? |
|---|---|---|
| `R-0026` | statement 35, §3.2.3 measure 1 | yes |
| `R-0027` | statement 36, §3.2.3 measure 2 | yes |
| `R-0028` | statement 37, §3.2.3 measure 3 | yes |
| `R-0029` | statement 39, §3.2.3 | yes |
| `R-0031` | statement 47, §5 | yes |
| `R-0033` | inside statement 48, §5 step 1 | no — 48's lead sentence carries the `MUST` |
| `R-0034` | inside statement 48, §5 step 2 | no — likewise |
| `R-0035` | inside statement 48, §5 step 3 | no — likewise |
| `R-0036` | `kind: inferred`, the ordering of statement 48's three steps | no — not verbatim text at all |

**The other 31 flagged statements, with a verdict for each.** Verdict is
*already a requirement* (5, above), or *correctly excluded* with the reason.
**None of the 31 should become a requirement entry.**

| # | locator | opens | verdict |
|---|---|---|---|
| 1 | §2 | *"Note that this document is not on the IETF standards track…"* | **Correctly excluded** — document-status boilerplate. It does bind "a conformant implementation", but its content is *obey the rest of the document*: an entry would be the conjunction of all 41 others. |
| 3 | §3 | *"This section describes the details related to…"* | **Correctly excluded** — section roadmap. No actor, no obligation. |
| 11 | §3.1 | *"Data to be canonically serialized is usually created by:"* | **Correctly excluded** — lead-in to a two-item list. The obligation is the next sentence, `R-0002`. Structural twin of statement 31, which was deliberately *not* flagged for exactly this reason. |
| 12 | §3.1 Note | *"…JCS-compliant string processing does not take this into consideration."* | **Correctly excluded** — the premise half of a pair whose obligation half is `R-0008` (`MUST` preserve "as is"). Splitting the pair would state one obligation at two strengths. |
| 13 | §3.2 | *"The following subsections describe the steps required…"* | **Correctly excluded** — roadmap. |
| 14 | §3.2 | *"Appendix A shows sample code…"* | **Correctly excluded** — navigational pointer. Contrast `R-0001`, §3's near-identical *"Appendix F describes the RECOMMENDED way…"*, which is a requirement **only** because it carries a keyword. |
| 18 | §3.2.2 | *"The reason for the difference… is due to a wide tolerance on input data"* | **Correctly excluded** — rationale for a worked example. |
| 19 | §3.2.2 | *"…This part is identical to that of ECMAScript. In the (unlikely) event…"* | **Correctly excluded** — roadmap plus a future contingency whose actor is "the developer community" and whose trigger has not occurred. The operative half is already `R-0011` and `R-0018`. |
| 28 | §3.2.2.3 | *"Due to the relative complexity of this part, the algorithm itself is not included…"* | **Correctly excluded** — bibliographic: names V8 and Ryu as references ("may serve as") and points at Appendix B. That the algorithm is *absent* is a source defect, recorded in `design-notes.md`, not a requirement. |
| 29 | §3.2.3 | *"Although the previous step normalized… the result would not yet qualify as 'canonical'"* | **Correctly excluded** — motivating narrative; the obligation is `R-0020`/`R-0021`. |
| 42 | §3.2.3 Note | *"…sorting of data encoded in UTF-8 or UTF-32 would also work, but…"* | **Correctly excluded** — adds no obligation beyond `R-0027`/`R-0029`. It is substantively important as a **caveat that partially undercuts `R-0029`**, and that tension is already carried in `design-notes.md`. |
| 45 | §3.2.4 | *"This data is intended to be usable as input to cryptographic methods."* | **Correctly excluded** — statement of intent. No actor, nothing testable. It is nonetheless the sentence this whole topic rests on. |
| 54 | App. B note (2) | *"Although a set of specific integers like 2**68 could be regarded as having extended precision…"* | **Correctly excluded** — footnote to table row 9 (`JCS-B-09`); a consequence of `R-0018`. |
| 55 | App. B note (3) | *"Values out of range are not permitted in JSON. See Section 3.2.2.3."* | **Correctly excluded** — an explicit back-reference; the obligation it points at is `R-0019`. |
| 56 | App. B note (4) | *"This number is exactly 1424953923781206.25 but will… be truncated and rounded…"* | **Correctly excluded** — footnote to table row 26 (`JCS-B-26`); a consequence of `R-0018`'s "Note 2" enhancement. |
| 57 | App. B | *"For a more exhaustive validation… you may test against a file…"* | **Correctly excluded** — testing advice, explicitly optional, pointing at Appendix I. |
| 58 | App. C | *"…it can also be used as 'Wire Format'. However, this is just an option…"* | **Correctly excluded** — a **permission**, not an obligation, and hedged twice. `requirements.yaml` holds obligations. It is captured instead as the `messages.yaml` structure `canonicalized-json-as-wire-format`, which is why that structure has no flow. |
| 60 | App. C | *"Using canonicalization, the properties above would be output in the order…"* | **Correctly excluded** — worked example (`JCS-C-01`) plus an ergonomics observation; the ordering is a consequence of `R-0020`. |
| 62 | App. D | *"…applications would normally use different native data types…"* | **Correctly excluded** — commentary on the Appendix D example. "would normally", "would presumably": descriptive. |
| 63 | App. D | *"The established way of handling this kind of 'overloading'… is through mapping mechanisms"* | **Correctly excluded** — rationale, describing the alternative the appendix *rejects* in favour of `R-0039`. |
| 66 | App. D | *"…JCS imposes no limits on applications, including when using ECMAScript."* | **Correctly excluded** — a disclaimer of constraint. An entry asserting that no requirement applies would be vacuous. |
| 71 | App. E | *"Note that the 'BigInt' data type is currently only natively supported by V8"* | **Correctly excluded** — a dated ecosystem fact. No actor. |
| 75 | App. E | *"…the string arguments for 'big' and 'time' have changed with respect to the original"* | **Correctly excluded** — narration of the `JCS-E-02` failure case; the obligations are `R-0007` and `R-0041`. |
| 76 | App. E | *"The reason for the deviation is that in stream- and schema-based JSON parsers…"* | **Correctly excluded** — causal explanation of 75; the obligation is `R-0041`. |
| 79 | App. E | *"In an application, 'Amount' can be accessed as any other property…"* | **Correctly excluded** — description of the C#/Json.NET remedy example. |
| 80 | App. E Note | *"Note: The example above also addresses the constraints on numeric data implied by I-JSON…"* | **Correctly excluded** — commentary tying the example back to `R-0005`. |
| 81 | App. E.1 | *"…custom parsing and serialization code may be required to cope with subtypes anyway."* | **Correctly excluded — the closest call in the table.** "May be required… anyway" is a prediction, not a prescription: nothing can fail it. The obligation it anticipates is already `R-0040` (`MUST` deal with subtype interoperability problems), which it extends to arrays without adding anything. Appendix E.1 is two sentences and yields no requirement and no vector — `JCS-E1-01` records that absence deliberately. |
| 82 | App. F | *"The optimal solution is integrating support for JCS directly in JSON serializers…"* | **Correctly excluded** — this is the *content* that `R-0001` points at. Appendix F contains **no BCP 14 keyword anywhere**, so the whole appendix is governed by that one `RECOMMENDED` in §3. |
| 85 | App. F | *"A canonicalizer like above is effectively only a 'filter'…"* | **Correctly excluded** — architectural characterisation, already captured as `protocol.yaml`'s `canonicalizer` role. |
| 86 | App. F | *"…the serialization performed before the canonicalization step could be eliminated…"* | **Correctly excluded** — a hypothetical optimisation ("could be"). |
| 89 | App. H | *"The listed efforts all build on text-level JSON-to-JSON transformations…"* | **Correctly excluded** — related-work comparison. Design rationale, and it is used as such in `design-notes.md`. |

### Verdict in summary

**0 of the 36 should become a requirement entry; 5 already are one; 31 are
correctly excluded.** The recommendation to the human reviewer is therefore to
**add nothing to `requirements.yaml`**. Had any been added it would have had to
preserve `extracted_keyword_count: 32`, because not one of the 36 carries a BCP
14 keyword — the count is of keywords, not of entries, and `verb: none` entries
do not touch it. The 41-entry / 32-keyword pair stands.

The 31 fall into six kinds, and the kinds are the argument:

| kind | statements | n |
|---|---|---|
| roadmap / section lead-in | 3, 11, 13, 19 | 4 |
| rationale or narrative for a rule stated elsewhere | 18, 29, 42, 62, 63, 76, 89 | 7 |
| commentary on a worked example | 60, 75, 79, 80 | 4 |
| footnote restating a consequence of another requirement | 12, 54, 55, 56 | 4 |
| bibliographic or navigational pointer | 14, 28, 57, 71 | 4 |
| permission, disclaimer or statement of intent | 1, 45, 58, 66, 81, 82, 85, 86 | 8 |

### One thing the human should decide

**The flag is applied more broadly than the test `normative.md`'s own header
states.** That header says an entry is flagged "when it states an obligation
that binds an actor and carries no BCP 14 keyword of its own". By that test,
statements 3, 11, 13, 14, 18, 19, 28, 29, 45, 57, 60, 62, 63, 66, 71, 75, 76,
79, 80, 85, 86 and 89 — **22 of the 36** — should not be flagged at all: they
bind no actor and state no obligation. Statement 11 is the sharpest case,
because it is a bare list lead-in and the header *itself* gives statement 31,
another list lead-in, as an example of something deliberately left unflagged.
In practice the flag marks *"carries no BCP 14 keyword"*, which is a different
and broader property than the one the header describes.

The 14 that do survive the stated test are 1, 12, 35, 36, 37, 39, 42, 47, 54,
55, 56, 58, 81 and 82 — and five of those 14 are already the `verb: none`
requirements, which is a good sign that the narrower reading is the one the
requirement set was actually built on.

Both readings are defensible; only one is written down. This pass **did not
change any flag**, because doing so would move the 36 that pass 3 has just
reconciled, and would re-open pass 1's and pass 2's work on a definition rather
than on a fact. The choice — narrow the flag set to 14, or widen the stated
test to match the practice — belongs to the human. Either way the table above
is unaffected: the verdict for all 22 is *correctly excluded* under both
readings.

## Known gaps

~~1. `i-json-input.schema.json` has not been checked against the metaschema.~~
**Closed.** 0 errors against JSON Schema 2020-12; nothing changed.

~~2. The 44 vectors have not been validated as a set.~~ **Closed.** 44 of 44,
0 mismatches, with a real YAML parser.

~~3. `protocol.yaml` has not been cross-checked against `messages.yaml`.~~
**Closed.** Nothing referenced is undefined; 4 structures unreachable and
correctly so.

~~4. The lowercase-obligation enumeration was not written down.~~ **Closed.**
Redone from scratch and written down above: 0 should-be-requirements, 5 already
requirements, 31 correctly excluded.

**Still open:**

1. **`$id` in `i-json-input.schema.json` is a placeholder**, pending whether
   this library publishes schema identifiers at all — a project decision, not a
   record one. See `library#44`. The metaschema run confirms this is a
   publication question and not a validity defect.
2. **Derived files here do not use the `.derived.` filename infix** that
   `rfc-8949` uses; the marker is in each file's header instead. `library#44`.
3. **`protocol.yaml` has no machine-readable link to `messages.yaml`** — no
   `structure:` key and no requirement ids, so the cross-check above is a
   reading and cannot be re-run by a tool. This is the same wiring gap that
   `constrained_by` closed on the `messages.yaml` side, and it is the next
   obvious piece of work on this record.
4. **The `_[lowercase/implied]_` flag is broader than the test
   `normative.md` states for it** — 22 of the 36 fail that test. Recorded, not
   resolved; see *One thing the human should decide* above. No verdict in the
   table depends on which way it goes.
5. **`bin/_yaml.py` still makes every CI check over `vectors.yaml` values
   vacuous** (`library#43`). Pass 3's validation used `pyyaml` and so is
   *not* reproducible by `bin/validate` as it stands.

Gaps 1–4 above, now closed, were the reason `profile: full` was not declared.
**This pass does not declare it**, and does not add its own entry to
`record.yaml`'s pass list: the human sets both after reading the report, so
that a partial run can never leave a false completeness claim behind it.

## A tooling warning that outlives this record

`bin/_yaml.py` has **no block-scalar support** and returns the literal string
`"|-"` for every `|-` value. Every `input:` and `expected:` in `vectors.yaml`
reads as `"|-"` through it, and both `bin/validate` and
`bin/check-pr-extraction` import it — so **any CI check over those values is
vacuous**. The in-file warnings in `protocol.yaml` and `messages.yaml` against
`>` and `|` are working around this, not expressing a style preference. A
defect of the `sorting.md` class above would not be caught by CI today.
