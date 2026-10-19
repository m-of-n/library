---
record: draft-mcnally-deterministic-cbor
kind: design-notes
title: "draft-mcnally-deterministic-cbor — bearing on our design"
extracted: "2026-10-16"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§2.3`) are **draft-mcnally-deterministic-cbor-18** (dCBOR), the only revision
read. RFC 8949 is always named. Our own documents are cited by id (`ARCH-0002
P1`, `MD-3`, `R-O-03`). Three markers distinguish voices:

- unmarked prose reports **dCBOR** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project that the sources
  do not support.

**Decision status, stated plainly.** DEC-002 in `ARCH-0001` §7 (v0.1.1) lists
**four** options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3; that proposal is unmerged and ARCH-0001 still
carries DEC-002 under "Open decisions". `MD-3` (2026-09-28) **narrowed** DEC-002
to option 5 and **did not accept it** — `DECISIONS-0001` tier 1 item 2 says so
in terms, and item 4b names the DEC-002 ADR, due Oct 28, as the instrument.
**No DEC-002 ADR exists.** `ADR-0001` (accepted) constrains DEC-002 and records
that option 2 "as originally written does not" remain on the table. Nothing
below may be read as an accepted encoding decision, and nothing below is
written to agree with MD-3.

**What option 5 actually says, quoted, because the comparison depends on it.**
`ARCH-0001-PROPOSAL-v0.2.0` §3.3 in full:

> **DEC-002, proposed additional option 5.** CBOR as the canonical encoding,
> using the CBOR data model and deterministic encoding rules, but with **no
> reliance on the IANA CBOR Tags registry and no native use of COSE header
> parameters**. Types, predicate types, and tags are identified key-relatively
> per R-M-12, carried as ordinary map entries. COSE_Sign1 and DSSE remain
> **export** envelopes under R-I-03, with the mapping from key-relative
> identifiers to registered COSE labels documented as a lossy interchange step
> in the §6 matrix.

MD-3 adds one sentence: "CBOR data model, no IANA tags, COSE as export only;
type identity is `(defining key, label)` per P1; YAML is the human form with a
canonical one-way mapping." That is the whole of option 5 as drafted. It
decides **one** thing dCBOR also decides (registry dependence, and it decides
it the other way), and is **silent** on almost everything else dCBOR decides.

> **[correction] "Reduced CBOR" is not option 5's own name for itself, and the
> data-model subtraction it implies is nowhere in an m-of-n document.** The word
> *reduced* appears in neither `ARCH-0001-PROPOSAL-v0.2.0` §3.3, nor
> `DECISIONS-0001`, nor the 2026-09-28 minute. It comes from the spike
> (`prototype/statements/rcbor.py`: "Reduced CBOR — a deterministic encoder")
> and from this library's own `docs/extraction.md`, which glosses MD-3 as
> "option 5: reduced CBOR". Option 5 as drafted subtracts exactly one thing from
> CBOR: reliance on the tag registry (which, via `ADR-0001`, makes major type 6
> interchange rather than native). **The further subtractions routinely
> attributed to it — no floats, no `undefined`, no indefinite lengths on decode,
> a bounded integer profile — are the spike's and this library's `rfc-8949`
> extraction's, not option 5's.** They are code and analysis, neither normative.
> This matters for every row of the table below that reads *silent*: the silence
> is option 5's, not an oversight in this extraction.

**What dCBOR is, structurally, and why that makes the comparison asymmetric.**
dCBOR and option 5 are different *kinds* of statement. §2 ¶5: "dCBOR places no
direct requirement on what subset of CBOR is implemented." dCBOR constrains
**how you encode whatever you use**; it does not constrain **what you may use**
(the two exceptions are §2.6's simple values and §2.1's indefinite lengths).
Option 5 is the reverse: a data-model subset rule that is silent on encoding
beyond "deterministic encoding rules". **[analysis]** They therefore compose
rather than compete — a profile can be dCBOR's encoding discipline applied to
option 5's data model — and the table below reads *silent* in most rows not
because option 5 disagrees but because it is not making statements of that kind.
That composition is the only honest way to read "option 5 cites dCBOR", and §2
¶2 licenses it: "The rules specified here do not "fork" CBOR: A dCBOR
implementation produces well-formed, deterministically encoded CBOR according to
[RFC8949], and existing CBOR decoders will therefore be able to decode it."

---

## What we adopt

**The decoder-side obligation, stated as a normative MUST for every rule — this
is the one thing in the document we could not get anywhere else.** §1: these
requirements "go beyond, including requiring that dCBOR decoders validate that
encoded CBOR conforms to the requirements of this document." Every subsection of
§2 carries a paired decoder rule: reject indefinite lengths (§2.1), validate and
reject non-preferred serialization (§2.2), validate and reject unsorted keys
(§2.3), reject duplicate keys (§2.4), reject non-conforming floats (§2.5), reject
other major-type-7 values (§2.6), reject non-NFC text (§2.7).

This is **condition (2)** of `topics/canonical-encoding.yaml` — "the decoder
REJECTS non-canonical input rather than normalising it" — written down. That
topic records it as "the one nobody writes down", and closes with: "RDFC is now
the THIRD ratified canonicalisation specification this topic has read that
defines an encoder and leaves the decoder's obligation unstated, after RFC 8949
§4.2 and RFC 9804. That is a pattern rather than three coincidences."

> **[analysis] dCBOR breaks that pattern, and it is the only document the
> library holds that does.** This is a correction to the topic's
> generalisation, not a contradiction of it: the three it names are *ratified*
> and dCBOR is not, so "no ratified specification writes condition (2) down"
> survives intact while "nobody writes it down" does not. The consequence for
> `R-O-03` is concrete and favourable to MD-3: under option 5, condition (2)
> can be **cited** rather than asserted from our own `rcbor_decode.py`. It is
> the strongest single argument this record supplies for citing dCBOR.

**§2's recursive conformance rule.** §2 ¶4: "A CBOR data item is considered to
conform to dCBOR only if every CBOR data item nested within it, recursively
(including array elements, map keys and values, and the contents of tagged data
items), also conforms to the narrowing rules in this section." Option 5 states no
conformance rule at all. **[analysis]** We need one, and the recursion is not
optional for us: `ARCH-0002` P4 hashes a *set of schemas*, so a non-conforming
item nested four levels inside one schema changes the domain-of-discourse hash.
Adopt the sentence substantially as written.

**§2.1 definite lengths, §2.2 preferred serialization, §2.3 bytewise
lexicographic map key order, §2.4 duplicate-key prohibition.** These are RFC
8949 §4.2.1's core deterministic encoding requirements restated, and option 5
already inherits them through "deterministic encoding rules". Adopting them from
dCBOR changes nothing on the encoder side; what it adds is the decoder half
above.

> **[analysis] §2.3 and §2.4 are not redundant, and the pair matters to us.**
> "Bytewise lexicographic order" alone permits *equal* adjacent keys; §2.4 is
> what makes the ordering strict. Our own decoder collapses the two —
> `DECODE-FINDINGS.md`: "Duplicate keys come free. *Strictly* ascending rejects
> equality as a special case, so one comparison enforces both rules." dCBOR
> states them separately and therefore admits a conformant decoder that checks
> order non-strictly and duplicates not at all. If we cite dCBOR we should say
> we implement §2.3 as *strictly* ascending, which satisfies both in one
> comparison.

**§2.6's restriction of major type 7 to `false`, `true`, `null` and the
floating-point values.** §2.6 (1): encoders "MUST NOT encode major type 7 values
other than false, true, null, and the floating point values." This answers open
question 3 of this library's `rfc-8949` design notes — whether a strict "basic
generic data model" reading strips our booleans — in the same place and the same
way that extraction's **[analysis]** proposed: keep 20/21/22, drop 23. §8.4
gives the argument, and it is ours as well: the unassigned code points' "semantics
are officially undefined, and they cannot simply be used as application-defined
values without risking interoperability issues."

**§8.2's exclusion of `undefined`, on a reason stronger than our own.** §8.2
chooses `null` "as the sole representation of a placeholder for an absent value".
`ARCH-0002` P5 already excludes simple value 23 because RFC 8949 §5.7 offers it
as an encoder *substitute* for an item with an encoding problem, and "a failure
at any level is a rejection, never a repair." §8.2 adds a data-modelling reason
that stands even where no repair is in question. Both belong in the ADR; they are
independent arguments for the same exclusion.

**§5's threat statement, which is `ARCH-0002` P4's threat in the source's own
words.** §5: "Vulnerabilities regarding dCBOR will revolve around whether an
attacker can find value in producing semantically equivalent documents that are
nonetheless serialized into non-identical byte streams." **[analysis]** That is
condition (1) and P4's hash-as-identity failure stated as an attack by a third
party, and it is worth quoting in the ADR for exactly that reason: the project's
claim that canonical serialization is on the critical path for the *semantic*
layer (`ARCH-0002` P4: "DEC-002 and R-O-05 constrain DEC-007 directly. They are
one problem, not two") is not idiosyncratic to us.

---

## What we adapt, and how

**§2.7 NFC — the only answer to condition (6) any document we hold supplies, and
it needs splitting in two before we can take it.** §2.7 (1): encoders "MUST only
emit text strings that are in NFC." §2.7, decoder rule: "MUST reject any encoded
text strings that are not in NFC."

`topics/canonical-encoding.yaml` states condition (6) as: "Text that is
load-bearing for identity has a declared Unicode normalisation rule, or an
explicit refusal to normalise together with rejection of unnormalised input."
Under `ARCH-0002` P1 a type *is* `(defining key, label)`, so a text label is
load-bearing for identity and two normalization variants are two types,
silently. `DECISIONS-0001`'s standing note on item 2 records conditions (5) and
(6) as "reachable by no candidate and stated in no document of ours."

dCBOR states (6). It takes the **normalise** branch, where the topic's preferred
route — citing RDFC-1.0 §4.4.3's "not subject to any normalization" — is the
**refuse-to-normalise** branch. Both are citation-compatible under `R-O-03`;
they are not interchangeable.

> **[analysis] "MUST only emit NFC" does not say whether the encoder rejects
> non-NFC input or rewrites it, and the difference is the whole of the risk.**
> Read as *rewrite*, canonicalisation becomes lossy at authoring time: NFC is
> idempotent but not information-preserving on first application — the
> `canonical-encoding` topic's own phrase is "stable on re-application, lossy on
> application" — and the worked hazard is in that topic's answer, where
> transcribing test vectors "corrupted U+FB33 HEBREW LETTER DALET WITH DAGESH,
> which has a canonical decomposition that an ordinary normalising layer applies
> silently." U+FB33 is composition-excluded, so an NFC pass turns it into
> U+05D3 U+05BC and never turns it back. A `(key, label)` pair authored with
> that label becomes a *different type* after the encoder runs. Read as
> *reject*, the encoder is safe and the obligation to normalise moves to the
> application, which is exactly where `R-O-05` puts canonicalisation
> ("Canonicalization happens once, at authoring time, on trusted input").
> **Our adaptation: take §2.7's decoder rule verbatim, and take the encoder rule
> as reject-rather-than-rewrite, saying so explicitly because the source does
> not.** This is the single most consequential sentence in these notes for the
> identity path.

**§2.5 Numeric Reduction — adopt-or-vacate, and the choice is forced by a
decision option 5 has not taken.** §2.5 (1): an implementation supporting floats
"MUST check whether floating point values to be encoded have the numerically
equal value in DCBOR_INT = [-2^63, 2^64-1]. If that is the case, it MUST be
converted to that numerically equal integer value before encoding it." §2.5 (2):
"MUST reduce all encoded NaN values to the quiet NaN value having the half-width
CBOR representation 0xf97e00."

§2 permits an application that uses no floats to ignore all of this: "there is no
requirement that dCBOR implementations support floating point numbers ... when
they are used with applications that do not use them." Our spike excludes floats
outright (`rcbor.py`: "no floats"), and the `rfc-8949` extraction's open question
6 leaves "floats in or out of option 5" undecided, gated on `ARCH-0001` §4.1
value scales.

> **[analysis] If floats are out, dCBOR's hardest rule costs us nothing and
> option 5 is dCBOR-compatible on this row by vacuity. If floats are in, dCBOR
> and the recorded reading of option 5 disagree about the *data model*, not
> about serialization.** This library's `rfc-8949` design notes read option 5 as
> declaring "**no** cross-type value equivalences, so §5.6.1's generic-model
> distinctness holds unmodified (integer 1 ≠ float 1.0 ≠ simple value 1)". §8.1
> answers the identical question the opposite way: "If two numeric values are
> semantically equal, should they be encoded identically? dCBOR answers "yes" to
> this question, and Numeric Reduction is the mechanism by which this is
> achieved." **The practical consequence is that the float decision stops being
> a loose end and becomes a precondition for citing dCBOR at all** — it moves
> `rfc-8949` open question 6 onto the Oct 28 critical path, where nothing
> currently puts it.

> **[analysis] How dCBOR gets condition (1), and what it pays.** Condition (1) is
> "the encoding is INJECTIVE over the values it encodes". dCBOR satisfies it not
> by restricting encodings but by **changing the domain**: §2.5's final paragraph
> defines "the dCBOR numeric model" and quotients RFC 8949's basic generic data
> model by numeric equality, so 2 and 2.0 are not two values with one encoding
> but one value. The price is stated by the source itself, in §2.5's indented
> note: "Numeric Reduction means that some maps that are valid CBOR cannot be
> reduced to valid dCBOR maps, as Numeric Reduction can result in multiple
> entries with the same keys", with Figures 1 and 2 as the worked case. So the
> encoding function is **total over dCBOR's model and partial over CBOR's**, and
> the partiality lands on maps with numeric keys. For us this is survivable twice
> over — `rcbor.py` excludes floats, and the `rfc-8949` extraction's determinism
> row 12 restricts map keys to text strings per RFC 8949 §5.6 — but a canonical
> form that must be *total* over our schema has to say which escape it is taking,
> and the ADR should state it rather than inherit it.

**§2.5's tagged/untagged separation — adapt by vacuity, and note the word
collision.** §2.5 final paragraph: "two tagged data items are equal in dCBOR only
if both their tag numbers and their enclosed CBOR data items are equal, and no
tagged data item is ever considered numerically equal to an untagged data item."
Under option 5 there are no tags, so the rule has nothing to range over.
**[analysis]** Record the terminology collision while we are here: `ARCH-0001`
§4.1's `Tag` is "Authorization language value; opaque at this layer except for
defined intersection" and has nothing to do with CBOR major type 6. Every
sentence in an ADR that says "tag" needs to say which.

**§3's CDDL control operators — usable where tag 201 is not.** §3: "The control
operators .dcbor and .dcborseq are exactly like .cbor and .cborseq as defined in
[RFC8610] except that they also require the encoded data item(s) to conform to
dCBOR." §6 Table 2 registers both in IANA's "CDDL Control Operators" registry.
**[analysis]** These are registry-allocated identifiers, so the reflex is to
refuse them under `ADR-0001`. The refusal would be wrong, and the reason is worth
writing down because it is the cleanest available statement of where the
no-registry rule **stops**: `ADR-0001` scopes R-M-12 to "type identifiers,
predicate types, tags, header parameters" — things that appear *in the bytes a
verifier authenticates*. A CDDL control operator appears in a schema document,
never on the wire. `.dcbor` is therefore available to our `distilled/schema/`
artifacts and to any CDDL we publish, while tag 201 is not available to our
encoder. If the ADR does not draw that line, the next reader will draw it
somewhere arbitrary.

---

## What we reject, and why

**Tag 201 (§3, §6 Table 1) as the conformance marker.** §3: "Tag 201 (Section 6)
is defined in this specification as a way to declare its tag content to conform
to dCBOR at the data model level and the encoded data item level." §6: "IANA
**has** registered the following CBOR tag in the "CBOR Tags" registry" — present
tense, allocation already made, `#201 | (any) | enclosed dCBOR`. This is
precisely what option 5 excludes and what `ADR-0001` settles: "CBOR tags and COSE
header parameters are IANA allocated, so they are interchange, not native." See
*Where dCBOR cuts against MD-3*, finding 1 — rejecting it is not free.

