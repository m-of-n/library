---
record: rfc-8742
kind: design-notes
title: "rfc-8742 — bearing on our design"
extracted: "2026-10-20"
reviewed_by: ""
---

**Scope and provenance conventions.** Section numbers with no document name
(`§2`) are RFC 8742. Our own documents are cited by id (`ARCH-0002` P1, `MD-3`,
`R-O-03`). Four markers distinguish voices:

- unmarked prose reports **RFC 8742** or **our decisions**, as cited;
- a quotation is RFC 8742's own words, contiguous and mechanically checked,
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
such file. **Every quotation of those documents below is therefore
unverifiable from this repository** and is marked `[unverifiable-here]` at
first use in each section. The convention is `rfc-9741`'s, established by its
cross-check pass; this record follows it from pass 1 rather than acquiring it at
pass 3. What **was** verified in-library at this pass is listed at the end of
this file. **One exception, in the other direction:** the quotations in §8 are
of this record's own `summary.md`, which *is* in this repository; each was
checked against its rendered text at this pass, and §8 names it in every case.

**Decision status, stated plainly.** `DEC-002` in `ARCH-0001` §7 lists **four**
options — (1) canonical S-expressions, (2) "CBOR + CDDL as canonical; COSE for
signed form", (3) JSON + RFC 8785 JCS, (4) "Dual canonical (CBOR and JSON) with
a documented bijection" `[unverifiable-here]`. "Option 5" exists only as
*proposed* text in `ARCH-0001-PROPOSAL-v0.2.0` §3.3. `MD-3` (2026-09-28)
**narrowed** DEC-002 to option 5 — reduced CBOR, no IANA tags, COSE export only,
YAML as the human form — and a narrowing is **not** an acceptance: **no DEC-002
ADR exists.** `docs/extraction.md` is explicit that "An extraction that can only
confirm is not evidence." Nothing below may be read as an accepted encoding
decision.

**What this document is, in one line.** The claim that a container is
unnecessary: concatenate encoded CBOR data items and the bytes *are* the format.
**Four BCP 14 keywords in 18 KB, none of them in §2**, and two of the four
vacuous at publication by the document's own admission. It registers three
things and **not one of them is a CBOR tag**.

**Why a 7-page format RFC reaches our design at all.** Because MD-3's option 5
names no container, and this is the only ratified answer to *how two
statements share one file*. `[analysis]` On the letter of option 5's exclusion
list — no reliance on the IANA CBOR Tags registry, no native use of COSE header
parameters — a CBOR Sequence is **admissible**: measured at this pass, the word
"tag" occurs **0 times** in RFC 8742 and the word "header" occurs **0 times**.
That admissibility is exactly the danger: **it will become the container nobody
chose.**

---

## 1. The question this record was extracted to answer

**Can a CBOR Sequence state how many items it should contain, or report that it
is complete? No — and §2 says so three separate times.**

1. **"There is no end-of-sequence indicator."** (`rfc-8742#R-0013`) Five words,
   no qualification.
2. The format **"can reliably detect truncation of the bytes making up the last
   CBOR data item in the sequence, but it cannot detect entirely missing CBOR
   data items at the end."** (`rfc-8742#R-0024`)
3. **"an empty (zero-length) sequence of bytes"** is case one of the definition
   (`rfc-8742#R-0009`), and decoding it yields "an empty sequence of CBOR data
   model values" (`rfc-8742#R-0018`).

`[analysis]` Together, and this is the finding to act on: **truncating an
append-only log at an item boundary is in spec and undetectable, and a log
truncated to nothing is a valid empty log.** The three fixtures are
`examples/vectors.yaml` `D-0004` (two items, no error), `D-0005` (zero bytes, no
error) and `D-0001` (the empty sequence), and `D-0001` and `D-0005` are
deliberately the **same bytes**. `state-machine.yaml` carries the same finding
as an indistinguishability between two states that the source never names.

**And one corrupt entry costs the tail, not just the entry.** §2: "if any data
item in the sequence is not well formed, it is not possible to reliably decode
the rest of the sequence." (`rfc-8742#R-0021`) There is no marker to
resynchronise on, because §2 declines the one RFC 7464 uses: "CBOR Sequences,
unlike JSON Text Sequences [RFC7464], do not use a marker between items."
(`rfc-8742#R-0015`) Fixture `D-0007`.

