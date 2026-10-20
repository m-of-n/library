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

**State: all three machine passes complete (extract, verify, cross-check), and
`distillation.profile: full` against `standard: FX-1` as of 2026-10-20.** The
artifact set is complete, every artifact kind is present or declared
not-applicable with a reason, and the cross-check pass found the set internally
consistent — see *Cross-check run (pass 3)* below for what it checked and the
five things it corrected. **Pass 4 is human review and has not happened: no
`reviewed_by` is signed, so these artifacts are readable but not
buildable-on.**

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
  Four distinct **cross-record** ids are cited, all of them record-prefixed and
  all four verified to exist in the record named: `rfc-8610#R-0079` (×6),
  `rfc-8610#R-0102` (×4), `rfc-8610#R-0106` (×2) and `rfc-9165#R-0053` (×5).
  *[correction 2026-10-20, cross-check pass: this said "the only
  unqualified-looking exceptions are `rfc-8610#R-0102` and `rfc-8610#R-0106`".
  Those two are merely the only ones a prefix-blind resolver notices, because
  they fall outside this record's `R-0001`–`R-0092` range. The other two —
  `rfc-8610#R-0079` and `rfc-9165#R-0053` — **collide with ids this record also
  defines** (its own `R-0079` is the `from-clause` production and its `R-0053`
  is the prelude exemption), so a resolver that drops the prefix silently
  returns the wrong requirement. That is the dangerous case, and it was the
  unreported one.]*
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

### Cross-check run (pass 3, 2026-10-20)

Pass 3 did neither the extract nor the verify pass and wrote its own scripts. It
is the FX-1 cross-check: **requirements ↔ schema ↔ messages ↔ examples.** It did
not repeat pass 2's word sweeps, which stand.

**The four cross-check deliverables (`.claude/skills/extract` §3).**

1. **Every field a requirement names exists in `messages.yaml` or the schema —
   holds, in both directions.** `messages.yaml` carries **13 constructs and 41
   fields**; **all 41** have a non-empty `constrained_by`, citing **43 distinct**
   requirement ids, and **all 43 resolve**. Each of Appendix A's **ten**
   productions appears in `messages.yaml` *and* in `schema/`, and each one's
   requirement (`R-0078`–`R-0087`, one per production) is cited by at least one
   message field. Checked the hard way too: every field-like token in the 92
   requirement texts — production names, `%s"…"` literals, `%x` ranges, `;#`,
   `CDDL_INCLUDE_PATH`, `-icose=rfc9052`, `-scose.COSE_Key`, `$.start.$`,
   rule-name left-hand sides — was harvested mechanically and looked up: **30 of
   32 are held** in `messages.yaml` or `schema/`. The two that are not are
   `[I-D.bormann-cbor-cddl-2-draft]` and `[I-D.bormann-t2trg-deref-id]`, which
   are bibliography, not fields — and they are the record's one open limit (see
   the end of this file).
