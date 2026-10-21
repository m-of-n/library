---
record: rfc-9054
kind: normative
title: "rfc-9054 — normative statements"
extracted: "2026-10-20"
reviewed_by: ""
---

# RFC 9054 — normative text, verbatim

**What this file is.** Every normative statement of RFC 9054, reproduced as an
exact run of source lines with its line range and its own `sha256`, in the
document's own section order. Nothing here is paraphrased and nothing is
retyped: each fenced block was lifted from `.cache/rfc-9054.txt` by line range
by script.

| | |
|---|---|
| **Source** | `.cache/rfc-9054.txt`, 499 newline-delimited lines |
| **Digest** | `75a6bf62b4226baa1e14ccdcc4c603b8a039084ad79677db029e0bbec4525e6f` |
| **Category** | **Informational** — "This document is not an Internet Standards Track specification" (line 25) |
| **BCP 14 keywords** | **2** — 1 SHOULD NOT, 1 SHOULD, both in §2 and both about collision attacks |
| **Digest values printed** | **none** — no hex, no base64, no worked example anywhere |

**Region convention.** Each digest is the sha256 of the region's lines joined
by `\n` with no trailing newline.

**There is no page decoration in this source and no region is split.** This
rendering has **0 form feeds** and no running headers or footers in its 499
lines, checked with the same patterns that match 25 page breaks in RFC 8392.
Built with `split("\n")`, never `splitlines()`.

**What the shape of this document is.** Two BCP 14 keywords, eight registry
rows, one new value in a registry column, two CDDL fragments the document
itself calls examples, and no carrier. Its six force-bearing sentences outside
those two keywords are all lower case; `requirements.yaml`'s reconciliation
names every one.

---

## §1 — Introduction

**The two absences, and the sentence this record exists for.** COSE defines no
direct method for using hash algorithms *and* no digested-object structure
"along the lines of the DigestedData ASN.1 structure in [CMS]" — and "This
omission was intentional". `R-O-03` can cite the algorithm from here and has
nothing to cite for the carrier. Note also which two reasons the document
gives for leaving the structure to the application: additional data, and
methods of obtaining the data — exactly fields 3 and 4 of §2.1's four.

```
   The CBOR Object Signing and Encryption (COSE) syntax [RFC9052] does
   not define any direct methods for the use of hash algorithms.  It
   also does not define a structure syntax that is used to encode a
   digested object structure along the lines of the DigestedData ASN.1
   structure in [CMS].  This omission was intentional, as a structure
   consisting of just a digest identifier, the content, and a digest
   value does not, by itself, provide any strong security service.
   Additionally, an application is going to be better off defining this
   type of structure so that it can include any additional data that
   needs to be hashed, as well as methods of obtaining the data.
```

*Source `.cache/rfc-9054.txt` lines 74-83 · `sha256:7db4fec5cd09626f311b5187b137c1f0eb7c6c4783c4dd84cb4e7eea4e63f1c6`*


The stated justification for registering identifiers at all.

```
   While the above is true, there are some cases where having some
   standard hash algorithms defined for COSE with a common identifier
   makes a great deal of sense.  Two of the cases where these are going
   to be used are:

   *  Indirect signing of content, and

   *  Object identification.
```

*Source `.cache/rfc-9054.txt` lines 85-92 · `sha256:3c7bf904a4bddd595866e7a740789380a0a92d4262bfa2836472465d692afa21`*


**Declared use 1 of 2 — indirect signing.** Note what is signed: the hash
value *and* an identifier for the hash algorithm. The algorithm is in-band and
inside the signed bytes, which is the shape `R-O-05`'s type-indicator clause
wants.

```
   Indirect signing of content is a paradigm where the content is not
   directly signed, but instead a hash of the content is computed, and
   that hash value -- along with an identifier for the hash algorithm --
   is included in the content that will be signed.  Indirect signing
   allows for a signature to be validated without first downloading all
   of the content associated with the signature.  Rather, the signature
   can be validated on all of the hash values and pointers to the
   associated contents; those associated parts can then be downloaded,
   then the hash value of that part can be computed and compared to the
   hash value in the signed content.  This capability can be of even
   greater importance in a constrained environment, as not all of the
   content signed may be needed by the device.  An example of how this
   is used can be found in Section 5.4 of [SUIT-MANIFEST].
```

