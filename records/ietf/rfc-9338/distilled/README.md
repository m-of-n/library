---
record: rfc-9338
kind: index
title: "rfc-9338 — distilled artifacts"
extracted: "2026-10-20"
reviewed_by: ""
---

# `distilled/` — RFC 9338, COSE countersignatures

**FX-1.** `standard: FX-1` is declared in `record.yaml` and **no `profile` is**,
because no `reviewed_by` is signed — `docs/extraction.md`: an unfinished
extraction has no profile at all. **`record.yaml`'s `distillation.passes` is the
only authority for which passes have run and what each found**, and no artifact
here restates the pass count, because a restatement goes stale the moment the
next pass lands and nothing reports it.

| artifact | file | lines | coverage |
|---|---|---:|---|
| normative | `normative.md` | 937 | **38 verbatim regions**, front page and §1–§6 complete plus Appendix A's lead-in **and its terminology list** (lines 619–635, added by pass 2, which found those eight acronym expansions in no artifact), each an exact run of source lines with its range and its own sha256. 419 distinct source lines, no line quoted twice. The only non-heading run of §1–§6 not reproduced is §1's opening IoT/CBOR paragraph (lines 90–101), which carries nothing normative |
| requirements | `requirements.yaml` | 1994 | **140 entries**, R-0001–R-0140, source order, no gaps: **2 stated keywords**, 21 `kind: stated` verbatim fragments, 119 inferred. `source_keyword_count` and `extracted_keyword_count` both **2** and agreeing, with a reconciliation written anyway |
| schema | `schema/` | — | 2 verbatim files, 3 derived, including the `bstr`-slot census that the whole record turns on |
| messages | `messages.yaml` | 601 | 6 structures, 6 `Countersign_structure` fields with byte-level layout, the **8-row derived target-coverage table**, 3 registry actions, 2 byte layouts; 49 requirement ids wired |
| protocol | `protocol.yaml` + `protocol.md` | 345 + 191 | **APPLICABLE** with the boundary measured — 5 roles (4 named in the source), 5 flows, 6 error paths, 5 Mermaid diagrams |
| state machine | `state-machine.yaml` | 266 | **APPLICABLE and deliberately small** — 2 machines, 3 states each, 6 transitions, 2 unbounded self-loops and 1 unreachable state |
| examples | `examples/` | 357 + 6 fixtures | **14 vectors**: the 6 printed messages encoded and size-checked, and 8 derived to-be-signed structures. **One stated size is wrong** |
| design notes | `design-notes.md` | 725 | 12 sections; 3 adopt, 4 adapt, 5 reject; **MD-3 header by header with 5 named cuts**, each naming the `DEC-002` option it affects; all 6 `canonical-encoding` conditions; **7 source defects**; 6 open questions |

## The five results to read first

1. **`other_fields` reaches three of the eight permitted targets, and carries a
   *signature* for exactly one.** The rule §3.3 states for one structure is
   arithmetic on RFC 9052's grammar for the other seven, and
   `schema/bstr-slot-census.derived.txt` carries it out mechanically against
   this library's verbatim capture of that grammar. `COSE_Sign1`, `COSE_Mac` and
   `COSE_Mac0` get `other_fields`; the other five keep **RFC 8152's context
   string**, so the document's only domain separator does not separate the two
   versions of its own algorithm for most targets. And of the three that do get
   it, `COSE_Mac`/`COSE_Mac0` get a **MAC tag**. `messages.yaml`
   `target_coverage`.
2. **A countersignature over a `COSE_Sign` binds no signature at all, and that
   is unconditional.** `signatures : [+ COSE_Signature]` is an array, so the
   `bstr` count never reaches it. `examples/vectors.yaml` V-0007 is the whole
   45-byte to-be-signed structure. This confirms the answer
   `records/ietf/rfc-9052/distilled/design-notes.md` §6 gave its own open
   question 7 on 2026-10-20 — read, **not edited**, and `design-notes.md` §9
   says which limb of it this pass had to narrow.
3. **The headline about `COSE_Signature` is REFUTED as stated and SCOPED.**
   `Countersign_structure.payload` has two available readings, the document
   states neither, and the better-supported one puts the countersigned
   signature value in that slot — so §1 and §3 are reconcilable and the
   Alice/Bob transferability collapses. Both readings were **built, not
   argued**: `examples/vectors.yaml` V-0013, V-0014 and `collisions`.
   `design-notes.md` §3.4.
4. **Appendix A.6.1's stated size is wrong by 20 bytes, and no erratum covers
   it.** *"The size of the binary file is 159 bytes"*, and the message printed
   encodes to **139**. The 20 is exactly the tag head plus A.5.1's `recipients`
   array, and the two preambles are byte-identical runs of source text. Five of
   six sizes reproduce exactly, which is also what validates the encoder.
   `examples/vectors.yaml` V-0006.
5. **Two BCP 14 keywords in 921 lines, and neither is about
   countersignatures.** Every migration obligation — the whole
   backward-compatibility contract of a repair document — is **lowercase**, and
   the deprecation of RFC 8152's labels 7 and 9 is a registry Description-field
   edit with no `MUST NOT` behind it. `requirements.yaml`'s reconciliation names
   each one.

