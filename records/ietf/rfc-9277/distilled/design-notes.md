---
record: rfc-9277
kind: design-notes
title: "rfc-9277 — bearing on our design"
extracted: "2026-10-20"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§2.3`) are RFC 9277. Our own documents are cited by id (`ARCH-0002` P1,
`MD-3`, `R-O-03`). Four markers distinguish voices:

- unmarked prose reports **RFC 9277** or **our decisions**, as cited;
- a quotation is RFC 9277's own words, contiguous and mechanically checked,
  **unless the sentence names another document**, in which case the quotation is
  that document's;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project, or a claim in a
  sibling record of this library, that the sources do not support.

**[unverifiable-here] — read this before any quotation of ours.** This library
is **standalone by design** and holds **none** of `ARCH-0001`, `ARCH-0002`,
`ADR-0001`, `MD-3`, `PLAN-0001`, `DECISIONS-0001` or the `R-M-*` / `R-O-*` /
`R-I-*` requirement texts. A `find` over the worktree at this pass returns no
such file. **Every quotation of those documents below is therefore unverifiable
from this repository** and is marked `[unverifiable-here]` at first use in each
section. The convention is `rfc-9741`'s. **Two exceptions, in the other
direction:** `topics/canonical-encoding.yaml` *is* in this repository and its
conditions are quoted exactly; and §9's quotations are of this record's own
`summary.md`, checked against it at this pass.

**Decision status, stated plainly.** `DEC-002` in `ARCH-0001` §7 lists **four**
options — (1) canonical S-expressions, (2) "CBOR + CDDL as canonical; COSE for
signed form", (3) JSON + RFC 8785 JCS, (4) "Dual canonical (CBOR and JSON) with
a documented bijection" `[unverifiable-here]`. "Option 5" exists only as
*proposed* text in `ARCH-0001-PROPOSAL-v0.2.0` §3.3. `MD-3` (2026-09-28)
**narrowed** DEC-002 to option 5 — reduced CBOR, no IANA tags, COSE export only,
YAML as the human form — and a narrowing is **not** an acceptance: **no DEC-002
ADR exists.** `docs/extraction.md`: "An extraction that can only confirm is not
evidence." Nothing below may be read as an accepted encoding decision.

**What this document is, in one line.** The IETF's answer to *what identifies a
stored CBOR artifact*, and the answer is **two nested tags** — three times over,
with **zero BCP 14 keywords** in 41 KB. It does **not** define tag 55799; it
allocates 55800, 55801 and **65,279** content-format tag numbers.

**Why it reaches our design.** Because MD-3's option 5 excludes the IANA CBOR
Tags registry, and this is the sharpest available measure of what that exclusion
costs: the only in-band type indicator the IETF has standardised for stored CBOR
is built from the mechanism option 5 forbids. `[analysis]` And because the
answer turns out to be weaker than it looks — which is the half of the finding
that could only come from an extraction.

---

## 1. The question this record was extracted to answer

**Under a no-IANA-tags rule, is in-band identification of a stored artifact
available at any price? No. And the reason is narrower and sharper than "option
5 forbids the only way to say this file is CBOR".**

**Both methods are two nested tags, and the outer one is not the one that
matters.** §2.2: "The outer tag is a self-described CBOR tag, 55799, as described
in Section 3.4.6 of [STD94]." §2.3: "The outer tag is the self-described CBOR
Sequence tag, 55800." Appendix D: "The outer tag is the CBOR-Labeled Non-CBOR
Data tag, 55801." The outer tag says only *CBOR*, or — in the registry's own
words, verified in-library — "indicates that the file contains CBOR Sequences".
**The inner tag is the one that says which protocol**, which is the whole point
of §1's APK-is-a-ZIP argument: "For instance, an Android Package Kit APK (as used
to transfer and store an application) may be identified as a ZIP file." And §2.1
is explicit about where the inner tag comes from: "In both enveloping methods,
CBOR Protocol designers need to obtain a CBOR tag for each kind of object that
they might store in files." **Per kind of object.**

**So the 55799 loss is already booked and is not what this document costs us.**
`rfc-8949`'s design notes already score §3.4.6 — "Self-described CBOR, head
`0xd9d9f7`", with the concrete cost that "statements stored as files on a share
have no magic number". 55799 belongs to RFC 8949; the in-library IANA row for it
reads reference **"RFC 8949"**, checked at this pass. **What RFC 9277 adds is
that the IETF's substitute is also a tag, and that the part doing the work needs
a First Come First Served allocation.** `[analysis]` Under a no-tags rule the
in-band answer to *what kind of file is this* is unavailable at any price. Under
**option 2** it costs one email: §2.1, "The IANA policy for 4-byte CBOR tags is
First Come First Served [RFC8126] so only a simple interaction (e.g., via Web or
email) with IANA is required."

### 1.1 And the substitute would not have discharged condition (4) anyway

This is the part that changes the balance, and it is easy to miss.

`topics/canonical-encoding.yaml` condition (4) reads: **"The encoding profile is
named by an authenticated type indicator carried inside the signed bytes."**
`R-O-05` `[unverifiable-here]` delivers it.

**RFC 9277's indicator is outside every signature, under all three methods, by
construction.** In Tag Wrapped the two tag heads *enclose* the payload; in the
Labeled CBOR Sequence the label is a *separate data item* in front of it — §2.3,
"This method prepends a newly constructed, separate data item to the CBOR
Sequence, the _label_."; Appendix D the same. There is no nesting in which a
signature over the content could cover it.

§3 states the adjacent problem and draws no conclusion: "Protective applications
(that check data) cannot rely on the applications they try to protect (that use
the data) to make exactly the same decisions in recognizing file formats.  (This
is an instance of a check versus use issue.)"

`[analysis]` So **relabelling a stored artifact — swapping the inner tag — breaks
no signature and can route the same bytes to a different parser.** The fixture is
`examples/vectors.yaml` `D-0003`: §2.3.1's payload behind Appendix C's Openswan
label, well formed, 15 bytes, and nothing in the document detects it.
**The mechanism option 5 forbids would not have satisfied our own condition (4).**
What option 5 actually gives up is `file(1)`, triage and forensics; on the signing
path it gives up nothing. Worth stating plainly, because *we have a magic number* reads like an answer to the type-indicator question and is not one.

### 1.2 The second finding: the magic number is not deterministic

**§2's central claim is false in general, and the refutation is arithmetic.**
"Both use CBOR tags in a way that results in a deterministic first 8 to 12
bytes." That holds only under **preferred serialization**, and nothing in
RFC 9277 requires anything — the document has **zero** BCP 14 keywords. RFC 8949
§3.1 admits a wider head for the same argument value, and §4.1's preferred rule
is an encoder-side recommendation a conforming decoder does not enforce.

`schema/prefix-spellings.derived.txt` enumerates every well-formed
definite-length spelling. For the 12-byte label: **30 of them.** One is 12 bytes
long. **Five** match the 8-byte fingerprint §2.3.1 states. **Twenty** put a zero
byte inside the first eight — defeating §2.1's own advice to avoid values that
"may confuse implementations that treat the magic number as a C string", *even
when the registrant followed it*. And **30 is a floor**, because RFC 8949 §3.2.3
also admits an indefinite-length byte string for the 3-byte content.

§2.1 pins the tag **value** into `0x01000000` to `0xFFFFFFFF` — "In order to be
in the 4-byte range, and so that there are no leading zero bytes in the 4-byte
encoding of the tag number" — and that is exactly as far as it goes: it makes
`da` the *shortest* head and does not forbid `db`, and it does not reach the
outer tag at all, whose value is `55800 = 0xD9F8`. Fixtures `D-0001` and
`D-0002`.

`[analysis]` **This is not an argument against option 5** — option 5 carries none
of these tags and pays nothing here. It is an argument that **the substitute
option 5 is compared against is weaker than it looks.** *We could have had a magic number* is worth less when the magic number has thirty spellings and the
specification that defines it requires nothing.

---

## 2. What we adopt

**Very little, and the list is short on purpose.**

### 2.1 `TN(63)`, as a fact to put in front of the ADR — not as a mechanism

`application/cbor-seq` already holds CoAP Content-Format **63** (RFC 8742 §6.2,
Table 1, held verbatim at
`records/ietf/rfc-8742/distilled/schema/registrations.txt` region `T01`). §2.1:
"For CBOR data items that form a representation that is already described by such
a Content-Format Number, a tag number has proactively been allocated in Section
4.3". `[analysis]` So `TN(63) = 1668546880 = 0x63740140`, recomputed at this
pass, and a labelled CBOR-sequence file is
`d9d9f8 da63740140 43 424f52` — fingerprint `d9d9f8da63740140`, fixture
`D-0006`. **It needs no new IANA allocation at all**, because the tag number is a
function of a number RFC 8742 obtained in 2020.

We adopt the **fact**, not the label: it is the price of the thing option 5
refuses, and it is **zero** for the part that says *a CBOR sequence follows* and
**an FCFS allocation** for the part that says *an m-of-n statement log follows*.
That asymmetry is what the ADR needs and it is not written down anywhere else.

### 2.2 The storage-versus-wire distinction, as a structure for our own profile

Four separate statements establish that the envelope is **storage-only and
strippable by design**: §1, "there is no requirement that either type of envelope
be transferred on the wire"; §2.2, "may wish to remove the two tags if the type is
understood from the protocol context"; §2.3, "The use of a CBOR Sequence allows
the application to trivially remove the first item with the two tags."; and
Appendix A, "Both the Labeled CBOR Sequence and the wrapped tag can be trivially
removed by an application before sending the CBOR content out on the wire."

`[analysis]` We adopt the **distinction** — a stored form and a wire form are two
artifacts and may differ — and we note that it **weakens the cut against MD-3 in
one direction**: a tag-free wire format is exactly what RFC 9277 expects, so
MD-3's export posture conflicts with nothing here. It does not weaken the cut for
**storage**, which is §1's stated motivation: "When files become disconnected
from their type information, such as when attempting to do forensics on a damaged
system, being able to identify the type of information stored in a file can
become very important."

### 2.3 Appendix A.2's rule, as the first line of an append-only log's export profile

"If the CBOR-Sequence-based protocol does not define the semantics for or at
least tolerate embedded labels, care must be taken when concatenating Labeled
CBOR Sequences to remove the label from all but the first part."

`[analysis]` Whatever we do about labels, **we have to answer this question
explicitly**, because the document delegates it with no default and because the
operation it concerns — concatenating two logs — is the one RFC 8742 §2 blesses
and the one an append-only log does constantly. §3 below.

---

## 3. What we adapt, and how

### 3.1 The concatenation question, adapted into a rule we must write

**The finding, and it is the record's headline.** RFC 8742 §2 states
"concatenating zero or more CBOR Sequences also results in a CBOR Sequence" —
verified against `.cache/rfc-8742.txt` at this pass — so `cat a.seq b.seq >
c.seq` is in spec, and it is the whole reason to pick a sequence over an array.
RFC 9277 Appendix A.2 then: "There are situations where multiple objects may be
concatenated into a single file.  If each object is preceded by a Labeled CBOR
Sequence label, then there may be multiple such labels in the file." And it
offers **two incompatible readings and chooses neither** — a feature, "A protocol
based on CBOR Sequences may specify that Labeled CBOR Sequence labels can occur
within a CBOR Sequence, possibly even to switch to data items following in the
sequence that are of a different type", or a hazard, the "care must be taken"
sentence above.

`[analysis]` So **a magic number designed for an appendable format is unsafe
under append**, and the fix is delegated to each protocol with no default. Both
documents are individually right — RFC 8742's claim is about **well-formedness**
and RFC 9277's about **interpretation** — which is why neither record asserts
`contradicts`. `state-machine.yaml` holds it as a transition into a state the
document declines to define; `examples/vectors.yaml` `D-0004` is the 30-byte
file with a label at offset 15, and `D-0005` is the same file with the second
label stripped.

**And `D-0005` carries a cost the document does not mention.** `[analysis]`
Stripping the inner labels makes the two source files indistinguishable from one
six-element file: the boundary between them is gone, which is RFC 8742's
completeness hole arriving from the other direction. If the boundary matters,
stripping is wrong; if it does not, the label was never needed per object. **The
document poses neither half**, and an append-only log has to answer both.

### 3.2 §1.2's four properties, adapted as a test for whatever we substitute

"Ideally, a magic number is a fingerprint that is unique to a specific CBOR
Protocol, is present in the first few (small multiple of 4) bytes of the file and
does not change when the contents change, and does not depend upon the length of
the file."

`[analysis]` Four checkable properties in a section titled *Requirements for a
Magic Number* that contains **no requirements language whatever**. They are the
right test and we should apply them to our own answer — and note that **a media
type passes three of the four and fails the second**, because it is not in the
file at all.

---

## 4. What we reject, and why

- **Both enveloping methods, for anything of ours, under option 5.** §1. Not a
  judgement about their quality: option 5's exclusion makes the inner tag
  unobtainable, and the inner tag is the whole mechanism.
- **The claim that the envelope gives a deterministic prefix.** §1.2. Thirty
  spellings. If we ever write a `file(1)` rule for our own artifacts, it must
  enumerate or must declare that we require preferred serialisation — and the
  declaration would be **ours**, since RFC 9277 does not make it.
- ***We have a magic number* as an answer to the type-indicator question.**
  §1.1. It is unauthenticated under all three methods.
- **Appendix A as guidance.** §1 declares it informative in four words — "This
  advice is informative." — and it answers its three survey questions with
  conditionals. `[analysis]` A stored format is chosen once for an archive's
  lifetime, which is the worst case for advice that is explicitly not normative.
- **Our own private framing, as the substitute.** `[analysis]` `rfc-8949`'s
  design notes list three substitutes for §3.4.6: a media type, a file
  extension, or our own framing. Under `R-O-03` `[unverifiable-here]` —
  "canonicalization algorithm SHALL be cited, not invented silently", which
  `docs/extraction.md` has already generalised once, to filenames — a media type
  and a file extension each **cite** something and cost nothing, while our own
  framing is an invention: a private magic number, unregistered, with no defining
  specification to cite. It is also **the only substitute that is both in band
  and tag-free.** So the honest finding is that **option 5's in-band
  identification options are: nothing, or a rule it forbids.**

---

## 5. Mapping to our decisions

### 5.1 MD-3, clause by clause

FX-1 requires a CBOR/COSE/envelope record to address MD-3 **header by header**.
This document defines no COSE header parameter, so the mapping is
clause-by-clause and the interesting cells are the two that are not empty.

| MD-3 option-5 clause | what RFC 9277 says to it | measured |
|---|---|---|
| **reduced CBOR** (data model, no extras) | nothing about the data model. Its whole content is a byte prefix | the document adds no type, no value and no data-model element |
| **no IANA tags** | **the whole document.** Three enveloping methods, every one two nested tags; §4: "These IANA considerations are entirely about CBOR tags in the "Concise Binary Object Representation (CBOR) Tags" registry [IANA.CBOR-TAGS]." | 3 tags allocated plus a **65,279**-wide block; **0** non-tag registrations |
| **COSE as export only** | **nothing, and it says so explicitly.** §1: "CBOR Object Signing and Encryption (COSE) itself [RFC8152] is considered infrastructure." So a COSE message is **not** a CBOR Protocol and gets no magic number of its own | `COSE` occurs twice in the body, both in §1; no COSE header parameter is named anywhere |
| **YAML as the human form** | nothing | `YAML` = **0** occurrences |

`[analysis]` The `COSE is infrastructure` row is the one worth keeping. **Our
export artifact is a `COSE_Sign1`, and RFC 9277 declines to give that class of
object an identity at all** — so even a project that accepted the two tags would
find this document silent about the one artifact we export. The identifiable
thing would have to be *our* statement format, not the COSE envelope carrying it.

### 5.2 `ARCH-0001` §4.1 and `ARCH-0002` P1, artifact by artifact `[unverifiable-here]`

This document is about **artifact-type identity**, which is a different question
from the one our naming requirements answer, and the table is worth drawing
because the two are easy to confuse.

| our construct | what identifies it, natively | what RFC 9277 would add | verdict |
|---|---|---|---|
| a principal (`ARCH-0002` P1) | a **key**, and names are key-relative | nothing — it identifies file *types*, not principals | **different question** |
| `KeyId` (`DEC-003`) | a digest of canonical key bytes | nothing. `DEC-003`'s open point, "must specify canonical key bytes before hashing", is untouched | nothing applies |
| `Name.labels` (P1 local labels) | the defining key plus the label | nothing | nothing applies |
| `R-M-12`'s `(key, local label)` pair | the pair | nothing *directly* — but §5.4 below is the registry-dependence evidence `R-M-12` wants | **evidence, not mechanism** |
| a **stored statement file** | nothing in band today | tag 55799 + an FCFS protocol tag, 8 bytes | **unavailable under option 5** |
| a **stored statement log** (CBOR Sequence) | nothing in band today | tag 55800 + an FCFS protocol tag, 12 bytes | **unavailable under option 5**; `TN(63)` gives a free but uninformative version (§2.1) |
| an **exported `COSE_Sign1`** (`R-I-03`) | nothing in band today | **nothing — COSE is "infrastructure"** | the document declines the case |
| a **domain of discourse** (`ARCH-0002` P4) | a hash over the schema set | an FCFS tag would identify the *file*, never the content | nothing applies |

`[analysis]` The shape: **everything of ours that this document could label is a
file, and everything our requirements are about is a key or a digest.** The two
identity systems do not meet. That is itself the answer to "is this core?" — it
is core to DEC-002 and irrelevant to `ARCH-0002` P1, and the record's
`applicability` saying `naming: core` is defensible only in the registry-governance
sense of §5.4.

### 5.3 The `canonical-encoding` topic's six conditions

| condition | does RFC 9277 bear on it? |
|---|---|
| **(1) injective encoding** | **Yes, negatively, and it is a new instance.** One label has **30** well-formed spellings (§1.2). The *data model value* is one; the *bytes* are thirty; and the whole deliverable is a claim about bytes. Condition (1) is about the encoding of values, and this is a non-injectivity in the **inverse** direction — many encodings of one value — which is exactly what a deterministic profile forbids and what this document does not require |
| **(2) decoder rejects non-canonical input** | **Yes, negatively.** Nothing here rejects anything: zero BCP 14 keywords, and no rule for a non-preferred spelling, an unknown inner tag, a mid-file label or a missing label. Four undefined reader behaviours, enumerated in `state-machine.yaml` |
| **(3) canonicalise once, at authoring** | no. There is nothing to canonicalise |
| **(4) authenticated type indicator inside the signed bytes** | **Yes, and this is the record's sharpest finding. NOT DISCHARGED by either method.** §1.1, fixture `D-0003` |
| **(5) canonical order for set-valued fields** | no. But note §2.2.1's own example prints its map keys `0, 6, 2`, which is **not** RFC 8949 §4.2.1 order — the document's only Tag Wrapped example has a non-deterministically encoded payload |
| **(6) declared Unicode normalisation rule** | no. `normaliz*` occurs **0** times; `Unicode` occurs 4 times and every one is about the prefix **not** being valid Unicode |

### 5.4 `R-M-12`: the registry-reduction argument, and the escape route this closes

**MD-3's two halves — no IANA tags, and identify by media type instead —
stopped being independent choices in 2022.** `[unverifiable-here]` §4.3 allocates `1668546817` (`0x63740101`) to `1668612095`
(`0x6374FFFF`) with semantics "the representation of content-format ct < 65025 is
indicated by tag number TN(ct) = 0x63740101 + (ct / 255) * 256 + ct % 255".

Computed at this pass and held as data in
`schema/content-format-tag.derived.yaml`:

- the block is **65,279** code points wide; **TN**'s image is **65,025**;
- **TN is injective** over `ct < 65025`, and maps its domain **exactly onto the
  block's endpoints**: `TN(0) = 1668546817` and `TN(65024) = 1668612095`;
- the image is **exactly** the values `0x6374XXYY` with `XX` and `YY` both
  non-zero. So the aside's claim — "This formula avoids the use of zero bytes in
  the representation of the tag number." — is **stronger than it says**: **no**
  value in the image contains a zero byte in **any** of its four bytes, because
  the high half-word is `0x6374`, which `[analysis]` is the ASCII pair **"ct"**;
- the **254** allocated code points TN cannot reach are **exactly** the
  zero-low-byte ones, and the document never mentions them.

`[analysis]` **So 65,025 of the CBOR Tags registry's code points are a mechanical
function of the CoAP Content-Formats registry's numbers.** Not a cross-reference
and not a convention: a formula, published as the semantics field of the
allocation, and reproduced verbatim in the registry
(`records/iso/iana-cbor-tags/distilled/tables.yaml`, row
`1668546817-1668612095`, checked at this pass). For `R-M-12`
`[unverifiable-here]` that is the strongest evidence in this library that the
CBOR tag space and the media-type space are **not independent governance
domains**, and it closes an escape route: **naming a media type leads
back to a tag number** whenever the media type has a content-format number — and
`application/cbor-seq` has one.

---

## 6. Where this document cuts against MD-3

`MD-3` is a dated **narrowing** of DEC-002, not an acceptance. **Six cuts. Four
name the option they favour, one is stated in option 5's favour, and one runs
against the record's own headline.** `[analysis]` throughout — the document takes
no view on our decision.

**Cut 1 — the in-band type indicator costs option 5 everything and option 2 one
email. Favours option 2 outright, and it is the cleanest cut in the record.**
§2.1: "The IANA policy for 4-byte CBOR tags is First Come First Served [RFC8126]
so only a simple interaction (e.g., via Web or email) with IANA is required."
Under option 2 ("CBOR + CDDL as canonical; COSE for signed form")
`[unverifiable-here]` a protocol-specific tag is an ordinary cost of doing
business; under option 5 it is excluded by definition, so the answer to §1's
question is unavailable **at any price**. `[analysis]` **And it lands on
artifact identity rather than on encoding** — the same shape as `rfc-9679`'s
Cut A, one layer out. Note the scope honestly: `MD-3` retains option 2 only as a
comparison fixture, so this is a cost comparison and not a live contest.

**Cut 2 — the 65,025-point formula is the registry-reduction argument's best
evidence and it cuts *for* option 5's premise while cutting *against* its
tactic. Favours option 5's reasoning, not its rule.** §5.4. `[analysis]` Option
5 exists because central allocation is a dependency worth refusing, and §4.3 is
the strongest demonstration in this library that the dependency is real and
compounding — one registry's numbers became another registry's address space by
arithmetic. But the same fact shows that **naming a media type does not escape
it**: the escape route option 5's own rationale reaches for leads back to a tag
number. So the evidence supports the *motive* and withdraws the *method*, and an
ADR that cites this document for either half alone has misread it.

**Cut 3 — the substitute does not satisfy our own condition (4), so the thing
option 5 gives up is smaller than it looks. Favours option 5, and it is stated
so the balance is honest.** §1.1, fixture `D-0003`. `[analysis]` Under every
option that carries these tags, the type indicator is **outside** the signature.
So options 2 and 4 do not get condition (4) from this mechanism either; they get
`file(1)`, triage and forensics, and option 5 gives up exactly those three
things and nothing on the signing path. This is the one place in the record where
the evidence runs in option 5's favour, and it is worth more than it looks,
because it narrows the loss from *we cannot identify our artifacts* to *we cannot
identify them to `file(1)`*.

**Cut 4 — the one deliverable is not deterministic, which weakens the comparison
fixture rather than any option. Option-neutral.** §1.2, 30 spellings, fixtures
`D-0001` and `D-0002`. `[analysis]` It binds whichever option wins in one
concrete way: **if we ever write a magic rule or a prefix check for our own
artifacts, the determinism of that prefix is ours to require**, and under
`R-O-03` the requirement must be declared as ours, because RFC 9277 does not
make it. It is also the one place where this record touches the determinism work
in `draft-ietf-cbor-cde` and `draft-mcnally-deterministic-cbor`, **neither of
which RFC 9277 cites**.

**Cut 5 — the precedent for carving the tags out by name already exists in this
library, and it was set by the profile closest to option 5. Favours option 5
procedurally and costs it coherence.** `draft-mcnally-deterministic-cbor`
announces itself with registered tag **201**, "enclosed dCBOR", and that
record's extraction says to "exclude tag 201 ... by name". `[analysis]` So the
deterministic-CBOR profile nearest to option 5 **uses the mechanism option 5
refuses, for exactly the purpose option 5 needs it for.** Either the ADR carves
55799/55800 out by name as that record did for 201 — which is a coherent,
precedented narrowing — or it takes the out-of-band answer and says so. **What it
cannot do is leave the question unstated**, because the default is *stored
artifacts of ours are unidentifiable in band* and nobody has decided that.

**Cut 6 — nothing here supports option 1 or option 3, and the absence is worth
recording.** `[analysis]` Canonical S-expressions and JCS JSON have their own
out-of-band identification stories and neither is engaged by this document, which
is entirely about CBOR tags. An extraction that found a cut for option 1 here
would be reading it in. `rfc-8742`'s record is where option 1 wins on *container*
grounds; this one has nothing to add to that.

---

## 7. Source defects found

Nine. All reported, none repaired.

1. **The document's own CDDL does not match the document's own example.**
   Appendix B.1: `senml-cbor = #6.1668546929(bstr)`, justified by "Note that a
   byte string is used as the type of the tag content because a media type
   representation in general can be any byte string." But Appendix B's exception
   — "Exceptionally, when used immediately as tag content of one of the tags
   55799, 55800, or 55801, the tag content is as follows:" and then, for 55799,
   "The CBOR data item within the representation (without byte-" / "string
   wrapping)." — makes §2.2.1's tag content an **array**. B.1 is introduced by a
   cross-reference *to* §2.2.1. Vectors `V-0001` and `V-0004`.