*Source `.cache/rfc-9054.txt` lines 94-106 · `sha256:83adc8dbcb7fc78283c2f977247cceb815e5d57413fb066ae96837f43e78fd76`*


**Declared use 2 of 2 — object identification**, and the cross-record join.
`[COSE-x509]` is `draft-ietf-cose-x509-08`, 14 December 2020, which became
**RFC 9360**. The dependency runs backwards in time: this document cites
RFC 9360's draft, and RFC 9360 as published cites RFC 9054 zero times.

```
   The use of hashes to identify objects is something that has been very
   common.  One of the primary things that has been identified by a hash
   function in a secure message is a certificate.  Two examples of this
   can be found in [ESS] and the COSE equivalents in [COSE-x509].
```

*Source `.cache/rfc-9054.txt` lines 108-111 · `sha256:c8ecac0bf47a8950c2f573b6414268f69274ef6b68ab7caf44c6c6887628c7e8`*


## §1.1 — Requirements Terminology

Quoted here and **deliberately never quoted in `requirements.yaml`**: it
recites all eleven keywords and constrains nothing, and `bin/validate`
recounts the requirement texts with boilerplate stripping **off**. Nine of
the eleven words it recites are never used again in the document; only
`SHOULD` and `SHOULD NOT` appear, once each.

```
   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in BCP
   14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.
```

*Source `.cache/rfc-9054.txt` lines 115-119 · `sha256:2262576bb7a8ae928b9fe0d2aae26958f4ce7e7d74ffdb75248c8e92fffa6051`*


## §2 — Hash Algorithm Usage

Which purposes need a cryptographically strong hash, and which do not.

```
   As noted in the previous section, hash functions can be used for a
   variety of purposes.  Some of these purposes require that a hash
   function be cryptographically strong.  These include direct and
   indirect signatures -- that is, using the hash as part of the
   signature or using the hash as part of the body to be signed.  Other
   uses of hash functions may not require the same level of strength.
```

*Source `.cache/rfc-9054.txt` lines 123-128 · `sha256:0b2d82cd367ed99b7d6a8a86e511d83f2d75aaea295cb9dea898e788624b87df`*


**The document says of itself that it contains hash functions not designed
for cryptographic use** — two of the eight, SHA-1 (−14) and SHA-256/64 (−15).
The agility advice in the second half is **lower case** and is the document's
whole position on agility.

```
   This document contains some hash functions that are not designed to
   be used for cryptographic operations.  An application that is using a
   hash function needs to carefully evaluate exactly what hash
   properties are needed and which hash functions are going to provide
   them.  Applications should also make sure that the ability to change
   hash functions is part of the base design, as cryptographic advances
   are sure to reduce the strength of any given hash function [BCP201].
```

*Source `.cache/rfc-9054.txt` lines 130-136 · `sha256:6f5e0e91e50a2e38f421624d7c41beb7a665a5666d90567eb534ea719f255d7c`*


**Both of the document's BCP 14 keywords are in this paragraph**, at lines 146
and 148. Neither is decidable by an implementation: "practical" is never
defined, and the SHOULD is conditioned on alternatives being available *and*
migration being viable, with "protocol maintainers and users" as its actor.
The escape hatch in the second half — "absolutely no other choice (e.g., a
Hardware Security Module (HSM) that cannot be replaced)" — is a deployment
excuse promoted to a specification clause.

