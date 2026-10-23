---
record: rfc-9596
kind: index
title: "rfc-9596 — distilled artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

**State: passes 1 and 2 of 3 complete. NO `profile` IS CLAIMED.** Extract ran
2026-10-20 at effort max, reading only `.cache/rfc-9596.txt` — never
`summary.md` and never another record's artifacts. **Verify ran 2026-10-20 at
effort max**, by an independent agent that did not extract, over all three
records of the lane at once. **Pass 3 (cross-check) has not run**, and every
`reviewed_by` here is empty.

RFC 9596 is the **last** record of library#39 Tier 2's CWT envelope lane
(`rfc-8392` → `rfc-9597` → `rfc-9596`) and the thinnest: 232 lines, **three
BCP 14 keywords**, no grammar, no example, not one byte. **This extraction
mostly documents absences, which is worth doing precisely because the absences
are the content.**

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | **11 verbatim regions** covering the whole **body** — every one of source lines 69–164 except the six section headings, **76 distinct lines** — and not the front matter (lines 1–65: masthead, abstract, Status of This Memo, Copyright Notice, table of contents), the references, the acknowledgements or the authors' addresses. **[corrected 2026-10-21, pass 3]** this row claimed "the whole document except the references, acknowledgements and authors' addresses"; the abstract is excluded too, and it states the value space a **third** time at lines 16–22. Each region is an exact run of source lines with its own `sha256`. §1 is quoted in three parts because **the value space is stated there as well as in §2** — a reader who treats §1 as background misses half the document's statement of its own type space. Unpaginated source, **zero form feeds**, so no region removes anything |
| requirements | `requirements.yaml` | **21 entries R-0001 to R-0021: 3 `stated`, 18 `inferred`**, counts reconciling **3 = 3**, all 21 texts verified mechanically as contiguous substrings of the whitespace-normalised source. The reconciliation is about what **3** *means*: all three are in §2, **there is no MUST, SHOULD, SHALL or RECOMMENDED anywhere in the document**, and not one of the three requires anything |
| schema | `schema/` | 1 verbatim file, 2 derived. **The document ships no grammar of any kind** — `CDDL`, `ABNF`, `ASN.1` and `JSON Schema` each occur **zero** times, and `syntax` occurs three times as the English word. Five verbatim regions: Table 1, plus the four prose passages that fix the value space (twice — §1 and §2), the placement and the scope limit. **[corrected 2026-10-21, pass 3]** this row called those four *"prose sentences"*; they are four regions carrying **seven** sentences, and the fourth is about scope rather than the value space or the placement. The derived CDDL names the three things it **cannot** express, each of which is a real gap: equality, consistency with content type, and any check at all |
| messages | `messages.yaml` | 3 structures, 4 fields. `constrained_by` wired, 7 of 21 requirements cited, 0 dangling, and the `coverage` block explains the other 14 — *"One field, one prohibition, and nineteen sentences about a check the specification declines to require."* Every layout is **derived**, because nothing is printed |
| protocol | `protocol.yaml`, `protocol.md` | **NOT APPLICABLE, with the measurement written out.** `protocol`, `exchange`, `sender`, `receiver`, **`recipient`** and `verifier` each occur **zero** times — this is the only record in the lane where even `recipient` is absent — and the document says in terms that there is nothing to model: *"Any processing of this parameter is performed by the COSE application using application-specific processing rules."* |
| state-machine | `state-machine.yaml` | **NOT APPLICABLE, with the measurement written out.** `state`, `lifecycle`, `revoke`, `rotate`, `expire` and `registration` each occur **zero** times. The sharpest form of it is the document's own sentence: *"Changes to unprotected headers do not change the type of the COSE object."* **A type indicator is a constant** — fixed at signing — so there is nothing for a state to be |
| examples | `examples/README.md` | **NOT APPLICABLE, and the absence is the finding.** `Figure`, `hex`, `vector` and `diagnostic notation` each occur **zero** times; `example` occurs **once** and is a definition. **Not one `typ` value is named anywhere in the document**, so there is no reference fixture, no worked example of the equality problem, and every fixture is ours |
| design-notes | `design-notes.md` | the in-band substitute for the tag option 5 drops, with the scoping correction that **the argument is ours**; what the mechanism's absence enables and its presence does not prevent; the `rfc-9597` asymmetry; the four-signal table with the third row now proved; 3 adopts, 3 adaptations, 2 rejections; **MD-3 mapped header by header over 7 of our fields**, then **five cuts against MD-3**, one of them the strongest thing in the lane **in option 5's favour**; `DEC-005`; **condition (4) of `canonical-encoding`, which this is the only document in the lane to supply**; the summary's nine findings tested; 6 source defects; 5 open questions |