2. **The TN formula's arithmetic is defined only in an appendix, and only by
   reference to a paywalled standard.** Appendix B: "(where +, *, / and % stand
   for integer addition, multiplication, division, and remainder as in the
   programming language C [C].)" `[C]` is ISO/IEC 9899:2018 and is a
   **normative** reference used nowhere outside an appendix, while the §4.3
   registry entry — the text IANA publishes — carries the formula and **not** the
   citation.
3. **§2's determinism claim is false in general.** §1.2. The document's single
   deliverable is a fixed byte prefix and it leaves that prefix's own encoding to
   RFC 8949 §4.2.1 by implication.
4. **Tag content is not determined by the tag number, and one case is
   undefined.** §4.3's Data Item field is a disjunction — "byte string or any
   CBOR data item (see Appendix B)" — and both of Appendix B's options for 55799
   are limited to **identity** content-coding. `[analysis]` So `TN(ct)`
   immediately inside 55799, where `ct` names a non-identity coding or a non-CBOR
   format, has **no defined tag content**. Appendix D.1's own `TN(11050)` is
   `application/json` in deflate and is routed through 55801 instead — which is
   consistent, and the document never says 55799 is unavailable for it.
5. **A reader with a known outer tag and an unknown inner tag has no defined
   behaviour.** Fixture `D-0007`. The file parses cleanly, so a reader can
   successfully read a file it cannot interpret, and the magic number's entire
   purpose fails open and silently. RFC 8949 §5.4 governs unrecognised tags in
   general; nothing here narrows it. §3 approaches it from the security side and
   states no rule.
