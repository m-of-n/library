---
record: rfc-9741
kind: normative
title: "rfc-9741 — normative statements"
extracted: "2026-10-19"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 9741, "Concise Data Definition Language (CDDL): Additional Control Operators for the Conversion and Processing of Text", Standards Track, March 2025. sha256 `3234aeea39d01b7c1c8e9c70d4d7dc8745852e0b6edbea167a3e55b91e7a9ee3` (602 lines, 28550 bytes, plain text). Quotations are verbatim from the plain-text RFC. Blocks that reproduce tables, figures or CDDL preserve the source's own line breaks and indentation — including the RFC's left margin — inside fenced blocks.

**Why this file is mostly definitions.** `bin/bcp14-count` reports **3** BCP 14
keyword occurrences in 28 KB: two `MUST NOT`s in §2.3 forbidding three C `printf`
specifiers in a format string, and one `RECOMMENDED` in §3.1's implementation-note
aside asking a validator to cover the marker-based subset of `.join`. That is
expected and correct for a grammar extension. This document's normative content is
**fourteen control-operator definitions and their matching rules** — what each
operator's target and controller may be, and what text it matches — not obligations
laid on an actor. The file therefore records the **definitional-normative** material
at the same grain another record would use for MUST statements, exactly as
`records/ietf/rfc-8610/distilled/normative.md` does for CDDL itself (2 keywords in
125 KB) and `records/ietf/draft-ietf-cbor-edn-literals/distilled/normative.md` for
EDN.

**What this document does NOT contain, stated once here because the absence is
load-bearing.** It mentions Unicode normalisation nowhere — the strings
`normaliz`, `normalis`, `NFC`, `NFD`, `NFKC` and `NFKD` do not occur in the
source. "Unicode" occurs once, in §2.3's definition of the `%c` conversion
specifier. The only text-identity property any operator here imposes on a text
result is **validity as UTF-8** (§3.1), and §2.4 says in the document's own words
that it "provides no way to constrain the use of blank space or other
serialization variants". See `design-notes.md` §1.

**Conventions in this file.**

- A bullet `- (§X) "…"` is one contiguous verbatim span of the source. No span is
  spliced from two non-adjacent parts of the document. Contiguity is asserted
  after collapsing runs of whitespace; no interior word, clause or punctuation
  mark was altered, dropped or reordered. The source carries **no form feeds and
  no page footers** (RFC 9741 is an unpaginated v3 text rendering), so there is no
  page-frame decoration to remove — unlike `rfc-8610`.
- **Two declared exceptions, both mechanical, neither healed:**
  1. **One hyphenation break.** At source lines 133/134 the token `left-hand-side`
     is severed by the line break (`…refers to the left-hand-` / `side operand…`).
     The sentence is therefore **not** a contiguous span of the document. It is
     quoted here as **two** bullets, cut where the source cuts it. It is not
     repaired.
  2. **One aside bar.** §3.1's implementation note (source lines 416–428) is set as
     an RFC v3 aside, so every line begins `      |  `. The four spans under
     *§3.1, the implementation-note aside* are contiguous **after removing that
     leading `|` bar and nothing else**; they are marked there, and the same
     removal is declared in `requirements.yaml`. No other line of the document is
     transformed, and the bar removal is confined to lines 416–428.
- Tables, the one figure and all six CDDL fragments are reproduced in fenced
  blocks with their source line range. They are also held as files in
  `schema/` with per-region digests.
- §1.1's BCP 14 boilerplate is quoted below for completeness and is
  **deliberately absent from `requirements.yaml`**: `bin/validate` counts
  requirement texts with boilerplate stripping off, so quoting it there would add
  11 phantom keywords.

---

## §1. Introduction

- (§1) "The Concise Data Definition Language (CDDL), standardized in [RFC8610], provides "control operators" as its main language extension point (Section 3.8 of [RFC8610])."
- (§1) "RFCs have added to this extension point in both an application-specific [RFC9090] and a more general [RFC9165] way."
- (§1) "The present document defines a number of additional generally applicable control operators."
- (§1) "In Table 1, the column marked t is for "target type" (left-hand side), and the column marked c is for "controller type" (right-hand side)."

Table 1, verbatim (source lines 88–119) — the whole of this document in one table:

```
    +===============+=========+=======+==============================+
    | Name          | t       | c     | Purpose                      |
    +===============+=========+=======+==============================+
    | .b64u, .b64c  | text    | bytes | Base64 representation of     |
    |               |         |       | byte strings                 |
    +---------------+---------+-------+------------------------------+
    | .b64u-sloppy, | text    | bytes | Sloppy-tolerant variants of  |
    | .b64c-sloppy  |         |       | the above                    |
    +---------------+---------+-------+------------------------------+
    | .hex, .hexlc, | text    | bytes | Base16 representation of     |
    | .hexuc        |         |       | byte strings                 |
    +---------------+---------+-------+------------------------------+
    | .b32, .h32    | text    | bytes | Base32 representation of     |
    |               |         |       | byte strings                 |
    +---------------+---------+-------+------------------------------+
    | .b45          | text    | bytes | Base45 representation of     |
    |               |         |       | byte strings                 |
    +---------------+---------+-------+------------------------------+
    | .base10       | text    | int   | Text representation of       |
    |               |         |       | integer numbers              |
    +---------------+---------+-------+------------------------------+
    | .printf       | text    | array | Printf-formatted text        |
    |               |         |       | representation of data items |
    +---------------+---------+-------+------------------------------+
    | .json         | text    | any   | Text representation of JSON  |
    |               |         |       | values                       |
    +---------------+---------+-------+------------------------------+
    | .join         | text or | array | Build text or byte string    |
    |               | bytes   |       | from array of components     |
    +---------------+---------+-------+------------------------------+

        Table 1: Summary of New Control Operators in This Document
```


### §1.1. Terminology

- (§1.1) "The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here."
- (§1.1) "Regular expressions mentioned in the text are as defined in [RFC9485]."
- (§1.1) "This specification uses terminology from [RFC8610]."
- (§1.1) "In particular, with respect to control operators, "target" refers to the left-hand-"  *(first half of a sentence severed by the hyphenation break at source lines 133/134)*
- (§1.1) "side operand and "controller" to the right-hand-side operand."  *(second half of the same sentence; it begins mid-token because that is where the source breaks)*
- (§1.1) ""Tool" refers to tools along the lines of that described in Appendix F of [RFC8610]."
- (§1.1) "Note also that the data model underlying CDDL provides for text strings as well as byte strings as two separate types, which are then collectively referred to as "strings"."
- (§1.1) "The term "opinionated" is used in this document to explain that the selection of operators included is somewhat frugal, based on opinions about what the preferred (and likely) usage scenarios will be."
- (§1.1) "Specifically, not including a potential choice doesn't by itself intend to express that the choice is unacceptable; it might still be added in a future registration if these opinions evolve."

## §2. Text Conversion

- (§2) *The section carries no prose of its own; its four subsections follow.*

### §2.1. Byte Strings: Base 16 (Hex), Base 32, Base 45, and Base 64

- (§2.1) "A CDDL model often defines data that are byte strings in essence but need to be transported in various encoded forms, such as base64 or hex."
- (§2.1) "This section defines a number of control operators to model these conversions."
- (§2.1) "The control operators generally are of a form that could be used like this:"

The §2.1 example, verbatim (source lines 159–160):

```
   signature-for-json = text .b64u signature
   signature = bytes .cbor COSE_Sign1
```

- (§2.1) "The specification of these control operators cannot provide full coverage of the large number of transformations in use; it focuses on [RFC4648] and additionally [RFC9285], as shown in Table 2."
- (§2.1) "For the representations defined in [RFC4648], this specification uses names as inspired by Section 8 of RFC 8949 [STD94]:"

Table 2, verbatim (source lines 168–201):

```
   +==============+===========================+========================+
   | Name         | Meaning                   | Reference              |
   +==============+===========================+========================+
   | .b64u        | Base64url, no padding     | Section 5 of           |
   |              |                           | [RFC4648]              |
   +--------------+---------------------------+------------------------+
   | .b64u-sloppy | Base64url, no padding,    | Section 5 of           |
   |              | sloppy                    | [RFC4648]              |
   +--------------+---------------------------+------------------------+
   | .b64c        | Base64 classic, padding   | Section 4 of           |
   |              |                           | [RFC4648]              |
   +--------------+---------------------------+------------------------+
   | .b64c-sloppy | Base64 classic, padding,  | Section 4 of           |
   |              | sloppy                    | [RFC4648]              |
   +--------------+---------------------------+------------------------+
   | .b32         | Base32, no padding        | Section 6 of           |
   |              |                           | [RFC4648]              |
   +--------------+---------------------------+------------------------+
   | .h32         | Base32 with "Extended     | Section 7 of           |
   |              | Hex" alphabet, no padding | [RFC4648]              |
   +--------------+---------------------------+------------------------+
   | .hex         | Base16 (hex), either case | Section 8 of           |
   |              |                           | [RFC4648]              |
   +--------------+---------------------------+------------------------+
   | .hexlc       | Base16 (hex), lower case  | Section 8 of           |
   |              |                           | [RFC4648]              |
   +--------------+---------------------------+------------------------+
   | .hexuc       | Base16 (hex), upper case  | Section 8 of           |
   |              |                           | [RFC4648]              |
   +--------------+---------------------------+------------------------+
   | .b45         | Base45                    | [RFC9285]              |
   +--------------+---------------------------+------------------------+

       Table 2: Control Operators for Text Conversion of Byte Strings
```