```
   A hash function is a map from one, normally large, bit string to a
   second, usually smaller, bit string.  As the number of possible input
   values is far greater than the number of possible output values, it
   is inevitable that there are going to be collisions.  The trick is to
   make sure that it is difficult to find two values that are going to
   map to the same output value.  A "Collision Attack" is one where an
   attacker can find two different messages that have the same hash
   value.  A hash function that is susceptible to practical collision
   attacks SHOULD NOT be used for a cryptographic purpose.  The
   discovery of theoretical collision attacks against a given hash
   function SHOULD trigger protocol maintainers and users to review the
   continued suitability of the algorithm if alternatives are available
   and migration is viable.  The only reason such a hash function is
   used is when there is absolutely no other choice (e.g., a Hardware
   Security Module (HSM) that cannot be replaced), and only after
   looking at the possible security issues.  Cryptographic purposes
   would include the creation of signatures or the use of hashes for
   indirect signatures.  These functions may still be usable for
   noncryptographic purposes.
```

*Source `.cache/rfc-9054.txt` lines 138-156 · `sha256:840c462066d2ef94ab18e24cbaf27205dffc1ef7b30b5ea1753263c1479958f4`*


**The filtering case, and the precondition that makes it safe.** This is the
paragraph `rfc-9360` §5's last sentence needs and does not honour: a
fingerprint used "to verify that it is the correct certificate" is *by this
document's own words* a cryptographic use subject to the collision warning,
while a fingerprint used "to sort through a collection of certificates" is
safe **only because** "one still needs to confirm that the public key
validates the signature (and that the certificate is trusted)".

```
   An example of a noncryptographic use of a hash is filtering from a
   collection of values to find a set of possible candidates; the
   candidates can then be checked to see if they can successfully be
   used.  A simple example of this is the classic fingerprint of a
   certificate.  If the fingerprint is used to verify that it is the
   correct certificate, then that usage is a cryptographic one and is
   subject to the warning above about collision attack.  If, however,
   the fingerprint is used to sort through a collection of certificates
   to find those that might be used for the purpose of verifying a
   signature, a simple filter capability is sufficient.  In this case,
   one still needs to confirm that the public key validates the
   signature (and that the certificate is trusted), and all certificates
   that don't contain a key that validates the signature can be
   discarded as false positives.
```

*Source `.cache/rfc-9054.txt` lines 158-171 · `sha256:0bd37f42e3c244b42a31e38e8b5e08ddac704d8c7cfa2183ab3d77b0f7c5d215`*


**Definition 1 of 2 of "Filter Only"**, and the force word is the lower-case
"should". Compare §4.1's definition below: the two sentences defining the same
registry value are not the same sentence.

```
   To distinguish between these two cases, a new value in the
   Recommended column of the "COSE Algorithms" registry has been added.
   "Filter Only" indicates that the only purpose of a hash function
   should be to filter results; it is not intended for applications that
   require a cryptographically strong algorithm.
```

*Source `.cache/rfc-9054.txt` lines 173-177 · `sha256:be80efa88d48c52cf202b0ca86fdafff7d105b0e6179a7c0f7ea20c3c0104ace`*


## §2.1 — Example CBOR Hash Structure

**The four fields, and the one piece of canonicalization advice in the
document.** "it is strongly suggested that either it be a fixed known size,
or the lengths of the pieces being hashed be included so that the resulting
byte string has a unique interpretation as the additional data. (Encoding as a
CBOR array accomplishes this requirement.)" — that is a `canonical-encoding`
condition (1) argument, made in a parenthetical, with no keyword.

```
   [COSE] did not provide a default structure for holding a hash value
   both because no separate hash algorithms were defined and because the
   way the structure is set up is frequently application specific.
   There are four fields that are often included as part of a hash
   structure:

   *  The hash algorithm identifier.

   *  The hash value.

   *  A pointer to the value that was hashed.  This could be a pointer
      to a file, an object that can be obtained from the network, a
      pointer to someplace in the message, or something very application
      specific.

   *  Additional data.  This can be something as simple as a random
      value (i.e., salt) to make finding hash collisions slightly harder
      (because the payload handed to the application could have been
      selected to have a collision), or as complicated as a set of
      processing instructions that is used with the object that is
      pointed to.  The additional data can be dealt with in a number of
      ways, prepending or appending to the content, but it is strongly
      suggested that either it be a fixed known size, or the lengths of
      the pieces being hashed be included so that the resulting byte
      string has a unique interpretation as the additional data.
      (Encoding as a CBOR array accomplishes this requirement.)
```

