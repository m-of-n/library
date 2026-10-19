---
record: rfc-8610
kind: normative
title: "rfc-8610 — normative statements"
extracted: "2026-10-18"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 8610, "Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures", Standards Track, June 2019. sha256 `3713f2a50e23a2bea0a6147ad6c4433605a00c3d00a868bfa86a42b204997089` (3587 lines, plain text). Quotations are verbatim from the plain-text RFC. Blocks that reproduce tables, lists, structures, or pseudocode preserve the source's own line breaks and indentation inside fenced blocks.

**Why this file is mostly definitions.** `bin/bcp14-count` reports **2** BCP 14
keyword occurrences in 125 KB, and only **one** of them is RFC 8610 stating an
obligation of its own (§3.8.3.1); the other (Appendix H) is a quotation of
RFC 7071. CDDL's normative content is a **grammar and a type system**: it is
carried by matching rules and by definitions of what a construct *means*, not by
obligations laid on an actor. This file therefore records the
**definitional-normative** material — the type-matching rules, the group-matching
rules, the occurrence semantics, the control-operator semantics, the socket/plug
mechanism, the prelude's status — at the same grain another record would use for
MUST statements. The precedent is `records/ietf/rfc-9942/distilled/normative.md`,
which retained a Terminology section as definitional-normative; here the
definitions *are* the specification.

**Normative scope, as the document itself states it.** Appendices A, B, C, D, E
and G each open with "This appendix is normative."; Appendices F and H each open
with "This appendix is for information only." Those eight sentences are quoted
in place below and are the document's own statement of its normative extent.

**Conventions in this file.**

- A bullet `- (§X) "…"` is one contiguous verbatim span of the source. No span
  is spliced from two non-adjacent parts of the document. Contiguity is asserted
  after removing the running page header/footer decoration
  (`Birkholz, et al. … [Page n]`, `RFC 8610 CDDL June 2019`, form feeds) and
  collapsing runs of whitespace, exactly as the mechanical check in this
  record's PR applies it; no interior word, clause or punctuation mark was
  altered, dropped or reordered. Where a short display line (a CDDL fragment on
  its own line) falls inside a quoted sentence, it is part of the sentence and is
  quoted with it — the source's own sentence runs through it.
- The source's own cursive convention is preserved: `_group_` in a quote is the
  RFC's rendering of a term being introduced, not emphasis added here.
- In Appendix C the ABNF production that heads each matching rule is shown in
  `backticks` as the locator anchor for the prose that follows. The grammar
  itself (Appendix B, Figure 13) and the prelude (Appendix D, Figure 14) are
  **not** reproduced here; they are this record's `distilled/schema/` artifacts.
  Their *prose* — what gives them force — is captured below.

---

## §1. Introduction

- (§1) "In this document, a notational convention to express Concise Binary Object Representation (CBOR) data structures [RFC7049] is defined."
- (§1) "The main goal for the convention is to provide a unified notation that can be used when defining protocols that use CBOR."
- (§1) "We term the convention "Concise Data Definition Language", or CDDL."

The six goals, verbatim (§1):

- (§1) "(G1) Provide an unambiguous description of the overall structure of a CBOR data item."
- (§1) "(G2) Be flexible in expressing the multiple ways in which data can be represented in the CBOR data format."
- (§1) "(G3) Be able to express common CBOR datatypes and structures."
- (§1) "(G4) Provide a single format that is both readable and editable for humans and processable by a machine."
- (§1) "(G5) Enable automatic checking of CBOR data items for data format compliance."
- (§1) "(G6) Enable extraction of specific elements from CBOR data for further processing."

- (§1) "Not an original goal per se, but a convenient side effect of the JSON generic data model being a subset of the CBOR generic data model, is the fact that CDDL can also be used for describing JSON data structures (see Appendix E)."
- (§1) "A formal definition of CDDL using ABNF grammar [RFC5234] is provided in Appendix B."
- (§1) "Finally, a _prelude_ of standard CDDL definitions that is automatically prepended to, and thus available in, every CDDL specification is listed in Appendix D."

### §1.1. Requirements Notation

- (§1.1) "The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here."

This clause is what makes everything else in this file non-BCP-14 by the
document's own terms. §3.8.3.1 carries the only all-capitals keyword RFC 8610
asserts in its own voice.

### §1.2. Terminology

Definitional-normative: these three sentences fix how every other sentence in
the document is to be read.

- (§1.2) "New terms are introduced in _cursive_, which is rendered in plain text as the new term surrounded by underscores."
- (§1.2) "CDDL text in the running text is in "typewriter", which is rendered in plain text as the CDDL text in double quotes (double quotes are also used in the usual English sense; the reader is expected to disambiguate this by context)."
- (§1.2) "In this specification, the term "byte" is used in its now-customary sense as a synonym for "octet"."

---

## §2. The Style of Data Structure Specification

- (§2) "CDDL focuses on styles of specification that are in use in the community employing the data model as pioneered by JSON and now refined in CBOR."
- (§2) "There are a number of more or less atomic elements of a CBOR data model, such as numbers, simple values (false, true, nil), text strings, and byte strings; CDDL does not focus on specifying their structure."
- (§2) "CDDL of course also allows adding a CBOR tag to a data item."
- (§2) "Beyond those atomic elements, further components of a data structure definition language are the datatypes used for composition: arrays and maps in CBOR (called "arrays" and "objects" in JSON)."
- (§2) "While these are only two representation formats, they are used to specify four loosely distinguishable styles of composition:"

The four styles, verbatim (§2):

- (§2) "A _vector_: an array of elements that are mostly of the same semantics."
- (§2) "A _record_: an array the elements of which have different, positionally defined semantics, as detailed in the data structure definition."
- (§2) "A _table_: a map from a domain of map keys to a domain of map values, that are mostly of the same semantics."
- (§2) "The key domain is usually not limited to a specific set by the specification but is open for the application, e.g., in a table mapping IP addresses to Media Access Control (MAC) addresses, the specification does not attempt to foresee all possible IP addresses."
- (§2) "A _struct_: a map from a domain of map keys as defined by the specification to a domain of map values the semantics of each of which is bound to a specific map key."
- (§2) "This is what many people have in mind when they think about JSON objects; CBOR adds the ability to use map keys that are not just text strings."
- (§2) "Structs can be used to solve problems similar to those records are used for; the use of explicit map keys facilitates optionality and extensibility."

The two foundational concepts (§2):

- (§2) "Two important concepts provide the foundation for CDDL:"
- (§2) "Instead of defining all four types of composition in CDDL separately, or even defining one kind for arrays (vectors and records) and one kind for maps (tables and structs), there is only one kind of composition in CDDL: the _group_ (Section 2.1)."
- (§2) "The other important concept is that of a _type_."
- (§2) "The entire CDDL specification defines a type (the one defined by its first _rule_), which formally is the set of CBOR data items that are acceptable as "instances" for this specification."
- (§2) "CDDL predefines a number of basic types such as "uint" (unsigned integer) or "tstr" (text string), often making use of a simple formal notation for CBOR data items."
- (§2) "Each value that can be expressed as a CBOR data item is also a type in its own right, e.g., "1"."
- (§2) "A type can be built as a _choice_ of other types, e.g., an "int" is either a "uint" or a "nint" (negative integer)."
- (§2) "Finally, a type can be built as an array or a map from a group."
- (§2) "Appendix C gives a concise summary of the semantics of CDDL."

### §2.1. Groups and Composition in CDDL

The two matching rules in this section are the base case of the whole type
system: every array and every map in every CDDL specification matches by them.

