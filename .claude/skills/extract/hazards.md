# FX-1 hazards — the defects that actually happen

Every item here was found in this library's own artifacts, most of them more
than once. None is hypothetical. They are ordered by how expensive they are to
miss, not by how interesting they are.

The pattern across all of them: **the defect is in OUR wording, not the
source's**, and `bin/validate` reported nothing. A source defect is usually
visible on a careful first read. What survives pass 1 is the extraction's own
confident prose, and that is what a later engineer builds on without
re-checking.

Measured during library#39 Tier 2: **every one of six independent cross-check
passes found at least one claim that pass 2 had corrected in one artifact and
failed to propagate to the others stating the same claim.** Six for six. That
is the specific thing an artifact-wide third pass buys.

The sixth is the sharpest: pass 2 of `rfc-9596` verified an octet count by
encoding, propagated it to **five** sites, and left it wrong in `messages.yaml`
— **the one artifact the measurement describes.** In the same lane, `rfc-8392`'s
claim-key bound had reached 3 of 6 sites, and `rfc-9597`'s placement ambiguity
was recorded in exactly the three files that do **not** state the placement
rule, while the four asserting it as settled said nothing. Work outward from the
corrected claim to every artifact that states it, including `summary.md`.

---

## 1. Fabricated digests and dates

Two digests were written into summary tables from invention rather than read.
Both were caught by a later pass; `bin/validate` now checks the
`| **Digest** |` row because of it.

**Rule.** Copy the digest from `content.sha256` in the record's own
`record.yaml`, then verify it three ways: against `record.yaml`, against a
fresh `shasum -a 256` of the cached source, and against the `retrieved` date.
Every bibliographic cell — authors, date, maturity, identifiers — comes from
`record.yaml` or the source's own front page. `maturity` especially: an RFC
being an RFC does not make it Standards Track. Two maturity values were wrong
in briefs this effort (`rfc-9054` is Informational; `rfc-9338` is STD 96).

## 2. Spliced and healed quotations

The two recurring verbatim defects:

- **Splice** — two non-adjacent quotes welded into one, inside a paragraph
  asserting "verified verbatim". Found in vCon (2026-09) and again in
  `rfc-9679`.
- **Heal** — a line-break hyphenation silently joined, so the quoted token
  does not occur in the source at all.

**Rule.** Build a quote audit over every file the pass writes, with a **named
relaxation channel**: retry each non-resolving fragment under
terminal-punctuation swap, hyphenation heal, line-break heal and case fold, so
the defect class is *reported* rather than masked. Then, for anything still
unresolved, take the longest matching prefix and test whether the remainder
matches **elsewhere in the source** — that is the splice signature.

Zero relaxations needed is the result you want. Four separate lanes each found
4–5 defects in their own prose this way, including an inserted `only`, an
ellipsis splice, a terminal colon turned into a full stop, and five nested
quotation marks silently re-punctuated.

### Grade WHOLE SPANS, longest first — a fragment audit reports a false clean

The CWT envelope lane's passes 1 and 2 each ran the audit above and each
reported **zero** quotation defects. Pass 3 re-ran it over **whole quotation
spans** instead of fragments and found **three** relaxations in the same files.

The reason is specific and it will happen again. `rfc-9596` quotes §2 and
spells a registry name `CoAP Content-Formats`. §2 breaks that name across lines
**at the hyphen**, so §2 reads `Content- Formats` — but the unhyphenated
spelling **is** a genuine contiguous substring of the same document, at §1's
break, which cuts at a **space**. A per-fragment audit resolves the healed token
against §1 and reports success. Only the whole §2 sentence, tested as one span,
exposes the weld. Splices hide the same way: each half resolves *somewhere*.

That record had declared three times that it heals no break, and its README
concluded *"no artifact healed anything."* It was healed in two artifacts.

**Rule.** Take every span between two quote marks as a candidate, **longest
first**, so a sentence containing nested quotes is tested whole rather than as
pieces. Resolve each against the source the span is *attributed to* — a
quotation marked §2 must resolve inside §2, not merely somewhere in the file.

### Two blind spots that are invisible by construction

- **Undelimited quotations.** Every audit extracts *delimited* quotations, so a
  verbatim span pasted into our own prose **with its quote marks lost** cannot
  be found by one. `rfc-9596` carried a span of its §1.1 BCP 14 recital that
  way, with a full stop added and a sentence fragment left behind it, through
  two passes. Sweep for our prose that *reads* like the source: long
  undelimited runs that resolve verbatim are the signature.
- **Whole-scalar quotations in YAML.** A scalar whose *entire value* is a
  quotation has no quote marks left after unescaping, so the delimited-span pass
  cannot see it. That is where `guard:` and `action:` values live, and it is
  where a paraphrase presented as a quotation was found (`"for creating the
  object"`, which occurs **zero** times in RFC 8392 — each of §7.1 step 4's
  three bullets names its own structure). Run a **separate whole-scalar pass**.