## The two results

**1. This is the in-band, authenticated substitute for the CBOR tag MD-3
removes — and it converts a recorded cost of option 5 into a recorded
non-cost.** `records/ietf/rfc-9053`'s extraction ended an item with *"option 5
declines the tag registry — no tag, which means the recipient must be told out
of band that these bytes are a `COSE_Sign1`."* Label 16 is the substitute, and
§2's `MUST NOT` puts it inside `Sig_structure` where no CBOR tag ever was.

**With one scoping correction this pass insists on: the word `tag` occurs ZERO
times in RFC 9596.** The document makes no claim about tags at all, so the
replacement argument is **ours** — assembled from §2's `MUST NOT`, RFC 9052
§4.4, and `rfc-8392` §7.1/§7.2's step order — and must be cited as `[analysis]`
in the `DEC-002` ADR rather than attributed to the RFC.

**2. Three keywords, and no MUST, SHOULD, SHALL or RECOMMENDED at all.** The
whole enforcement side of the mechanism is §3's two **lowercase** `should
reject` sentences, and §2 tells COSE libraries to ignore the parameter. **A
conformant implementation of RFC 9596 performs no check whatsoever.** The only
obligation in the document is a prohibition — and it is the prohibition that
makes the mechanism worth having.

## This pass's own quote audit

Built because the lane that wrote these summaries ran one and caught **five
transcription defects in its own prose** — an ellipsis-spliced quotation, two
silently healed line breaks, a terminal colon turned into a full stop, and an
inserted word. The audit here pulls every **unambiguously delimited** quotation
out of every artifact in all three records of the lane — markdown blockquote
runs and `*"..."*` spans, whose delimiters survive the nested `"` that RFC
sentences are full of — and probes each one against every cached source and
every library file, normalising both sides the same way.

**178 quotations audited, 169 resolved as contiguous substrings, 0 splices.**
For any fragment that did not resolve whole, the probe found its longest
matching prefix and then tested whether the remainder matched *elsewhere* — the
signature of two non-adjacent quotes welded into one. **No fragment in these
three records has that shape.**

**It found four defects in this pass's own prose, and each is corrected in
place with the falsified wording recorded:**

1. **An inserted word.** `rfc-9052`'s design notes read *"No tags" and "no
   registry dependence" are different rules, and MD-3 states the first.* All
   three of this lane's design notes quoted it with **`only` inserted**. The
   word is now added in our own voice, marked `[analysis]`, and the three
   summaries carry the same correction.
2. **An ellipsis splice**, in `rfc-9597`'s design notes. The elided clause was
   *"made based on previously unverified information"* — the most load-bearing
   part of the sentence. Now quoted whole.
3. **A silently healed line break**, in `rfc-9596`'s `examples/README.md`:
   *"CoAP Content-Formats"* written as one token where the source breaks it
   across lines 116/117. *[correction 2026-10-21, pass 3 — cross-check] This
   read "The one place in this lane that healed a break was in the record that
   declares three times that it does not." It was not the one place: pass 3's
   whole-span audit found the same break healed twice more, in this record's
   `schema/typ-header.derived.cddl` and in its `record.yaml` examples reason.
   Three sites, all in `rfc-9596`. The sentence's point survives — every healed
   break in the lane is in the record that declares it heals none — but the
   count was wrong.*
