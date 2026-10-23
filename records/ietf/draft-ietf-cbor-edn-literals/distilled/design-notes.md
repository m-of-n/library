---
record: draft-ietf-cbor-edn-literals
kind: design-notes
title: "draft-ietf-cbor-edn-literals — bearing on our design"
extracted: "2026-10-19"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§3.1`) are `draft-ietf-cbor-edn-literals-27`, "Concise Diagnostic Notation
(CDN)", 20 July 2026. Other documents are named (`RFC 8610 §3.1`). Our own
documents are cited by id (`ARCH-0002 P5`, `MD-3`, `R-O-03`). Three markers
distinguish voices:

- unmarked prose reports **the source** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project, or a claim in a
  sibling record of this library, that the sources do not support.

**Naming.** The document renames EDN to **CDN**. `library#39` and our own
documents say "EDN". They are the same language: §1 says diagnostic notation
"is now specified by this document, obsoleting all these previous descriptions,
and is known as Concise Diagnostic Notation (CDN)". This file says CDN when
reporting the source and EDN when reporting us. Note the cref at the head of the
draft: it "does not have WG input yet on any renaming decisions (CDN name, b1/t1
name)", so the name itself is not settled.

**Decision status, stated plainly.** DEC-002 in `ARCH-0001` §7 lists **four**
options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3; that proposal is unmerged. `ADR-0001`
(accepted) constrains DEC-002. `MD-3` (2026-09-28) **narrowed** DEC-002 to
option 5 and named YAML as the human form; `DECISIONS-0001` item 2 says in terms
that "a narrowing is not an acceptance, and no ADR exists". **Nothing below may
be read as an accepted encoding decision**, and *Mapping to our decisions* §4,
"Where this cuts against MD-3", is written to be read by someone who has not
yet decided.

**Document status.** This is an Internet-Draft at revision **-27**, expiring 21
January 2027, carrying unresolved WG cref notes and two **unassigned** tag
numbers written `CPA888` and `CPA999` (§5.1, §5.2, §7.5). Anything we build on
the elision or unresolved-extension machinery will change at publication.

---

## What we adopt

**CDN as the notation for the `edn`/`diagnostic` column of our vector sets, and
only for that column.** §1 states the role precisely: "The interchange format
created by standardizing CDN is not intended to compete with the actual binary
interchange format CBOR, but enables the use of a shared diagnostic notation in
tools for and in documents about CBOR. However, between tools for CBOR
development and diagnosis, document generation systems, continuous integration
(CI) environments, configuration files, and user interfaces ... CDN is often
'interchanged'." That is exactly our use: a library of vector files under source
control, read by people and by CI. §2 repeats RFC 8949's line unchanged: "All
actual interchange always happens in the binary format."

**The lexical type distinctions, which are the reason to prefer CDN over YAML
for this job.** §2.3 fixes four literal forms that a reader can tell apart
without a schema:

| form | §ref | denotes |
|---|---|---|
| `"x"` | §2.3.1 | text string, major type 3 |
| `'x'` | §2.3.2 | byte string, major type 2 |
| `` `x` `` | §2.3.3 | text string, no backslash processing |
| `h'…'` / `b64'…'` | §3.1 | byte string from base16 / base64 |

**[analysis]** This retires, for a CDN vector file, the single largest hazard
the `rfc-8949` extraction identified in MD-3's YAML human form: "YAML has no
byte type; CBOR's major type 2 is distinct from major type 3 'even if composed
of the same bytes' (§5.6.1). Without an unambiguous YAML spelling for bytes, a
text string and a byte string share one YAML scalar and the mapping is **not
injective** — which defeats canonicality outright." In CDN the distinction is in
the quote character. §1.2 makes the point in the source's own words: "true,
"true", 'true', and `true` are all different literals in CDN and should not be
confused" — four spellings, three distinct CBOR items, no schema consulted.
Vectors `V-0001`–`V-0004` are that sentence as fixtures.

**No barewords, therefore no implicit typing.** §6.1's `item` production admits
`map / array / tagged / number / simple / string / streamstring` and nothing
else; `simple` is the four case-sensitive keywords plus `simple(n)`. There is no
production that turns an unquoted word into a scalar. **[analysis]** The
withdrawn YAML profile (`ARCH-0001-PROPOSAL-v0.2.0` Appendix A) asks for
"schema-driven typing, so a field declared textual makes `no` the string
`"no"`". CDN does not need the schema: `no` is a syntax error and `"no"` is the
string. The second-largest YAML hazard disappears the same way the first did.

**Comments as blank space, with the hazard the source itself names.** §2.1 gives
four comment forms, all of which "can be used where the syntax allows blank
space". They leave no trace in the data item — §2.1's `/grasp-message/` example
"reduces to [1, 10584416, ["opsonize", 7, 105]]" (`V-0009`, `V-0010`). The
withdrawn YAML profile says "Comments would be stripped and unsigned, which is
why a YAML surface was never a good home for meaning". CDN has the identical
property and §5.2 states the identical warning: "The consumer of this CDN will
ignore the comments and therefore will have no idea after ingestion that some
information has been elided; validation steps may then simply fail instead of
being informed about the elisions." We adopt comments for annotating vectors and
adopt the rule that nothing load-bearing goes in one.

**§1.3.3's "basic output format" as the specification of our rendering
direction.** It is a four-item list: looks like JSON where possible; inserts
encoding indicators "only where the binary form differs from Preferred
Serialization"; "uses hexadecimal representation (h'') for byte strings, not
b64'' or embedded CBOR (<<>>)"; no elaborate pretty-printing but ordinary spaces
after `,` and `:`. **[analysis]** `R-O-05` (proposed) requires that "Any
human-facing form SHALL be regenerated from verified canonical bytes". §1.3.3 is
a citable, already-written specification of what that regeneration should
produce, which is a thing we would otherwise have to invent. It is the one place
in this document that discharges work `R-O-05` creates.

