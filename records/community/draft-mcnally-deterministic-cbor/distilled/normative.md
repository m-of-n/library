---
record: draft-mcnally-deterministic-cbor
kind: normative
title: "draft-mcnally-deterministic-cbor — normative statements"
extracted: "2026-10-16"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: "dCBOR: Deterministic CBOR", draft-mcnally-deterministic-cbor-18, W. McNally, C. Allen (Blockchain Commons), C. Bormann (Universität Bremen TZI), L. Lundblade (Security Theory LLC), Internet-Draft, Intended status: Standards Track, 10 August 2026, expires 11 February 2027. Quotations are verbatim from the plain-text source. Blocks that reproduce tables, lists, structures, or pseudocode preserve the source's own line breaks and indentation inside fenced blocks; page headers, footers and form feeds that interrupt a block are the only lines omitted from one. Bullet locators name the section and, for the numbered rule lists of §2, the source's own role heading and item number. Dropped as non-normative: §1's opening motivation, §4 Implementation Status, the rationale prose of §8.1-§8.6 (except the statements reproduced below), §9 References, Acknowledgments, Authors' Addresses, and the "About This Document" / "Status of This Memo" / "Copyright Notice" boilerplate.

## §1. Introduction

- (§1) "This document narrows CBOR to a set of requirements called "dCBOR"."
- (§1) "These requirements include choices left open in CBOR, but also go beyond, including requiring that dCBOR decoders validate that encoded CBOR conforms to the requirements of this document."

### §1.1. Conventions and Definitions

- (§1.1) "The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here."

## §2. Narrowing Rules

- (§2) "This section is normative and specifies the exclusions and reductions that dCBOR applies to CBOR, thereby narrowing the set of data items allowed that are drawn from CBOR’s basic generic data model."
- (§2) "The rules specified here do not "fork" CBOR: A dCBOR implementation produces well-formed, deterministically encoded CBOR according to [RFC8949], and existing CBOR decoders will therefore be able to decode it."
- (§2) "Similarly, CBOR encoders will be able to produce valid dCBOR if handed dCBOR-conforming data model level information from an application."
- (§2) "Note that the separation between standard CBOR processing and the processing required by the dCBOR rules is a conceptual one: Both dCBOR processing and standard CBOR processing may be combined into a unified dCBOR/CBOR codec."
- (§2) "The requirements in this document apply to encoding or decoding of dCBOR data, regardless of whether the codec is a unified dCBOR/CBOR codec operating in dCBOR-compliant modes, or a single-purpose dCBOR codec."
- (§2) "Both of these are generically referred to as "dCBOR codecs" in this document."
- (§2) "A CBOR data item is considered to conform to dCBOR only if every CBOR data item nested within it, recursively (including array elements, map keys and values, and the contents of tagged data items), also conforms to the narrowing rules in this section."
- (§2) "dCBOR is intended to be used in conjunction with an application, which typically will use a subset of CBOR, which in turn influences which subset of dCBOR that is used."
- (§2) "As a result, dCBOR places no direct requirement on what subset of CBOR is implemented."
- (§2) "For instance, there is no requirement that dCBOR implementations support floating point numbers (or any other kind of non-basic integer type, such as arbitrary precision integers or complex numbers) when they are used with applications that do not use them."
- (§2) "However, this document does place requirements on dCBOR implementations that support 64-bit integers and 64-bit or smaller floating point numbers."

### §2.1. Definite Length Items

- (§2.1) "CBOR [RFC8949] allows both "definite-length" and "indefinite-length" items for byte strings, text strings, arrays, and maps (§3.2)."
- (§2.1 dCBOR encoders, 1) "MUST only emit "definite-length" items for byte strings, text strings, arrays, and maps."
- (§2.1 dCBOR decoders, 2) "MUST reject any encoded "indefinite-length" items for byte strings, text strings, arrays, and maps."

```text
   dCBOR encoders:

   1.  MUST only emit "definite-length" items for byte strings, text
       strings, arrays, and maps.

   dCBOR decoders:

   2.  MUST reject any encoded "indefinite-length" items for byte
       strings, text strings, arrays, and maps.
```

### §2.2. Preferred Serialization

- (§2.2) "CBOR [RFC8949] allows multiple possible encodings for the same data item, and defines a "preferred serialization" in §4.1 to be used for deterministic encoding."
- (§2.2 dCBOR encoders, 1) "MUST only emit "preferred serialization"."
- (§2.2 dCBOR decoders, 2) "MUST validate that encoded CBOR conforms to "preferred serialization", and reject any encoded CBOR that does not conform."

