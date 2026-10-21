---
record: rfc-9360
kind: normative
title: "rfc-9360 — normative statements"
extracted: "2026-10-20"
reviewed_by: ""
---

# RFC 9360 — normative text, verbatim

**What this file is.** Every normative statement of RFC 9360, reproduced as an
exact run of source lines with its line range and its own `sha256`, in the
document's own section order. Nothing here is paraphrased and nothing is
retyped: each fenced block was lifted from `.cache/rfc-9360.txt` by line range
by script. Prose outside the fences is this extraction's, and says only where a
statement sits and what it is.

| | |
|---|---|
| **Source** | `.cache/rfc-9360.txt`, 615 newline-delimited lines |
| **Digest** | `3dbe546adf08e309b429c8e71b2ee8384292fb8767338d3eb17d1c4e5adefc23` |
| **BCP 14 keywords** | **14** — 10 MUST, 3 MUST NOT, 1 SHOULD; `bin/bcp14-count`, boilerplate excluded |
| **Examples in the source** | **none** — `Figure`, `Appendix` and `vector` occur zero times |

**Region convention.** Each digest is the sha256 of the region's lines joined
by `\n` with no trailing newline — the convention established by earlier passes
in this effort.

**There is no page decoration in this source and no region is split.** This
rendering has **0 form feeds** and no running headers or footers in its 615
lines, checked with the same footer and header patterns that match 25 page
breaks in RFC 8392. So every section below is one contiguous region and
**nothing is welded across a gap**, because there are no gaps. Note for any
later pass: this file was built with `split("\n")`, never `splitlines()`.

**Where a line break falls inside a sentence**, the sentence is quoted as the
whole fenced region rather than reflowed, so the break is visible. The source
wraps `DER-encoded` across lines 222–223 as `DER-` + `encoded`;
`requirements.yaml` carries that text whitespace-normalised as
`DER- encoded certificate`, **and the hyphenation is not healed in either
file**.

**What the shape of this document is.** Four header parameters, three
algorithm-scoped siblings, two lines of CDDL, one media type and a security
section of nine paragraphs. Ten of its fourteen keywords are MUSTs, and **four
of those ten are one sentence restated once per carrying parameter**. Its
strongest prohibition — the one every other obligation depends on — is lower
case (§2, lines 134–137).

---

## §1 — Introduction

The reversal the document embodies, in its own words. The COSE WG decided
against certificates while writing RFC 8152 and RFC 9052; this paragraph is
the record of that decision being withdrawn.

```
   In the process of writing [RFC8152] and [RFC9052], the CBOR Object
   Signing and Encryption (COSE) Working Group discussed X.509
   certificates [RFC5280] and decided that no use cases were presented
   that showed a need to support certificates.  Since that time, a
   number of cases have been defined in which X.509 certificate support
   is necessary, and by implication, applications will need a documented
   and consistent way to handle such certificates.  This document
   defines a set of attributes that will allow applications to transport
   and refer to X.509 certificates in a consistent manner.
```

*Source `.cache/rfc-9360.txt` lines 72-80 · `sha256:03bb92bb1f2d82724af76069e4eeb3679795355618eff1a9d86874cb96097df7`*


The two cited use cases, both Internet-Drafts at publication:
`[Constrained-BRSKI]` and `[EDHOC]`.

```
   In some of these cases, a constrained device is being deployed in the
   context of an existing X.509 PKI: for example, [Constrained-BRSKI]
   describes a device enrollment solution that relies on the presence of
   a factory-installed certificate on the device.  [EDHOC] was also
   written with the idea that long-term certificates could be used to
   provide for authentication of devices and establish session keys.
   Another possible scenario is the use of COSE as the basis for a
   secure messaging application.  This scenario assumes the presence of
   long-term keys and a central authentication authority.  Basing such
   an application on public key certificates allows it to make use of
   well-established key management disciplines.
```

*Source `.cache/rfc-9360.txt` lines 82-92 · `sha256:b72efc985e663f5d4507882e9af479d0d75cadc8d406a8753793a26d2bbf815d`*


## §1.1 — Requirements Terminology

