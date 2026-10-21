---
record: rfc-9054
kind: design-notes
title: "rfc-9054 — bearing on our design"
extracted: "2026-10-20"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§2.1`, `§4.1`) are RFC 9054's. Our own documents are cited by id
(`ARCH-0001`, `DEC-002`, `MD-3`, `R-O-03`). Three markers distinguish voices,
following `records/ietf/rfc-9741/distilled/design-notes.md` and `rfc-8392`'s:

- unmarked prose reports **RFC 9054** or **our decisions**, as cited;
- **[analysis]** marks reasoning of this extraction that neither the source nor
  our documents state;
- **[correction]** marks a working assumption, or a claim in one of our own
  artifacts, that the source does not support.

**Which quotations below are checkable here, and which are not.** This library
is **standalone by design** (`CLAUDE.md`). The `mofn` documents this file cites
are **not present in this repository**: `ARCH-0001` (including §4.1 and §7),
`ARCH-0001-PROPOSAL-v0.2.0`, `ARCH-0002` (P1–P5), `ADR-0001`, `MD-3`,
`DECISIONS-0001`, and the `R-M-*` / `R-O-*` rules. **Every quotation of those
documents here is reproduced from the extracting agent's context and cannot be
verified from this repository.** Treat each as a citation to be re-checked
against `mofn` before it is relied on. `rfc-9741` set that convention and
`rfc-9964` followed it; this file follows it rather than inventing a third.

What *is* checkable here, and was: `docs/extraction.md`'s statement of MD-3
(*"option 5: reduced CBOR, no IANA tags, COSE as export only"*),
`topics/canonical-encoding.yaml`'s six conditions and its identification of
`DEC-002` options 1 and 3, RFC 8610's grammar at
`records/ietf/rfc-8610/distilled/schema/cddl.abnf` and its 44 enumerated
grammar gaps beside it, and the artifacts of `records/ietf/rfc-9360`,
`rfc-9679` and `rfc-9964`. Each is in this worktree.

**How quotations of the source are produced.** Every one was cut from
`.cache/rfc-9054.txt` by line range **by script**, narrowed to a contiguous
character span where a sentence is quoted out of a flowed paragraph, and
verified mechanically as a substring of the whitespace-normalised source before
this file was written. **Nothing is spliced and no hyphenation is healed.** The
lane-wide quote audit covering this file, `rfc-9360`'s design notes and both
READMEs was run as one pass rather than per record.

**Decision status, stated plainly.** `DEC-002` in `ARCH-0001` §7 lists **four**
options. "Option 5" exists only as *proposed* text in
`ARCH-0001-PROPOSAL-v0.2.0` §3.3, unmerged. `MD-3` (2026-09-28) *narrows*
`DEC-002` to option 5. **No `DEC-002` ADR has been written.** Within this
library option 1 is canonical S-expressions (`records/ietf/rfc-9804`,
`rfc-2693`) and option 3 is JCS over JSON (`records/ietf/rfc-8785`), both per
`topics/canonical-encoding.yaml`.

**What this extraction added beyond the summary, mechanically.** A CDDL parser
for RFC 8610 Appendix B's grammar, run against both §2.1 fragments — which
**refutes** the summary's account of what is wrong with the first one and
confirms the more serious thing that is wrong with it; a measurement that
contradicts §4.1's own size rationale for five of eight allocations; and three
computed vectors that make the SHA-256/64 ambiguity, the SHA-512/256 confusion
and §2.1's injectivity rule testable rather than described.

---
## 1. What this record decides, in one paragraph

**It registers the identifiers and refuses the carrier, so `R-O-03` can be
half-satisfied by citation and no more.** §1:> It also does not define a structure syntax that is used to encode a digested object structure along the lines of the DigestedData ASN.1 structure in [CMS]. This omission was intentional, as a structure consisting of just a digest identifier, the content, and a digest value does not, by itself, provide any strong security service.
Citing `-16` for SHA-256 discharges the **algorithm** half of
*"the canonicalization algorithm SHALL be cited, not invented silently"*. The
four-field structure around it — algorithm, value, pointer to what was hashed,
additional data (§2.1) — **is ours to invent, with no COSE citation
available**, and the document says that is deliberate. That is the decision a
reviewer should take from this record. The second thing to take is small and
real: §2.1 does supply one citable injectivity rule, in a parenthetical (§6).

---
## 2. `R-M-07` and `R-O-03` — the algorithm is citable, the structure is not

`R-M-07` requires an artifact statement to bind a content digest; `R-O-03`
requires the algorithm to be cited rather than invented silently. **[Both
unverifiable from this repository — `mofn` rules.]**

**What is citable.** Eight identifiers, in a registry, with a stable reference:
SHA-1 (−14), SHA-256/64 (−15), SHA-256 (−16), SHA-512/256 (−17), SHAKE128
(−18), SHA-384 (−43), SHA-512 (−44), SHAKE256 (−45). `schema/hash-algorithms.derived.yaml`
carries them as rows with each one's CBOR encoding computed, and
`examples/vectors.yaml` V-0002 computes all eight digests over one input so the
set is checkable against FIPS 180-4, FIPS 202 and RFC 3174.

**What is not citable, in the document's own words.** §2.1 restates §1:> [COSE] did not provide a default structure for holding a hash value both because no separate hash algorithms were defined and because the way the structure is set up is frequently application specific.
So `R-M-07`'s content digest has an identifier and **no structure to travel
in**. The two structures §2.1 prints are introduced as examples — > An example of a structure that permits all of the above fields to exist would look like the following:
and > Below is an alternative structure that could be used in situations where one is searching a group of objects for a matching hash value. In this case, the location would not be needed, and adding extra data to the hash would be counterproductive. This results in a structure that looks like this:
— and neither is normative, neither is registered, and §3 below shows that
one of them does not work.

[analysis] **The asymmetry is the finding.** `R-O-03` exists to stop us
inventing an algorithm silently. Here the algorithm is the *easy* half: it is
registered, numbered and referenced. The hard half is the envelope, and the
rule has nothing to say about inventing *that* — so a record that satisfies
`R-O-03` by citing `-16` can still contain a wholly invented four-field
structure with no citation and no flag. **That is a gap in `R-O-03`'s wording,
not in this document**, and it is worth reporting upward: the rule should cover
the carrier as well as the algorithm, or say explicitly that it does not.

---
## 3. §2.1's two structures, judged mechanically — and the summary's account of the first one is wrong

The record's `summary.md` says of `COSE_Hash_V` that *"the fragment does not
parse"*. **[correction] It parses.** What it does not do is mean what it looks
like, and the real defect is worse than the one claimed.

A recursive-descent parser for RFC 8610 Appendix B's grammar was written for
this pass, transcribed production for production from
`records/ietf/rfc-8610/distilled/schema/cddl-dedented.derived.abnf` (this
library's mechanical dedent of RFC 8610 Figure 13, with the verbatim bytes in
`cddl.abnf` beside it). It was gated first on RFC 8610's own 40-rule prelude,
on `rfc-9360` §2's two rules, and on three deliberate negatives. Full output:
`schema/cddl-parse.derived.txt`.

### 3.1 Erratum 7335 is real, and `#` does not stop the parse