- (§2.1) "CDDL groups are lists of group _entries_, each of which can be a name/value pair or a more complex group expression (which then in turn stands for a sequence of name/value pairs)."
- (§2.1) "A CDDL group is a production in a grammar that matches certain sequences of name/value pairs but not others."
- (§2.1) "The grammar is based on the concepts of Parsing Expression Grammars (PEGs) (see Appendix A)."
- (§2.1) "In an array context, only the value of the name/value pair is represented; the name is annotation only (and can be left off from the group specification if not needed). In a map context, the names become the map keys ("member keys")."
- (§2.1) "In an array context, the actual sequence of elements in the group is important, as that sequence is the information that allows associating actual array elements with entries in the group."
- (§2.1) "In a map context, the sequence of entries in a group is not relevant (but there is still a need to write down group entries in a sequence)."
- (§2.1) "An array matches a specification given as a group when the group matches a sequence of name/value pairs the value parts of which exactly match the elements of the array in order."
- (§2.1) "A map matches a specification given as a group when the group matches a sequence of name/value pairs such that all of these name/value pairs are present in the map and the map has no name/value pair that is not covered by the group."
- (§2.1) "A group by itself (without creating a map around it) can be placed in (round) parentheses and given a name by using it in a rule:"
- (§2.1) "Note that the (curly) braces signify the creation of a map; the groups themselves are neutral as to whether they will be used in a map or an array."
- (§2.1) "As shown in Figure 1, the parentheses for groups are optional when there is some other set of brackets present."
- (§2.1) "Groups can be used to factor out common parts of structs, e.g., instead of writing specifications in copy/paste style, such as in Figure 5, one can factor out the common subgroup, choose a name for it, and write only the specific parts into the individual maps (Figure 6)."
- (§2.1) "Note that the lists inside the braces in the above definitions constitute (anonymous) groups, while "identity" is a named group, which can then be included as part of other groups (anonymous as in the example, or themselves named)."

#### §2.1.1. Usage

- (§2.1.1) "Groups are the instrument used in composing data structures with CDDL."
- (§2.1.1) "It is a matter of style in defining those structures whether to define groups (anonymously) right in their contexts or whether to define them in a separate rule and to reference them with their respective name (possibly more than once)."
- (§2.1.1) "With this, one is allowed to define all small parts of their data structures and compose bigger protocol data units with those or to have only one big protocol data unit that has all definitions ad hoc where needed."

#### §2.1.2. Syntax

- (§2.1.2) "The composition syntax is intended to be concise and easy to read:"
- (§2.1.2) "The start and end of a group can be marked by "(" and ")"."
- (§2.1.2) "Definitions of entries inside of a group are noted as follows: _keytype => valuetype,_ (read "keytype maps to valuetype")."
- (§2.1.2) "The comma is actually optional (not just in the final entry), but it is considered good style to set it."
- (§2.1.2) "The double arrow can be replaced by a colon in the common case of directly using a text string or integer literal as a key; see Section 3.5.1."
- (§2.1.2) "This is also the common way of naming elements of an array just for documentation; see Section 3.4."
- (§2.1.2) "A basic entry consists of a _keytype_ and a _valuetype_, both of which are types (Section 2.2); this entry matches any name/value pair the name of which is in the keytype and the value of which is in the valuetype."
- (§2.1.2) "A group defined as a sequence of group entries matches any sequence of name/value pairs that is composed by concatenation in order of what the entries match."
- (§2.1.2) "A group definition can also contain choices between groups; see Section 2.2.2."

### §2.2. Types

#### §2.2.1. Values

- (§2.2.1) "Values such as numbers and strings can be used in place of a type."
- (§2.2.1) "The value notation is based on the C language, but does not offer all the syntactic variations (see Appendix B for details)."
- (§2.2.1) "The value notation for numbers inherits from C the distinction between integer values (no fractional part or exponent given -- NR1 [ISO6093]; "NR" stands for "numerical representation") and floating-point values (where a fractional part, an exponent, or both are present -- NR2 or NR3), so the type "1" does not include any floating-point numbers while the types "1e3" and "1.5" are both floating-point numbers and do not include any integer numbers."

#### §2.2.2. Choices

- (§2.2.2) "Many places that allow a type also allow a choice between types, delimited by a "/" (slash)."
- (§2.2.2) "The entire choice construct can be put into parentheses if this is required to make the construction unambiguous (please see Appendix B for details of the CDDL grammar)."
- (§2.2.2) "Choices of values can be used to express enumerations:"
- (§2.2.2) "Analogous to types, CDDL also allows choices between groups, delimited by a "//" (double slash)."
- (§2.2.2) "Note that the "//" operator binds much more weakly than the other CDDL operators, so each line within "delivery" in the following example is its own alternative in the group choice:"
- (§2.2.2) "A group choice matches the union of the sets of name/value pair sequences that the alternatives in the choice can."
- (§2.2.2) "For both type choices and group choices, additional alternatives can be added to a rule later in separate rules by using "/=" and "//=", respectively, instead of "=":"
- (§2.2.2) "It is not an error if a name is first used with a "/=" or "//=" (there is no need to "create it" with "=")."

##### §2.2.2.1. Ranges

- (§2.2.2.1) "Instead of naming all the values that make up a choice, CDDL allows building a _range_ out of two values that are in an ordering relationship: a lower bound (first value) and an upper bound (second value)."
- (§2.2.2.1) "A range can be inclusive of both bounds given (denoted by joining two values by ".."), or it can include the lower bound and exclude the upper bound (denoted by instead using "...")."
- (§2.2.2.1) "If the lower bound exceeds the upper bound, the resulting type is the empty set (this behavior can be desirable when generics (Section 3.10) are being used)."
- (§2.2.2.1) "CDDL currently only allows ranges between integers (matching integer values) or between floating-point values (matching floating-point values)."
- (§2.2.2.1) "If both are needed in a type, a type choice between the two kinds of ranges can be (clumsily) used:"
- (§2.2.2.1) "Note that the dot is a valid name continuation character in CDDL, so min..max is not a range expression but a single name."
- (§2.2.2.1) "When using a name as the left-hand side of a range operator, use spacing as in min .. max to separate off the range operator."

##### §2.2.2.2. Turning a Group into a Choice

- (§2.2.2.2) "Some choices are built out of large numbers of values, often integers, each of which is best given a semantic name in the specification."
- (§2.2.2.2) "Instead of naming each of these integers and then accumulating them into a choice, CDDL allows building a choice from a group by prefixing it with an "&" character:"
- (§2.2.2.2) "As with the use of groups in arrays (Section 3.4), the member names have only documentary value (in particular, they might be used by a tool when displaying integers that are taken from that choice)."

#### §2.2.3. Representation Types

This subsection is where CDDL states its relationship to bytes, and the
statement is a **disclaimer**: the `#major.ai` notation names a set of *values*,
not a serialization.

- (§2.2.3) "CDDL allows the specification of a data item type by referring to the CBOR representation (specifically, to major types and additional information; see Section 2 of [RFC7049])."
- (§2.2.3) "How this is used should be evident from the prelude (Appendix D): a hash mark ("#") optionally followed by a number from 0 to 7 identifying the major type, which then can be followed by a dot and a number specifying the additional information."
- (§2.2.3) "This construction specifies the set of values that can be serialized in CBOR (i.e., "any"), by the given major type if one is given, or by the given major type with the additional information if both are given."
- (§2.2.3) "Where a major type of 6 (Tag) is used, the type of the tagged item can be specified by appending it in parentheses."
- (§2.2.3) "Note that although this notation is based on the CBOR serialization, it is about a set of values at the data model level, e.g., "#7.25" specifies the set of values that can be represented as half-precision floats; it does not mandate that these values also do have to be serialized as half-precision floats: CDDL does not provide any language means to restrict the choice of serialization variants."
- (§2.2.3) "This also enables the use of CDDL with JSON, which uses a fundamentally different way of serializing (some of) the same values."
- (§2.2.3) "It may be necessary to make use of representation types outside the prelude, e.g., a specification could start by making use of an existing tag in a more specific way or could define a new tag not defined in the prelude:"

#### §2.2.4. Root Type

- (§2.2.4) "There is no special syntax to identify the root of a CDDL data structure definition: that role is simply taken by the first rule defined in the file."
- (§2.2.4) "This is motivated by the usual top-down approach for defining data structures, decomposing a big data structure unit into smaller parts; however, except for the root type, there is no need to strictly follow this sequence."
- (§2.2.4) "(Note that there is no way to use a group as a root -- it must be a type.)"