Quoted here and **deliberately never quoted in `requirements.yaml`**: it
recites all eleven keywords and constrains nothing. `bin/validate` recounts
the requirement texts with boilerplate stripping **off**, so an entry carrying
this paragraph would add eleven phantom keywords and break the
reconciliation. Note the words it recites that the document then never uses:
`REQUIRED`, `SHALL`, `SHALL NOT`, `SHOULD NOT`, `RECOMMENDED`,
`NOT RECOMMENDED`, `MAY` and `OPTIONAL` — eight of the eleven.

```
   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in
   BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.
```

*Source `.cache/rfc-9360.txt` lines 96-100 · `sha256:bacf9d543839982621d89929fa0d1176ac5a43937460748c5fbab2c8c6f918eb`*


## §2 — X.509 COSE Header Parameters

**What carriage buys, and what COSE lacks.** The operational case for
certificates, stated operationally rather than architecturally.

```
   The use of X.509 certificates allows for an existing trust
   infrastructure to be used with COSE.  This includes the full suite of
   enrollment protocols, trust anchors, trust chaining, and revocation
   checking that have been defined over time by the IETF and other
   organizations.  The Concise Binary Object Representation (CBOR) key
   structures [RFC8949] that have been defined in COSE currently do not
   support all of these properties, although some may be found in CBOR
   Web Tokens (CWTs) [RFC8392].
```

*Source `.cache/rfc-9360.txt` lines 104-111 · `sha256:0bc06108006e6a6414d1a8838ca7901a1f6edf4d2f190213f2371ec43216ebb9`*


**The deployment the document contemplates, and the one that matters for
`DEC-003`:** a constrained device that holds *the hash of a certificate* and
is configured to use a public key for that thumbprint, *without having the
certificate*. Also the sentence that assigns revocation to nobody.

```
   It is not necessarily expected that constrained devices themselves
   will evaluate and process X.509 certificates: it is perfectly
   reasonable for a constrained device to be provisioned with a
   certificate that it subsequently provides to a relying party -- along
   with a signature or encrypted message -- on the assumption that the
   relying party is not a constrained device and is capable of
   performing the required certificate evaluation and processing.  It is
   also reasonable that a constrained device would have the hash of a
   certificate associated with a public key and be configured to use a
   public key for that thumbprint, but without performing the
   certificate evaluation or even having the entire certificate.  In any
   case, there still needs to be an entity that is responsible for
   handling the possible certificate revocation.
```

*Source `.cache/rfc-9360.txt` lines 113-125 · `sha256:ecc9a55877121c66452c54cdd8bdc4b429e7ae0dce44895704b47fbb4ccd5d02`*


**The validation obligation, and the document's strongest prohibition — which
is lower case.** "the public key contained in the certificate cannot be used
for cryptographic operations" is the sentence the whole document rests on, and
under §1.1 it binds nobody.

```
   Parties that intend to rely on the assertions made by a certificate
   obtained from any of these methods still need to validate it.  This
   validation can be done according to the PKIX rules specified in
   [RFC5280] or by using a different trust structure, such as a trusted
   certificate distributor for self-signed certificates.  The PKIX
   validation includes matching against the trust anchors configured for
   the application.  These rules apply when the validation succeeds in a
   single step as well as when certificate chains need to be built.  If
   the application cannot establish trust in the certificate, the public
   key contained in the certificate cannot be used for cryptographic
   operations.
```

*Source `.cache/rfc-9360.txt` lines 127-137 · `sha256:8a3bafc0df3ce4bcea67b07d2a4c81596125b2d37e7fbbb66f46918a17cd9d0f`*


The lead-in to the four parameter definitions.

```
   The header parameters defined in this document are as follows:
```

*Source `.cache/rfc-9360.txt` lines 139-139 · `sha256:84acbca6d4be08c80895ff9125b87f7dc7e9e39818645975559b7f4e460ae04b`*


### §2 — `x5bag` (label 32)

Two of the fourteen keywords are here (lines 154 and 156), plus the first of
four occurrences of "The end-entity certificate MUST be integrity protected by
COSE" (line 163). Note the four properties that between them make the
work unbounded: unordered, possibly duplicated, possibly extraneous, possibly
incomplete — with path building left to "the party evaluating the signature".

