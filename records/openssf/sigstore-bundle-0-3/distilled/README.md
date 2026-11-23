---
record: sigstore-bundle-0-3
kind: index
title: "sigstore-bundle-0-3 — distilled artifacts"
extracted: "2026-11-20"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

FX-1 full extraction of **Sigstore Bundle v0.3**: `protos/sigstore_bundle.proto`
at sigstore/protobuf-specs tag v0.5.2 (`0342fe5`), with the four other inputs
that make the format readable, each pinned by sha256 (`record.yaml`
`content.note` and the digest table in `render-source.py`): the three Sigstore
files the bundle imports, at the same commit (`envelope.proto`, the DSSE
envelope; `sigstore_common.proto`; `sigstore_rekor.proto`), and the docs page
"Sigstore Bundle Format" (`content/en/about/bundle.md` in sigstore/docs at
`8aed8c1`, "Version 0.3.2", with its two complete example bundles). The
google/api field_behavior and google/protobuf timestamp imports are Google's and
are not spliced. Quotes and line numbers count in `.cache/sigstore-bundle-0-3.txt`
(1189 lines, sha256 `42559970…19d3`, the `source_digest` of `requirements.yaml`),
which `render-source.py` builds from the five inputs: §1 `sigstore_bundle.proto`
L1-193, §2 `envelope.proto` L195-265, §3 `sigstore_common.proto` L267-672, §4
`sigstore_rekor.proto` L674-868, §5 the docs page L870-1189. Proto comment
markers are blanked in place, so comment prose reads as prose, and every
declaration is its own paragraph. The original bytes are `.cache/sigstore-bundle-0-3.bin`
and `.cache/sigstore-bundle-0-3.include/`; a verbatim schema or example fixture is
cut from those, never from the rendering. None of these files is committed.

**Status: passes 1–3 complete; `reviewed_by` empty.** A person signs it on each
artifact; until then these are readable but not buildable-on. Pass 3 is a
script-run cross-check of requirements, schema, messages, protocol and state
machine against one another (fields both ways, message joins, transition states
and events, requirement and defect ids, every stated count recomputed).

