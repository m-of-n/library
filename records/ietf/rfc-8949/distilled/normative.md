---
record: rfc-8949
kind: normative
title: "rfc-8949 — normative statements"
extracted: "2026-09-30"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 8949 (STD 94), "Concise Binary Object Representation (CBOR)",
December 2020. Quotations are verbatim from the plain-text RFC. Blocks that
reproduce tables, lists, structures, or pseudocode preserve the source's own
line breaks and indentation inside fenced blocks.

## §1. Introduction

### §1.2 Terminology

- (§1.2) "The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here."
- (§1.2) "The term "byte" is used in its now-customary sense as a synonym for "octet"."
- (§1.2) "All multi-byte values are encoded in network byte order (that is, most significant byte first, also known as "big-endian")."
- (§1.2) "Data item:  A single piece of CBOR data.  The structure of a data item may contain zero, one, or more nested data items.  The term is used both for the data item in representation format and for the abstract idea that can be derived from that by a decoder; the former can be addressed specifically by using the term "encoded data item"."
- (§1.2) "Decoder:  A process that decodes a well-formed encoded CBOR data item and makes it available to an application.  Formally speaking, a decoder contains a parser to break up the input using the syntax rules of CBOR, as well as a semantic processor to prepare the data in a form suitable to the application."
- (§1.2) "Encoder:  A process that generates the (well-formed) representation format of a CBOR data item from application information."
- (§1.2) "Data Stream:  A sequence of zero or more data items, not further assembled into a larger containing data item (see [RFC8742] for one application).  The independent data items that make up a data stream are sometimes also referred to as "top-level data items"."
- (§1.2) "Well-formed:  A data item that follows the syntactic structure of CBOR.  A well-formed data item uses the initial bytes and the byte strings and/or data items that are implied by their values as defined in CBOR and does not include following extraneous data.  CBOR decoders by definition only return contents from well-formed data items."
- (§1.2) "Valid:  A data item that is well-formed and also follows the semantic restrictions that apply to CBOR data items (Section 5.3)."
- (§1.2) "Expected:  Besides its normal English meaning, the term "expected" is used to describe requirements beyond CBOR validity that an application has on its input data.  Well-formed (processable at all), valid (checked by a validity-checking generic decoder), and expected (checked by the application) form a hierarchy of layers of acceptability."
- (§1.2) "Stream decoder:  A process that decodes a data stream and makes each of the data items in the sequence available to an application as they are received."
- (§1.2) "Terms and concepts for floating-point values such as Infinity, NaN (not a number), negative zero, and subnormal are defined in [IEEE754]."
- (§1.2) "Where bit arithmetic or data types are explained, this document uses the notation familiar from the programming language C [C], except that ".." denotes a range that includes both ends given, and superscript notation denotes exponentiation.  For example, 2 to the power of 64 is notated: 2^(64).  In the plain-text version of this specification, superscript notation is not available and therefore is rendered by a surrogate notation.  That notation is not optimized for this RFC; it is unfortunately ambiguous with C's exclusive-or (which is only used in the appendices, which in turn do not use exponentiation) and requires circumspection from the reader of the plain-text version."
- (§1.2) "Examples and pseudocode assume that signed integers use two's complement representation and that right shifts of signed integers perform sign extension; these assumptions are also specified in Sections 6.8.1 (basic.fundamental) and 7.6.7 (expr.shift) of the 2020 version of C++ (currently available as a final draft, [Cplusplus20])."
- (§1.2) "Similar to the "0x" notation for hexadecimal numbers, numbers in binary notation are prefixed with "0b".  Underscores can be added to a number solely for readability, so 0b00100001 (0x21) might be written 0b001_00001 to emphasize the desired interpretation of the bits in the byte; in this case, it is split into three bits and five bits.  Encoded CBOR data items are sometimes given in the "0x" or "0b" notation; these values are first interpreted as numbers as in C and are then interpreted as byte strings in network byte order, including any leading zero bytes expressed in the notation."
- (§1.2) "Words may be _italicized_ for emphasis; in the plain text form of this specification, this is indicated by surrounding words with underscore characters.  Verbatim text (e.g., names from a programming language) may be set in "monospace" type; in plain text, this is approximated somewhat ambiguously by surrounding the text in double quotes (which also retain their usual meaning)."

## §2. CBOR Data Models

- (§2) "In the basic (unextended) generic data model defined in Section 3, a data item is one of the following:"

```text
   *  an integer in the range -2^(64)..2^(64)-1 inclusive

   *  a simple value, identified by a number between 0 and 255, but
      distinct from that number itself

   *  a floating-point value, distinct from an integer, out of the set
      representable by IEEE 754 binary64 (including non-finites)
      [IEEE754]

   *  a sequence of zero or more bytes ("byte string")

   *  a sequence of zero or more Unicode code points ("text string")

   *  a sequence of zero or more data items ("array")

   *  a mapping (mathematical function) from zero or more data items
      ("keys") each to a data item ("values"), ("map")

   *  a tagged data item ("tag"), comprising a tag number (an integer in
      the range 0..2^(64)-1) and the tag content (a data item)
```

- (§2) "Note that integer and floating-point values are distinct in this model, even if they have the same numeric value."
- (§2) "Also note that serialization variants are not visible at the generic data model level.  This deliberate absence of visibility includes the number of bytes of the encoded floating-point value.  It also includes the choice of encoding for an "argument" (see Section 3) such as the encoding for an integer, the encoding for the length of a text or byte string, the encoding for the number of elements in an array or pairs in a map, or the encoding for a tag number."

### §2.1 Extended Generic Data Models

- (§2.1) "In other words, the basic generic data model is stable as defined in this document, while the extended generic data model expands by the registration of new simple values or tag numbers, but never shrinks."
- (§2.1) "While there is a strong expectation that generic encoders and decoders can represent "false", "true", and "null" ("undefined" is intentionally omitted) in the form appropriate for their programming environment, the implementation of the data model extensions created by tags is truly optional and a matter of implementation quality."

### §2.2 Specific Data Models

- (§2.2) "When documenting such specific data models and specifying the types of data items, it is preferable to identify the types by their generic data model names ("negative integer", "array") instead of referring to aspects of their CBOR representation ("major type 1", "major type 4")."
- (§2.2) "Specific data models can also specify value equivalency (including values of different types) for the purposes of map keys and encoder freedom.  For example, in the generic data model, a valid map MAY have both "0" and "0.0" as keys, and an encoder MUST NOT encode "0.0" as an integer (major type 0, Section 3.1)."
- (§2.2) "However, if a specific data model declares that floating-point and integer representations of integral values are equivalent, using both map keys "0" and "0.0" in a single map would be considered duplicates, even while encoded as different major types, and so invalid; and an encoder could encode integral-valued floats as integers or vice versa, perhaps to save encoded bytes."

## §3. Specification of the CBOR Encoding

- (§3) "A CBOR data item (Section 2) is encoded to or decoded from a byte string carrying a well-formed encoded data item as described in this section."
- (§3) "An encoder MUST produce only well-formed encoded data items."
- (§3) "A decoder MUST NOT return a decoded data item when it encounters input that is not a well-formed encoded CBOR data item (this does not detract from the usefulness of diagnostic and recovery tools that might make available some information from a damaged encoded CBOR data item)."
- (§3) "The initial byte of each encoded data item contains both information about the major type (the high-order 3 bits, described in Section 3.1) and additional information (the low-order 5 bits).  With a few exceptions, the additional information's value describes how to load an unsigned integer "argument":"

Additional-information / argument rules (§3), verbatim:

```text
   Less than 24:  The argument's value is the value of the additional
      information.

   24, 25, 26, or 27:  The argument's value is held in the following 1,
      2, 4, or 8 bytes, respectively, in network byte order.  For major
      type 7 and additional information value 25, 26, 27, these bytes
      are not used as an integer argument, but as a floating-point value
      (see Section 3.3).

   28, 29, 30:  These values are reserved for future additions to the
      CBOR format.  In the present version of CBOR, the encoded item is
      not well-formed.

   31:  No argument value is derived.  If the major type is 0, 1, or 6,
      the encoded item is not well-formed.  For major types 2 to 5, the
      item's length is indefinite, and for major type 7, the byte does
      not constitute a data item at all but terminates an indefinite-
      length item; all are described in Section 3.2.
```

- (§3) "The initial byte and any additional bytes consumed to construct the argument are collectively referred to as the _head_ of the data item."
- (§3) "The meaning of this argument depends on the major type.  For example, in major type 0, the argument is the value of the data item itself (and in major type 1, the value of the data item is computed from the argument); in major type 2 and 3, it gives the length of the string data in bytes that follow; and in major types 4 and 5, it is used to determine the number of data items enclosed."
- (§3) "If the encoded sequence of bytes ends before the end of a data item, that item is not well-formed."
- (§3) "If the encoded sequence of bytes still has bytes remaining after the outermost encoded item is decoded, that encoding is not a single well-formed CBOR item."
- (§3) "Depending on the application, the decoder may either treat the encoding as not well-formed or just identify the start of the remaining bytes to the application."

### §3.1 Major Types

- (§3.1) "The following lists the major types and the additional information and other bytes associated with the type."

```text
   Major type 0:
      An unsigned integer in the range 0..2^(64)-1 inclusive.  The value
      of the encoded item is the argument itself.  For example, the
      integer 10 is denoted as the one byte 0b000_01010 (major type 0,
      additional information 10).  The integer 500 would be 0b000_11001
      (major type 0, additional information 25) followed by the two
      bytes 0x01f4, which is 500 in decimal.

   Major type 1:
      A negative integer in the range -2^(64)..-1 inclusive.  The value
      of the item is -1 minus the argument.  For example, the integer
      -500 would be 0b001_11001 (major type 1, additional information
      25) followed by the two bytes 0x01f3, which is 499 in decimal.

   Major type 2:
      A byte string.  The number of bytes in the string is equal to the
      argument.  For example, a byte string whose length is 5 would have
      an initial byte of 0b010_00101 (major type 2, additional
      information 5 for the length), followed by 5 bytes of binary
      content.  A byte string whose length is 500 would have 3 initial
      bytes of 0b010_11001 (major type 2, additional information 25 to
      indicate a two-byte length) followed by the two bytes 0x01f4 for a
      length of 500, followed by 500 bytes of binary content.

   Major type 3:
      A text string (Section 2) encoded as UTF-8 [RFC3629].  The number
      of bytes in the string is equal to the argument.  A string
      containing an invalid UTF-8 sequence is well-formed but invalid
      (Section 1.2).  This type is provided for systems that need to
      interpret or display human-readable text, and allows the
      differentiation between unstructured bytes and text that has a
      specified repertoire (that of Unicode) and encoding (UTF-8).  In
      contrast to formats such as JSON, the Unicode characters in this
      type are never escaped.  Thus, a newline character (U+000A) is
      always represented in a string as the byte 0x0a, and never as the
      bytes 0x5c6e (the characters "\" and "n") nor as 0x5c7530303061
      (the characters "\", "u", "0", "0", "0", and "a").

   Major type 4:
      An array of data items.  In other formats, arrays are also called
      lists, sequences, or tuples (a "CBOR sequence" is something
      slightly different, though [RFC8742]).  The argument is the number
      of data items in the array.  Items in an array do not need to all
      be of the same type.  For example, an array that contains 10 items
      of any type would have an initial byte of 0b100_01010 (major type
      4, additional information 10 for the length) followed by the 10
      remaining items.

   Major type 5:
      A map of pairs of data items.  Maps are also called tables,
      dictionaries, hashes, or objects (in JSON).  A map is comprised of
      pairs of data items, each pair consisting of a key that is
      immediately followed by a value.  The argument is the number of
      _pairs_ of data items in the map.  For example, a map that
      contains 9 pairs would have an initial byte of 0b101_01001 (major
      type 5, additional information 9 for the number of pairs) followed
      by the 18 remaining items.  The first item is the first key, the
      second item is the first value, the third item is the second key,
      and so on.  Because items in a map come in pairs, their total
      number is always even: a map that contains an odd number of items
      (no value data present after the last key data item) is not well-
      formed.  A map that has duplicate keys may be well-formed, but it
      is not valid, and thus it causes indeterminate decoding; see also
      Section 5.6.

   Major type 6:
      A tagged data item ("tag") whose tag number, an integer in the
      range 0..2^(64)-1 inclusive, is the argument and whose enclosed
      data item (_tag content_) is the single encoded data item that
      follows the head.  See Section 3.4.

   Major type 7:
      Floating-point numbers and simple values, as well as the "break"
      stop code.  See Section 3.3.
```

Well-formedness and validity rules stated inside §3.1, called out:

- (§3.1, Major type 3) "A string containing an invalid UTF-8 sequence is well-formed but invalid (Section 1.2)."
- (§3.1, Major type 3) "In contrast to formats such as JSON, the Unicode characters in this type are never escaped.  Thus, a newline character (U+000A) is always represented in a string as the byte 0x0a, and never as the bytes 0x5c6e (the characters "\" and "n") nor as 0x5c7530303061 (the characters "\", "u", "0", "0", "0", and "a")."
- (§3.1, Major type 5) "Because items in a map come in pairs, their total number is always even: a map that contains an odd number of items (no value data present after the last key data item) is not well-formed."
- (§3.1, Major type 5) "A map that has duplicate keys may be well-formed, but it is not valid, and thus it causes indeterminate decoding; see also Section 5.6."
- (§3.1, Major type 6) "A tagged data item ("tag") whose tag number, an integer in the range 0..2^(64)-1 inclusive, is the argument and whose enclosed data item (_tag content_) is the single encoded data item that follows the head."
- (§3.1) "In major types 6 and 7, many of the possible values are reserved for future specification.  See Section 9 for more information on these values."
- (§3.1) "Table 1 summarizes the major types defined by CBOR, ignoring Section 3.2 for now.  The number N in this table stands for the argument."

(Table 1)

```text
     +============+=======================+=========================+
     | Major Type | Meaning               | Content                 |
     +============+=======================+=========================+
     | 0          | unsigned integer N    | -                       |
     +------------+-----------------------+-------------------------+
     | 1          | negative integer -1-N | -                       |
     +------------+-----------------------+-------------------------+
     | 2          | byte string           | N bytes                 |
     +------------+-----------------------+-------------------------+
     | 3          | text string           | N bytes (UTF-8 text)    |
     +------------+-----------------------+-------------------------+
     | 4          | array                 | N data items (elements) |
     +------------+-----------------------+-------------------------+
     | 5          | map                   | 2N data items (key/     |
     |            |                       | value pairs)            |
     +------------+-----------------------+-------------------------+
     | 6          | tag of number N       | 1 data item             |
     +------------+-----------------------+-------------------------+
     | 7          | simple/float          | -                       |
     +------------+-----------------------+-------------------------+

       Table 1: Overview over the Definite-Length Use of CBOR Major
                           Types (N = Argument)
```

### §3.2 Indefinite Lengths for Some Major Types

- (§3.2) "Four CBOR items (arrays, maps, byte strings, and text strings) can be encoded with an indefinite length using additional information value 31."
- (§3.2) "Indefinite-length arrays and maps are dealt with differently than indefinite-length strings (byte strings and text strings)."

#### §3.2.1 The "break" Stop Code

- (§3.2.1) "The "break" stop code is encoded with major type 7 and additional information value 31 (0b111_11111).  It is not itself a data item: it is just a syntactic feature to close an indefinite-length item."
- (§3.2.1) "If the "break" stop code appears where a data item is expected, other than directly inside an indefinite-length string, array, or map -- for example, directly inside a definite-length array or map -- the enclosing item is not well-formed."

#### §3.2.2 Indefinite-Length Arrays and Maps

- (§3.2.2) "Indefinite-length arrays and maps are represented using their major type with the additional information value of 31, followed by an arbitrary-length sequence of zero or more items for an array or key/value pairs for a map, followed by the "break" stop code (Section 3.2.1)."
- (§3.2.2) "In other words, indefinite-length arrays and maps look identical to other arrays and maps except for beginning with the additional information value of 31 and ending with the "break" stop code."
- (§3.2.2) "If the "break" stop code appears after a key in a map, in place of that key's value, the map is not well-formed."
- (§3.2.2) "There is no restriction against nesting indefinite-length array or map items.  A "break" only terminates a single item, so nested indefinite-length items need exactly as many "break" stop codes as there are type bytes starting an indefinite-length item."

#### §3.2.3 Indefinite-Length Byte Strings and Text Strings

- (§3.2.3) "Indefinite-length strings are represented by a byte containing the major type for byte string or text string with an additional information value of 31, followed by a series of zero or more strings of the specified type ("chunks") that have definite lengths, and finished by the "break" stop code (Section 3.2.1)."
- (§3.2.3) "The data item represented by the indefinite-length string is the concatenation of the chunks.  If no chunks are present, the data item is an empty string of the specified type.  Zero-length chunks, while not particularly useful, are permitted."
- (§3.2.3) "If any item between the indefinite-length string indicator (0b010_11111 or 0b011_11111) and the "break" stop code is not a definite-length string item of the same major type, the string is not well-formed."
- (§3.2.3) "The design does not allow nesting indefinite-length strings as chunks into indefinite-length strings."
- (§3.2.3) "If any definite-length text string inside an indefinite-length text string is invalid, the indefinite-length text string is invalid.  Note that this implies that the UTF-8 bytes of a single Unicode code point (scalar value) cannot be spread between chunks: a new chunk of a text string can only be started at a code point boundary."

#### §3.2.4 Summary of Indefinite-Length Use of Major Types

- (§3.2.4) "Table 2 summarizes the major types defined by CBOR as used for indefinite-length encoding (with additional information set to 31)."

(Table 2)

```text
   +============+===================+==================================+
   | Major Type | Meaning           | Enclosed up to "break" Stop Code |
   +============+===================+==================================+
   | 0          | (not well-        | -                                |
   |            | formed)           |                                  |
   +------------+-------------------+----------------------------------+
   | 1          | (not well-        | -                                |
   |            | formed)           |                                  |
   +------------+-------------------+----------------------------------+
   | 2          | byte string       | definite-length byte strings     |
   +------------+-------------------+----------------------------------+
   | 3          | text string       | definite-length text strings     |
   +------------+-------------------+----------------------------------+
   | 4          | array             | data items (elements)            |
   +------------+-------------------+----------------------------------+
   | 5          | map               | data items (key/value pairs)     |
   +------------+-------------------+----------------------------------+
   | 6          | (not well-        | -                                |
   |            | formed)           |                                  |
   +------------+-------------------+----------------------------------+
   | 7          | "break" stop      | -                                |
   |            | code              |                                  |
   +------------+-------------------+----------------------------------+

        Table 2: Overview of the Indefinite-Length Use of CBOR Major
                    Types (Additional Information = 31)
```

### §3.3 Floating-Point Numbers and Values with No Content

- (§3.3) "Major type 7 is for two types of data: floating-point numbers and "simple values" that do not need any content.  Each value of the 5-bit additional information in the initial byte has its own separate meaning, as defined in Table 3.  Like the major types for integers, items of this major type do not carry content data; all the information is in the initial bytes (the head)."

(Table 3)

```text
    +=============+===================================================+
    | 5-Bit Value | Semantics                                         |
    +=============+===================================================+
    | 0..23       | Simple value (value 0..23)                        |
    +-------------+---------------------------------------------------+
    | 24          | Simple value (value 32..255 in following byte)    |
    +-------------+---------------------------------------------------+
    | 25          | IEEE 754 Half-Precision Float (16 bits follow)    |
    +-------------+---------------------------------------------------+
    | 26          | IEEE 754 Single-Precision Float (32 bits follow)  |
    +-------------+---------------------------------------------------+
    | 27          | IEEE 754 Double-Precision Float (64 bits follow)  |
    +-------------+---------------------------------------------------+
    | 28-30       | Reserved, not well-formed in the present document |
    +-------------+---------------------------------------------------+
    | 31          | "break" stop code for indefinite-length items     |
    |             | (Section 3.2.1)                                   |
    +-------------+---------------------------------------------------+

         Table 3: Values for Additional Information in Major Type 7
```

- (§3.3) "As with all other major types, the 5-bit value 24 signifies a single-byte extension: it is followed by an additional byte to represent the simple value.  (To minimize confusion, only the values 32 to 255 are used.)  This maintains the structure of the initial bytes: as for the other major types, the length of these always depends on the additional information in the first byte.  Table 4 lists the numeric values assigned and available for simple values."

(Table 4)

```text
                        +=========+==============+
                        | Value   | Semantics    |
                        +=========+==============+
                        | 0..19   | (unassigned) |
                        +---------+--------------+
                        | 20      | false        |
                        +---------+--------------+
                        | 21      | true         |
                        +---------+--------------+
                        | 22      | null         |
                        +---------+--------------+
                        | 23      | undefined    |
                        +---------+--------------+
                        | 24..31  | (reserved)   |
                        +---------+--------------+
                        | 32..255 | (unassigned) |
                        +---------+--------------+

                          Table 4: Simple Values
```

- (§3.3) "An encoder MUST NOT issue two-byte sequences that start with 0xf8 (major type 7, additional information 24) and continue with a byte less than 0x20 (32 decimal).  Such sequences are not well-formed.  (This implies that an encoder cannot encode "false", "true", "null", or "undefined" in two-byte sequences and that only the one-byte variants of these are well-formed; more generally speaking, each simple value only has a single representation variant)."
- (§3.3) "The 5-bit values of 25, 26, and 27 are for 16-bit, 32-bit, and 64-bit IEEE 754 binary floating-point values [IEEE754].  These floating-point values are encoded in the additional bytes of the appropriate size."

### §3.4 Tagging of Items

- (§3.4) "In CBOR, a data item can be enclosed by a tag to give it some additional semantics, as uniquely identified by a _tag number_. The tag is major type 6, its argument (Section 3) indicates the tag number, and it contains a single enclosed data item, the _tag content_. (If a tag requires further structure to its content, this structure is provided by the enclosed data item.)  We use the term _tag_ for the entire data item consisting of both a tag number and the tag content: the tag content is the data item that is being tagged."
- (§3.4) "In the extended generic data model, a tag number's definition describes the additional semantics conveyed with the tag number.  These semantics may include equivalence of some tagged data items with other data items, including some that can be represented in the basic generic data model."
- (§3.4) "The tag definition may specify a preferred serialization (Section 4.1) that is recommended for generic encoders; this may prefer basic generic data model representations over ones that employ a tag."
- (§3.4) "The tag definition usually defines which nested data items are valid for such tags.  Tag definitions may restrict their content to a very specific syntactic structure, as the tags defined in this document do, or they may define their content more semantically."
- (§3.4) "As a matter of convention, many tags do not accept "null" or "undefined" values as tag content; instead, the expectation is that a "null" or "undefined" value can be used in place of the entire tag; Section 3.4.2 provides some further considerations for one specific tag about the handling of this convention in application protocols and in mapping to platform types."
- (§3.4) "Decoders do not need to understand tags of every tag number, and tags may be of little value in applications where the implementation creating a particular CBOR data item and the implementation decoding that stream know the semantic meaning of each item in the data flow."
- (§3.4) "Understanding the semantics of tags is optional for a decoder; it can simply present both the tag number and the tag content to the application, without interpreting the additional semantics of the tag."
- (§3.4) "A tag applies semantics to the data item it encloses.  Tags can nest: if tag A encloses tag B, which encloses data item C, tag A applies to the result of applying tag B on data item C."
- (§3.4) "IANA maintains a registry of tag numbers as described in Section 9.2.  Table 5 provides a list of tag numbers that were defined in [RFC7049] with definitions in the rest of this section."

(Table 5)

```text
        +=======+=============+==================================+
        | Tag   | Data Item   | Semantics                        |
        +=======+=============+==================================+
        | 0     | text string | Standard date/time string; see   |
        |       |             | Section 3.4.1                    |
        +-------+-------------+----------------------------------+
        | 1     | integer or  | Epoch-based date/time; see       |
        |       | float       | Section 3.4.2                    |
        +-------+-------------+----------------------------------+
        | 2     | byte string | Unsigned bignum; see             |
        |       |             | Section 3.4.3                    |
        +-------+-------------+----------------------------------+
        | 3     | byte string | Negative bignum; see             |
        |       |             | Section 3.4.3                    |
        +-------+-------------+----------------------------------+
        | 4     | array       | Decimal fraction; see            |
        |       |             | Section 3.4.4                    |
        +-------+-------------+----------------------------------+
        | 5     | array       | Bigfloat; see Section 3.4.4      |
        +-------+-------------+----------------------------------+
        | 21    | (any)       | Expected conversion to base64url |
        |       |             | encoding; see Section 3.4.5.2    |
        +-------+-------------+----------------------------------+
        | 22    | (any)       | Expected conversion to base64    |
        |       |             | encoding; see Section 3.4.5.2    |
        +-------+-------------+----------------------------------+
        | 23    | (any)       | Expected conversion to base16    |
        |       |             | encoding; see Section 3.4.5.2    |
        +-------+-------------+----------------------------------+
        | 24    | byte string | Encoded CBOR data item; see      |
        |       |             | Section 3.4.5.1                  |
        +-------+-------------+----------------------------------+
        | 32    | text string | URI; see Section 3.4.5.3         |
        +-------+-------------+----------------------------------+
        | 33    | text string | base64url; see Section 3.4.5.3   |
        +-------+-------------+----------------------------------+
        | 34    | text string | base64; see Section 3.4.5.3      |
        +-------+-------------+----------------------------------+
        | 36    | text string | MIME message; see                |
        |       |             | Section 3.4.5.3                  |
        +-------+-------------+----------------------------------+
        | 55799 | (any)       | Self-described CBOR; see         |
        |       |             | Section 3.4.6                    |
        +-------+-------------+----------------------------------+

                 Table 5: Tag Numbers Defined in RFC 7049
```