*Source `.cache/rfc-9054.txt` lines 181-206 · `sha256:4836c6769c24c6561f1776617fd4b938bfb704bc367b45c3b81858640578afc1`*


### §2.1 — `COSE_Hash_V`, as printed

**Declared an example, and it carries erratum 7335** (*Reported*, Technical,
§2.1, Carsten Bormann, 2023-02-06): the comment marker is `#`, where CDDL's
is `;`. Checked mechanically against RFC 8610 Appendix B's grammar for this
pass — **it does parse**, as a group of 24 entries rather than 4, with 16 bare
type references harvested from the comment words. `schema/README.md` carries
the measurement. Even with the erratum applied it is a **group**, not a type,
so under RFC 8610 §2.2.4 it cannot be the root of a model and needs a `{ }`
the document never supplies.

```
   An example of a structure that permits all of the above fields to
   exist would look like the following:

   COSE_Hash_V = (
       1 : int / tstr, # Algorithm identifier
       2 : bstr, # Hash value
       ? 3 : tstr, # Location of object that was hashed
       ? 4 : any   # object containing other details and things
       )
```

*Source `.cache/rfc-9054.txt` lines 208-216 · `sha256:8a03b0a20f9c0a16ad3ab9d41be352f0965ba6a61d55fb9ae0eebeae30976c3c`*


### §2.1 — `COSE_Hash_Find`, as printed

**Parses as printed**, as a type rule with two entries. Field for field this
is `rfc-9360`'s `COSE_CertHash` with the same member-key names and
`int / tstr` unparenthesised — the same working group arriving at the same
two-field shape twice, in two documents, with no cross-reference between the
two structures.

```
   Below is an alternative structure that could be used in situations
   where one is searching a group of objects for a matching hash value.
   In this case, the location would not be needed, and adding extra data
   to the hash would be counterproductive.  This results in a structure
   that looks like this:

   COSE_Hash_Find = [
       hashAlg : int / tstr,
       hashValue : bstr
   ]
```

*Source `.cache/rfc-9054.txt` lines 218-227 · `sha256:8c337b30630446be8bc918344174922c893ad4214576f1c636b81ce45d448694`*


## §3.1 — SHA-1 Hash Algorithm

The registration of a broken hash, with the two situations that justify it:
unreplaceable HSMs, and filtering — "thus, the collision-resistance property
is not needed". The strongest thing said about SHA-1 is the lower-case "the
fact that it should no longer be used".

```
   The SHA-1 hash algorithm [RFC3174] was designed by the United States
   National Security Agency and published in 1995.  Since that time, a
   large amount of cryptographic analysis has been applied to this
   algorithm, and a successful collision attack has been created
   [SHA-1-collision].  The IETF formally started discouraging the use of
   SHA-1 in [RFC6194].

   Despite these facts, there are still times where SHA-1 needs to be
   used; therefore, it makes sense to assign a code point for the use of
   this hash algorithm.  Some of these situations involve historic HSMs
   where only SHA-1 is implemented; in other situations, the SHA-1 value
   is used for the purpose of filtering; thus, the collision-resistance
   property is not needed.

   Because of the known issues for SHA-1 and the fact that it should no
   longer be used, the algorithm will be registered with the
   recommendation of "Filter Only".  This provides guidance about when
   the algorithm is safe for use, while discouraging usage where it is
   not safe.

   The COSE capabilities for this algorithm is an empty array.
```

*Source `.cache/rfc-9054.txt` lines 233-253 · `sha256:2880e9008e5997555cf6e0ef87431c970722766b03c1376367a34fa19e326518`*


**Table 1.** `-14` encodes as the **single** CBOR octet `0x2d` (RFC 8949 §3),
which is the measurement §4.1's rationale fails against.

