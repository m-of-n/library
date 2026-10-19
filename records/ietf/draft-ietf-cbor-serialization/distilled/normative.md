---
record: draft-ietf-cbor-serialization
kind: normative
title: "draft-ietf-cbor-serialization — normative statements"
extracted: "2026-10-16"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: "CBOR Serialization and Determinism", draft-ietf-cbor-serialization-08, L. Lundblade, Security Theory LLC, 29 July 2026; document header states "Intended status: Standards Track" and "Expires: 30 January 2027". Quotations are verbatim from the plain-text source. Blocks that reproduce tables, lists, structures, code or pseudocode preserve the source's own line breaks and indentation inside fenced blocks. Where such a block spans a page boundary in the source it appears as consecutive fenced blocks, with only the running page header/footer falling between them. In the inline quotations the source's hard line wraps inside a sentence are rendered as single spaces, except where the source wraps immediately after a hyphen or a solidus inside a word, where the word is rejoined without a space. Six inline quotations rely on that rejoining — "definite-" / "length" (§4.1 item 3), "floating-" / "point" (App. B), "preferred-" / "plus" (§2.2.1 and §4.3), "COSE-" / "based" (§2.2.2) and "half-" / "precision" (App. D) — and one on the solidus form, "signer/" / "sender" (App. K.1). No quotation in this file crosses a page boundary. No other character is altered. "Status of This Memo", "Copyright Notice", the Table of Contents, "About This Document" (which the source marks "This note is to be removed before publishing as an RFC."), §11.2 (Informative References), Contributors and the Author's Address are omitted, as are the two `//`-prefixed editorial asides to the author and the RFC Editor in §7 and §10. §1, §1.1 and §1.2 are motivation and are omitted apart from Table 1; §1.3, which states this document's normative relation to RFC 8949, is kept. Appendix C.2 ("Implementation Support for Non-Trivial NaNs", source lines 1327-1367) is also omitted in full: it is a survey of programming-language and CPU support for NaN payloads, it carries no BCP 14 keyword and no obligation of any form, and nothing in the document cross-references it. Declared here because pass 1 omitted it without saying so. Appendix I declares itself non-normative and says so verbatim below; its guidance is reproduced anyway. The source carries no BCP 14 / RFC 8174 boilerplate paragraph and no Conventions section, yet uses 65 uppercase keywords and cites [RFC2119] as a normative reference — see "Source defects" at the end.

## Document header

```text
CBOR                                                        L. Lundblade
Internet-Draft                                       Security Theory LLC
Intended status: Standards Track                            29 July 2026
Expires: 30 January 2027


                   CBOR Serialization and Determinism
                    draft-ietf-cbor-serialization-08
```


## §1. Introduction

The body of §1 is motivation and is omitted. Table 1 is reproduced because it fixes the two encodings of `[1, 2]` that the rest of the document reasons from.

```text
       +===================+==========================+===========+
       | Type              | Description              | Bytes     |
       +===================+==========================+===========+
       | Definite-length   | The array length (2) is  | 0x82 0x01 |
       |                   | encoded at the beginning | 0x02      |
       +-------------------+--------------------------+-----------+
       | Indefinite-length | The array is terminated  | 0x9f 0x01 |
       |                   | by the break byte (0xff) | 0x02 0xff |
       +-------------------+--------------------------+-----------+

          Table 1: [1, 2] definite-length and indefinite-length
                              serializations
```


## §1.3. Relation to RFC 8949

- (§1.3) "This document defines new serializations rather than updating those in [STD94]."
- (§1.3) "This approach enables the serialization requirements to be expressed directly in normative [RFC2119] language and to be defined entirely in this document."
- (§1.3) "The serializations defined herein are formally new but largely interchangeable with the way the serializations described in [STD94] are implemented."
- (§1.3) "For example, preferred serialization (Section 4.1 of [STD94]) is commonly implemented without support for indefinite lengths."
- (§1.3) "Preferred-plus serialization is effectively the same as preferred serialization without indefinite lengths, so it is largely interchangeable with what is commonly implemented."

## §2. Recommendations Summary

## §2.1. Protocol Specifications

## §2.1.1. Framework Protocols

- (§2.1.1) "Framework protocols are those that offer a set of options and alternatives, with interoperability depending on the sender and receiver making compatible choices."
- (§2.1.1) "CWT, COSE, EAT, and CBOR itself are examples of framework protocols."
- (§2.1.1) "It is RECOMMENDED that CBOR-based framework protocols not state serialization requirements, enabling individual uses and profiles to choose serialization to suit their environments and constraints."
- (§2.1.1) "CBOR-based framework protocols MAY impose serialization requirements."
- (§2.1.1) "For example, if a protocol is never expected to be deployed in constrained environments where map sorting is too expensive, it may mandate deterministic serialization for all implementations in order to eliminate all serialization variability."
- (§2.1.1) "There is one situation in which a framework protocol MUST require deterministic serialization, though typically limited to a specific subset of the protocol.  This requirement arises when the protocol design requires the involved parties to independently construct and serialize data to be hashed or signed, rather than transmitting the exact serialized bytes that were hashed or signed."
- (§2.1.1) "See Section 5.3."
- (§2.1.1) "See Appendix K for a COSE-based example."

## §2.1.2. End-to-End Protocols

- (§2.1.2) "End-to-end protocols are specified such that interoperability is assured when they are implemented in accordance with their specification."
- (§2.1.2) "TLS, HTTP, and FIDO are examples of end-to-end protocols."
- (§2.1.2) "End-to-end protocols MUST define a serialization strategy that ensures the sender and receiver use interoperable serialization."
- (§2.1.2) "The strategy most highly RECOMMENDED is to normatively require preferred-plus serialization."
- (§2.1.2) "If a protocol does not need to be deployed where map sorting is too expensive, requiring deterministic serialization is also RECOMMENDED."
- (§2.1.2) "An end-to-end protocol MAY instead define its own specialized serialization (see Section 6)."
- (§2.1.2) "In such cases, it MUST explicitly specify the permitted serialization behaviors necessary to ensure interoperability."
- (§2.1.2) "For example, if a sender is permitted to use indefinite-length serialization, the protocol MUST require that receivers be capable of decoding indefinite-length items."
- (§2.1.2) "As with framework protocols, deterministic serialization may be required for parts of the protocol using hashing or signing.  See Section 5.3."
- (§2.1.2) "If no specific serialization is required, general serialization (see Section 3) applies by default."
- (§2.1.2) "In this case, the sender MAY use any valid serialization, and the receiver MUST be able to decode it."
- (§2.1.2) "Defaulting to general serialization is NOT RECOMMENDED, because some serializations like indefinite-lengths are not widely supported."

## §2.2. Libraries

## §2.2.1. CBOR Libraries

- (§2.2.1) "It is RECOMMENDED that CBOR libraries support preferred-plus serialization.  This can be achieved by conforming to the decoding requirements in Section 4.2 and by making the encoding behavior defined in Section 4.1 the default or primary encoding API."
- (§2.2.1) "Preferred-plus serialization is recommended because it is suitable for the majority of CBOR-based protocols."
- (§2.2.1) "In practice, preferred-plus serialization is equivalent to preferred serialization Section 4.1 of [STD94] for most use cases."
- (§2.2.1) "It is also RECOMMENDED that CBOR libraries support deterministic serialization, as some protocols (for example, COSE) require it."
- (§2.2.1) "Relative to preferred-plus serialization, the only additional requirement for deterministic serialization is that encoded maps be sorted."
- (§2.2.1) "This recommendation is particularly strong for environments in which map sorting is easy to implement (for example, Python, Go, and Ruby)."
- (§2.2.1) "A CBOR library may choose to implement only deterministic serialization and make it the default."
- (§2.2.1) "Deterministic serialization is a superset of preferred-plus serialization; therefore, if deterministic serialization is fully supported, explicit support for preferred-plus serialization may be omitted."
- (§2.2.1) "A CBOR library MAY also choose to support some or all aspects of general serialization (see Section 3) thereby enabling support for protocols that use specialized serializations (see Section 6)."

## §2.2.2. Libraries for Framework Protocols

- (§2.2.2) "When a framework protocol specification does not mandate a specific serialization, it is RECOMMENDED that it implement preferred-plus serialization."
- (§2.2.2) "For example, it is recommended that a library implementing CWT or COSE implement preferred-plus serialization."
- (§2.2.2) "However, a library MAY choose to support only deterministic serialization if this aligns with its deployment environment and design goals."
- (§2.2.2) "When a framework protocol mandates serialization requirements, libraries must of course conform."
- (§2.2.2) "For instance, certain parts of COSE mandate deterministic serialization.  See Appendix K for a COSE-based example."

## §2.2.3. Libraries for End-to-End Protocols

