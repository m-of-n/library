---
record: rfc-9597
kind: index
title: "rfc-9597 — distilled artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

**State: passes 1, 2 and 3 complete. NO `profile` IS CLAIMED HERE.** Extract ran
2026-10-20 at effort max, reading only `.cache/rfc-9597.txt` — never
`summary.md` and never another record's artifacts. **Verify ran 2026-10-20 at
effort max**, by an independent agent that did not extract, over all three
records of the lane at once. **Cross-check ran 2026-10-21 at effort max** over
this record alone — see the last section. Every `reviewed_by` here is still
empty, so pass 4 (human review) is outstanding; `record.yaml` is where the
profile is declared, and `docs/extraction.md` is the standard it is declared
against.

RFC 9597 is the **middle** record of library#39 Tier 2's CWT envelope lane
(`rfc-8392` → `rfc-9597` → `rfc-9596`) and the smallest of the three: 265
lines, **8 BCP 14 keywords, all of them in §1 and §2**, and **not one printed
byte.**

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | **16 verbatim regions** covering the whole document except the references, acknowledgements and authors' addresses, each an exact run of source lines with its own `sha256`. §1 is quoted in four parts because it is **normative, not background** — half the keywords are in it. The source is an unpaginated RFC v3 rendering with **zero form feeds**, so no region removes anything |
| requirements | `requirements.yaml` | **28 entries R-0001 to R-0028, 8 `stated` and 20 `inferred`**, counts reconciling **8 = 8**, all **28** texts verified mechanically as contiguous substrings of the whitespace-normalised source (this cell read *31* until pass 3 recounted it; no artifact in this record has 31 of anything). The reconciliation states where all 8 keywords are by line number and why §3, §4 and §5 have none |
| schema | `schema/` | 1 verbatim file, 2 derived. **The document ships four lines of CDDL and declares them non-normative in the sentence immediately before them**, so the verbatim capture reproduces the declaration *and* the fragment as **one region** — separating them would leave the fragment looking normative. The derived CDDL carries what §1's and §2's normative sentences fix and the source's CDDL omits: the three conformant placements, **including the conformant-but-unsigned one** |
| messages | `messages.yaml` | 3 structures, 5 fields. `constrained_by` wired, **8 of 28 requirements cited and all eight are §2's** — 0 dangling, and the `coverage` block explains the other 20, which is the document: **three sentences bind bytes; the rest bind a reader.** Every layout is **derived** from Table 1 and RFC 9052 §3, because the document prints nothing to decode |
| protocol | `protocol.yaml`, `protocol.md` | **NOT APPLICABLE, with the measurement written out.** `protocol`, `exchange`, `sender`, `receiver`, `verifier` and `steps` each occur **zero** times; `recipients` occurs **once**, as the subject of the `MUST NOT`. The one receiver-side check has no failure action, no ordering and no counterparty |
| state-machine | `state-machine.yaml` | **NOT APPLICABLE, with the measurement written out.** `state`, `lifecycle`, `revoke`, `rotate`, `expire` and even `registration` each occur **zero** times. The file records where a lifecycle *would* have been useful: §4 describes two states of a decision — tentative and confirmed — and names neither |
| examples | `examples/README.md` | **NOT APPLICABLE, and the absence is the finding.** `example`, `examples`, `Figure`, `hex`, `vector` and `diagnostic notation` each occur **zero** times. **Every fixture for label 15 would be ours** under `R-O-03`, with nothing to cite |
| design-notes | `design-notes.md` | the protected-placement decision and the precedent to cite for it; the duplication rule's two escape hatches and its undefined *"identical"*; `R-M-12` evidence from both registries; 4 adopts, 6 adapt-or-reject items; **MD-3 mapped header by header over 8 of our fields**, then **five cuts against MD-3** — one of them **for** option 5 — each naming the option it affects; `DEC-005` stated honestly as the weakest edge; all six `canonical-encoding` conditions; the summary's seven findings tested; **6 source defects** (D-1…D-6; D-6 was added by pass 2 and this cell still read *5* until pass 3 recounted it); 5 open questions |