**§8.5's tag escape hatch.** "Tags provide a useful "escape hatch" for
applications that need to use data items not covered by dCBOR. For example,
dCBOR applications can freely use Tag 2 or Tag 3 to encode bignums ... Similarly,
the rare applications that need to convey nontrivial NaN values can use Tag 80,
81, or 82." Under option 5 there is no escape hatch, so out-of-model data must be
either forbidden or carried as structure. For us the loss is small and already
costed in the `rfc-8949` design notes: `ARCH-0001` §4.1 makes `Key` and `KeyId`
byte-valued, so bignums are not needed, and nontrivial NaN is moot if floats are
out. §8.5 sits in a section the document marks "This section is non-normative"
(§8 preamble), which is what keeps excising it a *scoping* of the citation rather
than a *modification* of the algorithm — the distinction `R-O-03` turns on.

**dCBOR as an answer to the convergence question.** The string "CDE" does not
occur in the document, nor does any reference to `draft-ietf-cbor-cde` or
`draft-ietf-cbor-serialization`. At -18 (10 August 2026) it narrows RFC 8949
§4.2 directly and positions itself against nothing else. So it cannot answer
`topics/deterministic-cbor-profiles.yaml`'s question — "Do the emerging
deterministic CBOR profiles converge" — and this record is evidence about only
one of the four profiles that topic names.

