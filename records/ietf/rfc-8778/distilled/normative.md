---
record: rfc-8778
kind: normative
title: "rfc-8778 — normative statements"
extracted: "2026-10-20"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 8778, "Use of the HSS/LMS Hash-Based Signature Algorithm with CBOR
Object Signing and Encryption (COSE)", Standards Track, April 2020 (R. Housley,
Vigil Security; ISSN 2070-1721). Quotations are verbatim from the plain-text RFC
at `content.sha256` `2d43646b974c76b9e13565af9b96432ac2b7ba39b66a61820d97f94f3cf1c398`.
Prose sentences are quoted with whitespace normalised (the RFC's line wrap and
double sentence spacing become single spaces). Every **fenced** block is an
exact consecutive run of source lines, reproduced with the RFC's three-space
left margin and its own blank lines, and carries its line range and the sha256
of that run — the region's lines joined by `\n` with no trailing newline.

**Line-break severances — declared, never healed.** Four prose sentences contain
a token the plain-text wrap cuts in two. Each is quoted **exactly as the
normalised source renders it**, with the wrap space left in place, so nothing is
healed and nothing is truncated:

| source lines | token severed | rendered by the wrap as | entry |
|---|---|---|---|
| 84–85 (§1) | `hash-based` | `hash-` + `based` | `R-0004` |
| 85–86 (§1) | `HSS/LMS` | `HSS/` + `LMS` | `R-0005` |
| 117–118 (§1.1) | `HSS/LMS` | `HSS/` + `LMS` | `R-0013` |
| 373–374 (§4) | `brute-force` | `brute-` + `force` | `R-0104` |

The 85–86 severance is the one that matters: it falls inside the document's
first statement of the finite signature budget, which §5 then makes terminal.

**What this document does not contain.** Measured as whole words,
case-insensitively, over all 772 lines. `protocol`, `exchange`, `verifier`,
`sender`, `recipient`, `handshake`, `negotiate` — **0 each**; `signer` 3, never
inside a flow. `lifecycle`, `revoke`, `rotate`, `expire`, `exhaust` — **0 each**,
although §4 and §5 specify a lifecycle in other words. `thumbprint`, `canonical`,
`deterministic`, `COSE_Key`, `Sig_structure`, `header`, `tag` — **0 each**.
`CDDL` once (a reference title), `ABNF`, `ASN.1` and `JSON Schema` **0**: the
document ships **no formal grammar of any kind**, so every schema in this
record's `schema/` directory except `source-renderings.txt` is the library's own.
`kty` occurs **exactly once** (§3) and `pub` **exactly once** as a word (§6.3).
**No `COSE_Key` and no `pub` value is printed anywhere.** `9052` occurs 0 times
and `8152` 7: this document is written against RFC 8152, not against STD 96.


## Abstract (lines 16–20)

Carried here with **no requirement entry**: its scope sentence restates §1's,
which `R-0001` carries, and quoting both would double-count the scope.

lines 16-20  sha256:ed685f84461bce855b085b399396299a5dfffed340103c3663921d58eb065bed

```text
   This document specifies the conventions for using the Hierarchical
   Signature System (HSS) / Leighton-Micali Signature (LMS) hash-based
   signature algorithm with the CBOR Object Signing and Encryption
   (COSE) syntax.  The HSS/LMS algorithm is one form of hash-based
   digital signature; it is described in RFC 8554.
```


## §1. Introduction

- (§1) "This document specifies the conventions for using the Hierarchical Signature System (HSS) / Leighton-Micali Signature (LMS) hash-based signature algorithm with the CBOR Object Signing and Encryption (COSE) [RFC8152] syntax." — `R-0001`
- (§1) "The LMS system provides a one-time digital signature that is a variant of Merkle Tree Signatures (MTS)." — `R-0002`
- (§1) "The HSS is built on top of the LMS system to efficiently scale for a larger number of signatures." — `R-0003`
- (§1) "The HSS/LMS algorithm is one form of a hash- based digital signature, and it is described in [HASHSIG]." — `R-0004`, **severance 84–85 declared above**
- (§1) "The HSS/ LMS signature algorithm can only be used for a fixed number of signing operations." — `R-0005`, **severance 85–86**
- (§1) "The number of signing operations depends upon the size of the tree." — `R-0006`
- (§1) "The HSS/LMS signature algorithm uses small public keys, and it has low computational cost; however, the signatures are quite large." — `R-0007`
- (§1) "The HSS/LMS private key can be very small when the signer is willing to perform additional computation at signing time; alternatively, the private key can consume additional memory and provide a faster signing time." — `R-0008`
- (§1) "The HSS/LMS signatures [HASHSIG] are currently defined to use exclusively SHA-256 [SHS]." — `R-0009`

