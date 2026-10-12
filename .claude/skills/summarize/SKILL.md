---
name: Summarise a reference
description: Use when a library record has been read and needs its summary.md written — the primary human- and AI-facing document for every record.
---

# Summarise a reference

`summary.md` is the **primary** document for a record and the one a human
reviews. Write it first. `schema/summary.template.md` is the shape.
Extraction is a different job — it produces `distilled/`, and it is the
`extract` skill (FX-1, `docs/extraction.md`). Summarising never owes it.

Sections, all of them:

1. **Bibliographic header** — type, maturity, authors, date, identifier,
   source URL, digest. Enough to cite the document without opening it.
2. **Overview** — two to five sentences on the *argument*. "Registers signed
   statements with a transparency service so a relying party can check
   inclusion without trusting the issuer" beats "Section 4 defines the
   architecture."
3. **Applicability** — rate security, cryptography, and this project as
   `core` / `adjacent` / `none`, each with a one-line why. Name the `DEC-*` or
   `R-*`, or say plainly it bears on none yet.
4. **Implementations** — open source and commercial, what we could build on.
   *"Searched, none found on YYYY-MM-DD"* is a result; an empty section with no
   date is not.
5. **Artifacts in this record** — every other file in the directory and what it
   is for. The reviewer should not have to `ls`.
6. **Limits** — what it does not settle. Nothing here means it was not read
   critically.

Rules:

- **YAML front matter on every markdown file** in a record. OKF alignment;
  `bin/validate` enforces it.
- **`maturity`: do not guess.** RFC 2026 levels — `standard`, `best-practice`,
  `informational`, `experimental`, `historic`. Leave it unset rather than
  assert standing you did not check. An RFC being an RFC does not make it a
  standard.
- **Attribute by locator, not by transcription.** Cite the section —
  §5.1.1.1 — and let the reader open the source. Never paraphrase a normative
  sentence into `summary.md` as if it were ours: paraphrase is how a MUST
  silently becomes a SHOULD. Verbatim normative text belongs in
  `distilled/normative.md` under FX-1, with its locator, where the verbatim
  check can reach it. There is no `quotes.md` — retired 2026-10-09,
  `docs/construction.md` decision 6.
- **Say what the record does NOT have, and why.** Close *Artifacts in this
  record* with the absences and what would trigger them — see
  `records/ietf/rfc-9943/summary.md`. An unstated absence reads as an
  oversight; a stated one is a judgement a reviewer can check.
- **Disagree in writing.** If the source is wrong or contradicts another
  record, say so and set `contradicts`. Agreement is cheap; a recorded
  disagreement is what makes the library worth keeping.
- Prefer a controlled tag from `schema/tags.yaml` — subject and role — when one
  fits. `body` is not a tag; who published the document is `publisher`, and its
  standing is `maturity` (`docs/scope.md` §4).
- `status: summarized` only when all six sections are real. CI rejects
  template text left in place.

Four honest paragraphs beat two pages of restatement. If the document bears on
nothing yet, say that in one line and leave it `status: stub` — that is a
legitimate record, not a failure.
