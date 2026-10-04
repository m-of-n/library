---
record: rfc-9804
kind: design-notes
title: "rfc-9804 — bearing on our design"
extracted: "2026-10-04"
reviewed_by: ""
---

# RFC 9804 — bearing on our design

RFC 9804 is **DEC-002 option 1**: *"Canonical S-expressions (RFC 9804) as
canonical; JSON as diagnostic"* (ARCH-0001 §8, DEC-002). ARCH-0001 §3.1 already
records that it *"restates canonical S-expressions as a living encoding option.
It is **not** selected here (see DEC-002)."*

The `canonical-encoding` topic answer of 2026-10-03 names this record as the one
remaining blocker: *"RFC 9804 is still queued, which is the one remaining
blocker, since option 1 cannot be fairly scored against the six conditions until
it is extracted."* Scoring option 1 against those six conditions is therefore the
job of this file, and §1 below does it.

**Nothing here decides DEC-002.** DEC-002 is open, and a DEC is accepted only in
an `ADR-NNNN` file with a changelog line and a status update in ARCH-0001. What
follows is evidence for that decision, assembled from the source and cited to it.

---

## 1. Option 1 against the six conditions

The six conditions are the `canonical-encoding` topic answer's, in its own
numbering. Group A (1–4) is *safe to sign*; group B (5–6) is *safe to derive an
identifier from*.

| # | Condition | RFC 9804 | Basis |
|---|---|---|---|
| 1 | Encoding is **injective** over the values encoded | **Yes at its own layer, with one crack** | R-0051, R-0052; crack at R-0037/R-0039 |
| 2 | Decoder **rejects** non-canonical input rather than normalising | **Mechanism yes, obligation no** | R-0056, R-0057 give a separate grammar; no requirement anywhere states rejection |
| 3 | Canonicalisation runs once at authoring, **never at verification** | **Compatible — the document is silent** | §10 in full; R-0064 |
| 4 | Encoding profile named by an **authenticated type indicator** in the signed bytes | **Not supplied** | R-0066; §4.6 forbids pressing the display-hint into this role |
| 5 | Set-valued fields in arrays have a **defined canonical order** | **Not supplied, and silent rather than prohibiting** | R-0003, R-0052 |
| 6 | Load-bearing text has a declared **Unicode normalisation** rule or an explicit refusal | **No rule, but no place for a normaliser to hide** | R-0032, R-0041 |

Condition by condition.

### Condition 1 — injectivity

§6.2 asserts it directly: *"It is uniquely defined for each S-expression"*
(R-0051). The mechanism is subtraction, not algorithm. The canonical form takes
each octet-string *"in verbatim mode"* and each list *"with no blanks separating
elements from each other or from the surrounding parentheses"* (R-0052), which
collapses the five octet-string representations of §4 to one and deletes every
optional length prefix, every ignorable-whitespace allowance and every padding
choice at a stroke.

