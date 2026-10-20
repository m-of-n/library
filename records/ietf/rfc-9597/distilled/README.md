---
record: rfc-9597
kind: index
title: "rfc-9597 — distilled artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

**State: pass 1 of 3 complete. NO `profile` IS CLAIMED.** Extract ran
2026-10-20 at effort max, reading only `.cache/rfc-9597.txt` — never
`summary.md` and never another record's artifacts. **Pass 2 (verify) and pass 3
(cross-check) have not run**, and every `reviewed_by` here is empty: under
`docs/extraction.md` an unfinished extraction has no profile at all.

RFC 9597 is the **middle** record of library#39 Tier 2's CWT envelope lane
(`rfc-8392` → `rfc-9597` → `rfc-9596`) and the smallest of the three: 265
lines, **8 BCP 14 keywords, all of them in §1 and §2**, and **not one printed
byte.**

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | **16 verbatim regions** covering the whole document except the references, acknowledgements and authors' addresses, each an exact run of source lines with its own `sha256`. §1 is quoted in four parts because it is **normative, not background** — half the keywords are in it. The source is an unpaginated RFC v3 rendering with **zero form feeds**, so no region removes anything |
| requirements | `requirements.yaml` | **28 entries R-0001 to R-0028, 8 `stated` and 20 `inferred`**, counts reconciling **8 = 8**, all 31 texts verified mechanically as contiguous substrings of the whitespace-normalised source. The reconciliation states where all 8 keywords are by line number and why §3, §4 and §5 have none |
| schema | `schema/` | 1 verbatim file, 2 derived. **The document ships four lines of CDDL and declares them non-normative in the sentence immediately before them**, so the verbatim capture reproduces the declaration *and* the fragment as **one region** — separating them would leave the fragment looking normative. The derived CDDL carries what §1's and §2's normative sentences fix and the source's CDDL omits: the three conformant placements, **including the conformant-but-unsigned one** |
| messages | `messages.yaml` | 3 structures, 5 fields. `constrained_by` wired, **8 of 28 requirements cited and all eight are §2's** — 0 dangling, and the `coverage` block explains the other 20, which is the document: **three sentences bind bytes; the rest bind a reader.** Every layout is **derived** from Table 1 and RFC 9052 §3, because the document prints nothing to decode |
| protocol | `protocol.yaml`, `protocol.md` | **NOT APPLICABLE, with the measurement written out.** `protocol`, `exchange`, `sender`, `receiver`, `verifier` and `steps` each occur **zero** times; `recipients` occurs **once**, as the subject of the `MUST NOT`. The one receiver-side check has no failure action, no ordering and no counterparty |
| state-machine | `state-machine.yaml` | **NOT APPLICABLE, with the measurement written out.** `state`, `lifecycle`, `revoke`, `rotate`, `expire` and even `registration` each occur **zero** times. The file records where a lifecycle *would* have been useful: §4 describes two states of a decision — tentative and confirmed — and names neither |
| examples | `examples/README.md` | **NOT APPLICABLE, and the absence is the finding.** `example`, `examples`, `Figure`, `hex`, `vector` and `diagnostic notation` each occur **zero** times. **Every fixture for label 15 would be ours** under `R-O-03`, with nothing to cite |
| design-notes | `design-notes.md` | the protected-placement decision and the precedent to cite for it; the duplication rule's two escape hatches and its undefined *"identical"*; `R-M-12` evidence from both registries; 4 adopts, 6 adapt-or-reject items; **MD-3 mapped header by header over 8 of our fields**, then **five cuts against MD-3** — one of them **for** option 5 — each naming the option it affects; `DEC-005` stated honestly as the weakest edge; all six `canonical-encoding` conditions; the summary's seven findings tested; 5 source defects; 5 open questions |

## The two results