- (§2.2.3) "End-to-end protocols should have explicit serialization requirements to ensure interoperability.  Libraries for end-to-end protocols should fulfill them."
- (§2.2.3) "If an end-to-end protocol specification does not state serialization requirements, the library is free to choose, but it is RECOMMENDED that they implement preferred-plus serialization."

## §3. General Serialization

- (§3) "This section assigns the name "general serialization" to the complete set of all encodings standardized in Section 3 of [STD94]."
- (§3) "The term itself was not explicitly defined in [STD94]."
- (§3) "Preferred-plus and deterministic serialization are subsets of it."

```text
   General serialization permits any and all of these:

   *  CBOR arguments of any length (for example, the integer 0 may be
      encoded as 0x00, 0x1800, or 0x190000 and so on).

   *  Floating-point values encoded at any length (for example, 0.00 can
      be 0xf90000, 0xfa00000000, and so on).

   *  Both definite or indefinite-length strings, arrays, and maps.

   *  Big number representation of values that are also representable
      using major types 0 and 1 (for example, 0 can be encoded as the
      big number 0xc34100).
```


- (§3) "A decoder claiming to support general serialization MUST accept and decode all the encodings for the data types it supports."

## §3.1. General Serialization is the Default

- (§3.1) "When a CBOR-based protocol specification does not explicitly specify serialization, general serialization is the implied requirement — meaning a compliant decoder must accept and decode any and all encodings it permits, including both definite and indefinite lengths."
- (§3.1) "CBOR Web Token [RFC8392], for example, does not specify serialization, so a fully compliant CWT decoder must handle general serialization, including indefinite-length strings, arrays, and maps."
- (§3.1) "The same pattern holds for other protocols, such as COSE [RFC9052]."

## §3.2. When To Use General Serialization

- (§3.2) "Preferred-plus serialization (Section 4) is efficient and supports the full CBOR data model (except non-trivial NaNs; see Appendix C.1), satisfying the vast majority of CBOR use cases."
- (§3.2) "The main scenario where general serialization is warranted is a protocol that must accommodate highly constrained encoders, at the cost of requiring decoders — assumed to be unconstrained — to support every possible serialization option."
- (§3.2) "When general serialization is required by a protocol, this SHOULD be stated explicitly."
- (§3.2) "Although it is the default for CBOR in theory, it has not been widely implemented as such in practice."
- (§3.2) "CBOR libraries may nonetheless wish to support general serialization, as a complete set of other serialization forms, to be useful across a broader range of protocols."

## §4. Preferred-Plus Serialization

- (§4) "This section defines a serialization named "preferred-plus serialization.""

## §4.1. Encoder Requirements

The numbered procedure verbatim. The source breaks a page between the first and the second bullet of item 1, so item 1 is reproduced as two fenced blocks.

```text
   1.  The shortest-form of the CBOR argument must be used for all major
       types.  The shortest-form encoding for any argument that is not a
       floating point value is:

       *  0 to 23 and -1 to -24 MUST be encoded in the same byte as the
          major type.
```


```text
       *  24 to 255 and -25 to -256 MUST be encoded only with an
          additional byte (ai = 0x18).

       *  256 to 65535 and -257 to -65536 MUST be encoded only with an
          additional two bytes (ai = 0x19).

       *  65536 to 4294967295 and -65537 to -4294967296 MUST be encoded
          only with an additional four bytes (ai = 0x1a).

   2.  If maps or arrays are encoded, they MUST use definite-length
       encoding (never indefinite-length).

   3.  If text or byte strings are encoded, they MUST use definite-
       length encoding (never indefinite-length).

   4.  If floating-point numbers are encoded, the following apply:

       *  Half-precision MUST be supported

       *  Values MUST be encoded in the shortest of double, single or
          half-precision that preserves precision.  For example, 0.0 can
          always be reduced to half-precision so it MUST be encoded as
          0xf90000.  For another example, 0.1 would lose precision if
          not encoded as double-precision so it MUST be encoded as
          0xfb3fb999999999999a.  Subnormal numbers MUST be supported in
          this shortest-length encoding.

       *  Encoders MUST NOT output any NaN other than the half-precision
          NaN 0xf9 0x7e 0x00 (sign bit clear, most significant
          significand bit set, all remaining significand bits clear).
          When a signaling NaN, a NaN with a non-zero payload, or a NaN
          with the sign bit set is presented to an application or
          library for encoding, the encoder MUST either reject it or
          encode it as 0xf9 0x7e 0x00.  Consequently, the floating-point
          values that can be encoded are the finite numbers, positive
          and negative infinity, and a single NaN.

       *  Aside from the requirement allowing only the half-precision
          quiet NaN, these are the same floating-point requirements as
          Section 4.1 of [STD94] and also as Section 4.2.1 of [STD94].

   5.  If big numbers (tags 2 and 3) are encoded, the following apply:

       *  Leading zeros MUST NOT be encoded.

       *  If a value can be encoded using major type 0 or 1, then it
          MUST be encoded with major type 0 or 1, never as a big number.
```


Individually, with locators:

- (§4.1 item 1) "The shortest-form of the CBOR argument must be used for all major types.  The shortest-form encoding for any argument that is not a floating point value is:"
- (§4.1 item 1) "0 to 23 and -1 to -24 MUST be encoded in the same byte as the major type."
- (§4.1 item 1) "24 to 255 and -25 to -256 MUST be encoded only with an additional byte (ai = 0x18)."
- (§4.1 item 1) "256 to 65535 and -257 to -65536 MUST be encoded only with an additional two bytes (ai = 0x19)."
- (§4.1 item 1) "65536 to 4294967295 and -65537 to -4294967296 MUST be encoded only with an additional four bytes (ai = 0x1a)."
- (§4.1 item 2) "If maps or arrays are encoded, they MUST use definite-length encoding (never indefinite-length)."
- (§4.1 item 3) "If text or byte strings are encoded, they MUST use definite-length encoding (never indefinite-length)."
- (§4.1 item 4) "If floating-point numbers are encoded, the following apply:"
- (§4.1 item 4) "Half-precision MUST be supported"
- (§4.1 item 4) "Values MUST be encoded in the shortest of double, single or half-precision that preserves precision."
- (§4.1 item 4) "For example, 0.0 can always be reduced to half-precision so it MUST be encoded as 0xf90000."
- (§4.1 item 4) "For another example, 0.1 would lose precision if not encoded as double-precision so it MUST be encoded as 0xfb3fb999999999999a."
- (§4.1 item 4) "Subnormal numbers MUST be supported in this shortest-length encoding."
- (§4.1 item 4) "Encoders MUST NOT output any NaN other than the half-precision NaN 0xf9 0x7e 0x00 (sign bit clear, most significant significand bit set, all remaining significand bits clear)."
- (§4.1 item 4) "When a signaling NaN, a NaN with a non-zero payload, or a NaN with the sign bit set is presented to an application or library for encoding, the encoder MUST either reject it or encode it as 0xf9 0x7e 0x00."
- (§4.1 item 4) "Consequently, the floating-point values that can be encoded are the finite numbers, positive and negative infinity, and a single NaN."
- (§4.1 item 4) "Aside from the requirement allowing only the half-precision quiet NaN, these are the same floating-point requirements as Section 4.1 of [STD94] and also as Section 4.2.1 of [STD94]."
- (§4.1 item 5) "If big numbers (tags 2 and 3) are encoded, the following apply:"
- (§4.1 item 5) "Leading zeros MUST NOT be encoded."
- (§4.1 item 5) "If a value can be encoded using major type 0 or 1, then it MUST be encoded with major type 0 or 1, never as a big number."

## §4.2. Decoder Requirements

```text
   1.  Decoders MUST accept shortest-form encoded arguments.

   2.  If arrays or maps are supported, definite-length arrays or maps
       MUST be accepted.

   3.  If text or byte strings are supported, definite-length text or
       byte strings MUST be accepted.

   4.  If floating-point numbers are supported, the following apply:

       *  Half-precision values MUST be accepted.

       *  Double- and single-precision values SHOULD be accepted;
          leaving these out is only foreseen for decoders that need to
          work in exceptionally constrained environments.

       *  If double-precision values are accepted, single-precision
          values MUST be accepted.

   5.  If big numbers (tags 2 and 3) are accepted, the following apply:

       *  Big numbers described in Section 3.4.3 of [STD94] MUST be
          accepted.

       *  Leading zeros MUST be ignored.

       *  An empty byte string MUST be accepted and treated as the value
          zero.

   See also Appendix E and Appendix G for further background on big
   numbers.  See Appendix F for specification in CDDL.
```


Individually, with locators:

- (§4.2 item 1) "Decoders MUST accept shortest-form encoded arguments."
- (§4.2 item 2) "If arrays or maps are supported, definite-length arrays or maps MUST be accepted."
- (§4.2 item 3) "If text or byte strings are supported, definite-length text or byte strings MUST be accepted."
- (§4.2 item 4) "If floating-point numbers are supported, the following apply:"
- (§4.2 item 4) "Half-precision values MUST be accepted."
- (§4.2 item 4) "Double- and single-precision values SHOULD be accepted; leaving these out is only foreseen for decoders that need to work in exceptionally constrained environments."
- (§4.2 item 4) "If double-precision values are accepted, single-precision values MUST be accepted."
- (§4.2 item 5) "If big numbers (tags 2 and 3) are accepted, the following apply:"
- (§4.2 item 5) "Big numbers described in Section 3.4.3 of [STD94] MUST be accepted."
- (§4.2 item 5) "Leading zeros MUST be ignored."
- (§4.2 item 5) "An empty byte string MUST be accepted and treated as the value zero."
- (§4.2) "See also Appendix E and Appendix G for further background on big numbers.  See Appendix F for specification in CDDL."

## §4.3. When to use preferred-plus serialization

- (§4.3) "Preferred-plus is the recommended default."
- (§4.3) "It supports all CBOR data types and value ranges (except non-trivial NaNs), typically produces the most compact encoding, is straightforward to implement, and is widely supported by CBOR libraries."
- (§4.3) "It provides strong interoperability because (1) decoders are required to accept all encodings that a preferred-plus encoder is permitted to produce, and (2) the requirements are formally specified."
- (§4.3) "Choose a different serialization only when you have a specific need: deterministic serialization when determinism is required, a special serialization with indefinite lengths when streaming is required, or another special serialization for capabilities beyond what preferred-plus provides (see Section 6)."
- (§4.3) "Note that preferred-plus is deterministic when maps are not in use."

## §4.4. Relation To Preferred Serialization

- (§4.4) "Preferred-plus serialization is defined to be the long-term replacement for preferred serialization."

```text
   The differences are:

   *  Definite lengths are a requirement, not a preference.

   *  The only NaN allowed in encoded output is the half-precision quiet
      NaN.

   *  For big numbers, leading zeros must be ignored and the empty
      string must be accepted as zero.
```


- (§4.4) "These differences are not of significance in real-world implementations, so preferred-plus serialization is already largely supported."
- (§4.4) "Section 3 of [STD94] states that in preferred serialization the use of definite-length encoding is a "preference", not a requirement."
- (§4.4) "Technically that means preferred serialization decoders must support indefinite lengths, but in reality many do not."
- (§4.4) "Thus preferred-plus serialization is largely interchangeable with preferred serialization in the real world."

## §5. Deterministic Serialization

- (§5) "This section defines a serialization named "deterministic serialization""
- (§5) "Deterministic serialization is the same as described in Section 4.2.1 of [STD94] except for the encoding of floating-point NaNs."
- (§5) "See Section 4 and Appendix C for details on, and the rationale for NaN encoding."
- (§5) "Note that in deterministic serialization, any big number that can be represented as an integer must be encoded as an integer.  This rule is inherited from preferred-plus serialization (Section 4), just as Section 4.2.1 of [STD94] inherits this requirement from preferred serialization."
- (§5) "See also Appendix B for considerations involved in designing a deterministic protocol that extend beyond serialization."

## §5.1. Encoder Requirements

```text
   1.  All of preferred-plus serialization defined in Section 4.1 MUST
       be used.

   2.  If a map is encoded, the items in it MUST be sorted in the
       bytewise lexicographic order of their deterministic encodings of
       the map keys.  (Note that this is the same as the sorting in
       Section 4.2.1 of [STD94] and not the same as Section 3.9 of
       [RFC7049] / Section 4.2.3 of [STD94].)
```


## §5.2. Decoder Requirements

```text
   1.  Decoders MUST meet the decoder requirements described in
       Section 4.2.  That is, deterministic encoding imposes no
       requirements over and above the requirements for decoding
       preferred-plus serialization.
```


## §5.3. When to use Deterministic Serialization

## §5.3.1. Not Commonly Needed for Hashing and Signing

- (§5.3.1) "Most applications do not require deterministic encoding — even those that employ signing or hashing to authenticate or protect the integrity of data."
- (§5.3.1) "For example, the payload of a COSE_Sign message (See [RFC9052]) does not need to be encoded deterministically because it is transmitted with the message.  The recipient receives the exact same bytes that were signed."
- (§5.3.1) "Deterministic encoding becomes necessary only when the protected data is not transmitted as the exact bytes that are used for authenticity or integrity verification.  In such cases, both the sender and the receiver must independently construct the exact same sequence of bytes.  To guarantee this, the encoding must eliminate all variability and ambiguity."
- (§5.3.1) "The Sig_structure, defined in Section 4.4 of [RFC9052], is an example of this requirement."
- (§5.3.1) "See the more detailed, COSE-based example in Appendix K."

## §5.3.2. Decoding Deterministic Serialization and Relation to Preferred-Plus Serialization

The section title is itself wrapped in the source as "Decoding Deterministic Serialization and Relation to Preferred-" / "Plus Serialization".

- (§5.3.2) "The only difference between preferred-plus and deterministic serialization is that in deterministic serialization, maps are required to be sorted by their keys."
- (§5.3.2) "Preferred-plus serialization exists as a separate mode solely because map sorting can be too expensive in some constrained environments."
- (§5.3.2) "Map decoding must never depend on the sort order of a map, even when maps are required to be sorted."
- (§5.3.2) "As a result, deterministic serialization (Section 5) can always be decoded by a decoder that supports preferred-plus serialization (Section 4).  Because of this property, deterministic serialization can always be used in place of preferred-plus serialization."
- (§5.3.2) "In environments where map sorting is not costly, it is both acceptable and beneficial to always use deterministic serialization.  In such environments, a CBOR encoder may produce deterministic encoding by default and may even omit support for preferred-plus encoding entirely."
- (§5.3.2) "However, note that deterministic serialization is never a substitute for general serialization where use cases may require indefinite lengths, separate big numbers from integers in the data model, or need non-trivial NaNs."

## §5.3.3. No Map Ordering Semantics

- (§5.3.3) "In the basic generic data model, maps are unordered (See Section 5.6 of [STD94])."
- (§5.3.3) "Applications MUST NOT rely on any particular map ordering, even if deterministic serialization was used."
- (§5.3.3) "A CBOR library is not required to preserve the order of keys when decoding a map, and the underlying programming language may not preserve map order either — for example, the Go programming language provides no ordering guarantees for maps."
- (§5.3.3) "The sole purpose of map sorting in deterministic serialization is to ensure reproducibility of the encoded byte stream, not to provide any semantic ordering of map entries."
- (§5.3.3) "If an application requires a map to be ordered, it is responsible for applying its own sorting."

## §6. Special Serializations

```text
   When needed, protocols may define special serializations beyond the
   three described above.  The main capabilities they enable are:

   *  Streaming encoding of strings, arrays, and maps using indefinite
      lengths, for use when the encoded item(s) exceeds the memory
      available on the encoding device.

   *  Fixed-size integer encoding, allowing values to be copied directly
      to and from hardware registers.  CBOR is simple enough that
      encoders and decoders for some protocols can be implemented
      entirely in hardware.

   *  Fixed-width floating-point encoding, relieving the encoder from
      performing floating-point reduction to the shortest representable
      form.

   *  In-place length updates for strings, arrays, and maps, by encoding
      their lengths in a fixed number of bits.  For example, if a string
      length is always encoded in 32 bits, increasing its length from
      2^16-1 to 2^16 requires only overwriting the length field rather
      than shifting all 2^16 bytes of content.

   *  Transmission of non-trivial NaN floating-point values (see
      Appendix C).

   *  Deterministic serialization with any or all of the above.

   All of these except determinism are also available with general
   serialization, but a targeted special serialization will usually be
   substantially easier to implement.
```


- (§6) "A recommended approach is to define a special serialization as preferred-plus or deterministic serialization with additional constraints or extensions."
- (§6) "For example, a protocol requiring deterministic streaming of maps and arrays could be specified as:"

The block below is an illustrative example of how a protocol would word a special serialization. Its three MUSTs bind nothing in this document; they are reproduced because the source carries them.

```text
      Deterministic serialization MUST be used, except that maps and
         arrays MUST be encoded with indefinite lengths.  Strings retain
         definite-length encoding, and map ordering MUST follow the
         rules of deterministic serialization.
```


- (§6, example) "Deterministic serialization MUST be used, except that maps and arrays MUST be encoded with indefinite lengths."
- (§6, example) "Strings retain definite-length encoding, and map ordering MUST follow the rules of deterministic serialization."

## §7. New Tag Data Model Rule

The `//`-prefixed editorial aside to the author at the head of this section is omitted.

- (§7) "Section 2 of [STD94] states that each new CBOR tag definition introduces a new and distinct data type."
- (§7) "In contrast, the definitions of Tags 2 and 3 (bignums) in Section 3.4.3 of [STD94] do not introduce a separate data type; instead, they attach directly to the integer type and extend its numeric range."
- (§7) "As a result, the generic data model’s integer type is modified rather than augmented with a new, independent type (see Appendix E)."
- (§7) "This document establishes a new rule that prohibits future tag definitions from having such effects:"

