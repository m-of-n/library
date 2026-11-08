---
record: w3c-vc-jose-cose
kind: normative
title: "w3c-vc-jose-cose — normative statements"
extracted: "2026-11-03"
reviewed_by: ""
---

<!-- FX-1 pass 1 (extract; normative agent; 2026-11-03). Every normative
     statement and normative block of the W3C Recommendation
     `Securing Verifiable Credentials using JOSE and COSE` (title block),
     VERBATIM, with its locator and source line range, in source order.
     Statements that sit in sections the source declares non-normative are
     reproduced and flagged, never dropped. Inside blockquotes and fences:
     source text only. Outside them: structure added by this extraction
     (headings, entry numbers, locators, line ranges, flags, link targets and
     notes). -->

Source: W3C Recommendation
`Securing Verifiable Credentials using JOSE and COSE` (title block), 15 May
2025 (REC-vc-jose-cose-20250515), editors Michael Jones, Michael Prorock and
Gabe Cohen, Verifiable Credentials Working Group;
https://www.w3.org/TR/2025/REC-vc-jose-cose-20250515/. Authoritative bytes:
the Recommendation's HTML, 382270 bytes, sha256
6c70cf8d7de9d8a3ff28a743fea9d569a67a402111c3245fdafbaa2ad6709af9 — equal to
content.sha256 in record.yaml (retrieved 2026-10-23) and recomputed from
.cache/w3c-vc-jose-cose.bin in this pass. Every quotation is taken from, and
line-numbered against, its plain-text rendering .cache/w3c-vc-jose-cose.txt:
1980 lines, 172097 bytes, sha256
f02bd4966800863d533746c6c39ad267ada1b8bfcbb92186c204b617bb46c126, produced by
bin/render-w3c (then a scratch render_w3c.py) and reproduced byte-identically by re-running it on
the HTML in this pass. Neither file is committed.

## How to read this file

**The .txt rendering.** The source is an HTML page. Its rendering keeps one
line per HTML block element (paragraph, list item, definition term,
definition, table row), collapses whitespace as a browser displays it (so a
double space in the HTML source, as in §5.2 step 2.3, reads as one; all 1043
no-break spaces of the HTML lie inside examples, so none reaches a reproduced
line), keeps pre-formatted example content byte for byte, and prints numbered
headings at column 0 in RFC style so that bin/check-locators can read them. A
paragraph of the source is therefore one line of the .txt. Two things the HTML
shows are not text and are not in the .txt: the numbers and bullets of lists,
which the browser generates, and link targets. The renderer marks each table
cell with a vertical bar. Its known artefact, a space inserted where two
inline spans meet, affects example strings only: no line reproduced here has a
space before a comma, full stop, semicolon, colon or closing bracket, or after
an opening one, which is the artefact's signature (checked by script; see
Coverage).

**Verbatim containers.** Two are used:

- A **blockquote** (a line opening with a greater-than sign and a space)
  reproduces one paragraph of the source: the text after the marker and its
  space is the .txt line, byte for byte — spelling, punctuation and the
  source's own errors included.
- A **fenced block** reproduces a contiguous run of .txt lines, every line of
  the run, in order: a paragraph (in §A, two) together with the list,
  definition list or table it introduces; or a list alone (§1.1.2.2 ¶2). Each
  line of a fence is one .txt line, preceded by a structure prefix that this
  extraction adds and that is not source text: a list item opens with the marker a browser would display (a
  hyphen and a space for an unordered item; for an ordered item its
  position, 1. or 2.1. and so on, where 2.1. is the first item of the list
  nested in item 2 — the browser shows plain numbers at each level); each
  nesting level, each definition (under its term) and each paragraph or list
  inside a table cell (under its row) is indented four spaces. Removing the
  prefix gives the .txt line byte for byte. The vertical bars of the §6 tables
  are the .txt's own.

