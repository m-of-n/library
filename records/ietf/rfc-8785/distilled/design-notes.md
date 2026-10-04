---
record: rfc-8785
kind: design-notes
title: "rfc-8785 — bearing on our design"
extracted: "2026-10-03"
reviewed_by: ""
---

**Scope and provenance conventions.** Section and appendix numbers with no
document name (`§3.2.3`, `Appendix D`) are RFC 8785. Other sources are named
(`RFC 8949 §4.2.1`). Our own documents are cited by id (`ARCH-0002 P1`, `D-3`,
`R-O-05`). Three markers distinguish voices:

- unmarked prose reports **RFC 8785** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption of the project that the sources
  do not support.

**Decision status, stated plainly.** DEC-002 in `ARCH-0001` §7 (v0.1.1) is
**open** and lists four options. RFC 8785 is the canonicalization half of
**option 3** — "JSON + RFC 8785 JCS as canonical; DSSE for signed form."
`D-3` (2026-09-28, `PLAN-0003`) narrows DEC-002 to proposed option 5; **no ADR
for DEC-002 has been written.** `R-O-05` and `R-O-03`'s scope are *proposed*
text in `ARCH-0001-PROPOSAL-v0.2.0` §3.4 and §7 — R-O-03 itself is live in
`ARCH-0001` §5.3, R-O-05 is not. `ARCH-0002` P1 is accepted (`ADR-0001`); P4 is
**held** per `DECISIONS-0001` T1-B. Nothing below may be read as an accepted
encoding decision. The verdict in *Mapping to our decisions* §6 is a
recommendation to a decision maker.

---

## What we adopt

Six rules, all of them rules RFC 8785 states that RFC 8949 leaves silent or
states more weakly. This is the shorter list and it is worth being clear that
it is not empty: on *reject rather than repair*, JCS is closer to `ARCH-0002`
P5 than RFC 8949 is.

**§3.2.2.2's lone-surrogate rule, as a P5 instance.** "Since invalid Unicode
data like "lone surrogates" (e.g., U+DEAD) may lead to interoperability issues
including broken signatures, occurrences of such data MUST cause a compliant
JCS implementation to terminate with an appropriate error." Terminate, not
substitute. `ARCH-0002` P5: "a failure at any level is a rejection, never a
repair." RFC 8949 §5.3.1 makes invalid UTF-8 *invalid* but §5.3 leaves the
response to the protocol and §5.7 positively offers `undefined` as a
substitute; the RFC 8949 record rejects §5.7 for collision with P5. RFC 8785
needs no such rejection — it already says terminate.

**§3.2.2.3's NaN/Infinity rule, likewise.** "Since Not a Number (NaN) and
Infinity are not permitted in JSON, occurrences of NaN or Infinity MUST cause a
compliant JCS implementation to terminate with an appropriate error." RFC 8949
§4.2.2 hands NaN representation to the protocol as a choice ("the protocol
needs to pick a single representation"); rows 7 and 8 of the RFC 8949 record's
determinism table are open because of it. JSON removes the choice by removing
the values. **[analysis]** This is the same relief the rcbor spike buys by
excluding floats outright, obtained from the substrate rather than from a
profile, and it is a real point in option 3's favour on determinism rows 4–8.

**§3.1's I-JSON constraint on duplicate property names.** "JSON objects MUST
NOT exhibit duplicate property names." Adopted as the "valid" level of P5's
three-level hierarchy, the direct analogue of RFC 8949 §5.3.1's duplicate map
keys and §5.6's "MUST define the behaviour". See the defects list for why the
RFC's own machinery cannot enforce it — the rule is right, the enforcement
story is not.

**§3.1's refusal to normalize Unicode, stated out loud.** "Although the Unicode
standard offers the possibility of rearranging certain character sequences,
referred to as "Unicode Normalization" [UCNORM], JCS-compliant string
processing does not take this into consideration. That is, all components
involved in a scheme depending on JCS MUST preserve Unicode string data "as
is"." RFC 8949 is simply silent here; the RFC 8949 record lists the silence as
determinism gap 2 and open question 5. **We adopt the refusal, not the
silence** — a canonicalizer that normalized would mutate the signer's data, and
under `ARCH-0002` P1 it would silently merge two distinct `(key, label)` types
into one. Merging is worse than splitting. See item 3 of the mapping for what
the refusal obliges us to do instead.

**§3.1's immutability rule for parsed strings.** "An additional constraint is
that parsed JSON string data MUST NOT be altered during subsequent
serializations." Generalised beyond JSON: **a value whose identity is its
lexical form is immutable through the signing path.** This is the same
discipline DEC-003 needs when it says canonical key bytes must be specified
before hashing, and it is the rule the rcbor spike's `keyid()` breaks (topic
answer: it "hashes the key bytes it is handed with NO canonical encoding
step").

**Appendix C's licence to use the canonical form as the wire format.** "Since
the result from the canonicalization process (see Section 3.2.4) is fully valid
JSON, it can also be used as "Wire Format". However, this is just an option
since cryptographic schemes based on JCS, in most cases, would not depend on
that externally supplied JSON data already being canonicalized." This single
sentence is the only place RFC 8785 licenses the architecture R-O-05 requires.
Note what it concedes while licensing it: the *designed* deployment of JCS is
the other one. See mapping item 2.

---

## What we adapt, and how

**§3.2.3's recursive property sorting — the idea, not the comparison basis.**
"JSON object properties MUST be sorted recursively, which means that JSON child
Objects MUST have their properties sorted as well." Correct and necessary.
The comparison basis is UTF-16 code units (mapping item 5) and we replace it
with bytewise order over the encoded form, per RFC 8949 §4.2.1. **An
implementation that does this is not JCS-conformant**, which is the point: the
adaptation cannot be made while claiming the citation.

**§5's three-step procedure — inverted, not amended.** §5's ordering is parse →
check correctness and locate the signature → verify. R-O-05's is verify →
decode → check. Steps 1 and 2 of §5 survive as *post*-verification obligations;
step 2's clause "This also includes locating the property holding the signature
data" disappears entirely, because under R-O-05 the signature is not in the
payload. This is the record's central finding and it has its own section below.

**Appendix F's producer scheme — kept; its consumer scheme — discarded.**
Appendix F's signature creation steps 1–4 (create the data, serialize it,
canonicalize it, sign the canonicalized data) are exactly R-O-05's "Canonicalization
happens once, at authoring time, on trusted input." Steps 5 and 6 — "Add the
resulting signature value to the original JSON data through a designated
signature property" and re-serialize — are rejected, because the embedded
signature is precisely what forces the six-step verifier that follows. The
cleavage is clean: Appendix F's first four steps are ours; its last two, and
its whole verification scheme, are not.

**Appendix D's big-number rule — replaced by exclusion.** "Due to the above,
numbers that do not have a natural place in the current JSON ecosystem MUST be
wrapped using the JSON string type." We do not promote; we exclude. Where a
value outside the double range is genuinely needed it is carried as an integer
mantissa/exponent pair under our own labels — the same shape the RFC 8949
record proposes in place of tag 4 decimal fractions — not as a string whose
lexical form nothing governs. Mapping item 1 shows why the promotion is worse
than it looks.