```text
   All future CBOR tag definitions MUST NOT incorporate, modify, or
   otherwise affect any data types other than the type defined by the
   tag itself.  A set of tags MAY affect each other, provided that all
   defining authorities for those tags explicitly agree.
```


- (§7) "All future CBOR tag definitions MUST NOT incorporate, modify, or otherwise affect any data types other than the type defined by the tag itself."
- (§7) "A set of tags MAY affect each other, provided that all defining authorities for those tags explicitly agree."
- (§7) "Tags 2 and 3 are exempt from this rule, as they were defined prior to the establishment of this requirement."

## §8. CDDL Serialization Control Operator

- (§8) "The ".serial" control operator specifies the serialization of any type in CDDL, including the serialization of the whole document or byte-string-wrapped sub-parts."
- (§8) "The controller (the right-hand side) MUST be either "prefp" or "dtrm", specifying preferred-plus (Section 4) or deterministic (Section 5) serialization, respectively."
- (§8) "The scope of .serial applies recursively through nested arrays and maps, but does not extend into byte strings or other data items that happen to contain encoded CBOR."
- (§8) "Every instance of embedded CBOR that requires specific serialization must specify it explicitly.  See also Appendix I."
- (§8) "For example, the following specifies that a message or protocol described by "stuff" is deterministically serialized and wrapped in a byte string:"

```text
   stuff = ...
   deterministic-stuff = stuff .serial dtrm
   wrapped-deterministic-stuff = #6.24(bytes .cbor deterministic-stuff)
```


- (§8) "For another example, the first lines of a CDDL document as follows specify that "my-protocol" be serialized with preferred-plus."

```text
   my-prefp-protocol = my-protocol .serial prefp
   my-protocol = ...
```


- (§8) "New controller values for new serializations are possible but are highly discouraged.  Standards action is required to add them."

## §9. Security Considerations

- (§9) "The security considerations in Section 10 of [STD94] apply."

## §9.1. Covert Channel

- (§9.1) "CBOR’s serialization variants can be used as a covert channel [LAM73] to steganographically exfiltrate data."
- (§9.1) "For example, a CBOR argument (such as an integer encoding or a string length) can be encoded up to five different ways (e.g. the value 1 can be encoded as 0x01, 0x1801, 0x190001, 0x1A00000001, or 0x1B0000000000000001)."
- (§9.1) "This variability can be used to encode ~2 hidden bits per argument."
- (§9.1) "Since every CBOR item carries an argument, even moderately complex protocols may accumulate sufficient bits to exfiltrate sensitive material (e.g., cryptographic keys) or to generate persistent identifiers for tracking users or devices."
- (§9.1) "The following techniques may be used to establish a covert channel:"

```text
   *  Varying the encoding of CBOR arguments (as above)

   *  Representing text or byte strings as indefinite-length encodings,
      and encoding information in the segmentation structure (e.g.,
      segment lengths or insertion of empty segments)
```

```text
   *  Encoding data within NaN payloads

   *  Manipulating the ordering of map entries

   *  Varying the Unicode representation of text strings
```


- (§9.1) "These channels are covert because most CBOR decoders accept all such representations without raising errors or warnings." — the source line ends with a stray pilcrow, "warnings.¶"; see "Source defects".
- (§9.1) "The primary safeguard is to ensure the CBOR encoding library used is trustworthy and does not exfiltrate data."
- (§9.1) "Another option is to require preferred-plus or deterministic serialization and to have decoders issue a warning if not compliant.  See Appendix H."

## §10. IANA Considerations

The `//`-prefixed note to the RFC Editor at the head of this section is omitted.

```text
   This document requests IANA to register the ".serial" control
   operator into the registry "CDDL Control Operators" of the
   [IANA.cddl] registry group.

   IANA is requested to add a reference to Section 7 to the CBOR tag
   registry [IANA.cbor-tags].
```


- (§10) "This document requests IANA to register the ".serial" control operator into the registry "CDDL Control Operators" of the [IANA.cddl] registry group."
- (§10) "IANA is requested to add a reference to Section 7 to the CBOR tag registry [IANA.cbor-tags]."

## §11.1. Normative References

```text
   [IANA.cbor-tags]
              IANA, "Concise Binary Object Representation (CBOR) Tags",
              <https://www.iana.org/assignments/cbor-tags>.

   [IANA.cddl]
              IANA, "Concise Data Definition Language (CDDL)",
              <https://www.iana.org/assignments/cddl>.

   [IEEE754]  IEEE, "IEEE Standard for Floating-Point Arithmetic", IEEE
              Std 754-2019, DOI 10.1109/IEEESTD.2019.8766229,
              <https://ieeexplore.ieee.org/document/8766229>.
```


```text
   [RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
              Requirement Levels", BCP 14, RFC 2119,
              DOI 10.17487/RFC2119, March 1997,
              <https://www.rfc-editor.org/rfc/rfc2119>.

   [RFC8610]  Birkholz, H., Vigano, C., and C. Bormann, "Concise Data
              Definition Language (CDDL): A Notational Convention to
              Express Concise Binary Object Representation (CBOR) and
              JSON Data Structures", RFC 8610, DOI 10.17487/RFC8610,
              June 2019, <https://www.rfc-editor.org/rfc/rfc8610>.

   [STD94]    Bormann, C. and P. Hoffman, "Concise Binary Object
              Representation (CBOR)", STD 94, RFC 8949,
              DOI 10.17487/RFC8949, December 2020,
              <https://www.rfc-editor.org/rfc/rfc8949>.
```


## Appendix A. Information Model, Data Model and Serialization

```text
   +================+=============+===================+================+
   |                | Information | Data Model        | Serialization  |
   |                | Model       |                   |                |
   +================+=============+===================+================+
   | Abstraction    | Top level;  | Realization of    | Actual bytes   |
   | Level          | conceptual  | information in    | encoded for    |
   |                |             | data structures   | transmission   |
   |                |             | and data types    |                |
   +----------------+-------------+-------------------+----------------+
   | Example        | The         | A floating-       | Encoded CBOR   |
   |                | temperature | point number      | of a floating- |
   |                | of          | representing      | point number   |
   |                | something   | the temperature   |                |
   +----------------+-------------+-------------------+----------------+
   | Standards      | [UML]       | CDDL              | CBOR           |
   +----------------+-------------+-------------------+----------------+
   | Implementation | n/a         | API Input to      | Encoded CBOR   |
   | Representation |             | CBOR encoder      | in memory or   |
   |                |             | library, output   | for            |
   |                |             | from CBOR         | transmission   |
   |                |             | decoder library   |                |
   +----------------+-------------+-------------------+----------------+

          Table 2: Information Model, Data Model and Serialization
```


- (App. A) "CBOR doesn't provide facilities for information models.  They are mentioned here for completeness and to provide some context."
- (App. A) "While not required, [RFC8610] may be used to describe the data model of a protocol.  The types in the data model are serialized per [STD94] to create encoded CBOR."
- (App. A) "CBOR allows certain data types to be serialized in multiple ways to facilitate easier implementation in constrained environments."
- (App. A) "Crucially, CBOR allows — and even expects — that some implementations will not support all serialization variants."

## Appendix B. General Protocol Considerations for Determinism

- (App. B) "In addition to Section 5, there are considerations in the design of any deterministic protocol."
- (App. B) "For a protocol to be deterministic, both the encoding (serialization) and data model (application) layer must be deterministic."
- (App. B) "While deterministic serialization, Section 5, ensures determinism at the encoding layer, requirements at the application layer may also be necessary."
- (App. B) "Here’s an example application layer specification:"

```text
      At the sender’s convenience, the birth date MAY be sent either
         as an integer epoch date or string date.  The receiver MUST
         decode both formats.
```


- (App. B, example) "At the sender’s convenience, the birth date MAY be sent either as an integer epoch date or string date."
- (App. B, example) "The receiver MUST decode both formats."
- (App. B) "While this specification is interoperable, it lacks determinism."
- (App. B) "To make this example application layer specification deterministic, specify one date format and prohibit the other."
- (App. B) "A more interesting source of application layer variability comes from CBOR’s variety of number types.  For instance, the number 2 can be represented as an integer, float, big number, decimal fraction and other."
- (App. B) "Most protocols designs will just specify one number type to use, and that will give determinism, but here’s an example specification that doesn’t:"

```text
      At the sender’s convenience, the fluid level measurement MAY be
         encoded as an integer or a floating-point number.  This allows
         for minimal encoding size while supporting a large range.  The
         receiver MUST be able to accept both integers and floating-
         point numbers for the measurement.
```