- (§2.1) "Note that this specification is somewhat opinionated here: It does not provide base64url or base32(hex) encoding with padding or base64 classic without padding."
- (§2.1) "Experience indicates that these combinations only ever occur in error, so the usability of CDDL is increased by not providing them in the first place."
- (§2.1) "Also, adding "c" makes sure that any decision for classic base64 is actively taken."
- (§2.1) "These control operators are "strict" in their matching, i.e., they only match base encodings that conform to the mandates of their defining documents."
- (§2.1) "Note that this also means that .b64u and .b64c only match text strings composed of the set of characters defined for each of them, respectively."
- (§2.1) "(This is perhaps worth pointing out explicitly as it contrasts with the "b64" literal prefix that can be used to notate byte strings in CDDL source code, which simply accepts characters from either alphabet."
- (§2.1) "This behavior is different from the matching behavior of the four base64 control operators defined here.)"
- (§2.1) "The additional designation "sloppy" indicates that the text string is not validated for any additional bits being zero, in variance to what is specified in the paragraph that follows Table 1 in Section 4 of [RFC4648]."
- (§2.1) "Note that the present specification is opinionated again in not specifying a sloppy variant of base32 or base32hex, as no legacy use of sloppy base32(hex) was known at the time of writing."
- (§2.1) "Base45 [RFC9285] is known to be suboptimal for use in environments with limited data transparency (such as URLs) but is included because of its close relationship to QR codes and its wide use in health informatics (note that base45 is strongly specified not to allow sloppy forms of encoding)."

### §2.2. Numerals

Table 3, verbatim (source lines 234–241):

```
           +=========+============================+===========+
           | Name    | Meaning                    | Reference |
           +=========+============================+===========+
           | .base10 | Base-ten (decimal) integer | ---       |
           +---------+----------------------------+-----------+

             Table 3: Control Operator for Text Conversion of
                                 Integers
```

- (§2.2) "The control operator .base10 allows the modeling of text strings that carry an integer number in decimal form (as a text string with digits in the usual base-ten positional numeral system), such as in the uint64/int64 formats of YANG-JSON [RFC7951]."

The §2.2 example, verbatim (source line 248):

```
   yang-json-sid = text .base10 (0..9223372036854775807)
```

- (§2.2) "Again, the specification is opinionated by only providing for integer numbers represented without leading zeros, i.e., the decimal integer numerals match the regular expression 0|-?[1-9][0-9]* (of course, this is further restricted by the control type)."
- (§2.2) "See Section 2.3 for more flexibility and for other numeric bases such as octal, hexadecimal, or binary conversions."
- (§2.2) "Note that this control operator governs text representations of integers and should not be confused with the control operators governing text representations of byte strings (such as .b64u)."
- (§2.2) "This contrast is somewhat reinforced by spelling out "base" in the name .base10 as opposed to those of the byte string operators."

### §2.3. Printf-Style Formatting

Table 4, verbatim (source lines 265–272):

```
     +=========+=========================================+===========+
     | Name    | Meaning                                 | Reference |
     +=========+=========================================+===========+
     | .printf | Printf-style formatting of data item(s) | ---       |
     +---------+-----------------------------------------+-----------+

       Table 4: Control Operator for Printf-Style Formatting of Data
                                  Item(s)
```

