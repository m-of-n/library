---
name: Full extraction of a protocol or format document (FX-1)
description: Use when a record of type rfc, draft, spec or ietf moves past stub, or when asked to extract, distil, or "fully process" a standard. Produces the complete FX-1 artifact set — normative text, every requirement, schemas, message formats, protocol model, state machines, test vectors and design notes — a script-built verbatim layer, then multi-agent passes with judgement at maximum effort.
---

# Full extraction (FX-1)

**The goal is implementation and testing, not understanding.** Every artifact
must be something a later engineer or test harness consumes directly. If an
implementer would still have to open the source to find something, the
extraction is not finished. The normative definition is `docs/extraction.md`;
this skill is how to do it well.

## 0. Before starting

- `summary.md` exists and is reviewed. Labels are set: `tags`, `bears_on`, `topic`.
- The source is fetched and hashed: `bin/fetch-source <id> --xml` writes the
  verified `.cache/<id>.txt` and, for an RFC, the XML v3 rendering beside it
  (structure only, never quoted). For a PDF, `pdftotext -layout`.
- `bin/extract-scaffold records/<body>/<id>` has laid out the artifact set.
- **`bin/fx1-skeleton records/<body>/<id> --force`** has written the verbatim
  layer over it: `requirements.yaml` (every BCP 14 sentence, text and
  `source_lines` filled, keyword counts computed), `inferred-candidates.yaml`,
  `normative.md`, and every `<sourcecode>` as a `.verbatim.` fixture. Read
  `skeleton-report.txt`: a section where the .txt and XML counts differ is
  where a keyword hides in a table or a comment.
- Strip from what pass-1 agents read anything a previous extraction left in
  `record.yaml` comments: it is another agent's output, and a test run that
  left it in found four "new" defects that were not blind.

## 1. Pass 1 — extract (parallel, effort per the table)

Each agent reads the **source**, never the summary or another agent's output.
**No agent types a quotation.** Requirement texts come from the skeleton or a
candidate; a Markdown quotation is a marker, `<!-- q L120-123 -->` or
`<!-- q L120-123 "starts" .. "ends" -->`, and `bin/check-quotes --render --only
<your file>` writes the words; a YAML quotation outside requirements is
`quote:` beside `source_lines:`. Run `bin/check-quotes` before you report.

Model and effort per agent are in `docs/extraction.md` "Who runs what":
judgement at max on the largest model, the mechanical lanes allowed a smaller
one, and every agent's model, effort and tokens recorded in the pass.

| agent | effort | produces | hunt for |
|---|---|---|---|
| requirements | **max** | `requirements.yaml`, verdicts in `inferred-candidates.yaml`, keyword-less binding text into `normative.md` as markers | fill `actor`, `object`, `field`, `testable` (reason when not yes); split a multi-keyword entry with `split_of` children whose texts are sub-spans; give **every** candidate a verdict — `stated` (verbatim, `verb: none`, `candidate: C-NNNN`), `inferred` (own words, `kind: inferred`), or `reject` with a reason; then hunt what has no cue: what the document never says outright but an implementer must do (which parameters are excluded, what order things go in) — `kind: inferred` |
| schema | smaller allowed | `schema/*.cddl`, `*.schema.json` | the source's own CDDL/ASN.1/JSON Schema **copied verbatim** with section; where only prose exists, a derived schema. **Derived files are named `*.derived.*`** — the infix is mandatory, not just a header marker; an unmarked name asserts verbatim. Derived JSON Schemas take `$id: urn:library:<record-id>:<artifact-name>`. `bin/validate` enforces both |
| messages | smaller allowed | `messages.yaml` | every message, header, envelope, structure; field, type, required, encoding, byte-level layout; `constrained_by` links to R-ids |
| protocol | **max** | `protocol.yaml`, `protocol.md` | roles, every flow, every error path; a Mermaid sequence diagram per flow |
| state machine | **max** | `state-machine.yaml` | anything with lifecycle — registration, issuance, receipt, verification, key rollover; states, triggers, guards, error states |
| examples | smaller allowed | `examples/` | every example and test vector as a fixture file, verbatim, with the expected result; hex for binary |
| design notes | **max** | `design-notes.md` | adopt / adapt / reject, each mapped to ARCH-0001/0002, DEC-*, MD-n; for COSE/CBOR/envelope documents, **MD-3 explicitly** with a header-by-header mapping, **and where the source cuts against MD-3** — it narrowed DEC-002, it did not accept it; see `docs/extraction.md` |

