---
schema: "library-summary/v1"
id: rfc-9277
record: rfc-9277
type: summary
updated: "2026-10-20"
---

# On Stable Storage for Items in Concise Binary Object Representation (CBOR)

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | standard — Standards Track |
| **Authors** | M. Richardson, C. Bormann |
| **Published** | August 2022 |
| **Identifier** | RFC 9277 · DOI 10.17487/RFC9277 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9277.txt |
| **Digest** | `bd637eafad9ef940c8f5d029076f70c58af7bde6beb38efee5ba7af3690289f7` (sha-256 of the .txt, retrieved 2026-09-22) |

## Overview

RFC 9277 gives stored CBOR a magic number, so that `file(1)` can tell one CBOR
artifact from another. Its argument is that identifying a file as "CBOR" is no
more use than identifying an APK as a ZIP (§1), so the first bytes must name the
**CBOR Protocol** — "a specification that uses CBOR as its encoding" — rather
than the encoding. **Three** enveloping methods, each built from **two nested
tags**: *CBOR Tag Wrapped* (§2.2), tag 55799 around a protocol-specific tag
around a single data item, giving an 8-byte fingerprint; *Labeled CBOR Sequence*
(§2.3), a separate 12-byte data item prepended to an RFC 8742 sequence, tag
**55800** around a protocol-specific tag around the 3-byte string `'BOR'`; and
*CBOR-Labeled Non-CBOR Data* (Appendix D), the same 12-byte shape under tag
**55801**, prepended to data that is not CBOR at all. §4
allocates 55800, 55801, and 65,279 tag numbers — one for every actual or
potential CoAP Content-Format.
*(`[correction]` 2026-10-21, pass 3: this read "Two enveloping methods". §1
introduces the third outright — "A third method is also proposed by which a CBOR
format tag is prepended to identify non-CBOR files." — and §2's own "This
section presents two enveloping methods." scopes its count to §2.
`design-notes.md` §9 recorded this refutation on 2026-10-20 and did not carry it
back here; it matters because a non-CBOR artifact of ours would be labelled by
the third method and not by either of the other two.)*

**It does not define tag 55799.** RFC 8949 §3.4.6 does; RFC 9277 cites it as
STD 94 and builds on it. And the document carries **zero** BCP 14 keywords
(`bin/bcp14-count` → 0) and no requirements-language section at all.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Encoding | **core** | MD-3's option 5 excludes IANA tags. This is the IETF's answer to "what identifies a stored CBOR artifact", and the answer is two tags. It is the sharpest available measure of what that exclusion costs. |
| Naming | **core** | `ARCH-0002` P1 makes identity key-relative. This makes *artifact-type* identity registry-relative, in band, at byte 0. Two answers to two different questions, and only one of them is ours. |
| Security | supporting | §3 raises the check-versus-use problem by name and resolves nothing; under all three methods the label sits outside every signature. |

**The finding to act on: concatenating two labelled files is the operation
RFC 8742 blesses and this document says needs care, and neither says who
resolves it.** RFC 8742 §2 states that "concatenating zero or more CBOR
Sequences also results in a CBOR Sequence" — `cat a.seq b.seq > c.seq` is in
spec, and it is the whole reason to pick a sequence over an array. RFC 9277
Appendix A.2 then: "There are situations where multiple objects may be
concatenated into a single file. If each object is preceded by a Labeled CBOR
Sequence label, then there may be multiple such labels in the file… If the
CBOR-Sequence-based protocol does not define the semantics for or at least
tolerate embedded labels, care must be taken when concatenating Labeled CBOR
Sequences to remove the label from all but the first part."

So **a magic number designed for an appendable format is unsafe under append**,
and the fix is delegated to each protocol with no default. For an append-only
log of statements that is the first rule the export profile has to write and the
easiest one to miss, because both documents are individually right: RFC 8742's
claim is about well-formedness and RFC 9277's is about interpretation. Asserting
`contradicts` would overclaim; the edge is `see_also` and the tension is
recorded here. Appendix A.2 also offers the opposite reading — "A protocol based
on CBOR Sequences may specify that Labeled CBOR Sequence labels can occur within
a CBOR Sequence, possibly even to switch to data items following in the sequence
that are of a different type" — which is a *feature* for a mixed-type archive
and a parser ambiguity for a homogeneous log. Choosing between them is ours, and
the document is explicit that its advice "is informative" (§1).

