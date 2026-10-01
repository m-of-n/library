---
record: rfc-9052
kind: normative
title: "rfc-9052 — normative statements"
extracted: "2026-09-30"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Section headings
mirror RFC 9052. In every bullet, all text after the "(locator)" prefix is
verbatim source text; any quotation marks inside it are the RFC's own. Fenced blocks are byte-exact source text with the RFC's
3-space left margin removed; nothing inside them is edited, reordered, or
spliced. Inline quotes are contiguous source text with line wraps joined; a
token broken across a line wrap is rejoined without an inserted space. Each
quote is a single contiguous run of source text -- no quote in this file joins
non-adjacent passages. Motivation, history, JOSE comparison, acknowledgements,
boilerplate, references, examples (Appendix C) and authors' addresses are
dropped. Locators are RFC 9052's own section and table numbers: note that CBOR
Encoding Restrictions is Section 9, Application Profiling is Section 10, IANA
Considerations is Section 11, and Security Considerations is Section 12. -->

## §1.4 CDDL Grammar for CBOR Data Structures

- (§1.4) In this specification, the following primitive types are used:
- (§1.4) The CDDL grammar is informational; the prose description is normative.
- (§1.4) CDDL expects the initial nonterminal symbol to be the first symbol in the file.  For this reason, the first fragment of CDDL is presented here.
- (§1.4) The collected CDDL can be extracted from the XML version of this document via the XPath expression below.
- (§1.4) The nonterminal Internal_Types is defined for dealing with the automated validation tools used during the writing of this document.  It references those nonterminals that are used for security computations but are not emitted for transport.

Primitive types, CDDL shorthands, and CDDL constraints used by the prose (§1.4):

```text
any:  A nonspecific value that permits all CBOR values to be placed
   here.

bool:  A boolean value (true: major type 7, value 21; false: major
   type 7, value 20).

bstr:  Byte string (major type 2).

int:  An unsigned integer or a negative integer.

nil:  A null value (major type 7, value 22).

nint:  A negative integer (major type 1).

tstr:  A UTF-8 text string (major type 3).

uint:  An unsigned integer (major type 0).

Three syntaxes from CDDL appear in this document as shorthand.  These
are:

FOO / BAR:  Indicates that either FOO or BAR can appear here.

[+ FOO]:  Indicates that the type FOO appears one or more times in an
   array.

* FOO:  Indicates that the type FOO appears zero or more times.

Two of the constraints defined by CDDL are also used in this
document.  These are:

type1 .cbor type2:  Indicates that the contents of type1, usually
   bstr, contains a value of type2.

type1 .size integer:  Indicates that the contents of type1 is integer
   bytes long.
```

XPath expression for extracting the collected CDDL (§1.4):

```text
//sourcecode[@type='cddl']/text()
```

CDDL — initial nonterminal (§1.4):

```cddl
start = COSE_Messages / COSE_Key / COSE_KeySet / Internal_Types

; This is defined to make the tool quieter:
Internal_Types = Sig_structure / Enc_structure / MAC_structure
```

## §1.5 CBOR-Related Terminology

- (§1.5) In COSE, we use text strings, negative integers, and unsigned integers as map keys.
- (§1.5) In a CBOR map defined by this specification, the presence a label that is neither a text string nor an integer is an error.
- (§1.5) Applications can either fail processing or process messages by ignoring incorrect labels; however, they MUST NOT create messages with incorrect labels.

CDDL — label and values (§1.5):

```cddl
label = int / tstr
values = any
```

## §2 Basic COSE Structure

- (§2) All of the message structures are built on the CBOR array type.
- (§2) The first three elements of the array always contain the same information:
- (§2) Elements after this point are dependent on the specific message type.
- (§2) Identification of which type of message has been presented is done by the following methods:
- (§2, method 2) This document defines a CBOR tag for each of the message structures.  These tags can be found in Table 1.
- (§2, method 3) The parameter is OPTIONAL if the tagged version of the structure is used.  The parameter is REQUIRED if the untagged version of the structure is used.
- (§2, method 3) The value to use with the parameter for each of the structures can be found in Table 1.
- (§2, method 4) The CoAP Content-Format values can be found in Table 2.  The CBOR tag for the message structure is not required, as each security message is uniquely identified.
- (§2) The following CDDL fragment identifies all of the top messages defined in this document.  Separate nonterminals are defined for the tagged and untagged versions of the messages.

The first three elements of every COSE message array (§2):

```text
1.  The protected header parameters, encoded and wrapped in a bstr.

2.  The unprotected header parameters as a map.

3.  The content of the message.  The content is either the plaintext
    or the ciphertext, as appropriate.  The content may be detached
    (i.e., transported separately from the COSE structure), but the
    location is still used.  The content is wrapped in a bstr when
    present and is a nil value when detached.
```

Message-type identification methods (§2):

```text
1.  The specific message type is known from the context.  This may be
    defined by a marker in the containing structure or by
    restrictions specified by the application protocol.

2.  The message type is identified by a CBOR tag.  Messages with a
    CBOR tag are known in this specification as tagged messages,
    while those without the CBOR tag are known as untagged messages.
    This document defines a CBOR tag for each of the message
    structures.  These tags can be found in Table 1.

3.  When a COSE object is carried in a media type of "application/
    cose", the optional parameter "cose-type" can be used to identify
    the embedded object.  The parameter is OPTIONAL if the tagged
    version of the structure is used.  The parameter is REQUIRED if
    the untagged version of the structure is used.  The value to use
    with the parameter for each of the structures can be found in
    Table 1.

4.  When a COSE object is carried as a CoAP payload, the CoAP
    Content-Format Option can be used to identify the message
    content.  The CoAP Content-Format values can be found in Table 2.
    The CBOR tag for the message structure is not required, as each
    security message is uniquely identified.
```

COSE Message Identification (Table 1):

```text
+==========+===============+===============+=======================+
| CBOR Tag | cose-type     | Data Item     | Semantics             |
+==========+===============+===============+=======================+
| 98       | cose-sign     | COSE_Sign     | COSE Signed Data      |
|          |               |               | Object                |
+----------+---------------+---------------+-----------------------+
| 18       | cose-sign1    | COSE_Sign1    | COSE Single Signer    |
|          |               |               | Data Object           |
+----------+---------------+---------------+-----------------------+
| 96       | cose-encrypt  | COSE_Encrypt  | COSE Encrypted Data   |
|          |               |               | Object                |
+----------+---------------+---------------+-----------------------+
| 16       | cose-encrypt0 | COSE_Encrypt0 | COSE Single Recipient |
|          |               |               | Encrypted Data Object |
+----------+---------------+---------------+-----------------------+
| 97       | cose-mac      | COSE_Mac      | COSE MACed Data       |
|          |               |               | Object                |
+----------+---------------+---------------+-----------------------+
| 17       | cose-mac0     | COSE_Mac0     | COSE Mac w/o          |
|          |               |               | Recipients Object     |
+----------+---------------+---------------+-----------------------+

                Table 1: COSE Message Identification
```

CoAP Content-Formats for COSE (Table 2):

```text
     +===========================+==========+=====+===========+
     | Media Type                | Encoding | ID  | Reference |
     +===========================+==========+=====+===========+
     | application/cose; cose-   |          | 98  | RFC 9052  |
     | type="cose-sign"          |          |     |           |
     +---------------------------+----------+-----+-----------+
     | application/cose; cose-   |          | 18  | RFC 9052  |
     | type="cose-sign1"         |          |     |           |
     +---------------------------+----------+-----+-----------+
     | application/cose; cose-   |          | 96  | RFC 9052  |
     | type="cose-encrypt"       |          |     |           |
     +---------------------------+----------+-----+-----------+
     | application/cose; cose-   |          | 16  | RFC 9052  |
     | type="cose-encrypt0"      |          |     |           |
     +---------------------------+----------+-----+-----------+
     | application/cose; cose-   |          | 97  | RFC 9052  |
     | type="cose-mac"           |          |     |           |
     +---------------------------+----------+-----+-----------+
     | application/cose; cose-   |          | 17  | RFC 9052  |
     | type="cose-mac0"          |          |     |           |
     +---------------------------+----------+-----+-----------+
     | application/cose-key      |          | 101 | RFC 9052  |
     +---------------------------+----------+-----+-----------+
     | application/cose-key-set  |          | 102 | RFC 9052  |
     +---------------------------+----------+-----+-----------+

               Table 2: CoAP Content-Formats for COSE
```

CDDL — top-level messages (§2):

```cddl
COSE_Messages = COSE_Untagged_Message / COSE_Tagged_Message

COSE_Untagged_Message = COSE_Sign / COSE_Sign1 /
    COSE_Encrypt / COSE_Encrypt0 /
    COSE_Mac / COSE_Mac0

COSE_Tagged_Message = COSE_Sign_Tagged / COSE_Sign1_Tagged /
    COSE_Encrypt_Tagged / COSE_Encrypt0_Tagged /
    COSE_Mac_Tagged / COSE_Mac0_Tagged
```

## §3 Header Parameters

- (§3) Both buckets are implemented as CBOR maps.
- (§3) The map key is a "label" (Section 1.5).
- (§3) Both maps use the same set of label/value pairs.
- (§3) The defined labels can be found in the "COSE Header Parameters" IANA registry (Section 11.1).
- (§3, protected) Contains parameters about the current layer that are cryptographically protected.
- (§3, protected) This bucket MUST be empty if it is not going to be included in a cryptographic computation.
- (§3, protected) This bucket is encoded in the message as a binary object.  This value is obtained by CBOR encoding the protected map and wrapping it in a bstr object.
- (§3, protected) Senders SHOULD encode a zero-length map as a zero-length byte string rather than as a zero-length map (encoded as h'a0').
- (§3, protected) Recipients MUST accept both a zero-length byte string and a zero-length map encoded in a byte string.
- (§3, protected) This avoids the problem of all parties needing to be able to do a common canonical encoding of the map for input to cryptographic operations.
- (§3, unprotected) Contains parameters about the current layer that are not cryptographically protected.
- (§3) Only header parameters that deal with the current layer are to be placed at that layer.
- (§3) The buckets are present in all of the security objects defined in this document.  The fields, in order, are the "protected" bucket (as a CBOR "bstr" type) and then the "unprotected" bucket (as a CBOR "map" type).  The presence of both buckets is required.
- (§3) Labels in each of the maps MUST be unique.  When processing messages, if a label appears multiple times, the message MUST be rejected as malformed.
- (§3) Applications SHOULD verify that the same label does not occur in both the protected and unprotected header parameters.
- (§3) If the message is not rejected as malformed, attributes MUST be obtained from the protected bucket, and only if an attribute is not found in the protected bucket can that attribute be obtained from the unprotected bucket.