```text
   dCBOR encoders:

   1.  MUST only emit "preferred serialization".

   dCBOR decoders:

   2.  MUST validate that encoded CBOR conforms to "preferred
       serialization", and reject any encoded CBOR that does not
       conform.
```

### §2.3. Ordered Map Keys

- (§2.3) "The last bullet item of CBOR [RFC8949] §4.2.1 defines a "bytewise lexicographic order" for map keys to be used for deterministic encoding."
- (§2.3 dCBOR encoders, 1) "MUST only emit CBOR maps with keys in "bytewise lexicographic order"."
- (§2.3 dCBOR decoders, 2) "MUST validate that encoded CBOR maps have keys in "bytewise lexicographic order", and reject any encoded maps that do not conform."

```text
   dCBOR encoders:

   1.  MUST only emit CBOR maps with keys in "bytewise lexicographic
       order".

   dCBOR decoders:

   2.  MUST validate that encoded CBOR maps have keys in "bytewise
       lexicographic order", and reject any encoded maps that do not
       conform.
```

### §2.4. Duplicate Map Keys

- (§2.4) "CBOR [RFC8949] defines maps with duplicate keys as invalid, but leaves how to handle such cases to the implementor (§2.2, §3.1, §5.4, §5.6)."
- (§2.4 dCBOR encoders, 1) "MUST NOT emit CBOR maps that contain duplicate keys."
- (§2.4 dCBOR decoders, 2) "MUST reject encoded maps with duplicate keys."

```text
   dCBOR encoders:

   1.  MUST NOT emit CBOR maps that contain duplicate keys.

   dCBOR decoders:

   2.  MUST reject encoded maps with duplicate keys.
```

### §2.5. Numeric Reduction

- (§2.5) "The purpose of determinism is to ensure that semantically equivalent data items are encoded into identical byte streams."
- (§2.5) "Numeric Reduction ensures that semantically equal numeric values (e.g. 2 and 2.0) are encoded into identical byte streams (e.g. 0x02) by encoding "Integral floating point values" (floating point values with a zero fractional part) as integers when possible."
- (§2.5 dCBOR implementations that support floating point numbers, 1) "MUST check whether floating point values to be encoded have the numerically equal value in DCBOR_INT = [-2^63, 2^64-1]."
- (§2.5 dCBOR implementations that support floating point numbers, 1) "If that is the case, it MUST be converted to that numerically equal integer value before encoding it."
- (§2.5 dCBOR implementations that support floating point numbers, 1) "(Preferred encoding will then ensure the shortest length encoding is used.)"
- (§2.5 dCBOR implementations that support floating point numbers, 1) "If a floating point value has a non-zero fractional part, or an exponent that takes it out of DCBOR_INT, the original floating point value is used for encoding."
- (§2.5 dCBOR implementations that support floating point numbers, 1) "(Specifically, conversion to a CBOR bignum is never considered.)"
- (§2.5 dCBOR implementations that support floating point numbers, 1) "This also means that the three representations of a zero number in CBOR (0, 0.0, -0.0 in diagnostic notation) are all reduced to the basic integer 0 (with preferred encoding 0x00)."
- (§2.5 dCBOR implementations that support floating point numbers, 2) "MUST reduce all encoded NaN values to the quiet NaN value having the half-width CBOR representation 0xf97e00."
- (§2.5 dCBOR decoders that support floating point numbers, 3) "MUST reject any encoded floating point values that are not encoded according to the above rules."
- (§2.5) "For the purposes of this document, the dCBOR numeric model comprises only untagged integers and untagged floating point values in the CBOR basic generic data model (major types 0, 1, and 7 as defined in [RFC8949] and by the type number in [RFC8610])."
- (§2.5) "Numeric Reduction and the duplicate-key considerations in this section apply only to such untagged numeric values, wherever they occur in a dCBOR data item."
- (§2.5) "Tagged data items themselves are not part of the dCBOR numeric model: two tagged data items are equal in dCBOR only if both their tag numbers and their enclosed CBOR data items are equal, and no tagged data item is ever considered numerically equal to an untagged data item."

The rule list of §2.5, with its indented aside and Figures 1 and 2. The aside's
own statements are quoted only here, inside the block, because the source sets
them as an indented aside whose every line carries a "|" marker:

```text
   dCBOR implementations that support floating point numbers:

   1.  MUST check whether floating point values to be encoded have the
       numerically equal value in DCBOR_INT = [-2^63, 2^64-1].  If that
       is the case, it MUST be converted to that numerically equal
       integer value before encoding it.  (Preferred encoding will then
       ensure the shortest length encoding is used.)  If a floating
       point value has a non-zero fractional part, or an exponent that
       takes it out of DCBOR_INT, the original floating point value is
       used for encoding.  (Specifically, conversion to a CBOR bignum is
       never considered.)

       This also means that the three representations of a zero number
       in CBOR (0, 0.0, -0.0 in diagnostic notation) are all reduced to
       the basic integer 0 (with preferred encoding 0x00).

      |  Note that Numeric Reduction means that some maps that are valid
      |  CBOR cannot be reduced to valid dCBOR maps, as Numeric
      |  Reduction can result in multiple entries with the same keys
      |  ("duplicate keys").  For example, the following is a valid CBOR
      |  map:
      |  
      |     {
      |        10: "ten",
      |        10.0: "floating ten"
      |     }
      |  
      |         Figure 1: Valid CBOR data item with numeric map keys
      |  
      |  Applying Numeric Reduction to this map would yield the invalid
      |  map:
      |  
      |     {  / invalid: multiple entries with the same key /
      |        10: "ten",
      |        10: "floating ten"
      |     }
      |  
      |         Figure 2: Numeric Reduction turns valid CBOR invalid
      |  
      |  In general, dCBOR applications need to avoid maps that have
      |  entries with keys that are semantically equivalent in dCBOR's
      |  numeric model.

   2.  MUST reduce all encoded NaN values to the quiet NaN value having
       the half-width CBOR representation 0xf97e00.

   dCBOR decoders that support floating point numbers:

   3.  MUST reject any encoded floating point values that are not
       encoded according to the above rules.
```

### §2.6. Simple Values

- (§2.6) "Only the three "simple" (major type 7) values false (0xf4), true (0xf5), and null (0xf6) and the floating point values are valid in dCBOR."
- (§2.6 dCBOR encoders, 1) "MUST NOT encode major type 7 values other than false, true, null, and the floating point values."
- (§2.6 dCBOR decoders, 2) "MUST reject any encoded major type 7 values other than false, true, null, and the floating point values."

```text
   dCBOR encoders:

   1.  MUST NOT encode major type 7 values other than false, true, null,
       and the floating point values.

   dCBOR decoders:

   2.  MUST reject any encoded major type 7 values other than false,
       true, null, and the floating point values.
```

### §2.7. Strings

- (§2.7) "CBOR [RFC8949] allows text strings to be any valid UTF-8 string (§3.1)."
- (§2.7) "However, Unicode character sequences can represent the same text string in different ways, leading to variability in the encoding of semantically equivalent data items."
- (§2.7) "Unicode Normalization Form C (NFC) [UNICODE-NORM] is a commonly used normalization form that eliminates such variability."
- (§2.7 dCBOR encoders, 1) "MUST only emit text strings that are in NFC."
- (§2.7 dCBOR decoders, 1) "MUST reject any encoded text strings that are not in NFC."

The decoder item is numbered "1." in the source, not "2." as in §2.1-§2.6; the list is reproduced unaltered:

```text
   dCBOR encoders:

   1.  MUST only emit text strings that are in NFC.

   dCBOR decoders:

   1.  MUST reject any encoded text strings that are not in NFC.
```

## §3. CDDL support, Declarative Tag

- (§3) "CDDL [RFC8610] is a widely used language for specifying CBOR data models."
- (§3) "This specification adds two CDDL control operators that can be used to specify that the data items should be encoded in dCBOR."
- (§3) "The control operators .dcbor and .dcborseq are exactly like .cbor and .cborseq as defined in [RFC8610] except that they also require the encoded data item(s) to conform to dCBOR."
- (§3) "The CDDL Standard Prelude as defined in [RFC8610] Appendix D defines:"

```text
   number = int / float
```

- (§3) "This type encompasses the full space of CBOR numeric values representable by CBOR major types 0, 1, and 7."
- (§3) "Therefore dCBOR applications can use number to specify fields with numeric values, and dCBOR's Numeric Reduction ensures that these values are encoded deterministically."
- (§3) "Tag 201 (Section 6) is defined in this specification as a way to declare its tag content to conform to dCBOR at the data model level and the encoded data item level."
- (§3) "(In conjunction with these semantics, tag 201 may also be employed as a boundary marker leading from an overall structure to specific application data items; see Section 3 of [GordianEnvelope] for an example for this usage.)"