**§8.6's refusal to specify an API, as a model for us.** "the authors have chosen
to not widen the scope of this document. We direct the reader to the several
existing dCBOR implementations for guidance on API design." **[analysis]** Taken
as a precedent this would be a mistake for us, because the single open question
`#73` was spun up to answer is a *processing-model* question — whether
canonicality is decidable single-pass on decode — and a profile that specifies
only outcomes leaves it open. `DECODE-FINDINGS.md` answers it for our rules, not
for dCBOR's; see *Open questions* 5.

---

## Mapping to our decisions

### 1. Rule by rule against option 5

Issue library#39's instruction for this record. **23 rows: the 15 numbered
encoder/decoder rules of §2.1–§2.7, plus 8 rule-shaped statements elsewhere in
the document.** The verdict column describes **option 5 as drafted, relative to
dCBOR** — not the spike and not this library's `rfc-8949` reading, both of which
are noted separately where they differ. "Silent" is the honest answer wherever
option 5's three sentences make no statement of that kind; see the
**[correction]** in the preamble.

| # | dCBOR rule | § | option 5 as drafted | verdict |
|---|---|---|---|---|
| 1 | Conformance is recursive through array elements, map keys, map values and tag content | §2 ¶4 | no conformance rule at all | **silent** |
| 2 | Output is well-formed, deterministically encoded RFC 8949 CBOR; existing decoders can read it ("do not "fork" CBOR") | §2 ¶2 | "using the CBOR data model and deterministic encoding rules" implies it | **silent (same by implication)** |
| 3 | "dCBOR places no direct requirement on what subset of CBOR is implemented" | §2 ¶5 | *is* a subset rule: no reliance on the tag registry, hence via `ADR-0001` no native major type 6 | **stricter** |
| 4 | Encoder: definite-length byte strings, text strings, arrays, maps only | §2.1 (1) | inherits RFC 8949 §4.2.1 | **same** |
| 5 | Decoder: MUST reject indefinite-length items | §2.1 (2) | silent; RFC 8949 §4.2 makes decoder checking optional. Spike rejects | **silent (spike same)** |
| 6 | Encoder: preferred serialization only | §2.2 (1) | inherits RFC 8949 §4.1 / §4.2.1 | **same** |
| 7 | Decoder: MUST validate preferred serialization and reject | §2.2 (2) | silent. Spike rejects, in `_head()` | **silent (spike same)** |
| 8 | Encoder: map keys in bytewise lexicographic order | §2.3 (1) | inherits RFC 8949 §4.2.1 | **same** |
| 9 | Decoder: MUST validate key order and reject | §2.3 (2) | silent. Spike rejects, strictly ascending | **silent (spike same, and stricter — strict ordering)** |
| 10 | Encoder: MUST NOT emit maps with duplicate keys | §2.4 (1) | silent as drafted; RFC 8949 §5.6 obliges *some* rule and `ARCH-0002` P5 forces rejection | **silent (P5 same)** |
| 11 | Decoder: MUST reject maps with duplicate keys | §2.4 (2) | silent. Spike rejects | **silent (spike same)** |
| 12 | Encoder: integral floats numerically equal to a value in `DCBOR_INT = [-2^63, 2^64-1]` MUST be converted to that integer | §2.5 (1) | silent. Floats undecided (`rfc-8949` OQ6); spike excludes floats, which §2 ¶5 permits | **silent — vacuous if floats are out; in direct conflict with the recorded "no cross-type equivalence" reading if floats are in** |
| 13 | Encoder: all NaN values MUST be reduced to `0xf97e00` | §2.5 (2) | silent | **silent (vacuous if floats are out)** |
| 14 | Decoder: MUST reject floats not encoded per §2.5 | §2.5 (3) | silent. Spike rejects *every* float | **silent (spike stricter)** |
| 15 | The numeric model is untagged major types 0/1/7 only; no tagged item is ever numerically equal to an untagged one | §2.5 ¶final | no tags exist to range over | **stricter by vacuity** |
| 16 | Encoder: MUST NOT emit major type 7 other than `false`, `true`, `null`, floats | §2.6 (1) | silent as drafted; this library's `rfc-8949` reading admits only simple values 20/21/22 | **silent (our reading: same, or stricter if floats are out)** |
| 17 | Decoder: MUST reject other major type 7 values | §2.6 (2) | silent. Spike rejects | **silent (spike same)** |
| 18 | Encoder: MUST only emit text strings in NFC | §2.7 (1) | **silent.** Condition (6) is stated in no document of ours (`DECISIONS-0001` standing note); `rcbor.py` does `v.encode("utf-8")` with no normalization | **silent — and this is the gap** |
| 19 | Decoder: MUST reject text strings not in NFC | §2.7, decoder rule (mis-numbered "1.") | silent. `rcbor_decode.py` validates UTF-8 via `raw.decode("utf-8")` and imports no `unicodedata` | **silent — the one dCBOR rule our decoder cannot satisfy as written** |
| 20 | Tag 201 declares its content to conform to dCBOR "at the data model level and the encoded data item level"; registered in the IANA CBOR Tags registry | §3; §6 Table 1 | "**no reliance on the IANA CBOR Tags registry**"; `ADR-0001` makes tags interchange, not native | **conflict** |
| 21 | CDDL control operators `.dcbor` / `.dcborseq`, registered in the IANA CDDL Control Operators registry | §3; §6 Table 2 | silent. R-M-12's scope is wire identifiers, not schema-language ones | **silent (available to us — see *What we adapt*)** |
| 22 | Decoder MUST reject the eleven valid-CBOR encodings of Table 4, including the 65-bit negative integers `-2^63-1` and `-2^64` | §7.2 (the table preamble carries the MUST) | silent; `rfc-8949` determinism row 9 leaves the integer profile range open. `rcbor.py` `_head()` **emits** `3bffffffffffffffff` | **looser** |
| 23 | Tags are the escape hatch for data items dCBOR does not cover — Tag 2/3 for bignums, Tag 80/81/82 for nontrivial NaN *(non-normative, §8 preamble)* | §8.5 | no tags at all | **stricter / conflict** |