6. **The reference consumer has no rule file.** `file(1)` appears four times
   (abstract, §1 twice, §1.2) and the abstract's claim is to define a format
   "friendly to common systems that recognize file types, such as the Unix
   file(1) command" — yet the document contains **no `magic(5)` pattern** for
   anyone to install, and §1.2 concedes the hard case: "Less ideal solutions have
   a pattern that needs to be matched, but in which some bytes need to be
   ignored.  While the Unix file(1) command can be told to ignore certain bytes,
   this can lead to ambiguities."
7. **An unresolved authoring-tool cross-reference survives into the published
   text.** Appendix D: "As with the Labeled CBOR Sequence {#sequences}, this
   choice of the tag content places the ASCII characters "CBOR" prominently into
   the header." A kramdown anchor. Editorial, and not checked against the errata.
8. **Three smaller inconsistencies.** §4.1 says "IANA has updated this tag
   registration to point to this document." and §4.2 says "IANA updated this tag
   registration to point to this document." for two otherwise word-for-word
   parallel entries. §4.3 writes the block's upper bound `0x6374ffff` where
   Appendix B writes `0x6374FFFF`. §2.3 writes the constant as `'BOR'` and
   Appendix C writes the same three bytes as `h'424F52'`.
9. **Two structural slips.** §2.2.1's lead-in closes a parenthesis it never
   opens: "of the "CoAP Content-Formats" registry [IANA.CORE-PARAMETERS])."
   And Appendix C's "The above magic number is included in the file and on the
   IPC in order to distinguish the "shutdown" command CBOR operation." refers
   **forward** — the tag it calls "above" is allocated three paragraphs later.