## Where it cuts against MD-3

MD-3 (2026-09-28) narrowed DEC-002 to option 5 — "reduced CBOR, no IANA tags,
COSE as export only" — and a narrowing is not an acceptance; no DEC-002 ADR exists.
<!-- [correction 2026-10-21, pass 3 - cross-check] This dropped "as" inside a
     quotation attributed to MD-3. docs/extraction.md:124, the only
     in-repository statement of the gloss, writes "COSE as export only". The
     lane's design-notes asserted that the no-"as" form MATCHED that source;
     it does not, and that correction is recorded there. -->

**Verdict: tag 55799 is a genuine cut against the no-tags half, and it is
narrower and sharper than "option 5 forbids the only way to say this file is
CBOR".** Four parts.

**1. The 55799 loss is already booked, and it is not what *this* document
costs us.** `rfc-8949`'s design notes already score §3.4.6: "Self-described
CBOR, head `0xd9d9f7` … media type, file extension, or our own framing …
concrete cost for the MD-1 archives target: statements stored as files on a
share have no magic number." 55799 belongs to RFC 8949, so option 5 loses it
whether or not RFC 9277 exists. What RFC 9277 adds is that **the IETF's
substitute is also a tag, and the outer one is not the one that matters.** Both
methods are two nested tags; the outer (55799, or 55800 for a sequence) says only
"CBOR" or "the file contains CBOR Sequences", while the inner — the tag that
says *which* protocol, which is the whole point of §1's APK-is-a-ZIP argument —
must be a 4-byte First Come First Served allocation obtained by the protocol
designer (§2.1). Under a no-tags rule the in-band answer to "what kind of file
is this" is therefore unavailable at any price. Under **option 2** ("CBOR + CDDL
as canonical; COSE for signed form") it costs one email: §2.1, "The IANA policy
for 4-byte CBOR tags is First Come First Served [RFC8126] so only a simple
interaction (e.g., via Web or email) with IANA is required." **That is a cost
option 5 pays and option 2 does not, and it lands on artifact identity rather
than on encoding** — the same shape as `rfc-9679`'s Cut A, one layer out.

**2. The source's own words on optionality, and they are permissive four times
over.** With zero BCP 14 keywords nothing below is a dispensation or an
obligation; every one is description.

- §1: "there is no requirement that either type of envelope be transferred on
  the wire." Lowercase, and the document has no requirements language at all.
- §2.2: "Applications that need to send the stored CBOR data item across a
  constrained network may wish to remove the two tags if the type is understood
  from the protocol context"; and "a CBOR Protocol specification may pick the
  specific cases where the CBOR Tag Wrapped enveloping method is to be used. For
  instance, it might specify its use for storing the representation in a local
  file or for Web access, but not within protocol messages that already provide
  the necessary context."
- §2.3: "The use of a CBOR Sequence allows the application to trivially remove
  the first item with the two tags."
- Appendix A: "Both the Labeled CBOR Sequence and the wrapped tag can be
  trivially removed by an application before sending the CBOR content out on the
  wire." Appendix A.1: if the eight bytes "are a problem on the wire (and they
  often are if CBOR is being considered), then the Labeled CBOR Sequence format
  should be adopted for the stored format" — lowercase again.

So the envelope is **storage-only and strippable by design**, which weakens the
cut in one direction: a tag-free *wire* format is exactly what RFC 9277 expects,
and MD-3's export posture conflicts with nothing here. It does not weaken the
cut for storage, which is MD-1's archive target and §1's stated motivation:
"When files become disconnected from their type information, such as when
attempting to do forensics on a damaged system, being able to identify the type
of information stored in a file can become very important."

**On stripping and on absence, the asymmetry is itself the finding: tolerating
absence is assumed everywhere and required nowhere, and the document's one
explicit warning runs the other way.** Appendix A: the label "requires that all
programs that expect to examine that file be able to skip what appears to be a
CBOR item with two tags nested around a 3-byte byte string. The 3-byte entry is
not of the format the program would normally have processed, so it may be a
surprise." With no BCP 14 keywords there is no conformance statement in either
direction — so a reader that rejects a labelled file and a reader that rejects
an unlabelled one are both conformant, and the two are not interoperable.