**Reading the table.** Option 5 is the **same** as dCBOR in 3 rows (4, 6, 8 — the
RFC 8949 §4.2.1 core it already inherits), **stricter** in 3 (3, 15, 23),
**looser** in 1 (22), in **direct conflict** in 1 (20), conditionally in conflict
in 1 (12), and **silent** in the remaining 14. **[analysis]** The silence is the
finding. A profile that decides one question out of twenty-three is not yet a
profile, and `topics/deterministic-cbor-profiles.yaml` names the consequence
exactly: "The live risk is inventing a fourth-and-a-half profile by accident,
which is what the rcbor spike currently is."

**The spike measured against dCBOR, since that is what the risk is about.**
`rcbor.py` plus `rcbor_decode.py` are **not** dCBOR, and neither contains the
other:

- **Stricter than dCBOR** in two places, both harmless: no tags at all (rows 3,
  15, 23), and no floats at all (rows 12–14) — the second of which §2 ¶5
  expressly permits as an application subset, so it is conformance, not
  divergence.
- **Looser than dCBOR** in exactly two places, both silent:
  1. **NFC is not checked** (rows 18, 19). `rcbor.py` encodes `v.encode("utf-8")`
     and `rcbor_decode.py` returns `raw.decode("utf-8")`, which validates UTF-8
     and nothing else.
  2. **65-bit negative integers are emitted** (row 22). `_head(MAJOR_NINT, -v-1)`
     accepts any `n < 2^64`, so `-2^64` encodes as `3bffffffffffffffff` — byte
     for byte the fourth entry of Table 4, which dCBOR requires a decoder to
     reject.

