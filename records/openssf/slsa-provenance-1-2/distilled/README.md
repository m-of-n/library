---
record: slsa-provenance-1-2
kind: index
title: "slsa-provenance-1-2 — distilled artifacts"
extracted: "2026-11-16"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

FX-1 full extraction of **SLSA Build Provenance v1.2**: `spec/build-provenance.md`
in slsa-framework/slsa, branch `releases/v1.2` at `ae7fc76` (the Markdown
https://slsa.dev/spec/v1.2/build-provenance is built from; `content.note` says
why it replaced the HTML). Authoritative bytes: `.cache/slsa-provenance-1-2.bin`,
sha256 `182ab5cf…d74854a0` (= `content.sha256`), and the two files the page
includes, `provenance.cue` and `provenance.proto` (digests in `content.note`).
Quotes and line numbers count in `.cache/slsa-provenance-1-2.txt` (704 lines),
which `render-source.py` builds: the includes spliced in where the page shows
them, the ATX headings renumbered in place (§1 Purpose, §2 Model, §3 Parsing
rules, §4 Schema with §4.1 to §4.7, §5 Verification, §6 Index of build types,
§7 Migrating from 0.2, §8 Change history). None of these files is committed.

**Status: passes 1–3 complete.** `reviewed_by` is empty on every artifact. A
person signs it; until then these are readable but not buildable-on.

**53 BCP 14 keywords in the source, all reconciled** (`requirements.yaml`
`reconciliation`). The RFC 2119 recital (L25-27) adds 10 more to the texts and
is kept as the withdrawn R-0001: `bin/fx1-skeleton` does not strip a Markdown
recital whose RFC link contains `www.`.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | Every requirement text with source lines verbatim under §1-§8 as check-quotes markers over distilled/render-source.py's rendering (spec/build-provenance.md at releases/v1.2 ae7fc76 with the provenance.cue and provenance.proto includes spliced in), the binding-force finding (prose and field tables authoritative; cue and protobuf informative), the 12 inferred entries named, and the canonical source-defect list SD-1 to SD-14 with a crosswalk to the pass-1 lane ids. |
| requirements | requirements.yaml, inferred-candidates.yaml | 170 entries: 50 skeleton BCP 14 sentences (R-0001, the RFC 2119 recital, withdrawn), 15 split children of 9 parents, 32 promoted from candidates, 61 hunted (field-table rows and descriptions, the per-level field annotations, binding-force notes, footnote rules, the §7 migration mappings, the front-matter predicateType rules), 12 inferred. 53 BCP 14 keywords reconciled line by line as a bijection (bin/bcp14-count 53; the 10 more in the texts are the recital's). All 92 candidates have a verdict (32 stated, 2 inferred, 58 reject). The in-toto Statement, ResourceDescriptor and field types, and SLSA Verifying artifacts, are outside this source. |
| schema | schema/ | 2 verbatim (provenance.cue and provenance.proto, byte-identical to the pinned include files; the proto compiles under protoc from grpcio-tools 1.85.1) and 1 derived JSON Schema of the predicate following the text where it overrides the summaries; 143 cases (62 accept, 81 reject, each tagged by basis), 144 keyword mutants with 0 survivors, field and type sets compared with the cue and proto (0 differences); jsonschema 4.26 agrees on all 143. |
| messages | messages.yaml | 8 structures (Statement, Provenance, BuildDefinition, RunDetails, Builder, BuildMetadata, ResourceDescriptor, extension fields) with 27 fields and per-level required-ness, 6 encoding rules, 5 field types, the v0.2 to v1 migration mapping with removed and renamed fields, the keyword-less statements with their ids; 305 constrained_by links. The 6 fields with none are in-toto's, each with a note. |
| protocol | protocol.yaml, protocol.md | No transport, signing or distribution is defined. 16 roles (4 inferred), 9 flows, 76 steps (20 inferred), 13 error paths, 12 open issues; one Mermaid diagram per flow in protocol.md; message names joined to messages.yaml; Verifying artifacts is an opaque step. |
| state-machine | state-machine.yaml | 3 machines: a consumer's handling of one attestation, how one field is read, and predicateType across versions; 25 states (14 inferred, 6 error), 29 transitions, 15 events; M02's guards evaluated over all 64 inputs (SD-5 is the one input on which two transitions fire). |
| examples | examples/ | 5 verbatim fixtures (every fenced example in the source, cut by line) and 5 derived instances (minimal and full provenance, a full Statement, a v0.2 input and its v1 migration), with a manifest; reproduce.py (49 checks) re-runs render-source.py byte for byte, re-extracts every fixture, and runs the schema checks. The source prints no signed attestation, so there is no external oracle. |
| design-notes | design-notes.md | 32 rows against m-of-n at 7c3c731 (4 adopt, 5 adapt, 4 reject, 10 constrains, 4 conflicts, 5 silent); the predicate field by field onto the native model, structured against opaque carriage, with what round-trips, what is lost and what has no home (for T-053); T-052's round trip byte-faithful only with the original envelope; the v1.1 against 1.2 mismatch recorded, not reconciled; post-quantum: the predicate carries no signature or key. Decides nothing. |