`R-0005` and `R-0007` together are the whole of this record's size story in the
document's own words, and `examples/vectors.yaml` measures both halves: a
56-octet public key against 2512 octets of signature.


## §1.2. Terminology — the BCP 14 recital (lines 126–130)

Carried here with **no requirement entry**, deliberately. It recites all eleven
keywords and constrains nothing; `bin/validate` recomputes the extracted keyword
count from the entry texts, so an entry for this paragraph would add eleven
phantom keywords and break the reconciliation.

lines 126-130  sha256:bacf9d543839982621d89929fa0d1176ac5a43937460748c5fbab2c8c6f918eb

```text
   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in
   BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.
```


## §2. LMS Digital Signature Algorithm Overview

- (§2) "This specification makes use of the hash-based signature algorithm specified in [HASHSIG], which is the Leighton and Micali adaptation [LM] of the original Lamport-Diffie-Winternitz-Merkle one-time signature system [M1979][M1987][M1989a][M1989b]." — `R-0014`
- (§2) "As implied by the name, the hash-based signature algorithm depends on a collision-resistant hash function." — `R-0018`
- (§2) "The hash-based signature algorithm specified in [HASHSIG] currently makes use of the SHA-256 one-way hash function [SHS], but it also establishes an IANA registry to permit the registration of additional one-way hash functions in the future." — `R-0019`

The three components, verbatim — `R-0015`, `R-0016`, `R-0017`. **The third bullet
is missing the space before `--`**; see *Observations on the source*.

lines 139-146  sha256:755f052711b568c33fcacb4b7de100aabd9a02c2e6c0ab7415efb6ebe6f64a2f

```text
   The hash-based signature algorithm has three major components:

   *  Hierarchical Signature System (HSS) -- see Section 2.1

   *  Leighton-Micali Signature (LMS) -- see Section 2.2

   *  Leighton-Micali One-time Signature (LM-OTS) Algorithm-- see
      Section 2.3
```


## §2.1. Hierarchical Signature System (HSS)

- (§2.1) "The hash-based signature algorithm specified in [HASHSIG] uses a hierarchy of trees." — `R-0020`
- (§2.1) "The N-time Hierarchical Signature System (HSS) allows subordinate trees to be generated when needed by the signer." — `R-0021`
- (§2.1) "Otherwise, generation of the entire tree might take weeks or longer." — `R-0022`
- (§2.1) "An HSS signature, as specified in [HASHSIG], carries the number of signed public keys (Nspk), followed by that number of signed public keys, followed by the LMS signature, as described in Section 2.2." — `R-0023`
- (§2.1) **"The public key for the topmost LMS tree is the public key of the HSS system."** — `R-0024`
- (§2.1) "The LMS private key in the parent tree signs the LMS public key in the child tree, and the LMS private key in the bottom-most tree signs the actual message." — `R-0025`
- (§2.1) "The signature over the public key and the signature over the actual message are LMS signatures, as described in Section 2.2." — `R-0026`
- (§2.1) "As defined in Section 3.3 of [HASHSIG], a signed_public_key is the lms_signature over the public key followed by the public key itself." — `R-0030`
- (§2.1) "Note that Nspk is the number of levels in the hierarchy of trees minus 1." — `R-0031`

`R-0024` is one of the two sentences this record exists for. With §2.2's layout
it is the entire specification, anywhere in COSE, of what the `pub` octets of a
`kty: 5` key are.

