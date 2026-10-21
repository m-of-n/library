---
record: rfc-9360
kind: index
title: "rfc-9360 — distilled artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# `distilled/` — RFC 9360, COSE header parameters for X.509 certificates

**FX-1 pass 1 (extract) only.** `standard: FX-1` is declared in `record.yaml`
and **no `profile` is**: passes 2 (verify) and 3 (cross-check) have not run and
no `reviewed_by` is signed. Under `docs/extraction.md` an unfinished extraction
has no profile at all, and that is this record's state.

| artifact | file | lines | coverage |
|---|---|---:|---|
| normative | `normative.md` | 811 | 29 verbatim regions, §1–§5 complete, each with its line range and sha256 |
| requirements | `requirements.yaml` | 1600 | 129 entries, R-0001–R-0129; 14 stated, 115 inferred; counts agree at 14 |
| schema | `schema/` | — | 1 verbatim CDDL file, 1 verbatim source-rendering file, 4 derived |
| messages | `messages.yaml` | 562 | 6 structures, 19 fields, 74 requirement ids wired |
| protocol | `protocol.yaml` + `protocol.md` | 409 + 139 | **APPLICABLE**: 3 flows, 18 steps, 5 error paths, 6 roles |
| state machine | `state-machine.yaml` | 220 | **APPLICABLE**: 2 machines, 9 states, 9 transitions (1 forbidden) |
| examples | `examples/` | 430 | 8 vectors, **every one computed** — the source prints none |
| design notes | `design-notes.md` | 694 | 15 sections; MD-3 mapped header by header with 5 cuts; 9 source defects |

## The three results to read first

1. **§5's last paragraph contradicts §5's eighth, and they are adjacent.**
   Paragraph 8 says protecting `x5bag`, `x5chain` **and `x5t`** in the protected
   bucket mitigates a misbehaving CA; paragraph 9 says the security of `x5t`'s
   algorithm does not affect the security of the system. The record's own
   summary located the contradiction in "§5's own next paragraph" — **that is
   corrected here**: §5 has nine paragraphs, the `x5t` claim is the ninth and
   last, the identity-misbinding attack is the third, and the real neighbour is
   a sharper citation than the one claimed. `design-notes.md` §2.1.
2. **A filtering `x5t` and a binding `x5t` are the same 25 octets.**
   `examples/vectors.yaml` V-0004, as an identity rather than an inference:
   `COSE_CertHash` has exactly two fields, `rfc-9054`'s `Filter Only` is a
   registry column, and RFC 9360 restricts `hashAlg` to no subset of the
   registry. V-0006 then executes §2's own recommended configuration and shows
   the protected bucket's bytes are **identical** across an intermediary
   rewrite, so the digest comparison is the whole binding.
3. **`kid` occurs zero times in 614 lines.** Four ways to identify a key, none
   of them COSE's own key identifier, so `R-O-01` is unsatisfiable *from the
   message* without a rule we write — and option 1 of `DEC-002` cannot have
   this hole at all, because it has no separate identifier field.
   `design-notes.md` §3 and Cut 5.

## Conventions this directory follows

- **Verbatim or nothing.** Every quotation and every fenced region was cut from
  `.cache/rfc-9360.txt` by line range **by script**, never retyped, and
  verified mechanically as a contiguous substring of the whitespace-normalised
  source. 129 of 129 requirement texts and 15 of 15 design-note quotations
  passed; a terminator check found 26 spans that ran into the next sentence and
  every one was tightened before the files were written.
- **No page decoration anywhere.** This rendering has **zero** form feeds and
  no running headers or footers in its 614 lines — checked with the same
  patterns that match 25 page breaks in RFC 8392 — so no region is split and
  nothing is welded across a gap. Built with `split("\n")`, never
  `splitlines()`.
- **Hyphenation is not healed.** The source wraps `DER-encoded` across lines
  222–223; `requirements.yaml` R-0042 carries `DER- encoded certificate`
  exactly as the normalised source does.
- **`.derived.` on everything we wrote.** `schema/README.md` lists which files
  are which.
- **Cross-record ids are spelled in full and emitted from the id table.** Every
  `constrained_by` entry was selected out of `requirements.yaml` by a predicate
  on that entry's own locator, object and field, by script, and the selection
  refuses to resolve unless it is unique. A join audit resolving each cited id
  to its requirement's own text was read before these files were accepted.

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

No end-to-end COSE fixture, because **the source prints no example at all** —
`Figure`, `Appendix`, `vector` and "test vector" are each at zero. A real
fixture needs a certificate, a key, a signature and RFC 9052's machinery; the
honest ceiling for pass 1 is conformance and cost, which is what
`examples/` carries. `examples/README.md` says what a later pass would have to
build and against what.