**§5 closes the escape route rather than opening one.** "(COSE protections can
be applied to an entire CBOR Sequence or to each of the elements of the sequence
independently; in the latter case, additional effort may be required if there is
a need to protect the relationship of the elements in the sequence.)"
(`rfc-8742#R-0042`) `[analysis]` Option 5's export story is per-statement
`COSE_Sign1`, which is "the latter case". So **an exported bundle of *n* signed
statements is *n* facts and no fact about the bundle**: nothing binds the count,
nothing binds the order, and under `R-O-01` `[unverifiable-here]` the sequence
has no issuer key at all, because the sequence is not a signed object. The whole
of the guidance offered is "additional effort may be required". **Nothing in
RFC 8742 supplies that effort or asks for it.**

---

## 2. What we adopt

### 2.1 §4.3's byte-string wrapper, as the element form — not as an optimisation

"For these applications, byte strings (which carry length information in bytes)
containing embedded CBOR can be used as the elements of a CBOR Sequence:"
(`rfc-8742#R-0038`), with the bound stated in the same breath: "Within limits,
this may also enable recovering from elements that internally are not well
formed; the limitation is that the sequence of byte strings does need to be well
formed as such." (`rfc-8742#R-0039`)

The document offers this for **skipping and fan-out** — "being able to
efficiently skip an element without the need for decoding its substructure, or
efficiently fanning out elements to multi-threaded decoding processes"
(`rfc-8742#R-0037`). `[analysis]` **We should adopt it for durability**, which is
an argument the document does not make. Fixtures `D-0007` against `D-0009`: the
same corrupted byte destroys the tail of a bare sequence and costs **one
element** of a wrapped one. `D-0010` is where that stops — a corrupt
byte-string *head* still strands the tail, because the length that makes
skipping possible is itself in the bytes being skipped.

**Cost, computed at this pass:** 1 byte of head per element under 24 bytes, 2
under 256, 3 under 65536, 5 under 2**32. For a 100-byte statement that is about
2%. `[analysis]` It is tag 24's pattern with the tag removed — the move
`rfc-8949`'s design notes already record option 5 making for its signed payload
— so a tag-free profile converges on this shape anyway. **The point is that it
has to be *chosen*: nothing in option 5 chooses it.**

### 2.2 §2's own alternative, for a finished signed export

"(If one is desired, CBOR encoding an array of the CBOR data model values being
encoded, employing either a definite or an indefinite length encoding, as a
single CBOR data item may actually be the more appropriate representation.)"
(`rfc-8742#R-0014`)

`[analysis]` A **definite-length** array head states *n*, is self-delimiting, and
**uses no tag** — so it is exactly as admissible under MD-3's no-tags rule as the
sequence is. Fixtures `D-0003` (`83010203`, 4 bytes) against `D-0002`
(`010203`, 3 bytes), and the pair that decides it, `D-0006` against `D-0004`:
**the same deletion is loud in an array and silent in a sequence, and the
difference is one byte of head.**

**This settles a question, and it is not a DEC-002 question.** A finished signed
export should be an **array**; an append-only log is the only thing that needs
the sequence, and the one thing the sequence buys — incremental append — is the
same thing that makes the count unstateable. **Two artifacts, and option 5
currently names neither.** The document wrote the sentence for us; one line of
ADR work takes it.

The **indefinite-length** variant §2 also offers is excluded: it hands the
problem straight back (no count in the head) and every deterministic profile this
library holds forbids it (RFC 8949 §4.2.1, `draft-ietf-cbor-cde`,
`draft-mcnally-deterministic-cbor`). The exclusion is recorded in
`schema/cbor-seq-container.derived.cddl` C4 rather than left silent.

### 2.3 The media type, as the out-of-band type indicator — and only that

`application/cbor-seq` (§6.1) and the `+cbor-seq` suffix (§6.3) are citable,
cost nothing, and live out of band. `[analysis]` Under `R-O-03`
`[unverifiable-here]` — *"canonicalization algorithm SHALL be cited, not invented
silently"*, generalised once already by `docs/extraction.md` to filenames — a
registered media type is the **strongest** citation available for a type
indicator. It is also the only one left to us for this format, because **§6.1's
own registration says there is nothing in the bytes**: "Magic number(s): N/A"
(`rfc-8742#R-0046`) and "File extension(s): N/A" (`rfc-8742#R-0047`). Two of the
three out-of-band substitutes `rfc-8949`'s design notes list are therefore
unavailable for `application/cbor-seq` **by its own registration**, which leaves
the media type itself.

---

## 3. What we adapt, and how

### 3.1 §4.1's container rule — adapted into a derived schema, with its status on the filename

"Currently, CDDL does not provide for unadorned CBOR Sequences as a top-level
subject of a specification. For now, the suggestion is to use an array for the
top-level rule, as is used for the ".cborseq" control operator, and add English
text that explains that the specification is really about a CBOR Sequence with
the elements of the array:" (`rfc-8742#R-0030`, `rfc-8742#R-0031`)

