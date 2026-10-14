---
record: draft-ietf-vcon-vcon-core-04
kind: design-notes
title: "draft-ietf-vcon-vcon-core-04 — design notes"
extracted: "2026-10-13"
reviewed_by: "pass 2, adversarial verifier, 2026-10-14"
---

# draft-ietf-vcon-vcon-core-04 — bearing on our design

vCon is the only document this library holds that was designed by people who had
never heard of us, for a problem we do not have, and that nonetheless builds
every structure ARCH-0002 claims is necessary: a signed container, a
must-understand extension mechanism, a supersession model, a per-object schema
set, and an attempt at key-relative vocabulary. `record.yaml` says why we keep
it — *"the best available test of whether our statement form can express
something we did not design."* This file is that test, run against the source.

**Nothing here decides anything.** DEC-002 and DEC-005 are open; `CLAUDE.md` in
`m-of-n` states that *"DEC-001 … DEC-005 and DEC-007 are open. No encoding, tag
language, or envelope has been selected."* `MD-3` (2026-09-28) is a *narrowing*
of DEC-002 to option 5, recorded in a meeting minute and in `PLAN-0003`; **no
DEC-002 ADR exists**, and `CONTRIBUTING` §5 is explicit that only an ADR accepts
a decision. ARCH-0002 P2–P7 are `[draft]`; `ADR-0002` is `proposed` with an
empty `decision_makers`. §5 below records where this source *supports* MD-3 and
where it *cuts against* it, as `docs/extraction.md` requires.

**Three voices, kept apart throughout.**

| marker | means |
|---|---|
| unmarked, or quoted | **what the draft says**, with a §-locator |
| **[we conclude]** | our inference from the draft — not the draft's position |
| **[open]** | unresolved, and named again in §6 |
| **[closed …, pass 2]** | a pass-1 `[open]` marker discharged against a cited source |
| **[verified …, pass 2]** | checked at pass 2 against a source named on the spot |

Locators are the draft's own section numbers **unless followed by *below* or
*of this file***, which point at this document's own headings. The two numbering
schemes collide — this file has a §4.2 and so does the draft — so every
self-reference is marked. Quotes are verbatim from
`.cache/draft-ietf-vcon-vcon-core-04.txt`, sha256
`cc2a2cb5…033cd722`, with the RFC-format line wrapping removed. Where the
draft uses `*emphasis*` markers in its plain-text rendering, they are preserved.
Two artefacts of that rendering are joined rather than reproduced, and are flagged
here so a verifier diffing against the source knows to expect them: the published
text hyphenates across line ends (`de-\nidentification`, `party-\nidentifying` in
§2.5), and Appendices B and C split long JSON strings mid-token (`a\nttachments`
in Appendix B's closing `$comment`).

---

## 1. What we adopt

**A1 — the extension-document contract (§2.5).** `[ARCH-0002 P3]` This is the
best single thing in the document and we have no equivalent. A vCon extension is
not a registered label; it is a *document* that MUST contain five named sections,
and three of them are obligations nothing in our stack imposes:

- *Compatibility Considerations*: **"Describe how the extension behaves in the
  presence of implementations that do not support it."**
- *Incompatibility Considerations*: for each incompatibility, **"state the
  processing that is affected, for example redaction versus transcription,
  whether the extension name is therefore required in the critical (Section
  4.1.4) parameter, and the behavior required of implementations that do not
  support the extension."**
- *Privacy and Integrity Considerations*: whether the extension's parameters can
  carry party-identifying data or PII and **"how a redactor is expected to handle
  them"**; and **"State whether the extension introduces any new external content
  references, and if so, the integrity mechanism that protects them."**

P3 says a type is a schema carrying *representation*, *constraints on usage*,
*semantic descriptions*, *tags for human review* and *short descriptions*. P3
does not say what the *constraints on usage* field should contain, and ARCH-0002
§P3 complains that *"a schema that validates structure and says nothing about
meaning forces every consumer to re-derive intent from prose."* §2.5 is the
missing content: **a per-consumer-role statement of what breaks if you do not
understand me.** That is the field P3 is reaching for, written by someone who had
to ship it. **[we conclude]** this is directly transplantable and should be a
required part of a P3 schema, not an extension-document convention.

**A2 — a mandatory asserter index on contributed content (§4.4.3).** `[P2]` The
Attachment Object carries a party index and the draft's own word for it is
provenance: **"To provide provenance for the attachment, the party index MUST be
specified."** It then draws the exact distinction P2 needs — **"This party is not
necessarily the document's author, but rather the party that distributed the
document"** — and it explicitly anticipates the assembler: **"an organization
that processes or constructs the vCon may add attachments containing information
about the conversation. The organization or entity that adds the attachment
SHOULD be represented as a Party Object."** §4.1 of this file argues that this
single paragraph materially narrows the topic's *"no speaker"* finding.

**A3 — two version concepts, separately named (§2.1).** `[library scope.md §5]`
The terminology section defines both: **"vCon instance version - a single version
of an instance of a conversation, which may be modified to redact or amend
additional information forming a subsequent vCon instance version"** and **"vCon
syntax version - the version for the data syntax used for form a vCon."** Our
`docs/scope.md` §5 has one word, *version*, doing both jobs, which is why §4.2
below can be asked as a question at all.

**A4 — sign the bytes you were handed (§5.2).** `[R-O-05]` The signed payload is
**"the Base64Url Encoded string containing either: the unsigned form of the JSON
vCon; or the gzipped [GZIP] unsigned form of the JSON vCon."** A verifier
base64url-decodes and hashes; it does not parse, reorder, re-serialise or
canonicalise. **The word "canonical" appears exactly once in 8,904 lines**, in
the `ContentHash` definition copied from STIR PASSporT (§2.2), and even there it
describes the *external* content's digest, not the vCon's. A live, implemented,
JSON-based signed-container format has **no canonicalisation requirement at all**
— because it never re-derives the signed bytes. See §5 below for what that does to
DEC-002.

**A5 — one schema definition over two serialisation stories.** `[MD-3]` The draft
ships Appendix B (JSON Schema) and Appendix C (CDDL) for the *same* JSON format;
`[CBOR]` and `[CDDL]` are **informative** references (§8.2). CDDL describing JSON
is RFC 8610 working as designed. MD-3 says *"YAML is the human form with a
canonical one-way mapping"*; vCon demonstrates the machine-checkable half of that
arrangement — a single CDDL governing both a human-legible and a machine form —
in a shipped document. **Adopt the arrangement, not its status**: both appendices
are subordinate to the prose, in identical words — **"This JSON schema is provided
as informational. The text in sections 1-6 of this document define the normative
definition of the vCon schema. If the JSON schema provided below differs from that
in the text of the above sections, the text should be taken as the definitive
definition and the JSON Schema below should be consider incorrect."** (Appendix B;
Appendix C repeats it for the CDDL). §4.5 below treats that as the record's
central finding about P3.

**A6 — digest and locator together, digest authoritative (§2.4, §2.4.2, §5.1).**
`[R-M-07, R-M-11]` Externally referenced files **"MUST have the parameters: url,
content_hash"**, and both the Redacted and Amended Objects repeat it:
`content_hash` MUST be included if `url` is provided (§4.1.8.1, §4.1.9.1). §5.1
states the reason without hedging: **"the signature on the vCon does not secure
the file contents from modification."** R-M-11 says *"A locator SHALL be treated
as non-authoritative evidence about a subject, not as its definition"* and *"At
least one content digest SHALL be bound in all cases."* vCon implements exactly
that rule, for the one class of subject that is bytes.

**A7 — per-type applicability as a first-class, published table (§4.3.1.6).**
`[P3]` Table 1 gives, for every Dialog parameter × every Dialog type, one of
`M / S / O / SN / X / -`. Our ARCH-0001 §4 types carry cardinality in prose. A
table that a tool can read is the difference between a schema and a description,
and the draft is careful about its own status: **"The parameter definitions in
the subsections of this document are definitive; this table is provided as a
summary."** The `-` cell is rejected separately (C5).

Both formal artifacts carry **part** of this table and the part they drop is the
finding. Appendix C discriminates `dialog_object_type` into five per-type groups
(`dialog_recording_type`, `dialog_text_type`, `dialog_recording_set_type`,
`dialog_transfer_type`, `dialog_incomplete_type`) and comments the prohibitions
(`; Parameters prohibited in "transfer" type Dialog Objects`); Appendix B does the
same with `allOf` / `if` / `then` keyed on `type` consts — `{"if": {"properties":
{"type": {"const": "incomplete"}} …}, "then": {"required": ["disposition"]}}`. So
**both express the `M` and `X` cells and neither expresses `S`, `SN` or `-`**: a
SHOULD becomes `?` plus a prose comment (`; parties SHOULD be present`).

**The loss is not symmetric, and the asymmetry is the sharper finding.** Table 1
is 24 rows × 5 columns = **120 cells**: `X` 57, `O` 30, `S` 19, `M` 9, `SN` 4,
`-` 1. Counted cell by cell, and the two appendices fail three different ways.

1. **Appendix B's `X` is enforceable; Appendix C's is advisory.** B writes all
   **57** prohibition cells — the count matches Table 1 exactly, 13 for
   `transfer`, 14 for `recording-set`, 15 for `incomplete`, 7 for `recording`,
   8 for `text` — as `{"if": {…"const": t}, "then": {"not": {"anyOf":
   [{"required": [p]}, …]}}}`. That construction **bites without closing the
   object**: B contains no `additionalProperties` or `unevaluatedProperties`
   anywhere (C4) and the prohibitions still hold, because asserting `not
   required` is a direct statement that the member is absent. C encodes the same
   57 cells by *omitting* them from the branch, and `extension_parameters_type =
   ( * tstr => any )` then matches anything omitted. C's own preamble concedes
   it: **"Note: the extension parameter wildcard (* tstr => any) means the
   per-type parameter prohibitions in this CDDL are advisory; a prohibited
   parameter matches the wildcard. The prose and Table 1 of the draft are
   definitive."**
