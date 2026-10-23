---
record: rfc-9682
kind: normative
title: "rfc-9682 — normative statements"
extracted: "2026-10-19"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 9682, "Updates to the Concise Data Definition Language (CDDL) Grammar", Standards Track, November 2024, Updates: 8610. sha256 `d35602e7f784e509a5984283ea8d998adfee23f086ad0d77bd22f98c6cdea89c` (699 lines, plain text). Quotations are verbatim from the plain-text RFC. Blocks that reproduce figures, grammar fragments or asides are exact source line runs and preserve the source's own line breaks and relative indentation inside fenced blocks.

**Why this file has no BCP 14 keywords at all.** `bin/bcp14-count` reports
**0** occurrences in 28 KB. That is expected and correct: this is a
**grammar-correcting document**, and its normativity is carried by **the ABNF
it replaces** and by **the prose that says what it replaces**. Appendix A is
the whole of the obligation, and it states its own force in two sentences —
"This appendix is normative." and "It provides the full ABNF from [RFC8610] as
updated by the present document." Section 1 fixes the replacement: "the updated
collected ABNF syntax in Figure 11 in Appendix A replaces the collected ABNF
syntax in Appendix B of [RFC8610]." Everything below is **definitional-
normative** at the same grain another record would use for MUST statements.
The precedents are the sibling records `rfc-8610` (2 keywords in 125 KB, 137 of
139 requirements `inferred`) and `draft-ietf-cbor-edn-literals` (10 keywords in
168 KB, 205 of 215 `inferred`).

**Normative scope, as the document itself states it.** Two appendices declare
their own status in one sentence each, and they disagree: **Appendix A** opens
"This appendix is normative."; **Appendix B** opens "This appendix is
informative." Both sentences are quoted in place below, and the second one
matters more than it looks — Appendix B.2 is where this document states the
two-stage model for prefixed byte strings, having dropped the normative note
RFC 8610 carried for it.

**Conventions in this file.**

- A bullet `- (§X) "…"` is one contiguous verbatim span of the source. No span
  is spliced from two non-adjacent parts of the document. Contiguity is
  asserted after collapsing runs of whitespace; no interior word, clause or
  punctuation mark was altered, dropped or reordered. **This document has no
  page frames at all** — no form feed, no running head, no `[Page n]` footer in
  699 lines — so no span crosses one and none needed repair.
- **TWO PLACES WHERE THIS DOCUMENT CANNOT BE QUOTED AS FLOWING PROSE. Both
  were found mechanically and neither is healed anywhere in this record.**
  - **The RFC's two aside blocks**, source lines 162–165 and 342–362, prefix
    every line with `      |`. Normalising whitespace across one interleaves
    `|` into the text, so **no sentence spanning two of its lines is a
    contiguous span of this document.** Both are reproduced below as exact
    source line runs, with the `|` marker intact, instead of being flowed into
    bullets. Where the prose above a block needs one of its claims, it names
    the block rather than quoting across it.
  - **Two end-of-line word breaks in prose.** Line 329 ends `the head-` and
    line 330 begins `number`, so the §3.2 sentence about `#7` **cannot be
    quoted whole**; the bullet carries the obligation-bearing half and names
    the severed half. Line 669 ends `copying-` and line 670 begins
    `and-pasting`, handled the same way in Appendix B.2. These are the only
    two in the document's prose; a third and fourth fall inside reference
    entries (lines 430, 432) which this file does not quote.
- Figures are reproduced as fenced blocks with their captions named, because a
  figure *is* the normative content of this document. The blocks are exact
  source line runs with the common left margin removed; relative indentation,
  the source's own ABNF comments, and the alignment of its trailing comment
  column are preserved.
- `grammar fragments` in backticks inside a bullet are the source's own, lifted
  from the same sentence.

---

## Abstract

- (Abstract) "The Concise Data Definition Language (CDDL), as defined in RFCs 8610 and 9165, provides an easy and unambiguous way to express structures for protocol messages and data formats that are represented in Concise Binary Object Representation (CBOR) or JSON."
- (Abstract) "This document updates RFC 8610 by addressing related errata reports and making other small fixes for the ABNF grammar defined for CDDL."

## §1. Introduction