Erratum **7335** (*Reported*, Technical, §2.1, Carsten Bormann, 2023-02-06,
checked at `https://errata.rfc-editor.org/search/?rfc_number=9054` on
2026-10-20): the comment marker in `COSE_Hash_V` is `#`, where CDDL's is `;`.
RFC 8610 Appendix B gives `COMMENT = ";" *PCHAR CRLF`, and `#` is the **tag
operator** (`type2 = … / "#" DIGIT ["." uint] / "#"`).

**Measured consequence: the fragment parses as a whole, and the grammar sees 24
group entries where four were written.** Each `#` is read as the "any" type and
each comment word after it as a bare type reference — four member entries, four
`#`, sixteen name references, **15 of them distinct**: `Algorithm`,
`identifier`, `Hash`, `value`, `Location`, `of`, `object`, `that`, `was`,
`hashed`, `containing`, `other`, `details`, `and`, `things`. None begins with
`$`, so RFC 8610 §3.9's socket convention does not silence them (this library's
`grammar-gaps.derived.txt`, items G-23 and G-40) and a name-resolving tool
rejects the file **at name resolution, not at syntax**. With the erratum applied
the undefined count is zero.

So: the defect is real, the summary's conclusion ("unusable as printed") is
right, and **its stated mechanism is wrong**. Worth correcting rather than
leaving, because "does not parse" invites the wrong repair — a syntax fix —
when the real repair is two fixes, and the second one no erratum covers.

### 3.2 The defect no erratum covers: it is a group, not a type

**Even with erratum 7335 applied, `COSE_Hash_V` cannot be the root of a CDDL
model.** Forced as a type rule it fails after 14 characters — immediately after
`COSE_Hash_V = ` — because `type2`'s parenthesised alternative is
`"(" S type S ")"` and a `type` cannot contain member keys. Forced as a group
rule it succeeds. `COSE_Hash_Find`, by contrast, parses as a **type** rule,
because `"[" S group S "]"` *is* a `type2`.

That difference is decisive. RFC 8610 §2.2.4, as this library's
`grammar-gaps.derived.txt` quotes it at item G-04: *"there is no way to use a
group as a root -- it must be a type."* So something must wrap `COSE_Hash_V`;
its member keys mean that something is a **map** (G-03: *"If the memberkey is
not given, the entry can only be used for matching arrays, not for maps"* — and
these keys *are* given); and **RFC 9054 never supplies the wrapper.**
`schema/cose-hash.derived.cddl` supplies it, marked as ours, with the
round-trip to the verbatim bytes asserted by the generator.

And the grammar cannot catch the misuse either: `X = COSE_Hash_V` parses, because
RFC 8610 Appendix C concedes that `a = b` makes `a` a type or a group depending
on `b` (G-01). **So of the two structures the document offers, one is a working
type and the other needs an erratum, a wrapper the document never mentions, and
a side condition no CDDL tool enforces.**