**`dt''` — the one app-extension a no-tags profile can use unchanged.** §3.2:
the lowercase prefix yields a plain number, "In the all-uppercase variant of the
app-prefix, the value is enclosed in a tag number 1." So `dt'1969-07-21T02:56:16Z'`
is the integer `-14159024` and nothing else (`V-0130`). The withdrawn YAML
profile asks for "RFC 3339 UTC timestamps with integer seconds"; `dt''` is that,
with the RFC 3339 grammar supplied in §6.2.3 and the untagged result option 5
needs. Note the trap in the same table: `dt'…16.0Z'` is a **float**
(`V-0131`), because §3.2 makes a `time-secfrac` switch the result type. A
profile that forbids floats must forbid the fractional form, not merely avoid
it.

**RFC 8949's well-formed/valid distinction, inherited by reference.** §2 points
at "Section 5.3 of RFC 8949 ... with basic validity discussed in Section 5.3.1"
and splits the two basic-validity cases across §2.3.5 (UTF-8) and §2.4.2
(duplicate map keys) — the same two `ARCH-0002` P5 adopts, which takes RFC
8949's full three-level hierarchy. §2.4.2's `{1: "to", 1: "from"}` (`V-0102`) is a
ready-made negative fixture for the duplicate-key rule P5 requires us to state.

---

## What we adapt, and how

**The round-trip direction. We use CDN → CBOR only, and never the reverse as an
equality test.** §1.3.2 is unambiguous and is the single most important sentence
in the document for `library#39`:

> “Because of this, a deterministic representation is not defined for CDN. More
> generally speaking, there is no expectation for "roundtripping": Converting
> CDN to binary CBOR and back to CDN will generally not achieve exactly the same
> result as the original input CDN.”

**[analysis]** Our vector sets pair a notation with bytes. That is sound only if
the notation→bytes direction is a function and the bytes are the authority. It
is, and they are: the `hex` column is normative in our files and the `edn`
column is the human's view. What we must never do is compare two CDN texts for
equality, or regenerate CDN and diff it against the authored CDN — the document
says that will fail, and §3.8's own worked example proves it (`V-0198`
in, `V-0199` out: four input elements come back as four different spellings).

**Encoding indicators — adopted for the hex column's *explanation*, not relied
on as a contract.** §4.1's `_i`, `_0`–`_3` and `_` give the notation a way to
say which serialization variant a vector exercises, which is precisely what our
CDE / dCBOR / serialization vector sets are about. But §4 undercuts it:

> "To be able to process CDN that contains encoding indicators, a CDN-consuming
> implementation MUST accept them (i.e., process or ignore the presence or
> absence of each encoding indicator). It is RECOMMENDED to provide a warning
> for each encoding indicator value that is encountered but not further
> processed."

and “Implementations of CDN generally do not need to provide this functionality
in full; if they do, they can be called "diagnostic implementations".”

**[analysis]** "Accept" is defined as *process **or ignore***. So a conforming
non-diagnostic CDN consumer may discard `_0` and emit Preferred Serialization
instead, with at most a warning. **A vector whose entire point is a
non-preferred encoding therefore cannot be stated in CDN in a form every
conforming consumer must honour.** For us the consequence is a rule, not a
blocker: *in our vector files the `hex` column is the expectation and the `edn`
column is commentary; an indicator in `edn` is never the test.* This is also a
direct collision with `ARCH-0002` P5's "unknown is critical unless declared
otherwise" — §4 mandates the opposite default for its own extension point — and
it is a narrower collision than P5's one with RFC 8949 §5.4, because encoding
indicators carry serialization rather than data.

**The `h''` literal as our byte-string spelling, with its blank-space licence
used deliberately.** §3.1: "In the base-encoded byte string literals, blank
space is ignored in the input", and §6.2.1 adds comments inside the literal.
`V-0121` (`h'4 86 56c 6c6f\n  20776 f726c64'`) splits bytes across lines at
non-byte boundaries; `V-0123` annotates individual bytes with `/…/` comments.
**[analysis]** This is genuinely useful for a 32-byte digest or a COSE protected
header in a vector file — it is the feature §2.1's COSE key example exists to
show (`V-0011`). But it is a CDN-only licence; see *What we reject* on CDDL.

**Elision, adapted as a documentation device that must never reach a fixture.**
§5.2's `...` and the `CPA888` tag are for exposition — "it is often useful to be
able to leave out parts of a CDN document that are not of interest at that point
of the exposition" — and §5.2 says plainly that "Upon ingesting CDN as a
representation of a CBOR data item for further processing, the occurrence of an
ellipsis usually is an error and processing has to stop." **[analysis]** We
adopt ellipses for prose and `summary.md` excerpts and forbid them in
`vectors.yaml`, because the tag that carries them is unassigned and because a
vector containing one has no bytes. 26 of this record's 251 vectors have no
`hex` for exactly this reason.

