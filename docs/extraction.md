# Full extraction standard (FX-1)

**Status: normative for this library from 2026-09-28.** Applies to every
record of type `rfc`, `draft`, `spec` or `ietf` that a pull request touches.
Older records are grandfathered until someone works on them.

## Why

A summary tells a person what a document is about. It cannot drive an
implementation or a test. This library exists to feed a specification and its
test suite, so for every protocol or format document we hold, the goal is to
extract **everything an implementer would otherwise have to re-read the source
to find** — in forms a program can consume.

Summaries-only is not a finished record. It is a started one.

## The artifact set

Every in-scope record ends with `distillation.profile: full` and **all** of
these in `distilled/`. An artifact may be declared not applicable only with a
written reason in `distillation.not_applicable` — never silently omitted.

| kind | file | what it is | N/A allowed? |
|---|---|---|---|
| **summary + labels** | `summary.md`, record `tags`, `bears_on`, `topic` | what it is, why we hold it, what it bears on | **no** |
| **normative** | `distilled/normative.md` | every normative statement, verbatim, with its locator; structure preserved | **no** |
| **requirements** | `distilled/requirements.yaml` | **every** BCP 14 statement as `<record>#R-NNNN`: verbatim text, locator, verb, actor, `testable`, `kind: stated \| inferred` | **no** |
| **schema** | `distilled/schema/*.cddl`, `*.schema.json` | usable schemas: the spec's own CDDL/ASN.1/JSON Schema **verbatim**, plus a machine-checkable rendering if the source has only prose | with reason |
| **messages** | `distilled/messages.yaml` | every message / structure / header: fields, types, encoding, byte-level layout, which requirements constrain it | with reason |
| **protocol** | `distilled/protocol.yaml` + `protocol.md` | roles, messages exchanged, sequences, error paths; a Mermaid sequence diagram | with reason (pure data formats) |
| **state machine** | `distilled/state-machine.yaml` | states, transitions, triggers, guards, error states — for anything with lifecycle (registration, receipt, verification) | with reason |
| **examples / test vectors** | `distilled/examples/` | every example in the source as a fixture file, plus expected results; this is what drives our tests | with reason |
| **design notes** | `distilled/design-notes.md` | **how this document bears on our design**: what we adopt, adapt or reject, mapped to ARCH / DEC / D-n decisions; open questions | **no** |

**Design notes for COSE / CBOR / signing-envelope documents** must address
D-3 explicitly (option 5: reduced CBOR, no IANA tags, COSE as export only):
which headers and structures map onto our statement fields, what the export
mapping is, and what we deliberately do not carry.

## Completeness is checked, not asserted

`requirements.yaml` carries two counts in its header:

```yaml
source_keyword_count: 83     # bin/bcp14-count on the fetched source
extracted_keyword_count: 83  # BCP 14 keywords across all extracted texts
reconciliation: ""           # REQUIRED if the two differ: say exactly why
```

`bin/validate` recomputes `extracted_keyword_count` from the texts and fails if
it does not match the header, and fails if the two counts differ with no
reconciliation. The source count comes from `bin/bcp14-count` on the cached
source (sources are never committed, so this is recorded, not re-derived in CI).

## Multi-agent passes — maximum effort

Extraction runs as independent passes, each at **maximum reasoning effort**,
each recorded in `distillation.passes`:

| pass | what | output |
|---|---|---|
| **1 · extract** | one agent per artifact kind, in parallel, each reading the **source** (never the summary) | the artifact set |
| **2 · verify** | an adversarial agent that did not extract: re-derives the keyword count, checks every locator and every verbatim quote against the source, hunts for dropped statements and spliced quotes | defects fixed, count reconciled |
| **3 · cross-check** | requirements ↔ schema ↔ messages ↔ state machine: every field a requirement names exists in the schema; every transition's trigger is a defined message | inconsistencies fixed or recorded |
| **4 · human review** | a person signs `reviewed_by` on each artifact | buildable-on |

Pass 2 exists because pass 1 fails in known ways: the vCon extraction (2026-09)
dropped four MUSTs and spliced two non-adjacent quotes, and both were found
only by the mechanical checks.

## Tooling

```sh
bin/extract-scaffold records/ietf/rfc-9943   # creates the full artifact set as templates
bin/bcp14-count .cache/rfc-9943.txt          # source keyword count for the header
bin/validate                                  # enforces all of the above
```

The skill `.claude/skills/extract` carries the judgement: how to run the passes,
what a good artifact looks like, and the failure modes to hunt for.

## Definition of done for a lane PR

A topic-lane PR that adds or changes an in-scope record is mergeable only when
that record has `profile: full`, all artifacts present or N/A with reason, the
keyword counts reconciled, and passes 1–3 recorded. CI enforces this on the
records the PR touches (`bin/check-pr-extraction`).