### 3.3 `COSE_Hash_Find` parses, and it is already `rfc-9360`'s type

`COSE_Hash_Find = [ hashAlg : int / tstr, hashValue : bstr ]` against
`rfc-9360` §2's `COSE_CertHash = [ hashAlg: (int / tstr), hashValue: bstr ]`.
Same member key names, same types, same order; the only difference is a pair of
parentheses around a single `/` expression, which changes nothing.
`examples/vectors.yaml` V-0006 encodes the same *(algorithm, digest)* pair under
both for all eight algorithms: **byte-identical every time.**

Same working group, same author, two documents six months apart, and **neither
cites the other's structure.** RFC 9360 cites RFC 9054 zero times; RFC 9054
cites RFC 9360 only as `draft-ietf-cose-x509-08`, and only for the certificate
*scenarios*, never for the type. [analysis] That is as close to a settled COSE
digest shape as the registry gets, and it is settled by **coincidence**. For us
it is a small practical gift: one codec serves both, and one restriction on
`hashAlg` restricts both.

---
## 4. "Filter Only" — defined twice, in different words, and carried nowhere

The document's one structural contribution to COSE is a new value in a registry
column. **It is defined twice and the two definitions are not the same
constraint.**

§2:> "Filter Only" indicates that the only purpose of a hash function should be to filter results; it is not intended for applications that require a cryptographically strong algorithm.
§4.1:> This value is only to be used for hash functions and indicates that it is not to be used for purposes that require collision resistance.
The first is about **strength** and its force word is the lower-case
"should". The second is about **one specific property**. Neither is a BCP 14
statement, and this is an Informational document with two keywords in it. **The
second is the one the conflict with `rfc-9360` turns on**, and a reader who
takes the §2 wording as the definition will not see the conflict at all.

**And it is unenforceable by construction, which is the part that costs us.**
A registry column is not a wire field. `COSE_Hash_Find` and `rfc-9360`'s
`COSE_CertHash` both have **exactly two fields**, so a verifier handed
`[-14, h'…']` cannot tell whether the sender was filtering or binding —
`records/ietf/rfc-9360/distilled/examples/vectors.yaml` V-0004 shows the two
uses are the same 25 octets. The fitness judgement lives in a registry a
verifier is not required to consult, in a document with no `MUST`.

### 4.1 The cross-record result: §3.2 registers a 64-bit truncation **because of** `rfc-9360`, and `rfc-9360` makes it a binding

This is the finding neither record reaches alone, and it is a chain of three
sentences in two documents.

**One.** §3.2 justifies SHA-256/64's registration by pointing at `rfc-9360`'s
draft:> The latter is the case for some of the scenarios identified in [COSE-x509], specifically, for the cases when the hash value is used to select among possible certificates: if there are multiple choices remaining, then each choice can be tested by using the public key.
`[COSE-x509]` is `draft-ietf-cose-x509-08`, 14 December 2020 — the document
that became RFC 9360. **The safety argument is that a false positive is caught
downstream by testing the public key.**

**Two.** §2 of the same document states that precondition in general terms, and
it is the sentence that makes filtering safe at all:> In this case, one still needs to confirm that the public key validates the signature (and that the certificate is trusted), and all certificates that don't contain a key that validates the signature can be discarded as false positives.
**Three.** `rfc-9360` §2's recommended configuration does not have that
downstream test. It puts `x5t` in the **protected** bucket as the integrity
binding for an `x5chain` in a bucket the same section says *"allows an
intermediary to remove or add certificates"*. There the digest comparison is
the **only** check on which certificate arrived;
`records/ietf/rfc-9360/distilled/examples/vectors.yaml` V-0006 executes it and
shows the protected bytes are identical across the rewrite. Confirming the
public key validates the signature establishes that *a* key works — not that
the *certificate*, and therefore the identity bound to that key, is the one the
signer sent.

**So the registration's own justification does not hold in the position the
justifying document recommends.** `rfc-9360`'s record carries the `contradicts`
edge because the root is internal to RFC 9360 (§2 against §5); this record is
where the *inheritance* is visible. Neither half is readable from one document:
RFC 9054 §3.2 points forward at a draft, and RFC 9360 never points back.

---
## 5. `DEC-003` — it supplies the hash identifier and is silent on what gets hashed

`DEC-003`'s mandatory clause: *"must specify canonical key bytes before
hashing."* **[Unverifiable from this repository — `mofn` decision.]**

**RFC 9054 never says what gets hashed, anywhere, for anything.** It defines
the identifier space and the field that holds a digest, and the object on the
other side of the digest is the application's business. `§2.1`'s field 3 is a
pointer *"to the value that was hashed"* and its type is `tstr` with no stated
syntax — the document lists four different kinds of thing it might be:> * A pointer to the value that was hashed. This could be a pointer to a file, an object that can be obtained from the network, a pointer to someplace in the message, or something very application specific.
Four kinds of reference in one text string with no discriminator.

