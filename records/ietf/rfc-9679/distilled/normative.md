---
record: rfc-9679
kind: normative
title: "rfc-9679 — normative statements"
extracted: "2026-10-18"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 9679, "CBOR Object Signing and Encryption (COSE) Key Thumbprint",
K. Isobe, H. Tschofenig, O. Steele, December 2024. Standards Track,
ISSN 2070-1721. 627 lines;
`sha256:f6b460e38ba1496bbba7d1430175f6398af104d6b8803f7a4ea059af5d3fa29d`.
Quotations are verbatim from the plain-text RFC. Blocks that reproduce tables,
lists, structures, or pseudocode preserve the source's own line breaks and
indentation inside fenced blocks.

## How to read this file

- A quoted run in a `- (§x)` bullet is **running prose**, verbatim, with the
  RFC line wrapping undone: a line break and the indentation that follows it
  become a single space. The RFC's two spaces after a sentence-ending period
  are kept where a quote spans one. Nothing else is altered. One exception,
  and it is not cosmetic: where the RFC breaks an already-hyphenated word
  across lines ("low-" / "entropy", §7) the halves are rejoined with **no**
  space, because "low- entropy" is not a word the source contains.
- A quoted run opens at the **first** `"` on the line and closes at the **last
  `"` before the first annotation marker** — ` _[` or ` — ` — or, where no
  annotation follows, at the last `"` on the line. The RFC writes parameter
  names in double quotes of its own, so a quoted run routinely contains `"`
  characters; nothing inside the run is escaped, and nothing is added. Any
  `_[...]_` annotation or editorial note follows the closing `"`, **and may
  itself quote a word** — six lines here do exactly that (§3 "may", §4.6
  "should", §5.2 "must" and "may", §6 "link breaks", §7 "should").
  *(Corrected by the verify pass: this rule previously read "its first and last
  `"` on the line", which those six lines falsify — a mechanical reader
  following it swallowed the annotation into the run. The quoted runs
  themselves were all correct; only the rule for finding them was wrong.)*
- A **fenced block** reproduces source lines byte-exactly, three-space RFC
  left margin and all. Every bullet list, structure, example and registration
  template is fenced, so nothing whitespace-significant is rewrapped.
- Everything outside a quote or a fence — headings, locators, labels — is
  structure added by this extraction, not source text. No two non-adjacent
  passages are ever spliced into one quoted run.
- **BCP 14 census of the source body**, excluding the §2 boilerplate
  enumeration: 10 `MUST`, 2 `MUST NOT`, 1 `MAY` = **13 occurrences**. No
  `SHALL`, `SHALL NOT`, `SHOULD`, `SHOULD NOT`, `REQUIRED`, `RECOMMENDED`,
  `NOT RECOMMENDED` or `OPTIONAL` appears anywhere outside that enumeration.
  Verified with `bin/bcp14-count .cache/rfc-9679.txt --by-keyword`.
- Where a statement carries binding content in **lowercase** — a step of the
  §3 procedure, a required-parameter list, an exclusion rule, a registration
  value — it is marked `_[lowercase/implied]_`. Eight of this document's
  thirteen keyword occurrences sit in §3, §4 and §5.7; most of what an
  implementer must obey to reproduce a thumbprint byte-for-byte is stated
  without a keyword, and the marker records which is which.
- §1 (Introduction) is motivation and is dropped, as are §9 (References),
  Acknowledgements and Authors' Addresses.

## §2. Terminology

- (§2) "The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here."

  Verbatim, with the source's own line breaks:

```text
   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in
   BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.
```

## §3. COSE Key Thumbprint

- (§3) "The thumbprint of a COSE Key MUST be computed as follows:"

  The three numbered steps the sentence above governs, verbatim:

```text
   1.  Construct a COSE_Key structure (see Section 7 of [RFC9052])
       containing only the required parameters representing the key as
       described in Section 4 of this document.

   2.  Apply the deterministic encoding described in Section 4.2.1 of
       [RFC8949] to the representation constructed in step 1.

   3.  Hash the bytes produced in step 2 with a cryptographic hash
       function H.  For example, SHA-256 [RFC6234] may be used as a hash
       function.
```