2. **Every message in a protocol flow is defined — `not_applicable`, and the
   verdict is consistent with everything else here.** There is no `protocol.yaml`
   to cross-check against. The verdict was not re-litigated by re-running the
   sweep; it was tested for *consistency*: all **13** constructs in
   `messages.yaml` carry an `encoding:` beginning **"plain text"** and none
   names a sender, a receiver or a role, which is what the file's header
   already claims ("There is no CBOR, no COSE and no wire format anywhere in
   this document"); the **19** vectors divide by `role:` into **6** module
   inputs, **7** composed outputs, **3** shell command lines, **1** directive,
   **1** grammar and **1** environment-variable value, and **not one is a
   message**; `normative.md`'s twenty locators are all front matter, §1–§4 or
   an appendix, with no exchange among them; and §4 allocates nothing
   (`R-0076`), so there is no registration to model either. Nothing in the
   record contradicts the verdict.
3. **Every state-machine trigger is a defined message or a named event — also
   `not_applicable`, same test, and the one thing that *looks* like a trigger
   checks out.** Swept the whole of `distilled/` for the state-machine
   vocabulary. `guard` and `lifecycle` occur **only** inside this file's own
   prose about the absence. `transition` occurs once outside it, in
   `requirements.yaml`'s `field` note for `R-0025`, where it means a tooling
   transition and not a state transition. And `trigger` occurs exactly once as
   a **field name**: `messages.yaml`'s `alias rule` construct has
   `- name: trigger`, whose value is "the selector written without the prefix,
   with an `as` clause present". That is a *syntactic condition on a one-shot
   transformation* — it names no source state, no target state and no event —
   and it is a defined condition on a defined construct, with both its
   `constrained_by` ids (`R-0063`, `R-0064`) resolving. So the deliverable is
   satisfied rather than vacuous. The one procedure in the document, module
   name resolution, is held as data in `schema/name-resolution.derived.yaml`,
   whose own fields read `resolution.specified_by_this_document: false`,
   `module_name.carries_a_principal/_version/_digest/_uri: false` and
   `one_way.composition_is_reversible: false` — a lookup, not a lifecycle, and
   the file contains no `state`, `transition`, `trigger` or `guard` key at all.
4. **Every example validates against the schema — all 19 confirmed, from the
   verbatim capture.** Pass 3 built the two checkers rather than taking pass 2's
   verdicts: (a) a backtracking recogniser for `directive`, whose character
   classes were read **out of `schema/module-directives.abnf` by parsing its
   `%x` ranges**, not transcribed by hand — first set 55 characters
   (`$ @ A-Z _ a-z`), repeat set 65 (adds `0-9`), `filename` 65 (`- . 0-9 A-Z _
   a-z`), and `.`/`-` in `filename` but in neither `id` set; and (b) a rule-name
   closure checker over the composed outputs using the **40** prelude names read
   from `records/ietf/rfc-8610/distilled/schema/prelude.cddl`. Result: **19 of 19
   `expect` verdicts reproduced**, tally **9 valid · 2 invalid · 4 incomplete · 4
   not-applicable**; of the seven printed directive instances **exactly two are
   not derivable** (lines 388 and 414), which is `G-01` and `V-0008`/`V-0010`;
   **six composed outputs closed, `V-0009` not** (dangling `label`, `values`),
   and `V-0009` is the only block with dead definitions beyond its root rule
   (`cose.label`, `cose.values`), which is `V-0013`'s alias apart. `V-0017`,
   whose basis is ABNF rather than CDDL, was checked separately: after dedent
   **all ten productions parse as well-formed RFC 5234 / RFC 7405 ABNF with no
   undefined reference**, so its `expect: valid` holds.

**Whole-record sweep, re-derived.**

- **Source.** 784 lines, 25 993 bytes, **13 form feeds**, sha256 recomputed
  `7cf825aa…a644` — identical to `record.yaml`'s `content.sha256` and to
  `summary.md`'s `| **Digest** |` row. (A note for anyone re-checking: Python's
  `str.splitlines()` splits on those 13 form feeds too, which shifts every line
  number by up to 13. Use `split("\n")`.)
- **Appendix A.** Lines 677–688, **12 lines, 10 productions**, region sha256
  `43c17148…96ab` recomputed and matching; the capture's body is byte-identical
  to the source region; common indent 3; **dedent and re-indent are exact
  inverses**; the dedented file's grammar-body sha256 is `520099c0…c149e`, which
  is what its own header claims; **no page-furniture and no blank line falls
  inside the region**.