**1. The document gives a conformant producer permission to emit an unsigned
`iss`.** §2 only `RECOMMENDED`s protected placement, and its one `MUST` bars
label 15 from appearing in **both** buckets — expressly permitting the
unprotected one. **This pass demonstrated the coverage boundary rather than
reading it**: `records/ietf/rfc-8392`'s extraction, in the same pass, rebuilt
`Sig_structure` from RFC 9052 §4.4 and **verified RFC 8392's A.3 signature from
exactly its four fields**, so the unprotected map is provably not an input. Our
profile must state protected-only placement and cite `rfc-9943` §6.

**2. All 8 BCP 14 keywords are in §1 and §2 — four in each — and §3, §4 and §5
have none.** So the document's most important instruction to an implementer
(§4: *"Implementers must ensure that any tentative decisions made based on
previously unverified information are confirmed once the cryptographic
processing has been completed"*) is **lower case**, in a document whose entire
purpose is to make claims readable before verification. Under §1.1's *"when, and
only when, they appear in all capitals"* it binds nobody.

## This pass's own quote audit

Built because the lane that wrote these summaries ran one and caught **five
transcription defects in its own prose** — an ellipsis-spliced quotation, two
silently healed line breaks, a terminal colon turned into a full stop, and an
inserted word. The audit here pulls every **unambiguously delimited** quotation
out of every artifact in all three records of the lane — markdown blockquote
runs and `*"..."*` spans, whose delimiters survive the nested `"` that RFC
sentences are full of — and probes each one against every cached source and
every library file, normalising both sides the same way.

**178 quotations audited, 169 resolved as contiguous substrings, 0 splices.**
For any fragment that did not resolve whole, the probe found its longest
matching prefix and then tested whether the remainder matched *elsewhere* — the
signature of two non-adjacent quotes welded into one. **No fragment in these
three records has that shape.**

**It found four defects in this pass's own prose, and each is corrected in
place with the falsified wording recorded:**

1. **An inserted word.** `rfc-9052`'s design notes read *"No tags" and "no
   registry dependence" are different rules, and MD-3 states the first.* All
   three of this lane's design notes quoted it with **`only` inserted**. The
   word is now added in our own voice, marked `[analysis]`, and the three
   summaries carry the same correction.
2. **An ellipsis splice**, in `rfc-9597`'s design notes. The elided clause was
   *"made based on previously unverified information"* — the most load-bearing
   part of the sentence. Now quoted whole.
3. **A silently healed line break**, in `rfc-9596`'s `examples/README.md`:
   *"CoAP Content-Formats"* written as one token where the source breaks it
   across lines 116/117. The one place in this lane that healed a break was in
   the record that declares three times that it does not.
4. **A case change** in a quotation of our own `messages.yaml`.

The nine residuals are each accounted for: three are the **superseded summary
wordings** this pass quotes in order to record them, three are the audit
regex over-running past a closing `**` into our own following sentence, one is
the ellipsis form **deliberately preserved** inside the `[correction]` note that
identifies it, and two are our own `[...]`-labelled notes set as blockquotes.

## What pass 2 should attack hardest

1. **The 28 requirement texts and, more importantly, their `locator`s.** The
   texts were verified mechanically as contiguous substrings; **no check in this
   pass tested a locator**, and §1 spans 43 lines of four very different
   paragraphs.
2. **The claim that §1 is normative.** It rests on a keyword census; recount it.
3. **The derived CDDL's three placement shapes.** They are this extraction's
   reading of one `MUST` and one `RECOMMENDED`, and `nonclaims-label = label
   .ne 15` is a construct of ours — check it against RFC 8610 §3.8 rather than
   against this file.
4. **The three `not_applicable` verdicts.** Each rests on word counts; re-run
   them, and in particular look for a role or a lifecycle hiding in §4's four
   paragraphs, which are the only prose in the document long enough to hide one.
5. **The §7.6 implementation cut**, which is the one argument here that rests on
   a search rather than on the source. It has a shelf life and should be
   re-dated, not re-asserted.
