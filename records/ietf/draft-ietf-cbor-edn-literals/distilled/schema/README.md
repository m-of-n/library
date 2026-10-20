---
record: draft-ietf-cbor-edn-literals
kind: schema
title: "draft-ietf-cbor-edn-literals — schemas"
extracted: "2026-10-19"
reviewed_by: ""
---

# Schemas

**For this record the schema directory is the extraction, not a side artifact.**
draft-ietf-cbor-edn-literals-27 carries **ten** BCP 14 keyword occurrences in
168 KB, and Section 6 — 340 lines of ABNF in **fourteen figures** — carries
none of them. CDN is a *notation*: it says what a sequence of characters
denotes and which CBOR data item it maps to. Its normativity lives in the
grammar and in the meaning of the literal forms, so what a reader needs from
this record is **the grammar held exactly** and **the side conditions held
honestly**. Thirteen of the sixteen files here, this README aside, are the
source's own bytes; three are ours.

The filename carries the distinction and `bin/validate` enforces it: a
`.derived.` infix is mandatory on anything this library wrote, and an unmarked
name asserts verbatim bytes (`docs/extraction.md`, "Derived vs verbatim — the
filename carries it"). Each file repeats the claim in its own header.

**Every verbatim region in this directory carries its source line range and a
sha256 of those lines in its own header, and all 23 regions were re-read and
compared byte-for-byte against the cached source after writing.** The source is
`draft-ietf-cbor-edn-literals-27`, cached sha256
`43cfb1236435a9de62d3c202b7ee653b0f5adbd40d3800bbb9379379dbdbf7e9`, which is
this record's `content.sha256`.

## Per-file

| file | claim | what it covers | what it does **not** constrain |
|---|---|---|---|
| `cdn.abnf` | **verbatim** | **Section 6.1, Figure 1, complete** — the whole grammar of CDN, **85 productions** `seq` … `NONASCII`, with the draft's three-column page margin preserved, in **four** BEGIN/END regions split at the three page frames the figure crosses (source lines 2357‑2404, 2413‑2459, 2469‑2516, 2525‑2557) | **everything semantic.** It cannot tell `alikerawdelim` from `shortrawdelim` (they have the same RHS and are distinguished only by ABNF comments), cannot check that a `streamstring`'s chunks are all one type, cannot express PEG ordering, and admits any `[a-z][a-z0-9-]*` prefix whether registered or not. Section 6.1 item 7 concedes the first of these outright |
| `cdn-dedented.derived.abnf` | derived | `cdn.abnf` with the three-column margin removed and each page frame replaced by one blank line — **nothing else** | it is **not** the source's bytes. Cite `cdn.abnf`. It exists because an indented ABNF file collapses into a single rule under RFC 5234 and no tool can read it. It also **joins the `hexscalar-s` rule that the page 45/46 frame cuts in half** |
| `app-extension-common.abnf` | **verbatim** | Section 6.2, Figure 2 — the 7 rules the per-extension grammars do not repeat | **collides with `cdn.abnf`.** `non-lf` is `%x09 / %x0D / %x20-7F / NONASCII` in Figure 1 and `%x20-7f / NONASCII` here; `ALPHA` is respelt. The two sets are not namespaced |
| `app-string-h.abnf` | **verbatim** | Section 6.2.1, Figure 3 — 10 rules for the **decoded** content of `h''` and `` h` ` ``, including blank space, both comment syntaxes and ellipses | it parses the string *after* escape decoding and after Section 1.3.5's carriage-return removal. It says nothing about the enclosing literal |
| `app-string-b64.abnf` | **verbatim** | Section 6.2.2, Figure 4 — 4 rules for the decoded content of `b64''` and `` b64` ` `` | **no ellipses** (unlike `h`), and `b64dig` mixes the classic and URL-safe alphabets in one rule, so a literal may contain `+`, `/`, `-` and `_` together |
| `app-string-dt.abnf` | **verbatim** | Section 6.2.3, Figure 5 — 14 rules, RFC 3339 `date-time` | the comments carry the real ranges (`; 01-12`, `; 00-23`, leap-second rules); the grammar admits `9999-99-99T99:99:99Z` |
| `app-string-ip.abnf` | **verbatim** | Section 6.2.4, Figure 6 — 9 rules, RFC 3986 `IPv4address`/`IPv6address` **rearranged for PEG compatibility**, plus an optional `/` prefix length | the rearrangement is the draft's; it is not RFC 3986's own ordering. Nothing bounds the prefix length against the address family |
| `app-string-cri.abnf` | **verbatim** | Section 6.2.5, Figure 7 — 37 rules, RFC 3986 `URI-reference`, in two regions split at the page 54/55 frame | IRIs must first be converted per RFC 3987 Section 3.1. Carries `path-empty = 0<pchar>` (prose-value notation several ABNF tools reject), an `IPv4adress` typo and an unfilled `[RFC XXXX]` placeholder, all in the source |
| `integrated-parser-common.abnf` | **verbatim** | Section 6.3, Figures 8, 9 and 10 — the glue rule, the escape-aware rules and the raw-string rule an optional one-pass parser needs | **Figure 8 silently drops `app-rstring` and `rawstring` from `bstr`** — see *Defects* below. Section 6.3 also understates the dependencies: Figure 9 needs `DIGIT1`, `HEXDIG1` and `ODIGIT`, which live only in Figure 1 |
| `integrated-parsers-h-b64.abnf` | **verbatim** | Sections 6.3.1–6.3.4, Figures 11–14 — 26 rules, worked integrated parsers for `h''`, `b64''`, `` h` ` `` and `` b64` ` `` | **entirely optional.** Section 6.3: there is "no expectation for a new app-extension to supply ABNF for an integrated parser (or any ABNF at all!)" |
| `app-prefix-table.txt` | **verbatim** | Section 6.2, Table 7 — every prefix **defined in this document**, its input and its result type, in two regions split at the page 48/49 frame | it is the authoritative list of what exists. **`b32` and `h32` are not in it** |
| `app-extension-registry.txt` | **verbatim** | Section 7.1, Table 8 — the 16 initial IANA entries, all Change Controller "IETF" | "Reserved" here is a **registry** state, not a notation state: `h` and `b64` are listed the same way as `b32` and `h32`, and only the first two have meanings |
| `encoding-indicator-registry.txt` | **verbatim** | Section 7.2, Table 9 — the 10 initial encoding indicators and the `ai` value each selects | the grammar's `spec = ["_" *wordchar]` admits any of them and many more; the registry, not the grammar, says which mean anything |
| `tags.txt` | **verbatim** | Section 7.5, Table 12 — the two CBOR tags requested | **`CPA888` and `CPA999` are placeholders, not assignments.** Section 7.5 gives them as "suggested assignments: 888 and 999" and an RFC-Editor note instructs that the `CPA` prefix be stripped and the residue replaced |
| `byte-string-prefixes.derived.yaml` | derived | **the library#39 question, settled**: every byte-string prefix, its status, its carriers, what the draft does to RFC 8610 Appendix G and RFC 8949 Section 8, and the residual mismatch with CDDL | the table and the verdicts are **ours**; every `quote:` is the draft's own words and is checked as a contiguous span of the source. RFC 8610 and RFC 8949 were **not read**; they are cited from this library's `rfc-8610` record |
| `grammar-gaps.derived.txt` | derived | **32 enumerated side conditions and defects** (G‑01…G‑32) a conforming tool must carry beyond the ABNF, each with a locator and a STATIC / INSTANCE / NOT-CHECKABLE / DEFECT verdict. `G‑31` and `G‑32` were found by the cross-check pass | it is a list, not an implementation, and the verdicts are ours. The claims WERE run through an ABNF recogniser by the cross-check pass — see *State* — but no CDN implementation was used and `G‑08`'s PEG ordering is still unchecked |
| `README.md` | — | this file | — |

## The byte-string prefix question (library#39)

This library's `rfc-8610` extraction found an unreconciled conflict inside
RFC 8610: Appendix G.2 (normative) names **four** EDN byte-string prefixes —
`h`, `b32`, `h32`, `b64` — while Section 3.1 (normative) and the Appendix B
grammar's `bsqual = "h" / "b64"` admit **two**. #39 assigns EDN the test-vector
role, so a vector written `b32'…'` would be valid EDN and not a valid CDDL
literal.

**This draft RESOLVES it, by narrowing to two and retiring the text that said
four.** It does so twice over:

1. It **obsoletes the wider text.** The header reads `Updates: 8610, 8949 (if
   approved)`, and Section 1 says it "updates RFC8949 by obsoleting Section 8 of
   RFC 8949 [STD94], and [RFC8610] by obsoleting Appendix G of [RFC8610]". The
   four-prefix list lived in Appendix G.2. Obsoleting Appendix G removes it.
2. It **defines exactly two** base-encoding prefixes. Section 3.1: "prefixed by
   »h« for base16 or »b64« for base64 or base64url". Of `b32` and `h32` it says,
   in an aside: "This has not been implemented widely and therefore is not
   directly included in this specification."

So the notation converges on the **CDDL side** of the old conflict. The prefix
sets now agree, and both survivors are mandatory to implement (Section 3: "the
app-extensions h, b64, t1, b1, dt and ip are mandatory to implement").

**Three things that are easy to get wrong, and matter for vectors:**

- **`b32'…'` still PARSES.** `app-prefix = lcalpha *lcldh` admits any
  `[a-z][a-z0-9-]*` string. What rejects it is Section 5.1 — an app-extension
  "not known or not implemented by the ingesting process" is "usually an error
  and processing has to stop" — a *resolution* rule, one layer above the parse.
  **Do not use an ABNF check as a prefix allowlist.**
- **`b32` and `h32` are Reserved in Table 8, which is not the same as defined.**
  `h` and `b64` carry the identical "Reserved | RFC8949" row. The reservation
  blocks the names from being reused for something else; Table 7 is the list of
  what has a meaning, and `b32`/`h32` are absent from it.
- **The prefix set agrees; the literal syntax still does not.** CDDL's byte
  string literal is `bytes = [bsqual] %x27 *BCHAR %x27` — a prefix and a
  *single-quoted* string. CDN admits three carriers for the same prefix: a
  single-quoted string, a **raw string** (`` h`12345678` ``) and a **sequence
  literal** (`h<<"…">>`), and says the app-extension "cannot distinguish"
  between them. `h'12345678'` is valid on both sides; `` h`12345678` `` is valid
  CDN and is not a CDDL literal. **A vector generator aimed at CDDL must emit
  the single-quoted form** — which is also what the draft's own "basic output
  format" picks: "uses hexadecimal representation (h'') for byte strings, not
  b64'' or embedded CBOR (<<>>)".

Full disposition, with locators and verbatim text, in
`byte-string-prefixes.derived.yaml`. **Caveat: this is an Internet-Draft.** The
resolution is a proposal until it is published; until then RFC 8610 Appendix G.2
is still in force and the conflict is still live. The two-prefix set is the
intersection and is safe under either reading.

## What the ABNF alone does not capture

`cdn.abnf` is the complete formal definition of CDN's **syntax**. It is not a
definition of CDN, and the draft is candid about it — Section 6.1 ends with
seven numbered interpretation items precisely because "the mapping of these
character strings into the generic data model of CBOR is not always obvious".
The full enumeration is `grammar-gaps.derived.txt`; the classes are:

1. **The raw-string rules are carried by comments.** `rawdelim`,
   `startrawdelim`, `alikerawdelim` and `shortrawdelim` all have the same
   right-hand side, `1*"\``"`, and are told apart only by ABNF comments on
   delimiter width. Section 6.1 item 7 says so and prints PEG predicates. **A
   parser generated from the ABNF alone will mis-parse every raw string.** Two
   further rules — strip one leading newline, else strip one leading and one
   trailing space — are applied *after* parsing and are nowhere in the grammar.
2. **Registration is not syntax.** The grammar admits any lowercase prefix and
   any encoding indicator (`spec = ["_" *wordchar]`). Which prefixes resolve is
   the Section 7.1 registry's business; which indicators mean anything is
   Section 7.2's; `_4`…`_7` are reserved by Section 4.1. None of it is in
   Figure 1.
3. **PEG, not BNF.** Section 6 states the figures "are intended to be useful in
   a Parsing Expression Grammar (PEG) parser interpretation". Ordered choice is
   load-bearing: `number` must try `hexfloat` before `hexint`, `item` must try
   `tagged` before `number`, and `simple-number` is a hand-ordered
   longest-match ladder. ABNF notation cannot say so.
4. **The Section 6.2 grammars run on *decoded* text.** They parse the string
   after escape processing *and* after Section 1.3.5's carriage-return removal.
   Section 6.2 states the first; the second appears only inside an ABNF comment
   in Figure 2 — `lblank = %x0A / %x20  ; Not HT or CR (gone)`. "(gone)" is the
   whole statement.
5. **Prose and grammar disagree twice, in opposite directions.** Section 2.6
   admits `simple()` with any `0|[1-9][0-9]*`, so `simple(25)` and
   `simple(1000)`; `simple-number` admits 0–23 and 32–255 and nothing else.
   Conversely `string1 = (tstr / bstr) spec` admits a bare `_` on any string,
   while Section 4.1 allows it "only … behind the opening brace/bracket for map
   and array", reserving `''_` and `""_` for the no-chunks case.
6. **Case sensitivity is mixed and almost undocumented.** ABNF double quotes are
   case-insensitive, so `0X1267`, `0O11147` and `1E5` are legal CDN; `%s"NaN"`
   and `%s"true"` are case-sensitive, so `NAN` and `TRUE` are not. The figure
   carries exactly one note about this, and it is about hex digits.

## Defects and internal inconsistencies, recorded not repaired

Reported here because `docs/extraction.md` forbids repairing them in a verbatim
file. Full detail and locators in `grammar-gaps.derived.txt`.

- **Figure 8 silently drops two alternatives from `bstr`.** Section 6.3
  introduces it as an instruction to "add an alternative to bstr", but what it
  prints is a full redefinition that omits `app-rstring` and `rawstring`:

  ```
  Figure 1 (source 2423-2425):
     bstr            = app-string / sqstr / app-rstring / rawstring
                     / app-sequence / embedded
                       ; note: rawstring is text; app-... can be any type

  Figure 8 (source 3092-3093):
     bstr            = sq-app-string-dt /
                       app-string / sqstr / app-sequence / embedded
  ```

  A parser assembled as Figure 8 instructs **loses raw string literals
  entirely**, and loses them silently, because the result is still a closed
  grammar. Raw strings are a headline feature of this draft (Section 2.3.3) and
  Table 3 shows `` dt`…` `` as an equivalent form. (G‑16)
- **Section 6.3 understates its own dependencies.** It says the integrated
  grammars need "common definitions in Figures 2 and 9". Checked mechanically:
  Figure 9 references `DIGIT1`, `HEXDIG1` and `ODIGIT`, and Figures 11–14
  reference `alikerawdelim`, `ellipsis`, `eol-comment`, `shortrawdelim` and
  `startrawdelim` — none of which Figure 2 defines. **All eight live only in
  Figure 1.** (Pass 1 said six, omitting `ellipsis` and `eol-comment`; the
  cross-check pass re-derived the closure of the integrated set against the
  verbatim files and got eight.) (G‑17)
- **Eight rule names are defined more than once with different right-hand
  sides**, across figures a reader is told to combine. Twenty-four names are
  defined twice or more; sixteen identically. (Pass 1 counted nine differing and
  fifteen identical, putting `ellipsis` among the differing ones although its two
  definitions differ only in an ABNF comment. The cross-check pass re-derived the
  split by parsing the verbatim files figure by figure: **24 names redefined, 16
  identically, 8 differently** — `ALPHA`, `S`, `bstr`, `comment`, `non-lf`,
  `non-slash`, `non-slash-star`, `non-star`.) The `blank`/`lblank` family (`S`,
  `non-lf`, `non-slash`, `non-slash-star`, `non-star`) differs *deliberately* —
  Figure 1 parses source where HT and CR may appear, Section 6.2 parses decoded
  content where they cannot — but the draft never namespaces the two sets.
  (G‑18)
- **Three rules in Figure 1 are defined and never referenced.** `one-item` is a
  second plausible **start symbol** and no sentence says which of `seq` and
  `one-item` is the root. `newline = [%x0D] %x0A` is referenced nowhere in any
  of the fourteen figures. `lblank` belongs to the Section 6.2 grammars, where
  Figure 2 defines it identically. (G‑19)
- **Ellipses work inside `h''` and not inside `b64''`.** Figure 3 admits
  `ellipsis`; Figure 4 does not. Section 5.2 relies on the `h` form —
  `"signature": h'4711...0815'` — without noting the asymmetry. (G‑20)
- **`b64dig` mixes both RFC 4648 alphabets in one rule**, so `b64'-_+/'` parses.
  Section 3.1 justifies accepting either alphabet because they "have the same
  meaning where they overlap" — but those four characters are exactly where they
  do *not* overlap. (G‑21)
- **`bstr` holds text-string forms.** `rawstring` and `app-rstring` denote text
  strings and sit under a nonterminal named `bstr`. The rule's own comment
  admits it: `; note: rawstring is text; app-... can be any type`. (G‑25)
- **A production is cut in half by a page frame.** `hexscalar-s` begins at source
  line 2514 and its last two alternatives, `/ "7F"` and `/ HEXDIG1`, fall after
  the page 45/46 frame at lines 2525‑2526. Read one page and the rule is
  truncated. `cdn.abnf` keeps both halves; `cdn-dedented.derived.abnf` joins
  them. A rendering defect, not a grammar defect. (G‑24)
- **Figure 7 carries a typo and an unfilled placeholder inside its ABNF
  comments**: `IPv4adress` (one `d`) and `[RFC XXXX]`. It also uses
  `path-empty = 0<pchar>`, RFC 5234 prose-value notation that several ABNF tools
  reject, and carries four rules defined and never referenced. (G‑22, G‑23)
- **Two app-extension names are provisional.** Section 3.5 opens with a cref
  marked for removal before publication: `t1` and `b1` are "placeholders … while
  the actual names are still being decided by the WG". Both are in the
  mandatory-to-implement set. The document's opening cref says the same of the
  CDN name itself. (G‑29)

**One thing this draft gets right that RFC 8610 did not:**
`NONASCII = %x80-D7FF / %xE000-10FFFF` correctly **excludes** the surrogate
range U+D800–U+DFFF. The sibling record `rfc-8610` records the opposite finding
as its G‑32 — `SCHAR`, `BCHAR`, `PCHAR` and `SESC` all span `%x80-10FFFD` and
admit surrogates.

## Not held here

The Section 7.3 media-type template (`application/cdn`) and the Section 7.4
CoAP Content-Format request are captured in `../normative.md` rather than as
schema files; they are registration templates, not grammars. Tables 1–6 are
example tables and belong to `../examples/`, not here; Table 7 is held because
it is the definitive list of prefixes, and Tables 8, 9 and 12 because they are
registry content a tool must honour.

## State

**All three passes complete for this directory** — extract, verify, cross-check,
each at effort max. What was established mechanically, by script, against the
cached source:

- **All 23 verbatim regions across 13 files are byte-identical to the source
  lines their headers name**, verified by re-reading each written file and
  comparing region by region. Each region carries its own sha256 (digest
  convention: the region's source lines joined by `\n`, no trailing newline).
- **Figure 1 is closed.** 85 productions, no duplicate names; 82 distinct names
  referenced and every one resolves inside the figure or to an RFC 5234 core
  rule. Closure holds **across** the three page frames, which is an independent
  proof that no rule was lost at a frame.
- **`cdn-dedented.derived.abnf` round-trips exactly.** Re-indenting it by three
  columns reproduces the four verbatim regions of `cdn.abnf` line for line, and
  the generator aborts if it does not.
- Per-figure production counts: Fig 2 = 7, Fig 3 = 10, Fig 4 = 4, Fig 5 = 14,
  Fig 6 = 9, Fig 7 = 37, Figs 8–10 = 12, Figs 11–14 = 26. Re-derived figure by
  figure by the cross-check pass from the BEGIN/END region labels: all eight
  agree, 204 productions across the fourteen figures.
- Every `quote:` in `byte-string-prefixes.derived.yaml` (13 of 13) is a
  contiguous span of the whitespace-normalised source.

**AND NOW, A PARSE.** The cross-check pass (2026-10-19) wrote an RFC 5234 ABNF
reader and a memoised set-of-end-positions recogniser, pointed it at `cdn.abnf`
itself — stripping the `;` headers and the three-column margin in the reader, so
the grammar under test is this directory's own bytes — and ran the corpus
through it. Results:

- **`cdn.abnf` loads as 85 productions with 82 distinct names referenced, 0
  unresolved and exactly three unreferenced** (`lblank`, `newline`, `one-item`).
  Independently reproduced; `cdn-dedented.derived.abnf` yields the same 85 rules
  in the same order with identical right-hand sides, which is a second,
  stronger round-trip than the line-for-line one.
- **242 of the 251 vectors in `../examples/vectors.yaml` parse**; 246 with the
  line terminator the document's own lines carry. The nine that do not are the
  six `expect: invalid` vectors whose `violates` already names a §6.1
  production, and three §2.3.1 vectors that end in an end-of-line comment
  (G‑31). Full result in `../examples/README.md`.
- **The start symbol does not matter for this corpus.** `seq` and `one-item`
  give the same verdict on all 251, and diverge on exactly one input in the
  whole set — `//` with its newline, which `seq` accepts as an item-less
  sequence and `one-item` rejects. That is the practical size of G‑19's defect.
- **56 parse claims made in this file and in `grammar-gaps.derived.txt` were
  run as tests, and all 56 hold** — `b32'…'`, `nosuch'x'`, `pragma'y'` and
  `true'x'` parse; `simple(25)`, `simple(31)`, `simple(1000)` and `simple(256)`
  do not while `simple(23)`/`simple(32)`/`simple(255)` do; `0X1267`, `0O11147`,
  `0B1001`, `1E5` and `0x1.8P0` parse while `NAN`, `TRUE` and `INFINITY` do
  not; `h'00'_`, `'A'_`, `"A"_`, `''_` and `""_` parse; HT parses between
  tokens and not inside a string literal; DEL parses inside a quoted string and
  not inside a raw string; a lone surrogate is rejected and U+D7FF/U+E000
  accepted; `(_ h'01', "foo")` and `(_ "foo", "bar")` parse; and against
  Figures 2+3 and 2+4, `4711...0815` parses as `h` content while `47...08` does
  not parse as `b64` content, which is G‑20 observed rather than reasoned.

**Still not done:** no CDN implementation was used — none is installed in this
environment — so no conformance claim is made about any tool. The recogniser is
a plain backtracking ABNF recogniser, *not* a PEG: where ordered choice is
load-bearing (G‑08) it accepts the union, which is the right instrument for
asking what the grammar as written admits and the wrong one for asking what a
§6-conforming PEG parser would do. The raw-string delimiter widths (G‑01) are
not in the ABNF at all and were hand-coded in two modes, lenient and the §6.1
item 7 PEG reading; no vector distinguishes them.