**Not a defect, recorded because it looks like one.** §1.2 is titled
*Requirements for a Magic Number* and contains no requirements language. That is
consistent with the whole document, which has none; it is listed in §8 as a
property of the document rather than as an error in that section.

---

## 8. The zero-keyword finding, and what it costs a reader

`bin/bcp14-count` returns **0**, and this is not a rendering artefact. Measured
over the whole 960-line source at this pass: **"BCP 14", "RFC 2119", "RFC 8174"
and "key words" do not appear at all**, so there is no requirements-language
section for the keywords to have been omitted from. Every all-capitals keyword
form occurs **zero** times.

What the document uses instead: `may` **24** times, `should` 5 plus one
sentence-initial `Should`, `must` **twice**, `required` twice, `optional` twice,
and `encouraged` / `suggested` / `needs to` throughout. **Both lower-case
`must`s matter**: one is boilerplate licence text and the other is Appendix A.2's
"care must be taken when concatenating Labeled CBOR Sequences to remove the label
from all but the first part" — the record's headline finding, carrying no force.

`[analysis]` Three consequences, and the third is the one to act on.

1. **A claim to conform to RFC 9277 is not testable.** Under
   `docs/requirements.md` §1's four-part test, nothing in RFC 9277 qualifies as a
   requirement. The record's `tags` say `evidence`, not `normative`, for this
   reason, and that label is correct.
