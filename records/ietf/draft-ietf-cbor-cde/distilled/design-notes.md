---
record: draft-ietf-cbor-cde
kind: design-notes
title: "draft-ietf-cbor-cde — bearing on our design"
extracted: "2026-10-16"
reviewed_by: ""
---

**Scope and provenance conventions.** Section and appendix numbers with no
document name (`§3.3`, `Appendix C.3.2`) are **draft-ietf-cbor-cde-13**. RFC
8949 is cited as `RFC 8949 §4.2.1` and, where the claim is ours rather than the
RFC's, through this library's record `rfc-8949`. Other library records are
cited by id (`draft-ietf-cbor-serialization`, `draft-mcnally-deterministic-cbor`,
`rfc-9679`). Our own documents are cited by id (`ARCH-0002 P5`, `MD-3`,
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
to option 5; `DECISIONS-0001` tier 1 item 2 records that narrowing with the
words "**Still open: a narrowing is not an acceptance, and no ADR exists**",
and its front matter says "MD-3 NARROWED DEC-002 without accepting it, so
DEC-002 is still open and no code or vector may assume an encoding." `ADR-0001`
(accepted) constrains DEC-002: "CBOR tags and COSE header parameters are IANA
allocated, so they are interchange, not native." **No DEC-002 ADR has been
written**; `PLAN-0003` dates it to Oct 28 (D5), and `DECISIONS-0001` item 4b
calls it "Item 2's instrument". Nothing below may be read as an accepted
encoding decision, and nothing below is written to agree with MD-3.

**Provenance of the source read.** `draft-ietf-cbor-cde-13`, dated **14 October
2025** on its own front page, "Intended status: Best Current Practice",
"Updates: 8949 (if approved)", "Expires: 17 April 2026". The cached bytes
match `record.yaml`'s `content.sha256` (`bc554e3d…605c`, retrieved 2026-09-22).
The revision carries its own editorial note: "// This revision -13 merges all
active pull requests in preparation for the 2025-cbor-17 interim on
2025-10-15." It is a pre-interim merge snapshot, and §*The cost of an unstable
reference* below treats that as a finding rather than a footnote.

> **[correction]** `record.yaml` carries `date: "2026-04-16"`. The document's
> own date line is **14 October 2025**; 2026-04-16 is the day before the stated
> expiry. A record whose `date` is the expiry rather than the publication date
> will put a wrong year in any citation the ADR copies out of it, which is an
> R-O-03 defect in our own metadata rather than in the source. *Fix in
> `record.yaml`; flagged for pass 2 and for the record owner (S1).*

---

## What CDE requires

**One constraint built from three.** §3 ¶4: "CDE combines the constraints of
preferred-serialization with definite-length-only and the
lexicographic-map-sorting constraint." Table 1's `cde` row says the same as
"the combination of preferred-serialization, definite-length-encoding and
lexicographic-map-sorting as interoperability constraints to obtain CDE". §1.2
defines the whole as a RECOMMENDATION, not a mandate: "Out of many potential
and actual deterministic encodings, CDE is RECOMMENDED for implementation and
specification where deterministic encoding is required or desired."

The three constituents, with what each adds beyond RFC 8949:

1. **`preferred-serialization`** (§3.1) — "a combination of the shortest-head
   constraint and tag-specific encoding constraints defined to be part of
   preferred-serialization." For integers it turns an RFC 8949 §4.2.2
   *recommendation* into a mandate (§3.1.1 ¶2): "Integers that can be
   represented by basic major type 0 and 1 MUST be encoded using the
   (shortest-head) deterministic encoding defined for them, and integers
   outside this range MUST be encoded using the Preferred Serialization
   (Section 3.4.3 of RFC 8949 [STD94]) of tag 2 and 3 (i.e., no leading zero
   bytes)." For floating point it adds **nothing**: §3.1.2 — "this
   specification entirely recurs to the shortest-head component of Preferred
   Serialization and does _not_ itself define any additional constraints" —
   and then clarifies five points (zeros, no integer/float mixing, NaNs,
   subnormals, no tag 4/5 equivalence).
2. **`definite-length-only`** (§3.2 ¶1) — "indefinite length encoding MUST NOT
   be used."
3. **`lexicographic-map-sorting`** (§3.3 ¶3) — "the (CDE-encoded) map key of a
   map entry MUST be lexicographically strictly greater than that of the map
   entry immediately preceding it in the encoding of the map, if any."

**The normative surface is six keywords, and three rules.** `bin/bcp14-count`
reports **40** BCP 14 keywords in the source. They sit as follows: **6 in the
document body** — the §1.2 RECOMMENDED above, two MUSTs in one sentence of
§3.1.1, a NOT RECOMMENDED for signalling NaNs in §3.1.2 item 3, the §3.2 MUST
NOT, and the §3.3 MUST; **4 in Appendix B**, two inside an illustrative
hypothetical protocol and two quoted from RFC 9679 §4.2; and **30 in Appendix
C**, which opens by disclaiming them: "It uses RFC2119 language, specifically
the keyword MUST, to highlight the specific items that implementers may want to
check. It does not contain any normative mandates."

> **[analysis]** So what CDE *requires* in BCP 14 terms is three encoder rules:
> the integer rule, the indefinite-length prohibition, and the map-sorting rule.
> Everything else people mean by "CDE" arrives either by reference to RFC 8949
> §4.1/§4.2.1 — which is where the force actually lives — or as declarative
> prose (all of §3.1.2's float clarifications) or as an informative checklist
> (all of Appendix C, including every decoder obligation and the shortest-head
> bands). That matters for R-O-03 in a specific way: "our canonicalisation
> algorithm is CDE" cites a document whose added normative content is three
> sentences, and whose checklists — the part an implementer would actually work
> from — are explicitly non-mandating. It is still a citation, and a good one;
> it is not the closed algorithm the phrase suggests.

**The decoder side is conditional and informative.** Appendix C.3.2 requires a
"CDE-checking decoder" to check preferred-serialization and definite-length-only
(item 1), lexicographic-map-sorting "including rejecting duplicate map keys"
(item 2) and UTF-8 validity (item 3), and closes: "it MUST NOT present to the
application a decoded data item that fails one of these checks". But C.3.2
opens by defining the term as "a shorthand for a CBOR decoder that advertises
_supporting_ CDE", and §2 says of preferred-serialization that "Typically, this
encoding constraint is relevant only for the encoder, as there is nothing to be
gained by enforcing it by itself in a decoder, which will instead accept all
well-formed CBOR." §5 states the consequence: "However, this effect only
accrues if the decoder actually checks that deterministic encoding was applied
correctly."

**What CDE deliberately excludes.** Application-level determinism, which it
names ALDR and puts out of scope (§1.1): "ALDR rules are situated at the
application-level, i.e., on top of CDE, and address requirements on
deterministic representation of application data that are specific to an
application or a set of applications." Appendix C note 3: "Preferred
serialization and CDE only affect serialization. They do not place any
requirements, exclusions, mappings or such on the data model level." And
Appendix B: "While CDE ensures determinism at the encoding layer, requirements
at the application layer may also be necessary."

---

## What we adopt

**The decomposition and its names.** `preferred-serialization`,
`definite-length-only`, `lexicographic-map-sorting`, `cde`, "encoding
constraint", "encoding constraint set" (§1.2). This is the vocabulary our
profile should be stated in, whatever DEC-002 decides, because it lets a
reviewer check our profile constraint by constraint instead of reading prose.
`rfc-8949`'s extraction already lists fourteen decisions RFC 8949 §4.2 leaves
open; CDE supplies the names for three of them and settles four more (below).

**The encoding-constraint / interoperability-constraint distinction (§2, Table
1).** §2 separates a constraint the encoder merely follows from one the decoder
*enforces*: definite-length-encoding is "often yes (enabling partial
implementations in the decoder)" and lexicographic-map-sorting is "an
interoperability constraint specifically for _Common Deterministic Encoding_
(CDE)". This is condition (2) of `canonical-encoding` — decoder rejection — in
the source's own words, and it is the clearest external statement we have that
`ARCH-0002` P5 is not an eccentricity: "For most of these use cases, the
benefits of the encoding constraints for deterministic serialization not only
require the encoder to follow them, but also need the constraints to be
enforced ("checked") by the decoder" (§2).

**The strictly-greater phrasing of map sorting (§3.3 ¶3), in preference to RFC
8949 §4.2.1's.** CDE's aside says why: with preferred-serialization and
definite-length-only in force, "multiple entries with the same map key would
have the same (deterministic) map key serialization and would therefore be
consecutive when sorted", so the constraint "is deliberately phrased to require
consecutive entries to have strictly increasing map keys; with the other CDE
encoding constraints, this prevents encoding multiple entries that have the same
key." One rule discharges both `rfc-8949` row 1 (ordering) and row 10
(duplicate keys), and it is checkable inline against the previous key with no
table of seen keys — which is exactly the property mofn#73's single-pass
rejecting decoder needs.

**§3.1.2 item 2 — no integer/float mixing.** "There is no attempt to mix
integers and floating point numbers, i.e., all floating point values are encoded
as the preferred floating-point representation that accurately represents the
value, independent of whether the floating point value is, mathematically, an
integral value (choice 2 of the second bullet in Section 4.2.2 of RFC 8949
[STD94])." This closes `rfc-8949` row 6, where RFC 8949 offered three rules and
only hinted at a preference, and it agrees with the "no cross-type value
equivalences" declaration that record's design notes propose for option 5.

**The ALDR layering (§1.1, Appendix B) as the home for everything option 5 adds
on top of an encoding.** Appendix B gives the two operations by name:
"constraining the set of data items handled (_exclusions_, e.g., no compressed
point representations) and defining further mappings (_reductions_, e.g.,
conversions to uncompressed form)". It also answers, in advance, the reviewer
objection that a reduced profile forks the ecosystem: ALDR rules "enable simply
using implementations of the common CDE; they do not "fork" CBOR in the sense
of requiring distinct generic encoder/decoder implementations for each
application." Appendix A.1 adds that they impose no floor on implementations:
"there is no requirement that implementations of that set of ALDR rules support
floating point numbers (or any other kind of number, such as arbitrary precision
integers or 64-bit negative integers) when they are used with applications that
do not use them."