- (§3.4) "Conceptually, tags are interpreted in the generic data model, not at (de-)serialization time."
- (§3.4) "A small number of tags (at this time, tag number 25 and tag number 29 [IANA.cbor-tags]) have been registered with semantics that may require processing at (de-)serialization time: the decoder needs to be aware of, and the encoder needs to be in control of, the exact sequence in which data items are encoded into the CBOR data item."
- (§3.4) "The definition of new tags with this property is NOT RECOMMENDED."
- (§3.4) "IANA allocated tag numbers 65535, 4294967295, and 18446744073709551615 (binary all-ones in 16-bit, 32-bit, and 64-bit).  These can be used as a convenience for implementers who want a single-integer data structure to indicate either the presence of a specific tag or absence of a tag.  That allocation is described in Section 10 of [CBOR-TAGS].  These tags are not intended to occur in actual CBOR data items; implementations MAY flag such an occurrence as an error."
- (§3.4) "Protocols can extend the generic data model (Section 2) with data items representing points in time by using tag numbers 0 and 1, with arbitrarily sized integers by using tag numbers 2 and 3, and with floating-point values of arbitrary size and precision by using tag numbers 4 and 5."

#### §3.4.1 Standard Date/Time String

- (§3.4.1) "Tag number 0 contains a text string in the standard format described by the "date-time" production in [RFC3339], as refined by Section 3.3 of [RFC4287], representing the point in time described there.  A nested item of another type or a text string that doesn't match the format described in [RFC4287] is invalid."

#### §3.4.2 Epoch-Based Date/Time

- (§3.4.2) "Tag number 1 contains a numerical value counting the number of seconds from 1970-01-01T00:00Z in UTC time to the represented point in civil time."
- (§3.4.2) "The tag content MUST be an unsigned or negative integer (major types 0 and 1) or a floating-point number (major type 7 with additional information 25, 26, or 27).  Other contained types are invalid."
- (§3.4.2) "Nonnegative values (major type 0 and nonnegative floating-point numbers) stand for time values on or after 1970-01-01T00:00Z UTC and are interpreted according to POSIX [TIME_T]."
- (§3.4.2) "Note that applications that require the expression of times beyond early 2106 cannot leave out support of 64-bit integers for the tag content."
- (§3.4.2) "Negative values (major type 1 and negative floating-point numbers) are interpreted as determined by the application requirements as there is no universal standard for UTC count-of-seconds time before 1970-01-01T00:00Z (this is particularly true for points in time that precede discontinuities in national calendars).  The same applies to non-finite values."
- (§3.4.2) "To indicate fractional seconds, floating-point values can be used within tag number 1 instead of integer values."
- (§3.4.2) "An application that requires tag number 1 support may restrict the tag content to be an integer (or a floating-point value) only."

#### §3.4.3 Bignums

- (§3.4.3) "Protocols using tag numbers 2 and 3 extend the generic data model (Section 2) with "bignums" representing arbitrarily sized integers.  In the basic generic data model, bignum values are not equal to integers from the same model, but the extended generic data model created by this tag definition defines equivalence based on numeric value, and preferred serialization (Section 4.1) never makes use of bignums that also can be expressed as basic integers (see below)."
- (§3.4.3) "Bignums are encoded as a byte string data item, which is interpreted as an unsigned integer n in network byte order.  Contained items of other types are invalid.  For tag number 2, the value of the bignum is n.  For tag number 3, the value of the bignum is -1 - n."
- (§3.4.3) "The preferred serialization of the byte string is to leave out any leading zeroes (note that this means the preferred serialization for n = 0 is the empty byte string, but see below)."
- (§3.4.3) "Decoders that understand these tags MUST be able to decode bignums that do have leading zeroes."
- (§3.4.3) "The preferred serialization of an integer that can be represented using major type 0 or 1 is to encode it this way instead of as a bignum (which means that the empty string never occurs in a bignum when using preferred serialization)."
- (§3.4.3) "Note that this means the non-preferred choice of a bignum representation instead of a basic integer for encoding a number is not intended to have application semantics (just as the choice of a longer basic integer representation than needed, such as 0x1800 for 0x00, does not)."

#### §3.4.4 Decimal Fractions and Bigfloats

- (§3.4.4) "Protocols using tag number 4 extend the generic data model with data items representing arbitrary-length decimal fractions of the form m*(10^(e)).  Protocols using tag number 5 extend the generic data model with data items representing arbitrary-length binary fractions of the form m*(2^(e)).  As with bignums, values of different types are not equal in the generic data model."
- (§3.4.4) "A decimal fraction or a bigfloat is represented as a tagged array that contains exactly two integer numbers: an exponent e and a mantissa m.  Decimal fractions (tag number 4) use base-10 exponents; the value of a decimal fraction data item is m*(10^(e)).  Bigfloats (tag number 5) use base-2 exponents; the value of a bigfloat data item is m*(2^(e)).  The exponent e MUST be represented in an integer of major type 0 or 1, while the mantissa can also be a bignum (Section 3.4.3).  Contained items with other structures are invalid."
- (§3.4.4) "Decimal fractions and bigfloats provide no representation of Infinity, -Infinity, or NaN; if these are needed in place of a decimal fraction or bigfloat, the IEEE 754 half-precision representations from Section 3.3 can be used."

#### §3.4.5 Content Hints

- (§3.4.5) "The tags in this section are for content hints that might be used by generic CBOR processors.  These content hints do not extend the generic data model."

##### §3.4.5.1 Encoded CBOR Data Item

- (§3.4.5.1) "Tag number 24 (CBOR data item) can be used to tag the embedded byte string as a single data item encoded in CBOR format.  Contained items that aren't byte strings are invalid.  A contained byte string is valid if it encodes a well-formed CBOR data item; validity checking of the decoded CBOR item is not required for tag validity (but could be offered by a generic decoder as a special option)."

##### §3.4.5.2 Expected Later Encoding for CBOR-to-JSON Converters

- (§3.4.5.2) "Tag numbers 21 to 23 indicate that a byte string might require a specific encoding when interoperating with a text-based representation."
- (§3.4.5.2) "The data item tagged can be a byte string or any other data item.  In the latter case, the tag applies to all of the byte string data items contained in the data item, except for those contained in a nested data item tagged with an expected conversion."
- (§3.4.5.2) "These three tag numbers suggest conversions to three of the base data encodings defined in [RFC4648].  Tag number 21 suggests conversion to base64url encoding (Section 5 of [RFC4648]) where padding is not used (see Section 3.2 of [RFC4648]); that is, all trailing equals signs ("=") are removed from the encoded string.  Tag number 22 suggests conversion to classical base64 encoding (Section 4 of [RFC4648]) with padding as defined in RFC 4648.  For both base64url and base64, padding bits are set to zero (see Section 3.5 of [RFC4648]), and the conversion to alternate encoding is performed on the contents of the byte string (that is, without adding any line breaks, whitespace, or other additional characters).  Tag number 23 suggests conversion to base16 (hex) encoding with uppercase alphabetics (see Section 8 of [RFC4648]).  Note that, for all three tag numbers, the encoding of the empty byte string is the empty text string."

##### §3.4.5.3 Encoded Text

Tag validity rules for tag numbers 32, 33, 34, and 36 (§3.4.5.3), verbatim:

```text
   *  Tag number 32 is for URIs, as defined in [RFC3986].  If the text
      string doesn't match the "URI-reference" production, the string is
      invalid.

   *  Tag numbers 33 and 34 are for base64url- and base64-encoded text
      strings, respectively, as defined in [RFC4648].  If any of the
      following apply:

      -  the encoded text string contains non-alphabet characters or
         only 1 alphabet character in the last block of 4 (where
         alphabet is defined by Section 5 of [RFC4648] for tag number 33
         and Section 4 of [RFC4648] for tag number 34), or

      -  the padding bits in a 2- or 3-character block are not 0, or

      -  the base64 encoding has the wrong number of padding characters,
         or

      -  the base64url encoding has padding characters,

      the string is invalid.

   *  Tag number 36 is for MIME messages (including all headers), as
      defined in [RFC2045].  A text string that isn't a valid MIME
      message is invalid.  (For this tag, validity checking may be
      particularly onerous for a generic decoder and might therefore not
      be offered.  Note that many MIME messages are general binary data
      and therefore cannot be represented in a text string;
      [IANA.cbor-tags] lists a registration for tag number 257 that is
      similar to tag number 36 but uses a byte string as its tag
      content.)
```

- (§3.4.5.3) "Note that tag numbers 33 and 34 differ from 21 and 22 in that the data is transported in base-encoded form for the former and in raw byte string form for the latter."
- (§3.4.5.3) "Instead, this tag remains available (as registered in [RFC7049]) for applications that specify the particular regular expression variant they use out-of-band (possibly by limiting the usage to a defined common subset of both PCRE and ECMA262).  As this specification clarifies tag validity beyond [RFC7049], we note that due to the open way the tag was defined in [RFC7049], any contained string value needs to be valid at the CBOR tag level (but then may not be "expected" at the application level)."

#### §3.4.6 Self-Described CBOR

- (§3.4.6) "Tag number 55799 is defined for this purpose, specifically for use at the start of a stored encoded CBOR data item as specified by an application.  It does not impart any special semantics on the data item that it encloses; that is, the semantics of the tag content enclosed in tag number 55799 is exactly identical to the semantics of the tag content itself."
- (§3.4.6) "The serialization of this tag's head is 0xd9d9f7, which does not appear to be in use as a distinguishing mark for any frequently used file types.  In particular, 0xd9d9f7 is not a valid start of a Unicode text in any Unicode encoding if it is followed by a valid CBOR data item."

## §4. Serialization Considerations

### §4.1 Preferred Serialization

- (§4.1) "For some values at the data model level, CBOR provides multiple serializations.  For many applications, it is desirable that an encoder always chooses a preferred serialization (preferred encoding); however, the present specification does not put the burden of enforcing this preference on either the encoder or decoder."
- (§4.1) "Full implementations of CBOR decoders are by definition variation tolerant; the distinction is only relevant if a constrained implementation of a CBOR decoder meets a variant encoder."
- (§4.1) "The preferred serialization always uses the shortest form of representing the argument (Section 3); it also uses the shortest floating-point encoding that preserves the value being encoded."
- (§4.1) "The preferred serialization for a floating-point value is the shortest floating-point encoding that preserves its value, e.g., 0xf94580 for the number 5.5, and 0xfa45ad9c00 for the number 5555.5.  For NaN values, a shorter encoding is preferred if zero-padding the shorter significand towards the right reconstitutes the original NaN value (for many applications, the single NaN encoding 0xf97e00 will suffice)."
- (§4.1) "Definite-length encoding is preferred whenever the length is known at the time the serialization of the item starts."

### §4.2 Deterministically Encoded CBOR

- (§4.2) "Some protocols may want encoders to only emit CBOR in a particular deterministic format; those protocols might also have the decoders check that their input is in that deterministic format.  Those protocols are free to define what they mean by a "deterministic format" and what encoders and decoders are expected to do.  This section defines a set of restrictions that can serve as the base of such a deterministic format."

#### §4.2.1 Core Deterministic Encoding Requirements

Complete and verbatim (§4.2.1):