```
   x5bag:  This header parameter contains a bag of X.509 certificates.
      The set of certificates in this header parameter is unordered and
      may contain self-signed certificates.  Note that there could be
      duplicate certificates.  The certificate bag can contain
      certificates that are completely extraneous to the message.  (An
      example of this would be where a signed message is being used to
      transport a certificate containing a key agreement key.)  As the
      certificates are unordered, the party evaluating the signature
      will need to be capable of building the certificate path as
      necessary.  That party will also have to take into account that
      the bag may not contain the full set of certificates needed to
      build any particular chain.

      The trust mechanism MUST process any certificates in this
      parameter as untrusted input.  The presence of a self-signed
      certificate in the parameter MUST NOT cause the update of the set
      of trust anchors without some out-of-band confirmation.  As the
      contents of this header parameter are untrusted input, the header
      parameter can be in either the protected or unprotected header
      bucket.  Sending the header parameter in the unprotected header
      bucket allows an intermediary to remove or add certificates.

      The end-entity certificate MUST be integrity protected by COSE.
      This can, for example, be done by sending the header parameter in
      the protected header, sending an 'x5bag' in the unprotected header
      combined with an 'x5t' in the protected header, or including the
      end-entity certificate in the external_aad.

      This header parameter allows for a single X.509 certificate or a
      bag of X.509 certificates to be carried in the message.

      *  If a single certificate is conveyed, it is placed in a CBOR
         byte string.

      *  If multiple certificates are conveyed, a CBOR array of byte
         strings is used, with each certificate being in its own byte
         string.
```

*Source `.cache/rfc-9360.txt` lines 141-177 · `sha256:4cf1c56f928444d19b663a433b335582b6e7e673b104eb88de8e04c39c88b6b2`*


### §2 — `x5chain` (label 33)

Two more keywords (lines 189 and 191) and the second occurrence of the
integrity-protection MUST (line 198). **Lines 198–202 are the configuration
this whole record turns on:** `x5chain` in the unprotected header combined
with `x5t` in the protected header — where lines 195–196 have just said the
unprotected bucket "allows an intermediary to remove or add certificates".

```
   x5chain:  This header parameter contains an ordered array of X.509
      certificates.  The certificates are to be ordered starting with
      the certificate containing the end-entity key followed by the
      certificate that signed it, and so on.  There is no requirement
      for the entire chain to be present in the element if there is
      reason to believe that the relying party already has, or can
      locate, the missing certificates.  This means that the relying
      party is still required to do path building but that a candidate
      path is proposed in this header parameter.

      The trust mechanism MUST process any certificates in this
      parameter as untrusted input.  The presence of a self-signed
      certificate in the parameter MUST NOT cause the update of the set
      of trust anchors without some out-of-band confirmation.  As the
      contents of this header parameter are untrusted input, the header
      parameter can be in either the protected or unprotected header
      bucket.  Sending the header parameter in the unprotected header
      bucket allows an intermediary to remove or add certificates.

      The end-entity certificate MUST be integrity protected by COSE.
      This can, for example, be done by sending the header parameter in
      the protected header, sending an 'x5chain' in the unprotected
      header combined with an 'x5t' in the protected header, or
      including the end-entity certificate in the external_aad.

      This header parameter allows for a single X.509 certificate or a
      chain of X.509 certificates to be carried in the message.

      *  If a single certificate is conveyed, it is placed in a CBOR
         byte string.

      *  If multiple certificates are conveyed, a CBOR array of byte
         strings is used, with each certificate being in its own byte
         string.
```

*Source `.cache/rfc-9360.txt` lines 179-212 · `sha256:311a4253eedeb1fc167bbe263622e19efab014a7e74fdc4d78dffbe54057f41d`*


### §2 — `x5t` (label 34)

**The registry join, the `DEC-003` answer and the premise §5 later reuses, all
in one definition.** Line 220 names the "COSE Algorithms" registry and gives
the IANA URL; it cites **no document**, and `rfc-9054` — which populates that
registry with the eight hash identifiers — is cited **zero times** in all 614
lines of RFC 9360. Lines 221–223 put the hash over the **DER-encoded
certificate**, not over the key. Lines 225–227 assert that the parameter "does
not provide any trust"; lines 234–236 then say it provides "integrity
protection of the end-entity certificate". Line 239 is the only
mandatory-to-implement algorithm floor in either document of this lane.

