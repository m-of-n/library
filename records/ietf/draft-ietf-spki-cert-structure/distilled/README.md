---
record: draft-ietf-spki-cert-structure
kind: index
title: "draft-ietf-spki-cert-structure — distilled artifacts"
extracted: "2026-11-08"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

This is the FX-1 full extraction of **draft-ietf-spki-cert-structure-06**, *Simple
Public Key Certificate*, dated 26 July 1999. The draft expired on 31 January 2000
and was never published as an RFC. The authoritative bytes are the lead author's
copy at `content.url`, `.cache/draft-ietf-spki-cert-structure.source.txt`, sha256
`6d3332d77a3b…bb64b7397d15` (= `content.sha256`). `record.yaml` says why this
record uses -06 rather than -05.

Quotes and line numbers count in the rendering
`.cache/draft-ietf-spki-cert-structure.txt` (2622 lines, sha256
`7542050ffd86…2af7f19f33de`, = `source_digest` in `requirements.yaml`).
`render-source.py` builds it from the source of record by rewriting the 57 section
headings into RFC form, so that the library's section reader files each line under
its section. Nothing else changes: every line number and every body line is the
source of record's. Neither file is committed.

**Status: passes 1–3 complete.** `reviewed_by` is empty on every artifact. A
person signs it, and until then these artifacts are readable but not
buildable-on.

**0 BCP 14 keywords in the source, 0 in the requirement texts**
(`bin/bcp14-count`). The draft recites RFC 2119's keywords once, in capitals
(lines 39-41), then writes every obligation in lower case. There are 60
lowercase force words: must 21, may 18, optional 10, should 6, required 3,
may not 1, optionally 1. Each one is traced in `requirements.yaml`
`lowercase_modals.census`: 48 are inside stated entries, 8 inside rejected
candidates, and 4 in front matter. Binding text was extracted sentence by
sentence, whatever its modal. No RFC 2119 force is assigned (`verb: none`
throughout).

