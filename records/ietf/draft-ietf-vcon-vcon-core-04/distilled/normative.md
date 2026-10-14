---
record: draft-ietf-vcon-vcon-core-04
kind: normative
title: "draft-ietf-vcon-vcon-core-04 — normative statements"
extracted: "2026-10-13"
reviewed_by: ""
---

<!-- FX-1 pass 1. Every normative statement and normative block of
     draft-ietf-vcon-vcon-core-04, VERBATIM, with its locator, in source
     order. Verbatim source only: no analysis, no paraphrase, no opinion.
     Blockquotes and fenced blocks delimit verbatim text; everything outside
     them is structure (headings, entry numbers, locators, flags) only. -->

Source: `draft-ietf-vcon-vcon-core-04`, "The JSON format for vCon - Conversation Data Container", D. Petrie, IETF vcon WG, September 2026.

Cached source: `.cache/draft-ietf-vcon-vcon-core-04.txt`, 8904 lines,
sha256 `cc2a2cb5051b860e2f29478a9ff946e3d882818bfad55dff48e0f5ae033cd722`.


## How to read this file

**Verbatim containers.** Two are used, and the distinction matters:

- A **blockquote** (`>`) reproduces running prose. The source's own line
  breaks are kept and its leading three-space RFC indent is removed; no word,
  spelling or punctuation mark is altered — including the source's own
  misspellings, doubled articles and broken cross-references.