- (App. B, example) "At the sender’s convenience, the fluid level measurement MAY be encoded as an integer or a floating-point number."
- (App. B, example) "The receiver MUST be able to accept both integers and floating-point numbers for the measurement."
- (App. B) "Again, this ensures interoperability but not determinism — identical fluid level measurements can be represented in more than one way."
- (App. B) "A better solution requires the fluid level always be encoded using the smallest representation for every particular value."
- (App. B) "See the numeric reduction defined by [I-D.mcnally-deterministic-cbor]."
- (App. B) "Although this is not strictly a CBOR issue, deterministic CBOR protocol designers should be mindful of variability in Unicode text, as some characters can be encoded in multiple ways."

## Appendix C. IEEE 754 NaN

## Appendix C.1. Basics

- (App. C.1) "IEEE 754 formally defines the notions of quiet and signaling NaN, but the bit pattern distinguishing them is only a recommendation, directed at CPU designers:"

```text
   *  A quiet NaN has the most significant significand bit set.

   *  A signaling NaN has that bit clear and at least one other
      significand bit set, to distinguish it from infinity.

   *  Either can have a non-zero payload, which is the bits other than
      the most significant significand bit.

   *  No recommendation is made for the sign bit.
```


- (App. C.1) "This recommendation is not universally followed (e.g., PA-RISC and pre-R6 MIPS)."
- (App. C.1) "For this discussion, a non-trivial NaN is a signaling NaN, a NaN with a non-zero payload, or a NaN with the sign bit set, as the host represents it."
- (App. C.1) "A trivial NaN is one that passively indicates that the value is not a number, and nothing more."

## Appendix C.3. Use and Non-use for Non-Trivial NaNs

- (App. C.3) "Preferred-plus and deterministic serialization cannot be used for this protocol."
- (App. C.3) "Support for NaN payloads is unreliable across programming environments and CBOR libraries."
- (App. C.3) "Values cannot be translated directly to JSON, which does not support NaNs of any kind."

## Appendix C.4. Clarification of RFC 8949

- (App. C.4) "This is a clarifying restatement of how NaNs are to be treated according to [STD94]."
- (App. C.4) "NaNs represented in floating-point values of different lengths are considered equivalent in the basic generic data model if:"

```text
   *  Their sign bits are identical, and

   *  Their significands are identical after both significands are zero-
      extended on the right to 64 bits
```


- (App. C.4) "This equivalence is established for the entire CBOR basic generic data model."
- (App. C.4) "A NaN encoded as half-, single-, or double-precision is equivalent whenever it satisfies the rules above.  This remains true regardless of how a CBOR library accepts, stores, or presents a NaN in its API.  At the application layer, the equivalence still holds."
- (App. C.4) "The only way to avoid this equivalence is by using a tag specifically designed to carry NaNs without these equivalence rules, since tags extend the data model unless otherwise specified."
- (App. C.4) "In preferred serialization, this equivalence MUST be used to shorten encoding length."
- (App. C.4) "If a NaN can be represented equivalently in a shorter form (e.g., half-precision rather than single-precision), then the shorter representation MUST be used."
- (App. C.4) "This equivalence also applies when floating-point values are used as map keys."
- (App. C.4) "A map key encoded as half-precision MUST be considered a duplicate of one encoded as double-precision if they meet the equivalence rules above."
- (App. C.4) "However, this equivalence does not apply to map sorting.  Sorting operates on the fully encoded and serialized representation, not on the abstract data model."
- (App. C.4) "It is Section 2 of [STD94] that establishes this equivalence by stating that the number of bytes used to encode a floating-point value is not visible in the data model."
- (App. C.4) "Since Section 4.2.1 of [STD94], (Core Deterministic Encoding Requirements), explicitly requires preferred serialization, compliant deterministic encodings must use the shortest equivalent representation of NaNs."
- (App. C.4) "Finally, Section 4.2.2 of [STD94] discusses alternative approaches to deterministic encoding.  It suggests, for example, that all NaNs may be encoded as a half-precision quiet NaN.  This section is distinct from the Core Deterministic Encoding Requirements and represents an optional alternative for handling NaNs."

## Appendix C.5. Divergence from [STD94]

- (App. C.5) "Non-trivial NaNs are not permitted in either preferred-plus or deterministic serializations.  This is in contrast to preferred serialization and Section 4.2.1 of [STD94]."
- (App. C.5) "Note that the prohibition of non-trivial NaNs is the sole difference between deterministic serialization (Section 5) and Section 4.2.1 of [STD94]."
- (App. C.5) "Non-trivial NaNs remain supported by general serialization; the divergence is only for preferred-plus and deterministic serialization."
- (App. C.5) "A new CBOR tag can be defined in the future to explicitly support them."

## Appendix C.6. Recommendations for Use of Non-Trivial NaNs

- (App. C.6) "While non-trivial NaNs are excluded from preferred-plus and deterministic serialization, they are supported by Section 3."
- (App. C.6) "New protocol designs SHOULD avoid non-trivial NaNs."
- (App. C.6) "Support for them is unreliable, and it is straightforward to design CBOR-based protocols that do not depend on them."
- (App. C.6) "In many cases, the use of NaN can be replaced entirely with null."

## Appendix D. Code for Encoding Preferred-Plus Floating-Point Values

- (App. D) "Preferred-plus (Section 4.1) and deterministic serialization require that floating-point values fitting in single-precision and half-precision be encoded as such."
- (App. D) "Two functions are provided: one to convert from double to single, and another from single to half.  Used together, they cover all possible cases."
- (App. D) "If the input is a double, pref_plus_double_to_single() must be called first; if it succeeds, pref_plus_single_to_half() is then called to complete the conversion from double to half.  If the input is already a single, only pref_plus_single_to_half() need be called."
- (App. D) "Both functions return an integer with the bit pattern for the resulting floating-point value, or -1 if the conversion can't be performed because the input is out of range or precision would be lost."

Figure 1 verbatim. The source breaks three pages inside it, so it appears as four fenced blocks.

```text
   /* Constants based on IEEE 754; _LEN is in bits */

   /* Half-precision */
   #define HLF_MANT_LEN          10
   #define HLF_EXP_LEN           5
   #define HLF_MANT_BITS         0x3ffUL /* 10 bits */
   #define HLF_SIGN_BIT         (0x01UL << (HLF_EXP_LEN + HLF_MANT_LEN))
   #define HLF_NAN_INF_EXP_BITS  0x7c00
   #define HLF_QUIET_NAN        (0x1UL << (HLF_MANT_LEN-1))

   /* Single-precision */
   #define SGL_MANT_LEN          23
   #define SGL_EXP_LEN           8
   #define SGL_MANT_BITS         0x7fffffUL /* 23 bits */
   #define SGL_SIGN_BIT         (0x01UL << (SGL_EXP_LEN + SGL_MANT_LEN))
   #define SGL_EXP_BITS          0xffUL /* 8 bits */
   #define SGL_QUIET_NAN        (0x1UL << (SGL_MANT_LEN - 1))
   #define SGL_ZERO_SUBNORM_EXP  0
   #define SGL_NAN_INF_EXP       255
   #define SGL_NAN_INF_EXP_BITS (SGL_NAN_INF_EXP << SGL_MANT_LEN)
   #define SGL_MANT_ADD_ONE     (0x01UL << SGL_MANT_LEN)

   /* Double-precision */
   #define DBL_MANT_LEN          52
   #define DBL_EXP_LEN           11
   #define DBL_MANT_BITS         0xfffffffffffffULL /* 52 bits */
   #define DBL_EXP_BITS          0x7ffULL /* 11 bits */
   #define DBL_QUIET_NAN        (0x1ULL << (DBL_MANT_LEN-1))
   #define DBL_ZERO_SUBNORM_EXP  0
   #define DBL_NAN_INF_EXP       2047
   #define DBL_MANT_ADD_ONE     (0x01ULL << (DBL_MANT_LEN))

   /* Converting single to half; _EXP are biased single exponents */
```

