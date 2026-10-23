---
record: rfc-9053
kind: normative
title: "rfc-9053 — normative statements"
extracted: "2026-10-19"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 9053, "CBOR Object Signing and Encryption (COSE): Initial Algorithms", August 2022. Quotations are verbatim from the plain-text RFC. Blocks that reproduce tables, lists, structures, or pseudocode preserve the source's own line breaks and indentation inside fenced blocks.


## §1. Introduction

- (§1) "The core COSE specification consists of two documents.  [RFC9052] contains the serialization structures and the procedures for using the different cryptographic algorithms.  This document provides an initial set of algorithms for use with those structures."

### §1.1. Requirements Terminology

- (§1.1) "The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here."

### §1.3. Document Terminology

- (§1.3) "The term "byte string" is used for sequences of bytes, while the term "text string" is used for sequences of characters."
- (§1.3) "The tables for algorithms contain the following columns:"
- (§1.3) "Additional columns may be present in a table depending on the algorithms."

```text
   *  A name for the algorithm for use in documents.

   *  The value used on the wire for the algorithm.  One place this is
      used is the algorithm header parameter of a message.

   *  A short description so that the algorithm can be easily identified
      when scanning the IANA registry.
```

### §1.4. CDDL Grammar for CBOR Data Structures

- (§1.4) "For that reason, the CBOR data objects defined here are described in prose.  Additional (non-normative) descriptions of the COSE data objects are provided in a subset of CDDL, described in [RFC9052]."

## §2. Signature Algorithms

- (§2) "Section 8.1 of [RFC9052] contains a generic description of signature algorithms.  This document defines signature algorithm identifiers for two signature algorithms."

### §2.1. ECDSA

- (§2.1) "The ECDSA signature algorithm is parameterized with a hash function (h)."
- (§2.1) "The signature algorithm results in a pair of integers (R, S).  These integers will be the same length as the length of the key used for the signature process."
- (§2.1) "Implementations SHOULD use a deterministic version of ECDSA such as the one defined in [RFC6979]."
- (§2.1) "The use of deterministic ECDSA does not lessen the need to have good random number generation when creating the private key."
- (§2.1) "In the event that the length of the hash function output is greater than the group of the key, the leftmost bytes of the hash output are used."
- (§2.1) "This document defines ECDSA as working only with the curves P-256, P-384, and P-521."
- (§2.1) "This document requires that the curves be encoded using the "EC2" (two coordinate elliptic curve) key type."
- (§2.1) "Implementations need to check that the key type and curve are correct when creating and verifying a signature."
- (§2.1) "In order to promote interoperability, it is suggested that SHA-256 be used only with curve P-256, SHA-384 be used only with curve P-384, and SHA-512 be used only with curve P-521."
- (§2.1) "The signature is encoded by converting the integers into byte strings of the same length as the key size."
- (§2.1) "The length is rounded up to the nearest byte and is left padded with zero bits to get to the correct length."
- (§2.1) "The two integers are then concatenated together to form a byte string that is the resulting signature."
- (§2.1) "The "kty" field MUST be present"
- (§2.1) "it MUST be "EC2""
- (§2.1) "If the "alg" field is present, it MUST match the ECDSA signature algorithm being used."
- (§2.1) "If the "key_ops" field is present, it MUST include "sign" when creating an ECDSA signature."
- (§2.1) "If the "key_ops" field is present, it MUST include "verify" when verifying an ECDSA signature."

```text
              +=======+=======+=========+==================+
              | Name  | Value | Hash    | Description      |
              +=======+=======+=========+==================+
              | ES256 |   -7  | SHA-256 | ECDSA w/ SHA-256 |
              +-------+-------+---------+------------------+
              | ES384 |  -35  | SHA-384 | ECDSA w/ SHA-384 |
              +-------+-------+---------+------------------+
              | ES512 |  -36  | SHA-512 | ECDSA w/ SHA-512 |
              +-------+-------+---------+------------------+

                     Table 1: ECDSA Algorithm Values
```

```text
   Signature = I2OSP(R, n) | I2OSP(S, n)

   where n = ceiling(key_length / 8)
```

#### §2.1.1. Security Considerations for ECDSA

- (§2.1.1) "The security strength of the signature is no greater than the minimum of the security strength associated with the bit length of the key and the security strength of the hash function."
- (§2.1.1) "We currently do not have any way to deal with this version of the attack except to restrict the overall set of curves that can be used."
- (§2.1.1) "As the hash algorithm is part of the signature algorithm identifier, this attack is mitigated by including a signature algorithm identifier in the protected-header bucket."

### §2.2. Edwards-Curve Digital Signature Algorithm (EdDSA)

- (§2.2) "The document additionally describes two variants of the EdDSA algorithm: Pure EdDSA, where no hash function is applied to the content before signing, and HashEdDSA, where a hash function is applied to the content before signing and the result of that hash function is signed."
- (§2.2) "For EdDSA, the content to be signed (either the message or the prehash value) is processed twice inside of the signature algorithm."
- (§2.2) "A single signature algorithm is defined, which can be used for multiple curves."
- (§2.2) "[RFC8032] describes the method of encoding the signature value."
- (§2.2) "For use with COSE, only the pure EdDSA version is used."
- (§2.2) "This is because it is not expected that extremely large contents are going to be needed and, based on the arrangement of the message structure, the entire message is going to need to be held in memory in order to create or verify a signature."
- (§2.2) "Therefore, there does not appear to be a need to be able to do block updates of the hash, followed by eliminating the message from memory."
- (§2.2) "Applications can provide the same features by defining the content of the message as a hash value and transporting the COSE object (with the hash value) and the content as separate items."
- (§2.2) "The "kty" field MUST be present"
- (§2.2) "it MUST be "OKP" (Octet Key Pair)"
- (§2.2) "The "crv" field MUST be present"
- (§2.2) "it MUST be a curve defined for this signature algorithm"
- (§2.2) "If the "alg" field is present, it MUST match "EdDSA"."
- (§2.2) "If the "key_ops" field is present, it MUST include "sign" when creating an EdDSA signature."
- (§2.2) "If the "key_ops" field is present, it MUST include "verify" when verifying an EdDSA signature."

```text
                      +=======+=======+=============+
                      | Name  | Value | Description |
                      +=======+=======+=============+
                      | EdDSA |   -8  | EdDSA       |
                      +-------+-------+-------------+

                       Table 2: EdDSA Algorithm Value
```

#### §2.2.1. Security Considerations for EdDSA

- (§2.2.1) "Public values are computed differently in EdDSA and Elliptic Curve Diffie-Hellman (ECDH); for this reason, the public key from one should not be used with the other algorithm."
- (§2.2.1) "If batch signature verification is performed, a well-seeded cryptographic random number generator is REQUIRED (Section 8.2 of [RFC8032])."
- (§2.2.1) "Signing and nonbatch signature verification are deterministic operations and do not need random numbers of any kind."

## §3. Message Authentication Code (MAC) Algorithms

- (§3) "Section 8.2 of [RFC9052] contains a generic description of MAC algorithms.  This section defines the conventions for two MAC algorithms."

### §3.1. Hash-Based Message Authentication Codes (HMACs)

- (§3.1) "The HMAC algorithm is parameterized by an inner and outer padding, a hash function (h), and an authentication tag value length."
- (§3.1) "For use in constrained environments, we define one HMAC algorithm that is truncated."
- (§3.1) "There are currently no known issues with truncation; however, the security strength of the message tag is correspondingly reduced in strength."
- (§3.1) "For this specification, the inner and outer padding are fixed to the values set in [RFC2104]."
- (§3.1) "When truncating, the leftmost tag-length bits are kept and transmitted."
- (§3.1) "For those algorithms that transport the key (such as AES Key Wrap), the size of the HMAC key SHOULD be the same size as the output of the underlying hash function."
- (§3.1) "For those algorithms that derive the key (such as ECDH), the derived key MUST be the same size as the output of the underlying hash function."
- (§3.1) "The "kty" field MUST be present"
- (§3.1) "it MUST be "Symmetric""
- (§3.1) "If the "alg" field is present, it MUST match the HMAC algorithm being used."
- (§3.1) "If the "key_ops" field is present, it MUST include "MAC create" when creating an HMAC authentication tag."
- (§3.1) "If the "key_ops" field is present, it MUST include "MAC verify" when verifying an HMAC authentication tag."
- (§3.1) "Implementations creating and validating MAC values MUST validate that the key type, key length, and algorithm are correct and appropriate for the entities involved."

