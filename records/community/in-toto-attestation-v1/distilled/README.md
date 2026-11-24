---
record: in-toto-attestation-v1
kind: index
title: "in-toto-attestation-v1 — distilled artifacts"
extracted: "2026-11-09"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

FX-1 full extraction of the **in-toto Attestation Framework v1.2**, tag
v1.2.0, commit `df02077bf97218a8860a5c534eff1f1381f56984`. Authoritative
bytes: the GitHub source archive, `.cache/in-toto-attestation-v1.bin`, sha256
`c66cbb44b115…667795d91` (= `content.sha256`). Quotes and line numbers count
in its plain-text rendering `.cache/in-toto-attestation-v1.txt` (1162 lines,
sha256 `87260bf00f01…1ed13d0`, = `source_digest` in `requirements.yaml`),
which `render-source.py` builds from twelve of the archive's Markdown files.
Neither file is committed.

**Status: passes 1–3 complete.** `reviewed_by` is empty on every artifact. A
person signs it, and until then these are readable but not buildable-on.

**101 BCP 14 keywords in the source, 101 in the requirement texts**
(SHOULD 36, MUST 30, MAY 18, SHOULD NOT 7, REQUIRED 4, RECOMMENDED 4, MUST NOT
2), once the §1.2 recital (L63-65) is stripped. 94 source lines carry them,
each claimed by exactly one skeleton entry; `requirements.yaml`
`reconciliation` lists them by line. The keyword declaration is RFC 2119
without RFC 8174 (normative SD-11), so lowercase forms were judged as
sentences, not counted.

**No exchange, no trust model, no canonical form.** The framework defines four
data layers (Predicate, Statement, Envelope, Bundle) and one consumer
procedure, the validation model in `docs/validation.md`, which has no keyword
and sits outside the documents §1.2 declares keywords for. Rows that depend on
DSSE, ITE-5 or the predicate specifications are marked as outside this source.

## Scope

**In: twelve files**, rendered in this order as sections §1 to §12 (file *i*
is §*i*, its level-2 headings §*i*.*j*, and so on):

| § | file in the archive |
|---|---|
| §1 | `spec/README.md` (included for its RFC 2119 declaration and release rules) |
| §2 | `spec/v1/README.md` |
| §3 | `spec/v1/statement.md` |
| §4 | `spec/v1/resource_descriptor.md` |
| §5 | `spec/v1/digest_set.md` |
| §6 | `spec/v1/field_types.md` |
| §7 | `spec/v1/predicate.md` |
| §8 | `spec/v1/envelope.md` (same sha256 as the record `in-toto-envelope-v1`) |
| §9 | `spec/v1/bundle.md` |
| §10 | `spec/v1/CHANGELOG.md` |
| §11 | `spec/versioning.md` |
| §12 | `docs/validation.md` |

**Out:** `spec/predicates/*` (each predicate is its own specification; the
directory was listed only to check the file names R-0059 and R-0069 refer to)
and `spec/v0.1.0`. The reference bindings (`protos/`, Go, Python, Rust) are not
source: the two `.proto` files are kept as verbatim schema, and the bindings'
validators are read only by `schema/refimpl-compare.derived.py`, to say where
they differ from the text.

## Artifacts

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 180 verbatim entries in source order, each with a locator and line range (every BCP 14 sentence the skeleton found, split into one statement per entry where it held several; the keyword-less statements judged binding; R-0217 and R-0218, found by pass 2), 20 pointers to the inferred entries, and the 18 split parents represented by their children: 218 requirement ids in all. 27 source defects and tensions `SD-1`–`SD-27` (9 defect, 7 tension, 7 gap, 2 form, 1 editorial, 1 unclear), and a Crosswalk table mapping the four lanes' independently numbered SD lists. Overview prose, examples and use cases not reproduced, except where a defect needs them. |
| requirements | `requirements.yaml` | 218 entries `R-0001`–`R-0218`: 198 stated, 20 inferred (flagged, own words, with grounds). 87 skeleton entries (18 are split parents), 36 `split_of` children, 37 promoted from 60 candidates, 38 hunted (36 pass 1, 2 pass 2), 20 inferred. By first keyword: MUST 35, SHOULD 42, MAY 20, REQUIRED 8, SHOULD NOT 7, RECOMMENDED 4, MUST NOT 3, none 99. Testable: yes 110, partial 57, no 51. Keywords 101 of 101 reconciled by line. 6 groups of identical text, listed in the header. Ids are stable; R-0001–R-0087 are the skeleton's, the rest were appended. |
| candidates | `inferred-candidates.yaml` | 120 keyword-less candidates, every one with a verdict: 60 stated, 57 reject (each with a reason), 3 inferred. The stated and inferred ones back-link to 40 entries. |
| schema | `schema/` | Source ships no JSON Schema. Verbatim: 6 files (4 schema blocks from §3.1, §4.1, §5.1, §7.1, and the two `.proto` files), indexed in `verbatim-sources.derived.json`. Derived: 7 JSON Schemas 2020-12 (Statement, ResourceDescriptor, DigestSet, DigestSet with output lengths, Envelope, Bundle line, field types), a generator, and a checker with 1403 cases (274 must-accept, 1120 must-reject) and a mutation test (846 mutants, 841 killed, 5 equivalent, 0 survived). 1061-case hand port of the Go and Python validators, with the differences listed in the schema README. |
| messages | `messages.yaml` | 16 messages (Envelope, Signature, Statement, ResourceDescriptor, DigestSet, Predicate layer, Bundle, Bundle line, field types, ResourceURI, TypeURI, Timestamp, media types, file naming and storage, parsing and versioning rules, validation-model inputs and outputs), 24 fields on the structural messages, the 19 DigestSet algorithms, the media-type, naming and parsing-rule tables. 551 requirement citations to 197 distinct ids. 8 local source defects `SD-01`–`SD-08`, each with its normative SD. |
| protocol | `protocol.yaml`, `protocol.md` | No exchange of its own: each flow is one party building or holding an object, a delivery the source does not define, and the receiving party processing it alone. 11 roles, 11 flows with 71 steps (10 inferred), 16 error paths, 18 source defects and tensions (9 defect, 7 tension, 2 gap), 10 `not_defined`, 166 step quotes. 262 requirement citations to 192 distinct ids; 11 steps carry none, each named with its reason. A sequence diagram per flow. |
| state-machine | `state-machine.yaml` | 6 machines, 35 states (6 error), 39 transitions (6 inferred), 14 triggers (all defined and all used). M01 the validation model as written (14 states, 16 transitions); M02 per-line Bundle processing; M03 the life of a Bundle file; M04 and M05 the version lifecycle from the author's and the consumer's side; M06 the framework release lifecycle. 99 transition citations to 63 distinct ids (103 and 64 with the three M02 invariants); 1 transition without one (M03.T05). No key, attestation or session lifecycle: the source defines none. |
| examples | `examples/` | 17 verbatim fixtures (every code block: JSON, shell and JSON Lines), 12 derived fixtures, 22 inline examples with no file, all indexed in `vectors.derived.json`; 73 expected-result checks. Most printed JSON examples are placeholders and are expected to be rejected; each has a derived twin that is accepted. Arithmetic examples (dirHash listing, `h1:` conversion, gitBlob of `Hello`, Tekton digest) recomputed. |
| design-notes | `design-notes.md` | 36 mapping rows against m-of-n at `bb005ed`: adopt 7, adapt 3, reject 2, constrains 11, conflicts 5, silent 8. Beyond the table: 7 adopt notes (A-1–A-7), 8 adapt (D-1–D-8), 6 reject (J-1–J-6); MD-3, `ADR-0004` and DEC-002 (§5), per-requirement sections (§6–§11), 10 source defects found (§12, own numbering), 9 corrections to our own documents' readings (§12b), 15 open questions. Decides nothing. |
| skeleton report | `skeleton-report.txt` | `bin/fx1-skeleton` output. "code blocks: 0" is the skeleton not reading Markdown fences; all 21 fenced blocks are covered (17 fixtures and 4 schema blocks). |