The two header-parameter buckets, in full (§3):

```text
The two buckets are:

protected:  Contains parameters about the current layer that are
   cryptographically protected.  This bucket MUST be empty if it is
   not going to be included in a cryptographic computation.  This
   bucket is encoded in the message as a binary object.  This value
   is obtained by CBOR encoding the protected map and wrapping it in
   a bstr object.  Senders SHOULD encode a zero-length map as a zero-
   length byte string rather than as a zero-length map (encoded as
   h'a0').  The zero-length byte string encoding is preferred,
   because it is both shorter and the version used in the
   serialization structures for cryptographic computation.
   Recipients MUST accept both a zero-length byte string and a zero-
   length map encoded in a byte string.

   Wrapping the encoding with a byte string allows the protected map
   to be transported with a greater chance that it will not be
   altered accidentally in transit.  (Badly behaved intermediates
   could decode and re-encode, but this will result in a failure to
   verify unless the re-encoded byte string is identical to the
   decoded byte string.)  This avoids the problem of all parties
   needing to be able to do a common canonical encoding of the map
   for input to cryptographic operations.

unprotected:  Contains parameters about the current layer that are
   not cryptographically protected.
```

CDDL — Headers group, header_map, empty_or_serialized_map (§3):

```cddl
Headers = (
    protected : empty_or_serialized_map,
    unprotected : header_map
)

header_map = {
    Generic_Headers,
    * label => values
}

empty_or_serialized_map = bstr .cbor header_map / bstr .size 0
```

## §3.1 Common COSE Header Parameters

- (§3.1, alg) This header parameter is used to indicate the algorithm used for the security processing.
- (§3.1, alg) This header parameter MUST be authenticated where the ability to do so exists.
- (§3.1, alg) This authentication can be done either by placing the header parameter in the protected-header-parameters bucket or as part of the externally supplied data (Section 4.3).
- (§3.1, alg) The value is taken from the "COSE Algorithms" registry (see [COSE.Algorithms]).
- (§3.1, crit) This header parameter is used to indicate which protected header parameters an application that is processing a message is required to understand.
- (§3.1, crit) Header parameters defined in this document do not need to be included, as they should be understood by all implementations.
- (§3.1, crit) Additionally, the header parameter "counter signature" (label 7) defined by [RFC8152] must be understood by new implementations, to remain compatible with senders that adhere to that document and assume all implementations will understand it.
- (§3.1, crit) When present, the "crit" header parameter MUST be placed in the protected-header-parameters bucket.  The array MUST have at least one value in it.
- (§3.1, crit) Integer labels in the range of 0 to 7 SHOULD be omitted.
- (§3.1, crit) Integer labels in the range -129 to -65536 SHOULD be included, as these would be less common header parameters that might not be generally supported.
- (§3.1, crit) Labels for header parameters required for an application MAY be omitted.
- (§3.1, crit) The header parameters indicated by "crit" can be processed by either the security-library code or an application using a security library; the only requirement is that the header parameter is processed.
- (§3.1, crit) If the "crit" value list includes a label for which the header parameter is not in the protected-header-parameters bucket, this is a fatal error in processing the message.
- (§3.1, content type) Integers are from the "CoAP Content-Formats" IANA registry table [COAP.Formats].
- (§3.1, content type) Text values follow the syntax of "<type-name>/<subtype-name>", where <type-name> and <subtype-name> are defined in Section 4.2 of [RFC6838].
- (§3.1, content type) Leading and trailing whitespace is not permitted.
- (§3.1, content type) Applications SHOULD provide this header parameter if the content structure is potentially ambiguous.
- (§3.1, kid) Applications MUST NOT assume that "kid" values are unique.
- (§3.1, kid) The internal structure of "kid" values is not defined and cannot be relied on by applications.
- (§3.1, Partial IV) The "Initialization Vector" and "Partial Initialization Vector" header parameters MUST NOT both be present in the same security layer.
- (§3.1, Partial IV) The message IV is generated by the following steps:

Rules for deciding which header parameters are placed in the "crit" array (§3.1, crit):

```text
   Not all header-parameter labels need to be included in the "crit"
   header parameter.  The rules for deciding which header parameters
   are placed in the array are:

   *  Integer labels in the range of 0 to 7 SHOULD be omitted.

   *  Integer labels in the range -1 to -128 can be omitted.
      Algorithms can assign labels in this range where the ability to
      process the content of the label is considered to be core to
      implementing the algorithm.  Algorithms can assign labels
      outside of this range and include them in the "crit" header
      parameter when the ability to process the content of the label
      is not considered to be core functionality of the algorithm but
      does need to be understood to correctly process this instance.
      Integer labels in the range -129 to -65536 SHOULD be included,
      as these would be less common header parameters that might not
      be generally supported.

   *  Labels for header parameters required for an application MAY be
      omitted.  Applications should have a statement declaring
      whether or not the label can be omitted.

   The header parameters indicated by "crit" can be processed by
   either the security-library code or an application using a
   security library; the only requirement is that the header
   parameter is processed.  If the "crit" value list includes a label
   for which the header parameter is not in the protected-header-
   parameters bucket, this is a fatal error in processing the
   message.
```

Message IV derivation steps (§3.1, Partial IV):

```text
   1.  Left-pad the Partial IV with zeros to the length of IV
       (determined by the algorithm).

   2.  XOR the padded Partial IV with the Context IV.
```

Common Header Parameters (Table 3):

```text
+=========+=======+========+=====================+==================+
| Name    | Label | Value  | Value Registry      | Description      |
|         |       | Type   |                     |                  |
+=========+=======+========+=====================+==================+
| alg     | 1     | int /  | COSE Algorithms     | Cryptographic    |
|         |       | tstr   | registry            | algorithm to use |
+---------+-------+--------+---------------------+------------------+
| crit    | 2     | [+     | COSE Header         | Critical header  |
|         |       | label] | Parameters          | parameters to be |
|         |       |        | registry            | understood       |
+---------+-------+--------+---------------------+------------------+
| content | 3     | tstr / | CoAP Content-       | Content type of  |
| type    |       | uint   | Formats or Media    | the payload      |
|         |       |        | Types registries    |                  |
+---------+-------+--------+---------------------+------------------+
| kid     | 4     | bstr   |                     | Key identifier   |
+---------+-------+--------+---------------------+------------------+
| IV      | 5     | bstr   |                     | Full             |
|         |       |        |                     | Initialization   |
|         |       |        |                     | Vector           |
+---------+-------+--------+---------------------+------------------+
| Partial | 6     | bstr   |                     | Partial          |
| IV      |       |        |                     | Initialization   |
|         |       |        |                     | Vector           |
+---------+-------+--------+---------------------+------------------+

                  Table 3: Common Header Parameters
```

CDDL — Generic_Headers (§3.1):

```cddl
Generic_Headers = (
    ? 1 => int / tstr,  ; algorithm identifier
    ? 2 => [+label],    ; criticality
    ? 3 => tstr / int,  ; content type
    ? 4 => bstr,        ; key identifier
    ? ( 5 => bstr //    ; IV
        6 => bstr )     ; Partial IV
)
```

## §4 Signing Objects

- (§4) COSE_Sign allows for one or more signatures to be applied to the same content.  COSE_Sign1 is restricted to a single signer.
- (§4) The structures cannot be converted between each other; as the signature computation includes a parameter identifying which structure is being used, the converted structure will fail signature validation.

### §4.1 Signing with One or More Signers

- (§4.1) A tagged COSE_Sign structure is identified by the CBOR tag 98.
- (§4.1) The COSE_Sign structure is a CBOR array.  The fields of the array, in order, are:
- (§4.1, payload) This field contains the serialized content to be signed.  If the payload is not present in the message, the application is required to supply the payload separately.
- (§4.1, payload) The payload is wrapped in a bstr to ensure that it is transported without changes.  If the payload is transported separately ("detached content"), then a nil CBOR object is placed in this location, and it is the responsibility of the application to ensure that it will be transported without changes.
- (§4.1, payload) If all of the bytes of the original payload are consumed, then the transmitted payload is encoded as a zero-length byte string rather than as being absent.
- (§4.1) The COSE_Signature structure is a CBOR array.  The fields of the array, in order, are:
- (§4.1, signature) This field contains the computed signature value.  The type of the field is a bstr.  Algorithms MUST specify padding if the signature value is not a multiple of 8 bits.

Multiple signatures — the passage §4.1 quotes from [RFC5652] (§4.1):

```text
|  When more than one signature is present, the successful validation
|  of one signature associated with a given signer is usually treated
|  as a successful signature by that signer.  However, there are some
|  application environments where other rules are needed.  An
|  application that employs a rule other than one valid signature for
|  each signer must specify those rules.  Also, where simple matching
|  of the signer identifier is not sufficient to determine whether
|  the signatures were generated by the same signer, the application
|  specification must describe how to determine which signatures were
|  generated by the same signer.  Support of different communities of
|  recipients is the primary reason that signers choose to include
|  more than one signature.
```

CDDL — COSE_Sign_Tagged (§4.1):

```cddl
COSE_Sign_Tagged = #6.98(COSE_Sign)
```

COSE_Sign fields, in order (§4.1):

```text
The COSE_Sign structure is a CBOR array.  The fields of the array, in
order, are:

protected:  This is as described in Section 3.

unprotected:  This is as described in Section 3.

payload:  This field contains the serialized content to be signed.
   If the payload is not present in the message, the application is
   required to supply the payload separately.  The payload is wrapped
   in a bstr to ensure that it is transported without changes.  If
   the payload is transported separately ("detached content"), then a
   nil CBOR object is placed in this location, and it is the
   responsibility of the application to ensure that it will be
   transported without changes.

   Note: When a signature with a message recovery algorithm is used
   (Section 8.1), the maximum number of bytes that can be recovered
   is the length of the original payload.  The size of the encoded
   payload is reduced by the number of bytes that will be recovered.
   If all of the bytes of the original payload are consumed, then the
   transmitted payload is encoded as a zero-length byte string rather
   than as being absent.

signatures:  This field is an array of signatures.  Each signature is
   represented as a COSE_Signature structure.
```