**Not applicable** is a finding, not a shortcut: record it in
`distillation.not_applicable` with the reason (e.g. *"protocol: pure data
format, no exchange defined — see §1"*). Normative, requirements and design
notes are never N/A.

## 2. Pass 2 — verify (a different agent, adversarial, effort: max, never tiered)

The verifier did not extract. Its job is to break the extraction. Run the
mechanical checks first — they are free — and spend the judgement on what
they cannot see:

1. `bin/check-quotes`, `bin/check-locators`, `bin/bcp14-count`, `bin/validate`,
   `bin/check-id-joins --surface`, every `reproduce.py`. Every keyword
   difference is fixed or written into `reconciliation`.
2. Quotations nobody marked are invisible to check-quotes: an unmarked
   blockquote, a quoted phrase inside a note. Grep for them. Known failure:
   two non-adjacent quotes spliced into one (vCon, 2026-09).
3. Walk the source section by section looking for dropped statements —
   especially in tables, figure captions, IANA considerations and security
   considerations, which pass 1 skims.
4. Check every example fixture reproduces byte-for-byte.
5. Attack the smaller-model lanes hardest. In the one tiered run they held 13
   of the 15 false claims: off-by-one id joins, `constrained_by` left empty,
   a schema that rejected what its CDDL accepted, a validator that accepted
   `kty: true`.

## 3. Pass 3 — cross-check (smaller model allowed; joins by script)

- Every field a requirement names exists in `messages.yaml` or the schema.
- Every message in a protocol flow is defined in `messages.yaml`.
- Every state-machine trigger is a defined message or a named event.
- Every example validates against the schema.

Record inconsistencies as fixes, or as open questions in `design-notes.md` if
the source itself is inconsistent — never paper over a source defect.

## 4. Record it

```yaml
distillation:
  profile: full
  artifacts:
    - {kind: requirements, path: distilled/requirements.yaml,
       coverage: "all 83 BCP 14 statements, §1–§9; excludes IANA registrations",
       reviewed_by: ""}
    # ...one per artifact
  not_applicable:
    - {kind: state-machine, reason: "stateless format; no lifecycle defined"}
  passes:
    - pass: extract
      by: "claude (4 parallel agents over bin/fx1-skeleton)"
      effort: tiered
      date: "2026-09-29"
      agents:
        - {role: requirements, model: claude-opus-5-5, effort: max, tokens: 210000}
        - {role: schema+examples+messages, model: claude-sonnet-5-5, effort: medium, tokens: 80000}
        - {role: protocol+state-machine, model: claude-opus-5-5, effort: max, tokens: 290000}
        - {role: design-notes, model: claude-opus-5-5, effort: max, tokens: 355000}
    - {pass: verify,      by: "claude (independent)", effort: max, date: "2026-09-29", tokens: 530000}
    - pass: cross-check
      by: "claude"
      effort: tiered
      date: "2026-09-29"
      agents:
        - {role: cross-check, model: claude-sonnet-5-5, effort: medium, tokens: 113000}
status: distilled
```

Then `bin/validate` — it enforces all of the above — and open the PR. A human
signs `reviewed_by` per artifact; until then the artifacts are readable but not
buildable-on.

## Hard rules

- **Never invent a requirement.** Implied is `kind: inferred`, flagged.
- **Never extract from a summary**, including our own.
- **Never paraphrase normative text.** Verbatim or nothing.
- **Never type a quotation.** Reference it by lines; let the script write it.
- **Never edit generated artifacts** (`bin/derive` output); fix the source artifact and regenerate.
- **Never commit the source document.** Digest and URL only.

## Hazards — read `hazards.md` before pass 1

`hazards.md` beside this file is the list of defects that **actually happen**,
every one found in this library's own artifacts and most of them more than
once. It is not optional reading: the later passes of library#39 found more
than the earlier ones precisely because this list grew. It also carries the
measured **batching calibration** and what a verify pass should really attack.

The one-line versions, in the order they cost you most:

- **Digests and dates come from `record.yaml`, verified three ways.** Two were
  fabricated into summary tables. `bin/validate` checks the Digest row because
  of it. `maturity` is read off the front page — an RFC being an RFC does not
  make it Standards Track.
- **Never splice, never heal, and characterise breaks correctly.** Build a
  quote audit with a *named relaxation channel* so the defect class is
  reported rather than masked, plus a longest-prefix test for the splice
  signature. Four lanes each found 4–5 defects in their own prose this way.
- **Grade WHOLE SPANS, longest first, or the audit reports a false clean.** Two
  passes found zero defects by checking fragments; a healed token resolved
  against a *different* part of the same source. Resolve each span against the
  section it is attributed to, add a separate whole-scalar pass for YAML, and
  remember that an undelimited quotation is invisible to any audit. Distrust
  every blanket claim — "nothing healed", "zero relaxations" were both false.
- **Fixing a reader falsifies the counts measured with it.** Two coverage counts
  were true measurements through a parser bug, and repairing the parser made
  them false with nothing to report it. When you fix a reader, grep the records
  for every number it produced.
- **Resolve a foreign quotation against the foreign document only.** Never per
  record *and* never including self: a sibling's copy of a shared wrong
  quotation resolves it, and so does the record's own other file. One record's
  `summary.md` was validated against its own `record.yaml`'s copy of the same
  welded quotation, and the audit reported success.
- **Check the arithmetic, not just the words.** A record claimed a width was
  "the only" one its byte count admitted; the congruence admits every eighth
  value. Enumerate the solution set before writing "only" or "uniquely".
- **A schema that parses is not a schema that binds.** A derived CDDL parsed
  perfectly for two passes and constrained nothing, because a `* label => any`
  wildcard in the same map satisfied every item its rule rejected. Write down
  the instance the schema must REJECT, and check that it does.
- **A new check can under-report to ZERO, silently.** One collected no pairs at
  all on the lane it existed for, and printed that as a clean result. Make every
  check report how many candidates it EXAMINED beside what it found — an absence
  of findings must be distinguishable from an absence of looking.
- **Escapes resolve through editing paths.** Assemble any `\u{…}` in a script
  and grep for the resolved character afterwards. One record carried this
  seven times, always inside a sentence about the hazard.
- **Emit every cited id from the id table by script, then read the resolved
  pairs.** Two lanes shipped 41 ids that resolved to a real but *different*
  statement — not dangling, so nothing caught them.
  `bin/check-id-joins --surface` gives the attack surface.
- **Prefer block sequences and maps over flow**, keep each `text:` on one line
  or in a block scalar, and parse every artifact with **both** readers
  comparing values rather than counts. Five data-loss defects in `_yaml.py`
  came from this, one losing a whole `requirements.yaml` list.
- **`split("\n")`, not `splitlines()`** (form feeds), and `python3 -I` with
  `bin/` on the path explicitly (the shared scratch has a stale `__pycache__`).
- **The first version of any new check over-reports.** Measure it across the
  library and scope it narrowly before trusting it. Three for three.

Tools that already exist, so no pass rebuilds them: `bin/fx1-skeleton`,
`bin/check-quotes`, `bin/bcp14-count`, `bin/check-locators`,
`bin/check-id-joins`, `bin/fetch-source`, `bin/validate`. In the measured runs
every max-effort agent without them wrote its own quote-cutting script.