## The two results

**1. The document gives a conformant producer permission to emit an unsigned
`iss`.** §2 only `RECOMMENDED`s protected placement, and its one `MUST` bars
label 15 from appearing in **both** buckets — expressly permitting the
unprotected one. **This pass demonstrated the coverage boundary rather than
reading it**: `records/ietf/rfc-8392`'s extraction, in the same pass, rebuilt
`Sig_structure` from RFC 9052 §4.4 and **verified RFC 8392's A.3 signature from
exactly its four fields**, so the unprotected map is provably not an input. Our
profile must state protected-only placement and cite `rfc-9943` §6.

**2. All 8 BCP 14 keywords are in §1 and §2 — four in each — and §3, §4 and §5
have none.** So the document's most important instruction to an implementer
(§4: *"Implementers must ensure that any tentative decisions made based on
previously unverified information are confirmed once the cryptographic
processing has been completed"*) is **lower case**, in a document whose entire
purpose is to make claims readable before verification. Under §1.1's *"when, and
only when, they appear in all capitals"* it binds nobody.

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
   whole-span audit found the same break healed twice more, both in `rfc-9596`
   (`schema/typ-header.derived.cddl` and `record.yaml`). Three sites, all in
   that record. The point survives, the count was wrong.*
4. **A case change** in a quotation of our own `messages.yaml`.

The nine residuals are each accounted for: three are the **superseded summary
wordings** this pass quotes in order to record them, three are the audit
regex over-running past a closing `**` into our own following sentence, one is
the ellipsis form **deliberately preserved** inside the `[correction]` note that
identifies it, and two are our own `[...]`-labelled notes set as blockquotes.

## What pass 2 should attack hardest

1. **The 28 requirement texts and, more importantly, their `locator`s.** The
   texts were verified mechanically as contiguous substrings; **no check in this
   pass tested a locator**, and §1 spans 44 lines (source 69–112) of four very
   different paragraphs.
2. **The claim that §1 is normative.** It rests on a keyword census; recount it.
3. **The derived CDDL's three placement shapes.** They are this extraction's
   reading of one `MUST` and one `RECOMMENDED`, and `nonclaims-label = label
   .ne 15` is a construct of ours — check it against RFC 8610 §3.8 rather than
   against this file.
4. **The three `not_applicable` verdicts.** Each rests on word counts; re-run
   them, and in particular look for a role or a lifecycle hiding in §4's four
   paragraphs, which are the only prose in the document long enough to hide one.
5. **The §7.6 implementation cut**, which is the one argument here that rests on
   a search rather than on the source. It has a shelf life and should be
   re-dated, not re-asserted.

---

## What pass 2 did, and what it found (2026-10-20, independent, effort max)

**1. The 28 texts and their locators.** All 28 texts re-derived as contiguous
verbatim spans. All 28 locators checked under a **stricter** rule than
`bin/check-locators` applies — the tool permits a text that really lives in a
subsection to be filed under its parent, so pass 2 computed the **innermost**
containing section and compared. **0 misfiled, 0 imprecise, 0 unresolvable.**
That is the result that mattered most here, because §1 spans 44 lines of four
unlike paragraphs. Two terminator suspects, both legitimate: `R-0015` is a whole
Table 1 row ending at its closing rule and `R-0018` is a complete CDDL
production.

**2. §1 is normative — confirmed exactly, with the section map computed rather
than read.** §1 spans lines 69–112, §1.1 spans 113–120, §2 spans 121–160. The
eight keywords sit at **L102 `MAY`, L105 `RECOMMENDED`, L107 `MAY`, L108
`MUST NOT`** (four in §1) and **L148 `MUST`, L152 `RECOMMENDED`, L154 `MUST`,
L157 `MAY`** (four in §2). §3, §4 and §5 have **none**. So half the document's
BCP 14 force — **including its only `MUST NOT`** — is in the introduction.
Recount: 8 = 8.

**3. The derived CDDL.** `nonclaims-label = label .ne 15` was checked against
**RFC 8610 §3.8 and §3.8.6 directly**, not against the file. §3.8's syntax is
*"target .control-operator controller"*, satisfied with `15` as a controller
"containing just that single value"; §3.8.6 states *".ne and .eq are defined for
both numeric values and values of other types"* and that *"All other cases are
not equal"*, so a `tstr` target **satisfies** `.ne 15` rather than erroring, and
the production admits every text label and every integer but 15 — the intent.
**The construct is correct.** One locator corrected: `label = int / tstr` was
cited as RFC 9052 **§1.4**; it is **§1.5**. `rfc-9596` carried the same error,
which is the signature of one wrong cross-record locator copied across a lane.

**4. The three N/A sweeps are confirmed, and pass 1's work was more thorough
than this README summarised.** It had already swept `party`, `producer`,
`consumer`, `step`, `transport`, `handshake` and `negotiate`, and had already
recorded `application`/`applications` at 9 occurrences — pass 2 re-counted
exactly 9. **The §4 lifecycle hunt found what pass 1 already recorded and
nothing more**: paragraph 4's tentative-then-confirmed decision is two states of
a decision with neither named and no failure action, and `state-machine.yaml`
says so. §4's other three paragraphs name `the application` and `Implementers`
as responsible parties but never as counterparties, so the right form of the
verdict is **no two roles that address each other**, which still holds.

**5. §7.6 was re-dated, not re-asserted.** Pass 2 **deliberately did not repeat
the search**: a second unreproducible search on the same day adds a date and no
information and would make a one-source claim look corroborated. The cut now
states its own shelf life, names what would retire it, and is marked as the only
claim in the record that cannot be checked against a cached source.

**One defect added that pass 1 did not list — D-6.** §2's placement `MUST`
(*"MUST only occur once in either the protected or unprotected header"*) is
**ambiguous across three readings**, and the derived CDDL's enumeration of
exactly three conformant shapes is complete only under the first. Reading 1 is
right and the record keeps it, but it is a reading, not a statement — so this
document's **two** hard rules both turn on wording it leaves undefined:
*"identical"* in the duplication `MUST`, and in the placement one the scope of
the either/or — across the two buckets together, or within each. *[the second
read `*"either … or"*` until pass 3; an elided quotation in a record that
states it elides none.]*

**All 16 `normative.md` regions and both schema regions re-verified** — digest
**and** printed block byte-identical to the cache. **Body source-line coverage
computed**: the only uncovered lines are the six section headings, so no
statement is dropped.

**This record's headline is now demonstrated rather than cited.** Pass 2's own
independent A.3 verification succeeds on the four-field `Sig_structure` and
**fails** when the unprotected map is folded in as a fifth field, so the
unprotected bucket is provably not a signature input and a conformant producer's
unsigned `iss` is a real exposure.

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

> **[correction 2026-10-21, pass 3 — cross-check]** **Withdrawn.** Pass 3
> re-ran the audit over whole quotation spans rather than fragments, across all
> 48 files of the lane at once, and **three** fragments needed a named
> relaxation. One is in **this** record: `record.yaml`'s state-machine
> `not_applicable` reason quoted §1's scope exclusion cut at a **comma** with a
> full stop substituted, dropping *"whether they are in the COSE payload or the
> CWT Claims header parameter, or both"* — the clause that extends the exclusion
> to the very mechanism this record documents. Three sibling artifacts here
> quote it whole, so it was a single un-propagated site. The other two are
> hyphenation heals in `rfc-9596`. 310 of 313 spans resolved exactly and there
> were **0 splices**. Pass 1's `only` correction was verified as
correctly applied in all six places, and pass 2 traced the word's provenance —
it is `rfc-9053`'s design notes restating the point **in their own lowercase
voice**, where `only` is legitimate, so nothing in `rfc-9053` is defective
either and the attribution was the only error.

**Id join audit: every id emitted from the three requirements tables by script,
then 456 references resolved and printed beside their requirement's own text
for reading. 0 dangling, and 0 resolving to the wrong statement.** The sibling
lane's 30 wrong-but-resolvable ids came from one record's layout being in
working memory and another's not, so pass 2 also flagged every **bare**
reference whose number exists in a sibling record — 70 of them — and checked
each in context. All 70 are inside their own record's files, where the bare form
correctly means the owning record.

**[pass 3 amendment, 2026-10-21] That clean result holds for the 456 *prefixed*
references and does not hold for the bare ones.** `bin/check-id-joins`
deliberately collects only `record#R-NNNN`, and pass 2's bare-reference check
asked **which record** a bare number belongs to, not **which requirement** —
so a bare number naming the wrong requirement inside its own record passes
both. Pass 3 resolved every bare `R-NNNN` in this record by hand and found
**three of them wrong, in three files**: `protocol.yaml` and `protocol.md` both
filed §2's duplication `MUST` as `R-0020` (it is `R-0019`; `R-0020` is the
RECOMMENDED protected placement), and
`schema/cwt-claims-header.derived.schema.json` filed the two placement rules as
`R-0021` and `R-0022` (they are `R-0020` and `R-0021`; `R-0022` is the
any-COSE-object `MAY`). None dangled, all three resolved to real requirements,
and `record.yaml`'s own `not_applicable` reason had the duplication rule as
`R-0019` all along — the defect was the propagation, not the reading.