- (§1) "The Concise Data Definition Language (CDDL), as defined in [RFC8610] and [RFC9165], provides an easy and unambiguous way to express structures for protocol messages and data formats that are represented in CBOR or JSON."
- (§1) "This document updates [RFC8610] by addressing errata reports and making other small fixes for the ABNF grammar defined for CDDL."
- (§1) "The body of this document explains and shows motivation for the updates; the updated collected ABNF syntax in Figure 11 in Appendix A replaces the collected ABNF syntax in Appendix B of [RFC8610]."

**That last sentence is the whole of this document's normative force.** It is the only statement of replacement scope, and the word it turns on is *syntax*: RFC 8610 Appendix B's two prose sentences — the case-sensitivity preamble and the prefixed-byte-string note — are not reproduced in Appendix A. See `schema/production-changes.derived.txt`.

### §1.1. Conventions and Definitions

- (§1.1) "The terminology from [RFC8610] applies."
- (§1.1) "The grammar in [RFC8610] is based on ABNF, which is defined in [STD68] and [RFC7405]."

**There is no BCP 14 boilerplate paragraph in this section**, and no BCP 14 keyword anywhere in the document. §1.1 is two sentences long and both are quoted above. [STD68] is RFC 5234 and [RFC7405] is *Case-Sensitive String Support in ABNF*; the second is cited here as normative and then **deliberately not used** — see the §2.1.1 aside.

## §2. Clarifications and Changes Based on Errata Reports

- (§2) "A number of errata reports have been made regarding some details of text string and byte string literal syntax: for example, [Err6527] and [Err6543]."
- (§2) "These are being addressed in this section, updating details of the ABNF for these literal syntaxes."
- (§2) "Also, the changes described in [Err6526] need to be applied (backslashes have been lost during the RFC publication process of Appendix G.2 of [RFC8610], garbling the text explaining backslash escaping)."
- (§2) "These changes are intended to mirror the way existing implementations have dealt with the errata reports."
- (§2) "This document also uses the opportunity presented by the necessary cleanup of the grammar of string literals for a backward-compatible addition to the syntax for hexadecimal escapes."
- (§2) "The latter change is not automatically forward compatible (i.e., CDDL specifications that make use of this syntax do not necessarily work with existing implementations until these are updated, which is recommended by this specification)."

**Note what §2 does and does not claim.** It claims that the changes *mirror
existing implementations* — a statement about deployed tools, not about the
language — and it calls only the hex-escape **addition** backward compatible.
The explicit backward-compatibility claim in this document belongs to §3 and is
scoped there by its own opening words. §2's rewrite of `SESC` **narrows** the
language; nothing in the document says so. Recorded in
`schema/grammar-gaps-status.derived.txt`, NEW-OBS-2.

**"which is recommended by this specification"** is the closest this document
comes to an obligation, and it is lower case. It is extracted as
`rfc-9682#R-0013`, `kind: inferred`, with that phrase named in its `field`.

### §2.1. Updates to String Literal Grammar

The section heading carries no prose of its own.

#### §2.1.1. Erratum ID 6527 (Text String Literals)

- (§2.1.1) "The ABNF used in [RFC8610] for the content of text string literals is rather permissive:"

Figure 1, *Original ABNF from RFC 8610 for Strings with Permissive ABNF for SESC (Which Did Not Allow Hex Escapes)* (source lines 123–126) — **this is the superseded text**:

```
; ABNF from RFC 8610:
text = %x22 *SCHAR %x22
SCHAR = %x20-21 / %x23-5B / %x5D-7E / %x80-10FFFD / SESC
SESC = "\" (%x20-7E / %x80-10FFFD)
```

- (§2.1.1) "This allows almost any non-C0 character to be escaped by a backslash, but critically misses out on the \uXXXX and \uHHHH\uLLLL forms that JSON allows to specify characters in hex (which should apply here according to item 6 of Section 3.1 of [RFC8610])."
- (§2.1.1) "(Note that CDDL imports from JSON the unwieldy \uHHHH\uLLLL syntax, which represents Unicode code points beyond U+FFFF by making them look like UTF-16 surrogate pairs; CDDL text strings do not use UTF-16 or surrogates.)"
- (§2.1.1) "Both can be solved by updating the SESC rule."
- (§2.1.1) "This document uses the opportunity to add a popular form of directly specifying characters in strings using hexadecimal escape sequences of the form \u{hex}, where hex is the hexadecimal representation of the Unicode scalar value."
- (§2.1.1) "The result is the new set of rules defining SESC in Figure 2."