- (§3) "Construct a COSE_Key structure (see Section 7 of [RFC9052]) containing only the required parameters representing the key as described in Section 4 of this document." _[lowercase/implied]_ — step 1, governed by the MUST above.
- (§3) "Apply the deterministic encoding described in Section 4.2.1 of [RFC8949] to the representation constructed in step 1." _[lowercase/implied]_ — step 2, governed by the MUST above.
- (§3) "Hash the bytes produced in step 2 with a cryptographic hash function H." _[lowercase/implied]_ — step 3, governed by the MUST above.
- (§3) "For example, SHA-256 [RFC6234] may be used as a hash function." _[lowercase/implied]_ — lowercase "may", inside step 3; an illustration, not an obligation.
- (§3) "The details of this computation are further described in subsequent sections."
- (§3) "The SHA-256 hash algorithm MUST be supported; other algorithms MAY be supported."

## §4. Required COSE Key Parameters

- (§4) "Only the required parameters of a key's representation are used when computing its COSE Key Thumbprint value." _[lowercase/implied]_
- (§4) "This section summarizes the required parameters."
- (§4) "The "kty" (label: 1) element MUST be present for all key types, and the integer value specified in the IANA "COSE Key Types" registry MUST be used."
- (§4) "The tstr data type is not used with the "kty" element." _[lowercase/implied]_
- (§4) "Many COSE Key parameters are specific to the chosen key type."
- (§4) "The following subsections list the required parameters for commonly used key types."

### §4.1. Octet Key Pair (OKP)

- (§4.1) "The required parameters for elliptic curve public keys that use the Octet Key Pair (OKP) key type, such as X25519, are:" _[lowercase/implied]_

  The list itself, verbatim:

```text
   *  "kty" (label: 1, data type: int, value: 1)

   *  "crv" (label: -1, value: int)

   *  "x" (label: -2, value: bstr)
```

- (§4.1) "Further details are described in Section 7.1 of [RFC9053]."

### §4.2. Elliptic Curve Keys with X- and Y-Coordinates

- (§4.2) "The required parameters for elliptic curve public keys that use the EC2 key type, such as NIST P-256, are:" _[lowercase/implied]_

  The list itself, verbatim:

```text
   *  "kty" (label: 1, data type: int, value: 2)

   *  "crv" (label: -1, data type: int)

   *  "x" (label: -2, data type: bstr)

   *  "y" (label: -3, data type: bstr)
```

- (§4.2) "Further details are described in Section 7.1 of [RFC9053]."
- (§4.2) "Note: [RFC9052] supports both compressed and uncompressed point representations."
- (§4.2) "For interoperability, implementations adhering to this specification MUST use the uncompressed point representation."
- (§4.2) "Therefore, the y-coordinate is expressed as a bstr." _[lowercase/implied]_
- (§4.2) "If an implementation uses the compressed point representation, it MUST first convert it to the uncompressed form for the purpose of thumbprint calculation."

### §4.3. RSA Public Keys

- (§4.3) "The required parameters for an RSA public key are:" _[lowercase/implied]_

  The list itself, verbatim:

```text
   *  "kty" (label: 1, data type: int, value: 3)

   *  "n" (label: -1, data type: bstr)

   *  "e" (label: -2, data type: bstr)
```

### §4.4. Symmetric Keys

- (§4.4) "The required parameters for a symmetric key are:" _[lowercase/implied]_

  The list itself, verbatim:

```text
   *  "kty" (label: 1, data type: int, value: 4)

   *  "k" (label: -1, data type: bstr)
```

### §4.5. HSS-LMS Keys

- (§4.5) "The required parameters for HSS-LMS keys are:" _[lowercase/implied]_

  The list itself, verbatim:

```text
   *  "kty" (label: 1, data type: int, value: 5)

   *  "pub" (label: -1, data type: bstr)
```