---

## §3. Syntax

- (§3) "In this section, the overall syntax of CDDL is shown, alongside some examples just illustrating syntax."
- (§3) "(The definition does not attempt to be overly formal; refer to Appendix B for details.)"

### §3.1. General Conventions

- (§3.1) "The basic syntax is inspired by ABNF [RFC5234], with the following:"
- (§3.1) "Rules, whether they define groups or types, are defined with a name, followed by an equals sign "=" and the actual definition according to the respective syntactic rules of that definition."
- (§3.1) "A name can consist of any of the characters from the set {"A" to "Z", "a" to "z", "0" to "9", "_", "-", "@", ".", "$"}, starting with an alphabetic character (including "@", "_", "$") and ending in such a character or a digit."
- (§3.1) "Names are case sensitive."
- (§3.1) "It is preferred style to start a name with a lowercase letter."
- (§3.1) "The hyphen is preferred over the underscore (except in a "bareword" (Section 3.5.1), where the semantics may actually require an underscore)."
- (§3.1) "The period may be useful for larger specifications, to express some module structure (as in "tcp.throughput" vs. "udp.throughput")."
- (§3.1) "A number of names are predefined in the CDDL prelude, as listed in Appendix D."
- (§3.1) "Rule names (types or groups) do not appear in the actual CBOR encoding, but names used as "barewords" in member keys do."
- (§3.1) "Comments are started by a ";" (semicolon) character and finish at the end of a line (LF or CRLF)."
- (§3.1) "Except within strings, whitespace (spaces, newlines, and comments) is used to separate syntactic elements for readability (and to separate identifiers, range operators, or numbers that follow each other); it is otherwise completely optional."
- (§3.1) "Hexadecimal numbers are preceded by "0x" (without quotes) and are case insensitive. Similarly, binary numbers are preceded by "0b"."
- (§3.1) "They follow the conventions for strings as defined in Section 7 of [RFC8259]."
- (§3.1) "(ABNF users may want to note that there is no support in CDDL for the concept of case insensitivity in text strings; if necessary, regular expressions can be used (Section 3.8.3).)"
- (§3.1) "Byte strings are enclosed by single quotation "'" characters and may be prefixed by "h" or "b64"."
- (§3.1) "If unprefixed, the string is interpreted as with a text string, except that single quotes must be escaped and that the resulting UTF-8 bytes are marked as a byte string (major type 2)."
- (§3.1) "If prefixed as "h" or "b64", the string is interpreted as a sequence of pairs of hex digits (base16; see Section 8 of [RFC4648]) or a base64(url) string (Section 4 or Section 5 of [RFC4648]), respectively (as with the diagnostic notation in Section 6 of [RFC7049]; cf. Appendix G.2); any whitespace present within the string (including comments) is ignored in the prefixed case."
- (§3.1) "CDDL uses UTF-8 [RFC3629] for its encoding. Processing of CDDL does not involve Unicode normalization processes."

### §3.2. Occurrence

- (§3.2) "An optional _occurrence_ indicator can be given in front of a group entry. It is either (1) one of the characters "?" (optional), "*" (zero or more), or "+" (one or more) or (2) of the form n*m, where n and m are optional unsigned integers and n is the lower limit (default 0) and m is the upper limit (default no limit) of occurrences."
- (§3.2) "If no occurrence indicator is specified, the group entry is to occur exactly once (as if 1*1 were specified)."
- (§3.2) "A group entry with an occurrence indicator matches sequences of name/value pairs that are composed by concatenating a number of sequences that the basic group entry matches, where the number needs to be allowed by the occurrence indicator."
- (§3.2) "Note that CDDL, outside any directives/annotations that could possibly be defined, does not make any prescription as to whether arrays or maps use definite-length or indefinite-length encoding. That is, there is no correlation between leaving the size of an array "open" in the spec and the fact that it is then interchanged with definite or indefinite length."
- (§3.2) "Please also note that CDDL can describe flexibility that the data model of the target representation does not have. This is rather obvious for JSON but is also relevant for CBOR:"
- (§3.2) "The previous specification does not mean that CBOR is changed to allow using the key "bedroom" more than once. In other words, due to the restrictions imposed by the data model, the third line pretty much turns into:"
- (§3.2) "(Occurrence indicators beyond one are still useful in maps for groups that allow a variety of keys.)"

### §3.3. Predefined Names for Types

- (§3.3) "CDDL predefines a number of names. This subsection summarizes these names, but please see Appendix D for the exact definitions."
- (§3.3) "The following keywords for primitive datatypes are defined:"

The primitive-datatype keywords, verbatim (§3.3):

```
"bool"  Boolean value (major type 7, additional information 20
   or 21).

"uint"  An unsigned integer (major type 0).

"nint"  A negative integer (major type 1).

"int"  An unsigned integer or a negative integer.

"float16"  A number representable as a half-precision float [IEEE754]
   (major type 7, additional information 25).

"float32"  A number representable as a single-precision float
   [IEEE754] (major type 7, additional information 26).

"float64"  A number representable as a double-precision float
   [IEEE754] (major type 7, additional information 27).

"float"  One of float16, float32, or float64.

"bstr" or "bytes"  A byte string (major type 2).

"tstr" or "text"  Text string (major type 3).
```

- (§3.3) "(Note that there are no predefined names for arrays or maps; these are defined with the syntax given below.)"
- (§3.3) "In addition, a number of types are defined in the prelude that are associated with CBOR tags, such as "tdate", "bigint", "regexp", etc."

### §3.4. Arrays

- (§3.4) "Array definitions surround a group with square brackets."
- (§3.4) "For each entry, an occurrence indicator as specified in Section 3.2 is permitted."
- (§3.4) "The group "person" is defined in such a way that repeating it in the array each time generates alternating names and ages, so these are four valid values for a data item of type "unlimited-people":"

### §3.5. Maps

- (§3.5) "The syntax for specifying maps merits special attention, as well as a number of optimizations and conveniences, as it is likely to be the focal point of many specifications employing CDDL."
- (§3.5) "While the syntax does not strictly distinguish struct and table usage of maps, it caters specifically to each of them."
- (§3.5) "But first, let's reiterate a feature of CBOR that it has inherited from JSON: the key/value pairs in CBOR maps have no fixed ordering."
- (§3.5) "Unfortunately, neither JSON nor CBOR supports this, so no attempt was made to support this in CDDL either."

#### §3.5.1. Structs

- (§3.5.1) "The "struct" usage of maps is similar to the way JSON objects are used in many JSON applications."
- (§3.5.1) "A map is defined in the same way as that for defining an array (see Section 3.4), except for using curly braces "{}" instead of square brackets "[]"."
- (§3.5.1) "An occurrence indicator as specified in Section 3.2 is permitted for each group entry."
- (§3.5.1) "When encoding, the Geography record is encoded using a CBOR array with two members (the keys for the group entries are ignored), whereas the GpsCoordinates structure is encoded as a CBOR map with two key/value pairs."
- (§3.5.1) "Types used in a structure can be defined in separate rules or just in place (potentially placed inside parentheses, such as for choices)."
- (§3.5.1) "This is actually a complete example: an identifier that is followed by a colon can be directly used as the text string for a member key (we speak of a "bareword" member key), as can a double-quoted string or a number."
- (§3.5.1) "(When other types -- in particular, types that contain more than one value -- are used as the types of keys, they are followed by a double arrow; see below.)"
- (§3.5.1) "If a text string key does not match the syntax for an identifier (or if the specifier just happens to prefer using double quotes), the text string syntax can also be used in the member key position, followed by a colon."
- (§3.5.1) "More generally, types specified in ways other than those listed for the cases described above can be used in a key-type position by following them with a double arrow -- in particular, the double arrow is necessary if a type is named by an identifier (which, when followed by a colon, would be interpreted as a "bareword" and turned into a text string)."
- (§3.5.1) "A literal text string also gives rise to a type (which contains a single value only -- the given string), so another form for this example is:"
- (§3.5.1) "See Section 3.5.4 below for how the colon (":") shortcut described here also adds some implied semantics."
- (§3.5.1) "Note that the group definition for NameComponents does not generate another map; instead, all four keys are directly in the struct built by PersonalData."
- (§3.5.1) "In this example, all key/value pairs are optional from the perspective of CDDL. With no occurrence indicator, an entry is mandatory."
- (§3.5.1) "If the addition of more entries not specified by the current specification is desired, one can add this possibility explicitly:"
- (§3.5.1) "(See Section 3.9 for one way to explicitly identify an extension point.)"