> **[analysis]** Two edits bring the spike inside dCBOR: a normalization check
> and a lower bound on negative integers. That is a small, checkable, finite
> list, and it is worth stating in those terms because "we are accidentally
> inventing a profile" is otherwise unfalsifiable. It also prices the accident:
> the integer bound is three lines; the NFC check is a Unicode dependency inside
> a 136-line decoder, which is finding 3 below.

### 2. Can option 5 cite dCBOR rather than invent its own rules?

`R-O-03` (`ARCH-0001` §5.3): "Canonicalization algorithm for each concrete
encoding SHALL be cited, not invented silently."

**Answer: mostly yes — and the "mostly" is three specific items, none of which is
a divergence in dCBOR's algorithm.** Stated precisely:

1. **The encoder rules can be cited whole.** Rows 4–17 and 22 are either rules
   option 5 already inherits from RFC 8949 §4.2.1 or rules option 5 is silent on
   and has no reason to contradict. Nothing in §2.1–§2.6 is incompatible with a
   data model that excludes major type 6, because §2 ¶5 explicitly declines to
   constrain the subset.
2. **The decoder rules can be cited whole, and are available nowhere else.** See
   *What we adopt*. Citing dCBOR for condition (2) is strictly better than
   asserting it from `rcbor_decode.py`.
3. **Three items force a stated divergence, and only the first is a real
   exclusion:**
   - **Tag 201 and §8.5's escape hatch (rows 20, 23) must be excluded by name.**
     This is an exclusion of a *declaration mechanism* and of a *non-normative
     recommendation*, not of a canonicalisation rule. **[analysis]** On the
     distinction `topics/canonical-encoding.yaml` makes the decisive one —
     "Prohibited versus absent is the decisive distinction" — excluding dCBOR's
     tag affordances leaves the algorithm a **subset**, not a modification,
     because dCBOR never *requires* a tag anywhere. That is the opposite of
     option 3's position, where RFC 8785 §3.2.3 **prohibits** what we need.
     `R-O-03` is satisfied.
   - **Condition (5) is not closed by citing dCBOR.** There is no array-order
     rule anywhere in the document: §8 Table 5 enumerates nine variability
     sources and array element order is not among them. **[analysis]** This is
     additive silence, not prohibition, so a bytewise set-ordering rule layered
     on top does not modify dCBOR — and the `canonical-encoding` topic has
     already settled that the addition is itself a citation rather than an
     invention: "its shape is ratified twice over, by RFC 8949 §4.2.1 for map
     keys and by RDFC-1.0 §5 for set members. We cite a construction rather than
     invent one." So the honest form of the citation is **"dCBOR §2, plus one
     stated addition for set-valued arrays"**, and that form is `R-O-03`-clean.
   - **The integer profile range must be restated normatively (row 22).** dCBOR
     rejects 65-bit negatives only in §7.2's table; §2 contains no rule that
     forbids them. See *Defects* 9. Citing §7.2 for this is citing an appendix
     for something the normative section omits, which is thin.
4. **The one thing citation cannot fix is standing.** The document's own Status
   of This Memo: "It is inappropriate to use Internet-Drafts as reference
   material or to cite them other than as "work in progress."" It expires
   **11 February 2027**. Finding 4 below.

**So: option 5 can cite dCBOR §2 rather than invent, subject to three named
carve-outs and one expiry.** That is a materially better `R-O-03` position than
MD-3 has today, where option 5 cites nothing at all and the spike is the
specification.

### 3. Where dCBOR cuts against MD-3

Required by `docs/extraction.md`: "where a source supports a different option, or
exposes a cost option 5 pays and another does not, **say so in the same section
and name the option.**" Six findings. The sixth runs the other way and is
recorded with the rest so the balance is visible.