### §4.6. Others

- (§4.6) "As other key type values are defined, their defining specifications should be similarly consulted to determine which parameters, in addition to the "kty" element, are required." _[lowercase/implied]_ — lowercase "should".

## §5. Miscellaneous Considerations

### §5.1. Why Not Include Optional COSE Key Parameters?

- (§5.1) "Optional parameters of COSE Keys are intentionally not included in the COSE Key Thumbprint computation so that their absence or presence in the COSE Key does not alter the resulting value." _[lowercase/implied]_
- (§5.1) "The COSE Key Thumbprint is a digest of the ordered essential parameters needed to represent a COSE Key, with all other parameters excluded." _[lowercase/implied]_
- (§5.1) "By excluding optional parameters, the COSE Key Thumbprint consistently refers to the key itself, not to a key with additional attributes."
- (§5.1) "Different application contexts may include various optional attributes in the COSE Key structure."
- (§5.1) "If these optional parameters were included in the thumbprint calculation, the resulting values could differ for the same key depending on the attributes present."
- (§5.1) "Including only the required parameters ensures that the COSE Key Thumbprint remains consistent for a given key, regardless of any additional attributes." _[lowercase/implied]_
- (§5.1) "Different kinds of thumbprints could be defined by other specifications that might include some or all additional COSE Key parameters, if use cases arise where such different kinds of thumbprints would be useful."

### §5.2. Selection of Hash Function

- (§5.2) "A specific hash function must be chosen by an application to compute the hash value of the hash input." _[lowercase/implied]_ — lowercase "must".
- (§5.2) "For instance, SHA-256 [RFC6234] may be used as the hash function." _[lowercase/implied]_ — lowercase "may".
- (§5.2) "While SHA-256 is a good default choice at the time of writing, the preferred hash function may evolve as the cryptographic landscape develops."
- (§5.2) "In many cases, only the party that generates the key needs to be aware of the hash function used."
- (§5.2) "For example, the key producer might use the thumbprint value as a "kid" (key ID)."
- (§5.2) "In such scenarios, the consumer of the "kid" treats it as an opaque value solely for key selection."
- (§5.2) "However, when multiple parties are involved in reproducing and comparing the COSE Key Thumbprint, it is crucial that they know and use the same hash function to ensure consistent results." _[lowercase/implied]_

### §5.3. Thumbprints of Keys Not in COSE Key Format

- (§5.3) "Keys that are in other formats can be represented as COSE Keys."
- (§5.3) "The only prerequisites are that the COSE_Key representation of the key be defined and the party creating the COSE Key Thumbprint be in possession of the necessary key material." _[lowercase/implied]_

### §5.4. Relationship to Digests of X.509 Values