**73 BCP 14 keywords in the source, all reconciled** (`requirements.yaml`
`reconciliation`; `bin/bcp14-count` 73). None of the five files declares BCP 14;
the capitalised keywords are read as BCP 14 because they are printed in its form.
29 of them are REQUIRED: the 25 `(google.api.field_behavior) = REQUIRED`
annotations and the 4 comment-line labels of DSSE's `envelope.proto` make the 29.
The other 44 are 23 MUST, 7 MUST NOT, 5 SHOULD, 5 MAY, 2 SHOULD NOT, 1 OPTIONAL
and 1 RECOMMENDED. Source defects: **SD-1 to SD-37** in `normative.md`, the one
register every lane id resolves to.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | Every one of the 182 stated requirement texts verbatim as check-quotes markers (252 markers) under 36 sections of distilled/render-source.py's rendering (§1 to §5.1.3: the bundle, envelope, common and rekor protos and the docs page), the keyword declaration and binding-force finding (none of the five files declares BCP 14; the protos are the format and the page a profile of it), the 15 inferred entries named, and the unified source-defect register SD-1 to SD-37 (from 51 lane ids, 1 withdrawn, duplicates merged) with the lines each rests on. |
| requirements | requirements.yaml, inferred-candidates.yaml | 197 entries: 67 skeleton BCP 14 sentences, 23 split children of 13 parents, 43 promoted from candidates, 49 hunted (keyword-less binding text no candidate caught), 15 inferred; 182 stated, testable 102 yes, 62 partial, 33 no. 73 BCP 14 keywords reconciled line by line as a bijection (bin/bcp14-count 73: 29 REQUIRED, 23 MUST, 7 MUST NOT, 5 SHOULD, 5 MAY, 2 SHOULD NOT, 1 OPTIONAL, 1 RECOMMENDED); the 52 lowercase must, should, may, required, recommended and optional are classified, none counted. All 72 candidates have a verdict (43 stated, 0 inferred, 29 reject). 4 groups of identical texts named (R-0028/R-0029/R-0031, R-0053/R-0059, R-0078/R-0087, R-0093/R-0097). Outside this source and not extracted: DSSE's protocol and signature extensions, RFC 3161, RFC 6962 and RFC 9162 tree hashing, the C2SP checkpoint format, Rekor's entry types, the Sigstore client spec, the trusted root and Fulcio's certificate profile. |
| schema | schema/ | 4 verbatim protos (byte-identical to the pinned inputs; they compile under protoc 35.1 from grpcio-tools 1.85.3: 23 messages, 53 fields, 25 of them REQUIRED, 3 enums, written to protoc-descriptor.derived.json) and 1 derived JSON Schema 2020-12 of the proto3 JSON form of a v0.3 Bundle (25 definitions: the 17 messages and the 1 enum reachable from Bundle, and 7 helpers); 251 cases (66 accept, 185 reject; 78 source, 149 proto3-json, 24 source-silent), 337 keyword mutants (324 killed, 13 survive, all 13 equivalent by a named rule, 0 unexplained); jsonschema 4.26.0 agrees on 249 of 251 (the 2 are trailing-newline anchoring), python protobuf rejects none the schema accepts and accepts 89 of the 246 Bundle-level cases it rejects. Field set compared with the descriptor and messages.yaml both ways: 53 of 53, 0 differences. 6 messages and 2 enums not reachable from Bundle are in messages.yaml and not in the schema. Derived: the descriptor, the schema and 4 scripts (build-schema, build-messages, check-protoc, check-schemas, with _ids). |
| messages | messages.yaml | 23 messages with 53 fields (every field of the protoc descriptor and none beyond it), 3 enums, 8 named values (media types, the DSSE extension kind, the in-toto payloadType) and 5 external definitions; per field the number, json_name, type, oneof, field_behavior, wire and JSON encodings and the declaration quoted; 223 field-level constrained_by links, 189 of the 197 requirements placed and the 8 cross-cutting or outside-the-bundle rules listed unplaced with a reason; 10 source silences and 9 lane defects mapped to SD-n. Generated by schema/build-messages.derived.py from the descriptor and requirements.yaml. |
| protocol | protocol.yaml, protocol.md, protocol-evidence.derived.py | The source defines a data format, not a transport; the verification procedure is deferred to an unpinned client spec and is an opaque step. 6 roles (2 inferred), 8 flows, 67 steps (16 inferred), 20 error paths (5 stated, 8 inferred, 7 unspecified), 2 findings, 7 evidence items with 30 checks (21 true, 9 false: the alternative readings the checks were paired with) over the source's two example bundles, re-run by protocol-evidence.derived.py, 12 lane defects mapped to SD-n, 8 open issues, 11 out-of-scope items; one Mermaid diagram per flow in protocol.md (8). Every step's message joins to messages.yaml (message_join: 18 names, 3 free-text names; 5 steps with message none name their object; 70 field names checked). constrained_by holds 320 links to 167 distinct ids; the 30 requirements cited by neither protocol.yaml nor state-machine.yaml are listed with reasons. 50 quotations. |
| state-machine | state-machine.yaml, state-machine-eval.derived.py | 4 machines (M01 bundle verification, M02 version acceptance, M03 signing-time evidence, M04 signing time against the leaf's validity); 48 states (26 inferred, 19 error, 28 terminal), 58 transitions (32 inferred), 23 events, 5 decision states; every transition's states and event and every constrained_by id resolves (88 links to 45 distinct ids) and every state is reachable; guards evaluated over all 403 input combinations (M01 18, M02 20, M03 360, M04 5) and re-checked by state-machine-eval.derived.py with 0 differences (SD-4 is the input on which an accepting and a refusing transition fire together). The source names no state machine; the machines are this model's, with the stated and inferred transitions marked. 4 quotations. |
| examples | examples/ | 9 verbatim fixtures (every fenced example block of the docs page, cut by line from the original bytes: 3 parse as JSON, 6 do not, 3 of those on purpose-defects SD-23 and the placeholder blocks) and 4 derived files (cases.derived.json of 251 cases, fixtures.derived.json, and expected results for the 2 complete bundles: 44 checks, 38 pass, 6 NOT VERIFIABLE because the source holds no log key, no trust root and no TSA certificate, 8 negative controls); reproduce.py (86 checks) re-runs render-source.py byte for byte, re-extracts every fixture and runs the schema checks. The DSSE payload decodes byte-identical to the printed attestation. The source prints no third-party artifact, so a message-signature bundle's digest is not checked against its artifact. |
| design-notes | design-notes.md | 32 rows against m-of-n at 656bac0 (6 adopt, 3 adapt, 4 reject, 11 constrains, 3 conflicts, 5 silent); the four questions of library#151 (which versions exist, what exactly is signed, what a verifier needs, whether a single-signature bundle is ITE-5 compliant); the bundle field by field against MD-3, ADR-0004 and DEC-002; what a byte-faithful import for T-052 keeps; post-quantum; 10 checks and enumerated onlys; 7 design-lane source defects (SD-D-1 to SD-D-7, mapped to SD-26 and SD-30 to SD-37); 12 open questions for mofn's owners. Decides nothing. |

## Files

Every file in this directory, by name.

| file | what it is |
|---|---|
| `normative.md` | the verbatim layer and the unified defect register (script-written, then completed) |
| `requirements.yaml` | R-0001 to R-0197 and the reconciliation |
| `inferred-candidates.yaml` | the 72 keyword-less candidates, each with a verdict (C-0001 to C-0072) |
| `skeleton-report.txt` | the report `bin/fx1-skeleton` wrote: 73 keywords, 67 skeleton sentences, 72 candidates, sections |
| `render-source.py` | builds `.cache/sigstore-bundle-0-3.txt` from the five pinned inputs; carries their sha256 table |
| `messages.yaml` | the message model, generated by `schema/build-messages.derived.py` |
| `protocol.yaml`, `protocol.md` | the protocol model and its prose and diagrams |
| `protocol-evidence.derived.py` | re-runs the seven evidence items of `protocol.yaml` over the example bundles |
| `state-machine.yaml` | the four machines and the guard evaluation |
| `state-machine-eval.derived.py` | re-evaluates every guard over all inputs and compares with `guard_evaluation` |
| `design-notes.md` | bearing on m-of-n's design |
| `schema/` | `README.md`; verbatim `sigstore_bundle`, `envelope`, `sigstore_common`, `sigstore_rekor` `.verbatim.proto`; derived `protoc-descriptor.derived.json`, `bundle.derived.schema.json` and the scripts `check-protoc`, `build-schema`, `build-messages`, `check-schemas`, `_ids` (`.derived.py`) |
| `examples/` | `README.md`; 9 `*.verbatim.*` fixtures; `cases.derived.json`, `fixtures.derived.json`, `message-signature-bundle.expected.derived.json`, `dsse-bundle.expected.derived.json`; `reproduce.py` |