2. **Two conformant implementations can be non-interoperable.** A reader that
   rejects a labelled file and a reader that rejects an unlabelled one are both
   conformant, and there is no clause to point at. The asymmetry behind it is
   measurable: **four** permissive statements about *removing* the envelope,
   **zero** statements about adding one, and **one** explicit warning — Appendix
   A's lower-case "requires that all programs that expect to examine that file be
   able to skip what appears to be a CBOR item with two tags nested around a
   3-byte byte string." **Tolerating absence is assumed everywhere and required
   nowhere; tolerating presence is the only thing the document asks of anyone.**
3. **The permissive statements are description, not dispensation.** With no
   requirements language, "there is no requirement that either type of envelope
   be transferred on the wire" is not a grant — it is a report that the document
   grants nothing. An ADR that cited it as permission to strip would be citing
   the absence of a rule as a rule.

---

## 9. What this extraction confirmed, refuted and narrowed in `summary.md`

The summary was written first and reviewed; FX-1 forbids extracting *from* it, so
every claim below was re-derived from `.cache/rfc-9277.txt` at this pass.

**Confirmed, mechanically:**

- **Zero BCP 14 keywords, and no requirements-language section at all.** ✔
  `bin/bcp14-count` → 0, and "BCP 14", "RFC 2119", "RFC 8174" and "key words" are
  all absent.
