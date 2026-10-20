---
schema: "library-summary/v1"
id: draft-ietf-cbor-edn-literals
record: draft-ietf-cbor-edn-literals
type: summary
updated: "2026-10-19"
---

# Concise Diagnostic Notation (CDN)

|  |  |
|---|---|
| **Type** | draft |
| **Maturity** | draft — IETF CBOR WG, intended status **Standards Track**, `Updates: 8610, 8949 (if approved)` |
| **Authors** | C. Bormann (Universität Bremen TZI) |
| **Published** | 20 July 2026 (revision -27); expires 21 January 2027 |
| **Identifier** | draft-ietf-cbor-edn-literals-27 |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-cbor-edn-literals-27.txt |
| **Digest** | `43cfb1236435a9de62d3c202b7ee653b0f5adbd40d3800bbb9379379dbdbf7e9` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

CDN is the notation CBOR data is written in for people: in specifications, on
whiteboards and for entering test data. This draft replaces every previous
description of it — §1: "It updates RFC8949 by obsoleting Section 8 of
RFC 8949 [STD94], and [RFC8610] by obsoleting Appendix G of [RFC8610]" — and
renames it from "diagnostic notation" to CDN.

Beyond the JSON-like core it adds **prefixed literals**: `h'…'` and `b64'…'`
for byte strings, `dt'…'` for dates, `ip'…'` for addresses, `t1`/`b1` for
tags, plus raw strings (`` h`1234` ``), embedded-CBOR sequences (`<<…>>`),
encoding indicators (`_1`, `_2`) that pin a specific wire form, and four
comment syntaxes. Six app-extensions are mandatory to implement. §2 claims it
is "a true superset of JSON as it is defined in [STD90] in conjunction with
[RFC7493]".

Its own scope statements are narrow and matter: §1 says CDN "is not designed or
intended for general-purpose use in protocol elements exchanged between systems",
§1.3 and §2 both quote STD 94's "All actual interchange always happens in the
binary format", and §7.3 registers the media type with Intended usage
**LIMITED USE**.

Structurally it is a grammar, not a set of obligations: §6 is 340 lines of ABNF
across 14 figures and carries **no BCP 14 keyword at all**. The whole document
has ten, of which only two are obligations.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Encoding | supporting | How our test vectors and spec examples get written down; it constrains nothing on the wire. |
| Security | supporting | Only indirectly — a notation that silently parses as a *different* schema language is a review hazard, which is the main finding below. |

**library#39 assigns CDN the test-vector role. The extraction's verdict is that
it cannot carry it — and the document says so first.** §1.3.2: "a deterministic
representation is not defined for CDN. More generally speaking, there is no
expectation for 'roundtripping': Converting CDN to binary CBOR and back to CDN
will generally not achieve exactly the same result as the original input CDN."

The decisive clause is §4. A conforming consumer "MUST accept" encoding
indicators, where the same sentence defines *accept* as "process **or
ignore**". So **a vector whose entire point is a non-preferred encoding cannot
be stated in CDN in a form every conforming consumer must honour** — and that
is most of our corpus. There is no map-ordering rule either (§1.3.3 makes
deterministic ordering an optional extra feature), over-precise floats are
silently rounded to binary64 rather than rejected, and big integers silently
become tag 2/3.

**The rule adopted, and written into the artifacts: `hex` is normative, `edn`
is commentary.** Our vector sets keep CDN in the `diagnostic` column for human
readers and treat the bytes as the authority.

## Implementations

The draft names none and has no implementation-status section. Its own
reference points are the `cbor.me` / `cbor-diag` family that long predate it.
*Searched on 2026-10-19; no named CDN implementation in the document.* Two
stability risks worth knowing before depending on any: `t1` and `b1` are
explicitly **provisional** names although both are mandatory to implement, and
`CPA888`/`CPA999` are **unassigned placeholders** — do not hard-code 888 or 999.

## Limits

- **Four CDN comment and separator forms parse silently as valid CDDL with a
  different meaning.** `# alg` hits CDDL's `"#"` any-type; `// alg` hits its
  group-choice operator; `[_ 1, 2]` is two elements in CDN and a three-entry
  group in CDDL; `[1 ... 3]` is a three-element array in CDN and the
  **exclusive range 1..2** in CDDL. The draft's own Appendix A example parses
  as valid CDDL with six group entries where CDN sees a one-entry map — and its
  advice to "always validate formal language instances with tools" does not
  help, because *both* tools succeed. This is the single most dangerous
  property for us, because our vectors and our schemas sit in the same files.