CDDL — COSE_Sign (§4.1):

```cddl
COSE_Sign = [
    Headers,
    payload : bstr / nil,
    signatures : [+ COSE_Signature]
]
```

COSE_Signature fields, in order (§4.1):

```text
The COSE_Signature structure is a CBOR array.  The fields of the
array, in order, are:

protected:  This is as described in Section 3.

unprotected:  This is as described in Section 3.

signature:  This field contains the computed signature value.  The
   type of the field is a bstr.  Algorithms MUST specify padding if
   the signature value is not a multiple of 8 bits.
```

CDDL — COSE_Signature (§4.1):

```cddl
COSE_Signature =  [
    Headers,
    signature : bstr
]
```

### §4.2 Signing with One Signer

- (§4.2) A tagged COSE_Sign1 structure is identified by the CBOR tag 18.
- (§4.2) The COSE_Sign1 structure is a CBOR array.  The fields of the array, in order, are:

CDDL — COSE_Sign1_Tagged (§4.2):

```cddl
COSE_Sign1_Tagged = #6.18(COSE_Sign1)
```

COSE_Sign1 fields, in order (§4.2):

```text
The COSE_Sign1 structure is a CBOR array.  The fields of the array,
in order, are:

protected:  This is as described in Section 3.

unprotected:  This is as described in Section 3.

payload:  This is as described in Section 4.1.

signature:  This field contains the computed signature value.  The
   type of the field is a bstr.
```

CDDL — COSE_Sign1 (§4.2):

```cddl
COSE_Sign1 = [
    Headers,
    payload : bstr / nil,
    signature : bstr
]
```

### §4.3 Externally Supplied Data

- (§4.3) This document describes the process for using a byte array of externally supplied authenticated data; the method of constructing the byte array is a function of the application.
- (§4.3) Applications that use this feature need to define how the externally supplied authenticated data is to be constructed.  Such a construction needs to take into account the following issues:
- (§4.3) If multiple items are included, applications need to ensure that the same byte string cannot be produced if there are different inputs.
- (§4.3) If multiple items are included, an order for the items needs to be defined.
- (§4.3) Applications need to ensure that the byte string is going to be the same on both sides.

Constraints on constructing the externally supplied authenticated data (§4.3):

```text
*  If multiple items are included, applications need to ensure that
   the same byte string cannot be produced if there are different
   inputs.  An example of how the problematic scenario could arise
   would be by concatenating the text strings "AB" and "CDE" or by
   concatenating the text strings "ABC" and "DE".  This is usually
   addressed by making fields a fixed width and/or encoding the
   length of the field as part of the output.  Using options from
   CoAP [RFC7252] as an example, these fields use a TLV structure so
   they can be concatenated without any problems.

*  If multiple items are included, an order for the items needs to be
   defined.  Using options from CoAP as an example, an application
   could state that the fields are to be ordered by the option
   number.

*  Applications need to ensure that the byte string is going to be
   the same on both sides.  Using options from CoAP might give a
   problem if the same relative numbering is kept.  An intermediate
   node could insert or remove an option, changing how the relative
   numbering is done.  An application would need to specify that the
   relative number must be re-encoded to be relative only to the
   options that are in the external data.
```

### §4.4 Signing and Verification Process

- (§4.4) In order to create a signature, a well-defined byte string is needed.  The Sig_structure is used to create the canonical form.
- (§4.4) This signing and verification process takes in the body information (COSE_Sign or COSE_Sign1), the signer information (COSE_Signature), and the application data (external source).
- (§4.4) A Sig_structure is a CBOR array.  The fields of the Sig_structure, in order, are:
- (§4.4, field 1) A context text string identifying the context of the signature.
- (§4.4, field 1) "Signature" for signatures using the COSE_Signature structure.
- (§4.4, field 1) "Signature1" for signatures using the COSE_Sign1 structure.
- (§4.4, field 2) The protected attributes from the body structure, encoded in a bstr type.  If there are no protected attributes, a zero-length byte string is used.
- (§4.4, field 3) The protected attributes from the signer structure, encoded in a bstr type.  If there are no protected attributes, a zero-length byte string is used.  This field is omitted for the COSE_Sign1 signature structure.
- (§4.4, field 4) The externally supplied data from the application, encoded in a bstr type.  If this field is not supplied, it defaults to a zero-length byte string.
- (§4.4, field 5) The payload to be signed, encoded in a bstr type.  The full payload is used here, independent of how it is transported.
- (§4.4) Create a Sig_structure and populate it with the appropriate fields.
- (§4.4) Create the value ToBeSigned by encoding the Sig_structure to a byte string, using the encoding described in Section 9.
- (§4.4) Call the signature creation algorithm, passing in K (the key to sign with), alg (the algorithm to sign with), and ToBeSigned (the value to sign).
- (§4.4) Place the resulting signature value in the correct location.  This is the "signature" field of the COSE_Signature or COSE_Sign1 structure.
- (§4.4) Call the signature verification algorithm, passing in K (the key to verify with), alg (the algorithm used to sign with), ToBeSigned (the value to sign), and sig (the signature to be verified).
- (§4.4) In addition to performing the signature verification, the application performs the appropriate checks to ensure that the key is correctly paired with the signing identity and that the signing identity is authorized before performing actions.

Sig_structure fields, in order — the exact byte-string construction (§4.4):

```text
1.  A context text string identifying the context of the signature.
    The context text string is:

       "Signature" for signatures using the COSE_Signature structure.

       "Signature1" for signatures using the COSE_Sign1 structure.

2.  The protected attributes from the body structure, encoded in a
    bstr type.  If there are no protected attributes, a zero-length
    byte string is used.

3.  The protected attributes from the signer structure, encoded in a
    bstr type.  If there are no protected attributes, a zero-length
    byte string is used.  This field is omitted for the COSE_Sign1
    signature structure.

4.  The externally supplied data from the application, encoded in a
    bstr type.  If this field is not supplied, it defaults to a zero-
    length byte string.  (See Section 4.3 for application guidance on
    constructing this field.)

5.  The payload to be signed, encoded in a bstr type.  The full
    payload is used here, independent of how it is transported.
```

CDDL — Sig_structure (§4.4):

```cddl
Sig_structure = [
    context : "Signature" / "Signature1",
    body_protected : empty_or_serialized_map,
    ? sign_protected : empty_or_serialized_map,
    external_aad : bstr,
    payload : bstr
]
```

How to compute a signature (§4.4):

```text
How to compute a signature:

1.  Create a Sig_structure and populate it with the appropriate
    fields.

2.  Create the value ToBeSigned by encoding the Sig_structure to a
    byte string, using the encoding described in Section 9.

3.  Call the signature creation algorithm, passing in K (the key to
    sign with), alg (the algorithm to sign with), and ToBeSigned (the
    value to sign).

4.  Place the resulting signature value in the correct location.
    This is the "signature" field of the COSE_Signature or COSE_Sign1
    structure.
```

The steps for verifying a signature (§4.4):

```text
The steps for verifying a signature are:

1.  Create a Sig_structure and populate it with the appropriate
    fields.

2.  Create the value ToBeSigned by encoding the Sig_structure to a
    byte string, using the encoding described in Section 9.

3.  Call the signature verification algorithm, passing in K (the key
    to verify with), alg (the algorithm used to sign with),
    ToBeSigned (the value to sign), and sig (the signature to be
    verified).
```

## §5 Encryption Objects

- (§5) COSE_Encrypt0 is used when a recipient structure is not needed because the key to be used is known implicitly.  COSE_Encrypt is used the rest of the time.

### §5.1 Enveloped COSE Structure

- (§5.1) The protected header parameters associated with the content are authenticated by the content encryption algorithm.  The protected header parameters associated with the recipient (when the algorithm supports it) are authenticated by the recipient algorithm.
- (§5.1) A tagged COSE_Encrypt structure is identified by the CBOR tag 96.
- (§5.1) The COSE_Encrypt structure is a CBOR array.  The fields of the array, in order, are:
- (§5.1, ciphertext) This field contains the ciphertext, encoded as a bstr.  If the ciphertext is to be transported independently of the control information about the encryption process (i.e., detached content), then the field is encoded as a nil value.
- (§5.1) The COSE_recipient structure is a CBOR array.  The fields of the array, in order, are:
- (§5.1, COSE_recipient ciphertext) This field contains the encrypted key, encoded as a bstr.  All encoded keys are symmetric keys; the binary value of the key is the content.  If there is not an encrypted key, then this field is encoded as a nil value.
- (§5.1, COSE_recipient recipients) If there are no recipient information structures, this element is absent.

CDDL — COSE_Encrypt_Tagged (§5.1):

```cddl
COSE_Encrypt_Tagged = #6.96(COSE_Encrypt)
```

COSE_Encrypt fields, in order (§5.1):

```text
The COSE_Encrypt structure is a CBOR array.  The fields of the array,
in order, are:

protected:  This is as described in Section 3.

unprotected:  This is as described in Section 3.

ciphertext:  This field contains the ciphertext, encoded as a bstr.
   If the ciphertext is to be transported independently of the
   control information about the encryption process (i.e., detached
   content), then the field is encoded as a nil value.

recipients:  This field contains an array of recipient information
   structures.  The type for the recipient information structure is a
   COSE_recipient.
```

CDDL — COSE_Encrypt (§5.1):

```cddl
COSE_Encrypt = [
    Headers,
    ciphertext : bstr / nil,
    recipients : [+COSE_recipient]
]
```

COSE_recipient fields, in order (§5.1):

```text
The COSE_recipient structure is a CBOR array.  The fields of the
array, in order, are:

protected:  This is as described in Section 3.

unprotected:  This is as described in Section 3.

ciphertext:  This field contains the encrypted key, encoded as a
   bstr.  All encoded keys are symmetric keys; the binary value of
   the key is the content.  If there is not an encrypted key, then
   this field is encoded as a nil value.

recipients:  This field contains an array of recipient information
   structures.  The type for the recipient information structure is a
   COSE_recipient (an example of this can be found in Appendix B).
   If there are no recipient information structures, this element is
   absent.
```

CDDL — COSE_recipient (§5.1):