**§3.4's `hash` extension — useful, and a registry dependency to notice.** §3.4
identifies the hash function "in the COSE Algorithms registry ... either by the
identifier (value: integer or string), or, if no algorithm is registered with
this value, by its name used in the registry", defaulting to −16 (SHA-256).
`hash<<'foo'>>` denotes the digest, not the input. **[analysis]** For
`ARCH-0001` `R-M-07` ("Artifact statements SHALL bind at least one content
digest") this is attractive: a vector could carry the *derivation* of a digest
rather than a copied constant, which is a class of transcription error removed.
Both of the document's digests were recomputed here and both are exact
(`V-0161`–`V-0168`), so the extension is sound as specified. The cost is that
the notation now depends on an IANA registry — a COSE one, not the tag one —
which is worth naming next to `ADR-0001`.

---

## What we reject, and why

**CDN as a canonical or signed form. It cannot be one, and the document says
so.** §1.3.2: "a deterministic representation is not defined for CDN". `R-O-03`
requires that a "Canonicalization algorithm for each concrete encoding SHALL be
cited, not invented silently". There is nothing to cite. **[analysis]** The
correct placement follows immediately: canonicalization belongs one level down,
in the CBOR, where `draft-ietf-cbor-cde` and `draft-ietf-cbor-serialization`
live; CDN is an *input* notation and a *display* notation and never the thing
that is hashed or signed. This must be stated, because the temptation to diff
two `.cdn` files instead of two byte strings is real and the failure is silent.

**Map ordering as something the notation can express.** CDN has no ordering
rule. §1.3.3 mentions "ensuring deterministic map ordering (Section 4.2 of RFC
8949 [STD94]) on output" only as an *additional* feature a generator may offer.
**[analysis]** So the key order in a CDN text is the order the author typed, and
whether the encoder sorts is a tool option. For the determinism vector sets —
where RFC 8949 §4.2.1 bytewise ordering versus §4.2.3 length-first *is* the
point — the `edn` column cannot carry the expectation and the `hex` column must.
A second reason the hex is normative in our files.

**Silent float precision adjustment.** §6.1 item 5: "the number range needs to
fit into an [IEEE754] binary64 (or the size corresponding to the encoding
indicator), and the precision will be adjusted to binary64 before further
applying Preferred Serialization". **[analysis]** A decimal literal carrying
more precision than binary64 is rounded, not rejected. For a test vector that is
silent corruption. Our rule: any float in a vector is written in a form that is
exact in its target width — hexadecimal float (`0x1.22102ap+15`, `V-0200`) or
`float'…'` (§3.8) — or it is not written in CDN at all. The document's own
`1.1_1`/`1.1_2` rows (`V-0044`, `V-0045`) show the *good* behaviour, where the
indicator forces an error rather than a round; without an indicator there is no
error.

**`undefined` and the open simple-value space, per P5.** §2.6 admits
`undefined` and `simple(n)` for every value the §6.1 `simple-number` production
allows (0–23 and 32–255). The `rfc-8949` design notes already exclude simple
value 23 under `ARCH-0002` P5, and `ARCH-0001-PROPOSAL-v0.2.0` §3.3 excludes the
registry. CDN gives us the spelling for everything we have decided not to use;
the profile, not the notation, says no.

**The deprecated `streamstring` syntax (§4.3).** "With this document, the
streamstring syntax is now deprecated; new CDN documents should instead use the
ilbs/ilts app-extensions (Section 3.6)". We write neither: option 5 rejects
indefinite lengths in both directions (`rfc-8949` design notes, determinism row
3), so `(_ …)`, `ilbs` and `ilts` are only ever *negative* fixtures for us.
`V-0218`–`V-0222` and `V-0185`–`V-0189` are those fixtures, and `V-0220` (`(_ )`)
is a rare case of a grammar encoding a semantic impossibility: §6.1's
`streamstring` carries the ABNF comment "note that there must be at least one
string to distinguish".

**Raw strings in authored vectors.** §2.3.3's backquote literals are an elegant
answer to "quoting hell", but their content is decided by two post-processing
rules — a leading newline is removed; failing that, one leading and one trailing
space are removed — and nothing removes a *trailing* newline, which this
extraction had to reason out rather than read (`V-0066`'s note). **[analysis]**
A notation whose value depends on which of two rules fired is a poor choice for
a file whose purpose is to be unambiguous. We read raw strings (the document
uses them) and author `"…"` and `h'…'`.

---

## Mapping to our decisions

### 1. The byte-string prefix conflict — settled

`rfc-8610`'s extraction (defect 13 in its `design-notes.md`) records that RFC
8610 contains an unreconciled contradiction. Verified here against the cached
RFC 8610 bytes, both halves hold:

- **RFC 8610 Appendix G.2 (normative):** "Diagnostic notation notates byte
  strings in one of the base encodings per [RFC4648], enclosed in single quotes,
  prefixed by >h< for base16, >b32< for base32, >h32< for base32hex, or >b64<
  for base64 or base64url." (Four. The `>…<` is the rendering artifact
  `rfc-8610` defect 14 reports; confirmed in the `.txt` our `content.sha256`
  pins.)
- **RFC 8610 §3.1 (normative):** byte strings "may be prefixed by "h" or
  "b64"", and RFC 8610 Appendix B has `bsqual = "h" / "b64"`. (Two.)

**What this document does: it resolves the conflict by deleting one side of it,
and lands on CDDL's number.** The abstract: "Replacing CDN's previous informal
descriptions, it updates RFC 8949, obsoleting its Section 8, and RFC 8610,
obsoleting its Appendix G." §1 repeats it: "It updates RFC8949 by obsoleting
Section 8 of RFC 8949 [STD94], and [RFC8610] by obsoleting Appendix G of
[RFC8610]. It is intended to serve as the single reference target that can be
used in specifications that use CDN." Both documents that named four prefixes —
RFC 8949 §8 and RFC 8610 Appendix G — are obsoleted together.

**What replaces them defines exactly two.** §3.1 is titled "Base-Encoded Byte
String Literals: h and b64" and the aside inside it is explicit:

> "(Note that Section 8 of RFC 8949 [STD94] also mentions »b32« for base32 and
> »h32« for base32hex. This has not been implemented widely and therefore is not
> directly included in this specification. These and further byte string formats
> now can easily be added back as prefixed literals.)"

