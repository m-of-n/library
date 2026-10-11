---
schema: "library-doc/v1"
id: gaps
title: "What is left to make this library best in class"
type: assessment
status: draft
version: "0.2.0"
updated: "2026-10-11"
needs_review: true
reviewed: false
---

# What is left

**State at 2026-10-11 — 304 records, 19 topics.** Of the records: **37
written, 267 unwritten scaffolds, 4 fully extracted** under FX-1 (6 carry any
`distilled/` at all). Of the topics: **4 answered, 15 open.**

> **This file was wrong by an order of magnitude for ten days.** Until this
> revision it opened *"28 records — 1 distilled, 1 summarised, 17 stubs, 9
> queued"*, written against 2026-10-01 and never updated while the library grew
> past 300. An assessment document that reports a stale headline is worse than
> no assessment, because it is read as current. Every number above comes from
> `bin/validate`, and the rule going forward is that **this file is refreshed
> from the tool, in the same PR as any change that moves a count.**

The machinery is built. The reading has started hard **in one lane** and barely
anywhere else, and that distribution — not the total — is the finding.

---

## 1. Content — the shape of what is missing has changed

The old version of this section said the reading had barely started. That is no
longer true, and the replacement problem is sharper.

| | |
|---|---|
| **267 of 304 records are unwritten scaffolds** | They look done in a listing and are empty when opened. This is the same defect the old "9 template summaries" named, at thirty times the scale (library#45) |
| **The written work is concentrated in one area** | All 4 FX-1 extractions are CBOR/COSE/JSON canonicalisation. 4 of the 19 topics are answered and 3 of those 4 sit in the same lane |
| **`cites` now exists, on 6 records** | All six came in through the SBOM lane. `index/frontier.md` is no longer empty, but snowballing has been demonstrated **once**, not adopted |
| **One research sweep ingested, not written; one not begun** | L-013 attestation specifications: 26 records under `device-attestation`, ingested, unwritten. L-014 trust management: not started |

**Nothing here needs a design decision.** It needs someone to read. The count
stopped being the measure some time ago; **37 written** is the number to move.

## 2. Depth — progressive distillation, now genuinely progressing

Six records carry `distilled/`. Four reach FX-1 `full`.

**What the model supports and now has:** normative prose, requirements with
reconciled keyword counts, schemas, messages, protocol models, design notes
mapped to our decisions, and — new since the last revision — **`examples/` on
all four full records.** The old version named `examples/` as the obvious
missing kind and it is now the best-populated one. RFC 8785's vectors in
particular are carried verbatim with expected results, including the ones the
source gets wrong.

**Kinds that nothing has yet:**

- **`state-machine.yaml` — zero records.** vCon is the named candidate and is
  already `distilled`: `Dialog.type` transitions and the `redacted`/`amended`
  chains are state, described in prose. Nobody has lifted them
- **diagrams** beyond the Mermaid sequence diagrams in two `protocol.md` files

## 3. Review — still the gap that undermines the rest

**Unchanged, and still first. Every artifact in the library is
`reviewed_by: ""` — 73 of them, across records and topics. Not one has been
reviewed by a second person.**

The three mechanical checks pass; mechanical checks are not review. Until a
second person checks one, the library's own rule says its contents are
*readable but not buildable-on* — and that rule currently applies to
everything in it, **including the four FX-1 extractions that mofn#8 is
expected to decide DEC-002 against.**

`docs/distillation.md` §8 states its own test: **a second person distils a
different specification from it alone.** That has not happened. Until it does,
the procedure is a description of one run.

> This is the cheapest high-value item in the file and has been for a month.
> One afternoon, one record, one second reader.

## 4. Discovery — nobody outside can find anything

The library is a git repo with generated markdown. That is enough for us and
insufficient for anyone else:

- **No search.** `index/by-decision.md` answers *our* question; a stranger has
  no way in
- **Not published.** `index/bibliography.md` renders on the site through `mofn`,
  but the library has no page of its own
- **No reading path.** PROC-0004 §9.3 calls for *a reading path for a newcomer,
  not just an index*. There is an index
- **No stable citation form.** A record can be cited as `library@<commit>`;
  there is no DOI, no permalink, no "how to cite this library"

## 5. Federation — designed, never exercised

`MANIFEST.yaml` carries a `federation.peers` list that is **still empty.**
Cross-library references resolve as `(library-id, record-id, content-hash)` —
**untested**, because there has only ever been one library. The Shelfmark
convergence (T-023) is the obvious first peer and has not started.

## 6. Integrity — the library does not eat its own cooking

This is a **provenance** project. The library:

- records content digests but **verifies none of them on a schedule** — link rot
  and content drift are invisible until someone re-fetches by hand
- publishes `exports/` and `index/` with **no attestation** over them
- has no signed statement over `MANIFEST.yaml`, **and no document specifies
  one.** `docs/construction.md` decision 4 makes *content hash is identity* the
  federation integrity mechanism, which is digest-based: two libraries that
  never sync agree on *which document* they mean, and on nothing about *who
  said so*. §5 above is federation's untested half; this is its undesigned
  half. (Earlier revisions of this bullet cited `docs/scope.md` §4 for a signed
  manifest. §4 has never mentioned federation, in either revision — the
  citation was wrong rather than stale.)

**A provenance project whose own bibliography is unattested is the sharpest
criticism available**, and it is currently true. It is also now *reachable*:
mofn's W-1 wallet engine signs statements over a file digest, and a library
record is a file with a digest.

## 7. Terminology — one collision, being fixed

The two collisions this section used to name — **`tags`** and **`topic`** —
were **withdrawn on 2026-09-22** as register items 6b and 6c. Neither survives
the test `GLOSSARY-0001` states: two senses collide only when both can be live
in the same context, and both of those are homonyms across separated repos.
Carrying them here for three weeks after they were withdrawn was this file
repeating a retracted claim.

**The live one is `D-n`.** `D-1 … D-7` (mofn's dated decisions) and `D0 … D10`
(its deliverables) are both live in one table in `PLAN-0003`, and this library
cites `D-3` in fifteen files including its own PR template and extract skill.
Being fixed by the rename to `MD-n` (library#65 and the mofn companion); a
redirect note in `GLOSSARY-0001` keeps older citations resolving.

---

## Ranked — what actually moves the needle

1. **Get one thing reviewed by a second person.** Unchanged at #1 for a month.
   It unblocks the credibility of everything else, costs an afternoon, and
   currently blocks four extractions that a DEC-002 ADR is meant to rest on.
2. **Move `37 written` upward.** The 267 scaffolds are the ones that look done
   and are not (library#45). Batch by topic.
3. **Spread the written work beyond one lane.** Four answered topics, three in
   the same area. L-013's 26 ingested attestation records are the obvious next
   block.
4. **Extract `cites` beyond the SBOM lane**, so the frontier reflects the whole
   library rather than one topic.
5. **Lift one state machine** — vCon, already distilled, prose already read.
6. **Attest `MANIFEST.yaml`.** Small, removes the sharpest criticism, and the
   mofn wallet engine (W-1) makes it a demo rather than a chore.
7. **A reading path**, for a person who has not read any of it.
8. Federate with Shelfmark.

**1 through 5 are days. 6 through 8 are the difference between a working tool
and something a stranger would adopt.**