4. **A case change** in a quotation of our own `messages.yaml`.

The nine residuals are each accounted for: three are the **superseded summary
wordings** this pass quotes in order to record them, three are the audit
regex over-running past a closing `**` into our own following sentence, one is
the ellipsis form **deliberately preserved** inside the `[correction]` note that
identifies it, and two are our own `[...]`-labelled notes set as blockquotes.

## What pass 2 should attack hardest

1. **The keyword census**, which three separate claims rest on. Recount it
   against `bin/bcp14-count` and against the source by eye; if a fourth keyword
   exists anywhere, two sections of `design-notes.md` change.
2. **The 21 requirement `locator`s.** The texts were verified mechanically as
   contiguous substrings; **no check in this pass tested a locator**, and the
   value space is stated in **both** §1 and §2, so a §1/§2 mix-up is the likely
   error.
3. **The two line-break severances at 85/86 and 116/117.** They are declared
   not-healed in three places; check that no artifact healed one anyway. This is
   the defect class the lane's own audit caught twice.
   *[correction 2026-10-21, pass 3 — cross-check] This read 85/86 as `86/87`.
   Pass 2 reported the wrong numbers corrected "in eight places across six
   files"; this was a ninth, and the only one that asserted them as fact rather
   than quoting them inside a `[correction]` note — it contradicted this same
   file twelve lines below. And the check it prescribes was the right one: pass
   3 found two artifacts had healed the 116/117 break after all.*
   **[pass 2: the breaks are at 85/86 and 116/117, and only the second cuts at
   the hyphen — see `design-notes.md` D-5. No artifact healed either: all 11
   normative.md regions and all 5 schema regions reproduce from the cache byte
   for byte, and R-0004/R-0010 carry exactly what the source prints.]**
4. **The size arithmetic in `design-notes.md` §7.5** — 2 octets against 16 —
   which is this extraction's computation from RFC 8949 §3 heads and is not in
   either document.
5. **The `not_applicable` verdicts**, each resting on word sweeps. In particular
   re-check `protocol`: §2's *"an application might verify ... and reject the
   data structure if it is not"* is the closest thing to a flow in the
   document, and this pass judged it illustrative rather than procedural.

---

## What pass 2 did, and what it found (2026-10-20, independent, effort max)

**1. The keyword census — confirmed, and there is no fourth keyword.** Counted
two ways. `bin/bcp14-count` gives **3**. A raw whole-word sweep over all 233
split lines finds **14** all-caps keyword tokens, of which **11 are the §1.1
BCP 14 recital at L95–L97**, leaving exactly **`OPTIONAL` at L112, `MAY` at
L119 and `MUST NOT` at L130**, all three in §2. No `MUST`, `SHOULD`, `SHALL` or
`RECOMMENDED` anywhere. **So the three claims resting on the census stand**, and
the two sections that would have changed do not.