**3. The substitute does not discharge condition (4), and it is easy to think it
does.** The `canonical-encoding` topic's condition (4) is that "the encoding
profile is named by an authenticated type indicator carried inside the signed
bytes", which `R-O-05` delivers. RFC 9277's indicator is outside every signature
under all three methods: in Tag Wrapped the two tag heads enclose the COSE
message, and in Labeled CBOR Sequence and CBOR-Labeled Non-CBOR Data the
12-byte label is a *separate data item* in front of it. §3 says the adjacent thing without drawing the conclusion:
"Protective applications (that check data) cannot rely on the applications they
try to protect (that use the data) to make exactly the same decisions in
recognizing file formats. (This is an instance of a check versus use issue.)" So
relabelling a stored artifact — swapping the inner tag — breaks no signature and
can route the same bytes to a different parser. **The mechanism option 5 forbids
would not have satisfied our own condition (4) anyway.** What option 5 actually
gives up is `file(1)`, triage and forensics; on the signing path it gives up
nothing. Worth stating plainly, because "we have a magic number" reads like an
answer to the type-indicator question and is not one.

**4. "No IANA tags, identify by media type instead" stopped being two
independent choices in 2022.** §4.3 and Appendix B allocate 1668546817
(0x63740101) through 1668612095 (0x6374FFFF) — 65,279 code points — with
semantics "the representation of content-format ct < 65025 is indicated by tag
number TN(ct) = 0x63740101 + (ct / 255) * 256 + ct % 255". **65,025 of the CBOR
tag registry's code points are now a mechanical function of the CoAP
Content-Formats registry's numbers.** (Checked here: the image of TN over
ct < 65025 is 65,025 distinct values and none contains a zero byte, which is
what the formula's own note says it is for — "This formula avoids the use of
zero bytes in the representation of the tag number" — so the 254 allocated
points TN cannot reach are exactly the zero-low-byte ones. The arithmetic is
ours; the document works only TN(112), TN(272), TN(432) and TN(11050).) For
`R-M-12` that is the strongest evidence in this library that CBOR's tag space
and the media-type space are not independent governance domains, and for the
registry-reduction argument it closes an escape route: **"use a media type, not
a tag" leads back to a tag number** whenever the media type has a content-format
number.

The useful corollary, and it is **ours rather than the document's**:
`application/cbor-seq` already holds CoAP Content-Format 63 (RFC 8742 §6.2,
Table 1), so TN(63) = 1668546880 = 0x63740140, and a labelled CBOR-sequence file
needs **no new allocation at all** — the 12-byte label would be
`d9d9f8 da63740140 43 424f52`, fingerprint `d9d9f8da63740140`. It costs nothing
and says only "a CBOR sequence follows", which is why it is cheap and why it
does not answer §1's question. Saying "an m-of-n statement log follows" is the
part that needs the FCFS allocation.

**What `R-O-03` demands of whatever we substitute.** `R-O-03` governs
canonicalisation, so it does not reach a file header on its own terms;
`docs/extraction.md` has already generalised it once, to filenames. Applied here
it rules out exactly one of the three substitutes `rfc-8949`'s design notes
list. A **media type** (`application/cbor-seq`, RFC 8742 §6.1) and a **file
extension** each cite something, cost nothing, and live out of band. **Our own
framing** is an invention — a private magic number, unregistered, with no
defining specification to cite — and it is the one R-O-03's spirit rejects,
while being the only substitute that is both in band and tag-free. So the honest
finding is that **option 5's in-band identification options are: nothing, or a
rule it forbids.** The ADR has to take the out-of-band answer and say so, or
carve the two tags out by name — which is the precedent
`draft-mcnally-deterministic-cbor` already set, since the profile closest to
option 5 announces itself with registered tag 201 and that record's extraction
says to "exclude tag 201 … by name".

## Implementations

