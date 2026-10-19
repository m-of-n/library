---
record: rfc-8551
kind: normative
title: "rfc-8551 — normative statements"
extracted: "2026-10-18"
reviewed_by: ""
---

<!-- FX-1 pass 1. Every normative statement and normative block of RFC 8551
     (S/MIME 4.0 Message Specification), VERBATIM, with its locator and
     source line range, in source order. Verbatim source only: no analysis,
     no paraphrase, no opinion. Blockquotes and fenced blocks delimit
     verbatim text; everything outside them is structure (headings, entry
     numbers, locators, line ranges, flags, and notes on what a section
     yields). -->

Source: RFC 8551, "Secure/Multipurpose Internet Mail Extensions (S/MIME)
Version 4.0 Message Specification", J. Schaad, B. Ramsdell, S. Turner,
April 2019. Internet Engineering Task Force (IETF), Category: Standards
Track; obsoletes RFC 5751. 3531 lines, sha256
`dac39f749a08d3422bd78d4e492195067e7bc03f5fc2d0dac515f0d7ed884ae2`.

## How to read this file

**Verbatim containers.** Two are used, and the distinction matters:

- A **blockquote** (`>`) reproduces running prose. The source's own line
  breaks are kept and its leading three-space RFC indent is removed; a `>`
  line with nothing after it is one of the source's blank lines between
  paragraphs. No word, spelling, space or punctuation mark is altered — the
  source's double space after a full stop and its own typos included.
