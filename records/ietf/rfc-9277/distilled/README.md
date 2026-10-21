---
record: rfc-9277
kind: index
title: "rfc-9277 — distilled artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

**State: passes 1 and 2 of 3 (extract, verify). `distillation.standard: FX-1`
and NO `profile`.** An unfinished extraction has no profile — pass 3
(cross-check) has not run, and **no `reviewed_by` is signed** on any artifact.
These files are readable and citable; they are not buildable-on.

Pass 2 (2026-10-20, adversarial, did not extract) re-derived every count,
re-ran the id-join audit across the whole lane, and corrected **fourteen** things
in this record's own text — six wrong requirement ids, a cluster of five wrong id
*ranges* in one schema header, one truncated requirement `text`, two rows that
claimed a cite their own counts contradicted, three bad self-counts, one word
whose occurrence count was zero rather than two, and the 30-spelling zero-byte
figure, which stood at 20 in **six** files when it is 25. It also found **nine
statements with no requirement entry**. Every correction is marked
`[correction]` with its date where it stands; `requirements.yaml` `verify_pass`
is the index.

Source: RFC 9277, *On Stable Storage for Items in Concise Binary Object
Representation (CBOR)*, Standards Track, August 2022. sha256
`bd637eafad9ef940c8f5d029076f70c58af7bde6beb38efee5ba7af3690289f7`, 960 lines,
41659 bytes. No form feeds, no page footers; **two RFC v3 asides** (source lines
715–727 and 765–777), **four lines with trailing whitespace** (724, 767, 770,
772 — all blank aside lines), **two U+2264** characters on line 771, and
**fourteen line-end word breaks** in the body, every one left unhealed.
*(`[correction]` 2026-10-20, pass 2: this read "twelve hyphenation breaks".
`requirements.yaml`'s own list named thirteen, the census is fourteen — the
fourteenth is at source lines 897/898 in Appendix D, and `requirements.yaml`
described that very break in the sentence after the list it omitted it from. Only
eight of the fourteen break a hyphenated token; the other six break after a
slash, in `application/`. Two of the fourteen have a half with no partner: see
`verify_pass`.)*

## Read this first: the document has no normative statements

`bin/bcp14-count` returns **0**, and it is not a rendering artefact. Measured
over the whole source at this pass, **"BCP 14", "RFC 2119", "RFC 8174" and "key
words" do not appear at all** — there is no requirements-language section for the
keywords to have been omitted from, and every all-capitals keyword form occurs
zero times.

So **all 195 requirements here are `kind: inferred`**, each naming in `field` the
structural rule, allocation, registry field value, permission, disclaimer or
lower-case force word that carries the force. The precedent is `rfc-9682`, also a
zero-keyword Standards Track RFC. And the consequence is the reason the record's
`tags` say `evidence` rather than `normative`: **a claim to conform to RFC 9277
is not testable**, and when two implementations disagree about whether a label
may appear mid-file there is no clause to point at.

## The answers this record was extracted for

**1. Under a no-IANA-tags rule, is in-band identification available at any
price? No — and the reason is narrower than it looks.** All **three** envelopes
are two nested tags, and the **outer** tag (55799, 55800, 55801) says only
*CBOR*. The **inner** tag is the one that names the protocol, and §2.1 requires
one "for each kind of object that they might store in files", from a First Come
First Served allocation. Under DEC-002 option 2 that costs one email; under
option 5 it is excluded by definition.

**2. And the substitute would not have discharged our own condition (4)
anyway.** Under all three methods the indicator sits **outside every
signature** — the tag heads enclose the payload, or the label is a separate data
item in front of it. Fixture `examples/vectors.yaml` `D-0003` relabels a file by
swapping the inner tag: well formed, 15 bytes, no signature broken. So what
option 5 gives up is `file(1)`, triage and forensics — **not** the type
indicator `R-O-05` wants.

**3. The magic number is not deterministic.** §2 claims "a deterministic first 8
to 12 bytes" and nothing in the document requires preferred serialization.
`schema/prefix-spellings.derived.txt` enumerates **30** well-formed
definite-length spellings of the 12-byte label: **1** is 12 bytes, **5** match
the stated fingerprint, **25** contain a zero byte inside the first eight
(`[correction]` 2026-10-20, pass 2: **20** here and in five other files; the
enumeration itself always said 25, and 25 re-derives from RFC 8949 §3). And
**30 is a floor** — settled at pass 2: RFC 8949 §3.2.3 admits "zero or more"
chunks in an indefinite-length byte string, so empty chunks are permitted
without bound and **the set of well-formed labels is infinite.** 30 is exact
only for the definite-length family.

**4. 65,025 CBOR tag code points are a mechanical function of another
registry.** §4.3's `TN(ct)` formula, recomputed and held as data in
`schema/content-format-tag.derived.yaml`. This is the strongest evidence in the
library for `R-M-12`, and it closes the *identify by media type, not by tag* escape route — because `application/cbor-seq` already holds content-format 63,
so `TN(63) = 0x63740140` and the tag comes for free.