```text
   A CBOR encoding satisfies the "core deterministic encoding
   requirements" if it satisfies the following restrictions:

   *  Preferred serialization MUST be used.  In particular, this means
      that arguments (see Section 3) for integers, lengths in major
      types 2 through 5, and tags MUST be as short as possible, for
      instance:

      -  0 to 23 and -1 to -24 MUST be expressed in the same byte as the
         major type;

      -  24 to 255 and -25 to -256 MUST be expressed only with an
         additional uint8_t;

      -  256 to 65535 and -257 to -65536 MUST be expressed only with an
         additional uint16_t;

      -  65536 to 4294967295 and -65537 to -4294967296 MUST be expressed
         only with an additional uint32_t.

      Floating-point values also MUST use the shortest form that
      preserves the value, e.g., 1.5 is encoded as 0xf93e00 (binary16)
      and 1000000.5 as 0xfa49742408 (binary32).  (One implementation of
      this is to have all floats start as a 64-bit float, then do a test
      conversion to a 32-bit float; if the result is the same numeric
      value, use the shorter form and repeat the process with a test
      conversion to a 16-bit float.  This also works to select 16-bit
      float for positive and negative Infinity as well.)

   *  Indefinite-length items MUST NOT appear.  They can be encoded as
      definite-length items instead.

   *  The keys in every map MUST be sorted in the bytewise lexicographic
      order of their deterministic encodings.  For example, the
      following keys are sorted correctly:

      1.  10, encoded as 0x0a.

      2.  100, encoded as 0x1864.

      3.  -1, encoded as 0x20.

      4.  "z", encoded as 0x617a.

      5.  "aa", encoded as 0x626161.

      6.  [100], encoded as 0x811864.

      7.  [-1], encoded as 0x8120.

      8.  false, encoded as 0xf4.

      |  Implementation note: the self-delimiting nature of the CBOR
      |  encoding means that there are no two well-formed CBOR encoded
      |  data items where one is a prefix of the other.  The bytewise
      |  lexicographic comparison of deterministic encodings of
      |  different map keys therefore always ends in a position where
      |  the byte differs between the keys, before the end of a key is
      |  reached.
```

#### §4.2.2 Additional Deterministic Encoding Considerations

Complete and verbatim (§4.2.2):

```text
   CBOR tags present additional considerations for deterministic
   encoding.  If a CBOR-based protocol were to provide the same
   semantics for the presence and absence of a specific tag (e.g., by
   allowing both tag 1 data items and raw numbers in a date/time
   position, treating the latter as if they were tagged), the
   deterministic format would not allow the presence of the tag, based
   on the "shortest form" principle.  For example, a protocol might give
   encoders the choice of representing a URL as either a text string or,
   using Section 3.4.5.3, tag number 32 containing a text string.  This
   protocol's deterministic encoding needs either to require that the
   tag is present or to require that it is absent, not allow either one.

   In a protocol that does require tags in certain places to obtain
   specific semantics, the tag needs to appear in the deterministic
   format as well.  Deterministic encoding considerations also apply to
   the content of tags.

   If a protocol includes a field that can express integers with an
   absolute value of 2^(64) or larger using tag numbers 2 or 3
   (Section 3.4.3), the protocol's deterministic encoding needs to
   specify whether smaller integers are also expressed using these tags
   or using major types 0 and 1.  Preferred serialization uses the
   latter choice, which is therefore recommended.

   Protocols that include floating-point values, whether represented
   using basic floating-point values (Section 3.3) or using tags (or
   both), may need to define extra requirements on their deterministic
   encodings, such as:

   *  Although IEEE floating-point values can represent both positive
      and negative zero as distinct values, the application might not
      distinguish these and might decide to represent all zero values
      with a positive sign, disallowing negative zero.  (The application
      may also want to restrict the precision of floating-point values
      in such a way that there is never a need to represent 64-bit -- or
      even 32-bit -- floating-point values.)

   *  If a protocol includes a field that can express floating-point
      values, with a specific data model that declares integer and
      floating-point values to be interchangeable, the protocol's
      deterministic encoding needs to specify whether, for example, the
      integer 1.0 is encoded as 0x01 (unsigned integer), 0xf93c00
      (binary16), 0xfa3f800000 (binary32), or 0xfb3ff0000000000000
      (binary64).  Example rules for this are:

      1.  Encode integral values that fit in 64 bits as values from
          major types 0 and 1, and other values as the preferred
          (smallest of 16-, 32-, or 64-bit) floating-point
          representation that accurately represents the value,

      2.  Encode all values as the preferred floating-point
          representation that accurately represents the value, even for
          integral values, or

      3.  Encode all values as 64-bit floating-point representations.

      Rule 1 straddles the boundaries between integers and floating-
      point values, and Rule 3 does not use preferred serialization, so
      Rule 2 may be a good choice in many cases.

   *  If NaN is an allowed value, and there is no intent to support NaN
      payloads or signaling NaNs, the protocol needs to pick a single
      representation, typically 0xf97e00.  If that simple choice is not
      possible, specific attention will be needed for NaN handling.

   *  Subnormal numbers (nonzero numbers with the lowest possible
      exponent of a given IEEE 754 number format) may be flushed to zero
      outputs or be treated as zero inputs in some floating-point
      implementations.  A protocol's deterministic encoding may want to
      specifically accommodate such implementations while creating an
      onus on other implementations by excluding subnormal numbers from
      interchange, interchanging zero instead.

   *  The same number can be represented by different decimal fractions,
      by different bigfloats, and by different forms under other tags
      that may be defined to express numeric values.  Depending on the
      implementation, it may not always be practical to determine
      whether any of these forms (or forms in the basic generic data
      model) are equivalent.  An application protocol that presents
      choices of this kind for the representation format of numbers
      needs to be explicit about how the formats for deterministic
      encoding are to be chosen.
```

#### §4.2.3 Length-First Map Key Ordering

Complete and verbatim (§4.2.3):

```text
   The core deterministic encoding requirements (Section 4.2.1) sort map
   keys in a different order from the one suggested by Section 3.9 of
   [RFC7049] (called "Canonical CBOR" there).  Protocols that need to be
   compatible with the order specified in [RFC7049] can instead be
   specified in terms of this specification's "length-first core
   deterministic encoding requirements":

   A CBOR encoding satisfies the "length-first core deterministic
   encoding requirements" if it satisfies the core deterministic
   encoding requirements except that the keys in every map MUST be
   sorted such that:

   1.  If two keys have different lengths, the shorter one sorts
       earlier;

   2.  If two keys have the same length, the one with the lower value in
       (bytewise) lexical order sorts earlier.

   For example, under the length-first core deterministic encoding
   requirements, the following keys are sorted correctly:

   1.  10, encoded as 0x0a.

   2.  -1, encoded as 0x20.

   3.  false, encoded as 0xf4.

   4.  100, encoded as 0x1864.

   5.  "z", encoded as 0x617a.

   6.  [-1], encoded as 0x8120.

   7.  "aa", encoded as 0x626161.

   8.  [100], encoded as 0x811864.
```

Terminology aside in the same subsection (§4.2.3), verbatim:

```text
      |  Although [RFC7049] used the term "Canonical CBOR" for its form
      |  of requirements on deterministic encoding, this document avoids
      |  this term because "canonicalization" is often associated with
      |  specific uses of deterministic encoding only.  The terms are
      |  essentially interchangeable, however, and the set of core
      |  requirements in this document could also be called "Canonical
      |  CBOR", while the length-first-ordered version of that could be
      |  called "Old Canonical CBOR".
```

## §5. Creating CBOR-Based Protocols

- (§5) "CBOR-based protocols MUST specify how their decoders handle invalid and other unexpected data.  CBOR-based protocols MAY specify that they treat arbitrary valid data as unexpected.  Encoders for CBOR-based protocols MUST produce only valid items, that is, the protocol cannot be designed to make use of invalid items."
- (§5) "An encoder can be capable of encoding as many or as few types of values as is required by the protocol in which it is used; a decoder can be capable of understanding as many or as few types of values as is required by the protocols in which it is used."
- (§5) "The rest of this section discusses some considerations in creating CBOR-based protocols.  With few exceptions, it is advisory only and explicitly excludes any language from BCP 14 [RFC2119] [RFC8174] other than words that could be interpreted as "MAY" in the sense of BCP 14.  The exceptions aim at facilitating interoperability of CBOR-based protocols while making use of a wide variety of both generic and application-specific encoders and decoders."

### §5.1 CBOR in Streaming Applications

- (§5.1) "In a streaming application, a data stream may be composed of a sequence of CBOR data items concatenated back-to-back.  In such an environment, the decoder immediately begins decoding a new data item if data is found after the end of a previous data item."
- (§5.1) "Such an application also MUST have a matching streaming security mechanism, where the desired protection is available for incremental data presented to the application."

### §5.2 Generic Encoders and Decoders

- (§5.2) "A generic CBOR decoder can decode all well-formed encoded CBOR data items and present the data items to an application."
- (§5.2) "Generic CBOR encoders provide an application interface that allows the application to specify any well-formed value to be encoded as a CBOR data item, including simple values and tags unknown to the encoder."
- (§5.2) "Even though CBOR attempts to minimize these cases, not all well-formed CBOR data is valid: for example, the encoded text string "0x62c0ae" does not contain valid UTF-8 (because [RFC3629] requires always using the shortest form) and so is not a valid CBOR item."
- (§5.2) "Also, specific tags may make semantic constraints that may be violated, for instance, by a bignum tag enclosing another tag or by an instance of tag number 0 containing a byte string or containing a text string with contents that do not match the "date-time" production of [RFC3339]."
- (§5.2) "There is no requirement that generic encoders and decoders make unnatural choices for their application interface to enable the processing of invalid data.  Generic encoders and decoders are expected to forward simple values and tags even if their specific codepoints are not registered at the time the encoder/decoder is written (Section 5.4)."

### §5.3 Validity of Items

- (§5.3) "A CBOR-based protocol could be specified in several layers, in which the lower layers don't process the semantics of some of the CBOR data they forward.  These layers can't notice any validity errors in data they don't process and MUST forward that data as-is.  The first layer that does process the semantics of an invalid CBOR item MUST pick one of two choices:"

```text
   1.  Replace the problematic item with an error marker and continue
       with the next item, or

   2.  Issue an error and stop processing altogether.
```

- (§5.3) "A CBOR-based protocol MUST specify which of these options its decoders take for each kind of invalid item they might encounter."
- (§5.3) "Such problems might occur at the basic validity level of CBOR or in the context of tags (tag validity)."

#### §5.3.1 Basic validity

Verbatim (§5.3.1):

```text
   Two kinds of validity errors can occur in the basic generic data
   model:

   Duplicate keys in a map:  Generic decoders (Section 5.2) make data
      available to applications using the native CBOR data model.  That
      data model includes maps (key-value mappings with unique keys),
      not multimaps (key-value mappings where multiple entries can have
      the same key).  Thus, a generic decoder that gets a CBOR map item
      that has duplicate keys will decode to a map with only one
      instance of that key, or it might stop processing altogether.  On
      the other hand, a "streaming decoder" may not even be able to
      notice.  See Section 5.6 for more discussion of keys in maps.

   Invalid UTF-8 string:  A decoder might or might not want to verify
      that the sequence of bytes in a UTF-8 string (major type 3) is
      actually valid UTF-8 and react appropriately.
```

#### §5.3.2 Tag validity

Verbatim (§5.3.2):

```text
   Two additional kinds of validity errors are introduced by adding tags
   to the basic generic data model:

   Inadmissible type for tag content:  Tag numbers (Section 3.4) specify
      what type of data item is supposed to be used as their tag
      content; for example, the tag numbers for unsigned or negative
      bignums are supposed to be put on byte strings.  A decoder that
      decodes the tagged data item into a native representation (a
      native big integer in this example) is expected to check the type
      of the data item being tagged.  Even decoders that don't have such
      native representations available in their environment may perform
      the check on those tags known to them and react appropriately.

   Inadmissible value for tag content:  The type of data item may be
      admissible for a tag's content, but the specific value may not be;
      e.g., a value of "yesterday" is not acceptable for the content of
      tag 0, even though it properly is a text string.  A decoder that
      normally ingests such tags into equivalent platform types might
      present this tag to the application in a similar way to how it
      would present a tag with an unknown tag number (Section 5.4).
```

### §5.4 Validity and Evolution

- (§5.4) "A decoder with validity checking will expend the effort to reliably detect data items with validity errors.  For example, such a decoder needs to have an API that reports an error (and does not return data) for a CBOR data item that contains any of the validity errors listed in the previous subsection."
- (§5.4) "The set of tags defined in the "Concise Binary Object Representation (CBOR) Tags" registry (Section 9.2), as well as the set of simple values defined in the "Concise Binary Object Representation (CBOR) Simple Values" registry (Section 9.1), can grow at any time beyond the set understood by a generic decoder.  A validity-checking decoder can do one of two things when it encounters such a case that it does not recognize:"

```text
   *  It can report an error (and not return data).  Note that treating
      this case as an error can cause ossification and is thus not
      encouraged.  This error is not a validity error, per se.  This
      kind of error is more likely to be raised by a decoder that would
      be performing validity checking if this were a known case.

   *  It can emit the unknown item (type, value, and, for tags, the
      decoded tagged data item) to the application calling the decoder,
      and then give the application an indication that the decoder did
      not recognize that tag number or simple value.
```