- **Quote fidelity and page frames, independently.** **89** bullet quotes across
  **20** distinct locators in `normative.md`, **18** fenced blocks (18 distinct —
  so `examples/` has 19 vectors where this file has 18 blocks, the difference
  being Appendix A's grammar, which is `V-0017` and lives in `schema/`), **92**
  requirement texts and **19** vector texts were each matched against the source
  twice, once with the page furniture removed and once with it left in. **All
  218 spans matched both: 0 failures, 0 page-frame crossings.** 14 footers, 13
  headers, 13 form feeds.
- **BCP 14.** 0 with stripping on, 11 with it off, **0** across all 92
  requirement texts, and **0** on the source with lines 146–150 deleted — so the
  zero is exact, not a filter artefact. `reconciliation` is 7 142 characters,
  as the header says.
- **Both YAML readers, on all five YAML artifacts.** `requirements.yaml`,
  `messages.yaml`, `examples/vectors.yaml`, `schema/name-resolution.derived.yaml`
  and `record.yaml` all parse under `bin/_yaml.py` and `bin/_record_yaml.py`, and
  **agree on every value**, with identical id sequences (92 and 19, unique and
  contiguous from 1). The two readers differ **by design** on five things, and
  normalising for them is what "agree" means here: block-scalar chomping,
  numeric coercion, boolean/null coercion, flow collections (`_yaml.py` has
  none, so `['a','b']` is a string to it) and `\"` unescaping inside a
  double-quoted scalar. Those are properties of the two tools and apply to every
  record in this library.
- **Derived vs verbatim.** **1 verbatim, 4 derived.** Every `.derived.` filename
  has a header claiming derived; `module-directives.abnf` has no infix and its
  header claims verbatim; no name and header disagree. Re-derived with the same
  first-marker-wins rule `bin/validate` uses.
- **Placeholder markers under `distilled/`: 0.** Every file under `distilled/`
  was swept for the all-capitals four-letter placeholder token before `status`
  moved to `distilled`, because `bin/validate` rejects that status while one
  survives. The Acknowledgments placeholder therefore stays **described, never
  quoted** — defect 8. (Precisely: `bin/validate` sweeps the FX-1 artifact
  paths, which is every file under `distilled/` except this one. Pass 3 swept
  all of them anyway and this file carries no instance either.)
- **Citations.** 92 R, 19 V and 21 G ids defined, unique and contiguous; every
  one of the 132 is cited somewhere; **0 dangling**. **Entering pass 3, 23 of
  the 92 R ids were cited nowhere but their own definition** — `R-0002`,
  `R-0004`, `R-0006`, `R-0007`, `R-0010`, `R-0011`, `R-0013`, `R-0014`,
  `R-0016`, `R-0017`, `R-0018`, `R-0024`, `R-0025`, `R-0026`, `R-0027`,
  `R-0029`, `R-0037`, `R-0044`, `R-0055`, `R-0059`, `R-0065`, `R-0070`,
  `R-0074`. (Writing that list here is itself a citation of each, so the count
  is now 0 — said this way because the number is a measurement of a moment, and
  a later pass re-running the check will get 0 and should not read it as
  disagreement.) That is deliberate, not an omission: every one is
  document status, motivation, terminology, a section lead-in, a presentation
  convention or security posture, and **none names a construct or a field that
  `messages.yaml` and `schema/` do not already hold** — which is the thing
  deliverable 1 asks. They are recorded so a later pass does not have to
  re-derive the list.
- **Cross-record claims, re-verified at the source.** `rfc-8610`'s `id = EALPHA
  *(*("-" / ".") (EALPHA / DIGIT))` and `EALPHA = ALPHA / "@" / "_" / "$"` are
  where `G-01` says they are — inside the `BEGIN VERBATIM B-3` region of
  `records/ietf/rfc-8610/distilled/schema/cddl.abnf`, cited by production name.
  The **40** prelude names are set-equal to the list `examples/README.md` prints,
  and **five** of them are hyphenated (`cbor-any`, `encoded-cbor`, `float16-32`,
  `float32-64`, `mime-message`). `rfc-9682`'s change table does list `id`,
  `EALPHA`, `ALPHA`, `DIGIT` **and** `CRLF` among its forty-one
  carried-unchanged productions. `rfc-8610#R-0079`, `rfc-8610#R-0102`,
  `rfc-8610#R-0106` and `rfc-9165#R-0053` all exist and say what this record
  quotes them as saying. **Every cross-record id in this record is written with
  its record name in full**, never abbreviated to `#R-nnnn`: the abbreviation
  resolves to the wrong requirement under any prefix-blind reader, and **two of
  these four** — `rfc-8610#R-0079` and `rfc-9165#R-0053` — fall inside this
  record's own `R-0001`–`R-0092` range, so for those two a prefix-blind reader
  silently succeeds with the wrong text rather than failing.

**Five things corrected in pass 3**, all of them our own text, each marked
`[correction 2026-10-20]` where it sits. None is a finding and none touches the
source.

1. **The `$.start.$` wording pass 2 corrected in one place survived in six.**
   Pass 2 fixed `G-18`'s headline — "used once and never defined" is false at
   face value, because source line 509 *is* the definition — and left the same
   claim standing in `normative.md` **twice** (the inline note before the §2.7
   block, and the *What the document does not say* bullet), in `messages.yaml`,
   in `examples/vectors.yaml` `V-0016`, in `examples/README.md`'s diff-pairs
   table, and in `record.yaml`'s own coverage line for the normative artifact.
   All six now say what `G-18` says: the name occurs once, as its own
   definition, and the *convention* is what is never introduced. This is the
   shape of the failure worth naming — a correction applied where it was found
   rather than where the claim lives, in a record that states the same fact in
   six artifacts.
2. **Three cross-record citations by line number.** `schema/README.md`,
   `design-notes.md` and `G-17` each cited
   `records/ietf/rfc-9052/distilled/schema/cose.cddl` "lines 60–67 and 168–175".
   The ranges are correct today, but this is precisely the drift pass 2 had to
   repair in `G-01`, and the remedy is the same: all three now cite the
   `COSE_Key` and `Generic_Headers` fragments by production name and by that
   file's own `; §…` markers. **No cross-record citation by line number remains
   anywhere in this record.**
3. **The citation-integrity bullet above understated the cross-record surface**
   — see its own correction note. Two of the four cross-record ids collide with
   ids this record defines, which is the case that actually misleads.
4. **`summary.md` said the draft "names no implementation".** It names `cddlc`,
   with a repository, an install command and a version floor — in an appendix it
   declares informative. The record's own `R-0089`–`R-0092`, `V-0018`, `V-0019`
   and `G-20` all said so; only the summary did not.
5. **`record.yaml` carried `authors: []`** while `summary.md`'s metadata table
   named both authors off the same four title-block lines — the record and its
   summary disagreeing about a fact both state. Now filled from source lines
   5–8. It changes the two generated views that read the field
   (`index/bibliography.md`'s entry, and `bin/render-html`'s Authors row, which
   is suppressed on an empty list); `bin/export` does not read `authors`, so the
   CSL-JSON and BibTeX are untouched.

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

**One question this record still cannot answer, and it is the record's one open
limit**: the rationale for naming modules by filename lives in
`[I-D.bormann-cbor-cddl-2-draft]-09` (1 September 2026, §4 and §A.2, per
`R-0021` and `R-0041`) and the dereferenceable-identifier security analysis in
`[I-D.bormann-t2trg-deref-id]-07` (24 February 2026, per `R-0075`). Pass 2
confirmed that **this library holds neither**, and pass 3 re-confirmed it on
2026-10-20 across **all 439 record directories, not just `records/ietf/`**, and
in `.cache/`: no record, no identifier naming either draft in any record, and no
cached copy. So the namespacing argument is one hop away and unread, and this
is the only gap the cross-check's token sweep found between what the
requirements name and what `messages.yaml` and `schema/` hold — correctly, since
these are bibliography rather than fields. **Ingesting them is a separate
decision and pass 3 did not take it**; `design-notes.md` open questions 6 and 7
own it, and `summary.md`'s *Limits* states it where a reader meets it.