§6.2 Table 7 lists `h` and `b64` and does not list `b32` or `h32`. §3 makes `h`
and `b64` two of the six mandatory-to-implement app-extensions. **So as of
draft-27 the defined CDN prefix set and CDDL's `bsqual` are the same two names.**

**But the agreement is coincidental, not structural, and the document says how
it will break.** Four facts, each with a locator:

1. §6.1's grammar is **open**: `app-prefix = lcalpha *lcldh`. `b32` matches it.
   So `b32'MZXW6'` is syntactically well-formed CDN with no defined value, and
   §5.1 governs it: "If an app-extension is not known or not implemented by the
   ingesting process, this is usually an error and processing has to stop",
   with `CPA999` as the alternative. CDDL's `bsqual` is a closed two-element
   alternation, so the same text is a **syntax error** there. The failure modes
   differ in kind, which matters for diagnosis.
2. §7.1 creates an **expert-review registry** for the prefix space, and §3.1
   invites the base encodings back into it ("can easily be added back"). The
   moment one is registered, CDN admits a byte-string prefix CDDL does not — the
   original conflict, rebuilt between two documents instead of inside one.
3. **Nobody has extended `bsqual`.** RFC 9682 — which this document names in
   §1.2 as part of what "CDDL" now means — rewrote CDDL's string-literal grammar
   and left `bsqual = "h" / "b64"` unchanged, saying only, in its Appendix B.2,
   that "the approach taken lends support to extending bsqual in CDDL similar to
   the way this is done for CBOR diagnostic notation in [EDN-LITERALS]". Support
   lent, not taken.
4. **[analysis] §7.1's own registry cannot tell the two pairs apart.** Table 8 gives
   `h`, `b32`, `h32` and `b64` the **identical** registry row — Description
   "Reserved", Reference "RFC8949" — even though this document defines `h` and
   `b64` in §3.1 and declines to define `b32` and `h32`. An implementer reading
   the registry alone cannot tell the two pairs apart, and `b32`'s row points at
   a document whose §8 this draft has just obsoleted. The registry contradicts
   §6.2 Table 7, which lists only `h` and `b64`.

**The answer for `library#39`, in one line:** *if our vectors are EDN and our
schema is CDDL, `h'…'` and `b64'…'` are safe today and are the only two safe
today; `b32'…'` and `h32'…'` must not be used; and the agreement is held in
place by nothing stronger than nobody having registered a third base encoding.*

**[analysis] One further prefix hazard that neither document states.** ABNF
double-quoted strings are case-insensitive (RFC 5234 §2.3 — a fact this draft
relies on, carrying the note "double-quoted strings as in "A" are
case-insensitive in ABNF" in Figures 1 and 2, and using `%s"…"` wherever it
wants case sensitivity). RFC 8610's `bsqual = "h" / "b64"` is written with plain
double quotes, so the CDDL grammar as written admits `H'1234'` and `B64'…'` and
reads them as base16 and base64. CDN pins case numerically — `lcalpha =
%x61-7A`, `ucalpha = %x41-5A` — and §6.2 Table 7 gives `H` and `B64` the entry
"(not used)", so in CDN those are undefined app-extensions falling to §5.1. The
same text is a byte string in one language and an error in the other. Our rule:
**lowercase prefixes only, always.**

### 2. Does CDN diverge from CDDL anywhere else? Yes — ten further places

`rfc-8610`'s extraction named two more divergences. Both survive this document,
and the comment one is much worse than recorded. The table below is checked
against RFC 8610 Appendix B as updated by RFC 9682 (cached in this library), and
against §6.1 Figure 1.

| # | CDN | CDDL | verdict |
|---|---|---|---|
| 1 | `0o11147` — §6.1 `octint = [sign] "0o" 1*ODIGIT` | `uint = DIGIT1 *DIGIT / "0x" 1*HEXDIG / "0b" 1*BINDIG / "0"` — no octal | **confirmed, unchanged**. `rfc-8610`'s claim stands; `V-0030` |
| 2 | four comment forms, all operators in CDDL — see below | `COMMENT = ";" *PCHAR CRLF` | **confirmed and much wider than recorded** |
| 3 | `+1`, `+0001` — `sign = "+" / "-"` on every numeric form | `int = ["-"] uint`; no `+` | **new here.** `V-0024`, `V-0025` |
| 4 | `001`, `000` — `decnumber` starts `1*DIGIT` | `uint = DIGIT1 *DIGIT / "0"` forbids leading zeros | **new here.** `V-0019`, `V-0023` |
| 5 | `3.` and `.3` — §6.1 item 3 states both | `number = hexfloat / (int ["." fraction] …)`, `fraction = 1*DIGIT` | **new here.** `V-0234`, `V-0236` |
| 6 | `Infinity`, `-Infinity`, `NaN` — `nonfin` | no literal; the prelude has no non-finite name | **new here.** `V-0040`–`V-0042` |
| 7 | `` `raw` `` strings (§2.3.3) | `text = %x22 *SCHAR %x22` only | **new here** (raw strings are introduced by this document) |
| 8 | `1(…)` for a tag; `uint` is decimal-only, no leading zeros (§2.5) | `#6.1(…)`; CDDL's `uint` admits `0x`/`0b` | **divergence in BOTH directions**: CDN cannot write a hex tag number, CDDL can |
| 9 | `<<…>>` embedded CBOR (§2.3.4) | `.cbor` control operator | named by the source, Appendix A |
| 10 | string literals admit raw LF and CR (`unescaped = %x0A / %x0D / …`), U+007F, and C1 controls (`NONASCII = %x80-D7FF / %xE000-10FFFF`) | `SCHAR` has no C0 at all, stops at `%x5D-7E`, and RFC 9682's `NONASCII = %xA0-D7FF / %xE000-10FFFD` | **new here.** A multi-line `"…"` is CDN-only; U+007F–U+009F and U+10FFFE–U+10FFFF are CDN-only |
| 11 | §1.3.5: CR "ignored as if they were not in the input wherever they appear … not copied into the resulting string" | RFC 8610 §3.1: in unprefixed byte strings "Whitespace is included literally"; `BCHAR` includes `CRLF` | **new here, and sharp.** The same literal containing a CRLF is one byte shorter in CDN |
| 12 | `[[][]]` is **not** CDN (§2.4.1, `V-0101`) | `a = [[][]]` is valid CDDL, as §2.4.1's own aside concedes | the one place CDN is stricter |