So `DEC-003` gets exactly half of what it needs from here. The other half is
`rfc-9360`, which *does* specify what gets hashed and specifies the wrong thing
(the DER certificate rather than the key). **Between the two documents that
should have settled "which hash names a key", one names the hash and not the
object and the other names the object and gets it wrong.**

### 5.1 [analysis] The `rfc-9679` inversion, verified

A hypothesis this library already refuted once, restated so it is not
re-asserted: **RFC 9054 does not supply the algorithm identifiers `rfc-9679`'s
thumbprint selects from.** Verified independently by this pass over
`.cache/rfc-9679.txt`: **`9054` occurs zero times**, and *"COSE Algorithms"*
occurs zero times. RFC 9679's `H` is chosen by the application and is not
carried in the thumbprint value, so two parties on different `H` never match
and cannot tell why — that is `rfc-9679`'s own `profile: full` finding.

**The useful inversion.** `-16` is the citation that *would* close RFC 9679's
algorithm-agility hole, and RFC 9679 cannot reach it: it names no identifier
space, so there is nothing for the identifier to go in. The shape is the same
as the `rfc-8230` edge `rfc-9679` already carries — a rule that exists and is
unreachable from the document that needs it. `see_also: rfc-9679` on this
record records it from this side.

---
## 6. `canonical-encoding` conditions (1)–(6), and the one the document supplies

The six conditions are `topics/canonical-encoding.yaml`'s, which **is** in this
repository.

**Condition (1) — injectivity — is the one RFC 9054 contributes, and it
contributes it in a parenthetical.** §2.1, on the additional-data field:> The additional data can be dealt with in a number of ways, prepending or appending to the content, but it is strongly suggested that either it be a fixed known size, or the lengths of the pieces being hashed be included so that the resulting byte string has a unique interpretation as the additional data. (Encoding as a CBOR array accomplishes this requirement.)
That is an injectivity argument: a byte string with a *unique
interpretation*. `examples/vectors.yaml` V-0007 executes the collision it
prevents — `("AB","C")` and `("A","BC")` concatenate to the same three octets
and therefore hash identically, while their CBOR array encodings differ in
their length heads and hash differently. **Zero cryptographic work, and the
document's parenthetical is the fix.** It is lower case, non-normative, and
citable, which is the difference between citing and inventing.

The rest:

| condition | verdict for RFC 9054 |
|---|---|
| **(1)** injective, not merely deterministic | **supplied, as advice.** §2.1's length rule, with the CBOR-array mechanism named. Lower case ("strongly suggested"), in an Informational document, and it applies only to the additional-data field — not to the structure as a whole |
| **(2)** the decoder REJECTS non-canonical input | **not addressed.** The document states no decoder behaviour and no encoding rule of any kind |
| **(3)** canonicalisation runs once, at authoring, on trusted input, never during verification | **not addressed, and §1's indirect-signing paradigm runs the other way:** the hash is recomputed over content downloaded *later*, i.e. over untrusted input, during verification. That is the paradigm the identifiers exist for, and the document gives no rule for it |
| **(4)** the profile is named by an authenticated type indicator inside the signed bytes | **PASS, and stated.** §1: the hash value *"-- along with an identifier for the hash algorithm --"* is included in the content that will be signed. The algorithm indicator is in-band and inside the signed bytes, which is the shape `R-O-05` wants. Same answer as `rfc-9360` §2's `x5t`, and the opposite of `rfc-9679`'s bare `ckt` |
| **(5)** set-valued fields in arrays have a defined canonical order | **not addressed.** No field in either §2.1 structure is set-valued |
| **(6)** text load-bearing for identity has a declared Unicode normalisation rule, or an explicit refusal plus rejection | **FAILED, and there is text in the hashed path.** §2.1's field 3 is a `tstr` locator and field 4 is `any`. `Unicode` occurs **zero** times in the source. If a locator or any text in the additional data is inside the digest, its normalisation decides the digest, and nothing says which |

**One pass, one supplied condition, four unaddressed and one failed** — which
is what an Informational registry document should be expected to score, and is
worth recording rather than omitting.

---
## 7. MD-3, header by header — and where this document cuts against it

`MD-3` narrowed `DEC-002` to **option 5**: `docs/extraction.md`, in this
repository, states it as *"reduced CBOR, no IANA tags, COSE as export only"*.
**A narrowing, not an acceptance.**

### 7.1 The header-by-header mapping

RFC 9054 defines no header, so the mapping is thinner than `rfc-8392`'s or
`rfc-9360`'s and the thinness is the point. Field names are `ARCH-0001` §4.1's.