**2. The 21 locators.** All 21 checked under a **stricter** rule than
`bin/check-locators` applies, comparing the **innermost** containing section
rather than permitting an ancestor: **0 misfiled, 0 imprecise, 0 unresolvable.**
The feared §1/§2 mix-up **did not happen**, even though the value space is
stated in both. 0 terminator suspects. **[corrected 2026-10-21, pass 3 —
cross-check: there was 1.** R-0010's span ran into the following sentence and
stopped inside it, at *"...have a media type name [MediaTypes]"*, truncating
*"and MAY include media type parameters."* — which R-0011 carries whole. Pass 1
reported a terminator check "catching two hand-chosen spans"; this was a third
it did not catch, and pass 2 reported zero. The span is trimmed to the sentence
boundary; the keyword count is unaffected because the `MAY` was never inside
it. Pass 3's own re-derivation: 21 of 21 texts contiguous, 21 of 21 locators
correct under the innermost-section rule, each text occurring exactly **once**
in the source.**

**3. The two line breaks — THIS IS THE DEFECT.** The record said, **in eight
places across six files**, that the wrap cuts *"CoAP Content-Formats"* at
**86/87** and 116/117, *"hyphen and all"*. Both halves of that are wrong for the
first break: it is at **85/86**, and it cuts at the **space** — line 85 ends
`the "CoAP` and line 86 begins `Content-Formats"`, hyphen intact — so joining it
with one space is ordinary whitespace normalisation and **not** a heal. Only
**116/117** is a true hyphenation break. **The data was right everywhere**: all
11 `normative.md` regions and all 5 schema regions reproduce from the cache byte
for byte, and R-0004 and R-0010 each carry exactly what the source prints. So
**no artifact healed anything** — the record's discipline held and only its
account of the breaks was defective. All eight sites corrected; see
`design-notes.md` D-5.

> **[correction 2026-10-21, pass 3 — cross-check]** *"No artifact healed
> anything"* is **false**, and it is the most consequential thing pass 3
> overturned. It is true of the two places pass 2 checked — the `normative.md`
> and schema REGIONS, which are digest-verified, and the requirement TEXTS. It
> is not true of the record's prose: the 116/117 break is healed in
> `schema/typ-header.derived.cddl`'s §2 comment and in `record.yaml`'s examples
> reason, both of which attribute the quotation to **§2**, where the source
> prints `Content- Formats`.
>
> The reason it survived two passes is worth keeping: `CoAP Content-Formats` is
> a genuine contiguous substring of this source, at §1's 85/86 break, which cuts
> at the **space**. So a fragment-level audit resolves the healed token against
> §1 and reports success. Only testing the whole §2 sentence as a single span
> exposes the weld — which is why hazards.md requires the longest-span test and
> a named relaxation channel rather than a per-fragment check.

**4. The 2-vs-16 arithmetic — confirmed by encoding, not by reading.** `61`
encodes as `0x18 0x3d` (**2** octets) and `"application/cwt"` as `0x6f` plus 15
characters (**16** octets), with both head bytes exactly as claimed, and
`rfc-8392` §9.3.1 does register **Id 61** for that media type while §9.2.1
registers the subtype. Worth noting alongside: **61 is also the CWT CBOR tag**
(§9.4.1), which is precisely why this file's warning that a no-tags lint must
not treat `typ: 61` as a tag hit is a real one.

**5. The `protocol` N/A — confirmed.** §2's *"For instance, an application might
verify … and reject the data structure if it is not"* carries **no keyword, no
counterparty and no ordering**, is introduced by *"For instance"*, and sits in a
paragraph that disclaims procedure in terms: *"Any processing of this parameter
is performed by the COSE application using application-specific processing
rules."* Illustrative, as pass 1 judged. The sweeps re-ran clean —
`protocol`, `exchange`, `sender`, `receiver`, `recipient`, `recipients`,
`verifier`, `state`, `lifecycle`, `revoke`, `rotate`, `expire` and
`registration` all **zero**; `example` **once**, at L89, and it is a definition;
`CDDL`, `ABNF`, `ASN.1`, `JSON Schema` all zero with `syntax` three times as the
English word. `application(s)` at **12** under pass 1's tokenisation (10 bare
plus `application-chosen` and `application-specific`) — so the document does
name an actor, just never a counterparty, and that is the right form of the
verdict.

**The scoping holds, and the zero is verified.** `tag` and `tags` each occur
**zero** times, so the typ-replaces-the-tag argument is **ours**. Its three
assembled premises were each checked at source: §2's `MUST NOT` at L130; RFC
9052 §4.4's `Sig_structure`, taken from `records/ietf/rfc-9052`'s own
`cose.cddl`; and `rfc-8392` §7.1 step 6 — the tag is prepended **after** the
signing of step 4 — with §7.2 steps 2–3, where both tags are **removed before**
the cryptographic validation of step 5. **The middle premise is now
demonstrated rather than cited**: pass 2's independent A.3 verification succeeds
on the four-field `Sig_structure` and **fails** when the unprotected map is
folded in. So a CBOR tag is never authenticated, `typ` under the `MUST NOT`
always is, and the argument is sound as well as ours.