Figure 2, *Update to String ABNF in Appendix B of [RFC8610]: Allow Hex Escapes* (source lines 145–157) — **normative; six of the eight new productions are here**:

```
; new rules collectively defining SESC:
SESC = "\" ( %x22 / "/" / "\" /                 ; \" \/ \\
             %x62 / %x66 / %x6E / %x72 / %x74 / ; \b \f \n \r \t
             (%x75 hexchar) )                   ; \uXXXX
hexchar = "{" (1*"0" [ hexscalar ] / hexscalar) "}" /
          non-surrogate / (high-surrogate "\" %x75 low-surrogate)
non-surrogate = ((DIGIT / "A"/"B"/"C" / "E"/"F") 3HEXDIG) /
                ("D" %x30-37 2HEXDIG )
high-surrogate = "D" ("8"/"9"/"A"/"B") 2HEXDIG
low-surrogate = "D" ("C"/"D"/"E"/"F") 2HEXDIG
hexscalar = "10" 4HEXDIG / HEXDIG1 4HEXDIG
          / non-surrogate / 1*3HEXDIG
HEXDIG1 = DIGIT1 / "A" / "B" / "C" / "D" / "E" / "F"
```

The aside that follows Figure 2 (source lines 162–165) is reproduced as an
exact line run, because every sentence in it crosses the `|` prefix. It is the
only place in this document where the case-insensitivity of ABNF quoted
strings is mentioned, and it is scoped to the new rules by its own words:

```
      |  Notes: In ABNF, strings such as "A", "B", etc., are case
      |  insensitive, as is intended here.  The rules above could have
      |  also used %s"b", etc., instead of %x62, but didn't, in order to
      |  maximize compatibility with ABNF tools.
```

**Why that matters beyond style.** `%x62` … `%x75` are numeric and therefore
exact, so the escape *letter* is case-sensitive (`\B`, `\N`, `\U` are errors)
while the hex *digits* of a payload are quoted strings and stay
case-insensitive. Figure 5 exercises both spellings in one file. [RFC7405],
which exists to make ABNF case-sensitivity explicit and is a normative
reference of this document, is named in this aside only to say it was not used.

- (§2.1.1) "Now that SESC is more restrictively formulated, an update to the BCHAR rule used in the ABNF syntax for byte string literals is also required:"

Figure 3, *ABNF from RFC 8610 for BCHAR* (source lines 171–174) — **superseded text**:

```
; ABNF from RFC 8610:
bytes = [bsqual] %x27 *BCHAR %x27
BCHAR = %x20-26 / %x28-5B / %x5D-10FFFD / SESC / CRLF
bsqual = "h" / "b64"
```

- (§2.1.1) "With the SESC updated as above, \' is no longer allowed in BCHAR and now needs to be explicitly included there; see Figure 4."

**The document states the `BCHAR` half of that consequence and not the `SCHAR` half.** `\'` is no longer a `SESC` in a *text* string either, and no sentence says so; U+0027 needs no escape in a text string, so nothing becomes inexpressible, but `"\'"` was valid RFC 8610 CDDL and is not valid RFC 9682 CDDL.

#### §2.1.2. Erratum ID 6278 (Consistent String Literals)

- (§2.1.2) "Updating BCHAR also provides an opportunity to address [Err6278], which points to an inconsistency in treating U+007F (DEL) between SCHAR and BCHAR."
- (§2.1.2) "As U+007F is not printable, including it in a byte string literal is as confusing as for a text string literal; therefore, it should be excluded from BCHAR as it is from SCHAR."
- (§2.1.2) "The same reasoning also applies to the C1 control characters, so the updated ABNF actually excludes the entire range from U+007F to U+009F."
- (§2.1.2) "The same reasoning also applies to text in comments (PCHAR)."
- (§2.1.2) "For completeness, all these rules should also explicitly exclude the code points that have been set aside for UTF-16 surrogates."

