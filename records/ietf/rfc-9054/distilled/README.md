---
record: rfc-9054
kind: index
title: "rfc-9054 — distilled artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# `distilled/` — RFC 9054, COSE hash algorithms

**FX-1 pass 1 (extract) only.** `standard: FX-1` is declared in `record.yaml`
and **no `profile` is**: passes 2 (verify) and 3 (cross-check) have not run and
no `reviewed_by` is signed.

| artifact | file | lines | coverage |
|---|---|---:|---|
| normative | `normative.md` | 652 | 25 verbatim regions, §1–§5 complete, each with its line range and sha256 |
| requirements | `requirements.yaml` | 1214 | 96 entries, R-0001–R-0096; **2 stated**, 94 inferred; counts agree at 2 |
| schema | `schema/` | — | 2 verbatim files, 3 derived, plus the parse report |
| messages | `messages.yaml` | 453 | 4 structures, 16 fields, 28 requirement ids wired |
| protocol | `protocol.yaml` + `protocol.md` | 93 + 88 | **NOT APPLICABLE**, measured — see below |
| state machine | `state-machine.yaml` | 80 | **NOT APPLICABLE**, measured — see below |
| examples | `examples/` | 431 | 8 vectors: 1 printed, 6 computed, 1 census |
| design notes | `design-notes.md` | 648 | 13 sections; MD-3 mapped with 4 cuts and 1 convergence; 9 source defects |

## The three results to read first

1. **`COSE_Hash_V` parses — and that refutes this record's own summary.** The
   summary says *"the fragment does not parse"*. It parses, as a group of **24
   entries instead of 4**, because `#` is CDDL's tag operator: each `#` is read
   as the "any" type and each comment word after it as a bare type reference,
   15 of them distinct. A tool rejects the file at **name resolution**, not at
   syntax. The defect is real and the stated mechanism is not the mechanism.
   And the worse defect is the one no erratum covers: **even repaired it is a
   group, not a type**, so RFC 8610 §2.2.4 forbids it as a root and the
   document supplies no wrapper. `schema/cddl-parse.derived.txt`.
2. **§4.1's own size rationale is backwards for five of eight allocations.**
   It says a "two-byte algorithm identifier seems reasonable" and that for
   SHA-1 "a longer algorithm identifier is appropriate" — but −14 to −18 each
   cost **one** CBOR octet, and SHA-1 at −14 is in the shortest class available
   while SHA-384 at −43 costs two. `examples/vectors.yaml` V-0001. **No
   erratum covers it**; the only erratum on this RFC is 7335, on §2.1.
3. **§3.2 registers a 64-bit truncation *because of* `rfc-9360`, and
   `rfc-9360` then makes it a binding.** §3.2's safety argument is that a false
   positive is caught by testing the public key — `rfc-9360` §2's recommended
   configuration has no such test for the certificate's identity.
   `design-notes.md` §4.1 is the chain, and neither document states it alone.

## The two `not_applicable` verdicts, measured

Both are recorded in `record.yaml` under `distillation.not_applicable` with the
same counts the files carry.

**protocol.** `sender`, `recipient`, `receiver`, `verifier`, `exchange`,
`handshake`, `negotiate`, `response`, `server`, `client`, `retrieve`, `GET`,
`intermediary` and "relying party" each occur **zero** times. `protocol` occurs
**once**, at line 148, in *"SHOULD trigger protocol maintainers"*; `party`
once, at line 403, in *"a third party"*; `verify` once, at line 162; `request`
once, at line 6, in the masthead. §1's indirect-signing paradigm is the closest
thing to a flow and it names no parties, no messages and no error path.
Contrast `rfc-9360` in the same lane, which is **applicable** — four parties, a
GET with a transport `SHOULD`, an active intermediary and a two-check join. The
split is in the documents.

**state machine.** `state`, `lifecycle`, `transition`, `revoke`, `revocation`,
`rotate`, `rotation`, `expire`, `expiry`, `expiration`, `issue`, `issuance`,
`enroll`, `step`, `steps` and `order` each occur **zero** times — and both
occurrences of `states` are *"United States"*. An algorithm identifier has no
lifecycle. The progression the document gestures at (sound → theoretically
attacked → practically attacked → Filter Only → unusable) has **not one of its
steps defined**, so a machine over it would be ours entirely.

## Conventions this directory follows

- **Verbatim or nothing.** Every quotation and fenced region was cut from
  `.cache/rfc-9054.txt` by line range by script and verified as a contiguous
  substring of the whitespace-normalised source: 96 of 96 requirement texts and
  20 of 20 design-note quotations. A terminator check found 23 over-running
  spans and all were tightened.
- **No page decoration.** Zero form feeds, no running headers or footers, in
  498 lines. Built with `split("\n")`.
- **The source's own emphasis is not edited away.** §3.2 writes `*SHA-256/64*`;
  R-0057's text begins `SHA-256/64* provides` because the cut starts inside the
  emphasis. **That trailing asterisk is the source's.**
- **Cross-record ids are spelled in full and emitted from the id table**, with
  a uniqueness-enforcing selector and a join audit read before acceptance.

## The nine expected `bin/validate` warnings

`bin/validate` reports **nine warnings** across these two records and **no
errors**. All nine are the same warning, and it is the one introduced for this
effort:

```
cites rfc-9054#R-0087 while defining its own R-0087 — a bare 'R-0087' in prose
resolves two ways
```

They are **unavoidable for this lane and are the price of the cross-record
evidence.** `rfc-9360` holds 129 requirements numbered `R-0001`–`R-0129` and
`rfc-9054` holds 96 numbered `R-0001`–`R-0096`, so *every* id in the smaller
range exists in both records, and any citation across the two collides by
construction. The check is a warning rather than an error for exactly this
reason.

What the warning actually guards against is a **bare** `R-NNNN` in prose, and
that is prevented here rather than tolerated: every cross-record citation in
both records is spelled in full (`rfc-9054#R-0087`), every one was **emitted
from the other record's id table by a uniqueness-enforcing predicate** rather
than typed, and the bare form of a colliding number is written nowhere. The
only bare `R-NNNN` forms in either record are inside that record's own
`requirements.yaml` reconciliation and its own `README.md`, where the record is
unambiguous.

A lane-wide **join audit** resolved all 271 citations across both records to the
requirement texts they point at and printed the pairs for reading: **0 dangling,
14 cross-record, 0 resolving to a different statement than intended.** That
audit is the real guard — the warning only tells you the numbers overlap.

## What is not here

No digest-carrier fixture, because **there is no carrier**: §1 says COSE
defines none and that *"This omission was intentional"*. A fixture for our own
carrier belongs with our own carrier. And no reproduction of a printed digest,
because the document prints **none** — for any of the eight algorithms it
registers, including the one it defines itself.