- **It does not define tag 55799; RFC 8949 §3.4.6 does.** ✔ §2.2 cites it as
  `[STD94]`, and the in-library IANA row for 55799 reads reference "RFC 8949".
- **It allocates 55800, 55801 and the §4.3 block.** ✔ And the block is **65,279**
  code points, carrying **65,025** reachable values — both recomputed.
- **`TN(ct) = 0x63740101 + (ct / 255) * 256 + ct % 255` makes 65,025 tag code
  points a mechanical function of the CoAP Content-Formats registry.** ✔ And the
  summary's own arithmetic checks: the image is 65,025 distinct values, none
  contains a zero byte, and the 254 unreachable allocated points are exactly the
  zero-low-byte ones.
- **Both envelopes are two nested tags, and the inner one needs an FCFS
  allocation.** ✔ §2.1, §2.2, §2.3 — and Appendix D makes it **three**.
- **The label is unauthenticated under both methods, so condition (4) is not
  discharged.** ✔ And now fixtured: `D-0003`.
- **Appendix A.2 makes concatenating labelled sequences a per-protocol
  question.** ✔ And now fixtured: `D-0004`, `D-0005`.
- **The four permissive statements about stripping, and the one warning running
  the other way.** ✔ All five located and quoted.
- **`TN(63) = 1668546880 = 0x63740140`, label `d9d9f8da63740140 43 424f52`.** ✔
  Recomputed, and the fingerprint confirmed by construction: `D-0006`.