```text
   #define S2H_SIGN_SHIFT       16
   #define S2H_BIAS_DIFF_EXP   (127 - 15)
   #define S2H_MIN_NORM_EXP     113
   #define S2H_MIN_SUBNORM_EXP  102
   #define S2H_SUBNORM_SHIFT    126
   #define S2H_MAX_NORM_EXP     142
   #define S2H_LOST_BITS        0x1fffUL /* 23 - 10 bits */

   /* Converting double to single; _EXP are biased double exponents */
   #define D2S_SIGN_SHIFT       32
   #define D2S_BIAS_DIFF_EXP   (1023 - 127)
   #define D2S_MIN_NORM_EXP     898
   #define D2S_MIN_SUBNORM_EXP  874
   #define D2S_SUBNORM_SHIFT    926
   #define D2S_MAX_NORM_EXP     1150
   #define D2S_LOST_BITS        0x1fffffffULL /* 52 - 23 bits */


   long pref_plus_single_to_half(unsigned long single) {
     const unsigned long sign = single >> S2H_SIGN_SHIFT & HLF_SIGN_BIT;
     const unsigned long mant = single & SGL_MANT_BITS;
     const unsigned long exp  = single >> SGL_MANT_LEN & SGL_EXP_BITS;

     if (exp == SGL_ZERO_SUBNORM_EXP) {
       if (mant == 0) {
         return (long)sign; /* +/- 0.0 */
       } else {
         return -1; /* single subnormals are out of range for half */
       }
     } else if (exp >= S2H_MIN_SUBNORM_EXP && exp < S2H_MIN_NORM_EXP) {
       if (mant & ((1UL << (S2H_SUBNORM_SHIFT - exp)) - 1)) {
         return -1;   /* bits lost in conversion to half subnormal */
       } else {
         return (long)(sign + /* converts to half subnormal */
              ((mant + SGL_MANT_ADD_ONE) >> (S2H_SUBNORM_SHIFT - exp)));
       }
     } else if (exp >= S2H_MIN_NORM_EXP && exp <= S2H_MAX_NORM_EXP) {
       if (mant & S2H_LOST_BITS) {
         return -1; /* bits lost in conversion */
       } else {
         return (long)(sign + /* Converts to normal */
                      ((exp - S2H_BIAS_DIFF_EXP) << HLF_MANT_LEN) +
                      (mant >> (SGL_MANT_LEN - HLF_MANT_LEN)));
       }
     } else if (exp == SGL_NAN_INF_EXP) {
       if (mant == 0) {
         return (long)(sign + HLF_NAN_INF_EXP_BITS); /* +/- infinity */
       } else if (mant == SGL_QUIET_NAN && sign == 0) {
```

```text
          return HLF_QUIET_NAN + HLF_NAN_INF_EXP_BITS; /* trivial NaN */
       } else {
          return -1; /* non-trivial NaN */
       }
     } else {
        return -1; /* large exponent -- out of range for half */
     }
   }


   long long pref_plus_double_to_single(unsigned long long dbl) {
     const unsigned long long sign =
                                   dbl >> D2S_SIGN_SHIFT & SGL_SIGN_BIT;
     const unsigned long long mant = dbl & DBL_MANT_BITS;
     const unsigned long long exp  = dbl >> DBL_MANT_LEN & DBL_EXP_BITS;

     if (exp == DBL_ZERO_SUBNORM_EXP) {
       if (mant == 0) {
         return (long long)sign; /* +/- 0.0 */
       } else {
         return -1; /* double subnormals are out of range for single */
       }
     } else if (exp >= D2S_MIN_SUBNORM_EXP && exp < D2S_MIN_NORM_EXP) {
       if (mant & ((1ULL << (D2S_SUBNORM_SHIFT - exp)) - 1)) {
         return -1; /* bits lost in conversion to single subnormal */
       } else {
         return (long long)(sign + /* converts to single subnormal */
              ((mant + DBL_MANT_ADD_ONE) >> (D2S_SUBNORM_SHIFT - exp)));
        }
     } else if (exp >= D2S_MIN_NORM_EXP && exp <= D2S_MAX_NORM_EXP) {
       if (mant & D2S_LOST_BITS) {
         return -1; /* bits lost in conversion */
       } else {
          return (long long)(sign + /* Converts to normal */
                           ((exp - D2S_BIAS_DIFF_EXP) << SGL_MANT_LEN) +
                            (mant >> (DBL_MANT_LEN - SGL_MANT_LEN)));
       }
     } else if (exp == DBL_NAN_INF_EXP) {
       if (mant == 0) {
         /* +/- infinity */
         return (long long)(sign + SGL_NAN_INF_EXP_BITS);
       } else if (mant == DBL_QUIET_NAN && sign == 0) {
          return SGL_QUIET_NAN + SGL_NAN_INF_EXP_BITS; /* quiet NaN */
       } else {
          return -1; /* non-trivial NaN */
       }
     } else {
        return -1; /* large exponent -- out of range for single */
```

```text
     }
   }

    Figure 1: Example C Code for Preferred-Plus Floating-Point Encoding
```


## Appendix E. Big Numbers and the CBOR Data Model

- (App. E) "In the basic, generic CBOR data model, each tag represents a distinct data type (Section 2 of [STD94]).  Tags are also distinct from the major types, such as numbers and strings."
- (App. E) "By this, an integer value such as 0 or 1 encoded as major type 0 is clearly distinct in the data model from the same integer value encoded as tag 2."
- (App. E) "However, the text in Section 3.4.3 of [STD94] overrides this by defining these encodings to be equivalent rather than distinct.  This text therefore modifies the CBOR data model."
- (App. E) "No other serialization requirement in [STD94] or in this document alters the data model; this equivalence is the sole exception."
- (App. E) "Further, Section 3.4.3 of [STD94] along with text in Section 2 of [STD94] are interpreted such that there is never a CBOR data model where there is a distinction between these integer representations.  That is, the equivalence applies regardless of the serialization even though much of the relevant text appears in proximity to discussions of serialization."
- (App. E) "This document does not attempt to update or revise the text of Section 3.4.3 of [STD94].  Rather, it records the commonly accepted interpretation of that text and its implications for the CBOR data model."
- (App. E) "This document does create a new rule for future tag definitions.  See Section 7."

## Appendix F. CDDL for Big Numbers

- (App. F) "The types bigint and biguint in the CDDL Standard Prelude (Appendix D of [RFC8610]) do NOT describe the big numbers described in this document or in Section 3.4.3 of [STD94], not even for general serialization."
- (App. F) "The types integer and unsigned can be used, but note that they do not fully express the rules that govern the choice between major types 0 and 1 and the big number tags."
- (App. F) "CDDL-described protocols SHOULD use integer and unsigned and in prose state that these values correspond to either Section 4 of this document or Section 3.4.3 of [STD94]."
- (App. F) "The following CDDL can be used:"

```text
   ; big number byte strings are of unlimited size, but that
   ; can't be expressed in CDDL, so a limit of 1,000
   bnmax = 1000
   bnbstr = bstr .size (8..bnmax)

   pplus-tag2bstr = #6.2(bnbstr)
   pplus-biguint  = #0 / pplus-tag2bstr

   pplus-tag3bstr = #6.3(bnbstr)
   pplus-bignint  = #1 / pplus-tag3bstr

   pplus-bigint = pplus-biguint / pplus-bignint
```


## Appendix G. Big Number Implementation Strategies

- (App. G) "It is therefore reasonable for a CBOR library to expose separate APIs for native-sized integers and for big numbers."
- (App. G) "When a CBOR library provides a big number API, values that fall within the range of major types 0 and 1 must be encoded using those major types rather than tags 2 or 3."
- (App. G) "Similarly, decoding facilities that return big numbers must accept values encoded using major types 0 and 1, even though the returned representation is a big number."
- (App. G) "Alternatively, some CBOR libraries may choose to return tags 2 and 3 as raw byte strings, as this approach is simpler than implementing full big number support."
- (App. G) "When a library adopts this approach, it should clearly document that the application layer is responsible for performing the integer unification."
- (App. G) "The application is also responsible for handling CBOR’s offset-by-one encoding of negative values and the extended negative integer range permitted by major type 1."
- (App. G) "Another acceptable approach is for a CBOR library to provide a generic mechanism that allows applications to register handlers for specific tags.  In this case, handlers for tags 2 and 3 MUST perform the required unification with major types 0 and 1."
- (App. G) "Finally, note that big numbers are not a widely used feature of CBOR.  Some CBOR libraries may entirely omit support for tags 2 and 3."

## Appendix H. Serialization Checking

- (App. H) "Serialization checking rejects input which, while well-formed CBOR, does not conform to a particular serialization rule set it is enforcing."
- (App. H) "For example, a decoder checking for deterministic serialization will error out if map keys are not in the required sorted order."
- (App. H) "Likewise, a decoder checking for preferred-plus serialization will reject any CBOR data item that is not encoded in its shortest form."
- (App. H) "This type of checking goes beyond the basic requirement of verifying that input is well-formed CBOR.  The data rejected by serialization checking is well-formed; it is rejected because it violates additional serialization constraints."

## Appendix H.1. Serialization Checking Use Cases

- (App. H.1) "Some applications that rely on deterministic serialization may choose serialization checking in order to ensure that the data they consume is truly deterministic and that the assumptions their logic makes about determinism hold."
- (App. H.1) "Some protocol environments may use serialization checking to minimize representational variants as a strategy to improve interoperability."
- (App. H.1) "Serialization checking may enhance security in certain contexts, but such checking is never a substitute for correct and complete CBOR input validation."
- (App. H.1) "All CBOR decoders — regardless of their capabilities, modes, or optional features — must always perform full input validation.  This includes rejecting CBOR features the decoder does not support.  For example, a decoder that does not support indefinite-length items must reject them because they are unsupported, not because it is acting as a checking decoder."
- (App. H.1) "Decoders that fail to perform this essential input validation are fundamentally inadequate and represent a security risk.  The appropriate remedy is to fix their input validation, not to add the serialization checking described here."