```
   +=====+======+=============+==============+===========+=============+
   |Name |Value | Description | Capabilities | Reference | Recommended |
   +=====+======+=============+==============+===========+=============+
   |SHA-1|-14   | SHA-1 Hash  | []           | RFC 9054  | Filter Only |
   +-----+------+-------------+--------------+-----------+-------------+

                       Table 1: SHA-1 Hash Algorithm
```

*Source `.cache/rfc-9054.txt` lines 255-261 · `sha256:8dcf77cb1a348e2a084e9d1ebafb6021f1eba53f861282348fdc87371e843155`*


## §3.2 — SHA-2 Hash Algorithms

```
   The family of SHA-2 hash algorithms [FIPS-180-4] was designed by the
   United States National Security Agency and published in 2001.  Since
   that time, some additional algorithms have been added to the original
   set to deal with length-extension attacks and some performance
   issues.  While the SHA-3 hash algorithms have been published since
   that time, the SHA-2 algorithms are still broadly used.

   There are a number of different parameters for the SHA-2 hash
   functions.  The set of hash functions that has been chosen for
   inclusion in this document is based on those different parameters and
   some of the trade-offs involved.
```

*Source `.cache/rfc-9054.txt` lines 265-275 · `sha256:94acb31f9c90b546fc9b477b9ed6fded185e8132bd81eb93f2d652b7f182ec11`*


**SHA-256/64, and the justification that cites `rfc-9360`'s draft.** The
condition on its use — "it must be limited to where the purpose of the hash is
noncryptographic" — is a **lower-case** must. The safety argument in the
second half is that a false positive is caught by testing the public key,
which is not what `rfc-9360` §2's protected `x5t` does.

```
   *  *SHA-256/64* provides a truncated hash.  The length of the
      truncation is designed to allow for smaller transmission size.
      The trade-off is that the odds that a collision will occur
      increase proportionally.  Use of this hash function requires
      analysis of the potential problems that could result from a
      collision, or it must be limited to where the purpose of the hash
      is noncryptographic.

      The latter is the case for some of the scenarios identified in
      [COSE-x509], specifically, for the cases when the hash value is
      used to select among possible certificates: if there are multiple
      choices remaining, then each choice can be tested by using the
      public key.
```

*Source `.cache/rfc-9054.txt` lines 277-289 · `sha256:081a322141a38b1d17fa0cc11e539521f8571525a4a07ce18009033d6a5e338a`*


The other four SHA-2 selections.

```
   *  *SHA-256* is probably the most common hash function used
      currently.  SHA-256 is an efficient hash algorithm for 32-bit
      hardware.

   *  *SHA-384* and *SHA-512* hash functions are efficient for 64-bit
      hardware.

   *  *SHA-512/256* provides a hash function that runs more efficiently
      on 64-bit hardware but offers the same security level as SHA-256.
```

*Source `.cache/rfc-9054.txt` lines 291-299 · `sha256:0193514d25db5ed7faa9fa1b3aa5c07af210963844c5426cc4a529b34ffd3e10`*


**The NOTE is the whole of SHA-256/64's definition**, and it does not say
which 64 bits. Both candidate truncations are computed in
`examples/vectors.yaml` and they differ. It does separate SHA-256/64 from
SHA-512/256, which is a different construction rather than a truncation —
also measured.

```
      |  NOTE: SHA-256/64 is a simple truncation of SHA-256 to 64 bits
      |  defined in this specification.  SHA-512/256 is a modified
      |  variant of SHA-512 truncated to 256 bits, as defined in
      |  [FIPS-180-4].

   The COSE capabilities array for these algorithms is empty.
```

*Source `.cache/rfc-9054.txt` lines 301-306 · `sha256:75312cf860819975c144cefdddd4cab66044747e627ec9486004d6c541c0f1ef`*


**Table 2.**