**5. Concatenating two labelled files is in spec under RFC 8742 and undefined
here.** `design-notes.md` §3.1, `state-machine.yaml`, fixtures `D-0004` and
`D-0005`.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 195 verbatim spans across **24 locators** (Abstract, §1, §1.1, §1.2, §2, §2.1–§2.3.1, §3, §4–§4.3, Appendices A, A.1–A.3, B, B.1, C, D, D.1), plus both hex examples, the Openswan hex, all four CDDL snippets, the three registry entries and the TN formula with its aside reproduced in fenced blocks with their source line ranges. All 195 confirmed contiguous substrings of the whitespace-normalised source **and** confirmed to start and end inside their locator's section, 0 failures — re-verified at pass 2, where **188** resolve against the raw source and **7** only against the bar-stripped source, exactly the seven declared, and **0** resolve only after a word break is healed. **Two declared classes of exception, neither healed:** the two aside bars (stripped on 715–727 and 765–777 and nowhere else), and **fourteen line-end word breaks**, each sentence quoted as two halves cut where the source cuts it — *except two, where the second half was never extracted at all, and one more in Appendix D whose halves are reachable only through §2.3's ids* (`[correction]` 2026-10-20, pass 2: this cell said "twelve" and "each sentence quoted as two halves"; both were wrong). **Six statements pass 1 dropped are now bullets here marked `no id`**, and three more are listed under *What is NOT in this file* |
| requirements | `requirements.yaml` | 195 entries `R-0001`–`R-0195` in source order, no gaps, **all `inferred`**. `source_keyword_count` and `extracted_keyword_count` both **0**, with a 3367-character `reconciliation` — required by `bin/validate` at zero — stating that the baseline is *there is none*, what the document uses instead (`may` 24, `should` 6, `must` **2**, both lower case — all three recounted and agreeing at pass 2, where `optional` turned out to occur **zero** times rather than the twice `reconciliation` claimed), and what was counted in its place: every structural rule of the three methods, every allocation and registry field value, the **four** permissive statements about stripping and the **one** warning running the other way, every disclaimer of normativity, and the four worked `TN` values. **Pass 2 added a `verify_pass` block**: the lane-wide id-join audit, the nine statements with no entry, and the eleven corrections to this record's own text |
| schema | `schema/` | **4 verbatim, 3 derived.** Verbatim: all four CDDL snippets, the three registry entries complete, and the TN formula with its aside — 8 regions, each byte-identical to its declared range with its own sha256 verifying under the stated convention and **under none of the alternatives**. Derived: `content-format-tag.derived.yaml`, the TN function as checkable data; `prefix-spellings.derived.txt`, the enumeration that refutes §2's determinism claim; and `envelopes.derived.cddl`, the three envelopes as CDDL — whose value is the **four things CDDL cannot say** about them. 15 mechanical checks, all passing |
| messages | `messages.yaml` | 7 structures and 29 field entries plus a 3-field `shared_shape`: the three envelopes, the derivable content-format tag, and the three registry records. Each envelope carries `relation_to_signature` — the condition-(4) finding, per method. `constrained_by` is used: **56** of the 195 requirements are cited by a named field and the **139** that are not are accounted for **by locator with counts**, every row recomputed mechanically. The ratio is low on purpose and the file says why: most of this document is motivation, terminology, informative advice and a case study, none of which a field-centred artifact can hold |
| state-machine | `state-machine.yaml` | **DERIVED; the N/A verdict was weighed and rejected at pass 1 and the rejection was UPHELD at pass 2, on a different argument** — see *Not applicable*. 5 states, 8 transitions, **1 self-loop** (relabelling, which no integrity check sees), 1 error state, and **0** occurrences of the word "state" in the source. Its payload is `the_asymmetry` — four permissive statements about removing the envelope, **zero** about adding one, one warning about its presence — and **6 `undefined_transitions`**, including the mid-file label the document creates and declines to define |
| examples | `examples/` | **14 vectors.** `V-0001`–`V-0007` are the source's own: **three complete annotated hex examples** and four CDDL snippets. Every hex string was rebuilt from its annotated source lines and found identical, executed through a CBOR decoder, and both stated fingerprints confirmed; all four `TN` values recomputed and agreeing. `D-0001`–`D-0007` are **derived, ours**: non-preferred spellings, relabelling, concatenation with and without the second label, `TN(63)`, and an unregistered inner tag. **Two derived fixtures deliberately have no expected result, because the document defines none** |
| design-notes | `design-notes.md` | the five answers above with their fixtures; **MD-3 clause by clause**, where the load-bearing cell is that COSE is "considered infrastructure" and so gets no identity at all — which matters because our export artifact *is* a `COSE_Sign1`; an artifact-by-artifact map over `ARCH-0001` §4.1 whose shape is that *this document labels files and our requirements are about keys and digests*; all six `canonical-encoding` conditions; **six named cuts against MD-3**, four naming the option they favour, **one stated in option 5's favour** and one recording that nothing here supports options 1 or 3; **9 source defects**; the zero-keyword finding with its three consequences; and a confirmed / extended / **refuted** audit of `summary.md` with **three refutations** |

