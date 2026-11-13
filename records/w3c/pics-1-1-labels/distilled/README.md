---
record: pics-1-1-labels
kind: index
title: "pics-1-1-labels — distilled artifacts"
extracted: "2026-11-12"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`), **`profile: partial`** — see `record.yaml`
`distillation.profile_reason` for what is not covered and why. One line per
artifact: what it covers, and what it does not.

**Source.** `.cache/pics-1-1-labels.bin`, the W3C Recommendation HTML,
sha256 `a1acf19869f6b8df9ab7387b6172fd0002960dd0f82983c82df614a0cbd8948d`
(`content.sha256`). Every line number and quotation counts in its rendering
`.cache/pics-1-1-labels.txt`, produced by `bin/render-w3c --ordinal`, sha256
`469de99e9845669cd4445879f7272d0513b8e94cd4760490ba3df408edba94f8`.
Fixtures are taken from the HTML `<pre>` blocks, not the rendering.

**Locators.** The source has **no section numbers**. A `§12.2` here is a
*structural ordinal* the renderer assigned from the h2..h6 nesting, not a
number the W3C printed; prose locators carry the heading title beside it.
The source uses **no BCP 14 keywords** (`bin/bcp14-count` 0): every
requirement is `verb: none` or `kind: inferred`.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | every stated entry of requirements.yaml as a quotation marker in source order under its section; split children beside parents; inferred entries named in place; source defects SD-1 to SD-23 and SD-E |
| requirements | requirements.yaml | 349 entries: 136 promoted candidates, 93 binding texts the skeleton missed (one per grammar production of §7, §11.3, §11.4, §12.2, the date rules, MIC rule, §13.1 special-form steps, §12.3 response rules, Appendix A steps), 97 split children, 23 inferred. All 202 candidates have a verdict (136 stated, 66 rejected). Keywords 0 = 0. Requirements of the HTTP and label-bureau sections are included although their flows are not modelled |
| schema | schema/ | the 4 source grammars verbatim (§7 labels, §11.3 HTTP request, §11.4 response headers, §12.2 bureau query); 3 derived ABNF files and an executing checker (`check-grammar.derived.py`, 288 checks, 0 failing, incl. 79 must-reject cases and 60 mutants); ambiguities A1 to A26 |
| messages | messages.yaml | 20 messages and 72 fields: label list, service-info, label, every option (long and short forms), ratings, extensions, error tokens, HTML META embedding, PICS-Label header, Protocol-Request, bureau query and response, MIC input, signature special form |
| examples | examples/ | all 19 examples as fixtures, byte-identical to their HTML `<pre>` blocks; `reproduce.py` (212 checks, 0 failing) parses each against the derived grammar; findings D1 to D10. The source prints no MD5 or signature value, so no vector is verifiable |
| design-notes | design-notes.md | adopt / adapt / reject / constrains / conflicts / silent against m-of-n at d7f7f89 (30 rows); MD-3 / DEC-002 and where PICS 1.1 cuts against option 5; the MIC and the signature special form against R-O-05 and R-M-07; R-I-01; 10 open questions |
| protocol | — | **not covered** (`profile_reason`); wire formats are in messages.yaml and schema/ |
| state-machine | — | **not covered** (`profile_reason`) |

## Passes

Recorded in `record.yaml` `distillation.passes`. A first launch of the three
judgement lanes ran below max effort (the effort was not set per agent and
was inherited from the session); its output was discarded unread by the
re-run, and the max-effort re-run started from fresh `bin/fx1-skeleton`
output.