Everything outside a container is structure added here. In notes, a span in
backticks is a verbatim fragment of the .txt, attributed to the section or
sections the note names (or, under an entry, to that entry's section); nothing
else is set in backticks, and no other quotation marks are used to quote. No
two non-adjacent passages are spliced into one entry: each entry is a single
contiguous run of source lines, given in its header as line n or lines a–b
(1-based, over the .txt split on newline characters).

**Ids.** N-001 to N-145 were assigned in source order. N-200 (§8.5 ¶5) and
N-201 (§B ¶1) were added later in pass 1, when its checks were run, and no id
was renumbered: they stand in source order, N-200 between N-143 and N-144 and
N-201 after N-145. Ids are unique, not consecutive.

**Locators.** § plus the section number as the .txt prints it (§3.1.1; the
appendices are §A, §B, §C, §C.1 and §C.2), then a position inside that
section:

- ¶n — the nth **block** of the section's own body, counting the child
  elements of the section in the HTML that render at least one line besides
  the heading: each paragraph, each list (ul, ol, dl, with all its items),
  each table and each example is one block. A parent section's count stops at its first
  subsection. An empty paragraph renders nothing and is not counted (the HTML has
  three, one each in §3.1.2, §3.2.2 and §3.3.2, after ¶7). requirements.yaml counts
  differently, paragraphs only, so its paragraph numbers differ from these
  wherever a list or an example comes earlier in the section: its §3.1.2
  paragraph 11 (R-0025) is ¶13 here (N-044). design-notes.md and protocol.yaml
  use this file's count.
- ¶m–¶n — an entry that reproduces blocks m to n inclusive, a contiguous run:
  used where an introducing paragraph and its list or table are kept together.
- step n, step n.m — an item of the ordered list of §5.1, §5.2 or §5.3,
  numbered as in its fence; item n — the nth item of any other list.

**Flags.** Each entry header may carry:

- _[scope]_ — the entry says what is normative: §1.1 ¶1, and the paragraph
  `This section is non-normative.` that opens each of §3.1.3, §6, §7, §8, §A
  and §B.
- _[boilerplate]_ — the BCP 14 conventions paragraph (N-003), which
  bin/bcp14-count strips.
- _[mention]_ — the capitalised keyword is quoted, not used (§1.1.1 ¶1, ¶4,
  ¶7: `"MUST"` statements). Counted by bin/bcp14-count, so carried.
- _[implied]_ — no capitalised keyword and nothing that sets _[lowercase]_,
  _[permissive]_ or _[advisory]_; included because it binds or scopes the
  rest: a definition, a conformance class, an algorithm input, output or
  step, a structure or property of a secured form, a precondition, or a
  pointer to where a requirement is specified.
- _[lowercase]_ — carries a lowercase must, may or optional (the only
  lowercase BCP 14 words the source uses) that states an obligation,
  permission or optionality of the thing specified, so it reads as normative
  though RFC 8174 makes only capitals keywords. Flagged whether or not the
  entry also carries a capitalised keyword.
- _[permissive]_ — carries a lowercase can that grants a use
  (`a verifier can use this parameter`, §4.1.1 ¶1) or states the values a
  field takes (`can be either a string or an object`, §4.1.2 ¶2), so it reads
  as a MAY though BCP 14 does not define can. Flagged whether or not the entry
  also carries a capitalised keyword. A can that only describes — a
  definition's capability, a benefit, an illustrative list — does not set it.
- _[advisory]_ — an obligation or advice phrased in words BCP 14 does not
  define: are advised to, are to be interpreted, needs to, it is essential, it
  is crucial, it is vital, it is important, it is considered best practice, or
  an imperative verb outside an algorithm (Follow, take special care,
  conduct, Remember). Flagged whether or not the entry also carries a
  capitalised keyword (N-086 carries a MAY); the conventions paragraph
  (N-003) does not set it.
- _[algorithm]_ — an ordered-list procedure of §5.1 to §5.3, reproduced whole
  with its steps numbered.
- _[table]_ — the entry is or contains a table of the source.
- _[IANA]_ — a media-type registration template of §6.1.1 to §6.1.6.
- _[changelog]_ — Appendix A, which reports changes since the First Candidate
  Recommendation.
- _[non-normative]_ — the entry lies in a section the source declares
  non-normative (§3.1.3, §6 with §6.1 to §6.1.6, §7 with §7.1 to §7.3, §8 with
  §8.1 to §8.5, §A, §B). Under §1.1 ¶1 its statements are not requirements of
  this document; they are reproduced so that every keyword reconciles and
  every normative-sounding sentence is visible with its status.

**Links.** After an entry, _Links:_ gives the HTML target of each link in the
entry's lines, with the link text in backticks; an internal target is given
with the section it resolves to. Omitted are citations of the bibliography,
section references by number, permalinks, links whose text is their own URL
or mail address (§6), and links to a term definition — this document's own or
one in the data model or DID Core (targets #dfn-…) — together with the data
model's links from the words verifiable credentials and verifiable
presentations to its sections on them. The data model's definitions of the
Enveloped Verifiable Credential and Enveloped Verifiable Presentation types
(targets #defn-…) are given. Checked by script; see Coverage.

**BCP 14 census: 97.** bin/bcp14-count .cache/w3c-vc-jose-cose.txt
--by-keyword returns 97 — MUST 48, SHOULD 25, MAY 11, RECOMMENDED 6, NOT
RECOMMENDED 4, MUST NOT 2, SHOULD NOT 1; no SHALL, SHALL NOT, REQUIRED or
OPTIONAL — after it strips the conventions paragraph (§1.1 ¶2, N-003), whose
seven keywords it does not count. The same counter over the HTML returns 97
with the same split, and the HTML holds 104 elements of class rfc2119: these
97 and the seven of the conventions paragraph. The counter (bin/_bcp14.py)
matches capitals only, longest match first, with a non-letter on each side; no
keyword of this source is split across a line. All 97 lie inside the entries
below; the reconciliation, occurrence by occurrence, is under Coverage. Of the
97: 3 are mentions (N-004, N-007, N-010); 7 sit in non-normative sections — 6
in §3.1.3 (N-049, N-050, N-052 ×2, N-053, N-054) and 1 in §A (N-145); the
other 87 are keywords of normative sections.

**Lowercase, permissive and advisory accounting.** Over the whole .txt,
case-sensitively, the whole words must, should, may, shall, required,
recommended and optional occur 19 times: optional 8, may 8, must 3, and the
other 4 never. 18 lie inside entries; the 1 outside is line 43
(`must disclose`, in the front matter's Status of This Document, on the W3C
Patent Policy). Of the 18, 16 set _[lowercase]_ in 14 entries and 2 do not:
line 1110 `it may be impossible` (§7.2 ¶6, N-139, epistemic) and line 1855
`may be selectively disclosed` (§A ¶4 item 5, N-145, a changelog report). The
whole word can occurs 21 times: 20 inside entries, of which 15 set
_[permissive]_ in 11 entries and 5 only describe (§2 ¶2 twice, §3 ¶3, and the
illustrative lists of §3.2.1 ¶5 and §3.2.2 ¶8), and 1 outside, line 38 in the
Status of This Document. The other modals BCP 14 does not define — could 3,
might 3, will 13, would 1 — occur only inside entries, where they describe or
predict and set no flag; needs occurs twice and sets _[advisory]_ (N-091,
N-129). The advisory entries are listed under Coverage.

**Source text kept as printed.** Nothing inside a container is corrected. The
defects and tensions found while extracting are listed, with their entries,
under Source defects and tensions (SD-1 to SD-34); an entry affected by one
points to it.

**Not reproduced.** The front matter; §1 ¶2–¶4; §4 ¶2; every example (26,
named under each section with its title and lines) and the nine pointer
paragraphs that follow the examples of §3; §B ¶2; Appendix C; and the page's
back-to-top arrow and term-reference panels. Each omission is named in an
italic note under its section heading, so that every omission is a recorded
decision rather than a drop. No capitalised keyword occurs in any block not
reproduced.

## Front matter

_No entries — title block, Abstract, Status of This Document and Table of
Contents (lines 1–100). The Status section's lowercase `must` (line 43) and
`mandatory` (line 39) bind W3C process and patent-policy participants, not
implementations. The title block records `Errata exists.` (line 25): this file
reproduces the Recommendation as published and applies no erratum (SD-31)._



## §1 Introduction

_Not reproduced: ¶2–¶4 (lines 105–107), which describe JWS, SD-JWT and COSE
and what each provides. They state no requirement, definition or rule of this
specification. §1 is not declared non-normative, so under §1.1 ¶1 (N-002) its
text is formally normative; ¶1 is reproduced because it fixes the scope and
the role of content types._

**N-001.** (§1 ¶1) _[implied]_ — line 104

> This specification defines how to secure media types expressing Verifiable Credentials and Verifiable Presentations as described in [VC-DATA-MODEL-2.0] using approaches defined by the JOSE, OAuth, and COSE working groups at the IETF. This includes JSON Web Signature (JWS) [RFC7515], Selective Disclosure for JWTs [SD-JWT], and CBOR Object Signing and Encryption (COSE) [RFC9052]. It uses content types [RFC6838] to distinguish between the data types of unsecured documents conforming to [VC-DATA-MODEL-2.0] and the data types of secured documents conforming to [VC-DATA-MODEL-2.0].

### §1.1 Conformance

_Every block is reproduced._

**N-002.** (§1.1 ¶1) _[scope]_ — line 111

> As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

_Applied throughout this file. Six sections open with
`This section is non-normative.`: §3.1.3, §6, §7, §8, §A and §B; their
subsections inherit the status. The source has no element of class note; its
26 examples are named under their sections rather than reproduced._

**N-003.** (§1.1 ¶2) _[boilerplate]_ — line 112

> The key words MAY, MUST, MUST NOT, NOT RECOMMENDED, RECOMMENDED, SHOULD, and SHOULD NOT in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

_bin/bcp14-count strips this paragraph and counts 0 in it. It names seven
keywords; REQUIRED, SHALL, SHALL NOT and OPTIONAL are not among them, and none
of those four occurs in capitals anywhere in the source._

_Links:_ `BCP 14` → https://www.rfc-editor.org/info/bcp14.

### §1.1.1 Conformance Classes

_Every block is reproduced. Each paragraph defines one conformance class; in
the HTML each class name is a defining term (dfn)._

**N-004.** (§1.1.1 ¶1) _[mention]_ — line 116

> A conforming JWS document is one that conforms to all of the "MUST" statements in Section 3.1 With JOSE.

_The quoted `"MUST"` is a mention, not a use: the sentence defines a
conformance class by reference to the MUST statements of §3.1. It is counted
by bin/bcp14-count and so carried in the census._

**N-005.** (§1.1.1 ¶2) — line 117

> A conforming JWS issuer implementation produces conforming JWS documents and MUST secure them as described in Section 3.1 With JOSE.

**N-006.** (§1.1.1 ¶3) _[implied]_ — line 118

> A conforming JWS verifier implementation verifies conforming JWS documents as described in Section 3.1 With JOSE.

**N-007.** (§1.1.1 ¶4) _[mention]_ — line 119

> A conforming SD-JWT document is one that conforms to all of the "MUST" statements in Section 3.2 With SD-JWT.

_Mention of `"MUST"`, as in §1.1.1 ¶1 (N-004); the class is defined by the
MUST statements of §3.2._

**N-008.** (§1.1.1 ¶5) — line 120

> A conforming SD-JWT issuer implementation produces conforming SD-JWT documents and MUST secure them as described in Section 3.2 With SD-JWT.

**N-009.** (§1.1.1 ¶6) _[implied]_ — line 121

> A conforming SD-JWT verifier implementation verifies conforming SD-JWT documents as described in Section 3.2 With SD-JWT.

_Contrast §3.2.1 ¶4 and §3.2.2 ¶4 (N-058, N-064): see SD-1._

**N-010.** (§1.1.1 ¶7) _[mention]_ — line 122

> A conforming COSE document is one that conforms to all of the "MUST" statements in Section 3.3 With COSE.

_Mention of `"MUST"`, as in §1.1.1 ¶1 (N-004); the class is defined by the
MUST statements of §3.3._

**N-011.** (§1.1.1 ¶8) — line 123

> A conforming COSE issuer implementation produces conforming COSE documents and MUST secure them as described in Section 3.3 With COSE.

**N-012.** (§1.1.1 ¶9) _[implied]_ — line 124

> A conforming COSE verifier implementation verifies conforming COSE documents as described in Section 3.3 With COSE.

### §1.1.2 Securing Verifiable Credentials

_Every block is reproduced._

**N-013.** (§1.1.2 ¶1) _[implied]_ — line 128

> The Verifiable Credentials Data Model v2.0 describes the approach taken by this specification to secure JSON and CBOR claims by applying an enveloping proof.

_Links:_ `Verifiable Credentials Data Model v2.0` →
https://www.w3.org/TR/vc-data-model-2.0/#securing-mechanism-specifications.

**N-014.** (§1.1.2 ¶2–¶3) _[lowercase]_ — lines 129–135

```
This specification defines how to secure different data structures using various enveloping proof mechanisms:
JSON Web Token (JWT):
    A JWT secures a JWT Claims Set, in its entirety. A JWT Claims Set is a JSON object containing one or more claims about an entity (typically the subject of the JWT). If any part of the JWT Claims Set is to be revealed, all claims in that set must be revealed; there is no option to reveal (or conceal) some of the claims while concealing (or revealing) the others.
Selective Disclosure JSON Web Token (SD-JWT):
    An SD-JWT secures a JWT Claims Set, similar to a JWT securing a JWT Claims Set, but with the added capabilities of selectively revealing or withholding parts of the JWT Claims Set. A JWT Claims Set is one or more claims about an entity (typically the subject of the SD-JWT).
CBOR Object Signing and Encryption (COSE):
    COSE secures CBOR (Concise Binary Object Representation) data structures. CBOR is a binary data format that is more compact than JSON and is designed for constrained environments.
```

_A definition list (three terms). The lowercase
`all claims in that set must be revealed` states a property of a JWT, which
reveals its claims all or none; it reads as a rule. Two definitions of
`JWT Claims Set` stand in the one list: see SD-28._

**N-015.** (§1.1.2 ¶4–¶5) _[implied]_ — lines 136–139

```
In the context of Verifiable Credentials:
- When using JWTs, the Verifiable Credential or Presentation is encoded as a JWT Claims Set.
- When using SD-JWTs, the Verifiable Credential or Presentation is encoded as a JWT Claims Set with Selective Disclosure features.
- When using COSE, the Verifiable Credential or Presentation is encoded as a CBOR data structure.
```

**N-016.** (§1.1.2 ¶6) _[implied]_ — line 140

> In all cases, the underlying data model of the Verifiable Credential or Presentation remains consistent with the [VC-DATA-MODEL-2.0], but the encoding and security mechanisms differ.

**N-017.** (§1.1.2 ¶7) _[implied]_ — line 141

> The normative statements in Securing Mechanisms apply to securing application/vc+jwt and application/vp+jwt, application/vc+sd-jwt and application/vp+sd-jwt, application/vc+cose and application/vp+cose.

_Links:_ `Securing Mechanisms` →
https://www.w3.org/TR/vc-data-model-2.0/#securing-mechanisms.

### §1.1.2.1 JWT Format and Requirements

_Every block is reproduced._

**N-018.** (§1.1.2.1 ¶1) _[advisory]_ — line 145

> JSON Web Token implementers are advised to review Implementation Requirements.

_Links:_ `Implementation Requirements` →
https://www.rfc-editor.org/rfc/rfc7519#section-8.

**N-019.** (§1.1.2.1 ¶2) — line 146

> Issuers, Holders, and Verifiers of JWTs MUST understand the effect of the JSON Web Token header parameter setting of "alg": "none" when using JSON Web Tokens to secure [VC-DATA-MODEL-2.0]. When content types from the [VC-DATA-MODEL-2.0] are secured using JSON Web Tokens, the header parameter setting of "alg": "none" is used to communicate that a Verifiable Credential or Verifiable Presentation encoded as a JWT Claims Set has no integrity protection.

**N-020.** (§1.1.2.1 ¶3) — line 147

> Issuers, Holders, and Verifiers MUST ignore all JWT Claims Sets that have no integrity protection.

**N-021.** (§1.1.2.1 ¶4) — line 148

> The JWT Claim Names vc and vp MUST NOT be present in any JWT Claims Set that comprises a verifiable credential or a verifiable presentation.

_Restated, without the qualifier, in non-normative §3.1.3 ¶9 (N-053)._

### §1.1.2.2 SD-JWT Format and Requirements

_Every block is reproduced._

**N-022.** (§1.1.2.2 ¶1) — line 152

> This specification uses Selective Disclosure for JWTs (SD-JWT) as defined in the IETF draft [SD-JWT]. Implementers SHOULD refer to this draft for the full details of the SD-JWT format and processing requirements.

_The [SD-JWT] reference is an unversioned Internet-Draft: see SD-30._

**N-023.** (§1.1.2.2 ¶2) _[lowercase]_ — lines 153–156

```
- An SD-JWT consists of three main parts: the SD-JWT itself, optional disclosures, and an optional KB-JWT (Key Binding JWT). These parts are separated by tilde (~) characters.
- If the KB-JWT is not present, the SD-JWT must end with a tilde (~) character. This is crucial for correct parsing and processing of the SD-JWT.
- Selective disclosure is achieved through the use of disclosure objects. These are base64url-encoded JSON arrays containing the digest of the disclosed claim, the claim name, and the claim value.
- Each disclosable claim is combined with a salt value before hashing to prevent dictionary attacks.
```

_Lowercase `optional disclosures, and an optional KB-JWT` (structure) and
`the SD-JWT must end with a tilde (~) character` (format rule). Item 3 says
the disclosure arrays contain `the digest of the disclosed claim`; the
source's own Example 4 contradicts it: see SD-5._



## §2 Terminology

_Every block is reproduced._

**N-024.** (§2 ¶1–¶2) _[implied]_ — lines 160–168

```
This section defines the terms used in this specification. A link to these terms is included whenever they appear in this specification.
public key
    Cryptographic material that can be used to verify digital proofs created with a corresponding private key.
private key
    Cryptographic material that can be used to generate digital proofs.
verifiable credential
    A standard data model and representation format for expressing cryptographically-verifiable digital credentials, as defined by the W3C Verifiable Credentials specification [VC-DATA-MODEL-2.0].
controlled identifier document
    A document that contains public cryptographic material as defined in the Controlled Identifiers v1.0 specification.
```

_A definition list (four terms). In the HTML each term is a defining term
(dfn). Three are linked from the text; no link leads to `public key`, whose
reference panel reads `Not referenced in this document.` (line 1964), though
¶1 says
`A link to these terms is included whenever they appear in this specification.`
and the term appears, unlinked, in §4.2 ¶3 (N-102)._

_Links:_ `Controlled Identifiers v1.0` → https://www.w3.org/TR/cid-1.0/.



## §3 Securing the VC Data Model

_Every block is reproduced._

**N-025.** (§3 ¶1) _[implied]_ — line 172

> This section outlines how to secure documents conforming to [VC-DATA-MODEL-2.0] using JOSE, SD-JWT, and COSE.

**N-026.** (§3 ¶2) _[implied]_ — line 173

> Documents conforming to [VC-DATA-MODEL-2.0], and their associated media types, rely on JSON-LD, which is an extensible format for describing linked data; see JSON-LD Relationship to RDF.

_Links:_ `JSON-LD Relationship to RDF` →
https://www.w3.org/TR/json-ld11/#relationship-to-rdf.

**N-027.** (§3 ¶3) _[implied]_ — line 174

> A benefit to this approach is that payloads can be made to conform directly to [VC-DATA-MODEL-2.0] without any mappings or transformation, while at the same time supporting registered header parameters and claims that are understood in the context of JOSE, SD-JWT, and COSE.

**N-028.** (§3 ¶4) — line 175

> It is RECOMMENDED that media types be used to distinguish verifiable credentials and verifiable presentations from other kinds of secured JSON or CBOR.

**N-029.** (§3 ¶5) — line 176

> The most specific media type (or subtype) available SHOULD be used, instead of more generic media types (or supertypes). For example, rather than the general application/sd-jwt, application/vc+sd-jwt SHOULD be used, unless there is a more specific media type that would even better identify the secured envelope format.

**N-030.** (§3 ¶6) — line 177

> If implementations do not know which media type to use, media types defined in this specification MUST be used.

_The media types this MUST points at are registered in non-normative §6: see
SD-16._

### §3.1 With JOSE

_No blocks of its own: the heading is followed directly by §3.1.1._

### §3.1.1 Securing JSON-LD Verifiable Credentials with JOSE

_Not reproduced: ¶6,
`Example 1: A simple example of a verifiable credential secured with JOSE`
(lines 188–266), and ¶7, its pointer (line 267). Examples are non-normative
(§1.1 ¶1) and are the examples artifact's material; each of the nine
examples of §3 is followed by a pointer paragraph that reads, every time,
`See Verifiable Credentials Data Model v2.0 for more details regarding this example.`_

**N-031.** (§3.1.1 ¶1) _[implied]_ — line 183

> This section details how to use JOSE to secure verifiable credentials conforming to [VC-DATA-MODEL-2.0].

_Byte-identical to §3.2.1 ¶1 (N-055)._

**N-032.** (§3.1.1 ¶2) — line 184

> A conforming JWS issuer implementation MUST use [RFC7515] to secure this media type. The unsecured verifiable credential is the unencoded JWS payload.

_`this media type` has no antecedent in the section: see SD-27._

**N-033.** (§3.1.1 ¶3) _[lowercase]_ _[permissive]_ — line 185

> The typ header parameter SHOULD be vc+jwt. When present, the cty header parameter SHOULD be vc. The cty header parameter value can be used to differentiate between secured content of different types when using vc+jwt. The content type header parameter is optional, and can be used to express a more specific media type than application/vc when one is available. See Registered Header Parameter Names for additional details regarding usage of typ and cty.

_Lowercase `is optional`; permissive `can be used`, twice. The parameter it
calls `content type` is set in code font in the HTML, but JOSE has no header parameter of that name: see SD-13._

_Links:_ `Registered Header Parameter Names` →
https://www.rfc-editor.org/rfc/rfc7515#section-4.1.

**N-034.** (§3.1.1 ¶4) — line 186

> A conforming JWS verifier implementation MUST use [RFC7515] to verify conforming JWS documents that use this media type.

_Byte-identical to §3.1.2 ¶4 (N-039)._

**N-035.** (§3.1.1 ¶5) — line 187

> To encrypt a secured verifiable credential when transmitting over an insecure channel, implementers MAY use JSON Web Encryption (JWE) [RFC7516] by nesting the secured verifiable credential as the plaintext payload of a JWE, per the description of Nested JWTs in [RFC7519].

### §3.1.2 Securing JSON-LD Verifiable Presentations with JOSE

_Not reproduced: ¶9,
`Example 2: A simple example of a verifiable presentation secured with JOSE with the EnvelopedVerifiableCredential type`
(lines 279–321); ¶10, its pointer (line 322); ¶11,
`Example 3: A simple example of a verifiable presentation secured with JOSE with the EnvelopedVerifiablePresentation type`
(lines 323–355); ¶12, its pointer (line 356). The HTML holds an empty
paragraph between ¶7 and ¶8; it renders no line and is not counted._

**N-036.** (§3.1.2 ¶1) _[implied]_ — line 271

> This section details how to use JOSE to secure verifiable presentations conforming to [VC-DATA-MODEL-2.0].

**N-037.** (§3.1.2 ¶2) — line 272

> A conforming JWS issuer implementation MUST use [RFC7515] to secure this media type. The unsecured verifiable presentation is the unencoded JWS payload.

**N-038.** (§3.1.2 ¶3) _[lowercase]_ _[permissive]_ — line 273

> The typ header parameter SHOULD be vp+jwt. When present, the cty header parameter SHOULD be vp. The cty header parameter value can be used to differentiate between secured content of different types when using vp+jwt. The content type header parameter is optional, and can be used to express a more specific media type than application/vc when one is available. See Registered Header Parameter Names for additional details regarding usage of typ and cty.

_Lowercase `is optional`; permissive `can be used`, twice; `content type` as
in §3.1.1 ¶3 (N-033; SD-13). In this presentation section the sentence reads
`than application/vc when one is available`: see SD-2._

_Links:_ `Registered Header Parameter Names` →
https://www.rfc-editor.org/rfc/rfc7515#section-4.1.

**N-039.** (§3.1.2 ¶4) — line 274

> A conforming JWS verifier implementation MUST use [RFC7515] to verify conforming JWS documents that use this media type.

_Byte-identical to §3.1.1 ¶4 (N-034)._

**N-040.** (§3.1.2 ¶5) — line 275

> Verifiable Credentials secured in verifiable presentations MUST use the Enveloped Verifiable Credential type defined by the [VC-DATA-MODEL-2.0].

_Byte-identical to §3.2.2 ¶5 (N-065) and §3.3.2 ¶5 (N-082)._

_Links:_ `Enveloped Verifiable Credential` →
https://www.w3.org/TR/vc-data-model-2.0/#defn-EnvelopedVerifiableCredential.

**N-041.** (§3.1.2 ¶6) — line 276

> Verifiable Presentations in verifiable presentations MUST use the Enveloped Verifiable Presentation type defined by the [VC-DATA-MODEL-2.0].

_Byte-identical to §3.2.2 ¶6 (N-066) and §3.3.2 ¶6 (N-083)._

_Links:_ `Enveloped Verifiable Presentation` →
https://www.w3.org/TR/vc-data-model-2.0/#defn-EnvelopedVerifiablePresentation.

**N-042.** (§3.1.2 ¶7) — line 277

> Credentials in verifiable presentations MUST be secured. In this case, these credentials are secured using JWS.

_Whether a presentation may carry credentials secured by another mechanism is
not stated: see SD-25._

**N-043.** (§3.1.2 ¶8) — line 278

> To encrypt a secured verifiable presentation when transmitting over an insecure channel, implementers MAY use JSON Web Encryption (JWE) [RFC7516] by nesting the secured verifiable presentation as the plaintext payload of a JWE, per the description of Nested JWTs in [RFC7519].

**N-044.** (§3.1.2 ¶13) — line 357

> Implementations MUST support the JWS compact serialization. Use of the JWS JSON serialization is NOT RECOMMENDED.

_Sits after the examples of the presentation section; its scope is not stated:
see SD-24._

### §3.1.3 JOSE Header Parameters and JWT Claims

_Declared non-normative by ¶1 (N-045); in the HTML the section carries the
classes appendix and informative. Every block is reproduced, each flagged
non-normative. Its COSE twin §3.3.3 is not so declared: see SD-15._

**N-045.** (§3.1.3 ¶1) _[scope]_ _[non-normative]_ — line 361

> This section is non-normative.

**N-046.** (§3.1.3 ¶2) _[advisory]_ _[non-normative]_ — line 362

> When present in the JOSE Header or the JWT Claims Set, members registered in the IANA JSON Web Token Claims registry or the IANA JSON Web Signature and Encryption Header Parameters registry are to be interpreted as defined by the specifications referenced in the registries.

_Links:_ `JOSE Header` → https://www.rfc-editor.org/rfc/rfc7515#section-4;
`JWT Claims Set` → https://www.rfc-editor.org/rfc/rfc7519#section-4;
`JSON Web Token Claims` → https://www.iana.org/assignments/jwt/jwt.xhtml;
`JSON Web Signature and Encryption Header Parameters` →
https://www.iana.org/assignments/jose/jose.xhtml.

**N-047.** (§3.1.3 ¶3) _[implied]_ _[non-normative]_ — line 363

> The normative statements in Registered Header Parameter Names, JOSE Header, and Replicating Claims as Header Parameters apply to securing credentials and presentations.

_A non-normative section declaring that other documents' normative statements
apply: see SD-15._

_Links:_ `Registered Header Parameter Names` →
https://www.rfc-editor.org/rfc/rfc7515#section-4.1; `JOSE Header` →
https://www.rfc-editor.org/rfc/rfc7519#section-5;
`Replicating Claims as Header Parameters` →
https://www.rfc-editor.org/rfc/rfc7519#section-5.3.

**N-048.** (§3.1.3 ¶4) _[implied]_ _[non-normative]_ — line 364

> The unencoded JOSE Header is JSON (application/json), not JSON-LD (application/ld+json).

**N-049.** (§3.1.3 ¶5) _[non-normative]_ — line 365

> It is RECOMMENDED to use the IANA JSON Web Token Claims registry and the IANA JSON Web Signature and Encryption Header Parameters registry to identify any claims and header parameters that might be confused with members defined by [VC-DATA-MODEL-2.0]. These include but are not limited to: iss, kid, alg, iat, exp, and cnf.

_Links:_ `JSON Web Token Claims` →
https://www.iana.org/assignments/jwt/jwt.xhtml;
`JSON Web Signature and Encryption Header Parameters` →
https://www.iana.org/assignments/jose/jose.xhtml.

**N-050.** (§3.1.3 ¶6) _[non-normative]_ — line 366

> When the iat (Issued At) and/or exp (Expiration Time) JWT claims are present, they represent the issuance and expiration time of the signature, respectively. Note that these are different from the validFrom and validUntil properties defined in Validity Period, which represent the validity of the data that is being secured. Use of the nbf (Not Before) claim is NOT RECOMMENDED, as it makes little sense to attempt to assign a future date to a signature.

_Links:_ `Validity Period` →
https://www.w3.org/TR/vc-data-model-2.0/#validity-period.

**N-051.** (§3.1.3 ¶7) _[implied]_ _[non-normative]_ — line 367

> The claims and security provided by this specification are independent of the data secured and semantics provided by the [VC-DATA-MODEL-2.0]. This means that while the security features of this specification ensure data integrity and authenticity, they do not dictate the interpretation of claim data.

**N-052.** (§3.1.3 ¶8) _[non-normative]_ — line 368

> Implementers SHOULD avoid setting JWT claims to values that conflict with the values of verifiable credential properties when a claim and property pair refer to the same conceptual entity, especially with pairs such as iss and issuer, jti and id, and sub and credentialSubject.id. For example, JWK claim iss SHOULD NOT be set to a value which conflicts with the value of verifiable credential property issuer.

_`JWK claim iss`: see SD-4._

**N-053.** (§3.1.3 ¶9) _[non-normative]_ — line 369

> The JWT Claim Names vc and vp MUST NOT be present.

_Restates §1.1.2.1 ¶4 (N-021), which is normative._

**N-054.** (§3.1.3 ¶10) _[lowercase]_ _[non-normative]_ — line 370

> Additional members may be present as header parameters and claims. If they are not understood, they MUST be ignored.

_Lowercase `may be present` (permission). Byte-identical to §3.3.3 ¶5 (N-090),
which is normative._

### §3.2 With SD-JWT

_No blocks of its own: the heading is followed directly by §3.2.1._

### §3.2.1 Securing JSON-LD Verifiable Credentials with SD-JWT

_Not reproduced: ¶7,
`Example 4: A simple example of a verifiable credential secured with SD-JWT`
(lines 382–506), and ¶8, its pointer (line 507)._

**N-055.** (§3.2.1 ¶1) _[implied]_ — line 376

> This section details how to use JOSE to secure verifiable credentials conforming to [VC-DATA-MODEL-2.0].

_Byte-identical to §3.1.1 ¶1 (N-031): this SD-JWT section says
`how to use JOSE`; see SD-3._

**N-056.** (§3.2.1 ¶2) — line 377

> A conforming SD-JWT issuer implementation MUST use [SD-JWT] to secure this media type. The unsecured verifiable credential is the input JWT Claims Set. The Issuer then converts the input JWT Claims Set (i.e., the unsecured verifiable credential) into an [SD-JWT] payload according to SD-JWT issuance instructions.

_Links:_ `SD-JWT issuance instructions` →
https://datatracker.ietf.org/doc/html/draft-ietf-oauth-selective-disclosure-jwt#section-6.1.

**N-057.** (§3.2.1 ¶3) _[lowercase]_ _[permissive]_ — line 378

> The typ header parameter SHOULD be vc+sd-jwt. When present, the cty header parameter SHOULD be vc. The cty header parameter value can be used to differentiate between secured content of different types when using vc+sd-jwt. The content type header parameter is optional, and can be used to express a more specific media type than application/vc when one is available. See Registered Header Parameter Names for additional details regarding usage of typ and cty.

_Lowercase `is optional`; permissive `can be used`, twice; `content type` as
in §3.1.1 ¶3 (N-033; SD-13)._

_Links:_ `Registered Header Parameter Names` →
https://www.rfc-editor.org/rfc/rfc7515#section-4.1.

**N-058.** (§3.2.1 ¶4) — line 379

> A conforming SD-JWT verifier implementation MUST use [SD-JWT] to verify conforming JWS documents that use this media type.

_`conforming JWS documents` in the SD-JWT section: see SD-1. Byte-identical to
§3.2.2 ¶4 (N-064)._

**N-059.** (§3.2.1 ¶5) — line 380

> When securing verifiable credentials with [SD-JWT], implementers SHOULD ensure that properties necessary for the validation and verification of a credential are NOT selectively disclosable (i.e., such properties SHOULD be disclosed). These properties can include but are not limited to @context, type, credentialStatus, credentialSchema, and relatedResource.

_Links:_ `@context` → https://www.w3.org/TR/vc-data-model-2.0/#contexts;
`type` → https://www.w3.org/TR/vc-data-model-2.0/#types; `credentialStatus` →
https://www.w3.org/TR/vc-data-model-2.0/#status; `credentialSchema` →
https://www.w3.org/TR/vc-data-model-2.0/#data-schemas; `relatedResource` →
https://www.w3.org/TR/vc-data-model-2.0/#integrity-of-related-resources.

**N-060.** (§3.2.1 ¶6) — line 381

> To encrypt a secured verifiable credential when transmitting over an insecure channel, implementers MAY use JSON Web Encryption (JWE) [RFC7516] by nesting the secured verifiable credential as the plaintext payload of a JWE, per the instructions in Section 11.2 of [SD-JWT].

### §3.2.2 Securing JSON-LD Verifiable Presentations with SD-JWT

_Not reproduced: ¶10,
`Example 5: A simple example of a verifiable presentation secured with SD-JWT using the EnvelopedVerifiableCredential type`
(lines 520–574); ¶11, its pointer (line 575); ¶12,
`Example 6: A simple example of a verifiable presentation secured with SD-JWT using the EnvelopedVerifiablePresentation type`
(lines 576–616); ¶13, its pointer (line 617). The HTML holds an empty
paragraph between ¶7 and ¶8; it is not counted._

**N-061.** (§3.2.2 ¶1) _[implied]_ — line 511

> This section details how to use [SD-JWT] to secure verifiable presentations conforming to [VC-DATA-MODEL-2.0].

**N-062.** (§3.2.2 ¶2) — line 512

> A conforming SD-JWT issuer implementation MUST use [SD-JWT] to secure this media type. The unsecured verifiable presentation is the unencoded [SD-JWT] payload.

**N-063.** (§3.2.2 ¶3) _[lowercase]_ _[permissive]_ — line 513

> The typ header parameter SHOULD be vp+sd-jwt. When present, the cty header parameter SHOULD be vp. The cty header parameter value can be used to differentiate between secured content of different types when using vp+sd-jwt. The content type header parameter is optional, and can be used to express a more specific media type than application/vc when one is available. See Registered Header Parameter Names for additional details regarding usage of typ and cty.

_Lowercase `is optional`; permissive `can be used`, twice; `content type` as
in §3.1.1 ¶3 (N-033; SD-13); `than application/vc when one is available` in
a presentation section (SD-2)._

_Links:_ `Registered Header Parameter Names` →
https://www.rfc-editor.org/rfc/rfc7515#section-4.1.

**N-064.** (§3.2.2 ¶4) — line 514

> A conforming SD-JWT verifier implementation MUST use [SD-JWT] to verify conforming JWS documents that use this media type.

_`conforming JWS documents`: see SD-1. Byte-identical to §3.2.1 ¶4 (N-058)._

**N-065.** (§3.2.2 ¶5) — line 515

> Verifiable Credentials secured in verifiable presentations MUST use the Enveloped Verifiable Credential type defined by the [VC-DATA-MODEL-2.0].

_Byte-identical to §3.1.2 ¶5 (N-040) and §3.3.2 ¶5 (N-082)._

_Links:_ `Enveloped Verifiable Credential` →
https://www.w3.org/TR/vc-data-model-2.0/#defn-EnvelopedVerifiableCredential.

**N-066.** (§3.2.2 ¶6) — line 516

> Verifiable Presentations in verifiable presentations MUST use the Enveloped Verifiable Presentation type defined by the [VC-DATA-MODEL-2.0].

_Byte-identical to §3.1.2 ¶6 (N-041) and §3.3.2 ¶6 (N-083)._

_Links:_ `Enveloped Verifiable Presentation` →
https://www.w3.org/TR/vc-data-model-2.0/#defn-EnvelopedVerifiablePresentation.

**N-067.** (§3.2.2 ¶7) — line 517

> Credentials in verifiable presentations MUST be secured. These credentials are secured using SD-JWT in this case.

_See SD-25._

**N-068.** (§3.2.2 ¶8) — line 518

> When securing verifiable presentations with [SD-JWT] implementers SHOULD ensure that properties necessary for the validation and verification of a credential are NOT selectively disclosable (i.e., such properties SHOULD be disclosed). These properties can include but are not limited to @context, type, credentialStatus, credentialSchema, and relatedResource.

_Links:_ `@context` → https://www.w3.org/TR/vc-data-model-2.0/#contexts;
`type` → https://www.w3.org/TR/vc-data-model-2.0/#types; `credentialStatus` →
https://www.w3.org/TR/vc-data-model-2.0/#status; `credentialSchema` →
https://www.w3.org/TR/vc-data-model-2.0/#data-schemas; `relatedResource` →
https://www.w3.org/TR/vc-data-model-2.0/#integrity-of-related-resources.

**N-069.** (§3.2.2 ¶9) — line 519

> To encrypt a secured verifiable presentation when transmitting over an insecure channel, implementers MAY use JSON Web Encryption (JWE) [RFC7516] by nesting the secured verifiable presentation as the plaintext payload of a JWE, per the instructions in Section 11.2 of [SD-JWT].

**N-070.** (§3.2.2 ¶14) — line 618

> Implementations MUST support the compact serialization (application/sd-jwt) and MAY support the JSON serialization (application/sd-jwt+json). If the JSON serialization is used, it is RECOMMENDED that a profile be defined to ensure any additional JSON members are understood consistently.

_Sits after the examples of the presentation section; its scope is not stated:
see SD-24._

### §3.3 With COSE

_Every block of its own is reproduced._

**N-071.** (§3.3 ¶1) — line 622

> COSE [RFC9052] is a common approach to encoding and securing information using CBOR [RFC8949]. Verifiable credentials MAY be secured using COSE [RFC9052] and SHOULD be identified through use of content types as outlined in this section.

### §3.3.1 Securing JSON-LD Verifiable Credentials with COSE

_Not reproduced: ¶7,
`Example 7: A simple example of a verifiable credential secured with COSE`
(lines 632–703), and ¶8, its pointer (line 704)._

**N-072.** (§3.3.1 ¶1) _[implied]_ — line 626

> This section details how to use COSE to secure verifiable credentials conforming to [VC-DATA-MODEL-2.0].

**N-073.** (§3.3.1 ¶2) — line 627

> A conforming COSE issuer implementation MUST use COSE_Sign1 as specified in [RFC9052] to secure this media type. The unsecured verifiable credential is the unencoded COSE_Sign1 payload.

**N-074.** (§3.3.1 ¶3) _[lowercase]_ _[permissive]_ — line 628

> The typ (16) header parameter, as described in COSE "typ" (type) Header Parameter, SHOULD be application/vc+cose. The content type (3) header parameter SHOULD be application/vc. The content type (3) header parameter is optional, and can be used to express a more specific media type than application/vc when one is available. See Common COSE Header Parameters for additional details.

_Lowercase `is optional`, beside an unconditional SHOULD on the same
parameter (SD-22); permissive `can be used`._

_Links:_ `COSE "typ" (type) Header Parameter` →
https://www.rfc-editor.org/rfc/rfc9596#section-2;
`Common COSE Header Parameters` →
https://www.rfc-editor.org/rfc/rfc9052#section-3.1.

**N-075.** (§3.3.1 ¶4) — line 629

> A conforming COSE verifier implementation MUST use COSE_Sign1 as specified in [RFC9052] to verify conforming COSE documents that use this media type.

_Byte-identical to §3.3.2 ¶4 (N-081)._

**N-076.** (§3.3.1 ¶5) — line 630

> When including verifiable credentials secured with COSE in verifiable presentations as Enveloped Verifiable Credentials, the credentials MUST be encoded using base64 as specified in [RFC2397].

_No counterpart for presentations in §3.3.2: see SD-26._

_Links:_ `Enveloped Verifiable Credentials` →
https://www.w3.org/TR/vc-data-model-2.0/#defn-EnvelopedVerifiableCredential.

**N-077.** (§3.3.1 ¶6) — line 631

> To encrypt a secured verifiable credential when transmitting over an insecure channel, implementers MAY use COSE encryption, as defined in Section 5 of [RFC9052], by nesting the secured verifiable credential as the plaintext payload of an encrypted COSE object.

### §3.3.2 Securing JSON-LD Verifiable Presentations with COSE

_Not reproduced: ¶9,
`Example 8: A simple example of a verifiable presentation secured withCOSE using the EnvelopedVerifiableCredential type`
(lines 716–751; the title is printed so, SD-14); ¶10, its pointer (line 752);
¶11,
`Example 9: A simple example of a verifiable presentation secured with COSE using the EnvelopedVerifiablePresentation type`
(lines 753–778); ¶12, its pointer (line 779)._

**N-078.** (§3.3.2 ¶1) _[implied]_ — line 708

> This section details how to use COSE to secure verifiable presentations conforming to [VC-DATA-MODEL-2.0].

**N-079.** (§3.3.2 ¶2) — line 709

> A conforming COSE issuer implementation MUST use COSE_Sign1 as specified in [RFC9052] to secure this media type. The unsecured verifiable presentation is the unencoded COSE_Sign1 payload.

**N-080.** (§3.3.2 ¶3) _[lowercase]_ _[permissive]_ — line 710

> The typ (16) header parameter, as described in COSE "typ" (type) Header Parameter, SHOULD be application/vp+cose. The content type (3) header parameter SHOULD be application/vp. The content type (3) header parameter is optional, and can be used to express a more specific media type than application/vp when one is available. See Common COSE Header Parameters for additional details.

_Lowercase `is optional`, beside an unconditional SHOULD on the same
parameter (SD-22); permissive `can be used`._

_Links:_ `COSE "typ" (type) Header Parameter` →
https://www.rfc-editor.org/rfc/rfc9596#section-2;
`Common COSE Header Parameters` →
https://www.rfc-editor.org/rfc/rfc9052#section-3.1.

**N-081.** (§3.3.2 ¶4) — line 711

> A conforming COSE verifier implementation MUST use COSE_Sign1 as specified in [RFC9052] to verify conforming COSE documents that use this media type.

_Byte-identical to §3.3.1 ¶4 (N-075)._

**N-082.** (§3.3.2 ¶5) — line 712

> Verifiable Credentials secured in verifiable presentations MUST use the Enveloped Verifiable Credential type defined by the [VC-DATA-MODEL-2.0].

_Byte-identical to §3.1.2 ¶5 (N-040) and §3.2.2 ¶5 (N-065)._

_Links:_ `Enveloped Verifiable Credential` →
https://www.w3.org/TR/vc-data-model-2.0/#defn-EnvelopedVerifiableCredential.

**N-083.** (§3.3.2 ¶6) — line 713

> Verifiable Presentations in verifiable presentations MUST use the Enveloped Verifiable Presentation type defined by the [VC-DATA-MODEL-2.0].

_Byte-identical to §3.1.2 ¶6 (N-041) and §3.2.2 ¶6 (N-066)._

_Links:_ `Enveloped Verifiable Presentation` →
https://www.w3.org/TR/vc-data-model-2.0/#defn-EnvelopedVerifiablePresentation.

**N-084.** (§3.3.2 ¶7) — line 714

> Credentials in verifiable presentations MUST be secured. These credentials are secured using COSE in this case.

_See SD-25._

**N-085.** (§3.3.2 ¶8) — line 715

> To encrypt a secured verifiable presentation when transmitting over an insecure channel, implementers MAY use COSE encryption, as defined in Section 5 of [RFC9052], by nesting the secured verifiable presentation as the plaintext payload of an encrypted COSE object.

### §3.3.3 COSE Header Parameters and CWT Claims

_Every block is reproduced. Not declared non-normative, unlike its JOSE twin
§3.1.3: see SD-15._

**N-086.** (§3.3.3 ¶1) _[advisory]_ — line 783

> When present in the COSE Header or as CWT Claims, members registered in the IANA CBOR Web Token (CWT) Claims registry or the IANA COSE Header Parameters registry are to be interpreted as defined by the specifications referenced in those registries. CBOR Web Token (CWT) [RFC8392] Claims MAY be included in a COSE header parameter, as specified in I-D.ietf-cose-cwt-claims-in-headers.

_`I-D.ietf-cose-cwt-claims-in-headers` has no entry in Appendix C: see SD-30._

_Links:_ `COSE Header` → https://www.rfc-editor.org/rfc/rfc9052#section-3.1;
`CWT Claims` → https://www.rfc-editor.org/rfc/rfc8392#section-3;
`CBOR Web Token (CWT) Claims` →
https://www.iana.org/assignments/cwt/cwt.xhtml; `COSE Header Parameters` →
https://www.iana.org/assignments/cose/cose.xhtml;
`I-D.ietf-cose-cwt-claims-in-headers` →
https://www.ietf.org/archive/id/draft-ietf-cose-cwt-claims-in-headers-10.html.

**N-087.** (§3.3.3 ¶2) _[implied]_ — line 784

> The normative statements in Header Parameters, Claims, and CBOR Web Token (CWT) Claims in COSE Headers apply to securing credentials and presentations.

_Links:_ `Header Parameters` →
https://www.rfc-editor.org/rfc/rfc9052#section-3.1; `Claims` →
https://www.rfc-editor.org/rfc/rfc8392#section-3;
`CBOR Web Token (CWT) Claims in COSE Headers` →
https://www.ietf.org/archive/id/draft-ietf-cose-cwt-claims-in-headers-10.html.

**N-088.** (§3.3.3 ¶3) — line 785

> It is RECOMMENDED to use the IANA CBOR Web Token Claims registry and the IANA COSE Header Parameters registry to identify any claims and header parameters that might be confused with members defined by [VC-DATA-MODEL-2.0]. These include but are not limited to: iss, kid, alg, iat, exp, and cnf.

_Links:_ `CBOR Web Token Claims` →
https://www.iana.org/assignments/cwt/cwt.xhtml; `COSE Header Parameters` →
https://www.iana.org/assignments/cose/cose.xhtml.

**N-089.** (§3.3.3 ¶4) — line 786

> When the iat (Issued At) and/or exp (Expiration Time) CWT claims are present, they represent the issuance and expiration time of the signature, respectively. Note that these are different from the validFrom and validUntil properties defined in Validity Period, which represent the validity of the data that is being secured. Use of the nbf (Not Before) claim is NOT RECOMMENDED, as it makes little sense to attempt to assign a future date to a signature.

_Links:_ `Validity Period` →
https://www.w3.org/TR/vc-data-model-2.0/#validity-period.

**N-090.** (§3.3.3 ¶5) _[lowercase]_ — line 787

> Additional members may be present as header parameters and claims. If they are not understood, they MUST be ignored.

_Lowercase `may be present` (permission). Byte-identical to §3.1.3 ¶10
(N-054), which is non-normative._



## §4 Key Discovery

_Not reproduced: ¶2 (line 792),
`There are several different ways to discover the verification keys of the issuers and holders.`
(overview; no rule)._

**N-091.** (§4 ¶1) _[advisory]_ — line 791

> To complete the verification process, a verifier needs to obtain the cryptographic keys used to secure the credential.

### §4.1 Using Header Parameters and Claims for Key Discovery

_Every block of its own is reproduced._

**N-092.** (§4.1 ¶1) _[permissive]_ — line 796

> These JOSE header parameters and JWT claims can be used by verifiers to discover verification keys.

_Permissive `can be used by verifiers`. Names
`JOSE header parameters and JWT claims` only, though §4.1.1 to §4.1.3
also name the COSE Header: see SD-29._

### §4.1.1 kid

_Every block is reproduced._

**N-093.** (§4.1.1 ¶1) _[permissive]_ — line 800

> If kid is present in the JOSE Header or the COSE Header, a verifier can use this parameter as a hint indicating which key was used to secure the verifiable credential, when performing a verification process as defined in RFC7515.

_Permissive `a verifier can use this parameter`._

_Links:_ `JOSE Header` → https://www.rfc-editor.org/rfc/rfc7515#section-4.1;
`COSE Header` → https://www.rfc-editor.org/rfc/rfc9052#section-3; `RFC7515` →
https://www.rfc-editor.org/rfc/rfc7515#section-4.1.4.

**N-094.** (§4.1.1 ¶2) — line 801

> kid MUST be present when the key of the issuer or subject is expressed as a DID URL.

### §4.1.2 iss

_Every block is reproduced._

**N-095.** (§4.1.2 ¶1) _[permissive]_ — line 805

> If iss is present in the JOSE Header, the JWT Claims, or the COSE Header, a verifier can use this parameter to obtain a JSON Web Key to use in the verification process.

_Permissive `a verifier can use this parameter`._

_Links:_ `JOSE Header` → https://www.rfc-editor.org/rfc/rfc7515#section-4.1;
`JWT Claims` → https://www.rfc-editor.org/rfc/rfc7519#section-4.1.1;
`COSE Header` → https://www.rfc-editor.org/rfc/rfc9052#section-3;
`JSON Web Key` → https://www.rfc-editor.org/rfc/rfc7517#section-4.

**N-096.** (§4.1.2 ¶2) _[permissive]_ — line 806

> The value of the issuer property can be either a string or an object. When issuer value is a string, iss value, if present, MUST match issuer value. When issuer value is an object with an id value, iss value, if present, MUST match issuer.id value.

_Permissive `can be either a string or an object`: the value domain that the
two MUSTs then condition on._

_Links:_ `issuer` → https://www.w3.org/TR/vc-data-model-2.0/#issuer.

**N-097.** (§4.1.2 ¶3) _[implied]_ — line 807

> If kid is also present in the JOSE Header, it is used to distinguish the specific key used.

_Names the JOSE Header only: see SD-29._

_Links:_ `JOSE Header` → https://www.rfc-editor.org/rfc/rfc7515#section-4.1.

### §4.1.3 cnf

_Every block is reproduced._

**N-098.** (§4.1.3 ¶1) — line 811

> If cnf is present in the JOSE Header, the JWT Claims, or the COSE Header, a verifier MAY use this parameter to identify a proof-of-possession key in the manner described in [RFC7800] or [RFC8747] for use in the verification process.

_Links:_ `JOSE Header` → https://www.rfc-editor.org/rfc/rfc7515#section-4.1;
`JWT Claims` → https://www.rfc-editor.org/rfc/rfc7519#section-4.1.1;
`COSE Header` → https://www.rfc-editor.org/rfc/rfc9052#section-3.

**N-099.** (§4.1.3 ¶2) — line 812

> Use of a proof-of-possession key provided by the Holder to the Issuer to establish a cryptographic binding to the Holder in the Verifiable Credential that is verifiable by the Verifier in the Verifiable Presentation is RECOMMENDED.

### §4.2 Using Controlled Identifier Documents

_Not reproduced: ¶6,
`Example 10: An issuer identified by a controlled identifier document identifier`
(lines 821–828); ¶7,
`Example 11: A kid as a controlled identifier document verification method identifier`
(lines 830–835); ¶9,
`Example 12: A holder identified by a controlled identifier document identifier`
(lines 838–845); ¶10,
`Example 13: A kid as a controlled identifier document verification method identifier`
(lines 847–852). None of the four is well-formed JSON as printed: Examples
10 and 12 elide with `// ...`, and Examples 11 and 13 leave a string
unterminated (SD-14)._

**N-100.** (§4.2 ¶1) _[implied]_ — line 816

> When using controlled identifier documents with this specification, the following requirements apply.

**N-101.** (§4.2 ¶2) — line 817

> The value of the type property of the verification method MUST be JsonWebKey.

**N-102.** (§4.2 ¶3) — line 818

> Verification material MUST be expressed in the publicKeyJwk property of a JsonWebKey. This key material is retrieved based on hints in the JOSE or COSE message envelopes, such as kid or iss. At the time of writing, there is no standard way to retrieve a public key in JWK format from a DID URL or controlled identifier documents.

**N-103.** (§4.2 ¶4) — line 819

> When iss is absent, and the issuer is identified as a [URL], the kid MUST be an absolute [URL] to a verification method listed in a controlled identifier documents or a DID Document.

_`a controlled identifier documents`: see SD-6._

_Links:_ `iss` → #iss (§4.1.2); `kid` → #kid (§4.1.1).

**N-104.** (§4.2 ¶5) — line 820

> When using [URL] identifiers, the kid is RECOMMENDED to be an absolute [URL] that includes a JWK Thumbprint URI as defined in [RFC7638]. For example: https://vendor.example/issuers/42/keys/urn:ietf:params:oauth:jwk-thumbprint:sha-256:NzbLsXh8uDCcd-6MNwXF4W_7noWXFZAfHkxZsRGC9Xs

_`as defined in [RFC7638]`: see SD-34._

**N-105.** (§4.2 ¶8) — line 837

> When the holder is identified as a [URL], and iss is absent, the kid MUST be an absolute [URL] to a verification method listed in a controlled identifier document.

_Links:_ `iss` → #iss (§4.1.2); `kid` → #kid (§4.1.1).



## §5 Algorithms

_Every block is reproduced._

**N-106.** (§5 ¶1) _[implied]_ — line 856

> This specification might be used with many different key discovery protocols. Therefore, discovery of verification keys is described in 4. Key Discovery, and is assumed to have succeeded prior to beginning the verification process.

**N-107.** (§5 ¶2) — line 857

> As a general rule, verifiers SHOULD strive to minimize the processing of untrusted data. This includes minimizing any processing of the protected header, unprotected header, or payload as part of the key discovery procedures.

**N-108.** (§5 ¶3) — line 858

> After verification has succeeded, additional validation checks SHOULD be performed as described in Section 5.4 Validation

_The sentence ends without a full stop: see SD-8._

**N-109.** (§5 ¶4–¶5) _[implied]_ — lines 859–862

```
The outputs for the following algorithms are:
- status: a boolean indicating the result of verification, true for success and false for failure.
- document: a document conforming to the [VC-DATA-MODEL-2.0]
- mediaType: vc or vp
```

_The output domains omit the null that every failure branch sets: see SD-20._

### §5.1 Verifying a Credential or Presentation Secured with JOSE

_Every block is reproduced._

**N-110.** (§5.1 ¶1–¶2) _[implied]_ — lines 866–868

```
The inputs for this algorithm are:
- inputMediaType: vc+jwt or vp+jwt
- inputDocument: the verifiable credential secured as a JWT [RFC7519]
```

_`inputDocument` names the credential only, though `inputMediaType` admits
`vp+jwt`: see SD-18._

**N-111.** (§5.1 ¶3–¶4) _[implied]_ _[algorithm]_ — lines 869–880

```
Upon receipt of the verifiable credential or presentation secured as a JWT [RFC7519], the holder or verifier follows this algorithm:
1. Follow the algorithm defined in Validating a JWT [RFC7519].
2. If processing completes successfully:
    2.1. Set status to true
    2.2. Set mediaType to vc or vp
    2.3. Set document to the decoded JWS payload.
    2.4. Return
3. If processing aborts for any reason or the JWT is rejected:
    3.1. Set status to false
    3.2. Set document to null
    3.3. Set mediaType to null
    3.4. Return
```

_Step 2.2 does not say how to choose between `vc` and `vp`: see SD-19._

_Links:_ `Validating a JWT` →
https://www.rfc-editor.org/rfc/rfc7519#section-7.2.

### §5.2 Verifying a Credential or Presentation Secured with SD-JWT

_Every block is reproduced._

**N-112.** (§5.2 ¶1–¶2) _[implied]_ — lines 884–886

```
The inputs for this algorithm are:
- inputMediaType: vc+sd-jwt
- inputDocument: the verifiable credential secured with [SD-JWT]
```

_`inputMediaType: vc+sd-jwt` only: see SD-17._

**N-113.** (§5.2 ¶3–¶4) _[implied]_ _[algorithm]_ — lines 887–898

```
Upon receipt of the verifiable credential or presentation secured with [SD-JWT], the holder or verifier follows this algorithm:
1. Follow the algorithms defined in SD-JWT for verification of the SD-JWT.
2. If processing completes successfully:
    2.1. Set status to true
    2.2. Set mediaType to vc
    2.3. Convert the SD-JWT payload back into the JWT Claims Set by reversing the process in [SD-JWT]. Set document to the JWT Claims Set. (For examples of the transition from JWT Claims Set to SD-JWT payload, please see SD-JWT examples).
    2.4. Return
3. If processing aborts for any reason or the SD-JWT is rejected:
    3.1. Set status to false
    3.2. Set document to null
    3.3. Set mediaType to null
    3.4. Return
```

_Step 2.2 sets `vc` only: see SD-17._

_Links:_ `SD-JWT` →
https://datatracker.ietf.org/doc/html/draft-ietf-oauth-selective-disclosure-jwt#section-8;
`SD-JWT examples` →
https://datatracker.ietf.org/doc/html/draft-ietf-oauth-selective-disclosure-jwt#appendix-A.

### §5.3 Verifying a Credential or Presentation Secured with COSE

_Every block is reproduced._

**N-114.** (§5.3 ¶1–¶2) _[implied]_ — lines 902–904

```
The inputs for this algorithm are:
- inputMediaType: vc+cose or vp+cose
- inputDocument: the verifiable credential or verifiable presentation secured with CBOR Object Signing and Encryption (COSE): Structures and Process
```

_Links:_ `CBOR Object Signing and Encryption (COSE): Structures and Process` →
https://www.rfc-editor.org/rfc/rfc9052.

**N-115.** (§5.3 ¶3–¶4) _[implied]_ _[algorithm]_ — lines 905–916

```
Upon receipt of the verifiable credential or presentation secured with [RFC9052], the holder or verifier follows this algorithm:
1. Follow the algorithm defined in CBOR Object Signing and Encryption (COSE): Structures and Process [RFC9052] under the Signing and Verification Process for COSE_Sign1.
2. If processing completes successfully:
    2.1. Set status to true
    2.2. Set mediaType to vc or vp
    2.3. Set document to the decoded COSE_Sign1 payload.
    2.4. Return
3. If processing aborts for any reason:
    3.1. Set status to false
    3.2. Set document to null
    3.3. Set mediaType to null
    3.4. Return
```

_Step 3 has no rejection clause, unlike step 3 of §5.1 and §5.2: see SD-21._

_Links:_ `CBOR Object Signing and Encryption (COSE): Structures and Process` →
https://www.rfc-editor.org/rfc/rfc9052.

### §5.4 Validation

_Every block is reproduced._

**N-116.** (§5.4 ¶1) — line 920

> All claims expected for the typ MUST be present. All claims that are understood MUST be evaluated according the verifier's validation policies. All claims that are not understood MUST be ignored.

_`according the`: see SD-7. `claims expected for the typ` is not defined
anywhere: see SD-23._

**N-117.** (§5.4 ¶2) — line 921

> The verified document returned from verification MUST be a well-formed compact JSON-LD document, as described in Verifiable Credentials Data Model v2.0.

_Links:_ `Verifiable Credentials Data Model v2.0` →
https://www.w3.org/TR/vc-data-model-2.0/#conformance.

**N-118.** (§5.4 ¶3) — line 922

> Schema extension mechanisms such as credentialSchema SHOULD be checked. If the extension mechanism type is not understood, this property MUST be ignored.

**N-119.** (§5.4 ¶4) — line 923

> Status extension mechanisms such as credentialStatus SHOULD be checked. If the extension mechanism type is not understood, this property MUST be ignored.

**N-120.** (§5.4 ¶5) — line 924

> Based on the validation policy of the verifier, the type of credentials, and the type of securing mechanism, additional validation checks MAY be applied. For example, dependencies between multiple credentials, ordering or timing information associated with multiple credentials, and/or multiple presentations could cause an otherwise valid credential or presentation to be considered invalid.



## §6 IANA Considerations

_Declared non-normative by ¶1 (N-121); in the HTML the section carries the
class informative. Every block of §6 is reproduced, each flagged
non-normative: the six media-type registration templates are below in full.
See SD-16._

**N-121.** (§6 ¶1) _[scope]_ _[non-normative]_ — line 928

> This section is non-normative.

### §6.1 Media Types

_No blocks of its own: the heading is followed directly by §6.1.1._

### §6.1.1 application/vc+jwt

_Every block is reproduced: the registration paragraph and its template, in
one fence._

**N-122.** (§6.1.1 ¶1–¶2) _[lowercase]_ _[table]_ _[IANA]_ _[non-normative]_ — lines 934–956

```
This specification registers the application/vc+jwt Media Type specifically for identifying a JSON Web Token (JWT) with a payload conforming to the Verifiable Credential Data Model.
| Type name: | application
| Subtype name: | vc+jwt
| Required parameters: | N/A
| Optional parameters: | N/A
| Encoding considerations: | binary; application/jwt values are a series of base64url-encoded values (some of which may be the empty string) separated by period ('.').
| Security considerations: |
    As defined in this specification. See also the security considerations in [RFC7519].
| Interoperability considerations: |
    As defined in this specification.
| Published specification: | https://www.w3.org/TR/vc-jose-cose
| Applications that will use this media: |
    W3C Verifiable Credential issuer, holder, and verifier software, conforming to the [VC-DATA-MODEL-2.0], are among the applications that will use the media types. Conforming application types are described here and here.
| Restrictions on usage: | N/A
| Additional information: |
    1. Deprecated alias names for this type: N/A
    2. Magic number(s): N/A
    3. File extension(s): N/A
    4. Macintosh file type code: N/A
    5. Object Identifiers: N/A
| Author: | Ivan Herman ivan@w3.org
| Intended usage: | COMMON
| Change controller: | W3C Verifiable Credentials Working Group public-vc-wg@w3.org
```

_Lowercase `some of which may be the empty string` (a permission of the
encoding)._

_`Applications that will use this media:` (SD-9). The rows of the six
templates are byte-identical except Subtype name, Encoding considerations and
the second sentence of Security considerations._

_Links:_ `JSON Web Token (JWT)` → https://www.rfc-editor.org/rfc/rfc7519;
`Verifiable Credential Data Model` →
https://www.w3.org/TR/vc-data-model-2.0/#verifiable-credentials;
`this specification` → #security-considerations (§7.2); `this specification`
→ #conformance (§1.1); `here` → #conformance (§1.1); `here` →
https://www.w3.org/TR/vc-data-model-2.0/#conformance.

### §6.1.2 application/vp+jwt

_Every block is reproduced: the registration paragraph and its template, in
one fence._

**N-123.** (§6.1.2 ¶1–¶2) _[lowercase]_ _[table]_ _[IANA]_ _[non-normative]_ — lines 960–982

```
This specification registers the application/vp+jwt Media Type specifically for identifying a JSON Web Token (JWT) with a payload conforming to the Verifiable Presentations definition in the Verifiable Credential Data Model.
| Type name: | application
| Subtype name: | vp+jwt
| Required parameters: | N/A
| Optional parameters: | N/A
| Encoding considerations: | binary; application/jwt values are a series of base64url-encoded values (some of which may be the empty string) separated by period ('.').
| Security considerations: |
    As defined in this specification. See also the security considerations in [RFC7519].
| Interoperability considerations: |
    As defined in this specification.
| Published specification: | https://www.w3.org/TR/vc-jose-cose
| Applications that will use this media: |
    W3C Verifiable Credential issuer, holder, and verifier software, conforming to the [VC-DATA-MODEL-2.0], are among the applications that will use the media types. Conforming application types are described here and here.
| Restrictions on usage: | N/A
| Additional information: |
    1. Deprecated alias names for this type: N/A
    2. Magic number(s): N/A
    3. File extension(s): N/A
    4. Macintosh file type code: N/A
    5. Object Identifiers: N/A
| Author: | Ivan Herman ivan@w3.org
| Intended usage: | COMMON
| Change controller: | W3C Verifiable Credentials Working Group public-vc-wg@w3.org
```

_Lowercase `some of which may be the empty string`, as in §6.1.1 (N-122)._

_`Applications that will use this media:` (SD-9). The rows of the six
templates are byte-identical except Subtype name, Encoding considerations and
the second sentence of Security considerations._

_Links:_ `JSON Web Token (JWT)` → https://www.rfc-editor.org/rfc/rfc7519;
`Verifiable Presentations definition in the Verifiable Credential Data Model`
→ https://www.w3.org/TR/vc-data-model-2.0/#verifiable-presentations;
`this specification` → #security-considerations (§7.2); `this specification`
→ #conformance (§1.1); `here` → #conformance (§1.1); `here` →
https://www.w3.org/TR/vc-data-model-2.0/#conformance.

### §6.1.3 application/vc+sd-jwt

_Every block is reproduced: the registration paragraph and its template, in
one fence._

**N-124.** (§6.1.3 ¶1–¶2) _[lowercase]_ _[table]_ _[IANA]_ _[non-normative]_ — lines 986–1008

```
This specification registers the application/vc+sd-jwt Media Type specifically for identifying a Selective Disclosure for JWTs (SD-JWT) with a payload conforming to the Verifiable Credential Data Model.
| Type name: | application
| Subtype name: | vc+sd-jwt
| Required parameters: | N/A
| Optional parameters: | N/A
| Encoding considerations: | binary; application/sd-jwt values are a series of base64url-encoded values (some of which may be the empty string) separated by period ('.') and tilde ('~') characters.
| Security considerations: |
    As defined in this specification. See also the security considerations in Selective Disclosure for JWTs (SD-JWT).
| Interoperability considerations: |
    As defined in this specification.
| Published specification: | https://www.w3.org/TR/vc-jose-cose
| Applications that will use this media: |
    W3C Verifiable Credential issuer, holder, and verifier software, conforming to the [VC-DATA-MODEL-2.0], are among the applications that will use the media types. Conforming application types are described here and here.
| Restrictions on usage: | N/A
| Additional information: |
    1. Deprecated alias names for this type: N/A
    2. Magic number(s): N/A
    3. File extension(s): N/A
    4. Macintosh file type code: N/A
    5. Object Identifiers: N/A
| Author: | Ivan Herman ivan@w3.org
| Intended usage: | COMMON
| Change controller: | W3C Verifiable Credentials Working Group public-vc-wg@w3.org
```

_Lowercase `some of which may be the empty string`, as in §6.1.1 (N-122)._

_`Applications that will use this media:` (SD-9). The rows of the six
templates are byte-identical except Subtype name, Encoding considerations and
the second sentence of Security considerations._

_Links:_ `Selective Disclosure for JWTs (SD-JWT)` →
https://datatracker.ietf.org/doc/html/draft-ietf-oauth-selective-disclosure-jwt;
`Verifiable Credential Data Model` →
https://www.w3.org/TR/vc-data-model-2.0/#verifiable-credentials;
`this specification` → #security-considerations (§7.2); `this specification`
→ #conformance (§1.1); `here` → #conformance (§1.1); `here` →
https://www.w3.org/TR/vc-data-model-2.0/#conformance.

### §6.1.4 application/vp+sd-jwt

_Every block is reproduced: the registration paragraph and its template, in
one fence._

**N-125.** (§6.1.4 ¶1–¶2) _[lowercase]_ _[table]_ _[IANA]_ _[non-normative]_ — lines 1012–1034

```
This specification registers the application/vp+sd-jwt Media Type specifically for identifying a Selective Disclosure for JWTs (SD-JWT) with a payload conforming to the Verifiable Presentations definition in the Verifiable Credential Data Model.
| Type name: | application
| Subtype name: | vp+sd-jwt
| Required parameters: | N/A
| Optional parameters: | N/A
| Encoding considerations: | binary; application/sd-jwt values are a series of base64url-encoded values (some of which may be the empty string) separated by period ('.') and tilde ('~') characters.
| Security considerations: |
    As defined in this specification. See also the security considerations in Selective Disclosure for JWTs (SD-JWT).
| Interoperability considerations: |
    As defined in this specification.
| Published specification: | https://www.w3.org/TR/vc-jose-cose
| Applications that will use this media: |
    W3C Verifiable Credential issuer, holder, and verifier software, conforming to the [VC-DATA-MODEL-2.0], are among the applications that will use the media types. Conforming application types are described here and here.
| Restrictions on usage: | N/A
| Additional information: |
    1. Deprecated alias names for this type: N/A
    2. Magic number(s): N/A
    3. File extension(s): N/A
    4. Macintosh file type code: N/A
    5. Object Identifiers: N/A
| Author: | Ivan Herman ivan@w3.org
| Intended usage: | COMMON
| Change controller: | W3C Verifiable Credentials Working Group public-vc-wg@w3.org
```

_Lowercase `some of which may be the empty string`, as in §6.1.1 (N-122)._

_`Applications that will use this media:` (SD-9). The rows of the six
templates are byte-identical except Subtype name, Encoding considerations and
the second sentence of Security considerations._

_Links:_ `Selective Disclosure for JWTs (SD-JWT)` →
https://datatracker.ietf.org/doc/html/draft-ietf-oauth-selective-disclosure-jwt;
`Verifiable Presentations definition in the Verifiable Credential Data Model`
→ https://www.w3.org/TR/vc-data-model-2.0/#verifiable-presentations;
`this specification` → #security-considerations (§7.2); `this specification`
→ #conformance (§1.1); `here` → #conformance (§1.1); `here` →
https://www.w3.org/TR/vc-data-model-2.0/#conformance.

### §6.1.5 application/vc+cose

_Every block is reproduced: the registration paragraph and its template, in
one fence._

**N-126.** (§6.1.5 ¶1–¶2) _[table]_ _[IANA]_ _[non-normative]_ — lines 1038–1060

```
This specification registers the application/vc+cose Media Type specifically for identifying a COSE object [RFC9052] with a payload conforming to the Verifiable Credential Data Model.
| Type name: | application
| Subtype name: | vc+cose
| Required parameters: | N/A
| Optional parameters: | N/A
| Encoding considerations: | binary (CBOR)
| Security considerations: |
    As defined in this specification. See also the security considerations in [RFC9052].
| Interoperability considerations: |
    As defined in this specification.
| Published specification: | https://www.w3.org/TR/vc-jose-cose
| Applications that will use this media: |
    W3C Verifiable Credential issuer, holder, and verifier software, conforming to the [VC-DATA-MODEL-2.0], are among the applications that will use the media types. Conforming application types are described here and here.
| Restrictions on usage: | N/A
| Additional information: |
    1. Deprecated alias names for this type: N/A
    2. Magic number(s): N/A
    3. File extension(s): N/A
    4. Macintosh file type code: N/A
    5. Object Identifiers: N/A
| Author: | Ivan Herman ivan@w3.org
| Intended usage: | COMMON
| Change controller: | W3C Verifiable Credentials Working Group public-vc-wg@w3.org
```

_`Applications that will use this media:` (SD-9). The rows of the six
templates are byte-identical except Subtype name, Encoding considerations and
the second sentence of Security considerations._

_Links:_ `Verifiable Credential Data Model` →
https://www.w3.org/TR/vc-data-model-2.0/#verifiable-credentials;
`this specification` → #security-considerations (§7.2); `this specification`
→ #conformance (§1.1); `here` → #conformance (§1.1); `here` →
https://www.w3.org/TR/vc-data-model-2.0/#conformance.

### §6.1.6 application/vp+cose

_Every block is reproduced: the registration paragraph and its template, in
one fence._

**N-127.** (§6.1.6 ¶1–¶2) _[table]_ _[IANA]_ _[non-normative]_ — lines 1064–1086

```
This specification registers the application/vp+cose Media Type specifically for identifying a COSE object [RFC9052] with a payload conforming to the Verifiable Presentations definition in the Verifiable Credential Data Model.
| Type name: | application
| Subtype name: | vp+cose
| Required parameters: | N/A
| Optional parameters: | N/A
| Encoding considerations: | binary (CBOR)
| Security considerations: |
    As defined in this specification. See also the security considerations in [RFC9052].
| Interoperability considerations: |
    As defined in this specification.
| Published specification: | https://www.w3.org/TR/vc-jose-cose
| Applications that will use this media: |
    W3C Verifiable Credential issuer, holder, and verifier software, conforming to the [VC-DATA-MODEL-2.0], are among the applications that will use the media types. Conforming application types are described here and here.
| Restrictions on usage: | N/A
| Additional information: |
    1. Deprecated alias names for this type: N/A
    2. Magic number(s): N/A
    3. File extension(s): N/A
    4. Macintosh file type code: N/A
    5. Object Identifiers: N/A
| Author: | Ivan Herman ivan@w3.org
| Intended usage: | COMMON
| Change controller: | W3C Verifiable Credentials Working Group public-vc-wg@w3.org
```

_`Applications that will use this media:` (SD-9). The rows of the six
templates are byte-identical except Subtype name, Encoding considerations and
the second sentence of Security considerations._

_Links:_
`Verifiable Presentations definition in the Verifiable Credential Data Model`
→ https://www.w3.org/TR/vc-data-model-2.0/#verifiable-presentations;
`this specification` → #security-considerations (§7.2); `this specification`
→ #conformance (§1.1); `here` → #conformance (§1.1); `here` →
https://www.w3.org/TR/vc-data-model-2.0/#conformance.



## §7 Other Considerations

_Declared non-normative by ¶1 (N-128); in the HTML the section carries the
class informative. Every block of §7 is reproduced, each flagged
non-normative, because nearly every one is phrased as advice or obligation._

**N-128.** (§7 ¶1) _[scope]_ _[non-normative]_ — line 1090

> This section is non-normative.

### §7.1 Privacy Considerations

_Every block is reproduced._

**N-129.** (§7.1 ¶1) _[advisory]_ _[non-normative]_ — line 1094

> Verifiable Credentials often contain sensitive information that needs to be protected to ensure the privacy and security of organizations and individuals. This section outlines some privacy considerations relevant to implementers and users.

**N-130.** (§7.1 ¶2) _[advisory]_ _[non-normative]_ — line 1095

> Implementers are advised to note and abide by all privacy considerations called out in [VC-DATA-MODEL-2.0].

**N-131.** (§7.1 ¶3) _[advisory]_ _[non-normative]_ — line 1096

> Implementers are additionally advised to reference the Privacy Consideration section of the JWT specification and NIST Special Publication 800-122 [[SP-800-122] "Guide to Protecting the Confidentiality of Personally Identifiable Information (PII)" for privacy guidance.

_`[[SP-800-122]`: see SD-11._

_Links:_ `Privacy Consideration` →
https://www.rfc-editor.org/rfc/rfc7519#section-12.

**N-132.** (§7.1 ¶4–¶5) _[advisory]_ _[non-normative]_ — lines 1097–1100

```
In addition to the privacy recommendations in the [VC-DATA-MODEL-2.0], the following considerations are given:
- Minimization of data: It is considered best practice for Verifiable Credentials to only contain the minimum amount of data necessary to achieve their intended purpose. This helps to limit the amount of sensitive information that is shared or stored unnecessarily.
- Informed consent: It is considered best practice that individuals be fully informed about how their data will be used and provide the ability to consent to or decline the use of their data. This helps to ensure that individuals maintain control over their own personal information.
- Data protection: It is considered best practice to protect Verifiable Credentials using strong encryption and other security measures to prevent unauthorized access, modification, or disclosure.
```

**N-133.** (§7.1 ¶6) _[advisory]_ _[non-normative]_ — line 1101

> These considerations are not exhaustive, and implementers and users are advised to consult additional privacy resources and best practices to ensure the privacy and security of Verifiable Credentials implemented using this specification.

### §7.2 Security Considerations

_Every block is reproduced._

**N-134.** (§7.2 ¶1) _[advisory]_ _[non-normative]_ — line 1105

> This section outlines security considerations for implementers and users of this specification. It is important to carefully consider these factors to ensure the security and integrity of Verifiable Credentials when implemented using JOSE or COSE.

**N-135.** (§7.2 ¶2) _[advisory]_ _[non-normative]_ — line 1106

> When implementing this specification, it is essential to address all security issues relevant to broad cryptographic applications. This especially includes protecting the user's asymmetric private and symmetric secret keys, as well as employing countermeasures against various attacks. Failure to adequately address these issues could compromise the security and integrity of Verifiable Credentials, potentially leading to unauthorized access, modification, or disclosure of sensitive information.

**N-136.** (§7.2 ¶3) _[advisory]_ _[non-normative]_ — line 1107

> Implementers are advised to follow best practices and established cryptographic standards to ensure the secure handling of keys and other sensitive data. Additionally, conduct regular security assessments and audits to identify and address any vulnerabilities or threats.

**N-137.** (§7.2 ¶4) _[advisory]_ _[non-normative]_ — line 1108

> Follow all security considerations outlined in [RFC7515] and [RFC7519].

**N-138.** (§7.2 ¶5) _[advisory]_ _[non-normative]_ — line 1109

> When utilizing JSON-LD, take special care around remote retrieval of contexts and follow the additional security considerations noted in [JSON-LD11].

**N-139.** (§7.2 ¶6) _[advisory]_ _[non-normative]_ — line 1110

> As noted in [RFC7515] when utilizing JSON [RFC7159], strict validation is a security requirement. If malformed JSON is received, it may be impossible to reliably interpret the producer's intent, potentially leading to ambiguous or exploitable situations. To prevent these risks, it is essential to use a JSON parser that strictly validates the syntax of all input data. It is essential that any JSON inputs that do not conform to the JSON-text syntax defined in [RFC7159] be rejected in their entirety by JSON parsers. Failure to reject invalid input could compromise the security and integrity of Verifiable Credentials.

_The lowercase `it may be impossible` is epistemic and does not set the
lowercase flag._

### §7.3 Accessibility

_Every block is reproduced._

**N-140.** (§7.3 ¶1) _[advisory]_ _[non-normative]_ — line 1114

> When implementing this specification, it is crucial for technical implementers to consider various accessibility factors. Ignoring accessibility concerns renders the information unusable for a significant portion of the population. To ensure equal access for all individuals, regardless of their abilities, it is vital to adhere to accessibility guidelines and standards, such as the Web Content Accessibility Guidelines (WCAG 2.1) [WCAG21]. This becomes even more critical when establishing systems that involve cryptography, as they have historically posed challenges for assistive technologies.

**N-141.** (§7.3 ¶2) _[advisory]_ _[non-normative]_ — line 1115

> Implementers are advised to note and abide by all accessibility considerations called out in [VC-DATA-MODEL-2.0].



## §8 Examples

_Declared non-normative by ¶1 (N-142). Besides ¶1, §8 holds 13 examples
(Examples 14 to 26) and two paragraphs, both in §8.5 (N-143, N-200)._

**N-142.** (§8 ¶1) _[scope]_ _[non-normative]_ — line 1119

> This section is non-normative.

### §8.1 Controllers

_No entries: ¶1–¶4 are `Example 14: A minimal controlled identifier document`
(lines 1123–1127),
`Example 15: A controlled identifier document with verification method` (lines
1129–1145),
`Example 16: A controlled identifier document with verification relationships`
(lines 1147–1165) and
`Example 17: A verifiable credential controlled identifier document` (lines
1167–1238)._

### §8.2 Credentials

_No entries: ¶1–¶2 are
`Example 18: A revocable credential with multiple subjects` (lines 1242–1455)
and `Example 19: A credential with a schema` (lines 1456–1613)._

### §8.3 Presentations

_No entries: ¶1 is `Example 20: Presentation` (lines 1617–1790)._

### §8.4 Data URIs

_No entries: ¶1–¶3 are
`Example 21: A simple URI-encoded SD-JWT Verifiable Credential` (lines
1794–1796), `Example 22: A simple URI-encoded SD-JWT Verifiable Presentation`
(lines 1798–1800) and
`Example 23: A simple URI-encoded COSE Verifiable Presentation` (lines
1802–1804)._

### §8.5 COSE Examples

_Not reproduced: ¶2–¶4,
`Example 24: A COSE Sign 1 Protected Header for a Verifiable Credential`
(lines 1809–1819),
`Example 25: A COSE Sign 1 Protected Header for a Verifiable Presentation`
(lines 1821–1831) and `Example 26: A COSE Sign 1 with an attached payload`
(lines 1833–1842)._

**N-143.** (§8.5 ¶1) _[advisory]_ _[non-normative]_ — line 1808

> These examples rely on CBOR Diagnostic Notation. Remember that all actual interchange always happens in the binary format.

_Links:_ `CBOR Diagnostic Notation` →
https://www.rfc-editor.org/rfc/rfc7049#section-6.

**N-200.** (§8.5 ¶5) _[permissive]_ _[non-normative]_ — line 1844

> The payload can be either a credential or presentation as described in Securing Mechanisms.

_Follows Example 26 and describes its payload; the permissive
`can be either a credential or presentation` states the values a payload
takes. Added in pass 1 when its checks were run (see Ids)._

_Links:_ `Securing Mechanisms` →
https://www.w3.org/TR/vc-data-model-2.0/#securing-mechanisms.



## §A Revision History

_Declared non-normative by ¶1 (N-144); in the HTML the appendix carries the
classes appendix and informative. Every block is reproduced._

**N-144.** (§A ¶1) _[scope]_ _[non-normative]_ — line 1848

> This section is non-normative.

**N-145.** (§A ¶2–¶4) _[changelog]_ _[non-normative]_ — lines 1849–1858

```
This section describes substantive changes that have been made to this specification.
Changes since the First Candidate Recommendation:
- Updated to use the Controlled Identifiers v1.0 specification.
- Changed media types from application/{vc,vp}+ld+json+{jwt,sd-jwt,cose} to application/{vc,vp}+{jwt,sd-jwt,cose}.
- Use COSE "typ" (type) Header Parameter.
- Described differentiating between secured content of different types using the cty header parameter.
- Added considerations about what which parameters may be selectively disclosed.
- Described encrypting secured credentials and presentations.
- Said that use of the nbf (Not Before) claim is NOT RECOMMENDED.
- Updated many examples.
```

_Item 7 carries the only capitalised keyword of the appendix; it reports the
change made in §3.1.3 ¶6 and §3.3.3 ¶4 (N-050, N-089). Item 5 reads
`what which`: see SD-12. Its lowercase `may be selectively disclosed` reports
a change and does not set the lowercase flag._

_Links:_ `First Candidate Recommendation` →
https://www.w3.org/TR/2024/CRD-vc-jose-cose-20240425/;
`Controlled Identifiers v1.0` → https://www.w3.org/TR/cid-1.0/;
`COSE "typ" (type) Header Parameter` →
https://www.rfc-editor.org/rfc/rfc9596#section-2.



## §B Acknowledgements

_Declared non-normative by ¶1 (N-201); in the HTML the appendix carries the
classes appendix and informative. Not reproduced: ¶2 (line 1863), an
acknowledgement._

**N-201.** (§B ¶1) _[scope]_ _[non-normative]_ — line 1862

> This section is non-normative.

_Added in pass 1 when its checks were run (see Ids), so that each of the six
paragraphs of this wording is an entry._



## §C References

_No entries — C.1 and C.2 (lines 1867–1921) are bibliographies; the entries
that bear on a finding are named under Source defects and tensions (SD-11,
SD-30). Line 1922 is the page's back-to-top arrow and lines 1923–1980 are
the HTML's term-reference panels (`Permalink`, `Referenced in:`); neither
carries text of the specification._

### §C.1 Normative references

_No entries (bibliography)._

### §C.2 Informative references

_No entries (bibliography)._



## Source defects and tensions

_Recorded, never repaired: every entry above carries the source exactly as
printed. SD-1 to SD-14 are textual defects; SD-15 to SD-33 are tensions and
gaps that a requirement, a schema or a test will meet. SD-34, a textual defect
found after the list was numbered (pass 2; recorded here in pass 3), is
appended rather than renumbered. Each names the entries it touches._

- **SD-1.** Wrong conformance class. §3.2.1 ¶4 and §3.2.2 ¶4 (N-058, N-064)
  both read
  `A conforming SD-JWT verifier implementation MUST use [SD-JWT] to verify conforming JWS documents that use this media type.`
  The HTML links `conforming JWS documents` to the §1.1.1 definition of the
  JWS class (dfn-conforming-jws-document), while §1.1.1 ¶6 (N-009) says
  `A conforming SD-JWT verifier implementation verifies conforming SD-JWT documents`.
  Read literally, the two SD-JWT MUSTs bind an SD-JWT verifier to JWS
  documents.
- **SD-2.** Credential media type in the presentation sections. §3.1.2 ¶3 and
  §3.2.2 ¶3 (N-038, N-063) read
  `can be used to express a more specific media type than application/vc when one is available`,
  copied from their credential twins; the COSE presentation twin §3.3.2 ¶3
  (N-080) reads `than application/vp when one is available`.
- **SD-3.** JOSE named in the SD-JWT section. §3.2.1 ¶1 (N-055) reads
  `This section details how to use JOSE to secure verifiable credentials conforming to [VC-DATA-MODEL-2.0].`,
  byte-identical to §3.1.1 ¶1 (N-031); its presentation twin §3.2.2 ¶1 (N-061)
  reads
  `This section details how to use [SD-JWT] to secure verifiable presentations`.
- **SD-4.** JWK for JWT. §3.1.3 ¶8 (N-052) reads
  `For example, JWK claim iss SHOULD NOT be set`, while the same paragraph
  opens `Implementers SHOULD avoid setting JWT claims`. JWK (RFC 7517) defines
  key parameters, not claims; iss is a JWT claim, which the source itself
  links as `JWT Claims` to RFC 7519 §4.1.1 in §4.1.2 ¶1 (N-095). The keyword
  stands as printed.
- **SD-5.** Disclosure contents misstated. §1.1.2.2 ¶2 item 3 (N-023) reads
  `These are base64url-encoded JSON arrays containing the digest of the disclosed claim, the claim name, and the claim value.`
  The source's own Example 4 (§3.2.1 ¶7, lines 424–506) contradicts it: each
  of its eight `Contents:` arrays opens with a 22-character string that is not
  the 43-character `SHA-256 Hash:` value printed above it, and that hash is
  the SHA-256 of the printed `Disclosure(s):` string (recomputed from the HTML
  for all eight in this pass). The first element is the salt that item 4 mentions
  (`Each disclosable claim is combined with a salt value before hashing`); the
  digest is computed over the disclosure, not carried in it.
- **SD-6.** Number disagreement. §4.2 ¶4 (N-103) reads
  `listed in a controlled identifier documents or a DID Document`; §4.2 ¶8
  (N-105) reads `listed in a controlled identifier document.`
- **SD-7.** Missing word. §5.4 ¶1 (N-116) reads
  `evaluated according the verifier's validation policies`.
- **SD-8.** Missing full stop. §5 ¶3 (N-108) ends
  `as described in Section 5.4 Validation` with no terminal punctuation; the
  HTML confirms the paragraph closes after the link.
- **SD-9.** Template field name. Each of §6.1.1 to §6.1.6 (N-122 to N-127)
  names a row `Applications that will use this media:`, with no noun after
  `media`; the cell beside it says
  `are among the applications that will use the media types`.
- **SD-10.** Title of the data model. The opening paragraph of each of §6.1.1
  to §6.1.6 says `Verifiable Credential Data Model`. The prose elsewhere
  names it `Verifiable Credentials Data Model v2.0` — §1.1.2 ¶1 (N-013), §5.4
  ¶2 (N-117) and the nine pointers after the examples of §3 — except the
  Abstract, which says `Verifiable Credential data model` (line 34, twice),
  and §2, which says `W3C Verifiable Credentials specification` (N-024). The
  HTML links the §6 name and `Verifiable Credentials Data Model v2.0` to the
  same document; the other two are each followed by the citation
  `[VC-DATA-MODEL-2.0]`.
- **SD-11.** Broken citation. §7.1 ¶3 (N-131) reads
  `[[SP-800-122] "Guide to Protecting the Confidentiality of Personally Identifiable Information (PII)"`,
  with unbalanced brackets in the HTML text itself, and neither reference list
  (§C.1, §C.2) has an entry for it.
- **SD-12.** Doubled word. §A ¶4 item 5 (N-145) reads
  `Added considerations about what which parameters may be selectively disclosed.`
- **SD-13.** A header parameter that does not exist. §3.1.1 ¶3, §3.1.2 ¶3,
  §3.2.1 ¶3 and §3.2.2 ¶3 (N-033, N-038, N-057, N-063) each say
  `The content type header parameter is optional`, with `content type` set in
  code font in the HTML as if it were a parameter name. JOSE has no header
  parameter of that name; the same paragraphs name the content-type parameter
  `cty`, three times each. The COSE twins (§3.3.1 ¶3, §3.3.2 ¶3) name theirs
  `content type (3)`, which is COSE header label 3.
- **SD-14.** Example defects (named only; the examples artifact carries the
  fixtures). §3.3.2 ¶9 is titled
  `Example 8: A simple example of a verifiable presentation secured withCOSE using the EnvelopedVerifiableCredential type`;
  the HTML id (secured-withcose) confirms the missing space. §4.2 ¶7 and ¶10
  (Examples 11 and 13) leave the string value of `kid` unterminated, so
  neither is well-formed JSON as printed; §4.2 ¶6 and ¶9 (Examples 10 and 12)
  elide with `// ...`, so they are not JSON either. In Example 2 (§3.1.2 ¶9)
  and Example 8 (§3.3.2 ¶9), each under its application/vp label, and in
  Example 20 (§8.3 ¶1), the id of an enveloped credential holds two data URLs
  joined by a semicolon (lines 314 and 744, for two). The examples artifact
  is home to all three: examples/README.md P-03 (the title), D-02 and D-01
  (Examples 11 and 13; 10 and 12), D-15 (the joined data URLs; messages.yaml
  TEN-15, TEN-24); its D-01 to D-23 and P-01 to P-03 are the full list.
  Examples that contradict the text are SD-33.
- **SD-15.** Normative status of the JOSE header section. §3.1.3 is declared
  non-normative (N-045) yet carries six capitalised keywords (N-049, N-050,
  N-052 ×2, N-053, N-054), and its ¶3 (N-047) declares that the normative
  statements of RFC 7515 §4.1, RFC 7519 §5 and RFC 7519 §5.3 apply. Its COSE
  twin §3.3.3 carries the parallel RECOMMENDED, NOT RECOMMENDED and MUST
  (N-088 to N-090) and is normative. Under §1.1 ¶1 (N-002) the JOSE rules
  (registry use, nbf, claim conflicts, ignoring members not understood) are
  therefore advice while the COSE ones bind. §1.1.1 ¶1 (N-004) defines a
  conforming JWS document by `all of the "MUST" statements in Section 3.1`,
  and §3.1.3 sits inside §3.1; whether its MUST NOT and MUST count toward the
  class is not stated. The MUST NOT of §3.1.3 ¶9 is also imposed, normatively,
  by §1.1.2.1 ¶4 (N-021).
- **SD-16.** Media types defined only in a non-normative section. §6 is
  declared non-normative (N-121), so its six registration templates are not
  normative under §1.1 ¶1, while §3 ¶6 (N-030) requires
  `media types defined in this specification MUST be used` and §1.1.2 ¶7
  (N-017) names all six. Each template's `Security considerations:` cell links
  `this specification` to §7.2, which is also non-normative.
- **SD-17.** No input for SD-JWT presentations. §5.2 is titled
  `Verifying a Credential or Presentation Secured with SD-JWT` and its ¶3
  reads
  `Upon receipt of the verifiable credential or presentation secured with [SD-JWT]`,
  but its inputs are `inputMediaType: vc+sd-jwt` and
  `inputDocument: the verifiable credential secured with [SD-JWT]` (N-112),
  and step 2.2 is `Set mediaType to vc` (N-113). vp+sd-jwt, the typ value of
  §3.2.2 (N-063) and registered in §6.1.4, has no verification algorithm that
  admits it.
- **SD-18.** Credential-only input documents. §5.1 ¶2 (N-110) pairs
  `inputMediaType: vc+jwt or vp+jwt` with
  `inputDocument: the verifiable credential secured as a JWT [RFC7519]`; §5.2
  ¶2 likewise names the credential only. §5.3 ¶2 (N-114) names both.
- **SD-19.** Unspecified choice. Step 2.2 of §5.1 and of §5.3 (N-111, N-115)
  is `Set mediaType to vc or vp`, with no rule for choosing (not from
  inputMediaType, not from typ).
- **SD-20.** Output domains omit failure. §5 ¶5 (N-109) declares
  `document: a document conforming to the [VC-DATA-MODEL-2.0]` and
  `mediaType: vc or vp`, but steps 3.2 and 3.3 of each algorithm (N-111,
  N-113, N-115) set both to null.
- **SD-21.** Asymmetric failure branches. Step 3 of §5.3 (N-115) is
  `If processing aborts for any reason:`; step 3 of §5.1 (N-111) is
  `If processing aborts for any reason or the JWT is rejected:` and of §5.2
  (N-113) `If processing aborts for any reason or the SD-JWT is rejected:`.
- **SD-22.** Recommended and optional at once. §3.3.1 ¶3 (N-074) says
  `The content type (3) header parameter SHOULD be application/vc.` and then
  `The content type (3) header parameter is optional`; §3.3.2 ¶3 (N-080) has
  the same pair for application/vp. The JOSE and SD-JWT twins condition their
  SHOULD (`When present, the cty header parameter SHOULD be vc.`, §3.1.1 ¶3,
  N-033); the COSE SHOULD is unconditional, so it reads as recommending that
  the optional parameter be present.
- **SD-23.** Undefined term. §5.4 ¶1 (N-116) requires
  `All claims expected for the typ MUST be present.`; the document never says
  which claims a typ value leads a verifier to expect.
- **SD-24.** Serialization rules placed in the presentation sections.
  `Implementations MUST support the JWS compact serialization. Use of the JWS JSON serialization is NOT RECOMMENDED.`
  is §3.1.2 ¶13 (N-044) and
  `Implementations MUST support the compact serialization (application/sd-jwt)`
  opens §3.2.2 ¶14 (N-070): each closes a presentation section, after its
  examples, and neither says whether it also governs credentials (§3.1.1,
  §3.2.1).
- **SD-25.** Mixed mechanisms in one presentation. §3.1.2 ¶7 (N-042) reads
  `Credentials in verifiable presentations MUST be secured. In this case, these credentials are secured using JWS.`;
  §3.2.2 ¶7 (N-067) and §3.3.2 ¶7 (N-084) end
  `These credentials are secured using SD-JWT in this case.` and
  `These credentials are secured using COSE in this case.` Whether the second
  sentence describes the example or constrains a presentation to carry only
  credentials secured by its own mechanism is not stated. The source's own
  COSE presentation examples carry SD-JWT-secured content, so the sentence
  describes neither of them: see SD-33.
- **SD-26.** Encoding of enveloped COSE presentations. §3.3.1 ¶5 (N-076)
  requires that COSE-secured credentials enveloped in presentations
  `MUST be encoded using base64 as specified in [RFC2397]`; §3.3.2, which
  requires the Enveloped Verifiable Presentation type for presentations in
  presentations (N-083), states no encoding for a COSE-secured one.
- **SD-27.** Antecedent of this media type. §3.1.1 ¶2 and ¶4 (N-032, N-034),
  and the matching paragraphs of §3.1.2, §3.2.1, §3.2.2, §3.3.1 and §3.3.2,
  say `to secure this media type` and `that use this media type`; no sentence
  before ¶2 in its section names a media type. Each section first names its
  own in ¶3, between the two, as the typ value; §1.1.2 ¶7 (N-017) lists all
  six and §6 registers them.
- **SD-28.** Two definitions of JWT Claims Set. In the §1.1.2 ¶3 definition
  list (N-014), the JWT entry says
  `A JWT Claims Set is a JSON object containing one or more claims about an entity`
  and the SD-JWT entry says
  `A JWT Claims Set is one or more claims about an entity`.
- **SD-29.** JOSE-only wording over COSE coverage. §4.1 ¶1 (N-092) reads
  `These JOSE header parameters and JWT claims can be used by verifiers to discover verification keys.`
  and §4.1.2 ¶3 (N-097) `If kid is also present in the JOSE Header`, while
  §4.1.1 ¶1, §4.1.2 ¶1 and §4.1.3 ¶1 each also name `the COSE Header`.
- **SD-30.** Unpinned normative dependencies. The [SD-JWT] entry of §C.1
  (line 1906) names an Internet-Draft with no version and no date
  (`IETF. Internet-Draft.`), and the links in §3.2.1 ¶2 and §5.2 ¶4 go to the
  unversioned datatracker URL (sections 6.1 and 8, Appendix A) — yet §1.1.2.2,
  §3.2 and §5.2 depend on it. §3.3.3 ¶1 (N-086) relies on
  `I-D.ietf-cose-cwt-claims-in-headers`, which the HTML links to draft -10 and
  which has no entry in either reference list.
- **SD-31.** Errata. The front matter records `Errata exists.` (line 25),
  linked to the editors' errata page. This file reproduces the Recommendation
  as published; no erratum was consulted or applied.
- **SD-32.** Circular part. §1.1.2.2 ¶2 item 1 (N-023) reads
  `An SD-JWT consists of three main parts: the SD-JWT itself, optional disclosures, and an optional KB-JWT (Key Binding JWT).`,
  naming the whole as one of its own parts.
- **SD-33.** Examples that contradict the text (decoded from the HTML, not
  the .txt). Examples 8 and 9 (§3.3.2 ¶9 and ¶11) secure a presentation with
  COSE, but the credential that Example 8 envelopes is a
  `data:application/vc+sd-jwt` value and the presentation that Example 9
  envelopes a `data:application/vp+sd-jwt` one, while §3.3.2 ¶7 (N-084) says
  `These credentials are secured using COSE in this case.` Example 20 (§8.3
  ¶1) gives its COSE-secured credential as `data:application/vc+cose;base64`
  where first printed (line 1632) and as `data:application/vc+cose;base64url`
  at lines 1666, 1695 and 1739, against §3.3.1 ¶5 (N-076):
  `MUST be encoded using base64 as specified in [RFC2397]`. The JWS header
  of the SD-JWT presentation that Examples 6 (§3.2.2 ¶12) and 9 envelope, as a
  `data:application/vp+sd-jwt` value, declares typ vp+ld+json+sd-jwt and cty
  vp+ld+json (their outer headers, an SD-JWT in Example 6 and a COSE_Sign1 in
  Example 9, carry no typ), and the issuer-signed JWT that Examples 21 and 22
  (§8.4 ¶1 and ¶2) share declares typ vc+ld+json+sd-jwt and cty vc+ld+json —
  the forms §A ¶4 item 2 (N-145)
  reports as changed since the First Candidate Recommendation, where
  §3.2.1 ¶3 and §3.2.2 ¶3 (N-057, N-063) recommend vc+sd-jwt and vp+sd-jwt.
  Example 22, titled a Verifiable Presentation and carried as
  `data:application/vp+sd-jwt`, carries the issuer-signed JWT of Example 21,
  byte for byte, so its header declares a credential typ.
- **SD-34.** A definition attributed to a document that does not contain it.
  §4.2 ¶5 (N-104, R-0073) reads
  `that includes a JWK Thumbprint URI as defined in [RFC7638]`, and the
  example after it in the same paragraph ends
  `urn:ietf:params:oauth:jwk-thumbprint:sha-256:NzbLsXh8uDCcd-6MNwXF4W_7noWXFZAfHkxZsRGC9Xs`.
  RFC 7638 (§C.1, lines 1889–1890) defines the JWK Thumbprint and no URI
  form: it contains no `urn:ietf:params:oauth` and no `jwk-thumbprint`, and
  its only URIs are its authors' addresses. The prefix is defined by RFC 9278
  §3 (JWK Thumbprint URI, August 2022), which the source never cites (the
  number 9278 occurs 0 times in the .txt), and the printed example ends with
  RFC 9278 §6's example URI, whose thumbprint is the RFC 7638 §3.1 example
  value. Checked against fetched copies of both RFCs, sha256
  98b29ab9…3110 and c84d83e4…4816, the digests schema/README.md lists
  (F-06); requirements.yaml (R-0073) and messages.yaml (TEN-23) record it
  too.



## Coverage

**Entries.** 147 — N-001 to N-145, N-200 and N-201 (see Ids) — in source
order: §1 1; §1.1 2; §1.1.1 9; §1.1.2 5; §1.1.2.1 4; §1.1.2.2 2; §2 1; §3 6; §3.1 0; §3.1.1 5; §3.1.2 9;
§3.1.3 10; §3.2 0; §3.2.1 6; §3.2.2 10; §3.3 1; §3.3.1 6; §3.3.2 8; §3.3.3 5;
§4 1; §4.1 1; §4.1.1 2; §4.1.2 3; §4.1.3 2; §4.2 6; §5 4; §5.1 2; §5.2 2; §5.3
2; §5.4 5; §6 1; §6.1 0; §6.1.1 1; §6.1.2 1; §6.1.3 1; §6.1.4 1; §6.1.5 1;
§6.1.6 1; §7 1; §7.1 5; §7.2 6; §7.3 2; §8 1; §8.1 0; §8.2 0; §8.3 0; §8.4 0;
§8.5 2; §A 2; §B 1; §C, §C.1, §C.2 0. By top-level section: §1 23, §2 1, §3
66, §4 15, §5 15, §6 7, §7 14, §8 3, §A 2, §B 1, §C 0.

Of the 147, 37 carry _[non-normative]_ and 110 lie in normative sections.
Containers: 128 blockquotes and 19 fences, reproducing 353 .txt lines.

**Keyword reconciliation: 97 = 97.** Mechanically, by script against the .txt:
the counter's pattern finds 104 capitalised keywords in the whole file; 7 fall
inside the conventions paragraph that the counter strips (§1.1 ¶2, N-003) and
are excluded, exactly as bin/bcp14-count excludes them; each of the other 97
was mapped from its character offset to its .txt line and from the line to the
entry whose range reproduces it: 97 mapped, 0 unmapped, 0 mapped to more than
one entry. Independently, the same counter over the verbatim text of all 147
entries together, with the conventions paragraph stripped as in the source,
returns 97 — MUST 48, SHOULD 25, MAY 11, RECOMMENDED 6, NOT RECOMMENDED 4,
MUST NOT 2, SHOULD NOT 1, the source's split exactly. So every keyword
occurrence of the source lies in an entry and none is counted twice.

Per section: §1.1.1 6; §1.1.2.1 3; §1.1.2.2 1; §3 4; §3.1.1 5; §3.1.2 10;
§3.1.3 6; §3.2.1 7; §3.2.2 13; §3.3 2; §3.3.1 6; §3.3.2 8; §3.3.3 4; §4.1.1 1;
§4.1.2 2; §4.1.3 2; §4.2 5; §5 2; §5.4 9; §A 1.

Occurrence by occurrence (line, keyword, entry):

| entry | line | keywords |
|---|---|---|
| N-004 | 116 | MUST |
| N-005 | 117 | MUST |
| N-007 | 119 | MUST |
| N-008 | 120 | MUST |
| N-010 | 122 | MUST |
| N-011 | 123 | MUST |
| N-019 | 146 | MUST |
| N-020 | 147 | MUST |
| N-021 | 148 | MUST NOT |
| N-022 | 152 | SHOULD |
| N-028 | 175 | RECOMMENDED |
| N-029 | 176 | SHOULD, SHOULD |
| N-030 | 177 | MUST |
| N-032 | 184 | MUST |
| N-033 | 185 | SHOULD, SHOULD |
| N-034 | 186 | MUST |
| N-035 | 187 | MAY |
| N-037 | 272 | MUST |
| N-038 | 273 | SHOULD, SHOULD |
| N-039 | 274 | MUST |
| N-040 | 275 | MUST |
| N-041 | 276 | MUST |
| N-042 | 277 | MUST |
| N-043 | 278 | MAY |
| N-044 | 357 | MUST, NOT RECOMMENDED |
| N-049 | 365 | RECOMMENDED |
| N-050 | 366 | NOT RECOMMENDED |
| N-052 | 368 | SHOULD, SHOULD NOT |
| N-053 | 369 | MUST NOT |
| N-054 | 370 | MUST |
| N-056 | 377 | MUST |
| N-057 | 378 | SHOULD, SHOULD |
| N-058 | 379 | MUST |
| N-059 | 380 | SHOULD, SHOULD |
| N-060 | 381 | MAY |
| N-062 | 512 | MUST |
| N-063 | 513 | SHOULD, SHOULD |
| N-064 | 514 | MUST |
| N-065 | 515 | MUST |
| N-066 | 516 | MUST |
| N-067 | 517 | MUST |
| N-068 | 518 | SHOULD, SHOULD |
| N-069 | 519 | MAY |
| N-070 | 618 | MUST, MAY, RECOMMENDED |
| N-071 | 622 | MAY, SHOULD |
| N-073 | 627 | MUST |
| N-074 | 628 | SHOULD, SHOULD |
| N-075 | 629 | MUST |
| N-076 | 630 | MUST |
| N-077 | 631 | MAY |
| N-079 | 709 | MUST |
| N-080 | 710 | SHOULD, SHOULD |
| N-081 | 711 | MUST |
| N-082 | 712 | MUST |
| N-083 | 713 | MUST |
| N-084 | 714 | MUST |
| N-085 | 715 | MAY |
| N-086 | 783 | MAY |
| N-088 | 785 | RECOMMENDED |
| N-089 | 786 | NOT RECOMMENDED |
| N-090 | 787 | MUST |
| N-094 | 801 | MUST |
| N-096 | 806 | MUST, MUST |
| N-098 | 811 | MAY |
| N-099 | 812 | RECOMMENDED |
| N-101 | 817 | MUST |
| N-102 | 818 | MUST |
| N-103 | 819 | MUST |
| N-104 | 820 | RECOMMENDED |
| N-105 | 837 | MUST |
| N-107 | 857 | SHOULD |
| N-108 | 858 | SHOULD |
| N-116 | 920 | MUST, MUST, MUST |
| N-117 | 921 | MUST |
| N-118 | 922 | SHOULD, MUST |
| N-119 | 923 | SHOULD, MUST |
| N-120 | 924 | MAY |
| N-145 | 1857 | NOT RECOMMENDED |

**Lowercase.** 14 entries carry _[lowercase]_, holding 16 weighted words
(entry: line and word): N-014: 131 must; N-023: 153 optional ×2, 154 must;
N-033: 185 optional; N-038: 273 optional; N-054: 370 may; N-057: 378 optional;
N-063: 513 optional; N-074: 628 optional; N-080: 710 optional; N-090: 787 may;
N-122: 939 may; N-123: 965 may; N-124: 991 may; N-125: 1017 may.

**Permissive.** 11 entries carry _[permissive]_, holding 15 lowercase can
(entry: line and count): N-033: 185 ×2; N-038: 273 ×2; N-057: 378 ×2; N-063:
513 ×2; N-074: 628; N-080: 710; N-092: 796; N-093: 800; N-095: 805; N-096:
806; N-200: 1844.

**Advisory.** 18 entries carry _[advisory]_: N-018, N-046, N-086, N-091,
N-129, N-130, N-131, N-132, N-133, N-134, N-135, N-136, N-137, N-138, N-139,
N-140, N-141, N-143.

**Implied.** 32 entries carry _[implied]_: N-001, N-006, N-009, N-012, N-013,
N-015, N-016, N-017, N-024, N-025, N-026, N-027, N-031, N-036, N-047, N-048,
N-051, N-055, N-061, N-072, N-078, N-087, N-097, N-100, N-106, N-109, N-110,
N-111, N-112, N-113, N-114, N-115.

**Identical texts.** 8 groups of blockquote entries are byte-identical, so a
requirement id that cites one of them can match its quoted words while naming
the wrong section — the surface that bin/check-id-joins --surface reports:
N-031 (§3.1.1 ¶1) = N-055 (§3.2.1 ¶1); N-034 (§3.1.1 ¶4) = N-039 (§3.1.2 ¶4);
N-040 (§3.1.2 ¶5) = N-065 (§3.2.2 ¶5) = N-082 (§3.3.2 ¶5); N-041 (§3.1.2 ¶6) =
N-066 (§3.2.2 ¶6) = N-083 (§3.3.2 ¶6); N-045 (§3.1.3 ¶1) = N-121 (§6 ¶1) =
N-128 (§7 ¶1) = N-142 (§8 ¶1) = N-144 (§A ¶1) = N-201 (§B ¶1); N-054
(§3.1.3 ¶10) = N-090 (§3.3.3 ¶5); N-058 (§3.2.1 ¶4) = N-064 (§3.2.2 ¶4); N-075 (§3.3.1 ¶4) = N-081
(§3.3.2 ¶4). The six templates of §6.1.1 to §6.1.6 (N-122 to N-127) also share
all but three of their table lines verbatim.

**Excluded, and why.** Front matter: the title block, Status of This
Document and Table of Contents are publication matter, and the Abstract
summarises the scope that §1 ¶1 (N-001) states. §1 ¶2–¶4: overview of the
base technologies. §4 ¶2: overview. The 26 examples and the nine pointers to
the data model that follow the §3 examples: non-normative by §1.1 ¶1, and the
examples artifact's material. §B ¶2: an acknowledgement. Appendix C:
bibliography, cited where a finding rests on it (SD-11, SD-30). The
back-to-top arrow and the term-reference panels: navigation. No capitalised
BCP 14 keyword occurs in any excluded block.

**Checks run in pass 1.** By script, over this file, the .txt and the HTML;
each states what it examined beside what it found, and each was shown to
catch a planted defect before its result was trusted.

- Rendering. bin/render-w3c run again on the HTML gives the .txt byte for
  byte; an instrumented copy that records the HTML element stack of every
  line gives it too, with 0 unbalanced elements.
- Containers. 353 container lines compared with their .txt lines after the
  structure prefix, the prefix recomputed from the element stack: 0 defects;
  every header range equals the lines reproduced, no line is reproduced
  twice, entries run in source order, and no reproduced line continues an
  element begun on the line before. Planted: a changed word, a wrong step number, a
  wrong list marker and a wrong line range were each caught.
- Locators. 147 examined, section and ¶ range recomputed from the HTML block
  structure and the heading each entry is filed under: 0 defects. Planted: a
  wrong ¶ was caught.
- Keywords. As under Keyword reconciliation, 97 of 97 mapped and the table's
  78 rows equal to the measurement. Planted: removing N-030 left its MUST
  unmapped.
- Flags. 147 entries tested against the definitions under How to read: 7
  findings, all the stated exceptions — N-003 (the conventions paragraph),
  N-139 and N-145 (a lowercase may that does not set the flag), and N-024,
  N-027, N-059 and N-068 (a can that only describes, two in N-024). Planted:
  dropping a non-normative flag was caught.
- Counts. Every number and list under How to read and in this section
  recomputed: entries per section, flags, containers, the lowercase,
  permissive and modal counts, the identical-text groups, the template rows,
  and keywords outside the entries (0 in the 1350 non-blank lines no entry
  reproduces). Planted: a wrong container count was caught.
- Quotations. 308 backtick spans (191 distinct) in pass 1, 314 (196
  distinct) after the cross-check pass added SD-34, the note under N-104 and
  one span to SD-33, each tested whole, longest
  first: all are contiguous substrings of the .txt, none crosses a line of
  this file, 305 occur in a section their note or entry names (299 in pass 1;
  the 6 added lie in §4.2 and §3.2.2), and the other
  9 occur where their note gives a line instead — the title block and lines
  25, 34, 39, 43 and 1964. The spans of the source-defect list were also read
  against each section they are attributed to. Planted: one inserted word
  and one misattributed section were each caught.
- Undelimited quotations. The prose outside containers and backticks, 9132
  words in pass 1 (the cross-check pass's recount, by a method that gives 8824
  for that version, gives 9179 after its edits, this bullet included, 355 more), swept for runs of
  five or more words found verbatim in the .txt: 15
  runs before the cross-check pass's edits and after them (reproduced by script), all names — 13 section titles used as headings, a pair of terms in
  the Links paragraph of How to read and a type name in SD-26; no unmarked
  quotation.
- Links. 115 pairs checked against the HTML links in their entry's lines: 0
  mismatches, and the 22 internal targets resolve to the sections given. The
  pairs cover 117 links (one pair in each of §6.1.3 and §6.1.4 names a link
  that occurs twice); the rule under How to read accounts for all 395 links
  in the entries' lines, the other 278 being 104 citations, 11 numbered
  section references, 43 heading permalinks, 94 links to term definitions, 8
  data-model term sections and 18 self-named URLs and mail addresses.
  Planted: a wrong target was caught.
- Rendering artefact. 353 reproduced lines: 0 with a space before a comma,
  full stop, semicolon, colon or closing bracket or after an opening one;
  the same test finds 149 such spaces in the whole .txt, all inside
  examples. All 1043 no-break spaces of the HTML lie inside examples: 791 in
  pre-formatted blocks, kept in the .txt, and 252 outside them, which the
  renderer collapses.
- SD-5. The 8 disclosure digests of Example 4, recomputed from the HTML: 8
  equal the printed SHA-256 Hash values, and no Contents array opens with
  its digest.
- File. The front matter parses to the same values under bin/_yaml.py and
  bin/_record_yaml.py; the file carries none of the scaffold markers that
  bin/validate rejects.
