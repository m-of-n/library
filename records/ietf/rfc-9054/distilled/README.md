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
<!-- `lines` is `len(text.split("\n"))`, i.e. one more than `wc -l`, measured
     by pass 2 on 2026-10-21. The `examples/` row read 431 under pass 1 and
     matched nothing measurable; it is now vectors.yaml under the same rule. -->
| normative | `normative.md` | 654 | 25 verbatim regions, §1–§5 complete, each with its line range and sha256 |
| requirements | `requirements.yaml` | 1216 | 96 entries, R-0001–R-0096; **2 stated**, 94 inferred; counts agree at 2 |
| schema | `schema/` | — | 7 files: 2 verbatim, 4 derived (one of them the parse report), 1 README |
| messages | `messages.yaml` | 453 | 4 structures, 16 fields, 28 requirement ids wired |
| protocol | `protocol.yaml` + `protocol.md` | 93 + 88 | **NOT APPLICABLE**, measured — see below |
| state machine | `state-machine.yaml` | 80 | **NOT APPLICABLE**, measured — see below |
| examples | `examples/vectors.yaml` | 555 | 8 vectors: 1 printed, 6 computed, 1 census |
| design notes | `design-notes.md` | 653 | 13 sections; MD-3 mapped with 4 cuts and 1 convergence; 9 source defects |

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

- **Verbatim or nothing, with one stated exception.** Every quotation and
  fenced region was cut from `.cache/rfc-9054.txt` by line range by script:
  96 of 96 requirement texts are contiguous substrings of the
  whitespace-normalised source, and a terminator check found 23 over-running
  spans, all tightened. **Pass 2 re-measured the design-note quotations and
  pass 1's "20 of 20 … 0 failures" does not hold.** 20 spans in
  `design-notes.md` do resolve in a cached source, but one of them — §3.2's
  NOTE — resolves only once the **source's own `|` box margin** is removed: the
  normalised source reads `to 64 bits | defined in this specification`, and
  `requirements.yaml` R-0065 keeps that `|` while the prose drops it. **Eight
  quotations in this record join across that margin**, one each in
  `design-notes.md`, `examples/README.md`, `schema/hash-algorithms.derived.yaml`
  and `summary.md` and two each in `examples/vectors.yaml` and `messages.yaml`;
  and **three quote Table 2's Description cell** for `-17`
  (*"SHA-2 512-bit Hash truncated to 256-bits"*, in `design-notes.md` and twice
  in `examples/vectors.yaml`), which is a cell **read down a column** and is
  contiguous in no reading of the table — each of the three now says so. Both
  are legible renderings of what the source says; neither is a contiguous span,
  and that is the rule this directory actually keeps.
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
that is mostly prevented here: every cross-record citation in both records is
spelled in full (`rfc-9054#R-0087`) and every one was **emitted from the other
record's id table by a uniqueness-enforcing predicate** rather than typed. Pass
1 claimed the bare form of a colliding number is "written nowhere"; **pass 2
found one place** — the comment at `rfc-9360/distilled/messages.yaml:300` names
`R-0068` and `R-0087` bare, in order to say that rfc-9360 defines its own. It is
unambiguous in context and is left as it is, recorded here rather than covered by
a blanket. Otherwise the bare forms are in each record's own
`requirements.yaml` reconciliation and its own `README.md`.

A lane-wide **join audit** resolved every record-qualified citation in both
records to the requirement or vector it points at and printed the pairs for
reading. The count depends entirely on its scope, so the method is stated:
`bin/check-id-joins --resolve` resolves **587 citation occurrences** across
the two records with **0 dangling** — 501 distinct file/id pairs — of which
**19 occurrences at 18 distinct file/id sites are cross-record**. Measured on
the state at the end of pass 2, including the citations pass 2's own notes
added: the first number this paragraph carried (585) was already stale by the
time the notes were written, which is the hazard in miniature. Pass 1's "271
citations, 14 cross-record" is the same audit counted as distinct file/id pairs
with `requirements.yaml` and these two `README.md`s excluded — 273 and 16 under
that scoping now, and a different number under any other. Pass 2 then read
every cross-record pair and every citation of an id in a duplicate-text group —
the only places a wrong id still matches the quoted words — and **0 resolve to a
statement other than the one meant**: in `rfc-9054` the per-algorithm citations
discriminate §3.2's capabilities sentence (`R-0066`) from §3.3's (`R-0077`)
correctly in all 7 places, and in `rfc-9360` the `x5bag` field cites the x5bag
member of every duplicate pair and the `x5chain` field the x5chain member.

## What is not here

No digest-carrier fixture, because **there is no carrier**: §1 says COSE
defines none and that *"This omission was intentional"*. A fixture for our own
carrier belongs with our own carrier. And no reproduction of a printed digest,
because the document prints **none** — for any of the eight algorithms it
registers, including the one it defines itself.
