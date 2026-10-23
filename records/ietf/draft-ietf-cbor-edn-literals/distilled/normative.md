---
record: draft-ietf-cbor-edn-literals
kind: normative
title: "draft-ietf-cbor-edn-literals — normative statements"
extracted: "2026-10-19"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. The source's
     section structure is preserved as headings. Motivation, history,
     acknowledgements, the Status of This Memo, the Copyright Notice, the
     Table of Contents, the List of Figures and Tables, the references and
     the Author's Address are dropped.

     RELATION TO requirements.yaml. The bullets below are the SAME 226
     verbatim spans that requirements.yaml carries, regrouped for reading
     rather than for querying: every bullet is one `text` field and every
     `text` field appears once here. The id is given so the two can be
     cross-checked mechanically, and `field`, `verb`, `actor`, `kind` and
     `testable` live only in requirements.yaml.

     IDS R-0216 TO R-0226 were appended by the verify pass (pass 2) for
     statements the extract pass dropped. Ids are never reused, so they
     could not be interleaved in requirements.yaml; here they ARE in their
     document positions, which is what this file is for. The consequence is
     that bullet order tracks the source, not the id number, from §2.3.2
     onwards.

     CONTIGUITY. Each span was checked by script against the cached source
     after removing exactly two classes of plain-text page decoration: the
     running header and footer with their form feeds, and the aside gutter
     the renderer draws as three or more spaces, a vertical bar and two
     spaces. Runs of whitespace were then collapsed. Where the source
     hyphenated a token at a line break the span carries the hyphen and the
     space exactly as the source renders them ('app- extension', 'SHA-
     256'); requirements.yaml names every such break in `field`.

     FENCES are EXACT source line runs, never retyped. Each carries its
     line range and the sha256 of those lines joined by LF. A fence split
     into parts is split where a page frame interrupts it. The draft's
     three-column left margin is preserved inside every fence.

     The Section 1.2 BCP 14 boilerplate is deliberately NOT quoted: it
     constrains nothing and quoting it would add eleven phantom keywords
     to the count bin/validate recomputes. -->

Source: **Concise Diagnostic Notation (CDN)**, `draft-ietf-cbor-edn-literals-27`, C. Bormann, Universität Bremen TZI, **20 July 2026**. Internet-Draft, Intended status: Standards Track, Expires 21 January 2027, `Updates: 8610, 8949 (if approved)`. Cached source sha256 `43cfb1236435a9de62d3c202b7ee653b0f5adbd40d3800bbb9379379dbdbf7e9`.

## §1.2  Terminology and Conventions

- (§1.2) [`R-0001`] “The term "ABNF" in this document refers to the language defined in [STD68] as extended in [RFC7405], where the "characters" of Section 2.3 of RFC 5234 [STD68] are Unicode scalar values.”

## §1.3  (Non-)Objectives of this Document

**Section 8 of RFC 8949, quoted by the draft as the objective of diagnostic notation**

_The draft introduces the quotation and then gives it in an aside; the gutter (`|`) is the renderer's._

<!-- source lines 365-368 (4 lines), sha256 cc7fb0c3481d6e1c9e054164ead9bcfd702b6cb2be42801e3e089b8e4cd5548f -->
```
   common human-readable diagnostic notation with CBOR.  In particular,
   it states:

   |  All actual interchange always happens in the binary format.
```

## §1.3.2  Determinism?

- (§1.3.2) [`R-0002`] “Because of this, a deterministic representation is not defined for CDN.”
- (§1.3.2) [`R-0003`] “More generally speaking, there is no expectation for "roundtripping": Converting CDN to binary CBOR and back to CDN will generally not achieve exactly the same result as the original input CDN.”

## §1.3.3  Basic Output Format

- (§1.3.3) [`R-0004`] “However, there is a certain expectation that CDN generators can be configured to some basic output format, which:”
- (§1.3.3) [`R-0005`] “looks like JSON where that is possible;”
- (§1.3.3) [`R-0006`] “inserts encoding indicators, if any, only where the binary form differs from Preferred Serialization (Section 4.1 of RFC 8949 [STD94]);”
- (§1.3.3) [`R-0007`] “uses hexadecimal representation (h'') for byte strings, not b64'' or embedded CBOR (<<>>);”
- (§1.3.3) [`R-0008`] “does not generate elaborate blank space (newlines, indentation) for pretty-printing, but does use common blank spaces such as after , and :.”

## §1.3.5  Character Repertoire of Source

- (§1.3.5) [`R-0009`] “Similar to JSON, CDN is designed to enable representing all CBOR data items using a source character repertoire just containing printable ASCII characters (%x20-7e in ABNF) and newlines.”
- (§1.3.5) [`R-0010`] “(Platforms that use just a CARRIAGE RETURN by itself to signify an end of line are no longer relevant and the files they produce are out of scope for this document.)”
- (§1.3.5) [`R-0011`] “To ensure that platforms will generate the same bytes in the CBOR data items created from input in either conversion state, CDN MUST create the same processing result independent of which newline representation is used by its input.”
- (§1.3.5) [`R-0012`] “To deal with this variability in platform presentation of newlines, Unicode CARRIAGE RETURN characters that exist in the input unescaped are ignored as if they were not in the input wherever they appear.”
- (§1.3.5) [`R-0013`] “Specifically, any carriage return characters that may be present in a CDN (text or byte) string literal are not copied into the resulting string.”
- (§1.3.5) [`R-0014`] “If a carriage return is needed in a CBOR string data item, it can be added explicitly, for instance by using the escaped form \r in single-quoted or double-quoted strings.”

## §2  Concise Diagnostic Notation (CDN)

- (§2) [`R-0015`] “CDN is a true superset of JSON as it is defined in [STD90] in conjunction with [RFC7493] (that is, any interoperable [RFC7493] JSON text also is a CDN text), extending it both to cover the greater expressiveness of CBOR and to increase its usability.”
- (§2) [`R-0016`] “CDN borrows the JSON syntax for numbers (integer and floating-point, Section 2.2), certain simple values (Section 2.6), UTF-8 [STD63] text strings, arrays, and maps (maps are called objects in JSON; the diagnostic notation extends JSON here by allowing any data item in the map key position).”
- (§2) [`R-0017`] “Many of the forms of literals provided are predefined by this document, but it also defines an extension point that enables defining additional _application-oriented extension literals_.”
- (§2) [`R-0018`] “As CDN is used for truly diagnostic purposes, its implementations MAY support generation and possibly ingestion of CDN for CBOR data items that are well-formed but not valid.”
- (§2) [`R-0019`] “It is RECOMMENDED that an implementation enables such usage only explicitly by configuration (such as an API or CLI flag).”

## §2.1  Comments

- (§2.1) [`R-0020`] “CDN provides two comment syntaxes, which can be used where the syntax allows blank space (outside of constructs such as numbers, string literals, etc.):”
- (§2.1) [`R-0021`] “any text that starts with a slash followed by a character that is not a star or a slash, up to another slash, or”
- (§2.1) [`R-0022`] “any text that starts with "/*" up to and including the next following "*/"”
- (§2.1) [`R-0023`] “In a position that allows blank space, any text starting with "#" or "//" and ending with and including the end of the line is considered blank space (and thus effectively a comment).”
- (§2.1) [`R-0024`] “Note that app-extensions can define their own internal comment syntaxes for text inside strings, which may or may not mimic the overall comment syntax of CDN.”

## §2.1.1  Discussion

- (§2.1.1) [`R-0025`] “delimited comments that were allowed by Appendix G.6 of [RFC8610] in two ways:”
- (§2.1.1) [`R-0026`] “Inline comments no longer can be empty: The construct "//" that was an empty comment in Appendix G.6 of [RFC8610] is now used instead to introduce an end-of-line comment.”
- (§2.1.1) [`R-0027`] “Enabling the use of C-style inline comments can extend the scope of what previously were parsed as slash-delimited comments: for instance, "/*foo/" was a complete comment in Appendix G.6 of [RFC8610] and now is the beginning of a C-style comment that goes on up to a "*/".”

## §2.2  Numbers

- (§2.2) [`R-0028`] “In addition to JSON's decimal number literals, CDN provides hexadecimal, octal, and binary number literals in the usual C-language notation (0x, 0o prefix only, and 0b, respectively).”
- (§2.2) [`R-0029`] “Numbers composed only of digits (of the respective base) are interpreted as CBOR integers (major type 0/1, or where the number cannot be represented in this way, major type 6 with tag 2/3).”
- (§2.2) [`R-0030`] “A leading "+" sign is a no-op, and a leading "-" sign inverts the sign of the number.”
- (§2.2) [`R-0031`] “Using a decimal point (.) and/or an exponent (e for decimal, p for hexadecimal) turns the number into a floating point number (part of major type 7) instead, irrespective of whether it is an integral number mathematically.”
- (§2.2) [`R-0032`] “Note that, in floating point numbers, 0.0 is not the same number as -0.0, even if they are mathematically equal.”
- (§2.2) [`R-0033`] “The non-finite floating-point values Infinity, -Infinity, and NaN are written exactly as in this sentence (this is also a way they can be written in JavaScript, although JSON does not allow them).”
- (§2.2) [`R-0034`] “NaN in CDN stands for the NaN value with a zero sign bit and an all-zero significand except for a set quiet bit; this is represented as F9 7E 00 in CBOR Preferred Serialization.”
- (§2.2) [`R-0035`] “(Note that literals for further number formats, e.g., for representing rational numbers as fractions, or for other NaN values than the one called NaN, can be added as app-extensions.”

**Table 1: Example Sets of Equivalent Notations for Some Numbers**

<!-- source lines 789-807 (19 lines), sha256 11a3e8abaa833520cb3afde7441d0a01e68bffa7e96551fc559a319e5825dd2e -->
```
      +========================================+===================+
      | CDN                                    | CBOR hex          |
      +========================================+===================+
      | 4711, 0x1267, 0o11147, 0b1001001100111 | 19 1267 # uint    |
      +----------------------------------------+-------------------+
      | 1.5, 0.15e1, 15e-1, 0x1.8p0, 0x18p-4   | F9 3E00 # float16 |
      +----------------------------------------+-------------------+
      | 0, +0, -0                              | 00      # uint    |
      +----------------------------------------+-------------------+
      | 0.0, +0.0                              | F9 0000 # float16 |
      +----------------------------------------+-------------------+
      | -0.0                                   | F9 8000 # float16 |
      +----------------------------------------+-------------------+
      | Infinity                               | F9 7C00 # float16 |
      +----------------------------------------+-------------------+
      | -Infinity                              | F9 FC00 # float16 |
      +----------------------------------------+-------------------+
      | NaN                                    | F9 7E00 # float16 |
      +----------------------------------------+-------------------+
```

**Table 2: Encoding indicators on floating point values**

_Reproduced with the draft's aside gutter (`|`) intact._

<!-- source lines 845-877 (33 lines), sha256 c9790bd1fad43e960c3f56c445232cfd0bc3487bfa2b9d00e5e77f7787f5f46c -->
```
      |           +========================+=====================+
      |           | CDN                    | CBOR hex            |
      |           +========================+=====================+
      |           | 1.1                    | fb 3ff199999999999a |
      |           +------------------------+---------------------+
      |           | 1.1_1, 1.1_2           | (error)             |
      |           +------------------------+---------------------+
      |           | 1.1_3                  | fb 3ff199999999999a |
      |           +------------------------+---------------------+
      |           | 1.5, 1.5_1             | f9 3e00             |
      |           +------------------------+---------------------+
      |           | 1.5_2                  | fa 3fc00000         |
      |           +------------------------+---------------------+
      |           | 1.5_3                  | fb 3ff8000000000000 |
      |           +------------------------+---------------------+
      |           | Infinity, Infinity_1   | f9 7c00             |
      |           +------------------------+---------------------+
      |           | Infinity_2             | fa 7f800000         |
      |           +------------------------+---------------------+
      |           | Infinity_3             | fb 7ff0000000000000 |
      |           +------------------------+---------------------+
      |           | -Infinity, -Infinity_1 | f9 fc00             |
      |           +------------------------+---------------------+
      |           | -Infinity_2            | fa ff800000         |
      |           +------------------------+---------------------+
      |           | -Infinity_3            | fb fff0000000000000 |
      |           +------------------------+---------------------+
      |           | NaN, NaN_1             | f9 7e00             |
      |           +------------------------+---------------------+
      |           | NaN_2                  | fa 7fc00000         |
      |           +------------------------+---------------------+
      |           | NaN_3                  | fb 7ff8000000000000 |
      |           +------------------------+---------------------+
```

## §2.3  Strings

- (§2.3) [`R-0036`] “CBOR distinguishes two kinds of strings: text strings (the bytes in the string constitute UTF-8 [STD63] text, major type 3), and byte strings (CBOR does not further characterize the bytes that constitute the string, major type 2).”
- (§2.3) [`R-0037`] “(UTF-8) text strings can be directly represented (unprefixed) in CDN either as double-quoted (Section 2.3.1) or as raw strings (Section 2.3.3), while byte strings can be represented as single- quoted strings (Section 2.3.2).”
- (§2.3) [`R-0038`] “Before prefixed literals were turned into a general extension point for diagnostic notation, Appendix G.4 of [RFC8610] added a syntax for concatenating strings by just juxtaposing them. This syntax was not widely implemented and is problematic in the presence of optional commas; it is now entirely removed from CDN and replaced by app-extensions such as Section 3.5.”

## §2.3.1  Double-Quoted String Literals

- (§2.3.1) [`R-0039`] “This also applies to CDN, and all escaping rules apply as in JSON, with a single exception: In CDN, string literals additionally can contain newlines (LINEFEED U+000A), which are copied into the resulting string like other characters in the string literal.”
- (§2.3.1) [`R-0040`] “CDN keeps it, but also adds the syntax \u{NNN} where NNN is the Unicode scalar value as a hexadecimal number.”

## §2.3.2  Single-Quoted String Literals

- (§2.3.2) [`R-0041`] “Analogously to text-string literals delimited by double quotes, CDN allows the use of single quotes (without a prefix) to express byte- string literals with UTF-8 text; for instance, the following are equivalent:”
- (§2.3.2) [`R-0216`] “The escaping rules of JSON strings are applied equivalently for text- based byte-string literals, e.g., \\ stands for a single backslash and \' stands for a single quote. However, to facilitate parsing, in single-quoted strings CDN excludes certain escaping mechanisms available for double-quoted strings:”
- (§2.3.2) [`R-0042`] “\/ is an escape in JSON that is available for double-quoted CDN text strings as well to ensure all JSON texts are CDN literals. Since CDN's single-quoted strings do not occur in JSON, this legacy compatibility feature is not available for them.”
- (§2.3.2) [`R-0043`] “\u-based escapes are not available for characters in the range from U+0020 through U+007E (essentially, printable ASCII).”
- (§2.3.2) [`R-0044`] “All other escaping mechanisms that are available in double-quoted string literals are available in single-quoted string literals.”
- (§2.3.2) [`R-0045`] “Single-quoted string literals can occur unprefixed and stand for the byte string that encodes its text string value (the "content"), or be prefixed by what looks like an app-extension prefix (see Section 3).”
- (§2.3.2) [`R-0046`] “In a prefixed string literal, the text content of the single-quoted string literal is not used directly as a byte string, but is further processed in a way that is defined by the meaning given to the prefix. Depending on the prefix, the result of that processing can, but often is not, a byte string value.”
- (§2.3.2) [`R-0047`] “(Additional kinds of base-encoded string literals can be defined as prefixed literals by registering their prefixes; there is no fundamental difference between the original two predefined base-encoded string literal prefixes (Section 3.1: h, b64) and any such potential future extension literal prefixes; for simplicity of expression, both cases are referred to as "prefixed literals".)”

## §2.3.3  Raw String Literals

- (§2.3.3) [`R-0048`] “CDN therefore also allows text strings to be notated as raw string literals, which do not perform any special processing on backslashes, i.e., treat them as raw string content like any other characters.”
- (§2.3.3) [`R-0049`] “Instead, data transparency is provided by enclosing the entire string content in starting and ending delimiters built as a sequence of one or more backquote (»`«, U+0060 GRAVE ACCENT) characters.”
- (§2.3.3) [`R-0050`] “By using more backquotes for each of the outer delimiters than the longest sequence of backquotes that can be found in the string, internal backquotes do not prematurely end the string literal.”
- (§2.3.3) [`R-0051`] “raw strings could not be used for empty string data items, which therefore need to be notated using double- or single-quoted strings.”
- (§2.3.3) [`R-0052`] “any single newline (LF or CRLF, see Section 1.3.5) at the start of the inner string is removed to yield the string content.”
- (§2.3.3) [`R-0053`] “if the first rule does not apply, but the inner string starts with a space character as well as ends with one, exactly one single space character starting the inner string together with exactly one single space character ending the inner string are removed to yield the string content.”
- (§2.3.3) [`R-0054`] “If neither of these rules apply, the inner string between the raw delimiters is used as the raw string unchanged.”

## §2.3.4  CBOR Sequence Literals

- (§2.3.4) [`R-0055`] “In diagnostic notation, a sequence of zero or more CBOR data item literals can be enclosed in << and >> and separated by comma or blank space, optionally prefixed by an app-extension prefix; this specification speaks of _sequence literals_.”
- (§2.3.4) [`R-0217`] “CDN mainly deals with individual data items, not with CBOR sequences [RFC8742], so the CBOR sequence represented by the sequence literal needs to be further processed to obtain the value of the literal.”
- (§2.3.4) [`R-0056`] “Prefixed sequence literals refer to the app-extension (see Section 3) identified by the prefix and apply the extension to its sequence content, resulting in a single data item.”
- (§2.3.4) [`R-0218`] “This data item may be a string or not (always), depending on the definition of the app- extension.”
- (§2.3.4) [`R-0057`] “An unprefixed sequence literal applies CBOR encoding to the data items in its content, taken as a CBOR sequence. The value of the literal thus is a byte string with the encoded content; this is commonly referred to as _embedded CBOR_.”
- (§2.3.4) [`R-0058`] “A diagnostic implementation is expected to honor encoding indicators (please see Section 4) on the individual items in the supplied sequence before assembling them into an encoded CBOR sequence.”
- (§2.3.4) [`R-0059`] “Encoding indicators on the arguments are ignored if the app-extension does not define special handling of encoding variants.”

## §2.3.5  Validity of Text Strings

- (§2.3.5) [`R-0060`] “Double-quoted, single-quoted, and raw string literals have been defined such that they lead to byte sequences that are UTF-8: the source language of CDN is UTF-8, and all escaping mechanisms lead only to adding further UTF-8 characters.”
- (§2.3.5) [`R-0061`] “As discussed at the start of Section 2, CDN implementations MAY support generation and possibly ingestion of CDN for CBOR data items that are well-formed but not valid;”
- (§2.3.5) [`R-0062`] “when this is enabled, such implementations MAY relax the requirement on text strings to be valid UTF-8.”
- (§2.3.5) [`R-0063`] “No additional Unicode processing or validation such as normalization or checking whether a scalar value is actually assigned is foreseen by CDN, particularly not any processing that is dependent on a specific Unicode version.”
- (§2.3.5) [`R-0064`] “Such processing, if offered, MUST NOT get in the way of processing the data item represented in CDN (i.e., it may be appropriate to issue warnings but not to error out or to generate output that does not match the input at the UTF-8 level).”

## §2.4  Arrays and Maps

- (§2.4) [`R-0065`] “For maps, CDN extends the JSON syntax by allowing any data item in the map key position (before the colon).”

## §2.4.1  Mandatory Separators, Optional Terminators

- (§2.4.1) [`R-0066`] “The separator commas are now optional in the places where CDN syntax allows commas; however, where no comma is used in a separator position, there must be blank space (composed of at least one space, newline, and/or comment) instead.”
- (§2.4.1) [`R-0067`] “In addition, CDN also allows, but does not require, a trailing comma before the closing bracket/brace, enabling an easier to maintain "terminator" style of their use.”
- (§2.4.1) [`R-0068`] “As a comma and/or blank/comment is mandatory in a separator position, »[11]« is unambiguously an array with a single element (the integer 11), different from »[1 1]« or »[1,1]«.”
- (§2.4.1) [`R-0069`] “As this is a general rule, »[[] []]« or »[[],[]]« are well-formed CDN, while »[[][]]« is not.”

## §2.4.2  Validity of Maps

- (§2.4.2) [`R-0070`] “As discussed at the start of Section 2, CDN implementations MAY support generation and possibly ingestion of CDN for CBOR data items that are well-formed but not valid (Section 5.3 of RFC 8949 [STD94]).”

## §2.5  Tags

- (§2.5) [`R-0071`] “A tag is written as a decimal unsigned integer (no leading zeros except for the actual tag number zero, i.e., 0|[1-9][0-9]*) for the tag number, followed by the tag content in parentheses;”
- (§2.5) [`R-0072`] “The tag number can be followed by an encoding indicator giving the encoding of the tag head.”

## §2.6  Simple values

- (§2.6) [`R-0073`] “CDN uses JSON syntax for the simple values True (»true«), False (»false«), and Null (»null«). Undefined is written »undefined« as in JavaScript.”
- (§2.6) [`R-0074`] “These and all other simple values can be given as "simple()" with the appropriate decimal unsigned integer (0|[1-9][0-9]*) in the parentheses.”

## §3  Prefixed Literals

- (§3) [`R-0075`] “Prefixed literals start with a _prefix_ that identifies the app- extension and possibly a specific variant of that, immediately followed by a sequence literal (Section 2.3.4) or a single-quoted or raw string literal (Section 2.3).”
- (§3) [`R-0076`] “The string-based forms use their string literal as a shorthand form for a sequence literal representing a sequence with exactly that one text string data item, e.g., b64`Zm9v` is a shorthand for b64<<"Zm9v">> or b64<<`Zm9v`>>”
- (§3) [`R-0077`] “This notation is generalized from Section 8 of RFC 8949 [STD94], which provides for notating byte strings in a number of [RFC4648] base encodings, where the encoded text is enclosed in single quotes, prefixed by a prefix (»h« for base16, »b32« for base32, »h32« for base32hex, »b64« for base64 or base64url).”
- (§3) [`R-0078`] “This syntax can be thought to establish a name space, with the names "h", "b32", "h32", and "b64" taken, but other names being unallocated. The present specification allows registering additional names for this namespace, which it calls _app- extension identifiers_.”
- (§3) [`R-0079`] “More precisely, an _app-extension identifier_ is a registered name consisting of a lowercase ASCII letter ([a-z]) and zero or more additional ASCII characters that are either lowercase letters, digits, or hyphens ([a-z0-9-]).”
- (§3) [`R-0080`] “»false«, »true«, »null«, and »undefined« cannot be used as such identifiers and are reserved.”
- (§3) [`R-0081`] “app-extension identifiers are registered in the "App-Extension Identifiers" registry (Section 7.1).”
- (§3) [`R-0082`] “An app-extension (such as dt) MAY also define the meaning of one additional prefix derived from its app-extension identifier by replacing each lowercase character by its uppercase counterpart (such as DT).”
- (§3) [`R-0083`] “As a convention, using the all-uppercase variant implies making use of a CBOR tag appropriate for this app-extension (such as tag number 1 for DT, where in contrast the prefix dt stands for the unwrapped tag content).”
- (§3) [`R-0084`] “In summary, an app-extension identifier gives rise to one or two prefixes, one that is lexically identical to the identifier (i.e., all lowercase), and potentially another one that is an all-uppercase variation of it.”
- (§3) [`R-0219`] “In addition to specifying which of these two variations exhibits which specific semantics, the app-extension specifies what input the extension takes.”
- (§3) [`R-0085`] “When the prefix is used immediately in front of a single-quoted or a raw string, the input takes the form of a single text string CBOR data item (this is useful only if the app-extension is designed to receive a text string as input).”
- (§3) [`R-0086`] “When used immediately in front of a sequence literal, the input is a CBOR sequence of elements of the sequence literal as input.”
- (§3) [`R-0087`] “The app-extension can provide behavior that depends on the number of items supplied as input to it and their data types; it cannot distinguish between its prefix being used with a single-quoted string, a raw string, or a CBOR sequence composed of a single text string data item (as illustrated for instance in Tables 3, 4, and 5).”
- (§3) [`R-0088`] “Of these, the app-extensions h, b64, t1, b1, dt and ip are mandatory to implement.”

## §3.1  Base-Encoded Byte String Literals: h and b64

- (§3.1) [`R-0089`] “The app-extension identifier selects one of the base encodings [RFC4648], without padding.”
- (§3.1) [`R-0090`] “Most often, the base encoding is enclosed in a single-quoted or raw string literal, prefixed by »h« for base16 or »b64« for base64 or base64url (the actual encodings of the latter two have the same meaning where they overlap, so the string remains unambiguous).”
- (§3.1) [`R-0091`] “(Note that Section 8 of RFC 8949 [STD94] also mentions »b32« for base32 and »h32« for base32hex. This has not been implemented widely and therefore is not directly included in this specification. These and further byte string formats now can easily be added back as prefixed literals.)”
- (§3.1) [`R-0092`] “In the base-encoded byte string literals, blank space is ignored in the input;”
- (§3.1) [`R-0093`] “The internal syntax of prefixed single-quote literals such as h'' and b64'' also allow comments as blank space (see Section 2.1).”
- (§3.1) [`R-0094`] “Slash characters are part of the base64 classic alphabet (see Table 1 in Section 4 of [RFC4648]), and they therefore need to be in the b64'' set of characters that contribute to the byte string. Therefore, only end-of-line comments starting with # are available inside b64 byte string literals.”

## §3.2  Date and Time: dt

- (§3.2) [`R-0095`] “The content of the literal is a single Standard Date/Time String as per Section 3.4.1 of RFC 8949 [STD94], as a text or byte string.”
- (§3.2) [`R-0096`] “The value of the literal is a number representing the result of a conversion of the given Standard Date/Time String to an Epoch-Based Date/Time. If fractional seconds are given in the text (production time-secfrac in Figure 5), the value is a floating-point number; the value is an integer number otherwise.”
- (§3.2) [`R-0097`] “In the all-uppercase variant of the app-prefix, the value is enclosed in a tag number 1.”

**Table 3: dt and DT literals vs. plain CDN**

<!-- source lines 1517-1535 (19 lines), sha256 5044b501acfa57d3e92448b4c98d1c7ddc5f9c2786b8e4740494ed84350ffc52 -->
```
             +================================+==============+
             | dt literal                     | plain CDN    |
             +================================+==============+
             | dt'1969-07-21T02:56:16Z'       | -14159024    |
             +--------------------------------+--------------+
             | dt'1969-07-21T02:56:16.0Z'     | -14159024.0  |
             +--------------------------------+--------------+
             | dt'1969-07-21T02:56:16.5Z'     | -14159023.5  |
             +--------------------------------+--------------+
             | dt`1969-07-21T02:56:16.5Z`     | -14159023.5  |
             +--------------------------------+--------------+
             | dt<<'1969-07-21T02:56:16.5Z'>> | -14159023.5  |
             +--------------------------------+--------------+
             | dt<<"1969-07-21T02:56:16.5Z">> | -14159023.5  |
             +--------------------------------+--------------+
             | dt<<`1969-07-21T02:56:16.5Z`>> | -14159023.5  |
             +--------------------------------+--------------+
             | DT'1969-07-21T02:56:16Z'       | 1(-14159024) |
             +--------------------------------+--------------+
```

## §3.3  IP Addresses and Related Structures: ip

- (§3.3) [`R-0098`] “The input of the literal is a single text string representing an IPv4address or IPv6address as per Section 3.2.2 of [RFC3986].”
- (§3.3) [`R-0099`] “With the lowercase app-string prefix ip, the value of the literal is a byte string representing the binary IP address. With the uppercase app-string prefix IP, the literal is such a byte string tagged with tag number 54, if an IPv6address is used, or tag number 52, if an IPv4address is used.”
- (§3.3) [`R-0100`] “As an additional case, the uppercase app-string prefix IP can be used with an IP address prefix such as 2001:db8::/56 or 192.0.2.0/24, with the equivalent tag as its value.”
- (§3.3) [`R-0101`] “For completeness, the lowercase variant ip'2001:db8::/56' or ip'192.0.2.0/24' stands for an unwrapped [56,h'20010db8'] or [24,h'c00002']; however, in this case the information on whether an address is IPv4 or IPv6 often needs to come from the context.”
- (§3.3) [`R-0102`] “Note that this app-extension provides no direct representation of the "Interface format" defined in Section 3.1.3 of [RFC9164], an address combined with an optional prefix length and an optional zone identifier, and therefore no way to reference a zone identifier at all.”

**Table 4: ip and IP literals vs. plain CDN**

<!-- source lines 1597-1613 (17 lines), sha256 6969f2a7f9486399c453b0576bb4bdbecd061d1278e97b05ed5c5383872051e9 -->
```
     +====================+=========================================+
     | ip literal         | plain CDN                               |
     +====================+=========================================+
     | ip'192.0.2.42'     | h'c000022a'                             |
     +--------------------+-----------------------------------------+
     | ip<<'192.0.2.42'>> | h'c000022a'                             |
     +--------------------+-----------------------------------------+
     | IP'192.0.2.42'     | 52(h'c000022a')                         |
     +--------------------+-----------------------------------------+
     | IP'192.0.2.0/24'   | 52([24,h'c00002'])                      |
     +--------------------+-----------------------------------------+
     | ip'2001:db8::42'   | h'20010db8000000000000000000000042'     |
     +--------------------+-----------------------------------------+
     | IP'2001:db8::42'   | 54(h'20010db8000000000000000000000042') |
     +--------------------+-----------------------------------------+
     | IP'2001:db8::/64'  | 54([64,h'20010db8'])                    |
     +--------------------+-----------------------------------------+
```

## §3.4  Cryptographic Hash Values: hash

- (§3.4) [`R-0103`] “The app-extension identifier "hash" is used to notate the input to a cryptographic hash function as well as to identify such a hash function. Its value is a byte string that represents the output of that hash function.”
- (§3.4) [`R-0104`] “The input of the literal is a (text or byte) string, optionally followed by either an integer or a text string that identifies the hash function in the COSE Algorithms registry of the CBOR Object Signing and Encryption (COSE) registry group [IANA.cose], either by the identifier (value: integer or string), or, if no algorithm is registered with this value, by its name used in the registry.”
- (§3.4) [`R-0105`] “If the second item is not given, the default algorithm used is -16 ("SHA- 256").”
- (§3.4) [`R-0106`] “No uppercase variant prefix is defined for the app-extension identifier "hash".”

**Table 5: hash literals vs. plain CDN**

<!-- source lines 1648-1672 (25 lines), sha256 f319c2e28130319e5a80f29f8602445a1b551e6e82e6a3cd92da08a68eee53a8 -->
```
          +===============+====================================+
          | hash literal  | plain CDN                          |
          +===============+====================================+
          | hash<<'foo'>> | h'2C26B46B68FFC68FF99B453C1D304134 |
          |               | 13422D706483BFA0F98A5E886266E7AE'  |
          +---------------+------------------------------------+
          | hash'foo'     | h'2C26B46B68FFC68FF99B453C1D304134 |
          |               | 13422D706483BFA0F98A5E886266E7AE'  |
          +---------------+------------------------------------+
          | hash<<'foo',  | h'2C26B46B68FFC68FF99B453C1D304134 |
          | -16>>         | 13422D706483BFA0F98A5E886266E7AE'  |
          +---------------+------------------------------------+
          | hash<<'foo',  | h'2C26B46B68FFC68FF99B453C1D304134 |
          | "SHA-256">>   | 13422D706483BFA0F98A5E886266E7AE'  |
          +---------------+------------------------------------+
          | hash<<'foo',  | h'F7FBBA6E0636F890E56FBBF3283E524C |
          | -44>>         | 6FA3204AE298382D624741D0DC663832   |
          |               | 6E282C41BE5E4254D8820772C5518A2C   |
          |               | 5A8C0C7F7EDA19594A7EB539453E1ED7'  |
          +---------------+------------------------------------+
          | hash<<'foo',  | h'F7FBBA6E0636F890E56FBBF3283E524C |
          | "SHA-512">>   | 6FA3204AE298382D624741D0DC663832   |
          |               | 6E282C41BE5E4254D8820772C5518A2C   |
          |               | 5A8C0C7F7EDA19594A7EB539453E1ED7'  |
          +---------------+------------------------------------+
```

## §3.5  String Concatenation: b1 and t1

- (§3.5) [`R-0107`] “The "b1" and "t1" app-extensions allow a (byte or text) string to be built up from multiple (byte or text) string literals; these are then concatenated into a single string.”
- (§3.5) [`R-0108`] “As the examples show, text strings and byte strings can mix within such a concatenation, so that, for instance, byte string literal notation can be used inside a sequence of concatenated text string notation literals, to encode characters that may be better represented in an encoded way.”
- (§3.5) [`R-0109`] “This is realized by simply joining together the bytes in the sequence of string arguments to the b1/t1 app-extension, proceeding from left to right.”
- (§3.5) [`R-0110`] “For "b1", the joining operation results in a byte string. For "t1", the joining operation results in a text string, and the result therefore needs to be valid UTF-8 except for "diagnostic" implementations that support and are enabled for generation/ingestion of CDN for CBOR data items that are well-formed but not valid; see also Section 2.3.5.”
- (§3.5) [`R-0111`] “A single ... is a general ellipsis, which by itself can stand for any data item, but when used as argument to t1/b1 must stand in for a string value.”
- (§3.5) [`R-0112`] “Multiple adjacent ellipses are equivalent to a single ellipsis.”
- (§3.5) [`R-0113`] “When an ellipsis is concatenated (on one or both sides) with strings, the result is a CBOR tag number CPA888 that contains an array with joined together spans of such strings plus the ellipses represented by /CPA/888(null).”
- (§3.5) [`R-0114`] “Arguments with nested ellipses are flattened and the above equivalences applied, so that, for instance, these values are equivalent:”
- (§3.5) [`R-0115`] “If there is no ellipsis in the concatenated list, the result of processing the list will always be a single string data item.”

## §3.6  Creating Indefinite-length Encoded Strings: ilbs and ilts

- (§3.6) [`R-0116`] “The ilbs and ilts app-extensions are semantically identical to t1 and b1 at the data model level, but instead of concatenating the arguments to a single (byte/text) string data item, they build an indefinite length string out of the arguments, with one chunk of the correct major type (byte string/text string for ilbs/ilts, respectively) created per argument.”
- (§3.6) [`R-0117`] “A diagnostic implementation would honor encoding indicators on each of the arguments, creating a chunk with the same encoding. As the app-extension is already implying indefinite length encoding, there is no point in applying an encoding indicator to the entire prefixed literal.”
- (§3.6) [`R-0118`] “There is no way to include ellipses in an indefinite length string.”

## §3.7  Concise Resource Identifiers: The "cri" Extension

- (§3.7) [`R-0119`] “The input of the literal is a URI Reference as per [RFC3986] or an IRI Reference as per [RFC3987].”
- (§3.7) [`R-0120`] “The value of the literal is a CRI reference that can be converted to the text of the literal using the procedure of Section 6.1 of [I-D.ietf-core-href]. Note that there may be more than one CRI reference that can be converted to the URI/IRI reference given; implementations are expected to favor the simplest variant available and make non-surprising choices otherwise.”
- (§3.7) [`R-0121`] “In the all-uppercase variant of the app-prefix, the value is enclosed in a tag number 99.”

## §3.8  Floating-Point Values: float

- (§3.8) [`R-0122`] “The "float" app-extension enables the notation of 2-byte, 4-byte, and 8-byte byte strings to express floating point values (mt=7, ai=25/26/27 respectively) by giving their IEEE 754 representation. A text string used as an argument is interpreted exactly as a hex literal (like the h prefix); the result is used as the byte string.”
- (§3.8) [`R-0123`] “The prefixed literal is interpreted as an encoded data item would be that prefixes the byte string by a single byte 0xF9 (2 bytes, i.e., binary16), 0xFA (4 bytes, i.e., binary32), and 0xFB (8 bytes, i.e., binary64), respectively. Byte strings of a different length than 2, 4, or 8 raise an error. Note that the interpretation as an encoded data item does not create or imply an encoding indicator; that can be added separately.”
- (§3.8) [`R-0124`] “The purpose of this app-extension is to close a gap in CDN's [IEEE754] binary64 support: Without this (or a similar) extension there is no way to represent NaN values different from the one called out at the end of Section 4.1 of RFC 8949 [STD94]”

## §4  Encoding Indicators

- (§4) [`R-0125`] “Encoding indicators are always optional: CDN is usually used to describe CBOR data items at the data model level.”
- (§4) [`R-0126`] “Implementations of CDN generally do not need to provide this functionality in full; if they do, they can be called "diagnostic implementations".”
- (§4) [`R-0127`] “To be able to process CDN that contains encoding indicators, a CDN-consuming implementation MUST accept them (i.e., process or ignore the presence or absence of each encoding indicator).”
- (§4) [`R-0128`] “It is RECOMMENDED to provide a warning for each encoding indicator value that is encountered but not further processed.”
- (§4) [`R-0129`] “Where no encoding indicator is placed, a diagnostic CBOR encoder is expected to generate Preferred Serialization (Section 4.1 of RFC 8949 [STD94]) with definite-length encoding only.”
- (§4) [`R-0130`] “Similarly, when using CDN as output for a diagnostic CBOR decoder, a basic diagnostic configuration of the tool is expected to provide encoding indicators only in places where the CBOR input did not use Preferred Serialization with definite-length encoding (see also Section 1.3.3).”
- (§4) [`R-0131`] “Diagnostic implementations of CDN that process encoding indicators as discussed here are expected to document their diagnostic behavior and the processing options that can be selected.”

## §4.1  Syntax, Semantics, Examples

- (§4.1) [`R-0132`] “Encoding indicators start with an underscore and comprise all immediately following characters that are alphanumeric or underscore.”
- (§4.1) [`R-0133`] “Encoding indicators are placed immediately to the right of the data item or of a syntactic feature that can stand for the data item the encoding of which the encoding indicator is controlling.”
- (§4.1) [`R-0220`] “Encoding indicators can be ignored by anyone not interested in this information.”
- (§4.1) [`R-0134`] “An underscore followed by a decimal digit n indicates that the item was or is to be encoded with an additional information value of ai=24+n.”
- (§4.1) [`R-0221`] “For an example involving floating point values (Section 3.3 of RFC 8949 [STD94]), 1.5_1 is a half-precision floating-point number (2^1 = 2 additional bytes or 16 bits), while 1.5_3 is encoded as double precision (2^3 = 8 additional bytes or 64 bits).”
- (§4.1) [`R-0135`] “For a tool consuming CDN in a diagnostic mode, encountering an encoding indicator that does not provide enough space to correctly encode the unchanged data item given is an error; there is no truncation or rounding that would change the data item encoded.”
- (§4.1) [`R-0136`] “Truncation or rounding semantics imply performing changes at the data model level, which is outside the scope of encoding indicators. Such operations can be provided by app-extensions.”
- (§4.1) [`R-0137`] “The encoding indicator _ (an underscore on its own) is used to indicate indefinite-length encoding.”
- (§4.1) [`R-0138`] “Indefinite-length encoding uses ai=31, which could have been indicated by _7, which is therefore not used and marked as reserved (as are _4, _5, and _6, which would stand for ai=28 to ai=30, values currently not in use in CBOR; these encoding indicators will be available if and when CBOR is extended to make use of them).”
- (§4.1) [`R-0139`] “Note that the encoding indicator _ is only available behind the opening brace/bracket for map and array (Section 4.2): strings originally had a now deprecated special syntax streamstring for indefinite-length encoding except for the special cases”
- (§4.1) [`R-0222`] “Section 8.1 of RFC 8949 [STD94] does not address ai=0 to ai=23 — the assumption seems to have been that Preferred Serialization (Section 4.1 of RFC 8949 [STD94]) will be used when converting CBOR diagnostic notation to an encoded CBOR data item, so leaving out the encoding indicator for a data item with a Preferred Serialization will implicitly use ai=0 to ai=23 if that is possible.”
- (§4.1) [`R-0140`] “The encoding indicators _0 to _3 indicate ai=24 to ai=27, respectively; they therefore stand for 1, 2, 4, and 8 bytes of additional information (ai) following the initial byte in the head of the data item.”
- (§4.1) [`R-0141`] “_i ("immediate") stands for encoding with ai=0 to ai=23, i.e., it indicates that the argument is encoded directly in the initial byte of the CBOR item.”
- (§4.1) [`R-0142`] “Encoding indicators are an extension point for CDN; Section 7.2 defines a registry for additional values.”

**Table 6: Examples of Definite Length Encoding Indicators for Different Data Items**

<!-- source lines 1965-1986 (22 lines), sha256 3a018ba8c33035888cdca2a1fca3113a1a9d31a439fd66d3f738a78975d45215 -->
```
        +====+==============+====================+===============+
        | mt | examples     | encoding (in hex)  | ignoring e.i. |
        +====+==============+====================+===============+
        | 0  | 1_1          | 190001             | 01            |
        |    | 0x4711_3     | 1b0000000000004711 | 194711        |
        +----+--------------+--------------------+---------------+
        | 1  | -1_1         | 390000             | 20            |
        +----+--------------+--------------------+---------------+
        | 2  | 'A'_1        | 59000141           | 4141          |
        +----+--------------+--------------------+---------------+
        | 3  | "A"_1        | 79000161           | 6161          |
        +----+--------------+--------------------+---------------+
        | 4  | [_1 "bar"]   | 99000163626172     | 8163626172    |
        +----+--------------+--------------------+---------------+
        | 5  | {_1 "bar":   | b900016362617201   | a16362617201  |
        |    | 1}           |                    |               |
        +----+--------------+--------------------+---------------+
        | 6  | 1_1(4711)    | d90001191267       | c1191267      |
        +----+--------------+--------------------+---------------+
        | 7  | 1.5_2        | fa3fc00000         | f93e00        |
        |    | 0x4711p+03_3 | fb4101c44000000000 | fa480e2200    |
        +----+--------------+--------------------+---------------+
```

## §4.2  Encoding Indicators of Arrays and Maps

- (§4.2) [`R-0143`] “A single underscore can be written after the opening brace of a map or the opening bracket of an array to indicate that the data item was represented in indefinite-length format.”
- (§4.2) [`R-0144`] “At the same position, encoding indicators for specifying the size of the array or map head for definite-length format can be used instead, specifically _i or _0 to _3.”

## §4.3  Deprecated: Indefinite-length Encoding Indicators for Strings

- (§4.3) [`R-0145`] “This syntax represents the individual chunks in sequence within parentheses, each optionally followed by a comma, with an encoding indicator _ immediately after the opening parenthesis:”
- (§4.3) [`R-0146`] “The overall type (byte string or text string) of the string is provided by the types of the individual chunks, which all need to be of the same type (Section 3.2.3 of RFC 8949 [STD94]).”
- (§4.3) [`R-0147`] “In this syntax, an indefinite-length string with no chunks inside, (_ ) would be ambiguous as to whether a byte string (encoded 5f ff) or a text string (encoded 7f ff) is meant and is therefore not used.”
- (§4.3) [`R-0148`] “With this document, the streamstring syntax is now deprecated; new CDN documents should instead use the ilbs/ilts app-extensions (Section 3.6) to build indefinite-length encoded strings.”

## §5  Tag-based Representations of CDN Input in Binary CBOR

- (§5) [`R-0149`] “In some cases, a CDN consumer cannot construct actual CBOR items that represent the CBOR data intended for eventual interchange. This document defines a CBOR tags-based representation for two such cases:”
- (§5) [`R-0150`] “Implementation note: Typically, the ultimate applications will fail if they encounter tags unknown to them, which the ones defined in this section likely are.”

## §5.1  Handling unknown app-extension identifiers

- (§5.1) [`R-0151`] “During ingestion of CDN, prefixed literals are usually decoded and transformed into the corresponding data item. If an app-extension is not known or not implemented by the ingesting process, this is usually an error and processing has to stop.”
- (§5.1) [`R-0152`] “This specification defines a CBOR Tag for this purpose: The Diagnostic Notation Unresolved App-Extension Tag, tag number CPA999 (Section 7.5). The content of this tag is an array of a text string for the app-extension prefix, and another array:”
- (§5.1) [`R-0153`] “For app-strings, the second array contains a single item, a text string containing the text notated by the single-quoted string in the app-string.”
- (§5.1) [`R-0154`] “For app-sequences, the second array contains zero or more items, which represent each item in the sequence contained in the app- sequence.”
- (§5.1) [`R-0155`] “Extension Tag, this is an error and processing has to stop,”

## §5.2  Handling information deliberately elided from a CDN document

- (§5.2) [`R-0156`] “To facilitate this, this specification supports the use of an _ellipsis_ (notated as three or more dots in a row, as in ...) to indicate parts of a CDN document that have been elided (and therefore cannot be reconstructed).”
- (§5.2) [`R-0157`] “Upon ingesting CDN as a representation of a CBOR data item for further processing, the occurrence of an ellipsis usually is an error and processing has to stop.”
- (§5.2) [`R-0158`] “The Diagnostic Notation Ellipsis Tag, tag number CPA888 (Section 7.5). The content of this tag is one of:”
- (§5.2) [`R-0159`] “null (indicating a data item entirely replaced by an ellipsis);”
- (§5.2) [`R-0160`] “an array, the elements of which are alternating between parts of a string and the actual elisions, represented as ellipses carrying a null as content.”
- (§5.2) [`R-0161`] “A single ellipsis (or key/value pair of ellipses) can imply eliding multiple elements in an array (members in a map). If more detailed control is required, a data definition language such as CDDL can be employed.”
- (§5.2) [`R-0162`] “(Note that the tag-based representation form defined here does not allow multiple key/value pairs with an ellipsis as a key: the CBOR data item would not be valid.)”
- (§5.2) [`R-0163`] “String elisions can be represented in a CBOR data item by a tag CPA888 that wraps an array containing string parts alternating with ellipsis indicators:”
- (§5.2) [`R-0164`] “The consumer of this CDN will ignore the comments and therefore will have no idea after ingestion that some information has been elided; validation steps may then simply fail instead of being informed about the elisions.”
- (§5.2) [`R-0223`] “The example "signature" uses special syntax that allows the use of ellipses between the bytes notated _inside_ h'' literals.”

## §6  ABNF Definitions

- (§6) [`R-0165`] “This section collects grammars in ABNF form ([STD68] as extended in [RFC7405]) that serve to define the syntax of CDN and some prefixed literals.”
- (§6) [`R-0166`] “Implementation note: The ABNF definitions in this section are intended to be useful in a Parsing Expression Grammar (PEG) parser interpretation (see Appendix A of [RFC8610] for an introduction into PEG).”

## §6.1  Overall ABNF Definition for Concise Diagnostic Notation

- (§6.1) [`R-0167`] “This ABNF definition treats all single-quoted string literals the same, whether they are unprefixed and constitute byte string literals, or prefixed and their content subject to further processing.”
- (§6.1) [`R-0168`] “as a convention, the grammar for the content of an app-string with prefix, say, p, is described by an ABNF definition with the rule name app-string-p.”
- (§6.1) [`R-0169`] “While an ABNF grammar defines the set of character strings that are considered to be valid CDN by this ABNF, the mapping of these character strings into the generic data model of CBOR is not always obvious.”
- (§6.1) [`R-0170`] “As mentioned in the terminology (Section 1.2), the ABNF terminal values in this document define Unicode scalar values (characters) rather than their UTF-8 encoding.”
- (§6.1) [`R-0171`] “decnumber stands for an integer in the usual decimal notation, unless at least one of the optional parts starting with "." and "e" are present, in which case it stands for a floating point value in the usual decimal notation. Note that the grammar allows 3. for 3.0 and .3 for 0.3 (also for hexadecimal floating point below); implementers are advised that some platform numeric parsers accept only a subset of the floating point syntax in this document and may require some preprocessing to use here.”
- (§6.1) [`R-0172`] “hexint, octint, and binint stand for an integer in the usual base 16/hexadecimal ("0x"), base 8/octal ("0o"), or base 2/binary ("0b") notation.”
- (§6.1) [`R-0173`] “For hexint, octint, binint, and when decnumber stands for an integer, the corresponding CBOR data item is represented using major type 0 or 1 if possible, or using tag 2 or 3 if not. In the latter case, this specification does not define any encoding indicators that apply.”
- (§6.1) [`R-0174`] “When decnumber stands for a floating point value, and for hexfloat and nonfin, a floating point data item with major type 7 is used; diagnostic implementations employ Preferred Serialization unless the item was modified by an encoding indicator, which then needs to be _1, _2, or _3.”
- (§6.1) [`R-0175`] “For this, the number range needs to fit into an [IEEE754] binary64 (or the size corresponding to the encoding indicator), and the precision will be adjusted to binary64 before further applying Preferred Serialization (or to the size corresponding to the encoding indicator). Tag 4/5 representations are not generated in these cases.”
- (§6.1) [`R-0176`] “The ABNF grammar for raw strings is lenient; a parser needs to implement the ABNF comments on alikerawdelim and shortrawdelim as well. shortrawdelim only matches sequences of backquotes that are shorter than startrawdelim. alikerawdelim only matches sequences of backquotes that are exactly as long as startrawdelim.”

**Figure 1: Overall ABNF Definition of CDN — 85 productions**
_Reproduced in 4 parts, split where the draft's page frame interrupts it._


_The `hexscalar-s` rule is CUT BY THE PAGE 45/46 FRAME: it begins in part 3 and its last two alternatives are the first two lines of part 4. See `schema/grammar-gaps.derived.txt` G-24._

<!-- source lines 2357-2404 (48 lines), sha256 a920bf06763b5dd90db733b5b968207677ac0c64bb432320a3e102fc7a90e1b4 -->
```
   seq             = S [item *(MSC item) SOC]
   one-item        = S item S
   item            = map / array / tagged
                   / number / simple
                   / string / streamstring

   string1         = (tstr / bstr) spec
   string          = string1 / ellipsis
   ellipsis        = 3*"." ; "..." or more dots

   number          = (hexfloat / hexint / octint / binint
                      / decnumber / nonfin) spec
   sign            = "+" / "-"
   decnumber       = [sign] (1*DIGIT ["." *DIGIT] / "." 1*DIGIT)
                            ["e" [sign] 1*DIGIT]
   hexfloat        = [sign] "0x" (1*HEXDIG ["." *HEXDIG] / "." 1*HEXDIG)
                            "p" [sign] 1*DIGIT
   hexint          = [sign] "0x" 1*HEXDIG
   octint          = [sign] "0o" 1*ODIGIT
   binint          = [sign] "0b" 1*BDIGIT
   nonfin          = %s"Infinity"
                   / %s"-Infinity"
                   / %s"NaN"
   simple          = %s"false"
                   / %s"true"
                   / %s"null"
                   / %s"undefined"
                   / %s"simple(" S simple-number S ")"
   simple-number   = "25" %x30-35         ; 250-255
                   / "2" %x30-34 DIGIT    ; 200-249
                   / "1" 2DIGIT           ; 100-199
                   / %x34-39 DIGIT        ; 40-99
                   / "3" %x32-39          ; 32-39
                   ;; there are no simple values between 24-31
                   / "2" %x30-33          ; 20-23
                   / "1" DIGIT            ; 10-19
                   / DIGIT                ; 0-9
   uint            = "0" / DIGIT1 *DIGIT
   tagged          = uint spec "(" S item S ")"

   app-prefix      = lcalpha *lcldh ; including h and b64
                   / ucalpha *ucldh ; tagged variant, if defined
   app-string      = app-prefix sqstr
   app-sequence    = app-prefix "<<" seq ">>"
   app-rstring     = app-prefix rawstring
   rawstring       = startrawdelim
                     raw-inner
                     alikerawdelim
```

<!-- source lines 2413-2459 (47 lines), sha256 b9cd3b2219ff2be9250bbfcd00908cbc5a8bdd12efb1c4524330ef1fed7e95b6 -->
```
   rawdelim        = 1*"`"
   startrawdelim   = rawdelim
                     ; width (number of backquotes) distinguishes
                     ; between following alikerawdelim and shortrawdelim
   alikerawdelim   = rawdelim ; width == previous startrawdelim
   shortrawdelim   = rawdelim ; width < previous startrawdelim
   rawchars        = 1*(%x0a/%x0d / %x20-5f / %x61-7e / NONASCII)
   raw-inner       = 1*(rawchars / shortrawdelim)

   sqstr           = SQUOTE *single-quoted SQUOTE
   bstr            = app-string / sqstr / app-rstring / rawstring
                   / app-sequence / embedded
                     ; note: rawstring is text; app-... can be any type
   tstr            = DQUOTE *double-quoted DQUOTE
   embedded        = "<<" seq ">>"

   array           = "[" (specms S item *(MSC item) SOC / spec S) "]"
   map             = "{" (specms S keyp *(MSC keyp) SOC / spec S) "}"
   keyp            = item S ":" S item

   ; We allow %x09 HT in prose, but not in string literals
   blank           = %x09 / %x0A / %x0D / %x20
   lblank          = %x0A / %x20  ; Not HT or CR (gone)
   non-slash       = blank / %x21-2e / %x30-7F / NONASCII
   non-slash-star  = blank / %x21-29 / %x2b-2e / %x30-7F / NONASCII
   non-star        = blank / %x21-29 / %x2b-7F / NONASCII
   ends-in-star    = *non-star 1*"*"
   non-lf          = %x09 / %x0D / %x20-7F / NONASCII
   eol-comment     = "#" / "//"
   comment         = "/" non-slash-star *non-slash "/"
                   / "/*" ends-in-star
                          *(non-slash-star ends-in-star) "/"
                   / eol-comment *non-lf %x0A
   ; optional space
   S               = *blank *(comment *blank)
   ; mandatory space
   MS              = (blank/comment) S
   ; mandatory comma and/or space
   MSC             = ("," S) / (MS ["," S])
   ; optional comma and/or space
   SOC             = S ["," S]

   ; check semantically that strings are either all text or all bytes
   ; note that there must be at least one string to distinguish
   streamstring    = "(_" MS string *(MSC string) SOC ")"
   spec            = ["_" *wordchar]
   specms          = ["_" *wordchar MS]
```

<!-- source lines 2469-2516 (48 lines), sha256 afa7e28a9ab40fe425bc0285bbc3fc01a3e4faf3ed3da2e936dea2dfc1213cbd -->
```
   double-quoted   = unescaped
                   / SQUOTE
                   / "\" escapable-d

   single-quoted   = unescaped
                   / DQUOTE
                   / "\" escapable-s

   escapable1      = %s"b" ; BS backspace U+0008
                   / %s"f" ; FF form feed U+000C
                   / %s"n" ; LF line feed U+000A
                   / %s"r" ; CR carriage return U+000D
                   / %s"t" ; HT horizontal tab U+0009
                   / "\"   ; \ backslash (reverse solidus) U+005C

   escapable-d     = escapable1
                   / DQUOTE
                   / "/"   ; / slash (solidus) U+002F (JSON!)
                   / (%s"u" hexchar) ;  uXXXX      U+XXXX

   escapable-s     = escapable1
                   / SQUOTE
                   / (%s"u" hexchar-s) ;  uXXXX      U+XXXX

   hexchar         = "{" (1*"0" [ hexscalar ] / hexscalar) "}"
                   / non-surrogate
                   / two-surrogate
   non-surrogate   = ((DIGIT / "A"/"B"/"C" / "E"/"F") 3HEXDIG)
                   / ("D" ODIGIT 2HEXDIG )
   two-surrogate   = high-surrogate "\" %s"u" low-surrogate
   high-surrogate  = "D" ("8"/"9"/"A"/"B") 2HEXDIG
   low-surrogate   = "D" ("C"/"D"/"E"/"F") 2HEXDIG
   hexscalar       = "10" 4HEXDIG / HEXDIG1 4HEXDIG
                   / non-surrogate / 1*3HEXDIG

   ; single-quote hexchar-s: don't allow 0020..007e
   hexchar-s       = "{" (1*"0" [ hexscalar-s ] / hexscalar-s) "}"
                   / non-surrogate-s
                   / two-surrogate
   non-surrogate-s = "007F"                 ; rubout
                   / "00" ("0"/"1"/"8"/"9"/HEXDIGA) HEXDIG
                   / "0" HEXDIG1 2HEXDIG
                   / non-surrogate-1
   non-surrogate-1 = ((DIGIT1 / "A"/"B"/"C" / "E"/"F") 3HEXDIG)
                   / ("D" ODIGIT 2HEXDIG )
   hexscalar-s     = "10" 4HEXDIG / HEXDIG1 4HEXDIG
                   / non-surrogate-1 / HEXDIG1 2HEXDIG
                   / ("1"/"8"/"9"/HEXDIGA) HEXDIG
```

<!-- source lines 2525-2557 (33 lines), sha256 2dcf800a93f54dbcaf176ce6ea5107c9eae781dad1e85d0543c0b7c5ee54336e -->
```
                   / "7F"
                   / HEXDIG1

   ; Note that no other C0 characters are allowed, including %x09 HT
   unescaped       = %x0A ; new line
                   / %x0D ; carriage return -- ignored on input
                   / %x20-21
                        ; omit 0x22 "
                   / %x23-26
                        ; omit 0x27 '
                   / %x28-5B
                        ; omit 0x5C \
                   / %x5D-7F
                   / NONASCII

   newline         = [%x0D] %x0A
   DQUOTE          = %x22    ; " double quote
   SQUOTE          = "'"     ; ' single quote
   DIGIT           = %x30-39 ; 0-9
   DIGIT1          = %x31-39 ; 1-9
   ODIGIT          = %x30-37 ; 0-7
   BDIGIT          = %x30-31 ; 0-1
   HEXDIGA         = "A" / "B" / "C" / "D" / "E" / "F"
   ; Note: double-quoted strings as in "A" are case-insensitive in ABNF
   HEXDIG          = DIGIT / HEXDIGA
   HEXDIG1         = DIGIT1 / HEXDIGA
   lcalpha         = %x61-7A ; a-z
   lcldh           = lcalpha / DIGIT / "-"
   ucalpha         = %x41-5A ; A-Z
   ucldh           = ucalpha / DIGIT / "-"
   ALPHA           = lcalpha / ucalpha
   wordchar        = "_" / ALPHA / DIGIT ; [_a-z0-9A-Z]
   NONASCII        = %x80-D7FF / %xE000-10FFFF
```

**Section 6.1, numbered interpretation items 1-7, and the PEG predicate note**
_Reproduced in 2 parts, split where the draft's page frame interrupts it._


<!-- source lines 2581-2628 (48 lines), sha256 73f7fff7ffa67ce5bf27523b36a4b830a4b181f1a60d98fd7ebe995749d4f25f -->
```
   1.  As mentioned in the terminology (Section 1.2), the ABNF terminal
       values in this document define Unicode scalar values (characters)
       rather than their UTF-8 encoding.  For example, the Unicode PLACE
       OF INTEREST SIGN (U+2318) would be defined in ABNF as %x2318.

   2.  See Section 1.3.5 for more considerations about the character
       repertoire used for CDN source text and, in particular, the
       special handling of newline characters in the source.

   3.  decnumber stands for an integer in the usual decimal notation,
       unless at least one of the optional parts starting with "." and
       "e" are present, in which case it stands for a floating point
       value in the usual decimal notation.  Note that the grammar
       allows 3. for 3.0 and .3 for 0.3 (also for hexadecimal floating
       point below); implementers are advised that some platform numeric
       parsers accept only a subset of the floating point syntax in this
       document and may require some preprocessing to use here.

   4.  hexint, octint, and binint stand for an integer in the usual base
       16/hexadecimal ("0x"), base 8/octal ("0o"), or base 2/binary
       ("0b") notation.  hexfloat stands for a floating point number in
       the usual hexadecimal notation (which uses a mantissa in
       hexadecimal and an exponent in decimal notation, see
       Section 5.12.3 of [IEEE754], Section 6.4.4.3 of [C], or
       Section 5.13.4 of [Cplusplus]; floating-suffix/floating-point-
       suffix from the latter two is not used here).

   5.  For hexint, octint, binint, and when decnumber stands for an
       integer, the corresponding CBOR data item is represented using
       major type 0 or 1 if possible, or using tag 2 or 3 if not.  In
       the latter case, this specification does not define any encoding
       indicators that apply.  If fine control over encoding is desired,
       this can be expressed by being explicit about the representation
       as a tag: E.g., 987654321098765432310, which is equivalent to
       2(h'35 8a 75 04 38 f3 80 f5 f6') in its Preferred Serialization,
       might be written as 2_3(h'00 00 00 35 8a 75 04 38 f3 80 f5 f6'_1)
       if leading zeros need to be added during serialization to obtain
       specific sizes for tag head, byte string head, and the overall
       byte string.

       When decnumber stands for a floating point value, and for
       hexfloat and nonfin, a floating point data item with major type 7
       is used; diagnostic implementations employ Preferred
       Serialization unless the item was modified by an encoding
       indicator, which then needs to be _1, _2, or _3.  For this, the
       number range needs to fit into an [IEEE754] binary64 (or the size
       corresponding to the encoding indicator), and the precision will
       be adjusted to binary64 before further applying Preferred
```

<!-- source lines 2637-2658 (22 lines), sha256 17d0b22d4a6b8ee2c92a28d70fb90ecfc813a7b2dae31ef3cfec1833f7b4052f -->
```
       Serialization (or to the size corresponding to the encoding
       indicator).  Tag 4/5 representations are not generated in these
       cases.  Future app-prefixes could be defined to allow more
       control for obtaining a tag 4/5 representation directly from a
       hex or decimal floating point literal.

   6.  spec stands for an encoding indicator.  See Section 4 for
       details.

   7.  The ABNF grammar for raw strings is lenient; a parser needs to
       implement the ABNF comments on alikerawdelim and shortrawdelim as
       well.  shortrawdelim only matches sequences of backquotes that
       are shorter than startrawdelim.  alikerawdelim only matches
       sequences of backquotes that are exactly as long as
       startrawdelim.

     |  In a PEG parser that implements predicates, these matching
     |  rules can for instance be implemented as follows:
     |  
     |   startrawdelim = rawdelim&{|(rd)|@rdlen = rd.text_value.length}
     |   shortrawdelim = rawdelim&{|(rd)|rd.text_value.length < @rdlen}
     |   alikerawdelim = rawdelim&{|(rd)|rd.text_value.length == @rdlen}
```

## §6.2  ABNF Definitions for App-Extension Content

- (§6.2) [`R-0177`] “These grammars describe the _decoded_ content of the single-quoted or raw string components that combine with prefixes to form prefixed literals.”
- (§6.2) [`R-0178`] “Each of these may integrate ABNF rules defined in Figure 1, which are not always repeated here.”
- (§6.2) [`R-0179`] “For convenience, the common definitions in Figure 2 are not repeated in the below ABNF grammars.”
- (§6.2) [`R-0180`] “Note that implementation platforms may already provide implementations of grammars used in app-extensions, such as of RFC 3339 for dt'' and of IP address syntax for ip''. CDN-based tools may want to use these implementation libraries instead of using the grammars that are provided here as a reference.”

**Table 7: App-prefix Values Defined in this Document**
_Reproduced in 2 parts, split where the draft's page frame interrupts it._


_This is the definitive list of prefixes this draft defines. `b32` and `h32` are not in it._

<!-- source lines 2671-2684 (14 lines), sha256 54fbbbe722c7d2b0e024b70f222145ccfb0ab6703d56e4d2589e9dceb6e544f4 -->
```
       +============+===========================+=================+
       | app-prefix | content of single-quoted  | result type     |
       |            | or raw string             |                 |
       +============+===========================+=================+
       | h          | hexadecimal form of       | byte string     |
       |            | binary data               |                 |
       +------------+---------------------------+-----------------+
       | H          | (not used)                |                 |
       +------------+---------------------------+-----------------+
       | b64        | base64 forms (classic or  | byte string     |
       |            | base64url) of binary data |                 |
       +------------+---------------------------+-----------------+
       | B64        | (not used)                |                 |
       +------------+---------------------------+-----------------+
```

<!-- source lines 2693-2733 (41 lines), sha256 7fb307cf3c1a2bfd75a2a14cfc384a925f22eb60a03171fcd2ff6b3a0e290a6f -->
```
       | dt         | RFC 3339 date/time        | number (int or  |
       |            |                           | float)          |
       +------------+---------------------------+-----------------+
       | DT         | "                         | Tag 1 on the    |
       |            |                           | above           |
       +------------+---------------------------+-----------------+
       | ip         | IP address or prefix      | byte string,    |
       |            |                           | array of length |
       |            |                           | and byte string |
       +------------+---------------------------+-----------------+
       | IP         | "                         | Tag 54 (IPv6)   |
       |            |                           | or 52 (IPv4) on |
       |            |                           | the above       |
       +------------+---------------------------+-----------------+
       | hash       | string (usually used with | byte string     |
       |            | sequences)                |                 |
       +------------+---------------------------+-----------------+
       | HASH       | (not used)                |                 |
       +------------+---------------------------+-----------------+
       | t1         | strings (usually used     | text string     |
       |            | with sequences)           |                 |
       +------------+---------------------------+-----------------+
       | T1         | (not used)                |                 |
       +------------+---------------------------+-----------------+
       | b1         | strings (usually used     | byte string     |
       |            | with sequences)           |                 |
       +------------+---------------------------+-----------------+
       | B1         | (not used)                |                 |
       +------------+---------------------------+-----------------+
       | cri        | RFC 3986 URI or URI       | CBOR structure  |
       |            | reference                 | representing    |
       |            |                           | equivalent CRI  |
       +------------+---------------------------+-----------------+
       | CRI        | "                         | Tag 99 on the   |
       |            |                           | above           |
       +------------+---------------------------+-----------------+
       | float      | floating point value from | floating point  |
       |            | input bytes               | value (mt=7)    |
       +------------+---------------------------+-----------------+
       | FLOAT      | (not used)                |                 |
       +------------+---------------------------+-----------------+
```

**Figure 2: Common Rules Used in app-extension ABNF grammars**

<!-- source lines 2758-2765 (8 lines), sha256 934dba471d87b2893d5c5bc39ad648d880e1e70c7dbb9a1f4540c09ff3b1bb5f -->
```
   ALPHA           = %x41-5a / %x61-7a
   DIGIT           = %x30-39 ; 0-9
   HEXDIG          = DIGIT / HEXDIGA
   HEXDIGA         = "A" / "B" / "C" / "D" / "E" / "F"
   ; Note: double-quoted strings as in "A" are case-insensitive in ABNF
   lblank          = %x0A / %x20  ; Not HT or CR (gone)
   non-lf          = %x20-7f / NONASCII
   NONASCII        = %x80-D7FF / %xE000-10FFFF
```

## §6.2.1  h: ABNF Definition of Hexadecimal representation of a byte string

- (§6.2.1) [`R-0181`] “This syntax accommodates both lowercase and uppercase hex digits, as well as blank space (including comments) around each hex digit.”

**Figure 3: ABNF Definition of Hexadecimal Representation of a Byte String**

<!-- source lines 2778-2791 (14 lines), sha256 03c690a21665b2b8a43582c05d6315af52ee52ae85869db192eaf5c761f5a177 -->
```
   app-string-h    = S *(HEXDIG S HEXDIG S / ellipsis S)
                     [eol-comment *non-lf]
   ellipsis        = 3*"."
   non-slash       = lblank / %x21-2e / %x30-7f / NONASCII
   non-slash-star  = lblank / %x21-29 / %x2b-2e / %x30-7f / NONASCII
   non-star        = lblank / %x21-29 / %x2b-7f / NONASCII
   ends-in-star    = *non-star 1*"*"
   non-lf          = %x20-7f / NONASCII
   eol-comment     = "#" / "//"
   S               = *lblank *(comment *lblank)
   comment         = "/" non-slash-star *non-slash "/"
                   / "/*" ends-in-star
                          *(non-slash-star ends-in-star) "/"
                   / eol-comment *non-lf %x0A
```

## §6.2.2  b64: ABNF Definition of Base64 representation of a byte string

- (§6.2.2) [`R-0182`] “This syntax allows both the classic (Section 4 of [RFC4648]) and the URL-safe (Section 5 of [RFC4648]) alphabet to be used. It accommodates, but does not require base64 padding.”
- (§6.2.2) [`R-0183`] “Note that inclusion of classic base64 makes it impossible to have comments based on slash characters in b64, as "/" is valid base64-classic.”

**Figure 4: ABNF definition of Base64 Representation of a Byte String**

<!-- source lines 2830-2835 (6 lines), sha256 5321d8c80d08b7e87dee695bdaf9082a49b4f62ad551a1a555aad11379c3a2dd -->
```
   app-string-b64  = B *(4(b64dig B))
                     [b64dig B b64dig B ["=" B "=" / b64dig B ["="]] B]
                     ["#" *non-lf]
   b64dig          = ALPHA / DIGIT / "-" / "_" / "+" / "/"
   B               = *lblank *(comment *lblank)
   comment         = "#" *non-lf %x0A
```

## §6.2.3  dt: ABNF Definition of RFC 3339 Representation of a Date/Time

- (§6.2.3) [`R-0184`] “The syntax of the content of dt literals can be described by the ABNF for date-time in Figure 5. This is derived from [RFC3339] as summarized in Section 3 of [RFC9165].”

**Figure 5: ABNF Definition of RFC3339 Representation of a Date/Time**

<!-- source lines 2861-2880 (20 lines), sha256 7127d6d69425ed8dcf23874c33f4d0d79a2d69876cdc7b98e9167196eee2a2e3 -->
```
   app-string-dt   = date-time

   date-fullyear   = 4DIGIT
   date-month      = 2DIGIT  ; 01-12
   date-mday       = 2DIGIT  ; 01-28, 01-29, 01-30, 01-31 based on
                             ; month/year
   time-hour       = 2DIGIT  ; 00-23
   time-minute     = 2DIGIT  ; 00-59
   time-second     = 2DIGIT  ; 00-58, 00-59, 00-60 based on leap sec
                             ; rules
   time-secfrac    = "." 1*DIGIT
   time-numoffset  = ("+" / "-") time-hour ":" time-minute
   time-offset     = "Z" / time-numoffset

   partial-time    = time-hour ":" time-minute ":" time-second
                     [time-secfrac]
   full-date       = date-fullyear "-" date-month "-" date-mday
   full-time       = partial-time time-offset

   date-time       = full-date "T" full-time
```

## §6.2.4  ip: ABNF Definition of Textual Representation of an IP Address

- (§6.2.4) [`R-0185`] “The syntax of the content of ip literals can be described by the ABNF for IPv4address and IPv6address in Section 3.2.2 of [RFC3986], as included in slightly updated form in Figure 6.”

**Figure 6: ABNF Definition of Textual Representation of an IP Address**

<!-- source lines 2917-2944 (28 lines), sha256 c0aa4534ad25cdec0356f7ca2680705359674670f989209eccc17d913a88cc60 -->
```
   app-string-ip = IPaddress ["/" uint]

   IPaddress     = IPv4address
                 / IPv6address

   ; ABNF from RFC 3986, re-arranged for PEG compatibility:

   IPv6address   =                            6( h16 ":" ) ls32
                 /                       "::" 5( h16 ":" ) ls32
                 / [ h16               ] "::" 4( h16 ":" ) ls32
                 / [ h16 *1( ":" h16 ) ] "::" 3( h16 ":" ) ls32
                 / [ h16 *2( ":" h16 ) ] "::" 2( h16 ":" ) ls32
                 / [ h16 *3( ":" h16 ) ] "::"    h16 ":"   ls32
                 / [ h16 *4( ":" h16 ) ] "::"              ls32
                 / [ h16 *5( ":" h16 ) ] "::"              h16
                 / [ h16 *6( ":" h16 ) ] "::"

   h16           = 1*4HEXDIG
   ls32          = ( h16 ":" h16 ) / IPv4address
   IPv4address   = dec-octet "." dec-octet "." dec-octet "." dec-octet
   dec-octet     = "25" %x30-35         ; 250-255
                 / "2" %x30-34 DIGIT    ; 200-249
                 / "1" 2DIGIT           ; 100-199
                 / %x31-39 DIGIT        ; 10-99
                 / DIGIT                ; 0-9

   DIGIT1        = %x31-39 ; 1-9
   uint          = "0" / DIGIT1 *DIGIT
```

## §6.2.5  cri: ABNF Definition of URI Representation of a CRI

- (§6.2.5) [`R-0186`] “In case such a URI parser is not available or inconvenient to integrate, a grammar of the content of cri literals is provided by the ABNF for URI-reference in Section 4.1 of RFC 3986 [RFC3986] with certain re-arrangements taken from Section 6.2.4; these are reproduced in Figure 7. If the content is not ASCII only (i.e., for IRIs), first apply Section 3.1 of [RFC3987] and apply this grammar to the result.”

**Figure 7: ABNF Definition of URI Representation of a CRI**
_Reproduced in 2 parts, split where the draft's page frame interrupts it._


<!-- source lines 2973-3020 (48 lines), sha256 a48a58d6370e1bafc0530c7808240db6f41f54544b8c70757afc8607f6651e0c -->
```
   app-string-cri = URI-reference
   ; ABNF from RFC 3986:

   URI           = scheme ":" hier-part [ "?" query ] [ "#" fragment ]

   hier-part     = "//" authority path-abempty
                    / path-absolute
                    / path-rootless
                    / path-empty

   URI-reference = URI / relative-ref

   absolute-URI  = scheme ":" hier-part [ "?" query ]

   relative-ref  = relative-part [ "?" query ] [ "#" fragment ]

   relative-part = "//" authority path-abempty
                    / path-absolute
                    / path-noscheme
                    / path-empty

   scheme        = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )

   authority     = [ userinfo "@" ] host [ ":" port ]
   userinfo      = *( unreserved / pct-encoded / sub-delims / ":" )
   host          = IP-literal / IPv4address / reg-name
   port          = *DIGIT

   IP-literal    = "[" ( IPv6address / IPvFuture  ) "]"

   IPvFuture     = "v" 1*HEXDIG "." 1*( unreserved / sub-delims / ":" )

   ; Use IPv6address, h16, ls32, IPv4adress, dec-octet as re-arranged
   ; for PEG Compatibility in Figure 6 of [RFC XXXX]:

   IPv6address   =                            6( h16 ":" ) ls32
                 /                       "::" 5( h16 ":" ) ls32
                 / [ h16               ] "::" 4( h16 ":" ) ls32
                 / [ h16 *1( ":" h16 ) ] "::" 3( h16 ":" ) ls32
                 / [ h16 *2( ":" h16 ) ] "::" 2( h16 ":" ) ls32
                 / [ h16 *3( ":" h16 ) ] "::"    h16 ":"   ls32
                 / [ h16 *4( ":" h16 ) ] "::"              ls32
                 / [ h16 *5( ":" h16 ) ] "::"              h16
                 / [ h16 *6( ":" h16 ) ] "::"

   h16           = 1*4HEXDIG
   ls32          = ( h16 ":" h16 ) / IPv4address
   IPv4address   = dec-octet "." dec-octet "." dec-octet "." dec-octet
```

<!-- source lines 3029-3066 (38 lines), sha256 ce38929f5f0d44a50b024953364853b831b9a1f9a67350b14ac18032332feb43 -->
```
   dec-octet     = "25" %x30-35         ; 250-255
                 / "2" %x30-34 DIGIT    ; 200-249
                 / "1" 2DIGIT           ; 100-199
                 / %x31-39 DIGIT        ; 10-99
                 / DIGIT                ; 0-9

   reg-name      = *( unreserved / pct-encoded / sub-delims )

   path          = path-abempty    ; begins with "/" or is empty
                    / path-absolute   ; begins with "/" but not "//"
                    / path-noscheme   ; begins with a non-colon segment
                    / path-rootless   ; begins with a segment
                    / path-empty      ; zero characters

   path-abempty  = *( "/" segment )
   path-absolute = "/" [ segment-nz *( "/" segment ) ]
   path-noscheme = segment-nz-nc *( "/" segment )
   path-rootless = segment-nz *( "/" segment )
   path-empty    = 0<pchar>

   segment       = *pchar
   segment-nz    = 1*pchar
   segment-nz-nc = 1*( unreserved / pct-encoded / sub-delims / "@" )
                    ; non-zero-length segment without any colon ":"

   pchar         = unreserved / pct-encoded / sub-delims / ":" / "@"

   query         = *( pchar / "/" / "?" )

   fragment      = *( pchar / "/" / "?" )

   pct-encoded   = "%" HEXDIG HEXDIG

   unreserved    = ALPHA / DIGIT / "-" / "." / "_" / "~"
   reserved      = gen-delims / sub-delims
   gen-delims    = ":" / "/" / "?" / "#" / "[" / "]" / "@"
   sub-delims    = "!" / "$" / "&" / "'" / "(" / ")"
                    / "*" / "+" / "," / ";" / "="
```

## §6.3  ABNF Definitions for Integrated Extension Parsers

- (§6.3) [`R-0187`] “For some applications of CDN, it is an optimization to integrate parsers for the content of some prefixed string literals into the main parser, handling both the string literal syntax (e.g., escapes such as \' and \\) and the syntax of the extension content in one go.”
- (§6.3) [`R-0188`] “For app-extensions that only use printable ASCII characters (from U+0020 to U+007E) minus single-quote ' and backslash \, the ABNF such as that given in Section 6.2 can be directly used as an integrated parser, after adding some glue ABNF.”
- (§6.3) [`R-0189`] “There is no expectation for a new app-extension to supply ABNF for an integrated parser (or any ABNF at all!), in particular if the parsing function is likely to be fulfilled by a platform library.”

**Figure 8: Glue ABNF for Integrated DT Parser**

_This redefinition DROPS `app-rstring` and `rawstring` from `bstr`; compare Figure 1 above. See `schema/grammar-gaps.derived.txt` G-16._

<!-- source lines 3092-3094 (3 lines), sha256 5f748439b06082b0cc51ba55d815cd78e52adb8c9ad4df52536f93a4c66db041 -->
```
   bstr            = sq-app-string-dt /
                     app-string / sqstr / app-sequence / embedded
   sq-app-string-dt = (%s"dt'"/%s"DT'") app-string-dt "'"
```

**Figure 9: ABNF Definitions Useful for Integrated Extension Parsers**

<!-- source lines 3102-3125 (24 lines), sha256 4a9ae29b040ca25f4bd34c3180499abc4d0a2be10bb95c52fa30714592378848 -->
```
   i-HT =        %s"\t" / %s"\u" ("0009" / "{" *("0") "9}")
   i-LF = %x0a / %s"\n" / %s"\u" ("000A" / "{" *("0") "A}")
   i-CR = %x0d / %s"\r" / %s"\u" ("000D" / "{" *("0") "D}")

   i-blank = i-LF / i-CR / " "
   i-non-lf = i-HT / i-CR / %x20-26 / "\'" / %x28-5b
            / "\\" / %x5d-7f / i-NONASCII

   i-NONASCII = NONASCII / %s"\u" ESCGE7F

   ; hex escaping for U+007F or greater
   ESCGE7F = "D" ("8"/"9"/"A"/"B") 2HEXDIG
             %s"\u" "D" ("C"/"D"/"E"/"F") 2HEXDIG
           / FOURHEX1 / "0" HEXDIG1 2HEXDIG / "00" TWOHEX1
           / "{" *("0")
             ("10" 4HEXDIG / HEXDIG1 4HEXDIG
              / FOURHEX1 / HEXDIG1 2HEXDIG / TWOHEX1)
             "}"

   ; xxxx - 0xxx - Dhigh\uDloow
   FOURHEX1 = (DIGIT1 / "A"/"B"/"C" / "E"/"F") 3HEXDIG
            / "D" ODIGIT 2HEXDIG
   ; 00xx - ASCII + 007F
   TWOHEX1  = ("8"/"9" / HEXDIGA) HEXDIG / "7F"
```

**Figure 10: ABNF Definitions Useful for Raw String Integrated Extension Parsers**

<!-- source lines 3141-3141 (1 lines), sha256 a3104c7ba1346a610465bf6c5cd29e4ca2772c66fdd8fe9fc0760376ee0e75b1 -->
```
   r-non-lf = %x0D / %x20-5f / %x61-7f / NONASCII / shortrawdelim
```

## §6.3.1  h'': ABNF Definition of Integrated Parser

**Figure 11: ABNF Definition for Integrated Hex Parser**

<!-- source lines 3163-3178 (16 lines), sha256 8c5059bb9567fcdf1be547f85ff2654a1496d08530c8b185d933b087d057e983 -->
```
   sq-app-string-h = %s"h'" s-app-string-h "'"
   s-app-string-h = h-S *(HEXDIG h-S HEXDIG h-S / ellipsis h-S)
       [eol-comment *i-non-lf]

   h-S = *(i-blank) *(h-comment *(i-blank))
   h-non-slash = i-blank / %x21-26 / "\'" / %x28-2e
               / %x30-5b / "\\" / %x5d-7f / i-NONASCII
   h-non-slash-star = i-blank / %x21-26 / "\'" / %x28-29 / %x2b-2e
                    / %x30-5b / "\\" / %x5d-7f / i-NONASCII
   h-non-star = i-blank / %x21-26 / "\'" / %x28-29 / %x2b-5b
              / "\\" / %x5d-7f / i-NONASCII
   h-ends-in-star = *h-non-star 1*"*"
   h-comment = "/" h-non-slash-star *h-non-slash "/"
             / "/*" h-ends-in-star
                    *(h-non-slash-star h-ends-in-star) "/"
             / eol-comment *i-non-lf i-LF
```

## §6.3.2  b64'': ABNF Definition of Integrated Parser

**Figure 12: ABNF Definition for Integrated Base64 Parser**

<!-- source lines 3197-3204 (8 lines), sha256 3c54c384bd423e88e58a92e0aaad3b223de145148f0a989d6524a9bdd66f549d -->
```
   sq-app-string-b64 = %s"b64'" s-app-string-b64 "'"
   s-app-string-b64  = b64-S *(4(b64dig b64-S))
                     [b64dig b64-S b64dig b64-S
                      ["=" b64-S "=" / b64dig b64-S ["="]] b64-S]
                     ["#" *i-non-lf]
   b64dig          = ALPHA / DIGIT / "-" / "_" / "+" / "/"
   b64-S           = *i-blank *(b64-comment *i-blank)
   b64-comment     = "#" *i-non-lf %x0A
```

## §6.3.3  h``: ABNF Definition of Integrated Parser

**Figure 13: ABNF Definition for Integrated Raw String Hex Parser**

<!-- source lines 3214-3226 (13 lines), sha256 8bde7b256751b7487d350d782eb064f436bf4b754ff50428841e01f66043370a -->
```
   raw-app-string-h = %s"h" startrawdelim r-app-string-h
   r-app-string-h = rh-S *(HEXDIG rh-S HEXDIG rh-S / ellipsis rh-S)
       (eol-comment *r-non-lf alikerawdelim / alikerawdelim)
   rh-S = *(lblank) *(rh-comment *(lblank))
   rh-2 = %x61-7f / NONASCII / shortrawdelim
   rh-non-slash = lblank / %x21-2e / %x30-5f / rh-2
   rh-non-slash-star = lblank / %x21-29 / %x2b-2e / %x30-5f / rh-2
   rh-non-star = lblank / %x21-29 / %x2b-5f / rh-2
   rh-ends-in-star = *rh-non-star 1*"*"
   rh-comment = "/" rh-non-slash-star *rh-non-slash "/"
              / "/*" rh-ends-in-star
                     *(rh-non-slash-star rh-ends-in-star) "/"
              / eol-comment *r-non-lf %x0A
```

## §6.3.4  b64``: ABNF Definition of Integrated Parser

**Figure 14: ABNF Definition for Integrated Raw String Base64 Parser**

<!-- source lines 3237-3243 (7 lines), sha256 2c5d8a2ec6743a2f9c64637e3f1371e1f38d7545610acde65d0b0ad6f44361ab -->
```
   raw-app-string-b64 = %s"b64" startrawdelim r-app-string-b64
   r-app-string-b64  = rb64-S *(4(b64dig rb64-S))
                     [b64dig rb64-S b64dig rb64-S
                      ["=" rb64-S "=" / b64dig rb64-S ["="]] rb64-S]
                     ("#" *r-non-lf alikerawdelim / alikerawdelim)
   rb64-S           = *lblank *(rb64-comment *lblank)
   rb64-comment     = "#" *r-non-lf %x0A
```

## §7.1  Concise Diagnostic Notation App-extension Identifiers Registry

- (§7.1) [`R-0190`] “IANA is requested to create an "App-Extension Identifiers" registry in a new "Concise Diagnostic Notation" registry group [IANA.concise- diagnostic-notation], with the policy "expert review" (Section 4.5 of RFC 8126 [BCP26]).”
- (§7.1) [`R-0191`] “The experts are instructed to be frugal in the allocation of app- extension identifiers that are suggestive of generally applicable semantics, keeping them in reserve for app-extensions that are likely to enjoy wide use and can make good use of their conciseness.”
- (§7.1) [`R-0192`] “The experts are also instructed to direct the registrant to provide a specification (Section 4.6 of RFC 8126 [BCP26]), but can make exceptions, for instance when a specification is not available at the time of registration but is likely forthcoming.”
- (§7.1) [`R-0224`] “If the experts become aware of app-extension identifiers that are deployed and in use, they may also initiate a registration on their own if they deem such a registration can avert potential future collisions.”
- (§7.1) [`R-0193`] “Each entry in the registry must include:”
- (§7.1) [`R-0194`] “a lowercase ASCII [STD80] string that starts with a letter and can contain letters, digits, and hyphens after that ([a-z][a-z0-9-]*). No other entry in the registry can have the same app-extension identifier.”
- (§7.1) [`R-0195`] “The initial content of the registry is shown in Table 8; all initial entries have the Change Controller "IETF".”

**Required fields of an App-Extension Identifiers registry entry**

<!-- source lines 3283-3300 (18 lines), sha256 37e2174a5f0bd448f61f2d9a9d696617de113eb340b58734eadc6b6b9ea3032e -->
```
   App-Extension Identifier:
      a lowercase ASCII [STD80] string that starts with a letter and can
      contain letters, digits, and hyphens after that ([a-z][a-z0-9-]*).
      No other entry in the registry can have the same app-extension
      identifier.

   Description:
      a brief description

   Change Controller:
      (see Section 2.3 of RFC 8126 [BCP26])

   Reference:
      a reference document that provides a description of the app-
      extension identifier

   The initial content of the registry is shown in Table 8; all initial
   entries have the Change Controller "IETF".
```

**Table 8: Initial Content of app-extension Identifier Registry**

_`b32` and `h32` appear here, and only here, as Reserved against RFC8949. Reserved in the registry is not defined in the notation._

<!-- source lines 3309-3349 (41 lines), sha256 e77de6f2c1872a4f8f653596b2af97710a1223fc6b05ee692676e450cb33fc45 -->
```
      +===============+=====================+======================+
      | app-extension | Description         | Reference            |
      | identifier    |                     |                      |
      +===============+=====================+======================+
      | h             | Reserved            | RFC8949              |
      +---------------+---------------------+----------------------+
      | b32           | Reserved            | RFC8949              |
      +---------------+---------------------+----------------------+
      | h32           | Reserved            | RFC8949              |
      +---------------+---------------------+----------------------+
      | b64           | Reserved            | RFC8949              |
      +---------------+---------------------+----------------------+
      | false         | Reserved            | RFC-XXXX             |
      +---------------+---------------------+----------------------+
      | true          | Reserved            | RFC-XXXX             |
      +---------------+---------------------+----------------------+
      | null          | Reserved            | RFC-XXXX             |
      +---------------+---------------------+----------------------+
      | undefined     | Reserved            | RFC-XXXX             |
      +---------------+---------------------+----------------------+
      | pragma        | Reserved for future | RFC-XXXX             |
      |               | use                 |                      |
      +---------------+---------------------+----------------------+
      | dt            | Date/Time           | RFC-XXXX             |
      +---------------+---------------------+----------------------+
      | ip            | IP Address/Prefix   | RFC-XXXX             |
      +---------------+---------------------+----------------------+
      | hash          | Cryptographic Hash  | RFC-XXXX             |
      +---------------+---------------------+----------------------+
      | b1            | Byte String         | RFC-XXXX             |
      |               | Concatenation       |                      |
      +---------------+---------------------+----------------------+
      | t1            | Text String         | RFC-XXXX             |
      |               | Concatenation       |                      |
      +---------------+---------------------+----------------------+
      | cri           | Constrained         | RFC-XXXX,            |
      |               | Resource Identifier | [I-D.ietf-core-href] |
      +---------------+---------------------+----------------------+
      | float         | Floating-Point      | RFC-XXXX             |
      |               | Value               |                      |
      +---------------+---------------------+----------------------+
```

## §7.2  Encoding Indicators

- (§7.2) [`R-0196`] “IANA is requested to create an "Encoding Indicators" registry in the newly created "Concise Diagnostic Notation" registry group [IANA.concise-diagnostic-notation], with the policy "specification required" (Section 4.6 of RFC 8126 [BCP26]).”
- (§7.2) [`R-0225`] “The experts are instructed to be frugal in the allocation of encoding indicators that are suggestive of generally applicable semantics, keeping them in reserve for encoding indicator registrations that are likely to enjoy wide use and can make good use of their conciseness.”
- (§7.2) [`R-0226`] “If the experts become aware of encoding indicators that are deployed and in use, they may also solicit a specification and initiate a registration on their own if they deem such a registration can avert potential future collisions.”
- (§7.2) [`R-0197`] “an ASCII [STD80] string that starts with an underscore letter and can contain zero or more underscores, letters and digits after that (_[_A-Za-z0-9]*). No other entry in the registry can have the same Encoding Indicator.”
- (§7.2) [`R-0198`] “As the "Reference" column reflects, all the encoding indicators initially registered are already defined in Section 8.1 of RFC 8949 [STD94], with the exception of _i, which is defined in Section 6.1 of the present document.”

**Required fields of an Encoding Indicators registry entry**

<!-- source lines 3383-3403 (21 lines), sha256 2d384af089b9436e8d887b4bb27880773fd6e8bcd4dc1fafd333d333795fa551 -->
```
   Encoding Indicator:
      an ASCII [STD80] string that starts with an underscore letter and
      can contain zero or more underscores, letters and digits after
      that (_[_A-Za-z0-9]*).  No other entry in the registry can have
      the same Encoding Indicator.

   Description:
      a brief description.  This description may employ an abbreviation
      of the form ai=nn, where nn is the numeric value of the field
      _additional information_, the low-order 5 bits of the initial byte
      (see Section 3 of RFC 8949 [STD94]).

   Change Controller:
      (see Section 2.3 of RFC 8126 [BCP26])

   Reference:
      a reference document that provides a description of the app-
      extension identifier

   The initial content of the registry is shown in Table 9; all initial
   entries have the Change Controller "IETF".
```

**Table 9: Initial Content of Encoding Indicator Registry**

<!-- source lines 3421-3452 (32 lines), sha256 1d83ef550e49aeaa396c34df48924b0c4e1a650f762751086d4cc03c877eb0e0 -->
```
          +====================+===================+===========+
          | Encoding Indicator | Description       | Reference |
          +====================+===================+===========+
          | _                  | Indefinite-Length | RFC8949,  |
          |                    | Encoding (ai=31)  | RFC-XXXX  |
          +--------------------+-------------------+-----------+
          | _i                 | ai=0 to ai=23     | RFC-XXXX  |
          +--------------------+-------------------+-----------+
          | _0                 | ai=24             | RFC8949,  |
          |                    |                   | RFC-XXXX  |
          +--------------------+-------------------+-----------+
          | _1                 | ai=25             | RFC8949,  |
          |                    |                   | RFC-XXXX  |
          +--------------------+-------------------+-----------+
          | _2                 | ai=26             | RFC8949,  |
          |                    |                   | RFC-XXXX  |
          +--------------------+-------------------+-----------+
          | _3                 | ai=27             | RFC8949,  |
          |                    |                   | RFC-XXXX  |
          +--------------------+-------------------+-----------+
          | _4                 | Reserved (for     | RFC-XXXX  |
          |                    | ai=28)            |           |
          +--------------------+-------------------+-----------+
          | _5                 | Reserved (for     | RFC-XXXX  |
          |                    | ai=29)            |           |
          +--------------------+-------------------+-----------+
          | _6                 | Reserved (for     | RFC-XXXX  |
          |                    | ai=30)            |           |
          +--------------------+-------------------+-----------+
          | _7                 | Reserved (see _)  | RFC8949,  |
          |                    |                   | RFC-XXXX  |
          +--------------------+-------------------+-----------+
```

## §7.3  Media Type

- (§7.3) [`R-0199`] “IANA is requested to add the following Media-Type to the "Media Types" registry [IANA.media-types].”
- (§7.3) [`R-0200`] “Restrictions on usage: Concise diagnostic notation represents CBOR data items, which are the format intended for actual interchange. The media type application/cdn is intended to be used within documents about CBOR data items, in diagnostics for human consumption, and in other representations of CBOR data items that are necessarily text-based such as in configuration files or other data edited by humans, often under source-code control.”
- (§7.3) [`R-0201`] “Fragment identifier considerations: The syntax and semantics of fragment identifiers is as specified for "application/cbor". (At publication of RFC XXXX, there is no fragment identification syntax defined for "application/cbor".)”

**Table 10: New Media Type application/cdn**

<!-- source lines 3477-3481 (5 lines), sha256 53fdc991e3bf6f5c41a0cada65bb79f935944b637012a9a663a2aaebfe9f3346 -->
```
            +======+=================+=======================+
            | Name | Template        | Reference             |
            +======+=================+=======================+
            | cdn  | application/cdn | RFC-XXXX, Section 7.3 |
            +------+-----------------+-----------------------+
```

**Media type registration template for application/cdn**

<!-- source lines 3485-3519 (35 lines), sha256 172a68fb6201724affdf47271786195c5a908cc9e5a7ba8a67eb84a59a2c1318 -->
```
   Type name:  application
   Subtype name:  cdn
   Required parameters:  N/A
   Optional parameters:  N/A
   Encoding considerations:  binary (UTF-8)
   Security considerations:  Section 8 of RFC XXXX
   Interoperability considerations:  none
   Published specification:  Section 7.3 of RFC XXXX
   Applications that use this media type:  Tools interchanging a human-
      readable form of CBOR
   Fragment identifier considerations:  The syntax and semantics of
      fragment identifiers is as specified for "application/cbor".  (At
      publication of RFC XXXX, there is no fragment identification
      syntax defined for "application/cbor".)
   Additional information:
      Deprecated alias names for this type:  N/A

      Magic number(s):  N/A

      File extension(s):  .cdn

      Macintosh file type code(s):  N/A
   Person & email address to contact for further information:  CBOR WG
      mailing list (cbor@ietf.org), or IETF Applications and Real-Time
      Area (art@ietf.org)
   Intended usage:  LIMITED USE
   Restrictions on usage:  Concise diagnostic notation represents CBOR
      data items, which are the format intended for actual interchange.
      The media type application/cdn is intended to be used within
      documents about CBOR data items, in diagnostics for human
      consumption, and in other representations of CBOR data items that
      are necessarily text-based such as in configuration files or other
      data edited by humans, often under source-code control.
   Author/Change controller:  IETF
   Provisional registration:  no
```

## §7.4  Content-Format

- (§7.4) [`R-0202`] “TBD1 is to be assigned from the space 256..9999, according to the procedure "IETF Review or IESG Approval", preferably a number less than 1000.”

**Table 11: New Content-Format for application/cdn**

<!-- source lines 3540-3544 (5 lines), sha256 7a45f9e0c7cc30daf544a651f43412d065ba866cd49eb8d8e4c97c748ea32c2f -->
```
          +=================+================+======+===========+
          | Content-Type    | Content Coding | ID   | Reference |
          +=================+================+======+===========+
          | application/cdn | -              | TBD1 | RFC-XXXX  |
          +-----------------+----------------+------+-----------+
```

## §7.5  Tags

- (§7.5) [`R-0203`] “In the "CBOR Tags" registry [IANA.cbor-tags], IANA is requested to assign the tags in Table 12 from the "specification required" space (suggested assignments: 888 and 999), with the present document as the specification reference.”

**Table 12: Values for Tags**

_`CPA888` and `CPA999` are PLACEHOLDERS, not assignments._

<!-- source lines 3568-3576 (9 lines), sha256 43e065384b110ed7ea540a09f247af98e9d5c1a24fafe882ab2cc35c53476ebb -->
```
   +========+===============+==============================+===========+
   |    Tag | Data Item     | Semantics                    | Reference |
   +========+===============+==============================+===========+
   | CPA888 | null or array | Diagnostic Notation          | RFC-XXXX  |
   |        |               | Ellipsis                     |           |
   +--------+---------------+------------------------------+-----------+
   | CPA999 | array         | Diagnostic Notation          | RFC-XXXX  |
   |        |               | Unresolved App-Extension     |           |
   +--------+---------------+------------------------------+-----------+
```

## §8  Security considerations

- (§8) [`R-0204`] “The security considerations of [STD94] apply, including by applying the considerations about the CBOR format to the CDN format in an analogous sense. Security considerations documented in [RFC8610] for the CDDL language often are also applicable to the CDN language in an analogous sense.”
- (§8) [`R-0205`] “The CDN specification defines two explicit extension points: app- extension identifiers (Section 7.1) and encoding indicators (Section 7.2). Extensions introduced through these can have their own security considerations, which need to be considered in the specification for the extension (see, e.g., Section 5 of [I-D.ietf-cbor-edn-e-ref]).”
- (§8) [`R-0206`] “Implementers of tools that support the use of CDN extensions need to avoid inadvertently introducing a vector that allows attackers to invoke extensions not planned for by the tool operator, who might not have considered security considerations of specific extensions such as those posed by their use of dereferenceable identifiers”
- (§8) [`R-0207`] “Tools might require explicitly enabling the use of each extension that is not on an allowlist.”
- (§8) [`R-0208`] “Tools that process app-extensions — directly from their use in CDN or later via Tag CPA999 (Section 5.1) — need to be configured out of band to enable processing each specific app-extension only if that is desired. An allowlist built out of the mandatory-to-implement application extensions may be an exception.”
- (§8) [`R-0209`] “Similarly, inputs to validators may be prepared with partially specified subtrees by representing ellipses via Tag CPA888 (Section 5.2). Validators that want to accept such partially specified CBOR data items need to require explicit configuration to do so.”

## Appendix A  CDN and CDDL

- (App-A) [`R-0210`] “This appendix is for information.”
- (App-A) [`R-0211`] “CDN was designed as a language to provide a human-readable representation of an instance, i.e., a single CBOR data item or CBOR sequence. CDDL was designed as a language to describe an (often large) set of such instances (which itself constitutes a language), in the form of a _data definition_ or _grammar_ (or sometimes called _schema_).”
- (App-A) [`R-0212`] “For engineers that are using both CDN and CDDL, it is easy to write "CDDLisms" or "CDNisms" into their drafts that are meant to be in the other language. (This is one more of the many motivations to always validate formal language instances with tools.)”
- (App-A) [`R-0213`] “Comment syntax. CDDL inherits ABNF's semicolon-delimited end of line characters, while CDN finds nothing in JSON that could be inherited here.”
- (App-A) [`R-0214`] “Syntax for tags. CDDL's tag syntax is part of the system for referring to CBOR's fundamentals (the major type 6, in this case) and (with [RFC9682]) allows specifying the actual tag number separately, while CDN's tag syntax is a simple decimal number and a pair of parentheses.”
- (App-A) [`R-0215`] “Embedded CBOR. CDN has a special syntax to describe the content of byte strings that are encoded CBOR data items. CDDL can specify these with a control operator, which looks very different.”

## Editorial notes marked for removal before publication

Reproduced because two of them bear on stability, not because they are
normative. The draft writes each as a `//` cref. They will not be in the
published RFC.

<!-- source lines 29-33 (5 lines), sha256 aacca21dc5a732f023a72ca8161f19b3b7a7894e97880dd86a3718298e5c5a3b -->
**Opening editorial cref, before Section 1**

```
   // (This cref will be removed by the RFC editor:) This is the
   // editorial round focusing on editorial cleanup, specifically where
   // that causes moving text around.  It does not have WG input yet on
   // any renaming decisions (CDN name, b1/t1 name), ABNF cleanup, or
   // Rohan's suggestion to fix the questionable figure in 3.8.
```

<!-- source lines 1688-1690 (3 lines), sha256 53997f06f8851acbcaa3bca280bde7cc980224c392c272379f6432154c0dff66 -->
**Section 3.5**

```
   // This section uses the placeholders t1 and b1 as provisional app-
   // extension identifiers, allowing the text to stabilize while the
   // actual names are still being decided by the WG.
```

<!-- source lines 2195-2201 (7 lines), sha256 7bc2c8ee3399785aa545f573ad2b3429f0dd9524dd7bf30a0aadbefc3254f940 -->
**Section 5.1 (CPA code point allocation convention)**

```
   // RFC-Editor: This document uses the CPA (code point allocation)
   // convention described in [I-D.bormann-cbor-draft-numbers].  For
   // each usage of the term "CPA", please remove the prefix "CPA" from
   // the indicated value and replace the residue with the value
   // assigned by IANA; perform an analogous substitution for all other
   // occurrences of the prefix "CPA" in the document.  Finally, please
   // remove this note.
```

<!-- source lines 2567-2569 (3 lines), sha256 309e068b1f17d17d03fcce6501b2559d6fb452713ec9f3505a1cb64362e9655e -->
**Section 6.1**

```
   // Further information can be moved up to Section 2 by splitting it
   // up into information specific to the ABNF grammar and general
   // information.
```

<!-- source lines 3258-3260 (3 lines), sha256 7eee8e88d35a9edffa0513dbc61ca9f155294bd89cafc570abc9214aa63cbc9d -->
**Section 7**

```
   // RFC Editor: please replace RFC-XXXX with the RFC number of this
   // RFC, [IANA.concise-diagnostic-notation] with a reference to the
   // new registry group, and remove this note.
```

<!-- source lines 3555-3561 (7 lines), sha256 7bc2c8ee3399785aa545f573ad2b3429f0dd9524dd7bf30a0aadbefc3254f940 -->
**Section 7.5 (CPA, repeated verbatim from Section 5.1)**

```
   // RFC-Editor: This document uses the CPA (code point allocation)
   // convention described in [I-D.bormann-cbor-draft-numbers].  For
   // each usage of the term "CPA", please remove the prefix "CPA" from
   // the indicated value and replace the residue with the value
   // assigned by IANA; perform an analogous substitution for all other
   // occurrences of the prefix "CPA" in the document.  Finally, please
   // remove this note.
```

The two that matter: the opening cref says the draft has no WG input yet
on the CDN name or the `b1`/`t1` names, and the Section 3.5 cref says
`t1` and `b1` are placeholders while the WG decides. Both are in the
mandatory-to-implement set (§3).