```
   x5t:  This header parameter identifies the end-entity X.509
      certificate by a hash value (a thumbprint).  The 'x5t' header
      parameter is represented as an array of two elements.  The first
      element is an algorithm identifier that is an integer or a string
      containing the hash algorithm identifier corresponding to the
      Value column (integer or text string) of the algorithm registered
      in the "COSE Algorithms" registry (see
      <https://www.iana.org/assignments/cose/>).  The second element is
      a binary string containing the hash value computed over the DER-
      encoded certificate.

      As this header parameter does not provide any trust, the header
      parameter can be in either a protected or unprotected header
      bucket.

      The identification of the end-entity certificate MUST be integrity
      protected by COSE.  This can be done by sending the header
      parameter in the protected header or including the end-entity
      certificate in the external_aad.

      The 'x5t' header parameter can be used alone or together with the
      'x5bag', 'x5chain', or 'x5u' header parameters to provide
      integrity protection of the end-entity certificate.

      For interoperability, applications that use this header parameter
      MUST support the hash algorithm 'SHA-256' but can use other hash
      algorithms.  This requirement allows for different implementations
      to be configured to use an interoperable algorithm, but does not
      preclude the use (by prior agreement) of other algorithms.
```

*Source `.cache/rfc-9360.txt` lines 214-242 · `sha256:b4d8656f1c1d1ae5ad8b204ff5cf14f49c57cc5fa4be1f5bd8d4a2179fa5f513`*


### §2 — `x5u` (label 35)

Two keywords (lines 270 and 277) and the third occurrence of the
integrity-protection MUST (line 261). Lines 256–258 define
`application/cose-x509` as **a CBOR sequence**, a construct `rfc-8742`
defines and which this document cites zero times. Lines 264–267 say the URI
"does not need to provide any protection"; lines 269–274 then require URI
integrity protection and server authentication before a retrieved certificate
may be trusted.

```
   x5u:  This header parameter provides the ability to identify an X.509
      certificate by a URI [RFC3986].  It contains a CBOR text string.
      The referenced resource can be any of the following media types:

      *  application/pkix-cert [RFC2585]

      *  application/pkcs7-mime; smime-type="certs-only" [RFC8551]

      *  application/cose-x509 (Section 4.3)

      *  application/cose-x509; usage=chain (Section 4.3)

      When the application/cose-x509 media type is used, the data is a
      CBOR sequence of single-entry COSE_X509 structures (encoding
      "bstr").  If the parameter "usage" is set to "chain", this
      sequence indicates a certificate chain.

      The end-entity certificate MUST be integrity protected by COSE.
      This can, for example, be done by sending the 'x5u' in the
      unprotected or protected header combined with an 'x5t' in the
      protected header, or including the end-entity certificate in the
      external_aad.  As the end-entity certificate is integrity
      protected by COSE, the URI does not need to provide any
      protection.

      If a retrieved certificate does not chain to an existing trust
      anchor, that certificate MUST NOT be trusted unless the URI
      provides integrity protection and server authentication and the
      server is configured as trusted to provide new trust anchors or if
      an out-of-band confirmation can be received for trusting the
      retrieved certificate.  If an HTTP or Constrained Application
      Protocol (CoAP) GET request is used to retrieve a certificate, TLS
      [RFC8446], DTLS [RFC9147], or Object Security for Constrained
      RESTful Environments (OSCORE) [RFC8613] SHOULD be used.
```

*Source `.cache/rfc-9360.txt` lines 244-277 · `sha256:651fba24a0939ff40d2b7b2be9717cd60e492ab337059cbb01fa1fab637840c5`*


### §2 — where the parameters are used

**Two locations and no more.** `COSE_Encrypt`, `COSE_Mac` and `COSE_Mac0` are
not named anywhere in the document.

```
   The header parameters are used in the following locations:

   COSE_Signature and COSE_Sign1 objects:  In these objects, the
      parameters identify the certificate to be used for validating the
      signature.

   COSE_recipient objects:  In this location, the parameters identify
      the certificate for the recipient of the message.
```

