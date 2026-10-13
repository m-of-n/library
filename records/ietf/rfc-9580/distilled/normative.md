---
record: rfc-9580
kind: normative
title: "rfc-9580 — normative statements"
extracted: "2026-10-13"
reviewed_by: ""
---

<!-- FX-1 pass 1. Every normative statement and normative block of RFC 9580,
     VERBATIM, with its locator and source line range, in source order.
     Verbatim source only: no analysis, no paraphrase, no opinion. Blockquotes
     and fenced blocks delimit verbatim text; everything outside them is
     structure (headings, entry numbers, locators, line ranges, flags). -->

Source: RFC 9580, "OpenPGP", P. Wouters (Ed.), D. Huigens, J. Winter,
Y. Niibe, July 2024. Standards Track; obsoletes RFC 4880, 5581 and 6637.
9138 lines, sha256
`36540e57b63d24c0b17be0748b704bdeed3d643ce99a4fb1abb6469c1eb1ff18`.
The text has no page furniture (xml2rfc v3 plain text), so no entry needed a
page break removed.

## How to read this file

**Verbatim containers.** A **blockquote** (`>`) reproduces running prose: the
source's line breaks are kept, its leading three-space RFC indent is removed,
and no word, spelling or punctuation mark is altered, the source's own typos
included. A **fenced block** reproduces source lines byte-exactly,
indentation included: every packet field list, registry table, figure,
grammar, formula and code listing.

**Entries.** Each entry `N-nnn` is one contiguous run of source lines, and its
header gives the section and the source line range. No two non-adjacent
passages are spliced into one entry. An entry may start or end mid-line at a
sentence boundary. Every entry's content was located mechanically within its
stated range.

**Flags.** `_[lowercase/implied]_` marks an entry included because it binds
although it carries no capitalised BCP 14 keyword: a field or packet
definition, a lowercase must/should, a processing step. `_[table]_`,
`_[grammar]_` and `_[code]_` mark a registry or figure table, a grammar or
pseudo-code, and a formula or code listing. `_[IANA action]_` marks a §15
registry action or registration policy. `_[non-normative]_` marks text the
source itself labels non-normative or informational (Appendix B, Appendix C),
kept so the upgrade guidance and errata list are locatable. `_[test vector]_`
marks an Appendix A vector: its entry quotes the vector's descriptive prose
(or its heading where it has none) with the vector's full line range; the
bytes themselves are in `examples/`.

**Omissions.** Motivation, history, overview prose and the §16 references
are omitted, each with an italic note in place, so a reader can see what was
left out and why.

**BCP 14 census.** `bin/bcp14-count .cache/rfc-9580.txt --by-keyword`
returns 365 after the §1.1 RFC 2119 / RFC 8174 paragraph (N-001) is
stripped: MUST 126, MUST NOT 87, SHOULD 71, SHOULD NOT 24, MAY 46,
RECOMMENDED 7, REQUIRED 2, NOT RECOMMENDED 1, SHALL NOT 1.
`requirements.yaml` reconciles every keyword.

**Delegated to other artifacts.** The Appendix A test vectors are in
`examples/`, the §10 packet-sequence grammars also in `schema/`. Here each
gets an entry giving its line range, plus the normative prose around it.

## Front matter

_Lines 1–399 (title block, Abstract, Status of This Memo, Copyright Notice, Table of Contents) are omitted: document metadata and legal boilerplate. The lowercase "must include Revised BSD License text" at line 61 concerns code-component licensing, not the protocol._

## §1 Introduction

_Lines 402–414 (relationship to RFC 4880, RFC 2440, RFC 1991; obsoleted RFCs; pointer to Appendix B) are history and overview and are omitted._

### §1.1 Terms

**N-001** (§1.1) — source lines 418–422

> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
> "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
> "OPTIONAL" in this document are to be interpreted as described in
> BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
> capitals, as shown here.

**N-002** (§1.1) _[lowercase/implied]_ — source lines 424–426

> The key words "Private Use", "Specification Required", and "RFC
> Required" that appear in this document when used to describe
> namespace allocation are to be interpreted as described in [RFC8126].

_Lines 428–430 (terminology changes, pointer to Appendix B.1) are omitted: overview._

## §2 General Functions

_Lines 434–440 (scope overview) are omitted._

### §2.1 Confidentiality via Encryption

_Lines 444–483 (the six-step overview of public-key and symmetric encryption, and of sign-then-encrypt) are an overview of the encryption process, whose packets and processing are specified in §5; omitted._

### §2.2 Authentication via Digital Signature

_Lines 487–507 (the six-step overview of signing and verification) are an overview of the signing process, whose packets are specified in §5.2; omitted._

### §2.3 Compression

**N-003** (§2.3) — source lines 511–515

> An OpenPGP implementation MAY support the compression of data.  Many
> existing OpenPGP Messages are compressed.  Implementers, such as
> those working on constrained implementations that do not want to
> support compression, might want to consider at least implementing
> decompression.

### §2.4 Conversion to Base64

_Lines 519–527 (motivation for ASCII Armor, specified in §6) are omitted._

**N-004** (§2.4) — source line 529

> Implementations SHOULD support base64 conversions.

### §2.5 Signature-Only Applications

**N-005** (§2.5) _[lowercase/implied]_ — source lines 533–538

> OpenPGP is designed for applications that use both encryption and
> signatures, but there are a number of use cases that only require a
> signature-only implementation.  Although this specification requires
> both encryption and signatures, it is reasonable for there to be
> subset implementations that are non-conformant only in that they omit
> encryption support.

## §3 Data Element Formats

_Line 542 (section overview) is omitted._

### §3.1 Scalar Numbers

**N-006** (§3.1) _[lowercase/implied]_ — source lines 546–549

> Scalar numbers are unsigned and always stored in big-endian format.
> Using n[k] to refer to the kth octet being interpreted, the value of
> a 2-octet scalar is ((n[0] << 8) + n[1]).  The value of a 4-octet
> scalar is ((n[0] << 24) + (n[1] << 16) + (n[2] << 8) + n[3]).

### §3.2 Multiprecision Integers

**N-007** (§3.2) _[lowercase/implied]_ — source lines 553–561

> Multiprecision Integers (MPIs) are unsigned integers used to hold
> large integers such as the ones used in cryptographic calculations.
>
> An MPI consists of two pieces: a 2-octet scalar that is the length of
> the MPI in bits, followed by a string of octets that contain the
> actual integer.
>
> These octets form a big-endian number; a big-endian number can be
> made into an MPI by prefixing it with the appropriate length.

**N-008** (§3.2) _[lowercase/implied]_ — source lines 563–572

```
   Examples:

   (Note that all numbers in the octet strings identified by square
   brackets are in hexadecimal.)

      The string of octets [00 00] forms an MPI with the value 0.

      The string of octets [00 01 01] forms an MPI with the value 1.

      The string [00 09 01 FF] forms an MPI with the value 511.
```

**N-009** (§3.2) — source lines 574–586

```
   Additional rules:

   *  The size of an MPI is ((MPI.length + 7) / 8) + 2 octets.

   *  The length field of an MPI describes the length starting from its
      most significant non-zero bit.  Thus, the MPI [00 02 01] is not
      formed correctly.  It should be [00 01 01].  When parsing an MPI
      in a version 6 Key, Signature, or Public Key Encrypted Session Key
      (PKESK) packet, the implementation MUST check that the encoded
      length matches the length starting from the most significant non-
      zero bit; if it doesn't match, reject the packet as malformed.

   *  Unused bits of an MPI MUST be zero.
```

### §3.2.1 Using MPIs to Encode Other Data

**N-010** (§3.2.1) _[lowercase/implied]_ — source lines 590–596

> Note that in some places, MPIs are used to encode non-integer data,
> such as an elliptic curve (EC) point (see Section 11.2) or an octet
> string of known, fixed length (see Section 11.3).  The wire
> representation is the same: 2 octets of length in bits counted from
> the first non-zero bit, followed by the smallest series of octets
> that can represent the value while stripping off any leading zero
> octets.

### §3.3 Key IDs and Fingerprints

**N-011** (§3.3) — source lines 600–605

> A Key ID is an 8-octet scalar that identifies a key.  Implementations
> SHOULD NOT assume that Key IDs are unique.  A fingerprint is more
> likely to be unique than a Key ID.  The fingerprint and Key ID of a
> key are calculated differently according to the version of the key.
>
> Section 5.5.4 describes how Key IDs and Fingerprints are formed.

### §3.4 Text

**N-012** (§3.4) _[lowercase/implied]_ — source lines 609–610

> Unless otherwise specified, the character set for text is the UTF-8
> [RFC3629] encoding of Unicode [ISO10646].

### §3.5 Time Fields

**N-013** (§3.5) _[lowercase/implied]_ — source lines 614–615

> A time field is an unsigned 4-octet number containing the number of
> seconds elapsed since midnight, 1 January 1970 UTC.

### §3.6 Keyrings

_Lines 619–622 (a keyring is a collection of keys; details out of scope) are omitted: they state no requirement and place keyrings out of scope._

### §3.7 String-to-Key (S2K) Specifier

**N-014** (§3.7) _[lowercase/implied]_ — source lines 626–630

> A string-to-key (S2K) Specifier is used to convert a passphrase
> string into a symmetric key encryption/decryption key.  Passphrases
> requiring use of S2K conversion are currently used in two places: to
> encrypt the secret part of private keys and for symmetrically
> encrypted messages.

### §3.7.1 S2K Specifier Types

**N-015** (§3.7.1) _[lowercase/implied]_ _[table]_ — source lines 634–663

```
   There are four types of S2K Specifiers currently specified and some
   reserved values:

   +=========+==============+===============+==============+===========+
   |      ID | S2K Type     | S2K Field     | Generate?    | Reference |
   |         |              | Size          |              |           |
   |         |              | (Octets)      |              |           |
   +=========+==============+===============+==============+===========+
   |       0 | Simple S2K   | 2             | No           | Section   |
   |         |              |               |              | 3.7.1.1   |
   +---------+--------------+---------------+--------------+-----------+
   |       1 | Salted S2K   | 10            | Only when    | Section   |
   |         |              |               | string is    | 3.7.1.2   |
   |         |              |               | high entropy |           |
   +---------+--------------+---------------+--------------+-----------+
   |       2 | Reserved     | -             | No           |           |
   |         | value        |               |              |           |
   +---------+--------------+---------------+--------------+-----------+
   |       3 | Iterated and | 11            | Yes          | Section   |
   |         | Salted S2K   |               |              | 3.7.1.3   |
   +---------+--------------+---------------+--------------+-----------+
   |       4 | Argon2       | 20            | Yes          | Section   |
   |         |              |               |              | 3.7.1.4   |
   +---------+--------------+---------------+--------------+-----------+
   | 100-110 | Private or   | -             | As           |           |
   |         | Experimental |               | appropriate  |           |
   |         | Use          |               |              |           |
   +---------+--------------+---------------+--------------+-----------+

            Table 1: OpenPGP String-to-Key (S2K) Types Registry
```

**N-016** (§3.7.1) — source lines 665–668

> The S2K Specifier Types are described in the subsections below.  If
> "Yes" is not present in the "Generate?" column, the S2K entry is used
> only for reading in backward-compatibility mode and SHOULD NOT be
> used to generate new output.

### §3.7.1.1 Simple S2K

**N-017** (§3.7.1.1) _[lowercase/implied]_ — source lines 672–676

```
   Simple S2K directly hashes the string to produce the key data.  This
   hashing is done as shown below.

     Octet 0:        0x00
     Octet 1:        hash algorithm
```

**N-018** (§3.7.1.1) _[lowercase/implied]_ — source lines 678–697

> Simple S2K hashes the passphrase to produce the session key.  The
> manner in which this is done depends on the size of the session key
> (which depends on the cipher the session key will be used with) and
> the size of the hash algorithm's output.  If the hash size is greater
> than the session key size, the high-order (leftmost) octets of the
> hash are used as the key.
>
> If the hash size is less than the key size, multiple instances of the
> hash context are created -- enough to produce the required key data.
> These instances are preloaded with 0, 1, 2, ... octets of zeros (that
> is, the first instance has no preloading, the second gets preloaded
> with 1 octet of zero, the third is preloaded with 2 octets of zeros,
> and so forth).
>
> As the data is hashed, it is given independently to each hash
> context.  Since the contexts have been initialized differently, they
> will each produce a different hash output.  Once the passphrase is
> hashed, the output data from the multiple hashes is concatenated,
> first hash leftmost, to produce the key data, and any excess octets
> on the right are discarded.

### §3.7.1.2 Salted S2K

**N-019** (§3.7.1.2) _[lowercase/implied]_ — source lines 701–711

```
   Salted S2K includes a "salt" value in the S2K Specifier -- some
   arbitrary data -- that gets hashed along with the passphrase string
   to help prevent dictionary attacks.

     Octet 0:        0x01
     Octet 1:        hash algorithm
     Octets 2-9:     8-octet salt value

   Salted S2K is exactly like Simple S2K, except that the input to the
   hash function(s) consists of the 8 octets of salt from the S2K
   Specifier, followed by the passphrase.
```

### §3.7.1.3 Iterated and Salted S2K

**N-020** (§3.7.1.3) _[lowercase/implied]_ _[code]_ — source lines 715–731

```
   Iterated and Salted S2K includes both a salt and an octet count.  The
   salt is combined with the passphrase, and the resulting value is
   repeated and then hashed.  This further increases the amount of work
   an attacker must do to try dictionary attacks.

     Octet  0:        0x03
     Octet  1:        hash algorithm
     Octets 2-9:      8-octet salt value
     Octet  10:       count; a 1-octet coded value

   The count is coded into a 1-octet number using the following formula:

     #define EXPBIAS 6
         count = ((Int32)16 + (c & 15)) << ((c >> 4) + EXPBIAS);

   The above formula is described in [C99], where "Int32" is a type for
   a 32-bit integer, and the variable "c" is the coded count, octet 10.
```

**N-021** (§3.7.1.3) _[lowercase/implied]_ — source lines 733–749

> Iterated and Salted S2K hashes the passphrase and salt data multiple
> times.  The total number of octets to be hashed is specified in the
> encoded count in the S2K Specifier.  Note that the resulting count
> value is an octet count of how many octets will be hashed, not an
> iteration count.
>
> Initially, one or more hash contexts are set up the same as the other
> S2K algorithms, depending on how many octets of key data are needed.
> Then the salt, followed by the passphrase data, is repeatedly
> processed as input to each hash context until the number of octets
> specified by the octet count has been hashed.  The input is truncated
> to the octet count, except if the octet count is less than the
> initial size of the salt plus passphrase.  That is, at least one copy
> of the full salt plus passphrase will be provided as input to each
> hash context regardless of the octet count.  After the hashing is
> done, the key data is produced from the hash digest(s), which is the
> same way it is produced for the other S2K algorithms.

### §3.7.1.4 Argon2

**N-022** (§3.7.1.4) _[lowercase/implied]_ — source lines 753–762

```
   This S2K method hashes the passphrase using Argon2, as specified in
   [RFC9106].  This provides memory hardness, further protecting the
   passphrase against brute-force attacks.

     Octet  0:        0x04
     Octets 1-16:     16-octet salt value
     Octet  17:       1-octet number of passes t
     Octet  18:       1-octet degree of parallelism p
     Octet  19:       1-octet encoded_m, specifying the exponent of
                         the memory size
```

**N-023** (§3.7.1.4) — source lines 764–782

> The salt SHOULD be unique for each passphrase.
>
> The number of passes t and the degree of parallelism p MUST be non-
> zero.
>
> The memory size m is 2^(encoded_m) kibibytes (KiB) of RAM.  The
> encoded memory size MUST be a value from 3+ceil(log_2(p)) to 31, such
> that the decoded memory size m is a value from 8*p to 2^31.  Note
> that memory-hardness size is indicated in KiB, not octets.
>
> Argon2 is invoked with the passphrase as P, the salt as S, the values
> of t, p, and m as described above, the required key size as the tag
> length T, 0x13 as the version v, and Argon2id as the type.
>
> For the recommended values of t, p, and m, see Section 4 of
> [RFC9106].  If the recommended value of m for a given application is
> not a power of 2, it is RECOMMENDED to round up to the next power of
> 2 if the resulting performance would be acceptable; otherwise, round
> down (keeping in mind that m must be at least 8*p).

**N-024** (§3.7.1.4) _[lowercase/implied]_ — source lines 784–790

```
   As an example, with the first recommended option (t=1, p=4, m=2^21),
   the full S2K Specifier would be:

     04 XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX
     XX 01 04 15

   where XX represents a random octet of salt.
```

### §3.7.2 S2K Usage

**N-025** (§3.7.2) — source lines 794–807

> Simple S2K and Salted S2K Specifiers can be brute-forced when used
> with a low-entropy string, such as those typically provided by users.
> In addition, the usage of Simple S2K can lead to key and
> initialization vector (IV) reuse (see Section 5.3).  Therefore, when
> generating an S2K Specifier, an implementation MUST NOT use Simple
> S2K.  Furthermore, an implementation SHOULD NOT generate a Salted S2K
> unless the implementation knows that the input string is high entropy
> (for example, it generated the string itself using a known good
> source of randomness).
>
> It is RECOMMENDED that implementations use Argon2.  If Argon2 is not
> available, Iterated and Salted S2K MAY be used if care is taken to
> use a high octet count and a strong passphrase.  However, this method
> does not provide memory hardness, unlike Argon2.

### §3.7.2.1 Secret Key Encryption

**N-026** (§3.7.2.1) _[lowercase/implied]_ — source lines 811–834

> The first octet following the public key material in a Secret Key
> packet (Section 5.5.3) indicates whether and how the secret key
> material is passphrase protected.  This first octet is known as the
> "S2K usage octet".
>
> If the S2K usage octet is zero, the secret key data is unprotected.
> If it is non-zero, it describes how to use a passphrase to unlock the
> secret key.
>
> Implementations predating [RFC2440] indicated a protected key by
> storing a Symmetric Cipher Algorithm ID (see Section 9.3) in the S2K
> usage octet.  In this case, the MD5 hash function was always used to
> convert the passphrase to a key for the specified cipher algorithm.
>
> Later implementations indicate a protected secret key by storing one
> of the special values 253 (AEAD), 254 (CFB), or 255 (MalleableCFB) in
> the S2K usage octet.  The S2K usage octet is then followed
> immediately by a set of fields that describe how to convert a
> passphrase to a symmetric key that can unlock the secret material,
> plus other parameters relevant to the type of encryption used.
>
> The wire format fields also differ based on the version of the
> enclosing OpenPGP packet.  The table below, indexed by the S2K usage
> octet, summarizes the specifics described in Section 5.5.3.

**N-027** (§3.7.2.1) _[lowercase/implied]_ — source lines 836–839

> In the table below, check(x) means the "2-octet checksum", which is
> the sum of all octets in x mod 65536.  The info and packetprefix
> parameters are described in detail in Section 5.5.3.  Note that the
> "Generate?" column header has been shortened to "Gen?" here.

**N-028** (§3.7.2.1) _[lowercase/implied]_ _[table]_ — source lines 841–891

```
   +=========+============+============+==========================+====+
   |S2K Usage|Shorthand   |Encryption  |Encryption                |Gen?|
   |Octet    |            |Parameter   |                          |    |
   |         |            |Fields      |                          |    |
   +=========+============+============+==========================+====+
   |0        |Unprotected |-           |*v3 or v4 keys:*          |Yes |
   |         |            |            |[cleartext secrets ||     |    |
   |         |            |            |check(secrets)]           |    |
   |         |            |            |*v6 keys:* [cleartext     |    |
   |         |            |            |secrets]                  |    |
   +---------+------------+------------+--------------------------+----+
   |Known    |LegacyCFB   |IV          |CFB(MD5(passphrase),      |No  |
   |symmetric|            |            |secrets || check(secrets))|    |
   |cipher   |            |            |                          |    |
   |algo ID  |            |            |                          |    |
   |(see     |            |            |                          |    |
   |Section  |            |            |                          |    |
   |9.3)     |            |            |                          |    |
   +---------+------------+------------+--------------------------+----+
   |253      |AEAD        |params-     |AEAD(HKDF(S2K(passphrase),|Yes |
   |         |            |length      |info), secrets,           |    |
   |         |            |(*v6-only*),|packetprefix)             |    |
   |         |            |cipher-algo,|                          |    |
   |         |            |AEAD-mode,  |                          |    |
   |         |            |S2K-        |                          |    |
   |         |            |specifier-  |                          |    |
   |         |            |length      |                          |    |
   |         |            |(*v6-only*),|                          |    |
   |         |            |S2K-        |                          |    |
   |         |            |specifier,  |                          |    |
   |         |            |nonce       |                          |    |
   +---------+------------+------------+--------------------------+----+
   |254      |CFB         |params-     |CFB(S2K(passphrase),      |Yes |
   |         |            |length      |secrets || SHA1(secrets)) |    |
   |         |            |(*v6-only*),|                          |    |
   |         |            |cipher-algo,|                          |    |
   |         |            |S2K-        |                          |    |
   |         |            |specifier-  |                          |    |
   |         |            |length      |                          |    |
   |         |            |(*v6-only*),|                          |    |
   |         |            |S2K-        |                          |    |
   |         |            |specifier,  |                          |    |
   |         |            |IV          |                          |    |
   +---------+------------+------------+--------------------------+----+
   |255      |MalleableCFB|cipher-algo,|CFB(S2K(passphrase),      |No  |
   |         |            |S2K-        |secrets || check(secrets))|    |
   |         |            |specifier,  |                          |    |
   |         |            |IV          |                          |    |
   +---------+------------+------------+--------------------------+----+

     Table 2: OpenPGP Secret Key Encryption (S2K Usage Octet) Registry
```

**N-029** (§3.7.2.1) — source lines 893–907

> When emitting a secret key (with or without passphrase protection),
> an implementation MUST only produce data from a row with "Generate?"
> marked as "Yes".  Each row with "Generate?" marked as "No" is
> described for backward compatibility (for reading version 4 and
> earlier keys only) and MUST NOT be used to generate new output.
> Version 6 secret keys using these formats MUST be rejected.
>
> Note that compared to a version 4 secret key, the parameters of a
> passphrase-protected version 6 secret key are stored with an
> additional pair of length counts, each of which is 1 octet wide.
>
> Argon2 is only used with Authenticated Encryption with Associated
> Data (AEAD) (S2K usage octet 253).  An implementation MUST NOT create
> and MUST reject as malformed any Secret Key packet where the S2K
> usage octet is not AEAD (253) and the S2K Specifier Type is Argon2.

### §3.7.2.2 Symmetric Key Message Encryption

**N-030** (§3.7.2.2) — source lines 911–922

> OpenPGP can create a Symmetric Key Encrypted Session Key (SKESK)
> packet at the front of a message.  This is used to allow S2K
> Specifiers to be used for the passphrase conversion or to create
> messages with a mix of SKESK packets and PKESK packets.  This allows
> a message to be decrypted with either a passphrase or a public key
> pair.
>
> Implementations predating [RFC2440] always used the International
> Data Encryption Algorithm (IDEA) with Simple S2K conversion when
> encrypting a message with a symmetric algorithm; see Section 5.7.
> IDEA MUST NOT be generated but MAY be consumed for backward
> compatibility.

## §4 Packet Syntax

_Line 926 (section overview) is omitted._

### §4.1 Overview

**N-031** (§4.1) _[lowercase/implied]_ — source lines 930–939

> An OpenPGP Message is constructed from a number of records that are
> typically called packets.  A packet is a chunk of data that has a
> Type ID specifying its meaning.  An OpenPGP Message, keyring,
> certificate, detached signature, and so forth consists of a number of
> packets.  Some of those packets may contain other OpenPGP packets
> (for example, a compressed data packet, when uncompressed, contains
> OpenPGP packets).
>
> Each packet consists of a packet header, followed by the packet body.
> The packet header is of variable length.

**N-032** (§4.1) — source lines 941–955

> When handling a stream of packets, the length information in each
> packet header is the canonical source of packet boundaries.  An
> implementation handling a packet stream that wants to find the next
> packet MUST look for it at the precise offset indicated in the
> previous packet header.
>
> Additionally, some packets contain internal length indicators (for
> example, a subfield within the packet).  In the event that a subfield
> length indicator within a packet implies inclusion of octets outside
> the range indicated in the packet header, a parser MUST abort without
> writing outside the indicated range and MUST treat the packet as
> malformed and unusable.
>
> An implementation MUST NOT interpret octets outside the range
> indicated in the packet header as part of the contents of the packet.

### §4.2 Packet Headers

**N-033** (§4.2) _[lowercase/implied]_ — source lines 959–970

> The first octet of the packet denotes the format of the rest of the
> header, and it encodes the Packet Type ID, indicating the type of the
> packet (see Section 5).  The remainder of the packet header is the
> length of the packet.
>
> There are two packet formats: 1) the (current) OpenPGP packet format
> specified by this document and its predecessors [RFC4880] and
> [RFC2440] and 2) the Legacy packet format as used by implementations
> predating any IETF specification of OpenPGP.
>
> Note that the most significant bit is the leftmost bit, called "bit
> 7".  A mask for this bit is 0x80 in hexadecimal.

**N-034** (§4.2) _[lowercase/implied]_ _[table]_ — source lines 972–984

```
                             +---------------+
     Encoded Packet Type ID: |7 6 5 4 3 2 1 0|
                             +---------------+
     OpenPGP format:
       Bit 7 -- always one
       Bit 6 -- always one
       Bits 5 to 0 -- Packet Type ID

     Legacy format:
       Bit 7 -- always one
       Bit 6 -- always zero
       Bits 5 to 2 -- Packet Type ID
       Bits 1 to 0 -- length-type
```

**N-035** (§4.2) — source lines 986–1003

> Bit 6 of the first octet of the packet header indicates whether the
> packet is encoded in the OpenPGP or Legacy packet format.  The Legacy
> packet format MAY be used when consuming packets to facilitate
> interoperability and accessing archived data.  The Legacy packet
> format SHOULD NOT be used to generate new data, unless the recipient
> is known to only support the Legacy packet format.  This latter case
> is extremely unlikely, as the Legacy packet format was obsoleted by
> [RFC2440] in 1998.
>
> An implementation that consumes and redistributes pre-existing
> OpenPGP data (such as Transferable Public Keys) may encounter packets
> framed with the Legacy packet format.  Such an implementation MAY
> either redistribute these packets in their Legacy format or transform
> them to the current OpenPGP packet format before redistribution.
>
> Note that Legacy format headers only have 4 bits for the Packet Type
> ID and hence can only encode Packet Type IDs less than 16, whereas
> the OpenPGP format headers can encode IDs as great as 63.

### §4.2.1 OpenPGP Format Packet Lengths

**N-036** (§4.2.1) _[lowercase/implied]_ — source lines 1007–1021

```
   OpenPGP format packets have four possible ways of encoding length:

   1.  A 1-octet Body Length header encodes packet lengths of up to 191
       octets.

   2.  A 2-octet Body Length header encodes packet lengths of 192 to
       8383 octets.

   3.  A 5-octet Body Length header encodes packet lengths of up to
       4,294,967,295 (0xFFFFFFFF) octets in length.  (This actually
       encodes a 4-octet scalar number.)

   4.  When the length of the packet body is not known in advance by the
       issuer, Partial Body Length headers encode a packet of
       indeterminate length, effectively making it a stream.
```

### §4.2.1.1 1-Octet Lengths

**N-037** (§4.2.1.1) _[lowercase/implied]_ _[code]_ — source lines 1025–1029

```
   A 1-octet Body Length header encodes a length of 0 to 191 octets.
   This type of length header is recognized because the 1-octet value is
   less than 192.  The body length is equal to:

     bodyLen = 1st_octet;
```

### §4.2.1.2 2-Octet Lengths

**N-038** (§4.2.1.2) _[lowercase/implied]_ _[code]_ — source lines 1033–1037

```
   A 2-octet Body Length header encodes a length of 192 to 8383 octets.
   It is recognized because its first octet is in the range 192 to 223.
   The body length is equal to:

     bodyLen = ((1st_octet - 192) << 8) + (2nd_octet) + 192
```

### §4.2.1.3 5-Octet Lengths

**N-039** (§4.2.1.3) _[lowercase/implied]_ _[code]_ — source lines 1041–1049

```
   A 5-octet Body Length header consists of a single octet holding the
   value 255, followed by a 4-octet scalar.  The body length is equal
   to:

     bodyLen = (2nd_octet << 24) | (3rd_octet << 16) |
               (4th_octet << 8)  | 5th_octet

   This basic set of 1-octet, 2-octet, and 5-octet lengths is also used
   internally to some packets.
```

### §4.2.1.4 Partial Body Lengths

**N-040** (§4.2.1.4) _[lowercase/implied]_ _[code]_ — source lines 1053–1059

```
   A Partial Body Length header is 1 octet long and encodes the length
   of only part of the data packet.  This length is a power of 2, from 1
   to 1,073,741,824 (2 to the 30th power).  It is recognized by its
   1-octet value that is greater than or equal to 224, and less than
   255.  The Partial Body Length is equal to:

     partialBodyLen = 1 << (1st_octet & 0x1F);
```

**N-041** (§4.2.1.4) — source lines 1061–1074

> Each Partial Body Length header is followed by a portion of the
> packet body data; the Partial Body Length header specifies this
> portion's length.  Another length header (1-octet, 2-octet, 5-octet,
> or partial) follows that portion.  The last length header in the
> packet MUST NOT be a Partial Body Length header.  Partial Body Length
> headers may only be used for the non-final parts of the packet.
>
> Note also that the last Body Length header can be a zero-length
> header.
>
> An implementation MAY use Partial Body Lengths for data packets,
> whether they are literal, compressed, or encrypted.  The first
> partial length MUST be at least 512 octets long.  Partial Body
> Lengths MUST NOT be used for any other packet types.

### §4.2.2 Legacy Format Packet Lengths

**N-042** (§4.2.2) — source lines 1078–1098

```
   A zero in bit 6 of the first octet of the packet indicates a Legacy
   packet format.  Bits 1 and 0 of the first octet of a Legacy packet
   are the "length-type" field.  The meaning of length-type in Legacy
   format packets is as follows:

   0  The packet has a 1-octet length.  The header is 2 octets long.

   1  The packet has a 2-octet length.  The header is 3 octets long.

   2  The packet has a 4-octet length.  The header is 5 octets long.

   3  The packet is of indeterminate length.  The header is 1 octet
      long, and the implementation must determine how long the packet
      is.  If the packet is in a file, it means that the packet extends
      until the end of the file.  The OpenPGP format headers have a
      mechanism for precisely encoding data of indeterminate length.  An
      implementation MUST NOT generate a Legacy format packet with
      indeterminate length.  An implementation MAY interpret an
      indeterminate length Legacy format packet in order to deal with
      historic data or data generated by a legacy system that predates
      support for [RFC2440].
```

### §4.2.3 Packet Length Examples

**N-043** (§4.2.3) _[lowercase/implied]_ — source lines 1102–1133

```
   These examples show ways that OpenPGP format packets might encode the
   packet body lengths.

   *  A packet body with length 100 may have its length encoded in one
      octet: 0x64.  This is followed by 100 octets of data.

   *  A packet body with length 1723 may have its length encoded in two
      octets: 0xC5, 0xFB.  This header is followed by the 1723 octets of
      data.

   *  A packet body with length 100000 may have its length encoded in
      five octets: 0xFF, 0x00, 0x01, 0x86, 0xA0.

   It might also be encoded in the following octet stream:

   *  0xEF, first 32768 octets of data;

   *  0xE1, next 2 octets of data;

   *  0xE0, next 1 octet of data;

   *  0xF0, next 65536 octets of data; and

   *  0xC5, 0xDD, last 1693 octets of data.

   This is just one possible encoding, and many variations are possible
   on the size of the Partial Body Length headers, as long as a regular
   Body Length header encodes the last portion of the data.

   Please note that in all of these explanations, the total length of
   the packet is the length of the header(s) plus the length of the
   body.
```

### §4.3 Packet Criticality

**N-044** (§4.3) — source lines 1137–1144

> The Packet Type ID space is partitioned into critical packets and
> non-critical packets.  If an implementation encounters a critical
> packet where the packet type is unknown in a packet sequence, it MUST
> reject the whole packet sequence (see Section 10).  On the other
> hand, an unknown non-critical packet MUST be ignored.
>
> Packets with Type IDs from 0 to 39 are critical.  Packets with Type
> IDs from 40 to 63 are non-critical.

## §5 Packet Types

**N-045** (§5) _[table]_ — source lines 1148–1231

```
   The defined packet types are as follows:

    +=======+==========+=====================+===========+===========+
    |    ID | Critical | Packet Type         | Shorthand | Reference |
    |       |          | Description         |           |           |
    +=======+==========+=====================+===========+===========+
    |     0 | Yes      | Reserved - this     |           |           |
    |       |          | Packet Type ID MUST |           |           |
    |       |          | NOT be used         |           |           |
    +-------+----------+---------------------+-----------+-----------+
    |     1 | Yes      | Public Key          | PKESK     | Section   |
    |       |          | Encrypted Session   |           | 5.1       |
    |       |          | Key Packet          |           |           |
    +-------+----------+---------------------+-----------+-----------+
    |     2 | Yes      | Signature Packet    | SIG       | Section   |
    |       |          |                     |           | 5.2       |
    +-------+----------+---------------------+-----------+-----------+
    |     3 | Yes      | Symmetric Key       | SKESK     | Section   |
    |       |          | Encrypted Session   |           | 5.3       |
    |       |          | Key Packet          |           |           |
    +-------+----------+---------------------+-----------+-----------+
    |     4 | Yes      | One-Pass Signature  | OPS       | Section   |
    |       |          | Packet              |           | 5.4       |
    +-------+----------+---------------------+-----------+-----------+
    |     5 | Yes      | Secret Key Packet   | SECKEY    | Section   |
    |       |          |                     |           | 5.5.1.3   |
    +-------+----------+---------------------+-----------+-----------+
    |     6 | Yes      | Public Key Packet   | PUBKEY    | Section   |
    |       |          |                     |           | 5.5.1.1   |
    +-------+----------+---------------------+-----------+-----------+
    |     7 | Yes      | Secret Subkey       | SECSUBKEY | Section   |
    |       |          | Packet              |           | 5.5.1.4   |
    +-------+----------+---------------------+-----------+-----------+
    |     8 | Yes      | Compressed Data     | COMP      | Section   |
    |       |          | Packet              |           | 5.6       |
    +-------+----------+---------------------+-----------+-----------+
    |     9 | Yes      | Symmetrically       | SED       | Section   |
    |       |          | Encrypted Data      |           | 5.7       |
    |       |          | Packet              |           |           |
    +-------+----------+---------------------+-----------+-----------+
    |    10 | Yes      | Marker Packet       | MARKER    | Section   |
    |       |          |                     |           | 5.8       |
    +-------+----------+---------------------+-----------+-----------+
    |    11 | Yes      | Literal Data Packet | LIT       | Section   |
    |       |          |                     |           | 5.9       |
    +-------+----------+---------------------+-----------+-----------+
    |    12 | Yes      | Trust Packet        | TRUST     | Section   |
    |       |          |                     |           | 5.10      |
    +-------+----------+---------------------+-----------+-----------+
    |    13 | Yes      | User ID Packet      | UID       | Section   |
    |       |          |                     |           | 5.11      |
    +-------+----------+---------------------+-----------+-----------+
    |    14 | Yes      | Public Subkey       | PUBSUBKEY | Section   |
    |       |          | Packet              |           | 5.5.1.2   |
    +-------+----------+---------------------+-----------+-----------+
    |    17 | Yes      | User Attribute      | UAT       | Section   |
    |       |          | Packet              |           | 5.12      |
    +-------+----------+---------------------+-----------+-----------+
    |    18 | Yes      | Symmetrically       | SEIPD     | Section   |
    |       |          | Encrypted and       |           | 5.13      |
    |       |          | Integrity Protected |           |           |
    |       |          | Data Packet         |           |           |
    +-------+----------+---------------------+-----------+-----------+
    |    19 | Yes      | Reserved (formerly  |           | Section   |
    |       |          | Modification        |           | 5.13.1    |
    |       |          | Detection Code      |           |           |
    |       |          | Packet)             |           |           |
    +-------+----------+---------------------+-----------+-----------+
    |    20 | Yes      | Reserved            |           |           |
    +-------+----------+---------------------+-----------+-----------+
    |    21 | Yes      | Padding Packet      | PADDING   | Section   |
    |       |          |                     |           | 5.14      |
    +-------+----------+---------------------+-----------+-----------+
    | 22-39 | Yes      | Unassigned Critical |           |           |
    |       |          | Packets             |           |           |
    +-------+----------+---------------------+-----------+-----------+
    | 40-59 | No       | Unassigned Non-     |           |           |
    |       |          | Critical Packets    |           |           |
    +-------+----------+---------------------+-----------+-----------+
    | 60-63 | No       | Private or          |           |           |
    |       |          | Experimental Use    |           |           |
    +-------+----------+---------------------+-----------+-----------+

                  Table 3: OpenPGP Packet Types Registry
```

**N-046** (§5) _[lowercase/implied]_ — source lines 1233–1236

> The labels in the "Shorthand" column are used for compact reference
> elsewhere in this document, and they may also be used by
> implementations that provide debugging or inspection affordances for
> streams of OpenPGP packets.

### §5.1 Public Key Encrypted Session Key Packet (Type ID 1)

**N-047** (§5.1) _[lowercase/implied]_ — source lines 1240–1250

> Zero or more PKESK packets and/or SKESK packets (Section 5.3) precede
> an encryption container (that is, a Symmetrically Encrypted and
> Integrity Protected Data (SEIPD) packet or -- for historic data -- a
> Symmetrically Encrypted Data (SED) packet), which holds an Encrypted
> Message.  The message is encrypted with the session key, and the
> session key is itself encrypted and stored in the Encrypted Session
> Key packet(s).  The encryption container is preceded by one Public
> Key Encrypted Session Key packet for each OpenPGP Key to which the
> message is encrypted.  The recipient of the message finds a session
> key that is encrypted to their public key, decrypts the session key,
> and then uses the session key to decrypt the message.

**N-048** (§5.1) _[lowercase/implied]_ — source lines 1252–1260

> The body of this packet starts with a 1-octet number giving the
> version number of the packet type.  The currently defined versions
> are 3 and 6.  The remainder of the packet depends on the version.
>
> The versions differ in how they identify the recipient key and in
> what they encode.  The version of the PKESK packet must align with
> the version of the SEIPD packet (see Section 10.3.2.1).  Any new
> version of the PKESK packet should be registered in the registry
> established in Section 10.3.2.1.

### §5.1.1 Version 3 Public Key Encrypted Session Key Packet Format

**N-049** (§5.1.1) — source lines 1264–1267

> A version 3 PKESK packet precedes a v1 SEIPD packet (see
> Section 5.13.1).  In historic data, it is sometimes found preceding a
> deprecated SED packet; see Section 5.7.  A v3 PKESK packet MUST NOT
> precede a v2 SEIPD packet (see Section 10.3.2.1).

**N-050** (§5.1.1) _[lowercase/implied]_ — source lines 1269–1291

```
   The v3 PKESK packet consists of:

   *  A 1-octet version number with value 3.

   *  An 8-octet number that gives the Key ID of the public key to which
      the session key is encrypted.  If the session key is encrypted to
      a subkey, then the Key ID of this subkey is used here instead of
      the Key ID of the primary key.  The Key ID may also be all zeros,
      for an "anonymous recipient" (see Section 5.1.8).

   *  A 1-octet number giving the public key algorithm used.

   *  A series of values comprising the encrypted session key.  This is
      algorithm specific and described below.

   The public key encryption algorithm (described in subsequent
   sections) is passed two values:

   *  The session key.

   *  The 1-octet algorithm identifier that specifies the symmetric key
      encryption algorithm used to encrypt the v1 SEIPD packet described
      in the following section.
```

### §5.1.2 Version 6 Public Key Encrypted Session Key Packet Format

**N-051** (§5.1.2) — source lines 1295–1297

> A v6 PKESK packet precedes a v2 SEIPD packet (see Section 5.13.2).  A
> v6 PKESK packet MUST NOT precede a v1 SEIPD packet or a deprecated
> SED packet (see Section 10.3.2.1).

**N-052** (§5.1.2) _[lowercase/implied]_ — source lines 1299–1316

```
   The v6 PKESK packet consists of the following fields:

   *  A 1-octet version number with value 6.

   *  A 1-octet size of the following two fields.  This size may be
      zero, if the key version number field and the fingerprint field
      are omitted for an "anonymous recipient" (see Section 5.1.8).

   *  A 1-octet key version number.

   *  The fingerprint of the public key or subkey to which the session
      key is encrypted.  Note that the length N of the fingerprint for a
      version 4 key is 20 octets; for a version 6 key, N is 32.

   *  A 1-octet number giving the public key algorithm used.

   *  A series of values comprising the encrypted session key.  This is
      algorithm specific and described below.
```

**N-053** (§5.1.2) _[lowercase/implied]_ — source lines 1318–1321

> The session key is encrypted according to the public key algorithm
> used, as described below.  No symmetric key encryption algorithm
> identifier is passed to the public key algorithm for a v6 PKESK
> packet, as it is included in the v2 SEIPD packet.

### §5.1.3 Algorithm-Specific Fields for RSA Encryption

**N-054** (§5.1.3) _[lowercase/implied]_ — source lines 1325–1336

```
   *  MPI of RSA-encrypted value m^e mod n.

   To produce the value "m" in the above formula, first concatenate the
   following values:

   *  The 1-octet algorithm identifier, if it was passed (in the case of
      a v3 PKESK packet).

   *  The session key.

   *  A 2-octet checksum of the session key, equal to the sum of the
      session key octets, modulo 65536.
```

**N-055** (§5.1.3) _[lowercase/implied]_ — source lines 1338–1342

> Then, the above values are encoded using the PKCS#1 block encoding
> EME-PKCS1-v1_5, as described in Step 2 in Section 7.2.1 of [RFC8017]
> (see also Section 12.1.1).  When decoding "m" during decryption, an
> implementation should follow Step 3 in Section 7.2.2 of [RFC8017]
> (see also Section 12.1.2).

**N-056** (§5.1.3) — source lines 1344–1347

> Note that when an implementation forms several PKESK packets with one
> session key, forming a message that can be decrypted by several keys,
> the implementation MUST make a new PKCS#1 encoding for each key.
> This defends against attacks such as those discussed in [HASTAD].

### §5.1.4 Algorithm-Specific Fields for Elgamal Encryption

**N-057** (§5.1.4) _[lowercase/implied]_ — source lines 1351–1364

```
   *  MPI of Elgamal (Diffie-Hellman) value g^k mod p.

   *  MPI of Elgamal (Diffie-Hellman) value m * y^k mod p.

   To produce the value "m" in the above formula, first concatenate the
   following values:

   *  The 1-octet algorithm identifier, if it was passed (in the case of
      a v3 PKESK packet).

   *  The session key.

   *  A 2-octet checksum of the session key, equal to the sum of the
      session key octets, modulo 65536.
```

**N-058** (§5.1.4) _[lowercase/implied]_ — source lines 1366–1370

> Then, the above values are encoded using the PKCS#1 block encoding
> EME-PKCS1-v1_5, as described in Step 2 in Section 7.2.1 of [RFC8017]
> (see also Section 12.1.1).  When decoding "m" during decryption, an
> implementation should follow Step 3 in Section 7.2.2 of [RFC8017]
> (see also Section 12.1.2).

**N-059** (§5.1.4) — source lines 1372–1375

> Note that when an implementation forms several PKESK packets with one
> session key, forming a message that can be decrypted by several keys,
> the implementation MUST make a new PKCS#1 encoding for each key.
> This defends against attacks such as those discussed in [HASTAD].

**N-060** (§5.1.4) — source line 1377

> An implementation MUST NOT generate ElGamal v6 PKESK packets.

### §5.1.5 Algorithm-Specific Fields for ECDH Encryption

**N-061** (§5.1.5) _[lowercase/implied]_ — source lines 1381–1386

```
   *  MPI of an EC point representing an ephemeral public key in the
      point format associated with the curve as specified in
      Section 9.2.

   *  A 1-octet size, followed by a symmetric key encoded using the
      method described in Section 11.5.
```

### §5.1.6 Algorithm-Specific Fields for X25519 Encryption

**N-062** (§5.1.6) _[lowercase/implied]_ — source lines 1390–1397

```
   *  32 octets representing an ephemeral X25519 public key.

   *  A 1-octet size of the following fields.

   *  The 1-octet algorithm identifier, if it was passed (in the case of
      a v3 PKESK packet).

   *  The encrypted session key.
```

**N-063** (§5.1.6) _[lowercase/implied]_ — source lines 1399–1412

```
   See Section 6.1 of [RFC7748] for more details on the computation of
   the ephemeral public key and the shared secret.  The HMAC-based Key
   Derivation Function (HKDF) [RFC5869] is then used with SHA256
   [RFC6234] and an info parameter of "OpenPGP X25519" and no salt.  The
   input of HKDF is the concatenation of the following three values:

   *  32 octets of the ephemeral X25519 public key from this packet.

   *  32 octets of the recipient public key material.

   *  32 octets of the shared secret.

   The key produced from HKDF is used to encrypt the session key with
   AES-128 key wrap, as defined in [RFC3394].
```

**N-064** (§5.1.6) — source lines 1414–1420

> Note that unlike Elliptic Curve Diffie-Hellman (ECDH), no checksum or
> padding are appended to the session key before key wrapping.
> Finally, note that unlike the other public key algorithms, in the
> case of a v3 PKESK packet, the symmetric algorithm ID is not
> encrypted.  Instead, it is prepended to the encrypted session key in
> plaintext.  In this case, the symmetric algorithm used MUST be AES-
> 128, AES-192, or AES-256 (algorithm IDs 7, 8, or 9, respectively).

### §5.1.7 Algorithm-Specific Fields for X448 Encryption

**N-065** (§5.1.7) _[lowercase/implied]_ — source lines 1424–1431

```
   *  56 octets representing an ephemeral X448 public key.

   *  A 1-octet size of the following fields.

   *  The 1-octet algorithm identifier, if it was passed (in the case of
      a v3 PKESK packet).

   *  The encrypted session key.
```

**N-066** (§5.1.7) _[lowercase/implied]_ — source lines 1433–1446

```
   See Section 6.2 of [RFC7748] for more details on the computation of
   the ephemeral public key and the shared secret.  HKDF [RFC5869] is
   then used with SHA512 [RFC6234] and an info parameter of "OpenPGP
   X448" and no salt.  The input of HKDF is the concatenation of the
   following three values:

   *  56 octets of the ephemeral X448 public key from this packet.

   *  56 octets of the recipient public key material.

   *  56 octets of the shared secret.

   The key produced from HKDF is used to encrypt the session key with
   AES-256 key wrap, as defined in [RFC3394].
```

**N-067** (§5.1.7) — source lines 1448–1454

> Note that unlike ECDH, no checksum or padding are appended to the
> session key before key wrapping.  Finally, note that unlike the other
> public key algorithms, in the case of a v3 PKESK packet, the
> symmetric algorithm ID is not encrypted.  Instead, it is prepended to
> the encrypted session key in plaintext.  In this case, the symmetric
> algorithm used MUST be AES-128, AES-192, or AES-256 (algorithm ID 7,
> 8, or 9).

### §5.1.8 Notes on PKESK

**N-068** (§5.1.8) — source lines 1458–1462

> An implementation MAY accept or use a Key ID of all zeros, or an
> omitted key fingerprint, to hide the intended decryption key.  In
> this case, the receiving implementation would try all available
> private keys, checking for a valid decrypted session key.  This
> format helps reduce traffic analysis of messages.

## §5.2 Signature Packet (Type ID 2)

_The opening paragraph (a Signature packet describes a binding between some public key and some data; the most common signatures) is overview and is omitted._

**N-069** (§5.2) _[lowercase/implied]_ — source lines 1470–1477

> Three versions of Signature packets are defined.  Version 3 provides
> basic signature information, while versions 4 and 6 provide an
> expandable format with subpackets that can specify more information
> about the signature.
>
> For historical reasons, versions 1, 2, and 5 of the Signature packet
> are unspecified.  Any new Signature packet version should be
> registered in the registry established in Section 10.3.2.2.

**N-070** (§5.2) — source lines 1479–1484

> An implementation MUST generate a version 6 signature when signing
> with a version 6 key.  An implementation MUST generate a version 4
> signature when signing with a version 4 key.  Implementations MUST
> NOT create version 3 signatures; they MAY accept version 3
> signatures.  See Section 10.3.2.2 for more details about packet
> version correspondence between keys and signatures.

### §5.2.1 Signature Types

_The paragraph on the deliberate vagueness of signature meanings (lines 1488–1495) is motivation and is omitted._

**N-071** (§5.2.1) _[table]_ — source lines 1497–1533

```
     +======+====================================+==================+
     | ID   | Name                               | Reference        |
     +======+====================================+==================+
     | 0x00 | Binary Signature                   | Section 5.2.1.1  |
     +------+------------------------------------+------------------+
     | 0x01 | Text Signature                     | Section 5.2.1.2  |
     +------+------------------------------------+------------------+
     | 0x02 | Standalone Signature               | Section 5.2.1.3  |
     +------+------------------------------------+------------------+
     | 0x10 | Generic Certification Signature    | Section 5.2.1.4  |
     +------+------------------------------------+------------------+
     | 0x11 | Persona Certification Signature    | Section 5.2.1.5  |
     +------+------------------------------------+------------------+
     | 0x12 | Casual Certification Signature     | Section 5.2.1.6  |
     +------+------------------------------------+------------------+
     | 0x13 | Positive Certification Signature   | Section 5.2.1.7  |
     +------+------------------------------------+------------------+
     | 0x18 | Subkey Binding Signature           | Section 5.2.1.8  |
     +------+------------------------------------+------------------+
     | 0x19 | Primary Key Binding Signature      | Section 5.2.1.9  |
     +------+------------------------------------+------------------+
     | 0x1F | Direct Key Signature               | Section 5.2.1.10 |
     +------+------------------------------------+------------------+
     | 0x20 | Key Revocation Signature           | Section 5.2.1.11 |
     +------+------------------------------------+------------------+
     | 0x28 | Subkey Revocation Signature        | Section 5.2.1.12 |
     +------+------------------------------------+------------------+
     | 0x30 | Certification Revocation Signature | Section 5.2.1.13 |
     +------+------------------------------------+------------------+
     | 0x40 | Timestamp Signature                | Section 5.2.1.14 |
     +------+------------------------------------+------------------+
     | 0x50 | Third-Party Confirmation Signature | Section 5.2.1.15 |
     +------+------------------------------------+------------------+
     | 0xFF | Reserved                           | Section 5.2.1.16 |
     +------+------------------------------------+------------------+

                Table 4: OpenPGP Signature Types Registry
```

_The sentence introducing the subsections (lines 1535–1536) is structure and is omitted._

### §5.2.1.1 Binary Signature (Type ID 0x00) of a Document

**N-072** (§5.2.1.1) _[lowercase/implied]_ — source lines 1540–1541

> This means the signer owns it, created it, or certifies that it has
> not been modified.

### §5.2.1.2 Text Signature (Type ID 0x01) of a Canonical Document

**N-073** (§5.2.1.2) _[lowercase/implied]_ — source lines 1545–1547

> This means the signer owns it, created it, or certifies that it has
> not been modified.  The signature is calculated over the text data
> with its line endings converted to <CR><LF>.

### §5.2.1.3 Standalone Signature (Type ID 0x02)

**N-074** (§5.2.1.3) — source lines 1551–1554

> This signature is a signature of only its own subpacket contents.  It
> is calculated identically to a signature over a zero-length binary
> document.  Version 3 Standalone signatures MUST NOT be generated and
> MUST be ignored.

### §5.2.1.4 Generic Certification Signature (Type ID 0x10) of a User ID and Public Key Packet

**N-075** (§5.2.1.4) _[lowercase/implied]_ — source lines 1559–1561

> The issuer of this certification does not make any particular
> assertion as to how well the certifier has checked that the owner of
> the key is in fact the person described by the User ID.

### §5.2.1.5 Persona Certification Signature (Type ID 0x11) of a User ID and Public Key Packet

**N-076** (§5.2.1.5) _[lowercase/implied]_ — source lines 1566–1567

> The issuer of this certification has not done any verification of the
> claim that the owner of this key is the User ID specified.

### §5.2.1.6 Casual Certification Signature (Type ID 0x12) of a User ID and Public Key Packet

**N-077** (§5.2.1.6) _[lowercase/implied]_ — source lines 1572–1573

> The issuer of this certification has done some casual verification of
> the claim of identity.

### §5.2.1.7 Positive Certification Signature (Type ID 0x13) of a User ID and Public Key Packet

**N-078** (§5.2.1.7) _[lowercase/implied]_ — source lines 1578–1579

> The issuer of this certification has done substantial verification of
> the claim of identity.

_The note on how implementations use 0x10 versus 0x11–0x13 in practice (lines 1581–1583) is descriptive and is omitted._

### §5.2.1.8 Subkey Binding Signature (Type ID 0x18)

**N-079** (§5.2.1.8) — source lines 1587–1593

> This signature is a statement by the top-level signing key,
> indicating that it owns the subkey.  This signature is calculated
> directly on the primary key and subkey, and not on any User ID or
> other packets.  A signature that binds a signing subkey MUST have an
> Embedded Signature subpacket in this binding signature that contains
> a 0x19 signature made by the signing subkey on the primary key and
> subkey.

### §5.2.1.9 Primary Key Binding Signature (Type ID 0x19)

**N-080** (§5.2.1.9) _[lowercase/implied]_ — source lines 1597–1600

> This signature is a statement by a signing subkey, indicating that it
> is owned by the primary key.  This signature is calculated the same
> way as a Subkey Binding signature (Type ID 0x18): directly on the
> primary key and subkey, and not on any User ID or other packets.

### §5.2.1.10 Direct Key Signature (Type ID 0x1F)

**N-081** (§5.2.1.10) _[lowercase/implied]_ — source lines 1604–1610

> This signature is calculated directly on a key.  It binds the
> information in the Signature subpackets to the key and is appropriate
> to be used for subpackets that provide information about the key,
> such as the Key Flags subpacket or the (deprecated) Revocation Key
> subpacket.  It is also appropriate for statements that non-self
> certifiers want to make about the key itself rather than the binding
> between a key and a name.

### §5.2.1.11 Key Revocation Signature (Type ID 0x20)

**N-082** (§5.2.1.11) _[lowercase/implied]_ — source lines 1614–1617

> This signature is calculated directly on the key being revoked.  A
> revoked key is not to be used.  Only Revocation Signatures by the key
> being revoked, or by a (deprecated) Revocation Key, should be
> considered valid Revocation Signatures.

### §5.2.1.12 Subkey Revocation Signature (Type ID 0x28)

**N-083** (§5.2.1.12) _[lowercase/implied]_ — source lines 1621–1625

> This signature is calculated directly on the primary key and the
> subkey being revoked.  A revoked subkey is not to be used.  Only
> Revocation Signatures by the top-level signature key that is bound to
> this subkey, or by a (deprecated) Revocation Key, should be
> considered valid Revocation Signatures.

### §5.2.1.13 Certification Revocation Signature (Type ID 0x30)

**N-084** (§5.2.1.13) _[lowercase/implied]_ — source lines 1629–1634

> This signature revokes an earlier User ID certification signature
> (Type IDs 0x10 through 0x13) or Direct Key signature (Type ID 0x1F).
> It should be issued by the same key that issued the revoked signature
> or by a (deprecated) Revocation Key. The signature is computed over
> the same data as the certification that it revokes, and it should
> have a later creation date than that certification.

### §5.2.1.14 Timestamp Signature (Type ID 0x40)

**N-085** (§5.2.1.14) _[lowercase/implied]_ — source line 1638

> This signature is only meaningful for the timestamp contained in it.

### §5.2.1.15 Third-Party Confirmation Signature (Type ID 0x50)

**N-086** (§5.2.1.15) — source lines 1642–1645

> This signature is a signature over another OpenPGP Signature packet.
> It is analogous to a notary seal on the signed data.  A Third-Party
> Confirmation signature SHOULD include a Signature Target subpacket
> that identifies the confirmed signature.

### §5.2.1.16 Reserved (Type ID 0xFF)

**N-087** (§5.2.1.16) — source lines 1649–1651

> An implementation MUST NOT create any signature with this type and
> MUST NOT validate any signature made with this type.  See
> Section 5.2.4.1 for more details.

### §5.2.2 Version 3 Signature Packet Format

**N-088** (§5.2.2) — source lines 1655–1674

```
   The body of a version 3 Signature packet contains:

   *  A 1-octet version number with value 3.

   *  A 1-octet length of the following hashed material; it MUST be 5:

      -  A 1-octet Signature Type ID.

      -  A 4-octet creation time.

   *  An 8-octet Key ID of the signer.

   *  A 1-octet public key algorithm.

   *  A 1-octet hash algorithm.

   *  A 2-octet field holding left 16 bits of the signed hash value.

   *  One or more MPIs comprising the signature.  This portion is
      algorithm specific, as described below.
```

**N-089** (§5.2.2) _[lowercase/implied]_ — source lines 1676–1681

> The concatenation of the data to be signed, the signature type, and
> the creation time from the Signature packet (5 additional octets) is
> hashed.  The resulting hash value is used in the signature algorithm.
> The high 16 bits (first two octets) of the hash are included in the
> Signature packet to provide a way to reject some invalid signatures
> without performing a signature verification.

**N-090** (§5.2.2) — source lines 1683–1691

```
   Algorithm-specific fields for RSA signatures:

   *  MPI of RSA signature value m^d mod n.

   Algorithm-specific fields for DSA signatures:

   *  MPI of DSA value r.

   *  MPI of DSA value s.
```

**N-091** (§5.2.2) _[lowercase/implied]_ — source lines 1693–1696

> The signature calculation is based on a hash of the signed data, as
> described above.  The details of the calculation are different for
> DSA signatures than for RSA signatures; see Sections 5.2.3.1 and
> 5.2.3.2.

### §5.2.3 Versions 4 and 6 Signature Packet Formats

**N-092** (§5.2.3) — source lines 1700–1739

```
   The body of a version 4 or version 6 Signature packet contains:

   *  A 1-octet version number.  This is 4 for version 4 signatures and
      6 for version 6 signatures.

   *  A 1-octet Signature Type ID.

   *  A 1-octet public key algorithm.

   *  A 1-octet hash algorithm.

   *  A scalar octet count for the hashed subpacket data that follows
      this field.  For a version 4 signature, this is a 2-octet field.
      For a version 6 signature, this is a 4-octet field.  Note that
      this is the length in octets of all of the hashed subpackets; an
      implementation's pointer incremented by this number will skip over
      the hashed subpackets.

   *  A hashed subpacket data set (zero or more subpackets).

   *  A scalar octet count for the unhashed subpacket data that follows
      this field.  For a version 4 signature, this is a 2-octet field.
      For a version 6 signature, this is a 4-octet field.  Note that
      this is the length in octets of all of the unhashed subpackets; an
      implementation's pointer incremented by this number will skip over
      the unhashed subpackets.

   *  An unhashed subpacket data set (zero or more subpackets).

   *  A 2-octet field holding the left 16 bits of the signed hash value.

   *  Only for version 6 signatures, a variable-length field containing:

      -  A 1-octet salt size.  The value MUST match the value defined
         for the hash algorithm as specified in Table 23.

      -  The salt, which is a random value of the specified size.

   *  One or more MPIs comprising the signature.  This portion is
      algorithm specific.
```

### §5.2.3.1 Algorithm-Specific Fields for RSA Signatures

**N-093** (§5.2.3.1) — source line 1743

```
   *  MPI of RSA signature value m^d mod n.
```

**N-094** (§5.2.3.1) _[lowercase/implied]_ — source lines 1745–1750

> With RSA signatures, the hash value is encoded using PKCS#1 encoding
> type EMSA-PKCS1-v1_5, as described in Section 9.2 of [RFC8017] (see
> also Section 12.1.3).  This requires inserting the hash value as an
> octet string into an ASN.1 structure.  The object identifier (OID)
> for the hash algorithm itself is also included in the structure; see
> the OIDs in Table 24.

### §5.2.3.2 Algorithm-Specific Fields for DSA or ECDSA Signatures

**N-095** (§5.2.3.2) — source lines 1754–1756

```
   *  MPI of DSA or ECDSA value r.

   *  MPI of DSA or ECDSA value s.
```

**N-096** (§5.2.3.2) — source lines 1758–1759

> A version 3 signature MUST NOT be created and MUST NOT be used with
> the Elliptic Curve Digital Signature Algorithm (ECDSA).

**N-097** (§5.2.3.2) — source lines 1761–1763

> A DSA signature MUST use a hash algorithm with a digest size of at
> least the number of bits of q, the group generated by the DSA key's
> generator value.

**N-098** (§5.2.3.2) _[lowercase/implied]_ — source lines 1765–1769

> If the output size of the chosen hash is larger than the number of
> bits of q, the hash result is truncated to fit by taking the number
> of leftmost bits equal to the number of bits of q.  This (possibly
> truncated) hash function result is treated as a number and used
> directly in the DSA signature algorithm.

**N-099** (§5.2.3.2) — source lines 1771–1774

> An ECDSA signature MUST use a hash algorithm with a digest size of at
> least the curve's "fsize" value (see Section 9.2), except in the case
> of NIST P-521, for which at least a 512-bit hash algorithm MUST be
> used.

### §5.2.3.3 Algorithm-Specific Fields for EdDSALegacy Signatures (Deprecated)

**N-100** (§5.2.3.3) — source lines 1779–1780

```
   *  Two MPI-encoded values, whose contents and formatting depend on
      the choice of curve used (see Section 9.2.1).
```

**N-101** (§5.2.3.3) — source lines 1782–1783

> A version 3 signature MUST NOT be created and MUST NOT be used with
> EdDSALegacy.

**N-102** (§5.2.3.3) — source lines 1785–1788

> An EdDSALegacy signature MUST use a hash algorithm with a digest size
> of at least the curve's "fsize" value (see Section 9.2).  A verifying
> implementation MUST reject any EdDSALegacy signature that uses a hash
> algorithm with a smaller digest size.

### §5.2.3.3.1 Algorithm-Specific Fields for Ed25519Legacy Signatures (Deprecated)

**N-103** (§5.2.3.3.1) _[lowercase/implied]_ — source lines 1793–1795

> The two MPIs for Ed25519Legacy represent the octet strings R and S of
> the Edwards-curve Digital Signature Algorithm (EdDSA) described in
> [RFC8032].

**N-104** (§5.2.3.3.1) — source lines 1797–1801

```
   *  MPI of an EC point R, represented as a (non-prefixed) native
      (little-endian) octet string up to 32 octets.

   *  MPI of EdDSA value S, also in (non-prefixed) native (little-
      endian) format with a length up to 32 octets.
```

**N-105** (§5.2.3.3.1) — source lines 1803–1804

> Ed25519Legacy MUST NOT be used in Signature packets version 6 or
> above.

### §5.2.3.4 Algorithm-Specific Fields for Ed25519 Signatures

**N-106** (§5.2.3.4) — source lines 1808–1810

```
   *  64 octets of the native signature.

   For more details, see Section 12.7.
```

**N-107** (§5.2.3.4) — source lines 1812–1813

> A version 3 signature MUST NOT be created and MUST NOT be used with
> Ed25519.

**N-108** (§5.2.3.4) — source lines 1815–1818

> An Ed25519 signature MUST use a hash algorithm with a digest size of
> at least 256 bits.  A verifying implementation MUST reject any
> Ed25519 signature that uses a hash algorithm with a smaller digest
> size.

### §5.2.3.5 Algorithm-Specific Fields for Ed448 Signatures

**N-109** (§5.2.3.5) — source lines 1822–1824

```
   *  114 octets of the native signature.

   For more details, see Section 12.7.
```

**N-110** (§5.2.3.5) — source lines 1826–1827

> A version 3 signature MUST NOT be created and MUST NOT be used with
> Ed448.

**N-111** (§5.2.3.5) — source lines 1829–1831

> An Ed448 signature MUST use a hash algorithm with a digest size of at
> least 512 bits.  A verifying implementation MUST reject any Ed448
> signature that uses a hash algorithm with a smaller digest size.

### §5.2.3.6 Notes on Signatures

**N-112** (§5.2.3.6) — source lines 1835–1844

> The concatenation of the data being signed, the signature data from
> the version number through the hashed subpacket data (inclusive), and
> (for signature versions later than 3) a 6-octet trailer (see
> Section 5.2.4) is hashed.  The resulting hash value is what is
> signed.  The high 16 bits (first two octets) of the hash are included
> in the Signature packet to provide a way to reject some invalid
> signatures without performing a signature verification.  When
> verifying a version 6 signature, an implementation MUST reject the
> signature if these octets do not match the first two octets of the
> computed hash.

**N-113** (§5.2.3.6) _[lowercase/implied]_ — source lines 1846–1851

> There are two fields consisting of Signature subpackets.  The first
> field is hashed with the rest of the signature data, while the second
> is not hashed into the signature.  The second set of subpackets (the
> "unhashed section") is not cryptographically protected by the
> signature and should include only advisory information.  See
> Section 13.13 for more information.

**N-114** (§5.2.3.6) _[lowercase/implied]_ — source lines 1853–1857

> The differences between a version 4 and version 6 signature are two-
> fold: first, a version 6 signature increases the width of the fields
> that indicate the size of the hashed and unhashed subpackets, making
> it possible to include significantly more data in subpackets.
> Second, the hash is salted with random data (see Section 13.2).

_The pointer to Section 5.2.4 (lines 1859–1860) is a cross-reference and is omitted._

### §5.2.3.7 Signature Subpacket Specification

**N-115** (§5.2.3.7) _[lowercase/implied]_ — source lines 1864–1869

> A subpacket data set consists of zero or more Signature subpackets.
> In Signature packets, the subpacket data set is preceded by a 2-octet
> (for version 4 signatures) or 4-octet (for version 6 signatures)
> scalar count of the length in octets of all the subpackets.  A
> pointer incremented by this number will skip over the subpacket data
> set.

**N-116** (§5.2.3.7) — source lines 1871–1878

```
   Each subpacket consists of a subpacket header and a body.  The header
   consists of:

   *  The encoded subpacket length (1, 2, or 5 octets).

   *  The encoded Subpacket Type ID (1 octet).

   *  The subpacket-specific data.
```

**N-117** (§5.2.3.7) _[lowercase/implied]_ — source lines 1880–1884

> The subpacket length field covers the encoded Subpacket Type ID and
> the subpacket-specific data, and it does not include the subpacket
> length field itself.  It is encoded similarly to a 1-octet, 2-octet,
> or 5-octet OpenPGP format packet header.  The encoded subpacket
> length can be decoded as follows:

**N-118** (§5.2.3.7) _[grammar]_ — source lines 1886–1896

```
   if the 1st octet <  192, then
       lengthOfLength = 1
       subpacketLen = 1st_octet

   if the 1st octet >= 192 and < 255, then
       lengthOfLength = 2
       subpacketLen = ((1st_octet - 192) << 8) + (2nd_octet) + 192

   if the 1st octet = 255, then
       lengthOfLength = 5
       subpacket length = [4-octet scalar starting at 2nd_octet]
```

**N-119** (§5.2.3.7) — source lines 1898–1903

> Bit 7 of the encoded Subpacket Type ID is the "critical" bit.  If
> set, it denotes that the subpacket is one that is critical for the
> evaluator of the signature to recognize.  If a subpacket is
> encountered that is marked critical but is unknown to the evaluating
> implementation, the evaluator SHOULD consider the signature to be in
> error.

**N-120** (§5.2.3.7) — source lines 1905–1906

> An implementation SHOULD ignore any non-critical subpacket of a type
> that it does not recognize.

**N-121** (§5.2.3.7) _[lowercase/implied]_ — source lines 1908–1911

> An evaluator may "recognize" a subpacket but not implement it.  The
> purpose of the critical bit is to allow the signer to tell an
> evaluator that it would prefer a new, unknown feature to generate an
> error rather than being ignored.

**N-122** (§5.2.3.7) _[lowercase/implied]_ — source lines 1913–1914

> The other bits of the encoded Subpacket Type ID (i.e., bits 6-0)
> contain the Subpacket Type ID.

**N-123** (§5.2.3.7) _[table]_ — source lines 1916–2002

```
   The following signature subpackets are defined:

        +=========+===========================+==================+
        |      ID | Description               | Reference        |
        +=========+===========================+==================+
        |       0 | Reserved                  |                  |
        +---------+---------------------------+------------------+
        |       1 | Reserved                  |                  |
        +---------+---------------------------+------------------+
        |       2 | Signature Creation Time   | Section 5.2.3.11 |
        +---------+---------------------------+------------------+
        |       3 | Signature Expiration Time | Section 5.2.3.18 |
        +---------+---------------------------+------------------+
        |       4 | Exportable Certification  | Section 5.2.3.19 |
        +---------+---------------------------+------------------+
        |       5 | Trust Signature           | Section 5.2.3.21 |
        +---------+---------------------------+------------------+
        |       6 | Regular Expression        | Section 5.2.3.22 |
        +---------+---------------------------+------------------+
        |       7 | Revocable                 | Section 5.2.3.20 |
        +---------+---------------------------+------------------+
        |       8 | Reserved                  |                  |
        +---------+---------------------------+------------------+
        |       9 | Key Expiration Time       | Section 5.2.3.13 |
        +---------+---------------------------+------------------+
        |      10 | Placeholder for backward  |                  |
        |         | compatibility             |                  |
        +---------+---------------------------+------------------+
        |      11 | Preferred Symmetric       | Section 5.2.3.14 |
        |         | Ciphers for v1 SEIPD      |                  |
        +---------+---------------------------+------------------+
        |      12 | Revocation Key            | Section 5.2.3.23 |
        |         | (deprecated)              |                  |
        +---------+---------------------------+------------------+
        |   13-15 | Reserved                  |                  |
        +---------+---------------------------+------------------+
        |      16 | Issuer Key ID             | Section 5.2.3.12 |
        +---------+---------------------------+------------------+
        |   17-19 | Reserved                  |                  |
        +---------+---------------------------+------------------+
        |      20 | Notation Data             | Section 5.2.3.24 |
        +---------+---------------------------+------------------+
        |      21 | Preferred Hash Algorithms | Section 5.2.3.16 |
        +---------+---------------------------+------------------+
        |      22 | Preferred Compression     | Section 5.2.3.17 |
        |         | Algorithms                |                  |
        +---------+---------------------------+------------------+
        |      23 | Key Server Preferences    | Section 5.2.3.25 |
        +---------+---------------------------+------------------+
        |      24 | Preferred Key Server      | Section 5.2.3.26 |
        +---------+---------------------------+------------------+
        |      25 | Primary User ID           | Section 5.2.3.27 |
        +---------+---------------------------+------------------+
        |      26 | Policy URI                | Section 5.2.3.28 |
        +---------+---------------------------+------------------+
        |      27 | Key Flags                 | Section 5.2.3.29 |
        +---------+---------------------------+------------------+
        |      28 | Signer's User ID          | Section 5.2.3.30 |
        +---------+---------------------------+------------------+
        |      29 | Reason for Revocation     | Section 5.2.3.31 |
        +---------+---------------------------+------------------+
        |      30 | Features                  | Section 5.2.3.32 |
        +---------+---------------------------+------------------+
        |      31 | Signature Target          | Section 5.2.3.33 |
        +---------+---------------------------+------------------+
        |      32 | Embedded Signature        | Section 5.2.3.34 |
        +---------+---------------------------+------------------+
        |      33 | Issuer Fingerprint        | Section 5.2.3.35 |
        +---------+---------------------------+------------------+
        |      34 | Reserved                  |                  |
        +---------+---------------------------+------------------+
        |      35 | Intended Recipient        | Section 5.2.3.36 |
        |         | Fingerprint               |                  |
        +---------+---------------------------+------------------+
        |      37 | Reserved (Attested        |                  |
        |         | Certifications)           |                  |
        +---------+---------------------------+------------------+
        |      38 | Reserved (Key Block)      |                  |
        +---------+---------------------------+------------------+
        |      39 | Preferred AEAD            | Section 5.2.3.15 |
        |         | Ciphersuites              |                  |
        +---------+---------------------------+------------------+
        | 100-110 | Private or Experimental   |                  |
        |         | Use                       |                  |
        +---------+---------------------------+------------------+

           Table 5: OpenPGP Signature Subpacket Types Registry
```

**N-124** (§5.2.3.7) — source lines 2004–2014

> Implementations SHOULD implement the four preferred algorithm
> subpackets (11, 21, 22, and 39), as well as the "Features" (30) and
> "Reason for Revocation" (29) subpackets.  To avoid surreptitious
> forwarding (see Section 13.12), implementations SHOULD also implement
> the "Intended Recipients Fingerprint" (35) subpacket.  Note that if
> an implementation chooses not to implement some of the preferences
> subpackets, it MUST default to the mandatory-to-implement algorithms
> to ensure interoperability.  An encrypting implementation that does
> not implement the "Features" (30) subpacket SHOULD select the type of
> encrypted data format based on the versions of the recipient keys or
> external inference (see Section 13.7 for more details).

### §5.2.3.8 Signature Subpacket Types

**N-125** (§5.2.3.8) _[lowercase/implied]_ — source lines 2018–2023

> A number of subpackets are currently defined for OpenPGP signatures.
> Some subpackets apply to the signature itself and some are attributes
> of the key.  Subpackets that are found on a self-signature are placed
> on a certification made by the key itself.  Note that a key may have
> more than one User ID and thus may have more than one self-signature
> and differing subpackets.

**N-126** (§5.2.3.8) _[lowercase/implied]_ — source lines 2025–2029

> A subpacket may be found in either the hashed or the unhashed
> subpacket sections of a signature.  If a subpacket is not hashed,
> then the information in it cannot be considered definitive because it
> is not covered by the cryptographic signature.  See Section 13.13 for
> more discussion about hashed and unhashed subpackets.

### §5.2.3.9 Notes on Subpackets

**N-127** (§5.2.3.9) — source lines 2033–2042

> It is certainly possible for a signature to contain conflicting
> information in subpackets.  For example, a signature may contain
> multiple copies of a preference or multiple expiration times.  In
> most cases, an implementation SHOULD use the last subpacket in the
> hashed section of the signature, but it MAY use any conflict
> resolution scheme that makes more sense.  Please note that conflict
> resolution is intentionally left to the implementer; most conflicts
> are simply syntax errors, and the ambiguous language here allows a
> receiver to be generous in what they accept, while putting pressure
> on a creator to be stingy in what they generate.

**N-128** (§5.2.3.9) _[lowercase/implied]_ — source lines 2044–2050

> Some apparent conflicts may actually make sense.  For example,
> suppose a keyholder has a version 3 key and a version 4 key that
> share the same RSA key material.  Either of these keys can verify a
> signature created by the other, and it may be reasonable for a
> signature to contain an Issuer Key ID subpacket (Section 5.2.3.12)
> for each key, as a way of explicitly tying those keys to the
> signature.

### §5.2.3.10 Notes on Self-Signatures

**N-129** (§5.2.3.10) _[lowercase/implied]_ — source lines 2054–2062

> A self-signature is a binding signature made by the key to which the
> signature refers.  There are three types of self-signatures: the
> certification signatures (Type IDs 0x10-0x13), the Direct Key
> signature (Type ID 0x1F), and the Subkey Binding signature (Type ID
> 0x18).  A cryptographically valid self-signature should be accepted
> from any primary key, regardless of what Key Flags (Section 5.2.3.29)
> apply to the primary key.  In particular, a primary key does not need
> to have 0x01 set in the first octet of the Key Flags order to make a
> valid self-signature.

**N-130** (§5.2.3.10) — source lines 2064–2070

> For certification self-signatures, each User ID MAY have a self-
> signature and thus different subpackets in those self-signatures.
> For Subkey Binding signatures, each subkey MUST have a self-
> signature.  Subpackets that appear in a certification self-signature
> apply to the User ID, and subpackets that appear in the subkey self-
> signature apply to the subkey.  Lastly, subpackets on the Direct Key
> signature apply to the entire key.

**N-131** (§5.2.3.10) _[lowercase/implied]_ — source lines 2072–2081

> An implementation should interpret a self-signature's preference
> subpackets as narrowly as possible.  For example, suppose a key has
> two user names, Alice and Bob. Suppose that Alice prefers the AEAD
> ciphersuite AES-256 with OCB, and Bob prefers Camellia-256 with GCM.
> If the implementation locates this key via Alice's name, then the
> preferred AEAD ciphersuite is AES-256 with OCB; if the implementation
> locates the key via Bob's name, then the preferred algorithm is
> Camellia-256 with GCM.  If the key is located by Key ID, the
> algorithm of the Primary User ID of the key provides the preferred
> AEAD ciphersuite.

**N-132** (§5.2.3.10) _[lowercase/implied]_ — source lines 2083–2094

> Revoking a self-signature or allowing it to expire has a semantic
> meaning that varies with the signature type.  Revoking the self-
> signature on a User ID effectively retires that user name.  The self-
> signature is a statement, "My name X is tied to my signing key K",
> and it is corroborated by other users' certifications.  If another
> user revokes their certification, they are effectively saying that
> they no longer believe that name and that key are tied together.
> Similarly, if the users themselves revoke their self-signature, then
> the users no longer go by that name, no longer have that email
> address, etc.  Revoking a binding signature effectively retires that
> subkey.  Revoking a Direct Key signature cancels that signature.
> Please see Section 5.2.3.31 for more relevant details.

**N-133** (§5.2.3.10) — source lines 2096–2099

> Since a self-signature contains important information about the key's
> use, an implementation SHOULD allow the user to rewrite the self-
> signature and important information in it, such as preferences and
> key expiration.

**N-134** (§5.2.3.10) — source lines 2101–2106

> When an implementation imports a secret key, it SHOULD verify that
> the key's internal self-signatures do not advertise features or
> algorithms that the implementation doesn't support.  If an
> implementation observes such a mismatch, it SHOULD warn the user and
> offer to create new self-signatures that advertise the actual set of
> features and algorithms supported by the implementation.

**N-135** (§5.2.3.10) — source lines 2108–2110

> An implementation that encounters multiple self-signatures on the
> same object MUST select the most recent valid self-signature and
> ignore all other self-signatures.

**N-136** (§5.2.3.10) — source lines 2112–2118

> By convention, a version 4 key stores information about the primary
> Public Key (key flags, key expiration, etc.) and the Transferable
> Public Key as a whole (features, algorithm preferences, etc.) in a
> User ID self-signature of type 0x10 or 0x13.  To use a version 4 key,
> some implementations require at least one User ID with a valid self-
> signature to be present.  For this reason, it is RECOMMENDED to
> include at least one User ID with a self-signature in version 4 keys.

**N-137** (§5.2.3.10) — source lines 2120–2128

> For version 6 keys, it is RECOMMENDED to store information about the
> primary Public Key as well as the Transferable Public Key as a whole
> (key flags, key expiration, features, algorithm preferences, etc.) in
> a Direct Key signature (Type ID 0x1F) over the Public Key, instead of
> placing that information in a User ID self-signature.  An
> implementation MUST ensure that a valid Direct Key signature is
> present before using a version 6 key.  This prevents certain attacks
> where an adversary strips a self-signature specifying a Key
> Expiration Time or certain preferences.

**N-138** (§5.2.3.10) — source lines 2130–2140

> An implementation SHOULD NOT require a User ID self-signature to be
> present in order to consume or use a key, unless the particular use
> is contingent on the keyholder identifying themselves with the
> textual label in the User ID.  For example, when refreshing a key to
> learn about changes in expiration, advertised features, algorithm
> preferences, revocation, subkey rotation, and so forth, there is no
> need to require a User ID self-signature.  On the other hand, when
> verifying a signature over an email message, an implementation MAY
> choose to only accept a signature from a key that has a valid self-
> signature over a User ID that matches the message's From: header, as
> a way to avoid a signature transplant attack.

### §5.2.3.11 Signature Creation Time

**N-139** (§5.2.3.11) — source lines 2144–2150

> (4-octet time field)
>
> The time the signature was made.
>
> This subpacket MUST be present in the hashed area.
>
> When generating this subpacket, it SHOULD be marked as critical.

### §5.2.3.12 Issuer Key ID

**N-140** (§5.2.3.12) — source lines 2154–2159

> (8-octet Key ID)
>
> The OpenPGP Key ID of the key issuing the signature.  If the version
> of that key is greater than 4, this subpacket MUST NOT be included in
> the signature.  For these keys, consider the Issuer Fingerprint
> subpacket (Section 5.2.3.35) instead.

_The note that this subpacket was formerly called the "Issuer" subpacket (lines 2161–2162) is history and is omitted._

### §5.2.3.13 Key Expiration Time

**N-141** (§5.2.3.13) — source lines 2166–2176

> (4-octet time field)
>
> The validity period of the key.  This is the number of seconds after
> the key creation time that the key expires.  For a direct or
> certification self-signature, the key creation time is that of the
> primary key.  For a Subkey Binding signature, the key creation time
> is that of the subkey.  If this is not present or has a value of
> zero, the key never expires.  This is found only on a self-signature.
>
> When an implementation generates this subpacket, it SHOULD be marked
> as critical.

### §5.2.3.14 Preferred Symmetric Ciphers for v1 SEIPD

**N-142** (§5.2.3.14) _[lowercase/implied]_ — source lines 2180–2191

> (array of 1-octet values)
>
> A series of Symmetric Cipher Algorithm IDs indicating how the
> keyholder prefers to receive the version 1 Symmetrically Encrypted
> and Integrity Protected Data packet (Section 5.13.1).  The subpacket
> body is an ordered list of octets with the most preferred listed
> first.  It is assumed that only the algorithms listed are supported
> by the recipient's implementation.  Algorithm IDs are defined in
> Section 9.3.  This is only found on a self-signature.
>
> When generating a v2 SEIPD packet, this preference list is not
> relevant.  See Section 5.2.3.15 instead.

### §5.2.3.15 Preferred AEAD Ciphersuites

**N-143** (§5.2.3.15) _[lowercase/implied]_ — source lines 2195–2214

> (array of pairs of octets indicating Symmetric Cipher and AEAD
> algorithms)
>
> A series of paired algorithm IDs indicating how the keyholder prefers
> to receive the version 2 Symmetrically Encrypted and Integrity
> Protected Data packet (Section 5.13.2).  Each pair of octets
> indicates a combination of a symmetric cipher and an AEAD mode that
> the keyholder prefers to use.  The Symmetric Cipher Algorithm ID
> precedes the AEAD algorithm ID in each pair.  The subpacket body is
> an ordered list of pairs of octets with the most preferred algorithm
> combination listed first.
>
> It is assumed that only the combinations of algorithms listed are
> supported by the recipient's implementation, with the exception of
> the mandatory-to-implement combination of AES-128 and OCB.  If
> AES-128 and OCB are not found in the subpacket, it is implicitly
> listed at the end.
>
> AEAD algorithm IDs are listed in Section 9.6.  Symmetric Cipher
> Algorithm IDs are listed in Section 9.3.

**N-144** (§5.2.3.15) _[lowercase/implied]_ — source lines 2216–2222

> For example, a subpacket containing the six octets
>
> 09 02 09 03 13 02
>
> indicates that the keyholder prefers to receive v2 SEIPD using
> AES-256 with OCB, then AES-256 with GCM, then Camellia-256 with OCB,
> and finally the implicit AES-128 with OCB.

**N-145** (§5.2.3.15) _[lowercase/implied]_ — source lines 2224–2231

> Note that support for the version 2 Symmetrically Encrypted and
> Integrity Protected Data packet (Section 5.13.2) in general is
> indicated by a Features Flag (Section 5.2.3.32).
>
> This subpacket is only found on a self-signature.
>
> When generating a v1 SEIPD packet, this preference list is not
> relevant.  See Section 5.2.3.14 instead.

### §5.2.3.16 Preferred Hash Algorithms

**N-146** (§5.2.3.16) _[lowercase/implied]_ — source lines 2235–2240

> (array of 1-octet values)
>
> Message digest algorithm IDs that indicate which algorithms the
> keyholder prefers to receive.  Like the Preferred AEAD Ciphersuites,
> the list is ordered.  Algorithm IDs are defined in Section 9.5.  This
> is only found on a self-signature.

### §5.2.3.17 Preferred Compression Algorithms

**N-147** (§5.2.3.17) _[lowercase/implied]_ — source lines 2244–2251

> (array of 1-octet values)
>
> Compression algorithm IDs that indicate which algorithms the
> keyholder prefers to use.  Like the Preferred AEAD Ciphersuites, the
> list is ordered.  Algorithm IDs are defined in Section 9.4.  A zero,
> or the absence of this subpacket, denotes that uncompressed data is
> preferred; the keyholder's implementation might have no compression
> support available.  This is only found on a self-signature.

### §5.2.3.18 Signature Expiration Time

**N-148** (§5.2.3.18) — source lines 2255–2262

> (4-octet time field)
>
> The validity period of the signature.  This is the number of seconds
> after the Signature Creation Time that the signature expires.  If
> this is not present or has a value of zero, it never expires.
>
> When an implementation generates this subpacket, it SHOULD be marked
> as critical.

### §5.2.3.19 Exportable Certification

**N-149** (§5.2.3.19) _[lowercase/implied]_ — source lines 2266–2273

> (1 octet of exportability, 0 for not, 1 for exportable)
>
> This subpacket denotes whether a certification signature is
> "exportable"; it is intended for use by users other than the
> signature's issuer.  The packet body contains a Boolean flag
> indicating whether the signature is exportable.  If this packet is
> not present, the certification is exportable; it is equivalent to a
> flag containing a 1.

**N-150** (§5.2.3.19) _[lowercase/implied]_ — source lines 2275–2280

> Non-exportable, or "local", certifications are signatures made by a
> user to mark a key as valid within that user's implementation only.
>
> Thus, when an implementation prepares a user's copy of a key for
> transport to another user (this is the process of "exporting" the
> key), any local certification signatures are deleted from the key.

**N-151** (§5.2.3.19) _[lowercase/implied]_ — source lines 2282–2292

> The receiver of a transported key "imports" it and likewise trims any
> local certifications.  In normal operation, there won't be any local
> certifications, assuming the import is performed on an exported key.
> However, there are instances where this can reasonably happen.  For
> example, if an implementation allows keys to be imported from a key
> database in addition to an exported key, then this situation can
> arise.
>
> Some implementations do not represent the interest of a single user
> (for example, a key server).  Such implementations always trim local
> certifications from any key they handle.

**N-152** (§5.2.3.19) — source lines 2294–2296

> When an implementation generates this subpacket and denotes the
> signature as non-exportable, the subpacket MUST be marked as
> critical.

### §5.2.3.20 Revocable

**N-153** (§5.2.3.20) _[lowercase/implied]_ — source lines 2300–2307

> (1 octet of revocability, 0 for not, 1 for revocable)
>
> A Signature's revocability status.  The packet body contains a
> Boolean flag indicating whether the signature is revocable.
> Signatures that are not revocable ignore any later Revocation
> Signatures.  They represent the signer's commitment that its
> signature cannot be revoked for the life of its key.  If this packet
> is not present, the signature is revocable.

### §5.2.3.21 Trust Signature

**N-154** (§5.2.3.21) _[lowercase/implied]_ — source line 2311

> (1 octet "level" (depth), 1 octet of trust amount)

**N-155** (§5.2.3.21) — source lines 2313–2325

> The signer asserts that the key is not only valid but also
> trustworthy at the specified level.  Level 0 has the same meaning as
> an ordinary validity signature.  Level 1 means that the signed key is
> asserted to be a valid trusted introducer, with the 2nd octet of the
> body specifying the degree of trust.  Level 2 means that the signed
> key is asserted to be trusted to issue level 1 Trust Signatures; that
> is, the signed key is a "meta introducer".  Generally, a level n
> Trust Signature asserts that a key is trusted to issue level n-1
> Trust Signatures.  The trust amount is in a range from 0-255,
> interpreted such that values less than 120 indicate partial trust and
> values of 120 or greater indicate complete trust.  Implementations
> SHOULD emit values of 60 for partial trust and 120 for complete
> trust.

### §5.2.3.22 Regular Expression

**N-156** (§5.2.3.22) _[lowercase/implied]_ — source line 2329

> (null-terminated UTF-8 encoded Regular Expression)

**N-157** (§5.2.3.22) _[lowercase/implied]_ — source lines 2331–2340

> Used in conjunction with Trust Signature packets (of level > 0) to
> limit the scope of trust that is extended.  Only signatures by the
> target key on User IDs that match the Regular Expression in the body
> of this packet have trust extended by the Trust Signature subpacket.
> The Regular Expression uses the same syntax as Henry Spencer's
> "almost public domain" Regular Expression [REGEX] package.  A
> description of the syntax is found in Section 8.  The Regular
> Expression matches (or does not match) a sequence of UTF-8-encoded
> Unicode characters from User IDs.  The expression itself is also
> written with UTF-8 characters.

**N-158** (§5.2.3.22) — source lines 2342–2348

> For historical reasons, this subpacket includes a null character (an
> octet with value zero) after the Regular Expression.  When an
> implementation parses a Regular Expression subpacket, it MUST remove
> this octet; if it is not present, it MUST reject the subpacket (i.e.,
> ignore the subpacket if it's non-critical and reject the signature if
> it's critical).  When an implementation generates a Regular
> Expression subpacket, it MUST include the null terminator.

**N-159** (§5.2.3.22) — source line 2350

> When generating this subpacket, it SHOULD be marked as critical.

### §5.2.3.23 Revocation Key (Deprecated)

**N-160** (§5.2.3.23) _[lowercase/implied]_ — source lines 2354–2355

> (1 octet of class, 1 octet of public key algorithm ID, 20 octets of
> version 4 fingerprint)

**N-161** (§5.2.3.23) — source lines 2357–2358

> This mechanism is deprecated.  Applications MUST NOT generate such a
> subpacket.

**N-162** (§5.2.3.23) _[lowercase/implied]_ — source lines 2360–2365

> An application that wants the functionality of delegating revocation
> can use an escrowed Revocation Signature.  See Section 13.9 for more
> details.
>
> The remainder of this section describes how some implementations
> attempt to interpret this deprecated subpacket.

**N-163** (§5.2.3.23) _[lowercase/implied]_ — source lines 2367–2373

> This packet was intended to authorize the specified key to issue
> Revocation Signatures for this key.  The class octet must have bit
> 0x80 set.  If bit 0x40 is set, it means the revocation information is
> sensitive.  Other bits are for future expansion to other kinds of
> authorizations.  This is only found on a Direct Key self-signature
> (Type ID 0x1F).  The use on other types of self-signatures is
> unspecified.

**N-164** (§5.2.3.23) — source lines 2375–2383

> If the "sensitive" flag is set, the keyholder feels this subpacket
> contains private trust information that describes a real-world
> sensitive relationship.  If this flag is set, implementations SHOULD
> NOT export this signature to other users except in cases where the
> data needs to be available, i.e., when the signature is being sent to
> the designated revoker or when it is accompanied by a Revocation
> Signature from that revoker.  Note that it may be appropriate to
> isolate this subpacket within a separate signature so that it is not
> combined with other subpackets that need to be exported.

### §5.2.3.24 Notation Data

**N-165** (§5.2.3.24) — source lines 2387–2397

> (4 octets of flags, 2 octets of name length (M), 2 octets of value
> length (N), M octets of name data, N octets of value data)
>
> This subpacket describes a "notation" on the signature that the
> issuer wishes to make.  The notation has a name and a value, each of
> which are strings of octets.  There may be more than one notation in
> a signature.  Notations can be used for any extension the issuer of
> the signature cares to make.  The "flags" field holds 4 octets of
> flags.
>
> All undefined flags MUST be zero.  Defined flags are as follows:

**N-166** (§5.2.3.24) _[table]_ — source lines 2399–2407

```
        +=======================+================+================+
        | Flag Position         | Shorthand      | Description    |
        +=======================+================+================+
        | 0x80000000 (first bit | human-readable | Notation value |
        | of the first octet)   |                | is UTF-8 text  |
        +-----------------------+----------------+----------------+

             Table 6: OpenPGP Signature Notation Data Subpacket
                          Notation Flags Registry
```

**N-167** (§5.2.3.24) — source lines 2409–2414

> Notation names are arbitrary strings encoded in UTF-8.  They reside
> in two namespaces: the IETF namespace and the user namespace.
>
> The IETF namespace is registered with IANA.  These names MUST NOT
> contain the "@" character (0x40).  This is a tag for the user
> namespace.

**N-168** (§5.2.3.24) _[table]_ — source lines 2416–2425

```
              +===============+===========+================+
              | Notation Name | Data Type | Allowed Values |
              +===============+===========+================+
              | No registrations at this time.             |
              +============================================+

                 Table 7: OpenPGP Signature Notation Data
                         Subpacket Types Registry

   This registry is initially empty.
```

**N-169** (§5.2.3.24) — source lines 2427–2430

> Names in the user namespace consist of a UTF-8 string tag followed by
> "@", followed by a DNS domain name.  Note that the tag MUST NOT
> contain an "@" character.  For example, the "sample" tag used by
> Example Corporation could be "sample@example.com".

**N-170** (§5.2.3.24) _[lowercase/implied]_ — source lines 2432–2434

> Names in a user space are owned and controlled by the owners of that
> domain.  Obviously, it's bad form to create a new name in a DNS space
> that you don't own.

**N-171** (§5.2.3.24) — source lines 2436–2440

> Since the user namespace is in the form of an email address,
> implementers MAY wish to arrange for that address to reach a person
> who can be consulted about the use of the named tag.  Note that due
> to UTF-8 encoding, not all valid user space name tags are valid email
> addresses.

**N-172** (§5.2.3.24) _[lowercase/implied]_ — source lines 2442–2443

> If there is a critical notation, the criticality applies to that
> specific notation and not to notations in general.

### §5.2.3.25 Key Server Preferences

**N-173** (§5.2.3.25) — source lines 2447–2451

> (N octets of flags)
>
> This is a list of 1-bit flags that indicates preferences that the
> keyholder has about how the key is handled on a key server.  All
> undefined flags MUST be zero.

**N-174** (§5.2.3.25) _[table]_ — source lines 2453–2461

```
    +=========+===========+===========================================+
    | Flag    | Shorthand | Definition                                |
    +=========+===========+===========================================+
    | 0x80... | No-modify | The keyholder requests that this key only |
    |         |           | be modified or updated by the keyholder   |
    |         |           | or an administrator of the key server.    |
    +---------+-----------+-------------------------------------------+

           Table 8: OpenPGP Key Server Preference Flags Registry
```

**N-175** (§5.2.3.25) _[lowercase/implied]_ — source line 2463

> This is found only on a self-signature.

### §5.2.3.26 Preferred Key Server

**N-176** (§5.2.3.26) _[lowercase/implied]_ — source lines 2467–2473

> (String)
>
> This is a URI of a key server that the keyholder prefers be used for
> updates.  Note that keys with multiple User IDs can have a Preferred
> Key Server for each User ID.  Note also that since this is a URI, the
> key server can actually be a copy of the key retrieved by https, ftp,
> http, etc.

### §5.2.3.27 Primary User ID

**N-177** (§5.2.3.27) — source lines 2477–2486

> (1 octet, Boolean)
>
> This is a flag in a User ID's self-signature that states whether this
> User ID is the main User ID for this key.  It is reasonable for an
> implementation to resolve ambiguities in preferences, for example, by
> referring to the Primary User ID.  If this flag is absent, its value
> is zero.  If more than one User ID in a key is marked as primary, the
> implementation may resolve the ambiguity in any way it sees fit, but
> it is RECOMMENDED that priority be given to the User ID with the most
> recent self-signature.

**N-178** (§5.2.3.27) _[lowercase/implied]_ — source lines 2488–2493

> When appearing on a self-signature on a User ID packet, this
> subpacket applies only to User ID packets.  When appearing on a self-
> signature on a User Attribute packet, this subpacket applies only to
> User Attribute packets.  That is, there are two different and
> independent "primaries" -- one for User IDs and one for User
> Attributes.

### §5.2.3.28 Policy URI

**N-179** (§5.2.3.28) _[lowercase/implied]_ — source lines 2497–2500

> (String)
>
> This subpacket contains a URI of a document that describes the policy
> under which the signature was issued.

### §5.2.3.29 Key Flags

**N-180** (§5.2.3.29) — source lines 2504–2510

> (N octets of flags)
>
> This subpacket contains a list of binary flags that hold information
> about a key.  It is a string of octets, and an implementation MUST
> NOT assume a fixed size, so that it can grow over time.  If a list is
> shorter than an implementation expects, the unstated flags are
> considered to be zero.  The defined flags are as follows:

**N-181** (§5.2.3.29) _[table]_ — source lines 2512–2538

```
   +===========+======================================================+
   | Flag      | Definition                                           |
   +===========+======================================================+
   | 0x01...   | This key may be used to make User ID certifications  |
   |           | (Signature Type IDs 0x10-0x13) or Direct Key         |
   |           | signatures (Signature Type ID 0x1F) over other keys. |
   +-----------+------------------------------------------------------+
   | 0x02...   | This key may be used to sign data.                   |
   +-----------+------------------------------------------------------+
   | 0x04...   | This key may be used to encrypt communications.      |
   +-----------+------------------------------------------------------+
   | 0x08...   | This key may be used to encrypt storage.             |
   +-----------+------------------------------------------------------+
   | 0x10...   | The private component of this key may have been      |
   |           | split by a secret-sharing mechanism.                 |
   +-----------+------------------------------------------------------+
   | 0x20...   | This key may be used for authentication.             |
   +-----------+------------------------------------------------------+
   | 0x80...   | The private component of this key may be in the      |
   |           | possession of more than one person.                  |
   +-----------+------------------------------------------------------+
   | 0x0004... | Reserved (ADSK)                                      |
   +-----------+------------------------------------------------------+
   | 0x0008... | Reserved (timestamping)                              |
   +-----------+------------------------------------------------------+

                   Table 9: OpenPGP Key Flags Registry
```

**N-182** (§5.2.3.29) _[lowercase/implied]_ — source lines 2540–2552

> Usage notes:
>
> The flags in this packet may appear in self-signatures or in
> certification signatures.  They mean different things depending on
> who is making the statement.  For example, a certification signature
> that has the "sign data" flag is stating that the certification is
> for that use.  On the other hand, the "communications encryption"
> flag in a self-signature is stating a preference that a given key be
> used for communications.  However, note that determining what is
> "communications" and what is "storage" is a thorny issue.  This
> decision is left wholly up to the implementation; the authors of this
> document do not claim any special wisdom on the issue and realize
> that accepted opinion may change.

**N-183** (§5.2.3.29) — source lines 2554–2558

> The "split key" (0x10) and "group key" (0x80) flags are placed on a
> self-signature only; they are meaningless on a certification
> signature.  They SHOULD be placed only on a Direct Key signature
> (Type ID 0x1F) or a Subkey Binding signature (Type ID 0x18), one that
> refers to the key the flag applies to.

**N-184** (§5.2.3.29) — source lines 2560–2561

> When an implementation generates this subpacket, it SHOULD be marked
> as critical.

### §5.2.3.30 Signer's User ID

**N-185** (§5.2.3.30) _[lowercase/implied]_ — source lines 2565–2574

> (String)
>
> This subpacket allows a keyholder to state which User ID is
> responsible for the signing.  Many keyholders use a single key for
> different purposes, such as business communications as well as
> personal communications.  This subpacket allows such a keyholder to
> state which of their roles is making a signature.
>
> This subpacket is not appropriate to use to refer to a User Attribute
> packet.

### §5.2.3.31 Reason for Revocation

**N-186** (§5.2.3.31) _[lowercase/implied]_ — source lines 2578–2585

> (1 octet of revocation code, N octets of reason string)
>
> This subpacket is used only in Key Revocation and Certification
> Revocation signatures.  It describes the reason why the key or
> certification was revoked.
>
> The first octet contains a machine-readable code that denotes the
> reason for the revocation:

**N-187** (§5.2.3.31) _[table]_ — source lines 2587–2609

```
           +=========+========================================+
           |    Code | Reason                                 |
           +=========+========================================+
           |       0 | No reason specified (Key Revocation or |
           |         | Certification Revocation signatures)   |
           +---------+----------------------------------------+
           |       1 | Key is superseded (Key Revocation      |
           |         | signatures)                            |
           +---------+----------------------------------------+
           |       2 | Key material has been compromised (Key |
           |         | Revocation signatures)                 |
           +---------+----------------------------------------+
           |       3 | Key is retired and no longer used (Key |
           |         | Revocation signatures)                 |
           +---------+----------------------------------------+
           |      32 | User ID information is no longer valid |
           |         | (Certification Revocation signatures)  |
           +---------+----------------------------------------+
           | 100-110 | Private Use                            |
           +---------+----------------------------------------+

                 Table 10: OpenPGP Reason for Revocation
                       (Revocation Octet) Registry
```

**N-188** (§5.2.3.31) — source lines 2611–2618

> Following the revocation code is a string of octets that gives
> information about the Reason for Revocation in human-readable form
> (UTF-8).  The string may be null (of zero length).  The length of the
> subpacket is the length of the reason string plus one.  An
> implementation SHOULD implement this subpacket, include it in all
> Revocation Signatures, and interpret revocations appropriately.
> There are important semantic differences between the reasons, and
> there are thus important reasons for revoking signatures.

**N-189** (§5.2.3.31) — source lines 2620–2626

> If a key has been revoked because of a compromise, all signatures
> created by that key are suspect.  However, if it was merely
> superseded or retired, old signatures are still valid.  If the
> revoked signature is the self-signature for certifying a User ID, a
> revocation denotes that that user name is no longer in use.  Such a
> signature revocation SHOULD include a Reason for Revocation subpacket
> containing code 32.

**N-190** (§5.2.3.31) _[lowercase/implied]_ — source lines 2628–2632

> Note that any certification may be revoked, including a certification
> on some other person's key.  There are many good reasons for revoking
> a certification signature, such as the case where the keyholder
> leaves the employ of a business with an email address.  A revoked
> certification is no longer a part of validity calculations.

### §5.2.3.32 Features

**N-191** (§5.2.3.32) _[lowercase/implied]_ — source lines 2636–2645

> (N octets of flags)
>
> The Features subpacket denotes which advanced OpenPGP features a
> user's implementation supports.  This is so that as features are
> added to OpenPGP that cannot be backward compatible, a user can state
> that they can use that feature.  The flags are single bits that
> indicate that a given feature is supported.
>
> This subpacket is similar to a preferences subpacket and only appears
> in a self-signature.

**N-192** (§5.2.3.32) — source lines 2647–2650

> An implementation SHOULD NOT use a feature listed when sending to a
> user who does not state that they can use it, unless the
> implementation can infer support for the feature from another
> implementation-dependent mechanism.

**N-193** (§5.2.3.32) _[table]_ — source lines 2652–2670

```
   Defined features are as follows:

   First octet:

       +=========+=====================================+===========+
       | Feature | Definition                          | Reference |
       +=========+=====================================+===========+
       | 0x01... | Version 1 Symmetrically Encrypted   | Section   |
       |         | and Integrity Protected Data packet | 5.13.1    |
       +---------+-------------------------------------+-----------+
       | 0x02... | Reserved                            |           |
       +---------+-------------------------------------+-----------+
       | 0x04... | Reserved                            |           |
       +---------+-------------------------------------+-----------+
       | 0x08... | Version 2 Symmetrically Encrypted   | Section   |
       |         | and Integrity Protected Data packet | 5.13.2    |
       +---------+-------------------------------------+-----------+

                 Table 11: OpenPGP Features Flags Registry
```

**N-194** (§5.2.3.32) — source lines 2672–2673

> If an implementation implements any of the defined features, it
> SHOULD implement the Features subpacket, too.

_The pointer to Section 13.7 for using the Features subpacket (lines 2675–2676) is a cross-reference and is omitted._

### §5.2.3.33 Signature Target

**N-195** (§5.2.3.33) _[lowercase/implied]_ — source lines 2680–2687

> (1 octet public key algorithm, 1 octet hash algorithm, N octets hash)
>
> This subpacket identifies a specific target signature to which a
> signature refers.  For Revocation Signatures, this subpacket provides
> explicit designation of which signature is being revoked.  For a
> Third-Party Confirmation or Timestamp signature, this designates what
> signature is signed.  All arguments are an identifier of that target
> signature.

**N-196** (§5.2.3.33) — source lines 2689–2691

> The N octets of hash data MUST be the size of the signature's hash.
> For example, a target signature with a SHA-1 hash MUST have 20 octets
> of hash data.

### §5.2.3.34 Embedded Signature

**N-197** (§5.2.3.34) _[lowercase/implied]_ — source lines 2695–2699

> (1 Signature packet body)
>
> This subpacket contains a complete Signature packet body as specified
> in Section 5.2.  It is useful when one signature needs to refer to,
> or be incorporated in, another signature.

### §5.2.3.35 Issuer Fingerprint

**N-198** (§5.2.3.35) — source lines 2703–2710

> (1 octet key version number, N octets of fingerprint)
>
> The OpenPGP Key fingerprint of the key issuing the signature.  This
> subpacket SHOULD be included in all signatures.  If the version of
> the issuing key is 4 and an Issuer Key ID subpacket
> (Section 5.2.3.12) is also included in the signature, the Key ID of
> the Issuer Key ID subpacket MUST match the low 64 bits of the
> fingerprint.

**N-199** (§5.2.3.35) — source lines 2712–2717

> Note that the length N of the fingerprint for a version 4 key is 20
> octets; for a version 6 key, N is 32.  Since the version of the
> signature is bound to the version of the key, the version octet here
> MUST match the version of the signature.  If the version octet does
> not match the signature version, the receiving implementation MUST
> treat it as a malformed signature (see Section 5.2.5).

### §5.2.3.36 Intended Recipient Fingerprint

**N-200** (§5.2.3.36) — source lines 2721–2728

> (1 octet key version number, N octets of fingerprint)
>
> The OpenPGP Key fingerprint of the intended recipient primary key.
> If one or more subpackets of this type are included in a signature,
> it SHOULD be considered valid only in an encrypted context, where the
> key it was encrypted to is one of the indicated primary keys or one
> of their subkeys.  This can be used to prevent forwarding a signature
> outside of its intended, encrypted context (see Section 13.12).

**N-201** (§5.2.3.36) _[lowercase/implied]_ — source lines 2730–2731

> Note that the length N of the fingerprint for a version 4 key is 20
> octets; for a version 6 key, N is 32.

**N-202** (§5.2.3.36) — source lines 2733–2734

> An implementation SHOULD generate this subpacket when creating a
> signed and encrypted message.

**N-203** (§5.2.3.36) — source lines 2736–2737

> When generating this subpacket in a version 6 signature, it SHOULD be
> marked as critical.

### §5.2.4 Computing Signatures

**N-204** (§5.2.4) _[lowercase/implied]_ — source lines 2741–2745

> All signatures are formed by producing a hash over the signature data
> and then using the resulting hash in the signature algorithm.
>
> When creating or verifying a version 6 signature, the salt is fed
> into the hash context before any other data.

**N-205** (§5.2.4) — source lines 2747–2751

> For binary document signatures (Type ID 0x00), the document data is
> hashed directly.  For text document signatures (Type ID 0x01), the
> implementation MUST first canonicalize the document by converting
> line endings to <CR><LF> and encoding it in UTF-8 (see [RFC3629]).
> The resulting UTF-8 byte stream is hashed.

**N-206** (§5.2.4) _[lowercase/implied]_ — source lines 2753–2758

> When a version 4 signature is made over a key, the hash data starts
> with the octet 0x99, followed by a 2-octet length of the key,
> followed by the body of the key packet.  When a version 6 signature
> is made over a key, the hash data starts with the salt and then octet
> 0x9B, followed by a 4-octet length of the key, followed by the body
> of the key packet.

**N-207** (§5.2.4) _[lowercase/implied]_ — source lines 2760–2765

> A Subkey Binding signature (Type ID 0x18) or Primary Key Binding
> signature (Type ID 0x19) then hashes the subkey using the same format
> as the main key (also using 0x99 or 0x9B as the first octet).
> Primary Key Revocation signatures (Type ID 0x20) hash only the key
> being revoked.  A Subkey Revocation signature (Type ID 0x28) first
> hashes the primary key and then the subkey being revoked.

**N-208** (§5.2.4) _[lowercase/implied]_ — source lines 2767–2775

> A Certification signature (Type IDs 0x10 through 0x13) hashes the
> User ID that is bound to the key into the hash context after the
> above data.  A version 3 certification hashes the contents of the
> User ID or User Attribute packet without the packet header.  A
> version 4 or version 6 certification hashes the constant 0xB4 for
> User ID certifications or the constant 0xD1 for User Attribute
> certifications, followed by a 4-octet number giving the length of the
> User ID or User Attribute data, followed by the User ID or User
> Attribute data.

**N-209** (§5.2.4) _[lowercase/implied]_ — source lines 2777–2784

> A Third-Party Confirmation signature (Type ID 0x50) hashes the salt
> (version 6 signatures only), followed by the octet 0x88, followed by
> the 4-octet length of the signature, and then the body of the
> Signature packet.  (Note that this is a Legacy packet header for a
> Signature packet with the length-of-length field set to zero.)  The
> unhashed subpacket data of the Signature packet being hashed is not
> included in the hash, and the unhashed subpacket data length value is
> set to zero.

**N-210** (§5.2.4) _[lowercase/implied]_ — source lines 2786–2787

> Once the data body is hashed, then a trailer is hashed.  This trailer
> depends on the version of the signature.

**N-211** (§5.2.4) _[lowercase/implied]_ — source lines 2789–2819

```
   *  A version 3 signature hashes five octets of the packet body,
      starting from the signature type field.  This data is the
      signature type, followed by the 4-octet Signature Creation Time.

   *  A version 4 or version 6 signature hashes the packet body starting
      from its first field, the version number, through the end of the
      hashed subpacket data and a final extra trailer.  Thus, the hashed
      fields are:

      -  an octet indicating the signature version (0x04 for version 4,
         and 0x06 for version 6),

      -  the signature type,

      -  the public key algorithm,

      -  the hash algorithm,

      -  the hashed subpacket length,

      -  the hashed subpacket body,

      -  a second version octet (0x04 for version 4, and 0x06 for
         version 6),

      -  a single octet 0xFF, and

      -  a number representing the length (in octets) of the hashed data
         from the Signature packet through the hashed subpacket body.
         This a 4-octet big-endian unsigned integer of the length modulo
         2^32.
```

**N-212** (§5.2.4) _[lowercase/implied]_ — source lines 2821–2824

> After all this has been hashed in a single hash context, the
> resulting hash field is used in the signature algorithm, and its
> first two octets are placed in the Signature packet, as described in
> Section 5.2.3.

_The pointer to the worked examples in Appendix A.3.1 (lines 2826–2827) is a cross-reference and is omitted; the vectors are recorded with Appendix A._

### §5.2.4.1 Notes about Signature Computation

**N-213** (§5.2.4.1) _[lowercase/implied]_ — source lines 2831–2836

> The data actually hashed by OpenPGP varies depending on the signature
> version, in order to ensure that a signature made using one version
> cannot be repurposed as a signature with a different version over
> subtly different data.  The hashed data streams differ based on their
> trailer, most critically in the fifth and sixth octets from the end
> of the stream.  In particular:

**N-214** (§5.2.4.1) — source lines 2838–2844

```
   *  A version 3 signature uses the fifth octet from the end to store
      its Signature Type ID.  This MUST NOT be Signature Type ID 0xFF.

   *  All signature versions later than version 3 always use a literal
      0xFF in the fifth octet from the end.  For these later signature
      versions, the sixth octet from the end (the octet before the 0xFF)
      stores the signature version number.
```

### §5.2.5 Malformed and Unknown Signatures

**N-215** (§5.2.5) _[lowercase/implied]_ — source lines 2848–2851

> In some cases, a Signature packet (or its corresponding One-Pass
> Signature packet; see Section 5.4) may be malformed or unknown.  For
> example, it might encounter any of the following problems (this is
> not an exhaustive list):

**N-216** (§5.2.5) _[lowercase/implied]_ — source lines 2853–2875

```
   *  An unknown signature type

   *  An unknown signature version

   *  An unsupported signature version

   *  An unknown "critical" subpacket (see Section 5.2.3.7) in the
      hashed area

   *  A subpacket with a length that diverges from the expected length

   *  A hashed subpacket area with length that exceeds the length of the
      Signature packet itself

   *  A hash algorithm known to be weak (e.g., MD5)

   *  A mismatch between the expected salt length of the hash algorithm
      and the actual salt length

   *  A mismatch between the One-Pass Signature version and the
      Signature version (see Section 10.3.2.2)

   *  A signature with a version other than 6, made by a version 6 key
```

**N-217** (§5.2.5) — source lines 2877–2882

> When an implementation encounters such a malformed or unknown
> signature, it MUST ignore the signature for validation purposes.  It
> MUST NOT indicate a successful signature validation for such a
> signature.  At the same time, it MUST NOT halt processing on the
> packet stream or reject other signatures in the same packet stream
> just because an unknown or invalid signature exists.

_The rationale paragraph (forward compatibility; lines 2884–2886) is motivation and is omitted._

## §5.3 Symmetric Key Encrypted Session Key Packet (Type ID 3)

**N-218** (§5.3) _[lowercase/implied]_ — source lines 2890–2898

> The Symmetric Key Encrypted Session Key (SKESK) packet holds the
> symmetric key encryption of a session key used to encrypt a message.
> Zero or more Public Key Encrypted Session Key packets (Section 5.1)
> and/or Symmetric Key Encrypted Session Key packets precede an
> encryption container (that is, a Symmetrically Encrypted and
> Integrity Protected Data packet or -- for historic data -- a
> Symmetrically Encrypted Data packet) that holds an Encrypted Message.
> The message is encrypted with a session key, and the session key is
> itself encrypted and stored in the Encrypted Session Key packet(s).

**N-219** (§5.3) _[lowercase/implied]_ — source lines 2900–2904

> If the encryption container is preceded by one or more Symmetric Key
> Encrypted Session Key packets, each specifies a passphrase that may
> be used to decrypt the message.  This allows a message to be
> encrypted to a number of public keys, and also to one or more
> passphrases.

**N-220** (§5.3) _[lowercase/implied]_ — source lines 2906–2908

> The body of this packet starts with a 1-octet number giving the
> version number of the packet type.  The currently defined versions
> are 4 and 6.  The remainder of the packet depends on the version.

**N-221** (§5.3) _[lowercase/implied]_ — source lines 2910–2914

> The versions differ in how they encrypt the session key with the
> passphrase and in what they encode.  The version of the SKESK packet
> must align with the version of the SEIPD packet (see
> Section 10.3.2.1).  Any new version of the SKESK packet should be
> registered in the registry established in Section 10.3.2.1.

### §5.3.1 Version 4 Symmetric Key Encrypted Session Key Packet Format

**N-222** (§5.3.1) — source lines 2918–2921

> A v4 SKESK packet precedes a v1 SEIPD (see Section 5.13.1).  In
> historic data, it is sometimes found preceding a deprecated SED
> packet (see Section 5.7).  A v4 SKESK packet MUST NOT precede a v2
> SEIPD packet (see Section 10.3.2.1).

**N-223** (§5.3.1) — source lines 2923–2933

```
   A version 4 Symmetric Key Encrypted Session Key packet consists of:

   *  A 1-octet version number with value 4.

   *  A 1-octet number describing the symmetric algorithm used.

   *  An S2K Specifier.  The length of the S2K Specifier depends on its
      type (see Section 3.7.1).

   *  Optionally, the encrypted session key itself, which is decrypted
      with the S2K object.
```

**N-224** (§5.3.1) _[lowercase/implied]_ — source lines 2935–2939

> If the encrypted session key is not present (which can be detected on
> the basis of packet length and S2K Specifier size), then the S2K
> algorithm applied to the passphrase produces the session key for
> decrypting the message, using the Symmetric Cipher Algorithm ID from
> the Symmetric Key Encrypted Session Key packet.

**N-225** (§5.3.1) _[lowercase/implied]_ — source lines 2941–2947

> If the encrypted session key is present, the result of applying the
> S2K algorithm to the passphrase is used to decrypt just that
> encrypted session key field, using CFB mode with an IV of all zeros.
> The decryption result consists of a 1-octet algorithm identifier that
> specifies the symmetric key encryption algorithm used to encrypt the
> following encryption container, followed by the session key octets
> themselves.

**N-226** (§5.3.1) — source lines 2949–2952

> Note: because an all-zero IV is used for this decryption, the S2K
> Specifier MUST use a salt value, a Salted S2K, an Iterated and Salted
> S2K, or Argon2.  The salt value will ensure that the decryption key
> is not repeated even if the passphrase is reused.

### §5.3.2 Version 6 Symmetric Key Encrypted Session Key Packet Format

**N-227** (§5.3.2) — source lines 2956–2958

> A v6 SKESK packet precedes a v2 SEIPD packet (see Section 5.13.2).  A
> v6 SKESK packet MUST NOT precede a v1 SEIPD packet or a deprecated
> Symmetrically Encrypted Data packet (see Section 10.3.2.1).

**N-228** (§5.3.2) — source lines 2960–2980

```
   A version 6 Symmetric Key Encrypted Session Key packet consists of:

   *  A 1-octet version number with value 6.

   *  A 1-octet scalar octet count for the 5 fields following this
      octet.

   *  A 1-octet Symmetric Cipher Algorithm ID (from Table 21).

   *  A 1-octet AEAD algorithm identifier (from Table 25).

   *  A 1-octet scalar octet count of the following field.

   *  An S2K Specifier.  The length of the S2K Specifier depends on its
      type (see Section 3.7.1).

   *  A starting IV of the size specified by the AEAD algorithm.

   *  The encrypted session key itself.

   *  An authentication tag for the AEAD mode.
```

**N-229** (§5.3.2) _[lowercase/implied]_ — source lines 2982–2988

> A key-encryption key (KEK) is derived using HKDF [RFC5869] with
> SHA256 [RFC6234] as the hash algorithm.  The Initial Keying Material
> (IKM) for HKDF is the key derived from S2K.  No salt is used.  The
> info parameter is comprised of the Packet Type ID in OpenPGP format
> encoding (bits 7 and 6 are set, and bits 5-0 carry the Packet Type
> ID), the packet version, and the cipher-algo and AEAD-mode used to
> encrypt the key material.

**N-230** (§5.3.2) _[lowercase/implied]_ — source lines 2990–2998

> Then, the session key is encrypted using the resulting key, with the
> AEAD algorithm specified for the version 2 Symmetrically Encrypted
> and Integrity Protected Data packet.  Note that no chunks are used
> and that there is only one authentication tag.  The Packet Type ID
> encoded in OpenPGP format (bits 7 and 6 are set, and bits 5-0 carry
> the Packet Type ID), the packet version number, the cipher algorithm
> ID, and the AEAD algorithm ID are given as additional data.  For
> example, the additional data used with AES-128 with OCB consists of
> the octets 0xC3, 0x06, 0x07, and 0x02.

## §5.4 One-Pass Signature Packet (Type ID 4)

**N-231** (§5.4) _[lowercase/implied]_ — source lines 3002–3006

> The One-Pass Signature packet precedes the signed data and contains
> enough information to allow the receiver to begin calculating any
> hashes needed to verify the signature.  It allows the Signature
> packet to be placed at the end of the message so that the signer can
> compute the entire signed message in one pass.

**N-232** (§5.4) — source lines 3008–3039

```
   The body of this packet consists of:

   *  A 1-octet version number.  The currently defined versions are 3
      and 6.  Any new One-Pass Signature packet version should be
      registered in the registry established in Section 10.3.2.2.

   *  A 1-octet Signature Type ID.  Signature types are described in
      Section 5.2.1.

   *  A 1-octet number describing the hash algorithm used.

   *  A 1-octet number describing the public key algorithm used.

   *  Only for version 6 packets, a variable-length field containing:

      -  A 1-octet salt size.  The value MUST match the value defined
         for the hash algorithm as specified in Table 23.

      -  The salt; a random value of the specified size.  The value MUST
         match the salt field of the corresponding Signature packet.

   *  Only for v3 packets, an 8-octet number holding the Key ID of the
      signing key.

   *  Only for version 6 packets, 32 octets of the fingerprint of the
      signing key.  Since a version 6 signature can only be made by a
      version 6 key, the length of the fingerprint is fixed.

   *  A 1-octet number holding a flag showing whether the signature is
      nested.  A zero value indicates that the next packet is another
      One-Pass Signature packet that describes another signature to be
      applied to the same message data.
```

**N-233** (§5.4) — source lines 3041–3046

> When generating a one-pass signature, the OPS packet version MUST
> correspond to the version of the associated Signature packet, except
> for the historical accident that version 4 keys use a version 3 One-
> Pass Signature packet (there is no version 4 OPS).  See
> Section 10.3.2.2 for the full correspondence of versions between
> Keys, Signatures, and One-Pass Signatures.

**N-234** (§5.4) _[lowercase/implied]_ — source lines 3048–3052

> Note that if a message contains more than one one-pass signature,
> then the Signature packets bracket the message; that is, the first
> Signature packet after the message corresponds to the last One-Pass
> Signature packet and the final Signature packet corresponds to the
> first One-Pass Signature packet.

## §5.5 Key Material Packets

_Lines 3056–3059, the overview of the four key packet versions and the remark that the section is complex, are document overview and are omitted._

**N-235** (§5.5) _[lowercase/implied]_ — source lines 3061–3062

> For historical reasons, versions 1 and 5 of the key packets are
> unspecified.

### §5.5.1 Key Packet Variants

_No entry: the section is a heading only; its content is in §5.5.1.1 to §5.5.1.4._

### §5.5.1.1 Public Key Packet (Type ID 6)

**N-236** (§5.5.1.1) _[lowercase/implied]_ — source lines 3068–3069

> A Public Key packet starts a series of packets that forms an OpenPGP
> Key (sometimes called an OpenPGP certificate).

### §5.5.1.2 Public Subkey Packet (Type ID 14)

**N-237** (§5.5.1.2) _[lowercase/implied]_ — source lines 3073–3078

> A Public Subkey packet (Type ID 14) has exactly the same format as a
> Public Key packet, but it denotes a subkey.  One or more subkeys may
> be associated with a top-level key.  By convention, the top-level key
> offers certification capability, but it does not provide encryption
> services, while a dedicated subkey provides encryption (see
> Section 10.1.5).

### §5.5.1.3 Secret Key Packet (Type ID 5)

**N-238** (§5.5.1.3) _[lowercase/implied]_ — source lines 3082–3084

> A Secret Key packet contains all the information that is found in a
> Public Key packet, including the public key material, but it also
> includes the secret key material after all the public key fields.

### §5.5.1.4 Secret Subkey Packet (Type ID 7)

**N-239** (§5.5.1.4) _[lowercase/implied]_ — source lines 3088–3089

> A Secret Subkey packet (Type ID 7) is the subkey analog of the Secret
> Key packet and has exactly the same format.

### §5.5.2 Public Key Packet Formats

**N-240** (§5.5.2) _[lowercase/implied]_ — source lines 3093–3095

> There are four versions of key material packets.  Versions 2 and 3
> have been deprecated since 1998.  Version 4 has been deprecated by
> this document.

**N-241** (§5.5.2) — source lines 3097–3102

> OpenPGP implementations SHOULD create keys with version 6 format.
> Version 4 keys are deprecated; an implementation SHOULD NOT generate
> a version 4 key but SHOULD accept it.  Version 3 keys are deprecated;
> an implementation MUST NOT generate a version 3 key but MAY accept
> it.  Version 2 keys are deprecated; an implementation MUST NOT
> generate a version 2 key but MAY accept it.

**N-242** (§5.5.2) _[lowercase/implied]_ — source lines 3104–3105

> Any new Key Version must be registered in the registry established in
> Section 10.3.2.2.

### §5.5.2.1 Version 3 Public Keys

**N-243** (§5.5.2.1) — source lines 3109–3125

```
   Version 2 keys are identical to version 3 keys except for the version
   number.  A version 3 Public Key or Public Subkey packet contains:

   *  A 1-octet version number (3).

   *  A 4-octet number denoting the time that the key was created.

   *  A 2-octet number denoting the time in days that the key is valid.
      If this number is zero, then it does not expire.

   *  A 1-octet number denoting the public key algorithm of the key.

   *  A series of multiprecision integers comprising the key material:

      -  MPI of RSA public modulus n.

      -  MPI of RSA public encryption exponent e.
```

_Lines 3127–3135, the three weaknesses of version 3 keys, are motivation for the deprecation and are omitted._

### §5.5.2.2 Version 4 Public Keys

**N-244** (§5.5.2.2) _[lowercase/implied]_ — source lines 3139–3143

> The version 4 format is similar to the version 3 format except for
> the absence of a validity period.  This has been moved to the
> Signature packet.  In addition, fingerprints of version 4 keys are
> calculated differently from version 3 keys, as described in
> Section 5.5.4.

**N-245** (§5.5.2.2) — source lines 3145–3154

```
   A version 4 packet contains:

   *  A 1-octet version number (4).

   *  A 4-octet number denoting the time that the key was created.

   *  A 1-octet number denoting the public key algorithm of the key.

   *  A series of values comprising the key material.  This is algorithm
      specific and described in Section 5.5.5.
```

### §5.5.2.3 Version 6 Public Keys

**N-246** (§5.5.2.3) _[lowercase/implied]_ — source lines 3158–3163

> The version 6 format is similar to the version 4 format except for
> the addition of a count for the key material.  This count helps
> parsing Secret Key packets (which are an extension of the Public Key
> packet format) in the case of an unknown algorithm.  In addition,
> fingerprints of version 6 keys are calculated differently from
> version 4 keys, as described in Section 5.5.4.

**N-247** (§5.5.2.3) — source lines 3165–3177

```
   A version 6 packet contains:

   *  A 1-octet version number (6).

   *  A 4-octet number denoting the time that the key was created.

   *  A 1-octet number denoting the public key algorithm of the key.

   *  A 4-octet scalar octet count for the public key material specified
      in the next field.

   *  A series of values comprising the public key material.  This is
      algorithm specific and described in Section 5.5.5.
```

### §5.5.3 Secret Key Packet Formats

**N-248** (§5.5.3) _[lowercase/implied]_ — source lines 3181–3183

> The Secret Key and Secret Subkey packets contain all the data of the
> Public Key and Public Subkey packets, with additional algorithm-
> specific secret key data appended, usually in encrypted form.

**N-249** (§5.5.3) — source lines 3185–3242

```
   The packet contains:

   *  The fields of a Public Key or Public Subkey packet, as described
      above.

   *  One octet (the "S2K usage octet") indicating whether and how the
      secret key material is protected by a passphrase.  Zero indicates
      that the secret key data is not encrypted.  253 (AEAD), 254 (CFB),
      or 255 (MalleableCFB) indicates that an S2K Specifier and other
      parameters will follow.  Any other value is a symmetric key
      encryption algorithm identifier.  A version 6 packet MUST NOT use
      the value 255 (MalleableCFB).

   *  Only for a version 6 packet where the secret key material is
      encrypted (that is, where the previous octet is not zero), a
      1-octet scalar octet count of the cumulative length of all the
      following conditionally included S2K parameter fields.

   *  Conditionally included S2K parameter fields:

      -  If the S2K usage octet was 253, 254, or 255, a 1-octet
         symmetric key encryption algorithm.

      -  If the S2K usage octet was 253 (AEAD), a 1-octet AEAD
         algorithm.

      -  Only for a version 6 packet, and if the S2K usage octet was 253
         or 254, a 1-octet count of the size of the one field following
         this octet.

      -  If the S2K usage octet was 253, 254, or 255, an S2K Specifier.
         The length of the S2K Specifier depends on its type (see
         Section 3.7.1).

      -  If the S2K usage octet was 253 (AEAD), an IV of a size
         specified by the AEAD algorithm (see Section 5.13.2), which is
         used as the nonce for the AEAD algorithm.

      -  If the S2K usage octet was 254, 255, or a cipher algorithm ID
         (that is, the secret data uses some form of CFB encryption), an
         IV of the same length as the cipher's block size.

   *  Plain or encrypted multiprecision integers comprising the secret
      key data.  This is algorithm specific and described in
      Section 5.5.5.  If the S2K usage octet is 253 (AEAD), then an AEAD
      authentication tag is at the end of that data.  If the S2K usage
      octet is 254 (CFB), a 20-octet SHA-1 hash of the plaintext of the
      algorithm-specific portion is appended to plaintext and encrypted
      with it.  If the S2K usage octet is 255 (MalleableCFB) or another
      non-zero value (that is, a symmetric key encryption algorithm
      identifier), a 2-octet checksum of the plaintext of the algorithm-
      specific portion (sum of all octets, mod 65536) is appended to
      plaintext and encrypted with it.  (This is deprecated and SHOULD
      NOT be used; see below.)

   *  Only for a version 3 or 4 packet where the S2K usage octet is
      zero, a 2-octet checksum of the algorithm-specific portion (sum of
      all octets, mod 65536).
```

_Lines 3244–3248, a pointer to Table 2 and the remark that the version 6 count values help parsing, are cross-reference and motivation and are omitted._

**N-250** (§5.5.3) — source lines 3250–3257

> Secret MPI values can be encrypted using a passphrase.  If an S2K
> Specifier is given, it describes the algorithm for converting the
> passphrase to a key; otherwise, a simple MD5 hash of the passphrase
> is used.  An implementation producing a passphrase-protected Secret
> Key packet MUST use an S2K Specifier; the simple hash is for read-
> only backward compatibility, though implementations MAY continue to
> use existing private keys in the old format.  The cipher for
> encrypting the MPIs is specified in the Secret Key packet.

**N-251** (§5.5.3) _[lowercase/implied]_ — source lines 3259–3267

> Encryption/decryption of the secret data is done using the key
> created from the passphrase and the IV from the packet.  If the S2K
> usage octet is not 253, CFB mode is used.  A different mode is used
> with version 3 keys (which are only RSA) than with other key formats.
> With version 3 keys, the MPI bit count prefix (that is, the first two
> octets) is not encrypted.  Only the MPI non-prefix data is encrypted.
> Furthermore, the CFB state is resynchronized at the beginning of each
> new MPI value so that the CFB block boundary is aligned with the
> start of the MPI data.

**N-252** (§5.5.3) _[lowercase/implied]_ — source lines 3269–3270

> With version 4 and version 6 keys, a simpler method is used.  All
> secret MPI values are encrypted, including the MPI bit count prefix.

**N-253** (§5.5.3) _[lowercase/implied]_ — source lines 3272–3278

> If the S2K usage octet is 253, the KEK is derived using HKDF
> [RFC5869] to provide key separation.  SHA256 [RFC6234] is used as the
> hash algorithm for HKDF.  IKM for HKDF is the key derived from S2K.
> No salt is used.  The info parameter is comprised of the Packet Type
> ID encoded in OpenPGP format (bits 7 and 6 are set, and bits 5-0
> carry the Packet Type ID), the packet version, and the cipher-algo
> and AEAD-mode used to encrypt the key material.

**N-254** (§5.5.3) _[lowercase/implied]_ — source lines 3280–3294

> Then, the encrypted MPI values are encrypted as one combined
> plaintext using one of the AEAD algorithms specified for the version
> 2 Symmetrically Encrypted and Integrity Protected Data packet.  Note
> that no chunks are used and that there is only one authentication
> tag.  As additional data, the Packet Type ID in OpenPGP format
> encoding (bits 7 and 6 are set, and bits 5-0 carry the Packet Type
> ID), followed by the Public Key packet fields, starting with the
> packet version number, are passed to the AEAD algorithm.  For
> example, the additional data used with a Secret Key packet of version
> 4 consists of the octets 0xC5, 0x04, followed by four octets of
> creation time, one octet denoting the public key algorithm, and the
> algorithm-specific public key parameters.  For a Secret Subkey
> packet, the first octet would be 0xC7.  For a version 6 key packet,
> the second octet would be 0x06, and the 4-octet octet count of the
> public key material would be included as well (see Section 5.5.2).

**N-255** (§5.5.3) — source lines 3296–3307

> The 2-octet checksum that follows the algorithm-specific portion is
> the algebraic sum, mod 65536, of the plaintext of all the algorithm-
> specific octets (including the MPI prefix and data).  With version 3
> keys, the checksum is stored in the clear.  With version 4 keys, the
> checksum is encrypted like the algorithm-specific data.  This value
> is used to check that the passphrase was correct.  However, this
> checksum is deprecated, and an implementation SHOULD NOT use it;
> instead, an implementation should use the SHA-1 hash denoted with a
> usage octet of 254.  The reason for this is that there are some
> attacks that involve modifying the secret key undetected.  If the S2K
> usage octet is 253, no checksum or SHA-1 hash is used, but the
> authentication tag of the AEAD algorithm follows.

**N-256** (§5.5.3) — source lines 3309–3316

> When decrypting the secret key material using any of these schemes
> (that is, where the usage octet is non-zero), the resulting cleartext
> octet stream must be well formed.  In particular, an implementation
> MUST NOT interpret octets beyond the unwrapped cleartext octet stream
> as part of any of the unwrapped MPI objects.  Furthermore, an
> implementation MUST reject any secret key material whose cleartext
> length does not align with the lengths of the unwrapped MPI objects
> as unusable.

### §5.5.4 Key IDs and Fingerprints

**N-257** (§5.5.4) _[lowercase/implied]_ — source lines 3320–3324

> Every OpenPGP Key has a fingerprint and a Key ID.  The computation of
> these values differs based on the key version.  The fingerprint
> length varies with the key version, but the Key ID (which is only
> used in v3 PKESK packets; see Section 5.1.1) is always 64 bits.  The
> following registry represents the subsections below:

**N-258** (§5.5.4) _[table]_ — source lines 3326–3344

```
   +=======+===================+===============+=============+=========+
   |Key    | Fingerprint       | Fingerprint   | Key ID      |Reference|
   |Version|                   | Length        |             |         |
   |       |                   | (Bits)        |             |         |
   +=======+===================+===============+=============+=========+
   |3      | MD5(MPIs without  | 128           | low 64 bits |Section  |
   |       | length octets)    |               | of RSA      |5.5.4.1  |
   |       |                   |               | modulus     |         |
   +-------+-------------------+---------------+-------------+---------+
   |4      | SHA1(normalized   | 160           | last 64     |Section  |
   |       | pubkey packet)    |               | bits of     |5.5.4.2  |
   |       |                   |               | fingerprint |         |
   +-------+-------------------+---------------+-------------+---------+
   |6      | SHA256(normalized | 256           | first 64    |Section  |
   |       | pubkey packet)    |               | bits of     |5.5.4.3  |
   |       |                   |               | fingerprint |         |
   +-------+-------------------+---------------+-------------+---------+

            Table 12: OpenPGP Key IDs and Fingerprints Registry
```

### §5.5.4.1 Version 3 Key ID and Fingerprint

**N-259** (§5.5.4.1) _[lowercase/implied]_ — source lines 3348–3349

> For a version 3 key, the 8-octet Key ID consists of the low 64 bits
> of the public modulus of the RSA key.

**N-260** (§5.5.4.1) _[lowercase/implied]_ — source lines 3351–3354

> The fingerprint of a version 3 key is formed by hashing the body (but
> not the 2-octet length) of the MPIs that form the key material
> (public modulus n, followed by exponent e) with MD5.  Note that both
> version 3 keys and MD5 are deprecated.

### §5.5.4.2 Version 4 Key ID and Fingerprint

**N-261** (§5.5.4.2) _[lowercase/implied]_ — source lines 3358–3362

> A version 4 fingerprint is the 160-bit SHA-1 hash of the octet 0x99,
> followed by the 2-octet packet length, followed by the entire Public
> Key packet starting with the version field.  The Key ID is the low-
> order 64 bits of the fingerprint.  Here are the fields of the hash
> material, including an example of an Ed25519 key:

**N-262** (§5.5.4.2) — source lines 3364–3378

```
   a.1)  0x99 (1 octet)

   a.2)  2-octet, big-endian scalar octet count of (b)-(e)

   b)  version number = 4 (1 octet)

   c)  timestamp of key creation (4 octets)

   d)  algorithm (1 octet): 27 = Ed25519 (example)

   e)  algorithm-specific fields

   Algorithm-specific fields for Ed25519 keys (example):

   e.1)  32 octets representing the public key
```

### §5.5.4.3 Version 6 Key ID and Fingerprint

**N-263** (§5.5.4.3) _[lowercase/implied]_ — source lines 3382–3386

> A version 6 fingerprint is the 256-bit SHA2-256 hash of the octet
> 0x9B, followed by the 4-octet packet length, followed by the entire
> Public Key packet starting with the version field.  The Key ID is the
> high-order 64 bits of the fingerprint.  Here are the fields of the
> hash material, including an example of an Ed25519 key:

**N-264** (§5.5.4.3) — source lines 3388–3405

```
   a.1)  0x9B (1 octet)

   a.2)  4-octet scalar octet count of (b)-(f)

   b)  version number = 6 (1 octet)

   c)  timestamp of key creation (4 octets)

   d)  algorithm (1 octet): 27 = Ed25519 (example)

   e)  4-octet scalar octet count for the key material specified in the
       next field

   f)  algorithm-specific public key material

   Algorithm-specific fields for Ed25519 keys (example):

   f.1)  32 octets representing the public key
```

_Lines 3407–3414, the notes that Key ID and fingerprint collisions are possible and that the same RSA material yields different Key IDs and fingerprints across key versions, are informative and are omitted._

**N-265** (§5.5.4.3) _[lowercase/implied]_ — source lines 3416–3419

> Finally, the Key ID and fingerprint of a subkey are calculated in the
> same way as for a primary key, including the 0x99 (version 4 key) or
> 0x9B (version 6 key) as the first octet (even though this is not a
> valid Packet Type ID for a public subkey).

### §5.5.5 Algorithm-Specific Parts of Keys

_Lines 3423–3424 are a one-sentence overview of the subsections and are omitted._

### §5.5.5.1 Algorithm-Specific Part for RSA Keys

**N-266** (§5.5.5.1) — source lines 3428–3443

```
   For RSA keys, the public key consists of this series of
   multiprecision integers:

   *  MPI of RSA public modulus n,

   *  MPI of RSA public encryption exponent e.

   The secret key consists of this series of multiprecision integers:

   *  MPI of RSA secret exponent d;

   *  MPI of RSA secret prime value p;

   *  MPI of RSA secret prime value q (p < q); and

   *  MPI of u, the multiplicative inverse of p, mod q.
```

### §5.5.5.2 Algorithm-Specific Part for DSA Keys

**N-267** (§5.5.5.2) — source lines 3447–3460

```
   For DSA keys, the public key consists of this series of
   multiprecision integers:

   *  MPI of DSA prime p;

   *  MPI of DSA group order q (q is a prime divisor of p-1);

   *  MPI of DSA group generator g; and

   *  MPI of DSA public key value y (= g^x mod p where x is secret).

   The secret key consists of this single multiprecision integer:

   *  MPI of DSA secret exponent x.
```

### §5.5.5.3 Algorithm-Specific Part for Elgamal Keys

**N-268** (§5.5.5.3) — source lines 3464–3475

```
   For Elgamal keys, the public key consists of this series of
   multiprecision integers:

   *  MPI of Elgamal prime p;

   *  MPI of Elgamal group generator g; and

   *  MPI of Elgamal public key value y (= g^x mod p where x is secret).

   The secret key consists of this single multiprecision integer:

   *  MPI of Elgamal secret exponent x.
```

### §5.5.5.4 Algorithm-Specific Part for ECDSA Keys

**N-269** (§5.5.5.4) — source lines 3479–3494

```
   For ECDSA keys, the public key consists of this series of values:

   *  A variable-length field containing a curve OID, which is formatted
      as follows:

      -  A 1-octet size of the following field; values 0 and 0xFF are
         reserved for future extensions.

      -  The octets representing a curve OID, as defined in Section 9.2.

   *  An MPI of an EC point representing a public key.

   The secret key consists of this single multiprecision integer:

   *  An MPI of an integer representing the secret key, which is a
      scalar of the public EC point.
```

### §5.5.5.5 Algorithm-Specific Part for EdDSALegacy Keys (Deprecated)

**N-270** (§5.5.5.5) — source lines 3498–3516

```
   For EdDSALegacy keys (deprecated), the public key consists of this
   series of values:

   *  A variable-length field containing a curve OID, formatted as
      follows:

      -  A 1-octet size of the following field; values 0 and 0xFF are
         reserved for future extensions.

      -  The octets representing a curve OID, as defined in Section 9.2.

   *  An MPI of an EC point representing a public key Q in prefixed
      native form (see Section 11.2.2).

   The secret key consists of this single multiprecision integer:

   *  An MPI-encoded octet string representing the native form of the
      secret key in the curve-specific format, as described in
      Section 9.2.1.
```

**N-271** (§5.5.5.5) _[lowercase/implied]_ — source lines 3518–3525

> Note that the native form for an EdDSA secret key is a fixed-width
> sequence of unstructured random octets, with size corresponding to
> the specific curve.  That sequence of random octets is used with a
> cryptographic digest to produce both a curve-specific secret scalar
> and a prefix used when making a signature.  See Section 5.1.5 of
> [RFC8032] for more details about how to use the native octet strings
> for Ed25519Legacy.  The value stored in an OpenPGP EdDSALegacy Secret
> Key packet is the original sequence of random octets.

**N-272** (§5.5.5.5) _[lowercase/implied]_ — source lines 3527–3528

> Note that the only curve defined for use with EdDSALegacy is the
> Ed25519Legacy OID.

### §5.5.5.6 Algorithm-Specific Part for ECDH Keys

**N-273** (§5.5.5.6) — source lines 3532–3562

```
   For ECDH keys, the public key consists of this series of values:

   *  A variable-length field containing a curve OID, which is formatted
      as follows:

      -  A 1-octet size of the following field; values 0 and 0xFF are
         reserved for future extensions.

      -  The octets representing a curve OID, as defined in Section 9.2.

   *  An MPI of an EC point representing a public key, in the point
      format associated with the curve, as specified in Section 9.2.1.

   *  A variable-length field containing key derivation function (KDF)
      parameters, which is formatted as follows:

      -  A 1-octet size of the following fields; values 0 and 0xFF are
         reserved for future extensions.

      -  A 1-octet value 1, reserved for future extensions.

      -  A 1-octet hash function ID used with a KDF.

      -  A 1-octet algorithm ID for the symmetric algorithm that is used
         to wrap the symmetric key for message encryption; see
         Section 11.5 for details.

   The secret key consists of this single multiprecision integer:

   *  An MPI representing the secret key, in the curve-specific format
      described in Section 9.2.1.
```

### §5.5.5.6.1 ECDH Secret Key Material

**N-274** (§5.5.5.6.1) _[lowercase/implied]_ — source lines 3566–3570

> When curve NIST P-256, NIST P-384, NIST P-521, brainpoolP256r1,
> brainpoolP384r1, or brainpoolP512r1 are used in ECDH, their secret
> keys are represented as a simple integer in standard MPI form.  Other
> curves are presented on the wire differently (though still as a
> single MPI), as described below and in Section 9.2.1.

### §5.5.5.6.1.1 Curve25519Legacy ECDH Secret Key Material (Deprecated)

**N-275** (§5.5.5.6.1.1) — source lines 3574–3577

> A Curve25519Legacy secret key is stored as a standard integer in big-
> endian MPI form.  Curve25519Legacy MUST NOT be used in key packets
> version 6 or above.  Note that this form is in reverse octet order
> from the little-endian "native" form found in [RFC7748].

**N-276** (§5.5.5.6.1.1) — source lines 3579–3584

> Note also that the integer for a Curve25519Legacy secret key for
> OpenPGP MUST have the appropriate form; that is, it MUST be divisible
> by 8, MUST be at least 2^254, and MUST be less than 2^255.  The
> length of this MPI in bits is by definition always 255, so the two
> leading octets of the MPI will always be 00 FF, and reversing the
> following 32 octets from the wire will produce the "native" form.

**N-277** (§5.5.5.6.1.1) _[lowercase/implied]_ _[code]_ — source lines 3586–3595

> When generating a new Curve25519Legacy secret key from 32 fully
> random octets, the following pseudocode produces the MPI wire format
> (note the similarity to decodeScalar25519 as described in [RFC7748]):

```
   def curve25519Legacy_MPI_from_random(octet_list):
       octet_list[0] &= 248
       octet_list[31] &= 127
       octet_list[31] |= 64
       mpi_header = [ 0x00, 0xFF ]
       return mpi_header || reversed(octet_list)
```

### §5.5.5.7 Algorithm-Specific Part for X25519 Keys

**N-278** (§5.5.5.7) — source lines 3599–3605

```
   For X25519 keys, the public key consists of this single value:

   *  32 octets of the native public key.

   The secret key consists of this single value:

   *  32 octets of the native secret key.
```

**N-279** (§5.5.5.7) _[lowercase/implied]_ — source lines 3607–3611

> See Section 6.1 of [RFC7748] for more details about how to use the
> native octet strings.  The value stored in an OpenPGP X25519 Secret
> Key packet is the original sequence of random octets.  The value
> stored in an OpenPGP X25519 Public Key packet is the value
> X25519(secretKey, 9).

### §5.5.5.8 Algorithm-Specific Part for X448 Keys

**N-280** (§5.5.5.8) — source lines 3615–3621

```
   For X448 keys, the public key consists of this single value:

   *  56 octets of the native public key.

   The secret key consists of this single value:

   *  56 octets of the native secret key.
```

**N-281** (§5.5.5.8) _[lowercase/implied]_ — source lines 3623–3626

> See Section 6.2 of [RFC7748] for more details about how to use the
> native octet strings.  The value stored in an OpenPGP X448 Secret Key
> packet is the original sequence of random octets.  The value stored
> in an OpenPGP X448 Public Key packet is the value X448(secretKey, 5).

### §5.5.5.9 Algorithm-Specific Part for Ed25519 Keys

**N-282** (§5.5.5.9) — source lines 3630–3636

```
   For Ed25519 keys, the public key consists of this single value:

   *  32 octets of the native public key.

   The secret key consists of this single value:

   *  32 octets of the native secret key.
```

**N-283** (§5.5.5.9) _[lowercase/implied]_ — source lines 3638–3640

> See Section 5.1.5 of [RFC8032] for more details about how to use the
> native octet strings.  The value stored in an OpenPGP Ed25519 Secret
> Key packet is the original sequence of random octets.

### §5.5.5.10 Algorithm-Specific Part for Ed448 Keys

**N-284** (§5.5.5.10) — source lines 3644–3650

```
   For Ed448 keys, the public key consists of this single value:

   *  57 octets of the native public key.

   The secret key consists of this single value:

   *  57 octets of the native secret key.
```

**N-285** (§5.5.5.10) _[lowercase/implied]_ — source lines 3652–3654

> See Section 5.2.5 of [RFC8032] for more details about how to use the
> native octet strings.  The value stored in an OpenPGP Ed448 Secret
> Key packet is the original sequence of random octets.

## §5.6 Compressed Data Packet (Type ID 8)

_Lines 3658–3661, where the packet is typically found, are overview and are omitted._

**N-286** (§5.6) — source lines 3663–3667

```
   The body of this packet consists of:

   *  One octet specifying the algorithm used to compress the packet.

   *  Compressed data, which makes up the remainder of the packet.
```

**N-287** (§5.6) _[lowercase/implied]_ — source lines 3669–3671

> A Compressed Data packet's body contains data that is a compression
> of a series of OpenPGP packets.  See Section 10 for details on how
> messages are formed.

**N-288** (§5.6) _[lowercase/implied]_ — source lines 3673–3680

> A ZIP-compressed series of packets is compressed into raw DEFLATE
> blocks [RFC1951].
>
> A ZLIB-compressed series of packets is compressed with raw ZLIB-style
> blocks [RFC1950].
>
> A BZip2-compressed series of packets is compressed using the BZip2
> [BZ2] algorithm.

**N-289** (§5.6) — source lines 3682–3685

> An implementation that generates a Compressed Data packet MUST use
> the OpenPGP format for packet framing (see Section 4.2.1).  It MUST
> NOT generate a Compressed Data packet with Legacy format
> (Section 4.2.2).

**N-290** (§5.6) — source lines 3687–3690

> An implementation that deals with either historic data or data
> generated by legacy implementations predating support for [RFC2440]
> MAY interpret Compressed Data packets that use the Legacy format for
> packet framing.

## §5.7 Symmetrically Encrypted Data Packet (Type ID 9)

**N-291** (§5.7) _[lowercase/implied]_ — source lines 3694–3698

> The Symmetrically Encrypted Data packet contains data encrypted with
> a symmetric key algorithm.  When it has been decrypted, it contains
> other packets (usually a Literal Data packet or compressed data
> packet, but in theory, it could be another sequence of packets that
> forms a valid OpenPGP Message).

**N-292** (§5.7) — source lines 3700–3704

> This packet is obsolete.  An implementation MUST NOT create this
> packet.  An implementation SHOULD reject such a packet and stop
> processing the message.  If an implementation chooses to process the
> packet anyway, it MUST return a clear warning that a non-integrity-
> protected packet has been processed.

_Lines 3706–3709, why the packet cannot be handled safely and a pointer to Section 13.7, are motivation and are omitted._

**N-293** (§5.7) — source lines 3711–3719

```
   The body of this packet consists of:

   *  A random prefix, containing block-size random octets (for example,
      16 octets for a 128-bit block length) followed by a copy of the
      last two octets, encrypted together using Cipher Feedback (CFB)
      mode, with an IV of all zeros.

   *  Data encrypted using CFB mode, with the last block-size octets of
      the first ciphertext as the IV.
```

**N-294** (§5.7) _[lowercase/implied]_ — source lines 3721–3727

> The symmetric cipher used may be specified in a Public Key or
> Symmetric Key Encrypted Session Key packet that precedes the
> Symmetrically Encrypted Data packet.  In that case, the cipher
> algorithm ID is prefixed to the session key before it is encrypted.
> If no packets of these types precede the encrypted data, the IDEA
> algorithm is used with the session key calculated as the MD5 hash of
> the passphrase, though this use is deprecated.

**N-295** (§5.7) _[lowercase/implied]_ — source lines 3729–3740

> The data is encrypted in CFB mode (see Section 12.9).  For the random
> prefix, the IV is specified as all zeros.  Instead of achieving
> randomized encryption through an IV, a string of length equal to the
> block size of the cipher plus two is encrypted for this purpose.  The
> first block-size octets (for example, 16 octets for a 128-bit block
> length) are random, and the following two octets are copies of the
> last two octets of the first block-size random octets.  For example,
> for a 16-octet block length, octet 17 is a copy of octet 15, and
> octet 18 is a copy of octet 16.  For a cipher of block length 8,
> octet 9 is a copy of octet 7, and octet 10 is a copy of octet 8.  (In
> both of these examples, we consider the first octet to be numbered
> 1.)

**N-296** (§5.7) _[lowercase/implied]_ — source lines 3742–3747

> After encrypting these block-size-plus-two octets, a new CFB context
> is created for the encryption of the data, with the last block-size
> octets of the first ciphertext as the IV.  (Alternatively and
> equivalently, the CFB state is resynchronized: the last block-size
> octets of ciphertext are passed through the cipher, and the block
> boundary is reset.)

**N-297** (§5.7) _[lowercase/implied]_ — source lines 3749–3751

> The repetition of two octets in the random prefix allows the receiver
> to immediately check whether the session key is incorrect.  See
> Section 13.4 for hints on the proper use of this "quick check".

## §5.8 Marker Packet (Type ID 10)

**N-298** (§5.8) — source lines 3755–3757

```
   The body of the Marker packet consists of:

   *  The three octets 0x50, 0x47, 0x50 (which spell "PGP" in UTF-8).
```

**N-299** (§5.8) — source line 3759

> Such a packet MUST be ignored when received.

## §5.9 Literal Data Packet (Type ID 11)

**N-300** (§5.9) _[lowercase/implied]_ — source lines 3763–3764

> A Literal Data packet contains the body of a message; that is, data
> that is not to be further interpreted.

**N-301** (§5.9) — source lines 3766–3806

```
   The body of this packet consists of:

   *  A 1-octet field that describes how the data is formatted.

      If it is a b (0x62), then the Literal Data packet contains binary
      data.  If it is a u (0x75), then the Literal Data packet contains
      UTF-8-encoded text data and thus may need line ends converted to
      local form or other text mode changes.

      Previous versions of the OpenPGP specification used t (0x74) to
      indicate textual data but did not specify the character encoding.
      Implementations SHOULD NOT emit this value.  An implementation
      that receives a Literal Data packet with this value in the format
      field SHOULD interpret the packet data as UTF-8 encoded text,
      unless reliable (not attacker-controlled) context indicates a
      specific alternate text encoding.  This mode is deprecated due to
      its ambiguity.

      Some implementations predating [RFC2440] also defined a value of l
      as a "local" mode for machine-local conversions.  [RFC1991]
      incorrectly states that this local mode flag is 1 (ASCII numeral
      one).  Both of these local modes are deprecated.

   *  The file name as a string (1-octet length, followed by a file
      name).  This may be a zero-length string.  Commonly, if the source
      of the encrypted data is a file, it will be the name of the
      encrypted file.  An implementation MAY consider the file name in
      the Literal Data packet to be a more authoritative name than the
      actual file name.

   *  A 4-octet number that indicates a date associated with the literal
      data.  Commonly, the date might be the modification date of a
      file, or the time the packet was created, or a zero that indicates
      no specific time.

   *  The remainder of the packet is literal data.

      Text data MUST be encoded with UTF-8 (see [RFC3629]) and stored
      with <CR><LF> text endings (that is, network-normal line endings).
      These should be converted to native line endings by the receiving
      implementation.
```

**N-302** (§5.9) — source lines 3808–3814

> Note that OpenPGP signatures do not include the formatting octet, the
> file name, and the date field of the Literal Data packet in a
> signature hash; therefore, those fields are not protected against
> tampering in a signed document.  A receiving implementation MUST NOT
> treat those fields as though they were cryptographically secured by
> the surrounding signature when either representing them to the user
> or acting on them.

**N-303** (§5.9) — source lines 3816–3824

> Due to their inherent malleability, an implementation that generates
> a Literal Data packet SHOULD avoid storing any significant data in
> these fields.  If the implementation is certain that the data is
> textual and is encoded with UTF-8 (for example, if it will follow
> this Literal Data packet with a Signature packet of type 0x01 (see
> Section 5.2.1), it MAY set the format octet to u.  Otherwise, it MUST
> set the format octet to b.  It SHOULD set the filename to the empty
> string (encoded as a single zero octet) and the timestamp to zero
> (encoded as four zero octets).

**N-304** (§5.9) _[lowercase/implied]_ — source lines 3826–3828

> An application that wishes to include such filesystem metadata within
> a signature is advised to sign an encapsulated archive (for example,
> [PAX]).

**N-305** (§5.9) — source lines 3830–3832

> An implementation that generates a Literal Data packet MUST use the
> OpenPGP format for packet framing (see Section 4.2.1).  It MUST NOT
> generate a Literal Data packet with Legacy format (Section 4.2.2).

**N-306** (§5.9) — source lines 3834–3837

> An implementation that deals with either historic data or data
> generated by an implementation that predates support for [RFC2440]
> MAY interpret Literal Data packets that use the Legacy format for
> packet framing.

### §5.9.1 Special Filename _CONSOLE (Deprecated)

**N-307** (§5.9.1) _[lowercase/implied]_ — source lines 3841–3846

> The Literal Data packet's filename field has a historical special
> case for the special name _CONSOLE.  When the filename field is
> _CONSOLE, the message is considered to be "for your eyes only".  This
> advises that the message data is unusually sensitive, and the
> receiving program should process it more carefully, perhaps avoiding
> storing the received data to disk, for example.

**N-308** (§5.9.1) — source lines 3848–3851

> An OpenPGP deployment that generates Literal Data packets MUST NOT
> depend on this indicator being honored in any particular way.  It
> cannot be enforced, and the field itself is not covered by any
> cryptographic signature.

**N-309** (§5.9.1) — source lines 3853–3854

> It is NOT RECOMMENDED to use this special filename in a newly
> generated Literal Data packet.

## §5.10 Trust Packet (Type ID 12)

**N-310** (§5.10) _[lowercase/implied]_ — source lines 3858–3863

> The Trust packet is used only within keyrings and is not normally
> exported.  Trust packets contain data that record the user's
> specifications of which keyholders are trustworthy introducers, along
> with other information that implementation uses for trust
> information.  The format of Trust packets is defined by a given
> implementation.

**N-311** (§5.10) — source lines 3865–3867

> Trust packets SHOULD NOT be emitted to output streams that are
> transferred to other users, and they SHOULD be ignored on any input
> other than local keyring files.

## §5.11 User ID Packet (Type ID 13)

**N-312** (§5.11) _[lowercase/implied]_ — source lines 3871–3875

> A User ID packet consists of UTF-8 text that is intended to represent
> the name and email address of the keyholder.  By convention, it
> includes a mail name-addr as described in [RFC2822], but there are no
> restrictions on its content.  The packet length in the header
> specifies the length of the User ID.

## §5.12 User Attribute Packet (Type ID 17)

**N-313** (§5.12) _[lowercase/implied]_ — source lines 3879–3884

> The User Attribute packet is a variation of the User ID packet.  It
> is capable of storing more types of data than the User ID packet,
> which is limited to text.  Like the User ID packet, a User Attribute
> packet may be certified by the key owner ("self-signed") or any other
> key owner who cares to certify it.  Except as noted, a User Attribute
> packet may be used anywhere that a User ID packet may be used.

**N-314** (§5.12) — source lines 3886–3891

> While User Attribute packets are not a required part of the OpenPGP
> specification, implementations SHOULD provide at least enough
> compatibility to properly handle a certification signature on the
> User Attribute packet.  A simple way to do this is by treating the
> User Attribute packet as a User ID packet with opaque contents, but
> an implementation may use any method desired.

**N-315** (§5.12) — source lines 3893–3901

```
   The User Attribute packet is made up of one or more attribute
   subpackets.  Each subpacket consists of a subpacket header and a
   body.  The header consists of:

   *  the subpacket length (1, 2, or 5 octets)

   *  the Subpacket Type ID (1 octet)

   and is followed by the subpacket specific data.
```

**N-316** (§5.12) _[table]_ — source lines 3903–3915

```
   The following table lists the currently known subpackets:

        +=========+=============================+================+
        |      ID | Attribute Subpacket         | Reference      |
        +=========+=============================+================+
        |       0 | Reserved                    |                |
        +---------+-----------------------------+----------------+
        |       1 | Image Attribute Subpacket   | Section 5.12.1 |
        +---------+-----------------------------+----------------+
        | 100-110 | Private or Experimental Use |                |
        +---------+-----------------------------+----------------+

        Table 13: OpenPGP User Attribute Subpacket Types Registry
```

**N-317** (§5.12) — source lines 3917–3918

> An implementation SHOULD ignore any subpacket of a type that it does
> not recognize.

### §5.12.1 Image Attribute Subpacket

**N-318** (§5.12.1) _[lowercase/implied]_ — source lines 3922–3923

> The Image Attribute subpacket is used to encode an image, presumably
> (but not required to be) that of the key owner.

**N-319** (§5.12.1) _[lowercase/implied]_ — source lines 3925–3933

> The Image Attribute subpacket begins with an image header.  The first
> two octets of the image header contain the length of the image
> header.  Note that unlike other multi-octet numerical values in this
> document, due to a historical accident, this value is encoded as a
> little-endian number.  The image header length is followed by a
> single octet for the image header version.  The only currently
> defined version of the image header is 1, which is a 16-octet image
> header.  The first three octets of a version 1 image header are thus
> 0x10, 0x00, 0x01.

**N-320** (§5.12.1) _[table]_ — source lines 3935–3943

```
                       +=========+================+
                       | Version | Reference      |
                       +=========+================+
                       |       1 | Section 5.12.1 |
                       +---------+----------------+

                         Table 14: OpenPGP Image
                            Attribute Versions
                                 Registry
```

**N-321** (§5.12.1) — source lines 3945–3950

> The fourth octet of a version 1 image header designates the encoding
> format of the image.  The only currently defined encoding format is
> the value 1 to indicate JPEG.  Image format IDs 100 through 110 are
> reserved for Private or Experimental Use. The rest of the version 1
> image header is made up of 12 reserved octets, all of which MUST be
> set to 0.

**N-322** (§5.12.1) _[table]_ — source lines 3952–3963

```
                 +=========+=============================+
                 |      ID | Encoding                    |
                 +=========+=============================+
                 |       0 | Reserved                    |
                 +---------+-----------------------------+
                 |       1 | JPEG [JFIF]                 |
                 +---------+-----------------------------+
                 | 100-110 | Private or Experimental Use |
                 +---------+-----------------------------+

                     Table 15: OpenPGP Image Attribute
                          Encoding Format Registry
```

**N-323** (§5.12.1) _[lowercase/implied]_ — source lines 3965–3968

> The rest of the image subpacket contains the image itself.  As the
> only currently defined image type is JPEG, the image is encoded in
> the JPEG File Interchange Format (JFIF), a standard file format for
> JPEG images [JFIF].

**N-324** (§5.12.1) — source lines 3970–3973

> An implementation MAY try to determine the type of an image by
> examination of the image data if it is unable to handle a particular
> version of the image header or if a specified encoding format value
> is not recognized.

## §5.13 Symmetrically Encrypted and Integrity Protected Data Packet (Type ID 18)

**N-325** (§5.13) _[lowercase/implied]_ — source lines 3978–3980

> The SEIPD packet contains integrity-protected and encrypted data.
> When it has been decrypted, it will contain other packets forming an
> OpenPGP Message (see Section 10.3).

**N-326** (§5.13) _[lowercase/implied]_ — source lines 3982–3992

> The first octet of this packet is always used to indicate the version
> number, but different versions contain ciphertext that is structured
> differently.  Version 1 of this packet contains data encrypted with a
> symmetric key algorithm and is thus protected against modification by
> the SHA-1 hash algorithm.  This mechanism was introduced in [RFC4880]
> and offers some protections against ciphertext malleability.
>
> Version 2 of this packet contains data encrypted with an AEAD
> construction.  This offers a more cryptographically rigorous defense
> against ciphertext malleability.  See Section 13.7 for more details
> on choosing between these formats.

**N-327** (§5.13) _[lowercase/implied]_ — source lines 3994–3995

> Any new version of the SEIPD packet should be registered in the
> registry established in Section 10.3.2.1.

### §5.13.1 Version 1 Symmetrically Encrypted and Integrity Protected Data Packet Format

**N-328** (§5.13.1) — source lines 4000–4006

```
   A version 1 Symmetrically Encrypted and Integrity Protected Data
   packet consists of:

   *  A 1-octet version number with value 1.

   *  Encrypted data -- the output of the selected symmetric key cipher
      operating in CFB mode.
```

**N-329** (§5.13.1) — source lines 4008–4012

> The symmetric cipher used MUST be specified in a Public Key or
> Symmetric Key Encrypted Session Key packet that precedes the
> Symmetrically Encrypted and Integrity Protected Data packet.  In
> either case, the cipher algorithm ID is prefixed to the session key
> before it is encrypted.

**N-330** (§5.13.1) _[lowercase/implied]_ — source lines 4014–4026

> The data is encrypted in CFB mode (see Section 12.9).  The IV is
> specified as all zeros.  Instead of achieving randomized encryption
> through an IV, OpenPGP prefixes an octet string to the data before it
> is encrypted for this purpose.  The length of the octet string equals
> the block size of the cipher in octets, plus two.  The first octets
> in the group, of length equal to the block size of the cipher, are
> random; the last two octets are each copies of their 2nd preceding
> octet.  For example, with a cipher whose block size is 128 bits or 16
> octets, the prefix data will contain 16 random octets, then two more
> octets, which are copies of the 15th and 16th octets, respectively.
> Unlike the deprecated Symmetrically Encrypted Data packet
> (Section 5.7), this prefix data is encrypted in the same CFB context,
> and no special CFB resynchronization is done.

**N-331** (§5.13.1) _[lowercase/implied]_ — source lines 4028–4031

> The repetition of 16 bits in the random data prefixed to the message
> allows the receiver to immediately check whether the session key is
> incorrect.  See Section 13.4 for hints on the proper use of this
> "quick check".

**N-332** (§5.13.1) _[lowercase/implied]_ — source lines 4033–4041

> Two constant octets with the values 0xD3 and 0x14 are appended to the
> plaintext.  Then, the plaintext of the data to be encrypted is passed
> through the SHA-1 hash function.  The input to the hash function is
> comprised of the prefix data described above and all of the
> plaintext, including the trailing constant octets 0xD3, 0x14.  The 20
> octets of the SHA-1 hash are then appended to the plaintext (after
> the constant octets 0xD3, 0x14) and encrypted along with the
> plaintext using the same CFB context.  This trailing checksum is
> known as the Modification Detection Code (MDC).

**N-333** (§5.13.1) — source lines 4043–4049

> During decryption, the plaintext data should be hashed with SHA-1,
> including the prefix data as well as the trailing constant octets
> 0xD3, 0x14, but excluding the last 20 octets containing the SHA-1
> hash.  The computed SHA-1 hash is then compared with the last 20
> octets of plaintext.  A mismatch of the hash indicates that the
> message has been modified and MUST be treated as a security problem.
> Any failure SHOULD be reported to the user.

_Lines 4051–4105, the block headed NON-NORMATIVE EXPLANATION (the rationale for the MDC system and its fixed use of SHA-1), are non-normative by their own label and are omitted._

### §5.13.2 Version 2 Symmetrically Encrypted and Integrity Protected Data Packet Format

**N-334** (§5.13.2) — source lines 4110–4127

```
   A version 2 Symmetrically Encrypted and Integrity Protected Data
   packet consists of:

   *  A 1-octet version number with value 2.

   *  A 1-octet cipher algorithm ID.

   *  A 1-octet AEAD algorithm identifier.

   *  A 1-octet chunk size.

   *  32 octets of salt.  The salt is used to derive the message key and
      MUST be securely generated (see Section 13.10).

   *  Encrypted data; that is, the output of the selected symmetric key
      cipher operating in the given AEAD mode.

   *  A final summary authentication tag for the AEAD mode.
```

**N-335** (§5.13.2) _[lowercase/implied]_ — source lines 4129–4139

> The decrypted session key and the salt are used to derive an M-bit
> message key and N-64 bits used as the IV, where M is the key size of
> the symmetric algorithm and N is the nonce size of the AEAD
> algorithm.  M + N - 64 bits are derived using HKDF (see [RFC5869]).
> The leftmost M bits are used as a symmetric algorithm key, and the
> remaining N - 64 bits are used as an IV.  HKDF is used with SHA256
> [RFC6234] as hash algorithm.  The session key is used as IKM and the
> salt as salt.  The Packet Type ID in OpenPGP format encoding (bits 7
> and 6 are set, and bits 5-0 carry the Packet Type ID), version
> number, cipher algorithm ID, AEAD algorithm ID, and chunk size octet
> are used as info parameter.

_Lines 4141–4146, the key-separation rationale and the reply-with-a-new-salt use (pointer to Section 13.8), are motivation and are omitted._

**N-336** (§5.13.2) _[lowercase/implied]_ — source lines 4148–4150

> A v2 SEIPD packet consists of one or more chunks of data.  The
> plaintext of each chunk is of a size specified by the chunk size
> octet using the method specified below.

**N-337** (§5.13.2) _[lowercase/implied]_ — source lines 4152–4156

> The encrypted data consists of the encryption of each chunk of
> plaintext, followed immediately by the relevant authentication tag.
> If the last chunk of plaintext is smaller than the chunk size, the
> ciphertext for that data may be shorter; nevertheless, it is followed
> by a full authentication tag.

**N-338** (§5.13.2) _[lowercase/implied]_ — source lines 4158–4164

> For each chunk, the AEAD construction is given the Packet Type ID
> encoded in OpenPGP format (bits 7 and 6 are set, and bits 5-0 carry
> the Packet Type ID), version number, cipher algorithm ID, AEAD
> algorithm ID, and chunk size octet as additional data.  For example,
> the additional data of the first chunk using EAX and AES-128 with a
> chunk size of 2^22 octets consists of the octets 0xD2, 0x02, 0x07,
> 0x01, and 0x10.

**N-339** (§5.13.2) _[lowercase/implied]_ — source lines 4166–4170

> After the final chunk, the AEAD algorithm is used to produce a final
> authentication tag encrypting the empty string.  This AEAD instance
> is given the additional data specified above, plus an 8-octet, big-
> endian value specifying the total number of plaintext octets
> encrypted.  This allows detection of a truncated ciphertext.

**N-340** (§5.13.2) _[lowercase/implied]_ _[code]_ — source lines 4172–4175

> The chunk size octet specifies the size of chunks using the following
> formula (in C [C99]), where c is the chunk size octet:

```
     chunk_size = (uint32_t) 1 << (c + 6)
```

**N-341** (§5.13.2) — source lines 4177–4179

> An implementation MUST accept chunk size octets with values from 0 to
> 16.  An implementation MUST NOT create data with a chunk size octet
> value larger than 16 (4 MiB chunks).

**N-342** (§5.13.2) _[lowercase/implied]_ — source lines 4181–4184

> The nonce for AEAD mode consists of two parts.  Let N be the size of
> the nonce.  The leftmost N - 64 bits are the IV derived using HKDF.
> The rightmost 64 bits are the chunk index as a big-endian value.  The
> index of the first chunk is zero.

### §5.13.3 EAX Mode

**N-343** (§5.13.3) _[lowercase/implied]_ — source lines 4188–4192

> The EAX AEAD algorithm used in this document is defined in [EAX].
>
> The EAX algorithm can only use block ciphers with 16-octet blocks.
> The nonce is 16 octets long.  EAX authentication tags are 16 octets
> long.

### §5.13.4 OCB Mode

**N-344** (§5.13.4) _[lowercase/implied]_ — source lines 4196–4200

> The OCB AEAD algorithm used in this document is defined in [RFC7253].
>
> The OCB algorithm can only use block ciphers with 16-octet blocks.
> The nonce is 15 octets long.  OCB authentication tags are 16 octets
> long.

### §5.13.5 GCM Mode

**N-345** (§5.13.5) _[lowercase/implied]_ — source lines 4204–4209

> The GCM AEAD algorithm used in this document is defined in
> [SP800-38D].
>
> The GCM algorithm can only use block ciphers with 16-octet blocks.
> The nonce is 12 octets long.  GCM authentication tags are 16 octets
> long.

## §5.14 Padding Packet (Type ID 21)

**N-346** (§5.14) _[lowercase/implied]_ — source lines 4213–4215

> The Padding packet contains random data and can be used to defend
> against traffic analysis (see Section 13.11) on v2 SEIPD messages
> (see Section 5.13.2) and Transferable Public Keys (see Section 10.1).

**N-347** (§5.14) — source line 4217

> Such a packet MUST be ignored when received.

**N-348** (§5.14) — source lines 4219–4220

> Its contents SHOULD be random octets to make the length obfuscation
> it provides more robust even when compressed.

**N-349** (§5.14) — source lines 4222–4230

```
   An implementation adding padding to an OpenPGP stream SHOULD place
   such a packet:

   *  At the end of a version 6 Transferable Public Key that is
      transferred over an encrypted channel (see Section 10.1).

   *  As the last packet of an Optionally Padded Message within a
      version 2 Symmetrically Encrypted and Integrity Protected Data
      packet (see Section 10.3.1).
```

**N-350** (§5.14) — source lines 4232–4234

> An implementation MUST be able to process Padding packets anywhere
> else in an OpenPGP stream so that future revisions of this document
> may specify further locations for padding.

_Lines 4236–4237 state that padding-size policy is beyond the scope of the document and are omitted._

## §6 Base64 Conversions

_Lines 4241–4250 (why OpenPGP has a printable encoding) are motivation and are omitted._

**N-351** (§6) _[lowercase/implied]_ — source lines 4252–4255

> The encoding is composed of two parts: a base64 encoding of the
> binary data and an optional checksum.  The base64 encoding used is
> described in Section 4 of [RFC4648], and it is wrapped into lines of
> no more than 76 characters each.

**N-352** (§6) — source lines 4257–4258

> When decoding base64, an OpenPGP implementation MUST ignore all
> whitespace.

### §6.1 Optional Checksum

**N-353** (§6.1) _[lowercase/implied]_ — source lines 4262–4268

> The optional checksum is a 24-bit Cyclic Redundancy Check (CRC)
> converted to four characters of base64 encoding by the same MIME
> base64 transformation, preceded by an equal sign (=).  The CRC is
> computed by using the generator 0x864CFB and an initialization of
> 0xB704CE.  The accumulation is done on the data before it is
> converted to base64 rather than on the converted data.  A sample
> implementation of this algorithm is in Section 6.1.1.

**N-354** (§6.1) — source lines 4270–4271

> If present, the checksum with its leading equal sign MUST appear on
> the next line after the base64-encoded data.

**N-355** (§6.1) — source lines 4273–4277

> An implementation MUST NOT reject an OpenPGP object when the CRC24
> footer is present, missing, malformed, or disagrees with the computed
> CRC24 sum.  When forming ASCII Armor, the CRC24 footer SHOULD NOT be
> generated, unless interoperability with implementations that require
> the CRC24 footer to be present is a concern.

**N-356** (§6.1) — source lines 4279–4294

> The CRC24 footer MUST NOT be generated if it can be determined by the
> context or by the OpenPGP object being encoded that the consuming
> implementation accepts base64-encoded blocks without a CRC24 footer.
> Notably:
>
> *  An ASCII-armored Encrypted Message packet sequence that ends in a
>    v2 SEIPD packet MUST NOT contain a CRC24 footer.
>
> *  An ASCII-armored sequence of Signature packets that only includes
>    version 6 Signature packets MUST NOT contain a CRC24 footer.
>
> *  An ASCII-armored Transferable Public Key packet sequence of a
>    version 6 key MUST NOT contain a CRC24 footer.
>
> *  An ASCII-armored keyring consisting of only version 6 keys MUST
>    NOT contain a CRC24 footer.

_Lines 4296–4301 (rationale for discouraging the CRC24 footer) are history and motivation and are omitted._

### §6.1.1 An Implementation of the CRC24 in "C"

**N-357** (§6.1.1) _[code]_ _[lowercase/implied]_ — source lines 4305–4326

```
   The following code is written in [C99].

   #define CRC24_INIT 0xB704CEL
   #define CRC24_GENERATOR 0x864CFBL

   typedef unsigned long crc24;
   crc24 crc_octets(unsigned char *octets, size_t len)
   {
       crc24 crc = CRC24_INIT;
       int i;
       while (len--) {
           crc ^= (*octets++) << 16;
           for (i = 0; i < 8; i++) {
               crc <<= 1;
               if (crc & 0x1000000) {
                   crc &= 0XFFFFFF; /* Clear bit 25 to avoid overflow */
                   crc ^= CRC24_GENERATOR;
               }
           }
       }
       return crc & 0xFFFFFFL;
   }
```

### §6.2 Forming ASCII Armor

**N-358** (§6.2) — source lines 4330–4334

> When OpenPGP encodes data into ASCII Armor, it puts specific headers
> around the base64-encoded data, so OpenPGP can reconstruct the data
> later.  An OpenPGP implementation MAY use ASCII Armor to protect raw
> binary data.  OpenPGP informs the user what kind of data is encoded
> in the ASCII Armor through the use of the headers.

**N-359** (§6.2) _[lowercase/implied]_ — source lines 4336–4348

> Concatenating the following data creates ASCII Armor:
>
> *  An Armor Header Line, appropriate for the type of data
>
> *  Armor Headers
>
> *  A blank (zero length or containing only whitespace) line
>
> *  The ASCII-Armored data
>
> *  An optional Armor Checksum (discouraged; see Section 6.1)
>
> *  The Armor Tail, which depends on the Armor Header Line

### §6.2.1 Armor Header Line

**N-360** (§6.2.1) _[lowercase/implied]_ — source lines 4352–4356

> An Armor Header Line consists of the appropriate header line text
> surrounded by five (5) dashes (-, 0x2D) on either side of the header
> line text.  The header line text is chosen based on the type of data
> being encoded in Armor and how it is being encoded.  Header line
> texts include the following strings:

**N-361** (§6.2.1) _[table]_ — source lines 4358–4374

```
    +===================+============================================+
    | Armor Header      | Use                                        |
    +===================+============================================+
    | BEGIN PGP MESSAGE | Used for signed, encrypted, or compressed  |
    |                   | files.                                     |
    +-------------------+--------------------------------------------+
    | BEGIN PGP PUBLIC  | Used for armoring public keys.             |
    | KEY BLOCK         |                                            |
    +-------------------+--------------------------------------------+
    | BEGIN PGP PRIVATE | Used for armoring private keys.            |
    | KEY BLOCK         |                                            |
    +-------------------+--------------------------------------------+
    | BEGIN PGP         | Used for detached signatures, OpenPGP/MIME |
    | SIGNATURE         | signatures, and cleartext signatures.      |
    +-------------------+--------------------------------------------+

              Table 16: OpenPGP Armor Header Lines Registry
```

**N-362** (§6.2.1) — source lines 4376–4379

> Note that all of these Armor Header Lines are to consist of a
> complete line.  Therefore, the header lines MUST start at the
> beginning of a line and MUST NOT have text other than whitespace
> following them on the same line.

### §6.2.2 Armor Headers

**N-363** (§6.2.2) _[lowercase/implied]_ — source lines 4383–4387

> The Armor Headers are pairs of strings that can give the user or the
> receiving OpenPGP implementation some information about how to decode
> or use the message.  The Armor Headers are a part of the armor, not
> the message, and hence are not protected by any signatures applied to
> the message.

**N-364** (§6.2.2) — source lines 4389–4394

> The format of an Armor Header is that of a key-value pair.  A colon
> (: 0x3A) and a single space (0x20) separate the key and value.  An
> OpenPGP implementation may consider improperly formatted Armor
> Headers to be a corruption of the ASCII Armor, but it SHOULD make an
> effort to recover.  Unknown keys should be silently ignored, and an
> OpenPGP implementation SHOULD continue to process the message.

_Lines 4396–4398 (an example of a transport line-length limit) are informative and are omitted._

**N-365** (§6.2.2) _[lowercase/implied]_ — source lines 4400–4405

> While there is a limit of 76 characters for the base64 data
> (Section 6), there is no limit for the length of Armor Headers.  Care
> should be taken to ensure that the Armor Headers are short enough to
> survive transport.  One way to do this is to repeat an Armor Header
> Key multiple times with different values for each so that no one line
> is overly long.

**N-366** (§6.2.2) _[table]_ — source lines 4407–4422

```
   Currently defined Armor Header Keys are as follows:

       +=========+==============================+=================+
       | Key     | Summary                      | Reference       |
       +=========+==============================+=================+
       | Version | Implementation information   | Section 6.2.2.1 |
       +---------+------------------------------+-----------------+
       | Comment | Arbitrary text               | Section 6.2.2.2 |
       +---------+------------------------------+-----------------+
       | Hash    | Hash algorithms used in some | Section 6.2.2.3 |
       |         | v4 cleartext signed messages |                 |
       +---------+------------------------------+-----------------+
       | Charset | Character set                | Section 6.2.2.4 |
       +---------+------------------------------+-----------------+

               Table 17: OpenPGP Armor Header Keys Registry
```

### §6.2.2.1 "Version" Armor Header

**N-367** (§6.2.2.1) — source lines 4426–4429

> The Armor Header Key Version describes the OpenPGP implementation and
> version used to encode the message.  To minimize metadata,
> implementations SHOULD NOT emit this key and its corresponding value
> except for debugging purposes with explicit user consent.

### §6.2.2.2 "Comment" Armor Header

**N-368** (§6.2.2.2) _[lowercase/implied]_ — source lines 4433–4438

> The Armor Header Key Comment supplies a user-defined comment.
> OpenPGP defines all text to be in UTF-8.  A comment may be any UTF-8
> string.  However, the whole point of armoring is to provide 7-bit
> clean data.  Consequently, if a comment has characters that are
> outside the ASCII range of UTF-8, they may very well not survive
> transport.

### §6.2.2.3 "Hash" Armor Header

**N-369** (§6.2.2.3) — source lines 4442–4453

> The Armor Header Key Hash is deprecated, but some older
> implementations expect it in messages using the Cleartext Signature
> Framework (Section 7).  When present, this Armor Header Key contains
> a comma-separated list of hash algorithms used in the signatures on
> message, with digest names as specified in the "Text Name" column in
> Table 23.  These headers SHOULD NOT be emitted unless:
>
> *  the cleartext signed message contains a version 4 signature made
>    using a SHA2-based digest (SHA224, SHA256, SHA384, or SHA512), and
>
> *  the cleartext signed message might be verified by a legacy OpenPGP
>    implementation that requires this header.

**N-370** (§6.2.2.3) — source lines 4455–4460

> A verifying application MUST decline to validate any signature in a
> message with a non-conformant Hash header (that is, a Hash header
> that contains anything other than a comma-separated list of hash
> algorithms).  When a conformant Hash header is present, a verifying
> application MUST ignore its contents, deferring to the hash algorithm
> indicated in the Embedded Signature.

### §6.2.2.4 "Charset" Armor Header

**N-371** (§6.2.2.4) — source lines 4464–4474

> The Armor Header Key Charset contains a description of the character
> set that the plaintext is in (see [RFC2978]).  Please note that
> OpenPGP defines text to be in UTF-8.  An implementation will get the
> best results by translating into and out of UTF-8.  However, there
> are many instances where this is easier said than done.  Also, there
> are communities of users who have no need for UTF-8 because they are
> all happy with a character set like ISO Latin-5 or a Japanese
> character set.  In such instances, an implementation MAY override the
> UTF-8 default by using this header key.  An implementation MAY
> implement this key and any translations it cares to; an
> implementation MAY ignore it and assume all text is UTF-8.

### §6.2.3 Armor Tail Line

**N-372** (§6.2.3) _[lowercase/implied]_ — source lines 4478–4480

> The Armor Tail Line is composed in the same manner as the Armor
> Header Line, except the string "BEGIN" is replaced by the string
> "END".

## §7 Cleartext Signature Framework

**N-373** (§7) _[lowercase/implied]_ — source lines 4484–4491

> It is desirable to be able to sign a textual octet stream without
> ASCII armoring the stream itself, so the signed text is still
> readable with any tool capable of rendering text.  In order to bind a
> signature to such a cleartext, the Cleartext Signature Framework is
> used, which follows the same basic format and restrictions as the
> ASCII armoring described in Section 6.2.  (Note that this framework
> is not intended to be reversible.  [RFC3156] defines another way to
> sign cleartext messages for environments that support MIME.)

### §7.1 Cleartext Signed Message Structure

**N-374** (§7.1) — source lines 4495–4512

> An OpenPGP cleartext signed message consists of:
>
> *  The cleartext header -----BEGIN PGP SIGNED MESSAGE----- on a
>    single line.
>
> *  One or more legacy Hash Armor Headers that MAY be included by some
>    implementations and MUST be ignored when well formed (see
>    Section 6.2.2.3).
>
> *  An empty line (not included in the message digest).
>
> *  The dash-escaped cleartext.
>
> *  A line ending separating the cleartext and following armored
>    signature (not included in the message digest).
>
> *  The ASCII-armored signature(s), including the -----BEGIN PGP
>    SIGNATURE----- Armor Header and Armor Tail Lines.

**N-375** (§7.1) _[lowercase/implied]_ — source lines 4514–4518

> As with any other Text signature (Section 5.2.1.2), a cleartext
> signature is calculated on the text using canonical <CR><LF> line
> endings.  As described above, the line ending before the -----BEGIN
> PGP SIGNATURE----- Armor Header Line of the armored signature is not
> considered part of the signed text.

**N-376** (§7.1) _[lowercase/implied]_ — source lines 4520–4522

> Also, any trailing whitespace -- spaces (0x20) and tabs (0x09) -- at
> the end of any line is removed before signing or verifying a
> cleartext signed message.

**N-377** (§7.1) — source lines 4524–4529

> Between the -----BEGIN PGP SIGNED MESSAGE----- line and the first
> empty line, the only Armor Header permitted is a well-formed Hash
> Armor Header (see Section 6.2.2.3).  To reduce the risk of confusion
> about what has been signed, a verifying implementation MUST decline
> to validate any signature in a cleartext message if that message has
> any other Armor Header present in this location.

### §7.2 Dash-Escaped Text

**N-378** (§7.2) _[lowercase/implied]_ — source line 4533

> The cleartext content of the message must also be dash-escaped.

**N-379** (§7.2) — source lines 4535–4542

> Dash-escaped cleartext is the ordinary cleartext where every line
> starting with a "-" (HYPHEN-MINUS, U+002D) is prefixed by the
> sequence "-" (HYPHEN-MINUS, U+002D) and " " (SPACE, U+0020).  This
> prevents the parser from recognizing Armor Headers of the cleartext
> itself.  An implementation MAY dash-escape any line, SHOULD dash-
> escape lines commencing in "From" followed by a space, and MUST dash-
> escape any line commencing in a dash.  The message digest is computed
> using the cleartext itself, not the dash-escaped form.

**N-380** (§7.2) — source lines 4544–4547

> When reversing dash-escaping, an implementation MUST strip the string
> - if it occurs at the beginning of a line, and it SHOULD provide a
> warning for - and any character other than a space at the beginning
> of a line.

### §7.3 Issues with the Cleartext Signature Framework

_Lines 4551–4569 (why the framework fails on semantically meaningful whitespace and on very large messages) are motivation and are omitted; the requirement they motivate follows._

**N-381** (§7.3) — source lines 4571–4582

> An implementation that knows it is working with a textual stream with
> any of the above characteristics SHOULD NOT use the Cleartext
> Signature Framework.  Safe alternatives for a semantically meaningful
> OpenPGP signature over such a file format are:
>
> *  A signed message, as described in Section 10.3.
>
> *  A detached signature, as described in Section 10.4.
>
> Either of these alternatives may be ASCII-armored (see Section 6.2)
> if they need to be transmitted across a text-only (or 7-bit clean)
> channel.

_Lines 4584–4589 (the misleading-Hash-header attack and the constraints that mitigate it) are security motivation and are omitted._

## §8 Regular Expressions

_Line 4593 ("This section describes Regular Expressions.") is a section overview and is omitted._

**N-382** (§8) _[grammar]_ _[lowercase/implied]_ — source lines 4595–4623

```
   Regular Expression:  Zero or more branches, separated by |. It
      matches anything that matches one of the branches.

   Branch:  Zero or more pieces, concatenated.  It matches a match for
      the first, followed by a match for the second, etc.

   Piece:  An atom possibly followed by *, +, or ?. An atom followed by
      * matches a sequence of 0 or more matches of the atom.  An atom
      followed by + matches a sequence of 1 or more matches of the atom.
      An atom followed by ? matches a match of the atom or the null
      string.

   Atom:  A Regular Expression in parentheses (matching a match for the
      Regular Expression), a range (see below), a . (matching any single
      Unicode character), a ^ (matching the null string at the beginning
      of the input string), a $ (matching the null string at the end of
      the input string), a \ followed by a single Unicode character
      (matching that character), or a single Unicode character with no
      other significance (matching that character).

   Range:  A sequence of characters enclosed in [].  It normally matches
      any single character from the sequence.  If the sequence begins
      with ^, it matches any single Unicode character not from the rest
      of the sequence.  If two characters in the sequence are separated
      by -, this is shorthand for the full list of Unicode characters
      between them in codepoint order (for example, [0-9] matches any
      decimal digit).  To include a literal ] in the sequence, make it
      the first character (following a possible ^).  To include a
      literal -, make it the first or last character.
```

## §9 Constants

_Line 4627 (section overview) and line 4634 (pointer to Section 12) are omitted._

**N-383** (§9) — source lines 4629–4632

> Note that these tables are not exhaustive lists; an implementation
> MAY implement an algorithm that is not on these lists, as long as the
> algorithm IDs are chosen from the Private or Experimental Use
> algorithm range.

### §9.1 Public Key Algorithms

**N-384** (§9.1) _[table]_ — source lines 4638–4758

```
   +===+==============+=========+============+===========+=============+
   | ID| Algorithm    |Public   | Secret Key | Signature | PKESK       |
   |   |              |Key      | Format     | Format    | Format      |
   |   |              |Format   |            |           |             |
   +===+==============+=========+============+===========+=============+
   |  0| Reserved     |         |            |           |             |
   +---+--------------+---------+------------+-----------+-------------+
   |  1| RSA (Encrypt |MPI(n),  | MPI(d),    | MPI(m^d   | MPI(m^e     |
   |   | or Sign)     |MPI(e)   | MPI(p),    | mod n)    | mod n)      |
   |   | [FIPS186]    |[Section | MPI(q),    | [Section  | [Section    |
   |   |              |5.5.5.1] | MPI(u)     | 5.2.3.1]  | 5.1.3]      |
   +---+--------------+---------+------------+-----------+-------------+
   |  2| RSA Encrypt- |MPI(n),  | MPI(d),    | N/A       | MPI(m^e     |
   |   | Only         |MPI(e)   | MPI(p),    |           | mod n)      |
   |   | [FIPS186]    |[Section | MPI(q),    |           | [Section    |
   |   |              |5.5.5.1] | MPI(u)     |           | 5.1.3]      |
   +---+--------------+---------+------------+-----------+-------------+
   |  3| RSA Sign-    |MPI(n),  | MPI(d),    | MPI(m^d   | N/A         |
   |   | Only         |MPI(e)   | MPI(p),    | mod n)    |             |
   |   | [FIPS186]    |[Section | MPI(q),    | [Section  |             |
   |   |              |5.5.5.1] | MPI(u)     | 5.2.3.1]  |             |
   +---+--------------+---------+------------+-----------+-------------+
   | 16| Elgamal      |MPI(p),  | MPI(x)     | N/A       | MPI(g^k     |
   |   | (Encrypt-    |MPI(g),  |            |           | mod p),     |
   |   | Only)        |MPI(y)   |            |           | MPI(m *     |
   |   | [ELGAMAL]    |[Section |            |           | y^k mod     |
   |   |              |5.5.5.3] |            |           | p)          |
   |   |              |         |            |           | [Section    |
   |   |              |         |            |           | 5.1.4]      |
   +---+--------------+---------+------------+-----------+-------------+
   | 17| DSA (Digital |MPI(p),  | MPI(x)     | MPI(r),   | N/A         |
   |   | Signature    |MPI(q),  |            | MPI(s)    |             |
   |   | Algorithm)   |MPI(g),  |            | [Section  |             |
   |   | [FIPS186]    |MPI(y)   |            | 5.2.3.2]  |             |
   |   |              |[Section |            |           |             |
   |   |              |5.5.5.2] |            |           |             |
   +---+--------------+---------+------------+-----------+-------------+
   | 18| ECDH public  |OID,     | MPI(value  | N/A       | MPI(point   |
   |   | key          |MPI(point| in curve-  |           | in curve-   |
   |   | algorithm    |in curve-| specific   |           | specific    |
   |   |              |specific | format)    |           | point       |
   |   |              |point    | [Section   |           | format),    |
   |   |              |format), | 9.2.1]     |           | size        |
   |   |              |KDFParams|            |           | octet,      |
   |   |              |[Sections|            |           | encoded     |
   |   |              |9.2.1 and|            |           | key         |
   |   |              |5.5.5.6] |            |           | [Sections   |
   |   |              |         |            |           | 9.2.1,      |
   |   |              |         |            |           | 5.1.5,      |
   |   |              |         |            |           | and 11.5]   |
   +---+--------------+---------+------------+-----------+-------------+
   | 19| ECDSA public |OID,     | MPI(value) | MPI(r),   | N/A         |
   |   | key          |MPI(point|            | MPI(s)    |             |
   |   | algorithm    |in SEC1  |            | [Section  |             |
   |   | [FIPS186]    |format)  |            | 5.2.3.2]  |             |
   |   |              |[Section |            |           |             |
   |   |              |5.5.5.4] |            |           |             |
   +---+--------------+---------+------------+-----------+-------------+
   | 20| Reserved     |         |            |           |             |
   |   | (formerly    |         |            |           |             |
   |   | Elgamal      |         |            |           |             |
   |   | Encrypt or   |         |            |           |             |
   |   | Sign)        |         |            |           |             |
   +---+--------------+---------+------------+-----------+-------------+
   | 21| Reserved for |         |            |           |             |
   |   | Diffie-      |         |            |           |             |
   |   | Hellman      |         |            |           |             |
   |   | (X9.42, as   |         |            |           |             |
   |   | defined for  |         |            |           |             |
   |   | IETF-S/MIME) |         |            |           |             |
   +---+--------------+---------+------------+-----------+-------------+
   | 22| EdDSALegacy  |OID,     | MPI(value  | MPI, MPI  | N/A         |
   |   | (deprecated) |MPI(point| in curve-  | [Sections |             |
   |   |              |in       | specific   | 9.2.1 and |             |
   |   |              |prefixed | format)    | 5.2.3.3]  |             |
   |   |              |native   | [Section   |           |             |
   |   |              |format)  | 9.2.1]     |           |             |
   |   |              |[Sections|            |           |             |
   |   |              |11.2.2   |            |           |             |
   |   |              |and      |            |           |             |
   |   |              |5.5.5.5] |            |           |             |
   +---+--------------+---------+------------+-----------+-------------+
   | 23| Reserved     |         |            |           |             |
   |   | (AEDH)       |         |            |           |             |
   +---+--------------+---------+------------+-----------+-------------+
   | 24| Reserved     |         |            |           |             |
   |   | (AEDSA)      |         |            |           |             |
   +---+--------------+---------+------------+-----------+-------------+
   | 25| X25519       |32 octets| 32 octets  | N/A       | 32          |
   |   |              |[Section |            |           | octets,     |
   |   |              |5.5.5.7] |            |           | size        |
   |   |              |         |            |           | octet,      |
   |   |              |         |            |           | encoded     |
   |   |              |         |            |           | key         |
   |   |              |         |            |           | [Section    |
   |   |              |         |            |           | 5.1.6]      |
   +---+--------------+---------+------------+-----------+-------------+
   | 26| X448         |56 octets| 56 octets  | N/A       | 56          |
   |   |              |[Section |            |           | octets,     |
   |   |              |5.5.5.8] |            |           | size        |
   |   |              |         |            |           | octet,      |
   |   |              |         |            |           | encoded     |
   |   |              |         |            |           | key         |
   |   |              |         |            |           | [Section    |
   |   |              |         |            |           | 5.1.7]      |
   +---+--------------+---------+------------+-----------+-------------+
   | 27| Ed25519      |32 octets| 32 octets  | 64 octets |             |
   |   |              |[Section |            | [Section  |             |
   |   |              |5.5.5.9] |            | 5.2.3.4]  |             |
   +---+--------------+---------+------------+-----------+-------------+
   | 28| Ed448        |57 octets| 57 octets  | 114       |             |
   |   |              |[Section |            | octets    |             |
   |   |              |5.5.5.10]|            | [Section  |             |
   |   |              |         |            | 5.2.3.5]  |             |
   +---+--------------+---------+------------+-----------+-------------+
   |100| Private or   |         |            |           |             |
   | to| Experimental |         |            |           |             |
   |110| Use          |         |            |           |             |
   +---+--------------+---------+------------+-----------+-------------+

              Table 18: OpenPGP Public Key Algorithms Registry
```

**N-385** (§9.1) — source lines 4760–4771

> Implementations MUST implement Ed25519 (27) for signatures and X25519
> (25) for encryption.  Implementations SHOULD implement Ed448 (28) and
> X448 (26).
>
> RSA (1) keys are deprecated and SHOULD NOT be generated but may be
> interpreted.  RSA Encrypt-Only (2) and RSA Sign-Only (3) are
> deprecated and MUST NOT be generated (see Section 12.4).  Elgamal
> (16) keys are deprecated and MUST NOT be generated (see
> Section 12.6).  DSA (17) keys are deprecated and MUST NOT be
> generated (see Section 12.5).  For notes on Elgamal Encrypt or Sign
> (20) and X9.42 (21), see Section 12.8.  Implementations MAY implement
> any other algorithm.

**N-386** (§9.1) — source lines 4773–4775

> Note that an implementation conforming to the previous version of
> this specification [RFC4880] has only DSA (17) and Elgamal (16) as
> the algorithms that MUST be implemented.

_The MUST in this entry reports what RFC 4880 required; it places no requirement on implementations of this document (see the EXCLUDED note in req-D.yaml)._

_Lines 4777–4779 (where compatible ECDSA and ECDH definitions are found) are informative pointers and are omitted._

### §9.2 ECC Curves for OpenPGP

**N-387** (§9.2) _[lowercase/implied]_ — source lines 4783–4790

> The parameter curve OID is an array of octets that defines a named
> curve.
>
> The table below specifies the exact sequence of octets for each named
> curve referenced in this document.  It also specifies which public
> key algorithms the curve can be used with, as well as the size of
> expected elements in octets.  Note that there is a break in
> "EdDSALegacy" for display purposes only.

**N-388** (§9.2) _[table]_ — source lines 4792–4841

```
   +======================+===+========+================+======+=======+
   |ASN.1 Object          |OID| Curve  |Curve Name      |Usage |Field  |
   |Identifier            |Len| OID    |                |      |Size   |
   |                      |   | Octets |                |      |(fsize)|
   +======================+===+========+================+======+=======+
   |1.2.840.10045.3.1.7   |8  | 2A 86  |NIST P-256      |ECDSA,|32     |
   |                      |   | 48 CE  |                |ECDH  |       |
   |                      |   | 3D 03  |                |      |       |
   |                      |   | 01 07  |                |      |       |
   +----------------------+---+--------+----------------+------+-------+
   |1.3.132.0.34          |5  | 2B 81  |NIST P-384      |ECDSA,|48     |
   |                      |   | 04 00  |                |ECDH  |       |
   |                      |   | 22     |                |      |       |
   +----------------------+---+--------+----------------+------+-------+
   |1.3.132.0.35          |5  | 2B 81  |NIST P-521      |ECDSA,|66     |
   |                      |   | 04 00  |                |ECDH  |       |
   |                      |   | 23     |                |      |       |
   +----------------------+---+--------+----------------+------+-------+
   |1.3.36.3.3.2.8.1.1.7  |9  | 2B 24  |brainpoolP256r1 |ECDSA,|32     |
   |                      |   | 03 03  |                |ECDH  |       |
   |                      |   | 02 08  |                |      |       |
   |                      |   | 01 01  |                |      |       |
   |                      |   | 07     |                |      |       |
   +----------------------+---+--------+----------------+------+-------+
   |1.3.36.3.3.2.8.1.1.11 |9  | 2B 24  |brainpoolP384r1 |ECDSA,|48     |
   |                      |   | 03 03  |                |ECDH  |       |
   |                      |   | 02 08  |                |      |       |
   |                      |   | 01 01  |                |      |       |
   |                      |   | 0B     |                |      |       |
   +----------------------+---+--------+----------------+------+-------+
   |1.3.36.3.3.2.8.1.1.13 |9  | 2B 24  |brainpoolP512r1 |ECDSA,|64     |
   |                      |   | 03 03  |                |ECDH  |       |
   |                      |   | 02 08  |                |      |       |
   |                      |   | 01 01  |                |      |       |
   |                      |   | 0D     |                |      |       |
   +----------------------+---+--------+----------------+------+-------+
   |1.3.6.1.4.1.11591.15.1|9  | 2B 06  |Ed25519Legacy   |EdDSA |32     |
   |                      |   | 01 04  |                |Legacy|       |
   |                      |   | 01 DA  |                |      |       |
   |                      |   | 47 0F  |                |      |       |
   |                      |   | 01     |                |      |       |
   +----------------------+---+--------+----------------+------+-------+
   |1.3.6.1.4.1.3029.1.5.1|10 | 2B 06  |Curve25519Legacy|ECDH  |32     |
   |                      |   | 01 04  |                |      |       |
   |                      |   | 01 97  |                |      |       |
   |                      |   | 55 01  |                |      |       |
   |                      |   | 05 01  |                |      |       |
   +----------------------+---+--------+----------------+------+-------+

            Table 19: OpenPGP ECC Curve OIDs and Usage Registry
```

**N-389** (§9.2) _[lowercase/implied]_ — source lines 4843–4850

> The "Field Size (fsize)" column represents the field size of the
> group in number of octets, rounded up, such that x or y coordinates
> for a point on the curve or native point representations for the
> curve can be represented in that many octets.  The curves specified
> here, and scalars such as the base point order and the private key,
> can be represented in fsize octets.  However, note that curves exist
> outside this specification where the representation of scalars
> requires an additional octet.

**N-390** (§9.2) _[lowercase/implied]_ — source lines 4852–4861

> The sequence of octets in the third column is the result of applying
> the Distinguished Encoding Rules (DER) to the ASN.1 Object Identifier
> with subsequent truncation.  The truncation removes the two fields of
> encoded Object Identifier.  The first omitted field is 1 octet
> representing the Object Identifier tag, and the second omitted field
> is the length of the Object Identifier body.  For example, the
> complete ASN.1 DER encoding for the NIST P-256 curve OID is "06 08 2A
> 86 48 CE 3D 03 01 07", from which the first entry in the table above
> is constructed by omitting the first two octets.  Only the truncated
> sequence of octets is the valid representation of a curve OID.

**N-391** (§9.2) — source lines 4863–4867

> The deprecated OIDs for Ed25519Legacy and Curve25519Legacy are used
> only in version 4 keys and signatures.  Implementations MAY implement
> these variants for compatibility with existing version 4 key material
> and signatures.  Implementations MUST NOT accept or generate version
> 6 key material using the deprecated OIDs.

### §9.2.1 Curve-Specific Wire Formats

**N-392** (§9.2.1) _[lowercase/implied]_ — source lines 4871–4874

> Some elliptic curve public key algorithms use different conventions
> for specific fields depending on the curve in use.  Each field is
> always formatted as an MPI, but with a curve-specific framing.  This
> table summarizes those distinctions.

**N-393** (§9.2.1) _[table]_ — source lines 4876–4904

```
   +================+========+============+=======+=========+==========+
   |Curve           |ECDH    |ECDH Secret |EdDSA  |EdDSA    |EdDSA     |
   |                |Point   |Key MPI     |Secret |Signature|Signature |
   |                |Format  |            |Key MPI|first MPI|second    |
   |                |        |            |       |         |MPI       |
   +================+========+============+=======+=========+==========+
   |NIST P-256      |SEC1    |integer     |N/A    |N/A      |N/A       |
   +----------------+--------+------------+-------+---------+----------+
   |NIST P-384      |SEC1    |integer     |N/A    |N/A      |N/A       |
   +----------------+--------+------------+-------+---------+----------+
   |NIST P-521      |SEC1    |integer     |N/A    |N/A      |N/A       |
   +----------------+--------+------------+-------+---------+----------+
   |brainpoolP256r1 |SEC1    |integer     |N/A    |N/A      |N/A       |
   +----------------+--------+------------+-------+---------+----------+
   |brainpoolP384r1 |SEC1    |integer     |N/A    |N/A      |N/A       |
   +----------------+--------+------------+-------+---------+----------+
   |brainpoolP512r1 |SEC1    |integer     |N/A    |N/A      |N/A       |
   +----------------+--------+------------+-------+---------+----------+
   |Ed25519Legacy   |N/A     |N/A         |32     |32 octets|32 octets |
   |                |        |            |octets |of R     |of S      |
   |                |        |            |of     |         |          |
   |                |        |            |secret |         |          |
   +----------------+--------+------------+-------+---------+----------+
   |Curve25519Legacy|prefixed|integer     |N/A    |N/A      |N/A       |
   |                |native  |(Section    |       |         |          |
   |                |        |5.5.5.6.1.1)|       |         |          |
   +----------------+--------+------------+-------+---------+----------+

         Table 20: OpenPGP ECC Curve-Specific Wire Formats Registry
```

**N-394** (§9.2.1) _[lowercase/implied]_ — source lines 4906–4908

> For the native octet-string forms of Ed25519Legacy values, see
> [RFC8032].  For the native octet-string forms of Curve25519Legacy
> secret scalars and points, see [RFC7748].

### §9.3 Symmetric Key Algorithms

**N-395** (§9.3) _[table]_ — source lines 4912–4951

```
         +=========+============================================+
         |      ID | Algorithm                                  |
         +=========+============================================+
         |       0 | Plaintext or unencrypted data              |
         +---------+--------------------------------------------+
         |       1 | IDEA [IDEA]                                |
         +---------+--------------------------------------------+
         |       2 | TripleDES (or DES-EDE) [SP800-67] with     |
         |         | 168-bit key derived from 192               |
         +---------+--------------------------------------------+
         |       3 | CAST5 with 128-bit key [RFC2144]           |
         +---------+--------------------------------------------+
         |       4 | Blowfish with 128-bit key, 16 rounds       |
         |         | [BLOWFISH]                                 |
         +---------+--------------------------------------------+
         |       5 | Reserved                                   |
         +---------+--------------------------------------------+
         |       6 | Reserved                                   |
         +---------+--------------------------------------------+
         |       7 | AES with 128-bit key [AES]                 |
         +---------+--------------------------------------------+
         |       8 | AES with 192-bit key                       |
         +---------+--------------------------------------------+
         |       9 | AES with 256-bit key                       |
         +---------+--------------------------------------------+
         |      10 | Twofish with 256-bit key [TWOFISH]         |
         +---------+--------------------------------------------+
         |      11 | Camellia with 128-bit key [RFC3713]        |
         +---------+--------------------------------------------+
         |      12 | Camellia with 192-bit key                  |
         +---------+--------------------------------------------+
         |      13 | Camellia with 256-bit key                  |
         +---------+--------------------------------------------+
         | 100-110 | Private or Experimental Use                |
         +---------+--------------------------------------------+
         | 253-255 | Reserved to avoid collision with Secret    |
         |         | Key Encryption (Table 2 and Section 5.5.3) |
         +---------+--------------------------------------------+

           Table 21: OpenPGP Symmetric Key Algorithms Registry
```

**N-396** (§9.3) — source lines 4953–4961

> Implementations MUST implement AES-128.  Implementations SHOULD
> implement AES-256.  Implementations MUST NOT encrypt data with IDEA,
> TripleDES, or CAST5.  Implementations MAY decrypt data that uses
> IDEA, TripleDES, or CAST5 for the sake of reading older messages or
> new messages from implementations predating support for [RFC2440].
> An Implementation that decrypts data using IDEA, TripleDES, or CAST5
> SHOULD generate a deprecation warning about the symmetric algorithm,
> indicating that message confidentiality is suspect.  Implementations
> MAY implement any other algorithm.

### §9.4 Compression Algorithms

**N-397** (§9.4) _[table]_ — source lines 4965–4980

```
                 +=========+=============================+
                 |      ID | Algorithm                   |
                 +=========+=============================+
                 |       0 | Uncompressed                |
                 +---------+-----------------------------+
                 |       1 | ZIP [RFC1951]               |
                 +---------+-----------------------------+
                 |       2 | ZLIB [RFC1950]              |
                 +---------+-----------------------------+
                 |       3 | BZip2 [BZ2]                 |
                 +---------+-----------------------------+
                 | 100-110 | Private or Experimental Use |
                 +---------+-----------------------------+

                       Table 22: OpenPGP Compression
                            Algorithms Registry
```

**N-398** (§9.4) — source lines 4982–4985

> Implementations MUST implement uncompressed data.  Implementations
> SHOULD implement ZLIB.  For interoperability reasons, implementations
> SHOULD be able to decompress using ZIP.  Implementations MAY
> implement any other algorithm.

### §9.5 Hash Algorithms

**N-399** (§9.5) _[table]_ — source lines 4989–5034

```
   +=========+==================+=============+========================+
   |      ID | Algorithm        | Text Name   | V6 Signature           |
   |         |                  |             | Salt Size              |
   +=========+==================+=============+========================+
   |       0 | Reserved         |             |                        |
   +---------+------------------+-------------+------------------------+
   |       1 | MD5 [RFC1321]    | "MD5"       | N/A                    |
   +---------+------------------+-------------+------------------------+
   |       2 | SHA-1 [FIPS180]  | "SHA1"      | N/A                    |
   +---------+------------------+-------------+------------------------+
   |       3 | RIPEMD-160       | "RIPEMD160" | N/A                    |
   |         | [RIPEMD-160]     |             |                        |
   +---------+------------------+-------------+------------------------+
   |       4 | Reserved         |             |                        |
   +---------+------------------+-------------+------------------------+
   |       5 | Reserved         |             |                        |
   +---------+------------------+-------------+------------------------+
   |       6 | Reserved         |             |                        |
   +---------+------------------+-------------+------------------------+
   |       7 | Reserved         |             |                        |
   +---------+------------------+-------------+------------------------+
   |       8 | SHA2-256         | "SHA256"    | 16                     |
   |         | [FIPS180]        |             |                        |
   +---------+------------------+-------------+------------------------+
   |       9 | SHA2-384         | "SHA384"    | 24                     |
   |         | [FIPS180]        |             |                        |
   +---------+------------------+-------------+------------------------+
   |      10 | SHA2-512         | "SHA512"    | 32                     |
   |         | [FIPS180]        |             |                        |
   +---------+------------------+-------------+------------------------+
   |      11 | SHA2-224         | "SHA224"    | 16                     |
   |         | [FIPS180]        |             |                        |
   +---------+------------------+-------------+------------------------+
   |      12 | SHA3-256         | "SHA3-256"  | 16                     |
   |         | [FIPS202]        |             |                        |
   +---------+------------------+-------------+------------------------+
   |      13 | Reserved         |             |                        |
   +---------+------------------+-------------+------------------------+
   |      14 | SHA3-512         | "SHA3-512"  | 32                     |
   |         | [FIPS202]        |             |                        |
   +---------+------------------+-------------+------------------------+
   | 100-110 | Private or       |             |                        |
   |         | Experimental Use |             |                        |
   +---------+------------------+-------------+------------------------+

                 Table 23: OpenPGP Hash Algorithms Registry
```

**N-400** (§9.5) _[table]_ — source lines 5036–5094

```
    +============+=========================+=========================+
    | Hash       | OID                     | Full Hash Prefix        |
    | Algorithm  |                         |                         |
    +============+=========================+=========================+
    | MD5        | 1.2.840.113549.2.5      | 0x30, 0x20, 0x30, 0x0C, |
    |            |                         | 0x06, 0x08, 0x2A, 0x86, |
    |            |                         | 0x48, 0x86, 0xF7, 0x0D, |
    |            |                         | 0x02, 0x05, 0x05, 0x00, |
    |            |                         | 0x04, 0x10              |
    +------------+-------------------------+-------------------------+
    | SHA-1      | 1.3.14.3.2.26           | 0x30, 0x21, 0x30, 0x09, |
    |            |                         | 0x06, 0x05, 0x2B, 0x0E, |
    |            |                         | 0x03, 0x02, 0x1A, 0x05, |
    |            |                         | 0x00, 0x04, 0x14        |
    +------------+-------------------------+-------------------------+
    | RIPEMD-160 | 1.3.36.3.2.1            | 0x30, 0x21, 0x30, 0x09, |
    |            |                         | 0x06, 0x05, 0x2B, 0x24, |
    |            |                         | 0x03, 0x02, 0x01, 0x05, |
    |            |                         | 0x00, 0x04, 0x14        |
    +------------+-------------------------+-------------------------+
    | SHA2-256   | 2.16.840.1.101.3.4.2.1  | 0x30, 0x31, 0x30, 0x0D, |
    |            |                         | 0x06, 0x09, 0x60, 0x86, |
    |            |                         | 0x48, 0x01, 0x65, 0x03, |
    |            |                         | 0x04, 0x02, 0x01, 0x05, |
    |            |                         | 0x00, 0x04, 0x20        |
    +------------+-------------------------+-------------------------+
    | SHA2-384   | 2.16.840.1.101.3.4.2.2  | 0x30, 0x41, 0x30, 0x0D, |
    |            |                         | 0x06, 0x09, 0x60, 0x86, |
    |            |                         | 0x48, 0x01, 0x65, 0x03, |
    |            |                         | 0x04, 0x02, 0x02, 0x05, |
    |            |                         | 0x00, 0x04, 0x30        |
    +------------+-------------------------+-------------------------+
    | SHA2-512   | 2.16.840.1.101.3.4.2.3  | 0x30, 0x51, 0x30, 0x0D, |
    |            |                         | 0x06, 0x09, 0x60, 0x86, |
    |            |                         | 0x48, 0x01, 0x65, 0x03, |
    |            |                         | 0x04, 0x02, 0x03, 0x05, |
    |            |                         | 0x00, 0x04, 0x40        |
    +------------+-------------------------+-------------------------+
    | SHA2-224   | 2.16.840.1.101.3.4.2.4  | 0x30, 0x2D, 0x30, 0x0D, |
    |            |                         | 0x06, 0x09, 0x60, 0x86, |
    |            |                         | 0x48, 0x01, 0x65, 0x03, |
    |            |                         | 0x04, 0x02, 0x04, 0x05, |
    |            |                         | 0x00, 0x04, 0x1C        |
    +------------+-------------------------+-------------------------+
    | SHA3-256   | 2.16.840.1.101.3.4.2.8  | 0x30, 0x31, 0x30, 0x0D, |
    |            |                         | 0x06, 0x09, 0x60, 0x86, |
    |            |                         | 0x48, 0x01, 0x65, 0x03, |
    |            |                         | 0x04, 0x02, 0x08, 0x05, |
    |            |                         | 0x00, 0x04, 0x20        |
    +------------+-------------------------+-------------------------+
    | SHA3-512   | 2.16.840.1.101.3.4.2.10 | 0x30, 0x51, 0x30, 0x0D, |
    |            |                         | 0x06, 0x09, 0x60, 0x86, |
    |            |                         | 0x48, 0x01, 0x65, 0x03, |
    |            |                         | 0x04, 0x02, 0x0a, 0x05, |
    |            |                         | 0x00, 0x04, 0x40        |
    +------------+-------------------------+-------------------------+

           Table 24: OpenPGP Hash Algorithm Identifiers for RSA
           Signatures' Use of EMSA-PKCS1-v1_5 Padding Registry
```

**N-401** (§9.5) — source lines 5096–5113

> Implementations MUST implement SHA2-256.  Implementations SHOULD
> implement SHA2-384 and SHA2-512.  Implementations MAY implement other
> algorithms.  Implementations SHOULD NOT create messages that require
> the use of SHA-1, with the exception of computing version 4 key
> fingerprints for purposes of the MDC in version 1 Symmetrically
> Encrypted and Integrity Protected Data packets.  Implementations MUST
> NOT generate signatures with MD5, SHA-1, or RIPEMD-160.
> Implementations MUST NOT use MD5, SHA-1, or RIPEMD-160 as a hash
> function in an ECDH KDF.  Implementations MUST NOT generate packets
> using MD5, SHA-1, or RIPEMD-160 as a hash function in an S2K KDF.
> Implementations MUST NOT decrypt a secret using MD5, SHA-1, or
> RIPEMD-160 as a hash function in an S2K KDF in a version 6 (or later)
> packet.  Implementations MUST NOT validate any recent signature that
> depends on MD5, SHA-1, or RIPEMD-160.  Implementations SHOULD NOT
> validate any old signature that depends on MD5, SHA-1, or RIPEMD-160
> unless the signature's creation date predates known weakness of the
> algorithm used, and the implementation is confident that the message
> has been in the secure custody of the user the whole time.

### §9.6 AEAD Algorithms

**N-402** (§9.6) _[table]_ — source lines 5117–5133

```
    +=========+==================+==============+====================+
    |      ID | Name             | Nonce Length | Authentication Tag |
    |         |                  | (Octets)     | Length (Octets)    |
    +=========+==================+==============+====================+
    |       0 | Reserved         |              |                    |
    +---------+------------------+--------------+--------------------+
    |       1 | EAX [EAX]        | 16           | 16                 |
    +---------+------------------+--------------+--------------------+
    |       2 | OCB [RFC7253]    | 15           | 16                 |
    +---------+------------------+--------------+--------------------+
    |       3 | GCM [SP800-38D]  | 12           | 16                 |
    +---------+------------------+--------------+--------------------+
    | 100-110 | Private or       |              |                    |
    |         | Experimental Use |              |                    |
    +---------+------------------+--------------+--------------------+

                Table 25: OpenPGP AEAD Algorithms Registry
```

**N-403** (§9.6) — source lines 5135–5136

> Implementations MUST implement OCB.  Implementations MAY implement
> EAX, GCM, and other algorithms.

## §10 Packet Sequence Composition

_Lines 5140–5152 (overview: packets form sequences; the three kinds of sequence and their sections) are document overview and are omitted._

**N-404** (§10) _[lowercase/implied]_ — source lines 5154–5161

> Each sequence has an explicit grammar of what packet types (Table 3)
> can appear in what place.  The presence of an unknown critical
> packet, or a known but unexpected packet, is a critical error,
> invalidating the entire sequence (see Section 4.3).  On the other
> hand, unknown non-critical packets can appear anywhere within any
> sequence.  This provides a structured way to introduce new packets
> into OpenPGP, while making sure that certain packets will be handled
> strictly.

**N-405** (§10) _[lowercase/implied]_ — source lines 5163–5166

> An implementation may "recognize" a packet but not implement it.  The
> purpose of Packet Criticality is to allow the producer to tell the
> consumer whether it would prefer a new, unknown packet to generate an
> error or be ignored.

_Lines 5168–5172 (earlier versions had no Packet Criticality) are history and are omitted._

**N-406** (§10) — source lines 5174–5176

> When generating a sequence of OpenPGP packets according to one of the
> three grammars, an implementation MUST NOT inject a critical packet
> of a type that does not adhere to the grammar.

**N-407** (§10) — source lines 5178–5181

> When consuming a sequence of OpenPGP packets, if an implementation
> encounters a critical packet of an inappropriate type according to
> the relevant grammar, the implementation MUST reject the sequence
> with an error.

### §10.1 Transferable Public Keys

**N-408** (§10.1) _[lowercase/implied]_ — source lines 5185–5190

> OpenPGP users may transfer public keys.  This section describes the
> structure of public keys in transit to ensure interoperability.  An
> OpenPGP Transferable Public Key is also known as an OpenPGP
> certificate, in order to distinguish it from both its constituent
> Public Key packets (Sections 5.5.1.1 and 5.5.1.2) and the underlying
> cryptographic key material.

### §10.1.1 OpenPGP Version 6 Certificate Structure

**N-409** (§10.1.1) _[grammar]_ _[lowercase/implied]_ — source lines 5194–5209

```
   The format of an OpenPGP version 6 certificate is as follows.
   Entries in square brackets are optional and ellipses indicate
   repetition.

   Primary Key
      [Revocation Signature...]
       Direct Key Signature...
      [User ID or User Attribute
              [Certification Revocation Signature...]
              [Certification Signature...]]...
      [Subkey [Subkey Revocation Signature...]
              Subkey Binding Signature...]...
      [Padding]

   In addition to these rules, a Marker packet (Section 5.8) can appear
   anywhere in the sequence.
```

**N-410** (§10.1.1) _[lowercase/implied]_ — source lines 5211–5212

> Note that a version 6 key uses a self-signed Direct Key signature to
> store algorithm preferences.

**N-411** (§10.1.1) — source lines 5214–5218

> Every subkey for a version 6 primary key MUST be a version 6 subkey.
> Every subkey MUST have at least one Subkey Binding signature.  Every
> Subkey Binding signature MUST be a self-signature (that is, made by
> the version 6 primary key).  Like all other signatures, every self-
> signature made by a version 6 key MUST be a version 6 signature.

### §10.1.2 OpenPGP Version 6 Revocation Certificate

**N-412** (§10.1.2) _[grammar]_ _[lowercase/implied]_ — source lines 5222–5229

```
   When a primary version 6 Public Key is revoked, it is sometimes
   distributed with only the Revocation Signature:

   Primary Key
       Revocation Signature

   In this case, the Direct Key signature is no longer necessary, since
   the primary key itself has been marked as unusable.
```

### §10.1.3 OpenPGP Version 4 Certificate Structure

**N-413** (§10.1.3) _[grammar]_ _[lowercase/implied]_ — source lines 5233–5243

```
   The format of an OpenPGP version 4 key is as follows.

   Primary Key
      [Revocation Signature]
      [Direct Key Signature...]
      [User ID or User Attribute [Signature...]]...
      [Subkey [Subkey Revocation Signature...]
              Subkey Binding Signature...]...

   In addition to these rules, a Marker packet (Section 5.8) can appear
   anywhere in the sequence.
```

**N-414** (§10.1.3) — source lines 5245–5250

> A subkey always has at least one Subkey Binding signature after it
> that is issued using the primary key to tie the two keys together.
> These binding signatures may be in either version 3 or version 4
> format, but they SHOULD be in version 4 format.  Subkeys that can
> issue signatures MUST have a version 4 binding signature due to the
> REQUIRED embedded Primary Key Binding signature.

**N-415** (§10.1.3) — source line 5252

> Every subkey for a version 4 primary key MUST be a version 4 subkey.

**N-416** (§10.1.3) — source lines 5254–5258

> When a primary version 4 Public Key is revoked, the Revocation
> Signature is sometimes distributed by itself, without the primary key
> packet it applies to.  This is referred to as a "revocation
> certificate".  Instead, a version 6 revocation certificate MUST
> include the primary key packet, as described in Section 10.1.2.

### §10.1.4 OpenPGP Version 3 Key Structure

**N-417** (§10.1.4) _[grammar]_ _[lowercase/implied]_ — source lines 5262–5270

```
   The format of an OpenPGP version 3 key is as follows.

   RSA Public Key
      [Revocation Signature]
       User ID [Signature...]
      [User ID [Signature...]]...

   In addition to these rules, a Marker packet (Section 5.8) can appear
   anywhere in the sequence.
```

**N-418** (§10.1.4) — source lines 5272–5276

> Each signature certifies the RSA public key and the preceding User
> ID.  The RSA public key can have many User IDs, and each User ID can
> have many signatures.  Version 3 keys are deprecated.
> Implementations MUST NOT generate new version 3 keys but MAY continue
> to use existing ones.

**N-419** (§10.1.4) — source line 5278

> Version 3 keys MUST NOT have subkeys.

### §10.1.5 Common Requirements

**N-420** (§10.1.5) _[lowercase/implied]_ — source line 5282

> The Public Key packet occurs first.

**N-421** (§10.1.5) — source lines 5284–5290

> The primary key MUST be an algorithm capable of making signatures
> (that is, not an encryption-only algorithm).  This is because the
> primary key needs to be able to create self-signatures (see
> Section 5.2.3.10).  The subkeys may be keys of any type.  For
> example, there may be a single-key RSA key, an Ed25519 primary key
> with an RSA encryption subkey, an Ed25519 primary key with an X25519
> subkey, etc.

**N-422** (§10.1.5) — source lines 5292–5298

> Each of the following User ID packets provides the identity of the
> owner of this public key.  If there are multiple User ID packets,
> this corresponds to multiple means of identifying the same unique
> individual user; for example, a user may have more than one email
> address and construct a User ID for each one.  A Transferable Public
> Key SHOULD include at least one User ID packet unless storage
> requirements prohibit this.

**N-423** (§10.1.5) _[lowercase/implied]_ — source lines 5300–5305

> Immediately following each User ID packet, there are zero or more
> Signature packets.  Each Signature packet is calculated on the
> immediately preceding User ID packet and the initial Public Key
> packet.  The signature serves to certify the corresponding public key
> and User ID.  In effect, the signer is testifying to the belief that
> this public key belongs to the user identified by this User ID.

**N-424** (§10.1.5) _[lowercase/implied]_ — source lines 5307–5311

> Within the same section as the User ID packets, there are zero or
> more User Attribute packets.  Like the User ID packets, a User
> Attribute packet is followed by zero or more Signature packets
> calculated on the immediately preceding User Attribute packet and the
> initial Public Key packet.

**N-425** (§10.1.5) _[lowercase/implied]_ — source lines 5313–5315

> User Attribute packets and User ID packets may be freely intermixed
> in this section, as long as the signatures that follow them are
> maintained on the proper User Attribute or User ID packet.

**N-426** (§10.1.5) _[lowercase/implied]_ — source lines 5317–5324

> After the sequence of User ID packets and Attribute packets and their
> associated signatures, zero or more Subkey packets follow, each with
> their own signatures.  In general, subkeys are provided in cases
> where the top-level public key is a certification-only key.  However,
> any version 4 or version 6 key may have subkeys, and the subkeys may
> be encryption keys, signing keys, authentication keys, etc.  It is
> good practice to use separate subkeys for every operation (i.e.,
> signature-only, encryption-only, authentication-only keys, etc.).

**N-427** (§10.1.5) — source lines 5326–5331

> Each Subkey packet MUST be followed by one Signature packet, which
> should be a Subkey Binding signature issued by the top-level key.
> For subkeys that can issue signatures, the Subkey Binding signature
> MUST contain an Embedded Signature subpacket with a Primary Key
> Binding signature (Type ID 0x19) issued by the subkey on the top-
> level key.

**N-428** (§10.1.5) _[lowercase/implied]_ — source lines 5333–5337

> Subkey and Key packets may each be followed by a Revocation Signature
> packet to indicate that the key is revoked.  Revocation Signatures
> are only accepted if they are issued by the key itself or by a key
> that is authorized to issue revocations via a Revocation Key
> subpacket in a self-signature by the top-level key.

**N-429** (§10.1.5) — source lines 5339–5346

> The optional trailing Padding packet is a mechanism to defend against
> traffic analysis (see Section 13.11).  For maximum interoperability,
> if the Public Key packet is a version 4 key, the optional Padding
> packet SHOULD NOT be present unless the recipient has indicated that
> they are capable of ignoring it successfully.  An implementation that
> is capable of receiving a Transferable Public Key with a version 6
> Public Key primary key MUST be able to accept (and ignore) the
> trailing optional Padding packet.

**N-430** (§10.1.5) _[lowercase/implied]_ — source lines 5348–5349

> Transferable Public Key packet sequences may be concatenated to allow
> transferring multiple public keys in one operation (see Section 3.6).

### §10.2 Transferable Secret Keys

**N-431** (§10.2) — source lines 5353–5363

> OpenPGP users may transfer secret keys.  The format of a Transferable
> Secret Key is the same as a Transferable Public Key except that
> Secret Key and Secret Subkey packets can be used in addition to the
> Public Key and Public Subkey packets.  If a single Secret Key or
> Secret Subkey packet is included in a packet sequence, it is a
> Transferable Secret Key and should be handled and marked as such (see
> Section 6.2.1).  An implementation SHOULD include self-signatures on
> any User IDs and subkeys, as this allows for a complete public key to
> be automatically extracted from the Transferable Secret Key. An
> implementation MAY choose to omit the self-signatures, especially if
> a Transferable Public Key accompanies the Transferable Secret Key.

### §10.3 OpenPGP Messages

**N-432** (§10.3) _[grammar]_ _[lowercase/implied]_ — source lines 5367–5398

```
   An OpenPGP Message is a packet or sequence of packets that adheres to
   the following grammatical rules (a comma (,) represents sequential
   composition, and a vertical bar (|) separates alternatives):

   OpenPGP Message:  Encrypted Message | Signed Message | Compressed
      Message | Literal Message.

   Compressed Message:  Compressed Data Packet.

   Literal Message:  Literal Data Packet.

   ESK:  Public Key Encrypted Session Key Packet | Symmetric Key
      Encrypted Session Key Packet.

   ESK Sequence:  ESK | ESK Sequence, ESK.

   Encrypted Data:  Symmetrically Encrypted Data Packet | Symmetrically
      Encrypted and Integrity Protected Data Packet.

   Encrypted Message:  Encrypted Data | ESK Sequence, Encrypted Data.

   One-Pass Signed Message:  One-Pass Signature Packet, OpenPGP Message,
      Corresponding Signature Packet.

   Signed Message:  Signature Packet, OpenPGP Message | One-Pass Signed
      Message.

   Optionally Padded Message:  OpenPGP Message | OpenPGP Message,
      Padding Packet.

   In addition to these rules, a Marker packet (Section 5.8) can appear
   anywhere in the sequence.
```

### §10.3.1 Unwrapping Encrypted and Compressed Messages

**N-433** (§10.3.1) — source lines 5402–5414

> In addition to the above grammar, certain messages can be "unwrapped"
> to yield new messages.  In particular:
>
> *  Decrypting a version 2 Symmetrically Encrypted and Integrity
>    Protected Data packet MUST yield a valid Optionally Padded
>    Message.
>
> *  Decrypting a version 1 Symmetrically Encrypted and Integrity
>    Protected Data packet or -- for historic data -- a Symmetrically
>    Encrypted Data packet MUST yield a valid OpenPGP Message.
>
> *  Decompressing a Compressed Data packet MUST also yield a valid
>    OpenPGP Message.

**N-434** (§10.3.1) — source lines 5416–5424

> When any unwrapping is performed, the resulting stream of octets is
> parsed into a series of OpenPGP packets like any other stream of
> octets.  The packet boundaries found in the series of octets are
> expected to align with the length of the unwrapped octet stream.  An
> implementation MUST NOT interpret octets beyond the boundaries of the
> unwrapped octet stream as part of any OpenPGP packet.  If an
> implementation encounters a packet whose header length indicates that
> it would extend beyond the boundaries of the unwrapped octet stream,
> the implementation MUST reject that packet as malformed and unusable.

### §10.3.2 Additional Constraints on Packet Sequences

**N-435** (§10.3.2) _[lowercase/implied]_ — source lines 5428–5429

> Note that some subtle combinations that are formally acceptable by
> this grammar are nonetheless unacceptable.

### §10.3.2.1 Packet Versions in Encrypted Messages

**N-436** (§10.3.2.1) — source lines 5433–5440

> As noted above, an Encrypted Message is a sequence of zero or more
> PKESK packets (Section 5.1) and SKESK packets (Section 5.3), followed
> by an SEIPD (Section 5.13) payload.  In some historic data, the
> payload may be a deprecated SED packet (Section 5.7) instead of
> SEIPD, though implementations MUST NOT generate SED packets (see
> Section 13.7).  The versions of the preceding ESK packets within an
> Encrypted Message MUST align with the version of the payload SEIPD
> packet, as described in this section.

**N-437** (§10.3.2.1) — source lines 5442–5446

> v3 PKESK and v4 SKESK packets both contain the Symmetric Cipher
> Algorithm ID and the session key for the subsequent SEIPD packet in
> their cleartext.  Since a v1 SEIPD does not contain a symmetric
> algorithm ID, all ESK packets preceding a v1 SEIPD payload MUST be
> either v3 PKESK or v4 SKESK.

**N-438** (§10.3.2.1) — source lines 5448–5451

> On the other hand, the cleartext of the v6 ESK packets (either PKESK
> or SKESK) do not contain a Symmetric Cipher Algorithm ID, so they
> cannot be used in combination with a v1 SEIPD payload.  The payload
> following any v6 PKESK or v6 SKESK packet MUST be a v2 SEIPD.

**N-439** (§10.3.2.1) — source lines 5453–5455

> Additionally, to avoid potentially conflicting cipher algorithm IDs,
> and for simplicity, implementations MUST NOT precede a v2 SEIPD
> payload with either v3 PKESK or v4 SKESK packets.

**N-440** (§10.3.2.1) — source lines 5457–5463

> The versions of packets found in an Encrypted Message are summarized
> in the following table.  An implementation MUST only generate an
> Encrypted Message using packet versions that match a row with "Yes"
> in the "Generate?" column.  Other rows are provided for the purpose
> of historic interoperability.  A conforming implementation MUST only
> generate an Encrypted Message using packets whose versions correspond
> to a single row.

**N-441** (§10.3.2.1) _[table]_ — source lines 5465–5487

```
   +==============+=====================+==================+===========+
   | Version of   | Version of          | Version of       | Generate? |
   | Encrypted    | Preceding Symmetric | Preceding        |           |
   | Data Payload | Key ESK (If Any)    | Public Key       |           |
   |              |                     | ESK (If Any)     |           |
   +==============+=====================+==================+===========+
   | SED (Section | -                   | v2 PKESK         | No        |
   | 5.7)         |                     | [RFC2440]        |           |
   +--------------+---------------------+------------------+-----------+
   | SED (Section | v4 SKESK            | v3 PKESK         | No        |
   | 5.7)         | (Section 5.3.1)     | (Section         |           |
   |              |                     | 5.1.1)           |           |
   +--------------+---------------------+------------------+-----------+
   | v1 SEIPD     | v4 SKESK            | v3 PKESK         | Yes       |
   | (Section     | (Section 5.3.1)     | (Section         |           |
   | 5.13.1)      |                     | 5.1.1)           |           |
   +--------------+---------------------+------------------+-----------+
   | v2 SEIPD     | v6 SKESK            | v6 PKESK         | Yes       |
   | (Section     | (Section 5.3.2)     | (Section         |           |
   | 5.13.2)      |                     | 5.1.2)           |           |
   +--------------+---------------------+------------------+-----------+

        Table 26: OpenPGP Encrypted Message Packet Versions Registry
```

**N-442** (§10.3.2.1) — source lines 5489–5491

> An implementation processing an Encrypted Message MUST discard any
> preceding ESK packet with a version that does not align with the
> version of the payload.

### §10.3.2.2 Packet Versions in Signatures

**N-443** (§10.3.2.2) — source lines 5495–5501

> OpenPGP Key packets and Signature packets are also versioned.  The
> version of a Signature typically matches the version of the signing
> key.  When a version 6 key produces a Signature packet, it MUST
> produce a version 6 Signature packet, regardless of the Signature
> packet type.  When a message is signed or verified using the one-pass
> construction, the version of the One-Pass Signature packet
> (Section 5.4) should also be aligned to the other versions.

**N-444** (§10.3.2.2) — source lines 5503–5507

> Some legacy implementations have produced unaligned signature
> versions for older key material, which are also described in the
> table below for the purpose of historic interoperability.  A
> conforming implementation MUST only generate Signature packets with
> version numbers matching rows with "Yes" in the "Generate?" column.

**N-445** (§10.3.2.2) _[table]_ — source lines 5509–5526

```
     +=====================+================+============+===========+
     | Signing Key Version | Signature      | OPS Packet | Generate? |
     |                     | Packet Version | Version    |           |
     +=====================+================+============+===========+
     | 3 (Section 5.5.2.1) | 3 (Section     | 3 (Section | No        |
     |                     | 5.2.2)         | 5.4)       |           |
     +---------------------+----------------+------------+-----------+
     | 4 (Section 5.5.2.2) | 3 (Section     | 3 (Section | No        |
     |                     | 5.2.2)         | 5.4)       |           |
     +---------------------+----------------+------------+-----------+
     | 4 (Section 5.5.2.2) | 4 (Section     | 3 (Section | Yes       |
     |                     | 5.2.3)         | 5.4)       |           |
     +---------------------+----------------+------------+-----------+
     | 6 (Section 5.5.2.3) | 6 (Section     | 6 (Section | Yes       |
     |                     | 5.2.3)         | 5.4)       |           |
     +---------------------+----------------+------------+-----------+

           Table 27: OpenPGP Key and Signature Versions Registry
```

**N-446** (§10.3.2.2) — source lines 5528–5531

> Note, however, that a version mismatch between these packets does not
> invalidate the packet sequence as a whole; it merely invalidates the
> signature, as a signature with an unknown version SHOULD be discarded
> (see Section 5.2.5).

### §10.4 Detached Signatures

**N-447** (§10.4) _[lowercase/implied]_ — source lines 5535–5542

> Some OpenPGP applications use so-called "detached signatures".  For
> example, a program bundle may contain a file, and with it a second
> file that is a detached signature of the first file.  These detached
> signatures are simply one or more Signature packets stored separately
> from the data for which they are a signature.
>
> In addition, a Marker packet (Section 5.8) and a Padding packet
> (Section 5.14) can appear anywhere in the sequence.

## §11 Elliptic Curve Cryptography

**N-448** (§11) _[lowercase/implied]_ — source lines 5546–5549

> This section describes algorithms and parameters used with Elliptic
> Curve Cryptography (ECC) keys.  A thorough introduction to ECC can be
> found in [KOBLITZ].  Refer to [FIPS186], Appendix B.4, for the
> methods to generate a uniformly distributed ECC private key.

**N-449** (§11) _[lowercase/implied]_ — source lines 5551–5552

> None of the ECC methods described in this document are allowed with
> deprecated version 3 keys.

### §11.1 ECC Curves

**N-450** (§11.1) _[lowercase/implied]_ — source lines 5556–5563

> This document references three named prime field curves defined in
> [FIPS186] as "Curve P-256", "Curve P-384", and "Curve P-521" and
> three named prime field curves defined in [RFC5639] as
> "brainpoolP256r1", "brainpoolP384r1", and "brainpoolP512r1".  All six
> curves can be used with ECDSA and ECDH public key algorithms.  They
> are referenced using a sequence of octets, referred to as the curve
> OID.  Section 9.2 describes in detail how this sequence of octets is
> formed.

**N-451** (§11.1) _[lowercase/implied]_ — source lines 5565–5569

> Separate algorithms are also defined for the use of X25519 and X448
> [RFC7748] and Ed25519 and Ed448 [RFC8032].  Additionally, legacy OIDs
> are defined for "Curve25519Legacy" (for encryption using the ECDH
> algorithm) and "Ed25519Legacy" (for signing using the EdDSALegacy
> algorithm).

### §11.2 EC Point Wire Formats

**N-452** (§11.2) _[lowercase/implied]_ — source lines 5573–5577

> A point on an elliptic curve will always be represented on the wire
> as an MPI.  Each curve uses a specific point format for the data
> within the MPI itself.  Each format uses a designated prefix octet to
> ensure that the high octet has at least 1 bit set to make the MPI a
> constant size.

**N-453** (§11.2) _[table]_ — source lines 5579–5588

```
           +=================+================+================+
           |            Name | Wire Format    | Reference      |
           +=================+================+================+
           |            SEC1 | 0x04 || x || y | Section 11.2.1 |
           +-----------------+----------------+----------------+
           | Prefixed native | 0x40 || native | Section 11.2.2 |
           +-----------------+----------------+----------------+

                Table 28: OpenPGP Elliptic Curve Point Wire
                              Formats Registry
```

### §11.2.1 SEC1 EC Point Wire Format

**N-454** (§11.2.1) _[lowercase/implied]_ — source lines 5592–5601

```
   For a SEC1-encoded (uncompressed) point, the content of the MPI is:

   B = 04 || x || y

   where x and y are coordinates of the point P = (x, y), and each is
   encoded in the big-endian format and zero-padded to the adjusted
   underlying field size.  The adjusted underlying field size is the
   underlying field size rounded up to the nearest 8-bit boundary, as
   noted in the "fsize" column in Section 9.2.  This encoding is
   compatible with the definition given in [SEC1].
```

### §11.2.2 Prefixed Native EC Point Wire Format

**N-455** (§11.2.2) _[lowercase/implied]_ — source lines 5605–5612

```
   For a custom compressed point, the content of the MPI is:

   B = 40 || p

   where p is the public key of the point encoded using the rules
   defined for the specified curve.  This format is used for ECDH keys
   based on curves expressed in Montgomery form and for points when
   using EdDSA.
```

### §11.2.3 Notes on EC Point Wire Formats

**N-456** (§11.2.3) _[lowercase/implied]_ — source lines 5616–5622

> Given the above definitions, the exact size of the MPI payload for an
> encoded point is 515 bits for both NIST P-256 and brainpoolP256r1,
> 771 for both NIST P-384 and brainpoolP384r1, 1059 for NIST P-521,
> 1027 for brainpoolP512r1, and 263 for both Curve25519Legacy and
> Ed25519Legacy.  For example, the length of an EdDSALegacy public key
> for the curve Ed25519Legacy is 263 bits: 7 bits to represent the 0x40
> prefix octet and 32 octets for the native value of the public key.

**N-457** (§11.2.3) — source lines 5624–5627

> Even though the zero point (also called the "point at infinity") may
> occur as a result of arithmetic operations on points of an elliptic
> curve, it SHALL NOT appear in data structures defined in this
> document.

**N-458** (§11.2.3) — source lines 5629–5632

> Each particular curve uses a designated wire format for the point
> found in its public key or ECDH data structure.  An implementation
> MUST NOT use a different wire format for a point other than the wire
> format associated with the curve.

### §11.3 EC Scalar Wire Formats

**N-459** (§11.3) _[lowercase/implied]_ — source lines 5636–5644

> Some non-curve values in elliptic curve cryptography (for example,
> secret keys and signature components) are not points on a curve, but
> they are also encoded on the wire in OpenPGP as an MPI.
>
> Because of different patterns of deployment, some curves treat these
> values as opaque bit strings with the high bit set, while others are
> treated as actual integers, encoded in the standard OpenPGP big-
> endian form.  The choice of encoding is specific to the public key
> algorithm in use.

**N-460** (§11.3) _[table]_ — source lines 5646–5662

```
   +==========+===========================================+===========+
   | Type     | Description                               | Reference |
   +==========+===========================================+===========+
   | integer  | An integer encoded in big-endian format   | Section   |
   |          | as a standard OpenPGP MPI                 | 3.2       |
   +----------+-------------------------------------------+-----------+
   | octet    | An octet string of fixed length that may  | Section   |
   | string   | be shorter on the wire due to leading     | 11.3.1    |
   |          | zeros being stripped by the MPI encoding  |           |
   |          | and may need to be zero-padded before use |           |
   +----------+-------------------------------------------+-----------+
   | prefixed | An octet string of fixed length N,        | Section   |
   | N octets | prefixed with octet 0x40 to ensure no     | 11.3.2    |
   |          | leading zero octet                        |           |
   +----------+-------------------------------------------+-----------+

        Table 29: OpenPGP Elliptic Curve Scalar Encodings Registry
```

### §11.3.1 EC Octet String Wire Format

**N-461** (§11.3.1) _[lowercase/implied]_ — source lines 5666–5690

```
   Some opaque strings of octets are represented on the wire as an MPI
   by simply stripping the leading zeros and counting the remaining
   bits.  These strings are of known, fixed length.  They are
   represented in this document as MPI(N octets of X), where N is the
   expected length in octets of the octet string.

   For example, a 5-octet opaque string (MPI(5 octets of X)) where X has
   the value 00 02 EE 19 00 would be represented on the wire as an MPI
   like so: 00 1A 02 EE 19 00.

   To encode X to the wire format, set the MPI's 2-octet bit counter to
   the value of the highest set bit (bit 26, or 0x001A), and do not
   transfer the leading all-zero octet to the wire.

   To reverse the process, an implementation can take the following
   steps, if it knows that X has an expected length of, for example, 5
   octets:

   *  Ensure that the MPI's 2-octet bit count is less than or equal to
      40 (5 octets of 8 bits)

   *  Allocate 5 octets, setting all to zero initially

   *  Copy the MPI data octets (without the two count octets) into the
      lower octets of the allocated space
```

### §11.3.2 EC Prefixed Octet String Wire Format

**N-462** (§11.3.2) _[lowercase/implied]_ — source lines 5694–5718

```
   Another way to ensure that a fixed-length bytes string is encoded
   simply to the wire while remaining in MPI format is to prefix the
   byte string with a dedicated non-zero octet.  This specification uses
   0x40 as the prefix octet.  This is represented in this specification
   as MPI(prefixed N octets of X), where N is the known byte string
   length.

   For example, a 5-octet opaque string using MPI(prefixed 5 octets of
   X) where X has the value 00 02 EE 19 00 would be written to the wire
   form as: 00 2F 40 00 02 EE 19 00.

   To encode the string, prefix it with the octet 0x40 (whose 7th bit is
   set), and then set the MPI's 2-octet bit counter to 47 (0x002F -- 7
   bits for the prefix octet and 40 bits for the string).

   To decode the string from the wire, an implementation that knows that
   the variable is formed in this way can:

   *  ensure that the first three octets of the MPI (the 2-bit count
      octets plus the prefix octet) are 00 2F 40, and

   *  use the remainder of the MPI directly off the wire.

   Note that this is a similar approach to that used in the EC point
   encodings found in Section 11.2.2.
```

### §11.4 Key Derivation Function

**N-463** (§11.4) — source lines 5722–5725

> A key derivation function (KDF) is necessary to implement EC
> encryption.  The Concatenation Key Derivation Function (Approved
> Alternative 1) [SP800-56A] with the KDF hash function that is
> SHA2-256 [FIPS180] or stronger is REQUIRED.

**N-464** (§11.4) _[lowercase/implied]_ — source lines 5727–5730

> For convenience, the synopsis of the encoding method is given below
> with significant simplifications attributable to the restricted
> choice of hash functions in this document.  However, [SP800-56A] is
> the normative source of the definition.

**N-465** (§11.4) _[code]_ _[lowercase/implied]_ — source lines 5732–5746

```
   //   Implements KDF( X, oBits, Param );
   //   Input: point X = (x,y)
   //   oBits - the desired size of output
   //   hBits - the size of output of hash function Hash
   //   Param - octets representing the parameters
   //   Assumes that oBits <= hBits
   // Convert the point X to the octet string:
   //   ZB' = 04 || x || y
   // and extract the x portion from ZB'
   ZB = x;
   MB = Hash ( 00 || 00 || 00 || 01 || ZB || Param );
   return oBits leftmost bits of MB.

   Note that ZB in the KDF description above is the compact
   representation of X as defined in Section 4.2 of [RFC6090].
```

### §11.5 ECDH Algorithm

_Lines 5750–5755 (overview of the One-Pass Diffie-Hellman method and key wrapping) are section overview and are omitted._

**N-466** (§11.5) — source lines 5757–5761

> The One-Pass Diffie-Hellman method C(1, 1, ECC CDH) [SP800-56A] MUST
> be implemented with the following restrictions: the ECC Cofactor
> Diffie-Hellman (CDH) primitive employed by this method is modified to
> always assume the cofactor is 1, the KDF specified in Section 11.4 is
> used, and the KDF parameters specified below are used.

**N-467** (§11.5) _[lowercase/implied]_ — source lines 5763–5799

```
   The KDF parameters are encoded as a concatenation of the following 5
   variable-length and fixed-length fields, which are compatible with
   the definition of the OtherInfo bit string [SP800-56A]:

   *  A variable-length field containing a curve OID, which is formatted
      as follows:

      -  A 1-octet size of the following field.

      -  The octets representing a curve OID, as defined in Section 9.2.

   *  A 1-octet public key algorithm ID, as defined in Section 9.1.

   *  A variable-length field containing KDF parameters, which are
      identical to the corresponding field in the ECDH public key and
      formatted as follows:

      -  A 1-octet size of the following fields; values 0 and 0xFF are
         reserved for future extensions.

      -  A 1-octet value 0x01, reserved for future extensions.

      -  A 1-octet hash function ID used with the KDF.

      -  A 1-octet algorithm ID for the symmetric algorithm that is used
         to wrap the symmetric key for message encryption; see
         Section 11.5 for details.

   *  20 octets representing the UTF-8 encoding of the string "Anonymous
      Sender" padded at the end with spaces (0x20) to 20 octets, which
      is the octet sequence 41 6E 6F 6E 79 6D 6F 75 73 20 53 65 6E 64 65
      72 20 20 20 20.

   *  A variable-length field containing the fingerprint of the
      recipient encryption subkey identifying the key material that is
      needed for decryption.  For version 4 keys, this field is 20
      octets.  For version 6 keys, this field is 32 octets.
```

**N-468** (§11.5) _[lowercase/implied]_ — source lines 5801–5807

> The size in octets of the KDF parameters sequence, as defined above,
> for encrypting to a version 4 key is 54 for curve NIST P-256; 51 for
> curves NIST P-384 and NIST P-521; 55 for curves brainpoolP256r1,
> brainpoolP384r1, and brainpoolP512r1; or 56 for Curve25519Legacy.
> For encrypting to a version 6 key, the size of the sequence is 66 for
> curve NIST P-256; 63 for curves NIST P-384 and NIST P-521; or 67 for
> curves brainpoolP256r1, brainpoolP384r1, and brainpoolP512r1.

**N-469** (§11.5) — source lines 5809–5814

> The key wrapping method is described in [RFC3394].  The KDF produces
> a symmetric key that is used as a KEK as specified in [RFC3394].
> Refer to Section 11.5.1 for the details regarding the choice of the
> KEK algorithm, which SHOULD be one of the three AES algorithms.  Key
> wrapping and unwrapping is performed with the default initial value
> of [RFC3394].

**N-470** (§11.5) _[lowercase/implied]_ — source lines 5816–5828

```
   To produce the input to the key wrapping method, first concatenate
   the following values:

   *  The 1-octet algorithm identifier, if it was passed (in the case of
      a v3 PKESK packet).

   *  The session key.

   *  A 2-octet checksum of the session key, equal to the sum of the
      session key octets, modulo 65536.

   Then, the above values are padded to an 8-octet granularity using the
   method described in [RFC8018].
```

**N-471** (§11.5) — source lines 5830–5843

```
   For example, in a version 3 Public Key Encrypted Session Key packet,
   an AES-256 session key is encoded as follows, forming a 40-octet
   sequence:

   09 k0 k1 ... k31 s0 s1 05 05 05 05 05

   The octets k0 to k31 above denote the session key, and the octets s0
   and s1 denote the checksum of the session key octets.  This encoding
   allows the sender to obfuscate the size of the symmetric encryption
   key used to encrypt the data.  For example, assuming that an AES
   algorithm is used for the session key, the sender MAY use 21, 13, and
   5 octets of padding for AES-128, AES-192, and AES-256, respectively,
   to provide the same number of octets, 40 total, as an input to the
   key wrapping method.
```

**N-472** (§11.5) — source lines 5845–5856

```
   In a version 6 Public Key Encrypted Session Key packet, the symmetric
   algorithm is not included, as described in Section 5.1.  For example,
   an AES-256 session key would be composed as follows:

   k0 k1 ... k31 s0 s1 06 06 06 06 06 06

   The octets k0 to k31 above again denote the session key, and the
   octets s0 and s1 denote the checksum.  In this case, assuming that an
   AES algorithm is used for the session key, the sender MAY use 22, 14,
   and 6 octets of padding for AES-128, AES-192, and AES-256,
   respectively, to provide the same number of octets, 40 total, as an
   input to the key wrapping method.
```

**N-473** (§11.5) _[lowercase/implied]_ — source lines 5858–5871

```
   The output of the method consists of two fields.  The first field is
   the MPI containing the ephemeral key used to establish the shared
   secret.  The second field is composed of the following two subfields:

   *  One octet encoding the size in octets of the result of the key
      wrapping method; the value 255 is reserved for future extensions.

   *  Up to 254 octets representing the result of the key wrapping
      method, applied to the 8-octet padded session key, as described
      above.

   Note that for session key sizes 128, 192, and 256 bits, the size of
   the result of the key wrapping method is, respectively, 32, 40, and
   48 octets, unless size obfuscation is used.
```

**N-474** (§11.5) _[code]_ _[lowercase/implied]_ — source lines 5873–5909

```
   For convenience, the synopsis of the encoding method is given below;
   however, this section, [SP800-56A], and [RFC3394] are the normative
   sources of the definition.

   *  Obtain the authenticated recipient public key R

   *  Generate an ephemeral, single-use key pair {v, V=vG}

   *  Compute the shared point S = vR

   *  m = symm_alg_ID || session key || checksum || pkcs5_padding

   *  curve_OID_len = (octet)len(curve_OID)

   *  Param = curve_OID_len || curve_OID || public_key_alg_ID || 03 ||
      01 || KDF_hash_ID || KEK_alg_ID for AESKeyWrap || 41 6E 6F 6E 79
      6D 6F 75 73 20 53 65 6E 64 65 72 20 20 20 20 ||
      recipient_fingerprint

   *  Z_len = the key size for the KEK_alg_ID used with AESKeyWrap

   *  Compute Z = KDF( S, Z_len, Param )

   *  Compute C = AESKeyWrap( Z, m ) (per [RFC3394])

   *  Wipe the memory that contained S, v, and Z to avoid leaking
      ephemeral secrets

   *  VB = convert point V to the octet string

   *  Output (MPI(VB) || len(C) || C)

   The decryption is the inverse of the method given.  Note that the
   recipient with key pair (r,R) obtains the shared secret by
   calculating:

   S = rV = rvG
```

### §11.5.1 ECDH Parameters

**N-475** (§11.5.1) _[lowercase/implied]_ — source lines 5913–5914

> ECDH keys have a hash algorithm parameter for key derivation and a
> symmetric algorithm for key encapsulation.

**N-476** (§11.5.1) — source lines 5916–5921

> For version 6 keys, the following algorithms MUST be used depending
> on the curve.  An implementation MUST NOT generate a version 6 ECDH
> key over any listed curve that uses different KDF or KEK parameters.
> An implementation MUST NOT encrypt any message to a version 6 ECDH
> key over a listed curve that announces a different KDF or KEK
> parameter.

**N-477** (§11.5.1) — source lines 5923–5925

> For version 4 keys, the following algorithms SHOULD be used depending
> on the curve.  An implementation SHOULD only use an AES algorithm as
> a KEK algorithm.

**N-478** (§11.5.1) _[table]_ — source lines 5927–5945

```
        +==================+================+=====================+
        | Curve            | Hash Algorithm | Symmetric Algorithm |
        +==================+================+=====================+
        | NIST P-256       | SHA2-256       | AES-128             |
        +------------------+----------------+---------------------+
        | NIST P-384       | SHA2-384       | AES-192             |
        +------------------+----------------+---------------------+
        | NIST P-521       | SHA2-512       | AES-256             |
        +------------------+----------------+---------------------+
        | brainpoolP256r1  | SHA2-256       | AES-128             |
        +------------------+----------------+---------------------+
        | brainpoolP384r1  | SHA2-384       | AES-192             |
        +------------------+----------------+---------------------+
        | brainpoolP512r1  | SHA2-512       | AES-256             |
        +------------------+----------------+---------------------+
        | Curve25519Legacy | SHA2-256       | AES-128             |
        +------------------+----------------+---------------------+

           Table 30: OpenPGP ECDH KDF and KEK Parameters Registry
```

## §12 Notes on Algorithms

### §12.1 PKCS#1 Encoding in OpenPGP

**N-479** (§12.1) _[lowercase/implied]_ — source lines 5951–5956

> This specification makes use of the PKCS#1 functions EME-PKCS1-v1_5
> and EMSA-PKCS1-v1_5.  However, the calling conventions of these
> functions have changed in the past.  To avoid potential confusion and
> interoperability problems, we are including local copies in this
> document, adapted from those in PKCS#1 v2.1 [RFC8017].  [RFC8017]
> should be treated as the ultimate authority on PKCS#1 for OpenPGP.

_The rest of the paragraph (source lines 5957–5959) states the motivation for a self-contained copy of the PKCS#1 functions and is omitted._

### §12.1.1 EME-PKCS1-v1_5-ENCODE

**N-480** (§12.1.1) _[lowercase/implied]_ — source lines 5963–5988

```
   Input:

   k =  key modulus length in octets.

   M =  message to be encoded; an octet string of length mLen, where
      mLen <= k - 11.

   Output:

   EM =  encoded message; an octet string of length k.

   Error: "message too long".

   1.  Length checking: If mLen > k - 11, output "message too long" and
       stop.

   2.  Generate an octet string PS of length k - mLen - 3 consisting of
       pseudorandomly generated non-zero octets.  The length of PS will
       be at least 8 octets.

   3.  Concatenate PS, the message M, and other padding to form an
       encoded message EM of length k octets as

      EM = 0x00 || 0x02 || PS || 0x00 || M.

   4.  Output EM.
```

### §12.1.2 EME-PKCS1-v1_5-DECODE

**N-481** (§12.1.2) _[lowercase/implied]_ — source lines 5992–6013

```
   Input:

   EM =  encoded message; an octet string.

   Output:

   M =  decoded message; an octet string.

   Error: "decryption error".

   To decode an EME-PKCS1_v1_5 message, separate the encoded message EM
   into an octet string PS consisting of non-zero octets and a message M
   as follows

     EM = 0x00 || 0x02 || PS || 0x00 || M.

   If the first octet of EM does not have hexadecimal value 0x00, the
   second octet of EM does not have hexadecimal value 0x02, there is no
   octet with hexadecimal value 0x00 to separate PS from M, or the
   length of PS is less than 8 octets, output "decryption error" and
   stop.  See also Section 13.5 regarding differences in reporting
   between a decryption error and a padding error.
```

### §12.1.3 EMSA-PKCS1-v1_5

**N-482** (§12.1.3) _[lowercase/implied]_ — source lines 6017–6063

```
   This encoding method is deterministic and only has an encoding
   operation.

   Input:

   Hash =  hash function to be used.

   M =  message to be encoded.

   emLen =  intended length of the encoded message in octets, at least
      tLen + 11, where tLen is the octet length of the DER encoding T of
      a certain value computed during the encoding operation.

   Output:

   EM =  encoded message; an octet string of length emLen.

   Errors: "message too long"; "intended encoded message length too
   short".

   Steps:

   1.  Apply the hash function to the message M to produce hash value H:

       H = Hash(M).

       If the hash function outputs "message too long," output "message
       too long" and stop.

   2.  Let T be the Full Hash Prefix from Table 24 for the given hash
       function, concatenated with the hash digest H (representing an
       ASN.1 DER value for the hash function used and the hash digest).
       Let tLen be the length in octets of T.

   3.  If emLen < tLen + 11, output "intended encoded message length too
       short" and stop.

   4.  Generate an octet string PS consisting of emLen - tLen - 3 octets
       with hexadecimal value 0xFF.  The length of PS will be at least 8
       octets.

   5.  Concatenate PS, the hash prefix T, and other padding to form the
       encoded message EM as

      EM = 0x00 || 0x01 || PS || 0x00 || T.

   6.  Output EM.
```

### §12.2 Symmetric Algorithm Preferences

**N-483** (§12.2) _[lowercase/implied]_ — source lines 6067–6073

> The symmetric algorithm preference is an ordered list of algorithms
> that the keyholder accepts.  Since it is found on a self-signature,
> it is possible that a keyholder may have multiple, different
> preferences.  For example, Alice may have AES-128 only specified for
> "alice@work.com" but Camellia-256, Twofish, and AES-128 specified for
> "alice@home.org".  Note that it is also possible for preferences to
> be in a subkey's binding signature.

**N-484** (§12.2) — source lines 6075–6082

> Since AES-128 is the algorithm that MUST be implemented, if it is not
> explicitly in the list, it is tacitly at the end.  However, it is
> good form to place it there explicitly.  Note also that if an
> implementation does not implement the preference, then it is
> implicitly an AES-128-only implementation.  Furthermore, note that
> implementations conforming to the previous version of this
> specification [RFC4880] have TripleDES as the only algorithm that
> MUST be implemented.

**N-485** (§12.2) — source lines 6084–6089

> An implementation MUST NOT use a symmetric algorithm that is not in
> the recipient's preference list.  When encrypting to more than one
> recipient, the implementation finds a suitable algorithm by taking
> the intersection of the preferences of the recipients.  Note that
> since the AES-128 algorithm MUST be implemented, the intersection is
> guaranteed to be non-empty.

**N-486** (§12.2) — source lines 6091–6099

> If an implementation can decrypt a message that a keyholder doesn't
> have in their preferences, the implementation SHOULD decrypt the
> message anyway, but it MUST warn the keyholder.  For example, suppose
> that Alice (above) has an implementation that implements all
> algorithms in this specification.  Nonetheless, she prefers subsets
> for work or home.  If she is sent a message encrypted with IDEA,
> which is not in her preferences, the implementation warns her that
> someone sent an IDEA-encrypted message, but it would ideally decrypt
> it anyway.

### §12.2.1 Plaintext

**N-487** (§12.2.1) — source lines 6103–6107

> Algorithm 0, "plaintext", may only be used to denote secret keys that
> are stored in the clear.  An implementation MUST NOT use algorithm 0
> as the indicated symmetric cipher for an encrypted data packet
> (Sections 5.7 or 5.13); it can use a Literal Data packet
> (Section 5.9) to encode unencrypted literal data.

### §12.3 Other Algorithm Preferences

**N-488** (§12.3) _[lowercase/implied]_ — source lines 6111–6114

> Other algorithm preferences work similarly to the symmetric algorithm
> preference in that they specify which algorithms the keyholder
> accepts.  There are two interesting cases in which further comments
> are needed: the compression preferences and the hash preferences.

### §12.3.1 Compression Preferences

**N-489** (§12.3.1) — source lines 6118–6121

> Like the algorithm preferences, an implementation MUST NOT use an
> algorithm that is not in the preference vector.  If Uncompressed (0)
> is not explicitly in the list, it is tacitly at the end.  That is,
> uncompressed messages may always be sent.

**N-490** (§12.3.1) — source lines 6123–6127

> Note that earlier implementations may assume that the absence of
> compression preferences means that [ZIP(1), Uncompressed(0)] are
> preferred, and default to ZIP compression.  Therefore, an
> implementation that prefers uncompressed data SHOULD explicitly state
> this in the Preferred Compression Algorithms.

### §12.3.1.1 Uncompressed

**N-491** (§12.3.1.1) — source lines 6131–6135

> Algorithm 0, "uncompressed", may only be used to denote a preference
> for uncompressed data.  An implementation MUST NOT use algorithm 0 as
> the indicated compression algorithm in a Compressed Data packet
> (Section 5.6); it can use a Literal Data packet (Section 5.9) to
> encode uncompressed literal data.

### §12.3.2 Hash Algorithm Preferences

_Source lines 6139–6147 explain why the hash preference exists (signer chooses; recipient states acceptable algorithms) and are omitted as motivation._

**N-492** (§12.3.2) — source lines 6149–6151

> Since SHA2-256 is the hash algorithm that MUST be implemented, if it
> is not explicitly in the list, it is tacitly at the end.  However, it
> is good form to place it there explicitly.

### §12.4 RSA

**N-493** (§12.4) — source lines 6155–6158

> The PKCS1-v1_5 padding scheme, used by the RSA algorithms defined in
> this document, is no longer recommended, and its use is deprecated by
> [SP800-131A].  Therefore, an implementation SHOULD NOT generate RSA
> keys.

**N-494** (§12.4) — source lines 6160–6163

> There are algorithm types for RSA Sign-Only and RSA Encrypt-Only
> keys.  These types are deprecated in favor of the Key Flags signature
> subpacket.  An implementation MUST NOT create such a key, but it MAY
> interpret it.

**N-495** (§12.4) — source lines 6165–6171

> An implementation MUST NOT generate RSA keys of a size less than 3072
> bits.  An implementation SHOULD NOT encrypt, sign, or verify using
> RSA keys of a size less than 3072 bits.  An implementation MUST NOT
> encrypt, sign, or verify using RSA keys of a size less than 2048
> bits.  An implementation that decrypts a message using an RSA secret
> key of a size less than 3072 bits SHOULD generate a deprecation
> warning that the key is too weak for modern use.

### §12.5 DSA

**N-496** (§12.5) — source lines 6175–6176

> DSA is no longer recommended.  It has also been deprecated in
> [FIPS186].  Therefore, an implementation MUST NOT generate DSA keys.

**N-497** (§12.5) — source line 6178

> An implementation MUST NOT sign or verify using DSA keys.

### §12.6 Elgamal

**N-498** (§12.6) — source lines 6182–6185

> The PKCS1-v1_5 padding scheme, used by the Elgamal algorithm defined
> in this document, is no longer recommended, and its use is deprecated
> by [SP800-131A].  Therefore, an implementation MUST NOT generate
> Elgamal keys.

**N-499** (§12.6) — source lines 6187–6190

> An implementation MUST NOT encrypt using Elgamal keys.  An
> implementation that decrypts a message using an Elgamal secret key
> SHOULD generate a deprecation warning that the key is too weak for
> modern use.

### §12.7 EdDSA

**N-500** (§12.7) _[lowercase/implied]_ — source lines 6194–6198

> Although the EdDSA algorithm allows arbitrary data as input, its use
> with OpenPGP requires that a digest of the message be used as input
> (pre-hashed).  See Section 5.2.4 for details.  Truncation of the
> resulting digest is never applied; the resulting digest value is used
> verbatim as input to the EdDSA algorithm.

**N-501** (§12.7) _[lowercase/implied]_ — source lines 6200–6204

> For clarity: while [RFC8032] describes different variants of EdDSA,
> OpenPGP uses the "pure" variant (PureEdDSA).  The hashing that
> happens with OpenPGP is done as part of the standard OpenPGP
> signature process, and that hash itself is fed as the input message
> to the PureEdDSA algorithm.

**N-502** (§12.7) _[lowercase/implied]_ — source lines 6206–6207

> As specified in [RFC8032], Ed448 also expects a "context string".  In
> OpenPGP, Ed448 is used with the empty string as a context string.

### §12.8 Reserved Algorithm IDs

**N-503** (§12.8) _[lowercase/implied]_ — source lines 6211–6214

> A number of algorithm IDs have been reserved for algorithms that
> would be useful to use in an OpenPGP implementation, yet there are
> issues that prevent an implementer from actually implementing the
> algorithm.  These are marked as reserved in Section 9.1.

**N-504** (§12.8) _[lowercase/implied]_ — source lines 6216–6219

> The reserved public key algorithm X9.42 (21) does not have the
> necessary parameters, parameter order, or semantics defined.  The
> same is currently true for reserved public key algorithms AEDH (23)
> and AEDSA (24).

**N-505** (§12.8) — source lines 6221–6225

> Previous versions of the OpenPGP specification permitted Elgamal
> [ELGAMAL] signatures with a public key algorithm ID of 20.  These are
> no longer permitted.  An implementation MUST NOT generate such keys.
> An implementation MUST NOT generate Elgamal signatures; see
> [BLEICHENBACHER].

### §12.9 CFB Mode

**N-506** (§12.9) _[lowercase/implied]_ — source lines 6229–6233

> The Cipher Feedback (CFB) mode used in this document is defined in
> Section 6.3 of [SP800-38A].
>
> The CFB segment size s is equal to the block size of the cipher
> (i.e., n-bit CFB mode, where n is the block size used).

### §12.10 Private or Experimental Parameters

**N-507** (§12.10) _[lowercase/implied]_ — source lines 6237–6246

> S2K Specifiers, Signature Subpacket Type IDs, User Attribute
> Subpacket Type IDs, image format IDs, and the various algorithm IDs
> described in Section 9 all reserve the range 100 to 110 for Private
> and Experimental Use. Packet Type IDs reserve the range 60 to 63 for
> Private and Experimental Use. These are intentionally managed by the
> Private Use and Experimental Use policies, as described in [RFC8126].
>
> However, implementations need to be careful with these and promote
> them to full IANA-managed parameters when they grow beyond the
> original, limited system.

### §12.11 Meta Considerations for Expansion

**N-508** (§12.11) _[lowercase/implied]_ — source lines 6250–6254

> If OpenPGP is extended in a way that is not backward compatible,
> meaning that old implementations will not gracefully handle their
> absence of a new feature, the extension proposal can be declared in
> the keyholder's self-signature as part of the Features signature
> subpacket.

_Source lines 6256–6258 (which extensions are typically forward compatible) are an observation, not a rule, and are omitted._

**N-509** (§12.11) — source lines 6260–6264

> If an extension proposal does not update the Features system, it
> SHOULD include an explanation of why this is unnecessary.  If the
> proposal contains neither an extension to the Features system nor an
> explanation of why such an extension is unnecessary, the proposal
> SHOULD be rejected.

## §13 Security Considerations

**N-510** (§13) _[lowercase/implied]_ — source lines 6268–6274

> *  As with any technology involving cryptography, implementers should
>    check the current literature to determine if any algorithms used
>    here have been found to be vulnerable to an attack.  If so,
>    implementers should consider disallowing such algorithms for new
>    data and warning the end user, or preventing use, when they are
>    trying to consume data protected by such algorithms that are now
>    vulnerable.

_Source lines 6276–6278 (the private key is assumed to be controlled by the proper party) state an assumption of the security model and are omitted._

**N-511** (§13) _[lowercase/implied]_ — source lines 6280–6282

> *  The MD5 and SHA-1 hash algorithms have been found to have
>    weaknesses, with collisions found in a number of cases.  MD5 and
>    SHA-1 are deprecated for use in OpenPGP (see Section 9.5).

**N-512** (§13) _[lowercase/implied]_ — source lines 6284–6289

> *  Many security protocol designers think that it is a bad idea to
>    use a single key for both privacy (encryption) and integrity
>    (signatures).  In fact, this was one of the motivating forces
>    behind the version 4 key format with separate signature and
>    encryption keys.  Using a single key for encrypting and signing is
>    discouraged.

**N-513** (§13) _[lowercase/implied]_ — source lines 6291–6295

> *  The DSA algorithm will work with any hash, but it is sensitive to
>    the quality of the hash algorithm.  Verifiers should be aware that
>    even if the signer used a strong hash, an attacker could have
>    modified the signature to use a weak one.  Only signatures using
>    acceptably strong hash algorithms should be accepted as valid.

**N-514** (§13) _[lowercase/implied]_ — source lines 6297–6304

> *  As OpenPGP combines many different asymmetric, symmetric, and hash
>    algorithms, each with different measures of strength, care should
>    be taken to ensure that the weakest element of an OpenPGP Message
>    is still sufficiently strong for the purpose at hand.  While
>    consensus about the strength of a given algorithm may evolve, NIST
>    Special Publication 800-57 [SP800-57] contains recommendations
>    (current at the time of this publication) about equivalent
>    security levels of different algorithms.

_Source lines 6306–6317 describe a cross-hash-algorithm signature forgery scenario (Alice, Mallet, H and H') and are omitted as motivation._

**N-515** (§13) _[lowercase/implied]_ — source lines 6319–6322

> *  If you are building an authentication system, the recipient may
>    specify a preferred signing algorithm.  However, the signer would
>    be foolish to use a weak algorithm simply because the recipient
>    requests it.

_Source lines 6324–6328 (some ciphers analysed less than others, e.g. TWOFISH) and 6330–6339 (history of the 2002 Jallad, Katz and Schneier attack; points to §13.7) are omitted as motivation and history._

### §13.1 SHA-1 Collision Detection

**N-516** (§13.1) _[lowercase/implied]_ — source lines 6343–6349

> As described in [SHAMBLES], the SHA-1 digest algorithm is not
> collision resistant.  However, an OpenPGP implementation cannot
> completely discard the SHA-1 algorithm, because it is required for
> implementing version 4 public keys.  In particular, the version 4
> fingerprint derivation uses SHA-1.  So as long as an OpenPGP
> implementation supports version 4 public keys, it will need to
> implement SHA-1 in at least some scenarios.

**N-517** (§13.1) — source lines 6351–6357

> To avoid the risk of uncertain breakage from a maliciously introduced
> SHA-1 collision, an OpenPGP implementation MAY attempt to detect when
> a hash input is likely from a known collision attack and then either
> reject the hash input deliberately or modify the hash output.  This
> should convert an uncertain breakage (where it is unclear what the
> effect of a collision will be) to an explicit breakage, which is more
> desirable for a robust implementation.

_Source lines 6359–6361 point to [STEVENS2013] and [SHA1CD] for a collision-detection method and code; omitted (reference pointer)._

### §13.2 Advantages of Salted Signatures

**N-518** (§13.2) _[lowercase/implied]_ — source lines 6365–6366

> Version 6 signatures include a salt that is hashed first, and it's
> size depends on the hashing algorithm.

_The rest of source lines 6366–6380 explains why salting defeats chosen-prefix collision attacks ([SHAMBLES]) and is omitted as motivation._

**N-519** (§13.2) _[lowercase/implied]_ — source lines 6380–6382

> The size of the salt is bound to
> the hash function to match the expected collision-resistance level
> and is at least 16 octets.

_Source lines 6384–6389 (fault attacks on repeated signatures, [PSSLR17]) are omitted as motivation._

**N-520** (§13.2) _[lowercase/implied]_ — source lines 6389–6390

> Choosing a new random salt for each signature ensures
> that no repeated signatures are produced, which mitigates this risk.

### §13.3 Elliptic Curve Side Channels

_No entry: source lines 6394–6404 describe side-channel exposure of ECC scalar multiplication and possible countermeasures; they state no requirement._

### §13.4 Risks of a Quick Check Oracle

_Source lines 6408–6419 give the history of the Mister–Zuccherato quick-check oracle [MZ05] and the conditions under which it is dangerous; omitted as motivation._

**N-521** (§13.4) _[lowercase/implied]_ — source line 6421

> Disabling the quick check prevents the attack.

**N-522** (§13.4) _[lowercase/implied]_ — source lines 6423–6431

> For very large encrypted data whose session key is protected by a
> passphrase using a v4 SKESK, the quick check may be convenient to the
> user by informing them early that they typed the wrong passphrase.
> But the implementation should use the quick check with care.  The
> recommended approach for secure and early detection of decryption
> failure is to encrypt data using v2 SEIPD.  If the session key is
> public key encrypted, the quick check is not useful as the public key
> encryption of the session key should guarantee that it is the right
> session key.

_Source lines 6433–6435 classify the attack as ciphertext malleability and point to §13.7; omitted._

### §13.5 Avoiding Leaks from PKCS#1 Errors

_Source lines 6439–6446 describe Bleichenbacher-style padding-oracle attacks [BLEICHENBACHER-PKCS1]; omitted as motivation._

**N-523** (§13.5) — source lines 6448–6449

> To make the attack more difficult, an implementation SHOULD implement
> strict, robust, and constant time padding checks.

**N-524** (§13.5) _[lowercase/implied]_ — source lines 6451–6461

> To prevent the attack, in settings where the attacker does not have
> access to timing information concerning message decryption, the
> simplest solution is to report a single error code for all variants
> of PKESK processing errors as well as SEIPD integrity errors (this
> also includes session key parsing errors, such as on an invalid
> cipher algorithm for v3 PKESK, or a session key size mismatch for v6
> PKESK).  If the attacker may have access to timing information, then
> a constant time solution is also needed.  This requires careful
> design, especially for v3 PKESK, where session key size and cipher
> information is typically not known in advance, as it is part of the
> PKESK encrypted payload.

### §13.6 Fingerprint Usability

_Source lines 6465–6485 describe where fingerprints are used and why human comparison of them is unreliable [USENIX-STUDY]; omitted as motivation._

**N-525** (§13.6) — source lines 6487–6490

> An OpenPGP implementation should prioritize mechanical fingerprint
> transfer and comparison where possible and SHOULD NOT promote manual
> transfer or comparison of full fingerprints by a human unless there
> is no other way to achieve the desired result.

**N-526** (§13.6) _[lowercase/implied]_ — source lines 6492–6495

> While this subsection acknowledges existing practice for human-
> representable version 4 fingerprints, this document does not attempt
> to standardize any specific human-readable form of version 6
> fingerprint for this discouraged use case.

_Source lines 6497–6498 (a NOTE that human-in-the-loop key verification is left to a separate document) are omitted._

### §13.7 Avoiding Ciphertext Malleability

**N-527** (§13.7) _[lowercase/implied]_ — source lines 6502–6503

> If ciphertext can be modified by an attacker but still subsequently
> decrypted to some new plaintext, it is considered "malleable".

_The rest of the paragraph (source lines 6503–6509: OpenPGP data predating the defences may be encountered) is omitted as motivation._

**N-528** (§13.7) — source lines 6511–6517

> When an OpenPGP implementation discovers that it is decrypting data
> that appears to be malleable, it MUST generate a clear error message
> that indicates the integrity of the message is suspect, it SHOULD NOT
> attempt to parse nor release decrypted data to the user, and it
> SHOULD halt with an error.  Parsing or releasing decrypted data
> before having confirmed its integrity can leak the decrypted data
> [EFAIL] [MRLG15].

**N-529** (§13.7) — source lines 6519–6521

> In the case of AEAD encrypted data, if the authentication tag fails
> to verify, the implementation MUST NOT attempt to parse nor release
> decrypted data to the user, and it MUST halt with an error.

**N-530** (§13.7) — source lines 6523–6526

> An implementation that encounters malleable ciphertext MAY choose to
> release cleartext to the user if it is not encrypted using AEAD, it
> is known to be dealing with historic archived legacy data, and the
> user is aware of the risks.

**N-531** (§13.7) — source lines 6528–6533

> In the case of AEAD encrypted messages, if the message is truncated,
> i.e., the final zero-octet chunk and possibly (part of) some chunks
> before it are missing, the implementation MAY choose to release
> cleartext from the fully authenticated chunks before it to the user
> if it is operating in a streaming fashion, but it MUST indicate a
> clear error message as soon as the truncation is detected.

**N-532** (§13.7) _[lowercase/implied]_ — source lines 6535–6560

```
   Any of the following OpenPGP data elements indicate that malleable
   ciphertext is present:

   *  All Symmetrically Encrypted Data packets (Section 5.7).

   *  Within any encrypted container, any Compressed Data packet
      (Section 5.6) where there is a decompression failure.

   *  Any version 1 Symmetrically Encrypted and Integrity Protected Data
      packet (Section 5.13.1) where the internal Modification Detection
      Code does not validate.

   *  Any version 2 Symmetrically Encrypted and Integrity Protected Data
      packet (Section 5.13.2) where the authentication tag of any chunk
      fails or where there is no final zero-octet chunk.

   *  Any Secret-Key packet with encrypted secret key material
      (Section 3.7.2.1) where there is an integrity failure, based on
      the value of the secret key protection octet:

      -  Value 253 (AEAD): where the AEAD authentication tag is invalid.

      -  Value 254 (CFB): where the SHA1 checksum is mismatched.

      -  Value 255 (MalleableCFB) or raw cipher algorithm: where the
         trailing 2-octet checksum does not match.
```

**N-533** (§13.7) — source lines 6562–6565

> To avoid these circumstances, an implementation that generates
> OpenPGP encrypted data SHOULD select the encrypted container format
> with the most robust protections that can be handled by the intended
> recipients.  In particular:

**N-534** (§13.7) — source lines 6567–6590

```
   *  The SED packet is deprecated and MUST NOT be generated.

   *  When encrypting to one or more public keys:

      -  If all recipient keys indicate support for a version 2
         Symmetrically Encrypted and Integrity Protected Data packet in
         their Features signature subpacket (Section 5.2.3.32), if all
         recipient keys are version 6 keys without a Features signature
         subpacket, or the implementation can otherwise infer that all
         recipients support v2 SEIPD packets, the implementation SHOULD
         encrypt using a v2 SEIPD packet.

      -  If one of the recipients does not support v2 SEIPD packets,
         then the message generator MAY use a v1 SEIPD packet instead.

   *  Passphrase-protected secret key material in a version 6 Secret Key
      or version 6 Secret Subkey packet SHOULD be protected with AEAD
      encryption (S2K usage octet 253) unless it will be transferred to
      an implementation that is known to not support AEAD.  An
      implementation should be aware that, in scenarios where an
      attacker has write access to encrypted private keys, CFB-encrypted
      keys (S2K usage octet 254 or 255) are vulnerable to corruption
      attacks that can cause leakage of secret data when the secret key
      is used [KOPENPGP] [KR02].
```

**N-535** (§13.7) _[lowercase/implied]_ — source lines 6592–6593

> Implementers should implement AEAD (v2 SEIPD and S2K usage octet 253)
> promptly and encourage its spread.

**N-536** (§13.7) — source line 6595

> Users are RECOMMENDED to migrate to AEAD.

### §13.8 Secure Use of the v2 SEIPD Session-Key-Reuse Feature

**N-537** (§13.8) _[lowercase/implied]_ — source lines 6599–6609

> The salted key derivation of v2 SEIPD packets (Section 5.13.2) allows
> the recipient of an encrypted message to reply to the sender and all
> other recipients without needing their public keys but by using the
> same v6 PKESK packets it received and a different random salt value.
> This ensures a secure mechanism on the cryptographic level that
> enables the use of message encryption in cases where a sender does
> not have a copy of an encryption-capable certificate for one or more
> participants in the conversation and thus can enhance the overall
> security of an application.  However, care must be taken when using
> this mechanism not to create security vulnerabilities, such as the
> following:

**N-538** (§13.8) _[lowercase/implied]_ — source lines 6611–6660

```
   *  Replying to only a subset of the original recipients and the
      original sender by use of the session-key-reuse feature would mean
      that the remaining recipients (including the sender) of the
      original message could read the encrypted reply message, too.

   *  Adding a further recipient to the reply that is encrypted using
      the session-key-reuse feature gives that further recipient also
      cryptographic access to the original message that is being replied
      to (and potentially to a longer history of previous messages).

   *  A modification of the list of recipients addressed in the above
      points also needs to be safeguarded when a message is initially
      composed as a reply with session-key reuse but then is stored
      (e.g., as a draft) and later reopened for further editing and to
      be finally sent.

   *  There is the potential threat that an attacker with network or
      mailbox access, who is at the same time a recipient of the
      original message, silently removes themselves from the message
      before the victim's client receives it.  The victim's client that
      then uses the mechanism for replying with session-key reuse would
      unknowingly compose an encrypted message that could be read by the
      attacker.  Implementations are encouraged to use the Intended
      Recipient Fingerprint subpacket (Section 5.2.3.36) when composing
      messages and checking the consistency of the set of recipients of
      a message before replying to it with session-key reuse.

   *  When using the session-key-reuse feature in any higher-layer
      protocol, care should be taken to ensure that there is no other
      potentially interfering practice of session-key reuse established
      in that protocol.  Such interfering session-key reuse could, for
      instance, be given -- if an initial message is already composed --
      by reusing the session key of an existing encrypted file that may
      have been shared among a group of users already.  Using the
      session-key-reuse feature to compose an encrypted reply to such a
      message would unknowingly give this whole group of users
      cryptographic access to the encrypted message.

   *  Generally, the use of the session-key-reuse feature should be
      under the control of the user.  Specifically, care should be taken
      so that this feature is not silently used when the user assumes
      that proper public key encryption is used.  This can be the case,
      for instance, when the public key of one of the recipients of the
      reply is known but has expired.  Special care should be taken to
      ensure that users do not get caught in continued use of the
      session-key reuse unknowingly but instead receive the chance to
      switch to proper fresh public key encryption as soon as possible.

   *  Whenever possible, a client should prefer a fresh public key
      encryption over the session-key reuse.
```

_Source lines 6662–6667 (a draft composed with session-key reuse and reopened in a client without the feature may not interoperate) are noted by the source as not a security aspect; omitted._

**N-539** (§13.8) _[lowercase/implied]_ — source lines 6669–6677

> Avoiding the pitfalls described above requires context-specific
> expertise.  An implementation should only make use of the session-
> key-reuse feature in any particular application layer when it can
> follow reasonable documentation about how to deploy the feature
> safely in the specific application.  At the time of this writing,
> there is no known documentation about safe reuse of OpenPGP session
> keys for any specific context.  An implementer that intends to make
> use of this feature should publish their own proposed guidance for
> others to review.

### §13.9 Escrowed Revocation Signatures

**N-540** (§13.9) _[lowercase/implied]_ — source lines 6681–6682

> A keyholder, Alice, may wish to designate a third party to be able to
> revoke her own key.

**N-541** (§13.9) _[lowercase/implied]_ — source lines 6684–6689

> The preferred way for Alice to do this is to produce a specific
> Revocation Signature (Signature Type ID 0x20, 0x28, or 0x30) and
> distribute it securely to a preferred revoker who can hold it in
> escrow.  The preferred revoker can then publish the escrowed
> Revocation Signature at whatever time is deemed appropriate rather
> than generating the Revocation Signature themselves.

**N-542** (§13.9) _[lowercase/implied]_ — source lines 6691–6712

Kept in full although it is rationale: it is the stated case for escrowed Revocation Signatures over the deprecated Revocation Key subpacket (§5.2.3.23).

```
   There are multiple advantages of using an escrowed Revocation
   Signature over the deprecated Revocation Key subpacket
   (Section 5.2.3.23):

   *  The keyholder can constrain what types of revocation the preferred
      revoker can issue, by only escrowing those specific signatures.

   *  There is no public/visible linkage between the keyholder and the
      preferred revoker.

   *  Third parties can verify the revocation without needing to find
      the key of the preferred revoker.

   *  The preferred revoker doesn't even need to have a public OpenPGP
      Key if some other secure transport is possible between them and
      the keyholder.

   *  Implementation support for enforcing a revocation from an
      authorized Revocation Key subpacket is uneven and unreliable.

   *  If the fingerprint mechanism suffers a cryptanalytic flaw, the
      escrowed Revocation Signature is not affected.
```

**N-543** (§13.9) _[lowercase/implied]_ — source lines 6714–6717

> A Revocation Signature may also be split up into shares and
> distributed among multiple parties, requiring some subset of those
> parties to collaborate before the escrowed Revocation Signature is
> recreated.

### §13.10 Random Number Generation and Seeding

**N-544** (§13.10) — source lines 6721–6729

> OpenPGP requires a cryptographically secure pseudorandom number
> generator (CSPRNG).  In most cases, the operating system provides an
> appropriate facility such as a getrandom() syscall on Linux or BSD,
> which should be used absent other (for example, performance)
> concerns.  It is RECOMMENDED to use an existing CSPRNG implementation
> as opposed to crafting a new one.  Many adequate cryptographic
> libraries are already available under favorable license terms.
> Should those prove unsatisfactory, [RFC4086] provides guidance on the
> generation of random values.

**N-545** (§13.10) _[lowercase/implied]_ — source lines 6731–6739

```
   OpenPGP uses random data with three different levels of visibility:

   *  In publicly visible fields such as nonces, IVs, public padding
      material, or salts.

   *  In shared-secret values, such as session keys for encrypted data
      or padding material within an encrypted packet.

   *  In entirely private data, such as asymmetric key generation.
```

_Source lines 6741–6746 (a broken CSPRNG lets visible output reveal less-visible data, [CHECKOWAY]) are omitted as motivation._

**N-546** (§13.10) _[lowercase/implied]_ — source lines 6748–6750

> An implementation can provide extra security against this form of
> attack by using separate CSPRNGs to generate random data with
> different levels of visibility.

### §13.11 Traffic Analysis

_Source lines 6754–6770 describe length-based leaks (yes/no messages; certificate length over an encrypted channel); omitted as motivation._

**N-547** (§13.11) _[lowercase/implied]_ — source lines 6772–6773

> In both cases, an implementation can adjust the size of the compound
> structure by including a Padding packet (see Section 5.14).

### §13.12 Surreptitious Forwarding

**N-548** (§13.12) — source lines 6777–6782

> When an attacker obtains a signature for some text, e.g., by
> receiving a signed message, they may be able to use that signature
> maliciously by sending a message purporting to come from the original
> sender, with the same body and signature, to a different recipient.
> To prevent this, an implementation SHOULD implement the Intended
> Recipient Fingerprint subpacket (Section 5.2.3.36).

### §13.13 Hashed vs. Unhashed Subpackets

**N-549** (§13.13) _[lowercase/implied]_ — source lines 6786–6790

> Each OpenPGP signature can have subpackets in two different sections.
> The first set of subpackets (the "hashed section") is covered by the
> signature itself.  The second set has no cryptographic protections
> and is used for advisory material only, including locally stored
> annotations about the signature.

**N-550** (§13.13) — source lines 6792–6798

> For example, consider an implementation working with a specific
> signature that happens to know that the signature was made by a
> certain key, even though the signature contains no Issuer Fingerprint
> subpacket (Section 5.2.3.35) in the hashed section.  That
> implementation MAY synthesize an Issuer Fingerprint subpacket and
> store it in the unhashed section so that it will be able to recall
> which key issued the signature in the future.

**N-551** (§13.13) — source lines 6800–6808

> Some subpackets are only useful when they are in the hashed section,
> and an implementation SHOULD ignore them when they are found with
> unknown provenance in the unhashed section.  For example, a Preferred
> AEAD Ciphersuites subpacket (Section 5.2.3.15) in a Direct Key self-
> signature indicates the preferences of the keyholder when encrypting
> v2 SEIPD data to the key.  An implementation that observes such a
> subpacket found in the unhashed section would open itself to an
> attack where the recipient's certificate is tampered with to
> encourage the use of a specific cipher or mode of operation.

### §13.14 Malicious Compressed Data

_Source lines 6812–6817 describe compression quines and crash-report leakage; omitted as motivation._

**N-552** (§13.14) — source lines 6819–6820

> An OpenPGP implementation SHOULD limit the number of layers of
> compression it is willing to decompress in a single message.

## §14 Implementation Considerations

_Source lines 6824–6829 introduce the section as a non-comprehensive list of backward-compatibility gotchas; omitted._

**N-553** (§14) _[lowercase/implied]_ — source lines 6831–6836

> *  There are many possible ways for two keys to have the same key
>    material but different fingerprints (and thus different Key IDs).
>    For example, since a version 4 fingerprint is constructed by
>    hashing the key creation time along with other things, two version
>    4 keys created at different times yet with the same key material
>    will have different fingerprints.

**N-554** (§14) _[lowercase/implied]_ — source lines 6838–6843

> *  OpenPGP does not put limits on the size of public keys.  However,
>    larger keys are not necessarily better keys.  Larger keys take
>    more computation time to use, and this can quickly become
>    impractical.  Different OpenPGP implementations may also use
>    different upper bounds for public key sizes, so care should be
>    taken when choosing sizes to maintain interoperability.

**N-555** (§14) _[lowercase/implied]_ — source lines 6845–6859

> *  ASCII Armor is an optional feature of OpenPGP.  The OpenPGP
>    Working Group strives for a minimal set of mandatory-to-implement
>    features, and since there could be useful implementations that
>    only use binary object formats, this is not a "MUST" feature for
>    an implementation.  For example, an implementation that is using
>    OpenPGP as a mechanism for file signatures may find ASCII Armor
>    unnecessary.  OpenPGP permits an implementation to declare what
>    features it does and does not support, but ASCII Armor is not one
>    of these.  Since most implementations allow binary and armored
>    objects to be used indiscriminately, an implementation that does
>    not implement ASCII Armor may find itself with compatibility
>    issues with general-purpose implementations.  Moreover,
>    implementations of OpenPGP-MIME [RFC3156] already have a
>    requirement for ASCII Armor, so those implementations will
>    necessarily have support.

**N-556** (§14) _[lowercase/implied]_ — source lines 6861–6867

> *  What this document calls the "Legacy packet format"
>    (Section 4.2.2) is what older documents called the "old packet
>    format".  It is the packet format used by implementations
>    predating [RFC2440].  The current "OpenPGP packet format"
>    (Section 4.2.1) was called the "new packet format" by older RFCs.
>    This is the format introduced in [RFC2440] and maintained through
>    [RFC4880] to this document.

### §14.1 Constrained Legacy Fingerprint Storage for Version 6 Keys

**N-557** (§14.1) _[lowercase/implied]_ — source lines 6871–6874

> Some OpenPGP implementations have fixed length constraints for key
> fingerprint storage that will not fit all 32 octets of a version 6
> fingerprint.  For example, [OPENPGPCARD] reserves 20 octets for each
> stored fingerprint.

**N-558** (§14.1) — source lines 6876–6883

> An OpenPGP implementation MUST NOT attempt to map any part of a
> version 6 fingerprint to such a constrained field unless the relevant
> specification for the constrained environment has explicit guidance
> for storing a version 6 fingerprint that distinguishes it from a
> version 4 fingerprint.  An implementation interacting with such a
> constrained field SHOULD directly calculate the version 6 fingerprint
> from public key material and associated metadata instead of relying
> on the constrained field.

## §15 IANA Considerations

**N-559** (§15) _[IANA action]_ — source lines 6887–6888

> This document obsoletes [RFC4880].  IANA has updated all registration
> information that references [RFC4880] to reference this RFC instead.

### §15.1 Renamed Protocol Group

**N-560** (§15.1) _[IANA action]_ — source lines 6892–6899

> IANA bundles a set of registries associated with a particular
> protocol into a "protocol group".  IANA has updated the name of the
> "Pretty Good Privacy (PGP)" protocol group (i.e., the group of
> registries described at <https://www.iana.org/assignments/pgp-
> parameters>) to "OpenPGP".  IANA has arranged a permanent redirect
> from the existing URL to the new URL for the registries in this
> protocol group.  All further updates specified below are for
> registries within this same OpenPGP protocol group.

### §15.2 Renamed and Updated Registries

**N-561** (§15.2) _[IANA action]_ — source lines 6903–6948

> IANA has renamed the "PGP String-to-Key (S2K)" registry to "OpenPGP
> String-to-Key (S2K) Types" and updated its contents as shown in
> Table 1.
>
> IANA has renamed the "PGP Packet Types/Tags" registry to "OpenPGP
> Packet Types" and updated its contents as shown in Table 3.
>
> IANA has renamed the "Signature Subpacket Types" registry to "OpenPGP
> Signature Subpacket Types" and updated its contents as shown in
> Table 5.
>
> IANA has renamed the "Key Server Preference Extensions" registry to
> "OpenPGP Key Server Preference Flags" and updated its contents as
> shown in Table 8.
>
> IANA has renamed the "Key Flags Extensions" registry to "OpenPGP Key
> Flags" and updated its contents as shown in Table 9.
>
> IANA has renamed the "Reason for Revocation Extensions" registry to
> "OpenPGP Reason for Revocation (Revocation Octet)" and updated its
> contents as shown in Table 10.
>
> IANA has renamed the "Implementation Features" registry to "OpenPGP
> Features Flags" and updated its contents as shown in Table 11.
>
> IANA has renamed the "PGP User Attribute Types" registry to "OpenPGP
> User Attribute Subpacket Types" and updated its contents as shown in
> Table 13.
>
> IANA has renamed the "Image Format Subpacket Types" registry to
> "OpenPGP Image Attribute Encoding Format" and updated its contents as
> shown in Table 15.
>
> IANA has renamed the "Public Key Algorithms" registry to "OpenPGP
> Public Key Algorithms" and updated its contents as shown in Table 18.
>
> IANA has renamed the "Symmetric Key Algorithms" registry to "OpenPGP
> Symmetric Key Algorithms" and updated its contents as shown in
> Table 21.
>
> IANA has renamed the "Compression Algorithms" registry to "OpenPGP
> Compression Algorithms" and updated its contents as shown in
> Table 22.
>
> IANA has renamed the "Hash Algorithms" registry to "OpenPGP Hash
> Algorithms" and updated its contents as shown in Table 23.

### §15.3 Removed Registry

**N-562** (§15.3) _[IANA action]_ — source line 6952

> IANA has marked the empty "New Packet Versions" registry as OBSOLETE.

**N-563** (§15.3) _[IANA action]_ — source lines 6954–6961

```
   A tombstone note has been added to the OpenPGP protocol group with
   the following content:

   |  Those wishing to use the removed "New Packet Versions" registry
   |  should instead register new versions of the relevant packets in
   |  the "OpenPGP Key and Signature Versions", "OpenPGP Key IDs and
   |  Fingerprints", and "OpenPGP Encrypted Message Packet Versions"
   |  registries.
```

### §15.4 Added Registries

**N-564** (§15.4) _[IANA action]_ — source lines 6965–7003

```
   IANA has added the following registries in the OpenPGP protocol
   group.  Note that the initial contents of each registry is shown in
   the corresponding table.

   *  "OpenPGP Secret Key Encryption (S2K Usage Octet)" (Table 2).

   *  "OpenPGP Signature Types" (Table 4).

   *  "OpenPGP Signature Notation Data Subpacket Notation Flags"
      (Table 6).

   *  "OpenPGP Signature Notation Data Subpacket Types" (Table 7).

   *  "OpenPGP Key IDs and Fingerprints" (Table 12).

   *  "OpenPGP Image Attribute Versions" (Table 14).

   *  "OpenPGP Armor Header Lines" (Table 16).

   *  "OpenPGP Armor Header Keys" (Table 17).

   *  "OpenPGP ECC Curve OIDs and Usage" (Table 19).

   *  "OpenPGP ECC Curve-Specific Wire Formats" (Table 20).

   *  "OpenPGP Hash Algorithm Identifiers for RSA Signatures' Use of
      EMSA-PKCS1-v1_5 Padding" (Table 24).

   *  "OpenPGP AEAD Algorithms" (Table 25).

   *  "OpenPGP Encrypted Message Packet Versions" (Table 26).

   *  "OpenPGP Key and Signature Versions" (Table 27).

   *  "OpenPGP Elliptic Curve Point Wire Formats" (Table 28).

   *  "OpenPGP Elliptic Curve Scalar Encodings" (Table 29).

   *  "OpenPGP ECDH KDF and KEK Parameters" (Table 30).
```

### §15.5 Registration Policies

**N-565** (§15.5) _[IANA action]_ _[lowercase/implied]_ — source lines 7007–7014

> All registries within the OpenPGP protocol group, with the exception
> of the registries listed in Section 15.5.1, use the Specification
> Required registration policy; see Section 4.6 of [RFC8126].  This
> policy means that review and approval by a designated expert is
> required and that the IDs and their meanings must be documented in a
> permanent and readily available public specification, in sufficient
> detail, so that interoperability between independent implementations
> is possible.

### §15.5.1 Registries That Use RFC Required

**N-566** (§15.5.1) _[IANA action]_ — source lines 7018–7027

```
   The following registries use the RFC Required registration policy, as
   described in Section 4.7 of [RFC8126]:

   *  "OpenPGP Packet Types" (Table 3).

   *  "OpenPGP Key IDs and Fingerprints" (Table 12).

   *  "OpenPGP Encrypted Message Packet Versions" (Table 26).

   *  "OpenPGP Key and Signature Versions" (Table 27).
```

### §15.6 Designated Experts

**N-567** (§15.6) _[IANA action]_ _[lowercase/implied]_ — source lines 7031–7038

> The designated experts will determine whether the new registrations
> retain the security properties that are expected by the base
> implementation and whether these new registrations do not cause
> interoperability issues with existing implementations, other than not
> producing or consuming the IDs associated with these new
> registrations.  Registration proposals that fail to meet these
> criteria could instead be proposed as new work items for the OpenPGP
> Working Group or its successor.

_Source lines 7040–7041 introduce the subsections; omitted._

**N-568** (§15.6) _[IANA action]_ _[lowercase/implied]_ — source lines 7043–7044

> The designated experts should also consider Section 12.11 when
> reviewing proposed additions to the OpenPGP protocol group.

### §15.6.1 Key and Signature Versions

**N-569** (§15.6.1) _[IANA action]_ _[lowercase/implied]_ — source lines 7048–7051

> When defining a new version of OpenPGP Keys or Signatures, the
> "OpenPGP Key and Signature Versions" registry (Table 27) should be
> updated.  When a new version of OpenPGP Key is defined, the "OpenPGP
> Key IDs and Fingerprints" registry (Table 12) should also be updated.

### §15.6.2 Encryption Versions

**N-570** (§15.6.2) _[IANA action]_ _[lowercase/implied]_ — source lines 7055–7061

> When defining a new version of the Symmetrically Encrypted and
> Integrity Protected Data packet (Section 5.13), Public Key Encrypted
> Session Key packet (Section 5.1), and/or Symmetric Key Encrypted
> Session Key packet (Section 5.3), the "OpenPGP Encrypted Message
> Packet Versions" registry (Table 26) should be updated.  When the
> SEIPD is updated, consider also adding a corresponding flag to the
> "OpenPGP Features Flags" registry (Table 11).

### §15.6.3 Algorithms

_Source lines 7065–7069 introduce the algorithm-registry subsections; omitted._

### §15.6.3.1 Elliptic Curve Algorithms

**N-571** (§15.6.3.1) _[IANA action]_ _[lowercase/implied]_ — source lines 7073–7082

> To register a new elliptic curve for use with OpenPGP, its OID needs
> to be registered in the "OpenPGP ECC Curve OIDs and Usage" registry
> (Table 19), its wire format needs to be documented in the "OpenPGP
> ECC Curve-Specific Wire Formats" registry (Table 20), and if used for
> ECDH, its KDF and KEK parameters must be populated in the "OpenPGP
> ECDH KDF and KEK Parameters" registry (Table 30).  If the wire
> format(s) used is not already defined in the "OpenPGP Elliptic Curve
> Point Wire Formats" (Table 28) or "OpenPGP Elliptic Curve Scalar
> Encodings" (Table 29) registries, they should be defined there as
> well.

### §15.6.3.2 Symmetric Key Algorithms

**N-572** (§15.6.3.2) _[IANA action]_ _[lowercase/implied]_ — source lines 7086–7096

> When registering a new symmetric cipher with a block size of 64 or
> 128 bits and a key size that is a multiple of 64 bits, no new
> considerations are needed.
>
> If the new cipher has a different block size, there needs to be
> additional documentation describing how to use the cipher in CFB
> mode.
>
> If the new cipher has an unusual key size, then padding needs to be
> considered for X25519 and X448 key wrapping, which currently needs no
> padding.

### §15.6.3.3 Hash Algorithms

**N-573** (§15.6.3.3) _[IANA action]_ _[lowercase/implied]_ — source lines 7100–7104

> When registering a new hash algorithm in the "OpenPGP Hash
> Algorithms" registry (Table 23), if the algorithm is also to be used
> with RSA signing schemes, it must also have an entry in the "OpenPGP
> Hash Algorithm Identifiers for RSA Signatures' Use of EMSA-PKCS1-v1_5
> Padding" registry (Table 24).

## §16 References

_§16 (source lines 7106–7574: §16.1 Normative References 7108–7304, §16.2 Informative References 7305–7574) is a bibliography. Not reproduced; it carries no normative statement and no BCP 14 keyword._

## Appendix A Test Vectors

**N-574** (Appendix A) _[non-normative]_ — source lines 7577–7578

> To help with the implementation of this specification, a set of non-
> normative examples follow.

### Appendix A.1 Sample Version 4 Ed25519Legacy Key

**N-575** (Appendix A.1) _[test vector]_ — source lines 7586–7588

Vector A.1: source lines 7580–7612. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> Note that this is the raw secret key used as input to the EdDSA
> signing operation.  The key was created on 2014-08-19 14:28:27 and
> thus the fingerprint of the OpenPGP Key is:

### Appendix A.2 Sample Version 4 Ed25519Legacy Signature

**N-576** (Appendix A.2) _[test vector]_ — source lines 7616–7618

Vector A.2: source lines 7614–7648. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> The signature is created using the sample key over the input data
> "OpenPGP" on 2015-09-16 12:24:53 UTC and thus the input to the hash
> function is:

### Appendix A.3 Sample Version 6 Certificate (Transferable Public Key)

**N-577** (Appendix A.3) _[test vector]_ — source lines 7652–7660

Vector A.3: source lines 7650–7684. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> Here is a Transferable Public Key consisting of:
>
> *  A version 6 Ed25519 Public Key packet
>
> *  A version 6 Direct Key self-signature
>
> *  A version 6 X25519 Public Subkey packet
>
> *  A version 6 Subkey Binding signature

### Appendix A.3.1 Hashed Data Stream for Signature Verification

**N-578** (Appendix A.3.1) _[test vector]_ — source lines 7688–7689

Vector A.3.1: source lines 7686–7854. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> The Direct Key self-signature in the certificate in Appendix A.3 is
> made over the following sequence of data:

### Appendix A.4 Sample Version 6 Secret Key (Transferable Secret Key)

**N-579** (Appendix A.4) _[test vector]_ — source lines 7858–7866

Vector A.4: source lines 7856–7884. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> Here is a Transferable Secret Key consisting of:
>
> *  A version 6 Ed25519 Secret Key packet
>
> *  A version 6 Direct Key self-signature
>
> *  A version 6 X25519 Secret Subkey packet
>
> *  A version 6 Subkey Binding signature

### Appendix A.5 Sample Locked Version 6 Secret Key (Transferable Secret Key)

**N-580** (Appendix A.5) _[test vector]_ — source lines 7888–7893

Vector A.5: source lines 7886–7910. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> Here is the same secret key as in Appendix A.4, but the secret key
> material is locked with a passphrase using AEAD and Argon2.
>
> The passphrase is the ASCII string:
>
> correct horse battery staple

### Appendix A.5.1 Intermediate Data for Locked Primary Key

**N-581** (Appendix A.5.1) _[test vector]_ — source line 7914

Vector A.5.1: source lines 7912–7926. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> The S2K-derived material for the primary key is:

### Appendix A.5.2 Intermediate Data for Locked Subkey

**N-582** (Appendix A.5.2) _[test vector]_ — source line 7930

Vector A.5.2: source lines 7928–7942. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> The S2K-derived key material for the subkey is:

### Appendix A.6 Sample Cleartext Signed Message

**N-583** (Appendix A.6) _[test vector]_ — source lines 7946–7951

Vector A.6: source lines 7944–8074. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> Here is a signed message that uses the Cleartext Signature Framework
> (Section 7).  It can be verified with the certificate from
> Appendix A.3.
>
> Note that this message makes use of dash-escaping (Section 7.2) due
> to its contents.

### Appendix A.7 Sample Inline-Signed Message

**N-584** (Appendix A.7) _[test vector]_ — source lines 8078–8080

Vector A.7: source lines 8076–8091. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This is the same message and signature as in Appendix A.6 but as an
> inline-signed message.  The hashed data is exactly the same, and all
> intermediate values and annotated hex dumps are also applicable.

### Appendix A.8 Sample X25519-AEAD-OCB Encryption and Decryption

**N-585** (Appendix A.8) _[test vector]_ — source lines 8095–8097

Vector A.8: source lines 8093–8097. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This example encrypts the cleartext string Hello, world! for the
> sample cert (see Appendix A.3), using AES-128 with AEAD-OCB
> encryption.

### Appendix A.8.1 Sample Version 6 Public Key Encrypted Session Key Packet

**N-586** (Appendix A.8.1) _[test vector]_ — source line 8101

Vector A.8.1: source lines 8099–8138. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This packet contains the following series of octets:

### Appendix A.8.2 X25519 Encryption/Decryption of the Session Key

**N-587** (Appendix A.8.2) _[test vector]_ — source lines 8147–8148

Vector A.8.2: source lines 8140–8175. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This ephemeral key is derived from the following ephemeral secret key
> material, which is never placed on the wire:

### Appendix A.8.3 Sample v2 SEIPD Packet

**N-588** (Appendix A.8.3) _[test vector]_ — source line 8179

Vector A.8.3: source lines 8177–8220. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This packet contains the following series of octets:

### Appendix A.8.4 Decryption of Data

**N-589** (Appendix A.8.4) _[test vector]_ — source line 8224

Vector A.8.4: source lines 8222–8279. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> Starting AEAD-OCB decryption of data, using the session key.

### Appendix A.8.5 Complete X25519-AEAD-OCB Encrypted Packet Sequence

**N-590** (Appendix A.8.5) _[test vector]_ — source line 8281

Vector A.8.5: source lines 8281–8290. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. No descriptive prose; heading quoted:

```
A.8.5.  Complete X25519-AEAD-OCB Encrypted Packet Sequence
```

### Appendix A.9 Sample AEAD-EAX Encryption and Decryption

**N-591** (Appendix A.9) _[test vector]_ — source lines 8294–8295

Vector A.9: source lines 8292–8295. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This example encrypts the cleartext string Hello, world! with the
> passphrase password, using AES-128 with AEAD-EAX encryption.

### Appendix A.9.1 Sample Version 6 Symmetric Key Encrypted Session Key Packet

**N-592** (Appendix A.9.1) _[test vector]_ — source line 8299

Vector A.9.1: source lines 8297–8333. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This packet contains the following series of octets:

### Appendix A.9.2 Starting AEAD-EAX Decryption of the Session Key

**N-593** (Appendix A.9.2) _[test vector]_ — source line 8335

Vector A.9.2: source lines 8335–8359. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. No descriptive prose; heading quoted:

```
A.9.2.  Starting AEAD-EAX Decryption of the Session Key
```

### Appendix A.9.3 Sample v2 SEIPD Packet

**N-594** (Appendix A.9.3) _[test vector]_ — source line 8363

Vector A.9.3: source lines 8361–8404. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This packet contains the following series of octets:

### Appendix A.9.4 Decryption of Data

**N-595** (Appendix A.9.4) _[test vector]_ — source line 8408

Vector A.9.4: source lines 8406–8456. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> Starting AEAD-EAX decryption of data, using the session key.

### Appendix A.9.5 Complete AEAD-EAX Encrypted Packet Sequence

**N-596** (Appendix A.9.5) _[test vector]_ — source line 8458

Vector A.9.5: source lines 8458–8466. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. No descriptive prose; heading quoted:

```
A.9.5.  Complete AEAD-EAX Encrypted Packet Sequence
```

### Appendix A.10 Sample AEAD-OCB Encryption and Decryption

**N-597** (Appendix A.10) _[test vector]_ — source lines 8470–8471

Vector A.10: source lines 8468–8471. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This example encrypts the cleartext string Hello, world! with the
> passphrase password, using AES-128 with AEAD-OCB encryption.

### Appendix A.10.1 Sample Version 6 Symmetric Key Encrypted Session Key Packet

**N-598** (Appendix A.10.1) _[test vector]_ — source line 8475

Vector A.10.1: source lines 8473–8509. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This packet contains the following series of octets:

### Appendix A.10.2 Starting AEAD-OCB Decryption of the Session Key

**N-599** (Appendix A.10.2) _[test vector]_ — source line 8511

Vector A.10.2: source lines 8511–8535. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. No descriptive prose; heading quoted:

```
A.10.2.  Starting AEAD-OCB Decryption of the Session Key
```

### Appendix A.10.3 Sample v2 SEIPD Packet

**N-600** (Appendix A.10.3) _[test vector]_ — source line 8539

Vector A.10.3: source lines 8537–8580. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This packet contains the following series of octets:

### Appendix A.10.4 Decryption of Data

**N-601** (Appendix A.10.4) _[test vector]_ — source line 8584

Vector A.10.4: source lines 8582–8632. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> Starting AEAD-OCB decryption of data, using the session key.

### Appendix A.10.5 Complete AEAD-OCB Encrypted Packet Sequence

**N-602** (Appendix A.10.5) _[test vector]_ — source line 8634

Vector A.10.5: source lines 8634–8642. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. No descriptive prose; heading quoted:

```
A.10.5.  Complete AEAD-OCB Encrypted Packet Sequence
```

### Appendix A.11 Sample AEAD-GCM Encryption and Decryption

**N-603** (Appendix A.11) _[test vector]_ — source lines 8646–8647

Vector A.11: source lines 8644–8647. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This example encrypts the cleartext string Hello, world! with the
> passphrase password, using AES-128 with AEAD-GCM encryption.

### Appendix A.11.1 Sample Version 6 Symmetric Key Encrypted Session Key Packet

**N-604** (Appendix A.11.1) _[test vector]_ — source line 8651

Vector A.11.1: source lines 8649–8683. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This packet contains the following series of octets:

### Appendix A.11.2 Starting AEAD-GCM Decryption of the Session Key

**N-605** (Appendix A.11.2) _[test vector]_ — source line 8685

Vector A.11.2: source lines 8685–8709. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. No descriptive prose; heading quoted:

```
A.11.2.  Starting AEAD-GCM Decryption of the Session Key
```

### Appendix A.11.3 Sample v2 SEIPD Packet

**N-606** (Appendix A.11.3) _[test vector]_ — source line 8713

Vector A.11.3: source lines 8711–8754. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> This packet contains the following series of octets, is:

### Appendix A.11.4 Decryption of Data

**N-607** (Appendix A.11.4) _[test vector]_ — source line 8758

Vector A.11.4: source lines 8756–8806. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> Starting AEAD-GCM decryption of data, using the session key.

### Appendix A.11.5 Complete AEAD-GCM Encrypted Packet Sequence

**N-608** (Appendix A.11.5) _[test vector]_ — source line 8808

Vector A.11.5: source lines 8808–8816. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. No descriptive prose; heading quoted:

```
A.11.5.  Complete AEAD-GCM Encrypted Packet Sequence
```

### Appendix A.12 Sample Messages Encrypted Using Argon2

**N-609** (Appendix A.12) _[test vector]_ — source lines 8820–8824

Vector A.12: source lines 8818–8824. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. Description quoted:

> These messages are the literal data Hello, world! encrypted using v1
> SEIPD, with Argon2 and the passphrase "password", using different
> session key sizes.  In each example, the choice of symmetric cipher
> is the same in both the v4 SKESK packet and v1 SEIPD packet.  In all
> cases, the Argon2 parameters are t = 1, p = 4, and m = 21.

### Appendix A.12.1 V4 SKESK Using Argon2 with AES-128

**N-610** (Appendix A.12.1) _[test vector]_ — source line 8826

Vector A.12.1: source lines 8826–8835. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. No descriptive prose; heading quoted:

```
A.12.1.  V4 SKESK Using Argon2 with AES-128
```

### Appendix A.12.2 V4 SKESK Using Argon2 with AES-192

**N-611** (Appendix A.12.2) _[test vector]_ — source line 8837

Vector A.12.2: source lines 8837–8847. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. No descriptive prose; heading quoted:

```
A.12.2.  V4 SKESK Using Argon2 with AES-192
```

### Appendix A.12.3 V4 SKESK Using Argon2 with AES-256

**N-612** (Appendix A.12.3) _[test vector]_ — source line 8849

Vector A.12.3: source lines 8849–8859. The vector's values and packet bytes are not reproduced here; they belong in `examples/`. No descriptive prose; heading quoted:

```
A.12.3.  V4 SKESK Using Argon2 with AES-256
```

## Appendix B Upgrade Guidance (Adapting Implementations from RFCs 4880 and 6637)

**N-613** (Appendix B) _[non-normative]_ — source lines 8864–8869

> This subsection offers a concise, non-normative summary of the
> substantial additions to and departures from [RFC4880] and [RFC6637].
> It is intended to help implementers who are augmenting an existing
> implementation from those specifications to comply with this
> specification.  Cryptographic algorithms marked with "MTI" are
> mandatory to implement.

**N-614** (Appendix B) _[non-normative]_ — source lines 8871–9017

```
   *  Public Key Signing Algorithms:

      -  Ed25519 (Sections 5.5.5.9 and 5.2.3.4) -- MTI

      -  Ed448 (Sections 5.5.5.10 and 5.2.3.5)

      -  EdDSALegacy with Ed25519Legacy (Sections 5.5.5.5 and 5.2.3.3)

      -  ECDSA with Brainpool curves (Section 9.2)

   *  Public Key Encryption Algorithms:

      -  X25519 (Sections 5.5.5.7 and 5.1.6) -- MTI

      -  X448 (Sections 5.5.5.8 and 5.1.7)

      -  ECDH with Curve25519Legacy (Section 9.2)

      -  ECDH with Brainpool curves (Section 9.2)

   *  AEAD Encryption:

      -  V2 SEIPD (Section 5.13.2)

      -  AEAD modes:

         o  OCB mode (Section 5.13.4) -- MTI

         o  EAX mode (Section 5.13.3)

         o  GCM mode (Section 5.13.5)

      -  V6 PKESK (Section 5.1.2)

      -  V6 SKESK (Section 5.3.2)

      -  Features signature subpacket: add flag for v2 SEIPD
         (Section 5.2.3.32)

      -  Signature Subpacket: Preferred AEAD Ciphersuites
         (Section 5.2.3.15)

      -  Secret key encryption: AEAD "S2K usage octet" (Sections 3.7.2
         and 5.5.3)

   *  Version 6 Keys and Signatures:

      -  Version 6 Public Keys (Section 5.5.2.3)

      -  Version 6 Fingerprint and Key ID (Section 5.5.4.3)

      -  Version 6 Secret Keys (Section 5.5.3)

      -  Version 6 Signatures (Section 5.2.3)

      -  Version 6 One-Pass Signatures (Section 5.4)

   *  Certificate (Transferable Public Key) Structure:

      -  Preferences subpackets in Direct Key signatures
         (Section 5.2.3.10)

      -  Self-verifying revocation certificate (Section 10.1.2)

      -  User ID is explicitly optional (Section 10.1.1)

   *  S2K: Argon2 (Section 3.7.1.4)

   *  Subpacket: Intended Recipient Fingerprint (Section 5.2.3.36)

   *  Digest Algorithms: SHA3-256 and SHA3-512 (Section 9.5)

   *  Packet: Padding (Section 5.14)

   *  Message Structure: Packet Criticality (Section 4.3)

   *  Deprecations:

      -  Public Key Algorithms:

         o  Avoid RSA weak keys (Section 12.4)

         o  Avoid DSA (Section 12.5)

         o  Avoid ElGamal (Sections 12.6 and 5.1.4)

         o  For Version 6 Keys: Avoid EdDSA25519Legacy and
            Curve25519Legacy (Section 9.2)

      -  Digest Algorithms:

         o  Avoid MD5, SHA1, and RIPEMD160 (Section 9.5)

      -  Symmetric Key Algorithms:

         o  Avoid IDEA, TripleDES, and CAST5 (Section 9.3)

      -  S2K Specifier:

         o  Avoid Simple S2K (Section 3.7.1.1)

      -  Secret Key Protections (a.k.a. S2K Usage):

         o  Avoid MalleableCFB (Section 3.7.2.1)

      -  Packet Types:

         o  Avoid Symmetrically Encrypted Data (Sections 5.7 and 13.7)

      -  Literal Data Packet Metadata:

         o  Avoid Filename and Date fields (Section 5.9)

         o  Avoid Special _CONSOLE "filename" (Section 5.9.1)

      -  Packet Versions:

         o  Avoid Version 3 Public Keys (Section 5.5.2.1)

         o  Avoid Version 3 Signatures (Section 5.2)

      -  Signature Types:

         o  Avoid Reserved Signature Type ID 0xFF (Sections 5.2.1.16 and
            5.2.4.1)

      -  Signature Subpackets:

         o  For Version 6 Signatures: Avoid Issuer Key ID
            (Section 5.2.3.12)

         o  Avoid Revocation Key (Section 5.2.3.23)

      -  ASCII Armor:

         o  Ignore; do not emit CRC (Section 6.1)

         o  Do not emit "Version" Armor Header (Section 6.2.2.1)

      -  Cleartext Signature Framework:

         o  Ignore; avoid emitting unnecessary Hash: headers
            (Section 6.2.2.3)

         o  Reject Cleartext Signature Framework signatures with invalid
            Hash: headers (Section 6.2.2.3) or any other Armor Header
            (Section 7.1)
```

### Appendix B.1 Terminology Changes

_Source lines 9021–9022 introduce the list; omitted._

**N-615** (Appendix B.1) _[lowercase/implied]_ — source lines 9024–9051

```
   In previous versions, the following terms were used:

   *  "Radix-64" was used to refer to OpenPGP's ASCII Armor base64
      encoding (Section 6).

   *  "Old packet format" was used to refer to the Legacy packet format
      (Section 4.2.2) predating [RFC2440].

   *  "New packet format" was used to refer to the OpenPGP packet format
      (Section 4.2.1) introduced in [RFC2440].

   *  "Certificate" was used ambiguously to mean multiple things.  In
      this document, it means "Transferable Public Key" exclusively.

   *  "Preferred Symmetric Algorithms" was the old name for the
      "Preferred Symmetric Ciphers for v1 SEIPD" subpacket
      (Section 5.2.3.14).

   *  "Modification Detection Code" or "MDC" was originally described as
      a distinct packet (Packet Type ID 19), and its corresponding flag
      in the Features signature subpacket (Section 5.2.3.32) was known
      as "Modification Detection".  It is now described as an intrinsic
      part of v1 SEIPD (Section 5.13.1), and the same corresponding flag
      is known as "Version 1 Symmetrically Encrypted and Integrity
      Protected Data packet".

   *  "Packet Tag" was used to refer to the Packet Type ID (Section 5)
      or sometimes to the encoded Packet Type ID (Section 4.2).
```

## Appendix C Errata Addressed by This Document

**N-616** (Appendix C) _[non-normative]_ — source lines 9055–9101

The errata titles at source lines 9072 and 9074 contain the words MUST, MAY and SHOULD as names of the errata's subject; they are not BCP 14 usage.

```
   The following verified errata have been incorporated or are otherwise
   resolved by this document:

   *  [Errata-2199] - S2K hash/cipher octet correction

   *  [Errata-2200] - No implicit use of IDEA correction

   *  [Errata-2206] - PKESK acronym expansion

   *  [Errata-2208] - Signature key owner clarification

   *  [Errata-2214] - Signature hashing clarification

   *  [Errata-2216] - Self-signature applies to user ID correction

   *  [Errata-2219] - Session key encryption storage clarification

   *  [Errata-2222] - Simple hash MUST/MAY clarification

   *  [Errata-2226] - Native line endings SHOULD clarification

   *  [Errata-2234] - Radix-64/base64 clarification

   *  [Errata-2235] - ASCII/UTF-8 collation sequence clarification

   *  [Errata-2236] - Packet Composition is a sequence clarification

   *  [Errata-2238] - Subkey packets come after all User ID packets
      clarification

   *  [Errata-2240] - Subkey removal clarification

   *  [Errata-2242] - mL/emLen variable correction

   *  [Errata-2243] - CFB mode initialization vector (IV) clarification

   *  [Errata-2270] - SHA-224 octet sequence correction

   *  [Errata-2271] - Radix-64 correction

   *  [Errata-3298] - Key Revocation signatures correction

   *  [Errata-5491] - C code fix for CRC24_POLY define

   *  [Errata-7545] - Armor Header colon hex fix

   *  [Errata-7889] - Signature/certification correction
```

_Acknowledgements (source lines 9103–9117) and Authors' Addresses (9119–9138) carry no normative content; no entry._