**Appendix E's "pure string" discipline — promoted to a schema rule.** "That
is, stream- and schema-based parsing MUST treat subtypes as "pure" (immutable)
JSON string types and perform the actual conversion to the designated native
type in a subsequent step." Adapted: every field whose identity is its lexical
form — digest hex, encoded key material, RFC 3339 instants — carries a declared
normal form (case, padding, precision, offset spelling) enforced at authoring
and **rejected**, never repaired, on decode. Appendix E is the best worked
example of this failure in any document we hold, and we take it whichever
encoding wins.

**§3.2.2.3's by-reference number algorithm — adapted by not needing it.** "Due
to the relative complexity of this part, the algorithm itself is not included
in this document." We exclude floats (RFC 8949 §5.5 permits total exclusion;
the rcbor spike already does), which removes the dependency rather than
satisfying it. See mapping item 7 for why this matters to R-O-03 specifically.

---

## What we reject, and why

**§5's mandated ordering.** The headline rejection; argued at length in mapping
item 2. R-O-05 requires the exact inverse and gives documented reasons.

**Appendix F's verification scheme in full, and the embedded-signature pattern
it presupposes.** Six steps of which the first five operate on unauthenticated
input, including a structural mutation of it (step 3, "Remove the signature
property from the parsed JSON object") and a run of the canonicalizer over it
(step 5). Under R-O-05 nothing but signature verification may touch received
bytes first.

**§3.1's IEEE 754 double constraint as the model's only numeric type.** Not
because our current fields exceed it — they do not (mapping item 1) — but
because it makes the integer/float distinction unavailable at P5's "valid"
level, and because Appendix D's escape hatch is not canonicalized.

**§3.2.3's "array element order MUST NOT be changed" as a sufficient
canonicalization rule.** Correct for sequences, prohibitive for the logical
sets we carry in arrays. Mapping item 4. This is the strongest single
structural objection and, unlike §5, it cannot be reconciled by scoping a
citation.

**§3.2.3's UTF-16 code-unit sort basis, and the Note that licenses departing
from it.** "However, in practice, property names are rarely defined outside of
7-bit ASCII, making it possible to sort string data in UTF-8 or UTF-32 format
without conversion to UTF-16 and still be compatible with JCS." The premise is
false for our model **by requirement**: `ARCH-0002` P3 says "Multilingual
descriptions are a requirement, not a nicety," and under P1 a label is text a
key's owner chooses. Mapping item 5.

**JSON's lack of a byte-string type** — not a JCS choice, but a substrate
property option 3 inherits whole. RFC 8949 §5.6.1 makes text strings distinct
from byte strings "even if composed of the same bytes," and the RFC 8949 record
calls that "the distinction we most depend on": `Key` material, `KeyId`
digests, signatures and `ArtifactId.digest` are bytes, P1 labels are text.
JSON collapses them into one scalar type and JCS governs neither the alphabet
nor the case of the text encoding that results.

**DEC-002 option 3's own named pairing with DSSE, as written.** DSSE's
`payloadType` is a global string. `ADR-0001` (accepted) excludes centrally
allocated identifiers from the native model. Mapping item 8.

**§3.2.2's delegation of its own normative future.** "In the (unlikely) event
that a future version of ECMAScript would invalidate any of the following
serialization methods, it will be up to the developer community to either stick
to this specification or create a new specification." R-O-03 exists so that a
canonicalization algorithm has a citable owner. This sentence says it has none.

---

## Mapping to our decisions

### 1. The number problem, costed against `ARCH-0001` §4.1

**What the source says.** §3.1: "JSON number data MUST be expressible as IEEE
754 [IEEE754] double-precision values. For applications needing higher
precision or longer integers than offered by IEEE 754 double precision, it is
RECOMMENDED to represent such numbers as JSON strings; see Appendix D for
details on how this can be performed in an interoperable and extensible way."
Appendix B note (1): "For maximum compliance with the ECMAScript "JSON" object,
values that are to be interpreted as true integers SHOULD be in the range
-9007199254740991 to 9007199254740991."

**Field by field.**

| `ARCH-0001` §4.1 field | magnitude | cost under §3.1 |
|---|---|---|
| `Threshold.k`, `Threshold.n` | small integers, `1 ≤ k ≤ n` | **none.** Exactly representable; `n` bounded by the member list |
| `Validity` as epoch **seconds** | ~1.8 × 10⁹ | **none** |
| `Validity` as epoch **milliseconds** | ~1.8 × 10¹² | **none** |
| `Validity` as epoch **microseconds** | ~1.8 × 10¹⁵ | **none**, with ~5× headroom below 2⁵³ ≈ 9.007 × 10¹⁵ — exact until roughly 2255 |
| `Validity` as epoch **nanoseconds** | ~1.8 × 10¹⁸ | **excluded.** Two orders of magnitude past 2⁵³; not exactly representable *today*, not at some future date |
| `Validity` as an RFC 3339 **string** | — | not a number problem; an Appendix E problem, below |
| `ArtifactId.digest` | `{ alg, hex }` | **none from §3.1** — `hex` is already a string in our model. A different cost applies; see below |
| `Endorse` weight *w* | unspecified | **none if integral.** If fractional, imports the whole float chain |
| any counter or sequence number | ≤ 2⁵³ for any plausible deployment | **none** |

**Conclusion, stated plainly: the number rule does not disqualify option 3.**
Nothing in `ARCH-0001` §4.1 as written requires an integer past 2⁵³ or a
decimal needing exactness. The ceiling is real and it is precisely locatable —
it falls between microsecond and nanosecond time resolution, and on nothing
else we have. Two recommendations follow and neither is expensive:
`Validity` instants are integers at second or millisecond resolution, and
`Endorse` weight *w* is an integer out of a fixed denominator (basis points),
not a float. Both are recommendations, not decisions; D4 owns them.

**Four costs that are real, in descending order of force.**

**(a) Appendix D's escape hatch is not canonicalized, and the RFC demonstrates
it.** The moment a value is promoted to a string, JCS stops governing it —
§3.1's Unicode rule says preserve "as is". Appendix E shows exactly this
failure with the same value spelled two ways: canonicalizing the same logical
object through two different parse paths yields

```
{"big":"055","time":"2019-01-28T07:45:10Z","val":3.5}
{"big":"55","time":"2019-01-28T07:45:10.000Z","val":3.5}
```

and the RFC's own comment is "In this case, the string arguments for "big" and
"time" have changed with respect to the original, presumably making an
application depending on JCS fail." **[analysis]** This is the topic answer's
condition (1) — injectivity — failing, and failing *inside the mechanism JCS
offers as the remedy for the number constraint*. The remedy converts a
number-canonicalization problem into a string-canonicalization problem the
specification explicitly declines to solve. For `ARCH-0002` P4's hash-as-identity
that is total: `"055"` and `"55"` are two domains of discourse.

**(b) The `Validity`-as-RFC-3339-string path walks into Appendix E directly.**
The RFC's own worked example of the failure uses a field named `time` holding
`"2019-01-28T07:45:10Z"`, which a reviver-based parser converts to a `Date` and
re-serializes as `"2019-01-28T07:45:10.000Z"` — a **broken signature from a
correct JSON library using a documented API**. Appendix E's answer is a
discipline imposed on every parser in the ecosystem ("MUST treat subtypes as
"pure" (immutable) JSON string types"), not a mechanism. Option 3 therefore
makes our most security-relevant scalar — the validity window — the RFC's own
canonical example of a signature-breaking hazard.

**(c) The integer/float distinction is unavailable at P5's middle level.** JSON
has one number type, so `3` and `3.0` canonicalize to the same bytes. For
determinism that is a *benefit* (the RFC 8949 record's determinism row 6,
integer-vs-float for integral values, simply does not arise). For `ARCH-0002`
P5 it is a loss: integrality is unrepresentable at the "valid" level and falls
entirely to the application's "expected" check. RFC 8949 §2 makes "integer and
floating-point values are distinct in this model" a data-model fact; in JSON it
can only ever be a schema assertion. **[analysis]** This is a straight trade,
not a defect, and it should be scored as one: option 3 removes four determinism
rows and loses one validity level.

**(d) Digests and keys do not cost us under §3.1 but cost us elsewhere.** They
are already text in `ARCH-0001` §4.1 (`digest: { alg, hex }`), so nothing is
promoted. But JSON has no byte type at all, so `Key` material, `KeyId` and
signatures must also become text, and **JCS governs the string but not the
encoding of bytes into it**: hex case, base64 vs base64url, padding present or
absent. Two spellings of one digest are two canonical documents and two
identities. RFC 8785 says nothing; the obligation is ours. This is the same
class of problem as the RFC 8949 record's "YAML spelling of a byte string",
except that in option 3 it is on the **wire**, not only in the human form.

### 2. §5's mandated ordering against R-O-05 — the central finding

**What the source requires, verbatim.** §5:

> When JCS is applied to signature schemes like the one described in Appendix
> F, applications MUST perform the following operations before acting upon
> received data:
>
> 1.  Parse the JSON data and verify that it adheres to I-JSON.
>
> 2.  Verify the data for correctness according to the conventions defined by
>     the ecosystem where it is to be used.  This also includes locating the
>     property holding the signature data.
>
> 3.  Verify the signature.
>
> If any of these steps fail, the operation in progress MUST be aborted.

Appendix F expands step 3 into six steps, of which five precede any
cryptographic operation: parse, read the signature value, **remove the
signature property from the parsed object**, re-serialize, **canonicalize**,
and only then "Verify that the canonicalized data matches the saved signature
value using the algorithm and key used for creating the signature."

**What we require, verbatim.** R-O-05 (`ARCH-0001-PROPOSAL-v0.2.0` §7):

> The signed payload SHALL be the canonical encoding verbatim, carried with an
> authenticated type indicator. A verifier SHALL verify the signature before
> decoding and SHALL NOT canonicalize input as part of verification. Any
> human-facing form SHALL be regenerated from verified canonical bytes.

These are not two styles. §5 and Appendix F require, on **unauthenticated
input**: a full parse; an application-semantic correctness check; a structural
mutation; a re-serialization; and a run of the canonicalizer. R-O-05 forbids
every one of them before verification. The conflict is total and it is
normative on both sides — §5 uses MUST, R-O-05 uses SHALL.

**Three sharper observations.**

**§5 step 2 puts P5's third level before the signature.** "Verify the data for
correctness according to the conventions defined by the ecosystem where it is
to be used" is, in `ARCH-0002` P5's terms, the **expected** level — "is it what
this application requires? ... the application". §5 runs it on input nobody has
authenticated. P5 as drafted does not say *when* the three levels run; §5 shows
why it must. **[analysis]** P5 and R-O-05 are not independent: P5 orders the
levels relative to each other, R-O-05 orders the whole stack relative to the
signature, and only together do they exclude §5. Worth one sentence in
ARCH-0002 if P5 is accepted.

**§5 step 2's "locating the property holding the signature data" is the
duplicate-key attack surface.** The verifier must find a named property in a
document it has not authenticated, using a parser that — see defect 14 — has
usually already destroyed the evidence of duplicate names. RFC 8949 §10 names
this class directly ("an attacker could make use of invalid input such as
duplicate keys in maps ... to make one application base its decisions on a
different interpretation than the one that will be used by a second
application"), and the RFC 8949 record quotes §10's threat posture as the
reason R-O-05 exists at all. RFC 8785's §5 opens with buffer-overflow advice
and never reaches this.

**R-O-05 forces the signature out of the payload, which dissolves option 3's
rationale.** An embedded signature cannot be verified over received bytes
verbatim: the bytes received include the signature, the bytes signed did not.
The remove-and-re-canonicalize dance in Appendix F is *forced* by embedding.
R-O-05 therefore requires an envelope with the payload carried verbatim — DSSE,
or COSE_Sign1, or a JWS with an opaque payload. And once the payload is an
opaque byte string inside an envelope, **JCS does no work at verification time
at all.**

**So: can JCS be used purely as a producer-side function?** Mechanically, yes,
and Appendix C licenses it. But it costs JCS its stated reason to exist. §1:
"The primary advantage with a canonicalizing scheme is that data can be kept in
its original form. This is the core rationale behind JCS. Put another way,
using canonicalization enables a JSON object to remain a JSON object even after
being signed." Appendix C concedes that the licensed path is the minority one:
"this is just an option since cryptographic schemes based on JCS, in most
cases, would not depend on that externally supplied JSON data already being
canonicalized."

**[analysis] Follow that through and option 3 collapses to something small.**
Under R-O-05, JCS's remaining job is *one* thing: making the same logical value
always produce the same bytes, so a digest of those bytes can serve as an
identifier. That is genuinely valuable and it is the one thing DSSE's
Pre-Authentication Encoding cannot give — the topic answer makes this exactly
the argument for keeping a canonical form at all (R-M-11's `description` mode,
P4's domain hashes). But it is also the job JCS is **worst** at, because
mapping items 1(a), 3, 4 and 5 are all identity-path failures: promoted numbers
are not canonicalized, Unicode is not normalized, set-valued arrays may not be
ordered, and the sort basis is representation-dependent. Option 3 keeps the
half of JCS that is weak and discards the half that is strong.

**What R-O-03 says about citing a spec while departing from its security
procedure.** R-O-03 (`ARCH-0001` §5.3, live): "Canonicalization algorithm for
each concrete encoding SHALL be cited, not invented silently." The proposal
itself separates the two: "R-O-03 governs *which* algorithm; R-O-05 governs
*when it runs*." On that reading, citing §3.2 while declining §5 is within
R-O-03's letter, and this extraction accepts that reading.

**[analysis] But the letter is not the point, and this record is the case that
shows it.** R-O-03 exists so a reader can *check* the algorithm against a
published, implemented specification and get interoperable results. An
unscoped citation of RFC 8785 imports §5 by default, and the import is
**invisible at the dependency boundary**: every implementation in Appendix G is
a canonicalizer built for the Appendix F flow, and a deployment that reaches
for a JCS *signature* library rather than a JCS *canonicalizer* gets §5's
ordering with no warning in any API. A reviewer who knows JCS will assume we
run §5 unless we say otherwise.

> **Proposed amendment to R-O-03**, offered to `ARCH-0001` v0.2.0 as a
> `propose-arch` diff and not made here: *where only part of a cited
> specification is adopted, the citation SHALL name the adopted sections and
> SHALL state which normative provisions of the cited document are not adopted,
> and why.*

That amendment is worth having whichever way DEC-002 goes: the RFC 8949 record
has the same shape of problem in miniature — it adopts §4.2.1, rejects §4.2.3
and §5.4, and the ADR has to say so.

### 3. Unicode normalization against `ARCH-0002` P1

**What the source says.** §3.1, Note: "Although the Unicode standard offers the
possibility of rearranging certain character sequences, referred to as "Unicode
Normalization" [UCNORM], JCS-compliant string processing does not take this
into consideration. That is, all components involved in a scheme depending on
JCS MUST preserve Unicode string data "as is"."

**What it meets.** P1 (accepted, `ADR-0001`): "An extension point is a pair:
**`(defining key, local label)`**." A label is a text string and is therefore
load-bearing for identity. `U+00E9` and `U+0065 U+0301` render identically and
are two different labels, hence two different types, hence — under P4 — two
different domains of discourse.

**It helps, in one precise way, and the help is real.** A normalizing
canonicalizer would be worse than a non-normalizing one. Normalizing merges two
distinct labels into one; not normalizing splits one apparent label into two.
Merging is a silent type collision; splitting is a lookup miss. For a signing
input, refusing to alter the signer's data is the correct default, and RFC 8785
states it where RFC 8949 §3.1 merely omits it. The RFC 8949 record lists that
omission as determinism gap 2 and open question 5; **RFC 8785 closes the
ambiguity without solving the problem**, which is strictly better than leaving
an implementer to guess.

**It hurts, in the breadth of the obligation.** The MUST binds "all components
involved in a scheme depending on JCS" — not the canonicalizer, the *scheme*.
That reaches every UI text field, every filesystem that normalizes names, every
database column with a normalizing collation, every clipboard round trip. JCS
makes all of that our conformance problem and supplies no mechanism and no
detection. See defect 15: as written the rule is unenforceable.

**It shifts the obligation to us, and the compatible shape is narrow.** Two
routes, and §3.1 rules one of them half out:

1. **Normalize at authoring, reject at decode, never normalize at decode.**
   Declaring NFC and applying it *before* canonicalization is compatible with
   §3.1, because JCS has not run yet; rejecting a non-NFC label on decode is
   also compatible, because rejection is not alteration. **Normalizing on
   decode would violate §3.1.** The proposal's own withdrawn YAML appendix
   already names "NFC-normalized strings", so the choice is on the table.
2. **Refuse to normalize and constrain the label grammar** so the question
   cannot arise — a profile in which no two distinct code point sequences
   normalize to the same string. This is the exclusion strategy the topic
   answer found works for CBOR, applied to text.

**[analysis] Route 1 has exactly R-O-05's shape** — do the expensive thing once,
at authoring, on trusted input; afterwards reject rather than repair — and that
is an argument for stating it in ARCH-0002 as a consequence of P5 rather than
as a new rule. It is also the cheaper of the two if P3's multilingual
requirement stands, because route 2's grammar would have to exclude a large
part of Latin, Greek, Cyrillic and Hangul.

**One consequence nobody has written down.** Because §3.2.3 sorts on the code
unit sequence, a normalization difference in a *single* label changes that
label's sort position and therefore the byte sequence of **the entire
document**, not just that field. Under P4's set hash the perturbation is total:
one composed-vs-decomposed accent anywhere in a domain of discourse yields a
different domain identifier. In RFC 8949 the same difference changes the key's
bytes and hence its sort position too — the hazard is not unique to JSON — but
JCS compounds it by adding a UTF-16 conversion step between the stored form and
the compared form (item 5).

### 4. Array element order, and what it does to P4

**What the source says.** §3.2.3: "JSON array data MUST also be scanned for the
presence of JSON objects (if an object is found, then its properties MUST be
sorted), but **array element order MUST NOT be changed**." Appendix A
implements it literally: the array branch carries the comment "Array - Maintain
element order" and iterates with `forEach`.

**Our logical sets carried in arrays.**

| construct | where | why it is a set |
|---|---|---|
| `Threshold.members: [Principal, ...]` | `ARCH-0001` §4.1 | *k*-of-*n* is a predicate over a set; member order carries no meaning, and `n = len(members)` is the only ordering-adjacent invariant |
| a tag's value set | DEC-004 option 1, "byte-string sets + intersection" | sets by name; R-M-08 requires intersection semantics per profile |
| a domain of discourse | `ARCH-0002` P4 | "a **set** of the schemas in P3, serialized in a form that can be reliably and repeatably hashed" |

**Consequence for P4's hash-as-identity: JCS cannot supply it, and this is
sharper than the RFC 8949 case.** RFC 8949 §4.2.1 is **silent** on array order,
so a profile may add a bytewise rule without contradicting the RFC — that is
exactly what the RFC 8949 record's determinism gap 1 proposes. RFC 8785 §3.2.3
says array element order **MUST NOT be changed**. A JCS-conformant
canonicalizer is therefore *forbidden* to order a set-valued array, and any
ordering we impose must run **outside and before** JCS, in a layer of our own,
with its own specification and its own vectors.

**[analysis] That is a second, independent R-O-03 problem, and unlike the §5
problem it cannot be fixed by scoping the citation.** Scoping works when we
adopt a subset of a document. Here we need a *modification*: "RFC 8785 applied
to the output of an unspecified set-ordering pre-pass" is a partly invented
algorithm, which is the thing R-O-03 forbids. A reviewer checking our
canonicalization against RFC 8785 would find it does not match.

**The mitigation, with its costs, because it does exist.** Carry a set as a
JSON **object** — members as property names, values `true` or `null` — and
§3.2.3's recursive property sorting canonicalizes it for free. It works, and
three costs come with it:

1. Property names are text strings only, so a `Principal` member must be
   rendered into a string key. That is RFC 8949 §5.6's warning verbatim — "there
   has to be a specified mapping from the other CBOR types to text strings, and
   this often leads to implementation errors" — reappearing as a wire-format
   requirement rather than an interworking one.
2. The ordering then falls under §3.2.3's UTF-16 rule (item 5) rather than a
   bytewise one, so the mitigation inherits that hazard.
3. **Duplicate members become duplicate property names.** §3.1 forbids them;
   defect 14 shows nothing reliably detects them; a last-wins parser silently
   collapses `[A, B, B]` to two members. The only thing then standing between
   that and a misread threshold is `ARCH-0001` §4.1's invariant `n =
   len(members)`, checked at P5's "expected" level. Under P5 that is a
   rejection, so the failure direction is denial rather than bypass — but it is
   a bypass in any implementation that repairs instead of rejecting, which is
   the default behaviour of ordinary JSON tooling.

**This question is live independent of DEC-002, and it is the same question as
RFC 8949 open question 4.** It is also gated: `DECISIONS-0001` T1-B recommends
**holding** P4, and the topic answer notes that if P4 is dropped and
`Threshold.members` is treated as a sequence, "the identity path then loses
both its hardest case and its text-identity case." So the force of this
objection to option 3 is conditional on a decision not yet taken — which is
worth being honest about, because it is the objection most likely to be
answered by "then do not accept P4."

### 5. UTF-16 sorting as an interoperability hazard

**What the source says.** §3.2.3: "Property name strings to be sorted are
formatted as arrays of UTF-16 [UNICODE] code units. The sorting is based on
pure value comparisons, where code units are treated as unsigned integers,
independent of locale settings." And the Note: "For the purpose of obtaining a
deterministic property order, sorting of data encoded in UTF-8 or UTF-32 would
also work, but the outcome for JSON data like above would differ and thus be
incompatible with this specification. However, in practice, property names are
rarely defined outside of 7-bit ASCII, making it possible to sort string data in
UTF-8 or UTF-32 format without conversion to UTF-16 and still be compatible
with JCS. Whether or not this is a viable option depends on the environment JCS
is used in."

**The divergence is precisely characterizable, and small.** UTF-8 bytewise
order preserves code point order, so UTF-8 and UTF-32 sorting agree with each
other. Both disagree with UTF-16 code unit order on exactly one comparison:
a supplementary-plane character (U+10000–U+10FFFF, encoded as a surrogate pair
beginning 0xD800–0xDBFF) against a BMP character in U+E000–U+FFFF. UTF-16 puts
the supplementary character **first**; code point order puts it **last**.

**The RFC's own test vector is the discriminating fixture.** §3.2.3's test data
contains `"😀"` (U+1F600, Grinning Face) and `"דּ"` (U+FB33,
Hebrew Letter Dalet With Dagesh), and the expected order ends:

```
"Euro Sign"                             U+20AC
"Emoji: Grinning Face"                  U+1F600
"Hebrew Letter Dalet With Dagesh"       U+FB33
```

Under code point order the last two transpose. **[analysis]** That makes
§3.2.3's test data a ready-made negative fixture for a D5-style package,
exactly as RFC 8949's eight-key §4.2.1/§4.2.3 ordering example is — the source
hands us the pair. It is extracted into this record's `examples/`.

**Severity is asymmetric between the two paths, and that is the finding.** On
the **signing** path a sort divergence fails loudly: the verifier computes
different bytes and the signature does not match. Annoying, debuggable, safe.
On the **identity** path it fails silently in the worst available way: two
implementations derive two different hashes for the same logical domain of
discourse and, per P4, "know they are talking about different vocabularies"
when in fact they are talking about the same one with one buggy sort. P4's
stated virtue — "it makes disagreement visible" — becomes a false positive
generator. This is the topic answer's point that a collision or divergence on
the identity path "is not a verification failure but two distinct principals
sharing one name, or two distinct vocabularies sharing one identifier", read in
the other direction.

**Implementation correctness: the RFC invites the bug.** The Note's "in
practice, property names are rarely defined outside of 7-bit ASCII" is an
explicit licence to skip the conversion. For a generic JSON tool that is
reasonable advice. For us it is false by requirement — P3 makes multilingual
descriptions mandatory and P1 makes labels user-chosen text in a key's own
namespace, which is precisely where an emoji or a supplementary-plane CJK
character will eventually land. **Our model violates RFC 8785's own stated
operating assumption by design.**

**The portability trap, stated carefully.** Appendix A sorts with ECMAScript's
`Object.keys(object).sort()`, which compares strings by UTF-16 code unit and is
therefore correct *in ECMAScript*. The same two lines ported to a language
whose default string order is code point or UTF-8 byte order are **wrong and
pass every ASCII test**. That is why Appendix G lists a separate verified
implementation per language rather than saying "sort your strings"; this
extraction does not assert that any listed implementation is defective, only
that the naive port is, and that the defect is undetectable without a
supplementary-plane fixture.

**One further trap the document does not signpost.** §3.2.3 requires "The
sorting process is applied to property name strings in their "raw" (unescaped)
form. That is, a newline character is treated as U+000A." So a conformant
implementation sorts the *pre-escape* form and emits the *post-escape* form —
two different strings in one function. Sorting the emitted form puts `\u000f`
under `\` (U+005C) instead of under U+000F. The §3.2.3 test data includes
`"\r"` specifically to catch this, and the expected order ("Carriage Return"
first) proves the raw form governs — but nowhere does the text say what goes
wrong if you get it backwards.

**Contrast with option 5, which wins this cleanly.** RFC 8949 §4.2.1 sorts map
keys bytewise on their **encoded** form. For a text key the encoded form is
UTF-8, there is no surrogate concept, there is no conversion step, and the
sorted form is the emitted form. The CBOR rule is architecturally simpler for a
structural reason — *sort the bytes you emit* — not an incidental one.

### 6. Namespace governance, R-M-12, and where option 3 genuinely wins

**This is the criterion `ARCH-0001-PROPOSAL-v0.2.0` §3.3 says was never scored**
— "all four original options were scored on fidelity, tooling, and ergonomics,
and none was scored on namespace governance" — and on it, **option 3 wins
outright.** It should be recorded that way even though the rest of this record
recommends against option 3.

**What the source says.** §1, listing why JCS should not repeat XML
canonicalization's failures: "JSON does not have a namespace concept and
default values." §4: "This document has no IANA actions."

**Against the registry critique that produced P1.** `ADR-0001`'s evidence is
"IANA allocation policies for CBOR tags (RFC 8949 §9.2) and COSE header
parameters (RFC 9052 §11.1)". **Option 3 has no counterpart to any of it.**
There is no tag space, no simple value space, no header parameter space, no
IANA action at all. Where option 5 must *construct* its registry-freedom by
subtraction — the RFC 8949 record shows this costs a positive rule that "major
type 6 MUST NOT appear", decoder rejection of it, a named untagged export
profile, and a §4.2.2 argument about why tag presence cannot be left to
convention — option 3 is registry-free **by construction**.

**P1's displacement is a no-op in JSON, and that is the strongest thing option 3
has.** The RFC 8949 record's §5 states P1's cost precisely: in CBOR, type
identity "has to be structure *inside* the data model ... and therefore it is
carried as data. That is the precise sense of P1's displacement: it does not
choose different numbers, it moves type identity from the encoding layer down
into the data layer." **In JSON there is no encoding layer to move it out of.**
`(defining key, local label)` is an ordinary two-member object or two-element
array; the label is a native JSON string; nothing is displaced because nothing
was ever in the encoding. For a project whose central novel claim is key-relative
type naming, that is a genuine architectural fit and this record should not
bury it.

**The byte cost, honestly.** The RFC 8949 record flags that `(KeyId, label)`
costs a 32-byte digest plus a label plus two heads against a tag's 1–3 bytes,
"a regression of one to two orders of magnitude per type reference" against
RFC 8949 §1.1 objective 2 (class-1 constrained nodes). **Option 3 does not have
that regression**, because JSON never offered the 1–3 byte alternative. It has
a worse *absolute* baseline — JSON text plus hex or base64 for every digest and
key is roughly twice the bytes of CBOR for the same content — but no regression
against its own baseline. **[analysis]** Neither cost should carry weight here:
RFC 8949 §1.1 objective 2 is the CBOR working group's goal, not ours, nothing
in `ARCH-0001` or `PLAN-0003` requires constrained-node operation, and D-1's two
targets are a software supply chain and an archive. The byte argument is the
weakest available reason to prefer either option and should be dropped from the
D5 comparison's conclusions, if not from its measurements.

**The counterweight, which is item 8.** Option 3's registry-freedom holds at the
encoding layer and is handed straight back at the envelope layer, because
DEC-002 option 3 names DSSE in its own text and DSSE's `payloadType` is a global
string. The win is real; it is also, as option 3 is currently written, given
away.

### 7. Standing under R-O-03, against RFC 8949's STD 94

**What the source says.** §2: "Note that this document is not on the IETF
standards track. However, a conformant implementation is supposed to adhere to
the specified behavior for security and interoperability reasons. This text
uses BCP 14 to describe that necessary behavior." Status of This Memo: "This is
a contribution to the RFC Series, independently of any other RFC stream. The
RFC Editor has chosen to publish this document at its discretion and makes no
statement about its value for implementation or deployment. Documents approved
for publication by the RFC Editor are not candidates for any level of Internet
Standard."

**Be fair first: the stream label alone is not disqualifying under R-O-03.**
R-O-03's bar is "cited, not invented silently". RFC 8785 is archival, has a
DOI, has a frozen text, has five independently verified implementations
(Appendix G) and extensive public test data (Appendix I). "Informational" on
the Independent stream is a statement about *process and consensus*, not about
quality, and RFC 8785 is more precise about its own canonicalization than many
standards-track documents are about theirs. A record that rejected option 3 on
the stream label would be rejecting it for the wrong reason.

**Three consequences of the standing that do bear on us.**

**(a) No working group, so the defects below have no owner.** An Independent
Submission has no WG to maintain it and no errata process backed by one. The
defects in the next section — the RECOMMENDED/MUST mismatch between §3.1 and
Appendix D, and §5's I-JSON check that Appendix A is structurally incapable of
performing — have nowhere to go. The equivalent questions about RFC 8949 land
on the CBOR WG, which is *actively* producing CDE and dCBOR precisely because
§4.2 left so much open (the topic answer: "Four mutually incompatible profiles
grew in that gap, which is why the CBOR WG is now writing CDE and dCBOR at
all"). A live WG producing successor profiles is evidence of an unresolved
problem *and* of a mechanism for resolving it. RFC 8785 has the first property
without the second.

**(b) The normative conformance evidence is hosted outside the RFC series, at a
mutable URL.** Appendix B: "For a more exhaustive validation of a JCS number
serializer, you may test against a file (currently) available in the
development portal (see Appendix I) containing a large set of sample values."
Appendix I names `github.com/cyberphone/ietf-json-canon` and
`github.com/cyberphone/json-canonicalization` — personal repositories. The RFC
hedges with "(currently)". **[analysis]** For a project that identifies
documents by content digest and runs a library on that principle, citing a
specification whose conformance suite lives at a third-party mutable URL is a
provenance problem of exactly the kind the library exists to prevent. If option
3 were selected, that test corpus would have to be ingested and digested as a
record of its own.

**(c) The decisive point, and it is not about standing at all: the normative
algorithm is not in the document.** §3.2.2.3: "ECMAScript builds on the IEEE 754
[IEEE754] double-precision standard for representing JSON number data. Such
data MUST be serialized according to Section 7.1.12.1 of [ECMA-262], including
the "Note 2" enhancement. **Due to the relative complexity of this part, the
algorithm itself is not included in this document.** For implementers of
JCS-compliant number serialization, Google's implementation in V8 [V8] may
serve as a reference. Another compatible number serialization reference
implementation is Ryu [RYU]."

**[analysis] This is the strongest R-O-03 argument in the record, and it is
independent of the Independent stream.** R-O-03 says *cited, not invented
silently*; the point of citing is that someone can check it. RFC 8785's number
rule cannot be checked from RFC 8785. Checking it means reading ECMA-262 10th
edition §7.1.12.1 including a note, or — as the RFC suggests — reading V8 or
Ryu, which are implementations, not specifications. Citing RFC 8785 is citing
*three* artifacts, one of them an edition of an annually revised standard and
two of them codebases. Citing RFC 8949 §4.2.1 is citing one document, STD 94,
complete in itself. **That comparison, not the stream label, is the R-O-03
reason to prefer RFC 8949.**

The mitigation is real and should be recorded: §3.2.2.3 pins a specific edition
(ECMA-262 10th, June 2019), so the dependency is at least frozen. §3.2.2 then
un-freezes it: "In the (unlikely) event that a future version of ECMAScript
would invalidate any of the following serialization methods, it will be up to
the developer community to either stick to this specification or create a new
specification."

**And one soft spot in the conformance language itself.** "A conformant
implementation is **supposed to** adhere to the specified behavior" (§2) is not
a conformance statement. The document defines no conformance clause, so
Appendix G's "verified to be compatible with JCS" has no stated criterion
behind it.

### 8. No authenticated type indicator, and what option 3 must pair with

**JCS supplies none.** §4: "This document has no IANA actions." The output of
§3.2.4 is bare UTF-8 JSON; nothing in it says which schema, which profile, or
which encoding produced it. R-O-05 requires that the signed payload be "carried
with an authenticated type indicator." JCS cannot provide one; only an envelope
can. DEC-002 option 3 knows this and names its envelope in its own text: "JSON
+ RFC 8785 JCS as canonical; **DSSE for signed form**."

**So option 3 is structurally a two-document choice**, and the second document
is where P1 bites. DSSE's `payloadType` is a **global string**, conventionally a
URI or a media type (`application/vnd.in-toto+json` and the like), with media
types themselves an IANA registry. `ADR-0001` (accepted): "Native extension
points — type identifiers, predicate types, tags, header parameters — are
identified relative to a defining principal, as a `(key, local label)` pair. The
native model depends on no centrally allocated registry for their meaning."
A `payloadType` is a header parameter in everything but name.

**[analysis] State the irony plainly, because it is the cleanest summary of
option 3's position.** Option 3's single best property — no registry anywhere in
the encoding, mapping item 6 — is handed back by the envelope option 3 names in
its own definition. JCS is registry-free; `payloadType` is not; and R-O-05 is
what forces the type indicator into the envelope rather than leaving it in the
payload. Option 3 as DEC-002 currently words it is P1-non-conformant at exactly
the point where P1 bites hardest.

**Two escapes, both costed.**

1. **Serialize the key-relative pair into the `payloadType` string** — e.g.
   `<keyid>/build-provenance`. DSSE treats `payloadType` as an opaque string in
   PAE, so this is mechanically fine, and it is the same move option 5 makes
   (carry the pair as data). The cost is a new micro-format: a separator, a key
   encoding, a case convention — all invented, all un-citable under R-O-03, and
   all subject to mapping item 1(d)'s problem that two spellings of one pair are
   two identities.
2. **Put the indicator inside the payload**, where it is authenticated because
   the payload is signed. Fine under PAE — but `payloadType` must still be set
   to *something*, and a DSSE verifier will compare it. Two type indicators, one
   authoritative and one decorative, is a confusion surface of the kind
   `ARCH-0002` P5 exists to close.

**This failure mode is already live in our own code.** The topic answer records
that in the rcbor spike "the envelope type indicator is a global string naming
the rcbor statement profile, which is R-M-12-non-conformant, and is the one
place the spike does not practise what it preaches." Option 3 would
institutionalise the one thing we have already caught ourselves doing wrong.

**A limit on this item.** DSSE's own record is queued, not extracted (topic
answer: "DSSE is queued and is type repo so it needs a summary rather than an
extraction"), so the PAE framing and the exact `payloadType` semantics are
reported here from `ARCH-0001-PROPOSAL-v0.2.0` §3.4 and from the topic answer,
not from a primary source this record holds. Open question 8.

### 9. D-3, addressed explicitly

`docs/extraction.md` requires design notes for signing-envelope documents to
address D-3 (option 5: reduced CBOR, no IANA tags, COSE export only). RFC 8785
is the canonicalization half of option 3, D-3's rejected alternative, so the
address is a comparison rather than a mapping.

| condition (topic `canonical-encoding`) | RFC 8785 / option 3 | D-3 / option 5 |
|---|---|---|
| (1) injective over encoded values | **fails** at promoted numbers (Appendix D/E) and at untyped byte encodings; holds for maps | holds once the fourteen §4.2 rows are pinned; the spike reaches it by exclusion |
| (2) decoder rejects non-canonical input | **not addressed**; JCS is a serializer-side filter, and §5 re-canonicalizes instead of rejecting | open, routed through P5; the topic answer recommends extending P5 by a clause |
| (3) canonicalize once at authoring | **contradicted** by §5 and Appendix F; licensed only as Appendix C's "just an option" | R-O-05, implemented in the spike (`verify()` never calls `encode()`) |
| (4) authenticated type indicator | **none**; must come from DSSE, whose `payloadType` is global | none natively either; COSE supplies one but via registry, hence option 5's own open question |
| (5) canonical order for set-valued arrays | **prohibited** by §3.2.3 | **absent** from RFC 8949 §4.2.1, so addable by profile |
| (6) normalization rule for identity-bearing text | **refused** by §3.1, explicitly, with the obligation pushed to every component | **silent** in RFC 8949 |

**[analysis] The decisive row is (5), and the decisive word is the difference
between *prohibited* and *absent*.** Both encodings lack a canonical order for
set-valued arrays. RFC 8949 leaves a gap a profile may fill without
contradicting the RFC; RFC 8785 states a MUST NOT that a profile cannot fill
without ceasing to be JCS. On conditions (5) and (6) — the two the topic answer
says this topic exists for — option 3 is not merely equal to option 5, it is
structurally worse, and worse in a way R-O-03 can see.

The one row where option 3 is better is **(1) for maps**: JSON's single number
type removes four of the RFC 8949 record's fourteen determinism rows
(float presence, float shortening, integer-vs-float, NaN) and §3.2.2.3's
NaN/Infinity prohibition removes another. That is a genuine simplification and
it is the same simplification the spike buys by excluding floats — obtained
from the substrate instead of from a profile.

**Does anything here reopen D-3?** No. Nothing in RFC 8785 undermines option 5;
two things in it *support* option 5 by showing what a well-specified
alternative still cannot do.

---

## Open questions

Items this document cannot settle, with who must. Items marked **[beyond
source]** are ones where this extraction reasoned past both RFC 8785 and our
own documents.

1. **Does DEC-002 option 3 stay on the table?** This record recommends
   **withdrawing** it rather than out-scoring it, on four grounds in descending
   force: §3.2.3 *prohibits* the set ordering P4 needs, so the algorithm we
   require is a modification of JCS rather than a subset (mapping 4); §5 and
   Appendix F mandate the ordering R-O-05 forbids, and used as R-O-05 requires,
   JCS reduces to an authoring-side normalizer whose only remaining job is the
   one it is worst at (mapping 2); the number serialization algorithm is not
   contained in the cited document (mapping 7); and option 3's own named
   envelope reintroduces a global type identifier (mapping 8). Recorded against
   it: option 3 **wins** namespace governance outright, the criterion the
   proposal says was never scored (mapping 6), and it removes five of the RFC
   8949 record's determinism rows. *DEC-002 ADR — Paul.*
2. **Does R-O-03 require a *scoped* citation?** Proposed amendment in mapping
   item 2: a partial adoption must name the adopted sections and state which
   normative provisions are not adopted. Needed whichever way DEC-002 goes —
   the RFC 8949 record has the same shape of problem with §4.2.3 and §5.4.
   *`propose-arch` diff against `ARCH-0001` §5.3; not made from the library.*
3. **The Unicode normalization rule for P1 labels.** Same question as the RFC
   8949 record's open question 5; this record adds three things to it: JCS
   *forbids* normalizing at canonicalization time, so only "normalize at
   authoring, reject at decode" is compatible with a JCS citation; the
   obligation JCS writes ("all components involved in a scheme") is
   unenforceable as drafted; and a single normalization difference perturbs the
   whole document's sort order, hence the whole P4 set hash, not just one field.
   P1 is accepted, so a change means a superseding ADR. *Paul.*
4. **A canonical order for set-valued arrays.** Same question as RFC 8949 open
   question 4. This record contributes that the question is *harder* under
   option 3, because §3.2.3 forbids the answer, and that the object-as-set
   mitigation trades it for a duplicate-property problem (mapping 4). *David,
   D4/D5, then the ADR.*
5. **Is `Threshold.members` a set or a sequence?** Gates question 4 entirely. If
   it is a sequence and P4 is not accepted, the identity path loses its hardest
   case and much of this record's objection to option 3 weakens.
   `DECISIONS-0001` T1-B currently recommends **holding** P4, so this is live.
   *Paul.*
6. **How is a `Validity` instant represented?** `ARCH-0001` §4.1 does not say,
   and under option 3 the choice is encoding-visible: a numeric epoch has a
   hard ceiling between microsecond and nanosecond resolution (mapping 1), while
   an RFC 3339 string walks into Appendix E's documented signature-breaking
   round trip. This extraction recommends integer seconds or milliseconds. The
   same question exists under option 5 but without the Appendix E hazard, since
   RFC 8949 §3.4.2's epoch form is excluded and a plain integer carries it.
   *David, D4.*
7. **The canonical lexical form for byte-valued fields rendered as text** — hex
   case, base64 versus base64url, padding. **[beyond source]** Needed even if
   option 3 dies, because R-I-03's in-toto/DSSE export path is JSON and the
   exported digests and keys must have one spelling. *David, D7.*
8. **Does DSSE's `payloadType` satisfy or violate R-O-05's "authenticated type
   indicator" under P1?** Cannot be settled from this record; the DSSE record is
   queued, not extracted. Bears on DEC-005 as much as DEC-002. *library, then
   DEC-005.*
9. **Does R-O-05's type indicator need to live inside the payload as well as in
   the envelope?** Same as RFC 8949 open question 10, reached by a different
   route: there, because the payload is an opaque `bstr`; here, because the
   envelope's own indicator is registry-governed. *`ARCH-0001` §4.2 and DEC-003.*
10. **[beyond source] Is JCS retained as an interchange-only canonicalization?**
    Withdrawing option 3 as the *native* encoding does not withdraw RFC 8785 as
    the rule for producing the JSON we **export** under R-I-03 and D7. If
    in-toto Statement and DSSE export are in scope, something must canonicalize
    that JSON, and RFC 8785 is the only cited candidate — so this record is
    needed for `ARCH-0001` §6's loss table under R-I-01 whether or not option 3
    survives. That reframing is the most useful thing this record can offer a
    reader who has already decided against option 3. *`ARCH-0001` §6, D7.*
11. **Must our JSON import path detect duplicate property names?** §5 step 1
    requires it, defect 14 shows Appendix A cannot do it, and P5 requires
    rejection rather than last-wins collapse. Most JSON parsers in most
    languages collapse silently. If D7 imports in-toto or DSSE objects, a
    duplicate-detecting parser is a requirement, not a preference. *David, D7.*
12. **Does the §3.1 / Appendix D normative mismatch (defect 13) govern as
    RECOMMENDED or as MUST?** Affects `requirements.yaml`'s keyword
    reconciliation for this record — the same obligation must be extracted twice
    with two different verbs — and would affect any conformance claim we made.
    There is no working group to ask. *Recorded; no action.*

### Defects and ambiguities in RFC 8785 itself

Places where the source does not decide something it appears to decide, or
mandates something its own machinery cannot perform. Recorded rather than
papered over. These are not objections to our design.

13. **§3.1 and Appendix D state the same obligation at two different BCP 14
    strengths.** §3.1: "it is **RECOMMENDED** to represent such numbers as JSON
    strings; see Appendix D for details". Appendix D: "numbers that do not have
    a natural place in the current JSON ecosystem **MUST** be wrapped using the
    JSON string type." The two are cross-referenced to each other, so this is
    not two topics that happen to overlap. An implementer cannot tell whether
    emitting a number outside the double range is a conformance failure or a
    style preference. *Affects this record's keyword reconciliation; see open
    question 12.*

14. **§5 mandates an I-JSON check that Appendix A's reference canonicalizer is
    structurally incapable of performing.** §5 step 1: "Parse the JSON data and
    verify that it adheres to I-JSON." I-JSON conformance includes §3.1's "JSON
    objects MUST NOT exhibit duplicate property names." Appendix A's
    canonicalizer takes an **already-parsed** object — `var canonicalize =
    function(object)` — by which point `JSON.parse` has silently collapsed any
    duplicate name and destroyed the evidence. The code's banner comment names
    error handling and "UTF-8 generation" as the only omissions and does not
    flag this one. The duplicate-name rule is therefore an
    obligation on the *data* with no detection point anywhere in the specified
    pipeline. This is the most consequential defect in the document for us,
    because it is also what makes the object-as-set mitigation in mapping item 4
    unsafe.

15. **§3.1's Unicode MUST binds parties outside the implementation and is
    unenforceable as written.** "All components involved in a scheme depending
    on JCS MUST preserve Unicode string data "as is"." A specification cannot
    impose a MUST on a text editor, a filesystem, or a database the
    implementation does not control, and nothing in the pipeline can detect a
    violation — a normalized label is perfectly well-formed JSON. The rule is
    the right one; it has to be restated as a *rejection* rule inside our own
    profile to have any force.

16. **JCS's number serialization is not injective over IEEE 754, independently
    of precision.** Appendix B, rows 1 and 2: `0000000000000000` → `0` (Zero)
    and `8000000000000000` → `0` (Minus zero). Two distinct doubles, one
    canonical token. The table records it without comment. RFC 8949 §4.2.2
    raises negative zero as something the protocol must rule on; RFC 8785
    silently collapses it. Harmless for every field in `ARCH-0001` §4.1 today;
    fatal for any future value where ±0 must be distinguished, and an exception
    to the general claim that a canonical form is injective over the values it
    encodes. *(The same table's NaN and Infinity rows carry an empty JSON
    Representation cell with note (3) — a presentational way of saying no
    representation exists, which leaves the table formally incomplete but
    misleads no one.)*

17. **The raw-versus-escaped sorting trap is demonstrated but never stated.**
    §3.2.3 requires sorting "property name strings in their "raw" (unescaped)
    form", then emits the escaped form. An implementation that sorts what it
    emits orders `\u000f` under U+005C rather than U+000F. §3.2.3's test data
    includes `"\r"` precisely to catch this and the expected order proves the
    raw form governs — but the document never says what goes wrong, so the
    vector only helps an implementer who already ran it.

18. **The normative number algorithm is outside the document and its
    conformance corpus is at a mutable third-party URL.** §3.2.2.3: "Due to the
    relative complexity of this part, the algorithm itself is not included in
    this document," with V8 and Ryu — implementations — offered as references.
    Appendix B: the exhaustive validation file is "(currently) available in the
    development portal", which Appendix I gives as two personal GitHub
    repositories. Discussed under mapping item 7 as the decisive R-O-03 point.

19. **The document disclaims its own normative future and names no successor
    process.** §3.2.2: "In the (unlikely) event that a future version of
    ECMAScript would invalidate any of the following serialization methods, it
    will be up to the developer community to either stick to this specification
    or create a new specification." Combined with §2's "a conformant
    implementation is **supposed to** adhere to the specified behavior" — which
    is not a conformance statement, and against which Appendix G's "verified to
    be compatible" claims have no stated criterion — and with the Independent
    stream's absence of a maintaining working group, defects 13 and 14 have
    nowhere to be resolved.

20. **Appendix H concedes the trade without quantifying it.** "The listed
    efforts all build on text-level JSON-to-JSON transformations. The primary
    feature of text-level canonicalization is that it can be made neutral to the
    flavor of JSON used. However, such schemes also imply major changes to the
    JSON parsing process, which is a likely hurdle for adoption. Albeit at the
    expense of **certain JSON and application constraints**, JCS was designed to
    be compatible with existing JSON tools." Those unnamed "certain JSON and
    application constraints" are mapping items 1, 3, 4 and 5 of this document.
    Not a defect so much as the document's own one-sentence admission that it
    chose tool compatibility over completeness — which is the right summary of
    why option 3 fails the identity path while remaining a perfectly good
    signing input.