```text
   +=============+=======+=========+============+======================+
   | Name        | Value | Hash    | Tag Length | Description          |
   +=============+=======+=========+============+======================+
   | HMAC        |   4   | SHA-256 |     64     | HMAC w/ SHA-256      |
   | 256/64      |       |         |            | truncated to 64 bits |
   +-------------+-------+---------+------------+----------------------+
   | HMAC        |   5   | SHA-256 |    256     | HMAC w/ SHA-256      |
   | 256/256     |       |         |            |                      |
   +-------------+-------+---------+------------+----------------------+
   | HMAC        |   6   | SHA-384 |    384     | HMAC w/ SHA-384      |
   | 384/384     |       |         |            |                      |
   +-------------+-------+---------+------------+----------------------+
   | HMAC        |   7   | SHA-512 |    512     | HMAC w/ SHA-512      |
   | 512/512     |       |         |            |                      |
   +-------------+-------+---------+------------+----------------------+

                       Table 3: HMAC Algorithm Values
```

#### §3.1.1. Security Considerations for HMAC

- (§3.1.1) "This means that key size is going to be directly related to the security of an HMAC operation."

### §3.2. AES Message Authentication Code (AES-CBC-MAC)

- (§3.2) "AES-CBC-MAC is the instantiation of the CBC-MAC construction (defined in [MAC]) using AES as the block cipher."
- (§3.2) "(Note that this is not the same algorithm as AES Cipher-Based Message Authentication Code (AES-CMAC) [RFC4493].)"
- (§3.2) "AES-CBC-MAC is parameterized by the key length, the authentication tag length, and the Initialization Vector (IV) used."
- (§3.2) "Keys may be obtained from either a key structure or a recipient structure."
- (§3.2) "For all of these algorithms, the IV is fixed to all zeros."
- (§3.2) "Implementations creating and validating MAC values MUST validate that the key type, key length, and algorithm are correct and appropriate for the entities involved."
- (§3.2) "The "kty" field MUST be present"
- (§3.2) "it MUST be "Symmetric""
- (§3.2) "If the "alg" field is present, it MUST match the AES-MAC algorithm being used."
- (§3.2) "If the "key_ops" field is present, it MUST include "MAC create" when creating an AES-MAC authentication tag."
- (§3.2) "If the "key_ops" field is present, it MUST include "MAC verify" when verifying an AES-MAC authentication tag."

```text
     +=========+=======+============+============+==================+
     | Name    | Value | Key Length | Tag Length | Description      |
     +=========+=======+============+============+==================+
     | AES-MAC |   14  |    128     |     64     | AES-MAC 128-bit  |
     | 128/64  |       |            |            | key, 64-bit tag  |
     +---------+-------+------------+------------+------------------+
     | AES-MAC |   15  |    256     |     64     | AES-MAC 256-bit  |
     | 256/64  |       |            |            | key, 64-bit tag  |
     +---------+-------+------------+------------+------------------+
     | AES-MAC |   25  |    128     |    128     | AES-MAC 128-bit  |
     | 128/128 |       |            |            | key, 128-bit tag |
     +---------+-------+------------+------------+------------------+
     | AES-MAC |   26  |    256     |    128     | AES-MAC 256-bit  |
     | 256/128 |       |            |            | key, 128-bit tag |
     +---------+-------+------------+------------+------------------+

                    Table 4: AES-MAC Algorithm Values
```

#### §3.2.1. Security Considerations for AES-CBC-MAC

- (§3.2.1) "A single key must only be used for messages of a fixed or known length."
- (§3.2.1) "This can be addressed by using different keys for messages of different lengths."
- (§3.2.1) "In Cipher Block Chaining (CBC) mode, if the same key is used for both encryption and authentication operations, an attacker can produce messages with a valid authentication code."
- (§3.2.1) "If the IV can be modified, then messages can be forged.  This is addressed by fixing the IV to all zeros."

## §4. Content Encryption Algorithms

- (§4) "Section 8.3 of [RFC9052] contains a generic description of content encryption algorithms.  This document defines the identifier and usages for three content encryption algorithms."

### §4.1. AES-GCM

- (§4.1) "The GCM mode is parameterized by the size of the authentication tag and the size of the nonce."
- (§4.1) "The size of the authentication tag is limited to a small set of values."
- (§4.1) "Keys may be obtained from either a key structure or a recipient structure."
- (§4.1) "This document fixes the size of the nonce at 96 bits."
- (§4.1) "For this document, however, the size of the authentication tag is fixed at 128 bits."
- (§4.1) "Implementations that are encrypting or decrypting MUST validate that the key type, key length, and algorithm are correct and appropriate for the entities involved."
- (§4.1) "The "kty" field MUST be present"
- (§4.1) "it MUST be "Symmetric""
- (§4.1) "If the "alg" field is present, it MUST match the AES-GCM algorithm being used."
- (§4.1) "If the "key_ops" field is present, it MUST include "encrypt" or "wrap key" when encrypting."
- (§4.1) "If the "key_ops" field is present, it MUST include "decrypt" or "unwrap key" when decrypting."

```text
      +=========+=======+==========================================+
      | Name    | Value | Description                              |
      +=========+=======+==========================================+
      | A128GCM |   1   | AES-GCM mode w/ 128-bit key, 128-bit tag |
      +---------+-------+------------------------------------------+
      | A192GCM |   2   | AES-GCM mode w/ 192-bit key, 128-bit tag |
      +---------+-------+------------------------------------------+
      | A256GCM |   3   | AES-GCM mode w/ 256-bit key, 128-bit tag |
      +---------+-------+------------------------------------------+

                  Table 5: Algorithm Values for AES-GCM
```

#### §4.1.1. Security Considerations for AES-GCM

- (§4.1.1) "When using AES-GCM, the following restrictions MUST be enforced:"
- (§4.1.1) "The key and nonce pair MUST be unique for every message encrypted."
- (§4.1.1) "The total number of messages encrypted for a single key MUST NOT exceed 2^32 [SP800-38D]."
- (§4.1.1) "An explicit check is required only in environments where it is expected that this limit might be exceeded."
- (§4.1.1) "Based on that recommendation, one should restrict the number of messages encrypted to 2^24.5."
- (§4.1.1) "Following the recommendation in DTLS (Section 4.5.3 of [RFC9147]), the number of failed message decryptions should be limited to 2^36."
- (§4.1.1) "Given that Counter with CBC-MAC (CCM) is the usual mode for constrained environments, restricted modes are not supported."

### §4.2. AES-CCM

- (§4.2) "The CCM mode has two parameter choices.  The first choice is M, the size of the authentication field."
- (§4.2) "The second choice is L, the size of the length field."
- (§4.2) "We define a matrix of algorithms in this document over the values of L and M."
- (§4.2) "Keys may be obtained from either a key structure or a recipient structure."
- (§4.2) "This document will follow the convention of using bit counts so that it is easier to compare the different algorithms presented in this document."
- (§4.2) "Implementations that are encrypting or decrypting MUST validate that the key type, key length, and algorithm are correct and appropriate for the entities involved."
- (§4.2) "The "kty" field MUST be present"
- (§4.2) "it MUST be "Symmetric""
- (§4.2) "If the "alg" field is present, it MUST match the AES-CCM algorithm being used."
- (§4.2) "If the "key_ops" field is present, it MUST include "encrypt" or "wrap key" when encrypting."
- (§4.2) "If the "key_ops" field is present, it MUST include "decrypt" or "unwrap key" when decrypting."

```text
   The following values are used for L:

   16 bits (2):  This limits messages to 2^16 bytes (64 KiB) in length.
      This is sufficiently long for messages in the constrained world.
      The nonce length is 13 bytes allowing for 2^104 possible values of
      the nonce without repeating.

   64 bits (8):  This limits messages to 2^64 bytes in length.  The
      nonce length is 7 bytes, allowing for 2^56 possible values of the
      nonce without repeating.

   The following values are used for M:

   64 bits (8):  This produces a 64-bit authentication tag.  This
      implies that there is a 1 in 2^64 chance that a modified message
      will authenticate.

   128 bits (16):  This produces a 128-bit authentication tag.  This
      implies that there is a 1 in 2^128 chance that a modified message
      will authenticate.
```

