---
record: draft-ietf-cbor-cddl-modules
kind: index
title: "draft-ietf-cbor-cddl-modules — distilled artifacts"
extracted: "2026-10-19"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

**State: passes 1 and 2 of 3 complete (extract, verify). No `profile` is
declared** — this record claims `distillation.standard: FX-1` and records both
passes; the cross-check pass is not done, so there is no numerator yet
(`docs/extraction.md`: "An *unfinished* extraction is neither `full` nor
`partial`: it has no profile yet"). **No `reviewed_by` is signed.**

Pass 2 (verify, 2026-10-20) re-derived the record's four sharpest claims from
the cached source alone, without reading pass 1's reasoning first: the `id`
character classes and all seven directive instances (defect 1), rule-name
closure over all seven composed outputs against the prelude capture (defect 2),
the 13 page frames, and the semicolon sweep. **All four hold.** It corrected
**six** things pass 1 got wrong — all of them pointers and counts, none of them
a finding — and they are marked *corrected in pass 2* where they sit:
`examples/README.md`'s `incomplete` list named `V-0008` for `V-0009`;
`normative.md` pointed at `R-0073`–`R-0082` for the ten productions instead of
`R-0078`–`R-0087`; G-01 cited line numbers in another record's file that had
drifted; G-18's headline said a name was "never defined" when the document
defines it; and the protocol vocabulary sweep below was miscounted and one of
its attributions was wrong. It also **narrowed the `CRLF` framing** (defect 4)
and **closed the open question** this file previously said the record could not
answer (bottom of this file).

Source: `draft-ietf-cbor-cddl-modules-07`, *CDDL Module Structure*, Bormann &
Moran, **2 September 2026**, Intended status: Standards Track, **Expires 6 March
2027**. sha256 `7cf825aaad43d3d4995bcd540d3865ee3f69dd3dd453be5761a02c009458a644`,
784 lines, 26 KB.

**Read this before using anything here.** `bin/bcp14-count` reports **0** BCP 14
keyword occurrences. The document *recites* the full BCP 14 boilerplate in §1.1
and then never exercises it: those eleven keywords are the only all-capitals
occurrences in the file. That is not a thin document — **its normativity is
carried by a grammar (Appendix A, ten productions) and by composition rules
stated as definitions**, which is why **all 92** requirements here are
`kind: inferred`, each naming the phrase or production that carries the force.
Only **five** sentences in the whole document put a force word on an actor, and
all five are lower case (`may provide` ×2 in §2.7; `need to ascertain`,
`needs to`, `need to be particularly careful`, `should strive` in §3). §1.1's
boilerplate is deliberately never quoted: `bin/validate` counts texts with
stripping off, so quoting it would add eleven phantom keywords.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | **89 verbatim bullet quotes** and **18 reproduced blocks** (every printed block except Appendix A's grammar, which lives in `schema/` instead — so `examples/` has 19 vectors where this file has 18 blocks) across **20 distinct locators** (front matter, title block, Status of This Memo, About This Document, §1, §1.1, §2, §2.1–§2.7 including the two unnumbered sub-headings of §2.6, §3, §4, Appendix A, Appendix B). All 89 confirmed contiguous substrings of the whitespace-normalised source and all 18 blocks confirmed present in it; **0 failures**. Includes a *What the document does not say* section with the mechanical counts behind each absence |
| requirements | `requirements.yaml` | **92 entries**, `R-0001`–`R-0092`, source order, **no gaps**: **0 stated, 92 inferred** — there is no all-capitals keyword in the document to make a `stated` entry with. `source_keyword_count` and `extracted_keyword_count` both **0**, with a **7 142-character** `reconciliation` stating what was counted instead: every ABNF production, every definition of the mechanism, the RFC 8610 baseline it measures itself against, every explicit disclaimer of capability, every compatibility claim, the one prefixing side condition, and the document-status statements that bind anyone citing an Internet-Draft. `R-0078`–`R-0087` are the ten productions, one entry each |
| schema | `schema/` | **1 verbatim, 4 derived.** Appendix A's complete grammar (ten productions, source lines 677–688, **one unbroken region**) byte-identical to the cache with the margin intact, region sha256 `43c17148…96ab`, plus a margin-removed companion that **round-trips exactly in both directions**. Derived: **21 enumerated gaps** G-01…G-21 (S 10, I 1, N 8, plus 2 recorded as *not* defects), the naming-and-resolution model as data, and the two RFC 8792-wrapped outputs unfolded. See `schema/README.md` |
| messages | `messages.yaml` | **13 constructs, 41 fields**, plus a 5-entry `absent_constructs` block with the grep counts. `constrained_by` **is** used throughout — unlike `rfc-8610`, where it is omitted — because every construct here has at least one requirement with a precise locator; the header states that all such ids are `inferred` and that the key means "this is the text that fixes this field", not "this is an obligation" |
| examples | `examples/` | **19 vectors**, `V-0001`–`V-0019`, every block the document prints, source order, no gaps. **9 valid · 2 invalid · 4 incomplete · 4 not-applicable.** Every `text:` block lifted by line range **by script, never retyped**, with the round trip asserted through **both** of this library's YAML readers: 0 failures, including the 63-space continuation of the two RFC 8792 `\` wraps. **No negative was invented** — the two `invalid` and the one unintended `incomplete` are the document contradicting itself. See `examples/README.md` |
| design-notes | `design-notes.md` | the two questions `library#39` sent this record to settle, answered first and with ids; whether `/=` ordering survives composition; what we adopt, adapt and reject; **five named cuts against MD-3**, one of which goes **in option 5's favour**; the cost of a two-draft-deep unstable reference; a checked list of what this does **not** invalidate in `rfc-8610`'s `profile: full` artifacts, plus the one refinement; and nine open questions |

## Not applicable

- **protocol** — `protocol.yaml` and `protocol.md` are absent. There are no
  roles, no messages exchanged and no error paths. §2.3 makes the whole
  mechanism a **transformation of one file**: "A single CDDL file becomes a
  _module_ by processing the (zero or more) directives in it" (`R-0030`), whose
  result is "the following CDDL 1.0 specification" (`R-0050`). The only
  multi-party content is §3, and it is about **provenance of source code in a
  build environment**, not an exchange: "Implementations that employ the module
  structure defined in this document need to ascertain the provenance of the
  modules they combine into the CDDL models they employ operationally"
  (`R-0071`). §4 is "This document has no IANA actions" (`R-0076`), so there is
  not even a registration process to model. **Checked by vocabulary sweep over
  the source**, not asserted, and **re-run in pass 2**: of **nineteen** exchange
  words, **sixteen do not occur at all** — `respon`, `send`, `receiv`,
  `client`, `server`, `peer`, `party`, `parties`, `endpoint`, `handshake`,
  `negotiat`, `message`, **`protocol`**, `transmit`, `reply`, `session`. The
  three that do hit are not exchanges: `request` ×1 is "The import statement can
  also request an alias" (line 437); `sent` ×7 is a substring every time —
  **six** inside "present" and the seventh inside "Representation", in RFC
  8610's title in the normative reference list (line 592); and `acknowledg` ×3
  is the table-of-contents entry (line 108), the section heading (line 711) and
  its placeholder (line 713). **The word "protocol" does not appear in this
  document.** *[corrected in pass 2: this read "of twenty exchange words,
  seventeen do not occur" while naming sixteen, and claimed all seven `sent`
  hits were inside "present".]*
- **state-machine** — `state-machine.yaml` is absent, for the same reason.
  Nothing in the document registers, issues, rotates, revokes or expires
  anything. The nearest thing to a procedure is **module name resolution**, and
  it is a name lookup over a search path, with no states and no transitions —
  and the specification declines to define even that: "The exact way how these
  source directories and possibly a precedence between them are established is
  intentionally not fully defined in this specification" (`R-0036`). Its
  structure is held as data in `schema/name-resolution.derived.yaml` instead,
  which is the honest shape for it. **Checked by the same sweep**, re-run in
  pass 2 and confirmed exactly: of seventeen lifecycle words, **thirteen do not
  occur** — `register`, `registr`, `issuanc`, `revoke`, `revocat`, `rotate`,
  `rotation`, `expiry`, `expiration`, `renew`, `transition`, `lifecycle`,
  `enroll`. The four that hit are all furniture: `expire` ×16 is the title
  block's "Expires: 6 March 2027" (line 8), the expiry sentence (line 71) and
  the running footer on all fourteen pages; `issue` ×1 is the sentence
  introducing the GitHub issue tracker (line 43, the URL itself is on line 44);
  `state` ×1 is inside "statement" (line 437); and `provision` ×3 is the BCP
  78/79 and Trust Legal Provisions boilerplate (lines 49, 79, 84). *[the
  `expire` and `issue` attributions were tightened in pass 2; the counts were
  already right.]*

## Source defects — reported, never repaired

Each is in the bytes `content.sha256` pins. The first two are the consequential
ones and both are mechanically demonstrable.

1. **Appendix A's `id` cannot match the dotted selectors the document's own
   examples write.** `id` admits neither `-` nor `.` (`R-0082`), where RFC
   8610's `id = EALPHA *(*("-" / ".") (EALPHA / DIGIT))` admits both. So
   `;# include cose.label, cose.values from rfc9052 as cose` (line 388) and
   `;# import cose.empty_or_serialized_map from rfc9052 as cose` (line 414) —
   **two of the seven directive instances the document prints**, carrying three
   dotted selectors — are **not derivable from `directive`**. The same
   restriction bars any rule name containing a hyphen. `schema/grammar-gaps.derived.txt`
   G-01; `examples/vectors.yaml` V-0008, V-0010.
2. **The document's only demonstration of `include` with an `as` clause
   produces a model that does not resolve.** The output at lines 399–401
   (`V-0009`) defines `mydata`, `cose.label` and `cose.values`, while `mydata`
   references `label` and `values` — defined nowhere in the block and **not**
   among the 40 names of the RFC 8610 prelude. Checked mechanically against
   this library's verbatim prelude capture; **the other six composed outputs
   are all closed.** The cause is visible in the input (line 387): the module
   file still names the unprefixed rules where the corresponding line in the
   §2.5 example *was* updated to the prefixed spelling. The document
   nonetheless introduces the output with "Again, only exactly the rules
   mentioned are included" (`R-0058`). `examples/README.md` has the derivation.
3. **The prose and the grammar disagree on what makes a line a directive.**
   §2.3 requires only that a line "start with the prefix ;#" (`R-0033`);
   `directive` requires whitespace after it (`R-0078`, `R-0084`). So
   `;#import rfc9052` is a directive under one and not the other — and a plain
   comment beginning `;#` is a directive under the prose and ungrammatical
   under the appendix, with nothing saying whether a processor then errors or
   falls back to reading the comment it also is. That choice **is** the
   compatibility story and it is not made. G-03.
4. **`CRLF` is redefined against its own metalanguage, and the redefinition is
   *undeclared*.** Appendix A declares STD 68 (`R-0077`), whose core rule is
   `CRLF = CR LF`, then defines `CRLF = %x0A / %x0D.0A` (`R-0087`), admitting a
   bare LF. **The substance is not the defect.** RFC 9165 §3 makes the
   byte-identical redefinition, *declares* it and scopes it exactly — "As is
   customary for ABNF, the syntax of ABNF itself (_not_ the syntax expressed in
   ABNF!) is relaxed to allow a single line feed as a newline"
   (`rfc-9165#R-0053`) — so relaxing ABNF's own newline is deliberate community
   practice, written by one of RFC 8610's own authors. What is defective **here**
   is only that this appendix does it **silently**: it names its metalanguage
   and then overrides one of that metalanguage's core rules with no sentence of
   any kind. That is a **documentation** defect, not a grammar defect, and it is
   `rfc-8610` defect 7 in the narrowed form that record now carries — where it
   hides among identical redefinitions of `ALPHA`, `DIGIT`, `HEXDIG` and `SP`,
   whereas here `SP = %x20` is the only other core rule touched and it keeps its
   value, so the one conflicting redefinition stands alone and still unremarked.
   G-02. *[framing narrowed in pass 2 to match the 2026-10-19 narrowing in
   `records/ietf/rfc-8610/distilled/schema/cddl.abnf`; this bullet previously
   said "the defect is now in two current CDDL documents", which counted a
   declared instance and an undeclared one as the same thing.]*
5. **A rendering defect in a load-bearing character.** Source line 522 reads
   "(no – was given on the command line)" with **U+2013 EN DASH**, where the
   sense requires the ASCII `-` that every other example uses as the stdin
   argument (`R-0069`). Reproduced in our quotes, not repaired.
6. **`$.start.$` occurs once, as a definition, and the convention behind it is
   never introduced.** Line 509 (`R-0068`) assigns it. It is a valid RFC 8610
   `id`, and it is spelled like an RFC 8610 §3.9 **type socket** (leading `$`)
   yet defined with `=` where §3.9 extends sockets with `/=`. No sentence
   introduces the convention or says whether the name is reserved. G-18.
   *[headline corrected in pass 2: it read "used once and never defined", which
   is false at face value — line 509 is its definition.]*
7. **A parenthetical that opens in one sentence and closes in the next.** §2
   lines 187–191: "(as was emulated with snippets in Section 11 of [RFC8428]."
   … "based on Section 4 of [RFC9165])." The parenthesis is balanced only
   across the sentence boundary and encloses a full stop (`R-0019`, `R-0020`).
8. **Acknowledgments is an unresolved placeholder in revision -07.** Source
   line 713 is the standard all-capitals four-letter placeholder token followed
   by the word `acknowledge`. **It is not quoted anywhere in this record**, and
   deliberately so: `bin/validate` rejects that token as a literal string in any
   file under `distilled/` (`docs/extraction.md`, *Definition of done*), so
   quoting it would make the record unmergeable. Recorded this way instead.
9. **Tool-interface inconsistency.** All seven examples in §2.5–§2.7 write the
   conversion flags as one argument, `cddlc -2tcddl -`; Appendix B writes them
   as two, `cddlc -2 -tcddl` (line 701, `R-0090`). Appendix B is declared "for
   information only" (`R-0088`), so neither spelling is normative. G-20.
10. **Three non-ASCII code points inside quoted spans**, reproduced as the
    source bytes carry them and never normalised: U+2019 in `cddlc’s`
    (line 276, `R-0043`), U+2013 as defect 5 (line 522), and U+2265 in
    "Ruby version ≥ 3.0" (line 704, `R-0091`).
11. **Editorial, recorded because our quotes carry them.** §2.1's "by carrying
    them in _directives_" has no antecedent for "them" — the subject
    "super-syntax" is singular (`R-0022`). §2.3 joins two independent clauses
    with a comma splice, "independent of the module(s) using it, however,
    importing a module may involve" (`R-0031`). §2.4 opens "The exact way how"
    (`R-0036`).

## Verification run for this pass

Mechanical, re-runnable, and the numbers in this file are these numbers:

- **Quote fidelity.** 89 of 89 bullet quotes in `normative.md` and 92 of 92
  requirement texts are contiguous substrings of the whitespace-normalised
  source. 18 of 18 fenced blocks found in the source. **0 failures.**
  Normalisation removes exactly two classes of page decoration — the running
  footer, the running header and the 13 form feeds beside them — and then
  collapses whitespace runs.
- **Parser agreement.** `requirements.yaml` reads as **92 / 92 / 92** entries
  under `bin/_record_yaml.py`, under `bin/_yaml.py`, and as unique ids.
  `examples/vectors.yaml` reads as **19 / 19 / 19** the same way, with every
  `text:` block byte-identical to its dedented source slice under both readers.
- **Keyword count.** `bin/bcp14-count` on the cache: **0**. BCP 14 keywords
  across all 92 requirement texts, counted the way `bin/validate` counts them
  (boilerplate stripping **off**): **0**. The two agree, and the `reconciliation`
  states the document's own normative baseline as `bin/validate` requires when
  the source count is 0.
- **No span crosses a page frame.** All 13 page breaks fall in blank space, in
  the table of contents, in the reference list, or between a sentence and a
  display block; Appendix A's grammar sits in one unbroken region. **Checked,
  not assumed** — both sibling records had a load-bearing sentence severed by
  the page furniture.
- **Hyphenation declared, never healed.** Exactly **three** quoted spans carry
  a token severed at a line break, each reproducing the hyphen and the
  following space as the normalised source renders them and naming the break in
  `field`: `follow- up` (`R-0009`), `Internet- Drafts` (`R-0041`),
  `module- structured` (`R-0089`). Two look-alikes were checked and are **not**
  breaks: the suspended hyphen in `backward- and forward-compatible`
  (`R-0008`, written on one line) and the trailing `-` on every
  `$ cddlc -2tcddl -` command line (the stdin argument).
- **Verbatim capture.** Appendix A's region sha256 verified; the dedented
  companion re-indents to the original byte-for-byte; the two RFC 8792 unfolds
  each fire exactly once and leave no backslash.
- **Rule-name closure.** All seven composed outputs tested for dangling
  references against the 40 RFC 8610 prelude names: **six closed, one not**
  (defect 2).

### Re-run independently in pass 2 (verify, 2026-10-20)

Every number below was produced from `.cache/draft-ietf-cbor-cddl-modules.txt`
and this library's own captures, by scripts written for pass 2 rather than
re-run from pass 1's.

- **BCP 14, both ways.** `bin/bcp14-count` (boilerplate stripping **on**): **0**.
  Stripping **off**, the way `bin/validate` counts our texts: **11**, and all
  eleven are inside §1.1's boilerplate at lines 146–150 — deleting those five
  lines takes the unstripped count to **0** as well. The 0 is therefore exact,
  not a filter artefact. Across all 92 requirement texts, stripping off: **0**.
- **Quote fidelity and page frames, as one test.** Each span was matched against
  two normalisations of the source: one with the running header and footer
  removed, one with them left in. A span that matched the first and not the
  second would have crossed a page frame. **92/92 requirement texts, 89/89
  `normative.md` bullet quotes and 18/18 fenced blocks matched *both*, and
  19/19 `vectors.yaml` text blocks did too — 0 crossings, 0 failures.** The 13
  breaks themselves were classified mechanically: 14 footers, 13 headers, and
  every break resolving to blank space, the table of contents, the reference
  list, or a point before a display block. The one break that severs a token,
  p11, splits `draft-bormann-cbor-cddl-2-` / `draft-09` inside the reference
  list, and nothing quotes across it.
- **Appendix A is one unbroken region.** No page-furniture line and no blank
  line falls inside source lines 677–688. Region sha256 recomputed:
  `43c17148af31265a171f2e722b24d2e0063d0ab253d8b681cc1c223d5df696ab`, matching
  the claim. The verbatim capture's body is byte-identical to the source
  region; dedent and re-indent are exact inverses; the dedented file's own
  body digest matches its header; **10** productions.
- **Vectors re-lifted from scratch.** Each of the 19 `text:` blocks was lifted
  again from its own `source_lines:` and dedented: **19/19 byte-identical**,
  including the 63-space continuation of both RFC 8792 wraps. Tally confirmed:
  **9 valid · 2 invalid · 4 incomplete · 4 not-applicable**, ids `V-0001`–
  `V-0019`, no gaps.
- **Parser agreement, with one honest caveat.** Both readers return 92
  requirements and 19 vectors with identical id sequences. On block scalars they
  differ by exactly one byte: `bin/_yaml.py` keeps the trailing newline a `|`
  block clips, `bin/_record_yaml.py` chomps it. Modulo that single known reader
  difference — which is a property of the two tools and applies to every record
  in this library, not to this file — all 19 texts are identical under both.
  Stated here because "byte-identical under both readers" cannot be literally
  true of a `|` block while that difference exists.
- **Citation integrity.** Every `R-`, `V-` and `G-` id cited anywhere under
  `distilled/`, in `record.yaml` or in `summary.md` resolves: 92 R ids defined
  and all local citations found, 19 of 19 V ids, 21 of 21 G ids, **0 dangling**.
  The only unqualified-looking exceptions are `rfc-8610#R-0102` and
  `rfc-8610#R-0106`, which are cross-record and both exist in that record.
- **The six module files.** Read as basic CDDL alone, all six have at least one
  rule name that resolves to nothing (`COSE_Key`, `cose.COSE_Key`, `label` and
  `values`, `cose.empty_or_serialized_map` twice) — re-derived, not taken over.
  The prelude list printed in `examples/README.md` is **set-equal** to the 40
  names in `records/ietf/rfc-8610/distilled/schema/prelude.cddl`.
- **Counts behind the two central questions, all confirmed.** `export` 0,
  `private` 0, `visib` 0, `public` 1 (line 80, inside "publication"), `socket`
  0, `plug` 0, `$$` 0, `/=` 0, `//=` 0, `order` 1 (line 181), `precedence` 1
  (line 252), `determin` 1 (line 259), `register`/`registry` 0. Semicolons in
  all seven composed outputs: **0**.

## This record and `rfc-8610`'s gate

`rfc-8610` is at `profile: full` and both its `distilled/README.md` and its
`summary.md` carry a gate: *nothing there may be treated as the current state
of CDDL until `rfc-9165`, `rfc-9682`, `rfc-9741` and this draft are read.*
**This closes one quarter of it.** The other three are still `status: fetched`
and the gate stands until they are read. `design-notes.md` §*What this does not
invalidate in `rfc-8610`'s artifacts* lists what was checked and holds, and the
one statement of that record it **sharpens** — which it names rather than
edits, because editing another record's `profile: full` artifacts is not this
pass's work.

**The open question this file used to say the record could not answer is now
answered, and the answer makes defect 1 worse rather than better.** `R-0005`
says CDDL is defined by RFC 8610 **and RFC 9682** as well as RFC 9165 and
RFC 9741, and `rfc-9682` is "Updates to the CDDL Grammar"; if RFC 9682 changed
`id`, the severity of defect 1 would change with it. **It does not change it.**
`rfc-9682`'s own extraction landed in this library between pass 1 and pass 2 of
this record, and its production-by-production change table puts `id` among the
**forty-one productions carried into Figure 11 unaltered**
(`records/ietf/rfc-9682/distilled/schema/production-changes.derived.txt`), with
`EALPHA` beside it. So the CDDL `id` in force today still admits `-` and `.`,
and Appendix A's `id` is narrower than the *current* grammar and not merely than
the 2019 one. Defect 1 stands at full strength. `rfc-9682` also leaves `CRLF`
untouched, which is why defect 4's narrowed framing names three undeclared
instances of that redefinition and one declared one.

**One question this record still cannot answer**: the rationale for naming
modules by filename lives in `[I-D.bormann-cbor-cddl-2-draft]` and the
dereferenceable-identifier security analysis in `[I-D.bormann-t2trg-deref-id]`.
Pass 2 confirmed that **this library holds neither** — there is no record under
`records/ietf/` for either — so the namespacing argument is one hop away and
unread. `design-notes.md` open questions 6 and 7 own it.