`[analysis]` `schema/cbor-seq-container.derived.cddl` is that adaptation: the
rule written four ways with the byte cost of each, so a DEC-002 ADR chooses
rather than inherits. It is `.derived.` **by construction** and not by
convention — §4.1 says CDDL cannot write it, and
`schema/cbor-seq.derived.abnf` shows ABNF cannot either, so under `R-O-03` there
is **nothing to cite** and whatever we write is ours.

Note what the adaptation preserves: in `V-0002` the **two comment lines are the
specification of the container**, and they have no machine meaning. A validator
handed a real multi-element file and that rule **rejects the file**.

### 3.2 §5's COSE sentence — adapted into one rule for the export profile

`[analysis]` The fix for §1's finding is one sentence, and it belongs in the
export profile rather than in the encoding: **a count, a chain or a root, inside
the signed bytes.** Under `R-O-05` `[unverifiable-here]` — *"The signed payload
SHALL be the canonical encoding verbatim"* — that sentence has to name what the
signed payload *is* for a bundle, and §2's array (2.2) is the cheapest answer
because its head already carries *n*. `R-M-11` `[unverifiable-here]` requires
that "At least one content digest SHALL be bound in all cases"; a bare sequence
offers no content to digest that is not an element.

---

## 4. What we reject, and why

- **The bare CBOR Sequence as the shape of a signed export.** §1 and 2.2. It is
  admissible under option 5 and it cannot state its own count. Rejected for
  exports; retained for the append-only log, where append is the requirement.
- **The indefinite-length array.** 2.2.
- **§4.2's bracket-free diagnostic notation, for anything of ours.** It is
  permitted only "In a more informal setting, where the boundaries within which
  the notation is used are obvious" (`rfc-8742#R-0035`), and the document
  concedes it cannot write the empty case: "Note that it is somewhat difficult
  to discuss zero-length CBOR Sequences in the latter form."
  (`rfc-8742#R-0036`) `[analysis]` `library#39` assigns EDN the test-vector role;
  a fixture whose notation cannot express one of the format's two definitional
  cases is not a fixture language.
- **§3's `SHOULD` test for the suffix, as a rule we could apply.** "it SHOULD be
  used by a media type when the result of parsing the bytes of the media type
  object as a CBOR Sequence is meaningful and is at least sometimes not just a
  single CBOR data item." (`rfc-8742#R-0026`) **"At least sometimes" is
  unquantified**, and the document's own parenthesis explains that the
  qualification exists only to stop the sentence being trivially true. It is the
  only conduct rule in the document aimed at a specification author and it has
  no decision procedure. If we ever register `application/mofn-statement-log+cbor-seq`
  the test cannot tell us whether we qualify.
- **Citing RFC 8742 without also citing RFC 8949 and RFC 9052.** §2 defines the
  sequence over "an encoded CBOR data item [RFC7049]" and §5's COSE reference is
  [RFC8152]; both are superseded, the header carries no `Updates:` or `Obsoleted
  by:` line, and **RFC 8949 and RFC 9052 are named nowhere in the document**.
  Under `R-O-03` citing RFC 8742 drags two superseded documents in behind it.
  The `see_also` edges on `record.yaml` are what make the current specifications
  reachable; the citation in any document of ours must name all three.

---

## 5. Mapping to our decisions

### 5.1 MD-3, header by header — and the mapping is **empty**, which is the datum

FX-1 requires that a CBOR/COSE/envelope record address MD-3 **header by
header**. For this document the honest header-by-header mapping is **empty**, and
it is empty for a measurable reason rather than from inattention:

| MD-3 option-5 clause | what RFC 8742 contributes | measured |
|---|---|---|
| **reduced CBOR** (data model, no extras) | nothing — the document adds no data-model element, no type, no value | the words `tag`, `header`, `canonical`, `determinis*`, `digest`, `hash`, `profile`, `UTF-8`, `Unicode`, `normaliz*` occur **0 times** each in the whole 462-line source |
| **no IANA tags** | **nothing to give up.** The format uses no tag, and §6 registers three things, none of them a tag | `tag` = 0 occurrences |
| **COSE as export only** | **one sentence, and it is a warning** — `rfc-8742#R-0042`, that per-element protection does not bind "the relationship of the elements in the sequence". `cose` occurs 3 times, all in §5 and §1's informative reference | `header parameter` = 0 occurrences; no COSE header is named |
| **YAML as the human form** | nothing. §4.2 offers CBOR diagnostic notation and says it cannot express the container either | `YAML` = 0 occurrences |