## §5. Security Considerations

- (§5) "This document inherits the security considerations of CBOR [RFC8949]."
- (§5) "Vulnerabilities regarding dCBOR will revolve around whether an attacker can find value in producing semantically equivalent documents that are nonetheless serialized into non-identical byte streams."
- (§5) "Such documents could be used to contain malicious payloads or exfiltrate sensitive data."
- (§5) "The ability to create such documents could indicate the failure of a dCBOR decoder to correctly validate according to this document, or the failure of the developer to properly specify or implement application protocol requirements using dCBOR."
- (§5) "Whether these possibilities present an identifiable attack surface is a question that developers should consider."

## §6. IANA Considerations

- (§6) "RFC Editor: please replace RFCXXXX with the RFC number of this RFC and remove this note."
- (§6) "IANA has registered the following CBOR tag in the "CBOR Tags" registry of [IANACBORTAGS]:"

```text
             +======+===========+================+===========+
             | Tag  | Data Item | Semantics      | Reference |
             +======+===========+================+===========+
             | #201 | (any)     | enclosed dCBOR | [RFCXXXX] |
             +------+-----------+----------------+-----------+

                        Table 1: CBOR Tag for dCBOR
```

- (§6) "This document requests IANA to register the contents of Table 1 into the registry "CDDL Control Operators" of [IANACDDL]:"

```text
                         +===========+===========+
                         | Name      | Reference |
                         +===========+===========+
                         | .dcbor    | [RFCXXXX] |
                         +-----------+-----------+
                         | .dcborseq | [RFCXXXX] |
                         +-----------+-----------+

                           Table 2: CDDL Control
                            Operators for dCBOR
```

## §7. Appendix A: dCBOR Numeric Test Vectors

- (§7) "The following tables provide common and edge-case numeric test vectors for dCBOR encoders and decoders, and are intended to exercise the requirements of this specification."

### §7.1. dCBOR Numeric Encodings

