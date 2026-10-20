---
record: draft-ietf-cbor-edn-literals
kind: index
title: "draft-ietf-cbor-edn-literals — distilled artifacts"
extracted: "2026-10-19"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

**State: all three passes complete, `profile: full`.** Extract by two agents in
parallel at effort max, then an independent verify pass at effort max, then a
cross-check pass at effort max, each reading only
`.cache/draft-ietf-cbor-edn-literals.txt` and the artifacts. Every
`reviewed_by` is still empty: no human has signed anything off.

What the verify pass changed is listed under *What pass 2 found*; what the
cross-check pass changed is under *What pass 3 found*.

Source: *Concise Diagnostic Notation (CDN)*, `draft-ietf-cbor-edn-literals-27`.
Header: `Updates: 8610, 8949 (if approved)`.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 226 verbatim bullets and 43 fenced blocks in 43 exact source line runs — 14 ABNF figures, 12 tables, §6.1's numbered items, both registry field blocks, the media-type template and the six editorial crefs marked for removal. 43/43 fences byte-identical by per-fence sha256, re-verified against the cached source by the cross-check pass; 226/226 bullets contiguous; 0 locator failures by section range; 0 overlapping runs; and the 226 bullet ids are the 226 `requirements.yaml` ids exactly, as sets. Bullet order follows the SOURCE, not the id number, because `R-0216`–`R-0226` were appended rather than renumbered |
| requirements | `requirements.yaml` | 226 entries, `R-0001`–`R-0226`, no gaps: **10 stated, 216 inferred**. Counts reconcile 10 = 10, and each of the ten keyword occurrences was matched to exactly one entry by normalised offset — a bijection, not a tally. `R-0001`–`R-0215` are in source order; `R-0216`–`R-0226` were appended by the verify pass. The reconciliation states the real baseline — see below |
| schema | `schema/` | **13 verbatim across 23 regions, 3 derived.** All 23 regions re-read in the verify pass and compared byte-for-byte against their declared line range and sha256: 23/23 exact. Figure 1's closure re-derived independently twice: 85 productions, 0 duplicates, 0 incremental `=/`, 82 distinct names referenced and all resolving, exactly three unreferenced — and it **holds across all three page frames**, with exactly one rule (`hexscalar-s`) straddling one. `cdn-dedented.derived.abnf` round-trips exactly in both directions and yields the same 85 rules with identical right-hand sides. The cross-check pass **loaded the grammar into a recogniser and ran it**: 56 parse claims tested, 56 held |
| messages | `messages.yaml` | 35 literal forms, 84 fields, **311** requirement references (167 distinct), 0 dangling. The cross-check pass walked all 226 requirements the other way: 173 are named by `messages.yaml` or `schema/`, and the 53 that name no construct fall in eleven classes the file's header enumerates |
| examples | `examples/` | **251 vectors**, 242 valid / 9 invalid. 52 hex sequences the document printed were decoded and confirmed; **1 was printed and is wrong**; **173** are ours and marked `COMPUTED HEX.`; **25** carry no hex with a stated reason. 63 printed byte sequences were independently re-encoded from the EDN — 61 matched, 2 did not, and both are cells of one Table 6 row. The verify pass re-encoded all 223 hex-carrying vectors with its own codec and **corrected two of ours** (`V-0131`, `V-0139`); the cross-check pass **parsed all 251 against `schema/cdn.abnf`** — 242 as held, 246 with the document's own line terminator — and gave `V-0238` the bytes it was withholding |
| design-notes | `design-notes.md` | the byte-string prefix disposition, ten further EDN/CDDL divergences, the verdict on EDN as our test-vector format, and the MD-3 section |

## Not applicable

- **protocol** — pure notation. §1: "CDN is not designed or intended for
  general-purpose use in protocol elements exchanged between systems engaged
  in processes outside those listed here." §1.3 and §2 both quote STD 94's
  "All actual interchange always happens in the binary format", and §7.3's
  media-type registration gives Intended usage **LIMITED USE** with
  "Restrictions on usage: Concise diagnostic notation represents CBOR data
  items, which are the format intended for actual interchange." No roles, no
  peers, no request/response, no error paths between parties.