## Not applicable

- **protocol** — RFC 9277 defines **no exchange, no role and no message**, and
  the measurement is unusually clean because the document's own term of art looks
  like a counter-example and is not. **"protocol" occurs 42 times** and every
  substantive one is the term §1 defines in a parenthesis: **"(A CBOR Protocol is
  a specification that uses CBOR as its encoding.)"** — a *specification*, not a
  party. The breakdown, counted at this pass: `CBOR Protocol` 13, `Protocol` standalone 13 (one of them "the Protocol"), `CBOR Protocols` 3, `Protocols` 1, `Non-CBOR Protocol` 2, lower-case `protocol`/`protocols` 10 — 42 in all. Meanwhile `role` 0 occurrences, `party`
  0, `client` 0, `sender` 0, `receiver` 0, `recipient` 0, `peer` 0, `endpoint`
  0, `handshake` 0, `negotiat*` 0, `session` 0, `connection` 0; **`message`
  occurs once** and refers to *other* protocols' messages ("but not within
  protocol messages that already provide the necessary context"); **`exchange`
  occurs once** and is in the Acknowledgements ("email exchanges on the mailing
  list"); and `server` occurs twice, both as examples of third-party software.
  §2 is *titled* "Protocol" and contains two byte layouts. §4's four allocations
  are **completed**, in the past tense. `protocol.yaml` and `protocol.md` are
  therefore absent, not stubbed.

- **state-machine is NOT declared not applicable, and the decision should be
  re-weighed at pass 2.** The expected verdict was N/A and the measurement that
  would support it is real: `state` 0 occurrences, `transition` 0, `lifecycle`
  0, `phase` 0, `step` 0, `event` 0, `verify` 0, `revoke` 0, `expire` 0,
  `rotate` 0. The test applied instead was *does the document distinguish two or
  more conditions of a thing over time, and name at least one transition between
  them?* — and it does **five times over**, all of them the same transition
  (strip), plus a second transition (concatenate) whose target state it declines
  to define. The artifact was built because **the record's two sharpest findings
  are both transition-shaped**: relabelling is a self-loop no signature sees, and
  a mid-file label is a state with no rule. `state-machine.yaml` states the
  alternative and the grounds in its own header so pass 2 can overturn it
  cheaply.
  **Pass 2 (2026-10-20) upheld the artifact and replaced that argument.** "Five
  times over" is not a test for lifecycle — by it, RFC 8949 §3 would qualify, and
  `records/ietf/rfc-8949` declares state-machine N/A. What survives is a
  **subject** argument: this machine's subject is one *stored representation over
  its life*, acted on by different parties at different times, where the five
  sibling CBOR records that declare N/A (`rfc-8949`, `rfc-9804`, `rfc-8610`,
  `rfc-9741`, `rfc-9682`) all give the same reason — *their only stateful process
  is parsing*. Storing, stripping and storing again is not parsing. See
  `state-machine.yaml`'s header and `design-notes.md` §12.

## Source defects found

Nine, in `design-notes.md` §7. The three that matter most: **the document's own
CDDL does not match the document's own example** (Appendix B.1's
`senml-cbor = #6.1668546929(bstr)` against §2.2.1's array tag content, with B.1
cross-referencing §2.2.1 directly); **the TN formula's arithmetic is defined only
in an appendix and only by reference to ISO/IEC 9899**, a paywalled normative
reference, while the §4.3 registry entry IANA publishes carries the formula and
not the citation; and **§2's determinism claim is false in general**. Also: a
content-format in a non-identity coding has **no defined tag content** inside
55799; a reader with a known outer tag and an unknown inner one has **no defined
behaviour**; the reference consumer `file(1)` gets **no `magic(5)` pattern**; an
unresolved kramdown anchor `{#sequences}` survives into the published text; three
textual inconsistencies; and two structural slips. All reported, none repaired.

## What this does to the lane

- **`rfc-8742` is the sibling, and the two disagree in a way neither records.**
  RFC 8742 §2 blesses concatenation of sequences; Appendix A.2 here says
  concatenating *labelled* sequences needs care and leaves the rule to each
  protocol. Both are right on their own ground — well-formedness there,
  interpretation here — so neither record asserts `contradicts`.
  `state-machine.yaml` holds it as a transition into an undefined state, where
  the sibling holds the same operation as a harmless self-loop.
- **The `TN(63)` corollary joins the two records.** `application/cbor-seq` holds
  CoAP Content-Format 63 (RFC 8742 §6.2, Table 1), so a labelled
  CBOR-sequence file needs **no new allocation at all** — and RFC 8742 §6.1 still
  registers "Magic number(s): N/A" while RFC 9277 carries no `Updates: 8742`.
- **One library defect found, reported, not repaired.** `bin/_yaml.py` silently
  mis-parses inline flow maps and **truncates a multi-line flow sequence at the
  first line**. The second already affects
  `records/ietf/rfc-8392/distilled/protocol.yaml` lines 260 and 272 and
  `state-machine.yaml` line 114 — not this lane's records.
  `design-notes.md` §11 records it.