`[analysis]` So **RFC 8742 has no headers to map and MD-3 has no header
objection to raise against it.** What it supplies instead is a *container*, a
layer MD-3 does not legislate at all — which is why §Cut 1 below is about
inheritance rather than conflict.

### 5.2 `ARCH-0001` §4.1, structure by structure `[unverifiable-here]`

The useful mapping for this document is not field-to-header but **artifact-to-container**: which of our artifacts is one data item and which is a file of many.

| our artifact (`ARCH-0001` §4.1) | one item or many? | container verdict |
|---|---|---|
| a single statement | **one** CBOR data item | no container question; RFC 8742 does not apply |
| `KeyId` (digest of canonical key bytes, `DEC-003`) | **one** byte string | no container question. `DEC-003`'s open point — "must specify canonical key bytes before hashing" — is untouched by this document |
| `ArtifactId` `{alg, hex}` | **one** map | untouched |
| `Name.labels` (`ARCH-0002` P1 local labels) | **one** array | untouched. P1's `(key, local label)` pair is a *naming* structure, not a file |
| `Threshold` | **one** map | untouched; `R-M-12`'s `(key, local label)` pair likewise |
| a **statement log** (append-only) | **many** | **CBOR Sequence**, with §4.3's wrapper (2.1). The one artifact the sequence is right for, because append is the requirement |
| a **signed export bundle** (`R-I-03`) | **many** | **definite-length array** (2.2). The head states *n*; the sequence cannot |
| a **key set** or a **trust anchor file** | **many** | array. Same argument; no append requirement at all |
| a **domain of discourse** (`ARCH-0002` P4) | **many** schemas, hashed as a unit | array, necessarily: P4 requires a form "that can be reliably and repeatably hashed", and a sequence has no form to hash that is not an element |

`[analysis]` The table has one shape: **everything of ours except the log wants
an array, and the log wants the sequence for exactly one reason.** That is a
one-line ADR input and the document supplies the sentence for it.

### 5.3 The `canonical-encoding` topic's six conditions

| condition | does RFC 8742 bear on it? |
|---|---|
| **(1) injective encoding** | **No** — but note the near miss. The format is injective over *sequences of values* only if each element's encoding is (which is RFC 8949's problem, not this document's); the sequence contributes no bytes of its own, so it adds no non-injectivity. `[analysis]` The one exception is the pair `D-0001`/`D-0005`: the empty sequence and the destroyed sequence have one encoding and two meanings, which is condition (1) failing at the *file* level rather than the value level. **No condition covers that, and it is the gap this record found.** |
| **(2) decoder rejects non-canonical input** | **No.** The document's only decoder obligation is §5's one `MUST` to "fail gracefully", and the one statement of *how* to decode is lower-case `must` (`rfc-8742#R-0019`). Nothing is rejected because nothing is non-canonical: there is no canonical form to deviate from |
| **(3) canonicalise once, at authoring** | **No**, and it cannot: there is nothing to canonicalise |
| **(4) authenticated type indicator inside the signed bytes** | **Yes, negatively, and sharply.** All three of §6's registrations are **out of band**, and §6.1 states the in-band position in two fields: "Magic number(s): N/A", "File extension(s): N/A". So the *only* type indicator available for a CBOR Sequence sits **outside every signature**. `R-O-05` `[unverifiable-here]` delivers (4) by carrying the indicator inside the signed bytes, and this format gives it nothing to carry. See `rfc-9277`'s record for what the IETF's in-band answer costs |
| **(5) canonical order for set-valued fields** | **Yes, and it widens the gap.** The sequence **binds no order at all** — order is not a field, there is no count, and `R-0012`'s concatenation closure means two orderings are both well formed and both silent. For a set carried as a *file* rather than as an array, condition (5) is not merely unreachable: there is no object whose order could be constrained |
| **(6) declared Unicode normalisation rule** | **No.** `normaliz*`, `Unicode` and `UTF-8` occur **0 times** each in the source |

---

## 6. Where this document cuts against MD-3

`MD-3` is a dated **narrowing** of DEC-002, not an acceptance, and
`docs/extraction.md` requires that an extraction say where the source cuts
against it. **Five cuts. Four name the option they favour; one is stated in
option 5's favour.** `[analysis]` throughout — the document takes no view on our
decision.

**Cut 1 — option 5 inherits this container by inertia, and it is the only option
that does. Favours nothing; indicts the narrowing's silence.** On the letter of
option 5's exclusion list a CBOR Sequence is admissible: zero tags (measured: 0
occurrences of `tag`), zero COSE header parameters (0 occurrences of `header`).
`[analysis]` MD-3 legislates the *encoding* and says nothing about the
*container*, so the container arrives for free and unexamined — and its cost is
§1's completeness hole. Options 1, 3 and 4 all have a container story written
into the thing they cite; option 5 is the only one whose container is a document
nobody in the narrowing had read. **That is not an argument against option 5. It
is an argument that the ADR owes a container clause whichever option wins**, and
this record's §5.2 table is the clause.