**The comment divergence is not "two syntaxes". It is four CDN delimiters, every
one of which is an operator in CDDL, and two of which are absorbed without an
error — the two this document added.** §2.1 gives CDN `/ … /`, `/* … */`, `# …`-to-EOL and `// …`-to-EOL.
Against RFC 8610 Appendix B:

| CDN comment | what CDDL does with the same characters | CDDL locator | outcome |
|---|---|---|---|
| `/ alg /` | `/` is the **type choice** operator, and it is **infix** — it cannot begin a group entry | `type = type1 *(S "/" S type1)`; `grpent = [occur S] [memberkey S] type` | **syntax error** where a CDN comment usually sits (leading position); absorbed into a type choice where a type already stands to its left |
| `/* … */` | `/` infix, then `*`, the **occurrence** operator | `occur = [uint] "*" [uint]` | **syntax error** in leading position |
| `# alg` | `#` **alone is "any CBOR data item"** | `type2 = … / "#" ; any` | **parses silently, different meaning** |
| `// alg` | `//` is the **group choice** operator | `group = grpchoice *(S "//" S grpchoice)` | **parses silently, different meaning** |
| — | `; …` is CDDL's only comment, and is a syntax error in CDN | `COMMENT = ";" *PCHAR CRLF` | **syntax error** in CDN |

**[analysis] Appendix A's own CDN example demonstrates the worst case.** The
document prints, as CDN:

```
{ 1:   # alg
    -7 # ECDSA 256
}
```

Fed to a CDDL parser this does **not** error. `1:` is a `value` memberkey, `#`
matches `type2 = … / "#"` ("any"), and `alg`, `-7`, `ECDSA`, `256` then parse as
four further group entries — six entries in all, where CDN sees a one-entry map.
The text is valid in both languages and means different things in each, with no
diagnostic. The same holds for `// alg`: `{1: 4, // alg` …`}` is a CDDL group
choice between `{1: 4}` and whatever follows.

The sibling example in the same appendix, `{ / alg / 1: -7 / ECDSA 256 / }`
(`V-0245`), behaves **better**: CDDL's `/` is infix and cannot begin a group
entry (`grpent = [occur S] [memberkey S] type`, and no `type2` alternative
starts with `/`), so a leading slash-delimited comment is a plain syntax error.
That is the outcome we want and it is why the distinction in the table above
matters: **the two end-of-line comment forms CDN added in this document are the
dangerous ones, and the inline form RFC 8610 Appendix G.6 already had is safe.**
Appendix A's warning — "it is easy to write 'CDDLisms' or 'CDNisms' into their
drafts that are meant to be in the other language. (This is one more of the many
motivations to always validate formal language instances with tools.)" —
understates it for `#` and `//`: **validating with tools does not catch those,
because both tools succeed.**

**[analysis] Two further families of silent collision, outside the table above:
the encoding-indicator and ellipsis syntaxes.** `_` and `_1` are legal CDDL ids (`EALPHA` includes `"_"`),
and CDDL's `optcom = S ["," S]` may be empty. So:

- `[_ 1, 2]` (`V-0214`) is a two-element indefinite-length array in CDN and a
  **three**-entry group in CDDL.
- `[1_1]` is a one-element array in CDN and a **two**-entry group in CDDL.
- `[_0 false, true]` (`V-0216`) is `[false, true]` in CDN and three entries in
  CDDL.
- `[1 ... 3]` is a three-element array in CDN (`ellipsis = 3*"."`) and the
  **exclusive range 1..2** in CDDL (`rangeop = "..." / ".."`). One element.

None of these errors. `[1, 2, ..., 3]` (`V-0227`) *does* error in CDDL, which is
the safe case and the exception.

**The rule this yields for us.** A single `.cdn`/`.cddl` boundary cannot be
checked by eye, and "validate with tools" is insufficient. If `library#39`'s
test-vector plan pairs EDN vectors with a CDDL schema, the two must live in
separate files with separate extensions, and the only characters that may appear
in both are the ones in the intersection of the two grammars. The safe
intersection is small: double-quoted strings without raw newlines or `\u{…}`
beyond RFC 9682's form, `h'…'`/`b64'…'` **without internal comments or
ellipses**, decimal integers without `+` or leading zeros, floats with at least
one digit on each side of the point, arrays and maps with explicit commas, and
`;` comments in the CDDL file and `/…/` comments in the CDN file, never mixed.

### 3. Can a reduced profile's data be written in CDN without naming a tag?

**Yes, and the tag-free subset is exactly §1.3.3's basic output format.** Walking
§6.1's `item` production against option 5's data model:

| CDN construct | §ref | needs major type 6? |
|---|---|---|
| `decnumber`, `hexint`, `octint`, `binint` within ±2^64 | §2.2 | no |
| `hexfloat`, `decnumber` with `.`/`e`, `nonfin` | §2.2 | no |
| `"…"`, `` `…` ``, `'…'`, `h'…'`, `b64'…'` | §2.3, §3.1 | no |
| `[ … ]`, `{ … : … }` | §2.4 | no |
| `true`, `false`, `null`, `undefined`, `simple(n)` | §2.6 | no |
| `<< … >>` embedded CBOR | §2.3.4 | **no** — the result is a plain byte string |
| encoding indicators `_i`, `_0`–`_3`, `_` | §4 | no |
| `dt'…'`, `ip'…'`, `hash<<…>>`, `b1`/`t1`, `float'…'` | §3.2–§3.8 | **no** — lowercase prefixes yield untagged values |