```
   +===========+=====+===========+==============+=========+============+
   |Name       |Value|Description| Capabilities |Reference|Recommended |
   +===========+=====+===========+==============+=========+============+
   |SHA-256/64 |-15  |SHA-2      | []           |RFC 9054 |Filter Only |
   |           |     |256-bit    |              |         |            |
   |           |     |Hash       |              |         |            |
   |           |     |truncated  |              |         |            |
   |           |     |to 64-bits |              |         |            |
   +-----------+-----+-----------+--------------+---------+------------+
   |SHA-256    |-16  |SHA-2      | []           |RFC 9054 |Yes         |
   |           |     |256-bit    |              |         |            |
   |           |     |Hash       |              |         |            |
   +-----------+-----+-----------+--------------+---------+------------+
   |SHA-384    |-43  |SHA-2      | []           |RFC 9054 |Yes         |
   |           |     |384-bit    |              |         |            |
   |           |     |Hash       |              |         |            |
   +-----------+-----+-----------+--------------+---------+------------+
   |SHA-512    |-44  |SHA-2      | []           |RFC 9054 |Yes         |
   |           |     |512-bit    |              |         |            |
   |           |     |Hash       |              |         |            |
   +-----------+-----+-----------+--------------+---------+------------+
   |SHA-512/256|-17  |SHA-2      | []           |RFC 9054 |Yes         |
   |           |     |512-bit    |              |         |            |
   |           |     |Hash       |              |         |            |
   |           |     |truncated  |              |         |            |
   |           |     |to 256-bits|              |         |            |
   +-----------+-----+-----------+--------------+---------+------------+

                       Table 2: SHA-2 Hash Algorithms
```

*Source `.cache/rfc-9054.txt` lines 308-336 · `sha256:53ddc35343e55adce421d02327d0eff4c0c13f74c9699cdae7940bad11a5956a`*


## §3.3 — SHAKE Algorithms

**The document declines for SHAKE exactly what it does for SHA-2 at −15**, and
gives no reason. Note the consequence: a SHAKE identifier carries its output
length, while −15 carries a truncation the document does not locate.

```
   The family of SHA-3 hash algorithms [FIPS-202] was the result of a
   competition run by NIST.  The pair of algorithms known as SHAKE-128
   and SHAKE-256 are the instances of SHA-3 that are currently being
   standardized in the IETF.  This is the reason for including these
   algorithms in this document.

   The SHA-3 hash algorithms have a significantly different structure
   than the SHA-2 hash algorithms.

   Unlike the SHA-2 hash functions, no algorithm identifier is created
   for shorter lengths.  The length of the hash value stored is 256 bits
   for SHAKE-128 and 512 bits for SHAKE-256.

   The COSE capabilities array for these algorithms is empty.
```

*Source `.cache/rfc-9054.txt` lines 340-353 · `sha256:4451e3c19f3db6a1b05806730f7844e6f4a68779d211a0f0838d62cb7dd9212f`*


**Table 3.**

```
   +========+=====+=============+==============+=========+=============+
   |Name    |Value|Description  | Capabilities |Reference| Recommended |
   +========+=====+=============+==============+=========+=============+
   |SHAKE128|-18  |SHAKE-128    | []           |RFC 9054 | Yes         |
   |        |     |256-bit Hash |              |         |             |
   |        |     |Value        |              |         |             |
   +--------+-----+-------------+--------------+---------+-------------+
   |SHAKE256|-45  |SHAKE-256    | []           |RFC 9054 | Yes         |
   |        |     |512-bit Hash |              |         |             |
   |        |     |Value        |              |         |             |
   +--------+-----+-------------+--------------+---------+-------------+

                       Table 3: SHAKE Hash Functions
```

*Source `.cache/rfc-9054.txt` lines 355-367 · `sha256:2c19350d53ae459b1137874698e1bc9f977e20869d4dad40d7cad29cc7e9ea7a`*


## §4.1 — COSE Algorithm Registry

**The registration actions, the size rationale, and definition 2 of 2 of
"Filter Only".** The size rationale does not hold against RFC 8949 §3: five of
the eight identifiers (−14 to −18) encode in **one** octet, not two, and
SHA-1 at −14 is in the *shortest* class available while the sentence says a
"longer algorithm identifier is appropriate" for it. Measured in
`examples/vectors.yaml`; no erratum covers it. The last paragraph is the
wording the contradiction with `rfc-9360` turns on: **"not to be used for
purposes that require collision resistance"**.