**Cut 2 — the container is not schema-checkable under option 5 or option 2, and
it is under options 1 and 3. Favours option 1.** §4.1, in the document's own
words: "Currently, CDDL does not provide for unadorned CBOR Sequences as a
top-level subject of a specification." §4.2 says diagnostic notation has the same
hole "at this time". `schema/cbor-seq.derived.abnf` shows that **ABNF cannot
express it either**, and for a deeper reason: an encoded CBOR data item is
length-prefixed, which is a context-sensitive dependency no ABNF can state —
already established in
`records/ietf/rfc-8949/distilled/schema/cbor-head.derived.abnf`, verified
present in-library at this pass. So a multi-statement file's top-level rule is
**prose** under option 5 and under option 2 (which names CDDL explicitly), and
under `R-O-03`'s discipline an English-prose container is the weakest citation
available. **Option 1 pays nothing here, and this is checkable from a grammar
this library holds verbatim:** `records/ietf/rfc-9804/distilled/schema/canonical.abnf`
is RFC 9804 §7.2 in two productions, `c-sexp = c-string / ("(" *c-sexp ")")` and
`c-string = [ "[" verbatim "]" ] verbatim`, whose **start symbol is `c-sexp`** —
a single S-expression, so a canonical S-expression file has a grammar for the
*whole file*. Option 3's JSON Text Sequences likewise have RFC 7464 and a
`+json-seq` suffix (RFC 8091), which §2 and the Acknowledgements both name.

**Cut 3 — option 1's container detects the truncation option 5's cannot, and its
atoms carry §4.3's wrapper by grammar. Favours option 1, on two grounds the
narrowing never considered.** `[analysis]` Both grounds come out of
`rfc-9804`'s verbatim grammar, held in this library:
1. **Truncation.** A canonical S-expression list is `"(" *c-sexp ")"`, so the
   closing parenthesis **is** an end-of-sequence indicator. Deleting the last
   element of a list leaves the `)` in place and deleting the `)` leaves an
   unterminated list — either way the file fails the grammar. That is
   `examples/vectors.yaml` `D-0006`'s behaviour (detected) rather than
   `D-0004`'s (silent), **for free, from the grammar, with no array head and no
   profile clause.**
2. **Length prefixes.** `verbatim = decimal ":" *OCTET`
   (`records/ietf/rfc-9804/distilled/schema/advanced-transport.abnf` §7.1), so
   **every atom in the canonical form is length-prefixed.** That is precisely
   what §4.3's byte-string wrapper buys for a CBOR Sequence — skippability and
   bounded recovery — made **mandatory by the grammar** instead of optional and
   unchosen.

   **The trade is real and should be stated with it:** a canonical S-expression
   file is one `c-sexp`, so it is not appendable the way a sequence is, and
   `rfc-9804`'s own extraction records that the canonical form "preserves
   whatever order the author wrote" with no sorting step — so option 1 answers
   the *detection* half of condition (5) and not the *canonical order* half. This
   is the same trade as `D-0003` against `D-0002`, one layer down.

**Cut 4 — option 4's documented bijection does not extend to the container, and
this document is the evidence. Favours nothing; narrows option 4.** Option 4 is
"Dual canonical (CBOR and JSON) with a documented bijection"
`[unverifiable-here]`. §2 states the container-level divergence in the
document's own words: "CBOR Sequences, unlike JSON Text Sequences [RFC7464], do
not use a marker between items." And the Acknowledgements say this document "has
mostly been generated from [RFC7464] by Nico Williams and [RFC8091] by Erik
Wilde, which do a similar but slightly more complicated exercise for JSON
[RFC8259]" — *slightly more complicated* being exactly the marker. `[analysis]`
So the two halves of a dual canon have **different error behaviour at the
container layer**: the JSON side can resynchronise after a malformed record and
the CBOR side loses the tail (`rfc-8742#R-0021`, fixture `D-0007`). A bijection
of *values* is not a bijection of *failure modes*, and a dual-canon archive would
have two different answers to *how much of this file survives one corrupt byte*.
This is the same shape as `rfc-9679`'s Cut B, which eliminated option 4 because a
bijection at the encoding layer gives none at the identity layer; here it gives
none at the **durability** layer. **RFC 7464 and RFC 8091 are not held in this
library**, so the marker's identity and the JSON side's exact recovery rule are
`[unverified]` here — §2's sentence is the whole of the evidence.