The stand-alone-tree rendering — `R-0027`, and `R-0028` ("where the notation
comes from [HASHSIG]"), which is as close as the document comes to defining
`u32str` or `||`:

lines 172-178  sha256:b957c65773cb28650e953be80b344c6625ecf5cc4ecf76ba261a1e7463bfad54

```text
   The elements of the HSS signature value for a stand-alone tree (a top
   tree with no children) can be summarized as:

      u32str(0) ||
      lms_signature  /* signature of message */

   where the notation comes from [HASHSIG].
```

The Nspk rendering — `R-0029`:

lines 180-194  sha256:5be7f80c9f714c72f52cab3fb777f88fec204ff2e1ff3edc640cb377a22aa0b4

```text
   The elements of the HSS signature value for a tree with Nspk signed
   public keys can be summarized as:

      u32str(Nspk) ||
      signed_public_key[0] ||
      signed_public_key[1] ||
         ...
      signed_public_key[Nspk-2] ||
      signed_public_key[Nspk-1] ||
      lms_signature  /* signature of message */

   As defined in Section 3.3 of [HASHSIG], a signed_public_key is the
   lms_signature over the public key followed by the public key itself.
   Note that Nspk is the number of levels in the hierarchy of trees
   minus 1.
```


## §2.2. Leighton-Micali Signature (LMS)

- (§2.2) "Subordinate LMS trees are placed in the HSS structure, as discussed in Section 2.1." — `R-0032`
- (§2.2) "Each tree in the hash-based signature algorithm specified in [HASHSIG] uses the Leighton-Micali Signature (LMS) system." — `R-0033`
- (§2.2) "LMS systems have two parameters." — `R-0034`
- (§2.2) "The first parameter is the height of the tree, h, which is the number of levels in the tree minus one." — `R-0035`
- (§2.2) "The [HASHSIG] includes support for five values of this parameter: h=5, h=10, h=15, h=20, and h=25." — `R-0036`
- (§2.2) "Note that there are 2^h leaves in the tree." — `R-0037`
- (§2.2) "The second parameter is the number of bytes output by the hash function, m, which is the amount of data associated with each node in the tree." — `R-0038`
- (§2.2) **"The [HASHSIG] specification supports only SHA-256 with m=32."** — `R-0039`
- (§2.2) "An IANA registry is defined so that other hash functions could be used in the future." — `R-0040`

The five tree sizes and the registry that extends them — `R-0041`…`R-0045`,
`R-0046`. **`R-0046` is load-bearing**: this is the registry that
`u32str(lms_algorithm_type)` indexes, and that field is octets 0–3 of the public
key.

lines 211-225  sha256:b9e0a5b5e8e74567272dd662fb1997e8d6488c6c67a780915aee5c8011401e06

```text
   The [HASHSIG] specification supports five tree sizes:

   *  LMS_SHA256_M32_H5

   *  LMS_SHA256_M32_H10

   *  LMS_SHA256_M32_H15

   *  LMS_SHA256_M32_H20

   *  LMS_SHA256_M32_H25

   The [HASHSIG] specification establishes an IANA registry to permit
   the registration of additional hash functions and additional tree
   sizes in the future.
```

- (§2.2) "The [HASHSIG] specification defines the value I as the private key identifier" — `R-0047`, **first clause**
- (§2.2) "the same I value is used for all computations with the same LMS tree." — `R-0048`, **second clause of the same sentence; nothing is spliced**
- (§2.2) **"The value I is also available in the public key."** — `R-0049`
- (§2.2) "In addition, the [HASHSIG] specification defines the value T[r] as the m-byte string associated with the ith node in the LMS tree" — `R-0050`, **first clause**
- (§2.2) "and the nodes are indexed from 1 to 2^(h+1)-1." — `R-0051`, **second clause**
- (§2.2) **"Thus, T[1] is the m-byte string associated with the root of the LMS tree."** — `R-0052`
- (§2.2) **"The LMS public key can be summarized as: u32str(lms_algorithm_type) || u32str(otstype) || I || T[1]"** — `R-0053`

`R-0053` is **the** statement of this record. The whole paragraph and the
rendering, byte-exact:

lines 227-237  sha256:da71ebd8973a3908c49bbe4317c8a7f8d27954fa1939d0cbb898d773097ee06c

```text
   The [HASHSIG] specification defines the value I as the private key
   identifier, and the same I value is used for all computations with
   the same LMS tree.  The value I is also available in the public key.
   In addition, the [HASHSIG] specification defines the value T[r] as
   the m-byte string associated with the ith node in the LMS tree, and
   the nodes are indexed from 1 to 2^(h+1)-1.  Thus, T[1] is the m-byte
   string associated with the root of the LMS tree.

   The LMS public key can be summarized as:

      u32str(lms_algorithm_type) || u32str(otstype) || I || T[1]
```

The four elements of an LMS signature — `R-0054`…`R-0058`, with `R-0059`,
`R-0060` and `R-0061` on the authentication path:

lines 239-256  sha256:8b013396539f2f3ee1e487af6ebe33bd69dbc439e6f74bc97df0a2554266066d

```text
   As specified in [HASHSIG], the LMS signature consists of four
   elements:

   *  the number of the leaf associated with the LM-OTS signature,

   *  an LM-OTS signature, as described in Section 2.3,

   *  a type code indicating the particular LMS algorithm, and

   *  an array of values that is associated with the path through the
      tree from the leaf associated with the LM-OTS signature to the
      root.

   The array of values contains the siblings of the nodes on the path
   from the leaf to the root but does not contain the nodes on the path
   itself.  The array for a tree with height h will have h values.  The
   first value is the sibling of the leaf, the next value is the sibling
   of the parent of the leaf, and so on up the path to the root.
```

- (§2.2) "The array of values contains the siblings of the nodes on the path from the leaf to the root but does not contain the nodes on the path itself." — `R-0059`
- (§2.2) "The array for a tree with height h will have h values." — `R-0060`
- (§2.2) "The first value is the sibling of the leaf, the next value is the sibling of the parent of the leaf, and so on up the path to the root." — `R-0061`

`R-0061` is testable against the document's own examples and this extraction
tested it: Appendix A's two signatures are leaf 1 and leaf 0 of one tree —
siblings — so the rule predicts that their paths agree everywhere above the leaf.
They agree in `path[1..9]` and differ only in `path[0]`
(`examples/vectors.yaml` `V-0006`).

The LMS signature rendering — `R-0062`:

lines 258-263  sha256:a5133e293e146cbc83a7f2603866daff699efcc527b80c584b7eb5da75b9b2e9

```text
   The four elements of the LMS signature value can be summarized as:

      u32str(q) ||
      ots_signature ||
      u32str(type) ||
      path[0] || path[1] || ... || path[h-1]
```


## §2.3. Leighton-Micali One-Time Signature (LM-OTS) Algorithm

- (§2.3) "The hash-based signature algorithm depends on a one-time signature method." — `R-0063`
- (§2.3) "This specification makes use of the Leighton-Micali One-time Signature (LM-OTS) Algorithm [HASHSIG]." — `R-0064`
- (§2.3) "An LM-OTS has five parameters:" — `R-0065`
- (§2.3) "n: The number of bytes output by the hash function. For SHA-256 [SHS], n=32." — `R-0066`
- (§2.3) "H: A preimage-resistant hash function that accepts byte strings of any length and returns an n-byte string." — `R-0067`
- (§2.3) "w: The width in bits of the Winternitz coefficients." — `R-0068`
- (§2.3) "[HASHSIG] supports four values for this parameter: w=1, w=2, w=4, and w=8." — `R-0069`
- (§2.3) "p: The number of n-byte string elements that make up the LM-OTS signature." — `R-0070`
- (§2.3) "ls: The number of left-shift bits used in the checksum function, which is defined in Section 4.4 of [HASHSIG]." — `R-0071`
- (§2.3) "The values of p and ls are dependent on the choices of the parameters n and w, as described in Appendix B of [HASHSIG]." — `R-0072`

The five parameters as printed. **`R-0070` contradicts `R-0079` in this same
section** — see *Observations on the source*.

lines 267-289  sha256:6ef09858849d51d81a351573e7c8007ef37205e32c9a0e11df6b8b7f747aabf1

```text
   The hash-based signature algorithm depends on a one-time signature
   method.  This specification makes use of the Leighton-Micali One-time
   Signature (LM-OTS) Algorithm [HASHSIG].  An LM-OTS has five
   parameters:

   n:    The number of bytes output by the hash function.  For SHA-256
         [SHS], n=32.

   H:    A preimage-resistant hash function that accepts byte strings of
         any length and returns an n-byte string.

   w:    The width in bits of the Winternitz coefficients.  [HASHSIG]
         supports four values for this parameter: w=1, w=2, w=4, and
         w=8.

   p:    The number of n-byte string elements that make up the LM-OTS
         signature.

   ls:   The number of left-shift bits used in the checksum function,
         which is defined in Section 4.4 of [HASHSIG].

   The values of p and ls are dependent on the choices of the parameters
   n and w, as described in Appendix B of [HASHSIG].
```

The four LM-OTS variants and the registry that extends them — `R-0073`…`R-0076`,
`R-0077`. **`R-0077` is load-bearing**: this is the registry that
`u32str(otstype)` indexes, and that field is octets 4–7 of the public key.

lines 291-303  sha256:8b3a1b44e9b9c782f8a54ea406f7d4236864572e0600bd6f4506a5f10da553dc

```text
   The [HASHSIG] specification supports four LM-OTS variants:

   *  LMOTS_SHA256_N32_W1

   *  LMOTS_SHA256_N32_W2

   *  LMOTS_SHA256_N32_W4

   *  LMOTS_SHA256_N32_W8

   The [HASHSIG] specification establishes an IANA registry to permit
   the registration of additional hash functions and additional
   parameter sets in the future.
```

- (§2.3) "Signing involves the generation of C, which is an n-byte random value." — `R-0078`
- (§2.3) "The LM-OTS signature value can be summarized as the identifier of the LM-OTS variant, the random value, and a sequence of hash values (y[0] through y[p-1]), as described in Section 4.5 of [HASHSIG]: u32str(otstype) || C || y[0] || ... || y[p-1]" — `R-0079`

lines 305-312  sha256:3b24652ff01735c82bffba08eaa6cf6cb40a519d0fff445d2dd52ed3d95f1d68

```text
   Signing involves the generation of C, which is an n-byte random
   value.

   The LM-OTS signature value can be summarized as the identifier of the
   LM-OTS variant, the random value, and a sequence of hash values (y[0]
   through y[p-1]), as described in Section 4.5 of [HASHSIG]:

      u32str(otstype) || C || y[0] || ... || y[p-1]
```


## §3. Hash-Based Signature Algorithm Identifiers

- (§3) "The CBOR Object Signing and Encryption (COSE) [RFC8152] supports two signature algorithm schemes." — `R-0080`
- (§3) "This specification makes use of the signature with appendix scheme for hash-based signatures." — `R-0081`
- (§3) "The signature value is a large byte string, as described in Section 2." — `R-0082`
- (§3) "The byte string is designed for easy parsing." — `R-0083`
- (§3) "The HSS, LMS, and LM-OTS components of the signature value format include counters and type codes that indirectly provide all of the information that is needed to parse the byte string during signature validation." — `R-0084`

lines 320-325  sha256:345b8b7574c26a5be8e6e38e3ee876d4a8442cfeaaf210c15da030b3a322b1c3

```text
   The signature value is a large byte string, as described in
   Section 2.  The byte string is designed for easy parsing.  The HSS,
   LMS, and LM-OTS components of the signature value format include
   counters and type codes that indirectly provide all of the
   information that is needed to parse the byte string during signature
   validation.
```

**This is the whole of the COSE integration.** `R-0085` and its five bullets are
the only place the document says anything about a COSE key, and nothing anywhere
says where the signature octets go in a COSE structure — `Sig_structure` occurs
0 times and the word `tag` 0 times. Appendix A shows it; §3 does not state it.

- (§3) "When using a COSE key for this algorithm, the following checks are made:" — `R-0085`
- (§3) **"The 'kty' field MUST be 'HSS-LMS'."** — `R-0086` · **MUST** · the only unconditional obligation about a key in the document
- (§3) "If the 'alg' field is present, it MUST be 'HSS-LMS'." — `R-0087` · **MUST**, conditional on presence
- (§3) "If the 'key_ops' field is present, it MUST include 'sign' when creating a hash-based signature." — `R-0088` · **MUST**, conditional
- (§3) "If the 'key_ops' field is present, it MUST include 'verify' when verifying a hash-based signature." — `R-0089` · **MUST**, conditional
- (§3) "If the 'kid' field is present, it MAY be used to identify the top of the HSS tree." — `R-0090` · **MAY**, conditional
- (§3) "In [HASHSIG], this identifier is called 'I'" — `R-0091`, **first clause**
- (§3) **"it is the 16-byte identifier of the LMS public key for the tree."** — `R-0092`, **second clause of the same sentence**

lines 327-342  sha256:8f54dced5037d63f8f1d93ac81f5e82a74125b60f7587fdc04ee3a8503f32fb1

```text
   When using a COSE key for this algorithm, the following checks are
   made:

   *  The 'kty' field MUST be 'HSS-LMS'.

   *  If the 'alg' field is present, it MUST be 'HSS-LMS'.

   *  If the 'key_ops' field is present, it MUST include 'sign' when
      creating a hash-based signature.

   *  If the 'key_ops' field is present, it MUST include 'verify' when
      verifying a hash-based signature.

   *  If the 'kid' field is present, it MAY be used to identify the top
      of the HSS tree.  In [HASHSIG], this identifier is called 'I', and
      it is the 16-byte identifier of the LMS public key for the tree.
```

`R-0092` is in an odd place and it is load-bearing: a bullet about `kid` is the
**only** statement of `I`'s width anywhere in the document, and 16 of the 56
octets of an HSS-LMS public key depend on it. §2.2, which puts `I` *in* the
public key (`R-0049`), gives no width at all.


## §4. Security Considerations

- (§4) "The security considerations from [RFC8152] and [HASHSIG] are relevant to implementations of this specification." — `R-0093`
- (§4) "There are a number of security considerations that need to be taken into account by implementers of this specification." — `R-0094`
- (§4) "Implementations MUST protect the private keys." — `R-0095` · **MUST**
- (§4) "Compromise of the private keys may result in the ability to forge signatures." — `R-0096` · lowercase `may`, **not** BCP 14
- (§4) **"Along with the private key, the implementation MUST keep track of which leaf nodes in the tree have been used."** — `R-0097` · **MUST**
- (§4) "Loss of integrity of this tracking data can cause a one-time key to be used more than once." — `R-0098`
- (§4) "As a result, when a private key and the tracking data are stored on nonvolatile media or in a virtual machine environment, failed writes, virtual machine snapshotting or cloning, and other operational concerns must be considered to ensure confidentiality and integrity." — `R-0099` · lowercase `must`, **not** BCP 14
- (§4) "When generating an LMS key pair, an implementation MUST generate each key pair independently of all other key pairs in the HSS tree." — `R-0100` · **MUST**
- (§4) **"An implementation MUST ensure that an LM-OTS private key is used to generate a signature only one time and ensure that it cannot be used for any other purpose."** — `R-0101` · **one MUST, two obligations**

The state paragraph and the one-time-use MUST, byte-exact. `R-0097`, `R-0098`,
`R-0099`, `R-0100` and `R-0101` are the document's whole state model, and
`R-0099` — the only place that names *how* the tracking data is lost — is the
sentence in it that carries **no** keyword:

lines 352-367  sha256:901680e0ec4858794eb1028e7074db61c4e78c369fa8ea41b89782904e285437

```text
   Implementations MUST protect the private keys.  Compromise of the
   private keys may result in the ability to forge signatures.  Along
   with the private key, the implementation MUST keep track of which
   leaf nodes in the tree have been used.  Loss of integrity of this
   tracking data can cause a one-time key to be used more than once.  As
   a result, when a private key and the tracking data are stored on
   nonvolatile media or in a virtual machine environment, failed writes,
   virtual machine snapshotting or cloning, and other operational
   concerns must be considered to ensure confidentiality and integrity.

   When generating an LMS key pair, an implementation MUST generate each
   key pair independently of all other key pairs in the HSS tree.

   An implementation MUST ensure that an LM-OTS private key is used to
   generate a signature only one time and ensure that it cannot be used
   for any other purpose.
```

- (§4) "The generation of private keys relies on random numbers." — `R-0102`
- (§4) "The use of inadequate pseudorandom number generators (PRNGs) to generate these values can result in little or no security." — `R-0103`
- (§4) "An attacker may find it much easier to reproduce the PRNG environment that produced the keys, searching the resulting small set of possibilities rather than brute- force searching the whole key space." — `R-0104`, **severance 373–374**; lowercase `may`
- (§4) "The generation of quality random numbers is difficult, and [RFC4086] offers important guidance in this area." — `R-0105`
- (§4) "The generation of hash-based signatures also depends on random numbers." — `R-0106`
- (§4) "While the consequences of an inadequate PRNG to generate these values is much less severe than in the generation of private keys, the guidance in [RFC4086] remains important." — `R-0107`

`R-0106`'s random number is `C` (`R-0078`). **Both Appendix A signatures carry
the same `C`** — `examples/vectors.yaml` `V-0005`.


## §5. Operational Considerations

Every sentence of §5, and not one BCP 14 keyword among them. This section is the
reason the record is `useful`.

- (§5) "The public key for the hash-based signature is the key at the root of Hierarchical Signature System (HSS)." — `R-0108`
- (§5) **"In the absence of a public key infrastructure [RFC5280], this public key is a trust anchor, and the number of signatures that can be generated is bounded by the size of the overall HSS set of trees."** — `R-0109`
- (§5) **"When all of the LM-OTS signatures have been used to produce a signature, then the establishment of a new trust anchor is required."** — `R-0110` · lowercase `required`
- (§5) "To ensure that none of the tree nodes are used to generate more than one signature, the signer maintains state across different invocations of the signing algorithm." — `R-0111`
- (§5) "Section 9.2 of [HASHSIG] offers some practical implementation approaches around this statefulness." — `R-0112`
- (§5) "In some of these approaches, nodes are sacrificed to ensure that none are used more than once." — `R-0113`
- (§5) **"As a result, the total number of signatures that can be generated might be less than the overall HSS set of trees."** — `R-0114`
- (§5) **"A COSE Key Type Parameter for encoding the HSS/LMS private key and the state about which tree nodes have been used is deliberately not defined."** — `R-0115`
- (§5) **"It was not defined to avoid creating the ability to save the private key and state, generate one or more signatures, and then restore the private key and state."** — `R-0116`
- (§5) "Such a restoration operation provides disastrous opportunities for tree node reuse." — `R-0117`

lines 385-407  sha256:07cac90114e26cf26ca5083d3726127bb4a5a5d9efa6cf94ead9f7490cc512b5

```text
   The public key for the hash-based signature is the key at the root of
   Hierarchical Signature System (HSS).  In the absence of a public key
   infrastructure [RFC5280], this public key is a trust anchor, and the
   number of signatures that can be generated is bounded by the size of
   the overall HSS set of trees.  When all of the LM-OTS signatures have
   been used to produce a signature, then the establishment of a new
   trust anchor is required.

   To ensure that none of the tree nodes are used to generate more than
   one signature, the signer maintains state across different
   invocations of the signing algorithm.  Section 9.2 of [HASHSIG]
   offers some practical implementation approaches around this
   statefulness.  In some of these approaches, nodes are sacrificed to
   ensure that none are used more than once.  As a result, the total
   number of signatures that can be generated might be less than the
   overall HSS set of trees.

   A COSE Key Type Parameter for encoding the HSS/LMS private key and
   the state about which tree nodes have been used is deliberately not
   defined.  It was not defined to avoid creating the ability to save
   the private key and state, generate one or more signatures, and then
   restore the private key and state.  Such a restoration operation
   provides disastrous opportunities for tree node reuse.
```

Read `R-0115` precisely. §5 does **not** forbid storing the private key in
software; it **withholds the format**. There is no standard encoding for an
HSS-LMS private key and its state, on purpose, so the key cannot be backed up,
replicated or migrated by any means this document or COSE defines. §6.3
registers exactly one key type parameter for `kty: 5`, and it is the public key.


## §6. IANA Considerations

`R-0118`, quoted as a block because it contains the source's own double quotes:

> IANA has added entries for the HSS/LMS hash-based signature algorithm in the
> "COSE Algorithms" registry and added HSS/LMS hash-based signature public keys
> in the "COSE Key Types" registry and the "COSE Key Type Parameters" registry.

Three registries, and **"COSE Header Parameters" is not among them**: the word
`header` occurs zero times in the document. This binding adds exactly one value
to the COSE Algorithms registry, one key type and one key type parameter, and
nothing to the interchange surface beyond that.

lines 411-414  sha256:eb2f603d5b5b8e1fb3995b5a559d31f04e348f3ec45b765f6ca27373ab38f1a8

```text
   IANA has added entries for the HSS/LMS hash-based signature algorithm
   in the "COSE Algorithms" registry and added HSS/LMS hash-based
   signature public keys in the "COSE Key Types" registry and the "COSE
   Key Type Parameters" registry.
```

### §6.1 — COSE Algorithms (`R-0119`, `R-0120`, `R-0121`, `R-0122`)

lines 418-425  sha256:0f984db2ea2b326ec758e7385381f677f147a424fc273cb2062d8243b910d035

```text
   The new entry in the "COSE Algorithms" registry [IANA] appears as
   follows:

   Name:  HSS-LMS
   Value:  -46
   Description:  HSS/LMS hash-based digital signature
   Reference:  RFC 8778
   Recommended:  Yes
```

**"Recommended: Yes"** (`R-0122`) on a stateful one-time-signature scheme is the
`DEC-005` finding; see `design-notes.md`.

### §6.2 — COSE Key Types (`R-0123`, `R-0124`, `R-0125`)

lines 429-435  sha256:ae7fe23fbbb034b644e784be898846e53295da6d7d23ceaa30c20c3440e0f13a

```text
   The new entry in the "COSE Key Types" registry [IANA] appears as
   follows:

   Name:  HSS-LMS
   Value:  5
   Description:  Public key for HSS/LMS hash-based digital signature
   Reference:  RFC 8778
```

### §6.3 — COSE Key Type Parameters (`R-0126`, `R-0127`, `R-0128`)

lines 439-447  sha256:9452ba401033b43f48b8235adb9dc82259b14d62c669a571af5b4d34d984e72e

```text
   The new entry in the "COSE Key Type Parameters" registry [IANA]
   appears as follows:

   Key Type:  5
   Name:  pub
   Label:  -1
   CBOR Type:  bstr
   Description:  Public key for HSS/LMS hash-based digital signature
   Reference:  RFC 8778
```

**One parameter is registered for `kty: 5`, and it is the public key.** `pub`
occurs exactly once in the whole document: here. This is the label RFC 9679 §4.5
requires for an HSS-LMS COSE Key Thumbprint without citing RFC 8778 or RFC 8554.


## Appendix A. Examples — non-normative

- (Appendix A) "This appendix provides a non-normative example of a COSE full message signature and an example of a COSE_Sign1 message." — `R-0129`
- (Appendix A) "This section is formatted according to the extended CBOR diagnostic format defined by [RFC8610]." — `R-0130`
- (Appendix A) "The programs that were used to generate the examples can be found at <https://github.com/cose-wg/Examples>." — `R-0131`
- (Appendix A, A.1) "This section provides an example of a COSE full message signature." — `R-0132`
- (Appendix A, A.1) "The size of binary file is 2560 bytes." — `R-0133` · **reproduced exactly**
- (Appendix A, A.2) "This section provides an example of a COSE_Sign1 message." — `R-0134`
- (Appendix A, A.2) "The size of binary file is 2552 bytes." — `R-0135` · **reproduced exactly**

lines 555-561  sha256:11bba1b0c4fab500744eec5be8e7a3f07c43aa45c90a3ce8b2f7230c750dbfc1

```text
   This appendix provides a non-normative example of a COSE full message
   signature and an example of a COSE_Sign1 message.  This section is
   formatted according to the extended CBOR diagnostic format defined by
   [RFC8610].

   The programs that were used to generate the examples can be found at
   <https://github.com/cose-wg/Examples>.
```

**A.1's frame** — the envelope around the 2512-octet signature, byte-exact. The
signature hex itself is not reproduced in this repository; `examples/vectors.yaml`
carries its line range, its length and its parsed structure, and
`examples/README.md` says why the bytes are not copied.

lines 565-583  sha256:d1372c58355d97269bda85960d09f51e654a610eb095bddabece32183379695a

```text
   This section provides an example of a COSE full message signature.

   The size of binary file is 2560 bytes.

   98(
     [
       / protected / h'a10300' / {
           \ content type \ 3:0
         } / ,
       / unprotected / {},
       / payload / 'This is the content.',
       / signatures / [
         [
           / protected / h'a101382d' / {
               \ alg \ 1:-46 \ HSS-LMS \
             } / ,
           / unprotected / {
             / kid / 4:'ItsBig'
           },
```

lines 659-662  sha256:e4918715e23e30a4102f5a1600930ace9cdfc794ea5fb19d3d81e79bbe015a23

```text
         ]
       ]
     ]
   )
```

**A.2's frame:**

lines 666-678  sha256:e9325fdcf930d8208d5940b971cf3d1b5757846d9e685df1745e3c74c45810c6

```text
   This section provides an example of a COSE_Sign1 message.

   The size of binary file is 2552 bytes.

   18(
     [
       / protected / h'a101382d' / {
           \ alg \ 1:-46 \ HSS-LMS \
         } / ,
       / unprotected / {
         / kid / 4:'ItsBig'
       },
       / payload / 'This is the content.',
```

lines 754-755  sha256:851ec5641feeab9ede5fdcea7c5e5855c3285dfd06cdad21291e83f72d2f232a

```text
     ]
   )
```


## Observations on the source

Reported, never repaired. Nine, in document order. The first six are
typographic or editorial; the last three cost a reader something.

1. **§2's third component bullet is missing a space** (lines 145–146):
   `"Leighton-Micali One-time Signature (LM-OTS) Algorithm-- see Section 2.3"`,
   against `"Hierarchical Signature System (HSS) -- see Section 2.1"` and
   `"Leighton-Micali Signature (LMS) -- see Section 2.2"` immediately above it.
   `R-0017`.

2. **§2.2 names its index twice, differently, in one clause** (line 230–232):
   `"defines the value T[r] as the m-byte string associated with the ith node"`.
   `T[r]` and "the *i*th node" are the same index under two letters. `R-0050`.

3. **§2.2 uses a reference tag as a noun with a definite article** (line 203):
   `"The [HASHSIG] includes support for five values of this parameter"`, where
   every other sentence in the section writes `"The [HASHSIG] specification"`.
   `R-0036`.

4. **§4 has a subject–verb disagreement** (lines 379–381): `"While the
   consequences of an inadequate PRNG to generate these values is much less
   severe"`. `R-0107`.

5. **§5 drops a definite article** (lines 385–386): `"the key at the root of
   Hierarchical Signature System (HSS)"`. `R-0108`.

6. **RFC 8610 is an informative reference that the examples cannot be read
   without.** `R-0130` says Appendix A "is formatted according to the extended
   CBOR diagnostic format defined by [RFC8610]", and §7.2 (line 547) lists
   RFC 8610 under **Informative** References. The appendix is itself
   non-normative, so this is consistent; it is recorded because the only
   notation definition in the document is classified as optional reading.

7. **§2.3's definition of `p` contradicts §2.3's own layout.** `R-0070` defines
   `p` as "The number of n-byte string elements that make up the LM-OTS
   signature", and `R-0079` renders that signature as
   `u32str(otstype) || C || y[0] || ... || y[p-1]` — which contains **p + 1**
   n-byte elements, `C` and the `p` values of `y`. The definition under-counts
   by one. It is inherited from RFC 8554 §4.1 and is measurable from this
   section alone; `examples/vectors.yaml` measures it on the printed signatures,
   where `p = 67` and the LM-OTS signature is 4 + 32 + 67×32 = 2180 octets.

8. **§3's parseability claim is true of [HASHSIG] and not of this document.**
   `R-0083` ("The byte string is designed for easy parsing") and `R-0084` ("type
   codes that indirectly provide all of the information that is needed to parse
   the byte string") are correct about the format. But RFC 8778 **prints no code
   point for any LMS or LM-OTS parameter set** — §2.2 and §2.3 give the ten
   names and no numbers — and `R-0072` defers every value of `p` to [HASHSIG]
   Appendix B. So a parser built from RFC 8778 alone cannot resolve the
   `00000003` and `00000006` its own Appendix A prints to any parameter set. It
   can only solve the length equation, which this extraction did
   (`examples/vectors.yaml` `V-0003`, `V-0004`).

9. **Both Appendix A signatures carry the same `C`.** `R-0078` says "Signing
   involves the generation of C, which is an n-byte random value". Octets 12–43
   of both printed signatures are
   `91291de76ce6e24d1e2a9b60266519bc8ce889f814deb0fc00edd3129de3ab9b` — one
   value, two signatures, over two different `Sig_structure` contexts
   ("Signature" and "Signature1") from two different leaves of one tree. Not a
   conformance violation of anything RFC 8778 states, and recorded because a
   reader treating the examples as a demonstration of per-signature
   randomisation would be wrong. `examples/vectors.yaml` `V-0005`.