*Source `.cache/rfc-9360.txt` lines 279-286 · `sha256:47dbb100737cfd03cd5ebd97f63c082565299ed3039672109efcf7f42441d919`*


### §2 — Table 1: the label assignments

The whole of the label assignment. Every one of these four labels is a
**two-octet** CBOR integer (0x1820–0x1823) — measured in
`examples/vectors.yaml`.

```
   The labels assigned to each header parameter can be found in Table 1.

         +=========+=======+===============+=====================+
         | Name    | Label | Value Type    | Description         |
         +=========+=======+===============+=====================+
         | x5bag   | 32    | COSE_X509     | An unordered bag of |
         |         |       |               | X.509 certificates  |
         +---------+-------+---------------+---------------------+
         | x5chain | 33    | COSE_X509     | An ordered chain of |
         |         |       |               | X.509 certificates  |
         +---------+-------+---------------+---------------------+
         | x5t     | 34    | COSE_CertHash | Hash of an X.509    |
         |         |       |               | certificate         |
         +---------+-------+---------------+---------------------+
         | x5u     | 35    | uri           | URI pointing to an  |
         |         |       |               | X.509 certificate   |
         +---------+-------+---------------+---------------------+

                   Table 1: X.509 COSE Header Parameters
```

*Source `.cache/rfc-9360.txt` lines 288-306 · `sha256:41ddd08c32e6b58df431e88fe505e60316a50631908fde4cecace7601a6bf42d`*


### §2 — the CDDL, and the sentence under it

**The entire wire format is these two lines**, and line 314 is the `DEC-002`
cut in one sentence. The `2*` makes a one-element array invalid: one
certificate has exactly one encoding. `COSE_CertHash` has **exactly two
fields**, so there is nowhere to carry the *purpose* of the hash — which is
why `rfc-9054`'s "Filter Only" cannot be read off the wire. Both rules were
checked against RFC 8610 Appendix B's grammar for this pass; see
`schema/README.md`.

```
   Below is an equivalent Concise Data Definition Language (CDDL)
   description (see [RFC8610]) of the text above.

   COSE_X509 = bstr / [ 2*certs: bstr ]
   COSE_CertHash = [ hashAlg: (int / tstr), hashValue: bstr ]

   The contents of "bstr" are the bytes of a DER-encoded certificate.
```

*Source `.cache/rfc-9360.txt` lines 308-314 · `sha256:8decd96ed30da85f33c629f40872ed4bbaf26d15570bb16be2ffef4700278cc3`*


## §3 — X.509 Certificates and Static-Static ECDH

**Three sender parameters, not four**, and the stated reason: a bag would be
the same attribute for both sides.

```
   The header parameters defined in the previous section are used to
   identify the recipient certificates for the Elliptic Curve Diffie-
   Hellman (ECDH) key agreement algorithms.  In this section, we define
   the algorithm-specific parameters that are used for identifying or
   transporting the sender's key for static-static key agreement
   algorithms.

   These attributes are defined analogously to those in the previous
   section.  There is no definition for the certificate bag, as the same
   attribute would be used for both the sender and recipient
   certificates.
```

*Source `.cache/rfc-9360.txt` lines 318-328 · `sha256:43ac0963aee6ab8f209e7c2c34635260e5fe08a3381ab145482784d9bb462034`*


Each defined entirely by reference to its §2 sibling. `x5u-sender` is the only
one whose *processing* is also inherited.

```
   x5chain-sender:
      This header parameter contains the chain of certificates starting
      with the sender's key exchange certificate.  The structure is the
      same as 'x5chain'.

   x5t-sender:
      This header parameter contains the hash value for the sender's key
      exchange certificate.  The structure is the same as 'x5t'.

   x5u-sender:
      This header parameter contains a URI for the sender's key exchange
      certificate.  The structure and processing are the same as 'x5u'.
```

*Source `.cache/rfc-9360.txt` lines 330-341 · `sha256:a76f8275bd04f4bf5467bfed1640f36cf8ff657d21c7470ebaa67f49eed78676`*


### §3 — Table 2: the algorithm-scoped assignments