```text
   +=========================+====================+====================+
   | Value                   | dCBOR Encoding     | Note               |
   +=========================+====================+====================+
   | 0                       | 00                 |                    |
   +-------------------------+--------------------+--------------------+
   | 1                       | 01                 |                    |
   +-------------------------+--------------------+--------------------+
   | 23                      | 17                 |                    |
   +-------------------------+--------------------+--------------------+
   | 24                      | 1818               |                    |
   +-------------------------+--------------------+--------------------+
   | 255 (2^8 - 1)           | 18ff               |                    |
   +-------------------------+--------------------+--------------------+
   | 65535 (2^16 - 1)        | 19ffff             |                    |
   +-------------------------+--------------------+--------------------+
   | 65536 (2^16)            | 1a00010000         |                    |
   +-------------------------+--------------------+--------------------+
   | 4294967295 (2^32 - 1)   | 1affffffff         |                    |
   +-------------------------+--------------------+--------------------+
   | 4294967296 (2^32)       | 1b0000000100000000 |                    |
   +-------------------------+--------------------+--------------------+
   | 18446744073709551615    | 1bffffffffffffffff |                    |
   | (2^64 - 1)              |                    |                    |
   +-------------------------+--------------------+--------------------+
   | -1                      | 20                 |                    |
   +-------------------------+--------------------+--------------------+
   | -2                      | 21                 |                    |
   +-------------------------+--------------------+--------------------+
   | -127 (-2^8 - 1)         | 387e               |                    |
   +-------------------------+--------------------+--------------------+
   | -128 (-2^7)             | 387f               |                    |
   +-------------------------+--------------------+--------------------+
   | -32768 (-2^16)          | 397fff             |                    |
   +-------------------------+--------------------+--------------------+
   | -2147483648 (-2^31)     | 3a7fffffff         |                    |
   +-------------------------+--------------------+--------------------+
   | -9223372036854775808    | 3b7fffffffffffffff |                    |
   | (-2^63)                 |                    |                    |
   +-------------------------+--------------------+--------------------+
   | 1.5                     | f93e00             |                    |
   +-------------------------+--------------------+--------------------+
   | 2345678.25              | fa4a0f2b39         |                    |
   +-------------------------+--------------------+--------------------+
   | 1.2                     | fb3ff3333333333333 |                    |
   +-------------------------+--------------------+--------------------+
   | 42.0                    | 182a               | Reduced.           |
   +-------------------------+--------------------+--------------------+
   | 2345678.0               | 1a0023cace         | Reduced.           |
   +-------------------------+--------------------+--------------------+
   | -2345678.0              | 3a0023cacd         | Reduced.           |
   +-------------------------+--------------------+--------------------+
   | -0.0                    | 00                 | Reduced.           |
   +-------------------------+--------------------+--------------------+
   | 5.960464477539063e-08   | f90001             | Smallest half-     |
   |                         |                    | precision          |
   |                         |                    | subnormal.         |
   +-------------------------+--------------------+--------------------+
   | 1.401298464324817e-45   | fa00000001         | Smallest single    |
   |                         |                    | subnormal.         |
   +-------------------------+--------------------+--------------------+
   | 5e-324                  | fb0000000000000001 | Smallest double    |
   |                         |                    | subnormal.         |
   +-------------------------+--------------------+--------------------+
   | 2.2250738585072014e-308 | fb0010000000000000 | Smallest double    |
   |                         |                    | normal.            |
   +-------------------------+--------------------+--------------------+
   | 6.103515625e-05         | f90400             | Smallest half-     |
   |                         |                    | precision normal.  |
   +-------------------------+--------------------+--------------------+
   | 65504.0                 | 19ffe0             | Reduced.  Largest  |
   |                         |                    | possible half-     |
   |                         |                    | precision.         |
   +-------------------------+--------------------+--------------------+
   | 33554430.0              | 1a01fffffe         | Reduced.           |
   |                         |                    | Exponent 24 to     |
   |                         |                    | test single        |
   |                         |                    | exponent           |
   |                         |                    | boundary.          |
   +-------------------------+--------------------+--------------------+
   | -9223372036854774784.0  | 3b7ffffffffffffbff | Reduced.  Most     |
   |                         |                    | negative double    |
   |                         |                    | that converts to   |
   |                         |                    | int64.             |
   +-------------------------+--------------------+--------------------+
   | 18446744073709550000.0  | 1bfffffffffffff800 | Reduced.  Largest  |
   |                         |                    | double that can    |
   |                         |                    | convert to         |
   |                         |                    | uint64, almost     |
   |                         |                    | UINT64_MAX.        |
   +-------------------------+--------------------+--------------------+
   | 18446744073709552000.0  | fa5f800000         | Just too large to  |
   |                         |                    | convert to         |
   |                         |                    | uint64, but        |
   |                         |                    | converts to a      |
   |                         |                    | single, just over  |
   |                         |                    | UINT64_MAX.        |
   +-------------------------+--------------------+--------------------+
   | -18446742974197924000.0 | fadf7fffff         | Large negative     |
   |                         |                    | that converts to   |
   |                         |                    | float, but too     |
   |                         |                    | large for int64.   |
   +-------------------------+--------------------+--------------------+
   | 3.4028234663852886e+38  | fa7f7fffff         | Largest possible   |
   |                         |                    | single.            |
   +-------------------------+--------------------+--------------------+
   | 3.402823466385289e+38   | fb47efffffe0000001 | Slightly larger    |
   |                         |                    | than largest       |
   |                         |                    | possible single.   |
   +-------------------------+--------------------+--------------------+
   | 1.7976931348623157e+308 | fb7fefffffffffffff | Largest double.    |
   +-------------------------+--------------------+--------------------+
   | Infinity (any size)     | f97c00             | Canonicalized.     |
   +-------------------------+--------------------+--------------------+
   | -Infinity (any size)    | f9fc00             | Canonicalized.     |
   +-------------------------+--------------------+--------------------+
   | NaN (any size, any      | f97e00             | Canonicalized.     |
   | payload)                |                    |                    |
   +-------------------------+--------------------+--------------------+

                                  Table 3
```

### §7.2. Invalid dCBOR Encodings

- (§7.2) "These are valid CBOR encodings that MUST be rejected as invalid by a dCBOR-compliant decoder."