Figure 4, *Update to ABNF in Appendix B of [RFC8610]: BCHAR, SCHAR, and PCHAR* (source lines 194–198) — **normative; the remaining two new productions, and the one rule that carries the whole surrogate fix**:

```
; new rules for SCHAR, BCHAR, and PCHAR:
SCHAR = %x20-21 / %x23-5B / %x5D-7E / NONASCII / SESC
BCHAR = %x20-26 / %x28-5B / %x5D-7E / NONASCII / SESC / "\'" / CRLF
PCHAR = %x20-7E / NONASCII
NONASCII = %xA0-D7FF / %xE000-10FFFD
```

- (§2.1.2) "(Note that, apart from addressing the inconsistencies, there is no attempt to further exclude non-printable characters from the ABNF; doing this properly would draw in complexity from the ongoing evolution of the Unicode standard [UNICODE] that is not needed here.)"

**That parenthetical is load-bearing.** The exclusion of U+007F–U+009F is **lexical only**: `hexscalar`'s `1*3HEXDIG` branch makes `\u{7F}` … `\u{9F}` — and the whole C0 range, and `\u{9}` — well-formed escapes. A tool that wants the exclusion to mean anything must check twice. The document's own sentence is its answer, so this is a gap it chose rather than missed.

#### §2.1.3. Addressing Erratum ID 6526 and Erratum ID 6543

- (§2.1.3) "The above changes also cover [Err6543] (a proposal to split off qualified byte string literals from UTF-8 byte string literals) and [Err6526] (lost backslashes); see Appendix B for details."

The section is one sentence. **Four errata are addressed by this document — 6527, 6278, 6543 and 6526 — and a fifth, [Err6575], is named in the §3.2 aside as *not* addressed here.**

### §2.2. Examples Demonstrating the Updated String Syntaxes

- (§2.2) "The CDDL example in Figure 5 demonstrates various escaping techniques now available for (byte and text) strings in CDDL."
- (§2.2) "Obviously, in the literals for a and x, there is no need to escape the second character, an o, as \u{6f}; this is just for demonstration."
- (§2.2) "Similarly, as shown in c and z, there also is no need to escape the "🁳" (DOMINO TILE VERTICAL-02-02, U+1F073) or "⌘" (PLACE OF INTEREST SIGN, U+2318); however, escaping them may be convenient in order to limit the character repertoire of a CDDL file itself to ASCII [STD80]."

Figure 5, *Example Text and Byte String Literals with Various Escaping Techniques* (source lines 226–237):

```
start = [a, b, c, x, y, z]

; "🁳", DOMINO TILE VERTICAL-02-02, and
; "⌘", PLACE OF INTEREST SIGN, in a text string:
a = "D\u{6f}mino's \u{1F073} + \u{2318}"      ; \u{}-escape 3 chars
b = "Domino's \uD83C\uDC73 + \u2318"          ; escape JSON-like
c = "Domino's 🁳 + ⌘"                          ; unescaped

; in a byte string given as text, the ' needs to be escaped:
x = 'D\u{6f}mino\u{27}s \u{1F073} + \u{2318}' ; \u{}-escape 4 chars
y = 'Domino\'s \uD83C\uDC73 + \u2318'         ; escape JSON-like
z = 'Domino\'s 🁳 + ⌘'                         ; escape ' only
```

- (§2.2) "In this example, the rules a to c and x to z all produce strings with byte-wise identical content: a to c are text strings and x to z are byte strings."
- (§2.2) "Figure 6 illustrates this by showing the output generated from the start rule in Figure 5, using pretty-printed hexadecimal."

Figure 6, *Generated CBOR from CDDL Example (Pretty-Printed Hexadecimal)* (source lines 248–260) — **the only byte-level output this document prints, and the whole of this record's test-vector basis**:

```
86                                      # array(6)
   73                                   # text(19)
      446f6d696e6f277320f09f81b3202b20e28c98 # "Domino's 🁳 + ⌘"
   73                                   # text(19)
      446f6d696e6f277320f09f81b3202b20e28c98 # "Domino's 🁳 + ⌘"
   73                                   # text(19)
      446f6d696e6f277320f09f81b3202b20e28c98 # "Domino's 🁳 + ⌘"
   53                                   # bytes(19)
      446f6d696e6f277320f09f81b3202b20e28c98 # "Domino's 🁳 + ⌘"
   53                                   # bytes(19)
      446f6d696e6f277320f09f81b3202b20e28c98 # "Domino's 🁳 + ⌘"
   53                                   # bytes(19)
      446f6d696e6f277320f09f81b3202b20e28c98 # "Domino's 🁳 + ⌘"
```

**This figure is the document's own acceptance criterion for §2.** Six rules, three spellings each of one 19-byte string, and `byte-wise identical content` asserted across the text/byte boundary. Every vector in `examples/vectors.yaml` derives from it.

## §3. Small Enabling Grammar Changes

- (§3) "Each subsection that follows specifies a small change to the grammar that is intended to enable certain kinds of specifications."
- (§3) "These changes are backward compatible (i.e., CDDL files that comply with [RFC8610] continue to match the updated grammar) but not necessarily forward compatible (i.e., CDDL specifications that make use of these changes cannot necessarily be processed by existing implementations of [RFC8610])."

**Read the scope of that claim exactly.** "Each subsection that follows" is §3.1 and §3.2 only. §2 makes no equivalent claim and does not satisfy one.

### §3.1. Empty Data Models

- (§3.1) "[RFC8610] requires a CDDL file to have at least one rule."

Figure 7, *ABNF from RFC 8610 for Top-Level Rule cddl* (source lines 279–280) — **superseded text**:

```
; ABNF from RFC 8610:
cddl = S 1*(rule S)
```

- (§3.1) "This makes sense when the file has to stand alone, as a CDDL data model needs to have at least one rule to provide an entry point (i.e., a start rule)."
- (§3.1) "With CDDL modules [CDDL-MODULES], CDDL files can also include directives, and these might be the source of all the rules that ultimately make up the module created by the file."
- (§3.1) "Any other rule content in the file has to be available for directive processing, making the requirement for at least one rule cumbersome."
- (§3.1) "Therefore, the present update extends the grammar as in Figure 8 and turns the existence of at least one rule into a semantic constraint, to be fulfilled after processing of all directives."

Figure 8, *Update to Top-Level ABNF in Appendices B and C of RFC 8610* (source lines 298–299) — **normative**:

```
; new top-level rule:
cddl = S *(rule S)
```

**Note the caption's scope: "Appendices B *and C*".** This document reproduces RFC 8610's Appendix B and none of its Appendix C, so the Appendix C half of this update is stated in a figure caption and nowhere else. The same is true of Figure 10.

**And note what moved rather than went away.** "at least one rule" is now a semantic constraint on a phase — "after processing of all directives" — that this document does not define; it belongs to `[CDDL-MODULES]`, which §6.2 cites as "Work in Progress, Internet-Draft, draft-ietf-cbor-cddl-modules-03".

### §3.2. Non-Literal Tag Numbers and Simple Values

- (§3.2) "The existing ABNF syntax for expressing tags in CDDL is as follows:"

Figure 9, *Original ABNF from RFC 8610 for Tag Syntax* (source lines 307–308) — **superseded text**:

```
; extracted from the ABNF in RFC 8610:
type2 =/ "#" "6" ["." uint] "(" S type S ")"
```

- (§3.2) "This means tag numbers can only be given as literal numbers (uints)."
- (§3.2) "Some specifications operate on ranges of tag numbers; for example, [RFC9277] has a range of tag numbers 1668546817 (0x63740101) to 1668612095 (0x6374FFFF) to tag specific content formats."
- (§3.2) "This cannot currently be expressed in CDDL."
- (§3.2) "Similar considerations apply to simple values (#7.xx)."
- (§3.2) "This update extends the syntax to the following:"

Figure 10, *Update to Tag and Simple Value ABNF in Appendices B and C of RFC 8610* (source lines 321–324) — **normative**:

```
; new rules collectively defining the tagged case:
type2 =/ "#" "6" ["." head-number] "(" S type S ")"
       / "#" "7" ["." head-number]
head-number = uint / ("<" type ">")
```