**YAML reader audit: all 17 YAML artifacts in the lane parsed with both
`bin/_record_yaml.py` and `bin/_yaml.py`, flattened to leaf paths, and compared
value by value — 2918 leaf paths, 0 key-set mismatches.** The detector was
proved non-blind on synthetic positive controls first, because a clean result
from an untested detector is worthless. **No inline flow map exists anywhere in
the lane** and **no wrapped flow collection remains**: all 27 flow collections
are empty `[]` and close on their own line. The 178 remaining value differences
are all `int`/`bool` versus `str` typing — a difference between the two readers,
not a mangling of our data.

---

## What pass 3 did, and what it found (2026-10-21, cross-check, effort max)

Scope: this record alone, against `.cache/rfc-9597.txt`. Every number below was
measured in this pass, not read off a previous one.

**1. The four FX-1 closure questions.**

- *Every field a requirement names exists in `messages.yaml` or `schema/`* —
  **closed, with one pointer.** The 5 fields across 3 structures carry 14
  `constrained_by` citations resolving to 8 distinct ids, exactly §2's `R-0015`
  to `R-0022`, 0 dangling. The one field named by a requirement and defined in
  neither file is `typ` (`R-0012`), RFC 9596's label 16, which belongs to
  `records/ietf/rfc-9596`; `messages.yaml`'s new `cross_check_2026_10_21` entry
  records that, and the same for `COSE_Sign`/`COSE_Sign1` (RFC 9052).