- **Openswan is the one named deployment and its tag arithmetic checks.** ✔
  `0x4f50534e = 1330664270 = "OPSN"`.
- **`file(1)` appears four times and no `magic(5)` pattern is supplied.** ✔
- **The 12 label bytes hold only because §2.1 forces the 4-byte range, and
  RFC 8949 §3.1 admits `0xdb` for the same value.** ✔ **and extended** — see
  below.
- **Four of the twelve label bytes exist because CBOR has no zero-arity tag, and
  the "CBOR" mnemonic sits past the fingerprint.** ✔ Offsets 8–11, outside the
  8-byte fingerprint, confirmed by construction.
- **Appendix D's unresolved kramdown anchor.** ✔

**Extended, materially:**

- The summary says the inner tag could be written `db 00000000 63740212` and that
  `file(1)` would miss it. **True, and it is 1 of 30 rather than 1 of 2.** The
  enumeration in `schema/prefix-spellings.derived.txt` covers the **outer** tag
  and the **byte-string head** as well: 3 × 2 × 5 = **30** definite-length
  spellings of the 12-byte label, of which 1 is 12 bytes, 5 match the stated
  fingerprint, and **20 contain a zero byte inside the first eight** — which
  defeats §2.1's C-string advice, a consequence the summary does not reach. And
  **30 is a floor**, because an indefinite-length byte string is also admissible.
- The summary says the Openswan tag "checks". **It does, and the registry row
  says something the summary does not:** its reference is "Michael Richardson;
  Samir Hussain", **not** RFC 9277, so the document's own worked deployment did
  not take §2.1's advice about the Reference field.

**Refuted, and corrected here:**

- **`[correction]` The summary says "Two enveloping methods, each built from
  **two nested tags**" and, later, "Both methods are two nested tags".** There
  are **three** envelopes, not two: §2.2, §2.3 and **Appendix D's
  CBOR-Labeled Non-CBOR Data method**, which §1 introduces as "A third method is
  also proposed by which a CBOR format tag is prepended to identify non-CBOR
  files." The summary mentions Appendix D's tag 55801 in passing and never counts
  it as a method. It matters for us in one specific way: §5.1's table needs the
  third row, because a non-CBOR artifact of ours — a PDF, a key file — would be
  labelled by that method and not by the other two.
- **`[correction]` The summary says the document "classes COSE itself as
  "infrastructure" rather than a protocol needing a magic number" and treats that
  as a remark about implementations.** It is confirmed as a quotation and
  **refuted as a side remark**: it is load-bearing for the MD-3 mapping, because
  our export artifact *is* a `COSE_Sign1`. §5.1. The summary files it under
  *Implementations*; it belongs in the mapping.
- **`[correction]` The summary's "What `R-O-03` demands of whatever we
  substitute" says `R-O-03` "governs canonicalisation, so it does not reach a
  file header on its own terms".** That is right, and the paragraph then applies
  it anyway to rule out "our own framing". **The reasoning survives and the
  framing of it does not:** what actually rules out a private magic number is not
  `R-O-03` but the plain fact that it would make our stored artifacts
  unidentifiable by anyone who has not read our own unpublished note — which is
  §1's APK-is-a-ZIP argument applied to us. Stated that way it needs no appeal to
  a requirement about canonicalisation.

**Added at this pass, not in the summary:**

- Defects 1, 4, 5, 8 and 9 of §7 — the **CDDL that does not match the example**,
  the **undefined tag content for a non-identity content-coding inside 55799**,
  the **undefined reader behaviour for an unknown inner tag**, the three textual
  inconsistencies and the two structural slips.
- The **"ct" mnemonic**: `0x6374` is ASCII `ct`, so the whole block satisfies
  §2.1's own mnemonic suggestion in its high half, for all 65,025 values at once.
- **TN maps its domain exactly onto the block's endpoints**, and the **254
  allocated-and-unreachable** code points, which the document never mentions.
- **§2.2.1's map keys are not in RFC 8949 §4.2.1 order.**
- **Cut 5** — the `draft-mcnally-deterministic-cbor` tag-201 precedent as the
  procedural answer. The summary names the precedent; it does not draw the
  conclusion that the ADR has a coherent carve-out available.