**One locator corrected:** `label = int / tstr` was cited as RFC 9052 **§1.4**;
it is **§1.5**. `rfc-9597` carried the same error.

**Body source-line coverage computed**: the only uncovered lines are the six
section headings, so no statement is dropped.

### Pass 2's own lane-wide audits

Run over the lane, not per record, because a per-record audit fixes one of
three and never suspects a pattern — which is exactly how pass 1's inserted
`only` reached all three design notes and all three summaries.

**Quote audit: 291 delimited quotations across all 48 files of the lane; 289
resolve whole as contiguous substrings; 2 unresolved and both are our own
`[...]`-labelled notes set as blockquotes, not quotations. Zero splices.** The
discriminator pass 2 added is a **named-relaxation channel**: any fragment that
did not resolve whole was retried under four named relaxations — terminal
punctuation swapped, a hyphenation break healed, a line break healed into one
token, case folded — so the defect class would be *reported* rather than
masked. **Zero fragments needed any relaxation.** That is the positive result:
none of the four transcription-defect classes this lane's audits were built to
catch survives anywhere in it.

> **[correction 2026-10-21, pass 3 — cross-check]** Both sentences are
> **withdrawn.** Pass 3 re-ran the audit over whole quotation spans rather than
> fragments, across all 48 files of the lane at once, and **three** fragments
> needed a named relaxation: a hyphenation heal at two sites in this record
> (`schema/typ-header.derived.cddl` and `record.yaml`, the 116/117 break — see
> the correction above) and a terminal-punctuation swap in `rfc-9597`'s
> `record.yaml`, where a §1 quotation was cut at a comma and given a full stop,
> dropping the clause that extends the scope exclusion to the header parameter.
> 310 of 313 spans resolved exactly and there were **0 splices**, so the
> discipline is sound — but "zero" was an artefact of auditing fragments, each
> of which resolved somewhere in the source. Pass 1's `only` correction was verified as
correctly applied in all six places, and pass 2 traced the word's provenance —
it is `rfc-9053`'s design notes restating the point **in their own lowercase
voice**, where `only` is legitimate, so nothing in `rfc-9053` is defective
either and the attribution was the only error.

**Id join audit: every id emitted from the three requirements tables by script,
then 456 references resolved and printed beside their requirement's own text
for reading. 0 dangling, and 0 resolving to the wrong statement.**
*[correction 2026-10-21, pass 3 — cross-check] True of this record — pass 3
re-read all 30 of its citations and all 30 name the intended statement — and
true of every **prefixed** `record#R-NNNN` reference in the lane. NOT true
lane-wide of **bare** `R-NNNN` references, which `bin/check-id-joins` does not
collect: pass 3 found 3 bare citations in `rfc-9597` naming the wrong
requirement (its duplication MUST filed as R-0020 where R-0019 is the
duplication MUST, and the two placement rules filed as R-0021/R-0022 where
R-0022 is the any-COSE-object MAY), and 1 in `rfc-8392`'s `vectors.yaml`
pointing at the wrong test vector. This record has no bare-id exposure and no
cross-record requirement citations at all, so the attack surface here is
structurally empty — which is why the lane-wide figure, not this record's, was
the wrong one to assert.* The sibling
lane's 30 wrong-but-resolvable ids came from one record's layout being in
working memory and another's not, so pass 2 also flagged every **bare**
reference whose number exists in a sibling record — 70 of them — and checked
each in context. All 70 are inside their own record's files, where the bare form
correctly means the owning record.

**YAML reader audit: all 17 YAML artifacts in the lane parsed with both
`bin/_record_yaml.py` and `bin/_yaml.py`, flattened to leaf paths, and compared
value by value — 2918 leaf paths, 0 key-set mismatches.** The detector was
proved non-blind on synthetic positive controls first, because a clean result
from an untested detector is worthless. **No inline flow map exists anywhere in
the lane** and **no wrapped flow collection remains**: all 27 flow collections
are empty `[]` and close on their own line. The 178 remaining value differences
are all `int`/`bool` versus `str` typing — a difference between the two readers,
not a mangling of our data.