```text
    +====================+=======+====+=====+========+===============+
    | Name               | Value | L  | M   |  Key   | Description   |
    |                    |       |    |     | Length |               |
    +====================+=======+====+=====+========+===============+
    | AES-CCM-16-64-128  |   10  | 16 | 64  |  128   | AES-CCM mode  |
    |                    |       |    |     |        | 128-bit key,  |
    |                    |       |    |     |        | 64-bit tag,   |
    |                    |       |    |     |        | 13-byte nonce |
    +--------------------+-------+----+-----+--------+---------------+
    | AES-CCM-16-64-256  |   11  | 16 | 64  |  256   | AES-CCM mode  |
    |                    |       |    |     |        | 256-bit key,  |
    |                    |       |    |     |        | 64-bit tag,   |
    |                    |       |    |     |        | 13-byte nonce |
    +--------------------+-------+----+-----+--------+---------------+
    | AES-CCM-64-64-128  |   12  | 64 | 64  |  128   | AES-CCM mode  |
    |                    |       |    |     |        | 128-bit key,  |
    |                    |       |    |     |        | 64-bit tag,   |
    |                    |       |    |     |        | 7-byte nonce  |
    +--------------------+-------+----+-----+--------+---------------+
    | AES-CCM-64-64-256  |   13  | 64 | 64  |  256   | AES-CCM mode  |
    |                    |       |    |     |        | 256-bit key,  |
    |                    |       |    |     |        | 64-bit tag,   |
    |                    |       |    |     |        | 7-byte nonce  |
    +--------------------+-------+----+-----+--------+---------------+
    | AES-CCM-16-128-128 |   30  | 16 | 128 |  128   | AES-CCM mode  |
    |                    |       |    |     |        | 128-bit key,  |
    |                    |       |    |     |        | 128-bit tag,  |
    |                    |       |    |     |        | 13-byte nonce |
    +--------------------+-------+----+-----+--------+---------------+
    | AES-CCM-16-128-256 |   31  | 16 | 128 |  256   | AES-CCM mode  |
    |                    |       |    |     |        | 256-bit key,  |
    |                    |       |    |     |        | 128-bit tag,  |
    |                    |       |    |     |        | 13-byte nonce |
    +--------------------+-------+----+-----+--------+---------------+
    | AES-CCM-64-128-128 |   32  | 64 | 128 |  128   | AES-CCM mode  |
    |                    |       |    |     |        | 128-bit key,  |
    |                    |       |    |     |        | 128-bit tag,  |
    |                    |       |    |     |        | 7-byte nonce  |
    +--------------------+-------+----+-----+--------+---------------+
    | AES-CCM-64-128-256 |   33  | 64 | 128 |  256   | AES-CCM mode  |
    |                    |       |    |     |        | 256-bit key,  |
    |                    |       |    |     |        | 128-bit tag,  |
    |                    |       |    |     |        | 7-byte nonce  |
    +--------------------+-------+----+-----+--------+---------------+

                  Table 6: Algorithm Values for AES-CCM
```

#### §4.2.1. Security Considerations for AES-CCM

- (§4.2.1) "When using AES-CCM, the following restrictions MUST be enforced:"
- (§4.2.1) "The key and nonce pair MUST be unique for every message encrypted."
- (§4.2.1) "The total number of times the AES block cipher is used MUST NOT exceed 2^61 operations."
- (§4.2.1) "An explicit check is required only in environments where it is expected that this limit might be exceeded."
- (§4.2.1) "Based on that recommendation, one should restrict the number of messages encrypted to 2^23."
- (§4.2.1) "Following the recommendation in DTLS (Section 4.5.3 of [RFC9147]), the number of failed message decryptions should be limited to 2^23.5."
- (§4.2.1) "It may be that, to keep the desired level of integrity, one needs to rekey as often as every 2^7 messages."
- (§4.2.1) "Ways to deal with this attack include adding a random portion to the nonce value and/or increasing the key size used."
- (§4.2.1) "It is possible to do a precomputation attack against the algorithm in cases where portions of the plaintext are highly predictable.  This reduces the security of the key size by half."

### §4.3. ChaCha20 and Poly1305

- (§4.3) "The ChaCha20/Poly1305 AEAD construction defined in [RFC8439] has no parameterization."
- (§4.3) "Keys may be obtained from either a key structure or a recipient structure."
- (§4.3) "It takes as inputs a 256-bit key and a 96-bit nonce, as well as the plaintext and additional data, and produces the ciphertext as an output."
- (§4.3) "Implementations that are encrypting or decrypting MUST validate that the key type, key length, and algorithm are correct and appropriate for the entities involved."
- (§4.3) "The "kty" field MUST be present"
- (§4.3) "it MUST be "Symmetric""
- (§4.3) "If the "alg" field is present, it MUST match the ChaCha20/Poly1305 algorithm being used."
- (§4.3) "If the "key_ops" field is present, it MUST include "encrypt" or "wrap key" when encrypting."
- (§4.3) "If the "key_ops" field is present, it MUST include "decrypt" or "unwrap key" when decrypting."

```text
         +===================+=======+==========================+
         | Name              | Value | Description              |
         +===================+=======+==========================+
         | ChaCha20/Poly1305 |   24  | ChaCha20/Poly1305 w/     |
         |                   |       | 256-bit key, 128-bit tag |
         +-------------------+-------+--------------------------+

              Table 7: Algorithm Value for ChaCha20/Poly1305
```

#### §4.3.1. Security Considerations for ChaCha20/Poly1305

- (§4.3.1) "The key and nonce values MUST be a unique pair for every invocation of the algorithm."
- (§4.3.1) "Nonce counters are considered to be an acceptable way of ensuring that they are unique."
- (§4.3.1) "Following the recommendation in DTLS (Section 4.5.3 of [RFC9147]), the number of failed message decryptions should be limited to 2^36."
- (§4.3.1) "COSE implementations should not send more than 2^64 messages encrypted using a single ChaCha20/Poly1305 key."

## §5. Key Derivation Functions (KDFs)

- (§5) "Section 8.4 of [RFC9052] contains a generic description of key derivation functions.  This document defines a single context structure and a single KDF.  These elements are used for all of the recipient algorithms defined in this document that require a KDF process.  These algorithms are defined in Sections 6.1.2, 6.3.1, and 6.4.1."

### §5.1. HMAC-Based Extract-and-Expand Key Derivation Function (HKDF)

- (§5.1) "The HKDF key derivation algorithm is defined in [RFC5869] and [HKDF]."
- (§5.1) "The HKDF algorithm takes these inputs:"
- (§5.1) "HKDF is defined to use HMAC as the underlying PRF."
- (§5.1) "When using a good random shared secret of the correct length, the extract step can be skipped."
- (§5.1) "If the salt is public and carried in the message, then the "salt" algorithm header parameter defined in Table 9 is used."
- (§5.1) "The salt value does not need to be unique for every message sent."
- (§5.1) "Specifically, one can use AES-CBC-MAC as the PRF for the expand step, but not for the extract step."
- (§5.1) "For the AES algorithm versions, the extract step is always skipped."
- (§5.1) "The extract step cannot be skipped if the secret is not uniformly random -- for example, if it is the result of an ECDH key agreement step."
- (§5.1) "This implies that the AES HKDF version cannot be used with ECDH."
- (§5.1) "If the extract step is skipped, the "salt" value is not used as part of the HKDF functionality."

```text
   secret:  A shared value that is secret.  Secrets may be either
      previously shared or derived from operations like a Diffie-Hellman
      (DH) key agreement.

   salt:  An optional value that is used to change the generation
      process.  The salt value can be either public or private.  If the
      salt is public and carried in the message, then the "salt"
      algorithm header parameter defined in Table 9 is used.  While
      [RFC5869] suggests that the length of the salt be the same as the
      length of the underlying hash value, any positive salt length will
      improve the security, as different key values will be generated.
      This parameter is protected by being included in the key
      computation and does not need to be separately authenticated.  The
      salt value does not need to be unique for every message sent.

   length:  The number of bytes of output that need to be generated.

   context information:  Information that describes the context in which
      the resulting value will be used.  Making this information
      specific to the context in which the material is going to be used
      ensures that the resulting material will always be tied to that
      usage.  The context structure defined in Section 5.2 is used by
      the KDFs in this document.

   PRF:  The underlying pseudorandom function to be used in the HKDF
      algorithm.  The PRF is encoded into the HKDF algorithm selection.
```

```text
       +==============+===================+========================+
       | Name         | PRF               | Description            |
       +==============+===================+========================+
       | HKDF SHA-256 | HMAC with SHA-256 | HKDF using HMAC        |
       |              |                   | SHA-256 as the PRF     |
       +--------------+-------------------+------------------------+
       | HKDF SHA-512 | HMAC with SHA-512 | HKDF using HMAC        |
       |              |                   | SHA-512 as the PRF     |
       +--------------+-------------------+------------------------+
       | HKDF AES-    | AES-CBC-MAC-128   | HKDF using AES-MAC as  |
       | MAC-128      |                   | the PRF w/ 128-bit key |
       +--------------+-------------------+------------------------+
       | HKDF AES-    | AES-CBC-MAC-256   | HKDF using AES-MAC as  |
       | MAC-256      |                   | the PRF w/ 256-bit key |
       +--------------+-------------------+------------------------+

                          Table 8: HKDF Algorithms
```