The document names exactly one deployment, and it is in an appendix.
**Openswan** moved the bespoke C-struct serialisation between its `pluto` daemon
and its `addconn`/`whack` control programs to CBOR, and took IANA tag
**1330664270** = 0x4F50534E = `"OPSN"` for the Labeled CBOR Sequence method
(Appendix C; the arithmetic checks). §1 names CoSWID and EAT as "Examples of
CBOR Protocols currently under development" and says of C509 only that it "would
benefit from being an identified CBOR Protocol" — three candidates, no users —
and classes COSE itself as "infrastructure" rather than a protocol needing a
magic number. *Searched the document on 2026-10-20: one named implementation,
and its registered tag is the evidence.*

| Name | Kind | License | URL |
|---|---|---|---|
| Openswan (`pluto`, `addconn`, `whack`) | IPsec daemon + IPC, tag 1330664270 | not stated in the source | not given in the source |

The license and URL are left unstated deliberately: Appendix C names "The
Openswan IPsec project" and nothing else, and neither was checked here.
<!-- [correction 2026-10-21, pass 3 - cross-check] The quotation opened with a
     lower-case "the"; source line 829 reads "The Openswan IPsec project". It
     was the ONLY delimited case-fold left in the lane, and it falsified the
     "ZERO resolve only case-insensitively" claim stated elsewhere in this
     record. -->


**And the consumer the whole document is written for is not shipped.** `file(1)`
appears four times (abstract, §1 twice, §1.2) and the abstract's claim is to
define a format "friendly to common systems that recognize file types, such as
the Unix file(1) command" — yet the document contains **no magic(5) pattern** for
anyone to install, and §1.2 concedes the hard case: "Less ideal solutions have a
pattern that needs to be matched, but in which some bytes need to be ignored.
While the Unix file(1) command can be told to ignore certain bytes, this can
lead to ambiguities." A magic number whose reference consumer has no rule file is
an allocation, not an identification.

## Artifacts in this record

*(`[correction]` 2026-10-21, pass 3 of the extraction: this section used to list
three files and then three absences — "**No `distilled/`, and no `distillation`
block**", "**No test vectors held here**" and "**No `distilled/schema/`**". All
three were true when the summary was written and all three were false by the end
of the same day: the record carries `distillation.standard: FX-1` with seven
artifacts, fourteen vectors and a seven-file schema directory. Pass 1 built
them, pass 2 audited them, and neither came back here. The reasoning that
survives is kept below.)*

| File | What it is |
|---|---|
| `record.yaml` | metadata — `bears_on: DEC-002` and `R-M-12`, four typed `see_also` edges, each commented, and the `distillation` block |
| `summary.md` | this document |
| `summary.html` | GENERATED and untracked — `bin/render-html` builds it beside the source (`docs/generated-views.md`) |
| `distilled/normative.md` | every normative span, verbatim, with its locator |
| `distilled/requirements.yaml` | 195 entries, **all `kind: inferred`**, both keyword counts **0** |
| `distilled/schema/` | 3 verbatim files and 4 derived — the four CDDL snippets, the three registry entries, the TN formula, and ours: the TN function as data, the 30 label spellings, the three envelopes as CDDL |
| `distilled/messages.yaml` | 7 structures, 29 fields; 56 of the 195 requirements cited by a named field |
| `distilled/state-machine.yaml` | DERIVED — 5 states, 8 transitions, 1 self-loop, 6 undefined transitions |
| `distilled/examples/` | 14 vectors: 7 the source's own, 7 ours |
| `distilled/design-notes.md` | MD-3 clause by clause, six cuts against it, 9 source defects |

What the extraction changed about the forecast above, and what it did not:

- **The "nothing qualifies as a requirement" judgement stands, and the
  extraction measured it rather than assuming it.** `bin/bcp14-count` returns 0
  and all 195 entries are `kind: inferred`; under `docs/requirements.md` §1's
  four-part test nothing here qualifies. `status` therefore stays `summarized`
  and `tags` stay `evidence`, not `normative`.
- **The source's test vectors did become fixtures.** §2.2.1, §2.3.1 and
  Appendix C are `V-0001`–`V-0003`, every hex string rebuilt from its annotated
  source lines and executed; seven more are ours, and two of those deliberately
  have no expected result because the document defines none.
- **There is a `distilled/schema/`, and the forecast's reason for not having one
  is now a finding in it.** Every one of the four snippets is a tag assertion —
  the mechanism option 5 excludes — and none of them is an envelope, so the
  envelope CDDL is `envelopes.derived.cddl` and its value is the four things
  CDDL cannot say about these layouts.
