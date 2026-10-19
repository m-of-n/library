---
record: draft-ietf-cbor-serialization
kind: design-notes
title: "draft-ietf-cbor-serialization — bearing on our design"
extracted: "2026-10-16"
reviewed_by: ""
---

**Scope and provenance conventions.** Section and appendix numbers with no
document name (`§5.1`, `Appendix K.2`) are **draft-ietf-cbor-serialization-08**.
RFC 8949 is cited as `RFC 8949 §4.2.1`; where the claim about RFC 8949 is ours
rather than the RFC's, through this library's record `rfc-8949`. Other library
records are cited by id (`draft-ietf-cbor-cde`, `draft-mcnally-deterministic-cbor`,
`rfc-9052`). Our own documents are cited by id (`ARCH-0002 P4`, `MD-3`,
`R-O-03`). Three markers distinguish voices:

- unmarked prose reports **the source** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project that the sources
  do not support.

**Decision status, stated plainly.** `ARCH-0001` §7 (v0.1.1) lists **four**
DEC-002 options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3; the proposal is unmerged and ARCH-0001 still
carries DEC-002 under "Open decisions". `MD-3` (2026-09-28) **narrows** DEC-002
to option 5; `DECISIONS-0001` tier 1 item 2 records the narrowing with the words
"**Still open: a narrowing is not an acceptance, and no ADR exists**", and its
front matter says "MD-3 NARROWED DEC-002 without accepting it, so DEC-002 is
still open and no code or vector may assume an encoding." `ADR-0001` (accepted)
constrains DEC-002: "CBOR tags and COSE header parameters are IANA allocated, so
they are interchange, not native." **No DEC-002 ADR has been written**;
`DECISIONS-0001` item 4b dates it to **Oct 28** and calls it "Item 2's
instrument". Nothing below may be read as an accepted encoding decision, and
nothing below is written to agree with MD-3.

**Provenance of the source read.** `draft-ietf-cbor-serialization-08`,
L. Lundblade (Security Theory LLC), **Intended status: Standards Track**, date
line **29 July 2026**, "Expires: 30 January 2027". A CBOR **working group**
document (`draft-ietf-` prefix); its source and issue tracker are at
`https://github.com/cbor-wg/draft-ietf-cbor-serialization`. The cached bytes
hash to `a612e6c4…7112`, which matches `record.yaml`'s `content.sha256`
(retrieved 2026-09-22). `bin/bcp14-count` reports **65** BCP 14 keywords.

> **[correction]** `record.yaml` carries `date: "2026-07-30"`; the document's
> own date line is **29 July 2026**. A citation copied out of `record.yaml`
> will carry a date the document does not bear. `record.yaml` also has
> `authors: []` where the document names one author, Laurence Lundblade, and
> seven Contributors. `summary.md` is still the ingest stub ("Maturity —
> _unset_", "Digest `not fetched`"). *Record owner (S1) and pass 2.*

---

## What this document is

**Three serializations, two of them new.** Abstract: "This document defines two
CBOR serializations: "preferred-plus serialization" and "deterministic
serialization."  It also introduces the term "general serialization" to name the
complete set of all serializations defined in RFC 8949."

| name | §ref | what it is |
|---|---|---|
| **general serialization** | §3 | the name for "the complete set of all encodings standardized in Section 3 of [STD94].  The term itself was not explicitly defined in [STD94]." It is the default: §3.1, "When a CBOR-based protocol specification does not explicitly specify serialization, general serialization is the implied requirement". §2.1.2 calls defaulting to it NOT RECOMMENDED |
| **preferred-plus serialization** | §4 | shortest-form arguments, definite lengths only, shortest float preserving precision, one permitted NaN, big-number/integer unification. §4.4: "Preferred-plus serialization is defined to be the long-term replacement for preferred serialization." |
| **deterministic serialization** | §5 | preferred-plus **plus map sorting**, and nothing else. §5.2: "deterministic encoding imposes no requirements over and above the requirements for decoding preferred-plus serialization." |

**Its relation to RFC 8949 is replacement-by-restatement, not amendment.** §1.3
is explicit about the method and about why: "This document defines new
serializations rather than updating those in [STD94].  This approach enables the
serialization requirements to be expressed directly in normative [RFC2119]
language and to be defined entirely in this document.  This approach provides
clarity and simplicity for implementers and the CBOR community over the long
term." It then disclaims technical novelty: "The serializations defined herein
are formally new but largely interchangeable with the way the serializations
described in [STD94] are implemented." Note that the front page carries **no**
`Updates:` line — contrast `draft-ietf-cbor-cde`-13's "Updates: 8949 (if
approved)".

**Its relation to RFC 8949 §4.2.1 is one technical divergence, stated twice.**
§5: "Deterministic serialization is the same as described in Section 4.2.1 of
[STD94] except for the encoding of floating-point NaNs." Appendix C.5: "Note
that the prohibition of non-trivial NaNs is the sole difference between
deterministic serialization (Section 5) and Section 4.2.1 of [STD94]." The map
sort is §4.2.1's own, and the draft says so and names what it is not: §5.1 item
2, "the items in it MUST be sorted in the bytewise lexicographic order of their
deterministic encodings of the map keys.  (Note that this is the same as the
sorting in Section 4.2.1 of [STD94] and not the same as Section 3.9 of
[RFC7049] / Section 4.2.3 of [STD94].)"