```text
    +======+=======+======+============================+=============+
    | Name | Label | Type | Algorithm                  | Description |
    +======+=======+======+============================+=============+
    | salt | -20   | bstr | direct+HKDF-SHA-256,       | Random salt |
    |      |       |      | direct+HKDF-SHA-512,       |             |
    |      |       |      | direct+HKDF-AES-128,       |             |
    |      |       |      | direct+HKDF-AES-256, ECDH- |             |
    |      |       |      | ES+HKDF-256, ECDH-ES+HKDF- |             |
    |      |       |      | 512, ECDH-SS+HKDF-256,     |             |
    |      |       |      | ECDH-SS+HKDF-512, ECDH-    |             |
    |      |       |      | ES+A128KW, ECDH-ES+A192KW, |             |
    |      |       |      | ECDH-ES+A256KW, ECDH-      |             |
    |      |       |      | SS+A128KW, ECDH-SS+A192KW, |             |
    |      |       |      | ECDH-SS+A256KW             |             |
    +------+-------+------+----------------------------+-------------+

                    Table 9: HKDF Algorithm Parameters
```

### §5.2. Context Information Structure

- (§5.2) "The context information structure is used to ensure that the derived keying material is "bound" to the context of the transaction."
- (§5.2) "The context information structure used here is based on that defined in [SP800-56A]."
- (§5.2) "The context structure is built from information that is known to both entities."
- (§5.2) "We define a CBOR object to hold the context information.  This object is referred to as COSE_KDF_Context.  The object is based on a CBOR array type."
- (§5.2) "Unless the application protocol defines differently, we assign PartyU to the entity that is creating the message and PartyV to the entity that is receiving the message."
- (§5.2) "These header parameters are designed to be placed in the unprotected bucket of the recipient structure; they do not need to be in the protected bucket, since they are already included in the cryptographic computation by virtue of being included in the context structure."
- (§5.2) "This field is required to be present."
- (§5.2) "The elements of PartyUInfo are encoded in the order presented below."
- (§5.2) "If identity information is carried in the message, applications SHOULD have a way of validating the supplied identity information."
- (§5.2) "The identity information does not need to be specified and is set to nil in that case."
- (§5.2) "This option does not need to be specified; if not needed, it is set to nil."
- (§5.2) "This option does not need to be specified; if not needed, it is set to nil."
- (§5.2) "This field holds information about PartyV.  The content of the structure is the same as for the PartyUInfo but for PartyV."
- (§5.2) "This is set to the number of bits of the desired output value."
- (§5.2) "If there are no elements in the "protected" field, then use a zero-length bstr."
- (§5.2) "Applications that define this SHOULD use CBOR to encode the data so that types and lengths are correctly included."
- (§5.2) "Applications that define this SHOULD use CBOR to encode the data so that types and lengths are correctly included."

```text
   +==========+=======+======+===========================+=============+
   | Name     | Label | Type | Algorithm                 | Description |
   +==========+=======+======+===========================+=============+
   | PartyU   | -21   | bstr | direct+HKDF-SHA-256,      | PartyU      |
   | identity |       |      | direct+HKDF-SHA-512,      | identity    |
   |          |       |      | direct+HKDF-AES-128,      | information |
   |          |       |      | direct+HKDF-AES-256,      |             |
   |          |       |      | ECDH-ES+HKDF-256,         |             |
   |          |       |      | ECDH-ES+HKDF-512,         |             |
   |          |       |      | ECDH-SS+HKDF-256,         |             |
   |          |       |      | ECDH-SS+HKDF-512,         |             |
   |          |       |      | ECDH-ES+A128KW,           |             |
   |          |       |      | ECDH-ES+A192KW,           |             |
   |          |       |      | ECDH-ES+A256KW,           |             |
   |          |       |      | ECDH-SS+A128KW,           |             |
   |          |       |      | ECDH-SS+A192KW,           |             |
   |          |       |      | ECDH-SS+A256KW            |             |
   +----------+-------+------+---------------------------+-------------+
   | PartyU   | -22   | bstr | direct+HKDF-SHA-256,      | PartyU      |
   | nonce    |       | /    | direct+HKDF-SHA-512,      | provided    |
   |          |       | int  | direct+HKDF-AES-128,      | nonce       |
   |          |       |      | direct+HKDF-AES-256,      |             |
   |          |       |      | ECDH-ES+HKDF-256,         |             |
   |          |       |      | ECDH-ES+HKDF-512,         |             |
   |          |       |      | ECDH-SS+HKDF-256,         |             |
   |          |       |      | ECDH-SS+HKDF-512,         |             |
   |          |       |      | ECDH-ES+A128KW,           |             |
   |          |       |      | ECDH-ES+A192KW,           |             |
   |          |       |      | ECDH-ES+A256KW,           |             |
   |          |       |      | ECDH-SS+A128KW,           |             |
   |          |       |      | ECDH-SS+A192KW,           |             |
   |          |       |      | ECDH-SS+A256KW            |             |
   +----------+-------+------+---------------------------+-------------+
   | PartyU   | -23   | bstr | direct+HKDF-SHA-256,      | PartyU      |
   | other    |       |      | direct+HKDF-SHA-512,      | other       |
   |          |       |      | direct+HKDF-AES-128,      | provided    |
   |          |       |      | direct+HKDF-AES-256,      | information |
   |          |       |      | ECDH-ES+HKDF-256,         |             |
   |          |       |      | ECDH-ES+HKDF-512,         |             |
   |          |       |      | ECDH-SS+HKDF-256,         |             |
   |          |       |      | ECDH-SS+HKDF-512,         |             |
   |          |       |      | ECDH-ES+A128KW,           |             |
   |          |       |      | ECDH-ES+A192KW,           |             |
   |          |       |      | ECDH-ES+A256KW,           |             |
   |          |       |      | ECDH-SS+A128KW,           |             |
   |          |       |      | ECDH-SS+A192KW,           |             |
   |          |       |      | ECDH-SS+A256KW            |             |
   +----------+-------+------+---------------------------+-------------+
   | PartyV   | -24   | bstr | direct+HKDF-SHA-256,      | PartyV      |
   | identity |       |      | direct+HKDF-SHA-512,      | identity    |
   |          |       |      | direct+HKDF-AES-128,      | information |
   |          |       |      | direct+HKDF-AES-256,      |             |
   |          |       |      | ECDH-ES+HKDF-256,         |             |
   |          |       |      | ECDH-ES+HKDF-512,         |             |
   |          |       |      | ECDH-SS+HKDF-256,         |             |
   |          |       |      | ECDH-SS+HKDF-512,         |             |
   |          |       |      | ECDH-ES+A128KW,           |             |
   |          |       |      | ECDH-ES+A192KW,           |             |
   |          |       |      | ECDH-ES+A256KW,           |             |
   |          |       |      | ECDH-SS+A128KW,           |             |
   |          |       |      | ECDH-SS+A192KW,           |             |
   |          |       |      | ECDH-SS+A256KW            |             |
   +----------+-------+------+---------------------------+-------------+
   | PartyV   | -25   | bstr | direct+HKDF-SHA-256,      | PartyV      |
   | nonce    |       | /    | direct+HKDF-SHA-512,      | provided    |
   |          |       | int  | direct+HKDF-AES-128,      | nonce       |
   |          |       |      | direct+HKDF-AES-256,      |             |
   |          |       |      | ECDH-ES+HKDF-256,         |             |
   |          |       |      | ECDH-ES+HKDF-512,         |             |
   |          |       |      | ECDH-SS+HKDF-256,         |             |
   |          |       |      | ECDH-SS+HKDF-512,         |             |
   |          |       |      | ECDH-ES+A128KW,           |             |
   |          |       |      | ECDH-ES+A192KW,           |             |
   |          |       |      | ECDH-ES+A256KW,           |             |
   |          |       |      | ECDH-SS+A128KW,           |             |
   |          |       |      | ECDH-SS+A192KW,           |             |
   |          |       |      | ECDH-SS+A256KW            |             |
   +----------+-------+------+---------------------------+-------------+
   | PartyV   | -26   | bstr | direct+HKDF-SHA-256,      | PartyV      |
   | other    |       |      | direct+HKDF-SHA-512,      | other       |
   |          |       |      | direct+HKDF-AES-128,      | provided    |
   |          |       |      | direct+HKDF-AES-256,      | information |
   |          |       |      | ECDH-ES+HKDF-256,         |             |
   |          |       |      | ECDH-ES+HKDF-512,         |             |
   |          |       |      | ECDH-SS+HKDF-256,         |             |
   |          |       |      | ECDH-SS+HKDF-512,         |             |
   |          |       |      | ECDH-ES+A128KW,           |             |
   |          |       |      | ECDH-ES+A192KW,           |             |
   |          |       |      | ECDH-ES+A256KW,           |             |
   |          |       |      | ECDH-SS+A128KW,           |             |
   |          |       |      | ECDH-SS+A192KW,           |             |
   |          |       |      | ECDH-SS+A256KW            |             |
   +----------+-------+------+---------------------------+-------------+

                   Table 10: Context Algorithm Parameters
```