**The sentence that gives those alternatives their meaning is severed by an
end-of-line word break** — source line 329 ends `the head-` and line 330 begins
`number` — so it is given here as the two halves it actually is, and the
obligation-bearing half is the second one. Nothing is healed.

- (§3.2) "For #6, the head-number stands for the tag number."
- (§3.2) *[severed subject, source line 329, quoted as it stands]* "For #7, the head-" **+** *[obligation-bearing half, line 330 onward]* "number stands for the simple value if it is in the ranges 0..23 or 32..255 (as per Section 3.3 of RFC 8949 [STD94], the simple values 24..31 are not used)."
- (§3.2) "For 24..31, the head-number stands for the "additional information", e.g., #7.25 or #7.<25> is a float16, etc."
- (§3.2) "(All ranges mentioned here are inclusive.)"

- (§3.2) "So the above range can be expressed in a CDDL fragment such as:"

The §3.2 CDDL fragment (source lines 338–340):

```
ct-tag<content> = #6.<ct-tag-number>(content)
ct-tag-number = 1668546817..1668612095
; or use 0x63740101..0x6374FFFF
```

The §3.2 aside (source lines 342–362) is reproduced as an exact line run, for
the same reason as the §2.1.1 one: every sentence in it crosses the `|` prefix.
Note 1 argues the angle-bracket reuse is unambiguous; note 2 records that the
reading was already RFC 8610's, names [Err6575] as the erratum that would say
so in RFC 8610's own prose, and regrets the choice of the dot while declining
to change it. **Source line 355 carries this document's one typographic defect
— a U+201D closing a phrase opened with U+0022 — and it is reproduced here
unrepaired.**

```
      |  Notes:
      |  
      |     1.  This syntax reuses the angle bracket syntax for
      |         generics; this reuse is innocuous because a generic
      |         parameter or argument only ever occurs after a rule name
      |         (id), while it occurs after the "." (dot) character
      |         here.  (Whether there is potential for human confusion
      |         can be debated; the above example deliberately uses
      |         generics as well.)
      |  
      |     2.  The updated ABNF grammar makes it a bit more explicit
      |         that the number given after the optional dot is the
      |         value of the argument: for tags and simple values, it is
      |         not giving the CBOR "additional information”, as it is
      |         with other uses of # in CDDL.  (Adding this observation
      |         to Section 2.2.3 of [RFC8610] is the subject of
      |         [Err6575]; it is correctly noted in Section 3.6 of
      |         [RFC8610].)  In hindsight, maybe a different character
      |         than the dot should have been chosen for this special
      |         case; however, changing the grammar in the current
      |         document would have been too disruptive.
```

## §4. Security Considerations

- (§4) "The grammar fixes and updates in this document are not believed to create additional security considerations."
- (§4) "The security considerations in Section 5 of [RFC8610] apply."
- (§4) "Specifically, the potential for confusion is increased in an environment that uses a combination of CDDL tools, some of which have been updated and some of which have not, in particular based on Section 2."
- (§4) "Attackers may want to exploit such potential confusion by crafting CDDL models that are interpreted differently by different parts of a system."
- (§4) "There will be a period of transition from the details that the grammar in [RFC8610] handled in a less well-defined way, to the updated grammar defined in the present document."
- (§4) "This transition might offer one (but not the only) type of opportunity for the kind of attack that relies on differences between implementations."
- (§4) "Implementations that make use of CDDL models operationally already need to ascertain the provenance (and thus authenticity and integrity) and applicability of models they employ."
- (§4) "At the time of writing, it is expected that the models will generally be processed by a software developer, within a software development environment."
- (§4) "Therefore, developers are advised to treat CDDL models with the same care as any other source code."

**§4 is the only place this document reasons about consequences, and it names a
class without naming an instance.** The instance exists and is recorded in
`schema/production-changes.derived.txt`: `"D\u{6f}mino"` and `"\uD83C\uDC73"`
**parse under both grammars with different meanings and produce no diagnostic
on either side.** That is "interpreted differently by different parts of a
system", exactly, in the one construct §2 added.

**§4 describes a deployment transition, not a protocol or a lifecycle.** The
states it names belong to the population of deployed tools, not to any object
this document defines; there is no trigger, no guard and no transition an
implementation performs. That is the basis for `protocol` and `state-machine`
being declared `not_applicable` in `record.yaml`, and the compatibility matrix
that would have been a state machine is in `design-notes.md` instead.