2. **Both lose the same two `M (1)` `mediatype` cells, by different
   mechanisms.** B keeps footnote 1's conditional — `{"if": {"required":
   ["body"]…}, "then": {"required": ["mediatype"]}}` — so the obligation
   survives as a condition on inline content. C demotes it to `? mediatype` and
   moves the obligation into a comment: `; mediatype MUST be present for inline
   content`. One relocates the `M`; the other deletes it and writes it down
   beside the hole.
3. **C does not merely fail to express `SN` — it *conflates* `SN` with `X`.**
   Omission is C's only encoding for both, so a reader reconstructing Table 1
   from the CDDL reads `disposition`'s four `SHOULD NOT`s as `MUST NOT`s. B
   keeps them distinct: `disposition` appears in **none** of the five
   prohibition lists, and is `required` in the `incomplete` branch.

`[we conclude]` this is where the expressive ceiling actually sits, and it is
lower and more uneven than "neither expresses `S`, `SN` or `-`" suggests.
**ARCH-0002 P3's *"a type is a schema"* fails *differently* depending on which
schema language you pick** — one language silently strengthens an advisory cell into a prohibition,
the other silently weakens every prohibition to advice. A reader who reconstructs
the normative content from the formal artifact gets a different specification
depending on which artifact they picked up, and neither tells them so except in a
comment. That is a worse problem than a uniform loss, because a uniform loss is
at least predictable. §4.5 below.

---

## 2. What we adapt, and how

**B1 — `critical`, with the default inverted.** `[ARCH-0002 P5]` Adopt the
*mechanism* — a list of names, inside the signed payload, that a consumer must
support or refuse — and reject the *polarity*. §4.3 below works this through, including
what P5 pays that vCon does not. Note one thing vCon got right that COSE and JOSE
did not and that we should copy: **`critical` is a top-level vCon parameter, so
it is inside the signed payload**, where COSE's `crit` (RFC 9052 §3.1) and JOSE's
`crit` live in a header. CVE-2025-59420, which `ADR-0002` §3 cites as P5's live
instance, is a header-handling bug. Putting the must-understand list in the
payload removes a whole class of it.

**B2 — the asserter index, extended to where the machine claims are.** `[P2]`
A2's `party` index is the right construct in the wrong places. Analysis is where
derived claims live and it has no party parameter at all (§4.5.1–4.5.9). **[we
conclude]** the adaptation is: every object that *adds a claim* carries a
reference to the principal who vouches for it, and under P2 that reference is a
key, not an array index into a list of telephone numbers.

**B3 — two typed edges with integrity, not one bare `supersedes`.** `[library
relations; DEC-005]` §4.2 below argues these are supersession rather than version
folding. The adaptation is in three parts. (i) **Two edges, because the direction
of information change is opposite**: `amended` is monotone growth — **"the newer
version of the vCon is a deep copy of the prior version with the amended and
additional data added to it"** (§4.1.9) — while `redacted` is subtraction, and
they are declared **"mutually exclusive"** (§4.1.8, §4.1.9). Our `supersedes` is
undifferentiated and cannot express that a successor is strictly smaller.
(ii) **The edge carries a digest**: `uuid` plus optional `url` + mandatory
`content_hash`. Our typed edges are bare ids with no integrity binding.
(iii) **The edge is inside the signed bytes**, so the successor's signer attests
to the link.

**B4 — array-order semantics declared per field, not as a global canonical
sort.** `[DEC-002 condition (5); P4]` vCon is a counterexample to any blanket
"sort set-valued arrays" profile rule, and it is worth setting out because the
`canonical-encoding` answer treats condition (5) as an encoding-layer question.
In vCon, **order is semantics in at least five distinct ways**:

| § | what order means |
|---|---|
| §4.2 | a party's identity *is* its index — **"They are distinct by the order or index in the Party Object array."** |
| §4.3.2 | **"Dialog Objects in the dialog array are in order that they were added to the vCon and cannot be reordered with out correcting the dialog indices which occur in other Objects in the vCon."** |
| §4.3.4 | **"It is implied that the first party in the dialog Object parties list, is the originator of the dialog."** |
| §4.3.4 | array position = recording channel; **"a null placeholder MUST be inserted into the parties array for the corresponding channel"** when a channel is unused |
| §4.1.8 | redaction **"SHOULD create an empty placeholder such that object array indices do not change for the rest of the elements of the array"** |

**[we conclude]** condition (5) is not a property of an encoding. Whether a
canonical sort is safe is a *per-field* fact that belongs in the schema — P3's
*representation* part — and a profile that sorted arrays globally would destroy
any document shaped like this one. That cuts both ways and it is worth saying
plainly: it does **not** weaken condition (5) for `Threshold` members, where a
set genuinely is a set; it says the rule must be declared field by field rather
than once at the encoding layer. This is one of the few findings in this record
that changes how a DEC-002 profile would have to be *written*, whichever option
wins.

**B5 — the signer's name inside the signed bytes.** `[DEC-003, DEC-005]` See C1
for the rejection. The adaptation: whatever DEC-005 selects, the identifier that
*names the issuer* must be covered by the signature. COSE_Sign1's protected
header can carry it; DSSE has no issuer field at all, which `rfc-9804`'s notes
record as an option-independent problem. vCon demonstrates the third arrangement
— name present, name unprotected — and it is the worst of the three.

**B6 — key-relative vocabulary, with the key actually present.** `[P1,
ADR-0001]` §4.4 below argues this at length. In three places vCon reaches for exactly
P1's construct and lands on a label with no defining principal: the `validation`
token (§4.2.7), the `vendor`/`product`/`schema` triple (§4.5.6–4.5.8), and the
redaction `type` (§4.1.8.1). The adaptation is simply ADR-0001's `(defining key,
local label)` pair applied where vCon wrote a bare string.

---

## 3. What we reject, and why

**C1 — `x5c`/`x5u` in the unprotected header, and X.509 as the only key
discovery.** `[R-M-01; ARCH-0001 §6]` §5.2: **"The vCon General JWS JSON
Serialization MUST include x5c or x5u in the unprotected header."** The
certificate chain is the only thing in the entire format that names the signer,
and it is normatively placed *outside* the signature. The stated motive is
operational: **"The x5c or x5u requirement makes the management and use of vCons
easier, allowing the certificate chain to be found as the vCon is moved"**
(§5.2.2). **[we conclude]** the consequence is that the signature binds the
*key* and not the *name*: a relaying party can substitute a different chain
asserting a different subject for the same public key, and no verification step
in the document detects it. Separately, ARCH-0001 §6 lists as a **forbidden
native mapping** *"X.509 certificate path validation as the native reducer"*, and
vCon's MUST makes X.509 the only key-discovery mechanism there is. **`kid` does
not appear anywhere in the document.**

A source observation that belongs here: in Appendix A.6 the example's
`protected` header decodes to `{"alg":"RS256","typ":"JWT","x5c":[…`, while the
unprotected `header` member carries `alg`, `x5c` *and* `uuid` — and the two
`x5c` chains are element-for-element identical. RFC 7515 §7.2.1, read against
the cached source, says it in one sentence: **"The Header Parameter names in the
two locations MUST be disjoint."** The example is therefore not conformant to the
JWS serialisation it cites, and it also contradicts §5.2's own normative
placement. Recorded in §6 as a defect to report, not as a position of the draft.
`[closed 2026-10-14, pass 2]` — verified against
`.cache/rfc-7515.txt`, sha256 `ecbf8467…4ae62e40`, §7.2.1; the signature itself
verifies cryptographically (RS256 over the RSA-2048 key in `x5c[0]`), so a
conforming JWS library rejects this document *before* reaching a signature that
is in fact valid.

**C2 — an unauthenticated identifier outside the envelope.** §5.2.2 and §5.3.1
put `uuid` in the JWS and JWE headers and §6.5 registers it as a new JOSE header
parameter. The reason is stated: **"This is added for convenience to not require
verification of the signed vCon to get it's UUID. When the vCon is verified, the
value of this uuid parameter SHOULD be verified against the UUID in the signed
vCon."** A `SHOULD` cross-check that exists only because the identifier was
placed where it could be lied about. We reject the construct; the requirement it
is trying to meet — route and deduplicate before verifying — is real and
`[open]` under DEC-005.

**C3 — per-object IANA parameter registries.** `[R-M-12, ADR-0001]` §6.3: **"Each
Object (i.e. dict, map, dictionary) has its own registry of parameter names."**
Eight registries of parameter names (§6.3.2–§6.3.9 — §6.3.1 is the shared
template, not a registry), plus a Dialog Type Name
registry (§6.3.4.1), a `party_event` Event Name registry (§6.3.5.1) and a vCon
Extensions Names Registry (§6.4), all mediated by Designated Experts — **eleven
new IANA registries** in one document. (§6.5 is not a twelfth: it *registers*
the `uuid` parameter into the existing JOSE **"JSON Web Signature and Encryption
Header Parameters registry"**, and its own pointer is wrong, citing **"Header
Object (Section 5.3.1)"** when §5.3.1 is the Unprotected Object and the Header
Object is §5.3.3.) This is the
global namespace at the extension point that ADR-0001 exists to refuse: *"a model
whose premise is that principals are keys inherits, at its extension points,
exactly the global namespace it rejected above"* (ARCH-0002 P1). Interchange
only, per R-I-01.

**C4 — the open-by-construction schema.** Appendix C makes every object in the
format open, by rule: `; Extension parameters MAY appear in any object (Section
2.5)` / `extension_parameters_type = ( * tstr => any )`, included in **every**
object production — vCon, Party, Dialog, Attachment, Analysis, Redacted, Amended,
Signature, Header, Unprotected, Recipient. Appendix B's JSON Schema contains no
`additionalProperties` or `unevaluatedProperties` constraint anywhere. Under P5
this is the thing to reject; it is also the structural reason §4.3 below's producer
opt-in is the *only* protection available in vCon.

**C5 — a named parameter with undefined semantics.** §4.3.1.6's legend: **"- The
parameter has no defined meaning for this type; it MAY be present but its
semantics are undefined."** Exactly one cell in Table 1 uses it — `duration` on
the `transfer` type — so the cost today is nil and the licence is general.
**[we conclude]** this is *worse* than an unknown field, because a consumer
recognises the name and will apply the meaning it has from another type. P5 as
drafted speaks to *unknown* fields and does not cover this case at all; see
§4.3 below.

**C6 — `vendor` / `product` / `schema` as a format identifier.** §4.5.6: **"The
vendor string value contains the vendor or product name of the software which
generated this analysis."** §4.5.8: **"The schema string contains a token or
label for the data format or schema for the analysis data."** Three free strings,
no registry, no resolution, no principal. Under P3 the format of a claim is a
schema with an identity; under P1 that identity is `(defining key, label)`.

**C7 — optional absence *and* null as two spellings of the same value.** §2.2:
**"Objects or arrays with no or null values MAY be excluded from the vCon."**
`MAY` makes `{"parties": []}`, `{"parties": null}` and omission all permitted
spellings of the same state. Signing opaque bytes (A4) means this costs vCon
nothing. **[we conclude]** it would cost *us* everything if we ever derived an
identifier from a structure, which P4 requires: three spellings, three digests,
one meaning.

**C8 — `alg` SHOULD be `RS256` (§5.2.2) and `A256CBC-HS512` / `RSA-OAEP`
(§5.3.1, §5.3.3).** Named for interoperability — *"to maximize
interoperability"* — not for strength. ARCH-0001 NG3 defers our algorithm suite
and nothing here should pre-empt it.

**C9 — an integrity binding that is mandatory to write and optional to read.**
Every BCP 14 obligation attaching to `content_hash` is about **carriage**:
**"Objects that refer to a file which is externally stored from the vCon MUST
have the parameters: url, content_hash"** (§2.4); **"content_hash MUST be
included if url is provided"** (§4.1.8.1); **"content_hash MUST be provided if
url is provided"** (§4.1.9.1 and twice in the CDDL). The only sentence in the
document asking anyone to *check* it is §5.1, and it is lowercase: **"After
retrieving externally referenced files, before using its content, the payload of
the HTTPS request should be verified using the signature parameter value for the
hash for the url body."** It also names a parameter that no longer exists — §7.3
records that **"'alg' and 'signature' were combined into 'content_hash'"** —
so the one verification instruction in the draft points at a field removed two
syntax versions ago. `[we conclude]` a binding nobody is required to verify is
documentation, not integrity, and under R-M-07 the obligation has to run in both
directions.

---

## 4. The four questions this record is held for

### 4.1 Can "A says B has C" express a vCon? — and does a vCon have a speaker?

**The topic's claim, tested.** `topics/artifact-statements.yaml` concludes that
*"A VCON HAS NO SPEAKER: it is signed by whoever assembled it, and that signer
appears nowhere in the data model,"* that *"vCon never distinguishes ASSEMBLED
from ASSERTED,"* and that `analysis[]` *"records vendor, product and schema,
everything except who vouches for the analysis."* Against the source, **the
second clause is wrong and the first and third survive in a sharper form.**

**What is wrong: vCon does draw the distinction, in §4.4.3 — in its own
vocabulary, not in ours.** `[pass 2: the draft's words are "provenance",
"author" and "distributed"; it uses neither "assembled" nor "asserted" anywhere
in 8,904 lines, and "provenance" occurs exactly once, in this paragraph. The
mapping below is ours.]` The Attachment Object's `party` is **"To provide
provenance for the attachment, the party index MUST be specified"** — a `MUST`,
the only mandatory contributor reference in the document — and the draft
separates the roles explicitly: **"This party is not necessarily the document's
author, but rather the party that distributed the document."** **[we conclude]**
author versus distributor is the asserted/assembled distinction under another
name. It goes further and names the
assembler as a first-class participant: **"an organization that processes or
constructs the vCon may add attachments containing information about the
conversation. The organization or entity that adds the attachment SHOULD be
represented as a Party Object."** So the vCon data model *does* have a slot for
"the entity that put this here, who is not a party to the conversation", and it
is mandatory on the one object type that uses it.

**What survives, and is stronger than the topic put it.** Three findings.

**(i) The slot exists and is absent precisely where the machine-derived claims
are.** Analysis (§4.5) has `type`, `dialog`, `attachment`, `mediatype`,
`filename`, `vendor`, `product`, `schema`, and content. **No `party`.** The same
draft that made a contributor index mandatory for a *document somebody attached*
provides none for a *transcript a machine produced*, where the attribution is to
software (§4.5.6) rather than to a principal. **[we conclude]** this is not an
oversight so much as a category error that P2 is designed to prevent: `vendor`
answers *what produced this*, and nothing in the object answers *who stands
behind it*.

**(ii) The draft states P2's form in prose and provides no field for it.** This
is the sharpest sentence in the document for our purposes, §4.1.8: **"The
assurance of the accuracy of the redaction is made by the entity that creates the
redaction which SHOULD sign the redacted version of the vCon."** Read it as P2:
*A* is "the entity that creates the redaction", *says* is "SHOULD sign", *B* is
this vCon, *C* is "the redaction is accurate". The whole form, correctly
assembled, in one sentence — and there is no `redactor` parameter, no key, no
party index, and the verb is `SHOULD`. The A exists in the prose and has no slot
in the schema. **[we conclude]** that is a better statement of the finding than
"a vCon has no speaker", because it shows the specification *knowing* it needs
the speaker and having nowhere to put it.

**(iii) At the envelope layer the signer is named but unprotected, and the name
is never joined to anything.** `x5c`/`x5u` are `MUST` (§5.2, §5.2.2) and an X.509
chain carries a subject DN — Appendix A.6 chains `grp.div.fakevcon.io` →
`div.fakevcon.io` → `fakevcon.io`. So there *is* a name. But (a) §5.2 puts it in
the **unprotected** header (C1), (b) no parameter anywhere relates it to a Party
index, to an Analysis object, or to the redaction assurance of §4.1.8, and (c)
`kid` never appears. §4.1.2 is the one place the two worlds touch, and only by
convention: the UUID's DNS input **"SHOULD be the same FQHN, or a subdomain to
allow for more distributed generation of UUIDs, as would used in the signing
certificate as they are the same domains of uniqueness."** A
domain-name coincidence, unverifiable from the document.

**And the one artifact a JSON toolchain would actually run does not reach the
signing layer at all.** Appendix B is titled `"vCon - Unsigned Form"`, carries
`"$id": "https://ietf.org/vcon/schemas/unsigned-vcon.json"`, and contains no
`payload`, `signatures`, `protected`, `header`, `x5c`, `ciphertext` or
`recipients` property anywhere in it. Appendix C's CDDL *does* cover
§5 (`signed_vcon_type`, `signature_object_type`, `signed_header_object_type`) and
makes every one of those objects open, by rule (C4). `[we conclude]` the place an
asserter would have to appear is the one place the draft ships no JSON Schema for,
and the one schema that does model it declines to close it.

**Does `validation` (§4.2.7) do any of this work? No — and the way it fails is
itself a finding.** It is a label for a *method*: **"The purpose of the
validation parameter, is to allow the validator to save a label or token which
identifies the method of identity validation used to identify the person at the
other end of the communication channel."** It names "the validator" in the
sentence and provides no field for the validator. And then: **"It is up to the
domain creating the vCon to define the set of tokens or values to be used for the
validation parameter."** That is P1's `(defining key, local label)` with the key
replaced by "the domain creating the vCon" — an actor the data model never
identifies. **[we conclude] this is ADR-0001's private-use-range argument
reproduced independently in a live specification**: *"private use gives escape
from a registry, not a namespace. Two parties independently using the same
private label collide with nothing to disambiguate them, because no principal is
attached."* vCon reaches for key-relative naming three times (B6) and gets an
unresolvable string each time, for the single reason that it has no A to make it
relative to. **P1 and P2 are not separable, and this record is the evidence.**

**Caveat, stated so the finding is not over-sold.** A Party Object can be
key-bound: `did` **"MUST be a valid DID URI that enables verifiable,
decentralized digital identity for the party"** (§4.2.6) and `stir` carries a
PASSporT **"in the JWS Compact Serialization form"** (§4.2.3). So vCon's A-slot
is not merely a name field — it is capable of holding a principal. It is simply
never connected to the signature, never mandatory, and never present on Analysis.

**How much does the signature actually bind? Less than "the A is missing"
implies.** Three obligations, read together, and all three are the draft's own
rather than inherited.

1. **The signer's name is outside the signature.** §5.2, in the draft's own
   words: **"The vCon General JWS JSON Serialization MUST include x5c or x5u in
   the unprotected header."** For `x5c`/`x5u` this needs no reading of RFC 7515
   to establish — the draft says *unprotected*, in terms — and §5.2.1/§5.2.2
   agree structurally: §5.2.1 lists `header`, `protected` and `signature` as the
   Signature Object's members, §5.2.1 then says **"The value of header is
   defined in Header Object (Section 5.2.2),"** and §5.2.2 says **"The Header
   Object for a signed vCon MUST include the alg and either the x5c or x5u
   arrays."**

   **For `alg` the draft is genuinely ambiguous, and the ambiguity is itself a
   finding.** `[verified 2026-10-14, pass 2]` No sentence anywhere places `alg`
   the way §5.2's sentence places `x5c`/`x5u`. The placement has to be inferred,
   and the two available inferences disagree. §5.2.1 binds §5.2.2's Header Object
   to the `header` member, which RFC 7515 §7.2.1 defines as **"the value JWS
   Unprotected Header"** — on that reading `alg` is required in the *unprotected*
   header. But §5.2.2's own first sentence says **"The Header Object and its
   contents are defined in section 4 of [JWS]"**, and RFC 7515 §4 is *JOSE
   Header*, which §3.2 of the same RFC defines as **"the union of the members of
   the JWS Protected Header and the JWS Unprotected Header values that are
   present"** — on that reading the obligation is satisfied by *either* location.
   §5.2.1 makes `protected` mandatory and then assigns it no content at all, so
   the draft never says what the one integrity-protected header is for. The two
   readings cannot both hold once RFC 7515 §7.2.1's disjointness requirement is
   applied, and Appendix A.6 takes a third option that §7.2.1 forbids outright:
   `alg` and `x5c` in *both*. We record the ambiguity rather than resolving it;
   the example is evidence that the draft's text did not communicate a single
   location to its own author. Note also what §5.2.2's §4 reference does *not*
   supply: RFC 7515 §4.1.1 requires only that `alg` **"MUST be present and MUST
   be understood and processed by implementations"**, and names no header.

   So `x5c`/`x5u` and the convenience `uuid` are parameters of the `header`
   member, and `alg` is somewhere the draft does not say. `[we conclude]` on
   either reading the signature binds the **key** — the chain's public
   key must verify it — and leaves unbound the **subject name** in that
   certificate and the **path to a root**. An intermediary holding a second
   certificate over the same public key, or willing to present a different
   chain, changes who a verifier believes spoke without disturbing the
   signature.
2. **The identifier a consumer routes on is designed to be read before
   verifying.** C2. §5.2.2 states the purpose — **"This is added for convenience
   to not require verification of the signed vCon to get it's UUID"** — and
   makes the reconciliation a `SHOULD`.
3. **The hash binding to external content is mandatory to write and optional to
   read.** C9. Every BCP 14 obligation on `content_hash` is about carriage. The
   only sentence that asks anyone to check it is §5.1, lowercase.

`[we conclude]` the honest statement is stronger than *"a vCon has no speaker"*,
and it is the sentence to carry forward: **a vCon's signature establishes
that someone holding a particular private key produced these bytes. Nothing
normatively binds that key to a name, to a party, to the identifier consumers
index on, or — once content is external — to the conversation the vCon is
about.** Under P2 that is not *A says B has C* with *A* blank. It is closer to
*⊥ says B-by-reference has C*, where the by-reference binding is `MUST` to
include and lowercase-should to check.

**Is this about vCon or about layering? Mostly about vCon, and the test is
whether the draft chose or deferred.** The layering counter-reading deserves a
hearing, because it is the reading that would let us off: if the thinness is
RFC 7515 and RFC 7516 doing the work, then our own design faces the identical
question wherever it defers to an envelope, and the finding is about us rather
than about vCon. On the evidence it does not hold for any of the three.
Deference looks like silence; each of these is an active choice, stated with a
keyword and a rationale.

| | deference, or choice? | the evidence |
|---|---|---|
| unprotected `x5c`/`x5u` | **choice** | RFC 7515 supplies both a protected and an unprotected header and lets the application pick. §5.2 picks, with a `MUST`, and §5.2.2 gives the operational reason: **"The x5c or x5u requirement makes the management and use of vCons easier, allowing the certificate chain to be found as the vCon is moved."** |
| the convenience `uuid` | **choice** | it is not a JOSE parameter at all until this draft makes one: §6.5 **registers** it in the JSON Web Signature and Encryption Header Parameters registry |
| unchecked `content_hash` | **choice** | `content_hash` is vCon's own construct (§2.2, §2.4.2). No referenced RFC supplies an obligation to verify external content, so the obligation was vCon's to write and it wrote a lowercase one |

`[closed 2026-10-14, pass 2]` One claim here rested, at pass 1, on a document
the library held only as a stub. It no longer does. RFC 7515 is now cached at
`.cache/rfc-7515.txt`, sha256 `ecbf8467…4ae62e40`, and §7.2.1 of it says
verbatim: **"The Header Parameter names in the two locations MUST be disjoint."**
That is what makes Appendix A.6 non-conformant, and it is now checked against the
source rather than remembered. RFC 7516 is cached alongside it,
sha256 `722cfcdd…0474a21f`; its §7.2.1 carries the same rule for three locations,
which is what A.7 breaks (§6 item 14). Everything in the three numbered findings
above is established from vCon's own text and does not depend on either.
`records/ietf/rfc-7515` and `records/ietf/rfc-7516` remain stubs as *records* —
caching a source is not ingesting it — so this closes the evidentiary gap, not
the library's own backlog item.

**The answer.** `[we conclude]` *A says B has C* can express a vCon, with one
addition and one subtraction, and the addition is larger than the topic answer
supposed. The addition: an asserter slot on every claim-bearing object — which
vCon has, mandatorily, for Attachment (§4.4.3) and lacks entirely for Analysis
(§4.5) — **plus** a binding from that slot to the key that signed, which vCon
has nowhere. The subtraction: *B* is a conversation, not bytes; see R-M-11 in §5.

The thing P2 buys that vCon cannot have is the ability to say *who vouches for
the transcript* separately from *who assembled the container*, and §5.2.3's
nested archive chain shows why that matters: JWS1 ⊂ JWS2 ⊂ JWS3, where the outer
signers are archivists re-signing before certificate expiry, and **"then the vCon
(payload in JWS1) is assumed to have valid integrity."** A reader cannot tell
"A asserts this conversation happened" from "A asserts this bundle existed on
date D", because both are spelled the same way — and after the three findings
above, cannot establish *which A* said either without trusting an unprotected
certificate chain.

**So: the topic answer should be amended, not merely confirmed.** Its middle
clause — *"vCon never distinguishes ASSEMBLED from ASSERTED"* — is contradicted
by §4.4.3, which draws exactly that distinction and uses the word *provenance*
for it. Its headline — *"a vCon has no speaker"* — is true but understates the
case: vCon has the speaker in prose (§4.1.8), has a slot for a contributor
(§4.4.3), has a name in the envelope (§5.2.2), and binds none of them to each
other or to the signature. Its `analysis[]` clause is exactly right and is the
sharpest instance.


### 4.2 Do `redacted` / `amended` map to `supersedes`, or to version folding?

**To `supersedes`, decisively — and §7 is the thing that maps to folding.**

**What the draft does.** A new vCon instance version is a *new document with a
new globally unique identity* and a typed backward reference. §4.1.2: **"All vCon
documents MUST have the uuid parameter and value set"** and the value **"MUST be
globally unique."** The examples confirm the identities differ: A.8's redacted
vCon is `01928e10-193e-8231-b9a2-279e0d16bc46` with `"redacted": {"uuid":
"01a07da8-c2bb-83e5-b9a2-279e0d16bc46", "type": "PII Redaction"}`; A.9's amended
vCon is `01a07da8-c5c1-8db4-a20f-d188127fad29` with `"amended": {"uuid":
"01a07da8-c2bb-83e5-b9a2-279e0d16bc46"}`. New id, typed edge backwards, prior
version left intact and independently signed. That is our `supersedes` relation,
and it is also `CLAUDE.md`'s rule — *"Never reuse an id … A new version of a spec
is a new record linked by `supersedes`"* — arrived at independently.

**§7 is not examples and it is not instance versioning.** An earlier extraction
of this record mis-cited §7; it is **"Non-Upward Compatible Changes to the vCon
Container"**, a three-entry migration log for the *syntax* version: 0.3.0→0.4.0
(`appended`→`amended`, `must_support`→`critical`, `session_id` string→object),
0.0.2→0.3.0 and 0.0.1→0.0.2. That is the *document line*, and it is what
`docs/scope.md` §5's folding rule is about. The draft's own §2.1 keeps the two
apart (A3). **And it then deletes the syntax version entirely**: §4.1.1 opens
**"The 'vcon' parameter is DEPRECATED as of the publication of this document as
an RFC"** and gives the reason two sentences later — **"The extension mechanism
replaces the need for schema versioning."** `[we conclude]` vCon's position is
that instance supersession needs a typed edge and syntax versioning needs no
field at all — the extension list carries it. §7 survives as a changelog for
humans.

**The two axes are named and never related.** §2.1 defines both terms (A3) and
§4.1.1 points the deprecated `vcon` parameter at §7, but nothing in the document
says what happens where they cross: an `amended` vCon whose prior instance version
was written to syntax 0.3.0 would reference a predecessor in which the very
parameter doing the referencing was spelled `appended` (§7.1), and the draft gives
no rule for reading it. `[we conclude]` the gap is ours too, and in a sharper
form: `docs/scope.md` §5 folds along the syntax axis while `supersedes` runs along
the instance axis, and no library document says which one a given relation is on.
**[open]**, §6.

**What breaks under each reading.**

*Reading it as version folding breaks on three things, and all three are
structural rather than stylistic.*

1. **Signatures.** Each instance version is independently signed, because §4.1.9
   says it must be: **"A signed or encrypted vCon cannot be modified without
   invalidating it. In these cases, to allow for adding of additional information
   a new vCon instance version MUST be created."** Folding versions into one
   record asserts a single current document; here there are *n* documents, each
   with its own signer and its own validity.
2. **Access control.** The versions are not meant to be held together. §4.1.8:
   **"If a reference to the unredacted vCon is provided in the url parameter, the
   access to that URL MUST be restricted to only those who should be allowed to
   see the identity or PII for the redacted vCon."** §5: **"The non-redacted
   version of the vCon referenced from the redacted vCon MUST be encrypted such
   that only those with permission to view the non-redacted content can decrypt
   it."** `[we conclude]` **our folding rule silently assumes a trust-uniform
   holder.** vCon's whole premise is the opposite — §4: **"A vCon may be
   constructed across several security domains"** — and the holder of the latest
   version is frequently the party *least* entitled to the earlier ones.
3. **Citability.** Under folding, a superseded version lives in
   `versions/<version>/` and has no id of its own, so it cannot be the target of
   a citation. Every vCon instance version has a globally unique UUID and is the
   target of exactly such a citation, from its successor.

**A concrete defect in the index model, found at the join between §2.2 and
§4.1.8, and it is the strongest argument in this record against index-based
references.** Redaction is required to preserve positions: **"Data which is to be
completely removed from the redacted version, that is contained in a JSON array
in the unredacted vCon, SHOULD create an empty placeholder such that object array
indices do not change for the rest of the elements of the array"** (§4.1.8). The
draft never says what an *empty placeholder* is, and the two candidates it
supplies elsewhere are an empty object — §4.2 allows **"a Party Object with no
parameters in it"** and says **"They are distinct by the order or index in the
Party Object array"** — and `null`, which §4.3.4 mandates for unused recording
channels. §2.2 then permits dropping exactly those: **"Objects or arrays with no
or null values MAY be excluded from the vCon."**

`[we conclude]` **a conforming processor may delete a conforming redactor's
placeholder, and every `dialog`, `parties`, `attachment` and `originator` index
after that position silently retargets.** A `SHOULD` to insert against a `MAY` to
remove, with no rule about precedence, in a format where position *is* identity
(B4). Two further consequences of the same `MAY`: an anonymous party, which
§4.2.5 says **"SHOULD be create for each anonymous party in the
conversation"** and which carries no parameters beyond `name`, is at risk from
the same rule; and §5.4 detects the unsigned form by **"The presence of one or
more of the following parameters … parties, dialog, analysis, attachments"**,
which the examples carry as empty arrays (`"analysis":[],"attachments":[]` in
A.4 through A.6) and §2.2 permits dropping.

This is not a reason to prefer vCon's supersession model less. It is a reason to
prefer **referencing by identity rather than by position**: R-M-11's digest or
description mode over an array index. An index is a reference whose target can be
changed by an edit that touches neither the reference nor the referent, and it is
the direct cost of the "domain of discourse as one indexed document" shape §4.4
below describes. **[open]**, §6.

*Reading it as `supersedes` breaks on two things, both ours and both fixable.*

1. **One edge is not enough.** `amended` and `redacted` are **"mutually
   exclusive"** and have opposite information direction (B3). Our vocabulary —
   `supersedes`, `updates`, `cited_by`, `see_also`, `implements_concept`,
   `contradicts`, `part_of` — has nothing that says *the successor contains
   strictly less*. A reader who follows `supersedes` to a redacted vCon and
   concludes the predecessor is obsolete has it backwards: the predecessor is
   authoritative and merely restricted.
2. **Our edges carry no integrity.** vCon's carry `content_hash` (A6, B3). A bare
   id can retarget; a digest cannot.

**The answer.** `[we conclude]` `redacted` and `amended` are `supersedes`, with a
sign and a digest; §7 is version folding, and vCon has concluded that the folded
thing needs no identifier at all. The one amendment this suggests for
`docs/scope.md` §5 is that **the folding rule should state its assumption** —
that all versions of a line are equally disclosable to whoever holds the record.
For our own sources that is true. It is not a property of version folding in
general, and vCon is the counterexample.

### 4.3 Does `critical` match P5, and did they get something right we have not?

**The mechanism, exactly.** Two parameters, two different verbs.

- §4.1.3 `extensions`, **producer-side `SHOULD`**: **"The extensions parameter
  SHOULD contain the list of names of all vCon extensions for any parameters used
  that are not defined in this core vCon schema document."**
- §4.1.4 `critical`, **producer-side `MUST`, consumer-side `MUST NOT`**:
  **"Implementations that include extensions which are incompatible with the core
  vCon schema MUST list the names of those extensions in the critical
  parameter"**; and **"An implementation that does not recognize or support the
  extensions listed in the critical parameter MUST NOT attempt to process or
  operate on the vCon, except to reject it or report unsupported content."**
- §2.5 repeats it and adds the classification: *Compatible* extensions
  **"introduce additional data or fields without altering the meaning or
  structure of existing elements"**; *Incompatible* ones **"modify existing
  semantics or schema definitions in ways that render a vCon incompatible with
  implementations that do not support the extension."**

**Where the mechanism came from, which is evidence about what it is for.** §7.1
records the rename, and §7 is the only place the old spelling survives:

> The "must_support" parameter was renamed to "critical" to be consistent with
> other IETF JSON schema extension mechanisms.

 `[we conclude]` the two names describe different
things. *must_support* is a statement about the **document** — this vCon requires
support — and reads naturally as producer opt-in. *crit* is the JOSE and COSE
spelling (RFC 7515 §4.1.11, RFC 9052 §3.1), and the WG adopted the family for
consistency. **The polarity was inherited with the name.** That matters for §4.3(a)
below: the one thing vCon has that JOSE and COSE do not — a sense that criticality
depends on what the consumer is doing — survives in §2.5's prose and did not
survive into the parameter, and the rename is when that happened.

So the brief's framing is confirmed: **the consumer's obligation to reject is
conditional on the producer having declared.** The schema cannot help — C4 makes
every object open by construction — so there is no residual signal.

**What happens when a producer forgets. Four distinct failures.**

1. **Forgets `extensions` (a `SHOULD`).** Nothing happens, visibly. The consumer
   has no inventory of non-core parameters, and `* tstr => any` means an
   unexpected key is indistinguishable from a typo, a stale field or an
   injection.
2. **Forgets `critical` (a `MUST`).** A consumer that does not support a
   semantics-changing extension processes the vCon as though core semantics held.
   **The draft itself works the catastrophic case**: §2.5, **"a redactor must be
   aware of the implications of all parameters in the vCon to be sure to redact
   all of the objective information."** A redactor that walks past an unknown
   PII-bearing field emits a vCon labelled redacted that is not. The redaction
   machinery of §4.1.8, §5 and the whole privacy half of the document is defeated
   by one forgotten array entry, and **no consumer-side check in the document can
   detect the omission.**
3. **Mis-classifies.** §2.5 concedes the judgement is soft: **"The question of
   Compatible vs Incompatible is a little subjective."** The classification is
   made by the party with the least incentive to be conservative, since declaring
   `critical` shrinks your audience.
4. **Does everything right, and a consumer still misreads a core field.** C5's
   `-` cell: a *known* parameter, present, with **"no defined meaning for this
   type."** Nothing is unknown, nothing is an extension, `critical` has no role,
   and a consumer that applies the parameter's meaning-from-another-type is
   wrong. **P5 does not cover this case** — P5 speaks to *"an unknown field in a
   signed payload"*, and this field is known.

**What P5 fixes, stated precisely.** ARCH-0002 P5: *"The default is
must-understand; skippability is opt-in and explicit, never the other way
round."* And, a paragraph later: *"We invert the default so that forgetting is
safe: unknown is critical unless declared otherwise."* Against failure 2, this
is simply right and the draft agrees in the only sentence where it drops the
normative register: **"However the redactor perhaps should reject vCons with
any extension that it does not support."** The draft identifies the exact
consumer class for which producer opt-in is unsafe, and declines to make a
requirement of it. Lowercase "perhaps should", in a document carrying 216 BCP
14 keywords (`bin/bcp14-count` against the pinned digest, 2026-10-13).

**And now the part that is inconvenient for us. Two things vCon has that P5 does
not, and one cost P5 pays that vCon does not.**

**(a) vCon knows that criticality is a property of the consumer's *job*, not of
the field.** §2.5: **"A transcriber for vCon can be fairly tolerant of changes
adding new parameters or objects to a vCon. On the other hand, a redactor must be
aware of the implications of all parameters in the vCon to be sure to redact all
of the objective information. In these cases a transcriber will likely only need
to look at the critical extensions."** The same
unknown field is harmless to a transcriber and catastrophic to a redactor. **P5
has one global default and no consumer-role axis at all.** `[we conclude]` under
P5 as drafted, a pure signature-checking relay, an archival store or a transport
proxy must reject payloads containing fields it has no reason to care about —
because "unknown is critical" does not ask *critical to whom*. That is a real
cost P5 pays and vCon does not, and the axis vCon names is the one P5 is missing.

**(b) vCon pushes the work onto the party who has the knowledge, at
specification time.** A1's extension-document contract requires the *extension
author* to enumerate the incompatibilities and state, per incompatibility, which
processing is affected and what a non-supporting implementation must do. P5
pushes the work onto every *consumer*, at runtime, with no structured input to
reason from. `[we conclude]` the two are complementary, not alternatives, and
adopting A1 alongside B1 would give us the thing neither design has alone: an
inverted default *plus* a machine-readable statement of who is affected.

**(c) Inverting the default makes every additive change a flag day.** Under
vCon, a *Compatible* extension deploys gradually — **"Wherever feasible,
extensions SHOULD be designed as Compatible to preserve compatibility with
existing implementations"** — and old consumers keep working. Under P5, nothing
may be added to a signed payload without breaking every existing verifier.
`[we conclude]` our answer is presumably P4: the domain of discourse changes, so
its hash changes, so the disagreement is *visible* rather than silent — which is
the right failure mode but means **every additive change mints a new domain
identity.** `ADR-0002` §4 already records that P4 is held and that holding it now
costs more than it did; this is a second cost of *accepting* it that we have not
priced. **[open]**, §6.

**The answer.** `[we conclude]` `critical` is P5's mechanism with the polarity
reversed, and on the central question — what happens when the producer says
nothing — P5 is right and vCon's own §2.5 half-admits it. But vCon is right about
two things we have not written down: criticality is relative to a consumer role,
and the obligation to analyse belongs to the extension author at specification
time. Adopt the inversion; import the role axis and the extension contract with
it.

### 4.4 Would a vCon be a domain of discourse (P4) or a single type (P3)?

**A domain of discourse, argued from the structure — with one difference that
costs P4 something.**

**The structure.** (i) **Eight object types with independent schemas**, one
IANA parameter registry each: vCon,
Redacted (§4.1.8.1), Amended (§4.1.9.1), Party (§4.2), Dialog (§4.3),
Party_History (§4.3.13.1), Attachment (§4.4), Analysis (§4.5), plus the
envelope-level Signature, Header, Unprotected and Recipient objects of §5.2–§5.3,
and the `SessionId` and `ContentHash` value types of §2.2. IANA treats each as a
separate namespace: §6.3, **"Each Object (i.e. dict, map, dictionary) has its own
registry of parameter names."** Eight parameter registries (§6.3.2–§6.3.9) plus
two value registries (§6.3.4.1, §6.3.5.1). **A vCon is not one schema; it is a
published set of them.**

(ii) **The objects are meaningless apart.** Every cross-reference is an array
index resolved *within one vCon instance*: Dialog→parties, Dialog→originator,
Analysis→dialog, Analysis→attachment, Attachment→party, Attachment→dialog,
Party_History→party, transfer→target_dialog. Lift an Analysis Object out of its
vCon and `"dialog": 0` means nothing. That is P4's first argument verbatim:
*"Types are not independent. One references another, constrains another … Hashing
them separately lets a consumer assemble a combination the author never published
or checked."* B4's five order rules are the same point from the other side — the
*integrity of the set* is what makes the references denote.

(iii) **Three container forms over one content model** (§3: unsigned, signed,
encrypted; §5.4 distinguishes them by witness parameters), which is an envelope
question, not a typing one. The unsigned form exists for a reason worth noting:
**"The unsigned form of the top level vCon object is necessary as in many cases,
a vCon will be partially constructed and in process as conversation data is
collected"** (§4).

**So: not a single type.** P3's *"a type is a schema"* describes a Party Object
or a Dialog Object. It does not describe a vCon, because a vCon is the *set* plus
the integrity envelope over it plus the reference closure. That is P4's
definition — *"a set of the schemas in P3, serialized in a form that can be
reliably and repeatably hashed"* — with the hash swapped for a signature.

**The difference, and it is a cost P4 pays that vCon does not.** P4 says *"That
hash identifies the set."* vCon's identity is an **allocated** UUID, not a
derived digest: §4.1.2, a UUIDv8 whose **"rand_b/custom_c is generated from the
high 62 bits of the SHA-1 hash of the FQHN string"** — a hash of the *issuer's
domain name*, plus a v7 timestamp. The only hash-as-identity in the document is
`content_hash` over *external* bytes (§2.4.2).

`[we conclude]` **the reason is §4's unsigned form, and it generalises to us.
A hash-identified object cannot be named until it is finished.** vCon's core use
case is an object under construction across hours and across security domains —
metadata first, then dialog, then analysis from a SaaS transcriber — and every
stage needs a stable handle. Hash-as-identity makes the handle change at every
write. P4's alternative is to identify only the *published* domain, which is
right for a vocabulary and wrong for anything that accretes; and ARCH-0002 P4's
own open question — *"is a domain of discourse itself a statement by a key … or
a bare hashed artifact that any key may cite?"* — is exactly this question. vCon
answers it the first way (the set is signed) and then puts the signer's name
outside the signature (C1), so it gets neither property cleanly.

This is not an argument against P4. It is a constraint P4 has not stated: **hash
identity and in-progress construction are incompatible, and something in our
model has to say which objects are allowed to be unfinished.** `[open]`, §6.

### 4.5 Which bar does each answer rest on? — and what that says about P3

The four answers above quote the draft at two very different strengths, and the
difference is itself the record's main finding about ARCH-0002 P3.

**The ratio.** `SHOULD` outnumbers `MUST` **97 to 65** across the document and
**49 to 32** inside §4, the data model (counted with `bin/bcp14-count`'s keyword
set over the pinned digest, excluding the §2 BCP 14 boilerplate; 216 keywords in
total by the same count). Most of the container's shape is SHOULD-level:
`parties` on a recording, `start`, the Dialog and Attachment and Analysis
bodies, the `transfer` role parameters, the `extensions` list itself (§4.1.3),
and the `redacted` and `amended` back-references (§4.1.8, §4.1.9) are all
`SHOULD`. Only `uuid` (§4.1.2), `created_at` (§4.1.5), `critical` (§4.1.4),
`content_hash`-with-`url` (§2.4), `encoding`-with-`body` (§2.3.2), the
JWS-before-JWE ordering (§5.3), `x5c`/`x5u` (§5.2) and the Attachment `party`
index (§4.4.3) are `MUST`.

**And the schemas stop exactly at that line.** Appendix B's closing comment says
it without euphemism: **"At least one of the parties, dialog, analysis or
attachments parameters SHOULD be present (RFCXXXX Section 4). SHOULD-level
statements are not enforced by this schema."** Its `required` list at the root is
two entries — `["uuid", "created_at"]`. A7 shows both artifacts reproduce Table
1's `M` and `X` cells and demote `S`, `SN` and `-` to an optional marker plus a
comment — **and that they do it differently from each other**, B's 57
prohibitions biting while C's 57 are advisory by its own admission, C collapsing
`SN` into `X` where B keeps them apart. And both are **informational**,
subordinate to prose that is **"the definitive definition"** (A5).

**[we conclude] this is the sharpest evidence in the library against P3 as
stated, and for P3 as intended.** ARCH-0002 P3 says *"A type is not a bare
label. It is a **schema**."* In vCon a type is emphatically **not** its schema:
the schema is a non-normative rendering of prose that governs, it enforces two
required fields at the root, and three of the six applicability levels it is
asked to carry have no expression in either JSON Schema or CDDL — **and the
three that survive do not survive identically**, so which formal artifact you
read decides what the type means. P3's answer is
available and it is P3's own: the *constraints on usage* and *semantic
descriptions* parts exist precisely because representation alone cannot carry
this material. **But P3 then owes a mechanism those parts can be *checked* by,
and it does not have one.** A1's extension-document contract is the closest thing
anyone in this record has to that mechanism, and it is prose with a required
table of contents. `[open]`, §6.

**Which bar each answer rests on.**

| § | question | rests on | strength |
|---|---|---|---|
| 4.1 | the missing asserter | **MUST** — §4.4.3's `party` index is a `MUST`, and its absence from §4.5 is total, not weak | the finding is at full strength; the Attachment counter-example is the document's own strongest obligation |
| 4.1 | the signer outside the signature | **MUST** — §5.2's unprotected-header placement | full strength |
| 4.1 | the signature binds the key and nothing else | **MUST on two legs, lowercase on the third** — §5.2 and §6.5 are `MUST`-level; the `content_hash` check (C9) is lowercase *should* | the two `MUST` legs carry the finding; the third makes it worse, not load-bearing |
| 4.2 | index references are fragile | **`SHOULD` against `MAY`** — §4.1.8 placeholders versus §2.2 exclusion | a real defect, but it is a conflict between two weak verbs, so report it as a specification gap rather than a violation |
| 4.2 | `redacted`/`amended` are supersession | **mixed** — the *references* are `SHOULD` (§4.1.8, §4.1.9.1), the *new-document rule* is `MUST` (§4.1.9), the new `uuid` is `MUST` (§4.1.2) | the structural claim holds at MUST level; the *link* is only ever a SHOULD, so a vCon may supersede with no edge at all — which makes it weaker evidence for typed edges than it first appears, and is worth recording |
| 4.3 | `critical` is producer opt-in | **MUST on both sides** (§4.1.4, §2.5) | full strength; this is the document's firmest mechanism |
| 4.3 | the consumer-role axis | **non-normative** — §2.5's *"the redactor perhaps should reject"* is the only statement of it | the insight is real and the draft declined to require it; cite it as a design observation, never as a requirement |
| 4.4 | a vCon is a domain of discourse | **structural, not keyword-bearing** — nine object registries (§6.3), index references, §4's three forms | rests on structure and on IANA layout, so the SHOULD/MUST ratio does not touch it |
| 4.4 | allocated rather than derived identity | **MUST** (§4.1.2, globally unique `uuid`) with a `SHOULD` on the generation method | full strength on the fact, weak on the method |

`[we conclude]` one answer changes under this lens. §4.2's case for typed edges
is strong on *what a successor is* and weak on *whether the edge exists*: **"A
redacted vCon SHOULD provide a reference to the unredacted or prior, less
redacted, vCon instance version of itself"** (§4.1.8), and the Redacted Object's
`uuid` may be absent outright — **"The absence of a value for uuid indicates that
the less redacted version of this vCon is not available or does not exist"**
(§4.1.8.1). So vCon permits an orphan successor, and our `supersedes` is a
stronger construct than the thing it is being validated against. That is a point
*for* our relation vocabulary, arrived at by looking for a point against it.

**And a caution about reading that `uuid` at all, which generalises past this
one field.** `[pass 2, 2026-10-14]` §4.1.8.1 declares the parameter bare — `*
uuid: "String"` — and §2.2 supplies a default that makes a bare declaration
binding: **"All parameters are assumed to be mandatory unless otherwise
noted."** So the Redacted Object's `uuid` is mandatory by the default rule and
optional by the sentence quoted above, and the two readings cannot both hold.
**The same collision occurs again at §4.3.2, which is what makes it a class
rather than a slip.** `start` is declared bare at source line 1701 — `* start:
"Date"` — while §4.3.2's prose says **"The start parameter SHOULD be present
unless it is not known"** and **"The start parameter is optional for the
"transfer" type Dialog Object as it may not always be known"**, and Table 1
gives it `S` on four types and `O` on `transfer`. Prose and table agree with
each other; the declaration contradicts both. The author plainly knows the
notation — of the **115** bullet parameter declarations in §§1–7, **52** carry
an explicit `(optional…)` and six more carry another parenthetical such as
`(SHOULD be provided)` or `(required for incomplete type Dialog Object)`,
§4.1.9.1's `uuid` among them at **"(optional if external reference
provided)"** — so the omission is the defect, not the convention. But that
leaves **57 bare declarations**, every one of them mandatory under §2.2 unless
some sentence elsewhere says otherwise, and the two cases above show that the
sentence elsewhere is where the real obligation lives. `[we conclude]` **§2.2's
mandatory-by-default rule is systematically unreliable in this document, and a
reader cannot tell a deliberately mandatory parameter from a forgotten
marker without reading the prose for all 57.** The lesson for us is narrow and sharp: *a default that fires on
absence needs every exception written down, and prose is the wrong place to keep
the exceptions* — which is A7's finding arriving from the other direction.
**[open]**, §6.

---

## 5. Mapping to our decisions

| Ours | What this document contributes |
|---|---|
| **DEC-002** (native encoding) | **Evidence that the decisive axis may not be the one MD-3 narrowed on.** See below. |
| **MD-3** (option 5: reduced CBOR, no IANA tags, COSE export only) | Supports the *no-registry* half (C3 is the counterexample); **cuts against the premise that JSON forces canonicalisation** (A4); supplies a worked example of one schema over two serialisations (A5). |
| **DEC-005** (envelope for `ArtifactStatement`) | `bears_on` in `record.yaml`. vCon is the JOSE arm of the same choice, and §4.1's three-legged finding is the whole of what it has to say: the must-understand list belongs **inside** the signed payload (B1); the issuer's name must be **inside** it too (C1); whatever identifier a consumer may read before verifying must be designed rather than bolted on (C2); and an integrity binding needs an obligation to check it, not only to carry it (C9). Whichever of DSSE or COSE_Sign1 DEC-005 selects, these are four acceptance criteria it can be scored against. |
| **DEC-003** (issuer/subject identifiers on the wire) | A negative result. vCon has no `kid`, no key thumbprint, no raw key — identity is an X.509 chain in an unprotected header (C1), and the only link to the data model is the FQHN convention of §4.1.2. |
| **R-M-11** (`ArtifactId`: digest / locator / description) | **The one mode vCon needs is the one R-M-11 does not have.** For external files, A6 implements digest + non-authoritative locator exactly. For the vCon itself, *B* is a **conversation** — an event, not bytes — and vCon identifies it with an allocated UUID, which is neither a digest nor a locator nor a canonical digest of a structured description. `summary.md` already states this; the source confirms it. `[open]` whether R-M-11 needs an allocated-name mode or whether an event subject must be pushed into `description` mode, which drags DEC-002 onto the semantic path exactly as P4 says. |
| **R-M-07** (a content digest is bound in all cases) | Satisfied **in carriage** for external content, §2.4 and §2.4.2 — and not in verification (C9). The lesson for R-M-07 is that "a digest SHALL be bound" needs a companion obligation to *check* it, or it states a formatting rule. |
| **R-O-05** (*sign the bytes; no canonicalization during verification*) | **The strongest confirmation in the library, from the least expected direction.** A4. |
| **R-O-03** (*canonicalization cited, not invented*) | Moot — there is no canonicalisation to cite. Worth recording as the limiting case: a format can be signed with no canonicalisation story at all, provided it never re-derives. |
| **R-M-12 / ADR-0001 / P1** | C3 is the pattern ADR-0001 refuses (eleven new registries). §4.1 is the richer finding: vCon reaches for key-relative vocabulary three times and gets `(⊥, label)` each time, because it has no A. **P1 without P2 does not work**, demonstrated rather than argued. |
| **ARCH-0002 P2** (*A says B has C*) | §4.1. The topic's claim survives in a sharper form; its middle clause is wrong. §4.4.3 draws that distinction in its own vocabulary — author versus distributor — §4.1.8 states P2's whole form in prose, and the schema provides no slot for the A in either place. |
| **ARCH-0002 P3** (*a type is a schema*) | **The hardest row, and §4.5 is the argument.** A1 supplies the content of P3's *constraints on usage* field and A7 the shape of its *representation* field; C6 is the failure mode when a format identifier is not a schema. But in vCon a type is **not** its schema: both formal artifacts are *informational* and subordinate to prose that is **"the definitive definition"**, `SHOULD` outnumbers `MUST` 97 to 65, and three of Table 1's six applicability levels have no expression in JSON Schema or CDDL — unevenly, so the same table read through the JSON Schema and read through the CDDL yields two different specifications (A7). P3 needs a way for its non-representational parts to be **checked**, and neither it nor this record has one. |
| **ARCH-0002 P4** (hash-identified schema set) | §4.4. vCon independently reproduces P4's structure and P4's own argument for it, and declines hash identity for a reason P4 has not written down: an object under construction cannot be named by its hash. |
| **ARCH-0002 P5** (validity checked, unknown rejected) | §4.3. P5 is right on polarity and incomplete on two axes vCon covers. C5 is a case P5 does not reach at all. |
| **ARCH-0002 P6** (*a name is an attested string*) | §4.2.7 `validation` is a name that is **not** attested — a free token whose vocabulary belongs to an unnamed domain. The contrapositive of P6, in the wild. |
| **R-I-01 / interchange** | Everything in C1–C3 is interchange-side and documented lossy. |
| **DEC-004** (tag language) | Untouched. |

### DEC-002 and MD-3 — what this document shows, including the inconvenient part

The `extract` skill requires MD-3 to be addressed explicitly for COSE / CBOR /
signing-envelope documents, **and to record where the source cuts against it.**
vCon is a signing-envelope document (JWS/JWE), so MD-3 applies; it is not CBOR,
so there is no header-by-header mapping to give. Four findings, two of which are
uncomfortable.

**1. The canonicalisation problem is created by re-derivation, not by JSON.**
`[we conclude, and it is the finding of this record for DEC-002]` The
`canonical-encoding` conditions (1) injectivity, (2) rejection of non-canonical
input and (3) no canonicalisation at verification are **all vacuous for vCon**,
because the signed object is a byte string the producer handed to JWS and the
verifier never reconstructs it (A4). vCon is JSON, is signed, is implemented, and
has no canonical form — one occurrence of the word "canonical" in 8,904 lines,
and that one about external content.

This cuts against the implicit framing that option 3's problems are JSON's
problems. They are **RFC 8785's** problems, and RFC 8785 is a choice you make
only if you want to sign a *structure* rather than *bytes*. On the evidence of
this record, the DEC-002 axis that decides conditions (1)–(3) is
**re-derive versus don't**, and it is orthogonal to JSON-versus-CBOR. MD-3
narrowed on the second axis. `[open]`, §6.

**2. And the price of not re-deriving is high, and visible here.** Because the
payload is an opaque blob: no selective disclosure, no partial verification, no
in-place amendment. §4.1.9 states the consequence as a `MUST` — **"A signed or
encrypted vCon cannot be modified without invalidating it. In these cases, to
allow for adding of additional information a new vCon instance version MUST be
created."** The entire `redacted` / `amended` machinery, the mandatory
JWS-then-JWE ordering (§5.3: **"A vCon MUST be signed first using JWS as
defined in Signed Form of vCon Object (Section 5.2), then encrypted using JWE
as opposed to just encrypted with integrity protection"**), and the nested-JWS
archive chain of §5.2.3 exist because of this one property. If we take R-O-05's
opaque payload — and we should — we inherit every one of those costs, and
`ArtifactStatement` acquires the same new-document-per-change discipline. That
is not an argument against R-O-05. It is a bill we have not itemised.

**3. Library availability is a DEC-002 driver and vCon is one data point for
JSON.** §5 gives the reasoning in full: **"This document specifies the JSON
format for vCons. So it seemed the logical solution for signing vCons, is JOSE
[JWS] JSON Serialization and likewise for encrypting vCons is JOSE [JWE] JSON
Serialization. The solutions are well documents, implementations are readily
available and tested."** And §3: **"The selection of the JSON format enables
interchange between application and lower layers of the network stack."** One
working group's judgement, recorded without weighting — the mirror image of
`rfc-9804`'s finding that option 1's implementations are a short list serving
GnuPG and RNP.

**4. Where it supports MD-3.** C3 is a twelve-registry namespace, Designated
Experts and all — a live demonstration of the cost ADR-0001 predicts, and an
argument for MD-3's "no IANA tags" half. A5 shows MD-3's "YAML is the human form
with a canonical one-way mapping" is checkable by a single CDDL over both forms,
which is more than MD-3 currently asserts. **Nothing here reopens MD-3's
no-registry half; finding 1 reopens the question of what MD-3 was choosing
between.**

---

## 6. Open questions

1. **Is the decisive DEC-002 axis re-derive-versus-don't rather than
   JSON-versus-CBOR?** §5 finding 1. If the signed bytes are never
   reconstructed, conditions (1)–(3) are vacuous under *every* option, and
   DEC-002 collapses to the drivers it names — library availability, SCITT
   alignment, SPKI fidelity, human debug — plus conditions (5) and (6), which are
   semantic-layer and P4-conditional. The `canonical-encoding` answer and
   `ADR-0002` §4 both treat (5) and (6) as the P4-dependent pair; this record
   says the other four may be envelope-dependent rather than encoding-dependent.
   **Resolving this is cheap and it should be done before the Oct 28 D5 package.**
2. **What does R-M-11 do with a subject that is an event?** §5's R-M-11 row. A
   conversation is not bytes; vCon allocates a UUID. Either R-M-11 gains an
   allocated-name mode — with the cost that an allocated name is not
   self-verifying — or event subjects go through `description` mode, which puts
   canonical serialisation on the semantic path exactly as P4 warns. This is the
   one question in this file that `summary.md`'s `bears_on: R-M-11` already
   anticipated and nothing has answered.
3. **Does P5 need a consumer-role axis?** §4.3(a). vCon's transcriber/redactor
   distinction is real and P5 has no vocabulary for it. If P5 stays
   role-blind, a signature-checking relay must reject payloads it has no stake
   in. `mofn#72` is already amending P5 for non-canonical serialisation of known
   content; if a second clause is coming, this is the time to ask whether a third
   is needed. **Relevant to `ADR-0002` §6's sequencing recommendation.**
4. **Does P5 cover a known field with undefined semantics?** C5 and §4.3 failure
   4. As drafted it speaks to *unknown* fields. §4.3.1.6's `-` cell is a known
   name whose meaning is undefined in context, which a consumer will fill in from
   another context. Either P5 extends, or something in P3 forbids declaring a
   field's semantics undefined.
5. **What does P5's inverted default cost in deployment, and does P4 pay it?**
   §4.3(c). Under P5 no field may be added to a signed payload without breaking
   every existing verifier, so additive evolution means minting a new domain of
   discourse per change. `ADR-0002` §4 prices P4's *deferral*; nobody has priced
   its *acceptance* against P5.
6. **Can an object under construction have a hash identity?** §4.4. P4 says the
   hash identifies the set; vCon needs a handle before the set is complete.
   Either P4 applies only to published vocabularies, or our model needs an
   explicit notion of a draft object that is not yet nameable.
7. **Does `docs/scope.md` §5's folding rule assume a trust-uniform holder?**
   §4.2. For our sources it is true and nothing needs to change. It should be
   stated, because the rule is written as though it were general and vCon is the
   counterexample.
8. **Does P3 have a way to check the parts of a schema that are not
   representation?** §4.5. vCon's answer is "no": the schema is informational,
   the prose governs, and the `S` / `SN` / `-` levels of Table 1 have no formal
   expression. P3 claims a type *is* a schema; on this evidence a type is a
   schema plus a document, and the document is where the load is. A1's
   extension-document contract is the nearest thing to a mechanism and it is a
   required table of contents. If P3 is accepted without this, we inherit vCon's
   position while believing we have improved on it.
9. **Which axis is a library `supersedes` edge on?** §4.2. vCon has two
   versioning axes and relates them nowhere; we have the same two —
   `docs/scope.md` §5 folds along the syntax axis, `supersedes` runs along the
   instance axis — and no library document says which. The RFC-obsoletes case
   named in §5 is the instance axis; a `-11`→`-18` draft series is the syntax
   axis; a C2PA 2.2→2.4 line is arguably both.
10. **Should references inside a signed structure be positional at all?** §4.2.
    vCon's index model is defeated by a conforming processor applying §2.2 to a
    conforming redactor's placeholder. If a domain of discourse is one indexed
    document (§4.4), we inherit the shape; if its members are referenced by
    digest or by key-relative name, we do not. This is a concrete design
    question for WP1 and it has an answer, which is more than most of this list.
11. **Source defect — the only verification instruction names a deleted
    parameter.** §5.1: **"the payload of the HTTPS request should be verified
    using the signature parameter value for the hash for the url body."** §7.3
    records that **"'alg' and 'signature' were combined into 'content_hash'"**,
    so there has been no `signature` parameter on an external reference since
    syntax version 0.0.2. Same issue tracker as items 12 and 13.
12. **Source defect — Appendix A.6 duplicates `alg` and `x5c` across the protected
   and unprotected headers.** The `protected` member decodes to
   `{"alg":"RS256","typ":"JWT","x5c":[…`, and the `header` member carries `alg`,
   `x5c` and `uuid`. RFC 7515 §7.2.1 requires the union to be disjoint. It also
   contradicts §5.2's own placement of `x5c`/`x5u` in the *unprotected* header —
   which suggests the implementation that generated the examples did not follow
   §5.2. **Verified against the source** `[pass 2, 2026-10-14]`: RFC 7515
   §7.2.1, `.cache/rfc-7515.txt` sha256 `ecbf8467…4ae62e40`, reads **"The Header
   Parameter names in the two locations MUST be disjoint."** The duplicated
   values are equal — the two `x5c` chains match element for element — so the
   defect is structural, not a disagreement about content. Nothing in §4.1
   depends on it. Worth an issue on
   `github.com/ietf-wg-vcon/draft-ietf-vcon-vcon-core`; recorded here because the
   example is a fixture in `distilled/examples/` and a conforming JWS library
   will reject it **before** checking a signature that, verified independently
   at pass 2, is cryptographically valid.
13. **Source defect — the `ContentHash` definition carries an unresolvable
   reference.** §2.2 copies text from STIR PASSporT, noting **"The relevant text
   is copied here for convenience and to remove the normative dependency"**, and
   the copied text ends: **"The subsequent characters are the Base64Url encoded
   (see Section 2 [JWS]) digest of a canonicalized and concatenated string or
   binary data based on the JSON pointer referenced elements of "rcd" claim or
   the URI referenced content contained in the claim."** There is no `rcd`
   claim in vCon. The one sentence in the document
   that uses the word *canonicalized* defines it against a field that does not
   exist. Same issue tracker.
14. **Source defect — §5.3's member list is incomplete, and Appendix A.7 carries
    `enc` in all three JWE header locations.** `[pass 2, 2026-10-14]` Two defects
    in one object, the second the JWE twin of item 12 and worse by one location.

    *The list.* §5.3 enumerates five top-level members — `unprotected`,
    `recipients`, `iv`, `ciphertext`, `tag` — and Appendix C's
    `encrypted_vcon_type` repeats the same five. But §5.3 says the encrypted form
    **"takes the General JWE JSON Serialization Syntax form as defined in section
    7.2.1 of [JWE]"**, and RFC 7516 §7.2.1 defines `protected` as a member of
    exactly that serialization: **"The 'protected' member MUST be present and
    contain the value BASE64URL(UTF8(JWE Protected Header)) when the JWE Protected
    Header value is non-empty; otherwise, it MUST be absent."** A.7's JWE Protected
    Header is non-empty, so `protected` is **required** there by the reference
    §5.3 invokes. **The example is right and the specification text is
    incomplete** — a validator built from the §5.3 list rejects the document's own
    example, and a validator built from the CDDL admits `protected` only through
    the `extension_parameters_type` catch-all, i.e. as an unregistered extension
    rather than as the core JOSE member it is. (`aad`, also defined by RFC 7516
    §7.2.1, is omitted from §5.3 as well.) The one header that is integrity
    protected is the one the section does not name.

    *The collision.* A.7's `protected` member decodes to
    `{"alg":"RSA-OAEP","enc":"A256CBC-HS512"}`, its shared `unprotected` object
    carries `cty`, `enc` and `uuid`, and `recipients[0].header` carries `enc`
    alone. RFC 7516 §7.2.1 — `.cache/rfc-7516.txt`, sha256
    `722cfcdd…0474a21f` — says **"The Header Parameter names in the three
    locations MUST be disjoint."** All three values agree, so again the defect is
    structural. Two further deviations in the same object: §5.3.3 defines `alg`
    as the Recipient Header Object's one member and the example's recipient
    header has no `alg` at all, which makes A.7 the only example in the appendix
    refused by the draft's **own** CDDL rather than by its prose; and
    `unprotected.cty` is `application/vcon+json`, which §5.3.1 does not permit
    (**"SHOULD be either "application/vcon" or "application/vcon+gzip""**) and
    which this document registers nowhere. Note the shared cause with item 12:
    the draft says which header a JOSE parameter goes in and never says it must
    then be *absent* from the others. Same issue tracker.
15. **Specification ambiguity — §5.2.2 does not determine where `alg` goes.**
    `[pass 2, 2026-10-14]` Recorded as an ambiguity, not resolved in either
    direction; §4.1 finding 1 sets out the two readings. In short: §5.2.1 binds
    §5.2.2's "Header Object" to the `header` member, which RFC 7515 §7.2.1 makes
    the *unprotected* header, while §5.2.2's own first sentence binds it to RFC
    7515 §4, which is the *JOSE Header* — the union of both. §5.2 disambiguates
    `x5c`/`x5u` explicitly and says nothing about `alg`; §5.2.1 makes `protected`
    mandatory and gives it no content. Item 12 is the consequence: the draft's
    own example resolves the ambiguity by writing `alg` twice. The fix is one
    sentence in §5.2.2 naming the location, plus a statement that the two header
    locations must not repeat a name. Same issue tracker.
16. **Source defect — §2.2's mandatory-by-default rule contradicts the prose in
    at least two places, and there is no way to tell how many more.**
    `[pass 2, 2026-10-14]` §2.2: **"All parameters are assumed to be mandatory
    unless otherwise noted."** §4.1.8.1 declares the Redacted Object's `uuid`
    bare and then gives its *absence* a defined meaning — **"The absence of a
    value for uuid indicates that the less redacted version of this vCon is not
    available or does not exist"** — which a mandatory parameter cannot have.
    §4.3.2 declares `start` bare at line 1701 while its own prose says **"The
    start parameter SHOULD be present unless it is not known"** and **"The start
    parameter is optional for the "transfer" type Dialog Object"**, and Table 1
    gives it `S`/`O`. In both cases the declaration says mandatory and
    everything else says otherwise. The scale is the problem rather than either
    instance: **57 of the 115 bullet declarations in §§1–7 are bare**, so a
    validator built from the declarations alone over-constrains by an unknown
    amount, and a reader must check the prose for every one. The repair is
    mechanical — mark the exceptions at the declaration, as 52 declarations
    already do. Same issue tracker as items 11–15.