```cddl
COSE_recipient = [
    Headers,
    ciphertext : bstr / nil,
    ? recipients : [+COSE_recipient]
]
```

#### §5.1.1 Content Key Distribution Methods

- (§5.1.1) An encrypted message consists of an encrypted content and an encrypted CEK for one or more recipients.  The CEK is encrypted for each recipient, using a key specific to that recipient.
- (§5.1.1) The details of this encryption depend on which class the recipient algorithm falls into.

The five content key distribution methods (§5.1.1):

```text
direct:  The CEK is the same as the identified previously distributed
   symmetric key or is derived from a previously distributed secret.
   No CEK is transported in the message.

symmetric key-encryption keys (KEKs):  The CEK is encrypted using a
   previously distributed symmetric KEK.  Also known as key wrap.

key agreement:  The recipient's public key and a sender's private key
   are used to generate a pairwise secret, a Key Derivation Function
   (KDF) is applied to derive a key, and then the CEK is either the
   derived key or encrypted by the derived key.

key transport:  The CEK is encrypted with the recipient's public key.

passwords:  The CEK is encrypted in a KEK that is derived from a
   password.  As of when this document was published, no password
   algorithms have been defined.
```

### §5.2 Single Recipient Encrypted

- (§5.2) The COSE_Encrypt0 encrypted structure does not have the ability to specify recipients of the message.  The structure assumes that the recipient of the object will already know the identity of the key to be used in order to decrypt the message.
- (§5.2) If a key needs to be identified to the recipient, the enveloped structure ought to be used.
- (§5.2) A tagged COSE_Encrypt0 structure is identified by the CBOR tag 16.
- (§5.2) The COSE_Encrypt0 structure is a CBOR array.  The fields of the array, in order, are:

CDDL — COSE_Encrypt0_Tagged (§5.2):

```cddl
COSE_Encrypt0_Tagged = #6.16(COSE_Encrypt0)
```

COSE_Encrypt0 fields, in order (§5.2):

```text
The COSE_Encrypt0 structure is a CBOR array.  The fields of the
array, in order, are:

protected:  This is as described in Section 3.

unprotected:  This is as described in Section 3.

ciphertext:  This is as described in Section 5.1.
```

CDDL — COSE_Encrypt0 (§5.2):

```cddl
COSE_Encrypt0 = [
    Headers,
    ciphertext : bstr / nil,
]
```

### §5.3 How to Encrypt and Decrypt for AEAD Algorithms

- (§5.3) The first step is to create a consistent byte string for the authenticated data structure.  For this purpose, we use an Enc_structure.
- (§5.3) The Enc_structure is a CBOR array.  The fields of the Enc_structure, in order, are:
- (§5.3, field 1) A context text string identifying the context of the authenticated data structure.
- (§5.3, field 1) "Encrypt0" for the content encryption of a COSE_Encrypt0 data structure.
- (§5.3, field 1) "Encrypt" for the first layer of a COSE_Encrypt data structure (i.e., for content encryption).
- (§5.3, field 1) "Enc_Recipient" for a recipient encoding to be placed in a COSE_Encrypt data structure.
- (§5.3, field 1) "Mac_Recipient" for a recipient encoding to be placed in a MACed message structure.
- (§5.3, field 1) "Rec_Recipient" for a recipient encoding to be placed in a recipient structure.
- (§5.3, field 2) The protected attributes from the body structure, encoded in a bstr type.  If there are no protected attributes, a zero-length byte string is used.
- (§5.3, field 3) The externally supplied data from the application encoded in a bstr type.  If this field is not supplied, it defaults to a zero-length byte string.
- (§5.3) Encode the Enc_structure to a byte string (Additional Authenticated Data (AAD)), using the encoding described in Section 9.
- (§5.3) Call the encryption algorithm with K (the encryption key), P (the plaintext), and AAD.  Place the returned ciphertext into the "ciphertext" field of the structure.
- (§5.3) For recipients of the message using non-direct algorithms, recursively perform the encryption algorithm for that recipient, using K (the encryption key) as the plaintext.
- (§5.3) Encode the Enc_structure to a byte string (AAD), using the encoding described in Section 9.
- (§5.3) Call the decryption algorithm with K (the decryption key to use), C (the ciphertext), and AAD.

Enc_structure fields, in order — the exact byte-string construction (§5.3):

```text
1.  A context text string identifying the context of the
    authenticated data structure.  The context text string is:

       "Encrypt0" for the content encryption of a COSE_Encrypt0 data
       structure.

       "Encrypt" for the first layer of a COSE_Encrypt data structure
       (i.e., for content encryption).

       "Enc_Recipient" for a recipient encoding to be placed in a
       COSE_Encrypt data structure.

       "Mac_Recipient" for a recipient encoding to be placed in a
       MACed message structure.

       "Rec_Recipient" for a recipient encoding to be placed in a
       recipient structure.

2.  The protected attributes from the body structure, encoded in a
    bstr type.  If there are no protected attributes, a zero-length
    byte string is used.

3.  The externally supplied data from the application encoded in a
    bstr type.  If this field is not supplied, it defaults to a zero-
    length byte string.  (See Section 4.3 for application guidance on
    constructing this field.)
```

CDDL — Enc_structure (§5.3):

```cddl
Enc_structure = [
    context : "Encrypt" / "Encrypt0" / "Enc_Recipient" /
        "Mac_Recipient" / "Rec_Recipient",
    protected : empty_or_serialized_map,
    external_aad : bstr
]
```

How to encrypt a message (§5.3):

```text
How to encrypt a message:

1.  Create an Enc_structure and populate it with the appropriate
    fields.

2.  Encode the Enc_structure to a byte string (Additional
    Authenticated Data (AAD)), using the encoding described in
    Section 9.

3.  Determine the encryption key (K).  This step is dependent on the
    class of recipient algorithm being used.  For:

    No Recipients:  The key to be used is determined by the algorithm
       and key at the current layer.  Examples are key wrap keys
       (Section 8.5.2) and preshared secrets.

    Direct Encryption and Direct Key Agreement:  The key is
       determined by the key and algorithm in the recipient
       structure.  The encryption algorithm and size of the key to be
       used are inputs into the KDF used for the recipient.  (For
       direct, the KDF can be thought of as the identity operation.)
       Examples of these algorithms are found in Sections 6.1 and 6.3
       of [RFC9053].

    Other:  The key is randomly generated.

4.  Call the encryption algorithm with K (the encryption key), P (the
    plaintext), and AAD.  Place the returned ciphertext into the
    "ciphertext" field of the structure.

5.  For recipients of the message using non-direct algorithms,
    recursively perform the encryption algorithm for that recipient,
    using K (the encryption key) as the plaintext.
```

How to decrypt a message (§5.3):

```text
How to decrypt a message:

1.  Create an Enc_structure and populate it with the appropriate
    fields.

2.  Encode the Enc_structure to a byte string (AAD), using the
    encoding described in Section 9.

3.  Determine the decryption key.  This step is dependent on the
    class of recipient algorithm being used.  For:

    No Recipients:  The key to be used is determined by the algorithm
       and key at the current layer.  Examples are key wrap keys
       (Section 8.5.2) and preshared secrets.

    Direct Encryption and Direct Key Agreement:  The key is
       determined by the key and algorithm in the recipient
       structure.  The encryption algorithm and size of the key to be
       used are inputs into the KDF used for the recipient.  (For
       direct, the KDF can be thought of as the identity operation.)

    Other:  The key is determined by decoding and decrypting one of
       the recipient structures.

4.  Call the decryption algorithm with K (the decryption key to use),
    C (the ciphertext), and AAD.
```

### §5.4 How to Encrypt and Decrypt for AE Algorithms

- (§5.4) Verify that the "protected" field is a zero-length byte string.
- (§5.4) Verify that there was no external additional authenticated data supplied for this operation.
- (§5.4) Call the encryption algorithm with K (the encryption key to use) and P (the plaintext).  Place the returned ciphertext into the "ciphertext" field of the structure.
- (§5.4) Call the decryption algorithm with K (the decryption key to use) and C (the ciphertext).

How to encrypt a message (§5.4):

```text
How to encrypt a message:

1.  Verify that the "protected" field is a zero-length byte string.

2.  Verify that there was no external additional authenticated data
    supplied for this operation.

3.  Determine the encryption key.  This step is dependent on the
    class of recipient algorithm being used.  For:

    No Recipients:  The key to be used is determined by the algorithm
       and key at the current layer.  Examples are key wrap keys
       (Section 8.5.2) and preshared secrets.

    Direct Encryption and Direct Key Agreement:  The key is
       determined by the key and algorithm in the recipient
       structure.  The encryption algorithm and size of the key to be
       used are inputs into the KDF used for the recipient.  (For
       direct, the KDF can be thought of as the identity operation.)
       Examples of these algorithms are found in Sections 6.1 and 6.3
       of [RFC9053].

    Other:  The key is randomly generated.

4.  Call the encryption algorithm with K (the encryption key to use)
    and P (the plaintext).  Place the returned ciphertext into the
    "ciphertext" field of the structure.

5.  For recipients of the message using non-direct algorithms,
    recursively perform the encryption algorithm for that recipient,
    using K (the encryption key) as the plaintext.
```

How to decrypt a message (§5.4):

```text
How to decrypt a message:

1.  Verify that the "protected" field is a zero-length byte string.

2.  Verify that there was no external additional authenticated data
    supplied for this operation.

3.  Determine the decryption key.  This step is dependent on the
    class of recipient algorithm being used.  For:

    No Recipients:  The key to be used is determined by the algorithm
       and key at the current layer.  Examples are key wrap keys
       (Section 8.5.2) and preshared secrets.

    Direct Encryption and Direct Key Agreement:  The key is
       determined by the key and algorithm in the recipient
       structure.  The encryption algorithm and size of the key to be
       used are inputs into the KDF used for the recipient.  (For
       direct, the KDF can be thought of as the identity operation.)
       Examples of these algorithms are found in Sections 6.1 and 6.3
       of [RFC9053].

    Other:  The key is determined by decoding and decrypting one of
       the recipient structures.

4.  Call the decryption algorithm with K (the decryption key to use)
    and C (the ciphertext).
```

## §6 MAC Objects