## §5. IANA Considerations

- (§5) "This document has no IANA actions."

The section is one sentence, and it is the whole of it. Contrast the sibling `draft-ietf-cbor-edn-literals`, which creates two registries.

## Appendix A. Updated Collected ABNF for CDDL

- (Appendix A) "This appendix is normative."
- (Appendix A) "It provides the full ABNF from [RFC8610] as updated by the present document."

**Those two sentences are the entire prose of the one normative appendix of
this document.** Figure 11 follows them and runs to the end of the appendix:
source lines 482–591, 110 lines, **55 rule definitions**, one unbroken region,
no page frame, and **no closing note of any kind** — the line after `CRLF` is
the figure caption.

Figure 11, *ABNF for CDDL as Updated*, is **not reproduced in this file**. It
is this record's primary schema artifact and is held byte-exact, with the RFC's
three-column margin intact and a per-region sha256, at
`schema/cddl-updated.abnf`; a dedented, tool-readable companion is at
`schema/cddl-updated-dedented.derived.abnf`. Reproducing it here as well would
give a reader two copies to choose between, which is the thing the derived/
verbatim convention exists to prevent.

**What a reader must take from this appendix, stated and not reproduced:**

- it REPLACES RFC 8610 Appendix B in whole — 8 new rules, 6 with a changed
  right-hand side, 41 carried over unchanged, 0 dropped;
- it does **not** reproduce RFC 8610 Appendix B's case-sensitivity preamble;
- it does **not** reproduce RFC 8610 Appendix B's closing note about prefixed
  byte strings, whose substance reappears in the **informative** Appendix B.2;
- `CRLF = %x0A / %x0D.0A` and `bsqual = "h" / "b64"` are both carried over
  **unchanged**.

The production-by-production statement is `schema/production-changes.derived.txt`.

## Appendix B. Details about Covering Erratum ID 6543

- (Appendix B) "This appendix is informative."
- (Appendix B) "[Err6543] notes that the ABNF used in [RFC8610] for the content of byte string literals lumps together byte strings notated as text with byte strings notated in base16 (hex) or base64 (but see also updated BCHAR rule in Figure 4):"

Figure 12, *Original ABNF from RFC 8610 for BCHAR* (source lines 604–606) — **superseded text, and a second quotation of the same two rules as Figure 3**:

```
; ABNF from RFC 8610:
bytes = [bsqual] %x27 *BCHAR %x27
BCHAR = %x20-26 / %x28-5B / %x5D-10FFFD / SESC / CRLF
```

### Appendix B.1. Change Proposed by Erratum ID 6543

- (Appendix B.1) "Erratum ID 6543 proposes handling the two cases in separate ABNF rules (where, with an updated SESC, BCHAR obviously needs to be updated as above):"

Figure 13, *Proposal from Erratum ID 6543 to Split the Byte String Rules* (source lines 616–620) — **the change that was NOT taken**:

```
; Proposal from Erratum ID 6543:
bytes = %x27 *BCHAR %x27
      / bsqual %x27 *QCHAR %x27
BCHAR = %x20-26 / %x28-5B / %x5D-10FFFD / SESC / CRLF
QCHAR = DIGIT / ALPHA / "+" / "/" / "-" / "_" / "=" / WS
```

- (Appendix B.1) "This potentially causes a subtle change, which is hidden in the WS rule:"

Figure 14, *ABNF Definition of WS from RFC 8610* (source lines 628–634) — **superseded text; this is also the only place RFC 9682 prints the old `PCHAR` and the unchanged `CRLF` side by side**:

```
; ABNF from RFC 8610:
WS = SP / NL
SP = %x20
NL = COMMENT / CRLF
COMMENT = ";" *PCHAR CRLF
PCHAR = %x20-7E / %x80-10FFFD
CRLF = %x0A / %x0D.0A
```

- (Appendix B.1) "This allows any non-C0 character in a comment, so this fragment becomes possible:"

The fragment that the **declined proposal** would have admitted (source lines 641–644):

```
foo = h'
   43424F52 ; 'CBOR'
   0A       ; LF, but don't use CR!
'
```

