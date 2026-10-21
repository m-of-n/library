---
record: rfc-8742
kind: index
title: "rfc-8742 — distilled artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

**State: all three machine passes have run (extract, verify, cross-check).
`distillation.standard: FX-1` and NO `profile`.** Two deliberate omissions, both
the lane's to close rather than pass 3's: `record.yaml` `distillation.passes`
still records **two** entries, because the cross-check pass was scoped not to
write its own, and no `profile` is declared. **No `reviewed_by` is signed** on
any artifact either, so these files are readable and citable but not
buildable-on. Read the 2-entry `passes` list against this paragraph, not
instead of it.

Pass 3 (2026-10-21, cross-check) closed the four closures and found **twenty**
defects and stale claims, every one in this record's own prose and every one marked
`[cross-check]` where it stands. The three that change what a reader should
believe: the **overturned vacuity claim survived in six places** pass 2 did not
reach (`record.yaml`, three `requirements.yaml` `field`s, two `messages.yaml`
notes); `summary.md` **still said this record had no `distilled/` and no
`distillation` block**; and two schema files cited **`V-0004`/`V-0005` for the
two byte strings**, which are `D-0003`/`D-0002` — bare ids in a namespace
`bin/check-id-joins` does not scan. Measured at pass 3: 6 of 6 schema regions
byte-identical and digest-verified under the stated convention and under none of
the alternatives; 61 of 61 requirement texts and 65 of 65 `normative.md` spans
contiguous in the raw whitespace-normalised source *and* inside their attributed
locator; `bin/bcp14-count` 4, extracted 4, all four in the four `stated` entries
and no fifth smuggled into any `text`; 7 of 7 state-machine triggers named
events with a source quote and a resolving id; 11 of 11 derived fixtures
reproduced by an independent decoder.

Pass 2 (2026-10-20, adversarial, did not extract) re-derived every count and
re-ran the id-join audit: **zero wrong ids** — this record has no
two requirements with the same text, so there is nowhere for a wrong id to hide,
which is exactly the structural property its sibling lacks. *(`[cross-check]`
2026-10-21, pass 3: pass 2 put the denominator at **243 citations**, and that
number is reachable by no counting rule pass 3 could construct.
`bin/check-id-joins --resolve` reported **344 citations, 0 dangling** on the
record as pass 3 received it — 260 distinct `(file, id)` pairs, and 555 once the
bare and `D-` spellings the tool does not scan are included, still 0 dangling.
It reads **352** now, because pass 3's own `[cross-check]` notes cite ids as
well; the figure is stated with its measurement point so a later pass can tell a
fossil from a lie. "Zero wrong" stands for everything the tool scans.)* It
made **five**
corrections, each marked `[correction]` where it stands:
`messages.yaml`'s header comment said 44/17 against its own 31/30; a
re-quotation in `design-notes.md` had a capital the source does not have; the
**vacuity claim about §6.3's two `SHOULD`s is overturned** (see *Read this
before using anything here*); `state-machine.yaml`'s headline
indistinguishability claim is withdrawn; and Cut 3's option-1 ground is narrowed.
It also found **two statements with no requirement entry**, now in `normative.md`
marked `no id`. `requirements.yaml` `verify_pass` is the index.

Source: RFC 8742, *Concise Binary Object Representation (CBOR) Sequences*,
Standards Track, February 2020. sha256
`4462966836b60f42ebae9b5f1d2a479c328e16f0380a3434311a083bccbce30e`, 462 lines,
18421 bytes (line 1 is a UTF-8 BOM alone, part of the hashed bytes and part of
no span). **No form feeds, no page footers, no trailing whitespace on any
line, no asides** — so there is no page decoration to remove, and every one of
the 61 requirement texts and 65 `normative.md` spans resolves against the
**raw** whitespace-normalised source with no transformation at all.

