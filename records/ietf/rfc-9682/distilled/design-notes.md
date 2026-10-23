---
record: rfc-9682
kind: design-notes
title: "rfc-9682 — bearing on our design"
extracted: "2026-10-19"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§3.2`) are RFC 9682. Our own documents are cited by id (`ARCH-0002 P1`,
`MD-3`, `R-O-03`). Four markers distinguish voices:

- unmarked prose reports **RFC 9682** or **our decisions**, as cited;
- a quotation is RFC 9682's own words, contiguous and mechanically checked,
  **unless the sentence names another document**, in which case the quotation is
  that document's: `RFC 8610 §3.1`, `ARCH-0001` §7, `ADR-0001`, `R-M-11`,
  `R-O-03`, `R-O-05`, `ARCH-0002` P5 and `DECISIONS-0001` are all quoted below
  and **none of their sentences appears in RFC 9682**;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project, or a claim in a
  sibling record of this library, that the sources do not support;
- **[correction, _date_, _pass_]** — the *dated* form — marks something **this
  file itself** got wrong, saying what it used to claim and why that was
  false. It is the library's maintenance convention, not a finding about the
  source, and the two senses are deliberately kept apart by the date.
  *(The second sense was added 2026-10-20 by pass 3, which needed it.)*

**Decision status, stated plainly.** DEC-002 in `ARCH-0001` §7 lists **four**
options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3; that proposal is unmerged and ARCH-0001 still
carries DEC-002 under "Open decisions". `ADR-0001` (accepted) constrains
DEC-002 and says option 2 "as originally written does not" remain on the table.
`MD-3` (2026-09-28) **narrowed** DEC-002 to option 5 and named YAML as the
human form; `DECISIONS-0001` item 2 says in terms that "a narrowing is not an
acceptance, and no ADR exists", and its standing note records that the evidence
moved after the narrowing. **Nothing below may be read as an accepted encoding
decision**, and *Where this cuts against MD-3* is written to be read by someone
who has not yet decided.

**What this document is, in one line.** A grammar-correcting RFC with **zero**
BCP 14 keywords that replaces RFC 8610 Appendix B's collected ABNF in whole:
8 new productions, 6 with a changed right-hand side, 41 carried over unchanged,
0 dropped. The production-by-production statement is
`schema/production-changes.derived.txt`; its effect on the 44 side conditions
this library enumerated against RFC 8610 is `schema/grammar-gaps-status.derived.txt`.

**Why a CDDL grammar document reaches our design at all.** DEC-002 option 2 is
"CBOR + CDDL as canonical"; option 5 keeps CBOR's data model and says nothing
about the schema language, so if we write a schema at all it is CDDL. `D4`'s
encoding-neutral types are the deliverable that would hold it. This record
therefore settles **which CDDL we would be writing** — and its answer is: not
the one the `rfc-8610` record holds.

---

## What we adopt

**The grammar in Figure 11, as the only current CDDL syntax, in place of
RFC 8610 Appendix B.** `§1`: "the updated collected ABNF syntax in Figure 11 in
Appendix A replaces the collected ABNF syntax in Appendix B of [RFC8610]." Any
CDDL we author or parse is measured against `schema/cddl-updated.abnf`, not
against the sibling record's `cddl.abnf`. **This discharges the `rfc-9682`
quarter of the gate that `rfc-8610`'s own `distilled/README.md` carries.**

**The surrogate exclusion, because it closes a hole under `ARCH-0002` P1.**
P1 makes an extension point a pair `(defining key, local label)`, and the local
label is a **text string** — `ARCH-0001` §4.1 carries it as major type 3.
RFC 8610's `SCHAR` spanned `%x80-10FFFD` and so **admitted U+D800–U+DFFF**,
which are not Unicode scalar values and cannot be encoded in UTF-8 at all.
RFC 9682's `NONASCII = %xA0-D7FF / %xE000-10FFFD` removes them from `SCHAR`,
`BCHAR` and `PCHAR`, and the new `SESC` removes them from the escape path too:
`non-surrogate` forces a leading `D` into `%x30-37`, and the only
surrogate-shaped form requires both halves of a pair and denotes a code point
above U+FFFF. The source is explicit — "CDDL text strings do not use UTF-16 or
surrogates."

**[analysis]** This matters to us and not merely to tidiness. A label
containing a lone surrogate is **unencodable**, so a schema that admitted one
described a label space larger than the wire can carry. Under `R-O-05` the
signed payload is "the canonical encoding verbatim", and a value that cannot be
encoded has no canonical encoding — so the old grammar permitted a *schema* for
a statement that could never be signed. That is now a syntax error.

**The closed escape set, as a restriction we want.** RFC 8610 admitted a
backslash before any of 1,114,077 code points; RFC 9682 admits eight
single-character escapes plus the `\u` family and nothing else. **[analysis]**
For `D4` this is the difference between a schema language whose string literals
have one reading and one whose literals must be interpreted by convention. It
is also the first thing in this family of documents that makes a CDDL *source
file* mechanically comparable: two schema files that differ only in escape
spelling can now be told apart from two that differ in meaning.

**`§4`'s one sentence that is about us.** "Implementations that make use of CDDL
models operationally already need to ascertain the provenance (and thus
authenticity and integrity) and applicability of models they employ."
**[analysis]** That is a description of an `ArtifactStatement`. A CDDL model is
an artifact with a content digest, a subject, and a claim about applicability —
`ARCH-0001` §4.1's own vocabulary — so **m-of-n can attest its own schema**, and
the IETF has independently stated the requirement that would make doing so
useful. Worth recording for `D4`: the schema is not infrastructure outside the
trust model, it is an object inside it.

**The provenance habit, as a model for `R-O-03`.** The Acknowledgments: "In one
of the ensuing discussions, Doug Ewell proposed defining an ABNF rule
"NONASCII", of which we have included the essence." The single rule carrying
the entire surrogate fix is credited to someone outside the authorship, in the
document itself. `R-O-03` asks for exactly that discipline of us —
"Canonicalization algorithm for each concrete encoding SHALL be cited, not
invented silently" — and this is what honouring it looks like in an RFC.

---

## What we adapt

**We write RFC 9682 CDDL but do not use `\u{hex}` in CDDL we author.**
`§2` denies forward compatibility for exactly this addition: "CDDL
specifications that make use of this syntax do not necessarily work with
existing implementations until these are updated, which is recommended by this
specification" — the source closes the parenthetical it opened, so the span
stops before its ")". **[analysis]** Taking the restriction without taking the
addition puts us on the safe side of that sentence: an un-updated tool reads
our schema correctly, and our schema contains nothing an updated tool reads
differently. The addition buys us nothing — rule names are constrained to
`id = EALPHA *(*("-" / ".") (EALPHA / DIGIT))` regardless, and for text
*values* our fixtures should pin bytes rather than spellings (see below).

**Fixtures pin bytes, not CDDL spellings, and Figure 6 is the argument.**
`§2.2` asserts "the rules a to c and x to z all produce strings with byte-wise
identical content", and Figure 6 shows all six resolving to
`446f6d696e6f277320f09f81b3202b20e28c98`. Three spellings of one text string
and three of one byte string. **[analysis]** So a fixture that records the CDDL
literal records a *choice of spelling*; only the hex records the value. Our
vector files must carry the bytes as the authority and the literal as
illustration — which is what `examples/vectors.yaml` does here, and it is why
the six one-line `instance` values in that file are declared **ours** rather
than quoted.

**The two-stage model for prefixed byte strings, with a warning about where it
is written.** Appendix B.2: syntax first by `bytes`/`BCHAR`, then "the rules in
Figure 14 (as updated by Figure 4) are applied to the result of this processing
where bsqual is given as h or b64." **[correction]** This is the only statement
of the model, and the appendix opens "This appendix is informative." RFC 8610
carried the equivalent caveat inside an appendix declared *normative*. Anything
we build on `h'…'` comment handling is building on informative text.

---

## What we reject, or do not carry

**`#6`/`#7` head-number ranges — the whole of `§3.2`.** `head-number = uint /
("<" type ">")` exists so that a tag-number *range* can be written, and the
motivating case is a registered one: "[RFC9277] has a range of tag numbers
1668546817 (0x63740101) to 1668612095 (0x6374FFFF) to tag specific content
formats." **Under option 5 we have no IANA tag numbers to range over**, by the
option's own terms — "no reliance on the IANA CBOR Tags registry and no native
use of COSE header parameters". The `#7` half is no better: `ARCH-0001` §4.1
uses simple values 20, 21 and 22 only, three literals, no range.