- A **fenced block** (```` ``` ````) reproduces the source's lines
  byte-exactly, indentation included. Every bulleted or numbered list, every
  `Step n.` procedure, every table, every hanging-indent definition list,
  every IANA registration template and the Appendix A ASN.1 module is
  fenced, together with the prose line that introduces it when that line is
  part of the same contiguous run, so whitespace-significant layout is never
  rewrapped.

Everything outside a quote or a fence is structure added by this
extraction, not source text. No two non-adjacent passages are ever spliced
into one entry: each entry is a single contiguous run of source lines, and
its header gives that run as `lines a–b` (1-based line numbers of the
`.cache/rfc-8551.txt` rendering hashed above).

**Locators.** RFC 8551 numbers its sections. Each locator is `§` plus the
section number as printed (`§2.5.3.1`; the appendices are `§A`, `§B`,
`§B.1` … `§B.4`, `§C`), then a position inside that section:

- `¶n` — the *n*th **block** of the section, counting every block,
  reproduced or not. A block is a maximal run of non-blank source lines
  between the section's heading and the next heading of any level, so a
  parent section's count stops at its first subsection. Each bullet, each
  numbered item, each `Step n.`, each hanging-indent definition, and each
  indented continuation paragraph under a bullet is its own block. A table
  is **one** block even where the source puts blank lines between its rows
  (§3.10 ¶3). A block split by a page break is still one block.
- `¶m–¶n` — an entry that reproduces blocks *m* through *n* inclusive, a
  contiguous run; used where an introducing sentence, its list and any note
  under it are kept together.
- `template` — the whole media-type or registry template of §5.1, §5.2 and
  §5.3; `module` — the ASN.1 module of Appendix A, from its module name
  (`SecureMimeMessageV3dot1`) to `END`.

Rows of a table and items of a list are pinned by the entry's line range;
every table and list is reproduced whole.

**Page breaks.** The source is the paginated plain-text RFC. Twelve entries
run across a page boundary, and each is flagged `_[crosses page break]_`:
N-003, N-053, N-058, N-063, N-091, N-096, N-122, N-165, N-169, N-172, N-174
and N-177. In those entries, and only those, the page furniture is deleted:
the footer line (`Schaad, et al.` … `Standards Track` … `[Page n]`), the
form-feed line, the running header (`RFC 8551` … `S/MIME 4.0 Message
Specification` … `April 2019`) and the blank padding lines around them.
Nothing else is touched. In three of them (N-091, N-096, N-169) the boundary
falls mid-sentence and the two halves are joined directly. In the other nine
it falls between two blocks, and one of the source's own blank lines is left
in place, as at every other block boundary. The line range of a crossing
entry includes the furniture lines it removes. Every other entry lies wholly
within one page.

**Flags.** Each entry header may carry:

- `_[lowercase]_` — the entry carries a lowercase `must`, `should`, `may`,
  `required`, `recommended`, `optional` or `ought to` that bears normative
  weight (RFC 8174: only capitals are BCP 14 keywords). Entries are flagged
  whether or not they also carry a capitalised keyword. Lowercase words that
  only describe (`other required data`, `may have changed`) do not set the
  flag; see *Lowercase accounting* below.
- `_[implied]_` — the entry carries no capitalised keyword and no weighted
  lowercase modal, and is included because it binds or scopes the rest: a
  definition, a procedure step, a structure or property of a content type
  or media type, a stated security property or precondition, or a pointer
  to where a requirement is specified.
- `_[table]_` — the entry is or contains a table of the source.
- `_[ASN.1]_` — the entry is the Appendix A ASN.1 module.
- `_[IANA]_` — the entry is an IANA action or registration template.
- `_[changelog]_` — the entry is from §1.5 or §1.6, which record changes
  between earlier versions of S/MIME. Its capitalised keywords name the
  requirement levels of those versions, not of S/MIME 4.0; the entries are
  reproduced because every capitalised keyword token of the source is.
- `_[boilerplate]_` — the BCP 14 conventions paragraph (N-004).
- `_[crosses page break]_` — see *Page breaks*.

**BCP 14 census: 190.** `bin/bcp14-count .cache/rfc-8551.txt --by-keyword`
returns 190 — MUST 82, SHOULD 84, MAY 12, MUST NOT 5, SHOULD NOT 4,
RECOMMENDED 2, OPTIONAL 1; no SHALL, SHALL NOT, REQUIRED or NOT
RECOMMENDED — after it strips the BCP 14 conventions paragraph (§1.3 ¶1,
reproduced here as N-004, which itself counts 0). The counter
(`bin/_bcp14.py`) matches capitals only, longest match first, with a
non-letter on each side, so the source's own requirement levels `SHOULD+`,
`SHOULD-` and `MUST-` (defined in §1.3, N-005) count as `SHOULD` and `MUST`.
No keyword in this source is split across a line break. All 190 lie inside
the entries below; the reconciliation is under *Coverage*. Of the 190, these
are not operative S/MIME 4.0 requirements in their own words, and are
reproduced so that the census reconciles: 14 in the definitions of
`SHOULD+`, `SHOULD-` and `MUST-` (N-005); 23 in the §1.5–§1.6 changelog
(N-008 to N-012); the `SHOULD` of an ASN.1 comment and the `OPTIONAL` of
ASN.1 type notation in the module (N-174).

**Not reproduced.** The front matter (title block, Abstract, Status of This
Memo, Copyright Notice, Table of Contents), §1 Introduction, §1.7, §7.2 and
§7.3 (reference lists), Appendix C, Acknowledgements and Authors' Addresses
yield no entry. Inside sections that do yield entries, every omitted block
is named in an italic note under its section heading, so that every
omission is a recorded decision rather than a drop. The sample messages and
example displays of §3.1.4, §3.3, §3.4, §3.5.2, §3.5.3.3 and §3.6 are not
normative statements and are not reproduced here; they are the examples
artifact's material.

**Lowercase accounting.** Over the whole source, case-sensitively, the
whole words `must`, `should`, `may`, `shall`, `required`, `recommended` and
`optional` occur 53 times (`shall` never), and `ought` once. 45 of the 53,
and the `ought`, lie inside entries. The 8 outside are: the front matter
(line 39 `may`, Status of This Memo; lines 73, 78, 81, 84, 85: `must`, `may`
×4, Copyright Notice), line 482 `required` (§1.5 ¶8, a changelog bullet not
reproduced) and line 1185 `required` (§3 ¶2, not reproduced). The entries
flagged `_[lowercase]_` are those listed under *Coverage*.

**Source text kept as printed.** These are the source's own and are not
corrected: the ASN.1 identifier `receipentKeyId` (N-174), which the module's
own comment calls misspelled; `File extensions(s)` in both media-type
templates (N-149, N-150); `SHOULD+ support RSA Encryption Scheme - Optimal
Asymmetric Encryption Padding` (N-021); `MD5*` / `SHA-1*` and the `*Note`
under the micalg table (N-119); the double space in `4096 <  key size` in
each key-size table (N-143 to N-146); `RSA-OAEP` in §4.4 beside `RSAES-OAEP`
in §4.5 (N-145, N-146); the bullets of §3.7 ¶6–¶7 whose continuation lines
sit at the bullet's own indent rather than under its text (N-128). The
source's cross-labels are also reproduced as printed: §7.1 (N-172) assigns
[SMIMEv3.1] the RFC list that §1.4 ¶5 gives for S/MIME version 3.2 and
[SMIMEv3.2] the list §1.4 ¶4 gives for version 3.1; Appendix A ¶1 (N-173)
labels RFC 5751 `[SMIMEv2]`; §1.6 ¶24 (not reproduced) names `Appendix B`
for the move to Historic, which this document prints as Appendix C. §1.4 is
not reproduced beyond ¶1, so its lists are recorded here only as the
referent of the §7.1 observation.



## Front matter

_No entries — title block, Abstract (overview of S/MIME; states no
requirement), Status of This Memo, Copyright Notice and Table of Contents.
Their lowercase modals (lines 39, 73, 78, 81, 84, 85) govern the document,
not S/MIME._



## §1 Introduction

_No entries — ¶1–¶4 describe S/MIME's services and transports and that this
document defines version 4.0 (overview); ¶5 explains that references to
obsoleted documents are intentional (editorial). No requirement, definition
or rule._

### §1.1 Specification Overview

_Not reproduced: ¶1–¶3 (what the document describes: overview of the CMS
body parts, application/pkcs7-mime and multipart/signed, each specified in
§3), ¶6 (motivation for separating receiving-agent and sending-agent
requirements)._

**N-001.** (§1.1 ¶4) — lines 293–295

> In order to create S/MIME messages, an S/MIME agent MUST follow the
> specifications in this document, as well as the specifications listed
> in [CMS], [RFC3370], [RFC4056], [RFC3560], and [RFC5754].

**N-002.** (§1.1 ¶5) _[implied]_ — lines 297–304

> Throughout this specification, there are requirements and
> recommendations made for how receiving agents handle incoming
> messages.  There are separate requirements and recommendations for
> how sending agents create outgoing messages.  In general, the best
> strategy is to follow the Robustness Principle (be liberal in what
> you receive and conservative in what you send).  Most of the
> requirements are placed on the handling of incoming messages, while
> the recommendations are mostly on the creation of outgoing messages.

### §1.2 Definitions

**N-003.** (§1.2 ¶1–¶14) _[implied]_ _[crosses page break]_ — lines 317–379

```
   For the purposes of this specification, the following definitions
   apply.

   ASN.1:
      Abstract Syntax Notation One, as defined in ITU-T Recommendations
      X.680, X.681, X.682, and X.683 [ASN.1].

   BER:
      Basic Encoding Rules for ASN.1, as defined in ITU-T Recommendation
      X.690 [X.690].

   Certificate:
      A type that binds an entity's name to a public key with a digital
      signature.

   DER:
      Distinguished Encoding Rules for ASN.1, as defined in ITU-T
      Recommendation X.690 [X.690].

   7-bit data:
      Text data with lines less than 998 characters long, where none of
      the characters have the 8th bit set, and there are no NULL
      characters.  <CR> and <LF> occur only as part of a <CR><LF>
      end-of-line delimiter.

   8-bit data:
      Text data with lines less than 998 characters, and where none of
      the characters are NULL characters.  <CR> and <LF> occur only as
      part of a <CR><LF> end-of-line delimiter.

   Binary data:
      Arbitrary data.

   Transfer encoding:
      A reversible transformation made on data so 8-bit or binary data
      can be sent via a channel that only transmits 7-bit data.

   Receiving agent:
      Software that interprets and processes S/MIME CMS objects, MIME
      body parts that contain CMS content types, or both.

   Sending agent:
      Software that creates S/MIME CMS content types, MIME body parts
      that contain CMS content types, or both.

   S/MIME agent:
      User software that is a receiving agent, a sending agent, or both.

   Data integrity service:
      A security service that protects against unauthorized changes to
      data by ensuring that changes to the data are detectable
      [RFC4949].

   Data confidentiality:
      The property that data is not disclosed to system entities unless
      they have been authorized to know the data [RFC4949].
```

### §1.3 Conventions Used in This Document

**N-004.** (§1.3 ¶1) _[boilerplate]_ — lines 383–387

> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
> "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
> "OPTIONAL" in this document are to be interpreted as described in
> BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
> capitals, as shown here.

**N-005.** (§1.3 ¶2–¶5) — lines 399–414

```
   We define the additional requirement levels:

   SHOULD+   This term means the same as SHOULD.  However, the authors
             expect that a requirement marked as SHOULD+ will be
             promoted at some future time to be a MUST.

   SHOULD-   This term means the same as SHOULD.  However, the authors
             expect that a requirement marked as SHOULD- will be demoted
             to a MAY in a future version of this document.

   MUST-     This term means the same as MUST.  However, the authors
             expect that this requirement will no longer be a MUST in a
             future document.  Although its status will be determined at
             a later time, it is reasonable to expect that if a future
             revision of a document alters the status of a MUST-
             requirement, it will remain at least a SHOULD or a SHOULD-.
```

**N-006.** (§1.3 ¶6) _[implied]_ — lines 416–420

> The term "RSA" in this document almost always refers to the
> PKCS #1 v1.5 RSA [RFC2313] signature or encryption algorithms even
> when not qualified as such.  There are a couple of places where it
> refers to the general RSA cryptographic operation; these can be
> determined from the context where it is used.

### §1.4 Compatibility with Prior Practice of S/MIME

_Not reproduced: ¶2–¶6 (the RFCs that make up S/MIME versions 2 to 3.2, and
a pointer to RFC 2311's history; bibliographic)._

**N-007.** (§1.4 ¶1) _[lowercase]_ — lines 424–425

> S/MIME version 4.0 agents ought to attempt to have the greatest
> interoperability possible with agents for prior versions of S/MIME.

### §1.5 Changes from S/MIME v3 to S/MIME v3.1

_Not reproduced: ¶5–¶8 (changelog bullets with no capitalised keyword; ¶8
holds the lowercase `required` of line 482)._

**N-008.** (§1.5 ¶1–¶4) _[changelog]_ — lines 457–470

```
   This section describes the changes made between S/MIME v3 and
   S/MIME v3.1.  Note that the requirement levels indicated by the
   capitalized key words ("MUST", "SHOULD", etc.) may have changed in
   later versions of S/MIME.

   -  The RSA public key algorithm was changed to a MUST implement.  The
      key wrap algorithm and the Diffie-Hellman (DH) algorithm [RFC2631]
      were changed to a SHOULD implement.

   -  The AES symmetric encryption algorithm has been included as a
      SHOULD implement.

   -  The RSA public key algorithm was changed to a MUST implement
      signature algorithm.
```

### §1.6 Changes from S/MIME v3.1 to S/MIME v3.2

_Not reproduced: ¶2, ¶4–¶6, ¶11–¶13 and ¶15–¶24 (changelog bullets with no
capitalised keyword)._

**N-009.** (§1.6 ¶1) _[changelog]_ — lines 487–491

> This section describes the changes made between S/MIME v3.1 and
> S/MIME v3.2.  Note that the requirement levels indicated by the
> capitalized key words ("MUST", "SHOULD", etc.) may have changed in
> later versions of S/MIME.  Note that the section numbers listed here
> (e.g., 3.4.3.2) are from [RFC5751].

**N-010.** (§1.6 ¶3) _[changelog]_ — lines 496–497

```
   -  Moved "Conventions Used in This Document" to Section 1.3.  Added
      definitions for SHOULD+, SHOULD-, and MUST-.
```

**N-011.** (§1.6 ¶7–¶10) _[changelog]_ — lines 516–530

```
   -  Section 2.1 (digest algorithm): SHA-256 added as MUST, SHA-1 and
      MD5 made SHOULD-.

   -  Section 2.2 (signature algorithms): RSA with SHA-256 added as
      MUST; DSA with SHA-256 added as SHOULD+; RSA with SHA-1, DSA with
      SHA-1, and RSA with MD5 changed to SHOULD-; and RSASSA-PSS with
      SHA-256 added as SHOULD+.  Also added note about what S/MIME v3.1
      clients support.

   -  Section 2.3 (key encryption): DH changed to SHOULD-, and RSAES-
      OAEP added as SHOULD+.  Elaborated on requirements for key wrap
      algorithm.

   -  Section 2.5.1: Added requirement that receiving agents MUST
      support both GeneralizedTime and UTCTime.
```

**N-012.** (§1.6 ¶14) _[changelog]_ — lines 542–543

```
   -  Section 2.7 (content encryption): AES-128 CBC added as MUST,
      AES-192 and AES-256 CBC SHOULD+, and tripleDES now SHOULD-.
```

### §1.7 Changes for S/MIME v4.0

_No entries — changelog of S/MIME v4.0 against v3.2; no capitalised keyword.
Each change it lists is specified, with its requirement level, in the
section it names._



## §2 CMS Options

**N-013.** (§2 ¶1) _[implied]_ — lines 625–631

> CMS allows for a wide variety of options in content, attributes, and
> algorithm support.  This section puts forth a number of support
> requirements and recommendations in order to achieve a base level of
> interoperability among all S/MIME implementations.  [RFC3370] and
> [RFC5754] provide additional details regarding the use of the
> cryptographic algorithms.  [ESS] provides additional details
> regarding the use of additional attributes.

### §2.1 DigestAlgorithmIdentifier

**N-014.** (§2.1 ¶1) — lines 635–641

> The algorithms here are used for digesting the body of the message
> and are not the same as the digest algorithms used as part of the
> signature algorithms.  The result of this is placed in the
> message-digest attribute of the signed attributes.  It is RECOMMENDED
> that the algorithm used for digesting the body of the message be of
> similar strength to, or greater strength than, the signature
> algorithm.

**N-015.** (§2.1 ¶2–¶4) — lines 643–647

```
   Sending and receiving agents:

   -  MUST support SHA-256.

   -  MUST support SHA-512.
```

**N-016.** (§2.1 ¶5) _[implied]_ — lines 649–650

> [RFC5754] provides the details for using these algorithms with
> S/MIME.

### §2.2 SignatureAlgorithmIdentifier

**N-017.** (§2.2 ¶1) _[implied]_ — lines 654–657

> There are different sets of requirements placed on receiving and
> sending agents.  By having the different requirements, the maximum
> amount of interoperability is achieved, as it allows for specialized
> protection of private key material but maximum signature validation.

**N-018.** (§2.2 ¶2–¶6) — lines 659–668

```
   Receiving agents:

   -  MUST support ECDSA with curve P-256 and SHA-256.

   -  MUST support EdDSA with curve25519 using PureEdDSA mode [RFC8419].

   -  MUST- support RSA PKCS #1 v1.5 with SHA-256.

   -  SHOULD support the RSA Probabilistic Signature Scheme (RSASSA-PSS)
      with SHA-256.
```

**N-019.** (§2.2 ¶7–¶10) — lines 679–687

```
   Sending agents:

   -  MUST support at least one of the following algorithms: ECDSA with
      curve P-256 and SHA-256, or EdDSA with curve25519 using PureEdDSA
      mode.

   -  MUST- support RSA PKCS #1 v1.5 with SHA-256.

   -  SHOULD support RSASSA-PSS with SHA-256.
```

**N-020.** (§2.2 ¶11) _[implied]_ — line 689

> See Section 4.1 for information on key size and algorithm references.

### §2.3 KeyEncryptionAlgorithmIdentifier

**N-021.** (§2.3 ¶1–¶5) — lines 693–705

```
   Receiving and sending agents:

   -  MUST support Elliptic Curve Diffie-Hellman (ECDH) ephemeral-static
      mode for P-256, as specified in [RFC5753].

   -  MUST support ECDH ephemeral-static mode for X25519 using HKDF-256
      ("HKDF" stands for "HMAC-based Key Derivation Function") for the
      KDF, as specified in [RFC8418].

   -  MUST- support RSA encryption, as specified in [RFC3370].

   -  SHOULD+ support RSA Encryption Scheme - Optimal Asymmetric
      Encryption Padding (RSAES-OAEP), as specified in [RFC3560].
```

**N-022.** (§2.3 ¶6) — lines 707–717

> When ECDH ephemeral-static is used, a key wrap algorithm is also
> specified in the KeyEncryptionAlgorithmIdentifier [RFC5652].  The
> underlying encryption functions for the key wrap and content-
> encryption algorithms [RFC3370] [RFC3565] and the key sizes for the
> two algorithms MUST be the same (e.g., AES-128 key wrap algorithm
> with AES-128 content-encryption algorithm).  As both 128-bit and
> 256-bit AES modes are mandatory to implement as content-encryption
> algorithms (Section 2.7), both the AES-128 and AES-256 key wrap
> algorithms MUST be supported when ECDH ephemeral-static is used.
> Recipients MAY enforce this but MUST use the weaker of the two as
> part of any cryptographic strength computations they might do.

**N-023.** (§2.3 ¶7) _[implied]_ — lines 719–720

> Appendix B provides information on algorithm support in older
> versions of S/MIME.

### §2.4 General Syntax

**N-024.** (§2.4 ¶1) _[implied]_ — lines 724–726

> There are several CMS content types.  Of these, only the Data,
> SignedData, EnvelopedData, AuthEnvelopedData, and CompressedData
> content types are currently used for S/MIME.

#### §2.4.1 Data Content Type

**N-025.** (§2.4.1 ¶1) — lines 737–748

> Sending agents MUST use the id-data content type identifier to
> identify the "inner" MIME message content.  For example, when
> applying a digital signature to MIME data, the CMS SignedData
> encapContentInfo eContentType MUST include the id-data object
> identifier (OID), and the media type MUST be stored in the SignedData
> encapContentInfo eContent OCTET STRING (unless the sending agent is
> using multipart/signed, in which case the eContent is absent, per
> Section 3.5.3 of this document).  As another example, when applying
> encryption to MIME data, the CMS EnvelopedData encryptedContentInfo
> contentType MUST include the id-data OID and the encrypted MIME
> content MUST be stored in the EnvelopedData encryptedContentInfo
> encryptedContent OCTET STRING.

#### §2.4.2 SignedData Content Type

**N-026.** (§2.4.2 ¶1) — lines 752–756

> Sending agents MUST use the SignedData content type to apply a
> digital signature to a message or, in a degenerate case where there
> is no signature information, to convey certificates.  Applying a
> signature to a message provides authentication, message integrity,
> and non-repudiation of origin.

#### §2.4.3 EnvelopedData Content Type

**N-027.** (§2.4.3 ¶1) _[implied]_ — lines 760–763

> This content type is used to apply data confidentiality to a message.
> In order to distribute the symmetric key, a sender needs to have
> access to a public key for each intended message recipient to use
> this service.

#### §2.4.4 AuthEnvelopedData Content Type

**N-028.** (§2.4.4 ¶1) _[implied]_ — lines 767–771

> This content type is used to apply data confidentiality and message
> integrity to a message.  This content type does not provide
> authentication or non-repudiation.  In order to distribute the
> symmetric key, a sender needs to have access to a public key for each
> intended message recipient to use this service.

#### §2.4.5 CompressedData Content Type

**N-029.** (§2.4.5 ¶1) _[implied]_ — lines 775–778

> This content type is used to apply data compression to a message.
> This content type does not provide authentication, message integrity,
> non-repudiation, or data confidentiality; it is only used to reduce
> the message's size.

**N-030.** (§2.4.5 ¶2) _[implied]_ — lines 780–781

> See Section 3.7 for further guidance on the use of this type in
> conjunction with other CMS types.

### §2.5 Attributes and the SignerInfo Type

**N-031.** (§2.5 ¶1) _[lowercase]_ — lines 793–798

> The SignerInfo type allows the inclusion of unsigned and signed
> attributes along with a signature.  These attributes can be required
> for the processing of messages (e.g., message digest), information
> the signer supplied (e.g., SMIME capabilities) that should be
> processed, or attributes that are not relevant to the current
> situation (e.g., mlExpansionHistory [RFC2634] for mail viewers).

**N-032.** (§2.5 ¶2–¶7) — lines 800–813

```
   Receiving agents MUST be able to handle zero or one instance of each
   of the signed attributes listed here.  Sending agents SHOULD generate
   one instance of each of the following signed attributes in each
   S/MIME message:

   -  Signing time (Section 2.5.1 in this document)

   -  SMIME capabilities (Section 2.5.2 in this document)

   -  Encryption key Preference (Section 2.5.3 in this document)

   -  Message digest (Section 11.2 in [RFC5652])

   -  Content type (Section 11.1 in [RFC5652])
```

**N-033.** (§2.5 ¶8) — lines 815–818

> Further, receiving agents SHOULD be able to handle zero or one
> instance of the signingCertificate and signingCertificateV2 signed
> attributes, as defined in Section 5 of RFC 2634 [ESS] and Section 3
> of RFC 5035 [ESS], respectively.

**N-034.** (§2.5 ¶9) — lines 820–822

> Sending agents SHOULD generate one instance of the signingCertificate
> or signingCertificateV2 signed attribute in each SignerInfo
> structure.

**N-035.** (§2.5 ¶10) — lines 824–826

> Additional attributes and values for these attributes might be
> defined in the future.  Receiving agents SHOULD handle attributes or
> values that they do not recognize in a graceful manner.

**N-036.** (§2.5 ¶11) — lines 828–830

> Interactive sending agents that include signed attributes that are
> not listed here SHOULD display those attributes to the user, so that
> the user is aware of all of the data being signed.

#### §2.5.1 Signing Time Attribute

**N-037.** (§2.5.1 ¶1) _[implied]_ — lines 834–836

> The signingTime attribute is used to convey the time that a message
> was signed.  The time of signing will most likely be created by a
> signer and therefore is only as trustworthy as that signer.

**N-038.** (§2.5.1 ¶2–¶3) — lines 847–853

```
   Sending agents MUST encode signing time through the year 2049 as
   UTCTime; signing times in 2050 or later MUST be encoded as
   GeneralizedTime.  When the UTCTime CHOICE is used, S/MIME agents MUST
   interpret the year field (YY) as follows:

      If YY is greater than or equal to 50, the year is interpreted as
      19YY; if YY is less than 50, the year is interpreted as 20YY.
```

**N-039.** (§2.5.1 ¶4) — lines 855–856

> Receiving agents MUST be able to process signingTime attributes that
> are encoded in either UTCTime or GeneralizedTime.

#### §2.5.2 SMIMECapabilities Attribute

**N-040.** (§2.5.2 ¶1) _[implied]_ — lines 860–872

> The SMIMECapabilities attribute includes signature algorithms (such
> as "sha256WithRSAEncryption"), symmetric algorithms (such as "AES-128
> CBC"), authenticated symmetric algorithms (such as "AES-128 GCM"),
> and key encipherment algorithms (such as "rsaEncryption").  The
> presence of an SMIMECapability attribute containing an algorithm
> implies that the sender can deal with the algorithm as well as
> understand the ASN.1 structures associated with that algorithm.
> There are also several identifiers that indicate support for other
> optional features such as binary encoding and compression.  The
> SMIMECapabilities attribute was designed to be flexible and
> extensible so that, in the future, a means of identifying other
> capabilities and preferences such as certificates can be added in a
> way that will not cause current clients to break.

**N-041.** (§2.5.2 ¶2) — lines 874–881

> If present, the SMIMECapabilities attribute MUST be a
> SignedAttribute.  CMS defines SignedAttributes as a SET OF Attribute.
> The SignedAttributes in a signerInfo MUST include a single instance
> of the SMIMECapabilities attribute.  CMS defines the ASN.1 syntax for
> Attribute to include attrValues SET OF AttributeValue.  An
> SMIMECapabilities attribute MUST only include a single instance of
> AttributeValue.  If a signature is detected as violating these
> requirements, the signature SHOULD be treated as failing.

**N-042.** (§2.5.2 ¶3) — lines 883–891

> The semantics of the SMIMECapabilities attribute specify a partial
> list as to what the client announcing the SMIMECapabilities can
> support.  A client does not have to list every capability it
> supports, and it need not list all its capabilities so that the
> capabilities list doesn't get too long.  In an SMIMECapabilities
> attribute, the OIDs are listed in order of their preference but
> SHOULD be separated logically along the lines of their categories
> (signature algorithms, symmetric algorithms, key encipherment
> algorithms, etc.).

**N-043.** (§2.5.2 ¶4) — lines 903–910

> The structure of the SMIMECapabilities attribute is to facilitate
> simple table lookups and binary comparisons in order to determine
> matches.  For instance, the encoding for the SMIMECapability for
> sha256WithRSAEncryption includes rather than omits the NULL
> parameter.  Because of the requirement for identical encoding,
> individuals documenting algorithms to be used in the
> SMIMECapabilities attribute SHOULD explicitly document the correct
> byte sequence for the common cases.

**N-044.** (§2.5.2 ¶5) — lines 912–914

> For any capability, the associated parameters for the OID MUST
> specify all of the parameters necessary to differentiate between two
> instances of the same algorithm.

**N-045.** (§2.5.2 ¶6) — lines 916–928

> The same OID that is used to identify an algorithm SHOULD also be
> used in the SMIMECapability for that algorithm.  There are cases
> where a single OID can correspond to multiple algorithms.  In these
> cases, a single algorithm MUST be assigned to the SMIMECapability
> using that OID.  Additional OIDs from the smimeCapabilities OID tree
> are then allocated for the other algorithms usages.  For instance, in
> an earlier specification, rsaEncryption was ambiguous because it
> could refer to either a signature algorithm or a key encipherment
> algorithm.  In the event that an OID is ambiguous, it needs to be
> arbitrated by the maintainer of the registered SMIMECapabilities list
> as to which type of algorithm will use the OID, and a new OID MUST be
> allocated under the smimeCapabilities OID to satisfy the other use of
> the OID.

**N-046.** (§2.5.2 ¶7) — lines 930–937

> The registered SMIMECapabilities list specifies the parameters for
> OIDs that need them, most notably key lengths in the case of
> variable-length symmetric ciphers.  In the event that there are no
> differentiating parameters for a particular OID, the parameters MUST
> be omitted and MUST NOT be encoded as NULL.  Additional values for
> the SMIMECapabilities attribute might be defined in the future.
> Receiving agents MUST handle an SMIMECapabilities object that has
> values that it does not recognize in a graceful manner.

**N-047.** (§2.5.2 ¶8) _[implied]_ — line 939

> Section 2.7.1 explains a strategy for caching capabilities.

#### §2.5.3 Encryption Key Preference Attribute

**N-048.** (§2.5.3 ¶1) _[implied]_ — lines 943–950

> The encryption key preference attribute allows the signer to
> unambiguously describe which of the signer's certificates has the
> signer's preferred encryption key.  This attribute is designed to
> enhance behavior for interoperating with those clients that use
> separate keys for encryption and signing.  This attribute is used to
> convey to anyone viewing the attribute which of the listed
> certificates is appropriate for encrypting a session key for future
> encrypted messages.

**N-049.** (§2.5.3 ¶2) — lines 959–966

> If present, the SMIMEEncryptionKeyPreference attribute MUST be a
> SignedAttribute.  CMS defines SignedAttributes as a SET OF Attribute.
> The SignedAttributes in a signerInfo MUST include a single instance
> of the SMIMEEncryptionKeyPreference attribute.  CMS defines the ASN.1
> syntax for Attribute to include attrValues SET OF AttributeValue.  An
> SMIMEEncryptionKeyPreference attribute MUST only include a single
> instance of AttributeValue.  If a signature is detected as violating
> these requirements, the signature SHOULD be treated as failing.

**N-050.** (§2.5.3 ¶3) — lines 968–974

> The sending agent SHOULD include the referenced certificate in the
> set of certificates included in the signed message if this attribute
> is used.  The certificate MAY be omitted if it has been previously
> made available to the receiving agent.  Sending agents SHOULD use
> this attribute if the commonly used or preferred encryption
> certificate is not the same as the certificate used to sign the
> message.

**N-051.** (§2.5.3 ¶4) — lines 976–983

> Receiving agents SHOULD store the preference data if the signature on
> the message is valid and the signing time is greater than the
> currently stored value.  (As with the SMIMECapabilities, the clock
> skew SHOULD be checked and the data not used if the skew is too
> great.)  Receiving agents SHOULD respect the sender's encryption key
> preference attribute if possible.  This, however, represents only a
> preference, and the receiving agent can use any certificate in
> replying to the sender that is valid.

**N-052.** (§2.5.3 ¶5) _[implied]_ — line 985

> Section 2.7.1 explains a strategy for caching preference data.

##### §2.5.3.1 Selection of Recipient Key Management Certificate

**N-053.** (§2.5.3.1 ¶1–¶4) _[crosses page break]_ — lines 989–1019

```
   In order to determine the key management certificate to be used when
   sending a future CMS EnvelopedData message for a particular
   recipient, the following steps SHOULD be followed:

   -  If an SMIMEEncryptionKeyPreference attribute is found in a
      SignedData object received from the desired recipient, this
      identifies the X.509 certificate that SHOULD be used as the X.509
      key management certificate for the recipient.

   -  If an SMIMEEncryptionKeyPreference attribute is not found in a
      SignedData object received from the desired recipient, the set of
      X.509 certificates SHOULD be searched for an X.509 certificate
      with the same subject name as the signer of an X.509 certificate
      that can be used for key management.

   -  Or, use some other method of determining the user's key management
      key.  If an X.509 key management certificate is not found, then
      encryption cannot be done with the signer of the message.  If
      multiple X.509 key management certificates are found, the S/MIME
      agent can make an arbitrary choice between them.
```

### §2.6 SignerIdentifier SignerInfo Type

**N-054.** (§2.6 ¶1) — lines 1023–1025

> S/MIME v4.0 implementations MUST support both issuerAndSerialNumber
> and subjectKeyIdentifier.  Messages that use the subjectKeyIdentifier
> choice cannot be read by S/MIME v2 clients.

**N-055.** (§2.6 ¶2) — lines 1027–1033

> It is important to understand that some certificates use a value for
> subjectKeyIdentifier that is not suitable for uniquely identifying a
> certificate.  Implementations MUST be prepared for multiple
> certificates for potentially different entities to have the same
> value for subjectKeyIdentifier and MUST be prepared to try each
> matching certificate during signature verification before indicating
> an error condition.

### §2.7 ContentEncryptionAlgorithmIdentifier

**N-056.** (§2.7 ¶1–¶4) — lines 1037–1046

```
   Sending and receiving agents:

   -  MUST support encryption and decryption with AES-128 GCM and
      AES-256 GCM [RFC5084].

   -  MUST- support encryption and decryption with AES-128 CBC
      [RFC3565].

   -  SHOULD+ support encryption and decryption with ChaCha20-Poly1305
      [RFC7905].
```

#### §2.7.1 Deciding Which Encryption Method to Use

**N-057.** (§2.7.1 ¶1) _[implied]_ — lines 1050–1055

> When a sending agent creates an encrypted message, it has to decide
> which type of encryption to use.  The decision process involves using
> information garnered from the capabilities lists included in messages
> received from the recipient, as well as out-of-band information such
> as private agreements, user preferences, legal restrictions, and
> so on.

**N-058.** (§2.7.1 ¶2–¶4) _[crosses page break]_ — lines 1057–1084

```
   Section 2.5.2 defines a method by which a sending agent can
   optionally announce, among other things, its decrypting capabilities
   in its order of preference.  The following method for processing and
   remembering the encryption capabilities attribute in incoming signed
   messages SHOULD be used.

   -  If the receiving agent has not yet created a list of capabilities
      for the sender's public key, then, after verifying the signature
      on the incoming message and checking the timestamp, the receiving
      agent SHOULD create a new list containing at least the signing
      time and the symmetric capabilities.

   -  If such a list already exists, the receiving agent SHOULD verify
      that the signing time in the incoming message is greater than the
      signing time stored in the list and that the signature is valid.
      If so, the receiving agent SHOULD update both the signing time and
      capabilities in the list.  Values of the signing time that lie far
      in the future (that is, a greater discrepancy than any reasonable
      clock skew), or a capabilities list in messages whose signature
      could not be verified, MUST NOT be accepted.
```

**N-059.** (§2.7.1 ¶5) — lines 1086–1087

> The list of capabilities SHOULD be stored for future use in creating
> messages.

**N-060.** (§2.7.1 ¶6) — lines 1089–1095

> Before sending a message, the sending agent MUST decide whether it is
> willing to use weak encryption for the particular data in the
> message.  If the sending agent decides that weak encryption is
> unacceptable for this data, then the sending agent MUST NOT use a
> weak algorithm.  The decision to use or not use weak encryption
> overrides any other decision in this section about which encryption
> algorithm to use.

**N-061.** (§2.7.1 ¶7) — lines 1097–1100

> Sections 2.7.1.1 and 2.7.1.2 describe the decisions a sending agent
> SHOULD use when choosing which type of encryption will be applied to
> a message.  These rules are ordered, so the sending agent SHOULD make
> its decision in the order given.

##### §2.7.1.1 Rule 1: Known Capabilities

**N-062.** (§2.7.1.1 ¶1) — lines 1104–1111

> If the sending agent has received a set of capabilities from the
> recipient for the message the agent is about to encrypt, then the
> sending agent SHOULD use that information by selecting the first
> capability in the list (that is, the capability most preferred by the
> intended recipient) that the sending agent knows how to encrypt.  The
> sending agent SHOULD use one of the capabilities in the list if the
> agent reasonably expects the recipient to be able to decrypt the
> message.

##### §2.7.1.2 Rule 2: Unknown Capabilities, Unknown Version of S/MIME

**N-063.** (§2.7.1.2 ¶1–¶3) _[lowercase]_ _[crosses page break]_ — lines 1115–1131

```
   If the following two conditions are met, the sending agent SHOULD use
   AES-256 GCM, as AES-256 GCM is a stronger algorithm and is required
   by S/MIME v4.0:

   -  The sending agent has no knowledge of the encryption capabilities
      of the recipient.

   -  The sending agent has no knowledge of the version of S/MIME used
      or supported by the recipient.
```

**N-064.** (§2.7.1.2 ¶4) — lines 1133–1135

> If the sending agent chooses not to use AES-256 GCM in this step,
> given the presumption is that a client implementing AES-GCM would do
> both AES-256 and AES-128, it SHOULD use AES-128 CBC.

#### §2.7.2 Choosing Weak Encryption

**N-065.** (§2.7.2 ¶1) — lines 1139–1147

> Algorithms such as RC2 are considered to be weak encryption
> algorithms.  Algorithms such as TripleDES are not state of the art
> and are considered to be weaker algorithms than AES.  A sending agent
> that is controlled by a human SHOULD allow a human sender to
> determine the risks of sending data using a weaker encryption
> algorithm before sending the data, and possibly allow the human to
> use a stronger encryption algorithm such as AES GCM or AES CBC even
> if there is a possibility that the recipient will not be able to
> process that algorithm.

#### §2.7.3 Multiple Recipients

**N-066.** (§2.7.3 ¶1) _[implied]_ — lines 1151–1158

> If a sending agent is composing an encrypted message to a group of
> recipients where the encryption capabilities of some of the
> recipients do not overlap, the sending agent is forced to send more
> than one message.  Please note that if the sending agent chooses to
> send a message encrypted with a strong algorithm and then send the
> same message encrypted with a weak algorithm, someone watching the
> communications channel could learn the contents of the strongly
> encrypted message simply by decrypting the weakly encrypted message.



## §3 Creating S/MIME Messages

_Not reproduced: ¶2 (that several formats exist and why; holds the
lowercase `required` of line 1185), ¶3 (the reader is expected to
understand MIME)._

**N-067.** (§3 ¶1) _[implied]_ — lines 1162–1173

> This section describes the S/MIME message formats and how they are
> created.  S/MIME messages are a combination of MIME bodies and CMS
> content types.  Several media types as well as several CMS content
> types are used.  The data to be secured is always a canonical MIME
> entity.  The MIME entity and other data, such as certificates and
> algorithm identifiers, are given to CMS processing facilities that
> produce a CMS object.  Finally, the CMS object is wrapped in MIME.
> The "Enhanced Security Services for S/MIME" documents [ESS] provide
> descriptions of how nested, secured S/MIME messages are formatted.
> ESS provides a description of how a triple-wrapped S/MIME message is
> formatted using multipart/signed and application/pkcs7-mime for the
> signatures.

### §3.1 Preparing the MIME Entity for Signing, Enveloping, or Compressing

**N-068.** (§3.1 ¶1) _[implied]_ — lines 1194–1205

> S/MIME is used to secure MIME entities.  A MIME message is composed
> of a MIME header and a MIME body.  A body can consist of a single
> MIME entity or a tree of MIME entities (rooted with a multipart).
> S/MIME can be used to secure either a single MIME entity or a tree of
> MIME entities.  These entities can be in locations other than the
> root.  S/MIME can be applied multiple times to different entities in
> a single message.  A MIME entity that is the whole message includes
> only the MIME message headers and MIME body and does not include the
> rfc822 header.  Note that S/MIME can also be used to secure MIME
> entities used in applications other than Internet mail.  For cases
> where protection of the rfc822 header is required, the use of the
> message/rfc822 media type is explained later in this section.

**N-069.** (§3.1 ¶2) _[lowercase]_ — lines 1207–1214

> The MIME entity that is secured and described in this section can be
> thought of as the "inside" MIME entity.  That is, it is the
> "innermost" object in what is possibly a larger MIME message.
> Processing "outside" MIME entities into CMS EnvelopedData,
> CompressedData, and AuthEnvelopedData content types is described in
> Sections 3.2 and 3.5.  Other documents define additional CMS content
> types; those documents should be consulted for processing those CMS
> content types.

**N-070.** (§3.1 ¶3) _[implied]_ — lines 1216–1221

> The procedure for preparing a MIME entity is given in [MIME-SPEC].
> The same procedure is used here with some additional restrictions
> when signing.  The description of the procedures from [MIME-SPEC] is
> repeated here, but it is suggested that the reader refer to those
> documents for the exact procedures.  This section also describes
> additional requirements.

**N-071.** (§3.1 ¶4) _[lowercase]_ — lines 1223–1230

> A single procedure is used for creating MIME entities that are to
> have any combination of signing, enveloping, and compressing applied.
> Some additional steps are recommended to defend against known
> corruptions that can occur during mail transport that are of
> particular importance for clear-signing using the multipart/signed
> format.  It is recommended that these additional steps be performed
> on enveloped messages, or signed and enveloped messages, so that the
> messages can be forwarded to any environment without modification.

**N-072.** (§3.1 ¶5) _[implied]_ — lines 1239–1241

> These steps are descriptive rather than prescriptive.  The
> implementer is free to use any procedure as long as the result is
> the same.

**N-073.** (§3.1 ¶6–¶8) _[implied]_ — lines 1243–1249

```
   Step 1.  The MIME entity is prepared according to local conventions.

   Step 2.  The leaf parts of the MIME entity are converted to
            canonical form.

   Step 3.  Appropriate transfer encoding is applied to the leaves
            of the MIME entity.
```

**N-074.** (§3.1 ¶9) _[implied]_ — lines 1251–1254

> When an S/MIME message is received, the security services on the
> message are processed, and the result is the MIME entity.  That MIME
> entity is typically passed to a MIME-capable user agent where it is
> further decoded and presented to the user or receiving application.

**N-075.** (§3.1 ¶10) — lines 1256–1264

> In order to protect outer, non-content-related message header fields
> (for instance, the "Subject", "To", "From", and "Cc" fields), the
> sending client MAY wrap a full MIME message in a message/rfc822
> wrapper in order to apply S/MIME security services to these header
> fields.  It is up to the receiving client to decide how to present
> this "inner" header along with the unprotected "outer" header.  Given
> the security difference between headers, it is RECOMMENDED that the
> receiving client provide a distinction between header fields,
> depending on where they are located.

**N-076.** (§3.1 ¶11) — lines 1266–1270

> When an S/MIME message is received, if the top-level protected MIME
> entity has a Content-Type of message/rfc822, it can be assumed that
> the intent was to provide header protection.  This entity SHOULD be
> presented as the top-level message, taking into account
> header-merging issues as previously discussed.

#### §3.1.1 Canonicalization

**N-077.** (§3.1.1 ¶1) — lines 1274–1278

> Each MIME entity MUST be converted to a canonical form that is
> uniquely and unambiguously representable in the environment where the
> signature is created and the environment where the signature will be
> verified.  MIME entities MUST be canonicalized for enveloping and
> compressing as well as signing.

**N-078.** (§3.1.1 ¶2) — lines 1280–1286

> The exact details of canonicalization depend on the actual media type
> and subtype of an entity and are not described here.  Instead, the
> standard for the particular media type SHOULD be consulted.  For
> example, canonicalization of type text/plain is different from
> canonicalization of audio/basic.  Other than text types, most types
> have only one representation, regardless of computing platform or
> environment, that can be considered their canonical representation.

**N-079.** (§3.1.1 ¶3) _[implied]_ — lines 1295–1296

> In general, canonicalization will be performed by the non-security
> part of the sending agent rather than the S/MIME implementation.

**N-080.** (§3.1.1 ¶4) — lines 1298–1304

> The most common and important canonicalization is for text, which is
> often represented differently in different environments.  MIME
> entities of major type "text" MUST have both their line endings and
> character set canonicalized.  The line ending MUST be the pair of
> characters <CR><LF>, and the charset SHOULD be a registered charset
> [CHARSETS].  The details of the canonicalization are specified in
> [MIME-SPEC].

**N-081.** (§3.1.1 ¶5) — lines 1306–1309

> Note that some charsets such as ISO-2022 have multiple
> representations for the same characters.  When preparing such text
> for signing, the canonical representation specified for the charset
> MUST be used.

#### §3.1.2 Transfer Encoding

**N-082.** (§3.1.2 ¶1) _[lowercase]_ — lines 1313–1317

> When generating any of the secured MIME entities below, except the
> signing using the multipart/signed format, no transfer encoding is
> required at all.  S/MIME implementations MUST be able to deal with
> binary MIME objects.  If no Content-Transfer-Encoding header field is
> present, the transfer encoding is presumed to be 7BIT.

**N-083.** (§3.1.2 ¶2) — lines 1319–1330

> As a rule, S/MIME implementations SHOULD use transfer encoding as
> described in Section 3.1.3 for all MIME entities they secure.  The
> reason for securing only 7-bit MIME entities, even for enveloped data
> that is not exposed to the transport, is that it allows the MIME
> entity to be handled in any environment without changing it.  For
> example, a trusted gateway might remove the envelope, but not the
> signature, of a message, and then forward the signed message on to
> the end recipient so that they can verify the signatures directly.
> If the transport internal to the site is not 8-bit clean, such as on
> a wide-area network with a single mail gateway, verifying the
> signature will not be possible unless the original MIME entity was
> only 7-bit data.

**N-084.** (§3.1.2 ¶3) — lines 1332–1341

> In the case where S/MIME implementations can determine that all
> intended recipients are capable of handling inner (all but the
> outermost) binary MIME objects, implementations SHOULD use binary
> encoding as opposed to a 7-bit-safe transfer encoding for the inner
> entities.  The use of a 7-bit-safe encoding (such as base64)
> unnecessarily expands the message size.  Implementations MAY
> determine that recipient implementations are capable of
> handling inner binary MIME entities by (1) interpreting the
> id-cap-preferBinaryInside SMIMECapabilities attribute, (2) prior
> agreement, or (3) other means.

**N-085.** (§3.1.2 ¶4) — lines 1351–1354

> If one or more intended recipients are unable to handle inner binary
> MIME objects or if this capability is unknown for any of the intended
> recipients, S/MIME implementations SHOULD use transfer encoding as
> described in Section 3.1.3 for all MIME entities they secure.

#### §3.1.3 Transfer Encoding for Signing Using multipart/signed

_Not reproduced: ¶2–¶5 (why the 7-bit requirement exists, and the three
options of a transfer agent that cannot carry 8-bit data; motivation)._

**N-086.** (§3.1.3 ¶1) — lines 1358–1364

> If a multipart/signed entity is ever to be transmitted over the
> standard Internet SMTP infrastructure or other transport that is
> constrained to 7-bit text, it MUST have transfer encoding applied so
> that it is represented as 7-bit text.  MIME entities that are already
> 7-bit data need no transfer encoding.  Entities such as 8-bit text
> and binary data can be encoded with quoted-printable or base64
> transfer encoding.

**N-087.** (§3.1.3 ¶6) _[implied]_ — lines 1384–1388

> [RFC1847] prohibits an agent from changing the transfer encoding of
> the first part of a multipart/signed message.  If a compliant agent
> that cannot transmit 8-bit or binary data encountered a
> multipart/signed message with 8-bit or binary data in the first part,
> it would have to return the message to the sender as undeliverable.

#### §3.1.4 Sample Canonical MIME Entity

_Not reproduced: ¶2 (`Note that this example is not an example of an S/MIME
message.`) and the sample multipart/mixed entity that follows it (lines
1409–1437; example)._

**N-088.** (§3.1.4 ¶1) — lines 1392–1397

> This example shows a multipart/mixed message with full transfer
> encoding.  This message contains a text part and an attachment.  The
> sample message text includes characters that are not ASCII and thus
> need to be transfer encoded.  Though not shown here, the end of each
> line is <CR><LF>.  The line ending of the MIME headers, the text, and
> the transfer-encoded parts all MUST be <CR><LF>.

### §3.2 The application/pkcs7-mime Media Type

**N-089.** (§3.2 ¶1) _[implied]_ — lines 1441–1445

> The application/pkcs7-mime media type is used to carry CMS content
> types, including EnvelopedData, SignedData, and CompressedData.  The
> details of constructing these entities are described in subsequent
> sections.  This section describes the general characteristics of the
> application/pkcs7-mime media type.

**N-090.** (§3.2 ¶2) — lines 1447–1450

> The carried CMS object always contains a MIME entity that is prepared
> as described in Section 3.1 if the eContentType is id-data.  Other
> contents MAY be carried when the eContentType contains different
> values.  See [ESS] for an example of this with signed receipts.

**N-091.** (§3.2 ¶3) _[implied]_ _[crosses page break]_ — lines 1452–1464

> Since CMS content types are binary data, in most cases base64
> transfer encoding is appropriate -- in particular, when used with
> SMTP transport.  The transfer encoding used depends on the transport
> through which the object is to be sent and is not a characteristic of
> the media type.

**N-092.** (§3.2 ¶4) _[implied]_ — lines 1466–1469

> Note that this discussion refers to the transfer encoding of the CMS
> object or "outside" MIME entity.  It is completely distinct from, and
> unrelated to, the transfer encoding of the MIME entity secured by the
> CMS object -- the "inside" object, which is described in Section 3.1.

**N-093.** (§3.2 ¶5) _[lowercase]_ — lines 1471–1477

> Because there are several types of application/pkcs7-mime objects, a
> sending agent SHOULD do as much as possible to help a receiving agent
> know about the contents of the object without forcing the receiving
> agent to decode the ASN.1 for the object.  The Content-Type header
> field of all application/pkcs7-mime objects SHOULD include the
> optional "smime-type" parameter, as described in the following
> sections.

#### §3.2.1 The name and filename Parameters

**N-094.** (§3.2.1 ¶1–¶2) _[lowercase]_ _[table]_ — lines 1481–1496

```
   For application/pkcs7-mime, sending agents SHOULD emit the
   optional "name" parameter to the Content-Type field for compatibility
   with older systems.  Sending agents SHOULD also emit the optional
   Content-Disposition field [RFC2183] with the "filename" parameter.
   If a sending agent emits the above parameters, the value of the
   parameters SHOULD be a filename with the appropriate extension:

                                                                File
   Media Type                                                Extension
   -------------------------------------------------------------------
   application/pkcs7-mime (SignedData, EnvelopedData,           .p7m
      AuthEnvelopedData)
   application/pkcs7-mime (degenerate SignedData certificate    .p7c
      management message)
   application/pkcs7-mime (CompressedData)                      .p7z
   application/pkcs7-signature (SignedData)                     .p7s
```

**N-095.** (§3.2.1 ¶3) — lines 1498–1502

> In addition, the filename SHOULD be limited to eight characters
> followed by a three-letter extension.  The eight-character filename
> base can be any distinct name; the use of the filename base "smime"
> SHOULD be used to indicate that the MIME entity is associated with
> S/MIME.

**N-096.** (§3.2.1 ¶4) _[crosses page break]_ — lines 1504–1525

> Including a filename serves two purposes.  It facilitates easier use
> of S/MIME objects as files on disk.  It also can convey type
> information across gateways.  When a MIME entity of type
> application/pkcs7-mime (for example) arrives at a gateway that has no
> special knowledge of S/MIME, it will default the entity's media type
> to application/octet-stream and treat it as a generic attachment,
> thus losing the type information.  However, the suggested filename
> for an attachment is often carried across a gateway.  This often
> allows the receiving systems to determine the appropriate application
> to hand the attachment off to -- in this case, a standalone S/MIME
> processing application.  Note that this mechanism is provided as a
> convenience for implementations in certain environments.  A proper
> S/MIME implementation MUST use the media types and MUST NOT rely on
> the file extensions.

#### §3.2.2 The smime-type Parameter

**N-097.** (§3.2.2 ¶1–¶2) _[lowercase]_ _[table]_ — lines 1529–1541

```
   The application/pkcs7-mime content type defines the optional
   "smime-type" parameter.  The intent of this parameter is to convey
   details about the security applied (signed or enveloped) along with
   information about the contained content.  This specification defines
   the following smime-types.

       Name                   CMS Type              Inner Content
       ----------------------------------------------------------
       enveloped-data         EnvelopedData         id-data
       signed-data            SignedData            id-data
       certs-only             SignedData            id-data
       compressed-data        CompressedData        id-data
       authEnveloped-data     AuthEnvelopedData     id-data
```

**N-098.** (§3.2.2 ¶3–¶6) _[lowercase]_ — lines 1543–1559

```
   In order for consistency to be obtained with future specifications,
   the following guidelines SHOULD be followed when assigning a new
   smime-type parameter.

   1.  If both signing and encryption can be applied to the content,
       then three values for smime-type SHOULD be assigned: "signed-*",
       "authEnv-*", and "enveloped-*".  If one operation can be
       assigned, then this can be omitted.  Thus, since "certs-only" can
       only be signed, "signed-" is omitted.

   2.  A common string for a content OID SHOULD be assigned.  We use
       "data" for the id-data content OID when MIME is the inner
       content.

   3.  If no common string is assigned, then the common string of
       "OID.<oid>" is recommended (for example,
       "OID.2.16.840.1.101.3.4.1.2" would be AES-128 CBC).
```

**N-099.** (§3.2.2 ¶7) _[implied]_ — lines 1561–1564

> It is explicitly intended that this field be a suitable hint for mail
> client applications to indicate whether a message is "signed",
> "authEnveloped", or "enveloped" without having to tunnel into the CMS
> payload.

**N-100.** (§3.2.2 ¶8) _[implied]_ — lines 1575–1576

> A registry for additional smime-type parameter values has been
> defined in [RFC7114].

### §3.3 Creating an Enveloped-Only Message

_Not reproduced: ¶7 (`A sample message would be:`) and the sample message
that follows it (lines 1611–1621; example)._

**N-101.** (§3.3 ¶1) _[implied]_ — lines 1580–1587

> This section describes the format for enveloping a MIME entity
> without signing it.  It is important to note that sending enveloped
> but not signed messages does not provide for data integrity.  The
> "enveloped-only" structure does not support authenticated symmetric
> algorithms.  Use the "authenticated enveloped" structure for these
> algorithms.  Thus, it is possible to replace ciphertext in such a way
> that the processed message will still be valid, but the meaning can
> be altered.

**N-102.** (§3.3 ¶2–¶5) — lines 1589–1603

```
   Step 1.  The MIME entity to be enveloped is prepared according to
            Section 3.1.

   Step 2.  The MIME entity and other required data are processed into a
            CMS object of type EnvelopedData.  In addition to encrypting
            a copy of the content-encryption key (CEK) for each
            recipient, a copy of the CEK SHOULD be encrypted for the
            originator and included in the EnvelopedData (see [RFC5652],
            Section 6).

   Step 3.  The EnvelopedData object is wrapped in a CMS ContentInfo
            object.

   Step 4.  The ContentInfo object is inserted into an
            application/pkcs7-mime MIME entity.
```

**N-103.** (§3.3 ¶6) _[implied]_ — lines 1605–1607

> The smime-type parameter for enveloped-only messages is
> "enveloped-data".  The file extension for this type of message
> is ".p7m".

### §3.4 Creating an Authenticated Enveloped-Only Message

_Not reproduced: ¶7 (`A sample message would be:`) and the sample message
that follows it (lines 1689–1713; example)._

**N-104.** (§3.4 ¶1) _[implied]_ — lines 1633–1643

> This section describes the format for enveloping a MIME entity
> without signing it.  Authenticated enveloped messages provide
> confidentiality and data integrity.  It is important to note that
> sending authenticated enveloped messages does not provide for proof
> of origination when using S/MIME.  It is possible for a third party
> to replace ciphertext in such a way that the processed message will
> still be valid, but the meaning can be altered.  However, this is
> substantially more difficult than it is for an enveloped-only
> message, as the algorithm does provide a level of authentication.
> Any recipient for whom the message is encrypted can replace it
> without detection.

**N-105.** (§3.4 ¶2–¶5) — lines 1645–1658

```
   Step 1.  The MIME entity to be enveloped is prepared according to
            Section 3.1.

   Step 2.  The MIME entity and other required data are processed into a
            CMS object of type AuthEnvelopedData.  In addition to
            encrypting a copy of the CEK for each recipient, a copy of
            the CEK SHOULD be encrypted for the originator and included
            in the AuthEnvelopedData (see [RFC5083]).

   Step 3.  The AuthEnvelopedData object is wrapped in a CMS ContentInfo
            object.

   Step 4.  The ContentInfo object is inserted into an
            application/pkcs7-mime MIME entity.
```

**N-106.** (§3.4 ¶6) _[implied]_ — lines 1660–1662

> The smime-type parameter for authenticated enveloped-only messages is
> "authEnveloped-data".  The file extension for this type of message
> is ".p7m".

### §3.5 Creating a Signed-Only Message

**N-107.** (§3.5 ¶1–¶4) — lines 1717–1724

```
   There are two formats for signed messages defined for S/MIME:

   -  application/pkcs7-mime with SignedData.

   -  multipart/signed.

   In general, the multipart/signed form is preferred for sending, and
   receiving agents MUST be able to handle both.
```

#### §3.5.1 Choosing a Format for Signed-Only Messages

**N-108.** (§3.5.1 ¶1) _[implied]_ — lines 1745–1749

> There are no hard-and-fast rules as to when a particular signed-only
> format is chosen.  It depends on the capabilities of all the
> receivers and the relative importance of receivers with S/MIME
> facilities being able to verify the signature versus the importance
> of receivers without S/MIME software being able to view the message.

**N-109.** (§3.5.1 ¶2) _[implied]_ — lines 1751–1757

> Messages signed using the multipart/signed format can always be
> viewed by the receiver whether or not they have S/MIME software.
> They can also be viewed whether they are using a MIME-native user
> agent or they have messages translated by a gateway.  In this
> context, "be viewed" means the ability to process the message
> essentially as if it were not a signed message, including any other
> MIME structure the message might have.

**N-110.** (§3.5.1 ¶3) _[implied]_ — lines 1759–1763

> Messages signed using the SignedData format cannot be viewed by a
> recipient unless they have S/MIME facilities.  However, the
> SignedData format protects the message content from being changed by
> benign intermediate agents.  Such agents might do line wrapping or
> content-transfer encoding changes that would break the signature.

#### §3.5.2 Signing Using application/pkcs7-mime with SignedData

_Not reproduced: ¶7 (`A sample message would be:`) and the sample message
that follows it (lines 1801–1824; example)._

**N-111.** (§3.5.2 ¶1–¶5) _[implied]_ — lines 1767–1779

```
   This signing format uses the application/pkcs7-mime media type.  The
   steps to create this format are as follows:

   Step 1.  The MIME entity is prepared according to Section 3.1.

   Step 2.  The MIME entity and other required data are processed into a
            CMS object of type SignedData.

   Step 3.  The SignedData object is wrapped in a CMS ContentInfo
            object.

   Step 4.  The ContentInfo object is inserted into an
            application/pkcs7-mime MIME entity.
```

**N-112.** (§3.5.2 ¶6) _[implied]_ — lines 1781–1783

> The smime-type parameter for messages using application/pkcs7-mime
> with SignedData is "signed-data".  The file extension for this type
> of message is ".p7m".

#### §3.5.3 Signing Using the multipart/signed Format

**N-113.** (§3.5.3 ¶1) _[implied]_ — lines 1828–1834

> This format is a clear-signing format.  Recipients without any S/MIME
> or CMS processing facilities are able to view the message.  It makes
> use of the multipart/signed media type described in [RFC1847].  The
> multipart/signed media type has two parts.  The first part contains
> the MIME entity that is signed; the second part contains the
> "detached signature" CMS SignedData object in which the
> encapContentInfo eContent field is absent.

##### §3.5.3.1 The application/pkcs7-signature Media Type

**N-114.** (§3.5.3.1 ¶1) — lines 1838–1841

> This media type always contains a CMS ContentInfo containing a single
> CMS object of type SignedData.  The SignedData encapContentInfo
> eContent field MUST be absent.  The signerInfos field contains the
> signatures for the MIME entity.

**N-115.** (§3.5.3.1 ¶2) _[implied]_ — lines 1843–1844

> The file extension for signed-only messages using
> application/pkcs7-signature is ".p7s".

##### §3.5.3.2 Creating a multipart/signed Message

**N-116.** (§3.5.3.2 ¶1–¶5) _[implied]_ — lines 1857–1874

```
   Step 1.  The MIME entity to be signed is prepared according to
            Section 3.1, taking special care for clear-signing.

   Step 2.  The MIME entity is presented to CMS processing in order to
            obtain an object of type SignedData in which the
            encapContentInfo eContent field is absent.

   Step 3.  The MIME entity is inserted into the first part of a
            multipart/signed message with no processing other than that
            described in Section 3.1.

   Step 4.  Transfer encoding is applied to the "detached signature" CMS
            SignedData object, and it is inserted into a MIME entity of
            type application/pkcs7-signature.

   Step 5.  The MIME entity of the application/pkcs7-signature is
            inserted into the second part of the multipart/signed
            entity.
```

**N-117.** (§3.5.3.2 ¶6) _[lowercase]_ — lines 1876–1877

> The multipart/signed Content-Type has two required parameters: the
> protocol parameter and the micalg parameter.

**N-118.** (§3.5.3.2 ¶7) _[lowercase]_ — lines 1879–1882

> The protocol parameter MUST be "application/pkcs7-signature".  Note
> that quotation marks are required around the protocol parameter
> because MIME requires that the "/" character in the parameter value
> MUST be quoted.

**N-119.** (§3.5.3.2 ¶8–¶10) _[table]_ — lines 1911–1931

```
   The micalg parameter allows for one-pass processing when the
   signature is being verified.  The value of the micalg parameter is
   dependent on the message digest algorithm(s) used in the calculation
   of the Message Integrity Check.  If multiple message digest
   algorithms are used, they MUST be separated by commas per [RFC1847].
   The values to be placed in the micalg parameter SHOULD be from the
   following:

        Algorithm      Value Used
        -----------------------------------------------------------
        MD5*           md5
        SHA-1*         sha-1
        SHA-224        sha-224
        SHA-256        sha-256
        SHA-384        sha-384
        SHA-512        sha-512
        Any other      (defined separately in the algorithm profile
                        or "unknown" if not defined)

   *Note: MD5 and SHA-1 are historical and no longer considered secure.
   See Appendix B for details.
```

**N-120.** (§3.5.3.2 ¶11) — lines 1933–1938

> (Historical note: Some early implementations of S/MIME emitted and
> expected "rsa-md5", "rsa-sha1", and "sha1" for the micalg parameter.)
> Receiving agents SHOULD be able to recover gracefully from a micalg
> parameter value that they do not recognize.  Future values for this
> parameter will be taken from the IANA "Hash Function Textual Names"
> registry.

##### §3.5.3.3 Sample multipart/signed Message

_No entries — the sample multipart/signed message (lines 1969–1992) and
the bytes of its digested first part (lines 1994–1998) are an example, not
a normative statement._

### §3.6 Creating a Compressed-Only Message

_Not reproduced: ¶7 (`A sample message would be:`) and the sample message
that follows it (lines 2035–2040; example)._

**N-121.** (§3.6 ¶1) _[implied]_ — lines 2002–2006

> This section describes the format for compressing a MIME entity.
> Please note that versions of S/MIME prior to version 3.1 did not
> specify any use of CompressedData and will not recognize it.  The use
> of a capability to indicate the ability to receive CompressedData is
> described in [RFC3274] and is the preferred method for compatibility.

**N-122.** (§3.6 ¶2–¶5) _[implied]_ _[crosses page break]_ — lines 2008–2027

```
   Step 1.  The MIME entity to be compressed is prepared according to
            Section 3.1.

   Step 2.  The MIME entity and other required data are processed into a
            CMS object of type CompressedData.

   Step 3.  The CompressedData object is wrapped in a CMS ContentInfo
            object.

   Step 4.  The ContentInfo object is inserted into an
            application/pkcs7-mime MIME entity.
```

**N-123.** (§3.6 ¶6) _[implied]_ — lines 2029–2031

> The smime-type parameter for compressed-only messages is
> "compressed-data".  The file extension for this type of message
> is ".p7z".

### §3.7 Multiple Operations

**N-124.** (§3.7 ¶1) _[implied]_ — lines 2044–2046

> The signed-only, enveloped-only, and compressed-only MIME formats can
> be nested.  This works because these formats are all MIME entities
> that encapsulate other MIME entities.

**N-125.** (§3.7 ¶2) — lines 2048–2050

> An S/MIME implementation MUST be able to receive and process
> arbitrarily nested S/MIME within reasonable resource limits of the
> recipient computer.

**N-126.** (§3.7 ¶3) _[implied]_ — lines 2052–2059

> It is possible to apply any of the signing, encrypting, and
> compressing operations in any order.  It is up to the implementer and
> the user to choose.  When signing first, the signatories are then
> securely obscured by the enveloping.  When enveloping first, the
> signatories are exposed, but it is possible to verify signatures
> without removing the enveloping.  This can be useful in an
> environment where automatic signature verification is desired, as no
> private key material is required to verify a signature.

**N-127.** (§3.7 ¶4) _[implied]_ — lines 2061–2068

> There are security ramifications related to choosing whether to sign
> first or encrypt first.  A recipient of a message that is encrypted
> and then signed can validate that the encrypted block was unaltered
> but cannot determine any relationship between the signer and the
> unencrypted contents of the message.  A recipient of a message that
> is signed and then encrypted can assume that the signed message
> itself has not been altered but that a careful attacker could have
> changed the unauthenticated portions of the encrypted message.

**N-128.** (§3.7 ¶5–¶7) _[implied]_ — lines 2079–2087

```
   When using compression, keep the following guidelines in mind:

   -  Compression of encrypted data that is transferred as binary data
   is discouraged, since it will not yield significant compression.
   Encrypted data that is transferred as base64-encoded data could
   benefit as well.

   -  If a lossy compression algorithm is used with signing, you will
   need to compress first, then sign.
```

### §3.8 Creating a Certificate Management Message

**N-129.** (§3.8 ¶1) _[implied]_ — lines 2091–2093

> The certificate management message or MIME entity is used to
> transport certificates and/or Certificate Revocation Lists (CRLs),
> such as in response to a registration request.

**N-130.** (§3.8 ¶2–¶4) — lines 2095–2104

```
   Step 1.  The certificates and/or CRLs are made available to the CMS
            generating process that creates a CMS object of type
            SignedData.  The SignedData encapContentInfo eContent field
            MUST be absent, and the signerInfos field MUST be empty.

   Step 2.  The SignedData object is wrapped in a CMS ContentInfo
            object.

   Step 3.  The ContentInfo object is enclosed in an
            application/pkcs7-mime MIME entity.
```

**N-131.** (§3.8 ¶5) _[implied]_ — lines 2106–2107

> The smime-type parameter for a certificate management message is
> "certs-only".  The file extension for this type of message is ".p7c".

### §3.9 Registration Requests

**N-132.** (§3.9 ¶1) — lines 2111–2115

> A sending agent that signs messages MUST have a certificate for the
> signature so that a receiving agent can verify the signature.  There
> are many ways of getting certificates, such as through an exchange
> with a certification authority, through a hardware token or diskette,
> and so on.

**N-133.** (§3.9 ¶2) _[implied]_ — lines 2117–2121

> S/MIME v2 [SMIMEv2] specified a method for "registering" public keys
> with certificate authorities using an application/pkcs10 body part.
> Since that time, the IETF PKIX Working Group has developed other
> methods for requesting certificates.  However, S/MIME v4.0 does not
> require a particular certificate request mechanism.

### §3.10 Identifying an S/MIME Message

**N-134.** (§3.10 ¶1) _[implied]_ — lines 2137–2142

> Because S/MIME takes into account interoperation in non-MIME
> environments, several different mechanisms are employed to carry the
> type information, and it becomes a bit difficult to identify S/MIME
> messages.  The following table lists criteria for determining whether
> or not a message is an S/MIME message.  A message is considered an
> S/MIME message if it matches any of the criteria listed below.

**N-135.** (§3.10 ¶2) _[implied]_ — lines 2144–2147

> The file suffix in the table below comes from the "name" parameter in
> the Content-Type header field or the "filename" parameter in the
> Content-Disposition header field.  The MIME parameters that carry the
> file suffix are not listed below.

**N-136.** (§3.10 ¶3) _[implied]_ _[table]_ — lines 2149–2157

```
   Media Type                 Parameters                     File Suffix
   ---------------------------------------------------------------------
   application/pkcs7-mime     N/A                            N/A

   multipart/signed           protocol=                      N/A
                              "application/pkcs7-signature"

   application/octet-stream   N/A                            p7m, p7s,
                                                             p7c, p7z
```



## §4 Certificate Processing

**N-137.** (§4 ¶1) — lines 2161–2166

> A receiving agent MUST provide some certificate retrieval mechanism
> in order to gain access to certificates for recipients of digital
> envelopes.  This specification does not cover how S/MIME agents
> handle certificates -- only what they do after a certificate has been
> validated or rejected.  S/MIME certificate issues are covered in
> [RFC5750].

**N-138.** (§4 ¶2) — lines 2168–2173

> At a minimum, for initial S/MIME deployment, a user agent could
> automatically generate a message to an intended recipient requesting
> that recipient's certificate in a signed return message.  Receiving
> and sending agents SHOULD also provide a mechanism to allow a user to
> "store and protect" certificates for correspondents in such a way as
> to guarantee their later retrieval.

### §4.1 Key Pair Generation

**N-139.** (§4.1 ¶1) — lines 2193–2195

> All key pairs MUST be generated from a good source of
> non-deterministic random input [RFC4086], and the private key MUST be
> protected in a secure fashion.

**N-140.** (§4.1 ¶2) — lines 2197–2198

> An S/MIME user agent MUST NOT generate asymmetric keys less than
> 2048 bits for use with an RSA signature algorithm.

**N-141.** (§4.1 ¶3) _[implied]_ — lines 2200–2202

> For 2048-bit through 4096-bit RSA with SHA-256, see [RFC5754] and
> [FIPS186-4].  The first reference provides the signature algorithm's
> OID, and the second provides the signature algorithm's definition.

**N-142.** (§4.1 ¶4) _[implied]_ — lines 2204–2205

> For RSASSA-PSS with SHA-256, see [RFC4056].  For RSAES-OAEP, see
> [RFC3560].

### §4.2 Signature Generation

**N-143.** (§4.2 ¶1–¶4) _[table]_ — lines 2209–2219

```
   The following are the requirements for an S/MIME agent when
   generating RSA and RSASSA-PSS signatures:

           key size <= 2047 : SHOULD NOT (Note 2)
   2048 <= key size <= 4096 : SHOULD     (Note 1)
   4096 <  key size         : MAY        (Note 1)

   Note 1: See Security Considerations in Section 6.
   Note 2: See Historical Mail Considerations in Appendix B.

   Key sizes for ECDSA and EdDSA are fixed by the curve.
```

### §4.3 Signature Verification

**N-144.** (§4.3 ¶1–¶4) _[table]_ — lines 2223–2233

```
   The following are the requirements for S/MIME receiving agents during
   verification of RSA and RSASSA-PSS signatures:

           key size <= 2047 : SHOULD NOT (Note 2)
   2048 <= key size <= 4096 : MUST       (Note 1)
   4096 <  key size         : MAY        (Note 1)

   Note 1: See Security Considerations in Section 6.
   Note 2: See Historical Mail Considerations in Appendix B.

   Key sizes for ECDSA and EdDSA are fixed by the curve.
```

### §4.4 Encryption

**N-145.** (§4.4 ¶1–¶4) _[table]_ — lines 2249–2260

```
   The following are the requirements for an S/MIME agent when
   establishing keys for content encryption using the RSA and RSA-OAEP
   algorithms:

           key size <= 2047 : SHOULD NOT (Note 2)
   2048 <= key size <= 4096 : SHOULD     (Note 1)
   4096 <  key size         : MAY        (Note 1)

   Note 1: See Security Considerations in Section 6.
   Note 2: See Historical Mail Considerations in Appendix B.

   Key sizes for ECDH are fixed by the curve.
```

### §4.5 Decryption

**N-146.** (§4.5 ¶1–¶4) _[table]_ — lines 2264–2275

```
   The following are the requirements for an S/MIME agent when
   establishing keys for content decryption using the RSA and RSAES-OAEP
   algorithms:

           key size <= 2047 : MAY        (Note 2)
   2048 <= key size <= 4096 : MUST       (Note 1)
   4096 <  key size         : MAY        (Note 1)

   Note 1: See Security Considerations in Section 6.
   Note 2: See Historical Mail Considerations in Appendix B.

   Key sizes for ECDH are fixed by the curve.
```



## §5 IANA Considerations

**N-147.** (§5 ¶1) _[IANA]_ — lines 2279–2283

> This section (1) updates the media type registrations for
> application/pkcs7-mime and application/pkcs7-signature to refer to
> this document as opposed to RFC 5751, (2) adds authEnveloped-data to
> the list of values for smime-type, and (3) updates references from
> RFC 5751 to this document in general.

**N-148.** (§5 ¶2) _[IANA]_ — lines 2285–2286

> Note that other documents can define additional media types for
> S/MIME.

### §5.1 Media Type for application/pkcs7-mime

**N-149.** (§5.1 template) _[IANA]_ — lines 2305–2342

```
   Type name: application

   Subtype Name: pkcs7-mime

   Required Parameters: NONE

   Optional Parameters: smime-type
                        name

   Encoding Considerations: See Section 3 of this document

   Security Considerations: See Section 6 of this document

   Interoperability Considerations: See Sections 1-6 of this document

   Published Specification: RFC 2311, RFC 2633, RFC 5751,
                            and this document

   Applications that use this media type: Security applications

   Fragment identifier considerations: N/A

   Additional information:
       Deprecated alias names for this type: N/A
       Magic number(s): N/A
       File extensions(s): See Section 3.2.1 of this document
       Macintosh file type code(s): N/A

   Person & email address to contact for further information:
      The IESG <iesg@ietf.org>

   Intended usage: COMMON

   Restrictions on usage: NONE

   Author: Sean Turner

   Change Controller: LAMPS working group delegated from the IESG
```

### §5.2 Media Type for application/pkcs7-signature

**N-150.** (§5.2 template) _[IANA]_ — lines 2361–2397

```
   Type name: application

   Subtype Name: pkcs7-signature

   Required Parameters: N/A

   Optional Parameters: N/A

   Encoding Considerations: See Section 3 of this document

   Security Considerations: See Section 6 of this document

   Interoperability Considerations: See Sections 1-6 of this document

   Published Specification: RFC 2311, RFC 2633, RFC 5751,
                            and this document

   Applications that use this media type: Security applications

   Fragment identifier considerations: N/A

   Additional information:
       Deprecated alias names for this type: N/A
       Magic number(s): N/A
       File extensions(s): See Section 3.2.1 of this document
       Macintosh file type code(s): N/A

   Person & email address to contact for further information:
      The IESG <iesg@ietf.org>

   Intended usage: COMMON

   Restrictions on usage: N/A

   Author: Sean Turner

   Change Controller: LAMPS working group delegated from the IESG
```

### §5.3 authEnveloped-data smime-type

**N-151.** (§5.3 template) _[IANA]_ — lines 2417–2422

```
   IANA has registered the following value in the "Parameter Values for
   the smime-type Parameter" registry.

      smime-type value: authEnveloped-data

      Reference: RFC 8551, Section 3.2.2
```

### §5.4 Reference Updates

**N-152.** (§5.4 ¶1) _[IANA]_ — lines 2426–2428

> IANA is to update all references to RFC 5751 to this document.  Known
> registries to be updated are "CoAP Content-Formats" and "media-
> types".



## §6 Security Considerations

_Every block of §6 is reproduced._

**N-153.** (§6 ¶1–¶4) _[implied]_ — lines 2432–2444

```
   Cryptographic algorithms will be broken or weakened over time.
   Implementers and users need to check that the cryptographic
   algorithms listed in this document continue to provide the expected
   level of security.  The IETF from time to time may issue documents
   dealing with the current state of the art.  For example:

   -  The Million Message Attack described in RFC 3218 [RFC3218].

   -  The Diffie-Hellman "small-subgroup" attacks described in RFC 2785
      [RFC2785].

   -  The attacks against hash algorithms described in RFC 4270
      [RFC4270].
```

**N-154.** (§6 ¶5) _[implied]_ — lines 2446–2448

> This specification uses Public-Key Cryptography technologies.  It is
> assumed that the private key is protected to ensure that it is not
> accessed or altered by unauthorized parties.

**N-155.** (§6 ¶6) _[implied]_ — lines 2450–2460

> It is impossible for most people or software to estimate the value of
> a message's content.  Further, it is impossible for most people or
> software to estimate the actual cost of recovering an encrypted
> message's content that is encrypted with a key of a particular size.
> Further, it is quite difficult to determine the cost of a failed
> decryption if a recipient cannot process a message's content.  Thus,
> choosing between different key sizes (or choosing whether to just use
> plaintext) is also impossible for most people or software.  However,
> decisions based on these criteria are made all the time, and
> therefore this specification gives a framework for using those
> estimates in choosing algorithms.

**N-156.** (§6 ¶7) _[lowercase]_ — lines 2471–2478

> The choice of 2048 bits as an RSA asymmetric key size in this
> specification is based on the desire to provide at least 100 bits of
> security.  The key sizes that must be supported to conform to this
> specification seem appropriate for the Internet, based on [RFC3766].
> Of course, there are environments, such as financial and medical
> systems, that may select different key sizes.  For this reason, an
> implementation MAY support key sizes beyond those recommended in this
> specification.

**N-157.** (§6 ¶8) _[implied]_ — lines 2480–2490

> Receiving agents that validate signatures and sending agents that
> encrypt messages need to be cautious of cryptographic processing
> usage when validating signatures and encrypting messages using keys
> larger than those mandated in this specification.  An attacker could
> send certificates with keys that would result in excessive
> cryptographic processing -- for example, keys larger than those
> mandated in this specification, as such keys could swamp the
> processing element.  Agents that use such keys without first
> validating the certificate to a trust anchor are advised to have some
> sort of cryptographic resource management system to prevent such
> attacks.

**N-158.** (§6 ¶9) _[lowercase]_ — lines 2492–2500

> Some cryptographic algorithms such as RC2 offer little actual
> security over sending plaintext.  Other algorithms such as TripleDES
> provide security but are no longer considered to be state of the art.
> S/MIME requires the use of current state-of-the-art algorithms such
> as AES and provides the ability to announce cryptographic
> capabilities to parties with whom you communicate.  This allows the
> sender to create messages that can use the strongest common
> encryption algorithm.  Using algorithms such as RC2 is never
> recommended unless the only alternative is no cryptography.

**N-159.** (§6 ¶10) _[lowercase]_ — lines 2502–2516

> RSA and DSA keys of less than 2048 bits are now considered by many
> experts to be cryptographically insecure (due to advances in
> computing power) and should no longer be used to protect messages.
> Such keys were previously considered secure, so processing previously
> received signed and encrypted mail will often result in the use of
> weak keys.  Implementations that wish to support previous versions of
> S/MIME or process old messages need to consider the security risks
> that result from smaller key sizes (e.g., spoofed messages) versus
> the costs of denial of service.  If an implementation supports
> verification of digital signatures generated with RSA and DSA keys of
> less than 1024 bits, it MUST warn the user.  Implementers should
> consider providing different warnings for newly received messages and
> previously stored messages.  Server implementations (e.g., secure
> mail list servers) where user warnings are not appropriate SHOULD
> reject messages with weak signatures.

**N-160.** (§6 ¶11) — lines 2527–2530

> Implementers SHOULD be aware that multiple active key pairs can be
> associated with a single individual.  For example, one key pair can
> be used to support confidentiality, while a different key pair can be
> used for digital signatures.

**N-161.** (§6 ¶12) — lines 2532–2538

> If a sending agent is sending the same message using different
> strengths of cryptography, an attacker watching the communications
> channel might be able to determine the contents of the strongly
> encrypted message by decrypting the weakly encrypted version.  In
> other words, a sender SHOULD NOT send a copy of a message using
> weaker cryptography than they would use for the original of the
> message.

**N-162.** (§6 ¶13) _[implied]_ — lines 2540–2546

> Modification of the ciphertext in EnvelopedData can go undetected if
> authentication is not also used, which is the case when sending
> EnvelopedData without wrapping it in SignedData or enclosing
> SignedData within it.  This is one of the reasons for moving from
> EnvelopedData to AuthEnvelopedData, as the authenticated encryption
> algorithms provide the authentication without needing the SignedData
> layer.

**N-163.** (§6 ¶14) _[implied]_ — lines 2548–2550

> If an implementation is concerned about compliance with National
> Institute of Standards and Technology (NIST) key size
> recommendations, then see [SP800-57].

**N-164.** (§6 ¶15) _[lowercase]_ — lines 2552–2559

> If messaging environments make use of the fact that a message is
> signed to change the behavior of message processing (examples would
> be running rules or UI display hints), without first verifying that
> the message is actually signed and knowing the state of the
> signature, this can lead to incorrect handling of the message.
> Visual indicators on messages may need to have the signature
> validation code checked periodically if the indicator is supposed to
> give information on the current status of a message.

**N-165.** (§6 ¶16–¶19) _[lowercase]_ _[crosses page break]_ — lines 2561–2596

```
   Many people assume that the use of an authenticated encryption
   algorithm is all that is needed for the sender of the message to be
   authenticated.  In almost all cases, this is not a correct statement.
   There are a number of preconditions that need to hold for an
   authenticated encryption algorithm to provide this service:

   -  The starting key must be bound to a single entity.  The use of a
      group key only would allow for the statement that a message was
      sent by one of the entities that held the key but will not
      identify a specific entity.

   -  The message must have exactly one sender and one recipient.
      Having more than one recipient would allow for the second
      recipient to create a message that the first recipient would
      believe is from the sender by stripping the second recipient from
      the message.

   -  A direct path needs to exist from the starting key to the key used
      as the CEK.  That path needs to guarantee that no third party
      could have seen the resulting CEK.  This means that one needs to
      be using an algorithm that is called a "Direct Encryption" or a
      "Direct Key Agreement" algorithm in other contexts.  This means
      that the starting key is (1) used directly as the CEK or (2) used
      to create a secret that is then transformed into the CEK via a
      KDF step.
```

**N-166.** (§6 ¶20) _[implied]_ — lines 2598–2606

> S/MIME implementations almost universally use ephemeral-static rather
> than static-static key agreement and do not use a shared secret for
> encryption.  This means that the first precondition is not met.
> [RFC6278] defines how to use static-static key agreement with CMS, so
> the first precondition can be met.  Currently, all S/MIME key
> agreement methods derive a key-encryption key (KEK) and wrap a CEK.
> This violates the third precondition above.  New key agreement
> algorithms that directly created the CEK without creating an
> intervening KEK would need to be defined.

**N-167.** (§6 ¶21) _[implied]_ — lines 2608–2615

> Even when all of the preconditions are met and origination of a
> message is established by the use of an authenticated encryption
> algorithm, users need to be aware that there is no way to prove this
> to a third party.  This is because either of the parties can
> successfully create the message (or just alter the content) based on
> the fact that the CEK is going to be known to both parties.  Thus,
> the origination is always built on a presumption that "I did not send
> this message to myself."

**N-168.** (§6 ¶22) _[implied]_ — lines 2617–2624

> All of the authenticated encryption algorithms in this document use
> counter mode for the encryption portion of the algorithm.  This means
> that the length of the plaintext will always be known, as the
> ciphertext length and the plaintext length are always the same.  This
> information can enable passive observers to infer information based
> solely on the length of the message.  Applications for which this is
> a concern need to provide some type of padding so that the length of
> the message does not provide this information.

**N-169.** (§6 ¶23) _[implied]_ _[crosses page break]_ — lines 2626–2641

> When compression is used with encryption, it has the potential to
> provide an additional layer of security.  However, care needs to be
> taken when designing a protocol that relies on using compression, so
> as not to create a compression oracle.  Compression oracle attacks
> require an adaptive input to the process and attack the unknown
> content of a message based on the length of the compressed output.
> This means that no attack on the encryption key is necessarily
> required.

**N-170.** (§6 ¶24) _[lowercase]_ — lines 2643–2656

> A recent paper on S/MIME and OpenPGP email security [Efail] has
> pointed out a number of problems with the current S/MIME
> specifications and how people have implemented mail clients.  Due to
> the nature of how CBC mode operates, the modes allow for malleability
> of plaintexts.  This malleability allows for attackers to make
> changes in the ciphertext and, if parts of the plaintext are known,
> create arbitrary blocks of plaintext.  These changes can be made
> without the weak integrity check in CBC mode being triggered.  This
> type of attack can be prevented by the use of an Authenticated
> Encryption with Associated Data (AEAD) algorithm with a more robust
> integrity check on the decryption process.  It is therefore
> recommended that mail systems migrate to using AES-GCM as quickly as
> possible and that the decrypted content not be acted on prior to
> finishing the integrity check.

**N-171.** (§6 ¶25) — lines 2658–2665

> The other attack that is highlighted in [Efail] is due to an error in
> how mail clients deal with HTML and multipart/mixed messages.
> Clients MUST require that a text/html content type be a complete HTML
> document (per [RFC1866]).  Clients SHOULD treat each of the different
> pieces of the multipart/mixed construct as being of different
> origins.  Clients MUST treat each encrypted or signed piece of a MIME
> message as being of different origins both from unprotected content
> and from each other.



## §7 References

### §7.1 Reference Conventions

_Reproduced because the requirements cite these composite labels
([CMS] in N-001, [ESS], [MIME-SPEC], [SMIMEv4]) and they resolve only here._

**N-172.** (§7.1 ¶1–¶9) _[implied]_ _[crosses page break]_ — lines 2671–2702

```
   [ASN.1] refers to [X.680], [X.681], [X.682], and [X.683].

   [CMS] refers to [RFC5083] and [RFC5652].

   [ESS] refers to [RFC2634] and [RFC5035].

   [MIME-SPEC] refers to [RFC2045], [RFC2046], [RFC2047], [RFC2049],
   [RFC6838], and [RFC4289].

   [SMIMEv2] refers to [RFC2311], [RFC2312], [RFC2313], [RFC2314], and
   [RFC2315].

   [SMIMEv3] refers to [RFC2630], [RFC2631], [RFC2632], [RFC2633],
   [RFC2634], and [RFC5035].

   [SMIMEv3.1] refers to [RFC2634], [RFC5035], [RFC5652], [RFC5750], and
   [RFC5751].

   [SMIMEv3.2] refers to [RFC2634], [RFC3850], [RFC3851], [RFC3852], and
   [RFC5035].

   [SMIMEv4] refers to [RFC2634], [RFC5035], [RFC5652], [RFC8550], and
   this document.
```

### §7.2 Normative References

_No entries — bibliography._

### §7.3 Informative References

_No entries — bibliography._



## §A ASN.1 Module

**N-173.** (§A ¶1) _[implied]_ — lines 3145–3150

> Note: The ASN.1 module contained herein is unchanged from RFC 5751
> [SMIMEv2] and RFC 3851 [SMIMEv3.1], with the exception of a change to
> the preferBinaryInside ASN.1 comment in RFC 3851 [SMIMEv3.1].  If a
> module is needed that is compatible with current ASN.1 standards, one
> can be found in [RFC6268].  This module uses the 1988 version
> of ASN.1.

**N-174.** (§A module) _[ASN.1]_ _[crosses page break]_ — lines 3152–3243

```
   SecureMimeMessageV3dot1

     { iso(1) member-body(2) us(840) rsadsi(113549)
            pkcs(1) pkcs-9(9) smime(16) modules(0) msg-v3dot1(21) }

   DEFINITIONS IMPLICIT TAGS ::=

   BEGIN

   IMPORTS

   -- Cryptographic Message Syntax [CMS]
      SubjectKeyIdentifier, IssuerAndSerialNumber,
      RecipientKeyIdentifier
          FROM  CryptographicMessageSyntax
                { iso(1) member-body(2) us(840) rsadsi(113549)
                  pkcs(1) pkcs-9(9) smime(16) modules(0) cms-2001(14) };

   -- id-aa is the arc with all new authenticated and unauthenticated
   -- attributes produced by the S/MIME Working Group.

   id-aa OBJECT IDENTIFIER ::= {iso(1) member-body(2) usa(840)
           rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) attributes(2)}

   -- S/MIME Capabilities provides a method of broadcasting the
   -- symmetric capabilities understood.  Algorithms SHOULD be ordered
   -- by preference and grouped by type.

   smimeCapabilities OBJECT IDENTIFIER ::= {iso(1) member-body(2)
           us(840) rsadsi(113549) pkcs(1) pkcs-9(9) 15}

   SMIMECapability ::= SEQUENCE {
      capabilityID OBJECT IDENTIFIER,
      parameters ANY DEFINED BY capabilityID OPTIONAL }

   SMIMECapabilities ::= SEQUENCE OF SMIMECapability

   -- Encryption Key Preference provides a method of broadcasting the
   -- preferred encryption certificate.

   id-aa-encrypKeyPref OBJECT IDENTIFIER ::= {id-aa 11}

   SMIMEEncryptionKeyPreference ::= CHOICE {
      issuerAndSerialNumber   [0] IssuerAndSerialNumber,
      receipentKeyId          [1] RecipientKeyIdentifier,
      subjectAltKeyIdentifier [2] SubjectKeyIdentifier
   }

   -- "receipentKeyId" is spelled incorrectly but is kept for
   -- historical reasons.

   id-smime OBJECT IDENTIFIER ::= { iso(1) member-body(2) us(840)
           rsadsi(113549) pkcs(1) pkcs-9(9) 16 }

   id-cap  OBJECT IDENTIFIER ::= { id-smime 11 }

   -- The preferBinaryInside OID indicates an ability to receive
   -- messages with binary encoding inside the CMS wrapper.
   -- The preferBinaryInside attribute's value field is ABSENT.

   id-cap-preferBinaryInside  OBJECT IDENTIFIER ::= { id-cap 1 }

   -- The following is a list of OIDs to be used with S/MIME v3.

   -- Signature Algorithms Not Found in [RFC3370], [RFC5754], [RFC4056],
   -- and [RFC3560]

   --
   -- md2WithRSAEncryption OBJECT IDENTIFIER ::=
   --    {iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-1(1)
   --     2}

   --
   -- Other Signed Attributes
   --
   -- signingTime OBJECT IDENTIFIER ::=
   --    {iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9)
   --     5}
   --    See [CMS] for a description of how to encode the attribute
   --    value.

   SMIMECapabilitiesParametersForRC2CBC ::= INTEGER
   --        (RC2 Key Length (number of bits))

   END