### Distrust every blanket claim

*"Never elided"*, *"nothing healed"*, *"zero relaxations needed"*, *"0 resolving
to the wrong statement"* — all four were asserted in this lane and all four were
false. A blanket claim is worse than the narrower truth, because it stops the
next reader checking. State the rule you actually keep: *an elision is visible
as `...` and the full sentence is carried verbatim in `requirements.yaml`.*

**Characterise breaks correctly, too.** One record claimed a break cut "hyphen
and all" when it cut at a space with the hyphen intact — wrong in eight places
while the data was right everywhere. Joining at a space is ordinary
normalisation, not a heal.

## 3. Escapes resolve through editing paths

Writing a literal escape sequence (`\u{6f}`, `\n`) through an ordinary edit can
silently resolve it to the character it denotes. The sentence quoting "the
escape" then becomes false, because the *character* and the *escape* are
exactly what the claim distinguishes.

`rfc-9682` carried this **seven times across six artifacts**, every one inside a
sentence *about* the hazard, and the correction hit the same trap three more
times. The Edit tool itself has refused such a change, reporting that it "also
tried swapping \uXXXX escapes and their characters".

**Rule.** Assemble any string containing an escape sequence in a script
(`chr(92)`), write the file from there, and afterwards grep the record for the
resolved characters expecting **zero** hits outside a verbatim capture. Treat
disagreement between two artifacts about the same quoted token as evidence of
this, not as a judgement call.

## 4. Ids that resolve to the wrong statement

The worst class, because nothing catches it. A `constrained_by` or `Derived
from` citation that resolves to a **real requirement which is not the one
meant**: it does not dangle, so no closure check sees it; the text is verbatim,
so no verbatim check sees it; the locator is right, so `bin/check-locators`
passes it.

