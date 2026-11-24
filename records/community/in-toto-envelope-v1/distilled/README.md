---
record: in-toto-envelope-v1
kind: index
title: "in-toto-envelope-v1 — distilled artifacts"
extracted: "2026-11-15"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

FX-1 full extraction of **in-toto Attestation Framework spec/v1/envelope.md**
at main commit `50bf017` (byte-identical to tag v1.2.0). Authoritative bytes:
`.cache/in-toto-envelope-v1.bin`, sha256 `c02c6588…5265d11` (= `content.sha256`).
Quotes and line numbers count in `.cache/in-toto-envelope-v1.txt` (110 lines,
sha256 `d4bdf93f…1659f42`, = `source_digest` in `requirements.yaml`), which
`render-source.py` builds from it: line N is line N of envelope.md, only the
six ATX headings renumbered (§1 Schema, §1.1 Alternative Envelope schemas, §2
Fields, §3 File naming convention, §4 Storage convention, §4.1 Examples).
Neither file is committed.

**Status: passes 1–3 complete.** `reviewed_by` is empty on every artifact. A
person signs it; until then these are readable but not buildable-on.

**30 BCP 14 keywords in the source, 30 in the requirement texts** (SHOULD 11,
MUST 10, SHOULD NOT 4, MAY 3, RECOMMENDED 1, REQUIRED 1). The file declares no
keyword convention; capitalised keywords are read as BCP 14, none occurs in
lowercase (`requirements.yaml` `reconciliation`).

**Pass-1 SD ids differ from the canonical ones.** Each pass-1 lane numbered
its own source defects. The canonical list is SD-1 to SD-15 in `normative.md`,
and its crosswalk maps the old numbers onto it.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | Every requirement text with source lines verbatim under §1-§4.1 as check-quotes markers over distilled/render-source.py's line-for-line rendering, the keyword declaration finding (none in this file), the preamble and link definitions as context, the 8 inferred entries named, and the canonical source-defect list SD-1 to SD-15 with a crosswalk to the lane ids in messages, protocol and design-notes. |
| requirements | requirements.yaml, inferred-candidates.yaml | 50 entries: 29 skeleton BCP 14 sentences (R-0009 split into 2 children), 7 promoted from candidates (R-0031 split into 2), 2 hunted keyword-less lead-ins, 8 inferred. All 30 BCP 14 keywords reconciled line by line as a bijection (bin/bcp14-count 30). All 10 candidates have a verdict (7 stated, 3 reject). DSSE v1.0, ITE-5, the Statement layer, the predicates directory and the in-toto KEYID definition are outside this source. |
| schema | schema/ | The source ships no schema. Derived only: envelope.derived.schema.json (JSON Schema 2020-12; generic and DSSE envelopes, signatures, payloadType, storage media type and file-name patterns) and a stdlib checker; 93 cases (32 accept, 61 reject, each for a named reason), every asserting keyword mutated (43 removals, each flips a case, 1 equivalent mutant reasoned); jsonschema 4.26 agrees on 83 of 93, the 10 being documented annotation and trailing-newline classes. |
| messages | messages.yaml | 8 messages (generic Envelope, Signature, DSSE-profile Envelope, the decoded Statement as referenced, the payloadType and storage media types, the file-name conventions) with 23 fields, every field with a non-empty constrained_by resolving to the right id; 3 referenced structures (Sigstore Bundle, COSE_Sign, COSE_Sign1); 5 source silences. |
| protocol | protocol.yaml, protocol.md | No exchange is defined; one-way store-and-forward only. 4 roles (storage inferred), 3 flows (produce, name and store, consume), 20 steps (2 inferred), 11 error paths (the source names none; 8 unspecified), one Mermaid diagram per flow in protocol.md; 73 constrained_by links to 48 ids; message names joined to messages.yaml. DSSE's own signing and verification are opaque steps. |
| examples | examples/ | 3 verbatim fixtures (the §4.1 media types, L94-96) with derived expected results, re-extracted from .cache/in-toto-envelope-v1.bin by two extractors in reproduce.py (43 checks); 93 derived accept/reject cases. The source prints no envelope, signature or test vector, so there is no external oracle. |
| design-notes | design-notes.md | 27 rows against m-of-n at 7c3c731 (5 adopt, 4 adapt, 3 reject, 7 constrains, 2 conflicts, 6 silent); MD-3 field by field (DSSE, COSE_Sign, KSA envelope) and where the source cuts against MD-3 and DEC-002; R-O-05 ordering; COSE_Sign as an option DEC-005 does not list; two conflicts with R-O-05 and SPEC-0001 §5.3 on export; post-quantum: the envelope is algorithm-silent; 15 open questions. Decides nothing. |
| state-machine | state-machine.yaml (evidence only) | **Not applicable.** No lifecycle: an Envelope is produced, stored and read once; nothing in the source updates, re-signs, supersedes, revokes or expires it. Of 26 lifecycle words (state, lifecycle, transition, status, revoke, expire, rotate, renew, update, valid, supersede, rollover and others) none occurs in the 110 lines, counted by script. The one process with an outcome, a consumer obtaining authenticated predicate information (§2 L54-55, §4 L87-88), is two operations in one sentence with no states and no fixed order: protocol.yaml F03, its order recorded as SD-3. Signature verification is DSSE v1.0's (§1 L8), not this source's. Evidence and census in distilled/state-machine.yaml. |