#### §3.5.2. Tables

- (§3.5.2) "A table can be specified by defining a map with entries where the key type allows more than just a single value; for example:"
- (§3.5.2) "Here, the key in each key/value pair has datatype x (defined as int), and the value has datatype y (defined as float)."
- (§3.5.2) "If the specification does not need to restrict one of x or y (i.e., the application is free to choose per entry), it can be replaced by the predefined name "any"."

#### §3.5.3. Non-deterministic Order

- (§3.5.3) "While the way arrays are matched is fully determined by the PEG formalism (see Appendix A), matching is more complicated for maps, as maps do not have an inherent order."
- (§3.5.3) "For each candidate name/value pair that the PEG algorithm would try, a matching member is picked out of the entire map."
- (§3.5.3) "For certain group expressions, more than one member in the map may match."
- (§3.5.3) "Most often, this is inconsequential, as the group expression tends to consume all matches:"
- (§3.5.3) "Here, if any member with the key "fritz" is present, this will be picked by the first entry of the group; all remaining text/number members will be picked by the second entry (and if anything remains unpicked, the map does not match)."
- (§3.5.3) "However, it is possible to construct group expressions where what is actually picked is indeterminate, but does matter:"
- (§3.5.3) "When this expression is matched against "{3: 5, 4: 6}", the first group entry might pick off the "3: 5", leaving "4: 6" for matching the second one. Or it might pick off "4: 6", leaving nothing for the second entry."
- (§3.5.3) "This pathological non-determinism is caused by specifying "more general" before "more specific" and by having a general rule that only consumes a subset of the map key/value pairs that it is able to match -- both tend not to occur in real-world specifications of maps."
- (§3.5.3) "At the time of writing, CDDL tools cannot detect such cases automatically, and for the present version of the CDDL specification, the specification writer is simply urged to not write pathologically non-deterministic specifications."
- (§3.5.3) "Note that RELAX NG's "interleave" pattern handles lack of order explicitly on the specification side, while the instances in XML always have determinate order."

#### §3.5.4. Cuts in Maps

- (§3.5.4) "The extensibility idiom discussed above for structs has one problem:"
- (§3.5.4) "In this example, there is one optional key "optional-key", which, when present, maps to an integer. There is also a wildcard for any future additions."
- (§3.5.4) "Unfortunately, the data item { "optional-key": "nonsense" } does match this specification: while the first entry of the group does not match, the second one (the wildcard) does."
- (§3.5.4) "This may very well be desirable (e.g., if a future extension is to be allowed to extend the type of "optional-key"), but in many cases it isn't."
- (§3.5.4) "In anticipation of a more general potential feature called "cuts", CDDL allows inserting a cut "^" into the definition of the map entry:"
- (§3.5.4) "A cut in this position means that once the member key matches the name part of an entry that carries a cut, other potential matches for the key of the member that occur in later entries in the group of the map are no longer allowed."
- (§3.5.4) "In other words, when a group entry would pick a key/value pair based on just a matching key, it "locks in" the pick -- this rule applies, independently of whether the value matches as well, so when it does not, the entire map fails to match."
- (§3.5.4) "In summary, the example above no longer matches the specification as modified with the cut."
- (§3.5.4) "Since the desire for this kind of exclusive matching is so frequent, the ":" shortcut is actually defined to include the cut semantics."

### §3.6. Tags

- (§3.6) "A type can make use of a CBOR tag (major type 6) by using the representation type notation, giving #6.nnn(type) where nnn is an unsigned integer giving the tag number and "type" is the type of the data item being tagged."
- (§3.6) "For example, the following line from the CDDL prelude (Appendix D) defines "biguint" as a type name for an unsigned bignum N:"
- (§3.6) "The tags defined by [RFC7049] are included in the prelude."
- (§3.6) "Additional tags registered since [RFC7049] was written need to be added to a CDDL specification as needed; e.g., a binary Universally Unique Identifier (UUID) tag could be referenced as "buuid" in a specification after defining"
- (§3.6) "In the following example, usage of tag 32 for URIs is optional:"

### §3.7. Unwrapping

- (§3.7) "The group that is used to define a map or an array can often be reused in the definition of another map or array. Similarly, a type defined as a tag carries an internal data item that one would like to refer to."
- (§3.7) "In these cases, it is expedient to simply use the name of the map, array, or tag type as a handle for the group or type defined inside it."
- (§3.7) "The "unwrap" operator (written by preceding a name by a tilde character "~") can be used to strip the type defined for a name by one layer, exposing the underlying group (for maps and arrays) or type (for tags)."
- (§3.7) "(Note that leaving out the first unwrap operator in the latter example would lead to nesting the basic-header in its own array inside the advanced-header, while, with the unwrapped basic-header, the definition of the group inside basic-header is essentially repeated inside advanced-header, leading to a single array."
- (§3.7) "This can be used for various applications often solved by inheritance in programming languages."
- (§3.7) "The effect of unwrapping can also be described as "threading in" the group or type inside the referenced type, which suggested the thread-like "~" character.)"

### §3.8. Controls

- (§3.8) "A _control_ allows relating a _target_ type with a _controller_ type via a _control operator_."
- (§3.8) "The syntax for a control type is "target .control-operator controller", where control operators are special identifiers prefixed by a dot."
- (§3.8) "(Note that _target_ or _controller_ might need to be parenthesized.)"
- (§3.8) "A number of control operators are defined at this point. Further control operators may be defined by new versions of this specification or by registering them according to the procedures in Section 6.1."

#### §3.8.1. Control Operator .size

- (§3.8.1) "A ".size" control controls the size of the target in bytes by the control type."
- (§3.8.1) "The control is defined for text and byte strings, where it directly controls the number of bytes in the string. It is also defined for unsigned integers (see below)."
- (§3.8.1) "When applied to an unsigned integer, the ".size" control restricts the range of that integer by giving a maximum number of bytes that should be needed in a computer representation of that unsigned integer. In other words, "uint .size N" is equivalent to "0...BYTES_N", where BYTES_N == 256**N."
- (§3.8.1) "Note that, as with value restrictions in CDDL, this control is not a representation constraint; a number that fits into fewer bytes can still be represented in that form, and an inefficient implementation could use a longer form (unless that is restricted by some format constraints outside of CDDL, such as the rules in Section 3.9 of [RFC7049])."

#### §3.8.2. Control Operator .bits

- (§3.8.2) "A ".bits" control on a byte string indicates that, in the target, only the bits numbered by a number in the control type are allowed to be set."
- (§3.8.2) "(Bits are counted the usual way, bit number "n" being set in "str" meaning that "(str[n >> 3] & (1 << (n & 7))) != 0".)"
- (§3.8.2) "Similarly, a ".bits" control on an unsigned integer "i" indicates that for all unsigned integers "n" where "(i & (1 << n)) != 0", "n" must be in the control type."
- (§3.8.2) "These examples do not illustrate that the above CDDL specification does not explicitly specify a size of two bytes: a valid all-clear instance of flag bytes could be "h''" or "h'00'" or even "h'000000'" as well."

#### §3.8.3. Control Operator .regexp

- (§3.8.3) "A ".regexp" control indicates that the text string given as a target needs to match the XML Schema Definition (XSD) regular expression given as a value in the control type."
- (§3.8.3) "XSD regular expressions are defined in Appendix F of [W3C.REC-xmlschema-2-20041028]."

##### §3.8.3.1. Usage Considerations

