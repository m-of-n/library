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

**State: pass 1 of 3 complete.** Two agents in parallel at effort max, each
reading only `.cache/draft-ietf-cbor-edn-literals.txt`. **The verify and
cross-check passes have NOT run**, so this record carries no `profile`.
Readable; nothing may be built on it. library#39 owns finishing it.

Source: *Concise Diagnostic Notation (CDN)*, `draft-ietf-cbor-edn-literals-27`.
Header: `Updates: 8610, 8949 (if approved)`.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 215 verbatim bullets and 31 fenced blocks in 37 exact source line runs — 14 ABNF figures, 12 tables, §6.1's numbered items, both registry field blocks, the media-type template. 37/37 fences byte-identical by per-fence sha256; 215/215 bullets contiguous; 0 locator failures; and bullets reconciled one-to-one against `requirements.yaml` for text, locator, order and completeness |
| requirements | `requirements.yaml` | 215 entries, `R-0001`–`R-0215`, source order, no gaps: **10 stated, 205 inferred**. Counts reconcile 10 = 10. A 5.8 KB reconciliation states the real baseline — see below |
| schema | `schema/` | **13 verbatim across 23 regions, 3 derived.** Every verbatim region re-read and compared byte-for-byte with its line range and sha256 in the file header. Figure 1's closure verified: 85 productions, 0 duplicates, 82 names referenced and all resolving — and it **holds across all three page frames**. `cdn-dedented.derived.abnf` round-trips exactly |
| messages | `messages.yaml` | 35 literal forms, 84 fields, 290 requirement references, 0 dangling |
| examples | `examples/` | **251 vectors**, 242 valid / 9 invalid. 50 hex sequences the document printed were decoded and confirmed; **1 was printed and is wrong**; 174 are ours and marked `COMPUTED HEX.`; 26 carry no hex with a stated reason. 61 printed byte sequences were independently re-encoded from the EDN — 59 matched, 2 did not |
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

1. **`b32'…'` still parses.** `app-prefix = lcalpha *lcldh` admits any
   `[a-z][a-z0-9-]*`, so it is a well-formed `app-string`; what rejects it is
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

## Why 10 keywords in 168 KB is the right answer

Like `rfc-8610`, this is a **notation**: its normativity is a grammar and a set
of literal meanings, not obligations on an actor. §6 is 340 lines of ABNF in 14
figures and carries **no BCP 14 keyword at all**. Only two of the ten are
obligations and both are narrow; the single MUST NOT bounds an *optional*
feature; and four of the five MAYs are one permission restated in four
contexts. **No keyword in this document constrains the notation itself.** The
reconciliation says what was counted instead — literal forms, grammar side
conditions, explicit disclaimers of capability, the removals relative to
RFC 8610 Appendix G and RFC 8949 §8, registry rules, and the lower-case force
words the document actually uses.

## Source defects found

Full enumeration in `schema/grammar-gaps.derived.txt` (G-01…G-30). The ones
that would bite an implementer:

1. **Figure 8 silently drops two alternatives from `bstr`.** §6.3 introduces it
   as "add an alternative to bstr", but prints a full redefinition that omits
   `app-rstring` and `rawstring`. A parser built as Figure 8 instructs **loses
   raw string literals entirely and silently**, because the result is still a
   closed grammar — and raw strings are a headline feature of §2.3.3.
2. **§6.3 understates its own dependencies**, naming Figures 2 and 9 as the
   common definitions when six referenced names (`DIGIT1`, `HEXDIG1`, `ODIGIT`,
   `startrawdelim`, `alikerawdelim`, `shortrawdelim`) appear only in Figure 1.
3. **§4.1 Table 6's major-type-3 row prints the wrong bytes.** `"A"_1` is given
   as `79000161` / `6161`; `0x79` is mt3 with a two-byte length, so with
   content `"A"` (`0x41`) the correct bytes are **`79000141` / `6141`**. The
   printed bytes encode `"a"` — almost certainly copied from the row above,
   where a one-byte *byte* string's head and content both read `0x41` and so
   coincide. Found by round-tripping, and independently re-derived.
4. **A production is cut in half by a page frame**: `hexscalar-s` loses
   `/ "7F"` and `/ HEXDIG1` across the page 45/46 boundary. Read one page, get
   a truncated rule.
5. Nine rule names are redefined with differing right-hand sides across figures
   a reader is told to combine; three rules in Figure 1 are dead, one of them
   (`one-item`) a **second plausible start symbol** with no sentence saying
   which is the root.
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