## Appendix I. CBOR Byte String Wrapping

- (App. I) "This appendix provides non-normative guidance on byte-string wrapping of CBOR."
- (App. I) "It applies primarily to tag 24 and the CDDL .cbor and .cborseq control operators, but also to the serialization-specifying control operators described in Section 8.  It also applies when prose states the byte-string wrapping requirement, such as for the COSE protected headers.  See also Appendix K.1."

## Appendix I.1. Purpose

```text
   Error isolation:  Wrapping CBOR in a byte string prevents encoding
      errors in the wrapped data from causing the enclosing CBOR to fail
      during decoding.  (CBOR decoding generally halts at the first
      error and lacks internal length redundancy found in formats like
      ASN.1/DER.)

   CBOR library support for signing and hashing:  When wrapped CBOR
      needs to be signed or hashed, its original encoded bytes must be
      available.  Most CBOR libraries cannot directly extract the raw
      bytes of substructures, but byte-string wrapping provides direct
      access to the exact bytes for signing or hashing.

   Protocol embedding:  Byte-string wrapping is generally useful when
      messages from one CBOR-based protocol need to be embedded within
      another CBOR protocol.

   Special map keys:  Some CBOR libraries only support simple, non-
      aggregate map keys (e.g., integers or strings).  To use complex
      data types like arrays and maps as map keys, they can be wrapped
      in a byte string.
```


## Appendix I.2. Wrapping Recommendations

- (App. I.2) "The serialization requirements for the wrapping CBOR may differ from those for the wrapped CBOR.  CBOR itself imposes no universal rule that they must match; this is determined by the design of the wrapping protocol."
- (App. I.2) "The wrapping protocol should not impose serialization requirements on the wrapped message.  The two should be treated as independent entities.  This approach avoids potential conflicts between serialization rules."
- (App. I.2) "For example, assume protocol XYZ wraps protocol ABC.  If protocol ABC requires Canonical CBOR as specified in Section 3.9 of [RFC7049] (e.g., [CTAP2] from WebAuthn) while protocol XYZ requires deterministic serialization, Section 5, a conflict would arise."
- (App. I.2) "Most CBOR data to be signed or hashed does not require a specific serialization."

## Appendix I.3. CBOR Library Implementation Suggestion

- (App. I.3) "A straightforward implementation strategy is to instantiate a second CBOR encoder or decoder for the wrapped message."
- (App. I.3) "A more efficient approach can be for the CBOR library to treat the wrapped CBOR like a container (similar to arrays or maps)."
- (App. I.3) "Similarly, a byte-string wrapping encoded CBOR can be treated as a container that always contains exactly one item."

## Appendix J. Signing and Hashing Encoded CBOR

- (App. J) "Signing or hashing is performed over some range of the encoded CBOR, possibly all of it."
- (App. J) "For signing or hashing to work, the sender/encoder and the receiver/verifier must operate on exactly the same range of encoded bytes, so a protocol definition MUST define that range unambiguously."
- (App. J) "There are several ways to specify it:"

```text
   *  Name an existing data item (e.g., a CDDL type)

   *  Name a data item created specifically for this purpose (e.g., a
      CDDL type)

   *  Describe the input data items in prose

   *  Wrap the input in a byte string
```


- (App. J) "Typically, a named data item is an array or a map, but non-aggregate items can be named as well."
- (App. J) "When naming an item, the specification should state explicitly whether the input is the full encoded item (head, contents, and trailing "break" if indefinite-length) or only its contents.  Covering the full encoded item is recommended, as it is clearer."
- (App. J) "If the item might be tag content (i.e., preceded by one or more tag numbers), the specification should state whether the tag numbers are included in the input; including them is recommended."
- (App. J) "It is also possible to specify a slice of a map or array as the input.  A good way to do this is to define a CDDL type that represents the slice as a CBOR sequence."
- (App. J) "Another practice is to wrap the bytes to be signed or hashed in a byte string, following the pattern of tag 24 (the tag number itself is typically unnecessary and omitted)."
- (App. J) "Byte-string wrapping is guaranteed to work with even simple, basic libraries, although it will probably require two instances of the encoder or decoder: one for the wrapped (signed/hashed) CBOR and one for the wrapping CBOR.  See Appendix I."
- (App. J) "If byte-string wrapping is not used, the CBOR library must provide an additional feature that gives access to the undecoded CBOR."
- (App. J) "Another tactic is to require deterministic encoding.  The receiver then reconstructs the signed/hashed bytes from the decoded data items rather than accessing the received encoded CBOR."
- (App. J) "In summary, byte-string wrapping is the most reliable approach because it clearly delineates what is signed or hashed and works with every decoder, but the other designs can also be made to work."

## Appendix K. Serialization for COSE

- (App. K) "This appendix highlights how the topics in this document apply to CBOR Object Signing and Encryption (COSE [RFC9052])."
- (App. K) "It focuses on the COSE_Sign1 message (Section 4.2 of [RFC9052]), which is sufficient for illustrating the relevant considerations."
- (App. K) "COSE_Sign1 is a simple structure for signing a payload.  Its serialization can be described in three parts:"

```text
   *  The payload

   *  The Sig_structure

   *  The encoded message (the header parameters and the array of four
      that is the COSE_Sign1)
```


## Appendix K.1. COSE Payload Serialization

- (App. K.1) "The payload is transmitted from the signer/sender fully intact all the way to the verifier/receiver."
- (App. K.1) "Because it is transmitted fully intact, CBOR is a binary protocol and intermediaries do not do things like wrap long lines or add base 64 encoding or such, it is not special in any way and COSE imposes no serialization restrictions on it at all.  That is, it can use any serialization it wants."
- (App. K.1) "The serialization is selected by the protocol that defines the payload, not by COSE."
- (App. K.1) "This highlights the principle that determinism is often NOT needed for signing and hashing described in Section 5.3."
- (App. K.1) "It is also worth noting that the payload is a byte string wrapped.  This is not for determinism, armoring or canonicalization.  It is so that the payload can be any data format, including not CBOR."
- (App. K.1) "It is also so CBOR libraries can return the CBOR-encoded payload for processing by the verification algorithms."
- (App. K.1) "This is an example of byte string wrapping described in Appendix I."

## Appendix K.2. COSE Sig_structure

- (App. K.2) "The Sig_structure Section 4.4 of [RFC9052] is used to aggregate all the items that are input to the signature algorithm — the payload, protected headers and other."
- (App. K.2) "The Sig_structure is not transmitted from the sender to the receiver; instead, it is constructed independently by both parties."
- (App. K.2) "COSE therefore explicitly requires deterministic encoding so that both the sender and receiver produce identical encoded CBOR representations.  This requirement is specified in Section 9 of [RFC9052]."
- (App. K.2) "This COSE requirement is effectively equivalent to the deterministic serialization defined in Section 5, since no floating-point NaNs are involved.  It is also effectively equivalent to preferred-plus serialization as defined in Section 4, because the Sig_structure contains no maps."
- (App. K.2) "The determinism requirement does not apply to the protected headers incorporated into the Sig_structure.  Deterministic encoding of the headers is unnecessary because they are transmitted in the exact encoded form in which they are included in the Sig_structure."
- (App. K.2) "Furthermore, determinism requirements do not extend into CBOR inside of byte strings.  Once CBOR data is wrapped in a byte string, its internal encoding is treated as opaque and is not subject to surrounding serialization constraints."
- (App. K.2) "This illustrates the general need for deterministic serialization when signed data is reconstructed rather than transmitted in the exact form that was signed.  See Section 5.3."

## Appendix K.3. The Encoded Message

- (App. K.3) "A COSE_Sign1 message is an array of four elements containing two header parameter chunks, the payload, and the signature.  The two header parameter chunks are maps that hold the various header parameters."
- (App. K.3) "COSE places no serialization requirements on these elements.  The COSE protocol functions correctly regardless of the CBOR serialization used, as long as the decoder can decode what the encoder sends."
- (App. K.3) "In this respect, the serialization of the COSE_Sign1 message is no different from that of any other CBOR-based protocol message.  Indefinite-length items may be used, and non-shortest CBOR arguments are permitted.  The only requirement is that the serialization used by the encoder be decodable by the receiver."
- (App. K.3) "Strictly speaking, COSE is a framework protocol intended for incorporation into an end-to-end protocol, which should explicitly define its serialization requirements.  See Section 2.1.1 and Section 2.1.2."
- (App. K.3) "In practice, some COSE libraries have implicitly implemented only the preferred (or preferred-plus) serialization, and end-to-end protocols have often defaulted to whatever behavior the underlying COSE library provides."
- (App. K.3) "While this generally works — particularly because the preferred serialization aligns with the recommendations here — it is more robust for an end-to-end protocol to state its serialization requirements explicitly."

## Appendix L. Examples