- (§5.4) "The latter approach, which is also appropriate for decoders that do not support validity checking, provides forward compatibility with newly registered tags and simple values without the requirement to update the encoder at the same time as the calling application.  (For this, the decoder's API needs the ability to mark unknown items so that the calling application can handle them in a manner appropriate for the program.)"
- (§5.4) "Since some of the processing needed for validity checking may have an appreciable cost (in particular with duplicate detection for maps), support of validity checking is not a requirement placed on all CBOR decoders."
- (§5.4) "Some encoders will rely on their applications to provide input data in such a way that valid CBOR results from the encoder.  A generic encoder may also want to provide a validity-checking mode where it reliably limits its output to valid CBOR, independent of whether or not its application is indeed providing API-conformant data."

### §5.5 Numbers

- (§5.5) "CBOR-based protocols should take into account that different language environments pose different restrictions on the range and precision of numbers that are representable."
- (§5.5) "A protocol that uses numbers should define its expectations on the handling of nontrivial numbers in decoders and receiving applications."
- (§5.5) "A CBOR-based protocol that includes floating-point numbers can restrict which of the three formats (half-precision, single-precision, and double-precision) are to be supported.  For an integer-only application, a protocol may want to completely exclude the use of floating-point values."
- (§5.5) "There is an expectation that encoders will use the most compact integer representation that can represent a given value.  However, a compact application that does not require deterministic encoding should accept values that use a longer-than-needed encoding (such as encoding "0" as 0b000_11001 followed by two bytes of 0x00) as long as the application can decode an integer of the given size.  Similar considerations apply to floating-point values; decoding both preferred serializations and longer-than-needed ones is recommended."
- (§5.5) "CBOR-based protocols for constrained applications that provide a choice between representing a specific number as an integer and as a decimal fraction or bigfloat (such as when the exponent is small and nonnegative) might express a quality-of-implementation expectation that the integer representation is used directly."

### §5.6 Specifying Keys for Maps

- (§5.6) "The encoding and decoding applications need to agree on what types of keys are going to be used in maps."
- (§5.6) "This means that, if integer keys are used, the protocol needs to avoid the use of floating-point keys the values of which happen to be integer numbers in the same map."
- (§5.6) "A CBOR-based protocol MUST define what to do when a receiving application sees multiple identical keys in a map.  The resulting rule in the protocol MUST respect the CBOR data model: it cannot prescribe a specific handling of the entries with the identical keys, except that it might have a rule that having identical keys in a map indicates a malformed map and that the decoder has to stop with an error."
- (§5.6) "When processing maps that exhibit entries with duplicate keys, a generic decoder might do one of the following:"

```text
   *  Not accept maps with duplicate keys (that is, enforce validity for
      maps, see also Section 5.4).  These generic decoders are
      universally useful.  An application may still need to perform its
      own duplicate checking based on application rules (for instance,
      if the application equates integers and floating-point values in
      map key positions for specific maps).

   *  Pass all map entries to the application, including ones with
      duplicate keys.  This requires that the application handle (check
      against) duplicate keys, even if the application rules are
      identical to the generic data model rules.

   *  Lose some entries with duplicate keys, e.g., deliver only the
      final (or first) entry out of the entries with the same key.  With
      such a generic decoder, applications may get different results for
      a specific key on different runs, and with different generic
      decoders, which value is returned is based on generic decoder
      implementation and the actual order of keys in the map.  In
      particular, applications cannot validate key uniqueness on their
      own as they do not necessarily see all entries; they may not be
      able to use such a generic decoder if they need to validate key
      uniqueness.  These generic decoders can only be used in situations
      where the data source and transfer always provide valid maps; this
      is not possible if the data source and transfer can be attacked.
```

- (§5.6) "Generic decoders need to document which of these three approaches they implement."
- (§5.6) "The CBOR data model for maps does not allow ascribing semantics to the order of the key/value pairs in the map representation.  Thus, a CBOR-based protocol MUST NOT specify that changing the key/value pair order in a map changes the semantics, except to specify that some orders are disallowed, for example, where they would not meet the requirements of a deterministic encoding (Section 4.2)."

#### §5.6.1 Equivalence of Keys

Complete and verbatim (§5.6.1):

```text
   The specific data model that applies to a CBOR data item is used to
   determine whether keys occurring in maps are duplicates or distinct.

   At the generic data model level, numerically equivalent integer and
   floating-point values are distinct from each other, as they are from
   the various big numbers (Tags 2 to 5).  Similarly, text strings are
   distinct from byte strings, even if composed of the same bytes.  A
   tagged value is distinct from an untagged value or from a value
   tagged with a different tag number.

   Within each of these groups, numeric values are distinct unless they
   are numerically equal (specifically, -0.0 is equal to 0.0); for the
   purpose of map key equivalence, NaN values are equivalent if they
   have the same significand after zero-extending both significands at
   the right to 64 bits.

   Both byte strings and text strings are compared byte by byte, arrays
   are compared element by element, and are equal if they have the same
   number of bytes/elements and the same values at the same positions.
   Two maps are equal if they have the same set of pairs regardless of
   their order; pairs are equal if both the key and value are equal.

   Tagged values are equal if both the tag number and the tag content
   are equal.  (Note that a generic decoder that provides processing for
   a specific tag may not be able to distinguish some semantically
   equivalent values, e.g., if leading zeroes occur in the content of
   tag 2 or tag 3 (Section 3.4.3).)  Simple values are equal if they
   simply have the same value.  Nothing else is equal in the generic
   data model; a simple value 2 is not equivalent to an integer 2, and
   an array is never equivalent to a map.

   As discussed in Section 2.2, specific data models can make values
   equivalent for the purpose of comparing map keys that are distinct in
   the generic data model.  Note that this implies that a generic
   decoder may deliver a decoded map to an application that needs to be
   checked for duplicate map keys by that application (alternatively,
   the decoder may provide a programming interface to perform this
   service for the application).  Specific data models are not able to
   distinguish values for map keys that are equal for this purpose at
   the generic data model level.
```

### §5.7 Undefined Values

- (§5.7) "In some CBOR-based protocols, the simple value (Section 3.3) of "undefined" might be used by an encoder as a substitute for a data item with an encoding problem, in order to allow the rest of the enclosing data items to be encoded without harm."

## §6. Converting Data between CBOR and JSON

- (§6) "This section gives non-normative advice about converting between CBOR and JSON.  Implementations of converters MAY use whichever advice here they want."
- (§6) "It is worth noting that a JSON text is a sequence of characters, not an encoded sequence of bytes, while a CBOR data item consists of bytes, not characters."

### §6.1 Converting from CBOR to JSON

- (§6.1) "The following non-normative advice deals with these by converting them to a single substitute value, such as a JSON null."

Verbatim (§6.1):

```text
   *  An integer (major type 0 or 1) becomes a JSON number.

   *  A byte string (major type 2) that is not embedded in a tag that
      specifies a proposed encoding is encoded in base64url without
      padding and becomes a JSON string.

   *  A UTF-8 string (major type 3) becomes a JSON string.  Note that
      JSON requires escaping certain characters ([RFC8259], Section 7):
      quotation mark (U+0022), reverse solidus (U+005C), and the "C0
      control characters" (U+0000 through U+001F).  All other characters
      are copied unchanged into the JSON UTF-8 string.

   *  An array (major type 4) becomes a JSON array.

   *  A map (major type 5) becomes a JSON object.  This is possible
      directly only if all keys are UTF-8 strings.  A converter might
      also convert other keys into UTF-8 strings (such as by converting
      integers into strings containing their decimal representation);
      however, doing so introduces a danger of key collision.  Note also
      that, if tags on UTF-8 strings are ignored as proposed below, this
      will cause a key collision if the tags are different but the
      strings are the same.

   *  False (major type 7, additional information 20) becomes a JSON
      false.

   *  True (major type 7, additional information 21) becomes a JSON
      true.

   *  Null (major type 7, additional information 22) becomes a JSON
      null.

   *  A floating-point value (major type 7, additional information 25
      through 27) becomes a JSON number if it is finite (that is, it can
      be represented in a JSON number); if the value is non-finite (NaN,
      or positive or negative Infinity), it is represented by the
      substitute value.

   *  Any other simple value (major type 7, any additional information
      value not yet discussed) is represented by the substitute value.

   *  A bignum (major type 6, tag number 2 or 3) is represented by
      encoding its byte string in base64url without padding and becomes
      a JSON string.  For tag number 3 (negative bignum), a "~" (ASCII
      tilde) is inserted before the base-encoded value.  (The conversion
      to a binary blob instead of a number is to prevent a likely
      numeric overflow for the JSON decoder.)

   *  A byte string with an encoding hint (major type 6, tag number 21
      through 23) is encoded as described by the hint and becomes a JSON
      string.

   *  For all other tags (major type 6, any other tag number), the tag
      content is represented as a JSON value; the tag number is ignored.

   *  Indefinite-length items are made definite before conversion.
```

### §6.2 Converting from JSON to CBOR

- (§6.2) "All JSON values, once decoded, directly map into one or more CBOR values.  As with any kind of CBOR generation, decisions have to be made with respect to number representation.  In a suggested conversion:"

Verbatim (§6.2):

```text
   *  JSON numbers without fractional parts (integer numbers) are
      represented as integers (major types 0 and 1, possibly major type
      6, tag number 2 and 3), choosing the shortest form; integers
      longer than an implementation-defined threshold may instead be
      represented as floating-point values.  The default range that is
      represented as integer is -2^(53)+1..2^(53)-1 (fully exploiting
      the range for exact integers in the binary64 representation often
      used for decoding JSON [RFC7493]).  A CBOR-based protocol, or a
      generic converter implementation, may choose -2^(32)..2^(32)-1 or
      -2^(64)..2^(64)-1 (fully using the integer ranges available in
      CBOR with uint32_t or uint64_t, respectively) or even
      -2^(31)..2^(31)-1 or -2^(63)..2^(63)-1 (using popular ranges for
      two's complement signed integers).  (If the JSON was generated
      from a JavaScript implementation, its precision is already limited
      to 53 bits maximum.)

   *  Numbers with fractional parts are represented as floating-point
      values, performing the decimal-to-binary conversion based on the
      precision provided by IEEE 754 binary64.  The mathematical value
      of the JSON number is converted to binary64 using the
      roundTiesToEven procedure in Section 4.3.1 of [IEEE754].  Then,
      when encoding in CBOR, the preferred serialization uses the
      shortest floating-point representation exactly representing this
      conversion result; for instance, 1.5 is represented in a 16-bit
      floating-point value (not all implementations will be capable of
      efficiently finding the minimum form, though).  Instead of using
      the default binary64 precision, there may be an implementation-
      defined limit to the precision of the conversion that will affect
      the precision of the represented values.  Decimal representation
      should only be used on the CBOR side if that is specified in a
      protocol.
```

## §7. Future Evolution of CBOR

### §7.1 Extension Points

- (§7.1) "Protocol designs should attempt to make the codepoint space large enough so that it can slowly be filled over the intended lifetime of the protocol."

Verbatim (§7.1):

```text
   CBOR has three major extension points:

   the "simple" space (values in major type 7):  Of the 24 efficient
      (and 224 slightly less efficient) values, only a small number have
      been allocated.  Implementations receiving an unknown simple data
      item may easily be able to process it as such, given that the
      structure of the value is indeed simple.  The IANA registry in
      Section 9.1 is the appropriate way to address the extensibility of
      this codepoint space.

   the "tag" space (values in major type 6):  The total codepoint space
      is abundant; only a tiny part of it has been allocated.  However,
      not all of these codepoints are equally efficient: the first 24
      only consume a single ("1+0") byte, and half of them have already
      been allocated.  The next 232 values only consume two ("1+1")
      bytes, with nearly a quarter already allocated.  These subspaces
      need some curation to last for a few more decades.
      Implementations receiving an unknown tag number can choose to
      process just the enclosed tag content or, preferably, to process
      the tag as an unknown tag number wrapping the tag content.  The
      IANA registry in Section 9.2 is the appropriate way to address the
      extensibility of this codepoint space.

   the "additional information" space:  An implementation receiving an
      unknown additional information value has no way to continue
      decoding, so allocating codepoints in this space is a major step
      beyond just exercising an extension point.  There are also very
      few codepoints left.  See also Section 7.2.
```

### §7.2 Curating the Additional Information Space

