---
record: rfc-9596
kind: index
title: "rfc-9596 — distilled artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what it
does not.

**State: pass 1 of 3 complete. NO `profile` IS CLAIMED.** Extract ran
2026-10-20 at effort max, reading only `.cache/rfc-9596.txt` — never
`summary.md` and never another record's artifacts. **Pass 2 (verify) and pass 3
(cross-check) have not run**, and every `reviewed_by` here is empty.

RFC 9596 is the **last** record of library#39 Tier 2's CWT envelope lane
(`rfc-8392` → `rfc-9597` → `rfc-9596`) and the thinnest: 232 lines, **three
BCP 14 keywords**, no grammar, no example, not one byte. **This extraction
mostly documents absences, which is worth doing precisely because the absences
are the content.**

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | **11 verbatim regions** covering the whole document except the references, acknowledgements and authors' addresses, each an exact run of source lines with its own `sha256`. §1 is quoted in three parts because **the value space is stated there as well as in §2** — a reader who treats §1 as background misses half the document's statement of its own type space. Unpaginated source, **zero form feeds**, so no region removes anything |
| requirements | `requirements.yaml` | **21 entries R-0001 to R-0021: 3 `stated`, 18 `inferred`**, counts reconciling **3 = 3**, all 21 texts verified mechanically as contiguous substrings of the whitespace-normalised source. The reconciliation is about what **3** *means*: all three are in §2, **there is no MUST, SHOULD, SHALL or RECOMMENDED anywhere in the document**, and not one of the three requires anything |
| schema | `schema/` | 1 verbatim file, 2 derived. **The document ships no grammar of any kind** — `CDDL`, `ABNF`, `ASN.1` and `JSON Schema` each occur **zero** times, and `syntax` occurs three times as the English word. Five verbatim regions capture Table 1 and the four prose sentences that fix the value space and the placement. The derived CDDL names the three things it **cannot** express, each of which is a real gap: equality, consistency with content type, and any check at all |
| messages | `messages.yaml` | 3 structures, 4 fields. `constrained_by` wired, 7 of 21 requirements cited, 0 dangling, and the `coverage` block explains the other 14 — *"One field, one prohibition, and nineteen sentences about a check the specification declines to require."* Every layout is **derived**, because nothing is printed |
| protocol | `protocol.yaml`, `protocol.md` | **NOT APPLICABLE, with the measurement written out.** `protocol`, `exchange`, `sender`, `receiver`, **`recipient`** and `verifier` each occur **zero** times — this is the only record in the lane where even `recipient` is absent — and the document says in terms that there is nothing to model: *"Any processing of this parameter is performed by the COSE application using application-specific processing rules."* |
| state-machine | `state-machine.yaml` | **NOT APPLICABLE, with the measurement written out.** `state`, `lifecycle`, `revoke`, `rotate`, `expire` and `registration` each occur **zero** times. The sharpest form of it is the document's own sentence: *"Changes to unprotected headers do not change the type of the COSE object."* **A type indicator is a constant** — fixed at signing — so there is nothing for a state to be |
| examples | `examples/README.md` | **NOT APPLICABLE, and the absence is the finding.** `Figure`, `hex`, `vector` and `diagnostic notation` each occur **zero** times; `example` occurs **once** and is a definition. **Not one `typ` value is named anywhere in the document**, so there is no reference fixture, no worked example of the equality problem, and every fixture is ours |
| design-notes | `design-notes.md` | the in-band substitute for the tag option 5 drops, with the scoping correction that **the argument is ours**; what the mechanism's absence enables and its presence does not prevent; the `rfc-9597` asymmetry; the four-signal table with the third row now proved; 3 adopts, 3 adaptations, 2 rejections; **MD-3 mapped header by header over 7 of our fields**, then **five cuts against MD-3**, one of them the strongest thing in the lane **in option 5's favour**; `DEC-005`; **condition (4) of `canonical-encoding`, which this is the only document in the lane to supply**; the summary's nine findings tested; 6 source defects; 5 open questions |

## The two results

**1. This is the in-band, authenticated substitute for the CBOR tag MD-3
removes — and it converts a recorded cost of option 5 into a recorded
non-cost.** `records/ietf/rfc-9053`'s extraction ended an item with *"option 5
declines the tag registry — no tag, which means the recipient must be told out
of band that these bytes are a `COSE_Sign1`."* Label 16 is the substitute, and
§2's `MUST NOT` puts it inside `Sig_structure` where no CBOR tag ever was.

**With one scoping correction this pass insists on: the word `tag` occurs ZERO
times in RFC 9596.** The document makes no claim about tags at all, so the
replacement argument is **ours** — assembled from §2's `MUST NOT`, RFC 9052
§4.4, and `rfc-8392` §7.1/§7.2's step order — and must be cited as `[analysis]`
in the `DEC-002` ADR rather than attributed to the RFC.

**2. Three keywords, and no MUST, SHOULD, SHALL or RECOMMENDED at all.** The
whole enforcement side of the mechanism is §3's two **lowercase** `should
reject` sentences, and §2 tells COSE libraries to ignore the parameter. **A
conformant implementation of RFC 9596 performs no check whatsoever.** The only
obligation in the document is a prohibition — and it is the prohibition that
makes the mechanism worth having.

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

1. **The keyword census**, which three separate claims rest on. Recount it
   against `bin/bcp14-count` and against the source by eye; if a fourth keyword
   exists anywhere, two sections of `design-notes.md` change.
2. **The 21 requirement `locator`s.** The texts were verified mechanically as
   contiguous substrings; **no check in this pass tested a locator**, and the
   value space is stated in **both** §1 and §2, so a §1/§2 mix-up is the likely
   error.
3. **The two line-break severances at 86/87 and 116/117.** They are declared
   not-healed in three places; check that no artifact healed one anyway. This is
   the defect class the lane's own audit caught twice.
4. **The size arithmetic in `design-notes.md` §7.5** — 2 octets against 16 —
   which is this extraction's computation from RFC 8949 §3 heads and is not in
   either document.
5. **The `not_applicable` verdicts**, each resting on word sweeps. In particular
   re-check `protocol`: §2's *"an application might verify ... and reject the
   data structure if it is not"* is the closest thing to a flow in the
   document, and this pass judged it illustrative rather than procedural.