**This is worth stating precisely, because it is option 1's strongest property.**
There is no sorting step, no normalisation step and no number algorithm in the
canonical form — uniqueness falls out of the grammar admitting exactly one
spelling per value, not out of a procedure an implementation must execute
correctly. Compare the other candidates: RFC 8785's uniqueness depends on the
ECMAScript `Number::toString` algorithm, which §3.2.2.3 does not even include
(*"Due to the relative complexity of this part, the algorithm itself is not
included in this document"*), and on a UTF-16 code-unit sort; RFC 8949 §4.2's
determinism depends on encoder-side rules about integer head length, map key
order and float shortening. RFC 9804's canonical form depends on a grammar of
two productions (R-0056, R-0057). It is the smallest attack surface of the three
by a wide margin.

**The crack, and it is on the identity path.** §4.6 says an octet-string
carrying no display-hint *"may be considered to have a media type [RFC2046]
specified by the application or use"*, defaulting to `[application/octet-stream]`
(R-0037). §4.6 then says the default is neither written out nor stripped: *"If a
display-hint is the default, it is not suppressed nor is the default display-hint
included in the representation for an octet-string without a display-hint"*
(R-0039). And §4.7 makes the hint part of equality: two octet-strings are
equivalent *"if and only if they have the same display-hint and the same data
octet-strings"* (R-0040).

Put together: an octet-string written with an explicit
`[24:application/octet-stream]` hint and the same octet-string written with no
hint are, to an application applying the default, the *same value* — and they
have **different canonical forms**, hence different digests. Injectivity in the
direction that matters for signing (one encoding, one value) holds. Injectivity
in the direction that matters for naming (one value, one encoding) does **not**,
unless a profile forbids writing the default explicitly.

This is the asymmetry the topic answer already names — *"a sort or normalisation
divergence fails LOUDLY when signing, as a signature mismatch, and SILENTLY when
deriving an identifier, where it yields a confidently wrong name"* — reappearing
in option 1 from a different cause. It is cheap to close (one profile rule: never
write a hint that equals the profile default), but it must be closed explicitly,
and the source does not close it. §10 names the same mechanism as the document's
one real security consideration (R-0065).

### Condition 2 — rejection of non-canonical input

**The mechanism is there and it is better than any other candidate's.** §7.2
gives the canonical form its **own grammar**, separate from the advanced one:

```abnf
c-sexp         =  c-string / ("(" *c-sexp ")")
c-string       =  [ "[" verbatim "]" ] verbatim
```

Two productions (R-0056, R-0057). A decoder that implements `c-sexp` and not
`sexp` rejects non-canonical input *by construction*: it is not normalising and
then comparing, it is simply failing to parse. Every octet-string is
length-prefixed and verbatim, so the check is single-pass, left-to-right, with no
lookahead and **no re-encoding**.

That bears directly on the topic's stated open experiment: *"If checking
canonicality on decode cannot be done without re-encoding, then condition (2)
drags the canonicaliser of the producer back into the verifier, the R-O-05
separation is cosmetic, and DSSE is simply right."* For option 1 the answer is
visibly yes, it can — the canonical grammar is context-free, and recognising it
costs one pass. For CBOR the same question is still open against the `rcbor`
spike, which has an encoder and no decoder. **Option 1 is the only DEC-002
candidate for which condition (2) is demonstrably reachable from the cited
document alone**, because it is the only one whose canonical form is published as
a grammar rather than as a set of encoder-side rules.

**The obligation is absent, and that is a real gap.** Nothing in RFC 9804
requires a decoder to reject non-canonical input. §6 requires an implementation
to support *both*: *"The first two MUST be supported by any implementation"*
(R-0045), the first two being canonical and basic transport. §6.3 makes basic
transport an alternation — the canonical octets, or the brace-wrapped base-64 of
them (R-0054, R-0058). So a conforming implementation **must** accept
`{KDE6YTE6YjE6Yyk=}` wherever it accepts `(1:a1:b1:c)`, and the document never
says which to use when, nor that a verifier should refuse the wrapped form. The
basic transport representation is therefore **not** uniquely defined for a given
S-expression; only the canonical form is, and R-0051 claims uniqueness for the
canonical form alone.

Condition (2) is thus available to a profile that states it, and is not supplied
by the document. That is the same shape as the topic's finding for ARCH-0002 P5,
and it routes to P5 the same way.

### Condition 3 — no canonicalisation during verification

**Compatible, and this is where option 1 differs most sharply from option 3.**
§10 is the entire security considerations section, and it imposes **no**
verification ordering:

> As a pure data representation format, there are few security considerations to
> S-expressions. A canonical form is required for the consistent creation and
> verification of digital signatures. This is provided in Section 6.2.

R-0064 is the whole of it: the canonical form is what gets signed and verified.
There is no instruction to parse first, no instruction to locate a signature
inside the payload, no re-serialise-and-compare scheme, and no BCP 14 keyword
anywhere in §10.

Contrast RFC 8785 §5, which **mandates** the ordering R-O-05 forbids — parse and
check I-JSON, verify correctness and locate the signature property, *then* verify
the signature — and Appendix F, which spells out remove-the-signature-property
and re-canonicalise. That contradiction is the second of the four grounds the
topic gives for withdrawing option 3. **Option 1 does not have it.** The document
is silent, and on an ordering question silence is permission.

Note the vocabulary coincidence and do not lean on it: R-O-05 says the signed
payload is the canonical encoding *"verbatim"*, and *verbatim* is also RFC 9804's
own name for its length-prefixed octet-string form (§4.1). The two uses are
unrelated. The substantive point is the §10 silence, not the shared word.

### Condition 4 — authenticated type indicator

**Not supplied, and the obvious substitute is explicitly disqualified.** §11
reads in full *"This document has no IANA actions"* (R-0066). There is no
version field, no profile identifier, no media type, no magic number and no
envelope anywhere in the format.

The tempting move is to use the display-hint as the type indicator — it is the
only modifier an octet-string can carry, it is carried inside the canonical bytes
(R-0038), and it is part of equality (R-0040). **§4.6 forecloses it:** *"The
purpose of a display-hint is to provide information on how to display an
octet-string to a user. It has no other function."* A profile that made the hint
load-bearing for type would be using a field against its specified meaning, which
is exactly the kind of silent reinterpretation R-O-03 exists to prevent. Record
this as a trap, because it will be proposed.

What is left is to build the indicator ourselves, as a convention inside the
S-expression — conventionally a distinguished first element of the outer list.
That is *constructible without any registry*, because a list element is just an
octet-string and there is no tag space, header space or registry to negotiate
with. Under R-M-12 and ADR-0001 the indicator must be key-relative, and an
octet-string first element accommodates that directly.

### Condition 5 — canonical order for set-valued fields

**Not supplied.** A list *"is a finite sequence of zero or more simpler
S-expressions"* (R-0003), the canonical form preserves whatever order the author
wrote (R-0052 adds no sorting step), and there are no maps in the data model at
all — so there is not even a map-key-ordering rule to borrow, as RFC 8949 §4.2.1
supplies.

**But it is silent, not prohibiting, and under R-O-03 that distinction decides
the question.** The topic's first and strongest ground for withdrawing option 3
is precisely this: *"RFC 8949 is SILENT on array order, so a profile may add a
bytewise rule without contradicting it, whereas RFC 8785 PROHIBITS reordering.
...  Prohibited versus absent is the decisive distinction."* I read §§2–8 for any
rule against reordering list elements and there is none — the nearest thing is
the §8 list of restrictions an application *might* adopt (no empty lists, no
lists having another list as a first element, and so on), which is a menu of
further restrictions, not a prohibition on adding one.

So on condition (5), **option 1 stands exactly where option 5 stands and not
where option 3 stands**: the rule we need is an addition to a silent
specification, which R-O-03 permits as a cited profile, rather than a
modification of a prohibiting one, which R-O-03 does not.

### Condition 6 — Unicode normalisation

**No rule, and the structural reason is more interesting than the absence.**
§4.6 RECOMMENDS UTF-8 for text (R-0032) and says nothing about normalisation
form. §4.7 makes comparison byte-exact and case-sensitive (R-0041).

That is the same position as RFC 8949, and the topic already records what it
leaves open: normalise-at-authoring plus reject-at-decode. But option 1 has a
property neither JSON nor CBOR has. **RFC 9804 has no text type.** An
octet-string is octets (R-0001); whether it *"consists of text"* is an
application claim the format never inspects, which is why R-0032 is only
`testable: partial`. A conforming parser reads a decimal length, a colon, and
that many raw octets, and has no reason — and under R-0010, *"No escape sequences
are interpreted in the octet-string"*, no licence — to touch a byte.

That matters because the topic's documented incident was a *silent normalising
layer* inside a JSON string pipeline: *"Transcribing this record's own test
vectors corrupted U+FB33 HEBREW LETTER DALET WITH DAGESH, which has a canonical
decomposition that an ordinary normalising layer applies silently. Any JCS
pipeline containing such a layer breaks signatures on exactly that input."* In a
canonical S-expression pipeline there is no string-processing stage for such a
layer to inhabit. The hazard is not *ruled out* — an application can still hand
the encoder differently-normalised bytes — but it is pushed up to the
application boundary, where it is visible, instead of hiding in the serialiser.

RFC 8785 is still the only candidate that states a rule at all (*preserve Unicode
string data as is*), and the topic already discounts that as binding parties we
do not control.

---

## 2. What we adopt

1. **The canonical/advanced split as an architectural pattern, not just an
   encoding detail.** §6.2 defines a form *"used for digital signature purposes"*
   that *"is not particularly readable, but that is not the point"*, and §6.4
   defines a separate advanced form *"intended to provide more flexible and
   readable notations for documentation, design, debugging, and (in some cases)
   user interface"* (R-0055). Two forms, different jobs, and **no requirement
   anywhere that a verifier convert between them**. That is R-O-05's
   *"Any human-facing form is regenerated from already-verified bytes"* with the
   priority already set the right way round, in a 1997 design. It is also the
   ancestor of R-O-05 in a literal sense, and this record is the citation for
   that claim.

2. **Uniqueness by grammar rather than by algorithm.** Condition (1) above. The
   canonical form is two ABNF productions; there is no procedure to get wrong.
   Whatever DEC-002 decides, *"can the canonical form be stated as a grammar
   rather than as a list of encoder obligations?"* is now a question worth asking
   of the winning option, because one candidate demonstrably answers yes.

3. **Length-prefixed, escape-free framing.** The verbatim form (R-0008, R-0009,
   R-0010) is self-delimiting with no escaping, no terminator and no lookahead.
   The §6.2 example `10:foo)]}>bar` is the one to keep as a fixture: the payload
   contains a close parenthesis, a close bracket, a close brace and a
   greater-than, and none needs escaping or can terminate anything early. A
   format with no escaping has no escaping bugs.

## 3. What we adapt, and how

1. **Condition (2) as a profile rule, routed to ARCH-0002 P5.** Adopt the §7.2
   canonical grammar as the *only* accepted decode grammar for signed bytes, and
   reject the §6.3 brace-wrapped alternative and everything in §7.1 outright.
   This contradicts nothing in RFC 9804 — R-0045 obliges an *implementation of
   RFC 9804* to support both forms, and a profile that narrows what it will
   accept as a signed payload is making a restriction of exactly the kind §8
   anticipates. It does mean a conforming m-of-n verifier is **not** a conforming
   RFC 9804 implementation, and that should be said out loud rather than
   discovered.

2. **A type-indicator convention, built not borrowed.** Condition (4). A
   distinguished first element of the outer list, key-relative per R-M-12 and
   ADR-0001. Explicitly **not** the display-hint (§4.6).

3. **A profile rule closing the default-display-hint crack.** Condition (1).
   Either forbid display-hints entirely in the native model — §8 lists *"no
   display-hints"* as a restriction applications may adopt, so this is a
   sanctioned restriction, not an invention — or require that a hint equal to the
   profile default is never written. Forbidding them outright is cleaner and
   costs nothing we currently need, since the display-hint carries no semantics
   by §4.6's own statement.

4. **A canonical order rule for set-valued fields.** Condition (5), as an
   addition to a silent spec. The same rule that ARCH-0001 §4.1 `Threshold`
   members, DEC-004 tag value sets and ARCH-0002 P4 schema sets need under any
   DEC-002 option; nothing about it is S-expression-specific, which is itself
   worth noting — **condition (5) is not a discriminator between DEC-002
   options.** All of them are silent on it except option 3, which prohibits it.

## 4. What we reject, and why

1. **The advanced transport representation, as anything other than display.**
   §8: *"advanced representation can only be used in applications that mandate
   its support or where a capability discovery mechanism indicates support"*
   (R-0060) — and RFC 9804 defines **no capability discovery mechanism**, so a
   sender has no in-band way to learn whether a receiver supports it. Optional
   (R-0046), undiscoverable, and strictly larger than what we need.

2. **The display-hint as a type indicator.** §4.6, *"It has no other function."*
   See condition (4).

3. **The base-64 brace wrapper (§6.1) in the native model.** Its purpose is
   channel robustness — §6.3 cites channels sensitive to NULL or DEL octets or to
   line length — which is a 1997 email-transport concern we do not have. Keeping
   it would mean two accepted encodings for one S-expression and would forfeit
   condition (2) at the point where it is cheapest to hold.

4. **The §9 in-memory layouts, as anything normative.** §9 says they are *"only
   sketched here, as they are only suggestive"*, and R-0063 confirms the wire
   forms do not depend on the implementation's chosen width `k`. They are in
   `messages.yaml` marked `normative_status: suggestive` because §9.2 prints
   exact bytes, and for no other reason.

5. **Optional-padding leniency on input.** R-0029 and R-0048 permit a parser to
   accept base-64 with equals signs dropped. A permission that two conforming
   parsers may answer differently is a disagreement about whether a given input
   is well formed. Moot in the native model once §6.1 is rejected, but it must
   stay rejected rather than merely unused.

## 5. Mapping to our decisions

| Ours | What RFC 9804 contributes |
|---|---|
| **DEC-002 option 1** | This is the option. Scored against all six conditions in §1. Not decided here. |
| **DEC-003** (issuer/subject identifiers on the wire) | `bears_on` in the record. The format supplies **no** key or digest encoding — a `KeyId` is *"Digest of a canonical key encoding"* (ARCH-0001 §4.1) and RFC 9804 defines no canonical key bytes. The `rcbor` `keyid()` defect the topic records — hashing key bytes with no canonical encoding step — is **not** repaired by choosing option 1. It is an open DEC-003 problem under every option. |
| **R-M-02** (*a principal MAY be identified solely by key or key digest*) | Uniqueness becomes a **naming** requirement, not only a signature one. Condition (1)'s display-hint crack is an R-M-02 hazard specifically: it yields two names for one principal, silently. |
| **R-O-03** (*canonicalization algorithm SHALL be cited, not invented silently*) | Strong for option 1. The whole canonical form is two ABNF productions in a current IETF RFC, complete in itself — no companion standard, no implementation to cite, no annually revised edition. Contrast the topic's finding that citing RFC 8785 means citing three artifacts. The additions we need (conditions 2, 4, 5) are additions to a **silent** spec, which R-O-03 permits as a cited profile. |
| **R-O-05** (*sign the bytes; no canonicalization during verification*) | **Compatible, uniquely among the scored candidates.** §10 imposes no verification ordering (condition 3). The §6.2/§6.4 split is R-O-05's authoring/display separation stated as format structure. This record is the citation for ARCH-0001 §3.1's claim that RFC 9804 is a living option. |
| **R-M-12 / ADR-0001** (key-relative extension points) | Satisfied trivially and for an unusual reason: there are **no** extension points to make key-relative. No tag space, no header space, no registry, `"This document has no IANA actions"` (R-0066). P1's displacement of type identity is a no-op here, exactly as the topic records it is for JSON — but *without* option 3's §5 ordering mandate. |
| **ARCH-0002 P4** (schema set serialised so it can be repeatably hashed) | Needs condition (5), which RFC 9804 does not supply but does not prohibit. Conditional on P4 surviving; DECISIONS-0001 T1-B currently recommends holding it. |
| **ARCH-0002 P5** (validity checked, unknown rejected) | The natural home for condition (2) under option 1, as it is under option 5. The §7.2 grammar makes the extension cheap: rejection is parse failure. |
| **D-3** (*reduced CBOR, no IANA tags, COSE export only*) | **Does not apply to this record, and the reason is the finding.** The `extract` skill requires a header-by-header D-3 mapping *for COSE/CBOR/envelope documents*. RFC 9804 is none of the three: it defines no envelope, no headers and no tags, and it is not CBOR. There is nothing to map header-by-header because there are no headers. What D-3 constructs by subtraction — registry-freedom via a positive rule excluding major type 6, decoder rejection, and a named untagged export profile — RFC 9804 has by construction. If DEC-002 resolved to option 1, D-3 would have no subject. |
| **R-I-03 / interchange** | Untouched. Option 1 is a *native* encoding choice; COSE_Sign1 and DSSE remain the export targets under any option, and the topic's finding that DSSE's `(t, n)` envelope already carries threshold semantics for R-M-06 is unaffected. |

### Where this leaves the scoring

Stated as evidence, not as a decision.

The topic's four grounds for withdrawing option 3 were: (i) condition (5) is
*prohibited* by RFC 8785, not merely absent; (ii) §5 mandates the ordering R-O-05
forbids; (iii) the number algorithm is not in the cited document; (iv) the named
envelope reintroduces a global type identifier excluded by R-M-12.

**Option 1 is on the right side of all four.** (i) silent, not prohibiting;
(ii) §10 is silent on ordering; (iii) the canonical form is two productions in
the cited document, with no number algorithm because there are no numbers;
(iv) no envelope and no registry at all.

And the single criterion the topic records as option 3's outright win —
namespace governance, *"registry-free by construction"*, the criterion the v0.2.0
proposal §3.3 says was never scored — **option 1 also wins, by the same
argument**: no tag space, no header space, no IANA actions. The difference is
that option 3 buys it at the cost of §5, and option 1 does not pay that cost.

Two things stop this from being a conclusion. First, **option 1's data model is
far poorer than CBOR's or JSON's** — octet-strings and lists, no integers, no
maps, no booleans, no null (R-0001, R-0003). Every logical type in ARCH-0001 §4
would need an application-level mapping onto nested lists of octet-strings, and
that mapping is where injectivity would have to be re-established by hand, field
by field, with no help from the format. Option 1 moves the hard part rather than
removing it; §1's praise for the canonical form's small attack surface is a claim
about the *encoding layer only*. Second, the drivers DEC-002 actually names
include **library availability**, and the implementations in Appendix A are a
short list serving GnuPG and RNP (`record.yaml` `implementations`), against
ubiquitous CBOR and JSON tooling. Neither point is settled here.

## 6. Open questions

1. **Does the ARCH-0001 §4 type model survive the mapping onto
   octet-strings-and-lists without losing injectivity?** This is the question
   option 1 lives or dies on, and it cannot be answered from RFC 9804, because
   the format defines no integers, no maps and no booleans to map onto. A spike
   encoding `NameCert`, `AuthzCert` and a threshold-subject `ArtifactStatement`
   as canonical S-expressions — the acceptance test DEC-002 already names — would
   answer it. Until then §1's condition-1 verdict applies to the encoding layer
   only.

2. **Is the default-display-hint ambiguity (condition 1's crack) real for our
   data, or removed by forbidding hints?** §8 sanctions *"no display-hints"* as a
   restriction. If we take it, the crack closes and R-0037/R-0039/R-0040 become
   moot. Is there any construct in ARCH-0001 §4 that wants a display-hint? None
   is apparent, but this should be checked before the restriction is written down
   as costless.

3. **Does single-pass canonicality checking actually hold under the §7.2
   grammar, implemented?** §1 argues it does from the grammar's shape. The topic
   names the equivalent question for CBOR as the experiment that settles
   condition (2). A reader of `c-sexp` is maybe fifty lines; writing it is the
   cheapest way to turn this argument into evidence, and it would settle the
   question for option 1 ahead of option 5.

4. **How does a canonical S-expression reach COSE_Sign1 or DSSE at the
   interchange boundary?** As an opaque octet-string payload with a `payloadType`
   naming the profile, presumably — but `payloadType` is a media type or URI,
   which the topic records as R-M-12-non-conformant when it appears in option 3.
   Does the same objection bite option 1 at the export boundary? ARCH-0001
   §3.2's position that interchange identifiers are exempt may already answer
   this; it should be confirmed rather than assumed.

5. **Source defect — grammatical number in §10.** R-0065 reads *"those untyped
   octet-string may be treated as if they had a different display-hint"*:
   singular *octet-string* after *those*, where §4.6 and the rest of §10 use the
   plural. Transcription-level, no effect on meaning, recorded because the
   extraction is verbatim and a reader diffing against the RFC will hit it. Not
   worth an erratum.

6. **Source observation — the §7.2 canonical grammar is not self-contained.**
   `c-string` references `verbatim`, defined only in §7.1, which pulls in
   `decimal` and the `OCTET` core rule. An ABNF tool fed §7.2 alone reports
   `verbatim` undefined. This is the RFC's own structure — §7 says the canonical
   and basic forms are *"derived therefrom"* — and `schema/canonical.abnf`
   records it without repairing it. It matters for us only if we cite §7.2 as the
   normative grammar for signed bytes, which §3 item 1 proposes: the citation
   must be *§7.2 together with the `verbatim`, `decimal` and `OCTET` rules it
   depends on*, not §7.2 alone.