- (§7.2) "The present specification does not manage the additional information codepoint space by an IANA registry.  Instead, allocations out of this space can only be done by updating this specification."
- (§7.2) "For an additional information value of n >= 24, the size of the additional data typically is 2^(n-24) bytes.  Therefore, additional information values 28 and 29 should be viewed as candidates for 128-bit and 256-bit quantities, in case a need arises to add them to the protocol.  Additional information value 30 is then the only additional information value available for general allocation, and there should be a very good reason for allocating it before assigning it through an update of the present specification."

## §8. Diagnostic Notation

- (§8) "CBOR is a binary interchange format.  To facilitate documentation and debugging, and in particular to facilitate communication between entities cooperating in debugging, this section defines a simple human-readable diagnostic notation.  All actual interchange always happens in the binary format."
- (§8) "Note that this truly is a diagnostic format; it is not meant to be parsed.  Therefore, no formal definition (as in ABNF) is given in this document."

Definition of the notation itself (§8), verbatim:

```text
   The diagnostic notation is loosely based on JSON as it is defined in
   RFC 8259, extending it where needed.

   The notation borrows the JSON syntax for numbers (integer and
   floating-point), True (>true<), False (>false<), Null (>null<), UTF-8
   strings, arrays, and maps (maps are called objects in JSON; the
   diagnostic notation extends JSON here by allowing any data item in
   the key position).  Undefined is written >undefined< as in
   JavaScript.  The non-finite floating-point numbers Infinity,
   -Infinity, and NaN are written exactly as in this sentence (this is
   also a way they can be written in JavaScript, although JSON does not
   allow them).  A tag is written as an integer number for the tag
   number, followed by the tag content in parentheses; for instance, a
   date in the format specified by RFC 3339 (ISO 8601) could be notated
   as:

        0("2013-03-21T20:04:00Z")

   or the equivalent relative time as the following:

        1(1363896240)
```

- (§8) "Byte strings are notated in one of the base encodings, without padding, enclosed in single quotes, prefixed by >h< for base16, >b32< for base32, >h32< for base32hex, >b64< for base64 or base64url (the actual encodings do not overlap, so the string remains unambiguous)."
- (§8) "Unassigned simple values are given as "simple()" with the appropriate integer in the parentheses."

### §8.1 Encoding Indicators

Verbatim (§8.1):

```text
   Sometimes it is useful to indicate in the diagnostic notation which
   of several alternative representations were actually used; for
   example, a data item written >1.5< by a diagnostic decoder might have
   been encoded as a half-, single-, or double-precision float.

   The convention for encoding indicators is that anything starting with
   an underscore and all following characters that are alphanumeric or
   underscore is an encoding indicator, and can be ignored by anyone not
   interested in this information.  For example, "_" or "_3".  Encoding
   indicators are always optional.

   A single underscore can be written after the opening brace of a map
   or the opening bracket of an array to indicate that the data item was
   represented in indefinite-length format.  For example, [_ 1, 2]
   contains an indicator that an indefinite-length representation was
   used to represent the data item [1, 2].

   An underscore followed by a decimal digit n indicates that the
   preceding item (or, for arrays and maps, the item starting with the
   preceding bracket or brace) was encoded with an additional
   information value of 24+n.  For example, 1.5_1 is a half-precision
   floating-point number, while 1.5_3 is encoded as double precision.
   This encoding indicator is not shown in Appendix A.  (Note that the
   encoding indicator "_" is thus an abbreviation of the full form "_7",
   which is not used.)

   The detailed chunk structure of byte and text strings of indefinite
   length can be notated in the form (_ h'0123', h'4567') and (_ "foo",
   "bar").  However, for an indefinite-length string with no chunks
   inside, (_ ) would be ambiguous as to whether a byte string (0x5fff)
   or a text string (0x7fff) is meant and is therefore not used.  The
   basic forms ''_ and ""_ can be used instead and are reserved for the
   case of no chunks only -- not as short forms for the (permitted, but
   not really useful) encodings with only empty chunks, which need to be
   notated as (_ ''), (_ ""), etc., to preserve the chunk structure.
```

## §9. IANA Considerations

Verbatim (§9):

```text
   IANA has created two registries for new CBOR values.  The registries
   are separate, that is, not under an umbrella registry, and follow the
   rules in [RFC8126].  IANA has also assigned a new media type, an
   associated CoAP Content-Format entry, and a structured syntax suffix.
```

### §9.1 CBOR Simple Values Registry

Registration policy, verbatim (§9.1):

```text
   IANA has created the "Concise Binary Object Representation (CBOR)
   Simple Values" registry at [IANA.cbor-simple-values].  The initial
   values are shown in Table 4.

   New entries in the range 0 to 19 are assigned by Standards Action
   [RFC8126].  It is suggested that IANA allocate values starting with
   the number 16 in order to reserve the lower numbers for contiguous
   blocks (if any).

   New entries in the range 32 to 255 are assigned by Specification
   Required.
```

### §9.2 CBOR Tags Registry

Registration policy and template, verbatim (§9.2):

```text
   IANA has created the "Concise Binary Object Representation (CBOR)
   Tags" registry at [IANA.cbor-tags].  The tags that were defined in
   [RFC7049] are described in detail in Section 3.4, and other tags have
   already been defined since then.

   New entries in the range 0 to 23 ("1+0") are assigned by Standards
   Action.  New entries in the ranges 24 to 255 ("1+1") and 256 to 32767
   (lower half of "1+2") are assigned by Specification Required.  New
   entries in the range 32768 to 18446744073709551615 (upper half of
   "1+2", "1+4", and "1+8") are assigned by First Come First Served.
   The template for registration requests is:

   *  Data item

   *  Semantics (short form)

   In addition, First Come First Served requests should include:

   *  Point of contact

   *  Description of semantics (URL) -- This description is optional;
      the URL can point to something like an Internet-Draft or a web
      page.

   Applicants exercising the First Come First Served range and making a
   suggestion for a tag number that is not representable in 32 bits
   (i.e., larger than 4294967295) should be aware that this could reduce
   interoperability with implementations that do not support 64-bit
   numbers.
```

### §9.3 Media Types Registry

Registration, verbatim (§9.3):

```text
   The Internet media type [RFC6838] ("MIME type") for a single encoded
   CBOR data item is "application/cbor" as defined in the "Media Types"
   registry [IANA.media-types]:

   Type name:  application

   Subtype name:  cbor

   Required parameters:  n/a

   Optional parameters:  n/a

   Encoding considerations:  Binary

   Security considerations:  See Section 10 of RFC 8949.

   Interoperability considerations:  n/a

   Published specification:  RFC 8949

   Applications that use this media type:  Many

   Additional information:

      Magic number(s):  n/a
      File extension(s):  .cbor
      Macintosh file type code(s):  n/a

   Person & email address to contact for further information:  IETF CBOR
      Working Group (cbor@ietf.org) or IETF Applications and Real-Time
      Area (art@ietf.org)

   Intended usage:  COMMON

   Restrictions on usage:  none

   Author:  IETF CBOR Working Group (cbor@ietf.org)

   Change controller:  The IESG (iesg@ietf.org)
```

### §9.4 CoAP Content-Format Registry

Registration, verbatim (§9.4):

```text
   The CoAP Content-Format for CBOR has been registered in the "CoAP
   Content-Formats" subregistry within the "Constrained RESTful
   Environments (CoRE) Parameters" registry [IANA.core-parameters]:

   Media Type:  application/cbor

   Encoding:  -

   ID:  60

   Reference:  RFC 8949
```

### §9.5 Structured Syntax Suffix Registry

Registration, verbatim (§9.5):

```text
   The structured syntax suffix [RFC6838] for media types based on a
   single encoded CBOR data item is +cbor, which IANA has registered in
   the "Structured Syntax Suffixes" registry [IANA.structured-suffix]:

   Name:  Concise Binary Object Representation (CBOR)

   +suffix:  +cbor

   References:  RFC 8949

   Encoding Considerations:  CBOR is a binary format.

   Interoperability Considerations:  n/a

   Fragment Identifier Considerations:  The syntax and semantics of
      fragment identifiers specified for +cbor SHOULD be as specified
      for "application/cbor".  (At publication of RFC 8949, there is no
      fragment identification syntax defined for "application/cbor".)

      The syntax and semantics for fragment identifiers for a specific
      "xxx/yyy+cbor" SHOULD be processed as follows:

      *  For cases defined in +cbor, where the fragment identifier
         resolves per the +cbor rules, then process as specified in
         +cbor.

      *  For cases defined in +cbor, where the fragment identifier does
         not resolve per the +cbor rules, then process as specified in
         "xxx/yyy+cbor".

      *  For cases not defined in +cbor, then process as specified in
         "xxx/yyy+cbor".

   Security Considerations:  See Section 10 of RFC 8949.

   Contact:  IETF CBOR Working Group (cbor@ietf.org) or IETF
      Applications and Real-Time Area (art@ietf.org)

   Author/Change Controller:  IETF
```

## §10. Security Considerations

- (§10) "Because CBOR decoders are often used as a first step in processing unvalidated input, they need to be fully prepared for all types of hostile input that may be designed to corrupt, overrun, or achieve control of the system decoding the CBOR data item.  A CBOR decoder needs to assume that all input may be hostile even if it has been checked by a firewall, has come over a secure channel such as TLS, is encrypted or signed, or has come from some other source that is presumed trusted."
- (§10) "Section 4.1 gives examples of limitations in interoperability when using a constrained CBOR decoder with input from a CBOR encoder that uses a non-preferred serialization.  When a single data item is consumed both by such a constrained decoder and a full decoder, it can lead to security issues that can be exploited by an attacker who can inject or manipulate content."
- (§10) "Hostile input may be constructed to overrun buffers, to overflow or underflow integer arithmetic, or to cause other decoding disruption.  CBOR data items might have lengths or sizes that are intentionally extremely large or too short.  Resource exhaustion attacks might attempt to lure a decoder into allocating very big data items (strings, arrays, maps, or even arbitrary precision numbers) or exhaust the stack depth by setting up deeply nested items.  Decoders need to have appropriate resource management to mitigate these attacks.  (Items for which very large sizes are given can also attempt to exploit integer overflow vulnerabilities.)"
- (§10) "A CBOR decoder, by definition, only accepts well-formed CBOR; this is the first step to its robustness.  Input that is not well-formed CBOR causes no further processing from the point where the lack of well-formedness was detected.  If possible, any data decoded up to this point should have no impact on the application using the CBOR decoder."
- (§10) "In addition to ascertaining well-formedness, a CBOR decoder might also perform validity checks on the CBOR data.  Alternatively, it can leave those checks to the application using the decoder.  This choice needs to be clearly documented in the decoder.  Beyond the validity at the CBOR level, an application also needs to ascertain that the input is in alignment with the application protocol that is serialized in CBOR."
- (§10) "Also, some hash-table implementations that are used by decoders to build in-memory representations of maps can be attacked to spend quadratic effort, unless a secret key (see Section 7 of [SIPHASH_LNCS], also [SIPHASH_OPEN]) or some other mitigation is employed.  Such superlinear efforts can be exploited by an attacker to exhaust resources at or before the input validator; they therefore need to be avoided in a CBOR decoder implementation."
- (§10) "Note that tag number definitions and their implementations can add security considerations of this kind; this should then be discussed in the security considerations of the tag number definition."
- (§10) "However, CBOR encoders often have an API that takes input from another level in the implementation and can be attacked through that API.  The design and implementation of that API should assume the behavior of its caller may be based on hostile input or on coding mistakes.  It should check inputs for buffer overruns, overflow and underflow of integer arithmetic, and other such errors that are aimed to disrupt the encoder."
- (§10) "Protocols should be defined in such a way that potential multiple interpretations are reliably reduced to a single interpretation."
- (§10) "To facilitate consistent interpretation, encoder and decoder implementations should provide a validity-checking mode of operation (Section 5.4).  Note, however, that a generic decoder cannot know about all requirements that an application poses on its input data; it is therefore not relieving the application from performing its own input checking."
- (§10) "Generic decoders therefore need to document which tag numbers they support and what validity checking they provide for those tag numbers as well as for basic CBOR (UTF-8 checking, duplicate map key checking)."
- (§10) "Section 3.4.3 notes that using the non-preferred choice of a bignum representation instead of a basic integer for encoding a number is not intended to have application semantics, but it can have such semantics if an application receiving CBOR data is using a decoder in the basic generic data model.  This disparity causes a security issue if the two sets of semantics differ.  Thus, applications using CBOR need to specify the data model that they are using for each use of CBOR data."
- (§10) "It is common to convert CBOR data to other formats.  In many cases, CBOR has more expressive types than other formats; this is particularly true for the common conversion to JSON.  The loss of type information can cause security issues for the systems that are processing the less-expressive data."
- (§10) "Security considerations for the use of base16 and base64 from [RFC4648], and the use of UTF-8 from [RFC3629], are relevant to CBOR as well."