| our field (`ARCH-0001` §4.1) | RFC 9054 carrier | code point | registry | option-5 verdict |
|---|---|---|---|---|
| digest algorithm indicator | the `Value` column of a COSE Algorithms entry | −16 (and 7 others) | COSE Algorithms (§4.1) | **carry** — this is the citation `R-O-03` needs |
| content digest (`R-M-07`) | **nothing** | — | — | **ours to invent**; §1 says the omission is intentional |
| pointer to what was hashed | §2.1 field 3, `tstr`, as an *example* | 3 | none | **adapt** — the field is right, the type is unusable (§5) |
| additional data / salt | §2.1 field 4, `any`, as an *example* | 4 | none | **adapt**, with §2.1's own length rule (§6) |
| "this digest is fit for binding" | **nothing** — `Recommended` is a registry column | — | COSE Algorithms | **cannot be carried.** Cut 2 |
| digest canonical form | **nothing** | — | — | **ours**; §2.1's parenthetical is the only constraint |
| CBOR tag for a digest structure | **none allocated** | — | — | nothing to drop; the document registers **zero** tags |

**The export mapping, in one line.** Our digest structure, whatever it is,
carries a COSE Algorithms integer from the set `{-16, -17, -18, -43, -44, -45}`
as its algorithm field, with the field inside the signed bytes, the digest
length pinned per algorithm, and the structure itself cited to nothing because
there is nothing to cite.

**What we deliberately do not carry:** `-14` and `-15` (Cut 2 and
`schema/hash-algorithms.derived.yaml`), §2.1's four-field structure as printed
(§3), and `Recommended` as anything but an input to our own profile.

### 7.2 Cut 1 — the expensive dependency is an **absent structure**, not a tag. Costs **option 5**; option 1 does not pay it

**Count the ledger first.** RFC 9054 registers **zero CBOR tags**. Measured:
`tag` occurs once in the whole document, inside the word *"tagged"* at line
383, about the `Recommended` column. Its eight allocations are negative
integers in the COSE Algorithms registry, which option 5 already accepts by
keeping COSE as the export form. **So option 5's "no IANA tags" clause is
untouched here, and §4.1's two-byte rationale is a size argument that agrees
with "reduced CBOR" rather than straining it** — see Cut 4 for what is wrong
with the rationale itself.

**The cost is one layer down from where option 5's exclusions operate.** Option
5 says "no IANA tags"; this document shows the expensive dependency is not tags
but the **absent carrier** (§1, §2.1). Under any COSE-exporting option our
digest-bearing structure is a native invention that `R-O-03` then obliges us to
cite, and **there is nothing to cite**.

**Option 1 does not pay this cost.** SPKI defines `(hash sha1 |…|)` as a
self-describing hash object (`rfc-2693` §2.8, §7.3), so the carrier *and* the
algorithm name are cited together from one document. COSE gives the algorithm
number and nothing to put it in. [analysis] This is the second ground in this
lane on which option 1 comes out ahead of option 5 — `rfc-9360`'s Cut 5 is the
first — and `docs/extraction.md`'s worked example is the precedent for saying
so: RFC 9804's extraction put option 1 *"on the right side of all four grounds
that withdraw option 3"*, and that finding existed only because the extraction
was not required to agree with the narrowing.

### 7.3 Cut 2 — the export format cannot carry the fitness judgement. Costs **option 5** by construction

§4 above, as a `DEC-002` entry. `Recommended: Filter Only` is a **registry
column**; `COSE_Hash_Find` and `COSE_CertHash` have two fields each; nothing in
COSE carries the column. So "COSE as export only" means we export into a format
that can name *which* `H` and cannot name *whether that `H` was fit for the
job* — and our profile has to supply the restriction because the format cannot
express it.

Options 1 and 3 pay this only if they choose to cite the same registry; option 5
pays it by construction. And note the asymmetry with Cut 1: there, option 1 wins
because it has a carrier; here, option 1 wins because `(hash sha1 |…|)` has no
`Recommended` column to be unable to carry — the algorithm name is simply the
algorithm name, and any fitness policy is the application's either way. **That
is a weaker win and should be scored as one.**

### 7.4 Cut 3 — citing the registry inherits an under-specified value. Costs **option 5** by construction

`-15` is defined by one sentence of a NOTE:> NOTE: SHA-256/64 is a simple truncation of SHA-256 to 64 bits | defined in this specification. SHA-512/256 is a modified | variant of SHA-512 truncated to 256 bits, as defined in | [FIPS-180-4].
**"defined in this specification" is the whole of the definition, and it does
not say which 64 bits.** `examples/vectors.yaml` V-0003 computes both readings
over one input and they differ; the document prints **no test vector** for any
of its eight algorithms, so nothing pins it. Leading is the universal
convention and **the document does not say so** — but rfc-9053 does say so for the exactly analogous case, and it is in this repository: *"When truncating, the leftmost tag-length bits are kept and transmitted"* (RFC 9053 section 3.1, .cache/rfc-9053.txt lines 424-425, region sha256 b04d568a758cd9de7c16ea051cfb3442f9bd0ee3b5ff933d39347e67539d725a), about HMAC 256/64 - the same truncation of the same hash to the same length, in the same registry, by the same working group. RFC 9054 does not cite it.

