---
record: rfc-9597
kind: examples
title: "rfc-9597 — examples and test vectors"
extracted: "2026-10-20"
reviewed_by: ""
---

# Not applicable, and the absence is the finding

**RFC 9597 prints not one byte.** No hex, no CBOR diagnostic notation, no
figure, no complete COSE object, no worked example of any kind.

Measured over all 265 lines of `.cache/rfc-9597.txt`, whole-word and
case-insensitive:

| token | occurrences |
|---|---|
| `example` | **0** |
| `examples` | **0** |
| `Figure` | **0** |
| `hex` | **0** |
| `vector` / `test vector` | **0** |
| `diagnostic notation` | **0** |

The phrase `use case` occurs **twice in the document and once in §1** — line 22
in the Abstract and line 75 in §1 — and both are prose. *[correction
2026-10-21, pass 3 — cross-check] This read "twice in §1"; the measurement puts
one of the two in the Abstract.* The only structural rendering in the document
is four lines of CDDL that **the document itself declares non-normative**
(`../schema/source-renderings.txt`).

## Why this matters more than it sounds

**Every fixture for label 15 would be ours**, under `R-O-03`'s cite-don't-invent
discipline, and there is nothing here to cite. The contrast inside this one lane
is stark:

| record | printed vectors | verified in pass 1 |
|---|---|---|
| `rfc-8392` | **five complete CWTs**; 19 numbered figures, nine of them in CBOR diagnostic notation | all five — signature, both MAC tags, both decryptions |
| `rfc-9597` | **none** | — |
| `rfc-9596` | **none** | — |

So the base document of the lane supplies reference bytes for the envelope and
**neither of the two header parameters we would actually rely on supplies any.**
A conformance suite for a protected-header `iss` has to be built from RFC 8392's
envelope plus our own construction of label 15, and nothing in the standards
checks our construction.

**The nearest thing to a reference instance found anywhere on 2026-10-20** is
`draft-ietf-scitt-scrapi`'s Signed Statement example, which carries label 15 in
the protected header with `iss` (1) and `sub` (2) nested — a specification, not
a library, and a draft. `records/ietf/rfc-9943` §6 *requires* that shape without
printing it.

*[labelled 2026-10-21, pass 3 — cross-check] Those two claims are not of the
same kind, and this file did not say so. **The `rfc-9943` §6 requirement is
checkable here**: both of its sentences resolve verbatim in
`records/ietf/rfc-9943/distilled/normative.md` and `requirements.yaml`, a
`profile: full` record. **The SCRAPI example is not.** No `.cache/` rendering of
`draft-ietf-scitt-scrapi` is held and that record is a `stub` — no summary, no
artifacts — so the claim rests on pass 1's 2026-10-20 search alone, by one
agent, and carries the same shelf life as `../design-notes.md` §7.6. It is
**unverifiable from this repository.***

`examples` is therefore declared `not_applicable` in `record.yaml` with this
measurement as its reason. This file exists so the measurement is readable from
inside the artifact set, not only from `record.yaml`.