- *Every message in a protocol flow is defined in `messages.yaml`* — **vacuous
  and correctly so**: `roles`, `flows` and `error_paths` are all `[]`.
- *Every state-machine trigger is a defined message or a named event* —
  **vacuous**: `machines: []`.
- *Every example validates against the schema* — **vacuous**: no fixture
  exists, because the document prints no bytes.

**2. The three `not_applicable` verdicts, re-derived rather than trusted.** All
37 tokens the three artifacts claim at zero occur **zero** times, whole-word and
case-insensitive, over all 265 lines — including `registration`, `state`,
`example`, `Figure`, `hex`, `vector`, `Unicode`, `normalization` and
`normalisation`. The four near-misses reproduce exactly: `recipients` 1 (L108),
`request` 1 (L6), `parties` 1 (L167), `application`/`applications` 9.

**3. The census and the spans, recomputed.** 265 lines; §1 = 69–112 (44 lines),
§1.1 = 113–120, §2 = 121–160; keywords at L102, L105, L107, L108 and L148, L152,
L154, L157; the §1.1 recital would add exactly **11** phantom keywords. 8 = 8,
with the 8 carried by `R-0011`–`R-0014` and `R-0019`–`R-0022`. 28 of 28 texts
contiguous in the whitespace-normalised source; 28 of 28 locators correct under
the innermost-section rule; 16 + 2 regions byte- **and** digest-identical to the
cache; the only uncovered body lines are the six section headings.