**The only BCP 14 keyword RFC 8610 asserts in its own voice.**

- (§3.8.3.1) "Note that XSD regular expressions do not support the usual \x or \u escapes for hexadecimal expression of bytes or Unicode code points."
- (§3.8.3.1) "However, in CDDL the XSD regular expressions are contained in text strings, the literal notation for which provides \u escapes; this should suffice for most applications that use regular expressions for text strings."
- (§3.8.3.1) "(Note that this also means that there is one level of string escaping before the XSD escaping rules are applied.)"
- (§3.8.3.1) "XSD regular expressions support character class subtraction, a feature often not found in regular expression libraries; specification writers may want to use this feature sparingly. Similar considerations apply to Unicode character classes; where these are used, the specification that employs CDDL SHOULD identify which Unicode versions are addressed."
- (§3.8.3.1) "No direct support for case insensitivity."
- (§3.8.3.1) "While case insensitivity has gone mostly out of fashion in protocol design, it is sometimes needed and then needs to be expressed manually as in "[Cc][Aa][Ss][Ee]"."
- (§3.8.3.1) "The support for popular character classes such as \w and \d is based on Unicode character properties; this is often not what is desired in an ASCII-based protocol and thus might lead to surprises."

##### §3.8.3.2. Discussion

- (§3.8.3.2) "However, there is no normative reference for PCREs that could be used in the present document. Instead, we opt for XSD regular expressions for now."
- (§3.8.3.2) "Note that CDDL uses controls as its main extension point. This creates the opportunity to add further regular expression formats in addition to the one referenced here, if desired."

#### §3.8.4. Control Operators .cbor and .cborseq

- (§3.8.4) "A ".cbor" control on a byte string indicates that the byte string carries a CBOR-encoded data item. Decoded, the data item matches the type given as the right-hand-side argument (type1 in the following example)."
- (§3.8.4) "Similarly, a ".cborseq" control on a byte string indicates that the byte string carries a sequence of CBOR-encoded data items. When the data items are taken as an array, the array matches the type given as the right-hand-side argument (type2 in the following example)."
- (§3.8.4) "(The conversion of the encoded sequence to an array can be effected, for instance, by wrapping the byte string between the two bytes 0x9f and 0xff and decoding the wrapped byte string as a CBOR-encoded data item.)"

#### §3.8.5. Control Operators .within and .and

- (§3.8.5) "A ".and" control on a type indicates that the data item matches both the left-hand-side type and the type given as the right-hand side. (Formally, the resulting type is the intersection of the two types given.)"
- (§3.8.5) "A variant of the ".and" control is the ".within" control, which expresses an additional intent: the left-hand-side type is meant to be a subset of the right-hand-side type."
- (§3.8.5) "While both forms have the identical formal semantics (intersection), the intention of the ".within" form is that the right-hand side gives guidance to the types allowed on the left-hand side, which typically is a socket (Section 3.9):"
- (§3.8.5) "For ".within", a tool might flag an error if type1 allows data items that are not allowed by type2. In contrast, for ".and", there is no expectation that type1 is already a subset of type2."

#### §3.8.6. Control Operators .lt, .le, .gt, .ge, .eq, .ne, and .default

The equality semantics here are the only value-equality definition CDDL gives.

- (§3.8.6) "The controls .lt, .le, .gt, .ge, .eq, and .ne specify a constraint on the left-hand-side type to be a value less than, less than or equal to, greater than, greater than or equal to, equal to, or not equal to a value given as a right-hand-side type (containing just that single value)."
- (§3.8.6) "In the present specification, the first four controls (.lt, .le, .gt, and .ge) are defined only for numeric types, as these have a natural ordering relationship."
- (§3.8.6) ".ne and .eq are defined for both numeric values and values of other types. If one of the values is not of a numeric type, equality is determined as follows: text strings are equal (satisfy .eq / do not satisfy .ne) if they are bytewise identical; the same applies for byte strings. Arrays are equal if they have the same number of elements, all of which are equal pairwise in order between the arrays. Maps are equal if they have the same number of key/value pairs, and there is pairwise equality between the key/value pairs between the two maps. Tagged values are equal if they both have the same tag and the values are equal. Values of simple types match if they are the same values. Numeric types that occur within arrays, maps, or tagged values are equal if their numeric value is equal and they are both integers or both floating-point values. All other cases are not equal (e.g., comparing a text string with a byte string)."
- (§3.8.6) "A variant of the ".ne" control is the ".default" control, which expresses an additional intent: the value specified by the right-hand-side type is intended as a default value for the left-hand-side type given, and the implied .ne control is there to prevent this value from being sent over the wire."
- (§3.8.6) "This control is only meaningful when the control type is used in an optional context; otherwise, there would be no way to make use of the default value."

### §3.9. Socket/Plug

CDDL's own extension mechanism, and the only one that needs no registry.

- (§3.9) "For both type choices and group choices, a mechanism is defined that facilitates starting out with empty choices and assembling them later, potentially in separate files that are concatenated to build the full specification."
- (§3.9) "Per convention, CDDL extension points are marked with a leading dollar sign (types) or two leading dollar signs (groups). Tools honor that convention by not raising an error if such a type or group is not defined at all; the symbol is then taken to be an empty type choice (group choice), i.e., no choice is available."
- (§3.9) "Names that start with a single "$" are "type sockets", starting out as an empty type, and intended to be extended via "/=". Names that start with a double "$$" are "group sockets", starting out as an empty group choice, and intended to be extended via "//="."
- (§3.9) "In either case, it is not an error if there is no definition for a socket at all; this then means there is no way to satisfy the rule (i.e., the choice is empty)."
- (§3.9) "As a convention, all definitions (plugs) for socket names must be augmentations, i.e., they must be using "/=" and "//=", respectively."
- (§3.9) "To pick up the example illustrated in Figure 7, the socket/plug mechanism could be used as shown in Figure 12:"

### §3.10. Generics

- (§3.10) "Using angle brackets, the left-hand side of a rule can add formal parameters after the name being defined, as in:"
- (§3.10) "When using a generic rule, the formal parameters are bound to the actual arguments supplied (also using angle brackets), within the scope of the generic rule (as if there were a rule of the form parameter = argument)."
- (§3.10) "Generic rules can be used for establishing names for both types and groups."
- (§3.10) "(At this time, there are some limitations to the nesting of generics in the CDDL tool described in Appendix F.)"

### §3.11. Operator Precedence

- (§3.11) "As with any language that has multiple syntactic features such as prefix and infix operators, CDDL has operators that bind more tightly than others."
- (§3.11) "This is becoming more complicated than, say, in ABNF, as CDDL has both types and groups, with operators that are specific to these concepts."
- (§3.11) "Type operators (such as "/" for type choice) operate on types, while group operators (such as "//" for group choice) operate on groups. Types can simply be used in groups, but groups need to be bracketed (as arrays or maps) to become types. So, type operators naturally bind closer than group operators."
- (§3.11) "group1 is a group choice between the type choice of a and b and the type choice of c and d."
- (§3.11) "is a group choice between the optional member "ab" of type a or b and the member "cd" of type c or d. Note that the optionality is attached to the first choice ("ab"), not to the second choice."
- (§3.11) "group3 is a repetition of a type choice between a, b, and c; if just a is to be repeatable, a group choice is needed to focus the occurrence:"
- (§3.11) "group4 is a group choice between a repeatable a and a single b or c."
- (§3.11) "A comment has been that the semantics of group3 could be counterintuitive. In general, as with many other languages with operator precedence rules, the specification writer is encouraged not to rely on them, but to insert parentheses liberally to guide readers that are not familiar with CDDL precedence rules:"
- (§3.11) "The operator precedences, in sequence of loose to tight binding, are defined in Appendix B and summarized in Table 1. (Arities given are 1 for unary prefix operators and 2 for binary infix operators.)"

Table 1, verbatim (§3.11):