*(`[cross-check]` 2026-10-21, pass 3: that claim used to run "so no
transformation of any kind was applied to **any quoted span**", which is a
blanket and `hazards.md` says to state the rule actually kept. Two places in the
record do transform, both declared where they stand and neither a quotation of
the source: `schema/cddl-fragments-dedented.derived.cddl` removes the RFC's
three-space margin — `.derived.`, and the removal round-trips, re-checked at
pass 3 — and `messages.yaml`'s `structured-syntax-suffix-registration` `Contact`
**value** states the joined form `IESG-designated`, marked OURS, where source
lines 373/374 break at the hyphen. `schema/registrations.txt` carries that break
unhealed and `normative.md` quotes the region verbatim. The rule kept is: **no
span presented as the source's words is healed, dedented or elided silently.**)*

## The answer this record was extracted for

**Can a CBOR Sequence state how many items it should contain, or report that it
is complete? No — and §2 says so three separate times.** "There is no
end-of-sequence indicator."; the format "can reliably detect truncation of the
bytes making up the last CBOR data item in the sequence, but it cannot detect
entirely missing CBOR data items at the end."; and "an empty (zero-length)
sequence of bytes" is itself a valid sequence.

So **truncating an append-only log at an item boundary is in spec and
undetectable**, and a log truncated to nothing is a valid empty log. The three
fixtures are `examples/vectors.yaml` `D-0004`, `D-0005` and `D-0001` — and
`D-0001` and `D-0005` are deliberately **the same bytes**, because that is the
finding. `messages.yaml`'s `cbor-sequence.completeness` states it in prose with
the same three quotations, and `state-machine.yaml` restates it as an
**indistinguishability between two files** — *not* between two states: a complete
log and one truncated at an item boundary are **both**
`input-exhausted-at-boundary`, one state and two files. *(`[correction]`
2026-10-20, pass 2: this read "an indistinguishability between two **states**",
which is what `state-machine.yaml`'s own header claimed and what its
`indistinguishable_pairs` block does not say.)*

And §5 closes the escape route rather than opening one: per-element COSE does
not bind "the relationship of the elements in the sequence", with "additional
effort may be required" as the whole of the guidance. `design-notes.md` §1 and
§3.2 carry the argument and the one-sentence fix.

## Read this before using anything here

RFC 8742 carries exactly **four** all-capitals BCP 14 occurrences in 18 KB, and
**§2 — the entire format — contains none of them.** **One** of the four is
**unsatisfiable at publication by the document's own admission, as a deferral**:
§6.3's first `SHOULD` points at a fragment-identifier syntax §6.1 registers as
N/A and §6.3 itself calls absent — the parenthesis opens "(At the time of
publication of this document, …" — so it binds if and when one is registered. And the document uses
**lower-case `must`** for the one sentence that states how to decode the format,
which §1.1's own clause excludes from BCP 14 force.

*(`[correction]` 2026-10-20, pass 2: this paragraph read "**Two** of the four
are **vacuous** at publication", and that claim — which this record made in six
places and built a headline on — **is overturned**. §6.3's *second* `SHOULD`
(`rfc-8742#R-0057`) is not vacuous at all: its three cases collapse onto
`rfc-8742#R-0060`, "For cases not defined in +cbor-seq, process as specified in
"xxx/yyy+cbor-seq"", which with no `+cbor-seq` rules is **universal and
determinate at publication** — the only one of the four keywords with an
applicable effect on the day the RFC shipped. Pass 1 noted that collapse itself,
in the same sentence as the vacuity claim. And calling the *first* `SHOULD`
vacuous rather than deferred needs a premise about what an RFC 6838 registration
may legitimately defer to; **RFC 6838 is not a record in this library and is not
cached**, so that premise is unverifiable from here. `design-notes.md` §7 defect
1 carries the argument and the replacement defect: §6.1 and §6.3 register
**contradictory** fragment-identifier dispositions for the same format, and §6.3
does not reconcile them.)*

That is expected and correct for a format defined by a recursive definition:
this document is normative by its **definitional cases and its decoding rule**,
not by obligations laid on an actor. **57 of the 61 requirements here are
`kind: inferred`**, each naming in `field` the phrase, definitional case,
explicit absence or registration field value that carries the force. The
precedents are `rfc-8610` (2 keywords in 125 KB, 137 of 139 inferred),
`rfc-9741` (3 in 28 KB, 58 of 61) and `rfc-9682` (0 keywords).

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | **65** verbatim spans across 12 locator labels — the 11 sections (§1, §1.1, §2, §3, §4.1–§4.3, §5, §6.1–§6.3) plus the Abstract's first half — with all 3 CDDL fragments, both §4.2 instances, Table 1 and both IANA registration templates reproduced in fenced blocks with their source line ranges. All 65 confirmed contiguous substrings of the whitespace-normalised source **and** confirmed to start and end inside their locator's section, 0 failures; 61 carry a primary `R-` id, strictly ascending and each labelled exactly once, and the other 4 are the Abstract fragment, §1.1's boilerplate and the two `no id` bullets. *(`[cross-check]` 2026-10-21, pass 3: this row said **63**, twice. 63 was pass 1's true count; pass 2 added the two `no id` bullets the same row goes on to advertise and never carried the arithmetic — the fossil class `hazards.md` §6 names, created by a correct earlier pass.)* **No transformation applied**: no form feeds, no page footers, no asides, no dedent, no healed hyphenation. Three hyphenation breaks exist in the source and **none** falls inside a quoted span — all re-verified at pass 2, where all 61 requirement texts resolve against the **raw** source with no transformation of any kind, and the word-break census reproduces at 3 (2 in the body, 1 in the references, none in a span). **Two statements pass 1 dropped are now bullets here marked `no id`** — §1's definition of what a structured syntax suffix is for, and §2's parenthesis about JSON's self-delimitation, which is the only sentence of §2 the extraction missed |
| requirements | `requirements.yaml` | 61 entries `R-0001`–`R-0061` in source order, no gaps: **4 stated, 57 inferred**. `source_keyword_count` and `extracted_keyword_count` both **4**, agreeing, with a **4462-character** `reconciliation` written anyway *(`[cross-check]` 2026-10-21, pass 3: this said "3.5 KB", which was its length before pass 2 appended the overturned-vacuity correction to it; measured from the parsed scalar)* because 4 is misleading in two directions — *where* the four are (none constrains the format; one is deferred, and only one of the four has an applicable effect at publication — `[correction]` 2026-10-20, pass 2, which read "two are vacuous") and *what the document says in lower case instead* (the only statement of how to decode it). §1.1's BCP 14 boilerplate is deliberately never quoted: `bin/validate` counts texts with stripping off, so quoting it would add 11 phantom keywords and make the extraction read 15 against a source of 4 |
| schema | `schema/` | **3 verbatim, 3 derived.** Verbatim: all 3 CDDL fragments, and the three registrations complete (§6.1 template, Table 1, §6.3 template) — 6 regions, each with its source line range and its own sha256, all byte-identical and all digests verifying under the stated convention and **under none of the alternatives**. Derived: the format as a grammar (`cbor-seq.derived.abnf` — **two productions, one a placeholder**, and the one-line first production is everything a grammar can say about this format), a dedented CDDL companion that round-trips, and **the container rule §4.1 says cannot be written, written four ways with the byte cost of each**. No `*.schema.json`, and `schema/README.md` says why |
| messages | `messages.yaml` | 6 structures, 37 field entries: the sequence, its element, §4.3's wrapped element, and the three IANA registration records. **`framing_bytes_contributed_by_this_document: 0`** — the `framing` pseudo-field enumerates the absence field by field. `constrained_by` is used: **31** of the 61 requirements are cited by a named field and the **30** that are not are listed with a reason each, the split being lopsided *because half of §2 is a decoding procedure rather than a set of fields* |
| state-machine | `state-machine.yaml` | **DERIVED. The N/A verdict was weighed and rejected at pass 1; pass 2 kept the artifact and withdrew the reason** — see *Not applicable* below, and read it before citing this file, because **five sibling CBOR records declare this artifact N/A for the same class of document.** 5 states, 7 transitions, 1 absorbing error state, every state anchored to a quoted sentence of §2, and **0 occurrences of the word "state" in the source**. Its payload is **not** `indistinguishable_pairs` — two of those three pairs are pairs of *artifacts*, not of states, and `messages.yaml` `completeness` already holds them. What has no other home is `guards_the_source_does_not_supply`: no element-size bound, no count bound, and **no timeout on a paused decoder**, which is only stateable if the pause is modelled |
| examples | `examples/` | **16 vectors in two classes.** `V-0001`–`V-0005` are the source's own — and **five is every example RFC 8742 prints**; all five re-verified as dedented contiguous slices at their declared line ranges. `D-0001`–`D-0011` are **derived, ours**, each executed through a CBOR well-formedness checker written for this pass and each carrying the observed result. **The document prints 0 hex octets** |
| design-notes | `design-notes.md` | the completeness answer with its three source statements and three fixtures; an artifact-to-container mapping over all of `ARCH-0001` §4.1 (*everything of ours except the log wants an array*); **MD-3 clause by clause, where the mapping is measurably empty**; all six `canonical-encoding` conditions; **five named cuts against MD-3**, four naming the DEC-002 option they favour and one stated in option 5's favour; 6 source defects; and an explicit confirmed/narrowed/**refuted** audit of `summary.md`, with three claims refuted |