```



## §B Historic Mail Considerations

_Not reproduced: ¶2 (references to obsoleted documents are intentional;
editorial)._

**N-175.** (§B ¶1) _[implied]_ — lines 3257–3263

> Over the course of updating the S/MIME specifications, the set of
> recommended algorithms has been modified each time the documents have
> been updated.  This means that if a user has historic emails and
> their user agent has been updated to only support the current set of
> recommended algorithms, some of those old emails will no longer be
> accessible.  It is strongly suggested that user agents implement some
> of the following algorithms for dealing with historic emails.

### §B.1 DigestAlgorithmIdentifier

**N-176.** (§B.1 ¶1–¶3) _[implied]_ — lines 3271–3281

```
   The following algorithms have been called out for some level of
   support by previous S/MIME specifications:

   -  SHA-1 was dropped in [SMIMEv4].  SHA-1 is no longer considered to
      be secure, as it is no longer collision resistant.  The IETF
      statement on SHA-1 can be found in [RFC6194], but it is out of
      date relative to the most recent advances.

   -  MD5 was dropped in [SMIMEv4].  MD5 is no longer considered to be
      secure, as it is no longer collision resistant.  Details can be
      found in [RFC6151].
```

### §B.2 Signature Algorithms

**N-177.** (§B.2 ¶1–¶6) _[lowercase]_ _[crosses page break]_ — lines 3285–3336

```
   There are a number of problems with validating signatures on
   sufficiently historic messages.  For this reason, it is strongly
   suggested that user agents treat these signatures differently from
   those on current messages.  These problems include the following:

   -  Certification authorities are not required to keep certificates on
      a CRL beyond one update after a certificate has expired.  This
      means that unless CRLs are cached as part of the message it is not
      always possible to check to see if a certificate has been revoked.
      The same problems exist with Online Certificate Status Protocol
      (OCSP) responses, as they may be based on a CRL rather than on the
      certificate database.

   -  RSA and DSA keys of less than 2048 bits are now considered by many
      experts to be cryptographically insecure (due to advances in
      computing power).  Such keys were previously considered secure, so
      the processing of historic signed messages will often result in
      the use of weak keys.  Implementations that wish to support
      previous versions of S/MIME or process old messages need to
      consider the security risks that result from smaller key sizes
      (e.g., spoofed messages) versus the costs of denial of service.

      [SMIMEv3.1] set the lower limit on suggested key sizes for
      creating and validation at 1024 bits.  Prior to that, the lower
      bound on key sizes was 512 bits.

   -  Hash functions used to validate signatures on historic messages
      may no longer be considered to be secure (see below).  While there
      are not currently any known practical pre-image or second
      pre-image attacks against MD5 or SHA-1, the fact that they are no
      longer considered to be collision resistant implies that the
      security levels of the signatures are generally considered
      suspect.  If a message is known to be historic and it has been in
      the possession of the client for some time, then it might still be
      considered to be secure.

   -  The previous two issues apply to the certificates used to validate
      the binding of the public key to the identity that signed the
      message as well.