**Cut 5 — and one point in option 5's favour, stated so the balance is honest.**
`[analysis]` **RFC 8742 is the one document in this lane that costs option 5
nothing in registry terms, and it is a measured zero rather than an absence of
evidence.** §6 makes three registrations — a media type, a CoAP Content-Format
number from the Expert Review range, and a structured syntax suffix — and **not
one is a CBOR tag**. Option 5's defining exclusion is reliance on the IANA CBOR
Tags registry, and the exclusion is simply not engaged. More than that: the
ecosystem minted a tag for the concept **anyway, from outside the RFC process**
— the IANA CBOR Tags registry carries tag **63**, semantics "Encoded CBOR
Sequence RFC 8742", reference `draft-bormann-cbor-notable-tags-02, Section 2.1`
(`records/iso/iana-cbor-tags/distilled/tables.yaml`, verified in-library at this
pass) — for an allocation this RFC never requested. `[analysis]` For `R-M-12`
`[unverifiable-here]` that is the **governance** half of the registry-reduction
argument and not the encoding half: *refusing to use a registry does not stop the
registry from describing you.* And note the trap: CoAP Content-Format **63**
(§6.2, Table 1) and CBOR tag **63** are **different namespaces** and the matching
numeral is a coincidence, checked at this pass.

**Option 4 note.** No cut is attributed to option 4 beyond Cut 4, and no cut is
attributed to option 2 beyond its share of Cut 2, because this document engages
neither on its own terms. Recorded so the absence is visible rather than read as
silence.

---

## 7. Source defects found

Six. All reported, none repaired.

1. **Two of the four BCP 14 keywords are vacuous at publication, by the
   document's own admission.** §6.3's two `SHOULD`s govern fragment identifiers
   for `+cbor-seq` by deferring to the same syntax and semantics as "that
   specified for "application/cbor-seq"" — which §6.1 registers as "Fragment
   identifier considerations: N/A", and which §6.3 then confirms: "(At the time
   of publication of this document, there is no fragment identification syntax
   defined for "application/cbor-seq".)" `[analysis]` **Half the document's
   normative content points at a referent the same document declares not to
   exist**, and the three cases of the second `SHOULD` collapse to the third,
   since with no `+cbor-seq` rules every case is one "not defined in
   +cbor-seq". (`rfc-8742#R-0048`, `R-0055`–`R-0060`)
2. **§6.3's second `SHOULD` is miscategorised.** "The syntax and semantics for
   fragment identifiers for a specific "xxx/yyy+cbor-seq" SHOULD be processed as
   follows:" — what gets *processed* is a fragment identifier, not its syntax
   and semantics. The subject of the verb cannot be processed.
   (`rfc-8742#R-0057`)
3. **§6.1 cites a section that does not exist.** "Interoperability
   considerations: Described herein." No part of RFC 8742 is headed
   interoperability; the nearest content is §2's truncation paragraph and §4.3's
   skipping advice, neither so headed. (`rfc-8742#R-0049`)
4. **The two registrations of one format disagree.** §6.1's interoperability
   field reads "Described herein." and §6.3's reads "Interoperability
   considerations: n/a". (`rfc-8742#R-0049`, `rfc-8742#R-0061`)
5. **Three references are informative and are used normatively.** §6.3 registers
   "in accordance with [RFC6838]", §6.2 assigns "from the "Expert Review"
   (0-255) range ([RFC8126])", and §4.1 and §4.3 both depend on RFC 8610's
   `.cborseq` and `.cbor` control operators — and **`[RFC6838]`, `[RFC8126]` and
   `[RFC8610]` are all in §7.2, Informative References.** Meanwhile `[RFC7049]`,
   the **obsoleted** CBOR specification, is normative.
6. **Both stated gaps were marked temporary and neither has closed.**
   "Currently" (§4.1), "at this time" (§4.2), and "(Future versions of CDDL may
   provide a notation for top-level CBOR Sequences, e.g., by using a group as the
   top-level rule in a CDDL specification.)" (`rfc-8742#R-0032`) Six years on, no
   record in this library closes it; `[analysis]` CDDL's live extension point is
   the **control-operator registry** (RFC 9741 §4, RFC 9165), which is not where
   a top-level *subject* could be added, and `draft-ietf-cbor-cddl-modules` adds
   a module system rather than a start-symbol rule.

**Not a defect, recorded because it is easy to mistake for one.** §2 claims
CBOR items "are self delimiting and the end can always be calculated"
(`rfc-8742#R-0016`) and then concedes two paragraphs later that a malformed item
breaks exactly that. The claim is about well-formed items and is correct as
scoped; the scoping is just never stated in the sentence that makes the claim.