"COSE as export only" means the COSE Algorithms registry is ours by
construction, and a registry is a set of values, not a set of good values. **An
option that adopts a registry adopts its worst member.** Our profile excludes
`-15` (`schema/hash-algorithms.derived.yaml`), and if we ever accept it the
truncation rule has to be cited to FIPS 180-4 rather than to RFC 9054 — which is
`R-O-03` applied to a gap in the document we are citing *for* `R-O-03`.

### 7.5 Cut 4 — §4.1's own size rationale is backwards, and option 5's cost model is what notices

**A point in option 5's favour, and a source defect, from the same
measurement.** §4.1 says:> Many of the hash values produced are relatively long; as such, use of a two-byte algorithm identifier seems reasonable.
and then:> SHA-1 is tagged as "Filter Only", so a longer algorithm identifier is appropriate even though it is a shorter hash value.
Against RFC 8949 §3: a negative integer `-1-n` with `n < 24` fits in the
initial byte, so −1 to −24 cost **one** octet and −25 and below cost two.
`examples/vectors.yaml` V-0001 computes all eight: **five of the eight (−14 to
−18) cost one octet**, and **SHA-1 at −14 encodes as the single octet `0x2d`**
— the shortest class available — while SHA-384 at −43 costs two (`0x382a`). The
allocation does the **opposite** of what the rationale says it does, for the one
algorithm the rationale names.

[analysis] Two things follow. **As a source defect**, it is a new one: no
erratum covers it (the search returned exactly one erratum, 7335, on §2.1's
comment markers), and anyone who reads §4.1's reasoning as a design principle
will mis-size their own allocations. **As a `DEC-002` datum, it is a point for
option 5**: "reduced CBOR" makes you count octets, and counting octets is what
catches this. An option that does not price its encodings would have read §4.1
and believed it. That is the smallest of the five cuts in this lane and it is
the only one that runs in option 5's favour, which is worth saying for exactly
that reason.

### 7.6 And the one place option 5 is simply right

§2.1's injectivity rule names the mechanism it wants: *"(Encoding as a CBOR
array accomplishes this requirement.)"* **Reduced CBOR gives us that
mechanism for free**, and `examples/vectors.yaml` V-0007 shows what it buys —
the difference between a zero-work collision and none. Option 3 would need
JCS's array rules to do the same job and gets there too; option 1's
S-expressions are length-prefixed by construction and get there most cheaply of
the three. **No cut here; a convergence.** Recorded because `docs/extraction.md`
asks for where a source supports option 5 as well as where it does not.

---
## 8. `DEC-005` — two keywords, both `SHOULD`, both about collisions

`DEC-005`. **[Unverifiable from this repository — `mofn` decision.]**

RFC 9054 is **Informational** — *"This document is not an Internet Standards
Track specification; it is published for informational purposes"* (Status of
This Memo, source line 25) — and it has **two** BCP 14 keywords in 498 lines.
Both are in §2 and both are about collision attacks:> A hash function that is susceptible to practical collision attacks SHOULD NOT be used for a cryptographic purpose.
and> The discovery of theoretical collision attacks against a given hash function SHOULD trigger protocol maintainers and users to review the continued suitability of the algorithm if alternatives are available and migration is viable. The only reason such a hash function is
**Neither is decidable by an implementation.** "practical" is never defined,
and §5 concedes the target moves: *"the cryptographic strength of hash
algorithms will be reduced over time"*. The second is doubly conditioned — on
alternatives being available *and* migration being viable — and its actor is
*"protocol maintainers and users"*, i.e. people. And the escape hatch is wide:> The only reason such a hash function is used is when there is absolutely no other choice (e.g., a Hardware Security Module (HSM) that cannot be replaced), and only after looking at the possible security issues. Cryptographic purposes
[analysis] That is a deployment excuse promoted to a specification clause,
and `DEC-005` should not copy it. What `DEC-005` can take from here is the
*shape* of the distinction — §5's separation of collision resistance from
second pre-image resistance, which is the sharpest sentence in either document
of this lane:> The different attacks correspond to who or what is being protected: is it the originator that is the attacker or a third party? This is the difference between collision resistance and second pre-image resistance. As a general rule, longer hash values
Measured: `collision` occurs **15** times in RFC 9054 and **zero** times in
RFC 9360 — the document whose central mechanism is a digest comparison. The
vocabulary for reasoning about hash fitness exists in this lane and it is in
the document that has no normative force.

---
## 9. `DEC-002`'s other half — what the document says about SHA-1 and about agility

Two facts worth carrying, both about time rather than about encoding.

**SHA-1 is registered in 2022, eleven years after the IETF discouraged it, and
the strongest sentence about it is lower case.** §3.1:> [SHA-1-collision]. The IETF formally started discouraging the use of SHA-1 in [RFC6194].
and then> Because of the known issues for SHA-1 and the fact that it should no longer be used, the algorithm will be registered with the recommendation of "Filter Only".
"should no longer be used" — lower case, so under §1.1 it binds nobody.