```

**N-178.** (§B.2 ¶7–¶10) _[implied]_ — lines 3338–3351

```
   The following algorithms have been called out for some level of
   support by previous S/MIME specifications:

   -  RSA with MD5 was dropped in [SMIMEv4].  MD5 is no longer
      considered to be secure, as it is no longer collision resistant.
      Details can be found in [RFC6151].

   -  RSA and DSA with SHA-1 were dropped in [SMIMEv4].  SHA-1 is no
      longer considered to be secure, as it is no longer collision
      resistant.  The IETF statement on SHA-1 can be found in [RFC6194],
      but it is out of date relative to the most recent advances.

   -  DSA with SHA-256 was dropped in [SMIMEv4].  DSA has been replaced
      by elliptic curve versions.
```

**N-179.** (§B.2 ¶11–¶14) _[lowercase]_ — lines 3367–3380

```
   As requirements for "mandatory to implement" have changed over time,
   some issues have been created that can cause interoperability
   problems:

   -  S/MIME v2 clients are only required to verify digital signatures
      using the rsaEncryption algorithm with SHA-1 or MD5 and might not
      implement id-dsa-with-sha1 or id-dsa at all.

   -  S/MIME v3 clients might only implement signing or signature
      verification using id-dsa-with-sha1 and might also use id-dsa as
      an AlgorithmIdentifier in this field.

   -  Note that S/MIME v3.1 clients support verifying id-dsa-with-sha1
      and rsaEncryption and might not implement sha256WithRSAEncryption.