```
+----------+-------+---------------------------+------------+
| Operator | Arity | Operates on               | Precedence |
+----------+-------+---------------------------+------------+
|    =     |   2   | name = type, name = group |     1      |
|    /=    |   2   | name /= type              |     1      |
|   //=    |   2   | name //= group            |     1      |
|    //    |   2   | group // group            |     2      |
|    ,     |   2   | group, group              |     3      |
|    *     |   1   | * group                   |     4      |
|   n*m    |   1   | n*m group                 |     4      |
|    +     |   1   | + group                   |     4      |
|    ?     |   1   | ? group                   |     4      |
|    =>    |   2   | type => type              |     5      |
|    :     |   2   | name: type                |     5      |
|    /     |   2   | type / type               |     6      |
|    ..    |   2   | type..type                |     7      |
|   ...    |   2   | type...type               |     7      |
|  .ctrl   |   2   | type .ctrl type           |     7      |
|    &     |   1   | &group                    |     8      |
|    ~     |   1   | ~type                     |     8      |
+----------+-------+---------------------------+------------+
```

---

## §4. Making Use of CDDL

### §4.1. As a Guide for a Human User

- (§4.1) "CDDL can be used to efficiently define the layout of CBOR data, such that a human implementer can easily see how data is supposed to be encoded."
- (§4.1) "Since CDDL maps parts of the CBOR data to human-readable names, tools could be built that use CDDL to provide a human-friendly representation of the CBOR data and allow them to edit such data while remaining compliant with its CDDL definition."

### §4.2. For Automated Checking of CBOR Data Structures

This section is where CDDL declines to say how much checking is required —
load-bearing for any verifier that leans on a CDDL schema.

- (§4.2) "CDDL has been specified such that a machine can handle the CDDL definition and related CBOR data (and, thus, also JSON data). For example, a machine could use CDDL to check whether or not CBOR data is compliant with its definition."
- (§4.2) "The need for thoroughness of such compliance checking depends on the application. For example, an application may decide not to check the data structure at all and use the CDDL definition solely as a means to indicate the structure of the data to the programmer."
- (§4.2) "On the other hand, the application may also implement a checking mechanism that goes as far as checking that all mandatory map members are available."
- (§4.2) "The matter of how far the data description must be enforced by an application is left to the designers and implementers of that application, keeping in mind related security considerations."
- (§4.2) "In no case is it intended that a CDDL tool would be "writing code" for an implementation."

### §4.3. For Data Analysis Tools

- (§4.3) "Where there is data, there is data analysis and the need to process such data automatically. CDDL can be used for such automated data processing, allowing tools to verify data, clean it, and extract particular parts of interest from it."

---

## §5. Security Considerations

- (§5) "This document presents a content rules language for expressing CBOR data structures. As such, it does not bring any security issues on itself, although specifications of protocols that use CBOR naturally need security analyses when defined."
- (§5) "General guidelines for writing security considerations are defined in [RFC3552] (BCP 72). Specifications using CDDL to define CBOR structures in protocols need to follow those guidelines."
- (§5) "Additional topics that could be considered in a security considerations section for a specification that uses CDDL to define CBOR structures include the following:"
- (§5) "Where could the language maybe cause confusion in a way that will enable security issues?"
- (§5) "Where a CDDL matcher is part of the implementation of a system, the security of the system ought not depend on the correctness of the CDDL specification or CDDL implementation without any further defenses in place."
- (§5) "Where the CDDL specification includes extension points, the impact of extensions on the security of the system needs to be carefully considered."
- (§5) "Writers of CDDL specifications are strongly encouraged to value clarity and transparency of the specification over its elegance. Keep it as simple as possible while still expressing the needed data model."
- (§5) "A related observation about formal description techniques in general that is strongly recommended to be kept in mind by writers of CDDL specifications: just because CDDL makes it easier to handle complexity in a specification, that does not make that complexity somehow less bad (except maybe on the level of the humans having to grasp the complex structure while reading the spec)."

---

## §6. IANA Considerations

### §6.1. CDDL Control Operators Registry

CDDL's declared main extension point (§3.8.3.2) is registry-governed. These are
the governing rules.

- (§6.1) "IANA has created a registry for control operators (Section 3.8). The "CDDL Control Operators" registry has been created within the "Concise Data Definition Language (CDDL)" registry."
- (§6.1) "Each entry in the subregistry must include the name of the control operator (by convention given with the leading dot) and a reference to its documentation. Names must be composed of the leading dot followed by a text string conforming to the production "id" in Appendix B."
- (§6.1) "Initial entries in this registry are as follows:"

Initial registry contents, verbatim (§6.1):

```
+----------+---------------+
| Name     | Documentation |
+----------+---------------+
| .size    | RFC 8610      |
| .bits    | RFC 8610      |
| .regexp  | RFC 8610      |
| .cbor    | RFC 8610      |
| .cborseq | RFC 8610      |
| .within  | RFC 8610      |
| .and     | RFC 8610      |
| .lt      | RFC 8610      |
| .le      | RFC 8610      |
| .gt      | RFC 8610      |
| .ge      | RFC 8610      |
| .eq      | RFC 8610      |
| .ne      | RFC 8610      |
| .default | RFC 8610      |
+----------+---------------+
```

- (§6.1) "All other control operator names are Unassigned."
- (§6.1) "The IANA policy for additions to this registry is "Specification Required" as defined in [RFC8126] (which involves an Expert Review) for names that do not include an internal dot and "IETF Review" for names that do include an internal dot."
- (§6.1) "The expert reviewer is specifically instructed that other Standards Development Organizations (SDOs) may want to define control operators that are specific to their fields (e.g., based on a binary syntax already in use at the SDO); the review process should strive to facilitate such an undertaking."

---

## Appendix A. Parsing Expression Grammars (PEGs)

- (Appendix A) "This appendix is normative."

The formal foundation of all CDDL matching. Prioritized choice and greedy
occurrence are the two properties that make matching deterministic for arrays
and that §3.5.3 says do *not* settle matching for maps.

- (Appendix A) "PEGs [PEG] provide an alternative formal foundation for describing grammars that emphasizes recognition over generation and resolves what would have been ambiguity in generative systems by introducing the concept of "prioritized choice"."
- (Appendix A) "The notation for PEGs is quite close to BNF, with the usual "Extended BNF" features, such as repetition, added."
- (Appendix A) "However, where BNF uses the unordered (symmetrical) choice operator "|" (incidentally notated as "/" in ABNF), PEG provides a prioritized choice operator "/". The two alternatives listed are to be tested in left-to-right order, locking in the first successful match and disregarding any further potential matches within the choice (but not disabling alternatives in choices containing this choice, as a cut (Section 3.5.4) would)."
- (Appendix A) "are equivalent in ABNF's original generative framework but are very different in PEG: in (2), the second alternative will never match, as any input string starting with an "a" will already succeed in the first alternative, locking in the match."
- (Appendix A) "Similarly, the occurrence indicators ("?", "*", "+") are "greedy" in PEG, i.e., they consume as much input as they match (and, as a consequence, "a* a" in PEG notation or "*a a" in CDDL syntax never can match anything, as all input matching "a" is already consumed by the initial "a*", leaving nothing to match the second "a")."
- (Appendix A) "Incidentally, the grammar of CDDL itself, as written in ABNF in Appendix B, can be interpreted both (1) in the generative framework on which RFC 5234 is based and (2) as a PEG."
- (Appendix A) "This was made possible by ordering the choices in the grammar such that a successful match made on the left-hand side of a "/" operator is always the intended match, instead of relying on the power of symmetrical choices (for example, note the sequence of alternatives in the rule for "uint", where the lone zero is behind the longer match alternatives that start with a zero)."
- (Appendix A) "The syntax used for expressing the PEG component of CDDL is based on ABNF, interpreted in the obvious way with PEG semantics."
- (Appendix A) "The ABNF convention of notating occurrence indicators before the controlled primary, and of allowing numeric values for minimum and maximum occurrence around a "*" sign, is copied."
- (Appendix A) "While PEG is only about characters, CDDL has a richer set of elements, such as types and groups. Specifically, the following constructs map:"

CDDL-to-PEG construct mapping, verbatim (Appendix A):