## No `not_applicable` declaration, and both candidate verdicts were measured

Every artifact in FX-1's set is present. The two that are usually N/A for a
format document were measured rather than assumed:

**protocol — APPLICABLE.** §3.3 prints two numbered procedures (four steps and
three) with named inputs, a named intermediate value and a stated precondition,
and §3.1 adds an unbounded recursion. **And there is no exchange**: `verifier`,
`sender`, `receiver`, `exchange`, `handshake`, `negotiate`, `response`,
`server`, `client`, `role`, `flow`, `error`, `reject` and `abort` each occur
**zero** times in the 921 lines; `request` once, in the masthead; `fail` once;
`protocol` five times and not once about this document's own protocol. So the
model is five flows of which **one is empty by measurement** — the standalone
tag-19 form, for which the document specifies no association and no recipient
behaviour.

**state machine — APPLICABLE, and small.** `state` 0, `lifecycle` 0,
`transition` 0, `revoke` 0, `rotate` 0, `expire` 0, `step` 0; `states` once, in
*"United States of America"*. But `finalized` occurs once and it is a **real
guard** on a real transition, §3.1's recursion is a **self-loop with no
termination rule**, and the label 7→11 migration is a lifecycle with **no
terminal state** — nothing in the document ever stops requiring label 7
verification. Two machines, modelled exactly that far and no further.

## Conventions this directory follows

- **Verbatim or nothing.** Every fenced region in `normative.md` was cut from
  `.cache/rfc-9338.txt` by line range by script; all 38 were re-read back and
  **38 of 38** match their claimed range and digest byte for byte. Every
  requirement `text` is a contiguous substring of the whitespace-normalised
  source, verified mechanically — the generator **refuses to write the file** if
  one is not, and it refused three times before this version.
- **A quote audit over every file here.** 167 delimited quotations pulled,
  normalised and resolved whole against the source; 9 listed explicitly as
  quotations of another document or as not quotations at all; **0 unresolved**.
  It found **6 real defects in this pass's own prose** - five quotations whose
  nested quotation marks had been re-punctuated as apostrophes, and one whose leading
  *The* had been lowercased — and **all six** are fixed. The convention now is that
  a verbatim quotation in a `.md` file is written `*"…"*` and **broken at a
  nested quotation mark rather than healed**.
- **And that audit was scoped to `distilled/`, which is where it missed three
  more.** Pass 2 re-ran it over whole spans across `summary.md` and
  `record.yaml` as well: **396 spans graded, 359 verbatim**, and the three
  remaining defects were all in `summary.md` — five nested quotation marks
  re-punctuated as apostrophes in §4's `MUST` and §5.2's registry edit, and one
  lowercased leading *The* in §3.3's `body_protected`. Inside `distilled/`
  the only non-verbatim spans are **four visible `...` elisions and one
  capitalised quotation**, `"the signer structure"` in `messages.yaml`, now lower-cased.
- **One line-break hyphenation, declared and not healed.** The wrap cuts
  `long-term` across source lines 308–309, so §3.1's archiving sentence is
  quoted as *"long- term archiving services"*. The space is the rendering's.
- **Two deliberate duplicate requirement texts.** §3.3 prints its ToBeSigned
  step twice, once per procedure. Both entries exist, same `text`, different
  `object`.
- **No page decoration.** **0 form feeds** and no running headers or footers in
  921 lines, checked with the patterns that match 25 page breaks in RFC 8392's
  rendering. Built with `split("\n")`, never `splitlines()`.
- **Cross-record and own-record ids are emitted from the id table by a
  uniqueness-enforcing selector, never typed.** A join audit then resolves every
  citation back to the requirement text it points at, and the pairs were read.
- **Derived is named `.derived.`**, in the filename and in the header, and the
  verbatim CDDL keeps erratum 7338 intact.

## Errata, stated as what the search returned

Searched 2026-10-20 at `errata.rfc-editor.org/rfc9338` and
`errata.rfc-editor.org/eid7338`. **One erratum: EID 7338**, status *Reported*,
Technical, §3.3, Carsten Bormann, 2023-02-06 — a trailing `/` in the `context`
choice. No Verified, Held-for-Document-Update or Rejected entry is listed. So
the six other defects `design-notes.md` §10 records, including the 20-byte size
error and the two disagreeing permitted-target lists, are **not** in the errata.

## What is not here

**No signature verification.** RFC 9338 prints **no key material of any kind**,
so none of the six examples can be verified from this document alone. The three
ECDSA examples are randomised and could not be reproduced even with keys; the
three EdDSA ones are deterministic and would be. A later pass that wants
verification needs the key set, which lives in RFC 8152's and RFC 9052's
appendices and is not this record's to copy.

**No tag-19 fixture, no label-12 fixture and no detached-payload fixture**,
because the document prints none — and the last of those is the one that would
have forced it to say whether its `bstr` count is by type slot or by wire item.
`detach` and `nil` occur **zero** times.

**No repair of any source defect.** Seven are recorded in `design-notes.md`
§10; the only file that applies one is
`schema/countersign-structure.derived.cddl`, which says so in its header and
carries `.derived.` in its name.