```text
   PartyInfo = (
       identity : bstr / nil,
       nonce : bstr / int / nil,
       other : bstr / nil
   )

   COSE_KDF_Context = [
       AlgorithmID : int / tstr,
       PartyUInfo : [ PartyInfo ],
       PartyVInfo : [ PartyInfo ],
       SuppPubInfo : [
           keyDataLength : uint,
           protected : empty_or_serialized_map,
           ? other : bstr
       ],
       ? SuppPrivInfo : bstr
   ]
```

## §6. Content Key Distribution Methods

- (§6) "Section 8.5 of [RFC9052] contains a generic description of content key distribution methods.  This document defines the identifiers and usage for a number of content key distribution methods."

### §6.1. Direct Encryption

- (§6.1) "A direct encryption algorithm is defined in Section 8.5.1 of [RFC9052].  Information about how to fill in the COSE_Recipient structure is detailed there."

#### §6.1.1. Direct Key

- (§6.1.1) "This recipient algorithm is the simplest; the identified key is directly used as the key for the next layer down in the message."
- (§6.1.1) "There are no algorithm parameters defined for this algorithm."
- (§6.1.1) "When this algorithm is used, the "protected" field MUST be zero length."
- (§6.1.1) "The key type MUST be "Symmetric"."

```text
      +========+=======+============================================+
      | Name   | Value | Description                                |
      +========+=======+============================================+
      | direct |   -6  | Direct use of content encryption key (CEK) |
      +--------+-------+--------------------------------------------+

                            Table 11: Direct Key
```

##### §6.1.1.1. Security Considerations for Direct Key

- (§6.1.1.1) "These keys need to have some method of being regularly updated over time."
- (§6.1.1.1) "These keys need to be dedicated to a single algorithm."
- (§6.1.1.1) "All of the content encryption algorithms specified in this document have limits on how many times a key can be used without significant loss of security."
- (§6.1.1.1) "Breaking one message means all messages are broken."

#### §6.1.2. Direct Key with KDF

- (§6.1.2) "These recipient algorithms take a common shared secret between the two parties and apply the HKDF function (Section 5.1), using the context structure defined in Section 5.2 to transform the shared secret into the CEK."
- (§6.1.2) "The "protected" field can be of nonzero length."
- (§6.1.2) "Either the "salt" parameter for HKDF (Table 9) or the "PartyU nonce" parameter for the context structure (Table 10) MUST be present (both can be present if desired)."
- (§6.1.2) "The requirement is that it be a unique value for the shared secret in question."
- (§6.1.2) "A new IV must be used for each message if the same key is used."
- (§6.1.2) "If HKDF is used for generating the IV, the algorithm identifier is set to 34 ("IV-"
- (§6.1.2) "The "kty" field MUST be present"
- (§6.1.2) "it MUST be "Symmetric""
- (§6.1.2) "If the "alg" field is present, it MUST match the algorithm being used."
- (§6.1.2) "If the "key_ops" field is present, it MUST include "derive key" or "derive bits"."
- (§6.1.2) "If the salt/nonce value is generated randomly, then it is suggested that the length of the random value be the same length as the output of the hash function underlying HKDF."
- (§6.1.2) "If the salt/nonce value is generated deterministically, it can be guaranteed to be unique, and thus there is no length requirement."
- (§6.1.2) "The IV can be modified in a predictable manner, a random manner, or an unpredictable manner (e.g., encrypting a counter)."

```text
   +=====================+=======+==============+=====================+
   | Name                | Value | KDF          | Description         |
   +=====================+=======+==============+=====================+
   | direct+HKDF-SHA-256 |  -10  | HKDF SHA-256 | Shared secret w/    |
   |                     |       |              | HKDF and SHA-256    |
   +---------------------+-------+--------------+---------------------+
   | direct+HKDF-SHA-512 |  -11  | HKDF SHA-512 | Shared secret w/    |
   |                     |       |              | HKDF and SHA-512    |
   +---------------------+-------+--------------+---------------------+
   | direct+HKDF-AES-128 |  -12  | HKDF AES-    | Shared secret w/    |
   |                     |       | MAC-128      | AES-MAC 128-bit key |
   +---------------------+-------+--------------+---------------------+
   | direct+HKDF-AES-256 |  -13  | HKDF AES-    | Shared secret w/    |
   |                     |       | MAC-256      | AES-MAC 256-bit key |
   +---------------------+-------+--------------+---------------------+

                      Table 12: Direct Key with KDF
```

##### §6.1.2.1. Security Considerations for Direct Key with KDF

- (§6.1.2.1) "The shared secret needs to have some method of being regularly updated over time."
- (§6.1.2.1) "Although not used directly, it should still be subject to scheduled rotation."
- (§6.1.2.1) "These methods do not provide for perfect forward secrecy, as the same shared secret is used for all of the keys generated; however, if the key for any single message is discovered, only the message or series of messages using that derived key are compromised."

### §6.2. Key Wrap

- (§6.2) "Key wrap is defined in Section 8.5.2 of [RFC9052].  Information about how to fill in the COSE_Recipient structure is detailed there."

#### §6.2.1. AES Key Wrap

- (§6.2.1) "The AES Key Wrap algorithm is defined in [RFC3394]."
- (§6.2.1) "As such, it can be used to wrap a key for any of the content encryption algorithms defined in this document."
- (§6.2.1) "The algorithm requires a single fixed parameter, the initial value."
- (§6.2.1) "There are no public key parameters that vary on a per-invocation basis."
- (§6.2.1) "Keys may be obtained from either a key structure or a recipient structure."
- (§6.2.1) "This algorithm uses an AES key to wrap a value that is a multiple of 64 bits."
- (§6.2.1) "This is fixed to the value specified in Section 2.2.3.1 of [RFC3394]."
- (§6.2.1) "The protected header bucket MUST be empty."
- (§6.2.1) "Implementations that are encrypting or decrypting MUST validate that the key type, key length, and algorithm are correct and appropriate for the entities involved."
- (§6.2.1) "The "kty" field MUST be present"
- (§6.2.1) "it MUST be "Symmetric""
- (§6.2.1) "If the "alg" field is present, it MUST match the AES Key Wrap algorithm being used."
- (§6.2.1) "If the "key_ops" field is present, it MUST include "encrypt" or "wrap key" when encrypting."
- (§6.2.1) "If the "key_ops" field is present, it MUST include "decrypt" or "unwrap key" when decrypting."

```text
        +========+=======+==========+=============================+
        | Name   | Value | Key Size | Description                 |
        +========+=======+==========+=============================+
        | A128KW |   -3  |   128    | AES Key Wrap w/ 128-bit key |
        +--------+-------+----------+-----------------------------+
        | A192KW |   -4  |   192    | AES Key Wrap w/ 192-bit key |
        +--------+-------+----------+-----------------------------+
        | A256KW |   -5  |   256    | AES Key Wrap w/ 256-bit key |
        +--------+-------+----------+-----------------------------+

                  Table 13: AES Key Wrap Algorithm Values
```

##### §6.2.1.1. Security Considerations for AES Key Wrap

- (§6.2.1.1) "The shared secret needs to have some method of being regularly updated over time."

### §6.3. Direct Key Agreement

- (§6.3) "Direct Key Agreement is defined in Section 8.5.4 of [RFC9052].  Information about how to fill in the COSE_Recipient structure is detailed there."

#### §6.3.1. Direct ECDH