**Finding 1 — dCBOR's own conformance marker is a registry-allocated tag, and
option 5 must refuse it and then replace it. Option favoured: option 2.**
§3 and §6 Table 1: tag 201 exists, is registered, and is how dCBOR says "this
content is dCBOR". `topics/canonical-encoding.yaml` condition (4) requires that
"The encoding profile is named by an authenticated type indicator carried inside
the signed bytes", and the attack notebook makes it load-bearing: "condition (1)
has to hold over the (profile, bytes) PAIR, not over bytes under one profile."
**dCBOR supplies condition (4) — with exactly the mechanism option 5 exists to
refuse.** Under option 2 (CBOR + CDDL canonical, COSE for the signed form) tag
201 is simply available and condition (4) costs nothing. Under option 5 the
profile indicator must be rebuilt key-relatively per `ARCH-0002` P1, with no
registry entry, no implementation and no interoperability, and it has to be
designed before Oct 28 because `R-O-05` puts it inside the signed bytes.
**[analysis]** `ADR-0001` has already ruled that option 2 as originally written
is off the table, so this is a **cost to record, not an option to revive** — but
it is a cost MD-3 did not score, and it is the clearest instance in the document
of the general pattern that the registry buys something real.

**Finding 2 — dCBOR's answer to out-of-model data is "use a tag", so citing it
means excising its own stated escape route. Option favoured: option 2.**
§8.5 names Tag 2/3 for bignums and Tag 80/81/82 for nontrivial NaN. Option 5
forecloses all of them. The *substantive* loss for us is near zero (`ARCH-0001`
§4.1 makes `Key`/`KeyId` byte-valued; nontrivial NaN is moot without floats), and
§8 is non-normative so the excision does not modify the algorithm. The residual
cost is specificational: every future "we need a data item dCBOR does not cover"
has an answer under option 2 and no answer under option 5 except "add a map
entry", which the `rfc-8949` extraction already costs at "one to two orders of
magnitude per type reference" against RFC 8949 §1.1 objective 2.

**Finding 3 — dCBOR answers condition (6), and the answer puts a Unicode
normalization dependency in the decoder. Option favoured: option 1.**
§2.7's decoder rule requires rejecting non-NFC text. That is the answer no
candidate was supposed to have. But it falls on the **decoder**, and
`rcbor_decode.py` is 136 lines that import nothing. A normalization check needs
Unicode tables (`unicodedata` and its data, ICU, or an embedded table) in the
component that must run on untrusted input and, per `ARCH-0002` P5, must reject
rather than repair. **[analysis]** Option 1 (canonical S-expressions, RFC 9804)
answers condition (6) by **absence**: its model is byte strings, so there is no
Unicode normalization question to decide, and the `canonical-encoding` topic
already records the refuse-to-normalise branch (RDFC §4.4.3) as the
citation-compatible route and PAE-style length-prefixed framing as "a second
route to condition (1) ... the one RFC 9804's verbatim form takes too." So dCBOR
does not merely leave option 1 ahead on condition (6) — it **prices** option 5's
answer, and the price is a Unicode dependency on the hot path plus the U+FB33
mutation hazard described under *What we adapt*. `DECISIONS-0001`'s standing note
says the evidence moved after the narrowing and that option 1 is "on the right
side of all four grounds"; this is a fifth data point on the same side.

**Finding 4 — citing dCBOR means citing an expiring individual draft, which is
the third ground against option 3 applied to option 5. Option favoured: option
1.** `topics/canonical-encoding.yaml`'s third ground for withdrawing option 3 is
about what you are actually citing: "Citing RFC 8785 means citing three
artifacts, one of them an edition of an annually revised standard. Citing RFC
8949 §4.2.1 means citing STD 94, complete in itself. That is the `R-O-03`
argument, and it is better than the one from standing." Apply it here. Option 5's
citable targets are (a) RFC 8949 §4.2.1 alone, which is STD 94 and complete in
itself but leaves fourteen decisions open and answers neither condition (5) nor
(6); or (b) §4.2.1 plus dCBOR, which answers (2) and (6) but adds a document
whose own boilerplate says "It is inappropriate to use Internet-Drafts as
reference material or to cite them other than as "work in progress."" and which
expires 11 February 2027. **[analysis] No single citable document gives option 5
what it needs.** Option 1 cites one published RFC that is complete for its own
encoding. This is the `R-O-03` ground cutting *inside* option 5, between two
citation targets, and MD-3 scored neither. The mitigation — cite
`draft-ietf-cbor-cde` instead, once it is read — is the open half of
`topics/deterministic-cbor-profiles.yaml`, and dCBOR-18 cannot help with it
because it does not mention CDE.