- **The byte-string prefix conflict is resolved, but not structurally.** §3.1
  defines exactly `h` and `b64`, declining `b32`/`h32` as "not implemented
  widely" — so CDN converges on the two that CDDL's `bsqual` already admitted.
  But `b32'…'` **still parses**, because `app-prefix = lcalpha *lcldh`; only
  §5.1's resolution rule rejects it, one layer above the grammar, where CDDL
  makes it a syntax error. **Never use an ABNF check as a prefix allowlist.**
  And the prefix sets agree while the **literal syntax does not**: CDDL takes a
  single-quoted string only, CDN also admits raw and sequence carriers, so our
  generator must emit the single-quoted form — which is also §1.3.3's own basic
  output format.
- **§7.1's registry contradicts §6.2's table**, listing `h`, `b32`, `h32` and
  `b64` with an identical "Reserved / RFC8949" row, pointing `b32` at a section
  this draft obsoletes.
- **It is an Internet-Draft** — `(if approved)`. Until it publishes, RFC 8610
  Appendix G.2 is still in force and the four-versus-two conflict is still
  live. `{h, b64}` is the intersection and is safe under both readings.
- **Figure 8 silently breaks any parser built from it.** §6.3 introduces it as
  "add an alternative to bstr" but prints a full redefinition omitting
  `app-rstring` and `rawstring`, so raw string literals — a headline feature of
  §2.3.3 — vanish. Silently, because the result is still a closed grammar.
- **§4.1 Table 6's major-type-3 row prints the wrong bytes**: `79000161` /
  `6161` for `"A"_1`, where mt3 with a two-byte length and content `"A"`
  (`0x41`) gives **`79000141` / `6141`**. The printed bytes encode `"a"`,
  almost certainly copied from the row above where a one-byte *byte* string's
  head and content both read `0x41` and so coincide. Found by round-trip and
  independently re-derived.
- **CDN cannot satisfy `R-O-03`.** That requirement wants a canonicalisation
  algorithm cited rather than invented; §1.3.2 says CDN has none to cite. So
  canonicalisation belongs one level down, in the CBOR — and nobody should diff
  two `.cdn` files instead of two byte strings.
- **An end-of-line comment needs its newline, so a CDN text cannot *end* with
  one.** `comment = … / eol-comment *non-lf %x0A` makes the LF mandatory and
  offers no end-of-input alternative, so `1 # done` does not parse while the
  same line followed by a newline does. Three of the draft's own §2.3.1
  examples are such lines. Found by running the grammar; recorded as `G-31`.
- **§6.1 names no start symbol.** `seq` and `one-item` are both plausible
  roots, `one-item` is referenced nowhere, and no sentence says which is the
  root. It makes no difference to any of the 251 vectors — the two differ only
  on item-less and multi-item input — but a tool has to choose. (`G-19`.)
- Eleven quoted requirement spans sit on mid-token hyphenation breaks and two
  sentences cannot be quoted whole; a page frame also cuts §2.4.1's
  mandatory-separator sentence in half, and fifteen quotations in the vector set
  had silently healed such a break before the verify pass restored the source's
  bytes. The full enumeration — thirty-two side conditions and defects,
  `G-01`…`G-32` — is in `distilled/schema/grammar-gaps.derived.txt`.
- The extraction is **complete at FX-1 `profile: full`** — extract, verify and
  cross-check, each at effort max — but **no human has reviewed it**: every
  `reviewed_by` is empty.

## One thing it gets right that RFC 8610 does not

`NONASCII = %x80-D7FF / %xE000-10FFFF` correctly **excludes the surrogate
range**. This library's `rfc-8610` record documents the opposite for CDDL's own
grammar, where `SCHAR`, `BCHAR`, `PCHAR` and `SESC` all span `%x80-10FFFD` and
therefore admit U+D800–DFFF although §3.1 mandates UTF-8.

## A note for the encoding ADR

CDN answers the two largest objections to YAML as MD-3's human form: it has
**no barewords at all**, which kills the `no` → `"no"` implicit-typing problem,
and it distinguishes `'x'` from `"x"`, which kills the byte-string
non-injectivity the `rfc-8949` extraction calls "the item most likely to sink
the Oct 28 package". Scored against our own withdrawn ten-item YAML profile,
four items are satisfied by construction and three are contradicted. That does
not reopen MD-3 — but the ADR now has to say *why YAML rather than CDN*, since
§1.3.1 states CDN's purpose as exactly the job MD-3 hands to YAML.