## Artifacts

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | <ul><li>408 verbatim quotation markers in source order, filed under their sections from the Abstract to §9.2. All 88 §9.2 productions are reproduced, each naming the entry that carries it. Each quotation names the requirements that carry it.</li><li>The 59 inferred entries are not quoted.</li><li>33 source defects, `SD-1`–`SD-33`, with a Crosswalk table to the messages, protocol and design-notes defect lists.</li><li>Extraction notes on tool behaviour: a quotation that crosses a page break keeps the running header's words.</li></ul> |
| requirements | `requirements.yaml` | <ul><li>461 entries, `R-0001`–`R-0461`:<ul><li>402 stated: 346 top-level, and 56 `split_of` children of 27 parents;</li><li>59 inferred (flagged, in our words, each with a `basis`).</li></ul></li><li>Coverage: every binding sentence of the body, the 19 glossary definitions, and 103 BNF production entries, which carry all 88 §9.2 productions (51 of them through `repeated_in`).</li><li>Testable: yes 318, partial 93, no 50, with a reason wherever it is not yes.</li><li>59 entries carry a lowercase modal, recorded with its sense.</li><li>Keywords: 0 = 0, so nothing is reconciled away.</li><li>Ids are stable; entries after R-0437 were appended by the completion audit.</li></ul> |
| candidates | `inferred-candidates.yaml` | 151 keyword-less candidates, every one with a verdict: 110 stated (each linked from its entry by `candidate:`), 41 rejected with a reason, 0 inferred. |
| schema | `schema/` | The draft's schema language is BNF; it ships no CDDL, ASN.1 or JSON Schema.<ul><li>**Verbatim:**<ul><li>§9.2 whole (88 productions);</li><li>every production printed in §3–§8 (66 productions, 64 names);</li><li>the §9 introduction and §9.1.</li></ul>`verbatim_files.derived.py` rebuilds all of it from the source (3 files, 41 blocks).</li><li>**Derived:**<ul><li>a reader and writer for the canonical, advanced and transport forms (`spki_sexp.derived.py`);</li><li>an executable BNF checker that also counts derivations (`spki_bnf.derived.py`);</li><li>187 MUST-accept and MUST-reject cases, run against each (`test_spki.derived.py`). `test_basis.derived.py` joins 342 case entries to 142 requirement ids.</li></ul></li><li>**Mutation:**<ul><li>the reader: 260 mutants, 236 killed, 24 survivors classified;</li><li>the grammar: 138 reachable mutants, 125 killed, 13 survivors, argued equivalent in the schema README.</li></ul></li><li>**BNF comparison** (`bnf_compare.derived.py`), 66 fragment productions against §9.2: 51 identical, 8 identical after an alias, 6 different, 1 in a fragment only.</li><li>`check_messages.derived.py` checks `messages.yaml` against the grammar: 105 messages, 45 instances.</li></ul> |
| messages | `messages.yaml` | <ul><li>105 messages: the 88 §9.2 productions, plus 17 structures the draft prints elsewhere or defines only by example.</li><li>142 fields and 11 encoding rules.</li><li>The canonical layout of each; a script-built minimal instance for 45, each re-encoded byte for byte and accepted by its production.</li><li>1123 `constrained_by` pairs to 440 distinct ids. The 21 ids no message cites are each listed with the reason.</li><li>18 source defects, `SD-01`–`SD-18`.</li></ul> |
| protocol | `protocol.yaml`, `protocol.md` | <ul><li>18 roles; 22 flows with 140 steps (30 inferred); 34 error paths.</li><li>Flows by kind: exchange 7, receive-processing 8, creation-and-delivery 2, and one each of creation, encoding, local, local-decision and local-with-fetch.</li><li>41 source defects, gaps and tensions, `D-01`–`D-41`; 20 `not_defined` items; 554 quotes, all cut by script.</li><li>619 `constrained_by` links to 352 distinct ids; no step or error path is without one.</li><li>`protocol.md` has one sequence diagram per flow (22) and one state diagram per machine (15).</li><li>`join_protocol.derived.py` recomputes the joins and both coverage paragraphs.</li></ul> |
| state-machine | `state-machine.yaml` | <ul><li>15 machines, 110 states, 130 transitions (53 inferred).</li><li>28 triggers: 10 draft objects and 18 named events.</li><li>The machines: SM-01 sequence reader, SM-02 signature check, SM-03 certificate acceptance, SM-04 online-reply check, SM-05 one-time revalidation, SM-06 instrument series, SM-07 name reduction, SM-08 top-level rule, SM-09 reduction driver, SM-10 tag intersection, SM-11 validity intersection, SM-12 threshold reduction, SM-13 ACL entry, SM-14 result certificate, SM-15 certificate standing.</li><li>261 quotes. 344 links to 197 distinct ids; no transition is without one.</li></ul> |
| examples | `examples/` | 31 verbatim fixtures: every S-expression the draft prints. The draft has no other test vectors and prints no expected results, so each expected result is what `reproduce.py` observes.<ul><li>21 are accepted by their production.</li><li>4 name certificates are rejected by `<name-cert>`: normative SD-12, messages SD-08.</li><li>2 `private-key` objects match no rule.</li><li>2 are dates.</li><li>2 are not parseable by design: an elided key and a template.</li></ul>There are also 12 conversion checks (advanced to base64 transport, length prefixes, hashes of the printed keys) and 3 signature checks:<ul><li>the DSA sample verifies over its printed hash, and not over the sha1 of the canonical `(hash ...)` object;</li><li>the RSA sample does not verify as PKCS#1 v1.5.</li></ul> |
| design-notes | `design-notes.md` | <ul><li>50 mapping rows against m-of-n at `bb005ed`: adopts 10, adapts 9, rejects 6, constrains 16, conflicts 4, silent 5.</li><li>The §6.3 threshold table: 11 rows.</li><li>11 adopt notes, 9 adapt notes and 9 reject notes.</li><li>MD-3, `ADR-0004` and DEC-002, option by option (§5).</li><li>Threshold subjects, delegation depth, tags, names, validity and principals (§6–§11).</li><li>What this source fills in mofn's R-0006, and what it corrects in R-0006 and R-0007 (§12).</li><li>A draft of ARCH-0001 §6's SPKI row (§13).</li><li>19 source inconsistencies, `SI-1`–`SI-19`; 20 open questions.</li></ul>Decides nothing. |
| skeleton report | `skeleton-report.txt` | `bin/fx1-skeleton` output: 0 keyword sentences and 151 candidates. "code blocks: 0" is the skeleton finding no XML; every S-expression is covered by the 31 fixtures and every BNF production by `schema/`. |

## Reproducing

This needs `.cache/draft-ietf-spki-cert-structure.source.txt`, which is not
committed. Run from the repository root:

```sh
R=records/ietf/draft-ietf-spki-cert-structure

# rebuild the rendering from the source of record (content.url, sha256 = content.sha256)
python3 -I $R/distilled/render-source.py .cache/draft-ietf-spki-cert-structure.source.txt .cache/draft-ietf-spki-cert-structure.txt

# re-cut every fixture, check its bytes, parse it, match it against the BNF, rerun the conversions
python3 -I $R/distilled/examples/reproduce.py

# the verbatim BNF files, the reader and checker cases, their basis, the messages, the comparison
python3 -I $R/distilled/schema/verbatim_files.derived.py --check
python3 -I $R/distilled/schema/test_spki.derived.py          # add --mutate for the mutation run
python3 -I $R/distilled/schema/test_basis.derived.py         # add --list for every case beside its ids
python3 -I $R/distilled/schema/check_messages.derived.py
python3 -I $R/distilled/schema/bnf_compare.derived.py        # --write regenerates bnf-comparison.derived.txt

# the requirement joins: messages, then protocol and state machine (recompute and compare)
python3 -I $R/distilled/schema/join_requirements.derived.py
python3 -I $R/distilled/join_protocol.derived.py             # --pairs to read every pair, --write after an edit

# quotes, locators, keywords, id joins
bin/check-quotes $R
bin/check-locators $R
bin/bcp14-count .cache/draft-ietf-spki-cert-structure.txt
bin/check-id-joins --resolve --surface $R
```

Every Markdown quotation is a `<!-- q Lx-y -->` marker whose words
`bin/check-quotes --render` wrote from the rendering. A quotation in YAML is a
`quote:` beside `source_lines:`, or a requirement `text` the skeleton or a
candidate cut. Nothing was typed. Each script prints what it examined beside
what it found.

## Numbering

Four artifacts keep source-defect lists, each numbered independently:
- `normative.md` `SD-1`–`SD-33`, cited by `requirements.yaml`;
- `messages.yaml` `SD-01`–`SD-18`, cited elsewhere as `messages.yaml SD-nn`;
- `protocol.yaml` `D-01`–`D-41`, repeated in `protocol.md` and `state-machine.yaml`;
- `design-notes.md` §14, `SI-1`–`SI-19`.

An SD number means nothing without its file. Normative SD-5 is not messages
SD-05. `normative.md`'s Crosswalk maps all four lists, and lists the defects only
one other lane carries.

Requirement ids are `draft-ietf-spki-cert-structure#R-NNNN` everywhere. A bare
`R-0006` or `R-0007` in `design-notes.md`, `summary.md` or `record.yaml` is
mofn's research report, not this record's requirement.

## Known gaps, stated rather than hidden

- `reviewed_by` is empty throughout. No person has signed any artifact.
- A quotation of a heading line carries the rendering's form of the number.
  Five quotations of the §8.4 and §8.7 headings (lines 2126 and 2142) read
  `8.4.` and `8.7.` where the source of record prints `8.4` and `8.7`. Three are
  in `normative.md` (SD-1 and SD-6) and two in `messages.yaml` (SD-16). Every
  other quoted line is byte-identical to the source of record.
- RFC 2692, RFC 2693 and the IETF archive are not cached, so claims about them
  point at their records and were not checked against their text. Claims about
  -05 were checked against -05, whose digest matches the one recorded.
- The 24 reader survivors of the mutation run are classified by category, not
  each proven equivalent. The 13 grammar survivors are argued equivalent in
  `schema/README.md`.
- `bin/check-locators` reports 61 unresolvable locators by design. 59 are
  inferred entries, which have no source lines. The other 2 are R-0001 and
  R-0002, filed under the Abstract, which the tool does not resolve.
- `bin/check-id-joins --quote-join` examines 0 pairs here, because no quotation
  sits beside a citation. The joins were made instead by
  `schema/join_requirements.derived.py`, `join_protocol.derived.py` and
  `schema/test_basis.derived.py`, and the pairs were read. The exception is the
  production-rule pairs in `messages.yaml`, which the script derives from each
  production's own text.
- Verify sampled the prose of `protocol.md` and `design-notes.md` §1–§11 rather
  than reading it line by line. Cross-check matched each of the 37 diagrams to
  its flow or machine, and every id reference in `design-notes.md` to its
  target.
- Left as judgement calls:
  - F-09 lists `prover` as a participant that no step uses; this agrees with
    §7's prover route.
  - SM-10-T01 and SM-10-T02 cite both R-0326 and R-0327, because one quotation
    spans both sentences.
  - `semantic_issues` does not enforce R-0403's K ≥ 1, and nothing claims it does.