**And agility is advice with no mechanism.** §5:> Algorithm agility needs to be considered a requirement for any use of hash functions [BCP201].
The document defines **no negotiation, no deprecation rule, no sunset and
no way for an endpoint to express which `H` it accepts.** `state-machine.yaml`
records the verdict and the measurement behind it: there is a progression in
view — sound, theoretically attacked, practically attacked, Filter Only,
unusable — and **not one of its steps is defined**. The actor is people, the
trigger is undefined, the transition is a *review* rather than a change of
state, and nothing says how the `Recommended` column is ever revised.

[analysis] So the agility policy for a hash we have cited is **ours to write,
in full**, and the `NOT APPLICABLE` state-machine verdict is the evidence that
there is nothing to inherit. `rfc-9360` §2's `MUST support SHA-256` is the only
mandatory-to-implement floor anywhere in this lane and it is in the other
document — which means a floor exists, a ceiling does not, and a deprecation
path does not.

---
## 10. What we adopt, adapt and reject

### 10.1 Adopt

1. **`-16` as the cited identifier for SHA-256**, and the six-value set
   `{-16, -17, -18, -43, -44, -45}` as the admissible range. This is the
   `R-O-03` citation (§2).
2. **§2.1's injectivity rule**, with the CBOR-array mechanism it names (§6,
   V-0007). Citable, and it is the only encoding constraint in the document.
3. **§1's in-band algorithm indicator**, inside the signed bytes — condition
   (4) (§6). The same answer `rfc-9360` gives and the opposite of
   `rfc-9679`'s.
4. **§5's collision-resistance / second-pre-image-resistance distinction** as
   the vocabulary for `DEC-005` (§8).

### 10.2 Adapt

1. **§2.1's four fields as the shape of our digest structure** — algorithm,
   value, locator, additional data — with the structure itself ours, the
   locator given a stated syntax, and the additional data a CBOR array of
   length-prefixed pieces (§6).
2. **§2's filtering argument as a *test*** rather than a category: a weak
   digest is admissible only where surviving candidates are each checked
   against the signature. Stated that way it is checkable, which neither
   document makes it (§4.1).
3. **§4.1's size reasoning, inverted into a rule**: price every code point in
   octets before allocating it, because §4.1 did not and got it backwards for
   five of eight (Cut 4).

### 10.3 Reject

1. **`-14` (SHA-1) and `-15` (SHA-256/64)** in any position of ours. `-14` is
   broken; `-15` is 64 bits *and* under-defined (Cut 3).
2. **`COSE_Hash_V` as printed** (§3): erratum 7335, plus a group-versus-type
   defect no erratum covers, plus a `tstr` locator carrying four kinds of
   reference with no discriminator.
3. **`Recommended` as a runtime signal.** It is a registry column and nothing
   carries it (§4). Our profile resolves fitness at authoring time, by
   restricting the range.
4. **§2's escape hatch** — "absolutely no other choice (e.g., a Hardware
   Security Module (HSM) that cannot be replaced)" — as specification text
   (§8).
5. **Agility as advice.** §5 says it "needs to be considered a requirement" and
   defines nothing. Ours needs a mechanism or an explicit statement that we
   have none (§9).

---
## 11. The summary's findings, tested against the source

1. **"It registers the identifiers and refuses the carrier."** **CONFIRMED**
   (§1, §2), with both sentences quoted and §1's "This omission was
   intentional" carried verbatim.