So every construct a tagless profile needs is available, and §2.3.4's `<<…>>` is
worth singling out: it gives us a readable notation for the
bstr-holding-encoded-CBOR pattern that `R-O-05` requires and that the `rfc-8949`
extraction established COSE uses *without* tag 24. `V-0249` is that case
written out — `<< {/alg/ 1: -7 /ECDSA 256/} >>`, which the document's own comment
annotates `# == h'a10126'`, and which this extraction decoded and confirmed. A
signed-payload vector can show the inner structure and the outer bytes at once,
which is exactly the debuggability the `rfc-8949` notes record as the cost of
dropping tag 24.

**Four places where CDN reaches for a tag anyway**, all avoidable but none
avoidable *silently*:

1. **Integers outside ±2^64 become tag 2 or 3, by the notation's own rule.**
   §6.1 item 5: "the corresponding CBOR data item is represented using major
   type 0 or 1 if possible, or using tag 2 or 3 if not. In the latter case, this
   specification does not define any encoding indicators that apply."
   `987654321098765432310` (`V-0238`) is plain CDN denoting an item option 5
   forbids. **[analysis]** CDN's integer syntax is therefore *wider* than a
   tagless profile, and CDN offers no way to express the profile's range limit;
   the range check is ours. This is the only place where writing ordinary CDN
   produces a tag without the author typing one.
2. **Uppercase prefixes** (`DT`, `IP`, `CRI`) mean a tag by convention (§3).
   Avoided by writing lowercase, which is already our rule from §1 above.
3. **`CPA999`** wraps an app-extension the ingester does not implement (§5.1).
   Avoided by using only the six mandatory-to-implement extensions.
4. **`CPA888`** carries elisions (§5.2). Avoided by forbidding `...` in fixtures.

### 4. Where this cuts against MD-3 — **mandatory section**

`MD-3` (2026-09-28) narrowed DEC-002 to option 5: CBOR data model, **no IANA
tags, COSE export only, YAML as the human form**. It is not an acceptance and
has no ADR. Four findings bear on it, in order of force.

**(a) MD-3 chose YAML as the human form without this document in evidence, and
the two largest objections to YAML do not apply to CDN.** The `rfc-8949`
extraction identifies the byte-string spelling as "the single largest source of
non-injectivity in the mapping and the item most likely to sink the Oct 28
package if left open", and the withdrawn YAML profile
(`ARCH-0001-PROPOSAL-v0.2.0` Appendix A) spends a clause on implicit typing
("so a field declared textual makes `no` the string `"no"`"). CDN has a byte
literal (§2.3.2) and no barewords (§6.1). Scored against that same ten-item
withdrawn list:

| the withdrawn YAML profile asks for | CDN |
|---|---|
| a single document, no streams | §6.1 has a `one-item` start rule beside `seq`. **Satisfied** |
| no anchors, aliases, merge keys | §1: YAML's "anchor/alias data sharing" is named as a feature "CDN does not provide". **Satisfied by construction** |
| string-only mapping keys | §2.4 extends JSON "by allowing any data item in the map key position". **Contradicted** |
| duplicate keys an error, not last-wins | §2.4.2 makes them writable; rejection is a configuration choice (§2). **Contradicted, permissively** |
| schema-driven typing so `no` is `"no"` | no barewords exist. **Satisfied, and without a schema** |
| no floating-point values | three widths plus `float''` and `nonfin`. **Available; the profile's job** |
| NFC-normalized strings | §2.3.5: "No additional Unicode processing or validation such as normalization … is foreseen by CDN", and such processing "MUST NOT get in the way of processing the data item represented in CDN". **Contradicted** |
| RFC 3339 UTC timestamps, integer seconds | §3.2 `dt''`, grammar in §6.2.3. **Satisfied** |
| output ordering matching the binary encoding's key order | §1.3.2: no deterministic representation. **Not provided** |
| comments stripped and unsigned | §2.1, and §5.2 states the hazard. **Same property, same hazard** |
| *(not on the list)* an unambiguous byte-string spelling | §2.3.2 / §3.1. **Satisfied — the item the list did not think to ask for** |