- (§6.3.1) "The mathematics for ECDH can be found in [RFC6090].  In this document, the algorithm is extended to be used with the two curves defined in [RFC7748]."
- (§6.3.1) "ECDH is parameterized by the following:"
- (§6.3.1) "The key agreement process may be done using either a static or an ephemeral key for the sender's side."
- (§6.3.1) "It is acceptable to use a global counter that is incremented for every Static-Static operation and use the resulting value."
- (§6.3.1) "The static key can be identified by providing either the key ("static key") or a key identifier for the static key ("static key id")."
- (§6.3.1) "The x-coordinate is used for all of the curves defined in this document."
- (§6.3.1) "For curves X25519 and X448, the resulting value is used directly, as it is a byte string of a known length."
- (§6.3.1) "For the P-256, P-384, and P-521 curves, the x-coordinate is run through the Integer-to-Octet-String primitive (I2OSP) function defined in [RFC8017], using the same computation for n as is defined in Section 2.1."
- (§6.3.1) "When using ephemeral keys, the sender MUST generate a new ephemeral key for every key agreement operation."
- (§6.3.1) "The ephemeral key is placed in the "ephemeral key" parameter and MUST be present for all algorithm identifiers that use ephemeral keys."
- (§6.3.1) "When using static keys, the sender MUST either generate a new random value or create a unique value for use as a KDF input."
- (§6.3.1) "For the KDFs used, this means that either the "salt" parameter for HKDF (Table 9) or the "PartyU nonce" parameter for the context structure (Table 10) MUST be present (both can be present if desired)."
- (§6.3.1) "The value in the parameter MUST be unique for the pair of keys being used."
- (§6.3.1) "Care must be taken that the counter is saved to permanent storage in a way that avoids reuse of that counter value."
- (§6.3.1) "When using static keys, the static key should be identified to the recipient."
- (§6.3.1) "The result of an ECDH key agreement process does not provide a uniformly random secret.  As such, it needs to be run through a KDF in order to produce a usable key."
- (§6.3.1) "All of the algorithms defined in this document use one of the HKDF algorithms defined in Section 5.1 with the context structure defined in Section 5.2."
- (§6.3.1) "No key wrap algorithm is used.  This is represented in Table 14 as "none".  The key size for the context structure is the content layer encryption algorithm size."
- (§6.3.1) "COSE does not have an Ephemeral-Ephemeral version defined."
- (§6.3.1) "This document defines these algorithms to be used with the curves P-256, P-384, P-521, X25519, and X448."
- (§6.3.1) "Implementations MUST verify that the key type and curve are correct."
- (§6.3.1) "Different curves are restricted to different key types."
- (§6.3.1) "Implementations MUST verify that the curve and algorithm are appropriate for the entities involved."
- (§6.3.1) "The "kty" field MUST be present"
- (§6.3.1) "it MUST be "EC2" or "OKP""
- (§6.3.1) "If the "alg" field is present, it MUST match the key agreement algorithm being used."
- (§6.3.1) "If the "key_ops" field is present, it MUST include "derive key" or "derive bits" for the private key."
- (§6.3.1) "If the "key_ops" field is present, it MUST be empty for the public key."

```text
   +==========+=======+=========+==================+=====+=============+
   |Name      | Value | KDF     | Ephemeral-Static |Key  |Description  |
   |          |       |         |                  |Wrap |             |
   +==========+=======+=========+==================+=====+=============+
   |ECDH-ES + | -25   | HKDF -- | yes              |none |ECDH ES w/   |
   |HKDF-256  |       | SHA-256 |                  |     |HKDF --      |
   |          |       |         |                  |     |generate key |
   |          |       |         |                  |     |directly     |
   +----------+-------+---------+------------------+-----+-------------+
   |ECDH-ES + | -26   | HKDF -- | yes              |none |ECDH ES w/   |
   |HKDF-512  |       | SHA-512 |                  |     |HKDF --      |
   |          |       |         |                  |     |generate key |
   |          |       |         |                  |     |directly     |
   +----------+-------+---------+------------------+-----+-------------+
   |ECDH-SS + | -27   | HKDF -- | no               |none |ECDH SS w/   |
   |HKDF-256  |       | SHA-256 |                  |     |HKDF --      |
   |          |       |         |                  |     |generate key |
   |          |       |         |                  |     |directly     |
   +----------+-------+---------+------------------+-----+-------------+
   |ECDH-SS + | -28   | HKDF -- | no               |none |ECDH SS w/   |
   |HKDF-512  |       | SHA-512 |                  |     |HKDF --      |
   |          |       |         |                  |     |generate key |
   |          |       |         |                  |     |directly     |
   +----------+-------+---------+------------------+-----+-------------+

                      Table 14: ECDH Algorithm Values
```

```text
    +===========+=======+==========+===================+=============+
    | Name      | Label | Type     | Algorithm         | Description |
    +===========+=======+==========+===================+=============+
    | ephemeral | -1    | COSE_Key | ECDH-ES+HKDF-256, | Ephemeral   |
    | key       |       |          | ECDH-ES+HKDF-512, | public key  |
    |           |       |          | ECDH-ES+A128KW,   | for the     |
    |           |       |          | ECDH-ES+A192KW,   | sender      |
    |           |       |          | ECDH-ES+A256KW    |             |
    +-----------+-------+----------+-------------------+-------------+
    | static    | -2    | COSE_Key | ECDH-SS+HKDF-256, | Static      |
    | key       |       |          | ECDH-SS+HKDF-512, | public key  |
    |           |       |          | ECDH-SS+A128KW,   | for the     |
    |           |       |          | ECDH-SS+A192KW,   | sender      |
    |           |       |          | ECDH-SS+A256KW    |             |
    +-----------+-------+----------+-------------------+-------------+
    | static    | -3    | bstr     | ECDH-SS+HKDF-256, | Static      |
    | key id    |       |          | ECDH-SS+HKDF-512, | public key  |
    |           |       |          | ECDH-SS+A128KW,   | identifier  |
    |           |       |          | ECDH-SS+A192KW,   | for the     |
    |           |       |          | ECDH-SS+A256KW    | sender      |
    +-----------+-------+----------+-------------------+-------------+

                   Table 15: ECDH Algorithm Parameters
```

##### §6.3.1.1. Security Considerations for ECDH

- (§6.3.1.1) "There is a method of checking that points provided from external entities are valid."
- (§6.3.1.1) "For the "EC2" key format, this can be done by checking that the x and y values form a point on the curve."
- (§6.3.1.1) "For the "OKP" format, there is no simple way to perform point validation."
- (§6.3.1.1) "Consideration was given to requiring that the public keys of both entities be provided as part of the key derivation process (as recommended in Section 6.1 of [RFC7748]).  This was not done, because COSE is used in a store-and-forward format rather than in online key exchange."
- (§6.3.1.1) "A proof of possession of the private key associated with the public key is recommended when a key is moved from untrusted to trusted (either by the end user or by the entity that is responsible for making trust statements on keys)."

### §6.4. Key Agreement with Key Wrap

- (§6.4) "Key Agreement with Key Wrap is defined in Section 8.5.5 of [RFC9052].  Information about how to fill in the COSE_Recipient structure is detailed there."

#### §6.4.1. ECDH with Key Wrap

- (§6.4.1) "ECDH with Key Agreement is parameterized by the same header parameters as for ECDH; see Section 6.3.1, with the following modifications:"
- (§6.4.1) "Any of the key wrap algorithms defined in Section 6.2 are supported."
- (§6.4.1) "The size of the key used for the key wrap algorithm is fed into the KDF."
- (§6.4.1) "The "kty" field MUST be present"
- (§6.4.1) "it MUST be "EC2" or "OKP""
- (§6.4.1) "If the "alg" field is present, it MUST match the key agreement algorithm being used."
- (§6.4.1) "If the "key_ops" field is present, it MUST include "derive key" or "derive bits" for the private key."
- (§6.4.1) "If the "key_ops" field is present, it MUST be empty for the public key."

