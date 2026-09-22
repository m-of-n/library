---
schema: "library-doc/v1"
id: distillation
title: "Distillation procedure — extracting formats and field definitions repeatably"
type: policy
status: draft
version: "0.1.0"
updated: "2026-09-22"
needs_review: true
reviewed: false
source: "library#9; first applied to draft-ietf-vcon-vcon-core-04"
---

# Distillation procedure

**Goal:** a compacted form an implementer can build from **without re-reading
the source**, plus field definitions in a machine-usable shape.

`docs/requirements.md` defines *what a requirement is*. This is the procedure.

---

## 1. Convert

Fetch the **text** form where one exists (IETF `.txt` beats PDF). Then strip:

- running heads and feet (`^Author\s+Expires`, `^Internet-Draft\s+<title>`)
- form feeds, page numbers
- repeated boilerplate, table of contents

**Keep section numbering.** Every extracted field needs a locator and **pages do
not survive conversion**. Keep tables — they carry normative content more often
than prose does.

## 2. Measure before you cut

Count normative verbs in the source *first*:

```sh
grep -oE '\b(MUST NOT|SHALL NOT|SHOULD NOT|MUST|SHALL|SHOULD|MAY|REQUIRED|RECOMMENDED|OPTIONAL)\b' clean.txt | sort | uniq -c
```

Record the counts in the distillation. **A distillation that loses any of them
has failed**, and you cannot tell without the baseline.

## 3. Extract by object, and state coverage per object

One `requirements/fields.yaml` entry per field: `object`, `field`, `json_type`,
`cardinality`, `required`, `verb`, `locator`, `text` (verbatim), `semantics`,
`kind` (`stated`|`inferred`), `testable`.

**Mark uncovered objects `pending` explicitly.** A partial extraction that says
so is usable; one that pretends to be complete is not.

## 4. Review — three mechanical checks, then a human

Run all three. On the first real distillation they found **five defects**.

1. **Verbatim check** — every `text:` value must appear in the source with
   whitespace normalised. Catches paraphrase drift.
2. **Coverage check** — every subsection of the object's section must be cited
   by at least one entry. Catches silent omission.
3. **Verb check** — for each cited section, if the source body contains MUST,
   the extracted `verb` must be MUST. **Catches the dominant failure: a
   normative statement sitting in prose rather than in the field bullet.**

Then a human confirms `kind: inferred` is honest and sets `reviewed_by`.

### Two rules the checks exist to enforce

- **Never weaken a verb.** Four of the five first-pass defects were dropped
  MUSTs — all of them in prose rather than in the field bullet. Read the whole
  section body, not the definition line.
- **Verbatim is not enough; preserve contiguity.** Two true quotes joined
  assert an adjacency the source may not have. Keep them as separate fields.

## 5. Use the extractor, then correct it

`bin/extract-fields <clean.txt> <Object> <section-prefix>` produces a first
pass: one entry per subsection, with the JSON type from the `*  name: "Type"`
declaration and **the strongest normative verb found anywhere in the section
body** — which is the dropped-MUST lesson mechanised.

**It cannot judge semantics, and it will make structural mistakes.** On vCon it
treated the five `Dialog.type` *values* as fields, because an enumerated value
and a field definition have the same shape in an IETF draft. **A tool that reads
structure cannot tell a value from a field.** Two legitimate fields were also
nearly lost by a filter that dropped anything without hand-written semantics —
absence of semantics is not evidence of not being a field.

Record every correction in `extraction_notes`. The corrections are how the next
person knows what to check.

## 6. Record what the review found

In the distillation itself, with the defects named. A review that found nothing
and says nothing is indistinguishable from a review that did not run.

## 7. Done when

- `reviewed_by` is set — **empty means readable but unusable**
- Coverage stated per object
- Verb counts recorded
- The three checks pass and their result is written down

## 8. The test of this document

**A second person distils a different specification from this alone.** Until
that has happened, this is a description of one run, not a procedure.