- **state-machine** — and this one was a genuine call rather than an absence.
  §5.1 defines a real **three-outcome resolution rule** for a prefixed literal
  (resolve it; defer it into `CPA999`; or "this is usually an error and
  processing has to stop"), and §5 describes a stage pipeline where "chains of
  tools are involved in processing CDN". But that is a *per-item decision
  procedure*, not a lifecycle: nothing persists between items, no item is in a
  state, and the pipeline's stages belong to the toolchain rather than to the
  notation. It is modelled where it belongs — as resolution behaviour in
  `messages.yaml` and in `schema/byte-string-prefixes.derived.yaml` — not as a
  machine. Compare `rfc-9053`, which *does* carry a state machine, because its
  key-usage counters persist across messages.

## The byte-string prefix question, settled

#39 assigns EDN the test-vector role, and this library's `rfc-8610` extraction
found a conflict bearing directly on that: RFC 8610 Appendix G.2 (normative)
names four prefixes — `h`, `b32`, `h32`, `b64` — while §3.1 and the ABNF
`bsqual = "h" / "b64"` admit two, never reconciled.

**This document resolves it, by retiring the text that said four.** §1: "It
updates RFC8949 by obsoleting Section 8 of RFC 8949 [STD94], and [RFC8610] by
obsoleting Appendix G of [RFC8610]." The four-prefix list lived in Appendix
G.2. §3.1 then defines exactly two, and explains the omission: `b32`/`h32`
"has not been implemented widely and therefore is not directly included in
this specification." So CDN converges on **the CDDL side** of the old
conflict, and both survivors are mandatory to implement.

Four things keep that from being structural, and they matter for us:

1. **`b32'…'` still parses.** `app-prefix = lcalpha *lcldh / ucalpha *ucldh` (Figure 1 — the lowercase alternative admits any
   `[a-z][a-z0-9-]*`), so it is a well-formed `app-string`; what rejects it is
   §5.1's *resolution* rule, one layer above the grammar. **Do not use an ABNF
   check as a prefix allowlist.** In CDDL the same text is a syntax error — so
   the two languages fail differently, not identically.
2. **The prefix sets now agree; the literal syntax still does not.** CDDL's
   `bytes = [bsqual] %x27 *BCHAR %x27` takes a prefix and a *single-quoted*
   string only. CDN admits three carriers — single-quoted, raw
   (`` h`12345678` ``) and sequence (`h<<"…">>`) — and says the extension
   "cannot distinguish" them. **Our vector generator must emit the
   single-quoted form**, which is also §1.3.3's own basic output format. The
   same applies to `dt'…'`, `ip'…'`, `cri'…'`, `float'…'`: all valid CDN, none
   a CDDL byte-string literal.
3. **§7.1's registry contradicts §6.2's table.** Table 8 lists `h`, `b32`,
   `h32` and `b64` with the *identical* row — Description "Reserved",
   Reference "RFC8949" — although this document defines two of them and
   declines the other two, and `b32`'s reference points at a section this
   draft obsoletes. Table 7 is the list of prefixes with meanings and
   `b32`/`h32` are absent from it.
4. **It is an Internet-Draft.** `(if approved)`. Until it publishes, RFC 8610
   Appendix G.2 is still in force and the conflict is still live. `{h, b64}`
   is the intersection and is safe under both readings.

## What pass 2 found

The verify pass re-derived every number in this file from the cached source with
its own tools — its own normaliser, its own section map, its own ABNF
analyser, its own CBOR codec and CDN parser. **Everything structural held.** The
ten keywords, the 85-production closure across three page frames, all 23 schema
regions, the 43 fence sha256s, the Table 6 defect, Figure 8's two dropped
alternatives, the byte-string-prefix disposition, and the verdict that EDN cannot
carry our vectors: all confirmed, none weakened. What it changed:

- **Two of our own computed vectors were wrong.** `V-0131` and `V-0139` encoded
  −14159024.0 as binary64. It fits binary32 exactly, so Preferred
  Serialization requires `facb580cb0`. Both corrected; `examples/README.md`
  shows the arithmetic.
- **Eleven dropped normative statements were added** as `R-0216`–`R-0226`:
  §2.3.2's escaping rule, two §2.3.4 statements about a sequence
  literal's value, §3's statement of what an app-extension specification
  fixes, three §4.1 statements, §5.2's licence for ellipses inside
  `h''`, and four §7.1/§7.2 expert-policy rules. The most consequential
  is `R-0222`: §4.1's own statement that an absent encoding indicator implies
  Preferred Serialization, which is the authority our vector files rest on and is
  what settles `V-0131`.
- **Fifteen quotations in `vectors.yaml` had silently healed a source defect.**
  Nine (the §3.5 `t1`/`b1` cref), four (§3.1's "single- quoted"), one
  (§2.3.2's "byte- string") and one (§5.1's "app- sequence" and
  "App- Extension") repaired a line-break hyphenation, and the cref quotation
  also dropped the source's own `//` markers. All now carry the source's bytes.
  Nine more quotations ended in a full stop the source does not have there —
  eight of them §2.4.1's trailing-comma sentence, clipped before its
  ", enabling …", and one §3.8's, where the period replaced a dropped
  `[STD94]` — and one was spliced across a `*` list marker.
- **`V-0212` and `V-0213` were reclassified** `COMPUTED HEX.` →
  `SOURCE HEX.`: §4.3 prints `5f ff` and `7f ff`, so "the document prints
  only the EDN" was false of them. Both agree with our encoding. That is why the
  printed-sequence tally moved from 61/59 to 63/61.
- **Counts corrected:** 31 fenced blocks in 37 runs → 37 in 43 (the six
  editorial crefs were verbatim with sha256 and uncounted — pass 3 took this
  the rest of the way to **43 in 43**, below); nine differing rule
  redefinitions → eight; six undeclared Figure 1 dependencies → eight;
  `cdn.abnf`'s header said Figure 1 had 97 productions where it has 85.
- **One `field` carried a mid-edit trace.** `R-0011`'s said the sentence was
  "SEVERED BY A PAGE FRAME between 'there' ... no — between 'CDN MUST' ...".
  No page frame cuts it; it runs over lines 518–521 with ordinary line breaks.
  Rewritten.
- **One reasoning defect in the reconciliation.** It called four of the five MAYs
  "one permission restated in four contexts". Three are (the §2 sentence and
  its two explicit back-references); the fourth, `R-0062`, is a separate
  permission conditional on the first — relaxing UTF-8 validity for text
  strings. It also now records the one place where the claim that *no keyword
  constrains the notation itself* is strained: `R-0011`'s grammatical subject is
  "CDN", not an implementation.

## What pass 3 found

The cross-check pass checked **artifact against artifact**, not artifact against
source, and it did the one thing no earlier pass had: **it ran the grammar.** An
RFC 5234 ABNF reader and a memoised set-of-end-positions recogniser, reading
`schema/cdn.abnf`'s own bytes — the reader strips the `;` headers and the
three-column margin itself, so the grammar under test is the verbatim artifact.

**The four cross-checks all pass.**

1. **Every field a requirement names exists.** All 226 requirements were walked
   against `messages.yaml`'s 35 literal forms and 84 fields and against the 16
   files in `schema/`. Shape confirmed exactly: 35 / 84 / 0 dangling. **173
   requirements are named by one or the other; 53 name no construct**, and all
   53 fall in eleven legitimate classes — generator configuration (§1.3.3's
   basic output format), pre-parse input transformation (§1.3.5), removals
   (§2.1.1), capability disclaimers (§2.3.5), statements about the language as a
   whole (§2, Appendix A), statements about *tools* (§4, §5, §8), statements
   *about the ABNF* (§6, which live in `schema/`), and registry process
   (§7.1/§7.2). **Thirteen links were missing and are now made.** The eleven
   entries pass 2 appended had never been reconciled here at all: eight of them
   name a construct (`R-0216`–`R-0223`) and now point at it, the other three
   are expert-review policy and correctly point at nothing. `R-0222` — an absent
   encoding indicator implies Preferred Serialization — is now linked from both
   forms whose `cbor` invokes that convention, because it is the authority every
   `COMPUTED HEX.` byte rests on. Five pass-1 omissions (`R-0037`, `R-0046`,
   `R-0047`, `R-0056`, `R-0059`) were linked too. 290 references → 311.
2. **`protocol: not_applicable` holds.** All 35 forms carry
   `encoding: CDN-text`; a CDN literal is a text, not a message. Swept for
   exchange vocabulary across every artifact, the only hits are IANA
   *registration* requests, the document's own *disclaimer* of round-tripping,
   and a `/session-id/` comment inside `V-0009` — a GRASP message *written in*
   CDN, which is CDN describing an exchange, not participating in one. No roles,
   no peers, no request/response, no error paths between parties.
3. **`state-machine: not_applicable` holds, and the parser corroborates it.** No
   state table, transition or lifecycle appears in any artifact; §5.1's
   three-outcome resolution rule is modelled where the reason says it is, in
   `messages.yaml` (three entries) and
   `schema/byte-string-prefixes.derived.yaml`. The reason's first persistence
   candidate is now evidence rather than argument: the raw-string delimiter
   width had to be hand-coded as a **parameter of one literal's match**, and
   nothing survives the literal.
4. **Every example parses.** 242 of 251 as held, 246 with the document's own line
   terminator; identical from both candidate start symbols and under both
   readings of the raw-string widths. Six of the nine `invalid` vectors fail the
   **grammar** rather than the semantics, and each already carried a `violates`
   naming the §6.1 production. All 17 deliberate non-encodables parse. Full
   result and the per-vector table in `examples/README.md`.

What it changed:

- **`V-0238` was refusing bytes that `V-0239` prints for the same value.** It
  carries them now (`c249358a750438f380f5f6`); the "no-IANA-tags profile"
  caveat stays in `notes`, where it belongs. Provenance `172`/`26` →
  **`173`/`25`**, which also makes the `NO HEX.` class exactly the 17
  deliberate non-encodables plus eight of the nine invalid vectors.
- **Two source defects were found by running the grammar**, recorded never
  repaired, as `schema/grammar-gaps.derived.txt` **G‑31** and **G‑32**. G‑31:
  `comment = … / eol-comment *non-lf %x0A` requires a terminating newline, so a
  CDN text cannot *end* with a `#` or `//` comment — which is why three of the
  document's own §2.3.1 examples parse only with their line terminator, and why
  `//` fails the grammar as well as §2.1.1's prose. G‑32: §7.2's `Reference`
  field describes "the app- extension identifier" inside the **Encoding
  Indicators** registry, copied from §7.1.
- **`R-0193`'s locator stays `§7.1`,** deliberately, and its `field` now says
  why. Its text is the only one in the file that occurs twice in the document
  (source lines 3281 and 3381, heading both registry field blocks); every
  locator in this library's IETF records names a single section and
  `normative.md` groups bullets per section, and nothing is lost because both
  blocks are fenced verbatim and §7.2's substance is carried by `R-0196`–
  `R-0198`, `R-0225` and `R-0226`.
- **Three stale counts corrected where pass 2 had moved the number but not
  every file.** `37 fenced blocks in 43 runs` → **43 in 43** (re-derived: 43
  fences, 43 run comments, all 43 byte-identical to the cached source, 0
  overlaps — the six editorial crefs are fenced like the rest, they merely put
  the run comment above the bold label). `schema/README.md` still said **nine**
  differing rule redefinitions and **six** names needed from Figure 1; both are
  re-derived here as **eight** and **eight**, and the 24 / 16 / 8 split is now
  the same in `schema/README.md` and in `grammar-gaps.derived.txt`'s own
  checklist, which still said 15 / 9.
- **`V-0174`'s note offered a repair that does not parse.** It read "`b1<"Hello
  world">>` or `b1<<"Hello world">>`"; only the second is well-formed, and the
  recogniser rejects all three of `b1<…>`, `b1<…>>` and `b1<<…>`.

**Nothing structural moved.** The ten keywords, the 226 entries, the
85-production closure, the 23 schema regions, the 43 fences, the per-figure
counts, the Table 6 defect, Figure 8's dropped alternatives, the byte-string
prefix disposition and the verdict that EDN cannot carry our vectors: all
re-derived or re-confirmed, none weakened.

## Why 10 keywords in 168 KB is the right answer

Like `rfc-8610`, this is a **notation**: its normativity is a grammar and a set
of literal meanings, not obligations on an actor. §6 is 340 lines of ABNF in 14
figures and carries **no BCP 14 keyword at all**. Only two of the ten are
obligations and both are narrow; the single MUST NOT bounds an *optional*
feature; and **three** of the five MAYs are one permission restated in three
contexts, while a fourth (`R-0062`) is a separate permission conditional on it
and the fifth (`R-0082`) licenses an app-extension's uppercase prefix variant.
**No keyword in this document constrains the notation itself.** The
reconciliation says what was counted instead — literal forms, grammar side
conditions, explicit disclaimers of capability, the removals relative to
RFC 8610 Appendix G and RFC 8949 §8, registry rules, and the lower-case force
words the document actually uses.

## Source defects found

Full enumeration in `schema/grammar-gaps.derived.txt` (G-01…G-32; `G-31` and
`G-32` were found by the cross-check pass, by running the grammar). The ones
that would bite an implementer:

1. **Figure 8 silently drops two alternatives from `bstr`.** §6.3 introduces it
   as "add an alternative to bstr", but prints a full redefinition that omits
   `app-rstring` and `rawstring`. A parser built as Figure 8 instructs **loses
   raw string literals entirely and silently**, because the result is still a
   closed grammar — and raw strings are a headline feature of §2.3.3.
2. **§6.3 understates its own dependencies**, naming Figures 2 and 9 as the
   common definitions when **eight** referenced names appear only in Figure 1:
   `DIGIT1`, `HEXDIG1`, `ODIGIT` (needed by Figure 9) and `alikerawdelim`,
   `ellipsis`, `eol-comment`, `shortrawdelim`, `startrawdelim` (by Figures
   11–14). §6.3.4 is the one subsection that does declare an out-of-set
   dependency — "the rule b64dig from Figure 12" — so the omission in the
   other three is an oversight, not a convention.
3. **§4.1 Table 6's major-type-3 row prints the wrong bytes.** `"A"_1` is given
   as `79000161` / `6161`; `0x79` is mt3 with a two-byte length, so with
   content `"A"` (`0x41`) the correct bytes are **`79000141` / `6141`**. The
   printed bytes encode `"a"` — almost certainly copied from the row above,
   where a one-byte *byte* string's head and content both read `0x41` and so
   coincide. Found by round-tripping, and independently re-derived.
4. **A production is cut in half by a page frame**: `hexscalar-s` loses
   `/ "7F"` and `/ HEXDIG1` across the page 45/46 boundary. Read one page, get
   a truncated rule.
5. **Eight** rule names are redefined with differing right-hand sides across
   figures a reader is told to combine (pass 1 said nine and counted
   `ellipsis`, whose two definitions differ only in an ABNF comment); three
   rules in Figure 1 are dead — `newline`, `lblank` and `one-item` — the
   last a **second plausible start symbol** with no sentence saying which is
   the root.
6. `b64dig` mixes both RFC 4648 alphabets in one rule, justified because they
   "have the same meaning where they overlap" — and `-_+/` is exactly where
   they do not.
7. Ellipses work inside `h''` and not inside `b64''`, unremarked, though §5.2
   relies on the `h` form.
8. `b1<"Hello world">` (§3.5) uses single angle brackets where
   `app-sequence` needs two; at 20 characters in a 78-column document it is a
   typo rather than a truncation. By contrast §5.2's `bytes_in_IRI` line is
   exactly 78 characters, so that one probably *is* a rendering truncation —
   recorded as such rather than as a defect.
9. **`ilbs`/`ilts` are unregistered.** §3.6 defines them and §4.3 makes them
   the replacement for the deprecated `streamstring`, yet neither appears in
   Table 7 or Table 8, while §5.1 makes an unregistered prefix an error.

**One thing this draft gets right that RFC 8610 did not:**
`NONASCII = %x80-D7FF / %xE000-10FFFF` correctly **excludes surrogates**.
`rfc-8610`'s own G-32 records the opposite for its grammar.

**Stability risks, not defects:** `t1` and `b1` are explicitly *provisional*
names and both are mandatory to implement, and `CPA888`/`CPA999` are
unassigned placeholders — do not hard-code 888 or 999.