- (Appendix B.1) "The current text is not unambiguously saying whether the three apostrophes need to be escaped with a \ or not, as in:"

The escaped form (source lines 649–652):

```
foo = h'
   43424F52 ; \'CBOR\'
   0A       ; LF, but don\'t use CR!
'
```

- (Appendix B.1) "... which would be supported by the existing ABNF in [RFC8610]."

**And by RFC 9682's**, where `BCHAR` admits `"\'"` explicitly. The unescaped fragment above is admitted by neither the old grammar nor the new one — U+0027 is in no `BCHAR` alternative, so the first bare apostrophe terminates the literal — which is why the document's words are "becomes possible" under the proposal. The two fragments are vectors `rfc-9682#V-0013` and `rfc-9682#V-0014`.

### Appendix B.2. No Further Change Needed after Updating String Literal Grammar

- (Appendix B.2) "This document takes the simpler approach of leaving the processing of the content of the byte string literal to a semantic step after processing the syntax of the bytes and BCHAR rules, as updated by Figures 2 and 4 in Section 2.1 (updates prompted by the combination of [Err6527] and [Err6278])."
- (Appendix B.2) "Therefore, the rules in Figure 14 (as updated by Figure 4) are applied to the result of this processing where bsqual is given as h or b64."

**Those two sentences are the only statement of the two-stage model, and they sit in an appendix that has just declared itself informative.** RFC 8610 carried the equivalent caveat as a note inside a *normative* appendix. The demotion is recorded in `schema/grammar-gaps-status.derived.txt`, G-12.
- (Appendix B.2) "Note that this approach also works well with the use of byte strings in Section 3 of [RFC9165]."
- (Appendix B.2) *[severed by an end-of-line word break: source line 669 ends "copying-", line 670 begins "and-pasting"; the obligation-bearing half is quoted]* "and-pasting into CDDL models from ABNF that contains single quotes (which may also hide as apostrophes in comments); these need to be escaped or possibly replaced by %x27."
- (Appendix B.2) "Finally, the approach taken lends support to extending bsqual in CDDL similar to the way this is done for CBOR diagnostic notation in [EDN-LITERALS]."
- (Appendix B.2) "(Note that, at the time of writing, the processing of string literals is quite similar for both CDDL and Extended Diagnostic Notation (EDN), except that CDDL has end-of-line comments that are ";" based and EDN has two comment syntaxes: one in-line "/" based and one end-of-line "#" based.)"

**"lends support to extending" is the whole of it. Support lent, not taken.**
`bsqual = "h" / "b64"` is carried into Figure 11 unchanged, so CDDL still has
exactly two byte-string prefixes after this document while the sibling
`draft-ietf-cbor-edn-literals` has more. The divergence is now deliberate and
documented rather than accidental, and it is a finding for us: a vector written
with any other prefix is valid EDN and is not a CDDL literal.

## Acknowledgments

Not normative, and one sentence of it is load-bearing for provenance under `R-O-03`: the rule that carries the entire surrogate fix was somebody's suggestion, and the document says so.

- (Acknowledgments) "In one of the ensuing discussions, Doug Ewell proposed defining an ABNF rule "NONASCII", of which we have included the essence."

---

## What this file does not contain

- **Figure 11 itself** — `schema/cddl-updated.abnf`, byte-exact, for the reason
  given under Appendix A.
- **§6's references** — 4 normative entries ([RFC8610], [STD68], [STD94], and
  §6.1's framing) and 14 informative ones. Two carry end-of-line word breaks
  inside the draft names themselves (lines 430, 432) and are not quoted here.
  The two that matter are cited in place above: `[CDDL-MODULES]` is "Work in
  Progress" and so is `[EDN-LITERALS]`.
- **The front matter, Status of This Memo and Copyright Notice** — boilerplate.
  Note that quoting the Copyright Notice would have added no BCP 14 keywords:
  its "must" ("Code Components extracted from this document must include
  Revised BSD License text") is lower case, as is §2's "recommended". The
  document's keyword count is a true zero, not a stripping artifact.
- **§6.1's and §6.2's bibliographic detail** — in `record.yaml` relations and
  in `design-notes.md` where it bears on us.
