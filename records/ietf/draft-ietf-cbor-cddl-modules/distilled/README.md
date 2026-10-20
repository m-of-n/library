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

**State: pass 1 (extract) complete. No `profile` is declared** — this record
claims `distillation.standard: FX-1` and records the extract pass; the verify
and cross-check passes are not done, so there is no numerator yet
(`docs/extraction.md`: "An *unfinished* extraction is neither `full` nor
`partial`: it has no profile yet"). **No `reviewed_by` is signed.**

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
  the source**, not asserted: of twenty exchange words, **seventeen do not
  occur at all** — `respon`, `send`, `receiv`, `client`, `server`, `peer`,
  `party`, `parties`, `endpoint`, `handshake`, `negotiat`, `message`,
  **`protocol`**, `transmit`, `reply`, `session`. The three that do hit are not
  exchanges: `request` ×1 is "The import statement can also request an alias"
  (line 437), `sent` ×7 is every occurrence inside the word "present", and
  `acknowledg` ×3 is the Acknowledgments heading and its placeholder. **The word
  "protocol" does not appear in this document.**
- **state-machine** — `state-machine.yaml` is absent, for the same reason.
  Nothing in the document registers, issues, rotates, revokes or expires
  anything. The nearest thing to a procedure is **module name resolution**, and
  it is a name lookup over a search path, with no states and no transitions —
  and the specification declines to define even that: "The exact way how these
  source directories and possibly a precedence between them are established is
  intentionally not fully defined in this specification" (`R-0036`). Its
  structure is held as data in `schema/name-resolution.derived.yaml` instead,
  which is the honest shape for it. **Checked by the same sweep**: of seventeen
  lifecycle words, **thirteen do not occur** — `register`, `registr`,
  `issuanc`, `revoke`, `revocat`, `rotate`, `rotation`, `expiry`,
  `expiration`, `renew`, `transition`, `lifecycle`, `enroll`. The four that hit
  are all furniture: `expire` ×16 is the Internet-Draft expiry sentence plus the
  running footer on all fourteen pages, `issue` ×1 is the GitHub issue-tracker
  URL (line 43), `state` ×1 is inside "statement" (line 437), and
  `provision` ×3 is the BCP 78/79 and Trust Legal Provisions boilerplate.

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
4. **`CRLF` is redefined against its own metalanguage.** Appendix A declares
   STD 68 (`R-0077`), whose core rule is `CRLF = CR LF`, then defines
   `CRLF = %x0A / %x0D.0A` (`R-0087`), admitting a bare LF. **This is
   `rfc-8610` defect 7 reproduced** — but there it hides among identical
   redefinitions of `ALPHA`, `DIGIT`, `HEXDIG` and `SP`, whereas here only
   `SP = %x20` keeps its core value, so the one redefinition stands alone and
   unremarked. The defect is now in **two** current CDDL documents. G-02.
5. **A rendering defect in a load-bearing character.** Source line 522 reads
   "(no – was given on the command line)" with **U+2013 EN DASH**, where the
   sense requires the ASCII `-` that every other example uses as the stdin
   argument (`R-0069`). Reproduced in our quotes, not repaired.
6. **`$.start.$` is used once and never defined.** Line 509 (`R-0068`). It is a
   valid RFC 8610 `id`, and it is spelled like an RFC 8610 §3.9 **type socket**
   (leading `$`) yet defined with `=` where §3.9 extends sockets with `/=`. No
   sentence introduces the convention or says whether the name is reserved.
   G-18.
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

**One open question this record explicitly cannot answer**: `R-0005` says CDDL
is defined by RFC 8610 **and RFC 9682** as well as RFC 9165 and RFC 9741, and
`rfc-9682` is "Updates to the CDDL Grammar". If RFC 9682 changes `id`, the
severity of defect 1 changes with it. That is the `rfc-9682` lane's to settle.