- (§2.3) "The control operator .printf allows the modeling of text strings that carry various formatted information, as long as the format can be represented in printf-style formatting strings as they are used in the C language (see Section 7.23.6.1 of [C]; note that the "C23" standard includes %b and %B for formatting into binary digits)."
- (§2.3) "The controller (right-hand side) of the .printf control is an array of one printf-style format string and zero or more data items that fit the individual conversion specifications in the format string."
- (§2.3) "The construct matches a text string representing the textual output of an equivalent C-language printf function call that receives as arguments the format string and the data items following it in the array."
- (§2.3) "Out of the functionality described for printf formatting in Section 7.23.6.1 of the C language specification [C], length modifiers (paragraph 7) are not used and MUST NOT be included in the format string."
- (§2.3) "The "s" conversion specifier (paragraph 8) is used to interpolate a text string in UTF-8 form."
- (§2.3) "The "c" conversion specifier (paragraph 8) represents a single Unicode scalar value as a UTF-8 character."
- (§2.3) "The "p" and "n" conversion specifiers (paragraph 8) are not used and MUST NOT be included in the format string."
- (§2.3) "In the following example, my_alg_19 matches the text string "0x0013":"

Verbatim (source lines 299–300):

```
   my_alg_19 = hexlabel<19>
   hexlabel<K> = text .printf (["0x%04x", K])
```

- (§2.3) "The data items in the controller array do not need to be literals, as in the following example:"

Verbatim (source lines 305–306):

```
   any_alg = hexlabel<1..20>
   hexlabel<K> = text .printf (["0x%04x", K])
```

- (§2.3) "Here, any_alg matches the text strings "0x0013" or "0x0001" but not "0x1234"."

### §2.4. JSON Values

- (§2.4) "Some applications store complete JSON texts [STD90] into text strings."
- (§2.4) "The JSON value of these can easily be defined in CDDL by using the default JSON-to-CBOR conversion rules provided in Section 6.2 of RFC 8949 [STD94]."
- (§2.4) "This is supported by a control operator similar to .cbor as defined in Section 3.8.4 of [RFC8610]."

Table 5, verbatim (source lines 319–327):

```
                      +=======+=========+===========+
                      | Name  | Meaning | Reference |
                      +=======+=========+===========+
                      | .json | JSON    | [STD90]   |
                      +-------+---------+-----------+

                         Table 5: Control Operator
                        for Text Conversion of JSON
                                   Values
```


The §2.4 example, verbatim (source lines 329–330):

```
   embedded-claims = text .json claims
   claims = {iss: text, exp: text}
```


*The six spans that follow are the source's own three-item `Notes:` list (source lines 332–356); the first item runs to four sentences.*

- (§2.4) "JSON has known interoperability problems [RFC7493]."
- (§2.4) "While Section 4 of [RFC7493] probably is not relevant to this specification, Section 2 of [RFC7493] provides requirements that need to be followed to make use of the generic data model underlying CDDL."
- (§2.4) "Note that the intention of Section 2.2 of [RFC7493] is directly supported by Section 6.2 of RFC 8949 [STD94]."
- (§2.4) "The recommendation to use text strings for representing numbers outside JSON's interoperable range is a requirement on the application data model and therefore needs to be reflected on the right-hand side of the .json control operator."
- (§2.4) "This control operator provides no way to constrain the use of blank space or other serialization variants in the JSON representation of the data items; restrictions on the serialization to specific variants (e.g., not providing for the addition of any insignificant blank space and prescribing an order in which map entries are serialized) could be defined in future control operators."
- (§2.4) "A .jsonseq is not provided in this document for JSON text sequences [RFC7464], as no use case for inclusion in CDDL is known at the time of writing; again, future control operators could address this use case."

## §3. Text Processing

- (§3) *The section carries no prose of its own; §3.1 follows.*

### §3.1. Join

- (§3.1) "Often, text strings need to be constructed out of parts that can best be modeled as an array."

Table 6, verbatim (source lines 365–372):

```
         +=======+==================================+===========+
         | Name  | Meaning                          | Reference |
         +=======+==================================+===========+
         | .join | Concatenate elements of an array | ---       |
         +-------+----------------------------------+-----------+

            Table 6: Control Operator for Text Generation from
                                  Arrays
```

- (§3.1) "For example, an IPv4 address in dotted-decimal might be modeled as in Figure 1."

Figure 1 with its caption, verbatim (source lines 377–384):

```
   legacy-ip-address = text .join legacy-ip-address-elements
   legacy-ip-address-elements = [bytetext, ".", bytetext, ".",
                                 bytetext, ".", bytetext]
   bytetext = text .base10 byte
   byte = 0..255

      Figure 1: Using the .join Operator to Build Dotted-Decimal IPv4
                                 Addresses
```