- `state-machine.yaml`, which the summary did not anticipate: the strip/apply
  asymmetry and the concatenation hazard as **six undefined transitions**.

---

## 10. Open questions this record raises

1. **Does the ADR carve 55799/55800 out by name, or take the out-of-band
   answer?** Cut 5. The precedent for carving out exists
   (`draft-mcnally-deterministic-cbor`, tag 201). **What the ADR cannot do is
   leave it unstated**, because the default is *our stored artifacts are
   unidentifiable in band*.
2. **What identifies an exported `COSE_Sign1` of ours?** §5.1. RFC 9277 declines
   the case — COSE is "considered infrastructure" — so even accepting the two
   tags would not answer it. This is an `R-I-03` question and it has no owner.
3. **What is the rule for concatenating two of our logs?** §3.1. Appendix A.2
   delegates it with no default, and `D-0004`/`D-0005` show both answers have a
   cost. It needs a `DECISIONS-0001` row, not an ADR.
4. **If we ever write a prefix check, do we require preferred serialisation?**
   Cut 4. The answer is almost certainly yes, and it would be **ours**: RFC 9277
   does not require it and `draft-ietf-cbor-cde` is the thing to cite if we do.
5. **Is the many-encodings-of-one-value case a new instance of condition (1), or
   something the topic does not cover?** §5.3's condition-(1) row. It is the
   mirror image of the condition as written, and `rfc-8742`'s record raises the
   same shape at the *file* level. If both are real, the topic owes a sentence.
6. **Is RFC 7252 worth ingesting?** §5.4's experimental-range inference and the
   Content-Format definition both rest on it, and it is **not held here**. One
   record would close two `[unverified]` marks in this lane.

---

## 11. Provenance: what was verified in-library at this pass

Pass 1 read **only** `.cache/rfc-9277.txt` for every claim about RFC 9277 — never
`summary.md`, never another agent's output. Mechanically re-derived from the
cache: the BCP 14 count (**0** in the source, **0** across the requirement texts,
with a 3367-character reconciliation because `bin/validate` requires one at zero);
**195 of 195** requirement texts and **195 of 195** normative spans contiguous in
the whitespace-normalised source with **both ends inside their locator's
section** (0 failures, across 24 locators); **8 of 8** schema regions
byte-identical to their declared line ranges with all 8 declared digests
verifying under the stated convention and **none** matching the
with-trailing-newline variant; **4 of 4** dedent round-trips; **3 of 3** source
hex regions rebuilt from their annotated lines and found identical; **4 of 4**
CDDL slices exact; **7 of 7** derived fixtures executed; **5 of 5** `TN` values
recomputed and agreeing; **both** stated fingerprints confirmed by construction;
**247** quoted spans across the YAML artifacts and **208** across `normative.md`
checked verbatim.

**The mechanical checks caught five defects in this extraction's own work, every
one corrected in place rather than left:** a twelfth hyphenation break missed at
source lines 821/822, so one sentence had been silently healed; **two elided
quotations** (an `A.1` pair welded with an ellipsis, and an `A.2` clause); a
**healed hyphenated token** quoted as if contiguous (`self-delimiting`, the
record's own hazard); and a condition-(4) quotation with its capital changed. A
sixth was found by audit rather than by a checker and was the most dangerous:
**the first draft of `messages.yaml` cited requirement ids chosen by guess, and
30 of them resolved to the wrong statement** — not dangling, which a checker
catches, but *wrong*, which is the hazard `library#39` already recorded once
("a cross-record id that silently returns the wrong requirement"). Every
`constrained_by` was re-derived from the id table and audited line by line, and
the join was recomputed as **56 cited / 139 uncited** against a first guess of
103/92.

**One library defect found and reported, not repaired.** `bin/_yaml.py` silently
mis-parses inline flow maps: `- {id: ..., reason: ...}` returns a one-key dict
named `{id` holding the rest of the line as a string, so no tool in `bin/` can
read such a block. It also **truncates a multi-line flow sequence at the first
line**. The first bit this extraction (a `requirements_no_field_cites` block and
two `constrained_by` lists, all converted to safe forms); the second **already
affects `records/ietf/rfc-8392/distilled/protocol.yaml` lines 260 and 272 and
`state-machine.yaml` line 114**, which are not this lane's records and are
reported rather than touched.

**Verified present and quoted in-library:**
`records/iso/iana-cbor-tags/distilled/tables.yaml` (rows 55799, 55800, 55801,
`1330664270`, `1668546817-1668612095`); `records/ietf/rfc-8742` and its
`distilled/schema/registrations.txt` region `T01`;
`records/ietf/rfc-8949/distilled/design-notes.md` §3.4.6 row;
`topics/canonical-encoding.yaml`; `records/community/draft-mcnally-deterministic-cbor`.

**Not held in this library, so every claim about them is `[unverified]` here:**
`ARCH-0001`, `ARCH-0002`, `ADR-0001`, `MD-3`, `PLAN-0001`, `DECISIONS-0001`, all
`R-M-*` / `R-O-*` / `R-I-*` texts, **RFC 7252**, **RFC 6838**, **RFC 8126**,
**RFC 8428**, **RFC 9177**, **RFC 9110**, **RFC 2781**, **ISO/IEC 9899** and
**X.690**. Of these, **RFC 7252** is the one a later pass should close: §5.4's
experimental-range inference and Appendix B's Content-Format definition both rest
on it.

**No `reviewed_by` is signed, and no `profile` is declared.** Passes 2 and 3 have
not run.
