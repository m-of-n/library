---
record: rfc-8742
kind: normative
title: "rfc-8742 — normative statements"
extracted: "2026-10-20"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 8742, "Concise Binary Object Representation (CBOR) Sequences", Standards Track, February 2020. sha256 `4462966836b60f42ebae9b5f1d2a479c328e16f0380a3434311a083bccbce30e` (462 lines, 18421 bytes, plain text). Quotations are verbatim from the plain-text RFC. Blocks that reproduce the table, the CDDL fragments, the diagnostic-notation examples or the IANA registration templates preserve the source's own line breaks and indentation — including the RFC's left margin — inside fenced blocks.

**Why this file is mostly definitions, and why that is the finding rather than a
shortfall.** `bin/bcp14-count` reports **4** BCP 14 keyword occurrences in 18 KB:
one `MUST` (§5, fail gracefully) and three `SHOULD`s (§3, the suffix test; §6.3
twice, fragment identifiers). **§2 — the entire format — contains none of them.**
The format is defined by a two-case recursive definition and a two-case decoding
rule, neither carrying a keyword, so this file records the *definitional*
normative material at the same grain another record would use for MUSTs. That is
the same treatment `records/ietf/rfc-8610/distilled/normative.md` gives CDDL
(2 keywords in 125 KB) and `records/ietf/rfc-9741/distilled/normative.md` gives
RFC 9741 (3 in 28 KB).

**Two further facts about the keyword count, both load-bearing, both stated once
here.**

1. **One of the four is unsatisfiable at publication, by the document's own
   admission — and it is a deferral, not a void.** §6.3's **first** `SHOULD`
   (`rfc-8742#R-0055`) governs fragment identifiers for `+cbor-seq` by reference
   to the syntax "specified for "application/cbor-seq"" — which §6.1 registers as
   **"Fragment identifier considerations: N/A"**, and which §6.3 then confirms in
   a parenthesis: "(At the time of publication of this document, there is no
   fragment identification syntax defined for "application/cbor-seq".)" Note the
   temporal qualifier: the rule binds if and when such a syntax is registered.
   §6.3's **second** `SHOULD` (`rfc-8742#R-0057`) is a different matter — its
   three cases collapse onto the third, "For cases not defined in +cbor-seq,
   process as specified in "xxx/yyy+cbor-seq"", which with no `+cbor-seq` rules
   is **universal and determinate at publication**. *(`[correction]` 2026-10-20,
   pass 2: this item read "Two of the four are vacuous at publication … So half
   the document's normative content points at a referent the same document
   declares not to exist." Overturned; `design-notes.md` §7 defect 1 carries the
   argument and the replacement defect.)*
2. **The document uses lower-case `must` where an uppercase keyword would be
   expected, and §1.1 binds keywords "when, and only when, they appear in all
   capitals".** The **one sentence that states how to decode the format** is
   lower case (§2, `rfc-8742#R-0019`), and so is "decoders must operate on input
   that is assumed to be untrusted" (§5, `rfc-8742#R-0043`) — the sentence
   immediately before the one uppercase `MUST`. Neither is counted, by
   `bin/bcp14-count` or here.

**Conventions in this file.**

- A bullet `- (§X) "…"  `rfc-8742#R-NNNN`` is one contiguous verbatim span of the
  source, carrying the id it holds in `requirements.yaml`. No span is spliced
  from two non-adjacent parts of the document. Contiguity is asserted after
  collapsing runs of whitespace; no interior word, clause or punctuation mark was
  altered, dropped or reordered.
- **No transformation of any kind was applied.** The source carries **no form
  feeds, no page footers, no running headers and no trailing whitespace on any
  line** (RFC 8742 is an unpaginated v3 text rendering), so there is no page
  decoration to remove. There is **no aside** in this document and therefore no
  aside bar to strip — unlike `rfc-9741` §3.1 and `rfc-9277` Appendix B. There is
  **no healed hyphenation**: three hyphenation breaks exist (source lines 16/17,
  373/374, 393/394) and **none falls inside a quoted span**, so no sentence
  needed splitting. The two inside §6.3 and §7.1 are carried verbatim by line
  range in `schema/registrations.txt` instead.
- The cached rendering begins with a **UTF-8 BOM** (U+FEFF) alone on line 1. It
  is part of the hashed bytes and part of no quoted span. (It is worth one
  sentence because this record's sibling `rfc-9277` is about magic numbers: the
  *text rendering* of RFC 8742 has one, and the format it specifies does not.)
