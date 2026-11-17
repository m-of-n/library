---
record: owasp-dsomm
kind: examples
title: "owasp-dsomm - examples and test vectors"
extracted: "2026-11-15"
reviewed_by: ""
---

# examples/

**Finding: the source's code examples are 3 fenced code blocks inside activity descriptions, and it has no
test vectors.** Its prose samples (the Sample steps and Sample concept lists, the e.g. lists) are text, carried where they stand by
`../requirements.yaml`, `../inferred-candidates.yaml` and `../normative.md`. Each code block is held here verbatim, cut by `schema/build.derived.py` from the decoded value of its YAML scalar
(the fence's indentation removed) and re-cut and compared byte for byte by `schema/check.derived.py`. The verify pass
(2026-11-16) added them: pass 1 recorded that the source had no examples at all.

| file | where (key path) | fence lines | expected result |
|---|---|---|---|
| `ex-01.verbatim.md` | Agentic AI / Guidance / Instructed load of security rules / description | L923-927 | None as a vector: an instruction-file fragment mapping two workflow steps to the file the assistant opens when that step begins, as the surrounding description explains. |
| `ex-02.verbatim.sh` | Agentic AI / Guidance / Dynamic load of security rules / description | L2226-2241 | Run with a JSON object on stdin: a prompt beginning /speckit.plan, /speckit.implement or /speckit.review prints one JSON object, hookSpecificOutput with hookEventName UserPromptSubmit and additionalContext set to the content of specs/threat-model.md, docs/secure-coding-rules.md or docs/security-review-checklist.md; any other prompt prints nothing and exits 0. check.derived.py runs all four cases (bash, jq). |
| `ex-03.verbatim.html` | Implementation / Application Hardening / Context-aware output encoding / description | L7295-7297 | No encoded output is given. The expectation is R-0146: the one template variable sits in four contexts (element content, a double-quoted attribute, a single-quoted script string, a script comment) and each needs its own encoding. |

Beyond these, the file is itself a set of 251 real instances (and 551 implementation items): those are the
fixtures for the schemas, and copying them here would put a second copy of the source's content in the repository.
`schema/check.derived.py` reads them from the pinned source and validates every one against
`../schema/activity.derived.schema.json`.

What else is held here is ours, marked `.derived.`: 14 instances the schemas must accept and 52 they must reject (missing
uuid, level outside 1-5, unknown key, dependsOn not a uuid, and others). Each file is
`{schema, expect, why, instance}`. All identifiers in them are made up.