---

## 8. What this extraction confirmed, refuted and narrowed in `summary.md`

The summary was written first and reviewed; FX-1 forbids extracting *from* it, so
every claim below was re-derived from `.cache/rfc-8742.txt` at this pass.

**Confirmed, mechanically:**

- **Four BCP 14 keywords, at §3, §5 and §6.3 twice.** `bin/bcp14-count` →
  4 (MUST 1, SHOULD 3), and §2 contains none. ✔
- **§2 states the completeness hole three times**, and the three statements are
  `R-0013`, `R-0024` and `R-0009`/`R-0018`. ✔
- **§5's COSE sentence and its "additional effort" wording.** ✔ verbatim.
- **§6.1's "Magic number(s): N/A" and "File extension(s): N/A"**, and §6.1's
  dangling "Described herein." ✔
- **CoAP Content-Format 63 and CBOR tag 63 are different namespaces**, and the
  tag registry's row reads "Encoded CBOR Sequence RFC 8742" against
  `draft-bormann-cbor-notable-tags-02, Section 2.1`. ✔ verified against
  `records/iso/iana-cbor-tags/distilled/tables.yaml` at this pass.
- **§4.1's and §4.2's gaps, and the "Future versions of CDDL" parenthesis.** ✔
- **The normative anchor is [RFC7049] and the COSE reference is [RFC8152]**, with
  no `Updates:` line. ✔
- **§3's suffix test is not decidable.** ✔

**Narrowed, with the narrowing stated:**

- The summary says §4.3's wrapper "is tag 24's pattern with the tag removed".
  Confirmed as an analogy, and **narrowed**: the two are not interchangeable.
  Tag 24 wraps *one* item in a tagged byte string; §4.3 wraps *each element* in
  an **untagged** byte string, and `D-0010` shows the resulting failure mode —
  a corrupt byte-string head strands the tail — which tag 24 shares and which the
  summary does not mention.
- The summary's Cut 1 says "option 3's JSON lineage does not pay it the same way"
  because the marker makes "resynchronisation after a malformed item" possible.
  **Narrowed to `[unverified]`:** RFC 7464 and RFC 8091 are **not held in this
  library**, so neither the marker's identity nor the JSON side's recovery rule
  is citable from here. §2's one sentence — that CBOR Sequences "do not use a
  marker between items" — is the whole of the evidence, and it establishes the
  *absence* on the CBOR side rather than the *recovery* on the JSON side. The
  cut survives as Cut 4, re-aimed at **option 4** where the evidence actually
  lands, because option 4 is the option that must make the two behave alike.

**Refuted, and corrected here:**

- **`[correction]` The summary's Cut 2 says the schema-expressibility cost "is
  shared by option 2 and option 5 and paid by neither option 1 nor option 3: a
  canonical S-expression file and a JSON text sequence each have a grammar for
  the whole file." The option-1 half is right and now checkable; the option-3
  half is not supported by anything this library holds.** RFC 7464 is not a
  record here and no grammar of it is held, so "a JSON text sequence ... has a
  grammar for the whole file" is an assertion about an unread document. Cut 2
  above therefore claims option 1 on evidence (`rfc-9804`'s verbatim
  `canonical.abnf`, start symbol `c-sexp`) and claims option 3 only as far as
  the existence of RFC 7464 and RFC 8091, which §2 and the Acknowledgements name.
- **`[correction]` The summary says the summary-bar extraction "would be cheap —
  four BCP 14 keywords makes `requirements.yaml` a four-row file".** It is a
  **61-row** file. The four keywords are the least informative thing in the
  document; what had to be extracted is every definitional case of §2, every
  explicit absence of capability, and every registration field that carries a
  claim. The estimate was wrong by a factor of fifteen, and it is worth recording
  because the same estimate will be made again for the next thin-keyword RFC.
- **`[correction]` The summary says of the `examples/` absence that "there is
  nothing here to make a fixture from".** There is nothing *of the document's*
  — confirmed, zero hex octets — but **eleven fixtures were derivable** and are
  now in `examples/vectors.yaml`, marked `D-` and executed. The pair
  `D-0004`/`D-0006` is the record's sharpest artifact and it did not exist when
  the summary concluded there was nothing to build.

**Added at this pass, not in the summary:**

- Defects 1, 2, 4 and 5 of §7 above — the **vacuity** of two of the four
  keywords, the miscategorised `SHOULD`, the two registrations disagreeing, and
  three informative references used normatively.
- The **lower-case `must`** finding: the one sentence that states how to decode
  the format carries no BCP 14 force (`R-0019`), and neither does "decoders must
  operate on input that is assumed to be untrusted" (`R-0043`), which sits
  immediately before the document's only uppercase `MUST`.