- The table, both §4.1 CDDL fragments, the §4.3 CDDL fragment, the §4.2
  diagnostic-notation examples and both IANA registration templates are
  reproduced in fenced blocks with their source line range. They are also held
  as files in `schema/` with per-region digests.
- §1.1's BCP 14 boilerplate is quoted below for completeness and is
  **deliberately absent from `requirements.yaml`**: `bin/validate` counts
  requirement texts with boilerplate stripping off, so quoting it there would add
  11 phantom keywords and make the extraction read 15 against a source of 4.

---

## Abstract

- (Abstract) "This document describes the Concise Binary Object Representation (CBOR) Sequence format and associated media type "application/cbor-"  *(first half of a sentence severed by the hyphenation break at source lines 16/17; the obligation-bearing content is in §2 and §6.1, and the remainder of this sentence is not quoted)*

## §1. Introduction

- (§1) "The Concise Binary Object Representation (CBOR) [RFC7049] can be used for serialization of data in the JSON [RFC8259] data model or in its own, somewhat expanded, data model."  *(`rfc-8742#R-0001`)*
- (§1) "This document describes the concept and format of "CBOR Sequences", which are composed of zero or more encoded CBOR data items."  *(`rfc-8742#R-0002`)*
- (§1) "CBOR Sequences can be consumed (and produced) incrementally without requiring a streaming CBOR parser that is able to deliver substructures of a data item incrementally (or a streaming encoder able to encode from substructures incrementally)."  *(`rfc-8742#R-0003`)*
- (§1) "This document defines and registers the "application/cbor-seq" media type in the "Media Types" registry along with a Constrained Application Protocol (CoAP) Content-Format identifier."  *(`rfc-8742#R-0004`)*
- (§1) "CBOR [RFC7049] defines the "+cbor" structured syntax suffix."  *(`rfc-8742#R-0005`)*
- (§1) "Media type structured syntax suffixes [RFC6838] were introduced as a way for a media type to signal that it is based on another media type as its foundation."  *(**no id.** `[correction]` 2026-10-20, pass 2: dropped at pass 1, source lines 96–98. It is the sentence that states **what a structured syntax suffix is for**, which is the premise of §3's whole `SHOULD` test and of §6.3's registration, and it is the document's only characterisation of RFC 6838's mechanism — a reference this record classifies as informative-but-used-normatively in §7 defect 5. See `requirements.yaml` `verify_pass`)*
- (§1) "This document defines and registers the "+cbor-seq" structured syntax suffix in the "Structured Syntax Suffix Registry"."  *(`rfc-8742#R-0006`)*

### §1.1. Conventions Used in This Document

- (§1.1) "The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here."  *(quoted for completeness; **not** in `requirements.yaml` — see Conventions above)*
- (§1.1) "In this specification, the term "byte" is used in its now-customary sense as a synonym for "octet"."  *(`rfc-8742#R-0007`)*

## §2. CBOR Sequence Format

**This section is the whole format, and it carries no BCP 14 keyword.** The
definition is recursive with exactly two cases; the decoding rule is recursive
with exactly two cases; and three separate statements here say that a sequence
cannot report its own completeness (`rfc-8742#R-0009`, `rfc-8742#R-0013`,
`rfc-8742#R-0024`).

