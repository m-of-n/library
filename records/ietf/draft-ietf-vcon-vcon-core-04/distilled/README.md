---
schema: "library-distilled-index/v1"
record: draft-ietf-vcon-vcon-core-04
type: distilled-index
updated: "2026-10-14"
---

# Distilled artifacts — vCon core `-04`

**`distillation.profile: full` against FX-1** (`docs/extraction.md`). Source
pinned at sha256 `cc2a2cb5…033cd722`, 8904 lines, never committed.

| artifact | kind | covers | reviewed |
|---|---|---|---|
| `normative.md` | normative | **202 blocks**, §1–§7 complete, source order. All 169 body BCP 14 occurrences | ✓ |
| `requirements.yaml` | requirements | **251 entries** `R-0001`–`R-0251`, 169 keywords reconciled against the source's 216 | ✓ |
| `fields.yaml` | fields | **106 rows**, 15 objects — reconciled against the draft's own IANA registries | ✓ |
| `schema/vcon.schema.json` | schema | **Appendix B verbatim**, src 6742–8352 | ✓ |
| `schema/types.cddl` | schema | **Appendix C verbatim**, src 8363–8839 | ✓ |
| `schema/vcon.derived.schema.json` | schema | Appendix B made parseable — see below | ✓ |
| `schema/types.derived.cddl` | schema | ours, `bin/derive` from `fields.yaml` | ✓ |
| `messages.yaml` | messages | **28 structures, 187 fields**, 451 requirement links | ✓ |
| `protocol.yaml` · `protocol.md` | protocol | **5 flows**, 5 Mermaid diagrams, `applicability: partial` | ✓ |
| `state-machine.yaml` | state-machine | **3 machines, 20 transitions** | ✓ |
| `examples/` | examples | **12 fixtures**, 108 checks, Appendix A | ✓ |
| `design-notes.md` | design-notes | 7 adopt / 6 adapt / 9 reject, 20 open questions | ✓ |
| `code/types.py` · `code/types.rs` | code | ours, `bin/derive` from `fields.yaml` | ✓ |

## Reading order

`normative.md` → `requirements.yaml` → `design-notes.md`. The first two are
what an implementer builds from; the third is what *we* build from.

For the data model, read **`schema/vcon.schema.json`** (Appendix B) over our
`types.derived.cddl` — it is the draft's own and it is stronger. Appendix B
covers **§4 only**: it is titled *"vCon - Unsigned Form"*. For §5's signed and
encrypted forms, `types.cddl` (Appendix C) is the only schema the draft has.

## Verbatim is not a claim, it is a digest

Every verbatim artifact records its sha256 and source line range. All of them
were **re-derived byte-exactly by an agent that did not produce them**, and the
twelve example fixtures were re-derived by an independently written
implementation of the de-wrapping rule — 833 rejoins, zero anomalies.

The strongest check is cryptographic rather than textual: **A.6's RS256
signature verifies** under `openssl` against the RSA-2048 key in its own
`x5c[0]`, and its payload decodes to a document equal to the A.4 fixture. One
wrong character in 7595 breaks both, so the de-furnishing is confirmed from
outside the extraction.

## Generated artifacts are never hand-edited

`types.derived.cddl`, `types.py` and `types.rs` come from `fields.yaml` via
`bin/derive`. A defect in the field table propagates into all three — which is
the point of recording `generated_from`: a fix reaches everything.

`bin/derive` carries two guards added by this extraction, both after near
misses. It writes `schema/types.derived.cddl`, never `schema/types.cddl` —
that path holds **Appendix C verbatim**, and the old behaviour would have
destroyed 413 lines of the source's own bytes. And it **refuses** to overwrite
a `requirements.yaml` that does not carry its own generation banner: under FX-1
that file is a primary artifact read out of the source, and regenerating it
from the field table would have replaced 251 entries with 34.

## What these artifacts deliberately do not express

- **Structural validity is not conformance.** Which Dialog parameters apply
  depends on `Dialog.type` (§4.3.1.6). Table 1 is **120 cells**: both
  appendices express its `M` and `X` cells, **neither expresses `S`, `SN` or
  `-`** — and Appendix C additionally **conflates `SN` with `X`**, so a reader
  reconstructing Table 1 from the CDDL reads four SHOULD NOTs as MUST NOTs.
  A reader gets a different specification depending on which appendix they
  picked up, and neither says so except in a comment.
- **A MUST on a field's *value* is not a MUST on its *presence*.** `vcon`
  (§4.1.1) carries a MUST constraining its value yet is deprecated.
- **Cross-field and cross-object constraints.** `Dialog.parties` indexes into
  the top-level `parties` array and nothing range-checks it anywhere.
- **SHOULD-level content.** `SHOULD` outnumbers `MUST` **97 to 65** in this
  document, and Appendix B says outright: *"SHOULD-level statements are not
  enforced by this schema."*

## Source defects — the draft's, not ours

Recorded where they were found; `design-notes.md` §6 holds the full list.

- **Appendix B is not valid JSON.** 89 line breaks fall inside string
  literals; **25 eat a word space irrecoverably** (`"RFC3339format"`,
  `"isstored"`). All 89 are inside `description` or `$comment`, so the
  schema's *meaning* survives. `vcon.derived.schema.json` is the parseable
  rendering, with the run-together words left visible.
- **One uuid names four documents** in Appendix A, and the reference is
  ambiguous between **two distinct contents** — in the appendix demonstrating
  the version chain that depends on it.
- **The worked redaction fails in both directions.** A.8 turns `"Okay."` into
  `"{{US_STATE}}"` twice while **"Bob" and "Alice" survive** in the
  transcript, and re-tokenizes, which is none of the three operations §4.1.8
  permits.
- **A.6 and A.7 violate JOSE header disjointness** (RFC 7515/7516 §7.2.1), and
  A.7 fails the draft's **own** CDDL.
- **The integrity machinery is mandatory to construct and optional to use.**
  Every BCP 14 obligation on `content_hash` is about carriage; the only
  instruction to verify (§5.1) is lowercase *and* names a `signature`
  parameter §7.3 folded away three syntax versions earlier.
- **An unresolved editorial marker** sits at source line 6725 in a **-04 WG
  draft**. Described here, never reproduced — `bin/validate` rejects that
  string anywhere under `distilled/`.

## Review state

**FX-1 pass 4 is complete.** All eleven artifacts are signed
`reviewed_by: "nfnewbury 2026-10-14"`, so this record is **buildable-on**.

Passes 1–3 are recorded in `record.yaml` under `distillation.passes` and were
run by agents. Pass 4 is the separate human check, and it is the one pass no
agent can run — three artifacts were found carrying
`reviewed_by: "pass 2, adversarial verifier"` at signing time, which is an
agent writing itself into the field that attests a person read the work. That
is what `distillation.passes` is for; `reviewed_by` means a human.

What the signature does **not** cover: the draft's own defects, which are the
WG's; the open questions in `design-notes.md` §6, which are recorded and not
resolved; and whether we adopt any of it, which is ARCH/DEC work in `mofn`.