```
+-------+-------+-------------------------------------------+
| CDDL  | PEG   | Remark                                    |
+-------+-------+-------------------------------------------+
| "="   | "<-"  | /= and //= are abbreviations              |
| "//"  | "/"   | prioritized choice                        |
| "/"   | "/"   | prioritized choice, limited to types only |
| "?" P | P "?" | zero or one                               |
| "*" P | P "*" | zero or more                              |
| "+" P | P "+" | one or more                               |
| A B   | A B   | sequence                                  |
| A, B  | A B   | sequence, comma is decoration only        |
+-------+-------+-------------------------------------------+
```

- (Appendix A) "The literal notation and the use of square brackets, curly braces, tildes, ampersands, and hash marks are specific to CDDL and unrelated to the conventional PEG notation."
- (Appendix A) "The DOT (".") from PEG is replaced by the unadorned "#" or its alias "any"."
- (Appendix A) "Also, CDDL does not provide the syntactic predicate operators NOT ("!") or AND ("&") from PEG, reducing expressiveness as well as complexity."

---

## Appendix B. ABNF Grammar

- (Appendix B) "This appendix is normative."
- (Appendix B) "The following is a formal definition of the CDDL syntax in ABNF [RFC5234]. Note that, as is defined in ABNF, the quote-delimited strings below are case insensitive (while string values and names are case sensitive in CDDL)."
- (Appendix B) "Note that this ABNF does not attempt to reflect the detailed rules of what can be in a prefixed byte string."

The grammar itself is Figure 13 and is carried verbatim in this record's
`distilled/schema/`, not reproduced here.

---

## Appendix C. Matching Rules

- (Appendix C) "This appendix is normative."
- (Appendix C) "In this appendix, we go through the ABNF syntax rules defined in Appendix B and briefly describe the matching semantics of each syntactic feature. In this context, an instance (data item) "matches" a CDDL specification if it is allowed by the CDDL specification; this is then broken down into parts of specifications (type and group expressions) and parts of instances (data items)."

This appendix is the specification. Each production below is Appendix C's own
anchor for the prose that follows it.

**`cddl = S 1*(rule S)`**

- (Appendix C) "A CDDL specification is a sequence of one or more rules. Each rule gives a name to a right-hand-side expression, either a CDDL type or a CDDL group. Rule names can be used in the rule itself and/or other rules (and tools can output warnings if that is not the case). The order of the rules is significant only in two cases:"
- (Appendix C) "The first rule defines the semantics of the entire specification; hence, there is no need to give that root rule a special name or special syntax in the language (as, for example, with "start" in RELAX NG); its name can therefore be chosen to be descriptive."
- (Appendix C) "(As with all other rule names, the name of the initial rule may be used in itself or in other rules.)"
- (Appendix C) "Where a rule contributes to a type or group choice (using "/=" or "//="), that choice is populated in the order the rules are given; see below."

**`rule = typename [genericparm] S assignt S type / groupname [genericparm] S assigng S grpent`**

- (Appendix C) "A rule defines a name for a type expression (production "type") or for a group expression (production "grpent"), with the intention that the semantics does not change when the name is replaced by its (parenthesized if needed) definition."
- (Appendix C) "Note that whether the name defined by a rule stands for a type or a group isn't always determined by syntax alone: e.g., "a = b" can make "a" a type if "b" is a type, or a group if "b" is a group."
- (Appendix C) "More subtly, in "a = (b)", "a" may be used as a type if "b" is a type, or as a group both when "b" is a group and when "b" is a type (a good convention to make the latter case stand out to the human reader is to write "a = (b,)")."
- (Appendix C) "(Note that the same dual meaning of parentheses applies within an expression but often can be resolved by the context of the parenthesized expression. On the more general point, it may not be clear immediately either whether "b" stands for a group or a type -- this semantic processing may need to span several levels of rule definitions before a determination can be made.)"

**`assignt = "=" / "/="` · `assigng = "=" / "//="`**

- (Appendix C) "A plain equals sign defines the rule name as the equivalent of the expression to the right; it is an error if the name was already defined with a different expression."
- (Appendix C) "A "/=" or "//=" extends a named type or a group by additional choices; a number of these could be replaced by collecting all the right-hand sides and creating a single rule with a type choice or a group choice built from the right-hand sides in the order of the rules given."
- (Appendix C) "(It is not an error to extend a rule name that has not yet been defined; this makes the right-hand side the first entry in the choice being created.)"

**`genericparm` · `genericarg`**

- (Appendix C) "Rule names can have generic parameters, which cause temporary assignments within the right-hand sides to the parameter names from the arguments given when citing the rule name."

**`type = type1 *(S "/" S type1)`**

- (Appendix C) "A type can be given as a choice between one or more types. The choice matches a data item if the data item matches any one of the types given in the choice. The choice uses PEG semantics as discussed in Appendix A: the first choice that matches wins. (As a result, the order of rules that contribute to a single rule name can very well matter.)"

**`type1 = type2 [S (rangeop / ctlop) S type2]`**

- (Appendix C) "Two types can be combined with a range operator (see below) or a control operator (see Section 3.8)."

**`type2` — the eight alternatives**

- (Appendix C) "A type can be just a single value (such as 1 or "icecream" or h'0815'), which matches only a data item with that specific value (no conversions defined),"
- (Appendix C) "or be defined by a rule giving a meaning to a name (possibly after supplying generic arguments as required by the generic parameters),"
- (Appendix C) "or be defined in a parenthesized type expression (parentheses may be necessary to override some operator precedence), or"
- (Appendix C) "a map expression, which matches a valid CBOR map the key/value pairs of which can be ordered in such a way that the resulting sequence matches the group expression, or"
- (Appendix C) "an array expression, which matches a CBOR array the elements of which -- when taken as values and complemented by a wildcard (matches anything) key each -- match the group, or"
- (Appendix C) "an "unwrapped" group (see Section 3.7), which matches the group inside a type defined as a map or an array by wrapping the group, or"
- (Appendix C) "an enumeration expression, which matches any value that is within the set of values that the values of the group given can take, or"
- (Appendix C) "a tagged data item, tagged with the "uint" given and containing the type given as the tagged value, or"
- (Appendix C) "a data item of a major type (given by the DIGIT), optionally constrained to the additional information given by the uint, or"
- (Appendix C) "any data item."

**`rangeop = "..." / ".."`**

- (Appendix C) "A range operator can be used to join two type expressions that stand for either two integer values or two floating-point values; it matches any value that is between the two values, where the first value is always included in the matching set and the second value is included for ".." and excluded for "..."."

**`ctlop = "." id`**

- (Appendix C) "A control operator ties a _target_ type to a _controller_ type as defined in Section 3.8. Note that control operators are an extension point for CDDL; additional documents may want to define additional control operators."

**`group = grpchoice *(S "//" S grpchoice)`**

- (Appendix C) "A group matches any sequence of key/value pairs that matches any of the choices given (again using PEG semantics)."

**`grpchoice = *(grpent optcom)`**

- (Appendix C) "Each of the component groups is given as a sequence of group entries. For a match, the sequence of key/value pairs given needs to match the sequence of group entries in the sequence given."

**`grpent` — the three alternatives**

- (Appendix C) "A group entry can be given by a value type, which needs to be matched by the value part of a single element; and, optionally, a memberkey type, which needs to be matched by the key part of the element, if the memberkey is given."
- (Appendix C) "If the memberkey is not given, the entry can only be used for matching arrays, not for maps. (See below for how that is modified by the occurrence indicator.)"
- (Appendix C) "A group entry can be built from a named group, or"
- (Appendix C) "from a parenthesized group, again with a possible occurrence indicator."

**`memberkey = type1 S ["^" S] "=>" / bareword S ":" / value S ":"`**

- (Appendix C) "Key types can be given by a type expression, a bareword (which stands for a type that just contains a string value created from this bareword), or a value (which stands for a type that just contains this value). A key value matches its key type if the key value is a member of the key type, unless a cut preceding it in the group applies (see Section 3.5.4 for how map matching is influenced by the presence of the cuts denoted by "^" or ":" in previous entries)."