- (§2) "Formally, a CBOR Sequence is a sequence of bytes that is recursively defined as either of the following:"  *(`rfc-8742#R-0008`)*
- (§2) "an empty (zero-length) sequence of bytes"  *(`rfc-8742#R-0009` — the empty byte string is a valid CBOR Sequence — 1 of 3)*
- (§2) "the sequence of bytes making up an encoded CBOR data item [RFC7049] followed by a CBOR Sequence."  *(`rfc-8742#R-0010`)*
- (§2) "In short, concatenating zero or more encoded CBOR data items generates a CBOR Sequence."  *(`rfc-8742#R-0011`)*
- (§2) "(Consequently, concatenating zero or more CBOR Sequences also results in a CBOR Sequence.)"  *(`rfc-8742#R-0012`)*
- (§2) "There is no end-of-sequence indicator."  *(`rfc-8742#R-0013` — no end-of-sequence indicator — 2 of 3)*
- (§2) "(If one is desired, CBOR encoding an array of the CBOR data model values being encoded, employing either a definite or an indefinite length encoding, as a single CBOR data item may actually be the more appropriate representation.)"  *(`rfc-8742#R-0014`)*
- (§2) "CBOR Sequences, unlike JSON Text Sequences [RFC7464], do not use a marker between items."  *(`rfc-8742#R-0015`)*
- (§2) "This is possible because CBOR-encoded data items are self delimiting and the end can always be calculated."  *(`rfc-8742#R-0016`)*
- (§2) "(Note that, while the early object/array-only form of JSON was self delimiting as well, this stopped being the case when simple values such as single numbers were made valid JSON documents.)"  *(**no id.** `[correction]` 2026-10-20, pass 2: dropped at pass 1, source lines 136–138, and it is the **only sentence in §2 that pass 1 did not extract** — §2 otherwise runs `rfc-8742#R-0008` to `#R-0025` with nothing skipped. It matters beyond completeness: it is the only statement **in either lane record** about the JSON side's self-delimitation, and `design-notes.md` §8 refutes the summary's "a JSON text sequence … has a grammar for the whole file" precisely on the ground that nothing in this library speaks to the JSON side. This sentence does — and it cuts the other way, saying JSON *lost* self-delimitation. It does not rescue the refuted claim, since self-delimitation of items is not a whole-file grammar, but it is the evidence the refutation should have weighed and did not. See `requirements.yaml` `verify_pass`)*
- (§2) "Decoding a CBOR Sequence works as follows:"  *(`rfc-8742#R-0017`)*
- (§2) "If the CBOR Sequence is an empty sequence of bytes, the result is an empty sequence of CBOR data model values."  *(`rfc-8742#R-0018`)*
- (§2) "Otherwise, one must decode a single CBOR data item from the bytes of the CBOR Sequence and insert the resulting CBOR data model value at the start of the result of repeating this decoding process recursively with the remaining bytes."  *(`rfc-8742#R-0019` — LOWER-CASE `must`: the one sentence that states how to decode the format carries no BCP 14 force)*
- (§2) "(A streaming decoder would therefore simply deliver zero or more CBOR data model values, each as soon as the bytes making it up are available.)"  *(`rfc-8742#R-0020`)*
- (§2) "This means that if any data item in the sequence is not well formed, it is not possible to reliably decode the rest of the sequence."  *(`rfc-8742#R-0021`)*
- (§2) "(An implementation may be able to recover from some errors in a sequence of bytes that is almost, but not entirely, a well-formed encoded CBOR data item."  *(`rfc-8742#R-0022`)*
- (§2) "Handling malformed data is outside the scope of this specification.)"  *(`rfc-8742#R-0023` — the parenthesis opened by `rfc-8742#R-0022` closes here; the two spans are quoted as the source punctuates them, not welded)*
- (§2) "This also means that the CBOR Sequence format can reliably detect truncation of the bytes making up the last CBOR data item in the sequence, but it cannot detect entirely missing CBOR data items at the end."  *(`rfc-8742#R-0024` — entirely missing items at the end are undetectable — 3 of 3)*
- (§2) "A CBOR Sequence decoder that is used for consuming streaming CBOR Sequence data may simply pause for more data (e.g., by suspending and later resuming decoding) in case a truncated final item is being received."  *(`rfc-8742#R-0025`)*