## Not applicable

- **protocol** — RFC 8742 defines **no exchange, no role and no message.**
  Measured over the whole source at this pass: `role` 0 occurrences, `party` 0,
  `client` 0, `sender` 0, `receiver` 0, `recipient` 0, `peer` 0, `endpoint` 0,
  `handshake` 0, `exchange` 0, `message` 0, `negotiat*` 0, `session` 0,
  `connection` 0 — all re-derived whole-word and case-insensitive at pass 3, and
  all still 0 as substrings too. `protocol` occurs once, inside "Constrained
  Application Protocol (CoAP)" in §1, and `request` occurs once, at **source
  line 6** — "Request for Comments: 8742", the RFC's own masthead. *(`[cross-check]`
  2026-10-21, pass 3: this bullet said `request` and `protocol` occurred once
  each "**both** inside "Constrained Application Protocol (CoAP)" in §1". The
  count was right for both and the attribution wrong for `request`: it is not in
  §1 at all. `record.yaml`'s `not_applicable` reason carried the same sentence
  and is corrected there too. The N/A verdict is unaffected and in fact
  strengthened — the document's one `request` is bibliographic.)* The only actors the document
  names are a **decoder**, a **producer**, an **application** and a
  **specification author**, and §3's one sentence about an application —
  "Applications encountering a "+cbor-seq" media type can then either simply use
  generic processing if all they need is a generic view of the CBOR Sequence or
  use generic CBOR Sequence tools for initial parsing and then implement their
  own specific processing on top of that generic parsing tool." — quoted in
  full rather than elided — is a permission about local processing, not a step
  in an exchange. §6's three registrations are **completed**, in the past tense
  ("IANA has registered", "IANA has assigned"), and are registry records rather
  than procedures. `protocol.yaml` and `protocol.md` are therefore absent, not
  stubbed.