- (§6) COSE_Mac0 is used when a recipient structure is not needed because the key to be used is implicitly known.  COSE_Mac is used for all other cases.
- (§6) The classes of recipient algorithms that support this are those that use a preshared secret or do Static-Static (SS) key agreement (without the key wrap step).

### §6.1 MACed Message with Recipients

- (§6.1) A tagged COSE_Mac structure is identified by the CBOR tag 97.
- (§6.1) The COSE_Mac structure is a CBOR array.  The fields of the array, in order, are:
- (§6.1, payload) This field contains the serialized content to be MACed.  If the payload is not present in the message, the application is required to supply the payload separately.
- (§6.1, payload) The payload is wrapped in a bstr to ensure that it is transported without changes.  If the payload is transported separately (i.e., detached content), then a nil CBOR value is placed in this location, and it is the responsibility of the application to ensure that it will be transported without changes.
- (§6.1, tag) This field contains the MAC value.

CDDL — COSE_Mac_Tagged (§6.1):

```cddl
COSE_Mac_Tagged = #6.97(COSE_Mac)
```

COSE_Mac fields, in order (§6.1):

```text
The COSE_Mac structure is a CBOR array.  The fields of the array, in
order, are:

protected:  This is as described in Section 3.

unprotected:  This is as described in Section 3.

payload:  This field contains the serialized content to be MACed.  If
   the payload is not present in the message, the application is
   required to supply the payload separately.  The payload is wrapped
   in a bstr to ensure that it is transported without changes.  If
   the payload is transported separately (i.e., detached content),
   then a nil CBOR value is placed in this location, and it is the
   responsibility of the application to ensure that it will be
   transported without changes.

tag:  This field contains the MAC value.

recipients:  This is as described in Section 5.1.
```

CDDL — COSE_Mac (§6.1):

```cddl
COSE_Mac = [
   Headers,
   payload : bstr / nil,
   tag : bstr,
   recipients : [+COSE_recipient]
]
```

### §6.2 MACed Messages with Implicit Key

- (§6.2) A tagged COSE_Mac0 structure is identified by the CBOR tag 17.
- (§6.2) The COSE_Mac0 structure is a CBOR array.  The fields of the array, in order, are:

CDDL — COSE_Mac0_Tagged (§6.2):

```cddl
COSE_Mac0_Tagged = #6.17(COSE_Mac0)
```

COSE_Mac0 fields, in order (§6.2):

```text
The COSE_Mac0 structure is a CBOR array.  The fields of the array, in
order, are:

protected:  This is as described in Section 3.

unprotected:  This is as described in Section 3.

payload:  This is as described in Section 6.1.

tag:  This field contains the MAC value.
```

CDDL — COSE_Mac0 (§6.2):

```cddl
COSE_Mac0 = [
   Headers,
   payload : bstr / nil,
   tag : bstr,
]
```

### §6.3 How to Compute and Verify a MAC

- (§6.3) In order to get a consistent encoding of the data to be authenticated, the MAC_structure is used to create the canonical form.
- (§6.3) The MAC_structure is a CBOR array.  The fields of the MAC_structure, in order, are:
- (§6.3, field 1) A context text string that identifies the structure that is being encoded.  This context text string is "MAC" for the COSE_Mac structure.  This context text string is "MAC0" for the COSE_Mac0 structure.
- (§6.3, field 2) The protected attributes from the body structure.  If there are no protected attributes, a zero-length bstr is used.
- (§6.3, field 3) The externally supplied data from the application, encoded as a bstr type.  If this field is not supplied, it defaults to a zero-length byte string.
- (§6.3, field 4) The payload to be MACed, encoded in a bstr type.  The full payload is used here, independent of how it is transported.
- (§6.3) Create the value ToBeMaced by encoding the MAC_structure to a byte string, using the encoding described in Section 9.
- (§6.3) Call the MAC creation algorithm, passing in K (the key to use), alg (the algorithm to MAC with), and ToBeMaced (the value to compute the MAC on).
- (§6.3) Place the resulting MAC in the "tag" field of the COSE_Mac or COSE_Mac0 structure.
- (§6.3) For COSE_Mac structures, encrypt and encode the MAC key for each recipient of the message.
- (§6.3) For COSE_Mac structures, obtain the cryptographic key by decoding and decrypting one of the recipient structures.
- (§6.3) Compare the MAC value to the "tag" field of the COSE_Mac or COSE_Mac0 structure.

MAC_structure fields, in order — the exact byte-string construction (§6.3):

```text
1.  A context text string that identifies the structure that is being
    encoded.  This context text string is "MAC" for the COSE_Mac
    structure.  This context text string is "MAC0" for the COSE_Mac0
    structure.

2.  The protected attributes from the body structure.  If there are
    no protected attributes, a zero-length bstr is used.

3.  The externally supplied data from the application, encoded as a
    bstr type.  If this field is not supplied, it defaults to a zero-
    length byte string.  (See Section 4.3 for application guidance on
    constructing this field.)

4.  The payload to be MACed, encoded in a bstr type.  The full
    payload is used here, independent of how it is transported.
```

CDDL — MAC_structure (§6.3):

```cddl
MAC_structure = [
     context : "MAC" / "MAC0",
     protected : empty_or_serialized_map,
     external_aad : bstr,
     payload : bstr
]
```

The steps to compute a MAC (§6.3):

```text
The steps to compute a MAC are:

1.  Create a MAC_structure and populate it with the appropriate
    fields.

2.  Create the value ToBeMaced by encoding the MAC_structure to a
    byte string, using the encoding described in Section 9.

3.  Call the MAC creation algorithm, passing in K (the key to use),
    alg (the algorithm to MAC with), and ToBeMaced (the value to
    compute the MAC on).

4.  Place the resulting MAC in the "tag" field of the COSE_Mac or
    COSE_Mac0 structure.

5.  For COSE_Mac structures, encrypt and encode the MAC key for each
    recipient of the message.
```

The steps to verify a MAC (§6.3):

```text
The steps to verify a MAC are:

1.  Create a MAC_structure and populate it with the appropriate
    fields.

2.  Create the value ToBeMaced by encoding the MAC_structure to a
    byte string, using the encoding described in Section 9.

3.  For COSE_Mac structures, obtain the cryptographic key by decoding
    and decrypting one of the recipient structures.

4.  Call the MAC creation algorithm, passing in K (the key to use),
    alg (the algorithm to MAC with), and ToBeMaced (the value to
    compute the MAC on).

5.  Compare the MAC value to the "tag" field of the COSE_Mac or
    COSE_Mac0 structure.
```

## §7 Key Objects

- (§7) A COSE Key structure is built on a CBOR map.
- (§7) A COSE Key Set uses a CBOR array object as its underlying type.  The values of the array elements are COSE Keys.  A COSE Key Set MUST have at least one element in the array.
- (§7) Each element in a COSE Key Set MUST be processed independently.  If one element in a COSE Key Set is either malformed or uses a key that is not understood by an application, that key is ignored, and the other keys are processed normally.
- (§7) The element "kty" is a required element in a COSE_Key map.

CDDL — COSE_Key and COSE_KeySet (§7):

```cddl
COSE_Key = {
    1 => tstr / int,          ; kty
    ? 2 => bstr,              ; kid
    ? 3 => tstr / int,        ; alg
    ? 4 => [+ (tstr / int) ], ; key_ops
    ? 5 => bstr,              ; Base IV
    * label => values
}

COSE_KeySet = [+COSE_Key]
```

### §7.1 COSE Key Common Parameters

- (§7.1, kty) This parameter is used to identify the family of keys for this structure and, thus, the set of key-type-specific parameters to be found.
- (§7.1, kty) This parameter MUST be present in a key object.
- (§7.1, kty) Implementations MUST verify that the key type is appropriate for the algorithm being processed.
- (§7.1, kty) The key type MUST be included as part of the trust-decision process.
- (§7.1, alg) This parameter is used to restrict the algorithm that is used with the key.
- (§7.1, alg) If this parameter is present in the key structure, the application MUST verify that this algorithm matches the algorithm for which the key is being used.
- (§7.1, alg) If the algorithms do not match, then this key object MUST NOT be used to perform the cryptographic operation.
- (§7.1, kid) The value of the identifier is not a unique value and can occur in other key objects, even for different keys.
- (§7.1, key_ops) This parameter is defined to restrict the set of operations that a key is to be used for.  The value of the field is an array of values from Table 5.
- (§7.1, key_ops) Algorithms define the values of key ops that are permitted to appear and are required for specific operations.
- (§7.1, Base IV) Extreme care needs to be taken when using a Base IV in an application.  Many encryption algorithms lose security if the same IV is used twice.
- (§7.1, Base IV) If the same key is used for multiple senders, then the application needs to provide for a method of dividing the IV space up between the senders.

Key Map Labels (Table 4):

```text
   +=========+=======+========+============+====================+
   | Name    | Label | CBOR   | Value      | Description        |
   |         |       | Type   | Registry   |                    |
   +=========+=======+========+============+====================+
   | kty     | 1     | tstr / | COSE Key   | Identification of  |
   |         |       | int    | Types      | the key type       |
   +---------+-------+--------+------------+--------------------+
   | kid     | 2     | bstr   |            | Key identification |
   |         |       |        |            | value -- match to  |
   |         |       |        |            | "kid" in message   |
   +---------+-------+--------+------------+--------------------+
   | alg     | 3     | tstr / | COSE       | Key usage          |
   |         |       | int    | Algorithms | restriction to     |
   |         |       |        |            | this algorithm     |
   +---------+-------+--------+------------+--------------------+
   | key_ops | 4     | [+     |            | Restrict set of    |
   |         |       | (tstr/ |            | permissible        |
   |         |       | int)]  |            | operations         |
   +---------+-------+--------+------------+--------------------+
   | Base IV | 5     | bstr   |            | Base IV to be xor- |
   |         |       |        |            | ed with Partial    |
   |         |       |        |            | IVs                |
   +---------+-------+--------+------------+--------------------+

                      Table 4: Key Map Labels
```

COSE Key common parameter definitions, in full (§7.1):

