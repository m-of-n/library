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

**State: passes 1 and 2 of 3 complete. NO `profile` IS CLAIMED.** Extract ran
2026-10-20 at effort max, reading only `.cache/rfc-9597.txt` — never
`summary.md` and never another record's artifacts. **Verify ran 2026-10-20 at
effort max**, by an independent agent that did not extract, over all three
records of the lane at once. **Pass 3 (cross-check) has not run**, and every
`reviewed_by` here is empty: under `docs/extraction.md` an unfinished extraction
has no profile at all.

RFC 9597 is the **middle** record of library#39 Tier 2's CWT envelope lane
(`rfc-8392` → `rfc-9597` → `rfc-9596`) and the smallest of the three: 265
lines, **8 BCP 14 keywords, all of them in §1 and §2**, and **not one printed
byte.**

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | **16 verbatim regions** covering the whole document except the references, acknowledgements and authors' addresses, each an exact run of source lines with its own `sha256`. §1 is quoted in four parts because it is **normative, not background** — half the keywords are in it. The source is an unpaginated RFC v3 rendering with **zero form feeds**, so no region removes anything |
| requirements | `requirements.yaml` | **28 entries R-0001 to R-0028, 8 `stated` and 20 `inferred`**, counts reconciling **8 = 8**, all 31 texts verified mechanically as contiguous substrings of the whitespace-normalised source. The reconciliation states where all 8 keywords are by line number and why §3, §4 and §5 have none |
| schema | `schema/` | 1 verbatim file, 2 derived. **The document ships four lines of CDDL and declares them non-normative in the sentence immediately before them**, so the verbatim capture reproduces the declaration *and* the fragment as **one region** — separating them would leave the fragment looking normative. The derived CDDL carries what §1's and §2's normative sentences fix and the source's CDDL omits: the three conformant placements, **including the conformant-but-unsigned one** |
| messages | `messages.yaml` | 3 structures, 5 fields. `constrained_by` wired, **8 of 28 requirements cited and all eight are §2's** — 0 dangling, and the `coverage` block explains the other 20, which is the document: **three sentences bind bytes; the rest bind a reader.** Every layout is **derived** from Table 1 and RFC 9052 §3, because the document prints nothing to decode |
| protocol | `protocol.yaml`, `protocol.md` | **NOT APPLICABLE, with the measurement written out.** `protocol`, `exchange`, `sender`, `receiver`, `verifier` and `steps` each occur **zero** times; `recipients` occurs **once**, as the subject of the `MUST NOT`. The one receiver-side check has no failure action, no ordering and no counterparty |
| state-machine | `state-machine.yaml` | **NOT APPLICABLE, with the measurement written out.** `state`, `lifecycle`, `revoke`, `rotate`, `expire` and even `registration` each occur **zero** times. The file records where a lifecycle *would* have been useful: §4 describes two states of a decision — tentative and confirmed — and names neither |
| examples | `examples/README.md` | **NOT APPLICABLE, and the absence is the finding.** `example`, `examples`, `Figure`, `hex`, `vector` and `diagnostic notation` each occur **zero** times. **Every fixture for label 15 would be ours** under `R-O-03`, with nothing to cite |
| design-notes | `design-notes.md` | the protected-placement decision and the precedent to cite for it; the duplication rule's two escape hatches and its undefined *"identical"*; `R-M-12` evidence from both registries; 4 adopts, 6 adapt-or-reject items; **MD-3 mapped header by header over 8 of our fields**, then **five cuts against MD-3** — one of them **for** option 5 — each naming the option it affects; `DEC-005` stated honestly as the weakest edge; all six `canonical-encoding` conditions; the summary's seven findings tested; 5 source defects; 5 open questions |

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
   across lines 116/117. The one place in this lane that healed a break was in
   the record that declares three times that it does not.
4. **A case change** in a quotation of our own `messages.yaml`.

The nine residuals are each accounted for: three are the **superseded summary
wordings** this pass quotes in order to record them, three are the audit
regex over-running past a closing `**` into our own following sentence, one is
the ellipsis form **deliberately preserved** inside the `[correction]` note that
identifies it, and two are our own `[...]`-labelled notes set as blockquotes.

## What pass 2 should attack hardest

1. **The 28 requirement texts and, more importantly, their `locator`s.** The
   texts were verified mechanically as contiguous substrings; **no check in this
   pass tested a locator**, and §1 spans 43 lines of four very different
   paragraphs.
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
document's **two** hard rules both turn on a word it leaves undefined:
*"identical"* in the duplication `MUST` and *"either … or"* in the placement
one.

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
catch survives anywhere in it. Pass 1's `only` correction was verified as
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

**YAML reader audit: all 17 YAML artifacts in the lane parsed with both
`bin/_record_yaml.py` and `bin/_yaml.py`, flattened to leaf paths, and compared
value by value — 2918 leaf paths, 0 key-set mismatches.** The detector was
proved non-blind on synthetic positive controls first, because a clean result
from an untested detector is worthless. **No inline flow map exists anywhere in
the lane** and **no wrapped flow collection remains**: all 27 flow collections
are empty `[]` and close on their own line. The 178 remaining value differences
are all `int`/`bool` versus `str` typing — a difference between the two readers,
not a mangling of our data.
