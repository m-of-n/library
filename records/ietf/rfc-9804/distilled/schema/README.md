---
record: rfc-9804
kind: schema
title: "rfc-9804 — schemas"
extracted: "2026-10-04"
reviewed_by: ""
---

# RFC 9804 — schemas

**All three files are verbatim.** RFC 9804 §7 ships its own ABNF (RFC 5234), so
nothing here is derived, inferred or authored by this project. That is unusual
for this library and it is the single most useful thing about this record: the
canonical form of DEC-002 option 1 is *published as a grammar*, not as a list of
encoder obligations.

| file | source | rules | start symbol |
|---|---|---|---|
| `advanced-transport.abnf` | §7.1, source lines 716–773 | 23 | `sexp` |
| `canonical.abnf` | §7.2, source lines 777–779 | 2 | `c-sexp` |
| `basic-transport.abnf` | §7.3, source lines 783–787 | 2 | `b-sexp` |

Each file carries, in its own header, the source digest, the sha256 of the
verbatim region between its `BEGIN`/`END` markers, and the source line range.
The markers are written as ABNF comments so each file stays machine-checkable as
RFC 5234.

## Verification

Checked in pass 3, mechanically, not by reading:

1. **Region digests.** The bytes between the markers hash to the digest each
   file's header claims. All three match.
2. **Verbatim fidelity.** Each region appears in `.cache/rfc-9804.txt` as a
   contiguous run, at the line range the header names. All three match,
   including the RFC's three-space left margin, its continuation-line alignment,
   its inline `;` comments and its internal blank lines.
3. **Rule closure.** Defined-versus-referenced over all three files: 27 rules
   defined, **no undefined references remain**, and **no rule name collides with
   an RFC 5234 Appendix B.1 core rule**.

That last check matters because it is where the RFC 8785 extraction found a real
defect — JCS's derived ABNF named rules `char` and `DIGIT`, and since RFC 5234
§2.1 makes rule names case-insensitive, those *are* the core rules, so a
conforming tool rejects the grammar outright. **RFC 9804 has no equivalent
defect.** Its 27 rule names are disjoint from the 16 core rules. The nine core
rules it uses are `ALPHA`, `CR`, `DIGIT`, `DQUOTE`, `HEXDIG`, `HTAB`, `LF`,
`OCTET` and `SP`.

## Recorded defect — §7.2 and §7.3 are not self-contained

This is the one finding, and the files record it rather than repairing it.

- `canonical.abnf` (§7.2) references `verbatim`, which is defined only in §7.1.
  `verbatim` in turn pulls in `decimal` and the `OCTET` core rule. An ABNF tool
  fed §7.2 alone reports **one** undefined rule.
- `basic-transport.abnf` (§7.3) references `c-sexp` (§7.2) and `whitespace`,
  `base-64-chars` and `base-64-end` (§7.1). Fed alone it reports **four**
  undefined rules.

This is the RFC's own structure, not a transcription error: §7 says *"The ABNF
for advanced representation of S-expressions is given first, and the basic and
canonical forms are derived therefrom."* Nothing has been added to close it, per
the FX-1 rule that a source defect is recorded and never papered over.

**It has one practical consequence for us,** carried into `design-notes.md` open
question 6. `design-notes.md` §3 proposes adopting the §7.2 grammar as the only
accepted decode grammar for signed bytes. If that is written down, the citation
must be *§7.2 together with the `verbatim`, `decimal` and `OCTET` rules it
depends on* — not §7.2 alone, which does not define a language by itself. Under
R-O-03, which requires a canonicalisation algorithm to be cited rather than
silently invented, citing an open grammar would be citing an incomplete
algorithm.

## What is not here, and why

**No CDDL, no JSON Schema, no ASN.1.** RFC 9804 defines none, and none is
derived here. The ABNF is the complete formal description the document gives of
every representation, and a derived schema in another language would add nothing
but a second thing to keep in sync.

**No schema for the §9 in-memory layouts.** §9 calls them *"only sketched here,
as they are only suggestive"*, and R-0063 confirms the wire forms are independent
of the implementation-chosen width `k`. Their byte layouts are captured in
`messages.yaml` as structures marked `normative_status: suggestive`, which is the
right level: exact enough to test an implementation against §9.2's worked bytes,
and clearly marked as interoperating with nothing.

**No ABNF for the §3 character repertoire.** §3's alphabetic, numeric,
pseudo-alphabetic, reserved-punctuation and unused-character classes are
enumerated in prose and are already enforced where they bite — `simple-punc`,
`printable`, `token` and `base-64-char` in §7.1 all encode the relevant subset.
The one class with no grammar production is the "unused and unavailable" set
(`!  %  ^  ~  ;  '  ,  <  >  ?`, R-0007), and it needs none: those characters are
excluded by not appearing in any production, which is also why they remain legal
inside `verbatim` and `quoted-string`, exactly as §3 says.
