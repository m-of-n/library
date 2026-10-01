---
record: rfc-8949
kind: design-notes
title: "rfc-8949 — bearing on our design"
extracted: "2026-09-30"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§4.2.1`) are RFC 8949. Our own documents are cited by id (`ARCH-0002 P1`,
`D-3`). Three markers distinguish voices:

- unmarked prose reports **RFC 8949** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project that the sources
  do not support.

**Decision status, stated plainly.** DEC-002 in `ARCH-0001` §7 (v0.1.1) lists
**four** options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3; that proposal is unmerged and ARCH-0001 still
carries DEC-002 under "Open decisions". `ADR-0001` (accepted) constrains
DEC-002 and says option 2 "as originally written does not" remain on the table.
`D-3` (2026-09-28) narrows DEC-002 to option 5. **No ADR for DEC-002 has been
written.** Both the D-3 minute and `PLAN-0003` say "then ADR", and the
2026-09-28 action list assigns Claude only ADR-0002 (P2, P3, P5, P6). Nothing
below may be read as an accepted encoding decision.

---

## What we adopt

**The basic generic data model (§2), as a specific data model (§2.2).** §2
enumerates a data item as one of: an integer in `-2^64..2^64-1`; a simple value
identified by 0..255 but distinct from that number; a binary64 floating-point
value distinct from an integer; a byte string; a text string of Unicode code
points; an array; a map from data items to data items; a tagged data item. We
take that list minus the last entry (see *What we reject*). §2.2 is the seat we
author from: "The specific data model for a CBOR-based protocol usually takes a
subset of the extended generic data model and assigns application semantics to
the data items within this subset."

**Major types 0–5 and 7's float/simple-value half (§3.1, §3.3).** Mapped onto
`ARCH-0001` §4.1:

| major type | §ref | our use |
|---|---|---|
| 0 / 1 integers | §3.1 | `Threshold.k`, `Threshold.n`, `Validity` times, `Endorse` weights |
| 2 byte string | §3.1 | `Key` material, `KeyId` digests, signatures, `ArtifactId.digest`, the R-O-05 signed payload |
| 3 text string, UTF-8, never escaped | §3.1 | the P1 **local label**, SDSI name-chain elements (`Name.labels`), P3 descriptions |
| 4 array | §3.1 | ordered things: name chains, `Threshold.members`, `subjects` |
| 5 map | §3.1 | the statement itself; `2N` items; odd count is not well-formed |
| 7 simple 20/21/22 | §3.3 Table 4 | `false`, `true`, `null` |

**§3.1's separation of extent from semantics.** The initial byte carries the
major type in its high 3 bits and additional information in its low 5, so a
decoder determines the *extent* of an item without understanding it. This is
already recorded in `ARCH-0002`'s CBOR note, and it is the substrate property
that makes P5's *may traverse, must never accept* a stateable rule.

**The three-level acceptability hierarchy (§1.2, §5.3).** well-formed (any
decoder) / valid (validity-checking decoder) / expected (the application).
`ARCH-0002` P5 adopts this wholesale and forbids skipping any level. §5.3.1
gives basic validity two failure kinds we inherit directly: duplicate map keys,
and invalid UTF-8 in a text string.

**§4.1 preferred serialization and §4.2.1 core deterministic encoding as the
base.** Shortest argument for integers, string lengths, array/map counts;
shortest float form that preserves the value; definite lengths only; map keys
sorted in bytewise lexicographic order of their deterministic encodings.

**The §5 MUSTs that bind any CBOR-based protocol, which option 5 must
discharge.** §5: "CBOR-based protocols MUST specify how their decoders handle
invalid and other unexpected data" and "Encoders for CBOR-based protocols MUST
produce only valid items". §5.3: the first layer that processes the semantics
of an invalid item MUST choose replace-with-error-marker or stop, and the
protocol MUST say which, per kind of invalid item. §5.6: a protocol MUST define
what to do on duplicate keys, and MUST NOT ascribe semantics to map order.

**§10's threat posture.** "A CBOR decoder needs to assume that all input may be
hostile even if it has been checked by a firewall, has come over a secure
channel such as TLS, is encrypted or signed". That sentence is the reason
R-O-05 (proposed) puts signature verification before decoding rather than after.

**§5.5's warning on number range.** CBOR's integers exceed platform `int64_t`
by one bit of sign; JavaScript silently loses precision above 53 significant
bits. A profile range is required of us, not optional.

---

## What we adapt, and how

**§2.1's "extended generic data model" — we subtract instead of extend.** §2.1
says the extended model "expands by the registration of new simple values or
tag numbers, but never shrinks". RFC 8949 offers no vocabulary for a protocol
that declines the extension mechanism outright; what it offers is §2.2's
subsetting. Option 5 is therefore expressed as a §2.2 specific data model whose
subset excludes major type 6 entirely and admits only the simple values §3.3
Table 4 defines in this document.

> **[analysis]** A literal "basic generic data model only" reading is
> self-defeating: §2.1 lists `false`, `true`, `null` and `undefined` as
> extensions created by the §9.1 Simple Values registry, so strict literalism
> would strip our booleans. The workable line is *no major type 6 at all, and
> simple values only as defined in §3.3 Table 4 by RFC 8949 itself*. This is
> our inference, it changes fixtures, and it belongs in one sentence of the ADR.

**§4.2 — we select the base and then further constrain it.** §4.2 is explicit
that this is our job: protocols "are free to define what they mean by a
"deterministic format" and what encoders and decoders are expected to do. This
section defines a set of restrictions that can serve as the base". See *Mapping
to our decisions* for the list option 5 owes.

**§5.6's map-key advice — we take the JSON half and drop the constrained-node
half.** §5.6 recommends limiting keys to text strings when interworking with
JSON-based applications, "otherwise, there has to be a specified mapping from
the other CBOR types to text strings, and this often leads to implementation
errors". We adopt that. §5.6 also recommends small integer keys for constrained
devices (24 keys in a single byte, 48 with negatives); we decline it, because
P1 type identity is a text label and the YAML human form cannot round-trip
integer keys without inventing the very mapping §5.6 warns against.

**§8's diagnostic notation — replaced by YAML, on the RFC's own suggestion.**
§8 defines a human-readable notation and immediately disclaims it: "this truly
is a diagnostic format; it is not meant to be parsed". In the same paragraph:
"Implementers looking for a text-based format for representing CBOR data items
in configuration files may also want to consider YAML [YAML]." D-3's YAML
choice therefore has the RFC's own pointer behind it. §8.1's encoding
indicators (`1.5_1` for binary16, `[_ 1, 2]` for indefinite length) exist
because a human form cannot show serialization variants — which is exactly why
the YAML mapping can only be canonical in one direction.

**§6.1 / §6.2's CBOR↔JSON advice — adapted as a failure catalogue, not as a
conversion.** §6.1's list of what has no JSON analogue (byte strings, non-text
map keys with "a danger of key collision", non-finite floats, tags) is the same
list the YAML mapping must answer. We reject §6.1's remedy of a "substitute
value, such as a JSON null" for any path a verifier depends on.

**Tag 24's construct, without tag 24.** §3.4.5.1 exists for "an embedded CBOR
data item that is not meant to be decoded immediately at the time the enclosing
data item is being decoded" — a byte string holding an encoded CBOR item. That
is precisely the shape R-O-05 (proposed) requires for the signed payload. We
use the construct as a bare byte string and let our schema, not the wire, say
it is CBOR. See the tag-24 treatment below.

---

## What we reject, and why

**Major type 6 and the IANA CBOR Tags registry (§3.4, §9.2) as a native
extension point.** §9.2's policies — Standards Action for 0–23, Specification
Required for 24–32767, First Come First Served above 32768 — allocate from one
global space. `ADR-0001` (accepted) settles this: "CBOR tags and COSE header
parameters are IANA allocated, so they are interchange, not native."

**§9.1's Simple Values registry as the alternative extension point.** Rejected
on structure, not policy. §3.3 defines a simple value as a value that does "not
need any content": all information is in the head. There is nowhere to attach a
defining key. **[analysis]** This is a stronger form of ADR-0001's private-use
argument than ADR-0001 makes: for simple values the impossibility is
syntactic, and no allocation policy could fix it.

**§4.2.3 length-first map key ordering.** §4.2.3 exists solely for
compatibility with RFC 7049 §3.9 "Canonical CBOR". We have no RFC 7049
deployment to be compatible with, and `rfc-7049` is held in this library as a
superseded record.

**Indefinite lengths (§3.2) in both directions.** §4.2.1 already forbids
emitting them. We additionally reject them on decode; §4.2 makes decoder
checking optional ("those protocols might also have the decoders check"), and
§5.1 notes indefinite lengths force a decoder "to allocate increasing amounts
of memory while waiting for the end of the item".

**§5.7's use of `undefined` as an encoder substitute "for a data item with an
encoding problem, in order to allow the rest of the enclosing data items to be
encoded without harm".** Direct collision with `ARCH-0002` P5: "a failure at
any level is a rejection, never a repair." Simple value 23 is excluded from
option 5 entirely.

**§5.4's forward-compatibility recommendation.** §5.4 offers a
validity-checking decoder two responses to an unrecognised tag or simple value
and discourages the strict one: "Note that treating this case as an error can
cause ossification and is thus not encouraged." `ARCH-0002` P5 inverts this:
"unknown is critical unless declared otherwise", motivated by CVE-2025-59420.
This is a real, explicit disagreement with RFC 8949 advice and must be stated
as such in the ADR rather than glossed. **[analysis]** The disagreement is
narrower than it looks: §5.4's ossification argument is about *registry growth*
reaching a decoder that predates it. Option 5 has no registry to grow, so the
premise of §5.4's advice is absent. Our inference; it is the argument that
makes P5 defensible to an RFC 8949 reader, and it should appear in the ADR.

**§1.1 objectives 3 and 7 as acceptance criteria.** "Data must be able to be
decoded without a schema description" and "The format must support a form of
extensibility that allows fallback so that a decoder that does not understand
an extension can still decode the message." We keep the *traversal* property
and reject the *acceptance* implication, per `ARCH-0002`'s one-line form.

---

## Mapping to our decisions

### 1. What option 5 takes from the CBOR data model

Stated in RFC 8949's own section terms, "the CBOR data model without the tag
registry" is exactly this:

1. **In:** §2's basic generic data model, minus its eighth bullet ("a tagged
   data item"). Concretely major types 0, 1, 2, 3, 4, 5 of §3.1, and of major
   type 7 the floating-point values of §3.3 and simple values 20, 21, 22 of
   §3.3 Table 4.
2. **Out:** §2.1's extended generic data model in its entirety — every tag
   number of §3.4 and §9.2, and every simple value not defined in §3.3.
3. **Authored under §2.2**, which permits a specific data model to take a
   subset and assign application semantics. Option 5 uses that licence three
   ways: to fix the subset in (1)–(2); to declare **no** cross-type value
   equivalences, so §5.6.1's generic-model distinctness holds unmodified
   (integer 1 ≠ float 1.0 ≠ simple value 1; text string ≠ byte string of the
   same bytes); and to select and further constrain §4.2.
4. **Integers:** §2's full `-2^64..2^64-1`, narrowed by a profile range that
   option 5 owes (§5.5). With tags 2 and 3 rejected, there is no bignum, so
   values outside the range are not representable and not promotable.
5. **Floats:** §3.3's binary16/32/64. §5.5 explicitly permits exclusion: "For
   an integer-only application, a protocol may want to completely exclude the
   use of floating-point values." Whether option 5 does is open (below).
6. **Text vs byte strings:** load-bearing for us and the distinction we most
   depend on. §3.1: major type 3 is UTF-8, never escaped, and invalid UTF-8 is
   well-formed but **invalid**; §5.6.1: text strings are distinct from byte
   strings "even if composed of the same bytes". P1 labels are text; keys,
   digests and signatures are bytes; the two are never confusable on the wire.
7. **Maps:** §3.1 major type 5 — key immediately followed by value, `2N` items,
   odd count not well-formed, duplicate keys well-formed but not valid.

### 2. The no-IANA-tags consequence

RFC 8949's only extension points are §7.1's three: the simple space (§9.1), the
tag space (§9.2), and the additional-information space, which §7.2 says is not
managed by a registry at all and can only be changed "by updating this
specification". Excluding tags therefore removes the one usable extension
point. What is lost, and what carries it instead:

| lost facility | §ref | what carries it under option 5 | awkwardness |
|---|---|---|---|
| Standard date/time string | §3.4.1 | a text string field | §3.4.1 makes a non-conforming string **invalid** at tag level; untagged, a malformed timestamp is only an "expected"-level error, so P5 obliges us to implement the RFC 3339 check ourselves |
| Epoch-based date/time | §3.4.2 | plain major-type-0/1 integer seconds | we must restate §3.4.2's own POSIX/leap-second caveats and its advice to use untagged `null` for "an expiry date that is not set" rather than `Infinity` |
| Bignums | §3.4.3 | byte strings (major type 2) | **no loss for us:** `ARCH-0001` §4.1 already makes `Key`/`KeyId` byte-valued, and we escape §3.4.3's leading-zero preferred-serialization trap entirely |
| Decimal fractions, bigfloats | §3.4.4 | a map or array of integer mantissa + exponent under our own labels | bears on DEC-004 tag intersection over numeric ranges and P3 value scales; §4.2.2's closing bullet (one number, many decimal-fraction forms) becomes a problem in *our* encoding rather than in a tag, and still needs a deterministic rule |
| Expected-conversion hints (base64url / base64 / base16) | §3.4.5.2 | a property of the P3 type, not of the value | **aligns with us:** P3 already says a type carries its rendering. Worth recording as a case where the tag exclusion improves the design rather than costing us |
| Encoded CBOR data item | §3.4.5.1 | a bare byte string, CBOR-ness asserted by schema | the sharp case — treated separately below |
| URI, base64url, base64, MIME | §3.4.5.3 (tags 32, 33, 34, 36) | text strings, validated by our schema | same shift of validation from decoder to application as tag 0 |
| Self-described CBOR, head `0xd9d9f7` | §3.4.6 | media type, file extension, or our own framing | concrete cost for the D-1 archives target: statements stored as files on a share have no magic number, and §3.4.6's whole purpose is "when CBOR data is stored in a file that does not have disambiguating metadata" |

**Carried as ordinary map entries instead of codepoints:** type identity
`(defining key, label)`; predicate type; authorization tag identity (DEC-004);
R-O-05's authenticated type indicator; P4's domain-of-discourse hash; and
content-encoding hints.

> **[analysis]** The byte cost is real and nobody has scored it. A tag number
> costs 1–3 bytes (§7.1: the first 24 are one byte, the next 232 are two). A
> `(KeyId, label)` pair costs a 32-byte digest plus the label plus two heads.
> Against §1.1 objective 2 (class-1 constrained nodes, RFC 7228) that is a
> regression of one to two orders of magnitude per type reference. The
> mitigation is already in our design: P4 lets a statement cite one
> domain-of-discourse hash and then use short labels within it, amortising the
> key across every type reference in the statement. This is the strongest
> practical argument that P4 is load-bearing rather than decorative, and it is
> our analysis, not anything ADR-0001 or ARCH-0002 says.

#### Tag 24 — set out precisely

**What the RFC says.** §3.4.5.1: tag number 24 tags "the embedded byte string
as a single data item encoded in CBOR format. Contained items that aren't byte
strings are invalid. A contained byte string is valid if it encodes a
well-formed CBOR data item; validity checking of the decoded CBOR item is not
required for tag validity (but could be offered by a generic decoder as a
special option)."

**Why we need the construct.** R-O-05 (proposed, `ARCH-0001-PROPOSAL` §3.4)
requires that the signed payload "SHALL be the canonical encoding verbatim" and
that a verifier "SHALL verify the signature before decoding". A byte string
holding an encoded CBOR item is the only way to express that inside the CBOR
data model. So option 5 uses tag 24's subject matter while forbidding tag 24.

**[correction] The premise carried into this extraction — that COSE's
protected header depends on tag 24 — does not hold.** RFC 9052 §3 (library record `rfc-9052`) defines the protected
bucket as `empty_or_serialized_map`: "This value is obtained by CBOR encoding
the protected map and wrapping it in a bstr object." It is a bare `bstr`, and
the string "tag 24" does not occur anywhere in RFC 9052. COSE uses tag 24's
*pattern* without tag 24, for the reason §3.4.5.1 gives and for one of its own,
stated in RFC 9052 §3: "This avoids the problem of all parties needing to be
able to do a common canonical encoding of the map for input to cryptographic
operations." The tension between "no tags" and "COSE as export" is real, but it
lands in three other places.

**Tension 1 — COSE identifies its message types by registry-allocated CBOR
tags.** RFC 9052 §2 Table 1: COSE_Sign is tag **98**, COSE_Sign1 is tag **18**
(also 96/16/97/17 for the encrypt and MAC structures). RFC 8392 §6 adds the CWT
tag **61**, and "If present, the CWT tag MUST prefix a tagged object using one
of the COSE CBOR tags." Those are §9.2 allocations appearing in exported bytes.
A native no-tags rule and a COSE export are compatible only if the tag lives
strictly outside the native object: export *adds* 18/98/61, import *strips*
them, and no native object is ever byte-identical to a tagged COSE message.
RFC 9052 §2 does supply three tag-free identification routes — context, the
`cose-type` parameter of `application/cose`, and the CoAP Content-Format — and
notes the parameter "is REQUIRED if the untagged version of the structure is
used". So an untagged export profile exists. Choosing it also forecloses the
CWT tag, since RFC 8392 §6 conditions tag 61 on a COSE tag beneath it. **This
extraction does not choose between tagged and untagged export**; it is a
DEC-002/DEC-005 question and is listed as open.

**Tension 2 — we use the bstr-embedded-CBOR pattern with its label removed.**
§3.4.5.1's tag exists so that a *generic* decoder can know a byte string is
CBOR. Without it, our `protected`-equivalent and our signed payload are opaque
hex to every generic CBOR tool, and their CBOR-ness is a schema fact rather
than a wire fact. That is what R-O-05 wants — the verifier must not decode
before verifying — so the semantic loss is nil and the cost is debuggability.
**[analysis]** This cost is an argument *for* D-3's YAML human form, not
against it: with §8 diagnostic notation unable to see inside an untagged bstr,
a regenerated YAML rendering from verified bytes is the only readable view we
will have.

**Tension 3 — §4.2.2 forbids leaving tag presence to convention.** "If a
CBOR-based protocol were to provide the same semantics for the presence and
absence of a specific tag ... the deterministic format would not allow the
presence of the tag, based on the "shortest form" principle", and "This
protocol's deterministic encoding needs either to require that the tag is
present or to require that it is absent, not allow either one." Consequently
option 5's determinism profile must state as a positive rule that **major type
6 MUST NOT appear**, and decoders must reject it — not merely omit tags by
habit. That rule plus a named export profile are the two halves that keep
tensions 1 and 2 from colliding; without the first, a tagged COSE object
imported and re-emitted would silently satisfy our encoder.

### 3. Determinism — what option 5 must pin down itself

§4.2 chooses nothing for us. §4.2.1 is "a set of restrictions that can serve as
the base"; §4.2.2 is a list of considerations the RFC hands to the protocol
designer; §4.2.3 is an alternative ordering. This is the direct input to the
**Oct 28 (D5)** fixture package.

| # | what §4.2 leaves open | option 5's required decision | negative fixture |
|---|---|---|---|
| 1 | which ordering | **§4.2.1 bytewise-lexicographic**, not §4.2.3 length-first | the RFC gives both orderings over the same eight keys (`10`, `100`, `-1`, `"z"`, `"aa"`, `[100]`, `[-1]`, `false`) and they differ — a ready-made discriminating pair |
| 2 | tags | **MUST NOT appear**; decoder rejects major type 6 (§4.2.2 requires present-or-absent, never either) | a tag-24-wrapped payload; a tag-18 COSE_Sign1 |
| 3 | indefinite lengths | §4.2.1 forbids emitting; option 5 adds **decoder rejection** (§4.2 leaves decoder checking optional) | `0x9f018202039f0405ffff` from §3.2.2 |
| 4 | floats present at all | decide; §5.5 permits total exclusion | a binary64 item where the profile forbids floats |
| 5 | float shortening | §4.2.1 already requires shortest-form-preserving-value; §4.1 adds the NaN rule (a shorter form is preferred if zero-padding the significand rightwards reconstitutes the value) | `0xfb3ff0000000000000` for 1.5 instead of `0xf93e00` |
| 6 | integer-vs-float for integral values | if floats are in, pick among §4.2.2's rules 1/2/3; the RFC says "Rule 2 may be a good choice in many cases" | `1.0` as `0x01`, `0xf93c00`, `0xfa3f800000`, `0xfb3ff0000000000000` |
| 7 | NaN | §4.2.2: "the protocol needs to pick a single representation, typically 0xf97e00" | a NaN with a payload; a signalling NaN |
| 8 | negative zero, subnormals | §4.2.2 raises both; option 5 must rule | `-0.0`; a subnormal binary16 |
| 9 | integer range | §5.5: pin the profile range and the decoder's response to in-CBOR-but-out-of-profile values | `2^63` where the profile stops at `int64` |
| 10 | duplicate map keys | §5.6 **MUST** define it; P5 forces §5.3 choice 2 (error and stop) | a map with two identical keys |
| 11 | key equivalence | §5.6.1 makes this the specific data model's call; declare **no** cross-type equivalences | `{0: …, 0.0: …}` — two keys generically, one if we declared equivalence |
| 12 | map key types | restrict to text strings (§5.6), foreclosing §5.6's integer-key optimisation | an integer-keyed map |
| 13 | invalid UTF-8 | §5.3.1 says a decoder "might or might not want to verify"; P5 makes it mandatory | `0x62c0ae` from §5.2 |
| 14 | per-kind invalid-item handling | §5 and §5.3 **MUST** specify, per kind | one fixture per row of this table |

**Two gaps the RFC does not fill, which option 5 must.**

> **[analysis] Array element ordering.** §4.2.1 canonicalises map *key* order
> and nothing else. RFC 8949 supplies **no** canonical ordering for array
> elements, because §3.1 major type 4 arrays are ordered by definition and
> their order is semantic. But several of our constructs are logical *sets*
> carried in arrays: `Threshold.members` (`ARCH-0001` §4.1), a tag's value set
> under DEC-004, and above all P4's "set of the schemas in P3, serialized in a
> form that can be reliably and repeatably hashed". Two parties that build the
> same set in different insertion orders get different hashes and, per P4,
> conclude they hold different vocabularies. Option 5 must define a canonical
> array order for set-valued fields — the natural choice being bytewise
> lexicographic order of element encodings, borrowing §4.2.1's rule one level
> out. This is the determinism hole most likely to be missed, it blocks P4's
> hash-as-identity from being well defined, and neither RFC 8949 nor any of our
> documents currently states it.

> **[analysis] Unicode normalization of labels.** §3.1 requires UTF-8 and says
> nothing about normalization form; §5.6.1 compares text strings "byte by
> byte". Under P1, a type *is* `(defining key, label)`, so two labels that a
> human reads as identical but that differ in normalization are two different
> types, silently. RFC 8949 has no opinion here and cannot be faulted for it;
> P1 creates the hazard by making a text string load-bearing for identity. A
> normalization rule (or an explicit refusal to normalize, with a reject-on-
> non-NFC decoder rule) is needed before fixtures are frozen.

**What the export comparison must isolate.** RFC 9052 §9 aligns COSE with
§4.2.1 but *narrows* it: the restriction applies only to the Sig/Enc/MAC
structures; encoding must use definite lengths with minimum-length arguments;
duplicate labels are forbidden. **RFC 9052 §9 does not require map key
sorting.** Option 5's native rule is therefore strictly stronger than COSE's,
so a conformant COSE producer may emit unsorted header maps and an
export→import cycle is not byte-stable unless we apply our own sort on export.
D-3 retains option 2 as the comparison fixture, and option 2 is COSE_Sign1 +
CWT claims; the comparison pair should isolate three axes, not one: tags 18/61
present vs absent, registry header labels vs `(key, label)` map entries, and
sorted vs unsorted maps.

**Package shape for Oct 28.** DEC-002's own acceptance test in `ARCH-0001` §7
is "round-trip fixtures for NameCert, AuthzCert (including threshold subject),
ArtifactStatement". Under P6 those are three predicate types over one form, so
the three fixtures exercise one encoder. Add one negative fixture per row of
the table above, one fixture per §4.2.1/§4.2.3 ordering divergence, and the
option-2 comparison. RFC 8949 Appendix A supplies ready diagnostic/hex pairs
and Appendix F.1 supplies not-well-formed examples; both are extracted in this
record's `examples/`. Related library records where the upstream determinism
work now sits: `draft-ietf-cbor-cde` and `draft-ietf-cbor-serialization`
(v08, 29 July 2026, "CBOR Serialization and Determinism"). Cited as pointers,
not as RFC 8949 content, and not as decisions.

### 4. The YAML human form

**Status first.** `ARCH-0001-PROPOSAL-v0.2.0` §4 **withdrew** the authoring
format: "Nothing in the analysis requires humans to author certificates or
statements in a text format ... The YAML restriction list from revision 1 is
retained only as an appendix note ... and carries no proposed status." D-3
names YAML as the human form with a canonical one-way mapping. Those two
statements are in tension, and the mapping's *direction* decides which: R-O-05
(proposed) implies two different one-way maps — YAML→CBOR at authoring time on
trusted input, and verified-CBOR→display at reading time — while D-3 as minuted
names one. The ADR must say which, and whether §4's withdrawal of DEC-006 is
thereby reversed. Not resolved here.

What a canonical one-way YAML → reduced-CBOR mapping must settle, each item
forced by the data model:

- **Key types.** §3.1 major type 5 admits any data item as a key, and §8 notes
  the diagnostic notation "extends JSON here by allowing any data item in the
  key position". YAML admits non-string keys in principle but no practical
  toolchain or schema language does. The mapping must restrict native map keys
  to **text strings**, per §5.6's warning about specified mappings from other
  CBOR types to text strings leading to implementation errors. Cost, recorded:
  §5.6's integer-key optimisation for constrained devices is foreclosed, so
  §1.1 objective 2 is the objective the YAML decision trades away.
- **Byte strings.** YAML has no byte type; CBOR's major type 2 is distinct from
  major type 3 "even if composed of the same bytes" (§5.6.1). Without an
  unambiguous YAML spelling for bytes, a text string and a byte string share
  one YAML scalar and the mapping is **not injective** — which defeats
  canonicality outright. The candidates are a YAML tag (`!!binary`), a typed
  wrapper, or making it schema-driven from the P3 type; §8's `h'…'` / `b64'…'`
  notations and §6.1's base64url-without-padding convention are the precedents.
  **[analysis]** This is the single largest source of non-injectivity in the
  mapping and the item most likely to sink the Oct 28 package if left open.
- **Integer width.** YAML integers are unbounded; §2 caps CBOR at
  `-2^64..2^64-1`, and with tags 2/3 rejected there is no bignum escape. Out of
  range must be an authoring **error**. §6.2 explicitly contemplates the
  alternative for JSON — "integers longer than an implementation-defined
  threshold may instead be represented as floating-point values" — and that
  behaviour must be rejected by name, since a silent integer→float promotion
  changes a `Threshold.k` or a validity instant into a different data-model
  type (§2: "integer and floating-point values are distinct in this model").
- **Float representation.** YAML floats are decimal text; §3.3 floats are
  binary16/32/64. §6.2 pins the only defensible procedure: convert the
  mathematical value to binary64 by `roundTiesToEven` (IEEE 754 §4.3.1), then
  emit the shortest form that exactly represents *that result*. If floats are
  admitted, the mapping must adopt exactly that two-step and say so; `.nan`,
  `.inf` and `-.inf` must be excluded or tied to the §4.2.2 NaN choice.
  **[analysis]** Our recommendation for I2 is to forbid floats in the human
  form and carry any scale as an integer mantissa/exponent pair, which also
  removes determinism rows 4–8 from the Oct 28 critical path. A recommendation,
  not a decision; DEC-004/P7 profiles are what actually decide.
- **Duplicate keys.** YAML forbids duplicate mapping keys, but loaders vary and
  many are last-wins. §3.1 and §5.3.1 make a duplicate-keyed CBOR map
  well-formed but invalid, and §5.6 requires the protocol to define the
  behaviour. So the rejection must happen **at YAML load**, not at encode: a
  last-wins loader turns an ambiguous document into a perfectly valid CBOR map,
  which is §10's named attack — "an attacker could make use of invalid input
  such as duplicate keys in maps ... to make one application base its decisions
  on a different interpretation than the one that will be used by a second
  application."
- **Null and absence.** §3.3 simple value 22 is a value; an absent map key is
  not. CBOR distinguishes them and §3.4.2 even recommends untagged `null` over
  a non-finite float for an unset expiry. YAML's `null`, `~` and empty scalar
  all mean null. The mapping must state whether an explicit `null` and an
  omitted key are distinguishable in our schema, and both spellings must reach
  the same encoding.
- **Text handling.** §3.1: CBOR text is never escaped — "a newline character
  (U+000A) is always represented in a string as the byte 0x0a". YAML escapes,
  folds and has multiple block scalar styles. The mapping must define
  unescaping and folding, and then meets the same normalization question as
  determinism gap 2.
- **YAML features to exclude by profile:** anchors and aliases (a CBOR data
  item is a tree; §1.1 objective 1 says "loops and lattice-style graphs are not
  supported"), merge keys, implicit boolean spellings beyond `true`/`false`,
  sexagesimals, and implicit timestamp resolution. RFC 8949 says nothing about
  any of this; it is entirely our problem. The restriction list already exists
  as the appendix note in `ARCH-0001-PROPOSAL-v0.2.0` §4 and should be promoted
  rather than rewritten.
- **Sequences map cleanly**, since §3.1 major type 4 arrays and YAML sequences
  are both ordered — except for set-valued fields, which inherit determinism
  gap 1.

### 5. `(defining key, label)` against CBOR's own way of naming things

RFC 8949 offers exactly two mechanisms for naming a type: a **tag number**
(§3.4, major type 6, registry §9.2) and a **registered simple value** (§3.3
Table 4, registry §9.1). Both are bare integers from a single global space.

`ARCH-0002` P1 displaces them **structurally, not politically**. A tag's data
item is (tag number, tag content) per §3.4, and the number is the entire
identifier: there is no field in which to name a defining principal, and §3.3
simple values carry no content at all. So the key-relative form cannot be
expressed as a codepoint under any allocation policy. It has to be structure
*inside* the data model — a two-element array or two-entry map of
(`Key`-or-`KeyId`, text label) — and therefore it is carried as data. That is
the precise sense of P1's displacement: it does not choose different numbers,
it moves type identity from the encoding layer down into the data layer, where
`ARCH-0001` §4.1's `Principal` already lives.

The §9.2 First Come First Served range above 32768 is the strongest available
counter-argument and it fails. **[analysis]** FCFS removes the gatekeeper but
not the namespace, and it is *not* private use, so collision is prevented only
by the registry continuing to exist and to be consulted — which is exactly the
global authority `ADR-0001` declines to depend on. ADR-0001 argues this for
private-use ranges; the FCFS case is worth adding to it, because FCFS is what a
reviewer will actually propose.

RFC 8949 raises no objection to any of this. §2.2 invites a protocol to build a
specific data model; §3.4 says "The primary purpose of tags in this
specification is to define common data types such as dates" and that
"Understanding the semantics of tags is optional for a decoder". Nothing in
RFC 8949 asks a
protocol to name its own types with tags.

One cost, stated so the ADR carries both sides. §7.1 lists tags as one of
CBOR's three extension points precisely because an unknown tag is still
traversable with fallback (§1.1 objective 7, and §7.1: "Implementations
receiving an unknown tag number can choose to process just the enclosed tag
content or, preferably, to process the tag as an unknown tag number wrapping
the tag content"). Moving type identity into map entries keeps the traversal
property — items remain self-delimiting per §3.1 — but discards the *signal*: a
generic decoder can no longer tell a type-identified object from an ordinary
map. Under P5 we do not want fallback acceptance, so this is aligned with our
model; the residue is that our types are invisible to every generic CBOR tool,
and that belongs in the ADR next to the namespace benefit.

---

## Open questions

Items this document cannot settle, with who must. Items marked **[beyond
source]** are ones where this extraction had to reason past both RFC 8949 and
our own documents.

1. **Tagged or untagged COSE export.** RFC 9052 §2 Table 1 tags 18/98 and RFC
   8392 §6 tag 61 against the `cose-type` / CoAP / context alternatives.
   Decides whether "no IANA tags" is a rule about the native model only or
   about every byte we emit. *DEC-002 and DEC-005 ADR — Paul.*
2. **Is the no-tags rule absolute?** Does a stored native file get §3.4.6's
   `0xd9d9f7`? Does an export serializer that emits tag 18 count as "our
   encoder" for §4.2.2 purposes? *Same ADR.*
3. **Do booleans and `null` survive a strict "basic generic data model"
   reading?** §2.1 frames simple values 20–23 as §9.1 registry extensions.
   **[beyond source]** Our reading is that the intended line is "no major type
   6, simple values only as §3.3 Table 4 defines them", and that simple value
   23 `undefined` is excluded by P5. Fixture-affecting; needs one ADR sentence.
4. **Canonical ordering for set-valued arrays.** **[beyond source]** RFC 8949
   canonicalises map keys only. P4's domain-of-discourse hash cannot be well
   defined without this, and DEC-004 tag value sets need it too. *David (D4
   schema, Oct 21) then the ADR.*
5. **Unicode normalization of P1 labels.** **[beyond source]** RFC 8949 is
   silent and §5.6.1 compares byte by byte, so normalization variants are
   distinct types. P1 is accepted via `ADR-0001`, so changing it means a
   superseding ADR rather than an edit. *Paul.*
6. **Floats in or out of option 5.** §5.5 permits exclusion. Gated by whether
   any P7 authorization profile or P3 value scale needs a non-integer. *David's
   D4 encoding-neutral schema, Oct 21.*
7. **The YAML spelling of a byte string.** The injectivity question; blocks the
   Oct 28 package. *David, before Oct 28.*
8. **Does D-3's "YAML is the human form" reinstate authoring?**
   `ARCH-0001-PROPOSAL-v0.2.0` §4 withdrew DEC-006's authoring format and
   folded display into DEC-007; the D-3 minute names YAML as the human form.
   The minute and the proposal text disagree and the ADR must say which governs
   and in which direction the one-way mapping runs. *Paul.*
9. **Integer profile range, and what a decoder does with an in-CBOR-range but
   out-of-profile integer** (§5.5). *ADR.*
10. **Where R-O-05's authenticated type indicator lives.** If the signed
    payload is an opaque byte string (tag 24's construct without the tag), the
    indicator must sit in the enclosing map, which makes it a field of the
    native statement and couples it to DEC-003's identifier form. *ARCH-0001
    §4.2 and DEC-003.*
11. **The interchange-matrix row.** `ARCH-0001` §6 has a `COSE_Sign1 + CWT`
    row, but it records no tag-stripping and no key-sort divergence.
    `ARCH-0001-PROPOSAL-v0.2.0` §3.3 asks for the option-5 mapping to be
    "documented as a lossy interchange step" in the ARCH-0001 §6 matrix;
    that row is not yet written, and R-I-01 requires it. *ARCH-0001 v0.2.0.*
12. **Byte-cost of `(key, label)` against §1.1 objective 2.** **[beyond
    source]** Our estimate of one to two orders of magnitude per type reference,
    and the claim that P4 amortises it, are analysis rather than measurement.
    A measured comparison is a natural by-product of the Oct 28 option-5 vs
    option-2 fixtures and would close the one DEC-002 criterion
    `ARCH-0001-PROPOSAL-v0.2.0` §3.3 says was never scored. *David, D5.*

### Defects and ambiguities in RFC 8949 itself

Found by the pass-3 cross-check (artifact against artifact). These are not
questions about our design; they are places where the source does not decide
something it appears to decide, so an implementer has to choose. Recorded here
rather than papered over in the schemas.

13. **§4.2.1's shortest-argument enumeration stops at `uint32_t`.** The four
    sub-bullets of the core deterministic encoding requirements cover 0..23 /
    -1..-24, 24..255 / -25..-256, 256..65535 / -257..-65536 and 65536..4294967295
    / -65537..-4294967296. There is no fifth bullet for the 8-byte argument, so
    for an integer, length, count or tag number of 4294967296 or more, nothing
    in the enumeration says which width to use. Only the general sentence it
    introduces — `rfc-8949#R-0012`, "arguments ... MUST be as short as possible"
    — and §4.1's "shortest form of representing the argument" cover that case.
    It is an incompleteness rather than a contradiction, but the gap is why
    `messages.yaml`'s `argument-uint64` fields carry only `R-0012` and no range
    requirement, while `argument-uint8` through `argument-uint32` carry one each.
    *Our deterministic profile must state the 8-byte case explicitly; D5 package.*
14. **Tag number 35's content type is not determinable from this document.**
    Appendix G says "Tag 35 is not defined by this document; the registration
    based on the definition in RFC 7049 remains in place", and Table 5 omits it.
    Yet §3.4.5.3 states a tag-validity rule for it — "any contained string value
    needs to be valid at the CBOR tag level" — and never says what "string
    value" means. In CBOR a string is major type 2 or major type 3, so RFC 8949
    on its own admits both; the text-string-only reading is the RFC 7049
    registration, which this record does not hold. Pass 1 had narrowed both
    `cbor-tag-35` and `messages.yaml`'s `tag-35` content to a text string on no
    authority in the source; pass 3 widened both and left this note. *No action
    for us under the no-IANA-tags rule; relevant only if a future profile
    carries tag 35.*
15. **Appendix F.1 has no fixture for a `break` directly inside a tag.** The
    taxonomy's subkind 4 names "a definite-length array or map or a tag", but
    all eight listed examples are arrays or maps. `vectors.yaml` therefore has
    no vector for the tag case, and the gap is the source's, not ours: a
    conformance suite should add `c0 ff`. *Test-suite author.*