## Reproducing

Needs `.cache/in-toto-attestation-v1.txt`, which is not committed.

```
# rebuild the rendering from the archive (content.url, sha256 = content.sha256)
python3 -I render-source.py <extracted attestation-<commit> dir> .cache/in-toto-attestation-v1.txt

# re-cut every verbatim fixture, re-derive every derived one, re-check all
# expected results, run the schema checker; prints what it examined
python3 -I examples/reproduce.py
python3 -I examples/reproduce.py --archive <extracted dir>   # also compare with the Markdown and .proto bytes

# schema checker alone; add --mutate and --basis ../requirements.yaml
python3 -I schema/check-schemas.derived.py

# quotes, locators, keywords, joins
bin/check-quotes --txt .cache/in-toto-attestation-v1.txt records/community/in-toto-attestation-v1
bin/check-locators records/community/in-toto-attestation-v1
bin/bcp14-count .cache/in-toto-attestation-v1.txt
bin/check-id-joins --resolve --surface records/community/in-toto-attestation-v1
```

Every quotation is a `<!-- q Lx-y -->` marker whose words
`bin/check-quotes --render` wrote from the rendering; a quotation in YAML is a
`quote:` beside `source_lines:`. Nothing was typed.

## Numbering

Four artifacts keep source-defect lists, numbered independently: `normative.md`
`SD-1`–`SD-27` (canonical, cited by `requirements.yaml`), `messages.yaml`
`SD-01`–`SD-08`, `protocol.yaml` `SD-01`–`SD-18`, and `design-notes.md` §12
`SD-1`–`SD-10`. An SD number means nothing without its file. Each local entry
names its normative one, and `normative.md`'s Crosswalk table maps all four.
Requirement ids are `in-toto-attestation-v1#R-NNNN` everywhere; a bare `R-0006`
in `design-notes.md` followed by a section sign or the word *report* is mofn's
research report, not this record's requirement.

## Known gaps, stated rather than hidden

- `reviewed_by` is empty throughout. No person has signed any artifact.
- DSSE v1.0, ITE-5, RFC 3986 §6.2.2.1 and RFC 3339 are not in the source.
  Facts about them point at their records or are marked outside this source.
  Normative SD-6 and SD-15 paraphrase RFC 3986 and RFC 3339 and were not checked
  against RFC text, which is not cached.
- `design-notes.md` prose cites some split-parent ids (52 distinct skeleton
  ids in all); where it does, the statement meant is one of the parent's
  children, which `requirements.yaml` names. It was not rewired.
- L725-726 ("Users are expected to choose an existing predicate type … or
  develop a new one") is advice, not carried as a requirement; protocol step
  F10.1 models it with an empty `constrained_by`. A reviewer may add it as
  hunted.
- `schema/refimpl-compare.derived.py` rests on three modelling assumptions it
  could not run: protojson and `json_format` reject unknown fields, and Python's
  `json_format` decodes bytes leniently. The Rust binding was read for a note
  only, not ported.
- `bin/check-id-joins --quote-join` examines 0 pairs in this record (no inline
  quotation sits beside a citation), so the join audit was done by selector
  script instead: every emitted citation was read against its resolved text.
- `examples/` placeholders are not valid hex, base64 or JSON; that is a
  property of the source's illustrations, recorded per fixture, not a defect in
  a rule.
- `record.yaml` was not edited for `bears_on` or usefulness corrections the
  design notes propose (§12b).