**`bareword = id`**

- (Appendix C) "A bareword is an alternative way to write a type with a single text string value; it can only be used in the syntactic context given above."

**`optcom = S ["," S]`**

- (Appendix C) "(Optional commas do not influence the matching.)"

**`occur = [uint] "*" [uint] / "+" / "?"`**

- (Appendix C) "An occurrence indicator modifies the group given to its right by requiring the group to match the sequence to be matched exactly for a certain number of times (see Section 3.2) in sequence, i.e., it acts as a (possibly infinite) group choice that contains choices with the group repeated each of the occurrences times."

**Closing**

- (Appendix C) "The rest of the ABNF describes syntax for value notation that should be familiar to readers from programming languages, with the possible exception of h'..' and b64'..' for byte strings, as well as syntactic elements such as comments and line ends."

---

## Appendix D. Standard Prelude

- (Appendix D) "This appendix is normative."
- (Appendix D) "The following prelude is automatically added to each CDDL file. (Note that technically, it is a postlude, as it does not disturb the selection of the first rule as the root of the definition.)"
- (Appendix D) "Note that the prelude is deemed to be fixed. This means, for instance, that additional tags beyond those defined in [RFC7049], as registered, need to be defined in each CDDL file that is using them."
- (Appendix D) "A common stumbling point is that the prelude does not define a type "string". CBOR has byte strings ("bytes" in the prelude) and text strings ("text"), so a type that is simply called "string" would be ambiguous."

The prelude itself is Figure 14 and is carried verbatim in this record's
`distilled/schema/`, not reproduced here.

---

## Appendix E. Use with JSON

- (Appendix E) "This appendix is normative."
- (Appendix E) "The JSON generic data model (implicit in [RFC8259]) is a subset of the generic data model of CBOR. So, one can use CDDL with JSON by limiting oneself to what can be represented in JSON. Roughly speaking, this means leaving out byte strings, tags, and simple values other than "false", "true", and "null", leading to the following limited prelude:"
- (Appendix E) "(The major types given here do not have a direct meaning in JSON, but they can be interpreted as CBOR major types translated through Section 4 of [RFC7049].)"
- (Appendix E) "First, JSON does not distinguish between integers and floating-point numbers; there is only one kind of number (which may happen to be integral). In this context, specifying a type as "uint", "nint", or "int" then becomes a predicate that the number be integral."
- (Appendix E) "CDDL distinguishes the various CBOR number types, but there is only one number type in JSON. The effect of specifying a floating-point precision (float16/float32/float64) is only to restrict the set of permissible values to those expressible with binary16/binary32/ binary64; this is unlikely to be very useful when using CDDL for specifying JSON data structures."
- (Appendix E) "Fundamentally, the number system of JSON itself is based on decimal numbers and decimal fractions and does not have limits to its precision or range."
- (Appendix E) "In particular, this means that integers can only be expressed with interoperable exactness when they lie in the range [-(2**53)+1, (2**53)-1] -- a smaller range than that covered by CDDL "int"."
- (Appendix E) "Note that the types given here are not part of the prelude; they need to be copied into the CDDL specification if needed."
- (Appendix E) "CDDL at this point does not have a way to express the unlimited floating-point precision that is theoretically possible with JSON; at the time of writing, this is rarely used in protocols in practice."
- (Appendix E) "Note that a data model described in CDDL is always restricted by what can be expressed in the serialization; e.g., floating-point values such as NaN (not a number) and the infinities cannot be represented in JSON even if they are allowed in the CDDL generic data model."

The JSON-compatible prelude subset (Figure 15) and the I-JSON types
(Figure 16) are carried in this record's `distilled/schema/`.

---

## Appendix F. A CDDL Tool

- (Appendix F) "This appendix is for information only."

Informative. Tool invocation and installation are not reproduced as normative
statements; they are captured as fixtures in this record's `distilled/examples/`.

---

## Appendix G. Extended Diagnostic Notation

- (Appendix G) "This appendix is normative."
- (Appendix G) "Section 6 of [RFC7049] defines a "diagnostic notation" in order to be able to converse about CBOR data items without having to resort to binary data. Diagnostic notation is based on JSON, with extensions for representing CBOR constructs such as binary data and tags."
- (Appendix G) "(Standardizing this together with the actual interchange format does not serve to create another interchange format but enables the use of a shared diagnostic notation in tools for and documents about CBOR.)"
- (Appendix G) "This appendix discusses a few extensions to the diagnostic notation that have turned out to be useful since RFC 7049 was written. We refer to the result as Extended Diagnostic Notation (EDN)."

### Appendix G.1. Whitespace in Byte String Notation

- (Appendix G.1) "In EDN, whitespace is ignored in prefixed byte strings; for instance, the following are equivalent:"

### Appendix G.2. Text in Byte String Notation

- (Appendix G.2) "Diagnostic notation notates byte strings in one of the base encodings per [RFC4648], enclosed in single quotes, prefixed by >h< for base16, >b32< for base32, >h32< for base32hex, or >b64< for base64 or base64url."
- (Appendix G.2) "EDN allows the use of single quotes without a prefix to express byte strings with UTF-8 text; for instance, the following are equivalent:"
- (Appendix G.2) "The escaping rules of JSON strings are applied equivalently for text-based byte strings, e.g., "\" stands for a single backslash and "'" stands for a single quote. Whitespace is included literally, i.e., the previous section does not apply to text-based byte strings."

### Appendix G.3. Embedded CBOR and CBOR Sequences in Byte Strings

- (Appendix G.3) "Where a byte string is to carry an embedded CBOR-encoded item, or more generally a sequence of zero or more such items, the diagnostic notation for these zero or more CBOR data items, separated by commas, can be enclosed in << and >> to notate the byte string resulting from encoding the data items and concatenating the result."

### Appendix G.4. Concatenated Strings

- (Appendix G.4) "We extend the diagnostic notation by allowing multiple text strings or multiple byte strings to be notated separated by whitespace; these are then concatenated into a single text or byte string, respectively."
- (Appendix G.4) "Text strings and byte strings do not mix within such a concatenation, except that byte string notation can be used inside a sequence of concatenated text string notation to encode characters that may be better represented in an encoded way."
- (Appendix G.4) "(Note that the approach of separating by whitespace, while familiar from the C language, requires some attention -- a single comma makes a big difference here.)"

### Appendix G.5. Hexadecimal, Octal, and Binary Numbers

- (Appendix G.5) "In addition to JSON's decimal numbers, EDN provides hexadecimal, octal, and binary numbers in the usual C-language notation (octal with 0o prefix present only)."

### Appendix G.6. Comments

- (Appendix G.6) "In EDN, comments can be included, delimited by slashes ("/"). Any text within and including a pair of slashes is considered a comment."
- (Appendix G.6) "Comments are considered whitespace. Hence, they are allowed in prefixed byte strings; for instance, the following are equivalent:"
- (Appendix G.6) "(There are currently no end-of-line comments. If we want to add them, "//" sounds like a reasonable delimiter given that we already use slashes for comments, but we could also go, for example, for "#".)"

---

## Appendix H. Examples

- (Appendix H) "This appendix is for information only."

Informative. The reputon example and its generated instance are fixtures in this
record's `distilled/examples/`. Appendix H contains the document's second BCP 14
keyword occurrence, and it is a **quotation of RFC 7071**, not an obligation
RFC 8610 asserts:

- (Appendix H) "Also, this definition makes it clear that several ext-values are allowed (by definition with different member names); RFC 7071 could be read to forbid the repetition of ext-value ("A specific reputon-element MUST NOT appear more than once" is ambiguous)."

---

## Dropped

Abstract, Status of This Memo, Copyright Notice, Table of Contents, §1's
document-structure paragraph beyond the sentences quoted, §7 References,
Acknowledgements, Contributors, Authors' Addresses. Figures reproduced in the
schema and examples artifacts are cited above by locator rather than duplicated.