**The label is scoped by the algorithm.** `-27` means `x5t-sender` only under
the five ECDH-SS algorithms named in the row; the same integer is free
elsewhere in the COSE Header Algorithm Parameters registry. This is IANA's own
answer to label scoping — the *(algorithm, label)* pair — and the nearest
ratified relative of `R-M-12`'s *(key, local label)*.

```
   +==============+=====+=============+===================+===========+
   |Name          |Label|Type         | Algorithm         |Description|
   +==============+=====+=============+===================+===========+
   |x5t-sender    |-27  |COSE_CertHash| ECDH-SS+HKDF-256, |Thumbprint |
   |              |     |             | ECDH-SS+HKDF-512, |for the    |
   |              |     |             | ECDH-SS+A128KW,   |sender's   |
   |              |     |             | ECDH-SS+A192KW,   |X.509      |
   |              |     |             | ECDH-SS+A256KW    |certificate|
   +--------------+-----+-------------+-------------------+-----------+
   |x5u-sender    |-28  |uri          | ECDH-SS+HKDF-256, |URI for the|
   |              |     |             | ECDH-SS+HKDF-512, |sender's   |
   |              |     |             | ECDH-SS+A128KW,   |X.509      |
   |              |     |             | ECDH-SS+A192KW,   |certificate|
   |              |     |             | ECDH-SS+A256KW    |           |
   +--------------+-----+-------------+-------------------+-----------+
   |x5chain-sender|-29  |COSE_X509    | ECDH-SS+HKDF-256, |static key |
   |              |     |             | ECDH-SS+HKDF-512, |X.509      |
   |              |     |             | ECDH-SS+A128KW,   |certificate|
   |              |     |             | ECDH-SS+A192KW,   |chain      |
   |              |     |             | ECDH-SS+A256KW    |           |
   +--------------+-----+-------------+-------------------+-----------+

                  Table 2: Static ECDH Algorithm Values
```

*Source `.cache/rfc-9360.txt` lines 343-365 · `sha256:84a23d6c12a3d1b2592b4bf752f99a47c2e1cc0147b8f5cbff51c82df15c1d2a`*


## §4.1 — COSE Header Parameters Registry

```
   IANA has registered the new COSE Header parameters in Table 1 in the
   "COSE Header Parameters" registry.  The "Value Registry" field is
   empty for all of the items.  For each item, the "Reference" field
   points to this document.
```

*Source `.cache/rfc-9360.txt` lines 371-374 · `sha256:0276ec9d9ce24e6b99a3cde344f9575c2287c49b8833baeedaac9f1536708e60`*


## §4.2 — COSE Header Algorithm Parameters Registry

**A different registry from §4.1's**, and that difference is the whole
mechanism of the scoping above.

```
   IANA has registered the new COSE Header Algorithm parameters in
   Table 2 in the "COSE Header Algorithm Parameters" registry.  For each
   item, the "Reference" field points to this document.
```

*Source `.cache/rfc-9360.txt` lines 378-380 · `sha256:9603f6c596b3ffdd550e14e8b2a411ef7ede0b8ad47fec6e409e661f408645ad`*


## §4.3 — Media type `application/cose-x509`

The complete registration template. Note what is absent: **no magic number,
no file extension**, so a CBOR sequence of byte strings carrying DER is not
self-identifying on disk or in a store. The `usage` parameter has exactly two
states and no declared default beyond "no further information".

```
   When the application/cose-x509 media type is used, the data is a CBOR
   sequence of single-entry COSE_X509 structures (encoding "bstr").  If
   the parameter "usage" is set to "chain", this sequence indicates a
   certificate chain.

   IANA has registered the following media type [RFC6838]:

   Type name:  application

   Subtype name:  cose-x509

   Required parameters:  N/A

   Optional parameters:  usage

      *  Can be absent to provide no further information about the
         intended meaning of the order in the CBOR sequence of
         certificates.

      *  Can be set to "chain" to indicate that the sequence of data
         items is to be interpreted as a certificate chain.

   Encoding considerations:  binary

   Security considerations:  See the Security Considerations section of
      RFC 9360.

   Interoperability considerations:  N/A

   Published specification:  RFC 9360

   Applications that use this media type:  Applications that employ COSE
      and use X.509 as a certificate type.

   Fragment identifier considerations:  N/A

   Additional information:

      Deprecated alias names for this type:  N/A
      Magic number(s):  N/A
      File extension(s):  N/A
      Macintosh file type code(s):  N/A

   Person & email address to contact for further information:
      iesg@ietf.org

   Intended usage:  COMMON

   Restrictions on usage:  N/A

   Author:  COSE WG

   Change controller:  IESG
```