```text
   +=========+=====+=========+==================+========+=============+
   |Name     |Value| KDF     | Ephemeral-Static |Key Wrap|Description  |
   +=========+=====+=========+==================+========+=============+
   |ECDH-ES +|-29  | HKDF -- | yes              |A128KW  |ECDH ES w/   |
   |A128KW   |     | SHA-256 |                  |        |HKDF and AES |
   |         |     |         |                  |        |Key Wrap w/  |
   |         |     |         |                  |        |128-bit key  |
   +---------+-----+---------+------------------+--------+-------------+
   |ECDH-ES +|-30  | HKDF -- | yes              |A192KW  |ECDH ES w/   |
   |A192KW   |     | SHA-256 |                  |        |HKDF and AES |
   |         |     |         |                  |        |Key Wrap w/  |
   |         |     |         |                  |        |192-bit key  |
   +---------+-----+---------+------------------+--------+-------------+
   |ECDH-ES +|-31  | HKDF -- | yes              |A256KW  |ECDH ES w/   |
   |A256KW   |     | SHA-256 |                  |        |HKDF and AES |
   |         |     |         |                  |        |Key Wrap w/  |
   |         |     |         |                  |        |256-bit key  |
   +---------+-----+---------+------------------+--------+-------------+
   |ECDH-SS +|-32  | HKDF -- | no               |A128KW  |ECDH SS w/   |
   |A128KW   |     | SHA-256 |                  |        |HKDF and AES |
   |         |     |         |                  |        |Key Wrap w/  |
   |         |     |         |                  |        |128-bit key  |
   +---------+-----+---------+------------------+--------+-------------+
   |ECDH-SS +|-33  | HKDF -- | no               |A192KW  |ECDH SS w/   |
   |A192KW   |     | SHA-256 |                  |        |HKDF and AES |
   |         |     |         |                  |        |Key Wrap w/  |
   |         |     |         |                  |        |192-bit key  |
   +---------+-----+---------+------------------+--------+-------------+
   |ECDH-SS +|-34  | HKDF -- | no               |A256KW  |ECDH SS w/   |
   |A256KW   |     | SHA-256 |                  |        |HKDF and AES |
   |         |     |         |                  |        |Key Wrap w/  |
   |         |     |         |                  |        |256-bit key  |
   +---------+-----+---------+------------------+--------+-------------+

               Table 16: ECDH Algorithm Values with Key Wrap
```

## §7. Key Object Parameters

- (§7) "The COSE_Key object defines a way to hold a single key object.  It is still required that the members of individual key types be defined."
- (§7) "In this document, we define four values for the member:"
- (§7) "Key types are identified by the "kty" member of the COSE_Key object."

```text
             +===========+=======+==========================+
             | Name      | Value | Description              |
             +===========+=======+==========================+
             | OKP       |   1   | Octet Key Pair           |
             +-----------+-------+--------------------------+
             | EC2       |   2   | Elliptic Curve Keys w/   |
             |           |       | x- and y-coordinate pair |
             +-----------+-------+--------------------------+
             | Symmetric |   4   | Symmetric Keys           |
             +-----------+-------+--------------------------+
             | Reserved  |   0   | This value is reserved   |
             +-----------+-------+--------------------------+

                        Table 17: Key Type Values
```

### §7.1. Elliptic Curve Keys

- (§7.1) "Two different key structures are defined for elliptic curve keys.  One version uses both an x-coordinate and a y-coordinate, potentially with point compression ("EC2")."
- (§7.1) "The other version uses only the x-coordinate, as the y-coordinate is either to be recomputed or not needed for the key agreement operation ("OKP")."
- (§7.1) "Applications MUST check that the curve and the key type are consistent and reject a key if they are not."

```text
   +=========+=======+==========+=====================================+
   | Name    | Value | Key Type | Description                         |
   +=========+=======+==========+=====================================+
   | P-256   |   1   |   EC2    | NIST P-256, also known as secp256r1 |
   +---------+-------+----------+-------------------------------------+
   | P-384   |   2   |   EC2    | NIST P-384, also known as secp384r1 |
   +---------+-------+----------+-------------------------------------+
   | P-521   |   3   |   EC2    | NIST P-521, also known as secp521r1 |
   +---------+-------+----------+-------------------------------------+
   | X25519  |   4   |   OKP    | X25519 for use w/ ECDH only         |
   +---------+-------+----------+-------------------------------------+
   | X448    |   5   |   OKP    | X448 for use w/ ECDH only           |
   +---------+-------+----------+-------------------------------------+
   | Ed25519 |   6   |   OKP    | Ed25519 for use w/ EdDSA only       |
   +---------+-------+----------+-------------------------------------+
   | Ed448   |   7   |   OKP    | Ed448 for use w/ EdDSA only         |
   +---------+-------+----------+-------------------------------------+

                        Table 18: Elliptic Curves
```

#### §7.1.1. Double Coordinate Curves

- (§7.1.1) "The members that are defined for this key type are:"
- (§7.1.1) "This contains an identifier of the curve to be used with the key."
- (§7.1.1) "Compressed point encoding is also supported."
- (§7.1.1) "This contains the private key."
- (§7.1.1) "For EC keys with both coordinates, the "kty" member is set to 2 (EC2)."
- (§7.1.1) "Other curves may be registered in the future, and private curves can be used as well."
- (§7.1.1) "This contains the x-coordinate for the EC point.  The integer is converted to a byte string as defined in [SEC1]."
- (§7.1.1) "zero octets MUST be preserved."
- (§7.1.1) "When encoding the value y, the integer is converted to a byte string (as defined in [SEC1]) and encoded as a CBOR bstr."
- (§7.1.1) "Leading-zero octets MUST be preserved."
- (§7.1.1) "If the sign bit is zero, then encode y as a CBOR false value; otherwise, encode y as a CBOR true value."
- (§7.1.1) "The encoding of the infinity point is not supported."
- (§7.1.1) "For public keys, it is REQUIRED that "crv", "x", and "y" be present in the structure."
- (§7.1.1) "For private keys, it is REQUIRED that "crv" and "d" be present in the structure."
- (§7.1.1) "For private keys, it is RECOMMENDED that "x" and "y" also be present, but they can be recomputed from the required elements, and omitting them saves on space."

```text
    +======+======+=======+========+=================================+
    | Key  | Name | Label | CBOR   | Description                     |
    | Type |      |       | Type   |                                 |
    +======+======+=======+========+=================================+
    |  2   | crv  |   -1  | int /  | EC identifier -- Taken from the |
    |      |      |       | tstr   | "COSE Elliptic Curves" registry |
    +------+------+-------+--------+---------------------------------+
    |  2   |  x   |   -2  | bstr   | x-coordinate                    |
    +------+------+-------+--------+---------------------------------+
    |  2   |  y   |   -3  | bstr / | y-coordinate                    |
    |      |      |       | bool   |                                 |
    +------+------+-------+--------+---------------------------------+
    |  2   |  d   |   -4  | bstr   | Private key                     |
    +------+------+-------+--------+---------------------------------+

                       Table 19: EC Key Parameters
```

### §7.2. Octet Key Pair

- (§7.2) "A new key type is defined for Octet Key Pairs (OKPs)."
- (§7.2) "This key type could be used for other curve types (for example, mathematics based on hyper-elliptic surfaces)."
- (§7.2) "Do not assume that keys using this type are elliptic curves."
- (§7.2) "Other curves may be registered in the future, and private curves can be used as well."
- (§7.2) "This contains the public key.  The byte string contains the public key as defined by the algorithm.  (For X25519, internally it is a little-endian integer.)"
- (§7.2) "For public keys, it is REQUIRED that "crv" and "x" be present in the structure."
- (§7.2) "For private keys, it is REQUIRED that "crv" and "d" be present in the structure."
- (§7.2) "For private keys, it is RECOMMENDED that "x" also be present, but it can be recomputed from the required elements, and omitting it saves on space."

```text
   +======+==========+=======+=======+=================================+
   | Name |   Key    | Label | Type  | Description                     |
   |      |   Type   |       |       |                                 |
   +======+==========+=======+=======+=================================+
   | crv  |    1     |   -1  | int / | EC identifier -- Taken from the |
   |      |          |       | tstr  | "COSE Elliptic Curves" registry |
   +------+----------+-------+-------+---------------------------------+
   | x    |    1     |   -2  | bstr  | Public Key                      |
   +------+----------+-------+-------+---------------------------------+
   | d    |    1     |   -4  | bstr  | Private key                     |
   +------+----------+-------+-------+---------------------------------+

                    Table 20: Octet Key Pair Parameters
```

### §7.3. Symmetric Keys

- (§7.3) "This contains the value of the key."
- (§7.3) "This key structure does not have a form that contains only public members."
- (§7.3) "For symmetric keys, the "kty" member is set to 4 ("Symmetric")."
- (§7.3) "As it is expected that this key structure is going to be transmitted, care must be taken that it is never transmitted accidentally or insecurely."
- (§7.3) "For symmetric keys, it is REQUIRED that "k" be present in the structure."

```text
             +======+==========+=======+======+=============+
             | Name | Key Type | Label | Type | Description |
             +======+==========+=======+======+=============+
             |  k   |    4     |   -1  | bstr | Key Value   |
             +------+----------+-------+------+-------------+

                    Table 21: Symmetric Key Parameters
```

## §8. COSE Capabilities

