---
record: rfc-9964
kind: normative
title: "rfc-9964 — normative statements"
extracted: "2026-10-19"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 9964, "ML-DSA for JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE)", Standards Track, May 2026 (M. Prorock, O. Steele, Tradeverifyd; ISSN 2070-1721). Quotations are verbatim from the plain-text RFC at `content.sha256` `8c42035b948301b197d431de8b3f40019bdaa3bb40150dc523306923948f34cf`. Blocks that reproduce tables, figures, bullet lists or IANA registration templates preserve the source's own line breaks and indentation inside fenced blocks, and each fence is an exact consecutive run of source lines whose range is given above it.

**Line-break severances — declared, never healed.** Three prose sentences in this
document contain a token the plain-text line wrap cuts in two, so those sentences
**cannot be quoted whole**. Each is quoted as its obligation-bearing half and the
severance is named at the point of use:

| source lines | token severed | rendered by the wrap as |
|---|---|---|
| 18-19 (Abstract) | `Post-Quantum` | `Post-` + `Quantum` |
| 180-181 (§5) | `ML-DSA-87` | `ML-` + `DSA-87` |
| 219-220 (§5) | `ML-DSA-65` | `ML-DSA-` + `65` |

The 219-220 break is the one that matters: it falls inside the only
algorithm-behaviour `MUST` in the document.