```text
kty:  This parameter is used to identify the family of keys for this
   structure and, thus, the set of key-type-specific parameters to be
   found.  The set of values defined in this document can be found in
   [COSE.KeyTypes].  This parameter MUST be present in a key object.
   Implementations MUST verify that the key type is appropriate for
   the algorithm being processed.  The key type MUST be included as
   part of the trust-decision process.

alg:  This parameter is used to restrict the algorithm that is used
   with the key.  If this parameter is present in the key structure,
   the application MUST verify that this algorithm matches the
   algorithm for which the key is being used.  If the algorithms do
   not match, then this key object MUST NOT be used to perform the
   cryptographic operation.  Note that the same key can be in a
   different key structure with a different or no algorithm
   specified; however, this is considered to be a poor security
   practice.

kid:  This parameter is used to give an identifier for a key.  The
   identifier is not structured and can be anything from a user-
   provided byte string to a value computed on the public portion of
   the key.  This field is intended for matching against a "kid"
   parameter in a message in order to filter down the set of keys
   that need to be checked.  The value of the identifier is not a
   unique value and can occur in other key objects, even for
   different keys.

key_ops:  This parameter is defined to restrict the set of operations
   that a key is to be used for.  The value of the field is an array
   of values from Table 5.  Algorithms define the values of key ops
   that are permitted to appear and are required for specific
   operations.  The set of values matches that in [RFC7517] and
   [W3C.WebCrypto].

Base IV:  This parameter is defined to carry the base portion of an
   IV.  It is designed to be used with the Partial IV header
   parameter defined in Section 3.1.  This field provides the ability
   to associate a Base IV with a key that is then modified on a per-
   message basis with the Partial IV.

   Extreme care needs to be taken when using a Base IV in an
   application.  Many encryption algorithms lose security if the same
   IV is used twice.

   If different keys are derived for each sender, starting at the
   same Base IV is likely to satisfy this condition.  If the same key
   is used for multiple senders, then the application needs to
   provide for a method of dividing the IV space up between the
   senders.  This could be done by providing a different base point
   to start from or a different Partial IV to start with and
   restricting the number of messages to be sent before rekeying.
```

Key Operation Values (Table 5):

```text
 +=========+=======+==============================================+
 | Name    | Value | Description                                  |
 +=========+=======+==============================================+
 | sign    | 1     | The key is used to create signatures.        |
 |         |       | Requires private key fields.                 |
 +---------+-------+----------------------------------------------+
 | verify  | 2     | The key is used for verification of          |
 |         |       | signatures.                                  |
 +---------+-------+----------------------------------------------+
 | encrypt | 3     | The key is used for key transport            |
 |         |       | encryption.                                  |
 +---------+-------+----------------------------------------------+
 | decrypt | 4     | The key is used for key transport            |
 |         |       | decryption.  Requires private key fields.    |
 +---------+-------+----------------------------------------------+
 | wrap    | 5     | The key is used for key wrap encryption.     |
 | key     |       |                                              |
 +---------+-------+----------------------------------------------+
 | unwrap  | 6     | The key is used for key wrap decryption.     |
 | key     |       | Requires private key fields.                 |
 +---------+-------+----------------------------------------------+
 | derive  | 7     | The key is used for deriving keys.  Requires |
 | key     |       | private key fields.                          |
 +---------+-------+----------------------------------------------+
 | derive  | 8     | The key is used for deriving bits not to be  |
 | bits    |       | used as a key.  Requires private key fields. |
 +---------+-------+----------------------------------------------+
 | MAC     | 9     | The key is used for creating MACs.           |
 | create  |       |                                              |
 +---------+-------+----------------------------------------------+
 | MAC     | 10    | The key is used for validating MACs.         |
 | verify  |       |                                              |
 +---------+-------+----------------------------------------------+

                   Table 5: Key Operation Values
```

## §8 Taxonomy of Algorithms Used by COSE

### §8.1 Signature Algorithms

- (§8.1) This means that the mixing of the signature-with-message-recovery and signature-with-appendix schemes in a single message is not supported.
- (§8.1) Signature algorithms are used with the COSE_Signature and COSE_Sign1 structures.

Signature functions — signature with appendix (§8.1):

```text
signature = Sign(message content, key)

valid = Verification(message content, key, signature)
```

Signature functions — signature with message recovery (§8.1):

```text
signature, message sent = Sign(message content, key)

valid, message content = Verification(message sent, key, signature)
```

### §8.2 Message Authentication Code (MAC) Algorithms

- (§8.2) MAC algorithms are used in the COSE_Mac and COSE_Mac0 structures.

The MAC functions (§8.2):

```text
tag = MAC_Create(message content, key)

valid = MAC_Verify(message content, key, tag)
```

### §8.3 Content Encryption Algorithms

- (§8.3) COSE restricts the set of legal content encryption algorithms to those that support authentication both of the content and additional data.
- (§8.3) The message content MUST NOT be used if the decryption does not validate.
- (§8.3) These algorithms are used in COSE_Encrypt and COSE_Encrypt0.

The encryption functions (§8.3):

```text
ciphertext = Encrypt(message content, key, additional data)

valid, message content = Decrypt(ciphertext, key, additional data)
```

### §8.4 Key Derivation Functions (KDFs)

- (§8.4) Functions like Argon2 [RFC9106] need to be used for nonrandom secrets.
- (§8.4) When using KDFs, one component that is included is context information.  Context information is used to allow for different keying information to be derived from the same secret.

### §8.5 Content Key Distribution Methods

- (§8.5) Content key distribution methods (recipient algorithms) can be defined into a number of different classes.  COSE has the ability to support many classes of recipient algorithms.

#### §8.5.1 Direct Encryption

- (§8.5.1) When direct-encryption mode is used, it MUST be the only mode used on the message.
- (§8.5.1) The "protected" field MUST be a zero-length byte string unless it is used in the computation of the content key.
- (§8.5.1) The "alg" header parameter MUST be present.
- (§8.5.1) A header parameter identifying the shared secret SHOULD be present.
- (§8.5.1) The "ciphertext" field MUST be a zero-length byte string.
- (§8.5.1) The "recipients" field MUST be absent.

COSE_Recipient structure for Direct Encryption (§8.5.1):

```text
*  The "protected" field MUST be a zero-length byte string unless it
   is used in the computation of the content key.

*  The "alg" header parameter MUST be present.

*  A header parameter identifying the shared secret SHOULD be
   present.

*  The "ciphertext" field MUST be a zero-length byte string.

*  The "recipients" field MUST be absent.
```

#### §8.5.2 Key Wrap

- (§8.5.2) The "protected" field MUST be a zero-length byte string if the key wrap algorithm is an AE algorithm.
- (§8.5.2) The "recipients" field is normally absent but can be used.  Applications MUST deal with a recipient field being present that has an unsupported algorithm.  Failing to decrypt that specific recipient is an acceptable way of dealing with it.  Failing to process the message is not an acceptable way of dealing with it.
- (§8.5.2) The plaintext to be encrypted is the key from the next layer down (usually the content layer).
- (§8.5.2) At a minimum, the "unprotected" field MUST contain the "alg" header parameter and SHOULD contain a header parameter identifying the shared secret.

COSE_Recipient structure for Key Wrap (§8.5.2):

```text
*  The "protected" field MUST be a zero-length byte string if the key
   wrap algorithm is an AE algorithm.

*  The "recipients" field is normally absent but can be used.
   Applications MUST deal with a recipient field being present that
   has an unsupported algorithm.  Failing to decrypt that specific
   recipient is an acceptable way of dealing with it.  Failing to
   process the message is not an acceptable way of dealing with it.

*  The plaintext to be encrypted is the key from the next layer down
   (usually the content layer).

*  At a minimum, the "unprotected" field MUST contain the "alg"
   header parameter and SHOULD contain a header parameter identifying
   the shared secret.
```

#### §8.5.3 Key Transport

- (§8.5.3) The "protected" field MUST be a zero-length byte string.
- (§8.5.3) The plaintext to be encrypted is the key from the next layer down (usually the content layer).
- (§8.5.3) At a minimum, the "unprotected" field MUST contain the "alg" header parameter and SHOULD contain a parameter identifying the asymmetric key.

COSE_Recipient structure for Key Transport (§8.5.3):

```text
*  The "protected" field MUST be a zero-length byte string.

*  The plaintext to be encrypted is the key from the next layer down
   (usually the content layer).

*  At a minimum, the "unprotected" field MUST contain the "alg"
   header parameter and SHOULD contain a parameter identifying the
   asymmetric key.
```

#### §8.5.4 Direct Key Agreement

- (§8.5.4) When Static-Static key agreement is used, then some piece of unique data for the KDF is required to ensure that a different key is created for each message.
- (§8.5.4) When direct key agreement mode is used, there MUST be only one recipient in the message.
- (§8.5.4) At a minimum, headers MUST contain the "alg" header parameter and SHOULD contain a header parameter identifying the recipient's asymmetric key.
- (§8.5.4) The headers SHOULD identify the sender's key for the Static-Static versions and MUST contain the sender's ephemeral key for the ephemeral-static versions.

COSE_Recipient structure for Direct Key Agreement (§8.5.4):

```text
*  At a minimum, headers MUST contain the "alg" header parameter and
   SHOULD contain a header parameter identifying the recipient's
   asymmetric key.

*  The headers SHOULD identify the sender's key for the Static-Static
   versions and MUST contain the sender's ephemeral key for the
   ephemeral-static versions.
```

#### §8.5.5 Key Agreement with Key Wrap

- (§8.5.5) The "protected" field is fed into the KDF context structure.
- (§8.5.5) The plaintext to be encrypted is the key from the next layer down (usually the content layer).
- (§8.5.5) The "alg" header parameter MUST be present in the layer.
- (§8.5.5) A header parameter identifying the recipient's key SHOULD be present.  A header parameter identifying the sender's key SHOULD be present.

Key Agreement with Key Wrap function (§8.5.5):

```text
encryptedKey = KeyWrap(KDF(DH-Shared, context), CEK)
```

COSE_Recipient structure for Key Agreement with Key Wrap (§8.5.5):

```text
*  The "protected" field is fed into the KDF context structure.

*  The plaintext to be encrypted is the key from the next layer down
   (usually the content layer).

*  The "alg" header parameter MUST be present in the layer.

*  A header parameter identifying the recipient's key SHOULD be
   present.  A header parameter identifying the sender's key SHOULD
   be present.
```

## §9 CBOR Encoding Restrictions