*Source `.cache/rfc-9360.txt` lines 384-436 · `sha256:7beac84a26743fbb34d5d7bc4074d35bf15e314a679cb94d47927d92f79f24fe`*


## §5 — Security Considerations

**Nine paragraphs, quoted one per region so their order is on the record.**
The ordering matters: the claim about `x5t`'s hash algorithm is the **ninth
and last**, the identity-misbinding attack is the **third**, and the paragraph
immediately before the ninth says the opposite of it. See `design-notes.md`
§10.

### Paragraph 1 of 9 — trust anchors

```
   Establishing trust in a certificate is a vital part of processing.  A
   major component of establishing trust is determining what the set of
   trust anchors are for the process.  A new self-signed certificate
   appearing on the client cannot be a trigger to modify the set of
   trust anchors, because a well-defined trust-establishment process is
   required.  One common way for a new trust anchor to be added to (or
   removed from) a device is by doing a new firmware upgrade.
```

*Source `.cache/rfc-9360.txt` lines 440-446 · `sha256:7353e88c51707f9fb20bc20ffe9725813ae95537b0830c9f9a9c61da83f753c8`*


### Paragraph 2 of 9 — the ordering trade-off, and the join

Keyword 12 of 14 (line 458). The two preceding sentences argue **both** orders
and the document picks neither; what it requires is only that both checks
complete.

```
   In constrained systems, there is a trade-off between the order of
   checking the signature and checking the certificate for validity.
   Validating certificates can require that network resources be
   accessed in order to get revocation information or retrieve
   certificates during path building.  The resulting network access can
   consume power and network bandwidth.  On the other hand, if the
   certificates are validated after the signature is validated, an
   oracle can potentially be built based on detecting the network
   resources, which is only done if the signature validation passes.  In
   any event, both the signature validation and the certificate
   validation MUST be completed successfully before acting on any
   requests.
```

*Source `.cache/rfc-9360.txt` lines 448-459 · `sha256:3e148fc21b58b0861fb771a2ec9862a726b371d81c04ee98a51ea73c65bb8e31`*


### Paragraph 3 of 9 — proof of possession and identity misbinding

Keyword 13 of 14 (line 463), and the fourth occurrence of the
integrity-protection obligation — this one with an "Unless it is known that"
escape that depends on a CA practice statement the message does not carry.
**The attack described here is the RFC's own argument for `ARCH-0002` P1:** it
exists only because the name and the key are separable.

```
   Unless it is known that the Certificate Authority (CA) required proof
   of possession of the subject's private key to issue an end-entity
   certificate, the end-entity certificate MUST be integrity protected
   by COSE.  Without proof of possession, an attacker can trick the CA
   into issuing an identity-misbinding certificate with someone else's
   "borrowed" public key but with a different subject.  An on-path
   attacker can then perform an identity-misbinding attack by replacing
   the real end-entity certificate in COSE with such an identity-
   misbinding certificate.
```

*Source `.cache/rfc-9360.txt` lines 461-469 · `sha256:579c8b6d05aedee71929807fce4d3736fce973398eae069e889f15f2cc23674c`*


### Paragraph 4 of 9 — identity exposure and permanent identifiers

The document's only statement of what `x5t` *is* beyond a selector: an
alternative **permanent identifier**.

```
   End-entity X.509 certificates contain identities that a passive on-
   path attacker eavesdropping on the conversation can use to identify
   and track the subject.  COSE does not provide identity protection by
   itself, and the 'x5t' and 'x5u' header parameters are just
   alternative permanent identifiers and can also be used to track the
   subject.  To provide identity protection, COSE can be sent inside
   another security protocol providing confidentiality.
```

*Source `.cache/rfc-9360.txt` lines 471-477 · `sha256:71bccf0f16987c892db5f0513fbfdabff90e89da33c58ab911a21984483e104c`*