**"Partial Implementation" as the honest name for our encoder (§1.2).** "A
decoder or encoder that is not generic, but usually limited to the needs of
specific (a specific set of) applications." Under option 5 our encoder is not a
generic CDE encoder and should not claim to be; it is a partial implementation
plus an ALDR ruleset. Saying so in the ADR costs one sentence and prevents a
conformance claim we cannot support.

**Appendix B's RFC 9679 precedent, for DEC-003.** "As an example, [RFC9679] is
intended to derive a (deterministic) thumbprint from a COSE key [STD96].
Section 4 of [RFC9679] provides the rules that are used to construct a
deterministic application-level representation (ALDR rules)." DEC-002's own
sibling DEC-003 says "Must specify: canonical key bytes before hashing"
(`ARCH-0001` §7), and `canonical-encoding` records that the rcbor spike's
`keyid()` "hashes the key bytes it is handed with NO canonical encoding step".
CDE names a worked, published answer to precisely that, and this library holds
it (`rfc-9679`, extracted under the same issue). Adopt the shape: a short,
explicit exclusion-and-reduction rule set, in the specification, for the bytes
that get hashed.

**§2's closing note, as external support for P4.** "Note that the objective to
have a deterministic serialization for a specific application data item can only
be fulfilled if the application itself does not generate multiple different CBOR
data items that represent that same (equivalent) application data item." That is
`ARCH-0002` P4's critical-path claim — "This puts canonical serialization on the
critical path for the semantic layer, not just the signing layer" — stated from
the other side. `DECISIONS-0001` T1-B currently **holds** P4; this is evidence
for it, and the strongest single sentence we have.

