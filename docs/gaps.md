---
schema: "library-doc/v1"
id: gaps
title: "What is left to make this library best in class"
type: assessment
status: draft
version: "0.1.0"
updated: "2026-09-22"
needs_review: true
reviewed: false
---

# What is left

**State: 28 records — 1 distilled, 1 summarised, 17 stubs, 9 queued.** The
machinery is built; the reading has barely started. This names what still
stands between here and a library someone outside the project would use.

---

## 1. Content — the largest gap, and the least interesting to fix

| | |
|---|---|
| **9 records still carry template summaries** | The original seeds. They look done in a listing and are empty when opened |
| **Two research sweeps not begun** | Trust management (L-014), attestation specifications (L-013) |
| **No `cites` extracted anywhere** | So `index/frontier.md` is empty and snowballing has never actually run |

**Nothing here needs a design decision.** It needs someone to read.

## 2. Depth — distillation is progressive and has barely progressed

One record has distilled artifacts. The model now supports many kinds —
normative prose, fields, requirements, schema, code, examples, state machines —
and only four are populated, for one document.

Missing kinds nothing has yet:

- **`examples/`** — test vectors lifted from a specification. For a project that
  publishes `spec/vectors/` as its interoperability contract, extracting other
  people's vectors is the obvious next move and nobody has done it
- **state machines** — vCon's `Dialog.type` transitions and `redacted`/`amended`
  chains are state, described in prose
- **diagrams**

## 3. Review — the gap that undermines the rest

**Every artifact in the library is `reviewed_by: ""`.** The three mechanical
checks pass; mechanical checks are not review. Until a second person checks one,
the library's own rule says its contents are *readable but not buildable-on* —
and that rule currently applies to everything in it.

`docs/distillation.md` §8 states its own test: **a second person distils a
different specification from it alone.** That has not happened. Until it does,
the procedure is a description of one run.

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

`MANIFEST.yaml` carries a `federation.peers` list that has always been empty.
Cross-library references resolve as `(library-id, record-id, content-hash)` —
**untested**, because there has only ever been one library. The Shelfmark
convergence (T-023) is the obvious first peer and has not started.

## 6. Integrity — the library does not eat its own cooking

This is a **provenance** project. The library:

- records content digests but **verifies none of them on a schedule** — link rot
  and content drift are invisible until someone re-fetches by hand
- publishes `exports/` and `index/` with **no attestation** over them
- has no signed statement over `MANIFEST.yaml`, though `docs/scope.md` §4
  describes exactly that as the federation integrity mechanism

**A provenance project whose own bibliography is unattested is the sharpest
criticism available**, and it is currently true.

## 7. Terminology — two live collisions

**`tags`** means both an SPKI authorization value and a bibliographic label.
**`topic`** means both a unit of parallel work and a delegation scope.
`GLOSSARY-0001`, register items 6b/6c. Every record added carries `tags:`, so
this compounds daily.

---

## Ranked — what actually moves the needle

1. **Get one thing reviewed by a second person.** It unblocks the credibility of
   everything else and costs an afternoon.
2. **Fill the 9 queued records.** They are the ones that look done and are not.
3. **Resolve `tags` / `topic`** before more records carry the collision.
4. **Extract `cites` on one record** so the frontier is non-empty and snowballing
   is demonstrated rather than described.
5. **Attest `MANIFEST.yaml`** — small, and it removes the sharpest criticism.
6. **A reading path**, for a person who has not read any of it.
7. Run the two research sweeps.
8. Federate with Shelfmark.

**1 through 4 are days. 5 through 8 are the difference between a working tool
and something a stranger would adopt.**