**Appendix A as "the whole grammar".** Figures 8 and 10 are each captioned for
"Appendices B and C of RFC 8610" — note the plural — and this document
reproduces RFC 8610's
Appendix B and **none of its Appendix C**. So the matching-rule half of two
updates is stated in a figure caption and nowhere else. Extracted as
`rfc-9682#R-0043` and `rfc-9682#R-0050` precisely because nothing else carries
it.

**Any reading of `§4` as a threat model we can inherit.** "At the time of
writing, it is expected that the models will generally be processed by a
software developer, within a software development environment."
**[analysis]** That is false for us. An m-of-n verifier evaluates a schema on an
automated policy path, with no developer in the loop, and `ARCH-0002` P5's *may
traverse, must never accept* assumes hostile input throughout. RFC 8610 §5's
"does not bring any security issues on itself" is weaker still. Our schema
handling needs its own threat statement; neither document supplies one.

---

## Where this cuts against MD-3

`MD-3` narrowed DEC-002 to **option 5** (CBOR data model, no IANA tags, COSE
export only, YAML as the human form) on 2026-09-28. Five cuts, each naming the
option it favours. **[analysis]** throughout — the document takes no view on
our decision.

**Cut 1 — `§3.2`, this document's principal new capability, is dead weight
under option 5 and live under option 2.** The feature exists to range over
registered tag numbers. Option 2 ("CBOR + CDDL as canonical; COSE for signed
form") would use it the day RFC 9277-style content-format tagging entered our
export path; option 5 forswears the registry those numbers come from. This is
a narrow point and it is the only one in this document that favours **option
2** outright: option 5 pays a cost here that option 2 does not, and it is
exactly the cost `ADR-0001` accepted knowingly when it said CBOR tags "are IANA
allocated, so they are interchange, not native".

**Cut 2 — the escape fix moves CDDL *towards* JSON's string model, narrowing
one of the arguments for option 2/5 over option 3.** `§2.1.1` names the defect
as a *divergence from JSON*: the old grammar "critically misses out on" the
`\uXXXX` and `\uHHHH\uLLLL` forms "that JSON allows", which "should apply here
according to item 6 of Section 3.1 of [RFC8610]". The fix imports JSON's escape
set verbatim — `\" \/ \\ \b \f \n \r \t \uXXXX` — and adds one form JSON does
not have. **Option 3 (JSON + RFC 8785 JCS) already had this.** So on the axis
of *string-literal determinacy in the schema language*, option 3's advantage
was real and is now matched rather than beaten. It does not revive option 3 —
`DECISIONS-0001`'s standing note says option 3 "should be withdrawn rather than
out-scored", on four grounds that this document does not touch — but it removes
one item from the column that out-scored it.

**Cut 3 — MD-3's YAML half loses, and this document shows why without
mentioning YAML.** `§2`'s entire subject is making a *text* schema language
unambiguous about *bytes*, and CDDL's answer is lexical: the quote character
decides the type (`"x"` is a text string, `'x'` a byte string), and the escape
set is exhaustive. The `rfc-8949` extraction's finding, which MD-3 predates:
YAML has no byte type, so a text string and a byte string share one YAML scalar
and the mapping is not injective. **YAML has neither of CDDL's two answers.**
The sibling `draft-ietf-cbor-edn-literals` record reaches the same conclusion
from the other direction and names CDN/EDN as the human form. This cut is
**option-neutral** on the encoding and decisive on the *human form*: it is
evidence against MD-3's YAML clause, not against option 5.

**Cut 4 — the bare-LF `CRLF` survives, and under `R-O-03` the normalisation we
need does not exist to be cited.** `CRLF = %x0A / %x0D.0A` is carried into the
normative appendix unchanged (`rfc-9682#R-0070`), so a CDDL file with CRLF
endings and the same file with LF endings are **both valid and not
byte-identical**. `R-M-11` requires that "At least one content digest SHALL be
bound in all cases", and `R-O-05` requires the signed payload be "the canonical
encoding verbatim". **[analysis]** The moment we digest a schema file —
which *Cut 1 of what we adopt* says we will — its digest depends on line
endings, and no document of ours or theirs declares a rule. `R-O-03` says the
algorithm "SHALL be cited, not invented silently"; there is **nothing to
cite**, so ours must be declared as ours. This is condition-(5)/(6)-shaped in
`DECISIONS-0001`'s standing note: an *identity* path where divergence fails
silently rather than as a signature mismatch. **Option-neutral, and it binds
whichever option wins.**

**Cut 5 — the new escape syntax multiplies the spellings of one label while
leaving Unicode normalisation exactly where it was.** `DECISIONS-0001`'s
standing note lists condition **(6) a declared Unicode normalisation rule** as
"reachable by no candidate and stated in no document of ours". RFC 9682 does
not supply it, and it makes the gap wider: `"café"`, `"caf\u{e9}"` and
`"caf\u00e9"` are three spellings of one byte sequence, while `"cafe\u{301}"`
is a *fourth* spelling of a different one that renders identically.
**[correction, 2026-10-20, pass 3 (cross-check)]** The third spelling read
`"café"`, byte-identical to the first, so the sentence offered two identical
spellings as three: the escape had been silently resolved into the character
it denotes -- this record's own central hazard, item (c) of
`schema/production-changes.derived.txt`, for a fourth time. Restored as the
bare four-digit JSON form, which `hexchar`'s `non-surrogate` branch adds and
RFC 8610 had no way to write. All three were run through an ABNF recognizer
loaded with Figure 11 and accepted; three is a floor and not a count, because
the braced form admits leading zeros (`"caf\u{0e9}"`) as well. RFC 8610
§3.1 — "Processing of CDDL does not involve Unicode normalization processes" —
is untouched, and §3.8.6 still compares text "bytewise identical". **[analysis]**
Under `ARCH-0002` P1 the local label is user-chosen text, so this is the P1
label space, not a corner case: **two principals can define labels that look
identical, compare unequal, and now have four ways each to be written in a
schema.** Option 5 inherits this from CBOR; option 1 (canonical S-expressions)
is the one candidate whose native identifiers are byte strings rather than text,
which sidesteps it rather than solving it. So this cut puts **option 1** on the
right side of condition (6) — the same direction `DECISIONS-0001`'s standing
note already records RFC 9804's extraction putting it, on four other grounds.

**And one thing that does NOT cut either way, recorded so the absence is
visible.** `§5` is one sentence: "This document has no IANA actions." This
document registers nothing and allocates nothing, so option 5's registry
objection — the whole reason option 5 exists — is neither helped nor hurt by
it. An extraction that reported this document as evidence *for* option 5 would
be reading the narrowing into the source.

---

## Open questions this record raises

1. **Do we digest schema files, and under what line-ending rule?** Cut 4. This
   is answerable now and cheaply, and it blocks nothing until `D4` ships a
   schema. It needs a `DECISIONS-0001` row, not an ADR.
2. **Which CDDL dialect do our fixtures declare?** RFC 8610 alone is wrong
   after this document. The honest declaration is RFC 8610 + RFC 9165 +
   RFC 9682 + RFC 9741, and `[CDDL-MODULES]` is still "Work in Progress". Until
   the other three Tier 2 records are read this answer is provisional.
3. **Is condition (6) answerable at all without changing the label type?**
   Cut 5. If the answer is "only by making labels byte strings", that is a
   DEC-002 input and an `ARCH-0002` P1 input at the same time, and it belongs
   on the DEC-002 ADR's agenda rather than here.
4. **`bsqual` is two prefixes in CDDL and more in EDN.** Appendix B.2 declines
   to close the gap: "Finally, the approach taken lends support to extending
   bsqual in CDDL similar to the way this is done for CBOR diagnostic notation
   in [EDN-LITERALS]." Support lent, not taken. **`library#39` assigns EDN the
   test-vector role**, so a vector written with any other prefix is valid EDN
   and is not a CDDL literal — which means one lexer cannot serve both columns
   of our vector files. Concrete, and it lands on whoever builds the fixture
   pipeline.
5. **Does `#7.<type>` with a type straddling 24..31 have a defined meaning?**
   `§3.2` gives three ranges with two meanings and does not address a
   `head-number` that spans the boundary. We would never write one, but a tool
   we *use* must decide, and the document does not say. Reported as a source
   defect in `schema/grammar-gaps-status.derived.txt`, NEW-2.