```

**N-180.** (§B.2 ¶15) — lines 3382–3383

> NOTE: Receiving clients SHOULD recognize id-dsa as equivalent to
> id-dsa-with-sha1.

**N-181.** (§B.2 ¶16) _[implied]_ — lines 3385–3390

> For 512-bit RSA with SHA-1, see [RFC3370] and [FIPS186-2] without
> Change Notice 1; for 512-bit RSA with SHA-256, see [RFC5754] and
> [FIPS186-2] without Change Notice 1; and for 1024-bit through
> 2048-bit RSA with SHA-256, see [RFC5754] and [FIPS186-2] with Change
> Notice 1.  The first reference provides the signature algorithm's
> OID, and the second provides the signature algorithm's definition.

**N-182.** (§B.2 ¶17) _[implied]_ — lines 3392–3398

> For 512-bit DSA with SHA-1, see [RFC3370] and [FIPS186-2] without
> Change Notice 1; for 512-bit DSA with SHA-256, see [RFC5754] and
> [FIPS186-2] without Change Notice 1; for 1024-bit DSA with SHA-1, see
> [RFC3370] and [FIPS186-2] with Change Notice 1; and for 1024-bit and
> above DSA with SHA-256, see [RFC5754] and [FIPS186-4].  The first
> reference provides the signature algorithm's OID, and the second
> provides the signature algorithm's definition.

### §B.3 ContentEncryptionAlgorithmIdentifier

**N-183.** (§B.3 ¶1–¶3) _[lowercase]_ — lines 3402–3414

```
   The following algorithms have been called out for some level of
   support by previous S/MIME specifications:

   -  RC2/40 [RFC2268] was dropped in [SMIMEv3.2].  The algorithm is
      known to be insecure and, if supported, should only be used to
      decrypt existing email.

   -  DES EDE3 CBC [TripleDES], also known as "tripleDES", was dropped
      in [SMIMEv4].  This algorithm is removed from the list of
      supported algorithms because (1) it has a 64-bit block size and
      (2) it offers less than 128 bits of security.  This algorithm
      should be supported only to decrypt existing email; it should not
      be used to encrypt new emails.