- (§5.4) "COSE Key Thumbprint values are computed on the COSE Key object containing only essential parameters in a specific order." _[lowercase/implied]_
- (§5.4) "Thus, they are more analogous to applications that use digests of X.509 Subject Public Key Info (SPKI) values, which are defined in Section 4.1.2.7 of [RFC5280], than to applications that use digests of complete certificate values, as the "x5t" (X.509 certificate SHA-1 thumbprint) [RFC9360] value defined for X.509 certificate objects does." — [correction] 2026-10-20, maintenance pass on this `profile: full` record (library#39 Tier 2), prompted by the `rfc-9360` summary. The quoted bytes are correct and are left exactly as captured; the error is the source's, inside them. "SHA-1" occurs ZERO times in RFC 9360 under every spelling checked — SHA-1, SHA1, sha-1, sha1, 0 each. Its `x5t` is hash-agile: "COSE_CertHash = [ hashAlg: (int / tstr), hashValue: bstr ]" with the first element "an algorithm identifier ... of the algorithm registered in the "COSE Algorithms" registry", and the only SHA named anywhere in RFC 9360 is §2's "MUST support the hash algorithm 'SHA-256' but can use other hash algorithms". The parenthetical is the JOSE registry name for `x5t`, imported wholesale and attached to the COSE citation — and source line 276, this sentence, is the ONLY place RFC 9679's body names [RFC9360] at all, as `x5t` is the only occurrence of that string in the document. Third instance of one pattern in §5.4–§5.5; `distilled/README.md` item 4 carries all three and the pattern.
- (§5.4) "While logically equivalent to a digest of the SPKI representation of the key, a COSE Key Thumbprint is computed over the CBOR representation of that key rather than over an ASN.1 representation of it." _[lowercase/implied]_

### §5.5. Relationship to JSON Web Key Thumbprints

- (§5.5) "The ckt of a COSE Key, as described in Section 7 of [RFC9052], and the jkt of a JSON Web Key, as described in Section 4 of [RFC7517], are different even when the underlying cryptographic key material is the same." _[lowercase/implied]_
- (§5.5) "This document does not register a JWT confirmation method [RFC7800] for using "ckt" as a confirmation method for a JWT or a CWT confirmation method [RFC8747] for using "jkt" as a confirmation method for a CWT." _[lowercase/implied]_

### §5.6. Confirmation Method

- (§5.6) "[RFC8747] introduces confirmation methods for use with CWTs with the addition of the "cnf" claim."
- (§5.6) "CWTs are defined in [RFC8392]."
- (§5.6) "This specification adds a new confirmation method based on COSE Key Thumbprints."
- (§5.6) "The proof-of-possession key is identified using the "ckt" member of the CWT confirmation claim "cnf"." _[lowercase/implied]_
- (§5.6) "This member contains the value of the COSE Key Thumbprint encoded as a binary string." _[lowercase/implied]_
- (§5.6) "Instead of communicating the actual COSE Key, only the thumbprint is conveyed."
- (§5.6) "This approach assumes that the recipient is able to obtain the identified COSE Key using the thumbprint contained in the "ckt" member."
- (§5.6) "In this approach, the issuer of a CWT declares that the presenter possesses a particular key and that the recipient can cryptographically confirm the presenter's proof of possession of the key by including a "ckt" CWT confirmation method member in the CWT."
- (§5.6) "The following example demonstrates the use of the "ckt" member in a CWT as part of the confirmation method (with line breaks inserted for editorial reasons):"

  The example itself, verbatim:

```text
      {
       /iss/ 1 : "coaps://as.example.com",
       /aud/ 3 : "coaps://resource.example.org",
       /exp/ 4 : 1361398824,
       /cnf/ 8 : {
         /ckt/ 5 : h'496bd8afadf307e5b08c64b0421bf9dc
                     01528a344a43bda88fadd1669da253ec'
        }
      }
```

- (§5.6) "Section 8 registers the "ckt" CWT confirmation method member."
- (§5.6) "The "ckt" member is used in the "cnf" claim." _[lowercase/implied]_

### §5.7. COSE Key Thumbprint URIs

- (§5.7) "This specification defines Uniform Resource Identifiers (URIs) to represent a COSE Key Thumbprint value."
- (§5.7) "The design follows the work of JSON Web Key (JWK) Thumbprint URIs, as specified in [RFC9278]."
- (§5.7) "This enables COSE Key Thumbprints to be used, for example, as key identifiers in contexts requiring URIs."
- (§5.7) "This specification defines a URI prefix indicating that the portion of the URI following the prefix is a COSE Key Thumbprint." _[lowercase/implied]_
- (§5.7) "The following URI prefix is defined to indicate that the portion of the URI following the prefix is a COSE Key Thumbprint:" _[lowercase/implied]_

  The prefix itself, verbatim:

```text
      urn:ietf:params:oauth:ckt
```

- (§5.7) "To make the hash algorithm being used explicit in a URI, the prefix is followed by a hash algorithm identifier and a COSE Key Thumbprint value, each separated by a colon character to form a URI representing a COSE Key Thumbprint." _[lowercase/implied]_
- (§5.7) "Hash algorithm identifiers used in COSE Key Thumbprint URIs MUST be values from the "Hash Name String" column in the IANA "Named Information Hash Algorithm Registry" [IANA.Hash.Algorithms]."
- (§5.7) "COSE Key Thumbprint URIs with hash algorithm identifiers not found in this registry are not considered valid, and applications MUST detect and handle this error, should it occur."
- (§5.7) "Since the URN is encoded as a string, the output of the COSE Key Thumbprint computation described in Section 3 MUST be base64url encoded without padding."
- (§5.7) "[RFC7515] specifies base64url encoding as follows:"

  The quoted definition, verbatim, the source's own `|` quote markers included:

```text
   |  Base64 encoding using the URL- and filename-safe character set
   |  defined in Section 5 of RFC 4648 [RFC4648], with all trailing '='
   |  characters omitted (as permitted by Section 3.2 of [RFC7515]) and
   |  without the inclusion of any line breaks, whitespace, or other
   |  additional characters.  Note that the base64url encoding of the
   |  empty octet sequence is the empty string.  (See Appendix C of
   |  [RFC7515] for notes on implementing base64url encoding without
   |  padding.)
```

- (§5.7) "The base64url encoding of the thumbprint shown in Section 6 is shown below (with a line break added for readability purposes)."

  The encoded thumbprint, verbatim:

```text
      SWvYr63zB-WwjGSwQhv53AFSijRKQ72oj63RZp2iU-w
```

- (§5.7) "The full example of a COSE Key Thumbprint URI is shown below (with a line break added for readability)."

  The full URI, verbatim — the blank line inside it is the source's own "line break added for readability":

```text
      urn:ietf:params:oauth:ckt:sha-256:

      SWvYr63zB-WwjGSwQhv53AFSijRKQ72oj63RZp2iU-w
```

- (§5.7) "Note that the use of oauth in the namespace is to align with JWK Thumbprint URIs as described in [RFC9278]; however, these URIs are intended for use with applications and specifications not necessarily related to OAuth."

## §6. Example

- (§6) "This section demonstrates the COSE Key Thumbprint computation for the following example COSE Key containing an Elliptic Curve Cryptography (ECC) public key."
- (§6) "For better readability, the example is first presented in CBOR diagnostic format (with the long line broken for display purposes only)."

  The example COSE Key in CBOR diagnostic notation, verbatim:

```text
     {
       / kty set to EC2 = Elliptic Curve Keys /
       1:2,
       / crv set to P-256 /
       -1:1,
       / public key: x-coordinate /
       -2:h'65eda5a12577c2bae829437fe338701a10aaa375e1bb5b5de108de439c0
   8551d',
       / public key: y-coordinate /
       -3:h'1e52ed75701163f7f9e40ddf9f341b3dc9ba860af7e0ca7ca7e9eecd008
   4d19c',
       / kid is bstr, not used in COSE Key Thumbprint /
       2:h'496bd8afadf307e5b08c64b0421bf9dc01528a344a43bda88fadd1669da2
   53ec'
     }
```

- (§6) "The example above corresponds to the following CBOR encoding (with link breaks added for display purposes only):" _[lowercase/implied]_ — "link breaks" is the source's own text, reproduced as printed.

  The encoding itself, verbatim:

```text
   A50102200121582065EDA5A12577C2BAE829437FE338701A10AAA375E1BB5B5DE108D
   E439C08551D2258201E52ED75701163F7F9E40DDF9F341B3DC9BA860AF7E0CA7CA7E9
   EECD0084D19C025820496BD8AFADF307E5B08C64B0421BF9DC01528A344A43BDA88FA
   DD1669DA253EC
```

- (§6) "Not all of the parameters from the example above are used in the COSE Key Thumbprint computation because the required parameters of an elliptic curve public key are (as listed in Section 4.2) "kty", "crv", "x", and "y"." _[lowercase/implied]_
- (§6) "The resulting COSE Key structure, in CBOR diagnostic format with line breaks added for better readability, with the minimum parameters in the correct order are:" _[lowercase/implied]_

  The thumbprint input in CBOR diagnostic notation, verbatim:

```text
   {
      1:2,
     -1:1,
     -2:h'65eda5a12577c2bae829437fe338701a
          10aaa375e1bb5b5de108de439c08551d',
     -3:h'1e52ed75701163f7f9e40ddf9f341b3d
          c9ba860af7e0ca7ca7e9eecd0084d19c'
   }
```

- (§6) "In CBOR encoding, the result is (with line breaks added for display purposes only):" _[lowercase/implied]_

  The bytes that are hashed, verbatim:

```text
   A40102200121582065EDA5A12577C2BAE829437FE338701A10AAA375E1BB5B5DE
   108DE439C08551D2258201E52ED75701163F7F9E40DDF9F341B3DC9BA860AF7E0
   CA7CA7E9EECD0084D19C
```

- (§6) "Using SHA-256, the resulting thumbprint is:" _[lowercase/implied]_

  The thumbprint itself, verbatim:

```text
   496bd8afadf307e5b08c64b0421bf9dc01528a344a43bda88fadd1669da253ec
```

## §7. Security Considerations

- (§7) "A COSE Key Thumbprint will only uniquely identify a particular key if a single unambiguous COSE Key representation for that key is defined and used when computing the COSE Key Thumbprint." _[lowercase/implied]_
- (§7) "Key identifiers are not included in the thumbprint calculation (similarly to other optional parameters in the COSE_Key structure)." _[lowercase/implied]_
- (§7) "If the inclusion of specific optional parameters in the thumbprint calculation is important for a particular application, this specification would not be suitable."
- (§7) "While thumbprint values are useful for identifying legitimate keys, comparing thumbprint values is not a reliable means of excluding the use of particular keys (or transformations thereof)."
- (§7) "The reason is because an attacker may supply a key that is a transformation of a key in order for it to appear as a different key."
- (§7) "For instance, if a legitimate RSA key uses a modulus value N and an attacker supplies a key with modulus 3*N, the modified key would still work about 1/3 of the time, but it would appear to be a different key."
- (§7) "Producing thumbprints of symmetric keys needs to be done with care."
- (§7) "Developers MUST ensure that the symmetric key has sufficient entropy to prevent attackers from precomputing tables of symmetric keys with their corresponding hash values."
- (§7) "This can be prevented if the symmetric key is a randomly selected key of at least a 128-bit length."
- (§7) "Thumbprints MUST NOT be used with passwords or other low-entropy secrets."
- (§7) "If a developer is unable to determine whether all symmetric keys used in an application have sufficient entropy, then thumbprints of symmetric keys MUST NOT be used."
- (§7) "In general, using thumbprints of symmetric keys should only be used in special applications." _[lowercase/implied]_ — lowercase "should".
- (§7) "In most other deployment scenarios, it is more appropriate to utilize a different naming scheme for key identifiers."

## §8. IANA Considerations

- (§8) "IANA has added the following entry to the "CWT Confirmation Methods" registry [IANA-CWT] established by [RFC8747]:" _[lowercase/implied]_

  The registration itself, verbatim:

```text
   Confirmation Method Name:  ckt
   Confirmation Method Description:  COSE Key SHA-256 Thumbprint
   JWT Confirmation Method Name:  (none)
   Confirmation Key:  5
   Confirmation Value Type(s):  binary string
   Change Controller:  IETF
   Specification Document(s):  RFC 9679
```

- (§8) "Furthermore, IANA has added a value to the "OAuth URI" registry [IANA-OAuth] established by [RFC6755]:" _[lowercase/implied]_

  The registration itself, verbatim:

```text
   URN:  urn:ietf:params:oauth:ckt
   Common Name:  COSE Key Thumbprint URI
   Change Controller:  IETF
   Specification Document(s):  RFC 9679
```

## Not reproduced here

§1 (Introduction) — motivation and use cases, no constraint. §9 (References),
Acknowledgements and Authors' Addresses — bibliography and credits. The RFC
boilerplate preceding §1 (Status of This Memo, Copyright Notice, Table of
Contents) — IETF front matter, no constraint on an implementation.