**[analysis]** Of the ten: four satisfied by construction, three contradicted,
one (floats) left to the profile, one (key ordering) not provided at all, and
one (comments) identical in both. Plus an eleventh that the list did not think
to ask for and that CDN satisfies — the byte-string spelling the `rfc-8949`
extraction called decisive. That does not overturn MD-3
and is not offered as doing so. It does mean the ADR must say why YAML rather
than CDN, because the minute's reason — a *human* form — is the one axis on
which CDN was designed for this and YAML was not. §1.3.1: "One important
application of CDN is the notation of CBOR data for humans: in specifications,
on whiteboards, and for entering test data." Note also that the two documents we
hold already disagree about whether a human authoring form exists at all:
`ARCH-0001-PROPOSAL-v0.2.0` §4 **withdrew** it ("Nothing in the analysis requires
humans to author certificates or statements in a text format"), while MD-3 names
YAML as the human form. Both are cited; neither is resolved here.

**(b) The document's own COSE idiom is tagged, and option 5's export profile
must say it will not be.** Appendix A's worked COSE example (`V-0247`) is:

```
98([h'', # empty encoded protected header
    {},  # empty unprotected header
    ...  # rest elided here
   ])
```

Tag **98** is COSE_Sign (RFC 9052 §2 Table 1), an IANA CBOR-tag allocation.
**[analysis]** The `rfc-8949` design notes already record this as "Tension 1" and
leave tagged-versus-untagged COSE export open. This document adds a small but
real consequence: *the canonical way to write a COSE object in the notation the
CBOR WG itself uses is tagged*, so an untagged export profile will produce
vectors that do not look like anyone else's COSE examples, and a reviewer
comparing our fixtures to the draft's will see a difference that is a decision
and not an error. That belongs in the `ARCH-0001` §6 interchange matrix row
`R-I-01` requires, which `rfc-8949`'s design notes record as not yet written
(its open question 11).

**(c) `ip''` is a miniature of what option 5 pays, in the source's own words.**
§3.3: "For completeness, the lowercase variant ip'2001:db8::/56' or
ip'192.0.2.0/24' stands for an unwrapped [56,h'20010db8'] or [24,h'c00002'];
however, in this case the information on whether an address is IPv4 or IPv6
often needs to come from the context." **[analysis]** That is option 5's
trade-off in one sentence, written by someone with no stake in our argument:
remove the tag and the type must come from context. It is the cleanest citable
illustration of the cost `ADR-0001` accepts, and it cuts both ways — the cost is
real, *and* the document treats it as perfectly workable. Worth putting in the
ADR for exactly that reason.

**(d) Where this source favours a DEC-002 option other than 5 — named.**

- **DEC-002 option 3 (JSON + RFC 8785 JCS; DSSE), and option 4 (dual canonical
  CBOR and JSON with a documented bijection).** §2 states a property neither of
  our documents has used: "CDN is a true superset of JSON as it is defined in
  [STD90] in conjunction with [RFC7493] (that is, any interoperable [RFC7493]
  JSON text also is a CDN text)". **[analysis]** Under option 3 every
  JCS-canonical JSON document is *already* a valid CDN text, so option 3 gets
  this notation for its vectors at no cost and gets byte strings and comments on
  top of it. Under **option 4** the superset property is stronger still: one CDN
  text can be the single authored form from which both halves of the bijection
  are generated, which is precisely the artifact option 4 needs and does not yet
  have. **This is a real, previously unnamed argument for options 3 and 4**, and
  since `ARCH-0001-PROPOSAL-v0.2.0` §3.3 records that "all four original options
  were scored on fidelity, tooling, and ergonomics, and none was scored on
  namespace governance", it is a tooling-axis point that the original scoring
  could have used and did not.
- **DEC-002 option 2 (CBOR + CDDL canonical; COSE signed) — evidence against, of
  a kind option 2 does not currently carry.** Option 2 bundles CBOR with CDDL.
  §2 above lists twelve surface divergences plus two further collision families;
  **four behaviours parse silently in both languages with different meanings** —
  `#` comments, `//` comments, encoding indicators read as CDDL ids, and `...`
  read as CDDL's range operator. **[analysis]** Option 2's cost is
  usually scored as the registry dependency `ADR-0001` rejects. This adds a
  second, independent cost: a project that writes instances in EDN and schemas
  in CDDL maintains two grammars that look alike and are not, and the failure
  mode is a silently different parse rather than an error. That cost is
  inherited by *any* option that adopts CDDL, including option 5 if `WP1`'s
  encoding-neutral schema is written in CDDL — which `ARCH-0001` §8 WP1 proposes
  ("JSON Schema or CDDL for logical types in §4"). **[analysis]** On this
  evidence, WP1's "JSON Schema or CDDL" choice is not neutral between the two:
  JSON Schema does not share a surface syntax with our vectors and CDDL does.
- **No option is favoured on the tag question.** §2.5 makes tags purely
  optional syntax, and §1.3.3's basic output format uses none. The document is
  neutral between a tag-using and a tag-free profile, which is itself worth
  recording: the usual objection that "no tags" makes the data unreadable does
  not survive contact with this specification.

### 5. Concrete consequences for our vector sets

1. **`hex` is normative, `edn` is commentary.** Forced by §1.3.2 (no
   determinism, no round-trip) and §4 (a conforming consumer may ignore an
   encoding indicator).
2. **Lowercase app-prefixes only; `h` and `b64` only.** §1 and §2 above.
3. **No ellipses, no raw strings, no `b32`/`h32`, no uppercase prefixes, no
   `0o`, no `+`-signed or zero-padded integers, no `3.`/`.3` in any file that a
   CDDL tool may also read.**
4. **Floats only in a form exact at the target width**, per *What we reject*.
5. **Our existing sets need no schema change.** `rfc-8949`,
   `draft-ietf-cbor-cde`, `draft-ietf-cbor-serialization` and
   `draft-mcnally-deterministic-cbor` already pair a `diagnostic` column with a
   `hex` column; this record's column is named `edn` for the obvious reason and
   is the same column. **[analysis]** What *is* newly owed is a line in each of
   those sets' READMEs saying which notation the `diagnostic` column is written
   in, because they were extracted against the diagnostic notation of RFC 8949
   §8 — and, wherever an EDN-only feature appears, RFC 8610 Appendix G — and
   this draft obsoletes both.

---

## Open questions

Items this document cannot settle, with who must. **[beyond source]** marks ones
where this extraction had to reason past both the draft and our own documents.

1. **Does the DEC-002 ADR choose CDN or YAML as the human form?** MD-3 says
   YAML; `ARCH-0001-PROPOSAL-v0.2.0` §4 withdrew the authoring half entirely and
   folded display into DEC-007. §4(a) above scores CDN against our own withdrawn
   YAML list and CDN wins on the two axes the `rfc-8949` extraction called
   decisive. *DEC-002 ADR — Paul.* (The `rfc-8949` notes already carry this as
   open question 8; this record adds the alternative the minute did not have.)
2. **Is `WP1`'s schema CDDL or JSON Schema?** `ARCH-0001` §8 WP1 offers both.
   §2 above shows that choosing CDDL imports twelve surface-syntax divergences
   from the notation our vectors are written in, four of whose behaviours are
   silent rather than an error.
   **[beyond source]** *David (D4 encoding-neutral schema, Oct 21.)*
3. **Does our profile forbid floats, and if not, in which spelling?** §6.1 item 5
   rounds silently. The `rfc-8949` notes already carry "floats in or out" as open
   question 6; this record adds that *if floats are in*, the vector spelling must
   be hexadecimal-float or `float'…'`, never decimal. *Same owner.*
4. **What is the integer range of the profile, and what does a vector do at the
   boundary?** §6.1 item 5 promotes to tag 2/3 silently, and `V-0238` is a plain
   CDN literal denoting an item option 5 forbids. The `rfc-8949` notes carry the
   range question; this adds that the *notation* will not help enforce it.
   *ADR.*
5. **Tagged or untagged COSE export**, unchanged from the `rfc-8949` record's
   open question 1, with §4(b) above as new input. *DEC-002 / DEC-005 ADR.*
6. **[beyond source] Does anything in our pipeline need a CDN parser, or only a
   CDN writer?** Everything above assumes we author CDN and compare bytes. If a
   tool must *read* our vector files' `edn` column, we inherit the §6.1 grammar
   including raw strings, four comment forms, the `startrawdelim`/`alikerawdelim`
   width predicate (§6.1 item 7, which needs a PEG predicate) and the §1.3.5 CR
   rule. That is a non-trivial parser and nobody has said whether we need one.
   *D5 fixture package.*
7. **[beyond source] What is hashed by `hash<<"text">>`?** §3.4 admits a text
   string as input and never says whether the bytes hashed are its UTF-8 content
   or its CBOR encoding; Table 5 exercises only the byte-string case. If we ever
   use `hash` to derive a digest in a fixture, we must pin this ourselves or
   avoid text-string inputs. *Raised with the CBOR WG, or avoided.*
8. **When does `CPA888`/`CPA999` become a number?** 26 of this record's vectors
   have no `hex` because of it (§7.5). *Re-check at RFC publication.*

### Defects and ambiguities in the source itself

Found by this extraction. Not questions about our design; places where draft-27
does not say what it appears to say.

9. **§4.1 Table 6's major-type-3 row is wrong in both hex columns.** It prints
   `| 3 | "A"_1 | 79000161 | 6161 |`. `0x79` is major type 3, `ai=25`, so the
   two-byte length `0x0001` must be followed by the string's one content byte,
   and `"A"` is `0x41`. The correct values are `79000141` and `6141`; the
   printed ones encode `"a"`. Found by decoding every byte sequence the document
   prints and re-encoding it from the EDN — 61 comparisons, 59 agreed, these two
   did not. Almost certainly copied from the row above (`V-0205`, `'A'_1`),
   where a one-byte byte string's head (`0x41`) and content (`0x41`) coincide.
   `V-0206` carries the correction. *Erratum material; report to the WG.*
10. **§3.5 prints `b1<"Hello world">` with single angle brackets** where §6.1's
    `app-sequence = app-prefix "<<" seq ">>"` requires two. The line is 20
    characters in a document whose longest line is 78, so it is not a margin
    truncation. `V-0174`. *Erratum material.*
11. **§3.6 defines the `ilbs` and `ilts` app-extensions and §4.3 makes them the
    replacement for the deprecated `streamstring`, but neither appears in §6.2
    Table 7 nor in §7.1 Table 8.** §3 says "app-extension identifiers are
    registered in the 'App-Extension Identifiers' registry (Section 7.1)", and
    §5.1 makes an unregistered prefix an error. As draft-27 stands, the
    recommended replacement for a deprecated syntax is spelled with two
    unregistered prefixes. *Erratum material; affects `V-0185`–`V-0189`.*
12. **§7.1 Table 8 cannot distinguish a defined prefix from an undefined one.**
    `h`, `b32`, `h32` and `b64` all carry Description "Reserved" and Reference
    "RFC8949", although this document defines `h` and `b64` (§3.1, §6.2 Table 7)
    and declines to define `b32` and `h32` (§3.1 aside). The registry and
    Table 7 therefore disagree, and `b32`'s reference points at RFC 8949 §8,
    which this draft obsoletes. See §1 above; this is the live half of the
    `rfc-8610` conflict after the resolution.
13. **§5.2's `bytes_in_IRI` line ends with a single `>`** — but at 78 characters
    it sits exactly on the document's right margin, so this one probably *is* a
    plain-text rendering truncation rather than a source defect. Recorded
    separately from 10 because the two look identical and are not. `V-0231`.
14. **[analysis] RFC 8610 is an informative reference (§9.2) of a document whose
    header says "Updates: 8610".** Defensible — the draft deletes part of RFC
    8610 rather than depending on it — but unusual enough to note, since a
    reader checking what "CDDL" means in §1.2 will follow an informative
    pointer to a document this draft has partly obsoleted.
15. **[correction] of `rfc-8610`'s own framing, not of its facts.** That
    record's defect 13 says the four-versus-two conflict is "never reconciled".
    True of RFC 8610 in isolation and still true of RFC 8610 as published — but
    the reconciliation exists, one document later: draft-27 obsoletes Appendix G
    and keeps two. `rfc-8610`'s `examples/README.md` bullet "**EDN admits
    byte-string prefixes CDDL does not** (`V-0085`)" should gain a pointer here,
    because read alone it now overstates the live risk. The `0o` octal claim in
    the same list (`V-0092`) needs no such qualification: §6.1 `octint` keeps it,
    and it remains a genuine CDN-only form.
