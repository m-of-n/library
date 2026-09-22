---
schema: "library-doc/v1"
id: scope
title: "Ingestion scope — what belongs in this library"
type: policy
status: draft
version: "0.1.0"
updated: "2026-09-22"
needs_review: true
reviewed: false
backlog: L-018
source: "library#1 item 10"
---

# Ingestion scope

**Status: draft. Open for review.** Decisions marked **[?]** need the sponsor.

The library fails in one of two ways: too narrow and it misses the evidence a
decision needed; too broad and nobody reads it, which is the same as it being
empty. This document draws the line.

---

## 1. In scope

| Kind | Type | Example |
|---|---|---|
| Standards | `rfc` `spec` | RFC 9943, ISO/IEC 19566-5 |
| Specifications, not ratified | `draft` `spec` | draft-ietf-cose-merkle-tree-proofs |
| Recommendations, best practice | `spec` `rfc` | IETF BCP, NIST SP 800-57 |
| White papers, technical reports | `paper` | NIST IR, vendor architecture papers |
| Academic publications | `paper` `article` | Wohlin snowballing, arXiv preprints |
| Open source projects | `repo` | sigstore/rekor, in-toto/attestation |
| Standards bodies and consortia | `consortium` | IETF COSE WG, C2PA, W3C |
| Document families | `hierarchy` | the SLSA release line, C2PA 2.x |
| Websites with durable technical content | `web` | a spec landing page, a registry |
| Registries and datasets | `dataset` | IANA COSE Header Parameters |
| Regulation | `spec` | EU CRA, EU AI Act Art. 50 |

## 2. Out of scope

- **News coverage and blog posts**, unless the post *is* the primary source for
  a claim we make — then `role: evidence`, and say why in `summary.md`.
- **Marketing material.** A vendor architecture paper is in; a product page is
  an `implementations` entry, not a record.
- **Secondary summaries of primary sources we already hold.** If we have RFC
  9943, an explainer about RFC 9943 adds nothing unless it *disagrees* — in
  which case ingest it and set `contradicts`.
- **Anything without a stable locator.** If it cannot be cited and re-retrieved,
  it cannot be evidence. A screenshot is not a source.
- **Anything we cannot lawfully record.** We store digest and URL, never bytes —
  but do not record paywalled material in a way that implies we redistribute it.

## 3. The rule that does most of the work

> **An implementation of a spec we already hold is not a new record. It is an
> `implementations` entry on that spec's record.**

`sigstore/cosign` does not get a record because it implements things we already
track. It appears under `implementations.open_source` on the relevant spec.

A repo earns its own record only when **the repo is the primary source** — the
specification lives there and nowhere else. `in-toto/attestation` qualifies;
`sigstore/cosign` does not.

This is the difference between a library of ~60 useful records and one of ~400
that nobody reads.

## 4. Depth and granularity

- **One record per document *version*.** A new version is a new record linked by
  `supersedes`, never an edit in place. Citations must not silently retarget.
- **Do not ingest a whole working group.** Ingest the WG as one `consortium`
  record, then only the documents that bear on something, each with `part_of`.
- **Families get a `hierarchy` parent.** Forty sibling records with no parent is
  a failure, not thoroughness.
- **Registries are one record**, not one per entry. The IANA COSE Header
  Parameters registry is a single `dataset` record even though it bears heavily
  on R-M-12.

## 5. Stubs — the cheap path

A reference that is interesting but bears on no open decision is ingested as
`status: stub` with empty `bears_on`. It costs one directory and preserves the
find.

**Never invent relevance to justify a record.** A stub is honest; a fabricated
`bears_on` corrupts the one query the library exists to answer.

## 6. Caps

| | |
|---|---|
| D2 v1 target | **~40 records**, depth over breadth |
| Per topic | ~6–10 records; more suggests the topic is too broad |
| Stub ratio | if over half the library is stubs, we are collecting, not researching |

The library is infrastructure for decisions, not the deliverable. PLAN-0001 §13
names "the library could quietly become the project" as a live risk.

---

## 7. Open questions **[?]**

1. **Does NIST cryptographic algorithm coverage (L-011) belong here at all?**
   FIPS 186-5, 180-4, 202 and SP 800-57 are foundational but bear on no open
   DEC — ARCH-0001 NG3 defers the algorithm suite. They may be a `stub` cluster
   rather than summarised records. This is the largest single scope call open.
2. **Does regulation get summarised or stubbed?** EU CRA and the AI Act drive
   the market analysis (D9) but touch no architectural decision.
3. **Is the ~40 cap right**, given L-011 through L-014 each imply 10+ records?
   Those four tasks alone could exceed it. Either the cap moves or those tasks
   produce stubs.
4. **Paywalled academic work** — record with digest of the abstract page, or
   skip? Affects the trust-management gather (L-014) most.