- (§3.1) "The elements of the controller array need to be strings (text or byte strings)."
- (§3.1) "The control operator matches a data item if that data item is also a string, built by concatenating the strings in the array."
- (§3.1) "The result of this concatenation is of the same kind of string (text or bytes) as the first element of the array."
- (§3.1) "(If there is no element in the array, the .join construct matches either kind of empty string, obviously further constrained by the control operator target.)"
- (§3.1) "The concatenation is performed on the sequences of bytes in the strings."
- (§3.1) "If the result of the concatenation is a text string, the resulting sequence of bytes only matches the target data item if that result is a valid text string (i.e., valid UTF-8)."
- (§3.1) "Note that in contrast to the algorithm used in Section 3.2.3 of RFC 8949 [STD94], there is no need for all individual byte sequences going into the concatenation to constitute valid text strings."
- (§3.1) "Note that this control operator is hard to validate in the most general case, as this would require full parser functionality."
- (§3.1) "Simple implementation strategies will use array elements with constant values as guideposts ("markers", such as the "." in Figure 1) for isolating the variable elements that need further validation at the CDDL data model level."
- (§3.1) "Therefore, it is recommended to limit the use of .join to simple arrangements where the array elements are laid out explicitly and there are no adjacent variable elements without intervening constant values, and where these constant values do not occur within the text described by the variable elements."
- (§3.1) "If more complex parsing functionality is required, the ABNF control operators (see Section 3 of [RFC9165]) may be useful; however, these cannot reach back into CDDL-specified elements like .join can."

#### §3.1, the implementation-note aside

- (§3.1) "Implementation note: A validator implementation can use the marker elements to scan the text and isolate the variable elements."
- (§3.1) "It also can build a parsing regexp from the elements of the controller array, with capture groups for each element, and validate the captures against the elements of the array."
- (§3.1) "(For more about parsing regexps, see Section 6 of [RFC9485]; see also Section 8 of [RFC9485] for security considerations related to regexps.)"
- (§3.1) "In the most general case, these implementation strategies can exhibit false negatives, where the implementation cannot find the structure that would be successfully validated using the controller; it is RECOMMENDED that implementations provide full coverage at least for the marker-based subset outlined in the previous paragraph."

## §4. IANA Considerations

- (§4) "IANA has registered the contents of Table 7 into the "CDDL Control Operators" registry of [IANA.cddl]:"

Table 7, verbatim (source lines 435–468):

```
                       +==============+===========+
                       | Name         | Reference |
                       +==============+===========+
                       | .b64u        | RFC 9741  |
                       +--------------+-----------+
                       | .b64u-sloppy | RFC 9741  |
                       +--------------+-----------+
                       | .b64c        | RFC 9741  |
                       +--------------+-----------+
                       | .b64c-sloppy | RFC 9741  |
                       +--------------+-----------+
                       | .b45         | RFC 9741  |
                       +--------------+-----------+
                       | .b32         | RFC 9741  |
                       +--------------+-----------+
                       | .h32         | RFC 9741  |
                       +--------------+-----------+
                       | .hex         | RFC 9741  |
                       +--------------+-----------+
                       | .hexlc       | RFC 9741  |
                       +--------------+-----------+
                       | .hexuc       | RFC 9741  |
                       +--------------+-----------+
                       | .base10      | RFC 9741  |
                       +--------------+-----------+
                       | .printf      | RFC 9741  |
                       +--------------+-----------+
                       | .json        | RFC 9741  |
                       +--------------+-----------+
                       | .join        | RFC 9741  |
                       +--------------+-----------+

                           Table 7: New Control
                                Operators
```


## §5. Security Considerations

- (§5) "The security considerations in Section 5 of [RFC8610] apply."
- (§5) "In addition, for the control operators defined in Section 2.1, the security considerations in Section 12 of [RFC4648] apply."

## §6.1. Normative References — the two entries that carry force

- (§6.1) "International Organization for Standardization, "Information technology - Programming languages - C", Fourth Edition, ISO/IEC 9899:2024, October 2024, <https://www.iso.org/standard/82075.html>."
- (§6.1) "Technically equivalent specification text is available at <https://www.open-std.org/jtc1/sc22/wg14/www/docs/ n3220.pdf>."

---

## What is not here

- **§6 References** — the two `[C]` entries above are quoted because they are the
  normative definition of `.printf`'s matching relation and the only free
  substitute for it. The remaining 14 entries are ordinary citations.
- **Acknowledgements, Author's Address, the lists of Figures and Tables, the
  Abstract and the Status-of-This-Memo boilerplate** — no normative content. The
  Abstract restates §1 and is not quoted separately.
- **§2 and §3** carry a heading and nothing else; both are noted in place.