> **[analysis]** The divergence is a **restriction**, not a modification. §4.1
> item 4 bars a class of values from the encoder's output; it does not change
> how any value RFC 8949 §4.2.1 permits is encoded. So the set of byte strings
> this draft's §5 admits is a strict subset of the set RFC 8949 §4.2.1 admits.
> That shape is what makes it citable under `R-O-03` without the citation
> becoming an invention — see *The R-O-03 question* below. Two decoder
> obligations are additions rather than restrictions (§4.2 item 5: leading
> zeros "MUST be ignored", an empty byte string "MUST be accepted and treated
> as the value zero"), and §4.4 lists them as two of the three differences from
> preferred serialization.

**Its relation to CDE: there is none, in either direction.** The strings "CDE"
and "Common Deterministic" **do not occur in the document**, in the normative
references, in the informative references, or in the Contributors section. The
draft defines, names and registers its own deterministic serialization without
mentioning the WG's other determinism document. This confirms the claim in
`draft-ietf-cbor-cde`'s design notes (§3, item 2) that serialization-08
"contains **no occurrence of "CDE"** at all" — checked directly against the
source, not taken from that record.

**Its relation to dCBOR: one informative citation, at the application layer.**
dCBOR appears twice: as informative reference `[I-D.mcnally-deterministic-cbor]`
(pinned at **-17, 11 February 2026**) and in Appendix B, which is about
*application-layer* determinism, not serialization: "A better solution requires
the fluid level always be encoded using the smallest representation for every
particular value. ... See the numeric reduction defined by
[I-D.mcnally-deterministic-cbor]." Wolf McNally (Blockchain Commons) and Carsten
Bormann are listed among the Contributors, and the dCBOR reference entry names
"McNally, W., Allen, C., Bormann, C., and L. Lundblade" — this draft's author is
a dCBOR co-author.

**Its relation to CTAP2 "Canonical CBOR": named once, as a conflict to avoid.**
Appendix I.2: "For example, assume protocol XYZ wraps protocol ABC.  If protocol
ABC requires Canonical CBOR as specified in Section 3.9 of [RFC7049] (e.g.,
[CTAP2] from WebAuthn) while protocol XYZ requires deterministic serialization,
Section 5, a conflict would arise." §5.1's
parenthetical rules RFC 7049 §3.9 / RFC 8949 §4.2.3 ordering out by name.

**DAG-CBOR is not mentioned at all.**

---

## What we adopt

**Deterministic serialization (§5) as the technical content of a key-centric
profile's base layer.** Its encoder rules are RFC 8949 §4.2.1's, restricted by
one; its sort is §4.2.1's bytewise-lexicographic rule, which `rfc-8949`'s
extraction already adopts as determinism row 1; and §4.1 settles four of the
fourteen decisions that extraction says RFC 8949 §4.2 leaves open — row 5
(shortest float), row 7 (NaN: exactly `0xf9 0x7e 0x00`), row 3's encoder half
(definite lengths), and the big-number seam.

**§4.1's single-NaN rule, taking the "reject" branch.** "Encoders MUST NOT
output any NaN other than the half-precision NaN 0xf9 0x7e 0x00 (sign bit clear,
most significant significand bit set, all remaining significand bits clear).
When a signaling NaN, a NaN with a non-zero payload, or a NaN with the sign bit
set is presented to an application or library for encoding, the encoder MUST
either reject it or encode it as 0xf9 0x7e 0x00." The disjunction is ours to
close: `ARCH-0002` P5 — "a failure at any level is a rejection, never a repair"
— forces the first branch. Adopting §4.1 without naming the branch would import
a licence to repair.

**§4.4's three differences from preferred serialization, especially the first.**
"Definite lengths are a requirement, not a preference." §4.4 explains the defect
this closes: "Section 3 of [STD94] states that in preferred serialization the
use of definite-length encoding is a "preference", not a requirement.
Technically that means preferred serialization decoders must support indefinite
lengths, but in reality many do not." This matters to us because RFC 8949
§4.2.1 reaches definite lengths *through* preferred serialization (Appendix C.4:
"Since Section 4.2.1 of [STD94], (Core Deterministic Encoding Requirements),
explicitly requires preferred serialization"), so a citation to §4.2.1 alone
drags in a decoder obligation we reject — `rfc-8949` determinism row 3 requires
decoder **rejection** of indefinite lengths, and `ARCH-0002` P5 forbids
accepting what we do not require. This draft is the only document we hold that
states the encoder requirement in BCP 14 language with the word "requirement".

**§5.3.3's prohibition on map-order semantics.** "Applications MUST NOT rely on
any particular map ordering, even if deterministic serialization was used. ...
The sole purpose of map sorting in deterministic serialization is to ensure
reproducibility of the encoded byte stream, not to provide any semantic ordering
of map entries." This is RFC 8949 §5.6's rule restated as a positive MUST NOT
and it binds us directly: `ARCH-0002` P4's domain-of-discourse hash is a *set*
identity, so nothing in our model may read order out of a sorted map.

**Appendix B's two-layer framing, as the name for the gap we already found.**
"For a protocol to be deterministic, both the encoding (serialization) and data
model (application) layer must be deterministic.  While deterministic
serialization, Section 5, ensures determinism at the encoding layer,
requirements at the application layer may also be necessary." This is
`topics/canonical-encoding.yaml`'s split in the source's own words, and it is
where our conditions (5) and (6) live.

**Appendix J's rule that the signed range must be pinned by the protocol.** "For
signing or hashing to work, the sender/encoder and the receiver/verifier must
operate on exactly the same range of encoded bytes, so a protocol definition
MUST define that range unambiguously." Appendix J then gives four ways and
ranks them: "byte-string wrapping is the most reliable approach because it
clearly delineates what is signed or hashed and works with every decoder". That
is exactly the construct `R-O-05` needs and that `rfc-8949`'s design notes
reached by a different route (tag 24's subject matter without tag 24).

**Appendix K.1 and K.3 as standards-track support for the separability thesis.**
K.1 on the COSE payload: "it is not special in any way and COSE imposes no
serialization restrictions on it at all.  That is, it can use any serialization
it wants.  The serialization is selected by the protocol that defines the
payload, not by COSE." K.3: "COSE places no serialization requirements on these
elements." `ARCH-0001-PROPOSAL-v0.2.0` §3.3 separates "CBOR as a **data model
and encoding**" from "COSE/CBOR-tags as a **governed type space**"; K.1 and K.3
are a WG document saying the first is genuinely free of the second on the
signing path. This is the strongest single piece of external support for option
5 in the whole document, and it is also support for option 2 (see below).

**Appendix H's name for condition (2).** "Serialization checking rejects input
which, while well-formed CBOR, does not conform to a particular serialization
rule set it is enforcing." And its guard-rail, which we should quote in P5's
rationale: "Serialization checking may enhance security in certain contexts, but
such checking is never a substitute for correct and complete CBOR input
validation. ... Decoders that fail to perform this essential input validation
are fundamentally inadequate and represent a security risk."
We adopt the *term*; we do not adopt its optionality (see *What we reject*).

**§9.1's covert-channel analysis, as the security framing for conditions (5) and
(6).** "CBOR’s serialization variants can be used as a covert channel [LAM73] to
steganographically exfiltrate data." Its list includes "Manipulating the
ordering of map entries" and "Varying the Unicode representation of text
strings". This is the first document we hold that prices non-canonical variance
as **exfiltration** rather than only as non-reproducibility.

---

## What we adapt, and how

**§2.1.1's framework-protocol rule — we take its exception, not its default.**
§2.1.1: "It is RECOMMENDED that CBOR-based framework protocols not state
serialization requirements, enabling individual uses and profiles to choose
serialization to suit their environments and constraints." Then the exception:
"There is one situation in which a framework protocol MUST require deterministic
serialization, though typically limited to a specific subset of the protocol.
This requirement arises when the protocol design requires the involved parties
to independently construct and serialize data to be hashed or signed, rather
than transmitting the exact serialized bytes that were hashed or signed."

> **[analysis]** By §2.1.1's own taxonomy — "Framework protocols are those that
> offer a set of options and alternatives, with interoperability depending on
> the sender and receiver making compatible choices.  These protocols sometimes
> make use of profiles" — `ARCH-0001` is a **framework protocol**: `ARCH-0002`
> P7 says "Authorization is a family, deployed by profile", and DEC-004 and
> DEC-007 are profile hooks. So the default advice is against stating a
> protocol-wide serialization at all, and the exception is scoped "typically
> limited to a specific subset of the protocol". Our reconstructed-bytes subset
> is `ARCH-0002` P4's domain-of-discourse hash, `R-M-11`'s "canonical digest of
> a structured description", and `DEC-003`'s key thumbprint — **not** the signed
> statement, which `R-O-05` transmits verbatim. This is a scoping finding, not
> a reason to abandon a single encoding; it says that if the ADR states
> determinism protocol-wide, it does so against this draft's recommendation and
> should say why.

**§8's `.serial` control operator — the vocabulary is useful, the controlled
value set does not fit us.** §8: "The controller (the right-hand side) MUST be
either "prefp" or "dtrm", specifying preferred-plus (Section 4) or deterministic
(Section 5) serialization, respectively." And: "New controller values for new
serializations are possible but are highly discouraged.  Standards action is
required to add them." §10 asks IANA to register `.serial` in the "CDDL Control
Operators" registry. For D4's schema this is the right spelling of the base
layer (`statement .serial dtrm`), with every option-5 restriction carried in
prose beside it — the operator has no vocabulary for them and the document
discourages minting one.

**§8's scope rule, applied to `R-O-05`'s payload.** "The scope of .serial
applies recursively through nested arrays and maps, but does not extend into
byte strings or other data items that happen to contain encoded CBOR.  Every
instance of embedded CBOR that requires specific serialization must specify it
explicitly." Appendix K.2 says the same for prose rules: "determinism
requirements do not extend into CBOR inside of byte strings.  Once CBOR data is
wrapped in a byte string, its internal encoding is treated as opaque and is not
subject to surrounding serialization constraints." Appendix I.2 goes further and
recommends the independence: "The wrapping protocol should not impose
serialization requirements on the wrapped message.  The two should be treated as
independent entities."

> **[analysis]** `R-O-05` makes the signed payload a byte string holding our
> canonical encoding. By all three statements above, our determinism rule does
> **not** reach inside that byte string by construction — it has to be stated
> separately for the payload. No document of ours states it. This is a
> one-sentence hole in `R-O-05` and it is exactly the kind of silent gap
> `R-O-03` exists to prevent: the wrapper's rules and the wrapped bytes' rules
> are two citations, not one. *Fix in the ADR or in `ARCH-0001` v0.2.0.*

**Appendix J's fourth tactic — adopted for identity, rejected for verification.**
"Another tactic is to require deterministic encoding.  The receiver then
reconstructs the signed/hashed bytes from the decoded data items rather than
accessing the received encoded CBOR." `R-O-05` forbids precisely this on the
verification path ("A verifier ... SHALL NOT canonicalize input as part of
verification"). But on the identity path there are no received bytes to keep —
`topics/canonical-encoding.yaml`: "at an identifier there are no received bytes
to verify verbatim. The digest IS produced by canonicalising." So Appendix J's
tactic 4 is what P4 does, and tactics 1–4 are the menu `ARCH-0001` §4.1 owes a
choice from for `ArtifactId`'s description mode.

**§6's "special serialization" as the declared layer for option 5's
restrictions.** §6 permits protocols to define serializations beyond the three,
including "Deterministic serialization with any or all of the above", and
recommends the shape: "A recommended approach is to define a special
serialization as preferred-plus or deterministic serialization with additional
constraints or extensions." Its worked example is a prose paragraph of the form
"Deterministic serialization MUST be used, except that …". That is the form
option 5's profile should take, and the draft's blessing of the form is what
keeps publishing it *authoring at a declared layer* rather than modifying a
cited algorithm. `draft-ietf-cbor-cde` calls the same move an "ALDR ruleset";
this draft calls it a special serialization; they are the same manoeuvre and we
should pick one name and say which document we took it from.

---

## What we reject, or must override

**§5.2 — no checking decoder.** "Decoders MUST meet the decoder requirements
described in Section 4.2.  That is, deterministic encoding imposes no
requirements over and above the requirements for decoding preferred-plus
serialization." §4.2 lists only what MUST be *accepted*; it imposes no rejection
of non-shortest arguments, of indefinite lengths, of unsorted maps, or of
non-trivial NaNs. Appendix H makes checking optional ("Some applications that
rely on deterministic serialization **may** choose serialization checking") and
§9.1's remedy is weaker still: "to require preferred-plus or deterministic
serialization and to have decoders issue a **warning** if not compliant."

> **[analysis]** This is the single most important limitation of the document
> for us. `topics/canonical-encoding.yaml` condition (2) requires that "the
> decoder REJECTS non-canonical input rather than normalising it", and
> `ARCH-0002` P5 makes rejection mandatory at all three levels. **This draft's
> deterministic serialization has no checking-decoder requirement at all, and
> says so in terms.** It is therefore exactly as silent on condition (2) as RFC
> 8949 §4.2 is, which is the gap `rfc-8949`'s extraction already recorded.
> Ranking the three profiles on condition (2), from the sources as we hold them:
> `draft-mcnally-deterministic-cbor` states it **normatively**;
> `draft-ietf-cbor-cde` states it in **Appendix C.3.2, informatively**; this
> draft states it **nowhere, deliberately**. Adopting §5 as our base means
> authoring condition (2) ourselves. That does not disqualify it — nothing else
> we might cite is better except dCBOR, which `ADR-0001` excludes from the
> native model because dCBOR registers CBOR tag 201 — but the ADR must not
> claim the citation carries it.

**§4.2's decoder tolerance, which Appendix L then contradicts.** §4.2 item 4
imposes no NaN rule on decode, yet Appendix L's `float_nan_payload.edn` says
"For preferred-plus and deterministic serialization, the decode should fail."
A conformant §4.2 decoder accepts `h'f97dff'`; the test vector says it must not.
We take the Appendix L behaviour and must say we are taking it from an example
rather than from §4.2 (see *Defects* below).

**§3's general serialization in both directions.** §3.1 makes it the default for
any protocol that does not specify, and §3.2 says the warranted scenario is "a
protocol that must accommodate highly constrained encoders, at the cost of
requiring decoders — assumed to be unconstrained — to support every possible
serialization option." We are not that protocol, and §2.1.2 agrees:
"Defaulting to general serialization is NOT RECOMMENDED". Concretely rejected on
decode: indefinite lengths, non-shortest arguments, non-shortest floats, and
big-number spellings of in-range integers — the four bullets of §3.

**§7's new tag data-model rule — accepted as sound, inapplicable to us, and
recorded because it narrows an argument of ours.** §7: "All future CBOR tag
definitions MUST NOT incorporate, modify, or otherwise affect any data types
other than the type defined by the tag itself.  A set of tags MAY affect each
other, provided that all defining authorities for those tags explicitly agree."
Tags 2 and 3 are grandfathered. Under `ADR-0001` we use no tags, so the rule
binds nothing of ours — but see *cut B* below for what it costs the argument.

**§2.1.2's headline recommendation, for the native form.** "The strategy most
highly RECOMMENDED is to normatively require preferred-plus serialization."
Preferred-plus is unsorted, so it cannot carry P4's hash. §4.3's own aside
concedes the boundary: "Note that preferred-plus is deterministic when maps are
not in use." Our statements are maps (`rfc-8949` design notes, major type 5
row), so we take §2.1.2's next sentence instead: "If a protocol does not need
to be deployed where map sorting is too expensive, requiring deterministic
serialization is also RECOMMENDED."

---

## Mapping to our decisions

### 1. The convergence question this record was ingested to answer

`topics/deterministic-cbor-profiles.yaml` asks: *"Do the emerging deterministic
CBOR profiles converge, and which one should a key-centric profile cite rather
than invent?"* It names four incompatible profiles — RFC 8949 §4.2.1 core, CTAP2
canonical, DAG-CBOR, dCBOR — and says "the CBOR WG is now writing CDE to close
it".

**Where this draft sits: it neither supersedes CDE nor feeds it. It routes
around the whole field by restating RFC 8949 §4.2.1 as a named, standards-track
serialization of its own.** The evidence, all from this source:

| profile | how this draft treats it | locator |
|---|---|---|
| RFC 8949 §4.2.1 core | **adopted wholesale, restricted once.** "Deterministic serialization is the same as described in Section 4.2.1 of [STD94] except for the encoding of floating-point NaNs" | §5; Appendix C.5 |
| CDE | **not mentioned.** Zero occurrences of "CDE" or "Common Deterministic" anywhere, including the reference lists | whole document |
| dCBOR | **relegated to the application layer.** One informative citation, for numeric reduction, inside the appendix about *data-model* determinism | Appendix B; §11.2 |
| CTAP2 / RFC 7049 §3.9 | **named as a conflict case and ruled out by name** | Appendix I.2; §5.1 item 2 |
| DAG-CBOR | **not mentioned** | whole document |

**The instrument of convergence is §8, not prose.** §8 defines `.serial` with
exactly two controllers, "prefp" and "dtrm", §10 asks IANA to register it, and
§8 closes the vocabulary: "New controller values for new serializations are
possible but are highly discouraged.  Standards action is required to add them."

> **[analysis]** That is the clearest statement of WG intent in the document and
> it is made in a registry request rather than in a position paragraph. A CDDL
> operator with two controlled values, protected by Standards Action, is a bid
> to make "deterministic CBOR" mean one thing in schema language.
> `draft-ietf-cbor-cde` §6 registers `.cde` and `.cdeseq` into the **same**
> IANA registry group. Two WG documents proposing competing control operators
> for the same concept is the state of the convergence, and this draft resolves
> it the way a working group resolves things: by writing the other one out and
> taking the shorter name.

**So the answer to the topic's first half, in one sentence:** the profiles are
converging, but by **absorption into a new standards-track baseline that is RFC
8949 §4.2.1 under a new name**, not by reconciliation of the four — and the
reconciliation document the topic names, CDE, is not cited by the document doing
the absorbing.

**Three cautions on that answer, so it is not over-read.**

1. The draft nowhere *says* it replaces CDE. Silence is evidence about the
   shape of the document, not a statement of intent, and the inference above is
   **[analysis]**. `record.yaml`'s `usefulness.reason` already takes this line —
   "The WG has not said it replaces CDE, so the edge is `see_also`, not
   `supersedes`" — and this reading supports keeping it. What would change it is
   a WG consensus call, a CDE `obsoleted-by`, or a `Replaces:` line; none is in
   this document.
2. §6 keeps the door open. "When needed, protocols may define special
   serializations beyond the three described above" — including "Deterministic
   serialization with any or all of the above". Convergence here means one
   *baseline*, not one profile.
3. **Our own documents are in tension about CDE's standing and the tension is
   not resolved here.** `topics/deterministic-cbor-profiles.yaml` says the WG
   "is now writing CDE to close" the gap; `records/ietf/draft-ietf-cbor-cde/record.yaml`
   says CDE "EXPIRED 2026-04-17 and parked ... the live work is
   draft-ietf-cbor-serialization". `draft-ietf-cbor-cde`'s design notes flag the
   same contradiction. The topic's `answer` is the stale side; it is
   `status: open` with `owner: unassigned` and should be updated when this
   record and the CDE record both land. *Topic owner.*

**The topic's second half — which one to cite — is answered next.**

### 2. The R-O-03 question

`R-O-03` (`ARCH-0001` §5.3): "Canonicalization algorithm for each concrete
encoding SHALL be cited, not invented silently."

**Start from the finding that makes the question live.** `draft-ietf-cbor-cde`'s
extraction reports that **option 5 as drafted names no canonicalisation
algorithm at all** — `ARCH-0001-PROPOSAL-v0.2.0` §3.3 says "deterministic
encoding rules" and `MD-3` says "CBOR data model", and neither is a citation.
Checked against our documents, that finding holds: §3.3's text contains no
section reference, no RFC number and no draft name for the encoding rules. So
`R-O-03` is **undischarged** for option 5, and naming a target is ADR work the
Oct 28 package cannot skip.

**The four candidates, with what each costs.**

| candidate | standing | what it gives | what it costs |
|---|---|---|---|
| **RFC 8949 §4.2.1** | STD 94. Published 2020-12. No expiry. Complete in itself | the three core constraints; the bytewise sort; stability | leaves fourteen decisions open (`rfc-8949`); permits non-trivial NaNs, which we and this draft forbid; reaches definite lengths *through* preferred serialization, whose decoder side technically requires accepting indefinite lengths (§4.4) — the opposite of our rule; states **no** decoder obligation at all |
| **draft-ietf-cbor-cde-13** | expired **2026-04-17**; intended BCP; "Updates: 8949 (if approved)" | vocabulary (`preferred-serialization` / `definite-length-only` / `lexicographic-map-sorting`); the strictly-greater sort phrasing; an informative checking-decoder appendix | expired; its added normative content is three sentences (`draft-ietf-cbor-cde` design notes); **not cited by this draft at all**; its `.cde` operator competes with `.serial` in the same IANA registry; its NaN table contains rows this draft's §4.1 forbids |
| **draft-mcnally-deterministic-cbor-18** | Internet-Draft; expires 11 February 2027 (per that record's extraction) | the only normative statement of condition (2) we hold | registers **CBOR tag 201**, which `ADR-0001` excludes from the native model; cited by this draft only informatively and only at the application layer (Appendix B); an Internet-Draft citation |
| **this draft, -08** | Internet-Draft, **Standards Track**, WG document; date line 29 July 2026; **expires 30 January 2027** | §4.2.1 restated in BCP 14 language; definite lengths as a *requirement* (§4.4); the single-NaN rule; a two-value CDDL operator; test vectors (Appendix L); §6's licence for our restriction layer | "It is inappropriate to use Internet-Drafts as reference material or to cite them other than as "work in progress."" (Status of This Memo); `.serial` and the §7 tag rule are **requests** to IANA, not registrations (§10, "please replace RFCXXXX"); §7 carries the author's own note that it "may be out of place in this document"; §5.2 disclaims any checking decoder; **expires 94 days after the Oct 28 ADR** and 106 days after this extraction |

**Recommendation to the ADR — a two-part citation, and it is the same *shape*
as `draft-ietf-cbor-cde`'s recommendation with a different second part.**

> **[analysis]** Cite **RFC 8949 §4.2.1 (STD 94)** as the normative
> canonicalisation algorithm, and name **draft-ietf-cbor-serialization §4 and
> §5 as the profile this project tracks**, carrying its one divergence
> (non-trivial NaNs prohibited; exactly `0xf9 0x7e 0x00`) as our own authored
> restriction with that draft cited as where the restriction is written down.
> Four reasons this beats the alternatives:
>
> 1. **It survives the draft.** §5 is §4.2.1 minus one class of values. If
>    serialization-08 expires, is renamed, or is replaced, the technical content
>    of the citation does not move, because the base is STD 94 and the delta is
>    ours.
> 2. **The delta is a restriction, so `R-O-03` is satisfied rather than
>    skirted.** Every byte string our encoder may emit is one RFC 8949 §4.2.1
>    permits. That is the test `DECISIONS-0001`'s standing note applies against
>    option 3 — "so what we need is a modification of JCS rather than a subset —
>    and under R-O-03 a modification is a partly invented algorithm" — and we
>    pass it where option 3 fails it.
> 3. **It is the live document, and the one with running test vectors.**
>    Appendix L is 25 example files with `general` / `preferred-plus` /
>    `deterministic` encodings for each, published at `[Examples-Repo]`. CDE
>    expired; dCBOR is excluded by `ADR-0001`. **But the corpus does not prove
>    the one rule we are buying.** Every map key in all 25 files encodes to the
>    same length within its map, so the required bytewise sort and the RFC 7049
>    length-first sort this draft rules out by name agree on all 16 map
>    encodings — an implementation of the *wrong* order passes the whole suite
>    (`examples/README.md`). Condition (1) still needs a fixture of our own with
>    keys of differing encoded length.
> 4. **It is better placed than dCBOR on the DEC-002 "library availability"
>    driver, at the profile layer where it is actually paid.** §2.2.1: "It is
>    also RECOMMENDED that CBOR libraries support deterministic serialization
>    ... This recommendation is particularly strong for environments in which
>    map sorting is easy to implement (for example, Python, Go, and Ruby)." Our
>    prototype is Python. `draft-mcnally-deterministic-cbor`'s extraction found
>    **no Python dCBOR implementation** and three of four under one maintainer;
>    this profile asks of a library only what RFC 8949 §4.2.1 asks, plus a
>    half-precision float reduction for which **Appendix D supplies the C code**.
>
> This is a recommendation to the ADR, not a decision, and it is this
> extraction's reasoning rather than anything the source or our documents state.

**Three things the recommendation does not buy, stated so the ADR does not
over-claim.**

- **Condition (2) is not carried.** §5.2 explicitly imposes no decoder
  obligation. We author it. The citation for the *idea* is Appendix H's
  "serialization checking"; the obligation is ours.
- **Condition (5), array order for set-valued fields, is not addressed
  anywhere in the document.** Not in §5, not in §6, not in Appendix B.
  `draft-ietf-cbor-cde`'s row CDE-26 records the same silence for CDE. Silence,
  not prohibition — which is what `R-O-03` needs, and is the contrast with RFC
  8785 §3.2.3.
- **Condition (6), Unicode normalisation, is raised and declined.** Appendix B:
  "Although this is not strictly a CBOR issue, deterministic CBOR protocol
  designers should be mindful of variability in Unicode text, as some characters
  can be encoded in multiple ways." That is an acknowledgement with no rule
  attached, and §9.1 then lists "Varying the Unicode representation of text
  strings" as a covert channel. **[analysis]** This is the first source we hold
  that states the condition-(6) hazard as a *security* problem rather than a
  reproducibility one, and under `ARCH-0002` P1 the hazard sits inside our type
  identifiers, because a type *is* `(defining key, text label)`.

### 3. Where this document cuts against MD-3

Required by `docs/extraction.md`: "where a source supports a different option,
or exposes a cost option 5 pays and another does not, **say so in the same
section and name the option**." Seven findings. Five cut against the narrowing
or price it, two support it. All seven name an option.

**Cut A — against MD-3, for option 2. The registered schema vocabulary fits
option 2 exactly and cannot express option 5.** §8's `.serial` admits exactly
two controllers, and §10 asks IANA to register it. Appendix K.2 establishes that
option 2's canonicalisation requirement is already `dtrm`: "This COSE
requirement is effectively equivalent to the deterministic serialization defined
in Section 5, since no floating-point NaNs are involved." So under **option 2**
("CBOR + CDDL as canonical; COSE for signed form") D4's schema writes
`my-protocol .serial dtrm` and the canonicalisation is fully specified by one
operator over two published RFCs. **[analysis]** Under option 5 the same line is
only the base: the eleven restrictions `draft-ietf-cbor-cde`'s extraction
enumerates (no major type 6, a profile integer range, no `undefined`, floats
excluded or reduced, text-string-only map keys, inline decoder checking,
canonical array order, a normalisation rule, a profile indicator, per-kind
invalid handling, bare-`bstr` embedding) have no spelling in the operator, and
§8 says minting one is "highly
discouraged" and needs Standards Action. Option 5's schema therefore carries
prose where option 2's carries a controlled term. That is a real, dated,
registry-backed cost and `MD-3` did not score it.

**Cut B — against MD-3, for option 2. §7 removes the technical half of the case
against tags and leaves only the governance half.** §7: "All future CBOR tag
definitions MUST NOT incorporate, modify, or otherwise affect any data types
other than the type defined by the tag itself." Appendix E explains what this
closes, on tags 2 and 3: "the text in Section 3.4.3 of [STD94] overrides this by
defining these encodings to be equivalent rather than distinct.  This text
therefore modifies the CBOR data model.  No other serialization requirement in
[STD94] or in this document alters the data model; this equivalence is the sole
exception."
**[analysis]** The `rfc-8949` extraction's structural complaint about major type
6 — beyond `ADR-0001`'s allocation argument — was precisely that a tag can reach
outside itself, and the integer seam is the proof. §7 forecloses that for every
future tag and even contemplates plural "defining authorities" agreeing among
themselves, which is a step towards the very thing `ARCH-0002` P1 wants.
`ADR-0001` is accepted and rules tags out on **allocation**, and §7 says nothing
about allocation, so this does not reopen it. But the ADR must not continue to
argue the technical case as if it stood: after §7, the only live objection to
**option 2**'s use of tags is the registry one, and `ADR-0001`'s own rebuttal of
private use ("private use gives escape from a registry, not a namespace") is
what has to carry the whole weight.

**Cut C — against MD-3, for option 1. On this document's own test, our signing
path needs no deterministic encoding, which deletes a reason option 5 was
preferred.** §5.3.1, titled "Not Commonly Needed for Hashing and Signing":
"Most applications do not require deterministic encoding — even those that
employ signing or hashing to authenticate or protect the integrity of data. ...
Deterministic encoding becomes necessary only when the protected data is not
transmitted as the exact bytes that are used for authenticity or integrity
verification." `R-O-05` transmits the exact bytes ("The signed payload SHALL be
the canonical encoding verbatim"), and Appendix K.1 says the same of a COSE
payload. **[analysis]** So every determinism argument in DEC-002 is being paid
on the **identity** path — `ARCH-0002` P4's domain-of-discourse hash, `R-M-11`'s
description mode, `DEC-003`'s thumbprint — and nowhere else. On that path this
document answers neither condition (5) nor condition (6), as established above.
`DECISIONS-0001`'s standing note says **option 1** (canonical S-expressions,
RFC 9804) "is now on the right side of all four of those grounds" and that what
stops it is "a far poorer data model and library availability". This finding
removes "modern deterministic-CBOR profile support" from option 5's side of that
ledger for the signing path, and leaves the two sides equally empty on the
identity path. Whether option 1 is *better* on conditions (5) and (6) is a claim
for the `rfc-9804` record and is not made here.

**Cut D — against MD-3, for option 1, on implementation cost.** Floating point
consumes §4.1 item 4, the whole of Appendix C (six subsections, C.1–C.6) and the
whole of Appendix D — pages 28 to 32, two C functions — because "While
conversion between single and double is widely supported, conversion to
half-precision is not". Appendix C.2:
"The programming languages C, C++, Java, Python and Rust do no provide APIs to
set or extract NaN payloads." **[analysis]** A conformant option-5 encoder must
implement half-precision reduction and the subnormal cases itself;
`pref_plus_single_to_half` and `pref_plus_double_to_single` are the specification
of that work. This is a cost on the DEC-002 "library availability" driver that
none of our documents has costed, and `draft-ietf-cbor-cde`'s finding 3 made the
same point qualitatively — this source quantifies it with running code. It is
also **avoidable**: RFC 8949 §5.5 permits excluding floats entirely (`rfc-8949`
open question 6), and `rfc-8949`'s design notes already recommend it for I2.
**The cut is conditional: option 5 pays Appendix C and D in full unless the ADR
excludes floats, and that exclusion is overdue.** Option named for comparison:
**option 1**, whose data model has no binary float — a claim belonging to the
`rfc-9804` record, flagged here as not established by this source.

**Cut E — against MD-3's scope, favouring no option but narrowing all of them.**
§2.1.1's default for framework protocols is *not* to state serialization
requirements, with the exception scoped "typically limited to a specific subset
of the protocol" (see *What we adapt*). `MD-3` narrows DEC-002 to a single
protocol-wide native encoding. **[analysis]** Under §2.1.1 the defensible form
of MD-3 is narrower: deterministic serialization required on the reconstructed-
bytes subset (P4 hash, `R-M-11` description digest, `DEC-003` thumbprint), and
preferred-plus or profile choice elsewhere. That is a smaller claim than MD-3
makes and it is the one a CBOR WG reviewer would recognise. It applies to
options 2, 4 and 5 alike.

**Cut F — for MD-3, and for option 5 specifically. COSE imposes nothing on the
payload, which is the separability thesis in a standards-track document.**
Appendix K.1: "COSE imposes no serialization restrictions on it at all.  That
is, it can use any serialization it wants.  The serialization is selected by the
protocol that defines the payload, not by COSE." K.3: "COSE places no
serialization requirements on these elements. ... Strictly speaking, COSE is a
framework protocol intended for incorporation into an end-to-end protocol, which
should explicitly define its serialization requirements." `ARCH-0001-PROPOSAL-v0.2.0`
§3.3's whole move is to separate "CBOR as a data model and encoding" from
"COSE/CBOR-tags as a governed type space"; K.1 and K.3 say the first is free of
the second on the signing path, from inside the CBOR WG. Recorded here rather
than only under *What we adopt*, because a findings list that only cuts one way
is as useless as one that only confirms.

**Cut G — for MD-3, on the library driver, and against
`draft-mcnally-deterministic-cbor`'s reading of it.** §2.2.1 recommends that
CBOR libraries support deterministic serialization and singles out "Python, Go,
and Ruby"; it also notes "Deterministic serialization is a superset of
preferred-plus serialization; therefore, if deterministic serialization is fully
supported, explicit support for preferred-plus serialization may be omitted."
`draft-mcnally-deterministic-cbor`'s extraction (finding 5) concluded that "the
library-availability driver has to be re-scored at the profile layer, where
option 5's advantage is much smaller than MD-3 assumed", on the evidence that
dCBOR has three of four implementations under one maintainer and none in Python.
**[analysis] That finding is correct about dCBOR and does not generalise to
option 5, because option 5 need not cite dCBOR.** Against *this* profile —
§4.2.1 plus a NaN restriction — the Python gap disappears, and MD-3's "this
keeps modern library support" survives at the profile layer. The dCBOR finding
should be read as an argument for **not citing dCBOR**, not as an argument
against option 5. This is the clearest case in the three-way comparison where
the citation target changes the score.

**The net, which is not a verdict.** MD-3's narrowing is supported on
separability (cut F) and on profile-layer library availability (cut G); it is
unsupported or paid for on schema expressibility against option 2 (cut A), on
the now-narrowed technical case against tags (cut B), on the deleted
signing-path justification (cut C), on float implementation cost (cut D), and on
protocol-wide scope (cut E). The weighing is the ADR's, not this extraction's.

### 4. A correction to a sibling record, with the evidence

**`rfc-9052`'s design notes propose an `R-O-03` citation this source shows to be
weaker than it reads.** That extraction's item 4 says: "`R-O-03` requires citing
a canonicalization rather than inventing one; RFC 8949 §4.2.1 narrowed by RFC
9052 §9 is that citation, and it is the same rule the domain-of-discourse hash
needs". Its README adds, correctly, that "§9 scopes determinism to the
`*_structure` encodings only ... and mandates no map-key ordering."

Appendix K.2 of this source completes the picture: "This COSE requirement is
effectively equivalent to the deterministic serialization defined in Section 5,
since no floating-point NaNs are involved.  It is also effectively equivalent to
preferred-plus serialization as defined in Section 4, **because the Sig_structure
contains no maps**."

> **[analysis]** So for the one structure RFC 9052 §9 governs, the COSE
> narrowing is indistinguishable from *unsorted* preferred-plus. RFC 9052 §9
> therefore contributes **no map-sorting force whatever** — and map sorting is
> the single rule `ARCH-0002` P4's hash depends on, because a domain of
> discourse is a set of schemas carried as maps. "RFC 8949 §4.2.1 narrowed by
> RFC 9052 §9" is, for our purposes, §4.2.1 doing all the work with §9 adding
> definite lengths and the duplicate-label prohibition. The citation is not
> wrong; the sentence "it is the same rule the domain-of-discourse hash needs"
> is, because the part the hash needs is the part §9 does not supply. *Flagged
> for the `rfc-9052` record owner; it does not change that extraction's other
> conclusions.*

### 5. What this changes in the Oct 28 (D5) package

`rfc-8949`'s extraction built a fourteen-row table of determinism decisions
option 5 owes. This draft settles or moves seven of them, and supplies vectors.

| `rfc-8949` row | what this draft decides | locator | vector in Appendix L |
|---|---|---|---|
| 1 · ordering | §4.2.1 bytewise, and RFC 7049 §3.9 / §4.2.3 ruled out by name | §5.1 item 2 | `map.edn`, `map_strings.edn` — six EDN orderings, one deterministic encoding |
| 2 · tags | **not decided.** The draft is tag-neutral; §7 constrains future tag *definitions* only | §7; Appendix E | `date_epoch_tag.edn`, `date_string_tag.edn` (tags present, serialization varies) |
| 3 · indefinite lengths | encoder MUST NOT (a requirement, not a preference); **decoder rejection still ours** | §4.1 items 2–3; §4.4; §5.2 | every `general-serializations` list with a `5f…`/`7f…`/`9f…`/`bf…` form |
| 4 · floats present at all | not decided — but Appendices C and D price keeping them | §4.1 item 4; Appendix D | ten `float_*.edn` files, half to double, subnormals, infinities, two NaNs |
| 5 · float shortening | shortest of double/single/half preserving precision; subnormals MUST be supported | §4.1 item 4 | `float_single.edn`, `float_half.edn`, `float_*_subnormal.edn` |
| 6 · integer-vs-float | **not decided** at the serialization layer; Appendix B points at dCBOR's numeric reduction as an application-layer answer | Appendix B | — |
| 7 · NaN | exactly `0xf9 0x7e 0x00`; encoder MUST reject or coerce | §4.1 item 4; Appendix C.5 | `float_quiet_nan.edn`; `float_nan_payload.edn` (empty `preferred-plus` and `deterministic` lists) |
| 8 · negative zero, subnormals | subnormals MUST be supported in shortest-length encoding; negative zero not separately addressed | §4.1 item 4 | `float_zero.edn` (positive zero only — no `-0.0` vector) |
| 9 · integer range | big numbers unified with major types 0/1, no leading zeros | §4.1 item 5; Appendix E | `65_bit_neg.edn`, `positive_bignum.edn`, `negative_bignum.edn` |
| 10 · duplicate keys | **not addressed.** Contrast `draft-ietf-cbor-cde` §3.3's strictly-greater phrasing, which discharges it inline | — | — |
| 11 · key equivalence | floats as map keys: NaN equivalence applies to duplicate detection but "does not apply to map sorting.  Sorting operates on the fully encoded and serialized representation" | Appendix C.4 | — |
| 12 · map key types | not restricted | — | `map.edn` (integer keys), `map_strings.edn` (text keys) |
| 13 · invalid UTF-8 | not addressed | — | — |
| 14 · per-kind invalid handling | not addressed; Appendix H describes checking as optional | Appendix H; §5.2 | Appendix L.1.3 describes how to drive a checking decoder from the vectors |

**What to take.** Appendix L's vectors are directly usable as negative fixtures:
L.1.3 ("Checking Decoder Test") specifies the construction we want — "for each
example, supply the decoder with every representation permitted under general
serialization except those allowed for the target serialization type.  Decoding
each such input must result in a conformance-checking error." That is condition
(2)'s test harness, written out, in a document that does not require condition
(2). The vectors live at `[Examples-Repo]`
(`https://github.com/cbor-wg/draft-ietf-cbor-serialization/tree/main/examples`)
and are extracted into this record's `examples/`.

**What is missing for us.** No duplicate-key vector; no invalid-UTF-8 vector; no
`-0.0` vector; no array-order vector (there cannot be one — §5 has no rule); no
Unicode-normalisation vector. Those five are ours to write and each one encodes
a rule no cited document states, so each needs a `.derived.` marker and a line
in the ADR.

---

## Open questions

Items this document cannot settle, with who must. **[beyond source]** marks ones
where this extraction had to reason past both the source and our documents.

1. **Which `R-O-03` target does DEC-002 name?** The question is live because
   option 5 as drafted names none. This extraction recommends RFC 8949 §4.2.1 as
   the algorithm with this draft's §4–§5 named as the tracked profile; the
   alternatives and their costs are tabulated above. *DEC-002 ADR — Paul,
   Oct 28.*
2. **Does the ADR cite a document that expires 30 January 2027?** Standards
   Track and WG-adopted, but an Internet-Draft whose own boilerplate says it is
   "inappropriate to use Internet-Drafts as reference material". The
   recommendation above is built so the answer can be "no" without losing the
   technical content. *Same ADR.*
3. **Condition (2) is ours to author whatever we cite.** §5.2 disclaims it;
   CDE's Appendix C.3.2 is informative; only dCBOR states it normatively and
   `ADR-0001` excludes dCBOR's tag. Where does our checking-decoder rule live —
   `ARCH-0002` P5, or the DEC-002 ADR? *mofn#72 already owns the P5 amendment.*
4. **Are we a framework protocol or an end-to-end protocol by §2.1.1/§2.1.2's
   taxonomy, and is the determinism requirement protocol-wide or scoped to the
   reconstructed-bytes subset?** **[beyond source]** The scoped form is what
   §2.1.1 recommends and it is a materially smaller claim than MD-3 makes.
   *DEC-002 ADR.*
5. **Does `R-O-05`'s signed payload get its own stated serialization rule?**
   §8, Appendix I.2 and Appendix K.2 all say determinism does not propagate into
   a byte string and must be specified explicitly for the wrapped content. No
   document of ours does. *`ARCH-0001` v0.2.0 or the ADR.*
6. **Floats in or out.** Appendices C and D are the price of "in"; RFC 8949 §5.5
   permits "out". Unresolved since `rfc-8949`'s extraction. *David, D4 schema.*
7. **Which branch of §4.1's NaN disjunction?** "the encoder MUST either reject
   it or encode it as 0xf9 0x7e 0x00." `ARCH-0002` P5 forces reject; nothing of
   ours states it. One sentence. *ADR.*
8. **Does `.serial` count as a registry dependence under `R-M-12`?** §10 asks
   IANA to register the operator, so the meaning of our own schema would depend
   on an IANA allocation. **[beyond source]** `R-M-12` names "type identifiers,
   predicate types, tags, and header parameters" — wire-level extension points —
   and a CDDL control operator is schema vocabulary, not a wire codepoint, so
   our reading is that it falls outside. It is close enough to the line that the
   ADR should say so in one sentence rather than leave a reviewer to ask. *ADR.*
9. **Update `topics/deterministic-cbor-profiles.yaml`.** Its `answer` says the
   WG "is now writing CDE to close" the §4.2 gap; this record and
   `records/ietf/draft-ietf-cbor-cde/record.yaml` both say the live work is this
   draft. `owner: unassigned`, `status: open`. *Topic owner, after pass 2.*
10. **Does the `see_also` edge to `draft-ietf-cbor-cde` stay `see_also`?** Yes,
    on this evidence — the WG has made no replacement statement and this draft
    makes none. Revisit on a WG consensus call or a CDE `obsoleted-by`.
    *Record owner (S1).*
11. **Flag to the `rfc-9052` record owner:** Appendix K.2's "because the
    Sig_structure contains no maps" weakens that record's item-4 claim that
    "RFC 8949 §4.2.1 narrowed by RFC 9052 §9 ... is the same rule the
    domain-of-discourse hash needs". See §4 above.

### Defects and ambiguities in the source itself

Places where the document does not decide something it appears to decide, or
where two of its parts disagree. Recorded rather than papered over.

12. **§4.1 item 1's shortest-form enumeration stops at `uint32_t`, and its
    general sentence is not BCP 14.** The four MUST bullets cover 0..23/-1..-24,
    24..255/-25..-256, 256..65535/-257..-65536 and
    65536..4294967295/-65537..-4294967296. There is **no fifth bullet** for the
    8-byte argument (`ai = 0x1b`), and the lead-in reads "The shortest-form of
    the CBOR argument **must** be used for all major types" in lower case. So
    for an integer, string length, array/map count or tag number of 4294967296
    or more, §4.1 contains no BCP 14 requirement at all. This is `rfc-8949`
    defect 13 inherited and made slightly worse: RFC 8949 §4.2.1's covering
    sentence is a MUST (`rfc-8949#R-0012`) where this one is not. Appendix L's
    `65_bit_neg.edn` nonetheless gives a single preferred-plus encoding
    (`h'3bffffffffffffffff'`), asserting a rule the normative text covers only
    in lower case. *Our profile must state the 8-byte case explicitly; raise
    upstream at `github.com/cbor-wg/draft-ietf-cbor-serialization`.*

13. **§3's bignum example encodes the wrong value.** §3, fourth bullet: "Big
    number representation of values that are also representable using major
    types 0 and 1 (for example, 0 can be encoded as the big number 0xc34100)."
    `0xc3` is tag 3, the *negative* bignum, whose value per RFC 8949 §3.4.3 is
    `-1 - n`; `0xc3 0x41 0x00` therefore decodes to **-1**, not 0. The
    document's own `zero.edn` gets it right, listing `h'c2420000'` and `h'c240'`
    — tag 2. An editorial slip (`c3` for `c2`), but it is in a bullet an
    implementer reads as a worked example. *Raise upstream.*

14. **§4.2 and Appendix L disagree about decoding a NaN payload.** §4.2 item 4
    states only what MUST be accepted and imposes no NaN rule, and §5.2 says
    deterministic decoding adds nothing. Yet `float_nan_payload.edn`'s note
    says: "For preferred-plus and deterministic serialization, the decode should
    fail." A decoder conforming to §4.2 may accept `h'f97dff'`; the test vector
    says it must not. The vector is the behaviour we want and the normative text
    does not require it. *This is condition (2) surfacing as an internal
    inconsistency; raise upstream and state our own rule.*

15. **§7 carries the author's own doubt that it belongs here.** The section
    opens with an editorial comment, reproduced with its line markers:
    "`// This section is new in draft-03.  The author thinks it may be out`
    `// of place in this document, but there's no other good place for it`
    `// yet.`" A normative MUST NOT
    binding all future tag registrations sits in a section its author expects to
    move. Relevant to stability scoring of any citation to this draft, and to
    cut B, which rests on §7. *Stability note for the ADR.*

16. **Appendix H is not labelled normative or informative.** Appendix I opens
    "This appendix provides non-normative guidance"; Appendix H does not say.
    It uses no BCP 14 keywords, so the reading is informative, but it is the
    only place the document describes checking decoders — the mechanism
    condition (2) needs. *Read as informative; raise upstream.*
