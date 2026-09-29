---
name: Full extraction of a protocol or format document (FX-1)
description: Use when a record of type rfc, draft, spec or ietf moves past stub, or when asked to extract, distil, or "fully process" a standard. Produces the complete FX-1 artifact set — normative text, every requirement, schemas, message formats, protocol model, state machines, test vectors and design notes — through multi-agent passes at maximum effort.
---

# Full extraction (FX-1)

**The goal is implementation and testing, not understanding.** Every artifact
must be something a later engineer or test harness consumes directly. If an
implementer would still have to open the source to find something, the
extraction is not finished. The normative definition is `docs/extraction.md`;
this skill is how to do it well.

## 0. Before starting

- `summary.md` exists and is reviewed. Labels are set: `tags`, `bears_on`, `topic`.
- The source is fetched and hashed (`bin/ingest --fetch`), and a plain-text
  rendering is in `.cache/` (RFC `.txt`, or `pdftotext -layout`).
- `bin/extract-scaffold records/<body>/<id>` has laid out the artifact set.
- `bin/bcp14-count .cache/<source>.txt --by-keyword` → the source count.

## 1. Pass 1 — extract (parallel, one agent per artifact kind, effort: max)

Each agent reads the **source**, never the summary or another agent's output.

| agent | produces | hunt for |
|---|---|---|
| normative | `normative.md` | every BCP 14 statement *and* every normative table, ABNF, CDDL, IANA rule; verbatim; locator on each |
| requirements | `requirements.yaml` | one entry per statement; split compound sentences only where each part is separately testable; `actor` is who must comply; `testable: yes/partial/no` with a reason when not yes; `kind: inferred` marks anything not literally stated |
| schema | `schema/*.cddl`, `*.schema.json` | the source's own CDDL/ASN.1/JSON Schema **copied verbatim** with section; where only prose exists, a derived schema marked `derived` |
| messages | `messages.yaml` | every message, header, envelope, structure; field, type, required, encoding, byte-level layout; `constrained_by` links to R-ids |
| protocol | `protocol.yaml`, `protocol.md` | roles, every flow, every error path; a Mermaid sequence diagram per flow |
| state machine | `state-machine.yaml` | anything with lifecycle — registration, issuance, receipt, verification, key rollover; states, triggers, guards, error states |
| examples | `examples/` | every example and test vector as a fixture file, verbatim, with the expected result; hex for binary |
| design notes | `design-notes.md` | adopt / adapt / reject, each mapped to ARCH-0001/0002, DEC-*, D-n; for COSE/CBOR/envelope documents, **D-3 explicitly** with a header-by-header mapping |

**Not applicable** is a finding, not a shortcut: record it in
`distillation.not_applicable` with the reason (e.g. *"protocol: pure data
format, no exchange defined — see §1"*). Normative, requirements and design
notes are never N/A.

## 2. Pass 2 — verify (a different agent, adversarial, effort: max)

The verifier did not extract. Its job is to break the extraction:

1. Recount with `bin/bcp14-count` and compare against the requirements texts.
   Every difference is either fixed or written into `reconciliation`.
2. Check every `text` is a **verbatim** substring of the source and every
   locator points at the section that contains it. Known failure: two
   non-adjacent quotes spliced into one (vCon, 2026-09).
3. Walk the source section by section looking for dropped statements —
   especially in tables, figure captions, IANA considerations and security
   considerations, which pass 1 skims.
4. Check every example fixture reproduces byte-for-byte.

## 3. Pass 3 — cross-check (effort: max)

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
    - {pass: extract,     by: "claude (8 parallel agents)", effort: max, date: "2026-09-29"}
    - {pass: verify,      by: "claude (independent)",       effort: max, date: "2026-09-29"}
    - {pass: cross-check, by: "claude",                     effort: max, date: "2026-09-29"}
status: distilled
```

Then `bin/validate` — it enforces all of the above — and open the PR. A human
signs `reviewed_by` per artifact; until then the artifacts are readable but not
buildable-on.

## Hard rules

- **Never invent a requirement.** Implied is `kind: inferred`, flagged.
- **Never extract from a summary**, including our own.
- **Never paraphrase normative text.** Verbatim or nothing.
- **Never edit generated artifacts** (`bin/derive` output); fix the source artifact and regenerate.
- **Never commit the source document.** Digest and URL only.