**The negative fixtures of Appendix D.3 (Table 6).** Eight rows, each a
non-CDE encoding with its hex: `a2616200616101` ("Incorrect map key ordering"),
`98020405` (array length not preferred), `1900ff` (integer not preferred),
`c34a00010000000000000000` ("Bignum with leading zero bytes"), `fa41280000`
(float not preferred), `fa7fc00000` (NaN not preferred), `c243010000` ("Integer
value too small for bignum"), `5f4101420203ff` ("Indefinite length encoding").
These go into `examples/` and straight into the D5 package as the decoder's
rejection suite. Appendix E's Table 7 does the same job for the integer 1
(`0x01` preferred; `0x1801`, `0x190001`, `0xc24101`, `0xc2420001` and
`0xc25f41004101ff` not).

---

## What we adapt, and how

**The integer seam — we delete the far side rather than implement it.** §3.1.1
mandates tag 2/3 for integers outside the basic range. Option 5 excludes major
type 6 (`ADR-0001`; `ARCH-0001-PROPOSAL-v0.2.0` §3.3), so we cannot satisfy that
clause; we make it vacuous by restricting the value range to RFC 8949 §2's
`-2^64..2^64-1`, which `rfc-8949`'s extraction already proposes narrowing
further under RFC 8949 §5.5. Appendix A.1's sentence quoted above licenses this
as an ALDR-level exclusion. **The boundary condition must be written down:**
the moment a profile field needs a value outside the basic integer range,
option 5 stops being expressible as CDE-plus-restrictions and becomes a
divergence, because CDE's encoding of such a value *is* tag 2/3 and nothing
else. Nothing in our model is near that boundary today — `Threshold.k`/`n`,
validity instants and weights are small; digests and key material are byte
strings — so the cost is a stated limit, not a lost capability.

**The decoder checklist — promoted from informative to normative, and narrowed.**
We take C.3.2 items 1–3 and its closing MUST NOT as the content of our decoder
rule, and restate them under `ARCH-0002` P5 with BCP 14 force, because in the
source they are informative (Appendix C opening) and conditional on a decoder
*advertising* CDE support. Narrowed, because C.3.2 is silent on the "expected"
level: an option-5 decoder must additionally reject major type 6, simple values
outside `false`/`true`/`null`, and anything outside the profile's value ranges.
Those are data-model rejections, which Appendix C note 3 puts outside CDE
altogether.

**Floats — exclude, or adopt the single-NaN ALDR rule; not CDE's default.**
§3.1.2 preserves NaN payloads and the sign bit, trimming only trailing zero
bits (item 3 and C.1.1 item 2), and encodes signalling NaNs on request —
"the use of signaling NaNs by application protocols is NOT RECOMMENDED but when
presented by an application these are encoded by using a leading significand bit
of 0". Table 5 then spends roughly twenty rows on distinct NaN encodings. CDE
offers the exit in the same breath: "an application's ALDR rules can decide that
it only ever allows a single NaN value that would be encoded as 0xf97e00, so a
CDE implementation focusing on this application would not even need to provide
processing for other NaN values" (§3.1.2, after item 5). Either exclusion
(RFC 8949 §5.5 permits removing floats entirely) or the single-NaN rule is
citable; CDE's default is not usable for us, for the reason in *What we reject*.

**The CDDL control operator — usable, but not yet citable.** §4 adds `.cde` and
`.cdeseq`, "exactly like .cbor and .cborseq except that they also require the
encoded data item(s) to be encoded according to CDE", and §6 Table 2 asks IANA
to register both against `[RFCXXXX]`. **[analysis]** `R-M-12` governs "type
identifiers, predicate types, tags, and header parameters"; a CDDL control
operator is none of those and never appears on the wire, so `.cde` does not
offend the no-registry rule and a reviewer who says otherwise has confused the
schema layer with the encoding layer. What it *does* cost is a citation to an
unregistered operator: D4's schema (Oct 21) would depend on a name whose
registry entry is a placeholder in a draft. Either state the constraint in prose
beside the CDDL, or use `.cde` and mark it pending.

**Tag 24's idiom without tag 24.** §4's worked example is
`leaf = #6.24(bytes .cde any)`. Under option 5 the same shape is
`bytes .cde any` with no `#6.24` wrapper, which CDDL expresses perfectly well.
What we lose is what `rfc-8949`'s extraction already records as the tag-24
tension: a generic tool can no longer tell that the byte string holds CBOR. The
new fact here is narrower and worth recording — **the one place CDE shows how to
formalise an embedded deterministically-encoded payload uses the tag we
forbid**, so our schema deviates visibly from the document's own example and
should say why in a comment.

**"Common" is the claim we cannot inherit.** §1 sells CDE as a practice "which
can be shared by a large set of applications with potentially diverging detailed
application requirements". An option-5 profile is a partial implementation plus
an ALDR ruleset, so the interoperability benefit we get is one-directional: our
output is readable by any CDE-checking decoder, but a conformant CDE encoder can
emit things we reject (tags, non-trivial NaNs, bignums). That asymmetry belongs
in the `ARCH-0001` §6 interchange matrix row that `R-I-01` requires and that
`DECISIONS-0001` notes is still unwritten.

---

## What we reject, and why

**CDE's NaN handling, if floats are admitted at all.** Preserving payloads and
sign makes the *encoding* injective while leaving the *application* with many
byte strings for what most applications treat as one value — which is condition
(1) of `canonical-encoding` failing one layer up, on exactly the path P4 uses
to turn a vocabulary into a hash. The live WG document is harsher than we are:
`draft-ietf-cbor-serialization` §4.1 requires that "Encoders MUST NOT output any
NaN other than the half-precision NaN 0xf9 0x7e 0x00" and that other NaNs be
rejected or coerced. We take the same position by ALDR rule, not by
reinterpreting CDE.

**Signalling NaNs** (§3.1.2 item 3): NOT RECOMMENDED in the source, excluded
outright by us.

**The re-encode-and-compare conformance check.** Appendix C's opening note: "If
a generic decoder needs to be used that does not "support" CDE, a simple (but
somewhat clumsy) way to check its input for proper CDE encoding is to re-encode
the decoded data with CDE and check for bit-to-bit equality with the original
input." `R-O-05` forbids it in terms — a verifier "SHALL NOT canonicalize input
as part of verification". **[analysis]** This is the sharpest single collision
between CDE and our requirements, and it is not a contradiction of a CDE rule,
because the sentence is informative advice about how to cope with a
non-checking library. But it is the deployment default: most CBOR libraries do
not ship a CDE-checking decode path, so a team told to "use CDE" will reach for
re-encoding, and `canonical-encoding` names that as the finding that would
overturn its whole answer — "If checking canonicality on decode cannot be done
without re-encoding, then condition (2) drags the canonicaliser of the producer
back into the verifier, the R-O-05 separation is cosmetic, and DSSE is simply
right". Option 5 must therefore state a positive rule: **the CDE checks are
performed inline on decode and SHALL NOT be discharged by re-encoding.** CDE's
C.3.2 is weak evidence that inline checking is feasible — the WG wrote MUSTs
for it — but CDE supplies no algorithm, and mofn#73 is the experiment that
settles it.

**Appendix C's MUSTs as requirements.** They are the most useful text in the
document and they are, by its own statement, not mandates. Any requirement we
state because of them is ours, authored, and must be marked so — `R-O-03`
applied to a sentence rather than to a filename.

**"Our canonicalisation algorithm is CDE", as a citation.** The Status of This
Memo is explicit: "It is inappropriate to use Internet-Drafts as reference
material or to cite them other than as "work in progress."" An ADR that names
CDE as the algorithm cites a work in progress as reference material, against the
document's own instruction. The citable form is set out under *The cost of an
unstable reference* below: cite **RFC 8949 §4.2.1 (STD 94)** for the rules, name
CDE as the profile the project tracks, and list the four CDE-only additions
explicitly as ours.

---

## Mapping to our decisions

### 1. Every CDE rule against option 5 as drafted

"Option 5 as drafted" is `ARCH-0001-PROPOSAL-v0.2.0` §3.3 — "CBOR as the
canonical encoding, using the CBOR data model and deterministic encoding rules,
but with **no reliance on the IANA CBOR Tags registry and no native use of COSE
header parameters**" — together with `MD-3` ("CBOR data model, no IANA tags,
COSE as export only; type identity is `(defining key, label)` per P1; YAML is
the human form with a canonical one-way mapping"), and the documents that
constrain it: `ADR-0001`, `ARCH-0002` P1 and P5, `R-O-03`, `R-O-05`.

**Read the "silent" rows literally.** Neither §3.3 nor MD-3 names a
deterministic encoding profile at all — not CDE, not RFC 8949 §4.2.1, not
dCBOR, not CTAP2. Where a row says *silent*, the position in the "our side"
column is from this library's `rfc-8949` extraction or from `canonical-encoding`,
which are evidence, **not decisions**. They are marked `[8949]` and `[topic]`.

**A · the three constituent constraints**

| # | CDE rule | locator | option 5 as drafted | relation |
|---|---|---|---|---|
| CDE-01 | `cde` = `preferred-serialization` + `definite-length-only` + `lexicographic-map-sorting` | §3 ¶4; Table 1 | names no profile | **silent** |
| CDE-02 | shortest-head for all major types | §3.1 ¶1; C.1.1 item 1 | `[8949]` adopts §4.2.1 | **same** |
| CDE-03 | shortest-argument bands 0–23 / 24–255 / 256–65535 / 65536–4294967295 and negatives | C.1.1 item 1 sub-bullets | `[8949]` same bands | **same — including the same gap** (no 8-byte band in either; see defect D-2) |
| CDE-04 | integers in the basic range MUST use mt0/mt1 shortest-head; **outside it MUST use tag 2/3**, no leading zeros | §3.1.1 ¶2; C.1.1 item 3; D.1; D.3 | major type 6 excluded entirely | **divergent unless the value range is restricted** — see §2 restriction R2 |
| CDE-05 | tag heads take shortest-head; tag definitions may add their own preferred serialization | §1.2; C.1.1 item 1 | no tags | **stricter** |
| CDE-06 | new tag registrations are recommended to address determinism "in the context of CDE"; a tag's constraints may exceed its preferred serialization | §3.1.1 aside | no tags | **stricter**, and it makes CDE's open-ended part vacuous — see §4, finding 1 |
| CDE-07 | indefinite length MUST NOT be used, strings and arrays/maps alike | §3.2 ¶1; C.2 | `[8949]` forbids, and rejects on decode | **same** (encoder); **stricter** (decoder) |
| CDE-08 | map entries strictly increasing, bytewise on CDE-encoded keys | §3.3 ¶3 | `[8949]` adopts §4.2.1 ordering | **same** |

**B · what `preferred-serialization` resolves for floats**

| # | CDE rule | locator | option 5 as drafted | relation |
|---|---|---|---|---|
| CDE-09 | floats take the shortest head preserving the value; the application has no control over size | §3.1.2 ¶2 | floats in or out is open | **silent** |
| CDE-10 | zeros get no special action; `-0.0` → `0xf98000` | §3.1.2 item 1; D.2 | — | **silent** |
| CDE-11 | no integer/float mixing (RFC 8949 §4.2.2 choice 2) | §3.1.2 item 2 | `[8949]` declares no cross-type equivalences | **same** under that reading |
| CDE-12 | NaN payloads and sign preserved; shortened only by removing trailing zero payload bits; quiet NaN leading significand bit 1 | §3.1.2 item 3; C.1.1 item 2 | one NaN or none | **looser than we need** — rejected above |
| CDE-13 | signalling NaNs NOT RECOMMENDED but encodable | §3.1.2 item 3 | excluded | **stricter** |
| CDE-14 | subnormals get no special handling | §3.1.2 item 4 | — | **silent** |
| CDE-15 | no presumed equivalence between basic floats and tag 4/5 representations | §3.1.2 item 5 | tags 4/5 unavailable | **stricter** |
| CDE-16 | encoders MUST support half- and single-precision floating point | C.1.1 item 2 | — | **silent**; a real implementation cost if floats are admitted (Appendix F exists for it) |

**C · the decoder side, validity, and standing**

| # | CDE rule | locator | option 5 as drafted | relation |
|---|---|---|---|---|
| CDE-17 | CDE encoders MUST emit basic validity: no duplicate keys, valid UTF-8 | C.3.1 item 3 | P5 requires all three RFC 8949 levels | **same** |
| CDE-18 | sorting makes duplicate keys unencodable — **except** RFC 8949 §5.6.1's `-0.0` = `0.0`, which "needs to be checked with extra code for a full validity checker" | §3.3 aside | P5 forbids skipping any validity check | **stricter**: the extra check is ours to implement, or floats are barred from key position |
| CDE-19 | CDE-checking decoders MUST check both other constraints, the sorting including duplicate rejection, and UTF-8; and MUST NOT present a failing item to the application | C.3.2 items 1–3 and closing | P5 rejects at all three levels | **same in content, stricter in standing** |
| CDE-20 | those decoder duties attach only to a decoder that "advertises _supporting_ CDE" | C.3.2 opening | our decoder is the only decoder in scope | **stricter** |
| CDE-21 | Appendix C "does not contain any normative mandates" | Appendix C opening | P5 is normative | **stricter** |
| CDE-22 | a non-CDE generic decoder may check by re-encoding and comparing bitwise | Appendix C opening, last ¶ | `R-O-05` forbids canonicalising during verification | **divergent on the verification path** — see R6 |
| CDE-23 | the benefit "only accrues if the decoder actually checks" | §5 | same position, as a rule | **same** |

**D · what CDE leaves to the application, or does not address**

| # | CDE rule or absence | locator | option 5 as drafted | relation |
|---|---|---|---|---|
| CDE-24 | CDE affects serialization only — no data-model requirements, exclusions or mappings | Appendix C note 3; §3.1.2 after item 5 | option 5 is largely data-model exclusions | **orthogonal**: option 5's additions are ALDR-level by CDE's own taxonomy |
| CDE-25 | ALDR rules sit on top of CDE, out of scope, as exclusions and reductions, published by the protocol or a ruleset document | §1.1; Appendix B | option 5 is such a ruleset but does not say so | **silent**, and nameable |
| CDE-26 | **array element order: not addressed anywhere in CDE** | — | `[topic]` condition (5) | **both silent** — and silence, not prohibition, is what R-O-03 needs |
| CDE-27 | **Unicode normalization: explicitly not required** | C.3.1 note | `[topic]` condition (6) | **both silent**; CDE declines it on the record |
| CDE-28 | map key types: unrestricted | inherited, RFC 8949 §3.1 | `[8949]` proposes text-string keys | **silent / prospectively stricter** |

**28 rules compared. Zero rows where option 5 is looser than CDE** — CDE-12 is
the one row where CDE is looser than we need, which is the same fact read from
the other side.

### 2. So what is option 5's relation to CDE?

Three answers, at three levels of precision.

**As drafted: no relation. Option 5 does not name a canonicalisation
algorithm.** §3.3 says "deterministic encoding rules"; MD-3 says "CBOR data
model". Issue #39 asks what option 5's relation to the IETF baseline is, and
the first honest finding is that the question is **underdetermined by our own
documents**. `R-O-03` requires a canonicalisation algorithm to be "cited, not
invented silently", and a narrowing that names no algorithm has not yet
discharged it. Naming one is ADR work, not extraction work, and it is the
cheapest R-O-03 fix available to the Oct 28 package.

**Under the natural reading: a subset of the encodings, a superset of the
obligations.** Read option 5's "deterministic encoding rules" as RFC 8949
§4.2.1 — what `rfc-8949`'s extraction adopts — and every option-5 encoding is a
CDE-conformant encoding, because each rule option 5 adds *removes* encodings
(no major type 6, no `undefined`, no indefinite lengths on decode, a narrower
integer range, at most one NaN). The containment is strict: CDE admits
encodings we reject (a `c249…` bignum, `f97e01`, an unsorted-but-tagged
structure is not CDE but a sorted tagged one is). In the other direction our
obligations are a superset: we require decoder rejection normatively, at the
expected level as well, and we forbid the re-encode fallback. So —
**option 5 restricts CDE at the serialization layer and extends it at the
application and verifier layers.** It is neither a pure subset nor a superset;
it is a subset of the *bytes* and a superset of the *duties*.

**Expressible as "CDE plus these restrictions" — yes, and CDE supplies the
vocabulary for the "plus".** One rule has to be made vacuous rather than
restricted (CDE-04, the integer seam), and that is the only obstruction. Under
CDE's own taxonomy the restrictions are an **ALDR ruleset** (§1.1, Appendix B),
which CDE declares out of scope and encourages protocols to publish. The eleven
restrictions, in the form the ADR can copy:

| R | restriction option 5 adds | kind | why CDE permits it |
|---|---|---|---|
| **R1** | major type 6 MUST NOT appear; decoders reject it | exclusion | CDE neither requires nor forbids tags per message; Appendix C note 3 puts data-model exclusions outside CDE |
| **R2** | integer values restricted to RFC 8949 §2's `-2^64..2^64-1`, narrowed further by profile range | exclusion | makes CDE-04's tag 2/3 clause vacuous; Appendix A.1 licenses non-support of "arbitrary precision integers" |
| **R3** | simple values limited to 20/21/22; `undefined` (23) excluded | exclusion | RFC 8949 §3.3 Table 4; P5 forbids the encoder-substitute use of `undefined` |
| **R4** | floats excluded, or admitted with exactly one NaN (`0xf97e00`), no signalling NaNs, and floats barred from map-key position | exclusion + reduction | §3.1.2's own ALDR paragraph; RFC 8949 §5.5 for total exclusion; CDE-18 for the key-position rule |
| **R5** | map keys restricted to text strings | exclusion | RFC 8949 §5.6; CDE is silent on key types |
| **R6** | the CDE checks are performed **inline on decode**, normatively, and SHALL NOT be discharged by re-encoding | obligation | contradicts no CDE rule; Appendix C's re-encode note is informative advice — and `R-O-05` forbids it |
| **R7** | a canonical order for set-valued fields carried in arrays | addition | CDE is **silent** on array order (CDE-26); `[topic]` records the construction as ratified twice over — RFC 8949 §4.2.1 for keys, RDFC-1.0 §5 for sets |
| **R8** | a declared Unicode normalisation rule, or an explicit refusal plus rejection of unnormalised input | addition | CDE explicitly declines to require normalization (CDE-27) |
| **R9** | an authenticated type indicator naming the profile, carried key-relatively | addition | CDE supplies none; `.cde` is a schema assertion, not an on-wire indicator |
| **R10** | per-kind handling of invalid items, stated | addition | required of us by RFC 8949 §5; CDE does not address it |
| **R11** | the embedded-CBOR pattern as a bare `bstr`, not `#6.24` | exclusion | CDE's §4 example uses `#6.24`; the construct survives without the tag |

> **[analysis]** R7 and R8 are the two that cannot be reached by subtraction.
> Everything else option 5 does is *delete cases*, which is the cheap route to
> condition (1) that `canonical-encoding` already identified; R7 and R8 are
> *additions*, and no candidate profile supplies them. CDE's contribution is
> that it gives them a place to live and a name — an ALDR ruleset — so that
> publishing them is **authored at a declared layer** rather than a silent
> modification of a cited algorithm. That distinction is the whole of R-O-03,
> and it is the single most useful thing CDE does for us.

### 3. The cost of an unstable reference

**Version and status, exactly.** `draft-ietf-cbor-cde-13`, 14 October 2025,
Intended status **Best Current Practice**, "Updates: 8949 (if approved)",
expiring **17 April 2026** — 182 days before this extraction. The revision note
says it "merges all active pull requests in preparation for the 2025-cbor-17
interim on 2025-10-15", so it is a snapshot taken for a meeting. Our
`record.yaml` assesses it `usefulness.verdict: marginal`, "EXPIRED 2026-04-17
and parked. Recorded because it is still widely cited as the deterministic CBOR
profile; the live work is draft-ietf-cbor-serialization."

**Our own documents are in tension about this, and the tension is not
resolved here.** `topics/deterministic-cbor-profiles.yaml` says "the CBOR WG is
now writing CDE to close it [the §4.2 gap]". `records/ietf/draft-ietf-cbor-cde/record.yaml`
says CDE expired and parked and that the live work is
`draft-ietf-cbor-serialization`. Both are ours; both are cited; the topic is
`status: open` and names no owner. A reviewer reading only the topic will
believe CDE is the WG's live determinism work, and it is not.

What depending on it costs, concretely:

1. **The citation is disallowed by the document itself.** "It is inappropriate
   to use Internet-Drafts as reference material or to cite them other than as
   "work in progress."" Under `R-O-03` that is not a technicality: the ADR's
   acceptance test is a round-trip fixture package, and a fixture package
   pinned to an expired draft cannot be checked against anything stable.
2. **The successor does not use the name.** `draft-ietf-cbor-serialization-08`
   (29 July 2026, **Standards Track**, Lundblade) contains **no occurrence of
   "CDE"** at all, while defining "deterministic serialization", a §1.3
   "Relation to RFC 8949" and its own CDDL control operator. Its §1.3 explains
   the method in terms that read as a direct critique of CDE's: "This document
   defines new serializations rather than updating those in [STD94]. This
   approach enables the serialization requirements to be expressed directly in
   normative [RFC2119] language and to be defined entirely in this document."
   That is the defect this extraction found in CDE — three normative sentences
   and thirty informative ones — identified inside the working group.
3. **The two live documents already disagree on a rule our fixtures would
   contain.** serialization-08 §5: "Deterministic serialization is the same as
   described in Section 4.2.1 of [STD94] except for the encoding of
   floating-point NaNs", and §4.1 requires `0xf97e00` as the only emittable
   NaN. Every non-trivial NaN row of CDE's Table 5 is forbidden there. Fixtures
   built from Table 5 would encode a rule the WG's live draft prohibits.
4. **CDE's content is registry-coupled where tags are in play.** §3.1.1's aside:
   "As CDE would continually need to address additional issues raised by the
   registration of new tags, this specification recommends that new tag
   registrations address deterministic encoding in the context of CDE. Note
   that not in all cases the tag's deterministic encoding constraints will be
   confined to its definition of Preferred Serialization." A citation to CDE
   for the generic data model is therefore a citation as of a date, because the
   rule set grows with the IANA CBOR Tags registry.
5. **The CDDL operators are unregistered.** §6 Table 2 registers `.cde` and
   `.cdeseq` against `[RFCXXXX]`. D4's schema would cite a placeholder.
6. **The account CDE gives of its neighbours is already stale.** Appendix B
   presents dCBOR as "an early example of a separate document" defining an ALDR
   ruleset on top of CDE, citing `draft-mcnally-deterministic-cbor-13` (10
   August 2025). This library holds that document at **-18** (2026-08-10) and
   its record says that at -18 "it narrows RFC 8949 Sec.4.2 directly and does
   not mention CDE, contrary to common secondary accounts." Five revisions on,
   the layering CDE asserts is not the layering dCBOR claims.

> **[analysis] The citable form, and it costs us nothing.** CDE's own abstract
> says "it does not make technical changes to RFC 8949." So cite **RFC 8949
> §4.2.1 (STD 94, stable, complete in itself)** for the three constraints, and
> name CDE as *the profile this project tracks and the vocabulary it uses*,
> listing CDE's four substantive additions as our own authored rules: the
> integer-seam mandate (which we make vacuous anyway, R2), the §3.1.2 float
> clarifications (which we replace, R4), the strictly-greater phrasing of map
> sorting, and the basic-validity requirement on encoders. That citation
> survives CDE expiring, being renamed, or being replaced by
> `draft-ietf-cbor-serialization`, and it is the same technical content.
> This is a recommendation to the ADR, not a decision, and it is this
> extraction's reasoning rather than anything CDE or our documents state.

### 4. Where CDE cuts against MD-3

Four findings. Two favour the narrowing, two cut against it; all four name an
option. `docs/extraction.md` requires this section and the reason is on the
record: "An extraction that can only confirm is not evidence."

**Finding 1 — for MD-3, and an argument MD-3 does not make. The no-tags rule
closes the one open-ended part of CDE, which is a point in option 5's favour
over option 2.** §3.1.1's aside (quoted above) concedes that CDE's content must
track new tag registrations, and §1.2 makes tag-specific preferred
serializations part of `preferred-serialization` itself. **[analysis]** Under
**option 2** — "CBOR + CDDL as canonical; COSE for signed form" (`ARCH-0001`
§7), with the tag space admitted — the cited algorithm's content is open-ended
by construction: a tag registered next year can add deterministic-encoding
constraints that were not in the document when we cited it. Under **option 5**,
excluding major type 6 renders that whole surface vacuous, and what remains —
shortest-head over major types 0–5 and 7, definite lengths, lexicographic
sorting — is closed and finite. For `R-O-03`, "cite a closed rule set" is
strictly better than "cite a rule set that grows with a registry", and this is
a **governance argument for option 5 that is about determinism rather than
namespaces**. The proposal's §3.2 argument is about who allocates identifiers;
this one is about whether the algorithm we cite stays the same algorithm.
Neither MD-3 nor §3.3 makes it, and it should be in the ADR.

**Finding 2 — against MD-3, for option 1. CDE's own fallback for conformance
checking is re-encoding, which is the thing option 1 does not need.** Appendix
C's opening note licenses "re-encode the decoded data with CDE and check for
bit-to-bit equality with the original input" for any generic decoder that does
not support CDE, which is most of them. `canonical-encoding` records that
**option 1** (canonical S-expressions, RFC 9804) gets condition (2) *by
grammar*: "a decoder that implements c-sexp and not sexp rejects non-canonical
input by construction, single-pass, with no re-encoding". CDE's position is the
inverse — the obligation exists (C.3.2) but it is informative, conditional on
advertisement, and backed by a re-encoding fallback the document itself calls
"somewhat clumsy". **[analysis]** So on condition (2), the single condition
`canonical-encoding` says "nobody writes down", option 1 is structurally ahead
and option 5 pays with machinery: a positive exclusion rule, a decoder
obligation we must author because CDE's is informative, and an unproven claim
that the checks are inline-checkable. mofn#73 exists precisely because that
claim is unproven. This is the same asymmetry the topic found at the namespace
level — "where option 5 must CONSTRUCT registry-freedom by subtraction …
option 1 is registry-free by construction" — now visible at the determinism
level too, in CDE's own text.

**Finding 3 — against MD-3, for option 1 again, on cost. CDE quantifies the
float burden option 5 inherits and option 1 does not have.** §3.1.2 spends five
enumerated clarifications on floats, C.1.1 item 2 obliges encoders to "support
half-precision and single-precision floating point", Table 5 lists roughly forty
float rows of which about twenty are NaNs, and Appendix F ships C code for
binary16 narrowing because "CDE implementations that support floating point
Numbers not only need to decode, but also to encode their 16-bit format". RFC
9804 has no float type at all. **[analysis]** The mitigation is real and
already identified — exclude floats (R4) — but notice what that does to the
comparison: option 5's defence against its own worst area is to delete a data
type, which narrows the data-model advantage that is the *only* reason the topic
gives for preferring options 2/5 over option 1 besides library availability.
The ADR should score the reduced model, not full CBOR, against option 1's
"far poorer data model", because option 5 is not full CBOR.

**Finding 4 — against MD-3's completeness, for an option it does not name:
option 5 **plus a cited ALDR ruleset**, with dCBOR the published candidate.**
CDE is explicit that what MD-3 asks for is two documents, not one: §1.1 puts
ALDR "on top of CDE" and out of scope, Appendix B says ALDR rules "are routinely
provided as part of a specification for a CBOR-based protocol, or, if needed,
can be provided by referencing a shared "ALDR ruleset" that is defined in a
separate document", and it names dCBOR as such a document, supplying the NFC
rule — our condition (6) — that CDE "does NOT include". **[analysis]** MD-3
narrowed DEC-002 to an encoding and said nothing about the ALDR layer, where
conditions (5) and (6) live and where, per `canonical-encoding`, divergence
"fails silently rather than as a signature mismatch". Under `R-O-03` the
question "do we cite dCBOR for the ALDR layer or author our own ruleset?" is
exactly as live as the encoding question MD-3 answered, and no document of ours
poses it. The evidence cuts both ways and the record should say so: dCBOR
supplies condition (6) and the layering; but our own `draft-mcnally-deterministic-cbor`
record says that at -18 it "narrows RFC 8949 Sec.4.2 directly and does not
mention CDE", so citing "CDE + dCBOR" may be citing two documents that no longer
compose. That record's own FX-1 extraction, in flight under this issue, is where
the question gets answered.

**One further cut, which favours no option but rescopes all of them.**
`draft-ietf-cbor-serialization` §5.3.1 is titled "Not Commonly Needed for
Hashing and Signing" and argues: "the payload of a COSE_Sign message (See
[RFC9052]) does not need to be encoded deterministically because it is
transmitted with the message. The recipient receives the exact same bytes that
were signed. Deterministic encoding becomes necessary only when the protected
data is not transmitted as the exact bytes that are used for authenticity or
integrity verification." **[analysis]** `R-O-05` makes our signed payload
exactly that case — bytes signed verbatim, verified before decoding — so by this
argument determinism is **not** required for our signing path at all. What
requires it is the identity path: P4's domain-of-discourse hash, R-M-11's
`description` digest, DEC-003's key thumbprint. That is independently the
conclusion `canonical-encoding` reached ("THE GAP IS IDENTITY, NOT PAYLOADS"),
and it reframes DEC-002: the ADR is choosing an encoding to **name things
with**, not to sign with, and should be scored on conditions (1), (5) and (6)
rather than on signing ergonomics. CDE itself does not make this argument — it
is silent on when determinism is needed, beyond §5's note that the benefit needs
a checking decoder.

### 5. Headers, structures and the export mapping

`docs/extraction.md` requires COSE/CBOR design notes to give the header and
structure mapping. **CDE defines no messages, no headers and no structures** —
it is an encoding-constraint document, which is why this record's
`messages.yaml`, `protocol.yaml` and `state-machine.yaml` are N/A-with-reason
artifacts. What it constrains in our model is *every map we emit*: the statement
map of `ARCH-0002` P2, the `(defining key, label)` pairs of P1, `Threshold`,
`Validity`, and the P4 schema set. The export mapping question belongs to
`rfc-9052` and `rfc-8392`, and the one fact worth carrying here is the direction
of the inequality: per `rfc-8949`'s extraction, **RFC 9052 §9 does not require
map key sorting**, so a conformant COSE producer may emit unsorted header maps.
Option 5's native rule is strictly stronger than COSE's, export is safe, and
**import is not CDE** — which is the asymmetry the unwritten `ARCH-0001` §6 row
has to state. CDE's Appendix B adds a worked instance of the same problem:
CWT's `NumericDate` "allows both integer and floating point numbers … which
allows multiple application-level representations of integral numbers", so a
deterministic CWT export needs an ALDR rule of its own.

---

## Open questions

Items this document cannot settle, with who must. **[beyond source]** marks ones
where this extraction had to reason past both CDE and our own documents.

1. **Which algorithm does option 5 cite?** Option 5 as drafted names none; CDE's
   boilerplate forbids citing it as reference material; `draft-ietf-cbor-serialization`
   is Standards Track but does not use CDE's name and differs on NaNs. The
   recommendation above — cite RFC 8949 §4.2.1, name CDE as the tracked profile,
   list the additions as ours — is **[beyond source]** and is the single
   sentence `R-O-03` is waiting for. *DEC-002 ADR — Paul, Oct 28.*
2. **Floats: out, or in with one NaN?** R4 settles CDE-09 through CDE-16 and
   removes five of `rfc-8949`'s fourteen determinism rows from the Oct 28
   critical path. Gated on whether any P7 profile or P3 value scale needs a
   non-integer. *David, D4 encoding-neutral schema, Oct 21.*
3. **Do we cite dCBOR for the ALDR layer, or author our own ruleset?** CDE
   declares the layer out of scope and names dCBOR as the published candidate;
   our record says dCBOR -18 no longer mentions CDE. **[beyond source]** as a
   question — neither document poses it. *Answerable from
   `draft-mcnally-deterministic-cbor`'s extraction under this issue, then the ADR.*
4. **Is the profile's integer range inside `-2^64..2^64-1`?** R2's boundary
   condition: outside it, option 5 is no longer expressible as CDE plus
   restrictions. *ADR, with D4's field inventory.*
5. **Can the CDE checks be done single-pass on decode, without re-encoding?**
   C.3.2 implies yes and gives no algorithm; Appendix C's fallback assumes no.
   `canonical-encoding` says this is the finding that would overturn its answer.
   *mofn#73 — the ~50-line experiment.*
6. **Canonical order for set-valued arrays (R7) and the normalisation rule
   (R8).** **[beyond source]** CDE is silent on the first and explicitly
   declines the second, so both are authored under any DEC-002 option. Blocked
   behind P4, which `DECISIONS-0001` T1-B currently **holds**. *Paul for P4;
   David for the schema.*
7. **Does the ADR score the reduced model or full CBOR against option 1?**
   Finding 3: once floats and tags are gone, "CBOR's richer data model" is a
   smaller advantage than DEC-002's driver list assumes. *ADR.*
8. **Which record governs CDE's standing in this library** — the topic's "the
   CBOR WG is now writing CDE" or the record's "EXPIRED and parked"? They
   disagree, and `deterministic-cbor-profiles` is `owner: unassigned`. *Library
   housekeeping; assign the topic.*
9. **Does `.cde` go into D4's CDDL?** Compatible with R-M-12, unregistered in
   the source. *David, Oct 21.*

### Defects and ambiguities in the source itself

Places where draft-13 does not decide something it appears to decide, or
contradicts itself. Recorded rather than smoothed over; all are consistent with
a revision that "merges all active pull requests".

- **D-1 · The constraint has two names.** §2 and Table 1 call it
  `definite-length-encoding` (4 occurrences); §3 ¶4, §3.2, Appendix A.1 and
  Appendix C.2 call it `definite-length-only`. A profile that cites "CDE's
  definite-length-only constraint" cites a name Table 1 spells differently, and
  Table 1 is the summary a reader is most likely to quote.
- **D-2 · The shortest-argument enumeration stops at four bytes.** C.1.1 item
  1's sub-bullets cover 0–23/−1..−24, 24–255/−25..−256, 256–65535/−257..−65536
  and 65536–4294967295/−65537..−4294967296, and there is no fifth bullet for the
  8-byte argument. This reproduces, verbatim and in the document whose purpose
  is to help implementers, the incompleteness logged as defect 13 of
  `rfc-8949`'s extraction. It is repaired only by example, in D.1's rows for
  4294967296 (`1b0000000100000000`) and 18446744073709551615
  (`1bffffffffffffffff`). *Our profile must state the 8-byte case as a rule;
  D5 package.*
- **D-3 · "This appendix is informative" appears twice** in Appendix C's opening
  paragraph, around the sentence that disclaims its MUSTs. Editorial, and
  evidence of the merge; worth noting only because the disclaimed MUSTs are the
  part of the document we most want to lean on.
- **D-4 · The duplicate-key claim has a documented hole and no fixture.** §3.3's
  aside says the sorting rule "prevents encoding multiple entries that have the
  same key", then concedes RFC 8949 §5.6.1's `-0.0` = `0.0` case "needs to be
  checked with extra code for a full validity checker". Appendix D.3 has no
  failing example for it. A conformance suite should carry
  `a2f90000…f98000…` — a map keyed on both zeros, which is correctly sorted,
  passes every CDE check, and is an invalid CBOR map. *Test-suite author; and
  it is the reason R4 bars floats from key position.*
