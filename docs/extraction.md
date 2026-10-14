# Full extraction standard (FX-1)

**Status: normative for this library from 2026-09-28.** Applies to every
record of type `rfc`, `draft`, `spec` or `ietf` that a pull request
**extracts**. Older records are grandfathered until someone extracts them.

**Scope amended 2026-10-03 (#8, PR #42).** As first written, FX-1 was
triggered by *touching* an in-scope record. That made the standard
unsatisfiable in both directions: a lane could not correct a typo in a
summary without owing four multi-agent passes, and — the case that forced
this — issue #8 could not summarise `rfc-9053` and `rfc-9964` at all, because
#8 assigns their extraction to **#39**. Two issues, one gate, no way to
satisfy both. The trigger is now the **intent to extract**. See
*What triggers FX-1* below.

## Why

A summary tells a person what a document is about. It cannot drive an
implementation or a test. This library exists to feed a specification and its
test suite, so for every protocol or format document we hold, the goal is to
extract **everything an implementer would otherwise have to re-read the source
to find** — in forms a program can consume.

Summaries-only is not a finished record. It is a started one. That remains
true: the amendment below changes **when the bar is enforced**, not what a
finished record is.

## What triggers FX-1

A touched in-scope record must declare `distillation.profile: full` when any
of these holds:

| trigger | meaning |
|---|---|
| the PR adds or changes its `distilled/` | the PR is extracting it now |
| `status: distilled` **and** `distillation.standard` is the current standard | the record claims to be extracted under the standard we enforce |
| a `distillation` block is present, same condition on its `standard` | extraction has been declared under that standard |

Otherwise the record is held to the **summary bar** — `summarized`, valid
relations, `bin/validate` clean — and `distillation` is left alone.

## The vintage — what "complete" is measured against

**Added 2026-10-13 (#73).** `distillation.profile` says *how completely* a
record was extracted. `distillation.standard` — the **vintage** — says *against
what*. A numerator without its denominator is not a claim, and for a year the
record format carried only the numerator.

```yaml
distillation:
  standard: FX-1      # what it was measured against
  profile: full       # how completely it met that
```

The grandfather clause in the first paragraph of this document — *older records
are grandfathered until someone extracts them* — was written here and
implemented nowhere. `bin/check-pr-extraction` read `status: distilled` as
"claims FX-1" with no regard for *when* or *under which standard* the status
was earned, so a record legitimately distilled under an earlier meaning of the
word was permanently delinquent, and **every PR touching it failed CI whatever
the PR did**. That stranded eleven records at the time #73 was written, and
twenty-three once the `distillation`-block trigger is counted too.

With a vintage the clause becomes a comparison a tool can make:

- **names the current standard** → enforce it. The ratchet: an extracted record
  cannot regress to a summary.
- **names an earlier one** → grandfathered, held to the summary bar.
- **names nothing** → read as the current standard. Omission fails *closed*, so
  new work is measured against the standard of the day.

**Grandfathering is not a licence to edit `distilled/`.** Touching the artifacts
is extraction, and extraction is measured against the current standard whatever
the record used to claim — the first row of the table above outranks the other
two. A grandfathered record cannot grow artifacts that quietly miss the bar; it
can only be left alone or raised.

This is also what makes the *next* standard survivable. When FX-2 lands, the 35
records saying `profile: full` will still say `full` — and they will also still
say `standard: FX-1`, so the gate grandfathers them instead of failing all 35 at
once. `profile: partial` was considered and rejected for exactly this: it
relabels today's stranded records and leaves tomorrow's.

The legal vintages and the current one are declared **once**, in
`schema/record.schema.yaml` under `fields.distillation.keys.standard`, and
parsed by `bin/_fx1.py`. The three vintages in the corpus today:

| vintage | what it is |
|---|---|
| `FX-1` | this document, normative from 2026-09-28 |
| `distillation/0.1.0` | `docs/distillation.md` v0.1.0 (2026-09-22), the #9 procedure |
| `threat-radar/import` | Threat-Radar/library's own practice, imported wholesale by #62, never re-measured here |

This is a **ratchet, not a loophole**. Once a record is extracted the first
two triggers keep firing on every later PR that touches it, so an extracted
record cannot quietly regress to a summary. `bin/check-pr-extraction` prints
the records it held to each bar, so a reviewer can see what was waived.

**Rejected alternatives.** Exempting `body: nist` was considered and rejected:
it confuses *who published a document* with *what we intend to do with it*, and
a NIST protocol document we did mean to extract would have slipped through.
Narrowing `IN_SCOPE` to drop `spec` was rejected for the same reason — a
`spec` record is extractable, and some should be. Both would have keyed the
rule off the document's provenance; intent is the thing that actually varies.

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
| **design notes** | `distilled/design-notes.md` | **how this document bears on our design**: what we adopt, adapt or reject, mapped to ARCH / DEC / MD-n decisions; open questions | **no** |

**Design notes for COSE / CBOR / signing-envelope documents** must address
MD-3 explicitly (option 5: reduced CBOR, no IANA tags, COSE as export only):
which headers and structures map onto our statement fields, what the export
mapping is, and what we deliberately do not carry.

**And they must record where the document cuts against MD-3.** MD-3 is a dated
*narrowing* of DEC-002, taken 2026-09-28 — **not an acceptance of it.**
`CONTRIBUTING` §5 in `m-of-n` is explicit that only an ADR accepts a decision,
and **no DEC-002 ADR exists.** An extraction that maps cleanly onto option 5
and reports nothing else has confirmed a choice rather than tested it, and the
ADR it is meant to feed learns nothing from it. So where a source supports a
different option, or exposes a cost option 5 pays and another does not, **say
so in the same section and name the option.**

`canonical-encoding` is the worked example. RFC 9804's extraction put **option
1 on the right side of all four grounds that withdraw option 3**, and found it
also wins namespace governance — the opposite of what MD-3 assumed when it was
taken six days earlier. That finding exists only because the extraction was not
required to agree with the narrowing it was mapped against. **An extraction
that can only confirm is not evidence.**

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
bin/check-pr-extraction main                  # which bar each touched record was held to
```

`bin/_fx1.py` is the **single implementation** of the trigger, and
`schema/record.schema.yaml` the single declaration of the vintages. Both exist
because the rule was previously stated three incompatible ways — here, in
`library/CLAUDE.md`, and in the schema, which still documented the "moves past
stub" trigger retired on 2026-10-03 (#73). A rule stated three ways is a rule
nobody can follow.

The skill `.claude/skills/extract` carries the judgement: how to run the passes,
what a good artifact looks like, and the failure modes to hunt for.

## Definition of done for a lane PR

A topic-lane PR that **extracts** an in-scope record — by any of the triggers
above — is mergeable only when that record has `profile: full`, all artifacts
present or N/A with reason, the keyword counts reconciled, and passes 1–3
recorded. CI enforces this (`bin/check-pr-extraction`).

A PR that only **summarises** an in-scope record is mergeable at the summary
bar. It should say so in its body, and name the issue that owns the eventual
extraction if one does — as #8 names #39 for the COSE/JOSE set.