2. **"`COSE_Hash_V` uses `#` for CDDL comments where CDDL uses `;` (erratum
   7335, status *Reported*) … so the fragment does not parse."** **Erratum
   CONFIRMED** (and its status, type, reporter and date verified against the
   RFC Editor's errata search on 2026-10-20). **"Does not parse" REFUTED**
   (§3.1): it parses, as 24 group entries with 15 undefined names, and fails
   at name resolution. The summary's conclusion survives; its mechanism does
   not.
3. **"once that is fixed it is still a parenthesised group rather than a type,
   so it cannot be instantiated without a `{ }` wrapper the document never
   supplies."** **CONFIRMED mechanically** (§3.2): forced as a type rule it
   fails after 14 characters; RFC 8610 §2.2.4 forbids a group as a root.
4. **"`COSE_Hash_Find` is a proper array type and does parse."**
   **CONFIRMED** (§3.3), and extended: it is `rfc-9360`'s `COSE_CertHash`
   field for field, and the two encode identically for all eight algorithms
   (V-0006).
5. **"Filter Only is a registry column, not a wire field … a verifier handed
   `[-14, h'…']` cannot tell whether the sender was filtering or binding."**
   **CONFIRMED** (§4), and scoped by a finding the summary does not make: the
   value is **defined twice**, in §2 and §4.1, and the two definitions are not
   the same constraint.
6. **"`-16` is the citation that would close RFC 9679's algorithm-agility hole,
   and RFC 9679 cannot reach it."** **CONFIRMED** (§5.1). The zero-citation
   count was re-verified by this pass directly against `.cache/rfc-9679.txt`:
   `9054` zero, *"COSE Algorithms"* zero.
7. **"SHA-256/64 … with no statement of which 64 bits … and no test vector."**
   **CONFIRMED and made testable** (Cut 3, V-0003): both readings computed, and
   they differ.
8. **"RFC 9054 registers zero CBOR tags: the string "tag" occurs once in the
   whole document and it is the word "tagged" in §4.1's prose."**
   **CONFIRMED** by sweep, and refined: as a whole word `tag` occurs **zero**
   times; the one occurrence is as a substring of `tagged` at line 383.
9. **"It does not cut [against MD-3], and the reason is worth recording."**
   **SCOPED — and this pass disagrees with the "does not cut" verdict.** Four
   cuts are now named (§7.2–§7.5), three of them costing option 5 and one
   running in its favour, plus one convergence (§7.6). The summary's
   underlying claim — that the cost is an absent structure rather than a tag —
   is Cut 1 and is confirmed; the claim that there is no cut is withdrawn.

---
## 12. Source defects and ambiguities — reported, never repaired

**E-1. Erratum 7335** (*Reported*, Technical, §2.1): `#` for `;` in
`COSE_Hash_V`. Verified against the RFC Editor errata search on 2026-10-20,
which returns `Reported (1)` for RFC 9054. The *only* erratum on this RFC.

**E-2. `COSE_Hash_V` is a group, not a type**, and nothing wraps it (§3.2). No
erratum covers it. It is the more serious of the two defects in the same six
lines.

**E-3. §4.1's size rationale is backwards for five of eight allocations**
(Cut 4), and exactly backwards for the one algorithm it names. No erratum.

**E-4. Table 2's Description for `-17` reads "SHA-2 512-bit Hash truncated to
256-bits"**, which is precisely what §3.2's NOTE says it is not — the NOTE
calls it *"a modified variant of SHA-512 truncated to 256 bits, as defined in
[FIPS-180-4]"*, i.e. a different initial value rather than a post-hoc
truncation. The row and the NOTE are 30 lines apart, and **the row is what gets
copied into a lookup table.** `examples/vectors.yaml` V-0004 computes both and
they differ completely. No erratum.

**E-5. `-15` is defined by one sentence that does not say which 64 bits**
(Cut 3). No erratum, and no test vector anywhere in the document to pin it.

**E-6. "Filter Only" is defined twice in incompatible terms** (§4). No erratum.

**E-7. §2.1 field 3 is a `tstr` carrying four different kinds of reference with
no discriminator** (§5).

**E-8. The document prints two CDDL fragments, never uses the word "CDDL", and
cites RFC 8610 in neither its normative nor its informative references.**
Measured: `CDDL` zero occurrences. So the grammar the fragments are written in
is nowhere identified, and the erratum that corrects one of them has to appeal
to a document the RFC does not cite.

**E-9. SHAKE gets no truncated identifiers and SHA-2 does, with no reason
given.** §3.3: *"Unlike the SHA-2 hash functions, no algorithm identifier is
created for shorter lengths."* The two decisions are inconsistent — `-15` is a
truncation the document does not locate, while a SHAKE identifier carries its
length — and §3.3 offers no rationale.

**Nine items, none repaired here.** `requirements.yaml` carries each in the
`note` of the entry it belongs to.

---
## 13. Open questions

1. **Does `R-O-03` cover the carrier or only the algorithm?** §2 says the rule
   as written is satisfiable by citing `-16` while the whole four-field
   structure around it is invented. Either the rule should cover the envelope
   or it should say that it does not.
2. **Which 64 bits does SHA-256/64 keep?** If we ever accept `-15`, the
   truncation rule must be cited to `rfc-9053` §3.1's leftmost-bits sentence
   (and behind it FIPS 180-4) rather than to RFC 9054, which does not state one
   (Cut 3). Our current answer is to exclude `-15`.
3. **What is our deprecation path for a cited hash?** §9: there is nothing to
   inherit. BCP 201 (RFC 7696) is what both §2 and §5 point at for this and
   this library does not hold it. **Worth ingesting** — it is the one missing
   reference this record's gaps keep pointing to.
4. **Do we carry a locator field at all?** §2.1's field 3 is the only prior art
   and it is a `tstr` with four meanings. If our digest structure has a
   pointer, its syntax is ours to define and `R-O-03` arguably applies to that
   too.
5. **Is a `Recommended`-column equivalent worth carrying on the wire?** §4 says
   COSE cannot, and that is what makes `rfc-9360`'s `x5t` ambiguous. A field
   that said "this digest is load-bearing" would make our own structure
   self-describing where COSE's is not — at the cost of a field nobody else
   has.
6. **Should this record carry a `contradicts` edge of its own?** Today the
   `rfc-9360` conflict is recorded on `rfc-9360` because the root is internal
   to that document (§2 against §5), and this record carries only `see_also`
   edges. §4.1 shows the *inheritance* is a real and separately citable fact:
   this document's §3.2 justifies `-15` by pointing at a configuration that
   does not satisfy its own safety argument. Whether that earns an edge is a
   curatorial call, not this pass's.