- A **fenced block** (```` ``` ````) reproduces the source's lines
  byte-exactly, indentation included. Every table, bullet list, type
  declaration, figure and registration template is fenced, so
  whitespace-significant material is never rewrapped.

Everything outside a quote or a fence — headings, entry numbers, locators,
flags — is structure added by this extraction, not source text. **No two
non-adjacent passages are ever spliced into one entry:** each entry is a
single contiguous run of source lines. (The previous extraction of this
document spliced two non-adjacent quotes; that was a recorded defect and the
reason this file was rebuilt.)

**Pagination.** This is an Internet-Draft in paginated text form. Where a
contiguous passage crosses a page boundary, the running apparatus — the form
feed, the `Petrie   Expires 11 March 2027   [Page N]` footer, the
`Internet-Draft   JSON vCon   September 2026` header and the blank padding
around them — is removed, and the passage is reproduced as the single
paragraph, list or table that it is. Nothing else is removed. Table 1
(§4.3.1.6) and the §2.1 terminology list are the passages where this matters
most.

**The `_[lowercase]_` marker.** An entry is marked `_[lowercase]_` when it
carries binding content — a definition, a type declaration, a constraint on a
representation, a registry rule, a conformance expectation — and carries no
BCP 14 keyword of its own. The marker records that fact. It neither demotes
the keyword-bearing statements nor upgrades the lowercase ones.

**Lowercase obligations inside keyword-bearing entries** are called out in a
`Lowercase obligation:` line beneath the entry, quoting the source's own
words. This document leans on lowercase `should`, `must`, `required`,
`mandatory`, `may not` and `not permitted` in places where they plainly bind;
they are flagged as lowercase, never promoted to BCP 14 keywords.


## BCP 14 keyword census

`bin/bcp14-count .cache/draft-ietf-vcon-vcon-core-04.txt --by-keyword`, with
the RFC 2119/8174 boilerplate paragraph excluded:

```
216
  SHOULD            97
  MUST              65
  MAY               31
  MUST NOT          17
  SHOULD NOT         6
```

No `SHALL`, `SHALL NOT`, `REQUIRED`, `RECOMMENDED`, `NOT RECOMMENDED` or
`OPTIONAL` occurs anywhere in the document. Note the shape of that census:
**`SHOULD` outnumbers `MUST` 97 to 65.** Distribution by division:

| division | occurrences |
|---|---|
| §1 Introduction | 0 |
| §2 Conventions and Definitions | 20 |
| §3 vCon JSON Object | 0 |
| §4 Unsigned Form | 121 |
| §5 Security Considerations | 27 |
| §6 IANA Considerations | 1 |
| §7 Non-Upward Compatible Changes | 0 |
| §8 References | 0 |
| Appendix A Example vCons | 0 |
| Appendix B vCon JSON Schema | 8 |
| Appendix C vCon CDDL | 39 |
| **total** | **216** |

**This file covers §1–§7 and therefore accounts for 169 of the 216.** The
remaining 47 are inside Appendix B's JSON Schema `description` strings and
Appendix C's CDDL comments, which restate body requirements inside the formal
artifacts; they are carried by `distilled/schema/`. See `## Coverage` at the
end for the per-section reconciliation.


## Section 1. Introduction

§1.1 *Purpose of vCon* and §1.3 *Benefits of vCon* are motivation and are
dropped per the extraction rule. §1 carries no BCP 14 keyword.

**1.** (§1) _[lowercase]_

> This document specifies the *vCon* (Conversational Data Exchange)
> standard, which defines a unified format for representing and
> exchanging conversational data across different communication
> platforms and modalities.  The goal of *vCon* is to provide a
> standardized, platform-agnostic structure for capturing and sharing
> conversational information, allowing for seamless integration between
> systems, enterprises, and trust boundaries.


### Section 1.2. Extending the vCon Schema

**2.** (§1.2) _[lowercase]_

> In addition to the core *vCon* schema, this document provides a
> framework for extending the *vCon* format to support specialized use
> cases.  The *vCon* schema can be customized to address the needs of
> specific industries or applications, such as:


### Section 1.4. Scope of the Document

**3.** (§1.4) _[lowercase]_

> This document defines the core structure and schema for *vCon* as a
> JSON format.  Detailed specifications for the various parameters and
> the extension framework will be provided in subsequent sections.  The
> primary focus is on creating a flexible, extensible standard for the
> exchange of conversational data that can be easily adopted across
> industries, use cases, and communication technologies.


## Section 2. Conventions and Definitions

The RFC 2119 / RFC 8174 boilerplate paragraph (§2, lines 324–329) is dropped:
it defines how the keywords are read, it is not itself an obligation, and
`bin/bcp14-count` excludes it from the census for the same reason.


### Section 2.1. Terminology

The whole terminology list, reproduced in one block: these are the
definitions every other section is written against. `vCon instance version`
and `vCon syntax version` are the two that carry the most weight downstream —
the redacted/amended model in §4.1.8/§4.1.9 is stated entirely in terms of
*instance versions*. The list crosses a page boundary between `vCon syntax
version` and `signed form`; the pagination is removed and the list is kept
whole.

**4.** (§2.1) _[lowercase]_

```
   *  analysis - analysis, transformations, summary, sentiment, or
      translation typically of the dialog data

   *  conversation - an exchange of communication using text, audio or
      video medium between at least one human and one or more bots or
      humans

   *  de-identification - removal of all information that could identify
      a party in a conversation.  This includes PII as well as audio and
      video recordings.  Voice recordings might be re-vocalized with a
      different speaker.

   *  dialog - the captured conversation in its original form (e.g.
      text, audio or video)

   *  encrypted form - encrypted JWE document with the JWS signed vCon
      form contained in the ciphertext

   *  file - a data block either included or referenced in a vCon

   *  object - JSON object containing key and value pairs

   *  parameter - JSON key and value pair

   *  party - an observer or participant to the conversation, either
      passive or active

   *  payload - the contents or bytes that make up a file

   *  PII - Personal Identifiable Information

   *  PII masked - may include voice recordings, but PII is removed from
      transcripts and recordings (audio and video).

   *  vCon - container for conversational information

   *  vCon instance - a vCon populated with data for a specific
      conversation

   *  vCon instance version - a single version of an instance of a
      conversation, which may be modified to redact or amend additional
      information forming a subsequent vCon instance version

   *  vCon syntax version - the version for the data syntax used for
      form a vCon

   *  signed form - JWS signed document with the unsigned vCon form
      contained in the payload
```


### Section 2.2. JSON Notation

**5.** (§2.2) _[lowercase]_

> For the ease of documentation, the convention for [JSON] notation
> used in this document is copied from sections 1.1-1.5 of [JMAP].

The base type vocabulary. `Date` and `Mediatype` each carry a `MUST`; the
rest are definitional.

**6.** (§2.2 (base types))

```
   *  Date - A string that MUST have the form of an [RFC3339] date
      string as defined for the Date type in section 1.4 of [JMAP].

   *  "*" - The type is undefined; the value can be any JSON type,
      although permitted values may be constrained by the context of the
      value, as defined in section 1.1 of [JMAP].

   *  "String" - a JSON string type.

   *  "UnsignedInt" - a positive JSON integer as defined in section 1.3
      of [JMAP].

   *  "UnsignedFloat" - a positive JSON floating point number containing
      a decimal point as defined in section 6 of [JSON].

   *  "Mediatype" - A "String" value that MUST be of the following form
      as defined in section 5.1 of [MIME]:

      type "/" subtype
```

`ContentHash` is where the externally-referenced-file integrity mechanism is
actually defined — four BCP 14 keywords inside a single bullet of a *notation*
section. It is reproduced whole because the algorithm-token grammar is only
legible as one run.

**7.** (§2.2 (ContentHash))

```
   *  "ContentHash" - The string token value is generated using the same
      approach used in section 6 of [STIR-PASS].  The relevant text is
      copied here for convenience and to remove the normative
      dependency.  The hash string token values are formed from
      combining a string that defines the crypto algorithm used to
      generate the digest along with the Base64Url Encoded value of the
      SHA-512 hash, as defined in section 6.3 and 6.4 [SHA-512], of the
      body of the content at the given url.  The hash algorithm is
      identified by "sha512".  SHA-512 is part of the SHA-2 set of
      cryptographic hash functions [SHA-512] defined by the US National
      Institute of Standards and Technology (NIST).  Implementations MAY
      support additional recommended hash algorithms in [IANA-COSE-ALG];
      that is, the hash algorithm has "Yes" in the "Recommended" column
      of the IANA registry.  Hash algorithm identifiers MUST use only
      lowercase letters, and they MUST NOT contain hyphen characters.
      The character following the algorithm string MUST be a hyphen
      character, "-", or ASCII 45.  The subsequent characters are the
      Base64Url encoded (see Section 2 [JWS]) digest of a canonicalized
      and concatenated string or binary data based on the JSON pointer
      referenced elements of "rcd" claim or the URI referenced content
      contained in the claim.
```

**8.** (§2.2 (SessionId)) _[lowercase]_

```
   *  "SessionId" - An object with the String parameters: "local" and
      "remote".  The String values of these parameters are UUIDs as
      defined in section 5 of [SESSION-ID] as "local-uuid" and "remote-
      uuid".  This is designed to also work with the H.323 correlated
      [H-460-27] which refers to them as "Sender-UUID" and "Recipient-
      UUID".

      { "local": String, "remote": String }
```

**9.** (§2.2 (array notation)) _[lowercase]_

```
   *  "A[]" and array of values of type A.
```

The single most load-bearing lowercase sentence in the document: it sets the
default cardinality for **every** parameter in **every** object, and it is
the reason an unannotated type declaration such as `*  uuid: "String"` in
§4.1.8.1 is a mandatory parameter.

**10.** (§2.2 (default cardinality)) _[lowercase]_

> All parameters are assumed to be mandatory unless otherwise noted.

Lowercase obligation: *"are assumed to be mandatory"*.

**11.** (§2.2 (empty values))

> Objects or arrays with no or null values MAY be excluded from the
> vCon.


### Section 2.3. Inline Files

**12.** (§2.3)

> Objects that contain a file or data inline (i.e. within the vCon)
> MUST have the parameters: body and encoding.  JSON does not support
> binary data values.  For this reason inline files MUST be Base64url
> (see Section 2 [JWS]) encoded to be included as a valid JSON string
> value if they are not already valid JSON strings.


#### Section 2.3.1. body

**13.** (§2.3.1) _[lowercase]_

```
   The body parameter contains the payload of the file to be included
   inline.  Depending upon the data in the file, it may require encoding
   to be represented as a valid JSON value.

   *  body: "*"
```


#### Section 2.3.2. encoding

**14.** (§2.3.2)

> The encoding parameter describes the type of encoding, if any, that
> was performed to represent the file payload as the value of the body
> parameter.  If the body parameter is provided and is not an empty
> string, the encoding parameter MUST be provided.  In the interest of
> being tolerant for interoperability, if the encoding value is not
> provided, applications can attempt to derive the encoding token value
> based upon the mediatype parameter or filename extension if either is
> provided.

**15.** (§2.3.2 (encoding token values))

```
   *  encoding: "String"

   This MUST be one of the following strings:

   *  "base64url": The payload of the file has been Base64Url encoded
      and provided as the string value of the body parameter.

   *  "json": The value of the body parameter is a JSON value (object,
      array, number, string, or one of the literals true, false, or
      null) as defined in [JSON].

   *  "none": The payload of the file is a valid JSON string and can be
      included without modification as the string value to the body
      parameter.
```


### Section 2.4. Externally Referenced Files

**16.** (§2.4)

> Files and data stored externally from the vCon MUST be "signed" to
> ensure that they have not been modified.  Objects that refer to a
> file which is externally stored from the vCon MUST have the
> parameters: url, content_hash.  These parameters are defined in the
> following subsections.  The values and format of the hashes are
> defined in Section 2.2 type: ContentHash.  The use of [SHA-512] hash
> for ensuring that the externally referenced data or file has not been
> modified, is defined in this document.  Other methods of ensuring
> integrity may be added in the future.


#### Section 2.4.1. url

**17.** (§2.4.1)

```
   The url value contains the [HTTPS] URL where the externally
   referenced file is stored.  HTTPS MUST be used for retrieval to
   protect the privacy of the contents of the file.

   *  url: "String"
```


#### Section 2.4.2. content_hash

**18.** (§2.4.2)

```
   The integrity of externally referenced files are protected using a
   hash of the external content.  The algorithm and hash value are
   contained in the content_hash parameter.  The value of the
   content_hash can be a single token or an array of tokens if multiple
   hash algorithms are desired to be provided.  The SHA-512 [SHA-512]
   algorithm MUST be supported.  Other algorithms MAY be included.  The
   algorithm used for signing the externally referenced file is defined
   in section 6.3 and 6.4 of [SHA-512].

   *  content_hash: "ContentHash" | "ContentHash[]"
```


### Section 2.5. Extending vCon

**19.** (§2.5)

> vCon provides a means to extend the schema defined in this document.
> A vCon extension can define new parameters at any level of the
> schema.  It can also redefine the semantics of or deprecate existing
> parameters.  A vCon extension is defined in its own document.  In
> addition to the standard sections of an Internet-Draft, a vCon
> extension document MUST also contain the following sections.

The four sections a vCon extension document is required to contain. Note
that the obligations *inside* these bullets — `State`, `Define`, `Register`,
`Describe`, `Demonstrate` — are bare imperatives, not BCP 14 keywords; the
`MUST` that binds them is the one in the entry above.

**20.** (§2.5 (required extension-document sections)) _[lowercase]_

```
   *  *Extension Name*: State the registered extensions token name for
      the extension.  State whether and under what conditions the name
      appears in the extensions (Section 4.1.3) parameter, the critical
      (Section 4.1.4) parameter, or both.  This is the name registered
      in the vCon Extensions Names Registry (Section 6.4) and the name
      against which implementations determine whether they support the
      extension.

   *  *Parameter Definitions*: Define each new parameter, the level of
      the schema at which it appears, its value type, and its semantics.
      For any existing parameter whose meaning or permitted values are
      redefined, state the new semantics and values.  For any deprecated
      parameter, state what is to be used in its stead and the migration
      approach.  Use the snake case naming convention for all parameter
      names, as opposed to camel case.  Register each new parameter in
      the appropriate Object registry with IANA.

   *  *Compatibility Considerations*: Describe how the extension behaves
      in the presence of implementations that do not support it.
      Identify the parameters and semantics the extension introduces or
      changes, and explain for each why an implementation that does not
      recognize the extension can continue to process the vCon correctly
      by ignoring the additions, or state the conditions under which
      that holds.  An extension that is *Compatible* under all
      conditions states so explicitly and justifies that claim.

   *  *Incompatibility Considerations*: Demonstrate either that the
      extension introduces no incompatibilities, or enumerate each
      incompatibility that it does introduce.  For each incompatibility,
      state the processing that is affected, for example redaction
      versus transcription, whether the extension name is therefore
      required in the critical (Section 4.1.4) parameter, and the
      behavior required of implementations that do not support the
      extension.  An extension that claims to be *Compatible* uses this
      section to show why no incompatibility exists.

   *  *Privacy and Integrity Considerations*: Describe how the
      extension's parameters interact with redaction and de-
      identification, including whether any of them can carry party-
      identifying data or PII and how a redactor is expected to handle
      them.  State whether the extension introduces any new external
      content references, and if so, the integrity mechanism that
      protects them, such as Section 2.4.2.
```

Lowercase obligation: *"whether the extension name is therefore required in the critical (Section 4.1.4) parameter"*; *"the behavior required of implementations that do not support the extension"*.

**21.** (§2.5 (extension categories)) _[lowercase]_

```
   Extensions to the vCon schema can be classified into two categories:

   *  *Compatible*: These extensions introduce additional data or fields
      without altering the meaning or structure of existing elements.
      Implementations that do not recognize these extensions can safely
      ignore them while maintaining valid processing of the vCon.

   *  *Incompatible*: These extensions modify existing semantics or
      schema definitions in ways that render a vCon incompatible with
      implementations that do not support the extension.  Interpreting
      such a vCon correctly requires explicit awareness of the
      extension.
```

**22.** (§2.5)

> Wherever feasible, extensions *SHOULD* be designed as *Compatible* to
> preserve compatibility with existing implementations.  The question
> of Compatible vs Incompatible is a little subjective.  A transcriber
> for vCon can be fairly tolerant of changes adding new parameters or
> objects to a vCon.  On the other hand, a redactor must be aware of
> the implications of all parameters in the vCon to be sure to redact
> all of the objective information.  In these cases a transcriber will
> likely only need to look at the critical extensions.  However the
> redactor perhaps should reject vCons with any extension that it does
> not support.

Lowercase obligation: *"a redactor must be aware of the implications of all parameters in the vCon"*; *"the redactor perhaps should reject vCons with any extension that it does not support"* — a hedged lowercase `should` on the behaviour that makes the `critical` mechanism work.

**23.** (§2.5)

> However, when disruptive extensions are necessary, the names of all
> such extensions *MUST* be listed in the critical (Section 4.1.4)
> parameter of the vCon.  This allows implementations to determine
> whether they are capable of processing the vCon safely and
> accurately.

**24.** (§2.5)

> Implementations that encounter a vCon containing a disruptive
> extension listed in the critical parameter, but do not support that
> extension, *MUST NOT* process the vCon except to reject it or notify
> the user.


## Section 3. vCon JSON Object

**25.** (§3 (the three forms)) _[lowercase]_

```
   The JSON form of a vCon is contained in a JSON object in one of three
   forms:

   *  unsigned

   *  signed

   *  encrypted
```

**26.** (§3) _[lowercase]_

> The unsigned form of the vCon has a single top level object.  This
> top level vCon object is also contained as described in the signed
> (Section 5.2) and encrypted (Section 5.3) forms of the vCon.  The
> selection of the JSON format enables interchange between application
> and lower layers of the network stack, critical for enablement of
> analysis of conversations.  The signed form of vCon is defined in
> Section 5.2 using [JWS] to provide integrity and proof of the
> conversation data.  The encrypted form of vCon is defined in
> Section 5.3 using [JWE] to provide complete privacy of the
> conversational data.  Partial privacy or data minimization can be
> provide for a vCon using the Section 4.1.8 construct.


## Section 4. Unsigned Form of vCon Object

**27.** (§4)

> The unsigned form of the top level vCon object is necessary as in
> many cases, a vCon will be partially constructed and in process as
> conversation data is collected.  This may change while the
> conversation is in progress or on-going.  The vCon may start with
> only meta data and party information, then progress to contain dialog
> information.  It may then get analysis added or it could be passed to
> another security domain for analysis.  A vCon in the unsigned form
> SHOULD contain at least one of the parties, dialog, analysis or
> attachments parameters.

**28.** (§4)

> A vCon may be constructed across several security domains.  When a
> vCon is to be exported from one security domain to another, it SHOULD
> be signed or encrypted by the domain that constructed it.  The
> subsequent domain may have need to redact or amend data to the vCon.
> Alternatively the originating domain may want to redact the vCon
> before providing it to an other domain.  The second or subsequent
> domain, MAY modify the prior vCon instance version and when complete
> or exporting to another security domain, it SHOULD sign or encrypt
> the new vCon instance version.  The new vCon instance version SHOULD
> refer to the prior vCon instance version via the redacted
> (Section 4.1.8) or amended (Section 4.1.9) parameters.


### Section 4.1. vCon JSON Object Keys and Values

**29.** (§4.1) _[lowercase]_

> The keys and values for the top level vCon JSON object are defined in
> the following subsections.


#### Section 4.1.1. vcon

**30.** (§4.1.1) _[lowercase]_

> The "vcon" parameter is DEPRECATED as of the publication of this
> document as an RFC.  The "vcon" parameter was used to differentiate
> schema changes to the vCon core container when incompatibilities were
> created in Internet-Draft versions.  The extension mechanism replaces
> the need for schema versioning.  The vcon parameter was used to
> contain the syntactic version of the JSON format used in the vCon.
> (see Non-Upward Compatible Changes to the vCon Container (Section 7))

Lowercase obligation: *"is DEPRECATED as of the publication of this document as an RFC"* — stated in capitals but not a BCP 14 keyword; the document attaches no processing rule to it.

**31.** (§4.1.1 (type and value))

```
   *  vcon: "String"

   For syntax defined in this document, the string MUST have the value:
   "0.4.0"
```


#### Section 4.1.2. uuid

**32.** (§4.1.2)

> The [UUID] for the vCon is used to refer to it when privacy or
> security may not allow for inclusion or URL reference to a vCon.  The
> UUID value MUST be globally unique.  All vCon documents MUST have the
> uuid parameter and value set.

**33.** (§4.1.2 (type)) _[lowercase]_

```
   *  uuid: "String"
```

**34.** (§4.1.2 (version 8 generation))

```
   The value of the string SHOULD be generated using the version 8 UUID
   defined in [UUID] which is generated identically to a version 7 UUID
   with the exception that:

   *  rand_b/custom_c is generated from the high 62 bits of the SHA-1
      hash of the FQHN string

   *  the variant and version fields are set as described for version 8
      UUID
```

**35.** (§4.1.2 (FQHN))

> The DNS name string used in generating the uuid value SHOULD be the
> same FQHN, or a subdomain to allow for more distributed generation of
> UUIDs, as would used in the signing certificate as they are the same
> domains of uniqueness.


#### Section 4.1.3. extensions

**36.** (§4.1.3)

```
   The vCon schema can be extended through the definition of new
   extensions.  The extensions parameter SHOULD contain the list of
   names of all vCon extensions for any parameters used that are not
   defined in this core vCon schema document.

   *  extensions: "String[]"
```


#### Section 4.1.4. critical

**37.** (§4.1.4)

```
   Implementations that include extensions which are incompatible with
   the core vCon schema MUST list the names of those extensions in the
   critical parameter.  A vCon that includes a critical parameter
   indicates that correct interpretation of the vCon requires explicit
   support for the listed extensions.  An implementation that does not
   recognize or support the extensions listed in the critical parameter
   MUST NOT attempt to process or operate on the vCon, except to reject
   it or report unsupported content.

   *  critical: "String[]"
```


#### Section 4.1.5. created_at

**38.** (§4.1.5)

```
   The created_at parameter provides the creation time of this vcon,
   which MUST be present, and should not change once the vcon object is
   created.

   *  created_at: "Date"
```

Lowercase obligation: *"should not change once the vcon object is created"* — lowercase where a `SHOULD NOT` would bind, in the same sentence as a `MUST`.


#### Section 4.1.6. updated_at

**39.** (§4.1.6)

```
   The updated_at parameter provides the last modified time of this
   vcon, which MAY be present.  For unsigned forms, the updated_at of
   the vcon object SHOULD be updated as it is modified.  For signed
   forms of the vCon object, the updated_at contains the time when this
   vcon was last signed.  Future updates MUST first set the updated_at
   to the new signing time as the vcon object is signed again.

   *  updated_at: "Date"
```


#### Section 4.1.7. subject

**40.** (§4.1.7) _[lowercase]_

```
   The subject or the topic of the conversation is provided in the
   subject parameter.  This parameter is optional as not all
   conversations have a defined subject.  Email threads and prescheduled
   calls and video conferences typically have a subject which can be
   captured here.  The subject may also be derived from analysis of the
   dialog.

   *  subject: "String" (optional)

   The string value of the subject parameter is a free formed JSON
   string with no constrained syntax.
```


#### Section 4.1.8. redacted

**41.** (§4.1.8)

> A redacted vCon SHOULD provide a reference to the unredacted or
> prior, less redacted, vCon instance version of itself.  The purpose
> of the Redacted Object (Section 4.1.8.1) is to provide the reference
> to the unredacted or less redacted version of the vCon from which
> this vCon was derived.  For privacy reasons, it may be necessary to
> redact a vCon to construct another vCon without the PII.  This allows
> the non-PII portion of the vCon to still be analyzed or used in a
> broader scope.  The Redacted Object (Section 4.1.8.1) SHOULD contain
> the uuid parameter and MAY include the url, content_hash parameters
> (see Externally Referenced Files (Section 2.4)).  If a reference to
> the unredacted vCon is provided in the url parameter, the access to
> that URL MUST be restricted to only those who should be allowed to
> see the identity or PII for the redacted vCon.

**42.** (§4.1.8 (assurance of redaction))

> The method(s) for redaction of text, audio and video can be done with
> existing post processing of media.  The method of redaction is out of
> scope of this document.  The assurance of the accuracy of the
> redaction is made by the entity that creates the redaction which
> SHOULD sign the redacted version of the vCon.

**43.** (§4.1.8 (disposition of prior data)) _[lowercase]_

```
   All data and parameters in the prior, less redacted, vCon instance
   version are either:

   *  Removed entirely in the redacted version

   *  Copied and partially redacted

   *  Copied as is
```

**44.** (§4.1.8 (array index stability))

```
   Data which is to be completely removed from the redacted version,
   that is contained in a JSON array in the unredacted vCon, SHOULD
   create an empty placeholder such that object array indices do not
   change for the rest of the elements of the array.

   *  redacted: "Redacted" (optional, mutually exclusive with amended
      parameter)
```

The `redacted` type declaration carries the mutual exclusion with `amended` as a parenthetical, not as a BCP 14 statement; §4.1.9 states the same exclusion from the other side.


##### Section 4.1.8.1. Redacted Object

**45.** (§4.1.8.1)

```
   A Redacted Object contains the following parameters:

   *  uuid: "String"

   The value contains the uuid string value (Section 4.1.2) of the
   unredacted/prior vCon instance version.  The absence of a value for
   uuid indicates that the less redacted version of this vCon is not
   available or does not exist.
```

Lowercase obligation: *"The absence of a value for uuid indicates that the less redacted version of this vCon is not available or does not exist"* — a defined meaning for an absent parameter which §2.2 has already declared mandatory by default. See the contradiction noted under `## Coverage`.

**46.** (§4.1.8.1 (type parameter)) _[lowercase]_

```
   *  type: "String"

   The value of the redacted type parameter is used to indicate the type
   of redaction that was performed on this vCon relative to the less
   redacted version referenced by the redacted uuid parameter.  This
   should indicate the type of information that was redacted.
```

Lowercase obligation: *"This should indicate the type of information that was redacted."*

**47.** (§4.1.8.1 (external reference))

```
   The the location of the referenced vCon MAY be provided as defined in
   Externally Referenced Files (Section 2.4) by including url and
   content_hash. content_hash MUST be included if url is provided.

   *  url: "String"

   *  content_hash: "ContentHash" | "ContentHash[]"
```

**48.** (§4.1.8.1 (Figure 1)) _[lowercase]_

```
   The following diagram illustrates an example partial JSON object tree
   for a redacted vCon.  The top level object is a JWS signed vCon which
   contains a vCon in the unsigned form in the payload parameter.  The
   second level object is the redacted vcon which refers to the
   encrypted unredacted vCon in it's redacted parameter.  Note that the
   redacted vCon references the JWE encrypted vCon by UUID and may
   reference it by URL.  The JWE encrypted unredacted vCon contains the
   signed version of the unredacted vCon in the ciphertext parameter.
   The signed unredacted vCon contains the unredacted vCon in the
   unsigned form in it's payload parameter.

                   --------------
   Signed          | JWS   uuid-|-- redacted vCon uuid in header
   redacted vCon:  |            |
                   |    payload-|-- unsigned redacted vCon in
                   -------------- / payload parameter
                                 /
               -------------    /
   vCon which  |vCon       |<---
   has been    |           |
   redacted:   |  redacted-|-- Redacted Object
               ------------- / refers to JWE
                            / encrypted unredacted vCon
                           /
                          /
                         /
                        /
                       / ---------------   signed unredacted vCon
                       ->| JWE    uuid-|-- uuid in unprotected
   Encrypted signed      |             |
   unredacted vCon:      |  cyphertext-|--- JWS signed
                         ---------------  / unredacted vCon
                                         / in cyphertext
                    /-------------------/ parameter
                   /
                  /  -------------
   Signed         -> |JWS   uuid-|-- unredacted vCon uuid in header
   unredacted vcon:  |           |
                     |   payload-|-- unsigned unredacted vCon
                     -------------  \ in payload
                                     \   ----------
                                      -->| vCon   |
   Unsigned unredacted vCon:             |        |
                                         ----------

                    Figure 1: redacted vCon object tree
```


#### Section 4.1.9. amended

**49.** (§4.1.9)

> A signed or encrypted vCon cannot be modified without invalidating
> it.  In these cases, to allow for adding of additional information a
> new vCon instance version MUST be created.  The prior vCon instance
> version is referenced by the Amended Object (Section 4.1.9.1).  The
> vCon with amended data contains all of the data that is in the
> referenced vCon with the exception of data that is amended.  That is
> to say that the newer version of the vCon is a deep copy of the prior
> version with the amended and additional data added to it.

**50.** (§4.1.9 (reference to prior version))

```
   The prior vCon instance version SHOULD be referenced via the uuid of
   the prior vCon instance version, and MAY include the url and
   content_hash parameters (see Externally Referenced Files
   (Section 2.4)).

   *  amended: "Amended" (optional, mutually exclusive with redacted
      parameter)
```


##### Section 4.1.9.1. Amended Object

**51.** (§4.1.9.1) _[lowercase]_

```
   The Amended Object contains the following parameters:

   *  uuid: "String" (optional if external reference provided)

   The value contains the uuid string value (Section 4.1.2) of the
   unredacted/original vCon instance version.
```

**52.** (§4.1.9.1 (external reference))

```
   The location of the referenced vCon MAY be provided, as defined in
   Externally Referenced Files (Section 2.4) by including url and
   content_hash.  content_hash MUST be provided if url is provided.

   *  url: "String"

   *  content_hash: "ContentHash" | "ContentHash[]"
```

**53.** (§4.1.9.1 (Figure 2)) _[lowercase]_

```
   The following figure illustrates an example partial JSON object tree
   for an amended vCon.  The top level object is the JWS signed amended
   vCon which contains the unsigned form of the vCon in it's payload
   parameter.  The second level object is the amended vCon with
   additional conversational data (e.g. analysis data).  It refers to
   its original parent (or prior vCon instance version) of the vCon in
   its amended parameter.  Note: the amended parameter may refer to the
   prior version of the vCon via URL.  The amended vCon in this figure
   refers to the JWS signed version of the vCon, which in turn contains
   the original vCon in unsigned form in its payload parameter.

                   --------------
   Signed          | JWS   uuid-|-- amended vCon uuid in header
   amended vCon:   |            |
                   |    payload-|-- payload parameter
                   -------------- / contains unsigned
                                 / amended vCon
               -------------    /
   vCon with   |vCon       |<---
   amended     |           |
   data:       |   amended-|--- amended parameter
               |  analysis-|  / refers to JWS
               ------------- / signed original vCon
                            / along with additional
                           / conversational data
                          / (e.g. analysis)
                         /
                        /
                       / ------------
                       ->| JWS uuid-|-- original vCon uuid in header
   signed                |          |
   original vCon:        |  payload-|--- payload parameter
                         ------------  / contains unsigned
                                      / original vCon
                     -------------   /
   Original vCon:    |vCon       |<--
                     |           |
                     |   parties |
                     |   dialog  |
                     -------------

                     Figure 2: amended vCon object tree
```


#### Section 4.1.10. parties Objects Array

**54.** (§4.1.10) _[lowercase]_

```
   The name, identity or contact information of all of the parties
   involved with the conversation are included in the parties object
   array.  Whether the parties were observers, passive or active
   participants in the conversation, they each are included as a Party
   Object in the parties array.

   *  parties: "Party[]" (optional)

   The value of the parties parameter is an array of Party Objects
   (Section 4.2).
```


#### Section 4.1.11. dialog Objects Array

**55.** (§4.1.11) _[lowercase]_

```
   The actual conversation which occurred over text, audio or video that
   was captured, is contained in the dialog Objects Array.

   *  dialog: "Dialog[]" (optional)

   The value of the dialog parameter is an array of Dialog Objects
   (Section 4.3).  It should be noted that the Dialog Objects may not be
   sorted in chronological order.  They are in the order that they were
   added.  It is the applications responsibility to sort dialog and
   transcriptions if they are needed in chronological order.
```

Lowercase obligation: *"It is the applications responsibility to sort dialog and transcriptions if they are needed in chronological order."* — the array is explicitly **not** ordered, and every index-based cross-reference in the document depends on that.


#### Section 4.1.12. analysis Objects Array

**56.** (§4.1.12) _[lowercase]_

```
   Analysis, which is performed on the conversational data, is stored in
   the analysis Objects array.

   *  analysis: "Analysis[]" (optional)

   The value of the analysis parameter is an array of Analysis Objects
   (Section 4.5).
```


#### Section 4.1.13. attachments Objects Array

**57.** (§4.1.13) _[lowercase]_

```
   Ancillary documents, discussed, presented, referenced or related to
   the conversation may be stored in the attachments array.  It should
   be noted that the Attachment Objects may not be sorted in
   chronological order.  They are in the order that they were added.

   *  attachments: "Attachment[]" (optional)

   The value of the attachments parameter is an array of Attachment
   Objects (Section 4.4).
```


### Section 4.2. Party Object

**58.** (§4.2)

> A Party Object contains information about a specific party or
> participant in the conversation.  The information that is available
> about the party varies with the context, the communication mode and
> platform.  There are times when no information is available for a
> party either initially or over the entire life of the vCon.  In such
> situations, it is possible to have a Party Object with no parameters
> in it.  A Party Object SHOULD be created for each participant.  This
> may result in more than one empty Party Object.  They are distinct by
> the order or index in the Party Object array.


#### Section 4.2.1. tel

**59.** (§4.2.1)

```
   If the tel URL for the party is known, it can be included in the tel
   parameter.

   *  tel: "String" (optional)

   The value of the tel parameter SHOULD be a valid [TEL] URL.  The URL
   scheme prefix (i.e. "tel:") is optional.
```


#### Section 4.2.2. sip

**60.** (§4.2.2) _[lowercase]_

```
   The [SIP] URL for the party can be provided in the sip parameter.

   *  sip: "String" (optional)

      The value of the sip parameter is the addr-spec as defined in
      section 25.1 of [SIP].
```


#### Section 4.2.3. stir

**61.** (§4.2.3) _[lowercase]_

```
   If the STIR [PASSporT] was provided to identify the party, the
   PASSporT can be included in the stir parameter for the party.

   *  stir: "String" (optional)

   The string value of the stir parameter contains the [PASSporT] in the
   JWS Compact Serialization form.
```


#### Section 4.2.4. mailto

**62.** (§4.2.4)

```
   If the mailto URL is known for the party, it can be included in the
   mailto parameter.

   *  mailto: "String" (optional)

   The value of the mailto parameter is a string containing an email
   address for the party.  It MAY be provided in any common form, such
   as a bare address or a [MAILTO] URL; when a [MAILTO] URL is used, the
   "mailto:" scheme prefix is optional.
```


#### Section 4.2.5. name

**63.** (§4.2.5)

```
   If the party's name is known, it can be included in the name
   parameter.

   *  name: "String" (optional)

   The string value of the name parameter is a free form JSON string in
   which part or all of the party's name can be included.  It may be
   necessary, for privacy reasons, to not identify any information about
   the party.  This MAY be indicated by creating a Party Object with
   only the name parameter and setting its value to "anonymous".  A
   Party Object SHOULD be create for each anonymous party in the
   conversation.  This is necessary to capture the number of parties and
   distinction between which party contributed what data or dialog in
   the conversation.  Hence it is possible to have multiple anonymous
   Party Objects in the vCon.  They are distinct by the order or index
   in the Party Object array.
```


#### Section 4.2.6. did

**64.** (§4.2.6)

```
   If a Decentralized Identifier [DID] is known for the party, it can be
   included in the did parameter.

   *  did: "String" (optional)

   The value of the did parameter MUST be a valid DID URI that enables
   verifiable, decentralized digital identity for the party.  DIDs are
   designed to be decoupled from centralized registries and identity
   providers, allowing the controller of the DID to prove control
   without requiring permission from other parties.  The DID can refer
   to any subject (person, organization, thing, etc.) as determined by
   the controller of the DID.
```


#### Section 4.2.7. validation

**65.** (§4.2.7)

```
   Proof of authorization of the communication channel through STIR,
   login or possession of a device, is often not sufficient proof of the
   identity of the person at the other end of the communications
   channel.  It is common in call centers to validate the identity of
   the person on the communication channel through verification of some
   sort of personal identification information.  The methods used, often
   varies with the situation and is business practices specific.  The
   purpose of the validation parameter, is to allow the validator to
   save a label or token which identifies the method of identity
   validation used to identify the person at the other end of the
   communication channel.  For confidentially reasons, it SHOULD NOT
   contain the data used to validate the name.  However it MAY name the
   data used to validate the name (e.g. "SSN", "DOB", "user ID and
   password").  It is up to the domain creating the vCon to define the
   set of tokens or values to be used for the validation parameter.

   *  validation: "String" (SHOULD be provided if name parameter is
      provided)

   The value of the validation string MAY be "none" or enterprise or
   domain defined token or string values.
```

The `SHOULD` in *"(SHOULD be provided if name parameter is provided)"* sits inside a type declaration rather than in prose; it is counted in the census and is reproduced here in place.


#### Section 4.2.8. gmlpos

**66.** (§4.2.8) _[lowercase]_

```
   If the geolocation of the party is known, it can be added in the
   gmlpos parameter.  The gmlpos parameter contains the latitude and
   longitude of the location of the party at the time of the
   conversation start.

   *  gmlpos: "String" (optional)

   The gmlpos parameter value contains a string of the same format as
   the gml:pos element defined in section 3.2 of the [PIDF-LO] PIDF.
```


#### Section 4.2.9. civicaddress

**67.** (§4.2.9)

```
   The the civicaddress parameter value contains a Civicaddress Object
   which is optional and contains civic address information about the
   location for the party.

   *  civicaddress: "Civicaddress" (optional)

   The Civicaddress Object MAY contain any or all of the following
   parameters: country, a1, a2, a3, a4, a5, a6, prd, pod, sts, hno, hns,
   lmk, loc, flr, nam, pc as defined in section 2.2.1 of [GEOPRIV].  The
   values of all of these parameters are of type String.  Note that the
   parameter names MUST be in lower case when contained in the
   Civicaddress Object even though they are in upper case in [GEOPRIV].
```

**68.** (§4.2.9 (Civicaddress parameters)) _[lowercase]_

```
   *  country: "String" (optional)

   *  a1: "String" (optional)

   *  a2: "String" (optional)

   *  a3: "String" (optional)

   *  a4: "String" (optional)

   *  a5: "String" (optional)

   *  a6: "String" (optional)

   *  prd: "String" (optional)

   *  pod: "String" (optional)

   *  sts: "String" (optional)

   *  hno: "String" (optional)

   *  hns: "String" (optional)

   *  lmk: "String" (optional)

   *  loc: "String" (optional)

   *  flr: "String" (optional)

   *  nam: "String" (optional)

   *  pc: "String" (optional)
```


#### Section 4.2.10. uuid

**69.** (§4.2.10)

```
   The uuid is a unique identifier for the participant.  In a contact
   center, this is particularly important for the call agent
   participant, and must be static across interactions to allow
   correlation with the actual agent configuration provisioned into the
   systems.  The value of the uuid parameter is a free form unique
   identifier string for the participant.  The value is not constrained
   to the syntax defined in [UUID].  Operators often have existing
   methods of generating unique participant identifiers and MAY use any
   unique string value.

   *  uuid: "String" (optional)
```

Lowercase obligation: *"must be static across interactions to allow correlation with the actual agent configuration provisioned into the systems"* — lowercase `must`, and the only statement in the document that constrains a party identifier across vCons.


#### Section 4.2.11. type

**70.** (§4.2.11)

```
   There are different types of parties that participate in or
   contribute information to a conversation.  The type parameter may be
   used to indicate the type of participant represented by the Party
   Object.

   *  type: "String" (optional)

   The value of the type parameter SHOULD be one of the following:
   "person", "bot", "organization"
```


#### Section 4.2.12. org

**71.** (§4.2.12) _[lowercase]_

```
   The party may belong to or be an organization.  The org parameter is
   a free form text string for containing the organization identifier.

   *  org: "String" (optional)
```


#### Section 4.2.13. dept

**72.** (§4.2.13) _[lowercase]_

```
   The party may belong to a department with in an organization.  The
   dept parameter is a free form text string for containing the party's
   department identifier.

   *  dept: "String" (optional)
```


### Section 4.3. Dialog Object

**73.** (§4.3 (the five dialog types)) _[lowercase]_

```
   The Dialog object references or contains text, audio or video
   captured from the conversation.  Currently five types of dialog
   objects are defined in this document:

   *  Text based media communications

   *  Audio or Video recorded media communications

   *  Metadata for failed or incompleted communications

   *  Metadata for providing relationships between other Dialog Objects
      in transfer scenarios

   *  Metadata for providing relationships between recording Dialog
      Objects in recording-set scenarios
```

**74.** (§4.3 (the two media constraints))

> Media captured in a media-based Dialog Object (type text and
> recording) SHOULD satisfy two constraints: the media is part of the
> conversation itself, and the media is transcribable.  Media is part
> of the conversation when it is the communication exchanged between
> the parties, as opposed to a document or item that is referenced,
> discussed or presented within the conversation.  Media that is
> transcribable can be converted into a textual representation of
> sequential communication between parties.  Text media is already in
> textual form and is therefore always transcribable.  While images
> such as sunsets, cows, photographs of documents, or application forms
> may be describable, they are not transcribable in a concise manner
> and SHOULD NOT be included as Dialog Objects.  They SHOULD be
> included as Attachment Objects.

**75.** (§4.3) _[lowercase]_

> Text and audio may be subject to interpretation, but they are
> transcribable to a precise dialog representation.  Although
> transcriptions may not always be accurate, there exists a single
> correct transcription for any given content.

**76.** (§4.3)

> Media that is not transcribable SHOULD be included in the vCon as
> Attachment Objects rather than Dialog Objects.

**77.** (§4.3 (fax, photograph, music))

> Whether a fax or photograph of a text-based letter belongs in a
> Dialog Object depends upon its role in the conversation.  A letter
> faxed to the other party as the communication itself, such as a
> letter faxed to a doctor, is both transcribable and part of the
> conversation and MAY be included as a Dialog Object.  The same letter
> shared or discussed within some other conversation is referenced
> material rather than the conversation itself and SHOULD be included
> as an Attachment Object, even though it is transcribable.  Most other
> faxes and photographs SHOULD be included as Attachment Objects and
> SHOULD NOT be included as Dialog Objects.  Similarly, a musical
> recording, even if it is in MP3 audio format, SHOULD be included as
> an Attachment and SHOULD NOT be included as a Dialog Object.

**78.** (§4.3) _[lowercase]_

> It may not always be known at the time of vCon construction whether
> an image or recording is transcribable.

**79.** (§4.3 (why the distinction binds)) _[lowercase]_

> This distinction is important for interoperability.  If it is
> ambiguous as to what belongs in a Dialog Object versus an Attachment
> Object, interoperability cannot be achieved, as vCon constructors
> will not be able to consistently determine where content should be
> placed and users of vCons will not know where content can be found
> within the vCon.

**80.** (§4.3 (placeholder Dialog Objects))

> There are situations when little or no information is available for a
> dialog either initially or over the entire life of the vCon and yet
> it is known that the dialog occurred.  For example this may occur in
> some call transfer cases where there is nothing known about the
> consultative call.  In such situations, it is possible to have a
> placeholder Dialog Object which contains only the type parameter and,
> for the "incomplete" type, the required disposition parameter.  As
> the consultative call is a call, a placeholder Dialog Object for it
> MUST be of type "recording" if the call was set up, or of type
> "incomplete" if it was not.  There may be more than one placeholder
> Dialog Object in the vCon.  They are distinct by the order or index
> in the Dialog Object array.

Lowercase obligation: *"for the \"incomplete\" type, the required disposition parameter"*. The `MUST` in this entry is the one that fixes which type a placeholder takes.


#### Section 4.3.1. type

**81.** (§4.3.1)

```
   *  type: "String"

   The string MUST have the value of either "recording", "recording-
   set", "text", "transfer" or "incomplete".  The semantics of each
   Dialog Object type are described in the following subsections.  The
   applicability of each of the Dialog Object parameters to each of the
   types is summarized in Section 4.3.1.6.
```


##### Section 4.3.1.1. recording

**82.** (§4.3.1.1) _[lowercase]_

> A dialog of type "recording" has Dialog Content that either contains
> a body or refers to via url, which is a recording of the video and/or
> audio of a segment of the conversation.  A recording Dialog Object
> that is part of a set of recordings which collectively represent a
> call or session, may reference the associated recording-set Dialog
> Object via the recording_set parameter (see Section 4.3.7).


##### Section 4.3.1.2. recording-set

**83.** (§4.3.1.2) _[lowercase]_

> A dialog of type "recording-set" contains metadata describing a set
> of "recording" Dialog Objects that collectively represent a call or
> session.  The conversation itself is captured in the referenced
> "recording" Dialog Objects; a recording-set Dialog Object does not
> have Dialog Content (see Section 4.3.10).  The recordings parameter
> identifies the "recording" Dialog Objects in the set (see
> Section 4.3.6).  The start, duration, parties and session_id
> parameters of a recording-set Dialog Object describe the call or
> session as a whole (see Section 4.3.2, Section 4.3.3, Section 4.3.4
> and Section 4.3.12).


##### Section 4.3.1.3. text

**84.** (§4.3.1.3) _[lowercase]_

> A dialog of type "text" has Dialog Content that either contains a
> body or refers to via url, which contains the text from one of the
> parties for a segment of the conversation.


##### Section 4.3.1.4. transfer

**85.** (§4.3.1.4) _[lowercase]_

> A dialog of type "transfer" does not capture actual conversation
> exchange, but rather captures operations, parties and relations
> between dialog segments.  The conversation is captured in other
> Dialog Objects; a transfer Dialog Object does not have Dialog Content
> (see Section 4.3.10).  The Dialog Transfer parameters are used to
> show the roles and relationships between the parties and other Dialog
> Objects as the transfer process occurred (see Section 4.3.14).


##### Section 4.3.1.5. incomplete

**86.** (§4.3.1.5) _[lowercase]_

> A dialog of type "incomplete" captures a call or conversation that
> failed to be setup to the point of exchanging any conversation.  As
> no conversation was exchanged, an incomplete Dialog Object does not
> have Dialog Content (see Section 4.3.10).  An incomplete Dialog
> Object has a required disposition parameter which indicates why the
> call or conversation failed (see Section 4.3.11).

Lowercase obligation: *"An incomplete Dialog Object has a required disposition parameter"*.


##### Section 4.3.1.6. Dialog Object Parameter Applicability by Type

**This is the single most load-bearing block in the document and the one the
previous extraction omitted.** A Dialog Object that satisfies the JSON Schema
in Appendix B can still be invalid, because which parameters apply depends on
`type`, and that dependency is expressed *only* here and in the individual
parameter definitions. Six symbols, five columns, twenty-five rows, four
footnotes. The symbol legend is itself normative: five of the six symbols are
defined by a BCP 14 keyword.

**87.** (§4.3.1.6 (status of the table)) _[lowercase]_

> The following table summarizes which Dialog Object parameters apply
> to each Dialog Object type.  The parameter definitions in the
> subsections of this document are definitive; this table is provided
> as a summary.

Lowercase obligation: *"The parameter definitions in the subsections of this document are definitive; this table is provided as a summary."* — where the table and a subsection disagree, the subsection wins.

**88.** (§4.3.1.6 (symbol legend))

```
   The symbols used in the table are defined as follows.

   M  The parameter MUST be present.

   S  The parameter SHOULD be present.

   O  The parameter is optional.

   SN  The parameter SHOULD NOT be present.

   X  The parameter MUST NOT be present.

   -  The parameter has no defined meaning for this type; it MAY be
      present but its semantics are undefined.
```

Table 1 itself. It crosses a page boundary between the `encoding` and `url`
rows; the pagination is removed and the table is reproduced as one grid,
byte-exactly otherwise.

**89.** (§4.3.1.6 (Table 1)) _[lowercase]_

```
   +=================+=========+=============+=====+========+==========+
   | Parameter       |recording|recording-set|text |transfer|incomplete|
   +=================+=========+=============+=====+========+==========+
   | type            |M        |M            |M    |M       |M         |
   +-----------------+---------+-------------+-----+--------+----------+
   | start           |S        |S            |S    |O       |S         |
   +-----------------+---------+-------------+-----+--------+----------+
   | duration        |O        |O            |O    |-       |O         |
   +-----------------+---------+-------------+-----+--------+----------+
   | parties         |S        |S            |S    |X       |O         |
   +-----------------+---------+-------------+-----+--------+----------+
   | originator      |O        |O            |O    |X       |O         |
   +-----------------+---------+-------------+-----+--------+----------+
   | recordings      |X        |M            |X    |X       |X         |
   +-----------------+---------+-------------+-----+--------+----------+
   | recording_set   |O        |X            |X    |X       |X         |
   +-----------------+---------+-------------+-----+--------+----------+
   | mediatype       |M (1)    |X            |M    |X       |X         |
   |                 |         |             |(1)  |        |          |
   +-----------------+---------+-------------+-----+--------+----------+
   | filename        |O        |X            |O    |X       |X         |
   +-----------------+---------+-------------+-----+--------+----------+
   | body            |S (2)    |X            |S    |X       |X         |
   |                 |         |             |(2)  |        |          |
   +-----------------+---------+-------------+-----+--------+----------+
   | encoding        |S (3)    |X            |S    |X       |X         |
   |                 |         |             |(3)  |        |          |
   +-----------------+---------+-------------+-----+--------+----------+
   | url             |S (2)    |X            |S    |X       |X         |
   |                 |         |             |(2)  |        |          |
   +-----------------+---------+-------------+-----+--------+----------+
   | content_hash    |S (4)    |X            |S    |X       |X         |
   |                 |         |             |(4)  |        |          |
   +-----------------+---------+-------------+-----+--------+----------+
   | disposition     |SN       |SN           |SN   |SN      |M         |
   +-----------------+---------+-------------+-----+--------+----------+
   | session_id      |O        |O            |O    |X       |O         |
   +-----------------+---------+-------------+-----+--------+----------+
   | party_history   |O        |O            |O    |X       |O         |
   +-----------------+---------+-------------+-----+--------+----------+
   | transferee      |X        |X            |X    |S       |X         |
   +-----------------+---------+-------------+-----+--------+----------+
   | transferor      |X        |X            |X    |S       |X         |
   +-----------------+---------+-------------+-----+--------+----------+
   | transfer_target |X        |X            |X    |O       |X         |
   +-----------------+---------+-------------+-----+--------+----------+
   | original        |X        |X            |X    |S       |X         |
   +-----------------+---------+-------------+-----+--------+----------+
   | consultation    |X        |X            |X    |O       |X         |
   +-----------------+---------+-------------+-----+--------+----------+
   | target_dialog   |X        |X            |X    |S       |X         |
   +-----------------+---------+-------------+-----+--------+----------+
   | application     |O        |O            |O    |O       |O         |
   +-----------------+---------+-------------+-----+--------+----------+
   | message_id      |O        |X            |O    |X       |X         |
   +-----------------+---------+-------------+-----+--------+----------+

                                  Table 1
```

**90.** (§4.3.1.6 (footnotes to Table 1))

```
   (1) MUST be present for inline Dialog Content; optional for
   externally referenced Dialog Content when the media type is provided
   in the [HTTPS] Content-Type header; not required when Dialog Content
   is absent, such as in a placeholder Dialog Object or a redacted vCon.

   (2) body or url MAY be absent in a redacted vCon.

   (3) MUST be present when the body parameter is present and is not an
   empty string (see Inline Files (Section 2.3)).

   (4) MUST be present when the url parameter is present (see
   Section 2.4.2).
```


#### Section 4.3.2. start

**91.** (§4.3.2)

```
   The start parameter contains the date and time for the beginning of
   the captured piece of dialog.  The start parameter SHOULD be present
   unless it is not known.  For text it is the time that the party
   started typing or if not available, then it is the time the text was
   sent.  For audio and video recordings, it is the time which
   corresponds to the beginning of the recording.  For a recording-set
   Dialog Object, it is the time corresponding to the beginning of the
   call or session.  It should be noted that Dialog Objects may not be
   ordered by the value of the start parameter.  Dialog Objects in the
   dialog array are in order that they were added to the vCon and cannot
   be reordered with out correcting the dialog indices which occur in
   other Objects in the vCon.  The start parameter is optional for the
   "transfer" type Dialog Object as it may not always be known.

   *  start: "Date"
```


#### Section 4.3.3. duration

**92.** (§4.3.3)

```
   The duration parameter contains the duration in seconds of the
   referenced or included piece of dialog.  For text, if known, it is
   the time duration from when the party started typing to when they
   completed typing and the text was sent.  For recordings, it is the
   duration of the recording.  For a recording-set Dialog Object, it is
   the duration of the call or session.  The start and duration
   parameters of a recording-set Dialog Object identify the complete
   time interval represented by the associated recording Dialog Objects.
   The duration parameter is not applicable to the "transfer" type
   Dialog Object.  For an "incomplete" type Dialog Object, the duration
   parameter may capture the time from the attempt to setup the call or
   conversation until it failed.

   *  duration: "UnsignedInt" | "UnsignedFloat" (optional)

   The value MUST be the dialog duration in seconds.
```


#### Section 4.3.4. parties

**93.** (§4.3.4)

```
   The party(s) which generated the text or recording for this piece of
   dialog are indicated in the parties parameter.  The parties parameter
   SHOULD be present in "recording", "recording-set" and "text" type
   Dialog Objects.  The parties parameter MUST NOT be present in
   "transfer" type Dialog Objects (see Section 4.3.14).  The parties
   parameter is optional for "incomplete" type Dialog Objects, where it
   indicates the parties between which the call or conversation setup
   was attempted.

   *  parties: "UnsignedInt" | "UnsignedInt[]" | ("UnsignedInt" |
      "UnsignedInt[]")[]
```

**94.** (§4.3.4 (single channel))

> Single channel recordings should have a parties value of the form:
> "UnsignedInt" or "UnsignedInt[]" where the integer value or array of
> integer values are the indices to the Party Object(s) in the parties
> array that contributed to the mix for the single channel recording.
> The index for the Party Object SHOULD be included even if the
> indicated party was silent the entire piece of dialog.

Lowercase obligation: *"Single channel recordings should have a parties value of the form"* — lowercase `should` introducing the single-channel form, immediately above a `MUST` for the multi-channel form.

**95.** (§4.3.4 (multi-channel))

> Multi-channel recordings MUST have a parties value that is an array
> of the same size as the number of channels in the recording.  The
> values in that array are either an integer or an array of integers
> which are the indices to the parties that contributed to the mix for
> the associated channel of the recording.  The index for Party Objects
> SHOULD be included even if the party was silent the entire
> conversation.  If not all channels are used in a recording, such that
> no parties are recorded on one or more channels, a null placeholder
> MUST be inserted into the parties array for the corresponding
> channel.

**96.** (§4.3.4 (segmented recordings and recording-set))

> Some recording systems represent a single call or session using
> multiple recording Dialog Objects.  This may occur when recordings
> are periodically segmented or when separate recordings are created
> for each party and talk spurt.  In these cases, a single recording
> Dialog Object identifies only the parties captured, or potentially
> captured, in that recording.  Other participants are identified only
> in the recording Dialog Objects in which they are captured or
> potentially captured.  As a result, no single recording Dialog Object
> necessarily identifies all parties participating in the conversation.
> Similarly, party_events need to be associated with a Dialog Object,
> but a recording Dialog Object may not exist for the point in time at
> which the event occurs.  A recording-set Dialog Object MAY be used to
> represent the complete call or session.  The start parameter of a
> recording-set Dialog Object identifies the beginning of the call or
> session.  The duration parameter of a recording-set Dialog Object
> identifies the duration of the call or session.  The parties
> parameter of a recording-set Dialog Object SHOULD contain all parties
> known to participate in the call or session, regardless of whether
> they contribute recorded media.

**97.** (§4.3.4 (implied originator)) _[lowercase]_

> It is implied that the first party in the dialog Object parties list,
> is the originator of the dialog.  However, in some situations, it is
> difficult to impose the constraint that the first channel of a
> recording is the originator.  If ensuring that the first channel and
> party listed is the originator is not possible, the optional
> originator parameter indicates the originator party.  In other cases,
> there may be a separate recording file for each party in a
> conversation, where only one party is recorded per file.  In this
> situation, it is necessary to indicate the originator as the dialog
> Object parties parameter may contain only one party and may not be
> the originator.  It should be noted that the recordings may be
> shorter than the collective conference when there is a separate
> recording per speaker/party.  For example the recording(s) of the
> individual speaker may be trimmed to only the parts where they are
> actually speaking.

**98.** (§4.3.4 (email))

> In the email context, [SMTP] messages have the headers From, To, Cc
> and Bcc that all correspond to parties to the text Dialog Object.
> The From header should be the first party index in the parties
> parameter for the text Dialog Object.  They are the implied
> originator.  The parties listed in the To, Cc and Bcc [SMTP] headers
> (if present) should all be added in that order to the parties
> parameter in the text Dialog Object.  The sender SHOULD be allowed to
> set a policy, through out of band means, as to whether they would
> like their application or server to include the Bcc parties in the
> vCon.  A text Dialog Object should only contain a single [SMTP]
> message.  Each may have a different set of parties.

Lowercase obligation: *"The From header should be the first party index"*; *"The parties listed in the To, Cc and Bcc [SMTP] headers (if present) should all be added in that order"*; *"A text Dialog Object should only contain a single [SMTP] message."* — three lowercase `should`s carrying the entire email-to-vCon mapping, around one `SHOULD` about Bcc policy.


#### Section 4.3.5. originator

**99.** (§4.3.5)

```
   The originator party for this dialog.  For email and text, this is
   the sender of the text.  For audio and video calls, this is the
   calling party.  For a scheduled meeting or conference, this is the
   organizer, the party that scheduled or created the meeting.  The
   organizer may be a party that never joins the conference; such a
   party may still be included in the parties array.  The organizer is
   distinct from the party acting as host or controller of the
   conference at any point during the meeting; identifying the host or
   controller is out of scope for this document.  If the originator is
   not known, an empty Party Object (see Party Object (Section 4.2)) may
   be used as the first party or as the party referenced by the
   originator parameter.  The originator parameter is only provided if
   the first party of the dialog Object parties list is NOT the
   originator.  The originator parameter MUST NOT be present in
   "transfer" type Dialog Objects (see Section 4.3.14).

   *  originator: "UnsignedInt" (optional)

   The originator value is the index into the parties Objects Array, to
   the party that originated the dialog.
```


#### Section 4.3.6. recordings

**100.** (§4.3.6)

```
   The recordings parameter identifies the recording Dialog Objects that
   are part of the recording-set Dialog Object.

   *  recordings: "UnsignedInt[]"

   The recordings parameter contains the indices of all recording Dialog
   Objects that are part of the recording-set.  The recordings parameter
   MUST be present in recording-set Dialog Objects.  The recordings
   parameter MUST NOT be present in other Dialog Object types.
```


#### Section 4.3.7. recording_set

**101.** (§4.3.7)

```
   The recording_set parameter identifies the recording-set Dialog
   Object to which the recording Dialog Object belongs.

   *  recording_set: "UnsignedInt" (optional; SHOULD be present when the
      recording is part of a recording-set)

   The recording_set parameter SHOULD be present when a recording Dialog
   Object is part of a recording-set Dialog Object.  The recording_set
   parameter MUST NOT be present in other Dialog Object types.
```


#### Section 4.3.8. mediatype

**102.** (§4.3.8)

```
   The media type for the piece of dialog included or referenced is
   provided in the mediatype parameter.  The mediatype parameter MUST be
   provided for inline dialog files and MUST be provided if the Content-
   Type header in the [HTTPS] response for the externally referenced URL
   is not provided.  The mediatype parameter is not required when the
   Dialog Content is absent, such as in a placeholder Dialog Object or
   when the body and url have been redacted.  The mediatype parameter
   MUST NOT be present in "recording-set", "transfer" or "incomplete"
   type Dialog Objects as they do not have Dialog Content.

   *  mediatype: "Mediatype" (optional for externally referenced files,
      if absent, this is provided in the [HTTPS] Content-Type header)
```

**103.** (§4.3.8 (media type token values))

```
   The media types SHOULD be one of the following strings:

   *  "text/plain"

   *  "audio/x-wav"

   *  "audio/x-mp3"

   *  "audio/x-mp4"

   *  "audio/ogg"

   *  "video/x-mp4"

   *  "video/ogg"

   *  "multipart/mixed"

      Note: multi-part will also likely include the boundary parameter
```


#### Section 4.3.9. filename

**104.** (§4.3.9)

```
   It is sometimes useful to preserve the name of the file which
   originally contained this piece of dialog.  This can be done in the
   filename parameter.  The filename parameter MUST NOT be present in
   "recording-set", "transfer" or "incomplete" type Dialog Objects as
   they do not have Dialog Content.

   *  filename: "String" (optional)
```


#### Section 4.3.10. Dialog Content

**105.** (§4.3.10)

```
   The Dialog Object SHOULD contain the body and encoding parameters or
   the url and content_hash parameters for all dialog types other than
   "incomplete", "transfer" and "recording-set", these parameters MUST
   NOT be present for "incomplete", "transfer" or "recording-set" dialog
   types (see Inline Files (Section 2.3) and Externally Referenced Files
   (Section 2.4)).  The exception to this is that the body or url MAY be
   absent if it is redacted.

   For inline included dialog:

   *  body: "*" (optional in a redacted vCon)

   *  encoding: "String"

   Alternatively, for externally referenced dialog:

   *  url: "String" (optional in a redacted vCon)

   *  content_hash: "ContentHash" | "ContentHash[]"
```


#### Section 4.3.11. disposition

**106.** (§4.3.11)

> If the dialog type is "incomplete", it MUST have a disposition
> parameter.  If the reason that the call or conversation failed is not
> known, such as in a placeholder Dialog Object, the disposition value
> "failed" SHOULD be used.  The value of the disposition parameter
> provides the reason that the "call control" failed.  The term: "call
> control" is used in a loose sense, as there in not always a call
> involved, to differentiate from a call disposition that an agent may
> assign to a call to indicate the reason, issue addressed or outcome
> of a conversation.  This latter definition of call disposition is not
> dialog, but analysis of the conversation and is not included in the
> dialog portion.

**107.** (§4.3.11 (type declaration))

```
   *  disposition: "String" (required for incomplete type Dialog
      Objects, SHOULD NOT be present for other dialog types)
```

**108.** (§4.3.11 (disposition token values))

```
   The value of the disposition parameter MUST be one of the following
   string:

   *  "no-answer" - a call or connection was attempted, but no one
      answered or accepted the connection

   *  "congestion" - a call or connection was attempted, but was unable
      to be completed due to system load

   *  "failed" - a call or connection was attempted, but failed

   *  "busy" - a call or connection was attempted, but the party was
      busy with another conversation

   *  "hung-up" - a call or connection was made, but the party hung-up
      before any conversation occurred

   *  "voicemail-no-message" - a call or connection was made, the
      voicemail system answered, but no message was left

      Note: if a message was left with the voicemail system this is no
      longer an "incomplete" type dialog, it is a "recording" type and
      the conversation SHOULD be included in the Dialog Content.
```


#### Section 4.3.12. session_id

**109.** (§4.3.12)

```
   The [SESSION-ID] MAY be included for the dialog.  If the same
   [SESSION-ID] applies to all the parties in a dialog, than a single
   instance of the SessionId Object is provided as the value of
   session_id.  If some parties have a different or no associated
   [SESSION-ID] for this Dialog Object, then the array structure of the
   session_id objects MUST correlate to the array structure of the
   Dialog Object's parties index array.  Parties which do not have a
   [SESSION-ID] associated with this dialog, MUST have an empty object
   ({}) for the SessionId Object.  That an empty Object and not an
   Object with two "nil UUIDs" as defined in section 7 of [SESSION-ID].
   It is also possible that the SessionId Object will not have values
   for both the local and remote parameters in some conferencing
   situations (See [SESSION-ID]).  In the case that one end of the
   [SESSION-ID] does not have a UUID, the "nil UUID" String value SHOULD
   be used as defined in section 7 of [SESSION-ID].  For a recording-set
   Dialog Object, a single SessionId Object value applies to the whole
   call or session represented by the set.  The individual recording
   Dialog Objects in the set may each capture only a leg or subset of
   the parties of the call or session; the session_id values on those
   recording Dialog Objects follow the party correlation rules above.
   The recording-set Dialog Object is the appropriate place to capture a
   session identifier that applies to the call or session as a whole.
   The session_id parameter MUST NOT be present in "transfer" type
   Dialog Objects.

   *  session_id: "SessionId" | "SessionId[]" | ("SessionId" |
      "SessionId[]")[] (optional)
```


#### Section 4.3.13. party_history Objects Array

**110.** (§4.3.13)

```
   Participants in a dialog may not all join and leave at the same time.
   To support the capturing of the information when parties join, drop,
   go on hold or mute and unmute, the party_history array may be added
   to the Dialog Object.  The party_history parameter MUST NOT be
   present in "transfer" type Dialog Objects.

   *  party_history: "Party_History[]" (optional)
```


##### Section 4.3.13.1. Party_History Object

**111.** (§4.3.13.1)

```
   The Party_History Object contains the following parameters:

   *  party: "UnsignedInt"

      The index of the party for this event.

   *  time: "Date"

      The time at which this event occurred.

   *  event: "String"

      The string token for the event which MUST be one of the following:

      -  "join" - when the party joins the dialog

      -  "drop" - when the party drops out of the dialog

      -  "hold" - when the party is put on hold

      -  "unhold" - when the part is taken off hold

      -  "mute" - when the party is muted

      -  "unmute" - when the part is taken off mute

      -  "keydown" - when a DTMF or application key/button was pressed

      -  "keyup" - when a DTMF or application key/button was released

   *  button: "String" - (optional, required for keydown and keyup
      events)

   The button parameter value is the String value of the DTMF digit,
   character or string label for the button that was pressed or
   released.
```


#### Section 4.3.14. Dialog Transfer

**112.** (§4.3.14 (the three roles)) _[lowercase]_

```
   A dialog of type "transfer" documents the roles of three parties and
   the relationship between 2 or three dialog segments.  In a transfer
   operation, the roles of the three parties to a transfer are defined
   in [SIP-XFER] as:

   *  Transferee

   *  Transferor

   *  Transfer Target
```

**113.** (§4.3.14 (the two or three calls)) _[lowercase]_

```
   There are two or three calls in which the parties are connected:

   *  original call

   *  consultative call (optional as this call may not get created)

   *  target call
```

**114.** (§4.3.14 (transfer parameters, transferee, transferor))

```
   To capture the above roles and dialog segments, the following
   parameters are defined for the "transfer" type dialog and MUST NOT be
   present in other dialog types.  Each of these parameters SHOULD be
   present in the "transfer" type Dialog Object unless noted as
   optional.

   *  transferee: "UnsignedInt"

   The value of the transferee parameter is the index into the parties
   Object array to the party that played the role of the Transferee.

   *  transferor: "UnsignedInt"

   The value of the transferor parameter is the index into the parties
   Object array to the party that played the role of the Transferor.
```

**115.** (§4.3.14 (transfer_target)) _[lowercase]_

```
   *  transfer_target: "UnsignedInt" (optional)

   The value of the transfer_target parameter is the index into the
   parties Object array to the party that played the role of the
   Transfer Target.  The transfer_target is optional in the case where
   the transfer is abandoned before the target was identified.
```

**116.** (§4.3.14 (call-to-Dialog-Object mapping))

> The consultation, target_dialog and original parameters all refer to
> the Dialog Objects that correspond to the 2 to 3 calls that are part
> of a transfer.  These calls may end up spread across multiple Dialog
> Objects due to the nature of how the calls are recorded.  For example
> each party may be recorded in a separate file which will result in a
> dialog for each.  Alternatively a call may go on hold where recording
> is stopped and back off again resulting where recording is started
> again in a separate recording file, resulting in multiple Dialog
> Objects.  The values for the consultation, target_dialog and original
> parameters each reference a single Dialog Object.  When a call is
> represented by multiple recording Dialog Objects, a recording-set
> type Dialog Object which represents that call MAY be referenced (see
> Section 4.3.1.2).

**117.** (§4.3.14 (placeholders for unknown legs))

> There are scenarios where we know that a transfer has occurred, but
> we have no Dialog Object information for one or two of the
> consultation, target or transfer calls.  In this case a placeholder
> Dialog Object is created and its index is used for the consultation,
> target_dialog or original parameter.  A unique Dialog Object SHOULD
> be referenced for each role in the transfer.  However a Dialog Object
> may be referenced in more than one transfer dialogs when multiple
> transfers occur.

**118.** (§4.3.14 (original)) _[lowercase]_

```
   *  original: "UnsignedInt"

   The value of the original parameter is the index into the dialog
   Object array to the "recording", "recording-set" or "text" type
   Dialog Object for the original dialog between the Transferee and the
   Transferor.
```

**119.** (§4.3.14 (consultation)) _[lowercase]_

```
   *  consultation: "UnsignedInt" (optional)

   The value of the consultation parameter is the index into the Dialog
   Object array to the "recording", "recording-set", "text" or
   "incomplete" type Dialog Object for the consultative dialog between
   the Transferor and the Transfer Target.  It is also possible for
   there to be more than one consultation.  This may occur for a number
   of reasons.  Call attempts may fail.  The caller may decide the
   consultation with a party is not the desired transfer target.
```

**120.** (§4.3.14 (target_dialog)) _[lowercase]_

```
   *  target_dialog: "UnsignedInt"

   The value of the target_dialog parameter is the index into the Dialog
   Object array to the "recording", "recording-set", "text" or
   "incomplete" type Dialog Object for the target dialog between the
   Transferee and the Transfer Target.
```

**121.** (§4.3.14 (prohibited parameters)) _[lowercase]_

> A number of Dialog Object parameters are prohibited in "transfer"
> type Dialog Objects; see Section 4.3.1.6 for a summary and the
> individual parameter definitions for the normative statements.

**122.** (§4.3.14 (scope of the transfer type)) _[lowercase]_

> The "transfer" type dialog only captures the roles, operations and
> events of the parties and the dialog setup.  It does not capture the
> purpose or reason for the transfer as that is analysis to be captures
> in the analysis section of the Vcon after the conversation has
> occurred.


#### Section 4.3.15. application

**123.** (§4.3.15) _[lowercase]_

```
   The application parameter is used to capture the application,
   communication channel or context over which the conversation was
   held.  The conversation mode can be identified by looking at the
   dialog type.  However that does not different between different
   communication platform service providers or hosting service.  For
   example, the application parameter can be used to identify the web
   conference hosting service.

   *  application "String" (optional)
```


#### Section 4.3.16. message_id

**124.** (§4.3.16)

```
   Some messaging systems assign a unique message identifier to each
   message.  The message_id parameter is applicable to "recording" and
   "text" type Dialog Objects and MUST NOT be present in "recording-
   set", "transfer" or "incomplete" type Dialog Objects.  The message_id
   parameter may be used to label the message for either cross
   referencing back to the messaging system or to prevent the addition
   of duplicate messages to the vCon.  For example SMTP [SMTP] messages
   have a message-id in the SMTP header.  In the SMTP case a message may
   exist in multiple mailboxes or tags.  When exporting these SMTP
   messages, the message_id parameter may be used to avoid adding the
   same message, to the vCon containing the email thread, more than
   once.

   *  message_id: "String" (optional)
```


### Section 4.4. Attachment Object

**125.** (§4.4) _[lowercase]_

> Ancillary documents to the conversation are included or referenced in
> the Attachment Object.  There is no constraint on the types files
> which can be included or referenced.  As most modes of communication,
> that allow the exchange of files, do not constrain the file type, any
> file type may be included here.


#### Section 4.4.1. purpose

**126.** (§4.4.1) _[lowercase]_

```
   The purpose parameter may be used to provide a text base description
   of the purpose or point of the attachment.  There is no restricted
   set of values for this description.

   *  purpose: "String" (optional)
```


#### Section 4.4.2. start

**127.** (§4.4.2) _[lowercase]_

```
   The start parameter contains the date and time that the Attachment
   Object was sent/exchanged.  It should be noted that Attachment
   Objects may not be ordered by the value of the start parameter.
   Attachment Objects in the attachments array are in order that they
   were added to the vCon and cannot be reordered with out correcting
   the attachment indices which may occur in other Objects in the vCon.

   *  start: "Date"
```


#### Section 4.4.3. party

**128.** (§4.4.3)

```
   In most conversations, ancillary documents originate from one of the
   parties involved in the conversation.  This party is not necessarily
   the document's author, but rather the party that distributed the
   document.  The distributing party is identified by the party
   parameter in the Attachment Object.  To provide provenance for the
   attachment, the party index MUST be specified.  The identified party
   need not be a participant in the conversation itself.  For example,
   an organization that processes or constructs the vCon may add
   attachments containing information about the conversation.  The
   organization or entity that adds the attachment SHOULD be represented
   as a Party Object.

   *  party: "UnsignedInt"

   The value of the party parameter is the index into the Party Object
   array to the party that contributed the attachment.
```


#### Section 4.4.4. dialog

**129.** (§4.4.4) _[lowercase]_

```
   Attachments are added as data related to the dialog.  The dialog
   parameter is used to identify the dialog that the attachment is part
   of.  The dialog is identified by the index to the dialog Object in
   the dialog objects array.

   *  dialog: "UnsignedInt"
```


#### Section 4.4.5. mediatype

**130.** (§4.4.5)

```
   The media type for the included or referenced attachment file is
   provided in the mediatype parameter.  The mediatype parameter MUST be
   provided for inline attachment files and MUST be provided if the
   Content-Type header in the [HTTPS] response for the externally
   referenced URL is not provided.  The mediatype parameter is not
   required when the Attachment Content is absent, such as when the body
   and url have been redacted.

   *  mediatype: "Mediatype" (optional for externally referenced files,
      if absent, this is provided in the [HTTPS] Content-Type header)

   The mediatype string contains the media type or [MIME] type of the
   attached file.
```


#### Section 4.4.6. filename

**131.** (§4.4.6) _[lowercase]_

```
   It is sometimes useful to preserve the name of the file which
   originally contained this attachment file.  This can be done in the
   filename parameter.

   *  filename: "String" (optional)

   The file name string contains an optional name for the attachment
   file referenced in this Attachment Object.
```


#### Section 4.4.7. Attachment Content

**132.** (§4.4.7)

```
   The Attachment Object SHOULD contain the body and encoding parameters
   or the url and content_hash parameters (see Inline Files
   (Section 2.3) and Externally Referenced Files (Section 2.4)).  The
   exception to this is that the body or url MAY be absent if it is
   redacted.

   For inline included attachments:

   *  body: "*"

   *  encoding: "String"

   Alternatively, for externally referenced attachments:

   *  url: "String"

   *  content_hash: "ContentHash" | "ContentHash[]"
```


### Section 4.5. Analysis Object

**133.** (§4.5)

> Analysis is a broad and in some cases developing field.  This
> document does not attempt to suggest a SHOULD support list of types.
> Nor are formats for analysis data defined in this document.  That is
> for research and specification outside the scope of this document.
> For this reason the Analysis Object provides multiple ways to define
> the media type of the analysis file.  If a well known media type is
> defined, it SHOULD be used.  For analysis data or files types for
> which a media type is not defined, the vendor and schema parameters
> SHOULD be used.


#### Section 4.5.1. type

**134.** (§4.5.1)

```
   The type parameter is used to label the semantic type of analysis
   data.

   *  type: "String"

   The string value SHOULD be one of the following:

   *  "report"

   *  "sentiment"

   *  "summary"

   *  "transcript"

   *  "translation"

   *  "tts"
```


#### Section 4.5.2. dialog

**135.** (§4.5.2) _[lowercase]_

```
   Analysis typically pertains to one or more of the Dialog Objects in
   the dialog array.  The dialog parameter is used to indicate which
   Dialog Objects this analysis was based upon.

   *  dialog: "UnsignedInt" | "UnsignedInt[]" (optional only if the
      analysis was not derived from any of the dialog)

   The value of the dialog parameter is the index to the dialog or array
   of indices to the Dialog Object array to which this analysis object
   corresponds.
```


#### Section 4.5.3. attachment

**136.** (§4.5.3) _[lowercase]_

```
   The analysis may pertain to one or more of the Attachment Objects in
   the attachment array.  The attachment parameter is used to indicate
   which Attachment Objects this analysis was based upon.

   *  attachment: "UnsignedInt" | "UnsignedInt[]" (optional only if the
      analysis was not derived from any of the attachments)

   The value of the attachment parameter is the index to the attachment
   or array of indices to the Attachment Object array to which this
   analysis object corresponds.
```


#### Section 4.5.4. mediatype

**137.** (§4.5.4)

```
   The media type for the included or referenced analysis file is
   provided in the mediatype parameter.  The mediatype parameter SHOULD
   be provided for inline analysis files and for externally referenced
   analysis files when the Content-Type header in the [HTTPS] response
   is not provided.  A media type may not be defined for the format of
   the analysis data; in this case the vendor, product and schema
   parameters SHOULD be used to identify the data format instead.

   *  mediatype: "Mediatype" (optional)

   The mediatype string contains the media type or [MIME] type of the
   analysis file.
```


#### Section 4.5.5. filename

**138.** (§4.5.5) _[lowercase]_

```
   It is sometimes useful to preserve the name of the file which
   originally contained this analysis data.  This can be done in the
   filename parameter.

   *  filename: "String" (optional)

   The file name string contains an optional name for the analysis data
   file referenced in this Analysis Object.
```


#### Section 4.5.6. vendor

**139.** (§4.5.6) _[lowercase]_

```
   There may not be a IANA registered media type for the file format
   containing the analysis data.  Even if a media type is defined, it is
   often useful to keep a record of the vendor that produced the
   software that produced the analysis.  Different implementations
   perform differently and knowing the implementation can be useful in
   interpreting the analysis.  For this reason, the vendor or product
   name is provided in the vendor parameter.

   *  vendor: "String"

   The vendor string value contains the vendor or product name of the
   software which generated this analysis.
```


#### Section 4.5.7. product

**140.** (§4.5.7) _[lowercase]_

```
   As the vendor may have more than one product, the product parameter
   may be used to differentiate it from other products which may have
   different schemas of analysis data.

   *  product: "string" (optional)
```


#### Section 4.5.8. schema

**141.** (§4.5.8) _[lowercase]_

```
   The same vendor or software product may produce different formats or
   data for the same analysis.  The schema parameter allows the data
   format, schema or configuration used to generate the analysis to be
   saved with the included or referenced analysis data.

   *  schema: "String" (optional)

   The schema string contains a token or label for the data format or
   schema for the analysis data.  As the vendor name may not be specific
   enough to identify the format of the analysis, the schema value is
   provide to differentiate from potentially multiple data formats for
   analysis provided by the same vendor or software.
```


#### Section 4.5.9. Analysis Content

**142.** (§4.5.9)

```
   The Analysis Object SHOULD contain the body and encoding parameters
   or the url and content_hash parameters (see Inline Files
   (Section 2.3) and Externally Referenced Files (Section 2.4)).  The
   exception to this is that the body or url MAY be absent if it is
   redacted.

   For inline included analysis:

   *  body: "*"

   *  encoding: "String"

   Alternatively, for externally referenced analysis:

   *  url: "String"

   *  content_hash: "ContentHash" | "ContentHash[]"
```


## Section 5. Security Considerations

**143.** (§5 (the two categories)) _[lowercase]_

> The security concerns for vCons can put into two categories: making
> the conversation immutable through integrity verification and
> protecting the confidentiality of privacy of the parties to the
> conversation and/or their PII.  These requirements along with need to
> evolve a vCon (e.g. adding analysis, translations and transcriptions)
> conflict in some ways.  To enable this, multiple versions of a vCon
> may be created.  Versions of a vCon may add information (e.g.
> analysis added to a prior vCon referenced by the amended
> (Section 4.1.9)) and versions that remove information (e.g.
> redactions of privacy information removed from the vCon referenced in
> the redacted (Section 4.1.8)).  Redactions may be at different levels
> for example:

**144.** (§5 (levels of redaction)) _[lowercase]_

```
   *  PII masked to remove PII data in the text, audio, video or
      transcripts

   *  De-identified to remove segments or whole recordings that might be
      used for voice printing or facial recognition
```

**145.** (§5 (security domains)) _[lowercase]_

```
   Different parts and versions of a vCon may be created in different
   security domains over a period of time.  In addition, some
   conversation data may be referenced externally through an HTTPS URL
   as opposed to completely contained within the vCon.  Typically a
   conversation of one mode, will be hosted or observed in a single
   domain.  This will likely fall into one of the following hosting
   situations:

   *  Enterprise Hosted Communications

   *  Software as a Service (SaaS) Hosted Communications

   *  Service Provider Hosted Communications
```

**146.** (§5 (crossing a security domain))

> The distinction among these has gotten clouded over recent years.
> The import consideration is that each is a different security domain.
> Information about a conversation captured in an enterprise
> communications system (e.g. meta data and Dialog Object(s) recorded
> in an IP PBX) is a different security domain from a SaaS
> transcription service (i.e. an Analysis Object).  Before a vCon
> leaves a security domain, it SHOULD be signed to prevent it from
> being altered.  If the new security domain needs to alter it, a new
> vCon is created with the removed or added data and the prior version
> is referenced (i.e. via the redacted (Section 4.1.8) or amended
> (Section 4.1.9)).  See the redacted vCon object tree figure-1 and
> amended vCon object tree figure-2.  If information is redacted for
> privacy reasons, the vCon referenced in the redacted (Section 4.1.8),
> if inline, SHOULD be encrypted to protect the privacy information in
> the unredacted version of the vCon.

**147.** (§5 (externally referenced data)) _[lowercase]_

> The secure storage and access of externally referenced conversation
> data is considered out of scope from this document.  Secure
> mechanisms for HTTPS access and storage of files are well defined.
> Identity and credentials for accessing externally stored data will be
> exchanged out of band from the vCon.  The one requirement for
> externally referenced data from the perspective of this document, is
> proof of integrity of that data.

Lowercase obligation: *"The one requirement for externally referenced data from the perspective of this document, is proof of integrity of that data."*

**148.** (§5 (reduction to signing and encryption)) _[lowercase]_

> Using the above described approach for redaction and amending of
> data, we can reduce the security operations on a vCon to signing and
> encryption.  Two approaches to signing are needed as we have data, in
> JSON format, that is contained within the vCon and may have data
> (typically media and file formats, often binary) not contained,
> inline in the vCon, that is externally referenced.

**149.** (§5 (why SHA-512 for external data)) _[lowercase]_

> Externally referenced data will be "signed" using [SHA-512] hash
> which along with the URL of the externally referenced data is
> included in the vCon.  [SHA-512] was chosen due to the relatively low
> cost to generate and verify the signature for what could be very
> large externally referenced media files.  As the hash for each
> externally referenced file is contained in the vCon which will be
> signed, the chain of authentication is provided via the signature on
> the vCon itself.

**150.** (§5 (why JOSE)) _[lowercase]_

> This document specifies the JSON format for vCons.  So it seemed the
> logical solution for signing vCons, is JOSE [JWS] JSON Serialization
> and likewise for encrypting vCons is JOSE [JWE] JSON Serialization.
> The solutions are well documents, implementations are readily
> available and tested.

**151.** (§5 (redaction and the unredacted original))

> Methods of redaction exist for text, audio and video using post
> processing of the media.  The method of redaction used is out of the
> scope of this document.  A redacted vCon SHOULD reference it's non-
> redacted version.  The non-redacted version of the vCon referenced
> from the redacted vCon MUST be encrypted such that only those with
> permission to view the non-redacted content can decrypt it.

**152.** (§5 (sharing outside the security domain))

> Any time a vCon is shared outside its original security domain, it
> SHOULD be signed and optionally encrypted.  Files externally
> referenced by a vCon SHOULD always be signed with the verification
> information included in the vCon that references the external file as
> defined in Externally Referenced Files (Section 2.4) and Signing
> Externally Referenced Files (Section 5.1).  Externally referenced
> files SHOULD only be transported over [HTTPS] and SHOULD be access
> controlled to those who are permitted to read the contents of that
> non-redacted vCon. vCons transported over non-secure channels such as
> email MUST be in the encrypted form.


### Section 5.1. Signing Externally Referenced Files

**153.** (§5.1)

> In some deployments, it is not practical to include all of the file
> contents of a vCon inline.  In support of that, a file may be
> externally referenced.  When external files are referenced, the
> signature on the vCon does not secure the file contents from
> modification.  For this reason any externally referenced files SHOULD
> also have a signature. vCons use the [SHA-512] hash method for
> integrity checking of externally referenced file content and include
> its url and content_hash in the vCon which are included in the
> integrity signature for the whole vCon.

**154.** (§5.1 (verification after retrieval)) _[lowercase]_

> After retrieving externally referenced files, before using its
> content, the payload of the HTTPS request should be verified using
> the signature parameter value for the hash for the url body using the
> procedure defined in section 6.3 and 6.4 of [SHA-512].

Lowercase obligation: *"the payload of the HTTPS request should be verified"* — the one statement that tells a consumer to actually check the hash it was given, and it is lowercase.


### Section 5.2. Signed Form of vCon Object

**155.** (§5.2)

> A signed vCon uses [JWS] and takes the General JWS JSON Serialization
> Syntax form as defined in section 7.2.1 of [JWS].  The vCon General
> JWS JSON Serialization MUST include x5c or x5u in the unprotected
> header.

**156.** (§5.2 (payload)) _[lowercase]_

```
   *  payload: "String"

   The value of the payload is the Base64Url Encoded string containing
   either: the unsigned form of the JSON vCon; or the gzipped [GZIP]
   unsigned form of the JSON vCon.  The general construction of the
   payload string value is described in section 7.2.1 of [JWS]
```

**157.** (§5.2 (signatures)) _[lowercase]_

```
   *  signatures: "Signature[]"

   The value of signatures is an array of Signature Objects
   (Section 5.2.1)
```


#### Section 5.2.1. Signature Object

**158.** (§5.2.1)

```
   The Signature Object MUST contain a header, protected and signature
   parameter as defined in section 7.2.1 of [JWS].

   *  header: "Header"

   The value of header is defined in Header Object (Section 5.2.2)

   *  protected: "String"

   *  signature: "String"
```


#### Section 5.2.2. Header Object

**159.** (§5.2.2)

> The Header Object and its contents are defined in section 4 of [JWS].
> The Header Object for a signed vCon MUST include the alg and either
> the x5c or x5u arrays.  The x5c or x5u requirement makes the
> management and use of vCons easier, allowing the certificate chain to
> be found as the vCon is moved.

**160.** (§5.2.2 (alg))

```
   *  alg: "String"

   The string value of alg is defined in section 4.1.1 of [JWS].  For a
   signed vCon this value SHOULD be "RS256" to maximize
   interoperability.
```

**161.** (§5.2.2 (x5c, x5u))

```
   *  x5c: "String[]" (MUST provide x5c or x5u)

   The array of string values for x5c are defined in section 4.1.6 of
   [JWS].

   *  x5u: "String" (MUST provide x5c or x5u)

   The string value of x5u MUST contain an [HTTPS] URL as defined in
   section 4.1.5 of [JWS].
```

**162.** (§5.2.2 (uuid))

```
   *  uuid: "String" (SHOULD be provided)

   The string value of the UUID for the vCon contained in the payload
   parameter.  This is added for convenience to not require verification
   of the signed vCon to get it's UUID.  When the vCon is verified, the
   value of this uuid parameter SHOULD be verified against the UUID in
   the signed vCon.
```


#### Section 5.2.3. Long Term Archiving of Signed vCons

**163.** (§5.2.3) _[lowercase]_

> In some use cases, it may be necessary to store or archive signed
> vCons for compliances or records purposes for as long as 10 years or
> more.  In most cases the keys and certificates used to sign the vCon
> and construct the [JWS] or signed form of the vCon, will have an
> expiration on the order of a few years at best.  Below is an approach
> on how integrity may be maintained on the archived vCon.  There may
> be other approaches to this as well.
>
> For our example illustrated below, we have a vCon which was signed
> (labeled as JWS1).  The certificate used to sign JWS1 has an
> expiration date.  Before the expiration of the JWS1 signing
> certificate, the content of JWS1 (the vCon) is verified and then JWS1
> is signed as the payload to construct JWS2.  Before the expiration of
> the JWS2 certificate, the contents of JWS2 (JWS1) is verified and
> then JWS2 is signed as the payload to construct JWS3.  The process is
> continued for the life of the vCon archiving.

**164.** (§5.2.3 (retrieval from the archive)) _[lowercase]_

> When it is desired to access the data in the archived vCon, first the
> outer JWS (JWS3 in diagram) is verified (payload of JWS2), then the
> vCon (payload in JWS1) is assumed to have valid integrity.

**165.** (§5.2.3 (nested JWS diagram)) _[lowercase]_

```
    ____________
   |    JWS3    |
   | __________ |
   ||   JWS2   ||
   || ________ ||
   |||  JWS1  |||
   ||| ______ |||
   |||| vCon ||||
   ||||______||||
   |||________|||
   ||__________||
   |____________|
```


### Section 5.3. Encrypted Form of vCon Object

**166.** (§5.3)

> A vCon MUST be signed first using JWS as defined in Signed Form of
> vCon Object (Section 5.2), then encrypted using JWE as opposed to
> just encrypted with integrity protection.  The rationale is that meta
> data and dialog will typically be collected in one security domain,
> then may be stored or exported to another.  The signing is likely for
> the lifetime of the vCon, where the encryption may be shorter term or
> domain specific. vCons may be stored in unencrypted form, but the
> signed form MUST be maintained to ensure its integrity.

**167.** (§5.3 (JWE serialization and members)) _[lowercase]_

```
   A encrypted vCon uses [JWE] and takes the General JWE JSON
   Serialization Syntax form as defined in section 7.2.1 of [JWE].

   *  unprotected: "Unprotected"

   *  recipients: "Recipient[]"

   *  iv: "String"

   The string value of iv is the Initialization Vector as constructed as
   defined in section 7.2.1 of [JWE].

   *  ciphertext: "String"

   The string value of ciphertext is constructed as defined in section
   7.2.1 of [JWE] using the signed form of the vCon as the plaintext
   input for encryption.

   *  tag: "String"

   The string value of tag is the the Authentication Tag as defined in
   section 7.2.1 of [JWE].
```


#### Section 5.3.1. Unprotected Object

**168.** (§5.3.1)

```
   *  cty: "String"

   The string value of cty SHOULD be either "application/vcon" or
   "application/vcon+gzip"

   *  enc: "String"

   The string value of enc SHOULD be "A256CBC-HS512"

   *  uuid: "String" (SHOULD be provided)
```

**169.** (§5.3.1 (uuid))

> The string value of the UUID for the vCon contained in the ciphertext
> parameter.  This is provided for identification of the encrypted vCon
> without the need of the key to decrypt the vCon.  The value of this
> uuid parameter SHOULD be verified when the vCon is decrypted.


#### Section 5.3.2. Recipient Object

**170.** (§5.3.2) _[lowercase]_

```
   *  header: "Header"

   *  encrypted_key: "String"

   The string value of encrypted_key is defined in section 7.2.1 of
   [JWE].
```


#### Section 5.3.3. Header Object

**171.** (§5.3.3)

```
   *  alg: "String"

   The string value of alg SHOULD be "RSA-OAEP".
```


### Section 5.4. Differentiation of vCon forms

**172.** (§5.4) _[lowercase]_

> vCons in the unsigned, signed and encrypted form are all valid JSON.
> A vCon in any of these forms may additionally be compressed using
> [GZIP] as described in Section 6.2.  It is necessary to distinguish
> which form a vCon is in, and whether it is compressed, in order to
> properly handle it.  For example a signed vCon needs to be verified.
> The following is the recommended approaches to identifying which form
> a particular vCon is in:

**173.** (§5.4 (form detection rules)) _[lowercase]_

```
   *  unsigned

      The presence of one or more of the following parameters indicates
      that the vCon is in the unsigned form:

      -  parties

      -  dialog

      -  analysis

      -  attachments

   *  signed (JWS)

      The presence of both of the following parameters indicates that
      the vCon is in the signed (JWS) form:

      -  payload

      -  signatures

   *  encrypted (JWE)

      The presence of both of the following parameters indicates that
      the vCon is in the encrypted (JWE) form:

      -  ciphertext

      -  recipients
```

**174.** (§5.4 (gzip))

> A gzip compressed vCon is not JSON and is differentiated from the
> JSON forms before the above parameter based rules can be applied.
> The gzip compressed vCon SHOULD be identified by the media type
> "application/vcon+gzip" when a media type is available, such as in
> the [HTTPS] Content-Type header.  When no media type is available, a
> gzip compressed vCon can be identified by the gzip member header
> magic numbers defined in section 2.3.1 of [GZIP].  Once decompressed,
> the contained vCon is in one of the JSON forms and is differentiated
> using the parameter based rules above.


## Section 6. IANA Considerations

**175.** (§6) _[lowercase]_

> This section includes the information required for IANA to register
> the application/vcon media type per [MEDIATYPE].


### Section 6.1. JSON Format vCon Mediatype

**176.** (§6.1) _[lowercase]_

> The JSON format for vCon is mandatory to implement.

Lowercase obligation: *"is mandatory to implement"* — the document's only mandatory-to-implement statement, and it is lowercase.

**177.** (§6.1 (application/vcon registration)) _[lowercase]_

```
   *  Type name: application

   *  Subtype name: vcon

   *  Required parameters: N/A

   *  Optional parameters: N/A; unrecognized parameters should be
      ignored.

   *  Encoding considerations: 8bit

   *  Additional information: [JSON] format

   *  Security considerations: See Security Considerations section of
      this document.

   *  Interoperability considerations: The vCon schema is defined in RFC
      XXXX.  The schema may be extended through extensions as defined
      there.

   *  Published specification: [VCON], this document: RFC XXXX

   *  Applications that use this media type:

   *  Fragment identifier considerations: N/A

   *  Additional Information:

      -  Deprecated alias names for this type: N/A

      -  Magic number(s): N/A

      -  File extension(s): "vcon"

      -  Macintosh file type code(s): N/A

      -  Windows Clipboard Name: VCON

   *  Author: See the Author's Addresses section of this document.

   *  Change controller: IETF
```

Lowercase obligation: *"unrecognized parameters should be ignored"*.


### Section 6.2. gzip Format vCon Mediatype

**178.** (§6.2)

> A gzip format vCon is a JSON format vCon that has been compressed
> using the gzip [GZIP] compression algorithm.  The gzip format is used
> to reduce the size of potentially very large vCons containing audio
> or video media in dialog objects.  Applications SHOULD support the
> receiving of gzip format vCons, but do not need to use the gzip
> format when sending.

**179.** (§6.2 (application/vcon+gzip registration)) _[lowercase]_

```
   *  Type name: application

   *  Subtype name: vcon+gzip

   *  Required parameters: N/A

   *  Optional parameters: N/A; unrecognized parameters should be
      ignored.

   *  Encoding considerations: binary

   *  Additional information: [GZIP] compression of [JSON] format

   *  Security considerations: See Security Considerations section of
      this document.

   *  Interoperability considerations: The vCon schema is defined in RFC
      XXXX.  The schema may be extended through extensions as defined
      there.

   *  Published specification: [VCON], this document: RFC XXXX

   *  Applications that use this media type:

   *  Fragment identifier considerations: N/A

   *  Additional Information:

      -  Deprecated alias names for this type: N/A

      -  Magic number(s): N/A

      -  File extension(s): "vcon"

      -  Macintosh file type code(s): N/A

      -  Windows Clipboard Name: VCON

   *  Author: See the Author's Addresses section of this document.

   *  Change controller: IETF
```

Lowercase obligation: *"unrecognized parameters should be ignored"*.


### Section 6.3. vCon JSON Registry

**180.** (§6.3) _[lowercase]_

> This document defines a number of new IANA registries for the JSON
> vCon schema.  Each Object (i.e. dict, map, dictionary) has its own
> registry of parameter names.  All of those registries have the same
> registry template which is defined in the following subsection.  When
> registering new entries, the following template should be used.

Lowercase obligation: *"When registering new entries, the following template should be used."*


#### Section 6.3.1. Object Registry Template

The template every per-Object parameter registry uses. The second sentence
of *Parameter Name* is the registry's one substantive rule and it is stated
in lowercase: case-sensitive names, no case-insensitive collisions, Designated
Expert override. The same rule is restated verbatim in §6.3.4.1.1, §6.3.5.1.1
and §6.4.1.

**181.** (§6.3.1) _[lowercase]_

```
   Parameter Name:

   The string name of a parameter to be used within the Object.  The
   name is case sensitive.  Names may not match other registered names
   in a case-insensitive manner unless the Designated Experts state that
   there is a compelling reason to allow an exception.

   Parameter Description:

   Brief description of the parameter

   Change Controller:

   For Standards Track RFCs, list the "IESG".  For others, give the name
   of the responsible party.  Other details (e.g., postal address, email
   address, home page URI) may also be included.

   Specification Document(s):

   Reference to the document or documents that specify the parameter,
   preferably including URIs that can be used to retrieve copies of the
   documents.  An indication of the relevant sections may also be
   included but is not required.
```

Lowercase obligation: *"Names may not match other registered names in a case-insensitive manner unless the Designated Experts state that there is a compelling reason to allow an exception."*


#### Section 6.3.2. vCon Object Parameter Names Registry

**182.** (§6.3.2 (Table 2)) _[lowercase]_

```
   The following defines the initial values for the vCon Object
   Parameter Names Registry.  Use the template in Object Registry
   Template (Section 6.3.1) when registering additional entries to this
   table.

   +=============+======================+============+================+
   | Parameter   | Parameter            | Change     | Specification  |
   | Name        | Description          | Controller | Document(s)    |
   +=============+======================+============+================+
   | vcon        | Schema version       | IESG       | Section 4.1.1  |
   |             | number               |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+
   | uuid        | vCon instance UUID   | IESG       | Section 4.1.2  |
   |             |                      |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+
   | extensions  | list of extensions   | IESG       | Section 4.1.3  |
   |             | used                 |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+
   | critical    | list of incompatible | IESG       | Section 4.1.4  |
   |             | extensions used      |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+
   | created_at  | creation date        | IESG       | Section 4.1.5  |
   |             |                      |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+
   | updated_at  | modification date    | IESG       | Section 4.1.6  |
   |             |                      |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+
   | subject     | conversation subject | IESG       | Section 4.1.7  |
   |             |                      |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+
   | redacted    | Redacted Object      | IESG       | Section 4.1.8  |
   |             |                      |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+
   | amended     | Amended Object       | IESG       | Section 4.1.8  |
   |             |                      |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+
   | group       | reserved for future  | IESG       | RFC XXXX       |
   |             | extension            |            |                |
   +-------------+----------------------+------------+----------------+
   | parties     | Party Objects array  | IESG       | Section 4.1.10 |
   |             |                      |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+
   | dialog      | Dialog Objects array | IESG       | Section 4.1.11 |
   |             |                      |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+
   | analysis    | Analysis Objects     | IESG       | Section 4.1.12 |
   |             | array                |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+
   | attachments | Attachment Objects   | IESG       | Section 4.1.13 |
   |             | array                |            | RFC XXXX       |
   +-------------+----------------------+------------+----------------+

                                 Table 2
```


#### Section 6.3.3. Party Object Parameter Names Registry

**183.** (§6.3.3 (Table 3)) _[lowercase]_

```
   The following defines the initial values for the Party Object
   Parameter Names Registry.  Use the template in Object Registry
   Template (Section 6.3.1) when registering additional entries to this
   table.

   +================+===================+============+================+
   | Parameter Name | Parameter         | Change     | Specification  |
   |                | Description       | Controller | Document(s)    |
   +================+===================+============+================+
   | tel            | tel URL           | IESG       | Section 4.2.1  |
   |                |                   |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+
   | sip            | SIP URL           | IESG       | Section 4.2.1  |
   |                |                   |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+
   | stir           | STIR token        | IESG       | Section 4.2.3  |
   |                |                   |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+
   | mailto         | mailto URL        | IESG       | Section 4.2.4  |
   |                |                   |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+
   | name           | participant name  | IESG       | Section 4.2.5  |
   |                |                   |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+
   | validation     | validation method | IESG       | Section 4.2.7  |
   |                |                   |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+
   | gmlpos         | participant       | IESG       | Section 4.2.8  |
   |                | geolocation       |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+
   | civicaddress   | civic address     | IESG       | Section 4.2.9  |
   |                |                   |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+
   | uuid           | participant       | IESG       | Section 4.2.10 |
   |                | unique identifier |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+
   | type           | participant type  | IESG       | Section 4.2.11 |
   |                |                   |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+
   | org            | participant       | IESG       | Section 4.2.12 |
   |                | organization      |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+
   | dept           | participant       | IESG       | Section 4.2.13 |
   |                | department        |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+
   | did            | decentralized     | IESG       | Section 4.2.6  |
   |                | identifier        |            | RFC XXXX       |
   +----------------+-------------------+------------+----------------+

                                 Table 3
```


#### Section 6.3.4. Dialog Object Parameter Names Registry

**184.** (§6.3.4 (Table 4)) _[lowercase]_

```
   The following defines the initial values for the Dialog Object
   Parameter Names Registry.  Use the template in Object Registry
   Template (Section 6.3.1) when registering additional entries to this
   table.

   +=================+=======================+==========+==============+
   | Parameter Name  | Parameter Description |Change    |Specification |
   |                 |                       |Controller|Document(s)   |
   +=================+=======================+==========+==============+
   | type            | dialog type name      |IESG      |Section 4.3.1 |
   |                 |                       |          |RFC XXXX      |
   +-----------------+-----------------------+----------+--------------+
   | start           | dialog start time     |IESG      |Section 4.3.2 |
   |                 |                       |          |RFC XXXX      |
   +-----------------+-----------------------+----------+--------------+
   | duration        | dialog duration       |IESG      |Section 4.3.3 |
   |                 | period                |          |RFC XXXX      |
   +-----------------+-----------------------+----------+--------------+
   | parties         | dialog parties list   |IESG      |Section 4.3.4 |
   |                 |                       |          |RFC XXXX      |
   +-----------------+-----------------------+----------+--------------+
   | originator      | dialog originator     |IESG      |Section 4.3.5 |
   |                 | party                 |          |RFC XXXX      |
   +-----------------+-----------------------+----------+--------------+
   | mediatype       | dialog content media  |IESG      |Section 4.3.8 |
   |                 | type                  |          |RFC XXXX      |
   +-----------------+-----------------------+----------+--------------+
   | filename        | dialog content        |IESG      |Section 4.3.9 |
   |                 | filename              |          |RFC XXXX      |
   +-----------------+-----------------------+----------+--------------+
   | body            | dialog inline content |IESG      |Section       |
   |                 |                       |          |4.3.10 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | encoding        | dialog inline content |IESG      |Section       |
   |                 | encoding              |          |4.3.10 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | url             | dialog referenced     |IESG      |Section       |
   |                 | content URL           |          |4.3.10 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | content_hash    | dialog content hash   |IESG      |Section       |
   |                 |                       |          |4.3.10 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | disposition     | dialog disposition    |IESG      |Section       |
   |                 |                       |          |4.3.11 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | session_id      | RFC7989 session ID    |IESG      |Section       |
   |                 |                       |          |4.3.12 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | party_history   | dialog party events   |IESG      |Section       |
   |                 | history               |          |4.3.13 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | transferee      | transferee party      |IESG      |Section       |
   |                 | index                 |          |4.3.14 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | transferor      | transferor party      |IESG      |Section       |
   |                 | index                 |          |4.3.14 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | transfer_target | transfer target party |IESG      |Section       |
   |                 | index                 |          |4.3.14 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | original        | original transfer     |IESG      |Section       |
   |                 | dialog index          |          |4.3.14 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | consultation    | consultation`transfer |IESG      |Section       |
   |                 | dialog index          |          |4.3.14 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | target_dialog   | target_dialog         |IESG      |Section       |
   |                 | transfer dialog index |          |4.3.14 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | application     | dialog source         |IESG      |Section       |
   |                 | application           |          |4.3.15 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | message_id      | dialog message id     |IESG      |Section       |
   |                 |                       |          |4.3.16 RFC    |
   |                 |                       |          |XXXX          |
   +-----------------+-----------------------+----------+--------------+
   | recordings      | multi recording       |IESG      |Section 4.3.6 |
   |                 | dialog reference      |          |RFC XXXX      |
   +-----------------+-----------------------+----------+--------------+
   | recording_set   | recording_set dialog  |IESG      |Section 4.3.7 |
   |                 | reference             |          |RFC XXXX      |
   +-----------------+-----------------------+----------+--------------+

                                  Table 4
```


##### Section 6.3.4.1. Dialog Type Name Registry

**185.** (§6.3.4.1) _[lowercase]_

> This document defines a new registry for the token name values that
> are permitted as values to the dialog type (Section 4.3.1) parameter.


###### Section 6.3.4.1.1. Dialog Type Name Registration Template

**186.** (§6.3.4.1.1) _[lowercase]_

```
   Dialog Type Name:

   The string token name of a Dialog Object Type The name is case
   sensitive.  Names may not match other registered names in a case-
   insensitive manner unless the Designated Experts state that there is
   a compelling reason to allow an exception.

   Dialog Type Description:

   Brief description of the Dialog Object type

   Change Controller:

   For Standards Track RFCs, list the "IESG".  For others, give the name
   of the responsible party.  Other details (e.g., postal address, email
   address, home page URI) may also be included.

   Specification Document(s):

   Reference to the document or documents that specify the parameter,
   preferably including URIs that can be used to retrieve copies of the
   documents.  An indication of the relevant sections may also be
   included but is not required.
```

Lowercase obligation: *"Names may not match other registered names in a case-insensitive manner unless the Designated Experts state that there is a compelling reason to allow an exception."*


###### Section 6.3.4.1.2. Dialog Type Name Registration Initial Values

**187.** (§6.3.4.1.2 (Table 5)) _[lowercase]_

```
   The following table defines the initial values for the Dialog Object
   Types Registry.

    +==================+=================+============+===============+
    | Dialog Type Name | Dialog Type     | Change     | Specification |
    |                  | Description     | Controller | Document(s)   |
    +==================+=================+============+===============+
    | text             | text dialog     | IESG       | Section 4.3.1 |
    |                  |                 |            | RFC XXXX      |
    +------------------+-----------------+------------+---------------+
    | recording        | recording       | IESG       | Section 4.3.1 |
    |                  | dialog          |            | RFC XXXX      |
    +------------------+-----------------+------------+---------------+
    | transfer         | transfer dialog | IESG       | Section 4.3.1 |
    |                  |                 |            | RFC XXXX      |
    +------------------+-----------------+------------+---------------+
    | incomplete       | incomplete      | IESG       | Section 4.3.1 |
    |                  | dialog          |            | RFC XXXX      |
    +------------------+-----------------+------------+---------------+
    | recording-set    | multi-recording | IESG       | Section 4.3.1 |
    |                  | dialog          |            | RFC XXXX      |
    +------------------+-----------------+------------+---------------+

                                  Table 5
```


#### Section 6.3.5. party_history Object Parameter Names Registry

**188.** (§6.3.5 (Table 6)) _[lowercase]_

```
   This initial values for the party_history Object Parameter Names
   Registry are listed in the following table.  Use the template in
   Object Registry Template (Section 6.3.1) when registering additional
   entries to this table.

    +===========+=====================+============+==================+
    | Parameter | Parameter           | Change     | Specification    |
    | Name      | Description         | Controller | Document(s)      |
    +===========+=====================+============+==================+
    | party     | event party index   | IESG       | Section 4.3.13.1 |
    |           |                     |            | RFC XXXX         |
    +-----------+---------------------+------------+------------------+
    | time      | time event occurred | IESG       | Section 4.3.13.1 |
    |           |                     |            | RFC XXXX         |
    +-----------+---------------------+------------+------------------+
    | event     | event type          | IESG       | Section 4.3.13.1 |
    |           |                     |            | RFC XXXX         |
    +-----------+---------------------+------------+------------------+
    | button    | button label        | IESG       | Section 4.3.13.1 |
    |           | character or string |            | RFC XXXX         |
    +-----------+---------------------+------------+------------------+

                                  Table 6
```


##### Section 6.3.5.1. party_event Event Name Registry

**189.** (§6.3.5.1) _[lowercase]_

> This document defines a new registry for the token name values that
> are permitted as values to the party_event Object event
> (Section 4.3.13.1) parameter.


###### Section 6.3.5.1.1. party_event Event Name Registration Template

**190.** (§6.3.5.1.1) _[lowercase]_

```
   party_event Event Name:

   The string token name of a party_event Object event type.  The name
   is case sensitive.  Names may not match other registered names in a
   case-insensitive manner unless the Designated Experts state that
   there is a compelling reason to allow an exception.

   party_event Event Description:

   Brief description of the party_event Object Event

   Change Controller:

   For Standards Track RFCs, list the "IESG".  For others, give the name
   of the responsible party.  Other details (e.g., postal address, email
   address, home page URI) may also be included.

   Specification Document(s):

   Reference to the document or documents that specify the parameter,
   preferably including URIs that can be used to retrieve copies of the
   documents.  An indication of the relevant sections may also be
   included but is not required.
```

Lowercase obligation: *"Names may not match other registered names in a case-insensitive manner unless the Designated Experts state that there is a compelling reason to allow an exception."*


###### Section 6.3.5.1.2. party_event Type Name Registration Initial Values

**191.** (§6.3.5.1.2 (Table 7)) _[lowercase]_

```
   The following table defines the initial values for the Dialog Object
   Types Registry.

   +=============+=====================+============+==================+
   | party_event | party_event Event   | Change     | Specification    |
   | Event Name  | Description         | Controller | Document(s)      |
   +=============+=====================+============+==================+
   | join        | party join event    | IESG       | Section 4.3.13.1 |
   |             |                     |            | RFC XXXX         |
   +-------------+---------------------+------------+------------------+
   | drop        | party drop event    | IESG       | Section 4.3.13.1 |
   |             |                     |            | RFC XXXX         |
   +-------------+---------------------+------------+------------------+
   | hold        | party on hold       | IESG       | Section 4.3.13.1 |
   |             | event               |            | RFC XXXX         |
   +-------------+---------------------+------------+------------------+
   | unhold      | party off hold      | IESG       | Section 4.3.13.1 |
   |             | event               |            | RFC XXXX         |
   +-------------+---------------------+------------+------------------+
   | mute        | party on mute       | IESG       | Section 4.3.13.1 |
   |             | event               |            | RFC XXXX         |
   +-------------+---------------------+------------+------------------+
   | unmute      | party off mute      | IESG       | Section 4.3.13.1 |
   |             | event               |            | RFC XXXX         |
   +-------------+---------------------+------------+------------------+
   | keydown     | DTMF/app key/       | IESG       | Section 4.3.13.1 |
   |             | button press event  |            | RFC XXXX         |
   +-------------+---------------------+------------+------------------+
   | keyup       | DTMF/app key/       | IESG       | Section 4.3.13.1 |
   |             | button release      |            | RFC XXXX         |
   |             | event               |            |                  |
   +-------------+---------------------+------------+------------------+

                                  Table 7
```


#### Section 6.3.6. Attachment Object Parameter Names Registry

**192.** (§6.3.6 (Table 8)) _[lowercase]_

```
   The following defines the initial values for the Attachment Object
   Parameter Names Registry.  Use the template in Object Registry
   Template (Section 6.3.1) when registering additional entries to this
   table.

   +==============+=======================+============+===============+
   | Parameter    | Parameter             | Change     | Specification |
   | Name         | Description           | Controller | Document(s)   |
   +==============+=======================+============+===============+
   | purpose      | attachment object     | IESG       | Section 4.4.1 |
   |              | purpose description   |            | RFC XXXX      |
   +--------------+-----------------------+------------+---------------+
   | start        | attachment start      | IESG       | Section 4.4.2 |
   |              | time                  |            | RFC XXXX      |
   +--------------+-----------------------+------------+---------------+
   | party        | sending party index   | IESG       | Section 4.4.3 |
   |              |                       |            | RFC XXXX      |
   +--------------+-----------------------+------------+---------------+
   | dialog       | associated dialog     | IESG       | Section 4.4.4 |
   |              | index                 |            | RFC XXXX      |
   +--------------+-----------------------+------------+---------------+
   | mediatype    | attachment body       | IESG       | Section 4.4.5 |
   |              | media type            |            | RFC XXXX      |
   +--------------+-----------------------+------------+---------------+
   | filename     | attachment content    | IESG       | Section 4.4.6 |
   |              | filename              |            | RFC XXXX      |
   +--------------+-----------------------+------------+---------------+
   | body         | attachment inline     | IESG       | Section 4.4.7 |
   |              | content               |            | RFC XXXX      |
   +--------------+-----------------------+------------+---------------+
   | encoding     | attachment inline     | IESG       | Section 4.4.7 |
   |              | content encoding      |            | RFC XXXX      |
   +--------------+-----------------------+------------+---------------+
   | url          | attachment            | IESG       | Section 4.4.7 |
   |              | referenced content    |            | RFC XXXX      |
   |              | URL                   |            |               |
   +--------------+-----------------------+------------+---------------+
   | content_hash | attachment content    | IESG       | Section 4.4.7 |
   |              | hash                  |            | RFC XXXX      |
   +--------------+-----------------------+------------+---------------+

                                  Table 8
```


#### Section 6.3.7. Analysis Object Parameter Names Registry

**193.** (§6.3.7 (Table 9)) _[lowercase]_

```
   The following defines the initial values for the Analysis Object
   Parameter Names Registry.  Use the template in Object Registry
   Template (Section 6.3.1) when registering additional entries to this
   table.

   +================+=====================+============+===============+
   | Parameter      | Parameter           | Change     | Specification |
   | Name           | Description         | Controller | Document(s)   |
   +================+=====================+============+===============+
   | type           | analysis type       | IESG       | Section 4.5.1 |
   |                |                     |            | RFC XXXX      |
   +----------------+---------------------+------------+---------------+
   | dialog         | associated dialog   | IESG       | Section 4.5.2 |
   |                | index               |            | RFC XXXX      |
   +----------------+---------------------+------------+---------------+
   | attachment     | associated          | IESG       | Section 4.5.3 |
   |                | attachment index    |            | RFC XXXX      |
   +----------------+---------------------+------------+---------------+
   | mediatype      | analysis body media | IESG       | Section 4.5.4 |
   |                | type                |            | RFC XXXX      |
   +----------------+---------------------+------------+---------------+
   | filename       | analysis content    | IESG       | Section 4.5.5 |
   |                | filename            |            | RFC XXXX      |
   +----------------+---------------------+------------+---------------+
   | vendor         | vendor producing    | IESG       | Section 4.5.6 |
   |                | content             |            | RFC XXXX      |
   +----------------+---------------------+------------+---------------+
   | product        | vendor product      | IESG       | Section 4.5.7 |
   |                | producing content   |            | RFC XXXX      |
   +----------------+---------------------+------------+---------------+
   | schema         | product schema of   | IESG       | Section 4.5.8 |
   |                | content             |            | RFC XXXX      |
   +----------------+---------------------+------------+---------------+
   | body           | analysis inline     | IESG       | Section 4.5.9 |
   |                | content             |            | RFC XXXX      |
   +----------------+---------------------+------------+---------------+
   | encoding       | analysis inline     | IESG       | Section 4.5.9 |
   |                | content encoding    |            | RFC XXXX      |
   +----------------+---------------------+------------+---------------+
   | url            | analysis referenced | IESG       | Section 4.5.9 |
   |                | content URL         |            | RFC XXXX      |
   +----------------+---------------------+------------+---------------+
   | content_hash   | analysis content    | IESG       | Section 4.5.9 |
   |                | hash                |            | RFC XXXX      |
   +----------------+---------------------+------------+---------------+

                                  Table 9
```


#### Section 6.3.8. Redacted Object Parameter Names Registry

**194.** (§6.3.8 (Table 10)) _[lowercase]_

```
   The following defines the initial values for the Redacted Object
   Parameter Names Registry.  Use the template in Object Registry
   Template (Section 6.3.1) when registering additional entries to this
   table.

   +================+===================+============+=================+
   | Parameter      | Parameter         | Change     | Specification   |
   | Name           | Description       | Controller | Document(s)     |
   +================+===================+============+=================+
   | uuid           | less redacted     | IESG       | Section 4.1.8.1 |
   |                | vCon UUID         |            | RFC XXXX        |
   +----------------+-------------------+------------+-----------------+
   | type           | redaction type or | IESG       | Section 4.1.8.1 |
   |                | reason            |            | RFC XXXX        |
   +----------------+-------------------+------------+-----------------+
   | url            | referenced less   | IESG       | Section 4.1.8.1 |
   |                | redacted vCon URL |            | RFC XXXX        |
   +----------------+-------------------+------------+-----------------+
   | content_hash   | less redacted     | IESG       | Section 4.1.8.1 |
   |                | vCon hash         |            | RFC XXXX        |
   +----------------+-------------------+------------+-----------------+

                                  Table 10
```


#### Section 6.3.9. Amended Object Parameter Names Registry

**195.** (§6.3.9 (Table 11)) _[lowercase]_

```
   The following defines the initial values for the Amended Object
   Parameter Names Registry.  Use the template in Object Registry
   Template (Section 6.3.1) when registering additional entries to this
   table.

   +================+==================+============+=================+
   | Parameter Name | Parameter        | Change     | Specification   |
   |                | Description      | Controller | Document(s)     |
   +================+==================+============+=================+
   | uuid           | prior vCon       | IESG       | Section 4.1.9.1 |
   |                | version UUID     |            | RFC XXXX        |
   +----------------+------------------+------------+-----------------+
   | url            | referenced prior | IESG       | Section 4.1.9.1 |
   |                | version vCon URL |            | RFC XXXX        |
   +----------------+------------------+------------+-----------------+
   | content_hash   | prior version    | IESG       | Section 4.1.9.1 |
   |                | vCon hash        |            | RFC XXXX        |
   +----------------+------------------+------------+-----------------+

                                 Table 11
```


### Section 6.4. vCon Extensions Names Registry

**196.** (§6.4) _[lowercase]_

> This document defines and new registry for the token name values that
> are permitted as values to the [extensions]s(#extensions) parameter.
> However it does not define any values for this registry.  Values for
> this registry are to be defined in subsequent documents which define
> extensions to the vCon schema.


#### Section 6.4.1. Extensions Registration Template

**197.** (§6.4.1) _[lowercase]_

```
   Extension Name:

   The string token name of an extension to the vCon JSON schema.  The
   name is case sensitive.  Names may not match other registered names
   in a case-insensitive manner unless the Designated Experts state that
   there is a compelling reason to allow an exception.

   Extension Description:

   Brief description of the the vCon extension

   Change Controller:

   For Standards Track RFCs, list the "IESG".  For others, give the name
   of the responsible party.  Other details (e.g., postal address, email
   address, home page URI) may also be included.

   Specification Document(s):

   Reference to the document or documents that specify the parameter,
   preferably including URIs that can be used to retrieve copies of the
   documents.  An indication of the relevant sections may also be
   included but is not required.
```

Lowercase obligation: *"Names may not match other registered names in a case-insensitive manner unless the Designated Experts state that there is a compelling reason to allow an exception."*


### Section 6.5. JSON Web Signature and Encryption Header Parameters

**198.** (§6.5) _[lowercase]_

> This document registers the following new parameter in the [JWS] JSON
> Web Signature and Encryption Header Parameters registry.

**199.** (§6.5 (uuid header parameter registration)) _[lowercase]_

```
   *  Header Parameter Name: "uuid"

   *  Header Parameter Description: UUID of the signed object

   *  Header Parameter Usage Location(s): JWS, JWE

   *  Change Controller: IESG

   *  Specification Document(s): Header Object (Section 5.2.2), Header
      Object (Section 5.3.1) of RFC XXXX
```


## Section 7. Non-Upward Compatible Changes to the vCon Container

**This is a version-migration log, not a set of examples.** An earlier
extraction of this record mis-cited §7 as "examples"; it is the record of
which renames and type changes break a reader of an older syntax version, and
it is the only place the pre-0.4.0 spellings are written down. §4.1.1 points
here for exactly that reason.

**200.** (§7.1 (0.3.0 to 0.4.0)) _[lowercase]_

```
   *  The "appended" Object was renamed to "amended"

   *  The "must_support" parameter was renamed to "critical" to be
      consistent with other IETF JSON schema extension mechanisms.

   *  The "session_id" Dialog Object parameter was changes from a String
      to a SessionId Object.
```

**201.** (§7.2 (0.0.2 to 0.3.0)) _[lowercase]_

```
   *  "transfer-target" parameter was renamed to "transfer_target" to be
      consistent with other compound names that use the underscore
      ("_").

   *  "target-dialog" parameter was renamed to "target_dialog" to be
      consistent with other compound names that use the underscore
      ("_").
```

**202.** (§7.3 (0.0.1 to 0.0.2)) _[lowercase]_

```
   *  "mimetype" parameters were renamed to "mediatype"

   *  "alg" and "signature" were combined into "content_hash"
```


## Section 8. References and the appendices

**§8 References** (§8.1 normative, §8.2 informative, lines 3844–4045) carries
no BCP 14 keyword. It is not reproduced here; the bracketed citations used
throughout this file — `[JWS]`, `[JWE]`, `[UUID]`, `[SHA-512]`, `[SESSION-ID]`,
`[GEOPRIV]`, `[PIDF-LO]`, `[SIP-XFER]`, `[JMAP]`, `[MIME]`, `[STIR-PASS]`,
`[GZIP]`, `[HTTPS]`, `[SMTP]`, `[DID]`, `[TEL]`, `[SIP]`, `[PASSporT]`,
`[MAILTO]`, `[H-460-27]`, `[IANA-COSE-ALG]`, `[MEDIATYPE]`, `[JSON]`,
`[RFC3339]`, `[VCON]` — resolve there.

The three appendices are out of scope for this file by instruction, and each
is carried by another FX-1 artifact:

- **Appendix A, Example vCons** (lines 4047–6726) — nine worked vCon
  instances in JSON: A.1 two-party call with inline recording, A.2 email
  thread multipart, A.3 email thread text, A.4 two-party call with externally
  referenced recording, A.5 two-party call with analysis, A.6 signed, A.7
  encrypted, A.8 redacted, A.9 amended signed. Carried as fixtures by
  `distilled/examples/`. Carries **no** BCP 14 keyword.
- **Appendix B, vCon JSON Schema** (lines 6727–8353) — the draft's own JSON
  Schema for the container. Carried verbatim by `distilled/schema/`. Carries
  **8** BCP 14 keywords: six inside `description` strings restating §4.3.2,
  §4.3.4, §4.3.8, §4.3.11, §4.5.4 or §4, and two inside its closing
  `$comment`, which says outright: *"SHOULD-level statements are not enforced
  by this schema."* **Appendix B cannot validate most of this document** — but
  that claim rests on the keyword census, not on Table 1: `SHOULD` outnumbers
  `MUST` 97 to 65 document-wide, and a `SHOULD` is not decidable by a binary
  validator.
- **Appendix C, vCon CDDL** (lines 8354–8852) — the draft's own CDDL
  definition. Carried verbatim by `distilled/schema/`. Carries **39** BCP 14
  keywords, every one inside a `;` comment restating §2–§5; CDDL expresses
  none of those keywords as a constraint.

**What the appendices do and do not express of Table 1.** Table 1 has **120**
cells — 24 parameters × 5 dialog types — distributed `X` 57, `O` 30, `S` 19,
`M` 9, `SN` 4, `-` 1. Both appendices express the **M** and **X** cells.
Appendix B carries 13 `"const"` discriminators and 43 `if`/`then`/`allOf`/`not`
constructs: every `X` cell is written as `if type=const then
not{anyOf[{required:[p]}]}`, and 7 of the 9 `M` cells as `if type=const then
required:[p]` — 64 cells in all. The two `M` cells it omits are `mediatype`'s,
which footnote (1) makes conditional on whether the content is inline.
Appendix C does the same structurally, discriminating on a literal `type:` in
each branch of a CDDL choice group, with mandatory parameters unmarked and
prohibited ones simply absent from the branch. **Neither expresses `S`, `SN`
or `-`** — 24 of the 120 cells. The reason is the useful part: `M` and `X` are
presence predicates over a single instance, which both languages have, whereas
`S` and `SN` are obligations on an author with conforming instances on both
sides of them, which no binary validator can decide. Appendix C shows the
collapse plainly — `start`, an `S` cell, becomes `? start: date_type`, the
same marking an `O` cell gets, with the obligation demoted to a comment:
*"start SHOULD be present; MAY be omitted if not known"*. That is where the
expressive ceiling of schema languages sits, and it is why §4.3.1.6 is
reproduced in full above.

Appendix B and Appendix C are **restatements, not additional requirements**:
every keyword in them echoes a body statement already captured above. They
are the reason the whole-document census is 216 while the body census is 169.


## Coverage

**Sections covered: §1, §2, §3, §4, §5, §6, §7 — complete.** Every subsection
listed in the draft's table of contents between §1 and §7.3 inclusive has at
least one entry above, and every BCP 14 keyword occurrence in those sections
falls inside a quoted or fenced block.

**Not covered, by instruction:** §8 References (0 keywords) and Appendices A,
B and C, noted one line each in the section above.

### Keyword count by section — this file against the source

| section | source (`bin/bcp14-count`) | captured here | delta |
|---|---|---|---|
| §1 | 0 | 0 | 0 |
| §2 | 20 | 20 | 0 |
| §3 | 0 | 0 | 0 |
| §4 | 121 | 121 | 0 |
| §5 | 27 | 27 | 0 |
| §6 | 1 | 1 | 0 |
| §7 | 0 | 0 | 0 |
| **§1–§7 total** | **169** | **169** | **0** |
| §8 References | 0 | not covered | — |
| Appendix A | 0 | not covered | — |
| Appendix B | 8 | not covered (`distilled/schema/`) | — |
| Appendix C | 39 | not covered (`distilled/schema/`) | — |
| **whole document** | **216** | **169** | **-47** |

**Reconciliation against the 216 baseline.** The body (§1–§7) carries
**169** of the 216. This file captures **169** — an exact match. The
**47** not captured are Appendix B's 8 and Appendix C's 39, every one of them
inside a JSON Schema `description` string or a CDDL comment that restates a
body statement already quoted above. No body keyword is unaccounted for.

By keyword, across the §1–§7 entries above:

| section | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY | total |
|---|---|---|---|---|---|---|
| §2 | 14 | 2 | 1 | 0 | 3 | 20 |
| §4 | 32 | 13 | 49 | 6 | 21 | 121 |
| §5 | 10 | 0 | 17 | 0 | 0 | 27 |
| §6 | 0 | 0 | 1 | 0 | 0 | 1 |
| **§1–§7** | **56** | **15** | **68** | **6** | **24** | **169** |

§1, §3 and §7 contribute 0 and are omitted from the keyword table.

### Unresolved — source defects and internal contradictions

Recorded, not corrected. Every quote above reproduces the source as written,
including each of these.

1. **§4.1.8.1 `uuid` is mandatory and optional at once.** The Redacted
   Object's type declaration is bare — `*  uuid: "String"` — and §2.2 says
   *"All parameters are assumed to be mandatory unless otherwise noted."*
   Yet the next sentence gives a defined meaning to its absence: *"The absence
   of a value for uuid indicates that the less redacted version of this vCon
   is not available or does not exist."* §4.1.9.1 avoids this for the Amended
   Object by writing `(optional if external reference provided)`. A validator
   cannot satisfy both readings of §4.1.8.1.

2. **§4.3.2 `start` is mandatory and `SHOULD` at once.** The Dialog Object's
   type declaration is bare — `*  start: "Date"` — and §2.2 says *"All
   parameters are assumed to be mandatory unless otherwise noted."* Yet the
   same subsection says *"The start parameter SHOULD be present unless it is
   not known."* and *"The start parameter is optional for the "transfer" type
   Dialog Object as it may not always be known."*, and Table 1 gives `start`
   as `S` for four types and `O` for `transfer` — none of which is mandatory.
   §4.3.3 avoids this for `duration` by writing `(optional)` on the
   declaration line itself. A validator cannot satisfy both readings of
   §4.3.2. This is item 1's defect class, in a second place.

3. **§6.3.2 Table 2 mis-cites `amended`.** The `amended` row gives
   `Section 4.1.8` as its specification document; `amended` is defined in
   §4.1.9. §4.1.8 is `redacted`, which has its own row citing the same
   section.

4. **§6.3.3 Table 3 mis-cites `sip`.** The `sip` row gives `Section 4.2.1`;
   `sip` is defined in §4.2.2. §4.2.1 is `tel`, which has its own row citing
   the same section.

5. **§6.5 mis-cites the encrypted-form Header Object.** It registers the
   `uuid` header parameter against *"Header Object (Section 5.2.2), Header
   Object (Section 5.3.1)"*. §5.3.1 is the **Unprotected** Object; the
   encrypted form's Header Object is §5.3.3. The Unprotected Object is in
   fact where the encrypted form's `uuid` lives, so the section number is
   right and the name is wrong — or the reverse — but the two do not agree.

6. **§6.3.5.1.2 is titled for the wrong registry.** Its body reads *"The
   following table defines the initial values for the Dialog Object Types
   Registry"* — copied from §6.3.4.1.2 — above Table 7, which is the
   `party_event` event name registry.

7. **§6.4 contains an unrendered Markdown link.** *"the token name values
   that are permitted as values to the [extensions]s(#extensions)
   parameter"* — a conversion artifact left in the published text.

8. **§4.1.1 deprecates `vcon` and then requires its value.** *"The "vcon"
   parameter is DEPRECATED"* and, four lines later, *"For syntax defined in
   this document, the string MUST have the value: "0.4.0""*. No statement
   says whether the parameter may be omitted, and §2.2's default makes it
   mandatory. Deprecated-but-mandatory-with-a-fixed-value is not a state the
   document anywhere resolves.

9. **§4.3.7's annotation and Table 1 disagree in strength.** The type
   declaration reads `recording_set: "UnsignedInt" (optional; SHOULD be
   present when the recording is part of a recording-set)` and the prose
   repeats the `SHOULD`; Table 1 marks `recording_set` as plain `O` for the
   `recording` column, which the legend defines as *"The parameter is
   optional"*. §4.3.1.6 states that the subsections are definitive, so the
   `SHOULD` governs — but the table under-reports it.

10. **`SHOULD` outnumbers `MUST` 97 to 65 across the whole document, and 49
   to 32 in §4 alone.** Most of the container's structure — `parties` on a
   recording, `start`, Dialog Content, the Attachment and Analysis bodies,
   the `transfer` role parameters — is `SHOULD`. Conformance to this draft
   therefore constrains a producer far less than the parameter tables
   suggest, and an interoperable profile would have to raise many of these.
   Not a defect; a property of the document that any implementation plan has
   to price in.

11. **Spelling and grammar errors inside normative sentences, reproduced as
    written.** §4.2.9 *"The the civicaddress parameter"*; §4.1.8.1 *"The the
    location of the referenced vCon"*; §4.2.5 *"A Party Object SHOULD be
    create for each anonymous party"*; §4.3.11 *"as there in not always a
    call involved"*; §4.3.14 *"analysis to be captures in the analysis
    section of the Vcon"*; §7.1 *"was changes from a String to a SessionId
    Object"*; §4.5.8 *"the schema value is provide to differentiate"*;
    §5.3 *"the the Authentication Tag"*. None changes a normative verb, but
    they are reproduced rather than silently corrected.
