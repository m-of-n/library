---
schema: "library-doc/v1"
id: requirements
title: "What is a requirement"
type: policy
status: draft
version: "0.3.0"
updated: "2026-10-16"
needs_review: true
reviewed: false
source: "sponsor question 2026-09-22: what is a requirement?"
---

# What is a requirement

**Status: draft. Open for review.** Governs
`records/<body>/<id>/distilled/requirements.yaml` — the requirements artifact
of the FX-1 set. `docs/extraction.md` is normative for the set as a whole and
for when it is owed; this document defines what may go in this one file.

## 1. Definition

> A **requirement** is a statement in a source document that constrains what a
> conforming implementation may do, expressed with a normative verb, attributed
> to an actor, and traceable to an exact locator.

Four parts, all mandatory. Missing any one and it is not a requirement:

| Part | Test |
|---|---|
| **Normative verb** | MUST, MUST NOT, SHALL, SHALL NOT, SHOULD, SHOULD NOT, MAY, REQUIRED, RECOMMENDED, OPTIONAL — [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) as updated by [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html) |
| **Actor** | *who* must do it — verifier, issuer, transparency service, implementation |
| **Condition** | when it applies; unconditional is a valid condition, stated as such |
| **Locator** | section or clause. Not a page number — pages do not survive conversion |

## 2. What is not a requirement

- **Description.** "The Transparency Service maintains an append-only log" states
  a fact about a design, not an obligation. Common and easy to misfile.
- **Motivation and rationale.** "This avoids a round trip" explains; it does not
  constrain.
- **Examples**, unless the example text itself carries a normative verb.
- **Lowercase modals.** RFC 8174 is explicit: only *capitalised* keywords carry
  normative force. "should be careful" is advice.
- **Our own conclusions.** A thing we decided is an `R-*` in ARCH-0001, not an
  extracted requirement. Keep the direction of travel straight: requirements are
  extracted *from sources*; our requirements are *authored*.

## 3. Shape

`distilled/requirements.yaml` — **one file per record**, not one per set:

```yaml
schema: "library-requirements/v1"
record: rfc-9943
source_version: "2026-06"
source_digest: "0db36c…"       # the bytes we read
source_keyword_count: 83       # bin/bcp14-count on the fetched source
extracted_keyword_count: 83    # recomputed by bin/validate from the texts
reconciliation: ""             # REQUIRED if the two differ: say exactly why
reviewed_by: ""                # REQUIRED before this set is used
requirements:
  - id: rfc-9943#R-0012
    verb: MUST
    actor: transparency-service
    condition: "on registering a Signed Statement"
    text: "The Transparency Service MUST perform signature verification."
    locator: "§4.2"
    kind: stated                # stated | inferred
    testable: yes               # yes | no | partial
    notes: ""
```

Rules:

- **`text` is verbatim.** Never paraphrase a normative sentence — paraphrase is
  how a MUST silently becomes a SHOULD.
- **`kind: inferred` for anything the document implies but does not state**, and
  it must say so in `notes`. **An invented MUST is a defect that propagates into
  our own specification**, which is the whole reason this file exists.
- **`testable: no` is a finding**, not a failure. A requirement nobody can test
  is worth recording precisely because it cannot be checked.
- **Extraction comes from the source, never from `summary.md`.** The verbatim
  text lands in `distilled/normative.md` and the requirement is lifted from
  there, so there is one hop and it is checkable. `summary.md` is our words
  about the document; extracting from it is two hops, and two hops from the
  source is where drift starts.
- **Completeness is checked, not asserted.** `bin/validate` recomputes
  `extracted_keyword_count` from the texts and fails if it disagrees with the
  header, or if the two counts differ with no written `reconciliation`. See
  `docs/extraction.md`.
- **`reviewed_by` empty means unusable.** An unreviewed extraction may be read,
  but nothing may be built on it.

## 3b. External reference — a requirement must be citable

**Every extracted requirement gets an identifier that resolves to a specific
statement in a specific version of a specific document.**

```
draft-ietf-vcon-vcon-core-04#R-0004
└── record id ──────────────┘ └seq┘
```

Resolving it yields:

| | |
|---|---|
| `locator` | `§4.1.4` — where in the source |
| `source_version` | `-04` — which revision |
| `source_digest` | the bytes we read |
| `verb` | MUST / MUST NOT / … |
| `text` | verbatim |

That is what makes a requirement **qualified**: another document can cite
`draft-ietf-vcon-vcon-core-04#R-0004` and a reader can get back to the exact
sentence, in the exact revision, that we read. A requirement without all five
is an assertion about a document, not a reference into one.

**Sequence numbers are stable and never reused.** A withdrawn requirement keeps
its id and is marked withdrawn — renumbering silently retargets every citation.

## 4. Why ids are namespaced by record

`rfc-9943#R-0012` carries its provenance in its name. A bare `R-0012` collides
across sources, and the first thing anyone asks of an extracted requirement is
"says who?"

Do not renumber. If a requirement is withdrawn, mark it, keep the id.

## 5. When requirements are extracted

**Resolved 2026-10-16 (#67).** This was §5 question 1 — *should requirements be
extracted for every summarised record, or only where we intend to conform or
map?* Five record summaries already cited `§5.1` as governing policy, and a
reader who followed the citation found a question mark. The answer those
records assert is the right one, and `docs/extraction.md` had already
implemented it. The numbering is kept deliberately: **`§5.1` is clause 1
below**, the rule those summaries always meant.

1. **Requirements are extracted only where we intend to conform or map** —
   never as a consequence of having read a document. Summarising a record does
   not owe a `requirements.yaml`. A record with no `distilled/` is a resting
   state we are entitled to leave it in, not an unpaid debt.
2. **`docs/extraction.md` — *What triggers FX-1* — is the operative rule**, and
   the only place the trigger is written down. It turns on what a record says
   it was measured against, not on `status` and not on contact with the record.
   It is not restated here: two copies of a trigger rule is how the last drift
   started (#63).
3. **This document is silent on owing a `requirements.yaml`.** §1–§4 govern the
   file when it exists. Nothing in them pulls a record into extraction.

The cost argument that made it a question stands as the reason for the answer:
extraction is expensive, most records will never need it, and spending it on a
document nothing depends on is how a library turns into a reading list
(`README.md`).

## 6. Open questions

Question 1 was resolved into §5 above (#67); the two that remain are
renumbered, and neither is cited anywhere as settled.

1. Do we track requirement **satisfaction** — which of ours discharges which of
   theirs? That is a conformance matrix and a much larger commitment.
2. Should `verb` normalise SHALL → MUST? They are synonymous in RFC 2119, but
   normalising loses the source's own wording.
