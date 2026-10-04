---
record: rfc-9804
kind: index
title: "rfc-9804 — distilled artifacts"
extracted: "2026-10-04"
reviewed_by: ""
---

# Distilled artifacts

FX-1 full extraction of **RFC 9804, Simple Public Key Infrastructure (SPKI)
S-Expressions** (Rivest & Eastlake, June 2025, Informational). Source
`.cache/rfc-9804.txt`, sha256 `0db36cc4bb9d…4434`, 1141 lines, read in full
including Appendix A.

**Status: all three passes complete.** `record.yaml` declares
`distillation.profile: full`. `reviewed_by` is empty on every artifact — a
human signs that, and until then these are readable but not buildable-on.

**Why this record exists.** RFC 9804 is DEC-002 **option 1**. The
`canonical-encoding` topic answer of 2026-10-03 named it *"the one remaining
blocker, since option 1 cannot be fairly scored against the six conditions until
it is extracted."* `design-notes.md` §1 does that scoring. Nothing here decides
DEC-002, which is open and is accepted only in an `ADR-NNNN`.

## Artifacts

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 91 verbatim statements and blocks, Abstract through Appendix A, in source order. 8 carry a BCP 14 keyword (12 occurrences); **79 are flagged `_[lowercase/implied]_`**, and 4 carry no keyword and are deliberately unflagged (the §1.4 boilerplate, the §11 IANA non-action, and the two reference lists). The flag density is the finding: 12 keyword occurrences across 1141 lines means almost all binding content here is stated in lowercase. |
| requirements | `requirements.yaml` | 66 entries `R-0001`–`R-0066` in source order. 12 carry a BCP 14 verb and **match the source count exactly** (7 MUST, 2 MAY, 2 RECOMMENDED, 1 OPTIONAL); 54 are lowercase obligations with `verb: none`. One entry, `R-0054`, is `kind: inferred` and declared non-verbatim. `reconciliation` is non-empty and records three things the counts alone do not show. |
| schema | `schema/` | **Three files, all verbatim** — §7.1, §7.2 and §7.3 ABNF, copied unchanged, each with its region sha256 and source line range. Nothing derived. Region digests, verbatim fidelity and rule closure all re-verified in pass 3. |
| messages | `messages.yaml` | 15 structures. Applicability is **partial** and the file says so: RFC 9804 defines no wire messages, headers or envelopes. What is captured is each representation decomposed — the five octet-string forms, the display-hint, the list, the three §6 representation types, the §6.1 brace wrapper, and the three §9.2 in-memory records marked `normative_status: suggestive`. `constrained_by` wired on every field, none empty. |
| protocol | — | **Not applicable**, declared in `record.yaml` with a reason. See below. |
| state-machine | — | **Not applicable**, declared in `record.yaml` with a reason. See below. |
| examples | `examples/vectors.yaml` | **78 vectors**, every example the source prints, across 14 section groups. Pass 1's `vector_count: 99` was a stale estimate and is corrected in `count_reconciliation`. Includes one **source defect**: the §4.6 UTF-8 example does not decode to the string its prose names. |
| design-notes | `design-notes.md` | Option 1 scored against all six `canonical-encoding` conditions; 3 adopt, 4 adapt, 5 reject; a decision mapping across DEC-002, DEC-003, R-M-02, R-O-03, R-O-05, R-M-12/ADR-0001, ARCH-0002 P4 and P5, and D-3; 6 open questions. |

## Two artifacts are not applicable, and the reason is the finding

Both are declared in `record.yaml` with written reasons, and their scaffold
stubs were removed rather than left as files of `TODO`s — the same treatment the
`rfc-8949` record gave the same two kinds.

**`protocol`.** RFC 9804 defines no exchange. There are no roles, no messages
between parties, no error signalling and no processing order anywhere in the
document. It prints no numbered procedure of any kind; §6.3's two numbered items
are a pair of *forms*, not steps.

That absence is load-bearing rather than incidental, which is why it is argued
in `design-notes.md` condition 3 instead of being buried here. §10 is the whole
of the security considerations and **imposes no verification ordering** — no
instruction to parse before verifying, no signature located inside the payload,
no re-serialise-and-compare, and no BCP 14 keyword. Compare RFC 8785 §5, which
*mandates* the ordering R-O-05 forbids, and whose `protocol.md` exists precisely
to hold that contradiction. Option 1 has nothing to hold.

**`state-machine`.** No lifecycle is defined. Nothing in the document registers,
issues, rolls over, expires or revokes; the one stateful process is parsing a
single S-expression, which has no persistent states, triggers or guards.

## What pass 3 checked, and what it changed

Pass 3 ran mechanically wherever a check could be mechanical, and it did change
things — recorded here rather than smoothed over.

**Verified, no change needed:**

1. **BCP 14 counts agree exactly.** `bin/bcp14-count` gives 12 for the source;
   the 66 requirement texts contain 12, in the same keyword breakdown.
2. **Every requirement text is verbatim.** All 65 `kind: stated` texts are
   contiguous substrings of the source under whitespace-normalised comparison.
   `R-0054` is `kind: inferred` and declared non-verbatim.
3. **Every declared `verb` appears in its own text.** Zero mismatches.
4. **All three ABNF region digests match**, and each region appears in the
   source at the line range its header claims, byte for byte.
5. **The ABNF closes.** 27 rules across the three files, no undefined references
   remaining, and **no rule name collides with an RFC 5234 core rule** — the
   defect class that bit RFC 8785, absent here.
6. **All §9.2 length fields verified by addition.** `0x000d` = 13, inner
   `0x0005` = 5, outer `0x001b` = 27. All consistent.
7. **`SEXP-63-02` base-64 round-trips** to `(1:a1:b1:c)` exactly.
8. **Cross-references resolve.** Every `same_sexp_as` target exists; every
   `constrained_by` id in `messages.yaml` is a real `R-NNNN`.

**Changed by pass 3:**

9. **The examples set was finished.** Pass 1 stopped after 7 vectors while
   referring forward to ids it had not written. 71 vectors added, total 78.
10. **`vector_count` corrected** from 99 to 78, with the enumeration recorded.
11. **A source defect found and recorded** — §4.6's UTF-8 display-hint example
    prints `\xC3\xB7` (U+00F7 DIVISION SIGN) where its prose says *ö* (U+00F6,
    `\xC3\xB6`), so the example decodes to `b÷b☺` and not `böb☺`. Found by
    decoding, not by reading. `examples/README.md` holds the detail.
12. **A verbatim-fidelity convention was made explicit.** The RFC hyphenates
    already-hyphenated words across line breaks (`octet-` / `strings`), so
    unwrapping must rejoin them with **no** space. Two entries, `R-0002` and
    `R-0065`, are verbatim only under that rule; `requirements.yaml`'s `note`
    now states it.
13. **`protocol` and `state-machine` declared not-applicable** and their stubs
    removed.

**Known gaps, stated rather than hidden:**

- `reviewed_by` is empty throughout. No human has signed any artifact.
- No vector has been round-tripped through an implementation — there is none
  here. Canonical forms under `derived:` were produced by applying §6.2 by hand
  and are marked `in_source: false`.
- `design-notes.md` open question 1 is the real one: whether the ARCH-0001 §4
  type model survives mapping onto octet-strings-and-lists without losing
  injectivity cannot be answered from this document, because the format defines
  no integers, maps or booleans to map onto. That needs the DEC-002 acceptance
  test, not another reading of RFC 9804.
