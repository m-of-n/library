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

**State: pass 1 (extract) only. `distillation.standard: FX-1` and NO
`profile`.** An unfinished extraction has no profile — passes 2 (verify) and 3
(cross-check) have not run, and **no `reviewed_by` is signed** on any artifact.
These files are readable and citable; they are not buildable-on.

Source: RFC 8742, *Concise Binary Object Representation (CBOR) Sequences*,
Standards Track, February 2020. sha256
`4462966836b60f42ebae9b5f1d2a479c328e16f0380a3434311a083bccbce30e`, 462 lines,
18421 bytes. **No form feeds, no page footers, no trailing whitespace on any
line, no asides** — so no transformation of any kind was applied to any quoted
span, and `requirements.yaml` says so rather than leaving it to be assumed.

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
finding. `state-machine.yaml` carries the same thing as an
**indistinguishability between two states**.

And §5 closes the escape route rather than opening one: per-element COSE does
not bind "the relationship of the elements in the sequence", with "additional
effort may be required" as the whole of the guidance. `design-notes.md` §1 and
§3.2 carry the argument and the one-sentence fix.

## Read this before using anything here

RFC 8742 carries exactly **four** all-capitals BCP 14 occurrences in 18 KB, and
**§2 — the entire format — contains none of them.** Two of the four are
**vacuous at publication by the document's own admission** (§6.3's fragment
identifiers point at a syntax §6.1 registers as N/A). And the document uses
**lower-case `must`** for the one sentence that states how to decode the format,
which §1.1's own clause excludes from BCP 14 force.

That is expected and correct for a format defined by a recursive definition:
this document is normative by its **definitional cases and its decoding rule**,
not by obligations laid on an actor. **57 of the 61 requirements here are
`kind: inferred`**, each naming in `field` the phrase, definitional case,
explicit absence or registration field value that carries the force. The
precedents are `rfc-8610` (2 keywords in 125 KB, 137 of 139 inferred),
`rfc-9741` (3 in 28 KB, 58 of 61) and `rfc-9682` (0 keywords).

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 63 verbatim spans across 11 locators (§1, §1.1, §2, §3, §4.1–§4.3, §5, §6.1–§6.3) plus the Abstract's first half, with all 3 CDDL fragments, both §4.2 instances, Table 1 and both IANA registration templates reproduced in fenced blocks with their source line ranges. All 63 confirmed contiguous substrings of the whitespace-normalised source **and** confirmed to start and end inside their locator's section, 0 failures. **No transformation applied**: no form feeds, no page footers, no asides, no dedent, no healed hyphenation. Three hyphenation breaks exist in the source and **none** falls inside a quoted span |
| requirements | `requirements.yaml` | 61 entries `R-0001`–`R-0061` in source order, no gaps: **4 stated, 57 inferred**. `source_keyword_count` and `extracted_keyword_count` both **4**, agreeing, with a 3.5 KB `reconciliation` written anyway because 4 is misleading in two directions — *where* the four are (none constrains the format; two are vacuous) and *what the document says in lower case instead* (the only statement of how to decode it). §1.1's BCP 14 boilerplate is deliberately never quoted: `bin/validate` counts texts with stripping off, so quoting it would add 11 phantom keywords and make the extraction read 15 against a source of 4 |
| schema | `schema/` | **3 verbatim, 3 derived.** Verbatim: all 3 CDDL fragments, and the three registrations complete (§6.1 template, Table 1, §6.3 template) — 6 regions, each with its source line range and its own sha256, all byte-identical and all digests verifying under the stated convention and **under none of the alternatives**. Derived: the format as a grammar (`cbor-seq.derived.abnf` — **two productions, one a placeholder**, and the one-line first production is everything a grammar can say about this format), a dedented CDDL companion that round-trips, and **the container rule §4.1 says cannot be written, written four ways with the byte cost of each**. No `*.schema.json`, and `schema/README.md` says why |
| messages | `messages.yaml` | 6 structures, 37 field entries: the sequence, its element, §4.3's wrapped element, and the three IANA registration records. **`framing_bytes_contributed_by_this_document: 0`** — the `framing` pseudo-field enumerates the absence field by field. `constrained_by` is used: **31** of the 61 requirements are cited by a named field and the **30** that are not are listed with a reason each, the split being lopsided *because half of §2 is a decoding procedure rather than a set of fields* |
| state-machine | `state-machine.yaml` | **DERIVED, and the N/A verdict was weighed and rejected** — see *Not applicable* below. 5 states, 7 transitions, 1 absorbing error state, every state anchored to a quoted sentence of §2, and **0 occurrences of the word "state" in the source**. Its payload is `indistinguishable_pairs`, which turns the record's headline finding into something a harness can assert, plus the guards the source does not supply (no element-size bound, no count bound, no timeout on a paused decoder) |
| examples | `examples/` | **16 vectors in two classes.** `V-0001`–`V-0005` are the source's own — and **five is every example RFC 8742 prints**; all five re-verified as dedented contiguous slices at their declared line ranges. `D-0001`–`D-0011` are **derived, ours**, each executed through a CBOR well-formedness checker written for this pass and each carrying the observed result. **The document prints 0 hex octets** |
| design-notes | `design-notes.md` | the completeness answer with its three source statements and three fixtures; an artifact-to-container mapping over all of `ARCH-0001` §4.1 (*everything of ours except the log wants an array*); **MD-3 clause by clause, where the mapping is measurably empty**; all six `canonical-encoding` conditions; **five named cuts against MD-3**, four naming the DEC-002 option they favour and one stated in option 5's favour; 6 source defects; and an explicit confirmed/narrowed/**refuted** audit of `summary.md`, with three claims refuted |

## Not applicable

- **protocol** — RFC 8742 defines **no exchange, no role and no message.**
  Measured over the whole source at this pass: `role` 0 occurrences, `party` 0,
  `client` 0, `sender` 0, `receiver` 0, `recipient` 0, `peer` 0, `endpoint` 0,
  `handshake` 0, `exchange` 0, `message` 0, `negotiat*` 0, `session` 0,
  `connection` 0; `request` occurs once and `protocol` once, both inside
  "Constrained Application Protocol (CoAP)" in §1. The only actors the document
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

## Source defects found

Six, in `design-notes.md` §7. The three that matter: **two of the four BCP 14
keywords are vacuous at publication** by the document's own admission; **§6.1
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