## Appendix A. Examples of Encoded CBOR Data Items

- (Appendix A) "The following table provides some CBOR-encoded values in hexadecimal (right column), together with diagnostic notation for these values (left column)."
- (Appendix A) "In the diagnostic notation provided for bignums, their intended numeric value is shown as a decimal number (such as 18446744073709551616) instead of a tagged byte string (such as 2(h'010000000000000000'))."

(Table 6)

```text
   +==============================+====================================+
   |Diagnostic                    | Encoded                            |
   +==============================+====================================+
   |0                             | 0x00                               |
   +------------------------------+------------------------------------+
   |1                             | 0x01                               |
   +------------------------------+------------------------------------+
   |10                            | 0x0a                               |
   +------------------------------+------------------------------------+
   |23                            | 0x17                               |
   +------------------------------+------------------------------------+
   |24                            | 0x1818                             |
   +------------------------------+------------------------------------+
   |25                            | 0x1819                             |
   +------------------------------+------------------------------------+
   |100                           | 0x1864                             |
   +------------------------------+------------------------------------+
   |1000                          | 0x1903e8                           |
   +------------------------------+------------------------------------+
   |1000000                       | 0x1a000f4240                       |
   +------------------------------+------------------------------------+
   |1000000000000                 | 0x1b000000e8d4a51000               |
   +------------------------------+------------------------------------+
   |18446744073709551615          | 0x1bffffffffffffffff               |
   +------------------------------+------------------------------------+
   |18446744073709551616          | 0xc249010000000000000000           |
   +------------------------------+------------------------------------+
   |-18446744073709551616         | 0x3bffffffffffffffff               |
   +------------------------------+------------------------------------+
   |-18446744073709551617         | 0xc349010000000000000000           |
   +------------------------------+------------------------------------+
   |-1                            | 0x20                               |
   +------------------------------+------------------------------------+
   |-10                           | 0x29                               |
   +------------------------------+------------------------------------+
   |-100                          | 0x3863                             |
   +------------------------------+------------------------------------+
   |-1000                         | 0x3903e7                           |
   +------------------------------+------------------------------------+
   |0.0                           | 0xf90000                           |
   +------------------------------+------------------------------------+
   |-0.0                          | 0xf98000                           |
   +------------------------------+------------------------------------+
   |1.0                           | 0xf93c00                           |
   +------------------------------+------------------------------------+
   |1.1                           | 0xfb3ff199999999999a               |
   +------------------------------+------------------------------------+
   |1.5                           | 0xf93e00                           |
   +------------------------------+------------------------------------+
   |65504.0                       | 0xf97bff                           |
   +------------------------------+------------------------------------+
   |100000.0                      | 0xfa47c35000                       |
   +------------------------------+------------------------------------+
   |3.4028234663852886e+38        | 0xfa7f7fffff                       |
   +------------------------------+------------------------------------+
   |1.0e+300                      | 0xfb7e37e43c8800759c               |
   +------------------------------+------------------------------------+
   |5.960464477539063e-8          | 0xf90001                           |
   +------------------------------+------------------------------------+
   |0.00006103515625              | 0xf90400                           |
   +------------------------------+------------------------------------+
   |-4.0                          | 0xf9c400                           |
   +------------------------------+------------------------------------+
   |-4.1                          | 0xfbc010666666666666               |
   +------------------------------+------------------------------------+
   |Infinity                      | 0xf97c00                           |
   +------------------------------+------------------------------------+
   |NaN                           | 0xf97e00                           |
   +------------------------------+------------------------------------+
   |-Infinity                     | 0xf9fc00                           |
   +------------------------------+------------------------------------+
   |Infinity                      | 0xfa7f800000                       |
   +------------------------------+------------------------------------+
   |NaN                           | 0xfa7fc00000                       |
   +------------------------------+------------------------------------+
   |-Infinity                     | 0xfaff800000                       |
   +------------------------------+------------------------------------+
   |Infinity                      | 0xfb7ff0000000000000               |
   +------------------------------+------------------------------------+
   |NaN                           | 0xfb7ff8000000000000               |
   +------------------------------+------------------------------------+
   |-Infinity                     | 0xfbfff0000000000000               |
   +------------------------------+------------------------------------+
   |false                         | 0xf4                               |
   +------------------------------+------------------------------------+
   |true                          | 0xf5                               |
   +------------------------------+------------------------------------+
   |null                          | 0xf6                               |
   +------------------------------+------------------------------------+
   |undefined                     | 0xf7                               |
   +------------------------------+------------------------------------+
   |simple(16)                    | 0xf0                               |
   +------------------------------+------------------------------------+
   |simple(255)                   | 0xf8ff                             |
   +------------------------------+------------------------------------+
   |0("2013-03-21T20:04:00Z")     | 0xc074323031332d30332d32315432303a |
   |                              | 30343a30305a                       |
   +------------------------------+------------------------------------+
   |1(1363896240)                 | 0xc11a514b67b0                     |
   +------------------------------+------------------------------------+
   |1(1363896240.5)               | 0xc1fb41d452d9ec200000             |
   +------------------------------+------------------------------------+
   |23(h'01020304')               | 0xd74401020304                     |
   +------------------------------+------------------------------------+
   |24(h'6449455446')             | 0xd818456449455446                 |
   +------------------------------+------------------------------------+
   |32("http://www.example.com")  | 0xd82076687474703a2f2f7777772e6578 |
   |                              | 616d706c652e636f6d                 |
   +------------------------------+------------------------------------+
   |h''                           | 0x40                               |
   +------------------------------+------------------------------------+
   |h'01020304'                   | 0x4401020304                       |
   +------------------------------+------------------------------------+
   |""                            | 0x60                               |
   +------------------------------+------------------------------------+
   |"a"                           | 0x6161                             |
   +------------------------------+------------------------------------+
   |"IETF"                        | 0x6449455446                       |
   +------------------------------+------------------------------------+
   |"\"\\"                        | 0x62225c                           |
   +------------------------------+------------------------------------+
   |"\u00fc"                      | 0x62c3bc                           |
   +------------------------------+------------------------------------+
   |"\u6c34"                      | 0x63e6b0b4                         |
   +------------------------------+------------------------------------+
   |"\ud800\udd51"                | 0x64f0908591                       |
   +------------------------------+------------------------------------+
   |[]                            | 0x80                               |
   +------------------------------+------------------------------------+
   |[1, 2, 3]                     | 0x83010203                         |
   +------------------------------+------------------------------------+
   |[1, [2, 3], [4, 5]]           | 0x8301820203820405                 |
   +------------------------------+------------------------------------+
   |[1, 2, 3, 4, 5, 6, 7, 8, 9,   | 0x98190102030405060708090a0b0c0d0e |
   |10, 11, 12, 13, 14, 15, 16,   | 0f101112131415161718181819         |
   |17, 18, 19, 20, 21, 22, 23,   |                                    |
   |24, 25]                       |                                    |
   +------------------------------+------------------------------------+
   |{}                            | 0xa0                               |
   +------------------------------+------------------------------------+
   |{1: 2, 3: 4}                  | 0xa201020304                       |
   +------------------------------+------------------------------------+
   |{"a": 1, "b": [2, 3]}         | 0xa26161016162820203               |
   +------------------------------+------------------------------------+
   |["a", {"b": "c"}]             | 0x826161a161626163                 |
   +------------------------------+------------------------------------+
   |{"a": "A", "b": "B", "c": "C",| 0xa5616161416162614261636143616461 |
   |"d": "D", "e": "E"}           | 4461656145                         |
   +------------------------------+------------------------------------+
   |(_ h'0102', h'030405')        | 0x5f42010243030405ff               |
   +------------------------------+------------------------------------+
   |(_ "strea", "ming")           | 0x7f657374726561646d696e67ff       |
   +------------------------------+------------------------------------+
   |[_ ]                          | 0x9fff                             |
   +------------------------------+------------------------------------+
   |[_ 1, [2, 3], [_ 4, 5]]       | 0x9f018202039f0405ffff             |
   +------------------------------+------------------------------------+
   |[_ 1, [2, 3], [4, 5]]         | 0x9f01820203820405ff               |
   +------------------------------+------------------------------------+
   |[1, [2, 3], [_ 4, 5]]         | 0x83018202039f0405ff               |
   +------------------------------+------------------------------------+
   |[1, [_ 2, 3], [4, 5]]         | 0x83019f0203ff820405               |
   +------------------------------+------------------------------------+
   |[_ 1, 2, 3, 4, 5, 6, 7, 8, 9, | 0x9f0102030405060708090a0b0c0d0e0f |
   |10, 11, 12, 13, 14, 15, 16,   | 101112131415161718181819ff         |
   |17, 18, 19, 20, 21, 22, 23,   |                                    |
   |24, 25]                       |                                    |
   +------------------------------+------------------------------------+
   |{_ "a": 1, "b": [_ 2, 3]}     | 0xbf61610161629f0203ffff           |
   +------------------------------+------------------------------------+
   |["a", {_ "b": "c"}]           | 0x826161bf61626163ff               |
   +------------------------------+------------------------------------+
   |{_ "Fun": true, "Amt": -2}    | 0xbf6346756ef563416d7421ff         |
   +------------------------------+------------------------------------+

                Table 6: Examples of Encoded CBOR Data Items
```

## Appendix B. Jump Table for Initial Byte

- (Appendix B) "For brevity, this jump table does not show initial bytes that are reserved for future extension.  It also only shows a selection of the initial bytes that can be used for optional features.  (All unsigned integers are in network byte order.)"

(Table 7)