```text
   +=======================+====================+======================+
   | Value                 | CBOR Encoding      | Reason for           |
   |                       |                    | Rejection            |
   +=======================+====================+======================+
   | 12.0                  | f94a00             | Can be reduced       |
   |                       |                    | to 12.               |
   +-----------------------+--------------------+----------------------+
   | 1.5                   | fb3ff8000000000000 | Not preferred        |
   |                       |                    | encoding.            |
   +-----------------------+--------------------+----------------------+
   | -9223372036854775809  | 3b8000000000000000 | 65-bit negative      |
   | (-2^63 - 1)           |                    | integer value.       |
   +-----------------------+--------------------+----------------------+
   | -18446744073709551616 | 3bffffffffffffffff | 65-bit negative      |
   | (-2^64)               |                    | integer value.       |
   +-----------------------+--------------------+----------------------+
   | Infinity              | fb7ff0000000000000 | Not preferred        |
   |                       |                    | encoding.            |
   +-----------------------+--------------------+----------------------+
   | Infinity              | fa7f800000         | Not preferred        |
   |                       |                    | encoding.            |
   +-----------------------+--------------------+----------------------+
   | -Infinity             | fbfff0000000000000 | Not preferred        |
   |                       |                    | encoding.            |
   +-----------------------+--------------------+----------------------+
   | -Infinity             | faff800000         | Not preferred        |
   |                       |                    | encoding.            |
   +-----------------------+--------------------+----------------------+
   | NaN                   | fb7ff9100000000001 | Not canonical        |
   |                       |                    | NaN.                 |
   +-----------------------+--------------------+----------------------+
   | NaN                   | faffc00001         | Not canonical        |
   |                       |                    | NaN.                 |
   +-----------------------+--------------------+----------------------+
   | NaN                   | f97e01             | Not canonical        |
   |                       |                    | NaN.                 |
   +-----------------------+--------------------+----------------------+

                                  Table 4
```

## §8. Appendix B: Design Principles

The source declares this appendix non-normative. Reproduced here: its own
statement of that status, its scoping statements, its summary table of the
narrowing rules, and the BCP 14 statement it quotes from [RFC8949] §3.4.2. The
rationale prose of §8.1-§8.6 is not normative text.

- (§8) "This section is non-normative."

```text
   +=====================================+============================+
   | Variability Source                  | dCBOR Rule                 |
   +=====================================+============================+
   | Indefinite or definite length items | Only definite Length Items |
   +-------------------------------------+----------------------------+
   | Multiple possible encodings for     | Only preferred             |
   | same data item                      | serialization              |
   +-------------------------------------+----------------------------+
   | Different orders for map keys       | Only ordered map Keys      |
   +-------------------------------------+----------------------------+
   | Duplicate map keys                  | Duplicate Map Keys         |
   |                                     | disallowed                 |
   +-------------------------------------+----------------------------+
   | Semantically equivalent numeric     | Only a single encoding for |
   | values (e.g., 0, 0.0, -0.0)         | each distinct value        |
   +-------------------------------------+----------------------------+
   | Choice of null or undefined         | Only null                  |
   +-------------------------------------+----------------------------+
   | Simple values other than false,     | Only false, true, null     |
   | true, null                          |                            |
   +-------------------------------------+----------------------------+
   | Nontrivial NaNs (sign, signaling,   | Single NaN                 |
   | payloads)                           |                            |
   +-------------------------------------+----------------------------+
   | Equivalent strings with multiple    | Only NFC text strings      |
   | Unicode representations             |                            |
   +-------------------------------------+----------------------------+

                                 Table 5
```

- (§8.1) "For example, §3.4.2 defines Tag 1 as "Epoch-Based Date/Time":"
- (§8.1, quoting [RFC8949] §3.4.2) "The tag content MUST be an unsigned or negative integer (major types 0 and 1) or a floating-point number (major type 7 with additional information 25, 26, or 27)."
- (§8.1, quoting [RFC8949] §3.4.2) "Other contained types are invalid."

```text
      Tag number 1 contains a numerical value counting the number of
      seconds from 1970-01-01T00:00Z in UTC time to the represented
      point in civil time.

      The tag content MUST be an unsigned or negative integer (major
      types 0 and 1) or a floating-point number (major type 7 with
      additional information 25, 26, or 27).  Other contained types are
      invalid.
```

- (§8.5) "As a result, dCBOR does not place requirements on the encoding or decoding of CBOR data items that are less commonly used in practice, such as bignums, complex numbers, or other tagged data items."
- (§8.5) "dCBOR implementations are not required to support these data items, but if they do, they must support them within the rules of dCBOR."
- (§8.5) "For example, dCBOR applications can freely use Tag 2 or Tag 3 to encode bignums, which contain byte strings, and on which dCBOR places no restrictions beyond those that apply to all byte strings (definite length only)."
- (§8.5) "Similarly, the rare applications that need to convey nontrivial NaN values can use Tag 80, 81, or 82 as defined in the IANA CBOR Tags Registery [IANACBORTAGS]."
- (§8.5) "These tags use byte strings to encode arrays of fixed-length IEEE 754 floating point values in big-endian byte order."