*(§2 prints no display block: the format is stated entirely in prose. The two
diagnostic-notation instances are §4.2's and are reproduced there.)*

## §3. The "+cbor-seq" Structured Syntax Suffix

- (§3) "The use case for the "+cbor-seq" structured syntax suffix is analogous to that for "+cbor": it SHOULD be used by a media type when the result of parsing the bytes of the media type object as a CBOR Sequence is meaningful and is at least sometimes not just a single CBOR data item."  *(`rfc-8742#R-0026` — **BCP 14 SHOULD — 1 of 4**)*
- (§3) "(Without the qualification at the end, this sentence is trivially true for any +cbor media type, which of course should continue to use the "+cbor" structured syntax suffix.)"  *(`rfc-8742#R-0027` — LOWER-CASE `should`)*
- (§3) "Applications encountering a "+cbor-seq" media type can then either simply use generic processing if all they need is a generic view of the CBOR Sequence or use generic CBOR Sequence tools for initial parsing and then implement their own specific processing on top of that generic parsing tool."  *(`rfc-8742#R-0028`)*

## §4. Practical Considerations

*(§4 is a heading only; it carries no prose of its own. Its three subsections
follow.)*

### §4.1. Specifying CBOR Sequences in Concise Data Definition Language (CDDL)

- (§4.1) "In Concise Data Definition Language (CDDL) [RFC8610], CBOR Sequences are already supported as contents of byte strings using the ".cborseq" control operator (Section 3.8.4 of [RFC8610]) by employing an array as the controller type:"  *(`rfc-8742#R-0029`)*
- (§4.1) "Currently, CDDL does not provide for unadorned CBOR Sequences as a top-level subject of a specification."  *(`rfc-8742#R-0030`)*
- (§4.1) "For now, the suggestion is to use an array for the top-level rule, as is used for the ".cborseq" control operator, and add English text that explains that the specification is really about a CBOR Sequence with the elements of the array:"  *(`rfc-8742#R-0031`)*
- (§4.1) "(Future versions of CDDL may provide a notation for top-level CBOR Sequences, e.g., by using a group as the top-level rule in a CDDL specification.)"  *(`rfc-8742#R-0032`)*

The §4.1 `.cborseq` fragment, verbatim (source lines 195–197):

```
   my-embedded-cbor-seq = bytes .cborseq my-array
   my-array = [* my-element]
   my-element = my-foo / my-bar
```

The §4.1 top-level workaround, verbatim — an array rule plus the English text the next sentence asks for (source lines 206–209):

```
   ; This defines an array, the elements of which are to be used
   ; in a CBOR Sequence:
   my-sequence = [* my-element]
   my-element = my-foo / my-bar
```

### §4.2. Diagnostic Notation

- (§4.2) "CBOR diagnostic notation (see Section 6 of [RFC7049]) or extended diagnostic notation (Appendix G of [RFC8610]) also does not provide for unadorned CBOR Sequences at this time (the latter does provide for CBOR Sequences embedded in a byte string as per Appendix G.3 of [RFC8610])."  *(`rfc-8742#R-0033`)*
- (§4.2) "In a similar spirit to the recommendation for CDDL above, this specification recommends enclosing the CBOR data items in an array."  *(`rfc-8742#R-0034`)*
- (§4.2) "In a more informal setting, where the boundaries within which the notation is used are obvious, it is also possible to leave off the outer brackets for this array, as shown in these two examples:"  *(`rfc-8742#R-0035`)*
- (§4.2) "Note that it is somewhat difficult to discuss zero-length CBOR Sequences in the latter form."  *(`rfc-8742#R-0036`)*

The §4.2 examples, verbatim — the only two instances in the document (source lines 229–231):

```
   [1, 2, 3]

   1, 2, 3
```

### §4.3. Optimizing CBOR Sequences for Skipping Elements

- (§4.3) "In certain applications, being able to efficiently skip an element without the need for decoding its substructure, or efficiently fanning out elements to multi-threaded decoding processes, is of the utmost importance."  *(`rfc-8742#R-0037`)*
- (§4.3) "For these applications, byte strings (which carry length information in bytes) containing embedded CBOR can be used as the elements of a CBOR Sequence:"  *(`rfc-8742#R-0038`)*
- (§4.3) "Within limits, this may also enable recovering from elements that internally are not well formed; the limitation is that the sequence of byte strings does need to be well formed as such."  *(`rfc-8742#R-0039`)*

The §4.3 byte-string-wrapped element, verbatim (source lines 245–249):

```
   ; This defines an array of CBOR byte strings, the elements of which
   ; are to be used in a CBOR Sequence:
   my-sequence = [* my-element]
   my-element = bytes .cbor my-element-structure
   my-element-structure = my-foo / my-bar
```

## §5. Security Considerations

**Three sentences and two parentheses, and one of them is the only statement in
this library's reference set about what per-element COSE does *not* bind.**

- (§5) "The security considerations of CBOR [RFC7049] apply."  *(`rfc-8742#R-0040`)*
- (§5) "This format provides no cryptographic integrity protection of any kind but can be combined with security specifications such as CBOR Object Signing and Encryption (COSE) [RFC8152] to do so."  *(`rfc-8742#R-0041`)*
- (§5) "(COSE protections can be applied to an entire CBOR Sequence or to each of the elements of the sequence independently; in the latter case, additional effort may be required if there is a need to protect the relationship of the elements in the sequence.)"  *(`rfc-8742#R-0042`)*
- (§5) "As usual, decoders must operate on input that is assumed to be untrusted."  *(`rfc-8742#R-0043` — LOWER-CASE `must`, in the sentence immediately before the document's only uppercase `MUST`)*
- (§5) "This means that decoders MUST fail gracefully in the face of malicious inputs."  *(`rfc-8742#R-0044` — **BCP 14 MUST — the only one in the document**)*

## §6. IANA Considerations

*(§6 is a heading only. Three registrations follow, and **not one of them is a
CBOR tag**: a media type, a CoAP Content-Format number and a structured syntax
suffix. All three are out of band — none appears in the encoded bytes.)*

### §6.1. Media Type

- (§6.1) "IANA has registered the media type for CBOR Sequence, application/cbor-seq, as follows:"  *(`rfc-8742#R-0045`)*
- (§6.1) "Magic number(s): N/A"  *(`rfc-8742#R-0046` — **the datum this record was read for**)*
- (§6.1) "File extension(s): N/A"  *(`rfc-8742#R-0047`)*
- (§6.1) "Fragment identifier considerations: N/A"  *(`rfc-8742#R-0048`)*
- (§6.1) "Interoperability considerations: Described herein."  *(`rfc-8742#R-0049` — cites a section that does not exist)*
- (§6.1) "Encoding considerations: binary"  *(`rfc-8742#R-0050`)*
- (§6.1) "Intended usage: COMMON"  *(`rfc-8742#R-0051`)*

The §6.1 media type registration template, verbatim and complete (source lines 278–317):

```
   Type name: application

   Subtype name: cbor-seq

   Required parameters: N/A

   Optional parameters: N/A

   Encoding considerations: binary

   Security considerations: See RFC 8742, Section 5.

   Interoperability considerations: Described herein.

   Published specification: RFC 8742.

   Applications that use this media type: Data serialization and
   deserialization.

   Fragment identifier considerations: N/A

   Additional information:

   *  Deprecated alias names for this type: N/A

   *  Magic number(s): N/A

   *  File extension(s): N/A

   *  Macintosh file type code(s): N/A

   Person & email address to contact for further information:
      cbor@ietf.org

   Intended usage: COMMON

   Author: Carsten Bormann (cabo@tzi.org)

   Change controller: IETF

```

### §6.2. CoAP Content-Format Registration

- (§6.2) "IANA has assigned a CoAP Content-Format ID for the media type "application/cbor-seq", within the "CoAP Content-Formats" subregistry of the "Constrained RESTful Environments (CoRE) Parameters" registry [IANA-CORE-PARAMETERS], from the "Expert Review" (0-255) range ([RFC8126])."  *(`rfc-8742#R-0052`)*
- (§6.2) "The assigned ID is shown in Table 1."  *(`rfc-8742#R-0053`)*

Table 1, verbatim (source lines 326–332):

```
           +----------------------+----------+----+-----------+
           | Media type           | Encoding | ID | Reference |
           +======================+==========+====+===========+
           | application/cbor-seq | -        | 63 | RFC 8742  |
           +----------------------+----------+----+-----------+

                     Table 1: CoAP Content-Format ID
```

### §6.3. Structured Syntax Suffix

- (§6.3) "IANA has registered the "+cbor-seq" structured syntax suffix in accordance with [RFC6838] as follows:"  *(`rfc-8742#R-0054`)*
- (§6.3) "Fragment identifier considerations: The syntax and semantics of fragment identifiers specified for +cbor-seq SHOULD be the same as that specified for "application/cbor-seq"."  *(`rfc-8742#R-0055` — **BCP 14 SHOULD — 3 of 4, and DEFERRED: unsatisfiable at publication, binding if and when a syntax is registered. See `rfc-8742#R-0048` and `rfc-8742#R-0056`.** `[correction]` 2026-10-20, pass 2: this annotation read "and vacuous")*
- (§6.3) "(At the time of publication of this document, there is no fragment identification syntax defined for "application/cbor-seq".)"  *(`rfc-8742#R-0056`)*
- (§6.3) "The syntax and semantics for fragment identifiers for a specific "xxx/yyy+cbor-seq" SHOULD be processed as follows:"  *(`rfc-8742#R-0057` — **BCP 14 SHOULD — 4 of 4, and NOT vacuous: its three cases collapse onto `rfc-8742#R-0060`, which is universal and determinate at publication.** `[correction]` 2026-10-20, pass 2: this annotation read "and vacuous for the same reason"; see `design-notes.md` §7 defect 1)*
- (§6.3) "For cases defined in +cbor-seq, if the fragment identifier resolves per the +cbor-seq rules, then process as specified in +cbor-seq."  *(`rfc-8742#R-0058`)*
- (§6.3) "For cases defined in +cbor-seq, if the fragment identifier does not resolve per the +cbor-seq rules, then process as specified in "xxx/yyy+cbor-seq"."  *(`rfc-8742#R-0059`)*
- (§6.3) "For cases not defined in +cbor-seq, process as specified in "xxx/yyy+cbor-seq"."  *(`rfc-8742#R-0060`)*
- (§6.3) "Interoperability considerations: n/a"  *(`rfc-8742#R-0061` — and §6.1's corresponding field reads "Described herein." for the same format)*

The §6.3 structured syntax suffix registration template, verbatim and complete (source lines 341–377):

```
      Name: CBOR Sequence

      +suffix: +cbor-seq

      References: RFC 8742

      Encoding considerations: binary

      Fragment identifier considerations: The syntax and semantics of
      fragment identifiers specified for +cbor-seq SHOULD be the same as
      that specified for "application/cbor-seq".  (At the time of
      publication of this document, there is no fragment identification
      syntax defined for "application/cbor-seq".)

         The syntax and semantics for fragment identifiers for a
         specific "xxx/yyy+cbor-seq" SHOULD be processed as follows:

         o  For cases defined in +cbor-seq, if the fragment identifier
            resolves per the +cbor-seq rules, then process as specified
            in +cbor-seq.

         o  For cases defined in +cbor-seq, if the fragment identifier
            does not resolve per the +cbor-seq rules, then process as
            specified in "xxx/yyy+cbor-seq".

         o  For cases not defined in +cbor-seq, process as specified in
            "xxx/yyy+cbor-seq".

      Interoperability considerations: n/a

      Security considerations: See RFC 8742, Section 5

      Contact: CBOR WG mailing list (cbor@ietf.org), or any IESG-
      designated successor.

      Author/Change controller: IETF

```

---

## What is NOT in this file, and why

- **§7 References, Acknowledgements and the Author's Address.** Dropped per
  `.claude/skills/extract` §1. Two facts from them are recorded in
  `design-notes.md` because they bear on citation rather than on conformance:
  the normative references are `[IANA-CORE-PARAMETERS]`,
  `[IANA-MEDIA-TYPES]`, `[IANA-STRUCTURED-SYNTAX-SUFFIX]`, `[RFC2119]`,
  **`[RFC7049]`** and `[RFC8174]` — so the format's normative anchor is the
  *obsoleted* CBOR specification — while **`[RFC6838]`, `[RFC8126]` and
  `[RFC8610]` are informative**, although §6.3 registers "in accordance with
  [RFC6838]", §6.2 assigns from a range `[RFC8126]` names, and §4.1 and §4.3
  depend on RFC 8610's control operators.
- **§1's motivation paragraph** about concatenating serializations is carried as
  `rfc-8742#R-0002` and `rfc-8742#R-0003` where it makes a claim, and dropped
  where it is narrative.
- **No test vector is quoted here, because the document prints none.** It prints
  three CDDL fragments, two diagnostic-notation lines and one table, and **not
  one hex octet.** See `examples/README.md`.

### `[correction]` 2026-10-20 — two statements pass 1 dropped

Pass 1 reported this file as 63 spans over 61 requirements with nothing dropped
but the narrative, and the sentence above accounted for §1's motivation
paragraph. A sentence-level coverage sweep of the whole source at pass 2 — mark
every character covered by some requirement `text`, then read every uncovered
run of 70 characters or more — found **two statements that are neither narrative
nor accounted for**, and both are now bullets above marked **no id**: §1's "Media
type structured syntax suffixes [RFC6838] were introduced as a way for a media
type to signal that it is based on another media type as its foundation."
(source 96–98) and **§2's** "(Note that, while the early object/array-only form
of JSON was self delimiting as well, …)" (source 136–138). The second is the only
sentence of §2 the extraction missed, and it is the only statement in this lane
about the JSON side's self-delimitation. Everything else the sweep surfaced is
declared: §1.1's BCP 14 boilerplate (deliberately unquoted, see the header), the
CDDL fragments and registration templates held by line range in `schema/`, Table
1, the references and the author's address. No id was minted: ids are
append-only and `requirements.yaml` asserts source order with no gaps.
`requirements.yaml` `verify_pass` holds the list.

**One difference from the sibling, recorded because it is a lane inconsistency
rather than a defect in either record.** This record extracts **no** Abstract
statement — its 11 locators start at §1 — while `records/ietf/rfc-9277` gives its
Abstract an entry of its own. Both choices are defensible for
an abstract that restates the body; the two records in one lane making different
ones is worth a reader knowing before comparing their counts. (That record's
Abstract entry is its **first** requirement, at locator `Abstract`; its id is not
spelled here because its bare form collides with this record's own first id and
`bin/validate` warns on exactly that.)