- **Cut 3** in full — option 1's grammar detects the truncation and its atoms
  are length-prefixed by construction. Both halves come from grammars this
  library already holds verbatim and neither was in the summary.
- `state-machine.yaml`, which the summary did not anticipate: the completeness
  hole stated as an **indistinguishability between two states**.

---

## 9. Open questions this record raises

1. **Does a statement log get §4.3's byte-string wrapper, and does a signed
   export get §2's array?** §2.1, §2.2 and the §5.2 table answer both with
   "yes", and the answer costs one array head and one byte-string head per
   entry. It needs a `DECISIONS-0001` row and a sentence in the export profile,
   not an ADR.
2. **What binds the count and the order of a signed bundle?** §1 and §3.2. The
   candidates are an array head (free, and `R-O-05`-compatible), a hash chain
   (append-friendly, and the only one that survives truncation), or a signed
   root. **This is the question `library#39` should route to whoever owns
   `R-I-03`**, and RFC 8742 contributes the problem and no mechanism.
3. **Is the empty-sequence ambiguity a condition (7)?** §5.3's condition-(1)
   row. `canonical-encoding`'s six conditions are all about *values*; `D-0001`
   and `D-0005` are one encoding with two meanings at the *file* level, and no
   condition covers it. If the answer is yes, it belongs on the topic rather
   than on this record.
4. **If we register a media type, does §3's suffix test let us use
   `+cbor-seq`?** §4. Undecidable as written. The practical answer is to register
   `+cbor-seq` and say in our own registration what "at least sometimes" means
   for us — which is inventing the test the RFC omitted, and under `R-O-03` must
   be declared as ours.
5. **Does the ADR need to say that `application/cbor-seq` has no magic number?**
   §5.3's condition-(4) row and `rfc-9277`'s record. `rfc-9277` makes one
   *constructible* for exactly this media type — `TN(63) = 1668546880 =
   0x63740140`, label `d9d9f8 da63740140 43 424f52`, arithmetic checked at this
   pass — and carries no `Updates: 8742`, so the registration a reader consults
   and the RFC that makes its magic number derivable disagree. Under a no-tags
   rule we cannot use it anyway; the question is whether the ADR says so out
   loud.

---

## 10. Provenance: what was verified in-library at this pass

Pass 1 read **only** `.cache/rfc-8742.txt` for every claim about RFC 8742 — never
`summary.md`, never another agent's output. Mechanically re-derived from the
cache: the BCP 14 count (4 in the source, 4 across the requirement texts, 4
stated / 57 inferred); 61 of 61 requirement texts and 63 of 63 normative spans
contiguous in the whitespace-normalised source with **both ends inside their
locator's section** (0 failures); 6 of 6 schema regions byte-identical to their
declared line ranges with all 6 declared digests verifying and **none** matching
the with-trailing-newline variant; 3 of 3 dedent round-trips; 5 of 5 source
vectors exact dedented slices; 11 of 11 derived fixtures executed; 112 quoted
spans across the YAML artifacts checked verbatim, **which caught one elided
quote in `examples/vectors.yaml` and two inexact ones in `messages.yaml`, all
three corrected in place**; 0 form feeds, 0 page footers, 0 lines with trailing
whitespace, 0 asides, 0 healed hyphenations; and the join in `messages.yaml`
recomputed as 31 cited / 30 uncited after a first draft that counted prose
mentions as cites and was wrong by 12.

**Verified present and quoted in-library:**
`records/iso/iana-cbor-tags/distilled/tables.yaml` (tag 63, and tags
55799/55800/55801 for the sibling record);
`records/ietf/rfc-8949/distilled/schema/cbor-head.derived.abnf` and its design
notes' §3.4.6 row; `records/ietf/rfc-9804/distilled/schema/canonical.abnf` and
`advanced-transport.abnf`; `topics/canonical-encoding.yaml`;
`records/ietf/rfc-8610`, `rfc-9741`, `rfc-9682`.

**Not held in this library, so every claim about them is `[unverified]` here:**
`ARCH-0001`, `ARCH-0002`, `ADR-0001`, `MD-3`, `PLAN-0001`, `DECISIONS-0001`, all
`R-M-*` / `R-O-*` / `R-I-*` texts, **RFC 7049**, **RFC 7464**, **RFC 8091**,
**RFC 6838**, **RFC 8126** and **RFC 7252**. Of these, RFC 7464's marker and
RFC 7252 §12.3's experimental range are the two that a later pass could usefully
close by ingesting them.

**No `reviewed_by` is signed, and no `profile` is declared.** Passes 2 and 3 have
not run.