```

### §B.4 KeyEncryptionAlgorithmIdentifier

**N-184.** (§B.4 ¶1–¶3) _[lowercase]_ — lines 3425–3433

```
   The following algorithms have been called out for some level of
   support by previous S/MIME specifications:

   -  DH ephemeral-static mode, as specified in [RFC3370] and
      [SP800-57], was dropped in [SMIMEv4].

   -  RSA key sizes have been increased over time.  Decrypting old mail
      with smaller key sizes is reasonable; however, new mail should use
      the updated key sizes.
```

**N-185.** (§B.4 ¶4) _[implied]_ — lines 3435–3437

> For 1024-bit DH, see [RFC3370].  For 1024-bit and larger DH, see
> [SP800-56A]; regardless, use the KDF, which is from X9.42, specified
> in [RFC3370].



## §C Moving S/MIME v2 Message Specification to Historic Status

_No entries — records that RFC 2311 was moved to Historic status
(administrative history); no requirement._



## Acknowledgements

_No entries._



## Authors' Addresses

_No entries — contact details._



## Coverage

**Entries.** 185, `N-001` to `N-185`, in source order: §1 0; §1.1 2; §1.2 1;
§1.3 3; §1.4 1; §1.5 1; §1.6 4; §1.7 0; §2 1; §2.1 3; §2.2 4; §2.3 3; §2.4 1;
§2.4.1–§2.4.5 6; §2.5 6; §2.5.1 3; §2.5.2 8; §2.5.3 5; §2.5.3.1 1; §2.6 2;
§2.7 1; §2.7.1 5; §2.7.1.1 1; §2.7.1.2 2; §2.7.2 1; §2.7.3 1; §3 1; §3.1 9;
§3.1.1 5; §3.1.2 4; §3.1.3 2; §3.1.4 1; §3.2 5; §3.2.1 3; §3.2.2 4; §3.3 3;
§3.4 3; §3.5 1; §3.5.1 3; §3.5.2 2; §3.5.3 1; §3.5.3.1 2; §3.5.3.2 5;
§3.5.3.3 0; §3.6 3; §3.7 5; §3.8 3; §3.9 2; §3.10 3; §4 2; §4.1 4; §4.2–§4.5
4; §5 2; §5.1–§5.4 4; §6 19; §7.1 1; §A 2; §B 1; §B.1 1; §B.2 6; §B.3 1;
§B.4 2. By top-level section: §1 12, §2 54, §3 70, §4 10, §5 6, §6 19,
§7 1, §A 2, §B 11.

**Keyword reconciliation: 190 = 190.** Capitalised BCP 14 keywords counted
with `bin/_bcp14.py`'s rule over the verbatim text of all entries
together, with the conventions paragraph (N-004) stripped exactly as the
counter strips it from the source: 190 — MUST 82, SHOULD 84, MAY 12,
MUST NOT 5, SHOULD NOT 4, RECOMMENDED 2, OPTIONAL 1. The source count is
190 with the same split, so every keyword occurrence of the source lies in
an entry and none is counted twice. Per section: §1.1 1; §1.3 14; §1.5 6;
§1.6 17; §2.1 3; §2.2 7; §2.3 8; §2.4.1 5; §2.4.2 1; §2.5 6; §2.5.1 4;
§2.5.2 13; §2.5.3 10; §2.5.3.1 3; §2.6 3; §2.7 3; §2.7.1 10; §2.7.1.1 2;
§2.7.1.2 2; §2.7.2 1; §3.1 3; §3.1.1 7; §3.1.2 5; §3.1.3 1; §3.1.4 1; §3.2 3;
§3.2.1 7; §3.2.2 3; §3.3 1; §3.4 1; §3.5 1; §3.5.3.1 1; §3.5.3.2 5; §3.7 1;
§3.8 2; §3.9 1; §4 2; §4.1 3; §4.2 3; §4.3 3; §4.4 3; §4.5 3; §6 8; §A 2;
§B.2 1.

**Lowercase.** 22 entries carry `_[lowercase]_`: N-007, N-031, N-063, N-069,
N-071, N-082, N-093, N-094, N-097, N-098, N-117, N-118, N-156, N-158, N-159,
N-164, N-165, N-170, N-177, N-179, N-183, N-184. The other lowercase
occurrences inside entries are descriptive (`may have changed`, N-008,
N-009; `optional features`, N-040; `other required data`, N-102, N-105,
N-111, N-122; `no private key material is required`, N-126; `may issue
documents`, N-153; `necessarily required`, N-169; `recommended
algorithms` ×2, N-175).

**Page breaks.** 12 entries cross one: N-003, N-053, N-058, N-063, N-091,
N-096, N-122, N-165, N-169, N-172, N-174, N-177; mid-sentence in N-091,
N-096 and N-169.

**Mechanical checks (pass 1).** Every entry was checked by script against
the hashed source: its container equals source lines a–b under the rules in
*How to read this file* (blockquote indent, fenced bytes, page furniture
removed only where the range contains it); its locator's section contains
both ends of the range; its `¶` numbers are the first and last blocks of
the range under the stated block rule; entries are numbered in source order
and no two ranges overlap; the `_[crosses page break]_` flag is set exactly
where the range contains page furniture; no capitalised keyword line of the
source lies outside an entry; and the keyword count over the entries is the
190 above. The lowercase census by word is `required` 16, `may` 12,
`should` 8, `recommended` 8, `optional` 5, `must` 4 (53), plus `ought` 1.

**Excluded, and why.**

- Front matter (title block, Abstract, Status of This Memo, Copyright
  Notice, Table of Contents): overview and publication boilerplate.
- §1 ¶1–¶5, §1.1 ¶1–¶3 and ¶6, §1.4 ¶2–¶6, §1.7: overview, motivation,
  bibliography of prior versions, and the v4.0 changelog (no keyword; each
  change is specified in the section it names).
- §1.5 ¶5–¶8 and §1.6 ¶2, ¶4–¶6, ¶11–¶13, ¶15–¶24: changelog bullets with
  no capitalised keyword.
- §3 ¶2–¶3, §3.1.3 ¶2–¶5, §B ¶2: motivation and editorial notes.
- Sample messages and example displays (§3.1.4 ¶2 onward, §3.3 ¶7 onward,
  §3.4 ¶7 onward, §3.5.2 ¶7 onward, §3.5.3.3, §3.6 ¶7 onward): examples,
  carried by the examples artifact.
- §7.2, §7.3: bibliography. §C: administrative history. Acknowledgements,
  Authors' Addresses.

No capitalised BCP 14 keyword occurs in any excluded block.
