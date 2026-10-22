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
<!-- `lines` is `len(text.split("\n"))`, i.e. one more than `wc -l`, measured
     by pass 2 on 2026-10-21. The `examples/` row read 430 under pass 1 and
     matched nothing measurable; it is now vectors.yaml under the same rule. -->
| normative | `normative.md` | 812 | 29 verbatim regions, §1–§5 complete, each with its line range and sha256 |
| requirements | `requirements.yaml` | 1600 | 129 entries, R-0001–R-0129; 14 stated, 115 inferred; counts agree at 14 |
| schema | `schema/` | — | 1 verbatim CDDL file, 1 verbatim source-rendering file, 4 derived |
| messages | `messages.yaml` | 562 | 6 structures, 19 fields, 74 requirement ids wired |
| protocol | `protocol.yaml` + `protocol.md` | 415 + 139 | **APPLICABLE**: 3 flows, 18 steps, 5 error paths, 6 roles |
| state machine | `state-machine.yaml` | 220 | **APPLICABLE**: 2 machines, 9 states, 9 transitions (1 forbidden) |
| examples | `examples/vectors.yaml` | 542 | 8 vectors, **every one computed** — the source prints none |
| design notes | `design-notes.md` | 696 | 15 sections; MD-3 mapped header by header with 5 cuts; 9 source defects |

## The three results to read first

1. **§5's last paragraph contradicts §5's eighth, and they are adjacent.**
   Paragraph 8 says protecting `x5bag`, `x5chain` **and `x5t`** in the protected
   bucket mitigates a misbehaving CA; paragraph 9 says the security of `x5t`'s
   algorithm does not affect the security of the system. The record's own
   summary located the contradiction in "§5's own next paragraph" — **that is
   corrected here**: §5 has nine paragraphs, the `x5t` claim is the ninth and
   last, the identity-misbinding attack is the third, and the real neighbour is
   a sharper citation than the one claimed. `design-notes.md` §2.1.
2. **A filtering `x5t` and a binding `x5t` are the same bytes** (23 octets with
   SHA-1; the identity holds for every `hashAlg`).
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
  source. 129 of 129 requirement texts passed; a terminator check found 26
  spans that ran into the next sentence and every one was tightened before the
  files were written. **Pass 2 re-measured the design-note quotations with a
  stated method** rather than repeating pass 1's "15 of 15": taking every span
  between two double quote marks, longest first, 11 of them resolve exactly in
  a cached source (9 in RFC 9360, 2 in RFC 9054) and 0 need a relaxation; three
  further verbatim spans are delimited by single quotes or backticks rather
  than by quote marks. Everything else in quotes in that file is our own prose,
  a `mofn` quotation marked unverifiable, or a quotation of `topics/` or
  `docs/`, which are in this repository and resolve there.
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

No end-to-end COSE fixture, because **the source prints no example at all** —
`Figure`, `Appendix`, `vector` and "test vector" are each at zero. A real
fixture needs a certificate, a key, a signature and RFC 9052's machinery; the
honest ceiling for pass 1 is conformance and cost, which is what
`examples/` carries. `examples/README.md` says what a later pass would have to
build and against what.