```
   IANA has registered the following algorithms in the "COSE Algorithms"
   registry (https://www.iana.org/assignments/cose/).

   *  The SHA-1 hash function found in Table 1.

   *  The set of SHA-2 hash functions found in Table 2.

   *  The set of SHAKE hash functions found in Table 3.

   Many of the hash values produced are relatively long; as such, use of
   a two-byte algorithm identifier seems reasonable.  SHA-1 is tagged as
   "Filter Only", so a longer algorithm identifier is appropriate even
   though it is a shorter hash value.

   IANA has added the value of "Filter Only" to the set of legal values
   for the Recommended column.  This value is only to be used for hash
   functions and indicates that it is not to be used for purposes that
   require collision resistance.  As a result of this addition, IANA has
   added this document as a reference for the "COSE Algorithms"
   registry.
```

*Source `.cache/rfc-9054.txt` lines 373-392 · `sha256:93656884ccccfd15386d8be024753ae2a69727f227fc5d624af236314da1cc86`*


## §5 — Security Considerations

**The property `rfc-9360` §2's protected `x5t` actually needs is named here
and nowhere in `rfc-9360`:** second pre-image resistance, and the distinction
from collision resistance. Measured: `collision` occurs **15 times** in
RFC 9054 and **zero times** in RFC 9360.

```
   Protocols need to perform a careful analysis of the properties of a
   hash function that are needed and how they map onto the possible
   attacks.  In particular, one needs to distinguish between those uses
   that need the cryptographic properties, such as collision resistance,
   and uses that only need properties that correspond to possible object
   identification.  The different attacks correspond to who or what is
   being protected: is it the originator that is the attacker or a third
   party?  This is the difference between collision resistance and
   second pre-image resistance.  As a general rule, longer hash values
   are "better" than short ones, but trade-offs of transmission size,
   timeliness, and security all need to be included as part of this
   analysis.  In many cases, the value being hashed is a public value
   and, as such, (first) pre-image resistance is not part of this
   analysis.
```

*Source `.cache/rfc-9054.txt` lines 396-409 · `sha256:9cad853baaa65665623772d878f14a1f98b3d72a4ee66a8aceb35fae3112f209`*


Algorithm agility as advice — "needs to be considered a requirement" — with no
negotiation, no deprecation mechanism and no way to express which H an
endpoint accepts.

```
   Algorithm agility needs to be considered a requirement for any use of
   hash functions [BCP201].  As with any cryptographic function, hash
   functions are under constant attack, and the cryptographic strength
   of hash algorithms will be reduced over time.
```

*Source `.cache/rfc-9054.txt` lines 411-414 · `sha256:7bc5d9ebd36fde0e74a3297a3f777e7f5229a48c54588fc6605840cdca44b51d`*


---

## What is deliberately not in this file

- **§6's references** (lines 418–493). Bibliography, not normative text. Two
  facts worth recording: the **normative** list is FIPS 180-4, FIPS 202,
  RFC 2119, RFC 3174, RFC 8174 and RFC 9052 — so the SHA-2 and SHA-3 standards
  are normative and the COSE structures document is too — while `[CMS]`,
  `[COSE]`, `[COSE-x509]`, `[ESS]`, `[BCP201]`, `[SUIT-MANIFEST]`,
  `[RFC6194]` and `[SHA-1-collision]` are informative. And `[COSE-x509]` is
  cited as **`draft-ietf-cose-x509-08`**, not as RFC 9360, because RFC 9360
  was still six months away.
- **The Author's Address** (lines 495–498).
- **The front matter** (lines 1–70): masthead, Abstract, Status of This Memo,
  Copyright Notice and Table of Contents. "Category: Informational" (line 7)
  and the Status paragraph (lines 25–26) are quoted in `summary.md`'s metadata
  table.
- **Nothing else.** Every line of §1 through §5 that carries an obligation, a
  definition, a registry row, a registry action or a security claim is above.