**What this document does not contain.** It defines no protocol exchange, no
roles, no message flow and no key lifecycle. The words *protocol*, *exchange*,
*handshake*, *negotiate*, *state*, *rotate*, *expire* and *revoke* do not occur
anywhere in its 2906 lines; neither do *EdDSA*, *Ed25519*, *Ed448*, *crv*,
*curve* or *OKP*. Signing is delegated by citation (§5, "Algorithm 2 of US NIST
[FIPS-204]"); **no verification algorithm is named at all** — "verify" occurs
once in the prose, in §7.2's phrase "the verify routines are different". See
*Observations on the source*.


## Abstract (lines 14-20)

- (Abstract) "This document specifies JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) serializations for the Module-Lattice-Based Digital Signature Standard (ML-DSA)" — **quoted half only.** The sentence continues "a Post-" / "Quantum Cryptography (PQC) digital signature scheme defined in US NIST FIPS 204.", and the wrap at lines 18-19 severs `Post-Quantum`, so it cannot be quoted whole. "serializations" is used here and nowhere else in the document.


## §1. Introduction

- (§1) "This document specifies how to use ML-DSA keys and signatures as described in [FIPS-204] in conjunction with JOSE and COSE."
- (§1) "A new key type named Algorithm Key Pair (AKP) is defined to express public and private keys for use with algorithms not limited to those registered in this document."
- (§1) "Similarly, a new thumbprint algorithm is defined for AKP to ensure these keys can be compared according to the procedures defined in [RFC7638] and [RFC9679]."

The third sentence is the document's own statement of why §6 exists, and it names
RFC 9679 explicitly. Read against §6, which defines **no new algorithm** and
instead says the thumbprint "is produced according to the process described in
Section 3 of [RFC9679]", "a new thumbprint algorithm" overstates what §6 does —
see *Observations on the source*.


## §2. Terminology

- (§2) "The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here."
- (§2) "Some examples in this specification are truncated using "..." for readability."

The second sentence is load-bearing for the test-vector artifact: the two figures
in §3 are truncated and are **not** usable as fixtures. The six figures in
Appendix A are not truncated.


## §3. AKP Key Type

- (§3) "This section specifies a generic cryptographic key structure for use with algorithms not limited to those registered in this document."
- (§3) "The Algorithm Key Pair (AKP) type is used to express public and private keys for use with algorithms."
- (§3) "The concept of public and private information classes for key pairs originates from Section 8.1 of [RFC7517]."
- (§3) "The parameters for public and private information classes contain byte strings in a format specified by the alg value."
- (§3) "The alg JSON Web Key (JWK) parameter or COSE Key Common parameter is REQUIRED for all AKP keys."
- (§3) "The pub parameter contains public information and is REQUIRED."
- (§3) "The priv parameter contains private information and MUST NOT be present in public keys."
- (§3) "Some algorithms may require or recommend additional structure or length checks for associated key type parameters."
- (§3) "When AKP keys are expressed as JWKs, the key parameters are base64url encoded."
- (§3) "When AKP keys are expressed as COSE keys, no encoding is needed."
- (§3) "This document introduces the AKP key type in [IANA.jose]:"
- (§3) "This document introduces the AKP key type in [IANA.cose]:"

**§3 carries the whole of the format story for `pub` and `priv`.** There is no
`crv` parameter and no second discriminator of any kind: the byte strings' format
is "specified by the alg value" and nothing else. The two "introduces the AKP key
type in" sentences each end in a colon that introduces nothing — see
*Observations on the source*.

Figure 1 — source lines 128-136, truncated per §2:

```text
   {
      "kid": "T4xl70S7MT6Zeq6r9V9fPJGVn76wfnXJ21-gyo0Gu6o",
      "kty": "AKP",
      "alg": "ML-DSA-44",
      "pub": "unH59k4Ru...DZgbTP07e7gEWzw4MFRrndjbDQ",
      "priv": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
   }

                   Figure 1: The All-Zeros ML-DSA-44 JWK
```

Figure 2 — source lines 143-151, truncated per §2. This is the document's own
in-text witness for the COSE code points `kty` = 7 and `alg` = -48:

```text
   {
      / kid /   2: h'b8969ab4b37da9f068...6f0583bf5b8d3a8059a',
      / kty /   1: 7, / AKP /
      / alg /   3: -48, / ML-DSA-44 /
      / pub  / -1: h'ba71f9f64e11baeb589...3830546b9dd8db0d',
      / priv / -2: h'00000000000000...0000000000000000'
   }

                 Figure 2: The All-Zeros ML-DSA-44 COSE Key
```


## §4. ML-DSA Private Keys

- (§4) "Note that US NIST [FIPS-204] defines 2 expressions for private keys: a seed, and a private key that is expanded from the seed."
- (§4) "Unlike [RFC9881], which supports the expanded private key format to maximize interoperability with existing implementations, this document specifies ML-DSA private key information using only the seed format."
- (§4) "The seed format was chosen to provide a single, compact representation that is consistent across both COSE and JOSE, simplifying key management and reducing storage requirements."
- (§4) "For the ML-DSA private keys described in this document, the priv parameter MUST be the seed and MUST have a length of 32 bytes."
- (§4) "This specification intentionally does not define a means of utilizing the expanded private key representation defined by US NIST FIPS so as to increase interoperability by having a single ML-DSA private key representation for COSE and JOSE."
- (§4) "See the Security Considerations of this document for details."

The fourth bullet is one sentence carrying **two** `MUST`s. It is quoted whole
here; `requirements.yaml` splits it into two entries, each quoting its own
contiguous clause, so that "is the seed" and "length == 32" are separately
testable.


## §5. ML-DSA Algorithms

- (§5) "The ML-DSA Signature Scheme is parameterized to support different security levels."
- (§5) "DSA-87 are used to refer to ML-DSA with the parameter choices given in Table 1 of [FIPS-204]." — **quoted half only.** The sentence begins "In this document, the abbreviations ML-DSA-44, ML-DSA-65, and ML-" on line 180, and that wrap severs `ML-DSA-87`, so it cannot be quoted whole. The half quoted is the obligation-bearing one: each of the three names denotes one FIPS-204 Table 1 parameter set.
- (§5) "This document has registered the ML-DSA-44, ML-DSA-65, and ML-DSA-87 algorithms in [IANA.jose] and [IANA.cose]."
- (§5) "In accordance with Section 3 of this document, ML-DSA key parameters have the following additional constraints:"
- (§5) "The pub parameter is the ML-DSA public key as described in Section 5.3 of US NIST [FIPS-204]."
- (§5) "The size of pub and the associated signature for each of these algorithms is defined in Table 2 of US NIST [FIPS-204] and repeated here for convenience:"

Table 1 — source lines 197-208, the document's own reproduction of FIPS-204
Table 2. **The "Private Key" column is the expanded private key, not the `priv`
parameter §4 defines**; the note immediately after the table is what reconciles
them:

```text
      +===========+=============+============+================+
      | Algorithm | Private Key | Public Key | Signature Size |
      +===========+=============+============+================+
      | ML-DSA-44 | 2560        | 1312       | 2420           |
      +-----------+-------------+------------+----------------+
      | ML-DSA-65 | 4032        | 1952       | 3309           |
      +-----------+-------------+------------+----------------+
      | ML-DSA-87 | 4896        | 2592       | 4627           |
      +-----------+-------------+------------+----------------+

         Table 1: Sizes (In Bytes) of Keys and Signatures of
                                ML-DSA
```

- (§5) "Note that priv size is always 32 bytes and that KeyGen_internal is called to produce the expanded private keys for "Private Key" in the table above."
- (§5) "See Section 4 for further details."
- (§5) "These algorithms are used to produce signatures as described in Algorithm 2 of US NIST [FIPS-204]."
- (§5) "The ctx parameter MUST be the empty string for ML-DSA-44" — **quoted half only.** The sentence continues ", ML-DSA-" / "65, and ML-DSA-87." across the wrap at lines 219-220, which severs `ML-DSA-65`, so it cannot be quoted whole. The obligation is on all three algorithms. `ctx` occurs **exactly once** in the whole document, on line 219: it is never defined, never registered in §8, and never appears in any figure, so this `MUST` constrains the FIPS-204 signing call and not the wire format.
- (§5) "Signatures are encoded as byte strings using the algorithms defined in Section 7.2 of US NIST [FIPS-204]."
- (§5) "When producing JSON Web Signatures, the signature byte strings are base64url encoded and the encoded signature size is larger than described in the table above."
- (§5) "When producing COSE signatures, no encoding is needed; see Section 4 of [RFC9052] for more details on how COSE signatures are created."
- (§5) "Table 2 of [FIPS-204] describes the ML-DSA key and signature sizes."
- (§5) "ML-DSA produces significantly larger public keys and signatures compared to traditional algorithms."
- (§5) "This size increase can create challenges for deployments with limited bandwidth, memory, or processing capacity."
- (§5) "ML-DSA may not be suitable for use cases requiring small keys or signatures."
- (§5) "Use of thumbprints as described in [RFC7638] and [RFC9679] can reduce the need to repeat public key representations."


## §6. AKP Thumbprints

This is the section RFC 9679 §4.6 delegates to. Both lead-in sentences and all
nine bullets are reproduced.

- (§6) "Although this document specifies how to represent ML-DSA keys using AKP, the AKP key type and thumbprint computations are suitable for use with algorithms other than ML-DSA."
- (§6) "When computing the COSE Key Thumbprint as described in [RFC9679], the required parameters for AKPs are:"

Source lines 249-253 — the required COSE Key Thumbprint parameters for AKP. The
source gives these as a **bullet list, not a sentence**; this is the form in
which the document states them:

```text
   *  "kty" (label: 1, data type: int, value: 7)

   *  "alg" (label: 3, data type: int, value: int)

   *  "pub" (label: -1, value: bstr)
```

- (§6) "The COSE Key Thumbprint is produced according to the process described in Section 3 of [RFC9679]."
- (§6) "When computing the JWK Thumbprint as described in [RFC7638], the required parameters for AKPs are:"

Source lines 261-265:

```text
   *  "kty"

   *  "alg"

   *  "pub"
```

- (§6) "Their lexicographic order, per Section 3.3 of [RFC7638], is:"

Source lines 269-273:

```text
   *  "alg"

   *  "kty"

   *  "pub"
```

- (§6) "The JWK Thumbprint is produced according to the process described in Section 3 of [RFC7638]."
- (§6) "See the kid values in the JWK and COSE Key examples in Appendix A for examples of AKP thumbprints."

Note the asymmetry between the two required-parameter lists. The COSE list
(lines 249-253) carries labels and CBOR types; the JWK list (lines 261-265)
carries bare names. Note also that the `pub` bullet alone omits the `data type:`
field that `kty` and `alg` both carry — it reads `(label: -1, value: bstr)`, not
`(label: -1, data type: bstr, value: bstr)`.


## §7. Security Considerations

- (§7) "The security considerations of [RFC7515], [RFC7517], and [RFC9053] apply to this specification as well."
- (§7) "A detailed security analysis of ML-DSA is beyond the scope of this specification; see [FIPS-204] for additional details."
- (§7) "Implementers should also refer to the security considerations in [RFC9881] for additional guidance on ML-DSA deployment considerations, including discussions on randomized versus deterministic signing approaches."

RFC 9881 is an **informative** reference here (§9.2, lines 617-622). Randomized
versus deterministic signing is the document's only word on signing-mode choice,
and it is delegated outside the normative reference set.

### §7.1. Private Key Compromise

- (§7.1) "The seed and the private key expanded from the seed require the same level of protection."
- (§7.1) "If an unauthorized party obtains the seed, or the expanded private key, they can forge signatures."
- (§7.1) "This undermines the authenticity and integrity guarantees provided by ML-DSA, as attackers could impersonate the legitimate signer or alter signed data without detection."

### §7.2. Rationale for Not Supporting HashML-DSA

The whole section, verbatim, all three sentences in order — source lines 303-309:

- (§7.2) "This document does not specify algorithms for use with HashML-DSA as described in Section 5.4 of [FIPS-204]."
- (§7.2) "As the verify routines are different, future support for HashML-DSA would require the registration of additional algorithms."
- (§7.2) "Section 8.3 of [RFC9881] explains the rationale for disallowing HashML-DSA, including the increased complexity and compatibility concerns with existing implementations."

**What kind of argument this is.** The section carries no cost argument of its
own. It makes a *registration-mechanics* statement — "As the verify routines are
different, future support for HashML-DSA would require the registration of
additional algorithms" — and then *delegates the rationale* to §8.3 of RFC 9881,
which it characterises as "the increased complexity and compatibility concerns
with existing implementations". It offers no substitute construction. There is no
memory argument, no streaming argument and no bandwidth argument here; the only
memory language in the document is §5's "limited bandwidth, memory, or
processing capacity", which is about ML-DSA's own key and signature sizes and is
not attached to pre-hashing. RFC 9881 is not held by this library, so the
dispositive rationale sits outside it — and is reached through an informative
reference.

### §7.3. Validation of Keys

- (§7.3) "When an AKP algorithm requires or encourages that a key be validated before being used, all algorithm-related key parameters MUST be validated."
- (§7.3) "Section 7.2 of [FIPS-204] describes the encoding of ML-DSA keys and signatures."
- (§7.3) "For Algorithms 22 and 23 (pkEncode and pkDecode), the inputs need to be within the ranges given in the algorithms."
- (§7.3) "For the ML-DSA algorithms registered in this document, the priv key parameter is the seed, and therefore, the seed length check MUST be performed."
- (§7.3) "The length of the seed is 256 bits, which is 32 bytes."
- (§7.3) "However, when the priv parameter is expanded using KeyGen_internal, the skEncode and skDecode algorithms MUST be used."
- (§7.3) "[FIPS-204] notes "skDecode should only be run on inputs that come from trusted sources" and that "as the seed can be used to compute the private key, it is sensitive data and shall be treated with the same safeguards as a private key"."

The last bullet quotes FIPS-204 inside this RFC. Its "should" and "shall" are
**lowercase** and are therefore not BCP 14 keywords of this document; they are
not counted.

### §7.4. Mismatched AKP Parameters

- (§7.4) "When using an AKP key with an algorithm, it is possible that the public and private information class parameters have been tampered with or mismatched."
- (§7.4) "Depending on the algorithm and implementation, the consequences of using mismatched parameters can range from operations failing to private key compromise."


## §8. IANA Considerations

Every registration template is reproduced in full. These templates, not the
prose, are the operative content of this document: they are where the code points
live.

### §8.1.1. New COSE Algorithms

- (§8.1.1) "IANA has registered the following entries in the "COSE Algorithms" registry."
- (§8.1.1) "The following completed registration actions are provided as described in [RFC9053] and [RFC9054]."

§8.1.1.1 ML-DSA-44 — source lines 349-361:

```text
   Name:  ML-DSA-44

   Value:  -48

   Description:  CBOR Object Signing Algorithm for ML-DSA-44

   Capabilities:  [kty]

   Change Controller:  IETF

   Reference:  RFC 9964

   Recommended:  Yes
```

§8.1.1.2 ML-DSA-65 — source lines 365-377:

```text
   Name:  ML-DSA-65

   Value:  -49

   Description:  CBOR Object Signing Algorithm for ML-DSA-65

   Capabilities:  [kty]

   Change Controller:  IETF

   Reference:  RFC 9964

   Recommended:  Yes
```

§8.1.1.3 ML-DSA-87 — source lines 381-393:

```text
   Name:  ML-DSA-87

   Value:  -50

   Description:  CBOR Object Signing Algorithm for ML-DSA-87

   Capabilities:  [kty]

   Change Controller:  IETF

   Reference:  RFC 9964

   Recommended:  Yes
```


### §8.1.2. New COSE Key Types

- (§8.1.2) "IANA registered the following entry in the "COSE Key Types" registry."
- (§8.1.2) "The following completed registration template is provided as described in [RFC9053]."

Note "IANA registered" here against "IANA has registered" in §8.1.1, §8.1.3,
§8.1.4, §8.1.5 and §8.1.6 — see *Observations on the source*.

§8.1.2.1 AKP — source lines 403-413. This is the normative home of `kty` = 7:

```text
   Name:  AKP

   Value:  7

   Description:  COSE Key Type for Algorithm Key Pairs

   Capabilities:  [kty(7)]

   Change Controller:  IETF

   Reference:  RFC 9964
```


### §8.1.3. New COSE Key Type Parameters

- (§8.1.3) "IANA has registered the following entries in the "COSE Key Type Parameters" registry."
- (§8.1.3) "The following completed registration templates are provided as described in [RFC9053]."

§8.1.3.1 AKP Public Key — source lines 423-433:

```text
   Key Type:  7

   Name:  pub

   Label:  -1

   CBOR Type:  bstr

   Description:  Public key

   Reference:  RFC 9964
```

§8.1.3.2 AKP Private Key — source lines 437-447:

```text
   Key Type:  7

   Name:  priv

   Label:  -2

   CBOR Type:  bstr

   Description:  Private key

   Reference:  RFC 9964
```

These two are the **only** COSE Key Type Parameters registered for `kty` 7.
There is no `crv`, and no other discriminator of parameter set.


### §8.1.4. New JOSE Algorithms

- (§8.1.4) "IANA has registered the following entries in the "JSON Web Signature and Encryption Algorithms" registry."
- (§8.1.4) "The following completed registrations are provided as described in [RFC7518]."

§8.1.4.1 ML-DSA-44 — source lines 457-469:

```text
   Algorithm Name:  ML-DSA-44

   Algorithm Description:  ML-DSA-44 as described in US NIST FIPS 204

   Algorithm Usage Location(s):  alg

   JOSE Implementation Requirements:  Optional

   Change Controller:  IETF

   Specification Document(s):  RFC 9964

   Algorithm Analysis Documents(s):  [FIPS-204]
```

§8.1.4.2 ML-DSA-65 — source lines 473-485:

```text
   Algorithm Name:  ML-DSA-65

   Algorithm Description:  ML-DSA-65 as described in US NIST FIPS 204

   Algorithm Usage Location(s):  alg

   JOSE Implementation Requirements:  Optional

   Change Controller:  IETF

   Specification Document(s):  RFC 9964

   Algorithm Analysis Documents(s):  [FIPS-204]
```

§8.1.4.3 ML-DSA-87 — source lines 489-501:

```text
   Algorithm Name:  ML-DSA-87

   Algorithm Description:  ML-DSA-87 as described in US NIST FIPS 204

   Algorithm Usage Location(s):  alg

   JOSE Implementation Requirements:  Optional

   Change Controller:  IETF

   Specification Document(s):  RFC 9964

   Algorithm Analysis Documents(s):  [FIPS-204]
```

The JOSE algorithm identifiers are the **names** `ML-DSA-44`, `ML-DSA-65` and
`ML-DSA-87`; the negative integers -48, -49 and -50 are COSE-only. Note also that
the three COSE registrations carry `Recommended:  Yes` while the three JOSE ones
carry `JOSE Implementation Requirements:  Optional`.


### §8.1.5. New JOSE Key Types

- (§8.1.5) "IANA has registered the following entry in the "JSON Web Key Types" registry."
- (§8.1.5) "The following completed registration is provided as described in [RFC7518] and [RFC7638]."

§8.1.5.1 AKP — source lines 511-519:

```text
   "kty" Parameter Value:  AKP

   Key Type Description:  Algorithm Key Pair

   JOSE Implementation Requirements:  Optional

   Change Controller:  IETF

   Specification Document(s):  RFC 9964
```


### §8.1.6. New JWK Parameters

- (§8.1.6) "IANA has registered the following entry in the "JSON Web Key Parameters" registry."
- (§8.1.6) "The following completed registrations are provided as described in [RFC7517] and [RFC7638]."

§8.1.6.1 AKP Public Key — source lines 529-539:

```text
   Parameter Name:  pub

   Parameter Description:  Public key

   Used with "kty" Value(s):  AKP

   Parameter Information Class:  Public

   Change Controller:  IETF

   Specification Document(s):  RFC 9964
```

§8.1.6.2 AKP Private Key — source lines 543-553:

```text
   Parameter Name:  priv

   Parameter Description:  Private key

   Used with "kty" Value(s):  AKP

   Parameter Information Class:  Private

   Change Controller:  IETF

   Specification Document(s):  RFC 9964
```

Note the singular "the following entry" in the §8.1.6 lead-in against the two
templates that follow, and the plural "registrations" in its second sentence —
see *Observations on the source*.


## Collated code points — NOT A QUOTATION

Derived by collation from the fenced templates above. Every value carries the
locator and source line of the template it came from. Nothing in this table is
quoted; it exists so a reader need not re-collate twelve templates, and it must
never be cited as the document's own text.

| what | registry | identifier | value | locator | source line |
|---|---|---|---|---|---|
| ML-DSA-44 | COSE Algorithms | `alg` | **-48** | §8.1.1.1 | 351 |
| ML-DSA-65 | COSE Algorithms | `alg` | **-49** | §8.1.1.2 | 367 |
| ML-DSA-87 | COSE Algorithms | `alg` | **-50** | §8.1.1.3 | 383 |
| AKP | COSE Key Types | `kty` | **7** | §8.1.2.1 | 405 |
| AKP public key | COSE Key Type Parameters | `pub` | **-1**, `bstr` | §8.1.3.1 | 427, 429 |
| AKP private key | COSE Key Type Parameters | `priv` | **-2**, `bstr` | §8.1.3.2 | 441, 443 |
| ML-DSA-44 | JOSE Algorithms | `alg` | **`ML-DSA-44`** | §8.1.4.1 | 457 |
| ML-DSA-65 | JOSE Algorithms | `alg` | **`ML-DSA-65`** | §8.1.4.2 | 473 |
| ML-DSA-87 | JOSE Algorithms | `alg` | **`ML-DSA-87`** | §8.1.4.3 | 489 |
| AKP | JSON Web Key Types | `kty` | **`AKP`** | §8.1.5.1 | 511 |
| AKP public key | JWK Parameters | `pub` | Public info class | §8.1.6.1 | 529, 535 |
| AKP private key | JWK Parameters | `priv` | Private info class | §8.1.6.2 | 543, 549 |

Cross-checked against the document's own figures: Figure 2 (§3, lines 145-146)
shows `1: 7` and `3: -48`; Appendix A's COSE `key_diag` lines show `1: 7, 3: -48`
(line 1497), `1: 7, 3: -49` (line 1849) and `1: 7, 3: -50` (line 2329). All
agree.


## Observations on the source — reported, not repaired

1. **Three line-break severances** (lines 18-19, 180-181, 219-220) cut
   `Post-Quantum`, `ML-DSA-87` and `ML-DSA-65` respectively. Declared at the top
   and at each point of use. The 219-220 one falls inside the document's only
   algorithm-behaviour `MUST`.
2. **Two dangling colons in §3.** "This document introduces the AKP key type in
   [IANA.jose]:" (line 123) and the same sentence for `[IANA.cose]` (line 138)
   each end in a colon, but what follows each is a *different* sentence — "An
   example truncated private key for use with ML-DSA-44 in JWK format is
   provided below:" (lines 125-126) and the COSE_Key equivalent (lines 140-141).
   Nothing is introduced after either colon. This reads as drafting residue from
   moving the registration templates to §8.
3. **§1 calls §6 "a new thumbprint algorithm"; §6 defines no algorithm.** §6
   specifies a *required-parameter set* and then says the digest "is produced
   according to the process described in Section 3 of [RFC9679]" (COSE) and
   "Section 3 of [RFC7638]" (JWK) — the same algorithms, different inputs. The
   distinction matters to anyone relying on §6, because what §6 supplies is the
   parameter list RFC 9679 §4.6 asks a defining specification for, not a new
   digest construction.
4. **`ctx` is used once and never defined.** Line 219 imposes `MUST be the empty
   string` on a parameter §8 does not register, no figure contains, and no other
   sentence mentions. It is FIPS-204's signing-call context string, so the
   obligation is on the signer's API call and cannot be checked against a
   received COSE_Sign1 or JWS.
5. **No verification algorithm is cited.** §5 names "Algorithm 2 of US NIST
   [FIPS-204]" for producing signatures. No sentence anywhere names the
   verification algorithm, and §7.2's "the verify routines are different" is the
   only occurrence of "verify" in the prose.
6. **`pub` is referred to two different FIPS-204 sections.** §5 says `pub` is the
   public key "as described in Section 5.3 of US NIST [FIPS-204]"; §7.3 says
   "Section 7.2 of [FIPS-204] describes the encoding of ML-DSA keys and
   signatures" and names Algorithms 22 and 23 (pkEncode/pkDecode). Likely both
   correct and complementary (generation vs encoding), recorded because a reader
   chasing the octet layout hits §5 first and §5 is not where it is.
7. **Table 1's "Private Key" column does not describe `priv`.** It gives
   2560/4032/4896 bytes — the expanded private key — while §4 requires `priv` to
   be the 32-byte seed. The note at lines 210-212 says so, but the table is
   titled "Sizes (In Bytes) of Keys and Signatures of ML-DSA" with no qualifier
   in the column head.
8. **Tense and number inconsistencies in §8.** §8.1.2 says "IANA registered"
   where §8.1.1, §8.1.3, §8.1.4, §8.1.5 and §8.1.6 all say "IANA has
   registered". §8.1.6's lead-in says "the following **entry**" (singular) and
   then "The following completed **registrations**" (plural) over two templates;
   §8.1.3's lead-in is plural in both places for its two. Editorial only; no code
   point is affected.
9. **The `pub` thumbprint bullet omits a field.** In §6 (line 253) `pub` reads
   `(label: -1, value: bstr)` where `kty` and `alg` (lines 249, 251) both carry
   a `data type:` field. Reported because §6 is the dispositive text for RFC
   9679's AKP case and this is the one bullet in it that is not fully specified
   in the same form as its siblings.
10. **Figure 2's comment column is misaligned** — line 147 reads `/ pub  / -1:`
    with two spaces inside the comment where lines 144-146 use the `/ kid /   2:`
    style. Cosmetic; recorded because the figure is reproduced byte-exactly
    above.
11. **Appendix A's six figure captions use underscores, and three strings cover
    six figures.** Figures 3-8 are captioned `ML_DSA_44`, `ML_DSA_65`,
    `ML_DSA_87`, `ML_DSA_44`, `ML_DSA_65`, `ML_DSA_87` (lines 823, 1091, 1450,
    1786, 2248, 2872) where every other mention in the document, Figures 1 and
    2 included, writes `ML-DSA-44` with hyphens. The JOSE figure (3) and the
    COSE figure (6) therefore carry **the same caption**, as do 4 and 7 and 5
    and 8: nothing in a caption says which serialisation its figure is. A
    fixture generator keying on captions would collide; the fixtures must be
    keyed on `A.1`/`A.2` plus the figure number.


## What was dropped, and why

Dropped as front- and back-matter boilerplate carrying no normative content:

- Status of This Memo (lines 22-34) and Copyright Notice (lines 36-49).
- Table of Contents (lines 51-80).
- §9 References (lines 555-622). Facts from it are used above and cited there
  rather than reproduced: RFC 9881 is **informative** (§9.2, lines 617-622,
  October 2025); RFC 9679 (December 2024), RFC 7638 (September 2015), RFC 7515,
  RFC 7517 and RFC 7518 (all May 2015), RFC 9052, RFC 9053 and RFC 9054 (all
  August 2022) and FIPS-204 (August 2024) are **normative** (§9.1).
- Acknowledgments (lines 2874-2878), Contributors (lines 2880-2895) and Authors'
  Addresses (lines 2897-2906).
- Appendix A, Examples (lines 624-2873) — six complete figures, three JOSE and
  three COSE, which belong to this record's `examples/` artifact. Nothing in
  Appendix A is prose: in all 2250 of those lines the only lines that are not
  example data are the heading `Appendix A.  Examples` (624), the two
  sub-headings `A.1.  JOSE` (626) and `A.2.  COSE` (1452), and the six
  `Figure N: ML_DSA_nn` captions (823, 1091, 1450, 1786, 2248, 2872). §3's two
  figures are reproduced above because they are §3's own content and the
  in-text witnesses for `kty` 7 and `alg` -48.

Nothing was marked for removal before publication: this is a published Standards
Track RFC with no RFC-Editor notes or placeholders.

**Kept although the template says to drop motivation.** Two §4 sentences that are
pure rationale are kept because in a document with nine BCP 14 keywords the
reasoned sentences are where the force lives, and both are cited by
`requirements.yaml`: "The seed format was chosen to provide a single, compact
representation..." (the stated reason for seed-only) and "This specification
intentionally does not define a means of utilizing the expanded private key
representation..." (the stated negative scope).