- (§8) "Two different types of capabilities are defined: capabilities for algorithms and capabilities for key type."
- (§8) "The capability structure is an array of values; the values included in the structure are dependent on a specific algorithm or key type."
- (§8) "The algorithm identifier is not included in the capabilities data, as it should be encoded elsewhere in the message."
- (§8) "The key type identifier is included in the capabilities data, as it is not expected to be encoded elsewhere."
- (§8) "Once defined by registration with IANA, the list of capabilities for an algorithm or key type is immutable."
- (§8) "If it is later found that a new capability is needed for a key type or algorithm, it will require that a new code point be assigned to deal with that."
- (§8) "For algorithm capabilities, the first element should always be a key type value if applicable, but the items that are specific to a key (for example, a curve) should not be included in the algorithm capabilities."
- (§8) "For a key, the first element should be the key type value."

### §8.1. Assignments for Existing Algorithms

- (§8.1) "GENERATION (those in this document as well as those in [RFC8230], [RFC8778], and [RFC9021]), the capabilities list is an array with one element, the key type (from the "COSE Key Types" Registry)."
- (§8.1) "It is expected that future registered algorithms could have zero, one, or multiple elements."

### §8.2. Assignments for Existing Key Types

- (§8.2) "There are a number of pre-existing key types; the following deals with creating the capability definition for those structures:"

```text
   *  OKP, EC2: The list of capabilities is:

      -  The key type value.  (1 for OKP or 2 for EC2.)

      -  One curve for that key type from the "COSE Elliptic Curves"
         registry.

   *  RSA: The list of capabilities is:

      -  The key type value (3).

   *  Symmetric: The list of capabilities is:

      -  The key type value (4).

   *  HSS-LMS: The list of capabilities is:

      -  The key type value (5).

      -  Algorithm identifier for the underlying hash function from the
         "COSE Algorithms" registry.

   *  WalnutDSA: The list of capabilities is:

      -  The key type value (6).

      -  The N value (group and matrix size) for the key, a uint.

      -  The q value (finite field order) for the key, a uint.
```

### §8.3. Examples

- (§8.3) "Capabilities can be used in a key derivation process to make sure that both sides are using the same parameters."

```text
   Algorithm ES256

   0x8102                 / [2 \ EC2 \ ] /

   Key type EC2 with P-256 curve:

   0x820201               / [2 \ EC2 \, 1 \ P-256 \] /

   ECDH-ES + A256KW with an X25519 curve:

   0x8101820104           / [1 \ OKP \],[1 \ OKP \, 4 \ X25519 \] /
```

```text
   [
    [-8 / EdDSA /,
      [1 / OKP key type /],
      [
        [1 / OKP /, 6 / Ed25519 / ],
        [1 /OKP/, 7 /Ed448 /]
      ]
    ],
    [-7 / ECDSA with SHA-256/,
      [2 /EC2 key type/],
      [
        [2 /EC2/, 1 /P-256/],
        [2 /EC2/, 3 /P-521/]
      ]
    ],
    [ -31 / ECDH-ES+A256KW/,
      [
        [ 2 /EC2/],
        [1 /OKP/ ]
      ],
      [
        [2 /EC2/, 1 /P-256/],
        [1 /OKP/, 4 / X25519/ ]
      ]
    ],
    [ 1 / A128GCM /,
      [ 4 / Symmetric / ],
      [ 4 / Symmetric /]
    ]
   ]
```

## §9. CBOR Encoding Restrictions

- (§9) "This document limits the restrictions it imposes on how the CBOR Encoder needs to work.  The new encoding restrictions are aligned with the Core Deterministic Encoding Requirements specified in Section 4.2.1 of RFC 8949 [STD94].  It has been narrowed down to the following restrictions:"
- (§9) "This means that the integer 1 is encoded as "0x01" and not "0x1801"."
- (§9) "The restriction applies to the encoding of the COSE_KDF_Context."
- (§9) "Encoding MUST be done using definite lengths"
- (§9) "the length of the (encoded) argument MUST be the minimum possible length"
- (§9) "Applications MUST NOT generate messages with the same label used twice as a key in a single map."
- (§9) "Applications MUST NOT parse and process messages with the same label used twice as a key in a single map."
- (§9) "Applications can enforce the parse-and-process requirement by using parsers that will fail the parse step or by using parsers that will pass all keys to the application, and the application can perform the check for duplicate keys."

## §10. IANA Considerations

- (§10) "IANA has updated all COSE registries except for "COSE Header Parameters" and "COSE Key Common Parameters" to point to this document instead of [RFC8152]."

### §10.1. Changes to the "COSE Key Types" Registry

- (§10.1) "IANA has added a new column in the "COSE Key Types" registry.  The new column is labeled "Capabilities" and has been populated according to the entries in Table 22."

```text
            +=======+===========+============================+
            | Value | Name      | Capabilities               |
            +=======+===========+============================+
            | 1     | OKP       | [kty(1), crv]              |
            +-------+-----------+----------------------------+
            | 2     | EC2       | [kty(2), crv]              |
            +-------+-----------+----------------------------+
            | 3     | RSA       | [kty(3)]                   |
            +-------+-----------+----------------------------+
            | 4     | Symmetric | [kty(4)]                   |
            +-------+-----------+----------------------------+
            | 5     | HSS-LMS   | [kty(5), hash algorithm]   |
            +-------+-----------+----------------------------+
            | 6     | WalnutDSA | [kty(6), N value, q value] |
            +-------+-----------+----------------------------+

                     Table 22: Key Type Capabilities
```

### §10.2. Changes to the "COSE Algorithms" Registry

- (§10.2) "IANA has added a new column in the "COSE Algorithms" registry.  The new column is labeled "Capabilities" and has been populated with "[kty]" for all current, nonprovisional registrations."
- (§10.2) "IANA has updated the Reference column in the "COSE Algorithms" registry to include this document as a reference for all rows where it was not already present."
- (§10.2) "IANA has added a new row to the "COSE Algorithms" registry."
- (§10.2) "The Capabilities column for this registration is to be empty."

```text
    +===============+=======+===============+===========+=============+
    | Name          | Value | Description   | Reference | Recommended |
    +===============+=======+===============+===========+=============+
    | IV-GENERATION | 34    | For doing IV  | RFC 9053  | No          |
    |               |       | generation    |           |             |
    |               |       | for symmetric |           |             |
    |               |       | algorithms.   |           |             |
    +---------------+-------+---------------+-----------+-------------+

            Table 23: New entry in the COSE Algorithms registry
```

### §10.3. Changes to the "COSE Key Type Parameters" Registry

- (§10.3) "IANA has modified the description to "Public Key" for the line with "Key Type" of 1 and the "Name" of "x".  See Table 20, which has been modified with this change."

### §10.4. Expert Review Instructions

- (§10.4) "All of the IANA registries established by [RFC8152] are, at least in part, defined as Expert Review [RFC8126]."
- (§10.4) "Expert reviewers should take the following into consideration:"
- (§10.4) "Point squatting should be discouraged."
- (§10.4) "Specifications should exist for Specification Required ranges, but early assignment before an RFC is available is considered to be permissible."
- (§10.4) "When algorithms are registered, vanity registrations should be discouraged."
- (§10.4) "Algorithms are expected to meet the security requirements of the community and the requirements of the message structures in order to be suitable for registration."
- (§10.4) "Standards Track or BCP RFCs are required to register a code point in the Standards Action range."

## §11. Security Considerations

- (§11) "There are a number of security considerations that need to be taken into account by implementers of this specification.  The security considerations that are specific to an individual algorithm are placed next to the description of the algorithm."
- (§11) "Implementations need to protect the private key material for all individuals."
- (§11) "Use of the same key for two different algorithms can leak information about the key."
- (§11) "Several of the algorithms in this document have limits on the number of times that a key can be used without leaking information about the key."
- (§11) "It is therefore recommended that keys be restricted to a single algorithm."
- (§11) "Section 8.5 of [RFC9052] forbids combining "direct" recipient algorithms with other modes."
- (§11) "Key creators and key consumers are strongly encouraged to not only create new keys for each different algorithm, but to include that selection of algorithm in any distribution of key material and strictly enforce the matching of algorithms in the key structure to algorithms in the message structure."
- (§11) "Do not use an "EC2" key where an "OKP" key is expected."
- (§11) "Before using a key for transmission, or before acting on information received, a trust decision on a key needs to be made."
- (§11) "In all of these cases, there is no known requirement on the nonce being both unique and unpredictable; under these circumstances, it's reasonable to use a counter for creation of the nonce."
- (§11) "This specification does not provide a uniform method for providing padding as part of the message structure."
- (§11) "This means that it is up to the applications to document how content padding is to be done in order to prevent or discourage such analysis."
- (§11) "Under these circumstances, it may be that no one single entity will see all of the messages that are encrypted, and therefore no single entity can trigger the rekey operation."
- (§11) "In addition to checking that algorithms are correct, the key form needs to be checked as well."