**Finding 5 — the library-availability driver has to be re-scored at the profile
layer, where option 5's advantage is much smaller than MD-3 assumed. Option
favoured: narrows option 1's deficit.** DEC-002's drivers (`ARCH-0001` §7) are
"library availability, SCITT alignment, SPKI fidelity, human debug", and
`ARCH-0001-PROPOSAL-v0.2.0` §3.3 argues for option 5 on the first: "This keeps
modern library support". That claim is true of **CBOR** and is not evidence about
**dCBOR**. §4 lists four implementations: Swift (§4.1), Rust (§4.2) and
TypeScript (§4.3) — all three with "Primary Maintainer: Wolf McNally" — and Ruby
(§4.4), Bormann's, whose coverage line reads "Checking of dCBOR - exclusions not
yet implemented". §4's own RFC 7942 boilerplate disclaims verification: "no
effort has been spent to verify the information presented here". **There is no
Python implementation**, and our prototype is Python. **[analysis]** Three of
four implementations under one maintainer is the same weakness the
`canonical-encoding` topic held against RFC 8785
("four-of-five-in-one-repository", against RDFC's "eleven independent
implementations across nine languages"). `DECISIONS-0001`'s standing note says
what stops option 1 being a conclusion is "a far poorer data model and library
availability" — on the *data model* half that stands, but on the *library* half,
if option 5 must implement its profile itself regardless, the gap narrows at the
layer that actually has to be written. MD-3 scored the format; the profile is
what we would be conforming to.

**Finding 6 — and running the other way: dCBOR is the only source we hold that
states condition (2) normatively, which is a real gain for option 5 and for no
other option.** Recorded here rather than only under *What we adopt*, because a
findings list that only cuts one way is as useless as one that only confirms. §1
and every decoder rule in §2 oblige rejection. `topics/canonical-encoding.yaml`
records that RFC 8949 §4.2, RFC 9804 and RDFC-1.0 all define an encoder and leave
the decoder's obligation unstated — including **option 1's** document. So on
condition (2) the position reverses: option 5 can cite the obligation, option 1
cannot, and `DECODE-FINDINGS.md` has already shown ("The falsifier does not
fire") that both are implementable. **[analysis]** The net across findings 1–6 is
not a verdict and must not be read as one. It is that **MD-3's narrowing is
supported on condition (2) and on encoder determinism, and is unsupported or paid
for on the profile indicator, on Unicode normalization, on citability and on
profile-layer library availability.** That is what the ADR has to weigh, and the
weighing is Paul's, not this extraction's.

### 4. What this changes in the Oct 28 (D5) package

The `rfc-8949` extraction built the fixture table option 5 owes. dCBOR supplies
ready answers and ready negative fixtures for several of its rows, and this is
the cheapest practical use of this record:

| `rfc-8949` determinism row | what dCBOR decides | locator | fixtures available |
|---|---|---|---|
| 3 · indefinite lengths on decode | reject | §2.1 (2) | — |
| 5 · float shortening | preferred serialization, decoder-enforced | §2.2; §7.2 rows 2, 5–8 | `fb3ff8000000000000` for 1.5; `fa7f800000` for Infinity |
| 6 · integer-vs-float for integral values | reduce to integer within `DCBOR_INT` | §2.5 (1); §7.1 "Reduced" rows | `42.0 → 182a`; `2345678.0 → 1a0023cace`; negative fixture `f94a00` (12.0) |
| 7 · NaN | single quiet NaN `0xf97e00` | §2.5 (2); §8.3 | `f97e01`, `faffc00001`, `fb7ff9100000000001`, all rejected |
| 8 · negative zero, subnormals | `-0.0` reduces to `00`; subnormals are ordinary preferred-serialization floats | §2.5 (1); §7.1 | `-0.0 → 00`; `f90001`, `fa00000001`, `fb0000000000000001` |
| 9 · integer range | `[-2^63, 2^64-1]` — but see *Defects* 9 | §2.5 (1); §7.2 rows 3–4 | `3b8000000000000000`, `3bffffffffffffffff` |
| 10 · duplicate map keys | reject, encoder and decoder | §2.4 | — |
| 11 · key equivalence | **the opposite of our reading**: numerically equal keys are one key | §2.5 note, Figures 1–2 | `{10: "ten", 10.0: "floating ten"}` — a discriminating fixture between dCBOR and the recorded option-5 reading |
| 13 · invalid UTF-8, and beyond it unnormalized UTF-8 | reject non-NFC | §2.7 | the source supplies **no** NFC vector; we must build one |

**[analysis]** Row 11's fixture is the one to build first, because it is the only
place where dCBOR and the recorded reading of option 5 produce *different
verdicts on the same bytes* rather than different silences, and because its
verdict is decided by the float question (`rfc-8949` OQ6) that nothing currently
schedules. Row 13's missing NFC vector is second: §7's vectors are numeric only
("Appendix A: dCBOR Numeric Test Vectors"), so the rule most consequential for
`ARCH-0002` P1 identity has no fixture in the source at all.

---

## Open questions

Items this document cannot settle, with who must. Items marked **[beyond
source]** are ones where this extraction had to reason past both dCBOR and our
own documents.

1. **Does option 5 cite dCBOR, cite RFC 8949 §4.2.1 alone, or wait for CDE?**
   The three have different `R-O-03` profiles (§2 above) and dCBOR-18 says
   nothing about CDE. `topics/deterministic-cbor-profiles.yaml` owns the
   convergence half and is open with no record past `fetched`. *DEC-002 ADR —
   Paul; the topic — unassigned.*
2. **Floats in or out of option 5.** Carried over from the `rfc-8949`
   extraction's open question 6 and **upgraded here from loose end to
   precondition**: rows 12–14 of the table, and the row 11 fixture, cannot be
   written until it is answered, and dCBOR §2.5 and our recorded reading
   disagree about the data model if floats are in. *David's D4 encoding-neutral
   schema, Oct 21 — before D5.*
3. **Reject or rewrite, for NFC.** §2.7 (1) does not say, and the difference
   decides whether canonicalisation mutates `(defining key, label)` identities.
   **[beyond source]** Our reading is reject-at-encode plus reject-at-decode, per
   `R-O-05`. One ADR sentence; fixture-affecting. *Paul.*
4. **Is the no-registry rule a rule about wire bytes or about every identifier we
   use?** `.dcbor` (§3) is registry-allocated and never appears on the wire; tag
   201 is registry-allocated and does. **[beyond source]** `ADR-0001`'s scope
   language ("type identifiers, predicate types, tags, header parameters")
   suggests the wire reading but does not state it. This is the same question the
   `rfc-8949` extraction asks about tagged-versus-untagged COSE export, one layer
   further out. *DEC-002 ADR.*
5. **Is dCBOR single-pass checkable, including §2.7?** `DECODE-FINDINGS.md`
   proved it for *our* rules. **[beyond source]** Our reading of dCBOR's: §2.1–
   §2.4 and §2.6 are local or need only the previous key's byte range, and §2.5's
   reduction check is a local test against `DCBOR_INT`, so all are single-pass
   with O(1) state; §2.7 is single-pass but needs normalization tables, which is
   a dependency rather than a pass. If that is right the falsifier still does not
   fire for dCBOR, and the cost is a dependency, not an architecture. Worth
   twenty lines of the spike to confirm rather than assert. *David, #73
   follow-on.*
6. **Where does the key-relative profile indicator live, and what replaces tag
   201?** Finding 1. Interacts with `rfc-8949`'s open question 10 (where
   `R-O-05`'s authenticated type indicator lives) and with DEC-003's identifier
   form. *`ARCH-0001` §4.2, DEC-002, DEC-003.*
7. **Does the "fourth-and-a-half profile" risk close with two edits, or is
   conformance testing owed?** §1 above names the two divergences (NFC, 65-bit
   negatives). **[beyond source]** Making the edits makes the spike a dCBOR
   subset; it does not make it *tested* against dCBOR, and no Python
   implementation exists to test against (§4). The Ruby implementation is
   reachable at `https://cbor.me` (§4.4) and is the only practical cross-check
   available. *David, D5.*
8. **Does `usefulness: marginal` survive this reading?** The record's verdict
   (2026-09-22) cites no IETF stream and no WG standing, which remains true
   procedurally. **[analysis]** Two things temper it: the author list includes
   Carsten Bormann, co-editor of RFC 8949, and Laurence Lundblade, and the
   Acknowledgments thank "Joe Hildebrand, Rohan Mahy, and Anders Rundgren in the
   CBOR working group" — so the document is individual in process and
   WG-adjacent in authorship; and it is the only source we hold that states
   condition (2). Neither changes its standing. Recorded for the record owner,
   not acted on here. *S1.*

### Defects and ambiguities in the draft itself

Found in this pass by reading §2 against §7. These are not questions about our
design; they are places where the source does not decide something it appears to
decide, so an implementer has to choose.

9. **§7.2 rejects 65-bit negative integers that no rule in §2 forbids.** Table 4
   requires a decoder to reject `3b8000000000000000` (`-2^63-1`) and
   `3bffffffffffffffff` (`-2^64`), both annotated "65-bit negative integer
   value", and the table's preamble carries the MUST: "These are valid CBOR
   encodings that MUST be rejected as invalid by a dCBOR-compliant decoder." But
   `DCBOR_INT = [-2^63, 2^64-1]` is introduced in §2.5 (1) solely as the range
   within which *floating point values* are reduced to integers, and §2.5 (3)'s
   decoder rule is scoped to "encoded floating point values". **Nothing in the
   normative §2 narrows the integer range.** Nine of Table 4's eleven rows trace
   to a §2 rule; these two do not. **[analysis] §3 cuts the same way, and pass 2
   adds it as independent corroboration: §3 reproduces the RFC 8610 prelude's
   `number = int / float`, states that it "encompasses the full space of CBOR
   numeric values representable by CBOR major types 0, 1, and 7", and then tells
   dCBOR applications they "can use `number` to specify fields with numeric
   values".** The prelude's `nint` is `#1`, the whole of major type 1, which
   reaches `-2^64` — so the one type §3 recommends for numeric fields admits, by
   the document's own description of it, exactly the two values Table 4 requires
   a decoder to reject. A §2 that narrowed the integer range would have made §3's
   sentence false; it does not, because it does not. *Our profile must state the
   integer range in its own normative text; it cannot inherit it by citing §2.
   `rfc-8949` determinism row 9; D5 package.*
10. **§2.7's decoder rule is numbered "1."** where every other subsection numbers
    the decoder rule "2." (§2.1, §2.2, §2.3, §2.4, §2.6). Editorial, but it
    breaks the `<section>(<n>)` locator convention the rest of §2 establishes,
    and any requirement id derived mechanically from the numbering collides with
    the encoder rule. *Recorded for `requirements.yaml`'s locator scheme.*
11. **§2.7 does not say whether a conforming encoder rejects or normalizes.** See
    open question 3; recorded here too because it is a defect in the source and
    not only a decision of ours. A specification whose stated purpose is to
    remove the protocol designer's choices (§8: "reduce the number of choices
    that protocol designers need to make") leaves this one open.
12. **Table 3's annotation for `-127` reads "(-2^8 - 1)".** `-2^8 - 1` is `-257`;
    `-127` is `-(2^7 - 1)`. The encoding given, `387e`, is correct for `-127`.
    Harmless, but it is in the table a conformance suite is built from. *Test-
    suite author; noted for `examples/`.*
13. **§4.4's Ruby entry claims "Coverage: Complete specification" and then says
    "Checking of dCBOR - exclusions not yet implemented".** Self-contradictory on
    its face, and the "exclusions" are §2.6 and §2.7 — the two rules that matter
    most to us. §4's RFC 7942 boilerplate covers it ("no effort has been spent to
    verify the information presented here"), but it means the only
    non-single-maintainer implementation is the one that does not check the rules
    we most need checked. *Relevant to open question 7.*
14. **Figure 1 is not rejected for the reason §2.5 gives for it, and a
    conformance suite built from the figure will test the wrong rule.** Found by
    the cross-check pass, which ran every vector through a transcription of
    `../schema/dcbor-validate.derived.pseudocode.txt`. §2.5's indented note
    presents Figure 1 — the map `{10: "ten", 10.0: "floating ten"}` — as a valid
    CBOR map that dCBOR cannot represent *because Numeric Reduction collides its
    keys*, and Figure 2 shows the collision. That is a statement about the
    **encoder**: reduce Figure 1's data model and you get Figure 2's duplicate
    keys, which §2.4 (1) forbids emitting. On the **decode** side the collision
    never arises, because a decoder rejects Figure 1's bytes strictly earlier
    and for a different rule: the key `f94900` is an integral floating point
    value inside `DCBOR_INT`, which §2.5 (1) required to have been reduced and
    §2.5 (3) therefore makes a decoder reject on sight — before any key is
    compared with any other. There is no input on which a dCBOR decoder reports
    "duplicate key" *because of* Numeric Reduction: by the time two encoded keys
    can be equal, both have already passed the reduction check. **[analysis]**
    Nothing in the source is false — §2.5's note says "cannot be *reduced to*
    valid dCBOR maps", which is the encoder direction — but the figures sit in a
    document whose every other rule is stated twice, once per role, and an
    implementer who reads them as a decoder test will write an assertion that
    can never fire. The library's own vector `V-0006` records both rules in its
    `violates`, encoder rule first, and this entry is why the order matters.
    *Test-suite author; relevant to open question 7 and to the D5 fixture set.*