- (§9) This document limits the restrictions it imposes on how the CBOR Encoder needs to work.  The new encoding restrictions are aligned with the Core Deterministic Encoding Requirements specified in Section 4.2.1 of RFC 8949 [STD94].  It has been narrowed down to the following restrictions:
- (§9) The restriction applies to the encoding of the Sig_structure, the Enc_structure, and the MAC_structure.
- (§9) Encoding MUST be done using definite lengths, and the length of the (encoded) argument MUST be the minimum possible length.  This means that the integer 1 is encoded as "0x01" and not "0x1801".
- (§9) Applications MUST NOT generate messages with the same label used twice as a key in a single map.  Applications MUST NOT parse and process messages with the same label used twice as a key in a single map.
- (§9) Applications can enforce the parse-and-process requirement by using parsers that will fail the parse step or by using parsers that will pass all keys to the application, and the application can perform the check for duplicate keys.

The CBOR encoding restrictions, in full (§9):

```text
*  The restriction applies to the encoding of the Sig_structure, the
   Enc_structure, and the MAC_structure.

*  Encoding MUST be done using definite lengths, and the length of
   the (encoded) argument MUST be the minimum possible length.  This
   means that the integer 1 is encoded as "0x01" and not "0x1801".

*  Applications MUST NOT generate messages with the same label used
   twice as a key in a single map.  Applications MUST NOT parse and
   process messages with the same label used twice as a key in a
   single map.  Applications can enforce the parse-and-process
   requirement by using parsers that will fail the parse step or by
   using parsers that will pass all keys to the application, and the
   application can perform the check for duplicate keys.
```

## §10 Application Profiling Considerations

- (§10) This document is designed to provide a set of security services but not impose algorithm implementation requirements for specific usage.
- (§10) The requirements about which algorithms and which services are needed are deferred to each application.
- (§10) It is intended that a profile of this document be created that defines the interoperability requirements for that specific application.
- (§10) Applications need to determine the set of messages defined in this document that they will be using.
- (§10) When applications use externally defined authenticated data, they need to define how that data is encoded.  This document assumes that the data will be provided as a byte string.
- (§10) Applications need to determine the set of security algorithms that is to be used.
- (§10) If the Partial IV header parameter is specified, then the application also needs to define how the fixed portion of the IV is determined.

Guidelines and topics to be considered when profiling this document (§10):

```text
*  Applications need to determine the set of messages defined in this
   document that they will be using.  The set of messages corresponds
   fairly directly to the needed set of security services and
   security levels.

*  Applications may define new header parameters for a specific
   purpose.  Applications will oftentimes select specific header
   parameters to use or not to use.  For example, an application
   would normally state a preference for using either the IV or the
   Partial IV header parameter.  If the Partial IV header parameter
   is specified, then the application also needs to define how the
   fixed portion of the IV is determined.

*  When applications use externally defined authenticated data, they
   need to define how that data is encoded.  This document assumes
   that the data will be provided as a byte string.  More information
   can be found in Section 4.3.

*  Applications need to determine the set of security algorithms that
   is to be used.  When selecting the algorithms to be used as the
   mandatory-to-implement set, consideration should be given to
   choosing different types of algorithms when two are chosen for a
   specific purpose.  An example of this would be choosing HMAC-
   SHA512 and AES-CMAC (Cipher-Based Message Authentication Code) as
   different MAC algorithms; the construction is vastly different
   between these two algorithms.  This means that a weakening of one
   algorithm would be unlikely to lead to a weakening of the other
   algorithms.  Of course, these algorithms do not provide the same
   level of security and thus may not be comparable for the desired
   security functionality.  Additional guidance can be found in
   [BCP201].

*  Applications may need to provide some type of negotiation or
   discovery method if multiple algorithms or message structures are
   permitted.  The method can range from something as simple as
   requiring preconfiguration of the set of algorithms to providing a
   discovery method built into the protocol.  S/MIME provided a
   number of different ways to approach the problem that applications
   could follow:

   -  Advertising in the message (S/MIME capabilities) [RFC8551].

   -  Advertising in the certificate (capabilities extension)
      [RFC4262].

   -  Minimum requirements for the S/MIME, which have been updated
      over time [RFC2633] [RFC3851] [RFC5751] [RFC8551].  (Note that
      [RFC2633] was obsoleted by [RFC3851], which was obsoleted by
      [RFC5751], which was obsoleted by [RFC8551].)
```

## §11 IANA Considerations

- (§11) Note that while [RFC9053] also updates the registries and registrations originally established by [RFC8152], the requested updates are mutually exclusive.

### §11.1 COSE Header Parameters Registry

- (§11.1) IANA has updated the reference for this registry to point to this document instead of [RFC8152].
- (§11.1) IANA has also updated all entries that referenced [RFC8152], except "counter signature" and "CounterSignature0", to refer to this document.  The references for "counter signature" and "CounterSignature0" continue to reference [RFC8152].

### §11.2 COSE Key Common Parameters Registry

- (§11.2) The "COSE Key Common Parameters" registry [COSE.KeyParameters] was defined in [RFC8152].  IANA has updated the reference for this registry to point to this document instead of [RFC8152].  IANA has also updated the entries that referenced [RFC8152] to refer to this document.

### §11.3 Media Type Registrations

#### §11.3.1 COSE Security Message

- (§11.3.1) IANA has registered the "application/cose" media type in the "Media Types" registry.  This media type is used to indicate that the content is a COSE message.
- (§11.3.1) Required parameters:  N/A
- (§11.3.1) Optional parameters:  cose-type
- (§11.3.1) Encoding considerations:  binary
- (§11.3.1) File extension(s): cbor

Media-type registration template for "application/cose", in full (§11.3.1):

```text
Type name:  application

Subtype name:  cose

Required parameters:  N/A

Optional parameters:  cose-type

Encoding considerations:  binary

Security considerations:  See the Security Considerations section of
   RFC 9052.

Interoperability considerations:  N/A

Published specification:  RFC 9052

Applications that use this media type:  IoT applications sending
   security content over HTTP(S) transports.

Fragment identifier considerations:  N/A

Additional information:
   *  Deprecated alias names for this type: N/A

   *  Magic number(s): N/A

   *  File extension(s): cbor

   *  Macintosh file type code(s): N/A

Person & email address to contact for further information:
   iesg@ietf.org

Intended usage:  COMMON

Restrictions on usage:  N/A

Author:  Jim Schaad

Change Controller:  IESG

Provisional registration?  No
```

#### §11.3.2 COSE Key Media Type

- (§11.3.2) IANA has registered the "application/cose-key" and "application/cose-key-set" media types in the "Media Types" registry.  These media types are used to indicate, respectively, that the content is a COSE_Key or COSE_KeySet object.
- (§11.3.2) Subtype name:  cose-key
- (§11.3.2) Subtype name:  cose-key-set

The template for "application/cose-key" is as follows (§11.3.2):

```text
Type name:  application

Subtype name:  cose-key

Required parameters:  N/A

Optional parameters:  N/A

Encoding considerations:  binary

Security considerations:  See the Security Considerations section of
   RFC 9052.

Interoperability considerations:  N/A

Published specification:  RFC 9052

Applications that use this media type:  Distribution of COSE-based
   keys for IoT applications.

Fragment identifier considerations:  N/A

Additional information:
   *  Deprecated alias names for this type: N/A

   *  Magic number(s): N/A

   *  File extension(s): cbor

   *  Macintosh file type code(s): N/A

Person & email address to contact for further information:
   iesg@ietf.org

Intended usage:  COMMON

Restrictions on usage:  N/A

Author:  Jim Schaad

Change Controller:  IESG

Provisional registration?  No
```

The template for registering "application/cose-key-set" is (§11.3.2):

```text
Type name:  application

Subtype name:  cose-key-set

Required parameters:  N/A

Optional parameters:  N/A

Encoding considerations:  binary

Security considerations:  See the Security Considerations section of
   RFC 9052.

Interoperability considerations:  N/A

Published specification:  RFC 9052

Applications that use this media type:  Distribution of COSE-based
   keys for IoT applications.

Fragment identifier considerations:  N/A

Additional information:
   *  Deprecated alias names for this type: N/A

   *  Magic number(s): N/A

   *  File extension(s): cbor

   *  Macintosh file type code(s): N/A

Person & email address to contact for further information:  iesg@ietf
   .org

Intended usage:  COMMON

Restrictions on usage:  N/A

Author:  Jim Schaad

Change Controller:  IESG

Provisional registration?  No
```

### §11.4 CoAP Content-Formats Registry

- (§11.4) IANA added entries to the "CoAP Content-Formats" registry as indicated in [RFC8152].  IANA has updated the reference to point to this document instead of [RFC8152].

### §11.5 CBOR Tags Registry

- (§11.5) IANA added entries to the "CBOR Tags" registry as indicated in [RFC8152].  IANA has updated the references to point to this document instead of [RFC8152].

### §11.6 Expert Review Instructions

- (§11.6) All of the IANA registries established by [RFC8152] are, at least in part, defined as Expert Review [RFC8126].
- (§11.6) Expert reviewers should take the following into consideration:
- (§11.6) Point squatting should be discouraged.
- (§11.6) The ranges tagged as private use are intended for testing purposes and closed environments; code points in other ranges should not be assigned for testing.
- (§11.6) Standards Track or BCP RFCs are required to register a code point in the Standards Action range.
- (§11.6) Specifications should exist for Specification Required ranges, but early assignment before an RFC is available is considered to be permissible.
- (§11.6) Specifications are needed for the first-come, first-served range if the points are expected to be used outside of closed environments in an interoperable way.
- (§11.6) When specifications are not provided, the description provided needs to have sufficient information to identify what the point is being used for.
- (§11.6) Experts should take into account the expected usage of fields when approving code point assignment.
- (§11.6) When algorithms are registered, vanity registrations should be discouraged.
- (§11.6) Algorithms are expected to meet the security requirements of the community and the requirements of the message structures in order to be suitable for registration.

Expert review considerations, in full (§11.6):

