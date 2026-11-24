---
record: secure-systems-lab-dsse
kind: index
title: "secure-systems-lab-dsse — distilled artifacts"
extracted: "2026-11-23"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

FX-1 full extraction of the **Dead Simple Signing Envelope (DSSE)** at pinned
commit `1d3370f62565bca041e97c8310b873ac340edc2e` (protocol and envelope
v1.0.2). Authoritative bytes: `.cache/secure-systems-lab-dsse.tar.gz`, the
source archive, sha256 `88fc65fd…3ac1` (= `content.sha256`). Quotes and line
numbers count in `.cache/secure-systems-lab-dsse.txt` (1145 lines, sha256
`b5fe6fb2…913247`, = `source_digest` in `requirements.yaml`), which
`render-source.py` builds from the archive. Neither file is committed.

**Status: passes 1-3 complete.** `reviewed_by` is empty on every artifact. A
person signs it; until then these are readable but not buildable-on.

## Source and rendering

The record is type `repo`; five files are specification text, read in full:
`protocol.md`, `envelope.md`, `envelope.proto`, `background.md` and
`hypothetical_signature_attack.ipynb`. `implementation/` and `governance/`
are not specification text and are not rendered. The four text files are
copied in place, byte for byte, except that ATX headings are renumbered in
place (`§1.4` is protocol.md "Test Vectors") and three column-0 list items are
indented one space; the notebook is rendered from its decoded cells. **The
notebook's cell outputs are not rendered** (the notebook is non-normative and
its outputs come from a random key). Line N of file i is rendering line
OFFSET + N, with OFFSET from `python3 -I distilled/render-source.py --offsets
.cache/secure-systems-lab-dsse.tar.gz`:

| file | section | offset | rendering lines |
|---|---|---|---|
| protocol.md | §1 | 3 | 1-186 |
| envelope.md | §2 | 191 | 189-277 |
| envelope.proto | §3 | 282 | 280-317 |
| background.md | §4 | 322 | 320-495 |
| hypothetical_signature_attack.ipynb | §5 | 500 (heading at L498, cell 0 marker at L501) | 498-1145 |

**36 BCP 14 keywords in the source, 36 in the requirement texts** (MUST 11,
SHOULD 9, REQUIRED 5, MAY 4, MUST NOT 3, OPTIONAL 2, SHOULD NOT 2;
bin/bcp14-count; protocol.md 10, envelope.md 10, envelope.proto 5,
background.md 11, notebook 0). No file declares a keyword convention;
capitalised keywords are read as BCP 14 (`requirements.yaml` `reconciliation`).

**Source defects: 20.** The canonical list SD-1 to SD-20 is in `normative.md`,
with a crosswalk to the pass-1 lane ids (SDC-n, SDP-n, DN-SD-n).

| kind | file | coverage |
|---|---|---|
| normative | normative.md | Every requirement text under §1-§5 as check-quotes markers over the rendering: 123 quotations in the text (100 carrying requirements, 23 context), the keyword declaration finding (none), the 7 inferred entries named, all 153 candidates named, and the 20 canonical source defects with 50 further quotations and a crosswalk. |
| requirements | requirements.yaml, inferred-candidates.yaml | 110 entries: 33 skeleton BCP 14 sentences, 7 split children, 48 promoted from candidates, 15 hunted keyword-less binding texts, 7 inferred (103 stated, 7 inferred; testable 54 yes, 36 partial, 20 no). All 36 keywords reconciled line by line as a bijection. All 153 candidates have a verdict (51 stated, in 48 entries as three pairs merge; 102 reject). |
| schema | schema/ | Source ships envelope.proto only: verbatim copy plus derived JSON Schema 2020-12 (Envelope, EnvelopeStrict), PAE ABNF and two stdlib checkers. 61 cases (25 accept, 36 reject, each rejected for its stated reason), 19 of 19 removal mutants and 12 of 12 insertion mutants flip a case; PAE: 17 build, 17 round-trip, 19 reject vectors, 20000 random and 1600 exhaustive injectivity cases. python-jsonschema 4.23.0 agrees on 54 of 61, the 7 being the contentEncoding rejects. |
| messages | messages.yaml | 9 messages with 28 fields, every message and field with a non-empty constrained_by (114 links to 57 distinct ids, all R-ids); 6 source-defect candidates (SD-1 to SD-6); 13 source silences. |
| protocol | protocol.yaml, protocol.md | 5 roles (1 inferred), 8 flows, 45 steps (8 inferred), 24 error paths (12 stated, 4 inferred, 8 unspecified), 11 source-defect candidates, 8 open issues, 7 out-of-scope items; 185 step links to 91 distinct requirement ids (33 of 33 skeleton) plus 48 error-path links; 160 quotations; one Mermaid diagram per flow. |
| state-machine | state-machine.yaml | **Applicable.** 2 machines: M1 (one signature) 12 states, 11 transitions (11 stated); M2 (a (t, n)-ENVELOPE) 15 states, 19 transitions (14 stated, 5 inferred); 60 transition links to 34 distinct ids; 8 candidates assessed (2 modelled); every trigger a listed event, simulated over 16 and 4080 inputs. |
| examples | examples/ | 13 verbatim fixtures (every fenced block of the source) with an independent second extractor; the one source test vector (protocol.md 1.4) recomputed byte-exact, P-256 / RFC 6979 self-tested on RFC 6979 A.2.5 (2 vectors); 17 PAE build vectors and 19 rejects; 61 envelope cases; reproduce.py runs 161 checks. |
| design-notes | design-notes.md | 40 rows against m-of-n at 656bac0 (10 adopt, 5 adapt, 4 reject, 10 constrains, 3 conflicts, 8 silent), 14 cross-checks with in-toto-envelope-v1, 16 open questions; 310 id citations of 103 distinct ids, 22 quotation markers, 14 foreign quotations. Decides nothing. |

## How to reproduce

```sh
python3 -I distilled/render-source.py .cache/secure-systems-lab-dsse.tar.gz .cache/secure-systems-lab-dsse.txt
bin/check-quotes records/community/secure-systems-lab-dsse --txt .cache/secure-systems-lab-dsse.txt
bin/check-locators records/community/secure-systems-lab-dsse
python3 -I -B distilled/examples/reproduce.py     # needs the archive in .cache/
python3 -I -B distilled/schema/check-envelope.derived.py
python3 -I -B distilled/schema/check-pae.derived.py
```

## Pass history

| pass | effort | what |
|---|---|---|
| 0 skeleton | script | bin/fx1-skeleton: 33 sentences, 153 candidates, verbatim layer |
| 1 extract | tiered | requirements, schema+examples+messages (smaller model), protocol+state-machine, design-notes (max) |
| 2 verify | max | mechanical checks first, then 27 defects fixed in artifacts, quotes re-proved, SD-18 to SD-20 added |
| 3 cross-check | tiered | candidate ids rewired to R-ids, ids qualified, counts recounted, summary.md and the topic note corrected |
| 4 human review | | `reviewed_by` empty |