- **No `contradicts` edge**, for the reason given in the finding above: the
  concatenation tension is well-formedness versus interpretation, not
  disagreement.

## Limits

- **A Standards Track RFC with zero normative statements.** `bin/bcp14-count` →
  0, and "BCP 14", "RFC 2119", "RFC 8174" and "key words" do not appear in the
  document at all — there is no requirements-language section to omit them from.
  It allocates three tags and 65,279 tag numbers, defines two stored formats and
  an advisory appendix, and constrains nobody. "We conform to RFC 9277" is not a
  testable claim, and when two implementations disagree about whether a label may
  appear mid-file — the question Appendix A.2 leaves open — there is no clause to
  point at.
- **The magic number is only as deterministic as the encoder's goodwill.** §2
  promises "a deterministic first 8 to 12 bytes", and that holds only because
  §2.1 forces the protocol tag into 0x01000000–0xFFFFFFFF "In order to be in the
  4-byte range, and so that there are no leading zero bytes in the 4-byte
  encoding of the tag number". Both worked examples write the 4-byte tag head
  `0xda`. But RFC 8949 §3.1 admits the 8-byte head `0xdb` for the same value, and
  nothing here requires preferred serialisation, because nothing here requires
  anything. A well-formed, semantically identical file could begin
  `d9 d9f8 db 00000000 63740212`, and `file(1)` would miss it. For a document
  whose single deliverable is a fixed byte prefix, leaving that prefix's own
  encoding to RFC 8949 §4.2.1 by implication is the defect — and it is the one
  place where this record touches the determinism work in `draft-ietf-cbor-cde`
  and `draft-mcnally-deterministic-cbor`.
- **Four of the twelve label bytes exist because CBOR has no zero-arity tag, and
  the document says so.** §2.3: the `'BOR'` content "is also included simply
  because the inner nested tag needs to tag something." Its advertised benefit —
  "Should this file be reviewed by a human (directly in an editor or in a hexdump
  display), it will include the ASCII characters "CBOR" prominently" — is real,
  but those bytes sit at offsets 8–11, *past* the 8-byte fingerprint §2.3.1
  identifies ("the unique fingerprint … is composed of the 8 bytes
  d9d9f8da63740212 hex"). The human-readable part is not the identifying part.
- **The choice between the two methods is load-bearing, unguided, and declared
  informative.** §1: "This advice is informative." Appendix A poses three
  questions (A.1–A.3) and answers none of them with a rule, while noting that
  getting it wrong makes existing readers "throw errors or warnings" and that
  "the use of the Labeled CBOR Sequence may present an implementation hurdle to
  programs that previously just read a single data item and used it." A stored
  format chosen once for an archive's lifetime is the worst case for advice that
  is explicitly not normative.
- **Nothing says what a reader does with a known outer tag and an unknown inner
  one.** 55800 announces "the file contains CBOR Sequences"; the inner tag names
  a protocol the reader may not know. RFC 8949 §5.4 gives a validity-checking
  decoder meeting an unrecognised tag number two choices, and says of the
  rejecting one that "treating this case as an error can cause ossification and
  is thus not encouraged". So the file parses cleanly, and a
  reader can successfully read a file it cannot interpret, and the magic number's
  entire purpose, selecting the right application, fails open and silently. §3
  approaches this from the security side and states no rule.
- **The `application/cbor-seq` registration still says there is no magic
  number.** RFC 8742 §6.1 reads "Magic number(s): N/A" and "File extension(s):
  N/A"; RFC 9277 makes one constructible for exactly that media type (Appendix B
  plus content-format 63) and carries no `Updates: 8742` in its header. Two and a
  half years on, the registration a reader consults and the RFC that defines its
  magic number disagree, and neither document points at the other on this point.
- **An unresolved authoring-tool cross-reference survives into the published
  text.** Appendix D: "As with the Labeled CBOR Sequence {#sequences}, this
  choice of the tag content places the ASCII characters "CBOR" prominently into
  the header." A kramdown anchor, left in the RFC. Editorial only, and we have
  not checked it against the errata.