- **state-machine is NOT declared not applicable, and the decision should be
  re-weighed at pass 2.** The expected verdict was N/A and the measurement that
  would support it is real: `state` 0 occurrences, `transition` 0, `lifecycle`
  0, `phase` 0, `step` 0, `event` 0, `verify` 0, `revoke` 0, `expire` 0,
  `rotate` 0. The test applied instead was *does the document distinguish two or
  more conditions of a thing over time, and name at least one transition between
  them?* — and it does, in one sentence: "A CBOR Sequence decoder that is used
  for consuming streaming CBOR Sequence data may simply pause for more data
  (e.g., by suspending and later resuming decoding) in case a truncated final
  item is being received." **Pause, suspend, later resume.** The artifact was
  built because the completeness finding's sharpest form *is* a state
  indistinguishability, and an N/A would have lost it. `state-machine.yaml`
  states the alternative and the grounds in its own header so that pass 2 can
  overturn it cheaply.

  **Pass 2 (2026-10-20) kept the artifact and withdrew that justification.
  `[correction]`** Two of its three claims do not hold. *First*, "the
  completeness finding's sharpest form **is** a state indistinguishability" is
  false as written: of the three `indistinguishable_pairs`, only the first is a
  pair of **states** of the machine, and it is marked
  `distinguishable: true`. The two that carry the finding — a complete log
  against one truncated at an item boundary, and a never-written sequence
  against a fully truncated one — are pairs of **artifacts**, not of states; the
  machine's own `how` field says "Both are `input-exhausted-at-boundary`", one
  state and two files. *Second*, "an N/A would have lost it" is false: the
  finding **does** relocate, and in fact is already relocated —
  `messages.yaml`'s `cbor-sequence.completeness` holds it with the same three
  quotations and the same three ids, and `examples/vectors.yaml` holds it
  executably as `D-0001`, `D-0004` and `D-0005`, with `D-0001` and `D-0005`
  deliberately the same bytes. *Third*, the precedent is against the artifact:
  **five sibling CBOR records are at `profile: full` with state-machine
  declared N/A, all five for the same class of document but on three different
  grounds** — `rfc-9804` names parsing, `rfc-8949` "The one stateful process is
  the decode of a single data item, which has no persistent states, triggers or
  guards.", `rfc-8610` and `rfc-9741` that matching is a *predicate* over a
  specification and an instance rather than a lifecycle, and `rfc-9682` a
  deployment transition in the installed-tool population.
  *[correction 2026-10-21, pass 3 — cross-check] This read "every one gives the
  same reason — their only stateful process is parsing". Only one of the five
  does. It also quoted `rfc-8949`'s sentence with a lowered capital and no
  final stop; that record writes "**The** one stateful process … guards**.**"
  The lower-case variant resolves nowhere in `rfc-8949` — it resolves only
  against this lane's own copies of the miscopy, which is why a per-record
  audit reported success.* §2 of RFC 8742 is a
  **loop over** the decode `rfc-8949`'s record calls stateless, and
  `rfc-8742#R-0025` is a lower-case `may` in a parenthetical whose content is an
  implementation technique — which is the `rfc-9741` pattern of holding an
  implementation note as an **algorithm**.

  **What keeps it, stated narrowly:** exactly one thing in the file has no other
  home — the **paused** state, and with it the absent **timeout on a suspended
  decoder** in `guards_the_source_does_not_supply`. An unbounded pause on an
  element that never completes is a denial of service; the document's only BCP 14
  `MUST` names no bound and no failure mode; and that absence is only *stateable*
  if the pause is modelled. `messages.yaml` has fields, and a missing guard on a
  suspended decoder is not a field. Plus the concatenation **self-loop**, which
  is what joins this record to `records/ietf/rfc-9277`. **This record is the
  outlier in its own lane and a reader should know that before citing the
  artifact.**