- (App. L) "This appendix provides examples of the serializations described in this document.  Each example is a single data item.  Collectively, the examples cover the major CBOR data types and some special cases."
- (App. L) "Table 3 describes the five fields provided for each example."

```text
     +===============================+===============================+
     | field                         | description                   |
     +===============================+===============================+
     | description                   | Text describing the item      |
     +-------------------------------+-------------------------------+
     | edn-representations           | Unencoded value(s) for the    |
     |                               | data item                     |
     +-------------------------------+-------------------------------+
     | general-serializations        | Encoded representation(s) for |
     |                               | general serialization         |
     +-------------------------------+-------------------------------+
     | preferred-plus-serializations | Encoded representation(s) for |
     |                               | preferred-plus serialization  |
     +-------------------------------+-------------------------------+
     | deterministic-serialization   | Encoded representation for    |
     |                               | deterministic serialization   |
     +-------------------------------+-------------------------------+

                     Table 3: Example Data Item Fields
```


Table 3's five body rows match the prose's "five fields"; the verify pass counted them against source lines 2209-2225 and withdrew pass 1's defect to the contrary — see "Source defects".

## Appendix L.1. Use for Testing

- (App. L.1) "These examples are designed to support testing of CBOR libraries.  They cover only what is defined in this document and therefore do not provide complete or general CBOR test coverage.  All examples are well-formed and valid."
- (App. L.1) "While the CBOR-encoded serializations for each item can be used directly as test input, the EDN representation usually must be incorporated into the test manually."
- (App. L.1) "Not all CBOR libraries support every data type represented in these examples.  This is acceptable: tests for unsupported types may be skipped, or used to verify that an appropriate “unsupported” error is returned."

## Appendix L.1.1. Encode Test

```text
   To test encoding, invoke the encoder for each example data item.  The
   encoder input is the item's EDN representations.  If an example
   provides multiple EDN representations, each of them should be tested.

   The encoder should be either configured for, or to default to, one of
   the three serialization types described in this document.  A test
   succeeds if the encoder produces any of the encoded representations
   given in the example for that serialization type.

   If an encoder supports multiple serialization types, each type can be
   tested in turn.
```


## Appendix L.1.2. Decode Test

```text
   To test decoding, invoke the decoder for each example data.

   The decoder should be either to be configured for, or to default to,
   one of the three serialization types described in this document.  For
   the selected serialization type, process every encoded representation
   defined for the target type.  A test passes if the decoded output
   matches the value specified by the corresponding EDN representation.

   If a decoder supports multiple serialization types, each type can be
   tested in turn.
```


## Appendix L.1.3. Checking Decoder Test

- (App. L.1.3) "Checking decoders are described in Appendix H."
- (App. L.1.3) "This test verifies that a checking decoder rejects encodings allowed by general serialization but non-conforming for the target serialization type.  It applies only to CBOR libraries that implement serialization conformance checking."
- (App. L.1.3) "Testing a checking decoder for a target serialization type is typically performed as follows: for each example, supply the decoder with every representation permitted under general serialization except those allowed for the target serialization type.  Decoding each such input must result in a conformance-checking error."
- (App. L.1.3) "General-serialization decoders are not tested in this way, since they must accept all valid serialization forms."

## Appendix L.1.4. Non-Checking Decoder Test

- (App. L.1.4) "A non-checking decoder may accept encodings beyond what is required for the target serialization type."
- (App. L.1.4) "For example, a preferred-plus decoder will often accept non-shortest-length arguments, even though it is not required to do so, and such encodings are not permitted under preferred-plus."
- (App. L.1.4) "Testing proceeds similarly to that for a checking decoder: inputs outside the target serialization type are supplied to the decoder.  The difference is that, for a non-checking decoder, many of these inputs may successfully decode rather than producing a conformance error."
- (App. L.1.4) "Which encoding forms are accepted and which are rejected as unsupported is entirely dependent on the additional capabilities a CBOR library chooses to support and therefore not specified here."
- (App. L.1.4) "Note the following:"

```text
   *  It is common for preferred-plus and deterministic decoders to
      accept non-shortest-length arguments.

   *  If the floating-point data type is supported, all serialization
      types described in this document require support for decoding
      half-precision representations and subnormals.
```


## Appendix L.2. Example Data Items

- (App. L.2) "These are available as individual files at [Examples-Repo]."
- (App. L.2) "All general serialization examples of strings, arrays and maps include indefinite-length encodings so as to provide full test cases."
- (App. L.2) "CBOR libraries that don't support indefinite-length decoding can not claim to support general serialization even if they support most of the rest of general serialization.  For the purpose of classification by this document they are preferred-plus libraries with extra decoding features.  The extra decoding features can be tested as described in Appendix L.1.4."
- (App. L.2, map.edn) "Note that map order is not significant in the CBOR data model.  Maps are only sorted to provide deterministic encoding."
- (App. L.2, positive_bignum.edn) "Note that big numbers are included in the test data because preferred-plus serialization requires their unification with integers."
- (App. L.2, negative_bignum.edn) "Note that this is the value closest that can be represented as a big number, not a type 1 integer for preferred-plus serialization."
- (App. L.2, date_epoch_tag.edn / date_string_tag.edn) "Note that this is provided as a test case for tags.  There are no requirements for dates in this document.  The tag content in this example does vary by serialization type."
- (App. L.2, simple111.edn) "Note that the simple value 111 is of not particular significance.  It was selected because it is an unassigned simple value."
- (App. L.2, float_double_subnormal.edn) "Note that full subnormal support is required for all serializations defined in this document."
- (App. L.2, float_nan_payload.edn) "The NaN payload is a special case.  For preferred-plus and deterministic serialization, the decode should fail.  For general serialization a NaN with a payload should be returned, but there is no EDN representation for that."

The 25 example data items themselves (`zero.edn` through `float_nan_payload.edn`, source lines 2366-2886 — the 25 `File:` lines are at 2366, 2382, 2397, 2425, 2436, 2448, 2483, 2494, 2554, 2610, 2625, 2650, 2669, 2710, 2720, 2733, 2759, 2769, 2782, 2793, 2814, 2826, 2838, 2850 and 2871) are test vectors, not normative statements; they are reproduced in `distilled/examples/vectors.yaml`.

## Source defects

Reported, not repaired.

1. The document carries 65 uppercase BCP 14 keywords and lists [RFC2119] among its **normative** references, but has **no** "Conventions and Definitions" / "Requirements Language" section, no RFC 2119 boilerplate paragraph and no reference to RFC 8174. Nothing in the document says the uppercase keywords are to be interpreted as described in BCP 14.
2. §5, first sentence: "This section defines a serialization named "deterministic serialization"" — the closing full stop is missing, unlike the parallel sentence in §4.
3. §9.1: the sentence "These channels are covert because most CBOR decoders accept all such representations without raising errors or warnings." ends with a stray pilcrow character (U+00B6) in the plain-text rendering — an artefact of the HTML-to-text conversion.
4. §11.2, [LAM73]: the reference renders a Ruby hash literal instead of the journal citation — `{"name"=>"Communications of the ACM", "value"=>"16(10)"} , {"name"=>"DOI", "value"=>"10.1145/362375.362389"} ,`.
5. Appendix L.2: "CBOR libraries that don't support indefinite-length decoding can not claim to support general serialization" — "can not" for "cannot".
6. Appendix L.1.2: "The decoder should be either to be configured for, or to default to, one of the three serialization types" — ungrammatical ("either to be"); the parallel sentence in L.1.1 reads "should be either configured for, or to default to". L.1.2's opening also drops a noun: "invoke the decoder for each example data".
7. §4.1 item 1 states the umbrella rule in lowercase ("The shortest-form of the CBOR argument must be used for all major types") while its four sub-bullets use MUST; §5 likewise states the big-number rule in lowercase ("any big number that can be represented as an integer must be encoded as an integer") although §4.1 item 5 states it with MUST.
8. §7 and §10 each open with a `//`-prefixed editorial aside that is plainly meant to be removed before publication, but unlike "About This Document" neither is marked as such in a way an automated tool would catch. §7's reads "This section is new in draft-03.  The author thinks it may be out of place in this document, but there's no other good place for it yet."
9. Appendix C.2 is never cross-referenced from anywhere in the document — §3.2 points to C.1 and §4.4 points to C.5, and no text points to C.2 — and §1's Table of Contents lists "C.5.  Divergence from STD94" while the section heading reads "C.5.  Divergence from [STD94]".

**Withdrawn by the verify pass.** Pass 1 reported a tenth defect, that Appendix L's "Table 3 describes the five fields provided for each example" disagreed with a table of four body rows. It does not: Table 3 (source lines 2209-2225) has **five** body rows — `description`, `edn-representations`, `general-serializations`, `preferred-plus-serializations`, `deterministic-serialization` — and the prose says five. The fenced reproduction above carries all five. The claim is struck rather than renumbered around, so a later pass does not re-litigate it.