```text
      +============+================================================+
      | Byte       | Structure/Semantics                            |
      +============+================================================+
      | 0x00..0x17 | unsigned integer 0x00..0x17 (0..23)            |
      +------------+------------------------------------------------+
      | 0x18       | unsigned integer (one-byte uint8_t follows)    |
      +------------+------------------------------------------------+
      | 0x19       | unsigned integer (two-byte uint16_t follows)   |
      +------------+------------------------------------------------+
      | 0x1a       | unsigned integer (four-byte uint32_t follows)  |
      +------------+------------------------------------------------+
      | 0x1b       | unsigned integer (eight-byte uint64_t follows) |
      +------------+------------------------------------------------+
      | 0x20..0x37 | negative integer -1-0x00..-1-0x17 (-1..-24)    |
      +------------+------------------------------------------------+
      | 0x38       | negative integer -1-n (one-byte uint8_t for n  |
      |            | follows)                                       |
      +------------+------------------------------------------------+
      | 0x39       | negative integer -1-n (two-byte uint16_t for n |
      |            | follows)                                       |
      +------------+------------------------------------------------+
      | 0x3a       | negative integer -1-n (four-byte uint32_t for  |
      |            | n follows)                                     |
      +------------+------------------------------------------------+
      | 0x3b       | negative integer -1-n (eight-byte uint64_t for |
      |            | n follows)                                     |
      +------------+------------------------------------------------+
      | 0x40..0x57 | byte string (0x00..0x17 bytes follow)          |
      +------------+------------------------------------------------+
      | 0x58       | byte string (one-byte uint8_t for n, and then  |
      |            | n bytes follow)                                |
      +------------+------------------------------------------------+
      | 0x59       | byte string (two-byte uint16_t for n, and then |
      |            | n bytes follow)                                |
      +------------+------------------------------------------------+
      | 0x5a       | byte string (four-byte uint32_t for n, and     |
      |            | then n bytes follow)                           |
      +------------+------------------------------------------------+
      | 0x5b       | byte string (eight-byte uint64_t for n, and    |
      |            | then n bytes follow)                           |
      +------------+------------------------------------------------+
      | 0x5f       | byte string, byte strings follow, terminated   |
      |            | by "break"                                     |
      +------------+------------------------------------------------+
      | 0x60..0x77 | UTF-8 string (0x00..0x17 bytes follow)         |
      +------------+------------------------------------------------+
      | 0x78       | UTF-8 string (one-byte uint8_t for n, and then |
      |            | n bytes follow)                                |
      +------------+------------------------------------------------+
      | 0x79       | UTF-8 string (two-byte uint16_t for n, and     |
      |            | then n bytes follow)                           |
      +------------+------------------------------------------------+
      | 0x7a       | UTF-8 string (four-byte uint32_t for n, and    |
      |            | then n bytes follow)                           |
      +------------+------------------------------------------------+
      | 0x7b       | UTF-8 string (eight-byte uint64_t for n, and   |
      |            | then n bytes follow)                           |
      +------------+------------------------------------------------+
      | 0x7f       | UTF-8 string, UTF-8 strings follow, terminated |
      |            | by "break"                                     |
      +------------+------------------------------------------------+
      | 0x80..0x97 | array (0x00..0x17 data items follow)           |
      +------------+------------------------------------------------+
      | 0x98       | array (one-byte uint8_t for n, and then n data |
      |            | items follow)                                  |
      +------------+------------------------------------------------+
      | 0x99       | array (two-byte uint16_t for n, and then n     |
      |            | data items follow)                             |
      +------------+------------------------------------------------+
      | 0x9a       | array (four-byte uint32_t for n, and then n    |
      |            | data items follow)                             |
      +------------+------------------------------------------------+
      | 0x9b       | array (eight-byte uint64_t for n, and then n   |
      |            | data items follow)                             |
      +------------+------------------------------------------------+
      | 0x9f       | array, data items follow, terminated by        |
      |            | "break"                                        |
      +------------+------------------------------------------------+
      | 0xa0..0xb7 | map (0x00..0x17 pairs of data items follow)    |
      +------------+------------------------------------------------+
      | 0xb8       | map (one-byte uint8_t for n, and then n pairs  |
      |            | of data items follow)                          |
      +------------+------------------------------------------------+
      | 0xb9       | map (two-byte uint16_t for n, and then n pairs |
      |            | of data items follow)                          |
      +------------+------------------------------------------------+
      | 0xba       | map (four-byte uint32_t for n, and then n      |
      |            | pairs of data items follow)                    |
      +------------+------------------------------------------------+
      | 0xbb       | map (eight-byte uint64_t for n, and then n     |
      |            | pairs of data items follow)                    |
      +------------+------------------------------------------------+
      | 0xbf       | map, pairs of data items follow, terminated by |
      |            | "break"                                        |
      +------------+------------------------------------------------+
      | 0xc0       | text-based date/time (data item follows; see   |
      |            | Section 3.4.1)                                 |
      +------------+------------------------------------------------+
      | 0xc1       | epoch-based date/time (data item follows; see  |
      |            | Section 3.4.2)                                 |
      +------------+------------------------------------------------+
      | 0xc2       | unsigned bignum (data item "byte string"       |
      |            | follows)                                       |
      +------------+------------------------------------------------+
      | 0xc3       | negative bignum (data item "byte string"       |
      |            | follows)                                       |
      +------------+------------------------------------------------+
      | 0xc4       | decimal Fraction (data item "array" follows;   |
      |            | see Section 3.4.4)                             |
      +------------+------------------------------------------------+
      | 0xc5       | bigfloat (data item "array" follows; see       |
      |            | Section 3.4.4)                                 |
      +------------+------------------------------------------------+
      | 0xc6..0xd4 | (tag)                                          |
      +------------+------------------------------------------------+
      | 0xd5..0xd7 | expected conversion (data item follows; see    |
      |            | Section 3.4.5.2)                               |
      +------------+------------------------------------------------+
      | 0xd8..0xdb | (more tags; 1/2/4/8 bytes of tag number and    |
      |            | then a data item follow)                       |
      +------------+------------------------------------------------+
      | 0xe0..0xf3 | (simple value)                                 |
      +------------+------------------------------------------------+
      | 0xf4       | false                                          |
      +------------+------------------------------------------------+
      | 0xf5       | true                                           |
      +------------+------------------------------------------------+
      | 0xf6       | null                                           |
      +------------+------------------------------------------------+
      | 0xf7       | undefined                                      |
      +------------+------------------------------------------------+
      | 0xf8       | (simple value, one byte follows)               |
      +------------+------------------------------------------------+
      | 0xf9       | half-precision float (two-byte IEEE 754)       |
      +------------+------------------------------------------------+
      | 0xfa       | single-precision float (four-byte IEEE 754)    |
      +------------+------------------------------------------------+
      | 0xfb       | double-precision float (eight-byte IEEE 754)   |
      +------------+------------------------------------------------+
      | 0xff       | "break" stop code                              |
      +------------+------------------------------------------------+

                    Table 7: Jump Table for Initial Byte
```

## Appendix C. Pseudocode

Well-formedness definition, prerequisites, and pseudocode, complete and verbatim (Appendix C):

```text
   The well-formedness of a CBOR item can be checked by the pseudocode
   in Figure 1.  The data is well-formed if and only if:

   *  the pseudocode does not "fail";

   *  after execution of the pseudocode, no bytes are left in the input
      (except in streaming applications).

   The pseudocode has the following prerequisites:

   *  take(n) reads n bytes from the input data and returns them as a
      byte string.  If n bytes are no longer available, take(n) fails.

   *  uint() converts a byte string into an unsigned integer by
      interpreting the byte string in network byte order.

   *  Arithmetic works as in C.

   *  All variables are unsigned integers of sufficient range.

   Note that "well_formed" returns the major type for well-formed
   definite-length items, but 99 for an indefinite-length item (or -1
   for a "break" stop code, only if "breakable" is set).  This is used
   in "well_formed_indefinite" to ascertain that indefinite-length
   strings only contain definite-length strings as chunks.

   well_formed(breakable = false) {
     // process initial bytes
     ib = uint(take(1));
     mt = ib >> 5;
     val = ai = ib & 0x1f;
     switch (ai) {
       case 24: val = uint(take(1)); break;
       case 25: val = uint(take(2)); break;
       case 26: val = uint(take(4)); break;
       case 27: val = uint(take(8)); break;
       case 28: case 29: case 30: fail();
       case 31:
         return well_formed_indefinite(mt, breakable);
     }
     // process content
     switch (mt) {
       // case 0, 1, 7 do not have content; just use val
       case 2: case 3: take(val); break; // bytes/UTF-8
       case 4: for (i = 0; i < val; i++) well_formed(); break;
       case 5: for (i = 0; i < val*2; i++) well_formed(); break;
       case 6: well_formed(); break;     // 1 embedded data item
       case 7: if (ai == 24 && val < 32) fail(); // bad simple
     }
     return mt;                    // definite-length data item
   }

   well_formed_indefinite(mt, breakable) {
     switch (mt) {
       case 2: case 3:
         while ((it = well_formed(true)) != -1)
           if (it != mt)           // need definite-length chunk
             fail();               //    of same type
         break;
       case 4: while (well_formed(true) != -1); break;
       case 5: while (well_formed(true) != -1) well_formed(); break;
       case 7:
         if (breakable)
           return -1;              // signal break out
         else fail();              // no enclosing indefinite
       default: fail();            // wrong mt
     }
     return 99;                    // indefinite-length data item
   }

               Figure 1: Pseudocode for Well-Formedness Check
```

- (Appendix C) "Note that the remaining complexity of a complete CBOR decoder is about presenting data that has been decoded to the application in an appropriate form."
- (Appendix C) "See Section 1.2 for some specific assumptions about the profile of the C language used in these pieces of code."

Signed-integer encoding pseudocode, verbatim (Appendix C, Figure 2):

```text
   void encode_sint(int64_t n) {
     uint64t ui = n >> 63;    // extend sign to whole length
     unsigned mt = ui & 0x20; // extract (shifted) major type
     ui ^= n;                 // complement negatives
     if (ui < 24)
       *p++ = mt + ui;
     else if (ui < 256) {
       *p++ = mt + 24;
       *p++ = ui;
     } else
          ...

             Figure 2: Pseudocode for Encoding a Signed Integer
```

## Appendix F. Well-Formedness Errors and Examples

Taxonomy of well-formedness errors, complete and verbatim (Appendix F):

```text
   There are three basic kinds of well-formedness errors that can occur
   in decoding a CBOR data item:

   Too much data:  There are input bytes left that were not consumed.
      This is only an error if the application assumed that the input
      bytes would span exactly one data item.  Where the application
      uses the self-delimiting nature of CBOR encoding to permit
      additional data after the data item, as is done in CBOR sequences
      [RFC8742], for example, the CBOR decoder can simply indicate which
      part of the input has not been consumed.

   Too little data:  The input data available would need additional
      bytes added at their end for a complete CBOR data item.  This may
      indicate the input is truncated; it is also a common error when
      trying to decode random data as CBOR.  For some applications,
      however, this may not actually be an error, as the application may
      not be certain it has all the data yet and can obtain or wait for
      additional input bytes.  Some of these applications may have an
      upper limit for how much additional data can appear; here the
      decoder may be able to indicate that the encoded CBOR data item
      cannot be completed within this limit.

   Syntax error:  The input data are not consistent with the
      requirements of the CBOR encoding, and this cannot be remedied by
      adding (or removing) data at the end.

   In Appendix C, errors of the first kind are addressed in the first
   paragraph and bullet list (requiring "no bytes are left"), and errors
   of the second kind are addressed in the second paragraph/bullet list
   (failing "if n bytes are no longer available").  Errors of the third
   kind are identified in the pseudocode by specific instances of
   calling fail(), in order:

   *  a reserved value is used for additional information (28, 29, 30)

   *  major type 7, additional information 24, value < 32 (incorrect)

   *  incorrect substructure of indefinite-length byte string or text
      string (may only contain definite-length strings of the same major
      type)

   *  "break" stop code (major type 7, additional information 31) occurs
      in a value position of a map or except at a position directly in
      an indefinite-length item where also another enclosed data item
      could occur

   *  additional information 31 used with major type 0, 1, or 6
```

### Appendix F.1 Examples of CBOR Data Items That Are Not Well-Formed

Complete and verbatim (Appendix F.1):

```text
   This subsection shows a few examples for CBOR data items that are not
   well-formed.  Each example is a sequence of bytes, each shown in
   hexadecimal; multiple examples in a list are separated by commas.

   Examples for well-formedness error kind 1 (too much data) can easily
   be formed by adding data to a well-formed encoded CBOR data item.

   Similarly, examples for well-formedness error kind 2 (too little
   data) can be formed by truncating a well-formed encoded CBOR data
   item.  In test suites, it may be beneficial to specifically test with
   incomplete data items that would require large amounts of addition to
   be completed (for instance by starting the encoding of a string of a
   very large size).

   A premature end of the input can occur in a head or within the
   enclosed data, which may be bare strings or enclosed data items that
   are either counted or should have been ended by a "break" stop code.

   End of input in a head:  18, 19, 1a, 1b, 19 01, 1a 01 02, 1b 01 02 03
      04 05 06 07, 38, 58, 78, 98, 9a 01 ff 00, b8, d8, f8, f9 00, fa 00
      00, fb 00 00 00

   Definite-length strings with short data:  41, 61, 5a ff ff ff ff 00,
      5b ff ff ff ff ff ff ff ff 01 02 03, 7a ff ff ff ff 00, 7b 7f ff
      ff ff ff ff ff ff 01 02 03

   Definite-length maps and arrays not closed with enough items:  81, 81
      81 81 81 81 81 81 81 81, 82 00, a1, a2 01 02, a1 00, a2 00 00 00

   Tag number not followed by tag content:  c0

   Indefinite-length strings not closed by a "break" stop code:  5f 41
      00, 7f 61 00

   Indefinite-length maps and arrays not closed by a "break" stop
   code:  9f, 9f 01 02, bf, bf 01 02 01 02, 81 9f, 9f 80 00, 9f 9f 9f 9f
      9f ff ff ff ff, 9f 81 9f 81 9f 9f ff ff ff

   A few examples for the five subkinds of well-formedness error kind 3
   (syntax error) are shown below.

   Subkind 1:
      Reserved additional information values:  1c, 1d, 1e, 3c, 3d, 3e,
         5c, 5d, 5e, 7c, 7d, 7e, 9c, 9d, 9e, bc, bd, be, dc, dd, de, fc,
         fd, fe,

   Subkind 2:
      Reserved two-byte encodings of simple values:  f8 00, f8 01, f8
         18, f8 1f

   Subkind 3:
      Indefinite-length string chunks not of the correct type:  5f 00
         ff, 5f 21 ff, 5f 61 00 ff, 5f 80 ff, 5f a0 ff, 5f c0 00 ff, 5f
         e0 ff, 7f 41 00 ff

      Indefinite-length string chunks not definite length:  5f 5f 41 00
         ff ff, 7f 7f 61 00 ff ff

   Subkind 4:
      Break occurring on its own outside of an indefinite-length
      item:  ff

      Break occurring in a definite-length array or map or a tag:  81
         ff, 82 00 ff, a1 ff, a1 ff 00, a1 00 ff, a2 00 00 ff, 9f 81 ff,
         9f 82 9f 81 9f 9f ff ff ff ff

      Break in an indefinite-length map that would lead to an odd
      number of items (break in a value position):  bf 00 ff, bf 00 00
         00 ff

   Subkind 5:
      Major type 0, 1, 6 with additional information 31:  1f, 3f, df
```