```text
*  Point squatting should be discouraged.  Reviewers are encouraged
   to get sufficient information for registration requests to ensure
   that the usage is not going to duplicate an existing registration
   and that the code point is likely to be used in deployments.  The
   ranges tagged as private use are intended for testing purposes and
   closed environments; code points in other ranges should not be
   assigned for testing.

*  Standards Track or BCP RFCs are required to register a code point
   in the Standards Action range.  Specifications should exist for
   Specification Required ranges, but early assignment before an RFC
   is available is considered to be permissible.  Specifications are
   needed for the first-come, first-served range if the points are
   expected to be used outside of closed environments in an
   interoperable way.  When specifications are not provided, the
   description provided needs to have sufficient information to
   identify what the point is being used for.

*  Experts should take into account the expected usage of fields when
   approving code point assignment.  The fact that the Standards
   Action range is only available to Standards Track documents does
   not mean that a Standards Track document cannot have points
   assigned outside of that range.  The length of the encoded value
   should be weighed against how many code points of that length are
   left and the size of device it will be used on.

*  When algorithms are registered, vanity registrations should be
   discouraged.  One way to do this is to require registrations to
   provide additional documentation on security analysis of the
   algorithm.  Another thing that should be considered is requesting
   an opinion on the algorithm from the Crypto Forum Research Group
   (CFRG).  Algorithms are expected to meet the security requirements
   of the community and the requirements of the message structures in
   order to be suitable for registration.
```

## §12 Security Considerations

- (§12) Implementations need to protect the private key material for all individuals.
- (§12) Use of the same key for two different algorithms can leak information about the key.  It is therefore recommended that keys be restricted to a single algorithm.
- (§12) Use of "direct" as a recipient algorithm combined with a second recipient algorithm exposes the direct key to the second recipient; Section 8.5 forbids combining "direct" recipient algorithms with other modes.
- (§12) Several of the algorithms in [RFC9053] have limits on the number of times that a key can be used without leaking information about the key.
- (§12) If the key wrap step is added, then no proof of origin is implied and this is not an issue.
- (§12) Key creators and key consumers are strongly encouraged to not only create new keys for each different algorithm, but to include that selection of algorithm in any distribution of key material and strictly enforce the matching of algorithms in the key structure to algorithms in the message structure.
- (§12) In addition to checking that algorithms are correct, the key form needs to be checked as well.  Do not use an "EC2" key where an "OKP" key is expected.
- (§12) Before using a key for transmission, or before acting on information received, a trust decision on a key needs to be made.
- (§12) This specification does not provide a uniform method for providing padding as part of the message structure.
- (§12) This means that it is up to the applications to document how content padding is to be done in order to prevent or discourage such analysis.

Private-key-material cases highlighted by this document (§12):

```text
*  Use of the same key for two different algorithms can leak
   information about the key.  It is therefore recommended that keys
   be restricted to a single algorithm.

*  Use of "direct" as a recipient algorithm combined with a second
   recipient algorithm exposes the direct key to the second
   recipient; Section 8.5 forbids combining "direct" recipient
   algorithms with other modes.

*  Several of the algorithms in [RFC9053] have limits on the number
   of times that a key can be used without leaking information about
   the key.
```

ECDH and direct plus KDF: shared-CEK proof-of-origin hazard (§12):

```text
The use of Elliptic Curve Diffie-Hellman (ECDH) and direct plus KDF
(with no key wrap) will not directly lead to the private key being
leaked; the one-way function of the KDF will prevent that.  There is,
however, a different issue that needs to be addressed.  Having two
recipients requires that the CEK be shared between two recipients.
The second recipient therefore has a CEK that was derived from
material that can be used for the weak proof of origin.  The second
recipient could create a message using the same CEK and send it to
the first recipient; the first recipient would, for either Static-
Static ECDH or direct plus KDF, make an assumption that the CEK could
be used for proof of origin, even though it is from the wrong entity.
If the key wrap step is added, then no proof of origin is implied and
this is not an issue.
```

Single key used for multiple algorithms (§12):

```text
Although it has been mentioned before, it bears repeating that the
use of a single key for multiple algorithms has been demonstrated in
some cases to leak information about a key, providing the opportunity
for attackers to forge integrity tags or gain information about
encrypted content.  Binding a key to a single algorithm prevents
these problems.  Key creators and key consumers are strongly
encouraged to not only create new keys for each different algorithm,
but to include that selection of algorithm in any distribution of key
material and strictly enforce the matching of algorithms in the key
structure to algorithms in the message structure.  In addition to
checking that algorithms are correct, the key form needs to be
checked as well.  Do not use an "EC2" key where an "OKP" key is
expected.
```

Factors associated with the trust decision on a key (§12):

```text
*  What are the permissions associated with the key owner?

*  Is the cryptographic algorithm acceptable in the current context?

*  Have the restrictions associated with the key, such as algorithm
   or freshness, been checked, and are they correct?

*  Is the request something that is reasonable, given the current
   state of the application?

*  Have any security considerations that are part of the message been
   enforced (as specified by the application or "crit" header
   parameter)?
```

Traffic analysis based on message length (§12):

```text
One area that has been getting exposure is traffic analysis of
encrypted messages based on the length of the message.  This
specification does not provide a uniform method for providing padding
as part of the message structure.  An observer can distinguish
between two different messages (for example, "YES" and "NO") based on
the length for all of the content encryption algorithms that are
defined in [RFC9053].  This means that it is up to the applications
to document how content padding is to be done in order to prevent or
discourage such analysis.  (For example, the text strings could be
defined as "YES" and "NO ".)
```

## Appendix A. Guidelines for External Data Authentication of Algorithms

- (Appendix A) The key words from BCP 14 ([RFC2119] and [RFC8174]) are deliberately not used here.  This specification can provide recommendations, but it cannot enforce them.
- (Appendix A) During development of COSE, the requirement that the algorithm identifier be located in the protected attributes was relaxed from a must to a should.
- (Appendix A) Three sets of recommendations are laid out.
- (Appendix A, set 1) Applications need to list the set of COSE structures that implicit algorithms are to be used in.  Applications need to require that the receipt of an explicit algorithm identifier in one of these structures will lead to the message being rejected.
- (Appendix A, set 1) Applications need to define the set of information that is to be considered to be part of a context when omitting algorithm identifiers.  At a minimum, this would be the key identifier (if needed), the key, the algorithm, and the COSE structure it is used with.
- (Appendix A, set 1) Applications should restrict the use of a single key to a single algorithm.
- (Appendix A, set 1) Applications cannot rely on key identifiers being unique unless they take significant efforts to ensure that they are computed in such a way as to create this guarantee.
- (Appendix A, set 1) Applications should continue the practice of protecting the algorithm identifier.
- (Appendix A, set 2) Applications that want to support this will need to define a structure that allows for, and clearly identifies, both the COSE structure to be used with a given key and the structure and algorithm to be used for the secondary layer.
- (Appendix A, set 3) Applications need to ensure that the multiple contexts stay associated.  If one of the contexts is invalidated for any reason, all of the contexts associated with it should also be invalidated.

Implicit algorithm for a single layer of a COSE object — items to take into account (Appendix A, set 1):

```text
*  Applications need to list the set of COSE structures that implicit
   algorithms are to be used in.  Applications need to require that
   the receipt of an explicit algorithm identifier in one of these
   structures will lead to the message being rejected.  This
   requirement is stated so that there will never be a case where
   there is any ambiguity about the question of which algorithm
   should be used, the implicit or the explicit one.  This applies
   even if the transported algorithm identifier is a protected
   attribute.  This applies even if the transported algorithm is the
   same as the implicit algorithm.

*  Applications need to define the set of information that is to be
   considered to be part of a context when omitting algorithm
   identifiers.  At a minimum, this would be the key identifier (if
   needed), the key, the algorithm, and the COSE structure it is used
   with.  Applications should restrict the use of a single key to a
   single algorithm.  As noted for some of the algorithms in
   [RFC9053], the use of the same key in different, related
   algorithms can lead to leakage of information about the key,
   leakage about the data, or the ability to perform forgeries.

*  In many cases, applications that make the algorithm identifier
   implicit will also want to make the context identifier implicit
   for the same reason.  That is, omitting the context identifier
   will decrease the message size (potentially significantly,
   depending on the length of the identifier).  Applications that do
   this will need to describe the circumstances where the context
   identifier is to be omitted and how the context identifier is to
   be inferred in these cases.  (An exhaustive search over all of the
   keys would normally not be considered to be acceptable.)  An
   example of how this can be done is to tie the context to a
   transaction identifier.  Both would be sent on the original
   message, but only the transaction identifier would need to be sent
   after that point, as the context is tied into the transaction
   identifier.  Another way would be to associate a context with a
   network address.  All messages coming from a single network
   address can be assumed to be associated with a specific context.
   (In this case, the address would normally be distributed as part
   of the context.)

*  Applications cannot rely on key identifiers being unique unless
   they take significant efforts to ensure that they are computed in
   such a way as to create this guarantee.  Even when an application
   does this, the uniqueness might be violated if the application is
   run in different contexts (i.e., with a different context
   provider) or if the system combines the security contexts from
   different applications together into a single store.

*  Applications should continue the practice of protecting the
   algorithm identifier.  Since this is not done by placing it in the
   protected attributes field, applications should define an
   application-specific external data structure that includes this
   value.  This external data field can be used as such for content
   encryption, MAC, and signature algorithms.  It can be used in the
   SuppPrivInfo field for those algorithms that use a KDF to derive a
   key value.  Applications may also want to protect other
   information that is part of the context structure as well.  It
   should be noted that those fields, such as the key or a Base IV,
   that are protected by virtue of being used in the cryptographic
   computation do not need to be included in the external data field.
```

Multiple implicit algorithms for a multiple-layer COSE object — additional items (Appendix A, set 2):

```text
*  Applications that want to support this will need to define a
   structure that allows for, and clearly identifies, both the COSE
   structure to be used with a given key and the structure and
   algorithm to be used for the secondary layer.  The key for the
   secondary layer is computed as normal from the recipient layer.
```

Implicit algorithms across unrelated layers or COSE objects — additional items (Appendix A, set 3):

```text
*  Applications need to ensure that the multiple contexts stay
   associated.  If one of the contexts is invalidated for any reason,
   all of the contexts associated with it should also be invalidated.
```

## Appendix B. Two Layers of Recipient Information

- (Appendix B) All of the currently defined recipient algorithm classes only use two layers of the COSE structure.  The first layer (COSE_Encrypt) is the message content, and the second layer (COSE_Recipient) is the content key encryption.
- (Appendix B) However, if one uses a recipient algorithm such as the RSA Key Encapsulation Mechanism (RSA-KEM) (see Appendix A of RSA-KEM [RFC5990]), then it makes sense to have two layers of the COSE_Recipient structure.
