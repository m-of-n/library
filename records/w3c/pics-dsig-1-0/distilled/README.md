---
record: pics-dsig-1-0
kind: index
title: "pics-dsig-1-0 — distilled artifacts"
extracted: "2026-11-12"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`), **`profile: partial`** — see `record.yaml`
`distillation.profile_reason` for what is not covered and why. One line per
artifact: what it covers, and what it does not.

**Source.** `.cache/pics-dsig-1-0.bin`, the W3C Recommendation HTML,
sha256 `69ecbc8314b767137281e6c3515bbb3a79fa2270434eae7cac18548c36eb261a`
(`content.sha256`). Every line number and quotation counts in its rendering
`.cache/pics-dsig-1-0.txt`, produced by `bin/render-w3c --ordinal`, sha256
`d9eafc9db7bd9a8b016c0d72ffd6d0c2c21f58ffafaec84e3e2a3cacdd7c2e94`.
Fixtures are taken from the HTML `<pre>` blocks, not the rendering.

**Locators.** The source has **no section numbers**. A `§7.3.4` here is a
*structural ordinal* the renderer assigned from the h2..h6 nesting, not a
number the W3C printed; prose locators carry the heading title beside it.
The source uses **no BCP 14 keywords** (`bin/bcp14-count` 0): every
requirement is `verb: none` or `kind: inferred`.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | every stated entry of requirements.yaml as a quotation marker in source order under its section; split children beside parents; inferred entries named in place; source defects SD-1 to SD-19 and SD-E |
| requirements | requirements.yaml | 318 entries: 108 promoted candidates, 111 binding texts the skeleton missed, 76 split children, 23 inferred (the verifier side, which the source never states as a procedure). All 170 candidates have a verdict (108 stated, 1 inferred, 61 rejected). Keywords 0 = 0 |
| schema | schema/ | the 3 source grammars verbatim (resinfo, field-list, sigblock); a derived recogniser (`check-grammar.derived.py`, 46 cases, 0 differing) and a mutation test (`mutate-grammar.derived.py`). Not covered: PICS 1.1 service-info `error` forms, RFC 1738 URL syntax |
| messages | messages.yaml | 14 messages and 63 fields: signature label, resinfo, sigblock, AttribInfo, Signature, SigData and keyholder tokens, canonical form rules C-01..C-14, equivalent standalone label rules E-01..E-08; findings F-01 to F-12 |
| examples | examples/ | all 27 `<pre>` blocks: 8 example fixtures, 16 structural templates, 3 grammars (in schema/); `reproduce.py` re-cuts each from the HTML (0 differing) and recomputes the Step 3 canonical form. No hash or signature is verifiable: the source prints no key, no signed bytes and not the hashed document |
| design-notes | design-notes.md | adopt / adapt / reject / constrains / conflicts / silent against m-of-n at d7f7f89 (37 rows); MD-3 / DEC-002 and where DSig cuts against option 5; R-O-05, R-M-07, R-M-12, DEC-005, DEC-007, R-I-01; 12 open questions |
| protocol | — | **not applicable**: see `distillation.not_applicable` |
| state-machine | — | **not covered** (`profile_reason`) |

## Passes

Recorded in `record.yaml` `distillation.passes`. A first launch of the three
judgement lanes ran below max effort (the effort was not set per agent and
was inherited from the session); its output was discarded unread by the
re-run, and the max-effort re-run started from fresh `bin/fx1-skeleton`
output.