### Paragraph 5 of 9 — checking the key against the algorithm

Keyword 14 of 14 (line 479).

```
   Before using the key in a certificate, the key MUST be checked
   against the algorithm to be used, and any algorithm-specific checks
   need to be made.  These checks can include validating that points are
   on curves for elliptical curve algorithms and that the sizes of RSA
   keys are within an acceptable range.  The use of unvalidated keys can
   lead to either loss of security or excessive consumption of resources
   (for example, using a 200K RSA key).
```

*Source `.cache/rfc-9360.txt` lines 479-485 · `sha256:cc1d502812817d014b67a34cfe191e30534a8c0743650b6eec8f5b18a6759268`*


### Paragraph 6 of 9 — `x5u` and RFC 3986

```
   When processing the 'x5u' header parameter, the security
   considerations of [RFC3986], and specifically those defined in
   Section 7.1 of [RFC3986], also apply.
```

*Source `.cache/rfc-9360.txt` lines 487-489 · `sha256:ac89fe5484169729c017ccd5320fc8851bf4dc711f002353a34494089dfcfe49`*


### Paragraph 7 of 9 — certification path validation

```
   Regardless of the source, certification path validation is an
   important part of establishing trust in a certificate.  Section 6 of
   [RFC5280] provides guidance for the path validation.  The security
   considerations of [RFC5280] are also important for the correct usage
   of this document.
```

*Source `.cache/rfc-9360.txt` lines 491-495 · `sha256:b540d4dd06cd19116da7d9e7f873916aba3c89d3ddbca3243e74d0d4bc00683d`*


### Paragraph 8 of 9 — the protected bucket mitigates a misbehaving CA

**Read this one immediately before the next.** It says that protecting the
integrity of `x5bag`, `x5chain` **and `x5t`** by placing them in the protected
bucket "can help mitigate some risks of a misbehaving CA".

```
   Protecting the integrity of the 'x5bag', 'x5chain', and 'x5t'
   contents by placing them in the protected header bucket can help
   mitigate some risks of a misbehaving CA (cf. Section 5.1 of
   [RFC2634]).
```

*Source `.cache/rfc-9360.txt` lines 497-500 · `sha256:a9cd5f5148feb7319774eef1e1aa887c91231cc7ff65b282ad7908e29952dc3d`*


### Paragraph 9 of 9 — the claim that the `x5t` algorithm does not matter

**The contradiction this record exists to record, and it is adjacent.** Its
premise — that the parameter "selects which certificate that is already
present on the system" — is false in the configuration §2 recommends at lines
198–202, where the certificate arrives in an unprotected bucket an
intermediary may rewrite and the protected `x5t` is the only binding.

```
   The security of the algorithm used for 'x5t' does not affect the
   security of the system, as this header parameter selects which
   certificate that is already present on the system should be used, but
   it does not provide any trust.
```

*Source `.cache/rfc-9360.txt` lines 502-505 · `sha256:ca8deb7db54bb8c5031b6b6002cd7e13761797768b30896059ced97643c18a98`*


---

## What is deliberately not in this file

- **§6's references** (lines 507–602). Bibliography, not normative text. The
  one fact worth recording from them is an absence: the normative list is
  RFC 2119, RFC 5280, RFC 8152, RFC 8174, RFC 8949 and RFC 9052, and the
  informative list adds twelve more. **`rfc-9054` is in neither**, although §2
  selects `x5t`'s `hashAlg` from the registry `rfc-9054` populates. Measured:
  the string `9054` occurs zero times in the source.
- **The Acknowledgements and Author's Address** (lines 604–614). Recorded in
  `summary.md`: Jim Schaad died on 3 October 2020 and Ivaylo Petrov saw the
  document through publication.
- **The front matter** (lines 1–68): masthead, Abstract, Status of This Memo,
  Copyright Notice and Table of Contents. "Category: Standards Track" (line 7)
  and "This is an Internet Standards Track document" (line 26) are quoted in
  `summary.md`'s metadata table.
- **Nothing else.** Every line of §1 through §5 that carries an obligation, a
  type, a label, a registry action or a security claim is above.