## Source defects found

Six, in `design-notes.md` §7. The three that matter: **§6.1 and §6.3 register
contradictory fragment-identifier dispositions for the same format** — "N/A"
against a `SHOULD` plus a three-case procedure — and §6.3 does not reconcile
them *(`[correction]` 2026-10-20, pass 2: defect 1 used to read "**two of the
four BCP 14 keywords are vacuous at publication** by the document's own
admission"; overturned, see above and `design-notes.md` §7)*; **§6.1
cites a section that does not exist** ("Interoperability considerations:
Described herein.") while §6.3's corresponding field for the same format reads
"n/a"; and **three references used normatively are classified informative** —
§6.3 registers "in accordance with [RFC6838]", §6.2 assigns from a range
[RFC8126] names, §4.1 and §4.3 depend on RFC 8610's control operators, and all
three are in §7.2 — while `[RFC7049]`, the **obsoleted** CBOR specification, is
normative. All reported, none repaired.

## What this does to the lane

- **`rfc-9277` is the sibling and the two disagree in a way neither records.**
  §2's "(Consequently, concatenating zero or more CBOR Sequences also results in
  a CBOR Sequence.)" is the operation RFC 9277 Appendix A.2 says "care must be
  taken" over for *labelled* sequences. Both are right on their own ground —
  well-formedness here, interpretation there — so neither record asserts
  `contradicts`. `state-machine.yaml` holds it as a **self-loop** that the
  sibling record holds as a transition into a state its document declines to
  define.
- **§6.1's "Magic number(s): N/A" is still the registration a reader consults**,
  and `rfc-9277` Appendix B plus this media type's content-format 63 makes one
  *constructible* — `TN(63) = 1668546880 = 0x63740140`, arithmetic checked at
  this pass. RFC 9277 carries no `Updates: 8742`.
- **Nothing here closes `rfc-8610`'s gate.** This document adds no CDDL syntax
  and registers no control operator; it only *uses* `.cborseq` and `.cbor`
  (RFC 8610 §3.8.4) and records that CDDL cannot state a top-level sequence.
  That absence is `design-notes.md` Cut 2 and is still open after RFC 9741,
  RFC 9682, RFC 9165 and `draft-ietf-cbor-cddl-modules`.