**4. The `.ne` construct, checked from a second place.** RFC 8610 §3.8 and
§3.8.6 in `.cache/rfc-8610.txt` carry the four sentences the derived CDDL quotes,
verbatim, and `records/ietf/rfc-8610`'s own `normative.md` and
`requirements.yaml` carry the same text — so `label .ne 15` is well formed and a
`tstr` target satisfies it rather than erroring. **Confirmed.**

**5. The defects, every one in this extraction's prose and none in the source.**
Three bare ids resolving to the wrong requirement (above); `31 texts` for 28;
`§1 spans 43 lines` against this file's own 44; `§2 in six parts` for five; `5
source defects` for six and `12 quotations` for what is now 14; a
`normative.md` sentence crediting `schema/` with a `non_normative: true` marker
that exists in no file there; `use case` twice **in §1** when one of the two is
in the Abstract; `rfc-8392`'s figures as nine when the document prints 19, nine
of them in diagnostic notation; `summary.md` saying passes 2 and 3 had not run
and that `bears_on` was *not* widened, both contradicted by `record.yaml` and
by `summary.md`'s own artifacts table; the same "pass 2 has not run" sentence
inside `record.yaml`'s `distillation` comment, three keys above the `passes:`
list that records it; two §1 fragments printed as unmarked
prose with their quotation marks lost, one of them leaving an orphaned full
stop; and an **elided quotation** — `*"either … or"*` — in a file that states
three paragraphs earlier that nothing in this directory elides one.

**6. D-6 propagated.** Pass 2 found the placement `MUST`'s ambiguity and
recorded it in `design-notes.md`, this file and `record.yaml` — not in the three
places that *state* the rule. `requirements.yaml` `R-0021`, `messages.yaml`,
`schema/cwt-claims-header.derived.cddl` and `schema/README.md` now each say that
this record takes **reading 1** and that the three enumerated shapes are
complete only under it; `summary.md` says the placement reading is ours.

**7. Pass 3's own quote audit**, with a named-relaxation channel, over this
record's `.md` files **as they now stand, this section included**: 80 delimited
quotations — **59 resolve as contiguous substrings of a cached source, 13 of
another library file, 0 needed any relaxation, 0 splices.** Every fragment that
did not resolve whole was retried under four named relaxations (terminal
punctuation, hyphenation heal, line-break heal, case fold) so the defect class
would be reported rather than masked, and then tested for the splice signature
by longest matching prefix. The 8 residuals are each accounted for and none is a
quotation of a document: 2 are the pre-existing regex over-run on the nested
`"No tags"` quotation, 2 are pass 2's own `treat the sentence as ...` reading
instructions in §7.6, 1 is the ellipsis deliberately preserved inside D-4's
correction note, and 3 are pass 3's own notes quoting the wording they correct.

**8. Still unverifiable from this repository**, and now labelled wherever it is
asserted: the §7.6 implementation cut and the SCRAPI example. `python-cwt`,
`draft-ietf-scitt-scrapi` (a `stub` record) and `rfc-9942` have no `.cache/`
rendering here. `rfc-9943` §6 **is** checkable and was checked, against that
record's own artifacts.

**9. Both readers, after the edits.** All 5 YAML artifacts parse under
`bin/_yaml.py` and `bin/_record_yaml.py`: **484 leaf paths, 0 key-set
mismatches**, and the only value differences are 6 `bool`-versus-`str` typings.
`bin/validate` is clean and reports nothing for this record. One pass-3 edit was
reverted in the making: splitting `record.yaml`'s one-line `coverage` scalar
across lines made `_record_yaml.py` return the raw quoted text while `_yaml.py`
decoded it — hazard 6 reproduced on the first attempt. That value is one
physical line again.