Two lanes shipped **41 of these** between them — 30 in one record's
`messages.yaml`, then 11 more in the files that pass never audited
(`normative.md`, `requirements.yaml`'s own header fields, `schema/`). Two cited
ids whose text was **byte-identical** to the intended one. One cluster of five
ranges off by fifteen.

Cause, and it is specific to batched lanes: one record's id layout is in
working memory and the other's is not, so the second record's ids get written
against the first record's shape.

**Rule.** Emit every cited id **from the id table by script**, never typed or
pattern-matched, with a selector that raises on zero or multiple matches rather
than guessing. Then run a **join audit**: resolve each id to its own
requirement's text, print the pairs, and read them. Only reading the resolved
sentence catches this.

`bin/check-id-joins --surface` gives you the attack surface: requirements
sharing **identical text** are the only place a wrong id can still match the
quoted words. `rfc-9277` has exactly two such groups and both were mis-joined;
its sibling has zero, which is structurally why that record was clean at 0 of
243 citations.

## 5. Locators nobody checked

A text can be perfectly verbatim and filed under the wrong section. Until
`bin/check-locators` existed, three separate passes had named this gap and none
had closed it; `rfc-9165` had a ten-production range off by five sections and
`rfc-9682` a locator naming one line of a three-line rule, both caught by eye.

**Rule.** Run `bin/check-locators` as you go, not once at the end. It also
resolves bare sub-appendix headings (`A.2.1.  …`), which an RFC prints without
the literal `Appendix` prefix — a gap that left 83 locators unchecked
library-wide.

## 6. The library's two YAML readers disagree

`bin/_yaml.py` (used by `bin/validate`) and `bin/_record_yaml.py` (used by
`bin/ingest`, `bin/fetch-source`, `bin/_record_html`, `bin/check-locators`,
`bin/check-id-joins`) are independent subset parsers. Which one a tool uses
changes what the record says.

Five data-loss defects were fixed in `_yaml.py` during library#39, all the same
shape — validate saw wrong data and reported nothing:

1. A **wrapped quoted scalar** truncated, keeping its opening quote **and
   minting a new map key from the remainder** (71 sites).
2. A **wrapped flow sequence** truncated at its first line.
3. An **inline flow map** stored as a single string key (4331 lines).
4. A **flow sequence** returning bracket text where the other reader returns a
   list (14,069 sites).
5. A **block sequence at the same indent as its key** lost **entirely** by both
   readers — three `requirements.yaml` files whose whole list was invisible to
   every tool in `bin/`.

6. **Double-quoted escape sequences**, in **both** readers and in opposite
   directions. `_yaml.py` processed none of them, so an escaped quote kept its
   backslash; `_record_yaml.py` resolved four with **chained `str.replace()`**,
   which rescans text it has already produced, so an escaped backslash followed
   by `n` came out as a backslash and a real **newline**. 435 values in 65 files
   across 46 records read differently under the two, **72 of them verbatim
   `text:` fields**. Fixed 2026-10-21 with one left-to-right pass in each
   reader, resolving a deliberately short table: a quote and a backslash
   (unambiguous — a double-quoted scalar cannot carry either bare) plus `n` and
   `t`. **Everything else is left exactly as written**, because the records that
   use the other forms are *about* escape notation: 107 sites carry EDN literals
   in the brace form YAML does not define, and `rfc-9804` prose names hex
   escapes. Resolving those would rewrite the records discussing escaping.

`rfc-8392` also shipped a protocol model and a state machine that
`_record_yaml.py` could not parse **at all**, while `bin/validate` was silent
because it only checked that the path exists.

**Rule.** Prefer **block** sequences and maps over flow for anything a record
writes. Keep each `text:` on one line or in a block scalar. Avoid unescaped
inner quotes. Then parse every artifact with **both** readers, flatten to leaf
paths, and compare **values, not counts** — one lane found 358 keys present
under one reader and absent under the other, and the key counts matched, which
is what hid it. `bin/validate` now warns when an artifact cannot be read by
both. Roughly 580 of 750 record YAML files still differ; see the open task.

### And fixing a reader FALSIFIES the counts measured with it

The consequence nobody anticipated, and the reason this section is not just
about data loss. `rfc-8392`'s `record.yaml` claimed **24** requirement ids wired
into its protocol model and **15** into its state machine. The artifacts hold
**38** and **19**.

Neither number was invented. Running the **pass-1-era `bin/_yaml.py`** (the blob
at `d85093d`) over the **pass-1 artifacts** returns exactly 24 and 15, because
that version truncated those files' wrapped flow sequences. Pass 2 fixed the
reader *and* the artifacts, and never carried the numbers back.

So they were **true measurements through a broken instrument**, and repairing
the instrument made them false retroactively. Nothing reports this:
`bin/validate` checks that an artifact exists and parses, never that a coverage
sentence still describes it. It is the one defect class in this document that a
*correct* earlier pass can create.

**Rule.** Treat any count measured before the `_yaml.py` fixes of library#39
(`9511f10` for wrapped scalars, `725439a` for double-quoted escapes) as
unverified until recomputed. The check is cheap and worth running library-wide:
recount cited ids per artifact by script and compare against the coverage prose.
When you fix a parser, **grep the records for every number that parser
produced** before closing the pass. And prefer to state a count *with the method
that produced it*, so a later pass can tell a fossil from a lie.

**Measured, 2026-10-21 — and it over-reported exactly as #7 says.** Run over
every record declaring FX-1 artifacts, the check flagged **9** mismatches, then
**5**, then **0** as it was scoped. All of them were the checker's fault, and
the three scoping traps are worth inheriting:

- **"7 of 21 requirements cited" states the CITED count as 7.** A pattern that
  matches a bare number before `requirements` grabs the 21 as well. The idiom
  also appears as `222 of the 251 requirement ids` and `74 of the 129` — note
  the `the`, which defeats a naive `(?<!of )` guard.
- **A count may be scoped to one section, not the file.** `rfc-9682` says "all
  35 requirement ids *the reconciliation* cites"; the file as a whole cites 87.
  Both are right.
- **Count the key the claim names.** `rfc-9943` says "80 `constrained_by` links
  to 54 requirement ids" and that is exact; a file-wide regex returns 55,
  because one id also appears under a `requirements:` key and in prose.
  `rfc-9580`'s "413 of 421 wired, 8 not wired with a reason" likewise cites all
  421, since the 8 are named where they are excused.

**[corrected hours later, 2026-10-21]** That measurement concluded *"the fossil
class is confined to the two counts in `rfc-8392`."* **It is not**, and the
sentence was over-narrow in a way worth dissecting: it was true only of the
pattern the script matched — *requirement ids cited per artifact* — and was
written as though it were true of counts in general. The next record
cross-checked, `rfc-8742`, carried **four** fossils, none of which that script
could see: normative spans claimed 63 where 65 bullets exist, a reconciliation
claiming 3536 characters where it holds 4462, "243 citations" where the tool
resolves 354, and an anchored-sentence count of 8 where 9 is measured.

**And the cause is broader than a parser fix.** Two of those four were created
by **pass 2 itself**: it added two bullets to `normative.md` without updating
the sentence that counts them, and appended its own correction to the
`reconciliation` field without updating the character count of that field. No
reader bug was involved. **Any pass that edits an artifact falsifies every
count of that artifact it does not also update** — which makes this a general
obligation of editing, not a one-off consequence of `9511f10`.

**The same two shapes then recurred in the sibling record**, `rfc-9277`, which
carried eight more: a `reconciliation` claiming 3367 characters where it holds
3858 (pass 2 appended 491 characters of correction and carried neither number
back — *the identical defect, in the identical field, in both records of one
lane*), "195 verbatim spans" where pass 2's own six added bullets make 201,
"4 verbatim and 3 derived" schema files where it is 3 and 4, a word-break
census of 14 where 15 exist, a sub-breakdown counted on the raw text when the
claim was about the normalised text, and a `bin/check-locators` figure that
moved when `cff7503` taught the tool sub-appendix resolution **during this very
lane**.

Two generalisations worth carrying, then:

- **Appending a correction to a field invalidates any count of that field.**
  It happened twice, in the same field name, in two records, by the same pass.
  If you append, recount — and prefer to state the count *outside* the text it
  measures, or not at all.
- **A count can be falsified by a tool improvement, not just a tool bug.**
  Giving `check-locators` sub-appendix resolution was a strict improvement and
  it still broke a recorded figure. Any number produced by a `bin/` tool is
  only true of that tool's behaviour on that day.

So the rule is wider than the subsection title: **recount everything the prose
asserts about an artifact you touched, not just ids, and not just after a
parser fix.** Spans, bullets, characters, citations, distinct-sentence counts
and byte lengths are all fossils waiting to happen, and a count stated in a
*different* file from the artifact it describes is the likeliest to be missed.
Scope each recount to the key the prose names, as above.

## 7. Small traps that cost real time

- **`splitlines()` splits on form feeds.** Use `split("\n")`. On a paginated
  RFC it shifts every line number by up to the number of page breaks.
- **The shared scratch directory has a poisoned `__pycache__`.** One agent got
  a wrong reader-diff result from a stale `.pyc`. Run everything with
  `python3 -I` and insert `bin/` on the path explicitly.
- **A digest check alone passes a retyped block.** Verify the printed region
  byte-for-byte against its declared line range as well as checking its sha256.
- **Region digests** are `sha256` of the region's lines joined by `\n`, with
  **no trailing newline** — proven to be the only convention that fits.
- **The first version of any new check over-reports.** Three for three: the
  digest check first flagged 16 records, mostly IANA summaries quoting
  superseded digests in prose on purpose; the id-collision check flagged a
  record's own paragraph *about* wrapped ids; the locator check reported 44
  misfilings that were all `str.find` returning the earliest of several
  occurrences. **Measure across the library before trusting a check, and scope
  it narrowly.**

---

## Batching, calibrated

Measured on real lanes. Batching three records cost **539k tokens against
~280k for a single-record pass** — about a 36% saving, not the 67% a naive
count suggests.

**Batch only a genuine dependency chain**, where the cross-record evidence is
the main product and is otherwise unobtainable. Writing a CBOR/ECDSA/HMAC/CCM
stack once for `rfc-8392` upgraded a central claim in *both* sibling records
from "RFC 9052 §4.4 says so" to "here is a signature that verifies without it";
three separate agents would each have had to redo it or cite a sibling's
unverified pass-1 output, which FX-1 forbids. Likewise, `rfc-9360` cites
`rfc-9054` twice as a draft while `rfc-9054` cites `rfc-9360` zero times in 614
lines — **the finding is the asymmetry**, and it is invisible from either side.

**Do not batch unrelated records.** There is no shared product, so you pay the
propagation risk and a thinner per-record budget for nothing but attention
divided by three.

The sign of the trade-off **flips by pass**, which is the non-obvious result:

| pass | batching helps | batching hurts |
|---|---|---|
| **extract** | the analysis — holding several sources at once is where cross-record findings come from | the **bookkeeping** — a shared wrong quotation propagates lane-wide, and id layouts get crossed |
| **verify** | the **bookkeeping** — verification *is* comparison and comparison needs a corpus; one record's clean invariants become tests against the other | barely touches the analysis — each check anchors to one source, and the analytical findings come from *leaving* the lane |

Two consequences to apply either way:

- **Run the quote audit lane-wide, never per record.** A per-record audit
  resolves a shared wrong quotation against the sibling's copy of it and
  reports success. One inserted word reached all three design notes *and* all
  three summaries; a per-record audit would have fixed one of three and never
  suspected a pattern.
- **A batched verifier should also check the records against *each other*** for
  conventions that should match and do not. That is how a wrong cross-record
  locator appearing in two records was recognised as a copied error rather than
  a typo, and how the `option 5` gloss was found to have split into two
  incompatible wordings across the library.

## What a verify pass should actually attack

Pass 1's self-nominated priorities were almost all clean. **Every serious
defect a verify pass found was in something pass 1 did not nominate** — two
unparseable artifacts, a false "both readers parse every file" claim, a
line-break characterisation wrong in eight places, a cross-record locator wrong
in two records, an ambiguous MUST absent from the defect list.

Pass 1's attention map is accurate about its own uncertainty and silent about
its blind spots. Work the predecessor's list **and** choose your own targets.
